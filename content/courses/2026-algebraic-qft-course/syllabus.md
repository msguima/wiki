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
modified: 2026-08-24
---

# Estrutura Algébrica da Teoria Quântica de Campos

*Written by AI assistants under the scientific and pedagogical supervision of Marcelo S. Guimarães; see [[ai-authorship]] for the division of labour and the models involved.*

**Álgebras, Fluxo Modular e Aplicações**

A two-semester graduate course on the algebraic structure of quantum field
theory, from operator algebras and modular theory to crossed products,
traversable wormholes, and gravitational entropy. The notes form an
**instructor's internal master dossier**: they are deliberately fuller than a
single classroom run, so that the same material can support lectures, a
reading seminar, or serious self-study. The aim is to take students with basic
QFT, but no operator-algebra background, to the point where they can read and
critically discuss Witten, Chandrasekaran--Penington--Witten (CPW), and
Ahmad--Jefferson (AAJ), with the
Chandrasekaran--Longo--Penington--Witten (CLPW) de Sitter construction as a
contrasting II$_1$ example.

---

## 1. Course architecture

| | Semester I — Fundamentos | Semester II — Literatura Recente |
|---|---|---|
| **Format** | Formal lectures supported by a master dossier | Reading seminar supported by a master dossier |
| **Scheduled hours/week** | 4 hr lectures + problem sets | 2 hr seminar + 1 hr office consultation |
| **Material available/week** | Classroom core + self-study derivations | Roughly 4 hr of instructor material + research extensions |
| **Mode** | Instructor-led | Student-led, instructor-guided |
| **Anchor** | Operator algebras → modular theory → free QFT → crossed products | Witten 2022 → CPW → Liu lectures → AAJ → MSY |

The two semesters are designed to be taken in sequence. Semester II assumes
Semester I as a hard prerequisite. Students who already have an
operator-algebra background may petition to enter directly into Semester II.

### How to use the master dossier

The dossier is not a script that must be spoken from first line to last. Dense
weeks expose three routes:

- **Classroom core:** motivation, definitions, the main claim, and one
  reproducible calculation for the scheduled meeting;
- **Full derivation / self-study:** omitted analytic steps, model proofs, and
  additional examples that make the account independently readable;
- **Research extension:** source comparisons, open problems, and calculations
  that require more preparation or instructor guidance.

Semester II is intentionally not shortened to fit the two-hour seminar. The
seminar selects a route through a substantially richer instructor dossier;
the remaining material supports office hours, student presentations, later
course runs, and independent study.

---

## 2. Learning outcomes

A graduate of the course can:

1. Use the language of C\*-algebras, von Neumann algebras, and the type classification (I, II, III) fluently.
2. State and apply the [[week-05-tomita-operator|Tomita–Takesaki theorem]]; compute the modular operator $\Delta$ and the modular conjugation $J$ for explicit examples.
3. Compute the modular operator for the [[week-10-bisognano-wichmann|Rindler wedge]] of a free scalar field using Bisognano–Wichmann, and derive the Unruh effect as a corollary.
4. Construct a [[week-13-crossed-product-construction|crossed product]]
   $\mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R}$ explicitly, distinguish
   its coordinate, momentum, and dual-action variables, and explain why the
   continuous core of a type III$_1$ factor is type II$_\infty$.
5. Read [[sem2-week-09-liu-type-iii-and-modular-geometry|Liu's lectures]], Witten's "Gravity and the [[crossed-product-construction|crossed product]]," CPW, and AAJ; identify their key technical inputs and explain which steps are algebraic versus holographic.
6. Outline a research question in the area, in the form of a 15–20 page write-up.

---

## 3. Audience and prerequisites

**Assumed:** Quantum mechanics at graduate-introductory level; general relativity (basic Schwarzschild, Rindler coordinates, asymptotic regions); free quantum field theory (canonical quantization of the free scalar, Wightman functions, smeared fields).

**Not assumed:** Von Neumann algebras; functional analysis beyond Hilbert space basics; conformal field theory; AdS/CFT; Ryu–Takayanagi formula.

**Audience:** Mixed M.Sc. and Ph.D. students at UERJ. The course is open to qualified outsiders (collaborators at CBPF, [[silvio-paolo-sorella|Sorella's]] group, [[itzhak-roditi|Roditi's]] group, and mathematical physicists at IME). All assessment carries a **classroom-core track** and a **self-study or research-extension track**. Only the classroom-core problems are presumed to be assigned in a standard run.

---

## 4. Materials

### Primary texts (Semester I)

- Bratteli & Robinson, *Operator Algebras and Quantum Statistical Mechanics*, Vols. I & II (selected chapters).
- Witten, "Notes on some entanglement properties of QFT," arXiv:1803.04993.
- [[sem2-week-09-liu-type-iii-and-modular-geometry|Liu's lectures]], arXiv:2510.07017 (used as bridge to Semester II).

### Primary texts (Semester II)

- Witten, "Gravity and the crossed product," JHEP 10 (2022) 008 [arXiv:2112.12828].
- Chandrasekaran, Penington, Witten, "Large $N$ algebras and generalized entropy," arXiv:2209.10454. *(The two-sided eternal black hole; type III$_1 \to$ type II$_\infty$.)*
- Chandrasekaran, Longo, Penington, Witten, "An algebra of observables for de Sitter space," arXiv:2206.10780. *(Static patch with observer; type II$_1$. Used as contrasting example in Block 5 Wk 14, not as primary reading.)*
- Ahmad & Jefferson, "Algebraic perturbation theory: traversable wormholes and generalized entropy beyond subleading order," arXiv:2501.01487.
- Maldacena, Stanford, Yang, "Diving into traversable wormholes," arXiv:1704.05333.
- Gao, Jafferis, Wall, "Traversable wormholes via a double trace deformation," JHEP 12 (2017) 151 [arXiv:1608.05687].
- [[sem2-week-09-liu-type-iii-and-modular-geometry|Liu's lectures]] (as connective tissue).

### Reference works

- Haag, *Local Quantum Physics*, 2nd ed., Springer, 1996.
- Takesaki, *Theory of Operator Algebras*, Vol. II, Springer, 2003.

### Lecture notes

The lecture notes live under `notes/` in this course repository. They are
written as durable teaching artifacts rather than as slides or compressed
speaker notes, and may later be mirrored into the group wiki.

### Course appendices

Seven standing reference documents under `appendices/`. A–C are prerequisites-on-demand: consult them when a lecture assumes something you lack. D–G are working references used throughout.

- [[functional-analysis-survival-kit|Appendix A — Functional-Analysis Survival Kit]] — the operator theory Block A assumes: unbounded operators, closability, spectral theorem, topologies.
- [[free-field-and-rindler-primer|Appendix B — Free-Field and Rindler Primer]] — the free scalar, Wightman functions, and Rindler coordinates. Read before Block C.
- [[holography-large-n-primer|Appendix E — Holography and Large-N Primer]] — the minimum AdS/CFT needed for Semester II, for students who have not taken a prior AdS/CFT course.
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
| Midterm calculation package (Week 8) | 20% |
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
2. **Bell-CHSH in holographic settings** — develops the open question in [[sem2-week-08-bell-chsh-on-tfd|Semester II Week 8]].
3. **Embezzlement cost on the crossed product** — connects to the Ph.D. work of ismael-porfirio and erick-landim.
4. **Critical exposition of one paper** — a clean, mathematically careful exposition of CPW, CLPW (de Sitter), or AAJ for a non-specialist reader.

---

## 6. Semester I — Fundamentos (15 weeks)

### Block A: Operator algebra foundations (Weeks 1–4) — skeleton

**Week 1 — C\*-algebras, states, GNS construction.** ([[week-01-cstar-algebras-and-gns|notes]])
Banach algebras → C\*-algebras → states (positive normalized linear functionals) → GNS construction. Examples: $\mathcal{B}(\mathcal{H})$, $C(X)$, $M_n(\mathbb{C})$. *Problem set:* prove GNS for finite-dimensional examples; verify the cyclic-vector property.

**Week 2 — Von Neumann algebras and the double commutant.** ([[week-02-von-neumann-algebras|notes]])
Strong/weak operator topologies → von Neumann's bicommutant theorem → factors → projections lattice. *Starred:* finite-dimensional bicommutant proof, group von Neumann algebras, and the $\sigma$-weak topology.

**Week 3 — Type classification (I, II, III) with examples.** ([[week-03-type-classification|notes]])
Type I (matrix algebras, $\mathcal{B}(\mathcal{H})$), Type II$_1$
(the hyperfinite factor and group von Neumann algebras), and Type III. We
state Connes' subclasses III$_0$, III$_\lambda$ for $0<\lambda<1$, and
III$_1$; the Powers endpoint at $\lambda=1$ is tracial and is not III$_1$.
The QFT classification question is deferred to Block C. *Problem set:* use
finite matrix models to practice traces and projection equivalence; show
$\mathcal{B}(\mathcal{H})$ is type I$_\infty$ when $\mathcal H$ is
infinite-dimensional.

**Week 4 — KMS states and the modular interpretation.** ([[week-04-kms-states-and-type-III|notes]])
KMS condition as algebraic thermal equilibrium → Gibbs states satisfy KMS in finite dimensions → KMS extends thermal physics to type III. [[week-05-tomita-operator|Tomita–Takesaki]] preview: the modular automorphism group is the KMS flow. *Problem set:* verify KMS for Gibbs states on $\mathcal{B}(\mathbb{C}^n)$.

### Block B: [[tomita-takesaki-modular-theory|Tomita–Takesaki]] theory (Weeks 5–7) — skeleton

**Week 5 — The setup: cyclic and separating vectors.** ([[week-05-tomita-operator|notes]])
$Sa\Omega=a^*\Omega$, polar decomposition $S=J\Delta^{1/2}$, modular
operator, and modular conjugation. Statement of Tomita's theorem in the course
convention: $\Delta^{-it}\mathcal{M}\Delta^{it}=\mathcal{M}$ and
$J\mathcal{M}J=\mathcal{M}'$. We prove the key lemmas in controlled models;
the general analytic theorem is stated with references.

**Week 6 — Modular flow and KMS.** ([[week-06-modular-flow-and-kms|notes]])
$\sigma_t(a)=\Delta^{-it}a\Delta^{it}$. In the upper-strip convention,
$\Omega$ is KMS for $\sigma_t$ at $\beta=+1$. We compute the generally
nontrivial inner modular flow of a faithful density matrix and contrast it
with the typically outer modular dynamics of a type III factor. The
"thermal-time" reading is presented as an interpretation, not as part of the
Tomita--Takesaki theorem.

**Week 7 — Connes cocycle and relative modular operator.** ([[week-07-connes-cocycle-and-relative-entropy|notes]])
Two states $\omega, \phi$ → relative modular operator $\Delta_{\omega,\phi}$ → Connes cocycle $(D\omega/D\phi)_t$ as a unitary cocycle for the modular flow. [[week-07-connes-cocycle-and-relative-entropy|Araki–Uhlmann relative entropy]] $S(\omega \| \phi) = -\langle \Omega_\omega, \log \Delta_{\phi,\omega} \Omega_\omega \rangle$ — the entropy that survives in type III. *Problem set:* compute relative entropy for finite-dim examples; verify monotonicity on a toy case.

### Block C: Modular structure of free QFT (Weeks 8–12) — skeleton

**Week 8 — Midterm + free-field algebras.** ([[week-08-free-field-algebras-and-weyl-operators|notes]]; midterm paper, solutions, and rubric)
Midterm (in-class, 2 hr): operator-algebra computations, modular operator for finite-dim examples, KMS verification. Then introduce: free scalar in Minkowski → Wightman two-point function → [[week-08-free-field-algebras-and-weyl-operators|Weyl operators]] $W(f) = \exp(i\phi(f))$ and the Weyl algebra.

**Week 9 — Local algebras and the Reeh–Schlieder theorem.** ([[week-09-reeh-schlieder-and-local-algebras|notes]])
$\mathcal{A}(\mathcal{O})$ for spacetime regions → Reeh--Schlieder (the
vacuum is cyclic for every nonempty open region, under the theorem's standard
QFT hypotheses). Locality then gives separation when the causal complement
contains a nonempty open set. Hence the relevant local algebra--vacuum pairs
have Tomita--Takesaki data. *Problem set:* identify the role of the spectrum
condition, derive separation from locality plus cyclicity of the complement,
and contrast relativistic Reeh--Schlieder with explicit product-state
counterexamples.

**Week 10 — [[rindler-wedges|Rindler wedge]] and Bisognano–Wichmann.** ([[week-10-bisognano-wichmann|notes]])
Right Rindler wedge → Bisognano--Wichmann:
$\Delta_R=e^{-2\pi K}$ and, with
$U(\Lambda(u))=e^{iuK}$,
$\Delta_R^{-it}=U(\Lambda(2\pi t))$. *This is the central geometric
lecture.* We derive the Unruh temperature as a corollary and keep the Wightman
$i\epsilon$ prescription consistent with the mostly-plus metric.

**Week 11 — Bell-CHSH in QFT.** ([[week-11-bell-chsh-in-qft|notes]])
[[week-11-bell-chsh-in-qft|Bell--CHSH inequality]] recap → the
Summers--Werner maximal-correlation results, stated with their algebraic and
geometric hypotheses. We distinguish these structural theorems from explicit
families of smeared [[week-08-free-field-algebras-and-weyl-operators|Weyl operators]], which give reproducible lower bounds
and may approach, but need not attain, $2\sqrt2$. Connections to the group's
work include [[brst-symmetry|BRST]]-invariant formulations and bumpified Haar
wavelet test functions. *Problem set:* compute a certified CHSH value from a
specified free-field covariance matrix and compare it with the structural
bound.

**Week 12 — [[type-iii-von-neumann-algebras|Type III₁]] classification of QFT algebras.** ([[week-12-type-III1-classification-of-qft-algebras|notes]])
We assemble the hypothesis-sensitive route from local QFT to the hyperfinite
[[week-12-type-III1-classification-of-qft-algebras|type III₁]] factor: the relevant chain runs
through results of Driessler, Fredenhagen, Buchholz--Wichmann, and
Buchholz--D'Antoni--Fredenhagen, together with Connes--Haagerup classification.
HHW is used for equilibrium/KMS theory, not for this classification. A type
III factor has no faithful normal semifinite trace and no intrinsic reduced
density matrix; Araki relative entropy remains available, as do other
modular quantities. This is the motivation for the continuous core.

### Block D: Crossed products (Weeks 13–15) — skeleton

**Week 13 — The [[crossed-product-construction|crossed product]] construction.** ([[week-13-crossed-product-construction|notes]])
$\mathcal{M}\rtimes_{\sigma^\omega}\mathbb{R}$ → covariant action on
$\mathcal{H}\otimes L^2(\mathbb{R})$ → represented observables
$\pi_\sigma(a)$ and translations $\lambda(t)=e^{-itP}$. For the modular
action, the continuous core is semifinite; for a type III$_1$ factor it is a
type II$_\infty$ factor. *Problem set:* construct the inner-action,
finite-dimensional crossed product as a sanity check and explain why that
model is not itself a type-II factor.

**Week 14 — Trace and entropy on the dressed algebra.** ([[week-14-dressed-entropy|notes]])
The canonical semifinite trace and its dual scaling → entropy relative to a
fixed trace normalization → a finite-dimensional entropy-difference identity
→ the additional hypotheses needed to compare core entropy with
[[week-07-connes-cocycle-and-relative-entropy|Araki relative entropy]]. The auxiliary
probability distribution contributes both a differential-entropy term and a
trace-weight term. *Problem set:* compute both terms in the type-I sanity
check and verify how entropy changes when the trace is rescaled.

**Week 15 — Bridge to Semester II: the TFD and gravity.** ([[week-15-tfd-and-bridge-to-sem-ii|notes]])
Two commuting algebras → thermofield-double purification → one-sided modular
data → the additional gravitational constraints used by Witten and CPW.
Gravity does not make an abstract crossed product "automatic" without this
dictionary. **Take-home final:** 4--5 problems combining the semester,
including a complete type-I core calculation and a clearly labelled
free-field computation protocol.

---

## 7. Semester II — Literatura Recente (15 weeks)

A reading seminar on the recent literature. Students take turns presenting;
the instructor steers, fills gaps, and marks each step as algebraic,
large-$N$/perturbative, holographic, or heuristic. The weekly notes remain
full master-dossier chapters. The scheduled seminar follows their classroom
core; derivations and research extensions are retained for self-study and
future use.

### How a typical seminar week runs

- **First hour:** student presents an assigned subsection. The presenter states
  the technical claim, its hypotheses and proof status, and one reproducible
  calculation or a precisely delimited computation protocol.
- **Second hour:** discussion + instructor fills gaps + algebra/holography demarcation.
- **Office hour (separate day):** anyone can come to work through the mini-calculation collectively.

### Block 1 — Witten 2022, *Gravity and the [[crossed-product-construction|crossed product]]* (Weeks 1–4) — skeleton

**Week 1 — Setup and motivation.** ([[sem2-week-01-witten-setup|notes]])
Large-$N$ single-trace observables → a type III$_1$ factor for the exterior
algebra in the regime considered by Witten. We separate this factor from the
central energy-fluctuation variable present in the strict $N=\infty$ extended
algebra and ask what changes at the first nontrivial order in $1/N$.

**Week 2 — Witten's construction.** ([[sem2-week-02-witten-crossed-product|notes]])
The gravitational constraint, asymptotic time translation, and the
renormalized ADM-energy variable deform the strict-limit algebra into the
[[week-13-crossed-product-construction|crossed-product]] structure. We distinguish
this physical identification from the abstract continuous-core theorem.

**Week 3 — Generalized entropy.** ([[sem2-week-03-generalized-entropy-on-dressed-algebra|notes]])
For the normal core state $\hat\omega(x)=\hat\tau(h_{\hat\omega}x)$,
Witten's setting identifies
$-\hat\tau(h_{\hat\omega}\log h_{\hat\omega})$, up to the fixed additive
normalization, with generalized entropy. We track exactly which part is the
operator-algebraic entropy and which part uses the holographic dictionary.

**Week 4 — Free-field analogue and mini-calculation.** ([[sem2-week-04-free-field-mini-calculation|notes]])
**Course-built analogue:** compute the covariant representation and weighted
trace in a regulated type-I/[[rindler-wedges|Rindler]] model, with the auxiliary coordinate and
momentum kept distinct. This illustrates Witten's mechanism; it is not
presented as a free-field section of Witten's paper or as a derivation of a
gravitational area term.

### Block 2 — Chandrasekaran–Penington–Witten, *Large N algebras and generalized entropy* (Weeks 5–8) — skeleton

**Week 5 — The TFD as a Type III₁ KMS state.** ([[sem2-week-05-tfd-and-two-sided-modular-structure|notes]])
Two-sided eternal BH → boundary algebras $\mathcal{A}_L, \mathcal{A}_R$ → modular operator on the TFD = boost. **Guest lecture slot 1 (suggested topic: [[brst-symmetry|BRST]] and algebraic structure in gauge theory).**

**Week 6 — The CPW construction.** ([[sem2-week-06-cpw-dressing-by-adm|notes]])
Adjoining the time-translation: $\hat{\mathcal{A}}_R = \mathcal{A}_R \rtimes \mathbb{R}$ becomes type II_∞. Subtle identifications: which Hamiltonian is dressed, which observer's clock, why the construction respects the two-sidedness.

**Week 7 — Trace, entropy, and generalized entropy.** ([[sem2-week-07-cpw-trace-entropy-area-law|notes]])
The semifinite trace explicitly. Under CPW's large-$N$ state construction,
the type-II entropy agrees with generalized entropy up to a state-independent
constant. The gravitational area term is input through that dictionary; it
is not inferred from the width of an auxiliary clock wavefunction.
**Course-built analogue:** perform the trace and density calculation in a
regulated two-wedge model and state exactly what it does and does not test.

**Week 8 — Bell-CHSH between the two sides.** ([[sem2-week-08-bell-chsh-on-tfd|notes]])
**Guest lecture slot 2 (suggested topic: Bell--CHSH via
[[week-08-free-field-algebras-and-weyl-operators|Weyl operators]] in QFT).** We calculate correlations from a
specified quasifree covariance matrix. Interpreting a Bell violation between
$\mathcal{A}_L$ and $\mathcal{A}_R$ as evidence for spacetime connectivity is
a holographic proposal, not a consequence of CHSH or modular theory alone;
this distinction defines the open question
[[sem2-week-08-bell-chsh-on-tfd|Bell--CHSH in holographic settings]].

### Block 3 — Hong [[2025-liu-lectures-entanglement-vna|Liu's lectures]] (Weeks 9–10) — skeleton

Two weeks on Liu's pedagogical review — the connective tissue between the technical Witten/CPW machinery and the AAJ perturbative analysis. [[2025-liu-lectures-entanglement-vna|Liu's lectures]] are extensive (~110 pp) and reward careful reading; this block gives them their proper weight.

**Week 9 — Type III at large $N$ and the geometric cases of modular flow.** ([[sem2-week-09-liu-type-iii-and-modular-geometry|notes]])
Selected parts of Liu §§II--IV and VI--VIII provide the structural
foundations and the large-$N$/subregion setting. Type III$_1$ at large $N$ is
a structural feature in the regime discussed, not an artefact. As a
supplementary exactly controlled example, for the Casini--Huerta--Myers
vacuum ball the modular Hamiltonian
$K_{\rm ball}=2\pi\int_{r<R}(R^2-r^2)/(2R)\,T_{00}\,d^{d-1}x$ generates a
geometric conformal flow; its bulk dual is geometric in the corresponding
symmetric entanglement wedge. Generic-region modular flow is not asserted to
be geometric. Worked example: the dictionary for a two- or four-dimensional
CFT ball.

**Week 10 — Crossed products, algebraic ER=EPR, semiclassical limits.** ([[sem2-week-10-liu-crossed-products-and-er-epr|notes]])
Selected parts of Liu §§V and VII--IX: the crossed product, subregion--subalgebra
duality, emergent bulk concepts, and observer models. We examine how
crossed-product entropy is related to area plus bulk entropy under a
semiclassical holographic dictionary, and then isolate the additional
hypotheses behind Liu's proposed algebraic ER=EPR reading. Commutants and
modular data do not by themselves prove bulk connectivity. **Final write-up
draft due** at the end of Week 10.

### Block 4 — Ahmad–Jefferson, *Algebraic perturbation theory* (Weeks 11–13) — skeleton

This block is the course's most detailed perturbative source study. Its three
seminar weeks are backed by full master-dossier chapters: the source's setup,
the complete through-quadratic bookkeeping, and a separate week for checking
scope and open questions.

**Week 11 — Unitary perturbation of modular data and application to GJW.** ([[sem2-week-11-aaj-cocycle-perturbation-and-gjw|notes]])
Recap of Sem I Week 7. AAJ §2 reviews the crossed-product entropy framework;
§3 develops perturbation theory for a unitarily perturbed state and its
modular data. We distinguish this construction from the course's separate
Araki perturbation model $\rho_V\propto e^{-(K+V)}$ and from ordinary
interaction-picture perturbation theory. The relation to the GJW double-trace
deformation is then stated at the order actually controlled.

**Week 12 — Corrections beyond subleading order.** ([[sem2-week-12-aaj-corrections-and-mini-calc|notes]])
AAJ §4 finds five additional terms linear in the perturbation and fifteen
quadratic terms: twenty corrections **through** quadratic order, not twenty
quadratic terms. We sort algebraic bookkeeping from state- and
holography-specific input. **Controlled model calculation:** for a bounded
self-adjoint two-sided perturbation, compute the first BCH/Dyson term and one
entropy contribution. The full AAJ list remains a source-guided audit, not
something silently claimed to have been reproduced by a Weyl toy model.

**Week 13 — Open questions and positioning.** ([[sem2-week-13-aaj-open-questions-and-positioning|notes]])
AAJ §5: what has been established, what remains conditional, and which
questions are tractable next. We compare the paper's result with the original
linear-order GJW analysis and formulate final-write-up topics with explicit
completion criteria.

### Block 5 — MSY and outlook (Weeks 14–15) — skeleton

**Week 14 — MSY: the bulk side; dS aside.** ([[sem2-week-14-msy-bulk-and-desitter-aside|notes]])
Maldacena--Stanford--Yang on traversable wormholes: Shapiro time advance,
averaged-null-energy violation, and gravitational backreaction. This is the
part of the story not supplied by operator algebra alone. The closing CLPW
aside (arXiv:2206.10780) treats the de Sitter static patch with an observer.
Its type II$_1$ trace comes from the observer-Hamiltonian spectral restriction
and bounded-below choice, not from a finite-dimensional Hilbert space or from
compactness of the horizon by itself.

**Week 15 — Final write-up presentations.** ([[sem2-week-15-presentations-and-outlook|notes]])
Each student gives a 20-minute talk on their final write-up topic. Group discussion. Closing lecture: a one-page sketch of "where this course leaves us" — open questions, possible thesis topics, which collaborators in the group can supervise what.

---

## 8. Guest lectures

Two guest-lecture slots are reserved in Semester II:

- **Slot 1, Week 5** — suggested topic: [[brst-symmetry|BRST]] and algebraic perspectives in gauge theory. Provides a cross-link to the group's other research line and gives students a second viewpoint on "algebra encoding constraints."
- **Slot 2, Week 8** — suggested topic: Bell-CHSH via [[week-08-free-field-algebras-and-weyl-operators|Weyl operators]] in QFT. Embeds the group's Bell-inequality program into the seminar at the natural point in the syllabus.

Specific guest lecturers will be confirmed semester by semester depending on availability of collaborators and visitors. Additional guest spots may be added if a relevant visitor is in town during the semester.

---

## 9. Recurring threads across the course

Three threads weave through both semesters and are flagged at each occurrence in the syllabus:

1. **Modular theory.** From abstract [[tomita-takesaki-modular-theory|Tomita–Takesaki]] (Sem I Block B) to its
   physical realization in Rindler (Sem I Week 10), then to two distinct
   comparison tools in Semester II: Connes cocycles for changes of reference
   state, and AAJ's unitary-covariance, spectral-reweighting, and BCH
   perturbation framework. The course compares these tools without
   identifying them.
2. **Bell-CHSH and quantum information.** From Summers–Werner in QFT (Sem I Week 11) to TFD violation (Sem II Week 8) to the holographic open question.
3. **Type III₁ → Type II_∞ via crossed product.** From the abstract construction (Sem I Block D) to its physical realization in gravity (Sem II Blocks 1, 2, 4).

These threads make the course feel like one coherent investigation rather than a sequence of disconnected topics.

---

## 10. Connection to the wiki

Each lecture may also create a corresponding wiki page (concept, paper, or
question). The repository is the canonical course dossier; the wiki is a
curated public-facing selection rather than a prerequisite for reading it.

The complete notes accumulate under `notes/`. Selected pages can be mirrored
to the wiki after their source claims and calculations have been checked.

---

## 11. Risks and contingencies

| Risk | Likelihood | Mitigation |
|---|---|---|
| Low enrollment (3–5 students) | Likely | Fine for a topics course; smaller class lets the seminar half work better. |
| Students hit a wall on Tomita–Takesaki in Weeks 4–6 | Likely | Hold the schedule firm; add an extra office hour during those weeks. |
| Source-dependent recent material requires extra preparation | Certain | Lead from the algebra side; label each Witten/CPW/AAJ input as proved, perturbative, holographic, or heuristic, and keep a source-checked derivation sheet for the classroom route. |
| Pacing miscalibration in Sem I | Possible | At Week 5 review point, reallocate ±1 week between blocks if needed. |
| Sem II seminar uneven (some presentations weak) | Possible | First seminar of each block is presented by the instructor as a model; subsequent presentations are by students. |

---

## 12. Outcomes

By the end of the two semesters, students will have:

- Learned to work reliably with operator algebras and modular theory as
  applied to QFT, including the hypotheses behind the main structural claims.
- Read the recent literature critically and identified its frontier.
- Written a 15–20 page exposition of one technical aspect of the field.
- Built a concrete relationship to the group's research program (via mini-calculations, write-up topics, and guest lectures from collaborators).
- Acquired the toolkit needed to begin doctoral research on the open questions developed in [[week-11-bell-chsh-in-qft|Bell inequalities in QFT]], [[week-07-connes-cocycle-and-relative-entropy|relative entropy]], or holographic von Neumann algebras.

The course is also a vehicle for instructor learning: by co-reading AAJ and CPW with prepared students, the instructor builds independent fluency in the recent literature without spending a sabbatical on it.

**Wiki connections.** [[weyl-operators|Weyl operators]] · [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] · [[bell-chsh-inequality|Bell–CHSH inequality]] · [[bell-inequalities-qft|Bell inequalities in QFT]] (research area) · [[relative-entropy-qft|relative entropy in QFT]] (research area) · [[bell-chsh-in-holographic-setting|Bell–CHSH in holographic settings]] (open question)

---

*Initial plan committed 2026-05-08; master-dossier revision completed
2026-08-24. To be recalibrated after the first classroom run.*
