---
title: "Week 6 — Wilson's Formulation: Compact Groups, Haar Measure, Strong Coupling"
type: lecture-notes
course: syllabus
semester: 1
week: 6
block: B
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 1–5; representation theory of U(1) and SU(2) (characters); Gaussian and group integrals
modified: 2026-09-28
---

# Week 6 — Wilson's Formulation: Compact Groups, Haar Measure, Strong Coupling

> *Wegner's $\mathbb Z_2$ gauge theory of Week 5 already contained the logic of lattice gauge theory: variables on links, an action on plaquettes, no local order parameter, and a Wilson loop whose strong-coupling expansion tiles a surface. This week we replace the sign on each link by an element of a compact Lie group, as Wilson did in 1974 to regulate electrodynamics and Yang–Mills theory. One new tool does all the work. We integrate each link over the group with its invariant (Haar) measure and expand the plaquette weight in characters, exactly as Week 1 expanded the rotor chain in the characters of U(1); the strong-coupling series then becomes a sum over surfaces, and the area law comes out for every compact group, with a coefficient that we compute for U(1), SU(2) and SU(N). Whether this confinement survives at weak coupling depends on the group and on the dimension: compact U(1) confines at every coupling in $d=3$ (Weeks 9–10) and has a Coulomb phase in $d=4$ (Week 11), while for SU(N) in $d=4$ the expectation, supported by Monte Carlo and unproven, is that no transition separates strong from weak coupling. Week 7 turns the same lattice into a Hamiltonian.*

### How to use this chapter

- **In class:** derive at the board, in this order, the invariance of the Haar measure and the rules (G0)–(G2) of §2.3 (the Schur argument takes five lines), the SU(2) class measure of §2.2, the coefficient $\tilde c_{1/2}=I_2(\beta)/I_1(\beta)=\beta/4+O(\beta^3)$ of §3.3 and the SU(N ≥ 3) coefficient $\beta/2N^2$ of §3.4; then the 2×2 loop link by link (§4.1, Figure 1), the tiling rule (§4.2) and the first correction $\sigma=-\ln\tilde c_F-2(d-2)\tilde c_F^4$ (§4.3, Figure 2). In the second lecture: the continuum limit with $\beta=2N/g^2$ and $\beta=1/e^2$ (§5), Creutz ratios (§6) and roughening (§7.3). Problems 1–4 are the classroom core.
- **For self-study:** the Euler-angle chart of §2.2, §3.5, the remaining fine print (§§7.1–7.2 and 7.4–7.7) and §§8–9. The one calculation to do alone is Problem 1, the 1×2 loop by hand, followed by the same computation with one tile reversed, which vanishes for SU(3) and does not vanish for SU(2).
- **Instructor checkpoint:** the SU(2) coefficient. Since $\operatorname{tr}U=\operatorname{tr}U^\dagger$ for SU(2), both halves of $\operatorname{Re}\operatorname{tr}U$ feed the spin-½ character and $\tilde c_{1/2}\simeq\beta/4$; setting $N=2$ in $\beta/2N^2$ gives $\beta/8$, off by a factor 2 (§3.3). The second trap is the counting of powers of N in a tiling: every link integral costs $1/N$ and every site of the surface returns a factor N, and a student who forgets the sites is off by $N^{-V}$, for instance $N^{-9}$ for the 2×2 loop (§4.2). The third is the coupling: $\beta=2N/g^2$ belongs to SU(N), and U(1) has $\beta=1/e^2$ (§5).

## 0. Reading

**Primary:** Wilson, *Phys. Rev. D* 10 (1974) 2445, §III (the lattice formulation, with the gauge field as an angular variable and no gauge fixing) and §IV (the strong-coupling expansion and the area law). Kogut, *Rev. Mod. Phys.* 55 (1983) 775: §III for the 2×2 SU(2) loop at strong coupling with the two Haar integrals of §2.3 (its Figs. 23–24), §IV.A for character expansions and the "house" correction of the $\mathbb Z_2$ loop, §§V.B–V.C for the universal $1/R$ term and roughening.

**Secondary:**
- Kogut, *Rev. Mod. Phys.* 51 (1979) 659, §V.D (the $\mathbb Z_2$ loop), §VI.A–B (abelian lattice gauge theory, its strong-coupling area law and phase diagrams) and §VIII.A–B (the SU(2) theory, its classical continuum limit, and whether strong and weak coupling are connected).
- Drouffe & Itzykson, *Phys. Rep.* 38 (1978) 133, §3.1 (selection rules of the character expansion) and Appendix C (group measures for $\mathbb Z_n$, U(1), SU(2) and U(n)).
- Creutz, *Phys. Rev. D* 21 (1980) 2308: the first Monte Carlo study of SU(2), with the ratios of §6.

**Optional research reading:** Osterwalder & Seiler, *Ann. Phys.* 110 (1978) 440 (convergence of the strong-coupling expansion and the area law at small β for every compact group); Göpfert & Mack, *Commun. Math. Phys.* 82 (1982) 545 (3d U(1) with the Villain action confines at every coupling); Guth, *Phys. Rev. D* 21 (1980) 2291, and Fröhlich & Spencer, *Commun. Math. Phys.* 83 (1982) 411 (the Coulomb phase of 4d U(1)); Svetitsky & Yaffe, *Nucl. Phys. B* 210 (1982) 423 (for §7.6).

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]]. Every sign and normalization comes from [[courses/generalized-symmetries-course/conventions|conventions]] §4, and every reference from [[courses/generalized-symmetries-course/appendices/bibliography-and-paper-map|bibliography-and-paper-map]].

## 1. From $\mathbb Z_2$ to a compact group

### 1.1 The question

Static sources in a representation r of the gauge group G, held at distance R for a Euclidean time T, feel a potential $V(R)$ that we read off the [[wilson-loop|Wilson loop]], $\langle W_r(C)\rangle\sim e^{-V(R)T}$ for the $R\times T$ rectangle C. If V grows linearly, the sources are confined. In [[week-05-wegner-z2-gauge-theory|Week 5]] the group was $\mathbb Z_2$ and the strong-coupling answer was $\langle W\rangle\simeq(\tanh\beta)^A$. For a compact Lie group three things change. The sum over the two values of a sign becomes an integral over G, which must respect the group multiplication (the Haar measure, §2). The plaquette weight expands in all irreducible representations of G (the characters, §3). And the rule "a link integrates to zero unless it appears an even number of times" becomes "a link integrates to zero unless the representations it carries contain the singlet", which forces tiled surfaces (§4). The two groups of physical interest are U(1), the lattice regulator of compact electrodynamics whose monopoles drive Block C, and SU(N), the lattice regulator of Yang–Mills theory ([[lattice-gauge-theory]], [[confinement]]).

### 1.2 Link variables and what is gauge invariant

On each oriented link $\ell_\mu(x)$ from x to $x+\hat\mu$ we place $U_\mu(x)\in G$; the reversed link carries $U_\mu(x)^{-1}=U_\mu(x)^\dagger$. A gauge transformation assigns $g_x\in G$ to every site and acts as
$$
U_\mu(x)\ \longrightarrow\ g_x\,U_\mu(x)\,g_{x+\hat\mu}^{-1}.
$$
The ordered product $U_\gamma$ along a path γ transforms as $g_{\rm start}U_\gamma g_{\rm end}^{-1}$, so the holonomy of a closed loop C based at x transforms by conjugation, $U_C\to g_xU_Cg_x^{-1}$. It is gauge covariant, and for a non-abelian group its invariant functions are the class functions, spanned by the characters $\chi_r(U_C)=\operatorname{tr}D^r(U_C)$ of the irreducible representations $D^r$ of dimension $d_r$. The Wilson loop in representation r is
$$
W_r(C)=\frac{1}{d_r}\,\chi_r(U_C),
$$
normalized to 1 on the trivial configuration. The plaquette holonomy, with the orientation of [[courses/generalized-symmetries-course/conventions|conventions]] §1 (bottom, right, top reversed, left reversed), is
$$
U_P=U_\mu(x)\,U_\nu(x+\hat\mu)\,U_\mu(x+\hat\nu)^\dagger\,U_\nu(x)^\dagger ,
$$
and the same remarks apply to it: $U_P$ is conjugated at its base corner under a gauge transformation, it is conjugated by a link when the base corner is moved, and it becomes $U_P^\dagger$ when the orientation is reversed. Only its class is observable. For U(1), $U_\mu(x)=e^{ia_\mu(x)}$ with $a_\mu(x)\in(-\pi,\pi]$, the plaquette is $U_P=e^{i(da)_P}$ with the coboundary of [[week-02-lattice-cell-complex-cochains|Week 2]], conjugation is trivial and $U_P$ itself is invariant; with $g_x=e^{-i\lambda_x}$ the transformation above is $a\to a+d\lambda$ of [[courses/generalized-symmetries-course/conventions|conventions]] §4, and the charge-q loop is $W_q(C)=e^{iq\sum_Ca}$ ([[courses/generalized-symmetries-course/conventions|conventions]] §6). In the continuum, $U_\ell=\mathcal P\exp(i\int_\ell A)$ with $A=A^aT^a$ and points earlier along the link standing to the left; for U(1), $a_\ell=\int_\ell A$.

Elitzur's theorem of Week 5 carries over word for word, since its proof uses only the compactness of the gauge group and the invariance of the measure: $\langle U_\ell\rangle=0$, and the observables are class functions of closed loops.

### 1.3 Wilson's action

The actions of [[courses/generalized-symmetries-course/conventions|conventions]] §4 are
$$
S_{U(1)}=\beta\sum_P\big(1-\cos(da)_P\big),\qquad
S_{SU(N)}=\frac{\beta}{N}\sum_P\operatorname{Re}\operatorname{tr}\big(1-U_P\big),\qquad
Z=\int\prod_\ell dU_\ell\;e^{-S},
$$
where $dU_\ell$ is the Haar measure of §2 and the sums run over unoriented plaquettes. Three requirements single out this form. The action must be a class function of $U_P$ (gauge invariance); it must not depend on the orientation of the plaquette, which is why the real part appears, $\operatorname{Re}\operatorname{tr}U^\dagger=\operatorname{Re}\operatorname{tr}U$; and it should be the simplest such function, the trace in the fundamental representation. The constant makes $S\ge0$, with $S=0$ only when every $U_P=1$. For SU(2) the trace is already real, since the eigenvalues are $e^{\pm i\alpha}$, and the action is $\frac\beta2\sum_P(2-\operatorname{tr}U_P)$. The coupling β is dimensionless; §5 shows that $\beta=1/(e^2a_{\rm lat}^{4-d})$ for U(1) and $\beta=2N/(g^2a_{\rm lat}^{4-d})$ for SU(N), which is $2N/g^2$ in $d=4$.

## 2. The Haar measure

### 2.1 Invariance, and the circle [Proved for U(1); existence and uniqueness Stated — refs.]

A Haar measure on a compact group G is a measure dU with
$$
\int_G dU=1,\qquad \int_G dU\,f(VU)=\int_G dU\,f(UV)=\int_G dU\,f(U)\quad\text{for all }V\in G
$$
and every integrable f. It exists and is unique for every compact group, and it is also invariant under $U\to U^{-1}$ [Stated — refs: Drouffe–Itzykson, Appendix C]. Invariance is what makes the lattice integrals gauge invariant: the change of variables $U_\mu(x)\to g_xU_\mu(x)g_{x+\hat\mu}^{-1}$ preserves every link measure.

For U(1) the measure is $dU=d\theta/2\pi$ on $(-\pi,\pi]$, the measure used for compact fields since Week 1, and uniqueness takes two lines. If μ is a normalized invariant measure, its Fourier coefficients $\hat\mu_n=\int e^{-in\theta}d\mu(\theta)$ satisfy $\hat\mu_n=e^{-in\alpha}\hat\mu_n$ for every translation α, so $\hat\mu_n=0$ for $n\ne0$, while $\hat\mu_0=1$; therefore $\mu=d\theta/2\pi$. The irreducible representations of U(1) are the characters $e^{in\theta}$, $n\in\mathbb Z$, and they are orthonormal,
$$
\int_{-\pi}^{\pi}\frac{d\theta}{2\pi}\;e^{in\theta}\,e^{-im\theta}=\delta_{nm}.
$$
This is the abelian selection rule: a link integrates to zero unless the net charge it carries vanishes.

### 2.2 SU(2) as the three-sphere [Proved.]

Every $U\in SU(2)$ can be written $U=u_0\mathbb 1+i\vec u\cdot\vec\sigma$ with real $(u_0,\vec u)$ and $\det U=u_0^2+\vec u^{\,2}=1$, so SU(2) is the unit sphere $S^3\subset\mathbb R^4$. Left multiplication by a fixed V is a linear map of $\mathbb R^4$ that preserves $u_0^2+\vec u^{\,2}=\det(VU)$, and is therefore an orthogonal transformation, and so is right multiplication. The round measure of $S^3$ is therefore left and right invariant, and normalized it reads
$$
dU=\frac{1}{\pi^2}\,\delta\big(u_0^2+\vec u^{\,2}-1\big)\,d^4u ,
$$
since $\int d^4u\,\delta(|u|^2-1)=\tfrac12{\rm Vol}(S^3)=\pi^2$. Two charts are useful.

*Class variables.* Put $u_0=\cos\alpha$ and $\vec u=\sin\alpha\,\hat n$, with $\alpha\in[0,\pi]$ and $\hat n\in S^2$. Then $U=e^{i\alpha\hat n\cdot\vec\sigma}$ has eigenvalues $e^{\pm i\alpha}$ and $\operatorname{tr}U=2\cos\alpha$. In hyperspherical coordinates $d^4u=\rho^3d\rho\,\sin^2\!\alpha\,d\alpha\,d^2\Omega_{\hat n}$ and $\delta(\rho^2-1)=\frac12\delta(\rho-1)$, so
$$
dU=\frac{1}{2\pi^2}\,\sin^2\!\alpha\,d\alpha\,d^2\Omega_{\hat n},\qquad
\int dU\,f(U)=\frac{2}{\pi}\int_0^{\pi}d\alpha\,\sin^2\!\alpha\;f(\alpha)\quad\text{for class functions},
$$
where $f(\alpha)$ is the value of f on the class with eigenvalues $e^{\pm i\alpha}$ (and $\frac2\pi\int_0^\pi\sin^2\alpha\,d\alpha=1$). The weight $\sin^2\alpha$ says that classes near $\pm\mathbb 1$ are rare, because they are small two-spheres in $S^3$.

*Euler angles.* With $U=e^{i\phi\sigma_3/2}e^{i\theta\sigma_2/2}e^{i\psi\sigma_3/2}$, $\phi\in[0,2\pi)$, $\theta\in[0,\pi]$, $\psi\in[0,4\pi)$, one multiplies out $u_0+iu_3=\cos\frac\theta2\,e^{i(\phi+\psi)/2}$ and $u_2+iu_1=\sin\frac\theta2\,e^{i(\phi-\psi)/2}$. These are Hopf coordinates $(\cos\eta\,e^{i\xi_1},\sin\eta\,e^{i\xi_2})$ on $S^3$, in which the round measure is $\sin\eta\cos\eta\,d\eta\,d\xi_1d\xi_2$; with $\eta=\theta/2$ and $d\xi_1d\xi_2=\frac12d\phi\,d\psi$ this is proportional to $\sin\theta\,d\phi\,d\theta\,d\psi$, and normalized,
$$
dU=\frac{1}{16\pi^2}\,\sin\theta\;d\phi\,d\theta\,d\psi .
$$

*Characters, and orthogonality verified.* In the spin-j representation, $U=e^{i\alpha\hat n\cdot\vec\sigma}=e^{2i\alpha\hat n\cdot\vec J}$ has eigenvalues $e^{2im\alpha}$, $m=-j,\dots,j$, so
$$
\chi_j(\alpha)=\sum_{m=-j}^{j}e^{2im\alpha}=\frac{\sin(2j+1)\alpha}{\sin\alpha},\qquad d_j=2j+1,
$$
and the class measure gives
$$
\int dU\,\chi_j\,\chi_{j'}=\frac{2}{\pi}\int_0^\pi d\alpha\,\sin(2j+1)\alpha\,\sin(2j'+1)\alpha=\delta_{jj'} .
$$
The characters are real, $\chi_j(U^\dagger)=\chi_j(U)$, because every representation of SU(2) is equivalent to its conjugate. They are also complete on class functions: $\sin\alpha\,f(\alpha)$ has a Fourier sine series on $[0,\pi]$, and that series is the character expansion of f. Two products are used below: $\chi_{1/2}^2=4\cos^2\alpha=\chi_0+\chi_1$, so that $\int dU\,\chi_{1/2}^2=1$ and $\int dU\,\chi_{1/2}^4=\int dU\,(\chi_0+\chi_1)^2=2$, the number of singlets in four spin-½'s.

### 2.3 Matrix elements and the gluing rules [Proved.]

Let D be an irreducible unitary representation of dimension d; for SU(N) the fundamental, with $d=N$. For an arbitrary $d\times d$ matrix X, the matrix $M=\int dU\,D(U)\,X\,D(U)^\dagger$ satisfies $D(V)MD(V)^\dagger=M$ for every V, by left invariance. It commutes with the irreducible $D(G)$, so $M=c\,\mathbb 1$ by Schur's lemma, and the trace gives $c=\operatorname{tr}X/d$. Reading off the components of X,
$$
\int dU\;D_{ij}(U)\,D^\dagger_{kl}(U)=\frac1d\,\delta_{il}\,\delta_{jk}.
$$
In the same way $B=\int dU\,D(U)$ satisfies $D(V)B=B$ for every V, so its range consists of invariant vectors and $B=0$ for a nontrivial irreducible D. For SU(N) the center gives a sharper rule. The element $z=e^{2\pi i/N}\mathbb 1$ belongs to SU(N), and invariance under $U\to zU$ multiplies a product of p matrix elements of U and q of $U^\dagger$ by $z^{p-q}$, so that
$$
\int dU\;U_{i_1j_1}\cdots U_{i_pj_p}\,U^\dagger_{k_1l_1}\cdots U^\dagger_{k_ql_q}=0\qquad\text{unless}\quad p-q\equiv0\ (\mathrm{mod}\ N).
$$
For $N\ge3$ this kills $\int dU\,U_{ij}U_{kl}$. For SU(2) it does not: from $U=u_0+i\vec u\cdot\vec\sigma$ one checks $\bar U=\epsilon\,U\,\epsilon^{-1}$ with $\epsilon=i\sigma_2$, so the fundamental is equivalent to its conjugate (pseudo-real), and the formula above gives $\int dU\,U_{ij}U_{kl}=\frac12\,\epsilon_{ik}\,\epsilon_{jl}$. This single difference between SU(2) and SU(N ≥ 3) is the origin of the factor 2 in §3.3.

Contracting the first formula with fixed matrices A and B gives the three rules that the rest of the week uses,
$$
\text{(G0)}\ \int dU\,\operatorname{tr}(AU)=0,\qquad
\text{(G1)}\ \int dU\,\operatorname{tr}(AU)\,\operatorname{tr}(U^\dagger B)=\frac1N\operatorname{tr}(AB),\qquad
\text{(G2)}\ \int dU\,\operatorname{tr}(AUBU^\dagger)=\frac1N\operatorname{tr}A\,\operatorname{tr}B,
$$
where (G1) follows from $A_{ji}U_{ij}U^\dagger_{kl}B_{lk}\to\frac1NA_{ji}B_{ij}$ and (G2) from $A_{li}U_{ij}B_{jk}U^\dagger_{kl}\to\frac1NA_{ii}B_{jj}$. In words: two traces that share a link, traversed in opposite directions, fuse into one trace at the cost $1/N$; a trace that passes a link twice in opposite directions splits into two, also at the cost $1/N$; and a link met once integrates to zero. When U and $U^\dagger$ stand next to each other in a trace, unitarity removes the link at no cost. For U(1) the three rules collapse into charge conservation at each link. They are the lattice form of Gauss's law: flux can neither begin nor end on a link.

## 3. The character expansion

### 3.1 Definition

The single-plaquette weight $e^{-S_P(U)}$ is a class function, so it expands in characters. In the normalization of [[courses/generalized-symmetries-course/conventions|conventions]] §4,
$$
e^{-S_P(U)}=a_0(\beta)\Big[1+\sum_{r\ne0}d_r\,\tilde c_r(\beta)\,\chi_r(U)\Big],\qquad
a_r=\int dU\;\chi_r(U)^*\,e^{-S_P(U)},\qquad \tilde c_r=\frac{a_r}{d_r\,a_0},
$$
where the formula for $a_r$ follows from the orthonormality of characters. The normalized coefficient has a direct meaning: $\tilde c_r=\langle\chi_r(U)^*\rangle_1/d_r$, the expectation value of the normalized character in the ensemble of a single plaquette. Therefore $|\tilde c_r|\le1$ (since $|\chi_r|\le d_r$), $\tilde c_r\to0$ for $r\ne0$ as $\beta\to0$, and $\tilde c_r\to1$ as $\beta\to\infty$; at small β these are the small parameters of the expansion. Because $S_P(U)=S_P(U^\dagger)$, a representation and its conjugate have the same coefficient, $\tilde c_{\bar r}=\tilde c_r$.

### 3.2 U(1) [Computed.]

With $S_P=\beta(1-\cos\phi)$ the expansion is the Jacobi–Anger expansion of [[week-01-compact-variables-xy-model|Week 1]] §5.1, $e^{-S_P}=e^{-\beta}\sum_nI_n(\beta)e^{in\phi}$, derived there from the integral representation of $I_n$. With $d_n=1$,
$$
\tilde c_n(\beta)=\frac{I_n(\beta)}{I_0(\beta)}=\frac{(\beta/2)^{|n|}}{|n|!}\big(1+O(\beta^2)\big),\qquad
\tilde c_1=\frac\beta2-\frac{\beta^3}{16}+O(\beta^5),
$$
where the small-β form picks the $|n|$-th power of $e^{\pm i\phi}$ from $e^{\frac\beta2(e^{i\phi}+e^{-i\phi})}$, and the $\beta^3$ term follows from $I_1/I_0=\frac\beta2(1+\frac{\beta^2}8)/(1+\frac{\beta^2}4)+O(\beta^5)$. The U(1) plaquette weight is literally the transfer matrix of the rotor chain.

### 3.3 SU(2) [Computed.]

For SU(2), $\operatorname{Re}\operatorname{tr}U=2\cos\alpha$ and $S_P=\beta(1-\cos\alpha)$. The class measure of §2.2 gives
$$
a_j=\frac2\pi\,e^{-\beta}\!\int_0^\pi\! d\alpha\,\sin^2\!\alpha\,\frac{\sin(2j+1)\alpha}{\sin\alpha}\,e^{\beta\cos\alpha}
=\frac1\pi\,e^{-\beta}\!\int_0^\pi\! d\alpha\,\big[\cos2j\alpha-\cos(2j+2)\alpha\big]\,e^{\beta\cos\alpha}
=e^{-\beta}\big[I_{2j}(\beta)-I_{2j+2}(\beta)\big],
$$
where the middle step uses $\sin\alpha\sin n\alpha=\frac12[\cos(n-1)\alpha-\cos(n+1)\alpha]$ and the last the representation $I_m(\beta)=\frac1\pi\int_0^\pi e^{\beta\cos\alpha}\cos m\alpha\,d\alpha$. The difference is a single Bessel function. Indeed $I_{m-1}-I_{m+1}=\frac2\pi\int_0^\pi e^{\beta\cos\alpha}\sin\alpha\,\sin m\alpha\,d\alpha$, and since $e^{\beta\cos\alpha}\sin\alpha=-\beta^{-1}\partial_\alpha e^{\beta\cos\alpha}$, an integration by parts (the boundary terms vanish with $\sin m\alpha$) gives $I_{m-1}-I_{m+1}=\frac{2m}{\beta}I_m$. Therefore $a_j=e^{-\beta}\frac{2(2j+1)}{\beta}I_{2j+1}(\beta)$, and
$$
\boxed{\ \tilde c_j(\beta)=\frac{a_j}{(2j+1)\,a_0}=\frac{I_{2j+1}(\beta)}{I_1(\beta)},\qquad
\tilde c_{1/2}=\frac{I_2(\beta)}{I_1(\beta)}=\frac\beta4-\frac{\beta^3}{96}+O(\beta^5),\ }
$$
where the series follows from $I_2/I_1=\frac\beta4(1+\frac{\beta^2}{12})/(1+\frac{\beta^2}8)+O(\beta^5)$. Numerically $\tilde c_{1/2}(1)=0.24019$ and $\tilde c_{1/2}(2)=0.43313$, in agreement with a direct numerical integration over the group.

The factor that distinguishes this from the SU(N) value of §3.4 is visible at first order. For SU(2), $\frac\beta N\operatorname{Re}\operatorname{tr}U=\frac\beta2\chi_{1/2}(U)$, so $a_{1/2}\simeq e^{-\beta}\frac\beta2\int dU\,\chi_{1/2}^2=e^{-\beta}\frac\beta2$ and $\tilde c_{1/2}\simeq\frac{\beta/2}{2}=\frac\beta4$. For SU(N) the same action is $\frac{\beta}{2N}(\chi_F+\chi_{\bar F})$, and only the $\chi_F$ half feeds the fundamental coefficient, because F and $\bar F$ are inequivalent. For SU(2) they are equivalent (§2.3), $\chi_{\bar F}=\chi_F$, and both halves feed spin ½: the coefficient is twice the value $\beta/2N^2=\beta/8$ that the generic formula gives at $N=2$.

### 3.4 SU(N ≥ 3) [Computed to O(β); SU(3) to O(β²).]

Write $\frac\beta N\operatorname{Re}\operatorname{tr}U=\frac{\beta}{2N}\big(\chi_F(U)+\chi_{\bar F}(U)\big)$ with $\chi_{\bar F}=\chi_F^*$, and expand $e^{-S_P}=e^{-\beta}\exp[\frac{\beta}{2N}(\chi_F+\chi_{\bar F})]$. At first order,
$$
a_F=e^{-\beta}\Big[\frac{\beta}{2N}\int dU\,\chi_F^*\big(\chi_F+\chi_{\bar F}\big)+O(\beta^2)\Big]=e^{-\beta}\Big[\frac{\beta}{2N}+O(\beta^2)\Big],
$$
since $\int\chi_F^*\chi_F=1$ while $\int\chi_F^*\chi_{\bar F}=\int(\operatorname{tr}U^\dagger)^2=0$ by the center rule ($p-q=-2$). With $a_0=e^{-\beta}[1+O(\beta^2)]$,
$$
\boxed{\ \tilde c_F=\frac{a_F}{N\,a_0}=\frac{\beta}{2N^2}+O(\beta^2)\qquad(N\ge3).\ }
$$
At second order the three integrals $\int\chi_F^*\chi_F^2$, $\int\chi_F^*\chi_F\chi_{\bar F}$ and $\int\chi_F^*\chi_{\bar F}^2$ have $p-q=1,-1,-3$, so only the last can survive, and only for $N=3$, where $\int(\operatorname{tr}U^\dagger)^3=1$ counts the single antisymmetric singlet (the baryon) in $\bar F^{\otimes3}$. Thus $\tilde c_F=\frac\beta{18}+\frac{\beta^2}{216}+O(\beta^3)$ for SU(3), and $\tilde c_F=\frac{\beta}{2N^2}+O(\beta^3)$ for $N\ge4$. A numerical integration over SU(3) gives $\tilde c_F(1)=0.06013$, against $0.06019$ from the two terms. The fundamental coefficients of the groups of the course are collected below.

| group | fundamental representation | $\tilde c_F$ at small β |
|---|---|---|
| U(1) | complex | $I_1/I_0\simeq\beta/2$ |
| $\mathbb Z_2$ (Week 5) | real | $\tanh\beta\simeq\beta$ |
| SU(2) | pseudo-real | $I_2/I_1\simeq\beta/4$ |
| SU(3) | complex | $\beta/18+\beta^2/216$ |
| SU(N ≥ 4) | complex | $\beta/2N^2+O(\beta^3)$ |

### 3.5 Higher representations: counting powers of β [Computed.]

At order $\beta^k$ the expansion of $\exp[\frac{\beta}{2N}(\chi_F+\chi_{\bar F})]$ contains products of k characters F or $\bar F$, that is, characters of $F^{\otimes p}\otimes\bar F^{\otimes q}$ with $p+q=k$. So $a_r$ starts at order $\beta^{n_r}$, where
$$
n_r=\min\{\,p+q\ :\ r\subset F^{\otimes p}\otimes\bar F^{\otimes q}\,\},
$$
and $-\ln\tilde c_r=n_r\ln(1/\beta)+O(1)$. For U(1), $n_q=|q|$. For SU(2), $n_j=2j$, the number of boxes of the one-row Young diagram of spin j, and $\tilde c_j=I_{2j+1}/I_1\simeq(\beta/2)^{2j}/(2j+1)!$, for instance $\tilde c_1\simeq\beta^2/24$ and $\tilde c_{3/2}\simeq\beta^3/192$. For SU(N ≥ 3) the adjoint sits in $F\otimes\bar F$, so $n_{\rm adj}=2$, $a_{\rm adj}\simeq e^{-\beta}\frac12(\frac\beta{2N})^2\cdot2\int\chi_{\rm adj}\chi_F\chi_{\bar F}=e^{-\beta}\frac{\beta^2}{4N^2}$ and $\tilde c_{\rm adj}\simeq\beta^2/4N^2(N^2-1)$; a representation with k boxes that is first reached through $F^{\otimes k}$, such as the k-index symmetric or antisymmetric one for $k\le N/2$, has $n_r=k$. The leading strong-coupling coefficient of the Wilson action therefore counts fundamental factors. For SU(2),
$$
\frac{-\ln\tilde c_1}{-\ln\tilde c_{1/2}}\ \longrightarrow\ 2,\qquad \frac{-\ln\tilde c_{3/2}}{-\ln\tilde c_{1/2}}\ \longrightarrow\ 3\qquad(\beta\to0),
$$
while the quadratic Casimirs $C_2(j)=j(j+1)$ would give $8/3$ and $5$. The approach is logarithmic (the ratios are 2.04 and 3.10 at $\beta=10^{-4}$), because the constants $\ln(2j+1)!$ compete with $2j\ln(2/\beta)$. Casimir scaling of the leading coefficient belongs to a different lattice action (Problem 6⋆), and what large loops in higher representations actually do is the subject of §7.5.

## 4. Strong coupling: the area law

### 4.1 The 2×2 loop, link by link [Computed.]

Consider the fundamental loop around the 2×2 square of Figure 1, with the eight boundary links $b_1,\dots,b_8$, the four interior links $i_1,\dots,i_4$ and the four plaquettes $P_1,\dots,P_4$. Each $U_\ell$ refers to the link in its positive direction, and the loop, traversed counterclockwise from the origin, is
$$
U_C=U_{b_1}U_{b_2}U_{b_3}U_{b_4}\,U_{b_5}^\dagger U_{b_6}^\dagger U_{b_7}^\dagger U_{b_8}^\dagger .
$$

![[gs-w06-two-by-two-loop.svg|The 2 by 2 square of plaquettes P1 to P4 with boundary links b1 to b8 and interior links i1 to i4, an arrow on every link in its positive direction, the loop C drawn counterclockwise around the boundary, and a clockwise circulation in each tile]]

**Figure 1. The 2×2 loop and its tiling. Arrows mark the positive direction of each link; the loop runs along b1, b2, b3, b4 and against b5, b6, b7, b8, and each tile carries the conjugate of its counterclockwise plaquette.**

The expectation value is
$$
\langle W_F(C)\rangle=\frac1Z\int\prod_\ell dU_\ell\;\frac1N\operatorname{tr}U_C\;\prod_P a_0\Big[1+\sum_{r\ne0}d_r\tilde c_r\chi_r(U_P)\Big],
$$
and the factors $a_0$ cancel against Z. Expanding the product over plaquettes, each term picks for every plaquette either 1 or one term $d_r\tilde c_r\chi_r(U_P)$. By (G0) a link that appears once gives zero, so each boundary link must be met by a plaquette that contains it. The cheapest way is to pick, on the four plaquettes inside C, the conjugate fundamental $\chi_{\bar F}(U_P)=\operatorname{tr}U_P^\dagger$, with weight $d_{\bar F}\tilde c_{\bar F}=N\tilde c_F$ (for SU(2), $\chi_{1/2}(U_P)$ with weight $2\tilde c_{1/2}$, and $\operatorname{tr}U_P=\operatorname{tr}U_P^\dagger$). The counterclockwise plaquettes, read from their lower-left corners, are
$$
U_{P_1}=U_{b_1}U_{i_1}U_{i_4}^\dagger U_{b_8}^\dagger,\quad
U_{P_2}=U_{b_2}U_{b_3}U_{i_2}^\dagger U_{i_1}^\dagger,\quad
U_{P_3}=U_{i_2}U_{b_4}U_{b_5}^\dagger U_{i_3}^\dagger,\quad
U_{P_4}=U_{i_4}U_{i_3}U_{b_6}^\dagger U_{b_7}^\dagger,
$$
and the term to evaluate is
$$
T=\frac1N\,(N\tilde c_F)^4\int\prod_\ell dU_\ell\;\operatorname{tr}U_C\,\operatorname{tr}U_{P_1}^\dagger\operatorname{tr}U_{P_2}^\dagger\operatorname{tr}U_{P_3}^\dagger\operatorname{tr}U_{P_4}^\dagger .
$$

*Step 1, link $i_1$.* It occurs in $\operatorname{tr}U_{P_1}^\dagger=\operatorname{tr}(U_{b_1}^\dagger U_{b_8}U_{i_4}\,U_{i_1}^\dagger)$ and in $\operatorname{tr}U_{P_2}^\dagger=\operatorname{tr}(U_{i_1}\,U_{i_2}U_{b_3}^\dagger U_{b_2}^\dagger)$, in opposite directions, and (G1) fuses the two traces:
$$
\int dU_{i_1}\operatorname{tr}U_{P_1}^\dagger\operatorname{tr}U_{P_2}^\dagger=\frac1N\operatorname{tr}\big(U_{b_1}^\dagger U_{b_8}U_{i_4}U_{i_2}U_{b_3}^\dagger U_{b_2}^\dagger\big),
$$
the clockwise holonomy of the lower 2×1 rectangle.

*Step 2, link $i_2$.* The fused trace contains $U_{i_2}$, and $\operatorname{tr}U_{P_3}^\dagger=\operatorname{tr}(U_{i_3}U_{b_5}U_{b_4}^\dagger\,U_{i_2}^\dagger)$ contains $U_{i_2}^\dagger$; (G1) gives
$$
\frac{1}{N^2}\operatorname{tr}\big(U_{b_3}^\dagger U_{b_2}^\dagger U_{b_1}^\dagger U_{b_8}U_{i_4}\,U_{i_3}U_{b_5}U_{b_4}^\dagger\big),
$$
the clockwise holonomy of the L-shaped region $P_1\cup P_2\cup P_3$.

*Step 3, link $i_3$.* With $\operatorname{tr}U_{P_4}^\dagger=\operatorname{tr}(U_{i_3}^\dagger\,U_{i_4}^\dagger U_{b_7}U_{b_6})$, (G1) gives
$$
\frac{1}{N^3}\operatorname{tr}\big(U_{b_5}U_{b_4}^\dagger U_{b_3}^\dagger U_{b_2}^\dagger U_{b_1}^\dagger U_{b_8}\,U_{i_4}U_{i_4}^\dagger\,U_{b_7}U_{b_6}\big).
$$

*Step 4, link $i_4$.* It now appears as $U_{i_4}U_{i_4}^\dagger=1$ and drops out with no factor. The path has reached the central site (1,1) along $i_4$ and returned at once: the index loop closed around that interior site gives back the N that a fourth integral would have cost. What remains is $N^{-3}\operatorname{tr}U_C^\dagger$, with $U_C^\dagger$ the clockwise holonomy of the boundary.

*Step 5, the boundary.* Writing $U_C=U_{b_1}R$, (G1) on $b_1$ turns $\int\operatorname{tr}U_C\operatorname{tr}U_C^\dagger$ into $\frac1N\operatorname{tr}(RR^\dagger)=\frac1N\operatorname{tr}\mathbb 1=1$, after which the other seven boundary links appear only in $RR^\dagger$.

Collecting the factors,
$$
T=\frac1N\,(N\tilde c_F)^4\cdot\frac1{N^3}\cdot1=\tilde c_F^{\,4}.
$$
Every other nonvanishing term has more plaquettes, and the vacuum terms, closed surfaces starting with the six faces of a cube at order $\tilde c^6$, cancel between numerator and denominator except where they touch the tiling (§4.3). Therefore $\langle W_F(C_{2\times2})\rangle=\tilde c_F^4\,[1+O(\tilde c_F^4)]$. The bare integral, $N^{-3}$, was also checked by Monte Carlo sampling of the Haar measure for SU(2) and SU(3).

### 4.2 Every disk weighs the same: the tiling rule [Computed for disks; other topologies Sketched and checked.]

The counting of §4.1 generalizes. Let Σ be a surface of $|\Sigma|$ plaquettes bounded by C, embedded (each link of Σ belongs to exactly two of its plaquettes, or to one plaquette and the loop) and oriented so that every link is traversed once in each direction. Each tile contributes $N\tilde c_F$ times a trace; each link integral, interior or on C, costs $1/N$ by (G1) or (G2); and after all integrations every site of Σ, interior or on C, closes one index loop and gives a factor N, as the central site did in Step 4 and the boundary sites did in Step 5. With V sites, E links and $F=|\Sigma|$ plaquettes the term is
$$
\frac1N\,(N\tilde c_F)^{F}\,N^{-E}\,N^{V}=\tilde c_F^{\,|\Sigma|}\,N^{\chi(\Sigma)-1},\qquad \chi=V-E+F,
$$
where χ is the Euler characteristic. For a disk $\chi=1$, and the term is exactly $\tilde c_F^{|\Sigma|}$, with no dependence on N or on the shape. The same counting with b boundary loops, each normalized by $1/N$, gives $\tilde c_F^{|\Sigma|}N^{\chi-b}$: a sphere without boundary, such as the surface of a cube, gives $N^2\tilde c_F^6$ for each orientation, and an annulus between two loops gives $N^{-2}\tilde c_F^{|\Sigma|}$ (used in §7.6). These values were checked against Monte Carlo evaluations of the bare Haar integrals for the 1×2 and 2×2 disks, the decorated disk of §4.3, the cube and the annulus of §7.6, for SU(2) and SU(3). For a representation r the same argument, with Schur's formula for $D^r$, gives $\tilde c_r^{|\Sigma|}$ for a disk.

The dominant surface is the one of smallest area. For a planar loop it is unique, the flat tiling of area $A(C)$, and
$$
\boxed{\ \langle W_F(C)\rangle=\tilde c_F^{\,A(C)}\big[1+O(\tilde c_F^4)\big],\qquad \sigma=-\ln\tilde c_F .\ }
$$
For the $R\times T$ rectangle, $V(R)=-\lim_{T\to\infty}T^{-1}\ln\langle W\rangle=\sigma R$: a linear potential, in lattice units, for every compact group. At small β, $\sigma\simeq\ln(2/\beta)$ for U(1), $\ln(4/\beta)$ for SU(2) and $\ln(2N^2/\beta)$ for SU(N ≥ 3); at $\beta=1$ the leading values are $0.807$, $1.426$ and, for SU(3), $2.81$.

> **Physical picture.** The selection rules are Gauss's law for the electric flux emitted by the static sources. Flux cannot end on a link, so the sheet of plaquettes that carries it must be a surface bounded by the loop, and each unit of area costs a factor $\tilde c_F$: the string tension is the free energy per unit area of the flux sheet. At strong coupling the sheet is rigid and flat, and nothing in the calculation used the group being abelian, which is why confinement at small β is universal. The statement concerns the lattice theory at large lattice spacing; what the sheet does at larger β, and what survives in the continuum, are §§7.3–7.4.

### 4.3 The first correction: decorated surfaces [Controlled to O(c̃⁴).]

The cheapest surfaces after the flat one are obtained by removing one plaquette p of the minimal surface and replacing it by the other five faces of a unit cube that has p as a face (Figure 2a). The result is again an embedded disk, now with $A+4$ plaquettes, so by §4.2 it contributes $\tilde c_F^{A+4}$ with group factor 1 (the bare integral for the decorated 1×1 loop, $N^{-4}$, was checked for SU(2) and SU(3)). There are A choices of p, and the cube can stand on either side of the plane in each of the $d-2$ transverse directions, $2(d-2)$ choices.

For SU(3), and likewise for $\mathbb Z_3$, a second configuration enters one order later. Keep p in the sheet but let it carry the conjugate representation, and attach the same five-face box with the orientation that runs along $\partial p$ in the same direction as the sheet. On each edge of p three fundamental lines then meet in the same direction, which the ε-tensor of SU(3) allows: $3\otimes3\otimes3$ contains one singlet, so $\int dU\,(\operatorname{tr}U)^3=1$. The box fuses to $N^{-4}\operatorname{tr}U_{\partial p}$, the bare integral is $N^{-4}\int dU(\operatorname{tr}U)^3=1/81$, and the weight relative to the flat sheet is $(3\tilde c_F)^5/81=3\tilde c_F^5$ per location, with the same $2(d-2)A$ locations. For U(1), $\mathbb Z_2$, SU(2) and SU($N\ge4$) the integral $\int(\operatorname{tr}U)^3$ vanishes and the configuration does not contribute (the SU(N) analogue needs N lines on an edge and appears only at much higher order).

![[gs-w06-decorated-surfaces.svg|Left, a flat sheet of plaquettes in which one plaquette p is replaced by the roof and four walls of a unit cube; right, a slice of the sheet with integer heights 0 0 1 1 0 0 -1 0 over the minimal surface and one wall plaquette for each unit step]]

**Figure 2. (a) A decorated surface: one plaquette p of the minimal sheet is replaced by the other five faces of a unit cube, adding four plaquettes. (b) A slice of the sheet in the solid-on-solid picture of §7.3: an integer height h on each plaquette of the minimal surface, and one wall plaquette for every unit step between neighbours.**

Vacuum bubbles cancel between numerator and denominator, apart from configurations that overlap the sheet: for the groups without a cubic invariant, a cube that shares a plaquette or a link with it changes $\ln\langle W\rangle$ at relative order $\tilde c^6$ (for SU(3), the ε-tensor box above is exactly such an overlap, at order $\tilde c^5$). Two decorations appear $\frac12[2(d-2)A]^2$ times at order $\tilde c^8$, minus $O(A)$ overlapping pairs, which is the square of the single-decoration term up to $O(A\tilde c^8)$. The series exponentiates, and
$$
\langle W_F(C)\rangle=\tilde c_F^{\,A}\exp\!\big[\,2(d-2)A\,\tilde c_F^4+O(A\,\tilde c_F^6)\big],\qquad
\boxed{\ \sigma=-\ln\tilde c_F-2(d-2)\,\tilde c_F^4+O(\tilde c_F^6)\ }
$$
for U(1), $\mathbb Z_2$, SU(2) and SU($N\ge4$), while for SU(3) the ε-tensor boxes add one term,
$$
\sigma_{SU(3)}=-\ln\tilde c_F-2(d-2)\,\tilde c_F^4-6(d-2)\,\tilde c_F^5+O(\tilde c_F^6),
$$
which in $d=4$ is the familiar $-\ln u-4u^4-12u^5$ of the SU(3) strong-coupling series.
At this order the decorations shift only the area term: every plaquette of the sheet can carry one, so their number is exactly $2(d-2)A$. Perimeter terms first appear at order $\tilde c^6$, for instance from boxes on a base of two adjacent plaquettes, whose number $2(d-2)(2A-R-T)$ for an $R\times T$ loop has an area part and a perimeter part. For SU(2) in $d=4$ at $\beta=1$, $\sigma=1.426-0.013=1.413$, a one per cent correction; for U(1) at the same β, where $\tilde c_1=0.446$ is larger, the correction is $0.159$ out of $0.807$. The decorations are Wilson's unit cubes attached to the minimal surface (§9) and Kogut's "house" (RMP 55, §IV.A), where $d=3$ gives $\sigma=-\ln\tanh\beta-2\tanh^4\beta$ for $\mathbb Z_2$.

## 5. The continuum limit and the normalization of β [Controlled to O(a²).]

### 5.1 U(1)

Take a smooth gauge field A and put $a_\mu(x)=\int_{\ell_\mu(x)}A$, writing a for $a_{\rm lat}$ in this section. By Stokes, $(da)_P=\oint_{\partial P}A=\int_PF$, and the midpoint rule $\int_{-a/2}^{a/2}\int_{-a/2}^{a/2}f=a^2f(0)+\frac{a^4}{24}(\partial_1^2+\partial_2^2)f(0)+O(a^6)$ (the odd terms vanish by symmetry, and $\int_{-a/2}^{a/2}t^2dt=a^3/12$) gives, about the center $x_P$ of the plaquette,
$$
(da)_P=a^2F_{\mu\nu}(x_P)+\frac{a^4}{24}\big(\partial_\mu^2+\partial_\nu^2\big)F_{\mu\nu}(x_P)+O(a^6).
$$
Then $1-\cos(da)_P=\frac12(da)_P^2-\frac1{24}(da)_P^4+\dots$, and with $\sum_P=\sum_x\sum_{\mu<\nu}$ and $a^d\sum_xf(x_P)\to\int d^dx\,f$ (for a smooth, decaying f the error of this midpoint sum vanishes faster than any power of a),
$$
S=\frac{\beta a^{4-d}}{2}\int d^dx\sum_{\mu<\nu}F_{\mu\nu}^2\,\big[1+O(a^2)\big]=\frac{\beta a^{4-d}}{4}\int d^dx\,F_{\mu\nu}F_{\mu\nu}\,\big[1+O(a^2)\big].
$$
Matching $\frac1{4e^2}\int F_{\mu\nu}F_{\mu\nu}$ of [[courses/generalized-symmetries-course/conventions|conventions]] §4 gives
$$
\boxed{\ \beta=\frac{1}{e^2\,a^{4-d}}\qquad(\text{U}(1)),\ }
$$
with $e^2$ of mass dimension $4-d$. The corrections are $\frac{a^2}{24e^2}\int\sum_{\mu<\nu}F_{\mu\nu}(\partial_\mu^2+\partial_\nu^2)F_{\mu\nu}$, of dimension six, and $-\frac{a^4}{24e^2}\int\sum_{\mu<\nu}F_{\mu\nu}^4$, of dimension eight; for the canonical field $A=eA_c$ they are suppressed by $a^2$ and by $e^2a^4$. A numerical check on a smooth field confirms that the relative error of the expansion of $(da)_P$ drops from $O(a^2)$ to $O(a^4)$ once the $a^4/24$ term is kept.

### 5.2 SU(N)

With $U_\ell=\mathcal P\exp(i\int_\ell A)$, $A=A^aT^a$ and $\operatorname{tr}T^aT^b=\frac12\delta^{ab}$, write each link as $U_\mu(x)=\exp[iaA_\mu(x+\frac a2\hat\mu)+O(a^3)]$ and combine the four factors of $U_P$ with $e^Xe^Y=e^{X+Y+\frac12[X,Y]+\dots}$. The abelian parts add up to $ia^2(\partial_\mu A_\nu-\partial_\nu A_\mu)$, and the group commutator $e^{iaA_\mu}e^{iaA_\nu}e^{-iaA_\mu}e^{-iaA_\nu}=e^{-a^2[A_\mu,A_\nu]+O(a^3)}$ supplies the rest, so that
$$
U_P=\exp\!\big\{ia^2F_{\mu\nu}+O(a^3)\big\},\qquad F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+i[A_\mu,A_\nu].
$$
Write $U_P=e^{iX_P}$ with $X_P$ hermitian. Then $\operatorname{Re}\operatorname{tr}(1-U_P)=\operatorname{tr}(1-\cos X_P)=\frac12\operatorname{tr}X_P^2-\frac1{24}\operatorname{tr}X_P^4+\dots$, and
$$
\operatorname{tr}X_P^2=a^4\operatorname{tr}F_{\mu\nu}(x_P)^2+O(a^6),
$$
with no $O(a^5)$ term. Such a term would be built from $A_\mu$, $A_\nu$ and their in-plane derivatives with an odd number of in-plane indices, so it would change sign under the rotation by π about $x_P$ in the $(\mu,\nu)$ plane; that rotation maps the plaquette onto itself with its orientation, and $\operatorname{tr}X_P^2$, a class function of $U_P$, is invariant under it. [Checked numerically for a smooth SU(2) field: $\operatorname{Re}\operatorname{tr}(1-U_P)\big/\big(\frac{a^4}2\operatorname{tr}F^2\big)-1$ is $-0.043$, $-0.011$ and $-0.0028$ at $a=0.2,0.1,0.05$, and fails to converge if the sign of the commutator in F is reversed.] Summing over plaquettes,
$$
S=\frac\beta N\sum_P\operatorname{Re}\operatorname{tr}(1-U_P)=\frac{\beta a^{4-d}}{2N}\int d^dx\sum_{\mu<\nu}\operatorname{tr}F_{\mu\nu}^2\,\big[1+O(a^2)\big]=\frac{\beta a^{4-d}}{4N}\int d^dx\,\operatorname{tr}F_{\mu\nu}F_{\mu\nu}\,\big[1+O(a^2)\big],
$$
and matching $\frac{1}{2g^2}\int\operatorname{tr}F_{\mu\nu}F_{\mu\nu}=\frac1{4g^2}\int F^a_{\mu\nu}F^a_{\mu\nu}$ of [[courses/generalized-symmetries-course/conventions|conventions]] §4 gives
$$
\boxed{\ \beta=\frac{2N}{g^2\,a^{4-d}}\quad(\text{SU}(N)),\qquad\text{that is,}\quad \beta=\frac{2N}{g^2}\ \text{ in } d=4 .\ }
$$
The factor 2N is specific to SU(N): it comes from $\operatorname{tr}T^aT^b=\frac12\delta^{ab}$ and the $1/N$ in front of the action. The U(1) link $e^{ia}$ is generated by the number 1, whose square is 1; setting $N=1$ in the SU(N) formula, $\beta=2/e^2$, would produce $\frac{1}{2e^2}\int F_{\mu\nu}F_{\mu\nu}$, twice the Maxwell action of the conventions, that is, a unit Wilson line of charge $e/\sqrt2$; this is why the two formulas are never interchanged.

### 5.3 What the classical limit shows

The expansion above is classical: it shows that Wilson's action reproduces the continuum action on smooth fields, with irrelevant corrections. In the quantum theory the typical plaquette angle at weak coupling is of order $\beta^{-1/2}$, so the expansion in $X_P$ is the weak-coupling expansion, and the continuum limit is taken by sending $a\to0$ with β adjusted to keep physical quantities fixed. In $d=3$ this means $\beta=1/(e^2a)\to\infty$ at fixed $e^2$. In $d=4$ it means $\beta\to\infty$ for SU(N), by asymptotic freedom (§7.4), and a finite β inside the Coulomb phase for U(1) ([[week-11-monopole-condensation-4d|Week 11]]). Either way, the strong-coupling results of §4 describe the lattice theory at large lattice spacing, where the irrelevant terms are as large as the leading one.

## 6. Creutz ratios and the handoff to Monte Carlo [Computed.]

The rectangular loop contains more than the area term. The self-energy of the static sources gives a term proportional to the perimeter (in the continuum it diverges like $1/a$), and the corners give a constant. At any coupling we may write
$$
-\ln\langle W(I,J)\rangle=\sigma IJ+f(I)+g(J)+\epsilon(I,J),
$$
where f and g collect everything that depends on one side only (perimeter, corners, constants) and ε is the rest, for instance a Coulomb-like term. Creutz's ratio (he wrote χ; we write R to keep χ for characters),
$$
R(I,J)=-\ln\frac{\langle W(I,J)\rangle\,\langle W(I-1,J-1)\rangle}{\langle W(I,J-1)\rangle\,\langle W(I-1,J)\rangle},
$$
removes f and g exactly, since $f(I)+f(I-1)-f(I)-f(I-1)=0$ and likewise for g. The area terms combine to $\sigma[IJ+(I-1)(J-1)-I(J-1)-(I-1)J]=\sigma$, so that
$$
R(I,J)=\sigma+\big[\epsilon(I,J)+\epsilon(I-1,J-1)-\epsilon(I,J-1)-\epsilon(I-1,J)\big],
$$
where the bracket is a mixed second difference of ε, which falls off for large loops (for $\epsilon=-\alpha J/I$ it is $\alpha/I(I-1)$). At strong coupling, with $W(I,0)=W(0,J)=1$, §§4.2–4.3 give $R(I,J)=-\ln\tilde c_F-2(d-2)\tilde c_F^4+O(\tilde c_F^6)$ for all $I,J\ge1$ (with $-6(d-2)\tilde c_F^5$ added for SU(3)); at higher orders the numbers of excitations take the form $aIJ+bI+cJ+e$ once the loop is large enough to contain them, so R isolates the area coefficient order by order. Creutz used these ratios in the first Monte Carlo study of SU(2) and found them crossing over, at intermediate β, from the strong-coupling behaviour to the scaling expected from asymptotic freedom [Stated — refs: Creutz, PRD 21 (1980) 2308]: numerical evidence that no phase transition separates the two regimes in $d=4$. The course leaves the numerical route here; its later weeks use the lattice for exact dualities and phase structure.

## 7. Subtleties and fine print

**7.1 Gauge covariance, base points and the real part.** Only class functions of closed holonomies are observable (§1.2). This is why the plaquette enters the action through a character, why the action takes the real part (plaquettes are unoriented), and why the continuum field strength appears only through $\operatorname{tr}F^2$: $F_{\mu\nu}$ transforms by conjugation, like $U_P$, and for $N\ge2$ neither is invariant. For U(1), $U_P$ and F are invariant, a special feature of the abelian group.

**7.2 Gauge fixing is allowed and never needed [Proved.]** The gauge group of the lattice theory is a product of one copy of G per site, compact, with total Haar volume 1, so the integral over link variables is finite without gauge fixing and no Faddeev–Popov procedure is required; this is what Wilson meant by treating the gauge fields as angular variables. Gauge fixing is nevertheless allowed. Choose a maximal tree T, a set of links that contains no closed loop and reaches every site. For fixed tree links there is a unique gauge transformation with $g=1$ at a root site that sets them to 1: move out from the root along the tree with $g_{x+\hat\mu}=g_xU_\mu(x)$. For a gauge-invariant f, write $\int\prod_\ell dU_\ell\,f=\int\prod_{\ell\in T}dU_\ell\int\prod_{\ell\notin T}dU_\ell\,f(U)$. In the inner integral replace $f(U)$ by $f(U^g)$ with the tree-trivializing g. Since g depends only on the tree links, $U_\ell\to g_xU_\ell g_y^{-1}$ is, for each link off the tree, a left and a right multiplication by fixed elements, which preserves the Haar measure. The inner integral therefore equals its value at $U_T=1$, independently of the tree links, and the outer integral gives 1:
$$
\int\prod_\ell dU_\ell\,f(U)=\int\prod_{\ell\notin T}dU_\ell\;f(U)\Big|_{U_\ell=1,\ \ell\in T}.
$$
The axial gauge is the case of a comb-shaped tree. The Jacobian is 1, and no gauge-invariant quantity changes; in $d=2$ with open boundaries the remaining links correspond one to one to the plaquettes, and Problem 4 turns this into an exact solution.

**7.3 The radius of convergence and roughening.**

*What converges.* The logarithm of Z per site and the string tension $\sigma(\beta)$ are given at small β by convergent expansions in the coefficients $\tilde c_r$: the number of connected surfaces of n plaquettes grows at most exponentially in n, and each weighs $\tilde c^n$ times a bounded group factor. Osterwalder and Seiler proved the convergence, and the area law at small β, for every compact gauge group [Stated — refs: Osterwalder–Seiler 1978; Kogut RMP 55 §IV.A].

*The sheet as a height model.* In the regime of §4.3 the relevant surfaces are the flat sheet with bumps. Neglecting overhangs and closed bubbles (the solid-on-solid approximation), a surface over the minimal one in $d=3$ is described by an integer height $h_x$ on each plaquette x of the minimal surface, with $h=0$ outside the loop, and its area is $A+\sum_{\langle xy\rangle}|h_x-h_y|$, one wall plaquette per unit step between neighbouring columns (Figure 2b). Every such surface is an embedded disk, so by §4.2 it weighs $\tilde c_F$ to the power of its area, and
$$
\langle W_F(C)\rangle\simeq\tilde c_F^{\,A}\,Z_{\rm SOS},\qquad
Z_{\rm SOS}=\sum_{\{h\}}\exp\Big(-K\sum_{\langle xy\rangle}|h_x-h_y|\Big),\qquad K=-\ln\tilde c_F,
$$
the absolute-value solid-on-solid model at coupling K. Its lowest excitation, $h_x=\pm1$ on one site, has four steps and weight $2\tilde c_F^4$ per site: the decorations of §4.3 in $d=3$. In $d=4$ the height becomes a two-component transverse displacement.

*Roughening.* At large K (small β) the surface is smooth, its height fluctuations are bounded, and the expansion in $e^{-K}$ converges. At a finite coupling $K_R$ it roughens: the height fluctuations grow logarithmically with the size of the surface, and its free energy has an essential singularity of the form $\exp(-B/\sqrt{T-T_R})$ at the transition [Stated — refs: Kogut RMP 55 §V.C]. This is the transition of the height model of [[week-03-villain-form-xy-duality|Week 3]] §3, which by Poisson duality is the BKT transition of the XY model seen from the height side (Chui–Weeks), now appearing on the confining string. For the gauge theory it means that $\sigma(\beta)$ is non-analytic at a roughening coupling $\beta_R$, and that the strong-coupling expansions have a radius of convergence bounded by the roughening point [Stated — refs: Kogut RMP 55 §V.C and the papers cited there].

*What roughening changes.* It is a transition of the flux sheet alone, visible only in large Wilson loops; the bulk free energy is analytic there, and σ stays positive on both sides, so confinement persists. What changes is the geometry of the flux tube. In the rough phase its mean-square width grows logarithmically with its length, its transverse fluctuations are massless and add the universal term $-\frac{(d-2)\pi}{24R}$ to the potential [Stated — refs: Kogut RMP 55 §V.B], and the rotational symmetry of the static potential is restored at long distances (§V.C there). In the 3d $\mathbb Z_2$ gauge theory, whose flux sheet is the interface of the dual Ising model of Week 5, the interface roughens at $T_R\approx\frac12T_c$ of the Ising model, deep inside the confining region of the gauge theory [Stated — refs: Kogut RMP 55 §V.C, Fig. 40].

**7.4 Why strong coupling cannot see asymptotic freedom.** For SU(N) in $d=4$, asymptotic freedom puts the continuum limit at $g\to0$, that is $\beta\to\infty$, where the lattice spacing in physical units vanishes as $a\Lambda\propto e^{-1/(2b_0g^2)}$ with $b_0=11N/48\pi^2$ at one loop [Stated — refs: Kogut RMP 51 §VIII.B; Kogut RMP 55 §§II.A, IV.D]. With $g^2=2N/\beta$ this reads
$$
\sigma a^2\ \propto\ (a\Lambda)^2\ \propto\ \exp\Big(-\frac{\beta}{2Nb_0}\Big)=\exp\Big(-\frac{24\pi^2}{11N^2}\,\beta\Big),
$$
which is $e^{-8\pi^2\beta/33}$ for SU(3). Three facts keep the strong-coupling series away from this regime. The series is defined near $\beta=0$ and has a finite radius, bounded by the roughening point (§7.3), so it cannot be continued to large β. Its truncations decrease only logarithmically, $\sigma\simeq\ln(2N^2/\beta)$, where the continuum limit requires an exponential decrease. And inside its domain σ is of order one or larger in lattice units, so correlation lengths are at most a lattice spacing and rotational invariance is broken: there is no continuum physics there to see. What strong coupling does establish is that the lattice theory confines at small β for every compact group. The continuum statement needs in addition the absence of a phase transition between small and large β, which Monte Carlo supports for SU(N) (§6) and nobody has proved.

**7.5 Representation dependence and a preview of N-ality.** The leading term $\langle W_r(C)\rangle=\tilde c_r^{A}$ is the first term for a loop of fixed size as $\beta\to0$, and for higher representations it fails to describe large loops. The adjoint of SU(N) is contained in $F\otimes\bar F$, so a closed tube of fundamental plaquettes running along C, with C drawn on its surface (Figure 3), is allowed by the selection rules: at each link of C the adjoint of the loop and the F and $\bar F$ of the two tube plaquettes that contain the link combine into the singlet, once. The smallest such tube is the surface of the ring of $2(R+T)-4$ unit cubes that lines the inside of an $R\times T$ loop; each cube of the ring exposes four faces, so the tube has $4P-16$ plaquettes, with $P=2(R+T)$. It gives a perimeter law $\propto\tilde c_F^{4P-16}$, while the adjoint sheet gives $\tilde c_{\rm adj}^A\sim\tilde c_F^{2A}$ (§3.5), and for large loops the tube wins. The adjoint charge is screened by gluons, and at leading logarithmic order the crossover sits where $2A\simeq4P-16$, at square loops of side about 7 [Sketched; the group factor of the tube is Problem 5⋆].

![[gs-w06-adjoint-tube.svg|Cross-section of the ring of unit cubes that lines the inside of the loop, with the links of C seen end-on as asterisks at the outer lower corners of the two end cubes, where the tube faces carrying F and F-bar meet]]

**Figure 3. The tube that screens the adjoint loop, in cross-section. A ring of unit cubes lines the inside of the loop; its surface is a torus of fundamental plaquettes that passes through every link of C (marked \*), where the adjoint combines with F and F̄ into a singlet.**

The general mechanism is the center. The element $z=e^{2\pi i/N}$ acts on a representation with $k_r$ boxes (mod N) as $z^{k_r}$, its N-ality, and the selection rule of §2.3 says that sheets of plaquettes may change representation along the way while their N-ality stays fixed. Gluons, of N-ality 0, can therefore screen any representation down to the lightest one of the same N-ality, and loops of N-ality 0 obey a perimeter law at large size. This is the local form of the electric $\mathbb Z_N$ 1-form (center) symmetry of pure SU(N) gauge theory, under which Wilson lines carry the charge $k_r$; the area law of the fundamental loop says that this symmetry is unbroken ([[courses/generalized-symmetries-course/conventions|conventions]] §6, [[higher-form-symmetries]]; [[week-14-fradkin-shenker-order-parameters|Week 14]] and Semester II Block 1). For U(1) the electric 1-form symmetry is U(1) itself, there are no charged gauge bosons, and every charge is conserved; even so, the flat sheet of charge 2 is not the cheapest surface for a large loop in $d\ge3$ (Problem 9⋆⋆). Finally, Casimir scaling of the leading coefficient depends on the action: it holds for the heat-kernel action (Problem 6⋆) and in the Hamiltonian strong-coupling limit of Week 7, where $\sigma=\frac{g^2}2C_2(F)$ ([[courses/generalized-symmetries-course/conventions|conventions]] §4), and it fails for the Wilson action (§3.5).

**7.6 The Polyakov line at finite temperature.** Make Euclidean time periodic with $N_\tau$ sites, so that $T=1/(N_\tau a)$, and define the Polyakov loop $L(\vec x)=\frac1N\operatorname{tr}\prod_{t=0}^{N_\tau-1}U_0(\vec x,t)$ (often written P; we keep P for plaquettes). Multiply every time-like link on one time slice by $z=e^{2\pi i/N}$. Each plaquette that contains one of these links contains exactly one more, traversed in the opposite direction, so the action is invariant, while $L\to zL$. Therefore $\langle L\rangle=z\langle L\rangle$ vanishes unless this center symmetry is broken spontaneously. Every term of the strong-coupling expansion obeys the selection rule, so $\langle L\rangle=0$ order by order: the expansion cannot show $\langle L\rangle\ne0$, and the deconfinement transition at high temperature lies outside its radius of convergence. The correlator is computable. For $\vec x$ and $\vec y$ at distance r along an axis, the strip of $N_\tau r$ time-like plaquettes between the two lines is an annulus bounded by the two loops (tiles oriented against the lines), and §4.2 gives
$$
\langle L(\vec x)\,L(\vec y)^\dagger\rangle=\frac{1}{N^2}\,\tilde c_F^{\,N_\tau r}\,\big[1+\dots\big]
$$
(without the $1/N^2$ for U(1)), so the free energy of a static pair, $F_{q\bar q}(r)=-T\ln\langle LL^\dagger\rangle=\sigma r+2T\ln N$ in lattice units ($TN_\tau=1$), rises linearly with the zero-temperature tension. As $N_\tau$ decreases, the effective coupling between neighbouring Polyakov lines, $\tilde c_F^{N_\tau}$ at leading order, grows until the center symmetry breaks: this is deconfinement, whose universality class, when the transition is continuous, is that of a $\mathbb Z_N$ spin model in $d-1$ dimensions [Stated — refs: Svetitsky–Yaffe 1982]. Week 14 returns to it.

**7.7 Phase structure by group and dimension.** Figure 4 collects what is known and what is expected. In $d=2$ the tiling is exact for every group (Problem 4): an area law at every β, and no roughening, since the sheet has no transverse direction. In $d=3$ compact U(1) confines at every coupling, at weak coupling through Polyakov's monopole plasma ([[week-09-compact-qed3-monopole-plasma|Week 9]] and [[week-10-polyakov-mass-gap-area-law|Week 10]], on the dual variables of [[week-08-dual-variables-abelian-gauge|Week 8]]) and for the Villain action at all couplings by a theorem [Stated — refs: Göpfert–Mack 1982]; in the language of [[courses/generalized-symmetries-course/conventions|conventions]] §6, its electric $U(1)^{(1)}$ symmetry is unbroken at every coupling. In $d=4$ compact U(1) has a Coulomb phase at large β, with a massless photon and a perimeter law, in which the electric 1-form symmetry is spontaneously broken [Stated — refs: Guth 1980 for the Villain action; Fröhlich–Spencer 1982]; a transition separates it from the confined phase. For SU(N) in $d=4$ no bulk transition is expected between the strong-coupling region and the continuum limit at $\beta\to\infty$, on the evidence of Monte Carlo, and the only non-analyticity expected along the way at zero temperature is the roughening of the flux sheet.

![[gs-w06-phase-structure.svg|Three beta axes, for U(1) in d=3, U(1) in d=4 and SU(N) in d=4, showing the confined regions, the Coulomb phase above the critical coupling, the roughening point, and the small-beta region where the strong-coupling series converges]]

**Figure 4. Phase structure in β at zero temperature. "Series" marks the small-β region where the strong-coupling expansion converges; $\beta_R$ is the roughening of the flux sheet (§7.3), a transition of the string that leaves the bulk analytic, drawn only for SU(N), where §7.3 cites it; $\beta_c$ is the transition of 4d compact U(1). Positions along the β axes are schematic.**

## 8. Common misconceptions

- **"The strong-coupling area law proves that QCD confines."** It is tempting because the area law at small β is a theorem, and it holds for SU(3). The theorem concerns the lattice theory at large lattice spacing. The continuum limit of SU(N) in $d=4$ is at $\beta\to\infty$, beyond the radius of convergence (§§7.3–7.4), and the same computation gives an area law for 4d compact U(1), whose continuum limit is Maxwell theory with a Coulomb potential. Confinement in the continuum requires in addition that no phase transition intervene, which Monte Carlo supports for SU(N) and nobody has proved.
- **"The Haar measure needs gauge fixing, as the continuum path integral does."** The continuum intuition comes from gauge orbits of infinite volume. On the lattice the orbits are compact, of volume 1 per site, and the unfixed integral is finite; gauge fixing on a maximal tree is allowed, with unit Jacobian (§7.2), and changes no gauge-invariant quantity.
- **"SU(2) and U(1) are the cases N = 2 and N = 1 of the SU(N) formulas."** The actions look alike, and the groups differ exactly where it matters. The SU(2) fundamental is pseudo-real, so $\tilde c_{1/2}\simeq\beta/4$, twice $\beta/2N^2$ at $N=2$ (§3.3); $\mathbb Z_2$, whose charge is real, shows the same doubling against $\mathbb Z_{N\ge3}$ (Problem 3). The U(1) charge normalization fixes $\beta=1/e^2$ in $d=4$, and $\beta=2N/g^2$ at $N=1$ would double the Maxwell term (§5.2).
- **"At strong coupling, string tensions obey Casimir scaling."** Casimir scaling is seen in simulations at intermediate distances and holds in the Hamiltonian strong-coupling limit, which makes the statement plausible. For the Wilson action the leading coefficient counts fundamental factors, $\sigma_1/\sigma_{1/2}\to2$ for SU(2) (§3.5); Casimir scaling of the leading coefficient belongs to the heat-kernel action (Problem 6⋆); and for large loops the tension depends only on the N-ality (§7.5).

## 9. Historical note

Wilson's "Confinement of quarks" (*Phys. Rev. D* 10 (1974) 2445) looked for a mechanism that keeps quarks bound, modelled on Schwinger's two-dimensional electrodynamics. Its §III formulates a gauge theory on a four-dimensional Euclidean lattice, with the gauge field on links as an angular variable, periodic with period 2π, which, in Wilson's words, "makes a gauge-fixing term unnecessary". The paper works out a single abelian gauge field coupled to quarks, with a cosine of the plaquette angle as the action, and treats the non-abelian case in a few lines: the link becomes a group element, the integrations become compact group integrations, and the plaquette action is written with the adjoint representation, with the remark that any representation would do. Its §IV develops the strong-coupling expansion. The gauge-field average of a closed quark path vanishes unless elementary squares fill a surface bounded by the path, so it falls exponentially with the minimal enclosed area, as $(g^2)^{-A}$ in lattice units; unit cubes attached to the minimal surface give about as many extra terms at the next order as the surface has plaquettes, so the expansion has to be organized for the logarithm of the loop; and the sum over surfaces has the structure of the string models of hadrons of the time. Wilson was explicit about the limits: the strong-coupling limit is far from Lorentz invariant, and for the abelian theory he expected a phase transition at intermediate coupling to a phase of massless photons and free charges. The character-expansion machinery of this week was systematized in the following years (reviewed by Drouffe and Itzykson in 1978), Osterwalder and Seiler proved the convergence of the expansion in 1978, and whether SU(N) has a transition between strong and weak coupling was taken up by Monte Carlo, starting with Creutz in 1980.

## 10. What to take away

1. **Haar measure plus Schur's lemma is a graphical calculus.** A link integrates to zero unless its representations contain the singlet, two traces sharing a link fuse at the cost $1/N$, and the center turns this into an N-ality selection rule, which the pseudo-real SU(2) and the abelian U(1) satisfy in their own ways.
2. **The character coefficients are computed.** $\tilde c_n=I_n/I_0\simeq\beta/2$ for U(1), $\tilde c_{1/2}=I_2/I_1\simeq\beta/4$ for SU(2) and $\tilde c_F\simeq\beta/2N^2$ for SU(N ≥ 3); a representation first reached with $n_r$ fundamental factors has $\tilde c_r=O(\beta^{n_r})$.
3. **The area law is a tiled disk.** Every embedded disk of fundamental plaquettes weighs exactly $\tilde c_F^{|\Sigma|}$, the powers of N cancelling through the Euler characteristic; therefore $\langle W_F\rangle=\tilde c_F^{A}(1+\dots)$ and $\sigma=-\ln\tilde c_F-2(d-2)\tilde c_F^4+O(\tilde c_F^6)$ for U(1), $\mathbb Z_2$, SU(2) and SU($N\ge4$); for SU(3) the baryon vertex adds $-6(d-2)\tilde c_F^5$.
4. **The coupling is fixed by the continuum limit.** Wilson's action tends to $\frac1{4e^2}\int F^2$ with $\beta=1/e^2a^{4-d}$ for U(1) and to $\frac1{2g^2}\int\operatorname{tr}F^2$ with $\beta=2N/g^2a^{4-d}$ for SU(N), with $O(a^2)$ corrections; Creutz ratios remove the perimeter and corner terms exactly.
5. **Strong coupling proves lattice confinement at small β, and the rest is dynamics.** Roughening bounds the series, the continuum limit of SU(N) sits at $\beta\to\infty$, and the group and the dimension decide what happens in between: 3d U(1) confines at every coupling, 4d U(1) has a Coulomb phase, and 4d SU(N) is believed to confine at every coupling.

## 11. Looking ahead: Week 7

We have the Euclidean picture. [[week-07-kogut-susskind-hamiltonian|Week 7]] makes time continuous: the anisotropic lattice, its transfer matrix and the limit that yields the Kogut–Susskind Hamiltonian, with link rotors, the electric field as their conjugate, and the Gauss law as an operator constraint. The character basis of this week becomes the electric-flux basis there, the strong-coupling flux sheets become electric strings whose energy per unit length is $\frac{g^2}{2}C_2(r)$, and the $\mathbb Z_2$ Hamiltonian turns out to be the toric code one renaming away, planted for Semester II.

## 12. Problem set

Problems 1–4 are the classroom core and are solvable from the note alone; Problems 5⋆–7⋆ are self-study consolidation, each with a hint or an indicated method; Problems 8⋆⋆ and 9⋆⋆ are research extensions that state what is known, what is explored, the sources they need and what counts as completion.

**Core problems** (everyone).

**1. The 1×2 loop by hand.**
(a) For SU(N) with $N\ge3$, label the seven links of the 1×2 rectangle and its two tiles as in Figure 1, integrate the shared link and then the boundary links with (G1) and unitarity, and show that the leading term of $\langle W_F\rangle$ is $\tilde c_F^2$, accounting for every power of N. (b) Repeat with one tile reversed ($\operatorname{tr}U_P$ in place of $\operatorname{tr}U_P^\dagger$) and show that the result vanishes for $N\ge3$ and not for SU(2); explain both with §2.3. (c) Count the decorated surfaces of §4.3 on the 1×2 loop in d dimensions and show that $\langle W_{1\times2}\rangle=\tilde c_F^2[1+4(d-2)\tilde c_F^4+O(\tilde c_F^6)]$ for SU(2) and SU($N\ge4$), and that for SU(3) the ε-tensor boxes of §4.3 add $12(d-2)\tilde c_F^5$ inside the bracket. (d) For SU(2) in $d=4$, evaluate the Creutz ratio $R(1,2)$ from $W(1,1)$, $W(1,2)$ and $W(0,J)=1$ at $\beta=1$ and $\beta=2$, and compare with σ of §4.3.

**2. SU(2) class integrals and higher representations.**
(a) With the class measure of §2.2, compute $\int dU\,\chi_{1/2}^3\chi_{3/2}$ and $\int dU\,\chi_1^3$, and interpret each as a count of singlets. (b) Expand $e^{\frac\beta2\chi_{1/2}}$ to second and third order and obtain $\tilde c_1\simeq\beta^2/24$ and $\tilde c_{3/2}\simeq\beta^3/192$ without Bessel functions; compare with $I_3/I_1$ and $I_4/I_1$ at $\beta=0.1$ and $\beta=1$. (c) Show that $-\ln\tilde c_j/(-\ln\tilde c_{1/2})\to2j$ as $\beta\to0$, and find the leading correction to this limit.

**3. Character coefficients of $\mathbb Z_N$.**
For the $\mathbb Z_N$ theory with $U_\ell=e^{2\pi ik_\ell/N}$ and $S_P=\beta\big(1-\cos(2\pi k_P/N)\big)$: (a) show that the characters are $e^{2\pi ink/N}$, $n=0,\dots,N-1$, and write $\tilde c_n(\beta)$ as a finite sum; (b) show that $N=2$ gives $\tanh\beta$ (Week 5), that $N=4$ gives $\tilde c_1=\tanh(\beta/2)$, and that $\tilde c_n\to I_n/I_0$ as $N\to\infty$ at fixed n; (c) show that $\tilde c_1\simeq\beta/2$ at small β for $N\ge3$, against $\tanh\beta\simeq\beta$ for $N=2$, and relate the factor 2 to §3.3.

**4. Two dimensions: the tiling is exact.**
On an open $L\times L$ lattice in $d=2$: (a) take as maximal tree all vertical links together with the horizontal links of the bottom row, and use §7.2 to set them to 1; (b) show that the plaquette variables are then $U_P(x,y)=U_h(x,y)\,U_h(x,y+1)^\dagger$ in terms of the remaining horizontal links, that the change of variables to plaquettes preserves the Haar measure, and that the plaquettes are independent; (c) conclude that $\langle W_r(C)\rangle=\tilde c_r^{A(C)}$ exactly, at every β and for every loop, and evaluate it for SU(2) at $\beta=2$ for the 1×1, 1×2 and 2×2 loops; (d) explain why there is neither roughening nor a Coulomb phase in $d=2$.

**Starred problems** (Ph.D. expected; ambitious M.Sc. encouraged).

**5⋆. The adjoint loop and its screening.**
(a) Show that the adjoint loop has the leading area term $\tilde c_{\rm adj}^{A}$, with $\tilde c_{\rm adj}\simeq\beta^2/4N^2(N^2-1)$ for $N\ge3$ and $\tilde c_1\simeq\beta^2/24$ for SU(2). (b) Construct the tube of Figure 3 for an $R\times T$ loop with $R,T\ge3$, show that the selection rules allow it, and verify that it has $4P-16$ plaquettes. (c) Write the contribution of the tube as $\kappa^{P}\tilde c_F^{4P-16}$ times a constant, with κ a nonzero group-theory factor per unit length that does not depend on the loop, and show that for any such κ the tube dominates the area term for large loops; find the crossover size of square loops at leading logarithmic order. (d) Explain why no such tube screens the fundamental loop of SU(N), and why nothing screens the charge-q loops of U(1). (Hint: $F\otimes\bar F=1\oplus{\rm adj}$ and ${\rm adj}\otimes F\otimes\bar F$ contains the singlet once; for (d) use the center rule of §2.3.)

**6⋆. The heat-kernel action and Casimir scaling.**
Take as plaquette weight the heat kernel on G at time τ, $e^{-S_P(U)}=\sum_rd_r\chi_r(U)\,e^{-\frac\tau2C_2(r)}$. (a) Show that $\tilde c_r=e^{-\tau C_2(r)/2}$ exactly, so that the leading coefficient obeys Casimir scaling at every τ, with the SU(2) ratios $8/3$ and $5$. (b) For U(1), where $C_2(n)=n^2$, use the periodic-Gaussian identity of [[courses/generalized-symmetries-course/conventions|conventions]] §3 to show that the heat kernel at $\tau=1/\beta$ is the Villain weight $\sum_ne^{-\frac\beta2(\phi-2\pi n)^2}$ up to normalization (Week 1 §6.2). (c) Match τ to β for SU(2) at weak coupling by comparing $e^{-3\tau/8}$ with the large-β form of $I_2/I_1$ (use the asymptotic form of Week 1 §5.2), and find $\tau\simeq4/\beta$. (d) Explain, with §7.5, why neither box counting nor Casimir scaling of the leading coefficient fixes the tension of very large loops.

**7⋆. The U(1) plaquette to ninth order.**
For U(1) every character coefficient is positive, and a configuration of integer plaquette charges contributes whenever the charge is conserved at every link; on the infinite lattice every closed 2-chain is the boundary of an integer combination of cubes. (a) Show that $\langle W_{1\times1}\rangle=u+2(d-2)\big[u^5(1+u_2)-2u^7\big]+O(u^9)$, with $u=I_1/I_0$ and $u_2=I_2/I_0$, identifying the cube that removes the plaquette, the cube that doubles its charge, and the vacuum cubes that the plaquette excludes. (b) Show that the $O(u^9)$ term is $10(d-2)(2d-5)\,u^9$, from pairs of face-adjacent cubes. (c) Evaluate the series at $\beta=0.5$ in $d=3$ and $d=4$. (Hint: write numerator and denominator as sums over integer cube charges h; the terms in which h does not touch the plaquette cancel exactly.)

**⋆⋆ problems** (research extension; optional).

**8⋆⋆. Roughening from the strong-coupling side.**
*What is known.* At strong coupling the flux sheet of the fundamental loop is, up to overhangs and bubbles, the absolute-value solid-on-solid model of §7.3 with $K=-\ln\tilde c_F$; solid-on-solid models roughen through a transition of BKT type, dual to the XY model (Week 3 §3, Chui–Weeks); for the 3d $\mathbb Z_2$ gauge theory the flux sheet is the Ising interface, which roughens at $T_R\approx\frac12T_c$ (Kogut RMP 55 §V.C and the papers cited there). *What is explored.* How well the solid-on-solid picture locates the roughening coupling of a gauge theory. (a) Derive the solid-on-solid weights for the 3d $\mathbb Z_2$ or U(1) flux sheet, and list the configurations the model omits with the order in $\tilde c$ at which each first appears. (b) Estimate $K_R$ of the absolute-value model by a Monte Carlo simulation, from the logarithmic growth of the height variance with the linear size of the surface. (c) Translate $K_R$ into $\beta_R$ for $\mathbb Z_2$ through $\tanh\beta_R=e^{-K_R}$ and compare with the Ising-interface value, using the duality $\tanh\beta=e^{-2K^*}$ of [[courses/generalized-symmetries-course/conventions|conventions]] §4. *Completion:* the derivation of (a) with the list; $K_R$ with an error bar from at least three lattice sizes; and the comparison of (c), with a statement of which omitted configurations could account for the difference.

**9⋆⋆. Charge-2 flux sheets in U(1).**
*What is known.* At leading order $\langle W_2(C)\rangle\simeq\tilde c_2^{A}$ with $\tilde c_2=I_2/I_0$ (§3.2), and $\tilde c_1^2>\tilde c_2$ at every $\beta>0$, an instance of the Turán-type inequalities $I_1^2>I_0I_2$ for modified Bessel functions (checked numerically for these notes). *What is explored.* Whether the flat charge-2 sheet or two unit sheets dominate large charge-2 loops in $d\ge3$. (a) In $d=3$, compare the flat charge-2 sheet with the configuration in which one unit of flux leaves the plane along the walls of a box of height one over the loop and closes along its lid, of weight $\tilde c_1^{2A+P}$; show that the second wins for large loops and find the crossover side of a square loop at $\beta=0.5$. (b) Using the positivity of all terms of the U(1) expansion, argue that the tension of large charge-2 loops lies below $-\ln\tilde c_2$ at small β, and estimate by how much. (c) Compare with the weak-coupling behaviour of charge-q loops in 3d compact QED (Week 10). *Sources:* the strong-coupling methods of Drouffe–Itzykson, Phys. Rep. 38 (1978) 133, and Week 10 for (c). *Completion:* (a) with the crossover size; (b) as an argument that states its assumptions about the cancellation of vacuum bubbles; (c) a paragraph built on the relevant formula of Week 10.

## Self-study answer checkpoints

These checkpoints cover the core problems; starred and ⋆⋆ problems remain source-led.

1. **The 1×2 loop.** The decisive step is the shared link, which appears in $\operatorname{tr}U_{P_1}^\dagger$ and $\operatorname{tr}U_{P_2}^\dagger$ in opposite directions; (G1) fuses the two traces into $\frac1N\operatorname{tr}U^\dagger_{P_1\cup P_2}$, and the boundary then gives $\frac1N\operatorname{tr}\mathbb 1=1$ as in Step 5 of §4.1. The result is $\frac1N(N\tilde c_F)^2\cdot\frac1N=\tilde c_F^2$, in agreement with the Euler count ($V=6$, $E=7$, $F=2$, $\chi=1$). With one tile reversed, the shared link appears twice in the same direction, and the center rule ($p-q=\pm2$) kills the integral for $N\ge3$; for SU(2), $\operatorname{tr}U_P=\operatorname{tr}U_P^\dagger$ and the value is still $\tilde c_{1/2}^2$ (equivalently, $\int U_{ij}U_{kl}=\frac12\epsilon_{ik}\epsilon_{jl}\ne0$). Each of the $A=2$ plaquettes carries $2(d-2)$ decorations, $4(d-2)$ in all (for SU(3) each location also carries the ε-tensor box of §4.3, which adds $12(d-2)\tilde c_F^5$); the next order has boxes on the two-plaquette base and the vacuum cubes that touch the sheet, both $O(\tilde c^6)$. Finally $R(1,2)=-\ln[W(1,2)/W(1,1)]=-\ln\tilde c-2(d-2)\tilde c^4+O(\tilde c^6)$, that is $1.4130$ at $\beta=1$ ($\tilde c=0.24019$) and $0.6959$ at $\beta=2$ ($\tilde c=0.43313$), equal to σ of §4.3 at this order. Common failure mode: taking both tiles with $\operatorname{tr}U_P$ for SU(3), which gives zero, or counting $1/N$ for every link and forgetting the factor N from every site.
2. **SU(2) class integrals.** $\int\chi_{1/2}^3\chi_{3/2}=1$, since spin 3/2 occurs once in $(\frac12)^{\otimes3}=\frac32\oplus\frac12\oplus\frac12$, and $\int\chi_1^3=1$, the single singlet in $1\otimes1\otimes1$ (the ε tensor). The expansion $e^{\frac\beta2\chi_{1/2}}\ni\frac{\beta^2}{8}\chi_{1/2}^2+\frac{\beta^3}{48}\chi_{1/2}^3$ projects to $a_1\simeq\beta^2/8$ and $a_{3/2}\simeq\beta^3/48$, and dividing by $d_j$ gives $\tilde c_1\simeq\beta^2/24$ and $\tilde c_{3/2}\simeq\beta^3/192$. At $\beta=0.1$ the exact values are $4.164\times10^{-4}$ and $5.204\times10^{-6}$ (series $4.167\times10^{-4}$ and $5.208\times10^{-6}$); at $\beta=1$ they are $0.03923$ and $0.004843$ (series $0.04167$ and $0.005208$). With $-\ln\tilde c_j=2j\ln\frac2\beta+\ln(2j+1)!+O(\beta^2)$ and $-\ln\tilde c_{1/2}=\ln\frac4\beta+O(\beta^2)$, the ratio is $2j+\frac{\ln(2j+1)!-2j\ln2}{\ln(4/\beta)}+O(\beta^2)$: $2+\frac{\ln(3/2)}{\ln(4/\beta)}$ for $j=1$ and $3+\frac{\ln3}{\ln(4/\beta)}$ for $j=\frac32$, which gives 2.038 and 3.104 at $\beta=10^{-4}$. Common failure mode: forgetting to divide $a_j$ by $d_j$, which gives $\beta^2/8$ and $\beta^3/48$.
3. **$\mathbb Z_N$ coefficients.** The Haar measure is $1/N$ on each element, and $\tilde c_n=\sum_{k=0}^{N-1}\cos\frac{2\pi nk}N\,e^{\beta\cos(2\pi k/N)}\big/\sum_ke^{\beta\cos(2\pi k/N)}$, with $\tilde c_{N-n}=\tilde c_n$. For $N=2$ this is $(e^\beta-e^{-\beta})/(e^\beta+e^{-\beta})=\tanh\beta$; for $N=4$, $(e^\beta-e^{-\beta})/(e^\beta+2+e^{-\beta})=\sinh\beta/(1+\cosh\beta)=\tanh(\beta/2)$; as $N\to\infty$ the sums become the Bessel integrals and $\tilde c_n\to I_n/I_0$. For $N=3$, $\tilde c_1=(e^\beta-e^{-\beta/2})/(e^\beta+2e^{-\beta/2})=\frac\beta2+\frac{\beta^2}8+O(\beta^3)$. The factor 2 at $N=2$ has the same origin as in SU(2): the charge-1 character of $\mathbb Z_2$ is real, so both halves $e^{\pm2\pi ik/N}$ of the cosine feed it. At $\beta=1$ the values are $0.7616$, $0.5372$, $0.4621$ and $0.4464$ for $N=2,3,4,\infty$. Common failure mode: keeping the sine terms in the numerator, which cancel between k and $N-k$.
4. **Two dimensions.** With the tree set to 1, $U_P(x,0)=U_h(x,1)^\dagger$ and $U_P(x,y)=U_h(x,y)U_h(x,y+1)^\dagger$. Solving upward, $U_h(x,y+1)=U_P(x,y)^\dagger U_h(x,y)$, a triangular change of variables in which each step is an inversion followed by a right multiplication, so the Haar measure is preserved and the plaquette variables are independent, each with density $e^{-S_P}$. A loop enclosing A plaquettes is then a product in which each enclosed $U_P$ occurs once, conjugated by matrices built from other plaquettes, and integrating the plaquettes one at a time with $\langle D^r(U_P)\rangle=\tilde c_r\mathbb 1$ gives $\langle W_r\rangle=\tilde c_r^{A}$ exactly. For SU(2) at $\beta=2$ this is $0.4331$, $0.1876$ and $0.0352$. There is no roughening because the sheet has no transverse direction, and no Coulomb phase because the plaquettes are independent at every β. Common failure mode: using periodic boundary conditions, where the product of all plaquettes is constrained and the plaquettes do not decouple, so that finite-size corrections appear.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block B. Rewritten to the note-quality-template standard on 2026-09-28 (first draft 2026-07-01). Last revised 2026-09-28.*
