---
title: "Condensed Matter Connections: Topological Materials and Effective Field Theories"
type: area
status: historical
modified: 2026-07-01
---

## Overview

This is a historical research line — active mainly from 2014 to 2022 — that applies quantum field theory techniques to topological condensed matter systems: topological insulators, Weyl semimetals, and topological superconductors. The line is dormant as an active primary focus, but the formal structures it developed (effective field theories for topological phases, axionic electrodynamics, monopole operators) remain relevant and feed into the 2026 revival of the [[confinement-duality|Julia-Toulouse and generalized symmetries]] program.

Condensed matter systems serve as theoretical laboratories for QFT methods: the collective dynamics of electrons in a crystal lattice can realize field-theoretic phenomena — anomalies, topological order, duality — in a setting where they are experimentally accessible. The research in this line moves in both directions: importing QFT tools (duality, effective field theories, [[axionic-electrodynamics|axionic electrodynamics]]) to understand topological materials, and using the condensed matter setting to sharpen and test QFT techniques.

The central topics are: (1) the effective electromagnetic description of Weyl superconductors via a dynamical pseudo-axion field; (2) monopole (disorder) operators and multivalued fields in topological superconductors; and (3) the topological magnetoelectric effect in topological insulators.

## Key Results

### Weyl Superconductors and Axionic Electrodynamics

- **Massive photon propagator via axionic fluctuations** (Phys. Rev. B 103, 2021; 4 citations): Microscopic derivation from a fermionic model of Weyl superconductors showing that the relative phase between Weyl nodes acts as a dynamical pseudo-axion field. Integrating out the fermions generates [[axionic-electrodynamics|axionic electrodynamics]], which modifies the photon propagator to acquire a mass in a topologically non-trivial way — distinct from the standard Higgs or Proca mechanisms.
- **PhD thesis of Breno Chrispim (2022)**: "Weyl superconductor with dynamical pseudo-axion field: an interplay between high-energy and condensed matter physics." Full microscopic and effective-field-theory treatment of the Weyl superconductor problem.
- **PhD thesis of Rodrigo Bruni (2021)**: "Effective electromagnetic description of Weyl superconductors." Alternative approaches to the electromagnetic effective theory.

### Topological Superconductors and Monopole Operators

- **Multivalued fields and monopole operators in topological superconductors** (Ann. Phys. 419, 2020; 2 citations): Application of the multivalued field formalism (related to the [[julia-toulouse-mechanism|Julia-Toulouse mechanism]]) to construct disorder (monopole) operators that create vortex configurations in the order parameter. These operators are the duals of the standard local order parameter fields and are essential for describing the topological phase.
- **Effective field theories for systems with multiple Fermi surfaces** (Ann. Phys. 374, 2016; 8 citations): Systematic derivation of effective electromagnetic theories for superconducting systems with multiple Fermi surfaces, a situation relevant to Weyl superconductors and multi-band superconductors.

### Topological Insulators

- **Undergraduate thesis supervision on the topological magnetoelectric effect** (Breno Chrispim, 2015): Introduction to θ-electrodynamics as the effective description of the topological magnetoelectric effect (TME) in topological insulators — where an applied electric field induces magnetic polarization via the bulk θ-term.
- **Duality and effective theories for topological materials** (Pedro Braga, Master's thesis 2014; PhD thesis 2018): Systematic application of duality methods and effective field theory to topological insulators and superconductors.

## Open Problems

This line is currently dormant, but the following questions remain open and may be revisited within the generalized symmetries program:

1. **Generalized symmetries in topological phases**: Modern higher-form and non-invertible symmetry language provides a unifying framework for classifying topological phases. Connecting the effective theories developed in this line to this framework is a natural direction. The generalized-symmetries course (`wiki/courses/generalized-symmetries-course/`) develops the toolkit — [[topological-order]], the [[toric-code]], [[string-net-condensation]], [[spt-phases]], and [[higher-form-symmetries]] — from the ground up, tying this line's monopole/disorder-operator formalism to [[condensation-defects]] and the Julia–Toulouse revival.
2. **[[julia-toulouse-higher-form-symmetries|Julia-Toulouse condensation in topological superconductors]]**: Whether the topological phase transitions in Weyl superconductors can be understood as spontaneous breaking of higher-form symmetries via the Julia-Toulouse mechanism. See [[julia-toulouse-meets-generalized-symmetries]].
3. **Entanglement structure of topological phases**: The tools from the [[bell-inequalities-qft|quantum information program]] (modular theory, relative entropy, Bell inequalities) may be applicable to the many-body ground states of topological materials. See [[condensed-matter-qft-bridge]].
4. **[[non-invertible-symmetries-mcs|Non-invertible symmetries in (2+1)d topological theories]]**: Maxwell-Chern-Simons and BF theories in (2+1)d — central to both this line and the [[confinement-duality]] line — are known to possess non-invertible symmetries; their physical consequences in the topological material context are unexplored.

## Key Concepts

- **Weyl semimetals**: Crystalline materials with linearly dispersing bulk energy bands that cross at isolated Weyl points in the Brillouin zone. Near each Weyl point the low-energy physics is that of a massless Weyl fermion. The chiral anomaly, [[axionic-electrodynamics|axionic electrodynamics]], and anomalous Hall effect are hallmarks.
- **Topological superconductors**: Superconductors with topologically non-trivial bulk gap and topologically protected gapless surface states (e.g., Majorana modes). The effective field theory involves multivalued order parameter fields and monopole operators.
- **[[axionic-electrodynamics|Axionic electrodynamics]]**: Electrodynamics modified by a term θ(x) E·B in the Lagrangian. When θ is a dynamical axion (or pseudo-axion) field, as in Weyl superconductors, this produces a topologically non-trivial, massive photon spectrum.
- **Topological magnetoelectric effect (TME)**: In topological insulators, a static θ = π bulk θ-term causes an applied electric field to induce a magnetic polarization and vice versa — the hallmark of the topological insulator phase at the level of electromagnetic response.
- **Monopole operators**: Non-local (disorder) operators that create vortex or monopole configurations in the order parameter field. They are the natural operators to insert in topological phases where the order parameter field is multivalued. Dual to the standard local operators, they are the condensed matter analog of 't Hooft operators.
- **[[julia-toulouse-mechanism|Julia-Toulouse mechanism]]**: The field-theoretic procedure for deriving effective theories from defect condensation. In the condensed matter context, condensation of vortices drives the transition from a superfluid to an insulating phase, and condensation of monopoles (in 3+1d) can drive confinement.

## Key Papers

| Paper | Journal | Year | Citations |
|-------|---------|------|-----------|
| Effective field theories for systems with multiple Fermi surfaces | Ann. Phys. 374 | 2016 | 8 |
| Massive photon propagator in Weyl superconductors via axionic fluctuations | Phys. Rev. B 103 | 2021 | 4 |
| Multivalued fields and monopole operators in topological superconductors | Ann. Phys. 419 | 2020 | 2 |
| Vanishing DC holographic conductivity from magnetic monopole condensate | JHEP | 2015 | — |

## Connections

- **[[confinement-duality]]**: The deepest connection in the portfolio. The [[julia-toulouse-mechanism|Julia-Toulouse mechanism]], [[axionic-electrodynamics|axionic electrodynamics]], and monopole operator formalism were all developed in the [[confinement-duality|confinement and duality line]] and then applied to condensed matter systems. The 2026 revival of the Julia-Toulouse program through generalized symmetries is expected to deepen this connection. See [[julia-toulouse-meets-generalized-symmetries]].
- **[[gribov-zwanziger]]**: Shared formal structures — effective field theories in strongly coupled gauge systems, dimension-two condensates, the interplay of topology and gauge symmetry — connect this line to the Gribov-Zwanziger program.
- **[[condensed-matter-qft-bridge]]**: The main connection page for the cross-disciplinary links between relativistic QFT methods and condensed matter physics in this portfolio.
- **[[bell-inequalities-qft]]**: Tools developed in the quantum information program (modular theory, type III algebras) may apply to many-body ground states of topological materials. See [[entanglement-probes-of-phases]].

### Collaborators

- Pedro R. Braga — topological superconductors, monopole operators (Master's and PhD student)
- Breno Chrispim — Weyl superconductors, [[axionic-electrodynamics|axionic electrodynamics]] (undergrad through PhD)
- Rodrigo Bruni — effective electromagnetic descriptions (PhD student)
- Clóvis Wotzasek (UFRJ) — effective field theory methods; PhD advisor and long-term collaborator
- Diego R. Granado — topological materials
