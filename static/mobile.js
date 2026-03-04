/**
 * PayBack — Mobile Navigation
 * Injects a hamburger button and overlay for the slide-out sidebar on small screens.
 * Only activates below 600px; above that the bottom-nav CSS handles everything.
 */
(function () {

  // Hamburger button (shown only by CSS at medium-mobile sizes if ever needed)
  // Primary mobile UX is the bottom-nav bar handled purely in CSS.
  // This script handles the touch-friendly active-state for nav items.

  // Highlight the current nav item based on pathname
  const path = window.location.pathname;
  document.querySelectorAll('.nav-item').forEach(function (el) {
    const href = el.getAttribute('href');
    if (!href) return;
    const isActive = href === '/'
      ? (path === '/' || path === '/index')
      : path.startsWith(href);
    if (isActive) {
      el.classList.add('active');
    } else {
      el.classList.remove('active');
    }
  });

})();
