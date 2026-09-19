---
title: "Sem II Week 8 — Hawking radiation and the information problem"
type: lecture-notes
course: syllabus
semester: 2
week: 8
block: 2
duration: "3 hours (lecture + seminar)"
status: drafting
modified: 2026-05-28
---

# Sem II Week 8 — Hawking Radiation and the Information Problem

> *Block 2 opens with the puzzle that organises the rest of the course. Hawking's 1975 calculation shows a black hole radiates **thermally** — and, taken at face value, that a pure initial state evaporates into a mixed one, breaking unitarity. We reproduce the thermal spectrum from the Bogoliubov transformation (with the detailed-balance step worked in full), state the paradox precisely against the **Page-curve** target, sharpen it in AdS/CFT (where the boundary is manifestly unitary), and survey the firewall argument and the landscape of proposals. Weeks 9–11 then resolve it with replica wormholes and islands.*

## Learning goals

By the end of this week, a student can:

1. Reproduce the Bogoliubov argument and **derive** the thermal occupation $\langle n_\omega\rangle=1/(e^{\omega/T_H}-1)$ from detailed balance.
2. State the information paradox precisely: thermal radiation + complete evaporation $\Rightarrow$ pure $\to$ mixed.
3. State the Page-curve target and why Hawking's monotonic entropy contradicts it.
4. Explain why AdS/CFT makes information loss untenable.
5. State the firewall (AMPS) argument and what each proposal sacrifices.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Black Hole Information* §1** — the *Hawking Radiation and Information Loss* page.
- Hawking, *Particle creation by black holes*, Commun. Math. Phys. 43 (1975) 199 — the original.
- Mathur, *The information paradox: a pedagogical introduction*, [arXiv:0909.1038](https://arxiv.org/abs/0909.1038).
- Almheiri, Hartman, Maldacena, Shaghoulian, Tajdini, *The entropy of Hawking radiation*, [arXiv:2006.06872](https://arxiv.org/abs/2006.06872) — §§1–2.

**Prerequisites.** [[week-12-finite-temperature-ads-schwarzschild]] (Hawking $T$ from the Euclidean tip), [[sem2-week-05-quantum-extremal-surfaces]] (QES — why the semiclassical answer must fail), [[sem2-week-06-jt-gravity-page-curve]] (the explicit JT Page curve). Bogoliubov transformations and curved-space vacuum ambiguity.

**AQFT cross-reference.** The Hawking state is a **KMS state** at $T_H$ for Schwarzschild time translation — the algebraic characterisation of thermality; see [[week-04-kms-states-and-type-III|AQFT Wk 4]].

## 1. Hawking's calculation (worked thermal spectrum)

Quantise a free scalar on the background of a collapsing star. The natural vacuum at early times (**in**-vacuum, defined by positive-frequency modes on past null infinity $\mathscr{I}^-$) is *not* the natural vacuum at late times (**out**-vacuum on $\mathscr{I}^+$), because the modes are mixed by propagation through the time-dependent collapse geometry. Expand the out-modes in in-modes via a **Bogoliubov transformation**,

$$
a^{\rm out}_\omega = \sum_{\omega'}\big(\alpha_{\omega\omega'}\,a^{\rm in}_{\omega'} + \beta_{\omega\omega'}\,a^{\rm in\,\dagger}_{\omega'}\big).
$$

The presence of the **$\beta$** (mode-mixing creation) piece means the in-vacuum contains out-particles: the expected out-number is

$$
\langle 0_{\rm in}|\,N^{\rm out}_\omega\,|0_{\rm in}\rangle = \sum_{\omega'}|\beta_{\omega\omega'}|^2.
$$

**The key input** is how a late-time out-mode, traced back through the collapse, behaves near the horizon: it is **exponentially blueshifted**, and the tracing-back amounts to analytically continuing the mode around the horizon. A mode of frequency $\omega$ acquires, under continuation across the horizon (a branch point), a relative factor $e^{-\pi\omega/\kappa}$ ($\kappa$ = surface gravity). This gives the **detailed-balance** relation between the Bogoliubov coefficients,

$$
\boxed{\;\frac{|\beta_\omega|^2}{|\alpha_\omega|^2} = e^{-2\pi\omega/\kappa} = e^{-\omega/T_H},\qquad T_H = \frac{\kappa}{2\pi}.\;}
$$

**Now solve for the spectrum.** Bosonic Bogoliubov coefficients obey the normalisation $|\alpha_\omega|^2-|\beta_\omega|^2=1$. Combine with detailed balance, $|\alpha_\omega|^2=|\beta_\omega|^2 e^{\omega/T_H}$:

$$
|\beta_\omega|^2 e^{\omega/T_H} - |\beta_\omega|^2 = 1
\;\Longrightarrow\;
|\beta_\omega|^2\big(e^{\omega/T_H}-1\big)=1
\;\Longrightarrow\;
\boxed{\;\langle n_\omega\rangle = |\beta_\omega|^2 = \frac{1}{e^{\omega/T_H}-1}.\;}
$$

This is the **Planck/Bose–Einstein distribution** at temperature $T_H=\kappa/2\pi$ — a *thermal* flux. For Schwarzschild, $\kappa=1/4GM$, so $T_H=1/(8\pi GM)$. The temperature also follows from the Euclidean smoothness argument of [[week-12-finite-temperature-ads-schwarzschild|Week 12]] ($\beta=4\pi/f'(r_h)$) — two routes, same $T_H$.

**Information loss.** Crucially, the out-state is not just thermal in expectation: tracing over the modes that fall *into* the black hole leaves the exterior radiation in a **mixed** (thermal) density matrix, with **no dependence on the details of the initial state** — only on $M$, $Q$, $J$. If the black hole evaporates completely, a pure initial state has become a mixed thermal final state: $\rho_{\rm final}=\mathrm{Tr}(\dots)$ with $S\neq0$.

> **[Sketched]** the thermal flux $\langle n_\omega\rangle=1/(e^{\omega/T_H}-1)$ (Bogoliubov + detailed balance, worked above; the $e^{-\pi\omega/\kappa}$ continuation factor is the one imported step — Exercise 1 / Hawking 1975).

## 2. The paradox, precisely

The conflict is about **purity**, not energy:

- **Quantum mechanics** evolves a pure state to a pure state ($S=0$ throughout): unitarity.
- **Hawking's semiclassical calculation** gives radiation in a mixed thermal state whose entropy *grows monotonically* as quanta accumulate; complete evaporation leaves a mixed state, $S_{\rm rad}>0$, from a pure start.

These cannot both be right. Either unitarity fails (information is destroyed — abhorrent in a quantum theory, and impossible in AdS/CFT, §4), or **Hawking's calculation is incomplete**. The paradox is sharp because Hawking's computation is "just QFT in curved space," seemingly trustworthy while the black hole is large.

## 3. The Page-curve target

What *should* $S_{\rm rad}(t)$ do if evaporation is unitary? **Page's argument**: model evaporation as a pure global state slowly transferring from "black hole" to "radiation." When the radiation is a small subsystem, its entropy tracks its (growing) thermal entropy; once the radiation is the *larger* subsystem (past the **Page time**), its entropy is bounded by the *shrinking* black-hole entropy $S_{\rm BH}=A/4G$. So the fine-grained $S_{\rm rad}(t)$ must

$$
\text{rise, peak at } t_{\rm Page}\ (\text{where } S_{\rm rad}=S_{\rm BH}),\ \text{then fall to }0.
$$

This is the **Page curve** ([[page-curve]], [[sem2-week-09-page-curve|Week 9]]). Hawking's monotonically rising entropy follows the rising branch but never turns over — it misses the descending branch entirely. *Reproducing the turnover from gravity* is the central problem, solved in Weeks 10–11 (replica wormholes / islands).

## 4. AdS/CFT framing

Holography makes information loss **untenable**, sharpening the paradox into a well-posed question. The boundary CFT is a unitary quantum system; the eternal/evaporating black hole is *a state in it* evolving by a Hermitian Hamiltonian. So:

- Information **cannot** be lost — the boundary evolution is unitary by construction.
- Therefore the bulk semiclassical (Hawking) calculation **must** be missing something at non-perturbative order in $G_N\sim1/N^2$.
- The fine-grained radiation entropy, computed holographically (via [[sem2-week-05-quantum-extremal-surfaces|QES]] / islands), **must** reproduce the Page curve.

AdS/CFT does not by itself say *how* the bulk encodes the purification — that is the content of entanglement-wedge reconstruction ([[week-14-hrt-and-subregion-subalgebra|Wk 14]]) and the island formula ([[sem2-week-11-island-formula|Wk 11]]) — but it guarantees that it *must*, and turns "is information lost?" into "which bulk saddle dominates?"

## 5. The firewall argument and the landscape

**AMPS firewall.** Sharpen the tension with three assumptions: (i) unitarity (radiation purifies), (ii) the infalling observer sees a smooth horizon (equivalence principle / effective field theory), (iii) **monogamy of entanglement**. A late Hawking quantum $b$ must be (a) maximally entangled with the early radiation $R$ (for unitarity/Page) *and* (b) maximally entangled with its interior partner $\tilde b$ (for a smooth horizon). Monogamy forbids $b$ being maximally entangled with two systems at once — contradiction. Something must give: dropping (ii) means a **firewall** of high-energy quanta at the horizon (no smooth interior). The island/replica-wormhole resolution instead reinterprets (a): past the Page time the interior partner $\tilde b$ **is in the entanglement wedge of $R$** (it is in the island), so (a) and (b) are the *same* entanglement, not two — monogamy is respected and the horizon stays smooth.

**Landscape (one line each).** *Complementarity* (Susskind): no single observer sees both copies, so no contradiction — strained by AMPS. *Soft hair* (Hawking–Perry–Strominger): horizon symmetries store information — unclear if enough. *Remnants*: Planckian leftovers holding the information — pathological (infinite species). *Fuzzballs* (Mathur): no smooth interior, microstate geometries — string-theoretic, hard to make generic. The **island** program (Weeks 9–11) is the current best-developed, semiclassical-gravity-internal resolution.

## 6. Key claims and proof status

- **[Sketched/Proven]** thermal spectrum $\langle n_\omega\rangle=1/(e^{\omega/T_H}-1)$ from Bogoliubov + detailed balance (§1; the $e^{-\pi\omega/\kappa}$ continuation factor imported).
- **[Stated-without-proof]** information loss from complete evaporation of a thermal state (§1–2).
- **[Stated-without-proof]** the Page-curve requirement of unitarity (§3; derived in Wk 9).
- **[Stated-without-proof]** the AMPS firewall trilemma and the landscape (§5).

*No coefficients in this note are uncertain. (No `CHECK` items for Wk 8.)*

## 7. What to take away

- **Hawking (worked):** Bogoliubov $\beta$-mixing + detailed balance $|\beta|^2/|\alpha|^2=e^{-\omega/T_H}$ and $|\alpha|^2-|\beta|^2=1$ give $\langle n_\omega\rangle=1/(e^{\omega/T_H}-1)$ — a thermal flux at $T_H=\kappa/2\pi$ ($=1/8\pi GM$ for Schwarzschild).
- The radiation is **mixed and state-independent** ⟹ complete evaporation takes pure → mixed: the **information paradox** (about purity, not energy).
- Unitarity demands the **Page curve** (rise, peak at $t_{\rm Page}$ where $S_{\rm rad}=S_{\rm BH}$, fall to 0); Hawking misses the turnover.
- **AdS/CFT** guarantees unitarity ⟹ the semiclassical calculation must be incomplete at $O(1/N^2)$; the fix is islands/replica wormholes (Weeks 10–11).
- **AMPS**: unitarity + smooth horizon + monogamy clash; islands resolve it by putting the interior partner in the radiation's entanglement wedge.

## Exercises

**Core.**

1. **Thermal spectrum.** Reproduce §1: from $|\alpha_\omega|^2-|\beta_\omega|^2=1$ and $|\beta_\omega|^2/|\alpha_\omega|^2=e^{-\omega/T_H}$, derive $\langle n_\omega\rangle=1/(e^{\omega/T_H}-1)$; identify $T_H=\kappa/2\pi=1/8\pi GM$ for Schwarzschild.
2. **Evaporation lifetime.** Using $dM/dt\sim-\sigma T_H^4 A$ with $A\sim G^2M^2$, $T_H\sim1/GM$, show $dM/dt\sim-1/(G^2M^2)$, hence $t_{\rm evap}\sim G^2M^3$; estimate it for a solar-mass black hole.
3. **Firewall trilemma.** State the AMPS assumptions (unitarity, smooth horizon, monogamy), derive the contradiction, and identify which assumption each proposal (complementarity, firewall, islands) sacrifices or reinterprets.

**Starred.**

4. $\star$ **Detailed balance from continuation.** Sketch why analytically continuing an out-mode around the horizon produces the factor $e^{-\pi\omega/\kappa}$, hence $|\beta|^2/|\alpha|^2=e^{-2\pi\omega/\kappa}$ (Hawking 1975; Unruh).
5. $\star$ **KMS.** Show the Hawking state satisfies the KMS condition at $T_H$ w.r.t. Schwarzschild time translation; connect to [[week-04-kms-states-and-type-III|AQFT Wk 4]].

**Project.**

6. **Page's theorem.** Read Page 1993; reproduce the average entropy of a subsystem of a random pure state and hence the Page curve, setting up [[sem2-week-09-page-curve|Week 9]].

## Connections to other parts of the wiki

- **Within the course.** Opens Block 2; the Page-curve target drives [[sem2-week-09-page-curve]], [[sem2-week-10-replica-wormholes]], [[sem2-week-11-island-formula]]. Back-links: [[week-12-finite-temperature-ads-schwarzschild]] ($T_H$), [[sem2-week-06-jt-gravity-page-curve]] (explicit JT Page curve).
- **AQFT course cross-reference.** [[week-04-kms-states-and-type-III|AQFT Wk 4]] — the Hawking state as a KMS/type-III thermal state.
- **Open questions.** [[bell-chsh-in-holographic-setting]] — quantum-information structure of Hawking radiation.
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 2. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*
