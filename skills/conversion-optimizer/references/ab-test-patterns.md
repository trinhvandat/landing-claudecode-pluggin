# A/B Test Patterns for Landing Pages

Reference for Step 5 of the conversion-optimizer skill. Common test variations organized by element.

## Testing Principles

1. **One variable per test** — change only one element to isolate impact.
2. **Statistical significance** — need ~1000 visitors per variant minimum for reliable results.
3. **Test duration** — run for at least 2 full business weeks (cover weekday + weekend patterns).
4. **Priority** — test highest-impact elements first: headline > CTA > social proof > layout.

---

## Headline Tests

### H-1: Benefit vs Feature Headline
```
Control:    "Công Nghệ Implant Hiện Đại Nhất"     (feature)
Variant B:  "Trồng Răng Không Đau — Ăn Nhai Ngay" (benefit)
Hypothesis: Benefit-focused headlines address the reader's goal directly,
            increasing engagement over feature descriptions.
Metric:     Scroll depth past hero, time on page
```

### H-2: Specific Number vs General Claim
```
Control:    "Nha Khoa Uy Tín Hàng Đầu"            (general)
Variant B:  "2,847 Ca Implant Thành Công Từ 2010"  (specific)
Hypothesis: Specific numbers create credibility and curiosity,
            outperforming vague trust claims.
Metric:     CTR on primary CTA
```

### H-3: Question vs Statement Headline
```
Control:    "Giải Pháp Implant Tốt Nhất"           (statement)
Variant B:  "Mất Răng? Đây Là Giải Pháp Vĩnh Viễn" (question + answer)
Hypothesis: Question headlines create a pattern interrupt and
            engage problem-aware visitors.
Metric:     Bounce rate, scroll depth
```

---

## CTA Tests

### C-1: Generic vs Benefit CTA
```
Control:    "Đăng Ký"                                (generic)
Variant B:  "Đặt Lịch Tư Vấn Miễn Phí"             (action + benefit)
Hypothesis: Specific benefit in CTA reduces hesitation.
Metric:     CTA click rate, form submissions
```

### C-2: CTA Color Contrast
```
Control:    CTA in brand primary color (low contrast)
Variant B:  CTA in high-contrast complementary color
Hypothesis: Higher visual contrast draws attention to the action.
Metric:     CTA click rate
```

### C-3: CTA with Urgency vs Without
```
Control:    "Đặt Lịch Ngay"
Variant B:  "Đặt Lịch Ngay — Chỉ Còn 5 Suất Hôm Nay"
Hypothesis: Scarcity motivates immediate action over procrastination.
Metric:     CTA click rate, form submissions
Caution:    Only use real scarcity. Fake urgency erodes trust long-term.
```

### C-4: Single CTA vs Phone + Form
```
Control:    Form CTA only
Variant B:  Form CTA + click-to-call phone button
Hypothesis: Adding phone option captures high-intent visitors
            who prefer immediate human contact.
Metric:     Total conversions (form + calls)
```

---

## Social Proof Tests

### S-1: Testimonial Format
```
Control:    Text-only testimonial quotes
Variant B:  Photo + name + quote + specific result
Hypothesis: Identifiable people with measurable outcomes
            are more persuasive than anonymous quotes.
Metric:     Scroll-past rate of testimonial section, CTA clicks after section
```

### S-2: Stats Bar Position
```
Control:    Stats bar below hero section
Variant B:  Stats bar above fold, integrated into hero
Hypothesis: Immediate social proof reduces bounce by
            establishing credibility before any content is consumed.
Metric:     Bounce rate, scroll depth
```

### S-3: Review Score Display
```
Control:    "Khách hàng hài lòng" (no specifics)
Variant B:  "4.9/5 ★★★★★ trên Google Reviews (327 đánh giá)"
Hypothesis: Third-party review scores with specific counts
            are more credible than self-reported satisfaction.
Metric:     Trust section engagement, CTA clicks
```

---

## Layout Tests

### L-1: Short vs Long Page
```
Control:    Full 9-section page
Variant B:  Condensed 5-section page (Hero + Benefits + Proof + CTA + Footer)
Hypothesis: For simple, low-cost offers, shorter pages reduce
            decision fatigue and increase conversion.
Metric:     Conversion rate, scroll completion rate
Caveat:     Long pages often win for high-ticket/complex services.
```

### L-2: Form Position
```
Control:    Form in hero section (immediate ask)
Variant B:  Form after social proof section (earn trust first)
Hypothesis: Placing the form after proof gives visitors
            time to build confidence before committing.
Metric:     Form submission rate
```

### L-3: FAQ Accordion vs Expanded
```
Control:    FAQ in collapsed accordion (click to expand)
Variant B:  FAQ fully expanded (all answers visible)
Hypothesis: Visible answers reduce friction for visitors
            who won't click to expand.
Metric:     Scroll depth through FAQ, CTA clicks after FAQ
```

---

## Form Tests

### F-1: Field Count
```
Control:    3 fields (name, phone, email)
Variant B:  2 fields (name, phone only)
Hypothesis: Removing email field reduces perceived effort
            and increases submission rate.
Metric:     Form submission rate
Trade-off:  Fewer follow-up channels. Worth testing.
```

### F-2: Multi-Step vs Single Form
```
Control:    All fields visible at once
Variant B:  Step 1: "Bạn cần gì?" (select service)
            Step 2: Name + Phone
Hypothesis: Micro-commitment in step 1 increases completion
            through consistency principle.
Metric:     Form completion rate, drop-off between steps
```

---

## How to Choose Which Test to Run

```
IF CTA score < 60%
  → Test CTA first (C-1, C-2, or C-3)
  → Highest impact, easiest to implement

IF Trust score < 60%
  → Test social proof (S-1, S-2, or S-3)
  → Build credibility before optimizing other elements

IF Message Match score < 60%
  → Test headline (H-1, H-2, or H-3)
  → Alignment with ad is critical for Quality Score

IF Form friction score < 60%
  → Test form (F-1 or F-2)
  → Reduce barrier to conversion

IF all scores > 60%
  → Test layout variations (L-1, L-2)
  → Optimize the overall experience
```
