---
name: cover-letter
description: "Generate a tailored cover letter for a specific role after JD analysis. Use when: user says 'cover letter', 'write a cover letter', 'application letter', 'letter of motivation'."
---

# Cover Letter — Generate Tailored Cover Letter

Generate a short, compelling cover letter for a specific role after `/jd` analysis.

## Instructions

### Step 1: Load context

1. Read `encyclopedia/career-encyclopedia.md`. If missing, tell the user to run `/setup` first.
2. List JD analyses in `jd-analysis/`.
   - If only one exists, use it.
   - If multiple exist, ask the user which one (use AskUserQuestion with the available analyses as options).
   - If none exist, tell the user to run `/jd` first.
3. Read the selected JD analysis.

### Step 2: Determine the tone

Ask the user ONE question using AskUserQuestion:

"What tone should the cover letter have?"
- Options: "Direct and confident" / "Conversational and personal" / "Formal and professional" / "Short and punchy (3-4 sentences)"

### Step 3: Write the cover letter

Write a cover letter following these rules:

**Structure:**
- **Opening (1-2 sentences):** Why this role, why this company. NOT "I am writing to apply for..." — start with something that shows you understand what they need.
- **Body (2-3 short paragraphs):** Connect the user's most relevant experience to the JD's top priorities. Use concrete proof points from the encyclopedia — numbers, outcomes, scale. Focus on 2-3 things, not everything.
- **Close (1-2 sentences):** Forward-looking, confident, not needy.

**Rules:**
- **Keep it short.** Maximum one page. Ideally under 250 words. Hiring managers skim.
- **Use the user's voice.** Read the encyclopedia summary and career aspirations for tone. No corporate boilerplate.
- **Mirror the JD's language.** If they say "builder," use "builder." If they say "scale," use "scale."
- **Never fabricate.** Only reference experience that's in the encyclopedia.
- **Don't repeat the CV.** The cover letter explains WHY this role, not WHAT you did. The CV handles the what.
- **Show you researched the company.** Reference something specific about the company from the JD analysis (company research section).

### Step 4: Present and iterate

Show the cover letter to the user. Ask: "How does this feel? Want me to adjust the tone, length, or emphasis?"

Iterate until they're satisfied.

### Step 5: Save

Save to `tailored-cvs/{Name}-cover-letter-{company}-{role-short}.md`.

If the user wants it in a different format, also save as plain text (no markdown formatting) for easy pasting into application forms.
