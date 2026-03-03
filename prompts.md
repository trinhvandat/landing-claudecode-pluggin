# Claude Code Prompt Templates

> Copy-paste these prompts into Claude Code to implement each phase.
> Run them IN ORDER. Each phase builds on the previous.

---

## Phase A: Foundation

### Prompt A1 — Scaffold + Core Files

```
Read CLAUDE.md and blueprint/plugin-structure.md.

Step 1: Run scaffold.sh to create the directory structure (folders + empty files only).
Step 2: Then create CONTENT for these core files based on the blueprint:
  - .claude-plugin/plugin.json (copy from blueprint/plugin-structure.md, verify schema)
  - manifest.json (copy from blueprint/plugin-structure.md)
  - README.md (brief placeholder — will expand in Phase E)

Note: scaffold.sh creates empty SKILL.md files. Content will be added in Phase B and C.
Confirm the final structure matches blueprint/plugin-structure.md.
```

---

## Phase B: Research Skills (Skills 1-3)

### Prompt B1 — Niche Research Skill

```
Read blueprint/plugin-spec.md — ONLY the "Skill 1: niche-research" section.
Read blueprint/plugin-structure.md for exact file paths.

Implement the niche-research skill:
1. Write skills/niche-research/SKILL.md — imperative prompt style, NOT documentation
2. Write skills/niche-research/references/keyword-research-guide.md
3. Write skills/niche-research/references/search-intent-mapping.md
4. Write skills/niche-research/assets/niche-brief-template.md
5. Write 2 test cases in skills/niche-research/evals/evals.json
   (1 Vietnamese brief, 1 English brief — realistic user prompts)

Show me the SKILL.md before writing the reference files.
Follow CLAUDE.md Rule 6: SKILL.md is a PROMPT, not documentation.
```

### Prompt B2 — Competitor Analysis Skill

```
Read blueprint/plugin-spec.md — ONLY the "Skill 2: competitor-analysis" section.

Implement the competitor-analysis skill:
1. Write skills/competitor-analysis/SKILL.md
2. Write skills/competitor-analysis/references/analysis-framework.md
3. Write skills/competitor-analysis/references/scoring-rubric.md
4. Write skills/competitor-analysis/scripts/extract-page-structure.py
5. Write skills/competitor-analysis/assets/competitor-report-template.md
6. Write skills/competitor-analysis/assets/swipe-file-template.md
7. Write 2 test cases in skills/competitor-analysis/evals/evals.json

IMPORTANT: SKILL.md must include error path for when web_fetch is unavailable
(ask user for copy-pasted HTML as fallback).
The Python script should parse HTML and extract: headings, forms, buttons, word count, section count, framework detection.
Show me SKILL.md first.
```

### Prompt B3 — Audience Persona Skill

```
Read blueprint/plugin-spec.md — ONLY the "Skill 3: audience-persona" section.

Implement the audience-persona skill:
1. Write skills/audience-persona/SKILL.md
2. Write skills/audience-persona/references/persona-framework.md
3. Write skills/audience-persona/references/ad-copy-formulas.md (include PAS, AIDA, BAB + Google Ads char limits)
4. Write skills/audience-persona/assets/persona-template.md
5. Write skills/audience-persona/assets/ad-copy-template.md
6. Write 2 test cases in skills/audience-persona/evals/evals.json

CRITICAL: Google Ads character limits must be prominently documented:
- Headline: 30 chars max
- Description: 90 chars max
Show me SKILL.md first.
```

---

## Phase C: Build Skills (Skills 4-6)

### Prompt C1 — Design Brief Skill (UUPM Integration)

```
Read blueprint/plugin-spec.md — ONLY the "Skill 4: design-brief" section.

This skill bridges research outputs to UUPM design intelligence.
UUPM is already installed at .claude/skills/ui-ux-pro-max/

Implement the design-brief skill:
1. Write skills/design-brief/SKILL.md — must include UUPM search.py integration
2. Write skills/design-brief/references/uupm-integration-guide.md
   (document exactly how to call UUPM search.py, what flags to use, how to parse output)
3. Write skills/design-brief/references/fallback-design-rules.md
   (15 industry color palettes + 8 landing page patterns — for when UUPM is not available)
4. Write skills/design-brief/assets/master-md-template.md

Show me SKILL.md first. The UUPM integration logic is the most critical part.
After SKILL.md is approved, also write 2 test cases in evals/evals.json.
```

### Prompt C2 — Landing Page Builder Skill

```
Read blueprint/plugin-spec.md — ONLY the "Skill 5: landing-page-builder" section.

This is the main code generation skill. It reads MASTER.md and produces a complete landing page.

Implement:
1. Write skills/landing-page-builder/SKILL.md — the longest skill, needs to cover:
   - Input validation
   - Tech stack detection
   - Section-by-section generation
   - Google Ads integration (DKI, UTM, GTM, conversion tracking, schema)
   - Performance optimization
   - Pre-delivery checklist
2. Write skills/landing-page-builder/references/google-ads-lp-rules.md
3. Write skills/landing-page-builder/references/section-patterns.md
4. Write skills/landing-page-builder/references/stack-guides/html-tailwind.md
5. Write skills/landing-page-builder/references/stack-guides/react-nextjs.md
6. Write skills/landing-page-builder/references/stack-guides/astro.md
7. Write skills/landing-page-builder/assets/html-tailwind-starter.html
8. Write 2 test cases in evals/evals.json

Show me SKILL.md first. This will be the largest skill — keep SKILL.md under 500 lines,
put details in references.
```

### Prompt C3 — Conversion Optimizer Skill

```
Read blueprint/plugin-spec.md — ONLY the "Skill 6: conversion-optimizer" section.

Implement:
1. Write skills/conversion-optimizer/SKILL.md — 7-category audit system
2. Write skills/conversion-optimizer/references/audit-checklist.md
   (detailed scoring for each of the 7 categories)
3. Write skills/conversion-optimizer/references/ab-test-patterns.md
   (common A/B test variations for landing pages)
4. Write skills/conversion-optimizer/assets/audit-report-template.md
5. Write 2 test cases in evals/evals.json

Show me SKILL.md first.
```

---

## Phase D: Integration

### Prompt D1 — OMC Orchestration

```
Read blueprint/plugin-spec.md — ONLY the "OMC Orchestration" section.
oh-my-claudecode is installed in this project.

The blueprint already contains complete prompt templates for OMC.
Copy them into the orchestration/ files:
1. orchestration/pipeline.md — copy the pipeline prompt template from blueprint
2. orchestration/swarm-config.md — copy the swarm + ecomode prompt templates

Then review: do the prompts reference the correct output paths from our plugin?
Fix any path mismatches.
```

### Prompt D2 — End-to-End Test

```
Let's test the full plugin with a real scenario:

Client: Phòng khám nha khoa "Smile Dental" ở TP.HCM
Service: Trồng răng implant
Budget: 500k VND/ngày Google Ads
Target: Người 35-55 tuổi, TP.HCM

Run through all 6 skills in order:
1. niche-research → save to output/smile-dental/research/niche-brief.md
2. competitor-analysis → top 3 dental ads
3. audience-persona → 2 personas + ad copy
4. design-brief → call UUPM for healthcare dental
5. landing-page-builder → HTML+Tailwind
6. conversion-optimizer → audit the generated page

Show me each output before proceeding to the next skill.
```

---

## Phase E: Polish

### Prompt E1 — README + Description Optimization

```
Read the complete plugin (all SKILL.md files, CLAUDE.md, manifest.json).

1. Write a comprehensive README.md that covers:
   - What the plugin does (with example flow)
   - Installation instructions
   - Usage (each skill + pipeline mode)
   - Dependencies (UUPM, OMC)
   - Example output screenshots/markdown

2. Review and optimize each skill's description in manifest.json
   for better triggering accuracy. Descriptions should be "pushy" —
   include many trigger phrases so Claude activates the skill even
   for indirect requests.
```

### Prompt E2 — Expand Eval Test Cases

```
Each skill already has 2 test cases from Phase B/C.
Add 1 MORE test case per skill to cover EDGE CASES:

For each of the 6 skills, add to their existing evals/evals.json:
{
  "id": 3,
  "prompt": "edge case prompt that tests error handling or unusual input",
  "expected_output": "description of what good output looks like",
  "files": []
}

Edge case ideas:
- niche-research: user gives very vague brief ("I want to sell stuff online")
- competitor-analysis: user gives broken/unreachable URLs
- audience-persona: niche-brief exists but competitor-report doesn't
- design-brief: UUPM not installed (test fallback path)
- landing-page-builder: user requests a stack not in stack-guides/
- conversion-optimizer: user provides URL that returns 404
```

---

## Quick Reference: Phase Order

```
Phase A → Foundation (30 min)
  └── A1: scaffold + core files

Phase B → Research Skills (2-3 hours)
  └── B1: niche-research
  └── B2: competitor-analysis
  └── B3: audience-persona

Phase C → Build Skills (3-4 hours)
  └── C1: design-brief (UUPM bridge)
  └── C2: landing-page-builder (largest skill)
  └── C3: conversion-optimizer

Phase D → Integration (1-2 hours)
  └── D1: OMC orchestration
  └── D2: end-to-end test

Phase E → Polish (1 hour)
  └── E1: README + descriptions
  └── E2: eval test cases
```

Total estimated: ~8-10 hours of Claude Code sessions.

---

## Tips for Claude Code Sessions

1. **Start each session** with: "Read CLAUDE.md" — this refreshes context
2. **One skill per session** is optimal. Don't try to build all 6 at once.
3. **Always ask to see SKILL.md first** before letting Claude write references — catch errors early
4. **Use OMC autopilot** for Phase D2 testing — it'll run the full pipeline automatically
5. **If Claude gets confused**, say: "Read blueprint/plugin-spec.md section for {skill-name}"
6. **For Vietnamese content**, explicitly say: "Output in Vietnamese" — Claude defaults to English
