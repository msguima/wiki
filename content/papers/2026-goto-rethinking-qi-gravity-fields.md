---
title: "Rethinking quantum information in gravity and fields"
type: paper
authors: [Goto, Hamada, Kato, Mori, Nakata, Watanabe, Yamasaki, Yamazaki, Yoda]
year: 2026
arxiv: "2606.30853"
areas: [gauge-gravity-duality, bell-inequalities-qft, relative-entropy-qft]
status: preprint
---

## Summary

A **position / open-problems paper** by a nine-author collaboration of Japanese theorists (Goto, Hamada, Kato, Mori, Nakata, Watanabe, Yamasaki, Yamazaki, Yoda; RIKEN iTHEMS, Osaka, KEK, Nagoya, Rikkyo, Science Tokyo, YITP, U. Tokyo, Kyoto), curating research questions at the intersection of **quantum gravity and quantum information**. It is not a research paper reporting theorems: it is a deliberately chosen list of problems the authors regard as important for *both* communities, written to get the two fields talking to each other.

The discussion is organized into **four themes**:

1. **Operational characterization of observables** (§2) — can gravitational/holographic observables (quantum extremal surfaces, dressed bulk operators, correlators) be characterized *operationally*, via the information-processing tasks they enable, rather than by fiat? Sub-questions connect OTOCs to channel capacity, apply resource theories to holography, formalize bulk causality as the "connected wedge theorem," and ask where genuine quantum-gravity effects give a computational advantage.
2. **The role of observers** (§3) — what reference structure is needed to define an observable in quantum gravity; are observers emergent, fundamental, or descriptive artifacts; what are the fundamental (complexity-theoretic, state-dependent) limits on an observer's access to the bulk; and how does a *dynamical* observer backreact on the semiclassical geometry and on the observable algebra?
3. **Quantum error correction** (§4) — refining the Hayden–Preskill toy model toward realistic black-hole physics, and asking whether *full* quantum-information protection is even required in quantum gravity (approximate / non-isometric codes).
4. **Infinite-dimensionality of Hilbert spaces** (§5) — the call to **establish quantum information theory in infinite-dimensional Hilbert spaces**, i.e. for the [[type-iii-von-neumann-algebras|type II and type III von Neumann algebras]] that actually appear in QFT and gravity, where standard finite-dimensional QI intuitions (density matrices, von Neumann entropy, Schmidt decomposition) break down.

For this wiki the paper functions as a **second open-problems agenda** — a holography/QI-community companion to the group's own IQOQI Open Quantum Problems triage (the [[long-range-bell-decay-project]] / [[bell-in-type-iii-project]] / [[embezzlement-capacity-project]] roadmap). Its Theme 4 is, almost verbatim, the frontier the group's own programs sit on: [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] as the *finite* information measure on [[type-iii-von-neumann-algebras|type III₁]] algebras, [[entanglement-embezzlement|entanglement embezzlement]] in type III₁, and the [[crossed-product-construction|crossed product]] as the type II regulator. That makes this an unusually high-value external landmark to hold in the wiki.

## Key Results

*(This is a position paper; the "results" below are the open problems it curates, grouped by theme. Problem numbering follows the paper's four sections.)*

**Theme 1 — Operational characterization of observables (§2).**

- Whether gravitational observables (extremal surfaces, dressed bulk operators) can be *characterized operationally* by the boundary tasks or information-processing capabilities they support.
- Reformulating QFT correlators as information-theoretic tasks; connecting **OTOCs** and scrambling to **channel capacity**.
- Bulk causality as boundary information-processing — the **connected wedge theorem** relating bulk causal structure to preshared correlations and nonlocality on the boundary.
- Importing **resource theories** (free operations, free states, monotones) into holography and QFT — e.g. RG flow / $c$- and $a$-theorems as monotones; "holographic LOCC."
- Identifying tasks where genuine **quantum-gravity** effects provide a computational advantage.

**Theme 2 — The role of observers (§3).**

- What reference structure is required before an observable is even definable in quantum gravity.
- Whether observers are emergent, fundamental, or descriptive artifacts.
- Fundamental limits on an observer's access to the bulk: complexity-theoretic obstructions (Harlow–Hayden decoding, **Python's Lunch**) and state-dependent reconstruction (Papadodimas–Raju mirror operators).
- **Backreaction of a dynamical observer** on semiclassical geometry and on the observable algebra — the crossed-product / CLPW "observer's algebra" made type II by a bounded-below observer Hamiltonian.
- Measurement theory incorporating stringy (non-local) interactions.

**Theme 3 — Quantum error correction (§4).**

- Refining the **Hayden–Preskill** black-hole toy model toward realistic evaporation and the [[page-curve|Page curve]].
- Whether *full* QI protection is required in gravity, given **non-isometric** bulk-to-boundary maps and only-approximate holographic codes.

**Theme 4 — Infinite-dimensionality of Hilbert spaces (§5).**

- The overarching call to **build a quantum information theory valid in infinite-dimensional Hilbert spaces**, and specifically on the [[type-iii-von-neumann-algebras|type II₁ / type III₁]] von Neumann algebras of QFT and gravity, where von Neumann entropy is UV-divergent and reduced density matrices do not exist.
- Operator-algebra quantum error correction (OAQECC) beyond finite dimension.
- The **Tsirelson problem** (tensor-product vs. commuting-operator correlations; the $\mathrm{MIP}^*=\mathrm{RE}$ resolution) as the sharp infinite-dimensional obstruction lurking behind nonlocal games and Bell correlations.

## Methods

As a survey the paper draws on a wide toolkit rather than deriving one result; the frameworks it leans on are exactly the ones the group and its AQFT/AdS-CFT courses use:

- **Algebraic QFT** — [[type-iii-von-neumann-algebras|type II/III von Neumann algebras]], [[tomita-takesaki-modular-theory|modular theory]], [[causal-diamonds|causal diamonds]], the [[crossed-product-construction|crossed product]].
- **Holography** — [[ryu-takayanagi-formula|RT]] / [[quantum-extremal-surfaces|quantum extremal surfaces]], the [[quantum-extremal-surfaces|island formula]], entanglement-wedge reconstruction and [[subregion-subalgebra-duality|subregion–subalgebra duality]], [[large-n-factorization|large-$N$ factorization]].
- **Operational QI & resource theory** — LOCC, channel capacity, hypothesis testing, entanglement distillation/dilution, state merging, free-operation monotones.
- **Quantum error correction** — code subspaces, holographic/operator-algebra codes, non-isometric codes.
- **Relativistic QI** — Unruh–DeWitt detectors, quantum reference frames, spacetime localization.
- **Complexity theory** — computational indistinguishability, pseudorandom/pseudoentangled states, Harlow–Hayden and Python's-Lunch hardness.
- **Soluble models** — [[jt-gravity|JT gravity]], double-scaled SYK (a gravity dual with a finite-dimensional bulk Hilbert space), celestial holography.

## Relevance

This is the most direct external validation to date of the bet the group's whole current program is placing — that the right information-theoretic quantities on **type III₁ algebras** are the frontier — and it maps cleanly onto the group's OQP roadmap ([[long-range-bell-decay-project]], [[bell-in-type-iii-project]], [[embezzlement-capacity-project]]) and the [[wormholes-and-quantum-information-qft|wormholes ↔ QI thread]].

- **Theme 4 is the group's home turf.** "Establish QI theory in infinite-dimensional Hilbert spaces / type II–III algebras" is precisely what the [[relative-entropy-qft|Araki–Uhlmann relative entropy]] line does (finite where von Neumann entropy diverges), what the [[entanglement-embezzlement|embezzlement]] work does (embezzlement is *native* to type III₁), and what the [[crossed-product-construction|crossed product]] does (promoting III₁ to a traceable type II). The group is already writing chapters of the very program this paper flags as open.
- **The Tsirelson problem ↔ Bell in type III₁.** Theme 4's infinite-dimensional obstruction (tensor vs. commuting-operator correlations) is exactly the distinction at issue in [[bell-in-type-iii-project]] (OQP #1/26/32, Werner/Gill/Gisin) and in whether the vacuum's [[bell-chsh-inequality|Bell-CHSH]] violation saturates Tsirelson on commuting wedge algebras — see also [[long-range-bell-decay]].
- **Theme 1 ↔ embezzlement capacity.** "Characterize holographic observables by the tasks they enable / import resource theory into holography" is the thesis of the group's [[embezzlement-capacity-project|generalized-entropy-as-capacity]] manuscript and the [[embezzlement-capacity-lower-bound|capacity lower-bound]] question: generalized entropy as the *operational capacity* for holographic embezzlement is a concrete instance of the operational characterization this theme asks for.
- **Theme 2 ↔ crossed product / observer.** The dynamical-observer, type-II "observer's algebra" is the CLPW/CPW material of the AQFT course Semester II, and the natural setting for a *physical-observer* version of the group's Bell-CHSH and relative-entropy computations — cf. [[bell-chsh-in-holographic-setting]].
- **Theme 3 ↔ holography scaffolding.** Hayden–Preskill, the [[page-curve|Page curve]], and holographic codes are covered in the [[gauge-gravity-duality|AdS/CFT course]]; this theme is where the group's toolkit is currently a consumer rather than a producer.
- **Meta-point.** An independent, holography-side community explicitly naming "operational characterization" and "QI in infinite dimensions" as the two central frontiers is strong outside confirmation that the group's OQP roadmap is aimed at live, high-attention targets.

## Questions Raised

1. Do the group's *finite* [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] results and its type III₁ [[entanglement-embezzlement|embezzlement]]-rate machinery already constitute publishable pieces of the "QI in infinite dimensions" program (Theme 4)? A short position note framing the 2025 relative-entropy papers + the embezzlement-capacity manuscript against §5 could stake that claim. → [[embezzlement-cost-relative-entropy]], [[relative-entropy-interacting-theories]]
2. Is the **Tsirelson problem** the sharp infinite-dimensional obstruction for vacuum Bell-CHSH in QFT — i.e. does the commuting-operator (wedge-algebra) value differ from any tensor-factorized model, and does that matter for the [[long-range-bell-decay|β(L) decay law]]? → [[bell-in-type-iii-project]]
3. Can "operational characterization of holographic observables via tasks" (Theme 1) be *realized concretely* by proving generalized entropy is the embezzlement capacity — turning a slogan into a theorem? → [[embezzlement-capacity-project]], [[embezzlement-capacity-lower-bound]], [[holographic-dual-embezzlement-protocol]]
4. Does the type-II **observer's algebra** (Theme 2) give a physically-honest home for Bell-CHSH and relative-entropy computations with a bounded-energy observer, sidestepping the [[impossible-measurements-qft|impossible-measurements]] worry? → [[bell-chsh-in-holographic-setting]]

## Problem Pages

Each of the paper's 20 formal problems (Appendix A) has its own [[index|question page]], connected to the group's programs where possible. Priority tags reflect relevance to the group's toolkit, not the paper's own emphasis.

**Theme 1 — Operational characterization (§2)**
- [[operational-characterization-of-gravitational-observables]] (2.1) · [[bulk-causality-and-information-tasks]] (2.2) · [[qft-correlators-as-information-tasks]] (2.3) · [[tasks-with-quantum-gravity-advantage]] (2.4) · [[free-states-and-operations-for-resource-theory-in-qft]] (2.5) · [[resource-theory-monotones-in-qft]] (2.6) · [[resource-theory-of-renormalization-group-flow]] (2.7) · [[holographic-resource-theory]] (2.8)

**Theme 2 — Observer (§3)**
- [[reference-structures-for-observables-in-qg]] (3.1) · [[is-the-observer-emergent]] (3.2) · [[observer-limits-on-bulk-geometry]] (3.3) · [[dynamical-observer-backreaction-and-algebra]] (3.4) · [[measurement-theory-with-stringy-interactions]] (3.5)

**Theme 3 — Quantum error correction (§4)**
- [[refining-the-hayden-preskill-model]] (4.1) · [[many-body-dynamics-for-near-haar-encoding]] (4.2) · [[learning-black-hole-dynamics-from-radiation]] (4.3) · [[qec-features-needed-for-quantum-gravity]] (4.4) · [[swampland-and-holographic-qec]] (4.5) · [[classical-quantum-correspondence-of-holographic-qec]] (4.6)

**Theme 4 — Infinite dimensionality (§5)**
- [[quantum-information-in-infinite-dimensions]] (5.1)

**Group-specific spin-offs** (the group's own research angles on the above)
- [[tsirelson-problem-vacuum-bell-chsh]] · [[relative-entropy-embezzlement-as-infinite-dim-qi]] · [[observer-algebra-bell-chsh]]

## Related Papers

- [[2025-liu-lectures-entanglement-vna]] — Liu's review; the type III₁ / crossed-product machinery this paper's Theme 4 calls to develop.
- [[2021-kundu-wormholes-holography]] — Kundu's wormhole review; the Theme 2–3 bulk (Page curve, traversability, ER=EPR) side.
- Witten (2022), *Gravity and the crossed product* (arXiv:2112.12828) — the type II observer's algebra behind Theme 2 (in Zotero, key KAQN5465).
- Chandrasekaran, Penington, Witten (2023), *Large N algebras and generalized entropy* (arXiv:2209.10454) — CPW; two-sided crossed product, covered in the AQFT course.
- Chandrasekaran, Longo, Penington, Witten (2022), *An algebra of observables for de Sitter space* (arXiv:2206.10780) — CLPW; the observer's algebra as type II₁.
- Hayden, Preskill (2007), *Black holes as mirrors* (arXiv:0708.4025) — the Theme 3 toy model.
- van Luijk, Stottmeister, Werner, Wilming (2024) — embezzlement in QFT / type III₁; background for the group's embezzlement line.

## See Also

- [[gravity-qi-open-problems]] — connection page mapping this agenda onto the group's programs and OQP roadmap.
- [[wormholes-and-quantum-information-qft]], [[type-iii-algebras-across-areas]], [[holographic-bell-program]].
