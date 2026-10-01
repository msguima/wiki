---
title: "Lecture 11 — A conformal ball and its modular clock"
type: lecture-notes
edition: "2.2 — rewritten at the AQFT standard"
lecture: 11
semester: 1
week: 9
hours: 4
prerequisites: "Lectures 3, 9 and 10; integration in spherical coordinates"
status: "rewritten 2026-09-30, pending instructor review; conformal maps, modular vector field and ball integrals derived and symbolically checked, geometric modular flow of balls stated with hypotheses, first law proved in finite dimensions with an exact two-dimensional test"
modified: 2026-09-30
---

# Lecture 11 — A conformal ball and its modular clock

> *A wedge is unbounded, and holography needs finite regions of the boundary. Conformal symmetry supplies one whose modular flow can still be computed: a ball in the vacuum of a conformal field theory. We construct the conformal transformation that maps the Rindler wedge onto the causal diamond of a ball, push the boost of Lecture 10 forward to a conformal Killing vector of the diamond, and integrate its flow. The modular Hamiltonian is then a weighted integral of the energy density, with a weight that vanishes on the entangling surface and reduces to the Rindler weight near it. A second map, due to Casini, Huerta and Myers, turns the diamond into a static patch of hyperbolic space in which the modular flow is time translation at temperature $1/2\pi R$. The entanglement first law follows from the positivity of relative entropy, and we test the law, and the relative entropy itself, against the exact entropy of a thermal interval in two dimensions.*

## How to use this lecture

**Classroom core, two meetings of two hours.** The first meeting covers the history (§1, 10 minutes), the diamond (§2, 5 minutes), the conformal map from the wedge (§3, 40 minutes), the modular flow and its clocks (§4, 25 minutes), and the modular Hamiltonian (§5, 25 minutes), leaving 15 minutes for Checkpoint 1. The second meeting covers the first law (§6, 25 minutes), the homogeneous perturbation (§7, 15 minutes), the thermal interval in two dimensions (§8, 35 minutes), and the bridge to gravity (§10, 10 minutes), with 35 minutes for Checkpoint 2 and Problems 3 and 4; Problems 1, 2, 5 and 6 complete the core assignment. These allocations are proposals and have not been tested in class.

**Self-study.** The map to hyperbolic space and the temperature $1/2\pi R$ (§9), the conservation of the conformal current, the two-sided modular Hamiltonian, and Problems 7–12.

**Research extension.** Deformations of the entangling surface, two intervals, and the holographic first law, in Problems 13–15; Lecture 22 turns the first law into the linearized Einstein equations.

**Prerequisites.** Lecture 3 for modular Hamiltonians and relative entropy in finite dimensions, Lecture 9 for relative entropy on general algebras, Lecture 10 for the Bisognano–Wichmann theorem and its conventions. Integration in spherical coordinates and the entropy of a thermal state.

**What this lecture establishes.** The conformal maps, the modular vector field, its flow and the ball integrals are exact calculations, checked symbolically. The identification of the vacuum modular flow of a ball with this conformal flow is stated with its hypotheses, following Hislop and Longo for the free massless scalar and Brunetti, Guido and Longo for conformal nets, and sketched by conjugating the wedge theorem. The first law is proved in finite dimensions and formulated through relative entropy for type III. The thermal entropy of an interval is used as an exact conformal field theory input, derived in Lecture 16.

## 0. Reading

**Primary.**

- H. Casini, M. Huerta, R. C. Myers, [Towards a derivation of holographic entanglement entropy](https://arxiv.org/abs/1102.0440) (2011), Section 2.
- D. D. Blanco, H. Casini, L.-Y. Hung, R. C. Myers, [Relative Entropy and Holography](https://arxiv.org/abs/1305.3182) (2013).
- P. D. Hislop, R. Longo, Modular structure of the local algebras associated with the free massless scalar field theory, *Commun. Math. Phys.* 84 (1982) 71.

**Secondary.**

- R. Brunetti, D. Guido, R. Longo, [Modular Structure and Duality in Conformal Quantum Field Theory](https://arxiv.org/abs/funct-an/9302008) (1993).
- G. Wong, I. Klich, L. A. Pando Zayas, D. Vaman, [Entanglement Temperature and Entanglement Entropy of Excited States](https://arxiv.org/abs/1305.3291) (2013).
- J. Bhattacharya, M. Nozaki, T. Takayanagi, T. Ugajin, [Thermodynamical Property of Entanglement Entropy for Excited States](https://arxiv.org/abs/1212.1164) (2012).
- J. Cardy, E. Tonni, [Entanglement hamiltonians in two-dimensional conformal field theory](https://arxiv.org/abs/1608.01283) (2016).

**Optional research reading.**

- N. Lashkari, M. B. McDermott, M. Van Raamsdonk, [Gravitational Dynamics From Entanglement "Thermodynamics"](https://arxiv.org/abs/1308.3716) (2013), and T. Faulkner, M. Guica, T. Hartman, R. C. Myers, M. Van Raamsdonk, [Gravitation from Entanglement in Holographic CFTs](https://arxiv.org/abs/1312.7856) (2014).
- T. Faulkner, R. G. Leigh, O. Parrikar, H. Wang, [Modular Hamiltonians for Deformed Half-Spaces and the Averaged Null Energy Condition](https://arxiv.org/abs/1605.08072) (2016).
- H. Casini, M. Huerta, [Reduced density matrix and internal dynamics for multicomponent regions](https://arxiv.org/abs/0903.5284) (2009).
- V. Rosenhaus, M. Smolkin, [Entanglement Entropy: A Perturbative Calculation](https://arxiv.org/abs/1403.3733) (2014).

## 1. Can a finite region have a geometric clock?

The wedge of Lecture 10 is the region whose vacuum modular flow is known to be geometric, up to Poincaré transformations, in every theory satisfying the Bisognano–Wichmann hypotheses. For a bounded region of a generic theory the flow is not expected to be induced by any spacetime transformation, but conformal symmetry changes this. In 1982 Hislop and Longo showed that for the free massless scalar field the vacuum modular group of a double cone, the causal diamond of a ball, is a one-parameter group of conformal transformations, obtained from the wedge by a conformal map. Brunetti, Guido and Longo extended the result in 1993 to general conformal nets: using a theorem of Borchers, they derived the Bisognano–Wichmann property of wedges from conformal covariance, and transported it to double cones.

The result was rediscovered in the study of entanglement. In 2011 Casini, Huerta and Myers mapped the causal diamond of a ball onto hyperbolic space times time and observed that the vacuum state of the ball becomes a thermal state there, at temperature $1/2\pi R$. In a holographic theory that thermal state is dual to a black hole with a hyperbolic horizon, and its entropy is the area of the Ryu–Takayanagi surface; this is the argument of Lecture 16, §7. In 2012 Bhattacharya, Nozaki, Takayanagi and Ugajin found that small excitations of a holographic state change the entanglement entropy of a small region in proportion to its energy, with an effective temperature inversely proportional to the size of the region. The following year Blanco, Casini, Hung and Myers explained the law as the first-order vanishing of relative entropy, and Wong, Klich, Pando Zayas and Vaman derived it in field theory from the local form of the modular Hamiltonian. Lashkari, McDermott and Van Raamsdonk, and Faulkner, Guica, Hartman, Myers and Van Raamsdonk, then showed that in holography the same law, imposed on every ball, is equivalent to the linearized Einstein equations, which is the subject of Lecture 22.

This lecture supplies the boundary side of that argument. It derives the modular flow of a ball explicitly, writes its modular Hamiltonian, and proves the first law in the form in which Lecture 22 uses it.

## 2. The ball and its causal diamond

In a conformal field theory in $d$ spacetime dimensions, consider the ball $B=\{t=0,\ r<R\}$, with $r=|\mathbf x|$. Its causal development is the diamond

$$
D(B)=\{|t|+r<R\},
$$

with tips at $(t,\mathbf x)=(\pm R,\mathbf 0)$, bounded by the future and past light cones of the tips. The entangling surface $\partial B$ is the sphere $t=0$, $r=R$. By the time-slice property of Lecture 9 the algebra of the ball is the algebra of the diamond, $\mathcal A(B)=\mathcal A(D(B))$.

## 3. From the wedge to the diamond

Let $e_1$ be the unit vector along $x^1$, and let a dot denote the Minkowski product. For a point $X$ of the right wedge $W_R=\{X^1>|X^0|\}$ define

$$
x^\mu=-R\,e_1^\mu+\frac{2R^2\,(X^\mu+R\,e_1^\mu)}{(X+Re_1)\cdot(X+Re_1)} .
$$

The map is a translation by $Re_1$, an inversion $Y^\mu\mapsto Y^\mu/Y\cdot Y$, a dilation by $2R^2$ and a translation by $-Re_1$. It has three properties, all checked symbolically in $d=4$ in the course scripts.

*It is conformal.* An inversion multiplies the metric by $(Y\cdot Y)^{-2}$, and translations and dilations are conformal, so

$$
\eta_{\mu\nu}\,dx^\mu dx^\nu=\Omega(X)^2\,\eta_{\mu\nu}\,dX^\mu dX^\nu,
\qquad
\Omega(X)=\frac{2R^2}{(X+Re_1)\cdot(X+Re_1)} .
$$

The map is smooth on the wedge, because $Y=X+Re_1$ is spacelike there: $|X^0|<X^1<X^1+R$ gives $Y\cdot Y=(X^1+R)^2-(X^0)^2+|\mathbf X_\perp|^2>0$.

*It maps the wedge onto the diamond.* On the slice $X^0=0$ everything is Euclidean. Since $x+Re_1=2R^2Y/|Y|^2$,

$$
|x|^2=|x+Re_1|^2-2R\,(x+Re_1)\cdot e_1+R^2=R^2+\frac{4R^3\,(R-Y^1)}{|Y|^2},
$$

and $Y^1=X^1+R$. Therefore the half-space $X^1>0$ is mapped into the ball $|x|<R$, and the edge $X^1=0$ onto the sphere $|x|=R$ with the point $-Re_1$ removed, which is the image of spatial infinity. The origin of the wedge goes to the point $Re_1$ of the sphere. The rest of the wedge is the causal development of its $X^0=0$ slice, and conformal maps preserve causal structure, so the wedge goes onto the diamond. At the origin $\partial x^0/\partial X^0=2>0$, so the future of the wedge goes to the future of the diamond.

*It pushes the boost forward to a conformal Killing vector.* The rescaled boost $2\pi(X^1\partial_0+X^0\partial_1)$ of Lecture 10 becomes

$$
\zeta=\frac\pi R\left[\left(R^2-t^2-r^2\right)\partial_t-2t\,x^i\partial_i\right].
$$

In two dimensions the computation is short (Problem 7). With null coordinates $X^\pm=X^0\pm X^1$ and $x^\pm=t\pm x$, the map becomes

$$
x^+=R\,\frac{R+X^-}{R-X^-},\qquad x^-=R\,\frac{X^+-R}{X^++R},
$$

so each null coordinate of the diamond is a Möbius function of one null coordinate of the wedge. On the wedge, $X^+\in(0,\infty)$ and $X^-\in(-\infty,0)$ are both mapped onto $(-R,R)$, which are the null coordinates of the diamond.

The map exchanges the two null directions, so it reverses spatial orientation. Composing it with the reflection $x^1\mapsto-x^1$, which maps the diamond and $\zeta$ to themselves, gives a map that preserves both orientations, an element of the identity component of the conformal group, with the same pushforward. This matters because a conformal field theory need not be parity invariant, while the identity component of the conformal group acts unitarily on its vacuum Hilbert space and leaves the vacuum invariant.

> **Physical picture: the edge of the wedge becomes a sphere.** The inversion bends the two null half-planes that bound the wedge into the two light cones that bound the diamond, and it bends the edge, a flat $(d-2)$-plane, into the entangling sphere. Spatial infinity of the wedge goes to the single point $-Re_1$ of the sphere, the far future and past of the accelerated orbits to the two tips, and null infinity to the null generators of the diamond boundary that join $-Re_1$ to the tips. Near the edge the map is a dilation by a finite factor, so locally the entangling sphere looks like the edge of a wedge. This is why the ball's modular Hamiltonian, derived below, reduces near $\partial B$ to the Rindler form of Lecture 10.

## 4. The flow and its clocks

The vector field $\zeta$ is timelike and future directed inside the diamond, null on its boundary, and vanishes on the entangling sphere and at the two tips. At $t=0$ it is purely temporal, $\zeta=\frac\pi R(R^2-r^2)\partial_t$.

The flow is easy to integrate along radial null coordinates $x^\pm=t\pm r$; in two dimensions the same formulas hold with the null coordinates $t\pm x$ of §3. Since $\zeta^t\pm\zeta^r=\frac\pi R\left[R^2-t^2-r^2\mp2tr\right]=\frac\pi R\left[R^2-(x^\pm)^2\right]$,

$$
\frac{dx^\pm}{ds}=\frac\pi R\left[R^2-(x^\pm)^2\right],
$$

and separation of variables gives

$$
x^\pm(s)=R\tanh\left[\pi s+\operatorname{artanh}\frac{x^\pm(0)}R\right].
$$

Equivalently, the coordinates

$$
u^\pm=\log\frac{R+x^\pm}{R-x^\pm}=2\operatorname{artanh}\frac{x^\pm}R
$$

translate by $2\pi s$. A translation of $u^\pm$ is the same exponential rescaling of null coordinates that described a wedge boost, which verifies both the normalization of $\zeta$ and the preservation of the diamond. As $s\to+\infty$ both $x^+$ and $x^-$ tend to $R$, so every orbit ends at the future tip, and as $s\to-\infty$ it starts at the past tip.

At the center the orbit is $t(s)=R\tanh\pi s$, with $dt/ds=\pi R\operatorname{sech}^2\pi s$. The whole infinite range of modular time fits inside the finite proper-time interval $-R<t<R$, and the conversion between modular time and proper time is not constant along the orbit. At $t=0$ each orbit is momentarily at rest, and there the orbit through the radius $r$ moves at $d\tau/ds=\frac\pi R(R^2-r^2)$, so the KMS period $s\to s+i$ corresponds to an inverse proper temperature

$$
\beta_{\mathrm{loc}}(r)=\frac{\pi\,(R^2-r^2)}R=2\pi\,\frac{R^2-r^2}{2R}.
$$

Near the sphere, with $r=R-\delta$, this is $2\pi\delta+O(\delta^2/R)$, the Rindler value $2\pi\times$distance of Lecture 10. At the center it is $\pi R$. The figure shows the orbits and the slices of constant modular time.

![[ads-cft-diamond-modular-flow.svg|Left: the causal diamond of an interval with the orbits of the modular flow, which run from the past tip to the future tip, and the slices of constant modular time, which all end on the entangling surface. Right: for a thermal state of a two-dimensional conformal field theory, the changes of the modular energy and of the entanglement entropy of an interval, and their difference, the relative entropy, as functions of the product of the radius and the temperature.]]

**Checkpoint 1.** An orbit starts at $t=0$, $r=r_0<R$. Where does it end, and how does the modular time at which it passes a given proper time depend on $r_0$?

**Answer.** It ends at the future tip, since $x^\pm\to R$. Along it $u^\pm(s)=u^\pm(0)+2\pi s$, so the modular time needed to reach a given point depends on $r_0$ through $u^\pm(0)=\pm\log\frac{R+r_0}{R-r_0}$: orbits near the sphere take longer, in modular time, to cover the same proper time.

## 5. The modular Hamiltonian

In a conformal field theory the stress tensor is conserved and traceless. For a conformal Killing vector $\zeta$, with $\partial_\mu\zeta_\nu+\partial_\nu\zeta_\mu=\frac2d(\partial\cdot\zeta)\,\eta_{\mu\nu}$, the current $J^\mu=T^{\mu\nu}\zeta_\nu$ is therefore conserved (Problem 8), and its charge on any Cauchy surface of the diamond is the same. On the slice $t=0$,

$$
K_B=2\pi\int_{r<R}d^{d-1}x\,\frac{R^2-r^2}{2R}\,T_{00}(0,\mathbf x)+C,
$$

where the constant $C$ normalizes a regulated state and drops out of every variation.

**Claim (geometric modular flow of balls). Stated only — refs: Hislop–Longo 1982; Brunetti–Guido–Longo 1993.** In the vacuum of a conformal field theory, the modular flow of the ball algebra is the flow of $\zeta$: $\sigma_s(A)=U(g_s)AU(g_s)^\dagger$, where $g_s$ is the conformal transformation obtained by following $\zeta$ for a parameter $s$ and $U$ is its unitary implementer. Hislop and Longo prove this for the free massless scalar, and Brunetti, Guido and Longo for conformal nets with positive energy, in which they also derive the Bisognano–Wichmann property of wedges.

*Sketch.* Let $\varphi$ be the orientation-preserving conformal map of §3 and $U(\varphi)$ its unitary implementer. Covariance gives $U(\varphi)\mathcal A(W_R)U(\varphi)^\dagger=\mathcal A(D(B))$, and $U(\varphi)\Omega=\Omega$. The modular objects of a pair (algebra, vector) transform covariantly under a unitary that maps one pair to the other, so $\Delta_{D(B)}=U(\varphi)\Delta_{W_R}U(\varphi)^\dagger$, and the modular flow of the diamond is $\varphi$ composed with the boost and with $\varphi^{-1}$, which is the flow of $\zeta$. The steps that require care are the unitary implementation of a conformal map that does not preserve Minkowski space as a whole, and the domains; these are the content of the cited theorems. $\square$

The full modular Hamiltonian of Lecture 3 is two-sided, as for the wedge:

$$
\widehat K_B=2\pi\int_{t=0}d^{d-1}x\,\frac{R^2-r^2}{2R}\,T_{00}(0,\mathbf x),
$$

integrated over the whole slice, with a weight that is positive inside the ball and negative outside. It is the charge of $\zeta=\pi R\,\partial_t+\frac\pi R\,\xi_{e_0}$, where $\xi_b=2(b\cdot x)x^\mu\partial_\mu-x^2b^\mu\partial_\mu$ is the special conformal vector field of Lecture 12 with $b$ along the time direction, which equals $-r^2\partial_t$ at $t=0$. The two-sided generator thus combines the Hamiltonian with a special conformal charge, and it annihilates the vacuum because both do. The one-sided $K_B$ is the regulated notation used in the rest of this lecture.

The weight vanishes on the entangling sphere, reduces to the Rindler weight $\delta$ near it, and reaches $R/2$ at the center. Note that the claim concerns the vacuum and the ball: a generic excited state, or a deformed region, has a modular Hamiltonian that is not of this local form, and two disjoint intervals of the free fermion already have a nonlocal one (Problem 14).

> **Physical picture: a local temperature, read with care.** One may read $\beta_{\mathrm{loc}}(r)$ as a profile of inverse temperature on the slice $t=0$: the vacuum restricted to the ball looks like a Gibbs state of $K_B$, which weights the energy density near the edge by the Rindler factor and the energy density at the center by $R/2$. This is a description of the generator, exact in the sense of the claim. It does not mean that the vacuum is a fluid in local equilibrium: correlation functions inside the ball are those of the vacuum, and the profile refers to the modular flow, which for $r\neq0$ does not move along worldlines of constant $r$.

## 6. The first law of entanglement

The first law is a property of entropy, and it holds before any physical interpretation. For a faithful finite reference state $\sigma=e^{-K_\sigma}/\operatorname{Tr}e^{-K_\sigma}$, consider a family $\rho(\lambda)=\sigma+\lambda\,\delta\rho+O(\lambda^2)$ with $\operatorname{Tr}\delta\rho=0$. Differentiating $S=-\operatorname{Tr}\rho\log\rho$ gives

$$
\left.\frac{dS}{d\lambda}\right|_0=-\operatorname{Tr}\bigl(\delta\rho\,\log\sigma\bigr)=\left.\frac d{d\lambda}\langle K_\sigma\rangle_{\rho(\lambda)}\right|_0 .
$$

Noncommutativity adds no term: under the trace, $\frac d{d\lambda}\operatorname{Tr}\rho\log\rho=\operatorname{Tr}\dot\rho(\log\rho+I)$, and normalization removes the identity. [Proved.] More generally, for any two states,

$$
D(\rho\Vert\sigma)=\Delta\langle K_\sigma\rangle-\Delta S\geq0,
$$

where the differences are taken between $\rho$ and $\sigma$. The relative entropy is minimized at $\rho=\sigma$, so its first derivative vanishes there, and this is the first law $\delta S=\delta\langle K_\sigma\rangle$. Its second derivative is the Fisher information of the family, which is nonnegative. The inequality $\Delta S\leq\Delta\langle K_\sigma\rangle$ therefore holds for every $\rho$, with equality at first order and a gap from second order.

For the ball in the continuum there is no $K_\sigma$ as an operator and no finite $S$, but the relative entropy is defined (Lecture 9), and the combination above is how one states the law: for a family of states $\omega_\lambda$ near the vacuum, $D_{\mathcal A(B)}(\omega_\lambda\Vert\omega)=O(\lambda^2)$, and the regulated entropy change is defined as $\Delta S=\Delta\langle K_B\rangle-D$, with $\Delta\langle K_B\rangle$ computed from the stress tensor. A subtraction of two unspecified infinities is not a definition, and it is not needed. The first law contains no gravity, and no assumption about the theory beyond the form of $K_B$.

## 7. A homogeneous perturbation

If a state changes the energy density by an amount $\delta\mathcal E$ approximately constant over the ball, the first law gives

$$
\delta S_B=2\pi\,\delta\mathcal E\,\Omega_{d-2}\int_0^Rdr\,r^{d-2}\,\frac{R^2-r^2}{2R}=\frac{2\pi\,\Omega_{d-2}R^d}{d^2-1}\,\delta\mathcal E,
$$

where $\Omega_{d-2}$ is the area of the unit sphere $S^{d-2}$. The integral is $\frac1{2R}\left[\frac{R^{d+1}}{d-1}-\frac{R^{d+1}}{d+1}\right]$. Since the energy in the ball is $\delta E_B=\Omega_{d-2}R^{d-1}\delta\mathcal E/(d-1)$,

$$
\delta S_B=\frac{2\pi R}{d+1}\,\delta E_B .
$$

The entanglement entropy of a small ball thus responds to a small change of energy as a thermal system would at the temperature $T_{\mathrm{ent}}=(d+1)/2\pi R$, inversely proportional to its size. This is the relation found holographically by Bhattacharya, Nozaki, Takayanagi and Ugajin. It holds to first order, for the stated perturbation, and $T_{\mathrm{ent}}$ is not the temperature of anything in the state.

## 8. Worked example: the thermal interval in two dimensions

A two-dimensional conformal field theory with $c=\bar c$ on the infinite line gives a complete test. For the interval $(-R,R)$, the entropy in the vacuum and in the thermal state at temperature $T=1/\beta$ are

$$
S_0=\frac c3\log\frac{2R}\epsilon+s_0,
\qquad
S_\beta=\frac c3\log\left[\frac\beta{\pi\epsilon}\sinh\frac{2\pi R}\beta\right]+s_0,
$$

with the same endpoint cutoff $\epsilon$ and the same nonuniversal constant $s_0$. [Exact CFT result; derived in Lecture 16 from the twist fields.] The thermal energy density relative to the vacuum is $\Delta\mathcal E=\pi cT^2/6$ (Lecture 12). With $x=2\pi RT$,

$$
\Delta S=\frac c3\log\frac{\sinh x}x,
\qquad
\Delta\langle K_B\rangle=2\pi\,\Delta\mathcal E\int_{-R}^Rdx'\,\frac{R^2-x'^2}{2R}=\frac{2\pi^2c}9R^2T^2=\frac c3\,\frac{x^2}6 .
$$

The relative entropy between the thermal and vacuum states of the interval is therefore known exactly:

$$
D(\rho_{\beta,B}\Vert\rho_{0,B})=\frac c3\left[\frac{x^2}6-\log\frac{\sinh x}x\right]
=\frac c3\left[\frac{x^4}{180}-\frac{x^6}{2835}+O(x^8)\right].
$$

[Exact calculation, given the CFT input.] Its leading term is $\frac{4c\pi^4}{135}R^4T^4$.

Three features deserve comment. The first law holds: $\Delta S$ and $\Delta\langle K_B\rangle$ agree at order $T^2$, which is first order in the perturbation of the state, since the energy density is proportional to $T^2$. The relative entropy begins at order $T^4$, second order in the same parameter, as it must. And the relative entropy is nonnegative for every $x$, because $f(x)=\frac{x^2}6-\log\frac{\sinh x}x$ vanishes at $x=0$ and has $f'(x)=\frac x3-\left(\coth x-\frac1x\right)\geq0$, by the inequality $\coth x-1/x\leq x/3$ (Problem 6).

At high temperature the three quantities separate. The entropy change becomes extensive, $\Delta S\simeq\frac c3x=\frac{2\pi c}3RT$, the thermal entropy of a length $2R$. The modular energy grows as $x^2$, because the vacuum modular Hamiltonian weights the thermal energy with a factor of order $R$. Their difference, the relative entropy, is then dominated by the modular energy, $D\simeq\frac c3\left(\frac{x^2}6-x+\log2x\right)$: the thermal state is easily distinguished from the vacuum on a large interval, and $\Delta S\leq\Delta\langle K_B\rangle$ holds with a wide margin. The figure shows the three curves.

**Checkpoint 2.** Why is the first law exact at order $T^2$ while $\Delta S$ and $\Delta\langle K_B\rangle$ differ at order $T^4$?

**Answer.** The thermal state differs from the vacuum at first order by a term proportional to $T^2$. Relative entropy is stationary at the reference state, so the difference $\Delta\langle K_B\rangle-\Delta S=D$ starts at second order in that perturbation, which is $T^4$.

## 9. Self-study: the diamond as hyperbolic space

Casini, Huerta and Myers found a second conformal map that makes the modular flow a time translation. In the diamond, set

$$
t=R\,\frac{\sinh(\tau/R)}{\cosh u+\cosh(\tau/R)},
\qquad
r=R\,\frac{\sinh u}{\cosh u+\cosh(\tau/R)},
$$

with $\tau\in\mathbb R$ and $u\geq0$. A direct computation gives

$$
-dt^2+dr^2+r^2d\Omega_{d-2}^2=\Omega^2\left[-d\tau^2+R^2\left(du^2+\sinh^2u\,d\Omega_{d-2}^2\right)\right],
\qquad
\Omega=\frac1{\cosh u+\cosh(\tau/R)},
$$

so the diamond is conformal to $\mathbb R\times\mathbb H^{d-1}$, time times hyperbolic space of curvature radius $R$ (Problem 9). The entangling sphere is at $u\to\infty$, the conformal boundary of $\mathbb H^{d-1}$. The pushforward of $2\pi R\,\partial_\tau$ is exactly $\zeta$, so the modular flow is the translation $\tau\mapsto\tau+2\pi Rs$. The KMS period $s\to s+i$ is $\tau\to\tau+2\pi iR$, and the vacuum of the diamond is mapped to a thermal state on hyperbolic space at temperature

$$
T=\frac1{2\pi R}.
$$

[Exact for the map and the flow; the identification of the states uses the conformal covariance of the claim of §5.] The entanglement entropy of the ball becomes a thermal entropy on $\mathbb H^{d-1}$, whose volume is infinite; regulating it at distance $\epsilon$ from the sphere reproduces the area-law divergence. In two dimensions $\mathbb H^1$ is a line with coordinate $Ru$, and at $\tau=0$ the map reduces to $r=R\tanh(u/2)$, that is, $Ru=R\log\frac{R+r}{R-r}$, the coordinate used in Lecture 16, §7. In a holographic theory the thermal state on hyperbolic space is dual to a black hole with a hyperbolic horizon, whose entropy is the area of the minimal surface of the ball.

## 10. The bridge to gravity

A ball in the vacuum of a conformal field theory now comes with three exact pieces of data: a causal diamond, a modular vector field, and a local expression for the modular Hamiltonian in terms of the stress tensor. In a holographic theory the conformal symmetry extends into the bulk. The vector field $\zeta$ becomes a Killing vector of a wedge of anti-de Sitter space bounded by the minimal surface of the ball, and the entropy of the ball is the area of that surface divided by $4G_N$.

The gravitational argument of Lecture 22 adds that geometric representation to the first law of §6. Without it, the first law is an identity about states of a conformal field theory. With it, imposed for every ball and every state near the vacuum, it becomes a linear constraint on the bulk metric that is equivalent to the linearized Einstein equations.

## 11. What to take away

- **Exact calculation:** an inversion composed with translations and a dilation maps the Rindler wedge conformally onto the causal diamond of a ball, and pushes the rescaled boost forward to $\zeta=\frac\pi R\left[(R^2-t^2-r^2)\partial_t-2tx^i\partial_i\right]$, whose flow translates $\log\frac{R+x^\pm}{R-x^\pm}$ by $2\pi s$.
- **Stated only, with a sketch:** in the vacuum of a conformal field theory the modular flow of a ball is the flow of $\zeta$, and $K_B=2\pi\int_B\frac{R^2-r^2}{2R}T_{00}+C$; the weight reduces to the Rindler weight near the entangling sphere.
- **Exact calculation:** the diamond is conformal to $\mathbb R\times\mathbb H^{d-1}$, the modular flow is time translation there, and the vacuum becomes thermal at $T=1/2\pi R$.
- **Proved:** the first law $\delta S=\delta\langle K\rangle$ is the stationarity of relative entropy at the reference state, and $\Delta S\leq\Delta\langle K\rangle$ holds at finite separation.
- **Exact calculation, given the claim of §5:** for a homogeneous perturbation of a ball, $\delta S_B=\frac{2\pi R}{d+1}\delta E_B$.
- **Exact calculation, given the CFT input:** for a thermal interval in two dimensions the relative entropy is $\frac c3\left[\frac{x^2}6-\log\frac{\sinh x}x\right]$ with $x=2\pi RT$, which begins at order $T^4$ and is nonnegative for all $T$.

## 12. Looking ahead

Lecture 12 develops the conformal algebra whose generators appear in $\widehat K_B$, and Lecture 16 derives the thermal interval entropy used in §8 and explains, with the map of §9, why the Ryu–Takayanagi prescription holds for balls. Lecture 22 extends $\zeta$ into the bulk and turns the first law into the linearized Einstein equations. Lecture 31 asks what can replace the geometric flow of this lecture for regions and states that have none.

## 13. Problem set

### Classroom core

1. **Following an orbit.** Start at $t=0$, $r=r_0$, and find the future endpoint of the orbit of $\zeta$ and its modular time of arrival at $t=R/2$ when $r_0=0$.

2. **The weight near the sphere.** Expand the weight of $K_B$ near $r=R$ and compare with a Rindler wedge at proper distance $\delta$ from its edge.

3. **The energy integral in two dimensions.** Compute $\int_{-R}^R\frac{R^2-x^2}{2R}\,dx$ and use it to obtain $\Delta\langle K_B\rangle$ of §8.

4. **The slice $X^0=0$.** Show by hand that the map of §3 sends the half-space $X^1>0$ of the slice $X^0=0$ into the ball $|x|<R$ and the plane $X^1=0$ onto the sphere $|x|=R$ minus one point.

5. **Modular speed and local temperature.** Compute $dt/ds$ along the central orbit, and the inverse local temperature $\beta_{\mathrm{loc}}(r)$ at $t=0$.

6. **The first law and the inequality.** Derive $\Delta S\leq\Delta\langle K_\sigma\rangle$ from the positivity of relative entropy, and prove that $\frac{x^2}6\geq\log\frac{\sinh x}x$ for all $x\geq0$.

### Self-study consolidation

7. **The pushforward in two dimensions.** Derive the null-coordinate form of the map of §3, and push the rescaled boost $2\pi(X^+\partial_{X^+}-X^-\partial_{X^-})$ forward to recover $\zeta$.

8. **A conserved current.** Show that $\partial_\mu(T^{\mu\nu}\zeta_\nu)=0$ for a conserved traceless $T$ and a conformal Killing vector $\zeta$, and that $\zeta$ of §3 satisfies the conformal Killing equation.

9. **The map to hyperbolic space.** Verify the conformal factor of §9 and that $2\pi R\,\partial_\tau$ pushes forward to $\zeta$.

10. **Four dimensions.** Evaluate the homogeneous first law for $d=4$, and compare the entanglement temperature with the temperature $1/2\pi R$ of §9.

11. **The exact relative entropy.** Derive the series of $D$ in §8 to order $x^6$, and its behavior at large $x$.

12. **The two-sided generator.** Show that $\zeta=\pi R\,\partial_t+\frac\pi R\,\xi_{e_0}$, with $\xi_b$ the special conformal vector field of Lecture 12, and conclude that the two-sided generator $\widehat K_B$ annihilates the vacuum of a conformal field theory.

### Research extension

13. **Deforming the entangling surface.** Deform the flat edge of a Rindler wedge along a null direction, so that it becomes the surface $x^+=X(\mathbf y)$ in the null plane $x^-=0$. *Known:* the vacuum modular Hamiltonian remains local, $2\pi\int d^{d-2}y\int dx^+\,(x^+-X(\mathbf y))\,T_{++}$ on the null plane, as shown by Faulkner, Leigh, Parrikar and Wang and by Casini, Teste and Torroba; for spatial deformations of a ball, Rosenhaus and Smolkin compute the change of entropy perturbatively. *Completion:* the derivation of the null-plane form in a free theory, and the demonstration that substituting a position-dependent radius into $K_B$ does not reproduce it for a spatial deformation.

14. **Two intervals.** For the free massless Dirac fermion in two dimensions, two disjoint intervals have a modular Hamiltonian with a local part and a bilocal part that couples points of the two intervals. *Known:* Casini and Huerta obtain both kernels in closed form. *Completion:* the local weight, the location of the bilocal couplings, and the limit in which the intervals merge into one, where the weight of §5 is recovered.

15. **The holographic first law.** For a planar black brane in AdS$_3$, compare the length of the geodesic of an interval with the vacuum length at small $RT$, and verify $\delta S=\delta\langle K_B\rangle$ at first order and the sign of the second-order term. *Known:* this is the bulk side of §8, since the BTZ geodesic reproduces the thermal entropy exactly (Lecture 16); Blanco, Casini, Hung and Myers check positivity of relative entropy holographically in higher dimensions. *Completion:* the expansion of the regulated length to order $T^4$, identified with $D$ of §8 through $c=3L/2G_3$.

## 14. Answer checkpoints

1. Both $x^+$ and $x^-$ tend to $R$ as $s\to+\infty$, so the orbit ends at the tip $(R,\mathbf 0)$. For $r_0=0$, $t(s)=R\tanh\pi s$ reaches $R/2$ at $s=\operatorname{artanh}(1/2)/\pi=\log3/2\pi$.

2. With $r=R-\delta$, $\frac{R^2-r^2}{2R}=\delta-\frac{\delta^2}{2R}$, so $K_B$ weights the energy density near the sphere by $2\pi\delta$, the Rindler weight at distance $\delta$ from an edge.

3. $\int_{-R}^R\frac{R^2-x^2}{2R}dx=\frac1{2R}\left(2R^3-\frac{2R^3}3\right)=\frac{2R^2}3$. Multiplying by $2\pi\Delta\mathcal E=\pi^2cT^2/3$ gives $\frac{2\pi^2c}9R^2T^2$.

4. With $Y=X+Re_1$ on $X^0=0$, $x+Re_1=2R^2Y/|Y|^2$ gives $|x+Re_1|=2R^2/|Y|$ and $|x|^2=R^2+4R^3(R-Y^1)/|Y|^2$. With $Y^1=X^1+R$, $|x|<R$ exactly when $X^1>0$, and $|x|=R$ when $X^1=0$. The point $-Re_1$ is reached only as $|X|\to\infty$.

5. $dt/ds=\pi R\operatorname{sech}^2\pi s$, which is $\pi R$ at $t=0$ and tends to zero at the tips. At $t=0$ the orbit through $r$ moves at $d\tau/ds=\frac\pi R(R^2-r^2)$, so $\beta_{\mathrm{loc}}=\pi(R^2-r^2)/R$.

6. $D(\rho\Vert\sigma)=\operatorname{Tr}\rho\log\rho-\operatorname{Tr}\rho\log\sigma=-S(\rho)+S(\sigma)+\operatorname{Tr}(\rho-\sigma)K_\sigma\geq0$. For the inequality, $f(0)=0$ and $f'(x)=\frac x3-\left(\coth x-\frac1x\right)$. The expansion $\coth x=\frac1x+\sum_{n\geq1}\frac{2x}{x^2+n^2\pi^2}$ gives $\coth x-\frac1x\leq\sum_{n\geq1}\frac{2x}{n^2\pi^2}=\frac x3$, using $\sum_n n^{-2}=\pi^2/6$. Therefore $f'\geq0$ and $f\geq0$.

7. With $Y\cdot Y=(R-X^-)(R+X^+)$, the components give $x^+=-R+\frac{2R^2}{R-X^-}$ and $x^-=R-\frac{2R^2}{R+X^+}$. The boost is $X^\pm\mapsto e^{\pm2\pi s}X^\pm$, generated by $2\pi(X^+\partial_{X^+}-X^-\partial_{X^-})$. Then $\frac{dx^-}{ds}=\frac{2R^2}{(R+X^+)^2}\,2\pi X^+$, and eliminating $X^+=R\frac{R+x^-}{R-x^-}$ gives $\frac\pi R(R^2-(x^-)^2)$; the same computation for $x^+$ gives $\frac\pi R(R^2-(x^+)^2)$.

8. $\partial_\mu(T^{\mu\nu}\zeta_\nu)=T^{\mu\nu}\partial_\mu\zeta_\nu=\frac12T^{\mu\nu}(\partial_\mu\zeta_\nu+\partial_\nu\zeta_\mu)=\frac1dT^\mu{}_\mu\,\partial\cdot\zeta=0$. For $\zeta$ of §3, $\partial\cdot\zeta=-\frac{2\pi d}Rt$, and the symmetrized derivative equals $-\frac{4\pi t}R\eta_{\mu\nu}$, which is $\frac2d(\partial\cdot\zeta)\eta_{\mu\nu}$.

9. Differentiating $t$ and $r$ and forming $-dt^2+dr^2$ gives $\Omega^2(-d\tau^2+R^2du^2)$, and $r^2=\Omega^2R^2\sinh^2u$ for the angular part. The pushforward of $2\pi R\partial_\tau$ has components $2\pi R\,\partial_\tau t=\frac\pi R(R^2-t^2-r^2)$ and $2\pi R\,\partial_\tau r=-\frac{2\pi}Rtr$.

10. With $d=4$, $\delta S_B=\frac{2\pi R}5\delta E_B$ and $T_{\mathrm{ent}}=\frac5{2\pi R}$, which is five times the temperature $1/2\pi R$ on hyperbolic space. The two describe different things: $T_{\mathrm{ent}}$ relates changes of entropy and energy in the ball for a homogeneous excitation, while $1/2\pi R$ is the temperature of the vacuum after the conformal map.

11. $\log\frac{\sinh x}x=\frac{x^2}6-\frac{x^4}{180}+\frac{x^6}{2835}+O(x^8)$ gives the series. At large $x$, $\log\frac{\sinh x}x=x-\log2x+O(e^{-2x})$, so $D=\frac c3\left(\frac{x^2}6-x+\log2x\right)+\dots$

12. With $b=e_0$ and the mostly-plus product, $b\cdot x=-t$ and $\xi_{e_0}=-2t\,x^\mu\partial_\mu-x^2\partial_t=-(t^2+r^2)\partial_t-2t\,x^i\partial_i$. Adding $\pi R\,\partial_t$ to $\frac\pi R\xi_{e_0}$ gives $\zeta$. The charge of $\partial_t$ is $H$, and the charge of $\xi_{e_0}$ is a special conformal generator; the vacuum is invariant under the whole conformal group, so both charges annihilate it, and so does $\widehat K_B$.

**Wiki connections.** [[causal-diamonds|causal diamonds]] · [[bisognano-wichmann-theorem|Bisognano–Wichmann theorem]]
