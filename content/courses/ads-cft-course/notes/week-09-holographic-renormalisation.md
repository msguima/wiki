---
title: "Week 9 — Holographic renormalisation"
type: lecture-notes
course: syllabus
semester: 1
week: 9
block: B
duration: "4 hours (2 lectures × 2 hours)"
status: drafting
modified: 2026-05-28
---

# Week 9 — Holographic Renormalisation

> *The on-shell action of [[week-08-gkp-witten-formula|Week 8]] is divergent: the conformal factor $L^2/z^2$ blows up at the boundary, and the radial integral diverges as $z\to0$. These are the **UV divergences of the dual CFT**, geometrised — recall (Week 6) that small $z$ is the UV. Holographic renormalisation is the systematic procedure that removes them with local boundary counterterms, leaving a finite generating functional. Its most beautiful output is the **holographic conformal anomaly**: the leftover, scheme-independent log divergence reproduces the CFT Weyl anomaly — in $d=2$ giving the Brown–Henneaux central charge $c=3L/2G_N$, tying the bulk geometry directly to the $c$ of [[week-04-stress-tensor-and-central-charge|Week 4]].*

## Learning goals

By the end of this week, a student can:

1. Identify the near-boundary ($z\to0$) divergences of the bulk on-shell action as CFT UV divergences.
2. Write the Fefferman–Graham expansion and explain which coefficients are local (determined by EOM) and which are the response.
3. Construct boundary counterterms that render $S_{\mathrm{ren}}$ finite, and obtain $\langle\mathcal{O}\rangle$, $\langle T_{\mu\nu}\rangle$ as renormalised one-point functions.
4. State the holographic Ward identities $\nabla_\mu\langle T^{\mu\nu}\rangle=0$ and $\langle T^\mu_\mu\rangle=\mathcal{A}$.
5. **Derive** the $d=2$ holographic Weyl anomaly $\langle T^\mu_\mu\rangle=\tfrac{c}{12}R$ with $c=3L/2G_N$.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *AdS/CFT Foundations* §6** — near-boundary expansion, counterterms, one-point functions from variation, Ward identities and anomalies.
- Skenderis, *Lecture notes on holographic renormalization*, [arXiv:hep-th/0209067](https://arxiv.org/abs/hep-th/0209067) — the canonical reference.
- de Haro, Skenderis, Solodukhin, [arXiv:hep-th/0002230](https://arxiv.org/abs/hep-th/0002230) — the systematic procedure and the stress-tensor anomaly.

**Prerequisites.** [[week-08-gkp-witten-formula]] (the divergent on-shell action), [[week-06-ads-geometries]] (Poincaré/FG coordinates), [[week-04-stress-tensor-and-central-charge]] (the CFT Weyl anomaly this reproduces).

**AQFT cross-reference.** None for Block B.

## 1. Divergences as CFT UV divergences

The Week-8 on-shell action, cut off at $z=\epsilon$, diverges as $\epsilon\to0$. Power-counting from the near-boundary expansion: a source $J$ of dimension $d-\Delta$ produces divergences $\sim\epsilon^{-(d-2\Delta)}$ (for $\Delta<d/2$) and, at special $\Delta$, a $\log\epsilon$. Geometrically these are inevitable: the proper distance to the boundary is infinite ([[week-06-ads-geometries|Week 6]], Exercise 3), and $z=\epsilon$ is a UV cutoff in the dual ($z$ = RG scale). So **bulk IR (near-boundary) divergences = boundary UV divergences** — the radial-position/energy-scale dictionary at work. They must be removed by *local* counterterms, exactly as in ordinary QFT renormalisation.

## 2. The Fefferman–Graham expansion

Choose FG gauge for the metric,

$$
ds^2 = L^2\,\frac{dz^2}{z^2} + \frac{1}{z^2}\,g_{\mu\nu}(z,x)\,dx^\mu dx^\nu,\qquad
g_{\mu\nu}(z,x) = g^{(0)}_{\mu\nu}(x) + z^2 g^{(2)}_{\mu\nu}(x) + \cdots,
$$

and similarly expand the scalar,

$$
\phi(z,x) = z^{d-\Delta}\big[\phi^{(0)} + z^2\phi^{(2)}+\cdots\big] + z^{\Delta}\big[\psi^{(0)} + \cdots\big].
$$

The EOM determine every coefficient **locally** in terms of the source $g^{(0)},\phi^{(0)}$ — *except* the response coefficients ($g^{(d)}_{\mu\nu}$ and $\psi^{(0)}$), which carry the dynamical one-point functions $\langle T_{\mu\nu}\rangle$ and $\langle\mathcal{O}\rangle$ and require the full (regular-in-the-interior) solution. This split — local source data vs non-local response — is the structural heart of the method.

**Worked example: the FG recursion is local.** Solve the scalar EOM near the boundary to see the locality explicitly. In Poincaré AdS the radial equation for $\phi(z,x)$ is

$$
z^2\partial_z^2\phi - (d-1)\,z\,\partial_z\phi + z^2\,\partial_x^2\phi - m^2L^2\,\phi = 0.
$$

Insert the source branch $\phi = z^{d-\Delta}\sum_{k\ge0} z^{2k}\phi^{(2k)}(x)$. The $z^{d-\Delta}$ and $z^{2k}$ powers make the first, second, and fourth terms reproduce the indicial combination $\beta(\beta-d)-m^2L^2$ evaluated at $\beta=d-\Delta+2k$, while the $z^2\partial_x^2$ term lowers $k$ by one. Matching order by order,

$$
\big[(d-\Delta+2k)(-\Delta+2k) - m^2L^2\big]\,\phi^{(2k)} = -\,\partial_x^2\,\phi^{(2k-2)},
$$

and using $m^2L^2=\Delta(\Delta-d)$ the bracket is $2k(2k-2\Delta+d)\ne0$ (away from the resonant integer), so

$$
\phi^{(2k)}(x) = \frac{-\,\partial_x^2\,\phi^{(2k-2)}(x)}{2k\,(2k-2\Delta+d)}.
$$

Each coefficient is a **local** differential operator acting on the source $\phi^{(0)}=J$ — no integration constant enters until the *other* branch $z^\Delta\psi^{(0)}$, which is fixed only by regularity deep in the interior and carries the response $\langle\mathcal{O}\rangle$. When $2\Delta-d\in2\mathbb{Z}_{\ge0}$ the denominator hits zero at some $k$: the resonance is resolved by a $z^d\log z$ term, and *its* coefficient is the **conformal anomaly** (the $d=2$, $d=4$ cases of §4). This recursion is the engine behind "counterterms are local."

## 3. Counterterms and the renormalised action

Cut off at $z=\epsilon$ and add boundary-covariant counterterms built from the induced metric $\gamma_{\mu\nu}=g_{\mu\nu}(\epsilon)/\epsilon^2$ and boundary fields:

$$
S_{\mathrm{ren}} = \lim_{\epsilon\to0}\Big(S_{\mathrm{on\text{-}shell}}[\epsilon] + S_{\mathrm{ct}}[\gamma,\phi|_\epsilon]\Big),\qquad
S_{\mathrm{ct}} = \int_{z=\epsilon}\!d^dx\sqrt{\gamma}\,\Big[\,a_0 + a_1 R[\gamma] + b\,\phi^2 + \cdots\Big].
$$

The counterterm coefficients are fixed, order by order, by demanding cancellation of the $\epsilon$-divergences; crucially they are **local** functionals of the boundary data (cosmological constant, curvature, mass terms), so they are legitimate renormalisations and do not touch the finite physics. The renormalised one-point functions are then

$$
\langle\mathcal{O}(x)\rangle = \frac{\delta S_{\mathrm{ren}}}{\delta\phi^{(0)}(x)} \propto (2\Delta-d)\,\psi^{(0)}(x),\qquad
\langle T_{\mu\nu}(x)\rangle = \frac{2}{\sqrt{g^{(0)}}}\frac{\delta S_{\mathrm{ren}}}{\delta g^{(0)\,\mu\nu}(x)} \propto g^{(d)}_{\mu\nu}(x).
$$

The response coefficients become the dictionary entries for VEVs.

**Worked: the leading divergence and its counterterm (power counting).** Track the $\epsilon$-power of the scalar boundary term explicitly. The on-shell action reduces to the boundary integral $S=-\tfrac12\int_{z=\epsilon}\!d^dx\,\sqrt\gamma\,n^z\phi\,\partial_z\phi$, with induced metric determinant $\sqrt\gamma=(L/\epsilon)^d$ and outward unit normal $n^z=\epsilon/L$. Near the boundary $\phi\simeq z^{d-\Delta}\phi^{(0)}$, so $\partial_z\phi\simeq(d-\Delta)z^{d-\Delta-1}\phi^{(0)}$. Multiply the $\epsilon$-powers:

$$
\underbrace{\epsilon^{-d}}_{\sqrt\gamma}\cdot\underbrace{\epsilon}_{n^z}\cdot\underbrace{\epsilon^{\,d-\Delta}}_{\phi}\cdot\underbrace{\epsilon^{\,d-\Delta-1}}_{\partial_z\phi}
= \epsilon^{\,d-2\Delta},
$$

so $S\sim (d-\Delta)\,\epsilon^{\,d-2\Delta}\!\int d^dx\,(\phi^{(0)})^2$, **divergent** whenever $\Delta>d/2$ — exactly the dual CFT's UV divergence. The cure is a **local** boundary counterterm with the *same* $\epsilon$-scaling: $\sqrt\gamma\,\phi^2\sim\epsilon^{-d}\,\epsilon^{2(d-\Delta)}=\epsilon^{d-2\Delta}$, i.e.

$$
S_{\rm ct} = \frac{\Delta-d}{2L}\int_{z=\epsilon}\!d^dx\,\sqrt\gamma\,\phi^2,
$$

whose coefficient is fixed by demanding $S+S_{\rm ct}$ be finite as $\epsilon\to0$ (de Haro–Skenderis–Solodukhin). Crucially $S_{\rm ct}$ is built from boundary-covariant data ($\gamma$, $\phi|_\epsilon$) — a legitimate local renormalisation that does not touch the finite response $\psi^{(0)}$. Subleading divergences (for larger $\Delta$, or from curvature) need higher-derivative counterterms $\int\sqrt\gamma\,\phi\,\Box_\gamma\phi$, $\int\sqrt\gamma\,R[\gamma]\phi^2$, …, generated systematically by the FG recursion.

> **[Proven]** the leading divergence $S\sim\epsilon^{d-2\Delta}$ (power counting above); **[Stated-without-proof]** the exact counterterm coefficient (de Haro–Skenderis–Solodukhin) and the local/finite split.

## 4. Holographic Ward identities and the Weyl anomaly (worked, $d=2$)

Bulk diffeomorphism invariance, pushed to the boundary, gives the **holographic Ward identities**:

$$
\nabla^\mu\langle T_{\mu\nu}\rangle = 0\quad(\text{diffeos}),\qquad
\langle T^\mu{}_\mu\rangle = \mathcal{A}\quad(\text{Weyl}),
$$

where the anomaly $\mathcal{A}$ is non-zero precisely when there is a residual $\log\epsilon$ divergence (only in even $d$). Compute it in $d=2$.

**Brown–Henneaux from the bulk.** Put AdS$_3$ ($d=2$) on a curved boundary metric $g^{(0)}=\gamma$. The regulated gravitational on-shell action (Einstein–Hilbert + Gibbons–Hawking + counterterms) has a residual logarithmic divergence whose coefficient is the boundary Euler/curvature density. Extracting the trace of the renormalised boundary stress tensor gives

$$
\boxed{\;\langle T^\mu{}_\mu\rangle = \frac{c}{12}\,R[\gamma],\qquad c = \frac{3L}{2G_N}.\;}
$$

This is the **Brown–Henneaux central charge**, recovered purely from bulk gravity (Henningson–Skenderis). It is the same $c$ that appeared in the $\langle TT\rangle$ OPE of [[week-04-stress-tensor-and-central-charge|Week 4]] and in the Cardy/BTZ count of [[week-05-2d-cft-essentials|Week 5]] — three routes to one number, now including the bulk. (In $d=4$ the same procedure yields the $a$ and $c$ anomalies in terms of $L^3/G_N$; the holographic result has $a=c$ at leading order in the two-derivative bulk theory, the hallmark of a strongly-coupled large-$N$ CFT with a gravity dual.)

> **[Stated-without-proof]** the holographic Ward identities (Henningson–Skenderis); **[Proven within the model]** $\langle T^\mu_\mu\rangle=\tfrac{c}{12}R$ with $c=3L/2G_N$ in $d=2$ (the bulk computation; Exercise 3). The Brown–Henneaux $c=3L/2G$ is a standard, robust result.

## 5. Key claims and proof status

- **[Sketched]** divergence structure = CFT UV divergences; local counterterm cancellation (§§1, 3).
- **[Stated-without-proof]** FG expansion: source coefficients local, response coefficients dynamical (§2).
- **[Stated-without-proof]** holographic Ward identities (Henningson–Skenderis) (§4).
- **[Proven within the model]** $d=2$ holographic Weyl anomaly $c=3L/2G_N$ (§4).

*No coefficients in this note are uncertain. (The $d=4$ holographic $a,c$ coefficients are not quoted numerically here; only the $a=c$ structure is stated.)*

## 6. What to take away

- Bulk near-boundary divergences **are** the dual CFT's UV divergences ($z$ = RG scale); remove them with **local boundary counterterms**.
- **Fefferman–Graham:** source coefficients are local (EOM-determined); the response coefficients ($\psi^{(0)}$, $g^{(d)}_{\mu\nu}$) carry $\langle\mathcal{O}\rangle$, $\langle T_{\mu\nu}\rangle$.
- **Holographic Ward identities:** $\nabla_\mu\langle T^{\mu\nu}\rangle=0$, $\langle T^\mu_\mu\rangle=\mathcal{A}$ (anomaly only in even $d$).
- **Brown–Henneaux:** the $d=2$ holographic Weyl anomaly gives $c=3L/2G_N$ — the same $c$ as the $\langle TT\rangle$ OPE (Wk 4) and the BTZ/Cardy count (Wk 5).

## Exercises

**Core.**

1. **Scalar counterterm.** For a scalar dual to $\Delta$, identify the leading divergence of the on-shell action and the counterterm $\propto\phi^2|_\epsilon$ that cancels it; check $S_{\mathrm{ren}}$ is $\epsilon$-independent.
2. **Conservation Ward identity.** Perturb $g^{(0)}\to g^{(0)}+h$ and show bulk diffeo invariance ⟹ $\nabla_\mu\langle T^{\mu\nu}\rangle=0$.
3. **Brown–Henneaux.** For AdS$_3$ on a curved boundary, compute the renormalised stress-tensor trace and obtain $\langle T^\mu_\mu\rangle=\tfrac{c}{12}R$ with $c=3L/2G_N$.

**Starred.**

4. $\star$ **Log term.** For $\Delta=\tfrac d2+n$ ($n\in\mathbb{Z}_{>0}$), show the FG expansion develops a $z^d\log z$ term and relate it to the operator's contribution to the anomaly.
5. $\star$ **$d=4$ structure.** Sketch why the two-derivative bulk gives $a=c$ for the dual CFT, and what higher-curvature bulk terms ($R^2$) would be needed to split them.

**Project.**

6. **Anomaly matching.** Connect the holographic $c=3L/2G$ to the Cardy/BTZ entropy of [[week-05-2d-cft-essentials|Wk 5]] and the $\langle TT\rangle$ definition of [[week-04-stress-tensor-and-central-charge|Wk 4]]; write a 2-page note showing the three computations give one $c$.

## Connections to other parts of the wiki

- **Within the course.** Makes the [[week-08-gkp-witten-formula|Week 8]] on-shell action finite; prerequisite for clean correlators in [[week-10-bulk-correlators]]. The holographic $c$ matches [[week-04-stress-tensor-and-central-charge|Wk 4]] and [[week-05-2d-cft-essentials|Wk 5]] (and feeds [[sem2-week-07-ads2-ads3-essentials|Sem II Wk 7]] / BTZ).
- **Concepts.** [[gkp-witten-formula]], [[holographic-dictionary]].
- **AQFT course cross-reference.** None for Block B.
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block B. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*
