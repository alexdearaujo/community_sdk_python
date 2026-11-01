/* Step-through controls for Mermaid sequence diagrams. Under each diagram it
   adds Back and Next buttons that light one message at a time, and one button
   per branch of an alt box that lights only the steps of that outcome. */
(() => {
  "use strict";
  const DIM = "0.15";

  function controls(svg) {
    const lines = [...svg.querySelectorAll(".messageLine0, .messageLine1")];
    const texts = [...svg.querySelectorAll(".messageText")];
    if (!lines.length || lines.length !== texts.length) return;
    const y = (el) => parseFloat(el.getAttribute("y1") || el.getAttribute("y") || "0");
    // A self-message is a path with no y attribute, so place every step by its text.
    const steps = lines.map((line, i) => ({ line, text: texts[i], y: y(texts[i]), label: texts[i].textContent.trim() }));

    const labels = [...svg.querySelectorAll(".loopText")].map((t) => ({ name: t.textContent.trim().replace(/^\[|\]$/g, ""), y: y(t) }));
    const bottom = Math.max(...[...svg.querySelectorAll(".loopLine")].map((l) => Math.max(y(l), parseFloat(l.getAttribute("y2") || "0"))), 0);
    const top = labels.length ? labels[0].y : Infinity;
    const branches = labels.map((label, i) => {
      const end = i + 1 < labels.length ? labels[i + 1].y : bottom;
      return { name: label.name, keep: steps.filter((s) => s.y < top || s.y > bottom || (s.y > label.y && s.y < end)) };
    });

    const bar = document.createElement("div");
    bar.className = "kx seq-steps";
    const status = document.createElement("p");
    status.className = "seq-status";
    status.setAttribute("aria-live", "polite");
    const button = (text, onClick) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "chip";
      b.textContent = text;
      b.addEventListener("click", onClick);
      return b;
    };

    let current = -1;
    let shown = steps;

    function paint() {
      for (const s of steps) {
        const inPath = shown.includes(s);
        const index = shown.indexOf(s);
        const visible = inPath && (current < 0 || index <= current);
        const lit = inPath && index === current;
        s.line.style.opacity = visible ? "1" : DIM;
        s.text.style.opacity = visible ? "1" : DIM;
        s.line.style.strokeWidth = lit ? "3" : "";
        s.text.style.fontWeight = lit ? "700" : "";
      }
      if (current < 0) {
        status.textContent = shown !== steps
          ? `${shown.length} steps on this path. Press Next to follow them.`
          : branches.length
            ? `Each call takes only one section of the dotted alt box. Pick one above, or press Next to follow the first: ${branches[0].name}.`
            : `${steps.length} steps. Press Next to follow them one at a time.`;
      } else {
        status.textContent = `Step ${current + 1} of ${shown.length}: ${shown[current].label}`;
      }
    }

    const branchButtons = branches.map((branch) => {
      const b = button(branch.name, () => {
        shown = branch.keep;
        current = -1;
        press(b);
        paint();
      });
      return b;
    });
    const all = button("All steps", () => { shown = steps; current = -1; press(all); paint(); });
    function press(active) {
      for (const b of [all, ...branchButtons]) b.setAttribute("aria-pressed", String(b === active));
    }

    const back = button("Back", () => { current = Math.max(-1, current - 1); paint(); });
    const next = button("Next", () => {
      // Stepping through every branch would suggest that a call runs all of them.
      if (shown === steps && branchButtons.length) branchButtons[0].click();
      current = Math.min(shown.length - 1, current + 1);
      paint();
    });
    back.classList.add("seq-nav");
    next.classList.add("seq-nav");

    bar.append(back, next, all, ...branchButtons, status);
    press(all);
    svg.closest(".mermaid")?.after(bar);
    paint();
  }

  function scan() {
    for (const svg of document.querySelectorAll('svg[aria-roledescription="sequence"]')) {
      if (svg.dataset.steps) continue;
      svg.dataset.steps = "1";
      controls(svg);
    }
  }

  // Mermaid draws the diagrams after the page loads, so wait for each one.
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
  scan();
})();
