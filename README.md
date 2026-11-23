# AI Career Coach

A plugin for **Claude Code and Codex** that becomes your long-term career positioning partner.

It builds a persistent career encyclopedia that grows through job analyses and gap interviews. Applications become more precise as you capture more of your experience, and honest fit assessments help you decide when to apply or pass.

## What it does

1. **Evaluates opportunities before you invest time.** Parse a job description, research the employer, match every qualification against your experience, and score fit across customizable dimensions.
2. **Surfaces experience you forgot to mention.** One-question-at-a-time interviews uncover relevant skills, stories, outcomes, and preferences, then save confirmed discoveries to your encyclopedia.
3. **Creates persona-targeted applications.** Frame the same truthful career for a startup, enterprise, or consulting role without inventing experience.
4. **Screens and tracks your search.** Batch-screen LinkedIn postings, identify promising roles, and keep analysis and screening logs.

## Install

Choose your host. Both use the same skills and career files; install the plugin once per host.

### Claude Code

Install [Claude Code](https://claude.ai/code), then run:

```bash
claude plugin marketplace add max-favilli/ai-career-coach
claude plugin install ai-career-coach@ai-career-coach-marketplace
```

Start a new session and use `/ai-career-coach:setup`. Plugin commands are namespaced; local standalone skills may also appear as `/setup`.

### Codex

Use a current [Codex](https://developers.openai.com/codex/) client with plugin support. With the Codex CLI:

```bash
codex plugin marketplace add max-favilli/ai-career-coach
codex plugin add ai-career-coach@ai-career-coach-marketplace
```

Start a new Codex session and select **AI Career Coach** in the skill picker, or ask, “Set up my career coach.” The workflows also support explicit `$ai-career-coach:setup`, `$ai-career-coach:jd`, and the other skill names below. If the picker shows qualified names, select the entry belonging to this plugin.

Codex reads `.codex-plugin/plugin.json` and the existing `.claude-plugin/marketplace.json` through its legacy marketplace support. There is no separate skill copy to keep in sync. See OpenAI's [plugin packaging documentation](https://developers.openai.com/plugins/build/plugins).

If `codex plugin add` is unavailable in your client version, register the marketplace with `codex plugin marketplace add`, then install **AI Career Coach** from that source in the desktop app's plugin browser. Restart the app and start a new chat after installation or updates.

The commands above install the repository's default branch. To test an unmerged contribution, use the local checkout instructions under **Development**.

### Optional tools

Core coaching works with text and local files. Employer research needs browsing; when unavailable, the analysis records that limitation.

LinkedIn URL screening uses the bundled Python scraper and requires Python 3 with `requests` and `beautifulsoup4`. Install these in a virtual environment if you want this feature:

```bash
python3 -m venv .venv
# macOS / Linux
. .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install requests beautifulsoup4
```

Use that environment's Python for scraping. Public postings may still be unavailable or rate-limited; paste the job description when retrieval fails. The plugin does not need a LinkedIn login for public guest-endpoint requests.

PDF output uses installed local conversion tools when available. Otherwise, open the generated styled HTML in a browser and print to PDF. Node.js is needed only for a Node-based conversion fallback.

## Getting started

Open a dedicated job-search folder in your chosen host, separate from the plugin checkout or installation directory:

```bash
mkdir my-job-search
cd my-job-search
# Launch either host:
# claude
# codex
```

1. Run **setup** with your CV, LinkedIn export, career summary, or a request for a guided interview. It creates the workspace and builds your encyclopedia.
2. Define your **dimensions**: the criteria and weights that matter to your next role.
3. Use **screen** for a batch of LinkedIn URLs, or **jd** for a detailed analysis of one posting.
4. Use **cv** and **cover-letter** for a role you have analyzed and want to pursue.

Setup adds a managed Career Coach section to `AGENTS.md` in Codex or `CLAUDE.md` in Claude Code. It preserves existing instructions and career files. Run setup once in each host if you use both with the same workspace.

## Skills

| Workflow | Codex | Claude Code |
|---|---|---|
| Initialize the workspace and build your profile | `$ai-career-coach:setup` | `/ai-career-coach:setup` |
| Define or refine scoring criteria | `$ai-career-coach:dimensions` | `/ai-career-coach:dimensions` |
| Batch-screen LinkedIn job postings | `$ai-career-coach:screen` | `/ai-career-coach:screen` |
| Analyze a role and interview for gaps | `$ai-career-coach:jd` | `/ai-career-coach:jd` |
| Create a tailored CV | `$ai-career-coach:cv` | `/ai-career-coach:cv` |
| Write a concise cover letter | `$ai-career-coach:cover-letter` | `/ai-career-coach:cover-letter` |
| Add career information to your profile | `$ai-career-coach:add-to-encyclopedia` | `/ai-career-coach:add-to-encyclopedia` |

Natural-language requests work in both hosts. Select the plugin's skill explicitly if another installed skill has the same name.

## How it works

### Career encyclopedia

`encyclopedia/career-encyclopedia.md` is the source of truth: roles, achievements, technologies, honest proficiency levels, education, aspirations, constraints, and key stories. Every analysis reads it. Confirmed discoveries from gap interviews are saved back to it; uncertain or contradictory details are marked `[UNVERIFIED]` and excluded from application claims until clarified.

### Scoring dimensions

| Default dimension | What it measures |
|---|---|
| **Hard Skills Match** | Job requirements compared with proven skills |
| **Domain Match** | Familiarity with the industry and business model |
| **Leadership Match** | Scope, seniority, and organizational complexity |
| **Culture & Values Match** | Employer signals compared with your preferences |
| **Career Trajectory Fit** | Whether the role advances your goals |

You can adjust the dimensions and their weights. Missing information receives a neutral score, not an optimistic assumption. Absolute disqualifiers remain visible even when the overall score is strong.

### Screening and analysis

**screen** retrieves LinkedIn postings, reports retrieval failures, applies your criteria, flags repeats, and ranks the opportunities. Promising roles then go to **jd** for a full assessment.

**jd** matches each qualification to evidence before judging fit. It distinguishes required and preferred qualifications, asks about unknown or adjacent experience one question at a time, and separates hands-on work from leadership oversight. It saves the qualification table, dimension scores, recommendation, and sources, then updates `jd-log.md`.

### Tailored applications

**cv** selects a truthful frame based on the analyzed role: builder, enterprise leader, product leader, transformation leader, startup CTO, or consulting leader. It tailors the headline, summary, bullets, and emphasis while preserving the facts.

The output includes Markdown and print-ready HTML. PDF generation is attempted when local tooling permits; success is reported only after the file has been verified. **cover-letter** uses the same evidence to write a concise letter in your voice.

## Workspace structure

```text
my-job-search/
├── AGENTS.md                         # Codex guidance, when set up in Codex
├── CLAUDE.md                         # Claude guidance, when set up in Claude
├── dimensions.md
├── screening-criteria.md             # Optional personal screening rules
├── jd-log.md
├── encyclopedia/
│   └── career-encyclopedia.md
├── jd-analysis/
│   └── {company}-{role}.md
├── tailored-cvs/
│   ├── {Name}-cv-{company}-{role}.md
│   ├── {Name}-cv-{company}-{role}-styled.html
│   ├── {Name}-cv-{company}-{role}.pdf   # When PDF generation succeeds
│   └── {Name}-cover-letter-{company}-{role}.md
└── scraper/
    ├── screening-log.md
    └── out/                          # Retrieved job postings and CSV
```

The scraper code stays in the installed plugin; its output belongs to your workspace. Keep career data private. See [Privacy](PRIVACY.md) for host processing and network behavior.

## Development

Clone this repository and check out the branch you want to test:

```bash
git clone https://github.com/max-favilli/ai-career-coach.git
cd ai-career-coach
```

Register the checkout in the host you are testing:

```bash
# Codex
codex plugin marketplace add .
codex plugin add ai-career-coach@ai-career-coach-marketplace

# Claude Code
claude plugin marketplace add .
claude plugin install ai-career-coach@ai-career-coach-marketplace
```

If this marketplace name is already registered from another source, use that host's marketplace management commands to remove the old registration before adding the local checkout. Installing a plugin copies it into a cache; refresh/reinstall after edits and start a new session. For Claude, `claude --plugin-dir /absolute/path/to/ai-career-coach` also loads the checkout directly for a development session.

Run the repository checks:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_plugin.py
python3 -m unittest discover -s tests
```

See [Contributing](CONTRIBUTING.md) for the manual smoke-test checklist and the limits of automated validation.

## Principles

Interview before crafting. Be honest about fit. Never fabricate. Preserve the user's voice. Distinguish hands-on skill, working knowledge, oversight, and historical experience. Ask one coaching question at a time.

## Author

Built by [Max Favilli](https://linkedin.com/in/maxfavilli) — making AI work for people, not the other way around.

## License

MIT
