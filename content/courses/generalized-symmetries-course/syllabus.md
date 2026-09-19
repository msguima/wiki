---
title: "Generalized Symmetries and Topological Matter: From Lattice Gauge Theory to Quantum Information"
type: course
instructor: Marcelo S. Guimarães
institution: UERJ — Departamento de Física Teórica
duration: two semesters (~30 weeks)
audience: M.Sc. and Ph.D. students; open to qualified outsiders
prerequisites: Quantum mechanics; statistical mechanics (partition functions, transfer matrices, Ising model); one semester of QFT (path integrals, canonical quantization, abelian gauge fields)
not assumed: algebraic topology, lattice field theory, conformal field theory, category theory, condensed-matter theory, quantum information
language: lectures in Portuguese; written materials in English
modified: 2026-07-01
---

# Generalized Symmetries and Topological Matter

*Written by AI assistants under the scientific and pedagogical supervision of Marcelo S. Guimarães; see ai-authorship for the division of labour and the models involved.*

**From Lattice Gauge Theory to Quantum Information**

A two-semester graduate course that starts from compact variables on a lattice and ends at the modern frontier: higher-form symmetries, 't Hooft anomalies, topological order, and non-invertible defects. Semester I builds the classic core — Kramers–Wannier, Wegner, Wilson, Kogut–Susskind, Polyakov, Fradkin–Shenker — with every duality derived on the lattice, in cochain language, with all the sums done. Semester II re-reads that material through Gaiotto–Kapustin–Seiberg–Willett and lands on Kitaev's toric code, Wen's string-nets, the modified Villain program, and condensation defects. The destination is deliberate: students finish able to read the current literature on higher gauging and defect condensation, which is where the group's [[julia-toulouse-mechanism|Julia–Toulouse]] research line now lives.

The course is the pedagogical arm of the [[confinement-duality]] area, with a second foot in [[condensed-matter-connections]]. It is independent of, but cross-linked with, the [[courses/generalized-symmetries-course/syllabus|2026 Algebraic-QFT course]] and the AdS/CFT course (see §9).

---

## 1. Course architecture

| | Semester I — Fundamentos na Rede | Semester II — Simetrias Generalizadas e Matéria Topológica |
|---|---|---|
| **Format** | Formal lectures | Lectures + reading seminar |
| **Hours/week** | 4 hr lectures + problem sets | 3 hr lectures + 1 hr seminar |
| **Mode** | Instructor-led | Instructor-led with student presentations |
| **Anchor** | Compact scalars → lattice gauge theory → monopoles and confinement → gauge–Higgs phase diagrams | GKSW → anomalies and SPTs → toric code and string-nets → modified Villain → condensation defects |

The semesters run in sequence; Semester II assumes Semester I as a hard prerequisite. A student with prior lattice-gauge-theory background may petition to enter Semester II directly, but the cochain toolkit of Sem I Week 2 is used everywhere and must be absorbed first.

---

## 2. Learning outcomes

A graduate of the course can:

1. Compute with the lattice cochain calculus: p-form fields as p-cochains, boundary and coboundary operators, dual lattice, homology and cohomology of the torus, Poisson resummation — and use it to execute abelian dualities exactly in the Villain form.
2. Reproduce the classic results with full derivations: Kramers–Wannier duality, the vortex Coulomb gas and BKT transition of the XY model, the strong-coupling area law, Polyakov's mass gap and permanent confinement in compact QED₃, and the Fradkin–Shenker phase diagram.
3. Identify the p-form symmetries of a given theory, the extended operators they act on, and how each symmetry is realized (unbroken, spontaneously broken, explicitly broken, gauged) — and use that data to classify phases where Landau order parameters fail.
4. Detect and match 't Hooft anomalies, including mixed anomalies with higher-form symmetries (Yang–Mills at θ = π) and their lattice avatars (Lieb–Schultz–Mattis); explain anomaly inflow and the SPT/boundary correspondence.
5. Solve the toric code completely — ground-state degeneracy, anyons, braiding, topological entanglement entropy, code distance — and place it inside the string-net framework and inside the Fradkin–Shenker diagram.
6. Read the current literature critically (GKSW; Gaiotto–Kapustin–Komargodski–Seiberg; Levin–Wen; Gorantla–Lam–Seiberg–Shao; Roumpedakis–Seifnashri–Shao) and produce a 15–20 page write-up on one technical topic.

---

## 3. Audience and prerequisites

**Assumed:** Graduate quantum mechanics; statistical mechanics including transfer matrices and the 2d Ising model; one semester of QFT (path integrals, canonical quantization, abelian gauge invariance). Comfort with Fourier analysis.

**Not assumed:** Algebraic topology (built operationally in Week 2), lattice field theory, CFT, category theory (F-symbols enter operationally in Sem II Week 11), condensed-matter background, quantum information (stabilizers built from scratch in Sem II Week 8).

**Audience:** Mixed M.Sc. and Ph.D. students at UERJ, open to qualified outsiders — the course is designed to be readable from three directions (hep-th, condensed matter, quantum information), and the problem sets carry a **core track** (everyone) and a **starred track** (Ph.D. students and the ambitious). The quantum-information weeks (Sem II Block 3) are pitched to be accessible to collaborators from the condensed-matter and quantum-information side, including [[itzhak-roditi|Roditi]]'s circle at CBPF.

---

## 4. Materials

### Primary texts (Semester I)

- Kogut, "An introduction to lattice gauge theory and spin systems," Rev. Mod. Phys. 51 (1979) 659.
- Savit, "Duality in field theory and statistical systems," Rev. Mod. Phys. 52 (1980) 453.
- Fradkin & Shenker, "Phase diagrams of lattice gauge theories with Higgs fields," Phys. Rev. D 19 (1979) 3682.
- Polyakov, *Gauge Fields and Strings*, ch. 4; and "Quark confinement and topology of gauge theories," Nucl. Phys. B 120 (1977) 429.
- Tong, *Lectures on Gauge Theory* (lattice chapter) and *Lectures on Statistical Field Theory* (BKT chapter) — the pedagogical companion when the original papers are terse.

### Primary texts (Semester II)

- Gaiotto, Kapustin, Seiberg, Willett, "Generalized global symmetries," JHEP 02 (2015) 172 [arXiv:1412.5148]. *(The spine of Block 1.)*
- Gaiotto, Kapustin, Komargodski, Seiberg, "Theta, time reversal, and temperature," JHEP 05 (2017) 091 [arXiv:1703.00501]. *(The spine of Block 2.)*
- Kitaev, "Fault-tolerant quantum computation by anyons," Annals Phys. 303 (2003) 2 [quant-ph/9707021]; Levin & Wen, "String-net condensation," Phys. Rev. B 71 (2005) 045110 [cond-mat/0404617]. *(The spine of Block 3.)*
- Gorantla, Lam, Seiberg, Shao, "A modified Villain formulation of fractons and other exotic theories," J. Math. Phys. 62 (2021) 102301 [arXiv:2103.01257]; Sulejmanpasic & Gattringer, Nucl. Phys. B 943 (2019) 114616 [arXiv:1901.02637]. *(The spine of Block 4.)*
- Roumpedakis, Seifnashri, Shao, "Higher gauging and non-invertible condensation defects," Commun. Math. Phys. 401 (2023) 3043 [arXiv:2204.02407]. *(The spine of Block 5.)*
- McGreevy, "Generalized symmetries in condensed matter," Ann. Rev. Cond. Mat. Phys. 14 (2023) [arXiv:2204.03045] and Shao, "What's done cannot be undone: TASI lectures on non-invertible symmetries," arXiv:2308.00747 — the two reviews students keep open all semester.

### Reference works

- Fradkin, *Field Theories of Condensed Matter Physics*, 2nd ed., CUP, 2013.
- Wen, *Quantum Field Theory of Many-Body Systems*, OUP, 2004.
- Zeng, Chen, Zhou, Wen, *Quantum Information Meets Quantum Matter*, Springer, 2019.
- Nakahara, *Geometry, Topology and Physics*, 2nd ed. (homology/cohomology chapters, as backup for Week 2).
- Preskill, *Lecture Notes on Quantum Computation*, ch. 9 (topological quantum computation).

The full reading guide, with per-paper instructions, is bibliography-and-paper-map. Notation is fixed in [[courses/generalized-symmetries-course/conventions]] — read it before Week 1; the cochain conventions there are used in every problem set.

### Lecture notes

All lecture notes will be hosted under `wiki/courses/generalized-symmetries-course/notes/`, committed weekly, and become a durable resource for future students and collaborators.

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
| Seminar presentation + participation | 40% | continuous |
| Final write-up draft (≥10 pp, feedback only) | 0% | end of Week 10 |
| Final write-up revision (≥15 pp) | 60% | end of Week 14 |
| Oral presentation of write-up | included in 60% | Week 15 |

Students propose a write-up topic by end of Week 4 of Semester II. Suggested topics:

1. **Polyakov confinement, retold** — a self-contained exposition of the compact-QED₃ mass gap with modern commentary: which higher-form symmetry is explicitly broken by monopoles, and what the modified Villain version restores.
2. **The Fradkin–Shenker diagram from the toric-code side** — the perturbed toric code as the quantum-information reading of the gauge–Higgs phase diagram (Trebst et al.; Tupitsyn et al.).
3. **Condensation defects in Z_N lattice gauge theory** — the seed of the companion master-project; feeds directly into the group's Julia–Toulouse/higher-gauging manuscript.
4. **Critical exposition of one spine paper** — GKSW, GKKS, Levin–Wen, or Roumpedakis–Seifnashri–Shao, rewritten for a reader who knows only Semester I.

---

## 6. Semester I — Fundamentos na Rede (15 weeks)

### Block A: Compact fields and duality in two dimensions (Weeks 1–4) — skeleton

**Week 1 — Compact variables and their defects: the XY model.** ([[week-01-compact-variables-xy-model|notes]])
Why compactness is physical: phases, angles, superfluids. Periodic scalars on the lattice; spin-wave expansion and where it lies; winding numbers and π₁(U(1)) = ℤ; vortices as the first topological defects; Mermin–Wagner (stated) and the stiffness picture. *Problem set:* transfer matrix of the O(2) rotor chain via Bessel functions (character expansion warm-up); winding decomposition of the partition function of a particle on a ring; the power-law spin-wave correlator.

**Week 2 — The lattice as a cell complex: chains, cochains, and duality.** ([[week-02-lattice-cell-complex-cochains|notes]])
The toolkit week; everything later stands on it. Hypercubic lattice as a cell complex; p-chains and p-cochains; boundary ∂ and coboundary d; discrete Stokes as a definition; H_p and H^p with ℤ, ℝ, ℤ_N coefficients computed by hand on T² and T³; the dual lattice and Poincaré duality; Poisson resummation as the engine of every duality in this course. Taught operationally — no point-set topology, just finite linear algebra. *Problem set:* compute H^p(T³, ℤ) from the cell complex; verify the codifferential identity on the dual lattice; Poisson-resum the periodic Gaussian; rewrite a Villain sum as a dual-lattice integer sum.

**Week 3 — The Villain form and the exact duality of the XY model.** ([[week-03-villain-form-xy-duality|notes]])
Villain's periodic Gaussian: approximation of the cosine action, and exact starting point in its own right. The José–Kadanoff–Kirkpatrick–Nelson decomposition: spin waves ⊗ vortex Coulomb gas, derived line by line with the Week-2 toolkit; the electromagnetic dictionary for the 2d Coulomb gas; sine-Gordon as the fugacity expansion. *Problem set:* the full Villain-XY → Coulomb-gas derivation (guided, multi-part); vortex–vortex interaction from the lattice propagator; charge correlators in the dual frame.

**Week 4 — BKT, Kramers–Wannier, and the first disorder operators.** ([[week-04-bkt-kramers-wannier-disorder|notes]])
The energy–entropy argument; BKT flow and the universal stiffness jump (stated, with the RG sketch); Kramers–Wannier duality of the 2d Ising model in cochain language; Kadanoff–Ceva disorder spins μ and the order–disorder algebra; the σμ composite as a lattice fermion (mention). Duality as a statement about a wall — the seed that grows into the non-invertible duality defect in Sem II Week 13. *Problem set:* Kramers–Wannier with boundary conditions tracked honestly; T_c from self-duality; the μμ correlator at high temperature; ⋆ spin structures and the σμ fermion.

### Block B: Lattice gauge theory — the classic core (Weeks 5–8) — skeleton

**Week 5 — Wegner's ℤ₂ gauge theory: phases without a local order parameter.** ([[week-05-wegner-z2-gauge-theory|notes]])
Gauging the Ising model by hand; Elitzur's theorem, proved; the Wilson loop as the surviving diagnostic; area law vs perimeter law; self-duality of the 3d ℤ₂ gauge theory and its map to the 3d Ising model. Wegner's discovery, stated in his own terms and ours: a phase transition with no symmetry-breaking order parameter — topological order before the name existed. *Problem set:* prove Elitzur's theorem for ℤ₂; strong- and weak-coupling expansions of ⟨W(C)⟩ in 3d; the duality map to the dual-lattice Ising model.

**Week 6 — Wilson's formulation: compact groups, Haar measure, strong coupling.** ([[week-06-wilson-action-strong-coupling|notes]])
Plaquette actions for U(1) and SU(N); Haar integration and the graded rules of the strong-coupling expansion; character expansions as the computational tool; leading-order area law and the string tension; corrections, and the roughening transition (mention); why Monte Carlo took over from there (mention, Creutz). *Problem set:* one-link Haar integrals for U(1) and SU(2); leading strong-coupling string tension for both; first correction to the area law; character coefficients for ℤ_N, U(1), SU(2).

**Week 7 — Kogut–Susskind: the Hamiltonian lattice.** ([[week-07-kogut-susskind-hamiltonian|notes]])
Transfer matrix → Hamiltonian limit; link rotors and the electric basis; the Gauss law as an operator constraint; physical states as closed electric strings; strong-coupling spectrum: flux strings and the glueball estimate. The ℤ₂ Hamiltonian gauge theory written out in full — the toric code Hamiltonian, one renaming away, planted here on purpose. *Problem set:* derive H_KS from the anisotropic transfer matrix; the one-plaquette universe for ℤ₂ and U(1); flux-string energetics; ⋆ the ℤ₂ gauge chain ↔ transverse-field Ising duality.

**Week 8 — Midterm + dual variables for abelian gauge theories.** ([[week-08-dual-variables-abelian-gauge|notes]])
In-class midterm (2 hr): dualities and strong-coupling computations. Then: current representations; Poisson resummation of U(1) gauge theories in 3d and 4d; where the monopoles live on the dual lattice; the Villain gauge action as the natural home of exact duality. Bridge to Block C: in 3d the monopoles are instantons, and Polyakov is waiting.

### Block C: Monopoles, condensation, confinement (Weeks 9–12) — skeleton

**Week 9 — Compact QED₃ I: the monopole plasma.** ([[week-09-compact-qed3-monopole-plasma|notes]])
Compact U(1) in 3d, Villain form; exact duality to the integer-height field; monopoles as instantons; the dilute gas becomes a Coulomb gas of magnetic charges; the dual photon as a periodic scalar and the magnetic shift symmetry it carries. Stated plainly and returned to in Sem II: the monopoles *explicitly* break that magnetic symmetry, and the would-be Goldstone — the photon — is gapped by it. *Problem set:* monopole action from the lattice Coulomb propagator; the monopole–antimonopole interaction; the sine-Gordon effective action; identify the magnetic symmetry current and its charged operators.

**Week 10 — Compact QED₃ II: the mass gap and the area law.** ([[week-10-polyakov-mass-gap-area-law|notes]])
The central computational week of Semester I, mirroring Polyakov 1977 step by step: Debye screening in the monopole plasma; the photon mass m ∝ e^(−S_mono/2); the Wilson loop as a domain wall of the dual scalar; the soap-film argument and the area law; permanent confinement at all couplings in 3d. *Problem set:* the full Polyakov calculation, guided in parts, every constant tracked; the string tension vs mass gap relation; ⋆ finite-temperature deconfinement as a BKT transition of the dual scalar.

**Week 11 — Compact U(1) in 4d: monopole condensation and the dual superconductor.** ([[week-11-monopole-condensation-4d|notes]])
Monopole worldlines; the energy–entropy argument for loops; the confinement–Coulomb transition (Banks–Myerson–Kogut; Guth's proof that the Coulomb phase exists); 't Hooft loops and disorder operators; the [[dual-superconductor]] picture of Nambu, Mandelstam, and 't Hooft. First appearance of the [[julia-toulouse-mechanism]] in its original form (Quevedo–Trugenberger): when a defect ensemble condenses, the low-energy field content changes rank. It returns in modern dress in Sem II Week 14. *Problem set:* worldline representation of monopole currents; the BMK dual form of 4d Villain U(1); lattice Dirac quantization from the cochain pairing.

**Week 12 — θ-terms, the Witten effect, and oblique responses.** ([[week-12-theta-terms-witten-effect|notes]])
Why the naive lattice θ-term fails and what the Villain/cochain formulation repairs (foreshadowing the modified Villain program of Sem II Week 12); the Witten effect: dyons carry electric charge θ/2π; θ-periodicity and spectral flow; Cardy–Rabinovici and oblique confinement (sketch); [[axionic-electrodynamics]] and its condensed-matter realization — the group's [[condensed-matter-connections]] line enters here. *Problem set:* the Witten effect from the θ-modified Gauss law; dyon spectral flow under θ → θ + 2π; ⋆ the SL(2,ℤ) action on the charge lattice.

### Block D: Matter fields and phase structure (Weeks 13–15) — skeleton

**Week 13 — Fradkin–Shenker I: gauge–Higgs systems.** ([[week-13-fradkin-shenker-gauge-higgs|notes]])
Adding matter; fundamental vs higher representations; unitary gauge and what remains of Elitzur; the phase diagram of ℤ₂ gauge theory + Ising matter in 3d; the complementarity theorem: Higgs and confinement analytically connected for fundamental matter; string breaking and the failure of the Wilson criterion with dynamical charges. *Problem set:* small-β and small-κ expansions of the Fradkin–Shenker model; perimeter law everywhere with fundamental matter; transition lines at strong coupling.

**Week 14 — Fradkin–Shenker II: order parameters beyond Landau.** ([[week-14-fradkin-shenker-order-parameters|notes]])
Center-neutral matter and the survival of center symmetry; Polyakov loops and finite-temperature deconfinement; 't Hooft's electric and magnetic flux classification (Nucl. Phys. B 138); the honest question the classics leave open — which corners of the diagram are genuinely distinct phases, and distinguished by *what*? Sem II answers with symmetry realization; the deconfined corner turns out to be topologically ordered. *Problem set:* ℤ_N gauge theory with charge-q matter: for which q does a global symmetry acting on Wilson loops survive?; the Polyakov-loop correlator at strong coupling; ⋆ 't Hooft flux sectors on T³.

**Week 15 — Consolidation: everything was symmetry all along.** ([[week-15-semester-i-consolidation|notes]])
Panoramic re-derivation: every Sem I duality and criterion restated as a property of operators supported on closed loops and surfaces; the catalogue of places where Landau order parameters failed us. **Take-home final** assigned: 4–5 multi-part problems spanning the semester (a Villain duality chain; a strong-coupling Wilson loop with matter; a Polyakov-style estimate; a Kramers–Wannier-with-defect problem that prefigures Sem II Week 13).

---

## 7. Semester II — Simetrias Generalizadas e Matéria Topológica (15 weeks)

Lectures carry the spine; the weekly seminar hour is for students presenting assigned sections of the primary papers, with the instructor filling gaps. Each block ends in a **mini-calculation** — a fully explicit computation students hand in, in the spirit of the AQFT course's mini-calculations.

### How a typical seminar hour runs

The presenter states the paper's technical claim, identifies what it needs from Semester I, and reproduces one nontrivial step at the board. Discussion follows; the instructor closes by placing the result on the course map. The first seminar of each block is presented by the instructor as a model.

### Block 1 — Generalized global symmetries (Weeks 1–4) — skeleton

*Spine: Gaiotto–Kapustin–Seiberg–Willett.*

**Week 1 — Symmetries are topological operators.**
From Noether currents to codimension-1 topological surfaces; the reframing that defines the modern subject. p-form symmetries and their p-dimensional charged objects; why higher-form symmetry groups are abelian; Maxwell theory as the master example: electric and magnetic 1-form symmetries with currents F and ⋆F; Wilson and 't Hooft lines as the charged operators. Back-reading Semester I: the magnetic shift symmetry of compact QED₃ (Wk 9) and center symmetry (Wk 14) were higher-form symmetries all along. *Mini-step:* the action of U_α(Σ) on W(C) by linking, computed on the lattice and in the continuum.

**Week 2 — ℤ_N gauge theory as BF theory: the universal topological skeleton.**
ℤ_N gauge theory at zero coupling; the continuum BF presentation; electric and magnetic symmetries and their mutual braiding; ground-state degeneracy on the torus from the clock–shift algebra of symmetry operators wrapping cycles — degeneracy as spontaneously broken 1-form symmetry. Seminar: the Kogut–Susskind ℤ₂ theory of Sem I Week 7, now named: the toric code. *Mini-step:* GSD = N^(2g) on the genus-g surface from the symmetry algebra on H₁(Σ_g, ℤ_N) with its intersection pairing.

**Week 3 — Spontaneous breaking of higher-form symmetries: the Landau paradigm regained.**
Order parameters for 1-form symmetries: perimeter vs area law, stated with care; the photon as the Goldstone boson of the broken magnetic 1-form symmetry; the superconductor re-read (Higgsed EM as broken/gauged 1-form symmetry, with a ℤ₂ topologically ordered remnant — Hansson–Oganesyan–Sondhi); confinement as the *unbroken* electric 1-form symmetry; Coleman–Mermin–Wagner for p-form symmetries (statement and heuristic). Every phase from Semester I re-classified by symmetry realization. *Mini-step:* the Goldstone commutator for the dual photon; the Meissner effect from the Villain abelian-Higgs action.

**Week 4 — Gauging: backgrounds, orbifolds, and the quantum dual symmetry.**
Background fields for discrete p-form symmetries as cocycle insertions; gauging as summing over backgrounds; the dual ("quantum") symmetry of the gauged theory and the ℤ_N^(p) → ℤ_N^(d−p−2) rule; gauging subgroups; SU(N) vs SU(N)/ℤ_N and the line-operator spectrum (Aharony–Seiberg–Tachikawa, statement plus the ℤ_N lattice toy version). **Mini-calculation 1:** gauge the ℤ₂ symmetry of the transverse-field Ising chain by an explicit cocycle sum, exhibit the dual ℤ₂, and identify Kramers–Wannier as gauging; then the same one dimension up, for the 1-form symmetry of ℤ₂ gauge theory. **Write-up topics due.**

### Block 2 — 't Hooft anomalies and SPT phases (Weeks 5–7) — skeleton

*Spine: Gaiotto–Kapustin–Komargodski–Seiberg; Chen–Gu–Liu–Wen.*

**Week 5 — 't Hooft anomalies: obstruction as physics.**
Anomalies as background-field phases that no local counterterm removes; anomaly matching; inflow: the anomalous theory as the boundary of a bulk SPT in one dimension higher. The discrete entry point, kept finite-dimensional: projective representations as anomalous ℤ₂×ℤ₂ quantum mechanics; Lieb–Schultz–Mattis as a lattice mixed anomaly between translation and internal symmetry — anomalies live inside ordinary spin chains, not only in chiral gauge theories. *Mini-step:* the sign cocycle of the projective ℤ₂×ℤ₂ algebra; Oshikawa's flux-threading argument on a small ring, explicitly.

**Week 6 — Mixed higher-form anomalies: Yang–Mills at θ = π.**
GKKS: the mixed anomaly between the ℤ_N 1-form center symmetry and time reversal at θ = π; the consequence: no trivially gapped, T-symmetric, confining vacuum there; the allowed phase-diagram scenarios and the large-N check. On the lattice: where the anomaly sits in the cochain formulation — fractional instanton number in the presence of a 2-form background, and the cup product earning its keep. *Mini-calculation 2:* the anomaly phase under θ → θ + 2π with background B∪B turned on; the N = 2 case fully explicit.

**Week 7 — SPT phases, group cohomology, Dijkgraaf–Witten.**
Symmetry-protected phases: trivial bulk, protected edge; the Haldane chain and AKLT as the physical example; classification by group cohomology (Chen–Gu–Liu–Wen; the 1d case derived, higher d stated); Dijkgraaf–Witten theories as gauged SPTs; the cluster state as a ℤ₂×ℤ₂ SPT and its measurement-based-computation reading (mention). *Mini-step:* the AKLT edge doublet from the MPS transfer matrix; the two ℤ₂ Dijkgraaf–Witten theories in 2+1d — toric code and double semion — distinguished by anyon self-statistics.

### Block 3 — Topological order and quantum information (Weeks 8–11) — skeleton

*Spine: Kitaev; Levin–Wen.*

**Week 8 — The toric code, solved to the bone.**
Stabilizer formalism from scratch; the ground space on Σ_g and its 2^(2g) dimensions; e, m, ε anyons; string operators, braiding, fusion; the spectrum of anyon pairs. Then the identification that organizes everything: the toric code *is* the deconfined phase of ℤ₂ gauge theory, and the perturbed toric code *is* the Fradkin–Shenker diagram (Trebst et al.; Tupitsyn et al.) — Semester I Week 13, seen from the quantum-information side. *Mini-step:* the full stabilizer solution; S and T matrices from the string-operator algebra.

**Week 9 — Long-range entanglement and error correction.**
Chen–Gu–Wen: phases as equivalence classes under local unitary circuits; long-range vs short-range entanglement as the sharp version of "topological order"; topological entanglement entropy (Kitaev–Preskill and Levin–Wen constructions, both); the code-theoretic reading: logical operators as homology classes, code distance, why no local operator distinguishes ground states — degeneracy that is also a quantum memory (Dennis–Kitaev–Landahl–Preskill). **Mini-calculation 3:** topological entanglement entropy of the toric code by explicit Schmidt decomposition of a disk bipartition, γ = ln 2; code distance on the L×L torus.

**Week 10 — The zoo beyond ℤ₂: quantum doubles, modular data, Chern–Simons.**
Kitaev's quantum double D(G) in outline; non-abelian anyons for G = S₃ (statement level); modular S and T matrices as the fingerprint of a topological order; abelian Chern–Simons and the K-matrix description; edge modes and bulk–boundary correspondence (chiral boson sketch); the fractional quantum Hall effect in one honest lecture: Laughlin ν = 1/3, its anyons, its threefold degeneracy. *Mini-step:* GSD, spins, and mutual statistics from the K-matrix for ν = 1/3 and for the toric code; match the Week 8 answers.

**Week 11 — String-net condensation: Wen's mechanism for emergent gauge fields.**
Levin–Wen input data — fusion rules and F-symbols — presented operationally, category theory kept offstage; the string-net Hamiltonian on the honeycomb lattice; the toric code as the ℤ₂ string-net; the doubled Ising phase (statement); "whence gauge theory": deconfined phases as condensates of electric strings, closing the loop with Kogut–Susskind Week 7. *Mini-calculation 4:* verify the pentagon identity for the ℤ₂ F-symbols; the ground state as an equal-weight loop gas; the perimeter law of ⟨W⟩ evaluated inside the wavefunction.

### Block 4 — The modern lattice synthesis (Weeks 12–13) — skeleton

*Spine: Gorantla–Lam–Seiberg–Shao; Shao's TASI lectures.*

**Week 12 — Modified Villain: exact dualities and exact higher-form symmetries on the lattice.**
The Sulejmanpasic–Gattringer construction and the GLSS systematics: promote the Villain integer to a ℤ gauge field with its own flatness constraint; compact QED without monopoles; exact self-duality of the 2d XY model and of 4d Maxwell; exact θ-periodicity and well-defined lattice θ-terms (repairing Sem I Week 12); exact discrete backgrounds and anomalies without a continuum limit. The Semester I dualities (JKKN, BMK) re-derived as exact statements. *Mini-step:* modified-Villain XY duality with every boundary term tracked; the exact ℤ_N 1-form background coupling in 4d Villain Maxwell.

**Week 13 — Non-invertible symmetries: duality defects and condensation defects.**
Kramers–Wannier as a topological defect line: the Aasen–Mong–Fendley lattice construction; the fusion D × D̄ = 1 + η — a projector, hence no inverse; half-space gauging as the general mechanism; higher gauging (gauging on a submanifold) and condensation defects (Roumpedakis–Seifnashri–Shao); duality defects in 3+1d at the self-dual point (Choi–Córdova–Hsin–Lam–Shao; Kaidi–Ohmori–Zheng, statement level). The general lesson, closing the arc from Sem I Week 4: every duality of this course is an operator inside the theory. **Mini-calculation 5:** the Ising duality defect on the transfer matrix; verify the projector fusion and the fusion with the Kadanoff–Ceva disorder line.

### Block 5 — Condensation as gauging: the research frontier (Weeks 14–15) — skeleton

**Week 14 — Defect condensation and the Julia–Toulouse mechanism in modern dress.**
The [[julia-toulouse-mechanism|Julia–Toulouse approach]] (Quevedo–Trugenberger; the group's 2009–2013 series): condensation of a defect ensemble as a rank-changing transition. The modern re-reading, following the group's current manuscript: the restricted Villain defect ensemble of a charge-k condensate *constructively realizes* subgroup higher gauging — residual symmetry, condensation wall, projector fusion, and the endpoint rules for Wilson lines crossing the wall. Bulk versus hypersurface condensation. What the students can now read: the condensation-defect literature, and the group's manuscript itself. Seminar: open-problems session (fractons via GLSS; non-abelian condensates; measurement-based realizations of gauging).

**Week 15 — Write-up presentations and panoramic closing.**
Student talks (20 min each) on the final write-ups. Closing lecture: one continuous story from Kramers–Wannier 1941 to condensation defects, told entirely with operators supported on closed submanifolds — dualities, symmetries, anomalies, and phases as one subject. Where each open thread lives on the wiki, and which can become theses.

---

## 8. Recurring threads across the course

Four threads run through both semesters and are flagged at each occurrence:

1. **Duality is Poisson resummation.** From the XY model (Sem I Wk 3) through Banks–Myerson–Kogut (Wk 11) to the modified Villain program (Sem II Wk 12), every duality in the course is one manipulation, done with increasing care.
2. **Symmetries live on topological operators.** Kadanoff–Ceva disorder lines (Sem I Wk 4) → Wilson, 't Hooft, and Polyakov loops (Wks 5–14) → GKSW symmetry surfaces (Sem II Wk 1) → non-invertible duality defects (Wk 13).
3. **Condensation changes the theory.** Vortex unbinding (BKT), monopole plasmas (Polyakov), Higgs condensation (Fradkin–Shenker), anyon and string-net condensation (Wen), and defect condensation as higher gauging (Julia–Toulouse, Wk 14). This thread ends at the group's active research line.
4. **Cohomology is the bookkeeping.** Cell complexes and Poincaré duality (Sem I Wk 2) → flux sectors and ground-state degeneracy (Sem II Wk 2) → group cohomology and SPTs (Wk 7) → cup products and anomalies (Wk 6) → higher gauging on submanifolds (Wks 13–14).

---

## 9. Relation to the other courses and to the group's research

**AQFT course.** Independent; the shared sensibility is "symmetries and phases read off from the operator content, not from a Lagrangian." Students who took AQFT will recognize the style of argument in Sem II Block 1; disorder operators and superselection sectors give the two courses a common vocabulary.

**AdS/CFT course.** Independent; the natural contact points are Wilson loops, center symmetry and deconfinement at finite temperature, and 1-form symmetries of line-operator spectra — the holographic reading of material this course develops on the lattice.

**Research program.** Semester II Block 5 lands, by construction, on the group's current manuscript (Julia–Toulouse condensation as a constructive Villain realization of finite higher gauging). The companion master-project turns that landing into an M.Sc. thesis path, and write-up topic 3 is its on-ramp. The course as a whole is the pedagogical arm of [[confinement-duality]], with [[condensed-matter-connections]] re-entering through axionic electrodynamics (Sem I Wk 12) and topological matter (Sem II Block 3).

---

## 10. Connection to the wiki

Each lecture creates or updates a wiki page. The Semester I toolkit and classic-duality concepts are [[lattice-gauge-theory]], [[wilson-loop]], [[villain-action]], and [[kramers-wannier-duality]]; the Semester II generalized-symmetry and topological-order concepts are [[higher-form-symmetries]], [[t-hooft-anomaly]], [[spt-phases]], [[topological-order]], [[toric-code]], [[string-net-condensation]], and [[condensation-defects]] — the last being the anchor for the group's Julia–Toulouse manuscript and the companion master-project. Lecture notes accumulate under `wiki/courses/generalized-symmetries-course/notes/` and become a durable resource.

Build phasing follows the AdS/CFT precedent: **Phase 1** (scaffold: syllabus, [[courses/generalized-symmetries-course/conventions]], master-project, bibliography-and-paper-map), **Phase 2** (done: the nine block skeletons under `skeletons/`, the eleven concept pages above, and the [[cochain-calculus-survival-kit]] appendix), **Phase 3** (weekly notes under `notes/`; Semester I first drafts written 2026-07-01, judged too superficial on review). **Phase 3-R** (active): every note is being rewritten to the standard of the note-quality-template, per the notes-upgrade-plan — comprehensive inline derivations, fine-print and misconception sections, figures, and a physical-insight floor; Semester II notes will be written directly to that standard.

---

## 11. Risks and contingencies

| Risk | Likelihood | Mitigation |
|---|---|---|
| The Week-2 cochain toolkit intimidates students | Likely | Keep it operational (finite linear algebra on T² and T³); survival-kit appendix in Phase 2; the toolkit pays off visibly within one week (Wk 3 duality). |
| Scope explosion — the field is enormous | Certain, if unmanaged | Hold the spine: one target paper per Sem II block; everything else is starred or statement-level. Fractons, non-abelian condensates, and categorical machinery are explicitly out of scope. |
| Heterogeneous audience (hep-th / cond-mat / quant-info) | Likely | Three-entry design: every block has at least one anchor from each community; problem sets carry core + starred tracks. |
| Instructor's distance from quantum-information practice | Possible | Preskill ch. 9 and Zeng et al. as the guide; the toric-code weeks are self-contained stabilizer algebra, built from the ground up. |
| Sem II seminar uneven | Possible | Instructor models the first seminar of each block (same device as the AQFT course). |
| Low enrollment (3–5 students) | Likely | Fine for a topics course; the seminar hour works better small. |

---

## 12. Outcomes

By the end of the two semesters, students will have:

- A working lattice-duality toolkit (cochains, Villain forms, Poisson resummation) that they have used, not just seen.
- The classic literature — Wegner, Wilson, Kogut–Susskind, Polyakov, Fradkin–Shenker — read with every central calculation reproduced.
- The generalized-symmetry language at working fluency: p-form symmetries, gauging, anomalies, and the extended-operator reading of phases.
- The toric code, string-nets, and topological entanglement entropy computed from scratch, with the quantum-error-correction reading attached.
- A 15–20 page write-up on one technical topic, presentable as a seminar.
- A direct path into the group's research: the Julia–Toulouse/higher-gauging manuscript, the master-project, and the open-problems list of Week 14.

The course also serves the instructor's own program: it rebuilds the [[confinement-duality]] line's foundations in the modern language the current manuscript speaks, and it trains the students who can join that line.

---

*Plan committed 2026-07-01. Phase 1 scaffold; to be revised after skeletons are drafted and again after the first run.*
