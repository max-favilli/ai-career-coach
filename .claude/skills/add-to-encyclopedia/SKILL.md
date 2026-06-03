---
name: add-to-encyclopedia
description: "Add new career content to your encyclopedia. Paste a CV, LinkedIn export, career summary, or interview notes and it gets parsed and integrated. Use when: user says 'add to my profile', 'update my encyclopedia', 'import my CV'."
---

# Add to Encyclopedia

Add new career content to the encyclopedia. Accepts pasted text (CV, LinkedIn export, career summary, interview notes) and integrates it through an interactive interview.

## Instructions

### Step 1: Check encyclopedia exists

Read `encyclopedia/career-encyclopedia.md`. If it's missing, tell the user to run `/setup` first and stop.

### Step 2: Accept content

The user may provide content as:
- `$ARGUMENTS` — text pasted directly after the command
- A file path to read
- Text in a follow-up message

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

For each piece of new information that needs clarification, ask ONE question at a time using AskUserQuestion:

- Ambiguous dates: "You mentioned working at {company}. When approximately did you start and leave?"
- Skill proficiency: "You mention {technology}. What's your proficiency level?"
  - Options: "Deep, hands-on" / "Working knowledge" / "Oversight/strategic only" / "Historical, not current"
- Contradictions: "Your encyclopedia says {X} but this content says {Y}. Which is correct?"
- Missing context: "What was your team size at {company}?" / "What was the business outcome?"

### Step 5: Integrate

- Add new information in the correct chronological position
- Maintain the existing structure and section headers
- Mark any unverified items with `[UNVERIFIED]` — the user can confirm and remove the tag later
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
