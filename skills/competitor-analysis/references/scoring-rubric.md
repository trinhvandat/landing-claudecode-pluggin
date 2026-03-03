# Scoring Rubric — Competitor Landing Page Analysis

Use this rubric when scoring competitors in Step 3. Each dimension is scored 1-10.

## Quick Reference Table

| Dimension | Sub-Metric | Weight | What a 10 Looks Like |
|-----------|-----------|--------|---------------------|
| MESSAGE | Headline clarity | High | Specific benefit, < 10 words, contains keyword |
| MESSAGE | Value prop strength | High | Unique, quantified, compelling |
| MESSAGE | Keyword-headline match | High | Would match Google Ad verbatim |
| STRUCTURE | Section flow | Medium | Follows PAS/AIDA, 6-10 sections |
| STRUCTURE | Content length | Medium | Appropriate for offer complexity |
| STRUCTURE | Above-fold quality | High | Headline + CTA + trust signal visible |
| TRUST | Testimonials | High | Real photos, full names, specific outcomes |
| TRUST | Trust badges | Medium | Relevant industry certifications |
| TRUST | Social proof | Medium | Specific numbers, client logos |
| TRUST | Risk reversal | Medium | Clear, specific guarantee |
| CTA | Copy quality | High | Action verb + benefit |
| CTA | Placement | High | Above fold + repeated 2-3x |
| CTA | Urgency/scarcity | Low | Real deadline or limited availability |
| CTA | Form friction | High | 1-3 fields max |
| DESIGN | Color scheme | Medium | Professional, CTA contrasts at 4.5:1 |
| DESIGN | Typography | Low | Readable, clear hierarchy |
| DESIGN | Visual style | Low | Consistent, matches brand |
| DESIGN | Image usage | Medium | Real photos, optimized, alt text |
| TECH | Framework | Low | Modern, maintained stack |
| TECH | Speed signals | Medium | < 5 scripts, lazy loading, preloaded fonts |
| TECH | Mobile ready | High | Viewport meta, responsive layout |

## Scoring Rules

### DO:
- Score based on evidence you can see in the HTML/content
- Be consistent across competitors — same criteria, same standards
- Note specific examples for scores 8+ or 3- (explain WHY)
- Round to whole numbers only (no 7.5)

### DO NOT:
- Guess about backend performance (you can only see frontend signals)
- Score based on aesthetics alone — effectiveness matters more
- Give inflated scores. A 10 should be genuinely exceptional.
- Compare to unrelated industries. Score relative to THIS niche.

## Dimension Averages — How to Compute

```
MESSAGE score   = avg(headline_clarity, value_prop, keyword_match)
STRUCTURE score = avg(section_flow, content_length, above_fold)
TRUST score     = avg(testimonials, badges, social_proof, risk_reversal)
CTA score       = avg(cta_copy, placement, urgency, form_friction)
DESIGN score    = avg(color, typography, style, images)
TECH score      = avg(framework, speed, mobile)

OVERALL score   = avg(MESSAGE, STRUCTURE, TRUST, CTA, DESIGN, TECH)
```

## Score Interpretation

| Overall Score | Rating | Meaning |
|--------------|--------|---------|
| 8.0 - 10.0 | Excellent | Strong page. Hard to beat — find niche gaps instead. |
| 6.0 - 7.9 | Good | Competent page with clear improvement areas. |
| 4.0 - 5.9 | Average | Significant weaknesses. Beatable on multiple fronts. |
| 1.0 - 3.9 | Weak | Major gaps. Our page should easily outperform. |

## Red Flags to Always Note

Regardless of score, flag these if found:
- No mobile viewport meta tag → **critical mobile failure**
- CTA says only "Submit" or "Gửi" → **CTA copy failure**
- No testimonials or social proof at all → **trust gap**
- Form asks for 6+ fields → **high friction**
- Navigation menu on landing page → **distraction leak**
- No above-fold CTA → **conversion barrier**
- Stock photos with watermarks → **credibility destroyer**
- Broken images or 404 resources → **neglected page**
