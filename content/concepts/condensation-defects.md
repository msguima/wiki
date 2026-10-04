---
title: Condensation Defects
type: concept
areas: [confinement-duality, condensed-matter-connections]
aliases: [condensation defect, higher gauging, non-invertible defects, duality defect, higher-gauging wall]
modified: 2026-10-04
---

## Definition

A **condensation defect** is a topological defect built by **gauging a (higher-form) symmetry on a positive-codimension submanifold** — "higher gauging" (Roumpedakis–Seifnashri–Shao, 2022). Summing the symmetry's own operators over a network on a closed submanifold $Y$, with a normalization, produces an operator supported on $Y$ that is topological but generically **non-invertible**: it fuses with its orientation reversal into itself times a decoupled factor,
$$S \times \bar S = Z(Y)\,S,$$
where $Z(Y)$, the partition function on $Y$ of the gauge theory of the condensed group, depends on the normalization chosen for $S$, and no inverse defect exists. In $2+1$d $\mathbb{Z}_N$ gauge theory, summing the Wilson lines of a subgroup $H$ on a closed surface gives a sheet with $Z(\Sigma_g)=|H|^{2g-1}$ in the course's normalization. One dimension lower, gauging $\mathbb{Z}_2$ on a closed curve of the Ising model gives $1+\eta$, which is what the Kramers–Wannier duality defect fuses into, $D\times\bar D=1+\eta$. Duality defects come from gauging on half of spacetime at a self-dual point, condensation defects from gauging on a closed submanifold, and both are non-invertible.

Gauging a symmetry on all of spacetime produces a new theory; gauging it on a closed submanifold of positive codimension, when the restricted symmetry is free of anomaly, produces a defect inside the original theory. Gauging a $p$-form symmetry on submanifolds of the various dimensions this allows generates many of the non-invertible symmetries now organizing the field.

## Role in Research

Condensation defects are the modern target of the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]] and the setting of the group's manuscript in preparation, *Finite-Cost Currents at Higher-Gauging Walls in Four-Dimensional $\mathbb{Z}_N$ Gauge Theory*. Its object is the wall obtained by gauging a subgroup $H=\langle k\rangle\subset\mathbb{Z}_N$ of the electric 1-form symmetry on a closed three-dimensional hypersurface $Y$,
$$D_H(Y)=\frac{1}{\mathcal N_Y}\sum_{S\in Z_2(Y;H)}U[S],$$
a sum over closed $H$-labelled sheet networks. A charge-$q$ [[wilson-loop|Wilson line]] crosses the wall intact exactly when $q\in\mathrm{Ann}(H)\simeq\mathbb{Z}_r$, with $r=\gcd(N,k)$; any other line meets the wall at a junction, and a line along the wall carrying the endpoint charge $q$ mod $N/r$ joins it to a partner junction. The manuscript takes this surface sum, its charge filter and its fusion as prior work (Roumpedakis–Seifnashri–Shao; Choi–Córdova–Hsin–Lam–Shao; Bah–Leung–Waddleton, the closest construction). What it adds is a cost per unit length for the lines along the wall, motivated by the activation cost that the [[julia-toulouse-mechanism|Julia–Toulouse]] picture keeps for proliferating defects. An exact character transform turns these lines into a $\mathbb{Z}_{N/r}$ clock model in which a Wilson–wall junction is a local clock operator. The clock phases decide whether junctions are confined along the wall, and at large cost the tension between junctions, per unit cost, tends to $\bar\alpha/2$, where $\bar\alpha$ is the smallest absolute value of an integer representing the endpoint charge.

The restricted [[villain-action|Villain]] ensemble is a result of the course rather than of the manuscript: in $2+1$ dimensions a charge-$k$ condensate restricted to a surface reproduces, in its London limit, the condensation sheet of higher gauging. Together these results connect the group's older [[confinement-duality|Julia–Toulouse]] language with the modern language of higher-form symmetries, higher gauging and condensation defects.

## Relations

- [[julia-toulouse-mechanism]] — the defect-condensation picture that motivates a finite cost for the lines along the wall
- [[higher-form-symmetries]] — higher gauging = gauging a higher-form symmetry on a submanifold
- [[villain-action]] — a charge-$k$ Villain condensate restricted to a surface gives the condensation sheet in the London limit
- [[kramers-wannier-duality]] — the duality defect fuses into the simplest condensation defect, $1+\eta$
- [[wilson-loop]] — the charge filter and the endpoint rule for lines crossing the wall
- [[dual-superconductor]] — the physical condensation picture in the pure-gauge case

## Papers

Roumpedakis–Seifnashri–Shao, "Higher gauging and non-invertible condensation defects," Commun. Math. Phys. 401 (2023) 3043 [arXiv:2204.02407]; Choi–Córdova–Hsin–Lam–Shao, Phys. Rev. D 105 (2022) 125016 [arXiv:2111.01139] and Commun. Math. Phys. 402 (2023) 489 [arXiv:2204.09025]; Bah–Leung–Waddleton, JHEP 09 (2026) 272 [arXiv:2506.04346]; Shao (TASI), arXiv:2308.00747. The group's manuscript (in preparation; version of 2026-09-20) contributes the finite-cost line sector. See the course bibliography.

## Notes

- The novelty boundary is explicit in the manuscript: the subgroup surface sum, its filter and its fusion are prior work, and the contribution is the line sector at a fixed charge filter, "the endpoint prescription with a fixed crossing filter, the resulting observable dictionary, and the uniform bound on the stable charge cost." It does not derive the line weight from a continuum condensate; that derivation, the relation of the wall tension to a complete Wilson observable and the full topological worldvolume amplitude are among its open problems.
- Bulk condensation (gauging on all of spacetime: a new theory, in which the lines outside $\mathrm{Ann}(H)$ are no longer genuine) versus hypersurface condensation (a defect of the original theory, at which those lines end on junctions) is the distinction between "gauging a subgroup" and "inserting a condensation wall"; the exact sequence $0\to\mathrm{Ann}(H)\to\mathbb{Z}_N\to\widehat H\to0$ organizes both.
- This page is the concept anchor for the companion master-project on condensation defects in $\mathbb{Z}_N$ lattice gauge theory.
