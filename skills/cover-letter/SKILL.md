---
name: cover-letter
description: Write a concise, truthful cover letter for a role that has already been analyzed. Use when the user asks for a cover letter, application letter, or letter of motivation for a specific opportunity.
---

# Cover Letter — Generate Tailored Cover Letter

Generate a short, compelling cover letter for a specific role after `jd` analysis.

## Workspace and invocation

Resolve career-file paths relative to the user's career workspace, never the installed plugin directory. Skill names below can be invoked as `$ai-career-coach:skill-name` in Codex or `/ai-career-coach:skill-name` in Claude Code; natural-language requests also work.

## Instructions

### Step 1: Load context

1. Read `encyclopedia/career-encyclopedia.md`. If missing or empty, tell the user to use the `setup` skill first and stop.
2. Use the analysis explicitly identified by the user or established in the current conversation. Otherwise, list JD analyses in `jd-analysis/`.
   - If only one exists, use it.
   - If multiple exist, ask which one. Use an interactive user-input tool with up to three likely analyses when available; otherwise ask directly.
   - If none exist, tell the user to use the `jd` skill first and stop.
3. Read the selected JD analysis. Resolve relevant interview gaps before drafting unless the user asks to proceed with confirmed facts only.

### Step 2: Determine the tone

Ask one question and wait for the answer. Use an interactive user-input tool when available; otherwise ask directly:

"What tone should the cover letter have?"
- Likely options: "Direct and confident" / "Conversational and personal" / "Formal and professional"

If the user already specified a tone, do not ask again.

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
- **Never fabricate.** Only reference confirmed experience in the encyclopedia. Exclude `[UNVERIFIED]` or contradictory claims until resolved. Do not invent personal enthusiasm, connections, metrics, or achievements.
- **Don't repeat the CV.** The cover letter explains WHY this role, not WHAT you did. The CV handles the what.
- **Use employer context accurately.** Reference a relevant sourced fact from the JD analysis when available. If employer research was unavailable, use the supplied posting and do not imply research was completed.

### Step 4: Present and iterate

Show the cover letter to the user. Ask: "How does this feel? Want me to adjust the tone, length, or emphasis?"

Iterate until they're satisfied.

### Step 5: Save

Save to `tailored-cvs/{Name}-cover-letter-{company}-{role-short}.md`. Create the directory if needed and sanitize filename components to exclude path separators and reserved characters. Preserve a different posting's file with a posting ID or date suffix; update the same application's file when iterating.

If the user wants it in a different format, also save as plain text (no markdown formatting) for easy pasting into application forms.
