---
name: jd
description: "Analyze a job description against your career profile. Scores the match, gives an honest recommendation, and conducts a gap interview. Use when: user says 'analyze this JD', 'evaluate this job', 'is this role a good fit', pastes a job description, or provides a link to a LinkedIn job posting."
---

# JD — Analyze Job Description

Analyze a job description against the user's career encyclopedia. Parse, score, give an honest recommendation, and conduct a gap interview.

## Instructions

The user has provided a job description (in the conversation, as $ARGUMENTS, or will paste it) — either as text or as a link to the job posting. Analyze it against their career.

### Step 0: Acquire the JD text

If the input is a **LinkedIn job URL** (contains `linkedin.com/jobs/view/` or `currentJobId=`) instead of pasted text:

1. Run the bundled scraper from the workspace root:
   ```
   python scraper/linkedin_jd_scraper.py --url "<url>" -o scraper/out
   ```
   (Requires `pip install requests beautifulsoup4`. If the script isn't at that path, locate it with Glob.)
2. Read the scraped posting from `scraper/out/jobs/<job_id>.md` and use it as the JD text for all following steps. Record the source URL in the analysis.
3. **If the scrape fails or returns no description** (login-gated, closed, or rate-limited posting), say so explicitly and ask the user to paste the JD text. **Never analyze a posting from the URL slug or from memory.**

For a non-LinkedIn URL, try fetching the page; if the description can't be extracted cleanly, ask for a paste.

If the input is already pasted JD text, skip this step.

### Step 1: Load context

1. Read `encyclopedia/career-encyclopedia.md`. If it's missing or empty, tell the user to run `/setup` first and stop.
2. Read `dimensions.md`. If it's missing, use these defaults and tell the user "Using default dimensions. Run /dimensions to customize.":
   - Hard Skills Match
   - Domain Match
   - Leadership Match
   - Culture & Values Match
   - Career Trajectory Fit

### Step 2: Parse the JD

Parse the JD into structured sections:
- Role title, company, location, remote/hybrid/onsite
- Reporting line and team size (if mentioned)
- Key responsibilities (ranked by emphasis)
- Required skills / must-haves
- Nice-to-haves
- Red flags (unrealistic expectations, mismatched seniority, vague scope)
- Culture signals (from language, values, tone)
- Compensation (if stated)

### Step 2b: Quick company research

If the company name is identifiable from the JD, do a brief web search to understand:
- What the company does (product, service, industry)
- Company size and stage (startup, scale-up, enterprise)
- Funding status and financial health (if available)
- Recent news or notable facts
- Glassdoor/reputation signals (if easily found)

Summarize in 2-3 sentences at the top of the analysis. This provides context for more accurate scoring — especially for Culture & Values and Career Trajectory dimensions.

If the company is anonymous (via recruiter), skip this step and note "Company anonymous — no research possible."

### Step 3: Identify the persona

Identify the "persona" the JD is looking for — e.g., "hands-on engineering leader," "strategic IT director," "digital commerce platform owner," "startup CTO." This determines how to frame the user's experience if they proceed to `/cv`.

### Step 3b: Match every qualification, one by one — BEFORE scoring or judging shape

Do not decide fit from the title, the industry, or the role's "shape" (consulting, platform, internal IT…) until this step is done. Shape rules are heuristics; the qualification list is evidence.

1. **Extract every qualification** the JD states — each bullet under "Requirements", "Qualifications", "What we're looking for", "Must-have", "Preferred/Nice-to-have". Keep the JD's own wording. Note whether each is *required* or *preferred*, and whether it is phrased as an "or" list (any one item satisfies it) or as a conjunction.
2. **Match each one against the encyclopedia** and produce a table:

   | # | Qualification (JD wording) | Required / Preferred | Evidence from the encyclopedia | Verdict |
   |---|---|---|---|---|

   Verdicts: **Strong** (direct, proven evidence) · **Adjacent** (related experience, honest framing needed) · **Miss** (no evidence — never claim it) · **Unknown** (the encyclopedia is silent or ambiguous).
3. **Grill the user interactively on every Adjacent and Unknown item, one at a time**, using AskUserQuestion with 2–4 pre-baked options that describe plausible truthful answers (e.g. "Yes, strongly — with evidence", "Partly — my team did this under my leadership, not me personally", "No"). Ask one qualification per question. Do not batch. Update the table with the answers.
4. **Distinguish "led" from "did".** When the user's answer is "my people did this under my leadership", record it as *led, not performed* — claimable as leadership, never as hands-on skill.
5. Only then proceed to scoring. The dimension scores must be consistent with the table: a required *Miss* caps Hard Skills; a list that is mostly *Strong* cannot produce a "poor fit" on hard skills regardless of the role's shape.
6. Save the completed table in the analysis file (Step 7) and record any new facts the grilling surfaced in the encyclopedia (Step 6b).
7. **Exception — absolute disqualifiers:** if the user has defined an absolute disqualifier (for example a language they do not speak and will never claim) and the JD requires it, build the table but skip the grilling and go straight to a Pass, stating the disqualifier. Do not spend the user's time confirming strengths for a role they cannot take.

### Step 4: Score match

Score the match on each dimension from `dimensions.md` (each X/10).

**Scoring calibration:** Default to 5 when information is ambiguous or missing. Only score higher with clear evidence. A company that doesn't disclose salary is a 5, not a 9. A JD that doesn't mention team size is a 5 on leadership match.
- **9-10:** Exceptional match — direct, proven, deep experience
- **7-8:** Strong match — significant overlap, minor gaps
- **5-6:** Neutral or partial — some match, some unknowns
- **3-4:** Weak — meaningful gaps or misalignment
- **1-2:** Hard blocker — fundamental mismatch

**CRITICAL: ALWAYS present scores as a markdown table. Never use a list or any other format.**

Example format (use exactly this structure):

| Dimension | Score | Notes |
|---|---|---|
| Hard Skills Match | 4/10 | PHP/Laravel blocker. Architecture and integration patterns are strong. |
| Domain Match | 9/10 | Enterprise eCommerce / D2C — strongest domain. |
| Leadership Match | 7/10 | Right scope — mentor leads, own recruitment. |
| Culture & Values Match | 8/10 | Builder arena, fast-growing, agile. |
| Career Trajectory Fit | 7/10 | eCommerce + integration + AI — right direction. |

### Step 5: Give honest recommendation

Provide an overall recommendation. Be direct — the user's time is more valuable than another application:
- **Strong match** — Apply. Multiple dimensions align strongly.
- **Worth applying** — No hard blockers, enough alignment to warrant pursuing.
- **Stretch** — Significant gaps but could work with the right narrative.
- **Poor fit** — Hard blockers or fundamental misalignment. Pass.

If recommending Pass, clearly state the blockers.

### Step 6: Gap interview

If the recommendation is NOT a hard pass, conduct a gap interview. Ask 3-6 targeted questions to:
- Surface unlisted experience that matches JD requirements
- Gauge genuine interest in specific aspects of the role
- Identify deal-breakers (location, salary, culture, scope)
- Understand which career arc to emphasize

**CRITICAL:** Ask questions ONE AT A TIME using the AskUserQuestion tool with pre-baked answer options. Never dump all questions at once. Wait for each answer before asking the next.

After the gap interview, update the recommendation if answers changed the picture.

### Step 6b: Update the encyclopedia

**IMPORTANT:** If the gap interview surfaced NEW information about the user — skills they didn't mention, experience not in the encyclopedia, career preferences, deal-breakers — update `encyclopedia/career-encyclopedia.md` with the new discoveries. This is how the system gets smarter over time: every JD analysis enriches the user's profile.

Examples of what to add:
- "I actually did pre-sales at that job too" → add to the role's entry
- "I used Angular at my startup" → add to Technology Skills
- "I won't relocate to city X" → add to Career Aspirations / Location preferences
- "My max team size was 27" → add to the relevant role

Mark any unverified additions with `[UNVERIFIED]`.

### Step 7: Save the analysis

Save to `jd-analysis/{company}-{role-short}.md` using kebab-case naming. Include:
- Header with company, location, date, recommendation
- Scores with notes
- Key strengths and concerns
- Gap interview answers
- CV frame suggestion (if proceeding)

### Step 8: Update the JD log

Append a row to `jd-log.md`. If the file doesn't exist, create it with this header:

```markdown
# JD Analysis Log

| Date | Company | Role | Recommendation | Applied? | Notes |
|------|---------|------|----------------|----------|-------|
```

Append one row with the date, company, role title, recommendation, "—" for Applied (user updates manually), and a brief note.

### Step 9: Next steps

Do NOT write a CV. Tell the user: "Run `/cv` when you're ready to tailor a CV for this role."

If it was a Pass, just save and move on — no need to suggest /cv.
