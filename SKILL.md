---
name: ai-career-coach
description: "Overview of the AI Career Coach plugin for building a persistent career profile, evaluating job fit, and creating truthful tailored applications."
---

# AI Career Coach

Your long-term career positioning partner. This plugin helps you:

1. **Build a career encyclopedia** — a structured source of truth about your professional history (`setup`)
2. **Define scoring dimensions** — customize how jobs are evaluated against your profile (`dimensions`)
3. **Analyze job descriptions** — parse, score, get honest recommendations, and conduct gap interviews (`jd`)
4. **Generate tailored applications** — persona-based CVs and cover letters (`cv`, `cover-letter`)
5. **Grow your profile over time** — integrate CVs, LinkedIn exports, and career notes (`add-to-encyclopedia`)
6. **Screen batches of opportunities** — fetch LinkedIn postings, rank likely matches, and record screening results (`screen`)

## Getting Started

Open a dedicated career workspace and ask to set up the career coach. In Codex, invoke `$ai-career-coach:setup`; in Claude Code, invoke `/ai-career-coach:setup`. The same seven skills support both clients and natural-language requests.

Setup creates `AGENTS.md` guidance for Codex or `CLAUDE.md` guidance for Claude, preserving existing instructions. Career files belong to the user's workspace, never the installed plugin directory. Read the relevant skill under `skills/` for its workflow.
