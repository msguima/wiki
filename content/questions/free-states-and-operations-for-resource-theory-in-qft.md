---
title: "How should free states/operations be chosen for resource theories in QFT?"
type: question
status: open
areas: [relative-entropy-qft, bell-inequalities-qft]
priority: medium
originated: 2026-06-30
---

## Statement

Problem 2.5 of [[2026-goto-rethinking-qi-gravity-fields|Goto et al.]]: to build a resource theory in QFT one must fix a class of free operations $\mathcal{O}$, but the choice is subtle — it must respect locality, causality, and sometimes spacetime symmetry. Natural candidates are operations localized in spacetime regions (i.e. maps on the [[type-iii-von-neumann-algebras|von Neumann algebras]] of those regions), possibly with classical communication.

## Why It Matters

This is resource theory phrased in exactly the group's language: operations on local algebras, causal constraints, modular structure. The group's [[entanglement-embezzlement|embezzlement]] and [[araki-uhlmann-relative-entropy|relative-entropy]] work implicitly picks free operations (Weyl/Gaussian, causal); making that choice explicit is a natural way to systematize the [[quantum-information-in-infinite-dimensions]] program.

## What We Know

- In finite-dim QI, LOCC / separable / PPT operations define entanglement resource theories.
- In QFT the analog must be algebra-preserving and causal; "causal operations" and "operations with compact spacetime support" are the paper's suggested classes.
- The group already works with a *de facto* free class (Weyl operators, Bogoliubov/Gaussian maps).

## Possible Approaches

- Fix a causal free-operation class on wedge/diamond algebras and identify the induced resource (entanglement? coherence? athermality?).
- Tie the free class to the split property (which supplies an intermediate type-I factor and a tensor structure).

## Related Questions

- [[resource-theory-monotones-in-qft]], [[holographic-resource-theory]], [[resource-theory-of-renormalization-group-flow]]
- [[quantum-information-in-infinite-dimensions]], [[embezzlement-cost-relative-entropy]]
