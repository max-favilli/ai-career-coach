---
name: add-to-encyclopedia
description: Integrate new career information from a CV, LinkedIn export, career summary, or interview notes into the user's existing career encyclopedia. Use when the user asks to add to their profile, update the encyclopedia, or import career material.
---

# Add to Encyclopedia

Add new career content to the encyclopedia. Accepts pasted text (CV, LinkedIn export, career summary, interview notes) and integrates it through an interactive interview.

## Workspace and invocation

Resolve career-file paths relative to the user's career workspace, never the installed plugin directory. Skill names below can be invoked as `$ai-career-coach:skill-name` in Codex or `/ai-career-coach:skill-name` in Claude Code; natural-language requests also work.

## Instructions

### Step 1: Check encyclopedia exists

Read `encyclopedia/career-encyclopedia.md`. If it is missing or empty, tell the user to use the `setup` skill first and stop.

### Step 2: Accept content

The user may provide content in the current message, an attachment, a file path, or a follow-up message.

If no content is provided, ask: "What would you like to add to your encyclopedia?"
- Options: "I'll paste text (CV, LinkedIn, etc.)" / "I have a file to read" / "I want to add something specific through an interview"

### Step 3: Parse and identify new information

Parse the provided content and identify:
- New roles, companies, dates
- New technologies or skills
- New achievements or metrics
- New education or certifications
- Any information that contradicts existing encyclopedia content

### Step 4: Interview to clarify

For each piece of new information that needs clarification, ask one question at a time and wait for the answer. Use an interactive user-input tool with two or three likely options when available; otherwise ask directly:

- Ambiguous dates: "You mentioned working at {company}. When approximately did you start and leave?"
- Skill proficiency: "You mention {technology}. What's your proficiency level?"
  - Distinguish deep hands-on, working knowledge, oversight/strategic only, and historical experience. If the input tool allows only three choices, ask about current versus historical use separately.
- Contradictions: "Your encyclopedia says {X} but this content says {Y}. Which is correct?"
- Missing context: "What was your team size at {company}?" / "What was the business outcome?"

### Step 5: Integrate

- Add new information in the correct chronological position
- Maintain the existing structure and section headers
- Treat direct, unambiguous user statements as confirmed. Mark inferred, contradictory, or uncertain items `[UNVERIFIED]` so the user can resolve them later.
- Do NOT duplicate information that already exists
- Do NOT add ephemeral details (current conversation context, task lists)
- Update the "Last updated" date

### Step 6: Report changes

Show the user a concise summary of what was added or changed:
- New roles added
- Skills updated
- Achievements added
- Items marked [UNVERIFIED]

Ask: "Does this look correct? Anything to adjust?"
