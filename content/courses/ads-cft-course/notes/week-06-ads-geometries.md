---
title: "Week 6 — AdS geometries: global, Poincaré, Euclidean"
type: lecture-notes
course: syllabus
semester: 1
week: 6
block: B
duration: "4 hours (2 lectures × 2 hours)"
status: drafting
modified: 2026-05-28
---

# Week 6 — AdS Geometries: Global, Poincaré, Euclidean

> *Holography starts here. Block A built the boundary CFT; Block B builds the bulk and the dictionary between them. This week is the bulk geometry: anti-de Sitter space as a hyperboloid, its three working coordinate systems (global, Poincaré, Euclidean), and — the kinematic backbone of the whole duality — the fact that the AdS$_{d+1}$ isometry group $\mathrm{SO}(d,2)$ is exactly the conformal group of the $d$-dimensional boundary derived in [[week-01-conformal-algebra-and-primaries|Week 1]]. We also see why the boundary carries only a **conformal structure** (no preferred scale), which is precisely why the dual theory must be a CFT.*

## Learning goals

By the end of this week, a student can:

1. Describe AdS$_{d+1}$ as a hyperboloid in $\mathbb{R}^{d,2}$ and **derive** the global metric from the embedding.
2. Write the metric in global, Poincaré, and Euclidean coordinates and say when each is useful.
3. Locate the asymptotic boundary of each patch and explain Poincaré geodesic incompleteness.
4. Explain conformal compactification and why the boundary has a conformal structure, not a metric.
5. State the isometry $\mathrm{SO}(d,2)$ and match it to the boundary conformal group — the kinematic core of AdS/CFT.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *AdS/CFT Foundations* §3** — all coordinate patches, the conformal boundary, global AdS and the cylinder.
- AGMOO, *Large-N Field Theories, String Theory and Gravity*, [arXiv:hep-th/9905111](https://arxiv.org/abs/hep-th/9905111), §2.
- McGreevy, [arXiv:0909.0518](https://arxiv.org/abs/0909.0518), §2 — Poincaré-patch emphasis.

**Prerequisites.** [[week-01-conformal-algebra-and-primaries]] (the conformal group $\mathrm{SO}(d,2)$ = AdS isometry); [[week-02-radial-quantisation-and-state-operator]] (the $\mathbb{R}\times S^{d-1}$ cylinder = global boundary). Standard GR (metrics, geodesics, causal structure).

**AQFT cross-reference.** None — purely classical geometry.

## 1. Why AdS

Solve the vacuum Einstein equations with a **negative** cosmological constant, $R_{\mu\nu}-\tfrac12 R g_{\mu\nu}+\Lambda g_{\mu\nu}=0$, $\Lambda<0$. The maximally symmetric solution is AdS$_{d+1}$, with $\Lambda=-\tfrac{d(d-1)}{2L^2}$ and constant negative curvature $R=-\tfrac{d(d+1)}{L^2}$ ($L$ the AdS radius). AdS is singled out for holography by two features absent from Minkowski/de Sitter: a **timelike conformal boundary** (where the dual CFT lives, and through which the bulk is in causal contact with "infinity"), and an isometry group that is exactly a conformal group. We set $L=1$ except where dimensions matter (conventions page).

## 2. Global coordinates from the hyperboloid (worked)

Realise AdS$_{d+1}$ as the hyperboloid

$$
-X_0^2 - X_{d+1}^2 + \sum_{i=1}^{d} X_i^2 = -L^2
$$

in $\mathbb{R}^{d,2}$ (signature $(-,-,+,\dots,+)$). The defining equation is invariant under the rotations/boosts of $\mathbb{R}^{d,2}$ that preserve this form — the group $\mathrm{SO}(d,2)$.

**Derive the metric.** Parametrise the two timelike directions by an angle $\tau$ and the spatial ones by a radial $\rho$ and a unit vector $\hat n\in S^{d-1}$:

$$
X_0 = L\cosh\rho\,\cos\tau,\quad X_{d+1}=L\cosh\rho\,\sin\tau,\quad \vec X = L\sinh\rho\,\hat n.
$$

(This solves the constraint: $-X_0^2-X_{d+1}^2+\vec X^2 = -L^2\cosh^2\rho + L^2\sinh^2\rho = -L^2$ ✓.) Now differentiate each embedding coordinate:

$$
\begin{aligned}
dX_0 &= L(\sinh\rho\cos\tau\,d\rho - \cosh\rho\sin\tau\,d\tau),\\
dX_{d+1} &= L(\sinh\rho\sin\tau\,d\rho + \cosh\rho\cos\tau\,d\tau),\\
d\vec X &= L(\cosh\rho\,\hat n\,d\rho + \sinh\rho\,d\hat n).
\end{aligned}
$$

Form $ds^2=-dX_0^2-dX_{d+1}^2+d\vec X^2$ and collect terms. The two timelike differentials give

$$
-dX_0^2-dX_{d+1}^2 = -L^2\big(\sinh^2\rho\,d\rho^2 + \cosh^2\rho\,d\tau^2\big),
$$

the $d\rho\,d\tau$ cross-terms cancelling between the $\cos\tau\sin\tau$ pieces of the two lines. The spatial part gives, using $\hat n\cdot d\hat n=0$ and $d\hat n\cdot d\hat n=d\Omega_{d-1}^2$,

$$
d\vec X^2 = L^2\big(\cosh^2\rho\,d\rho^2 + \sinh^2\rho\,d\Omega_{d-1}^2\big).
$$

Adding, the $d\rho^2$ coefficients combine as $L^2(\cosh^2\rho-\sinh^2\rho)=L^2$, and one finds

$$
\boxed{\;ds^2 = L^2\big(-\cosh^2\rho\,d\tau^2 + d\rho^2 + \sinh^2\rho\,d\Omega_{d-1}^2\big).\;}
$$

Here $\rho\in[0,\infty)$ is a radial coordinate and $\tau$ the global time (unwrap $\tau\in\mathbb{R}$ to avoid closed timelike curves — pass to the universal cover). As $\rho\to\infty$ both $\cosh^2\rho,\sinh^2\rho\to\tfrac14 e^{2\rho}$, so $ds^2\to \tfrac{L^2}{4}e^{2\rho}\big(-d\tau^2+d\Omega_{d-1}^2\big)$: the metric blows up, but its **conformal class** approaches $-d\tau^2+d\Omega_{d-1}^2$ — the cylinder $\mathbb{R}\times S^{d-1}$ of [[week-02-radial-quantisation-and-state-operator|Week 2]]. That is the global conformal boundary.

> **[Proven]** the global metric from the embedding (Exercise 1); **[Proven]** the isometry group $\mathrm{SO}(d,2)$ (the hyperboloid's symmetry).

## 3. The Poincaré patch

For holographic computations the most useful chart covers a wedge of AdS with a flat boundary. Introduce $z>0$ and $x^\mu=(t,\vec x)$:

$$
\boxed{\;ds^2 = \frac{L^2}{z^2}\big(-dt^2 + d\vec x^2 + dz^2\big) = \frac{L^2}{z^2}\big(\eta_{\mu\nu}dx^\mu dx^\nu + dz^2\big).\;}
$$

- The **boundary** is $z\to0$, where the conformal factor $L^2/z^2$ diverges; stripping it leaves flat $\mathbb{R}^{1,d-1}$ — the Poincaré-patch boundary.
- $z\to\infty$ is a **Poincaré horizon**: the patch is **geodesically incomplete**, covering only a wedge of global AdS (a radial null geodesic reaches $z\to\infty$ in finite affine parameter — Exercise 2). Global coordinates cover the whole manifold; the Poincaré patch is the relevant one for a CFT on flat space.
- The radial coordinate $z$ is a geometric **RG scale**: small $z$ (near-boundary) ↔ UV of the CFT, large $z$ ↔ IR. The log-divergent proper distance to the boundary (Exercise 3) is the geometric origin of UV divergences in the dual (Week 9).

## 4. Euclidean AdS and conformal flatness (worked)

Wick-rotate $t\to -i t_E$:

$$
ds^2_E = \frac{L^2}{z^2}\big(dt_E^2 + d\vec x^2 + dz^2\big),\qquad z>0.
$$

This is the **upper half-space** $\{z>0\}$ with a hyperbolic metric — Euclidean AdS, $\mathbb{H}^{d+1}$. Two immediate observations:

- **Conformally flat.** The metric is $\tfrac{L^2}{z^2}\times(\text{flat }\mathbb{R}^{d+1})$, i.e. Weyl-equivalent to flat space with conformal factor $\Omega^2=L^2/z^2$ (Exercise 4). All curvature lives in the conformal factor.
- **Thermal AdS.** Periodically identifying Euclidean time $t_E\sim t_E+\beta$ gives the bulk dual of the CFT at temperature $1/\beta$ — the starting point of [[week-12-finite-temperature-ads-schwarzschild|Wk 12]] (where AdS-Schwarzschild competes with this saddle in the Hawking–Page transition).

## 5. The conformal boundary, and why the dual is a CFT

The boundary metric is not well-defined: near $z=0$, $g\sim L^2/z^2\times(\text{flat})$ diverges, and one must strip a conformal factor to get a finite boundary metric. But the choice of factor is ambiguous — multiplying by any positive function rescales the boundary metric. So **the boundary inherits only a conformal class of metrics, not a metric**. This is the geometric reason the dual lives without a preferred scale: a theory defined on a conformal manifold must be invariant under Weyl rescalings of the boundary metric — it must be a **conformal field theory**.

And the symmetry counting closes the loop: the bulk isometry group $\mathrm{SO}(d,2)$ acts on the boundary conformal structure as exactly the **conformal group** of $\mathbb{R}^{1,d-1}$ derived in [[week-01-conformal-algebra-and-primaries|Week 1]] (Euclidean: $\mathrm{SO}(d+1,1)$ on $\mathbb{H}^{d+1}$). Bulk isometries = boundary conformal transformations:

$$
\text{AdS}_{d+1}\ \text{isometry } \mathrm{SO}(d,2)\;=\;\text{conformal group of the }d\text{-dim boundary.}
$$

This is the kinematic backbone of AdS/CFT — before any dynamics, the symmetries match exactly. The embedding-space coordinates $X^A$ of §2 are literally the embedding coordinates of Week 1 §2; "putting a CFT on the projective null cone" and "the AdS hyperboloid in $\mathbb{R}^{d,2}$" are the same $\mathrm{SO}(d,2)$ geometry seen from two sides.

> **[Sketched]** the conformal-boundary construction (strip the divergent factor; the residual ambiguity is the conformal class). **[Proven]** the isometry/conformal-group match (same $\mathrm{SO}(d,2)$, §2 + Week 1 §2).

**Worked example: an isometry acting as a boundary conformal transformation.** Make the match of §5 concrete in the Poincaré patch. Consider the bulk isometry that rescales all coordinates,

$$
(z,x^\mu)\ \longmapsto\ (\lambda z,\ \lambda x^\mu),\qquad \lambda>0.
$$

The Poincaré metric is invariant: $ds^2 = \tfrac{L^2}{(\lambda z)^2}(\lambda^2 dx^2 + \lambda^2 dz^2) = \tfrac{L^2}{z^2}(dx^2+dz^2)$ ✓. Restricting to the boundary $z\to0$, it acts as $x^\mu\to\lambda x^\mu$ — a **boundary dilatation**, the generator $D$ of [[week-01-conformal-algebra-and-primaries|Week 1]]. Likewise: bulk isometries that act as $x^\mu\to x^\mu+a^\mu$ (with $z$ fixed) are boundary **translations** $P_\mu$; the bulk rotations of the $x^\mu$ are boundary **rotations** $M_{\mu\nu}$; and the bulk image of the inversion $x^M\to x^M/(x^2+z^2)$ (acting on the full $(z,x)$) restricts on the boundary to the **special conformal** transformations $K_\mu$. The full set is $\mathrm{SO}(d,2)$, acting in the bulk as isometries and on the boundary as the conformal group — exactly the dictionary entry "bulk isometry = boundary conformal symmetry." A bulk field that is invariant under an isometry corresponds to a boundary operator covariant under the matching conformal transformation; this is how the $(\Delta,\ell)$ labels of Week 1 will attach to bulk fields in Week 8.

## 6. Causal structure and the Penrose diagram

The timelike boundary is what makes AdS unusual, and it has a concrete dynamical consequence. From the global metric, a radial null ray ($d\Omega=0$, $ds^2=0$) satisfies $\cosh\rho\,d\tau=\pm d\rho$, so

$$
\Delta\tau = \int_0^{\infty}\frac{d\rho}{\cosh\rho}.
$$

Do the integral with the antiderivative $\int\frac{d\rho}{\cosh\rho}=2\arctan(\tanh\tfrac{\rho}{2})$ (equivalently $\arctan\sinh\rho$): as $\rho:0\to\infty$, $\tanh\tfrac\rho2:0\to1$, so $\Delta\tau = 2\arctan(1)-2\arctan(0)=2\cdot\tfrac{\pi}{4}=\tfrac{\pi}{2}$.

A **light ray reaches the boundary in finite global time** $\Delta\tau=\pi/2$ (a massless signal travels to "infinity" and — once a boundary condition is imposed there — back, in global time $\pi$). Massive geodesics, by contrast, never reach the boundary: they oscillate, turning around at finite $\rho$, as if in a confining box. So AdS behaves like a **box** of size $L$ with reflecting (or otherwise specified) walls — which is precisely why one must *choose boundary conditions* at $z=0$, and why those boundary conditions are the CFT sources of [[week-08-gkp-witten-formula|Week 8]].

The Penrose diagram of global AdS is an infinite vertical strip: the left edge is the (regular) centre $\rho=0$, the right edge is the timelike conformal boundary $\rho\to\infty$ ($\mathbb{R}\times S^{d-1}$), and time runs vertically. Unlike Minkowski space (whose conformal boundary is null $\mathscr{I}^\pm$ plus points) or de Sitter (spacelike boundaries), AdS has a **timelike** boundary in causal contact with the interior at all times — the home of the dual CFT's time evolution.

> **[Proven]** the null-ray result $\Delta\tau=\pi/2$ (the elementary integral above); **[Sketched]** the massive-geodesic confinement and the Penrose-diagram structure.

## 7. Key claims and proof status

- **[Proven]** AdS$_{d+1}$ = hyperboloid in $\mathbb{R}^{d,2}$, isometry $\mathrm{SO}(d,2)$; global metric from the embedding (§2).
- **[Proven]** Poincaré and Euclidean metrics; conformal flatness of Euclidean AdS (§§3–4).
- **[Stated-without-proof]** Poincaré geodesic incompleteness (Exercise 2).
- **[Sketched]** conformal-boundary structure; **[Proven]** isometry = boundary conformal group (§5).

*No coefficients in this note are uncertain. (No `CHECK` items for Wk 6.)*

## 8. What to take away

- AdS$_{d+1}$ = hyperboloid in $\mathbb{R}^{d,2}$; **isometry $\mathrm{SO}(d,2)$ = boundary conformal group** (Week 1) — the kinematic core of the duality.
- **Global** coords cover the whole space ($ds^2=L^2(-\cosh^2\rho\,d\tau^2+d\rho^2+\sinh^2\rho\,d\Omega^2)$, boundary $\mathbb{R}\times S^{d-1}$); **Poincaré** ($\tfrac{L^2}{z^2}(\eta\,dx^2+dz^2)$, flat boundary at $z=0$) is the computational workhorse, with $z$ = RG scale; **Euclidean** = upper half-space $\mathbb{H}^{d+1}$, conformally flat.
- The boundary carries a **conformal structure, not a metric** ⟹ the dual is a CFT.
- $z$ small = UV, $z$ large = IR; the log-divergent distance to the boundary is the geometric seed of holographic UV divergences (Week 9).

## Exercises

**Core.**

1. **Global metric.** From $X_0=L\cosh\rho\cos\tau$, $X_{d+1}=L\cosh\rho\sin\tau$, $\vec X=L\sinh\rho\,\hat n$, derive $ds^2=L^2(-\cosh^2\rho\,d\tau^2+d\rho^2+\sinh^2\rho\,d\Omega_{d-1}^2)$.
2. **Geodesic incompleteness.** Exhibit a radial null geodesic in the Poincaré patch reaching $z\to\infty$ in finite affine parameter.
3. **Log distance.** Compute the proper length of the radial spacelike geodesic from $z=\epsilon$ to $z=1/\epsilon$ and show it diverges as $\log(1/\epsilon)$.

**Starred.**

4. $\star$ **Conformal flatness.** Show the Poincaré/Euclidean metric is conformally flat by exhibiting the conformal factor $\Omega^2=L^2/z^2$.
5. $\star$ **Boundary topology.** From the global metric, write the boundary metric up to conformal equivalence and identify the topology ($\mathbb{R}\times S^{d-1}$).

**Project.**

6. **Symmetry match.** Show explicitly that the $\mathrm{SO}(d,2)$ rotations/boosts of the embedding $\mathbb{R}^{d,2}$ act on the $z\to0$ boundary as the conformal transformations of Week 1 (translations, rotations, dilatation, SCT). This is the kinematic statement of AdS/CFT.

## Connections to other parts of the wiki

- **Within the course.** Prerequisite for [[week-07-large-n-and-thooft-limit]] (the gauge theory living on this boundary) and every later bulk computation ([[week-08-gkp-witten-formula|Wk 8]]–[[week-10-bulk-correlators|Wk 10]]). The thermal/Euclidean saddle here is the Hawking–Page setting of [[week-12-finite-temperature-ads-schwarzschild|Wk 12]]; the global boundary is the [[week-02-radial-quantisation-and-state-operator|Week 2]] cylinder.
- **AQFT course cross-reference.** None — classical geometry.
- **Area page.** [[gauge-gravity-duality]] — AdS is the bulk; the isometry/conformal-group match is the first reason the duality is even possible.

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block B. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*
