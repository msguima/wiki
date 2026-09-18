---
title: Condensation Defects
type: concept
areas: [confinement-duality, condensed-matter-connections]
aliases: [condensation defect, higher gauging, non-invertible defects, duality defect, higher-gauging wall]
modified: 2026-07-01
---

## Definition

A **condensation defect** is a topological defect built by **gauging a (higher-form) symmetry on a positive-codimension submanifold** — "higher gauging" (Roumpedakis–Seifnashri–Shao, 2022). Summing over the insertions of a symmetry's charged operators along a wall $Y$ produces an operator supported on $Y$ that is topological but generically **non-invertible**: its fusion with its orientation reversal is a projector,
$$D \times \bar D \ \propto\ \sum_{\text{sector}} (\dots) \ =\ \text{projector},$$
so no inverse defect exists. The Kramers–Wannier duality defect (fusion $D\times\bar D = 1 + \eta$) is the simplest example; condensation defects are the general family.

Higher gauging interpolates between two familiar operations: gauging on all of spacetime (an ordinary orbifold) and inserting an invertible symmetry operator (gauging on a codimension-1 wall of an already-gauged theory). The intermediate cases — gauging a $p$-form symmetry on a $q$-dimensional submanifold — generate the non-invertible symmetries now organizing much of the field.

## Role in Research

Condensation defects are the modern target the generalized-symmetries course is built to reach, and the exact structure the group's **Julia–Toulouse / higher-gauging manuscript** realizes constructively. The manuscript's claim is narrow and load-bearing: the codimension-one higher-gauging wall is not merely posited but *derived* from a restricted [[villain-action|Villain]] defect ensemble. For a charge-$k$ electric condensate in 4d $\mathbb{Z}_N$ BF/Villain theory, the integer electric-brane variable, restricted to a hypersurface $Y$ and reduced mod $N$, is exactly the wall field
$$b = n_Y \bmod N \in C^2(Y, H), \qquad H = \langle k\rangle \subset \mathbb{Z}_N,$$
and the [[julia-toulouse-mechanism|Julia–Toulouse]] sum over restricted residues reproduces the residual higher-form symmetry, the condensation wall, the non-invertible projector fusion, and the endpoint rule for [[wilson-loop|Wilson lines]] crossing the wall. The arithmetic is governed by $d = \gcd(N,k)$ and the annihilator $\mathrm{Ann}(H) \simeq \mathbb{Z}_d$.

This is the clean bridge between the group's older [[confinement-duality|Julia–Toulouse]] language and the modern language of higher-form symmetries, higher gauging, and condensation defects.

## Relations

- [[julia-toulouse-mechanism]] — the defect-condensation mechanism whose restricted ensemble builds the wall
- [[higher-form-symmetries]] — higher gauging = gauging a higher-form symmetry on a submanifold
- [[villain-action]] — the integer brane variable that the wall field is a restriction of
- [[kramers-wannier-duality]] — the duality defect is the simplest condensation defect
- [[wilson-loop]] — endpoint / screening rules for lines crossing the wall
- [[dual-superconductor]] — the physical condensation picture in the pure-gauge case

## Papers

Roumpedakis–Seifnashri–Shao, "Higher gauging and non-invertible condensation defects," Commun. Math. Phys. 401 (2023) 3043 [arXiv:2204.02407]; Choi–Córdova–Hsin–Lam–Shao, arXiv:2111.01139; Shao (TASI), arXiv:2308.00747. The group's manuscript (in preparation, 2026) is the constructive-Villain contribution. See the course bibliography.

## Notes

- The novelty boundary is explicit in the manuscript: the higher-gauging algebra (projector fusion, annihilator selection, quantum-symmetry sectors) is known; the contribution is *deriving the wall field from the restricted Julia–Toulouse/Villain ensemble*, not positing $D_H$ abstractly.
- Bulk condensation (gauging on all of spacetime) versus hypersurface condensation (the codimension-one defect) is the distinction between "gauging a subgroup" and "inserting a condensation wall" — both live in the same Villain ensemble, restricted differently.
- This page is the concept anchor for the companion master-project on condensation defects in $\mathbb{Z}_N$ lattice gauge theory.
