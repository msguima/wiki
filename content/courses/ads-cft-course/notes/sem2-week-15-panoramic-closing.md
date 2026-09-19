---
title: "Sem II Week 15 — Panoramic closing: where the field is going"
type: lecture-notes
course: syllabus
semester: 2
week: 15
block: 2
duration: "3 hours (lecture + seminar)"
status: drafting
modified: 2026-05-28
---

# Sem II Week 15 — Panoramic Closing: Where the Field Is Going

> *The course ends not with a new computation but with a map. We trace the single thread that ran through all thirty weeks — **entanglement entropy as the organising principle of holography** — from the conformal algebra to the island formula, survey the live research frontiers (higher-dimensional islands, the algebraic-holography / crossed-product programme, holographic quantum error correction, and the quantum-information diagnostics closest to this group's work), and lay out concrete first calculations a student could start tomorrow. This is the bridge from the course to research, and from this course to the [[courses/ads-cft-course/syllabus|2026 Algebraic-QFT course]].*

## Learning goals

By the end of this week, a student can:

1. Trace the course arc in a few logical steps, identifying the new input at each stage.
2. State the main open frontiers and the key obstacle in each.
3. Explain the CPW type II$_1$ result and why dressing changes the algebra type.
4. Pick an open question, state its status, and name a concrete first calculation.
5. Place this course relative to the AQFT course and the group's research lines.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Black Hole Information* §6** — *Puzzles and Research Frontiers* — factorization, ensemble averaging, open problems.
- Almheiri, Hartman, Maldacena, Shaghoulian, Tajdini, [arXiv:2006.06872](https://arxiv.org/abs/2006.06872) — the islands review, for the post-2020 synthesis.
- Chandrasekaran, Penington, Witten, *Large $N$ algebras and generalized entropy*, [arXiv:2209.10454](https://arxiv.org/abs/2209.10454) — the algebraic frontier.
- Harlow, Ooguri, *Symmetries in quantum field theory and quantum gravity*, [arXiv:1810.05338](https://arxiv.org/abs/1810.05338) — no global symmetries.

**Prerequisites.** All of the course; especially [[sem2-week-11-island-formula]], [[sem2-week-10-replica-wormholes]], [[sem2-week-03-modular-flow-on-subregions]], [[sem2-week-12-er-epr-and-tfd]], [[week-14-hrt-and-subregion-subalgebra]].

**AQFT cross-reference.** This week is where the two courses converge — see [[sem2-week-01-witten-setup|AQFT Sem II]] throughout.

## 1. The course in five steps

The whole subject compresses to one through-line — *entanglement is geometry* — refined five times:

1. **Symmetry & dictionary (Sem I A–B).** A CFT's data $\{(\Delta,\ell),C_{ijk}\}$ matches a bulk AdS theory; the isometry $\mathrm{SO}(d,2)$ *is* the conformal group, $\Delta(\Delta-d)=m^2L^2$, and large $N$ makes the bulk classical with a [[type-iii-von-neumann-algebras|type III$_1$]] boundary algebra. *New input: the holographic dictionary.*
2. **Entropy = area (Sem I C, RT).** $S_A=\mathrm{Area}(\gamma_A)/4G_N$ — entanglement entropy is a minimal surface. *New input: the RT formula.*
3. **Covariance + algebra (Wk 14, Sem II 3).** HRT (extremal surfaces), the entanglement wedge, subregion–subalgebra duality, JLMS, the first law $\delta S=\delta\langle K\rangle$. *New input: modular theory.*
4. **Quantum corrections (Sem II 5).** The QES prescription: extremise $S_{\rm gen}=\mathrm{Area}/4G_N+S_{\rm bulk}$. *New input: bulk entropy.*
5. **Islands & wormholes (Sem II 9–11).** Applied to the radiation, the QES gives an **island**; the replica-wormhole saddle competition reproduces the **Page curve** and *derives* the island rule. *New input: the connected saddles of the gravitational path integral.*

Each step solved the problem the previous one left open; together they answer Hawking's paradox within semiclassical gravity. **Exercise 2** asks you to reconstruct this chain.

## 2. Open frontier I: islands in the real world

The island formula is solid in 2d (JT) and in special higher-$d$ setups, but a **general, higher-dimensional, dynamical** island calculation for an evaporating astrophysical black hole remains hard: the QES is a genuine codimension-2 extremisation in a time-dependent geometry, the bulk entropy $S_{\rm bulk}$ is itself hard to compute, and the asymptotically-flat "bath" is not holographic. Partial results exist (eternal higher-$d$ black holes; Karch–Randall braneworlds). *Obstacle:* computing $S_{\rm bulk}$ in interacting, dynamical, higher-$d$ gravity. *Status:* active, incremental.

## 3. Open frontier II: the algebraic-holography programme (closest to this group)

The frontier where the course meets the [[courses/ads-cft-course/syllabus|AQFT 2026 course]] and the group's own work:

- At large $N$ the boundary single-trace algebra is **type III$_1$** ([[week-07-large-n-and-thooft-limit|Wk 7]], [[week-14-hrt-and-subregion-subalgebra|Wk 14]]) — no trace, no density matrix, no von Neumann entropy.
- **CPW / Witten (2022):** including the leading $1/N$ (gravitational) correction means **dressing** observables by the modular flow / ADM Hamiltonian — the [[crossed-product-construction|crossed product]]. The dressed algebra is **type II** (II$_\infty$ for the one-sided exterior, **II$_1$** for the closed-universe / observer case), which *does* have a trace and a finite **generalised entropy** $S_{\rm gen}$.
- So the holographic generalised entropy is, algebraically, the **type II trace** — a rigorous footing for "$A/4G_N+S_{\rm bulk}$."

This converts island/QES statements into operator-algebra statements, and is where rigour is being built. It is also exactly the group's territory: [[crossed-product-and-island-formula]] tracks the dictionary, and [[holographic-dual-embezzlement-protocol]] asks what the same $O(1/N^2)$ crossed-product machinery says about embezzlement cost. *Obstacle:* extending the type II construction to evaporating (non-equilibrium) black holes and to general subregions. *Status:* fast-moving, 2022–.

## 4. Open frontier III: quantum information and quantum gravity

Holography has become a source of theorems *about* quantum gravity:

- **Holographic quantum error correction** (Almheiri–Dong–Harlow; HaPPY code): the bulk effective theory is an error-correcting code in the boundary; entanglement-wedge reconstruction = decoding. The island formula is a decoding statement ([[week-14-hrt-and-subregion-subalgebra|Wk 14]]).
- **No global symmetries** (Harlow–Ooguri): exact global symmetries are impossible in quantum gravity, *derived* from the QEC structure of holography — a structural theorem from entanglement.
- **Hayden–Preskill / complexity:** information thrown into an old black hole returns in the radiation after the scrambling time, but decoding requires complexity exponential in $S_{\rm BH}$ (Harlow–Hayden) — the gap where firewall paradoxes live ([[sem2-week-11-island-formula|Wk 11]] §7).

## 5. Open frontier IV: quantum-information diagnostics (the group's lines)

The course's open questions that connect directly to the group's Bell-CHSH / relative-entropy / embezzlement programme:

- **[[bell-chsh-in-holographic-setting]]** — can Bell-CHSH violation be computed for boundary subregions of a holographic CFT, and what does it say about bulk geometry? *First calculation:* Bell-CHSH on a pair of intervals in a large-$c$ 2d holographic CFT (generalised-free-field structure), compared to the RT configuration.
- **[[holographic-bell-program]]** — the broader programme: Weyl operators and the Tsirelson bound on type III$_1$ boundary algebras.
- **[[crossed-product-and-island-formula]]** — algebraic derivation of the island rule from the dressed type II trace; the GJW deformation as a Connes cocycle ([[sem2-week-14-traversable-wormholes-gjw|Wk 14]] §6).
- **[[holographic-dual-embezzlement-protocol]]** — the bulk dual of an entanglement-embezzlement catalyst, and the $O(G_N)$ cost theorem; the closest of all to the group's current work.

## 6. Research directions for students

- **(a) Algebraic holography.** Read CPW (2209.10454) and Witten (2112.12828) alongside the AQFT course; reproduce the type III$_1\to$II crossed-product entropy for the eternal black hole, then attempt a subregion or a perturbation. *Master's-scale* (with AQFT background); the perturbative/evaporating extension is PhD-scale.
- **(b) Islands in models.** Implement the JT + bath Page-curve calculation explicitly; then a higher-$d$ braneworld. *Master's-scale* with the JT machinery of [[week-15-jt-gravity-intro|Sem I Wk 15]].
- **(c) Quantum-information diagnostics.** Pick a question from §5 and do its first calculation. Bell-CHSH-on-intervals and the embezzlement-cost calculations are *master's-accessible* (using the group's existing Weyl / Araki–Uhlmann toolkit); the full holographic cost theorem is PhD-scale.

## 7. Key claims and proof status

- **[Stated-without-proof]** CPW: the dressed black-hole-interior / observer algebra is type II$_1$ (II$_\infty$ for the one-sided exterior) — crossed product of the type III$_1$ algebra by the modular/ADM flow.
- **[Sketched]** algebraic re-derivation of the island formula as a type II trace ([[crossed-product-and-island-formula]]).
- **[Stated-without-proof]** holographic QEC (Almheiri–Dong–Harlow; HaPPY) and the Harlow–Ooguri no-global-symmetries theorem.

*This is a synthesis/outlook week; no new coefficients. No `CHECK` items for Wk 15.*

## 8. What to take away

- The whole course is one thread — **entanglement is geometry** — refined in five steps: dictionary → RT → modular/JLMS → QES → islands/wormholes.
- **Live frontiers:** higher-$d$ dynamical islands; the **algebraic (crossed-product) programme** making $S_{\rm gen}$ a type II trace (CPW — the group's territory); holographic QEC and no-global-symmetries; quantum-information diagnostics (Bell, embezzlement).
- **Closest contact with this group:** dressing type III$_1$ → type II (crossed product), the GJW = Connes-cocycle link, and the embezzlement cost theorem — [[crossed-product-and-island-formula]], [[holographic-dual-embezzlement-protocol]], [[bell-chsh-in-holographic-setting]].
- This course is the **holographic complement** of the AQFT 2026 course; together they give the geometric and algebraic faces of the same modern story.

## Exercises

**Core / project.**

1. **Master-project milestone essay (2 pages).** Choose one open question — [[bell-chsh-in-holographic-setting]], [[holographic-bell-program]], [[crossed-product-and-island-formula]], or [[holographic-dual-embezzlement-protocol]] — summarise what is known vs open, propose one concrete first calculation, and explain the insight it would give.
2. **Five-step synthesis.** Reconstruct the RT → island logic in $\le5$ steps, naming the new input and the problem solved at each.
3. **CPW type II.** Explain in one paragraph why the dressed interior algebra is type II$_1$ rather than III$_1$, and identify which step requires the ADM-Hamiltonian dressing.

**Starred.**

4. $\star$ **No global symmetries.** Sketch the Harlow–Ooguri argument from holographic QEC; identify where entanglement-wedge reconstruction enters.
5. $\star$ **Bell on intervals.** Set up (don't fully evaluate) the Bell-CHSH correlator for two intervals in a large-$c$ 2d holographic CFT using the generalised-free-field two-point function; identify the RT data it should be compared to.

## Connections to other parts of the wiki

- **Within the course.** Synthesises everything; especially [[sem2-week-11-island-formula]], [[sem2-week-10-replica-wormholes]], [[sem2-week-03-modular-flow-on-subregions]], [[week-14-hrt-and-subregion-subalgebra]], [[week-13-ryu-takayanagi]].
- **AQFT course cross-reference.** [[sem2-week-01-witten-setup|AQFT Sem II]] (crossed product / type II) is the algebraic complement of this whole block.
- **Concepts.** [[crossed-product-construction]], [[type-iii-von-neumann-algebras]], [[quantum-extremal-surfaces]], [[page-curve]].
- **Open questions (the group's lines).** [[bell-chsh-in-holographic-setting]], [[holographic-bell-program]], [[crossed-product-and-island-formula]], [[holographic-dual-embezzlement-protocol]].
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 2. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*

*End of Sem II Block 2 — and of the course's black-hole-information arc.*
