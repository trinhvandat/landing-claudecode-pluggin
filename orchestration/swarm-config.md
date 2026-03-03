# Landing Page Pro — Parallel Research & Eco Mode Prompt Templates

> **IMPORTANT**: oh-my-claudecode does NOT read config files. It uses magic keywords in prompts.
> These are PROMPT TEMPLATES for the user to paste into Claude Code with OMC active.
> They are NOT machine-readable configs.

## How to Use

1. Replace `{client brief}` with your actual client brief.
2. Replace `{project}` with the kebab-case project name.
3. Copy-paste the relevant prompt into Claude Code (with OMC installed).

---

## Parallel Research Prompt (swarm)

Use this to run niche-research and competitor-analysis simultaneously, then continue sequentially.

```
swarm: Research for a landing page project: {client brief}.

Run these tasks in parallel:
- Task 1: niche-research
  → Find keywords, CPC estimates, search intent
  → Save to output/{project}/research/niche-brief.md

- Task 2: competitor-analysis
  → Crawl and analyze top 3-5 competitor landing pages
  → Save to output/{project}/research/competitor-report.md
  → Save to output/{project}/research/swipe-file.md

After both complete, continue sequentially:
- audience-persona
  → Save to output/{project}/research/personas.md
  → Save to output/{project}/research/ad-copy-suggestions.md
```

## Full Swarm + Pipeline Combo

Run research in parallel, then feed into the sequential design→build→optimize pipeline.

```
swarm: Complete landing page project for {client brief}.

Phase 1 — Research (parallel):
- niche-research → output/{project}/research/niche-brief.md
- competitor-analysis → output/{project}/research/competitor-report.md

Phase 2 — Sequential (after both research tasks complete):
- audience-persona → output/{project}/research/personas.md + ad-copy-suggestions.md
- design-brief → output/{project}/design-system/MASTER.md
- landing-page-builder → output/{project}/src/index.html
- conversion-optimizer → output/{project}/audit/optimization-report.md

Show progress after each step.
```

---

## Eco Mode Prompt (save tokens)

Use this for budget-conscious runs. Research is concise, creative tasks are thorough.

```
eco: Build a landing page for {client brief}.

Use the landing-page-pro pipeline. Rules for token efficiency:
- Research tasks (niche-research, competitor-analysis): be CONCISE.
  → Bullet points, no lengthy explanations.
  → 15-20 keywords instead of 30-40.
  → 3 competitors max instead of 5.
- Creative tasks (audience-persona, design-brief): be THOROUGH.
  → Full persona cards with specific pain points.
  → Complete design system with all tokens.
- Code generation (landing-page-builder): be THOROUGH.
  → Full, production-ready code. No shortcuts.
- Audit (conversion-optimizer): be CONCISE.
  → Scores + top 3 fixes + 1 A/B test. Skip nice-to-haves.

Save all outputs to output/{project}/.
```

---

## Research-Only Prompt

When you just need market intelligence without building a page.

```
swarm: Research the market for {client brief}.

Run in parallel:
- niche-research → output/{project}/research/niche-brief.md
- competitor-analysis → output/{project}/research/competitor-report.md

Then sequentially:
- audience-persona → output/{project}/research/personas.md + ad-copy-suggestions.md

Stop after research. Do NOT proceed to design or build.
Summarize key findings when complete.
```

---

## Audit-Only Prompt

When you have an existing page and just want optimization recommendations.

```
autopilot: Audit this landing page: {url_or_filepath}.
Project name: {project}.

Run conversion-optimizer skill only.
Save to output/{project}/audit/optimization-report.md.

If the page scores below 60, suggest the top 3 critical fixes
and estimate the score improvement for each.
```

---

## Output Path Reference

All prompts use these paths (matching CLAUDE.md convention):

```
output/{project}/
├── research/
│   ├── niche-brief.md           ← niche-research
│   ├── competitor-report.md     ← competitor-analysis
│   ├── swipe-file.md            ← competitor-analysis
│   ├── personas.md              ← audience-persona
│   └── ad-copy-suggestions.md   ← audience-persona
├── design-system/
│   ├── MASTER.md                ← design-brief
│   └── pages/*.md               ← design-brief (per ad group)
├── src/
│   └── index.html               ← landing-page-builder
├── landing-page-checklist.md    ← landing-page-builder
└── audit/
    └── optimization-report.md   ← conversion-optimizer
```
