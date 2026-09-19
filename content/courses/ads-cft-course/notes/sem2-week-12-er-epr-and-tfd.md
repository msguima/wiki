---
title: "Sem II Week 12 — ER=EPR, TFD, and the eternal black hole"
type: lecture-notes
course: syllabus
semester: 2
week: 12
block: 2
duration: "3 hours (lecture + seminar)"
status: final
modified: 2026-05-28
---

# Sem II Week 12 — ER=EPR, TFD, and the Eternal Black Hole

> *The cleanest entangled state in holography is the thermofield double (TFD), and its bulk dual is the most-studied geometry in the subject: the maximally extended eternal AdS-Schwarzschild black hole. This week we build the TFD, **derive** its thermal reduced state and its two-sided modular Hamiltonian $K = \beta(H_R - H_L)$, identify the bulk dual (Maldacena 2003), state ER=EPR, and explain why the wormhole is non-traversable — setting up [[sem2-week-14-traversable-wormholes-gjw|Week 14]], where a coupling opens it.*
>
> *This is the week with the tightest contact to the [[courses/ads-cft-course/syllabus|AQFT course]]: the modular Hamiltonian we derive here, $\beta(H_R - H_L)$, is exactly the generator by which Chandrasekaran–Penington–Witten **dress** the type III$_1$ single-trace algebra into a type II$_\infty$ algebra (AQFT Sem II Block 1). This course gives the holographic side of that story; the AQFT course gives the algebraic side.*

## Learning goals

By the end of this week, a student can:

1. Write the TFD state and **derive** $\rho_R = e^{-\beta H_R}/Z$ by explicit partial trace.
2. **Derive** the two-sided modular Hamiltonian $K = \beta(H_R - H_L)$ from $\Delta = \rho_R\,\rho_L^{-1}$, and identify the modular flow with two-sided Schwarzschild time.
3. State Maldacena's identification TFD ↔ eternal AdS-Schwarzschild and the partition-function match.
4. State ER=EPR and explain the entanglement-as-geometry picture.
5. Explain non-traversability from the commutation of the two boundary algebras, and preview how GJW evades it.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Black Hole Information* §5** — *Thermofield Double and Two-Sided Black Holes*.
- Maldacena, *Eternal black holes in anti-de Sitter*, JHEP 04 (2003) 021, [arXiv:hep-th/0106112](https://arxiv.org/abs/hep-th/0106112) — **the anchor**: TFD ↔ eternal AdS-Schwarzschild.
- Maldacena, Susskind, *Cool horizons for entangled black holes*, Fortsch. Phys. 61 (2013) 781, [arXiv:1306.0533](https://arxiv.org/abs/1306.0533) — the ER=EPR conjecture.

**Prerequisites (within the course).**

- [[sem2-week-08-hawking-radiation-info-problem]] — Hawking temperature; eternal-BH Penrose diagram.
- [[week-12-finite-temperature-ads-schwarzschild]] — thermal-state ↔ AdS-Schwarzschild; Hawking–Page.
- [[sem2-week-03-modular-flow-on-subregions]] — Tomita–Takesaki; the TFD modular Hamiltonian below is the two-sided cousin of the Rindler case there.

**For students coming from the AQFT course.** [[sem2-week-01-witten-setup|AQFT Sem II Wk 1]] (Witten 2022 / CPW: the type II$_\infty$ crossed product of the eternal BH dressed by $H_R-H_L$) and [[sem2-week-05-tfd-and-two-sided-modular-structure|AQFT Sem II Wk 5]] (TFD and two-sided modular structure) are the algebraic complements of this lecture.

**Assumed.** Density matrices, partial trace, the KMS condition, purification of a mixed state.

## 1. The thermofield double (worked)

Take two copies of a system, $\mathcal{H}_L\otimes\mathcal{H}_R$, with identical spectra $H_{L,R}|n\rangle_{L,R} = E_n|n\rangle_{L,R}$. The **thermofield double** at inverse temperature $\beta$ is

$$
\boxed{\;|\mathrm{TFD}\rangle = \frac{1}{\sqrt{Z(\beta)}}\sum_n e^{-\beta E_n/2}\,|n\rangle_L\otimes|n\rangle_R,
\qquad Z(\beta) = \sum_n e^{-\beta E_n}.\;}
$$

**Reduced state (derived).** Trace out the left copy:

$$
\rho_R = \mathrm{Tr}_L\,|\mathrm{TFD}\rangle\langle\mathrm{TFD}|
= \frac{1}{Z}\sum_{m,n} e^{-\beta(E_m+E_n)/2}\,\big(\mathrm{Tr}_L\,|m\rangle_L\langle n|_L\big)\,|m\rangle_R\langle n|_R.
$$

Since $\mathrm{Tr}_L\,|m\rangle_L\langle n|_L = \delta_{mn}$, the double sum collapses:

$$
\boxed{\;\rho_R = \frac{1}{Z}\sum_n e^{-\beta E_n}\,|n\rangle_R\langle n|_R = \frac{e^{-\beta H_R}}{Z}.\;}
$$

So the TFD is a **purification of the thermal state** at temperature $1/\beta$. An observer on one side sees a thermal density matrix; the purity of the global state is hidden in the cross-side entanglement. (By symmetry $\rho_L = e^{-\beta H_L}/Z$.)

> **[Proven]** the partial trace above (finite-dimensional / formal computation).

## 2. The two-sided modular Hamiltonian (worked)

The TFD is cyclic and separating for the right algebra $\mathcal{A}_R$ (acting as $\mathcal{A}_R\otimes 1$), so Tomita–Takesaki ([[sem2-week-03-modular-flow-on-subregions|Wk 3]]) applies. For a purification of this form the modular operator is

$$
\Delta = \rho_R\otimes\rho_L^{-1}.
$$

Plugging in $\rho_R = e^{-\beta H_R}/Z$ and $\rho_L = e^{-\beta H_L}/Z$, the normalisations cancel:

$$
\Delta = \frac{e^{-\beta H_R}}{Z}\cdot\Big(\frac{e^{-\beta H_L}}{Z}\Big)^{-1} = e^{-\beta H_R}\,e^{+\beta H_L} = e^{-\beta(H_R - H_L)}.
$$

Hence the **two-sided modular Hamiltonian** and flow:

$$
\boxed{\;K = -\log\Delta = \beta\,(H_R - H_L),
\qquad \sigma_t(a) = \Delta^{it}\,a\,\Delta^{-it} = e^{-i\beta(H_R-H_L)t}\,a\,e^{+i\beta(H_R-H_L)t}.\;}
$$

**Two consequences:**

- **The TFD is invariant under $H_R - H_L$:** $e^{-i(H_R-H_L)s}|\mathrm{TFD}\rangle = Z^{-1/2}\sum_n e^{-\beta E_n/2}e^{-i(E_n-E_n)s}|n\rangle_L|n\rangle_R = |\mathrm{TFD}\rangle$. The phases cancel because the two copies share the spectrum. So $(H_R-H_L)|\mathrm{TFD}\rangle = 0$ — the modular flow fixes the state, as a KMS state must.
- **It is the boost.** In the bulk (§3), $H_R - H_L$ generates the **Killing time** that runs *upward* on the right exterior and *downward* on the left — the two-sided boost fixing the bifurcation surface. This is the exact holographic analogue of the free-field Rindler–Rindler boost of [[sem2-week-03-modular-flow-on-subregions|Wk 3]] / Bisognano–Wichmann.

> **[Proven within the model]** $K = \beta(H_R-H_L)$, from $\Delta=\rho_R\rho_L^{-1}$ (finite-dim). The identification of $H_R-H_L$ with the bulk Killing time is **[Stated-without-proof]** (holographic dictionary, §3).

## 3. Eternal AdS-Schwarzschild as the bulk dual

**Maldacena's identification (2003).** The bulk dual of $|\mathrm{TFD}_\beta\rangle$ on $\mathcal{H}_L\otimes\mathcal{H}_R$ is the **maximally extended (two-sided) eternal AdS-Schwarzschild** black hole at Hawking temperature $T_H = 1/\beta$:

- Two asymptotic AdS boundaries, $\partial M_L$ and $\partial M_R$, carrying the two CFT copies.
- Two exterior regions joined behind the horizon by a non-traversable **Einstein–Rosen bridge** (the wormhole), with a bifurcation surface at the centre.
- The Euclidean continuation is the cigar geometry $M_\beta$ whose smooth tip fixes the period $\beta$; the gravitational partition function matches the field-theory one,
$$
Z(\beta) = \mathrm{Tr}\,e^{-\beta H} = Z_{\mathrm{grav}}[M_\beta].
$$

The two CFTs do not interact; all that connects them is the entanglement of the TFD — and, in the bulk, the wormhole.

> **[Stated-without-proof]** Maldacena 2003 (the TFD ↔ eternal-BH dictionary entry). The $Z(\beta)=Z_{\mathrm{grav}}[M_\beta]$ match is the [[gkp-witten-formula|GKP-Witten]] statement at finite temperature ([[week-12-finite-temperature-ads-schwarzschild|Sem I Wk 12]]).

## 4. ER=EPR

Maldacena–Susskind (2013) abstract the lesson: **entanglement is geometry**. The "ER" (Einstein–Rosen bridge) of the eternal black hole *is* the "EPR" (the L–R entanglement of the TFD). Sharpened to a conjecture:

> **ER=EPR.** Any two systems in an entangled state are connected, in a suitable bulk description, by a (possibly highly quantum, Planck-thin) wormhole; the TFD/eternal-BH pair is the smooth, semiclassical paradigm.

The entropy bookkeeping is consistent: $S(\rho_R) = $ thermal entropy of the CFT $= \mathrm{Area}(\text{horizon})/4G_N$ at leading order ([[ryu-takayanagi-formula|RT]] with the bifurcation surface as the minimal surface) — the entanglement entropy across the TFD equals the black-hole entropy.

> **[Stated-without-proof]** ER=EPR — a conjecture, consistent with all known AdS/CFT but not proven in general.

## 5. Non-traversability

Why can't you send a signal through the wormhole from $R$ to $L$?

**Boundary statement.** The two CFTs are independent factors: $\mathcal{A}_L$ and $\mathcal{A}_R$ **commute**, $[\mathcal{A}_L,\mathcal{A}_R]=0$ (they act on different tensor factors; at large $N$, $\mathcal{A}_L = \mathcal{A}_R'$). No operator on $R$ can change any expectation value on $L$: for all $a\in\mathcal{A}_R$, $b\in\mathcal{A}_L$, $\langle\mathrm{TFD}|\,b^\dagger\,a\,b\,|\mathrm{TFD}\rangle$ depends on $a$ only through $\langle a\rangle$ — acting on $R$ cannot signal to $L$.

**Bulk statement.** Correspondingly, the Einstein–Rosen bridge is **spacelike**: the two exteriors lie outside each other's light cones, and an infalling signal from $R$ hits the singularity before reaching $L$. The wormhole connects but does not transmit.

This is exactly the obstruction that [[sem2-week-13-quantum-focusing-anec|Wk 13]] (ANEC) formalises and [[sem2-week-14-traversable-wormholes-gjw|Wk 14]] (GJW) evades: coupling the two boundaries by $\sim\mathcal{O}_L\mathcal{O}_R$ breaks $[\mathcal{A}_L,\mathcal{A}_R]=0$, injects negative null energy, and renders the bridge briefly traversable.

> **[Sketched]** non-traversability from $[\mathcal{A}_L,\mathcal{A}_R]=0$ and bulk causality. The precise bulk statement uses the averaged null energy condition (Wk 13).

## 6. The AQFT bridge: this modular Hamiltonian is the CPW dressing generator

The contact with the [[courses/ads-cft-course/syllabus|AQFT course]] is unusually sharp. At large $N$ the single-trace algebra $\mathcal{A}_R$ on one boundary is a [[type-iii-von-neumann-algebras|type III$_1$ factor]] with the TFD as its cyclic-separating vector. Chandrasekaran–Penington–Witten **dress** this algebra by its modular flow — and the modular Hamiltonian is precisely the $K = \beta_H(H_R - H_L)$ we derived in §2. The [[crossed-product-construction|crossed product]] $\mathcal{A}_R\rtimes_\sigma\mathbb{R}$ is then type II$_\infty$, with a trace and a finite (generalised) entropy.

| This course (holographic) | AQFT course (algebraic) |
|---|---|
| TFD state | cyclic-separating vector $\Omega$ |
| eternal AdS-Schwarzschild | type III$_1$ factor + commutant |
| $K=\beta_H(H_R-H_L)$ (§2) | modular Hamiltonian / ADM dressing generator |
| horizon area $/4G_N$ | dressed type II$_\infty$ trace → $S_{\mathrm{gen}}$ |
| non-traversability | $[\mathcal{A}_L,\mathcal{A}_R]=0$ (Haag duality) |

So the holographic eternal black hole is the geometric face of the crossed-product machinery the group studies algebraically — see [[crossed-product-and-island-formula]] and [[sem2-week-01-witten-setup|AQFT Sem II Wk 1]].

## 7. Key claims and proof status

- **[Proven]** $\rho_R = e^{-\beta H_R}/Z$ from the TFD partial trace (§1).
- **[Proven within the model]** $K = \beta(H_R-H_L)$ from $\Delta=\rho_R\rho_L^{-1}$, and TFD-invariance under $H_R-H_L$ (§2).
- **[Stated-without-proof]** TFD ↔ eternal AdS-Schwarzschild and $Z(\beta)=Z_{\mathrm{grav}}[M_\beta]$ (Maldacena 2003).
- **[Stated-without-proof]** ER=EPR (conjecture).
- **[Sketched]** non-traversability from $[\mathcal{A}_L,\mathcal{A}_R]=0$ + bulk causality.

*No coefficients in this note are uncertain. (No `CHECK` items for Wk 12.)*

## 8. What to take away

- **TFD** $= Z^{-1/2}\sum_n e^{-\beta E_n/2}|n\rangle_L|n\rangle_R$; its one-sided reduction is **thermal**, $\rho_R = e^{-\beta H_R}/Z$.
- The **two-sided modular Hamiltonian** is $K=\beta(H_R-H_L)$, the boost fixing the bifurcation surface.
- The bulk dual is the **eternal two-sided AdS-Schwarzschild** black hole (Maldacena); $S(\rho_R) = $ horizon area$/4G_N$.
- **ER=EPR:** the wormhole *is* the entanglement.
- The wormhole is **non-traversable** because $[\mathcal{A}_L,\mathcal{A}_R]=0$ — the obstruction GJW (Wk 14) evades.
- The modular Hamiltonian here is the **CPW dressing generator**; this week is the holographic face of the AQFT crossed-product story.

## Exercises

**Core.**

1. **Reduced state.** Derive $\rho_R = e^{-\beta H_R}/Z$ from the TFD by explicit partial trace (fill in §1).
2. **Modular Hamiltonian.** From $\Delta=\rho_R\rho_L^{-1}$ derive $K=\beta(H_R-H_L)$, and verify $(H_R-H_L)|\mathrm{TFD}\rangle=0$.
3. **Partition-function match.** Show $\langle\mathrm{TFD}|e^{-\beta' H_R}|\mathrm{TFD}\rangle = Z(\beta+\beta')/Z(\beta)$ and interpret it as the Euclidean eternal-BH amplitude.

**Starred.**

4. $\star$ **Two-sided two-point function.** Compute $\langle\mathrm{TFD}|\mathcal{O}_R(t)\,\mathcal{O}_L(0)|\mathrm{TFD}\rangle$ for a free field and show it is the analytic continuation of the thermal two-point function by half a period $i\beta/2$ — the KMS signature of the L–R correlation.
5. $\star$ **No signalling.** Using $[\mathcal{A}_L,\mathcal{A}_R]=0$, show that acting with any $a\in\mathcal{A}_R$ leaves all $\mathcal{A}_L$ expectation values unchanged; relate to non-traversability.

**Project.**

6. **Map to CPW.** Read [[sem2-week-01-witten-setup|AQFT Sem II Wk 1]] / CPW §3. Identify, line by line, how the $K=\beta(H_R-H_L)$ derived here becomes the dressing generator of the type II$_\infty$ crossed product, and write a 2–3 page note bridging the two courses (feeds [[crossed-product-and-island-formula]]).

## Connections to other parts of the wiki

- **Within the course.** Back: [[week-12-finite-temperature-ads-schwarzschild]] (thermal AdS/CFT), [[sem2-week-11-island-formula]] (two-sided BH + bath), [[sem2-week-03-modular-flow-on-subregions]] (one-sided modular flow). Forward: [[sem2-week-13-quantum-focusing-anec]] (ANEC) and [[sem2-week-14-traversable-wormholes-gjw]] (opening the wormhole).
- **AQFT course cross-reference.** [[sem2-week-01-witten-setup|AQFT Sem II Wk 1]] (Witten/CPW crossed product) and [[sem2-week-05-tfd-and-two-sided-modular-structure|AQFT Sem II Wk 5]] (TFD, two-sided modular structure) — this week is their holographic complement.
- **Open questions raised or motivated.** [[bell-chsh-in-holographic-setting]] and [[holographic-bell-program]] — probing the TFD's quantum-information structure; [[crossed-product-and-island-formula]] — the algebraic/holographic dictionary.
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 2. Reviewed and approved (status: final). Last revised 2026-05-28.*
