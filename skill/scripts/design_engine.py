#!/usr/bin/env python3
"""
UI/UX Ultra v1.0.0 — Open-Source Design Intelligence & Multi-Platform Theme Compiler
Created by Pardeep Kumar | Powered by ToolNPlay.com (https://ToolNPlay.com)
GitHub: https://github.com/PardeepPatel/ui-ux-ultra

20 Categories x 5 Curated Families x 2 Modes (Light & Dark) = 200 Standalone Palettes
Zero external dependencies. Works with Google Antigravity, Cursor, Claude Code, Windsurf, Flutter, SwiftUI & Web.
"""

import argparse
import csv
import json
import os
import re

RAW_FAMILIES = {
    "saas": [
        ("saas-linear-indigo", "Linear Obsidian & Indigo", "modern precision command-bar developer b2b",
         ["#F8FAFC", "#FFFFFF", "#F1F5F9", "#0B0F19", "#475569", "#4F46E5", "#0D9488", "#E2E8F0"],
         ["#08090C", "#11131A", "#1A1D27", "#F3F4F6", "#8A94A6", "#6366F1", "#14B8A6", "#222634"]),
        ("saas-stripe-violet", "Stripe Mesh & Royal Slate", "payments enterprise billing clean elevated",
         ["#F6F9FC", "#FFFFFF", "#EDF2F7", "#0A2540", "#425466", "#635BFF", "#00D4B6", "#E3E8EE"],
         ["#050D1A", "#0A192F", "#112240", "#F8FAFC", "#8892B0", "#7A73FF", "#00F5D4", "#1D2D50"]),
        ("saas-vercel-geist", "Geist Monochrome & Signal", "minimalist cloud edge deployment stark",
         ["#FAFAFA", "#FFFFFF", "#F0F0F0", "#0A0A0A", "#525252", "#000000", "#0070F3", "#E5E5E5"],
         ["#000000", "#0A0A0A", "#141414", "#EDEDED", "#888888", "#FFFFFF", "#3291FF", "#262626"]),
        ("saas-raycast-crimson", "Raycast Productivity & Crimson", "launcher workflow speed keyboard macos",
         ["#F9F8F6", "#FFFFFF", "#EFECE8", "#141210", "#635E59", "#E11D48", "#F59E0B", "#E4DFD9"],
         ["#0B0A0E", "#15131B", "#201D29", "#F5F3F7", "#968FA6", "#FF3366", "#FFAA00", "#2A2636"]),
        ("saas-attio-editorial", "Attio Warm CRM & Cobalt", "crm relational database collaborative",
         ["#FAF9F5", "#FFFFFF", "#F2EFE9", "#191918", "#6B6860", "#2563EB", "#D97706", "#E6E2D8"],
         ["#0E0E0D", "#171715", "#22221F", "#F5F4F0", "#99968E", "#3B82F6", "#F59E0B", "#2E2E2A"])
    ],
    "education": [
        ("edu-oxford-parchment", "Oxford Library & Brass", "university academic research classical literature",
         ["#FCFBF7", "#F4F1EA", "#FFFFFF", "#161E2E", "#525E75", "#1E3A8A", "#B45309", "#E2DDD2"],
         ["#0A0F1D", "#121A2F", "#1B2642", "#F5F3EF", "#8E9BB5", "#60A5FA", "#F59E0B", "#263554"]),
        ("edu-brilliant-axiom", "Axiom Interactive STEM", "math physics logic puzzles interactive stem",
         ["#FFFDF9", "#F7F3EB", "#FFFFFF", "#111111", "#55524D", "#EAB308", "#10B981", "#E5DFD3"],
         ["#0D0D0C", "#171715", "#242320", "#FAFAFA", "#A3A09A", "#FACC15", "#34D399", "#302E2A"]),
        ("edu-duolingo-kinetic", "Kinetic Language Pop", "gamified language flashcards streaks kids",
         ["#F7FBF7", "#FFFFFF", "#EBF5EB", "#142416", "#4F6953", "#16A34A", "#0284C7", "#D1E7D3"],
         ["#0A140C", "#122215", "#1B3320", "#F0FDF4", "#86EFAC", "#22C55E", "#38BDF8", "#23422A"]),
        ("edu-bauhaus-studio", "Bauhaus Primary Workshop", "design art school architecture modernist",
         ["#F5F3EE", "#FFFFFF", "#EAE6DD", "#121212", "#4F4F4F", "#D92B2B", "#1D4ED8", "#121212"],
         ["#111111", "#1C1C1C", "#292929", "#F5F3EE", "#A0A0A0", "#EF4444", "#FACC15", "#F5F3EE"]),
        ("edu-montessori-botanic", "Montessori Sage & Terracotta", "early-learning calm mindful reading",
         ["#F8F7F2", "#EFECE4", "#FFFFFF", "#212922", "#5C6B5E", "#3D7A5A", "#C86D51", "#DCD7C9"],
         ["#111713", "#19221C", "#243028", "#F2F5F3", "#94A898", "#52B788", "#E07A5F", "#2F3E34"])
    ],
    "pet-services": [
        ("pet-sunny-meadow", "Sunny Paws & Clover", "dog-walking grooming cheerful friendly",
         ["#FEFBF6", "#FFF5E4", "#FFFFFF", "#2B1E16", "#6E5648", "#EA580C", "#16A34A", "#F2DFC4"],
         ["#14100E", "#1F1815", "#2C221E", "#FDF8F5", "#B0978A", "#FB923C", "#4ADE80", "#382C26"]),
        ("pet-nordic-vet", "Nordic Veterinary Clinic", "clinical vet medical pet-insurance clean",
         ["#F4FAF9", "#FFFFFF", "#E6F4F1", "#0D2624", "#4A6B68", "#0D9488", "#F59E0B", "#CBE5E0"],
         ["#071413", "#0E2422", "#163633", "#F0FDFA", "#81B5B0", "#2DD4BF", "#FBBF24", "#214A46"]),
        ("pet-cozy-whiskers", "Cozy Whiskers & Lavender", "cat-cafe adoption shelter boutique gentle",
         ["#FDF8FA", "#F7EEF2", "#FFFFFF", "#291822", "#6E5062", "#DB2777", "#7C3AED", "#EBD8E2"],
         ["#160E13", "#24161F", "#331F2C", "#FDF2F8", "#B894A9", "#F472B6", "#A78BFA", "#422839"]),
        ("pet-woodland-hound", "Woodland Hound & Bark", "outdoor adventure k9 training gear",
         ["#F7F5F0", "#EDE8DD", "#FFFFFF", "#211C15", "#63584A", "#B45309", "#15803D", "#DDD4C2"],
         ["#120F0B", "#1C1712", "#29221A", "#F7F3EB", "#A39481", "#F59E0B", "#22C55E", "#382E24"]),
        ("pet-aquatic-coral", "Reef & Exotic Aquatics", "aquarium exotic birds reptiles vibrant",
         ["#F2F9FC", "#FFFFFF", "#E1F2F7", "#08202B", "#436575", "#0284C7", "#F97316", "#C4E3ED"],
         ["#041017", "#091E2B", "#102E40", "#F0F9FF", "#7AB0C7", "#38BDF8", "#FB923C", "#1A435C"])
    ],
    "ai-chatbot": [
        ("ai-velvet-cosmos", "Velvet Cosmos & Neural Violet", "llm generative-ai copilot reasoning",
         ["#F7F6FF", "#FFFFFF", "#EDE9FE", "#140F24", "#59507A", "#7C3AED", "#EC4899", "#DDD6FE"],
         ["#070510", "#110D21", "#1B1534", "#F5F3FF", "#9B90C2", "#8B5CF6", "#F43F5E", "#2A214D"]),
        ("ai-anthropic-warm", "Humanist Parchment & Clay", "research alignment conversational reading",
         ["#F9F6F0", "#F1ECE1", "#FFFFFF", "#191714", "#666159", "#C86446", "#2E6F64", "#E2DBD0"],
         ["#12110F", "#1C1A17", "#26231F", "#F2EFE9", "#999287", "#E07A5F", "#52B788", "#332F29"]),
        ("ai-synapse-cyan", "Synapse Matrix & Bioluminescence", "autonomous-agents voice-ai real-time",
         ["#F2FBF9", "#FFFFFF", "#E0F5F0", "#071F1C", "#436661", "#059669", "#0284C7", "#C2E8E0"],
         ["#040D0C", "#091A18", "#102926", "#ECFDF5", "#74B8B0", "#10B981", "#00F5D4", "#193D38"]),
        ("ai-aurora-prism", "Aurora Glass & Hologram", "multimodal video-gen image-gen creative-ai",
         ["#FAF8FF", "#FFFFFF", "#F3E8FF", "#1E1033", "#644F82", "#9333EA", "#2563EB", "#E9D5FF"],
         ["#090612", "#130D26", "#1E153B", "#FAF5FF", "#A796C7", "#C084FC", "#38BDF8", "#32235E"]),
        ("ai-terminal-inference", "Inference Zero-Latency Mono", "local-llm cli benchmark tokens developer",
         ["#F4F4F0", "#FFFFFF", "#E8E8E2", "#111110", "#575752", "#EA580C", "#111110", "#D4D4CC"],
         ["#0A0A09", "#141412", "#1F1F1C", "#F5F5F0", "#8C8C84", "#FF6B00", "#10B981", "#2B2B26"])
    ],
    "e-commerce": [
        ("ecom-atelier-alabaster", "Atelier Alabaster & Espresso", "fashion luxury apparel lookbook d2c",
         ["#FAF8F5", "#F2EFE9", "#FFFFFF", "#181512", "#665E57", "#8C4A27", "#1F4E3D", "#E5DFD5"],
         ["#0E0C0A", "#171411", "#241F1B", "#F7F4EF", "#9E9389", "#D48C6A", "#4E9A7E", "#302A24"]),
        ("ecom-tokyo-street", "Shibuya Streetwear & Volt", "sneakers drops streetwear hype limited",
         ["#F6F6F4", "#FFFFFF", "#EAEAE6", "#0A0A0A", "#52524E", "#FF2A00", "#0044FF", "#0A0A0A"],
         ["#080808", "#121212", "#1F1F1F", "#FFFFFF", "#8C8C8C", "#CCFF00", "#FF0055", "#2E2E2E"]),
        ("ecom-nordic-home", "Copenhagen Ceramic & Oak", "furniture interior decor minimal craft",
         ["#F7F5F0", "#EFECE4", "#FFFFFF", "#1E1C1A", "#69645E", "#A16207", "#3F6212", "#DFD9CE"],
         ["#121110", "#1C1A18", "#262320", "#F5F2EB", "#9C958C", "#EAB308", "#84CC16", "#332F2B"]),
        ("ecom-fresh-bazaar", "Artisanal Pantry & Saffron", "grocery organic spices gourmet-food",
         ["#FFFDF7", "#F7F2E4", "#FFFFFF", "#211911", "#6B5B4B", "#D97706", "#15803D", "#E8DEC6"],
         ["#120E09", "#1C160F", "#292016", "#FDF8EE", "#A89682", "#F59E0B", "#22C55E", "#382C1E"]),
        ("ecom-sonic-electronics", "Precision Matte & Cobalt", "gadgets audio electronics cameras gear",
         ["#F2F4F7", "#FFFFFF", "#E4E8EE", "#0D131A", "#4F5B69", "#2563EB", "#EA580C", "#D0D7E2"],
         ["#090C10", "#11161D", "#19212B", "#F0F4F8", "#8594A6", "#3B82F6", "#F97316", "#25303F"])
    ],
    "fintech-crypto": [
        ("fin-emerald-quant", "Emerald Quant & Institutional", "trading stocks wealth terminal hedge-fund",
         ["#F4F7F6", "#FFFFFF", "#E6F0EC", "#071713", "#46635B", "#059669", "#0284C7", "#CBE0D8"],
         ["#040B09", "#091713", "#102620", "#ECFDF5", "#6EE7B7", "#10B981", "#38BDF8", "#17382F"]),
        ("fin-swiss-private", "Zurich Private Banking Gold", "private-wealth gold-standard heritage card",
         ["#F9F8F6", "#F0EDE6", "#FFFFFF", "#12151C", "#565B66", "#9A7B3E", "#1E3A8A", "#DFDAD0"],
         ["#090B10", "#11151F", "#1A202E", "#F7F5F0", "#8F96A6", "#D4AF37", "#60A5FA", "#283044"]),
        ("fin-defi-plasma", "DeFi Plasma & Zero-Knowledge", "crypto dex liquidity layer2 perp",
         ["#F5F7FF", "#FFFFFF", "#E8ECFF", "#0A0E24", "#4E557A", "#4F46E5", "#EC4899", "#D4DCFF"],
         ["#050611", "#0C0E21", "#141836", "#F2F4FF", "#8890BD", "#6366F1", "#00F5D4", "#232954"]),
        ("fin-neobank-lime", "Neobank Gen-Z Volt & Charcoal", "consumer-banking split-bills cashback wallet",
         ["#F8FAF5", "#FFFFFF", "#EDF2E6", "#0E140B", "#4F5E48", "#65A30D", "#7C3AED", "#D8E3CC"],
         ["#0A0D08", "#12170F", "#1B2416", "#F4FCE3", "#8FA882", "#A3E635", "#A855F7", "#283621"]),
        ("fin-ledger-copper", "Ledger Copper & Slate", "accounting audit tax treasury invoicing",
         ["#F7F6F4", "#FFFFFF", "#EDEBE6", "#171A1C", "#575E63", "#B45309", "#0F766E", "#DDD9D0"],
         ["#0C0E10", "#14181C", "#1E2429", "#F5F3F0", "#8D979E", "#F59E0B", "#14B8A6", "#2B333B"])
    ],
    "healthcare": [
        ("health-clinical-teal", "Mayo Clinical Calm & Teal", "hospital telemedicine patient-portal ehr",
         ["#F2F9F9", "#FFFFFF", "#E3F2F2", "#082226", "#45686E", "#0D9488", "#2563EB", "#C7E5E5"],
         ["#051114", "#0B1F24", "#123038", "#ECFEFF", "#7AB8C2", "#2DD4BF", "#38BDF8", "#1C454F"]),
        ("health-biometric-pulse", "Biometric Wearable & Coral", "cardio sleep-tracker longevity diagnostics",
         ["#FAF7F7", "#FFFFFF", "#F5ECEC", "#1F1215", "#6B5056", "#E11D48", "#0284C7", "#E8D5D8"],
         ["#0F080A", "#1A0E12", "#26151B", "#FFF1F2", "#B58A94", "#FB7185", "#38BDF8", "#3B2029"]),
        ("health-mindful-sage", "Mindful Therapy & Eucalyptus", "mental-health counseling psychology calm",
         ["#F6F8F5", "#ECEFE9", "#FFFFFF", "#1B241D", "#566659", "#3B7A57", "#D97706", "#D6DFD8"],
         ["#0D120E", "#151F18", "#1F2E23", "#F0F7F2", "#8CA692", "#52B788", "#FBBF24", "#2B4031"]),
        ("health-pharma-cobalt", "Precision Biotech & Genomics", "biotech lab genomics pharma research",
         ["#F5F8FC", "#FFFFFF", "#E8EFF8", "#0A1829", "#495E78", "#1D4ED8", "#0D9488", "#CFE0F2"],
         ["#060D17", "#0C192B", "#142742", "#F0F6FF", "#7FA0C4", "#3B82F6", "#2DD4BF", "#1E3A5F"]),
        ("health-pediatric-warm", "Warm Family Care & Apricot", "pediatrics maternity womens-health care",
         ["#FFFBF7", "#FFF3E8", "#FFFFFF", "#261812", "#6E5549", "#EA580C", "#0D9488", "#F2DCC9"],
         ["#140D0A", "#211611", "#2E1F18", "#FFF7ED", "#B39486", "#FB923C", "#2DD4BF", "#3D2920"])
    ],
    "creative": [
        ("creative-swiss-grid", "International Typographic Red", "swiss-design agency architecture poster",
         ["#FFFFFF", "#F4F4F2", "#FFFFFF", "#0A0A0A", "#525252", "#E60012", "#0A0A0A", "#0A0A0A"],
         ["#0A0A0A", "#141414", "#1F1F1F", "#FFFFFF", "#999999", "#FF1E27", "#FFFFFF", "#FFFFFF"]),
        ("creative-acid-brutal", "Neo-Brutal Acid & Violet", "indie-maker zine web-brutalism experimental",
         ["#FFFDF5", "#FFFFFF", "#F3EFE0", "#0A0A0A", "#4A4A46", "#A3E635", "#7C3AED", "#0A0A0A"],
         ["#0B0B0A", "#161614", "#22221E", "#FAF8F0", "#9E9E95", "#CCFF00", "#A855F7", "#FAF8F0"]),
        ("creative-risograph-ink", "Risograph Soy Ink & Paper", "illustration printmaker webtoon comic art",
         ["#FBF7EE", "#F2EBD9", "#FFFFFF", "#1B263B", "#5C677D", "#FF4D6D", "#00A896", "#DFD5BE"],
         ["#0F141F", "#182030", "#222D42", "#F7F2E6", "#8FA0BA", "#FF758F", "#02C39A", "#31405E"]),
        ("creative-monochrome-film", "Leica Silver Gelatin & Film", "photography cinematography visual-arts",
         ["#F5F5F3", "#EAEAE6", "#FFFFFF", "#121212", "#595956", "#121212", "#D9381E", "#D6D6D0"],
         ["#080808", "#111111", "#1A1A1A", "#F2F2F0", "#8C8C88", "#FFFFFF", "#FF4500", "#292929"]),
        ("creative-kinetic-pop", "Studio Memphis & Cobalt", "motion-design 3d-artist interactive-studio",
         ["#FAF8FF", "#FFFFFF", "#F0EBFF", "#120D24", "#544C70", "#2563EB", "#F43F5E", "#120D24"],
         ["#090712", "#130F24", "#1D1736", "#F8F6FF", "#9A90BD", "#38BDF8", "#FB7185", "#38BDF8"])
    ],
    "real-estate": [
        ("estate-travertine-villa", "Travertine Stone & Olive Sanctuary", "luxury-estate villa acreage architecture",
         ["#F7F5F0", "#EDEAE2", "#FFFFFF", "#1C1A17", "#69635A", "#8C6239", "#3B5E4C", "#D8D2C5"],
         ["#0C0B09", "#151310", "#201D18", "#F5F2EB", "#9E9589", "#C5A059", "#52826A", "#2E2A23"]),
        ("estate-manhattan-penthouse", "Penthouse Obsidian & Brass", "high-rise commercial luxury-condos",
         ["#F6F6F8", "#ECECEF", "#FFFFFF", "#111318", "#555963", "#1E293B", "#B45309", "#D8D9E0"],
         ["#08090C", "#101218", "#191C26", "#F4F5F7", "#8C92A3", "#D4AF37", "#60A5FA", "#252A38"]),
        ("estate-nordic-timber", "Nordic Birch & Fjord Slate", "sustainable-homes modular-cabins interior",
         ["#F9F8F5", "#F0EDE6", "#FFFFFF", "#1E2224", "#5F666A", "#2D5A6B", "#B86B43", "#DFDBD0"],
         ["#0E1112", "#161B1D", "#20272A", "#F2F5F6", "#8F9A9E", "#569BB5", "#D98A62", "#2D373B"]),
        ("estate-mediterranean-terracotta", "Amalfi Sun & Terracotta", "resort coastal holiday-rentals hospitality",
         ["#FDFBF7", "#F5EFE4", "#FFFFFF", "#241B16", "#6E5A4E", "#C85A32", "#0284C7", "#E6DBC8"],
         ["#120E0B", "#1C1612", "#281F1A", "#FAF5EE", "#A69183", "#E07A5F", "#38BDF8", "#382C25"]),
        ("estate-proptech-blueprint", "PropTech Valuation & Map", "marketplace mortgage appraisal zoning",
         ["#F4F7FA", "#FFFFFF", "#E8EEF5", "#0C1726", "#4B5E75", "#0284C7", "#059669", "#CEDBE8"],
         ["#060C14", "#0D1726", "#15243B", "#F0F6FC", "#7EA8CC", "#38BDF8", "#10B981", "#1F3657"])
    ],
    "gaming": [
        ("game-cyber-phosphor", "Night City Cyber Phosphor", "sci-fi cyberpunk esports fps hud",
         ["#ECEFF4", "#FFFFFF", "#DDE3ED", "#090D16", "#475266", "#FF0055", "#0066FF", "#090D16"],
         ["#05050A", "#0C0B16", "#151326", "#ECFEFF", "#7C759E", "#00F5D4", "#FF2A85", "#00F5D4"]),
        ("game-elden-mythos", "Tarnished Gold & Shadow Lore", "rpg dark-fantasy soulslike mythology",
         ["#F5F2EB", "#EAE4D7", "#FFFFFF", "#1A1612", "#635A4F", "#9E7B2F", "#8C1D1D", "#D6CCB8"],
         ["#080706", "#120F0D", "#1C1814", "#F2ECE1", "#9C8F7E", "#D4AF37", "#DC2626", "#302820"]),
        ("game-arcade-nectar", "16-Bit Shibuya Arcade Pop", "indie-game platformer retro party-game",
         ["#FFFDF7", "#FFFFFF", "#F3EFE2", "#120C1F", "#594E70", "#7C3AED", "#F59E0B", "#120C1F"],
         ["#0D0817", "#170F29", "#23173D", "#FAF5FF", "#A695C7", "#FACC15", "#EC4899", "#FACC15"]),
        ("game-tactical-ops", "Tactical Radar & Olive Telemetry", "battle-royale mil-sim strategy mech",
         ["#F2F4F0", "#E6E9E2", "#FFFFFF", "#141712", "#555C50", "#EA580C", "#3F6212", "#C9CFC2"],
         ["#0A0C09", "#131711", "#1C2219", "#EBF0E8", "#889481", "#FF5500", "#84CC16", "#2B3626"]),
        ("game-valor-mecha", "Mecha Chassis White & Crimson", "hero-shooter anime-action esports-tournament",
         ["#F5F6F8", "#FFFFFF", "#E6E8ED", "#0F141C", "#525B6B", "#FF334B", "#00B4D8", "#D0D5DE"],
         ["#090C12", "#121722", "#1B2333", "#F2F5FA", "#8592A8", "#FF4655", "#00F5D4", "#28344B"])
    ],
    "food-restaurant": [
        ("food-saffron-thali", "Royal Saffron & Brass Thali", "indian-cuisine vegetarian thali festive spice",
         ["#FDFBF7", "#F5EFE2", "#FFFFFF", "#241710", "#6E5647", "#D97706", "#15803D", "#E8DCC4"],
         ["#120B08", "#1C120D", "#291B14", "#FDF7EE", "#A88F7D", "#F59E0B", "#22C55E", "#3B281E"]),
        ("food-kyoto-matcha", "Uji Matcha & Black Sesame", "tea-house ramen japanese organic zen",
         ["#F7F6F0", "#EDEBE0", "#FFFFFF", "#1A211B", "#59665B", "#3B6E4C", "#C85A32", "#D8D5C5"],
         ["#0E120F", "#161C18", "#202923", "#F2F5F2", "#8FA392", "#52B788", "#E07A5F", "#2D3B31"]),
        ("food-artisanal-roastery", "Third-Wave Espresso & Crema", "coffee-house bakery cafe roastery",
         ["#FBF8F3", "#F2ECE1", "#FFFFFF", "#211813", "#6B584E", "#9C4A27", "#2A6F68", "#E3D8C6"],
         ["#110C0A", "#1B1410", "#261C17", "#F7F1E8", "#A38E82", "#E07A5F", "#52B788", "#362820"]),
        ("food-mediterranean-bistro", "Olive Grove & Heirloom Tomato", "farm-to-table bistro vegan pizzeria",
         ["#FCFBF7", "#F3EFE6", "#FFFFFF", "#1E2118", "#5F6653", "#C83E2B", "#4D7C0F", "#E2DCCB"],
         ["#10120C", "#191C14", "#24291D", "#F6F7F0", "#969E86", "#EF4444", "#84CC16", "#323828"]),
        ("food-neon-izakaya", "Midnight Street Food & Lantern", "night-market street-food delivery cloud-kitchen",
         ["#FFFDF8", "#FFF5E6", "#FFFFFF", "#1C1417", "#665259", "#E11D48", "#EAB308", "#F0DEC6"],
         ["#0E090C", "#181015", "#241820", "#FFF5F7", "#AD8E99", "#FF2A55", "#FACC15", "#382431"])
    ],
    "fitness": [
        ("fit-carbon-volt", "Carbon Track & High-Volt", "hiit crossfit gym performance-tracker",
         ["#F7F9F4", "#FFFFFF", "#EBF0E4", "#0E140A", "#4F5E46", "#65A30D", "#EA580C", "#D4E0C5"],
         ["#080B07", "#11160E", "#1A2216", "#F4FCE3", "#8CA67E", "#A3E635", "#FF5500", "#273321"]),
        ("fit-alpine-endurance", "Alpine Trail & Strava Orange", "running cycling marathon outdoor-gps",
         ["#F9F8F6", "#FFFFFF", "#EFECE6", "#171412", "#5E5650", "#FC4C02", "#0284C7", "#E0DAD0"],
         ["#0C0A09", "#161311", "#211C19", "#F7F5F2", "#9C9189", "#FF5714", "#38BDF8", "#302925"]),
        ("fit-pilates-sculpt", "Studio Sculpt & Warm Clay", "pilates yoga barre mobility recovery",
         ["#FAF7F2", "#F2ECE3", "#FFFFFF", "#241D18", "#6B5E54", "#B86B4B", "#4A6B5D", "#E3D9CA"],
         ["#13100D", "#1D1814", "#29221D", "#F7F2EC", "#A39387", "#D98A6C", "#6BA38B", "#362D26"]),
        ("fit-aqua-triathlon", "Hydro Velocity & Cobalt", "swimming triathlon hydration biometrics",
         ["#F2F8FC", "#FFFFFF", "#E3F0F9", "#081C29", "#466375", "#0284C7", "#10B981", "#C5DFF0"],
         ["#050E14", "#0B1B26", "#122A3B", "#F0F9FF", "#7AA8C4", "#38BDF8", "#34D399", "#1D4059"]),
        ("fit-combat-arena", "Octagon Crimson & Matte Steel", "boxing mma strength powerlifting",
         ["#F5F5F6", "#FFFFFF", "#E8E8EB", "#111114", "#54545C", "#DC2626", "#D97706", "#D4D4DA"],
         ["#09090B", "#131317", "#1D1D24", "#FAFAFA", "#8E8E99", "#EF4444", "#F59E0B", "#2C2C36"])
    ],
    "travel": [
        ("travel-bharat-nomad", "Grand Trunk Terracotta & Peacock", "india-travel transit train bus vlog heritage",
         ["#FDFBF7", "#F4EFE6", "#FFFFFF", "#241914", "#6E5A4F", "#C85A32", "#0F766E", "#E6DEC8"],
         ["#0E0A08", "#18120E", "#241B15", "#FAF5EE", "#A68E80", "#E07A5F", "#14B8A6", "#362820"]),
        ("travel-himalayan-expedition", "Alpine Glacier & Prayer Flag", "trekking mountains ladakh camping route",
         ["#F5F8FA", "#FFFFFF", "#E8EFF5", "#0D1B26", "#4B6070", "#0284C7", "#D97706", "#CFDCE8"],
         ["#070D14", "#0E1926", "#17273B", "#F0F7FC", "#809EB8", "#38BDF8", "#F59E0B", "#223A57"]),
        ("travel-kyoto-rail", "Shinkansen Slate & Stamp Red", "rail-pass metro ferry schedule timetable",
         ["#F8F7F4", "#EFECE6", "#FFFFFF", "#141619", "#545961", "#D92B2B", "#1D4ED8", "#DCD8CE"],
         ["#0B0C0E", "#13161A", "#1C2127", "#F5F4F0", "#8D949E", "#F43F5E", "#60A5FA", "#2A313B"]),
        ("travel-tropical-archipelago", "Andaman Lagoon & Teak", "islands southeast-asia ferry backpacking coastal",
         ["#F4F1E8", "#FFFFFF", "#E2F2EB", "#07221C", "#43665E", "#0D9488", "#EA580C", "#C4E3D8"],
         ["#040F0D", "#0A1C19", "#102B26", "#EFFCF6", "#73ADA2", "#2DD4BF", "#FB923C", "#193E37"]),
        ("travel-first-class-lounge", "Concorde Midnight & Champagne", "aviation hotel-booking luxury-concierge miles",
         ["#FAF9F6", "#F1EFEA", "#FFFFFF", "#12151E", "#565B6B", "#1E3A8A", "#B45309", "#DFDCD2"],
         ["#080A10", "#101420", "#181E30", "#F7F5F0", "#8C93A8", "#D4AF37", "#38BDF8", "#262F47"])
    ],
    "nft-web3": [
        ("web3-hologram-vault", "Zero-Knowledge Hologram & Void", "nft-marketplace collector art-blocks",
         ["#F8FAFF", "#FFFFFF", "#EDF1FF", "#0A0917", "#504E75", "#6366F1", "#EC4899", "#DCE3FF"],
         ["#05040D", "#0D0A1C", "#16112E", "#F5F3FF", "#9189BA", "#00F5D4", "#A855F7", "#281F52"]),
        ("web3-solana-ultraviolet", "High-TPS Ultraviolet & Mint", "solana depin token-launch ecosystem",
         ["#F6FBF9", "#FFFFFF", "#E8F7F2", "#0C141F", "#4C5E70", "#9333EA", "#10B981", "#CEEAE0"],
         ["#06080E", "#0D111C", "#151B2E", "#F2FBF9", "#8596B0", "#14F195", "#9945FF", "#222C47"]),
        ("web3-ordinal-amber", "Bitcoin Ordinal & Raw Block", "bitcoin inscriptions hash-rate node",
         ["#FBF9F5", "#F2EFE9", "#FFFFFF", "#141210", "#5E5850", "#EA580C", "#141210", "#E0DAD0"],
         ["#0A0908", "#14110E", "#1F1A16", "#FAF7F2", "#9C9085", "#F7931A", "#FACC15", "#332B24"]),
        ("web3-dao-governance", "Protocol Agora & Marble", "dao voting governance treasury public-goods",
         ["#F7F8FA", "#FFFFFF", "#EBEEF2", "#111622", "#525C70", "#2563EB", "#0D9488", "#D8DEE8"],
         ["#090C12", "#111622", "#1A2233", "#F2F5FA", "#8894AB", "#60A5FA", "#2DD4BF", "#29354D"]),
        ("web3-metaverse-prism", "Spatial Canvas & Hyper-Cyan", "spatial-web 3d-worlds virtual-fashion",
         ["#FAF7FF", "#FFFFFF", "#F2EAFF", "#160D29", "#5E4F7A", "#D946EF", "#06B6D4", "#E5D4FF"],
         ["#080512", "#120B24", "#1C1238", "#FDF4FF", "#A894C7", "#F0ABFC", "#22D3EE", "#332061"])
    ],
    "beauty-spa": [
        ("beauty-aesop-apothecary", "Apothecary Amber & Botanical", "skincare apothecary luxury-retail organic",
         ["#F6F4EE", "#EBE7DC", "#FCFBF8", "#211D18", "#665E54", "#8C583A", "#3B5E4C", "#DAD3C2"],
         ["#12100D", "#1C1814", "#26211C", "#F2EFE9", "#9E9488", "#C88A65", "#689F82", "#332C24"]),
        ("beauty-velvet-rose", "Parisian Rosewater & Silk", "cosmetics makeup fragrance editorial-beauty",
         ["#FDF9FA", "#F7EFEF", "#FFFFFF", "#241619", "#6E555B", "#BE185D", "#B45309", "#EADAD9"],
         ["#130B0D", "#1F1216", "#2B191F", "#FDF2F5", "#B08F98", "#F472B6", "#FBBF24", "#3D242C"]),
        ("beauty-onsen-mineral", "Onsen Hinoki & Thermal Stone", "spa massage thermal-bath wellness-retreat",
         ["#F5F6F4", "#EAECE8", "#FFFFFF", "#1A201C", "#5A665E", "#3F6E58", "#A16207", "#D6DBD2"],
         ["#0E1210", "#161C19", "#202924", "#F0F4F1", "#8FA195", "#68B08E", "#EAB308", "#2D3B33"]),
        ("beauty-clinical-derma", "Derma Peel & Hyaluronic Pure", "dermatology med-spa laser clean-beauty",
         ["#F7FAFC", "#FFFFFF", "#EDF3F7", "#0F1D26", "#516673", "#0284C7", "#0D9488", "#D7E4ED"],
         ["#070E14", "#0E1B24", "#162936", "#F0F8FF", "#82A3B5", "#38BDF8", "#2DD4BF", "#223E52"]),
        ("beauty-ayurveda-kumkum", "Ayurvedic Kumkumadi & Sandalwood", "ayurveda holistic-ritual herbal oils",
         ["#FCF9F2", "#F4EDE0", "#FFFFFF", "#261A12", "#6E5849", "#B45309", "#15803D", "#E5D8C2"],
         ["#130D09", "#1F150F", "#2B1E16", "#FAF3E8", "#A89180", "#F59E0B", "#4ADE80", "#3B291E"])
    ],
    "developer-tools": [
        ("dev-teenage-chassis", "Field Aluminium & International Orange", "hardware-tool calculator audio-synth utility",
         ["#E5E5E0", "#F2F2EE", "#FFFFFF", "#111110", "#595954", "#FF4F00", "#0055FF", "#111110"],
         ["#0E0E0D", "#171715", "#22221F", "#F2F2EE", "#8C8C84", "#FF5E1A", "#38BDF8", "#33332E"]),
        ("dev-warp-obsidian", "Rust Terminal & Amber Forge", "cli ide compiler debugger git-client",
         ["#F6F6F4", "#FFFFFF", "#EAEAE6", "#121214", "#55555C", "#D97706", "#2563EB", "#D8D8D2"],
         ["#09090B", "#111115", "#19191F", "#F4F4F6", "#8A8A96", "#F59E0B", "#38BDF8", "#25252E"]),
        ("dev-supabase-emerald", "Postgres Emerald & Carbon", "database backend-as-a-service api-docs",
         ["#F6FAF8", "#FFFFFF", "#E8F2EE", "#0A1712", "#486157", "#10B981", "#4F46E5", "#CEE3DA"],
         ["#060A08", "#0C1410", "#13211B", "#ECFDF5", "#76A895", "#34D399", "#818CF8", "#1C3329"]),
        ("dev-grafana-telemetry", "Observability Flame & Metric", "monitoring logs apm devops kubernetes",
         ["#F5F7FA", "#FFFFFF", "#E8ECF2", "#0D131C", "#4D596B", "#EA580C", "#0284C7", "#D2DAE6"],
         ["#070A0F", "#0E131C", "#161E2B", "#F0F4FA", "#8291A8", "#FF6B2B", "#38BDF8", "#232F42"]),
        ("dev-monokai-modern", "Modern Monokai & Matcha", "code-playground regex-tester json-formatter",
         ["#F8F7F2", "#EFECE4", "#FFFFFF", "#1C1B18", "#615E56", "#E11D48", "#65A30D", "#DDD8CA"],
         ["#10100E", "#191916", "#24241F", "#F8F8F2", "#99978B", "#FF2A85", "#A6E22E", "#33332C"])
    ],
    "entertainment": [
        ("ent-mythic-agni", "Mythic Agni & Sacred Bronze", "ramayana mythology epic-animation trailer-score",
         ["#FAF6F0", "#EFE9DF", "#FFFFFF", "#1C120D", "#6B564B", "#B45309", "#BE123C", "#DFD4C2"],
         ["#090605", "#130D0B", "#1F1512", "#F7EDE8", "#9E867B", "#D4AF37", "#E11D48", "#2E201B"]),
        ("ent-imax-premiere", "A24 Editorial & Cinema Noir", "film-studio streaming festival documentary",
         ["#F7F6F2", "#ECEAE3", "#FFFFFF", "#111111", "#575652", "#B91C1C", "#111111", "#D8D5CA"],
         ["#050505", "#0E0E0E", "#181818", "#F5F3EE", "#8C8A84", "#EF4444", "#F59E0B", "#262626"]),
        ("ent-webtoon-cel", "2.5D Manhwa Cel & Neon Ink", "webtoon manhwa anime-studio comics",
         ["#FAF8FF", "#FFFFFF", "#EFEBFF", "#120E21", "#554E70", "#6D28D9", "#F43F5E", "#120E21"],
         ["#080610", "#110D21", "#1B1533", "#FAF8FF", "#9B92BD", "#A855F7", "#FF2A85", "#2D2352"]),
        ("ent-symphony-hall", "Orchestral Mahogany & Brass", "music-production soundtrack classical-audio",
         ["#FAF7F2", "#F0EAE1", "#FFFFFF", "#1F1712", "#66574E", "#9A5B25", "#1E3A8A", "#DFD5C6"],
         ["#0C0907", "#16110D", "#211914", "#F5EFEA", "#9E8D82", "#E09F3E", "#60A5FA", "#33271F"]),
        ("ent-vinyl-hifi", "Hi-Fi Warm Tube & VU Meter", "podcast radio streaming-player dj-tool",
         ["#F4F2EC", "#E8E4DA", "#FFFFFF", "#171614", "#5C5953", "#EA580C", "#0D9488", "#D4CFC2"],
         ["#0D0C0B", "#161513", "#211F1C", "#F2EFE9", "#948F86", "#FF5500", "#14B8A6", "#2E2B27"])
    ],
    "legal": [
        ("legal-chambers-mahogany", "Lincoln's Inn Mahogany & Parchment", "law-firm litigation corporate-governance",
         ["#F9F8F5", "#F0EDE6", "#FFFFFF", "#111827", "#4B5563", "#1E3A8A", "#92400E", "#D6D2C8"],
         ["#080B12", "#101624", "#182136", "#F8FAFC", "#94A3B8", "#D4AF37", "#60A5FA", "#26334D"]),
        ("legal-patent-ip", "Intellectual Property Blueprint", "patent trademark legaltech ai-contract",
         ["#F4F7FA", "#FFFFFF", "#E8EEF5", "#0C1624", "#495A70", "#0369A1", "#0F766E", "#CFDCEB"],
         ["#060B12", "#0C1522", "#132136", "#F0F6FC", "#7FA0C2", "#38BDF8", "#2DD4BF", "#1E3352"]),
        ("legal-notary-seal", "Supreme Wax Seal & Oxford", "constitutional-law arbitration compliance",
         ["#FCFBF9", "#F3F0EA", "#FFFFFF", "#171717", "#575551", "#991B1B", "#1E3A8A", "#DFDBD2"],
         ["#0B0B0C", "#141417", "#1F1F24", "#F7F6F2", "#96948E", "#EF4444", "#D4AF37", "#2E2E36"]),
        ("legal-civic-policy", "Public Policy & Diplomatic Slate", "think-tank ngo regulation government",
         ["#F6F7F8", "#ECEEF0", "#FFFFFF", "#121A21", "#515E69", "#0F766E", "#B45309", "#D5DBE0"],
         ["#090D10", "#11181F", "#19242E", "#F2F5F7", "#8797A3", "#2DD4BF", "#F59E0B", "#263645"]),
        ("legal-private-notary", "Private Family Office & Olive", "estate-planning wealth-trust tax-law",
         ["#F8F7F3", "#EFECE4", "#FFFFFF", "#1A211C", "#57635A", "#2D5A43", "#8C6239", "#DBD6C8"],
         ["#0C100D", "#141C17", "#1D2921", "#F2F5F3", "#8CA192", "#52B788", "#C5A059", "#29382E"])
    ],
    "events": [
        ("event-bachelor-arcade", "Afterhours Neon & Velvet Dare", "bachelor-party party-game social-dares riddle",
         ["#FFFDF5", "#FFFFFF", "#F4EFE0", "#0A0A0A", "#4B5563", "#A3E635", "#8B5CF6", "#0A0A0A"],
         ["#0B0614", "#150D26", "#21153B", "#FAF5FF", "#A78BFA", "#FACC15", "#FF2A85", "#FACC15"]),
        ("event-arena-festival", "Mainstage Laser & Wristband", "music-festival concert ticketing lineup",
         ["#FAF8FF", "#FFFFFF", "#F0EBFF", "#120A1F", "#574B6E", "#FF0055", "#6366F1", "#120A1F"],
         ["#07040C", "#11091C", "#1B0F2E", "#FDF4FF", "#A892C4", "#00F5D4", "#FF0055", "#321C54"]),
        ("event-royal-utsav", "Royal Mandap Marigold & Sindoor", "wedding cultural-festival celebration rsvp",
         ["#FFFBF5", "#F7EFE2", "#FFFFFF", "#291410", "#70514A", "#C83E2B", "#D97706", "#EBD8C0"],
         ["#140907", "#21100C", "#301712", "#FFF7ED", "#B58E84", "#F59E0B", "#F43F5E", "#45231B"]),
        ("event-tech-summit", "Keynote Stage & Badge Pass", "developer-conference hackathon summit expo",
         ["#F5F7FA", "#FFFFFF", "#E8ECF2", "#0B111E", "#4A5568", "#2563EB", "#10B981", "#D2DAE6"],
         ["#060911", "#0D1322", "#151F36", "#F8FAFC", "#8A99B5", "#38BDF8", "#A3E635", "#243457"]),
        ("event-gala-champagne", "Black Tie Velvet & Gold", "awards-show charity-gala VIP-invite",
         ["#FAF9F6", "#F2EFE9", "#FFFFFF", "#141311", "#5E5B55", "#9A7B3E", "#141311", "#E0DBD0"],
         ["#080807", "#12110F", "#1C1A17", "#F7F5F0", "#999388", "#D4AF37", "#F43F5E", "#2E2A24"])
    ],
    "other": [
        ("other-bento-neutral", "Universal Bento Studio", "personal-hub multi-tool dashboard all-purpose",
         ["#FAFAFA", "#FFFFFF", "#F2F2F3", "#09090B", "#52525B", "#18181B", "#2563EB", "#E4E4E7"],
         ["#09090B", "#121215", "#1C1C21", "#FAFAFA", "#A1A1AA", "#FAFAFA", "#38BDF8", "#27272A"]),
        ("other-warm-craft", "Artisanal Paper & Ink", "notes wiki second-brain PKM",
         ["#FBF9F5", "#F2EFE9", "#FFFFFF", "#1C1A17", "#635E56", "#C85A32", "#2D6A4F", "#E2DDD2"],
         ["#11100E", "#1A1815", "#24211D", "#F5F2EB", "#999288", "#E07A5F", "#52B788", "#302C26"]),
        ("other-blueprint-cad", "Engineering CAD Blueprint", "architecture calculator converter physics",
         ["#F2F6FA", "#FFFFFF", "#E4ECF5", "#091829", "#465E78", "#0284C7", "#EA580C", "#C5D7EB"],
         ["#050E1A", "#0A192E", "#102645", "#EBF5FF", "#7AA6D1", "#38BDF8", "#F97316", "#1B3B66"]),
        ("other-nordic-calm", "Scandinavian Slate & Pine", "habit-tracker weather minimalist-utility",
         ["#F6F7F5", "#ECEEE9", "#FFFFFF", "#181E1A", "#566159", "#2F5E4E", "#D97706", "#D6DDD8"],
         ["#0D110F", "#151C18", "#1F2923", "#F0F4F1", "#8BA193", "#52B788", "#FBBF24", "#2A3830"]),
        ("other-kinetic-mono", "High-Contrast Kinetic Mono", "experimental brutalist-tool portfolio",
         ["#FFFFFF", "#F0F0F0", "#FFFFFF", "#000000", "#4A4A4A", "#000000", "#FF3E00", "#000000"],
         ["#000000", "#111111", "#1F1F1F", "#FFFFFF", "#999999", "#FFFFFF", "#CCFF00", "#FFFFFF"])
    ]
}

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def rel_luminance(rgb):
    def adjust(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = [adjust(c) for c in rgb]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast_ratio(hex1, hex2):
    l1 = rel_luminance(hex_to_rgb(hex1))
    l2 = rel_luminance(hex_to_rgb(hex2))
    lum1, lum2 = max(l1, l2), min(l1, l2)
    return round((lum1 + 0.05) / (lum2 + 0.05), 2)

def audit_palette_contrast(bg, surface, text, muted, accent, border):
    c_text_canvas = contrast_ratio(text, bg)
    c_text_surface = contrast_ratio(text, surface)
    c_muted_surface = contrast_ratio(muted, surface)
    c_accent_surface = contrast_ratio(accent, surface)
    c_border_surface = contrast_ratio(border, surface)
    rating = "AAA Pass" if c_text_surface >= 7.0 and c_muted_surface >= 3.0 else ("AA Pass" if c_text_surface >= 4.5 else "Fail")
    return {
        "text_on_canvas": c_text_canvas,
        "text_on_surface": c_text_surface,
        "muted_on_surface": c_muted_surface,
        "accent_on_surface": c_accent_surface,
        "border_on_surface": c_border_surface,
        "rating": rating
    }

def get_chart_palette(accent, secondary, mode):
    if mode == "light":
        return [accent, secondary, "#F59E0B", "#10B981", "#6366F1"]
    else:
        return [accent, secondary, "#FBBF24", "#34D399", "#818CF8"]

def build_200_palettes():
    palettes = []
    idx = 1
    for cat_key, families in RAW_FAMILIES.items():
        for fam_id, fam_name, vibes, L, D in families:
            for mode, arr in [("light", L), ("dark", D)]:
                audit = audit_palette_contrast(arr[0], arr[1], arr[3], arr[4], arr[5], arr[7])
                charts = get_chart_palette(arr[5], arr[6], mode)
                palettes.append({
                    "index": idx,
                    "id": f"{fam_id}-{mode}",
                    "family_id": fam_id,
                    "category": cat_key,
                    "name": f"{fam_name} ({mode.capitalize()})",
                    "mode": mode,
                    "vibes": vibes,
                    "bg": arr[0],
                    "surface": arr[1],
                    "elevated": arr[2],
                    "text": arr[3],
                    "muted": arr[4],
                    "accent": arr[5],
                    "secondary": arr[6],
                    "border": arr[7],
                    "chart_1": charts[0],
                    "chart_2": charts[1],
                    "chart_3": charts[2],
                    "chart_4": charts[3],
                    "chart_5": charts[4],
                    "contrast_text": audit["text_on_surface"],
                    "contrast_muted": audit["muted_on_surface"],
                    "wcag_rating": audit["rating"]
                })
                idx += 1
    return palettes

ALL_200_PALETTES = build_200_palettes()

def export_catalog(out_dir="."):
    os.makedirs(out_dir, exist_ok=True)
    json_path = os.path.join(out_dir, "palettes_200.json")
    csv_path = os.path.join(out_dir, "palettes_200.csv")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(ALL_200_PALETTES, f, indent=2)
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(ALL_200_PALETTES[0].keys()))
        writer.writeheader()
        writer.writerows(ALL_200_PALETTES)
    print(f"[OK] Exported {len(ALL_200_PALETTES)} standalone palettes to {json_path}")

def search_palettes(query="", category=None, mode=None, limit=5):
    pool = ALL_200_PALETTES
    if category and category != "all":
        pool = [p for p in pool if p["category"] == category.lower()]
    if mode and mode in ("light", "dark"):
        pool = [p for p in pool if p["mode"] == mode]
    if not query:
        return pool[:limit]
    tokens = re.findall(r"[a-z0-9]+", query.lower())
    def score(p):
        hay = f"{p['id']} {p['name']} {p['category']} {p['vibes']}".lower()
        return sum(3 if t in hay.split() else (1 if t in hay else 0) for t in tokens)
    return sorted(pool, key=score, reverse=True)[:limit]

CATEGORY_TYPOGRAPHY = {
    "saas": {"display": "'Space Grotesk', sans-serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "ai-chatbot": {"display": "'Space Grotesk', sans-serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "developer-tools": {"display": "'JetBrains Mono', monospace", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "education": {"display": "'Fraunces', serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "e-commerce": {"display": "'Fraunces', serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "fintech-crypto": {"display": "'Space Grotesk', sans-serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "healthcare": {"display": "'Plus Jakarta Sans', sans-serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "creative": {"display": "'Syne', sans-serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "real-estate": {"display": "'Fraunces', serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "gaming": {"display": "'Space Grotesk', sans-serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "food-restaurant": {"display": "'Fraunces', serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "fitness": {"display": "'Space Grotesk', sans-serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "travel": {"display": "'Fraunces', serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "nft-web3": {"display": "'Space Grotesk', sans-serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "beauty-spa": {"display": "'Fraunces', serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "entertainment": {"display": "'Space Grotesk', sans-serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "legal": {"display": "'Fraunces', serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "events": {"display": "'Space Grotesk', sans-serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "pet-services": {"display": "'Plus Jakarta Sans', sans-serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"},
    "other": {"display": "'Space Grotesk', sans-serif", "sans": "'Plus Jakarta Sans', sans-serif", "mono": "'JetBrains Mono', monospace"}
}

def compile_css_pair(light_p, dark_p):
    cat = light_p.get('category', 'other')
    typo = CATEGORY_TYPOGRAPHY.get(cat, CATEGORY_TYPOGRAPHY['other'])
    pri_fg_light = "#FFFFFF" if contrast_ratio(light_p['accent'], "#FFFFFF") >= contrast_ratio(light_p['accent'], "#0B0F19") else "#0B0F19"
    pri_fg_dark  = "#FFFFFF" if contrast_ratio(dark_p['accent'], "#FFFFFF") >= contrast_ratio(dark_p['accent'], "#08090C") else "#08090C"

    return f"""/* ==========================================================================
   UI-UX-ULTRA v3.5 — 200-PALETTE ENGINE WITH DYNAMIC CONTRAST & RIM-LIGHTING
   Family: {light_p['family_id']} | Category: {light_p['category']}
   ========================================================================== */
:root, [data-theme="light"] {{
  --bg-canvas: {light_p['bg']};
  --bg-surface: {light_p['surface']};
  --bg-elevated: {light_p['elevated']};
  --text-primary: {light_p['text']};
  --text-muted: {light_p['muted']};
  --accent-primary: {light_p['accent']};
  --accent-foreground: {pri_fg_light};
  --accent-secondary: {light_p['secondary']};
  --elevated-foreground: {light_p['text']};
  --border-color: {light_p['border']};

  /* Chart & Data Visualization Series */
  --chart-1: {light_p['chart_1']};
  --chart-2: {light_p['chart_2']};
  --chart-3: {light_p['chart_3']};
  --chart-4: {light_p['chart_4']};
  --chart-5: {light_p['chart_5']};

  /* Typography scale */
  --font-display: {typo['display']};
  --font-sans: {typo['sans']};
  --font-mono: {typo['mono']};

  /* UI Accents & Radii */
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-card: 14px;

  /* Elevation Shadows */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
  --shadow-rim: inset 0 1px 0 0 rgba(255, 255, 255, 0.6);
  --shadow-glow: 0 0 24px -4px {light_p['accent']};
}}

[data-theme="dark"] {{
  --bg-canvas: {dark_p['bg']};
  --bg-surface: {dark_p['surface']};
  --bg-elevated: {dark_p['elevated']};
  --text-primary: {dark_p['text']};
  --text-muted: {dark_p['muted']};
  --accent-primary: {dark_p['accent']};
  --accent-foreground: {pri_fg_dark};
  --accent-secondary: {dark_p['secondary']};
  --elevated-foreground: {dark_p['text']};
  --border-color: {dark_p['border']};

  /* Chart & Data Visualization Series */
  --chart-1: {dark_p['chart_1']};
  --chart-2: {dark_p['chart_2']};
  --chart-3: {dark_p['chart_3']};
  --chart-4: {dark_p['chart_4']};
  --chart-5: {dark_p['chart_5']};

  /* Typography scale */
  --font-display: {typo['display']};
  --font-sans: {typo['sans']};
  --font-mono: {typo['mono']};

  /* UI Accents & Radii */
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-card: 14px;

  /* Elevation Shadows & Rim-Lighting (Apple/Linear Dark Polish) */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.5);
  --shadow-md: 0 4px 12px 0 rgba(0, 0, 0, 0.6);
  --shadow-lg: 0 12px 24px -4px rgba(0, 0, 0, 0.75);
  --shadow-rim: inset 0 1px 0 0 rgba(255, 255, 255, 0.09);
  --shadow-glow: 0 0 28px -4px {dark_p['accent']};
}}
"""

def compile_shadcn_css(light_p, dark_p):
    pri_fg_light = "#FFFFFF" if contrast_ratio(light_p['accent'], "#FFFFFF") >= contrast_ratio(light_p['accent'], "#0B0F19") else "#0B0F19"
    pri_fg_dark  = "#FFFFFF" if contrast_ratio(dark_p['accent'], "#FFFFFF") >= contrast_ratio(dark_p['accent'], "#08090C") else "#08090C"
    
    return f"""@tailwind base;
@tailwind components;
@tailwind utilities;

/* ==========================================================================
   UI-UX-ULTRA v3.5 — SHADCN UI COMPATIBLE GLOBALS.CSS
   Family: {light_p['family_id']}
   ========================================================================== */

@layer base {{
  :root {{
    --background: {light_p['bg']};
    --foreground: {light_p['text']};
    --card: {light_p['surface']};
    --card-foreground: {light_p['text']};
    --popover: {light_p['surface']};
    --popover-foreground: {light_p['text']};
    --primary: {light_p['accent']};
    --primary-foreground: {pri_fg_light};
    --secondary: {light_p['elevated']};
    --secondary-foreground: {light_p['text']};
    --muted: {light_p['elevated']};
    --muted-foreground: {light_p['muted']};
    --accent: {light_p['elevated']};
    --accent-foreground: {light_p['text']};
    --destructive: #DC2626;
    --destructive-foreground: #FFFFFF;
    --border: {light_p['border']};
    --input: {light_p['border']};
    --ring: {light_p['accent']};
    --radius: 0.625rem;
    --chart-1: {light_p['chart_1']};
    --chart-2: {light_p['chart_2']};
    --chart-3: {light_p['chart_3']};
    --chart-4: {light_p['chart_4']};
    --chart-5: {light_p['chart_5']};
  }}

  .dark, [data-theme="dark"] {{
    --background: {dark_p['bg']};
    --foreground: {dark_p['text']};
    --card: {dark_p['surface']};
    --card-foreground: {dark_p['text']};
    --popover: {dark_p['surface']};
    --popover-foreground: {dark_p['text']};
    --primary: {dark_p['accent']};
    --primary-foreground: {pri_fg_dark};
    --secondary: {dark_p['elevated']};
    --secondary-foreground: {dark_p['text']};
    --muted: {dark_p['elevated']};
    --muted-foreground: {dark_p['muted']};
    --accent: {dark_p['elevated']};
    --accent-foreground: {dark_p['text']};
    --destructive: #EF4444;
    --destructive-foreground: #FFFFFF;
    --border: {dark_p['border']};
    --input: {dark_p['border']};
    --ring: {dark_p['accent']};
    --chart-1: {dark_p['chart_1']};
    --chart-2: {dark_p['chart_2']};
    --chart-3: {dark_p['chart_3']};
    --chart-4: {dark_p['chart_4']};
    --chart-5: {dark_p['chart_5']};
  }}
}}
"""

def compile_tailwind_v4_css(light_p, dark_p):
    return """@import "tailwindcss";

@theme {
  --color-canvas: var(--bg-canvas);
  --color-surface: var(--bg-surface);
  --color-elevated: var(--bg-elevated);
  --color-primary: var(--text-primary);
  --color-muted: var(--text-muted);
  --color-accent: var(--accent-primary);
  --color-accent-secondary: var(--accent-secondary);
  --color-border: var(--border-color);

  --color-chart-1: var(--chart-1);
  --color-chart-2: var(--chart-2);
  --color-chart-3: var(--chart-3);
  --color-chart-4: var(--chart-4);
  --color-chart-5: var(--chart-5);

  --font-display: var(--font-display);
  --font-sans: var(--font-sans);
  --font-mono: var(--font-mono);

  --radius-card: var(--radius-card);
  --shadow-rim: var(--shadow-rim);
  --shadow-glow: var(--shadow-glow);
}
"""

def compile_motion_tokens():
    return """// UI/UX Ultra v3.5 — Spring & Motion Intelligence Tokens
export const motionTokens = {
  // Easing Curves (Cubic Bezier)
  ease: {
    snappy: [0.16, 1, 0.3, 1],    // Buttons, toggles, micro-interactions (Apple standard)
    gentle: [0.32, 0.72, 0, 1],   // Modal sheets, navigation drawers, card flips
    bounce: [0.34, 1.56, 0.64, 1], // Notification pills, toast alerts, success badges
  },
  // Durations (Seconds)
  duration: {
    instant: 0.1,
    fast: 0.2,
    normal: 0.35,
    slow: 0.5,
  },
  // Framer Motion Preset Variants
  framer: {
    fadeInUp: {
      initial: { opacity: 0, y: 16 },
      animate: { opacity: 1, y: 0, transition: { duration: 0.35, ease: [0.16, 1, 0.3, 1] } },
      exit: { opacity: 0, y: 12, transition: { duration: 0.2 } }
    },
    scaleIn: {
      initial: { opacity: 0, scale: 0.95 },
      animate: { opacity: 1, scale: 1, transition: { duration: 0.25, ease: [0.16, 1, 0.3, 1] } },
      exit: { opacity: 0, scale: 0.95, transition: { duration: 0.15 } }
    },
    staggerContainer: {
      animate: { transition: { staggerChildren: 0.08 } }
    }
  }
};
"""

def compile_tailwind_config():
    return """// Tailwind CSS Tokens Configuration
// Merge this into your tailwind.config.js `theme.extend` block:
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
          secondary: 'var(--accent-secondary)'
        },
        border: 'var(--border-color)',
        chart: {
          1: 'var(--chart-1)',
          2: 'var(--chart-2)',
          3: 'var(--chart-3)',
          4: 'var(--chart-4)',
          5: 'var(--chart-5)'
        }
      },
      fontFamily: {
        display: ['var(--font-display)'],
        sans: ['var(--font-sans)'],
        mono: ['var(--font-mono)']
      },
      borderRadius: {
        card: 'var(--radius-card)'
      },
      boxShadow: {
        rim: 'var(--shadow-rim)',
        glow: 'var(--shadow-glow)'
      }
    }
  }
};
"""

def compile_flutter_theme(light_p, dark_p):
    pri_fg_light = "#FFFFFF" if contrast_ratio(light_p['accent'], "#FFFFFF") >= contrast_ratio(light_p['accent'], "#0B0F19") else "#0B0F19"
    pri_fg_dark  = "#FFFFFF" if contrast_ratio(dark_p['accent'], "#FFFFFF") >= contrast_ratio(dark_p['accent'], "#08090C") else "#08090C"

    return f"""// UI/UX Ultra v3.5 — Flutter Material 3 & Cupertino Theme
// Family: {light_p['family_id']} | Category: {light_p['category']}
import 'package:flutter/material.dart';

class AppTheme {{
  // ─── Light ColorScheme ──────────────────────────────────────────
  static final ColorScheme lightColorScheme = ColorScheme(
    brightness: Brightness.light,
    primary: const Color(0xFF{light_p['accent'].replace('#', '')}),
    onPrimary: const Color(0xFF{pri_fg_light.replace('#', '')}),
    secondary: const Color(0xFF{light_p['secondary'].replace('#', '')}),
    onSecondary: const Color(0xFFFFFFFF),
    surface: const Color(0xFF{light_p['surface'].replace('#', '')}),
    onSurface: const Color(0xFF{light_p['text'].replace('#', '')}),
    surfaceVariant: const Color(0xFF{light_p['elevated'].replace('#', '')}),
    onSurfaceVariant: const Color(0xFF{light_p['muted'].replace('#', '')}),
    background: const Color(0xFF{light_p['bg'].replace('#', '')}),
    onBackground: const Color(0xFF{light_p['text'].replace('#', '')}),
    error: const Color(0xFFDC2626),
    onError: const Color(0xFFFFFFFF),
    outline: const Color(0xFF{light_p['border'].replace('#', '')}),
  );

  // ─── Dark ColorScheme ───────────────────────────────────────────
  static final ColorScheme darkColorScheme = ColorScheme(
    brightness: Brightness.dark,
    primary: const Color(0xFF{dark_p['accent'].replace('#', '')}),
    onPrimary: const Color(0xFF{pri_fg_dark.replace('#', '')}),
    secondary: const Color(0xFF{dark_p['secondary'].replace('#', '')}),
    onSecondary: const Color(0xFFFFFFFF),
    surface: const Color(0xFF{dark_p['surface'].replace('#', '')}),
    onSurface: const Color(0xFF{dark_p['text'].replace('#', '')}),
    surfaceVariant: const Color(0xFF{dark_p['elevated'].replace('#', '')}),
    onSurfaceVariant: const Color(0xFF{dark_p['muted'].replace('#', '')}),
    background: const Color(0xFF{dark_p['bg'].replace('#', '')}),
    onBackground: const Color(0xFF{dark_p['text'].replace('#', '')}),
    error: const Color(0xFFEF4444),
    onError: const Color(0xFFFFFFFF),
    outline: const Color(0xFF{dark_p['border'].replace('#', '')}),
  );

  // ─── ThemeData Builders ─────────────────────────────────────────
  static ThemeData get lightTheme => ThemeData(
    useMaterial3: true,
    colorScheme: lightColorScheme,
    scaffoldBackgroundColor: const Color(0xFF{light_p['bg'].replace('#', '')}),
    cardTheme: CardTheme(
      color: const Color(0xFF{light_p['surface'].replace('#', '')}),
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(14),
        side: const BorderSide(color: Color(0xFF{light_p['border'].replace('#', '')})),
      ),
    ),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: const Color(0xFF{light_p['accent'].replace('#', '')}),
        foregroundColor: const Color(0xFF{pri_fg_light.replace('#', '')}),
        minimumSize: const Size(88, 44), // Fitts's Law 44pt touch target
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
      ),
    ),
  );

  static ThemeData get darkTheme => ThemeData(
    useMaterial3: true,
    colorScheme: darkColorScheme,
    scaffoldBackgroundColor: const Color(0xFF{dark_p['bg'].replace('#', '')}),
    cardTheme: CardTheme(
      color: const Color(0xFF{dark_p['surface'].replace('#', '')}),
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(14),
        side: const BorderSide(color: Color(0xFF{dark_p['border'].replace('#', '')})),
      ),
    ),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: const Color(0xFF{dark_p['accent'].replace('#', '')}),
        foregroundColor: const Color(0xFF{pri_fg_dark.replace('#', '')}),
        minimumSize: const Size(88, 44), // Fitts's Law 44pt touch target
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
      ),
    ),
  );
}}
"""

def compile_swiftui_theme(light_p, dark_p):
    return f"""// UI/UX Ultra v3.5 — SwiftUI Multi-Platform Theme
// Family: {light_p['family_id']} | Category: {light_p['category']}
import SwiftUI

public struct AppTheme {{
  public struct Light {{
    public static let canvas = Color(hex: "{light_p['bg']}")
    public static let surface = Color(hex: "{light_p['surface']}")
    public static let elevated = Color(hex: "{light_p['elevated']}")
    public static let textPrimary = Color(hex: "{light_p['text']}")
    public static let textMuted = Color(hex: "{light_p['muted']}")
    public static let accent = Color(hex: "{light_p['accent']}")
    public static let secondary = Color(hex: "{light_p['secondary']}")
    public static let border = Color(hex: "{light_p['border']}")
  }}

  public struct Dark {{
    public static let canvas = Color(hex: "{dark_p['bg']}")
    public static let surface = Color(hex: "{dark_p['surface']}")
    public static let elevated = Color(hex: "{dark_p['elevated']}")
    public static let textPrimary = Color(hex: "{dark_p['text']}")
    public static let textMuted = Color(hex: "{dark_p['muted']}")
    public static let accent = Color(hex: "{dark_p['accent']}")
    public static let secondary = Color(hex: "{dark_p['secondary']}")
    public static let border = Color(hex: "{dark_p['border']}")
  }}

  // iOS Human Interface Guidelines (HIG) Touch & Spring Constants
  public static let minTouchTarget: CGFloat = 44.0 // Fitts's Law
  public static let cornerRadiusCard: CGFloat = 14.0
  public static let snappySpring = Animation.spring(response: 0.35, dampingFraction: 0.8)
  public static let bounceSpring = Animation.spring(response: 0.45, dampingFraction: 0.65)
}}

public extension Color {{
  init(hex: String) {{
    let cleanHex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
    var int: UInt64 = 0
    Scanner(string: cleanHex).scanHexInt64(&int)
    let a, r, g, b: UInt64
    switch cleanHex.count {{
    case 6:
      (a, r, g, b) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
    case 8:
      (a, r, g, b) = (int >> 24, int >> 16 & 0xFF, int >> 8 & 0xFF, int & 0xFF)
    default:
      (a, r, g, b) = (255, 0, 0, 0)
    }}
    self.init(
      .sRGB,
      red: Double(r) / 255,
      green: Double(g) / 255,
      blue:  Double(b) / 255,
      opacity: Double(a) / 255
    )
  }}
}}
"""

def compile_theme_toggle_js():
    return """// Zero-flash dual-theme switcher (light / dark)
(function() {
  const STORAGE_KEY = 'theme-preference';
  function getPreference() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) return stored;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  function setPreference(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem(STORAGE_KEY, theme);
  }
  window.toggleTheme = function() {
    const current = document.documentElement.getAttribute('data-theme') || getPreference();
    const next = current === 'dark' ? 'light' : 'dark';
    setPreference(next);
    return next;
  };
  setPreference(getPreference());
})();
"""

def compile_master_doc(light_p, dark_p, project_name="Project-Ultra"):
    cat = light_p.get('category', 'other')
    typo = CATEGORY_TYPOGRAPHY.get(cat, CATEGORY_TYPOGRAPHY['other'])
    return f"""# Design System: {project_name}

> Curated Family: **{light_p['name'].replace(' (Light)', '')}**  
> Category: **{cat.upper()}**  
> Vibes: `{light_p['vibes']}`  
> Accessibility: **{light_p.get('wcag_rating', 'AA Pass')} (Light)** / **{dark_p.get('wcag_rating', 'AA Pass')} (Dark)**

---

## 1. Dual Palette Specifications

| Role | Light Token | Light Hex | Dark Token | Dark Hex |
| :--- | :--- | :--- | :--- | :--- |
| **Canvas Background** | `--bg-canvas` | `{light_p['bg']}` | `--bg-canvas` | `{dark_p['bg']}` |
| **Surface (Cards/Panels)** | `--bg-surface` | `{light_p['surface']}` | `--bg-surface` | `{dark_p['surface']}` |
| **Elevated (Dropdowns/Badges)** | `--bg-elevated` | `{light_p['elevated']}` | `--bg-elevated` | `{dark_p['elevated']}` |
| **Primary Text** | `--text-primary` | `{light_p['text']}` | `--text-primary` | `{dark_p['text']}` |
| **Muted Text / Secondary** | `--text-muted` | `{light_p['muted']}` | `--text-muted` | `{dark_p['muted']}` |
| **Primary Accent** | `--accent-primary` | `{light_p['accent']}` | `--accent-primary` | `{dark_p['accent']}` |
| **Secondary Accent** | `--accent-secondary` | `{light_p['secondary']}` | `--accent-secondary` | `{dark_p['secondary']}` |
| **Subtle Border** | `--border-color` | `{light_p['border']}` | `--border-color` | `{dark_p['border']}` |

### Data Visualization Series
- **Series 1:** `{light_p['chart_1']}` (Light) / `{dark_p['chart_1']}` (Dark)
- **Series 2:** `{light_p['chart_2']}` (Light) / `{dark_p['chart_2']}` (Dark)
- **Series 3:** `{light_p['chart_3']}` (Light) / `{dark_p['chart_3']}` (Dark)
- **Series 4:** `{light_p['chart_4']}` (Light) / `{dark_p['chart_4']}` (Dark)
- **Series 5:** `{light_p['chart_5']}` (Light) / `{dark_p['chart_5']}` (Dark)

---

## 2. Typography Recommendations
- **Display / Headers:** {typo['display']}
- **Body / Interface:** {typo['sans']}
- **Code / Metrics / Monospace:** {typo['mono']}

---

## 3. WCAG 2.1 Contrast Telemetry
- **Light Theme Contrast (Text / Surface):** {light_p.get('contrast_text', 'N/A')}:1 ({light_p.get('wcag_rating', 'AA')})
- **Dark Theme Contrast (Text / Surface):** {dark_p.get('contrast_text', 'N/A')}:1 ({dark_p.get('wcag_rating', 'AA')})

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
"""

def generate_preview_svg(rec_light, rec_dark, alts):
    p = rec_dark
    alt1 = alts[0] if len(alts) > 0 else None
    alt2 = alts[1] if len(alts) > 1 else None

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 250" width="100%" style="border-radius:14px; background:{p['bg']}; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
  <!-- Recommended Main Card -->
  <g transform="translate(20, 20)">
    <rect width="380" height="210" rx="14" fill="{p['surface']}" stroke="{p['border']}" stroke-width="1"/>
    <rect x="1" y="1" width="378" height="1" fill="rgba(255,255,255,0.12)"/>
    <rect x="24" y="22" width="120" height="22" rx="5" fill="{p['accent']}22" stroke="{p['accent']}" stroke-width="1"/>
    <text x="32" y="37" fill="{p['accent']}" font-size="10" font-weight="700" letter-spacing="0.05em">RECOMMENDED</text>
    <text x="24" y="72" fill="{p['text']}" font-size="18" font-weight="700">{p['name'].replace(' (Dark)', '')}</text>
    <text x="24" y="94" fill="{p['muted']}" font-size="12">{p['vibes'][:44]}</text>
    
    <!-- Primary CTA -->
    <rect x="24" y="116" width="125" height="36" rx="8" fill="{p['accent']}"/>
    <text x="48" y="139" fill="#ffffff" font-size="12" font-weight="600">Primary Action</text>
    
    <!-- Secondary Button -->
    <rect x="160" y="116" width="110" height="36" rx="8" fill="{p['elevated']}" stroke="{p['border']}" stroke-width="1"/>
    <text x="182" y="139" fill="{p['text']}" font-size="12">Secondary</text>

    <!-- Contrast Pill -->
    <circle cx="30" cy="180" r="4" fill="#10B981"/>
    <text x="40" y="183" fill="{p['muted']}" font-size="11">WCAG {p.get('wcag_rating', 'AAA')} ({p.get('contrast_text', '18.4')}:1 Contrast)</text>
  </g>

  <!-- Alternatives Column -->
  <g transform="translate(420, 20)">
    <text x="0" y="14" fill="{p['muted']}" font-size="12" font-weight="600" letter-spacing="0.04em">OR SWITCH TO AN ALTERNATIVE:</text>
"""
    if alt1:
        svg += f"""    <!-- Alternative 1 -->
    <g transform="translate(0, 26)">
      <rect width="320" height="78" rx="10" fill="{p['surface']}" stroke="{p['border']}" stroke-width="1"/>
      <circle cx="22" cy="28" r="7" fill="{alt1['dark_accent']}"/>
      <text x="38" y="32" fill="{p['text']}" font-size="13" font-weight="600">{alt1['name']}</text>
      <text x="38" y="50" fill="{p['muted']}" font-size="11">{alt1['vibes'][:38]}...</text>
      <rect x="235" y="24" width="70" height="28" rx="6" fill="{alt1['dark_accent']}"/>
      <text x="249" y="42" fill="#ffffff" font-size="11" font-weight="600">Select</text>
    </g>
"""
    if alt2:
        svg += f"""    <!-- Alternative 2 -->
    <g transform="translate(0, 118)">
      <rect width="320" height="78" rx="10" fill="{p['surface']}" stroke="{p['border']}" stroke-width="1"/>
      <circle cx="22" cy="28" r="7" fill="{alt2['dark_accent']}"/>
      <text x="38" y="32" fill="{p['text']}" font-size="13" font-weight="600">{alt2['name']}</text>
      <text x="38" y="50" fill="{p['muted']}" font-size="11">{alt2['vibes'][:38]}...</text>
      <rect x="235" y="24" width="70" height="28" rx="6" fill="{alt2['dark_accent']}"/>
      <text x="249" y="42" fill="#ffffff" font-size="11" font-weight="600">Select</text>
    </g>
"""
    svg += "  </g>\n</svg>"
    return svg

def generate_preview_html(light_p, dark_p, alt_fams):
    rec_name = light_p['name'].replace(' (Light)', '')
    cat = light_p.get('category', 'app').upper()
    contrast_dark = dark_p.get('contrast_text', 16.8)
    
    themes_js = {
        "rec": {
            "title": rec_name,
            "badge": f"RECOMMENDED • {cat}",
            "vibes": light_p['vibes'],
            "statVal": f"{rec_name} Active",
            "statSub": f"WCAG {light_p.get('wcag_rating', 'AAA Pass')}",
            "darkSurface": dark_p['surface'],
            "darkBorder": dark_p['border'],
            "darkBg": dark_p['bg'],
            "darkAccent": dark_p['accent'],
            "darkAccentText": "#08090C" if contrast_ratio(dark_p['accent'], "#FFFFFF") < contrast_ratio(dark_p['accent'], "#08090C") else "#FFFFFF",
            "darkSecondary": dark_p['secondary'],
            "lightSurface": light_p['surface'],
            "lightBorder": light_p['border'],
            "lightBg": light_p['bg'],
            "lightAccent": light_p['accent'],
            "lightAccentText": "#0B0F19" if contrast_ratio(light_p['accent'], "#FFFFFF") < contrast_ratio(light_p['accent'], "#0B0F19") else "#FFFFFF",
            "lightSecondary": light_p['secondary']
        }
    }
    
    alts_html = ""
    for idx, alt in enumerate(alt_fams):
        key = f"alt_{idx}"
        fid = alt["family_id"]
        alp = next((p for p in ALL_200_PALETTES if p["family_id"] == fid and p["mode"] == "light"), light_p)
        adp = next((p for p in ALL_200_PALETTES if p["family_id"] == fid and p["mode"] == "dark"), dark_p)
        
        themes_js[key] = {
            "title": alt["name"],
            "badge": f"ALTERNATIVE {idx+1} • {cat}",
            "vibes": alt["vibes"],
            "statVal": f"{alt['name']} Selected",
            "statSub": f"WCAG {adp.get('wcag_rating', 'AAA Pass')}",
            "darkSurface": adp['surface'],
            "darkBorder": adp['border'],
            "darkBg": adp['bg'],
            "darkAccent": adp['accent'],
            "darkAccentText": "#08090C" if contrast_ratio(adp['accent'], "#FFFFFF") < contrast_ratio(adp['accent'], "#08090C") else "#FFFFFF",
            "darkSecondary": adp['secondary'],
            "lightSurface": alp['surface'],
            "lightBorder": alp['border'],
            "lightBg": alp['bg'],
            "lightAccent": alp['accent'],
            "lightAccentText": "#0B0F19" if contrast_ratio(alp['accent'], "#FFFFFF") < contrast_ratio(alp['accent'], "#0B0F19") else "#FFFFFF",
            "lightSecondary": alp['secondary']
        }
        
        alts_html += f"""
      <div onclick="selectTheme('{key}')" class="p-3 rounded-lg bg-[#0E1016] border border-[#1F2433] hover:border-white/30 cursor-pointer transition-all">
        <div class="flex items-center justify-between mb-1">
          <span class="text-xs font-semibold flex items-center gap-1.5" style="color: {alt['dark_accent']};">
            <span class="w-2.5 h-2.5 rounded-full inline-block" style="background-color: {alt['dark_accent']};"></span>
            {alt['name']}
          </span>
          <span class="text-[10px] font-mono text-[#8C93A8]">{fid}</span>
        </div>
        <p class="text-[11px] text-[#8C93A8] leading-tight">{alt['vibes']}</p>
      </div>"""

    themes_json_str = json.dumps(themes_js, indent=2)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&family=JetBrains+Mono:wght@400;500&display=swap');
    body {{ font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; }}
    .display-font {{ font-family: 'Space Grotesk', -apple-system, sans-serif; }}
    .rim-card {{ box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.1); }}
  </style>
</head>
<body class="bg-transparent text-[#F7F5F0] antialiased p-2">
  <div class="grid grid-cols-1 md:grid-cols-12 gap-3 max-w-4xl mx-auto">
    <!-- Main Recommended Card (Span 7) -->
    <div id="mainPreviewCard" class="md:col-span-7 bg-[#101420] border border-[#262F47] rounded-xl p-5 rim-card transition-all duration-200">
      <div class="flex items-center justify-between mb-3">
        <span id="themeBadge" class="text-xs font-bold uppercase tracking-wider px-2.5 py-1 rounded transition-all">
          RECOMMENDED • {cat}
        </span>
        <div class="flex items-center gap-2">
          <button id="toggleBtn" onclick="toggleModePolarity()" class="text-xs font-semibold px-2.5 py-1 rounded border transition-all">
            🌓 Toggle Light/Dark
          </button>
          <span class="text-xs font-mono text-[#10B981] flex items-center gap-1">
            <span class="w-2 h-2 rounded-full bg-[#10B981] inline-block animate-pulse"></span>
            WCAG AAA ({contrast_dark}:1)
          </span>
        </div>
      </div>

      <h3 id="themeTitle" class="text-xl font-bold text-[#F7F5F0] mb-1.5 display-font tracking-tight">
        {rec_name}
      </h3>
      <p id="themeVibes" class="text-xs text-[#8C93A8] mb-4 leading-relaxed">
        {light_p['vibes']}
      </p>

      <!-- Live Interactive Component Row -->
      <div class="space-y-3 pt-1">
        <div class="flex flex-wrap gap-2.5">
          <button id="primaryBtn" class="px-4 py-2 rounded-lg text-xs font-semibold transition-all shadow-lg active:scale-95">
            Primary Action →
          </button>
          <button id="secondaryBtn" class="px-3.5 py-2 rounded-lg text-xs font-medium border transition-all">
            Secondary Action
          </button>
          <span id="metricPill" class="px-3 py-2 rounded-lg text-xs font-mono font-medium border">
            ● Telemetry Active
          </span>
        </div>

        <!-- Metric Box -->
        <div id="statBox" class="p-3 rounded-lg border flex items-center justify-between">
          <div>
            <div class="text-[11px] font-mono text-[#8C93A8]" id="statLabel">Design System Status</div>
            <div id="statVal" class="text-xs font-bold mt-0.5">{rec_name} Active</div>
          </div>
          <div class="text-right">
            <div class="text-[11px] font-mono text-[#8C93A8]">Accessibility Rating</div>
            <div id="statSub" class="text-xs font-bold font-mono text-[#10B981]">WCAG {light_p.get('wcag_rating', 'AAA Pass')}</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Alternatives Column (Span 5) -->
    <div class="md:col-span-5 flex flex-col justify-between space-y-2">
      <div class="text-xs font-bold text-[#8C93A8] uppercase tracking-wider px-1">
        All Category Alternatives ({cat.lower()})
      </div>
      {alts_html}
    </div>
  </div>

  <script>
    let isDarkMode = true;
    let currentKey = 'rec';
    const themes = {themes_json_str};

    function toggleModePolarity() {{
      isDarkMode = !isDarkMode;
      applyTheme();
    }}

    function selectTheme(key) {{
      currentKey = key;
      applyTheme();
    }}

    function applyTheme() {{
      const t = themes[currentKey];
      const card = document.getElementById("mainPreviewCard");
      const title = document.getElementById("themeTitle");
      const vibes = document.getElementById("themeVibes");
      const pBtn = document.getElementById("primaryBtn");
      const sBtn = document.getElementById("secondaryBtn");
      const mPill = document.getElementById("metricPill");
      const statBox = document.getElementById("statBox");
      const statVal = document.getElementById("statVal");
      const statSub = document.getElementById("statSub");
      const badge = document.getElementById("themeBadge");
      const toggleBtn = document.getElementById("toggleBtn");

      badge.textContent = t.badge + (isDarkMode ? " • DARK" : " • LIGHT");
      title.textContent = t.title;
      vibes.textContent = t.vibes;
      statVal.textContent = t.statVal;
      statSub.textContent = t.statSub;

      if (isDarkMode) {{
        card.style.backgroundColor = t.darkSurface;
        card.style.borderColor = t.darkBorder;
        title.style.color = "#F7F5F0";
        vibes.style.color = "#8C93A8";

        toggleBtn.style.color = "#F7F5F0";
        toggleBtn.style.backgroundColor = "rgba(255, 255, 255, 0.08)";
        toggleBtn.style.borderColor = "rgba(255, 255, 255, 0.18)";

        badge.style.backgroundColor = t.darkAccent + "25";
        badge.style.borderColor = t.darkAccent + "45";
        badge.style.color = t.darkAccent;

        sBtn.style.backgroundColor = "rgba(255, 255, 255, 0.06)";
        sBtn.style.borderColor = t.darkBorder;
        sBtn.style.color = "#F7F5F0";

        pBtn.style.backgroundColor = t.darkAccent;
        pBtn.style.color = t.darkAccentText;

        mPill.style.color = t.darkSecondary;
        mPill.style.backgroundColor = t.darkSecondary + "18";
        mPill.style.borderColor = t.darkSecondary + "40";

        statBox.style.backgroundColor = t.darkBg;
        statBox.style.borderColor = t.darkBorder;
        statVal.style.color = "#F7F5F0";
      }} else {{
        card.style.backgroundColor = t.lightSurface;
        card.style.borderColor = t.lightBorder;
        title.style.color = "#12151E";
        vibes.style.color = "#565B6B";

        toggleBtn.style.color = "#12151E";
        toggleBtn.style.backgroundColor = "rgba(0, 0, 0, 0.06)";
        toggleBtn.style.borderColor = "rgba(0, 0, 0, 0.18)";

        badge.style.backgroundColor = t.lightAccent + "15";
        badge.style.borderColor = t.lightAccent + "40";
        badge.style.color = t.lightAccent;

        sBtn.style.backgroundColor = "#F8FAFC";
        sBtn.style.borderColor = t.lightBorder;
        sBtn.style.color = "#12151E";

        pBtn.style.backgroundColor = t.lightAccent;
        pBtn.style.color = t.lightAccentText;

        mPill.style.color = t.lightSecondary;
        mPill.style.backgroundColor = t.lightSecondary + "18";
        mPill.style.borderColor = t.lightSecondary + "45";

        statBox.style.backgroundColor = t.lightBg;
        statBox.style.borderColor = t.lightBorder;
        statVal.style.color = "#12151E";
      }}
    }}

    applyTheme();
  </script>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="UI/UX Ultra v3.5 Design Engine")
    parser.add_argument("query", nargs="?", default="", help="Search keywords")
    parser.add_argument("--category", default="all")
    parser.add_argument("--mode", choices=["light", "dark", "both"], default="both")
    parser.add_argument("--palette-id", help="Exact palette ID or family ID")
    parser.add_argument("-n", type=int, default=6)
    parser.add_argument("--export-catalog", action="store_true")
    parser.add_argument("--out-dir", default=None, help="Output directory for catalog export")
    parser.add_argument("--persist", action="store_true")
    parser.add_argument("--audit", action="store_true", help="Print WCAG 2.1 contrast audit breakdown")
    parser.add_argument("--svg", action="store_true", help="Output visual preview card as SVG")
    parser.add_argument("--html", help="Path to output interactive preview HTML file")
    parser.add_argument("-p", "--project", default="Project-Ultra")
    args = parser.parse_args()

    if args.export_catalog:
        out_dir = args.out_dir or (os.path.join(os.path.dirname(__file__), "..", "data") if os.path.exists(os.path.join(os.path.dirname(__file__), "..", "data")) else ".")
        export_catalog(out_dir)
        return

    matches = search_palettes(args.query, args.category, None if args.mode == "both" else args.mode, args.n)
    if args.palette_id:
        matches = [p for p in ALL_200_PALETTES if args.palette_id in (p["id"], p["family_id"])] or matches

    chosen = matches[0]
    fam_id = chosen["family_id"]
    light_p = next(p for p in ALL_200_PALETTES if p["family_id"] == fam_id and p["mode"] == "light")
    dark_p  = next(p for p in ALL_200_PALETTES if p["family_id"] == fam_id and p["mode"] == "dark")

    # Extract ALL distinct alternative families in the same category or search matches
    cat = chosen.get("category", "")
    seen_fams = {fam_id}
    alt_fams = []

    # 1. Grab all other families in the same category first
    for p in ALL_200_PALETTES:
        fid = p["family_id"]
        if p.get("category") == cat and fid not in seen_fams:
            seen_fams.add(fid)
            lp = next(x for x in ALL_200_PALETTES if x["family_id"] == fid and x["mode"] == "light")
            dp = next(x for x in ALL_200_PALETTES if x["family_id"] == fid and x["mode"] == "dark")
            alt_fams.append({
                "family_id": fid,
                "name": lp["name"].replace(" (Light)", ""),
                "vibes": lp["vibes"],
                "light_accent": lp["accent"],
                "dark_accent": dp["accent"]
            })

    # 2. Add any other relevant families from search matches
    for m in matches:
        fid = m["family_id"]
        if fid not in seen_fams:
            seen_fams.add(fid)
            lp = next(p for p in ALL_200_PALETTES if p["family_id"] == fid and p["mode"] == "light")
            dp = next(p for p in ALL_200_PALETTES if p["family_id"] == fid and p["mode"] == "dark")
            alt_fams.append({
                "family_id": fid,
                "name": lp["name"].replace(" (Light)", ""),
                "vibes": lp["vibes"],
                "light_accent": lp["accent"],
                "dark_accent": dp["accent"]
            })

    output_data = {
        "selected_family": fam_id,
        "light": light_p,
        "dark": dark_p,
        "alternatives": alt_fams
    }

    if args.audit:
        output_data["wcag_audit"] = {
            "light": audit_palette_contrast(light_p['bg'], light_p['surface'], light_p['text'], light_p['muted'], light_p['accent'], light_p['border']),
            "dark": audit_palette_contrast(dark_p['bg'], dark_p['surface'], dark_p['text'], dark_p['muted'], dark_p['accent'], dark_p['border'])
        }

    if args.svg:
        print(generate_preview_svg(light_p, dark_p, alt_fams))
        return

    if args.html:
        html_content = generate_preview_html(light_p, dark_p, alt_fams)
        out_dir = os.path.dirname(os.path.abspath(args.html))
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        with open(args.html, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[OK] Wrote live interactive preview HTML to {args.html}")

    print(json.dumps(output_data, indent=2))

    if args.persist:
        os.makedirs("design-system", exist_ok=True)
        with open("design-system/theme-tokens.css", "w", encoding="utf-8") as f:
            f.write(compile_css_pair(light_p, dark_p))
        with open("design-system/shadcn-globals.css", "w", encoding="utf-8") as f:
            f.write(compile_shadcn_css(light_p, dark_p))
        with open("design-system/tailwind.tokens.js", "w", encoding="utf-8") as f:
            f.write(compile_tailwind_config())
        with open("design-system/tailwind-v4.css", "w", encoding="utf-8") as f:
            f.write(compile_tailwind_v4_css(light_p, dark_p))
        with open("design-system/flutter_theme.dart", "w", encoding="utf-8") as f:
            f.write(compile_flutter_theme(light_p, dark_p))
        with open("design-system/Theme.swift", "w", encoding="utf-8") as f:
            f.write(compile_swiftui_theme(light_p, dark_p))
        with open("design-system/motion.tokens.js", "w", encoding="utf-8") as f:
            f.write(compile_motion_tokens())
        with open("design-system/theme-toggle.js", "w", encoding="utf-8") as f:
            f.write(compile_theme_toggle_js())
        with open("design-system/preview.svg", "w", encoding="utf-8") as f:
            f.write(generate_preview_svg(light_p, dark_p, alt_fams))
        with open("design-system/preview.html", "w", encoding="utf-8") as f:
            f.write(generate_preview_html(light_p, dark_p, alt_fams))
        with open("design-system/MASTER.md", "w", encoding="utf-8") as f:
            f.write(compile_master_doc(light_p, dark_p, args.project))
        print(f"[OK] Wrote complete design-system bundle for {fam_id} to ./design-system/ (CSS, Shadcn, Tailwind, Flutter, SwiftUI, Motion, Preview SVG & HTML)")

if __name__ == "__main__":
    main()