---
title: Toric Code
type: concept
areas: [condensed-matter-connections, confinement-duality]
aliases: [toric code, Kitaev toric code, surface code, quantum double]
modified: 2026-07-01
---

## Definition

The **toric code** (Kitaev, 1997) is the simplest exactly solvable model of [[topological-order]]: qubits on the links of a square lattice, with a commuting-projector Hamiltonian
$$H = -\sum_v A_v - \sum_p B_p,\qquad A_v = \prod_{\ell\ni v}\sigma^x_\ell,\quad B_p = \prod_{\ell\in\partial p}\sigma^z_\ell,$$
where $A_v$ (star) and $B_p$ (plaquette) all commute. The ground space is their common $+1$ eigenspace.

Its structure, solvable to the bone:

- **Degeneracy** $2^{2g}$ on a genus-$g$ surface (4 on the torus), labelled by the eigenvalues of non-contractible Wilson/'t Hooft loops.
- **Anyons**: $e$ (star violation), $m$ (plaquette violation), and $\varepsilon = e\times m$; $e$ and $m$ are mutual semions (braiding phase $-1$), $\varepsilon$ is a fermion.
- **String operators** create anyon pairs at their ends; only topologically non-trivial (non-contractible) strings connect distinct ground states.

The toric code is exactly the $\mathbb{Z}_2$ **Kogut–Susskind** [[lattice-gauge-theory|lattice gauge theory]] in its deconfined phase: $A_v = 1$ is the Gauss law, $B_p$ the magnetic energy. It is also the $\mathbb{Z}_2$ Dijkgraaf–Witten theory and the $\mathbb{Z}_2$ [[string-net-condensation|string-net]].

## Role in Research

In the generalized-symmetries course the toric code is where confinement/deconfinement, generalized symmetry, and quantum information become one object: its 4-fold torus degeneracy is spontaneously broken 1-form [[higher-form-symmetries|symmetry]], its anyons are the electric and magnetic charges of $\mathbb{Z}_2$ gauge theory, and its ground space is a quantum error-correcting code (the surface code). The perturbed toric code reproduces the Fradkin–Shenker phase diagram, tying Semester I to Semester II.

- As a **code**: logical operators are homology classes of $H_1(\Sigma,\mathbb{Z}_2)$; code distance = shortest non-contractible loop; no local operator acts within the code space (Dennis–Kitaev–Landahl–Preskill).
- Topological entanglement entropy $\gamma = \ln 2$ is computed by an explicit Schmidt decomposition.

## Relations

- [[topological-order]] — the toric code is its exactly solvable representative
- [[lattice-gauge-theory]] — the toric code is deconfined $\mathbb{Z}_2$ Kogut–Susskind theory
- [[higher-form-symmetries]] — its degeneracy is broken 1-form symmetry; anyons are charged objects
- [[string-net-condensation]] — the toric code is the $\mathbb{Z}_2$ string-net
- [[wilson-loop]] — the non-contractible loop operators that label the ground states

## Papers

Kitaev, "Fault-tolerant quantum computation by anyons," Annals Phys. 303 (2003) 2 [quant-ph/9707021]; Dennis–Kitaev–Landahl–Preskill, quant-ph/0110143 (the code). See the course bibliography.

## Notes

- "Toric" refers to the torus used to expose the degeneracy; on a planar patch with boundaries the same model is the **surface code**, the leading platform for fault-tolerant quantum computing.
- The $\mathbb{Z}_N$ generalization (clock/shift qubits) and the non-abelian quantum double $D(G)$ extend the construction; $D(S_3)$ already has non-abelian anyons.
