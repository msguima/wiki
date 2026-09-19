---
title: "Appendix B — Free-Field and Rindler Primer"
type: appendix
course: syllabus
modified: 2026-06-11
---

# Free-Field and Rindler Primer

This appendix collects the QFT-side prerequisites used in Block C and beyond. It is designed for a student who knows quantum mechanics but has limited prior exposure to QFT. **The course's modular conventions** (from Week 4 §6.1 and the note-quality template) are used throughout.

## B.1 Mass and Coordinates

We work in $(d+1)$-dimensional Minkowski space $\mathbb{R}^{1,d}$ with signature $(-,+,\ldots,+)$, metric $\eta = \mathrm{diag}(-1, +1, \ldots, +1)$, coordinates $x^\mu = (x^0, x^1, \ldots, x^d)$. The course's two main examples:
- $d = 1$: 2D Minkowski (one space dim + time). Most explicit calculations are here.
- $d = 3$: 4D Minkowski (three space dims + time). Physical case.

For most of the course we set $\hbar = c = 1$ and work in natural units.

## B.2 Distributions and Test Functions

A **test function** $f \in \mathcal{S}(\mathbb{R}^{1,d})$ is a Schwartz function: smooth, with all derivatives decaying faster than any polynomial. The dual space $\mathcal{S}'(\mathbb{R}^{1,d})$ consists of **tempered distributions**.

The smeared field $\phi(f) = \int d^{d+1}x\,f(x)\,\phi(x)$ pairs an operator-valued distribution $\phi$ with a test function $f$ to produce an honest operator.

**Fourier transform conventions** (used in Weeks 8–11):
$$
\tilde f(p) := \int d^{d+1}x\, f(x)\, e^{i p\cdot x}, \qquad f(x) = \int \frac{d^{d+1}p}{(2\pi)^{d+1}}\, \tilde f(p)\, e^{-i p \cdot x},
$$
with $p \cdot x = -p^0 x^0 + \vec p \cdot \vec x$ (Minkowski inner product).

For free fields, the on-shell measure restricts integration over $p^0$ to $\omega_p = \sqrt{|\vec p|^2 + m^2}$:
$$
\int \frac{d^{d+1}p}{(2\pi)^{d+1}}\,(2\pi)\delta(p^2 + m^2)\Theta(p^0)\, \tilde f(p) = \int \frac{d^d\vec p}{(2\pi)^d\,2\omega_p}\,\tilde f(\omega_p, -\vec p).
$$

## B.3 The Free Scalar Field

The free scalar field of mass $m \ge 0$ on Minkowski is the operator-valued distribution
$$
\phi(x) = \int \frac{d^d\vec p}{(2\pi)^d\sqrt{2\omega_p}}\,\left[a_{\vec p}\,e^{-i\omega_p x^0 + i\vec p\cdot\vec x} + a_{\vec p}^\dagger\,e^{+i\omega_p x^0 - i\vec p\cdot\vec x}\right],
$$
acting on Fock space $\mathcal{F} = \bigoplus_n \mathrm{Sym}^n(L^2(\mathbb{R}^d))$, with $[a_{\vec p}, a_{\vec p'}^\dagger] = (2\pi)^d\delta^d(\vec p - \vec p')$ and vacuum $a_{\vec p}|0_M\rangle = 0$.

**Smeared:** $\phi(f)$ is a (densely defined) self-adjoint operator for real $f \in \mathcal{S}$.

**Klein–Gordon equation:** $(\Box - m^2)\phi = 0$. As an operator identity on smeared fields: $\phi((\Box - m^2)f) = 0$ for $f \in \mathcal{S}$. Test functions related by $(\Box - m^2)$ give the same smeared field; this is the "test functions modulo the equation of motion" structure.

## B.4 Wightman Two-Point Function

The vacuum two-point function:
$$
W(f, g) := \langle 0_M | \phi(f)\,\phi(g) | 0_M\rangle = \int \frac{d^d\vec p}{(2\pi)^d 2\omega_p}\,\tilde f(\omega_p, -\vec p)^*\,\tilde g(\omega_p, -\vec p).
$$
Positive sesquilinear form on the complex test-function space (Week 8).

For unsmeared fields:
$$
W(x - y) := \langle 0_M|\phi(x)\phi(y)|0_M\rangle = \int \frac{d^d\vec p}{(2\pi)^d 2\omega_p}\,e^{-i\omega_p(x^0 - y^0) + i\vec p\cdot(\vec x - \vec y)}.
$$

**2D massless explicit form:**
$$
W(x - y) = -\frac{1}{4\pi}\log\!\big[-(x - y)^2 + i\epsilon(x^0 - y^0)\big].
$$

**4D massless explicit form:**
$$
W(x - y) = -\frac{1}{4\pi^2 [(x - y)^2 - i\epsilon(x^0 - y^0)]}.
$$

The $i\epsilon$ prescription regulates the light-cone singularity.

## B.5 Pauli–Jordan Distribution

The **commutator** $[\phi(x), \phi(y)] = i\,\Delta(x - y)\cdot\mathbf{1}$ is a $c$-number (the Pauli–Jordan distribution).

For real test functions $f, g$, the **symplectic form** is
$$
\sigma(f, g) := -i\,\langle 0_M|[\phi(f), \phi(g)]|0_M\rangle = \int d^{d+1}x\,d^{d+1}y\, f(x)\,\Delta(x - y)\,g(y).
$$
(B-R convention; matches Week 8 §3.2.)

**Properties:**
- $\sigma$ is real, bilinear, antisymmetric.
- Spacelike vanishing: $\sigma(f, g) = 0$ if $\mathrm{supp}(f)$ and $\mathrm{supp}(g)$ are spacelike separated.
- $\sigma(f, g) = 2\,\mathrm{Im}\,W(f, g)$ for real $f, g$.

**2D massless explicit form:**
$$
\Delta(x - y) = -\tfrac{1}{2}\,\mathrm{sgn}(x^0 - y^0)\,\Theta(-(x - y)^2).
$$
Sign $-\tfrac{1}{2}$ inside the future light cone of $y$, $+\tfrac{1}{2}$ inside the past, zero outside.

**4D massless explicit form:**
$$
\Delta(x - y) = \tfrac{1}{2\pi}\,\mathrm{sgn}(x^0 - y^0)\,\delta((x - y)^2).
$$
Delta function on the light cone, with sign from time ordering.

**2D massive form** ($m > 0$):
$$
\Delta(x - y) = -\tfrac{1}{2}\,\mathrm{sgn}(x^0 - y^0)\,J_0(m\sqrt{-(x - y)^2})\,\Theta(-(x - y)^2).
$$
Bessel function; oscillates inside the light cone.

## B.6 Weyl Operators (Week 8 §4)

For real $f \in \mathcal{S}$, the Weyl operator is $W(f) := e^{i\phi(f)}$ (unitary).

**Weyl relation:**
$$
W(f)\,W(g) = e^{-i\sigma(f, g)/2}\,W(f + g).
$$

Consequences:
- $W(f)^* = W(-f)$, $W(0) = 1$.
- If $\sigma(f, g) = 0$ (spacelike support), $W(f)$ and $W(g)$ commute.
- Vacuum expectation (Gaussian): $\langle 0_M|W(f)|0_M\rangle = e^{-W(f, f)/2}$ for real $f$.

## B.7 Local Algebras

For open $\mathcal{O} \subset \mathbb{R}^{1,d}$,
$$
\mathcal{A}(\mathcal{O}) := \{W(f): \mathrm{supp}(f) \subset \mathcal{O}\}''.
$$
This is the **local von Neumann algebra**.

**Net structure** (Week 9; Haag–Kastler axioms):
1. Isotony: $\mathcal{O}_1 \subset \mathcal{O}_2 \Rightarrow \mathcal{A}(\mathcal{O}_1) \subset \mathcal{A}(\mathcal{O}_2)$.
2. Locality: $\mathcal{O}_1, \mathcal{O}_2$ spacelike $\Rightarrow [\mathcal{A}(\mathcal{O}_1), \mathcal{A}(\mathcal{O}_2)] = 0$.
3. Covariance under $\mathcal{P}_+^\uparrow$.
4. Vacuum invariance.
5. Spectral condition $P^0 \ge 0$.

## B.8 Rindler Coordinates

The right Rindler wedge:
$$
W_R := \{x: x^1 > |x^0|\}.
$$
Rindler coordinates on $W_R$:
$$
x^1 = \xi\cosh\eta, \qquad x^0 = \xi\sinh\eta, \qquad \xi > 0,\; \eta \in \mathbb{R}.
$$
- $\xi$: "radial" coordinate, fixed-$\xi$ worldlines are uniformly accelerated.
- $\eta$: "Rindler time," $\eta \to \eta + s$ is the Lorentz boost.

**Metric in Rindler:** $ds^2 = -\xi^2\,d\eta^2 + d\xi^2 + d\vec x_\perp^2$. Lapse $\xi$.

**Observer at $\xi = \xi_0$:**
- Proper acceleration $a = 1/\xi_0$.
- Proper time $\tau = \xi_0\,\eta$.
- Modular time $t = \eta/(2\pi)$ relates to proper time as $\tau = 2\pi\xi_0\,t = 2\pi t/a$.

## B.9 Boost Generator

The boost subgroup $\Lambda^{\mathrm{boost}}(s): (x^0, x^1) \mapsto (\cosh s\,x^0 + \sinh s\,x^1, \sinh s\,x^0 + \cosh s\,x^1)$ preserves $W_R$ as a set. The unitary implementer on Hilbert space is $U(\Lambda^{\mathrm{boost}}(s)) = e^{-isK}$ where
$$
K = \int_{x^1 > 0} x^1\,T^{00}(0, \vec x)\,d^d \vec x - \int_{x^1 < 0}(-x^1)\,T^{00}(0, \vec x)\,d^d \vec x,
$$
the **boost generator**. $K\Omega_M = 0$ (vacuum is boost-invariant) but $K$ has full real spectrum on $\mathcal{H}$.

## B.10 Bisognano–Wichmann (Week 10)

In our convention,
$$
\Delta_{W_R} = e^{-2\pi K}, \qquad \sigma_t^{W_R}(a) = U(\Lambda^{\mathrm{boost}}(2\pi t))\,a\,U(\Lambda^{\mathrm{boost}}(2\pi t))^*.
$$
Modular flow = boost subgroup at rapidity $+2\pi t$. **Unruh temperature** $T_U = a/(2\pi)$ for an observer at $\xi = 1/a$.

## B.11 Bogoliubov Transformation in 2D Massless (Week 10 §4)

Decompose $\phi = \phi_R(x^-) + \phi_L(x^+)$ into right/left movers ($x^\pm = x^0 \pm x^1$). For right-movers in $W_R$:

**Minkowski modes**: $\phi_R(x^-) = \int_0^\infty \frac{dk}{\sqrt{4\pi k}}\,[a_k e^{-ikx^-} + h.c.]$.

**Rindler modes** in $W_R$ (positive-frequency w.r.t. $\eta$): $u_\omega^R(\eta) = \frac{1}{\sqrt{4\pi\omega}}\,e^{-i\omega\eta}$, with $b_\omega^R$ annihilation operators.

**Bogoliubov ratio**: $|\beta_{\omega k}|^2 / |\alpha_{\omega k}|^2 = e^{-2\pi\omega}$.

**Thermal occupation**: $\langle 0_M|(b_\omega^R)^\dagger b_\omega^R|0_M\rangle \propto 1/(e^{2\pi\omega} - 1)$ — Bose–Einstein at Rindler-time inverse temperature $2\pi$.

## B.12 Two-Sided Rindler (TFD; Week 15)

The left wedge $W_L = \{x: x^1 < -|x^0|\}$ is spacelike to $W_R$, and $[\mathcal{A}(W_R), \mathcal{A}(W_L)] = 0$.

The Minkowski vacuum, in Rindler modes, takes the **TFD form**:
$$
|0_M\rangle = \prod_\omega \frac{1}{\sqrt{Z_\omega}}\,\sum_{n_\omega} e^{-\pi n_\omega\,\omega}\,|n_\omega\rangle_R \otimes |n_\omega\rangle_L.
$$
This is the TFD of the Rindler-mode Hamiltonian at "temperature" $T_R = 1/(2\pi)$.

Modular operator for the right algebra: $\Delta_{\mathrm{Mink}}^{(W_R)} = e^{-2\pi(K_R - K_L)}$.

## B.13 What's Used Where

| Topic | Week |
|---|---|
| Smeared fields and Weyl operators | 8 |
| Wightman function and Pauli–Jordan | 8 |
| Local algebras and Haag–Kastler axioms | 9 |
| Reeh–Schlieder (cyclic-separating for local algebras) | 9 |
| Rindler coordinates and boost generator | 10 |
| Bisognano–Wichmann + Bogoliubov verification | 10 |
| Bell–CHSH on wedges | 11 |
| Type III$_1$ classification of local algebras | 12 |
| Free-field Rindler crossed product | 13 |
| Dressed entropy on Rindler crossed product | 14 |
| TFD identification of Minkowski vacuum | 15 |

## B.14 Further Reading

- Streater & Wightman, *PCT, Spin and Statistics, and All That* (Wightman axioms, ch. 3).
- Haag, *Local Quantum Physics* (the standard AQFT reference).
- Birrell & Davies, *Quantum Fields in Curved Space* (Rindler quantization, ch. 4).
- Witten, "Notes on some entanglement properties of QFT," arXiv:1803.04993 (modern algebraic introduction; consistent with our conventions).
- Crispino, Higuchi, Matsas, "The Unruh effect and its applications," *Rev. Mod. Phys.* 80 (2008) 787 (Unruh effect review).
