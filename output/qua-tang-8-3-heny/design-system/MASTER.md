# Design System: Quà Tặng 8/3 Heny Garden

**Generated**: 2026-03-05
**Project**: qua-tang-8-3-heny
**Design Mode**: Fallback (UUPM not available)

---

## Design Intent

**Mood**: Lãng mạn, ấm áp, nữ tính, urgency (8/3 sắp đến)
**Industry**: Gift/E-commerce, Seasonal Campaign
**Target Emotion**: Anticipation, Romance, Confidence in choice

---

## Color Palette

### Primary Colors

| Name | Hex | Usage |
|------|-----|-------|
| **Rose Pink** | `#E11D48` | CTA buttons, urgency elements, countdown |
| **Soft Blush** | `#FDF2F8` | Background sections (hero, testimonials) |
| **Warm Gold** | `#D97706` | Accents, badges, "Khắc tên miễn phí" highlight |

### Secondary Colors

| Name | Hex | Usage |
|------|-----|-------|
| **Deep Rose** | `#9F1239` | CTA hover state, headings |
| **Cream White** | `#FFFBEB` | Card backgrounds, form section |
| **Charcoal** | `#1F2937` | Body text |
| **Soft Gray** | `#6B7280` | Secondary text, captions |

### Semantic Colors

| Name | Hex | Usage |
|------|-----|-------|
| **Success Green** | `#059669` | Trust badges, "Còn hàng" |
| **Urgency Red** | `#DC2626` | Countdown timer, "Còn X ngày" |
| **Info Blue** | `#2563EB` | Links, Zalo button |

### Color Application

```css
:root {
  --color-primary: #E11D48;
  --color-primary-hover: #9F1239;
  --color-secondary: #D97706;
  --color-bg-soft: #FDF2F8;
  --color-bg-cream: #FFFBEB;
  --color-text: #1F2937;
  --color-text-secondary: #6B7280;
  --color-cta: #E11D48;
  --color-cta-hover: #BE123C;
  --color-urgency: #DC2626;
}
```

---

## Typography

### Font Families

| Type | Font | Fallback | Google Fonts URL |
|------|------|----------|------------------|
| **Heading** | Be Vietnam Pro | sans-serif | `family=Be+Vietnam+Pro:wght@500;600;700` |
| **Body** | Be Vietnam Pro | sans-serif | (same) |

**Why Be Vietnam Pro**: Vietnamese diacritics optimized, modern, readable, romantic feel

### Font Sizes (Mobile First)

| Element | Mobile | Desktop | Weight |
|---------|--------|---------|--------|
| h1 (Hero) | 28px | 40px | 700 |
| h2 (Section) | 24px | 32px | 600 |
| h3 (Card title) | 18px | 20px | 600 |
| Body | 16px | 16px | 400 |
| Caption | 14px | 14px | 400 |
| CTA Button | 16px | 18px | 600 |
| Badge | 12px | 14px | 500 |

### Line Heights

```css
h1, h2 { line-height: 1.3; }
h3 { line-height: 1.4; }
p, body { line-height: 1.6; }
```

---

## Spacing System

### Base Unit: 4px

| Token | Value | Usage |
|-------|-------|-------|
| `space-1` | 4px | Icon gaps |
| `space-2` | 8px | Inline spacing |
| `space-3` | 12px | Card padding small |
| `space-4` | 16px | Card padding, gaps |
| `space-6` | 24px | Section gaps |
| `space-8` | 32px | Section padding mobile |
| `space-12` | 48px | Section padding desktop |
| `space-16` | 64px | Hero padding |

### Tailwind Classes

```
padding: p-4 (16px), p-6 (24px), p-8 (32px), p-12 (48px), p-16 (64px)
margin: my-8 (32px vertical), my-12 (48px)
gap: gap-4 (16px), gap-6 (24px)
```

---

## Components

### CTA Button (Primary)

```css
.btn-cta {
  background: var(--color-cta);
  color: white;
  padding: 16px 32px;
  border-radius: 8px;
  font-size: 18px;
  font-weight: 600;
  box-shadow: 0 4px 14px rgba(225, 29, 72, 0.3);
  transition: all 0.2s ease;
  min-height: 52px; /* Touch target */
}
.btn-cta:hover {
  background: var(--color-cta-hover);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(225, 29, 72, 0.4);
}
```

**Tailwind**:
```html
<a class="bg-rose-600 hover:bg-rose-700 text-white px-8 py-4 rounded-lg
          font-semibold text-lg shadow-lg hover:shadow-xl
          transition-all hover:-translate-y-0.5">
  Đặt Quà 8/3 Ngay
</a>
```

### CTA Button (Secondary)

```html
<a class="border-2 border-rose-600 text-rose-600 hover:bg-rose-50
          px-6 py-3 rounded-lg font-semibold transition-all">
  Xem Chi Tiết
</a>
```

### Trust Badge

```html
<div class="flex items-center gap-2 bg-amber-50 text-amber-800
            px-3 py-2 rounded-full text-sm font-medium">
  <svg><!-- icon --></svg>
  <span>Khắc Tên Miễn Phí</span>
</div>
```

### Stats Bar

```html
<div class="grid grid-cols-2 md:grid-cols-4 gap-4 bg-rose-50 p-6 rounded-xl">
  <div class="text-center">
    <span class="block text-2xl font-bold text-rose-600">5,394+</span>
    <span class="text-gray-600 text-sm">Sets Đã Bán</span>
  </div>
  <!-- repeat -->
</div>
```

### Product Card (Set Comparison)

```html
<div class="bg-white rounded-xl shadow-md overflow-hidden border border-rose-100
            hover:shadow-lg hover:border-rose-300 transition-all">
  <div class="p-4">
    <h3 class="font-semibold text-lg text-gray-900">LOVE_01</h3>
    <p class="text-rose-600 font-bold text-xl">409.000đ</p>
    <ul class="mt-2 text-sm text-gray-600 space-y-1">
      <li>✓ Nến Chill n Relax 150gr</li>
      <li>✓ Đế gỗ vintage</li>
      <li>✓ Hộp hoa hồng sáp</li>
    </ul>
    <a href="#form" class="mt-4 block text-center bg-rose-600 text-white
                           py-2 rounded-lg font-medium hover:bg-rose-700">
      Chọn Set Này
    </a>
  </div>
</div>
```

### Countdown Timer

```html
<div class="bg-red-600 text-white py-3 px-4 rounded-lg text-center">
  <p class="text-sm mb-1">Còn lại để kịp giao 8/3:</p>
  <div class="flex justify-center gap-4 font-bold text-2xl">
    <div><span id="days">03</span><small class="block text-xs font-normal">Ngày</small></div>
    <div><span id="hours">14</span><small class="block text-xs font-normal">Giờ</small></div>
    <div><span id="minutes">22</span><small class="block text-xs font-normal">Phút</small></div>
    <div><span id="seconds">45</span><small class="block text-xs font-normal">Giây</small></div>
  </div>
</div>
```

### Testimonial Card

```html
<div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
  <div class="flex items-center gap-3 mb-3">
    <img src="avatar.jpg" class="w-12 h-12 rounded-full object-cover" alt="">
    <div>
      <p class="font-semibold text-gray-900">Chị Hương</p>
      <p class="text-sm text-gray-500">Quận 7, TPHCM</p>
    </div>
    <div class="ml-auto text-amber-400">★★★★★</div>
  </div>
  <p class="text-gray-700 italic">"Bạn gái rất thích, mở hộp ra thơm ngát luôn..."</p>
</div>
```

---

## Section Order

1. **Hero** — Headline + CTA + Trust badges + Countdown
2. **Stats Bar** — 5,394+ sets | 9 reviews | 10+ mùi hương | Giao 2h
3. **Product Comparison** — 6 sets table/cards
4. **USP/Benefits** — Khắc tên, hoa vĩnh cửu, gói quà sẵn
5. **How It Works** — 3 steps (Chọn set → Khắc tên → Nhận quà)
6. **Testimonials** — 3-4 reviews thật
7. **FAQ** — 5-6 câu hỏi từ objections
8. **Final CTA + Form** — Countdown repeat + Form liên hệ
9. **Footer** — Địa chỉ, SĐT, Zalo, legal

---

## Google Ads LP Overrides

### CTA Button
- Color: Rose #E11D48 on white — contrast ratio 4.8:1 ✅
- Size: min 52px height, full-width on mobile
- Position: Above fold, repeat after testimonials, form section

### Trust Section
- Position: Immediately below hero (stats bar)
- Must include: 5,394+ sold, 9 reviews 5★, Giao hỏa tốc badge

### Form
- Max 2 fields: Tên + Số điện thoại
- Optional: Chọn set (dropdown)
- Single column on mobile
- CTA: "Đặt Quà 8/3 Ngay"

### Hero Section
- NO navigation bar
- Countdown timer prominent
- Badge: "Còn X ngày đến 8/3"
- Trust badges inline (3-4 small badges)

---

## Imagery Guidelines

### Hero Image
- Product shot: Set quà mở hộp, thấy nến + hoa
- Tone: Warm lighting, romantic feel
- Aspect ratio: 4:3 or 16:9
- Background: Soft, không rối

### Product Images
- Clean white/cream background
- Show tất cả items trong set
- Consistent lighting
- Show khắc tên detail

### Testimonial Avatars
- Real faces (không stock)
- Circular crop
- 64x64px minimum

---

## Responsive Breakpoints

```css
/* Mobile first */
@media (min-width: 640px) { /* sm */ }
@media (min-width: 768px) { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl - max container */ }
```

### Layout Changes

| Element | Mobile | Tablet | Desktop |
|---------|--------|--------|---------|
| Hero | Stack vertical | Stack | 2 columns |
| Product grid | 1 col | 2 cols | 3 cols |
| Stats bar | 2x2 grid | 4 cols | 4 cols |
| Testimonials | 1 col stack | 2 cols | 3 cols |

---

## Urgency Elements (Campaign Specific)

### Countdown to 8/3
- Show days/hours/minutes/seconds
- Background: Red #DC2626
- Position: Below hero, sticky on mobile (optional)
- End date: 2026-03-08 23:59:59

### Limited Stock Badge
```html
<span class="bg-red-100 text-red-700 px-2 py-1 rounded text-sm font-medium">
  🔥 Còn ít hàng
</span>
```

### Discount Codes Banner
```html
<div class="bg-amber-100 text-amber-800 p-3 text-center text-sm">
  🎁 Mã <strong>HENY25K</strong> giảm 25k đơn từ 599k |
  <strong>HENY40K</strong> giảm 40k đơn từ 799k
</div>
```

---

## Anti-Patterns (DO NOT)

- ❌ Navigation menu — distraction
- ❌ Multiple CTA styles — confusion
- ❌ Cold colors (blue, gray hero) — kills romantic mood
- ❌ Stock photos for testimonials — destroys trust
- ❌ Long forms (>3 fields) — friction
- ❌ Tiny text (<14px) — unreadable mobile
- ❌ Fake countdown (resets on refresh) — scam feel

---

## Next Steps
- [x] Design system complete
- [ ] Build landing page HTML+Tailwind
- [ ] Include countdown timer (end: 2026-03-08)
- [ ] Product comparison table (6 sets)
- [ ] Conversion optimizer audit
