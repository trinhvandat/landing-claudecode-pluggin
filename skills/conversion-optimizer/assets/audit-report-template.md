# Optimization Report: {PROJECT_NAME}

**Generated**: {DATE}
**Page audited**: {URL_OR_FILE_PATH}
**Audit mode**: {FULL / STANDALONE (no research context)}

---

## Overall Score: {TOTAL}/100 — {RATING}

| Rating | Range |
|--------|-------|
| Excellent | 80-100 |
| Good | 60-79 |
| Needs Work | 40-59 |
| Poor | 0-39 |

---

## Category Scores

| # | Category | Raw Score | Weight | Weighted Score |
|---|----------|-----------|--------|----------------|
| 1 | Message Match | {SCORE}/100 | 20% | {WEIGHTED} |
| 2 | CTA Effectiveness | {SCORE}/100 | 20% | {WEIGHTED} |
| 3 | Trust & Social Proof | {SCORE}/100 | 15% | {WEIGHTED} |
| 4 | Page Speed Signals | {SCORE}/100 | 15% | {WEIGHTED} |
| 5 | Mobile Experience | {SCORE}/100 | 15% | {WEIGHTED} |
| 6 | Content Quality | {SCORE}/100 | 10% | {WEIGHTED} |
| 7 | Technical SEO | {SCORE}/100 | 5% | {WEIGHTED} |
| | **TOTAL** | | | **{TOTAL}/100** |

---

## Detailed Breakdown

### 1. Message Match ({SCORE}/100, weighted: {WEIGHTED})

| Sub-Metric | Score | Evidence |
|-----------|-------|---------|
| Headline matches ad copy | {SCORE}/40 | h1: "{ACTUAL_H1}" / expected: "{EXPECTED_H1}" |
| Keywords in first 100 words | {SCORE}/30 | Found: {KEYWORDS_FOUND} |
| Value prop clear in 5 sec | {SCORE}/30 | Above fold: {DESCRIPTION} |

### 2. CTA Effectiveness ({SCORE}/100, weighted: {WEIGHTED})

| Sub-Metric | Score | Evidence |
|-----------|-------|---------|
| CTA above fold | {SCORE}/25 | {YES_AT_POSITION / NO} |
| CTA copy quality | {SCORE}/25 | CTA text: "{ACTUAL_CTA}" |
| CTA color contrast | {SCORE}/25 | {CONTRAST_DESCRIPTION} |
| CTA repeated after proof | {SCORE}/25 | {COUNT} CTAs at positions: {POSITIONS} |

### 3. Trust & Social Proof ({SCORE}/100, weighted: {WEIGHTED})

| Sub-Metric | Score | Evidence |
|-----------|-------|---------|
| Testimonials | {SCORE}/30 | {COUNT} testimonials, {DETAIL_LEVEL} |
| Trust badges | {SCORE}/25 | {BADGES_FOUND} |
| Specific numbers | {SCORE}/25 | {NUMBERS_FOUND} |
| Real names/photos | {SCORE}/20 | {REAL_VS_STOCK} |

### 4. Page Speed Signals ({SCORE}/100, weighted: {WEIGHTED})

| Sub-Metric | Score | Evidence |
|-----------|-------|---------|
| Image optimization | {SCORE}/30 | {IMG_COUNT} images, {LAZY_COUNT} lazy, {ALT_COUNT} with alt |
| Script count | {SCORE}/25 | {SCRIPT_COUNT} scripts |
| CSS approach | {SCORE}/25 | {CSS_DESCRIPTION} |
| Font loading | {SCORE}/20 | {FONT_STRATEGY} |

### 5. Mobile Experience ({SCORE}/100, weighted: {WEIGHTED})

| Sub-Metric | Score | Evidence |
|-----------|-------|---------|
| Viewport meta | {SCORE}/20 | {PRESENT_WITH_CONTENT / MISSING} |
| Touch targets ≥ 48px | {SCORE}/25 | {ASSESSMENT} |
| Font size ≥ 16px | {SCORE}/25 | Body: {FONT_SIZE} |
| Single column mobile | {SCORE}/30 | {ASSESSMENT} |

### 6. Content Quality ({SCORE}/100, weighted: {WEIGHTED})

| Sub-Metric | Score | Evidence |
|-----------|-------|---------|
| Readability | {SCORE}/30 | {WORD_COUNT} words, {PARAGRAPH_ASSESSMENT} |
| Benefit-focused | {SCORE}/30 | {BENEFIT_VS_FEATURE} |
| Addresses objections | {SCORE}/20 | FAQ: {PRESENT_WITH_COUNT / MISSING} |
| Emotional triggers | {SCORE}/20 | {TRIGGERS_FOUND} |

### 7. Technical SEO ({SCORE}/100, weighted: {WEIGHTED})

| Sub-Metric | Score | Evidence |
|-----------|-------|---------|
| Schema markup | {SCORE}/30 | {SCHEMAS_FOUND} |
| Meta title + description | {SCORE}/25 | Title: {PRESENT/MISSING}, Desc: {PRESENT/MISSING} |
| OG/Twitter Card | {SCORE}/25 | {TAGS_FOUND} |
| Canonical URL | {SCORE}/20 | {PRESENT / MISSING} |

---

## Fix Recommendations

### Critical Fixes (do immediately)

{FOR_EACH_CRITICAL}
**{NUMBER}. {PROBLEM}**
- Current: {CURRENT_STATE}
- Fix: {SPECIFIC_ACTION}
- Impact: +{ESTIMATED_POINTS} points
- Effort: {ESTIMATED_TIME}
{END_FOR}

### Quick Wins (do next, <30 min each)

{FOR_EACH_QUICK_WIN}
**{NUMBER}. {PROBLEM}**
- Current: {CURRENT_STATE}
- Fix: {SPECIFIC_ACTION}
- Impact: +{ESTIMATED_POINTS} points
- Effort: {ESTIMATED_TIME}
{END_FOR}

### Nice to Have (backlog)

{FOR_EACH_NICE_TO_HAVE}
- {PROBLEM} → {FIX} (est. +{POINTS} pts)
{END_FOR}

---

## A/B Test Suggestions

### Test 1: {TEST_NAME}
- **Element**: {WHAT_TO_CHANGE}
- **Control (A)**: "{CURRENT_VERSION}"
- **Variant B**: "{ALTERNATIVE_1}"
- **Variant C**: "{ALTERNATIVE_2}"
- **Hypothesis**: {WHY_VARIANT_MIGHT_WIN}
- **Metric**: {WHAT_TO_MEASURE}
- **Priority**: {HIGH / MEDIUM / LOW}
- **Effort**: {IMPLEMENTATION_TIME}

### Test 2: {TEST_NAME}
{SAME_FORMAT}

### Test 3: {TEST_NAME}
{SAME_FORMAT — OPTIONAL}

---

## Score After Fixes (estimated)

| Scenario | Estimated Score |
|----------|----------------|
| Current | {CURRENT}/100 |
| After critical fixes | {ESTIMATED}/100 |
| After critical + quick wins | {ESTIMATED}/100 |
| After all fixes | {ESTIMATED}/100 |

---

## Next Steps
- [ ] Implement critical fixes immediately
- [ ] Set up A/B test #{HIGHEST_PRIORITY_TEST}
- [ ] Re-audit after fixes: "Audit landing page for {PROJECT_NAME}"
- [ ] Monitor conversion rate for 2 weeks before next optimization round
