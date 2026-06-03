---
name: dimensions
description: "Define or refine the scoring dimensions used to evaluate job descriptions against your profile. Use when: user says 'dimensions', 'scoring criteria', 'change how jobs are scored'."
---

# Dimensions — Define Scoring Criteria

Define or refine the scoring dimensions used by `/jd` to evaluate job descriptions against your profile.

## Instructions

### Step 1: Check current state

Check if `dimensions.md` exists in the workspace root.

**If it exists:** Read it, display the current dimensions in a concise summary, then ask:
"Your current dimensions are shown above. What would you like to do?"
- Options: "Refine these" / "Add a new dimension" / "Start over" / "They're fine, done"

**If it doesn't exist:** Check if `encyclopedia/career-encyclopedia.md` has content. If so, read it — especially the Career Aspirations section — and suggest dimensions based on the user's profile and goals. If the encyclopedia is empty, tell the user to run `/setup` first.

### Step 2: Suggest or refine dimensions

Start with these defaults, but tailor the suggestions based on the encyclopedia content:

1. **Hard Skills Match** — Technologies, tools, platforms, technical competencies. How well do the JD's technical requirements overlap with proven skills?
2. **Domain Match** — Industry, business model, domain expertise. How familiar is the user with this sector?
3. **Leadership Match** — Scope, team size, seniority level, organizational complexity. Does the role match their leadership experience?
4. **Culture & Values Match** — Company culture signals vs. what energizes the user. Red flags like bureaucracy, micromanagement, or values misalignment.
5. **Career Trajectory Fit** — Does this role move toward stated career goals? Advances the narrative or is it lateral/backwards?

For each dimension, ask ONE question at a time using AskUserQuestion:

"Is **[dimension name]** important to you when evaluating job opportunities? [Brief description of what it measures]"
- Options: "Very important" / "Somewhat important" / "Not very important" / "Remove this dimension"

If the user wants to add custom dimensions, ask for:
- Name
- What it measures
- What scores high vs. low

### Step 3: Save dimensions

Save to `dimensions.md` in workspace root:

```markdown
# Scoring Dimensions

> Used by /jd to evaluate job descriptions against your profile.
> Customize with /dimensions at any time.
> Last updated: {date}

## Dimensions

### 1. {Dimension Name}
- **Weight:** {High / Medium / Low}
- **Description:** {what it measures}
- **Scores high when:** {criteria}
- **Scores low when:** {criteria}

(repeat for each dimension)
```

### Step 4: Confirm

Show the final dimensions and confirm with the user. Tell them these will be used by `/jd` to score every job description they analyze.
