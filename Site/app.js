const modules = {
  portfolio: {
    eyebrow: "Portfolio intelligence",
    title: "Know what changed, not just what you own.",
    text: "WAZO summarizes the selected financial year, compares growth, and highlights allocation gaps that need attention.",
    bullets: ["Financial year: April 1 to March 31", "Current vs desired asset allocation", "Member-level portfolio breakdown"],
  },
  assets: {
    eyebrow: "Asset control",
    title: "Keep ownership and valuation clean.",
    text: "Assets are linked to members, searchable by year, category, owner, type, and value range, with manual gold and silver rates.",
    bullets: ["Member-owned assets", "Manual metal rates", "Search, sort, and pagination"],
  },
  goals: {
    eyebrow: "Financial planning",
    title: "Convert future goals into monthly action.",
    text: "Goal Intelligence estimates monthly and annual funding needs across equity, gold, and real estate assumptions.",
    bullets: ["FIRE number", "Goal funding gap", "Investment mix suggestions"],
  },
  reports: {
    eyebrow: "Designed reporting",
    title: "Export polished summaries when you need them.",
    text: "Create smart reports, PDF/HTML/CSV exports, portfolio summaries, growth views, and printable snapshots.",
    bullets: ["PDF-ready layouts", "Smart focus cards", "Portfolio and goal exports"],
  },
};

const formatter = new Intl.NumberFormat("en-IN");

function animateCounters() {
  document.querySelectorAll("[data-count]").forEach((element) => {
    const target = Number(element.dataset.count || 0);
    let current = 0;
    const steps = 46;
    const increment = target / steps;
    const timer = window.setInterval(() => {
      current += increment;
      if (current >= target) {
        current = target;
        window.clearInterval(timer);
      }
      element.textContent = target > 1000 ? `₹${formatter.format(Math.round(current))}` : formatter.format(Math.round(current));
      if (target === 58) element.textContent = `${Math.round(current)}%`;
    }, 24);
  });
}

function setTourPanel(key) {
  const panel = modules[key] || modules.portfolio;
  document.querySelectorAll(".tour-tabs button").forEach((button) => {
    button.classList.toggle("active", button.dataset.panel === key);
  });
  document.getElementById("tour-panel").innerHTML = `
    <div>
      <span class="eyebrow">${panel.eyebrow}</span>
      <h3>${panel.title}</h3>
      <p>${panel.text}</p>
    </div>
    <ul>${panel.bullets.map((item) => `<li>${item}</li>`).join("")}</ul>
  `;
}

function updateRebalance() {
  const equityTarget = Number(document.getElementById("equityRange").value);
  const goldTarget = Number(document.getElementById("goldRange").value);
  const equityGap = equityTarget - 42;
  const goldGap = goldTarget - 18;
  const blendedGap = Math.round((equityGap + goldGap) / 2);
  document.getElementById("equityValue").textContent = equityTarget;
  document.getElementById("goldValue").textContent = goldTarget;
  document.getElementById("rebalanceValue").textContent = `${blendedGap >= 0 ? "+" : ""}${blendedGap}%`;
  document.getElementById("rebalanceSignal").textContent = blendedGap > 5 ? "Add gradually" : blendedGap < -5 ? "Reduce exposure" : "Near target";
}

document.querySelectorAll(".tour-tabs button").forEach((button) => {
  button.addEventListener("click", () => setTourPanel(button.dataset.panel));
});

["equityRange", "goldRange"].forEach((id) => {
  document.getElementById(id).addEventListener("input", updateRebalance);
});

animateCounters();
updateRebalance();
