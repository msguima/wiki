---
title: Traversable Wormholes
type: concept
areas: [gauge-gravity-duality, bell-inequalities-qft, relative-entropy-qft]
aliases: [traversable wormhole, GJW wormhole, Gao-Jafferis-Wall]
modified: 2026-06-04
---

## Definition

A **traversable wormhole** is a Lorentzian geometry connecting two asymptotic regions through a throat that a causal signal (or observer) can actually cross. Classically this is forbidden: keeping the throat open requires defocusing of null geodesics, i.e. $\int T_{kk}\,d\lambda < 0$ along the crossing ray, which violates the **averaged null energy condition (ANEC)**. Any traversable wormhole therefore needs a quantum source of negative null energy.

The modern, controlled realization is the **Gao–Jafferis–Wall (GJW)** construction: starting from the two-sided eternal black hole (whose Einstein–Rosen bridge is non-traversable and is dual to the [[thermofield-double-state|thermofield double]]), one turns on a **double-trace coupling** between the two boundaries,
$$
\delta S = \int dt\; g(t)\, \mathcal{O}_L(t)\,\mathcal{O}_R(t),
$$
which produces a one-loop negative average null energy in the bulk and opens the throat just enough for a signal to pass. The coupling makes the two boundaries *communicate*: it is the bulk dual of a teleportation / Hayden–Preskill protocol.

Two regimes recur:
- **One-shot (GJW):** a brief coupling opens the wormhole transiently; a signal sent in at the right moment emerges on the other side (**regenesis**).
- **Eternal (Maldacena–Qi):** two systems (e.g. two SYK dots) kept permanently coupled have a near-AdS$_2$ ground state that is a *steady-state* traversable wormhole — a renewable entangled resource.

## Role in Research

Traversable wormholes are the sharpest meeting point between the group's algebraic-QFT tools and holographic gravity, for three reasons:

1. **The GJW coupling is a Connes-cocycle perturbation.** $V = g\,\mathcal{O}_L\mathcal{O}_R$ perturbs the modular flow of the [[thermofield-double-state|TFD]] exactly in the manner the group's [[crossed-product-construction|crossed-product]] and [[araki-uhlmann-relative-entropy|relative-entropy]] machinery handles (Ahmad–Jefferson make this precise). A free-field two-wedge analogue with $V = g\,W(f_L)W(f_R)$ is directly computable — see [[relative-entropy-wormhole-opening]].

2. **Traversability versus Bell-CHSH.** A maximal [[bell-chsh-inequality|Bell-CHSH]] violation between two regions presumes their algebras *commute* (no signaling). Opening the wormhole introduces signaling across the throat, so there should be a quantitative tension between traversability and achievable violation — see [[bell-chsh-across-traversable-wormhole]].

3. **A teleportation resource.** Regenesis through the wormhole is a physical channel for moving quantum information, inviting comparison with [[entanglement-embezzlement|embezzlement]] from a [[type-iii-von-neumann-algebras|type III₁]] resource.

This concept anchors Semester II of the algebraic-QFT course (Blocks 4–5: GJW, MSY, AAJ).

## Relations

- Built on the [[thermofield-double-state|thermofield double state]] and the [[er-epr|ER=EPR]] correspondence.
- Requires ANEC violation; contrast with the non-traversable Einstein–Rosen bridge of the eternal black hole.
- Treated algebraically via the [[crossed-product-construction|crossed product]] and Connes cocycle (Ahmad–Jefferson).
- Probed by [[araki-uhlmann-relative-entropy|relative entropy]] and [[bell-chsh-inequality|Bell-CHSH]] in the group's programs.
- Part of the [[gauge-gravity-duality]] area and the [[wormholes-and-quantum-information-qft]] connection.

## Papers

- [[2021-kundu-wormholes-holography]] — §5.2 reviews GJW, Maldacena–Qi, braneworld wormholes, and regenesis.
- Gao, Jafferis, Wall (2017), arXiv:1608.05687 — the original double-trace mechanism.
- Maldacena, Qi (2018), arXiv:1804.00491 — eternal traversable wormhole from coupled SYK.
- Maldacena, Stanford, Yang (2017), arXiv:1704.05333 — bulk "diving in" analysis.
- Ahmad, Jefferson (2025), arXiv:2501.01487 — algebraic / cocycle treatment.

## Notes

The honest scoping point stressed in the course: the *algebra* sees the cocycle-perturbed modular data, but the **Shapiro time advance** and geometric "opening" of the throat are bulk statements the boundary algebra does not directly resolve. Keeping this algebra/bulk demarcation explicit is what makes the wormhole a useful test bed rather than a slogan.
