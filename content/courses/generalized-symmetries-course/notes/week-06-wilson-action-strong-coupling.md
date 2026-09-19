---
title: "Week 6 — Wilson's Formulation: Compact Groups, Haar Measure, Strong Coupling"
type: lecture-notes
course: syllabus
semester: 1
week: 6
block: B
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 1–5; representation theory of U(1) and SU(2) (characters); Gaussian and group integrals
modified: 2026-07-01
---

# Week 6 — Wilson's Formulation: Compact Groups, Haar Measure, Strong Coupling

> *Wegner's ℤ₂ taught the structure; Wilson's compact-group version is the real thing — the lattice regulator of QED and QCD. The new technical content is a single, powerful idea: integrate over the group with its invariant (Haar) measure, expand the Boltzmann weight in characters, and the strong-coupling series becomes a bookkeeping of tiled surfaces. Confinement drops out for free at strong coupling, for any compact group. Whether it survives to the continuum is the question that separates $U(1)$ (it does not) from $SU(N)$ (we believe it does).*

## 0. Reading

**Primary:** Wilson, *Phys. Rev. D* 10 (1974) 2445 — the founding paper; §§1–3. Kogut, *Rev. Mod. Phys.* 51 (1979) 659, §VII (strong coupling and the character expansion).

**Secondary:**
- Creutz, *Quarks, Gluons and Lattices* — the standard monograph; chs. on strong coupling and Monte Carlo.
- Montvay & Münster, *Quantum Fields on a Lattice*, §§3, 6 — careful character-expansion technology.

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]].

## 1. The Wilson action for compact groups

Replace the ℤ₂ link variable by an element of a compact Lie group $G$ (we take $G = U(1)$ or $SU(N)$). A **link variable** $U_\ell \in G$ is the parallel transport along $\ell$; under a gauge transformation $g_x\in G$ at the sites,
$$
U_\ell \to g_x\, U_\ell\, g_y^{-1},\qquad \ell = (x\to y).
$$
The smallest gauge-invariant object is the **plaquette holonomy** $U_P = \prod_{\ell\in\partial P} U_\ell$ (ordered around the plaquette), and its trace is gauge-invariant. **Wilson's action**:
$$
\boxed{\ S = -\frac{\beta}{N}\sum_P \operatorname{Re}\operatorname{tr} U_P,\qquad \beta = \frac{2N}{g^2}.\ }
$$
Expanding $U_P = e^{i a^2 F_{\mu\nu} + \cdots}$ for smooth fields recovers $\frac{1}{4}\int \operatorname{tr} F^2$ in the continuum limit (Problem 1), so this is genuinely a lattice gauge theory. For $U(1)$, $U_P = e^{i(d a)_P}$ and $S = -\beta\sum_P\cos(da)_P$ — the compact Maxwell action, a gauge-field cousin of the XY model.

The partition function integrates each link over $G$ with the **Haar measure** $dU_\ell$ (the unique left- and right-invariant normalized measure):
$$
Z = \Big(\prod_\ell \int_G dU_\ell\Big)\, e^{-S}.
$$
No gauge-fixing is needed — Haar invariance makes the integral finite and gauge-invariant, exactly as in Wegner's ℤ₂. Elitzur's theorem ([[week-05-wegner-z2-gauge-theory|Week 5]]) holds verbatim: local gauge-variant operators vanish, and the observables are Wilson loops.

## 2. Haar integration and orthogonality

The engine of strong coupling is a handful of exact integrals. Let $d_r$ be the dimension and $\chi_r$ the character of an irreducible representation $r$.

**Orthogonality of matrix elements [Stated — refs: Peter–Weyl].**
$$
\int_G dU\, U_{ij} = 0,\qquad \int_G dU\, (U)_{ij}\,(U^\dagger)_{kl} = \frac{1}{N}\,\delta_{il}\,\delta_{jk}\quad(\text{fundamental of } SU(N)/U(N)).
$$
**Orthogonality of characters.**
$$
\int_G dU\, \chi_r(U)\,\overline{\chi_s(U)} = \delta_{rs}.
$$
The first line says: a single link integrates to zero unless the group elements on it are "paired" into an invariant. The second says characters are an orthonormal basis of class functions — the basis in which the Boltzmann weight wants to be expanded.

**The graded rule to remember:** an integral over a link $U_\ell$ vanishes unless every representation carried by $U_\ell$ is cancelled by a conjugate one. Strong coupling is the combinatorics of arranging those cancellations.

## 3. The character expansion

Because $e^{-S}$ is a class function of each $U_P$, it expands in characters:
$$
e^{\frac{\beta}{N}\operatorname{Re}\operatorname{tr} U_P} = c_0(\beta)\Big[1 + \sum_{r\neq 0} d_r\, \tilde c_r(\beta)\,\chi_r(U_P)\Big],
$$
with coefficients $\tilde c_r(\beta)$ that are small at small $\beta$. This is the exact analogue of the Jacobi–Anger expansion $e^{\beta\cos\phi} = \sum_n I_n(\beta)e^{in\phi}$ of [[week-01-compact-variables-xy-model|Week 1]] — indeed for $U(1)$ it *is* that expansion, with $\tilde c_n(\beta) = I_n(\beta)/I_0(\beta)$.

**Strong coupling** = keep the leading nontrivial representation (the fundamental, for a fundamental Wilson loop) and count. The coefficients:
- $U(1)$: $\tilde c_1(\beta) = I_1(\beta)/I_0(\beta) \approx \beta/2$ at small $\beta$.
- $SU(N)$: the fundamental coefficient $\tilde c_f(\beta) \approx \dfrac{\beta}{2N^2}$ at small $\beta$.

## 4. The area law and the string tension [Computed.]

Compute the fundamental Wilson loop $\langle W(C)\rangle = \frac{1}{N}\langle \operatorname{tr}\prod_{\ell\in C}U_\ell\rangle$ at strong coupling.

Each link on $C$ carries one fundamental index that must be cancelled by the Haar rule (§2). The only source of a conjugate factor is a plaquette from the character expansion sharing that link. So every link of $C$ must be "covered" by a plaquette, and — propagating inward — the plaquettes must **tile a surface spanning $C$**. Each tiling plaquette costs one factor $\tilde c_f(\beta)$. The minimal surface has area $\mathrm{Area}(C)$ (in plaquette units), giving
$$
\boxed{\ \langle W(C)\rangle \simeq \big(\tilde c_f(\beta)\big)^{\mathrm{Area}(C)} = e^{-\sigma_{\text{str}}\,\mathrm{Area}(C)},\qquad \sigma_{\text{str}} = -\ln \tilde c_f(\beta).\ }
$$
Explicitly,
$$
\sigma_{\text{str}}^{U(1)} = -\ln\frac{I_1(\beta)}{I_0(\beta)} \approx -\ln\frac{\beta}{2},\qquad
\sigma_{\text{str}}^{SU(N)} \approx -\ln\frac{\beta}{2N^2}\quad(\text{small }\beta).
$$
**Confinement is generic at strong coupling for every compact group.** A static quark–antiquark pair feels a linearly rising potential $V(R) = \sigma_{\text{str}} R$; the flux between them is squeezed into a string.

### 4.1 Corrections and the roughening transition

The next terms decorate the minimal surface with bumps and handles (Problem 2), organizing into a convergent series with a finite radius of convergence in $\beta$. At a coupling below the deconfinement transition the series hits the **roughening transition**: the interface (the flux sheet) delocalizes and the naive "smooth string" expansion reorganizes, though confinement persists. [Stated — refs: Kogut §VII.]

> **Physical picture.** The strong-coupling area law is confinement *made trivial* — it costs one factor of a small number per unit area of flux sheet, so large loops are exponentially suppressed. The subtlety is entirely at weak coupling. For $U(1)$ in 4d the small-$\beta$ area law does **not** continue to the continuum: at large $\beta$ the theory is in a **Coulomb phase** with a massless photon and deconfined charges ([[week-08-dual-variables-abelian-gauge|Week 8]] and Block C). For $SU(N)$ in 4d, asymptotic freedom means weak lattice coupling is the continuum limit, and the expectation — unproven, but supported by Monte Carlo — is that strong and weak coupling are **analytically connected**, so confinement is permanent. The area law you compute in five lines at strong coupling is, for QCD, the real thing.

## 5. Worked one-link integrals [Computed.]

**$U(1)$.** With $U_\ell = e^{i\theta_\ell}$, $\int_0^{2\pi}\frac{d\theta}{2\pi} e^{in\theta} = \delta_{n,0}$. A link integrates to zero unless the net $U(1)$ charge on it vanishes — the abelian version of the pairing rule. This is why the $U(1)$ Wilson loop needs a tiled surface: the surface supplies, plaquette by plaquette, the charges that neutralize each loop link.

**$SU(2)$.** Characters $\chi_j$, fundamental $j=\tfrac12$ with $\chi_{1/2}(U) = \operatorname{tr} U$. Using $\chi_{1/2}\cdot\chi_{1/2} = \chi_0 + \chi_1$ and $\int dU\,\chi_j = \delta_{j0}$:
$$
\int dU\,\chi_{1/2}(U) = 0,\qquad \int dU\,\chi_{1/2}(U)^2 = 1,\qquad \int dU\, U_{ij}(U^\dagger)_{kl} = \tfrac12\delta_{il}\delta_{jk}.
$$
The last integral is the $N=2$ case of the Peter–Weyl formula and is the elementary "plaquette covers a link" move in the $SU(2)$ area-law computation.

## 6. The handoff to Monte Carlo (orientation)

Beyond leading strong coupling the analytic series becomes unwieldy, and quantitative lattice QCD is done by **Monte Carlo** (Creutz, 1980): sample gauge configurations with weight $e^{-S}$ and measure Wilson loops directly. The string tension is extracted from **Creutz ratios**
$$
\chi(I,J) = -\ln\frac{W(I,J)\,W(I-1,J-1)}{W(I,J-1)\,W(I-1,J)} \xrightarrow{\text{large }I,J} \sigma_{\text{str}},
$$
in which the perimeter and corner contributions cancel and the pure area law survives. This course stays analytic — we use the lattice for exact dualities and clean phase structure, not for numbers — but it is worth knowing where the five-line area law connects to the quantitative program.

## 7. What to take away

1. **Wilson's action is compact Maxwell/Yang–Mills on a lattice.** Link variables in $G$, plaquette holonomies, Haar measure, no gauge fixing; Elitzur still forbids local order parameters.
2. **Haar orthogonality + character expansion = strong coupling.** A link integrates to zero unless its representations are paired; the Boltzmann weight expands in characters with small coefficients $\tilde c_r(\beta)$.
3. **The area law is a tiled surface.** $\langle W(C)\rangle \simeq \tilde c_f(\beta)^{\mathrm{Area}}$, $\sigma_{\text{str}} = -\ln\tilde c_f(\beta)$: generic confinement at strong coupling for any compact group.
4. **The continuum caveat is everything.** $U(1)$ in 4d deconfines at weak coupling (Coulomb phase); $SU(N)$ is believed to confine permanently by analytic continuation from strong coupling — the physical payoff, and the reason the lattice matters for QCD.

## 8. Looking ahead: Week 7

We have the Euclidean (Lagrangian) picture. Week 7 takes the anisotropic (time-continuum) limit of the transfer matrix to reach the **Kogut–Susskind Hamiltonian**: link rotors, the electric field as their conjugate momentum, the **Gauss law** as an operator constraint, and physical states as closed electric strings. The ℤ₂ Kogut–Susskind Hamiltonian will turn out to be the toric code, one renaming away — planted there on purpose for Semester II.

## 9. Problem set

**Core problems** (everyone).

**1. Continuum limit.**
Expand $U_P = \exp(i a^2 F_{\mu\nu} + \cdots)$ for a smooth field and show $-\frac{\beta}{N}\operatorname{Re}\operatorname{tr} U_P \to \text{const} + \frac{1}{4g^2}\int \operatorname{tr} F_{\mu\nu}^2$ with $\beta = 2N/g^2$. Identify the leading lattice artifact.

**2. String tension, leading and subleading.**
(a) Derive $\sigma_{\text{str}} = -\ln\tilde c_f(\beta)$ for $U(1)$ and $SU(2)$ and give the small-$\beta$ forms.
(b) Compute the first correction from decorating the minimal surface (a single displaced plaquette); estimate where the smooth-string expansion starts to fail (roughening).

**3. Haar integrals.**
(a) Verify $\int dU\, U_{ij}(U^\dagger)_{kl} = \frac{1}{N}\delta_{il}\delta_{jk}$ for $SU(2)$ using characters.
(b) Compute $\int dU\, \chi_{1/2}(U)^4$ for $SU(2)$ and interpret the result as counting the ways four fundamentals fuse to a singlet.

**Starred problems.**

**4⋆. Character coefficients.**
Compute $\tilde c_r(\beta)$ for the first two representations of $\mathbb{Z}_N$, $U(1)$, and $SU(2)$, and show the $U(1)$ result reproduces the Bessel ratios $I_n/I_0$ of Week 1. Explain why the fundamental dominates the area law and when a higher representation ("$k$-string") competes.

**5⋆. Casimir scaling of $k$-strings.**
For an $SU(N)$ Wilson loop in representation $r$, show the strong-coupling string tension scales with the quadratic Casimir $C_2(r)$ at leading order. Comment on whether this "Casimir scaling" is expected to survive to the continuum, and what it would say about the confining string.

**6⋆⋆ (optional).**
Set up the strong-coupling expansion for the **Polyakov loop** (a Wilson line wrapping the Euclidean time circle) at finite temperature, and show its expectation is an order parameter for center symmetry — nonzero (deconfined) at high $T$, zero (confined) at low $T$. This anticipates the center-symmetry / 1-form-symmetry reading of confinement in Semester II.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block B. Last revised 2026-07-01.*
