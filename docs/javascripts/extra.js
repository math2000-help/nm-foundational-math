// 1) Add a "Print / Save as PDF" button to the top of every page.
// 2) Open every "Show answer" box while printing, then restore them afterwards.

function addPrintButton() {
  const article = document.querySelector(".md-content__inner");
  if (!article || article.querySelector(".print-button")) return;
  const btn = document.createElement("button");
  btn.type = "button";
  btn.className = "print-button md-button";
  btn.textContent = "Print / Save as PDF";
  btn.addEventListener("click", () => window.print());
  article.insertBefore(btn, article.firstChild);
}

if (typeof document$ !== "undefined") {
  document$.subscribe(addPrintButton);
} else {
  document.addEventListener("DOMContentLoaded", addPrintButton);
}

window.addEventListener("beforeprint", () => {
  document.querySelectorAll("details").forEach((d) => {
    d.dataset.wasOpen = d.open ? "1" : "0";
    d.open = true;
  });
});

window.addEventListener("afterprint", () => {
  document.querySelectorAll("details").forEach((d) => {
    d.open = d.dataset.wasOpen === "1";
  });
});
