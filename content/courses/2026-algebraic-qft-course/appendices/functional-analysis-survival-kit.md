---
title: "Appendix A — Functional-Analysis Survival Kit"
type: appendix
course: syllabus
modified: 2026-06-11
---

# Functional-Analysis Survival Kit

This appendix collects the analytic facts used repeatedly in the course. It is **not a replacement** for a functional-analysis course. It is the minimum toolkit a student needs in order to read the lecture notes without stopping every page.

## A.1 Hilbert-Space Conventions

Inner products are linear in the *second* slot:
$$
\langle \xi, \lambda\eta\rangle = \lambda\langle\xi, \eta\rangle, \qquad \langle \lambda\xi, \eta\rangle = \overline{\lambda}\langle\xi, \eta\rangle.
$$
For a bounded operator $T$ on a Hilbert space $\mathcal{H}$, the adjoint $T^*$ is defined by $\langle\xi, T\eta\rangle = \langle T^*\xi, \eta\rangle$.

Key classes:
- $T$ is **self-adjoint** if $T = T^*$.
- $T$ is **positive** if $\langle\xi, T\xi\rangle \ge 0$ for all $\xi$.
- $U$ is **unitary** if $U^*U = UU^* = 1$.
- $P$ is a **projection** if $P = P^* = P^2$.

When $P$ is a projection, $P\mathcal{H}$ is a closed subspace; every closed subspace has an orthogonal projection.

## A.2 Bounded and Unbounded Operators

The course mostly uses bounded operator algebras, but QFT fields are unbounded before smearing or exponentiation.

A **bounded operator** $T$ satisfies $\|T\xi\| \le C\|\xi\|$ for all $\xi$; the smallest such $C$ is the operator norm $\|T\|$.

An **unbounded operator** $A$ is a pair $(A, \mathrm{Dom}\,A)$ where $\mathrm{Dom}\,A$ is a dense subspace and $A$ is linear on it. Domain questions matter for fields $\phi(f)$ and for logarithms like $\log\Delta$, but the von Neumann algebra itself is built from *bounded* operators.

**Course rule:**
- Use unbounded fields as motivation and for formal calculations.
- Use bounded Weyl operators $W(f) = e^{i\phi(f)}$, spectral projections, modular unitaries $\Delta^{-it}$, and von Neumann algebras for exact algebraic statements.

## A.3 The Spectral Theorem

If $A = A^*$ is a self-adjoint operator (bounded or unbounded with self-adjoint closure), there is a projection-valued measure $E_A$ on $\mathbb{R}$ such that
$$
A = \int_{\mathbb{R}} \lambda\, dE_A(\lambda), \qquad f(A) = \int_{\mathbb{R}} f(\lambda)\, dE_A(\lambda)
$$
for bounded measurable $f$. The spectrum $\sigma(A) = \{\lambda \in \mathbb{R}: E_A(B) \neq 0\text{ for every open ball } B \ni \lambda\}$.

**Used throughout the course for:**
- $\rho^{it}$ via $\rho > 0$, $\rho^{it} = e^{it\log\rho}$ (functional calculus).
- $\Delta^{-it}$ via $\Delta$ positive self-adjoint.
- $e^{-\beta H}$ for the Gibbs density.
- $\log\Delta$ as the modular Hamiltonian.

## A.4 Topologies on $\mathcal{B}(\mathcal{H})$

We use four topologies:

**Norm topology.** $T_n \to T$ iff $\|T_n - T\| \to 0$. Strongest of the four.

**Strong operator topology (SOT).** $T_n \to T$ iff $T_n\xi \to T\xi$ for every $\xi \in \mathcal{H}$. Strictly weaker than norm.

**Weak operator topology (WOT).** $T_n \to T$ iff $\langle\eta, T_n\xi\rangle \to \langle\eta, T\xi\rangle$ for every $\xi, \eta$. Strictly weaker than SOT.

**$\sigma$-weak (ultraweak) topology.** $T_n \to T$ iff $\mathrm{Tr}(\rho T_n) \to \mathrm{Tr}(\rho T)$ for every trace-class $\rho$. Equivalent to WOT on norm-bounded sets, but strictly stronger on unbounded ones. **The "right" topology for normal states/predual.**

A **von Neumann algebra** is a unital $*$-subalgebra of $\mathcal{B}(\mathcal{H})$ closed in WOT (equivalently, SOT, equivalently $\sigma$-weak). Norm-closure gives only a C\*-algebra, not generally a vN algebra.

*Physical reading (Week 2 §2):* norm closeness = uniform closeness over all states (no experiment tests this); WOT closeness = closeness of every measurable matrix element / correlation function (what experiments do test). Closing in WOT adds exactly the operators no experiment can distinguish from the algebra — e.g. spectral projections (yes/no questions), which norm closure misses.

**Key fact (Sakai).** A C\*-algebra $\mathcal{A}$ is a vN algebra iff it has a predual: there is a Banach space $\mathcal{A}_*$ with $\mathcal{A} = (\mathcal{A}_*)^*$.

## A.5 States, Normal States, Predual

A **state** on a C\*-algebra $\mathcal{A}$ is a positive linear functional $\omega: \mathcal{A} \to \mathbb{C}$ with $\omega(1) = 1$.

A state $\omega$ on a vN algebra $\mathcal{M}$ is **normal** if it is $\sigma$-weakly continuous; equivalently if it is order-continuous: $\omega(\sup_\alpha a_\alpha) = \sup_\alpha \omega(a_\alpha)$ for increasing nets of positive operators.

The predual $\mathcal{M}_*$ is the space of normal linear functionals; $\mathcal{M} = (\mathcal{M}_*)^*$.

**For type I**: $\mathcal{M}_* \cong \mathcal{T}(\mathcal{H})$ (trace-class operators), and every normal state has a density matrix.

**For type III**: $\mathcal{M}_*$ is still a Banach space of normal functionals, but **no density-matrix representation exists**.

## A.6 GNS Construction (Recap from Week 1)

Given a state $\omega$ on a C\*-algebra $\mathcal{A}$:
1. The sesquilinear form $\langle a, b\rangle_\omega := \omega(a^*b)$ on $\mathcal{A}$ is positive semi-definite.
2. Quotient by the null space $\mathcal{N}_\omega = \{a: \omega(a^*a) = 0\}$ to get a pre-Hilbert space $\mathcal{A}/\mathcal{N}_\omega$.
3. Complete to a Hilbert space $\mathcal{H}_\omega$.
4. Left multiplication by $\mathcal{A}$ defines a $*$-representation $\pi_\omega: \mathcal{A} \to \mathcal{B}(\mathcal{H}_\omega)$.
5. The image of $1 \in \mathcal{A}$ is a cyclic vector $\Omega_\omega \in \mathcal{H}_\omega$ with $\omega(a) = \langle\Omega_\omega, \pi_\omega(a)\,\Omega_\omega\rangle$.

The GNS triple $(\mathcal{H}_\omega, \pi_\omega, \Omega_\omega)$ is unique up to unitary equivalence.

The state is **faithful** ($\omega(a^*a) = 0 \Rightarrow a = 0$) iff $\Omega_\omega$ is **separating** for the WOT-closure $\pi_\omega(\mathcal{A})''$ (Week 5 Lemma 1.3).

The state is **factorial** ($\pi_\omega(\mathcal{A})''$ has trivial center) iff the GNS representation is **irreducible** in the appropriate sense.

## A.7 Trace-Class and Hilbert–Schmidt Operators

The **Hilbert–Schmidt** operators $\mathcal{HS}(\mathcal{H})$ are those with $\sum_i \|Te_i\|^2 < \infty$ for any orthonormal basis. They form a two-sided ideal in $\mathcal{B}(\mathcal{H})$.

The **trace-class** operators $\mathcal{T}(\mathcal{H})$ are those with $\sum_i \langle e_i, |T|\,e_i\rangle < \infty$. They form a two-sided ideal in $\mathcal{B}(\mathcal{H})$ and $\mathcal{T}(\mathcal{H}) \subset \mathcal{HS}(\mathcal{H}) \subset \mathcal{K}(\mathcal{H})$ (compact) $\subset \mathcal{B}(\mathcal{H})$.

The trace $\mathrm{Tr}: \mathcal{T}(\mathcal{H}) \to \mathbb{C}$ is the standard sum-of-diagonal-entries, basis-independent.

**In Week 7 §3**: the Hilbert–Schmidt space $\mathcal{HS}(\mathcal{H}) = M_n(\mathbb{C})$ (finite-dim case) is used as the GNS Hilbert space for type-I states, with left multiplication as the representation. This is the natural setting for explicit modular-operator and relative-modular-operator computations.

## A.8 Tensor Products

The **algebraic tensor product** $\mathcal{H}_1 \otimes_{\mathrm{alg}} \mathcal{H}_2$ has a natural inner product $\langle\xi_1\otimes\xi_2, \eta_1\otimes\eta_2\rangle = \langle\xi_1,\eta_1\rangle\langle\xi_2,\eta_2\rangle$. Completing gives the **Hilbert-space tensor product** $\mathcal{H}_1 \otimes \mathcal{H}_2$.

For vN algebras: $\mathcal{M}_1 \overline\otimes \mathcal{M}_2$ is the **spatial tensor product**, the WOT-closure of $\mathcal{M}_1 \otimes_{\mathrm{alg}} \mathcal{M}_2$ on $\mathcal{H}_1 \otimes \mathcal{H}_2$.

**Commutant theorem.** $(\mathcal{M}_1 \overline\otimes \mathcal{M}_2)' = \mathcal{M}_1' \overline\otimes \mathcal{M}_2'$ (this works in the spatial tensor product; abstract tensor products are more delicate).

In Block C / Block D, **tensor-product factorization fails** for AQFT local algebras of bounded regions: $\mathcal{H} \ne \mathcal{H}(\mathcal{O}) \otimes \mathcal{H}(\mathcal{O}')$ in general. This is the type-III$_1$ obstruction. Tensor-product reasoning is valid under split-property assumptions (Doplicher–Longo) and in type-I regulators.

## A.9 Polar Decomposition

A closed densely-defined operator $T$ has a unique polar decomposition $T = V|T|$, where $|T| = (T^*T)^{1/2} \ge 0$ and $V$ is a partial isometry with initial space $\overline{\mathrm{ran}\,|T|}$ and final space $\overline{\mathrm{ran}\,T}$.

For conjugate-linear $T$ (e.g., the Tomita operator $S$), the same decomposition holds with $V$ antiunitary. In the cyclic-separating setting, $V$ extends to an antiunitary on the full Hilbert space — this is the modular conjugation $J$.

**Used in:**
- Tomita operator polar decomposition $S = J\Delta^{1/2}$ (Week 5 §3).
- Connes cocycle existence (Week 7 §4).

## A.10 Analytic Vectors and the Analytic Subalgebra

For an unbounded self-adjoint $A$ generating a one-parameter unitary group $U(t) = e^{itA}$, a vector $\xi$ is **analytic** for $A$ if $\sum_n \frac{t^n}{n!}\|A^n\xi\| < \infty$ for $|t|$ in some open interval. The set of analytic vectors is dense (Nelson's theorem) for any self-adjoint $A$.

Analytic vectors are where the spectral expansion $U(z)\xi = \sum_n \frac{(iz)^n}{n!}A^n\xi$ converges for complex $z$ in a strip around the real axis. **The KMS condition is a statement about analytic continuation of two-point functions** (Week 4 §1.1, Week 6 §3); the analytic subalgebra is where such continuations are valid.

*Physical reading:* analytic continuation in time is licensed by spectral positivity — bounded-below generators make $e^{-\tau A}$ a damping operator for $\tau > 0$. Every "Euclidean" maneuver in the course (Wick rotation, KMS strips, the $\Delta^{1/2} = e^{-\pi K}$ half-rotation of Week 10) is, at the operator level, an evaluation on analytic vectors. When a formal manipulation of $\Delta^{iz}$ looks suspicious, the question to ask is always: *is the vector analytic in the required strip?*

## A.11 What's Used Where

| Topic | Used in |
|---|---|
| Spectral theorem | Throughout; especially Weeks 4, 5, 6 (modular operator), 10 (boost generator) |
| Bounded vs. unbounded | Weeks 8 (smeared fields), 5 (Tomita operator), 10 (boost) |
| Topologies (WOT/SOT) | Week 2 (vN algebra definition) |
| Predual / normal states | Weeks 2, 12 (type III; no density matrix as operator means via predual) |
| GNS | Week 1 (foundation), all subsequent weeks |
| Trace-class | Week 7 (Hilbert–Schmidt GNS for type I) |
| Tensor products | Week 5 (type-I modular), Week 9 (no factorization for AQFT), Week 13 (crossed product on $\mathcal{H} \otimes L^2(\mathbb{R})$) |
| Polar decomposition | Week 5 (Tomita operator), Week 7 (Connes cocycle) |
| Analytic vectors | Weeks 4, 6, 14 (KMS strip analytic continuations) |

## A.12 Suggested Reading

For students who need a full functional-analysis text:

- Reed & Simon, *Methods of Modern Mathematical Physics*, Vol. I (functional analysis) and Vol. II (Fourier analysis, self-adjointness). The standard reference.
- Conway, *A Course in Functional Analysis*. More accessible introduction.
- Pedersen, *Analysis Now*. Compact alternative.

For operator algebras specifically:
- Murphy, *C\*-algebras and Operator Theory*. Friendly first text.
- Bratteli & Robinson Vol. I, ch. 2. Course's primary reference.
