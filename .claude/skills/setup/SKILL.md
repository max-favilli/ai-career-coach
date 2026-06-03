---
name: setup
description: "Set up the AI Career Coach: create workspace structure, build your career encyclopedia through an interactive interview, and define scoring dimensions. Use when: user says 'setup', 'get started', 'initialize', 'onboard'."
---

# Setup — Career Coach Onboarding

One-time setup for the AI Career Coach. Creates workspace structure, builds your career encyclopedia through an interactive interview, and optionally defines scoring dimensions.

## Instructions

### Step 1: Check if already set up

Check if `CLAUDE.md` exists in the workspace root. If it does, warn the user: "Setup has already been run. Do you want to re-run it? This will overwrite your CLAUDE.md but will NOT touch your encyclopedia or other files." If they say no, stop.

### Step 2: Create folder structure

Create these directories if they don't exist:
- `encyclopedia/`
- `jd-analysis/`
- `tailored-cvs/`

### Step 3: Create CLAUDE.md

Write the following content to `CLAUDE.md` in the workspace root:

```markdown
# Career Coach Command Center

This workspace is your long-term job hunting system. Claude is your career positioning partner, not a one-shot CV writer.

## Core Principles

1. **Never fabricate experience — but represent strategically.** Don't claim skills or achievements you don't have. But represent truthfully in the most favorable light. The CV's job is to get you past screening so you can prove your worth in person.
2. **Authenticity over polish.** Preserve your personal voice. Generic corporate language is the enemy.
3. **The encyclopedia is the source of truth.** `encyclopedia/career-encyclopedia.md` contains everything known about your career. Read it at the start of every task.
4. **Interview before crafting.** For every new JD, conduct a gap interview before writing anything.
5. **Honesty about fit.** Tell the user when a role is a poor match. Their time is more valuable than another application.

## Interaction Style

**CRITICAL:** When asking questions during gap interviews, encyclopedia building, or any coaching interaction:
- ALWAYS use the AskUserQuestion tool to ask questions
- Ask ONE question at a time
- Provide 2-4 pre-baked answer options that cover the most likely responses
- The user can always select "Other" to provide free-text input
- Wait for the answer before asking the next question
- Never dump multiple questions at once

## Scoring Presentation

When scoring a JD against dimensions, ALWAYS present scores as a table for easy scanning:

| Dimension | Score | Notes |
|---|---|---|
| Hard Skills | X/10 | Brief note |
| Domain | X/10 | Brief note |
| ... | ... | ... |

Follow the table with the overall recommendation and key concerns.

## Folder Structure

- `encyclopedia/career-encyclopedia.md` — Single source of truth for career history
- `dimensions.md` — Scoring dimensions for JD evaluation
- `jd-analysis/` — Job description analyses
- `jd-log.md` — Running log of all analyzed JDs
- `tailored-cvs/` — Output CVs (markdown, HTML, PDF)

## Available Commands

- `/setup` — Initial onboarding (run once)
- `/dimensions` — Define or refine scoring dimensions
- `/jd` — Analyze a job description
- `/cv` — Craft a tailored CV after JD analysis
- `/add-to-encyclopedia` — Add new career content

## Representation Rules

- Never fabricate experience or skills
- Frame oversight as oversight, not hands-on expertise
- Early career dates can be approximate
- Strategic representation is OK — help the company make a good hiring decision
- Education: state what you studied and where, without specifying completion status unless the user tells you to
```

### Step 4: Build the career encyclopedia

Ask the user ONE question at a time using the AskUserQuestion tool. Always provide pre-baked answer options.

**First question:** "Do you have an existing CV, LinkedIn export, or career summary I can start from?"
- Options: "Yes, I'll paste it now" / "Yes, I have a file path" / "No, let's start from scratch"

**If they provide content:** Read it and parse it into the encyclopedia structure below. Then you MUST conduct a thorough clarification interview BEFORE saving. Do NOT skip this step. Do NOT move on to dimensions until the interview is complete.

**MANDATORY CLARIFICATION INTERVIEW (after parsing provided content):**

Go through the parsed content section by section and ask about anything that is missing, vague, or could be stronger. Ask ONE question at a time using AskUserQuestion. Typical gaps to probe:

- **For each role:** "What was your team size at {company}?" / "What was the key achievement you're most proud of here?" / "Why did you leave?"
- **Technologies:** "You mention {technology} — what's your honest proficiency level?" (Options: Deep hands-on / Working knowledge / Oversight only / Historical, not current)
- **Missing sections:** If the content doesn't mention side projects, education details, or career aspirations, ask about each.
- **Ambiguous dates:** "You mentioned {company} — when approximately did you start and leave?"
- **Achievements without metrics:** "You mention {achievement} — can you quantify the impact? Team size, revenue, users, budget?"
- **Career aspirations:** ALWAYS ask these even if not in the source content:
  - "What kind of role are you looking for next?" 
  - "What energizes you at work?"
  - "What drains you?"
  - "What's your minimum compensation requirement?"
  - "Location preferences — remote, hybrid, relocation?"

Ask at minimum 5-8 clarifying questions. The goal is to make the encyclopedia richer than the source content, not just a reformatted copy. This interview is the core value of the setup process.

**If starting from scratch (no source content):** Interview systematically through each section below, one question at a time:

1. **Personal details** — name, email, location, languages
2. **Education** — degrees, institutions, dates
3. **Career timeline** — for each role, ask:
   - Company name and your title
   - Dates (approximate is fine)
   - Location
   - What did you build/lead/deliver? (key achievements)
   - Team size and scope
   - Technologies used
   - Why did you leave?
4. **Side projects** — any startups, open source, communities
5. **Technology skills** — for each technology, ask about proficiency level (deep/working/oversight/historical)
6. **Career aspirations** — what they want next, what energizes them, what drains them, practical requirements (salary, location, company size)

### Step 5: Save the encyclopedia

Save to `encyclopedia/career-encyclopedia.md` with this structure:

```markdown
# Career Encyclopedia

> Single source of truth for your professional history.
> Last updated: {date}

## Personal Details
- Name:
- Email:
- Location:
- Languages:

## Education
(degrees, institutions, dates)

## Career Timeline
(chronological, each role as a ### subsection with: company, title, dates, location, achievements, team size, technologies)

## Side Projects & Entrepreneurship
(startups, open source, communities)

## Technology Skills — Truth Map
| Skill | Level | Notes |
|---|---|---|
(each technology with honest proficiency: deep/working/oversight/historical)

## Career Aspirations
- Ideal role:
- What energizes you:
- What drains you:
- Salary minimum:
- Location preferences:
- Company size/stage preference:

## Key Stories & Differentiators
(leadership stories, crisis management, unique achievements — added over time through /add-to-encyclopedia)
```

### Step 6: Offer to define dimensions

Ask: "Would you like to define your scoring dimensions now? Dimensions are the criteria used to score job descriptions against your profile."
- Options: "Yes, let's do it" / "No, I'll do it later with /dimensions"

If yes, tell the user to run `/dimensions`.

Print a summary of what was created and what commands are available.
