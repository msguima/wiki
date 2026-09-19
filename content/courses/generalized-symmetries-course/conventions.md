---
title: "Course Conventions"
type: course-note
course: syllabus
modified: 2026-07-01
---

# Conventions

Notation for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]]. Read before Week 1; the cochain conventions below appear in every problem set. Where a sign or normalization is not fixed here, we follow Gorantla–Lam–Seiberg–Shao (arXiv:2103.01257) and, for cup products, Chen–Tata (arXiv:2106.05274); lecture notes say "convention fixed here" at first use when they need something beyond this file.

**Course-local override.** In this course, lowercase *d* is the **Euclidean spacetime dimension** (lattice-literature convention), so a d-dimensional theory has d−1 spatial directions in its Hamiltonian presentation. This differs from the wiki-wide default (d = spatial, D = d+1); the wiki playbook flags the symbol as context-dependent, and this file is the context.

---

## 1. Lattice and cell complex

- Hypercubic lattice Λ ⊂ ℤ^d, spacing a = 1 unless dimensional analysis is the point. Euclidean signature throughout Semester I; Hamiltonian (continuous-time) presentations name their spatial lattice explicitly.
- Cells: sites = 0-cells, links = 1-cells, plaquettes = 2-cells, cubes = 3-cells; all cells carry a fixed orientation (links point in +μ̂, plaquettes oriented by (μ̂, ν̂) with μ < ν).
- p-chains: formal integer combinations of p-cells; boundary operator ∂ with ∂² = 0.
- p-cochains with coefficients in an abelian group G: C^p(Λ, G), i.e. G-valued functions on oriented p-cells. Coboundary d defined by (df)(c) = f(∂c); d² = 0. This *is* the discrete Stokes theorem — by definition, not by theorem.
- Cohomology H^p(Λ, G) = ker d / im d on the relevant complex; on the torus T^d computed by hand in Week 2. Coefficients used in the course: ℤ, ℝ, U(1), ℤ_N.

## 2. Dual lattice

- Dual lattice Λ*: p-cell of Λ ↔ (d−p)-cell of Λ*, with orientation conventions (and the resulting signs in δ = ±⋆d⋆) taken from GLSS.
- Poincaré duality H^p(Λ) ≅ H_{d−p}(Λ) is used freely after Week 2.
- The duality "move" of the course is always the same pair: (i) Poisson resummation of an integer cochain, (ii) solving the resulting constraint on the dual lattice.

**Poisson resummation** (the engine, memorize the abelian form):
Σ_{n∈ℤ} f(n) = Σ_{w∈ℤ} ∫ dx f(x) e^{2πiwx}.

## 3. Compact fields and Villain actions

- Compact scalar: θ ∈ (−π, π] on sites, U(1) link field U_ℓ = e^{iθ_ℓ}.
- Villain action, scalar: S = (β/2) Σ_ℓ (dθ − 2πn)² with n ∈ C¹(Λ, ℤ). Vortex current: the integer 2-cochain v = dn (0 on-shell of trivial topology; supported on defect cells otherwise).
- Villain action, gauge field: S = (β/2) Σ_p (da − 2πn)² with a ∈ C¹(Λ, ℝ), n ∈ C²(Λ, ℤ); monopole current m = dn ∈ C³(Λ, ℤ).
- Wilson (cosine) actions when we need them: scalar Σ β cos(dθ); gauge U(1) Σ_p β cos(da)_p; SU(N): S = −(β/N) Σ_p Re tr U_p with β = 2N/g².
- **Modified Villain** (Sem II Wk 12): promote n to a ℤ gauge field with its own constraint (dn = 0 enforced by a Lagrange multiplier on the dual lattice), which removes the defects instead of summing them; exact dualities and exact higher-form symmetries follow.

## 4. ℤ_N fields and BF presentation

- ℤ_N p-form field: a ∈ C^p(Λ, ℤ_N), represented by integers mod N; ω = e^{2πi/N}.
- ℤ_N BF weight in d = 4 for a 1-form ℤ_N gauge field: exp((2πi/N) Σ b ∪ da), with b ∈ C²(·, ℤ_N) living where the cup-product pairing puts it (dual placement per GLSS). The same structure in d = 3 with b ∈ C¹.
- When comparing with the group's Julia–Toulouse manuscript, that manuscript's normalizations take precedence; discrepancies get a margin note in the lecture notes rather than a silent fix.

## 5. Cup products

- Cup product ∪ : C^p × C^q → C^{p+q} on the hypercubic lattice, conventions of Chen–Tata. Leibniz: d(x ∪ y) = dx ∪ y + (−1)^p x ∪ dy.
- Non-commutativity is physical, not a nuisance: x ∪ y − (−1)^{pq} y ∪ x is d-exact via the ∪₁ product. Used in Sem II Weeks 6–7 (anomalies, Dijkgraaf–Witten) and stated precisely there.

## 6. Extended operators and symmetry operators

- Wilson operator of charge q on a closed p-cycle C: W_q(C) = exp(iq Σ_C a), i.e. ω^{q Σ_C a} in the ℤ_N case.
- 't Hooft / disorder operators: supported on cycles of Λ*, defined by their modification of the path-integral sum (Kadanoff–Ceva style in Sem I Wk 4; 4d version in Wk 11).
- Symmetry operator of a p-form symmetry: U_α(Σ) on a closed codimension-(p+1) surface Σ. Charge measured by linking: U_α(Σ) W(C) = e^{iα·Link(Σ,C)} W(C) U_α(Σ) in the appropriate sense.
- Ground-state degeneracy bookkeeping on T^d and Σ_g uses H₁ with the intersection pairing; clock–shift pairs (Z, X) obey ZX = ω XZ.

## 7. Hamiltonian conventions (Semester II Block 3)

- Qubits on links; Pauli operators X, Z; ℤ_N generalization by clock and shift.
- Toric code: A_v = Π_{ℓ∋v} X_ℓ (star), B_p = Π_{ℓ∈∂p} Z_ℓ (plaquette), H = −Σ_v A_v − Σ_p B_p.
- Anyons: e (star violation), m (plaquette violation), ε = e × m; braiding phase of e around m: −1 (ω^{q·q'} in ℤ_N).
- Entanglement conventions: von Neumann entropy S(ρ_A) = −tr ρ_A ln ρ_A (natural log; TEE of the toric code is γ = ln 2).

## 8. θ-terms and charges

- θ ∈ [0, 2π); lattice θ-term built from the Villain field strength with cup products (well-defined only in the Villain/modified-Villain form — this is a lecture point, Sem I Wk 12 and Sem II Wk 12).
- Witten effect normalization: dyon electric charge q_e = n_e + θ n_m / 2π.
- Dirac pairing on the lattice: integer linking of electric and magnetic worldobjects via the cochain pairing.

## 9. Units and miscellany

- ħ = c = 1; k_B = 1; β is inverse coupling in lattice actions and inverse temperature only when a transfer matrix says so explicitly.
- "SSB of a p-form symmetry" always means the statement about the realization of U_α(Σ) on the ground-state sector, made precise in Sem II Week 3.
- Abbreviations: LGT (lattice gauge theory), BKT (Berezinskii–Kosterlitz–Thouless), KW (Kramers–Wannier), KS (Kogut–Susskind), FS (Fradkin–Shenker), GKSW, GKKS, GLSS, RSS (per the paper map), TEE (topological entanglement entropy), SPT, DW (Dijkgraaf–Witten), GSD (ground-state degeneracy), JTA (Julia–Toulouse approach).
