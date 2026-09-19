---
title: "Sem II Week 15 — Final Presentations and Outlook (Course Capstone)"
type: lecture-notes
course: syllabus
semester: 2
week: 15
block: 5
duration: 4 hours (student presentations + closing lecture)
prerequisites: the entire course
target_paper: "(synthesis week — no new target paper)"
modified: 2026-08-23
---

# Sem II Week 15 — Final Presentations and Outlook (Course Capstone)

> *The last week. Students present their final write-ups; the instructor gives a closing synthesis. This note is the capstone: it records the structure of the final assessment, synthesizes the whole two-semester arc into one picture, lays out the open-question landscape and possible thesis topics, and connects the course back to the group's live research program. There is no new physics here — the value is in seeing the whole machine at once and knowing where to go next.*

## 0. Reading

**Primary:** none new — students consolidate the full course.

**For the closing synthesis, revisit:**
- Sem I Wks 13–15 (the crossed product, dressed entropy, TFD bridge — the structural hinge of the course).
- Sem II Wk 10 (Liu's organizing diagram — the map of the whole field).

**Pointers for continuing:**
- The group's [[bell-inequalities-qft|Bell-CHSH]], [[relative-entropy-qft|relative entropy]], and [[entanglement-embezzlement|embezzlement]] programs.
- The wiki open questions: [[bell-chsh-in-holographic-setting]], [[embezzlement-cost-relative-entropy]], [[relative-entropy-interacting-theories]].

## 1. Final presentations

### 1.1 Format

- Each student gives a **20-minute talk** on their final write-up topic.
- **5 minutes** of Q&A from the group.
- Final write-up due (**15+ pages**).

### 1.2 Suggested talk structure

1. **Background (5 min):** what is the topic, why does it matter, what is the state of the art?
2. **Technical content (10 min):** the main calculation or argument — typically the student's piece of Mini-Calc 4 (Sem II Wk 12) extended, or a critical exposition with one worked check.
3. **Outlook (5 min):** what is still open, what would the next paper look like?

### 1.3 The four topic families (recap)

From Block 2 §7, refined through Blocks 3–5:

1. **Free-field cocycle perturbation** — extend Mini-Calc 4 (Sem II Wk 12); the most self-contained, building directly on the course's central calculation.
2. **Bell-CHSH in holographic settings** — the wiki open question [[bell-chsh-in-holographic-setting]]; connect Summers–Werner (Sem I Wk 11) to large-$N$ boundary algebras (Sem II Wk 1).
3. **Embezzlement on the crossed product** — the group's program; the cocycle as the shared tool of AAJ perturbation theory and type-III$_1$ embezzlement (Sem II Wk 13 §2.5).
4. **Critical exposition** — of CPW, AAJ, or CLPW (de Sitter), with one explicit calculation reproduced.

## 2. The closing synthesis: the whole course in one picture

The instructor's closing lecture assembles the two semesters into a single arc.

### 2.1 The spine

$$
\underbrace{\text{C*-algebras} \to \text{vN algebras} \to \text{type I/II/III}}_{\text{Block A}}
\to \underbrace{\text{Tomita–Takesaki} \to \text{modular flow} \to \text{Connes cocycle}}_{\text{Block B}}
$$
$$
\to \underbrace{\text{free QFT} \to \text{Bisognano–Wichmann} \to \text{type III}_1}_{\text{Block C}}
\to \underbrace{\text{crossed product} \to \text{dressed entropy} \to \text{TFD}}_{\text{Block D}}
$$
$$
\to \underbrace{\text{Witten} \to \text{CPW} \to \text{Liu} \to \text{AAJ} \to \text{MSY}}_{\text{Semester II}}.
$$

### 2.2 The one-sentence summary

> **The local algebras of quantum field theory are type III$_1$; this is why they have no entropy of their own, and why gravity — by gauging their modular flow through a crossed product — manufactures the entropy we call the generalized entropy $A/4G_N + S_{\rm out}$.**

Everything in Semester II is this sentence applied to a specific geometry, state, or perturbation (Liu's organizing diagram, Sem II Wk 10 §4).

> **Physical picture: the arc as a single idea.** Semester I built one fact — that a region of a continuum QFT has a type III$_1$ algebra, with all the strange consequences (no trace, no density matrix, no von Neumann entropy, modular flow as intrinsic thermal time). Semester II turned that fact from a curiosity into a tool: the type III$_1$ structure is *precisely* what makes the crossed-product dressing nontrivial, and the dressing is *precisely* how semiclassical gravity supplies the entropy the matter algebra lacks. The whole course is the claim that the operator-algebraic type of a local region and the gravitational entropy of a horizon are two views of the same structure — and that modular theory is the bridge. A student who leaves with this single picture, and the ability to run the free-field analog of any step, has the course.*

### 2.3 What the free-field analog gave us

A methodological thread worth naming explicitly: **every holographic step had a free-field Rindler analog** where the calculation was fully explicit.

| Holographic (Sem II) | Free-field analog | Where |
|---|---|---|
| boundary algebra type III$_1$ at large $N$ | wedge algebra type III$_1$ | Wk 1 / Sem I Wk 12 |
| modular flow = ADM time | modular flow = boost (Bisognano–Wichmann) | Wks 1, 5 / Sem I Wk 10 |
| crossed product, dressed entropy | Rindler crossed product, explicit trace | Wks 2–3, 6–7 / Sem I Wks 13–14 |
| Bell-CHSH / ER=EPR | Summers–Werner saturation, Minkowski-as-TFD | Wk 8 / Sem I Wks 11, 15 |
| GJW cocycle corrections | boost-evolved Weyl bilinear, Mini-Calc 4 | Wks 11–12 |

The analog is the course's pedagogical engine: it makes every abstract holographic claim checkable in a theory where everything is computable, with the holography-specific physics carefully flagged as input (the honest-scoping thread, Sem II Wks 7, 12, 14).

### 2.4 The course's results in one table

The closing lecture's most useful single artifact. Every load-bearing result of the two semesters, with **what the course actually established about it** — because a student's next job is to write a paper, and knowing which results they own outright and which they are quoting is the difference between a careful manuscript and a sloppy one.

| Result | Where | Status in this course |
|---|---|---|
| Gelfand–Naimark (commutative and general) | I.1 | Stated only |
| von Neumann bicommutant | I.2 | Proved in finite dimensions; general case sketched via Kaplansky |
| Murray–von Neumann comparison; type I/II/III trichotomy | I.3 | Sketched; type III examples stated |
| Trace exists on II$_1$, fails on III | I.3, I.4 | Stated only |
| KMS ⇔ Gibbs in finite dimensions | I.4 | Proved |
| Powers factors $R_\lambda$ are type III$_\lambda$ | I.4 | Stated; recomputed as a model proof in II.9 §2.3 |
| Tomita–Takesaki ($\Delta^{it}\mathcal{M}\Delta^{-it} = \mathcal{M}$, $J\mathcal{M}J = \mathcal{M}'$) | I.5 | Stated only; key lemmas proved |
| Modular flow is KMS at $\beta = 1$ | I.6 | Model proof (type I) |
| Connes cocycle; Radon–Nikodym theorem | I.7 | Stated only; state-independence of the flow proved from it |
| Araki–Uhlmann relative entropy, positivity and monotonicity | I.7 | Model proof (finite dim); general stated |
| Weyl relations; Slawny uniqueness | I.8 | Weyl relation proved; Slawny stated |
| Reeh–Schlieder | I.9 | Stated only |
| **Bisognano–Wichmann** ($\Delta_{W_R} = e^{-2\pi K}$) | I.10 | Stated from the axioms — **the course's one imported modular computation**, and the source of every closed form that follows |
| Tsirelson bound $2\sqrt2$ | I.11 | Proved |
| Summers–Werner (maximal violation between wedges) | I.11 | Stated, hypothesis-explicit |
| Local algebras are hyperfinite III$_1$ | I.12 | Stated, hypothesis-explicit (nuclearity, split property) |
| Crossed product: III $\rtimes\,\mathbb{R} \to$ II$_\infty$; trace exists | I.13 | Stated only (trace existence, Connes–Takesaki duality); construction carried out explicitly |
| Dressed-entropy difference $= -S(\omega\Vert \phi) + \mathcal{B}(\omega,\phi)$ | I.14 | Stated; model derivation in §4.4 |
| TFD is cyclic-separating; $J$ swaps the sides | I.15, II.5 | Proved (finite dim), II.10 §3.2 |
| Large-$N$ factorization of single-trace correlators | II.1 | Stated, hypothesis-explicit |
| Boundary single-trace algebra is III$_1$ at $N=\infty$ | II.1, II.9 | Stated for the holographic algebra; **mechanism proved** as an Araki–Woods computation (II.9 §2.3) |
| Witten / CPW crossed-product dressing; $S_{\rm gen}$ on $\hat{\mathcal{A}}$ | II.2–II.3, II.6–II.7 | Constructed; mini-calculations computed in the free-field analog |
| Bell-CHSH between the two TFD sides | II.8 | Computed in the free-field analog; approaches but does not attain $2\sqrt2$ |
| **Casini–Huerta–Myers** ball modular Hamiltonian | II.9 | **Proved** in $d=2$ from Bisognano–Wichmann plus the conformal map; general $d$ by the same argument |
| Modular flow $=$ bulk geometric flow (the dictionary) | II.9 | Stated, hypothesis-explicit (requires a Killing symmetry) |
| Crossed product makes the modular flow inner | II.10 | Proved |
| Semiclassical reduction $S_{\rm vN}\to A/4G_N + S_{\rm out} + \text{const}$ | II.10 | Stated; matched term by term with an explicit Gaussian clock |
| Algebraic ER=EPR ($J\mathcal{A}_RJ = \mathcal{A}_L = \mathcal{A}_R'$) | II.10 | Model proof (finite dim), with the failure mode exhibited |
| Cocycle perturbation series $u_t = \overline{\mathcal{T}}e^{\,i\int_0^t\sigma_s(V)ds}$ | II.11 | Model proof (finite dim); checked against unitarity at $O(V^2)$ |
| GJW deformation makes the wormhole traversable | II.11, II.14 | Stated |
| $\Delta S^{(1)} = \delta\langle K_0\rangle$ (first law of entanglement) | II.12 | Proved; vanishing for GJW proved from $JVJ = V$ |
| Second-order $\Delta S$, all three terms in closed form | II.12 | **Computed** (model case), verified three ways |
| Kubo–Mori metric governs $S(\omega_V\Vert \omega_0)$ at $O(V^2)$ | II.12 | Stated; checked against the model |
| AAJ's twenty $O(g^2)$ corrections | II.12–II.13 | Stated — the count is AAJ's, under their grouping conventions |
| Embezzlement fidelity $1 - O(1/\log n)$; exact in III$_1$ | II.13 | Mechanism computed ($\ln 2$ mismatch); bound stated |
| ANEC violation $\Rightarrow$ horizon shrinks $\Rightarrow$ throat opens | II.14 | **Proved** from linearized Raychaudhuri and the teleological condition |
| Shapiro advance magnitude $\Delta u \propto -g$ | II.14 | Stated (Dray–'t Hooft shockwave) |
| dS dressed algebra is II$_1$; vacuum is max-entropy | II.14 | **Computed** ($\hat\tau(1)$ finite on a half-line); max-entropy theorem proved |
| AAJ corrections $\leftrightarrow$ MSY bulk geometry | II.14 | **Open.** Conjectured, not established at any order |

The "status" column records the course's own proof-status labels, not the state of the literature: a row reading *Stated only* means the theorem is true and referenced, and that we did not prove it here. Several of the deepest results — Tomita–Takesaki, Bisognano–Wichmann, Connes–Takesaki — are in that column, and that is the correct pedagogical choice for a one-year course. What matters is knowing which is which.

Three things are worth saying out loud about this table.

First, **Bisognano–Wichmann is the course's single imported modular computation.** Every closed-form modular Hamiltonian we possess — the ball (CHM), the eternal black hole, the free-field analogs — is B–W moved by a symmetry. When a student writes "the modular Hamiltonian is," they should be able to say which symmetry carried it there from a wedge, and if they cannot, the formula is probably wrong.

Second, **the free-field analog is a laboratory, not a proof.** Every mini-calculation of Semester II was done in a Rindler free-field model where Bisognano–Wichmann supplies the modular data explicitly. Those calculations establish structure and catch errors; they do not establish holographic statements, and a manuscript that blurs the two will be caught.

Third, **the last row is the honest frontier.** The course computed the algebraic side (AAJ) and the bulk side (MSY) of the same traversal and did not match them. Nobody has. That is not a gap in the lectures; it is where the subject currently stops.

### 2.5 A self-test

A student who has absorbed the course should be able to do the following without notes. Anyone who cannot do most of them has a specific gap, and the pointer says where to go.

1. Explain why a local algebra in QFT has no density matrix, and what replaces the von Neumann entropy. *(I.12, I.7)*
2. State Tomita–Takesaki and say what cyclic-separating buys you. *(I.5)*
3. Derive the modular Hamiltonian of a ball in a CFT vacuum from Bisognano–Wichmann. *(II.9 §4)*
4. Explain what the crossed product adjoins, why it changes the type, and why gravity supplies it. *(I.13, II.10 §1)*
5. Write the dressed-entropy difference and say which term is the area and which is the matter. *(I.14, II.10 §2)*
6. Write the cocycle perturbation series and say why Dyson will not do. *(II.11 §2)*
7. Compute a second-order entropy correction in a two-level model. *(II.12 §2)*
8. Say why de Sitter gives II$_1$ and a black hole II$_\infty$ — in one sentence, about one integral. *(II.14 §4.3)*
9. Name one thing the algebra computes that the bulk does not, and one the reverse. *(II.14 §2)*
10. Name one open problem you could start on Monday. *(II.13 §2, §3.1 below)*

## 3. Outlook (instructor's one-page sketch)

### 3.1 Where the course leaves us

We now know:
- The local algebras of QFT are type III$_1$ (hypothesis-explicit).
- Modular theory gives them an intrinsic dynamics; the crossed product gives them an entropy.
- In holography, that entropy is the generalized entropy, and perturbing it (AAJ) describes traversable wormholes.

We do **not** know (the honest frontier):
- The rigorous match between AAJ's algebraic corrections and MSY's bulk geometry (Sem II Wk 14 §2.2).
- The non-perturbative / higher-order structure of the corrections (Sem II Wk 13 §2).
- Whether Bell-CHSH saturation extends cleanly to holographic boundary subregions ([[bell-chsh-in-holographic-setting]]).

### 3.2 Possible thesis topics

For a student continuing in the group:

1. **Free-field cocycle perturbation to higher order** — extend Mini-Calc 4; the most tractable, self-contained direction.
2. **Embezzlement cost on the crossed product** — connect cocycle perturbation theory to type-III$_1$ embezzlement protocols ([[entanglement-embezzlement]]); the group's [[embezzlement-cost-relative-entropy|embezzlement-cost question]].
3. **Bell-CHSH in holographic settings** — the [[bell-chsh-in-holographic-setting|wiki question]]; does Summers–Werner saturation probe bulk connectivity?
4. **Relative entropy in interacting theories** — push beyond free-field/Gaussian computations ([[relative-entropy-interacting-theories]]).

### 3.3 Connections to the group's program

The course was built to feed the group's existing research:

- **Bell-CHSH (De Fabritiis–Sorella–Roditi–Guimarães):** Sem I Wk 11 and Sem II Wk 8 are the course's home for this; the bumpified-Haar-wavelet observables are exactly the group's tool.
- **Embezzlement (group Ph.D. work):** Sem I Wk 12 (type III$_1$ makes it exact) and Sem II Wk 13 (cocycle as the shared tool).
- **Relative entropy (group program):** Sem I Wk 7 and throughout Sem II (the relative-entropy piece of every dressed-entropy difference).

> **Physical picture: why this course serves this group.** The group's research lives in the type III$_1$ regime — Bell-CHSH violations between wedges, exact embezzlement, relative entropy in QFT. These are not three separate topics; they are three windows onto the same algebraic structure, the one the course is about. A student who has done this course can read the group's papers, reproduce their free-field calculations, and see where each connects to the recent holographic literature. That is the course's purpose: not to make holographers, but to make researchers fluent in the modular/operator-algebraic toolkit that the group already uses and the recent literature has made central.

### 3.4 Collaborator referrals

For each open direction, the natural co-supervisors within and around the group (Sorella, Roditi, Dudal, Palhares, and collaborators) are listed in the [[courses/2026-algebraic-qft-course/syllabus]] and matched to topics in the closing lecture.

## 4. Assessment

**Final assessment (per the syllabus):**
- Weekly seminar presentations + participation: **40%**.
- Final write-up (15+ pages): **60%** (oral presentation included).
- Letter grade or pass/fail per UERJ convention.

## 5. What to take away (the course)

- **The central fact:** local QFT algebras are type III$_1$ (hypothesis-explicit: nuclearity + split property). No trace, no density matrix, no von Neumann entropy — but a canonical modular flow.
- **The central tool:** Tomita–Takesaki modular theory, and the Connes cocycle for comparing states. These are the type-III-native replacements for Hamiltonians and density matrices.
- **The central construction:** the modular crossed product, which gauges the modular flow (adds a gravitational clock) and promotes III$_1 \to$ II$_\infty$, manufacturing a trace and a (renormalized) entropy.
- **The central identification:** the dressed entropy equals the generalized entropy $A/4G_N + S_{\rm out}$ in holography (Witten, CPW); perturbing it describes traversable wormholes (AAJ); the bulk picture is MSY.
- **The structural punchline:** the algebra type reads off the geometry — II$_\infty$ for the eternal BH, II$_1$ for de Sitter (CLPW). The construction is universal; the type is geometric.
- **The method:** every holographic claim has a free-field Rindler analog where it is explicit, with holography-specific physics flagged as input. This honesty about what is proved, modeled, or assumed is the course's discipline.

## 6. End of the course

The two semesters took students from "no operator algebras" to "reading and critically engaging with the recent literature, with original calculation experience." Concretely, the course:

- Built operator-algebra and modular-theory fluency.
- Embedded students in the group's computational toolkit (Bell-CHSH, relative entropy, embezzlement).
- Provided real entry points to the recent literature (Witten, CPW, Liu, AAJ, MSY, CLPW).
- Created a permanent wiki resource — these 30 weeks of notes — for next year's students.

The natural continuations are a thesis project (§3.2), a follow-up reading course on a single paper in depth, or research in the group's adjacent programs. This is the natural end of the course.

## 7. Problem set

There is no problem set for Week 15. The deliverable is the **final write-up (15+ pages)** and its **20-minute presentation**.

**For students continuing:** pick one open question from §3.1–§3.2 and draft a one-page research proposal — the seed of a thesis. Bring it to the instructor for a continuation conversation.

**For everyone, before the talk:** work through the §2.5 self-test and note which items you cannot do. Each maps to a specific week; revisit that week rather than rereading the course. The most common gaps in past cohorts are items 3 (the conformal map behind CHM) and 8 (the trace integral behind II$_1$ vs II$_\infty$) — both are half a page, and both are the kind of thing a seminar audience asks about.

**For anyone writing this up:** before submitting, check every result your manuscript uses against the §2.4 table and make sure your prose claims no more than the course established. A sentence beginning "it is a theorem that" carries a different obligation from one beginning "in the free-field analog one computes", and referees notice.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 5. Last revised 2026-08-23.*

***End of the course.***
