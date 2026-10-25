---
name: ui-ux-ultra
description: >-
  Advanced 200-palette design intelligence, UX laws, and multi-platform theme compiler by Pardeep Kumar (ToolNPlay.com).
  Use this skill whenever the user asks to create, build, style, design, or re-theme any website, landing page, SaaS application, dashboard, or mobile app (Flutter, SwiftUI, React Native, Next.js), or mentions "ui ux ultra", "ui-ux-ultra", "ui ux", "design system", "color palette", "theme", or "Tailwind".
---

# UI/UX Ultra v1.0.0 — Design Intelligence & Multi-Platform Theme Compiler

> **Created by Pardeep Kumar** | **Powered by [ToolNPlay.com](https://ToolNPlay.com)**  
> **GitHub**: [https://github.com/PardeepPatel/ui-ux-ultra](https://github.com/PardeepPatel/ui-ux-ultra)

A comprehensive design intelligence engine featuring **200 curated, dual-theme palettes** across 20 distinct industry domains. Every palette is engineered with mathematically balanced surface contrast, dedicated Light & Dark polarities, typography pairings, UX Laws enforcement, and native code generation for **Web (Tailwind/Shadcn)**, **Flutter**, and **SwiftUI**.

---

## 1. The Core USP: Mandatory Two-Phase Workflow (HARD STOP RULE)

UI/UX Ultra's main USP is that **it gives the user full visual control over their brand identity before any application code is written**.

To protect this USP, AI agents **MUST ALWAYS follow this strict TWO-PHASE protocol**:

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant AI as AI Agent
    participant Engine as UI/UX Ultra Engine
    
    Note over User,AI: PHASE 1: Theme Selection & Visual Preview (MANDATORY STOP)
    User->>AI: "Build a SaaS app using ui-ux-ultra"
    AI->>Engine: Run design_engine.py --html ./theme_preview.html
    Engine-->>AI: Recommended palette + All alternatives + preview HTML
    AI->>User: Renders live interactive embed + lists ALL alternatives + asks for choice
    Note over AI: 🛑 HARD STOP: AI ends turn immediately! Does NOT build yet!
    
    Note over User,AI: PHASE 2: Project Implementation (Only After User Approves)
    User->>AI: "Looks great, let's go with Dual Mode" (or "Switch to Stripe Violet")
    AI->>Engine: Compile chosen theme tokens (--persist)
    AI->>User: Scaffolds & builds application using confirmed tokens
```

---

### 🛑 PHASE 1: Preview & Theme Selection Protocol (CURRENT TURN)

When the user asks to build, create, or design any website, dashboard, or app:

#### Step 1: Detect Domain & Run Synthesis Engine
Extract the domain category (e.g. `saas`, `travel`, `healthcare`, `fintech-crypto`, etc.) and run the design engine to generate the interactive preview HTML:

```bash
# Locate design_engine.py in ~/.gemini/config/skills/ui-ux-ultra/scripts/ (or workspace)
python3 ~/.gemini/config/skills/ui-ux-ultra/scripts/design_engine.py "<keywords>" --category <category> --html ./theme_preview.html
```

#### Step 2: Present the Interactive Embed & Blueprint Box in Chat
In your chat response, you **MUST**:
1. **Render the Live Interactive Embed**:
   ```html
   <agent-embed src="file:///absolute/path/to/theme_preview.html"></agent-embed>
   ```
2. **Output the Design System & Conversion Blueprint Box**:
   Directly beneath the embed, render the structured specification box containing the target domain, conversion pattern, 5-step section architecture, dual-theme tokens, typography pairing, chart patterns, and craft checklist:
   ```text
   ┌────────────────────────────────────────────────────────────────────────────────────────┐
   │ 🎨 UI/UX ULTRA — DESIGN SYSTEM & CONVERSION BLUEPRINT                                 │
   ├────────────────────────────────────────────────────────────────────────────────────────┤
   │ TARGET: Linear Obsidian & Indigo (SAAS)
   │ CONVERSION PATTERN: Command Hero + Interactive Bento Matrix
   │ CONVERSION FOCUS: Product-led trial conversion & enterprise demo bookings
   │
   │ 📐 5-STEP SECTION ARCHITECTURE:
   │     1. Hero: Telemetry Pill + Bold Value Prop + Primary Action & Live Demo CTA
   │     2. Bento Matrix: Core feature grid with live component micro-interactions
   │     3. Interactive Terminal / API Playground: Instant developer aha moment
   │     4. Social Proof & Enterprise Telemetry: Uptime metrics (99.99%) & customer logos
   │     5. Tiered Pricing Matrix + Sticky Bottom Conversion Bar
   │
   │ 🎨 DUAL-THEME COLOR TOKENS:
   │   • Light Mode: Canvas #F8FAFC | Surface #FFFFFF | Accent #4F46E5 | Text #0B0F19
   │   • Dark Mode:  Canvas #08090C | Surface #11131A | Accent #6366F1 | Text #F3F4F6
   │   • Contrast Telemetry: WCAG AAA (19.15:1 Light / 16.86:1 Dark)
   │
   │ 🔤 TYPOGRAPHY PAIRING:
   │   • Display / Headers: 'Space Grotesk', sans-serif
   │   • Interface / Body:  'Plus Jakarta Sans', sans-serif
   │   • Code / Monospace:  'JetBrains Mono', monospace
   │
   │ 📊 DATA-VIZ CHARTS: Area Sparkline (Throughput / Requests/sec) & Segmented Ring (Resource Utilization)
   │
   │ 🛡️ PRE-DELIVERY CRAFT CHECKLIST:
   │   [ ] Zero Emoji Icons: Strictly use Lucide or Heroicons SVGs
   │   [ ] Tactile Press: active:scale-[0.98] + cursor-pointer on all clickables
   │   [ ] Resilient Text: text-wrap: balance on headings, zero clipped chips
   │   [ ] Mobile Touch Targets: 44x44pt (iOS) / 48x48dp (Android/Web)
   │   [ ] Dynamic Contrast: --elevated-foreground enforced (Zero washed-out text)
   └────────────────────────────────────────────────────────────────────────────────────────┘
   ```
3. **List ALL Available Alternatives in that Category**: Detail all 4-5 alternative families in that vertical with their family IDs, display names, accents, and specific vibes.
4. **Ask the User for Theme & Polarity Choice in Plain Markdown Text**:
   > **🌓 Theme & Polarity Selection:**
   > - **(Recommended) Support for Both (Dual Light & Dark with toggle)** — *Modern production standard with zero-flash toggle and system preference auto-detection.*
   > - **Dark Mode only** — *Sleek, high-focus obsidian aesthetic.*
   > - **Light Mode only** — *Crisp daylight clarity and high-contrast readability.*
   >
   > *Would you like to proceed with the recommended palette in **Dual Mode**, or switch to one of the alternatives above?*

#### ⛔ MANDATORY HARD STOP (DO NOT BUILD CODE YET!):
- **DO NOT** write application code (HTML, JSX, TSX, CSS).
- **DO NOT** scaffold the project or create repository files.
- **DO NOT** call the `ask_question` modal tool (which suppresses the chat UI and opens a blocking text-only prompt).
- **END YOUR TURN IMMEDIATELY** after outputting the preview embed, the blueprint box, and the questions above. Wait for the user's response!

---

### 🚀 PHASE 2: Code Implementation (NEXT TURN — AFTER USER REPLIES)

Only **after** the user replies to confirm their theme choice or select an alternative, proceed with building the project:

#### Step 3: Compile Design Tokens & Output Bundle
Run the synthesis engine with `--persist` targeting the user's confirmed palette:
```bash
python3 ~/.gemini/config/skills/ui-ux-ultra/scripts/design_engine.py --palette-id <confirmed-id> --persist -p "<Project Name>"
```

This compiles:
- `design-system/theme-tokens.css`: Standard CSS custom properties for light & dark modes
- `design-system/shadcn-globals.css`: Drop-in `globals.css` with HSL variables for shadcn/ui
- `design-system/tailwind-v4.css`: Modern Tailwind CSS v4 `@theme` configuration
- `design-system/tailwind.tokens.js`: Ready-to-import Tailwind CSS v3 color map
- `design-system/flutter_theme.dart`: Material 3 ThemeData with light & dark ColorSchemes
- `design-system/Theme.swift`: SwiftUI semantic Color extensions & iOS HIG constants
- `design-system/motion.tokens.js`: Framer Motion spring presets and easing curves
- `design-system/theme-toggle.js`: Zero-flash client-side theme switcher
- `design-system/MASTER.md`: Design system documentation and token reference

#### Step 4: Inject Semantic Design Tokens into the Project
Import `design-system/theme-tokens.css` into the project's main stylesheet. All UI elements must reference these semantic tokens rather than raw hardcoded hex codes:

```css
:root, [data-theme="light"] {
  --bg-canvas: #F8FAFC;        /* Base page background */
  --bg-surface: #FFFFFF;       /* Cards, modals, sidebars */
  --bg-elevated: #F1F5F9;      /* Dropdowns, hover states, chips, toggles */
  --text-primary: #0B0F19;     /* Headlines, body reading text, toggle text */
  --text-muted: #475569;       /* Secondary labels, hints, captions */
  --accent-primary: #4F46E5;   /* Primary CTAs, active highlights */
  --accent-foreground: #FFFFFF;/* Text/icon color ON top of accent background */
  --accent-secondary: #0D9488; /* Badges, secondary actions, metrics */
  --elevated-foreground: #0B0F19; /* High-contrast text on elevated cards & toggles */
  --border-color: #E2E8F0;     /* Dividers, card strokes */
}

[data-theme="dark"] {
  --bg-canvas: #08090C;
  --bg-surface: #11131A;
  --bg-elevated: #1A1D27;
  --text-primary: #F3F4F6;
  --text-muted: #8A94A6;
  --accent-primary: #6366F1;
  --accent-foreground: #FFFFFF;
  --accent-secondary: #14B8A6;
  --elevated-foreground: #F3F4F6;
  --border-color: #222634;
}
```

#### 🛡️ Dynamic Foreground-Background Contrast Rules (Zero Washed-Out Text)
1. **Container-Relative Inversion**:
   - In **Dark Mode**, elevated containers (cards, toggles, badges, chips) have dark backgrounds (`#1A1D27` or `rgba(255,255,255,0.08)`) with light foreground text (`#F3F4F6`).
   - In **Light Mode**, elevated containers flip to light backgrounds (`#F1F5F9` or `rgba(0,0,0,0.06)`). Their foreground text **MUST** flip to high-contrast dark text (`var(--text-primary)` or `var(--elevated-foreground)`, e.g. `#0B0F19` or `#241914`).
   - **CRITICAL ANTI-PATTERN**: Never hardcode light text utility classes (e.g. `text-white`, `text-gray-100`, `text-[#FAF5EE]`) onto toggle buttons, badges, secondary buttons, or form controls that flip in Light Mode. Always use `var(--elevated-foreground)` or `var(--text-primary)`.
2. **Primary Accent Contrast**:
   - Primary action buttons must always use `--accent-foreground` computed against the accent's luminance (e.g. `#FFFFFF` on dark indigo/slate, `#0B0F19` on high-luminance volt/lime/yellow).
3. **Interactive Toggle Buttons**:
   - Mode toggles (`🌓 Toggle Light/Dark`) must explicitly update their `color`, `background-color`, and `border-color` on switch, guaranteeing a minimum of **7:1 AAA contrast** in both states.

### Step 4: Configure Tech Stack (Tailwind / Next.js / CSS)

#### In Tailwind CSS (`tailwind.config.js`)
```javascript
module.exports = {
  darkMode: ['class', '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        canvas: 'var(--bg-canvas)',
        surface: 'var(--bg-surface)',
        elevated: 'var(--bg-elevated)',
        primary: 'var(--text-primary)',
        muted: 'var(--text-muted)',
        accent: {
          DEFAULT: 'var(--accent-primary)',
          foreground: 'var(--accent-foreground)',
          secondary: 'var(--accent-secondary)'
        },
        'elevated-foreground': 'var(--elevated-foreground)',
        border: 'var(--border-color)'
      },
      fontFamily: {
        display: ['var(--font-display)'],
        sans: ['var(--font-sans)'],
        mono: ['var(--font-mono)']
      },
      borderRadius: {
        card: 'var(--radius-card)'
      }
    }
  }
};
```

#### In Tailwind CSS v4 (`main.css`)
```css
@theme {
  --color-canvas: var(--bg-canvas);
  --color-surface: var(--bg-surface);
  --color-elevated: var(--bg-elevated);
  --color-primary: var(--text-primary);
  --color-muted: var(--text-muted);
  --color-accent: var(--accent-primary);
  --color-accent-foreground: var(--accent-foreground);
  --color-accent-secondary: var(--accent-secondary);
  --color-elevated-foreground: var(--elevated-foreground);
  --color-border: var(--border-color);
  --font-display: var(--font-display);
  --font-sans: var(--font-sans);
  --font-mono: var(--font-mono);
}
```

### Step 5: Apply Curated Font Pairings
Load Google Fonts matched to the domain personality:

| Archetype / Domain | Display Font | Sans / Interface Font | Monospace Font | Google Fonts Embed Link |
| :--- | :--- | :--- | :--- | :--- |
| **Tech, SaaS, AI** | Space Grotesk | Plus Jakarta Sans | JetBrains Mono | `family=JetBrains+Mono:wght@400;600&family=Plus+Jakarta+Sans:wght@400;600;700&family=Space+Grotesk:wght@600;700` |
| **Editorial, Luxury, Art** | Fraunces | Plus Jakarta Sans | JetBrains Mono | `family=Fraunces:opsz,wght@9..144,600;700&family=Plus+Jakarta+Sans:wght@400;500;600` |
| **Dev Tools, CLI, Web3** | JetBrains Mono | Inter | JetBrains Mono | `family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700` |
| **Modernist, Studio** | Syne | Plus Jakarta Sans | Space Mono | `family=Plus+Jakarta+Sans:wght@400;600&family=Syne:wght@600;700;800` |

### Step 6: Architectural UI Style Selection
Select the design style that amplifies the chosen palette:

1. **Bento Grid**: Modern modular cards with subtle borders (`1px solid var(--border-color)`), 14px-18px corner radius, and varied column spans (12-column grid: `col-span-8`, `col-span-4`, `col-span-6`).
2. **Glassmorphic Elevated**: Surfaces with `backdrop-filter: blur(16px)` and semi-transparent alpha borders `rgba(255,255,255,0.08)`.
3. **High-Density Dashboard**: Compact tables, pill badges (`--bg-elevated`), monospace metric indicators, and crisp dividers.
4. **Editorial Luxury**: Large serif headlines (`--font-display`), generous whitespace (padding: 4rem-6rem), and hairline dividers.
5. **Modern Cyberpunk / Neon**: Deep dark canvas (`#08090C`), high-saturation neon accents (`#00F5D4`, `#FF2A85`), glow drop-shadows `0 0 24px rgba(var(--accent-primary), 0.3)`.

### Step 7: Dual-Theme Switching Implementation
Add the zero-flash theme script in the document `<head>`:

```html
<script>
  (function() {
    const stored = localStorage.getItem('theme-preference');
    const theme = stored || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', theme);
  })();
</script>
```

Add a toggle button in the navbar:
```html
<button onclick="toggleTheme()" class="theme-btn" aria-label="Toggle Light/Dark Theme">
  🌓 Theme
</button>
```

---

## 2. Complete 20-Category Domain Architecture

UI/UX Ultra organizes **200 palettes** across **20 categories** (5 curated families each, in both Light and Dark polarities):

```
UI/UX Ultra (200 Palettes)
├── 01. saas             (5 Families: Linear, Stripe, Geist, Raycast, Attio)
├── 02. education        (5 Families: Oxford, Axiom, Kinetic, Bauhaus, Montessori)
├── 03. pet-services     (5 Families: Sunny Meadow, Nordic Vet, Cozy Whiskers, Woodland, Reef)
├── 04. ai-chatbot       (5 Families: Velvet Cosmos, Anthropic Warm, Synapse Cyan, Aurora, Terminal)
├── 05. e-commerce       (5 Families: Atelier Alabaster, Tokyo Street, Nordic Home, Bazaar, Sonic)
├── 06. fintech-crypto   (5 Families: Emerald Quant, Swiss Private, DeFi Plasma, Neobank Lime, Ledger)
├── 07. healthcare       (5 Families: Clinical Telehealth, Biopharma, Mindful Sanctuary, Pediatric, Dental)
├── 08. creative         (5 Families: Motion Amber, Hyper 3D, Risograph Press, Brutalist, Monotype)
├── 09. real-estate      (5 Families: Architectural Marble, PropTech, Alpine Timber, Metropolitan, Campus)
├── 10. gaming           (5 Families: Cyberpunk HUD, 8-Bit Arcade, Apex Esports, Fantasy Lore, Cozy Island)
├── 11. food-restaurant  (5 Families: Omakase Hinoki, Neo-Diner Flame, Sourdough Hearth, Taproom, Matcha)
├── 12. fitness          (5 Families: Crossfit High-Volt, Mindful Yoga, Velocity Run, Aqua Tri, Combat)
├── 13. travel           (5 Families: Bharat Grand Trunk, Himalayan Alpine, Kyoto Rail, Archipelago, Lounge)
├── 14. nft-web3         (5 Families: Hologram Vault, Solana UV, Ordinal Amber, Agora DAO, Spatial Prism)
├── 15. beauty-spa       (5 Families: Aesop Apothecary, Rosewater, Onsen Hinoki, Derma Peel, Kumkumadi)
├── 16. developer-tools  (5 Families: Teenage Chassis, Warp Obsidian, Supabase Emerald, Grafana, Monokai)
├── 17. entertainment    (5 Families: Mythic Agni, A24 Cinema Noir, 2.5D Manhwa, Symphony Brass, Hi-Fi Vinyl)
├── 18. legal            (5 Families: Lincoln Mahogany, Patent IP, Supreme Wax Seal, Civic Policy, Family Trust)
├── 19. events           (5 Families: Afterhours Arcade, Arena Festival, Royal Mandap, Tech Summit, Gala)
└── 20. other            (5 Families: Universal Bento, Warm Craft PKM, CAD Blueprint, Nordic Calm, Kinetic Mono)
```

### Curated Palette Catalog Quick Reference

| Category | Family ID | Primary Name | Vibes | Light Accent | Dark Accent |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `saas` | `saas-linear-indigo` | Linear Obsidian & Indigo | Modern precision command-bar | `#4F46E5` | `#6366F1` |
| `saas` | `saas-stripe-violet` | Stripe Mesh & Royal Slate | Enterprise billing clean | `#635BFF` | `#7A73FF` |
| `saas` | `saas-vercel-geist` | Geist Monochrome & Signal | Minimalist stark edge | `#000000` | `#FFFFFF` |
| `ai-chatbot` | `ai-velvet-cosmos` | Velvet Cosmos & Neural Violet | LLM reasoning copilot | `#7C3AED` | `#8B5CF6` |
| `ai-chatbot` | `ai-anthropic-warm` | Humanist Parchment & Clay | Humanist research alignment | `#C86446` | `#E07A5F` |
| `ai-chatbot` | `ai-synapse-cyan` | Synapse Matrix & Bioluminescence | Autonomous voice AI | `#059669` | `#10B981` |
| `developer-tools`| `dev-teenage-chassis` | Field Aluminium & Intl Orange | Hardware synth calculator | `#FF4F00` | `#FF5E1A` |
| `developer-tools`| `dev-supabase-emerald`| Postgres Emerald & Carbon | Database backend docs | `#10B981` | `#34D399` |
| `fintech-crypto` | `fin-emerald-quant` | Emerald Quant & Institutional | Wall Street wealth terminal | `#059669` | `#10B981` |
| `fintech-crypto` | `fin-swiss-private` | Zurich Private Banking Gold | Heritage gold card wealth | `#9A7B3E` | `#D4AF37` |
| `e-commerce` | `ecom-atelier-alabaster`| Atelier Alabaster & Espresso | Luxury fashion apparel lookbook | `#8C4A27` | `#D48C6A` |
| `e-commerce` | `ecom-tokyo-street` | Shibuya Streetwear & Volt | Limited sneakers drops | `#FF2A00` | `#CCFF00` |
| `healthcare` | `health-telehealth-sky` | Nordic Telehealth & Pure Sky | HIPAA clinic calm trust | `#0284C7` | `#38BDF8` |
| `creative` | `creative-hyper-3d` | Hyper-Spatial Glass & Cyan | 3D visual generative | `#06B6D4` | `#00F5D4` |
| `gaming` | `game-cyber-neon` | Night City Cyberpunk HUD | Neon raytracing HUD | `#FF0055` | `#00F5D4` |
| `nft-web3` | `web3-solana-uv` | High-TPS Ultraviolet & Mint | Solana DePIN launchpad | `#9333EA` | `#14F195` |
| `beauty-spa` | `beauty-aesop-amber` | Apothecary Amber & Botanical | Luxury botanical skincare | `#8C583A` | `#C88A65` |
| `events` | `event-royal-utsav` | Royal Mandap Marigold & Sindoor| Cultural wedding celebration | `#C83E2B` | `#F59E0B` |
| `other` | `other-bento-neutral` | Universal Bento Studio | Personal hub multi-tool | `#18181B` | `#FAFAFA` |

---

---
## 3. The 20-Domain Anti-Patterns Playbook ("What to Avoid")

To ensure modern, high-craft aesthetics, follow these strict domain guardrails:

| Category | Top Anti-Patterns to AVOID | Correct Implementation Rule |
| :--- | :--- | :--- |
| **`saas`** | Default Tailwind blue (`#2563EB`), fuzzy drop-shadows on dark canvas, low-contrast grey text. | Use dark Obsidian canvas with crisp 1px borders, subtle rim-lighting (`inset 0 1px 0 rgba(255,255,255,0.08)`), and Indigo/Teal accents. |
| **`ai-chatbot`** | Over-saturated glowing purple gradients that cause eye strain, generic robot avatars. | Use deep velvet canvas or warm humanist parchment with clean mono typography for generated tokens. |
| **`fintech-crypto`** | Unbordered cards on dark backgrounds, neon green text for long tabular numbers, aggressive pure red for minor market dips. | Use muted terracotta/rose for downward trends, tabular numerals (`font-variant-numeric: tabular-nums`), and high-contrast borders. |
| **`developer-tools`** | Large rounded corners (`>10px`), slow transitions (`>300ms`), playful cartoon iconography. | Stick to sharp/compact corners (`4px-8px`), instantaneous feedback (`<150ms`), and monospace metrics in JetBrains Mono. |
| **`healthcare`** | Pure black (`#000000`) text on pure white, high-contrast alarming red warnings for routine reminders. | Use clinical calm sky/teal tones, softened dark slate text (`#0F1D26`), and generous whitespace for patient accessibility. |
| **`e-commerce`** | Blinking countdown timers, low-resolution badges, busy multi-colored buttons competing for attention. | Single dominant accent CTA, generous card padding ($>24\text{px}$), and editorial typography (Fraunces/Syne) for luxury. |
| **`education`** | Cluttered dense layouts resembling 1990s academic PDFs, or overly childish pastels for adult learning. | Clean modular cards, clear hierarchy, high-contrast progress indicators, and warm brass/oxford accents. |
| **`gaming`** | Unreadable grunge fonts for body text, neon colors on light canvas. | High-contrast HUD layout, monospace data displays, and neon accents strictly preserved for dark canvases. |
| **`food-restaurant`** | Cold clinical blues/purples (which suppress appetite), tiny illegible menu text. | Warm organic hearth tones (saffron, clay, hinoki amber), high-contrast pricing, and tactile photography cards. |
| **`legal`** | Casual sans fonts for formal clauses, bright neon buttons, bubbly pill tags. | Classical authority (Fraunces/Cinzel headers), Lincoln mahogany/navy accents, and formal structured tables. |
| **`real-estate`** | Distorted property imagery, cramped card grids, unstyled MLS raw data. | High-resolution hero media, generous 16px border-radius, clean amenity pill chips, and clear pricing callouts. |
| **`beauty-spa`** | Sharp harsh corners, neon high-voltage colors, dense data tables. | Organic earth/botanical palettes, generous whitespace ($>48\text{px}$), and subtle tactile borders. |

---

## 4. Modern Stack Integration: Shadcn UI, Tailwind v4 & Motion

When `--persist` is run, UI/UX Ultra outputs native configurations for all major frontend stacks:

### 1. Shadcn UI (`design-system/shadcn-globals.css`)
Drop directly into Next.js/Vite `app/globals.css`. Fully maps:
`--background`, `--foreground`, `--card`, `--primary`, `--secondary`, `--muted`, `--accent`, `--destructive`, `--border`, `--input`, `--ring`, and `--chart-1` through `--chart-5`.

### 2. Tailwind CSS v4 (`design-system/tailwind-v4.css`)
Modern `@theme` directive ready to import into your stylesheet:
```css
@import "tailwindcss";
@import "./design-system/tailwind-v4.css";
```

### 3. Motion & Micro-Interactions (`design-system/motion.tokens.js`)
Calibrated Framer Motion springs and cubic-bezier curves:
```javascript
import { motionTokens } from './design-system/motion.tokens';

// In your Framer Motion component:
<motion.div {...motionTokens.framer.fadeInUp} />
```

### 4. Flutter Material 3 (`design-system/flutter_theme.dart`)
Production-ready Flutter theme with synchronized light & dark ColorSchemes and Fitts's Law touch compliance:
```dart
import 'package:flutter/material.dart';
import 'design-system/flutter_theme.dart';

void main() => runApp(MaterialApp(
  theme: AppTheme.lightTheme,
  darkTheme: AppTheme.darkTheme,
  themeMode: ThemeMode.system,
  home: const HomeScreen(),
));
```

### 5. SwiftUI Multi-Platform (`design-system/Theme.swift`)
iOS Human Interface Guidelines (HIG) compliant colors, corner radii, and Apple spring animations:
```swift
import SwiftUI

struct CardView: View {
  @Environment(\.colorScheme) var colorScheme

  var body: some View {
    VStack {
      Text("Telemetry Active")
        .foregroundColor(colorScheme == .dark ? AppTheme.Dark.textPrimary : AppTheme.Light.textPrimary)
    }
    .padding()
    .background(colorScheme == .dark ? AppTheme.Dark.surface : AppTheme.Light.surface)
    .cornerRadius(AppTheme.cornerRadiusCard)
  }
}
```

---

## 5. High-Level Design Theory & UX Laws Intelligence

UI/UX Ultra enforces the foundational psychological laws of human-computer interaction:

### The 8 Foundational Laws of UX
1. **Fitts's Law (Target Accessibility)**:
   - The time to acquire a target is a function of the distance to and width of the target.
   - **Rule**: Minimum touch targets must be **$44 \times 44\text{pt}$ on iOS** and **$48 \times 48\text{dp}$ on Android/Web**.
   - **Rule**: Position primary CTAs within the natural thumb zone (bottom sheets or persistent bottom action bars) on mobile.
2. **Hick-Hyman Law (Decision Latency)**:
   - The time it takes to make a decision increases logarithmically with the number and complexity of choices.
   - **Rule**: Never present more than 1 primary CTA per screen. Use secondary ghost buttons for alternatives.
   - **Rule**: Break complex multi-field inputs into step-by-step progressive forms.
3. **Miller's Law (Working Memory Chunking)**:
   - The average person can hold $7 \pm 2$ items in their working memory.
   - **Rule**: Chunk complex dashboards into distinct bento-grid modules with clear border boundaries.
   - **Rule**: Format numbers, phone inputs, and credit cards into rhythmic visual clusters.
4. **Jakob's Law (Familiarity Principle)**:
   - Users spend most of their time on other sites. They prefer your site to work the same way as all the other sites they already know.
   - **Rule**: Maintain conventional UI paradigms (search at top, cart/profile at top-right, navigation drawer on left). Don't reinvent standard patterns without overwhelming cause.
5. **Doherty Threshold (Under-400ms Productivity)**:
   - Productivity soars when a computer and its users interact at a pace that ensures neither has to wait on the other ($< 400\text{ms}$).
   - **Rule**: Always employ **Optimistic UI updates** on buttons and toggles.
   - **Rule**: Use shimmering skeleton screens instead of blocking spinner modals for background fetches.
6. **Law of Proximity & Common Region (Gestalt Grouping)**:
   - Elements close to each other or enclosed within a shared boundary are perceived as a single conceptual group.
   - **Rule**: Labels must be closer to their corresponding input ($4\text{px}-8\text{px}$) than to the preceding form field ($16\text{px}-24\text{px}$).
   - **Rule**: Enclose related data in cards using `--bg-surface` and 1px `--border-color`.
7. **Aesthetic-Usability Effect**:
   - Users perceive aesthetically pleasing design as design that is more usable, forgiving minor usability hurdles.
   - **Rule**: Never omit micro-details: subtle rim-lighting (`--shadow-rim`), Apple-style spring animations (`motionTokens.ease.snappy`), and optical padding.
8. **Peak-End Rule**:
   - People judge an experience largely based on how they felt at its peak and at its end.
   - **Rule**: Design celebratory micro-delight moments at task completion (subtle haptic feedback, checkmark animations, confetti on checkout).

### Spatial & Layout Architecture
- **The 8pt Grid System**: All margins, paddings, icon bounds, and layout dimensions must be multiples of 4 or 8:
  - `4px` (Tight micro-gaps, badge padding)
  - `8px` (Standard inner spacing, button padding-y)
  - `16px` (Default card padding, form field gap)
  - `24px` (Grid gutter, section gap)
  - `32px` / `48px` / `64px` (Major layout boundaries & hero sections)
- **Modular Typography Scale**: Uses a **1.250 Major Third** ratio:
  - Caption: `0.75rem` (12px)
  - Body: `0.875rem` / `1rem` (14px / 16px)
  - H4: `1.25rem` (20px)
  - H3: `1.563rem` (25px)
  - H2: `1.953rem` (31px)
  - H1: `2.441rem` - `3.5rem` (39px - 56px)
- **Optical Balance & Centering**:
  - Geometric centers are often optically bottom-heavy. Action icons (like play triangles or chevrons) must be offset by $1\text{px}-2\text{px}$ to achieve visual equilibrium.

---

## 6. Multi-Platform Mobile Guidelines (iOS HIG & Android Material 3)

When developing mobile apps using UI/UX Ultra:

### iOS Human Interface Guidelines (HIG) Best Practices
- **Safe Area Insets**: Always respect `.ignoresSafeArea(.all, edges: .top)` for backgrounds while anchoring interactive controls strictly within safe area guides.
- **Dynamic Type**: Never hardcode pixel sizes for body text. Use semantic text styles (`.font(.body)`) so users' iOS accessibility font size settings are honored.
- **Apple Spring Physics**: Avoid linear or mechanical easing. Always use fluid springs:
  - Snappy: `Animation.spring(response: 0.35, dampingFraction: 0.8)`
  - Bouncy: `Animation.spring(response: 0.45, dampingFraction: 0.65)`
- **Haptic Feedback**: Trigger `UIImpactFeedbackGenerator(style: .light).impactOccurred()` on primary button taps, theme toggles, and swipe completions.

### Android Material 3 Best Practices
- **Dynamic Color**: Material 3 surfaces leverage tonal palettes derived from the primary accent seed.
- **Elevation via Tone, Not Shadow**: In dark mode, higher elevation is communicated through lighter surface tints (`--bg-elevated`), not drop shadows.
- **Predictive Back Navigation**: Ensure screen transitions support Android 14+ predictive back gestures with smooth scale and fade transitions.

---

## 7. Domain-Coupled Conversion Page Blueprints (All 20 Categories)

High-converting user experiences depend on section architectures tailored to the psychological trigger of each domain. UI/UX Ultra encodes proven 5-step section flows for every category:

| Category | Conversion Pattern | Primary Conversion Focus | 5-Step Section Architecture |
| :--- | :--- | :--- | :--- |
| **`saas`** | Command Hero + Interactive Bento Matrix | Product-led trial conversion & enterprise demo | 1. Hero with telemetry pill & dual CTA<br>2. Bento feature matrix with live micro-interactions<br>3. Interactive terminal / API playground<br>4. Uptime telemetry (99.99%) & enterprise logos<br>5. Tiered pricing matrix + sticky bottom conversion bar |
| **`education`** | Curriculum Milestone & Instructor Proof | Course enrollment & syllabus download | 1. Hero with course outcome badge & video preview<br>2. Interactive curriculum syllabus tree<br>3. Faculty credentials & student outcome metrics<br>4. Live peer review carousel & project showcase<br>5. Enrollment countdown & flexible tuition options |
| **`pet-services`** | Emotional Trust & Instant Booking Calendar | Online booking & vet consultation scheduling | 1. Hero with warm pet imagery & immediate booking widget<br>2. Care service tiers (Daycare, Grooming, Medical)<br>3. Certified vet staff profiles & safety certifications<br>4. Pet parent photo reviews & satisfaction guarantees<br>5. Interactive location map & urgent care contact bar |
| **`ai-chatbot`** | Live Prompt Playground & Token Telemetry | Instant model playground test & API signup | 1. Hero with live conversational playground<br>2. Latency/benchmark telemetry vs frontier models<br>3. Pre-built agent workflow templates<br>4. Enterprise data security & zero-retention guarantee<br>5. Developer API keys generation & token calculator |
| **`e-commerce`** | Visual Lookbook Grid & 1-Click Checkout | Cart add rate & collection discovery | 1. Full-bleed editorial hero with seasonal drop badge<br>2. Curated collection grid with quick-view modal<br>3. Social proof gallery & customer styled looks<br>4. Material provenance & sustainability breakdown<br>5. 1-click Apple Pay/Google Pay express bag |
| **`fintech-crypto`** | Institutional Security & Live Ticker Bento | Account deposit & institutional onboarding | 1. Hero with real-time asset ticker & instant KYC start<br>2. Bento metrics (Yield, AUM, SOC-2/FINRA compliance)<br>3. Interactive fee comparison simulator<br>4. Cold storage architecture & insurance backing<br>5. Biometric mobile app QR download & signup card |
| **`healthcare`** | Empathetic Trust & Direct Intake Pathway | Telehealth visit booking & HIPAA assurance | 1. Calming hero with condition search & specialist booking<br>2. Clinical services directory with transparent pricing<br>3. Board-certified physician credentials & hospital affiliations<br>4. HIPAA compliance & insurance provider eligibility checker<br>5. 24/7 emergency triage hotline & patient portal login |
| **`creative`** | Full-Bleed Showcase & Case Study Reel | Client inbound inquiries & project kickoff | 1. Cinematic portfolio reel with dynamic filter tags<br>2. Deep-dive case studies with quantifiable client ROI<br>3. Design process breakdown (Sprint, Build, Ship)<br>4. Industry awards, Press recognition & Client quotes<br>5. Interactive project scope estimator & inquiry form |
| **`real-estate`** | Spatial Discovery & MLS Property Matrix | Property tour scheduling & agent contact | 1. Hero with interactive location search & filter pills<br>2. Featured properties carousel with 3D virtual tour badges<br>3. Neighborhood amenities, schools & transit walkscore<br>4. Verified agent broker credentials & recent transactions<br>5. Private VIP showing booking modal & mortgage calculator |
| **`gaming`** | Immersive Cinematic Lore & Battle Pass HUD | Game client pre-order & Discord guild join | 1. Full-motion video hero with cinematic sound toggle<br>2. Playable character class showcase & skill tree preview<br>3. Battle pass rewards track & seasonal leaderboard<br>4. Esports tournament highlights & Twitch live streamers<br>5. Instant game launcher download & early access claim |
| **`food-restaurant`** | Sensory Appetite Appeal & Instant Table Reserve | Dinner reservation & online delivery order | 1. High-sensory food photography hero with table booking bar<br>2. Seasonal tasting menu with dietary allergen badges<br>3. Chef's table story & local farm sourcing provenance<br>4. Guest photo reviews & culinary press accolades<br>5. Interactive seating calendar & gift card purchase |
| **`fitness`** | High-Energy Transformation & Class Pass Trial | Free 7-day pass claim & gym membership sign-up | 1. Kinetic video hero with transformation milestone ticker<br>2. Class schedule matrix with coach credentials<br>3. Member body-composition results & before/after case studies<br>4. Gym facility tour & recovery amenities (Sauna, Cryo)<br>5. Zero-commitment trial pass claim & membership tier picker |
| **`travel`** | Experiential Destination Reel & Itinerary Builder| Itinerary booking & custom quote request | 1. Breathtaking destination hero with dates & guests picker<br>2. Curated day-by-day bespoke itineraries<br>3. Verified local guide credentials & traveler photo reviews<br>4. Transparent all-inclusive pricing breakdown<br>5. Flexible cancellation guarantee & instant reservation |
| **`nft-web3`** | Mint Countdown & Trait Rarity Explorer | Wallet connect & primary mint purchase | 1. Hero with live mint countdown & supply progress bar<br>2. Trait rarity matrix & dynamic generative 3D preview<br>3. Roadmap milestones (Phase 1 to Phase 4 utility)<br>4. Smart contract audit verification (OpenZeppelin / CertiK)<br>5. Web3 wallet connect & Discord community portal |
| **`beauty-spa`** | Botanical Sensory Journey & Wellness Booking | Treatment appointment booking & ritual kit purchase | 1. Serene botanical hero with treatment calendar booking<br>2. Signature spa rituals & holistic ingredient index<br>3. Certified aesthetician profiles & organic certifications<br>4. Client transformation testimonials & press mentions<br>5. Gift certificate generator & bespoke concierge booking |
| **`developer-tools`** | CLI Terminal First & Documentation Sandbox | CLI install command copy & documentation reading | 1. Hero with 1-click terminal install snippet & GitHub stars<br>2. Interactive documentation sandbox with live code preview<br>3. Architecture benchmarks vs legacy tooling (10x faster)<br>4. Open-source contributor community & ecosystem plugins<br>5. CLI copy bar & cloud deployment start |
| **`entertainment`** | Trailer Cinema Vault & Seat Selection Grid | Ticket purchase & media streaming subscription | 1. Full-screen trailer hero with showtime selector<br>2. Cast and director spotlight with exclusive interviews<br>3. Interactive IMAX / Dolby seat reservation map<br>4. Rotten Tomatoes & critic praise quotes<br>5. Mobile ticket pass download & concessions pre-order |
| **`legal`** | Authoritative Counsel & Confidential Case Intake| Free consultation request & case assessment | 1. Hero with practice area focus & 24/7 hotline banner<br>2. Recovered damages track record ($100M+ recovered)<br>3. Attorney partner profiles & Bar association honors<br>4. Confidential client case histories & testimonials<br>5. Secure encrypted case assessment intake form |
| **`events`** | Dynamic Speaker Lineup & Pass Tier Countdown | Ticket registration & VIP pass purchase | 1. High-impact keynote video hero with date/venue badge<br>2. Keynote speaker grid with talk abstracts<br>3. Multi-track agenda schedule (Engineering, Design, Growth)<br>4. Previous year aftermovie & attendee company logos<br>5. Tiered ticket pricing (Early Bird, VIP) & group checkout |
| **`other`** | Modular Bento Grid & Multipurpose Action Bar | Primary engagement & application launch | 1. Bento hero with primary value proposition & live search<br>2. Modular functional widgets with micro-actions<br>3. User workflow templates & step-by-step guides<br>4. Telemetry metrics & verified user ratings<br>5. Universal action bar & cross-platform download links |

---

## 8. Metric-to-Chart Pattern Blueprints

When building analytics dashboards, data visualization must map directly to the domain's core metric architecture. UI/UX Ultra configures 5 semantic chart tokens (`--chart-1` through `--chart-5`) paired to specific chart types:

| Domain | Primary Chart Architecture (`--chart-1` / `--chart-2`) | Secondary / Alert Series (`--chart-3`, `--chart-4`, `--chart-5`) |
| :--- | :--- | :--- |
| **`saas`** | Area Sparkline (Throughput / Requests/sec) & Segmented Ring (Resource Utilization) | `--chart-3`: Target quota, `--chart-4`: Error spikes (P99), `--chart-5`: Baseline projection |
| **`fintech-crypto`** | Candlestick / OHLC Chart with Volume Histogram & Order Book Depth Area | `--chart-3`: 24h Moving Avg, `--chart-4`: Stop-loss threshold, `--chart-5`: Liquidity band |
| **`ai-chatbot`** | Token Generation Velocity Line & Latency Distribution Histogram (P50/P90/P99) | `--chart-3`: Context window utilization, `--chart-4`: Throttling/rate-limit, `--chart-5`: Cost/1k tokens |
| **`developer-tools`** | Build Duration Stepline & Test Matrix Pass/Fail Heatmap Grid | `--chart-3`: Flaky test count, `--chart-4`: CI failure rate, `--chart-5`: Historical build median |
| **`healthcare`** | Continuous Vitals Biometric Waveform & Medication Adherence Donut | `--chart-3`: Target clinical threshold, `--chart-4`: Elevated vital alert, `--chart-5`: Patient baseline |
| **`e-commerce`** | Daily GMV Revenue Trend Bar & Checkout Funnel Step Area (Drop-off Analysis) | `--chart-3`: Conversion goal, `--chart-4`: Cart abandonment rate, `--chart-5`: Prior period comparison |
| **`fitness`** | Heart Rate Zone Distribution Area & Weekly Caloric Burn Radial Bar | `--chart-3`: VO2 max target, `--chart-4`: Peak threshold, `--chart-5`: Resting heart rate |
| **`real-estate`** | Historical Neighborhood Price Trend & Price vs SqFt Scatter Plot | `--chart-3`: Median listing price, `--chart-4`: Price drops, `--chart-5`: Metro average benchmark |

---

## 9. Pre-Delivery Production Craft Checklist

Before finalizing any user interface, verify every item against this strict production-grade craft checklist:

- [ ] **Zero Emoji Icons**: Strictly use clean SVG icons (Lucide, Heroicons, Phosphor). Never render Unicode emojis (e.g. 🚀, ⚡, 💡) as UI icons or button decorators.
- [ ] **Tactile Press Feedback**: Every interactive button, chip, and card must include `active:scale-[0.98]` and `cursor-pointer` with transition timing `duration-150 ease-out`.
- [ ] **Resilient Typography**: Headings must use `text-wrap: balance` to prevent awkward single-word orphans; containers must feature overflow-safe wrapping (`break-words`, `overflow-hidden` where appropriate).
- [ ] **Mobile-First Touch Ergonomics**: Minimum touch bounding boxes of **44x44pt on iOS** and **48x48dp on Android/Web**; primary mobile CTAs anchored within thumb-accessible zones.
- [ ] **Dynamic Contrast Enforced**: All badge chips, elevated cards, and mode toggles must use `--elevated-foreground` rather than hardcoded light/dark text classes, guaranteeing **WCAG AAA (>7:1)** contrast across both themes.
- [ ] **Zero-Flash Theme Switching**: Ensure inline script initializes `data-theme` before page render, avoiding white-screen flashes during dark mode loads.
- [ ] **Semantic Token Discipline**: All colors reference `--bg-canvas`, `--bg-surface`, `--bg-elevated`, `--text-primary`, `--accent-primary`, and `--border-color`. Zero raw hex values in application stylesheets.

---

## 10. Interactive Studio Previewer

UI/UX Ultra includes an interactive single-page studio previewer (`previewer/index.html`) allowing real-time switching between all 200 palettes, live bento UI inspection, token chip extraction, and one-click CSS copying.

- **Live Hosted Demo**: [https://pardeeppatel.github.io/ui-ux-ultra/](https://pardeeppatel.github.io/ui-ux-ultra/)
- **Local Preview Command**:
  ```bash
  npx ui-ux-ultra --preview
  # or
  npm run preview
  ```

---

## 11. Updating to the Latest Version

To update an existing installation to the latest version with new palettes, blueprints, and rules:

```bash
npx github:pardeeppatel/ui-ux-ultra --update
```
*(or re-run `npx github:pardeeppatel/ui-ux-ultra --global`)*. Antigravity and other supported editors will hot-reload the updated skill files immediately.
