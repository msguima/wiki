---
title: "Sem II Week 3 — Spontaneous Breaking of Higher-Form Symmetries: the Landau Paradigm Regained"
type: lecture-notes
course: syllabus
semester: 2
week: 3
block: 1
duration: 4 hours (2 lectures × 2 hours) plus the seminar hour
prerequisites: Sem I Weeks 5, 8–11 and 13–15; Sem II Weeks 1–2; Goldstone's theorem for ordinary symmetries
modified: 2026-10-04
---

# Sem II Week 3 — Spontaneous Breaking of Higher-Form Symmetries: the Landau Paradigm Regained

> *Semester I told phases apart with large loops: the area and perimeter laws of Wegner's model, the massless photon of the Coulomb phase of compact QED₄, the gapped photon of compact QED₃, and the degenerate ground states of the lattice superconductor of [[week-14-fradkin-shenker-order-parameters|Week 14]] §8. Weeks 1 and 2 of this semester identified the topological operators behind those diagnostics. This week supplies their dynamics. We make precise what it means for a 1-form symmetry to be spontaneously broken when the charged line has a divergent self-energy, derive why a broken continuous 1-form symmetry forces a massless photon and why it can break only for $d\ge4$, and state exactly what is broken in a superconductor. Landau's three pillars (order parameter, Goldstone boson, Coleman–Mermin–Wagner) return with lines in place of points, as Gaiotto, Kapustin, Seiberg and Willett observed.*

### How to use this chapter

- **In class:** in the first lecture state the definition (2.1), derive the self-energy reading (2.2), the lattice coefficient (2.3)–(2.5) and the smooth and polygonal loops (2.6)–(2.8); then the broken-symmetry Ward identity (3.1)–(3.3) with Figure 1 and its model proof in free Maxwell theory, (3.4)–(3.8). In the second lecture derive the exact lattice Ward identity (3.9) of compact QED₄, the Goldstone commutator (3.10)–(3.11) of the dual photon, the reduction identity (4.1) with the potentials (4.2) and Figure 2, the infrared integral (4.3), and the superconductor of §5, (5.1)–(5.6) with Figure 3. Problems 1–4 are the classroom core; the seminar hour follows §7.
- **For self-study:** §§2.4, 5.3, 6 and 8–10, and Problems 5⋆–7⋆. The one calculation to do alone: compute $\langle J,GJ\rangle$ for the $L\times L$ square of §2.4 with $L\le16$ from the Bessel representation of [[courses/generalized-symmetries-course/conventions|conventions]] §5 and recover the corner coefficient $1/4\pi^2$ of (2.8).
- **Instructor checkpoint:** two errors recur. The first is to read a perimeter law as spontaneous breaking when the symmetry is broken explicitly, as in the Higgs phase (§3.3, Problem 3). The second is to call the photon of compact QED₄ the Goldstone boson of its magnetic 1-form symmetry, which the Villain theory breaks explicitly in both phases; what protects the Coulomb photon exactly is the electric symmetry (§3.3).

## 0. Reading

**Primary:** Gaiotto, Kapustin, Seiberg, Willett (GKSW), "Generalized global symmetries", *JHEP* 02 (2015) 172 [arXiv:1412.5148], §5 (pp. 22–27 in the JHEP pagination used throughout the course): large loops as the diagnostic of breaking, with the perimeter term removed by a local geometric counterterm; eq. (5.1), the photon as the Goldstone boson; the higher-form Coleman–Mermin–Wagner statement in its continuous and discrete forms; §5.1 on $U(1)$ gauge theory with and without charge-$n$ matter and its compactification to three dimensions; §5.2 on the discrete case. Then §7.2 (pp. 32–34), the classification of four-dimensional phases by a 1-form symmetry $G$ and its unbroken subgroup $K$.

**Seminar paper:** Hansson, Oganesyan, Sondhi (HOS), "Superconductors are topologically ordered", cond-mat/0404327, §§I–IV with §V.A–B (§7 below).

**Secondary:**
- Semester I: [[week-05-wegner-z2-gauge-theory|Week 5]] §§4–6 and 8; [[week-09-compact-qed3-monopole-plasma|Week 9]] §5; [[week-10-polyakov-mass-gap-area-law|Week 10]] §§5 and 6.3; [[week-11-monopole-condensation-4d|Week 11]] §§4.2 and 5; [[week-13-fradkin-shenker-gauge-higgs|Week 13]] §§2.4 and 5; [[week-14-fradkin-shenker-order-parameters|Week 14]] §§3, 8 and 9; [[week-15-semester-i-consolidation|Week 15]] §§2, 5 and 6.
- Semester II: [[sem2-week-01-symmetries-are-topological-operators|Sem II Week 1]] §§2–3 and 6 (the Ward identity with its contact term; Maxwell's two currents) and [[sem2-week-02-zn-gauge-theory-as-bf-theory|Sem II Week 2]] §§6.1 and 7 (BF theory from the Villain form; degeneracy as broken 1-form symmetry).
- Fröhlich & Spencer, *Commun. Math. Phys.* 83 (1982) 411, and Guth, *Phys. Rev. D* 21 (1980) 2291, the rigorous input for the Coulomb phase (Week 11 §4.2). McGreevy, arXiv:2204.03045, the review to keep open. The concept pages [[higher-form-symmetries]] and [[topological-order]].

**Optional research reading:** Hofman & Iqbal, "Goldstone modes and photonization for higher form symmetries", *SciPost Phys.* 6 (2019) 006 [arXiv:1802.09512], whose theorem is the general form of §3.1 (a perimeter law for a defect charged under a continuous higher-form symmetry implies a gapless mode); Lake, "Higher-form symmetries and spontaneous symmetry breaking", arXiv:1802.07747.

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Sem I Week 1]]. A bare "Week n" refers to Semester I; Semester II weeks are written "Sem II Week n". Normalizations from [[courses/generalized-symmetries-course/conventions|conventions]] §§2 and 4–6; $d$ is the Euclidean spacetime dimension. Every lattice number below was computed from the Bessel representation $G_d(x)=\int_0^\infty dt\,e^{-2dt}\prod_\mu I_{x_\mu}(2t)$ of [[courses/generalized-symmetries-course/conventions|conventions]] §5, and every operator identity was checked on explicit cochains of small periodic lattices; each section names its check.

## 1. Motivation and setting

Landau's theory of a broken symmetry has three parts. The order parameter is a local operator charged under the symmetry whose two-point function tends to a nonzero constant, so that by cluster decomposition its expectation value is nonzero in a pure state. Goldstone's theorem says that a broken continuous symmetry forces massless excitations, which the current creates from the vacuum. The Coleman–Mermin–Wagner theorem says that the infrared fluctuations of those modes destroy the order for $d\le2$. Semester I met all three for higher-form symmetries without the names. Wilson loops with an area or a perimeter law separated the phases of Wegner's model (Week 5 §§4–5); the Coulomb phase of compact QED₄ has a massless photon (Week 11 §4.2); and compact QED₃ has no Coulomb phase (Week 9 §6), while even its monopole-free version binds charges by a logarithm.

GKSW §5 reads these facts as Landau's theory for the 1-form symmetries of [[sem2-week-01-symmetries-are-topological-operators|Sem II Week 1]] ([[higher-form-symmetries]]). We make the reading precise in three steps. The order parameter comes first: a charged line in a regularized theory has a self-energy proportional to its length, and the definition must say which subtraction is allowed and what survives it (§2). Then the Goldstone theorem: we derive the broken-symmetry Ward identity of a 2-form current, prove the massless pole in free Maxwell theory, and find which of the two 1-form symmetries of compact QED₄ protects its photon (§3). Then the dimension bound, whose infrared integral is ordinary Coleman–Mermin–Wagner in the $d-p$ dimensions transverse to the charged object (§4). The superconductor of Hansson, Oganesyan and Sondhi becomes a precise statement about one explicit and one spontaneous breaking (§5), and §6 supplies the reasons behind the realizations listed in Week 15 Table 3.

Two statements of the block skeleton need correction, and the note carries both throughout.

(i) "Confinement is the unbroken electric 1-form symmetry" holds for pure gauge theory and for matter neutral under the center. With charge-1 matter there is no exact electric symmetry, and the area-law and symmetry criteria fail together; with charge $q$ in a $\mathbb{Z}_N$ theory only the residual $\mathbb{Z}_{\gcd(N,q)}^{(1)}$ can be realized ([[week-13-fradkin-shenker-gauge-higgs|Week 13]]; Week 14 §§3 and 9).

(ii) In Villain compact QED the integer lattice 't Hooft loop equals 1 identically, and the magnetic 1-form symmetry is explicitly broken in both phases; it is emergent in the Coulomb phase (Week 11 §5 and Table 1).

## 2. The order parameter of a 1-form symmetry

### 2.1 The definition [Stated after GKSW §5; the statements of §§2.2–2.4 Proved or Computed]

Let $G^{(1)}$ be an exact 1-form symmetry and $W(C)$ a genuine line operator charged under it, one whose definition needs no surface (F3). Fix a closed curve $C_0$, smooth in the continuum and on the lattice the lattice approximation of a smooth curve, and dilate it, $C_\lambda=\lambda C_0$. A local counterterm is a factor $\exp\big(\int_C\mu\,ds\big)$ whose coefficient μ may depend on the direction of the tangent (on the lattice the staircase approximant of a curve has a direction-dependent self-energy), together with constants at corners. We say that
$$
G^{(1)}\ \text{is broken if}\ \liminf_{\lambda\to\infty}\big|\langle W(C_\lambda)\rangle\big|\,e^{\int_{C_\lambda}\mu\,ds}>0\ \text{for some local }\mu,\qquad
\text{unbroken if}\ \lim_{\lambda\to\infty}\big|\langle W(C_\lambda)\rangle\big|\,e^{\int_{C_\lambda}\mu\,ds}=0\ \text{for every local }\mu .\tag{2.1}
$$
If $G$ breaks to a subgroup $K$, the lines charged under $K$ obey the second condition and the lines charged under $G$ but neutral under $K$ the first (GKSW §5). The definition sharpens the criterion of [[courses/generalized-symmetries-course/conventions|conventions]] §6 in two places: μ may depend on the direction, and "tends to a nonzero constant" becomes "stays bounded away from zero", because corners in gapless phases make the subtracted loop grow as a power (§2.4). It presupposes an exact symmetry (§3.3).

On a spatial torus the Hamiltonian face of (2.1) is the realization of the symmetry operators $U(\tilde\gamma)$ on the ground-state sector, the sense of [[courses/generalized-symmetries-course/conventions|conventions]] §11. For a discrete symmetry, (2.1) holds exactly when the wrapped charged lines act invertibly on the low-lying states, and then the $U(\tilde\gamma)$ on the crossing cycles permute those states and force the degeneracy; [[sem2-week-02-zn-gauge-theory-as-bf-theory|Sem II Week 2]] §§7.1–7.3 proves this at the soluble points. For continuous symmetries the Euclidean statement (2.1) is primary (F4).

### 2.2 The counterterm is the self-energy of a static charge [Proved, given the transfer matrix.]

Take $C$ a rectangle of sides $R$ and $T$ in a plane that contains the Euclidean time direction. Inserting the transfer matrix of [[week-07-kogut-susskind-hamiltonian|Week 7]] between the two spatial sides gives a sum over the states of the theory with static charges $\pm q$ at separation $R$, $\langle W_q(R\times T)\rangle=\sum_n|c_n(R)|^2e^{-TE_n(R)}$, so that
$$
\langle W_q(R\times T)\rangle\ \xrightarrow{\ T\to\infty\ }\ |c_0(R)|^2\,e^{-T\,V(R)},\tag{2.2}
$$
where $V(R)=E_0(R)$ is the static potential, measured from the vacuum. If $V(R)$ tends to a finite $V_\infty$, a counterterm $\mu=V_\infty/2$ on the time-like sides removes the exponential: μ is the energy of one isolated probe. If $V(R)$ grows without bound, as $\sigma R$ under an area law or as $\frac{q^2e^2}{2\pi}\ln R$ in three-dimensional Maxwell theory, no local μ can remove it, because a counterterm on a side cannot know the distance to the opposite side. A perimeter law therefore says that an isolated probe charge has finite energy, the deconfinement of probes, and the counterterm is that energy.

### 2.3 Free Maxwell theory on the lattice [Computed.]

In the non-compact (monopole-free) Gaussian theory at Feynman gauge, $\langle a_\ell a_{\ell'}\rangle=\delta_{\mu_\ell\mu_{\ell'}}G_d(x_\ell-x_{\ell'})/\beta$, because the Laplacian on 1-cochains acts as the scalar Laplacian on each direction (checked on the periodic $3^4$ lattice for 1- and 2-cochains). For a closed $C$ the gauge-dependent part of the propagator, of the form $d(\cdots)\delta$, annihilates $J_C$, since $\delta J_C=0$, and
$$
\langle W_q(C)\rangle=\exp\Big(-\frac{q^2}{2\beta}\,\langle J_C,GJ_C\rangle\Big),\qquad
\langle J_C,GJ_C\rangle=\sum_{\ell,\ell'\in C}J_\ell J_{\ell'}\,\delta_{\mu_\ell\mu_{\ell'}}\,G_d(x_\ell-x_{\ell'}),\tag{2.3}
$$
with $J_C\in C^1(\Lambda,\mathbb{Z})$ the signed indicator of the links of $C$. For the rectangle with $T\to\infty$ the two time-like sides contribute $T$ times a sum of $G_d$ along the time direction, and the reduction identity (4.1), proved in §4.1, evaluates that sum exactly: $\sum_kG_d(x_\perp+k\hat\tau)=G_{d-1}(x_\perp)$. The self-terms give $2TG_{d-1}(0)$ and the cross-terms $-2TG_{d-1}(R\hat1)$, while the spatial sides and the ends contribute terms subleading in $T$. Therefore
$$
V(R)=\frac{q^2}{\beta}\big[G_{d-1}(0)-G_{d-1}(R\hat1)\big].\tag{2.4}
$$
In $d=4$, with $\beta=1/e^2$, $V(R)=\frac{q^2}{\beta}G_3(0)-\frac{q^2}{\beta}G_3(R\hat1)\to2\mu-\frac{q^2e^2}{4\pi R}$, the Coulomb potential above twice the self-energy
$$
\mu=\frac{q^2}{2\beta}\,G_3(0)=0.126366\,\frac{q^2e^2}{a_{\rm lat}}\qquad(\text{axis-parallel line}).\tag{2.5}
$$
The values $\beta V(R)/q^2=1/6$ at $R=1$ (exactly, since $G_3(0)-G_3(\hat e)=\tfrac16$, [[courses/generalized-symmetries-course/conventions|conventions]] §2) and $0.2098,\ 0.2324,\ 0.2427,\ 0.2478$ at $R=2,4,8,16$ approach $G_3(0)-1/4\pi R$ from below. The perimeter law holds, and its coefficient is an ultraviolet quantity: $\mu\propto1/a_{\rm lat}$ is the linearly divergent Coulomb self-energy of a point charge. It depends on the direction of the line on the lattice and on the action, and it carries no physical information (F1).

### 2.4 Smooth loops and corners [Computed.]

For a circle of radius $R$ in the continuum, regulate the propagator by point splitting, $D_a(x)=1/4\pi^2(x^2+a^2)$. With $dx\cdot dy=R^2\cos\phi\,d\phi_1d\phi_2$, $\phi=\phi_1-\phi_2$, $(x-y)^2=2R^2(1-\cos\phi)$ and $\epsilon=a/R$,
$$
\oint\oint dx\cdot dy\,D_a=\frac{2\pi}{4\pi^2}\int_0^{2\pi}\frac{\cos\phi\,d\phi}{2(1-\cos\phi)+\epsilon^2}
=\frac1{2\pi}\Big[-\pi+\Big(1+\frac{\epsilon^2}2\Big)\frac{2\pi}{\epsilon\sqrt{4+\epsilon^2}}\Big]=\frac R{2a}-\frac12+O(\epsilon),
$$
where we wrote $\frac{\cos\phi}{2(1-\cos\phi)+\epsilon^2}=-\frac12+\frac{1+\epsilon^2/2}{2+\epsilon^2-2\cos\phi}$ and used $\int_0^{2\pi}\frac{d\phi}{2+\epsilon^2-2\cos\phi}=\frac{2\pi}{\epsilon\sqrt{4+\epsilon^2}}$. The Wilson loop is $\exp\big(-\frac{q^2e^2}2\oint\oint D_a\big)$, so
$$
\ln\langle W_q(\text{circle})\rangle=-\frac{q^2e^2}{8\pi a}\,|C|+\frac{q^2e^2}4+O(a/R),\qquad |C|=2\pi R .\tag{2.6}
$$
The subtracted loop tends to the constant $e^{q^2e^2/4}$, independent of $R$ (the closed form was checked against quadrature to $10^{-8}$ for $\epsilon=10^{-2},10^{-3},10^{-4}$).

Polygons behave differently in a gapless phase. A straight side of length $L$ has the self-energy integral
$$
\int_0^L\!\!\int_0^L\frac{ds\,dt}{(s-t)^2+a^2}=\frac{2L}a\arctan\frac La-\ln\Big(1+\frac{L^2}{a^2}\Big)=\frac{\pi L}a-2\ln\frac La-2+O(a/L),\tag{2.7}
$$
and the logarithm comes from its two endpoints. In Feynman gauge two perpendicular sides do not interact, so at a right-angle corner nothing cancels the two endpoint terms, and each corner contributes $+\frac{q^2e^2}{4\pi^2}\ln(L/a)$ to $\ln\langle W\rangle$. The lattice says the same. For the $L\times L$ square, $\langle J,GJ\rangle=4S(L)-4X(L)$, with the self-interaction of one side $S(L)=L\sum_{|k|<L}G_4(k\hat1)-2\sum_{k=1}^{L-1}kG_4(k\hat1)=G_3(0)L-\frac1{2\pi^2}\ln L+O(1)$, by (4.1) and $G_4(k\hat1)\to1/4\pi^2k^2$, and the interaction of opposite sides $X(L)\to\frac1{4\pi^2}\int_0^1\!\int_0^1\frac{du\,dv}{(u-v)^2+1}=\frac{\pi/2-\ln2}{4\pi^2}$. Therefore
$$
\ln\langle W_q(\square_L)\rangle=-\mu\,|C|+\frac{q^2}{\pi^2\beta}\ln L+c+o(1),\qquad |C|=4L .\tag{2.8}
$$
Numerically, the local slope of $\langle J,GJ\rangle-4G_3(0)L$ in $\ln L$ is $-0.20251$ between $L=24$ and 32 and $-0.20256$ between 32 and 40, against $-2/\pi^2=-0.20264$, and $X(40)=0.022241$ against the limit $0.022231$ (Bessel integrals with $G_4(k\hat1)$ up to $k=200$ and the fitted tail). A general corner gives a different coefficient (Problem 7⋆).

So in a broken gapless phase the subtracted loop tends to a constant for smooth shapes and grows as a power for polygons. A corner counterterm can cancel the $\ln a$ in (2.7), but the $\ln L$ is an infrared effect that no local term removes, and this is why (2.1) asks for "bounded away from zero". In gapped broken phases, such as the deconfined $\mathbb{Z}_N$ theory, corners contribute constants. In unbroken phases the subtracted loop vanishes faster than any power, by an area law or by the $R\ln R$ of $d=3$ (Problem 4).

## 3. The photon as a Goldstone boson

### 3.1 The broken-symmetry Ward identity [the identity Proved; the conclusion Heuristic, the general theorem Stated — refs: Hofman–Iqbal]

Let $\mathcal J^{\nu\mu}=-\mathcal J^{\mu\nu}$ be the current of an exact $U(1)^{(1)}$ in $d=4$, normalized so that the symmetry operator acts on a charge-$Q$ line by $e^{iQ\alpha\,{\rm Link}}$ ([[courses/generalized-symmetries-course/conventions|conventions]] §6). The infinitesimal form of the linking action ([[sem2-week-01-symmetries-are-topological-operators|Sem II Week 1]] §6.1) is the Ward identity
$$
\partial_\mu\big\langle\mathcal J^{\nu\mu}(x)\,\mathcal W_Q(C)\cdots\big\rangle=c\,Q\,J^\nu_C(x)\,\big\langle\mathcal W_Q(C)\cdots\big\rangle,\qquad J^\nu_C(x)=\oint_Cdy^\nu\,\delta^4(x-y),\tag{3.1}
$$
with further insertions away from $x$. For the electric symmetry $\mathcal J^{\nu\mu}=F_{\nu\mu}/e^2$, $\mathcal W_Q=W_q$ and $c=i$: this is (3.1) of Sem II Week 1, whose Euclidean $i$ comes from $F_{\tau i}=iE_i$. For the magnetic symmetry $\mathcal J^{\nu\mu}=J_m^{\nu\mu}\equiv\frac1{4\pi}\epsilon_{\nu\mu\rho\sigma}F_{\rho\sigma}$, the components of $\star F/2\pi$ (Sem II Week 1 §3.2), $\mathcal W_Q$ is the 't Hooft line $\tilde W_m(\tilde C)$ and $c=1$. Here (3.1) defines the 't Hooft line as a monopole worldline: with $\epsilon_{\tau123}=+1$, $B_i=\frac12\epsilon_{ijk}F_{jk}$ and a static line along $+\tau$, the component $\nu=\tau$ reads $\nabla\cdot B=2\pi m\,\delta^3(\vec x)$, the outward flux $2\pi m$ of [[courses/generalized-symmetries-course/conventions|conventions]] §5.

Now assume the symmetry broken in the sense of (2.1) and let $C$ become a straight line along τ through the origin. The counterterm multiplies numerator and denominator alike, so the normalized correlator
$$
\mathcal G^{\nu\mu}(\vec x)=\lim\frac{\langle\mathcal J^{\nu\mu}(x)\,\mathcal W_Q(C)\rangle}{\langle\mathcal W_Q(C)\rangle}\tag{3.2}
$$
does not depend on μ; in the broken phase we assume that the limit exists, which for a genuine line is what (2.1) means at the level of correlators, and by translation invariance along the line it depends on $\vec x$ only. The component $\nu=\tau$ of (3.1) gives $\partial_i\mathcal G^{\tau i}=cQ\,\delta^3(\vec x)$: the flux of $\mathcal G^{\tau i}$ through every sphere around the line equals $cQ$, whatever its radius. With $\tilde{\mathcal G}(\vec k)=\int d^3x\,e^{-i\vec k\cdot\vec x}\,\mathcal G(\vec x)$,
$$
ik_i\,\tilde{\mathcal G}^{\tau i}(\vec k)=cQ\qquad\Longrightarrow\qquad\tilde{\mathcal G}^{\tau i}(\vec k)=-icQ\,\frac{k_i}{\vec k^2}+(\text{transverse}).\tag{3.3}
$$
The longitudinal part is fixed by the charge alone and has a pole at $\vec k=0$. In a theory with a mass gap $m_0$, the one-point function of a local operator near a static genuine probe relaxes to its vacuum value, here zero, as $e^{-m_0|\vec x|}$, and its Fourier transform is analytic at $\vec k=0$. That contradicts (3.3). Therefore a spontaneously broken continuous 1-form symmetry implies gapless excitations created by its current. The static line selects $k_\tau=0$, so the pole in $\vec k^2$ is the restriction of a four-dimensional pole in $k^2$: a massive mode would give $1/(\vec k^2+m_0^2)$. Before normalization the residue is $cQ\langle\mathcal W_Q\rangle$, the analog of $\langle\delta\phi\rangle$ in the theorem for a 0-form symmetry, $ip_\mu\langle\tilde J^\mu(p)\,\phi(0)\rangle=\langle\delta\phi\rangle$.

In the unbroken phase (3.1) still holds, and Figure 1 shows how it is satisfied without a gapless mode. The line bounds a physical sheet, the worldsheet of the confining string, and the flux crosses every linking sphere where the sphere cuts the sheet: the field is localized and (3.2) has no rotation-invariant limit [Heuristic; the sine-Gordon wall of Week 10 §5 and the confining string of Week 11 §6.3 are the computed instances].

```
   (a) broken: perimeter law                 (b) unbroken: area law

          \     |     /
           \    |    /                          sheet bounded by C
      ------    ×    ------                ×====================> (the confining
           /    |    \                                              string)
          /     |     \
   flux cQ through every sphere,         flux cQ through every sphere,
   spread as 1/r²: massless pole         carried by the sheet: gapped
```
**Figure 1. A transverse slice through a static charged line (×). The Ward identity (3.1) forces the same flux through every sphere around it. In the broken phase the line bounds no physical surface and the flux spreads isotropically, as $1/r^2$, which is the pole (3.3); in the unbroken phase it runs along the sheet that the area law describes.**

> **Physical picture.** In a Monte Carlo simulation of compact QED₄ with two static charges, measure the plaquette correlator with the Polyakov-loop pair normalized by the pair. In the Coulomb phase the flux spreads through all of space and falls off as $1/r^2$ away from the charges; in the confining phase it is squeezed into a tube between them. The exact content is the Ward identity, which holds in both phases (§3.3); the profiles are the long-distance statement of (3.3) and of Figure 1 [Heuristic for the tube]. Problem 8⋆⋆ makes this a project.

### 3.2 Model proof: free Maxwell theory and its 't Hooft line [Model proof.]

In the monopole-free theory both symmetries are exact. Represent the 't Hooft line by a Dirac sheet: choose a surface $\tilde S$ with $\partial\tilde S=\tilde C$ and a 2-form Ξ supported on it, the continuum twisted sheet of Week 11 §5.1 at $\alpha=2\pi m$, oriented so that the field strength $F=da+2\pi m\,\Xi$ obeys (3.1). In the non-compact theory no Villain integers absorb the sheet, and
$$
\langle\tilde W_m(\tilde C)\cdots\rangle=\frac1Z\int Da\;e^{-\frac1{2e^2}\|da+2\pi m\,\Xi\|^2}\cdots,\qquad \|\omega\|^2=\int\omega\wedge\star\omega .\tag{3.4}
$$
The integral is Gaussian. On 2-forms of $\mathbb{R}^4$, $1=d\Delta^{-1}\delta+\delta\Delta^{-1}d$, and the classical solution removes the exact part of Ξ, $da_{\rm cl}=-2\pi m\,d\Delta^{-1}\delta\,\Xi$, so that
$$
F_{\rm cl}=2\pi m\,\delta\Delta^{-1}d\Xi,\qquad \frac1{2e^2}\|F_{\rm cl}\|^2=\frac{2\pi^2m^2}{e^2}\big\langle d\Xi,\Delta^{-1}d\Xi\big\rangle .\tag{3.5}
$$
The second equality uses $\|\delta\Delta^{-1}\omega\|^2=\langle\omega,d\delta\Delta^{-2}\omega\rangle=\langle\omega,\Delta^{-1}\omega\rangle$ for the 3-form $\omega=d\Xi$, which is closed, so that $\Delta\omega=d\delta\omega$. Since $d\Xi$ is the 3-form dual to $\tilde C$, the sheet has dropped out: $\tilde W_m$ is a genuine line, and $F_{\rm cl}$ obeys $dF_{\rm cl}=2\pi m\,d\Xi$ and $d\star F_{\rm cl}=0$. The Hodge star commutes with Δ and preserves the inner product, so $\langle d\Xi,\Delta^{-1}d\Xi\rangle=\oint\oint dx\cdot dy\,D(x-y)$ with $D(x)=1/4\pi^2x^2$, and the fluctuations around $F_{\rm cl}$ are those of the vacuum. Therefore
$$
\langle\tilde W_m(\tilde C)\rangle=\exp\Big(-\frac{\tilde e^2m^2}2\oint_{\tilde C}\oint_{\tilde C}dx\cdot dy\,D(x-y)\Big),\qquad \tilde e=\frac{2\pi}e ,\tag{3.6}
$$
the Wilson loop with $q\to m$ and $e\to\tilde e$, as electric–magnetic duality requires ([[week-08-dual-variables-abelian-gauge|Week 8]] §6; [[courses/generalized-symmetries-course/conventions|conventions]] §5). It obeys the perimeter law of §2.4, so the magnetic $U(1)^{(1)}$ is broken. For the static line along $+\tau$ the solution of $\nabla\cdot B=2\pi m\,\delta^3$ and $\nabla\times B=0$ that decays at infinity is $B=\frac m2\frac{\vec x}{|\vec x|^3}$, with $F_{\tau i}=0$, so that $\mathcal G_m^{\tau i}=J_m^{\tau i}=B_i/2\pi$ and
$$
\mathcal G_m^{\tau i}(\vec x)=\frac m{4\pi}\,\frac{x_i}{|\vec x|^3}=-m\,\partial_i\frac1{4\pi|\vec x|},\qquad\tilde{\mathcal G}_m^{\tau i}(\vec k)=-im\,\frac{k_i}{\vec k^2},\tag{3.7}
$$
which is (3.3) with $c=1$, $Q=m$ and no transverse part, since $\int d^3x\,e^{-i\vec k\cdot\vec x}/4\pi|\vec x|=1/\vec k^2$. The electric line gives the same with $c=i$: $\mathcal G_e^{\tau i}=F_{\tau i}/e^2=iE_i/e^2=iq\,x_i/4\pi|\vec x|^3$.

The pole is the photon. From $\langle a_\mu(k)a_\nu(-k)\rangle=e^2\delta_{\mu\nu}/k^2$,
$$
\langle F_{\mu\nu}(k)F_{\rho\sigma}(-k)\rangle=e^2\,\frac{k_\mu k_\rho\delta_{\nu\sigma}-k_\mu k_\sigma\delta_{\nu\rho}-k_\nu k_\rho\delta_{\mu\sigma}+k_\nu k_\sigma\delta_{\mu\rho}}{k^2},\tag{3.8}
$$
whose only singularity is the pole at $k^2=0$. In the two-point function of $J_m$ the residue carries $e^2/4\pi^2=1/\tilde e^2$, and in that of $F/e^2$ it carries $1/e^2$; these play the role of $f_\pi^2$ and are not universal, while the residue in (3.7) is the charge. GKSW (5.1) is the Minkowski form of the statement: the current creates one photon from the vacuum with amplitude $\zeta_\mu p_\nu-\zeta_\nu p_\mu$.

A Goldstone field is a field that shifts under the broken symmetry. Under the electric symmetry with a flat background, $a\to a+\lambda$ with $d\lambda=0$; under the magnetic one, the dual photon shifts in the same way (GKSW §5.1). A massless $p$-form gauge field in $d$ dimensions has $\binom{d-2}{p}$ physical polarizations: two for the photon in $d=4$, one for the photon in $d=3$, which is the dual scalar σ and the Goldstone boson of the magnetic 0-form symmetry. The two polarizations of the four-dimensional photon are the Goldstone modes of a broken $U(1)^{(1)}$, and in the monopole-free theory of both.

### 3.3 Compact QED₄: the exact electric Ward identity [Proved; the Coulomb-phase input Stated — refs.]

In the Villain theory the measure $\prod_\ell da_\ell/2\pi$ over one period and the summed weight $\sum_ne^{-\frac\beta2\|da-2\pi n\|^2}$ are periodic in each $a_\ell$, so $\int\prod da\;\partial_{a_\ell}\big[\sum_ne^{-S}\,W_q(C)\cdots\big]=0$. With $\partial S/\partial a_\ell=\beta\langle d\mathbb 1_\ell,F\rangle=\beta(\delta F)_\ell$, $F=da-2\pi n$, and $\partial_{a_\ell}W_q=iqJ_C(\ell)\,W_q$,
$$
\beta\,\big\langle(\delta F)_\ell\,W_q(C)\cdots\big\rangle=iq\,J_C(\ell)\,\big\langle W_q(C)\cdots\big\rangle\qquad\text{at every }\beta,\tag{3.9}
$$
the lattice form of (3.1); for the Wilson action $\beta F_P$ is replaced by $\beta\sin(da)_P$. It is the infinitesimal twisted sheet of Week 11 §5.1. Two checks, of identities that hold in every $d$, were run on a periodic $4^3$ lattice: the formula for $\partial S/\partial a_\ell$ against finite differences of the action, and the Gaussian solution $\langle F\rangle_W=\frac{iq}\beta\,dGJ_C$, which satisfies (3.9) because $\delta dG J_C=(\Delta-d\delta)GJ_C=J_C$. For a straight line along τ, $GJ_C$ on the time-like links equals $G_3(\vec x)$ by (4.1), so $\beta\langle F\rangle$ on the time-like plaquettes is $iq$ times the lattice gradient of $G_3$: its flux out of every box of a time slice is $iq$, because $\Delta G_3=\delta_{\vec x,0}$, and it decays as $1/4\pi r^2$. This is (3.3) on the lattice.

Identity (3.9) is exact in compact QED₄, monopoles included, because the electric symmetry is exact there. In the Coulomb phase the Wilson loop has a perimeter law (Guth), §3.1 then requires a gapless mode created by $F$, and Fröhlich and Spencer prove that the photon is massless [Stated — refs: Week 11 §4.2]. Therefore the photon of compact QED₄ is the Goldstone boson of the spontaneously broken electric $U(1)^{(1)}$, which is exact. In the confining phase the same identity holds with an area law, and the flux runs along the string.

The magnetic symmetry is another matter, and here correction (ii) enters: with dynamical monopoles $dF=-2\pi\,dn\ne0$, the integer 't Hooft loop equals 1 identically, and the magnetic form of (3.1) fails in both phases (Week 11 §5.2 and Table 1). The sentence "the photon is the Goldstone boson of the broken magnetic 1-form symmetry" is therefore exact in the monopole-free theory of §3.2 and, for compact QED₄, holds only for the emergent symmetry of the long-distance theory; what protects the photon exactly is (3.9).

With charge-$q$ matter the identity acquires the matter current (Problem 3): the flux of a probe can end on the matter cloud, the normalized field is screened, and nothing forbids a gap together with perimeter laws. That is the Higgs phase, and it is correction (i) in Ward-identity form.

### 3.4 The Goldstone commutator for the dual photon [Computed.]

In $d=3$ the magnetic symmetry is a 0-form symmetry and its Goldstone boson is the dual photon σ ([[week-09-compact-qed3-monopole-plasma|Week 9]] §5.2). The commutator form of the theorem is short. With $\tau=it$ ([[courses/generalized-symmetries-course/conventions|conventions]] §10) the Euclidean action $\frac{e^2}{8\pi^2}\int(\partial\sigma)^2$ becomes $S_M=\frac{e^2}{8\pi^2}\int dt\,d^2x\,[(\partial_t\sigma)^2-(\nabla\sigma)^2]$, with canonical momentum $\Pi_\sigma=\frac{e^2}{4\pi^2}\partial_t\sigma$. The duality relation $B_\mu=\frac{ie^2}{2\pi}\partial_\mu\sigma$ of [[courses/generalized-symmetries-course/conventions|conventions]] §5 has time component $B_\tau=F_{xy}$, for spatial axes with $\epsilon_{\tau xy}=+1$, and $\partial_\tau=-i\partial_t$, so that $F_{xy}=\frac{e^2}{2\pi}\partial_t\sigma$ and
$$
\frac{F_{xy}(\vec x)}{2\pi}=\Pi_\sigma(\vec x),\qquad Q_m=\int d^2x\,\frac{F_{xy}}{2\pi}=\int d^2x\,\Pi_\sigma .\tag{3.10}
$$
The magnetic flux density is the momentum conjugate to the dual photon. From $[\sigma(\vec x),\Pi_\sigma(\vec y)]=i\delta^2(\vec x-\vec y)$ we get $[Q_m,\sigma(\vec x)]=-i$ and
$$
[Q_m,e^{iq\sigma(\vec x)}]=q\,e^{iq\sigma(\vec x)},\qquad \langle0|[Q_m,e^{i\sigma(\vec x)}]|0\rangle=\langle e^{i\sigma}\rangle,\qquad |\langle e^{i\sigma}\rangle|=e^{-S_{\rm mono}}\ne0 ,\tag{3.11}
$$
in the monopole-free theory ([[courses/generalized-symmetries-course/conventions|conventions]] §5; Week 9 §5.2). The monopole operator raises the flux by $2\pi q$, the outward flux of conventions §5, and the nonvanishing expectation value of the commutator is Goldstone's condition (in a pure infinite-volume state, F4). Its Euclidean form, with the pole of (3.3) one degree down, and the effect of monopoles are Week 9 §§5.1–5.3; the four-dimensional equal-time form is Week 11 §5.3 and Sem II Week 1 §6.2.

## 4. Coleman–Mermin–Wagner for $p$-form symmetries

### 4.1 The reduction identity [Proved.]

For $k$ running over a $p$-dimensional coordinate plane of $\mathbb{Z}^d$ and $x_\perp$ in the complementary directions,
$$
\sum_{k\in\mathbb{Z}^p}G_d(x_\perp+k)=G_{d-p}(x_\perp),\tag{4.1}
$$
and the same holds for the massive Green function $(\Delta+m^2)^{-1}$. **Proof.** In the Bessel representation each summed direction contributes $e^{-2t}\sum_{k\in\mathbb{Z}}I_k(2t)=1$, by the generating function $e^{\frac z2(s+1/s)}=\sum_ks^kI_k(z)$ at $s=1$; the exchange of sum and integral is justified by positivity. What remains is $\int_0^\infty dt\,e^{-2(d-p)t}\prod_{\nu\perp}I_{x_\nu}(2t)=G_{d-p}(x_\perp)$, and a factor $e^{-m^2t}$ rides along. $\square$ For $d-p\le2$ both sides diverge, and the identity holds for the differences $G(0)-G(x_\perp)$. Checks: $\sum_kG_4(k\hat1)=0.252731=G_3(0)$ to $10^{-7}$, and the same at $x_\perp=\hat1,2\hat1,\hat1+\hat2$ to $2\times10^{-5}$; the planar sum of $G_5$ reproduces $G_3(0)$ to the accuracy of its tail estimate, $10^{-3}$; the massive identity holds to machine precision.

The identity says that a straight line in $d$ dimensions is seen by the Gaussian field as a point in the $d-1$ transverse dimensions, and a flat $p$-dimensional object as a point in $d-p$.

### 4.2 Static potentials in $d=2,3,4$ [Computed.]

Inserting $G_{d-1}$ into (2.4):
$$
d=2:\ V(R)=\frac{q^2}{2\beta}\,R;\qquad d=3:\ V(R)=\frac{q^2}\beta\,a(R)=q^2e^2\Big[\frac{\ln R}{2\pi}+0.257343+O(R^{-2})\Big];\qquad d=4:\ V(R)=2\mu-\frac{q^2}\beta\,G_3(R\hat1)\ \to\ 2\mu-\frac{q^2e^2}{4\pi R}.\tag{4.2}
$$
In $d=2$, $G_1(0)-G_1(R)=|R|/2$ exactly, since $|x|/2$ has lattice Laplacian $-\delta_{x,0}$, and with $\beta=1/e^2a_{\rm lat}^2$ the potential is linear with string tension $q^2e^2/2$, the area law of two-dimensional Maxwell theory. In $d=3$, $a(R)=G_2(0)-G_2(R)$ is the subtracted function of [[courses/generalized-symmetries-course/conventions|conventions]] §2 (its constant $0.257343$ is the κ of Weeks 1–4, a letter that §5 below reserves for the hopping coupling), with $a(1)=\tfrac14$, $a(2)=0.3634$, $a(4)=0.4770$, $a(8)=0.5881$, $a(16)=0.6986$. Figure 2 sets the three side by side: linear (unbroken), logarithmic (unbroken, the marginal case, for which no local counterterm exists), bounded (broken). GKSW §5 records the same: Coulomb behavior means a broken symmetry in four dimensions and an unbroken one in two and three.

```
   βV(R)/q²
      │      d = 2  ╱                             linear: area law, unbroken
      │           ╱
      │         ╱                      ___...--- d = 3: (ln R)/2π + 0.2573, unbroken
      │       ╱             ___...---''          (the marginal case)
      │     ╱    ___...---''
      │   ╱  _.-'
      │ -╱-.'- - - - - - - - - - - - - - - - - - G₃(0) = 0.2527
      │ ╱.'  ______________...................   d = 4: bounded, broken
      │╱/_.-'
      │'
      └──┬───────────────────────────────────── R
         1
```
**Figure 2. The exact lattice static potentials (4.2) of the Gaussian theory, schematic. A line in $d$ dimensions sees the $(d-1)$-dimensional Green function, which is bounded only for $d-1\ge3$; the $d=4$ values are 1/6, 0.2098, 0.2324, 0.2427, 0.2478 at $R=1,2,4,8,16$.**

### 4.3 The heuristic and the infrared integral [Heuristic; the theorem Stated — refs: GKSW §5]

Suppose a continuous $U(1)^{(p)}$ is spontaneously broken. The low-energy theory then contains a $p$-form Goldstone field $A$ that shifts under the symmetry, with action $\frac{\rho_p}2\|dA\|^2$, and the order parameter is the charged object $W_q(C)=e^{iq\oint_CA}$ on a $p$-dimensional $C$ ($\rho_1=1/e^2$ for the photon; $\rho_0=\beta$ for the XY model). At Gaussian level, with (4.1) and the componentwise Laplacian on $p$-cochains,
$$
-\ln\langle W_q(C)\rangle=\frac{q^2}{2\rho_p}\langle J_C,GJ_C\rangle,\qquad \frac{\langle J_C,GJ_C\rangle}{|C|}\ \xrightarrow{\ C\ \text{flat and large}\ }\ G_{d-p}(0)=\int_{-\pi}^{\pi}\frac{d^{d-p}k_\perp}{(2\pi)^{d-p}}\,\frac1{\hat k_\perp^2}.\tag{4.3}
$$
In the continuum the same integral appears with its ultraviolet part removed by μ. It converges at small $k_\perp$ if and only if $d-p>2$. For $d-p=2$ it diverges logarithmically; with the infrared cutoff $1/L$ set by the size of $C$, $\langle J_C,GJ_C\rangle/|C|\simeq\frac1{2\pi}\ln\frac La$, and $\langle W\rangle e^{\mu|C|}\sim\exp\big(-\frac{q^2}{4\pi\rho_p}|C|\ln L\big)\to0$ for every μ. For $d-p<2$ the divergence is a power, $|C|\,L^{2-d+p}$. Either way the order that the Goldstone field was assumed to carry is destroyed by its own fluctuations: a continuous $p$-form symmetry is unbroken for $p\ge d-2$, as stated in [[courses/generalized-symmetries-course/conventions|conventions]] §6 and GKSW §5. For $p=0$, (4.3) is the spin-wave variance $\langle\theta^2\rangle=G_d(0)/\beta$ of [[week-01-compact-variables-xy-model|Sem I Week 1]] §3.5, and GKSW's remark that one may compactify on $T^p$, turning the wrapped object into a local operator of a $(d-p)$-dimensional theory, is (4.1) in other words.

A discrete symmetry has no Goldstone field and no such integral. GKSW §5 states that a discrete $p$-form symmetry is unbroken for $d-p<2$; two-dimensional $\mathbb{Z}_2$ gauge theory, with $\langle W\rangle=(\tanh\beta)^A$ exactly (Week 5 §6), is the instance. Table 1 collects the bounds.

| | $p=0$ | $p=1$ | $p=2$ |
|---|---|---|---|
| continuous $U(1)^{(p)}$ can break for | $d\ge3$ | $d\ge4$ | $d\ge5$ |
| discrete $\mathbb{Z}_N^{(p)}$ can break for | $d\ge2$ | $d\ge3$ | $d\ge4$ |

**Table 1. The lowest dimension in which a $p$-form symmetry can be spontaneously broken (GKSW §5; the continuous row from (4.3)).**

## 5. The superconductor, sharpened

### 5.1 The Villain abelian-Higgs model and its exact symmetries [Proved.]

We use the Villain form of the charge-$q$ model,
$$
S=\frac\beta2\|da-2\pi n\|^2+\frac\kappa2\|d\phi-qa-2\pi\ell\|^2,\tag{5.1}
$$
with $a\in C^1$ and $\phi\in C^0$ integrated over one period, $n\in C^2(\Lambda,\mathbb{Z})$ and $\ell\in C^1(\Lambda,\mathbb{Z})$. It is invariant under $a\to a+2\pi k$, $n\to n+dk$, $\ell\to\ell-qk$, under $\phi\to\phi+2\pi j$, $\ell\to\ell+dj$, and under $a\to a+d\lambda$, $\phi\to\phi+q\lambda$. The cosine (London) form of [[courses/generalized-symmetries-course/conventions|conventions]] §4 is (8.1) of Week 14; at $q=2$ both describe the lattice superconductor. Write $F=da-2\pi n$ and $D\phi=d\phi-qa-2\pi\ell$. Three exact facts follow.

(a) *Residual electric symmetry.* The twisted sheet $F\to F-\alpha\,d\lambda_{\tilde V}$ is removed by $a\to a+\alpha\lambda_{\tilde V}$, which sends $D\phi\to D\phi-q\alpha\lambda_{\tilde V}$; the relabeling $\ell\to\ell-\frac{q\alpha}{2\pi}\lambda_{\tilde V}$ absorbs this if and only if $q\alpha\in2\pi\mathbb{Z}$. The electric $U(1)^{(1)}$ is broken explicitly to $\mathbb{Z}_q^{(1)}=\{\alpha\in\frac{2\pi}q\mathbb{Z}\}$, in every phase (Week 14 §8.1 for the cosine form).

(b) *Vortices and the flux quantum.* Since $d^2=0$,
$$
d(D\phi)=-q\,F-2\pi v,\qquad v\equiv qn+d\ell\in C^2(\Lambda,\mathbb{Z}),\tag{5.2}
$$
so wherever the condensate is rigid, $D\phi=0$, the magnetic flux through every plaquette is $F=-\frac{2\pi}qv$: it is quantized in units of $2\pi/q$, which for $q=2$ is $h/2e$ in units where the electron has charge 1.

(c) *Magnetic symmetry.* $dF=-2\pi\,dn$, so the magnetic $U(1)^{(d-3)}$ is exact if and only if $dn=0$ (the modified Villain constraint, Semester II Week 12), and then $dv=0$: vortex sheets close. With $n$ unconstrained the hopping term does not contain $n$, the twisted sheet at $2\pi m$ is still a relabeling, and $\tilde W_m=1$ identically, as in Week 11 §5.2.

### 5.2 The Meissner effect and the $\mathbb{Z}_q$ remnant [Computed in the London approximation; the $\kappa=\infty$ reduction Proved.]

Unitary gauge $\phi=0$ uses $\lambda=-\phi/q$ and leaves a $\mathbb{Z}_q$ gauge redundancy, $\lambda\in\frac{2\pi}q\mathbb{Z}$. In the London approximation, Gaussian in $a$ with $n=\ell=0$ (vortex and monopole integers suppressed at large β and κ),
$$
S\simeq\frac\beta2\|da\|^2+\frac{\kappa q^2}2\|a\|^2=\frac\beta2\big\langle a,(\delta d+m_A^2)\,a\big\rangle,\qquad m_A^2=\frac{q^2\kappa}\beta\qquad(\text{continuum: }m_A^2=q^2e^2\kappa),\tag{5.3}
$$
a massive vector. Since $\delta d$ and $d\delta$ commute with Δ and $\delta d\,d\delta=0$, its propagator is
$$
\langle a\,a\rangle=\frac1\beta(\Delta+m_A^2)^{-1}\Big(1+\frac{d\delta}{m_A^2}\Big),\qquad \langle W_k(C)\rangle=\exp\Big(-\frac{k^2}{2\beta}\big\langle J_C,(\Delta+m_A^2)^{-1}J_C\big\rangle\Big),\tag{5.4}
$$
the $d\delta$ term dropping on closed loops. A static magnetic field obeys $(-\nabla^2+m_A^2)B=0$ away from sources and decays over the London length $1/m_A$: this is the Meissner effect. Every probe $W_k$ has a perimeter law, with coefficient $\frac{k^2}{2\beta}G_{d-1,m_A}(0)$ by the massive (4.1), finite in every $d$ because the mass cuts off the infrared integral (4.3).

Which of these perimeter laws is spontaneous breaking? Only those of $W_k$ with $k\notin q\mathbb{Z}$, the lines charged under $\mathbb{Z}_q^{(1)}$; $W_q$ is neutral and screened in every phase (Week 14 §3.2). The London approximation cannot tell them apart, because it has dropped the vortices that carry the $\mathbb{Z}_q$ physics. The edge $\kappa=\infty$ keeps them: the hopping weight forces $D\phi=0$, so in unitary gauge $qa=-2\pi\ell$, $a=\frac{2\pi}q\,s$ with $s\in C^1(\Lambda,\mathbb{Z}_q)$, and
$$
S_{\kappa=\infty}=\frac\beta2\Big\|\frac{2\pi}q\,ds-2\pi n\Big\|^2,\tag{5.5}
$$
the $\mathbb{Z}_q$ Villain theory of [[sem2-week-02-zn-gauge-theory-as-bf-theory|Sem II Week 2]] (6.1) with $N=q$, whose deconfined phase flows to BF theory at level $q$ (Sem II Week 2 §6.1). At $q=2$ that is HOS eq. (14). The Wilson loop of a probe of charge $k$ is then the $\mathbb{Z}_q$ holonomy $e^{2\pi ik\oint s/q}$.

The magnetic side, in the monopole-free model, is the 't Hooft loop. Minimizing $\frac\beta2\|da-2\pi m\Xi\|^2+\frac{\kappa q^2}2\|a\|^2$, the classical $a$ solves $(\delta d+m_A^2)a=2\pi m\,\delta\Xi$; since $\delta\Xi$ is coexact, $(\delta d+m_A^2)^{-1}\delta\Xi=(\Delta+m_A^2)^{-1}\delta\Xi$, and on 2-cochains $1-d\delta(\Delta+m_A^2)^{-1}=(\delta d+m_A^2)(\Delta+m_A^2)^{-1}$. Therefore
$$
-\ln\langle\tilde W_m(\tilde C)\rangle_{\rm London}=2\pi^2m^2\beta\Big[\big\langle d\Xi,(\Delta+m_A^2)^{-1}d\Xi\big\rangle+m_A^2\big\langle\Xi,(\Delta+m_A^2)^{-1}\Xi\big\rangle\Big],\tag{5.6}
$$
an identity that holds in every $d$, checked against direct minimization for a random integer 2-cochain Ξ on a periodic $4^3$ lattice. The first term is the self-energy of the monopole loop with a short-range kernel, a perimeter term. The second depends on the sheet: for a flat sheet it is $m_A^2G_{d-2,m_A}(0)$ per plaquette by the massive (4.1), a tension. The Dirac sheet, invisible in Maxwell theory, has become the physical flux tube of the superconductor, and the minimal sheet gives an area law (Problem 6⋆). With the vortex integers restored the flux $2\pi m$ splits into $qm$ elementary tubes of flux $2\pi/q$, which lowers the tension and keeps the area law [Heuristic; GKSW §5.1 states the area law of the 't Hooft loop in the Higgs phase].

### 5.3 What is broken, what is unbroken, and what is explicit [the electric statements Controlled at $\kappa=\infty$ through (5.5) and Week 5 §5; the magnetic ones Computed in the London approximation (5.6), with the tube splitting Heuristic; Heuristic elsewhere]

In the superconducting (Higgs) phase at large β and κ:

1. $U(1)^{(1)}_e\to\mathbb{Z}_q^{(1)}$ is an **explicit** breaking, present in every phase (§5.1(a)). The charge of the matter fixes the residual group and the condensation does not; "the condensate Higgses the 1-form symmetry down to $\mathbb{Z}_2$" runs two steps together.
2. $\mathbb{Z}_q^{(1)}$ is **spontaneously broken**: at $\kappa=\infty$, (5.5) is in its deconfined phase for β above its transition, the lines $W_k$ with $k\notin q\mathbb{Z}$ obey a perimeter law, and the ground state is $q^2$-fold degenerate on the spatial $T^2$ and $q^3$-fold on $T^3$ at the soluble point (Week 14 (8.2) at $q=2$; Sem II Week 2 §7). The phase is gapped, so its infrared limit is a TQFT (GKSW §5.2), here BF at level $q$ ([[topological-order]]).
3. The magnetic symmetry depends on the model. In (5.1) as written $n$ is unconstrained, monopoles are dynamical and $\tilde W_m=1$ identically (§5.1(c)): the magnetic symmetry is explicitly broken in every phase. With $dn=0$ imposed, or in the continuum superconductor of HOS and GKSW, it is exact and **unbroken**, the 't Hooft loop having the area law (5.6); this is the Meissner effect in symmetry language.
4. No continuous symmetry is spontaneously broken, so nothing protects a massless photon, and (5.3) gives it a mass. The Goldstone mode of the Cooper-pair phase, which a neutral superfluid would keep, is absorbed (Week 14 §8.4).

The other phases depend on the model as well. The monopole-free model has no confined phase, since its gauge field is effectively non-compact. The compact model (5.1), like its cosine form, confines at small β, where $\mathbb{Z}_q^{(1)}$ is unbroken: the strong-coupling argument of Week 14 §3.5, with $U(1)$ plaquette charges reduced modulo $q$, gives $W_k$ with $k\notin q\mathbb{Z}$ an area law. In $d=4$ both models also have a Coulomb phase at large β and small κ, with the matter gapped: $\mathbb{Z}_q^{(1)}$ is broken there too, and the photon is massless because the long-distance Maxwell theory has an accidental electric $U(1)^{(1)}$, which is broken (GKSW §5.1). Figure 3 annotates the phase diagram of the compact model.

```
  κ ↑  κ = ∞: Wegner's ℤ₂ theory at the same β (cosine form), first order at β = 0.44069
    │ ══════════════════╤═══════════════════════════════════════════════
    │                    │  superconductor: ℤ₂^(1) broken (W₁ perimeter law),
    │  confined:         │  photon massive, BF at level 2, GSD 8 on T³
    │  ℤ₂^(1) unbroken,  │  at the soluble point
    │  W₁ area law,      ├───────────────────────────────────────────────  Higgs line
    │  photon massive    │  Coulomb: ℤ₂^(1) broken, accidental U(1)_e^(1)
    │                    │  broken, photon massless (its Goldstone boson)
    └────────────────────┴───────────────────────────────────────────────→ β
    0        β_T = 1.0111331(21) at κ = 0 (Wilson action)                 ∞
```
**Figure 3. The (β, κ) plane of compact four-dimensional $U(1)$ gauge theory with charge-2 matter in the cosine form (Week 14 (8.1)), annotated by the realization of the exact $\mathbb{Z}_2^{(1)}$; schematic, with the edge values of Week 14 §8.2 and of Arnold–Bunk–Lippert–Schilling for the pure theory. Monopoles are dynamical, so the magnetic symmetry is explicitly broken throughout; the monopole-free model has no confined region. The confinement boundary separates phases that realize the exact symmetry differently, so it cannot be crossed analytically; the Coulomb–Higgs boundary is the loss of the massless photon.**

> **Physical picture.** An experiment cannot place a superconductor on a torus with periodic electromagnetism, but it sees the ingredients of points 1–4: flux enters in quanta $h/2e$, a quasiparticle of odd charge acquires the phase $-1$ around each quantum, and a magnetic field is expelled over the London length. The exact content is the lattice chain §5.1(a) → (5.5) → the deconfined phase of Wegner's model; the physical conditions are the assumptions of Week 14 §8.4, of which the dimension of electromagnetism matters most, since a film coupled to the electromagnetic field of $3+1$ dimensions keeps a gapless in-plane mode. For the research line, a condensate of charge $k$ leaves ${\rm Ann}(\langle k\rangle)$ (Week 14 §3.3) and level-$k$ BF theory, and Semester II Week 14 relates this arithmetic to subgroup gauging on a hypersurface, the setting of the group's manuscript in preparation (forward reference).

## 6. The Semester I realizations, justified

Week 15 Table 3 lists the realization of every symmetry of Semester I. Table 2 does not repeat it; it gives, row by row, the argument of this week that makes each entry a consequence of (2.1), (3.1) or (4.3), and adds the rows that are new.

| Week 15 Table 3 row | Why, from this week |
|---|---|
| 2d XY; shift $U(1)^{(0)}$, unbroken in both phases | (4.3) at $p=0$, $d=2$: $G_2(0)$ diverges in the infrared, so $\langle e^{i\theta}\rangle=0$ (Mermin–Wagner; Sem I Week 1 §3.5); the power law at low $T$ is the marginal case $d-p=2$ |
| 2d XY; winding $U(1)^{(0)}$, explicitly broken, emergent at low $T$ | the vortex fugacity breaks it (Week 3 §6.1) and is irrelevant for $\pi\beta_R>2$ (Week 4 §2), where the symmetry is emergent (F5); a continuous 0-form symmetry could not break in $d=2$ in any case (Table 1) |
| 2d Ising; $\mathbb{Z}_2^{(0)}$, broken for $K>K_c$ | a discrete 0-form symmetry may break for $d\ge2$ (Table 1); no Ward identity forces a gapless mode (F7), and the ordered phase is gapped (Week 4 §3) |
| 3d and 4d $\mathbb{Z}_2$ gauge; electric $\mathbb{Z}_2^{(1)}$, broken at weak coupling | (2.1) with the perimeter law $\mu=2e^{-4(d-1)\beta}$ of Week 5 §5 and the area law of Week 5 §4; a discrete 1-form symmetry may break for $d\ge3$ (Table 1); no Ward identity forces a gapless mode (F7), and the deconfined phase is gapped, with BF theory as its infrared limit; the degeneracy is Sem II Week 2 §7 |
| 3d $\mathbb{Z}_2$ gauge; magnetic $\mathbb{Z}_2^{(1)}$, emergent only | visons are dynamical at finite β ([[courses/generalized-symmetries-course/conventions|conventions]] §6), so no topological operator exists; in the deconfined phase they are gapped and the symmetry is emergent (F5), realized as in the BF limit of Sem II Week 2 §7; in the confined phase they condense (Week 5 §7.3) |
| compact QED₃; electric $U(1)^{(1)}$, unbroken at every β | forbidden by (4.3), since $p=d-2$; the monopole-free theory gives the logarithm (4.2), compact QED₃ the area law of Week 10 §5. Both are unbroken: Polyakov's mechanism changes the magnetic realization and leaves the electric one as it was |
| compact QED₃; magnetic $U(1)^{(0)}$, explicitly broken | broken spontaneously without monopoles, with σ as Goldstone boson, (3.10)–(3.11); the monopoles add a term to the action and σ becomes a pseudo-Goldstone boson (Week 9 §5.3) |
| compact QED₄; electric $U(1)^{(1)}$, broken (Coulomb), unbroken (confining) | (3.9) is exact; the Coulomb perimeter law (Guth) and §3.1 force the massless photon that Fröhlich–Spencer prove; the confining area law allows the gap |
| compact QED₄; magnetic $U(1)^{(1)}$, explicitly broken, emergent and broken in the Coulomb phase | $\tilde W_m=1$ identically (Week 11 §5.2), so no exact symmetry in either phase; in the Coulomb phase the infrared probe obeys (3.6) with $\tilde e=2\pi/e$ |
| compact QED₄ at θ; as at θ = 0, monopoles carrying charge $\theta n_m/2\pi$ | the classification by $G$ and an unbroken subgroup $K$ of GKSW §7.2 includes oblique phases: with a condensed dyon $w$, the lines with $\langle v,w\rangle\ne0$ have an area law and those with $\langle v,w\rangle=0$ are screened; the status is that of Week 12 §§7.2–7.4 (Heuristic) |
| $\mathbb{Z}_2$ gauge–Higgs; no exact electric symmetry | the matter current enters (3.9) (Problem 3), so the perimeter laws are screening |
| $\mathbb{Z}_N$ with charge $q$; residual $\mathbb{Z}_r^{(1)}$ | exact by Week 14 (3.3); discrete, so no Ward identity forces a gapless mode; (2.1) applied to $W_e$ with $e\notin H$ |
| thermal center, order parameter $\langle L\rangle$ | on $S^1\times\mathbb{R}^{d-1}$ the 1-form symmetry contains a 0-form symmetry of the reduced theory, whose order parameter is the local operator $L$ (GKSW §5.1; Problem 5⋆) |
| $U(1)$ with charge 2; residual $\mathbb{Z}_2^{(1)}$, broken | §5.3, points 1–4 |
| *new:* free Maxwell, $d=4$; both $U(1)^{(1)}$ | both broken, (2.6) and (3.6); the photon is the Goldstone boson of both (§3.2) |
| *new:* free Maxwell, $d=3$; electric $U(1)^{(1)}$, magnetic $U(1)^{(0)}$ | electric unbroken (marginal), (4.2); magnetic broken, (3.11) |
| *new:* Maxwell, $d=2$; electric $U(1)^{(1)}$ | unbroken, the linear potential (4.2) |
| *new:* abelian Higgs, monopole-free; magnetic $U(1)^{(d-3)}$ | unbroken in the superconductor, (5.6); broken in the Coulomb phase |

**Table 2. Why the realizations of Week 15 Table 3 hold, with the rows this week adds.**

Corrections (i) and (ii) of §1 are the gauge–Higgs, charge-$q$ and magnetic compact-QED₄ rows: in each, the symmetry that the slogan invokes is broken explicitly, entirely or down to a subgroup.

## 7. Seminar: Hansson, Oganesyan and Sondhi

**Format.** The presenter states the paper's technical claim, identifies what it needs from Semester I and reproduces one nontrivial step at the board; discussion follows, and the instructor closes by placing the result on the course map (syllabus §7). Every student reads the sections beforehand and brings Problem 3.

**Sections.** HOS §I.C and §II (no local order parameter), §III (excitations, fractionalization and the BF action: eqs. (12)–(16) and the derivation of §III.C, eqs. (23)–(29)), §IV (ground-state degeneracy, with §IV.D for $d=3+1$, eqs. (47)–(48)), and §V.A–B (the $\mathbb{Z}_2$ lattice gauge theory and the $U(1)$ lattice gauge theory with charge-2 Higgs).

**The technical claim.** An s-wave superconductor coupled to dynamical electromagnetism has no local order parameter but is topologically ordered in Wen's sense: its low-energy theory is the topological action (14), $\frac1\pi\epsilon^{\mu\nu\sigma}b_\mu\partial_\nu a_\sigma$ in $2+1$ dimensions and its 2-form analog (18) in $3+1$, whose quantization gives a degeneracy on the torus and the phase $\pi$ of a quasiparticle around a vortex.

**What it needs from Semester I.** Week 14 §8 (the residual $\mathbb{Z}_2^{(1)}$ and the $\kappa=\infty$ edge), Week 5 §§7–8 (Wegner's deconfined phase and its closed sheets), Week 7 (the Kogut–Susskind $\mathbb{Z}_2$ Hamiltonian), and Sem II Week 2 §§2–3 and 6.1.

**The step at the board.** HOS §III.C: starting from the London limit of the abelian Higgs model at fixed vortex configuration, parametrize the vortex current by the curl of $a$ (26), impose the constraint with the multiplier $b_\mu$ (27), shift the massive gauge field and integrate it out, and read off the coefficient $\frac1\pi$ of (14). Then translate into the course's normalization: $\frac1\pi=\frac N{2\pi}$ at $N=2$, the weight $\frac{iN}{2\pi}\int b\wedge da$ of Sem II Week 2 §2.1, with Minkowski signature and HOS's charge $-2e$ for the pair field converted first. Close by comparing with the lattice route (5.5) and Sem II Week 2 §6.1, which reaches the same level without a derivative expansion.

**For the discussion.** What HOS §II's absence of a local order parameter becomes in GKSW's language: the charge-1 Wilson loop with a perimeter law, a nonlocal order parameter of a broken $\mathbb{Z}_2^{(1)}$ (§5.3). Why the relativistic model of HOS has equal electric and magnetic screening lengths, and what changes for a real metal (Week 14 §8.4). HOS §V.B's observation that the compact lattice model has a massive photon on both sides of its transition, and which exact symmetry nonetheless separates the phases (Figure 3).

**The open question it leaves for this course.** HOS work with a non-compact gauge field and add vortices by hand. With a compact gauge field and dynamical monopoles the magnetic symmetry is explicitly broken (§5.1(c)); whether the residual $\mathbb{Z}_2^{(1)}$ and the magnetic $U(1)^{(d-3)}$ can both be exact in a lattice model is answered by the modified Villain formulation (Semester II Week 12), and the level-$k$ generalization as subgroup gauging belongs to Block 5.

**On the course map.** The lattice chain is Week 14 §8; the symmetry realization is §5.3 of this note; the BF limit is Sem II Week 2 §6.1; gauging the broken $\mathbb{Z}_2^{(1)}$ is the second part of Mini-calculation 1 in [[sem2-week-04-gauging-backgrounds-and-dual-symmetry|Sem II Week 4]]; the Hamiltonian of the same phase is the toric code of Sem II Week 8.

## 8. Subtleties and fine print

**F1. The counterterm is not an observable, and neither is the constant.** The coefficient μ of (2.5) depends on the regularization, on the action (Villain or Wilson) and on the direction of the line on the lattice; in the continuum limit it diverges as $1/a$. The constant left after subtraction, such as $e^{q^2e^2/4}$ in (2.6), can be shifted by the local term $\oint k_g\,ds=2\pi$, the integrated geodesic curvature of a planar loop. Only the dichotomy of (2.1), zero against bounded away from zero, is physical.

**F2. Corners in gapless phases.** In the Coulomb phase each corner adds a power of the size, (2.8) and Problem 7⋆, because the cusp coefficient multiplies an infrared logarithm. Rectangles with $T\gg R$ add the Coulomb term $e^{q^2e^2T/4\pi R}$ (Problem 2). The criterion therefore dilates a fixed shape and asks only for a lower bound. In gapped phases corners and ends contribute constants.

**F3. Genuine lines only.** GKSW §5 restrict the diagnostic to lines whose definition needs no surface. The improperly quantized 't Hooft loop $\tilde W_\alpha$ with $\alpha\notin2\pi\mathbb{Z}$ of Week 11 §5.3 is the boundary of an electric symmetry surface, and the vison of Week 5 §7.3 is its lower-dimensional analog, a point attached to a string of flipped plaquettes. Such expectation values depend on the attached surface or string and diagnose nothing about the symmetry it generates.

**F4. Infinite volume, the torus and the zero mode.** A broken 1-form symmetry produces no degeneracy on $\mathbb{R}^D$, since there the symmetry operators on closed surfaces measure enclosed charge and act trivially on the vacuum; degeneracies need noncontractible cycles. On the spatial $T^3$ the Coulomb phase has a unique ground state, and the electric flux sectors cost $\frac{g^2n^2}{2L}$ (flux $n$ spread over $L^2$ links of each of $L$ cross-sections in the Kogut–Susskind energy $\frac{g^2}2\sum E^2$), of the same order in $1/L$ as the photon gap $2\pi/L$; no clean tower separates from the rest of the spectrum. Likewise (3.11) is a statement about a pure infinite-volume state: on the torus the zero-mode integral averages $\langle e^{i\sigma}\rangle$ to zero (Week 9 §5.2). For continuous groups the Euclidean criterion (2.1) is the definition.

**F5. Exact versus emergent.** An emergent symmetry has no topological operator at the cutoff. Its "breaking" refers to probes defined in the long-distance theory, such as the external static monopole of the Coulomb phase, which is a different operator from the lattice loop $\tilde W_m=1$ (Week 11 §5.2). Statements about emergent symmetries carry no exact consequence.

**F6. Order of limits.** The criterion takes the loop large at fixed cutoff. On a thermal circle the order matters again: a line that wraps the circle is a local operator of the reduced theory, and the 1-form symmetry splits into a 0-form and a 1-form symmetry of $\mathbb{R}^{d-1}$ (GKSW §5.1; Problem 5⋆), whose realizations differ.

**F7. Discrete groups have no Ward identity.** The identity (3.1) and the Goldstone conclusion need a continuous group, and nothing forces a gapless mode when a discrete symmetry breaks. Whether the broken phase is gapped is a separate question: the deconfined $\mathbb{Z}_N$ theory and the superconductor are gapped, and then the infrared limit is a TQFT (GKSW §5.2; Sem II Week 2), while the Coulomb phase of Figure 3 breaks $\mathbb{Z}_q^{(1)}$ and keeps a massless photon, protected by its accidental continuous symmetry. The finite twisted sheets of §5.1(a) survive although the infinitesimal identity (3.9) acquires the matter current: a residual discrete symmetry is a finite statement.

**F8. Gaplessness does not imply breaking.** In three-dimensional Maxwell theory the photon is massless while the electric 1-form symmetry is unbroken (the logarithm of (4.2)); the photon is the Goldstone boson of the magnetic 0-form symmetry instead. The theorem of §3.1 runs in one direction only.

## 9. Common misconceptions

1. *"A perimeter law always signals spontaneous breaking."* It is tempting because the dichotomy of Week 5 was introduced in a model with an exact symmetry. With charged matter every Wilson loop has a perimeter law, by string breaking, and the Higgs phase is gapped. The correct statement is (2.1) for an exact symmetry; without one, a perimeter law is screening (§3.3, Problem 3).
2. *"The photon of compact QED₄ is the Goldstone boson of the broken magnetic 1-form symmetry."* It is tempting because it is true in free Maxwell theory (§3.2), as GKSW state for the continuum. In the Villain theory the Coulomb photon is the Goldstone boson of the exact electric symmetry, (3.9), and of the magnetic one only at long distances (§3.3).
3. *"A superconductor spontaneously breaks the electromagnetic $U(1)$."* It is tempting because the Ginzburg–Landau field acquires an expectation value in unitary gauge. Elitzur's theorem forbids breaking a gauge symmetry (Week 5 §3; HOS §II). What happens is an explicit breaking of $U(1)^{(1)}_e$ to $\mathbb{Z}_2^{(1)}$ by the charge of the pairs and a spontaneous breaking of $\mathbb{Z}_2^{(1)}$ by the condensate, with the magnetic symmetry unbroken where it is exact (§5.3).

## 10. Historical note

The loop criteria of Wilson and 't Hooft and the rigorous Coulomb phase of Guth and of Fröhlich and Spencer are the history of Weeks 6, 11 and 15. At finite temperature the center symmetry and its order parameter, the Polyakov loop, were in place by 1978–79 (Week 14 §4); at zero temperature the criteria remained statements about loops and fluxes. The Landau language for them entered with Gaiotto, Kapustin, Seiberg and Willett (2014), whose §5 recasts the criteria of Wilson and 't Hooft as the realization of a 1-form symmetry, identifies the photon as a Goldstone boson through the matrix element (5.1), and transfers Coleman–Mermin–Wagner by compactifying on tori; the general Goldstone theorem was proved in 2018 by Hofman and Iqbal and sketched by Lake. A decade before GKSW, Hansson, Oganesyan and Sondhi had argued in Wen's language that a superconductor has no local order parameter and is described by a BF theory at level 2, and their §V.B already pointed to the charge-2 lattice model of Fradkin and Shenker; the identification of its order with a broken $\mathbb{Z}_2^{(1)}$ is GKSW §5.1.

## 11. What to take away

1. **Order parameter.** An exact 1-form symmetry is broken when large genuine charged lines keep an expectation value bounded away from zero after a local counterterm (2.1). The counterterm is the self-energy of an isolated probe, (2.2) and (2.5); physically, a perimeter law says that isolated charges have finite energy.
2. **Goldstone.** The Ward identity forces the flux of a charged line through every sphere around it; in the broken phase it must spread as $1/r^2$, which is a massless pole (3.3). In free Maxwell theory the photon is the Goldstone boson of both 1-form symmetries; in compact QED₄ it is protected by the exact electric symmetry (3.9).
3. **Dimension.** A flat $p$-dimensional object sees the $(d-p)$-dimensional Green function (4.1), so the infrared integral (4.3) is ordinary Coleman–Mermin–Wagner in the transverse dimensions: continuous $p$-form symmetries break only for $p\le d-3$, discrete ones for $p\le d-2$.
4. **Superconductor.** The charge of the pairs breaks $U(1)^{(1)}_e$ explicitly to $\mathbb{Z}_q^{(1)}$, and the condensate breaks $\mathbb{Z}_q^{(1)}$ spontaneously, which gives the flux quantum $2\pi/q$ and the level-$q$ BF theory. The magnetic symmetry is unbroken where it is exact (monopole-free lattice, continuum), which is the Meissner effect, and explicitly broken when monopoles are dynamical. No continuous symmetry is broken, so the photon may be massive.

## 12. Looking ahead

[[sem2-week-04-gauging-backgrounds-and-dual-symmetry|Sem II Week 4]] couples the discrete symmetries of this week to background fields and sums over them. Gauging a $\mathbb{Z}_N^{(p)}$ symmetry produces a dual $\mathbb{Z}_N^{(d-p-2)}$: for $p=0$ in $d=2$ this is Kramers–Wannier, and for the broken $\mathbb{Z}_2^{(1)}$ of the deconfined phase in $d=3$ it is the second part of Mini-calculation 1. In Block 3, Sem II Week 8 writes the phase of §5 as the toric code, where topological order is defined and the broken $\mathbb{Z}_2^{(1)}$ with its emergent partner becomes the anyon content. Sem II Week 12 then builds the modified Villain lattice in which the magnetic symmetry of §§3.3 and 5.1(c) is exact.

## 13. Problem set

Problems 1–4 are the classroom core and are solvable from the note alone; Problems 5⋆–7⋆ are self-study consolidation with hints; Problem 8⋆⋆ is a research extension that states what is known, what is explored, the sources and what counts as completion.

**Core problems** (everyone).

**1. Two-form symmetries and the winding symmetry of the 4d XY model.** (Extends §4.) (a) A compact 2-form gauge field $B\in C^2$ with action $\frac{\rho}2\|dB\|^2$ has charged surfaces $e^{iq\sum_SB}$. Using Feynman gauge and (4.1) twice, find the coefficient per plaquette of $-\ln\langle e^{iq\sum_SB}\rangle$ for a large flat surface, and the lowest $d$ in which a continuous 2-form symmetry can break. (b) In $d=4$ evaluate the leading growth of $-\ln\langle e^{iq\sum_SB}\rangle$ for an $L\times L$ surface. (c) The winding 2-form symmetry of the four-dimensional XY model ([[courses/generalized-symmetries-course/conventions|conventions]] §6, degree $d-2$) is explicitly broken by dynamical vortex sheets and emergent in the ordered phase, where its charged surfaces are, in the dual description, the surfaces of (a). Decide whether it is broken, and give the physical reason in terms of the energy per unit length of a global vortex line in three-dimensional space.

**2. Rectangles and the Coulomb term.** (Extends §2.4.) With the point-splitting regulator, (a) show that the interaction of the two sides of length $T$ at separation $R$ contributes $+\frac{q^2e^2}{4\pi^2}I(R,T)$ to $\ln\langle W_q\rangle$, with $I(R,T)=\int_0^T\!\int_0^T\frac{ds\,dt}{(s-t)^2+R^2}$, and evaluate $I$ in closed form. (b) Show that under dilation at fixed aspect ratio $\rho=T/R$ the opposite-side terms give a scale-independent constant $c(\rho)$, and compute $c(1)$. (c) At fixed $R$ and $T\to\infty$, recover the Coulomb term of (4.2), and explain why (2.1) dilates a fixed shape.

**3. The Ward identity with matter.** (Extends §§3.3 and 5.1.) For the action (5.1) and a probe $W_k(C)$, derive the lattice Schwinger–Dyson identity that replaces (3.9). Show that the flux of $\beta\langle F\rangle$ out of a box around one point of the line is no longer fixed by $k$, identify the term responsible, and explain why the twisted sheets with $\alpha\in\frac{2\pi}q\mathbb{Z}$ remain topological although no conserved current survives.

**4. The circular loop in three dimensions.** (Extends §§2.4 and 4.2.) With the regulated propagator $e^2\delta_{\mu\nu}/4\pi\sqrt{x^2+a^2}$ of three-dimensional Maxwell theory, compute $\ln\langle W_q\rangle$ for a circle of radius $R\gg a$, and show that no local counterterm keeps it bounded away from zero.

**Starred problems** (Ph.D. expected; ambitious M.Sc. encouraged).

**5⋆. The thermal reduction.** (Extends F6 and Table 2.) Put four-dimensional Maxwell theory on a thermal lattice with $N_\tau$ slices and compute the Polyakov-loop correlator $\langle L_q(\vec x)L_q(\vec 0)^\dagger\rangle$ at large $|\vec x|$, with $L_q=e^{iq\sum_\tau a_\tau}$. Decide which symmetry of the reduced three-dimensional theory it probes and whether it is broken, and do the same for spatial Wilson loops. *Hint:* the sum over a full period of the periodic Green function is $G_3$, and the spatial loops see three-dimensional Maxwell theory with coupling $e^2T$; compare GKSW §5.1.

**6⋆. The 't Hooft loop in a London superconductor.** (Extends (5.6).) For a flat sheet in $d=4$ compute the tension of the second term of (5.6), using the massive (4.1) and $G_{2,m}(0)\simeq\frac1{4\pi}\ln\frac{32}{m^2}$ for small $m$, which follows from $a(x)$ of [[courses/generalized-symmetries-course/conventions|conventions]] §2 and the small-argument form of $K_0$. Compare with the London energy per unit length of a flux tube, and estimate the gain when the flux $2\pi m$ splits into $qm$ tubes. *Hint:* use $\beta m_A^2=q^2\kappa$; the tension of a London tube is quadratic in its flux.

**7⋆. A corner of any angle.** (Extends (2.7)–(2.8).) Two straight sides of length $L$ meet at a corner with deflection angle θ (θ = 0 for a straight line, θ = π/2 for the square). Show that the corner contributes $\frac{q^2e^2}{4\pi^2}(1-\theta\cot\theta)\ln\frac La$ to $\ln\langle W_q\rangle$, check the square, and discuss θ → π. *Hint:* the cross term needs $\int_0^\infty\frac{d\tau}{\tau^2+2\tau\cos\theta+1}=\frac\theta{\sin\theta}$; add the endpoint terms of (2.7).

**⋆⋆ problem** (research extension; optional).

**8⋆⋆. The broken-symmetry Ward identity in a simulation.**
*What is known.* The identity (3.9) holds exactly at every β for the Villain and Wilson actions; the Coulomb phase exists and its photon is massless (Guth; Fröhlich–Spencer); for the Wilson action the transition is first order at $\beta_T=1.0111331(21)$ (Arnold, Bunk, Lippert, Schilling, hep-lat/0210010).
*What is explored.* Measure the normalized field around a pair of Polyakov loops, $\beta\langle\sin(da)_P\,L_q(\vec0)L_q(\vec R)^\dagger\rangle/\langle L_qL_q^\dagger\rangle$, on both sides of $\beta_T$; verify that its flux out of boxes around one charge is $iq$ in both phases, as (3.9) demands, and that its profile is $1/r^2$ in the Coulomb phase and a tube in the confining phase.
*Sources.* Week 11; [[week-10-polyakov-mass-gap-area-law|Week 10]] §5.5 for a lattice protocol; the paper map entries cited above.
*Completion.* Profiles with statistical errors on lattices of at least $16^4$ at two couplings on each side of $\beta_T$, with the flux check passed to its error and the decay exponent of the Coulomb profile fitted.

## Self-study answer checkpoints

These checkpoints cover the core problems; starred and ⋆⋆ problems remain source-led.

1. **Two-form symmetries.** The decisive step is that the Laplacian acts componentwise on 2-cochains, so Feynman gauge gives $\langle B_PB_{P'}\rangle=\delta_{S_PS_{P'}}G_d(x_P-x_{P'})/\rho$, and (4.1) applied in the two directions of the surface gives (a) $\frac{q^2}{2\rho}G_{d-2}(0)$ per plaquette, finite if and only if $d\ge5$. (b) In $d=4$, $G_2$ with infrared cutoff $1/L$ gives $-\ln\langle\cdot\rangle\simeq\frac{q^2}{4\pi\rho}L^2\ln\frac La$. (c) Unbroken, the marginal case $d-p=2$: a global vortex line costs $\frac\beta2\int(\nabla\theta)^2=\pi\beta\ln\frac La$ per unit length, which grows with the system, so vortex worldsheets cannot be free. A common failure is to apply the bound $p\le d-3$ to the shift symmetry of θ, which is a 0-form symmetry and is broken in $d=4$.
2. **Rectangles.** The decisive step is the sign: antiparallel sides have $dx\cdot dy=-ds\,dt$, and the two ordered pairs give $-\frac{q^2e^2}2\cdot2\cdot(-1)\frac{I}{4\pi^2}$. (a) $I(R,T)=2\rho\arctan\rho-\ln(1+\rho^2)$. (b) $c(\rho)=\frac{q^2e^2}{4\pi^2}\big[2\rho\arctan\rho-\ln(1+\rho^2)+\frac2\rho\arctan\frac1\rho-\ln(1+\rho^{-2})\big]$ and $c(1)=\frac{q^2e^2}{4\pi^2}(\pi-2\ln2)=0.04446\,q^2e^2$. (c) For $\rho\to\infty$, $\frac{q^2e^2}{4\pi^2}(\pi\rho-2\ln\rho-2)$, whose first term is $\frac{q^2e^2T}{4\pi R}$, the Coulomb term $-TV$ of (4.2); at fixed $R$ the subtracted loop grows without bound, so only a fixed shape gives a meaningful limit. A common failure is to drop the factor 2 of the ordered pairs.
3. **Ward identity with matter.** The decisive step is $\partial S/\partial a_\ell=\beta(\delta F)_\ell-q\kappa(D\phi)_\ell$ (checked by finite differences), so that $\big\langle\big[\beta(\delta F)_\ell-q\kappa(D\phi)_\ell\big]W_k(C)\cdots\big\rangle=ik\,J_C(\ell)\langle W_k(C)\cdots\rangle$. Summed over the time-like links of a box in a time slice, the flux of $\beta\langle F\rangle$ out of the box is $ik$ plus the matter charge inside it, $q\kappa$ times the sum of $\langle D\phi\rangle_W$ over those links: the screening cloud can cancel $ik$. The finite sheets survive because their effect, $D\phi\to D\phi-q\alpha\lambda_{\tilde V}$, is an integer relabeling of ℓ exactly when $q\alpha\in2\pi\mathbb{Z}$: the residual $\mathbb{Z}_q^{(1)}$. A common failure is to conclude from the loss of the infinitesimal identity that no symmetry survives.
4. **Circle in three dimensions.** The decisive step is the angular integral $\int_0^{2\pi}\frac{\cos\phi\,d\phi}{\sqrt{4\sin^2(\phi/2)+\epsilon^2}}=2\ln\frac8\epsilon-4+O(\epsilon)$, so $\oint\oint dx\cdot dy\,D_a=R\big(\ln\frac{8R}a-2\big)$ and $\ln\langle W_q\rangle=-\frac{q^2e^2}2R\big(\ln\frac{8R}a-2\big)$ (checked against quadrature). The term $R\ln R$ is not of the form $\mu|C|$, so $\langle W\rangle e^{\mu|C|}\to0$ for every μ: unbroken, the marginal case of (4.3). A common failure is to use the four-dimensional propagator, which gives the convergent result (2.6).

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester II Block 1. Written to the note-quality-template standard on 2026-10-01. Last revised 2026-10-04.*
