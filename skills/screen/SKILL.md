---
name: screen
description: "Batch-screen LinkedIn job postings from URLs: scrape them, pre-filter against your profile and screening criteria, rank them, and log the verdicts. Use when: user pastes one or more LinkedIn job URLs and says 'screen these', 'add to screened jobs', or wants a quick fit read without a full /jd analysis."
---

# Screen — Batch-Screen LinkedIn Job Postings

Turn a list of LinkedIn job-posting URLs into scraped JD text and a ranked screening verdict, personalized from the user's career encyclopedia. This is a **pre-filter**, not a full analysis — postings that survive go on to `/jd`.

## Instructions

### Step 1: Collect the URLs

Gather the LinkedIn URLs from the conversation ($ARGUMENTS or pasted). De-duplicate. For a **single URL**, run the scraper with `--url` directly. For **multiple URLs**, write them to a file **in the session scratchpad or temp directory — never inside a cloud-synced project folder** (OneDrive/iCloud sync locks cause `PermissionError`), then pass that file path to the scraper.

### Step 2: Scrape

From the workspace root:

```
python scraper/linkedin_jd_scraper.py <urls-file> -o scraper/out
python scraper/linkedin_jd_scraper.py --url "<single-url>" -o scraper/out
```

(Requires `pip install requests beautifulsoup4`. If the script isn't at that path, locate it with Glob.)

**Pacing matters.** LinkedIn rate-limits aggressively. Keep the default `--delay`; for more than ~30 URLs raise it to 8–10 rather than splitting into rapid batches. The script backs off and retries on HTTP 429 — a slow run is normal, not stuck.

Output: `scraper/out/jobs.csv` (one row per posting) and `scraper/out/jobs/<job_id>.md` (full description per posting).

### Step 3: Check failures before screening

Rows that failed carry a reason in the CSV `error` column. **Always report which URLs did not come through and why** — never silently fill a gap with a plausible guess. Common cases:

- `no description found` — closed or login-gated posting; the user may need to paste it manually
- `HTTP 429` after retries — rate-limited; wait, then re-run only the failed URLs with a higher `--delay`
- `could not parse job id from URL` — not a job-posting link; flag it
- Empty `title`/`company` on every row — LinkedIn changed their CSS; the selector lists in `parse_job()` need updating

### Step 4: Load or derive the screening criteria

1. **If `screening-criteria.md` exists in the workspace root**, use it. It is the user's personal pre-filter: target roles and seniority, geography and language constraints, compensation floor, hard disqualifiers, and screening rules learned from past batches. Where it disagrees with the encyclopedia, **the encyclopedia wins**.
2. **If it doesn't exist**, derive the criteria from `encyclopedia/career-encyclopedia.md` and `dimensions.md`:
   - Target role types, titles and seniority level (and what would be a step down)
   - Location, remote and language constraints
   - Compensation floor, if recorded
   - Hard disqualifiers: required skills the encyclopedia records as absent, languages the user doesn't speak, geographies that don't work
   - The user's strongest, most differentiated credentials — the things a match should light up
   Then **offer to save the derived criteria to `screening-criteria.md`** so future screens are faster and the user can edit the file directly. If the workspace is a git repository with a public remote, add the file to `.gitignore` — it contains personal data.
3. If the encyclopedia is missing too, tell the user to run `/setup` first and stop.

### Step 5: Check for repeats

Before screening, grep `scraper/screening-log.md` and `jd-log.md` for each company/posting. A posting already screened or analyzed — including the same role reposted under a new job ID — gets flagged as a repeat with a pointer to the prior verdict, not re-screened from scratch. Suggest the user unsave repeats from LinkedIn.

### Step 6: Screen and rank

Produce a compact ranked table first: company, title, location, verdict (**strong / worth a look / skip**), one-line reason. Sort by genuine fit, not by how appealing the company sounds. If nothing in the batch is a good match, say so — don't manufacture a ranking.

Below the table, short notes on the **strong ones only**:

1. Where the user clearly matches, quoting the posting's specific requirement
2. Where they fall short — be blunt; a flattering screen is useless
3. Anything odd in the posting (vague scope, title/work mismatch, junior scope under a senior title, laundry-list requirements)
4. What an application would need to emphasize

For skips, one line each. Don't pad. Stated requirements are usually wish-lists — note a gap without treating it as fatal unless it is an entire "essential" section or a recorded hard disqualifier.

### Step 7: Log the batch

Append the batch to `scraper/screening-log.md`, following the existing format (create the file with a short header if missing): date, source, the ranked table or per-posting verdicts with reasons.

**If the batch produced a reusable lesson** — a new disqualifier pattern, a recurring wall, a sourcing signal worth reusing — record it in `screening-criteria.md` too. This is how screening gets sharper over time, the same way `/jd` enriches the encyclopedia.

### Step 8: Hand off

Recommend which postings (if any) should go to `/jd` for full analysis. Remind the user this was a pre-filter: scores here are estimates, and `/jd` verdicts have overturned screening verdicts in both directions before.
