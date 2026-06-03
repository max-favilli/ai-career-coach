# AI Career Coach

A Claude Code plugin that turns Claude into your long-term career positioning partner — not a one-shot CV writer.

## What it does

Most people paste a job description into AI and get a generic CV back. This plugin does something different: it builds a deep understanding of your career, scores every job opportunity against your profile, coaches you through targeted gap interviews, and generates tailored CVs that tell the right story for each role. It also tells you when to **pass** — your time is more valuable than another application.

## Commands

| Command | What it does |
|---------|-------------|
| `/setup` | One-time onboarding. Creates your workspace, builds your career encyclopedia through an interactive interview. |
| `/dimensions` | Define the scoring criteria used to evaluate job descriptions against your profile. |
| `/jd` | Analyze a job description. Scores it on your dimensions, gives an honest recommendation, conducts a gap interview. |
| `/cv` | Craft a tailored CV for a role you've analyzed with `/jd`. Generates markdown, styled HTML, and PDF. |
| `/add-to-encyclopedia` | Add new career content — paste a CV, LinkedIn export, or career notes and it gets integrated. |

## Getting started

1. Install the plugin in your Claude Code workspace
2. Run `/setup` — it will walk you through everything interactively
3. When you find a job you're interested in, paste it with `/jd`
4. If the analysis says it's worth applying, run `/cv` to generate a tailored CV

## How it works

### The encyclopedia

The core of the system is your **career encyclopedia** — a structured document containing everything about your professional history: roles, achievements, technologies, skills (with honest proficiency levels), career aspirations, and key stories. The `/setup` command builds this through an interview, and `/add-to-encyclopedia` lets you expand it over time.

### Dimensions

Scoring dimensions define what matters to YOU in a job. The defaults cover hard skills, domain, leadership, culture, and career trajectory — but you can customize them. A senior engineer optimizing for technical depth will score jobs differently than a director optimizing for team scale.

### JD analysis

When you run `/jd`, the plugin:
- Parses the job description into structured sections
- Identifies the "persona" the company is looking for
- Scores the match on each of your dimensions
- Gives an honest recommendation (Strong match / Worth applying / Stretch / Pass)
- Conducts a gap interview to surface hidden experience and identify deal-breakers
- Saves everything to a log for tracking

### Tailored CVs

The `/cv` command doesn't just reshuffle bullet points. It selects the right **frame** for your experience based on what the JD is actually asking for — builder, enterprise leader, product owner, transformation driver — and tailors the headline, summary, bullet selection, and emphasis to match. It generates markdown, print-ready HTML, and PDF.

## Philosophy

- **Interview before crafting.** Every analysis starts with understanding, not output.
- **Honesty about fit.** The plugin tells you to pass when a role is wrong. That's a feature.
- **Never fabricate.** Strategic representation is OK. Lying is not.
- **Your voice, not corporate boilerplate.** The CV should sound like you, not a template.

## Requirements

- [Claude Code](https://claude.ai/code) CLI
- Node.js (optional, for automated PDF generation via `npx md-to-pdf`)
- A browser (fallback for PDF generation)

## Author

Built by [Max Favilli](https://linkedin.com/in/maxfavilli) — making AI work for people, not the other way around.

## License

MIT
