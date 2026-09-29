---
title: "Sem II Week 15 — Final Presentations and Outlook (Course Capstone)"
type: lecture-notes
course: syllabus
semester: 2
week: 15
block: 5
duration: "master dossier: 4 hours of material; classroom core: 2-hour seminar + 1-hour office/self-study"
prerequisites: the entire course
target_paper: "(synthesis week — no new target paper)"
modified: 2026-09-29
---

# Sem II Week 15 — Final Presentations and Outlook

> *A useful capstone does more than repeat the slogans. It tells students which statements are intrinsic operator algebra, which are exact models, which depend on AQFT hypotheses, which use the holographic dictionary, and which remain open. The course has given us one common language—standard pairs, modular flow, crossed products, traces, and relative entropy—but not one theorem that turns every algebraic datum into geometry. The last week is where that discipline becomes visible.*

> **Route through this master dossier.** **Classroom core (two-hour seminar):** the student presentations, the synthesis diagram, and the regime/claim-status ledger. **Full derivation or self-study:** the conceptual audit and the complete self-test, with earlier weeks reopened whenever an answer depends on a hypothesis. **Research extension or office hour:** the open-direction map, release checklist, and one-page proposal exercise. The capstone is a diagnostic map of the full course, not a compressed replacement for it.

## 0. No new reading

Revisit only what the final project needs:

- Sem I Weeks 5–7 for standard pairs, modular flow, Connes cocycles, and [[relative-entropy-qft|relative entropy]];
- Sem I Weeks 10–14 for Bisognano–Wichmann, Bell inequalities, type III, the continuous core, and type-II entropy;
- Sem II Weeks 1–3 for Witten's strict-$N=\infty$ versus perturbative-$1/N$ regimes;
- Sem II Weeks 5–8 for the TFD, CPW, and the exact Bell models/protocol;
- Sem II Weeks 9–10 for modular geometry and the large-$N$ synthesis;
- Sem II Weeks 11–13 for AAJ's unitary perturbation framework and its distinction from Araki perturbation;
- Sem II Week 14 for the MSY comparison and CLPW's positive-energy corner.

## 1. Final presentations

### 1.1 Format

- 20-minute talk;
- 5 minutes of questions;
- final write-up of at least 15 pages, or the length stated in the current syllabus;
- all numerical/symbolic work submitted in a reproducible form.

### 1.2 A presentation structure that exposes understanding

1. **Question and motivation — 3 minutes.** What is the narrow question, and why is it not already answered by the cited theorem?
2. **Controlled input — 5 minutes.** State the algebra, state/vector, representation, regulator, and imported result.
3. **Calculation or argument — 9 minutes.** Show one derivation in enough detail that the audience can check a sign or normalization.
4. **Status ledger — 3 minutes.** Separate proved/exact, finite-regulator, numerical, holographic interpretation, and open claims.

The talk should contain at least one sentence of the form: “This step uses ___ and would fail without ___.” That sentence is often the clearest evidence that the speaker owns the argument.

### 1.3 Defensible topic families

1. **Finite-regulator algebraic perturbation.** Compare AAJ's unitary BCH deformation with a fixed-algebra Araki/Gibbs perturbation. Do not call them the same series.
2. **[[bell-inequalities-qft|Bell-CHSH]] in a specified QFT or holographic setup.** Give explicit observables and a reproducible lower bound; distinguish it from the algebraic supremum and from bulk connectivity.
3. **Embezzlement under passage to a crossed product.** Start from the operational invariants of arXiv:2401.07299; do not use “exact” when the theorem means arbitrarily small error.
4. **Critical source exposition.** Audit one of Witten, CPW, AAJ, or CLPW equation by equation and reproduce one real calculation.
5. **Modular geometry.** Derive a symmetric modular Hamiltonian or compare a nongeometric case, keeping the code-subspace/holographic assumptions explicit.

## 2. The course in one diagram

$$
\text{operator algebras}
\longrightarrow
\text{standard pairs and modular flow}
\longrightarrow
\text{AQFT local algebras}
$$

$$
\longrightarrow
\text{continuous core / crossed product}
\longrightarrow
\text{semifinite trace and entropy}
\longrightarrow
\text{gravity applications and perturbations}.
$$

This is a dependency diagram, not an equivalence chain. In particular:

- Tomita–Takesaki theory applies to a standard pair without gravity.
- The continuous core of a type-III factor is type II independently of holography.
- Witten, CPW, and CLPW identify particular gravitational degrees of freedom with the algebraic extension in specified semiclassical regimes.
- A type-II entropy becomes a generalized gravitational entropy only after the state, trace normalization, and holographic/gravitational dictionary have been supplied.

### The calibrated one-sentence summary

> **Under the standard AQFT hypotheses, sharp local QFT algebras are often type III$_1$ and have no intrinsic trace. Their modular crossed products are semifinite. In the Witten/CPW/CLPW gravitational constructions, the added charge/observer degrees of freedom realize this extension and permit a renormalized entropy that agrees, in the stated semiclassical regime and up to the stated constant, with generalized entropy.**

Every phrase is doing work. “Often” prevents a theorem about a class of nets from becoming a definition of QFT. “Intrinsic” permits ambient trace-class representatives without inventing a trace on the factor. “In the stated regime” keeps exact finite $N$, strict $N=\infty$, and perturbative $1/N$ separate.

## 3. Regime map

The four most frequently confused regimes are:

| Regime/object | Algebraic feature | What one may say |
|---|---|---|
| sharp local continuum region | commonly type III$_1$ under AQFT assumptions | no intrinsic trace/density element |
| strict large-$N$ simple algebra in Witten's setup | type III$_1$; rescaled energy fluctuation central in the extended algebra | extended algebra is not yet a factor |
| Witten's perturbatively corrected algebra | $U$ is dressed by $\widehat h/(\beta_HN)$ and the result is a type-II$_\infty$ crossed-product factor; physical gravitational terms are organized with $G_N\sim1/N^2$ | canonical trace up to scale; entropy differences; do not identify the displayed $1/N$ generator correction with every $1/N^2$ observable correction |
| exact finite-$N$ complete boundary theory | expected type I globally | ordinary Hilbert-space quantum mechanics; local continuum nuance remains |

This table prevents two common mistakes: calling Witten's strict-$N=\infty$ extended algebra type II$_\infty$, and calling every finite-$N$ sharp subregion type I.

## 4. What the free-field analog did for us

The Rindler free field is a controlled laboratory for some, not all, arrows in the course.

| Question | Free-field status | Gravitational status |
|---|---|---|
| one-sided cyclicity/separatingness | Reeh–Schlieder/BW hypotheses | assumed or argued for chosen large-$N$ algebra |
| modular flow | exact geometric boost | ADM/Killing identification uses holographic input |
| KMS thermality | exact | Hawking/TFD interpretation in chosen state |
| continuous core and trace | genuine type-III free-field core and trace available abstractly; the explicit $e^{-p}dp$ weighted integral is the separate inner-action/type-I Fourier audit | charge/clock receives gravitational interpretation |
| Bell correlations | exact two-mode model; Gaussian protocol; AQFT supremum theorem under hypotheses | explicit boundary observable construction remains model dependent |
| unitary perturbation | exact nested commutators and Gaussian expectations | AAJ weight plus gravity data |
| horizon area or Shapiro shift | absent—no dynamical gravity | bulk calculation required |

The analog catches algebraic errors, sign errors, and unsupported observable claims. It cannot verify an area term, a QES motion, or a wormhole.

## 5. Proof-status map

This is the instructor's capstone reference. “Course proof” means the notes derive the stated version. “Source result” means the notes identify and quote the primary source. “Model” means a deliberately restricted calculation.

| Result | Course location | Status and boundary |
|---|---|---|
| Gelfand–Naimark and bicommutant theorems | I.1–I.2 | Gelfand–Naimark stated, finite/model components proved; bicommutant proved in general (I.2 §4.2) |
| Murray–von Neumann type classification | I.3 | structural theorem stated; examples developed |
| Tomita–Takesaki, $J\mathcal MJ=\mathcal M'$ | I.5 | source theorem; requires a cyclic-separating vector |
| KMS/modular relation | I.6 | finite-dimensional proof; general theorem stated |
| course cocycle convention | I.7, II.11 | $(D\omega_\rho/D\omega_\sigma)_t=\rho^{-it}\sigma^{it}$ in type I |
| relative entropy identity/first law | I.7, II.12 | exact finite-dimensional identity; general results stated |
| Reeh–Schlieder | I.9 | source theorem under QFT assumptions |
| Bisognano–Wichmann | I.10 | source theorem; geometric wedge modular flow |
| Tsirelson bound | I.11 | proved |
| Summers–Werner maximality | I.11, II.8 | source result with state/geometry/algebra hypotheses; not every quartet is optimal |
| local hyperfinite type III$_1$ | I.12 | source synthesis requiring factoriality, phase-space/hyperfinite input, and a separate scaling or modular-spectrum type-III$_1$ input |
| continuous core is semifinite | I.13 | Connes–Takesaki result stated; representation constructed |
| type-II entropy and trace-scale ambiguity | I.14, II.3 | algebraic calculation plus source theorem |
| finite-dimensional TFD standard pair | I.15, II.5 | proved for each one-sided matrix algebra |
| continuum TFD/Rindler statement | II.5 | one-sided standard pairs; formal mode TFD is not a literal continuum tensor product |
| $J\mathcal A_RJ=\mathcal A_L$ | II.5 | $J\mathcal A_RJ=\mathcal A_R'$ is automatic; equality with $\mathcal A_L$ needs duality input |
| ER=EPR criterion | II.5, II.8 | heuristic/structural analogy, not an iff theorem |
| Witten strict-$N=\infty$ extension | II.1 | central rescaled energy mode; nonfactor |
| Witten perturbative $1/N$ algebra | II.1–II.3 | type-II$_\infty$ crossed product in source regime |
| Witten entropy | II.3 | exact trace/density calculation in §§3.4–3.5; gravitational interpretation separately identified |
| CPW two-sided construction | II.5–II.7 | source construction; free-field modular analog only |
| exact two-mode TFD CHSH maximum | II.8 | course calculation: $2\sqrt{1+\operatorname{sech}^2(\beta\omega/2)}$ |
| continuum cosine-Weyl CHSH | II.8 | exact covariance formula and computation protocol; no claimed universal saturation by this ansatz |
| large-$N$ type-III mechanism | II.9 | source result; ITPFI mode-ratio section is a diagnostic, not a proof from one modular spectrum |
| CHM ball modular Hamiltonian | II.9 | $d=2$ conformal-map derivation; general symmetric result sourced |
| modular flow as bulk geometry | II.9 | exact in special QFT symmetries; holographic version conditional/code-subspace dependent |
| Araki implementing-cocycle series | II.11 | course finite-dimensional reconstruction, with partition phase restored for normalized states |
| AAJ method | II.11–II.13 | unitary covariance, changed weight/Jacobian, BCH—not the course cocycle series |
| GJW deformation | II.11, II.14 | source linear-order traversability result for suitable sign/profile |
| $M_2$ quadratic entropy model | II.12 | exact course calculation; no linear term because $V$ was chosen off diagonal |
| AAJ new-term count | II.12 | five additional linear plus fifteen quadratic, through $O(1/N^2)$ |
| free-field AAJ “mini-calc” | II.12 | honest finite-regulator protocol; continuum reproduction not claimed |
| type-III$_1$ universal [[entanglement-embezzlement\|embezzlement]] | II.13 | source operational theorem: arbitrarily small error; every normal state embezzling |
| harmonic finite catalyst | II.13 | van Dam–Hayden source; edge estimate is course intuition, not a new fidelity proof |
| Raychaudhuri area response | II.14 | derived at leading order with stated horizon boundary condition |
| generalized second law in GJW geometry | II.14 | not proved by Raychaudhuri; requires separate theorem hypotheses |
| MSY time advance | II.14 | source bulk result |
| CLPW type-II$_1$ algebra | II.14 | source construction with $\Pi=\Theta(-H-x)$; its trace reduces to the half-line integral in the de Sitter reference sector |
| CLPW maximum-entropy state | II.14 | proved from normalized finite trace; generalized entropy agrees up to constant semiclassically |
| detailed AAJ–MSY term matching | II.14 | open in these notes; no blanket literature claim |

### How to use the map

Before writing “we have shown,” find the row. If it says “source result,” name the source. If it says “model,” keep the model in the sentence. If it says “conditional,” state the condition before the conclusion. This habit is more valuable than memorizing another formula.

## 6. A final conceptual audit

### 6.1 TFD and two sides

The TFD vector is cyclic and separating for a one-sided algebra in the standard representation. It is not separating for the full matrix algebra generated by both sides in finite dimensions, nor for $\mathcal B(\mathcal H)$ in the wedge-dual continuum representation. Tomita theory is therefore applied to $(\mathcal A_R,\Omega_{\rm TFD})$ or $(\mathcal A_L,\Omega_{\rm TFD})$, not casually to the joint algebra.

### 6.2 Entropy and generalized entropy

A type-II trace can be rescaled. In a type-II$_\infty$ factor this shifts entropy by a state-independent constant, so entropy differences are the robust quantities. In CLPW's type-II$_1$ corner, the normalization $\operatorname{Tr}1=1$ selects the tracial maximum, while the comparison with gravitational generalized entropy still contains the usual state-independent renormalization constant.

### 6.3 Bell, embezzlement, and geometry

Strong Bell correlation and universal embezzlement are genuine operational consequences of rich infinite-algebra structure under their theorem hypotheses. Neither is an automatic wormhole detector. Minkowski wedges already show that modular duality and maximal Bell correlations can arise without inferring a dynamical Einstein–Rosen bridge.

### 6.4 Perturbations

There are at least three distinct objects:

1. physical-time Dyson evolution;
2. fixed-algebra Araki/Gibbs perturbation and its Connes cocycle;
3. AAJ's unitary transport of the algebra-state system and the resulting crossed-product reweighting.

Formal similarities among their nested integrals do not make them interchangeable.

## 7. Self-test

A student ready to use the material should be able to answer these without slogans:

1. Why does “no intrinsic density matrix” not forbid an ambient trace-class representative of a normal functional?
2. For which algebra is the TFD vector cyclic and separating?
3. What is central in Witten's strict-$N=\infty$ extended algebra, and what removes the center?
4. Why is Witten's entropy discussion in §3.5 rather than §4?
5. State the course cocycle convention and retain the normalized partition-function phase.
6. Explain in one line why a common Rindler boost does not move a packet toward the horizon.
7. Compute the exact two-mode TFD CHSH maximum.
8. Explain why a dense ratio group in one modular spectrum does not by itself prove type III$_1$.
9. Distinguish AAJ's five linear plus fifteen quadratic terms from “twenty quadratic terms.”
10. Explain why $\sigma(f_L,f_R)=0$ and which same-side symplectic form controls a right-Weyl commutator.
11. Starting from the general CLPW projection $\Pi=\Theta(-H-x)$, use $H\Psi_{\rm dS}=0$ to derive the reference-sector half-line integral and $\operatorname{Tr}\Pi=1$.
12. Give one algebra/bulk comparison that remains a proposal rather than a proved equality.

## 8. Research directions with first deliverables

### 8.1 Finite-regulator AAJ audit

Implement Eqs. (77)–(78) in a small matrix system, include the Jacobian and $\beta$ expansion, and compare with exact subsystem entropy. First deliverable: a verified $h$/$h^2$ coefficient table.

### 8.2 Bell observables beyond existence

Choose a concrete QFT state and region pair; specify four operators; compute a lower bound with errors. First deliverable: a reproducible covariance or correlation matrix, not a geometric slogan.

### 8.3 Crossed-product embezzlement

Translate the operational invariants of arXiv:2401.07299 to a type-II$_\infty$ continuous core or finite corner. First deliverable: a theorem-led literature map that identifies what is already implied by factor type and what needs a new protocol.

### 8.4 Moving-region algebras

Define comparison maps between $\mathcal A_h$ for perturbed regions/QESs. First deliverable: one finite or free-field example in which the embeddings/channels are explicit.

### 8.5 Interacting relative entropy

Start from a perturbatively controlled interacting QFT and compute a relative-entropy coefficient with renormalization conditions stated. First deliverable: one regulator-independent difference or a clear obstruction.

## 9. Assessment and release checklist

Use the current syllabus percentages. Independently of weighting, a passing final project must satisfy:

- correct algebra/state/representation specified;
- source claims tied to exact sections, equations, or theorems;
- conventions fixed, including the mostly-plus metric and modular-flow sign;
- no density matrix assigned intrinsically to a type-III factor;
- finite-regulator results not presented as continuum theorems;
- numerical values accompanied by inputs and convergence/error information;
- interpretations labeled separately from calculations;
- bibliography identifiers verified.

## 10. End of the course

The durable skill from these two semesters is not the ability to repeat “type III becomes type II.” It is the ability to ask: which algebra, in which representation, for which state, in which limit, with which trace normalization, and with what proof status? Once those questions are answered, the physical picture becomes clearer rather than less intuitive. That is the point of an instructor's master dossier: it preserves the derivations, the analogies, and the caveats in one place, so the classroom can move quickly without becoming careless.

There is no separate problem set. The deliverables are the final write-up, the talk, the self-test, and—if the student is continuing—a one-page proposal whose first calculation is small enough to begin next week.

**Wiki connections.** [[bell-chsh-in-holographic-setting|Bell–CHSH in holographic settings]] (open question) · [[embezzlement-cost-relative-entropy|embezzlement cost and relative entropy]] (open question) · [[relative-entropy-interacting-theories|relative entropy beyond free fields]] (open question)

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 5. Last revised 2026-09-29.*

***End of the course.***
