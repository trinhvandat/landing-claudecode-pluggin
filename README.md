# landing-page-pro

A Claude Code plugin that automates the full Google Ads landing page workflow — from market research to deployed, conversion-optimized page. 6 skills, 1 pipeline, zero guesswork.

> **Built for**: Marketers, agencies, and developers who run Google Ads campaigns and need high-converting landing pages — fast.

---

## What It Does

**landing-page-pro** turns a client brief into a production-ready landing page through 6 automated skills:

1. **Research** the market (keywords, intent, CPC)
2. **Analyze** competitor landing pages (crawl, score, find gaps)
3. **Create** buyer personas + Google Ads copy (with character-limit verification)
4. **Design** a complete design system (colors, fonts, components)
5. **Build** the landing page (HTML/React/Astro, mobile-first, single CTA)
6. **Audit** the result (7-category score, fix recommendations, A/B tests)

Every decision is research-backed. No guessing colors. No making up headlines. No generic templates.

---

## Pipeline Flow

```
niche-research ──────┐
                     ├──→ audience-persona → design-brief → landing-page-builder → conversion-optimizer
competitor-analysis ─┘
```

- **Skills 1 & 2** run in **parallel** (independent research)
- **Skills 3–6** run **sequentially** (each depends on previous outputs)
- Each skill reads from and writes to `output/{project-name}/`

---

## Quick Start

### Installation

```bash
# Clone the repo
git clone git@github.com:trinhvandat/landing-claudecode-pluggin.git

# Or install as a Claude Code plugin
claude plugin install landing-page-pro
```

### Run the Full Pipeline

Tell Claude your client brief:

```
Research keywords for "Smile Dental" — dental implant clinic in Ho Chi Minh City,
targeting adults 35-55, budget 500k VND/day Google Ads.
```

Claude runs Skill 1 (niche-research), then you continue:

```
Analyze competitors for smile-dental
Create personas for smile-dental
Create design system for smile-dental
Build landing page for smile-dental
Audit landing page for smile-dental
```

Or run the entire pipeline at once with [oh-my-claudecode](https://github.com/nicekid1/oh-my-claudecode):

```
/pipeline niche-research -> competitor-analysis -> audience-persona -> design-brief -> landing-page-builder -> conversion-optimizer "Smile Dental implant clinic TPHCM"
```

---

## Skills Reference

### Skill 1: `niche-research`

**Trigger phrases**: "research keywords", "find niche", "market analysis", "keyword research", "new project", "new campaign", "new client brief"

**What it does**:
- Searches 20–40 keywords via web search (Vietnamese + English)
- Classifies each by intent: TRANSACTIONAL, COMMERCIAL, INFORMATIONAL, NAVIGATIONAL
- Clusters into 3–5 ad groups
- Estimates CPC ranges from public benchmarks
- Generates 10–20 negative keywords

**Output**: `output/{project}/research/niche-brief.md`

**Example output snippet**:
```markdown
## Keyword Cluster: implant-pricing (Priority: P0)
| Keyword | Intent | Est. CPC |
|---------|--------|----------|
| giá implant TPHCM | TRANSACTIONAL | 15,000-25,000 VND |
| trồng răng implant bao nhiêu | TRANSACTIONAL | 20,000-35,000 VND |
| implant trả góp | TRANSACTIONAL | 10,000-20,000 VND |
```

---

### Skill 2: `competitor-analysis`

**Trigger phrases**: "analyze competitors", "check competition", "competitor research", "spy on competitors", "competitive analysis", "what are competitors doing"

**What it does**:
- Crawls 3–5 competitor landing pages via `web_fetch`
- Scores each across 6 dimensions (MESSAGE, STRUCTURE, TRUST, CTA, DESIGN, TECH) on a 1–10 scale
- Identifies common patterns, differentiators, and **gaps** (our opportunity)
- Creates a swipe file of best elements

**Outputs**:
- `output/{project}/research/competitor-report.md`
- `output/{project}/research/swipe-file.md`

**Example scoring**:
```markdown
| Competitor | MSG | STR | TRU | CTA | DES | TEC | AVG |
|-----------|-----|-----|-----|-----|-----|-----|-----|
| Dr. Care  | 8   | 7   | 9   | 7   | 8   | 7   | 7.8 |
| I-Dent    | 7   | 7   | 7   | 6   | 8   | 7   | 7.0 |
| NhaKhoaKim| 6   | 6   | 7   | 5   | 7   | 7   | 6.3 |
```

---

### Skill 3: `audience-persona`

**Trigger phrases**: "create personas", "buyer persona", "target audience", "who is the customer", "ad copy", "write ads", "Google Ads headlines"

**What it does**:
- Creates 2–3 buyer personas from keyword data + competitor gaps
- Generates Google Ads copy per ad group (headlines, descriptions, sitelinks)
- **Verifies every headline/description against Google Ads character limits** (30/90 chars)
- Maps persona → ad group → landing page tone

**Outputs**:
- `output/{project}/research/personas.md`
- `output/{project}/research/ad-copy-suggestions.md`

**Character limit verification**:
```markdown
| # | Headline                        | Chars  | Status |
|---|---------------------------------|--------|--------|
| 1 | Implant Không Đau Từ 15 Triệu  | 30/30  | ✅     |
| 2 | 500+ Ca Implant Thành Công      | 26/30  | ✅     |
```

> Vietnamese diacritics (ă, â, ê, ô, ơ, ư, đ) each count as 1 character.

---

### Skill 4: `design-brief`

**Trigger phrases**: "create design system", "design brief", "design the page", "colors and fonts", "visual style", "branding for landing page"

**What it does**:
- **With UUPM installed**: Runs 7 UUPM queries (design-system, landing patterns, color, typography, style, page overrides, stack guidelines)
- **Without UUPM**: Uses fallback design rules (industry-matched palettes and patterns)
- Merges Google Ads landing page–specific design overrides (CTA sizing, touch targets, no-nav rules)
- Validates contrast ratios and accessibility

**Output**: `output/{project}/design-system/MASTER.md`

**Example design tokens**:
```markdown
## Color Palette
| Role        | Hex       | Usage                              |
|-------------|-----------|-------------------------------------|
| Primary     | #0E7490   | Headers, trust elements (teal)      |
| CTA         | #F97316   | All CTA buttons (orange, high contrast) |
| Background  | #FFFFFF   | Page background                     |
| Surface     | #F0FDFA   | Card backgrounds (light teal tint)  |
```

---

### Skill 5: `landing-page-builder`

**Trigger phrases**: "build landing page", "create the page", "generate HTML", "code the landing page", "build the LP", "make the page"

**What it does**:
- Auto-detects tech stack (HTML+Tailwind / React+Next.js / Astro) or asks
- Generates all 9 sections: Hero, Stats, Pain Points, Benefits, Social Proof, How It Works, FAQ, Final CTA, Footer
- Message-matches h1 to ad headline **word for word**
- Adds Google Ads integration: GTM, DKI (Dynamic Keyword Insertion), conversion tracking, UTM support
- Adds schema markup (FAQPage + LocalBusiness/Product)
- Runs 18-item pre-delivery checklist before saving

**Output**: `output/{project}/src/index.html` (or `.tsx` / `.astro`)

**Build rules enforced**:
- Mobile-first (375px primary viewport)
- Single CTA repeated 3x (hero + after proof + form)
- **Zero navigation** — no nav bar, no hamburger menu
- Touch targets ≥ 48px, body font ≥ 16px
- CTA contrast ≥ 4.5:1 (WCAG AA)

---

### Skill 6: `conversion-optimizer`

**Trigger phrases**: "audit landing page", "optimize conversions", "check my page", "score the landing page", "CRO audit", "what should I improve", "review the page"

**What it does**:
- Scores the page across **7 weighted categories** (28 sub-metrics):

| Category | Weight | What It Checks |
|----------|--------|----------------|
| Message Match | 20% | h1 vs ad headline, keywords, value prop clarity |
| CTA Effectiveness | 20% | Above fold, copy quality, contrast, repetition |
| Trust & Social Proof | 15% | Testimonials, badges, specific numbers, real photos |
| Page Speed Signals | 15% | Image optimization, script count, CSS, font loading |
| Mobile Experience | 15% | Viewport, touch targets, font size, single column |
| Content Quality | 10% | Readability, benefit focus, objection handling, emotion |
| Technical SEO | 5% | Schema, meta tags, OG/Twitter, canonical |

- Generates prioritized fixes: Critical → Quick Wins → Nice to Have
- Suggests 2–3 A/B tests with hypotheses and metrics
- Works in **standalone mode** (no research context) or **full mode** (with research)

**Output**: `output/{project}/audit/optimization-report.md`

---

## Output Structure

Every project generates this file tree:

```
output/{project-name}/
├── research/
│   ├── niche-brief.md              ← Keywords, intent, CPC, ad groups
│   ├── competitor-report.md        ← Scored competitor analysis
│   ├── swipe-file.md               ← Best elements from competitors
│   ├── personas.md                 ← 2-3 buyer personas
│   └── ad-copy-suggestions.md      ← Ad headlines, descriptions, CTAs
├── design-system/
│   ├── MASTER.md                   ← Colors, fonts, components, spacing
│   └── pages/                      ← Per-ad-group design overrides
├── src/
│   └── index.html                  ← Production-ready landing page
└── audit/
    └── optimization-report.md      ← Score, fixes, A/B tests
```

---

## Dependencies

### Required

- **Claude Code** — This is a Claude Code plugin. Requires Claude Code CLI.

### Optional (Recommended)

- **[UI UX Pro Max (UUPM)](https://github.com/nicekid1/ui-ux-pro-max)** — Design intelligence engine. Provides data-driven color palettes, font pairings, and style patterns based on 50+ design styles, 21 palettes, and 50 font pairings. Without UUPM, Skill 4 falls back to built-in industry-matched design rules.

  ```bash
  # Install UUPM as a Claude Code skill
  # It should appear at: .claude/skills/ui-ux-pro-max/
  ```

- **[oh-my-claudecode (OMC)](https://github.com/nicekid1/oh-my-claudecode)** — Multi-agent orchestration. Enables:
  - `/pipeline` — Run all 6 skills in sequence with one command
  - `swarm` — Run Skills 1 & 2 in parallel, then pipeline the rest
  - `eco mode` — Token-saving variant with smaller models for research

  Without OMC, each skill runs independently via natural language prompts.

---

## Real-World Example: Smile Dental

Full pipeline test run for a dental implant clinic in Ho Chi Minh City:

**Input**:
> Client: Smile Dental, TPHCM. Service: dental implants. Budget: 500k VND/day. Target: adults 35–55.

**Results** (from actual test run in `output/smile-dental/`):

| Skill | Key Output |
|-------|-----------|
| niche-research | 28 keywords across 4 clusters, CPC 3k–50k VND |
| competitor-analysis | 3 competitors scored (6.3–7.8/10), found 8 competitive gaps |
| audience-persona | 2 personas (Chị Hạnh price-focused, Anh Minh quality-focused), verified ad copy |
| design-brief | Teal #0E7490 + Orange #F97316, Inter font, 9-section layout |
| landing-page-builder | 556-line HTML+Tailwind page, 3 CTAs, FAQPage schema, DKI support |
| conversion-optimizer | **Score: 97.75/100** — only 2 items to fix (placeholder photos, Tailwind CDN) |

**Competitive advantages over all 3 analyzed competitors**:
- CTA above fold (competitors hide it below)
- No navigation menu (competitors all have nav = traffic leak)
- Pain points section with PAS framework (none address patient fears in hero)
- 2-field form (competitors use 4+ fields)
- Explicit guarantee text (no competitor offers this)

---

## Tech Stack Support

| Stack | Status | File Output |
|-------|--------|------------|
| HTML + Tailwind CSS | Full support (default) | `src/index.html` |
| React / Next.js | Supported | `src/app/page.tsx` + components |
| Astro | Supported | `src/pages/index.astro` + components |

Stack is auto-detected from project files or selected by user.

---

## Configuration

### CLAUDE.md

The project includes `CLAUDE.md` at the root with core rules that Claude follows:
- Research before code (always)
- Message match is sacred (h1 = ad headline)
- UUPM first, fallback second
- Mobile-first, speed-first, single CTA
- No navigation menus on landing pages

### Orchestration (with OMC)

```
orchestration/
├── pipeline.md       ← Sequential 6-skill pipeline prompts
└── swarm-config.md   ← Parallel research + sequential build prompts
```

---

## Error Handling

Every skill handles common failures gracefully:

| Failure | Behavior |
|---------|----------|
| `web_search` unavailable | Retry → ask user for manual keywords → proceed with warning |
| `web_fetch` blocked/timeout | Try URL variations → ask for pasted HTML → skip with logged failure |
| Previous skill output missing | Clear error: "Run {skill-name} first" — never proceeds silently |
| UUPM not installed | Falls back to `fallback-design-rules.md` with note in output |
| Google Ads char limit exceeded | Auto-rewrites shorter, shows ❌→✅ verification |
| SPA/JS-rendered page | Asks user to paste rendered HTML from DevTools |

---

## License

MIT

---

## Author

Built by Leonard with Claude Code.
