function updateRebalance() {
  const equityControl = document.getElementById("equityRange");
  const goldControl = document.getElementById("goldRange");
  const equityTarget = Number(equityControl?.value || 60);
  const goldTarget = Number(goldControl?.value || 15);
  const equityGap = equityTarget - 42;
  const goldGap = goldTarget - 18;
  const blendedGap = Math.round((equityGap + goldGap) / 2);
  const signal =
    blendedGap > 5
      ? "Add gradually"
      : blendedGap < -5
        ? "Reduce exposure"
        : "Near target";

  document.getElementById("equityValue").textContent = equityTarget;
  document.getElementById("goldValue").textContent = goldTarget;
  document.getElementById("rebalanceValue").textContent =
    `${blendedGap >= 0 ? "+" : ""}${blendedGap}%`;
  document.getElementById("rebalanceSignal").textContent = signal;

  equityControl?.setAttribute("aria-valuetext", `${equityTarget}% equity target`);
  goldControl?.setAttribute("aria-valuetext", `${goldTarget}% gold target`);
}

["equityRange", "goldRange"].forEach((id) => {
  document.getElementById(id)?.addEventListener("input", updateRebalance);
});

updateRebalance();
