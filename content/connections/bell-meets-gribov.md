---
title: "Bell Inequalities Meet the Gribov Horizon"
type: connection
areas: [bell-inequalities-qft, gribov-zwanziger]
maturity: developing
modified: 2026-04-06
---

## The Link

The Gribov problem and quantum entanglement in QFT have so far been developed as almost entirely separate programs, but they converge on a concrete and well-posed question: does the restriction of the Yang-Mills path integral to the first [[gribov-horizon|Gribov region]] modify the vacuum entanglement structure and, in particular, Bell-CHSH violations between causally separated regions? This question is not merely formal. The [[gribov-horizon|Gribov horizon]] is a genuine non-perturbative feature of the QCD vacuum — it changes the infrared behavior of propagators, introduces a mass gap, and eliminates gluons from the physical spectrum. If the vacuum state of the Gribov-Zwanziger theory differs non-trivially from the perturbative vacuum, its entanglement across spacelike separated regions should differ too.

A concrete entry point already exists. The 2023 paper at SciPost Phys. 15 produced the first [[brst-symmetry|BRST-invariant]] formulation of Bell-CHSH in gauge theories. This was a necessary prerequisite: in a gauge theory, physical observables must be BRST-closed, and any Bell test must use operators that respect this structure. The [[gribov-zwanziger|Gribov-Zwanziger framework]] possesses its own exact nilpotent BRST symmetry (Phys. Rev. D 92, 2015 — the most cited paper in the portfolio), constructed specifically to survive the restriction to the Gribov region. These two BRST structures — one for the Bell test, one for the Gribov restriction — are the technical ingredients needed to formulate a well-defined Bell test inside the Gribov region.

The deeper physical motivation comes from the [[spectral-positivity-violation|spectral positivity violation]] of the GZ gluon propagator. In the [[refined-gribov-zwanziger|Refined Gribov-Zwanziger (RGZ) theory]], the gluon propagator has complex poles — it cannot describe an asymptotic particle. This is a signal of [[confinement]], and it is encoded in the vacuum state itself. Entanglement measures — Bell-CHSH values, Araki-Uhlmann relative entropy, entanglement entropy — probe the structure of the vacuum state directly. The hypothesis is that the modification induced by the Gribov restriction acts as a deformation of the vacuum entanglement, and that this deformation could either enhance or suppress Bell violations relative to the perturbative (Faddeev-Popov) vacuum. The answer would give a quantum-informational fingerprint of the Gribov physics in the vacuum.

## Evidence

- **BRST-invariant Bell-CHSH** (SciPost Phys. 15, 2023; 4 citations): The direct precursor. Demonstrates that a well-defined, BRST-consistent Bell-CHSH formulation can be constructed for gauge theories. The paper works with the perturbative Faddeev-Popov vacuum, making the Gribov extension the obvious next step.
- **Exact nilpotent BRST for the GZ action** (Phys. Rev. D 92, 2015; 92 citations): Establishes that the GZ theory has the correct BRST structure to define gauge-invariant observables. Without this, one could not construct BRST-closed dichotomic operators inside the Gribov region.
- **Local and BRST-invariant GZ formulation** (Phys. Rev. D 94, 2016; 63 citations): The local auxiliary-field form of the GZ action, which is needed for practical operator calculations and vacuum expectation value computations.
- **Spectral functions and phase structure at the Gribov horizon** (Phys. Rev. D 88, 2013; 27 citations): Shows that the Gribov horizon creates genuinely distinct phase structure in the Yang-Mills-Higgs system, suggesting that entanglement measures could similarly be sensitive to it.
- **GZ as an open direction** (bell-inequalities-qft.md, open problem 2): The research knowledge base explicitly flags "Bell inequalities in gauge theories with Gribov horizon" as a current and future direction of the quantum information program, and similarly the Gribov area file flags this as open problem 3.
- **Weyl operator + Tomita-Takesaki framework** (Phys. Rev. D 108, 085026; 2023; 15 citations): Provides the technical machinery — [[weyl-operators|Weyl operators]] in [[rindler-wedges|Rindler wedges]], modular conjugation J — that would need to be adapted to the GZ vacuum.

## Gaps

The fundamental gap is the lack of any computation of vacuum expectation values of [[weyl-operators|Weyl operators]] in the Gribov-Zwanziger vacuum, as opposed to the perturbative vacuum. The standard formula ⟨0|W(f)|0⟩ = exp(−½‖f‖²) holds for the Fock vacuum of a free field theory. In the GZ theory, the vacuum is not a simple Fock vacuum: the horizon function generates non-trivial correlations, and the gluon propagator is deformed to a form with complex poles. Computing ⟨Ω_GZ|W(f)|0⟩ requires either:

1. A coherent state or variational characterization of the GZ vacuum state, which does not yet exist in the literature.
2. A perturbative expansion around the GZ action, retaining the leading Gribov corrections to the two-point function and their effects on the Weyl operator vacuum expectation value.

A second gap is conceptual: it is not obvious how to define Alice's and Bob's operator algebras inside the Gribov region. The [[tomita-takesaki-modular-theory|Tomita-Takesaki modular theory]] applies to abstract von Neumann algebras, but the Gribov restriction introduces non-local constraints (the Faddeev-Popov operator must be positive definite everywhere) that may not commute cleanly with the local algebra structure assumed in the Rindler-wedge construction.

A third gap is whether the Gribov parameter γ (the Gribov mass, fixed self-consistently by the horizon condition) introduces any explicit dependence into the Bell-CHSH value, and whether that dependence could be related to an observable physical quantity — for instance, the string tension or glueball mass.

## Potential Projects

1. **Leading-order Gribov correction to Weyl vacuum expectation values**: Compute ⟨W(f)⟩ in the GZ theory at leading order in the Gribov parameter γ², using the modified gluon propagator. This requires evaluating Gaussian integrals with the GZ two-point function, which has a known analytic form (a ratio of polynomials in momentum). The result would give the first estimate of how the Gribov restriction shifts the Bell-CHSH value from its perturbative value.

2. **BRST cohomology of dichotomic operators in the GZ theory**: Systematically classify which linear combinations of [[weyl-operators|Weyl operators]] are BRST-closed in the GZ action with the exact nilpotent BRST of Phys. Rev. D 92, 2015. This is the prerequisite for a gauge-invariant Bell test in the Gribov sector.

3. **Gribov parameter as a Bell inequality deformation parameter**: Study the Bell-CHSH violation as a function of γ, from γ = 0 (perturbative/Faddeev-Popov limit) to γ → ∞ (deep confinement). This would produce a curve B(γ) that could be compared with other known order parameters for confinement, like the string tension or Polyakov loop.

4. **RGZ vacuum and modular structure**: Investigate whether the [[refined-gribov-zwanziger|RGZ]] dimension-two condensates ⟨A^μA_μ⟩ and ⟨φ̄φ⟩ generate a non-trivial modular Hamiltonian for the local algebra in a Rindler wedge. The condensates shift the vacuum energy and could modify the Tomita-Takesaki modular operator Δ at leading order.

5. **Lattice comparison**: Formulate Bell-CHSH observables in a lattice gauge theory setting and study their behavior across the deconfinement transition at finite temperature. This would provide a numerical check of whether Bell violation is sensitive to confinement, independent of the GZ analytic framework.

## Related

### Areas
- [[bell-inequalities-qft]]
- [[gribov-zwanziger]]

### Connections
- [[entanglement-probes-of-phases]]
- [[type-iii-algebras-across-areas]]

### Concepts
- [[bell-chsh-inequality]]
- [[weyl-operators]]
- [[tomita-takesaki-modular-theory]]
- [[gribov-horizon]]
- [[gribov-copies]]
- [[brst-symmetry]]
- [[refined-gribov-zwanziger]]
- [[spectral-positivity-violation]]
- [[rindler-wedges]]
- [[type-iii-von-neumann-algebras]]
- [[confinement]]

### Questions
- [[bell-inequalities-with-gribov-horizon]]
- [[entanglement-as-confinement-probe]]
- [[gribov-copies-physical-observables]]

### Entities
- [[silvio-paolo-sorella]]
- [[david-dudal]]
- [[leticia-palhares]]
