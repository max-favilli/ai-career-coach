# AI Career Coach — Marketing Plan

## Strategy

Position the plugin as a tool built from real frustration, not a side project. The narrative: "After months of job hunting and hundreds of CVs, I realized AI CV generators are doing it wrong. So I built something different." The key differentiator is the compounding encyclopedia — knowledge grows with every interaction.

**Skip LinkedIn** — employer visibility risk. Revisit after leaving current role.

---

## Calendar

| Week | Day | Channel | Action |
|------|-----|---------|--------|
| Week 1 | Tuesday | Hacker News | Show HN post |
| Week 1 | Wednesday | r/ClaudeAI | Plugin announcement |
| Week 1 | Friday | r/ExperiencedDevs | Personal story angle |
| Week 2 | Monday | Anthropic | Submit to official marketplace (clau.de/plugin-directory-submission) |
| Week 2 | Wednesday | r/jobsearch | Job seeker angle |
| Week 2 | Friday | r/resumes | CV tailoring angle |
| Week 3 | Tuesday | r/careerguidance | Career strategy angle |
| Week 3 | Thursday | r/ChatGPTCoding | Technical/builder angle |
| Week 3 | Weekend | Anthropic Discord | Share in community channel if available |

**Posting times:** Aim for 2-3pm CET (US East Coast morning) for maximum visibility.

---

## Post Texts

### 1. Hacker News — Show HN

**Title:** `Show HN: AI Career Coach – Claude Code plugin where your profile compounds with every job you analyze`

**First comment (post immediately after submitting):**

> I built this after 9 months of job hunting. I'm a Director of IT at a large company, sent hundreds of CVs, got called for interviews twice. The problem wasn't my experience — it was that every CV was either generic or took hours to tailor properly.
>
> I started using Claude Code to analyze JDs and write tailored CVs. But I noticed something: every conversation, I was re-explaining my career from scratch. The AI had no memory of what we discussed yesterday.
>
> So I built a system around it. The core idea is a "career encyclopedia" — a structured document that captures everything about your professional history, including things that aren't on any CV. Skills with honest proficiency levels. Stories about how you handled a crisis. What you're actually looking for. What drains you.
>
> Every time you analyze a job description, the gap interview surfaces new things: "Oh, I actually did pre-sales at that job." That gets added to the encyclopedia. So the 10th CV you generate is dramatically better than the first — Claude knows things about you that you forgot to write down.
>
> The plugin also tells you to pass when a role is a poor fit. I've analyzed ~20 JDs with it — roughly half were passes, which saved me hours of tailoring CVs for roles I shouldn't have applied to.
>
> It's free, MIT licensed, and runs entirely locally. No data leaves your machine.
>
> GitHub: https://github.com/max-favilli/ai-career-coach
>
> Blog post: [YOUR BLOG URL]
>
> Would love feedback — especially from anyone who's been through a senior-level job search and knows the pain.

---

### 2. r/ClaudeAI — Plugin Announcement

**Title:** `I built a free Claude Code plugin that turns Claude into a long-term career coach (not a one-shot CV generator)`

**Body:**

> After months of using Claude Code for job hunting, I realized the biggest problem isn't generating a CV — it's that Claude forgets everything between sessions.
>
> So I built **AI Career Coach**, a plugin that maintains a persistent "career encyclopedia" about you. Every job description you analyze, every gap interview you go through, every skill you mention — it all gets captured and compounds over time.
>
> **What it does:**
>
> - `/setup` — Builds your career encyclopedia through an interactive interview (or imports your existing CV)
> - `/dimensions` — Define what matters to YOU when scoring jobs (customizable)
> - `/jd` — Analyze a job description: scores it across your dimensions, gives an honest recommendation (including "pass"), and interviews you to surface hidden experience
> - `/cv` — Generates a tailored CV with the right "frame" for each role (builder, enterprise leader, startup CTO, etc.)
> - Every interaction enriches the encyclopedia — so the more you use it, the better it gets
>
> **Install:**
> ```
> claude plugin marketplace add max-favilli/ai-career-coach
> claude plugin install ai-career-coach
> ```
>
> Free, MIT licensed, no data leaves your machine. GitHub: https://github.com/max-favilli/ai-career-coach
>
> Would love to hear feedback from anyone who tries it.

---

### 3. r/ExperiencedDevs — Personal Story

**Title:** `After 9 months of job hunting at director level, I built an AI system that actually works for senior roles`

**Body:**

> I'm a Director of IT at a large company. Been looking for my next role since last summer. Sent hundreds of CVs, got called for interviews twice.
>
> The problem with job hunting at this level: every role needs a completely different narrative. A startup CTO role needs to see the scrappy builder who shipped products from zero. An enterprise transformation role needs to see the person who managed €20M budgets and 20-person teams. A consulting practice leader needs pre-sales and client management. It's all the same career — but the framing is everything.
>
> Generic AI CV generators are useless for this. They either produce corporate fluff or just rearrange your bullet points.
>
> So I built a Claude Code plugin that takes a different approach:
>
> 1. **It builds a "career encyclopedia"** — not a CV, but a deep structured document with every role, every skill (with honest proficiency levels), every achievement, every story. Things that wouldn't fit on any single CV but matter for specific roles.
>
> 2. **It grows with every interaction.** When I analyze a JD and it asks "do you have pre-sales experience?" and I say "actually yes, at three different companies" — that gets added to the encyclopedia. The 15th CV I generated was dramatically more targeted than the first.
>
> 3. **It tells me to pass.** Roughly half the JDs I've analyzed came back as "poor fit" with specific reasons. That saved me hours per role.
>
> 4. **It selects the right "frame."** Same career, different story depending on what the hiring manager actually needs.
>
> Open source, free: https://github.com/max-favilli/ai-career-coach
>
> Curious if others at senior/director level have found approaches that work. The job market for experienced leaders feels brutal right now.

---

### 4. r/jobsearch — Job Seeker Angle

**Title:** `Free tool: AI that learns your career over time and writes targeted CVs for each role (not the usual "paste JD, get generic CV")`

**Body:**

> I've been job hunting for 9 months. The biggest thing I learned: a generic CV doesn't work. Every role needs a different story. But manually tailoring a CV for every application takes 1-2 hours.
>
> I built a Claude Code plugin that solves this differently than the usual AI CV tools:
>
> **The key idea:** Instead of starting from scratch every time, the plugin maintains a "career encyclopedia" — a detailed document about your entire professional history. Not just job titles and dates, but: what you actually built, what technologies you know (and how well), what energizes you, what you want next.
>
> **Why it's different:**
> - It **interviews you** before writing anything — surfaces experience you forgot to mention
> - It **tells you to pass** when a job is a poor fit — saves you time
> - It **scores every JD** across customizable dimensions (hard skills, domain, culture, career trajectory)
> - It **grows smarter with every use** — gap interviews discover new things about your career that get saved permanently
> - The 10th CV it generates is dramatically better than the first
>
> **It's free**, open source, and runs entirely on your machine. No data is sent anywhere.
>
> You need Claude Code (Anthropic's CLI tool) to use it.
>
> Install:
> ```
> claude plugin marketplace add max-favilli/ai-career-coach
> claude plugin install ai-career-coach
> ```
>
> GitHub: https://github.com/max-favilli/ai-career-coach

---

### 5. r/resumes — CV Tailoring Angle

**Title:** `I built a free AI tool that generates persona-targeted CVs — same career, different framing for each role`

**Body:**

> The biggest lesson from my job search: a CV isn't a list of what you did. It's a story about who you are — and the story needs to change depending on who's reading it.
>
> The same 25 years of experience gets framed as:
> - **"Builder/CTO"** for a startup — emphasizing greenfield projects, architecture decisions, speed
> - **"Enterprise transformation leader"** for a big company — emphasizing budget (€20M), team size (20+), governance
> - **"Cloud modernization architect"** for consulting — emphasizing migration projects, DevSecOps, pre-sales
>
> Each version is 100% truthful. But the headline, summary, bullet selection, and emphasis are completely different.
>
> I built a Claude Code plugin that does this systematically:
>
> 1. You build a "career encyclopedia" — every role, skill, achievement, story
> 2. You paste a job description — it scores the fit and interviews you to surface hidden relevant experience
> 3. It picks the right "frame" and generates a tailored CV — markdown, styled HTML, and PDF
>
> The more jobs you analyze, the richer the encyclopedia gets, and the more targeted every subsequent CV becomes.
>
> Free, open source: https://github.com/max-favilli/ai-career-coach
>
> Requires Claude Code (Anthropic's CLI tool).

---

### 6. r/careerguidance — Career Strategy Angle

**Title:** `I built a free AI tool that tells you which jobs to skip (and it's more useful than the CV it generates)`

**Body:**

> The most valuable feature of the AI career coach I built isn't the CV generation — it's the honest "pass" recommendation.
>
> After months of applying to everything that looked vaguely relevant, I started analyzing JDs more systematically. Scoring them across 5 dimensions: hard skills match, domain match, leadership match, culture fit, and career trajectory.
>
> Roughly half the roles I analyzed came back as "pass" — with specific reasons:
> - "Embedded systems domain — zero experience, hard blocker"
> - "Return to consulting — left 13 years ago, doesn't advance goals"
> - "Degree required — Italian firms enforce this in screening"
> - "Python stack — no experience, startup can't afford ramp-up"
>
> Each pass saved me 1-2 hours of tailoring a CV for a role I wouldn't get anyway.
>
> The tool also maintains a "career encyclopedia" that grows over time — every gap interview surfaces experience you forgot to mention, and it gets saved permanently. So the analysis and CV tailoring gets more precise with every use.
>
> Free, open source, runs locally: https://github.com/max-favilli/ai-career-coach
>
> Requires Claude Code (Anthropic's CLI).

---

### 7. r/ChatGPTCoding — Technical/Builder Angle

**Title:** `Built a Claude Code plugin with 5 skills that compounds user knowledge over time — architecture walkthrough`

**Body:**

> I built an open-source Claude Code plugin called AI Career Coach. Sharing because the architecture pattern might be useful for other plugin builders.
>
> **The core design problem:** Claude Code sessions are stateless. For a career coaching use case, you need the AI to remember everything about the user across sessions. But Claude Code plugins can't store data inside the plugin directory (it gets copied to cache on install).
>
> **Solution:** The plugin creates a workspace-local "career encyclopedia" — a structured markdown file that serves as persistent memory. Every skill reads from it, and the `/jd` skill writes back to it when gap interviews surface new information. The encyclopedia is the compounding asset.
>
> **Plugin structure:**
> ```
> skills/
> ├── setup/SKILL.md          # Onboarding — builds encyclopedia through interactive interview
> ├── dimensions/SKILL.md     # Define customizable scoring dimensions
> ├── jd/SKILL.md             # Analyze JDs — score, recommend, interview, update encyclopedia
> ├── cv/SKILL.md             # Generate persona-targeted CVs (MD, HTML, PDF)
> └── add-to-encyclopedia/SKILL.md  # Import content from CVs, LinkedIn, etc.
> ```
>
> **Key patterns:**
> - All user interaction through `AskUserQuestion` tool with pre-baked options (one question at a time)
> - Scores presented as markdown tables (had to add "CRITICAL: ALWAYS use table format" — Claude kept reverting to lists)
> - Cross-platform PDF generation: tries `npx md-to-pdf` → browser headless (Edge/Chrome) → manual fallback
> - Skills reference each other implicitly (e.g., `/cv` reads JD analyses created by `/jd`)
>
> **What I learned building it:**
> - Skill instructions need to be extremely explicit about format — "present as a table" isn't enough, you need an example
> - The `AskUserQuestion` tool is great for structured interactions but you have to tell Claude repeatedly to use it
> - Plugin vs. project skills: `skills/` at root for distribution, `.claude/skills/` for local dev — keep both, gitignore the local copies
>
> GitHub: https://github.com/max-favilli/ai-career-coach
>
> MIT licensed. Feedback welcome, especially on the skill instruction patterns.

---

## Engagement Rules

- **Reply to every comment** within 24 hours
- **Don't be salesy** — you're sharing a tool you built for yourself, not selling a product
- **Be honest about limitations** — requires Claude Code (paid), plugin system is new, some rough edges
- **Link the blog post** in comments if someone asks for more detail
- **Cross-link** — if a post on r/ClaudeAI gets traction, mention it in r/ExperiencedDevs comments as social proof

## Metrics to Track

- GitHub stars and forks
- Plugin installs (if Anthropic provides analytics)
- Reddit upvotes and comment quality
- HN points and front-page duration
- Blog post traffic (if you have analytics)
