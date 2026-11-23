---
name: cv
description: Create a truthful, persona-targeted CV for a role that has already been analyzed, with Markdown and print-ready HTML plus PDF when local tooling permits. Use when the user asks to write or tailor a CV or resume for a specific opportunity.
---

# CV — Craft Tailored CV

Generate a tailored CV for a specific role after the `jd` analysis and gap interview are complete.

## Workspace and invocation

Resolve career-file paths relative to the user's career workspace, never the installed plugin directory. Skill names below can be invoked as `$ai-career-coach:skill-name` in Codex or `/ai-career-coach:skill-name` in Claude Code; natural-language requests also work.

## Instructions

### Step 1: Load context

1. Read `encyclopedia/career-encyclopedia.md`. If missing or empty, tell the user to use the `setup` skill first and stop.
2. Use the analysis explicitly identified by the user or established in the current conversation. Otherwise, list JD analyses in `jd-analysis/`.
   - If only one exists, use it.
   - If multiple exist, ask the user which one. Use an interactive user-input tool when available and show up to three likely analyses; otherwise ask directly.
   - If none exist, tell the user to use the `jd` skill first and stop.
3. Read the selected JD analysis. If the qualification or gap interview is incomplete, resolve relevant unknowns one question at a time before drafting, unless the user explicitly asks to proceed with confirmed facts only. If it recommends **Poor fit** (or an older **Pass**), briefly note the blockers and honor the user's explicit request to create a CV anyway.

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
- Exclude `[UNVERIFIED]` or contradictory claims until the user resolves them; missing metrics are not permission to invent numbers
- Frame oversight as oversight, not hands-on expertise
- Early career roles can be compressed or omitted if irrelevant
- Strategic representation is OK — emphasize what's relevant, compress what isn't
- Education: describe studies accurately; name an awarded degree only when completion is confirmed, and never imply graduation from attendance alone

### Step 5: Save markdown

Save to `tailored-cvs/{Name}-cv-{company}-{role-short}.md` using the user's name from the encyclopedia. Create the directory if needed. Sanitize filename components to exclude path separators and reserved characters. Keep one consistent basename across Markdown, HTML, and PDF. Preserve a different posting's files with a posting ID or date suffix; update files for this same application when iterating.

### Step 6: Generate styled HTML

Create a styled HTML version with inline CSS optimized for printing. Use this base style:

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Curriculum Vitae</title>
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

Convert the markdown CV to HTML manually (don't use npx marked — write the HTML directly for control over formatting). Escape document text and attribute values, use static HTML with no external scripts, fonts, or trackers, and preserve the Markdown content accurately. Save to `tailored-cvs/{Name}-cv-{company}-{role-short}-styled.html`.

### Step 7: Generate PDF

Prefer an already-installed Chromium-based browser so the PDF is generated from the styled HTML:

- **Windows:** Edge or Chrome in headless mode
- **macOS:** Chrome in headless mode
- **Linux:** Chrome or Chromium in headless mode

Pass the absolute HTML file URI and an absolute output path as safely quoted arguments. Use the browser's `--headless`, `--disable-gpu`, `--no-pdf-header-footer`, and `--print-to-pdf=...` options with an isolated temporary user-data directory to avoid interfering with the user's browser session. Follow the active client's approval and sandbox rules when executing local applications.

If no compatible browser is installed, check whether a local Markdown-to-PDF tool is already available. Do not download or install a package without the user's approval. If automation is unavailable or fails, retain the Markdown and HTML and tell the user to open the HTML in a browser and use Print → Save as PDF.

After generation, verify that the PDF was created or updated by this run, is non-empty, and has a plausible PDF file type. A stale PDF from a previous run does not count as success. Inspect rendered pages when local tools permit, checking for clipping or blank pages. Do not claim PDF success unless verification passes.

Save PDF to `tailored-cvs/{Name}-cv-{company}-{role-short}.pdf`.

### Step 8: Present for review

Show the user the CV and highlight:
- What frame you chose and why
- What you emphasized vs. compressed
- What you omitted and why
- Any trade-offs or choices they might want to adjust

Ask if they want to make changes. Iterate until they're satisfied.

### Step 9: Update JD log

Creating a CV does not mean the application was submitted. Preserve the corresponding row's Applied status in `jd-log.md`. Update it only when the user says they applied or explicitly requests that status change; preserve other rows and notes.
