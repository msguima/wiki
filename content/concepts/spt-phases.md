---
title: SPT Phases
type: concept
areas: [condensed-matter-connections, confinement-duality]
aliases: [SPT, symmetry-protected topological phase, symmetry-protected topological order, Haldane phase, Dijkgraaf-Witten]
modified: 2026-07-01
---

## Definition

A **symmetry-protected topological (SPT) phase** is a gapped phase with a unique symmetric ground state on any closed manifold — trivial in the bulk — but a **protected boundary** (degeneracy, gaplessness, or an anomalous edge realization) that the symmetry cannot remove. Unlike [[topological-order]], an SPT is short-range entangled: it can be deformed to a product state by a finite-depth local-unitary circuit, but not by one that respects the symmetry.

Key facts:

- The **edge realizes the symmetry anomalously** — the same 't Hooft anomaly by inflow: an SPT in $d+1$ dimensions is the bulk whose boundary carries a $d$-dimensional anomaly (see [[t-hooft-anomaly]]).
- Bosonic SPTs with symmetry $G$ are largely classified by **group cohomology** $H^{d+1}(G, U(1))$ (Chen–Gu–Liu–Wen). The 1d case $H^2(G,U(1))$ is exactly projective edge representations.
- **Gauging** an SPT produces a **Dijkgraaf–Witten** topological gauge theory with action $\omega \in H^d(G,U(1))$; the two $\mathbb{Z}_2$ theories in 2+1d — [[toric-code]] and double semion — differ by the SPT cocycle and hence by anyon self-statistics.

The physical archetype is the **Haldane/AKLT** spin-1 chain: a symmetric bulk gap with protected spin-$\tfrac12$ edge modes.

## Role in Research

SPT phases are the short-range-entangled half of the topological-phases story in the generalized-symmetries course, and the bridge from anomalies to topological order. Via gauging they connect [[spt-phases|protected phases]] to the [[topological-order|topologically ordered]] Dijkgraaf–Witten theories that Block 3 of the course diagonalizes, and via inflow they make [[t-hooft-anomaly|anomalies]] concrete and finite-dimensional. The cluster-state SPT is also a resource for measurement-based quantum computation, a point of contact with [[condensed-matter-connections]] and quantum information.

## Relations

- [[t-hooft-anomaly]] — the protected edge realizes a 't Hooft anomaly (inflow)
- [[topological-order]] — the long-range-entangled cousin; gauging an SPT yields topological order
- [[toric-code]] — the $\mathbb{Z}_2$ Dijkgraaf–Witten theory obtained by gauging the trivial vs nontrivial SPT
- [[higher-form-symmetries]] — higher-group and higher-form generalizations of SPT protection

## Papers

Chen–Gu–Liu–Wen, arXiv:1106.4772 (group-cohomology classification); Dijkgraaf–Witten, Commun. Math. Phys. 129 (1990) 393; Haldane (1983), Affleck–Kennedy–Lieb–Tasaki (1987). See the course bibliography.

## Notes

- "Protected" is the operative word: remove the symmetry and the SPT is trivial. This is the sharp contrast with intrinsic topological order, which is stable with no symmetry at all.
- The group-cohomology classification is not the whole story (beyond-cohomology / invertible-field-theory refinements exist), but it captures the cases the course uses.
