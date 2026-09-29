---
title: "Week 10 — The Bisognano–Wichmann Theorem"
type: lecture-notes
course: syllabus
semester: 1
week: 10
block: C
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 5–9 (Tomita–Takesaki + Reeh–Schlieder + Weyl algebras)
modified: 2026-09-29
---

# Week 10 — The Bisognano–Wichmann Theorem

> *Reeh–Schlieder gives the vacuum modular operator for every suitable local region as an existence theorem. Bisognano–Wichmann does something rarer: for a Rindler wedge it identifies that operator geometrically, as the exponential of the Lorentz-boost generator. This is the principal model-independent explicit modular flow used in the course and the algebraic core of the Unruh effect.*

### How to use this chapter

- **In class:** draw the wedge and its boost orbits first, fix $U(\Lambda(s))=e^{isK}$, and derive the dictionary $\Delta=e^{-2\pi K}$, $\sigma_t=\operatorname{Ad}\Delta^{-it}$, $s=2\pi t$ before discussing Unruh temperature.
- **For self-study:** check the theorem on smeared Weyl operators and then perform the Rindler-mode occupation calculation as a consistency check, not as the proof of the algebraic KMS theorem.
- **Instructor checkpoint:** a boost preserves the Rindler radius; fixed-radius orbits approach null infinity, not the bifurcation surface. Also keep regulated left/right mode notation distinct from a literal tensor factorization of the continuum vacuum representation.

## 0. Reading

**Primary:**
- Bisognano & Wichmann, "On the duality condition for a Hermitian scalar field," *J. Math. Phys.* 16 (1975) 985; "On the duality condition for quantum fields," *J. Math. Phys.* 17 (1976) 303 (the original two papers).
- Haag, *Local Quantum Physics*, ch. V §4 (the modular geometry of wedges; standard reference).

**Secondary:**
- Borchers, "On revolutionizing quantum field theory with Tomita's modular theory," *J. Math. Phys.* 41 (2000) 3604 — clean modernized exposition.
- Sewell, "Quantum fields on manifolds: PCT and gravitationally induced thermal states," *Ann. Phys.* 141 (1982) 201 (curved-space generalization; foundational for the algebraic Unruh effect).
- Summers, "Yet more ado about nothing: the remarkable relativistic vacuum state," arXiv:0802.1854, §4–5 (philosophical/structural review).

**Optional research reading:**
- Hislop & Longo, "Modular structure of the local algebras associated with the free massless scalar field theory," *Comm. Math. Phys.* 84 (1982) 71 (explicit double-cone modular structure for the free massless scalar in any spacetime dimension).
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
This subgroup preserves $W_R$. Formally, when a suitable stress tensor exists, the global **boost generator** at $x^0=0$ is
$$
K=\int_{\mathbb{R}^d}x^1T^{00}(0,\vec x)\,d^d x,
$$
and we fix the implementer convention
$$
\boxed{U(\Lambda^{\mathrm{boost}}(s))=e^{+isK}.}
$$
The theorem itself only needs the self-adjoint generator of the unitary boost representation. The stress-tensor formula is model-dependent and requires smearing and domain control.

Two properties of $K$ that we will use:
- **Vacuum annihilation:** $K\Omega = 0$. (Boosts fix the vacuum since the vacuum is Poincaré-invariant.)
- **Full real spectrum in the nontrivial vacuum representation:** $\sigma(K)=\mathbb{R}$ in the standard QFT setting. This does not mean that boosts turn positive-energy states into negative-energy states—the forward energy-momentum cone is Lorentz invariant. It means that the generator of the noncompact boost subgroup is unbounded in both directions.

Let $J^{\mathrm{wedge}}$ denote the geometric transformation
$$
J^{\mathrm{wedge}}:\;\; (x^0, x^1, \vec x_\perp) \mapsto (-x^0, -x^1, \vec x_\perp),
$$
i.e., reflection through the edge of the wedge $\{x^0 = x^1 = 0\}$. This has $\det = +1$ in $d \ge 2$ but is **not** connected to the identity in $\mathcal{P}_+^\uparrow$ (it reverses time). On a Wightman QFT satisfying the PCT theorem, the combination of $J^{\mathrm{wedge}}$ with a rotation in the perpendicular directions is implemented by the antiunitary CPT operator.

### 1.2 The theorem

**Theorem 1.1 (Bisognano–Wichmann). [Stated only — refs: Bisognano–Wichmann 1975, 1976; Borchers 2000 for the modernized proof.]** *Assume the standard finite-component Wightman framework (tempered fields, vacuum cyclicity, spectrum condition, locality, and Poincaré covariance). For the local vN algebra $\mathcal{A}(W_R)$ of a right Rindler wedge, the modular operator of the vacuum is*
$$
\boxed{\Delta_{W_R} = e^{-2\pi K}}
$$
*and, for the neutral bosonic observable/scalar net used in this course, the modular conjugation is*
$$
\boxed{J_{W_R} = \Theta \cdot R_\perp(\pi)},
$$
*where $\Theta$ is the antiunitary CPT operator and $R_\perp(\pi)$ denotes the transverse rotation required so that the combined geometric action fixes $\vec x_\perp$ (trivial in two spacetime dimensions). In our upper-strip convention (Week 6), the modular flow is*
$$
\sigma_t^{W_R}(a) \;=\; \Delta_{W_R}^{-it}\, a\, \Delta_{W_R}^{it} \;=\; U(\Lambda^{\mathrm{boost}}(2\pi t))\, a\, U(\Lambda^{\mathrm{boost}}(2\pi t))^*.
$$
*The modular conjugation maps $\mathcal{A}(W_R)$ onto $\mathcal{A}(W_L)$. For a field net containing fermions, the corresponding statement uses the standard statistics twist and gives twisted wedge duality; the untwisted observable-net statement above is the one used below.*

> **Physical picture: why $2\pi$ — the Euclidean angle.** Wick-rotate Minkowski time. The boost subgroup analytically continues to rotations in the Euclidean $(x_E^0,x^1)$ plane, and the wedge becomes a half-plane. In our implementer convention $U(\Lambda(s))=e^{isK}$,
> $$
> \Delta^{1/2}=e^{-\pi K}=U(\Lambda(i\pi)),
> $$
> the analytic boost through angle $\pi$. A full Euclidean turn has angle $2\pi$, which becomes the KMS period in boost rapidity. This is a geometric mnemonic, not the Wightman-domain proof: Bisognano–Wichmann is the operator-theoretic theorem that makes the continuation and its domains precise.

**Reading the formula.** The factor of $2\pi$ in the exponent is not an artifact — it is the algebraic shadow of the Unruh temperature. The relation $\Delta = e^{-2\pi K}$ means that **modular time $t$ corresponds to the boost subgroup at rapidity $2\pi t$**. An observer with proper acceleration $a$ has proper time $\tau$ related to boost rapidity by $s = a\tau$ (the trajectory $x^1 = (1/a)\cosh(a\tau), x^0 = (1/a)\sinh(a\tau)$), so modular time $t$ corresponds to proper time $\tau = 2\pi t / a$. The KMS condition at modular $\beta = 1$ (Week 6) translates into KMS for the accelerated observer at inverse proper-time temperature $\beta_{\text{proper}} = 2\pi/a$, i.e., physical temperature $T_U = a/(2\pi)$. This is the Unruh effect.

### 1.3 Three immediate consequences

**(a) The Unruh effect, made algebraic.** Theorem 1.1 directly implies that the Minkowski vacuum, viewed as a state on $\mathcal{A}(W_R)$, satisfies KMS at the Unruh temperature for the boost flow. For wedge-localized $A,B$, the correlation function
$$
F_{A,B}(\tau)=\omega_0\!\left(A\,\alpha_\tau(B)\right)
$$
has the KMS strip and boundary relation at $\beta_{\mathrm{proper}}=2\pi/a$. In Fourier space this gives detailed balance between excitation and de-excitation spectral densities. There is no universal Bose-denominator formula for arbitrary interacting-theory observables: the response also contains model-dependent spectral data. The free-mode computation of §4 exhibits the Bose factor in a controlled sector, while the algebraic theorem applies to every wedge observable under its Wightman hypotheses.

**(b) Haag duality for wedges.** Bisognano–Wichmann implies $J_{W_R}\,\mathcal{A}(W_R)\,J_{W_R}^{-1} = \mathcal{A}(W_L)$ (geometric, via CPT-plus-rotation acting as $J^{\mathrm{wedge}}$ on test functions). Combined with the Tomita commutant theorem $J\mathcal{A}(W_R)J = \mathcal{A}(W_R)'$ (Week 5 §4), this gives the geometric Haag duality
$$
\mathcal{A}(W_R)' \;=\; \mathcal{A}(W_L) \;=\; \mathcal{A}(W_R').
$$
**In the bosonic observable/scalar setting, Bisognano–Wichmann therefore proves Haag duality for wedges.** For fermionic field nets the parallel conclusion is twisted duality. The result is not just a statement about the modular operator; it also identifies the structural locality relation for wedge-shaped regions.

**(c) Modular flow is geometric in a special, powerful class of examples.** Wedges give the universal Wightman-theory example. Conformal covariance transports wedge boosts to geometric modular flows for balls, intervals, or double cones in the appropriate conformal setting, and additional special constructions exist. For a generic state and bounded region, however, modular flow is not expected to be induced by a spacetime diffeomorphism. The contrast—not an absolute uniqueness claim—is what makes the wedge theorem so useful.

## 2. Proof strategy: what we do and what we don't

The full Bisognano–Wichmann proof is technically demanding (originally ~25 pages each in the 1975 and 1976 papers, with substantial Wightman-analyticity prerequisites). It builds on:
- **Wightman analyticity** of the $n$-point functions in tube domains (forward-tube holomorphy from the spectral condition);
- **Reeh–Schlieder** (Week 9) supplying cyclicity of the vacuum for $\mathcal{A}(W_R)$;
- **The Bargmann–Hall–Wightman theorem**: Lorentz covariance and the spectral condition extend the Wightman functions to the complex Lorentz group. On vectors $a\Omega$ with $a$ localized in $W_R$, the boost $U(\Lambda(s))=e^{isK}$ therefore continues analytically in the rapidity to the strip $0\le\operatorname{Im}s\le\pi$. At $s=i\pi$ the complexified boost acts on real points as the reflection $(x^0,x^1)\mapsto(-x^0,-x^1)$, and $e^{isK}$ becomes $e^{-\pi K}$;
- **The PCT theorem** (Jost; Wightman): to identify the antiunitary $J_{W_R}$ as $\Theta \cdot R_\perp(\pi)$.

The full proof shows that the operator $J_0 \Delta_0^{1/2}$ defined by the Tomita procedure on $\mathcal{A}(W_R)\Omega$ — *a priori* unknown abstractly — coincides with the closure of $a\,\Omega \mapsto (\Theta R_\perp(\pi)\, e^{-\pi K}\, a)\,\Omega$, by exploiting the analytic structure of $K$ on the dense domain of analytic vectors. **[Stated only — for the full proof: Bisognano–Wichmann 1975, 1976; Borchers 2000 §3 for a streamlined modern treatment.]**

What we **do** in this lecture:

1. **Plausibility (§3):** establish that the boost flow is the *unique* candidate for the modular flow consistent with KMS at the Unruh temperature, via Takesaki uniqueness.
2. **Free-field mode check (§§4–5):** compute the Minkowski/Rindler Bogoliubov ratio and recover the Bose occupation factor. This verifies detailed balance in the free mode sector; it does not, by itself, prove the full algebraic KMS condition or identify the Tomita operator.
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

1. **Unruh's mode argument is theory-specific** (free fields, specific modes). Bisognano–Wichmann is **model-independent within its Wightman hypotheses** and is not restricted to free theories.
2. **Verifying KMS for the boost flow is non-trivial.** The KMS condition requires a particular *analytic continuation* of vacuum two-point functions of wedge-localized observables to a strip in modular time. The original Bisognano–Wichmann proof shows this analyticity holds for *any* Wightman field, via the spectral condition. This is the content of the proof we skip.

So the plausibility argument identifies the right **candidate**; the full theorem verifies the candidate under the stated Wightman hypotheses.

## 4. Rindler coordinates and a free-mode check (2D massless)

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

We now restrict to two spacetime dimensions and the massless derivative field (or an infrared-regulated scalar) for the rest of §4. The factorization $\phi=\phi_R(x^-)+\phi_L(x^+)$, with $x^\pm=x^0\pm x^1$, makes the mode calculation tractable. We focus on the right-moving sector; the left-moving sector is analogous.

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
u_\omega^R(x^-)
:=\frac{1}{\sqrt{4\pi\omega}}\,(-x^-)^{i\omega}
=\frac{1}{\sqrt{4\pi\omega}}\,\xi^{i\omega}e^{-i\omega\eta},
\qquad x^-<0,\quad\omega>0.
$$
The factor $\xi^{i\omega}$ is the spatial Rindler dependence. Along a fixed-$\xi$ trajectory it is a constant phase, but it must not be deleted from a wedge mode. Equivalently, the mode is a plane wave in the right-moving Rindler null coordinate $u_R=-\log(-x^-)=\eta-\log\xi$.

The Rindler-mode expansion of $\phi_R$ restricted to $W_R$ is
$$
\phi_R\big|_{W_R}(x^-) = \int_0^\infty d\omega\,\left[b_\omega^R\, u_\omega^R(x^-) + (b_\omega^R)^\dagger\, u_\omega^{R*}(x^-)\right],
$$
with $[b_\omega^R, b_{\omega'}^{R\dagger}] = \delta(\omega - \omega')$. The **Rindler vacuum** $|0_R\rangle$ is defined by $b_\omega^R |0_R\rangle = 0$ for all $\omega > 0$.

A parallel construction inside $W_L$ gives left-Rindler operators. In a regulated type-I mode model one writes a product Fulling vacuum $|0_R\rangle\otimes|0_L\rangle$. In the continuum this notation is formal: the touching wedge algebras do not define a Hilbert-space tensor factorization in the Minkowski representation, and the Fulling and Minkowski representations are not related by a single global Fock-space unitary.

**Key fact:** in the regulated mode picture, the Minkowski vacuum is not the Rindler product vacuum. The Bogoliubov ratio below captures the resulting thermal occupation. The exact continuum statement is the wedge KMS property, not a literal thermofield-double vector in a sharp $R/L$ tensor product.

### 4.4 The Bogoliubov transformation

To express $b_\omega^R$ in terms of $a_k, a_k^\dagger$, take the overlap of the two mode functions. Concretely, write $u := -x^- = \xi e^{-\eta}$, which is positive on $W_R$. The Minkowski mode $e^{-ikx^-} = e^{iku}$ has a known expansion in the Rindler powers $(-x^-)^{i\omega}=u^{i\omega}$ via the **Mellin transform**:
$$
e^{iku} = \int_{-\infty}^\infty \frac{d\omega}{2\pi}\, e^{i\omega \log(ku)}\, \Gamma(-i\omega)\, (-i)^{i\omega},
\qquad (-i)^{i\omega}=e^{\pi\omega/2},
$$
valid in a suitable distributional sense. It follows from $\int_0^\infty u^{s-1}e^{iku}\,du=\Gamma(s)(-ik)^{-s}$ for $0<\operatorname{Re}s<1$ on the principal branch, together with Mellin inversion along $s=-i\omega$. The weight $e^{+\pi\omega/2}$ therefore multiplies the Rindler-positive powers ($\omega>0$), and $e^{-\pi|\omega|/2}$ the Rindler-negative ones. Splitting into $\omega > 0$ (Rindler-positive) and $\omega < 0$ (Rindler-negative) parts and matching coefficients gives:
$$
b_\omega^R = \int_0^\infty dk\,\left[\alpha_{\omega k}\, a_k + \beta_{\omega k}\, a_k^\dagger\right],
$$
where the **Bogoliubov coefficients** are
$$
\alpha_{\omega k} = \frac{1}{2\pi}\sqrt{\frac{\omega}{k}}\,\Gamma(i\omega)\,k^{-i\omega}\, e^{+\pi\omega/2}, \qquad \beta_{\omega k} = \frac{1}{2\pi}\sqrt{\frac{\omega}{k}}\,\Gamma(i\omega)\,k^{-i\omega}\, e^{-\pi\omega/2}.
$$
Individual phases, powers of $k$, and normalization factors in these kernels depend on the mode and Klein–Gordon-inner-product conventions. The robust content used below is the **relative-modulus ratio**
$$
\frac{|\beta_{\omega k}|^2}{|\alpha_{\omega k}|^2} = e^{-2\pi\omega}.
$$
This $e^{-2\pi\omega}$ is the thermal Boltzmann factor at temperature $T = 1/(2\pi)$ in Rindler units; reinstating the lapse $\xi_0$ to get proper time gives $T_U = a/(2\pi)$ in physical units, as anticipated.

*Where the factor really comes from: analyticity across the horizon.* The cleanest derivation of the $e^{\pm\pi\omega/2}$ asymmetry (Unruh's original trick) avoids the Mellin integral entirely. A Minkowski positive-frequency function of $x^-$ is the boundary value of a function holomorphic in the **lower half** complex-$x^-$ plane (because $e^{-ikx^-}$ with $k>0$ decays there). A Rindler mode behaves as $(-x^-)^{i\omega}$ inside $W_R$ ($x^- < 0$) and $(x^-)^{i\omega}$ in $W_L$ ($x^- > 0$). To assemble a globally Minkowski-positive-frequency combination one must continue $(-x^-)^{i\omega}$ through the lower half plane to positive $x^-$, and the branch point at $x^- = 0$ — the horizon — produces the relative weight $|e^{i\omega\log(-1)}| = e^{-\pi\omega}$ on the far side. So the Boltzmann factor is the monodromy of $x^{i\omega}$ around the horizon point, with the *direction* of continuation (lower half plane) dictated by the spectral condition. The thermal character of the vacuum is, once again, an analyticity statement: positive energy fixes the side on which correlators are holomorphic, and the horizon's branch cut converts that choice into temperature.

### 4.5 Thermal occupation

A sharp continuum-frequency mode is delta-normalized, so its number expectation contains a $\delta(0)$ normalization volume. Dividing an informal $\int dk/k$ by a hand-chosen “volume” can leave spurious factors. The clean calculation uses normalized wave packets, or a discrete box regulator followed by a controlled limit.

For one normalized Bogoliubov pair, write
$$
b=\alpha a+\beta a^\dagger,
\qquad
|\alpha|^2-|\beta|^2=1.
$$
The analytic-continuation calculation gives
$$
r:=\frac{|\beta|^2}{|\alpha|^2}=e^{-2\pi\omega}.
$$
Solving these two equations,
$$
|\beta|^2=\frac{r}{1-r}
=\boxed{\frac{1}{e^{2\pi\omega}-1}}.
$$
Since $a|0_M\rangle=0$, this is $\langle0_M|b^\dagger b|0_M\rangle$ for the normalized packet. For continuum kernels the same Planck factor multiplies the appropriate delta function or packet overlap. This is the Bose–Einstein occupation at Rindler inverse temperature $2\pi$, with no normalization-dependent prefactor.

### 4.6 What the mode calculation verifies

For normalized Rindler wave packets, the two frequency-ordered correlations have the ratio
$$
\frac{\langle b^\dagger b\rangle_{0_M}}
{\langle b b^\dagger\rangle_{0_M}}
=e^{-2\pi\omega}.
$$
This is the detailed-balance consequence of KMS at $\beta_R=2\pi$ for boost time. Rescaling $\eta=2\pi t$ gives modular inverse temperature $1$.

What has been verified here is the Planck factor and detailed balance for a free mode sector. Full KMS requires the strip analyticity and boundary relation for a dense algebra of bounded wedge observables. The Bisognano–Wichmann theorem supplies precisely that missing statement and, together with Takesaki uniqueness, identifies $\Delta_{W_R}=e^{-2\pi K}$. Thus §4 is a consistency check and physical derivation of the temperature, not a substitute proof of the theorem.

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

This is a **geometric** action on the test function. The scalar pullback contains $-2\pi t$, while the support itself is transported by $\Lambda^{\mathrm{boost}}(+2\pi t)$, in agreement with the physical boost rapidity $s=+2\pi t$.

### 5.1 Worked example: a compact wave packet under modular flow

Let $f\in C_c^\infty(W_R)$ be a compact bump centered at $x_c=(\tau_0,s_0)$, as constructed in Week 8 §6. The modularly evolved test function is
$$
f_t(x)=f\!\left(\Lambda^{\mathrm{boost}}(-2\pi t)x\right),
$$
so
$$
\operatorname{supp}f_t
=\Lambda^{\mathrm{boost}}(2\pi t)\operatorname{supp}f,
\qquad
x_c(t)=\Lambda^{\mathrm{boost}}(2\pi t)x_c.
$$
The support is transported exactly by a Lorentz boost and remains compact inside the wedge for every finite $t$. If one plots a Euclidean-radial bump in the $(x^0,x^1)$ coordinate plane, its coordinate covariance becomes an ellipse; “same width” is not a Lorentz-invariant statement. What is preserved is the Minkowski geometry of the pulled-back profile.

Write the center as $x^1=\xi\cosh\eta$, $x^0=\xi\sinh\eta$. Modular flow sends
$$
(\xi,\eta)\longmapsto(\xi,\eta+2\pi t).
$$
Thus $\xi$—the proper distance scale from the horizons along the $t=0$ slice—is invariant. As $t\to+\infty$ the orbit runs toward future **null infinity**; as $t\to-\infty$ it runs toward past null infinity. It does not approach the bifurcation surface $\xi=0$. Approaching that surface requires a separate sequence of supports with $\xi\to0$, not a single modular orbit.

The noncompact boost spectrum is consistent with the modular spectrum used in the type-III analysis, but this geometric observation is not a proof of the factor subtype. Week 12 states the additional scaling theorem needed for that conclusion.

### 5.2 The KMS condition spelled out

The KMS condition at $\beta = 1$ for $\sigma^{W_R}$ says: the function
$$
t \mapsto \langle 0_M|\, W(f)\, \sigma_t^{W_R}(W(g))\, |0_M\rangle \;=\; \langle 0_M|\, W(f)\, W(g \circ \Lambda^{\mathrm{boost}}(-2\pi t))\, |0_M\rangle
$$
extends to a holomorphic function on the upper strip $0 \le \mathrm{Im}\,t \le 1$, and at $t \to t + i$ equals
$$
\langle 0_M|\, \sigma_t^{W_R}(W(g))\, W(f)\, |0_M\rangle.
$$
For the free field, both boundary values can be computed from the quasi-free characteristic functional and the symplectic form, with the two-dimensional infrared qualification of Week 8. The nontrivial step is analytic continuation in **complex boost time** through a strip; it is not a shift of the frequency variable itself. Bisognano–Wichmann proves that strip analyticity for the wedge algebra.

## 6. Modular conjugation and PCT

The modular conjugation $J_{W_R}$ is more subtle than $\Delta_{W_R}$. By the polar decomposition $S = J\Delta^{1/2}$ (Week 5), $J$ must be **antiunitary** and satisfy $J\mathcal{A}(W_R)J = \mathcal{A}(W_R)'$.

### 6.1 PCT in Wightman QFT

The PCT theorem in the standard finite-component Wightman framework supplies an antiunitary operator $\Theta$ on Hilbert space that implements the combined symmetry charge-conjugation × parity × time-reversal:
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
J_{W_R}\, W(f)\, J_{W_R}^{-1} = W(-f^j),
$$
for a neutral scalar, where $j(x^0,x^1,\vec x_\perp)=(-x^0,-x^1,\vec x_\perp)$ and $f^j=f\circ j$. The minus sign is forced by antiunitarity:
$$
J\,i\,J^{-1}=-i.
$$
For charged or multiplet fields, charge conjugation must be included; for fermionic field nets, so must the statistics twist. The simple Weyl formula here is the neutral scalar case.

If $f$ is supported in $W_R$, then $f^j$ is supported in $W_L$. Since $W(-f^j)$ belongs to the same left-wedge Weyl algebra as $W(f^j)$, $J_{W_R}$ maps $\mathcal{A}(W_R)$ to $\mathcal{A}(W_L)$, as required by Tomita's commutant theorem.

### 6.3 The 2D case

In 2D ($d = 1$), there is no perpendicular plane and $R_\perp$ is trivial. So $J_{W_R} = \Theta$ is just CPT. Acting on the 2D massless free scalar with the lightcone decomposition $\phi = \phi_R(x^-) + \phi_L(x^+)$:
$$
\Theta\,\phi_R(x^-)\,\Theta^{-1} = \phi_R(-x^-), \qquad \Theta\,\phi_L(x^+)\,\Theta^{-1} = \phi_L(-x^+).
$$
The map $x^- \to -x^-, x^+ \to -x^+$ is $(x^0, x^1) \to (-x^0, -x^1)$, which swaps $W_R$ and $W_L$. Remembering that $\Theta$ is antiunitary, the corresponding Weyl action contains the minus sign displayed in §6.2.

## 7. Failure of geometric modular flow beyond wedges

For a bounded region $\mathcal{O}$ that is *not* a wedge, the modular flow of the vacuum on $\mathcal{A}(\mathcal{O})$ exists (Reeh–Schlieder + Tomita–Takesaki) but is **not** in general a geometric symmetry of spacetime.

### 7.1 The conformal exception: Hislop–Longo and its net-theoretic extension

For the vacuum free massless scalar and a double cone $\mathcal{O}_{r}$, Hislop and Longo (1982) prove that the modular flow on $\mathcal{A}(\mathcal{O}_r)$ is the one-parameter family of **conformal transformations** preserving $\mathcal{O}_r$. Brunetti, Guido, and Longo later formulate the corresponding modular-covariance result for conformal nets under their stated hypotheses. The relevant subgroup is a fractional-linear conformal transformation fixing the two tips of the double cone.

This works because:
- Conformal invariance allows a conformal map from the wedge to the double cone;
- The map intertwines the boost subgroup of the wedge with the SCT-translation subgroup of the double cone;
- Bisognano–Wichmann on the wedge transports to a geometric modular flow on the double cone.

### 7.2 What fails for non-conformal bounded regions

For a massive scalar field, consider the algebra of the causal diamond generated by a time-zero ball. Its vacuum modular flow exists, but it is not generally induced by a spacetime symmetry preserving the diamond. The statement concerns the known form of the modular action; “full real spectrum” is neither a geometric obstruction nor, by itself, a proof of type III$_1$.

This is a structural fact, and it limits the explicit calculability of $\Delta$ outside wedges and conformal double cones. Most of the recent algebraic-gravity literature (Witten 2112.12828, CPW, AAJ) works in settings where Bisognano–Wichmann or its conformal analog gives an explicit modular operator; this is what enables the explicit dressed-entropy calculations of Sem II.

### 7.3 Modular flow as a probe of geometry

A research-level theme in AdS/CFT is the relation between boundary and bulk modular flow. For the CFT vacuum on a ball, boundary modular flow is conformal and extends to the AdS–Rindler Killing flow. For a generic region or state, neither boundary nor bulk modular flow is a global Killing symmetry; the more precise claim is an equality or intertwining of modular actions within an appropriate code subspace, subject to reconstruction assumptions. Semester II Block 3 will keep this special geometric case separate from the general modular-flow dictionary.

## 8. Why this matters for the rest of the course

Bisognano–Wichmann is a major anchor for the Semester II crossed-product program. A common calculational pattern is:

1. **Identify the local algebra.** Typically a wedge in a relativistic QFT, or the large-$N$ single-trace algebra on a holographic boundary.
2. **Identify the modular flow.** Via Bisognano–Wichmann (for wedges in free or Wightman theories) or via the holographic modular-flow ↔ bulk-Killing-flow dictionary (Liu lectures, Block 3).
3. **Apply Tomita–Takesaki + crossed-product machinery** (Block D) to obtain a dressed type II$_\infty$ algebra.
4. **Compute dressed entropies as concrete numbers**, because step 2 made the modular operator explicit and the trace on the dressed algebra is then an integral kernel involving $K$.

Without an explicit modular generator, the crossed product still exists abstractly, but concrete kernels and entropy calculations become harder. The free-field mini-calculations in Semester II use Bisognano–Wichmann precisely to make that generator explicit.

For Bell–CHSH (Week 11), modular theory and the structure of complementary wedge algebras enter the Summers–Werner maximal-correlation theorem. We will state the net and injectivity hypotheses explicitly rather than attribute the result to type III$_1$ alone.

## 9. What to take away

- **Stated only:** Bisognano–Wichmann — under the standard finite-component Wightman hypotheses, the Rindler-wedge modular operator of the vacuum is $\Delta_{W_R} = e^{-2\pi K}$, where $K$ is the Lorentz boost generator in the $(x^0, x^1)$-plane.
- **Checked in a free mode sector:** the Bogoliubov ratio gives the Planck factor at Rindler inverse temperature $2\pi$. The full KMS and modular-operator statements still come from Bisognano–Wichmann.
- **Modular flow is geometric:** $\sigma_t^{W_R}$ acts by $W(f)\mapsto W(f\circ\Lambda^{\mathrm{boost}}(-2\pi t))$. A fixed orbit preserves Rindler radius $\xi$ and runs toward null infinity; it does not approach the bifurcation surface.
- **Modular conjugation is PCT × rotation in the neutral bosonic case:** $J_{W_R} = \Theta \cdot R_\perp(\pi)$. It maps $\mathcal{A}(W_R)$ to $\mathcal{A}(W_L)$ and proves wedge duality; fermionic field nets require the statistics-twisted version.
- **Unruh effect as corollary:** $T_U = a/(2\pi)$ for a uniformly accelerated observer with proper acceleration $a$.
- **Geometric modular flow is special:** wedges under the theorem's hypotheses and conformally related regions are the principal examples. Generic bounded-region modular flow is not expected to be a spacetime symmetry.

## 10. Looking ahead

Week 11 studies the **Bell–CHSH inequality** for complementary wedges. Summers and Werner prove maximal Bell correlation for vector states under weak net assumptions; when the wedge algebra is injective, the statement extends to every normal density-matrix state on the ambient $\mathcal{B}(\mathcal{H})$. This is stronger and more precise than saying “type III$_1$ implies saturation.” We will distinguish the structural supremum from the performance of explicit Weyl-derived observables.

## 11. Problem set

**Core problems.**

**1. Bogoliubov coefficient ratio.** Derive the form $|\beta_{\omega k}|^2 / |\alpha_{\omega k}|^2 = e^{-2\pi\omega}$ in the 2D massless free scalar, starting from
$$
\alpha_{\omega k} = \frac{1}{2\pi}\sqrt{\frac{\omega}{k}}\,\Gamma(i\omega)\,k^{-i\omega}\, e^{+\pi\omega/2}, \qquad \beta_{\omega k} = \frac{1}{2\pi}\sqrt{\frac{\omega}{k}}\,\Gamma(i\omega)\,k^{-i\omega}\, e^{-\pi\omega/2}.
$$
(*Hint:* take absolute values; the $\Gamma$, $k$, and $\omega$ factors cancel, leaving only $e^{\pm\pi\omega}$.)

**2. Rindler thermal occupation.** For a normalized Rindler wave packet concentrated near frequency $\omega$, use
$$
\frac{|\beta|^2}{|\alpha|^2}=e^{-2\pi\omega},
\qquad
|\alpha|^2-|\beta|^2=1,
$$
to reproduce
$$
\frac{1}{e^{2\pi\omega} - 1}
$$
up to the packet's finite bandwidth corrections. Explain why a sharp continuum-frequency number operator carries a delta-normalization factor and why “divide by Rindler volume” must not introduce an extra $1/(2\pi)$.

**3. Boost generator commutator with Weyl operators.** Let $f_s=f\circ\Lambda^{\mathrm{boost}}(-s)$ and $h=\dot f_0=-\mathcal{L}_\chi f$, where $\chi=x^1\partial_0+x^0\partial_1$.
(a) Show on a common analytic core that
$$
i[K,W(f)]=\left.\frac{d}{ds}W(f_s)\right|_{s=0}.
$$
(b) Use the Weyl relation to derive
$$
\left.\frac{d}{ds}W(f+s h)\right|_{s=0}
=\frac{i}{2}\sigma(f,h)W(f)+iW(f)\phi(h).
$$
Explain why the derivative is a tangent operator and is **not** the Weyl unitary $W(h)$.

**4. Modular flow on a compact bump.** Take $f\in C_c^\infty(W_R)$ centered at $x_c$. Compute $f_t=f\circ\Lambda(-2\pi t)$ and prove $\operatorname{supp}f_t=\Lambda(2\pi t)\operatorname{supp}f$. Track the center in Rindler coordinates and show that $\xi$ is fixed. If the original bump is Euclidean-radial in the coordinate plot, compute its transformed covariance matrix and show why it is generally not a circle of the “same width.”

**5. Unruh temperature in physical units.** Restore constants:
$$
T_U=\frac{\hbar a}{2\pi c k_B}.
$$
Compute $T_U$ for $a=g\approx9.8\,\mathrm{m\,s^{-2}}$ and $a=10^{20}\,\mathrm{m\,s^{-2}}$, and solve for the acceleration giving $T_U=1\,\mathrm K$. Check units at every step and discuss why direct detection is difficult.

**6. Modular flow never reaches the wedge boundary.** Show that for any test function $f$ supported strictly inside $W_R$ (i.e., the support is at finite distance from the null boundaries), the modular-flowed support $\mathrm{supp}(f \circ \Lambda^{\mathrm{boost}}(-2\pi t))$ remains strictly inside $W_R$ for every $t \in \mathbb{R}$. (*Hint:* Lorentz boosts are isometries of the wedge into itself.)

**Starred problems.**

**7\*. Modular operator on a double cone (Hislop–Longo/BGL).** State first the Hislop–Longo result for the free massless scalar, and then the Brunetti–Guido–Longo conformal-net extension under its hypotheses. For the vacuum algebra of a symmetric double cone $\mathcal{O}_r$, write $\Delta_{\mathcal{O}_r} = e^{-2\pi K_{\mathrm{conf}}}$, where $K_{\mathrm{conf}}$ generates the conformal subgroup fixing $\mathcal{O}_r$. Sketch the input (conformal covariance, vacuum cyclicity and separatingness, and intertwining with the wedge by a conformal transformation). Explain why this is not a theorem about every abstract theory carrying the label “2D CFT.”

**8\*. 4D massless scalar.** Repeat the Bogoliubov analysis for the 4D massless free scalar, restricted to a single Rindler-direction mode (the transverse momenta $\vec k_\perp$ become parameters; the right-mover decomposes into a continuum of 2D-like sectors labeled by $\vec k_\perp$). Verify the same $e^{2\pi\omega}$ structure in each sector.

**9\*. Positivity of $\Delta$ does not mean positivity of $K$.** The boost generator has spectrum $\mathbb{R}$, while
$$
\Delta_{W_R}=e^{-2\pi K}
$$
is positive. Use the spectral theorem to explain why $e^A$ is positive for every self-adjoint $A$, regardless of the sign of $\sigma(A)$. Determine the spectrum of $\Delta_{W_R}$ when $\sigma(K)=\mathbb{R}$. Explain why Reeh–Schlieder makes $\overline{\mathcal{A}(W_R)\Omega}=\mathcal{H}$, so there is no smaller “wedge subspace” on which $K$ becomes positive.

**10\*. Modular conjugation in 2D.** For the neutral massless derivative field, verify that $J=\Theta$ maps $\mathcal{A}(W_R)$ to $\mathcal{A}(W_L)$. Track both pieces:

- the geometric pullback $f\mapsto f^j$ with $j(x)=-x$; and
- antiunitarity, $JiJ^{-1}=-i$.

Conclude that $JW(f)J^{-1}=W(-f^j)$, not $W(f^j)$.

**11\*. Modular flow vs. proper-time flow.** For an observer at fixed $\xi = \xi_0$ in $W_R$, the proper-time evolution $\alpha_\tau = \mathrm{Ad}(e^{i\tau H_{\xi_0}})$ for some self-adjoint $H_{\xi_0}$ is *not* the modular flow $\sigma_t^{W_R}$. The two differ by the lapse factor: $\sigma_t^{W_R} = \alpha_{2\pi t / a}$. State precisely the relationship and explain why the modular flow is observer-independent (it depends only on the wedge, not on the choice of accelerated observer inside it).

## Self-study answer checkpoints

These checkpoints cover the core problems. Starred, project, and explicitly research-level problems remain source-led; they should be completed with the references and hypotheses named in the problem.

1. Taking absolute values removes the common $\Gamma(i\omega)$, $k^{-i\omega}$, and normalization factors. Squaring the remaining exponentials gives
   $$
   \frac{|\beta_{\omega k}|^2}{|\alpha_{\omega k}|^2}=e^{-2\pi\omega}.
   $$
2. With $r=e^{-2\pi\omega}$, the two relations imply $|\beta|^2=r/(1-r)$, hence
   $$
   \langle N_\omega\rangle=\frac{1}{e^{2\pi\omega}-1}
   $$
   for a narrow normalized packet, up to bandwidth corrections. A sharp-frequency expression still carries its delta normalization; no additional $1/(2\pi)$ is generated by a fictitious “Rindler volume.”
3. Covariance gives $\frac{d}{ds}|_0\,\operatorname{Ad}(e^{isK})W(f)=i[K,W(f)]$ on the common analytic core. Using
   $$
   W(f+sh)=e^{is\sigma(f,h)/2}W(f)W(sh)
   $$
   yields
   $$
   \left.\frac d{ds}W(f+sh)\right|_0
   =\frac i2\sigma(f,h)W(f)+iW(f)\phi(h).
   $$
   The derivative is not $W(h)$.
4. For $s=2\pi t$,
   $$
   \operatorname{supp}f_t=\Lambda(s)\operatorname{supp}f,
   \qquad
   (\xi_c,\eta_c)\longmapsto(\xi_c,\eta_c+s).
   $$
   If the original coordinate covariance is $vI$, the transformed covariance is
   $$
   v\Lambda(s)\Lambda(s)^T
   =v\begin{pmatrix}\cosh(2s)&\sinh(2s)\\[2pt]\sinh(2s)&\cosh(2s)\end{pmatrix},
   $$
   with eigenvalues $ve^{\pm2s}$; it is therefore not Euclidean-radial unless $s=0$.
5. Using current SI constants,
   $$
   \frac{T_U}{a}=4.0550\times10^{-21}\ \mathrm{K}\,(\mathrm{m\,s^{-2}})^{-1}.
   $$
   Thus $T_U(g)\simeq3.97\times10^{-20}\,\mathrm K$, $T_U(10^{20}\,\mathrm{m\,s^{-2}})\simeq0.406\,\mathrm K$, and $T_U=1\,\mathrm K$ requires $a\simeq2.47\times10^{20}\,\mathrm{m\,s^{-2}}$. The required accelerations and competing detector/environmental effects explain the experimental difficulty.
6. In null coordinates $u=x^1-x^0$ and $v=x^1+x^0$, the right wedge is $u,v>0$, while a boost of rapidity $s$ gives $u\mapsto e^{-s}u$ and $v\mapsto e^sv$. For compact support strictly inside the wedge, the minima of both coordinates remain positive for every finite $s=2\pi t$; the transformed compact support therefore never reaches either null boundary at finite modular time.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block C. Last revised 2026-09-29.*
