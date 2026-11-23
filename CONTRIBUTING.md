# Contributing

AI Career Coach keeps one set of workflows for Claude Code and Codex. Edit `skills/<name>/SKILL.md` once for both hosts. Codex presentation metadata lives in each skill's `agents/openai.yaml`; plugin metadata lives in `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`. Keep the plugin name and release version aligned.

The existing `.claude-plugin/marketplace.json` is the shared installation catalog. Codex supports this legacy marketplace format, so a second catalog or duplicated skill tree is unnecessary.

## Automated checks

Use Python 3.10 or newer in a development virtual environment:

```bash
python3 -m venv .venv
. .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python scripts/validate_plugin.py
python -m unittest discover -s tests
```

CI runs the same checks on pushes and pull requests. They validate package structure, metadata, and references. They do not prove the quality of coaching responses, browser access, PDF rendering, or interaction behavior.

When Claude Code is installed, also run:

```bash
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

Install from the checkout using the README's development instructions and start a new session. Use a temporary workspace and synthetic career details for smoke tests; never add real career information or authenticated scraper output to a fixture or pull request.

## Manual smoke tests

Run these in both hosts. Use the skill picker or Codex `$ai-career-coach:skill-name` syntax; Claude plugin commands use `/ai-career-coach:skill-name`.

| Scenario | Expected result |
|---|---|
| Discover the plugin | All seven skills appear: setup, dimensions, screen, jd, cv, cover-letter, add-to-encyclopedia |
| Fresh setup with a sample CV | Workspace folders, an encyclopedia, and the current host's instruction file are created outside the plugin cache |
| Setup twice with existing custom instructions | Existing instructions, encyclopedia entries, dimensions, and log rows survive; one managed Career Coach section remains |
| Switch hosts in the same workspace | Each host can use the same encyclopedia and analyses; setup preserves the other host's instruction file |
| Add conflicting career details | Existing facts survive; contradictions are flagged for clarification rather than silently replaced |
| Create/refine dimensions | Weights and scoring anchors are saved, then used by JD analysis |
| JD without an encyclopedia | Explain the missing prerequisite and request setup; do not fabricate a profile |
| JD with an unknown qualification | Show qualification evidence; ask one question at a time; distinguish personal work from team oversight |
| JD with browsing unavailable | Analyze supplied text, disclose missing research, and avoid invented company facts |
| Batch-screen from a separate workspace | Locate the installed scraper; write results to the workspace; report failures and repeats |
| A failed scrape with an older Markdown result present | Inspect the current CSV error and request pasted text; never analyze stale output as a successful fetch |
| CV / cover letter without an analysis | Request or complete a JD analysis before drafting |
| CV / cover letter for a selected role | Use the selected analysis and confirmed profile details; preserve prior files and application statuses |
| PDF tool unavailable | Deliver Markdown and styled HTML with print instructions; do not claim a PDF exists |

Run real LinkedIn retrieval only when needed to check the integration; respect default pacing and stop on access restrictions. The scraper's network behavior is separate from the metadata checks. Check PDF output on each supported operating system before claiming that platform has been tested.

## Pull requests

Describe the user-visible change, how both hosts were checked, and any untested behavior. Keep new host support additive, preserve Max's authorship and existing contributors' history, and avoid changing unrelated coaching features in a packaging change.
