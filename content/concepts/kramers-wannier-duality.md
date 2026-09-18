---
title: Kramers-Wannier Duality
type: concept
areas: [condensed-matter-connections, confinement-duality]
aliases: [Kramers-Wannier, order-disorder duality, disorder operator, Kadanoff-Ceva]
modified: 2026-07-01
---

## Definition

**Kramers–Wannier duality** is the exact map of the 2d Ising model onto itself that exchanges high and low temperature. High-temperature graphs of one lattice are the low-temperature domain walls of the dual lattice; the self-dual point $\sinh(2\beta_c) = 1$ locates the critical temperature $\beta_c = \tfrac12\ln(1+\sqrt2)$ without solving the model.

The duality is cleanest in operator language:

- The **order variable** $\sigma_x$ (site spin) has $\langle\sigma\sigma\rangle$ long-ranged at low $T$.
- The **disorder variable** $\mu_{\tilde x}$ (Kadanoff–Ceva), living on dual sites, creates a domain-wall seam; $\langle\mu\mu\rangle$ is long-ranged at high $T$.
- They obey a mutual non-locality: $\sigma_x \mu_{\tilde y} = \pm\, \mu_{\tilde y}\sigma_x$, the sign set by whether the seam crosses $x$. The composite $\sigma\mu$ is a lattice fermion.

## Role in Research

Kramers–Wannier is the first appearance in the generalized-symmetries course of the thread "a duality is a statement about a wall." In the modern reading it is **gauging a $\mathbb{Z}_2$ symmetry**: summing over $\mathbb{Z}_2$ backgrounds maps the theory to its orbifold, and at the self-dual point the duality is implemented by a topological **defect line** whose fusion is a projector — a non-invertible symmetry. This is the ancestor of the [[condensation-defects]] the group's Julia–Toulouse construction produces.

- The disorder operator $\mu$ is the direct 2d ancestor of the 't Hooft/monopole disorder operators of [[lattice-gauge-theory]].
- Reading the duality as gauging connects it to the general $\mathbb{Z}_N^{(p)} \to \mathbb{Z}_N^{(d-p-2)}$ quantum-symmetry rule of [[higher-form-symmetries]].

## Relations

- [[villain-action]] — the same Poisson-resummation engine executes both the Ising and the XY duality
- [[higher-form-symmetries]] — Kramers–Wannier as gauging a 0-form symmetry, producing the dual (quantum) symmetry
- [[condensation-defects]] — the self-dual duality defect is the simplest non-invertible / condensation defect
- [[lattice-gauge-theory]] — Wegner's $\mathbb{Z}_2$ gauge theory is the gauged version, self-dual in 3d

## Papers

Kramers–Wannier, Phys. Rev. 60 (1941) 252; Kadanoff–Ceva, Phys. Rev. B 3 (1971) 3918; Aasen–Mong–Fendley, arXiv:1601.07185 (the duality defect on the lattice). See the course bibliography.

## Notes

- Tracking boundary conditions honestly (periodic vs antiperiodic, spin structures) is where the subtleties live; the naive self-dual statement hides how the duality acts on the different sectors.
- The order/disorder algebra is the 2d shadow of a general fact: symmetry operators and the objects they act on are mutually non-local extended operators.
