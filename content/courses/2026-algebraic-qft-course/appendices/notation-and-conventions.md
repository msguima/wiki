---
title: "Appendix F — Notation and Conventions"
type: appendix
course: syllabus
modified: 2026-06-11
---

# Notation and Conventions

This appendix is the quick lookup table for symbols and conventions used across the course. **All conventions here apply uniformly from Week 4 onward.**

## F.1 Algebras and Hilbert Spaces

| Symbol | Meaning |
|---|---|
| $\mathcal{A}$ | C\*-algebra, often abstract |
| $\mathcal{M}, \mathcal{N}$ | von Neumann algebras |
| $\mathcal{B}(\mathcal{H})$ | bounded operators on Hilbert space $\mathcal{H}$ |
| $\mathcal{M}'$ | commutant of $\mathcal{M}$ |
| $\mathcal{M}''$ | bicommutant of $\mathcal{M}$ |
| $\mathcal{Z}(\mathcal{M})$ | center of $\mathcal{M}$ |
| $\mathcal{M}_*$ | predual of $\mathcal{M}$ |
| $\mathcal{T}(\mathcal{H})$ | trace-class operators on $\mathcal{H}$ |
| $\mathcal{A}(\mathcal{O})$ | local algebra associated with region $\mathcal{O}$ |
| $W_R, W_L$ | right and left Rindler wedges |
| $\mathcal{F}$ | Fock space |
| $\lvert 0_M\rangle, \lvert 0_R\rangle$ | Minkowski and Rindler vacua |

## F.2 States, Weights, and Traces

| Symbol | Meaning |
|---|---|
| $\omega, \phi$ | states or normal positive linear functionals |
| $\omega_\rho(a) = \mathrm{Tr}(\rho\,a)$ | density-matrix state (type I or trace-class) |
| $\tau$ | trace, usually finite or semifinite |
| $\hat\tau$ | trace on a crossed product / continuous core |
| $\varphi$ | weight (possibly non-finite) |
| $\rho, \sigma$ | density matrices in type I, or trace densities in semifinite settings |
| $\hat\rho$ | density of a dressed state relative to $\hat\tau$ |
| $\Omega, \Omega_\omega$ | cyclic-separating GNS vector for state $\omega$ |

**Course rule on "density matrix" language:**
- $\rho$ is allowed when the algebra is type I, or when a specified trace is in scope.
- In type III, say "normal state" rather than "density matrix" unless using a regulator or split inclusion.

## F.3 Modular Objects

| Symbol | Meaning |
|---|---|
| $S$ | Tomita operator, $S(a\Omega) = a^*\Omega$ on $\mathcal{M}\Omega$ |
| $J$ | modular conjugation (antiunitary) |
| $\Delta$ | modular operator (positive self-adjoint) |
| $\sigma_t^\omega$ | modular automorphism group of $\omega$ |
| $K_\rho = -\log\rho$ | finite-dimensional modular Hamiltonian |
| $K_\omega = -\log\Delta_\omega$ | formal modular Hamiltonian |
| $\Delta_{\omega, \phi}$ | relative modular operator |
| $(D\omega/D\phi)_t$ | Connes cocycle of $\omega$ relative to $\phi$ |

**Course modular-flow convention (upper-strip $\beta > 0$):**
$$
\sigma_t^\omega(a) \;:=\; \Delta_\omega^{-it}\, a\, \Delta_\omega^{it}.
$$

**Finite-dimensional relation.** For $\omega(a) = \mathrm{Tr}(\rho\,a)$:
$$
\sigma_t^\rho(a) \;=\; \rho^{-it}\, a\, \rho^{it}.
$$

**Gibbs case.** If $\rho = e^{-\beta H}/Z$ and $\alpha_s(a) = e^{isH}\,a\,e^{-isH}$ is the physical Heisenberg flow,
$$
\sigma_t^\rho \;=\; \alpha_{+\beta t}.
$$
Modular time runs in the *same direction* as physical time, at $\beta$-rescaled rate.

**Opposite convention** (Bratteli–Robinson Vol. II; Codex parallel folder): $\sigma_t^\omega(a) = \Delta^{+it}_\omega a \Delta^{-it}_\omega$, giving $\sigma_t^\rho = \alpha_{-\beta t}$. The two are related by $t \to -t$ and describe the same automorphism group running in opposite directions. **Our convention matches Witten 1803.04993 §3** (modular Hamiltonian $K = -\log\rho$ generates the flow via $\sigma_t = \mathrm{Ad}(e^{itK}) = \mathrm{Ad}(\Delta^{-it})$).

## F.4 KMS Convention

Physical Heisenberg KMS for a Gibbs state at inverse temperature $\beta > 0$ is **upper-strip**:
$$
F_{a,b}(t) = \omega(a\,\alpha_t(b)),
\qquad
F_{a,b}(t + i\beta) = \omega(\alpha_t(b)\,a).
$$

The modular flow in our convention satisfies the same upper-strip KMS at $\beta = +1$:
$$
F_{a,b}(t) = \omega(a\,\sigma_t^\omega(b)),
\qquad
F_{a,b}(t + i) = \omega(\sigma_t^\omega(b)\,a).
$$

Both physical and modular flows live in the **same upper strip** — that is the structural advantage of our convention over the Bratteli–Robinson one (which puts physical Heisenberg in the upper strip and modular flow in the lower strip).

## F.5 Type Classification

| Type | Structural marker | Trace status |
|---|---|---|
| I$_n$ ($n < \infty$) | $\cong M_n(\mathbb{C})$ | finite trace |
| I$_\infty$ | $\cong \mathcal{B}(\mathcal{H})$, $\dim\mathcal{H} = \infty$ | semifinite trace |
| II$_1$ | no minimal projection, $1$ finite | unique normalized trace |
| II$_\infty$ | no minimal projection, $1$ infinite | semifinite trace |
| III | every non-zero projection infinite | no faithful normal trace |

**Connes type-III subclasses** (Connes 1973):
$$
\mathrm{III}_0, \qquad \mathrm{III}_\lambda \;(0 < \lambda < 1), \qquad \mathrm{III}_1.
$$

**Important — common pitfall.**
- III$_1$ is **not** the $\lambda = 1$ endpoint of the Powers III$_\lambda$ family.
- The Powers III$_\lambda$ family has $\lambda \in (0, 1)$ strictly. Its $\lambda = 1$ tracial endpoint is the hyperfinite II$_1$ factor.
- III$_1$ is a separate Connes class with full positive S-invariant $[0, \infty)$, realized by QFT local algebras under nuclearity + split property (Week 12).

## F.6 Crossed-Product Notation

| Symbol | Meaning |
|---|---|
| $\alpha_t$ | one-parameter automorphism group used in a crossed product |
| $\pi_\alpha(a)$ | fiberwise representation of $a \in \mathcal{M}$, $(\pi_\alpha(a)\xi)(s) = \alpha_{-s}(a)\xi(s)$ |
| $\lambda(t)$ | translation/clock unitary, $(\lambda(t)\xi)(s) = \xi(s-t)$ |
| $\mathcal{M} \rtimes_\alpha \mathbb{R}$ | crossed product |
| $\hat{\mathcal{M}}$ or $\hat{\mathcal{M}}_\omega$ | modular crossed product $\mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R}$ |
| $\theta_r$ | dual action of $\hat{\mathbb{R}}$ |
| $\hat\tau$ | faithful normal semifinite trace on the crossed product |

**Covariance relation:**
$$
\lambda(t)\,\pi_\alpha(a)\,\lambda(t)^* = \pi_\alpha(\alpha_t(a)).
$$

**Dual-action trace scaling:**
$$
\hat\tau \circ \theta_r = e^{-r}\,\hat\tau.
$$

## F.7 Rindler and TFD Symbols

| Symbol | Meaning |
|---|---|
| $\Lambda^{\mathrm{boost}}(s)$ | Lorentz boost in $(x^0, x^1)$ plane by rapidity $s$ |
| $K$ | boost generator, $U(\Lambda^{\mathrm{boost}}(s)) = e^{-isK}$ |
| $\eta$ | Rindler time coordinate |
| $\xi$ | Rindler radial coordinate (lapse $\xi_0$ for an observer with acceleration $a = 1/\xi_0$) |
| $\lvert\mathrm{TFD}_\beta\rangle$ | thermofield double state at inverse temperature $\beta$ |
| $H_R, H_L$ | right and left boundary Hamiltonians |

**Course Rindler conventions (Bisognano–Wichmann; our sign):**
$$
\Delta_{W_R} = e^{-2\pi K}, \qquad
\sigma_t^{W_R} = \mathrm{Ad}(U(\Lambda^{\mathrm{boost}}(2\pi t))).
$$
Modular time $t$ corresponds to boost rapidity $+2\pi t$ — the boost subgroup running *forward*. Unruh temperature $T_U = a/(2\pi)$.

## F.8 Entropy Notation

| Symbol | Meaning |
|---|---|
| $S(\rho) = -\mathrm{Tr}(\rho\log\rho)$ | von Neumann entropy (finite-dim or type I with trace) |
| $S(\rho\Vert\sigma)$ | Umegaki relative entropy (finite-dim or type I) |
| $S(\omega\Vert\phi)$ | Araki–Uhlmann relative entropy (any vN algebra) |
| $S_{\mathrm{vN}}(\hat\rho)$ | dressed entropy on type II$_\infty$ crossed product, up to additive constant |
| $S_{\mathrm{gen}}$ | generalized entropy in gravity (only in holographic settings) |
| $\mathcal{B}(\omega, \phi)$ | modular boundary term |

**Finite-dimensional identity** (Week 14 Theorem 3.1; explicit derivation in §4.4):
$$
S(\rho) - S(\sigma) = -S(\rho\|\sigma) + \mathrm{Tr}((\rho - \sigma)\,K_\sigma),
\qquad K_\sigma = -\log\sigma.
$$
In our notation:
$$
S_{\mathrm{vN}}(\omega) - S_{\mathrm{vN}}(\phi) = -S(\omega\|\phi) + \mathcal{B}(\omega, \phi),
\qquad \mathcal{B}(\omega, \phi) = \omega(K_\phi) - \phi(K_\phi).
$$
**Boundary term uses the modular Hamiltonian of the reference state $\phi$**, not of $\omega$.

**Safe distinctions** (Week 12 §4):
- $S(\omega\|\phi)$: *exact* type-III-safe relative entropy.
- $S_{\mathrm{vN}}(\hat\rho)$: well-defined on the dressed algebra, up to a state-independent additive constant.
- $S_{\mathrm{gen}}$: requires the holographic dictionary as additional input.

All three are *distinct controlled objects*, not the same thing.
