---
title: "Week 14 — HRT (covariant) and subregion–subalgebra duality"
type: lecture-notes
course: syllabus
semester: 1
week: 14
block: C
duration: "4 hours (2 lectures × 2 hours)"
status: drafting
modified: 2026-05-28
---

# Week 14 — HRT (Covariant) and Subregion–Subalgebra Duality

> *Ryu–Takayanagi ([[week-13-ryu-takayanagi|Week 13]]) needs a static bulk. This week we go covariant — the **HRT** prescription replaces "minimal" with "extremal" — and then take the conceptual leap that organises all of Semester II: the **entanglement wedge** and **subregion–subalgebra duality**. A boundary region $A$ is dual not just to an entropy but to a bulk region $W(A)$ whose operators can be reconstructed from $A$, and to a boundary subalgebra that is **type III$_1$** at large $N$. JLMS makes this an operator equation. This is the precise meeting point of holography with the group's algebraic-QFT program; the deep modular-flow treatment is [[sem2-week-03-modular-flow-on-subregions|Sem II Wk 3]].*

## Learning goals

By the end of this week, a student can:

1. Explain why RT fails in time-dependent bulks and state the covariant HRT (extremal-surface) prescription.
2. **Show** HRT reduces to RT in a static spacetime.
3. Define the entanglement wedge $W(A)$ and state entanglement-wedge reconstruction (with its QEC interpretation).
4. State subregion–subalgebra duality and the JLMS relative-entropy equality.
5. Explain why the boundary subregion algebra is type III$_1$ at large $N$ — the bridge to Semester II.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *AdS/CFT Foundations* §9** — the covariant HRT formula and entanglement wedges; *Black Hole Information* §3 for JLMS, reconstruction and the error-correction reading.
- Hubeny, Rangamani, Takayanagi (**HRT**), [arXiv:0705.0016](https://arxiv.org/abs/0705.0016) — the covariant proposal.
- Jafferis, Lewkowycz, Maldacena, Suh (**JLMS**), [arXiv:1512.06431](https://arxiv.org/abs/1512.06431) — relative entropy = bulk relative entropy.

**Prerequisites.** [[week-13-ryu-takayanagi]] (RT, minimal surfaces), [[week-06-ads-geometries]] (causal structure). For the algebra: a black-box acquaintance with modular theory ([[tomita-takesaki-modular-theory]]).

**Forward reference (not a prerequisite).** The full modular-flow / first-law treatment of JLMS is [[sem2-week-03-modular-flow-on-subregions|Sem II Wk 3]]; this week states the result and its meaning.

## 1. Why RT is not enough

The RT formula minimises area over a bulk surface on a *fixed time slice*. In a **time-dependent** bulk — a forming black hole, an infalling shell, any Lorentzian process — there is no canonical slice, and "minimal area" is ambiguous (one can always decrease a spacelike area by tilting into a timelike direction). A covariant, slice-independent prescription is needed.

## 2. The HRT prescription (worked reduction to RT)

**HRT:** the holographic entanglement entropy is

$$
\boxed{\;S_A = \frac{\mathrm{Area}(\mathcal{X}_A)}{4G_N},\;}
$$

where $\mathcal{X}_A$ is the **extremal** (not merely minimal) codimension-2 surface anchored at $\partial A$ and homologous to $A$ — a saddle of the area functional in the full Lorentzian geometry, $\delta\,\mathrm{Area}=0$ in *all* directions (spacelike and timelike). When several extremal surfaces exist, take the one of least area (equivalently, Wall's *maximin*: maximise over Cauchy slices the minimal area on each).

**Reduces to RT in static bulks (worked).** Suppose the metric has a time-reflection symmetry $t\to-t$ fixing the slice $t=0$. The area functional is even under $t\to-t$, so its variation in the *timelike* direction vanishes on the $t=0$ slice: $\partial_t\,\mathrm{Area}|_{t=0}=0$ automatically. Extremality then reduces to extremality *within* the $t=0$ slice, where the area functional is positive-definite and "extremal" = "minimal." So $\mathcal{X}_A=\gamma_A$ and HRT $=$ RT. The covariant formula contains the static one as the time-symmetric special case.

> **[Stated-without-proof]** HRT (Lorentzian gravitational path integral; analytic continuation). **[Proven]** the static reduction HRT$\to$RT (the $t\to-t$ argument above; Exercise 2).

**Worked example: the ball and its AdS-Rindler wedge.** Take a round ball $A$ on the boundary of vacuum AdS. Its causal diamond on the boundary is conformal to a Rindler wedge (the CHM map of [[sem2-week-03-modular-flow-on-subregions|Sem II Wk 3]]), and the corresponding bulk entanglement wedge $W(A)$ is exactly an **AdS-Rindler patch** — a wedge of pure AdS bounded by a bifurcate Killing horizon. The HRT surface $\mathcal{X}_A$ is the **bifurcation surface** of that horizon, and there is a bulk boost Killing vector $\xi$ generating a flow that fixes $\mathcal{X}_A$ (i.e. $\xi=0$ there). Two consequences make this the cornerstone example: (i) because the vacuum is invariant under $\xi$, the HRT surface is time-independent and equals the RT minimal surface (the static reduction in action); (ii) the boundary modular flow of the ball maps to this bulk boost — the geometric content of JLMS, derived in [[sem2-week-03-modular-flow-on-subregions|Sem II Wk 3]]. So "ball ↔ AdS-Rindler wedge ↔ boost" is the worked dictionary entry underlying everything algebraic that follows.

## 3. The entanglement wedge and reconstruction

The HRT surface $\mathcal{X}_A$ bounds, together with $A$, a bulk region. The **entanglement wedge** $W(A)$ is the bulk *domain of dependence* of any bulk Cauchy slice bounded by $A\cup\mathcal{X}_A$ — the bulk region "owned" by $A$.

**Entanglement-wedge reconstruction.** Any bulk operator localised in $W(A)$ can be represented by boundary operators acting on $A$ alone. This is sharper than the naive "causal wedge" reconstruction and is best understood as **quantum error correction** (Almheiri–Dong–Harlow; Dong–Harlow–Wall): the bulk effective field theory is a code subspace of the boundary Hilbert space, and a bulk operator deep in $W(A)$ is a logical operator protected against erasure of the complement $\bar A$. The redundancy — the same bulk operator reconstructable on different boundary regions whose wedges all contain it — is the code's error-correcting property. This QEC structure is *why* a smooth bulk can emerge from boundary entanglement, and it is the conceptual engine behind the island formula ([[sem2-week-11-island-formula|Sem II Wk 11]]).

## 4. Subregion–subalgebra duality and JLMS

Promote the geometric statement to an algebraic one. To a boundary region $A$ associate the von Neumann algebra $\mathcal{M}_A$ of operators supported on $A$. **Subregion–subalgebra duality** ([[subregion-subalgebra-duality]]) is the claim:

$$
\mathcal{M}_A \;\;\longleftrightarrow\;\; \text{bulk operator algebra of }W(A),
$$

an isomorphism (at leading order in $1/N$) between the boundary subalgebra and the bulk algebra of the entanglement wedge. **JLMS** is its quantitative form: for any two boundary states,

$$
\boxed{\;S_{\mathrm{rel}}(\rho_A\|\sigma_A) = S_{\mathrm{rel}}\big(\rho_{W(A)}\|\sigma_{W(A)}\big) + O(G_N),\;}
$$

boundary relative entropy on $\mathcal{M}_A$ equals bulk relative entropy in $W(A)$. Equivalently, as an operator equation, the boundary modular Hamiltonian splits into the area operator plus the bulk modular Hamiltonian, $K_A^{\rm bdy}=\widehat{\mathrm{Area}}/4G_N+K_{W(A)}^{\rm bulk}$ — which upgrades RT/HRT from an entropy formula to a full relative-entropy statement, and yields the first law $\delta S=\delta\langle K\rangle$. *The derivation (via modular flow and the CHM map) is [[sem2-week-03-modular-flow-on-subregions|Sem II Wk 3]];* here we record the statement and its structural meaning.

> **[Stated-without-proof]** subregion–subalgebra duality and JLMS (modular-theoretic; Sem II Wk 3). The $O(G_N)$ is the bulk-quantum-correction order.

## 5. Type III$_1$ at large $N$ — the bridge to Semester II

Why relative entropy and not entropy? Because the boundary subalgebra $\mathcal{M}_A$ is, at large $N$, a **type III$_1$ von Neumann factor** — it has *no* trace, no density matrix, and the von Neumann entropy is literally undefined ([[type-iii-von-neumann-algebras]]). The argument: at $N=\infty$ the single-trace two-point function is thermal (KMS) for *every* state ([[week-07-large-n-and-thooft-limit|Week 7]] factorisation), forcing the modular operator to be unbounded above and below — the signature of type III$_1$. So the only well-defined entropic quantity is the **[[araki-uhlmann-relative-entropy|relative entropy]]**, and JLMS is precisely the statement that *this* invariant is computed geometrically. The RT area's UV divergence is the shadow of the missing trace.

This is the exact setting of the group's program: the Bell-CHSH and relative-entropy work operate on type III$_1$ algebras with modular tools, and here those same algebras arise on the boundary of a holographic CFT ([[bell-chsh-in-holographic-setting]], [[holographic-bell-program]]). Semester II builds the crossed-product machinery that dresses this type III$_1$ algebra into a type II$_\infty$ one with a finite generalised entropy — the holographic image of "classical geometry + $1/N^2$ corrections."

> **[Sketched]** type III$_1$ at large $N$ (KMS/thermality of single-trace correlators ⟹ unbounded modular operator). Rigorous treatment: AQFT course; Liu lectures.

## 6. Key claims and proof status

- **[Stated-without-proof]** HRT (extremal surface); **[Proven]** static reduction to RT (§2).
- **[Stated-without-proof]** entanglement-wedge reconstruction / QEC (§3).
- **[Stated-without-proof]** subregion–subalgebra duality and JLMS (§4; derived in Sem II Wk 3).
- **[Sketched]** type III$_1$ at large $N$ (§5).

*No coefficients in this note are uncertain (it is structural/algebraic). No `CHECK` items for Wk 14.*

## 7. What to take away

- **HRT:** $S_A=\mathrm{Area}(\mathcal{X}_A)/4G_N$ with $\mathcal{X}_A$ **extremal** (maximin); reduces to RT in static bulks by time-reflection.
- **Entanglement wedge** $W(A)$ = bulk domain of dependence; **wedge reconstruction** = quantum error correction (bulk EFT as a boundary code).
- **Subregion–subalgebra duality**: $\mathcal{M}_A\leftrightarrow$ bulk algebra of $W(A)$; **JLMS**: boundary relative entropy = bulk relative entropy ($K^{\rm bdy}=\widehat{\mathrm{Area}}/4G_N+K^{\rm bulk}$).
- The boundary subalgebra is **type III$_1$** at large $N$ — no trace, only relative entropy is defined; JLMS computes that invariant geometrically. This is the group's algebraic setting, now holographic, and the gateway to Semester II.

## Exercises

**Core.**

1. **Global-AdS extremal surface.** For the equatorial $S^2$ on the boundary of global AdS$_5$ at $t=0$, find the extremal surface (by symmetry at constant $t$, constant $r=r_*$) and determine $r_*$.
2. **Static reduction.** Show that in a time-reflection-symmetric bulk the extremal surface lies on $t=0$ and extremality there is minimality — i.e. HRT $=$ RT.
3. **Growing wedge.** Describe how $W(A)$ grows as $A$ is enlarged in vacuum AdS; at what size does $W(A)$ first reach the bulk centre?

**Starred.**

4. $\star$ **JLMS constraint.** From JLMS, show $\rho_A=\sigma_A\Rightarrow\rho_{W(A)}=\sigma_{W(A)}$ at leading order, and explain why this is a non-trivial bulk constraint (bulk reconstruction from boundary data).
5. $\star$ **AdS-Rindler.** Show the entanglement wedge of a boundary ball is an AdS-Rindler patch whose horizon is the RT surface, and that the bulk boost Killing vector vanishes there (setup for the modular flow of Sem II Wk 3).

**Project.**

6. **Type III$_1$ and the group's program.** Read [[sem2-week-03-modular-flow-on-subregions|Sem II Wk 3]] and the AQFT [[holography-large-n-primer|holography primer]]; write a 3-page note explaining why $\mathcal{M}_A$ is type III$_1$, why only relative entropy is defined, and how JLMS / the crossed product connect to [[bell-chsh-in-holographic-setting]] and [[holographic-dual-embezzlement-protocol]].

## Connections to other parts of the wiki

- **Within the course.** Covariant extension of [[week-13-ryu-takayanagi]]; the algebra/modular treatment is [[sem2-week-03-modular-flow-on-subregions|Sem II Wk 3]]; QEC/wedge reconstruction underlies the island formula [[sem2-week-11-island-formula|Sem II Wk 11]]; type III$_1$ from [[week-07-large-n-and-thooft-limit|Week 7]].
- **Concepts.** [[ryu-takayanagi-formula]], [[subregion-subalgebra-duality]], [[type-iii-von-neumann-algebras]], [[tomita-takesaki-modular-theory]], [[araki-uhlmann-relative-entropy]].
- **AQFT course cross-reference.** The type III$_1$ / modular machinery is AQFT Block B; the holography primer §E covers the large-$N$ emergence.
- **Open questions.** [[bell-chsh-in-holographic-setting]], [[holographic-bell-program]], [[holographic-dual-embezzlement-protocol]].
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block C. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*
