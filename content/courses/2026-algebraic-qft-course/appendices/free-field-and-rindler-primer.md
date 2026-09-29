---
title: "Appendix B — Free-Field and Rindler Primer"
type: appendix
course: syllabus
modified: 2026-08-24
---

# Free-Field and Rindler Primer

This appendix collects the QFT-side prerequisites used in Block C and beyond. It is designed for a student who knows quantum mechanics but has limited prior exposure to QFT. **The course's modular conventions** (from Week 4 §6.1 and the note-quality template) are used throughout.

## B.1 Spacetime Conventions

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
\int \frac{d^{d+1}p}{(2\pi)^{d+1}}\,(2\pi)\delta(p^2 + m^2)\Theta(p^0)\, \tilde f(p) = \int \frac{d^d\vec p}{(2\pi)^d\,2\omega_p}\,\tilde f(\omega_p, \vec p).
$$

## B.3 The Free Scalar Field

The free scalar field of mass $m \ge 0$ on Minkowski is the operator-valued distribution
$$
\phi(x) = \int \frac{d^d\vec p}{(2\pi)^d\sqrt{2\omega_p}}\,\left[a_{\vec p}\,e^{-i\omega_p x^0 + i\vec p\cdot\vec x} + a_{\vec p}^\dagger\,e^{+i\omega_p x^0 - i\vec p\cdot\vec x}\right],
$$
acting on Fock space $\mathcal{F} = \bigoplus_n \mathrm{Sym}^n(L^2(\mathbb{R}^d))$, with $[a_{\vec p}, a_{\vec p'}^\dagger] = (2\pi)^d\delta^d(\vec p - \vec p')$ and vacuum $a_{\vec p}|0_M\rangle = 0$.

**Smeared:** on the finite-particle domain, $\phi(f)$ is symmetric for real
$f\in\mathcal S$ and is essentially self-adjoint there. Its closure is the
self-adjoint operator used to define $W(f)=e^{i\phi(f)}$.

**Klein–Gordon equation:** $(\Box - m^2)\phi = 0$. As an operator identity on smeared fields: $\phi((\Box - m^2)f) = 0$ for $f \in \mathcal{S}$. Test functions related by $(\Box - m^2)$ give the same smeared field; this is the "test functions modulo the equation of motion" structure.

## B.4 Wightman Two-Point Function

On the complexified test-function space, define the positive-frequency
wavefunction
$$
f_+(\vec p):=\int d^{d+1}x\,f(x)
e^{i\omega_p x^0-i\vec p\cdot\vec x}
=\tilde f(-\omega_p,-\vec p).
$$
The positive sesquilinear two-point form is then
$$
W(f,g):=\langle0_M|\phi(f)^*\phi(g)|0_M\rangle
=\int\frac{d^d\vec p}{(2\pi)^d2\omega_p}\,
\overline{f_+(\vec p)}g_+(\vec p).
$$
For real $f$ and $g$, this is the usual smeared Wightman function
$\langle0_M|\phi(f)\phi(g)|0_M\rangle$. Naming $f_+$ avoids hiding a
Fourier-sign choice in later calculations.

For unsmeared fields:
$$
W(x - y) := \langle 0_M|\phi(x)\phi(y)|0_M\rangle = \int \frac{d^d\vec p}{(2\pi)^d 2\omega_p}\,e^{-i\omega_p(x^0 - y^0) + i\vec p\cdot(\vec x - \vec y)}.
$$

**Two-dimensional massless form, with an infrared qualification.** There is
no ordinary Poincaré-invariant vacuum for the unsmeared massless scalar field
including its zero mode. On the zero-integral test-function subspace (or for
the derivative field), one may use the boundary value
$$
W_\epsilon(x-y)
=-\frac{1}{4\pi}\log\!\left[
\mu^2\big(-(\Delta t-i\epsilon)^2+(\Delta x)^2\big)
\right],
$$
up to an additive infrared-scale-dependent constant that drops out on that
subspace. Here $\Delta t=x^0-y^0$ and $\Delta x=x^1-y^1$.

**Four-dimensional massless form:**
$$
W_\epsilon(x-y)
=\frac{1}{4\pi^2}
\frac{1}{-(\Delta t-i\epsilon)^2+|\Delta\vec x|^2}.
$$

The limit $\epsilon\downarrow0$ defines a tempered-distribution boundary
value. It does not turn the light-cone singularity into an ordinary pointwise
function; smearing remains essential.

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
\Delta(x-y)=-\frac{1}{2\pi}\,\operatorname{sgn}(x^0-y^0)\,
\delta((x-y)^2).
$$
The minus sign agrees with
$[\phi(x),\phi(y)]=i\Delta(x-y)$ and the equal-time condition
$\partial_{x^0}\Delta(0,\vec x-\vec y)=-\delta^d(\vec x-\vec y)$.

**2D massive form** ($m > 0$):
$$
\Delta(x - y) = -\tfrac{1}{2}\,\mathrm{sgn}(x^0 - y^0)\,J_0(m\sqrt{-(x - y)^2})\,\Theta(-(x - y)^2).
$$
Bessel function; oscillates inside the light cone.

## B.6 Weyl Operators (Week 8 §4)

For real $f$ in the Klein--Gordon symplectic test-function space, the Weyl
operator is $W(f):=e^{i\phi(f)}$. In the two-dimensional massless example we
also impose the zero-mode restriction described in §B.4.

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
5. Spectral condition: the joint energy--momentum spectrum lies in the closed
   future light cone, $\operatorname{sp}(P)\subset\overline V_+$.

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

The boost subgroup
$\Lambda^{\mathrm{boost}}(u):(x^0,x^1)\mapsto
(\cosh u\,x^0+\sinh u\,x^1,
\sinh u\,x^0+\cosh u\,x^1)$ preserves $W_R$. We fix the active covariance
convention
$$
U(\Lambda(u))\phi(x)U(\Lambda(u))^*=\phi(\Lambda(u)x),
\qquad U(\Lambda(u))=e^{iuK},
$$
where, at $x^0=0$,
$$
K = \int_{x^1 > 0} x^1\,T^{00}(0, \vec x)\,d^d \vec x - \int_{x^1 < 0}(-x^1)\,T^{00}(0, \vec x)\,d^d \vec x,
$$
the **global boost generator**. The two displayed integrals are simply
$\int_{\mathbb R^d}x^1T^{00}(0,\vec x)d^d\vec x$ split at $x^1=0$.
$K\Omega_M=0$ (vacuum invariance), while $K$ has two-sided spectrum.

A boost changes $\eta$ and leaves $\xi$ fixed. It moves an observer along one
uniformly accelerated orbit; it does not move that observer toward the
bifurcation surface. Approaching the horizon or bifurcation surface requires
the separate limit $\xi\downarrow0$.

## B.10 Bisognano–Wichmann (Week 10)

In our convention,
$$
\Delta_{W_R} = e^{-2\pi K}, \qquad \sigma_t^{W_R}(a) = U(\Lambda^{\mathrm{boost}}(2\pi t))\,a\,U(\Lambda^{\mathrm{boost}}(2\pi t))^*.
$$
Modular flow = boost subgroup at rapidity $+2\pi t$. **Unruh temperature** $T_U = a/(2\pi)$ for an observer at $\xi = 1/a$.

## B.11 Bogoliubov Transformation in 2D Massless (Week 10 §4)

Decompose $\phi = \phi_R(x^-) + \phi_L(x^+)$ into right/left movers ($x^\pm = x^0 \pm x^1$). For right-movers in $W_R$:

**Minkowski modes**: $\phi_R(x^-) = \int_0^\infty \frac{dk}{\sqrt{4\pi k}}\,[a_k e^{-ikx^-} + h.c.]$.

**Rindler modes** in $W_R$ (positive-frequency with respect to $\eta$): for
the right-moving sector one may take
$$
u_\omega^R(x^-)
=\frac{\Theta(-x^-)}{\sqrt{4\pi\omega}}(-a x^-)^{i\omega/a},
\qquad x^-=-\xi e^{-\eta}.
$$
Along a fixed-$\xi$ orbit this is a $\xi$-dependent phase times
$e^{-i\omega\eta/a}$. Setting $a=1$ gives the dimensionless convention used
in Week 10. The associated annihilation operators are denoted $b_\omega^R$.

**Bogoliubov ratio**:
$$
\frac{|\beta_{\omega k}|^2}{|\alpha_{\omega k}|^2}
=e^{-2\pi\omega/a}.
$$
In the dimensionless convention $a=1$, this is $e^{-2\pi\omega}$.

**Thermal occupation**:
$$
\langle 0_M|(b_\omega^R)^\dagger b_\omega^R|0_M\rangle
\propto \frac{1}{e^{2\pi\omega/a}-1}.
$$
This is Bose--Einstein at proper-time temperature $a/(2\pi)$. With $a=1$,
it is equivalently thermal at dimensionless Rindler-time inverse temperature
$2\pi$.

## B.12 Two-Sided Rindler (TFD; Week 15)

The left wedge $W_L = \{x: x^1 < -|x^0|\}$ is spacelike to $W_R$, and $[\mathcal{A}(W_R), \mathcal{A}(W_L)] = 0$.

With a mode regulator, the Minkowski vacuum takes the familiar **TFD form**:
$$
|0_M\rangle = \prod_\omega \frac{1}{\sqrt{Z_\omega}}\,\sum_{n_\omega} e^{-\pi n_\omega\,\omega}\,|n_\omega\rangle_R \otimes |n_\omega\rangle_L.
$$
This is the TFD of the regulated Rindler-mode Hamiltonian at dimensionless
temperature $T_R=1/(2\pi)$. In continuum AQFT the product and tensor
factorization are formal mnemonic devices: the wedge algebras are type III
and the vacuum is handled directly as a cyclic-separating vector.

In the regulated bipartite model, the modular operator for the right algebra is
$$
\Delta_R=e^{-2\pi(K_R-K_L)}.
$$
This is one-sided modular data acting in a purification; it is not a thermal
density matrix for the joint algebra.

## B.13 What's Used Where

| Topic | Week |
|---|---|
| Smeared fields and Weyl operators | 8 |
| Wightman function and Pauli–Jordan | 8 |
| Local algebras and Haag–Kastler axioms | 9 |
| Reeh--Schlieder cyclicity; separation from locality when the causal complement has interior | 9 |
| Rindler coordinates and boost generator | 10 |
| Bisognano–Wichmann + Bogoliubov verification | 10 |
| Bell–CHSH on wedges | 11 |
| Type III$_1$ classification of local algebras | 12 |
| Free-field Rindler crossed product | 13 |
| Dressed entropy on Rindler crossed product | 14 |
| Regulated TFD picture and its type-III qualification | 15 |

## B.14 Further Reading

- Streater & Wightman, *PCT, Spin and Statistics, and All That* (Wightman axioms, ch. 3).
- Haag, *Local Quantum Physics* (the standard AQFT reference).
- Birrell & Davies, *Quantum Fields in Curved Space* (Rindler quantization, ch. 4).
- Witten, "Notes on some entanglement properties of QFT," arXiv:1803.04993 (modern algebraic introduction; consistent with our conventions).
- Crispino, Higuchi, Matsas, "The Unruh effect and its applications," *Rev. Mod. Phys.* 80 (2008) 787 (Unruh effect review).
