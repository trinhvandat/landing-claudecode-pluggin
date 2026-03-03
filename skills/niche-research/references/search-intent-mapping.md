# Search Intent Mapping

Reference for classifying keywords by search intent. Used by niche-research Step 3.

## The 4 Intent Types

### TRANSACTIONAL — User wants to BUY or ACT now
Signal words (English): buy, order, book, schedule, purchase, sign up, subscribe, get quote, hire, download, register, appointment
Signal words (Vietnamese): mua, đặt, đặt lịch, đăng ký, thuê, tải, đặt hàng, liên hệ, gọi, báo giá

**Landing page strategy**: Short page, strong CTA, minimal friction. Lead form or buy button above fold. Price/offer prominent.

### COMMERCIAL — User is COMPARING before buying
Signal words (English): best, top, review, compare, vs, versus, alternative, pros and cons, worth it, recommendation, rated
Signal words (Vietnamese): tốt nhất, top, đánh giá, so sánh, nên chọn, review, uy tín, chất lượng, có nên, loại nào

**Landing page strategy**: Longer page with social proof, comparison tables, testimonials. Build trust before CTA. Address objections in FAQ.

### INFORMATIONAL — User wants to LEARN
Signal words (English): what is, how to, why, guide, tutorial, tips, meaning, definition, explained, can I, should I
Signal words (Vietnamese): là gì, cách, hướng dẫn, tại sao, bao lâu, có đau không, quy trình, kinh nghiệm, chia sẻ, tìm hiểu

**Landing page strategy**: Do NOT target with ads. Use for blog/content marketing instead. Exception: "how much" questions can work with pricing landing pages.

### NAVIGATIONAL — User wants a SPECIFIC brand/place
Signal words (English): brand name, specific clinic/store name, "near me", address, hours, phone, login, official
Signal words (Vietnamese): brand name, "gần đây", "ở đâu", địa chỉ, số điện thoại, chi nhánh

**Landing page strategy**: Only target if it's YOUR brand. Do not bid on competitor brand names without strategy. "Near me" works for local service ads.

## Decision Tree for Ambiguous Keywords

```
START: "{product} {location}"
  └── Does it contain a price/action word?
        ├── YES → TRANSACTIONAL
        └── NO
              └── Does it contain a comparison/quality word?
                    ├── YES → COMMERCIAL
                    └── NO
                          └── Does it contain a question/learning word?
                                ├── YES → INFORMATIONAL
                                └── NO
                                      └── Does it contain a brand/place name?
                                            ├── YES → NAVIGATIONAL
                                            └── NO → Default to COMMERCIAL
```

### Why default to COMMERCIAL?
Commercial intent users are in the consideration phase — they're close to buying but need persuasion. A well-built landing page converts them. Safer than assuming transactional (which expects immediate action) or informational (which wastes ad spend).

## Intent → Landing Page Priority

| Intent | Ad-Worthy? | LP Priority | Page Type |
|--------|-----------|-------------|-----------|
| TRANSACTIONAL | YES — highest ROI | P0 | Short, CTA-focused |
| COMMERCIAL | YES — high volume | P0 | Longer, trust-building |
| INFORMATIONAL | NO — use blog/SEO | P2 | Blog post, not LP |
| NAVIGATIONAL | ONLY own brand | P1 | Brand landing page |

## Multi-Intent Keywords

Some keywords carry mixed intent:
- "implant giá bao nhiêu" = TRANSACTIONAL (price) + INFORMATIONAL (how much)
  → Classify as TRANSACTIONAL — the price intent is dominant
- "implant tốt nhất ở đâu" = COMMERCIAL (best) + NAVIGATIONAL (where)
  → Classify as COMMERCIAL — the comparison intent is dominant

Rule: when mixed, pick the intent closest to purchase action.
