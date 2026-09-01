#!/usr/bin/env python3
"""
linkedin_jd_scraper.py
Pull title, company, top-card metadata and the full "About the job" text for a
list of LinkedIn job-posting URLs.

It uses LinkedIn's public guest endpoint:
    https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/<jobId>
which serves the job card without a login for most public postings.

Usage
-----
    pip install requests beautifulsoup4
    python linkedin_jd_scraper.py urls.txt -o out
    python linkedin_jd_scraper.py --url https://www.linkedin.com/jobs/view/4012345678/

Input file: one URL per line. Blank lines and lines starting with # are ignored.

Output
------
    out/jobs.csv         one row per posting (opens cleanly in Excel)
    out/jobs/<id>.md     full description, one markdown file per posting
"""

import argparse
import csv
import html
import os
import random
import re
import sys
import time

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("Missing deps. Run:  pip install requests beautifulsoup4")


GUEST_ENDPOINT = "https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

JOB_ID_RE = re.compile(r"(?:jobs/view/|currentJobId=|jobPosting/)(\d+)")

CSV_FIELDS = [
    "job_id",
    "url",
    "title",
    "company",
    "company_url",
    "location",
    "posted",
    "applicants",
    "seniority_level",
    "employment_type",
    "job_function",
    "industries",
    "description",
    "error",
]


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def job_id_from_url(url: str):
    """Extract the numeric job id from any of LinkedIn's URL shapes."""
    m = JOB_ID_RE.search(url)
    if m:
        return m.group(1)
    # e.g. .../jobs/senior-engineer-at-acme-4012345678
    m = re.search(r"(\d{8,})", url)
    return m.group(1) if m else None


def pick(soup, selectors):
    """Return the first element matching any of the given CSS selectors."""
    for sel in selectors:
        el = soup.select_one(sel)
        if el is not None:
            return el
    return None


def text_of(el):
    if el is None:
        return ""
    return re.sub(r"\s+", " ", html.unescape(el.get_text(" ", strip=True))).strip()


def html_to_text(node):
    """Flatten LinkedIn's description markup into readable plain text."""
    if node is None:
        return ""
    for br in node.find_all("br"):
        br.replace_with("\n")
    for li in node.find_all("li"):
        li.insert(0, "- ")
    for tag in node.find_all(["p", "li", "ul", "ol", "div", "h1", "h2", "h3", "h4"]):
        tag.append("\n")

    text = html.unescape(node.get_text())
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = "\n".join(line.strip() for line in text.split("\n"))
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def fetch(job_id, session, cookie=None, retries=4):
    """GET the guest job card, backing off on 429/5xx."""
    url = GUEST_ENDPOINT.format(job_id=job_id)
    headers = dict(HEADERS)
    if cookie:
        headers["Cookie"] = cookie

    wait = 8.0
    last = None
    for attempt in range(retries):
        r = session.get(url, headers=headers, timeout=30)
        if r.status_code == 200:
            return r.text
        last = r.status_code
        if r.status_code in (429, 500, 502, 503):
            sleep_for = wait * (attempt + 1) + random.uniform(0, 3)
            print(f"    HTTP {r.status_code}, backing off {sleep_for:.0f}s", flush=True)
            time.sleep(sleep_for)
            continue
        break
    raise RuntimeError(f"HTTP {last}")


# --------------------------------------------------------------------------- #
# parsing
# --------------------------------------------------------------------------- #
def parse_job(page_html):
    soup = BeautifulSoup(page_html, "html.parser")
    rec = {k: "" for k in CSV_FIELDS}

    rec["title"] = text_of(
        pick(
            soup,
            [
                "h1.top-card-layout__title",
                "h2.top-card-layout__title",
                "h1.topcard__title",
                "h2.topcard__title",
                ".top-card-layout__title",
                ".topcard__title",
            ],
        )
    )

    company_el = pick(
        soup,
        [
            "a.topcard__org-name-link",
            "a.topcard__flavor--black-link",
            ".topcard__org-name-link",
            "span.topcard__flavor",
            ".top-card-layout__second-subline span",
        ],
    )
    rec["company"] = text_of(company_el)
    if company_el is not None and company_el.has_attr("href"):
        rec["company_url"] = company_el["href"].split("?")[0]

    rec["location"] = text_of(
        pick(soup, ["span.topcard__flavor--bullet", ".topcard__flavor--bullet"])
    )
    rec["posted"] = text_of(
        pick(soup, ["span.posted-time-ago__text", ".posted-time-ago__text"])
    )
    rec["applicants"] = text_of(
        pick(soup, ["span.num-applicants__caption", "figcaption.num-applicants__caption"])
    )

    # "Seniority level / Employment type / Job function / Industries" block
    key_map = {
        "seniority level": "seniority_level",
        "employment type": "employment_type",
        "job function": "job_function",
        "industries": "industries",
    }
    for li in soup.select("ul.description__job-criteria-list li, .description__job-criteria-item"):
        label = text_of(
            pick(li, ["h3.description__job-criteria-subheader", ".description__job-criteria-subheader", "h3"])
        ).lower().strip(":")
        value = text_of(
            pick(li, ["span.description__job-criteria-text", ".description__job-criteria-text", "span"])
        )
        if label in key_map and value:
            rec[key_map[label]] = value

    desc_node = pick(
        soup,
        [
            "div.show-more-less-html__markup",
            "div.description__text .show-more-less-html__markup",
            "section.description div.description__text",
            "div.description__text",
        ],
    )
    rec["description"] = html_to_text(desc_node)
    return rec


def to_markdown(rec):
    lines = [f"# {rec['title'] or 'Untitled role'}", ""]
    meta = [
        ("Company", rec["company"]),
        ("Location", rec["location"]),
        ("Posted", rec["posted"]),
        ("Applicants", rec["applicants"]),
        ("Seniority", rec["seniority_level"]),
        ("Employment type", rec["employment_type"]),
        ("Job function", rec["job_function"]),
        ("Industries", rec["industries"]),
        ("URL", rec["url"]),
    ]
    for label, value in meta:
        if value:
            lines.append(f"**{label}:** {value}  ")
    lines += ["", "## About the job", "", rec["description"] or "_(no description found)_"]
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def read_urls(path):
    urls = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                urls.append(line.split(",")[0].strip().strip('"'))
    return urls


def main():
    ap = argparse.ArgumentParser(description="Scrape LinkedIn job descriptions.")
    ap.add_argument("input", nargs="?", help="text file with one job URL per line")
    ap.add_argument("--url", action="append", default=[], help="a single URL (repeatable)")
    ap.add_argument("-o", "--out", default="out", help="output directory (default: out)")
    ap.add_argument("--delay", type=float, default=4.0, help="base seconds between requests")
    ap.add_argument("--cookie", default=os.environ.get("LI_COOKIE", ""),
                    help="raw Cookie header, e.g. 'li_at=...' — only needed for postings "
                         "that the guest endpoint won't serve")
    args = ap.parse_args()

    urls = list(args.url)
    if args.input:
        urls += read_urls(args.input)
    if not urls:
        ap.error("give me an input file or at least one --url")

    # de-dupe, preserve order
    seen, ordered = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u)
            ordered.append(u)

    jobs_dir = os.path.join(args.out, "jobs")
    os.makedirs(jobs_dir, exist_ok=True)
    csv_path = os.path.join(args.out, "jobs.csv")

    session = requests.Session()
    rows, failures = [], 0

    for i, url in enumerate(ordered, 1):
        job_id = job_id_from_url(url)
        print(f"[{i}/{len(ordered)}] {job_id or '?'}  {url[:70]}", flush=True)

        rec = {k: "" for k in CSV_FIELDS}
        rec["url"], rec["job_id"] = url, job_id or ""

        if not job_id:
            rec["error"] = "could not parse job id from URL"
            failures += 1
        else:
            try:
                rec.update(parse_job(fetch(job_id, session, args.cookie or None)))
                rec["url"], rec["job_id"] = url, job_id
                if not rec["description"]:
                    rec["error"] = "no description found (login-gated or closed posting?)"
                    failures += 1
                else:
                    fname = os.path.join(jobs_dir, f"{job_id}.md")
                    with open(fname, "w", encoding="utf-8") as fh:
                        fh.write(to_markdown(rec))
                    print(f"    ok — {rec['company'] or '?'} — {len(rec['description'])} chars",
                          flush=True)
            except Exception as exc:
                rec["error"] = str(exc)
                failures += 1
                print(f"    failed: {exc}", flush=True)

        rows.append(rec)
        if i < len(ordered):
            time.sleep(args.delay + random.uniform(0, args.delay * 0.6))

    with open(csv_path, "w", newline="", encoding="utf-8-sig") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nDone. {len(rows) - failures}/{len(rows)} scraped.")
    print(f"  CSV:      {csv_path}")
    print(f"  Markdown: {jobs_dir}/")
    if failures:
        print("  Check the 'error' column for the ones that failed.")


if __name__ == "__main__":
    main()
