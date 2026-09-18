---
title: "Can we establish quantum information theory in infinite-dimensional settings (QFT)?"
type: question
status: open
areas: [relative-entropy-qft, bell-inequalities-qft, gauge-gravity-duality]
priority: high
originated: 2026-06-30
---

## Statement

Problem 5.1 (the sole problem of Theme 4) of [[2026-goto-rethinking-qi-gravity-fields|Goto et al.]]: *what are the appropriate mathematical toolsets and arguments for canonically extending quantum information theory to infinite-dimensional settings, such as those encountered in QFT?* Finite-dimensional QI leans on density matrices, von Neumann entropy, and Schmidt decomposition — none of which survive intact on the [[type-iii-von-neumann-algebras|type III₁]] (and, after regularization, type II) von Neumann algebras that describe local regions in QFT and gravity.

## Why It Matters

This is, almost verbatim, the algebraic frontier the group's whole current program sits on — the single most on-target problem in the paper. Every one of the group's active tools is a partial answer to it: [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] is *finite* precisely where von Neumann entropy diverges; [[entanglement-embezzlement|embezzlement]] is native to type III₁; the [[crossed-product-construction|crossed product]] restores a trace by promoting III₁ to type II. That the holography/QI community independently names this as *the* open problem of infinite-dimensionality is strong outside validation of the group's bet.

## What We Know

- Local algebras in QFT are hyperfinite type III₁; individual entropies are UV-divergent but *differences* (relative entropy, mutual information) are finite and well-defined (Araki, Uhlmann; the group's 2025 papers compute them explicitly for coherent/squeezed/cat states).
- The crossed product regularizes III₁ to type II, restoring a (renormalized) trace and a finite generalized entropy (Witten 2022, CPW, CLPW).
- Embezzlement of entanglement is possible on type III₁ with vanishing standard-monotone cost (van Luijk–Stottmeister–Werner–Wilming 2024; the group's embezzlement line).
- The [[bell-chsh-inequality|Bell-CHSH]] / Tsirelson story in infinite dimensions carries genuine subtleties (commuting-operator vs. tensor models) — see the Tsirelson thread below.

## Possible Approaches

- Frame the group's existing finite-quantity results (relative entropy across dimensions, squeezed/cat states, embezzlement rate) as a coherent contribution to this program — see [[relative-entropy-embezzlement-as-infinite-dim-qi]].
- Push one-shot / smooth-entropy and resource-theoretic tools (Tomamichel-style) onto type II crossed-product windows — the tooling already flagged in [[embezzlement-capacity-lower-bound]].
- Isolate where the tensor-factorization failure genuinely changes an operational number — see [[tsirelson-problem-vacuum-bell-chsh]].

## Related Questions

- [[relative-entropy-embezzlement-as-infinite-dim-qi]], [[tsirelson-problem-vacuum-bell-chsh]]
- [[relative-entropy-interacting-theories]], [[embezzlement-cost-relative-entropy]], [[embezzlement-capacity-lower-bound]]
- [[free-states-and-operations-for-resource-theory-in-qft]], [[qft-correlators-as-information-tasks]]
