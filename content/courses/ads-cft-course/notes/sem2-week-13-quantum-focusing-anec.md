---
title: "Sem II Week 13 — Quantum focusing and ANEC"
type: lecture-notes
course: syllabus
semester: 2
week: 13
block: 2
duration: "3 hours (lecture + seminar)"
status: drafting
modified: 2026-05-28
---

# Sem II Week 13 — Quantum Focusing and ANEC

> *Why is the eternal wormhole non-traversable, and exactly what must be violated to open it? The answer is an energy condition. Classically, the **Raychaudhuri equation** plus the null energy condition forces light rays to focus — the engine behind the area theorem and the non-traversability of [[sem2-week-12-er-epr-and-tfd|Week 12]]. Quantum mechanically the sharp statements are the **quantum focusing conjecture** (QFC), the **quantum null energy condition** (QNEC), and the **averaged null energy condition** (ANEC). We derive classical focusing, state the quantum upgrades, and show ANEC is what forbids traversable wormholes — and how the GJW deformation of [[sem2-week-14-traversable-wormholes-gjw|Week 14]] evades it.*

## Learning goals

By the end of this week, a student can:

1. **Derive** the Raychaudhuri equation and the classical focusing theorem from the NEC.
2. State the quantum focusing conjecture and how the generalised entropy enters.
3. State the QNEC $\langle T_{kk}\rangle\ge\tfrac{\hbar}{2\pi}S''$ as the $\Theta\to0$ limit of QFC.
4. State the ANEC, its status (proven for QFT), and its modular-flow proof idea.
5. Explain why traversability requires ANEC violation and how GJW achieves it.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — no corresponding chapter.** The site covers neither the quantum focusing conjecture nor the QNEC, so these notes are the primary source for this week; supplement from Bousso–Fisher–Leichenauer–Wall directly. The nearest site material is *Advanced AdS/CFT* §12 / *AdS/CFT Foundations* §9 for the entanglement first law.
- Bousso, Fisher, Leichenauer, Wall (**BFLW**), *A quantum focusing conjecture*, [arXiv:1506.02669](https://arxiv.org/abs/1506.02669).
- Faulkner, Leigh, Parrikar, Wang (**FLPW**), *Modular Hamiltonians for deformed half-spaces and the averaged null energy condition*, [arXiv:1605.08072](https://arxiv.org/abs/1605.08072).

**Prerequisites.** [[sem2-week-05-quantum-extremal-surfaces]] (generalised entropy $S_{\rm gen}$), [[sem2-week-12-er-epr-and-tfd]] (non-traversability), [[sem2-week-03-modular-flow-on-subregions]] (modular flow — used in the ANEC proof). Raychaudhuri/null congruences from GR.

**AQFT cross-reference.** The ANEC proof uses Bisognano–Wichmann modular flow ([[week-10-bisognano-wichmann|AQFT Wk 10]]) and relative-entropy monotonicity ([[week-07-connes-cocycle-and-relative-entropy|AQFT Wk 7]]).

## 1. Classical focusing (worked)

Consider a congruence of null geodesics with tangent $k^\mu$, expansion $\theta$, shear $\sigma_{ab}$, twist $\omega_{ab}$. The **Raychaudhuri equation** governs the evolution of $\theta$ along the affine parameter $\lambda$:

$$
\boxed{\;\frac{d\theta}{d\lambda} = -\frac{\theta^2}{d-2} - \sigma_{ab}\sigma^{ab} + \omega_{ab}\omega^{ab} - R_{\mu\nu}k^\mu k^\nu.\;}
$$

(Derivation: differentiate $\theta=\nabla_\mu k^\mu$ along $k$, use the geodesic equation and the Ricci identity $[\nabla_\mu,\nabla_\nu]k^\rho=R^\rho{}_{\sigma\mu\nu}k^\sigma$; the transverse trace gives $-\theta^2/(d-2)$, the trace-free part $-\sigma^2$, etc. In $d=4$ the first term is $-\theta^2/2$.) For a **hypersurface-orthogonal** congruence $\omega=0$, and using Einstein's equations $R_{\mu\nu}k^\mu k^\nu=8\pi G\,T_{\mu\nu}k^\mu k^\nu\equiv 8\pi G\,T_{kk}$, every term on the right is manifestly non-positive **provided the null energy condition (NEC) $T_{kk}\ge0$ holds**:

$$
\frac{d\theta}{d\lambda} \le -\frac{\theta^2}{d-2} \le 0.
$$

So the expansion is non-increasing: **light rays focus**. Integrating, $\theta$ reaches $-\infty$ (a caustic) in finite affine parameter if it is ever negative. This single inequality underlies the **area theorem** (horizon area never decreases — Exercise 1), the singularity theorems, and the **non-traversability** of the wormhole: a ray trying to cross the Einstein–Rosen bridge focuses and hits the singularity rather than emerging.

> **[Proven]** Raychaudhuri and classical focusing under NEC (§1; Exercise 1 derives the area theorem).

## 2. Quantum focusing (QFC)

Quantum fields violate the NEC pointwise (e.g. the Casimir effect has $T_{kk}<0$ regions), so classical focusing fails microscopically. The fix (BFLW): replace the area by the **generalised entropy** and the classical expansion by a **quantum expansion**

$$
\Theta = \theta + \frac{4G_N\hbar}{\mathcal{A}}\frac{dS_{\rm bulk}}{d\lambda},
$$

the rate of change of $S_{\rm gen}=\mathcal{A}/4G_N+S_{\rm bulk}$ per unit area along a null deformation. The **quantum focusing conjecture** is that $\Theta$ is non-increasing under further null deformation:

$$
\boxed{\;\frac{d\Theta}{d\lambda} \le 0.\;}
$$

This is the quantum Raychaudhuri statement; it implies the **generalised second law** ($dS_{\rm gen}/d\lambda\ge0$ across horizons) and reduces to classical focusing when $\hbar\to0$. QFC packages "entropy + area can only focus" — the principle that survives when the NEC does not.

## 3. The quantum null energy condition (QNEC)

Take QFC in the limit of a locally flat cut with vanishing classical expansion ($\theta\to0$, $\sigma\to0$). Then $d\Theta/d\lambda\le0$ collapses to a **local** bound relating the null energy to the second variation of the entanglement entropy:

$$
\boxed{\;\langle T_{kk}\rangle \ge \frac{\hbar}{2\pi}\,S''_{\rm out},\;}
$$

the **QNEC**, where $S''_{\rm out}=d^2S_{\rm out}/d\lambda^2$ is the second derivative of the entanglement entropy of the region to one side under a null deformation of the cut. The QNEC is remarkable: it bounds a *local* energy density below by an *entropy* second derivative — and it is **proven** for free and superrenormalisable QFTs (and, via different methods, more broadly). It is the sharp local form of "you cannot have too much negative null energy without paying in entropy variation."

> **[Stated-without-proof]** QFC (BFLW, a conjecture); **[Sketched]** QNEC as its $\Theta\to0$ limit; QNEC is **[Proven, free/super-renormalisable QFT]**.

## 4. ANEC and traversability (worked saturation)

Integrate the null energy along a complete null geodesic. The **averaged null energy condition** is

$$
\boxed{\;\int_{-\infty}^{+\infty} d\lambda\,\langle T_{kk}(\lambda)\rangle \ge 0\;}
$$

for any complete **achronal** null geodesic, in any reasonable state. Unlike the pointwise NEC, the ANEC is **true in QFT**: proven for free fields and, generally, by FLPW from the **monotonicity of relative entropy under the modular flow of a deformed half-space** (and independently by Hartman–Kundu–Tajdini from boundary causality). It is exactly strong enough to forbid the exotic geometries that violate causality: traversable wormholes and closed timelike curves.

**Worked saturation (free 2d scalar).** In the 2d Minkowski vacuum, the normal-ordered stress tensor has $\langle 0|T_{uu}(u)|0\rangle=0$ identically (the vacuum carries no null energy), so $\int du\,\langle T_{uu}\rangle=0$ — ANEC is **saturated**. In an excited state the integral is strictly positive (Exercise 2). The saturation in vacuum is the statement that flat space is exactly marginally stable against focusing — consistent with its being a solution with no caustics.

**Why traversability needs ANEC violation.** For a signal to cross the Einstein–Rosen bridge ([[sem2-week-12-er-epr-and-tfd|Week 12]]) it must receive a **time advance**, which (integrating the $UU$-Einstein/Raychaudhuri equation across the horizon) requires $\int d\lambda\,\langle T_{kk}\rangle<0$ — a *negative* averaged null energy on the horizon generator. ANEC forbids this for a *complete achronal* geodesic. The **GJW loophole** ([[sem2-week-14-traversable-wormholes-gjw|Week 14]]): coupling the two boundaries by $g\,\mathcal{O}_L\mathcal{O}_R$ makes the relevant geodesic **non-achronal / the geodesic incomplete** (the two asymptotic regions are now in causal contact through the coupling), so the ANEC theorem does not apply, and the deformation can inject the negative averaged null energy that opens the wormhole — by an $O(G_N)$ quantum amount.

> **[Proven, free QFT]** ANEC (FLPW modular argument; the 2d vacuum saturation above). **[Stated-without-proof]** the traversability ⟺ negative averaged null energy link (Week 14).

## 5. Key claims and proof status

- **[Proven]** Raychaudhuri + classical focusing under NEC (§1).
- **[Stated-without-proof]** QFC (BFLW conjecture); **[Sketched]** QNEC from QFC; **[Proven, free QFT]** QNEC (§§2–3).
- **[Proven, free QFT]** ANEC (FLPW; 2d vacuum saturation worked) (§4).
- **[Stated-without-proof]** traversability ⟺ negative averaged null energy (§4; Week 14).

*No coefficients in this note are uncertain. (No `CHECK` items for Wk 13.)*

## 6. What to take away

- **Raychaudhuri (worked):** $d\theta/d\lambda=-\theta^2/(d-2)-\sigma^2+\omega^2-8\pi G\,T_{kk}$; NEC ⟹ focusing ⟹ area theorem, singularities, non-traversability.
- **QFC:** the quantum expansion $\Theta=\theta+(4G\hbar/\mathcal{A})dS_{\rm bulk}/d\lambda$ is non-increasing — "$S_{\rm gen}$ focuses"; implies the generalised second law.
- **QNEC** ($\Theta\to0$): $\langle T_{kk}\rangle\ge\tfrac{\hbar}{2\pi}S''$ — a local energy bound from entropy, **proven** for free QFT.
- **ANEC:** $\int\langle T_{kk}\rangle d\lambda\ge0$ on complete achronal geodesics — **true in QFT** (FLPW, modular flow); forbids traversable wormholes; saturated in the 2d vacuum.
- **GJW** evades ANEC by making the geodesic non-achronal (coupling the boundaries), injecting $O(G_N)$ negative averaged null energy — Week 14.

## Exercises

**Core.**

1. **Raychaudhuri & area theorem.** Derive the null Raychaudhuri equation; with NEC and $\omega=0$ show $d\theta/d\lambda\le0$, and argue the horizon area is non-decreasing.
2. **ANEC for the 2d scalar.** Compute $\langle T_{uu}(u)\rangle$ for the free massless scalar in the 2d Minkowski vacuum (normal-ordered) and show $\int du\,\langle T_{uu}\rangle=0$ (saturated); then argue it is $>0$ in a coherent state.
3. **Traversability needs ANEC violation.** Using the integrated $UU$-Einstein equation, show a time advance requires $\int d\lambda\langle T_{kk}\rangle<0$; identify why GJW's coupling lets this happen (non-achronal geodesic).

**Starred.**

4. $\star$ **QNEC from QFC.** Take the $\theta,\sigma,\Theta\to0$ limit of $d\Theta/d\lambda\le0$ and extract $\langle T_{kk}\rangle\ge\tfrac{\hbar}{2\pi}S''$.
5. $\star$ **ANEC via modular flow.** Sketch the FLPW argument: monotonicity of relative entropy under the modular flow of a null-deformed half-space implies ANEC; cite Bisognano–Wichmann ([[week-10-bisognano-wichmann|AQFT Wk 10]]).

**Project.**

6. **Energy conditions map.** Read BFLW and FLPW; write a 3-page note organising NEC → ANEC → QNEC → QFC (which implies which, what is proven vs conjectured), and how each bears on traversable wormholes ([[sem2-week-14-traversable-wormholes-gjw|Wk 14]]) and singularity theorems.

## Connections to other parts of the wiki

- **Within the course.** Back-links: [[sem2-week-05-quantum-extremal-surfaces]] ($S_{\rm gen}$ in QFC), [[sem2-week-12-er-epr-and-tfd]] (non-traversability). Forward: [[sem2-week-14-traversable-wormholes-gjw]] (GJW violates ANEC).
- **Concepts.** [[quantum-extremal-surfaces]], [[rindler-wedges]].
- **AQFT course cross-reference.** [[week-10-bisognano-wichmann|AQFT Wk 10]] (modular flow for the ANEC proof), [[week-07-connes-cocycle-and-relative-entropy|AQFT Wk 7]] (relative-entropy monotonicity).
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 2. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*
