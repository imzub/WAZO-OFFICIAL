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

function updateRebalance() {
  const equityTarget = Number(document.getElementById("equityRange")?.value || 60);
  const goldTarget = Number(document.getElementById("goldRange")?.value || 15);
  const equityGap = equityTarget - 42;
  const goldGap = goldTarget - 18;
  const blendedGap = Math.round((equityGap + goldGap) / 2);
  document.getElementById("equityValue").textContent = equityTarget;
  document.getElementById("goldValue").textContent = goldTarget;
  document.getElementById("rebalanceValue").textContent = `${blendedGap >= 0 ? "+" : ""}${blendedGap}%`;
  document.getElementById("rebalanceSignal").textContent = blendedGap > 5 ? "Add gradually" : blendedGap < -5 ? "Reduce exposure" : "Near target";
}

["equityRange", "goldRange"].forEach((id) => {
  const element = document.getElementById(id);
  if (element) element.addEventListener("input", updateRebalance);
});

animateCounters();
updateRebalance();
