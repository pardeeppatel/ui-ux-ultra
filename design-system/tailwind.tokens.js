// Tailwind CSS Tokens Configuration
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
