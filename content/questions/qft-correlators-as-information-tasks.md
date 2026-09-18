---
title: "Can we reformulate QFT correlators in terms of information-theoretic tasks?"
type: question
status: open
areas: [relative-entropy-qft, gauge-gravity-duality]
priority: medium
originated: 2026-06-30
---

## Statement

Problem 2.3 of [[2026-goto-rethinking-qi-gravity-fields|Goto et al.]]: *can we reformulate QFT correlators in terms of information-theoretic tasks?* The paper notes that task feasibility is bounded by entropic quantities — e.g. the optimal type-II error exponent in hypothesis testing is the relative entropy (quantum Stein's lemma), and mutual information bounds how much local randomness a region can share.

## Why It Matters

The quantum Stein's lemma reading is a direct operational handle on the group's central quantity: [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] *is* the optimal asymptotic distinguishability rate between two states. Casting the group's closed-form relative-entropy results (coherent/squeezed/cat states vs. vacuum) as **state-discrimination tasks** would give them an operational meaning and feed [[relative-entropy-embezzlement-as-infinite-dim-qi]].

## What We Know

- Quantum Stein's lemma: relative entropy = optimal type-II error exponent in asymmetric hypothesis testing (finite dim; the infinite-dim/type III₁ version is exactly the [[quantum-information-in-infinite-dimensions]] frontier).
- The group has explicit Araki–Uhlmann values for many state pairs; their operational (discrimination-rate) interpretation is available but not yet emphasized.
- Correlators ↔ mutual information ↔ shared randomness is standard in QI but under-exploited in the QFT program.

## Possible Approaches

- Restate the 2025 relative-entropy results as vacuum-vs-excited discrimination-rate statements; check the infinite-dimensional Stein's-lemma caveats.
- Bound specific smeared correlators by mutual information between regions.

## Related Questions

- [[quantum-information-in-infinite-dimensions]], [[relative-entropy-embezzlement-as-infinite-dim-qi]]
- [[resource-theory-monotones-in-qft]], [[relative-entropy-interacting-theories]]
