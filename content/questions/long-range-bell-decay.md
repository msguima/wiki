---
title: How does the maximal vacuum Bell-CHSH violation decay with spacelike separation?
type: question
status: open
areas:
  - bell-inequalities-qft
priority: high
originated: 2026-06-19
---

## Statement

Let $\beta(L)$ denote the supremum, over all admissible dichotomic observable pairs $(A_1,A_2;B_1,B_2)$ localized respectively in two spacelike-separated regions $\mathcal{O}_A,\mathcal{O}_B$ at separation $L$, of the [[bell-chsh-inequality|Bell-CHSH]] functional in the vacuum of a free relativistic field. What is the functional form and decay rate of $\beta(L)$ as $L \to \infty$?

This is the quantitative half of **IQOQI Open Quantum Problem #12** (R. Verch, *Bell inequalities for long range vacuum correlations*): vacuum fluctuations maximally violate CHSH for suitable spacelike-separated observables, and the violation tends to the classical bound $2$ as the two localization regions are moved apart. The *rate* of that decay — and explicit observables realizing it — is open.

## Why It Matters

The $L \to 0$ (region-tangency) endpoint is **PROVED**: Summers–Werner showed that the [[type-iii-von-neumann-algebras|type III$_1$]] structure together with the [[rindler-wedges|Reeh–Schlieder]] property forces maximal violation $\beta = 2\sqrt{2}$ (Tsirelson) for the algebras of tangent wedges/double cones. The group's [[weyl-operators|Weyl-operator]] + [[tomita-takesaki-modular-theory|Tomita–Takesaki]] machinery supplies the *body* of the curve at finite $L$. Pinning the decay class — exponential $e^{-mL}$ (massive) versus power-law $L^{-p}$ (massless) — would settle a named open problem and tie the falloff directly to the mass gap and the split property.

## What We Know

- **Lower-bound machinery (group results).** The Weyl + modular-conjugation construction (Phys. Rev. D 108, 085026) gives $\beta \ge 2\sqrt{1+|\langle W(f)W(g)\rangle|^2}$, with the correlator fixed by the smeared [[pauli-jordan-distribution|Pauli–Jordan]] / two-point function. [[causal-diamonds|Causal-diamond]] results (Eur. Phys. J. C 85) and the optimal bounded-Hermitian operator class (Phys. Rev. D 112) make $\beta(L)$ a genuine supremum rather than a single construction. The numerical framework (Phys. Rev. D 110) maps it across mass and dimension.
- **Upper-bound route (open).** Bounding the supremum over *all* observables requires controlling the maximal correlation between $\mathcal{A}(\mathcal{O}_A)$ and $\mathcal{A}(\mathcal{O}_B)$ via Buchholz–Wichmann–Yngvason nuclearity / the split property — not yet carried out for this quantity.

## Possible Approaches

1. **Explicit lower bound** $\beta_{\text{lower}}(L)$ for two diamonds, extracting the leading $L$-law (massive exponential / massless power-law).
2. **Nuclearity/split upper bound**: for massive free fields the split property yields exponential clustering, giving $\beta(L)-2 \le C\,e^{-mL}$.
3. **Massless dichotomy**: tie the slower (power-law) decay to the failure of the split property.
4. **Higher spin**: reuse the massless-spinor Haar-wavelet construction (Phys. Rev. D 108, L081701).

A full execution plan lives at [[long-range-bell-decay-project]].

## Related Questions

- [[higher-spin-bell-inequalities]] — the spin-dependence of the decay constant
- [[impossible-measurements-qft]] — whether the optimal observables are operationally realizable
- [[bell-inequalities-with-gribov-horizon]] — the gauge-theory analogue of the same vacuum-correlation question
- [[bell-chsh-across-traversable-wormhole]] — long-range vacuum correlations in the TFD / wormhole setting
