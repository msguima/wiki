---
title: Topological Order
type: concept
areas: [condensed-matter-connections, confinement-duality]
aliases: [topological order, long-range entanglement, anyons, topological entanglement entropy]
modified: 2026-07-01
---

## Definition

**Topological order** is a form of quantum order in gapped phases that lies outside the Landau symmetry-breaking paradigm: distinct phases with the same symmetry, no local order parameter, and a ground-state structure that depends on the topology of space. Its diagnostics:

- **Ground-state degeneracy (GSD)** that depends on the genus of the spatial surface (e.g. $2^{2g}$ for the $\mathbb{Z}_2$ [[toric-code]] on $\Sigma_g$), robust against any local perturbation.
- **Anyons**: pointlike excitations with fractional statistics under braiding, neither bosons nor fermions.
- **Long-range entanglement (LRE)**: the ground state cannot be reached from a product state by a finite-depth local-unitary circuit (Chen–Gu–Wen). This is the sharp definition.
- **Topological entanglement entropy**: the subleading universal constant in $S(A) = \alpha|\partial A| - \gamma + \dots$, with $\gamma = \ln\mathcal{D}$ ($\mathcal{D}$ the total quantum dimension); $\gamma = \ln 2$ for the toric code.

In the generalized-symmetry language, topological order is the **spontaneous breaking of a 1-form symmetry**: the degenerate ground states are the "order parameter," and the symmetry operators wrapping non-contractible cycles act irreducibly on them.

## Role in Research

Topological order is the quantum-information face of the [[confinement-duality]] material: the deconfined phase of a discrete [[lattice-gauge-theory]] *is* a topologically ordered state, and the perturbed [[toric-code]] is the Fradkin–Shenker gauge–Higgs phase diagram read from the other side. It is where the group's [[condensed-matter-connections]] line meets the generalized-symmetries course, and where quantum error correction enters (degeneracy as a protected code space).

- GSD as broken 1-form [[higher-form-symmetries|symmetry]] links it directly to confinement/deconfinement.
- [[string-net-condensation]] gives the microscopic mechanism (condensed electric strings) and the non-abelian generalizations.
- The code-theoretic reading (logical operators as homology classes) connects to quantum information and the group's interests around entanglement.

## Relations

- [[toric-code]] — the paradigmatic exactly solvable topologically ordered model
- [[string-net-condensation]] — the general mechanism producing (doubled) topological orders
- [[higher-form-symmetries]] — topological order as spontaneously broken 1-form symmetry
- [[lattice-gauge-theory]] — the deconfined phase of a discrete gauge theory is topologically ordered
- [[spt-phases]] — the short-range-entangled cousins (protected only with symmetry)

## Papers

Wen (1990, definition and GSD); Kitaev, quant-ph/9707021; Kitaev–Preskill and Levin–Wen (2006, topological entanglement entropy); Chen–Gu–Wen, arXiv:1004.3835 (LRE). See the course bibliography.

## Notes

- Topological order (long-range entangled, stable without symmetry) is sharply distinct from [[spt-phases|SPT order]] (short-range entangled, protected only by symmetry) — the difference is the presence of anyons and topological degeneracy.
- "Intrinsic" topological order (toric code, FQHE) has anyons in the bulk; the FQHE Laughlin state is the experimentally realized example, with charge-$e/3$ anyons at $\nu = 1/3$.
