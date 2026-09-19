---
title: "Course Conventions"
type: course-note
course: syllabus
modified: 2026-05-17
---

# Course Conventions

This is the canonical convention reference for the algebraic-QFT course. **All lecture notes (Weeks 1–15) and all appendices follow these conventions consistently from Week 4 onward.**

For a comprehensive symbol table, see [[notation-and-conventions|Appendix F]].

## Modular Flow

The course uses the **Witten 1803.04993 §3 convention**:
$$
\boxed{\sigma_t^\omega(a) := \Delta_\omega^{-it}\, a\, \Delta_\omega^{it}.}
$$

For $\mathcal{M} = M_n(\mathbb{C})$ and $\omega_\rho(a) = \mathrm{Tr}(\rho\, a)$:
$$
\sigma_t^\rho(a) = \rho^{-it}\, a\, \rho^{it}.
$$

For a Gibbs state $\rho = e^{-\beta H}/Z$ with physical Heisenberg flow $\alpha_s(a) = e^{isH}\,a\,e^{-isH}$:
$$
\sigma_t^\rho = \alpha_{+\beta t}.
$$

**Modular time runs in the same direction as physical time**, at $\beta$-rescaled rate. This is the structural reason our convention is "natural" for thermal physics.

**Opposite convention** (Bratteli–Robinson Vol. II, and the parallel Codex folder version of this course): $\sigma_t^\omega = \mathrm{Ad}(\Delta^{+it})$, giving $\sigma_t^\rho = \alpha_{-\beta t}$. The two conventions describe the same automorphism group running in opposite directions; they are related by $t \to -t$. **Our convention is fixed; do not mix.**

## KMS Convention

We use the **upper-strip $\beta > 0$** KMS condition:

A state $\omega$ is KMS at $\beta > 0$ for a one-parameter automorphism group $\sigma_t$ if for every $a, b$ there is a function $F_{a,b}$ on the closed strip $\{0 \le \mathrm{Im}\,z \le \beta\}$, holomorphic in the interior, bounded and continuous, with
$$
F_{a, b}(t) = \omega(a\,\sigma_t(b)), \qquad F_{a, b}(t + i\beta) = \omega(\sigma_t(b)\,a).
$$

**Two facts under this convention:**
1. The Gibbs state $\rho = e^{-\beta H}/Z$ with **physical Heisenberg flow** is KMS at $\beta > 0$ upper-strip (Week 4 §1.1, derived).
2. A faithful normal state $\omega$ with **its modular flow** (in our $\Delta^{-it}$ convention) is KMS at $\beta = +1$ upper-strip (Week 6 §3, model proof).

Both physical and modular flows live in the **same upper strip** in our convention — that is the pedagogical advantage.

## Rindler / Bisognano–Wichmann

For the right Rindler wedge $W_R$ in any Wightman QFT (Week 10):
$$
\Delta_{W_R} = e^{-2\pi K}, \qquad \sigma_t^{W_R}(a) = U(\Lambda^{\mathrm{boost}}(2\pi t))\, a\, U(\Lambda^{\mathrm{boost}}(2\pi t))^*.
$$
**Modular time $t$ corresponds to boost rapidity $+2\pi t$.** Unruh temperature $T_U = a/(2\pi)$.

## Modular Boundary Term

For two states $\omega, \phi$ on $\mathcal{M}$ with modular Hamiltonian $K_\phi = -\log\rho_\phi$ of the **reference** state $\phi$, the **modular boundary term** is
$$
\mathcal{B}(\omega, \phi) := \omega(K_\phi) - \phi(K_\phi) = \mathrm{Tr}((\rho_\omega - \rho_\phi)\,K_\phi).
$$

**Note:** uses $K_\phi$ (the second argument's modular Hamiltonian), not $K_\omega$. This is the relative modular energy of $\omega$ measured by the reference flow $\sigma^\phi$.

Vanishes when $\omega = \phi$.

## Dressed-Entropy Difference

The central technical identity (Week 14 Theorem 3.1, derived in §4.4):
$$
S_{\mathrm{vN}}(\hat\rho_\omega) - S_{\mathrm{vN}}(\hat\rho_\phi) = -S(\omega \| \phi) + \mathcal{B}(\omega, \phi),
$$
with $S(\omega\|\phi)$ the Araki–Uhlmann relative entropy (Week 7) and $\mathcal{B}$ as above.

The dressed entropy $S_{\mathrm{vN}}$ itself is well-defined only modulo a state-independent additive constant (from the dressed-trace rescaling ambiguity). The **difference** is finite and physically meaningful.

## Proof-Status Labels

Every theorem-level claim should carry one of these labels in the prose:

- **Proved.** Full proof is included.
- **Model proof.** Proved in finite dimensions, type I, or another controlled case.
- **Sketched.** Main ideas only; missing analytic details are named.
- **Stated only — refs.** Used as a theorem from the literature; reference given.
- **Hypothesis-explicit.** Stated with the technical assumptions required, even if the proof is in references.
- **Heuristic.** Physical or conceptual motivation, not a proof.
- **Example-only.** Demonstrated in one model; not claimed generally.

## Scope Discipline

The course must not blur:

- **Type-I density-matrix calculations** with **type-III local-algebra facts**.
- **Wedge-specific Bisognano–Wichmann geometry** with **generic bounded-region modular flow** (which is *not* geometric).
- **Structural Bell-correlation theorems** (Summers–Werner, hypothesis-explicit) with **explicit Weyl-test-function computations** (which approach but don't attain $2\sqrt 2$).
- **Proved operator-algebra statements** (Connes–Takesaki) with **holographic or gravitational interpretation** (Witten 2022 identification).

## Common Errors to Avoid

1. **Type III$_1$ ≠ Powers III$_\lambda$ at $\lambda = 1$.** The tracial endpoint of the Powers family is type II$_1$, not type III$_1$. III$_1$ is a separate Connes class with full positive S-invariant $[0, \infty)$, realized by QFT local algebras under nuclearity + split property (Week 12).

2. **Type III$_1$ universality is NOT due to Haag–Hugenholtz–Winnink.** HHW 1967 is about KMS/equilibrium states, not local-algebra classification. The correct citation chain is Driessler 1975/77 / Fredenhagen 1985 / Buchholz–Wichmann 1986 / Buchholz–D'Antoni–Fredenhagen 1987, plus Connes 1976 + Haagerup 1987 for operator-algebra uniqueness.

3. **Tomita–Takesaki does NOT produce a state.** Given a faithful normal state $\omega$ on $\mathcal{M}$ (equivalently, a cyclic-separating vector in a standard representation), Tomita–Takesaki produces the state's canonical modular flow $\sigma^\omega_t$, and $\omega$ is KMS for that flow at $\beta = 1$. The state is *input*, not output.

4. **Murray–vN equivalence of projections is INTERNAL to the algebra.** A non-tracial vector state cannot certify or rule out Murray–vN equivalence. Use a partial isometry $u \in \mathcal{M}$, not a state expectation.

5. **The crossed product is NOT the gravitational dressing.** The crossed product is an operator-algebraic construction (Block D, Week 13). Under the holographic dictionary at large $N$ (Witten 2022, Sem II Block 1), the dressed algebra *equals* the gravitational dressing of observables modulo bulk gauge constraints. The equality is a theorem of holographic QFT, separate from the algebraic construction.

6. **Tensor-product factorization does NOT hold for AQFT bounded local algebras.** Type III$_1$ algebras do not split $\mathcal{H} = \mathcal{H}(\mathcal{O}) \otimes \mathcal{H}(\mathcal{O}')$. Tensor reasoning is valid only under the split property (Doplicher–Longo) or in type-I regulators.
