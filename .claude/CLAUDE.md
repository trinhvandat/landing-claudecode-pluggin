# landing-page-pro — Claude Code Constitution

> **IMPORTANT**: This file MUST exist at the project root as `CLAUDE.md` (not only in `.claude/`).
> Claude Code reads `CLAUDE.md` from root on every session start. If you moved it, copy it back.

## What Is This
A Claude Code Plugin with 6 skills that automate the full Google Ads landing page workflow:
Research → Competitor Analysis → Personas → Design → Build → Optimize.

## Project Type
Claude Code Plugin. Follow `.claude-plugin/plugin.json` + `manifest.json` conventions.
Note: Plugin file formats may evolve — verify against Claude Code docs before publishing.

## Installed Plugins (Available to Use)
- **UI UX Pro Max (UUPM)** — Design intelligence engine. Located at `.claude/skills/ui-ux-pro-max/`.
  Use its `scripts/search.py` for design system generation. NEVER hardcode design decisions without consulting UUPM first.
- **oh-my-claudecode (OMC)** — Multi-agent orchestration. Use for pipeline/swarm execution.
  NOT required for skills to work — skills must be standalone-capable.

## Core Rules — MUST FOLLOW

### Rule 1: Read Blueprint Before Building
Before implementing ANY skill, read `blueprint/plugin-spec.md` for that skill's full specification.
Before creating directory structure, read `blueprint/plugin-structure.md` for exact paths.
DO NOT SKIP THIS. DO NOT guess file paths or skill behavior.

### Rule 2: Research Before Code — Always
NEVER generate landing page code without research outputs existing in `output/{project}/research/`.
A landing page without research is a landing page that wastes ad spend. No exceptions.

### Rule 3: Message Match is Sacred
The landing page headline MUST echo the Google Ads headline. Word for word.
If ad says "Trồng Răng Implant Không Đau" → page headline says "Trồng Răng Implant Không Đau".
Mismatch = low Quality Score = high CPC = failed campaign.

### Rule 4: UUPM First, Fallback Second
When generating design decisions:
1. Check if `.claude/skills/ui-ux-pro-max/scripts/search.py` exists
2. If YES → run UUPM search with industry + product + audience keywords
3. If NO → use `skills/design-brief/references/fallback-design-rules.md`
NEVER make up colors/fonts/patterns without design intelligence backing.

### Rule 5: Mobile-First, Speed-First, Single CTA
- Code for 375px viewport FIRST, then scale up
- Target < 3 seconds page load
- ONE primary CTA per page. No competing buttons. No navigation menu.
- Over 60% of Google Ads clicks come from mobile

### Rule 6: Imperative SKILL.md, Not Documentation
SKILL.md files are PROMPTS for Claude, not docs for humans.
Write them as imperative instructions: "DO this", "NEVER do that", "IF x THEN y".
Use decision trees, numbered steps, explicit file paths.
README.md is for humans. SKILL.md is for Claude.

### Rule 7: Ask Before Generating > 3 Files
Before creating more than 3 files in one step, show the plan and get confirmation.
This prevents wrong-direction work that's expensive to undo.

## Skill Pipeline Order

```
niche-research ──┐
                  ├──→ audience-persona → design-brief → landing-page-builder → conversion-optimizer
competitor-analysis┘
```

- Skills 1 & 2 (niche-research, competitor-analysis) can run in PARALLEL
- Skills 3-6 are SEQUENTIAL — each depends on previous outputs
- With OMC: use `swarm` for parallel research, `pipeline` for the rest

## Output Convention
All generated project outputs go to:
```
output/{project-name}/
├── research/          # Skills 1-3 outputs
│   ├── niche-brief.md
│   ├── competitor-report.md
│   ├── personas.md
│   └── ad-copy-suggestions.md
├── design-system/     # Skill 4 output (UUPM-generated)
│   ├── MASTER.md
│   └── pages/*.md
├── src/               # Skill 5 output (landing page code)
└── audit/             # Skill 6 output
    └── optimization-report.md
```
Project name = kebab-case from client/product name.

## Tech Stack Detection (for landing-page-builder skill)
1. Check current project for: `package.json` (React/Next), `astro.config.*` (Astro), `index.html` (static)
2. If detected → use that stack
3. If not detected → ASK user, suggest HTML+Tailwind as default
4. Read the corresponding `references/stack-guides/{stack}.md` BEFORE generating code

## Blueprint References
Read these ONLY when you need the detail (not upfront):
- `blueprint/plugin-structure.md` — Full directory tree, every file path, file purposes
- `blueprint/plugin-spec.md` — Detailed spec for each of the 6 skills (input/output/workflow/templates)

## Anti-Patterns — NEVER DO THESE
- NEVER write SKILL.md like documentation. It's a PROMPT.
- NEVER dump entire reference docs into SKILL.md. Summarize, keep only action steps.
- NEVER generate landing page without design-brief step. Even a quick page needs design decisions.
- NEVER create overloaded skills. 1 skill = 1 outcome.
- NEVER assume tech stack. Check project first, then decide.
- NEVER skip error handling in skills. Cover what happens when web_search fails, URLs are unreachable, UUPM is missing.
- NEVER put navigation menus on landing pages. They are distraction-free by design.

## Error Handling — Required in Every Skill
Each SKILL.md MUST include error paths for these common failures:
- **web_search unavailable or fails**: Retry once → ask user for manual input → proceed with partial data
- **web_fetch blocked/timeout**: Try alternate URL → ask user for copy-pasted HTML → skip that competitor
- **Previous skill output missing**: Show clear error: "⚠️ Required: {file}. Run {skill-name} first." — NEVER silently proceed
- **UUPM not installed**: Use `skills/design-brief/references/fallback-design-rules.md` (build this file in Phase C1 BEFORE it's needed)
- **Character limit exceeded** (ad copy): Rewrite shorter, never truncate mid-word
