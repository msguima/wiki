---
title: Chern-Simons Theory
type: concept
areas: [confinement-duality, condensed-matter-connections]
aliases: [Chern-Simons function, Chern-Simons invariant, Chern-Simons term, Chern-Simons level, CS term, abelian Chern-Simons, Maxwell-Chern-Simons, topologically massive gauge theory, K-matrix]
modified: 2026-10-04
---

## Definition

**The Chern–Simons function.** Take a connection $A$ on a bundle over a closed oriented 3-manifold $W$, and a 4-manifold $X$ with $\partial X = W$ over which the bundle and connection extend. Then
$$
\mathrm{CS}(A)=\int_X \frac{\mathrm{Tr}\,F\wedge F}{8\pi^2}\ \bmod \mathbb{Z}
$$
does not depend on the extension. Two extensions glue into a closed 4-manifold, and the difference is that manifold's instanton number, an integer ([[2026-witten-chern-simons-quantum-hall|Witten 2026]], §1). It is a *secondary* characteristic class: locally it is given by a Chern–Simons form whose exterior derivative is the second Chern form.

- *Abelian case.* For a trivialized line bundle, $\mathrm{CS}(A)=\frac{1}{8\pi^2}\int_W A\wedge dA$.
- *Non-abelian case.* The local formula acquires the familiar cubic term. Sign conventions for the trace differ between hermitian and anti-hermitian $A$.
- *Variation.* In the abelian case $\delta\,\mathrm{CS}=\frac{1}{4\pi^2}\int\delta A\wedge F$, so the critical points are the **flat connections**.

**Chern–Simons theory** is the gauge theory with action $2\pi k\,\mathrm{CS}(A)$; for $U(1)$ this is $\frac{k}{4\pi}\int A\,dA$.

**Level quantization.** $\mathrm{CS}$ is defined only mod $\mathbb{Z}$ and $e^{iI}$ must be single-valued, so $k\in\mathbb{Z}$. For $U(1)$ there is a refinement.

- $\int_X F\wedge F/8\pi^2=\tfrac12\int_X c_1^2$ is an integer only when the intersection form is even, i.e. on **spin** 4-manifolds.
- So $\mathrm{CS}(A) \bmod \mathbb{Z}$ needs a spin structure on $W$ and depends on it. On $T^3=T^2\times S^1$, with $A$ pulled back from a degree-one connection on $T^2$, it is $0$ or $\tfrac12$ according to the spin structure (Witten 2026, §3).
- Without a spin structure only $2\,\mathrm{CS}(A)$ is defined. A **bosonic** $U(1)_k$ therefore needs even $k$, and odd $k$ is a **spin TQFT**.
- The mixed invariant $\mathrm{CS}(A,a)$, defined via $\int_X F\wedge f/4\pi^2$, needs no spin structure and carries an integer coefficient (Witten 2026, §§3–4).

**Structure of the theory.**

- **A topological field theory.** No metric enters and classical solutions are flat. States on a closed surface $\Sigma_g$ form a finite-dimensional space, of dimension $|k|^g$ for $U(1)_k$. Anyons are Wilson lines: the charge-$n$ line has spin $h_n=n^2/2k \bmod 1$ and mutual braiding phase $e^{2\pi i nm/k}$. These lines generate a $\mathbb{Z}_k$ [[higher-form-symmetries|1-form symmetry]] whose 't Hooft anomaly is encoded in the spins (Hsin–Lam–Seiberg). Non-abelian Chern–Simons theory gives the Jones polynomial and 3-manifold invariants (Witten 1989).
- **Maxwell–Chern–Simons (topologically massive).** $\mathcal{L}=-\frac{1}{4e^2}F_{\mu\nu}F^{\mu\nu}+\frac{k}{4\pi}\epsilon^{\mu\nu\rho}A_\mu\partial_\nu A_\rho$ has a single massive mode.
  - Its mass is $m = k e^2/2\pi$ and its spin is $\pm1$, set by the sign of $k$ (Deser–Jackiw–Templeton).
  - At distances $\gg 1/m$ the Chern–Simons term dominates and the theory flows to the $U(1)_k$ TQFT.
  - On a spatial torus the holonomy zero modes form a Landau problem. Its cyclotron frequency is exactly $m$ and its $k$-fold degenerate lowest level is the TQFT sector (Dunne–Jackiw–Trugenberger; Dunne, hep-th/9902115).
- **Duality with the self-dual model** (Deser–Jackiw 1984). Maxwell–Chern–Simons is locally equivalent to $\mathcal{L}_{SD}=\tfrac12 f_\mu f^\mu-\frac{1}{2m}\epsilon^{\mu\nu\rho}f_\mu\partial_\nu f_\rho$. The self-dual model is not a gauge theory and has no holonomy sector, so globally the equivalence should hold only up to the $U(1)_k$ TQFT factor. That statement is EXPECTED; no clean reference has been checked yet.
- **The $K$-matrix** (Wen–Zee 1992). The multi-component theory $\mathcal{L}=-\frac{1}{4\pi}K_{IJ}\,a^I da^J+\frac{1}{2\pi}t_I\,A\,da^I$ has:
  - Hall conductance $\sigma_{xy}=t^{\mathsf T}K^{-1}t$ in units of $e^2/h$;
  - ground-state degeneracy $|\det K|^g$ on $\Sigma_g$;
  - anyon statistics read from $K^{-1}$.

  Witten's $(k,s,r)$ model maps onto it as $r=-K$ and $s=t$, on top of a background level $k$. The generalized-symmetries course writes $+\frac{1}{4\pi}K\,a\,da$, the mirror image, where $r=K$ and $\sigma_{xy}=k-t^{\mathsf T}K^{-1}t$.
- **Boundaries and inflow.** On a 3-manifold with boundary, $e^{2\pi i k\,\mathrm{CS}}$ is a vector in a line determined by the boundary data (Ramadas–Singer–Weitsman). Chiral edge degrees of freedom must compensate, which is [[t-hooft-anomaly|anomaly inflow]]. The Schwinger term (level) of the edge current algebra equals the Hall conductance.
- **Four-dimensional origin.** $\mathrm{CS}_X(A)=\int_X F\wedge F/8\pi^2$ says that a region with $\theta=2\pi k$ bounded by $W$ induces $2\pi k\,\mathrm{CS}(A)$ on $W$. A θ-wall of height $\Delta\theta$ carries level $\Delta\theta/2\pi$, which is the bridge to [[axionic-electrodynamics]].

## Role in Research

The earliest line of the portfolio lives on this page ([[confinement-duality]]):

- **Duality.** Marcelo's MSc thesis and PLB 605 (2005) extend the Maxwell–Chern–Simons/self-dual duality to noncommutative space. PLB 625 (2005) looks for the dual of Maxwell–Chern–Simons coupled to charged matter.
- **Monopoles and Julia–Toulouse.** PLB 674 (2009) studies monopoles in the presence of the Chern–Simons term via Julia–Toulouse. The Chern–Simons term forces monopole-instantons to carry electric charge, which spoils Polyakov confinement (Pisarski 1986; Affleck–Harvey–Palla–Semenoff 1989). PRD 88 (2013) puts the Chern–Simons term in a dual Josephson junction.
- **Lorentz violation.** The 2006–2009 papers on induced Chern–Simons-like (Carroll–Field–Jackiw) terms in Lorentz-violating QED concern a term that, for constant $b_\mu$, is [[axionic-electrodynamics|axion electrodynamics]] with linear $\theta=2b\cdot x$. That is the anomalous Hall response of a Weyl semimetal (Zyuzin–Burkov 2012, ★ in Zotero). The historical Lorentz-violation work and the condensed-matter line therefore share one object.

It also enters current work in three places:

- **Project 18** ([[non-invertible-symmetries-mcs]]). Any analysis of the global and non-invertible symmetries of Maxwell–Chern–Simons needs the data above: integer level, spin structure for odd $k$, the $\mathbb{Z}_k$ 1-form symmetry and its anomaly, the $|k|^g$ degeneracy, and the global caveat on the self-dual duality.
- **[[condensed-matter-connections]].** This is the effective action of the [[quantum-hall-effect]], the boundary term of θ-electrodynamics, and the source of chiral edge modes.
- **Quantum information.** The topological entanglement entropy of $U(1)_k$ is $\gamma=\ln\sqrt{|k|}$. Abelian link states are stabilizer states (Salton–Swingle–Walter 2017), so the TQFT is magic-free, whereas the local Maxwell–Chern–Simons theory is not ([[2026-benedetti-magic-in-qft]]).
- **Courses.** Generalized-symmetries course: Semester I Week 12 (the θ-term, its spin-structure periodicity and the Hall response of a θ-wall) and Semester II Week 10 ($K$-matrix, Laughlin $\nu=1/3$, in the mirror convention). Semester II Week 12 builds the modified-Villain lattice on which Jacobson and Sulejmanpasic construct $U(1)_k$ from a lattice θ-term, the lattice version of the formula above; the course itself does not construct $U(1)_k$.

## Relations

- [[quantum-hall-effect]]: the Chern–Simons level is the Hall conductance.
- [[topological-order]]: abelian Chern–Simons theories are the continuum topological orders of fractional quantum Hall fluids.
- [[axionic-electrodynamics]]: the level across a θ-wall is $\Delta\theta/2\pi$.
- [[t-hooft-anomaly]]: the boundary of a Chern–Simons region carries an anomalous chiral theory (inflow).
- [[higher-form-symmetries]]: the $\mathbb{Z}_k$ 1-form symmetry generated by Wilson lines.
- [[wilson-loop]]: anyons are Wilson lines.
- [[julia-toulouse-mechanism]]: condensation in 2+1d produces Chern–Simons mass terms, and any such derivation must produce integer levels.
- [[villain-action]]: modified-Villain lattice $U(1)_k$.
- [[non-invertible-symmetries-mcs]]: the open question on Maxwell–Chern–Simons symmetries.

## Papers

- S.-S. Chern, J. Simons, *Characteristic forms and geometric invariants*, Ann. Math. 99 (1974) 48.
- A. Schwarz, CMP 67 (1979) 1. The abelian topological theory.
- S. Deser, R. Jackiw, S. Templeton, Ann. Phys. 140 (1982) 372. Topologically massive gauge theories.
- S. Deser, R. Jackiw, PLB 139 (1984) 371. The self-dual model.
- E. Witten, CMP 121 (1989) 351. Chern–Simons theory and the Jones polynomial.
- G. Dunne, R. Jackiw, C. Trugenberger, Ann. Phys. 194 (1989) 197. Maxwell–Chern–Simons on the torus. See also G. Dunne, *Aspects of Chern–Simons theory*, hep-th/9902115.
- I. Affleck, J. Harvey, L. Palla, G. Semenoff, NPB 328 (1989) 575. The Chern–Simons term versus the monopole.
- X.-G. Wen, A. Zee, PRB 46 (1992) 2290. The $K$-matrix.
- P.-S. Hsin, H. T. Lam, N. Seiberg, SciPost Phys. 6 (2019) 039 [arXiv:1812.04716]. 1-form symmetries in 3d and their anomalies.
- T. Jacobson, T. Sulejmanpasic, PRD 107 (2023) 125017 [arXiv:2303.06160]. Modified-Villain lattice $U(1)_k$.
- [[2026-witten-chern-simons-quantum-hall]]. Level quantization, spin structure, inflow, and the $(k,s,r)$ model of the fractional effect.
- Group: MSc thesis (2005); PLB 605 (2005); PLB 625 (2005); PLB 674 (2009); PRD 88 (2013). See [[confinement-duality]].

## Notes

- **Compactness is what quantizes.** Level quantization is a statement about $U(1)$ as a *compact* group: line bundles, large gauge transformations, monopole configurations. For a non-compact gauge group, or in perturbation theory on $\mathbb{R}^3$, nothing forces $k\in\mathbb{Z}$. Much of the 1980s–2000s Maxwell–Chern–Simons literature, including the duality papers, works in that local, perturbative regime.
- **Normalization ledger.** Witten's $\mathrm{CS}\in\mathbb{R}/\mathbb{Z}$, and the physics action is $2\pi k\,\mathrm{CS}=\frac{k}{4\pi}\int A\,dA$. After $A\to eA$ the Maxwell–Chern–Simons Lagrangian reads $-\tfrac14F^2+\frac{ke^2}{4\pi}\epsilon A\partial A$. That is the Deser–Jackiw–Templeton form $-\tfrac14F^2+\frac{m}{2}\epsilon A\partial A$ with $m=ke^2/2\pi$.
- On $\mathbb{R}^{2,1}$ the TQFT sector is invisible. It appears only with nontrivial spatial topology, with boundaries, or with anyon (Wilson-line) insertions.
- Witten's argument implies that a purely bosonic lattice model can realize $U(1)_k$ only for even $k$. Odd levels need a lattice spin structure or fundamental fermions.
