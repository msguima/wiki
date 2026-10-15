---
title: Thermofield Double State
type: concept
areas: [gauge-gravity-duality, bell-inequalities-qft, relative-entropy-qft]
aliases: [thermofield double, TFD, thermal double, eternal black hole state]
modified: 2026-10-15
---

## Definition

The **thermofield double (TFD)** is a pure state on a doubled Hilbert space $\mathcal{H}_L \otimes \mathcal{H}_R$ whose reduced density matrix on either factor is thermal:
$$
|\mathrm{TFD}_\beta\rangle = \frac{1}{\sqrt{Z(\beta)}} \sum_n e^{-\beta E_n/2}\,|n\rangle_L \otimes |n\rangle_R,
\qquad \mathrm{Tr}_L |\mathrm{TFD}\rangle\langle\mathrm{TFD}| = \frac{e^{-\beta H_R}}{Z(\beta)},
$$
with $H|n\rangle = E_n|n\rangle$ and $Z(\beta)=\sum_n e^{-\beta E_n}$. It is the canonical purification of a Gibbs state, and it goes back to Takahashi and Umezawa's thermo field dynamics (1975).

In holography, the TFD of two copies of a CFT is dual to the **two-sided eternal AdS–Schwarzschild black hole**: the two boundary factors are the two asymptotic regions, joined by a (non-traversable) Einstein–Rosen bridge. Geometric connectivity of the bridge is the bulk image of the $L$–$R$ entanglement — the cleanest statement of [[er-epr|ER=EPR]].

Algebraically the TFD is a **cyclic and separating** vector for the boundary algebras $\mathcal{A}_L, \mathcal{A}_R$, and a **KMS state** at inverse temperature $\beta$ for the time translation that the bulk Killing flow implements. Its [[tomita-takesaki-modular-theory|modular Hamiltonian]] is the difference of the two Hamiltonians, $K \propto H_R - H_L$, so modular time translation is ordinary time running oppositely on the two copies. At large $N$ the algebras are [[type-iii-von-neumann-algebras|type III₁]].

## Role in Research

The TFD is the single state where almost every thread of the group's program converges:

- **Bell-CHSH on the TFD.** The left and right boundary algebras are each other's commutant, and the modular conjugation $J$ maps one to the other — exactly the structure the group uses to build Bob's operators from Alice's with [[weyl-operators|Weyl operators]]. Course Sem II Wk 8 computes Bell-CHSH between two Rindler wedges in the TFD, a direct extension of Summers–Werner, and it is the obvious arena for [[bell-chsh-in-holographic-setting]].
- **Relative entropy and the crossed product.** Because the TFD is KMS and type III₁, the [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] is the well-defined information measure; the [[crossed-product-construction|crossed product]] of $\mathcal{A}_R$ by its modular flow (Chandrasekaran–Penington–Witten) turns the algebra type II$_\infty$ and yields the generalized entropy. The TFD is the reference state of that construction.
- **The base geometry for traversability.** Deforming the TFD by a double-trace coupling $V = g\,\mathcal{O}_L\mathcal{O}_R$ makes the wormhole [[traversable-wormholes|traversable]]; this is the starting point of [[relative-entropy-wormhole-opening]] and [[bell-chsh-across-traversable-wormhole]].
- **A reference, not a catalyst.** In the [[holographic-dual-embezzlement-protocol|embezzlement protocol]] the TFD is the state with a unique dual geometry against which the proposed catalyst is contrasted: the catalyst has no geometry of its own, being a broad area/modular-clock wavepacket dressing the TFD wormhole.

## Relations

- The flat-space analogue is the **Minkowski vacuum** restricted to two complementary [[rindler-wedges|Rindler wedges]]: the vacuum is the TFD of the two wedge algebras at the Unruh temperature ([[bisognano-wichmann-theorem|Bisognano–Wichmann]]). This is why free-field two-wedge calculations model the holographic TFD.
- [[tomita-takesaki-modular-theory]] — cyclic-separating, with geometric modular flow $K \propto H_R - H_L$; the KMS condition encodes thermality
- [[type-iii-von-neumann-algebras]] — the left and right algebras are type III₁ at large $N$
- [[crossed-product-construction]] — the gravitational crossed product is built on the TFD modular flow, and its trace gives the generalized entropy
- [[araki-uhlmann-relative-entropy]] — computed between excited states and the TFD reference
- [[large-n-factorization]] — single-trace operators on each factor factorize at large $N$, which is what makes the algebras type III₁
- [[er-epr]], [[traversable-wormholes]] — connectivity from entanglement, and what it takes to send a signal across
- [[bell-chsh-across-traversable-wormhole]], [[relative-entropy-wormhole-opening]] — the two TFD wedges as the bipartite arena

## Papers

- Maldacena, *Eternal black holes in anti-de Sitter*, JHEP 04 (2003) 021 [hep-th/0106112] — the identification with the eternal black hole.
- Takahashi, Umezawa (1975) — the origin of thermo field dynamics, and of the construction itself.
- Chandrasekaran, Penington, Witten (2022), arXiv:2209.10454 — the TFD as a type III₁ KMS state and its crossed product (AQFT course Sem II Block 2).
- [[2021-kundu-wormholes-holography]] — §4.2.1 introduces the TFD as the two-sided eternal black hole.
- [[2025-liu-lectures-entanglement-vna]] — the modular/KMS treatment and the algebraic ER=EPR.

## Notes

- A useful slogan for students: the TFD is "entanglement masquerading as geometry". Everything the group computes in flat space on a pair of complementary wedges has a TFD reading, and conversely every TFD statement has a Rindler analogue that is explicitly calculable with [[weyl-operators|Weyl operators]].
- Common confusion: the TFD is a *pure* state on the doubled space, and its thermality is a property of the *reduced* state on one factor. The temperature is the modular/KMS temperature of the reference state, which in the holographic dual is the Hawking temperature of the eternal black hole.
- This page absorbed a duplicate, `thermofield-double`, written a day apart from it in June 2026 for the same object; the aliases of both are kept above.
