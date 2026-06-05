# AI Career Coach

A Claude Code plugin that turns Claude into your long-term career positioning partner — not a one-shot CV writer.

## What it does

Most people paste a job description into AI and get a generic CV back. This plugin does something different: it builds a deep, persistent understanding of your career that **grows with every interaction**.

Every gap interview surfaces experience you forgot to mention. Every JD analysis reveals skills worth capturing. Every conversation adds to your career encyclopedia — so the 10th CV you generate is dramatically better than the first, because Claude knows things about your career that aren't on any single CV.

The plugin also tells you when to **pass** — your time is more valuable than another application.

### Use cases

1. **Analyze a job posting before applying** — Paste a JD, get an honest score across customizable dimensions (defaults: hard skills, domain, leadership, culture, career trajectory), and a clear recommendation: apply or pass. Stop wasting time on poor-fit roles.
2. **Surface hidden experience through gap interviews** — The interactive interview digs into your past and surfaces relevant experience you forgot to mention. "Oh right, I did pre-sales at that job too." Every discovery gets saved to your encyclopedia.
3. **Generate persona-targeted CVs** — The same career gets framed as "builder/CTO" for a startup, "SAP transformation leader" for enterprise, or "cloud modernization architect" for consulting — each truthful, each perfectly targeted to what the hiring manager is looking for.
4. **Track your entire job search** — Every JD analyzed is logged with date, company, recommendation, and application status. See your full pipeline at a glance.

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
3. **Launch Claude Code** in that folder (run `claude` in your terminal)
4. **Run `/setup`** — it walks you through everything interactively:
   - Creates the folder structure
   - Builds your career encyclopedia through an interview (you can paste an existing CV or LinkedIn export to speed this up)
   - Optionally defines your scoring dimensions
5. **Analyze a job** — paste a job description with `/jd`:
   - Scores the role against your profile across each dimension (hard skills, domain, leadership, culture, trajectory)
   - Gives an honest recommendation: apply, stretch, or pass
   - Conducts a gap interview to dig into your past experience that matches this specific JD
   - New discoveries get added to your encyclopedia — so the next analysis is even better
6. **Generate a tailored CV** — run `/cv` if the analysis says it's worth applying

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

The encyclopedia is the single source of truth. Every JD analysis and CV tailoring reads from it. **Crucially, it grows with every interaction:** gap interviews during `/jd` often surface experience you didn't think to include ("Oh right, I did pre-sales at that job too"), and those discoveries get added back to the encyclopedia. The more jobs you analyze, the more Claude knows about you, and the more precise every subsequent CV becomes.

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
- **Updates your encyclopedia** with anything new discovered during the interview (skills, experience, preferences you hadn't captured yet)
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

## Why it gets better over time

This is what makes the plugin different from a one-shot AI CV generator:

1. **JD #1:** You run `/setup`, paste your CV, answer 10 questions. The encyclopedia has the basics.
2. **JD #5:** Gap interviews have surfaced pre-sales experience you forgot, a side project with 1M users, and the fact that you provisioned cloud infrastructure yourself. All added to the encyclopedia.
3. **JD #15:** Claude knows your career so deeply that it can frame your experience as a "builder who brings order to complexity" for a startup, or an "SAP transformation leader" for an enterprise role, or a "cloud modernization architect" for a consulting firm — each version truthful, each perfectly targeted. The encyclopedia now contains insights that no single CV or LinkedIn profile ever captured.

The encyclopedia is the compounding asset. Every conversation makes it richer.

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
