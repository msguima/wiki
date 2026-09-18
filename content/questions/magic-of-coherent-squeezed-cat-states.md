---
title: What is the magic of coherent, squeezed, and cat states in QFT?
type: question
status: open
areas: [relative-entropy-qft, bell-inequalities-qft]
priority: high
originated: 2026-07-21
---

## Statement

Compute the **[[magic-nonstabilizerness|magic]]** (via the anti-flatness witness $F_2$) of the group's standard free-field states — coherent, squeezed, and [[cat-states|cat states]] — reduced to a [[rindler-wedges|Rindler wedge]], using the same modular / Bogoliubov machinery already used for their [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]]. Concretely: for each state $\omega$, obtain the wedge reduced density matrix $\rho_\omega$, evaluate
$$F_2(\rho_\omega) = \mathrm{Tr}(\rho_\omega^{3})\,\mathrm{Tr}(\rho_\omega) - \mathrm{Tr}(\rho_\omega^{2})^2,$$
and hence the stabilizer-distance lower bound $F_2/8 \le \min_{\sigma\in\mathrm{STAB}}\lVert\omega-\sigma\rVert$. **Do cat states maximize magic where large-$N$ particle states flatten it?**

## Why It Matters

[[2026-benedetti-magic-in-qft|Benedetti–Dabholkar–Dalmonte]] establish that *every* physical QFT state is magical, and compute anti-flatness explicitly only for free-boson Unruh $N$-particle states — finding, counter-intuitively, that the spectrum becomes **flatter** as $N\to\infty$ (a singular, non-Fock limit). The group already possesses the exact reduced structure for a *different* and physically richer family — coherent, squeezed, and cat states — from its 2025 relative-entropy papers and the 2026 cat-states/Bell-CHSH paper (Phys. Rev. D 113, 065008). Assigning those states a magic content is therefore a **near-drop-in computation** that (i) extends the paper with new, non-trivial examples, (ii) puts magic side-by-side with relative entropy and Bell-CHSH violation *for the same states*, and (iii) tests a sharp hypothesis: superpositions (cat states) are exactly where non-classicality piles up, so they are the natural candidate for **maximal** anti-flatness, opposite to the $N\to\infty$ flattening. A clean "cat states are maximally magical" result would be a compact, publishable QI-in-QFT statement.

## What We Know

- **Flatness ⟺ stabilizer (necessary).** A flat entanglement spectrum is necessary for stabilizerness; anti-flatness $F_2$ is a magic witness and lower-bounds the distance to the stabilizer set (Tirrito et al. 2024; Cao et al. 2024). See [[magic-nonstabilizerness]].
- **The reduced states are in hand.** The Minkowski vacuum is a two-mode squeezed state of left/right Rindler modes; coherent, squeezed, and cat states are built by Weyl / Bogoliubov operations on it, and their wedge reductions are computable from the two-point function — the same input the group uses for $S(\omega\Vert\Omega)$.
- **A comparison point exists.** For Unruh $N$-particle states $F_n$ peaks at intermediate $q_\omega=e^{-\omega/T_U}$ and decreases with $n$ and with $N$; this is the curve to beat with cat states.
- **Relative entropy is already computed** for these states, so magic vs. relative entropy can be plotted directly, feeding [[relative-entropy-magic-inequality]].

## Possible Approaches

1. **Direct anti-flatness from the two-point function.** Express $\mathrm{Tr}(\rho_\omega^n)$ for coherent/squeezed/cat states via the Gaussian (for coherent/squeezed) and Gaussian-superposition (for cat) structure of the wedge reduced state; evaluate $F_2$ in closed form or numerically per Rindler frequency $\omega$, then sum $S_n(\rho)=\sum_\omega S_n(\rho_\omega)$ as in the paper.
2. **Cat vs. coherent contrast.** Since a cat state is a superposition of two coherent states, compute the interference contribution to $F_2$ and check whether it *enhances* anti-flatness relative to a single coherent state at matched energy.
3. **Cross-plot against relative entropy and Bell-CHSH.** For the same test-function / squeezing parameters that maximize the Bell-CHSH violation, evaluate magic — a first look at whether the operators that best violate Bell are also the most magical (Gap 1 of [[type-iii-algebras-across-areas]]).
4. **Sanity check against known limits.** Recover the paper's $N$-particle curve as a special case; verify $F_2\to 0$ on the (unphysical) flat Rindler/Boulware-like construction.

## Related Questions

- [[relative-entropy-magic-inequality]] — the quantitative magic ↔ relative-entropy ↔ Bell relation this feeds.
- [[magic-and-the-gribov-horizon]] — the same computation with a Gribov-restricted vacuum.
- [[relative-entropy-interacting-theories]] — extending beyond free fields.
- [[long-range-bell-decay]], [[bell-chsh-in-holographic-setting]] — sibling III₁ observables on the same states.
