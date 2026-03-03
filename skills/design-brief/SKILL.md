---
name: design-brief
description: "Generate a design system (MASTER.md) for a landing page project using UUPM design intelligence. Use when user says 'create design system', 'design brief', 'design the page', 'colors and fonts', 'visual style', 'branding for landing page', 'design tokens', or any request about visual design decisions before building a landing page."
---

# Design Brief — Design System Generation via UUPM

You are running the design-brief skill. Your job: generate a complete design system (MASTER.md) for the landing page by calling UUPM (UI UX Pro Max) and augmenting with Google Ads landing page-specific design rules.

## Step 1: Read Research Inputs (DO NOT SKIP)

```
REQUIRED (refuse to proceed without):
  output/{PROJECT_NAME}/research/niche-brief.md

RECOMMENDED (use if available):
  output/{PROJECT_NAME}/research/personas.md
  output/{PROJECT_NAME}/research/competitor-report.md

IF niche-brief.md does NOT exist
  → Stop. Tell user:
    "⚠️ Required input not found: output/{PROJECT_NAME}/research/niche-brief.md
     → Run niche-research skill first: 'Research keywords for {PROJECT_NAME}'"

IF personas.md does NOT exist
  → Proceed with warning: "Generating design system without persona data. Tone defaults may be generic."

IF competitor-report.md exists
  → Read the DESIGN dimension scores to understand competitor visual landscape.
  → Look for gaps in competitor design → our differentiation opportunity.
```

Extract from research:
- **Industry** → from niche-brief (e.g., "dental", "SaaS", "e-commerce")
- **Product type** → from niche-brief (e.g., "clinic service", "software tool")
- **Audience** → from personas (age range, style preference, device split)
- **Mood** → from competitor gaps + persona tone (e.g., "trust", "modern", "urgent")
- **Ad group names** → from niche-brief (each ad group may get a page-specific override)

## Step 2: Construct UUPM Search Query

Build a search query from the extracted data:

```
FORMAT: "{industry} {product_type} {audience_descriptor} {mood_keywords}"

EXAMPLES:
  "dental clinic implant healthcare Vietnamese trust professional"
  "SaaS project management modern clean minimal enterprise"
  "e-commerce fashion young trendy mobile-first vibrant"
  "legal services law firm corporate authoritative trustworthy"
```

Rules:
- Include 5-8 keywords. More keywords = better BM25 matching.
- Always include the industry AND the mood/tone.
- IF persona says "formal tone" → add "professional", "corporate", "clean"
- IF persona says "casual tone" → add "friendly", "playful", "modern"
- IF persona says "urgent tone" → add "bold", "direct", "high-contrast"
- IF persona says "data-driven tone" → add "clean", "structured", "minimal"

## Step 3: Check UUPM and Execute

This is the CRITICAL step. Follow this decision tree exactly:

```
CHECK: Does .claude/skills/ui-ux-pro-max/scripts/search.py exist?

═══════════════════════════════════════════════════════
  PATH A: UUPM IS AVAILABLE (search.py exists)
═══════════════════════════════════════════════════════

  STEP 3A-1: Generate main design system
  ─────────────────────────────────────
  Run UUPM with --design-system --persist:

    python3 .claude/skills/ui-ux-pro-max/scripts/search.py \
      "{search_query}" \
      --design-system \
      --persist \
      -p "{PROJECT_NAME}" \
      --output-dir "output/{PROJECT_NAME}/design-system"

  This creates:
    output/{PROJECT_NAME}/design-system/{project-slug}/MASTER.md

  STEP 3A-2: Search landing page patterns
  ────────────────────────────────────────
  Search the "landing" domain for conversion patterns:

    python3 .claude/skills/ui-ux-pro-max/scripts/search.py \
      "{industry} {product_type} landing page conversion" \
      --domain landing \
      --max-results 3

  Extract: section order, CTA placement, color strategy.

  STEP 3A-3: Search color palette
  ───────────────────────────────
  Search the "color" domain for industry-specific colors:

    python3 .claude/skills/ui-ux-pro-max/scripts/search.py \
      "{industry} {product_type}" \
      --domain color \
      --max-results 3

  Extract: primary color hex, CTA color hex, background color, text color.

  STEP 3A-4: Search typography
  ────────────────────────────
  Search for font pairings:

    python3 .claude/skills/ui-ux-pro-max/scripts/search.py \
      "{industry} {mood_keywords}" \
      --domain typography \
      --max-results 3

  Extract: heading font, body font, Google Fonts URL, Tailwind config.

  STEP 3A-5: Search visual style
  ──────────────────────────────
  Search for UI style patterns:

    python3 .claude/skills/ui-ux-pro-max/scripts/search.py \
      "{mood_keywords} {audience_descriptor}" \
      --domain style \
      --max-results 3

  Extract: style category, effects, design system variables.

  STEP 3A-6: Generate page-specific overrides (per ad group)
  ──────────────────────────────────────────────────────────
  FOR EACH ad_group IN niche-brief.ad_groups:
    Build a page-specific query with the ad group's persona tone.

    python3 .claude/skills/ui-ux-pro-max/scripts/search.py \
      "{ad_group_specific_query}" \
      --design-system \
      --persist \
      -p "{PROJECT_NAME}" \
      --page "{ad_group_slug}" \
      --output-dir "output/{PROJECT_NAME}/design-system"

    This creates:
      output/{PROJECT_NAME}/design-system/{project-slug}/pages/{ad-group-slug}.md

  STEP 3A-7: Search stack guidelines (if tech stack known)
  ───────────────────────────────────────────────────────
  IF tech stack is known (from project detection or user input):

    python3 .claude/skills/ui-ux-pro-max/scripts/search.py \
      "landing page performance optimization" \
      --stack {html-tailwind|react|nextjs|astro|vue|svelte} \
      --max-results 3

  Extract: stack-specific do/don't, code patterns, performance tips.

═══════════════════════════════════════════════════════
  PATH B: UUPM IS NOT AVAILABLE (search.py missing)
═══════════════════════════════════════════════════════

  Tell user: "UUPM (UI UX Pro Max) is not installed. Using fallback design rules."

  READ references/fallback-design-rules.md

  Follow these steps:
  1. Match industry to the fallback palette table → get colors
  2. Match mood to the fallback pattern table → get layout pattern
  3. Use default typography: Inter (body) + appropriate heading font
  4. Manually construct MASTER.md from fallback data
  5. Add note at top of MASTER.md:
     "⚠️ Generated from fallback rules (UUPM not available).
      Install UUPM for more precise, data-driven design decisions."
```

Read `references/uupm-integration-guide.md` for the complete UUPM API reference.

## Step 4: Augment with Google Ads Landing Page Rules

UUPM gives generic design intelligence. Landing pages have specific constraints.
ALWAYS merge these rules into MASTER.md, whether UUPM was used or not:

```markdown
## Google Ads Landing Page — Design Overrides

### CTA Button
- Color: MUST contrast with page background at 4.5:1 ratio minimum (WCAG AA)
- Size: minimum 48×48px touch target (WCAG 2.5.5)
- Position: above fold on mobile (visible without scrolling at 375px)
- Copy: action verb + benefit (from ad-copy-suggestions.md)
- Repetition: at least 3 times (hero, after social proof, page end)
- State: distinct hover/active/focus states

### Trust Section
- Position: immediately before OR after primary CTA
- Must include at least 2 of: testimonials, logos, badges, stats
- Real photos preferred over stock
- Numbers should be specific, not rounded ("2,847" not "thousands")

### Form (if lead gen)
- Maximum 3-5 fields for cold traffic
- Name + Phone is minimum viable form
- Name + Phone + Email is maximum for first interaction
- Single column layout on mobile — NEVER side-by-side fields
- Submit button: full width on mobile, matches CTA color
- Progress indicator if multi-step

### Hero Section
- Headline: large, bold, matches ad copy EXACTLY (message match)
- Sub-headline: expands value prop, 1-2 lines max
- NO navigation bar — landing pages are distraction-free
- NO hamburger menu — no navigation at all
- Background: must not compete with text readability (contrast check)
- Mobile: headline must be fully visible at 375px without scrolling

### Typography for Landing Pages
- Headline: ≥ 32px desktop, ≥ 24px mobile
- Body: ≥ 16px always (never smaller)
- Line height: 1.5-1.7 for body text
- Max 2 font families per page
- Font weight: headlines 600-800, body 400

### Spacing
- Section padding: 60-80px vertical on desktop, 40-60px on mobile
- Content max-width: 1200-1440px
- Mobile padding: 16-20px horizontal

### Images
- Hero: real product/service photo or illustration (never generic stock)
- All images: loading="lazy" except hero
- All images: alt text for accessibility
- WebP format preferred for performance
```

## Step 5: Validate and Merge

Before finalizing MASTER.md, validate:

```
CHECKLIST:
[ ] Primary color defined (hex value)
[ ] CTA color defined AND contrasts with background at 4.5:1
[ ] Heading font specified with Google Fonts URL
[ ] Body font specified with Google Fonts URL
[ ] Section order defined
[ ] Mobile breakpoints specified (375px primary)
[ ] CTA placement rules included
[ ] No navigation bar mentioned
[ ] Trust section positioning defined
[ ] Form field limits stated (if applicable)
```

IF any item missing → add it from the LP overrides in Step 4.
IF UUPM output conflicts with LP rules → LP rules WIN (they are conversion-specific).

## Step 6: Generate Output

Save the final design system:

```
output/{PROJECT_NAME}/design-system/MASTER.md          ← Global design system
output/{PROJECT_NAME}/design-system/pages/{page}.md    ← Per-ad-group overrides (if generated)
```

Read `assets/master-md-template.md` for the output structure.

IF UUPM was used → the MASTER.md is UUPM output + LP overrides merged.
IF fallback was used → the MASTER.md is manually constructed from fallback rules + LP overrides.

Show progress:
```
[design-brief] Step 1/6: Reading research inputs...
[design-brief] Step 2/6: Constructing UUPM search query...
[design-brief] Step 3/6: Running UUPM design system generation...
[design-brief]   → Main design system ✅
[design-brief]   → Landing page patterns ✅
[design-brief]   → Color palette ✅
[design-brief]   → Typography ✅
[design-brief]   → Visual style ✅
[design-brief]   → Page overrides: {N} ad groups ✅
[design-brief] Step 4/6: Applying Google Ads LP design overrides...
[design-brief] Step 5/6: Validating design system completeness...
[design-brief] Step 6/6: Saving design system...
[design-brief] ✅ Complete → output/{PROJECT_NAME}/design-system/MASTER.md
```

After saving, tell the user:
```
Next steps:
- Run landing-page-builder: "Build landing page for {PROJECT_NAME}"
- Review MASTER.md and adjust colors/fonts if needed
- Page-specific overrides are in design-system/pages/ for each ad group variant
```

## Error Handling

- **niche-brief.md missing**: STOP. Show error with instruction to run niche-research first.
- **personas.md missing**: Proceed with warning. Use generic audience assumptions.
- **UUPM search.py not found**: Use fallback-design-rules.md. Note in output.
- **UUPM search.py crashes or returns error**: Capture error, show to user, fall back to fallback-design-rules.md. Include error in output notes.
- **UUPM returns empty results**: Try broader query (fewer keywords). If still empty → fallback.
- **Competitor report missing**: Proceed. Design system won't account for competitive differentiation.
- **Tech stack unknown**: Default to html-tailwind. Skip stack-specific UUPM search.
- **Output directory cannot be created**: Report error, suggest checking file permissions.
