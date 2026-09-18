---
title: Thermofield Double
type: concept
areas:
  - relative-entropy-qft
  - bell-inequalities-qft
  - gauge-gravity-duality
aliases: [TFD, thermofield double state, thermal double]
modified: 2026-06-05
---

## Definition

The **thermofield double (TFD)** is a pure entangled state on a doubled Hilbert space $\mathcal H_L \otimes \mathcal H_R$ that purifies a thermal (Gibbs) state. For a system with Hamiltonian $H$ and eigenstates $H|n\rangle = E_n|n\rangle$, at inverse temperature $\beta$,

$$|\mathrm{TFD}_\beta\rangle = \frac{1}{\sqrt{Z(\beta)}}\sum_n e^{-\beta E_n/2}\,|n\rangle_L \otimes |n\rangle_R, \qquad Z(\beta)=\sum_n e^{-\beta E_n}.$$

Tracing out either factor returns the thermal density matrix, $\mathrm{Tr}_L |\mathrm{TFD}\rangle\langle\mathrm{TFD}| = e^{-\beta H}/Z$. The TFD is cyclic and separating for each side's algebra, and its modular flow is geometric: the modular Hamiltonian is (proportional to) the difference of the left and right Hamiltonians, $K \propto H_R - H_L$, so modular time translation is ordinary time translation acting oppositely on the two copies. The state satisfies the KMS condition at inverse temperature $\beta$, which is the algebraic statement of thermality.

## Role in Research

The TFD is the canonical two-sided entangled state and the recurring "arena" across the group's wormhole/quantum-information thread:

- **Holographic dual (Maldacena).** The TFD of two copies of a holographic CFT is dual to the maximally extended **eternal AdS–Schwarzschild black hole** — one state, one geometry. This is the template against which the [[holographic-dual-embezzlement-protocol|embezzlement catalyst]] is contrasted: the catalyst has *no* unique dual geometry but is instead a broad area/modular-clock wavepacket dressing the TFD wormhole.
- **Algebraic structure.** At strict large $N$ the left and right boundary algebras are [[type-iii-von-neumann-algebras|Type III₁ factors]]; including the gravitational constraint promotes the relevant algebra to a Type II$_\infty$ [[crossed-product-construction|crossed product]] whose trace gives the generalized entropy. The TFD is the reference state for this construction.
- **Bipartite test bed.** The two spacelike-separated wedges of the TFD provide the natural Alice/Bob split for [[bell-chsh-across-traversable-wormhole|Bell-CHSH across a traversable wormhole]] and for the [[relative-entropy-wormhole-opening|relative entropy of wormhole opening]].

## Relations

- [[type-iii-von-neumann-algebras]] — the left/right wedge algebras in the TFD are Type III₁ at large $N$
- [[crossed-product-construction]] — the gravitational crossed product is built on the TFD modular flow; trace → generalized entropy
- [[tomita-takesaki-modular-theory]] — the TFD is cyclic-separating with geometric modular flow $K \propto H_R - H_L$; the KMS condition encodes thermality
- [[rindler-wedges]] — the Minkowski vacuum restricted to a Rindler wedge is a TFD in the boost energy (Bisognano–Wichmann); same structure, modular flow = boost
- [[holographic-dual-embezzlement-protocol]] — the embezzlement catalyst is a dressing of the TFD wormhole rather than a new geometry
- [[bell-chsh-across-traversable-wormhole]], [[relative-entropy-wormhole-opening]] — use the two TFD wedges as the bipartite arena
- [[araki-uhlmann-relative-entropy]] — computed between excited states and the TFD reference

## Papers

- J. M. Maldacena, "Eternal black holes in anti-de Sitter," JHEP 04 (2003) 021 [hep-th/0106112] — TFD ↔ eternal AdS black hole.
- Y. Takahashi and H. Umezawa (1975) — origin of thermo field dynamics / the TFD construction.

See [[holographic-dual-embezzlement-protocol]] and the wormhole question pages for the active research context.

## Notes

- Created 2026-06-05 to resolve a recurring `[[thermofield-double]]` link referenced from the embezzlement and wormhole question pages.
- Common confusion: the TFD is a *pure* state on the doubled space; its thermality is a property of the *reduced* state on one factor. "Temperature" here is the modular/KMS temperature of the reference state, which in the holographic dual is the Hawking temperature of the eternal black hole.
