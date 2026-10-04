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
modified: 2026-10-04
---

# Generalized Symmetries and Topological Matter

*Written by AI assistants under the scientific and pedagogical supervision of Marcelo S. Guimarães; see [[ai-authorship]] for the division of labour and the models involved.*

**From Lattice Gauge Theory to Quantum Information**

A two-semester graduate course that starts from compact variables on a lattice and ends at the modern frontier: higher-form symmetries, 't Hooft anomalies, topological order, and non-invertible defects. Semester I builds the classic core — Kramers–Wannier, Wegner, Wilson, Kogut–Susskind, Polyakov, Fradkin–Shenker — with every duality derived on the lattice, in cochain language, with all the sums done. Semester II re-reads that material through Gaiotto–Kapustin–Seiberg–Willett and lands on Kitaev's toric code, Wen's string-nets, the modified Villain program, and condensation defects. The destination is deliberate: students finish able to read the current literature on higher gauging and defect condensation, which is where the group's [[julia-toulouse-mechanism|Julia–Toulouse]] research line now lives.

The course is the pedagogical arm of the [[confinement-duality]] area, with a second foot in [[condensed-matter-connections]]. It is independent of, but cross-linked with, the [[courses/2026-algebraic-qft-course/syllabus|2026 Algebraic-QFT course]] and the AdS/CFT course (see §9).

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
- Polyakov, *Gauge Fields and Strings*, ch. 4; and "Quark confinement and topology of gauge groups," Nucl. Phys. B 120 (1977) 429.
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

The full reading guide, with per-paper instructions, is [[courses/generalized-symmetries-course/appendices/bibliography-and-paper-map|bibliography-and-paper-map]]. Notation is fixed in [[courses/generalized-symmetries-course/conventions|conventions]] — read it before Week 1; the cochain conventions there are used in every problem set.

### Lecture notes

The lecture notes live in the courses repository (`generalized-symmetries/notes/`), which is the single source of truth for this course; the physics-wiki copy under `wiki/courses/generalized-symmetries-course/` is not updated automatically. They are committed as they are written and become a durable resource for future students and collaborators.

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
3. **Condensation defects in Z_N lattice gauge theory** — the seed of the companion master-project; feeds directly into the group's manuscript on higher-gauging walls.
4. **Critical exposition of one spine paper** — GKSW, GKKS, Levin–Wen, or Roumpedakis–Seifnashri–Shao, rewritten for a reader who knows only Semester I.

---

## 6. Semester I — Fundamentos na Rede (15 weeks)

### Block A: Compact fields and duality in two dimensions (Weeks 1–4) — skeleton

**Week 1 — Compact variables and their defects: the XY model.** ([[week-01-compact-variables-xy-model|notes]])
Why compactness is physical: phases, angles, superfluids. Periodic scalars on the lattice; spin-wave expansion and where it lies; winding numbers and π₁(U(1)) = ℤ; vortices as the first topological defects; Mermin–Wagner as a model proof and the stiffness picture; the O(2) rotor chain solved by the character expansion and the particle on a ring in its winding and momentum bases. *Problem set:* rotor-chain thermodynamics; finite-size scaling of the magnetization; higher-charge correlators; the dipole gas and the BKT criterion; ⋆ Villain versus cosine to order β⁻³; ⋆ twisted boundary conditions and the helicity modulus; ⋆⋆ the lattice constant κ.

**Week 2 — The lattice as a cell complex: chains, cochains, and duality.** ([[week-02-lattice-cell-complex-cochains|notes]])
The toolkit week; everything later stands on it. Hypercubic lattice as a cell complex; p-chains and p-cochains; boundary ∂ and coboundary d; discrete Stokes as a definition; H_p and H^p with ℤ, ℝ, ℤ_N coefficients computed by hand on T² and T³ with Smith normal forms; the codifferential, the Laplacian and the discrete Hodge decomposition; the dual lattice, the lattice Hodge map and Poincaré duality; Poisson resummation as the engine of every duality in this course; the intersection pairing and the clock–shift algebra; the cubical cup product. Taught operationally — no point-set topology, just finite linear algebra. *Problem set:* boundary matrices and homology of the 3×3 torus; cohomology of T³ and Poincaré duality; Laplacian zero modes; ⋆ torsion on the Klein bottle; ⋆ cup products by hand; ⋆ the self-dual degree in d = 4; ⋆ Poisson resummation in degree 2, the gauge-field Villain sum; ⋆⋆ Hodge theory with a metric.

**Week 3 — The Villain form and the exact duality of the XY model.** ([[week-03-villain-form-xy-duality|notes]])
Villain's periodic Gaussian: approximation of the cosine action, and exact starting point in its own right. The José–Kadanoff–Kirkpatrick–Nelson decomposition derived exactly with the Week-2 toolkit: the conserved-current model, the height (solid-on-solid) model with its winding sectors, and the second Poisson resummation that yields spin waves ⊗ a neutral vortex Coulomb gas with fugacity y = e^(−2π²βκ); the exact lattice identification of the Coulomb charges with the vorticity; the charge correlator through the duality; sine-Gordon to second order in the fugacity, in both directions. *Problem set:* the correlator through the duality, extended; anisotropic duality; vortex dressing of the spin correlator; ⋆ winding sectors and the helicity modulus; ⋆ multi-charge fugacities; ⋆ the duality with an external field; ⋆⋆ the ℤ_N clock model.

**Week 4 — BKT, Kramers–Wannier, and the first disorder operators.** ([[week-04-bkt-kramers-wannier-disorder|notes]])
The energy–entropy argument; the Kosterlitz flow derived at leading order with its constant 4π³, the essential singularity and the universal stiffness jump πβ_R = 2 (the bare critical coupling being model-dependent); Kramers–Wannier duality of the 2d Ising model in cochain language, with the four torus sectors and their exact transformation; Kadanoff–Ceva disorder spins μ and the order–disorder algebra; the σμ composite as a lattice fermion through Jordan–Wigner. Duality as a statement about a wall — the seed that grows into the non-invertible duality defect in Sem II Week 13, previewed here on the transfer matrix. *Problem set:* flow-diagram quantitative work; the jump from the helicity modulus; Kramers–Wannier with a magnetic field; the disorder correlator at criticality; ⋆ spin structures from the Jordan–Wigner string; ⋆ the defect commutes with the transfer matrix; ⋆⋆ the ℤ_N clock ladder; ⋆⋆ the Kosterlitz flow at next order.

### Block B: Lattice gauge theory — the classic core (Weeks 5–8) — skeleton

**Week 5 — Wegner's ℤ₂ gauge theory: phases without a local order parameter.** ([[week-05-wegner-z2-gauge-theory|notes]])
Gauging the Ising model by hand; Elitzur's theorem, proved; the Wilson loop as the surviving diagnostic; area law vs perimeter law; the duality of the 3d ℤ₂ gauge theory to the 3d Ising model, with the confined phase mapped to the ordered Ising phase (self-duality is the 4d statement). Wegner's discovery, stated in his own terms and ours: a phase transition with no symmetry-breaking order parameter — topological order before the name existed. *Problem set:* Elitzur's theorem for U(1) and any compact group; the string tension as an interface tension in d = 3; the next correction to the string tension and the first perimeter term; visons off the lattice axis; ⋆ testing a claim about ground states on the spatial torus; ⋆ Wegner's family M_dn; ⋆⋆ the duality as the gauging of a 1-form symmetry.

**Week 6 — Wilson's formulation: compact groups, Haar measure, strong coupling.** ([[week-06-wilson-action-strong-coupling|notes]])
Plaquette actions for U(1) and SU(N); Haar integration and the graded rules of the strong-coupling expansion; character expansions as the computational tool; leading-order area law and the string tension; corrections, and the roughening transition (mention); why Monte Carlo took over from there (mention, Creutz). *Problem set:* the 1×2 loop by hand; SU(2) class integrals and higher representations; character coefficients of ℤ_N; two dimensions, where the tiling is exact; ⋆ the adjoint loop and its screening; ⋆ the heat-kernel action and Casimir scaling; ⋆ the U(1) plaquette to ninth order; ⋆⋆ roughening from the strong-coupling side; ⋆⋆ charge-2 flux sheets in U(1).

**Week 7 — Kogut–Susskind: the Hamiltonian lattice.** ([[week-07-kogut-susskind-hamiltonian|notes]])
Transfer matrix → Hamiltonian limit, with the anisotropic couplings and the unit photon speed checked; link rotors and the electric basis (Peter–Weyl for U(1) and SU(2)); the Gauss law as an operator constraint and its physical projector; physical states as closed electric strings; strong-coupling spectrum: the string tension to second order and the glueball, whose hopping first appears at second order; the one-plaquette universe. The ℤ₂ Hamiltonian gauge theory in 2+1d and its duality to the transverse-field Ising model, with the confined phase ferromagnetic; the toric code as its Γ → 0 point with the Gauss law imposed energetically, planted here on purpose. *Problem set:* the SU(2) one-plaquette universe in the electric basis; the two-plaquette universe; charge-2 static sources; ⋆ the 2+1d U(1) theory in height variables; ⋆ the ℤ₂ gauge chain with matter; ⋆ the anisotropic tension and the Villain time step; ⋆⋆ the glueball in 3+1d; ⋆⋆ the one-plaquette instanton.

**Week 8 — Midterm + dual variables for abelian gauge theories.** ([[week-08-dual-variables-abelian-gauge|notes]])
In-class midterm (2 hr) on Weeks 1–7: dualities and strong-coupling computations. Then: the Villain gauge action with its compact measure; Dirac quantization; the current representation of U(1) gauge theory; the 3d duality to the dual photon σ ∼ σ + 2π with action (e²/8π²)(∂σ)², the monopoles appearing at the second Poisson resummation on dual sites; the 4d Banks–Myerson–Kogut duality with β̃ = 1/4π²β and conserved integer monopole currents on dual links; exact electric–magnetic identities at the Villain level. Bridge to Block C: in 3d the monopoles are instantons, and Polyakov is waiting. *Problem set:* a charge-q Wilson loop through the 3d duality; the ℤ_N gauge theory; the static monopole in 4d; ⋆ the BMK loop-gas free energy; ⋆ winding and flux sectors in d = 3; ⋆⋆ a self-dual abelian model.

### Block C: Monopoles, condensation, confinement (Weeks 9–12) — skeleton

**Week 9 — Compact QED₃ I: the monopole plasma.** ([[week-09-compact-qed3-monopole-plasma|notes]])
The exact dual photon of Week 8 in continuum form; the monopole as an instanton, seen in the flux jump across a time slice; the monopole action from the lattice Coulomb propagator, S_mono = 2π²G₃(0)β ≈ 4.99β; the fugacity expansion that turns Week 8's exact gas into a grand-canonical Coulomb gas with pair coefficient (4π²/e²) over unordered pairs; the three scales and the small parameter ζ/e⁶; the sine-Gordon theory with its vertex normalization, matched to the gas at O(ζ²); Debye–Hückel screening with m_D² = 8π²ζ/e². The magnetic symmetry of three-dimensional Maxwell theory is a 0-form U(1) whose charged objects are the local operators e^(iqσ): spontaneously broken without monopoles, with the photon as its Goldstone boson, and explicitly broken by them. The energy–entropy argument leaves no Coulomb phase at any coupling; the rigorous statements are cited. *Problem set:* the Debye cloud and its flux; order parameter, spontaneous and explicit breaking; the ℤ_N remnant of the magnetic symmetry; ⋆ beyond Debye–Hückel; ⋆ the symmetry operator in the plasma; ⋆⋆ monopoles with a Chern–Simons term.

**Week 10 — Compact QED₃ II: the mass gap and the area law.** ([[week-10-polyakov-mass-gap-area-law|notes]])
The central computational week of Semester I. The photon mass from both faces, sine-Gordon and Debye–Hückel, and the identity between the sine-Gordon saddle and the Poisson–Boltzmann equation of the plasma; the Wilson loop carried exactly through the duality, where it becomes a vortex line of σ and each monopole sees it through the solid angle; the smooth unwinding of the monodromy, the kink σ = 4 arctan e^(m_γξ), the Bogomolny bound and the tension σ_str = 2e²m_γ/π²; the area law, at the classical level and to leading order in (ζ/e⁶)^(1/2), with a lattice demonstration; charge-q loops, surface independence and the symmetry reading; the validity chain, set against Göpfert–Mack's theorem. *Problem set:* unscreened monopoles give a volume law; the wall between two loops; charge-2 probes; ⋆ a second harmonic and the first correction to the tension; ⋆ deconfinement from the dual photon; ⋆⋆ Göpfert–Mack against the semiclassics.

**Week 11 — Compact U(1) in 4d: monopole condensation and the dual superconductor.** ([[week-11-monopole-condensation-4d|notes]])
Monopole worldloops and their Dirac sheets; the action of one loop and the energy–entropy estimate of the transition; the Wilson loop in the loop gas, Guth's theorem and Fröhlich–Spencer, with a model bound; the 't Hooft loop as a twisted sheet, screened by the dynamical monopoles, and the equal-time algebra of Wilson and 't Hooft operators; the two phases read through their 1-form symmetries (Coulomb: both loops perimeter, electric U(1)⁽¹⁾ spontaneously broken; confined: Wilson area law, electric symmetry unbroken, magnetic symmetry explicitly broken). The [[dual-superconductor]] as an exact identity and as a dual Ginzburg–Landau model with the Bogomolny tension T = 2πv²|q|. First appearance of the [[julia-toulouse-mechanism]] in its original form (Julia–Toulouse; Quevedo–Trugenberger): when the Dirac sheets condense, the photon's two polarizations become the three of a massive Kalb–Ramond field, with three descriptions of one condensate and the area law of the Kalb–Ramond Wilson loop; the electric condensate of the group's papers is a different phase and is kept distinct. It returns in modern dress in Sem II Week 14. *Problem set:* a monopole core action and the dual stiffness; the magnetic flux loop at strong coupling; the static potential of the massive Kalb–Ramond theory; ⋆ type-I and type-II dual superconductors; ⋆ the Julia–Toulouse prescription in three dimensions; ⋆⋆ the ℤ_N remnant of a charge-N condensate.

**Week 12 — θ-terms, the Witten effect, and oblique responses.** ([[week-12-theta-terms-witten-effect|notes]])
The θ-term with one sign chain fixed at the start: S_θ = −(θ/4π²)∫E·B in Minkowski signature, the Euclidean weight e^(iθQ) with its orientation, and integrality (Q ∈ ½ℤ in general, ℤ on spin manifolds; a model proof on T⁴); the Witten effect from the θ-modified momentum and Gauss law, q_e = n_e + θn_m/2π, and spectral flow on the charge lattice. On the lattice: why the naive density fails; the Villain θ-term, written with the cubical cup product, integer on T⁴ without monopoles; the lattice Witten phase of a static monopole. SL(2,ℤ), the dyon self-energy and oblique confinement (Cardy–Rabinovici); varying θ: axion electrodynamics and the Hall conductivity (Δθ/2π)(e²/2π) of a θ-wall, with [[axionic-electrodynamics]] in topological insulators and Weyl semimetals, where the group's [[condensed-matter-connections]] line enters. Foreshadows the modified Villain program of Sem II Week 12. *Problem set:* dyon energies and their level crossings; the two-dimensional lattice θ-term; the θ = π slab; ⋆ the Witten effect from a collective coordinate; ⋆ SL(2,ℤ) orbit bookkeeping; ⋆ a moving lattice monopole; ⋆⋆ the axion response of a Weyl semimetal; ⋆⋆ the Witten effect for 't Hooft lines in the monopole-free theory.

### Block D: Matter fields and phase structure (Weeks 13–15) — skeleton

**Week 13 — Fradkin–Shenker I: gauge–Higgs systems.** ([[week-13-fradkin-shenker-gauge-higgs|notes]])
The ℤ₂ gauge–Higgs model: action, unitary gauge, Elitzur with matter, and Griffiths monotonicity with the perimeter bound ⟨W(C)⟩ ≥ (tanh κ)^|C|; the four edges of the (β, κ) diagram; strong coupling with matter boundaries and the self-duality in d = 3; string breaking, V = min(σR, 2E_M) with its avoided crossing. The analyticity argument of Osterwalder–Seiler and Fradkin–Shenker as a model proof: the polymer expansion converges at small β for every κ and at large κ for every β, and the union connects the Higgs and confinement regimes while excluding the free-charge corner. The phase diagram in d = 3: two continuous lines bounding the free-charge phase, a multicritical point, and a first-order segment ending at a critical endpoint, read through the liquid–gas analogy; continuity of the gauge-invariant spectrum between the two regimes; the toric code in two fields as the Hamiltonian face. *Problem set:* energy densities under the duality; string breaking at the next order; the open Wilson line and the Fredenhagen–Marcu ratio; ⋆ testing a claim about the 1-form symmetry generator with matter; ⋆ the e–m duality of the Hamiltonian; ⋆⋆ the U(1) diagram with charge-1 and charge-q matter in d = 4; ⋆⋆ scaling at the critical endpoint; ⋆⋆ correlator interpolation along the complementarity path.

**Week 14 — Fradkin–Shenker II: order parameters beyond Landau.** ([[week-14-fradkin-shenker-order-parameters|notes]])
ℤ_N gauge theory with charge-q matter and its four edges; the residual 1-form symmetry ℤ_r⁽¹⁾, r = gcd(N, q), from one change of variables, with the annihilator exact sequence and the worked case N = 6, q = 4, where the symmetry elements form the subgroup Ann(H) and the charges modulo screening the quotient ℤ_N/H. With charge-1 matter the area-law and symmetry criteria fail together; for r > 1 the realization of the residual symmetry distinguishes phases. The Polyakov loop and the center symmetry at finite temperature, the correlator at strong coupling, and the explicit and residual center breaking by charged matter; Svetitsky–Yaffe at model level, with the exact reduction at β_s = 0 and the universality statement conditional on a continuous transition; 't Hooft's electric and magnetic flux sectors on T³ at the soluble points and with charge-q matter; the ground-state degeneracy r² of the deconfined corner on T²; a superconductor is topologically ordered (Hansson–Oganesyan–Sondhi), derived from the charge-2 model and its residual ℤ₂⁽¹⁾. The question the classics leave open is answered in part; gauging and the rest wait for Sem II. *Problem set:* the case N = 4; Polyakov loops with charge-2 matter in ℤ₄; the 't Hooft spectrum with charge-q matter; ⋆ Svetitsky–Yaffe in 2+1 dimensions; ⋆ the superconductor in 3+1 dimensions; ⋆⋆ the screening data of a charge-k condensate, assembled for the comparison with gauging.

**Week 15 — Consolidation: everything was symmetry all along.** ([[week-15-semester-i-consolidation|notes]])
The definitions of Gaiotto–Kapustin–Seiberg–Willett stated precisely (form degree, topological operators and charged objects, explicit breaking and emergence, the SSB criterion for p ≥ 1 with its counterterm, the higher-form Coleman–Mermin–Wagner bound, twists as symmetry operators) and applied to the semester: a translation exercise on Wegner's ℤ₂ theory (the linking identity of the closed sheet, the torus algebra and its four ground states, visons as endpoints of open sheets); every Semester I duality as Poisson resummation, with the symmetries it exchanges; every criterion and where it fails; the realization of every Semester I symmetry by phase, with Wilson, 't Hooft and Polyakov loops as charged objects; the course map. **Take-home final** assigned (20%, due two weeks later): five problems of 20 points with sub-parts and a diagnostic map back to the notes (one engine and two Villain chains, with twists as symmetry operators; string breaking in the ℤ₂ gauge–Higgs model; a Polyakov estimate and the energy–entropy balance; the Kramers–Wannier operator on the periodic chain, which prefigures Sem II Week 13; ⋆ the residual 1-form symmetry of ℤ_N gauge theory with charge-q matter). Core track Problems 1–4, starred track all five; the solution key and rubric belong to the assessment package. *Problem set:* translate the two-dimensional Ising model; translate compact QED₄ at θ ≠ 0; a form-degree drill; ⋆ translate the four-dimensional ℤ₂ gauge theory; ⋆ the noncontractible symmetry operator as a diagnostic; ⋆⋆ the toric code in two fields, translated.

---

## 7. Semester II — Simetrias Generalizadas e Matéria Topológica (15 weeks)

Lectures carry the spine; the weekly seminar hour is for students presenting assigned sections of the primary papers, with the instructor filling gaps. Blocks 1–4 contain five **mini-calculations** (Weeks 4, 6, 9, 11 and 13), fully explicit computations students hand in, in the spirit of the AQFT course's mini-calculations; Block 5 has none, since its weeks carry the write-up.

### How a typical seminar hour runs

The presenter states the paper's technical claim, identifies what it needs from Semester I, and reproduces one nontrivial step at the board. Discussion follows; the instructor closes by placing the result on the course map. The first seminar of each block is presented by the instructor as a model.

### Block 1 — Generalized global symmetries (Weeks 1–4) — skeleton

*Spine: Gaiotto–Kapustin–Seiberg–Willett.*

**Week 1 — Symmetries are topological operators.** ([[sem2-week-01-symmetries-are-topological-operators|notes]])
From Noether currents to topological operators: the Ward identity with its contact term, the finite operator as a twist with its counterterm, and the compact scalar as the model; p-form symmetries and their p-dimensional charged objects; why higher-form symmetry groups are abelian, by the codimension-2 move; Maxwell theory as the master example, with the electric and magnetic 1-form symmetries generated by ⋆F/e² and F/2π and the Euclidean factors of i fixed once. The linking action of U_α(Σ) on W(C) computed on the lattice, through the intersection pairing and the Hodge map of Sem I Week 2, and in the continuum, through the equal-time commutator with ∮⋆F, with the orientations that make both +1. Back-reading Semester I: the magnetic 0-form symmetry of compact QED₃ (Wk 9), the twisted sheets of compact QED₄ (Wk 11) and center symmetry (Wk 14) were generalized symmetries all along. Seminar (presented by the instructor as the model for the block): GKSW §§2–3 and 4.1. *Mini-step:* the action of U_α(Σ) on W(C) by linking, computed on the lattice and in the continuum.

**Week 2 — ℤ_N gauge theory as BF theory: the universal topological skeleton.** ([[sem2-week-02-zn-gauge-theory-as-bf-theory|notes]])
ℤ_N gauge theory at zero coupling and its continuum BF presentation (iN/2π)∫b∧da, with the integrality of N; the electric and magnetic ℤ_N^(1) symmetries, generated by the lines of b and of a; canonical quantization on T² with the bracket fixed by the action and the orientation, the clock–shift algebra of the holonomies and GSD = N², then N^(2g) on Σ_g; braiding from linking in spacetime; the lattice dictionary in both directions (the ℤ_N Villain theory flows to BF at large β, the cup product is the dual-lattice pairing, the GLSS presentation); the degeneracy derived as a spontaneously broken 1-form symmetry. Seminar: Kitaev's toric code (quant-ph/9707021 §§2–4), the Kogut–Susskind ℤ₂ theory of Sem I Week 7 now named. *Mini-step:* GSD = N^(2g) on the genus-g surface from the symmetry algebra on H₁(Σ_g, ℤ_N) with its intersection pairing.

**Week 3 — Spontaneous breaking of higher-form symmetries: the Landau paradigm regained.** ([[sem2-week-03-spontaneous-breaking-of-higher-form-symmetries|notes]])
Order parameters for 1-form symmetries made precise: a perimeter law up to a local counterterm, the counterterm as the self-energy of the probe, and the corners that no local term removes; the photon as the Goldstone boson of a spontaneously broken 1-form symmetry, from the broken-symmetry Ward identity and its massless pole, with a model proof in free Maxwell theory (in compact QED₄ the Coulomb photon is the Goldstone boson of the exact electric symmetry, the magnetic one being only emergent); the higher-form Coleman–Mermin–Wagner bound from the infrared integral, for continuous and discrete groups; the superconductor in the Villain abelian-Higgs model, where charge-q matter breaks the electric U(1)^(1) explicitly to ℤ_q^(1) and the Higgs phase breaks ℤ_q^(1) spontaneously, with ℤ₂ topological order at q = 2 (Hansson–Oganesyan–Sondhi), the magnetic symmetry being exact and unbroken only without monopoles; confinement as the *unbroken* electric 1-form symmetry, for pure gauge theory or center-neutral matter. Every Semester I phase justified row by row against the table of Sem I Week 15. Seminar: Hansson–Oganesyan–Sondhi. *Mini-step:* the Goldstone commutator for the dual photon; the Meissner effect from the Villain abelian-Higgs action.

**Week 4 — Gauging: backgrounds, orbifolds, and the quantum dual symmetry.** ([[sem2-week-04-gauging-backgrounds-and-dual-symmetry|notes]])
Background fields for discrete p-form symmetries as cocycle insertions; gauging as a normalized sum over backgrounds, with the prefactors that make it invertible on tori; the transverse-field Ising chain gauged operator by operator, the dual ℤ₂ as a holonomy, and the Kramers–Wannier operator built from the gauging maps, with every matrix of a three-site chain displayed; the ℤ_N^(p) → ℤ_N^(d−p−2) rule from counting backgrounds and the cup pairing; Kramers–Wannier on the torus as gauging; subgroup gauging with the annihilator sequence of Sem I Week 14, and fractional charge in the ℤ₄ chain; SU(N) vs SU(N)/ℤ_N and the line-operator spectrum (Aharony–Seiberg–Tachikawa: the continuum statement cited, a ℤ_N lattice toy worked, and the count of global forms). Seminar: Aharony–Seiberg–Tachikawa. **Mini-calculation 1:** gauge the ℤ₂ symmetry of the transverse-field Ising chain by an explicit cocycle sum, exhibit the dual ℤ₂, and identify Kramers–Wannier as gauging; then the same one dimension up, for the 1-form symmetry of ℤ₂ gauge theory, whose gauging returns the transverse-field Ising model. **Write-up topics due.**

### Block 2 — 't Hooft anomalies and SPT phases (Weeks 5–7) — skeleton

*Spine: Gaiotto–Kapustin–Komargodski–Seiberg; Chen–Gu–Liu–Wen.*

**Week 5 — 't Hooft anomalies: obstruction as physics.** ([[sem2-week-05-thooft-anomalies-obstruction-as-physics|notes]])
Anomalies as background-field phases that no local counterterm removes; anomaly matching, with 't Hooft's spectator argument; inflow, with the cluster chain as the example: its symmetry acts projectively on each edge, and the bulk response cancels the edge phase. The discrete entry point, kept finite-dimensional: projective ℤ₂×ℤ₂ quantum mechanics and H²(ℤ₂×ℤ₂, U(1)) = ℤ₂; Lieb–Schultz–Mattis as a lattice mixed anomaly between translation and the internal U(1), through Oshikawa's flux threading, with every operator written on a small ring: anomalies live inside ordinary spin chains, not only in chiral gauge theories. Seminar (presented by the instructor as the model for the block): Oshikawa (2000). *Mini-step:* the sign cocycle of the projective ℤ₂×ℤ₂ algebra; Oshikawa's flux-threading argument on a small ring, explicitly.

**Week 6 — Mixed higher-form anomalies: Yang–Mills at θ = π.** ([[sem2-week-06-mixed-anomalies-yang-mills-at-theta-pi|notes]])
GKKS: the mixed anomaly between the ℤ_N 1-form center symmetry and time reversal at θ = π. The twisted SU(2) bundle on T⁴ built explicitly, with 't Hooft's twist matrices and a half-instanton; the fractional instanton number (N−1)/2N ∫𝒫(B) from a U(N) lift; on the lattice, the higher cup product ∪₁ and the Pontryagin square, the cup product earning its keep. The anomaly phase under θ → θ + 2π, the counterterms, and the consequence: for even N no trivially gapped, T-symmetric, confining vacuum at θ = π; the allowed scenarios and the large-N branch check. Seminar: Gaiotto–Kapustin–Komargodski–Seiberg. *Mini-calculation 2:* the anomaly phase under θ → θ + 2π with the background B turned on, tracking the Pontryagin square; the N = 2 case fully explicit.

**Week 7 — SPT phases, group cohomology, Dijkgraaf–Witten.** ([[sem2-week-07-spt-phases-group-cohomology-dijkgraaf-witten|notes]])
Symmetry-protected phases: trivial bulk, protected edge; the Haldane chain and AKLT as the physical example; classification by group cohomology (Chen–Gu–Liu–Wen), with the 1d case derived from matrix-product states, where the symmetry acts projectively on the virtual space, and higher d stated; H³(ℤ₂, U(1)) = ℤ₂ computed; cocycle models and Dijkgraaf–Witten theories as gauged SPTs, with the two ℤ₂ theories in 2+1d built on the cubic lattice; the cluster state as a ℤ₂×ℤ₂ SPT and its measurement-based-computation reading (mention). Seminar: Levin–Gu, the π-flux statistics of the gauged ℤ₂ SPT. *Mini-step:* the AKLT edge doublet from the MPS transfer matrix; the two ℤ₂ Dijkgraaf–Witten theories in 2+1d — toric code and double semion — distinguished by anyon self-statistics.

### Block 3 — Topological order and quantum information (Weeks 8–11) — skeleton

*Spine: Kitaev; Levin–Wen.*

**Week 8 — The toric code, solved to the bone.** ([[sem2-week-08-toric-code-solved-to-the-bone|notes]])
Stabilizer formalism from scratch; the ground space on Σ_g and its 2^(2g) dimensions; e, m, ε anyons; string operators, braiding, fusion; the spectrum of anyon pairs. Then the identification that organizes everything: the toric code *is* the deconfined phase of ℤ₂ gauge theory, and the perturbed toric code *is* the Fradkin–Shenker diagram (Trebst et al.; Tupitsyn et al.) — Semester I Week 13, seen from the quantum-information side, with both regimes read as anyon condensations (e in the Higgs regime, m in the confined one). Seminar (presented by the instructor as the model for the block): Kitaev (1997). *Mini-step:* the full stabilizer solution; S and T matrices from the string-operator algebra.

**Week 9 — Long-range entanglement and error correction.** ([[sem2-week-09-long-range-entanglement-and-error-correction|notes]])
Chen–Gu–Wen: phases as equivalence classes under local unitary circuits; long-range vs short-range entanglement as the sharp version of "topological order"; topological entanglement entropy (Kitaev–Preskill and Levin–Wen constructions, both); the code-theoretic reading: logical operators as homology classes, code distance, why no local operator distinguishes ground states — degeneracy that is also a quantum memory (Dennis–Kitaev–Landahl–Preskill), with the planar code, its rough and smooth boundaries, and decoding mapped onto the random-bond Ising model on the Nishimori line. Seminar: Kitaev–Preskill and Levin–Wen. **Mini-calculation 3:** topological entanglement entropy of the toric code by explicit Schmidt decomposition of a disk bipartition, γ = ln 2; code distance on the L×L torus.

**Week 10 — The zoo beyond ℤ₂: quantum doubles, modular data, Chern–Simons.** ([[sem2-week-10-beyond-z2-quantum-doubles-modular-data-chern-simons|notes]])
Kitaev's quantum double D(G) in outline; non-abelian anyons for G = S₃ (statement level); modular S and T matrices as the fingerprint of a topological order; abelian Chern–Simons and the K-matrix description; edge modes and bulk–boundary correspondence (chiral boson sketch); the fractional quantum Hall effect in one honest lecture: Laughlin ν = 1/3, its anyons, its threefold degeneracy, with the signs of the course's orientation (the mirror of the common −K/4π convention). Seminar: Wen–Niu; reading on the Hall level and the emergent field: Witten (2026), §§3–4. *Mini-step:* GSD, spins, and mutual statistics from the K-matrix for ν = 1/3 and for the toric code; match the Week 8 answers.

**Week 11 — String-net condensation: Wen's mechanism for emergent gauge fields.** ([[sem2-week-11-string-net-condensation|notes]])
Levin–Wen input data — fusion rules and F-symbols — presented operationally, category theory kept offstage; the string-net Hamiltonian on the honeycomb lattice; the toric code as the ℤ₂ string-net; the doubled Ising phase (statement); "whence gauge theory": deconfined phases as condensates of electric strings, closing the loop with Kogut–Susskind Week 7. Seminar: Levin–Wen. *Mini-calculation 4:* verify the pentagon identity for the ℤ₂ F-symbols; the ground state as an equal-weight loop gas; the perimeter law of ⟨W⟩ evaluated inside the wavefunction.

### Block 4 — The modern lattice synthesis (Weeks 12–13) — skeleton

*Spine: Gorantla–Lam–Seiberg–Shao; Shao's TASI lectures.*

**Week 12 — Modified Villain: exact dualities and exact higher-form symmetries on the lattice.** ([[sem2-week-12-modified-villain|notes]])
The Sulejmanpasic–Gattringer construction and the GLSS systematics: promote the Villain integer to a ℤ gauge field with its own flatness constraint; compact QED without monopoles; exact self-duality of the 2d XY model and of 4d Maxwell; exact θ-periodicity and well-defined lattice θ-terms (repairing Sem I Week 12); exact discrete backgrounds and anomalies without a continuum limit. The Semester I dualities (JKKN, BMK) re-derived as exact statements. Seminar (presented by the instructor as the model for the block): Gorantla–Lam–Seiberg–Shao. *Mini-step:* modified-Villain XY duality with every boundary term tracked; the exact ℤ_N 1-form background coupling in 4d Villain Maxwell.

**Week 13 — Non-invertible symmetries: duality defects and condensation defects.** ([[sem2-week-13-non-invertible-symmetries|notes]])
Kramers–Wannier as a topological defect line: the Aasen–Mong–Fendley lattice construction; the fusion D × D̄ = 1 + η, twice the projector onto the ℤ₂-even sector, hence no inverse; half-space gauging as the general mechanism; higher gauging (gauging on a submanifold) and condensation defects (Roumpedakis–Seifnashri–Shao); duality defects in 3+1d at the self-dual point (Choi–Córdova–Hsin–Lam–Shao; Kaidi–Ohmori–Zheng, statement level). The general lesson, closing the arc from Sem I Week 4: every duality of this course is an operator inside the theory. Seminar: Aasen–Mong–Fendley. **Mini-calculation 5:** the Ising duality defect on the transfer matrix; verify the projector fusion and the fusion with the Kadanoff–Ceva disorder line.

### Block 5 — Condensation as gauging: the research frontier (Weeks 14–15) — skeleton

**Week 14 — Defect condensation and the Julia–Toulouse mechanism in modern dress.** (notes)
The [[julia-toulouse-mechanism|Julia–Toulouse approach]] (Quevedo–Trugenberger; the group's 2009–2013 series) read as a weighted defect ensemble, whose proliferation is entropy against activation. The higher-gauging wall of four-dimensional ℤ_N gauge theory built in the course's language: its charge filter (a charge-q Wilson line crosses intact iff q ∈ Ann(H)), the wall on a time slice as a projector, the fusion D_H × D̄_H = D_H from the ensemble sum, and bulk against hypersurface condensation formula by formula; in 2+1d, a charge-k condensate restricted to a surface reproduces the condensation sheet of Week 13 in its London limit. Then the group's manuscript in preparation: the lines that complete Wilson–wall junctions carry a finite cost, an exact character transform maps them to a ℤ_N′ clock model, a junction pair is a charged clock correlator, and at large cost the tension per unit cost tends to ᾱ/2 because currents split into unit strands; charge-selective screening and the conditional matching to a Villain regulator. The novelty boundary as the manuscript states it. Seminar: open-problems session led by the instructor, twelve problems marked M.Sc.- or Ph.D.-scale (among them fractons via GLSS, non-abelian condensates and measurement-based realizations of gauging). *Problem set:* walls in ℤ₁₂ gauge theory; the N′ = 3 and N′ = 4 walls as spin models; the clock chain; the time-slice wall for N = 4, k = 2; ⋆ legs and charges; ⋆ charge-selective screening; ⋆ finite-group Villain self-duality; ⋆⋆ partial order at N′ = 4; ⋆⋆ a microscopic interface in 2+1 dimensions.
*The notes of this week are not on the public site until the group's manuscript is public.*

**Week 15 — Write-up presentations and panoramic closing.** ([[sem2-week-15-presentations-and-panoramic-closing|notes]])
Student talks (20 min each) on the final write-ups, each with one calculation reproduced at the board and the four questions every seminar presenter answered. Closing lecture: one continuous story from Kramers–Wannier 1941 to condensation defects, told entirely with operators supported on closed submanifolds — dualities, symmetries, anomalies, and phases as one subject — in nine stations, each naming the week that derived it; the four threads drawn against the thirty weeks; the reading list for after the course. Where each open thread lives on the wiki, and which can become theses. *Problem set:* the degree rule along the story; three fusions, one mechanism; your write-up on the map; ⋆ the cohomology thread; ⋆ exact, emergent, explicit; ⋆⋆ from the write-up to a project.

---

## 8. Recurring threads across the course

Four threads run through both semesters and are flagged at each occurrence:

1. **Duality is Poisson resummation.** From the XY model (Sem I Wk 3) through Banks–Myerson–Kogut (Wk 8, used in Wk 11) to the modified Villain program (Sem II Wk 12), every duality in the course is one manipulation, done with increasing care.
2. **Symmetries live on topological operators.** Kadanoff–Ceva disorder lines (Sem I Wk 4) → Wilson, 't Hooft, and Polyakov loops (Wks 5–14) → GKSW symmetry surfaces (Sem II Wk 1) → non-invertible duality defects (Wk 13).
3. **Condensation changes the theory.** Vortex unbinding (BKT), monopole plasmas (Polyakov), Higgs condensation (Fradkin–Shenker), anyon and string-net condensation (Wen), and defect condensation as higher gauging (Julia–Toulouse, Wk 14). This thread ends at the group's active research line.
4. **Cohomology is the bookkeeping.** Cell complexes and Poincaré duality (Sem I Wk 2) → flux sectors and ground-state degeneracy (Sem II Wk 2) → group cohomology and SPTs (Wk 7) → cup products and anomalies (Wk 6) → higher gauging on submanifolds (Wks 13–14).

---

## 9. Relation to the other courses and to the group's research

**AQFT course.** Independent; the shared sensibility is "symmetries and phases read off from the operator content, not from a Lagrangian." Students who took AQFT will recognize the style of argument in Sem II Block 1; disorder operators and superselection sectors give the two courses a common vocabulary.

**AdS/CFT course.** Independent; the natural contact points are Wilson loops, center symmetry and deconfinement at finite temperature, and 1-form symmetries of line-operator spectra — the holographic reading of material this course develops on the lattice.

**Research program.** Semester II Block 5 lands, by construction, on the group's current manuscript (finite-cost currents at higher-gauging walls in four-dimensional ℤ_N gauge theory, with the Julia–Toulouse ensemble as the motivation for the line weight). The companion master-project turns that landing into an M.Sc. thesis path, and write-up topic 3 is its on-ramp. The course as a whole is the pedagogical arm of [[confinement-duality]], with [[condensed-matter-connections]] re-entering through axionic electrodynamics (Sem I Wk 12) and topological matter (Sem II Block 3).

---

## 10. Connection to the wiki

Each lecture creates or updates a wiki page. The Semester I toolkit and classic-duality concepts are [[lattice-gauge-theory]], [[wilson-loop]], [[villain-action]], and [[kramers-wannier-duality]]; the Semester II generalized-symmetry and topological-order concepts are [[higher-form-symmetries]], [[t-hooft-anomaly]], [[spt-phases]], [[topological-order]], [[toric-code]], [[string-net-condensation]], and [[condensation-defects]] — the last being the anchor for the group's manuscript on higher-gauging walls and the companion master-project. Lecture notes accumulate under `wiki/courses/generalized-symmetries-course/notes/` and become a durable resource.

Build phasing follows the AdS/CFT precedent: **Phase 1** (scaffold: syllabus, [[courses/generalized-symmetries-course/conventions|conventions]], master-project, [[courses/generalized-symmetries-course/appendices/bibliography-and-paper-map|bibliography-and-paper-map]]), **Phase 2** (done: the nine block skeletons under `skeletons/`, the eleven concept pages above, and the [[cochain-calculus-survival-kit]] appendix), **Phase 3** (weekly notes under `notes/`; Semester I first drafts written 2026-07-01, judged too superficial on review). **Phase 3-R** (complete for the notes): every note was rewritten to the standard of the note-quality-template, per the notes-upgrade-plan: complete inline derivations, fine-print and misconception sections, figures, route sections and answer checkpoints. Block A was rewritten on 2026-07-10; on 2026-09-27 the course was reviewed against the algebraic-QFT course, the template was reconciled with that standard, `conventions.md` was completed, and Block A was corrected; on 2026-09-28 Block B was rewritten, and both blocks were verified independently (`reviews/2026-09-27-comprehensive-review.md`, `reviews/2026-09-28-implementation-audit.md`, plan Part VII); on 2026-09-28/29 Blocks C–D were rewritten and verified in the same way (`reviews/2026-09-29-implementation-audit.md`), which completes Semester I; on 2026-10-01/02 the two assessment packages and Semester II Block 1 followed (`reviews/2026-10-02-implementation-audit.md`). Block 2 followed the same day (`reviews/2026-10-02-semester-II-block-2-audit.md`). Block 3 followed on 2026-10-03 (`reviews/2026-10-03-semester-II-block-3-audit.md`). Block 4 followed the same day (`reviews/2026-10-03-semester-II-block-4-audit.md`), and Block 5 closed Semester II on 2026-10-03 (`reviews/2026-10-03-semester-II-block-5-audit.md`). Every note of the course is now written to the reconciled template, and on 2026-10-04 the dossier was assembled into a book draft (`book/`), in an instructor's edition and a public one without Sem II Week 14 and the assessments.

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
- A direct path into the group's research: the manuscript on higher-gauging walls, the master-project, and the open-problems list of Week 14.

The course also serves the instructor's own program: it rebuilds the [[confinement-duality]] line's foundations in the modern language the current manuscript speaks, and it trains the students who can join that line.

---

*Plan committed 2026-07-01. Phase 1 scaffold; to be revised after skeletons are drafted and again after the first run.*
