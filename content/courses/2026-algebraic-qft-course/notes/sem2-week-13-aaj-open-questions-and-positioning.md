---
title: "Sem II Week 13 — Ahmad–Jefferson III: Open Questions and Positioning the Field"
type: lecture-notes
course: syllabus
semester: 2
week: 13
block: 4
duration: 4 hours (seminar + student final-topic presentations)
prerequisites: Sem II Wks 11–12 (cocycle perturbation, Mini-Calc 4)
target_paper: "Ahmad & Jefferson, arXiv:2501.01487 §6 and outlook"
modified: 2026-08-23
---

# Sem II Week 13 — Ahmad–Jefferson III: Open Questions and Positioning the Field

> *Block 4 computed the second-order generalized-entropy correction under a GJW traversal — the technical climax of the course. This week we step back and ask: where does AAJ leave the program? We survey the open-question landscape (non-perturbative regimes, higher orders, bulk interpretation of the algebraic corrections, other deformations, and the embezzlement connection to the group's own research), and students present their final-write-up topics for group feedback. The goal is to position each student's work against the live frontier before the final paper. Block 5 (MSY) then supplies the bulk side, so the algebra/bulk gap can be stated honestly.*

## 0. Reading

**Primary:**
- Ahmad & Jefferson, arXiv:2501.01487, **§6 and outlook** (limitations, open directions).
- Re-read of CPW (arXiv:2209.10454) final section (limitations of the unperturbed construction).

**Secondary / gentler:**
- Sem II Wks 11–12 (the cocycle machinery and Mini-Calc 4 these questions extend).

**Optional research reading:**
- Faulkner, Li, Wang, "A modular toolkit for bulk reconstruction," arXiv:2206.00027 (modular methods that may go beyond perturbative).
- van Daele / recent embezzlement-in-type-III literature (the group's [[entanglement-embezzlement|embezzlement]] program).
- Gesteau, "Large N von Neumann algebras and the renormalization of Newton's constant," arXiv:2302.01938 (algebraic running of $G_N$).

## 1. What AAJ achieved, and where it stops

### 1.1 The achievement

AAJ's contribution, in one sentence: **algebraic perturbation theory for the generalized entropy**, taken to second order in a GJW deformation, yielding a structured set of 20 corrections that assemble into a bulk-interpretable $\delta S_{\rm gen}$. The tool — cocycle perturbation theory on the dressed type II$_\infty$ algebra — is reusable and is the main deliverable beyond the specific numbers.

> **Physical picture.** Before AAJ, the crossed-product framework (Witten, CPW, Liu) computed the generalized entropy of *equilibrium* configurations. AAJ made it a *dynamical* tool: you can now perturb the dressed algebra and watch $S_{\rm gen}$ respond, order by order, with the cocycle as the expansion parameter. This is the difference between "here is the entropy of the black hole" and "here is how the entropy changes when you throw something in / open the wormhole." The framework is young, and the natural questions are all about how far it extends.

### 1.2 Where it stops

AAJ go to **quadratic order** in $g$, in the **perturbative** regime, for the **GJW (double-trace)** deformation, with the bulk interpretation of individual terms **partially** established. Each of these four boundaries is an open direction.

## 2. The open-question landscape

We organize AAJ §6's outlook into five questions, each a candidate final-paper or thesis direction.

### 2.1 Beyond perturbative

**Question 1.** AAJ expand to finite order in $g$. What is the **non-perturbative** structure? Does the dressed algebra itself change character at large deformation (e.g. a phase transition in the wormhole's traversability)?

> **Physical picture.** Perturbatively, the GJW pulse is a small reorganization of modular time. Non-perturbatively, a strong enough coupling could change the *causal structure* — fully merging the two sides, or collapsing the wormhole. Algebraically this would show up as a change in the commutant relation $\mathcal{A}_R' = \mathcal{A}_L$ (the algebraic ER=EPR criterion, Sem II Wk 10): a strong deformation might break or restructure it. No one has a controlled non-perturbative handle; this is wide open.

### 2.2 Higher-order corrections

**Question 2.** AAJ enumerate 20 corrections at $O(g^2)$. What is the **full enumeration at higher orders**? Is there a generating function or a diagrammatic organization (a "modular Feynman rules")?

This is the most concrete and tractable direction — a careful combinatorial/diagrammatic extension of the Mini-Calc 4 bookkeeping. A good final-paper topic for a computationally inclined student.

### 2.3 Bulk interpretation

**Question 3.** Each of AAJ's algebraic corrections — which **bulk geometric feature** does it correspond to? The throat shift, the shape of the deformed ER bridge, the Shapiro advance? AAJ establish the dictionary partially; completing it is open.

> **Physical picture.** The algebra produces a sum of 20 numbers; the bulk produces a deformed geometry. Some terms clearly map (the modular-energy shift ↔ horizon-area change). Others — especially the cross-sector terms — do not yet have a clean bulk reading. Closing this is exactly the algebra/bulk matching the course flags as unfinished (Block 5 Wk 14 honest scoping). MSY gives the bulk Shapiro shift; AAJ gives the algebraic corrections; the precise map between them is not established at the rigorous level.

### 2.4 Other deformations

**Question 4.** AAJ focus on GJW (a double-trace $\mathcal{O}_L\mathcal{O}_R$). What about deformations by **conserved currents** or the **stress tensor**? These are more constrained (Ward identities) and may be more or less lossy. Different deformations probe different aspects of the dressed algebra.

### 2.5 Connection to embezzlement (the group's program)

**Question 5.** The Connes cocycle is *also* the natural tool for **entanglement embezzlement** in type III$_1$ algebras (van Daele; the group's Ph.D. work, [[entanglement-embezzlement]]). What is the relation between cocycle *perturbation theory* (AAJ) and cocycle-based *embezzlement protocols*?

This is the question in the list that touches the group's own program most directly, so it is worth making concrete rather than leaving at the level of a slogan. The mechanism of embezzlement can be exhibited completely in finite dimensions, and doing so shows exactly what the type III$_1$ limit supplies. **[Computed — finite-dimensional catalyst; the exactness claim in III$_1$ is stated with refs.]**

**The van Dam–Hayden catalyst.** Take the bipartite state
$$
|\mu_n\rangle = \frac{1}{\sqrt{C_n}}\sum_{j=1}^{n}\frac{1}{\sqrt j}\;|j\rangle_A\otimes|j\rangle_B,
\qquad C_n = \sum_{j=1}^{n}\frac1j = H_n \simeq \ln n + \gamma,
$$
whose Schmidt probabilities are $p_j = 1/(jC_n)$ — a harmonic, and therefore nearly scale-invariant, spectrum. The claim is that Alice and Bob can extract a Bell pair from $|\mu_n\rangle$ by local unitaries alone, leaving the catalyst almost unchanged.

**Why it works, computed.** Tensoring the catalyst with a Bell pair doubles the Schmidt rank and halves every probability, so $|\mu_n\rangle\otimes|\Phi^+\rangle$ has spectrum
$$
\Big\{\tfrac{1}{2jC_n}\ \text{with multiplicity } 2\Big\}_{j=1}^{n},
$$
while the larger catalyst $|\mu_{2n}\rangle$ has spectrum $\{1/(kC_{2n})\}_{k=1}^{2n}$. Compare them by pairing $k = 2j-1$ with $k = 2j$: the target contributes $\tfrac{1}{2j-1} + \tfrac{1}{2j}$ where the doubled state contributes $\tfrac{1}{2j}+\tfrac{1}{2j} = \tfrac1j$. The two agree in the large-$j$ tail, and the *total* discrepancy is
$$
\sum_{j\ge1}\Big(\frac{1}{2j-1} - \frac{1}{2j}\Big) = \ln 2,
$$
the alternating harmonic series. Note what this says: the mismatch between "catalyst plus one ebit" and "bigger catalyst" is **finite and $n$-independent**, while the normalization $C_{2n}\simeq\ln 2n$ **diverges**. The relative error is therefore of order $\ln 2/C_{2n} = O(1/\log n)$, and since the overlap of two pure states with sorted Schmidt spectra $\{p_i\}$, $\{q_i\}$ is $\sum_i\sqrt{p_iq_i}$, the extraction fidelity satisfies
$$
\big|\langle \mu_{2n}\,|\,U_A\otimes U_B\,|\,\mu_n\otimes\Phi^+\rangle\big| \;=\; 1 - O\!\big(1/\log n\big) \;\xrightarrow[n\to\infty]{}\; 1 .
$$
**[Stated — refs: van Dam & Hayden, quant-ph/0201041, for the error bound; the $\ln 2$ mismatch above is the computation behind it.]** A Bell pair has been produced from nothing but local unitaries, and the catalyst is returned in a state arbitrarily close to its original — but only *arbitrarily* close, never exactly, at any finite $n$.

**Where type III$_1$ enters.** The obstruction at finite $n$ is that the Schmidt spectrum is only *approximately* scale-invariant: it has a top ($j=1$) and a bottom ($j=n$), and the $\ln 2$ mismatch is the price of those edges. A type III$_1$ algebra has no such edges. Its modular spectrum is all of $\mathbb{R}$ (Sem II Wk 9 §2.3), which is exactly the statement that the "Schmidt spectrum" is scale-invariant with no top and no bottom, and the finite-$n$ error has nowhere to come from. Embezzlement becomes **exact**, and every normal state on a III$_1$ factor is an embezzling state. The $n\to\infty$ limit of the catalyst is not a technical convenience; it is the passage from type I to type III$_1$.

**The link to AAJ.** Both programs use the same object for the same structural reason. Embezzlement asks: given two states of the catalyst, what unitary in the algebra carries one to the other? Cocycle perturbation theory asks: given two states of the dressed algebra, what unitary relates their modular flows? The answer to both is the Connes cocycle $(D\omega_V/D\omega)_t$, because in the absence of a trace it is the only object that compares two states, and both questions are questions about comparing states. So a GJW deformation *is*, read from the embezzlement side, a particular cocycle-implemented state change — and one can ask whether the entropy corrections AAJ compute have an information-theoretic reading as embezzlement costs. That question is open, and it is the most direct bridge from the recent holographic literature to the group's [[bell-inequalities-qft|Bell-CHSH]] and [[entanglement-embezzlement|embezzlement]] program.

> **Physical picture.** Embezzlement extracts entanglement from a catalyst with arbitrarily good fidelity — exact in type III$_1$, impossible exactly in type I or II (Sem I Wk 12). The computation above says why in one line: the catalyst works to the extent that its entanglement spectrum looks the same after you take a piece out of it, and a harmonic spectrum looks the same up to its two edges. Type III$_1$ is the algebra of a system with no edges — no largest mode, no smallest — which is the same absence of a scale that made the local algebras of QFT type III$_1$ in the first place (Wk 9 §2.1). The vacuum of a quantum field theory is an infinitely good catalyst for the same reason that its entanglement entropy diverges. That is a genuinely striking statement, and it is why the group's embezzlement line and its Bell-CHSH line are the same subject seen from two sides.

## 3. Positioning the field

### 3.1 Two kinds of progress

AAJ enables both:

- **Incremental:** "compute more orders," "do other deformations," "nail down the bulk dictionary term by term." Tractable, valuable, good for a first paper.
- **Structural:** "the cocycle perturbation framework is now a standard tool." This reframes how one thinks about gravitational entropy dynamics — as algebraic perturbation theory on a type II$_\infty$ algebra. The structural shift may matter more than any single number.

### 3.2 The natural next papers

For a student wanting to continue:

- AAJ's own outlook (higher orders, other deformations).
- Faulkner–Li–Wang modular-toolkit methods (arXiv:2206.00027) for going beyond perturbative.
- The Gesteau-style algebraic renormalization of $G_N$ (arXiv:2302.01938) — connecting the dressed-algebra structure to the running of Newton's constant.
- The group's embezzlement program — applying cocycle perturbation theory to embezzlement cost.

## 4. Student final-topic presentations

The second half of the week is **student presentations** (the seminar deliverable). Each student gives a short talk on their chosen final-write-up topic (Block 2 §7 options, refined through Blocks 3–4):

1. **Free-field cocycle perturbation** — extend Mini-Calc 4; the most self-contained option, directly building on Week 12.
2. **Bell-CHSH in holographic settings** — the wiki open question [[bell-chsh-in-holographic-setting]]; connect Summers–Werner (Sem I Wk 11) to large-$N$ boundary algebras.
3. **Embezzlement on the crossed product** — Question 5 above; the group's program.
4. **Critical exposition** — of CPW, AAJ, or CLPW (de Sitter, Block 5 Wk 14).

Feedback from the group sharpens each plan against the open-question landscape before the final paper. Students refine their Week 10 drafts; the final is due Week 14 (with presentations in Week 15).

## 5. What to take away

- **AAJ's achievement:** algebraic (cocycle) perturbation theory for $S_{\rm gen}$, to second order in a GJW deformation — a reusable dynamical tool, not just a number.
- **Four boundaries, each an open direction:** quadratic order (→ higher orders / generating function), perturbative regime (→ non-perturbative / traversability transition), GJW deformation (→ currents, stress tensor), partial bulk dictionary (→ complete it).
- **The embezzlement bridge (computed, §2.5):** the van Dam–Hayden catalyst works because its harmonic Schmidt spectrum is nearly scale-invariant; the mismatch between "catalyst + one ebit" and "bigger catalyst" is exactly $\ln 2$, finite, against a normalization $C_{2n}\simeq\ln 2n$ that diverges — hence fidelity $1 - O(1/\log n)$. Type III$_1$ removes the spectrum's edges and makes embezzlement exact. The same Connes cocycle drives this and AAJ's perturbation theory, because without a trace it is the only object that compares two states.
- **Two kinds of progress:** incremental (more orders, other deformations) and structural (the framework itself as a standard tool). Both are open.
- **The algebra/bulk gap is real and acknowledged:** AAJ's algebraic corrections and MSY's bulk geometry are not yet matched rigorously — the honest frontier the course does not pretend to close.

## 6. Looking ahead

Block 5 (Weeks 14–15) supplies the **bulk side**: Maldacena–Stanford–Yang's "Diving into traversable wormholes," the gravitational picture of the GJW deformation AAJ computed algebraically. Seeing the two side by side is the clearest way to understand what the algebra captures (entropy corrections) and what it does not (the Shapiro shift, directly). Week 14 also includes the de Sitter / CLPW aside — the same crossed-product machine on a compact horizon, giving type II$_1$ — the contrast that closes the structural picture. Week 15 is final presentations and the instructor's outlook.

## 7. Problem set

**Core problems.**

**1. Map the four boundaries.** For each of AAJ's four limitations (order, perturbative, GJW-specific, partial bulk dictionary), state in 2–3 sentences what a concrete next step would look like and what tool it would need.

**2. A worse catalyst.** Repeat the §2.5 computation for the flat catalyst $|\nu_n\rangle = n^{-1/2}\sum_{j=1}^n |jj\rangle$, whose Schmidt spectrum is uniform. Show that tensoring with a Bell pair now produces a spectrum that is *not* close to $|\nu_{2n}\rangle$ for any $n$, and identify precisely which property of the harmonic spectrum the flat one lacks. Why does scale-invariance, rather than large rank, make a catalyst work?

**3. Other deformations.** The GJW deformation is a double-trace $\mathcal{O}_L\mathcal{O}_R$. Sketch what changes if the deformation is by a conserved current $J_L J_R$: which Ward identities constrain the corrections, and would you expect more or fewer than 20 terms at $O(g^2)$?

**Starred problems.**

**4\*. Higher-order counting.** Estimate the number of distinct corrections at $O(g^3)$ in the AAJ scheme by extending the §3.1 (Wk 12) combinatorics of cocycle × log × trace-pairing. Is there a pattern suggesting a generating function?

**5\*. Non-perturbative criterion.** Propose an algebraic diagnostic for "the wormhole has become non-perturbatively traversable" in terms of the commutant relation $\mathcal{A}_R' = \mathcal{A}_L$ (algebraic ER=EPR, Sem II Wk 10). What would its breakdown look like?

**Project problems.**

**6. Final-topic presentation.** Prepare and deliver a 10-minute talk on your final-write-up topic, positioned against the open-question landscape of §2. Incorporate group feedback into your final paper (due Wk 14).

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 4. Last revised 2026-08-23.*
