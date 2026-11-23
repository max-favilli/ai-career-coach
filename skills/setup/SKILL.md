---
name: setup
description: Set up the AI Career Coach workspace and build a persistent career encyclopedia from an existing CV, LinkedIn export, career summary, or guided interview. Use when the user asks to set up, initialize, onboard, or get started with the career coach.
---

# Career Coach Setup

Create the workspace structure, add project guidance for the active client, and build the user's career encyclopedia.

## Workspace and invocation

Work in the user's career workspace, never in the installed plugin directory. Resolve all career-file paths relative to that workspace. If the current folder is the plugin source or installation, ask for a career workspace before saving personal information.

Skill names below can be invoked as `$ai-career-coach:skill-name` in Codex or `/ai-career-coach:skill-name` in Claude Code. Natural-language requests work in either client.

## Interaction

Ask one question at a time and wait for the answer. When an interactive user-input tool is available, use it with two or three mutually exclusive likely answers; otherwise ask the question directly in chat. Free-text answers must always remain possible.

## 1. Check the current state

Select `AGENTS.md` for Codex or `CLAUDE.md` for Claude. If the active client cannot be determined, ask which instruction file the user wants. Read that file and `encyclopedia/career-encyclopedia.md` if they exist.

- If the selected instruction file already contains the managed Career Coach block shown below, update only that block as needed. An unchanged block requires no rewrite.
- If an encyclopedia already exists, preserve it. Offer to enrich it through the clarification interview instead of starting over.
- Preserve unrelated instructions in either file. Existing unmarked Career Coach instructions also remain intact unless the user requests migration; avoid appending a conflicting duplicate and explain any conflict that prevents adding guidance.

## 2. Create the workspace

Create these directories if needed:

- `encyclopedia/`
- `jd-analysis/`
- `tailored-cvs/`

Create or update only the text between the markers below in the selected root instruction file. Preserve all content outside the markers. If there is no block, append it; if the file does not exist, create it. If markers are incomplete or duplicated, leave that file unchanged and explain the issue rather than guessing which content to replace. Keep the other client's instruction file unchanged unless the user requests both.

```markdown
<!-- AI CAREER COACH:START -->
# Career Coach Command Center

This workspace is a long-term job-search system. Act as the user's career positioning partner.

## Core principles

1. Never fabricate experience, skills, dates, qualifications, or results. Represent verified facts strategically and truthfully.
2. Preserve the user's voice and avoid generic corporate language.
3. Treat `encyclopedia/career-encyclopedia.md` as the career source of truth and read it before career-coaching work.
4. Interview before crafting an application for a new job description.
5. Be candid when a role is a poor fit.

## Interaction

- Ask one coaching or interview question at a time.
- When an interactive user-input tool is available, provide two or three likely options while allowing free text.
- Wait for the user's answer before continuing the interview.

## Scoring

Present job-fit scores as a Markdown table with `Dimension`, `Score`, and `Notes` columns, followed by the recommendation and key concerns.

## Files

- `encyclopedia/career-encyclopedia.md` — career source of truth
- `dimensions.md` — scoring criteria
- `jd-analysis/` — saved job analyses
- `jd-log.md` — job-analysis history
- `tailored-cvs/` — generated CVs and cover letters
- `screening-criteria.md` — optional personal screening rules
- `scraper/screening-log.md` — batch-screening history
- `scraper/out/` — fetched job descriptions

## Skills

Use `$ai-career-coach:skill-name` in Codex or `/ai-career-coach:skill-name` in Claude Code; natural-language requests also work.

- `setup` — onboarding
- `dimensions` — define scoring criteria
- `screen` — screen LinkedIn job postings
- `jd` — analyze a job description
- `cv` — create a tailored CV
- `cover-letter` — create a cover letter
- `add-to-encyclopedia` — add career information

## Representation rules

- Distinguish hands-on expertise, working knowledge, oversight, and historical experience.
- Approximate dates are acceptable only when labeled approximate.
- Do not imply that education was completed unless the source of truth confirms it.
<!-- AI CAREER COACH:END -->
```

## 3. Gather source material

Use source material already supplied in the conversation. Otherwise, ask: "Do you have an existing CV, LinkedIn export, or career summary I can start from?"

Likely options are:

- "Yes, I'll attach or paste it"
- "Yes, I have a file path"
- "No, interview me from scratch"

If the user supplies content, parse it into the encyclopedia structure below, but do not save a mere reformatted copy. Clarify missing, vague, contradictory, or weak areas first.

For each role, probe useful gaps such as dates, scope, team size, strongest achievement, measurable impact, technologies, and reason for leaving. For skills, establish whether the experience is deep hands-on, working knowledge, oversight, or historical. Always cover side projects, education, and career aspirations when the source does not.

If starting from scratch, work through:

1. Personal details: name, email, location, and languages.
2. Education: subject, institution, dates, and confirmed completion status.
3. Career timeline: company, title, dates, location, achievements, scope, team size, technologies, and reason for leaving for each role.
4. Side projects, entrepreneurship, open source, and communities.
5. Technology skills and honest proficiency.
6. Career aspirations: desired role, energizers, drains, compensation floor, location/remote preferences, and company stage.

Continue until the source is materially clearer and richer. Do not force the user to answer optional sensitive fields such as compensation or contact details.

## 4. Save the encyclopedia

Create `encyclopedia/career-encyclopedia.md` using this structure. For an existing encyclopedia, merge only new or corrected facts while retaining its content and organization:

```markdown
# Career Encyclopedia

> Single source of truth for your professional history.
> Last updated: {YYYY-MM-DD}

## Personal Details
- Name:
- Email:
- Location:
- Languages:

## Education

## Career Timeline

## Side Projects & Entrepreneurship

## Technology Skills — Truth Map
| Skill | Level | Notes |
|---|---|---|

## Career Aspirations
- Ideal role:
- What energizes you:
- What drains you:
- Compensation floor:
- Location preferences:
- Company size/stage preference:

## Key Stories & Differentiators
```

Use ISO dates where known. Treat direct, unambiguous user statements and supplied career records as source material; mark inferred, contradictory, or uncertain claims `[UNVERIFIED]`. Never silently resolve contradictions. Save useful confirmed progress if the user pauses the interview; identify remaining gaps without filling them in.

## 5. Finish

Summarize the files created or updated. Offer to continue with the `dimensions` skill; if the user agrees, define the dimensions in the same conversation rather than making them repeat context.
