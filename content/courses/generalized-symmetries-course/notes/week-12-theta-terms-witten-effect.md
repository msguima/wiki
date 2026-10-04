---
title: "Week 12 — θ-Terms, the Witten Effect, and Oblique Responses"
type: lecture-notes
course: syllabus
semester: 1
week: 12
block: C
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 8–11; the Villain formulation and cup products (Weeks 2, 8); electromagnetic duality
modified: 2026-10-04
---

# Week 12 — θ-Terms, the Witten Effect, and Oblique Responses

> *A θ-angle multiplies a total derivative, and yet on a compact gauge field it changes the physics. Monopoles become dyons of electric charge $\theta/2\pi$ (the Witten effect), the theory at $\theta+2\pi$ returns to itself only after the charge lattice is relabelled, and near $\theta=\pi$ dyons can condense into oblique-confined phases. The lattice shows where the periodicity comes from. The naive discretization of $F\wedge F$ is not an integer, and neither is the Villain one once monopoles are allowed, so an exactly $2\pi$-periodic θ needs the monopole-free Villain theory that Semester II Week 12 builds systematically. When θ varies in space the same term is axion electrodynamics, and a θ-wall carries a Hall conductivity; this is where the course meets topological insulators, Weyl semimetals and the group's condensed-matter line.*

### How to use this chapter

- **In class:** the first lecture derives the normalization $S_\theta=-\frac\theta{4\pi^2}\int E\cdot B$ and the Euclidean weight $e^{i\theta Q}$ with the orientation stated (§§3.1–3.2), the θ-modified momentum, Gauss's law and the integer $n_e$ (§§4.1–4.2), and spectral flow with Figure 1 (§5). The second lecture writes the lattice θ-term $Q_{\rm lat}=\frac12\sum n\cup n-\frac1{4\pi}\sum(a\cup dn-dn\cup a)$ (§6.2), proves it integer on $T^4$ without monopoles (§6.3), computes the lattice Witten phase of a static monopole (§6.4, Figure 2), works the oblique example of §7.3, and ends with the Hall conductivity of a θ-wall (§8.2, Figure 4). The core Problems 1–3 extend §§4–5, §6 and §8.
- **For self-study:** integrality and the spin structure (§3.3), the Lagrangian route to the Witten effect with its surface terms (§4.3), the naive density (§6.1), the duality group, the confinement criterion and the phase sketch (§§7.1, 7.2, 7.4, Figure 3), the condensed-matter dictionary (§8.3) and the fine print (§9). The one calculation to do alone is the reproducible check of §6: on the $4^4$ torus with one unit of flux through the (1,2) and (3,4) tori, recover $Q_{\rm lat}=1$ and $Q_{\rm naive}=0.9496$, and on the $3^4$ torus recover $Q_{\rm lat}=L\alpha/2\pi$ for the static monopole of §6.4.
- **Instructor checkpoint:** two errors recur at the board. Every θ-odd sign of the week (the Witten charge, the direction of the wall current, which dyon condenses above $\theta=\pi$) follows from $-\frac\theta{4\pi^2}E\cdot B$ and the orientation $dt\wedge dx^1\wedge dx^2\wedge dx^3$, and a sign copied from a source with the opposite convention flips all of them at once (F1). And the plain Villain θ-term is not $2\pi$-periodic: dropping the term $-\frac1{4\pi}\sum(a\cup dn-dn\cup a)$, which is exactly the Witten coupling of the monopoles, turns a false statement into an apparently proved one.

## 1. Reading

**Primary:** Witten, "Dyons of charge $e\theta/2\pi$", *Phys. Lett. B* 86 (1979) 283, after §4, translating his sign conventions as in F1. Cardy & Rabinovici, "Phase structure of $\mathbb{Z}_p$ models in the presence of a θ parameter", *Nucl. Phys. B* 205 (1982) 1, and Cardy, "Duality and the θ parameter in abelian lattice models", *Nucl. Phys. B* 205 (1982) 17, after §7.

**Secondary:**
- Wilczek, "Two applications of axion electrodynamics", *Phys. Rev. Lett.* 58 (1987) 1799, after §8.
- Sulejmanpasic & Gattringer, *Nucl. Phys. B* 943 (2019) 114616 [arXiv:1901.02637]: a Villain-type lattice formulation obtained by gauging the center symmetry of a noncompact abelian theory, with a four-dimensional θ-term and the Witten effect for magnetically charged matter; read after §6.
- Qi, Hughes, Zhang, *Phys. Rev. B* 78 (2008) 195424 [arXiv:0802.3537], the θ-term as the effective theory of time-reversal-invariant topological insulators, after §8.3.
- Witten, "The Chern–Simons function and the quantum Hall effect", to appear in *Bull. Amer. Math. Soc.* [arXiv:2609.21182], §§1–3, after §8: the Chern–Simons function defined by extending the connection over a 4-manifold (his (25)), the integrality of $\frac1{8\pi^2}\int F\wedge F$ only on spin manifolds (his (23)–(24), our §3.3), and the integer Hall level of a two-dimensional insulator, in one argument written for mathematicians. See [[2026-witten-chern-simons-quantum-hall]].
- The concept page [[axionic-electrodynamics]] and the area [[condensed-matter-connections]].

**Optional research reading:** 't Hooft, *Nucl. Phys. B* 190 (1981) 455, where oblique confinement was proposed; Zyuzin & Burkov, *Phys. Rev. B* 86 (2012) 115133 [arXiv:1206.1868], and Vazifeh & Franz, *Phys. Rev. Lett.* 111 (2013) 027201 [arXiv:1303.5784], for Problem 7⋆⋆; Gorantla, Lam, Seiberg, Shao, arXiv:2103.01257, for the modified Villain theories of Semester II Week 12; the group's papers listed in §8.3.

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]]. Signs and normalizations: [[courses/generalized-symmetries-course/conventions|conventions]] §10 (θ-term and Witten effect), §8 (cup product), §§4–6 (Villain form, duality, form degrees).

## 2. Motivation and setting

Gauge invariance and locality allow a second quadratic term in Maxwell theory, proportional to $E\cdot B$. It is odd under parity and under time reversal, and it is a total derivative, so with a constant coefficient it does not enter the classical equations of motion. The question of this week is what such a term does in compact $U(1)$ gauge theory, where magnetic monopoles exist and the gauge field is not a global 1-form. The answers come in three parts. In the Hilbert space the term shifts the electric charge of every monopole by $\theta/2\pi$ per unit of magnetic charge (the Witten effect, §4), so that θ is an angle only up to a relabelling of the charge lattice (§5). On the lattice, the integer that makes the angle periodic exists only when the monopoles are removed, and the obstruction is the Witten coupling itself (§6). And where θ varies, the total derivative leaves a boundary term: a θ-wall is a Hall layer (§8), which in condensed matter is the surface of a topological insulator. In between, the Witten effect decides which dyons condense at strong coupling, and the pattern of confined charges changes as θ crosses π (§7).

In the language of [[courses/generalized-symmetries-course/conventions|conventions]] §6 the degrees and the groups of the higher-form symmetries of four-dimensional Maxwell theory are unchanged by the θ-term: both are $U(1)^{(1)}$ (see [[higher-form-symmetries]]). The magnetic closed form is $F/2\pi$. The electric one, whose symmetry operator has a $2\pi$-periodic parameter, becomes $\star F/e^2-i\theta F/4\pi^2$ in the Euclidean variables of §3.2, whose flux through a spatial sphere is $i$ times that of $E/e^2-\theta B/4\pi^2$; the flux of $E/e^2$ alone measures $q_e$, and $e^{2\pi i\oint E\cdot dS/e^2}$ acts on a line of charges $(n_e,n_m)$ as $e^{i\theta n_m}$, a magnetic rotation by θ. The assignment of charges to lines changes. The flux that is an integer on every line is that of $E/e^2-\theta B/4\pi^2$ (§4.2), and a line of magnetic charge $n_m$ carries the electric flux $\theta n_m/2\pi$.

## 3. The θ-term

### 3.1 Normalization in Minkowski signature [Computed.]

The Minkowski components of the gauge field are fixed by the rule that a point charge $q$ contributes $q\int a$ to the action, so that its Euclidean insertion is the Wilson line $e^{iq\oint a}$ of [[courses/generalized-symmetries-course/conventions|conventions]] §6:
$$
a=-\phi\,dt+A_i\,dx^i,\qquad q\int a=\int dt\,\big(-q\phi+q\,A\cdot v\big),
$$
where φ and $A$ are the scalar and vector potentials, $v$ is the velocity of the charge, $E=-\nabla\phi-\partial_tA$ and $B=\nabla\times A$. Then
$$
F=da=-E_i\,dt\wedge dx^i+B_3\,dx^1\wedge dx^2+B_1\,dx^2\wedge dx^3+B_2\,dx^3\wedge dx^1,
$$
and in $F\wedge F$ only the products of an electric term with a magnetic term survive, each twice,
$$
F\wedge F=-2\,E_i\,dt\wedge dx^i\wedge\big(B_3\,dx^1\wedge dx^2+B_1\,dx^2\wedge dx^3+B_2\,dx^3\wedge dx^1\big)=-2\,E\cdot B\;dt\wedge dx^1\wedge dx^2\wedge dx^3,
$$
where we used $dx^2\wedge dx^3\wedge dx^1=dx^3\wedge dx^1\wedge dx^2=dx^1\wedge dx^2\wedge dx^3$, since cyclic permutations of three are even. With the orientation $dt\wedge dx^1\wedge dx^2\wedge dx^3$ of [[courses/generalized-symmetries-course/conventions|conventions]] §10,
$$
\boxed{\ S_\theta=\frac{\theta}{8\pi^2}\int F\wedge F=-\frac{\theta}{4\pi^2}\int d^4x\;E\cdot B .\ }
$$
In components $F\wedge F=\frac14\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\,d^4x$, with $\varepsilon^{0123}=+1$ the permutation symbol of this orientation, so that $S_\theta=\frac{\theta}{32\pi^2}\int d^4x\,\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$. No metric has entered. The other common identification, $a=\phi\,dt-A\cdot dx$, reverses $F$ and leaves $F\wedge F$ unchanged; this is the sense in which [[courses/generalized-symmetries-course/conventions|conventions]] §10 calls the result signature-independent. The sign of the $E\cdot B$ term does depend on the orientation, and reversing the orientation reverses θ (F1). Since $E\cdot B$ is odd under parity ($E\to-E$, $B\to B$) and under time reversal ($E\to E$, $B\to-B$), both send $\theta\to-\theta$. (Both identifications checked symbolically.)

### 3.2 A total derivative, and the Euclidean weight [Computed.]

Locally $F\wedge F=d(a\wedge da)$, since $d(a\wedge da)=da\wedge da-a\wedge d^2a$. For constant θ the term therefore drops out of the equations of motion. Its content is global, in the integer of §3.3, and becomes local only where $\nabla\cdot B\neq0$ or where θ varies (§§4.3, 8).

Continue to Euclidean time $\tau=it$. A 1-form is continued as a form, $a_t\,dt=a_\tau\,d\tau$, so that $a_\tau=-i\,a_t$ with $a_\tau$ real, and $\partial_t=i\partial_\tau$. Then $F_{ti}=\partial_ta_i-\partial_ia_t=iF_{\tau i}$, and since every term of the coefficient of $dt\wedge dx^1\wedge dx^2\wedge dx^3$ contains exactly one time index,
$$
(F\wedge F)_{t123}\,dt=i\,(F\wedge F)_{\tau123}\,(-i\,d\tau)=(F\wedge F)_{\tau123}\,d\tau .
$$
The integral of $F\wedge F$ is therefore the same integral in Euclidean variables with the orientation $d\tau\wedge dx^1\wedge dx^2\wedge dx^3$, and the Minkowski weight becomes
$$
e^{iS_\theta}\ \longrightarrow\ e^{i\theta Q},\qquad Q=\frac1{8\pi^2}\int F\wedge F,\qquad\text{that is,}\quad S_E\supset-i\theta Q ,
$$
while the Maxwell weight $\exp\big[\frac{i}{2e^2}\int dt\,d^3x\,(E^2-B^2)\big]$ becomes $\exp\big[-\frac1{2e^2}\int d\tau\,d^3x\,(F_{\tau i}F_{\tau i}+B^2)\big]$, the Euclidean action of [[courses/generalized-symmetries-course/conventions|conventions]] §4 (both continuations checked symbolically). The θ-term keeps its factor $i$. It is a phase, so the Euclidean weight is not positive for any $\theta\notin2\pi\mathbb{Z}$: for $\theta\neq0,\pi$ it is complex, and at $\theta=\pi$ it is the real but indefinite sign $(-1)^Q$ ($Q\in\mathbb{Z}$ on $T^4$, §3.3). This is the sign problem of lattice simulations at nonzero θ; for bosonic matter Sulejmanpasic and Gattringer remove it by a worldline–worldsheet dualization [Stated — refs: Sulejmanpasic–Gattringer].

### 3.3 Integrality [Model proof on $T^4$.]

On a closed oriented 4-manifold $X$ the form $c_1=F/2\pi$ has integer periods (Dirac quantization, [[courses/generalized-symmetries-course/conventions|conventions]] §5), and $Q=\frac12\int_Xc_1\wedge c_1$.

**Claim.** On $T^4$, $Q\in\mathbb{Z}$ for every $U(1)$ gauge field.

**Proof.** Let $L_\mu$ be the periods of $T^4$ and $2\pi k_{\mu\nu}$, with $k_{\mu\nu}\in\mathbb{Z}$, the fluxes through the six 2-tori. The constant field strength $F_0=\sum_{\mu<\nu}\frac{2\pi k_{\mu\nu}}{L_\mu L_\nu}\,dx^\mu\wedge dx^\nu$ has these fluxes, and every gauge field with the same fluxes differs from a connection of curvature $F_0$ by a global 1-form α, $F=F_0+d\alpha$. Under this change $F\wedge F$ changes by $2\,d\alpha\wedge F_0+d\alpha\wedge d\alpha=d\big(2\alpha\wedge F_0+\alpha\wedge d\alpha\big)$, an exact form, so $Q$ equals its value on $F_0$. There, each complementary pair of planes appears in two orders, and the shuffle signs are $\epsilon(1234)=\epsilon(1423)=+1$ and $\epsilon(1324)=-1$, so
$$
F_0\wedge F_0=2\big(F_{12}F_{34}-F_{13}F_{24}+F_{14}F_{23}\big)\,dx^1\wedge dx^2\wedge dx^3\wedge dx^4,\qquad
Q=\frac{2\cdot4\pi^2}{8\pi^2}\big(k_{12}k_{34}-k_{13}k_{24}+k_{14}k_{23}\big)\in\mathbb{Z}.\qquad\square
$$
The factor 2 of the two orders cancels the ½: $\int c_1\wedge c_1$ is even on $T^4$. More generally $\int c_1\wedge c_1$ is even on every closed spin 4-manifold, by Wu's formula, and odd for some bundle on a non-spin one: on $\mathbb{CP}^2$ the bundle whose $c_1$ is the hyperplane class has $\int c_1\wedge c_1=1$, so $Q=\frac12$ [Stated — refs: Wu's formula; its role in abelian duality on four-manifolds is analysed in Witten, *Selecta Math.* 1 (1995) 383, arXiv:hep-th/9505186]. Therefore $Q\in\frac12\mathbb{Z}$ in general, and $e^{i\theta Q}$ is $2\pi$-periodic in θ on spin manifolds, among them $T^4$ and the lattice of §6 (F5).

## 4. The Witten effect

### 4.1 The θ-modified momentum and Gauss's law [Computed.]

Consider Maxwell theory with the θ-term and matter of integer charges, with charge density ρ and current $J$, in the normalization of §3.1,
$$
L=\int d^3x\,\Big[\frac1{2e^2}\big(E^2-B^2\big)-\frac\theta{4\pi^2}\,E\cdot B-\rho\,\phi+J\cdot A\Big],\qquad E=-\nabla\phi-\dot A,\quad B=\nabla\times A .
$$
Only $E$ contains a time derivative, through $-\dot A$, so the momentum conjugate to $A$ is
$$
\Pi=\frac{\partial\mathcal L}{\partial\dot A}=-\frac{E}{e^2}+\frac{\theta}{4\pi^2}\,B ,
$$
and the θ-term has moved the canonical momentum away from the electric field. The scalar potential appears without time derivative, and its equation is a constraint. Varying φ, $\delta\mathcal L=\big(\frac{E}{e^2}-\frac{\theta B}{4\pi^2}\big)\cdot(-\nabla\delta\phi)-\rho\,\delta\phi$, and after an integration by parts whose surface term vanishes for $\delta\phi$ of compact support,
$$
\nabla\cdot\Big(\frac{E}{e^2}-\frac{\theta}{4\pi^2}\,B\Big)=\rho,\qquad\text{that is,}\qquad-\nabla\cdot\Pi=\rho ,
$$
the Gauss law of [[courses/generalized-symmetries-course/conventions|conventions]] §10. The Hamiltonian says the same. From $\Pi\cdot\dot A=-\Pi\cdot E-\Pi\cdot\nabla\phi$ and $-\Pi\cdot E=E^2/e^2-\frac\theta{4\pi^2}E\cdot B$,
$$
H=\int d^3x\,\Big[\frac{E^2+B^2}{2e^2}+\phi\,\big(\nabla\cdot\Pi+\rho\big)-J\cdot A\Big],\qquad E=-e^2\Big(\Pi-\frac{\theta}{4\pi^2}B\Big),
$$
where a surface term in $\phi\,\Pi$ was dropped: the energy is the Maxwell energy, φ multiplies the Gauss constraint, and θ enters only through the relation between the canonical momentum and the physical field. Now integrate the Gauss law over a ball $V$ that contains a monopole, $\oint_{\partial V}B\cdot dS=2\pi n_m$, and matter of total charge $N=\int_V\rho$. Both terms become surface integrals over $\partial V$,
$$
\oint_{\partial V}\frac{E}{e^2}\cdot dS-\frac{\theta}{4\pi^2}\oint_{\partial V}B\cdot dS=N,\qquad\text{so}\qquad q_e\equiv\oint_{\partial V}\frac{E}{e^2}\cdot dS=N+\frac{\theta}{2\pi}\,n_m ,
$$
where $q_e$ is the electric charge seen from outside, in units of the Wilson-line charge; the monopole enters only through its flux. With $N=n_e\in\mathbb{Z}$, proved next,
$$
\boxed{\ q_e=n_e+\frac{\theta}{2\pi}\,n_m,\qquad n_e,\,n_m\in\mathbb{Z}.\ }
$$
(The constraint and the momentum were checked symbolically from the Euler–Lagrange equations of $L$.)

### 4.2 Why $n_e$ is an integer [Proved.]

The integer is the charge that generates gauge transformations. With $[A_i(x),\Pi_j(y)]=i\,\delta_{ij}\delta^3(x-y)$ and matter fields $\psi_j$ of integer charges $q_j$, so that $[\rho(x),\psi_j(y)]=-q_j\,\delta^3(x-y)\,\psi_j(y)$, the operator
$$
U[\lambda]=\exp\Big(i\int d^3x\,\big[\Pi\cdot\nabla\lambda-\lambda\,\rho\big]\Big)
$$
implements the gauge transformation $A\to A+\nabla\lambda$, $\psi_j\to e^{iq_j\lambda}\psi_j$. Integrating by parts,
$$
U[\lambda]=\exp\Big(i\oint_{S^2_\infty}\lambda\,\Pi\cdot dS-i\int d^3x\,\lambda\,(\nabla\cdot\Pi+\rho)\Big)=\exp\Big(i\oint_{S^2_\infty}\lambda\,\Pi\cdot dS\Big)\qquad\text{on physical states},
$$
by Gauss's law. Transformations with $\lambda\to0$ at infinity act as the identity: they are the redundancies. For λ tending to a constant $\lambda_0$, $U=e^{-i\lambda_0\hat N}$ with
$$
\hat N\equiv-\oint_{S^2_\infty}\Pi\cdot dS=\oint_{S^2_\infty}\Big(\frac{E}{e^2}-\frac{\theta}{4\pi^2}\,B\Big)\cdot dS .
$$
Take $\lambda\equiv2\pi$ everywhere. It leaves $A$ unchanged and multiplies every matter field by $e^{2\pi iq_j}=1$, since the charges are integers. That is the compactness of the gauge group, the same condition that makes the Wilson lines of integer charge the only gauge-invariant ones ([[week-08-dual-variables-abelian-gauge|Week 8]] §2.2). So $e^{-2\pi i\hat N}=1$, the eigenvalues of $\hat N$ are integers $n_e$, and §4.1 gives $q_e=n_e+\theta n_m/2\pi$. $\square$

For a point-like Dirac monopole in pure Maxwell theory $n_e$ is the charge of the matter bound to it, and the bare monopole carries $q_e=\theta/2\pi$. When the monopole has an internal collective coordinate, as in the Georgi–Glashow model of Witten's paper, the angular momentum of that coordinate supplies every $n_e$ (Problem 4⋆).

> **Physical picture.** At $\theta=\pi$ a unit monopole carries electric charge ½: a probe charge far away feels the Coulomb field of half a unit charge, and a Wilson loop of charge 1 carried around the monopole's worldline picks up the corresponding phase. Charge quantization survives as the integrality of the generator $\hat N$ of gauge rotations. The θ-term shifts the relation between that generator and the flux of $E$, by $\theta/2\pi$ per unit of magnetic flux. The statement is exact, since it uses only Gauss's law and compactness, and independent of the dynamics, which is why the lattice reproduces it configuration by configuration in §6.4.

### 4.3 The Lagrangian reading, with its surface terms [Computed.]

The same charge appears directly in the Lagrangian. Writing $E\cdot B=-\nabla\phi\cdot B-\dot A\cdot B$ and $-\nabla\phi\cdot B=-\nabla\cdot(\phi B)+\phi\,\nabla\cdot B$,
$$
-\frac\theta{4\pi^2}\int d^3x\,E\cdot B=\frac\theta{4\pi^2}\int d^3x\,\dot A\cdot B+\frac{\theta}{4\pi^2}\oint_{S^2_\infty}\phi\,B\cdot dS-\frac{\theta}{4\pi^2}\int d^3x\,\phi\,\nabla\cdot B .
$$
For a monopole at the origin, $\nabla\cdot B=2\pi n_m\,\delta^3(x)$ (the Dirac string carries no physical $B$), and the last term is $-\frac{\theta n_m}{2\pi}\,\phi(0)$: the θ-term couples the monopole to the scalar potential exactly as the term $-\rho\phi$ couples a point charge $\theta n_m/2\pi$. The surface term at infinity is $+\frac{\theta n_m}{2\pi}\phi_\infty$ when $\phi\to\phi_\infty$, and together the two give $-\frac{\theta n_m}{2\pi}\big[\phi(0)-\phi_\infty\big]$, invariant under a constant shift of φ; without the surface term that invariance would be lost. The first term vanishes for static fields. Thus the total derivative of §3.2 is total only where $\nabla\cdot B=0$, and at a monopole it leaves behind the Witten charge, with the sign of §4.1.

## 5. Spectral flow and the charge lattice [Proved.]

Label the dyons by $(n_e,n_m)\in\mathbb{Z}^2$, with charges $(q_e,q_m)=(n_e+\theta n_m/2\pi,\ n_m)$ and magnetic flux $2\pi q_m$. At $\theta+2\pi$,
$$
q_e(n_e,n_m;\theta+2\pi)=n_e+n_m+\frac{\theta}{2\pi}\,n_m=q_e(n_e+n_m,n_m;\theta),
$$
so the set of charges at $\theta+2\pi$ is the set at θ, and the labels are related by
$$
T:\ (n_e,n_m)\longmapsto(n_e+n_m,\,n_m),\qquad M_T=\begin{pmatrix}1&1\\0&1\end{pmatrix},
$$
acting on the column $(n_e,n_m)^{\rm T}$. As θ increases from 0 to $2\pi$, the row $n_m$ of the charge lattice slides by $n_m$ units (Figure 1): the state labelled $(0,1)$ moves from $q_e=0$ to $q_e=1$, where $(1,1)$ sat at $\theta=0$, while the lattice as a whole returns to itself. This spectral flow is the precise content of $\theta\sim\theta+2\pi$. The weight is periodic when $Q\in\mathbb{Z}$ (§3.3), the lattice of charges is periodic up to $T$, and individual states are permuted.

```
          q_e :   -3/2   -1   -1/2    0    1/2    1    3/2    2    5/2

θ = 0    n_m = +1         D           M           ·           ·
         n_m =  0         ·           o           E           ·
         n_m = -1         ·           ·           ·           ·

θ = π    n_m = +1   ·           D           M           ·           ·
         n_m =  0         ·           o           E           ·
         n_m = -1   ·           ·           ·           ·           ·

θ = 2π   n_m = +1         ·           D           M           ·
         n_m =  0         ·           o           E           ·
         n_m = -1         ·           ·           ·           ·

   M : the state labelled (0,1)     D : the state labelled (−1,1)
   E : the unit charge (1,0)        o : the vacuum (0,0)
```
**Figure 1. The charge lattice sheared by θ: the row $n_m$ slides by $\theta n_m/2\pi$. At $\theta=2\pi$ the set of points is that of $\theta=0$, but $M$ now sits where $(1,1)$ was and $D$ where $M$ was (spectral flow).**

The pairing that Dirac quantization constrains is insensitive to the shear. For $v=(n_e,n_m)$ and $w=(n_e',n_m')$ define
$$
\langle v,w\rangle\equiv q_e\,q_m'-q_m\,q_e'=n_e\,n_m'-n_m\,n_e',
$$
where the θ-dependent parts $\frac{\theta}{2\pi}(n_mn_m'-n_mn_m')$ cancel. It is an integer at every θ, and $T$ preserves it since $\det M_T=1$. That this antisymmetric combination is the one that must be an integer, the Dirac–Schwinger–Zwanziger condition, follows from the argument of Week 8 §2.2 [Heuristic.]: when $w$ is carried around $v$, its electric charge circles the magnetic flux $2\pi q_m$ of $v$ and picks up $e^{2\pi iq_e'q_m}$, while its magnetic charge circles the electric flux of $v$, which by electric–magnetic duality contributes the opposite phase $e^{-2\pi iq_m'q_e}$; the product is $e^{-2\pi i\langle v,w\rangle}$. The fractional part of $q_e$ is never what is quantized: for two unit monopoles at θ, $q_eq_m'=\theta/2\pi$, while $\langle v,w\rangle=0$.

## 6. The θ-term on the lattice

Consider the periodic hypercubic lattice of $L^4$ sites, the torus $T^4$, with the Villain gauge theory of [[courses/generalized-symmetries-course/conventions|conventions]] §4 and the weight $e^{i\theta Q_{\rm lat}}$. We read the lattice axes $(1,2,3,4)$ as $(\tau,x^1,x^2,x^3)$, so that the hypercube orientation of [[courses/generalized-symmetries-course/conventions|conventions]] §1 is the Euclidean orientation $d\tau\wedge dx^1\wedge dx^2\wedge dx^3$ of §3.2 (F1 says what changes when time is the fourth axis, as in the pictures of Week 8). The question is which lattice $Q_{\rm lat}$ makes the weight $2\pi$-periodic.

### 6.1 The naive density fails [Proved.]

For smooth fields $\sin\theta_P\simeq F_P$ at unit lattice spacing, where $\theta_P=(da)_P$ is the plaquette angle, and the naive topological density is
$$
q_{\rm naive}(x)=\frac1{32\pi^2}\sum_{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma}\,\sin\theta_{\mu\nu}(x)\,\sin\theta_{\rho\sigma}(x),\qquad Q_{\rm naive}=\sum_xq_{\rm naive}(x),
$$
where $\sin\theta_{\nu\mu}=-\sin\theta_{\mu\nu}$. It is built from sines because $F\wedge F$ is odd under $P$ and $T$, while $\cos\theta_P$ is even under $\theta_P\to-\theta_P$, so no density built from cosines alone can represent it.

**Claim.** $Q_{\rm naive}$ is not integer-valued, so $e^{i\theta Q_{\rm naive}}$ is not $2\pi$-periodic in θ.

**Proof.** $Q_{\rm naive}$ is a continuous function of the link angles on the connected torus $U(1)^{N_\ell}$ (the sines are $2\pi$-periodic, so the branch of $\theta_P$ is irrelevant). It vanishes at $a=0$ and is not identically zero, as the example below shows, and a continuous integer-valued function on a connected space is constant. $\square$

[Computed.] On the $4^4$ torus put one unit of flux, uniformly, through the (1,2) and the (3,4) tori: $a_2(x)=2\pi x_1/L^2$, together with $a_1(x)=-2\pi x_2/L$ on the links with $x_1=L-1$, and the same in the (3,4) directions. Then $\theta_{12}=\theta_{34}=2\pi/L^2$ on every plaquette of those orientations (after reduction to $(-\pi,\pi]$ at one corner plaquette per torus), the other plaquette angles vanish, and each site has 8 nonzero terms $\sin\theta_{12}\sin\theta_{34}$, so
$$
Q_{\rm naive}=\frac{8L^4}{32\pi^2}\,\sin^2\frac{2\pi}{L^2}=\frac{L^4}{4\pi^2}\,\sin^2\frac{2\pi}{L^2}=\frac{64}{\pi^2}\,\sin^2\frac{\pi}{8}=0.9496\qquad(L=4),
$$
which tends to 1 only as $L\to\infty$. The continuum value, and the Villain value of §6.3 for the same configuration, is exactly 1. The deviation is a lattice artefact for smooth fields, but it enters the weight of every configuration of the path integral, and rough configurations are not suppressed at finite coupling.

### 6.2 The Villain θ-term [Computed.]

With the Villain field strength $F=da-2\pi n$ and the cubical cup product of [[courses/generalized-symmetries-course/conventions|conventions]] §8, define
$$
Q_{\rm lat}=\frac1{8\pi^2}\sum_x(F\cup F)\big(x;\{1,2,3,4\}\big).
$$
For a constant 2-cochain the rule gives $(F\cup F)(x;1234)=\sum_{|A|=2}\epsilon(A,A^c)\,F_A\,F_{A^c}=2(F_{12}F_{34}-F_{13}F_{24}+F_{14}F_{23})$, the continuum density of §3.3, so $Q_{\rm lat}$ discretizes $Q$ with the two factors on complementary faces at opposite corners of each hypercube. Expanding,
$$
F\cup F=da\cup da-2\pi\,(da\cup n+n\cup da)+4\pi^2\,n\cup n ,
$$
and the Leibniz rule $d(\alpha\cup\beta)=d\alpha\cup\beta+(-1)^p\alpha\cup d\beta$ of [[courses/generalized-symmetries-course/conventions|conventions]] §8, with $p=1$ and $p=2$, gives
$$
da\cup da=d(a\cup da),\qquad da\cup n=d(a\cup n)+a\cup dn,\qquad n\cup da=d(n\cup a)-dn\cup a .
$$
The sum of a coboundary over the closed torus vanishes, since every cube is a face of two hypercubes with opposite orientations. With $m=dn$, the monopole number of [[courses/generalized-symmetries-course/conventions|conventions]] §4, therefore
$$
\boxed{\ Q_{\rm lat}=\frac12\sum n\cup n-\frac1{4\pi}\sum\big(a\cup m-m\cup a\big),\qquad m=dn .\ }
$$
(On the $3^4$ torus, with random real $a$ and random integer $n$, the two sides agree to $10^{-14}$.) $Q_{\rm lat}$ is invariant under both redundancies of the Villain form, since $F$ is (F6 shows how the two terms trade under a branch shift), and when $m=0$ the real field $a$ drops out.

### 6.3 Integrality without monopoles [Model proof on $T^4$.]

**Claim.** If $dn=0$, then for every real $a$
$$
Q_{\rm lat}=w_{12}w_{34}-w_{13}w_{24}+w_{14}w_{23}\in\mathbb{Z},
$$
where $w_{\mu\nu}=\sum_{P\in T^2_{\mu\nu}}n_P$ is the period of $n$ on any $(\mu\nu)$ 2-torus.

**Proof.** (i) Let $M^{(\mu\nu)}\in C^2(\Lambda,\mathbb{Z})$ be 1 on the $(\mu\nu)$ plaquettes based at the sites with $x_\mu=x_\nu=0$ and 0 elsewhere. It is closed, and its period is 1 on the $(\mu\nu)$ 2-tori and 0 on the others. As in Week 8 §5.1, there on $\Lambda^*$, $n-\sum w_{\mu\nu}M^{(\mu\nu)}$ is closed with zero periods, so it equals $dk$ with $k\in C^1(\Lambda,\mathbb{Z})$, since $H^2(T^4,\mathbb{Z})$ has no torsion. (ii) With $n_h=\sum w_{\mu\nu}M^{(\mu\nu)}$ and $dn_h=0$, Leibniz gives $dk\cup n_h=d(k\cup n_h)$, $n_h\cup dk=d(n_h\cup k)$ and $dk\cup dk=d(k\cup dk)$, so $\sum n\cup n=\sum n_h\cup n_h$. (iii) On the hypercube $(x;\{1,2,3,4\})$ the split $A=\{\mu,\nu\}$ of $M^{(\mu\nu)}\cup M^{(\rho\sigma)}$ evaluates $M^{(\mu\nu)}$ at $x$, which requires $x_\mu=x_\nu=0$, and $M^{(\rho\sigma)}$ at $x+\hat\mu+\hat\nu$, whose ρ and σ coordinates are those of $x$, which requires $x_\rho=x_\sigma=0$. Only complementary pairs contribute, each on the single hypercube at $x=0$ and with its shuffle sign,
$$
\sum M^{(12)}\cup M^{(34)}=\sum M^{(34)}\cup M^{(12)}=1,\qquad\sum M^{(13)}\cup M^{(24)}=\sum M^{(24)}\cup M^{(13)}=-1,\qquad\sum M^{(14)}\cup M^{(23)}=\sum M^{(23)}\cup M^{(14)}=1,
$$
so $\sum n\cup n=2\big(w_{12}w_{34}-w_{13}w_{24}+w_{14}w_{23}\big)$, and with $m=0$ the boxed formula of §6.2 is $Q_{\rm lat}=\frac12\sum n\cup n$. $\square$

(Checked on the $3^4$ torus with random $w$, random integer $k$ and random real $a$; for instance $w=(-2,-2,-3,2,3,-1)$ in the order (12, 13, 14, 23, 24, 34) gives $Q_{\rm lat}=2.000000000000$, and the six sums above come out as displayed.) By Week 8 §2.2 the magnetic flux through a $(\mu\nu)$ 2-torus is $\Phi_{\mu\nu}=-2\pi w_{\mu\nu}$, so $Q_{\rm lat}=\frac1{4\pi^2}(\Phi_{12}\Phi_{34}-\Phi_{13}\Phi_{24}+\Phi_{14}\Phi_{23})$ is the continuum $Q$ of §3.3, exactly and at every lattice spacing. For the uniform-flux configuration of §6.1 the Villain integer is $n=-1$ on one corner plaquette of each (1,2) and (3,4) torus, $w_{12}=w_{34}=-1$, and $Q_{\rm lat}=1$ against $Q_{\rm naive}=0.9496$.

Therefore, in the **monopole-free** theory, where the Villain sum runs over closed $n$ only (the theory that appeared as the dual of Week 8 §6, with $d\tilde n=0$, and the modified Villain theory of [[courses/generalized-symmetries-course/conventions|conventions]] §4), $e^{i\theta Q_{\rm lat}}$ is $2\pi$-periodic configuration by configuration, independent of $a$, and a topological invariant of the flux sector. Sulejmanpasic and Gattringer give a construction of the four-dimensional lattice θ-term in their Villain-type formulation and demonstrate the Witten effect for magnetic matter [Stated — refs: Sulejmanpasic–Gattringer]; the cochain derivation of this section is the course's own.

### 6.4 Monopoles and the lattice Witten effect [Computed.]

When $m\neq0$ the second term of the boxed formula is a linear function of $a$. Its coefficients follow from the cup product. On the hypercube at $x$, $a\cup m$ contains $\epsilon(\mu,\mu^c)\,a_\mu(x)\,m_{\mu^c}(x+\hat\mu)$ and $m\cup a$ contains $\epsilon(\mu^c,\mu)\,m_{\mu^c}(x)\,a_\mu(x+\hat e_{\mu^c})$, with $\epsilon(\mu^c,\mu)=-\epsilon(\mu,\mu^c)$, where $\mu^c$ denotes the three other directions and $\hat e_{\mu^c}$ the sum of their unit vectors. Collecting the terms in each link,
$$
\sum\big(a\cup m-m\cup a\big)=\sum_{y,\mu}\epsilon(\mu,\mu^c)\,a_\mu(y)\,\big[m_{\mu^c}(y+\hat\mu)+m_{\mu^c}(y-\hat e_{\mu^c})\big],
$$
so the link $\ell_\mu(y)$ couples to two cubes of the complementary type: the one based at its head and the one whose far corner is its tail (checked link by link on the $3^4$ torus).

[Computed.] On the $3^4$ torus put $n=1$ on the plaquettes $(x;\{3,4\})$ at the spatial position $(x^1,x^2,x^3)=(1,0,0)$, for every τ. Its coboundary is $m_{234}=+1$ on the spatial cubes based at $(0,0,0)$ and $m_{234}=-1$ on those based at $(1,0,0)$, at every τ: a static monopole–antimonopole pair joined by a one-plaquette Dirac string. The flux of $F$ out of a cube is $-2\pi m$ ([[courses/generalized-symmetries-course/conventions|conventions]] §4), and with the axes (2,3,4) read as $(x^1,x^2,x^3)$ it is $\oint B\cdot dS$, so the cube at $(1,0,0)$ holds $n_m=+1$. Put $a_\tau=\alpha$ on the time links at the two corners of that cube, $y=(1,0,0)$ and $y+(1,1,1)=(2,1,1)$, for every τ, and $a=0$ elsewhere (Figure 2). Here $\sum n\cup n=0$, since it needs plaquettes of complementary orientations, and $\epsilon(\tau,\tau^c)=+1$. Each column of time links contributes $-L\alpha$ to $\sum(a\cup m-m\cup a)$, the first through the cube based at the head of each link and the second through the cube whose far corner is its tail, so
$$
Q_{\rm lat}=-\frac1{4\pi}\,(-2L\alpha)=\frac{L\alpha}{2\pi},\qquad e^{i\theta Q_{\rm lat}}=\exp\Big(i\,\frac{\theta}{2\pi}\oint a\Big),\qquad\oint a=L\alpha ,
$$
where $\oint a$ is the holonomy around the time circle at the monopole, averaged over the two corners. (With $\alpha=0.7$: $Q_{\rm lat}=0.3342$; one column alone gives half, and the same columns at the antimonopole's corners give $-0.3342$.) The θ-term has attached to the worldline of the monopole the Wilson line $W_q$ of [[courses/generalized-symmetries-course/conventions|conventions]] §6 with $q=\theta n_m/2\pi$. This is the Witten effect of §4, derived on the lattice, with the same sign.

```
     τ ↑
       │     a_τ = α                                  a_τ = α
       │       ║                                        ║
       │       ║      ┌──────────────────────────┐      ║
       │       ║      │  spatial cube c           │      ║
       │       ║      │  m₂₃₄ = −1 ,  n_m = +1    │      ║
       │       ●      └──────────────────────────┘      ●
       │   y = (1,0,0)                          y + (1,1,1) = (2,1,1)
       │   base corner of c                     far corner of c
       └───────────────────────────────────────────────────────→ (x¹, x², x³)

       column at y           : a ∪ m, each link against c one step later in τ
       column at y + (1,1,1) : m ∪ a, each link against c at the same τ
```
**Figure 2. The lattice Witten effect. The time links at the base and far corners of a monopole's cube couple to it through $a\cup m$ and $m\cup a$; with $a_\tau=\alpha$ on both columns the θ-term is $e^{i(\theta/2\pi)L\alpha}$, a Wilson line of charge $\theta n_m/2\pi$ along the monopole's worldline.**

Three consequences follow. First, $Q_{\rm lat}$ is not an integer, and the plain Villain weight $e^{i\theta Q_{\rm lat}}$ is not $2\pi$-periodic in θ. Second, the shift $\theta\to\theta+2\pi$ multiplies the weight by $e^{2\pi iQ_{\rm lat}}$, which here is $e^{i\oint a}$, a unit Wilson line on the monopole: the flow $(0,1)\to(1,1)$ of §5 made literal. In a theory with dynamical unit charges that factor could be absorbed in a relabelling; in the plain Villain theory, which has no electric matter, θ and $\theta+2\pi$ define different lattice theories [Heuristic.]. Third, the failure is generic [Proved. for odd $L$]. If $Q_{\rm lat}$ is independent of $a$ at fixed $n$, every coefficient above vanishes, so that $J_\mu(z)\equiv\epsilon(\mu,\mu^c)\,m_{\mu^c}(z)$ obeys $J_\mu(z)=-J_\mu(z-\hat v)$ with $\hat v=(1,1,1,1)$; applying this $L$ times gives $J_\mu=(-1)^LJ_\mu$, and for odd $L$ we need $m=0$. On an odd torus, therefore, $Q_{\rm lat}$ is integer-valued for all $a$ if and only if $dn=0$. (On even tori, closed monopole configurations antiperiodic under $\hat v$ make the linear term vanish; the example above works for every $L\geq3$.)

## 7. SL(2,ℤ) and oblique confinement

Pure compact QED has monopoles and no electric matter, and its dyons are the monopoles of §4 with $n_e=0$. In a model where both kinds of matter are dynamical, the Villain model of Week 8 Problem 6⋆⋆ with a θ-term or the $\mathbb{Z}_p$ models of Cardy and Rabinovici, every $(n_e,n_m)$ is a particle whose loops can proliferate. This section asks which of them condense and what they confine.

### 7.1 The duality group and the dyon self-energy

Define the complex coupling
$$
\tau=\frac{\theta}{2\pi}+\frac{2\pi i}{e^2}.
$$
The shift $T:\tau\to\tau+1$ acts on labels as in §5. At $\theta=0$ the duality of Week 8 §6 maps $e\to\tilde e=2\pi/e$, that is $\tau=2\pi i/e^2\to2\pi i/\tilde e^2=ie^2/2\pi=-1/\tau$, and exchanges electric and magnetic charges; we write it as $S:\tau\to-1/\tau$ with $(n_e,n_m)\mapsto(-n_m,n_e)$, whose square is charge conjugation. Both label maps have determinant one, preserve $\langle\cdot,\cdot\rangle$, and generate $SL(2,\mathbb{Z})$. Cardy constructed the phase diagrams of abelian lattice gauge theories with θ from duality arguments of this kind [Stated — refs: Cardy].

The self-energy of a dyon loop follows from the numbers of Week 8 [Heuristic.]. A monopole loop costs $2\pi^2G_4(0)\beta=2\pi^2G_4(0)/e^2$ per link (Week 8 §5.5), and by the duality of Week 8 §6 an electric loop costs $2\pi^2G_4(0)\tilde\beta=G_4(0)e^2/2$. For a dyon the Witten effect replaces $n_e$ by $q_e$, and dropping the cross term between its electric and magnetic parts, which for a single loop is topological, the cost per link is
$$
\varepsilon(n_e,n_m)=G_4(0)\Big[\frac{e^2q_e^2}{2}+\frac{2\pi^2n_m^2}{e^2}\Big]=\frac{\pi G_4(0)}{{\rm Im}\,\tau}\,\big|n_e+n_m\tau\big|^2,
$$
where $|n_e+n_m\tau|^2=(n_e+\theta n_m/2\pi)^2+(2\pi n_m/e^2)^2$ and $\pi/{\rm Im}\,\tau=e^2/2$. The same combination is the field energy of a static dyon outside a sphere (Problem 1). It is invariant under $SL(2,\mathbb{Z})$ acting on τ and on the labels together [Proved.]: under $T$ the relabelling absorbs $\tau\to\tau+1$, and under $S$, ${\rm Im}(-1/\tau)={\rm Im}\,\tau/|\tau|^2$ and $|n_e-n_m/\tau|^2=|{-n_m}+n_e\tau|^2/|\tau|^2$, so that $\varepsilon(n_e,n_m)$ at $-1/\tau$ equals $\varepsilon(-n_m,n_e)$ at τ.

### 7.2 Which probes a condensate confines [Heuristic.]

Suppose the loops of a primitive charge $w=(p,q)$ proliferate, so that a field Φ of charge $w$ has $\langle\Phi\rangle\neq0$. Consider a static probe of charge $v$. A quantum of Φ carried around a closed path far from the probe picks up the Aharonov–Bohm phase of §5 from the part of the probe's flux that the path encloses, and a single-valued Φ with $|\Phi|\neq0$ tolerates only fluxes that give it integer windings. The flux is therefore collimated into vortex tubes of the condensate, around each of which the phase of Φ winds by $2\pi$, and the total winding around the probe is $\langle v,w\rangle$ up to orientation. Thus:

- if $\langle v,w\rangle\neq0$, then $|\langle v,w\rangle|$ vortex strings of the condensate end on the probe, and a probe–antiprobe pair is bound by a linear potential: the probe is **confined**;
- if $\langle v,w\rangle=0$, that is, $v$ is a multiple of $w$, no string ends on the probe, which the condensate **screens**.

Two checks. The dual superconductor of [[week-11-monopole-condensation-4d|Week 11]], $w=(0,1)$, confines the charge $(1,0)$ with $\langle(1,0),(0,1)\rangle=1$ string. An ordinary superconductor, $w=(2,0)$, attaches $|\langle(0,1),(2,0)\rangle|=2$ vortices to a Dirac monopole, each carrying the flux π, half a Dirac quantum, because the condensate has charge 2.

### 7.3 Worked example: the dyon $(-1,1)$ and the crossing at $\theta=\pi$ [Heuristic.]

Take the coupling strong enough that a magnetic dyon condenses (below the arc $|\tau|=1$ of Figure 3 at $\theta=0$). The example assumes, as the Cardy–Rabinovici models of §7.4 do, that dyons of every label are dynamical. In pure compact QED₄ the only dynamical magnetic objects are the monopoles, of label $(0,1)$ and electric charge $\theta/2\pi$; a $(-1,1)$ excitation needs a dynamical unit charge bound to a monopole, so the switch at $\theta=\pi$ below describes theories with electric matter, and without it θ is not $2\pi$-periodic (§6.4; [[courses/generalized-symmetries-course/conventions|conventions]] §10). Among dyons with $n_m=1$, $\varepsilon$ is smallest for the $n_e$ that minimizes $|q_e|=|n_e+\theta/2\pi|$: $n_e=0$ for $-\pi<\theta<\pi$ and $n_e=-1$ for $\pi<\theta<3\pi$. At $\theta=\pi$ the two, $(0,1)$ with $q_e=\frac12$ and $(-1,1)$ with $q_e=-\frac12$, tie, and CP exchanges them. In fact CP reverses $q_e$, keeps $q_m$ and sends $\theta\to-\theta$, so it maps the label $(n_e,n_m)$ at θ to $(-n_e,n_m)$ at $-\theta$. At $\theta=\pi$ the relabelling of §5 from $-\pi$ to π turns this into a symmetry of the $\theta=\pi$ theory,
$$
{\rm CP}_{\theta=\pi}:\ (n_e,n_m)\longmapsto(-n_e-n_m,\ n_m),
$$
which exchanges $(0,1)$ and $(-1,1)$. The pairings of §7.2 then decide every probe:

| probe $v$ | $q_e$ at $\theta=\pi$ | $\langle v,(0,1)\rangle$ | fate for $-\pi<\theta<\pi$ | $\langle v,(-1,1)\rangle$ | fate for $\pi<\theta<3\pi$ |
|---|---|---|---|---|---|
| $(1,0)$ | $1$ | $1$ | confined, 1 string | $1$ | confined, 1 string |
| $(0,1)$ | $\frac12$ | $0$ | screened | $1$ | confined, 1 string |
| $(-1,1)$ | $-\frac12$ | $-1$ | confined, 1 string | $0$ | screened |
| $(1,1)$ | $\frac32$ | $1$ | confined, 1 string | $2$ | confined, 2 strings |

The unit charge is confined in both phases, and the phases are distinguished by the magnetic line with a perimeter law: the 't Hooft line $(0,1)$ below π, the dyonic line $(-1,1)$ above. At strong coupling the two phases meet on the line $\theta=\pi$, where both condensates have the same free energy; the two vacua coexist there and CP is spontaneously broken, the mechanism for spontaneous CP violation at $\theta=\pi$ found by Cardy [Stated — refs: Cardy]. Just above π the condensed object carries the physical charges $(q_e,q_m)=(-1+\theta/2\pi,\,1)$, electric and magnetic at once: this is oblique confinement in the sense of 't Hooft [Stated — refs: 't Hooft 1981]. At $\theta=2\pi$ its charges are $(0,1)$, and the phase is the $T$-image of ordinary confinement.

### 7.4 The phase diagram [Stated — refs: Cardy–Rabinovici; Cardy.]

The crude rule that the dyon with the smallest $\varepsilon$ condenses [Heuristic.] turns Figure 3 into a computation. Boundaries are where two dyons tie, $|n_e+n_m\tau|=|n_e'+n_m'\tau|$, arcs of circles centred on the real axis. Near each rational $\theta/2\pi=-n_e/n_m$ the dyon $(n_e,n_m)$ has $|n_e+n_m\tau|^2=n_m^2({\rm Im}\,\tau)^2$, which vanishes as ${\rm Im}\,\tau\to0$, so at strong enough coupling it wins: there are infinitely many phases, in agreement with the structure found by Cardy. At $\theta=\pi$, for instance, the charge $(1,0)$ condenses for ${\rm Im}\,\tau>\sqrt3/2$ (Higgs), the CP-broken coexistence of $(0,1)$ and $(-1,1)$ holds for $1/\sqrt{12}<{\rm Im}\,\tau<\sqrt3/2$, and below $1/\sqrt{12}=0.289$ the dyon $(-1,2)$ wins, with $4({\rm Im}\,\tau)^2<\frac14+({\rm Im}\,\tau)^2$. Its physical charges at $\theta=\pi$ are $(0,2)$, and ${\rm CP}_{\theta=\pi}$ maps $(-1,2)$ to itself, so this oblique phase is CP-invariant.

```
 Im τ
   1.20 | HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH      weak coupling
   1.05 | HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
   0.95 | MMMMMMMMMMMMMMMHHHHHHHHHHHHHHHHHHHDDDDDDDDDDDDDDD
   0.90 | MMMMMMMMMMMMMMMMMMMMMHHHHHHHDDDDDDDDDDDDDDDDDDDDD
   0.80 | MMMMMMMMMMMMMMMMMMMMMMMMDDDDDDDDDDDDDDDDDDDDDDDDD
   0.60 | MMMMMMMMMMMMMMMMMMMMMMMMDDDDDDDDDDDDDDDDDDDDDDDDD
   0.40 | MMMMMMMMMMMMMMMMMMMMMMMMDDDDDDDDDDDDDDDDDDDDDDDDD
   0.30 | MMMMMMMMMMMMMMMMMMMMMMMMDDDDDDDDDDDDDDDDDDDDDDDDD
   0.25 | MMMMMMMMMMMMMMMMMMMMMMOOOOODDDDDDDDDDDDDDDDDDDDDD
   0.20 | MMMMMMMMMMMMMMMMMMMMOOOOOOOOODDDDDDDDDDDDDDDDDDDD
   0.15 | MMMMMMMMMMMMMMMMMMOOOOOOOOOOOOODDDDDDDDDDDDDDDDDD
   0.10 | MMMMMMMMMMMMMMM+++OOOOOOOOOOOOO+++DDDDDDDDDDDDDDD      strong coupling
        +-------------------------------------------------> θ
          0                       π                      2π

   H : (1,0), Higgs        M : (0,1), confinement        D : (−1,1), oblique (T-image of M)
   O : (−1,2), oblique, CP-invariant at θ = π           + : (−1,3), (−2,3), ...
   the M|D boundary at θ = π, 0.29 < Im τ < 0.87, is a first-order line with two CP-conjugate vacua
```
**Figure 3. The lightest dyon in the $(\theta,{\rm Im}\,\tau)$ plane, ${\rm Im}\,\tau=2\pi/e^2$, computed from the self-energy of §7.1 over all coprime $(n_e,n_m)$ with $n_m\le5$; a schematic of the structure found by Cardy and Rabinovici, with boundaries fixed by the course's heuristic rule.**

In this crude model something always condenses: the minimum over $w$ of $|n_e+n_m\tau|^2/{\rm Im}\,\tau$ is at most $2/\sqrt3$, attained at $\tau=e^{i\pi/3}$, so the smallest $\varepsilon$ is at most $0.562$, below the entropy $\ln7=1.946$ per step of Week 8 Problem 4⋆. Independent core energies for the two kinds of matter separate the regions and can open phases in which nothing condenses. In the $\mathbb{Z}_p$ models of Cardy and Rabinovici the structure depends on $p$, θ and the coupling, and besides electric and magnetic condensation it contains dyonic condensation and oblique confinement [Stated — refs: Cardy–Rabinovici].

## 8. Varying θ: axion electrodynamics and the θ-wall

### 8.1 The modified Maxwell equations [Computed.]

Let θ depend on $x$ and $t$ in the Lagrangian of §4.1. The equation of φ keeps its form with θ inside the divergence, and the equation of $A$, once Faraday's law $\nabla\times E=-\partial_tB$ is used (an identity for fields built from φ and $A$), acquires the gradients of θ:
$$
\nabla\cdot\frac{E}{e^2}=\rho+\frac1{4\pi^2}\nabla\cdot(\theta B),\qquad
\nabla\times\frac{B}{e^2}-\partial_t\frac{E}{e^2}=J-\frac1{4\pi^2}\big(\dot\theta\,B+\nabla\theta\times E\big).
$$
Away from monopoles the induced charge $\frac1{4\pi^2}\nabla\theta\cdot B$ and current $-\frac1{4\pi^2}(\dot\theta B+\nabla\theta\times E)$ obey the continuity equation, and for constant θ both vanish (all checked symbolically). The bulk value of θ is invisible to the equations of motion; its gradients act as sources. These are the equations of axion electrodynamics when θ is a field with its own dynamics [Stated — refs: Wilczek], and of a medium with a magnetoelectric parameter θ(x) when θ is a background.

### 8.2 The Hall conductivity of a θ-wall [Computed.]

Consider a wall at $z=0$ across which θ jumps from 0 ($z<0$) to Δθ ($z>0$), thin compared with the scales on which $E$ and $B$ vary. Then $\nabla\theta=\Delta\theta\,\delta(z)\,\hat z$, and integrating the induced current and charge across the wall gives a surface current and a surface charge,
$$
K=-\frac{\Delta\theta}{4\pi^2}\,\hat z\times E,\qquad\text{that is,}\qquad K_x=\frac{\Delta\theta}{4\pi^2}E_y,\quad K_y=-\frac{\Delta\theta}{4\pi^2}E_x,\qquad\sigma_{\rm wall}=\frac{\Delta\theta}{4\pi^2}\,B_z .
$$
The same result follows from the action by integrating the θ-term across the wall. With $F\wedge F=d(a\wedge da)$ and $d\theta=\Delta\theta\,\delta(z)\,dz$,
$$
\frac1{8\pi^2}\int\theta\,F\wedge F=-\frac1{8\pi^2}\int d\theta\wedge a\wedge da=\frac{\Delta\theta}{8\pi^2}\int_{z=0}a\wedge da ,
$$
where the wall is oriented by $dt\wedge dx\wedge dy$, since $dz\wedge dt\wedge dx\wedge dy=-dt\wedge dx\wedge dy\wedge dz$, and the boundary terms at infinity were dropped. This is a Chern–Simons term $\frac{k}{4\pi}\int a\wedge da$ at level $k=\Delta\theta/2\pi$, whose current $j^\mu=\frac{k}{2\pi}\varepsilon^{\mu\nu\rho}\partial_\nu a_\rho$ ($\varepsilon^{txy}=+1$) gives $J_x=\frac{k}{2\pi}(\partial_ya_t-\partial_ta_y)=\frac{k}{2\pi}E_y$ with $a_t=-\phi$, and $\rho=\frac{k}{2\pi}B_z$: the same $K_x$ and $\sigma_{\rm wall}$ (both routes checked symbolically). The Hall conductivity for the current of unit charges is $\Delta\theta/4\pi^2$. The canonically normalized current is $e$ times that current and the canonical field is $E/e$, so, with $\hbar=1$ and $h=2\pi$,
$$
\boxed{\ \sigma_{xy}=\frac{\Delta\theta}{2\pi}\,\frac{e^2}{2\pi}=\frac{\Delta\theta}{2\pi}\,\frac{e^2}{h}.\ }
$$
For $\Delta\theta=\pi$, $\sigma_{xy}=e^2/4\pi$, one half of the quantum $e^2/h$. The surface charge obeys the Středa relation $\partial\sigma_{\rm wall}/\partial B_z=\Delta\theta/4\pi^2=\sigma_{xy}$, as it must for a gapped layer, since adiabatically inserting flux through a Hall layer drives charge into the region.

```
   θ(z)
    Δθ ┤                           ┌──────────────────────────
       │                           │
     0 ┼───────────────────────────┘
       └───────────────────────────┼──────────────────────────→ z
                                 z = 0
                   Chern–Simons layer, level k = Δθ/2π, oriented by dt∧dx∧dy

   in the wall (normal ẑ, θ increasing along +ẑ):

          y ↑
            │     E = E_y ŷ
            │     ↑
            │     │                K_x = + (Δθ/4π²) E_y   ⟹ ⟹ ⟹
            └─────┼──────────────────────────────→ x
                        σ_wall = (Δθ/4π²) B_z
```
**Figure 4. A θ-wall is a Hall layer: an in-plane electric field drives the transverse current $K_x=(\Delta\theta/4\pi^2)E_y$, a normal magnetic field binds the charge $(\Delta\theta/4\pi^2)B_z$, and in canonical units $\sigma_{xy}=(\Delta\theta/2\pi)(e^2/h)$.**

> **Physical picture.** An experiment on a θ-wall sees two things at once. An in-plane electric field produces a current at right angles to it, confined to the wall, with $\sigma_{xy}=(\Delta\theta/2\pi)(e^2/h)$. And each magnetic flux quantum $2\pi$ that pierces the wall binds the charge $\frac{\Delta\theta}{4\pi^2}\cdot2\pi=\Delta\theta/2\pi$, half a unit on the surface of a $\theta=\pi$ insulator. The second is the Witten effect of the wall: flux lines crossing a jump of θ carry charge exactly as a monopole in a θ-region does (§4.3, where the charge came from $\phi\,\nabla\cdot B$). Both statements are exact consequences of the θ-term; whether a given material realizes them depends on the surface being gapped, which is a statement about its microscopic electrons (§8.3).

### 8.3 Topological insulators, Weyl semimetals, and the group's line [Stated — refs.]

Time reversal sends $\theta\to-\theta$ (§3.1), and with $\theta\sim\theta+2\pi$ the only time-reversal-invariant values are 0 and π. Qi, Hughes and Zhang showed that the electromagnetic response of a three-dimensional time-reversal-invariant topological insulator is the θ-term with $\theta=\pi$ [Stated — refs: Qi–Hughes–Zhang]. Its surface is a θ-wall with $\Delta\theta=\pm\pi$, and once a time-reversal-breaking perturbation gaps the surface, choosing the sign, the surface Hall conductivity is $\pm\frac12\,e^2/h$ by §8.2. The magnetoelectric response of the bulk follows from $L_\theta=-\frac\theta{4\pi^2}E\cdot B$: the polarization $P=\partial L_\theta/\partial E=-\frac{\theta}{4\pi^2}B$ and the magnetization $M=\partial L_\theta/\partial B=-\frac{\theta}{4\pi^2}E$, in the units of the course and with its sign of θ (F1).

In a Weyl semimetal with two nodes separated by $2b$ in momentum and $2b_0$ in energy, Zyuzin and Burkov identified the axion angle $\theta(x,t)=2(b\cdot x-b_0t)$, in their conventions [Stated — refs: Zyuzin–Burkov]. By §8.1 the gradient gives the bulk anomalous Hall current $-\frac1{4\pi^2}\nabla\theta\times E=-\frac1{2\pi^2}\,b\times E$ for unit charges, a Hall conductivity $e^2|b|/2\pi^2$ per unit length: a stack of the Hall layers of §8.2, one per $\pi/|b|$. The term $\dot\theta B$ would give an equilibrium current along $B$ (the chiral magnetic effect), and Vazifeh and Franz showed, in a lattice model of the Weyl medium, that the anomalous Hall effect is present while this equilibrium current is absent, in the semimetal and in the insulator [Stated — refs: Vazifeh–Franz]. A static $b_0$ therefore cannot be read as an equilibrium response through §8.1 (Problem 7⋆⋆).

This is where the course meets the group's [[condensed-matter-connections|condensed-matter line]]. Chrispim, Bruni and Guimaraes, *Phys. Rev. B* 103 (2021) 165120 [arXiv:2012.00184], study massive photons in the presence of axions, as the effective theory of a semimetal in which a quartic pairing perturbation forms charged chiral condensates (an axionic superconductor), and compute the one-loop corrections from axion excitations to the Yukawa-like potential and to the London penetration length: the θ of §8 promoted to a dynamical field. Braga, Guimaraes and Paganelly, *Ann. Phys.* 419 (2020) 168245 [arXiv:1812.01705], formulate monopole operators through multivalued fields, split into regular and singular parts, and apply the construction to chiral vortex configurations in topological superconductors; on the lattice the Villain integer $n$ of this week plays the part of that singular piece [Formal analogy.]. The [[julia-toulouse-mechanism|Julia–Toulouse]] condensation of Week 11 is the third leg of the same line, and [[axionic-electrodynamics]] collects the concepts.

## 9. Subtleties and fine print

**F1 — Orientation, the identification of $a$, and every θ-odd sign.** Reversing the orientation, or writing the θ-term with $+E\cdot B$, is the substitution $\theta\to-\theta$: the Witten charge becomes $n_e-\theta n_m/2\pi$, the wall current reverses, and the dyon that condenses above $\theta=\pi$ becomes $(1,1)$ instead of $(-1,1)$. The identification $a=-\phi\,dt+A\cdot dx$ of §3.1 leaves $F\wedge F$ unchanged and fixes which Euclidean Wilson line is a positive charge, and therefore the sign of the lattice Witten phase of §6.4. On the lattice we read the axes as $(\tau,x^1,x^2,x^3)$; if time is the fourth axis, as in Week 8 §5.3, the hypercube orientation is $dx^1\wedge dx^2\wedge dx^3\wedge d\tau=-d\tau\wedge dx^1\wedge dx^2\wedge dx^3$ and $Q_{\rm lat}\to-Q$. Before a θ-odd sign is imported from Witten's paper or from the condensed-matter literature, the source's term is rewritten as a multiple of $E\cdot B$ with its orientation and compared with $-\frac\theta{4\pi^2}E\cdot B$.

**F2 — Boundaries.** On a manifold with boundary, $\int_XF\wedge F=\int_{\partial X}a\wedge da$ up to the global issues of §3.3, and $e^{i\frac{\theta}{8\pi^2}\int a\wedge da}$ is invariant under large gauge transformations of the boundary only for $\theta\in2\pi\mathbb{Z}$ (the Chern–Simons level $\theta/2\pi$ must be an integer). A boundary at other values of θ needs boundary degrees of freedom or a boundary condition, and the half-level layer of §8.2 at $\Delta\theta=\pi$ is consistent only as the boundary of the $\theta=\pi$ bulk. The integrality of §§3.3 and 6.3 needs a closed manifold, here the periodic torus.

**F3 — Background θ versus dynamical axion.** As a coupling, θ is a parameter, and $\theta=0,\pi$ are the time-reversal-invariant values. As a background θ(x), it is a material property and §8 applies with θ prescribed. Promoted to a field with a kinetic term, θ is an axion, a compact scalar of the kind studied in Weeks 1–4, and $\theta\sim\theta+2\pi$ becomes the identification of its target circle. That identification is consistent only if $e^{i\theta Q}$ is periodic, which is the integrality of §3.3 again, and then a wall across which the axion winds once has $\Delta\theta=2\pi$ and an integer Hall conductivity $e^2/h$.

**F4 — Periodicity of the spectrum versus the Lagrangian.** The Lagrangian at $\theta+2\pi$ differs from that at θ; the weight is the same when $Q\in\mathbb{Z}$; the lattice of charges is the same up to $T$; and the dynamical content is the same only if the dynamics supplies every $n_e$ that the relabelling needs, as the collective coordinate does in the Georgi–Glashow model or as dynamical electric matter does. The plain Villain theory of §6.4 is the example where it does not.

**F5 — Spin structure.** $Q\in\frac12\mathbb{Z}$ on a general closed 4-manifold, with $Q=\frac12$ for the hyperplane bundle on $\mathbb{CP}^2$ (§3.3). There, with only bosonic charged fields, $e^{i\theta Q}$ returns only at $\theta\to\theta+4\pi$. The torus $T^4$ is spin, so nothing in §6 is affected, but statements such as "θ is $2\pi$-periodic" carry this hypothesis.

**F6 — How the two lattice terms trade under a branch shift.** Under $n\to n+dk$, $a\to a+2\pi k$ with $k\in C^1(\Lambda,\mathbb{Z})$, Leibniz gives $\sum n\cup dk=-\sum m\cup k$, $\sum dk\cup n=\sum k\cup m$ and $\sum dk\cup dk=0$, so $\frac12\sum n\cup n$ changes by $\frac12\sum(k\cup m-m\cup k)$, while the linear term changes by $-\frac1{4\pi}\sum(2\pi k\cup m-m\cup2\pi k)=-\frac12\sum(k\cup m-m\cup k)$. The two changes cancel, and when $m\neq0$ neither term is invariant alone: moving a Dirac sheet across a monopole's worldline changes the sheet-intersection count and the Witten Wilson line together. This is the lattice form of the statement that the fractional Witten charge is compatible with invisible Dirac strings (§5).

## 10. Common misconceptions

- **"θ is unobservable because it multiplies a total derivative."** It is tempting because $F\wedge F=d(a\wedge da)$ drops out of the classical equations. On a compact gauge field the total derivative integrates to the integer $Q$ on closed manifolds, fixes the electric charge of every monopole through the θ-modified Gauss law (§4), leaves the charge $\theta n_m/2\pi$ at each point where $\nabla\cdot B\neq0$ (§4.3), and produces Hall layers wherever θ jumps (§8). A shift of θ by $2\pi$ is unobservable, on spin manifolds and with the spectrum relabelled.
- **"The Witten effect violates charge quantization."** It is tempting because a monopole at $\theta=\pi$ carries charge ½. The quantized quantity is the generator $\hat N$ of gauge rotations, whose eigenvalues remain integers (§4.2); Wilson lines still have integer charges; fractional charges occur only on objects with magnetic charge; and the pairing $\langle v,w\rangle$ that Dirac quantization constrains is a θ-independent integer (§5).
- **"Since the physics at $\theta=2\pi$ equals that at 0, nothing happens in between."** It is tempting because the endpoints agree. Between them the states flow into one another (§5), and in the confining regime the lightest monopole-type dyon changes at $\theta=\pi$, where a first-order transition with spontaneous CP breaking can occur (§7.3); on the plain Villain lattice the endpoints do not even agree (§6.4).

## 11. Historical note

Witten's 1979 paper worked in the Georgi–Glashow model, where an adjoint Higgs field breaks $SO(3)$ to $U(1)$ and 't Hooft–Polyakov monopoles exist, with a θ-term added. He argued from the operator that generates gauge rotations about the direction of the Higgs field, which must satisfy $e^{2\pi iN}=1$ because a $2\pi$ rotation is the identity on the fields of the model; expressing $N$ through the electric and magnetic charges, he found that the electric charges of dyons are shifted by $e\theta/2\pi$ per unit of magnetic charge. Section 4.2 is the abelian transcription of that argument. In 1981 't Hooft proposed, for non-abelian gauge theories, confinement phases in which dyons condense, oblique confinement. Cardy and Rabinovici (1982) studied $\mathbb{Z}_p$ lattice gauge models in four dimensions with a θ parameter, where Witten's fractional charge appears directly, and found a rich phase structure in $p$, θ and the coupling, with electric and magnetic condensation, dyonic condensation and oblique confinement; in a companion paper Cardy constructed the phase diagrams of abelian lattice gauge theories with θ from duality arguments and found infinitely many phases and a mechanism for spontaneous CP violation at $\theta=\pi$. Wilczek (1987) wrote down the equations of axion electrodynamics and drew physical consequences from them, and two decades later Qi, Hughes and Zhang identified the θ-term with $\theta=\pi$ as the response theory of topological insulators. The lattice formulation with an integer instanton number and an exactly periodic θ, together with the Witten effect for magnetic matter, is recent: Sulejmanpasic and Gattringer (2019), and the modified Villain systematics of Gorantla, Lam, Seiberg and Shao that Semester II Week 12 follows.

## 12. What to take away

1. **The θ-term is $-\frac{\theta}{4\pi^2}\int E\cdot B$ in Minkowski signature and the phase $e^{i\theta Q}$ in Euclidean signature,** with $Q=\frac1{8\pi^2}\int F\wedge F$ an integer on closed spin manifolds and in $\frac12\mathbb{Z}$ in general; its θ-odd signs are tied to the orientation.
2. **The Witten effect is Gauss's law with the θ-modified momentum.** The integer is $\hat N=\oint(E/e^2-\theta B/4\pi^2)\cdot dS$, integral by compactness, so $q_e=n_e+\theta n_m/2\pi$: monopoles become dyons, and charge quantization survives as the integrality of $\hat N$ and of the pairing $\langle v,w\rangle$.
3. **θ is periodic up to spectral flow.** At $\theta+2\pi$ the charge lattice returns with $(n_e,n_m)\to(n_e+n_m,n_m)$, the $T$ of $SL(2,\mathbb{Z})$.
4. **On the lattice, periodicity needs the monopole-free theory.** $Q_{\rm lat}=\frac12\sum n\cup n-\frac1{4\pi}\sum(a\cup dn-dn\cup a)$ is an integer for $dn=0$ and not otherwise; the naive $\sin\theta_P$ density is never an integer; and the obstruction term is the Witten coupling of the monopoles, a Wilson line of charge $\theta n_m/2\pi$ on each worldline.
5. **Dyon condensation and θ-walls are the two physical faces of the term.** At strong coupling the condensing dyon changes at $\theta=\pi$, with CP breaking and oblique phases organized by $SL(2,\mathbb{Z})$; where θ jumps by Δθ, the wall is a Hall layer with $\sigma_{xy}=(\Delta\theta/2\pi)(e^2/h)$, the half-quantized surface of a topological insulator.

## 13. Looking ahead: Block D

Block C studied pure gauge theory and its defects, and this week showed that even the pure theory hides dyons, oblique phases and Hall layers once θ is switched on. [[week-13-fradkin-shenker-gauge-higgs|Week 13]] adds dynamical matter, the Fradkin–Shenker model, where the Higgs and confining regions of the gauge–Higgs diagram are analytically connected when the matter carries the fundamental charge; the question it leaves, what distinguishes phases when no local order parameter is available, is answered in Semester II by the realization of higher-form symmetries, and the lattice θ-term of §6 returns in Semester II Week 12 as the first exact construction of the modified Villain program.

## 14. Problem set

Problems 1–3 are the classroom core: Problem 1 uses §§4–5, Problem 2 §§3 and 6, and Problem 3 §8.2, and none needs §7; Problems 4⋆–6⋆ are self-study consolidation, solvable from the note, each with a hint; Problems 7⋆⋆ and 8⋆⋆ are research extensions and state what is known, what is explored and what counts as completion. The derivations of §§4, 6 and 8.2 are not set again.

**Core problems** (everyone).

**1. Dyon energies and their level crossings** (extends §§4–5; prepares §7.3). Consider a static dyon $(n_e,n_m)$ with $\oint B\cdot dS=2\pi n_m$ and electric charge given by the box of §4.1.
(a) Show that the field energy outside a sphere of radius $R$ is $\mathcal E(R)=\frac{e^2}{8\pi R}\,|n_e+n_m\tau|^2$, with $\tau=\theta/2\pi+2\pi i/e^2$.
(b) For $n_m=1$, compute the splitting $\mathcal E_{(0,1)}-\mathcal E_{(-1,1)}$ at $\theta=\pi+\delta$ to first order in δ, and show that the first-order result is exact.
(c) For $n_m=2$, find the values of θ in $[0,2\pi)$ at which the lowest level changes, the splitting there to first order in the distance from the crossing, and the lowest level at $\theta=\pi$ with its charge $q_e$. Show that for general $n_m$ the lowest level changes $n_m$ times per period, and relate this count to the spectral flow of §5.

**2. The two-dimensional lattice θ-term** (extends §6). Consider two-dimensional Villain $U(1)$ gauge theory on the $L\times L$ torus with the weight $e^{i\theta Q_2}$, where $Q_2=\frac1{2\pi}\sum_PF_P$ and $F=da-2\pi n$.
(a) Show that $Q_2=-\sum_Pn_P\in\mathbb{Z}$ for every configuration, and explain why no analogue of the monopole obstruction of §6.4 arises in two dimensions.
(b) Show that the naive $\frac1{2\pi}\sum_P\sin\theta_P$ is not integer-valued, and evaluate it for one unit of uniform flux on the $4\times4$ torus.
(c) Compute $Z(\theta)$ exactly by Poisson resummation on each plaquette followed by the compact link integrals, and show that it is $2\pi$-periodic in θ. Find the free energy per plaquette as $L\to\infty$ and describe its behaviour at $\theta=\pi$.
(*Hint:* the Poisson identity of [[courses/generalized-symmetries-course/conventions|conventions]] §3, with the phase $e^{i\theta(\phi-2\pi n)/2\pi}$ kept inside the Gaussian; Move 3 of Week 8 §3.)

**3. The θ = π slab** (extends §8.2). A slab $0<z<d$ has $\theta=\pi$ inside and $\theta=0$ outside, and magnetic coatings on its two faces gap them, choosing the branch of θ just inside each face.
(a) Using the wall result of §8.2, find the Hall conductance of each face and of the slab when θ runs $0\to\pi\to0$ across the slab, and when it runs $0\to\pi\to2\pi$.
(b) Show that the total is an integer multiple of $e^2/h$ in both cases, and explain why no surface perturbation that preserves the bulk value θ = π can remove the ½ of a single face.
(c) A uniform $B_z$ threads the slab. Find the surface charge on each face in both cases and check the Středa relation for the slab as a whole.

**Starred problems.**

**4⋆. The Witten effect from a collective coordinate** (extends §4.2; source: Witten 1979). Model the internal degree of freedom of a monopole as a rotor $\alpha\sim\alpha+2\pi$ carrying unit charge at the monopole's position, $L_{\rm rot}=\frac I2\big(\dot\alpha-a_t(0)\big)^2$ with $a_t=-\phi$ (§3.1), and add the coupling $-\frac{\theta n_m}{2\pi}\phi(0)$ of §4.3.
(a) Show that the charge $q\equiv-\partial L/\partial\phi(0)$ equals $-p_\alpha+\theta n_m/2\pi$, with $p_\alpha$ the momentum conjugate to α.
(b) Quantize, and show that the spectrum of $q$ is $n_e+\theta n_m/2\pi$ with $n_e=-p_\alpha\in\mathbb{Z}$; say which step uses the compactness of the gauge group.
(c) In the Georgi–Glashow model α is a global gauge rotation of the monopole solution about the direction of the Higgs field. Explain why the θ-term evaluated on the rotating solution is linear in $\dot\alpha$, and compare with (a).
(*Hint:* for (c), evaluate $E\cdot B$ on a solution rotated at angular velocity $\dot\alpha$ and use §4.3.)

**5⋆. $SL(2,\mathbb{Z})$ orbit bookkeeping** (extends §7). Let $M_T=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ and $M_S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ act on $(n_e,n_m)^{\rm T}$.
(a) CP sends θ to $-\theta$, that is $\tau\to-\bar\tau$, and the label $v$ to $M_{\rm CP}v$ with $M_{\rm CP}={\rm diag}(-1,1)$ (§7.3). Show that the pair leaves the self-energy of §7.1 invariant, that $\det M_{\rm CP}=-1$ and that CP reverses the Dirac pairing, so that CP extends $SL(2,\mathbb{Z})$ to $GL(2,\mathbb{Z})$. Show that CP followed by $\tau\to\tau+1$ acts as $\tau\to1-\bar\tau$, whose fixed line ${\rm Re}\,\tau=\frac12$ is $\theta=\pi$, with the label map ${\rm CP}_{\theta=\pi}$ of §7.3. Find the fixed set of CP followed by $S$, $\tau\to1/\bar\tau$, and its label map, and say which two charges it exchanges there and which boundary of Figure 3 the fixed set is.
(b) Show that every primitive $(p,q)$ is the image of $(1,0)$ under some element of $SL(2,\mathbb{Z})$, and find one that maps the Higgs region of Figure 3 onto the region where $(-1,2)$ condenses.
(c) In the $(-1,2)$ phase at θ = π, list the confined probes among $(1,0)$, $(0,1)$, $(-1,1)$ and $(1,1)$, with their numbers of strings.
(d) Find the points of Figure 3 where three phases meet, and say what the heuristic of §7.4 predicts there.
(*Hint:* for (a), $|n_e+n_m\bar\tau|=|n_e+n_m\tau|$, and the label map of each composite is fixed by requiring $\varepsilon$ to be invariant; for (b), the Euclidean algorithm on $(p,q)$; for (d), $\tau=e^{i\pi/3}$ and its images.)

**6⋆. A moving lattice monopole** (extends §6.4). Take a Dirac sheet on the $3^4$ torus whose boundary is a monopole worldline that runs in the τ direction and takes one step in the $x^1$ direction at some time.
(a) Compute $m=dn$ and identify the dual worldline $j=\star m$ with the orientations of Week 8 §5.3, translated to the axis order of §6.
(b) Using the coefficient formula of §6.4, show that the linear term of $Q_{\rm lat}$ couples $a$ to links next to the worldline with total weight $\frac{\theta n_m}{2\pi}$ per step, averaged over two diagonal corners, and that it is invariant under $a\to a+d\lambda$ because $dm=0$.
(*Hint:* Leibniz with $d(\lambda\cup m)=d\lambda\cup m$ and $d(m\cup\lambda)=-m\cup d\lambda$.)

**⋆⋆ problems** (research extension).

**7⋆⋆. The axion response of a Weyl semimetal.** *What is known:* for two Weyl nodes separated by $2b$ in momentum and $2b_0$ in energy, Zyuzin and Burkov identified $\theta(x,t)=2(b\cdot x-b_0t)$ in their conventions; Vazifeh and Franz confirmed the anomalous Hall effect in a lattice model of the Weyl medium and found the equilibrium current along $B$ predicted by the $b_0$ term (the chiral magnetic effect) to be absent, and they explain the discrepancy with the field-theoretic treatment. *What is explored:* how much of the axion response of a semimetal is a property of its equilibrium state. *Completion:* (i) the anomalous Hall conductivity from §8.1, with the sign of θ translated to the convention of §3.1 (F1), matched against the sum of the Chern numbers of the constant-$k_z$ planes between the nodes; (ii) an account, following Vazifeh–Franz, of why a static $b_0$ gives no equilibrium current, naming the step of the naive derivation that fails; (iii) a statement, with a verified source, of a non-equilibrium setting in which a $\dot\theta B$ term does describe a physical current, and of what the dynamical-axion setting of Chrispim–Bruni–Guimaraes adds. *Sources:* Zyuzin–Burkov; Vazifeh–Franz; §8 of this note; Chrispim, Bruni, Guimaraes (§8.3).

**8⋆⋆. The Witten effect for 't Hooft lines in the monopole-free theory.** *What is known:* in the monopole-free Villain theory $Q_{\rm lat}$ is an integer (§6.3); Sulejmanpasic and Gattringer construct the four-dimensional θ-term in their formulation and demonstrate the Witten effect for magnetically charged matter; Gorantla, Lam, Seiberg and Shao systematize the modified Villain theories. *What is explored:* an exact lattice statement of the Witten effect for an external 't Hooft line. *Completion:* define the 't Hooft line as a prescribed $m=dn$ along a closed dual loop in an otherwise monopole-free sum; show that the θ-term dresses it exactly with the corner-averaged Wilson line of charge $\theta/2\pi$ of §6.4; prove that the dressed line is invariant under both redundancies (F6); and prove the exact identity that the theory at $\theta+2\pi$ with the line $(0,1)$ equals the theory at θ with the line $(1,1)$, where the unit Wilson factor of the lattice $(1,1)$ line is defined with the same framing, the corner average $e^{\frac i2(\oint_{\rm base}a+\oint_{\rm far}a)}$ over the two corners of §6.4. That factor differs from a single-path unit Wilson line by $e^{\frac i2\int_{\rm ribbon}F}$, with the ribbon spanned between the two paths, times the sheet sign $(-1)^{\sum_{\rm ribbon}n}$, so with a single-path $(1,1)$ line the identity holds only up to that factor. *Sources:* §6 and F6 of this note; Sulejmanpasic–Gattringer; Gorantla–Lam–Seiberg–Shao, the four-dimensional Villain sections.

## Self-study answer checkpoints

These checkpoints cover the core problems; starred and ⋆⋆ problems remain source-led.

1. (a) The decisive step is the field of the dyon in the course's units: $\oint E/e^2\cdot dS=q_e$ gives $E=e^2q_e\hat r/4\pi r^2$, and $\oint B\cdot dS=2\pi n_m$ gives $B=n_m\hat r/2r^2$. With the energy density $(E^2+B^2)/2e^2$, $\int_R^\infty4\pi r^2dr$ gives $\frac{e^2q_e^2}{8\pi R}+\frac{\pi n_m^2}{2e^2R}=\frac{e^2}{8\pi R}\big[q_e^2+(2\pi n_m/e^2)^2\big]=\frac{e^2}{8\pi R}|n_e+n_m\tau|^2$. (b) The magnetic parts of the two energies are equal and the $q_e^2$ differ by a term linear in θ, so $\mathcal E_{(0,1)}-\mathcal E_{(-1,1)}=\frac{e^2}{8\pi R}\big(\frac\theta\pi-1\big)$ exactly, that is $\frac{e^2}{8\pi R}\cdot\frac{\delta}{\pi}$ at $\theta=\pi+\delta$, and $(-1,1)$ is the lower level above π. (c) With $q_e=n_e+\theta/\pi$ the lowest level is $(0,2)$ for $0\le\theta<\frac\pi2$, $(-1,2)$ for $\frac\pi2<\theta<\frac{3\pi}2$ and $(-2,2)$ for $\frac{3\pi}2<\theta<2\pi$; at $\theta=\frac\pi2+\delta$, $\mathcal E_{(0,2)}-\mathcal E_{(-1,2)}=\frac{e^2}{8\pi R}\cdot\frac{2\delta}{\pi}$, twice the slope of (b), and the same holds at $\frac{3\pi}2$. At $\theta=\pi$ the lowest level $(-1,2)$ is purely magnetic, $q_e=0$, with $\mathcal E=2\pi/e^2R$, and $(0,2)$ and $(-2,2)$, with $q_e=\pm1$, lie $\frac{e^2}{8\pi R}$ above it. For general $n_m$ the crossings sit at $\theta_k=(2k+1)\pi/n_m$, $k=0,\dots,n_m-1$, with the splitting $\frac{e^2}{8\pi R}\cdot\frac{n_m\delta}{\pi}$ at $\theta_k+\delta$; there are $n_m$ of them because over one period the flow of §5 raises the charge of every label by $n_m$ units, $q_e\to q_e+n_m$, and the lowest level passes from $(0,n_m)$ to $(-n_m,n_m)$ one unit at a time. A common failure is to use the Gaussian-unit monopole field ($\nabla\cdot B=4\pi g$) with the Gauss law of §4.1, which changes both the relative factor and the sign of the Witten term.
2. (a) $\sum_P(da)_P=0$ on the closed torus, since every link borders two plaquettes with opposite orientations, so $Q_2=-\sum n$; in two dimensions $dn$ would be a 3-cochain, which does not exist, so there are no monopoles and the Villain θ-term is automatically periodic. (b) With flux $2\pi/L^2$ per plaquette, $\frac{L^2}{2\pi}\sin\frac{2\pi}{L^2}=0.9745$ for $L=4$, tending to 1 as $L\to\infty$. (c) Per plaquette, $\sum_ne^{-\frac\beta2(\phi-2\pi n)^2+\frac{i\theta}{2\pi}(\phi-2\pi n)}=(2\pi\beta)^{-1/2}\sum_{w\in\mathbb{Z}}e^{-(w-\theta/2\pi)^2/2\beta+iw\phi}$; the link integrals force $w$ to be the same on every plaquette, so $Z(\theta)=(2\pi\beta)^{-N_P/2}\sum_{w\in\mathbb{Z}}e^{-N_P(w-\theta/2\pi)^2/2\beta}$, periodic under $\theta\to\theta+2\pi$ with $w\to w+1$. The free energy per plaquette tends to $\frac12\ln(2\pi\beta)+\min_w\frac{(w-\theta/2\pi)^2}{2\beta}$, with a cusp at θ = π where the electric-flux sectors $w=0$ and $w=1$ cross. A common failure is to complete the square with the wrong sign of the θ-shift, or to forget that the single surviving $w$ exists only because the link integrals run over one period.
3. (a) The bottom face has $\Delta\theta=+\pi$ and $\sigma_{xy}=+\frac12e^2/h$. If θ returns to 0, the top face has $\Delta\theta=-\pi$ and $-\frac12e^2/h$, and the slab has 0; if θ continues to $2\pi$, the top face has $+\frac12e^2/h$ and the slab has $e^2/h$. (b) The totals are 0 and 1 times $e^2/h$, the Chern number of the slab as a two-dimensional system; a perturbation at one face can change its Δθ only by a multiple of $2\pi$, so the face conductance stays in $(\frac12+\mathbb{Z})\,e^2/h$. (c) The surface charges are $\frac{\Delta\theta}{4\pi^2}B_z=\pm\frac{B_z}{4\pi}$ in units of the unit charge: opposite on the two faces in the first case (total 0), equal in the second (total $B_z/2\pi$), which is $\sigma_{xy}^{\rm total}B_z$ in both, as Středa requires. A common failure is to assign "θ = π" to the bulk and forget that each face selects the branch.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block C. Rewritten to the note-quality-template standard on 2026-09-28 (first draft 2026-07-01). Last revised 2026-10-04.*
