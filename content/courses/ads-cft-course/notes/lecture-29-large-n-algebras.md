---
title: "Lecture 29 — Large-N algebras and state-dependent representations"
type: lecture-notes
edition: "2.2 — rewritten at the AQFT standard"
lecture: 29
semester: 2
week: 12
hours: 3
prerequisites: "Lectures 3, 9, 14, 23 and 28; the GNS construction, KMS states and the Weyl form of the canonical commutation relations"
status: "rewritten 2026-09-30, pending instructor review; the GNS construction and its qubit examples, the c-number commutator of a Gaussian family, the type I algebra of a generalized free field in thermal AdS, the spectral densities of thermal AdS3 and of planar BTZ, and the theorem that decaying correlators exclude a type I factor are proved or exact calculations; the converse type I criterion of Araki and Woods, the identification of large-N thermal correlators with bulk saddles, the type III1 algebra of the black-hole phase and the mirror operators of Papadodimas and Raju are stated with sources"
modified: 2026-09-30
---

# Lecture 29 — Large-N algebras and state-dependent representations

> *Lecture 28 found that local bulk physics requires a boundary theory whose algebras on adjacent regions do not generate the algebra of their union, as a generalized free field does. Large-$N$ theories produce generalized free fields in a precise limit, and this lecture asks which von Neumann algebra the limit produces. The answer depends on the state. A state defines a Hilbert space through the GNS construction, and at large $N$ the single-trace operators of a semiclassical state have Gaussian correlations, with a commutator that is a number fixed by the bulk geometry. In thermal AdS the spectrum is discrete, the thermal state is a density matrix on a Fock space, and the algebra is of type I. In the black-hole phase the correlators decay forever, and we prove that a connected correlator that decays without vanishing identically is incompatible with a type I factor: the algebra must be of another type, which Leutheusser and Liu identified as III$_1$. The change of type at the Hawking–Page transition is the algebraic form of Maldacena's observation of Lecture 23, and it sets up the half-sided modular inclusions of Lectures 30 and 31.*

## How to use this lecture

**Classroom core, one meeting of three hours.** The history (§1, 10 minutes), the GNS construction (§2, 20 minutes), and the large-$N$ limit of single-trace correlators (§3, 25 minutes) come before a 10-minute break. After it come thermal AdS and its type I algebra (§4, 25 minutes), the black-hole phase and the theorem that decay excludes type I (§5, 30 minutes), and state-dependent representations (§6, 20 minutes), with 40 minutes for Checkpoints 1 and 2 and Problems 4–6; Problems 1–3 complete the core assignment. These allocations are proposals and have not been tested in class.

**Self-study.** Three algebras that coexist at finite $N$ (§7), the order of limits in a toy spectrum (§8), and Problems 7–12, including the cylinder weights, the Bose factors, the quasi-free Weyl correlators and a recurrence.

**Research extension.** A proof of type III$_1$ for a thermal generalized free field, the microcanonical algebra of type II$_\infty$, and the late-time plateau of a finite model, in Problems 13–15.

**Prerequisites.** Lecture 3 for the modular operator of a finite system, Lecture 9 for Weyl operators and continuum algebras, Lecture 14 for factorization at large $N$, Lecture 23 for the thermofield double, the Hawking–Page transition and the planar BTZ correlator, Lecture 28 for generalized free fields. The GNS construction, KMS states and the Weyl form of the canonical commutation relations.

**What this lecture establishes.** The GNS construction with its two qubit examples, the c-number commutator of a family with Gaussian correlations, the type I algebra of a generalized free field in thermal AdS whenever its single-particle partition function converges, the spectral densities of thermal AdS$_3$ and of planar BTZ, and the theorem that a decaying connected correlator excludes a type I factor, with its corollary for the black-hole phase, are proved or exact calculations. The converse type I criterion of Araki and Woods, the identification of large-$N$ thermal correlators with bulk saddles, the type III$_1$ algebra of the black-hole phase and the mirror operators of Papadodimas and Raju are stated with sources.

## 0. Reading

**Primary.**

- S. Leutheusser, H. Liu, [Causal connectability between quantum systems and the black hole interior in holographic duality](https://arxiv.org/abs/2110.05497) (2021).
- H. Liu, [Lectures on entanglement, von Neumann algebras, and emergence of spacetime](https://arxiv.org/abs/2510.07017) (2025), section VI.
- J. Maldacena, [Eternal Black Holes in AdS](https://arxiv.org/abs/hep-th/0106112) (2001).

**Secondary.**

- E. Witten, [Notes on Some Entanglement Properties of Quantum Field Theory](https://arxiv.org/abs/1803.04993) (2018).
- M. Brigante, G. Festuccia, H. Liu, [Inheritance principle and Non-renormalization theorems at finite temperature](https://arxiv.org/abs/hep-th/0509117) (2005).
- J. L. F. Barbón, E. Rabinovici, [Very Long Time Scales and Black Hole Thermal Equilibrium](https://arxiv.org/abs/hep-th/0308063) (2003).
- R. Haag, *Local Quantum Physics* (Springer, 1996), chapter V.

**Optional research reading.**

- G. Festuccia, H. Liu, [The arrow of time, black holes, and quantum mixing of large N Yang-Mills theories](https://arxiv.org/abs/hep-th/0611098) (2006).
- K. Papadodimas, S. Raju, [An Infalling Observer in AdS/CFT](https://arxiv.org/abs/1211.6767) (2012).
- E. Witten, [Gravity and the Crossed Product](https://arxiv.org/abs/2112.12828) (2021).
- V. Chandrasekaran, G. Penington, E. Witten, [Large N algebras and generalized entropy](https://arxiv.org/abs/2209.10454) (2022).
- E. Witten, [Anti-de Sitter Space, Thermal Phase Transition, And Confinement In Gauge Theories](https://arxiv.org/abs/hep-th/9803131) (1998).
- H. Araki, E. J. Woods, "A classification of factors," *Publ. RIMS* 4 (1968) 51.

## 1. Which algebra does a large-$N$ limit produce?

Gelfand and Naimark in 1943, and Segal in 1947, showed that a positive normalized functional on an algebra of observables determines a Hilbert space on which the algebra acts. Physicists learned to read the construction backward: the state comes first, and the Hilbert space is the closure of the excitations that the state allows. The lesson became concrete for infinite systems. Araki and Woods found in 1963 that the representations describing an infinite free Bose gas at positive temperature are not of type I. In 1967 Haag, Hugenholtz and Winnink characterized equilibrium states of infinite systems by the KMS condition and found that their representations carry a commutant, a second copy of the observables, the structure that Takahashi and Umezawa later called thermofield dynamics (Lecture 23). In 1968 Araki and Woods classified the infinite tensor products of type I factors.

Large $N$ produces infinite systems of its own. 't Hooft's expansion of 1974 implies that single-trace correlators factorize at infinite $N$ (Lecture 14), and in 1983 Hawking and Page found the transition that Witten identified in 1998 with deconfinement. In 2001 Maldacena observed that correlators in the eternal AdS black hole decay forever, which no system with a discrete spectrum allows, and Barbón and Rabinovici traced the decay to the continuous spectrum that the horizon produces. Festuccia and Liu argued in 2006 that the high-temperature phase at large $N$ mixes exponentially many states and develops an arrow of time, and Papadodimas and Raju constructed in 2012 the interior operators of a black hole relative to a given state. Leutheusser and Liu put these observations together in 2021. The single-trace operators of a large-$N$ theory, in the GNS representation of the thermofield double above the Hawking–Page temperature, generate a von Neumann algebra of type III$_1$, which emerges from the type I algebra of the finite-$N$ theory. Witten showed in the same year that the leading $1/N$ correction changes the type to II$_\infty$.

This lecture proves the parts of this story that can be proved with the tools of the course. The GNS construction makes the state dependence explicit, factorization makes the commutator a number, a convergent partition function gives type I below the transition, and a decaying correlator excludes type I above it.

## 2. A state defines a Hilbert space

Let $\mathfrak A$ be a unital $*$-algebra and $\omega$ a state, a linear functional with $\omega(A^\dagger A)\geq0$ and $\omega(1)=1$. The sesquilinear form

$$
\langle A,B\rangle_\omega=\omega(A^\dagger B)
$$

is positive semidefinite, and the null vectors $\mathcal N_\omega=\{A:\omega(A^\dagger A)=0\}$ form a left ideal by the Cauchy–Schwarz inequality. The quotient $\mathfrak A/\mathcal N_\omega$, completed in the norm of the form, is the GNS Hilbert space $\mathcal H_\omega$. The algebra acts by left multiplication, $\pi_\omega(C)[A]=[CA]$, and the class of the identity $\Omega_\omega=[1]$ is a cyclic vector with

$$
\langle\Omega_\omega,\pi_\omega(A)\,\Omega_\omega\rangle=\omega(A).
$$

[Proved.] Any other cyclic representation that reproduces $\omega$ is unitarily equivalent to this one, so the triple $(\mathcal H_\omega,\pi_\omega,\Omega_\omega)$ is determined by the state. For a $C^*$-algebra the operators $\pi_\omega(C)$ are bounded; for polynomials in unbounded fields one works with their Weyl exponentials, as we will do.

A qubit shows what depends on the state. Take $\omega_\rho(A)=\operatorname{Tr}\rho A$ on $M_2(\mathbb C)$ with $\rho$ invertible. The map $[A]\mapsto A\sqrt\rho$ is an isometry onto the matrices with the Hilbert–Schmidt inner product, since

$$
\operatorname{Tr}\bigl(A\sqrt\rho\bigr)^\dagger\bigl(B\sqrt\rho\bigr)=\operatorname{Tr}\rho A^\dagger B ,
$$

so $\mathcal H_\omega$ is four-dimensional, the cyclic vector is $\sqrt\rho$, and it is separating because $A\sqrt\rho=0$ forces $A=0$. The modular operator is $\Delta X=\rho X\rho^{-1}$, as in Lecture 3, with eigenvalues $p_i/p_j$ (Problem 2). For a pure state $\rho=|0\rangle\langle0|$ the norm is $\|A|0\rangle\|^2$, the null vectors are the matrices whose first column vanishes, and $\mathcal H_\omega\cong\mathbb C^2$ with the defining representation. [Exact.] The algebra is $M_2(\mathbb C)$ in both cases. The state changed the dimension of the Hilbert space, the multiplicity of the representation and the existence of a modular operator, and it did not change the type, which is an invariant of the von Neumann algebra $\pi_\omega(\mathfrak A)''$.

**Checkpoint 1.** In the pure-state construction, is $\Omega_\omega$ separating for $\pi_\omega(M_2)$? What is the commutant?

**Answer.** No: the nonzero matrix $|0\rangle\langle1|$ annihilates $|0\rangle$. The representation on $\mathbb C^2$ is irreducible, so the commutant is $\mathbb C\,1$. A vector is separating for an algebra exactly when it is cyclic for the commutant, and $\mathbb C\,1$ has no cyclic vector on a two-dimensional space. Modular theory needs a faithful state, as in the first construction.

## 3. Single-trace correlators at infinite $N$

Let $\mathcal O_N$ be a single-trace operator normalized so that its two-point function is of order one, and let $\omega_N$ be a semiclassical state, such as the vacuum or a thermal state. By the counting of Lecture 14, the connected $n$-point functions are of order $N^{2-n}$. At infinite $N$ only the two-point function survives,

$$
W(x,y)=\lim_{N\to\infty}\omega_N\bigl(\mathcal O_N(x)\,\mathcal O_N(y)\bigr),
$$

after subtracting the one-point function, and all correlators are sums over pairings,

$$
\omega\bigl(\mathcal O(x_1)\cdots\mathcal O(x_{2n})\bigr)=\sum_{\text{pairings}}\ \prod_{(i,j),\,i<j}W(x_i,x_j),
$$

with odd correlators equal to zero. The order within each pair is the order in the product. A family with these correlators is a generalized free field with two-point function $W$. [Stated only — refs: Lecture 14; Leutheusser–Liu 2021.]

**Proposition (c-number commutator). Proved.** For a family with Gaussian correlators, in the GNS representation of $\omega$,

$$
[\mathcal O(f),\mathcal O(g)]=\bigl(W(f,g)-W(g,f)\bigr)\,1\equiv i\sigma(f,g)\,1 ,
$$

where $\mathcal O(f)=\int f\,\mathcal O$ and $W(f,g)=\int f(x)g(y)W(x,y)$.

*Proof.* Insert the commutator between two products $X$ and $Y$ of smeared fields and expand $\omega(X\,\mathcal O(f)\mathcal O(g)\,Y)-\omega(X\,\mathcal O(g)\mathcal O(f)\,Y)$ in pairings. A pairing that contracts $\mathcal O(f)$ with $\mathcal O(g)$ contributes $W(f,g)$ in the first term and $W(g,f)$ in the second, times the same sum over pairings of $XY$. In every other pairing the two fields are contracted with fields of $X$ or $Y$, and each contraction keeps its order when $f$ and $g$ are exchanged, so these terms cancel. Thus $\langle X^\dagger\Omega,[\mathcal O(f),\mathcal O(g)]\,Y\Omega\rangle=i\sigma(f,g)\,\langle X^\dagger\Omega,Y\Omega\rangle$ on a dense set of vectors. $\square$

The limiting algebra is therefore generated by the Weyl operators $W(f)=e^{i\mathcal O(f)}$ with

$$
W(f)\,W(g)=e^{-i\sigma(f,g)/2}\,W(f+g),\qquad \omega\bigl(W(f)\bigr)=e^{-W(f,f)/2},
$$

the canonical commutation relations over the symplectic form $\sigma$ in a quasi-free state. [Exact.] The abstract algebra depends only on $\sigma$, the antisymmetric part of $W$; the representation depends on the whole of $W$. For a field dual to a free bulk field, $\sigma$ is the commutator function of the bulk field, smeared and brought to the boundary as in Lecture 28. It depends on the bulk geometry and on nothing else. Two states on the same geometry give two representations of one algebra, and two states on different geometries give different commutation relations for the same smeared operators.

In global AdS$_3$ this can be made explicit. A primary of dimension $\Delta$ on the boundary cylinder, normalized to $|x|^{-2\Delta}$ at short distance, has at a fixed angle the vacuum two-point function

$$
W_0(\tau)=\Bigl[2i\sin\!\bigl((\tau-i\epsilon)/2\bigr)\Bigr]^{-2\Delta}=\sum_{k=0}^\infty c_k\,e^{-i(\Delta+k)\tau},
\qquad
c_k=\frac{\Gamma(k+2\Delta)}{k!\,\Gamma(2\Delta)},
$$

where the expansion in $u=e^{-i(\tau-i\epsilon)}$ is that of $u^\Delta(1-u)^{-2\Delta}$, with the power continued from $\tau=0$, which agrees with the principal branch for $|\tau|<2\pi$. [Exact calculation (Problem 7).] The frequencies $\Delta+k$ are the normal modes $\Delta+2n+|l|$ of the bulk field, collected at a fixed angle. The spectral density, the Fourier transform of the commutator,

$$
\rho(\omega)=\int dt\,e^{i\omega t}\,\omega\bigl([\mathcal O(t),\mathcal O(0)]\bigr)=2\pi\sum_kc_k\bigl[\delta(\omega-\Delta-k)-\delta(\omega+\Delta+k)\bigr],
$$

is a comb of lines, and it is the same in every state of the field on global AdS.

## 4. Thermal AdS: a discrete spectrum gives type I

Below the Hawking–Page temperature the thermal state of the boundary theory at large $N$ is described by thermal AdS, global AdS with periodic Euclidean time (Lecture 23). Its single-trace correlators are the thermal correlators of the bulk free fields, which are sums over images of the vacuum correlators in imaginary time. [Stated only — refs: Witten 1998; Brigante–Festuccia–Liu 2005.] The spectral density is the comb of §3, and the state attaches Bose factors to it. For any thermal state, the KMS condition gives

$$
\widetilde G_<(\omega)=e^{-\beta\omega}\,\widetilde G_>(\omega),\qquad \widetilde G_>(\omega)=\frac{\rho(\omega)}{1-e^{-\beta\omega}} ,
$$

where $\widetilde G_>$ and $\widetilde G_<$ are the Fourier transforms of $\omega(\mathcal O(t)\mathcal O(0))$ and $\omega(\mathcal O(0)\mathcal O(t))$. [Exact (Problem 8).] Figure (a) shows the comb for $\Delta=3/2$.

The bulk field is a collection of oscillators, one for each normal mode. In AdS$_{d+1}$ with $L=1$ the modes have frequencies $\omega_{n,l}=\Delta+2n+l$, with the degeneracy of the spherical harmonics of angular momentum $l$ on $S^{d-1}$, and the single-particle partition function is

$$
z(q)=\sum_{\text{modes}}q^{\omega}=\frac{q^\Delta}{(1-q)^d},\qquad q=e^{-\beta}.
$$

[Exact calculation, checked by series expansion for $d=2,3,4$.] In AdS$_3$ the modes are labeled by $n\geq0$ and $l\in\mathbb Z$, and the sum is $q^\Delta(1-q^2)^{-1}(1+q)(1-q)^{-1}=q^\Delta(1-q)^{-2}$.

**Proposition (type I below the transition). Proved.** Let the generalized free field be the boundary dual of a free bulk field on global AdS, and let $\omega_\beta$ be its thermal state. If $z(e^{-\beta})<\infty$, then $\omega_\beta$ is given by a density matrix on the Fock space $\mathcal F$ of the bulk field, and the von Neumann algebra generated in its GNS representation is a type I factor.

*Proof.* The thermal state is the product over modes of the Gibbs states $(1-q^{\omega})\,q^{\omega a^\dagger a}$ of the oscillators, and its density matrix on $\mathcal F$ is the product of these. Its normalization is

$$
Z=\prod_{\text{modes}}\bigl(1-q^{\omega}\bigr)^{-1},\qquad \log Z=\sum_{m=1}^\infty\frac{z(q^m)}m .
$$

For $0\leq x_k\leq x_*<1$, the product $\prod_k(1-x_k)^{-1}$ converges exactly when $\sum_kx_k$ does, since $x\leq-\log(1-x)\leq x/(1-x_*)$, and here $x_k=q^{\omega}\leq q^\Delta$. Therefore $\rho_\beta=e^{-\beta H}/Z$ is a positive trace-class operator on $\mathcal F$ with trivial kernel. The GNS representation of a faithful normal state of $\mathcal B(\mathcal F)$ is $\pi(X)=X\otimes1$ on $\mathcal F\otimes\overline{\mathcal F}$, with cyclic vector $\rho_\beta^{1/2}$, the thermofield double; the Fock representation of the Weyl operators is irreducible, so the generated algebra is $\mathcal B(\mathcal F)\otimes1$. $\square$

In thermal AdS the single-particle partition function converges at every temperature, so the algebra is of type I. Its commutant $1\otimes\mathcal B(\overline{\mathcal F})$ is the second copy, and the two copies of thermal AdS are entangled and disconnected. Araki and Woods proved the converse within their classification: an infinite tensor product of type I factors in faithful normal states is of type I exactly when $\sum_k(1-\lambda_k)$ converges, where $\lambda_k$ is the largest eigenvalue of the $k$-th density matrix. [Stated only — refs: Araki–Woods 1968.] For a thermal oscillator $\lambda=1-e^{-\beta\omega}$, so the criterion is the convergence of $z$. A theory with infinitely many species must add their single-particle sums; for a string spectrum the total diverges above the Hagedorn temperature, which at strong coupling lies far above the Hawking–Page temperature. [Heuristic.]

## 5. The black-hole phase: decay excludes type I

Above the Hawking–Page temperature the large-$N$ thermal state is described by the black hole. For the planar BTZ black hole, Lecture 23, §7, found the boundary correlator at a fixed point,

$$
G(t)=\left(\frac\pi\beta\right)^{2\Delta}\Bigl[i\sinh\!\bigl(\pi(t-i\epsilon)/\beta\bigr)\Bigr]^{-2\Delta},
\qquad
|G(t)|\to\left(\frac{2\pi}\beta\right)^{2\Delta}e^{-2\pi\Delta t/\beta}.
$$

Its Fourier transform follows from a shift of contour. The function is analytic in the strip $-\beta<\operatorname{Im}t<0$, and on the line $\operatorname{Im}t=-\beta/2$ it is real, $G(s-i\beta/2)=(\pi/\beta)^{2\Delta}\cosh^{-2\Delta}(\pi s/\beta)$. With

$$
\int_{-\infty}^\infty ds\,\frac{e^{i\omega s}}{\cosh^{2\Delta}(as)}=\frac{2^{2\Delta-1}}{a\,\Gamma(2\Delta)}\,\Bigl|\Gamma\Bigl(\Delta+\frac{i\omega}{2a}\Bigr)\Bigr|^2 ,
$$

at $a=\pi/\beta$, we obtain

$$
\widetilde G_>(\omega)=e^{\beta\omega/2}\left(\frac{2\pi}\beta\right)^{2\Delta-1}\frac{\bigl|\Gamma(\Delta+i\beta\omega/2\pi)\bigr|^2}{\Gamma(2\Delta)},
\qquad
\rho(\omega)=2\sinh\frac{\beta\omega}2\left(\frac{2\pi}\beta\right)^{2\Delta-1}\frac{\bigl|\Gamma(\Delta+i\beta\omega/2\pi)\bigr|^2}{\Gamma(2\Delta)} .
$$

[Exact calculation, checked numerically.] The density is continuous and positive for every $\omega>0$, and it satisfies the KMS relation of §4, since $|\Gamma(\Delta+iy)|$ is even in $y$ (Problem 5). As $\beta\to\infty$ it tends to the vacuum density $2\pi\,\omega^{2\Delta-1}/\Gamma(2\Delta)$ of the boundary line. Figure (b) shows it at $\beta=2L$, above the transition at $\beta=2\pi L$. At finite $N$ the spectrum of the boundary theory on its circle is still discrete, with levels spaced by $e^{-O(N^2)}$ at these energies, and at infinite $N$ they have merged into a continuum.

![[ads-cft-large-n-spectra.svg|Left: the spectral density of a boundary generalized free field in thermal AdS3 for dimension 1.5, a comb of lines at the normal-mode frequencies Δ+k whose weights grow with k. Center: the spectral density of the same operator in the planar BTZ black hole at inverse temperature 2L, a smooth function of frequency that starts linearly at zero. Right: the modulus of the toy correlator C_N(t) for N equal to 20 and 60 together with its limit at fixed time, with the full recurrence of the N equal to 20 curve at t equal to 2πN.]]

A continuous density is evidence about the algebra, and the decay of the correlator turns it into a theorem.

**Proposition (decay excludes a type I factor). Proved.** Let $\mathcal M$ be a type I factor with a faithful normal state $\omega$ that is KMS at inverse temperature $\beta$ for a one-parameter group of automorphisms $\alpha_t$. Then for all $A,B\in\mathcal M$ the function

$$
F(t)=\omega\bigl(A\,\alpha_t(B)\bigr)-\omega(A)\,\omega(B)
$$

is almost periodic, and if $F(t)\to0$ as $t\to\infty$ then $F$ vanishes identically.

*Proof.* A type I factor is $\mathcal B(\mathcal K)$, up to multiplicity, and a faithful normal state is $\omega(X)=\operatorname{Tr}\rho X$ with $\rho$ trace class and injective. Its modular group is $\sigma_s(X)=\rho^{-is}X\rho^{is}$, as for the qubit of §2, and by Takesaki's theorem the only group for which $\omega$ is KMS at $\beta$ is $\alpha_t=\sigma_{t/\beta}$. Thus $\alpha_t(X)=e^{iHt}Xe^{-iHt}$ with $\rho=e^{-\beta H}$, the additive constant in $H$ fixed by $\operatorname{Tr}\rho=1$, and since $\rho$ is compact and injective, $H$ has a discrete spectrum $\{E_i\}$ with eigenvalues $p_i=e^{-\beta E_i}$ of $\rho$. In the eigenbasis,

$$
\omega\bigl(A\,\alpha_t(B)\bigr)=\sum_{i,j}p_i\,A_{ij}B_{ji}\,e^{i(E_j-E_i)t},
\qquad
\sum_{i,j}p_i\,|A_{ij}B_{ji}|\leq\bigl(\operatorname{Tr}\rho AA^\dagger\bigr)^{1/2}\bigl(\operatorname{Tr}\rho B^\dagger B\bigr)^{1/2},
$$

by the Cauchy–Schwarz inequality with weights $p_i$. The series converges absolutely, so $F$ is almost periodic, $F(t)=\sum_\nu a_\nu e^{i\nu t}$ with $\sum_\nu|a_\nu|<\infty$. Its mean square is $\lim_{T\to\infty}\frac1T\int_0^T|F|^2dt=\sum_\nu|a_\nu|^2$. If $F\to0$, the mean square vanishes, every $a_\nu$ vanishes, and $F\equiv0$. $\square$

This is the algebraic content of Lecture 23, §7: a type I factor cannot forget. Now apply it at infinite $N$. For a quasi-free state the Weyl correlators are

$$
\omega\bigl(W(f)\,\alpha_t(W(g))\bigr)=\omega\bigl(W(f)\bigr)\,\omega\bigl(W(g)\bigr)\,e^{-W_\beta(f,g_t)},
$$

where $g_t$ is the test function translated by $t$ (Problem 10), and in the black-hole phase $W_\beta(f,g_t)$ decays as $e^{-2\pi\Delta t/\beta}$.

**Corollary (the black-hole phase). Proved, given the large-$N$ correlator.** In the thermal state above the Hawking–Page temperature, the von Neumann algebra generated by a single-trace generalized free field in its GNS representation is a factor and is not of type I.

*Proof.* The connected Weyl correlators tend to zero, and the Weyl operators span a weakly dense $*$-algebra, so the time evolution, implemented by $U_t=\Delta^{-it/\beta}$, converges weakly to the projection onto $\Omega$. A central element $C$ is fixed by the modular group, so $C\Omega$ is invariant under $U_t$ and equal to its limit $\omega(C)\Omega$; since $\Omega$ is separating, $C=\omega(C)1$, and the algebra is a factor. A nonvanishing connected correlator that tends to zero is excluded in a type I factor by the proposition. $\square$

The proposition says nothing against a type II$_\infty$ factor, whose faithful normal states can have densities with continuous spectrum relative to the trace, or against type III. Leutheusser and Liu argued that the algebra of the black-hole phase is of type III$_1$, the type of the algebra of a free field outside a bifurcate Killing horizon, and contrasted it with the type I algebra of the thermal AdS phase, in agreement with §4. [Stated only — refs: Leutheusser–Liu 2021; Liu 2025.] Lecture 30 develops the structure they used, the half-sided modular inclusion.

> **Physical picture: a horizon is where the spectrum becomes continuous.** A perturbation of the black hole falls through the horizon and never returns, and its correlator decays. A system with discrete levels cannot do this: a superposition of countably many frequencies with summable amplitudes returns arbitrarily close to its initial value. At finite $N$ the black hole has discrete levels spaced by $e^{-S}$, and on every time scale held fixed as $N\to\infty$ they behave as a continuum. The limit trades recurrences for a horizon, and the proposition records the trade in the type of the algebra.

**Checkpoint 2.** Why does the proposition not exclude a type II$_\infty$ factor?

**Answer.** In a type II$_\infty$ factor with trace $\tau$, a faithful normal state is $\omega(X)=\tau(\rho X)$ with a density $\rho$ affiliated with the algebra, and $\rho$ may have continuous spectrum. The modular flow is $X\mapsto\rho^{-is}X\rho^{is}$, inner in the algebra, but the frequencies $E_j-E_i$ of the proof now form a continuum and the correlators can decay. This is the situation Witten found once $1/N$ corrections are included.

## 6. State-dependent representations

At infinite $N$ the representation is chosen together with the state, and the three examples of the lecture show three different relations between states. The vacuum and thermal AdS give two representations of one algebra, since the commutator is the same, and by §4 they are quasi-equivalent: the thermal state is a density matrix on the vacuum Fock space. The black-hole phase gives different commutation relations for the same smeared operators, and by §5 the algebra they generate is not of type I: no Hilbert space carries it as the algebra of all bounded operators with the thermal state as a density matrix. A state obtained from the thermofield double by finitely many single-trace operators lies in its GNS space. A state that differs from it by an energy of order $N^2$, such as the vacuum, has the correlators of another saddle and lies outside. [Heuristic.]

None of this introduces nonlinear quantum mechanics. Within a representation, observables are linear operators and probabilities follow the Born rule. The choice of representation resembles the choice of a background in perturbation theory, or of a superselection sector, and two descriptions can be compared only on a common domain with a specified map between them. Papadodimas and Raju constructed the operators behind the horizon of a one-sided black hole in this way: for a state close to thermal, the single-trace operators of the right system have mirror operators that act on the excitations of that state as the left operators act on the thermofield double. [Stated only — refs: Papadodimas–Raju 2012.] In the thermofield double itself the mirror of $\mathcal O$ is $J\mathcal O J$, by the theorem of Tomita and Takesaki, $J\mathcal MJ=\mathcal M'$, and the construction needs no choice. For a single black hole the state enters through the modular conjugation, which is why the construction depends on it.

## 7. Self-study: three algebras at finite $N$

Three different algebras appear in these statements, and they have different types. The full algebra of the boundary theory on a sphere, at finite $N$, acts irreducibly on a Hilbert space with a discrete spectrum and a trace-class $e^{-\beta H}$; it is $\mathcal B(\mathcal H)$, of type I, and its thermal states are Gibbs states. The algebra of a bounded region of the boundary spacetime, such as a diamond, is an algebra of a continuum quantum field theory, of type III$_1$ at every $N$. [Hypothesis-explicit: under the nuclearity and scaling hypotheses of Lecture 9.] And the algebra generated by single-trace operators in the large-$N$ limit of a given state is a third object, defined by the GNS construction of §2, whose type depends on the phase as §§4–5 showed.

A time band, the neighborhood of a whole Cauchy surface of the boundary, behaves differently from a diamond. At finite $N$ the time-slice property makes its algebra equal to the full algebra, since the Hamiltonian evolves the band into any other time. At infinite $N$ the generalized free field has no such property, because its correlators do not follow from those at one time, and the algebra of single-trace operators in a band becomes a proper subalgebra. [Stated only — refs: Leutheusser–Liu 2021.] Lecture 31 uses half-infinite bands of this kind.

The emergent type III$_1$ algebra of the black-hole phase therefore concerns the global algebra of simple operators on one boundary, all times included, which is of type I at every finite $N$ and loses that type in the limit. The local algebras of the boundary theory are of type III$_1$ for a different reason, at every $N$ and under the hypotheses of Lecture 9.

## 8. Self-study: the order of limits

A toy spectrum shows how a limit can change late times without changing early times. Consider

$$
C_N(t)=\frac1N\sum_{j=0}^{N-1}e^{-ijt/N},
\qquad
|C_N(t)|=\left|\frac{\sin(t/2)}{N\sin(t/2N)}\right| .
$$

At fixed $t$ the Riemann-sum limit is $C_\infty(t)=\int_0^1d\nu\,e^{-i\nu t}=e^{-it/2}\,2\sin(t/2)/t$, which decays as $1/t$. For every finite $N$, $C_N(2\pi N)=1$, and the long-time average of $|C_N|^2$ is $1/N$, the sum of the squared weights. [Exact.] The limit $N\to\infty$ at fixed $t$ cannot see the recurrence, which moves to infinity with $N$, and the floor $1/N$ of the mean of $|C_N|^2$ is the analogue of the time average of $|G(t)/G(0)|^2$ in Lecture 23, with $N$ in the role of the number of frequencies $E_m-E_n$. Figure (c) shows $N=20$ and $N=60$.

The algebraic statement of §5 is the same observation for the full family of correlators. At each finite $N$ the correlators are almost periodic; at infinite $N$ some of them decay; the type of the limiting algebra registers which of the two holds.

## 9. What to take away

- **Proved:** a state determines its GNS representation up to unitary equivalence; the qubit examples show the state changing the dimension, the multiplicity and the existence of a modular operator, and leaving the type unchanged.
- **Proved:** for Gaussian correlators the commutator is the number $W(f,g)-W(g,f)$; the limiting algebra is a CCR algebra fixed by the bulk geometry, and its representation is fixed by the state.
- **Proved:** in thermal AdS the single-particle partition function $q^\Delta/(1-q)^d$ converges, the thermal state is a density matrix on the Fock space, and the algebra is of type I; the converse criterion of Araki and Woods is stated.
- **Exact calculation:** the spectral density is a comb in thermal AdS$_3$ and the continuous function $2\sinh(\beta\omega/2)(2\pi/\beta)^{2\Delta-1}|\Gamma(\Delta+i\beta\omega/2\pi)|^2/\Gamma(2\Delta)$ in planar BTZ.
- **Proved:** a nonvanishing connected correlator that decays to zero is impossible in a type I factor with a faithful normal KMS state; in the black-hole phase the large-$N$ algebra is a factor not of type I, and Leutheusser and Liu identify it as type III$_1$ (stated).

## 10. Looking ahead

The type III$_1$ algebra of the black-hole phase has no density matrices, and its modular flow is outer. Lecture 30 studies a pair of such algebras, one inside the other, whose modular flows generate a translation that no single modular flow provides. Lecture 31 applies the structure to the outgoing sector of the JT model of Lecture 25 and constructs a time evolution that crosses the future horizon.

## 11. Problem set

### Classroom core

1. **The pure qubit.** For $\omega(A)=\langle0|A|0\rangle$ on $M_2(\mathbb C)$, find the null vectors, the dimension of $\mathcal H_\omega$, and a nonzero operator that annihilates $\Omega_\omega$.

2. **The faithful qubit.** For $\rho=\operatorname{diag}(p_1,p_2)$ invertible, show that $S(A\sqrt\rho)=A^\dagger\sqrt\rho$ is $J\Delta^{1/2}$ with $JX=X^\dagger$ and $\Delta X=\rho X\rho^{-1}$, and list the eigenvalues of $\Delta$.

3. **A Gaussian four-point function.** Using the pairing rule of §3, compute $\omega(\mathcal O(f_1)\,[\mathcal O(f_2),\mathcal O(f_3)]\,\mathcal O(f_4))$ and verify that it equals $i\sigma(f_2,f_3)\,W(f_1,f_4)$.

4. **The single-particle sum.** Derive $z(q)=q^\Delta/(1-q)^2$ for a scalar in AdS$_3$ from $\omega_{n,l}=\Delta+2n+|l|$, and show that $\log Z=\sum_mz(q^m)/m$.

5. **The BTZ spectral density.** Starting from $G(t)$ of §5, shift the contour to $\operatorname{Im}t=-\beta/2$, use the cosh integral, and derive $\widetilde G_>(\omega)$ and $\rho(\omega)$. Check the KMS relation and the limit $\beta\to\infty$.

6. **Decay excludes type I.** Reproduce the proof of the proposition of §5, and explain where each of the hypotheses, type I, factor, faithful, normal and KMS, enters.

### Self-study consolidation

7. **The cylinder weights.** Expand $[2i\sin((\tau-i\epsilon)/2)]^{-2\Delta}$ in $u=e^{-i(\tau-i\epsilon)}$ and obtain $c_k=\Gamma(k+2\Delta)/k!\,\Gamma(2\Delta)$. Show with the Vandermonde identity that $c_k=\sum_{m+n=k}(\Delta)_m(\Delta)_n/m!\,n!$, the sum over pairs of left and right descendants at level $k$, weighted by their norms.

8. **Bose factors and images.** Derive $\widetilde G_<=e^{-\beta\omega}\widetilde G_>$ from the KMS condition, and show that for a single mode of frequency $\omega_0$ the image sum $\sum_{m\geq0}e^{-i\omega_0(\tau-im\beta)}$ reproduces the factor $1+n_B(\omega_0)$.

9. **Products and sums.** Prove that $\prod_k(1-x_k)^{-1}$ converges for $0\leq x_k<1$ exactly when $\sum_kx_k$ does, and compute $1-\lambda_{\max}$ for a thermal oscillator.

10. **Weyl correlators.** For a quasi-free state, derive $\omega(W(f)W(g))=\omega(W(f))\,\omega(W(g))\,e^{-W(f,g)}$ from the Weyl relation and the formula for $\omega(W(f))$.

11. **Classify a statement.** "A continuous spectral density proves that the algebra is of type III$_1$." What does a decaying correlator prove, and what does it leave open?

12. **A recurrence.** Show that $C_N(2\pi N)=1$, that $C_N(t)\to C_\infty(t)$ at fixed $t$, and that the long-time average of $|C_N(t)|^2$ is $1/N$.

### Research extension

13. **Type III$_1$ for a thermal generalized free field.** Prove that the algebra of a generalized free field in a KMS state whose spectral density is positive for every $\omega>0$ is a factor of type III$_1$. *Known:* the corollary of §5 gives a factor not of type I; Leutheusser and Liu argue for type III$_1$; for quasi-free states the modular operator is the second quantization of a one-particle operator. *Completion:* a computation of Connes' invariant $S(\mathcal M)$, or an equivalent argument, with each hypothesis on $\rho(\omega)$ made explicit.

14. **The microcanonical algebra.** Chandrasekaran, Penington and Witten constructed a type II$_\infty$ algebra for the large-$N$ black hole in the microcanonical ensemble. *Known:* the crossed product of a type III$_1$ algebra by its modular group is of type II$_\infty$, and the entropy of semiclassical states is the generalized entropy. *Completion:* the operator adjoined to the algebra in the BTZ case, its spectrum, and the trace of a semiclassical state.

15. **The plateau of a finite model.** Combine the toy spectrum of §8 with the random-matrix statistics of Lecture 23, §7. *Known:* the plateau of the spectral form factor is $Z(2\beta)/Z(\beta)^2$, and Barbón and Rabinovici identified the time scales of the eternal black hole. *Completion:* the time at which the infinite-$N$ correlator fails, as a function of $N$, for a model whose level density reproduces the BTZ density of §5.

## 12. Answer checkpoints

1. The null vectors are the matrices with $A|0\rangle=0$, those with vanishing first column, and $\mathcal H_\omega\cong\mathbb C^2$ through $[A]\mapsto A|0\rangle$. The operator $|0\rangle\langle1|$ annihilates $\Omega_\omega=|0\rangle$.

2. $J\Delta^{1/2}(A\sqrt\rho)=(\rho^{1/2}A\sqrt\rho\,\rho^{-1/2})^\dagger=(\rho^{1/2}A)^\dagger=A^\dagger\sqrt\rho$. The eigenvectors of $\Delta$ are the matrix units $E_{ij}$, with $\Delta E_{ij}=(p_i/p_j)E_{ij}$, so the eigenvalues are $1$, $1$, $p_1/p_2$ and $p_2/p_1$.

3. The three pairings of four fields give $W_{12}W_{34}+W_{13}W_{24}+W_{14}W_{23}$ for the order $1234$ and $W_{13}W_{24}+W_{12}W_{34}+W_{14}W_{32}$ for $1324$. The difference is $W_{14}(W_{23}-W_{32})=i\sigma(f_2,f_3)W(f_1,f_4)$.

4. $\sum_{n\geq0}q^{2n}=1/(1-q^2)$ and $\sum_{l\in\mathbb Z}q^{|l|}=(1+q)/(1-q)$, whose product with $q^\Delta$ is $q^\Delta/(1-q)^2$. Then $\log Z=-\sum_{\text{modes}}\log(1-q^\omega)=\sum_{\text{modes}}\sum_mq^{m\omega}/m=\sum_mz(q^m)/m$.

5. $\int e^{i\omega t}G(t)\,dt=e^{\beta\omega/2}\int e^{i\omega s}G(s-i\beta/2)\,ds$, and the cosh integral at $a=\pi/\beta$ gives $\widetilde G_>$. Then $\widetilde G_>(-\omega)=e^{-\beta\omega}\widetilde G_>(\omega)$ because $|\Gamma(\Delta+iy)|$ is even in $y$, and as $\beta\to\infty$, $|\Gamma(\Delta+iy)|^2\simeq2\pi y^{2\Delta-1}e^{-\pi y}$ gives $2\pi\omega^{2\Delta-1}/\Gamma(2\Delta)$.

6. Type I and factor give $\mathcal M\cong\mathcal B(\mathcal K)$; normal gives a density matrix; faithful makes it injective, so that its modular group exists; KMS identifies $\alpha_t$ with the modular group and forces the Gibbs form. Without the factor property a diffuse center allows frequencies that vary continuously across it.

7. $u^\Delta(1-u)^{-2\Delta}=\sum_k\frac{(2\Delta)_k}{k!}u^{\Delta+k}$, and $(2\Delta)_k=\Gamma(k+2\Delta)/\Gamma(2\Delta)$. At a fixed angle the left and right factors $u^{\Delta/2}(1-u)^{-\Delta}$ multiply, and the coefficient of $u^{\Delta+k}$ is $\sum_{m+n=k}(\Delta)_m(\Delta)_n/m!\,n!=(2\Delta)_k/k!$.

8. KMS says $\omega(\mathcal O(0)\mathcal O(t))=\omega(\mathcal O(t-i\beta)\mathcal O(0))$; the Fourier transform of the right side is $e^{-\beta\omega}\widetilde G_>(\omega)$. The image sum is $e^{-i\omega_0\tau}\sum_me^{-m\beta\omega_0}=e^{-i\omega_0\tau}(1-e^{-\beta\omega_0})^{-1}=e^{-i\omega_0\tau}(1+n_B)$.

9. From $x\leq-\log(1-x)\leq x/(1-x)\leq x/(1-\max_kx_k)$ the series $\sum_k-\log(1-x_k)$ and $\sum_kx_k$ converge together, provided $\sup_kx_k<1$. A thermal oscillator has largest eigenvalue $1-e^{-\beta\omega}$, so $1-\lambda_{\max}=e^{-\beta\omega}$.

10. $W(f)W(g)=e^{-i\sigma(f,g)/2}W(f+g)$ and $W(f+g,f+g)=W(f,f)+W(g,g)+W(f,g)+W(g,f)$. With $i\sigma(f,g)=W(f,g)-W(g,f)$ the exponent becomes $-\frac12W(f,f)-\frac12W(g,g)-W(f,g)$.

11. The claim is insufficient. A nonvanishing connected correlator that decays excludes a type I factor, and if all connected Weyl correlators decay the algebra is a factor (the corollary of §5); together they exclude type I. Types II$_\infty$ and III remain open, and among the type III factors the subtype requires Connes' invariant.

12. Each term of $C_N(2\pi N)$ is $e^{-2\pi ij}=1$. At fixed $t$ the sum is a Riemann sum for $\int_0^1e^{-i\nu t}d\nu$. The frequencies $j/N$ are distinct, so the mean of $|C_N|^2$ is $\sum_j(1/N)^2=1/N$.

**Wiki connections.** [[type-iii-von-neumann-algebras|type III₁ von Neumann algebras]] · [[large-n-factorization|large-N factorization]] · [[thermofield-double-state|thermofield double]] · [[crossed-product-construction|crossed product]]
