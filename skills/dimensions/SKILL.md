---
name: dimensions
description: Define or refine the scoring dimensions and weights used to evaluate job descriptions against a career profile. Use when the user asks about dimensions, scoring criteria, job priorities, or changing how opportunities are scored.
---

# Dimensions — Define Scoring Criteria

Define or refine the scoring dimensions used by the `jd` skill to evaluate job descriptions against the user's profile.

## Workspace and invocation

Resolve career-file paths relative to the user's career workspace, never the installed plugin directory. Skill names below can be invoked as `$ai-career-coach:skill-name` in Codex or `/ai-career-coach:skill-name` in Claude Code; natural-language requests also work.

Ask one question at a time. Use an interactive user-input tool with two or three likely options when available; otherwise ask directly in chat.

## Instructions

### Step 1: Check current state

Check if `dimensions.md` exists in the workspace root.

**If it exists:** Read it, display the current dimensions in a concise summary, then ask:
"Your current dimensions are shown above. What would you like to do?"
- Likely options: "Refine these" / "Add a dimension" / "They're fine"

Honor any change already requested. Preserve existing custom dimensions and weights unless the user asks to replace them. If they are already satisfied, stop without rewriting the file.

**If it doesn't exist:** Read `encyclopedia/career-encyclopedia.md`, especially Career Aspirations, to inform customization. If the encyclopedia is missing or empty, tell the user to use the `setup` skill first and stop.

### Step 2: Present the default dimensions

For a new set, start with these five defaults. Do not rename or add dimensions unless the user asks. When refining an existing set, work from its saved dimensions instead:

1. **Hard Skills Match** — Technologies, tools, platforms, technical competencies. How well do the JD's technical requirements overlap with proven skills in the encyclopedia?
   - Scores high: significant overlap with hands-on skills
   - Scores low: JD requires deep expertise in technologies the user hasn't used

2. **Domain Match** — Industry, business model, domain expertise. How familiar is the user with this sector?
   - Scores high: direct experience in the industry or closely adjacent ones
   - Scores low: completely unfamiliar industry with domain-specific requirements

3. **Leadership Match** — Scope, team size, seniority level, organizational complexity. Does the role match their leadership experience?
   - Scores high: role scope aligns with proven leadership track record
   - Scores low: significant gap in team size, budget, or organizational complexity (either too big or too small)

4. **Culture & Values Match** — Company culture signals from JD language vs. what energizes the user (from encyclopedia Career Aspirations).
   - Scores high: JD signals align with what the user thrives in
   - Scores low: red flags like bureaucracy, micromanagement, values misalignment, or culture the user explicitly wants to avoid

5. **Career Trajectory Fit** — Does this role move the user toward their stated career goals? Does it advance their narrative or is it lateral/backwards?
   - Scores high: clear step toward career aspirations, develops target capabilities
   - Scores low: lateral move, dead-end, or pulls away from goals

**Scoring anchors** — when saving dimensions, always include these calibration rules:

> **How to score:** Default to 5 (neutral) when information is ambiguous or missing. Only score higher with clear evidence from the JD and encyclopedia. A company that doesn't disclose salary is a 5 on compensation, not a 9. A JD that doesn't mention team size is a 5 on leadership match, not an assumption.
>
> - **9-10:** Exceptional match — direct, proven, deep experience
> - **7-8:** Strong match — significant overlap, minor gaps
> - **5-6:** Neutral or partial — some match, some unknowns
> - **3-4:** Weak — meaningful gaps or misalignment
> - **1-2:** Hard blocker — fundamental mismatch or missing requirement

When creating a new set, present all five and ask: "These are the recommended scoring dimensions. Would you like to customize them?"
- Likely options: "Save these" / "Adjust weights" / "Customize the set"

For weight adjustment, ask about each dimension ONE at a time:
- Options: "High" / "Medium" / "Low"

Use Medium for every default unless the user chooses otherwise. Weights express relative priority in the recommendation: high matters more than medium, which matters more than low. Preserve any explicit weighting method the user already defined.

If the user wants to add a custom dimension, ask for:
- Name
- What it measures
- What scores high vs. low

### Step 3: Save dimensions

Save to `dimensions.md` in workspace root:

```markdown
# Scoring Dimensions

> Used by the jd skill to evaluate job descriptions against your profile.
> Customize with the dimensions skill at any time.
> Last updated: {date}

## Dimensions

### 1. {Dimension Name}
- **Weight:** {High / Medium / Low}
- **Description:** {what it measures}
- **Scores high when:** {criteria}
- **Scores low when:** {criteria}

(repeat for each dimension)

## Scoring calibration

(include the scoring anchors above)
```

### Step 4: Confirm

Show the final dimensions and confirm the saved changes. Tell the user these will be used by the `jd` skill to score every job description they analyze.
