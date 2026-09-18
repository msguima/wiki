---
title: Entanglement Embezzlement
type: concept
areas: [bell-inequalities-qft, relative-entropy-qft]
aliases: [embezzlement, quantum embezzlement]
modified: 2026-04-06
---

## Definition

**Entanglement embezzlement** refers to the extraction of entanglement from a resource state while leaving the resource state approximately (or exactly) unchanged. Concretely: given a resource state $\rho_{AB}$ shared between Alice and Bob, embezzlement is a protocol by which they can create a target entangled state $|\psi\rangle_{A'B'}$ using only local operations and classical communication (LOCC), without significantly disturbing $\rho_{AB}$.

**van Dam and Hayden (2003)** showed that in finite-dimensional systems there exist "universal embezzling states" from which any target entangled state can be approximately extracted, with approximation error going to zero as the embezzling state dimension grows.

In **infinite-dimensional quantum field theory** with [[type-iii-von-neumann-algebras|type III₁ local algebras]], embezzlement becomes **exact**: one can extract a maximally entangled state from the vacuum with zero perturbation to the state. This is a consequence of the equivalence of all faithful normal states on a type III₁ factor — there are no "minimal" states from which nothing can be extracted, and global unitaries can achieve exact state transfers.

Algebraically, exact embezzlement in type III₁ algebras follows from the fact that for any two normal faithful states $\omega$ and $\varphi$ on a type III₁ factor $\mathcal{M}$, there exists a unitary $U \in \mathcal{M}$ such that $\varphi(\cdot) = \omega(U^*\cdot U)$ — any state can be rotated into any other by a unitary in the algebra.

The cost of embezzlement can be bounded in terms of [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]]: in type III₁ algebras, the relative entropy cost can be zero for exact embezzlement.

## Role in Research

Entanglement embezzlement in type III₁ algebras is an open research direction listed explicitly in the [[bell-inequalities-qft]] area (Open Problem 1). The specific goal is:

1. **Construct explicit embezzlement protocols** using [[weyl-operators|Weyl operators]] in QFT. The Weyl algebra provides a concrete, computationally tractable framework for writing down the unitary operations implementing embezzlement.

2. **Quantify the (zero) cost** via [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]]. Since the relative entropy between the pre- and post-embezzlement states should vanish for exact protocols, one wants to verify this explicitly in the Weyl operator language.

3. **Connect to Bell violations**: embezzlement maximizes entanglement, which should push Bell-CHSH violations toward the Tsirelson bound. Understanding the quantitative relationship between embezzlement efficiency and Bell violation is an open question.

PhD students ismael-porfirio and erick-landim are working on this topic.

## Relations

- [[type-iii-von-neumann-algebras]] — exact embezzlement (as opposed to approximate) is a feature of type III₁ algebras; in type I algebras it is only approximate and requires infinite-dimensional resource states
- [[araki-uhlmann-relative-entropy]] — the cost of embezzlement is zero (measured by relative entropy) in type III₁; relative entropy provides the information-theoretic accounting
- [[weyl-operators]] — explicit embezzlement protocols in QFT are being constructed using the Weyl algebra; Gaussian states are particularly tractable
- [[bell-chsh-inequality]] — embezzlement extracts maximal entanglement, which is connected to maximal Bell violation; understanding this quantitative link is an open problem
- [[tomita-takesaki-modular-theory]] — modular theory is the algebraic tool that enables the state rotation argument underlying exact embezzlement
- [[rindler-wedges]] — the natural bipartite split for studying embezzlement in QFT: Alice holds the right wedge algebra, Bob the left wedge algebra

## Papers

See [[bell-inequalities-qft]] for full paper list. Explicit embezzlement papers are in preparation.

## Notes

- The term "embezzlement" is evocative: one "steals" entanglement without the resource state "noticing." The mathematical mechanism is the structure of infinite-dimensional (type III) algebras where approximate or exact state equivalences allow this.
- In finite-dimensional quantum computing, embezzlement requires growing Hilbert space dimensions. In QFT the local algebras are already infinite-dimensional and type III₁, so embezzlement is essentially "free."
- The distinction between exact and approximate embezzlement is sharp: type I (finite-dimensional) → approximate only; type II → approximate with logarithmically diverging cost; type III₁ → exact with zero cost.
- Recent work by Witten and collaborators on gravity has connected the type II structure of gravitational algebras (in the large-$N$ limit) to a version of approximate embezzlement with finite cost, which serves as a probe of black hole information puzzles.
- **Physical origin of type III₁ and embezzlement** ([[2025-liu-lectures-entanglement-vna]]): Liu's review provides a physically transparent explanation of why type III₁ algebras enable exact embezzlement. Through a concrete $N$-spin entangled chain example, Liu shows how the local algebra transitions from type I (finite $N$, where embezzlement is only approximate) to type III₁ ($N \to \infty$, where all faithful normal states become equivalent). In the type III₁ limit, there are no minimal-rank projections and no "ground floor" from which entanglement cannot be extracted --- every state has infinite entanglement with the complement, and local unitaries can redistribute this entanglement without any detectable cost. This makes the abstract mathematical statement ("all faithful normal states on a type III₁ factor are unitarily equivalent") physically intuitive.
- **Crossed product and embezzlement cost** ([[2025-liu-lectures-entanglement-vna]]): The [[crossed-product-construction|crossed product construction]] $\hat{\mathcal{M}} = \mathcal{M} \rtimes_\sigma \mathbb{R}$, which promotes a type III₁ algebra to type II$_\infty$, provides a framework for assigning a finite entropy cost to embezzlement. In the type II$_\infty$ crossed product, a semifinite trace exists and von Neumann entropy is well-defined, so an embezzlement protocol lifted from $\mathcal{M}$ to $\hat{\mathcal{M}}$ acquires a quantifiable cost. This is directly relevant to Ismael Porfirio's PhD work and to the open question [[embezzlement-cost-relative-entropy]].
