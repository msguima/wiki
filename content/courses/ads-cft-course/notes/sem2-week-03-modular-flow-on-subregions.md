---
title: "Sem II Week 3 — Modular flow on boundary subregions"
type: lecture-notes
course: syllabus
semester: 2
week: 3
block: 1
duration: "3 hours (lecture + seminar)"
status: final
modified: 2026-05-28
---

# Sem II Week 3 — Modular Flow on Boundary Subregions

> *This is the algebraic heart of Semester II, and the week where the course makes closest contact with the modular-theory / relative-entropy toolkit. The plan: recall Tomita–Takesaki as a black box (full development is the [[courses/ads-cft-course/syllabus|AQFT course]]); compute the modular Hamiltonian explicitly in the two cases where it is **local** — the Rindler wedge (Bisognano–Wichmann) and the ball (Casini–Huerta–Myers); see how the boundary modular flow becomes a **bulk Killing flow** in the entanglement wedge (Faulkner–Lewkowycz–Maldacena); and arrive at **JLMS** and the **first law of entanglement** $\delta S = \delta\langle K\rangle$, which is the seed of the QES prescription of [[sem2-week-05-quantum-extremal-surfaces|Week 5]].*
>
> *Status note: Tomita–Takesaki and Bisognano–Wichmann are imported as theorems (proved in the AQFT course); JLMS is imported from holography. What we **derive in full** here is the CHM ball modular Hamiltonian (with its coefficient) and the first law of entanglement from positivity of relative entropy.*

## Learning goals

By the end of this week, a student can:

1. State the Tomita–Takesaki data $(\Delta_\Omega, J_\Omega, \sigma_t)$ and the KMS property of the vacuum at modular temperature $\beta=2\pi$.
2. Write the modular Hamiltonian of the Rindler wedge as the local boost integral $K = 2\pi\!\int x^1 T_{00}$ (Bisognano–Wichmann).
3. **Derive** the ball modular Hamiltonian $K = 2\pi\!\int_{r<R}\frac{R^2-r^2}{2R}T_{00}$ (CHM) and recover Bisognano–Wichmann from it in the $R\to\infty$ limit.
4. Explain why $K$ is local only for the wedge/ball and non-local otherwise, and how the bulk modular flow is the Killing flow vanishing on the RT surface.
5. **Derive** the first law of entanglement $\delta S = \delta\langle K\rangle$ from $S_{\mathrm{rel}}\ge 0$, and read off how JLMS turns it into the gravitational first law that seeds the QES rule.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Advanced AdS/CFT* §12** — JLMS and the entanglement first law; *Black Hole Information* §3 for modular flow and bulk locality.
- Casini, Huerta, Myers, *Towards a derivation of holographic entanglement entropy*, JHEP 05 (2011) 036, [arXiv:1102.0440](https://arxiv.org/abs/1102.0440) (**CHM**) — the ball modular Hamiltonian and the conformal map to the hyperbolic cylinder. **The anchor for §3.**
- Jafferis, Lewkowycz, Maldacena, Suh, *Relative entropy equals bulk relative entropy*, JHEP 06 (2016) 004, [arXiv:1512.06431](https://arxiv.org/abs/1512.06431) (**JLMS**) — §5's operator equation.
- Faulkner, Guica, Hartman, Myers, Van Raamsdonk, *Gravitation from entanglement in holographic CFTs*, [arXiv:1312.7856](https://arxiv.org/abs/1312.7856) (**FGHMV/"FLM"**) — bulk Killing flow as the dual of boundary modular flow; the first law → linearised Einstein equations.

**Prerequisites (within the course).**

- [[week-14-hrt-and-subregion-subalgebra]] — entanglement wedge, subregion–subalgebra duality. JLMS is the algebraic upgrade of HRT.
- [[week-13-ryu-takayanagi]] — the RT area is the leading ($1/N^0$) piece of the modular Hamiltonian.
- [[tomita-takesaki-modular-theory]] — the algebraic machinery used as a black box here.

**For students coming from the AQFT course.** [[week-05-tomita-operator|AQFT Wk 5]] (Tomita operator, modular group) and [[week-10-bisognano-wichmann|AQFT Wk 10]] (Bisognano–Wichmann) prove the results §§1–2 import. [[week-07-connes-cocycle-and-relative-entropy|AQFT Wk 7]] is the algebraic version of the relative-entropy first law in §5.

**Assumed.** Reduced density matrices, von Neumann entropy, the modular Hamiltonian $K_A = -\log\rho_A$, the stress tensor $T_{\mu\nu}$ of a CFT.

## 1. Tomita–Takesaki, in one box

Let $\mathcal{A}$ be a von Neumann algebra of observables on a subregion, with a cyclic and separating vector $|\Omega\rangle$ (the vacuum is such, by Reeh–Schlieder). The **Tomita operator** is the antilinear $S_\Omega: a|\Omega\rangle \mapsto a^\dagger|\Omega\rangle$, with polar decomposition

$$
S_\Omega = J_\Omega\,\Delta_\Omega^{1/2},
\qquad
\Delta_\Omega = S_\Omega^\dagger S_\Omega \;(\text{modular operator}),
\qquad
J_\Omega \;(\text{modular conjugation, }J^2=1).
$$

The **modular flow** is the one-parameter automorphism group

$$
\boxed{\;\sigma_t(a) = \Delta_\Omega^{it}\,a\,\Delta_\Omega^{-it},\qquad a\in\mathcal{A}.\;}
$$

The single fact we use repeatedly: $|\Omega\rangle$ is a **KMS state** for $\sigma_t$ at inverse temperature $\beta = 2\pi$ (in modular units), equivalently $\rho_A = e^{-K_A}$ with the **modular Hamiltonian** $K_A = -\log\rho_A$ generating the flow, $\sigma_t = e^{iK_A t}\cdot e^{-iK_A t}$, so $\Delta_\Omega = e^{-K_A}$.

> **[Stated-without-proof]** Existence and uniqueness of $(\Delta_\Omega, J_\Omega)$ and the KMS property — Tomita–Takesaki theorem, proved in [[week-05-tomita-operator|AQFT Wk 5]]. For a holographic boundary subregion at large $N$, $\mathcal{A}(A)$ is a [[type-iii-von-neumann-algebras|type III₁ factor]], so $\rho_A$ does **not** exist as a trace-class operator and $K_A$ is defined only through $\Delta_\Omega$ — but every formula below is well-defined as written.

## 2. The Rindler wedge: Bisognano–Wichmann

Take the right Rindler wedge $W_R = \{x^1 > |x^0|\}$ in the Minkowski vacuum of any QFT. The **Bisognano–Wichmann theorem** identifies the modular data geometrically:

$$
\boxed{\;K_{W_R} = 2\pi\int_{x^1>0} x^1\,T_{00}(x)\,d^{d-1}x,\qquad \Delta_{W_R} = e^{-2\pi K_{\mathrm{boost}}},\;}
$$

where $K_{\mathrm{boost}} = \int_{x^1>0} x^1 T_{00}\,d^{d-1}x$ is the boost generator in the $(x^0,x^1)$ plane. The modular flow $\sigma_t$ is the **boost by rapidity $2\pi t$**, and $J_{W_R}$ is the CPT-reflection across the edge $x^1 = x^0 = 0$ (Haag duality: $J\mathcal{A}(W_R)J = \mathcal{A}(W_L)$).

The factor $2\pi$ is the Unruh temperature: an accelerated observer sees the vacuum as thermal at $T_U = 1/2\pi$ (in units of the boost parameter). This is the free-field anchor the whole subject leans on.

> **[Stated-without-proof]** Bisognano–Wichmann — an axiomatic-QFT theorem; see [[week-10-bisognano-wichmann|AQFT Wk 10]]. We **use** it.

## 3. The ball: the CHM modular Hamiltonian (worked)

Beyond the wedge, locality of $K_A$ is special. The one other case with a local modular Hamiltonian in the **vacuum** is the **ball**, by a conformal trick (CHM).

**Setup.** Take a ball $A = \{r < R\}$ on the $t=0$ slice of a CFT$_d$ vacuum; its domain of dependence is the causal diamond $\mathcal{D}_A$. CHM observe that a special conformal transformation maps $\mathcal{D}_A$ to the Rindler wedge (equivalently, maps the diamond to the static patch of a hyperbolic cylinder $\mathbb{H}^{d-1}\times\mathbb{R}_\tau$). Because the theory is conformal and the vacuum maps to the conformal vacuum, the Rindler/boost modular flow is pulled back to a flow generated by the **conformal Killing vector** that preserves $\mathcal{D}_A$:

$$
\zeta = \frac{\pi}{R}\Big[(R^2 - t^2 - r^2)\,\partial_t \;-\; 2\,t\,x^i\partial_i\Big].
$$

On the slice $t=0$ this is $\zeta = \frac{\pi}{R}(R^2 - r^2)\,\partial_t$. The modular Hamiltonian is the flux of $T_{\mu\nu}$ through $A$ along $\zeta$:

$$
K_A = \int_{t=0,\,r<R}\!\zeta^{\,t}\,T_{tt}\,d^{d-1}x
= \frac{\pi}{R}\int_{r<R}(R^2 - r^2)\,T_{00}\,d^{d-1}x.
$$

Writing $\frac{\pi}{R}(R^2-r^2) = 2\pi\cdot\frac{R^2-r^2}{2R}$ gives the standard form:

$$
\boxed{\;K_A = 2\pi\int_{r<R}\frac{R^2 - r^2}{2R}\;T_{00}(x)\,d^{d-1}x.\;}
$$

The $2\pi$ is again the modular temperature; the kernel $\frac{R^2-r^2}{2R}$ vanishes on the entangling surface $r=R$ (the flow has a fixed point there) and peaks at the centre.

**Recover Bisognano–Wichmann (the $R\to\infty$ check).** Zoom in on a point of the sphere: set $x^1 \equiv R - r$ = depth into the ball from the entangling surface, and hold $x^1$ fixed as $R\to\infty$. Then

$$
\frac{R^2 - r^2}{2R} = \frac{(R-r)(R+r)}{2R} \xrightarrow[R\to\infty]{} (R-r)\cdot\frac{2R}{2R} = x^1,
$$

so $K_A \to 2\pi\int x^1\,T_{00}\,d^{d-1}x$ — exactly the Rindler result of §2. The ball's local modular Hamiltonian degenerates to the wedge's as the ball flattens. ✓

> **[Proven within the model]** The CHM kernel and its $2\pi$ prefactor (above, given the conformal-Killing-vector $\zeta$ and conformal invariance of the vacuum). **[Proven]** the $R\to\infty$ reduction to Bisognano–Wichmann (the algebra above). The conformal map $\mathcal{D}_A \to$ hyperbolic cylinder is the one imported ingredient (CHM); we use its existence, not its construction (that is **Starred Exercise 6**).

**Why locality is special.** For a generic region, $J$ and $\Delta$ mix operators across the whole region non-locally; $K_A$ is not an integral of $T_{\mu\nu}$ with a c-number kernel. The wedge and the ball are local only because a (conformal) Killing vector preserves them. Two intervals, deformed regions, excited states — all give non-local $K_A$.

## 4. The bulk dual: modular flow ↔ Killing flow

Holographically, the boundary modular flow has a clean geometric image. For a boundary region $A$ whose entanglement wedge is $\mathcal{E}(A)$ (bounded by the RT surface $\gamma_A$), there is a **bulk Killing vector $\xi^\mu$** that:

- generates the bulk modular flow inside $\mathcal{E}(A)$;
- vanishes on $\gamma_A$ — the RT surface is its bifurcation surface (a bulk Rindler horizon);
- asymptotes to the boundary conformal Killing vector $\zeta$ of §3 near $\partial\mathcal{E}(A)$.

For the ball, $\mathcal{E}(A)$ is exactly an **AdS-Rindler wedge** of pure AdS, and $\xi$ is the AdS boost; the RT surface is its horizon. So:

$$
\text{boundary modular flow of }\mathcal{A}(A)\;\;\xleftrightarrow{\;1/N\text{-leading}\;}\;\;\text{bulk Killing flow in }\mathcal{E}(A).
$$

> **[Stated-without-proof]** modular flow ↔ bulk Killing flow at leading order in $1/N$ (FGHMV). The statement that $\xi\to 0$ on $\gamma_A$ is **[Proven within the model]** for AdS-Rindler (the boost Killing vector vanishes at its bifurcation surface — **Exercise 3**).

## 5. JLMS and the first law of entanglement (worked)

This is the payoff. **JLMS** promotes the RT formula to an operator equation relating boundary and bulk modular Hamiltonians:

$$
\boxed{\;K_A^{\mathrm{bdy}} \;=\; \frac{\widehat{\mathrm{Area}}(\gamma_A)}{4G_N} \;+\; K_{\mathcal{E}(A)}^{\mathrm{bulk}}\;+\;\dots\;}
$$

(equality as operators on the code subspace, to leading order in $G_N$; $\widehat{\mathrm{Area}}$ is the area operator of the RT surface). Equivalently, **boundary relative entropy = bulk relative entropy** on the entanglement wedge:

$$
S_{\mathrm{rel}}^{\mathrm{bdy}}(\rho_A\|\rho_A^{0}) = S_{\mathrm{rel}}^{\mathrm{bulk}}(\rho_{\mathcal{E}(A)}\|\rho_{\mathcal{E}(A)}^{0}).
$$

**The first law of entanglement (derived).** Recall the algebraic identity, for any state $\rho$ and reference $\rho_0 = e^{-K_A}$ on the same region,

$$
S_{\mathrm{rel}}(\rho\|\rho_0)
= \mathrm{Tr}\,\rho\log\rho - \mathrm{Tr}\,\rho\log\rho_0
= \underbrace{\big(\langle K_A\rangle_\rho - \langle K_A\rangle_{\rho_0}\big)}_{\Delta\langle K_A\rangle}
\;-\;\underbrace{\big(S(\rho) - S(\rho_0)\big)}_{\Delta S_A},
$$

using $K_A = -\log\rho_0$ and $S = -\mathrm{Tr}\,\rho\log\rho$. So

$$
S_{\mathrm{rel}}(\rho\|\rho_0) = \Delta\langle K_A\rangle - \Delta S_A \;\ge\; 0,
$$

with equality at $\rho=\rho_0$. Since $S_{\mathrm{rel}}\ge 0$ has its minimum (zero) at $\rho_0$, its **first-order** variation about $\rho_0$ vanishes, $\delta S_{\mathrm{rel}}=0$, giving the **first law of entanglement**:

$$
\boxed{\;\delta S_A = \delta\langle K_A\rangle.\;}
$$

(Positivity also gives the second-order statement $S_{\mathrm{rel}}\ge 0$ = relative-entropy monotonicity, but the first law is the first-order content.)

**From the first law to the gravitational first law / QES.** Feed JLMS into $\delta S_A = \delta\langle K_A\rangle$. The boundary $\delta\langle K_A^{\mathrm{bdy}}\rangle$ splits into a change in RT area plus a bulk modular-energy change:

$$
\delta S_A = \frac{\delta\langle\widehat{\mathrm{Area}}\rangle}{4G_N} + \delta\langle K^{\mathrm{bulk}}\rangle
= \frac{\delta\langle\widehat{\mathrm{Area}}\rangle}{4G_N} + \delta S_{\mathrm{bulk}},
$$

the last step using the **bulk** first law in $\mathcal{E}(A)$. The right-hand side is exactly $\delta S_{\mathrm{gen}}$ with $S_{\mathrm{gen}} = \mathrm{Area}/4G_N + S_{\mathrm{bulk}}$. Extremising $S_{\mathrm{gen}}$ over the surface is the **QES prescription** ([[sem2-week-05-quantum-extremal-surfaces|Week 5]]); demanding the first law hold for *all* $A$ yields the **linearised Einstein equations** (FGHMV) — "gravitation from entanglement."

> **[Proven]** the first law $\delta S = \delta\langle K\rangle$ from $S_{\mathrm{rel}}\ge 0$ (the algebra above; in the type III$_1$ setting it is the [[araki-uhlmann-relative-entropy|Araki–Uhlmann]] version — same identity, no density matrices). **[Stated-without-proof]** JLMS itself and the bulk first law (Iyer–Wald), imported from holography.

## 6. Why this matters here

Everything in §§1, 5 is the **same machinery as the group's own programs**. The modular operator $\Delta$, the modular conjugation $J$, and the [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] are precisely the tools used in the flat-space Bell-CHSH and relative-entropy work — only here they act on a **holographic** boundary subalgebra that is [[type-iii-von-neumann-algebras|type III₁]] at large $N$ ([[subregion-subalgebra-duality]]). The first law $\delta S = \delta\langle K\rangle$ is the bridge: it is an algebraic identity on the type III$_1$ algebra (no trace needed), yet it computes a *geometric* quantity (RT area) holographically. This is the cleanest entry point for asking whether the group's modular/relative-entropy methods can probe bulk geometry — see [[bell-chsh-in-holographic-setting]] and [[holographic-dual-embezzlement-protocol]].

## 7. Key claims and proof status

- **[Stated-without-proof]** Tomita–Takesaki ($\Delta, J, \sigma_t$, KMS at $\beta=2\pi$) — imported, AQFT Wk 5.
- **[Stated-without-proof]** Bisognano–Wichmann ($K_{W_R}=2\pi\!\int x^1 T_{00}$) — imported, AQFT Wk 10.
- **[Proven within the model]** CHM ball modular Hamiltonian $K_A = 2\pi\!\int_{r<R}\frac{R^2-r^2}{2R}T_{00}$ — derived in §3 from the conformal Killing vector $\zeta$; the conformal map's existence is imported (CHM).
- **[Proven]** $R\to\infty$ reduction of CHM to Bisognano–Wichmann (§3 algebra).
- **[Stated-without-proof]** modular flow ↔ bulk Killing flow (FGHMV) and JLMS — imported from holography.
- **[Proven]** first law of entanglement $\delta S = \delta\langle K\rangle$ from $S_{\mathrm{rel}}\ge 0$ (§5).

*No coefficients in this note are uncertain; all are standard and derived or imported as flagged. (No `CHECK` items for Wk 3.)*

## 8. What to take away

- The modular Hamiltonian is **local only for the wedge and the ball** (in the vacuum), where a (conformal) Killing vector preserves the region.
- **Bisognano–Wichmann:** $K_{W_R} = 2\pi\!\int x^1 T_{00}$, flow = boost, temperature $1/2\pi$.
- **CHM (worked):** $K_{\mathrm{ball}} = 2\pi\!\int \frac{R^2-r^2}{2R}T_{00}$, reducing to Bisognano–Wichmann as $R\to\infty$.
- Holographically, boundary modular flow = **bulk Killing flow** vanishing on the RT surface.
- **JLMS** makes this an operator equation $K^{\mathrm{bdy}} = \widehat{\mathrm{Area}}/4G_N + K^{\mathrm{bulk}}$; the **first law** $\delta S=\delta\langle K\rangle$ follows from $S_{\mathrm{rel}}\ge 0$ and seeds the QES rule and "gravitation from entanglement."
- This is the group's own modular / relative-entropy toolkit, now on a holographic type III$_1$ subalgebra.

## Exercises

**Core.**

1. **Rindler $K$.** For $W_R$ in $d=4$, write $K_{W_R}$ via Bisognano–Wichmann and show $K_{W_R}|\Psi\rangle = 2\pi H_{\mathrm{boost}}|\Psi\rangle$ with $H_{\mathrm{boost}}=\int x^1 T_{00}\,d^3x$.
2. **CHM kernel and its limit.** Starting from $\zeta = \frac{\pi}{R}[(R^2-t^2-r^2)\partial_t - 2tx^i\partial_i]$, derive $K_A = 2\pi\!\int_{r<R}\frac{R^2-r^2}{2R}T_{00}$, then verify the $R\to\infty$ reduction to the Rindler result by the $x^1=R-r$ substitution.
3. **AdS-Rindler Killing vector.** In the bulk dual of the half-space, write the boost Killing vector $\xi^\mu$ and verify $\xi^\mu\to 0$ on the RT surface (the AdS-Rindler bifurcation surface).
4. **First law.** Derive $\delta S_A = \delta\langle K_A\rangle$ from $S_{\mathrm{rel}}(\rho\|\rho_0)=\Delta\langle K_A\rangle-\Delta S_A\ge 0$. State precisely why the first-order term vanishes.

**Starred.**

5. $\star$ **Hyperbolic frame.** Show the CHM conformal map sends $\mathcal{D}_A$ to $\mathbb{H}^{d-1}\times\mathbb{R}_\tau$ and the vacuum to a thermal state at $T=1/2\pi$; hence $S_A$ = thermal entropy on the hyperbolic cylinder.
6. $\star$ **The conformal map explicitly.** Construct the special conformal transformation taking the diamond $\mathcal{D}_A$ to the Rindler wedge; identify where $\zeta$ comes from.

**Project.**

7. **Algebraic first law.** Read [[week-07-connes-cocycle-and-relative-entropy|AQFT Wk 7]]. Reproduce the first law $\delta S=\delta\langle K\rangle$ in the type III$_1$ (Araki–Uhlmann) language with no density matrices, and write a 2-page note connecting it to this week's holographic version and to [[bell-chsh-in-holographic-setting]].

## Connections to other parts of the wiki

- **Within the course:** the algebraic heart — looks back to [[week-14-hrt-and-subregion-subalgebra]] (entanglement wedge) and [[week-13-ryu-takayanagi]] (RT), forward to [[sem2-week-04-replica-trick-in-gravity]] (derives RT) and [[sem2-week-05-quantum-extremal-surfaces]] (the QES rule this week seeds). The reconstruction language reappears in [[sem2-week-11-island-formula|Wk 11]] and [[sem2-week-12-er-epr-and-tfd|Wk 12]].
- **AQFT course cross-reference:** [[week-05-tomita-operator|AQFT Wk 5]] (Tomita operator), [[week-10-bisognano-wichmann|AQFT Wk 10]] (Bisognano–Wichmann), [[week-07-connes-cocycle-and-relative-entropy|AQFT Wk 7]] (relative entropy first law) are the algebraic foundations.
- **Open questions raised or motivated:** the fate of modular flow at finite $G_N$ (crossed product / dressed algebras) — see [[week-06-modular-flow-and-kms|AQFT Wk 6]] and [[crossed-product-and-island-formula]]; whether modular/relative-entropy methods probe bulk geometry — [[bell-chsh-in-holographic-setting]], [[holographic-dual-embezzlement-protocol]].
- **Area page:** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 1. Reviewed and approved (status: final). Last revised 2026-05-28.*
