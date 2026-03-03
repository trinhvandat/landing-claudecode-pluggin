# Design System: Smile Dental — Implant Landing Page

> ⚠️ Generated from fallback rules (UUPM not available).
> Install UUPM for more precise, data-driven design decisions.

**Generated**: 2026-03-03
**Industry**: Healthcare / Dental Clinic
**Mood**: Trust, Professional, Clean, Reassuring
**Competitor Gap**: Warm + accessible (competitors are cold/corporate)

---

## Color Palette

| Role | Hex | Usage |
|------|-----|-------|
| **Primary** | `#0E7490` | Headers, section backgrounds, trust elements (teal — medical trust) |
| **CTA** | `#F97316` | All CTA buttons, urgency elements (orange — high contrast, warm action) |
| **CTA Hover** | `#EA580C` | Button hover state |
| **Background** | `#FFFFFF` | Page background |
| **Surface** | `#F0FDFA` | Card backgrounds, alternating sections (light teal tint) |
| **Text Primary** | `#1E293B` | Body text, headings |
| **Text Secondary** | `#64748B` | Captions, labels, secondary info |
| **Success** | `#16A34A` | Trust badges, checkmarks, positive indicators |
| **Border** | `#E2E8F0` | Card borders, dividers |

### Contrast Ratios
- CTA (#F97316) on White (#FFFFFF): **3.2:1** → add dark text on CTA button: `#FFFFFF` white text on orange passes at large text sizes. For body-sized CTA text, use `#7C2D12` dark brown or keep white with bold weight ≥ 18.66px.
- Text (#1E293B) on White (#FFFFFF): **12.6:1** ✅
- Text (#1E293B) on Surface (#F0FDFA): **11.8:1** ✅

### Design Rationale
- **Teal primary**: Medical trust without the cold corporate blue competitors use. Warmer, more approachable.
- **Orange CTA**: Maximum contrast against teal. Dr. Care uses this combination successfully. Warm color = action energy.
- **Light teal surface**: Subtle brand reinforcement without visual noise.

---

## Typography

### Font Pairing
| Role | Font | Weight | Size (Desktop) | Size (Mobile) |
|------|------|--------|----------------|---------------|
| **Heading** | Inter | 700 (Bold) | 36-48px | 24-32px |
| **Sub-heading** | Inter | 600 (Semibold) | 24-28px | 20-24px |
| **Body** | Inter | 400 (Regular) | 18px | 16px |
| **Caption** | Inter | 400 (Regular) | 14px | 14px |
| **CTA Button** | Inter | 700 (Bold) | 18px | 16px |

### Google Fonts URL
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
```

### Tailwind Config
```js
fontFamily: {
  sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
}
```

### Type Scale
- Line height: 1.6 for body, 1.2 for headings
- Letter spacing: -0.02em for headings, normal for body
- Max line width: 65ch for body text (readability)
- Vietnamese diacritics: Inter supports full Vietnamese character set ✅

---

## Spacing System

| Token | Value | Usage |
|-------|-------|-------|
| `space-xs` | 4px | Inline element gaps |
| `space-sm` | 8px | Icon-to-text gaps, badge padding |
| `space-md` | 16px | Card padding, form field gaps |
| `space-lg` | 24px | Between elements within a section |
| `space-xl` | 40px | Section padding (mobile) |
| `space-2xl` | 64px | Section padding (desktop) |
| `space-3xl` | 80px | Major section breaks (desktop) |

### Container
```
Max width: 1200px
Mobile padding: 16px horizontal
Tablet padding: 24px horizontal
Desktop: centered with auto margins
```

---

## Components

### CTA Button
```
Background: #F97316 (orange)
Text: #FFFFFF (white, bold 700)
Border radius: 8px
Padding: 16px 32px
Min height: 52px (exceeds 48px touch target ✅)
Min width: 200px
Font size: 18px desktop, 16px mobile
Full width on mobile
Shadow: 0 4px 6px rgba(249,115,22,0.25)
Hover: #EA580C, translateY(-1px), shadow increase
Active: #C2410C, translateY(0)
Focus: 3px ring #F97316/50%
Transition: all 150ms ease
```

### Trust Badge
```
Background: #F0FDFA (light teal)
Border: 1px solid #0E7490/20%
Border radius: 8px
Padding: 8px 16px
Icon: 20px, color #16A34A (green check)
Text: 14px, #1E293B
```

### Testimonial Card
```
Background: #FFFFFF
Border: 1px solid #E2E8F0
Border radius: 12px
Padding: 24px
Shadow: 0 1px 3px rgba(0,0,0,0.1)
Avatar: 48px circle
Name: 16px bold
Title/location: 14px #64748B
Quote: 16px italic #1E293B
```

### FAQ Accordion
```
Border: 1px solid #E2E8F0
Border radius: 8px
Question padding: 16px 20px
Question font: 16px bold
Answer padding: 0 20px 16px
Answer font: 16px regular, #64748B
Icon: chevron, 20px, rotate 180° on open
Transition: max-height 200ms ease
```

### Stats Bar
```
Background: #0E7490 (primary teal)
Text: #FFFFFF
Padding: 24px
Grid: 3-4 columns desktop, 2 columns mobile
Number: 36px bold
Label: 14px regular
```

---

## Section Order

```
1. HERO           — Headline + sub + CTA + trust badges (NO nav)
2. STATS BAR      — 3-4 key metrics (social proof numbers)
3. PAIN POINTS    — 3 patient fears with icons (PAS: Problem)
4. SOLUTION       — 3-4 benefits as cards (PAS: Solution)
5. SOCIAL PROOF   — Testimonials + client photos
6. HOW IT WORKS   — 3 numbered steps
7. FAQ            — 5 questions from persona objections
8. FINAL CTA      — Repeat CTA + guarantee
9. FOOTER         — Contact + legal (minimal)
```

---

## Responsive Breakpoints

| Breakpoint | Width | Layout |
|-----------|-------|--------|
| **Mobile (primary)** | 375px | Single column, full-width CTA, stacked cards |
| **Tablet** | 768px | 2-column grids, side-by-side testimonials |
| **Desktop** | 1024px | 3-column benefits, wider hero |
| **Large** | 1200px | Max-width container, generous whitespace |

### Mobile-First Rules
- Code 375px layout FIRST
- Add `min-width` breakpoints upward
- Touch targets: minimum 48px
- Font: minimum 16px body
- No horizontal scroll
- CTA: full width on mobile

---

## Image Guidelines

| Image | Format | Size | Loading |
|-------|--------|------|---------|
| Hero | WebP/JPG | 1200×600 max | `eager` |
| Doctor photos | WebP/JPG | 200×200 | `lazy` |
| Testimonial avatars | WebP/JPG | 96×96 | `lazy` |
| Trust badges/icons | SVG | n/a | inline |
| Before/after | WebP/JPG | 600×400 | `lazy` |

- All images: `width` + `height` attributes set (prevent CLS)
- All images: descriptive `alt` text in Vietnamese
- Hero image: real dental clinic or smiling patient (NOT stock)

---

## Google Ads Landing Page — Design Overrides

### CTA Button
- Color: #F97316 MUST contrast with #FFFFFF background ✅
- Size: 52px height (≥ 48px touch target) ✅
- Position: above fold on mobile (375px) — in hero section
- Copy: "Đặt Lịch Tư Vấn Miễn Phí" (action + benefit) ✅
- Repetition: hero + after social proof + final CTA = 3 times ✅

### Trust Section
- Position: stats bar immediately after hero, testimonials after benefits
- Includes: patient stats + doctor credentials + before/after photos

### Form (lead gen)
- 2 fields: Họ tên + Số điện thoại (maximum for cold traffic)
- Single column on mobile ✅
- Submit button: full width, matches CTA color

### Hero Section
- h1: EXACT match to ad headline ("Implant Không Đau Từ 15 Triệu")
- Sub-headline: 1 line expanding value prop
- NO navigation bar ✅
- NO hamburger menu ✅
- Background: white, clean, text-readable

### Typography
- Headline: 32px+ desktop, 24px+ mobile ✅
- Body: 18px desktop, 16px mobile ✅
- Line height: 1.6 body ✅
- Max 1 font family (Inter) ✅
