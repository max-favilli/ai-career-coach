# AI Career Coach — Roadmap

## Phase 1: Core Plugin (MVP)

- [x] Project structure and folders
- [x] `/setup` — onboarding wizard (creates workspace, CLAUDE.md, encyclopedia interview)
- [x] `/dimensions` — define/refine scoring criteria
- [x] `/jd` — analyze job descriptions (parse, score, gap interview, log)
- [x] `/cv` — tailored CV generation (markdown, styled HTML, PDF)
- [x] `/add-to-encyclopedia` — import/add career content
- [x] CLAUDE.md template with behavioral instructions (interactive questions, table scoring)
- [x] JD log tracking (`jd-log.md`)
- [x] Cross-platform PDF generation (npx md-to-pdf → browser headless → manual fallback)
- [x] PDF conversion support (execution permissions are managed by the host)
- [x] `.claude-plugin/plugin.json` — plugin metadata with schema, validated
- [x] Plugin directory structure (`skills/` at root with YAML frontmatter)
- [x] Root `SKILL.md` with plugin overview
- [x] README.md
- [x] MIT License
- [x] ROADMAP.md
- [x] Git repo initialized
- [x] Published to GitHub (`max-favilli/ai-career-coach`)

## Codex support

- [x] Integrate upstream LinkedIn scraper, batch screening, and qualification-by-qualification JD matching
- [x] Add `.codex-plugin/plugin.json` alongside the original Claude package
- [x] Share all seven skills between hosts, with Codex discovery metadata
- [x] Use host-appropriate invocation and interactive questions
- [x] Preserve existing workspace instructions with managed `AGENTS.md` / `CLAUDE.md` sections
- [x] Resolve bundled scraper paths from the installed plugin and write output to the user workspace
- [x] Document installation, updates, optional dependencies, and privacy for both hosts
- [x] Run package validation and host discovery checks (Codex CLI 0.171.0; Claude Code 2.1.143)
- [ ] Complete the manual smoke tests in `CONTRIBUTING.md` in both hosts

## Phase 2: Testing & Polish

- [ ] Test `/setup` end-to-end in a fresh workspace
- [ ] Test `/add-to-encyclopedia` with existing encyclopedia import
- [ ] Test `/jd` → `/cv` full workflow
- [ ] Test PDF generation on Windows
- [ ] Test PDF generation on Mac
- [ ] Test PDF generation on Linux
- [ ] Test `/dimensions` create and refine flows
- [ ] Edge case: `/jd` without encyclopedia → clear error message
- [ ] Edge case: `/cv` without JD analysis → clear error message
- [ ] Edge case: `/setup` run twice → graceful handling
- [ ] Review all skill instructions for clarity and completeness

## Phase 3: Enhancements

- [x] `/cover-letter` — generate tailored cover letter based on JD analysis
- [x] `/jd` company research — quick web search before scoring for better context
- [x] Scoring anchors — calibration rules to prevent over-optimistic scoring (default to 5)
- [ ] `/status` — show overview (encyclopedia completeness, dimensions defined, JDs analyzed, CVs generated)
- [ ] `/jd` auto-detect duplicate JDs (already analyzed)
- [ ] `/cv` support multiple CV styles/templates
- [ ] JD log: add columns for interview dates, outcome tracking
- [ ] Encyclopedia: technology skills auto-suggest from parsed CVs
- [ ] Dimensions: pre-built dimension sets for common profiles (engineer, director, product manager)
- [x] `.claude-plugin/marketplace.json` for self-hosted distribution (also read by Codex)

## Phase 4: Community & Distribution

- [x] Submit to official Claude Code marketplace (Anthropic review) — submitted 2026-06-05, awaiting review
- [x] Write a blog post about the approach
- [x] Marketing plan with Reddit/HN calendar (MARKETING.md, gitignored)
- [x] r/ClaudeAI post
- [ ] Hacker News Show HN post
- [ ] r/ExperiencedDevs post
- [ ] r/jobsearch post
- [ ] r/resumes post
- [ ] r/careerguidance post
- [ ] r/ChatGPTCoding post
- [ ] Add screenshots/examples to README
- [ ] Gather community feedback
