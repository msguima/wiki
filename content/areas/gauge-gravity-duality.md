---
title: Gauge/Gravity Duality
type: area
status: exploratory
modified: 2026-05-26
---

## Overview

Gauge/gravity duality — the conjecture that certain quantum gauge theories in $d$ spacetime dimensions are equivalent to theories of quantum gravity (typically string theory) on a $(d+1)$-dimensional asymptotically anti-de Sitter (AdS) spacetime — is, since Maldacena's 1997 proposal, one of the central organising frameworks of modern theoretical physics. In its sharpest form, the **AdS/CFT correspondence** identifies the boundary CFT's algebra of single-trace operators at large $N$ with the bulk gravitational algebra in a specific subregion (the entanglement wedge), so that every state and every operator on one side has a counterpart on the other.

**Status in this wiki.** Gauge/gravity duality is not a primary research line for the group. It is *exploratory / adjacent*: it sits next to the [[bell-inequalities-qft|Bell inequalities in QFT]] and [[relative-entropy-qft|relative entropy in QFT]] programs as a *structural source of concepts* (in particular, the [[type-iii-von-neumann-algebras|type III₁ algebra]] of single-trace operators at large $N$) and as a *target of speculation* (whether the Bell-CHSH and modular tools developed for flat-space QFT can probe boundary subalgebras of holographic CFTs — see [[bell-chsh-in-holographic-setting]]).

This area page exists primarily as the home of a two-semester graduate course (the *AdS/CFT course* — see syllabus under `wiki/courses/`) and as a scaffold for the concept pages that the course's lecture notes will reference. The external resource [adscft.org](https://adscft.org/) is treated as the course's primary text; this wiki adds framing, notation alignment, and explicit connections to the group's research programs.

## Key Results

- **Maldacena's conjecture (1997).** $\mathcal{N}=4$ SU($N$) super-Yang–Mills in 4d $\leftrightarrow$ Type IIB superstring theory on $\mathrm{AdS}_5 \times S^5$. The first concrete realisation of gauge/gravity duality.
- **GKP-Witten formula (1998).** $Z_{\text{CFT}}[J] = Z_{\text{gravity}}[\phi|_{\partial} = J]$ — see [[gkp-witten-formula]]. The operational dictionary that turns bulk classical computations into boundary correlators.
- **Large-$N$ factorization.** Single-trace boundary operators are generalized free fields at $N=\infty$; their algebra is type III₁ — see [[large-n-factorization]] and [[type-iii-von-neumann-algebras]].
- **Ryu-Takayanagi formula (2006).** Holographic entanglement entropy from minimal-area extremal surfaces in the bulk — see [[ryu-takayanagi-formula]].
- **Quantum extremal surfaces / island formula (2019).** Resolution of the black-hole information puzzle in semiclassical gravity coupled to a bath — see [[quantum-extremal-surfaces]] and [[page-curve]].
- **JT gravity as a soluble laboratory.** 2d dilaton gravity with a calculable boundary CFT (Schwarzian theory) — see [[jt-gravity]].
- **Subregion-subalgebra duality.** Bulk regions correspond to boundary subalgebras; the duality refines entanglement-wedge reconstruction at the level of algebras — see [[subregion-subalgebra-duality]].

## Open Problems

- [[bell-chsh-in-holographic-setting]] — Can Bell-CHSH and relative-entropy techniques probe holographic spacetime structure?
- [[bell-chsh-across-traversable-wormhole]] — Does opening a traversable wormhole (GJW coupling) degrade the Bell-CHSH violation between its two sides?
- [[relative-entropy-wormhole-opening]] — What is the Araki-Uhlmann relative entropy of the GJW double-trace deformation, treated as a Connes cocycle, in a free-field analogue?
- [[relative-entropy-interacting-theories]] — Can the Araki-Uhlmann relative entropy program be extended beyond free field theories, including in holographic CFTs?
- The interpretive status of the island formula and whether it admits a fully algebraic derivation parallel to [[crossed-product-construction]].
- Whether bulk reconstruction beyond the entanglement wedge can be made precise.

## Key Concepts

- [[holographic-dictionary]]
- [[gkp-witten-formula]]
- [[large-n-factorization]]
- [[ryu-takayanagi-formula]]
- [[quantum-extremal-surfaces]]
- [[replica-trick-gravity]]
- [[jt-gravity]]
- [[page-curve]]
- [[subregion-subalgebra-duality]]
- [[type-iii-von-neumann-algebras]]
- [[crossed-product-construction]]
- [[tomita-takesaki-modular-theory]]
- [[thermofield-double-state]]
- [[er-epr]]
- [[traversable-wormholes]]

## Key Papers

**Ingested:**

- [[2021-kundu-wormholes-holography]] — Kundu, *Wormholes & Holography: An Introduction* (arXiv:2110.14958; EPJC 82, 447, 2022). 89-page pedagogical review of Euclidean and traversable wormholes, the TFD/eternal-black-hole picture, replica wormholes, and GJW/Maldacena–Qi traversability.
- [[2026-goto-rethinking-qi-gravity-fields]] — Goto et al., *Rethinking quantum information in gravity and fields* (arXiv:2606.30853, 2026). Nine-author open-problems agenda at the gravity/QI interface (operational characterization, observers, QEC, infinite-dimensional Hilbert spaces); its type II–III / operational-characterization themes map directly onto the group's programs — see [[gravity-qi-open-problems]].

Paper-page candidates (to be ingested as the course is taught — see `wiki/courses/ads-cft-course/appendices/bibliography-and-paper-map.md`):

- Maldacena 1997 — *The large-N limit of superconformal field theories and supergravity* (arXiv:hep-th/9711200).
- Gubser, Klebanov, Polyakov 1998 — *Gauge theory correlators from non-critical string theory* (arXiv:hep-th/9802109).
- Witten 1998 — *Anti-de Sitter space and holography* (arXiv:hep-th/9802150).
- Aharony, Gubser, Maldacena, Ooguri, Oz 2000 — *Large $N$ field theories, string theory and gravity* (Phys. Rep. 323).
- McGreevy 2009 — *Holographic duality with a view toward many-body physics* (arXiv:0909.0518).
- Harlow 2018 — *TASI lectures on the emergence of bulk physics in AdS/CFT* (arXiv:1802.01040).
- Ryu, Takayanagi 2006 — *Holographic derivation of entanglement entropy from AdS/CFT* (PRL 96, 181602).
- Penington 2019 — *Entanglement wedge reconstruction and the information paradox* (arXiv:1905.08255).
- Almheiri, Engelhardt, Marolf, Maxfield 2019 — *The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole* (arXiv:1905.08762).
- Maldacena, Qi 2018 — *Eternal traversable wormhole* (arXiv:1804.00491).
- [[2025-liu-lectures-entanglement-vna]] — Liu's review of entanglement, von Neumann algebras, and emergence of spacetime (arXiv:2510.07017).

*General reference:* xiyin-qft-monograph — Vol V (Conformal Field Theory) for the CFT-side foundations. (QFT-focused; does not cover holographic RT/QES, islands, or the Page curve.)

## Connections

- [[bell-inequalities-qft]] — type III₁ algebras of subregions are the natural setting for both Bell-CHSH analyses (flat space) and holographic boundary subalgebras (large-$N$ AdS/CFT).
- [[relative-entropy-qft]] — Araki-Uhlmann relative entropy is well-defined on the type III₁ boundary algebras and connects to gravitational generalised entropy via the [[crossed-product-construction]].
- [[type-iii-algebras-across-areas]] — the holographic side joins flat-space QFT and Rindler as a third home of type III₁.
- [[holographic-bell-program]] (new) — speculative connection asking what specifically the Bell-CHSH machinery says about boundary subalgebras at large $N$.
- [[crossed-product-and-island-formula]] (new) — both involve dressing/regulating a type III₁ algebra; one ends in a generalized entropy, the other in an island.
- [[wormholes-and-quantum-information-qft]] (new) — the wormhole/traversability story of [[2021-kundu-wormholes-holography|Kundu's review]] mapped onto the group's flat-space Bell-CHSH, relative-entropy, and embezzlement programs via the TFD = two-wedge identification.
- [[gravity-qi-open-problems]] (new) — [[2026-goto-rethinking-qi-gravity-fields|Goto et al.'s]] gravity/QI open-problems agenda mapped onto the group's OQP roadmap and toolkit; an independent, holography-side confirmation that operational characterization and QI in infinite dimensions are the live frontiers.
- 2026 Algebraic-QFT course (Estrutura Algébrica da Teoria Quântica de Campos) — Semester II of the AQFT course covers Witten 2022 / CPW / AAJ, which use exactly the large-$N$ type III₁ structure of this area as their starting point.
