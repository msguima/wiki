---
title: "Gauge/Gravity Duality: Foundations and Black-Hole Information"
type: course
instructor: Marcelo S. Guimarães
institution: UERJ — Departamento de Física Teórica
duration: two semesters (~30 weeks)
audience: M.Sc. and Ph.D. students with standard QFT background
prerequisites: Quantum mechanics; general relativity (basic Schwarzschild, asymptotic regions); free quantum field theory (canonical quantization, Wightman functions); basic path integral
not assumed: string theory, conformal field theory beyond global conformal invariance, operator algebras, AdS/CFT
language: lectures in Portuguese; written materials in English
modified: 2026-05-26
---

# Gauge/Gravity Duality: Foundations and Black-Hole Information

*Written by AI assistants under the scientific and pedagogical supervision of Marcelo S. Guimarães; see ai-authorship for the division of labour and the models involved.*


A two-semester graduate course on the AdS/CFT correspondence and its applications to black-hole information. Designed as a self-contained route from standard QFT to the recent literature on Page curves, replica wormholes, and quantum extremal surfaces. The external resource [adscft.org](https://adscft.org/) is the **primary text**; this course adds framing, notation alignment, and connections to the algebraic-QFT and quantum-information-in-QFT research programs at UERJ.

This course is **independent of** but cross-linked with the [[courses/ads-cft-course/syllabus|2026 Algebraic-QFT course]]. Students who have taken AQFT will find Sem II's modular-flow / type III₁ material familiar; students who have not will be given the minimum they need without operator-algebra prerequisites.

---

## 1. Course architecture

| | Semester I — Foundations | Semester II — Advanced Machinery & Black-Hole Information |
|---|---|---|
| **Format** | Formal lectures + problem sessions | Lectures + paper-reading seminars |
| **Hours/week** | 4 hr lectures + 1 hr problem session | 3 hr lectures + 1 hr seminar |
| **Anchor** | Modern CFT → AdS geometry & dictionary → working examples | Advanced AdS/CFT → black-hole information |
| **Primary reading** | adscft.org *Modern CFT* + *Foundations* tracks | adscft.org *Advanced* + *Black Hole Information* tracks |

The two semesters are designed to be taken in sequence; Semester II assumes Semester I.

---

## 2. Learning outcomes

A graduate of the course can:

1. State and use the basic AdS/CFT dictionary ([[gkp-witten-formula]]): compute boundary correlators from bulk classical fields and vice versa, in tractable examples.
2. Derive and apply the [[ryu-takayanagi-formula]] for entanglement entropy in a holographic CFT, including the covariant (HRT) generalisation.
3. Explain large-$N$ factorisation, the type III₁ structure of boundary single-trace algebras, and the sense in which "large $N$ = classical gravity."
4. State and motivate the [[quantum-extremal-surfaces]] prescription and the island formula; trace through a Page-curve calculation in JT gravity or in a soluble toy model.
5. Read the modern black-hole-information literature (Penington 2019; Almheiri–Engelhardt–Marolf–Maxfield 2019; Maldacena–Qi 2018; Gao–Jafferis–Wall) critically — identifying which steps are general, which are JT-specific, and which depend on holography.
6. Submit a 15–20 page final project: either a calculation (Sem I track) or a paper-reading writeup (Sem II track) — see master-project.

---

## 3. Semester I — Foundations (15 weeks)

### Block A (Wks 1–5) — Modern CFT — skeleton

The CFT prerequisites tailored for holography. (adscft.org *Modern CFT for AdS/CFT* §§3–10, selected — see the crosswalk for the per-week chapters.)

**Week 1 — Conformal algebra and primary operators.** ([[week-01-conformal-algebra-and-primaries|notes]])
The conformal generators and their geometric meaning; $\mathfrak{so}(d,2)$ and the embedding-space realisation; quasi-primary vs primary. *Derived:* the scalar two-point function from the Ward identities; the level-1 descendant norm and the unitarity bounds.

**Week 2 — Radial quantisation and the state–operator correspondence.** ([[week-02-radial-quantisation-and-state-operator|notes]])
Quantising on spheres; the dilatation operator as the Hamiltonian; the bijection between local operators and states; the conformal multiplet built by $P_\mu$ and $K_\mu$.

**Week 3 — OPE and conformal blocks.** ([[week-03-ope-and-conformal-blocks|notes]])
The OPE as a convergent expansion; conformal blocks as the resummation of a multiplet's contribution; crossing symmetry stated. Generalised free fields introduced here, and used again in Week 7.

**Week 4 — Stress tensor, central charge, conformal anomalies.** ([[week-04-stress-tensor-and-central-charge|notes]])
$T_{\mu\nu}$ and its Ward identities; the central charge in $d = 2$; the $a$ and $c$ anomaly coefficients in $d = 4$ — the quantities Week 9 reproduces holographically.

**Week 5 — 2d CFT essentials.** ([[week-05-2d-cft-essentials|notes]])
Virasoro; the Cardy formula; modular invariance of the torus partition function. The 2d results Weeks 12–13 and Sem II Wk 7 all cash in.

### Block B (Wks 6–10) — AdS geometry and the holographic dictionary — skeleton

(adscft.org *AdS/CFT Foundations* §§2–7.)

**Week 6 — AdS geometries: global, Poincaré, Euclidean.** ([[week-06-ads-geometries|notes]])
AdS as a hyperboloid; global, Poincaré and Euclidean coordinates and what each is good for; the conformal boundary; causal structure and the need for boundary conditions. *Derived:* the metric in each patch.

**Week 7 — Large-$N$ gauge theory and the 't Hooft limit.** ([[week-07-large-n-and-thooft-limit|notes]])
The 't Hooft limit and why it is the sensible one; single-trace operators; large-$N$ factorisation. *Derived:* the genus scaling $N^{2-2g}$ by double-line counting. Lands on the statement that the single-trace algebra is type III$_1$ at $N = \infty$ — the point of contact with the [[courses/ads-cft-course/syllabus|AQFT course]]'s Semester II.

**Week 8 — GKP–Witten formula and the operator–field dictionary.** ([[week-08-gkp-witten-formula|notes]])
The generating-functional identification $Z_{\rm CFT}[J] = Z_{\rm grav}[\phi_\partial = J]$; sources and vacuum expectation values; which bulk field is dual to which operator. *Derived:* the mass–dimension relation $\Delta(\Delta-d) = m^2L^2$ from the near-boundary equation of motion.

**Week 9 — Holographic renormalisation.** ([[week-09-holographic-renormalisation|notes]])
The Fefferman–Graham expansion; divergences of the on-shell action and the counterterms that remove them; the holographic stress tensor. *Derived:* the $d = 2$ Weyl anomaly $\langle T^\mu_{\ \mu}\rangle = \tfrac{c}{12}R$ with $c = 3L/2G_N$ — Brown–Henneaux from the bulk action.

**Week 10 — Bulk computations of CFT correlators.** ([[week-10-bulk-correlators|notes]])
Bulk-to-boundary propagators; two- and three-point functions from the bulk; where the contact terms go. The technology Sem II Wk 2 extends to exchange diagrams.

### Block C (Wks 11–15) — Working examples and probes — skeleton

(adscft.org *AdS/CFT Foundations* §§7–9, with *Black Hole Information* §§3–4 for Wks 14–15.)

**Week 11 — Wilson loops and the area-of-string prescription.** ([[week-11-wilson-loops|notes]])
The Maldacena–Rey–Yee prescription; the static quark–antiquark potential. *Derived:* the minimal-surface profile and $V(L) \propto -\sqrt\lambda/L$ — a genuinely strong-coupling answer with no weak-coupling counterpart.

**Week 12 — Finite temperature: AdS-Schwarzschild and Hawking–Page.** ([[week-12-finite-temperature-ads-schwarzschild|notes]])
The planar and global black holes; the Hawking–Page transition as confinement/deconfinement. *Derived:* the Hawking temperature $T_H = d\,r_h/4\pi L^2$ from Euclidean regularity.

**Week 13 — Holographic entanglement entropy: Ryu–Takayanagi.** ([[week-13-ryu-takayanagi|notes]])
The replica trick; the RT prescription; the interval in AdS$_3$ computed in full, reproducing the CFT$_2$ answer via Brown–Henneaux; strong subadditivity as a one-line geometry argument.

**Week 14 — HRT (covariant) and subregion–subalgebra duality.** ([[week-14-hrt-and-subregion-subalgebra|notes]])
Extremal rather than minimal surfaces; the reduction to RT in static bulks; entanglement wedges, reconstruction, and the quantum-error-correction reading; JLMS stated. The clearest meeting point with the AQFT course.

**Week 15 — JT gravity: the soluble laboratory.** ([[week-15-jt-gravity-intro|notes]])
Dilaton gravity in two dimensions; the Schwarzian boundary mode. *Derived:* the dilaton equation of motion freezing the bulk to AdS$_2$. The model Semester II uses whenever a calculation must actually close.

**Sem I master-project milestone.** A calculation-grade exercise — e.g. reproduce the holographic stress-tensor two-point function, or compute RT for a strip in AdS₃. See master-project.

---

## 4. Semester II — Advanced Machinery and Black-Hole Information (15 weeks)

### Block 1 (Wks 1–7) — Advanced AdS/CFT machinery — skeleton

(adscft.org *Advanced AdS/CFT* §§6, 12, 14, with *Black Hole Information* §§2, 4 for Wks 5–6 — those two weeks are served by the BHI track, not Advanced.)

**Week 1 — Holographic renormalisation in depth.** ([[sem2-week-01-holographic-renormalisation-in-depth|notes]])
The Fefferman–Graham expansion carried to higher orders; the $a$ and $c$ anomalies in $d = 4$; scheme independence of the renormalised action.

**Week 2 — Witten diagrams.** ([[sem2-week-02-witten-diagrams|notes]])
Contact and exchange diagrams; $D$-functions; the conformal-block decomposition of an exchange diagram, and what it says about the operator content of the dual.

**Week 3 — Modular flow on boundary subregions.** ([[sem2-week-03-modular-flow-on-subregions|notes]])
*Derived:* the Casini–Huerta–Myers ball modular Hamiltonian $K = 2\pi\!\int (R^2-r^2)/2R\;T_{00}$, with Bisognano–Wichmann recovered in the $R\to\infty$ limit. Then FLM and JLMS: modular flow as the bulk Killing flow of the entanglement wedge. This week and [[sem2-week-09-liu-type-iii-and-modular-geometry|AQFT Sem II Wk 9]] derive the same formula from the two sides; students taking both should compare them.

**Week 4 — The gravitational replica trick (Lewkowycz–Maldacena).** ([[sem2-week-04-replica-trick-in-gravity|notes]])
The conical-defect saddle and the analytic continuation in $n$. *Derived:* $S_A = \mathrm{Area}/4G_N$ in the $n\to1$ limit — RT from the gravitational path integral rather than as a postulate.

**Week 5 — Quantum extremal surfaces.** ([[sem2-week-05-quantum-extremal-surfaces|notes]])
Generalised entropy and why RT needs correcting; the FLM $1/N$ correction; the Engelhardt–Wall prescription. *Derived:* QES from the replica trick with bulk matter. The island formula is already implicit here.

**Week 6 — JT gravity revisited: the Page curve in a tractable model.** ([[sem2-week-06-jt-gravity-page-curve|notes]])
JT plus a bath; the QES computation at early and late times; the Page time $\sim S_0$. The first place the Page curve is obtained rather than argued for.

**Week 7 — AdS$_2$/CFT$_1$ and AdS$_3$/CFT$_2$ essentials.** ([[sem2-week-07-ads2-ads3-essentials|notes]])
*Derived:* the Brown–Henneaux central charge $c = 3\ell/2G_N$ from the asymptotic symmetry algebra. BTZ entropy against Cardy; the AdS$_2$/SYK symmetry-breaking pattern sketched.

### Block 2 (Wks 8–15) — Black-hole information — skeleton

(adscft.org *Black Hole Information* §§1, 4–6. Note Wk 13 has no counterpart on the site; see the crosswalk.)

**Week 8 — Hawking radiation and the information problem.** ([[sem2-week-08-hawking-radiation-info-problem|notes]])
The Hawking calculation and what it assumes; the monotonic entropy growth that follows; why this contradicts unitarity, stated precisely enough to be worth resolving.

**Week 9 — The Page curve.** ([[sem2-week-09-page-curve|notes]])
*Derived:* Page's average-entropy formula $\langle S_A\rangle \approx \log d_A - d_A/2d_B$. The curve unitarity requires, obtained from random-state typicality before any gravity is involved.

**Week 10 — Replica wormholes.** ([[sem2-week-10-replica-wormholes|notes]])
The new saddles of the replica path integral; how they take over after the Page time; the ensemble-averaging question they raise and the course's honest position on it.

**Week 11 — The island formula.** ([[sem2-week-11-island-formula|notes]])
Islands as the QES prescription applied to the radiation; the entropy of Hawking radiation recomputed; what an island means for locality and for bulk reconstruction.

**Week 12 — ER=EPR, TFD, and the eternal black hole.** ([[sem2-week-12-er-epr-and-tfd|notes]])
*Derived:* the two-sided modular Hamiltonian $K = \beta(H_R - H_L)$ from $\Delta = \rho_R\rho_L^{-1}$, with the modular flow identified as two-sided Schwarzschild time. The holographic face of [[sem2-week-05-tfd-and-two-sided-modular-structure|AQFT Sem II Wk 5]].

**Week 13 — Quantum focusing and ANEC.** ([[sem2-week-13-quantum-focusing-anec|notes]])
*Derived:* the Raychaudhuri equation and the classical focusing theorem from the null energy condition. Then the quantum focusing conjecture and the quantum null energy condition, stated with their status.

**Week 14 — Traversable wormholes: Gao–Jafferis–Wall.** ([[sem2-week-14-traversable-wormholes-gjw|notes]])
The double-trace deformation; negative averaged null energy and the opened throat; the teleportation reading; Maldacena–Qi sketched. Compare with [[sem2-week-14-msy-bulk-and-desitter-aside|AQFT Sem II Wk 14]], which reaches the same geometry from the algebra.

**Week 15 — Panoramic closing: where the field is going.** ([[sem2-week-15-panoramic-closing|notes]])
The two semesters as one argument; what is established, what is conjectural, and which threads are live. Final presentations.

**Sem II master-project milestone.** A paper-reading project — e.g. follow Penington 2019, or AEMM 2019, or Maldacena–Qi (SYK wormhole). See master-project.

---

## 5. Course materials

- **Conventions:** [[courses/ads-cft-course/conventions]] — notation, sign conventions, AdS-radius normalisation. Read before Week 1.
- **adscft.org crosswalk:** adscft-org-crosswalk — bidirectional map between course weeks and adscft.org chapters, rebuilt against the live site on 2026-08-25 and now carrying verified chapter numbers. Always cite weeks via this crosswalk; if the site reorganises, that appendix is the only file to update.
- **Bibliography & paper map:** bibliography-and-paper-map — paper-grade references for each block.
- **Master's project:** master-project — one document with both Sem I and Sem II milestones.
- **Note quality standard:** note-quality-template — the binding per-note bar. Note that it is deliberately *not* the algebraic-QFT course's standard: this course is a scaffold over adscft.org, so a note's job is to own what the site does not, and paraphrasing the primary text is the failure mode it guards against.
- **Notes upgrade plan:** notes-upgrade-plan — the diagnosis and per-note worklists for bringing the thirty first-draft notes to that standard. Semester I Block A is done; the remaining blocks follow on acceptance.

---

## 6. Relation to the 2026 Algebraic-QFT course

The 2026 AQFT course's Semester II covers Witten 2022, CPW, AAJ — papers that work with the type III₁ algebra of single-trace operators at large $N$. This course supplies the holographic side of that machinery. Students who have taken AQFT can skim Block A and Sem II Wks 1–3 of this course; students taking both in sequence get the algebraic side (AQFT) and the holographic side (this course) of the same modern story.

See in particular `wiki/courses/2026-algebraic-qft-course/appendices/holography-large-n-primer.md`, which is the AQFT-side primer that this course expands into a full curriculum.
