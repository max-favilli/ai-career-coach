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
- [x] `.claude/settings.json` with permission allowlist
- [x] `.claude-plugin/plugin.json` — plugin metadata with schema, validated
- [x] Plugin directory structure (`skills/` at root with YAML frontmatter)
- [x] Root `SKILL.md` with plugin overview
- [x] README.md
- [x] MIT License
- [x] ROADMAP.md
- [x] Git repo initialized
- [x] Published to GitHub (`max-favilli/ai-career-coach`)

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

- [ ] `/cover-letter` — generate tailored cover letter based on JD analysis
- [ ] `/status` — show overview (encyclopedia completeness, dimensions defined, JDs analyzed, CVs generated)
- [ ] `/jd` auto-detect duplicate JDs (already analyzed)
- [ ] `/cv` support multiple CV styles/templates
- [ ] JD log: add columns for interview dates, outcome tracking
- [ ] Encyclopedia: technology skills auto-suggest from parsed CVs
- [ ] Dimensions: pre-built dimension sets for common profiles (engineer, director, product manager)
- [ ] `marketplace.json` for self-hosted marketplace distribution

## Phase 4: Community & Distribution

- [ ] Submit to official Claude Code marketplace (Anthropic review)
- [ ] Write a blog post / LinkedIn article about the approach
- [ ] Add screenshots/examples to README
- [ ] Gather community feedback
