---
title: "Wormholes and the group's quantum-information-in-QFT programs"
type: connection
areas: [gauge-gravity-duality, bell-inequalities-qft, relative-entropy-qft]
maturity: speculative
modified: 2026-06-04
---

## The Link

[[2021-kundu-wormholes-holography|Kundu's review]] tells the whole wormhole story in the language of **entanglement of the [[thermofield-double-state|thermofield double]]**, **modular/relative-entropy reasoning**, and **negative-energy deformations of a two-sided state**. Every one of these is something the group already computes — but in flat space, on a pair of complementary [[rindler-wedges|Rindler wedges]] of a free field, using [[weyl-operators|Weyl operators]] and [[tomita-takesaki-modular-theory|Tomita–Takesaki theory]]. Because the Minkowski vacuum restricted to two wedges *is* a thermofield double (Bisognano–Wichmann), the group's free-field toolkit is a literal, calculable model of the holographic wormhole's boundary data.

That gives three concrete bridges, in increasing order of ambition:

1. **The GJW coupling is a Connes-cocycle perturbation** of the TFD modular flow — the same object as the group's relative-entropy and crossed-product calculations. → [[relative-entropy-wormhole-opening]]
2. **Traversability injects signaling**, in apparent tension with the no-signaling premise of a maximal [[bell-chsh-inequality|Bell-CHSH]] violation. → [[bell-chsh-across-traversable-wormhole]]
3. **Regenesis is a teleportation channel** through a steady entangled resource — a possible physical instance of [[entanglement-embezzlement|embezzlement]] in [[type-iii-von-neumann-algebras|type III₁]]. → [[holographic-dual-embezzlement-protocol]]

## Evidence

- **Same algebras, same modular theory.** Holographic boundary algebras at large $N$ and free-field wedge algebras are both hyperfinite [[type-iii-von-neumann-algebras|type III₁]] with cyclic-separating vacuum/TFD; the modular conjugation $J$ and modular flow exist identically in both. ([[2025-liu-lectures-entanglement-vna|Liu]] states the holographic side; the group owns the flat-space side.)
- **GJW = cocycle, made explicit.** Ahmad–Jefferson (arXiv:2501.01487) treat the GJW deformation $V = g\,\mathcal{O}_L\mathcal{O}_R$ as a Connes-cocycle perturbation and compute corrections to generalized entropy — the exact technology of the group's relative-entropy program and Sem I Week 7 of the course.
- **The course already plans the flat-space mirror calculations.** AQFT Sem II Wk 8 (Bell-CHSH on the TFD) and Wk 12 (cocycle-perturbed entropy with $V = g\,W(f_L)W(f_R)$) are pencilled-in mini-calculations that would directly feed projects 1–2.

## Gaps

- The group's explicit results are for **free / generalized-free fields**; the GJW $\mathcal{O}_L\mathcal{O}_R$ deformation in a strongly-coupled holographic CFT is not directly one of these. The honest move is to do the free-field two-wedge analogue first and treat it as a model, not a derivation.
- **What is bulk vs. what is algebra.** The Shapiro time advance and the geometric "opening" of the throat are bulk statements the boundary algebra does not resolve (the course's standing caveat). Claims must stay on the algebra side unless a bulk input is explicitly imported.
- For the embezzlement link, there is as yet **no cost theorem** tying a regenesis/teleportation protocol to a relative-entropy cost on the type III$_1$ resource — that is the open content of [[embezzlement-cost-relative-entropy]] and [[holographic-dual-embezzlement-protocol]].

## Potential Projects

- **P1 — Relative entropy of wormhole opening (most computable).** Take the free-field two-wedge TFD; perturb by $V = g\,W(f_L)W(f_R)$; compute the [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] $S(\omega_V\|\omega)$ to $O(g^2)$ via the Connes cocycle, and interpret its sign/size as the "cost of opening the throat." Extends the group's 2025 relative-entropy papers and AQFT Sem II Wk 12. Detailed in [[relative-entropy-wormhole-opening]].
- **P2 — Traversability vs. Tsirelson (most distinctive).** Compute the Bell-CHSH correlator between the two wedge algebras *in the presence of* the coupling $V$, and test for a monotone trade-off between signaling strength $g$ and achievable violation. Detailed in [[bell-chsh-across-traversable-wormhole]].
- **P3 — Regenesis as embezzlement (most speculative).** Formulate the Maldacena–Qi eternal traversable wormhole as a renewable type III$_1$ resource and ask whether information transfer through it is an embezzlement protocol, assigning a relative-entropy cost. Connects ismael-porfirio/erick-landim's thesis work to wormholes.
- **P4 — Factorization vs. large-$N$ factorization (conceptual).** Clarify whether the Euclidean-wormhole **factorization puzzle** ($\langle Z_1 Z_2\rangle \neq \langle Z_1\rangle\langle Z_2\rangle$) and **[[large-n-factorization|large-N factorization]]** of single-trace operators (the very statement that makes the algebra type III$_1$) are in tension or are two faces of one structure. A position-paper / Socratic direction rather than a calculation.

## Related

- [[2021-kundu-wormholes-holography]]
- [[traversable-wormholes]], [[thermofield-double-state]], [[er-epr]]
- [[holographic-bell-program]], [[crossed-product-and-island-formula]]
- [[bell-chsh-in-holographic-setting]], [[holographic-dual-embezzlement-protocol]], [[embezzlement-cost-relative-entropy]]
- [[gauge-gravity-duality]], [[bell-inequalities-qft]], [[relative-entropy-qft]]
