// Zero-flash dual-theme switcher (light / dark)
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
