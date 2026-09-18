---
title: Bell Inequalities and Quantum Information in Quantum Field Theory
type: area
status: active
modified: 2026-04-06
---

## Overview

Since 2023 this has become the most active research line, producing 21+ publications. The program investigates [[bell-chsh-inequality|Bell-CHSH]] and [[mermin-inequalities|Mermin]] inequality violations, [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]], and entanglement measures in relativistic quantum field theory. The central formalism is built on [[weyl-operators|Weyl operators]] and [[tomita-takesaki-modular-theory|Tomita-Takesaki modular theory]], which together provide a natural and algebraically rigorous framework for constructing dichotomic observables in causally separated regions.

The foundational physical insight is that the vacuum state of a relativistic QFT is highly entangled across spacelike separated regions — a consequence of the [[type-iii-von-neumann-algebras|type III₁ von Neumann algebra]] structure of local observables. This entanglement can be quantified using tools from algebraic quantum information theory adapted to the QFT setting. The Tsirelson bound 2√2, violated by quantum correlations relative to the classical hidden-variable bound of 2, is achieved or approached in explicit constructions for free scalar, spinor, and vector fields in [[rindler-wedges|Rindler wedges]] and [[causal-diamonds|causal diamonds]].

The line connects directly to the [[relative-entropy-qft|relative entropy program]] launched in 2025, and has growing links to [[gribov-zwanziger|Gribov physics]] and confinement through the question of whether Bell violation measures can serve as probes of phase structure.

## Key Results

- **Maximal violation for massless spinors** (Phys. Rev. D 108, L081701; 2023): Explicit construction achieving the Tsirelson bound 2√2 using bumpified Haar wavelets as test functions. 10 citations.
- **Weyl + Tomita-Takesaki framework** (Phys. Rev. D 108, 085026; 2023): The most cited paper in this line (15 citations). Systematic derivation of Bell-CHSH violations using [[weyl-operators|Weyl operators]] localized in Rindler wedges, with Bob's operators constructed via modular conjugation J from Alice's.
- **Mermin inequalities via Weyl operators** (Phys. Rev. D 109, 045020; 2023): Extension from bipartite to multipartite entanglement, probing genuine multipartite entanglement in the QFT vacuum.
- **BRST-invariant Bell-CHSH in gauge theories** (SciPost Phys. 15, 2023): First formulation compatible with the [[brst-symmetry|BRST symmetry]] structure of gauge-fixed theories.
- **Unruh-De Witt detectors + Tomita-Takesaki** (JHEP 2024; 6 citations): Bridges the particle detector approach with the algebraic modular theory approach.
- **Bell-CHSH in causal diamond regions** (Eur. Phys. J. C 85, 2025): Extends the Rindler-wedge results to compact [[causal-diamonds|causal diamond]] regions, which are more physically accessible.
- **Numerical framework** (Phys. Rev. D 110, 2024; 5 citations): Complements analytical results with systematic numerical evaluation for varying mass, test function choice, and spacetime dimension.
- **Cat states and Bell-CHSH violation** (Phys. Rev. D 113, 065008; 2026): Shows that [[cat-states|cat states]] — superpositions of [[coherent-states|coherent states]] — produce Bell violations with qualitatively new features arising from quantum interference.
- **Class of bounded Hermitian operators** (Phys. Rev. D 112, 2025): Systematic characterization of the operator classes that optimize Bell-CHSH violations in QFT.

## Open Problems

1. **[[entanglement-embezzlement|Entanglement embezzlement]] in QFT**: Exploiting the [[type-iii-von-neumann-algebras|type III₁]] structure to construct explicit embezzlement protocols using [[weyl-operators|Weyl operators]]; quantifying cost via [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]]. See open question [[embezzlement-cost-relative-entropy]].
2. **[[bell-inequalities-with-gribov-horizon|Bell inequalities with Gribov horizon]]**: Whether the presence of the [[gribov-horizon|Gribov horizon]] in non-abelian gauge theories modifies Bell-CHSH violations, connecting this line to [[gribov-zwanziger]].
3. **[[higher-spin-bell-inequalities|Higher-spin and non-abelian extensions]]**: Extending the Weyl operator formalism beyond free scalar and Proca fields to higher-spin fields and non-abelian gauge theories.
4. **[[impossible-measurements-qft|Impossible measurements in QFT]]**: The limitations of ideal sharp measurements in relativistic settings and how they affect Bell-type arguments.
5. **[[entanglement-as-confinement-probe|Entanglement as a probe of confinement]]**: Using Bell-CHSH violation and relative entropy as order parameters or indicators for confinement phase transitions in gauge theories.

## Key Concepts

- **[[bell-chsh-inequality|Bell-CHSH inequality]]**: The upper bound ≤ 2 on correlations between causally separated measurements under local hidden-variable theories. Quantum correlations can reach the Tsirelson bound 2√2.
- **[[weyl-operators|Weyl operators]]**: Unitary operators W(f) = exp(iφ(f)) built from smeared field operators. They generate the local von Neumann algebra and provide a natural family of dichotomic operators for QFT Bell tests. Vacuum expectation values ⟨0|W(f)|0⟩ = exp(−½‖f‖²) are computable in closed form for free fields.
- **[[tomita-takesaki-modular-theory|Tomita-Takesaki modular theory]]**: Given a von Neumann algebra M and a cyclic separating vector Ω, the modular operator Δ and conjugation J encode the geometry of the algebra relative to the state. The modular conjugation J maps the algebra of the right Rindler wedge to that of the left, providing a systematic way to construct Bob's operators from Alice's.
- **[[rindler-wedges|Rindler wedges]] and [[causal-diamonds|causal diamonds]]**: The natural causal regions for locating Alice's and Bob's observables. Rindler wedges are complementary half-spaces; causal diamonds are compact double-cone regions, both key in algebraic QFT.
- **[[type-iii-von-neumann-algebras|Type III₁ von Neumann algebras]]**: Local algebras in QFT are of this type, which means the standard von Neumann entropy is ill-defined but [[araki-uhlmann-relative-entropy|relative entropy]] remains well-defined and finite. The type III₁ structure is also responsible for the [[entanglement-embezzlement|embezzlement]] phenomenon.
- **[[mermin-inequalities|Mermin inequalities]]**: Multipartite generalizations of Bell-CHSH that probe genuine multipartite entanglement in the QFT vacuum.
- **[[coherent-states|Coherent states]], [[squeezed-states|squeezed states]], [[cat-states|cat states]]**: Families of excited states for which Bell-CHSH violations and relative entropy are computed explicitly.

## Key Papers

| Paper | Journal | Year | Citations |
|-------|---------|------|-----------|
| Weyl operators and Tomita-Takesaki for Bell-CHSH violations | Phys. Rev. D 108, 085026 | 2023 | 15 |
| Maximal Bell violation for massless spinors via Haar wavelets | Phys. Rev. D 108, L081701 | 2023 | 10 |
| Unruh-De Witt detectors and Bell-CHSH + Tomita-Takesaki | JHEP 2024 | 2024 | 6 |
| Numerical approach to Bell-CHSH | Phys. Rev. D 110 | 2024 | 5 |
| BRST-invariant Bell-CHSH in gauge theories | SciPost Phys. 15 | 2023 | 4 |
| Mermin inequalities via Weyl operators | Phys. Rev. D 109, 045020 | 2023 | 2 |
| Bell-CHSH in causal diamond regions | Eur. Phys. J. C 85 | 2025 | — |
| Class of bounded Hermitian operators for Bell-CHSH | Phys. Rev. D 112 | 2025 | — |
| Bell-CHSH review in relativistic QFT | Rev. Phys. 13 | 2025 | — |
| Cat states and Bell-CHSH violation | Phys. Rev. D 113, 065008 | 2026 | — |
| [[2025-liu-lectures-entanglement-vna\|Lectures on entanglement, von Neumann algebras, and emergence of spacetime]] (review) | preprint (arXiv:2510.07017) | 2025 | — |

## Connections

- **[[relative-entropy-qft]]**: The relative entropy program is a direct outgrowth of this line, applying the same Weyl operator and modular theory machinery to compute [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]] between excited states and the vacuum.
- **[[gribov-zwanziger]]**: The [[bell-meets-gribov|Bell meets Gribov]] connection explores whether the [[gribov-horizon|Gribov horizon]] modifies vacuum entanglement in non-abelian gauge theories. See [[bell-inequalities-with-gribov-horizon]].
- **[[type-iii-algebras-across-areas]]**: The [[type-iii-von-neumann-algebras|type III₁ algebra]] structure is the algebraic backbone of both this area and the relative entropy area, and connects to condensed matter through operator algebraic methods.
- **[[entanglement-probes-of-phases]]**: The broader program of using entanglement measures as probes of quantum phase transitions, including confinement.
- **[[condensed-matter-qft-bridge]]**: Shared mathematical structures (modular theory, type III algebras, operator algebraic entanglement) appear in both relativistic QFT and many-body condensed matter systems.
- **[[wormholes-and-quantum-information-qft]]**: Because the Minkowski vacuum on two complementary wedges is a [[thermofield-double-state|thermofield double]], the Bell-CHSH toolkit is a calculable model of the holographic wormhole's boundary data. Opens the sharp question [[bell-chsh-across-traversable-wormhole|whether traversability degrades the Tsirelson violation]] (from [[2021-kundu-wormholes-holography|Kundu's review]]).
- **[[gravity-qi-open-problems]]**: [[2026-goto-rethinking-qi-gravity-fields|Goto et al.'s]] gravity/QI open-problems agenda flags the **Tsirelson problem** (tensor vs. commuting-operator correlations) as the infinite-dimensional obstruction behind nonlocal games — exactly the commuting-wedge-algebra setting of [[bell-in-type-iii-project]] and the ceiling on [[long-range-bell-decay|vacuum Bell-CHSH]].

### Collaborators

- [[silvio-paolo-sorella]] ([[uerj]]) — co-author of all papers
- [[itzhak-roditi]] ([[cbpf]]) — co-author of 14 papers
- [[david-dudal]] ([[ghent-university]]) — 3 papers
- ismael-porfirio ([[uerj]]) — PhD student; entanglement embezzlement in type III₁ algebras
- erick-landim ([[uerj]]) — PhD student; von Neumann algebras, embezzlement, many-body theory
- luigi-carvalho-ferreira ([[uerj]]) — postdoc (CNPq fellowship)
