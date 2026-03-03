---
name: audience-persona
description: "Create buyer personas and Google Ads copy suggestions for a landing page project. Use when user says 'create personas', 'who is the audience', 'buyer persona', 'target audience', 'ad copy', 'write ads', 'Google Ads headlines', 'who are we targeting', or wants to understand the audience before building a landing page."
---

# Audience Persona — Buyer Profiles & Ad Copy Generator

You are running the audience-persona skill. Your job: create 2-3 buyer personas from research data, then generate Google Ads copy that will be message-matched to the landing page.

## Step 1: Read Research Inputs (DO NOT SKIP)

Check for these files and read them:

```
REQUIRED (refuse to proceed without at least one):
  output/{PROJECT_NAME}/research/niche-brief.md

RECOMMENDED (use if available, proceed without):
  output/{PROJECT_NAME}/research/competitor-report.md

IF niche-brief.md does NOT exist
  → Stop. Tell user:
    "⚠️ Required input not found: output/{PROJECT_NAME}/research/niche-brief.md
     → Run niche-research skill first: 'Research keywords for {PROJECT_NAME}'"
  → Do NOT proceed. Do NOT generate personas from guesswork.

IF competitor-report.md exists
  → Read it. Use competitor messaging patterns to inform persona pain points and objections.
  → Note gaps from competitor analysis — these become our personas' unmet needs.

IF competitor-report.md does NOT exist
  → Proceed. Add note: "Personas generated without competitor analysis context."
```

Extract from niche-brief:
- Keyword clusters and their intent types
- Ad group names
- Target market (geo, language)
- Product/service details

## Step 2: Identify 2-3 Buyer Segments

From the keyword clusters and competitor messaging, identify distinct buyer types.

Use this decision tree:

```
IF keywords show price-sensitivity ("giá", "rẻ", "cheap", "bao nhiêu", "cost")
  → Create: PRICE-CONSCIOUS segment
  → Tone: reassuring about value, transparent pricing
  → Objection: "too expensive"

IF keywords show quality focus ("tốt nhất", "uy tín", "premium", "best", "top")
  → Create: QUALITY-SEEKING segment
  → Tone: authoritative, proof-heavy
  → Objection: "how do I know this is actually good?"

IF keywords show urgency ("gấp", "ngay", "emergency", "urgent", "now")
  → Create: URGENT-NEED segment
  → Tone: direct, fast, reassuring
  → Objection: "can they handle this quickly?"

IF keywords show research behavior ("so sánh", "review", "compare", "vs", "đánh giá")
  → Create: COMPARISON-SHOPPER segment
  → Tone: detailed, data-driven, comparative
  → Objection: "why this over alternatives?"

IF keywords show location focus ("gần đây", "near me", "ở {city}", "{district}")
  → Create: LOCAL-SEEKER segment
  → Tone: familiar, community-oriented
  → Objection: "is this convenient for me?"
```

Rules:
- Create EXACTLY 2-3 personas. Not 1, not 5.
- Each persona MUST map to at least one ad group from the niche-brief.
- If only 1 segment is obvious, split by demographics (age, device preference).
- Give each persona a Vietnamese name if the market is Vietnamese, English name otherwise.

## Step 3: Build Persona Cards

For EACH persona, fill this structure. Read `assets/persona-template.md` for the output format.

```
## Persona: {HUMAN_NAME} — "{SEGMENT_LABEL}"

- **Age**: {range, e.g., 35-50}
- **Occupation**: {type}
- **Income**: {range}
- **Location**: {city/region}
- **Device**: {mobile % vs desktop %}
- **Pain Points**:
  1. {specific problem — NOT generic}
  2. {specific problem}
  3. {specific problem}
- **Goals**: {what they want to achieve by buying}
- **Objections**: {top 3 reasons they might NOT buy}
  1. {objection}
  2. {objection}
  3. {objection}
- **Buying Triggers**: {what pushes them to act NOW}
- **Search Behavior**: {what they Google, at what time of day, on what device}
- **Preferred Tone**: {formal / casual / urgent / reassuring / data-driven}
- **Maps to Ad Group**: {which ad group from niche-brief}
```

Rules:
- Pain points must be SPECIFIC to the product/niche, not generic.
  BAD: "wants a good product"
  GOOD: "worried implant surgery will be painful and require weeks of recovery"
- Objections must be real barriers to purchase.
  BAD: "doesn't want to spend money"
  GOOD: "has seen horror stories of failed implants on forums, fears choosing wrong clinic"
- Each persona MUST have a different preferred tone — this drives ad copy variation.

Read `references/persona-framework.md` for detailed guidance on building realistic personas.

## Step 4: Generate Ad Copy Suggestions

For EACH ad group from the niche-brief, generate ad copy. Read `references/ad-copy-formulas.md` for copywriting frameworks.

### CHARACTER LIMITS — ABSOLUTE, NON-NEGOTIABLE

```
┌─────────────────────────────────────────────────────┐
│  Google Ads Character Limits — HARD LIMITS          │
│                                                     │
│  Headline:              30 characters max           │
│  Description:           90 characters max           │
│  Display URL path:      15 characters each (×2)     │
│  Sitelink title:        25 characters max           │
│  Sitelink description:  35 characters per line (×2) │
│                                                     │
│  Vietnamese: ă, â, ê, ô, ơ, ư, đ = 1 char each    │
│  Spaces count as characters.                        │
│  Punctuation counts as characters.                  │
└─────────────────────────────────────────────────────┘

BEFORE writing any ad copy:
  COUNT the characters.
  IF over limit → rewrite shorter.
  NEVER truncate mid-word.
  NEVER exceed the limit and add "(shortened)" — just write it correctly.
```

### For EACH ad group, generate:

**3 Headlines** (max 30 chars each):
```
Headline 1: Primary keyword + benefit (matches landing page h1)
Headline 2: Social proof or differentiator
Headline 3: CTA or urgency
```

**2 Descriptions** (max 90 chars each):
```
Description 1: Expand on value proposition, address primary objection
Description 2: Trust signal + CTA + urgency element
```

**2 CTA Variations**:
```
CTA 1: Action verb + specific benefit (for landing page button)
CTA 2: Lower-commitment alternative (for secondary CTA)
```

**4 Sitelink Suggestions** (max 25 char titles):
```
Sitelink 1: {pricing/offer page}
Sitelink 2: {testimonials/results}
Sitelink 3: {about/trust page}
Sitelink 4: {contact/location}
```

### Character Count Verification

After generating ALL copy, run this check:
```
FOR EACH headline:
  count = len(headline)
  IF count > 30 → REWRITE. Show: "❌ '{headline}' = {count} chars (max 30) → rewriting..."
  IF count ≤ 30 → Show: "✅ '{headline}' = {count} chars"

FOR EACH description:
  count = len(description)
  IF count > 90 → REWRITE. Show: "❌ '{description}' = {count} chars (max 90) → rewriting..."
  IF count ≤ 90 → Show: "✅ '{description}' = {count} chars"
```

ALWAYS show this verification in the output. The user must see proof that limits are met.

## Step 5: Map Persona → Ad Group → Landing Page Tone

Create a mapping table that connects everything:

```
| Persona | Ad Group | Headline (from Step 4) | LP Tone | Key Objection to Address |
|---------|----------|----------------------|---------|------------------------|
| {NAME}  | {GROUP}  | "{HEADLINE}"         | {TONE}  | {OBJECTION}            |
```

This table is the bridge between research and design. The design-brief skill will use it to set visual tone per landing page variant.

## Step 6: Generate Outputs

Fill templates and save:

```
output/{PROJECT_NAME}/research/personas.md          ← Persona cards
output/{PROJECT_NAME}/research/ad-copy-suggestions.md ← Ad copy with char counts
```

Read `assets/persona-template.md` and `assets/ad-copy-template.md` for output formats.

Show progress:
```
[audience-persona] Step 1/6: Reading research inputs...
[audience-persona] Step 2/6: Identifying buyer segments...
[audience-persona] Step 3/6: Building persona cards...
[audience-persona] Step 4/6: Generating ad copy...
[audience-persona] Step 5/6: Mapping persona → ad group → LP tone...
[audience-persona] Step 6/6: Saving outputs...
[audience-persona] ✅ Complete → output/{PROJECT_NAME}/research/personas.md
[audience-persona] ✅ Complete → output/{PROJECT_NAME}/research/ad-copy-suggestions.md
```

After saving, tell the user:
```
Next steps:
- Run design-brief: "Create design system for {PROJECT_NAME}"
- Review ad copy character counts — all within Google Ads limits
- Use the persona → ad group mapping to plan LP variants
```

## Error Handling

- **niche-brief.md missing**: STOP. Show error with instruction to run niche-research first. Do NOT generate personas without research data.
- **competitor-report.md missing**: Proceed with warning. Personas will be less informed about competitive landscape.
- **Character limit exceeded in ad copy**: Rewrite shorter. Never truncate mid-word. Never deliver over-limit copy.
- **Only 1 buyer segment identifiable**: Split by demographics (age or device). Always deliver 2-3 personas.
- **Vietnamese diacritics in character counting**: Each diacritic character (ă, â, ê, ô, ơ, ư, đ) counts as 1 character. Do NOT count the diacritic mark separately.
- **web_search unavailable** (for enriching persona data): Use niche-brief data alone. Add note: "Personas based on keyword data only. Enrich with customer interview data if available."
