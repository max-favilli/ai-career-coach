---
name: cv
description: "Craft a tailored CV for a specific role after JD analysis. Generates markdown, styled HTML, and PDF. Use when: user says 'write a CV', 'tailor my CV', 'create a resume for this role'."
---

# CV — Craft Tailored CV

Generate a tailored CV for a specific role after `/jd` analysis and gap interview are complete.

## Instructions

### Step 1: Load context

1. Read `encyclopedia/career-encyclopedia.md`. If missing, tell the user to run `/setup` first.
2. List JD analyses in `jd-analysis/`. 
   - If only one exists, use it.
   - If multiple exist, ask the user which one (use AskUserQuestion with the available analyses as options).
   - If none exist, tell the user to run `/jd` first.
3. Read the selected JD analysis. If it was a "Pass" recommendation, warn the user: "This JD was analyzed as a Pass. Are you sure you want to tailor a CV for it?"

### Step 2: Select the frame

Based on the JD persona identified in the analysis, select the right "frame" for the user's experience. Common frames:

- **Builder / Technical Leader** — emphasize greenfield builds, architecture, hands-on depth, technical decision-making
- **Enterprise / Strategic Leader** — emphasize organizational scale, budget, team size, stakeholder management, governance
- **Product / Digital Leader** — emphasize revenue impact, user growth, product thinking, digital marketing
- **Transformation Leader** — emphasize change management, modernization, crisis turnaround, culture building
- **Startup / CTO** — emphasize scrappiness, full-stack ownership, speed, founder mentality
- **Consulting / Practice Leader** — emphasize client delivery, pre-sales, multi-client management, practice growth

Hybrid frames are common — blend as needed based on what the JD is really asking for.

### Step 3: Write the tailored CV

Write a markdown CV with these sections:

**Header:**
- Name (from encyclopedia)
- Title line — tailored to the role persona (use a truthful functional title, not the JD's exact title if it doesn't match the user's actual title)
- Subtitle — 3-5 keywords that mirror the JD's priorities
- Location and contact info

**Summary:**
- 3-5 sentences in the user's voice
- Lead with what matters most to THIS role
- Include concrete proof points (numbers, scale, outcomes)

**Experience:**
- All relevant roles from the encyclopedia
- Lead bullets should directly mirror JD requirements
- Detailed for relevant roles, compressed for less relevant ones
- Side projects: include if they strengthen the narrative

**Technical Competencies:**
- Table format: Area | Detail
- Only claim what's true per the Technology Skills Truth Map in the encyclopedia
- Order rows by relevance to this JD (most relevant first)

**Education and Languages:**
- As recorded in encyclopedia

### Step 4: Representation rules

- Never fabricate experience or skills
- Frame oversight as oversight, not hands-on expertise
- Early career roles can be compressed or omitted if irrelevant
- Strategic representation is OK — emphasize what's relevant, compress what isn't
- Education: state what was studied and where, without specifying completion status

### Step 5: Save markdown

Save to `tailored-cvs/{Name}-cv-{company}-{role-short}.md` using the user's name from the encyclopedia.

### Step 6: Generate styled HTML

Create a styled HTML version with inline CSS optimized for printing. Use this base style:

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 11px; line-height: 1.45; color: #222; max-width: 800px; margin: 0 auto; padding: 20px 40px; }
  h1 { font-size: 22px; margin-bottom: 2px; color: #111; }
  h2 { font-size: 14px; color: #333; border-bottom: 1px solid #ccc; padding-bottom: 3px; margin-top: 16px; margin-bottom: 8px; }
  h3 { font-size: 12px; color: #222; margin-top: 12px; margin-bottom: 4px; }
  p { margin: 4px 0; }
  ul { margin: 4px 0 8px 0; padding-left: 18px; }
  li { margin-bottom: 3px; }
  li ul { margin-top: 2px; margin-bottom: 2px; }
  li ul li { margin-bottom: 1px; }
  hr { border: none; border-top: 1px solid #ddd; margin: 10px 0; }
  table { width: 100%; border-collapse: collapse; font-size: 10.5px; margin-top: 4px; }
  th { text-align: left; background: #f5f5f5; padding: 4px 8px; border: 1px solid #ddd; font-size: 10.5px; }
  td { padding: 4px 8px; border: 1px solid #ddd; vertical-align: top; }
  a { color: #1a5276; text-decoration: none; }
  strong { color: #111; }
  @media print { body { padding: 10px 20px; } }
</style>
</head>
<body>
<!-- CV content here, using HTML entities for special characters -->
</body>
</html>
```

Convert the markdown CV to HTML manually (don't use npx marked — write the HTML directly for control over formatting). Save to `tailored-cvs/{Name}-cv-{company}-{role-short}-styled.html`.

### Step 7: Generate PDF

Attempt PDF generation in this order:

1. **Try `npx md-to-pdf`:**
   ```
   npx md-to-pdf tailored-cvs/{Name}-cv-{company}-{role-short}.md --config-file none
   ```
   This works cross-platform if Node.js is installed.

2. **Try browser-based PDF (platform-dependent):**
   - **Windows:** `msedge --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="{output}" "file:///{input-html}"`
   - **Mac:** `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="{output}" "file:///{input-html}"`
   - **Linux:** `google-chrome --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="{output}" "file:///{input-html}"` or `chromium --headless ...`

3. **Fallback:** If all automated methods fail, tell the user: "PDF generation failed. Open the HTML file in your browser and press Ctrl+P / Cmd+P to save as PDF. The HTML is styled for clean printing."

Save PDF to `tailored-cvs/{Name}-cv-{company}-{role-short}.pdf`.

### Step 8: Present for review

Show the user the CV and highlight:
- What frame you chose and why
- What you emphasized vs. compressed
- What you omitted and why
- Any trade-offs or choices they might want to adjust

Ask if they want to make changes. Iterate until they're satisfied.

### Step 9: Update JD log

After the CV is finalized, ask the user: "Would you like me to mark this role as 'Applied' in the JD log?" If yes, update the corresponding row in `jd-log.md`.
