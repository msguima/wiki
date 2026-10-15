---
title: Entanglement Embezzlement
type: concept
areas: [bell-inequalities-qft, relative-entropy-qft]
aliases: [embezzlement, quantum embezzlement, universal embezzler, embezzling state]
modified: 2026-10-15
---

## Definition

**Entanglement embezzlement** refers to the extraction of entanglement from a resource state while leaving that state almost unchanged. Concretely: given a resource state shared between Alice and Bob, embezzlement is a protocol by which they produce a target entangled state $|\psi\rangle_{A'B'}$ by local operations alone, with no communication, and return the resource in a state that differs from the original by arbitrarily little. The figure of merit is the **embezzlement error**, the worst case over target states of a fixed dimension, and a state is called **embezzling** when that error can be made arbitrarily small.

**van Dam and Hayden (2003)** showed that in finite dimensions there are families of "universal embezzling states" from which any target state can be extracted with an error that goes to zero as the dimension of the resource grows. No finite member of the family does the job exactly.

In **quantum field theory** the local algebras are [[type-iii-von-neumann-algebras|type III₁ factors]], and van Luijk, Stottmeister, Werner and Wilming (2024) proved that such factors are **universal embezzlers**: *every* normal state on a type III₁ factor is an embezzling state, the vacuum included. The precise statement is that the optimal worst-case error is zero as an **infimum** — for every $\varepsilon>0$ and every finite-dimensional target there is a protocol reaching it within $\varepsilon$ while disturbing the resource by less than $\varepsilon$ — and no single finite protocol attains it. Embezzlement in QFT is therefore arbitrarily accurate rather than exact, and the quantifier is where the physics sits.

Algebraically the mechanism is **Connes–Størmer transitivity**: on a type III₁ factor the unitary orbit of a faithful normal state is norm-dense in the normal state space, so any state can be approached by $\omega(U^*\cdot U)$ to any accuracy, with no unitary in the algebra reaching it. Semifinite algebras behave in the opposite way: types I and II host no embezzling state at all, and the worst-case error there stays at its maximal value. Embezzling states live only in type III factors.

What the resource costs is then a question about the $\varepsilon$ dependence, and it is open. The [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] between the resource before and after is the natural accounting, and monotonicity under the local operations is what should bound it from below.

## Role in Research

Entanglement embezzlement in type III₁ algebras is an open research direction listed explicitly in the [[bell-inequalities-qft]] area (Open Problem 1). The specific goal is:

1. **Construct explicit embezzlement protocols** using [[weyl-operators|Weyl operators]] in QFT. The Weyl algebra provides a concrete, computationally tractable framework for writing down the unitary operations implementing embezzlement. Gaussian displacements alone will not do it — the symplectic invariants of a Gaussian state obstruct universality — so the protocol has to leave the Gaussian family.

2. **Quantify the cost of a given accuracy** via [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]]. The question is how the relative entropy between the pre- and post-protocol resource states scales with the error $\varepsilon$ and with the dimension of the target, and whether the scaling can be computed in the Weyl operator language.

3. **Connect to Bell violations**: both maximal [[bell-chsh-inequality|Bell-CHSH]] violation on complementary wedges and universal embezzlement follow from the same type III₁ structure. Whether they are quantitatively linked — whether a more efficient embezzlement protocol implies a larger violation — is an open question.

Two PhD students in the group are working on this topic.

## Relations

- [[type-iii-von-neumann-algebras]] — universal embezzlement is a consequence of the type III₁ structure, and embezzling states exist only in type III factors; semifinite algebras have none
- [[araki-uhlmann-relative-entropy]] — the information-theoretic accounting for the cost of a protocol at fixed accuracy, bounded through monotonicity
- [[crossed-product-construction]] — the type II$_\infty$ algebra it produces is semifinite, so it is not a universal embezzler; it is also where a trace exists and a cost can be computed
- [[weyl-operators]] — explicit protocols in QFT are being constructed in the Weyl algebra; the Gaussian sector alone is not enough
- [[bell-chsh-inequality]] — the sibling consequence of type III₁; the quantitative link is open
- [[tomita-takesaki-modular-theory]] — modular theory is the tool behind the density of the unitary orbit, and the flow of weights is what the classification of embezzlers runs through
- [[rindler-wedges]] — the natural bipartite split for studying embezzlement in QFT: Alice holds the right wedge algebra, Bob the left

## Papers

- van Luijk, Stottmeister, Werner, Wilming, *Relativistic quantum fields are universal entanglement embezzlers* [arXiv:2401.07292], and *Embezzlement of entanglement, quantum fields, and the classification of von Neumann algebras* [arXiv:2401.07299] — the theorem and its operator-algebraic setting.
- van Dam, Hayden, *Universal entanglement transformations without communication*, Phys. Rev. A 67 (2003) 060302 — the finite-dimensional families.
- Leung, Wang, *Characteristics of universal embezzling families*, Phys. Rev. A 90 (2014) 042331 — optimality in finite dimensions.
- Derived in the AQFT course: [[week-12-type-III1-classification-of-qft-algebras]] §4.6, which states the quantifiers, and [[week-09-reeh-schlieder-and-local-algebras]].

See [[bell-inequalities-qft]] for the group's paper list; explicit embezzlement papers are in preparation.

## Notes

- The term "embezzlement" is evocative: one "steals" entanglement without the resource state "noticing". The mechanism is the density of the unitary orbit in an infinite algebra, not a conservation loophole.
- **Arbitrarily accurate is not exact.** "Zero error" in the theorem means an infimum equal to zero, not a protocol that attains it. Any claim that embezzlement in QFT is exact, or free, drops the quantifier that makes the statement a theorem — and with it the cost question that the group's [[embezzlement-cost-relative-entropy|cost]] and [[embezzlement-capacity-lower-bound|capacity]] questions are about.
- In finite dimensions embezzlement needs a growing Hilbert space. In QFT the local algebras are already type III₁, which is why every state in them is embezzling; what is still finite, and still to be computed, is the price of a fixed accuracy.
- **Gravity makes the algebra semifinite.** The [[crossed-product-construction|crossed product]] that dresses a type III₁ algebra into type II$_\infty$ restores a trace, and a semifinite algebra hosts no embezzling state. So the dressed algebra is not a universal embezzler, and the $\varepsilon$-dependent cost is what survives the dressing — which is exactly why the crossed product is the arena in which the cost becomes computable.
- **Physical origin** ([[2025-liu-lectures-entanglement-vna]]): Liu's $N$-spin chain shows the local algebra passing from type I at finite $N$, where the error is bounded away from zero, to type III₁ as $N\to\infty$, where the unitary orbit of a faithful normal state becomes dense in the state space. There are then no minimal projections and no "ground floor" from which entanglement cannot be extracted.
