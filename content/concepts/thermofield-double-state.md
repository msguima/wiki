---
title: Thermofield Double State
type: concept
areas: [gauge-gravity-duality, bell-inequalities-qft, relative-entropy-qft]
aliases: [thermofield double, TFD, eternal black hole state]
modified: 2026-06-04
---

## Definition

The **thermofield double (TFD)** is a pure state on a doubled Hilbert space $\mathcal{H}_L \otimes \mathcal{H}_R$ whose reduced density matrix on either factor is thermal:
$$
|\mathrm{TFD}\rangle = \frac{1}{\sqrt{Z(\beta)}} \sum_n e^{-\beta E_n/2}\,|n\rangle_L \otimes |n\rangle_R,
\qquad \mathrm{Tr}_L |\mathrm{TFD}\rangle\langle\mathrm{TFD}| = \frac{e^{-\beta H_R}}{Z(\beta)}.
$$
It is the canonical purification of a Gibbs state. In holography, the TFD of two copies of a CFT is dual to the **two-sided eternal AdS–Schwarzschild black hole**: the two boundary factors are the two asymptotic regions, joined by a (non-traversable) Einstein–Rosen bridge. Geometric connectivity of the bridge is the bulk image of the $L$–$R$ entanglement — the cleanest statement of [[er-epr|ER=EPR]].

Algebraically, the TFD is a **cyclic and separating vector** for the boundary algebras $\mathcal{A}_L, \mathcal{A}_R$, and it is a **KMS state** at inverse temperature $\beta$ for the boost/time-translation that the bulk Killing flow implements. Its [[tomita-takesaki-modular-theory|modular operator]] is (the exponential of) the boost generator. At large $N$ the algebras are [[type-iii-von-neumann-algebras|type III₁]].

## Role in Research

The TFD is the single state where almost every thread of the group's program converges:

- **Bell-CHSH on the TFD.** The left/right boundary algebras are complementary, and the modular conjugation $J$ maps one to the other — exactly the structure the group uses to build Bob's operators from Alice's via [[weyl-operators|Weyl operators]]. Course Sem II Wk 8 computes Bell-CHSH between two Rindler wedges in the TFD (a direct extension of Summers–Werner). It is the obvious arena for [[bell-chsh-in-holographic-setting]].
- **Relative entropy and the crossed product.** Because the TFD is KMS and type III$_1$, [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] is the well-defined information measure; the [[crossed-product-construction|crossed product]] of $\mathcal{A}_R$ by its modular flow (Chandrasekaran–Penington–Witten) turns it type II$_\infty$ and yields generalized entropy.
- **The base geometry for traversability.** Deforming the TFD by a double-trace coupling $V = g\,\mathcal{O}_L\mathcal{O}_R$ makes the wormhole [[traversable-wormholes|traversable]]; this is the starting point of [[relative-entropy-wormhole-opening]] and [[bell-chsh-across-traversable-wormhole]].

## Relations

- The flat-space analogue is the **Minkowski vacuum** restricted to two complementary [[rindler-wedges|Rindler wedges]]: the vacuum is the TFD of the two wedge algebras at the Unruh temperature (Bisognano–Wichmann). This is why free-field two-wedge calculations model the holographic TFD.
- Cyclic-separating ⇒ [[tomita-takesaki-modular-theory|Tomita–Takesaki]] structure; KMS ⇒ modular flow = thermal time.
- Underlies [[er-epr|ER=EPR]] and the [[traversable-wormholes|traversable wormhole]] constructions.
- Single-trace operators on each boundary factorize at large $N$ ([[large-n-factorization]]) ⇒ [[type-iii-von-neumann-algebras|type III₁]].

## Papers

- [[2021-kundu-wormholes-holography]] — §4.2.1 introduces the TFD as the two-sided eternal black hole.
- [[2025-liu-lectures-entanglement-vna]] — modular/KMS treatment and the algebraic ER=EPR.
- Maldacena (2003), *Eternal black holes in AdS* (arXiv:hep-th/0106112) — the foundational identification.
- Chandrasekaran, Penington, Witten (2022), arXiv:2209.10454 — TFD as a type III$_1$ KMS state and its crossed product (AQFT course Sem II Block 2).

## Notes

A useful slogan for students: the TFD is "entanglement masquerading as geometry." Everything the group computes in flat space on a pair of complementary wedges has a TFD reading, and conversely every TFD statement has a Rindler analogue that is explicitly calculable with [[weyl-operators|Weyl operators]].
