// UI/UX Ultra v3.5 — Spring & Motion Intelligence Tokens
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
