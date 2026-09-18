---
title: Research Landscape Overview
type: overview
modified: 2026-04-06
---

# Research Landscape Overview

## Current Focus

The central theme of the current research program is quantum information in quantum field theory — specifically, whether operationally meaningful information-theoretic quantities can serve as probes of non-perturbative physics. This sits at the intersection of algebraic QFT, relativistic quantum information, and the theory of operator algebras, and it represents a significant departure from purely perturbative approaches to field-theoretic questions.

The longest-running active line concerns Bell inequalities in QFT, with 21+ papers produced since 2023. The core technical approach uses Weyl operators to construct CHSH-type observables in relativistic settings, bypassing the measurement-interpretation difficulties that arise when naively applying quantum mechanical Bell tests to field states. Tomita-Takesaki modular theory plays a central structural role: the modular Hamiltonian and modular flow provide a canonical way to relate algebras associated to different spacetime regions, and the Bisognano-Wichmann theorem connects this abstract structure to the physical Lorentz boosts in Minkowski space. The guiding physical question is whether the degree of Bell violation — or its suppression — encodes information about the vacuum structure, phase, or confinement properties of the theory.

A closely related line opened in 2025 concerns Araki-Uhlmann relative entropy for excited states in QFT. Relative entropy is the natural information-theoretic distance between states on a von Neumann algebra, and in the type III₁ setting relevant to QFT it has special properties (notably, it is always well-defined even when states are not mutually absolutely continuous in a classical sense). The immediate focus is on computing relative entropy for coherent, squeezed, and cat states in specific field-theoretic models, and on understanding how the quantity changes under the RG flow or when a mass gap is present. An emerging priority is the connection between embezzlement of entanglement and relative entropy: in type III₁ algebras, embezzlement can occur at zero cost, and making this precise in terms of relative entropy is an active open problem being pursued with PhD student Ismael Porfirio Jr.

## Research Areas

**[[bell-inequalities-qft|Bell inequalities in QFT]]** is the main active line. It combines the Weyl-operator formalism for constructing Bell observables, modular theory for relating spacelike-separated algebras, and explicit computation in model field theories (free scalar, Dirac field, gauge theories). The question of whether the Gribov horizon affects Bell violation — by modifying the propagator and hence the two-point structure — is one of the highest-priority open questions.

**[[relative-entropy-qft|Relative entropy in QFT]]** is an active line since 2025 focused on Araki-Uhlmann relative entropy. The algebraic definition is essential here: unlike the density-matrix formula familiar from quantum mechanics, the Araki-Uhlmann formula applies directly to states on type III₁ algebras where density matrices do not exist. The connection to embezzlement and to the modular Hamiltonian provides links back to the Bell inequalities line.

**[[gribov-zwanziger|Gribov-Zwanziger framework]]** represents the historical core of the research program. The Gribov problem — the failure of the Faddeev-Popov gauge fixing to be globally valid in non-Abelian gauge theories — is resolved in the Gribov-Zwanziger and Refined Gribov-Zwanziger (RGZ) approaches by restricting the path integral to the first Gribov region. This modifies the gluon propagator at low momenta and leads to a soft breaking of BRST symmetry, with implications for confinement.

**[[confinement-duality|Confinement and duality]]** covers the Julia-Toulouse mechanism, the dual superconductor picture of confinement, and MCS duality. This area is experiencing a 2026 revival through the lens of generalized symmetries: center symmetry and its higher-form generalizations provide a modern framework for understanding confinement order parameters, and the Julia-Toulouse approach to defect condensation connects naturally to this language.

**[[condensed-matter-connections|Condensed matter connections]]** captures the cross-disciplinary work on topological materials, Weyl semimetals, and axionic electrodynamics. The chiral anomaly and axion electrodynamics appear in both high-energy and condensed matter contexts, and methods developed for confinement (such as topological field theory descriptions of phases) transfer directly.

**Gauge/gravity duality (exploratory).** Not a primary research line but adjacent to the active programs. The AdS/CFT course (syllabus) is the wiki's main artefact here, treating [adscft.org](https://adscft.org/) as the primary text and adding framing, notation alignment, and the type-III₁ / modular-flow connections to the [[bell-inequalities-qft]] and [[relative-entropy-qft]] programs. See [[gauge-gravity-duality]].

## Key Themes Across Areas

**Non-perturbative methods.** The unifying technical challenge across almost all areas is that the physics of interest — confinement, vacuum entanglement structure, the effect of the Gribov horizon — is intrinsically non-perturbative. Algebraic QFT provides a framework that does not rely on perturbation theory; the Gribov-Zwanziger approach is a non-perturbative modification of the gauge-fixed action; modular theory is exact. The research program is broadly oriented around finding quantities that are both computable and sensitive to non-perturbative effects.

**Entanglement as a physical probe.** A recurrent hypothesis is that entanglement measures — Bell violation, relative entropy, entanglement entropy — carry physical information that is invisible to local observables or perturbative correlation functions. In the Bell inequalities line this takes the form: does the CHSH value distinguish confined from deconfined phases? In the relative entropy line: does the Araki-Uhlmann relative entropy between the vacuum and an excited state encode the mass gap?

**Algebraic QFT structures.** The mathematical framework of local nets of von Neumann algebras (Haag-Kastler axioms), Tomita-Takesaki theory, and the classification of von Neumann algebras (type I, II, III) runs through the current focus areas. In QFT, local algebras are generically type III₁, which has non-trivial consequences for entanglement (no Schmidt decomposition, embezzlement at zero cost, ill-defined reduced density matrices).

**Type III₁ everywhere.** The same algebraic type appears in flat-space QFT (Rindler wedges, [[bell-inequalities-qft]]), in algebraic models of equilibrium ([[relative-entropy-qft]]), and on the boundary of holographic CFTs at large N ([[gauge-gravity-duality]]). The [[crossed-product-construction]] is the unifying technical bridge; see [[type-iii-algebras-across-areas]] and [[crossed-product-and-island-formula]].

**Duality.** Electric-magnetic duality, S-duality, and the Julia-Toulouse mechanism appear in the confinement and condensed matter lines. The modern language of generalized symmetries — treating symmetry defects as topological operators — provides a unifying framework. This is expected to feed into the confinement-as-entanglement question: generalized symmetry structure constrains the entanglement properties of the vacuum.

## Active Questions

The following question pages represent the highest current priorities:

- [[entanglement-as-confinement-probe]] — Can Bell violation or relative entropy sharply distinguish confined from deconfined phases in a gauge theory? What is the precise role of the Gribov horizon?
- [[embezzlement-cost-relative-entropy]] — In type III₁ algebras, embezzlement occurs at zero relative entropy cost; what does this mean operationally, and how does it manifest in specific QFT models?
- [[bell-inequalities-with-gribov-horizon]] — How does the restriction of the path integral to the first Gribov region modify the two-point Wightman functions, and hence the maximum CHSH value achievable by Weyl-operator observables?

## Recent Activity

This wiki was seeded on 2026-04-06 from the research-knowledge-base. All area pages, concept pages, entity pages, question pages, and connection pages were created at that time. See [[index]] for the full catalog and log for the creation record.
