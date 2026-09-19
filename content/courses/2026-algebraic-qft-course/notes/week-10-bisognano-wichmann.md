---
title: "Week 10 — The Bisognano–Wichmann Theorem"
type: lecture-notes
course: syllabus
semester: 1
week: 10
block: C
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 5–9 (Tomita–Takesaki + Reeh–Schlieder + Weyl algebras)
modified: 2026-06-11
---

# Week 10 — The Bisognano–Wichmann Theorem

> *Reeh–Schlieder told us that every local algebra in a Wightman QFT has a canonical modular operator with respect to the vacuum — an **existence** statement: $\Delta$ exists for every $\mathcal{A}(\mathcal{O})$. Bisognano–Wichmann is the rare **constructive** complement: for a **Rindler wedge**, $\Delta$ is **known explicitly**. It is the exponentiated Lorentz boost generator. Modular flow is a geometric symmetry of spacetime. This is the only general theorem in physics in which the modular operator can be written down without further input, and it is the algebraic content of the Unruh effect. Every Sem II mini-calculation eats this fact.*

## 0. Reading

**Primary:**
- Bisognano & Wichmann, "On the duality condition for a Hermitian scalar field," *J. Math. Phys.* 16 (1975) 985; "On the duality condition for quantum fields," *J. Math. Phys.* 17 (1976) 303 (the original two papers).
- Haag, *Local Quantum Physics*, ch. V §4 (the modular geometry of wedges; standard reference).

**Secondary:**
- Borchers, "On revolutionizing quantum field theory with Tomita's modular theory," *J. Math. Phys.* 41 (2000) 3604 — clean modernized exposition.
- Sewell, "Quantum fields on manifolds: PCT and gravitationally induced thermal states," *Ann. Phys.* 141 (1982) 201 (curved-space generalization; foundational for the algebraic Unruh effect).
- Summers, "Yet more ado about nothing: the remarkable relativistic vacuum state," arXiv:0802.1854, §4–5 (philosophical/structural review).

**Optional research reading:**
- Hislop & Longo, "Modular structure of the local algebras associated with the free massless scalar field theory," *Comm. Math. Phys.* 84 (1982) 71 (extension to double cones in 2D conformal theories — the one bounded-region case where modular flow is geometric).
- Brunetti, Guido, Longo, "Modular structure and duality in conformal quantum field theory," *Comm. Math. Phys.* 156 (1993) 201 (higher-dim conformal generalization).
- Crispino, Higuchi, Matsas, "The Unruh effect and its applications," *Rev. Mod. Phys.* 80 (2008) 787 (physics review).

## 1. Statement

### 1.1 Setup

Let $\mathcal{A}(W_R)$ be the local von Neumann algebra of the right Rindler wedge in a Wightman QFT on Minkowski space $\mathbb{R}^{1,d}$ (we mostly think of $d = 1$ or $d = 3$ in the worked computations), where
$$
W_R = \{x \in \mathbb{R}^{1,d}: x^1 > |x^0|\}.
$$
$W_R$ is the causal closure of the worldline of an observer uniformly accelerated in the $x^1$ direction. It is bounded by the two null half-planes $x^0 = x^1$ ($x^1 > 0$) and $x^0 = -x^1$ ($x^1 > 0$), and intersects every Cauchy surface in a half-space.

Let $\Lambda^{\mathrm{boost}}(s)$ denote the one-parameter family of Lorentz boosts in the $(x^0, x^1)$-plane (with $\vec x_\perp = (x^2, \ldots, x^d)$ fixed):
$$
\Lambda^{\mathrm{boost}}(s):\;\; \begin{pmatrix}x^0 \\ x^1\end{pmatrix} \mapsto \begin{pmatrix}\cosh s & \sinh s \\ \sinh s & \cosh s\end{pmatrix}\begin{pmatrix}x^0 \\ x^1\end{pmatrix}, \quad x^j \mapsto x^j \text{ for } j \ge 2.
$$
This subgroup preserves $W_R$ as a set (boosts within the wedge stay within the wedge). The corresponding **boost generator** is the self-adjoint operator
$$
K = \int_{x^1 > 0} x^1\, T^{00}(0, \vec x)\, d\vec x \;-\; \int_{x^1 < 0} (-x^1)\, T^{00}(0, \vec x)\, d\vec x,
$$
where $T^{\mu\nu}$ is the stress–energy tensor (a quadratic operator-valued distribution in the field), and the unitary implementer of the boost subgroup is $U(\Lambda^{\mathrm{boost}}(s)) = e^{-isK}$.

Two properties of $K$ that we will use:
- **Vacuum annihilation:** $K\Omega = 0$. (Boosts fix the vacuum since the vacuum is Poincaré-invariant.)
- **Full real spectrum on the whole Hilbert space:** $\sigma(K) = \mathbb{R}$. (Boosts mix positive- and negative-energy states; $K$ is unbounded both above and below.)

Let $J^{\mathrm{wedge}}$ denote the geometric transformation
$$
J^{\mathrm{wedge}}:\;\; (x^0, x^1, \vec x_\perp) \mapsto (-x^0, -x^1, \vec x_\perp),
$$
i.e., reflection through the edge of the wedge $\{x^0 = x^1 = 0\}$. This has $\det = +1$ in $d \ge 2$ but is **not** connected to the identity in $\mathcal{P}_+^\uparrow$ (it reverses time). On a Wightman QFT satisfying the PCT theorem, the combination of $J^{\mathrm{wedge}}$ with a rotation in the perpendicular directions is implemented by the antiunitary CPT operator.

### 1.2 The theorem

**Theorem 1.1 (Bisognano–Wichmann). [Stated only — refs: Bisognano–Wichmann 1975, 1976; Borchers 2000 for the modernized proof.]** *Assume the Haag–Kastler axioms plus the Wightman framework (tempered fields, vacuum cyclicity, spectral condition, locality, covariance, PCT). For the local vN algebra $\mathcal{A}(W_R)$ of a right Rindler wedge, the modular operator and modular conjugation of the vacuum are*
$$
\boxed{\Delta_{W_R} = e^{-2\pi K}}
$$
*and*
$$
\boxed{J_{W_R} = \Theta \cdot R_\perp(\pi)},
$$
*where $\Theta$ is the antiunitary CPT operator and $R_\perp(\pi)$ is a $\pi$-rotation in the $(x^2, \ldots, x^d)$ plane (trivial in 2D where there are no perpendicular directions). In our upper-strip convention (Week 6), the modular flow on $\mathcal{A}(W_R)$ is*
$$
\sigma_t^{W_R}(a) \;=\; \Delta_{W_R}^{-it}\, a\, \Delta_{W_R}^{it} \;=\; U(\Lambda^{\mathrm{boost}}(2\pi t))\, a\, U(\Lambda^{\mathrm{boost}}(2\pi t))^*.
$$
*The modular conjugation maps $\mathcal{A}(W_R)$ onto $\mathcal{A}(W_L)$.*

> **Physical picture: why $2\pi$ — the Euclidean angle.** There is a geometric way to see the whole theorem at once. Wick-rotate Minkowski time: $x^0 = -i x_E^0$. The boost subgroup $\Lambda^{\mathrm{boost}}(s)$ analytically continues to *rotations* in the Euclidean $(x_E^0, x^1)$-plane, with rapidity becoming angle: $s = -i\theta$. The wedge $W_R$ continues to the half-plane $\{x^1 > 0\}$, and the entangling edge $x^0 = x^1 = 0$ becomes the rotation axis. Now read off the modular objects: $\Delta^{1/2} = e^{-\pi K}$ is the boost with imaginary rapidity $-i\pi$ — a Euclidean rotation by angle $\pi$, which carries the right half-plane onto the left. That is exactly the Tomita operator's job: $S = J\Delta^{1/2}$ flips an operator into the commutant ($\Delta^{1/2}$ rotates it to the other wedge, $J$ reflects it back with conjugation). And the *full* thermal period is the rotation by $2\pi$ — once around the entangling surface — which is why the KMS strip width, in boost rapidity, is exactly $2\pi$: the smoothness of the Euclidean vacuum at the origin (no conical singularity) *is* the statement that the Minkowski vacuum is thermal at $\beta_{\rm rapidity} = 2\pi$. Every Euclidean path-integral derivation of the Unruh and Hawking temperatures is this picture; Bisognano–Wichmann is its operator-theoretic theorem form, valid without any path integral.

**Reading the formula.** The factor of $2\pi$ in the exponent is not an artifact — it is the algebraic shadow of the Unruh temperature. The relation $\Delta = e^{-2\pi K}$ means that **modular time $t$ corresponds to the boost subgroup at rapidity $2\pi t$**. An observer with proper acceleration $a$ has proper time $\tau$ related to boost rapidity by $s = a\tau$ (the trajectory $x^1 = (1/a)\cosh(a\tau), x^0 = (1/a)\sinh(a\tau)$), so modular time $t$ corresponds to proper time $\tau = 2\pi t / a$. The KMS condition at modular $\beta = 1$ (Week 6) translates into KMS for the accelerated observer at inverse proper-time temperature $\beta_{\text{proper}} = 2\pi/a$, i.e., physical temperature $T_U = a/(2\pi)$. This is the Unruh effect.

### 1.3 Three immediate consequences

**(a) The Unruh effect, made algebraic.** Theorem 1.1 directly implies that the Minkowski vacuum, viewed as a state on $\mathcal{A}(W_R)$, satisfies KMS at the Unruh temperature for the boost flow. Concretely, an accelerated observer's two-point function for any wedge-localized observable thermalizes:
$$
\langle 0_M|\, A(x_1)\, A(x_2)\, |0_M\rangle \;\xrightarrow{\;\text{boost parametrization}\;}\; \frac{1}{e^{\beta_{\text{proper}}(\tau_1-\tau_2-i\epsilon)} - 1}\,\text{(times spectral data)}.
$$
The original Unruh argument (mode decomposition + Bogoliubov + thermal occupation, §4 below) is one way to *see* this. The algebraic Bisognano–Wichmann statement is **structurally stronger**: it says that the thermal character is the modular structure of the wedge algebra, regardless of which specific QFT one is in (free, interacting, conformal, …), as long as the Wightman axioms hold.

**(b) Haag duality for wedges.** Bisognano–Wichmann implies $J_{W_R}\,\mathcal{A}(W_R)\,J_{W_R}^{-1} = \mathcal{A}(W_L)$ (geometric, via CPT-plus-rotation acting as $J^{\mathrm{wedge}}$ on test functions). Combined with the Tomita commutant theorem $J\mathcal{A}(W_R)J = \mathcal{A}(W_R)'$ (Week 5 §4), this gives the geometric Haag duality
$$
\mathcal{A}(W_R)' \;=\; \mathcal{A}(W_L) \;=\; \mathcal{A}(W_R').
$$
**Bisognano–Wichmann is therefore the proof of Haag duality for wedges in Wightman QFT.** It is not just a statement about the modular operator; it is the structural locality result for wedge-shaped regions.

**(c) Modular flow is geometric — and unique to wedges.** The wedge is, up to Hislop–Longo's conformal extension, the **only** region for which the modular flow of the vacuum is a spacetime symmetry. For a bounded **double cone** in a 2D massless free scalar (which is conformally invariant), Hislop–Longo show that the modular flow is the one-parameter family of conformal transformations preserving the double cone. For non-conformal theories on bounded regions, the modular flow exists (Reeh–Schlieder + Tomita–Takesaki) but is **not** a geometric flow — it is a more abstract automorphism with no spacetime interpretation. This is the structural mystery the course will not resolve; it motivates much of the recent work on algebraic gravity and entanglement.

## 2. Proof strategy: what we do and what we don't

The full Bisognano–Wichmann proof is technically demanding (originally ~25 pages each in the 1975 and 1976 papers, with substantial Wightman-analyticity prerequisites). It builds on:
- **Wightman analyticity** of the $n$-point functions in tube domains (forward-tube holomorphy from the spectral condition);
- **Reeh–Schlieder** (Week 9) supplying cyclicity of the vacuum for $\mathcal{A}(W_R)$;
- **The Lüders–Pauli theorem** or its equivalents: spectral properties of the Poincaré group representation on Hilbert space;
- **The PCT theorem** (Jost; Wightman): to identify the antiunitary $J_{W_R}$ as $\Theta \cdot R_\perp(\pi)$.

The full proof shows that the operator $J_0 \Delta_0^{1/2}$ defined by the Tomita procedure on $\mathcal{A}(W_R)\Omega$ — *a priori* unknown abstractly — coincides with the closure of $a\,\Omega \mapsto (\Theta R_\perp(\pi)\, e^{-\pi K}\, a)\,\Omega$, by exploiting the analytic structure of $K$ on the dense domain of analytic vectors. **[Stated only — for the full proof: Bisognano–Wichmann 1975, 1976; Borchers 2000 §3 for a streamlined modern treatment.]**

What we **do** in this lecture:

1. **Plausibility (§3):** establish that the boost flow is the *unique* candidate for the modular flow consistent with KMS at the Unruh temperature, via Takesaki uniqueness.
2. **Explicit verification in the 2D massless free scalar (§§4–5):** compute the Bogoliubov transformation between Minkowski and Rindler modes, verify thermal occupation at $\beta = 2\pi$, and read off the modular operator.
3. **Modular flow on Weyl operators (§6):** identify $\sigma_t^{W_R}$ as a geometric boost on test-function supports.
4. **Modular conjugation via PCT (§7):** unpack the antiunitary structure.
5. **Failure of geometric modular flow beyond wedges (§8):** discuss why double cones and balls require conformal invariance to retain geometric modular flow, and what changes for general bounded regions.

## 3. Plausibility: KMS at the Unruh temperature

### 3.1 The thermal argument

Before any explicit calculation, the result is plausible from a thermal argument. Consider a uniformly accelerated observer in $W_R$, with worldline $x^1 = (1/a)\cosh(a\tau)$, $x^0 = (1/a)\sinh(a\tau)$. Their proper time is $\tau$; their proper acceleration is $a$; their natural "time translation" is the Lorentz boost subgroup parametrized by $s = a\tau$. The boost subgroup preserves $W_R$, so it acts as an automorphism on $\mathcal{A}(W_R)$.

If the Minkowski vacuum is to look thermal to this observer, the algebra $\mathcal{A}(W_R)$ must satisfy a KMS condition for the boost flow, at some specific inverse temperature. The Unruh argument (mode decomposition, Bogoliubov, thermal occupation) — which we will reproduce in §4 below — gives
$$
T_U = \frac{a}{2\pi}, \qquad \beta_{\text{proper}} = \frac{2\pi}{a}.
$$
Rescaling proper time into modular time by $t = s/(2\pi) = a\tau/(2\pi)$, the KMS condition becomes $\beta_{\text{modular}} = 1$.

### 3.2 Takesaki uniqueness fixes the modular flow

By Takesaki's uniqueness theorem (Week 6 Theorem 2.2): *the modular flow is the unique one-parameter automorphism group for which a given faithful normal state is KMS at $\beta = 1$* (in our convention). Reeh–Schlieder (Week 9) tells us the vacuum is faithful normal on $\mathcal{A}(W_R)$. So **if** the boost flow makes the vacuum KMS at $\beta_{\text{modular}} = 1$, then the boost flow **must** be the modular flow.

This is the structural content of Bisognano–Wichmann: it asserts that the boost flow does make the vacuum KMS at modular $\beta = 1$, and by uniqueness deduces $\Delta_{W_R} = e^{-2\pi K}$.

### 3.3 Why this is non-obvious

The argument above might suggest Bisognano–Wichmann is a "trivial corollary" of Unruh and uniqueness. It isn't, for two reasons:

1. **Unruh's mode argument is theory-specific** (free fields, specific modes). Bisognano–Wichmann is **theory-agnostic**: it holds under the Wightman axioms alone, including for interacting theories.
2. **Verifying KMS for the boost flow is non-trivial.** The KMS condition requires a particular *analytic continuation* of vacuum two-point functions of wedge-localized observables to a strip in modular time. The original Bisognano–Wichmann proof shows this analyticity holds for *any* Wightman field, via the spectral condition. This is the content of the proof we skip.

So the plausibility argument identifies the right **candidate**; the full theorem verifies the candidate **works** in any Wightman QFT.

## 4. Rindler coordinates and explicit verification (2D massless)

### 4.1 Rindler coordinates

On $W_R = \{x^1 > |x^0|\}$, introduce **Rindler coordinates** $(\eta, \xi)$:
$$
x^1 = \xi \cosh\eta, \qquad x^0 = \xi \sinh\eta, \qquad \xi > 0,\; \eta \in \mathbb{R}.
$$
These cover $W_R$ smoothly. The metric in Rindler coordinates is
$$
ds^2 = -\xi^2\,d\eta^2 + d\xi^2 + d\vec x_\perp^2,
$$
so $\eta$ is a "time" coordinate with $g_{\eta\eta} = -\xi^2$ (lapse $\xi$). The boost subgroup acts by $\eta \mapsto \eta + s$, leaving $\xi$ fixed.

An observer at fixed $\xi = \xi_0$ has worldline $x^\mu(\tau) = (\xi_0 \sinh(\tau/\xi_0), \xi_0\cosh(\tau/\xi_0))$ — a hyperbola with proper time $\tau = \xi_0\eta$ and proper acceleration $a = 1/\xi_0$. For these observers, Rindler time and proper time differ by the lapse:
$$
\tau = \xi_0\,\eta, \qquad a = 1/\xi_0.
$$

We now restrict to 2D ($d = 1$) and massless ($m = 0$) for the rest of §4. The factorization $\phi = \phi_R(x^-) + \phi_L(x^+)$ into right- and left-movers (with $x^\pm = x^0 \pm x^1$) makes the calculation tractable. We focus on the right-moving sector $\phi_R(x^-)$; the left-moving sector $\phi_L(x^+)$ is identical with $x^- \leftrightarrow x^+$.

### 4.2 Minkowski modes

The right-moving sector satisfies $\partial_+ \phi_R = 0$, so $\phi_R$ depends only on $x^-$. The standard Minkowski mode expansion is
$$
\phi_R(x^-) = \int_0^\infty \frac{dk}{\sqrt{4\pi k}}\left[a_k\, e^{-ikx^-} + a_k^\dagger\, e^{ikx^-}\right],
$$
with $[a_k, a_{k'}^\dagger] = \delta(k - k')$ and Minkowski vacuum $a_k|0_M\rangle = 0$. The mode $e^{-ikx^-}$ is positive-frequency with respect to Minkowski time $x^0$ (for $k > 0$, the dependence is $e^{-ik(x^0 - x^1)}$, with $k > 0$ matching the positive-energy half).

### 4.3 Rindler modes

In Rindler coordinates inside $W_R$,
$$
x^- = x^0 - x^1 = \xi(\sinh\eta - \cosh\eta) = -\xi\, e^{-\eta}.
$$
A right-moving wave $e^{-ikx^-} = e^{ik\xi e^{-\eta}}$ depends on $\xi$ and $\eta$ in an entangled way; it is *not* a Rindler-positive-frequency mode.

Define **Rindler right-moving modes**, positive-frequency with respect to Rindler time $\eta$:
$$
u_\omega^R(\eta) := \frac{1}{\sqrt{4\pi\omega}}\, e^{-i\omega\eta}, \qquad \omega > 0.
$$
These are functions of $\eta$ only; the corresponding $\xi$-dependence drops out because we are on a fixed-$\xi$ Rindler trajectory (or equivalently we are working with the lightcone field $\phi_R(x^-)$ in the variable $x^- = -\xi e^{-\eta}$, where $\xi$ only contributes a $\eta$-independent phase under change of variables).

The Rindler-mode expansion of $\phi_R$ restricted to $W_R$ is
$$
\phi_R\big|_{W_R}(\eta) = \int_0^\infty d\omega\,\left[b_\omega^R\, u_\omega^R(\eta) + (b_\omega^R)^\dagger\, u_\omega^{R*}(\eta)\right],
$$
with $[b_\omega^R, b_{\omega'}^{R\dagger}] = \delta(\omega - \omega')$. The **Rindler vacuum** $|0_R\rangle$ is defined by $b_\omega^R |0_R\rangle = 0$ for all $\omega > 0$.

A parallel construction inside $W_L$ gives left-Rindler operators $b_\omega^L$ and a vacuum $|0_L\rangle$. The combined Rindler vacuum on the full Minkowski Hilbert space (restricted to $W_R \cup W_L$) is the product $|0_R\rangle \otimes |0_L\rangle$.

**Key fact:** $|0_M\rangle \neq |0_R\rangle \otimes |0_L\rangle$. They are physically distinct vacua. The Bogoliubov transformation between them is the entire content of the Unruh derivation.

### 4.4 The Bogoliubov transformation

To express $b_\omega^R$ in terms of $a_k, a_k^\dagger$, take the overlap of the two mode functions. Concretely, in the variable $u := \xi$ (positive real) the Minkowski mode $e^{-ikx^-} = e^{iku}$ has a known expansion in Rindler modes via the **Mellin transform**:
$$
e^{iku} = \int_{-\infty}^\infty \frac{d\omega}{2\pi}\, e^{i\omega \log(ku)}\, \Gamma(-i\omega)\, (-i)^{-i\omega},
$$
valid in a suitable distributional sense. Splitting into $\omega > 0$ (Rindler-positive) and $\omega < 0$ (Rindler-negative) parts and matching coefficients gives:
$$
b_\omega^R = \int_0^\infty dk\,\left[\alpha_{\omega k}\, a_k + \beta_{\omega k}\, a_k^\dagger\right],
$$
where the **Bogoliubov coefficients** are
$$
\alpha_{\omega k} = \frac{1}{2\pi}\sqrt{\frac{\omega}{k}}\,\Gamma(i\omega)\,k^{-i\omega}\, e^{+\pi\omega/2}, \qquad \beta_{\omega k} = \frac{1}{2\pi}\sqrt{\frac{\omega}{k}}\,\Gamma(i\omega)\,k^{-i\omega}\, e^{-\pi\omega/2}.
$$
The crucial structural feature is the **ratio**
$$
\frac{|\beta_{\omega k}|^2}{|\alpha_{\omega k}|^2} = e^{-2\pi\omega}.
$$
This $e^{-2\pi\omega}$ is the thermal Boltzmann factor at temperature $T = 1/(2\pi)$ in Rindler units; reinstating the lapse $\xi_0$ to get proper time gives $T_U = a/(2\pi)$ in physical units, as anticipated.

*Where the factor really comes from: analyticity across the horizon.* The cleanest derivation of the $e^{\pm\pi\omega/2}$ asymmetry (Unruh's original trick) avoids the Mellin integral entirely. A Minkowski positive-frequency function of $x^-$ is the boundary value of a function holomorphic in the **lower half** complex-$x^-$ plane (because $e^{-ikx^-}$ with $k>0$ decays there). A Rindler mode behaves as $(-x^-)^{i\omega}$ inside $W_R$ ($x^- < 0$) and $(x^-)^{i\omega}$ in $W_L$ ($x^- > 0$). To assemble a globally Minkowski-positive-frequency combination one must continue $(-x^-)^{i\omega}$ through the lower half plane to positive $x^-$, and the branch point at $x^- = 0$ — the horizon — produces the relative weight $|e^{i\omega\log(-1)}| = e^{-\pi\omega}$ on the far side. So the Boltzmann factor is the monodromy of $x^{i\omega}$ around the horizon point, with the *direction* of continuation (lower half plane) dictated by the spectral condition. The thermal character of the vacuum is, once again, an analyticity statement: positive energy fixes the side on which correlators are holomorphic, and the horizon's branch cut converts that choice into temperature.

### 4.5 Thermal occupation

The expectation value of the Rindler number operator $N_\omega^R := (b_\omega^R)^\dagger b_\omega^R$ in the *Minkowski* vacuum is the central calculation:
$$
\langle 0_M |\,N_\omega^R\, |0_M\rangle \;=\; \int_0^\infty dk\,|\beta_{\omega k}|^2,
$$
where we used $a_k|0_M\rangle = 0$ so only the $|\beta|^2 a_k^\dagger a_k$ term survives. Substituting,
$$
\int_0^\infty dk\,|\beta_{\omega k}|^2 = \int_0^\infty dk\,\frac{\omega}{4\pi^2 k}\,|\Gamma(i\omega)|^2\, e^{-\pi\omega}.
$$
The $k$-integral is logarithmically divergent ($\int dk/k$ from the volume of Rindler space at fixed $\omega$); regulating it by some box-normalization $L$ gives
$$
\langle N_\omega^R\rangle_{0_M} = \frac{\omega}{4\pi^2}\,|\Gamma(i\omega)|^2\, e^{-\pi\omega}\,\log L.
$$
The factor $\log L$ is the volume; per unit volume,
$$
\frac{\langle N_\omega^R\rangle_{0_M}}{\log L} = \frac{\omega}{4\pi^2}\,|\Gamma(i\omega)|^2\, e^{-\pi\omega}.
$$
Using the gamma-function identity $|\Gamma(i\omega)|^2 = \pi/(\omega\sinh\pi\omega)$,
$$
\frac{\omega}{4\pi^2} \cdot \frac{\pi}{\omega\sinh\pi\omega}\cdot e^{-\pi\omega} = \frac{e^{-\pi\omega}}{4\pi\sinh\pi\omega} = \frac{1}{4\pi}\cdot\frac{e^{-\pi\omega}}{\sinh\pi\omega} = \frac{1}{4\pi}\cdot\frac{2}{e^{\pi\omega}(e^{\pi\omega} - e^{-\pi\omega})/e^{-\pi\omega}}.
$$
Simplifying: $\frac{e^{-\pi\omega}}{\sinh\pi\omega} = \frac{2e^{-\pi\omega}}{e^{\pi\omega} - e^{-\pi\omega}} = \frac{2}{e^{2\pi\omega} - 1}$. So per unit volume,
$$
\langle N_\omega^R\rangle_{0_M} \;=\; \frac{1}{2\pi}\cdot\frac{1}{e^{2\pi\omega} - 1}.
$$
This is the **Bose–Einstein distribution at Rindler-frequency inverse temperature $\beta_R = 2\pi$** — the Unruh effect, recovered from the Bogoliubov ratio.

### 4.6 KMS in Rindler time

The thermal occupation translates directly into a KMS condition on the wedge algebra. For Rindler creation/annihilation pairs, the two-point function in the Minkowski vacuum is
$$
\langle 0_M|\, b_\omega^R(\eta_1)\, (b_\omega^R)^\dagger(\eta_2)\,|0_M\rangle \;=\; \frac{e^{-i\omega(\eta_1 - \eta_2)}}{1 - e^{-2\pi\omega}},
$$
$$
\langle 0_M|\, (b_\omega^R)^\dagger(\eta_1)\,b_\omega^R(\eta_2)\,|0_M\rangle \;=\; \frac{e^{-i\omega(\eta_1 - \eta_2)} \cdot e^{-2\pi\omega}}{1 - e^{-2\pi\omega}}.
$$
The ratio of the second to the first is $e^{-2\pi\omega}$, which is the KMS condition at $\beta_R = 2\pi$ for the boost flow $\eta \to \eta + s$ (the Rindler-time translation).

Rescaling Rindler time into modular time by $t = \eta/(2\pi)$, this is the KMS condition at modular $\beta = 1$ of Theorem 1.1.

**We have explicitly verified** in the 2D massless free scalar that:
- the vacuum is KMS at modular $\beta = 1$ for the boost flow on $\mathcal{A}(W_R)$;
- by Takesaki uniqueness, the boost flow **is** the modular flow;
- hence the modular operator is $\Delta_{W_R} = e^{-2\pi K}$ where $K$ is the boost generator.

This is a **model proof** in the Block A sense: the general Bisognano–Wichmann theorem is the statement that the *same* conclusion holds in any Wightman QFT, by analyticity arguments that bypass the mode-by-mode Bogoliubov calculation.

## 5. The modular flow on Weyl operators

Let $f$ be a real test function supported in $W_R$, and consider the Weyl operator $W(f) = e^{i\phi(f)}$ from Week 8. The boost $\Lambda^{\mathrm{boost}}(s)$ acts on test functions by pullback:
$$
(f \circ \Lambda^{\mathrm{boost}}(-s))(x) = f(\Lambda^{\mathrm{boost}}(-s)\,x).
$$
The boost-implementing unitary acts on the smeared field $\phi(f)$ by
$$
U(\Lambda^{\mathrm{boost}}(s))\,\phi(f)\,U(\Lambda^{\mathrm{boost}}(s))^* = \phi(f \circ \Lambda^{\mathrm{boost}}(-s)),
$$
and by exponentiation on the Weyl operator:
$$
U(\Lambda^{\mathrm{boost}}(s))\, W(f)\, U(\Lambda^{\mathrm{boost}}(s))^* = W(f \circ \Lambda^{\mathrm{boost}}(-s)).
$$

Combining with Theorem 1.1, the modular flow on $\mathcal{A}(W_R)$ acts on Weyl operators by
$$
\boxed{\sigma_t^{W_R}(W(f)) \;=\; W\!\big(f \circ \Lambda^{\mathrm{boost}}(-2\pi t)\big).}
$$

This is a **geometric** action on the test function. The modular flow boosts the support of $f$ inside $W_R$, at boost rapidity $-2\pi t$.

### 5.1 Worked example: Gaussian wavelet under modular flow

Take a Gaussian bump $f(x) = c\, e^{-(x^0 - \tau_0)^2/\sigma^2 - (x^1 - s_0)^2/\sigma^2}$ centered at $(\tau_0, s_0) \in W_R$ with width $\sigma$, cut off to lie strictly inside $W_R$. Under the boost $\Lambda^{\mathrm{boost}}(s)$ with $s = -2\pi t$, the center moves:
$$
\begin{pmatrix}\tau_0 \\ s_0\end{pmatrix} \;\mapsto\; \begin{pmatrix}\cosh(-2\pi t)\,\tau_0 + \sinh(-2\pi t)\,s_0 \\ \sinh(-2\pi t)\,\tau_0 + \cosh(-2\pi t)\,s_0\end{pmatrix}.
$$
The width $\sigma$ is preserved (boosts are isometries of Minkowski). So the modular-flowed test function is a Gaussian of the same width centered at a hyperbolic translation of the original center.

**Behaviour at large $|t|$:** as $t \to +\infty$ (boost rapidity $-\infty$), the center moves along a hyperbola toward the past null boundary $x^0 = -x^1, x^1 > 0$ of $W_R$. As $t \to -\infty$, it moves toward the future null boundary $x^0 = x^1, x^1 > 0$. Modular time **never reaches** the wedge boundary in finite $t$ — the modular flow is a "diffeomorphism of the wedge that fixes the boundary at infinity."

This boundary behaviour is the algebraic source of the type III$_1$ structure on $\mathcal{A}(W_R)$: the modular flow has full real spectrum because the boost orbit fills the wedge non-compactly.

### 5.2 The KMS condition spelled out

The KMS condition at $\beta = 1$ for $\sigma^{W_R}$ says: the function
$$
t \mapsto \langle 0_M|\, W(f)\, \sigma_t^{W_R}(W(g))\, |0_M\rangle \;=\; \langle 0_M|\, W(f)\, W(g \circ \Lambda^{\mathrm{boost}}(-2\pi t))\, |0_M\rangle
$$
extends to a holomorphic function on the upper strip $0 \le \mathrm{Im}\,t \le 1$, and at $t \to t + i$ equals
$$
\langle 0_M|\, \sigma_t^{W_R}(W(g))\, W(f)\, |0_M\rangle.
$$
In the free 2D massless case, both sides are computable explicitly from the Gaussian vacuum expectation value formula (Week 8 §4.2) and the symplectic-form integral. The analytic continuation in $t$ corresponds, in Rindler-mode language, to shifting Rindler frequency $\omega$ by $i\omega \to i\omega + 1$ — exactly the Bose–Einstein shift of §4.6.

## 6. Modular conjugation and PCT

The modular conjugation $J_{W_R}$ is more subtle than $\Delta_{W_R}$. By the polar decomposition $S = J\Delta^{1/2}$ (Week 5), $J$ must be **antiunitary** and satisfy $J\mathcal{A}(W_R)J = \mathcal{A}(W_R)'$.

### 6.1 PCT in Wightman QFT

The PCT theorem (Jost 1957; Wightman) states that **any Wightman QFT** admits an antiunitary operator $\Theta$ on Hilbert space that implements the combined symmetry charge-conjugation × parity × time-reversal:
$$
\Theta\,\phi(x)\,\Theta^{-1} = \phi^*(-x), \qquad \Theta\,\Omega = \Omega,
$$
on the field algebra. PCT is a structural feature of relativistic locality: it follows from Lorentz covariance, the spectral condition, and Hermiticity, without further input.

### 6.2 Identifying $J_{W_R}$

Bisognano–Wichmann identifies
$$
J_{W_R} = \Theta \cdot R_\perp(\pi),
$$
where $R_\perp(\pi)$ is a $\pi$-rotation in the $(x^2, \ldots, x^d)$ plane that flips $\vec x_\perp \to -\vec x_\perp$. The combined geometric action of $J_{W_R}$ on a Weyl operator is
$$
J_{W_R}\, W(f)\, J_{W_R}^{-1} = W(f^*),
$$
where $f^*(x^0, x^1, \vec x_\perp) = f(-x^0, -x^1, \vec x_\perp)$ — reflection through the edge of the wedge.

If $f$ is supported in $W_R$, then $f^*$ is supported in $W_L = \{x^1 < -|x^0|\}$. So $J_{W_R}$ maps $\mathcal{A}(W_R)$ to $\mathcal{A}(W_L)$, as required by the Tomita commutant theorem.

### 6.3 The 2D case

In 2D ($d = 1$), there is no perpendicular plane and $R_\perp$ is trivial. So $J_{W_R} = \Theta$ is just CPT. Acting on the 2D massless free scalar with the lightcone decomposition $\phi = \phi_R(x^-) + \phi_L(x^+)$:
$$
\Theta\,\phi_R(x^-)\,\Theta^{-1} = \phi_R(-x^-), \qquad \Theta\,\phi_L(x^+)\,\Theta^{-1} = \phi_L(-x^+).
$$
The map $x^- \to -x^-, x^+ \to -x^+$ is $(x^0, x^1) \to (-x^0, -x^1)$, which swaps $W_R$ and $W_L$. The implementation on Weyl operators is consistent with §6.2.

## 7. Failure of geometric modular flow beyond wedges

For a bounded region $\mathcal{O}$ that is *not* a wedge, the modular flow of the vacuum on $\mathcal{A}(\mathcal{O})$ exists (Reeh–Schlieder + Tomita–Takesaki) but is **not** in general a geometric symmetry of spacetime.

### 7.1 The conformal exception: Hislop–Longo

For a 2D conformal field theory and a double cone $\mathcal{O}_{r}$ centered at the origin with proper radius $r$, Hislop–Longo (1982) prove that the modular flow on $\mathcal{A}(\mathcal{O}_r)$ is the one-parameter family of **conformal transformations** preserving $\mathcal{O}_r$. The relevant subgroup is the special conformal transformation (SCT) combined with translation that fixes the two tips of the double cone.

This works because:
- Conformal invariance allows a conformal map from the wedge to the double cone;
- The map intertwines the boost subgroup of the wedge with the SCT-translation subgroup of the double cone;
- Bisognano–Wichmann on the wedge transports to a geometric modular flow on the double cone.

### 7.2 What fails for non-conformal bounded regions

For a 4D scalar field with mass $m > 0$, restricted to a bounded ball at fixed time, the modular flow is **not** geometric. There is no spacetime symmetry that preserves a bounded region while having full real spectrum (required for type III$_1$ structure, Week 12). The modular flow exists as an abstract automorphism of the algebra, but it does not correspond to any pullback of a diffeomorphism.

This is a structural fact, and it limits the explicit calculability of $\Delta$ outside wedges and conformal double cones. Most of the recent algebraic-gravity literature (Witten 2112.12828, CPW, AAJ) works in settings where Bisognano–Wichmann or its conformal analog gives an explicit modular operator; this is what enables the explicit dressed-entropy calculations of Sem II.

### 7.3 Modular flow as a probe of geometry

A research-level question raised by the holographic AdS/CFT literature (Liu, Faulkner, others): **modular flow ↔ bulk Killing flow**. For a CFT vacuum on a boundary region $\mathcal{O}$, the modular flow on $\mathcal{A}(\mathcal{O})$ is dual to a one-parameter Killing flow inside the bulk causal wedge corresponding to $\mathcal{O}$. This is the holographic generalization of Bisognano–Wichmann: it identifies modular flow with a geometric flow, but the geometry is in the *bulk*, not on the boundary. We pick this up in Sem II Block 3 (Liu lectures).

## 8. Why this matters for the rest of the course

Bisognano–Wichmann is **the** anchor for the entire Sem II crossed-product program. Every research-level calculation in the Witten/CPW/AAJ literature follows the same pattern:

1. **Identify the local algebra.** Typically a wedge in a relativistic QFT, or the large-$N$ single-trace algebra on a holographic boundary.
2. **Identify the modular flow.** Via Bisognano–Wichmann (for wedges in free or Wightman theories) or via the holographic modular-flow ↔ bulk-Killing-flow dictionary (Liu lectures, Block 3).
3. **Apply Tomita–Takesaki + crossed-product machinery** (Block D) to obtain a dressed type II$_\infty$ algebra.
4. **Compute dressed entropies as concrete numbers**, because step 2 made the modular operator explicit and the trace on the dressed algebra is then an integral kernel involving $K$.

Without Bisognano–Wichmann, step 2 would be a black box and steps 3–4 could not be performed concretely. The free-field mini-calculations in Sem II Block 1 (Witten 2022 free-field analogue) and Block 4 (Ahmad–Jefferson free-field analogue) are exactly the case where step 2 is provided by Bisognano–Wichmann.

For Bell–CHSH (Week 11 next): Bisognano–Wichmann + Tomita–Takesaki + type III$_1$ structure (Week 12) is the input to Summers–Werner saturation of the Tsirelson bound between Rindler wedges.

## 9. What to take away

- **Stated only:** Bisognano–Wichmann — for the Rindler wedge in any Wightman QFT, the modular operator of the vacuum is $\Delta_{W_R} = e^{-2\pi K}$, where $K$ is the Lorentz boost generator in the $(x^0, x^1)$-plane.
- **Verified in the 2D massless free scalar (model proof):** Bogoliubov transformation between Minkowski and Rindler modes gives thermal Rindler occupation at $\beta = 2\pi$, equivalently KMS at modular $\beta = 1$ for the boost flow. By Takesaki uniqueness, the boost flow is the modular flow.
- **Modular flow is geometric:** $\sigma_t^{W_R}$ acts on Weyl operators by $W(f) \mapsto W(f \circ \Lambda^{\mathrm{boost}}(-2\pi t))$ — a pure boost on test functions. The orbit of any wedge-supported $f$ fills the wedge non-compactly and never reaches the boundary in finite modular time.
- **Modular conjugation is PCT × rotation:** $J_{W_R} = \Theta \cdot R_\perp(\pi)$. It maps $\mathcal{A}(W_R)$ to $\mathcal{A}(W_L)$, proving Haag duality for wedges.
- **Unruh effect as corollary:** $T_U = a/(2\pi)$ for a uniformly accelerated observer with proper acceleration $a$.
- **Geometric modular flow is rare:** only wedges (always) and double cones in conformal theories (Hislop–Longo). For general bounded regions, $\Delta$ exists but is not a spacetime symmetry.

## 10. Looking ahead

Week 11 puts Bisognano–Wichmann to work on a physically important observable: the **Bell–CHSH inequality** between two complementary Rindler wedges. The Summers–Werner theorem says that *every* normal state in any Wightman QFT (in particular the vacuum) saturates the Tsirelson bound $2\sqrt 2$ between $\mathcal{A}(W_R)$ and $\mathcal{A}(W_L)$. The structural reason is that the wedge algebras are type III$_1$ (Week 12) and the algebraic mechanism uses the modular operator from this week. The group's recent papers on Bell–CHSH in free scalar, Proca, and gauge theories sit exactly in this framework.

## 11. Problem set

**Core problems.**

**1. Bogoliubov coefficient ratio.** Derive the form $|\beta_{\omega k}|^2 / |\alpha_{\omega k}|^2 = e^{-2\pi\omega}$ in the 2D massless free scalar, starting from
$$
\alpha_{\omega k} = \frac{1}{2\pi}\sqrt{\frac{\omega}{k}}\,\Gamma(i\omega)\,k^{-i\omega}\, e^{+\pi\omega/2}, \qquad \beta_{\omega k} = \frac{1}{2\pi}\sqrt{\frac{\omega}{k}}\,\Gamma(i\omega)\,k^{-i\omega}\, e^{-\pi\omega/2}.
$$
(*Hint:* take absolute values; the $\Gamma$, $k$, and $\omega$ factors cancel, leaving only $e^{\pm\pi\omega}$.)

**2. Rindler thermal occupation.** Compute $\langle 0_M | (b_\omega^R)^\dagger\, b_\omega^R | 0_M\rangle$ from the Bogoliubov transformation, reproducing the Bose–Einstein form
$$
\frac{1}{e^{2\pi\omega} - 1}
$$
(per unit Rindler volume). Use the gamma-function identity $|\Gamma(i\omega)|^2 = \pi/(\omega\sinh\pi\omega)$ and verify the simplification step-by-step.

**3. Boost generator commutator with Weyl operators.** For a real test function $f$ supported in $W_R$, compute $i[K, W(f)]$ on the dense subspace of analytic vectors for $K$. (*Hint:* differentiate the boost action $U(\Lambda^{\mathrm{boost}}(s))\,W(f)\,U(s)^* = W(f\circ\Lambda^{\mathrm{boost}}(-s))$ at $s = 0$, identifying $\frac{d}{ds}\big|_0 f\circ\Lambda^{\mathrm{boost}}(-s) = -\mathcal{L}_K f$ as the Lie derivative along the boost vector field.) Express the result as $W(\dot f)$ for an explicit $\dot f$.

**4. Modular flow on a Gaussian wavelet.** For the 2D massless free scalar, take a Gaussian bump $f(x) = c\,e^{-(x^0 - \tau_0)^2/\sigma^2 - (x^1 - s_0)^2/\sigma^2}$ centered at $(\tau_0, s_0) \in W_R$. Compute $\sigma_t^{W_R}(W(f)) = W(f^{(t)})$ explicitly, identifying $f^{(t)}$ as a Gaussian of the same width centered at the boost-rotated point.

**5. Unruh temperature in physics units.** Convert modular $\beta = 1$ into the physical Unruh inverse temperature $\beta_{\text{proper}} = 2\pi/a$. Compute $T_U$ for an acceleration $a = g \approx 10\,\mathrm{m/s^2}$ (Earth gravity); for $a = 10^{20}\,\mathrm{m/s^2}$ (proton in an LHC dipole field — roughly); for an acceleration that produces $T_U = 1\,\mathrm{K}$. Discuss why direct laboratory detection of the Unruh effect is so hard.

**6. Modular flow never reaches the wedge boundary.** Show that for any test function $f$ supported strictly inside $W_R$ (i.e., the support is at finite distance from the null boundaries), the modular-flowed support $\mathrm{supp}(f \circ \Lambda^{\mathrm{boost}}(-2\pi t))$ remains strictly inside $W_R$ for every $t \in \mathbb{R}$. (*Hint:* Lorentz boosts are isometries of the wedge into itself.)

**Starred problems.**

**7\*. Modular operator on a double cone (Hislop–Longo).** State the Hislop–Longo theorem: for a 2D conformal field theory and a symmetric double cone $\mathcal{O}_r$, the modular operator is $\Delta_{\mathcal{O}_r} = e^{-2\pi K_{\mathrm{conf}}}$ where $K_{\mathrm{conf}}$ generates the conformal subgroup fixing $\mathcal{O}_r$. Sketch the input it requires (conformal invariance + cyclicity of the vacuum + intertwining with the wedge via conformal map).

**8\*. 4D massless scalar.** Repeat the Bogoliubov analysis for the 4D massless free scalar, restricted to a single Rindler-direction mode (the transverse momenta $\vec k_\perp$ become parameters; the right-mover decomposes into a continuum of 2D-like sectors labeled by $\vec k_\perp$). Verify the same $e^{2\pi\omega}$ structure in each sector.

**9\*. Boost generator is positive on the wedge subspace.** Show that, when restricted to the wedge subspace $\overline{\mathcal{A}(W_R)\,\Omega}$, the boost generator $K$ has non-negative spectrum on a dense subspace. (*Hint:* this is delicate. The spectral condition $P^0 \ge 0$ does not directly imply $K \ge 0$, but $e^{-2\pi K}$ must be a positive operator on the wedge subspace because $\Delta_{W_R}$ is a modular operator. Reconcile these.)

**10\*. Modular conjugation in 2D.** For the 2D massless free scalar, verify directly that $J = \Theta$ (CPT) implements the map $\mathcal{A}(W_R) \to \mathcal{A}(W_L)$. (*Hint:* in 2D massless, CPT acts on the right-moving sector by $x^- \to -x^-$ and on the left-moving sector by $x^+ \to -x^+$, swapping $W_R$ and $W_L$. Verify on Weyl operators via Theorem 1.1 and the action on test functions.)

**11\*. Modular flow vs. proper-time flow.** For an observer at fixed $\xi = \xi_0$ in $W_R$, the proper-time evolution $\alpha_\tau = \mathrm{Ad}(e^{i\tau H_{\xi_0}})$ for some self-adjoint $H_{\xi_0}$ is *not* the modular flow $\sigma_t^{W_R}$. The two differ by the lapse factor: $\sigma_t^{W_R} = \alpha_{2\pi t / a}$. State precisely the relationship and explain why the modular flow is observer-independent (it depends only on the wedge, not on the choice of accelerated observer inside it).

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block C. Last revised 2026-06-11.*
