---
title: "Appendix C — Modular Theory Reference Sheet"
type: appendix
course: syllabus
modified: 2026-06-11
---

# Modular Theory Reference Sheet

Compact reference for Tomita–Takesaki objects used throughout Block B and beyond. **All conventions match Week 4 §6.1 and the note-quality template.**

## C.1 Standard Setup

Let $\mathcal{M} \subset \mathcal{B}(\mathcal{H})$ be a von Neumann algebra and $\Omega \in \mathcal{H}$ a vector that is **cyclic** and **separating** for $\mathcal{M}$ (Week 5).

Cyclic: $\overline{\mathcal{M}\Omega} = \mathcal{H}$.
Separating: $a\Omega = 0$ with $a \in \mathcal{M}$ implies $a = 0$.

The vector state $\omega(a) := \langle\Omega, a\Omega\rangle$ is then a **faithful normal state** (Week 5 Lemma 1.3).

## C.2 Tomita Operator

On the dense subspace $\mathcal{M}\Omega \subset \mathcal{H}$, define the conjugate-linear operator
$$
S_0(a\Omega) := a^*\Omega.
$$
$S_0$ is closable (Week 5 Prop 2.2); its closure is denoted $S$.

**Polar decomposition.** $S = J\Delta^{1/2}$, where:
- $J$ is **antiunitary** with $J^* = J$ and $J^2 = 1$ (modular conjugation).
- $\Delta := S^*S$ is **positive self-adjoint** (modular operator).

## C.3 Tomita–Takesaki Theorem

**[Stated only — refs: B-R Vol. I §2.5; Takesaki Vol. II Ch. VIII.]** Under the standard setup,
$$
J\,\mathcal{M}\,J = \mathcal{M}', \qquad \Delta^{-it}\,\mathcal{M}\,\Delta^{it} = \mathcal{M} \quad \text{for all } t \in \mathbb{R}.
$$

The **modular automorphism group** of $(\mathcal{M}, \Omega)$ is
$$
\boxed{\sigma_t^\omega(a) := \Delta^{-it}\, a\, \Delta^{it}.}
$$

**This is the course convention** (upper-strip $\beta > 0$, matching Witten 1803.04993). The opposite-sign convention $\sigma_t = \mathrm{Ad}(\Delta^{+it})$ also appears in the literature (Bratteli–Robinson Vol. II) and gives the same automorphism group running backwards.

**Proof status in the course:**
- Finite-dimensional/type-I model: computed explicitly (Week 5 §5).
- Full theorem: statement only, used as a standard theorem.

## C.4 KMS Condition for the Modular Flow

With the course convention, $\omega$ is KMS at $\beta = 1$ for $\sigma^\omega$ in the upper strip:
$$
F_{a,b}(t) = \omega(a\,\sigma_t^\omega(b)), \qquad F_{a,b}(t + i) = \omega(\sigma_t^\omega(b)\,a),
$$
with $F_{a,b}$ holomorphic on $\{0 \le \mathrm{Im}\,z \le 1\}$.

Both physical Heisenberg + Gibbs (Week 4 §1.1) and modular flow at $\beta = +1$ live in the **same upper strip** in our convention.

## C.5 Finite-Dimensional Computation

For $\mathcal{M} = M_n(\mathbb{C})$ with state $\omega_\rho(a) = \mathrm{Tr}(\rho a)$, $\rho > 0$:
- GNS Hilbert space: $\mathcal{H}_{\mathrm{HS}} = M_n(\mathbb{C})$ with $\langle X, Y\rangle = \mathrm{Tr}(X^*Y)$.
- Cyclic-separating vector: $\Omega_\rho = \rho^{1/2}$.
- Tomita operator: $S(X) = \rho^{-1/2}\,X^*\,\rho^{1/2}$. (Check: extends $S(a\,\rho^{1/2}) = a^*\rho^{1/2}$, since $X = a\rho^{1/2} \Rightarrow a = X\rho^{-1/2}$; and $S^2 = 1$. For the tracial state $\rho = 1/n$ this reduces to $S(X) = X^*$.)
- Modular operator: $\Delta_\rho(X) = \rho X \rho^{-1}$ on $\mathcal{H}_{\mathrm{HS}}$. (Check: $J\Delta^{1/2}(X) = (\rho^{1/2}X\rho^{-1/2})^* = \rho^{-1/2}X^*\rho^{1/2} = S(X)$. ✓)
- Modular conjugation: $J_\rho(X) = X^*$ (Hilbert–Schmidt complex-conjugate-transpose).

Modular automorphism on $\mathcal{M}$:
$$
\sigma_t^\rho(a) = \rho^{-it}\, a\, \rho^{it}.
$$

For a Gibbs state $\rho = e^{-\beta H}/Z$:
$$
\sigma_t^\rho(a) = e^{i\beta t H}\,a\,e^{-i\beta t H} = \alpha_{+\beta t}(a),
$$
modular time is the inverse-temperature rescaling of physical Heisenberg time.

## C.6 Type-I Bipartite Computation

For $\mathcal{M} = \mathcal{B}(\mathcal{H}_A) \otimes 1$ acting on $\mathcal{H}_A \otimes \mathcal{H}_B$, and $\Omega = \sum_i \sqrt{p_i}\,e_i \otimes f_i$ in Schmidt form (all $p_i > 0$):
- $\rho_A = \sum_i p_i |e_i\rangle\langle e_i|$ (reduced density on $\mathcal{H}_A$).
- $\Delta = \rho_A \otimes \rho_A^{-1}$ (the inverse acts on $\mathcal{H}_B$ via the Schmidt isomorphism).
- $J(e_i \otimes f_j) = e_j \otimes f_i$ with complex conjugation in the Schmidt bases.
- $\sigma_t^\Omega(a \otimes 1) = (\rho_A^{-it} a \rho_A^{it}) \otimes 1$.

Modular Hamiltonian: $K_A := -\log\rho_A$ (positive operator on $\mathcal{H}_A$).

## C.7 Relative Modular Operator and Connes Cocycle (Week 7)

Given two faithful normal states $\omega, \phi$ with GNS vectors $\Omega_\omega, \Omega_\phi$:
- **Relative Tomita operator**: $S_{\omega, \phi}(a\Omega_\phi) := a^*\Omega_\omega$.
- **Relative modular operator**: $\Delta_{\omega, \phi} := S_{\omega, \phi}^*\,S_{\omega, \phi}$.

In finite dim, $\Delta_{\rho, \sigma}(X) = \rho X \sigma^{-1}$ on $\mathcal{H}_{\mathrm{HS}}$.

**Connes cocycle** (our convention):
$$
u_t = (D\omega / D\phi)_t := \Delta_{\omega, \phi}^{-it}\,\Delta_\phi^{it}.
$$
In finite dim: $u_t = \rho^{-it}\sigma^{it}$. Lies in $\mathcal{M}$.

**Cocycle identity**: $u_{t+s} = u_t\,\sigma_t^\phi(u_s)$.

**Intertwining**: $\sigma_t^\omega(a) = u_t\,\sigma_t^\phi(a)\,u_t^*$.

## C.8 Araki–Uhlmann Relative Entropy (Week 7)

$$
S(\omega \| \phi) := -\langle\Omega_\omega,\, \log\Delta_{\phi, \omega}\,\Omega_\omega\rangle.
$$

**Note the index order**: the modular operator inside $\log$ has $\phi$ first (reference state) and $\omega$ second.

In finite dim, reduces to Umegaki:
$$
S(\omega_\rho \| \omega_\sigma) = \mathrm{Tr}(\rho(\log\rho - \log\sigma)).
$$

**Properties.**
- $S(\omega\|\phi) \ge 0$, with equality iff $\omega = \phi$ (Klein's inequality + spectral theorem).
- Monotone under restriction to subalgebras: $S(\omega|_\mathcal{N}\|\phi|_\mathcal{N}) \le S(\omega|_\mathcal{M}\|\phi|_\mathcal{M})$ for $\mathcal{N} \subset \mathcal{M}$.

## C.9 Bisognano–Wichmann (Week 10)

For the right Rindler wedge $W_R = \{x: x^1 > |x^0|\}$ in a Wightman QFT, with vacuum $|0_M\rangle$:
$$
\Delta_{W_R} = e^{-2\pi K}, \qquad J_{W_R} = \Theta \cdot R_\perp(\pi),
$$
where $K$ is the boost generator and $\Theta$ is the antiunitary CPT operator. The modular flow:
$$
\sigma_t^{W_R}(a) = U(\Lambda^{\mathrm{boost}}(2\pi t))\, a\, U(\Lambda^{\mathrm{boost}}(2\pi t))^*.
$$
Modular time $t$ corresponds to boost rapidity $+2\pi t$. Unruh temperature $T_U = a/(2\pi)$.

## C.10 Three Distinguishing Properties (Week 12)

- **Type II$_1$**: tracial state has $\Delta = 1$, $\sigma_t = \mathrm{id}$, $S(\mathcal{M}) = \{1\}$.
- **Type III$_\lambda$ ($\lambda \in (0, 1)$)**: modular flow on Powers state is periodic, $T_\lambda = 2\pi/|\log\lambda|$, $S(\mathcal{M}) = \{0\}\cup\{\lambda^n: n \in \mathbb{Z}\}$.
- **Type III$_1$**: modular spectrum is full $\mathbb{R}$ on every faithful normal state, $S(\mathcal{M}) = [0, \infty)$.

## C.11 Use in the Course

| Week | Modular object used |
|---|---|
| 5 | $S, J, \Delta$ (Tomita operator + polar decomp) |
| 6 | $\sigma^\omega_t$ (modular automorphism + KMS) |
| 7 | $\Delta_{\omega,\phi}$, $(D\omega/D\phi)_t$, $S(\omega\Vert\phi)$ |
| 9 | Reeh–Schlieder licenses Tomita–Takesaki for local algebras |
| 10 | Bisognano–Wichmann: $\Delta = e^{-2\pi K}$ on wedges |
| 11 | Modular structure ⇒ Bell–CHSH saturation |
| 12 | S-invariant classifies type III subtypes |
| 13 | Crossed product by $\sigma^\omega$ |
| 14 | Dressed entropy + modular boundary term $\omega(K_\phi) - \phi(K_\phi)$ |
| 15 | TFD modular operator $\Delta = e^{-\beta(H_R - H_L)}$ |

## C.12 Math ↔ Physics Dictionary

| Modular object | Physical meaning |
|---|---|
| Cyclic vector $\Omega$ | Fully entangled reference state; local ops reach everything (Reeh–Schlieder) |
| Separating vector | No local annihilator; faithful state; "vacuum is nowhere empty" |
| Tomita operator $S$ | State-flip $a \to a^*$; its non-isometry encodes the state's thermal tilt |
| $J$ (modular conjugation) | Mirror into the commutant; CPT × rotation for wedges; system ↔ environment duality |
| $\Delta$ (modular operator) | Boltzmann-weight ratios of the state; $e^{-2\pi K}$ for wedges |
| $\sigma_t^\omega$ (modular flow) | Intrinsic thermal time of $(\mathcal{M}, \omega)$; boost for wedges; ADM time at large $N$ |
| $K = -\log\Delta$ | Modular Hamiltonian; boost generator (×$2\pi$); $\beta(H_R - H_L)$ for TFD |
| KMS at $\beta = 1$ | Equilibrium; imaginary-time periodicity; detailed balance $\hat G_- = e^{-\beta\nu}\hat G_+$ |
| Spectrum of $\Delta$ | Thermal fingerprint; its state-independent core is the Connes invariant (type) |
| Connes cocycle $(D\omega/D\phi)_t$ | Noncommutative Radon–Nikodym derivative; dressing converting one equilibrium dynamics into another |
| $S(\omega\Vert\phi)$ | Optimal distinguishability rate (quantum Stein); finite in type III |
| Crossed product $\mathcal{M}\rtimes_\sigma\mathbb{R}$ | Algebra of clock-dressed (relational/gauge-invariant) observables |
| Dressed trace $\hat\tau$ | Counting measure restored by gauging time; unique up to scale |
| Dressed entropy $S_{\mathrm{vN}}(\hat\rho)$ | Generalized entropy $A/4G_N + S_{\mathrm{out}}$ in holographic settings |
