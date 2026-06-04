# AI Career Coach

A Claude Code plugin that turns Claude into your long-term career positioning partner — not a one-shot CV writer.

## What it does

Most people paste a job description into AI and get a generic CV back. This plugin does something different: it builds a deep understanding of your career, scores every job opportunity against your profile, coaches you through targeted gap interviews, and generates tailored CVs that tell the right story for each role. It also tells you when to **pass** — your time is more valuable than another application.

## Installation

### From the marketplace

```bash
# Add the marketplace
claude plugin marketplace add max-favilli/ai-career-coach

# Install the plugin
claude plugin install ai-career-coach
```

### From source (for development)

```bash
git clone https://github.com/max-favilli/ai-career-coach.git
cd ai-career-coach
# Skills in .claude/skills/ are loaded automatically when you open Claude Code in this folder
```

## Getting started

1. **Install the plugin** using the commands above
2. **Create a workspace folder** for your job search (e.g. `mkdir my-job-search && cd my-job-search`)
3. **Run `/setup`** — it walks you through everything interactively:
   - Creates the folder structure
   - Builds your career encyclopedia through an interview (you can paste an existing CV or LinkedIn export to speed this up)
   - Optionally defines your scoring dimensions
4. **Analyze a job** — paste a job description with `/jd`
5. **Generate a tailored CV** — run `/cv` if the analysis says it's worth applying

## Commands

| Command | What it does |
|---------|-------------|
| `/setup` | One-time onboarding. Creates your workspace, builds your career encyclopedia through an interactive interview. |
| `/dimensions` | Define the scoring criteria used to evaluate job descriptions against your profile. |
| `/jd` | Analyze a job description. Scores it on your dimensions, gives an honest recommendation, conducts a gap interview. |
| `/cv` | Craft a tailored CV for a role you've analyzed with `/jd`. Generates markdown, styled HTML, and PDF. |
| `/add-to-encyclopedia` | Add new career content — paste a CV, LinkedIn export, or career notes and it gets integrated. |

## How it works

### The encyclopedia

The core of the system is your **career encyclopedia** — a structured document containing everything about your professional history: roles, achievements, technologies, skills (with honest proficiency levels), career aspirations, and key stories. The `/setup` command builds this through an interactive interview, and `/add-to-encyclopedia` lets you expand it over time.

The encyclopedia is the single source of truth. Every JD analysis and CV tailoring reads from it. The richer it is, the better the output.

### Dimensions

Scoring dimensions define what matters to YOU in a job. The defaults are:

| Dimension | What it measures |
|-----------|-----------------|
| **Hard Skills Match** | How well the JD's technical requirements overlap with your proven skills |
| **Domain Match** | Your familiarity with the industry and business model |
| **Leadership Match** | Whether the role's scope matches your leadership experience |
| **Culture & Values** | Company culture signals vs. what energizes you |
| **Career Trajectory** | Whether this role moves you toward your stated career goals |

You can customize weights, add dimensions, or remove ones that don't matter to you.

### JD analysis

When you run `/jd`, the plugin:
- Parses the job description into structured sections
- Identifies the "persona" the company is looking for
- Scores the match on each of your dimensions (presented as a table)
- Gives an honest recommendation: **Strong match** / **Worth applying** / **Stretch** / **Pass**
- Conducts a gap interview — one question at a time with pre-baked answer options — to surface hidden experience and identify deal-breakers
- Saves the analysis and appends to a running log (`jd-log.md`)

### Tailored CVs

The `/cv` command doesn't just reshuffle bullet points. It selects the right **frame** for your experience based on what the JD is actually asking for:

- **Builder / Technical Leader** — greenfield builds, architecture, hands-on depth
- **Enterprise / Strategic Leader** — scale, budget, team size, stakeholder management
- **Product / Digital Leader** — revenue impact, user growth, product thinking
- **Transformation Leader** — change management, modernization, crisis turnaround
- **Startup / CTO** — full-stack ownership, speed, founder mentality

It tailors the headline, summary, bullet selection, and emphasis to match. Output: markdown, print-ready styled HTML, and PDF.

## Workspace structure

After `/setup`, your workspace looks like this:

```
my-job-search/
├── CLAUDE.md                    # Behavioral instructions (created by /setup)
├── dimensions.md                # Your scoring criteria
├── jd-log.md                    # Running log of all analyzed JDs
├── encyclopedia/
│   └── career-encyclopedia.md   # Your career source of truth
├── jd-analysis/
│   └── {company}-{role}.md      # One file per analyzed JD
└── tailored-cvs/
    ├── {Name}-cv-{company}.md
    ├── {Name}-cv-{company}-styled.html
    └── {Name}-cv-{company}.pdf
```

## Philosophy

- **Interview before crafting.** Every analysis starts with understanding, not output.
- **Honesty about fit.** The plugin tells you to pass when a role is wrong. That's a feature.
- **Never fabricate.** Strategic representation is OK. Lying is not.
- **Your voice, not corporate boilerplate.** The CV should sound like you, not a template.
- **One question at a time.** All interactions use interactive questions with pre-baked options. No walls of text.

## Requirements

- [Claude Code](https://claude.ai/code) CLI
- Node.js (optional, for automated PDF generation via `npx md-to-pdf`)
- A browser (fallback for PDF generation — the styled HTML prints cleanly)

## Author

Built by [Max Favilli](https://linkedin.com/in/maxfavilli) — making AI work for people, not the other way around.

## License

MIT
