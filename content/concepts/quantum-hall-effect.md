---
title: Quantum Hall Effect
type: concept
areas: [condensed-matter-connections, confinement-duality]
aliases: [QHE, integer quantum Hall effect, fractional quantum Hall effect, IQHE, FQHE, Hall conductance, Hall conductivity, quantum anomalous Hall effect, Laughlin state, filling fraction]
modified: 2026-10-04
---

## Definition

Take a two-dimensional electron system whose bulk is an insulator: gapped, with vanishing longitudinal conductivity. A weak in-plane electric field then produces a perpendicular current, $J_y=\sigma_{xy}E_x$, with
$$
\sigma_{xy}=\nu\,\frac{e^2}{h},
$$
and $\nu$ is quantized. It can be an **integer** (von Klitzing–Dorda–Pepper 1980; measured to about $10^{-9}$, now a resistance standard) or a **rational number with a small, usually odd, denominator** (Tsui–Störmer–Gossard 1982, $\nu=1/3$). The original setting is a strong perpendicular magnetic field. Zero-field "anomalous" versions also exist: the quantum anomalous Hall effect (Haldane's 1988 model; observed by Chang et al. 2013) and the fractional quantum anomalous Hall effect (Park et al. 2023, twisted MoTe₂).

Three complementary explanations:

- **Effective action** ([[2026-witten-chern-simons-quantum-hall|Witten 2026]]).
  - In the effective action of a 2+1d insulator, the only term not built from $\vec E,\vec B$ is $2\pi k\,\mathrm{CS}(A)=\frac{k}{4\pi}\int A\,dA$.
  - Well-definedness of $e^{iI}$ forces $k\in\mathbb{Z}$, and odd $k$ requires a spin structure.
  - This is the only term whose current is proportional to the field, so $\sigma_{xy}=k\,e^2/h$.
  - In the fractional effect an emergent field $a$ couples through $(k,s,r)$ and $\nu=k-s^2/r$. See [[chern-simons-theory]].
- **Topology and index theory.**
  - Laughlin's flux-insertion argument (1981).
  - TKNN (1982): the Hall conductance is the Chern number of the filled bands. Avron–Seiler–Simon (1983).
  - Rigorous quantization for interacting gapped systems (Hastings–Michalakis 2015).
  - Rational indices with denominator bounded by the torus degeneracy (Bachmann–Bols–De Roeck–Fraas 2021).
- **Wavefunctions.** Laughlin (1983): $\Psi=\prod_{i<j}(z_i-z_j)^m e^{-\sum|z_i|^2/4}$ at $\nu=1/m$, with quasiparticle charge $e/m$. Moore–Read (1991): conformal blocks and the Pfaffian, the non-abelian candidate for $\nu=5/2$.

**Bulk and edge.**

- **Bulk.** The bulk is a [[topological-order]] described by abelian Chern–Simons theory, or by a $K$-matrix for multi-component states. The ground-state degeneracy is $|\det K|^g$ on genus $g$ and the excitations are anyons. The topological entanglement entropy is $\gamma=\ln\sqrt{|\det K|}$, i.e. $\ln\sqrt3$ at $\nu=1/3$.
- **Edge.** Chiral edge modes are forced by [[t-hooft-anomaly|anomaly inflow]]. The edge charge density obeys $[\rho(x),\rho(y)]=\frac{i\nu}{2\pi}\delta'(x-y)$: a $U(1)$ Kac–Moody algebra whose level is the Hall conductance.
- **The Laughlin edge** is a chiral boson (Wen 1990). The electron operator has scaling dimension $m/2$, so it is a fermion for odd $m$, and the quasiparticles carry charge $e/m$. In Witten's conventions $r=-m$.

## Role in Research

- **[[confinement-duality]], historical.** The group's Maxwell–Chern–Simons and Chern–Simons work lives here. The Chern–Simons level *is* the Hall conductance, and Maxwell–Chern–Simons is the fractional-effect effective theory with an irrelevant Maxwell term.
- **[[condensed-matter-connections]].** The half-quantized surface Hall conductance $e^2/2h$ of a $\theta=\pi$ topological insulator is the boundary of the θ-term ([[axionic-electrodynamics]]). Witten's integrality argument explains why that surface cannot be a standalone 2d insulator.
- **Quantum-information program.** The edge is a chiral CFT, a net of type III₁ algebras whose current has Pauli–Jordan distribution proportional to $\nu$. That is natural ground for the group's Weyl- and vertex-operator Bell-CHSH constructions and for coherent-state Araki–Uhlmann computations; see the Questions Raised in [[2026-witten-chern-simons-quantum-hall]]. In the bulk, abelian states are stabilizer states while non-abelian orders carry long-range magic (cf. [[magic-nonstabilizerness]]).
- **Courses.** The generalized-symmetries course treats the fractional effect in Semester II Week 10 ("one honest lecture": Laughlin $\nu=1/3$, $K=3$, three ground states on the torus). The Hall response of a θ-wall is Semester I Week 12 §8.

## Relations

- [[chern-simons-theory]]: the effective action; level = Hall conductance.
- [[topological-order]]: fractional quantum Hall fluids are the experimentally realized topological orders.
- [[axionic-electrodynamics]]: θ-walls carry Hall response $(\Delta\theta/2\pi)\,e^2/h$.
- [[t-hooft-anomaly]]: the chiral edge is the inflow partner of the bulk Chern–Simons term.
- [[spt-phases]]: the integer effect is invertible but not an SPT (see Notes).
- [[weyl-operators]]: the edge current generates a Weyl algebra with symplectic form proportional to $\nu$.
- [[julia-toulouse-mechanism]]: the composite-boson condensation picture (Zhang–Hansson–Kivelson; Read) is a defect-condensation derivation of the emergent Chern–Simons field.

## Papers

- E. Hall (1879); K. von Klitzing, G. Dorda, M. Pepper, PRL 45 (1980) 494.
- R. B. Laughlin, PRB 23 (1981) 5632 (the gauge argument) and PRL 50 (1983) 1395 (the wavefunction).
- D. J. Thouless, M. Kohmoto, M. P. Nightingale, M. den Nijs, PRL 49 (1982) 405. TKNN.
- D. C. Tsui, H. L. Störmer, A. C. Gossard, PRL 48 (1982) 1559.
- F. D. M. Haldane, PRL 61 (1988) 2015.
- S. C. Zhang, T. H. Hansson, S. Kivelson, PRL 62 (1989) 82; N. Read, PRL 62 (1989) 86.
- X.-G. Wen, PRB 41 (1990) 12838 (chiral Luttinger liquid); X.-G. Wen, A. Zee, PRB 46 (1992) 2290 ($K$-matrix).
- G. Moore, N. Read, NPB 360 (1991) 362.
- M. B. Hastings, S. Michalakis, CMP 334 (2015) 433.
- S. Bachmann, A. Bols, W. De Roeck, M. Fraas, J. Math. Phys. 62 (2021) 011901 [arXiv:2001.06458].
- H. Park et al., Nature 622 (2023) 74 [arXiv:2308.02657].
- [[2026-witten-chern-simons-quantum-hall]]. The effective-action derivation.

## Notes

- **Integer quantum Hall states are invertible but not SPTs.** Their chiral edge, with chiral central charge $c_-=k$, survives without any symmetry. The $U(1)$ response is the level-$k$ Chern–Simons term; the thermal Hall response is a gravitational Chern–Simons term (cf. Freed–Hopkins on invertible phases).
- **"Insulator" in Witten's sense** means no gapless bulk degrees of freedom. $\sigma_{xx}=0$ with $\sigma_{xy}\neq0$ also gives $\rho_{xx}=0$, which is why a Hall plateau shows zero longitudinal resistance.
- **Orientation.** The sign of $\sigma_{xy}$ depends on orientation; Witten fixes it by $dt\,dx\,dy$.
