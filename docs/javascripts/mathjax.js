// MathJax settings. "cancel" is the package that draws the slash marks
// (\cancel, \bcancel, \xcancel) used in the unit-cancellation examples.
window.MathJax = {
  loader: { load: ["[tex]/cancel"] },
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    packages: { "[+]": ["cancel"] }
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// Re-render the math whenever a page is loaded (needed for instant navigation).
document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
