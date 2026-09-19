---
title: Can Bell-CHSH and relative entropy techniques probe holographic spacetime structure?
type: question
status: open
areas: [bell-inequalities-qft, relative-entropy-qft]
priority: low
originated: 2026-04-07
---

## Statement

The [[subregion-subalgebra-duality]] in AdS/CFT identifies bulk spacetime regions with emergent [[type-iii-von-neumann-algebras|type III₁]] boundary subalgebras --- the same algebraic setting in which Marcelo's [[weyl-operators|Weyl operator]] Bell-CHSH tests and [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]] computations operate. Can these tools, developed for flat-space QFT, be applied to holographic boundary theories to extract information about bulk causal structure, spacetime connectivity, or gravitational entropy?

## Why It Matters

The [[bell-inequalities-qft|Bell inequality program]] and [[relative-entropy-qft|relative entropy program]] have developed a sophisticated and computationally tractable framework for probing entanglement in type III$_1$ algebras using Weyl operators and [[tomita-takesaki-modular-theory|Tomita-Takesaki modular theory]]. If this framework can be adapted to holographic CFTs, it would provide new computable probes of bulk geometry. In particular:

- Bell-CHSH violations between boundary subregions could detect whether the corresponding bulk regions are causally connected or disconnected.
- Relative entropy between boundary states could provide a direct algebraic route to the gravitational entropy, bypassing the Ryu-Takayanagi area formula.
- The [[crossed-product-construction|crossed product construction]] connecting type III$_1$ (boundary) to type II$_\infty$ (gravitational) could be tested by comparing relative entropy computations at the two levels.

## What We Know

- [[hong-liu|Liu's]] review ([[2025-liu-lectures-entanglement-vna]]) establishes that boundary subalgebras in the large $N$ limit are type III$_1$ and that modular flows generate bulk geometric flows.
- The algebraic ER=EPR proposal identifies spacetime connectivity with algebraic commutant structure, suggesting that entanglement measures (Bell violations, relative entropy) between boundary regions encode bulk topology.
- For free-field QFT in flat space, the Bell-CHSH and relative entropy techniques are well-developed and yield explicit results. In holographic CFTs, the boundary theory is strongly coupled, making direct computation far more difficult.
- The [[crossed-product-construction|crossed product construction]] provides a bridge between relative entropy (type III$_1$) and gravitational entropy (type II$_\infty$), but explicit computations have been done only in limited settings (JT gravity, static observers).

## Possible Approaches

1. **Large $N$ free-field models.** Consider holographic CFTs in limits where the boundary theory simplifies (e.g., generalized free fields at large $N$), and compute Bell-CHSH violations and relative entropy using the Weyl operator formalism adapted to the boundary. Compare with known bulk geometric data.

2. **Thermofield double state.** The thermofield double state in a holographic CFT is dual to the two-sided eternal black hole. The left and right boundary algebras are type III$_1$ factors. Apply the Weyl operator Bell test to these complementary algebras and study how the Bell violation depends on the black hole temperature (which controls the entanglement).

3. **Relative entropy and RT formula.** Compute [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]] between states on a boundary subregion algebra and compare with the bulk generalized entropy. The modular Hamiltonian for ball-shaped regions in CFTs is known explicitly (Casini-Huerta-Myers), which could make the computation tractable.

4. **Toy models.** Use 2d holographic CFTs or tensor network models (where the type III$_1$ structure is approximated by large but finite systems) to test whether Bell-CHSH violations between boundary subregions detect bulk connectivity changes (e.g., phase transitions in the RT surface).

## Related Questions

- [[embezzlement-cost-relative-entropy]] --- the crossed product provides a framework for computing embezzlement cost, which is also related to gravitational entropy
- [[relative-entropy-interacting-theories]] --- applying relative entropy to holographic (strongly coupled) theories requires going beyond free fields
- [[type-iii-algebras-across-areas|type III structure in gauge theories]] --- the type III$_1$ classification in gauge theories with Gribov restriction is an analogous structural question

This question is tracked under the exploratory [[gauge-gravity-duality]] area and is the originating question for the [[holographic-bell-program]] connection page.
