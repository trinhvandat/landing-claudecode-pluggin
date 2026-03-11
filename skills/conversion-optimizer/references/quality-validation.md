# Quality Validation Guide

> How to determine if landing page output is actually good — beyond the plugin's self-audit.

## The Validation Gap

The conversion-optimizer scores pages against its own criteria. This guide provides **external validation** to answer: "Is this page actually good?"

```
Plugin self-audit: 40% confidence
+ Human review:    +20% confidence
+ External tools:  +10% confidence
+ Real traffic:    100% confidence (the only true test)
```

---

## 1. Industry Benchmarks

### Conversion Rate by Industry (Google Ads Landing Pages)

| Industry | Average CVR | Good CVR | Excellent CVR |
|----------|-------------|----------|---------------|
| Dental/Medical | 3.5% | 5% | 8%+ |
| Legal Services | 2.5% | 4% | 6%+ |
| Home Services | 3% | 5% | 7%+ |
| E-commerce | 2% | 3.5% | 5%+ |
| SaaS/Software | 3% | 5% | 7%+ |
| Education | 4% | 6% | 9%+ |
| Real Estate | 2.5% | 4% | 6%+ |
| Finance | 2% | 3.5% | 5%+ |

*Sources: Unbounce Conversion Benchmark Report, WordStream Industry Benchmarks*

### Page Structure Standards

| Element | Minimum | Recommended | Excellent |
|---------|---------|-------------|-----------|
| Total sections | 5 | 7-9 | 9 |
| Word count | 300 | 500-1000 | 800-1200 |
| CTA instances | 2 | 3-4 | 4-5 |
| Testimonials | 2 | 3-4 | 5+ with video |
| Trust badges | 2 | 3-4 | 5+ |
| FAQ items | 3 | 5-6 | 8+ |
| Form fields | 2-3 | 2-3 | 2 (name + phone) |

### Page Speed Targets

| Metric | Poor | Acceptable | Good | Target |
|--------|------|------------|------|--------|
| Load time | > 5s | 3-5s | 2-3s | < 2s |
| Lighthouse Performance | < 50 | 50-70 | 70-90 | 90+ |
| Lighthouse Accessibility | < 70 | 70-85 | 85-95 | 95+ |
| Lighthouse SEO | < 80 | 80-90 | 90-95 | 95+ |
| First Contentful Paint | > 3s | 2-3s | 1-2s | < 1s |
| Largest Contentful Paint | > 4s | 2.5-4s | 1-2.5s | < 1s |

---

## 2. Human Review Checklist (5 Minutes)

Complete this before deploying any landing page.

### First Impression Test (5-Second Rule)

View the page for exactly 5 seconds, then answer WITHOUT scrolling back:

- [ ] **What is being sold?** (If you can't answer → h1 is unclear)
- [ ] **Who is it for?** (If you can't answer → value prop is weak)
- [ ] **What should I do next?** (If you can't answer → CTA is not visible)
- [ ] **Is this trustworthy?** (Gut feeling: yes/no/uncertain)

**Score**: 4/4 = Pass, 3/4 = Review needed, ≤2/4 = Redesign hero section

### Mobile Device Test (Use Actual Phone)

Open the page on your phone (not browser emulator):

- [ ] Page loads in under 3 seconds on 4G
- [ ] Text is readable without zooming
- [ ] CTA button is tappable with thumb (not too small, not at edge)
- [ ] No horizontal scrolling required
- [ ] Form is easy to fill (keyboard doesn't cover inputs)
- [ ] Phone number is tappable (opens dialer)

**Score**: 6/6 = Pass, 5/6 = Minor fix, ≤4/6 = Mobile needs rework

### Message Match Verification

Compare to your Google Ads:

- [ ] Landing page h1 matches ad headline **exactly** (word for word)
- [ ] Landing page delivers what the ad promises
- [ ] Keyword from ad appears in first paragraph
- [ ] Visual tone matches ad expectations

**Score**: 4/4 = Pass, 3/4 = Fix headline, ≤2/4 = Message mismatch risk

### Trust Verification (Be Skeptical)

Ask yourself honestly:

- [ ] Would YOU give your phone number to this page?
- [ ] Are testimonials believable? (Specific names, realistic stories)
- [ ] Can you verify the business is real? (Address, phone, Google Maps)
- [ ] Are trust badges legitimate? (Not just random icons)
- [ ] Is there a way to contact before committing? (Phone, chat)

**Score**: 5/5 = Strong trust, 4/5 = Acceptable, ≤3/5 = Trust issues

### Competitor Comparison

Open top competitor's page side-by-side:

- [ ] Is your headline clearer?
- [ ] Is your CTA more compelling?
- [ ] Do you have more/better trust signals?
- [ ] Does your page look more professional?
- [ ] Would you choose your page over theirs?

**Score**: 5/5 = Competitive advantage, 3-4/5 = Comparable, ≤2/5 = Rethink strategy

---

## 3. External Tool Validation

### HTML Validation

1. Go to: https://validator.w3.org/#validate_by_input
2. Paste your HTML
3. Target: **0 errors** (warnings are acceptable)

Common issues to fix:
- Unclosed tags
- Missing alt attributes
- Duplicate IDs
- Invalid attribute values

### Lighthouse Audit

1. Open page in Chrome
2. DevTools → Lighthouse tab → Generate report
3. Targets:
   - Performance: > 90
   - Accessibility: > 90
   - Best Practices: > 90
   - SEO: > 90

If < 90 on any category, address the specific issues listed.

### Accessibility Quick Check

1. Go to: https://wave.webaim.org/
2. Enter your page URL (must be deployed)
3. Target: **0 errors** (alerts are acceptable but review them)

Key accessibility requirements:
- All images have alt text
- Form fields have labels
- Color contrast is sufficient
- Focus states are visible

### Mobile-Friendly Test

1. Go to: https://search.google.com/test/mobile-friendly
2. Enter your page URL
3. Target: **Page is mobile-friendly** (green result)

### PageSpeed Insights

1. Go to: https://pagespeed.web.dev/
2. Enter your page URL
3. Check both Mobile and Desktop
4. Target: **Green scores** (90+) on both

---

## 4. Post-Launch Success Criteria

### When to Consider the Page "Validated"

The page is validated when ALL of these are true:

```
[ ] 100+ ad clicks received
[ ] Conversion rate is within industry benchmark (see Section 1)
[ ] Cost per lead is sustainable for business model
[ ] No critical issues reported by users
[ ] Bounce rate < 70%
[ ] Average time on page > 30 seconds
```

### Warning Signs (Take Action)

| Signal | What It Means | Action |
|--------|---------------|--------|
| CVR < 1% | Page is failing | Stop ads, review/rebuild |
| Bounce rate > 80% | Message mismatch or slow load | Check headline vs ad, check speed |
| Time on page < 15s | Not engaging | Improve above-fold content |
| Form abandonment > 70% | Form friction | Reduce fields or add incentive |
| High mobile bounce | Mobile issues | Test on real device |
| CTR high but CVR low | Curiosity click, not intent | Refine ad targeting |

### When to Iterate vs. Rebuild

**Iterate** (tweak existing page) when:
- CVR is 2-4% but you want 5%+
- Most metrics are healthy, one is weak
- A/B test shows clear winner direction

**Rebuild** (start from scratch) when:
- CVR is < 1% after 200+ clicks
- Multiple fundamental issues (message, trust, mobile)
- Competitor research shows completely different approach works
- Business offering has changed significantly

---

## 5. Validation Scorecard

Use this scorecard to track validation status:

```markdown
## Validation Scorecard: {PROJECT_NAME}

### Pre-Deployment
- [ ] Plugin audit score: ___/100 (target: 80+)
- [ ] Human review: ___/24 checks passed
- [ ] HTML validation: ___ errors (target: 0)
- [ ] Lighthouse scores: P___ A___ BP___ SEO___ (target: 90+ each)
- [ ] Mobile-friendly test: Pass / Fail
- [ ] Competitor comparison: Better / Equal / Worse

### Post-Launch (after 100+ clicks)
- [ ] Conversion rate: ___% (benchmark: ___%)
- [ ] Cost per lead: $___ (sustainable: Yes / No)
- [ ] Bounce rate: ___% (target: < 70%)
- [ ] Avg time on page: ___s (target: > 30s)

### Verdict
- [ ] VALIDATED — Page is performing well
- [ ] ITERATE — Tweak specific elements
- [ ] REBUILD — Fundamental issues found
```

---

## Summary

| Validation Layer | When | Confidence Added |
|-----------------|------|------------------|
| Plugin self-audit | Before delivery | 40% |
| Human review checklist | Before deployment | +20% |
| External tools (Lighthouse, validators) | Before deployment | +10% |
| Competitor comparison | Before deployment | +5% |
| **Real conversion data** | **After 100+ clicks** | **= 100%** |

**The only true validation is real traffic converting at a sustainable cost.**

Everything before that is educated prediction. Use all layers to maximize confidence before spending ad budget.
