---
title: Lattice Gauge Theory
type: concept
areas: [confinement-duality, condensed-matter-connections]
aliases: [LGT, Wilson lattice gauge theory, lattice gauge theories]
modified: 2026-07-01
---

## Definition

**Lattice gauge theory** is gauge theory formulated on a discrete spacetime lattice, with the gauge field represented by group-valued variables $U_\ell \in G$ on links rather than a Lie-algebra-valued connection $A_\mu$. It provides a gauge-invariant, nonperturbative regulator and is the natural home for the strong-coupling expansion, duality, and the modern operator view of phases.

The building blocks:

- **Link variables** $U_\ell = \mathcal{P}\exp(i\int_\ell A)$, one per oriented link, transforming as $U_\ell \to g_x U_\ell g_y^\dagger$ under gauge transformations at the endpoints.
- **Plaquette** $U_p = \prod_{\ell\in\partial p} U_\ell$, the smallest Wilson loop; the **Wilson action** $S = -\frac{\beta}{N}\sum_p \mathrm{Re}\,\mathrm{tr}\,U_p$ reduces to $\frac{1}{4}\int F^2$ in the continuum limit.
- **Haar measure** $\prod_\ell dU_\ell$ makes the path integral finite and gauge-invariant with no gauge fixing — the setting for Elitzur's theorem (local symmetries do not break).

Two complementary formulations run through the course: the Euclidean (Wilson) action above, and the Hamiltonian (**Kogut–Susskind**) form $H = \frac{g^2}{2}\sum_\ell E_\ell^2 - \frac{1}{g^2}\sum_p(U_p + U_p^\dagger)$ with the Gauss-law constraint selecting closed electric strings as physical states.

## Role in Research

Lattice gauge theory is the technical spine of Semester I of the generalized-symmetries course and the concrete setting for the group's [[confinement-duality]] revival. Its diagnostics — the [[wilson-loop]] area law, the string tension, the [[villain-action|Villain]] dualities — are exactly the objects that the modern [[higher-form-symmetries|higher-form symmetry]] language reinterprets, and the lattice is where the group's Julia–Toulouse/higher-gauging construction is most explicit (see [[condensation-defects]]).

- Strong-coupling expansion gives confinement (area law) for any compact group as a controlled calculation.
- The abelian cases dualize exactly (Villain form), producing the monopole pictures of confinement ([[dual-superconductor]], [[julia-toulouse-mechanism]]).
- Adding matter yields the Fradkin–Shenker phase diagram and the Higgs/confinement complementarity, the backdrop for [[topological-order]] (the deconfined phase is the [[toric-code]]).

## Relations

- [[wilson-loop]] — the central gauge-invariant order parameter; area vs perimeter law
- [[villain-action]] — the form in which abelian lattice gauge theories dualize exactly
- [[higher-form-symmetries]] — center/magnetic symmetries of lattice gauge theory are higher-form symmetries; confinement = unbroken 1-form symmetry
- [[toric-code]] — the $\mathbb{Z}_2$ Kogut–Susskind Hamiltonian in its deconfined phase
- [[julia-toulouse-mechanism]], [[dual-superconductor]] — confinement via condensation of the dual (monopole) defects
- [[confinement]] — the phenomenon lattice gauge theory was built to capture nonperturbatively

## Papers

Foundational: Wilson (1974); Wegner (1971); Kogut–Susskind (1975); Kogut's review, Rev. Mod. Phys. 51 (1979) 659. See the course bibliography and [[confinement-duality]] for the full list.

## Notes

- Elitzur's theorem is why lattice gauge theory forced the field toward extended (loop) order parameters decades before "generalized symmetry" named the pattern.
- The continuum limit is taken along a line of increasing $\beta$ toward a critical point; asymptotic freedom fixes how $a \to 0$ relates to $\beta \to \infty$ for non-abelian groups.
- Monte Carlo (Creutz, 1980) turned the lattice into the primary quantitative tool for QCD; this course stays analytic, using the lattice for its exact dualities and its clean phase structure rather than for numbers.
