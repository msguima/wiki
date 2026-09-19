---
title: What is the holographic dual of the entanglement embezzlement protocol?
type: question
status: partially-answered
areas:
  - bell-inequalities-qft
  - relative-entropy-qft
  - gauge-gravity-duality
priority: high
originated: 2026-05-26
modified: 2026-06-05
---

## Statement

Maldacena established that the [[thermofield-double|thermofield double (TFD) state]] of a holographic CFT is dual to a specific bulk geometry — the maximally extended eternal AdS-Schwarzschild black hole. The TFD is the canonical entangled state across two boundary copies, and its bulk dual is geometrically transparent. The question taken up here is the analog for the [[entanglement-embezzlement|entanglement embezzlement protocol]]:

1. **Q1 (Catalyst geometry).** What bulk geometry is dual to a catalyst (embezzling) state in a holographic CFT? Is there a single privileged geometry, as in TFD ↔ eternal black hole, or a family?
2. **Q2 (Protocol geometry).** What bulk operation implements the embezzlement unitary $U_A \otimes V_B$? Where does it live geometrically, and what bulk modes does it manipulate?
3. **Q3 (Cost).** At strict large $N$ the embezzlement is exact (zero cost). At $\mathcal{O}(1/N^2) \sim \mathcal{O}(G_N)$ corrections the [[crossed-product-construction|crossed product]] turns the [[type-iii-von-neumann-algebras|Type III₁]] boundary algebra into a Type II∞ algebra, where exact embezzlement is forbidden. What is the optimal embezzlement error rate as a function of $G_N$, and what is its geometric meaning?
4. **Q4 (Bell × embezzlement).** Maximal Bell-CHSH violation across the TFD has a clean bulk picture (the wormhole). Both Bell saturation and universal embezzlement arise from the same Type III₁ structure. Is there a parallel bulk picture for maximal embezzlement, and how does it differ geometrically from the Bell case?

The hypothesis being tested, in its corrected metric-aware form (see §Audit corrections below):

$$\delta_d^*(S_{\text{cap}}) \;\asymp\; \frac{\log d}{S_{\text{cap}}}, \qquad \kappa_d^*(S_{\text{cap}}) \;\asymp\; \sqrt{\frac{\log d}{S_{\text{cap}}}},$$

where $\delta_d = 1-F_d$ is the infidelity, $\kappa_d = \sqrt{1-F_d}$ is the Hilbert-space vector / trace-distance error, and $S_{\text{cap}}$ is the logarithmic reservoir capacity of the catalyst — identified in semiclassical holographic code subspaces with the generalized entropy $S_{\text{gen}} = \langle\widehat{\text{Area}}\rangle/(4G_N) + S_{\text{bulk}}$.

## Why It Matters

Two independent literatures have converged on the same algebraic object (Type III₁ factors in holographic CFTs) without anyone writing down the bridge:

- The [[entanglement-embezzlement|embezzlement-in-QFT]] program (van Luijk–Stottmeister–Werner–Wilming 2024) proved that every normal state on a Type III₁ factor is an embezzling state, but did not address holography.
- The [[crossed-product-construction|algebraic-holography]] program (Leutheusser–Liu 2021; Witten 2022; Chandrasekaran–Penington–Witten 2023; subsequent observer-dependence work) showed that gravitational corrections turn the boundary Type III₁ into a Type II∞ algebra whose trace gives generalized entropy, but did not address embezzlement.

Filling the bridge would yield:
1. A first explicit holographic protocol for entanglement embezzlement.
2. A quantitative cost formula via the crossed product — the natural follow-up to Witten/CPW that has not been written.
3. A new operational meaning for generalized entropy: it sets the operational catalyst capacity for holographic embezzlement.
4. A potential connection to [[bell-chsh-inequality|Bell-CHSH]] saturation: both phenomena arise from Type III₁ continuous modular spectrum, suggesting a unified bulk picture (Q4).

This is being actively investigated within the group through Ismael Porfirio and Erick Landim's PhD work on embezzlement in Type III₁ algebras.

## Project status (2026-06)

This page is the meta-document for the project. A full manuscript now exists.

- **Working title:** *Generalized Entropy as the Capacity for Holographic Entanglement Embezzlement* (M. S. Guimarães, sole author; CNPq).
- **Canonical draft (LaTeX, v7):** `/Users/marcelo/Documents/GPT Codex/Projects/holographic-embezzlement/2026-05-26-crossed-product-embezzlement-cost-standalone-v7.tex` (compiles clean, ~14 pp; target venue JHEP). Earlier versions v3–v6 and an audit note live in the same folder.
- **What is settled:** Q1 (no unique dual geometry — the catalyst is a broad area/modular-clock wavepacket dressing an ordinary entanglement wedge, not a new spacetime) and Q2 (the protocol is a clock-sector translation, realized near a horizon/RT surface by soft modes) are answered in the paper. Q3 has a **conditional achievability theorem**: in a finite sector of the crossed product of logarithmic trace volume $\mathcal C$ with a left–right mirror realization, a $d$-dimensional maximally entangled target is extracted with $1-F_d \le C_d \log d/\mathcal C$; under $\mathcal C \simeq S_{\text{gen}}$ in a semiclassical code subspace this gives $1-F_d \lesssim \log d/S_{\text{gen}} \sim 4G_N\log d/\langle\widehat{\text{Area}}\rangle$.
- **The one substantive gap (the live working question):** the **matching lower bound** is conjectural. As stands the paper proves a *bound* ("$S_{\text{gen}}$ suffices"), not a *capacity* ("$S_{\text{gen}}$ is necessary"). The title promises the latter. See [[embezzlement-capacity-lower-bound]] for the conjecture and the proof strategy. A second, smaller gap is deriving the mirror-window hypothesis (Assumption (c)) from bulk modular flow in an explicit example (TFD or CHM ball) rather than assuming it.
- **Single error measure:** the manuscript states all bounds as infidelity $1-F$; the vector/trace distance is the square root and is not tracked separately.

The remainder of this page records the original brainstorm, the literature scan, and the audit corrections that shaped the manuscript.

## Three converged lineages

### A. Embezzlement in QFT (PROVED, by van Luijk et al. 2024)

**Theorem.** Every normal state on a Type III₁ factor is an embezzling state. Conversely, embezzling states exist only in Type III factors. Connes' classification ($\lambda \in [0,1]$) has a quantitative operational interpretation via embezzling capacity.

**Implication for holography:** every cyclic-separating state on a Type III₁ subregion algebra of a holographic CFT is a catalyst.

**Holographic content of these papers:** none. The papers are pure AQFT / operator algebras. The only mention of gravity is a passing remark that "in the presence of gravity, local observable algebras may be of type II instead of type III" — with the implication that this would eliminate exact embezzlement.

### B. Algebraic holography and crossed products (STRONGLY SUPPORTED)

- **Leutheusser–Liu (2021).** At strict large $N$ in $\mathcal{N}=4$ SYM in the TFD state, the single-trace operator algebras organize into emergent [[type-iii-von-neumann-algebras|Type III₁ factors]] (one per boundary CFT).
- **Witten "Gravity and the Crossed Product" (2022).** The gravitational constraint converts the Type III₁ algebra into a Type II∞ [[crossed-product-construction|crossed product]]. Type II∞ has a trace → von Neumann entropy is well-defined → it equals the generalized entropy.
- **Chandrasekaran–Penington–Witten (2023).** Extension to single-sided black holes; observer-dependent entropy.
- **Soni (2024).** *Type-I approximation* of the crossed product — provides the technical regulator used in the achievability theorem of this project.
- **Recent observer-dependence work** (Witten 2023; De Vuyst–Eccles–Höhn–Kirklin 2025; covariant representations 2024).

**Embezzlement content of these papers:** none. They compute entropy, not embezzlement.

### C. The bridge between A and B (open, the project)

The pieces exist; the explicit holographic dictionary for the embezzlement protocol does not.

- Liu's 2025 lectures sketch the relationship between Araki-Uhlmann relative entropy on Type III₁ and the trace on Type II∞ crossed products, with embezzlement as a passing remark.
- The Oct 2025 review *Entanglement in von Neumann Algebraic Quantum Information Theory* ([arXiv:2510.07563](https://arxiv.org/abs/2510.07563)) confirms the absence: written from the AQFT side, no holographic discussion.
- Adjacent but different: *The Complexity of Entanglement Embezzlement* (Schwartzman, [arXiv:2410.19051](https://arxiv.org/abs/2410.19051), 2024) studies *circuit complexity* of embezzlement, not trace-norm cost in Type II∞ and not the holographic dictionary.

## Q1: Catalyst geometry

**Short answer.** There is *not* a single privileged geometry analogous to the TFD wormhole. The holographic catalyst is best understood as a **broad area/clock-sector wavepacket dressing** of a familiar entanglement-wedge state (TFD wormhole, Rindler wedge, ball-shaped CFT domain), not as a new classical spacetime.

**The TFD-↔-wormhole correspondence is *one-state-to-one-geometry*:** the TFD has a unique structure (modular Hamiltonian $= \beta H$; bipartite by construction), dual to a unique geometry.

**Catalyst is *one-algebra-to-many-states*:** van Luijk et al. show that every normal state on a Type III₁ factor is embezzling. Once a bipartite algebra split is chosen — equivalently, once an entanglement-wedge decomposition of the bulk is chosen — *any* cyclic-separating state for that pair is a catalyst.

**Refined holographic picture:** the operational reservoir is the sector whose conjugate variable is modular time or area. At strict large $N$ this reservoir is effectively unbounded (the Type III₁ limit). At finite $G_N$ the crossed product gives it a trace and hence a finite operational capacity. The catalyst is a broad wavepacket in that sector; the underlying geometry remains the familiar entanglement-wedge geometry (TFD wormhole, etc.), not a new classical solution.

**Privileged catalysts (where the protocol is geometrically transparent):**

| Catalyst | Modular flow | Geometric setup |
|---|---|---|
| TFD on eternal AdS-Schwarzschild | Killing time across the wormhole | Two boundaries, built-in bipartite structure; full Leutheusser–Liu/Witten/CPW machinery applies directly |
| Vacuum on a Rindler wedge | Boost generator (Bisognano–Wichmann) | Wedge complementarity; modular Hamiltonian linear in $T_{00}$ |
| Vacuum on a causal diamond in CFT | Casini–Huerta–Myers diamond Hamiltonian | Explicit modular Hamiltonian $K = 2\pi \int_{B_R} \tfrac{r^2-\lvert\mathbf{x}\rvert^2}{2r} T_{tt}\,d^{d-1}x$ |

**Recommended framing for the paper.** Do *not* try to dualize "the" catalyst. Instead, frame the eternal AdS-Schwarzschild as the privileged catalyst geometry and write the embezzlement protocol explicitly there as a clock-sector translation. The universal-catalyst result of van Luijk et al. enters as: "the protocol succeeds because the algebra is Type III₁ — but it is realized *geometrically* only here."

## Q2: Bulk operation implementing the embezzlement unitary

**Short answer.** The bulk image of the embezzlement unitary is a clock/area-sector translation acting in the entanglement wedge of Alice's subregion. Its geometric concentration near the RT/HRT surface (the "soft-mode shell" picture) is a *diagnostic* of where the action localizes, but the protocol itself is *non-Gaussian* — pure Weyl/coherent displacements do not suffice.

**The boundary protocol, recalled.** Alice's algebra is $\mathcal{M}$ (Type III₁), Bob's is $\mathcal{M}'$, the catalyst $|\Omega\rangle$ is cyclic-separating, and the auxiliary system $A'B'$ is finite-dimensional. The protocol is $U_A \otimes V_B$ with $U_A \in \mathcal{M} \otimes B(\mathcal{H}_{A'})$ and $V_B \in \mathcal{M}' \otimes B(\mathcal{H}_{B'})$ such that

$$U_A \otimes V_B \;\big(|\Omega\rangle \otimes |00\rangle_{A'B'}\big) \;\approx\; |\Omega\rangle \otimes |\phi\rangle_{A'B'}.$$

The mechanism: the modular Hamiltonian $K = -\log\Delta$ on a Type III₁ algebra has continuous spectrum reaching zero, supplying operators with arbitrarily low modular weight.

**Bulk dictionary, via JLMS.**

$$K_A^{\text{CFT}} \;=\; \frac{\widehat{\text{Area}}}{4 G_N} \;+\; K_A^{\text{bulk}}.$$

The locus of soft modular modes on the boundary corresponds to the **near-RT-surface shell** in the bulk, where the boost-like bulk modular Hamiltonian vanishes.

**JLMS consistency check.** "Catalyst undisturbed to $\epsilon$" means $S(\rho_A\|\rho_A')$ is $O(\epsilon)$, which by JLMS turns into two simultaneous conditions: the RT surface barely moves ($\delta\langle\widehat{\text{Area}}\rangle/(4G_N) = O(\epsilon)$) and the bulk modular Hamiltonian expectation barely shifts.

**Hierarchy of bulk constructions (audit correction).** Three levels:

1. **Pure Weyl / coherent displacements** — useful for diagnostics, but Gaussian symplectic invariants prevent universal embezzlement. The covariance matrix of a Gaussian state sharply constrains what local Gaussian operations can do.
2. **Squeezed modular/edge modes** — give a geometric Schmidt spectrum over a limited window. Approximate embezzlement is possible for targets fitting inside the window; the relevant scaling is the *width* of the usable log-spectrum, not "Gaussianity."
3. **Crossed-product clock/area reservoir** — the primary holographic construction. Translation in the modular clock coordinate is the non-Gaussian operation that implements universal embezzlement. Its capacity is measured by generalized entropy.

The primary object is not Gaussianity; it is **approximate translation invariance in the logarithmic Schmidt / modular-clock coordinate**.

**Reconciliation with the soft-mode picture.** Both views are consistent:

- *Algebraically*, the catalyst is a broad clock-sector wavepacket; the protocol translates this wavepacket along the modular flow.
- *Geometrically* in the bulk, the modular flow near a horizon/RT surface is a boost, and the wavepacket translation is concentrated on soft (low boost-energy) modes — the "shell at RT" picture.

The geometric near-RT description is therefore correct as far as it goes, but it must be implemented through a clock-sector translation, not a Gaussian displacement.

**Where the bulk operation lives, geometrically.**

| Catalyst | Bulk locus of $\hat U_A$ | Soft modes |
|---|---|---|
| TFD on eternal BH | Near-bifurcation-surface clock translation on Alice's side | Long-wavelength horizon modes (soft-hair-type) |
| Vacuum on a Rindler wedge | Near-Rindler-horizon boost translation | Modes with vanishing boost weight |
| Vacuum on a ball in any dimension | Near-RT-surface CHM-flow translation | Modes vanishing on the entangling surface |

**Connection to existing bulk physics.** The shell of soft modes near the RT surface is the locus of the [edge modes / Donnelly–Wall] entanglement contribution; the same place where soft hair carries an infinite reservoir of low-energy excitations. The embezzlement protocol is, geometrically, *the operational use of this reservoir for entanglement transfer.* The crossed product makes this finite, with capacity $\sim S_{\text{gen}}$.

## Q3: The cost — the actual paper

### Audit corrections (vs. the original plan)

A 2026-05-26 audit (`/Users/marcelo/Documents/Antigravity/.../2026-05-26-corrected-holographic-embezzlement-theorem-note.md`) identified three corrections to the original plan that are now incorporated below:

1. **Metric distinction.** Original plan wrote $\kappa_d^*(S) \asymp \log d/S$ for $\kappa$ a vector norm. Correct: infidelity $\delta = 1-F$ scales linearly, vector / trace-distance error $\kappa = \sqrt{1-F}$ scales as the square root. Pinsker + $\kappa^2 = 2(1-\sqrt F)$ enforces this.
2. **Capacity vs. von Neumann entropy.** The relevant invariant is the logarithmic reservoir capacity $S_{\text{cap}} = \log N_{\text{eff}}$, *not* the bare von Neumann entropy. For the vDH catalyst, $S(\mu_N) = \tfrac{1}{2}\log N + O(\log\log N)$ — half the reservoir width $\log N$. The identification $S_{\text{cap}} \simeq S_{\text{gen}}$ in semiclassical holographic sectors is a separate physical claim, not automatic.
3. **Clock-measure factor.** The crossed-product catalyst should be flat in the natural clock coordinate $s$, not $\propto e^{-s/2}$. Under $s = \log n$, the vDH coefficient $n^{-1/2}$ combined with the Jacobian $dn/ds = e^s$ gives flat amplitude in $s$.

### Literature check — verdict

A focused check confirms the gap is genuine.

- **Finite-dim (Type I):** vDH 2002 ($\epsilon \sim \log d/\log n$); Leung–Wang 2014; *Complete Characterization of Entanglement Embezzlement* (Quantum 2024). All finite-dim, nothing about gravity.
- **Type III₁:** van Luijk et al. 2024 — exact embezzlement.
- **Type II case — qualitatively dismissed, quantitatively open.** Van Luijk et al. state $\kappa_{\min}(\mathcal{M}) = \kappa_{\max}(\mathcal{M}) = 2$ for semifinite factors (worst possible value of their universal embezzlement quality parameter) and do not refine. They mention "in the presence of gravity, local observable algebras may be of type II" only in passing.
- **Crossed-product / Witten-CPW side:** computes entropy, not embezzlement.
- **Adjacent program:** Schwartzman 2024 — *circuit complexity* of embezzlement (different obstruction, not trace-norm cost; not holographic).

**Important subtlety: the $\kappa = 2$ result is not fatal.** "No *single* state on a Type II factor is a *universal* embezzler" is *not* the same as "no family approaches embezzlement parametrically." The vDH family $|\mu_n\rangle$ achieves embezzlement parametrically as $n \to \infty$; the limit is a Type III₁ state. In Type II∞, the analog is a family parameterized by $S_{\text{cap}}$ (equivalently $G_N$), and the rate $\delta_d \to 0$ as $S_{\text{cap}} \to \infty$ is what nobody has computed.

### Definitions and error metrics

For pure output and ideal vectors $|\Psi_{\text{out}}\rangle, |\Psi_{\text{id}}\rangle$:

$$F = |\langle\Psi_{\text{id}}|\Psi_{\text{out}}\rangle|^2, \quad \delta = 1-F, \quad \kappa = \inf_\theta \big\|e^{i\theta}|\Psi_{\text{out}}\rangle - |\Psi_{\text{id}}\rangle\big\|.$$

These satisfy $\kappa^2 = 2(1-\sqrt F) \leq 2(1-F) = 2\delta$, and for small $\delta$, $\kappa^2 = \delta + O(\delta^2)$. So $\delta$ and $\kappa^2$ scale the same way; the bare vector norm / trace distance $\kappa$ inherits a square root.

### Finite-dimensional benchmark (proved)

The van Dam–Hayden catalyst:

$$|\mu_N\rangle = \frac{1}{\sqrt{H_N}}\sum_{n=1}^N \frac{1}{\sqrt n}|n\rangle_A|n\rangle_B, \qquad H_N = \sum_{n=1}^N \frac{1}{n}.$$

For a $d$-dimensional maximally entangled target and $N = dM$, block-reindexing $n = d(m-1)+r+1 \mapsto (m,r)$ gives

$$\sqrt{F_{M,d}} = \frac{1}{\sqrt{dH_M H_{dM}}}\sum_{m=1}^M \frac{1}{\sqrt m}\sum_{r=0}^{d-1}\frac{1}{\sqrt{d(m-1)+r+1}}.$$

**Lemma (vDH scaling).** For fixed $d$ and $M \to \infty$,

$$1 - F_{M,d} \;\leq\; \frac{H_{dM} - H_M}{H_{dM}} \;=\; O\!\left(\frac{\log d}{\log M}\right).$$

**Proof sketch.** Using $d(m-1)+r+1 \leq dm$,

$$\sum_{r=0}^{d-1} \frac{1}{\sqrt{d(m-1)+r+1}} \geq \frac{d}{\sqrt{dm}} = \sqrt{d/m},$$

so $\sqrt{F_{M,d}} \geq \sqrt{H_M/H_{dM}}$, hence $F_{M,d} \geq H_M/H_{dM}$ and the bound follows from $H_{dM} - H_M \leq \log d + O(1/M)$.

**Capacity vs entropy of the catalyst.** Direct computation:

$$S(\mu_N) = \log H_N + \frac{1}{H_N}\sum_{n=1}^N \frac{\log n}{n} = \frac{1}{2}\log N + \log\log N + O(1).$$

The reservoir width $\log N$ and the vN entropy $S(\mu_N)$ differ by a factor of $\tfrac{1}{2}$ at leading order — the operational invariant is the reservoir width, defined as $S_{\text{cap}} = \log N_{\text{eff}}$.

### Continuous (clock-coordinate) toy model

Under $s = \log n$, the vDH state has flat amplitude in $s$. The continuous analog is

$$|\Gamma_L\rangle = \frac{1}{\sqrt L}\int_0^L ds\;|s\rangle_A|s\rangle_B.$$

A modular translation by $\Delta$ on Alice's side gives overlap $(L-\Delta)/L$ (for $0 \leq \Delta \leq L$), so

$$1 - F = 1 - (1 - \Delta/L)^2 \leq 2\Delta/L.$$

For a $d$-dimensional extraction, $\Delta_d = \log d$, giving $1 - F = O(\log d/L)$ with $L$ playing the role of $S_{\text{cap}}$. This reproduces the vDH scaling in the cleanest form.

### Crossed-product setup

Let $\mathcal{M}$ be Type III₁ with modular automorphism $\sigma_t^\Omega$ relative to a cyclic-separating $|\Omega\rangle$. Form

$$\hat{\mathcal{M}} = \mathcal{M} \rtimes_{\sigma^\Omega} \mathbb{R}.$$

This is Type II∞ in the holographic setting; it contains the original algebra and a modular clock with coordinate $s$ conjugate to modular translations. The Type II∞ trace $\widehat{\text{Tr}}$ gives notions of trace volume; for a finite projection $P \in \hat{\mathcal{M}}$, define

$$S_{\text{cap}}(P) = \log \widehat{\text{Tr}}(P).$$

**Finite-capacity crossed-product window (definition).** A regulated window of capacity $S_{\text{cap}}$ is a finite projection $P \in \hat{\mathcal{M}}$ together with a type-I or hyperfinite matrix approximation inside $P\hat{\mathcal{M}}P$ of effective dimension $N_{\text{eff}}$ with $S_{\text{cap}} = \log N_{\text{eff}}$, including the corresponding mirror window in the commutant.

This is a model of the regulated holographic clock/area sector; the regulator hypotheses are eventually to be derived from the Witten/CPW crossed product in a specified code subspace (Soni 2024 provides the type-I approximation technology).

### Sharpened theorem (achievability, proved)

**Theorem (Achievability in a finite-capacity regulator).** *Assume a crossed-product regulator contains a finite window with effective reservoir dimension $N_{\text{eff}} = dM$ and capacity $S_{\text{cap}} = \log M$ up to $O_d(1)$ additive terms. Then for a fixed $d$-dimensional maximally entangled target, there exist a normal catalyst state $\hat\omega_{S_{\text{cap}}}$ and local unitaries*

$$U_A \in \hat{\mathcal{M}} \otimes B(\mathbb{C}^d), \qquad V_B \in \hat{\mathcal{M}}' \otimes B(\mathbb{C}^d),$$

*such that the output fidelity obeys*

$$1 - F_d \leq C_d \frac{\log d}{S_{\text{cap}}}, \qquad \text{equivalently} \qquad \kappa_d \leq C'_d \sqrt{\frac{\log d}{S_{\text{cap}}}}.$$

**Proof.** Choose inside the finite window the type-I approximant of $|\mu_{dM}\rangle$. The block-reindexing permutation is implemented by local unitaries in $\hat{\mathcal{M}} \otimes B(\mathbb{C}^d)$ and $\hat{\mathcal{M}}' \otimes B(\mathbb{C}^d)$ because the regulator includes the mirror window. The finite-dimensional vDH calculation applies verbatim. ∎

**Holographic interpretation.** Identify $S_{\text{cap}} \simeq S_{\text{gen}}$ in a semiclassical code subspace. Then

$$1 - F_d \lesssim \frac{\log d}{S_{\text{gen}}} \sim \frac{4 G_N \log d}{\langle\widehat{\text{Area}}\rangle},$$

a Bekenstein-style **operational capacity** statement: extracting a $d$-dimensional Bell pair consumes a fraction $\log d/S_{\text{gen}}$ of the available area/edge/clock reservoir. *This is not a classical shockwave statement* — it should be phrased as operational capacity, not literal area fluctuation, unless a separate stress-tensor / backreaction calculation is supplied.

### Why this does not contradict the Type II no-go

The theorem constructs a *family* of finite-capacity states. For each finite $S_{\text{cap}}$, the state is not a universal embezzler for all $d$ and all accuracies. The van Luijk et al. theorem rules out a *single* universal embezzling state on a semifinite factor; it does not rule out a family whose performance improves as the trace window approaches the Type III₁ limit.

### Conjectural lower bound (the real research challenge)

**Conjecture (Holographic embezzlement cost).** *In a semiclassical crossed-product code subspace of capacity $S_{\text{cap}}$, any protocol extracting a worst-case $d$-dimensional maximally entangled target while returning the catalyst with fidelity $F_d$ obeys*

$$1 - F_d \geq c_d \frac{\log d}{S_{\text{cap}}}, \qquad \kappa_d \geq c'_d \sqrt{\frac{\log d}{S_{\text{cap}}}}$$

*for sufficiently large $S_{\text{cap}}$ and fixed $d$.*

**Proof strategy (the open work).** A direct Pinsker / data-processing argument is probably insufficient; Pinsker converts relative entropy to trace distance but does not capture the effective width of a catalyst spectrum under $d$-fold reshuffling. A plausible route:

1. Formulate the finite trace window using **smooth max entropy** or **smooth support trace** (one-shot QI machinery).
2. Show that producing a rank-$d$ maximally entangled target requires a $d$-fold approximate self-similarity of the catalyst spectrum.
3. Prove that a finite window of logarithmic width $S_{\text{cap}}$ cannot be $d$-self-similar with infidelity smaller than order $\log d/S_{\text{cap}}$.
4. Pass from finite type-I regulators to the hyperfinite Type II∞ window by approximation (Soni 2024).

This is the spirit of finite-dimensional universality results (Leung–Wang 2014) but the Type II trace-window formulation has not been isolated in the holographic literature.

### What's standard, what's new

| Step | Existing technology | New work |
|---|---|---|
| Crossed product setup | Takesaki; Witten 2022; CPW 2023; Soni 2024 | — |
| Modular spectrum / soft modes | Araki; Connes; Haag | — |
| vDH-type protocol | vDH 2002; Leung–Wang 2014 | Lift to Type II∞ via type-I approximation (essentially done) |
| Pinsker / data processing | Petz; Hiai | — |
| One-shot / smooth max entropy bounds | Renner; Tomamichel | **Application to Type II trace windows (Part B, conjectural)** |
| Holographic dictionary | JLMS; FLM; CPW | **Code-subspace identification $S_{\text{cap}} \simeq S_{\text{gen}}$ (Part C)** |
| Embezzlement-in-Type-II rate | Not in literature | **The whole conjecture** |

The achievability theorem is **proved**. The lower bound and the precise holographic dictionary identification are the open research challenges.

### Honest hedges

1. **Holographic dictionary $S_{\text{cap}} \simeq S_{\text{gen}}$.** Working identification, not a theorem. Needs to be derived in a specified code subspace; the bare vN entropy of every normal state on the Type II algebra is not automatically the operational capacity.
2. **Bekenstein-style reading.** Operational, not classical-shockwave. The Bell-pair extraction consumes a fraction of the reservoir, not a literal $4 G_N \log d$ horizon area fluctuation, unless backreaction is computed separately.
3. **Lower bound is conjectural.** Marked clearly as such until the one-shot entropy argument is actually written.

## Q4: Bell × embezzlement (preview, distinctive angle)

Both Bell-CHSH saturation and universal embezzlement are consequences of the same Type III₁ structure. In a holographic CFT, max Bell violation across the TFD has a clean bulk picture (the wormhole). Is there a parallel bulk picture for max embezzlement, and how do the two phenomena differ geometrically?

**Why this angle is favorable for the group.** The [[bell-inequalities-qft|Bell-CHSH program]] has built a sophisticated Weyl-operator toolkit in the group (papers with Sorella, Roditi, Vieira, Caribé, Dudal, De Fabritiis, Peruzzo, Guedes). The algebraic-holography insiders (Witten/Liu/CPW) are not in this idiom and would be slower to write this angle. The "Bell × embezzlement" framing is harder to scoop for that reason.

**Concrete subquestions.**

- Both phenomena saturate maximally because of continuous modular spectrum. Do they saturate *simultaneously* for the same family of states, or are there trade-offs?
- Holographically, max Bell violation lives in the *correlation* between the two boundary algebras; max embezzlement lives in the *internal* clock/area sector of one algebra (via auxiliary qubits). What is the bulk geometric distinction?
- Is there a unified bound combining Bell violation and embezzlement cost, both controlled by modular flow / generalized entropy / $S_{\text{cap}}$?

This is naturally the follow-up paper after Q3, exploiting the group's distinctive expertise.

## Concrete next steps

The achievability theorem is now essentially proved. The remaining work, in order:

1. **Hand the achievability theorem to a student now** (Porfirio or Landim). The Section-5-style write-up in the .tex draft is a clean publishable lemma even before the lower bound is settled. ~1 month to verify and polish.
2. **Lower bound proof** — the main research challenge. Smooth max entropy / one-shot machinery for trace windows. ~2–3 months of focused work.
3. **Holographic dictionary** — derive $S_{\text{cap}} \simeq S_{\text{gen}}$ explicitly in TFD and CHM ball code subspaces. Apply Witten/CPW/Soni technology.
4. **Explicit TFD example** — implement clock translation as near-horizon modular boost; verify that the protocol's bulk image is a soft-mode operation on Alice's side of the bifurcation surface (reconciles with Q2).
5. **Gaussian no-go diagnostic** — formulate the precise statement that pure Weyl/coherent constructions cannot embezzle universally, identifying which non-Gaussian ingredient evades it.

## Risks and timing

**Competing camps:**
- van Luijk / Wilming / Stottmeister (embezzlement-in-QFT camp). Could refine the Type II part of their dichotomy at any time.
- Witten / Liu / CPW (algebraic-holography camp). Could write the operational follow-up at any time.
- Schwartzman (complexity-of-embezzlement, 2410.19051). Closest competing program; could pivot to the holographic / trace-norm framing.

**Estimated writing window:** 6–12 months. Plenty of time for a careful paper, not for an indefinite study.

**Risk-mitigation:**
1. The achievability theorem is essentially done — write it up cleanly as Part 1 of the paper now.
2. The lower bound is the natural Part 2; can be developed in parallel.
3. Move on Q4 (Bell × embezzlement) after Q3 is on arXiv; that's the group's distinctive follow-up.

## Annotated bibliography

### Foundational — embezzlement and Type III

[1] L. van Luijk, A. Stottmeister, R. F. Werner, H. Wilming, *Embezzlement of entanglement, quantum fields, and the classification of von Neumann algebras*, [arXiv:2401.07299](https://arxiv.org/abs/2401.07299) (2024).
   - Role: Mathematical core. Connes' classification ↔ embezzling capacity. $\kappa = 2$ in semifinite factors; brief mention of gravity → Type II implication.

[2] L. van Luijk, A. Stottmeister, R. F. Werner, H. Wilming, *Relativistic Quantum Fields Are Universal Entanglement Embezzlers*, [arXiv:2401.07292](https://arxiv.org/abs/2401.07292), Phys. Rev. Lett. 133, 261602 (2024).

[3] L. van Luijk, A. Stottmeister, H. Wilming, *Multipartite Embezzlement of Entanglement*, [arXiv:2409.07646](https://arxiv.org/abs/2409.07646), Quantum 9, 1818 (2025).

[4] W. van Dam, P. Hayden, *Embezzling Entangled Quantum States*, [arXiv:quant-ph/0201041](https://arxiv.org/abs/quant-ph/0201041), Phys. Rev. A 67, 060302 (2003).

[5] D. Leung, B. Wang, *Characteristics of Universal Embezzling Families*, [arXiv:1311.6842](https://arxiv.org/abs/1311.6842), Phys. Rev. A 90, 042331 (2014).

[6] *Complete Characterization of Entanglement Embezzlement*, Quantum 8, 1368 (2024).

### Foundational — algebraic holography and crossed products

[7] J. M. Maldacena, *Eternal black holes in anti-de Sitter*, [arXiv:hep-th/0106112](https://arxiv.org/abs/hep-th/0106112), JHEP 04, 021 (2003).

[8] S. Leutheusser, H. Liu, *Emergent times in holographic duality*, [arXiv:2112.12156](https://arxiv.org/abs/2112.12156), Phys. Rev. D 108, 086020 (2023).

[9] E. Witten, *Gravity and the Crossed Product*, [arXiv:2112.12828](https://arxiv.org/abs/2112.12828), JHEP 10 (2022) 008.

[10] V. Chandrasekaran, G. Penington, E. Witten, *Large $N$ algebras and generalized entropy*, [arXiv:2209.10454](https://arxiv.org/abs/2209.10454), JHEP 04 (2023) 009.

[11] R. M. Soni, *A type I approximation of the crossed product*, [arXiv:2307.12481](https://arxiv.org/abs/2307.12481), JHEP 01 (2024) 123.
   - Role: **The technical regulator backbone of the achievability theorem.**

[12] E. Witten, *A Background-Independent Algebra in Quantum Gravity*, [arXiv:2308.03663](https://arxiv.org/abs/2308.03663), JHEP 03 (2024) 077.

[13] D. L. Jafferis, A. Lewkowycz, J. Maldacena, S. J. Suh, *Relative entropy equals bulk relative entropy* (JLMS), [arXiv:1512.06431](https://arxiv.org/abs/1512.06431), JHEP 06 (2016) 004.

[14] X. Dong, D. Harlow, D. Marolf, *Flat entanglement spectra in fixed-area states of quantum gravity*, [arXiv:1811.05382](https://arxiv.org/abs/1811.05382), JHEP 10 (2019) 240.
   - Role: Fixed-area states. Useful comparison: fixed-area is a flat *single* sector; embezzlement requires a broad *slowly-varying* reservoir across nearby sectors.

[15] J. De Vuyst, S. Eccles, P. Höhn, J. Kirklin, *Crossed products and quantum reference frames*, [arXiv:2412.15502](https://arxiv.org/abs/2412.15502), JHEP 07 (2025) 063.

### Review / overview

[16] H. Liu, *Lectures on entanglement, von Neumann algebras, and emergence of spacetime*, [arXiv:2510.07017](https://arxiv.org/abs/2510.07017) (2025). In wiki as [[2025-liu-lectures-entanglement-vna]].

[17] *Entanglement in von Neumann Algebraic Quantum Information Theory*, [arXiv:2510.07563](https://arxiv.org/abs/2510.07563) (Oct 2025).

### Adjacent / competing program

[18] O. Schwartzman, *The Complexity of Entanglement Embezzlement*, [arXiv:2410.19051](https://arxiv.org/abs/2410.19051) (2024).
   - Role: Studies *circuit complexity* of embezzlement (different obstruction). Closest competing program.

## Related Questions

- [[embezzlement-cost-relative-entropy]] — Original group-internal question about cost of embezzlement via relative entropy. This page extends and sharpens it to the holographic / crossed-product setting.
- [[bell-chsh-in-holographic-setting]] — Bell-CHSH and relative entropy as probes of holographic spacetime; complementary angle to Q4 here.
- [[relative-entropy-interacting-theories]] — Applying relative entropy beyond free fields.
- [[entanglement-as-confinement-probe]] — Shared modular-theory toolkit.

## Notes

- **Conversation history.** Original brainstorm and plan: 2026-05-26 with claude-opus-4-7. Iterated Q1 → Q2 → Q3 → literature check → sharpened theorem → next step. Audit and LaTeX implementation in `/Users/marcelo/Documents/Antigravity/physics-wiki/draft/` correct three metric/capacity/clock-measure issues and elevate the upper bound from "proof skeleton" to a proved theorem.
- **Discuss with ismael-porfirio and erick-landim** before committing — handing them the achievability theorem write-up is the natural first step.
- **Decision point on talking to a principal** (Wilming, Hollands) should come after the lower bound is at least at proof-strategy maturity, not before.
