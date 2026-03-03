# Audit Checklist — Detailed Scoring Criteria

Reference for Step 3 of the conversion-optimizer skill. Use this for consistent, evidence-based scoring.

## Scoring Principles

1. **Evidence-based**: Score only what you can observe in the HTML/content. Don't guess about server-side performance.
2. **Consistent**: Apply the same standard to every page. A 7 means the same thing across audits.
3. **Actionable**: Every score below 8 should have a clear path to improvement.
4. **Whole numbers only**: No 7.5. Round to nearest integer.

---

## Category 1: MESSAGE MATCH (20% weight)

### 1A. Headline matches ad copy (0-40 points)

WITH research context (ad-copy-suggestions.md available):
```
40 pts — h1 matches ad headline 1 word-for-word
30 pts — h1 contains all keywords from ad headline, slightly reworded
20 pts — h1 contains primary keyword but different phrasing
10 pts — h1 is on-topic but doesn't contain target keywords
 0 pts — h1 is generic, off-topic, or missing
```

STANDALONE mode (no ad-copy context):
```
40 pts — h1 is clear, specific, benefit-focused, contains industry keyword
30 pts — h1 is clear but generic (could apply to any competitor)
20 pts — h1 is vague or clever (not immediately clear what the page offers)
10 pts — h1 is present but unhelpful
 0 pts — h1 is missing or completely irrelevant
```

### 1B. Keywords in first 100 words (0-30 points)

```
30 pts — 3+ target keywords appear naturally in first 100 words
20 pts — 1-2 target keywords in first 100 words
10 pts — Keywords appear but after first 100 words
 0 pts — No relevant keywords found on page
```

How to check: Extract first 100 words of visible body text. Count occurrences of keywords from niche-brief or extracted from the page's meta keywords/description.

### 1C. Value prop clear within 5 seconds (0-30 points)

```
30 pts — Above fold shows: what it is + who it's for + why choose this
20 pts — Above fold shows what it is, but WHO or WHY is missing
10 pts — Above fold is mostly visual, value prop requires scrolling
 0 pts — Above fold is confusing or doesn't communicate the offer
```

"Above fold" = content visible at 375px mobile viewport without scrolling (~600px content height).

---

## Category 2: CTA EFFECTIVENESS (20% weight)

### 2A. CTA visible above fold (0-25 points)

```
25 pts — CTA button visible in first 600px of content (mobile viewport)
15 pts — CTA appears but requires minor scroll (600-900px)
 5 pts — CTA only appears below fold
 0 pts — No CTA button on the page
```

### 2B. CTA copy is action + benefit (0-25 points)

```
25 pts — Action verb + specific benefit: "Đặt Lịch Tư Vấn Miễn Phí"
20 pts — Action verb + generic benefit: "Đăng Ký Ngay"
10 pts — Weak action: "Tìm Hiểu Thêm", "Learn More"
 5 pts — No action verb: "Chi Tiết", "Thông Tin"
 0 pts — Generic: "Submit", "Gửi", "Click Here"
```

### 2C. CTA color contrasts with background (0-25 points)

```
25 pts — CTA color is visually distinct, high contrast (≥ 4.5:1), stands out clearly
15 pts — CTA is distinct but low contrast or similar to other elements
 5 pts — CTA blends into the page design
 0 pts — CTA is not visually identifiable as a button
```

### 2D. CTA repeated after social proof (0-25 points)

```
25 pts — CTA appears 3+ times: hero + after proof + page end
20 pts — CTA appears 2 times in logical positions
10 pts — CTA appears only once
 0 pts — No CTA or CTA only in unexpected position
```

---

## Category 3: TRUST & SOCIAL PROOF (15% weight)

### 3A. Testimonials (0-30 points)

```
30 pts — 3+ testimonials with: real photo + full name + title/role + specific result
25 pts — 2-3 testimonials with names and some details
15 pts — Testimonials present but anonymous or vague ("Khách hàng A nói...")
 5 pts — Only star ratings, no actual quotes
 0 pts — No testimonials or reviews
```

### 3B. Trust badges/certifications (0-25 points)

```
25 pts — 3+ relevant badges: industry certifications, awards, review platform scores
15 pts — 1-2 relevant badges or certifications
 5 pts — Only generic badges (SSL, payment icons) not relevant to offer
 0 pts — No trust badges
```

### 3C. Specific numbers/stats (0-25 points)

```
25 pts — 3+ specific metrics: "2,847 khách hàng", "15 năm kinh nghiệm", "4.9/5 Google"
15 pts — 1-2 specific numbers
 5 pts — Only round/vague numbers: "hàng nghìn", "nhiều năm"
 0 pts — No numerical social proof
```

### 3D. Real names/photos (0-20 points)

```
20 pts — Real photos of staff, facility, or customers (identifiably authentic)
10 pts — Mix of real and stock photography
 5 pts — All stock photography but high quality
 0 pts — No images, or obviously fake stock photos
```

---

## Category 4: PAGE SPEED SIGNALS (15% weight)

### 4A. Image optimization (0-30 points)

```
30 pts — All non-hero images lazy-loaded, alt text on all, width/height set
20 pts — Most images lazy-loaded, most have alt text
10 pts — Some optimization but inconsistent
 0 pts — No lazy loading, missing alt text, no dimensions set
```

### 4B. Script count (0-25 points)

```
25 pts — ≤ 3 script tags (minimal JS)
20 pts — 4-5 script tags
10 pts — 6-10 script tags
 0 pts — > 10 script tags (heavy, likely slow)
```

### 4C. CSS approach (0-25 points)

```
25 pts — Critical CSS inline in <head>, minimal external sheets
15 pts — External CSS but few files (1-2)
 5 pts — Multiple external CSS files or large inline blocks
 0 pts — Render-blocking CSS with no optimization
```

### 4D. Font loading (0-20 points)

```
20 pts — Fonts preloaded, display:swap, max 2 families
15 pts — Fonts loaded via Google Fonts with display=swap
 5 pts — Fonts loaded but no preload or swap
 0 pts — Multiple font families with no optimization, FOUT likely
```

---

## Category 5: MOBILE EXPERIENCE (15% weight)

### 5A. Viewport meta (0-20 points)

```
20 pts — Correct viewport meta: width=device-width, initial-scale=1
10 pts — Viewport meta present but non-standard
 0 pts — No viewport meta tag (page won't render correctly on mobile)
```

### 5B. Touch targets (0-25 points)

```
25 pts — All buttons/links appear ≥ 48px in touch area
15 pts — Primary CTA is large but secondary elements are small
 5 pts — Some interactive elements appear too small
 0 pts — Buttons are clearly too small for touch (< 32px)
```

### 5C. Font size (0-25 points)

```
25 pts — Body text ≥ 16px, headings properly scaled
15 pts — Most text ≥ 16px, some smaller elements
 5 pts — Body text 14px (borderline readable)
 0 pts — Body text < 14px (requires zooming)
```

### 5D. Single column on mobile (0-30 points)

```
30 pts — Clean single column layout, no horizontal scrolling
20 pts — Mostly single column, minor multi-column in non-critical areas
10 pts — Some horizontal scrolling or cramped multi-column layouts
 0 pts — Page clearly not responsive, horizontal scrolling throughout
```

---

## Category 6: CONTENT QUALITY (10% weight)

### 6A. Readability (0-30 points)

```
30 pts — Short paragraphs (2-3 sentences), bullet points, clear headings, scannable
20 pts — Mostly scannable, some long paragraphs
10 pts — Wall-of-text in places, few visual breaks
 0 pts — Dense, unscannable text throughout
```

### 6B. Benefit-focused (0-30 points)

```
30 pts — Content consistently frames features as benefits to the user
20 pts — Mix of benefits and features
10 pts — Mostly feature-focused ("we have X technology")
 0 pts — All features, no benefits, company-centric language
```

### 6C. Addresses objections (0-20 points)

```
20 pts — FAQ with 4+ questions directly addressing likely objections
15 pts — FAQ present with 2-3 questions
 5 pts — Some objection handling scattered in content but no FAQ section
 0 pts — No FAQ, no objection handling
```

### 6D. Emotional triggers (0-20 points)

```
20 pts — Clear emotional appeals: pain, aspiration, urgency, belonging
10 pts — Some emotional elements but mostly rational
 5 pts — Slightly emotional tone
 0 pts — Purely factual, no emotional engagement
```

---

## Category 7: TECHNICAL SEO (5% weight)

### 7A. Schema markup (0-30 points)

```
30 pts — FAQPage + at least one more schema (LocalBusiness, Product, Organization)
20 pts — FAQPage schema present
10 pts — Some schema but not FAQPage
 0 pts — No schema markup
```

### 7B. Meta title + description (0-25 points)

```
25 pts — Both present, correct length (title <60, desc <160), contain keywords
15 pts — Both present but suboptimal length or missing keywords
 5 pts — Only title present, no description
 0 pts — Neither present
```

### 7C. OG/Twitter Card tags (0-25 points)

```
25 pts — Full set: og:title, og:description, og:image, og:url, twitter:card
15 pts — Partial (title + description but no image)
 5 pts — Only 1-2 tags present
 0 pts — No social sharing tags
```

### 7D. Canonical URL (0-20 points)

```
20 pts — <link rel="canonical"> present with correct URL
10 pts — Canonical present but potentially incorrect URL
 0 pts — No canonical tag
```
