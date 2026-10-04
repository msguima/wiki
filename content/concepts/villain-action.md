---
title: Villain Action
type: concept
areas: [confinement-duality, condensed-matter-connections]
aliases: [Villain form, Villain model, periodic Gaussian, modified Villain]
modified: 2026-10-04
---

## Definition

The **Villain action** replaces a periodic (cosine) interaction by a sum of Gaussians over integer shifts, preserving the $2\pi$-periodicity of a compact variable while making the theory exactly dualizable. For a compact scalar,
$$e^{\beta\cos(\Delta\theta)} \ \longrightarrow\ \sum_{n\in\mathbb{Z}} e^{-\frac{\beta}{2}(\Delta\theta - 2\pi n)^2},$$
and for a $U(1)$ gauge field the plaquette term becomes $\frac{\beta}{2}\sum_p (da - 2\pi n)^2$ with an integer 2-cochain $n$. The integer field $n$ is what carries the topology: its coboundary $dn$ is the vortex (scalar) or monopole (gauge) current.

The Villain form matters because **every duality in abelian lattice theory is one manipulation** on it — Poisson resummation of $n$, followed by solving the resulting current-conservation constraint on the dual lattice. This is the engine behind the XY → Coulomb-gas map, the compact-QED₃ dual photon, and the Banks–Myerson–Kogut duality of 4d $U(1)$.

**Modified Villain** (Sulejmanpasic–Gattringer; Gorantla–Lam–Seiberg–Shao) promotes $n$ to a dynamical $\mathbb{Z}$ gauge field with a flatness constraint $dn = 0$. This removes the defects by a constraint instead of summing them, yielding *exact* higher-form symmetries, exact self-dualities, and well-defined $\theta$-terms on a finite lattice — not just in the continuum limit.

## Role in Research

The Villain action is the computational backbone of Semester I of the generalized-symmetries course, and in Semester II it carries the course's bridge to [[condensation-defects]]. Restricted to a surface, a charge-$k$ Villain condensate gives in its London limit the condensation sheet of higher gauging, whose field is $-k$ times the matter current reduced mod $N$; in four dimensions the field of a higher-gauging wall is the restricted Villain integer reduced mod $N$, a reparametrization that by itself assigns no weight to the lines on the wall. The group's manuscript in preparation keeps the ordinary Villain form, rather than the modified one, for its microscopic regulator, because monopole worldlines are the candidate source of the cost it gives to those lines, and its current–clock duality is a periodic-Gaussian self-duality. See [[condensation-defects]] and [[julia-toulouse-mechanism]].

- It makes the [[dual-superconductor]] and monopole-plasma pictures of confinement exact statements rather than approximations.
- The modified-Villain version supplies the exact lattice backgrounds needed to see [[t-hooft-anomaly|'t Hooft anomalies]] and [[higher-form-symmetries|higher-form symmetries]] without a continuum limit.

## Relations

- [[lattice-gauge-theory]] — the Villain form is the abelian corner where lattice gauge theory dualizes exactly
- [[kramers-wannier-duality]] — the same Poisson-resummation engine, applied to the Ising/scalar case
- [[julia-toulouse-mechanism]] — defect condensation described through the Villain integer field
- [[condensation-defects]] — a charge-$k$ Villain condensate restricted to a surface gives the condensation sheet in the London limit
- [[higher-form-symmetries]] — modified Villain carries these exactly on the lattice

## Papers

Villain, J. Physique 36 (1975) 581; José–Kadanoff–Kirkpatrick–Nelson (1977); Banks–Myerson–Kogut (1977); Sulejmanpasic–Gattringer (2019); Gorantla–Lam–Seiberg–Shao, arXiv:2103.01257. See the course bibliography.

## Notes

- Villain is not merely an approximation to the cosine: at large $\beta$ the two flow together, and for extracting topological (duality, symmetry) data the Villain form is the *correct* starting point, not a convenience.
- The whole point of "modified Villain" is that the ordinary Villain theory has a monopole/vortex-summing sector that breaks the would-be higher-form symmetry; constraining it restores the symmetry exactly.
