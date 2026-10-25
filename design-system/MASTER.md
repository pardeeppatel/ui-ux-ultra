# Design System: Project-Ultra

> Curated Family: **Grand Trunk Terracotta & Peacock**  
> Category: **TRAVEL**  
> Vibes: `india-travel transit train bus vlog heritage`  
> Accessibility: **AAA Pass (Light)** / **AAA Pass (Dark)**

---

## 1. Dual Palette Specifications

| Role | Light Token | Light Hex | Dark Token | Dark Hex |
| :--- | :--- | :--- | :--- | :--- |
| **Canvas Background** | `--bg-canvas` | `#FDFBF7` | `--bg-canvas` | `#0E0A08` |
| **Surface (Cards/Panels)** | `--bg-surface` | `#F4EFE6` | `--bg-surface` | `#18120E` |
| **Elevated (Dropdowns/Badges)** | `--bg-elevated` | `#FFFFFF` | `--bg-elevated` | `#241B15` |
| **Primary Text** | `--text-primary` | `#241914` | `--text-primary` | `#FAF5EE` |
| **Muted Text / Secondary** | `--text-muted` | `#6E5A4F` | `--text-muted` | `#A68E80` |
| **Primary Accent** | `--accent-primary` | `#C85A32` | `--accent-primary` | `#E07A5F` |
| **Secondary Accent** | `--accent-secondary` | `#0F766E` | `--accent-secondary` | `#14B8A6` |
| **Subtle Border** | `--border-color` | `#E6DEC8` | `--border-color` | `#362820` |

### Data Visualization Series
- **Series 1:** `#C85A32` (Light) / `#E07A5F` (Dark)
- **Series 2:** `#0F766E` (Light) / `#14B8A6` (Dark)
- **Series 3:** `#F59E0B` (Light) / `#FBBF24` (Dark)
- **Series 4:** `#10B981` (Light) / `#34D399` (Dark)
- **Series 5:** `#6366F1` (Light) / `#818CF8` (Dark)

---

## 2. Typography Recommendations
- **Display / Headers:** 'Fraunces', serif
- **Body / Interface:** 'Plus Jakarta Sans', sans-serif
- **Code / Metrics / Monospace:** 'JetBrains Mono', monospace

---

## 3. WCAG 2.1 Contrast Telemetry
- **Light Theme Contrast (Text / Surface):** 14.98:1 (AAA Pass)
- **Dark Theme Contrast (Text / Surface):** 17.11:1 (AAA Pass)

---

## 4. Quickstart Integration

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
