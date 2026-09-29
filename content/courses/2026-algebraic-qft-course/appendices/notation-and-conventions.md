---
title: "Appendix F — Notation and Conventions"
type: appendix
course: syllabus
modified: 2026-08-24
---

# Notation and Conventions

This appendix is the quick lookup table for symbols and conventions used across the course. **All conventions here apply uniformly from Week 4 onward.**

**Dimension warning.** The free-field chapters write $\mathbb R^{1,d}$ with
$d$ spatial dimensions. The holography chapters follow the usual
CFT$_d$/AdS$_{d+1}$ notation, where $d$ is the boundary spacetime dimension.
At a bridge between the two, the note spells out “$3+1$ dimensions” rather
than relying on an unqualified value of $d$.

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
| $K_{\mathrm{GNS},\omega} = -\log\Delta_\omega$ | modular generator on the GNS/standard-form Hilbert space |
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

**Opposite convention** (used, for example, in Bratteli--Robinson Vol. II):
$\sigma_t^\omega(a)=\Delta_\omega^{it}a\Delta_\omega^{-it}$, giving
$\sigma_t^\rho=\alpha_{-\beta t}$. The two are related by $t\mapsto-t$ and
describe the same automorphism group with reversed parametrization. **Our
convention matches Witten 1803.04993 §3:** $K=-\log\rho$ generates
$\sigma_t=\operatorname{Ad}(e^{itK})=\operatorname{Ad}(\Delta^{-it})$.

There are two related operators here, and the distinction matters. In a
finite-dimensional standard representation,
$$
-\log\Delta_\rho
=(-\log\rho)\otimes 1-1\otimes(-\log\rho)^{\mathsf T}.
$$
Thus $K_\rho=-\log\rho$ generates the automorphism of the observable algebra,
whereas $K_{\mathrm{GNS},\rho}=-\log\Delta_\rho$ acts on the doubled
standard-form Hilbert space.

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
- III$_1$ is a separate Connes class with full positive S-invariant
  $[0,\infty)$. Under the additional hypotheses reviewed in Week 12, local
  QFT algebras are hyperfinite type III$_1$; neither nuclearity nor the split
  property alone is being advertised here as a classification theorem.

## F.6 Crossed-Product Notation

| Symbol | Meaning |
|---|---|
| $\alpha_t$ | one-parameter automorphism group used in a crossed product |
| $t$ | parameter of $\alpha_t$; for a modular core, modular time |
| $q$ | coordinate on the auxiliary $L^2(\mathbb R,dq)$ factor |
| $Q$ | multiplication operator, $(Q\xi)(q)=q\xi(q)$ |
| $P$ | conjugate momentum $-i\partial_q$ |
| $p$ | Fourier-dual coordinate in which $P$ is multiplication |
| $\pi_\alpha(a)$ | covariant representation, $(\pi_\alpha(a)\xi)(q)=\alpha_{-q}(a)\xi(q)$ |
| $\lambda(t)$ | translation unitary, $(\lambda(t)\xi)(q)=\xi(q-t)$, hence $\lambda(t)=e^{-itP}$ |
| $\mathcal{M} \rtimes_\alpha \mathbb{R}$ | crossed product |
| $\hat{\mathcal{M}}$ or $\hat{\mathcal{M}}_\omega$ | modular crossed product $\mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R}$ |
| $r$ | parameter of the dual action |
| $\theta_r$ | dual action, implemented by $e^{irQ}$ in the $q$-representation |
| $\hat\tau$ | faithful normal semifinite trace on the crossed product |

**Covariance relation:**
$$
\lambda(t)\,\pi_\alpha(a)\,\lambda(t)^* = \pi_\alpha(\alpha_t(a)).
$$

**Dual action:**
$$
\theta_r(\pi_\alpha(a))=\pi_\alpha(a),\qquad
\theta_r(\lambda(t))=e^{irt}\lambda(t).
$$
It acts by a phase in the $q$-representation and by translation in the
$p$-representation. In particular, $g(P)$ is multiplication by $g(p)$ only
after Fourier transformation; it is not multiplication by $g(q)$.

**Dual-action trace scaling:**
$$
\hat\tau \circ \theta_r = e^{-r}\,\hat\tau.
$$

## F.7 Rindler and TFD Symbols

| Symbol | Meaning |
|---|---|
| $\Lambda^{\mathrm{boost}}(s)$ | Lorentz boost in $(x^0, x^1)$ plane by rapidity $s$ |
| $K$ | boost generator, $U(\Lambda^{\mathrm{boost}}(u))=e^{iuK}$ |
| $u$ | boost rapidity; for the right wedge, $u=2\pi t$ |
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
| $S_{\hat\tau}(h)=-\hat\tau(h\log h)$ | entropy of a normal state with density $h$ relative to the fixed semifinite trace $\hat\tau$ |
| $S_{\mathrm{gen}}$ | generalized entropy in gravity (only in holographic settings) |
| $\mathcal{B}(\omega, \phi)$ | modular boundary term |

**Finite-dimensional identity** (Week 14 Theorem 3.1; explicit derivation in §4.4):
$$
S(\rho) - S(\sigma) = -S(\rho\|\sigma) + \mathrm{Tr}((\rho - \sigma)\,K_\sigma),
\qquad K_\sigma = -\log\sigma.
$$
Thus, in the finite-dimensional model,
$$
S(\rho_\omega)-S(\rho_\phi)
=-S(\rho_\omega\|\rho_\phi)+\mathcal B(\omega,\phi),
\qquad
\mathcal B(\omega,\phi)=\omega(K_\phi)-\phi(K_\phi).
$$
The boundary term uses the modular Hamiltonian of the reference state
$\phi$, not that of $\omega$. A corresponding core statement requires a
fixed trace, a specified lift of both states to that core, and the appropriate
density-domain hypotheses; it is not an identity for arbitrary type-III state
pairs.

**Trace rescaling.** If $\hat\tau'=c\hat\tau$ and the same normalized state
has density $h'=h/c$, then
$$
S_{\hat\tau'}(h')=S_{\hat\tau}(h)+\log c.
$$

**Type-I weighted-trace check.** For
$$
\hat\tau(a\otimes f)=\operatorname{Tr}(a)
\int_{\mathbb R}f(p)e^{-p}\,dp
$$
and a product probability density $\rho\,\mu(p)$ relative to the flat product
measure, the density relative to $\hat\tau$ is
$h(p)=\rho\mu(p)e^p$. Hence
$$
S_{\hat\tau}(h)
=S(\rho)-\int\mu\log\mu\,dp-\int p\mu(p)\,dp.
$$
The last term is fixed by the non-flat trace; it cannot be omitted or absorbed
into the differential entropy without changing conventions.

**Safe distinctions** (Week 12 §4):
- $S(\omega\|\phi)$: *exact* type-III-safe relative entropy.
- $S_{\hat\tau}(h)$: well-defined for a normal state on a specified
  semifinite algebra once $\hat\tau$ is fixed; rescaling the trace shifts it by
  a state-independent constant.
- $S_{\mathrm{gen}}$: requires the holographic dictionary as additional input.

All three are *distinct controlled objects*, not the same thing.
