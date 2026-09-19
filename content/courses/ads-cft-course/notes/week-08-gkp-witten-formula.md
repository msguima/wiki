---
title: "Week 8 — GKP-Witten formula and the operator–field dictionary"
type: lecture-notes
course: syllabus
semester: 1
week: 8
block: B
duration: "4 hours (2 lectures × 2 hours)"
status: drafting
modified: 2026-05-28
---

# Week 8 — GKP-Witten Formula and the Operator–Field Dictionary

> *This is the operational heart of AdS/CFT: the rule that turns a bulk gravity computation into a boundary correlator. The **GKP-Witten formula** identifies the CFT generating functional with the on-shell bulk partition function, the boundary value of each bulk field playing the role of the CFT source. Working out the free scalar near the boundary gives the **mass–dimension relation** $\Delta(\Delta-d)=m^2L^2$ — the same combination $\Delta(\Delta-d)$ that was the conformal-block Casimir eigenvalue in [[week-03-ope-and-conformal-blocks|Week 3]] — and identifies the two near-boundary modes as source and VEV. We derive the bulk-to-boundary propagator and use it to reproduce the conformally-fixed two-point function from pure bulk geometry.*

## Learning goals

By the end of this week, a student can:

1. State the GKP-Witten formula and explain the source ↔ boundary-value identification.
2. **Derive** the mass–dimension relation $\Delta(\Delta-d)=m^2L^2$ from the bulk scalar EOM near the boundary.
3. Identify the two near-boundary modes ($z^{d-\Delta}$ source, $z^\Delta$ VEV) and state the BF bound.
4. Write the bulk-to-boundary propagator and verify it solves the EOM and reduces to $\delta^d$ on the boundary.
5. Compute the holographic two-point function and match its $|x|^{-2\Delta}$ form to Week 1.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *AdS/CFT Foundations* §5** — the GKP/Witten prescription, the mass–dimension relation, alternate quantisation and the BF bound.
- Gubser, Klebanov, Polyakov, [arXiv:hep-th/9802109](https://arxiv.org/abs/hep-th/9802109) and Witten, [arXiv:hep-th/9802150](https://arxiv.org/abs/hep-th/9802150) — the founding papers.
- Klebanov, Witten, [arXiv:hep-th/9905104](https://arxiv.org/abs/hep-th/9905104) — alternative quantisation / $\Delta_-$ branch (Exercise/Notes).

**Prerequisites.** [[week-06-ads-geometries]] (Poincaré metric), [[week-07-large-n-and-thooft-limit]] (single-trace operators $\mathcal{O}$ are the boundary side), [[week-01-conformal-algebra-and-primaries]] (the dimension $\Delta$ and unitarity bound).

**AQFT cross-reference.** None for Block B.

## 1. The action and the boundary value problem

Take a free bulk scalar in Poincaré AdS$_{d+1}$ ($ds^2=\tfrac{L^2}{z^2}(dz^2+\eta_{\mu\nu}dx^\mu dx^\nu)$, $L=1$):

$$
S = -\tfrac12\int d^{d+1}x\,\sqrt{g}\,\big[(\nabla\phi)^2 + m^2\phi^2\big],
\qquad (\Box - m^2)\phi = 0.
$$

The bulk equation is second order; a solution is fixed by data at the $z=0$ boundary. The duality says: that boundary data is a **source** for a boundary operator, and the on-shell action is the **generating functional** of that operator's correlators.

## 2. The mass–dimension relation (worked)

Solve the EOM near the boundary with a power ansatz $\phi\sim z^\beta$ (drop $x$-dependence to leading order). Compute the Laplacian on $z^\beta$ in the Poincaré metric ($\sqrt g = z^{-(d+1)}$, $g^{zz}=z^2$):

$$
\Box\,z^\beta = \frac{1}{\sqrt g}\,\partial_z\!\big(\sqrt g\,g^{zz}\,\partial_z z^\beta\big)
= z^{d+1}\,\partial_z\!\big(z^{-(d+1)}\,z^{2}\,\beta z^{\beta-1}\big)
= z^{d+1}\,\beta\,\partial_z z^{\beta-d}
= \beta(\beta-d)\,z^{\beta}.
$$

So $(\Box-m^2)z^\beta = [\beta(\beta-d)-m^2]z^\beta=0$ forces the **indicial equation**

$$
\boxed{\;\beta(\beta-d) = m^2 L^2,\qquad \beta = \Delta_\pm = \frac{d}{2}\pm\sqrt{\frac{d^2}{4}+m^2L^2}.\;}
$$

Calling $\Delta\equiv\Delta_+$ the operator dimension (and noting $\Delta_-=d-\Delta$), the two near-boundary modes are

$$
\phi(z,x) \;\sim\; z^{\,d-\Delta}\,J(x) \;+\; z^{\,\Delta}\,\frac{\langle\mathcal{O}(x)\rangle}{2\Delta-d} + \cdots\qquad(z\to0).
$$

The dominant (non-normalisable) mode $z^{d-\Delta}$ is the **source** $J$; the subleading (normalisable) mode $z^\Delta$ encodes the **response** $\langle\mathcal{O}\rangle$. This is the operator–field map: a bulk field of mass $m$ is dual to a boundary primary of dimension $\Delta=\tfrac d2+\sqrt{\tfrac{d^2}4+m^2L^2}$.

Two remarks: (i) the combination $\Delta(\Delta-d)$ is exactly the conformal-block Casimir eigenvalue of [[week-03-ope-and-conformal-blocks|Week 3 §4]] — kinematics on the two sides match. (ii) Reality of $\Delta$ requires the **Breitenlohner–Freedman bound**

$$
\boxed{\;m^2L^2 \ge -\frac{d^2}{4}.\;}
$$

A scalar can be tachyonic in AdS down to this bound and still define a stable, unitary theory (the AdS curvature stabilises it); $m^2L^2=0$ gives $\Delta=d$ (marginal), $m^2L^2<0$ gives $\Delta<d$ (relevant). In the window $-\tfrac{d^2}4\le m^2L^2<-\tfrac{d^2}4+1$ either root $\Delta_\pm$ is an admissible dimension (alternative quantisation; Klebanov–Witten).

> **[Proven]** the mass–dimension relation and BF bound from the indicial equation (above; Exercises 1–2).

**Worked example: reading off dimensions.** The relation $\Delta=\tfrac d2+\sqrt{\tfrac{d^2}4+m^2L^2}$ turns bulk masses into boundary dimensions. Tabulate the salient cases (in $d=4$, where $\tfrac d2=2$):

| bulk mass $m^2L^2$ | $\Delta$ | boundary operator |
|---|---|---|
| $m^2L^2>0$ | $\Delta>d$ | **irrelevant** operator |
| $m^2L^2=0$ (massless) | $\Delta=d$ (=4) | **marginal**; e.g. a conserved-current-like / exactly marginal coupling |
| $-\tfrac{d^2}4<m^2L^2<0$ | $\tfrac d2<\Delta<d$ | **relevant** operator |
| $m^2L^2=-\tfrac{d^2}4$ (BF bound) | $\Delta=\tfrac d2$ (=2) | the most relevant unitary scalar; $\Delta_+=\Delta_-$ |

So a **tachyonic** bulk scalar (negative $m^2$, stable down to the BF bound) is dual to a **relevant** boundary operator — the bulk mass-squared and the boundary relevance run oppositely, a frequent source of confusion. Worked instance: the $\Delta=3$ chiral primary of $\mathcal{N}=4$ SYM ($d=4$) needs $\Delta(\Delta-d)=3\cdot(-1)=-3$, i.e. $m^2L^2=-3$ — tachyonic but well above the BF bound $-4$, hence a relevant (super)operator, as expected. In the BF window $-\tfrac{d^2}4\le m^2L^2<-\tfrac{d^2}4+1$ *both* roots $\Delta_\pm=\tfrac d2\pm\sqrt{\cdots}$ exceed the unitarity bound $\tfrac{d-2}2$, so either may be chosen as the operator dimension — the **alternative quantisation** of Klebanov–Witten, where the roles of source ($z^{d-\Delta}$) and VEV ($z^\Delta$) are swapped and the two CFTs differ by a double-trace deformation.

## 3. The GKP-Witten formula

The dictionary, stated:

$$
\boxed{\;Z_{\mathrm{CFT}}[J] = \Big\langle e^{\int d^dx\,J(x)\,\mathcal{O}(x)}\Big\rangle_{\mathrm{CFT}} = Z_{\mathrm{grav}}\big[\phi(z,x)\big|_{z\to0}\to z^{d-\Delta}J(x)\big].\;}
$$

In the classical-gravity (large-$N$, large-$\lambda$) limit the right side is $e^{-S_{\mathrm{on\text{-}shell}}[J]}$, the bulk action evaluated on the solution with boundary data $J$. Correlators of $\mathcal{O}$ are functional derivatives:

$$
\langle\mathcal{O}(x_1)\cdots\mathcal{O}(x_n)\rangle = \frac{\delta^n}{\delta J(x_1)\cdots\delta J(x_n)}\,Z_{\mathrm{CFT}}[J]\Big|_{J=0}.
$$

This is a **definition** of the duality (a prescription), not a theorem; its content is checked by verifying that bulk computations reproduce CFT Ward identities, the conformally-fixed correlators (§5), and the OPE/crossing data of Block A.

> **[Stated-without-proof / definitional]** GKP-W itself — the consistency checks are the evidence.

## 4. The bulk-to-boundary propagator

To solve the boundary-value problem, one needs the bulk field sourced by a delta-function on the boundary — the **bulk-to-boundary propagator**:

$$
\boxed{\;K_\Delta(z,x;y) = C_\Delta\left(\frac{z}{z^2+|x-y|^2}\right)^{\!\Delta},\qquad
C_\Delta = \frac{\Gamma(\Delta)}{\pi^{d/2}\,\Gamma(\Delta-\tfrac d2)}.\;}
$$

One checks directly that $K_\Delta$ solves $(\Box-m^2)K=0$ with $\Delta(\Delta-d)=m^2L^2$ (it is built from the AdS-isometry-covariant chordal distance), and that as $z\to0$, $z^{\Delta-d}K_\Delta(z,x;y)\to\delta^d(x-y)$ — the normalisation that fixes $C_\Delta$. The general solution with source $J$ is then $\phi(z,x)=\int d^dy\,K_\Delta(z,x;y)\,J(y)$.

**Worked: fixing $C_\Delta$ and the $\delta$-function limit.** The normalisation follows from requiring $z^{\Delta-d}K_\Delta\to\delta^d(x-y)$ as $z\to0$. Integrate $K_\Delta$ over the boundary and substitute $x-y=z\,u$ (so $d^dx=z^d\,d^du$ and $z^2+|x-y|^2=z^2(1+u^2)$):

$$
\int d^dx\,\Big(\frac{z}{z^2+|x-y|^2}\Big)^{\!\Delta}
= \int d^dx\,\frac{z^\Delta}{(z^2+|x-y|^2)^\Delta}
= z^d\!\int d^du\,\frac{z^\Delta}{z^{2\Delta}(1+u^2)^\Delta}
= z^{\,d-\Delta}\!\int\frac{d^du}{(1+u^2)^\Delta}.
$$

The remaining integral is standard: $\int\frac{d^du}{(1+u^2)^\Delta}=\dfrac{\pi^{d/2}\,\Gamma(\Delta-\tfrac d2)}{\Gamma(\Delta)}$. Hence

$$
z^{\Delta-d}\int d^dx\,K_\Delta = C_\Delta\,\frac{\pi^{d/2}\,\Gamma(\Delta-\tfrac d2)}{\Gamma(\Delta)} \;\overset{!}{=}\; 1
\quad\Longrightarrow\quad
C_\Delta = \frac{\Gamma(\Delta)}{\pi^{d/2}\,\Gamma(\Delta-\tfrac d2)},
$$

as quoted. As $z\to0$ the profile $(z/(z^2+|x-y|^2))^\Delta$ concentrates at $x=y$ with unit integrated weight (in the $z^{\Delta-d}$-rescaled sense) — a nascent delta function. That $K_\Delta$ also solves $(\Box-m^2)K=0$ is the §2 indicial computation applied pointwise (it is the $\Delta$-mode dressed by an isometry mapping $y$ to infinity).

> **[Proven]** the normalisation $C_\Delta$ and the $\delta$-function reduction (worked above); $K_\Delta$ solving the EOM follows from §2 + AdS isometry.

## 5. The two-point function (worked sketch)

Feed $\phi=\int K_\Delta J$ into the on-shell action. Integrating by parts, the bulk term vanishes by the EOM and only a **boundary term** at $z=\epsilon$ survives:

$$
S_{\mathrm{on\text{-}shell}}[J] = -\tfrac12\int_{z=\epsilon}d^dx\,\sqrt{\gamma}\,n^z\,\phi\,\partial_z\phi,
$$

with $\gamma$ the induced boundary metric and $n^z$ the unit normal. After stripping the $\epsilon$-divergent contact terms (the systematic procedure is **holographic renormalisation**, [[week-09-holographic-renormalisation|Week 9]]), the finite piece quadratic in $J$ gives

$$
\langle\mathcal{O}(x)\mathcal{O}(y)\rangle = -\frac{\delta^2 S}{\delta J(x)\delta J(y)}
\;\propto\; \frac{(2\Delta-d)\,C_\Delta}{|x-y|^{2\Delta}}.
$$

This is exactly the conformally-fixed scalar two-point function of [[week-01-conformal-algebra-and-primaries|Week 1 §4]], $C_\mathcal{O}|x|^{-2\Delta}$, now **derived from the bulk** — the first non-trivial consistency check of GKP-W. (Three-point functions come from a cubic bulk vertex; Week 10.)

> **[Sketched]** the on-shell action reduces to a boundary term; **[Proven, given holographic renormalisation]** the $|x|^{-2\Delta}$ form (Exercise 4 + Week 9).

## 6. Key claims and proof status

- **[Proven]** mass–dimension relation $\Delta(\Delta-d)=m^2L^2$ and BF bound (§2).
- **[Stated-without-proof / definitional]** the GKP-W formula (§3).
- **[Sketched]** bulk-to-boundary propagator solves the EOM and reduces to $\delta^d$; normalisation $C_\Delta$ (§4).
- **[Sketched→Proven mod Wk 9]** holographic two-point function $\propto|x|^{-2\Delta}$ (§5).

*No coefficients in this note are uncertain. (No `CHECK` items for Wk 8 — the $C_\Delta$ normalisation is standard, AGMOO §3.)*

## 7. What to take away

- **GKP-W:** $Z_{\mathrm{CFT}}[J]=Z_{\mathrm{grav}}[\phi_\partial\to z^{d-\Delta}J]$; the bulk boundary value is the CFT source, the on-shell action is the generating functional.
- **Mass–dimension:** $\Delta(\Delta-d)=m^2L^2$, $\Delta=\tfrac d2+\sqrt{\tfrac{d^2}4+m^2L^2}$ — same $\Delta(\Delta-d)$ as the Week-3 Casimir. **BF bound** $m^2L^2\ge-\tfrac{d^2}4$.
- Near-boundary: $z^{d-\Delta}$ = source, $z^{\Delta}$ = VEV.
- **Bulk-to-boundary propagator** $K_\Delta\propto(z/(z^2+|x-y|^2))^\Delta$; bulk solution $\phi=\int K_\Delta J$.
- The on-shell action reproduces the conformally-fixed $\langle\mathcal{O}\mathcal{O}\rangle\propto|x|^{-2\Delta}$ — bulk geometry recovers Block A kinematics.

## Exercises

**Core.**

1. **Indicial equation.** With $\phi=f(z)e^{ik\cdot x}$ in Poincaré AdS, derive the near-boundary exponents $d-\Delta,\Delta$ and the relation $\Delta(\Delta-d)=m^2L^2$.
2. **BF bound / $\mathcal{N}=4$.** Verify $m^2L^2\ge-d^2/4$ from reality of $\Delta$; in $d=4$ find $m^2L^2$ for the $\Delta=3$ chiral primary.
3. **Bulk-to-boundary propagator.** Show $K_\Delta=C_\Delta(z/(z^2+|x-y|^2))^\Delta$ solves $(\Box-m^2)K=0$ and fix $C_\Delta$ from $\lim_{z\to0}z^{\Delta-d}K_\Delta=\delta^d(x-y)$.

**Starred.**

4. $\star$ **Two-point function.** Evaluate the on-shell action's boundary term with $\phi=\int K_\Delta J$, differentiate twice, and recover $\langle\mathcal{O}\mathcal{O}\rangle\propto|x-y|^{-2\Delta}$ (noting the divergent contact terms that Week 9 removes).
5. $\star$ **Alternative quantisation.** For $-\tfrac{d^2}4\le m^2L^2<-\tfrac{d^2}4+1$, show both $\Delta_\pm$ are above the unitarity bound and discuss choosing $\Delta_-$ (Klebanov–Witten).

**Project.**

6. **Witten-diagram preview.** Set up (not evaluate) the three-point function from a cubic bulk vertex $\lambda\phi^3$ using three bulk-to-boundary propagators meeting at an integrated bulk point; identify the structure that will give the conformally-fixed three-point form of [[week-01-conformal-algebra-and-primaries|Week 1]] (full evaluation: [[week-10-bulk-correlators|Week 10]]).

## Connections to other parts of the wiki

- **Within the course.** Built on [[week-06-ads-geometries]] and [[week-07-large-n-and-thooft-limit]]; central prerequisite for [[week-09-holographic-renormalisation]] (the on-shell action's divergences) and [[week-10-bulk-correlators]] (the propagator builds Witten diagrams). Mass–dimension ties to the unitarity bound of [[week-01-conformal-algebra-and-primaries]] and the Casimir of [[week-03-ope-and-conformal-blocks]].
- **Concepts.** [[gkp-witten-formula]], [[holographic-dictionary]].
- **AQFT course cross-reference.** None for Block B.
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block B. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*
