---
name: jd
description: "Analyze a job description against your career profile. Scores the match, gives an honest recommendation, and conducts a gap interview. Use when: user says 'analyze this JD', 'evaluate this job', 'is this role a good fit', or pastes a job description."
---

# JD — Analyze Job Description

Analyze a job description against the user's career encyclopedia. Parse, score, give an honest recommendation, and conduct a gap interview.

## Instructions

The user has provided a job description (in the conversation, as $ARGUMENTS, or will paste it). Analyze it against their career.

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

### Step 3: Identify the persona

Identify the "persona" the JD is looking for — e.g., "hands-on engineering leader," "strategic IT director," "digital commerce platform owner," "startup CTO." This determines how to frame the user's experience if they proceed to `/cv`.

### Step 4: Score match

Score the match on each dimension from `dimensions.md` (each X/10).

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
