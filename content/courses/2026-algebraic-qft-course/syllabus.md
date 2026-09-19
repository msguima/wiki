---
title: Estrutura Algébrica da Teoria Quântica de Campos — Álgebras, Fluxo Modular e Aplicações
type: course
instructor: Marcelo S. Guimarães
institution: UERJ — Departamento de Física Teórica
duration: two semesters (~30 weeks)
audience: M.Sc. and Ph.D. students, open to qualified outsiders
prerequisites: Quantum mechanics; general relativity; basic quantum field theory (free fields, canonical quantization)
not assumed: von Neumann algebras, conformal field theory, AdS/CFT
language: lectures in Portuguese; written materials in English
modified: 2026-05-08
---

# Estrutura Algébrica da Teoria Quântica de Campos
**Álgebras, Fluxo Modular e Aplicações**

A two-semester graduate course on the algebraic structure of quantum field theory, from the foundations of operator algebras to the recent literature on crossed products, traversable wormholes, and gravitational entropy. Designed to take students with basic QFT (and no operator-algebra background) to the point where they can read and critically discuss the recent papers of Witten, Chandrasekaran–Penington–Witten, and Ahmad–Jefferson, with the Chandrasekaran–Longo–Penington–Witten de Sitter paper as a contrasting II$_1$ example.

---

## 1. Course architecture

| | Semester I — Fundamentos | Semester II — Literatura Recente |
|---|---|---|
| **Format** | Formal lectures | Reading seminar with student presentations |
| **Hours/week** | 4 hr lectures + problem sets | 2 hr seminar + 1 hr office consultation |
| **Mode** | Instructor-led | Student-led, instructor-guided |
| **Anchor** | Operator algebras → modular theory → free QFT → crossed products | Witten 2022 → CPW → Liu lectures → AAJ → MSY |

The two semesters are designed to be taken in sequence. Semester II assumes Semester I as a hard prerequisite. Students who already have an operator-algebra background may petition to enter directly into Semester II.

---

## 2. Learning outcomes

A graduate of the course can:

1. Use the language of C\*-algebras, von Neumann algebras, and the type classification (I, II, III) fluently.
2. State and apply the [[tomita-takesaki-modular-theory|Tomita–Takesaki theorem]]; compute the modular operator $\Delta$ and the modular conjugation $J$ for explicit examples.
3. Compute the modular operator for the [[rindler-wedges|Rindler wedge]] of a free scalar field using Bisognano–Wichmann, and derive the Unruh effect as a corollary.
4. Construct a [[crossed-product-construction|crossed product]] $\mathcal{M} \rtimes_\sigma \mathbb{R}$ explicitly and explain the type III₁ → II_∞ promotion.
5. Read [[2025-liu-lectures-entanglement-vna|Liu's lectures]], Witten's "Gravity and the crossed product," CPW, and AAJ; identify their key technical inputs and explain which steps are algebraic versus holographic.
6. Outline a research question in the area, in the form of a 15–20 page write-up.

---

## 3. Audience and prerequisites

**Assumed:** Quantum mechanics at graduate-introductory level; general relativity (basic Schwarzschild, Rindler coordinates, asymptotic regions); free quantum field theory (canonical quantization of the free scalar, Wightman functions, smeared fields).

**Not assumed:** Von Neumann algebras; functional analysis beyond Hilbert space basics; conformal field theory; AdS/CFT; Ryu–Takayanagi formula.

**Audience:** Mixed M.Sc. and Ph.D. students at UERJ. The course is open to qualified outsiders (collaborators at CBPF, [[silvio-paolo-sorella|Sorella's]] group, [[itzhak-roditi|Roditi's]] group, mathematical physicists at IME). All assessment carries a **core track** (everyone) and a **starred track** (Ph.D. students and the ambitious).

---

## 4. Materials

### Primary texts (Semester I)

- Bratteli & Robinson, *Operator Algebras and Quantum Statistical Mechanics*, Vols. I & II (selected chapters).
- Witten, "Notes on some entanglement properties of QFT," arXiv:1803.04993.
- [[2025-liu-lectures-entanglement-vna|Liu's lectures]], arXiv:2510.07017 (used as bridge to Semester II).

### Primary texts (Semester II)

- Witten, "Gravity and the crossed product," JHEP 10 (2022) 008 [arXiv:2112.12828].
- Chandrasekaran, Penington, Witten, "Large $N$ algebras and generalized entropy," arXiv:2209.10454. *(The two-sided eternal black hole; type III$_1 \to$ type II$_\infty$.)*
- Chandrasekaran, Longo, Penington, Witten, "An algebra of observables for de Sitter space," arXiv:2206.10780. *(Static patch with observer; type II$_1$. Used as contrasting example in Block 5 Wk 14, not as primary reading.)*
- Ahmad & Jefferson, "Algebraic perturbation theory: traversable wormholes and generalized entropy beyond subleading order," arXiv:2501.01487.
- Maldacena, Stanford, Yang, "Diving into traversable wormholes," arXiv:1704.05333.
- Gao, Jafferis, Wall, "Traversable wormholes via a double trace deformation," JHEP 12 (2017) 151 [arXiv:1608.05687].
- [[2025-liu-lectures-entanglement-vna|Liu's lectures]] (as connective tissue).

### Reference works

- Haag, *Local Quantum Physics*, 2nd ed., Springer, 1996.
- Takesaki, *Theory of Operator Algebras*, Vol. II, Springer, 2003.

### Lecture notes

All lecture notes will be hosted under `wiki/courses/2026-algebraic-qft-course/notes/`, committed weekly. Notes are public-by-default within the wiki and become a durable resource for future students and collaborators.

### Course appendices

Seven standing reference documents under `appendices/`. A–C are prerequisites-on-demand: consult them when a lecture assumes something you lack. D–G are working references used throughout.

- [[functional-analysis-survival-kit|Appendix A — Functional-Analysis Survival Kit]] — the operator theory Block A assumes: unbounded operators, closability, spectral theorem, topologies.
- [[free-field-and-rindler-primer|Appendix B — Free-Field and Rindler Primer]] — the free scalar, Wightman functions, and Rindler coordinates. Read before Block C.
- [[holography-large-n-primer|Appendix E — Holography and Large-$N$ Primer]] — the minimum AdS/CFT needed for Semester II, for students who have not taken the [[courses/2026-algebraic-qft-course/syllabus|AdS/CFT course]].
- [[modular-theory-reference-sheet|Appendix C — Modular Theory Reference Sheet]] — every modular-theory formula in one place, in this course's conventions.
- [[crossed-product-reference-sheet|Appendix D — Crossed-Product Reference Sheet]] — the crossed-product construction, its trace, and the type III → II$_\infty$ statement.
- [[notation-and-conventions|Appendix F — Notation and Conventions]] — the symbol table. Companion to [[courses/2026-algebraic-qft-course/conventions]], which fixes the KMS and modular sign conventions.
- Appendix G — Bibliography and Paper Map — per-paper reading instructions for both semesters.

---

## 5. Assessment

### Semester I

| Item | Weight |
|---|---|
| Weekly problem sets (core + starred tracks) | 60% |
| Midterm calculation (Week 8) | 20% |
| Take-home final | 20% |

### Semester II

| Item | Weight | Deadline |
|---|---|---|
| Weekly seminar presentation + participation | 40% | continuous |
| Final write-up draft (≥10 pp, feedback only) | 0% | end of Week 10 |
| Final write-up revision (≥15 pp) | 60% | end of Week 14 |
| Oral presentation of write-up | included in 60% | Week 15 |

Students propose a write-up topic by end of Week 4 of Semester II. Suggested topics:

1. **Free-field cocycle perturbation** — extend the Week 12 mini-calculation to a self-contained 15–20 page exposition with a controlled second-order calculation in a free-field analogue.
2. **Bell-CHSH in holographic settings** — addresses the open question [[bell-chsh-in-holographic-setting]].
3. **Embezzlement cost on the crossed product** — connects to the Ph.D. work of ismael-porfirio and erick-landim.
4. **Critical exposition of one paper** — a clean, mathematically careful exposition of CPW, CLPW (de Sitter), or AAJ for a non-specialist reader.

---

## 6. Semester I — Fundamentos (15 weeks)

### Block A: Operator algebra foundations (Weeks 1–4) — skeleton

**Week 1 — C\*-algebras, states, GNS construction.** ([[week-01-cstar-algebras-and-gns|notes]])
Banach algebras → C\*-algebras → states (positive normalized linear functionals) → GNS construction. Examples: $\mathcal{B}(\mathcal{H})$, $C(X)$, $M_n(\mathbb{C})$. *Problem set:* prove GNS for finite-dimensional examples; verify the cyclic-vector property.

**Week 2 — Von Neumann algebras and the double commutant.** ([[week-02-von-neumann-algebras|notes]])
Strong/weak operator topologies → von Neumann's bicommutant theorem → factors → projections lattice. *Starred:* Murray–von Neumann equivalence of projections.

**Week 3 — Type classification (I, II, III) with examples.** ([[week-03-type-classification|notes]])
Type I (matrix algebras, $\mathcal{B}(\mathcal{H})$), Type II_1 (hyperfinite II_1, group von Neumann algebras), Type III (statement of Connes' classification III_λ for $\lambda \in [0,1]$). [[type-iii-von-neumann-algebras|Type III₁]] flagged as the type for QFT — to be derived in Block C. *Problem set:* compute the trace on a type II_1 factor for finite examples; show $\mathcal{B}(\mathcal{H})$ is type I_∞.

**Week 4 — KMS states and the modular interpretation.** ([[week-04-kms-states-and-type-III|notes]])
KMS condition as algebraic thermal equilibrium → Gibbs states satisfy KMS in finite dimensions → KMS extends thermal physics to type III. [[tomita-takesaki-modular-theory|Tomita–Takesaki]] preview: the modular automorphism group is the KMS flow. *Problem set:* verify KMS for Gibbs states on $\mathcal{B}(\mathbb{C}^n)$.

### Block B: Tomita–Takesaki theory (Weeks 5–7) — skeleton

**Week 5 — The setup: cyclic and separating vectors.** ([[week-05-tomita-operator|notes]])
$Sa\Omega = a^*\Omega$, polar decomposition $S = J\Delta^{1/2}$, modular operator and conjugation. Statement of Tomita's theorem: $\Delta^{it} \mathcal{M} \Delta^{-it} = \mathcal{M}$ and $J\mathcal{M}J = \mathcal{M}'$. We prove the key lemmas; auxiliary functional-analytic results are cited.

**Week 6 — Modular flow and KMS.** ([[week-06-modular-flow-and-kms|notes]])
$\sigma_t(a) = \Delta^{it} a \Delta^{-it}$. KMS theorem: $\Omega$ is KMS for $\sigma_t$ at $\beta = -1$. Physical interpretation: modular flow is "thermal time." Examples: type I (modular flow trivializes), type III (modular flow is the only intrinsic time).

**Week 7 — Connes cocycle and relative modular operator.** ([[week-07-connes-cocycle-and-relative-entropy|notes]])
Two states $\omega, \phi$ → relative modular operator $\Delta_{\omega,\phi}$ → Connes cocycle $(D\omega/D\phi)_t$ as a unitary cocycle for the modular flow. [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] $S(\omega \| \phi) = -\langle \Omega_\omega, \log \Delta_{\phi,\omega} \Omega_\omega \rangle$ — the entropy that survives in type III. *Problem set:* compute relative entropy for finite-dim examples; verify monotonicity on a toy case.

### Block C: Modular structure of free QFT (Weeks 8–12) — skeleton

**Week 8 — Midterm + free-field algebras.** ([[week-08-free-field-algebras-and-weyl-operators|notes]])
Midterm (in-class, 2 hr): operator-algebra computations, modular operator for finite-dim examples, KMS verification. Then introduce: free scalar in Minkowski → Wightman two-point function → [[weyl-operators|Weyl operators]] $W(f) = \exp(i\phi(f))$ and the Weyl algebra.

**Week 9 — Local algebras and the Reeh–Schlieder theorem.** ([[week-09-reeh-schlieder-and-local-algebras|notes]])
$\mathcal{A}(\mathcal{O})$ for spacelike regions → Reeh–Schlieder (vacuum is cyclic and separating for any open region) → consequence: every local algebra has a Tomita–Takesaki structure. *Problem set:* verify the Weyl algebra structure for a free scalar in 2d.

**Week 10 — Rindler wedge and Bisognano–Wichmann.** ([[week-10-bisognano-wichmann|notes]])
Right Rindler wedge → modular operator equals the boost generator: $\Delta_R^{it} = e^{-2\pi K_{\text{boost}} t}$. *This is the central computational lecture.* Includes derivation of the Unruh temperature as a corollary; comparison with KMS at $T = a/2\pi$.

**Week 11 — Bell-CHSH in QFT.** ([[week-11-bell-chsh-in-qft|notes]])
[[bell-chsh-inequality|Bell–CHSH inequality]] recap → Summers–Werner theorem: maximal Tsirelson violation $|C| = 2\sqrt{2}$ between any two spacelike-separated wedges in any QFT vacuum, as a direct consequence of [[tomita-takesaki-modular-theory|Tomita–Takesaki]] + [[type-iii-von-neumann-algebras|type III₁]] structure. Connection to the group's papers (smeared [[weyl-operators]], [[brst-symmetry|BRST]]-invariant formulations, bumpified Haar wavelet test functions). *Problem set:* compute Bell–CHSH for a free-scalar pair in a specific test-function basis; verify Tsirelson saturation in the limit.

**Week 12 — Type III₁ classification of QFT algebras.** ([[week-12-type-III1-classification-of-qft-algebras|notes]])
Sketch: Haag–Hugenholtz–Winnink + Connes structure theorem ⇒ local QFT algebras are hyperfinite [[type-iii-von-neumann-algebras|type III₁]]. Implications: no traces, no density matrices, no von Neumann entropy → [[araki-uhlmann-relative-entropy|Araki–Uhlmann]] is the only entropy that exists. Motivation for the [[crossed-product-construction|crossed product]] (next block).

### Block D: Crossed products (Weeks 13–15) — skeleton

**Week 13 — The crossed product construction.** ([[week-13-crossed-product-construction|notes]])
$\mathcal{M} \rtimes_\sigma \mathbb{R}$ → action on $\mathcal{H} \otimes L^2(\mathbb{R})$ → generators: $\mathcal{M}$ + the unitary $U(t)$ implementing $\sigma$. Connes' theorem: III × $\mathbb{R}$ → II. *Problem set:* construct the crossed product explicitly for a finite-dim example.

**Week 14 — Trace and entropy on the dressed algebra.** ([[week-14-dressed-entropy|notes]])
The Type II_∞ trace: explicit construction → von Neumann entropy on the crossed product → relation to [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] on the original algebra (the difference is the "clock contribution"). *Problem set:* compute the trace on the crossed product of a type I algebra (sanity check).

**Week 15 — Bridge to Semester II: the TFD and gravity.** ([[week-15-tfd-and-bridge-to-sem-ii|notes]])
Two-sided algebras → thermofield double state → Witten's heuristic: gravity introduces an automatic crossed product. Preview of CPW for Sem II. **Take-home final** assigned: 4–5 problems combining the semester (e.g., "compute the crossed product of the Rindler algebra and verify the trace formula for a coherent state").

---

## 7. Semester II — Literatura Recente (15 weeks)

A reading seminar on the recent literature. Students take turns presenting; the instructor steers, fills gaps, and is explicit about which steps are algebraic (we own these from Semester I) versus holographic (taken on physical trust).

### How a typical seminar week runs

- **First hour:** student presents an assigned subsection. The presenter states the technical claim, identifies prerequisites, and reproduces one nontrivial calculation.
- **Second hour:** discussion + instructor fills gaps + algebra/holography demarcation.
- **Office hour (separate day):** anyone can come to work through the mini-calculation collectively.

### Block 1 — Witten 2022, *Gravity and the crossed product* (Weeks 1–4) — skeleton

**Week 1 — Setup and motivation.** ([[sem2-week-01-witten-setup|notes]])
Large-$N$ limit of a holographic CFT → single-trace operators → algebra at large $N$ becomes [[type-iii-von-neumann-algebras|type III₁]]. Why semiclassical gravity demands an algebraic upgrade.

**Week 2 — Witten's construction.** ([[sem2-week-02-witten-crossed-product|notes]])
Gauging the boost / time-translation that drove Sem I modular flow → the ADM Hamiltonian as a constraint → emergent [[crossed-product-construction|crossed product]].

**Week 3 — Generalized entropy.** ([[sem2-week-03-generalized-entropy-on-dressed-algebra|notes]])
Witten's derivation of $S_{\text{gen}} = \mathrm{Tr}(\hat{\rho} \log \hat{\rho}) + \text{const}$ on the dressed algebra.

**Week 4 — Free-field analogue and mini-calculation.** ([[sem2-week-04-free-field-mini-calculation|notes]])
**Mini-calculation:** reproduce Witten's trace formula in the free-field [[rindler-wedges|Rindler]] analogue, dressing by the boost generator instead of ADM. Everything explicit, students compute.

### Block 2 — Chandrasekaran–Penington–Witten, *Large N algebras and generalized entropy* (Weeks 5–8) — skeleton

**Week 5 — The TFD as a Type III₁ KMS state.** ([[sem2-week-05-tfd-and-two-sided-modular-structure|notes]])
Two-sided eternal BH → boundary algebras $\mathcal{A}_L, \mathcal{A}_R$ → modular operator on the TFD = boost. **Guest lecture slot 1 (suggested topic: [[brst-symmetry|BRST]] and algebraic structure in gauge theory).**

**Week 6 — The CPW construction.** ([[sem2-week-06-cpw-dressing-by-adm|notes]])
Adjoining the time-translation: $\hat{\mathcal{A}}_R = \mathcal{A}_R \rtimes \mathbb{R}$ becomes type II_∞. Subtle identifications: which Hamiltonian is dressed, which observer's clock, why the construction respects the two-sidedness.

**Week 7 — Trace, entropy, and the area law.** ([[sem2-week-07-cpw-trace-entropy-area-law|notes]])
The semifinite trace explicitly. Comparison: $S_{\text{vN}}^{(\text{II})} = S_{\text{gen}}$ up to additive constant. **Mini-calculation:** the CPW construction in the free-field two-Rindler-wedge analogue.

**Week 8 — Bell-CHSH between the two sides.** ([[sem2-week-08-bell-chsh-on-tfd|notes]])
**Guest lecture slot 2 (suggested topic: Bell-CHSH via [[weyl-operators|Weyl operators]] in QFT).** Discussion: Bell violation between $\mathcal{A}_L$ and $\mathcal{A}_R$ in the TFD as a probe of "spacetime connectivity"; connects to the open question [[bell-chsh-in-holographic-setting]]. **Mini-calculation:** Bell-CHSH violation between two complementary Rindler wedges in the TFD (free scalar). Direct extension of Summers–Werner from Semester I Week 11.

### Block 3 — Hong Liu's lectures (Weeks 9–10) — skeleton

Two weeks on Liu's pedagogical review — the connective tissue between the technical Witten/CPW machinery and the AAJ perturbative analysis. Liu's lectures are extensive (~110 pp) and reward careful reading; this block gives them their proper weight.

**Week 9 — Type III at large $N$ and modular flow as bulk geometric flow.** ([[sem2-week-09-liu-type-iii-and-modular-geometry|notes]])
Liu §3 + parts of §5: structural foundations. Type III$_1$ at large $N$ is a structural feature, not an artefact. Casini–Huerta–Myers modular Hamiltonian for ball-shaped regions in CFT vacuum: $K_{ball} = 2\pi \int (R^2 - r^2)/(2R)\, T_{00}\, d^{d-1}x$. Identification of the bulk Killing flow that implements the boundary modular flow (modular flow ↔ bulk geometric flow). Worked example: the dictionary for a 2D / 4D CFT ball region.

**Week 10 — Crossed products, algebraic ER=EPR, semiclassical limits.** ([[sem2-week-10-liu-crossed-products-and-er-epr|notes]])
Liu §5 (rest) + §7: how the crossed product reduces to area-plus-bulk-entanglement in the semiclassical limit; the algebraic version of ER=EPR (commutant relationships encoding bulk connectivity); Liu's framing of how Witten 2022 / CPW / AAJ fit relative to one another. **Final write-up draft due** end of Week 10 (end of Liu block, before students enter the AAJ material).

### Block 4 — Ahmad–Jefferson, *Algebraic perturbation theory* (Weeks 11–13) — skeleton

The climax of the course, and the paper most directly tied to ongoing research. Compressed to 3 weeks (vs the original 4) by merging the abstract cocycle setup with its first GJW application, freeing a week for Liu (Block 3).

**Week 11 — Cocycle perturbation series and application to GJW.** ([[sem2-week-11-aaj-cocycle-perturbation-and-gjw|notes]])
Recap of Sem I Week 7 (Connes cocycle). AAJ §2–3: the perturbation series for $(D\omega_V/D\omega)_t$, distinguished from interaction-picture perturbation theory. The GJW deformation $V = g \mathcal{O}_L \mathcal{O}_R$ as a cocycle perturbation; perturbed modular flow; perturbed dressed entropy.

**Week 12 — Corrections beyond subleading order.** ([[sem2-week-12-aaj-corrections-and-mini-calc|notes]])
AAJ §4–5: 20 new entropy corrections at quadratic order in $g$. Discuss which corrections are universal (algebraic) versus holography-specific. **Mini-calculation:** reproduce the leading cocycle-perturbed entropy in the free-field two-Rindler-wedge analogue with a Weyl-bilinear perturbation $V = g\, W(f_L) W(f_R)$.

**Week 13 — Open questions and positioning.** ([[sem2-week-13-aaj-open-questions-and-positioning|notes]])
Where does AAJ leave the field? Which problems are tractable next? Final write-up topics are confirmed; ambitious students may use this week to draft an extended technical section.

### Block 5 — MSY and outlook (Weeks 14–15) — skeleton

**Week 14 — MSY: the bulk side; dS aside.** ([[sem2-week-14-msy-bulk-and-desitter-aside|notes]])
Maldacena–Stanford–Yang on traversable wormholes. Shapiro time advance, ANEC violation in the bulk, gravitational backreaction. Crucially: present this as the side of the story the algebra does *not* see. Honest scoping of the algebra/bulk gap. Closing aside (~1 lecture): CLPW (arXiv:2206.10780) on the de Sitter static patch as a contrasting type II$_1$ example — same crossed-product machinery, different geometry, different algebra type.

**Week 15 — Final write-up presentations.** ([[sem2-week-15-presentations-and-outlook|notes]])
Each student gives a 20-minute talk on their final write-up topic. Group discussion. Closing lecture: a one-page sketch of "where this course leaves us" — open questions, possible thesis topics, which collaborators in the group can supervise what.

---

## 8. Guest lectures

Two guest-lecture slots are reserved in Semester II:

- **Slot 1, Week 5** — suggested topic: [[brst-symmetry|BRST]] and algebraic perspectives in gauge theory. Provides a cross-link to the group's other research line and gives students a second viewpoint on "algebra encoding constraints."
- **Slot 2, Week 8** — suggested topic: Bell-CHSH via [[weyl-operators|Weyl operators]] in QFT. Embeds the group's Bell-inequality program into the seminar at the natural point in the syllabus.

Specific guest lecturers will be confirmed semester by semester depending on availability of collaborators and visitors. Additional guest spots may be added if a relevant visitor is in town during the semester.

---

## 9. Recurring threads across the course

Three threads weave through both semesters and are flagged at each occurrence in the syllabus:

1. **Modular theory.** From abstract Tomita–Takesaki (Sem I Block B) to its physical realization in Rindler (Sem I Week 10) to its perturbed form via Connes cocycle (Sem II Block 4).
2. **Bell-CHSH and quantum information.** From Summers–Werner in QFT (Sem I Week 11) to TFD violation (Sem II Week 8) to the holographic open question.
3. **Type III₁ → Type II_∞ via crossed product.** From the abstract construction (Sem I Block D) to its physical realization in gravity (Sem II Blocks 1, 2, 4).

These threads make the course feel like one coherent investigation rather than a sequence of disconnected topics.

---

## 10. Connection to the wiki

Each lecture has, or will create, a corresponding wiki page (concept, paper, or question). By the end of Semester I, the wiki will contain a complete pedagogical thread on the algebraic foundations. By the end of Semester II, it will contain wiki pages for every paper read and a research-question entry for each final write-up.

Lecture notes accumulate under `wiki/courses/2026-algebraic-qft-course/notes/` and become a durable resource — the next student or visiting collaborator can read straight from the wiki.

---

## 11. Risks and contingencies

| Risk | Likelihood | Mitigation |
|---|---|---|
| Low enrollment (3–5 students) | Likely | Fine for a topics course; smaller class lets the seminar half work better. |
| Students hit a wall on Tomita–Takesaki in Weeks 4–6 | Likely | Hold the schedule firm; add an extra office hour during those weeks. |
| Instructor learning some material in real time | Certain | By design. Lead from the algebra side (group's strength); be explicit about which Witten/CPW/AAJ claims are taken on physical trust. |
| Pacing miscalibration in Sem I | Possible | At Week 5 review point, reallocate ±1 week between blocks if needed. |
| Sem II seminar uneven (some presentations weak) | Possible | First seminar of each block is presented by the instructor as a model; subsequent presentations are by students. |

---

## 12. Outcomes

By the end of the two semesters, students will have:

- Mastered operator algebras and modular theory as applied to QFT.
- Read the recent literature critically and identified its frontier.
- Written a 15–20 page exposition of one technical aspect of the field.
- Built a concrete relationship to the group's research program (via mini-calculations, write-up topics, and guest lectures from collaborators).
- Acquired the toolkit needed to begin doctoral research on any of the open questions in [[bell-inequalities-qft]], [[relative-entropy-qft]], or holographic von Neumann algebras.

The course is also a vehicle for instructor learning: by co-reading AAJ and CPW with prepared students, the instructor builds independent fluency in the recent literature without spending a sabbatical on it.

---

*Plan committed 2026-05-08. To be revised after the first run.*
