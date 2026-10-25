# Design System: Project-Ultra

> Curated Family: **Linear Obsidian & Indigo**  
> Category: **SAAS**  
> Vibes: `modern precision command-bar developer b2b`  
> Accessibility: **AAA Pass (Light)** / **AAA Pass (Dark)**

---

## 1. Dual Palette Specifications

| Role | Light Token | Light Hex | Dark Token | Dark Hex |
| :--- | :--- | :--- | :--- | :--- |
| **Canvas Background** | `--bg-canvas` | `#F8FAFC` | `--bg-canvas` | `#08090C` |
| **Surface (Cards/Panels)** | `--bg-surface` | `#FFFFFF` | `--bg-surface` | `#11131A` |
| **Elevated (Dropdowns/Badges)** | `--bg-elevated` | `#F1F5F9` | `--bg-elevated` | `#1A1D27` |
| **Primary Text** | `--text-primary` | `#0B0F19` | `--text-primary` | `#F3F4F6` |
| **Muted Text / Secondary** | `--text-muted` | `#475569` | `--text-muted` | `#8A94A6` |
| **Primary Accent** | `--accent-primary` | `#4F46E5` | `--accent-primary` | `#6366F1` |
| **Secondary Accent** | `--accent-secondary` | `#0D9488` | `--accent-secondary` | `#14B8A6` |
| **Subtle Border** | `--border-color` | `#E2E8F0` | `--border-color` | `#222634` |

### Data Visualization Series
- **Series 1 (`--chart-1`):** `#4F46E5` (Light) / `#6366F1` (Dark)
- **Series 2 (`--chart-2`):** `#0D9488` (Light) / `#14B8A6` (Dark)
- **Series 3 (`--chart-3`):** `#F59E0B` (Light) / `#FBBF24` (Dark)
- **Series 4 (`--chart-4`):** `#10B981` (Light) / `#34D399` (Dark)
- **Series 5 (`--chart-5`):** `#6366F1` (Light) / `#818CF8` (Dark)

---

## 2. Typography Recommendations
- **Display / Headers:** 'Space Grotesk', sans-serif
- **Body / Interface:** 'Plus Jakarta Sans', sans-serif
- **Code / Metrics / Monospace:** 'JetBrains Mono', monospace

---

## 3. WCAG 2.1 Contrast Telemetry
- **Light Theme Contrast (Text / Surface):** 19.15:1 (AAA Pass)
- **Dark Theme Contrast (Text / Surface):** 16.86:1 (AAA Pass)

---

## 4. Conversion Blueprint Architecture
- **Conversion Pattern:** Command Hero + Interactive Bento Matrix
- **Conversion Focus:** Product-led trial conversion & enterprise demo bookings
- **5-Step Section Architecture:**
   - 1. Hero: Telemetry Pill + Bold Value Prop + Primary Action & Live Demo CTA
   - 2. Bento Matrix: Core feature grid with live component micro-interactions
   - 3. Interactive Terminal / API Playground: Instant developer aha moment
   - 4. Social Proof & Enterprise Telemetry: Uptime metrics (99.99%) & customer logos
   - 5. Tiered Pricing Matrix + Sticky Bottom Conversion Bar

---

## 5. Metric-to-Chart Pattern Blueprints
- **Recommended Chart Architecture:** Area Sparkline (Throughput / Requests/sec) & Segmented Ring (Resource Utilization)
- **Chart Palette Pairing:**
  - `--chart-1`: Primary Metric (Volume / Revenue / Core Series)
  - `--chart-2`: Secondary Metric (Comparisons / Retention / Benchmarks)
  - `--chart-3`: Accent / Target Indicator
  - `--chart-4`: Anomaly / Threshold Alert
  - `--chart-5`: Baseline / Projection

---

## 6. Pre-Delivery Production Craft Checklist
- [ ] **Zero Emoji Icons:** Strictly use Lucide, Heroicons, or Phosphor SVGs. Never use Unicode emojis as UI icons.
- [ ] **Tactile Press Feedback:** Every interactive element has `active:scale-[0.98]` and `cursor-pointer`.
- [ ] **Resilient Typography:** Headings use `text-wrap: balance`; containers use overflow-safe wrapping (`break-words`).
- [ ] **Mobile-First Touch Ergonomics:** Minimum 44x44pt (iOS) / 48x48dp (Android/Web) touch target bounding boxes.
- [ ] **Dynamic Contrast Enforced:** Badges and cards use `--elevated-foreground` for zero washed-out text across themes.

---

## 7. Quickstart Integration

### In Shadcn UI
Copy `design-system/shadcn-globals.css` into your project's `app/globals.css`.

### In Tailwind CSS v3 / v4
- **v3:** Include `design-system/tailwind.tokens.js` in `tailwind.config.js`.
- **v4:** Import `design-system/tailwind-v4.css` in your main stylesheet.

### In HTML & Vanilla JS
```html
<link rel="stylesheet" href="design-system/theme-tokens.css">
<script src="design-system/theme-toggle.js"></script>
```
