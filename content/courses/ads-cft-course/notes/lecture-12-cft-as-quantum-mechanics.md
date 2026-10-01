---
title: "Lecture 12 — Conformal field theory as organized quantum mechanics"
type: lecture-notes
edition: "2.2 — rewritten at the AQFT standard"
lecture: 12
semester: 1
week: 10
hours: 4
prerequisites: "Lectures 10–11; quantum mechanics of symmetry generators; complex analysis"
status: "rewritten 2026-09-29, pending instructor review; exact symmetry consequences, with Cardy's formula as a controlled asymptotic statement"
modified: 2026-09-29
---

# Lecture 12 — Conformal field theory as organized quantum mechanics

> *Conformal field theory is the boundary side of every holographic statement in the course, and this lecture develops the parts of it that later lectures use. We derive the conformal algebra from the conformal Killing equation, show how it fixes two- and three-point functions and constrains four-point functions, and then quantize radially, so that operator dimensions become energies on a cylinder and positivity of norms becomes the unitarity bound. The stress tensor supplies the conserved charges. In two dimensions it also supplies the central charge, which enters the Casimir energy of the cylinder and, through modular invariance, Cardy's formula for the density of states. Lecture 13 matches the cylinder spectrum with AdS normal modes, Lecture 15 matched the two-point function, and Lectures 16 and 23 use the central charge.*

## How to use this lecture

**Classroom core, two meetings of two hours.** The first meeting covers the motivation and the conformal algebra (§§1–2, 35 minutes), the constraints on correlators (§3, 40 minutes), and radial quantization (§4, 30 minutes), leaving 15 minutes for Checkpoints 1 and 2. The second meeting derives the unitarity bound (§5, 25 minutes), the Virasoro algebra, the Schwarzian and the Casimir energy (§8.1–8.3, 45 minutes), and Cardy's formula (§8.4, 25 minutes), with 25 minutes for Problems 1–4; Problems 5 and 6 complete the core assignment. These allocations are proposals and have not been tested in class.

**Self-study.** The operator product expansion and its convergence (§6), the stress tensor and the conformal Ward identity in general dimension (§7), and Problems 7–12, which supply the derivations stated in class.

**Research extension.** Large-$N$ corrections to a generalized free field, the sparseness condition behind the holographic range of Cardy's formula, and the Brown–Henneaux central charge, in Problems 13–15.

**Prerequisites.** Lectures 10 and 11 for modular flow as a symmetry; generators, Casimirs and raising operators from quantum mechanics; Laurent series and residues. We work in Euclidean signature except where Lorentzian time is named.

**What this lecture establishes.** Sections 2–8.3 are consequences of conformal symmetry, unitarity and the stated assumptions: a unitary, reflection-positive CFT with a unique vacuum and a state–operator correspondence. Cardy's formula in §8.4 is an exact asymptotic statement as $\beta/\ell\to0$; its extension to finite temperature at large central charge requires the additional sparseness condition stated there.

## 0. Reading

**Primary.**

- S. Rychkov, [EPFL Lectures on Conformal Field Theory in D >= 3 Dimensions](https://arxiv.org/abs/1601.05000) (2016): radial quantization, unitarity and the OPE.
- D. Simmons-Duffin, [TASI Lectures on the Conformal Bootstrap](https://arxiv.org/abs/1602.07982) (2016): the algebra, correlators, blocks and crossing.
- P. Ginsparg, [Applied Conformal Field Theory](https://arxiv.org/abs/hep-th/9108028) (1988): the two-dimensional material of §8.

**Secondary.**

- P. Di Francesco, P. Mathieu, D. Sénéchal, *Conformal Field Theory* (Springer, 1997), Chapters 4–6 and 10.
- H. Osborn, A. Petkou, [Implications of Conformal Invariance in Field Theories for General Dimensions](https://arxiv.org/abs/hep-th/9307010) (1993): the stress-tensor two-point function of §7.
- D. Pappadopulo, S. Rychkov, J. Espin, R. Rattazzi, [OPE Convergence in Conformal Field Theory](https://arxiv.org/abs/1208.6449) (2012): §6.

**Optional research reading.**

- A. A. Belavin, A. M. Polyakov, A. B. Zamolodchikov, *Infinite conformal symmetry in two-dimensional quantum field theory*, Nucl. Phys. B 241 (1984) 333, and J. L. Cardy, *Operator content of two-dimensional conformally invariant theories*, Nucl. Phys. B 270 (1986) 186.
- R. Rattazzi, V. S. Rychkov, E. Tonni, A. Vichi, [Bounding scalar operator dimensions in 4D CFT](https://arxiv.org/abs/0807.0004) (2008), and D. Poland, S. Rychkov, A. Vichi, [The Conformal Bootstrap: Theory, Numerical Techniques, and Applications](https://arxiv.org/abs/1805.04405) (2018).
- T. Hartman, C. A. Keller, B. Stoica, [Universal Spectrum of 2d Conformal Field Theory in the Large c Limit](https://arxiv.org/abs/1405.5137) (2014): Problem 14.

## 1. Why conformal symmetry

In 1970 Polyakov argued that the fluctuations of a system at a critical point are invariant under local changes of scale, that is, under conformal transformations, and he showed that this invariance fixes the three-point function of the fluctuating fields up to a constant. Ferrara, Gatto and Grillo then worked out the operator product expansion compatible with the symmetry, and in 1974 Polyakov proposed that the consistency of these expansions might by itself determine the critical exponents. That idea, the conformal bootstrap, succeeded first in two dimensions. Belavin, Polyakov and Zamolodchikov showed in 1984 how the infinite-dimensional Virasoro algebra, already familiar from string theory, organizes the operator content of two-dimensional critical theories, and they solved an infinite family of them, the minimal models, exactly. Two years later Cardy showed that invariance under the modular group fixes the high-temperature density of states in terms of a single number, the central charge. In higher dimensions the bootstrap became quantitative in 2008, when Rattazzi, Rychkov, Tonni and Vichi turned crossing symmetry into numerical bounds on operator dimensions.

For this course, conformal field theory is the boundary side of every holographic statement, and three of its results return repeatedly. The state–operator correspondence identifies the spectrum of the theory on a cylinder with the dimensions of local operators; Lecture 13 compares that spectrum with the normal modes of a field in AdS. The constraints of symmetry on correlators fix the form that the bulk must reproduce, as Lecture 15 did for the two-point function. And the stress tensor, with its central charge in two dimensions, controls the entropies of Lectures 16 and 23. The useful analogy throughout is the theory of angular momentum: symmetry labels states, raising operators generate multiplets, and positivity of norms restricts the allowed labels.

## 2. Conformal transformations and their algebra

A conformal transformation of flat Euclidean space $\mathbb R^d$ is a map $x\mapsto x'$ that preserves the metric up to a local factor, $dx'^2=\Omega(x)^2\,dx^2$. For an infinitesimal map $x^\mu\mapsto x^\mu+\xi^\mu(x)$ the condition is the conformal Killing equation

$$
\partial_\mu\xi_\nu+\partial_\nu\xi_\mu=\frac2d\,(\partial\cdot\xi)\,\delta_{\mu\nu}.
$$

For $d>2$ its solutions are at most quadratic in $x$ (Problem 1). The general solution is

$$
\xi^\mu=a^\mu+\omega^\mu{}_\nu x^\nu+\lambda x^\mu+2(b\cdot x)\,x^\mu-x^2\,b^\mu,\qquad\omega_{\mu\nu}=-\omega_{\nu\mu},
$$

where the four families are translations, rotations, the dilatation, and the special conformal transformations. For the last family $\partial\cdot\xi=2d\,(b\cdot x)$, so these maps rescale lengths by an amount that varies from point to point. Counting parameters,

$$
d+\frac{d(d-1)}{2}+1+d=\frac{(d+1)(d+2)}{2},
$$

which is the dimension of $\mathfrak{so}(d+1,1)$, or of $\mathfrak{so}(d,2)$ in Lorentzian signature. Note that this is also the isometry algebra of AdS$_{d+1}$; Lecture 13 makes the identification explicit.

The special conformal transformations are conjugates of translations by the inversion $x^\mu\mapsto x^\mu/x^2$. The inversion is conformal with $\Omega(x)=1/x^2$, although it is not connected to the identity, and it acts on distances as

$$
|x_1'-x_2'|=\frac{|x_1-x_2|}{|x_1|\,|x_2|}.
$$

Inverting, translating by $-b$ and inverting again gives the finite special conformal transformation $x'^\mu=(x^\mu-b^\mu x^2)/(1-2b\cdot x+b^2x^2)$, whose first-order term is the vector field above (Problem 7). In two dimensions the conformal Killing equation reduces to the Cauchy–Riemann equations, every holomorphic map is locally conformal, and the algebra becomes infinite-dimensional. The globally defined part is the Möbius group $z\mapsto(pz+q)/(rz+s)$ with $ps-qr=1$, which is the $d=2$ case of the finite-dimensional algebra above. Section 8 develops the rest.

## 3. Primary operators and what symmetry fixes

A scalar primary operator of dimension $\Delta$ is a local operator whose correlators transform under every conformal map with the local factor of each insertion,

$$
\left\langle\mathcal O_1(x_1')\cdots\mathcal O_n(x_n')\right\rangle=\prod_{i=1}^n\Omega(x_i)^{-\Delta_i}\,\left\langle\mathcal O_1(x_1)\cdots\mathcal O_n(x_n)\right\rangle.
$$

For a dilatation $x'=\lambda x$ the factor is $\lambda^{-\Delta_i}$, which is the familiar scaling of an operator of dimension $\Delta_i$. The derivatives of a primary are its descendants; they transform with additional terms and are determined by the primary.

Consider the two-point function of two scalar primaries. Translations and rotations make it a function of $|x_{12}|=|x_1-x_2|$ alone, and dilatations fix the power, so that $\langle\mathcal O_1(x_1)\mathcal O_2(x_2)\rangle=C_{12}|x_{12}|^{-\Delta_1-\Delta_2}$. Now apply the inversion. Its factor is $\Omega(x_i)^{-\Delta_i}=|x_i|^{2\Delta_i}$, and the distance transforms as above, so the transformation law requires

$$
\frac{C_{12}\,|x_1|^{\Delta_1+\Delta_2}|x_2|^{\Delta_1+\Delta_2}}{|x_{12}|^{\Delta_1+\Delta_2}}=|x_1|^{2\Delta_1}|x_2|^{2\Delta_2}\,\frac{C_{12}}{|x_{12}|^{\Delta_1+\Delta_2}}
$$

for all $x_1,x_2$. This holds only if $\Delta_1=\Delta_2$ or $C_{12}=0$ (Problem 2). Thus

$$
\langle\mathcal O(x_1)\mathcal O(x_2)\rangle=\frac{C_{\mathcal O}}{|x_{12}|^{2\Delta}},
$$

and operators of equal dimension can be chosen orthogonal. For a Hermitian scalar in a reflection-positive theory $C_{\mathcal O}>0$; this is the coefficient Lecture 15 computed from the bulk.

The same argument applied to three points leaves one constant undetermined,

$$
\langle\mathcal O_1(x_1)\mathcal O_2(x_2)\mathcal O_3(x_3)\rangle=\frac{C_{123}}{|x_{12}|^{\Delta_1+\Delta_2-\Delta_3}\,|x_{23}|^{\Delta_2+\Delta_3-\Delta_1}\,|x_{13}|^{\Delta_1+\Delta_3-\Delta_2}}.
$$

Under inversion each factor $|x_{ij}|^{-a_{ij}}$ produces $(|x_i||x_j|)^{a_{ij}}$, and matching the factor $|x_i|^{2\Delta_i}$ at each point requires $\sum_{j\neq i}a_{ij}=2\Delta_i$, whose unique solution is the set of exponents displayed (Problem 3). The constant $C_{123}$ is dynamical information, the first quantity that symmetry does not fix.

With four points, symmetry no longer fixes the dependence on positions. From four points one can form two independent cross-ratios,

$$
u=\frac{x_{12}^2x_{34}^2}{x_{13}^2x_{24}^2},\qquad v=\frac{x_{14}^2x_{23}^2}{x_{13}^2x_{24}^2},
$$

which are invariant under every conformal transformation, and for four identical scalars

$$
\langle\phi(x_1)\phi(x_2)\phi(x_3)\phi(x_4)\rangle=\frac{g(u,v)}{x_{12}^{2\Delta}x_{34}^{2\Delta}}
$$

with an arbitrary function $g$. Exchanging $x_1$ and $x_3$ maps $u\leftrightarrow v$ and gives the crossing equation

$$
v^\Delta\,g(u,v)=u^\Delta\,g(v,u),
$$

which is the constraint the bootstrap exploits. The simplest solution is the generalized free field, whose four-point function is the sum of the three pairings of two-point functions. In cross-ratios it reads

$$
g_{\mathrm{GFF}}(u,v)=1+u^\Delta+\left(\frac uv\right)^\Delta,
$$

and it satisfies crossing (Problem 8). Lecture 15 found that a free field in AdS produces exactly this structure on the boundary.

**Checkpoint 1.** Why can two scalar primaries of different dimensions have a nonzero three-point function with a third operator, while their two-point function vanishes?

**Answer.** Inversion constrains the exponents at each point. With two points both exponents equal the single power $\Delta_1+\Delta_2$, which forces $\Delta_1=\Delta_2$. With three points the three exponents can be chosen to satisfy $\sum_{j\neq i}a_{ij}=2\Delta_i$ at every point for any dimensions.

## 4. Radial quantization and the state–operator correspondence

To use this structure as quantum mechanics we need a Hilbert space and a Hamiltonian. In Euclidean space write

$$
ds^2=dr^2+r^2d\Omega_{d-1}^2=e^{2\tau}\left(d\tau^2+d\Omega_{d-1}^2\right),\qquad r=e^\tau.
$$

After removing the Weyl factor, this is a cylinder $\mathbb R\times S^{d-1}$ with a sphere of unit radius, and dilatations $r\mapsto e^ar$ become translations $\tau\mapsto\tau+a$. Their generator $D$ therefore acts as the Hamiltonian of the cylinder, up to the vacuum-energy convention; with a sphere of radius $R$ the energy gaps are $\Delta/R$. States live on spheres surrounding the origin. A local insertion at the origin prepares a state on every enclosing sphere,

$$
|\mathcal O\rangle=\lim_{r\to0}\mathcal O(r\hat n)|0\rangle,
$$

and conversely every state of the cylinder can be shrunk to a local operator at the origin. This is the state–operator correspondence. For a scalar primary, $D|\mathcal O\rangle=\Delta|\mathcal O\rangle$ and $K_\mu|\mathcal O\rangle=0$, while the translations $P_\mu$ generate descendants of dimension $\Delta+1,\Delta+2,\ldots$. The vacuum is the state prepared by an empty ball, and a dimension becomes an energy.

In radial quantization the adjoint combines Hermitian conjugation with inversion through the unit sphere, because the time reversal $\tau\mapsto-\tau$ of the cylinder is $r\mapsto1/r$ on the plane. The generators then satisfy

$$
D^\dagger=D,\qquad P_\mu^\dagger=K_\mu,\qquad[D,P_\mu]=P_\mu,\qquad[D,K_\mu]=-K_\mu,
$$

and, with suitable conventions for the rotation generators $M_{\mu\nu}$,

$$
[K_\mu,P_\nu]=2\delta_{\mu\nu}D-2M_{\mu\nu},\qquad[M_{\mu\nu},P_\rho]=\delta_{\nu\rho}P_\mu-\delta_{\mu\rho}P_\nu.
$$

There are no factors of $i$ in this Euclidean radial basis; they should not be mixed with a Lorentzian convention in which every generator is a Hermitian charge. The structure is that of angular momentum with $D$ in place of $J_z$: $P_\mu$ raises and $K_\mu$ lowers the eigenvalue of $D$ by one, and a primary is a lowest-weight state.

**Checkpoint 2.** On a cylinder of radius $R$, what is the energy of the descendant $P_\mu P^\mu|\mathcal O\rangle$ above the vacuum?

**Answer.** $(\Delta+2)/R$, since each $P_\mu$ raises the eigenvalue of $D$ by one.

## 5. Positivity and the unitarity bound

For a normalized scalar primary, $M_{\mu\nu}|\mathcal O\rangle=0$ and $K_\nu|\mathcal O\rangle=0$, so the first-level norms are

$$
\langle\mathcal O|K_\mu P_\nu|\mathcal O\rangle=\langle\mathcal O|[K_\mu,P_\nu]|\mathcal O\rangle=2\Delta\,\delta_{\mu\nu}.
$$

A nonidentity scalar therefore has $\Delta>0$, and $\Delta=0$ makes the first descendants null, which in the ordinary unitary vacuum sector leaves only the identity. The second level gives a stronger condition. Commuting one $K_\mu$ through $P^2=P_\nu P_\nu$, using the rotation commutator on the first-level descendant, one finds

$$
K_\mu P^2|\mathcal O\rangle=4\left(\Delta+1-\frac d2\right)P_\mu|\mathcal O\rangle,
$$

and applying the second $K_\mu$,

$$
\left\|P^2|\mathcal O\rangle\right\|^2=8d\,\Delta\left(\Delta-\frac{d-2}{2}\right).
$$

Positivity then requires

$$
\Delta\geq\frac{d-2}{2}
$$

for a nonidentity scalar. At saturation $P^2|\mathcal O\rangle$ is null, which in the state–operator correspondence is the equation $\partial^2\mathcal O=0$: the free massless scalar. A zero norm in a unitary theory means that the null state is removed from the physical Hilbert space. **[Proved, for scalar primaries.]** For operators of spin $\ell\geq1$ the analogous analysis gives $\Delta\geq\ell+d-2$, saturated by conserved currents. Mack derived these bounds in four dimensions by classifying the positive-energy representations of the conformal group, and the same bounds hold in general dimension; we state that result. The scalar bound will reappear in Lecture 13 as the normalizability of the slower bulk falloff, and in Lecture 15 as the point where the alternate quantization stops being unitary.

## 6. Self-study: the operator product expansion

Enclose two nearby insertions in a sphere that excludes every other insertion. They prepare a state on that sphere. Expanding the state in eigenstates of $D$, primaries and descendants, and using the state–operator correspondence to return to local operators, gives

$$
\mathcal O_i(x)\,\mathcal O_j(0)=\sum_kC_{ij}{}^{k}(x,\partial)\,\mathcal O_k(0),
$$

where the sum runs over primaries $\mathcal O_k$ and the differential operator $C_{ij}{}^k(x,\partial)$ is fixed by symmetry once the coefficient $C_{ijk}$ of the three-point function is known. The argument also shows why the expansion converges: it is the expansion of a normalizable state in an orthonormal basis, valid inside correlators whenever the other insertions lie outside the sphere, as Pappadopulo, Rychkov, Espin and Rattazzi made precise.

Applied to the four-point function, the expansion organizes $g(u,v)$ as a sum over the primaries exchanged between the pairs $(12)$ and $(34)$,

$$
g(u,v)=\sum_{\mathcal O}C_{\phi\phi\mathcal O}^2\;G_{\Delta_{\mathcal O},\ell_{\mathcal O}}(u,v),
$$

where the conformal block $G_{\Delta,\ell}$ collects the contribution of one primary and all its descendants and is fixed by symmetry. Crossing then becomes a set of equations for the dynamical data $\{\Delta_{\mathcal O},\ell_{\mathcal O},C_{\phi\phi\mathcal O}\}$. For the generalized free field the identity gives the term 1 in $g_{\mathrm{GFF}}$, and the remaining terms decompose into the double-trace families $[\phi\phi]_{n,\ell}$ of dimensions $2\Delta+2n+\ell$, with even $\ell$ for identical bosons. A Gaussian four-point function is therefore quite different from an expansion containing only the identity: it contains infinitely many composite primaries, which in AdS are two-particle states (Lecture 13).

## 7. Self-study: the stress tensor and the conformal Ward identity

A local conformal field theory has a stress tensor $T_{\mu\nu}$ that is symmetric, conserved and traceless, $\partial^\mu T_{\mu\nu}=0$ and $T^\mu{}_\mu=0$ at separated points. For every conformal Killing vector $\xi$ the current $J_\xi^\mu=T^{\mu\nu}\xi_\nu$ is then conserved, because

$$
\partial_\mu\left(T^{\mu\nu}\xi_\nu\right)=T^{\mu\nu}\,\partial_\mu\xi_\nu=\frac12T^{\mu\nu}\left(\partial_\mu\xi_\nu+\partial_\nu\xi_\mu\right)=\frac1d\,(\partial\cdot\xi)\,T^\mu{}_\mu=0
$$

(Problem 12). The corresponding charges, integrated over a sphere, are the generators of §4, normalized so that they act on primaries as the symmetry transformations; this Ward identity fixes the normalization of $T_{\mu\nu}$. Conformal symmetry then fixes the stress-tensor two-point function up to one constant,

$$
\langle T_{\mu\nu}(x)\,T_{\rho\sigma}(0)\rangle=\frac{C_T}{x^{2d}}\left[\frac12\left(I_{\mu\rho}I_{\nu\sigma}+I_{\mu\sigma}I_{\nu\rho}\right)-\frac1d\,\delta_{\mu\nu}\delta_{\rho\sigma}\right],\qquad I_{\mu\nu}=\delta_{\mu\nu}-\frac{2x_\mu x_\nu}{x^2},
$$

as Osborn and Petkou showed in general dimension. **[Stated only — refs: Osborn, Petkou.]** The constant $C_T$ counts degrees of freedom: it is additive for decoupled theories and positive in a unitary theory, and its numerical value depends on the normalization of $T_{\mu\nu}$, which we declare to be the Ward-identity normalization just described. In a gauge theory with $N^2$ adjoint fields it is of order $N^2$, which is the large parameter of Lecture 14.

## 8. Two dimensions: the Virasoro algebra, the Schwarzian, and Cardy's formula

### 8.1 The holomorphic stress tensor

In complex coordinates $z=x^1+ix^2$, conservation and tracelessness leave two components of the stress tensor, a holomorphic $T(z)$ and an antiholomorphic $\bar T(\bar z)$. We normalize $T$ by its operator product with a primary $\phi$ of weights $(h,\bar h)$, whose dimension is $\Delta=h+\bar h$ and whose spin is $h-\bar h$:

$$
T(z)\,\phi(w,\bar w)\sim\frac{h\,\phi(w,\bar w)}{(z-w)^2}+\frac{\partial_w\phi(w,\bar w)}{z-w}.
$$

The stress tensor itself is not a primary. Its operator product with itself contains one number beyond what symmetry fixes, the central charge $c$:

$$
T(z)\,T(w)\sim\frac{c/2}{(z-w)^4}+\frac{2\,T(w)}{(z-w)^2}+\frac{\partial_wT(w)}{z-w}.
$$

The first term is the two-point function $\langle T(z)T(w)\rangle=\frac{c}{2}(z-w)^{-4}$, so in two dimensions $c$ plays the role of $C_T$. A free boson has $c=1$ and a free Majorana fermion $c=1/2$; the antiholomorphic sector has its own $\bar c$, and in the theories of this course $\bar c=c$.

### 8.2 The Virasoro algebra

Expand $T(z)=\sum_nL_nz^{-n-2}$, so that $L_n=\oint\frac{dz}{2\pi i}\,z^{n+1}T(z)$. The commutator of two modes follows from the operator product by deforming contours: $[L_m,L_n]$ is the $w$-integral of the residue at $z=w$ of $z^{m+1}w^{n+1}T(z)T(w)$. The three singular terms give

$$
[L_m,L_n]=(m-n)\,L_{m+n}+\frac{c}{12}\,m\left(m^2-1\right)\delta_{m+n,0}.
$$

The central term comes from the fourth-order pole alone. Its residue is $\frac c2\cdot\frac1{3!}\,\partial_z^3z^{m+1}|_{z=w}=\frac{c}{12}(m+1)m(m-1)\,w^{m-2}$, and the $w$-integral of $w^{n+1}w^{m-2}$ is $\delta_{m+n,0}$ (Problem 5). This is the Virasoro algebra. Note that the central term vanishes for $m=0,\pm1$. The modes $L_{-1},L_0,L_1$ generate the Möbius group; in the notation of §4 they are the holomorphic parts of $P$, $D$ and $K$, with $D=L_0+\bar L_0$. The global conformal group of §2 therefore sits inside the infinite algebra without any anomaly.

### 8.3 The Schwarzian and the Casimir energy of the cylinder

Under a finite holomorphic map the operator product fixes how $T$ transforms. Infinitesimally, for $z\mapsto z+\epsilon(z)$, it gives $\delta_\epsilon T=\epsilon\,\partial T+2(\partial\epsilon)\,T+\frac{c}{12}\,\partial^3\epsilon$, and the finite version is

$$
T_w(w)=\left(\frac{dz}{dw}\right)^2T_z(z)+\frac{c}{12}\,\{z,w\},\qquad\{z,w\}=\frac{z'''}{z'}-\frac32\left(\frac{z''}{z'}\right)^2,
$$

where primes denote derivatives with respect to $w$. The Schwarzian derivative $\{z,w\}$ vanishes exactly for Möbius maps and obeys the composition law $\{z,t\}=(dw/dt)^2\{z,w\}+\{w,t\}$ that makes the transformation law consistent (Problem 9). **[Sketched: the finite law integrates the infinitesimal one.]**

The most important application is to the cylinder. Map the plane to a cylinder of circumference $\ell$ by $z=e^{2\pi w/\ell}$, with $w=\tau+i\sigma$ and $\sigma\sim\sigma+\ell$. Then $dz/dw=(2\pi/\ell)z$ and $\{z,w\}=-\frac12(2\pi/\ell)^2$, so

$$
T_{\mathrm{cyl}}(w)=\left(\frac{2\pi}{\ell}\right)^2\left[z^2T(z)-\frac{c}{24}\right].
$$

The generator of translations along the cylinder is the zero mode of this expression. With the same shift in the antiholomorphic sector,

$$
H_{\mathrm{cyl}}=\frac{2\pi}{\ell}\left(L_0+\bar L_0-\frac{c+\bar c}{24}\right),\qquad E_0=-\frac{\pi\,(c+\bar c)}{12\,\ell}.
$$

The vacuum of the plane, with $L_0=\bar L_0=0$, has a negative energy on the circle, the conformal analogue of the Casimir energy between plates. This is the physical meaning of the central charge: it measures how the vacuum responds to the scale introduced by compactifying space. The excited states have energies $E_0+2\pi(h+\bar h)/\ell$, which is §4 with the Casimir shift included.

### 8.4 Cardy's formula

Place the theory on a circle of circumference $\ell$ at inverse temperature $\beta$. Its partition function $Z(\beta)=\operatorname{Tr}e^{-\beta H_{\mathrm{cyl}}}$ is a path integral on a torus with sides $\ell$ and $\beta$. The torus does not know which side we call space. Exchanging the two roles is a modular transformation, and a consistent CFT has the same partition function in both descriptions:

$$
Z(\beta)=\operatorname{Tr}_{\ell}\,e^{-\beta H_\ell}=\operatorname{Tr}_{\beta}\,e^{-\ell H_\beta},
$$

where $H_\beta$ is the Hamiltonian on a circle of circumference $\beta$. At high temperature, $\beta\ll\ell$, the second description is dominated by its ground state, of energy $-\pi(c+\bar c)/(12\beta)$, and therefore

$$
\log Z(\beta)\simeq\frac{\pi\,(c+\bar c)\,\ell}{12\,\beta},\qquad S\simeq\frac{\pi\,(c+\bar c)\,\ell}{6\,\beta},\qquad\frac{E}{\ell}\simeq\frac{\pi\,(c+\bar c)}{12\,\beta^2}.
$$

For $c=\bar c$ these are $S=\frac{\pi c}{3}\,\ell T$ and an energy density $\frac{\pi c}{6}T^2$, the values used in Lectures 11 and 23. Expressed through the energy, the same result is Cardy's formula for the density of states, $S\simeq2\pi\sqrt{\frac c6\left(L_0-\frac c{24}\right)}+2\pi\sqrt{\frac{\bar c}6\left(\bar L_0-\frac{\bar c}{24}\right)}$ (Problem 10). The passage from the canonical to this microcanonical statement holds after averaging the density of states over energy windows, as Mukhametzhanov and Zhiboedov made precise. **[Controlled asymptotic, as $\beta/\ell\to0$ at fixed $c$, in a modular-invariant theory with a unique vacuum.]** The counting uses nothing beyond the Virasoro algebra and modular invariance: a thermodynamic quantity is fixed by the central charge alone.

Nevertheless the formula says nothing about temperatures of order $1/\ell$ in a general theory, because the corrections in the dual channel are controlled by the lightest nontrivial dimension. Hartman, Keller and Stoica showed that at large $c$, when the number of light states grows no faster than $e^{2\pi\Delta}$, the same free energy holds for all $\beta<\ell$, with a transition at $\beta=\ell$ to the low-temperature phase. Lecture 23 identifies that transition with the Hawking–Page transition between thermal AdS$_3$ and the BTZ black hole.

## 9. What the bulk will have to reproduce

The lectures that follow ask a gravitational description to reproduce the structures derived here. The spectrum of $D$ on the cylinder, one primary and its tower of descendants, must match the normal modes of a bulk field (Lecture 13). The two-point function $C_{\mathcal O}/|x|^{2\Delta}$ must come out with a positive coefficient (Lecture 15). Large-$N$ factorization must produce generalized free fields, whose double-trace families are the two-particle states of the bulk (Lectures 14 and 15). In two dimensions the central charge must be expressible through the AdS radius and Newton's constant, which is the Brown–Henneaux relation $c=3L/2G_3$ (Lecture 16), and Cardy's entropy must equal the Bekenstein–Hawking entropy of the BTZ black hole (Lecture 23). Each of these is a nontrivial check of the correspondence; none of them requires knowing the bulk in advance.

## 10. What to take away

- **Exact:** for $d>2$ the conformal algebra is $\mathfrak{so}(d+1,1)$, of dimension $(d+1)(d+2)/2$, the same as the isometry algebra of AdS$_{d+1}$.
- **Exact:** symmetry fixes two-point functions, $C_{\mathcal O}|x|^{-2\Delta}$ with equal dimensions, and three-point functions up to $C_{123}$; four-point functions depend on two cross-ratios and obey crossing.
- **Exact:** radial quantization turns dimensions into energies on the cylinder, and positivity of norms gives $\Delta\geq(d-2)/2$ for scalars.
- **Exact:** in two dimensions the modes of $T$ form the Virasoro algebra with central charge $c$, and the Schwarzian gives the Casimir energy $E_0=-\pi(c+\bar c)/(12\ell)$.
- **Controlled asymptotic:** modular invariance fixes the high-temperature entropy, $S\simeq\frac{\pi c}{3}\ell T$ for $c=\bar c$; its extension to all $\beta<\ell$ at large $c$ requires a sparse light spectrum.

## 11. Looking ahead

Lecture 13 constructs AdS$_{d+1}$, shows that its isometries act on the conformal boundary as the conformal group of §2, and quantizes a free field in global coordinates. Its single-particle states will turn out to form exactly one conformal family of §4, with energies $\Delta+2n+\ell$. Lecture 14 then explains why a theory with many degrees of freedom can have a small set of such fields at leading order.

## 12. Problem set

### Classroom core

1. **Conformal Killing vectors.** Show that for $d>2$ the solutions of the conformal Killing equation are at most quadratic, and that they are the four families of §2. *Hint:* with $f=\partial\cdot\xi$, derive $2\partial_\mu\partial_\nu\xi_\rho=\frac2d\left(\delta_{\rho\mu}\partial_\nu f+\delta_{\rho\nu}\partial_\mu f-\delta_{\mu\nu}\partial_\rho f\right)$, then $(d-2)\,\partial_\mu\partial_\nu f=-\delta_{\mu\nu}\Box f$ and $(d-1)\Box f=0$.

2. **The two-point selection rule.** Complete the inversion argument of §3 and show that $\Delta_1\neq\Delta_2$ forces $C_{12}=0$.

3. **Three-point exponents.** Show that inversion requires $\sum_{j\neq i}a_{ij}=2\Delta_i$ for the exponents of $\prod_{i<j}|x_{ij}|^{-a_{ij}}$, and solve for the $a_{ij}$.

4. **Descendant norms.** Evaluate the norm of $v^\mu P_\mu|\mathcal O\rangle$, and verify the coefficient $4(\Delta+1-d/2)$ of §5 by computing both terms of $[K_\mu,P_\nu P_\nu]$.

5. **The central term.** Compute the residue at $z=w$ of $\frac c2\,z^{m+1}(z-w)^{-4}$ and derive the central term of the Virasoro algebra.

6. **The Casimir energy.** Compute $\{z,w\}$ for $z=e^{2\pi w/\ell}$ and derive $E_0$. What is $E_0$ for a free boson on a circle of circumference $2\pi$?

### Self-study consolidation

7. **Finite special conformal transformations.** Compose inversion, translation by $-b$ and inversion, and check that the first-order term is $2(b\cdot x)x^\mu-x^2b^\mu$.

8. **Crossing of the generalized free field.** Derive $g_{\mathrm{GFF}}$ from the three pairings, verify the crossing equation, and identify the term that the identity operator contributes in the $(12)$ channel.

9. **The Schwarzian.** Show that $\{z,w\}=0$ for a Möbius map and verify the composition law. Explain why the composition law is required for the transformation law of $T$ to be consistent.

10. **Cardy's formula.** Legendre transform the canonical result for $c=\bar c$ and show that $S(E)=\sqrt{2\pi c\,\ell E/3}$ at high energy, which agrees with the microcanonical form in terms of $L_0$ and $\bar L_0$.

11. **Units on the cylinder.** A scalar primary of dimension $\Delta$ lives on a cylinder of radius $R$ in $d$ dimensions. What is its energy above the vacuum, and how does the Casimir energy enter when $d=2$?

12. **Conserved conformal currents.** Show that $\partial_\mu(T^{\mu\nu}\xi_\nu)=0$ for every conformal Killing vector, and identify which properties of $T_{\mu\nu}$ are used at each step.

### Research extension

13. **Beyond the generalized free field.** Add a connected four-point function of order $1/N^2$ to $g_{\mathrm{GFF}}$ and determine the first corrections to the double-trace dimensions and coefficients. *Known:* anomalous dimensions appear as logarithms of $u$, and crossing relates them to the exchanged single-trace operators. *Completion:* an explicit example, such as a contact interaction, with its crossing check.

14. **Sparseness.** Following Hartman, Keller and Stoica, show that if the density of states below $\Delta=c/12$ grows no faster than $e^{2\pi\Delta}$, then $\log Z(\beta)$ is universal at large $c$ for all $\beta\neq\ell$. *Known:* their paper. *Completion:* the bound on the light-state contribution in both channels and the location of the transition.

15. **Brown–Henneaux.** Show that the asymptotic symmetries of AdS$_3$ with Brown–Henneaux boundary conditions form two Virasoro algebras with $c=3L/2G_3$. *Known:* Brown and Henneaux, Commun. Math. Phys. 104 (1986) 207. *Completion:* the algebra of the asymptotic charges and the central term; Lecture 16 uses the result.

## 13. Answer checkpoints

1. Differentiating the conformal Killing equation and combining three permutations of indices gives the first identity. Contracting $\mu\nu$ gives $2\Box\xi_\rho=\frac2d(2-d)\partial_\rho f$, and differentiating again and symmetrizing gives $(d-2)\partial_\mu\partial_\nu f=-\delta_{\mu\nu}\Box f$; its trace is $(d-1)\Box f=0$. For $d>2$ this forces $\partial_\mu\partial_\nu f=0$, so $f$ is linear, $\partial_\mu\partial_\nu\xi_\rho$ is constant, and $\xi$ is at most quadratic. Substituting a quadratic ansatz into the equation leaves exactly the four families.

2. The requirement reduces to $|x_1|^{\Delta_2-\Delta_1}|x_2|^{\Delta_1-\Delta_2}=1$ for all $x_1,x_2$, which fails for $\Delta_1\neq\Delta_2$ unless $C_{12}=0$.

3. Under inversion $\prod_{i<j}|x_{ij}|^{-a_{ij}}$ acquires $\prod_i|x_i|^{\sum_{j\neq i}a_{ij}}$, which must equal $\prod_i|x_i|^{2\Delta_i}$. The three equations $a_{12}+a_{13}=2\Delta_1$, $a_{12}+a_{23}=2\Delta_2$, $a_{13}+a_{23}=2\Delta_3$ give $a_{12}=\Delta_1+\Delta_2-\Delta_3$ and its permutations.

4. The norm is $2\Delta\,v^*\cdot v$. For the second level, $[K_\mu,P_\nu]P_\nu|\mathcal O\rangle$ gives $2(\Delta+1)P_\mu|\mathcal O\rangle-2(d-1)P_\mu|\mathcal O\rangle$, because $[M_{\mu\nu},P_\nu]=(d-1)P_\mu$, and $P_\nu[K_\mu,P_\nu]|\mathcal O\rangle=2\Delta P_\mu|\mathcal O\rangle$; the total is $4(\Delta+1-d/2)P_\mu|\mathcal O\rangle$.

5. The residue of a fourth-order pole is $\frac1{3!}\partial_z^3$ of the numerator at $z=w$, which gives $\frac c2\cdot\frac{(m+1)m(m-1)}{6}w^{m-2}=\frac c{12}(m+1)m(m-1)w^{m-2}$. The $w$-integral of $w^{n+m-1}$ is $\delta_{m+n,0}$, so the central term is $\frac c{12}m(m^2-1)\delta_{m+n,0}$.

6. With $z'=az$, $z''=a^2z$ and $z'''=a^3z$ for $a=2\pi/\ell$, one finds $\{z,w\}=a^2-\frac32a^2=-\frac{a^2}2$. The zero mode of $T_{\mathrm{cyl}}$ is $a^2(L_0-c/24)$, and the translation generator on a circle of circumference $\ell$ is $\frac{\ell}{2\pi}$ times it, which gives $E_0=-\pi(c+\bar c)/(12\ell)$. For a free boson, $c=\bar c=1$ and $\ell=2\pi$ give $E_0=-1/12$.

7. After the first inversion and the translation the point is $x/x^2-b$; inverting again gives $(x-bx^2)/(1-2b\cdot x+b^2x^2)$. To first order in $b$ this is $x+2(b\cdot x)x-bx^2$.

8. Dividing the sum of the three pairings by $x_{12}^{-2\Delta}x_{34}^{-2\Delta}$ gives $1+u^\Delta+(u/v)^\Delta$. Then $v^\Delta g(u,v)=v^\Delta+(uv)^\Delta+u^\Delta=u^\Delta g(v,u)$. The term 1 is the identity exchanged in the $(12)$ channel, dominant as $x_1\to x_2$.

9. For $z=(pw+q)/(rw+s)$ the ratios $z''/z'=-2r/(rw+s)$ and $z'''/z'=6r^2/(rw+s)^2$ give $\{z,w\}=0$. The composition law follows from the chain rule. Applying two maps in succession must give the same $T$ as applying their composition, and the Schwarzian terms combine correctly only because of this law.

10. From $E=\pi c\ell/(6\beta^2)$ one has $\beta=\sqrt{\pi c\ell/(6E)}$, and then $S=\pi c\ell/(3\beta)=\sqrt{2\pi c\ell E/3}$. With $L_0=\bar L_0$ and $L_0-c/24=E\ell/(4\pi)$, the microcanonical form gives $4\pi\sqrt{cE\ell/(24\pi)}$, the same number.

11. The energy above the vacuum is $\Delta/R$ for any $d$. In two dimensions both levels are shifted by the same Casimir energy $-(c+\bar c)/(24R)$ for a circle of circumference $2\pi R$, so the difference is unchanged.

12. Symmetry of $T$ replaces $\partial_\mu\xi_\nu$ by its symmetric part, the conformal Killing equation replaces that by $\frac1d(\partial\cdot\xi)\delta_{\mu\nu}$, and tracelessness removes the result. Conservation of $T$ was used first, to move the derivative onto $\xi$.

13. *Guide.* Expand the corrected dimensions $2\Delta+2n+\ell+\gamma_{n,\ell}/N^2$ inside the block decomposition; the term linear in $\gamma$ multiplies $\log u$. A bulk contact interaction produces anomalous dimensions only for spins up to a bound set by the number of derivatives, a result of Heemskerk, Penedones, Polchinski and Sully that Lecture 14 uses.

14. *Guide.* Split $Z$ into light and heavy states in each channel. Sparseness bounds the light contribution by the vacuum term up to corrections that are subleading at large $c$, and modular invariance transfers the bound to the heavy states. The two channels exchange dominance at $\beta=\ell$.

15. *Guide.* Impose the Brown–Henneaux falloffs on the metric, find the vector fields that preserve them, and compute the algebra of their canonical charges. The central term is the variation of the charge $Q_m$ of the AdS background under the transformation generated by $Q_n$, and it is nonzero only for $|m|\geq2$.
