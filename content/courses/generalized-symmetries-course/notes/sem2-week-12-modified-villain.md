---
title: "Sem II Week 12 — Modified Villain: Exact Dualities and Exact Higher-Form Symmetries on the Lattice"
type: lecture-notes
course: syllabus
semester: 2
week: 12
block: 4
duration: 4 hours (3 hr lectures + 1 hr seminar)
prerequisites: Semester I Weeks 3, 8, 11 and 12; Sem II Weeks 1, 3, 4 and 6
modified: 2026-10-03
---

# Sem II Week 12 — Modified Villain: Exact Dualities and Exact Higher-Form Symmetries on the Lattice

> *Semester I left a list of near misses. The Villain XY model was self-dual only after a dilute-gas step ([[week-03-villain-form-xy-duality|Sem I Week 3]]); Villain $U(1)$ in four dimensions was dual to a theory with electric matter ([[week-08-dual-variables-abelian-gauge|Sem I Week 8]]); its magnetic symmetry was only emergent and its lattice 't Hooft loop identically 1 ([[week-11-monopole-condensation-4d|Sem I Week 11]]); and the lattice θ-term was $2\pi$-periodic only without monopoles ([[week-12-theta-terms-witten-effect|Sem I Week 12]]). All four come from summing the field strength $dn$ of the Villain integer freely. This week a Lagrange multiplier on the dual lattice imposes $dn=0$: the integer becomes a flat $\mathbb{Z}$ gauge field, the multiplier becomes the dual field, and every item on the list becomes exact on a finite lattice, prefactors included. Week 13 builds non-invertible defects from the self-duality derived here.*

### How to use this chapter

- **In class:** first hour, the construction (§2.1), the exact self-duality (2.3)–(2.7) with Figure 1, and the 2×2 check of §2.3; Problem 1. Second hour, the exact symmetries of §2.4 (Figure 2), monopole-free compact QED and its magnetic operator (§§3.1–3.2, Figure 3), the statement (3.4); Problem 2. Third hour, the $\mathbb{Z}_N$ background (§§4.1–4.2) and the θ-term sealed (§5.1); Problems 3–4. The seminar hour (§7) is GLSS, presented by the instructor.
- **For self-study:** §§3.3, 4.3, 5.2, 6 and 8–10, and Problems 5⋆–7⋆. The one calculation to do alone: rerun §2.2 for four-dimensional Maxwell theory, where (2.3) carries the opposite sign, and recover $\tilde n=-\star m$ and the dual multiplier $a^\vee=-a$ of §3.3.
- **Instructor checkpoint:** three errors recur. The multiplier must be integrated over one period, or the constraint carries a divergent factor (F3). The sign of the summation by parts (2.3) depends on the degree, and so does the sign of a defect operator: the charge-$q$ monopole operator of $d=3$ is $e^{+iq\sigma}$, while the charge-$m$ 't Hooft line running forward in time in $d=4$ is $e^{-im\sum\tilde a}$, because the Hodge map gives a spatial cube the sign $-1$ in four dimensions (§3.2). And θ-periodicity is a property of the integrated weight: off the constraint surface $Q_{\rm lat}$ need not be an integer, and on 't Hooft lines θ → θ + 2π acts by the Witten effect (F5).

## 0. Reading

**Primary:** Gorantla, Lam, Seiberg, Shao (GLSS), arXiv:2103.01257, §1.2 and Apps. B.1 and C.1, the seminar paper (§7); Sulejmanpasic and Gattringer, arXiv:1901.02637, §§1–3, where the multiplier that removes monopoles was introduced.

**Secondary:** Sem I Week 3 §§2–5 and Week 8 §§5–6, reread with this week in mind; Chen and Tata, arXiv:2106.05274, for the cup products of §5; Shao's TASI lectures, arXiv:2308.00747, the companion for Blocks 4–5.

**Optional research reading:** José, Kadanoff, Kirkpatrick, Nelson, *Phys. Rev. B* 16 (1977) 1217; Banks, Myerson, Kogut, *Nucl. Phys. B* 129 (1977) 493; Choi, Córdova, Hsin, Lam, Shao, arXiv:2111.01139, and Kaidi, Ohmori, Zheng, arXiv:2111.01141, for Week 13 and Problem 8⋆⋆.

Proof-status labels follow note-quality-template §4; cochains, the Hodge map and cup products follow [[courses/generalized-symmetries-course/conventions|conventions]] §§1–2 and 8. The sign of the multiplier term in (2.1) and (3.1) is fixed so that the multiplier is the dual field of [[courses/generalized-symmetries-course/conventions|conventions]] §5; GLSS (B.6) and (C.5) write the opposite sign.

## 1. Motivation and setting

Every Semester I duality was exact; what failed was the form of the answer, and in each case of the epigraph the culprit was a defect summed freely. The question of the week is whether the defects can be removed without leaving the lattice, and what remains. The answer of Sulejmanpasic–Gattringer and GLSS is a constraint: the Villain integer is already a $\mathbb{Z}$ gauge field, and a compact multiplier on the dual lattice makes it flat. The resulting modified Villain (MV) theories are free compact theories with exact self-dualities, higher-form symmetries and θ-periodicity. The physics of the defects (BKT, Polyakov's mass gap, confinement) is absent from the MV theory and recoverable from it: the defects return as its operators, and summing them with unit weight gives back the Villain theories exactly (§6).

## 2. The modified Villain XY model

### 2.1 The integer as a flat $\mathbb{Z}$ gauge field [Proved.]

Consider the $L_1\times L_2$ periodic lattice Λ, with $N_0$ sites, $N_1=2N_0$ links and $N_2=N_0$ plaquettes, and its dual Λ*, the same torus shifted by $(\tfrac12,\tfrac12)$ ([[courses/generalized-symmetries-course/conventions|conventions]] §2). The modified Villain XY model is
$$
Z_{\rm MV}[\Lambda;\beta]=\prod_x\int_{-\pi}^{\pi}\frac{d\theta_x}{2\pi}\prod_{\tilde x}\int_{-\pi}^{\pi}\frac{d\tilde\theta_{\tilde x}}{2\pi}\sum_{n\in C^1(\Lambda,\mathbb{Z})}\exp\Big(-\frac\beta2\|d\theta-2\pi n\|^2+i\langle\tilde\theta,\star dn\rangle\Big),\tag{2.1}
$$
where θ is the compact scalar on the sites, $n$ the Villain integer ([[villain-action]]), $\tilde\theta\in C^0(\Lambda^*)$ a second compact field on the dual sites, and $\langle\tilde\theta,\star dn\rangle=\sum_P\tilde\theta(P^*)(dn)_P$, since the Hodge map sends a plaquette to its center with sign $+1$; β is dimensionless. The redundancy $\theta\to\theta+2\pi k$, $n\to n+dk$ ($k\in C^0(\Lambda,\mathbb{Z})$) is a $\mathbb{Z}$ gauge transformation with $n$ as gauge field, which makes θ compact; its field strength is the vorticity $v=dn$. The redundancy $\tilde\theta\to\tilde\theta+2\pi\tilde k$ holds because $\star dn$ is an integer, so $\tilde\theta$ is compact too. Integrating it with the last identity of [[courses/generalized-symmetries-course/conventions|conventions]] §3,
$$
\prod_{\tilde x}\int_{-\pi}^{\pi}\frac{d\tilde\theta_{\tilde x}}{2\pi}\,e^{i\tilde\theta_{\tilde x}(\star dn)_{\tilde x}}=\prod_P\delta_{(dn)_P,0},\qquad
Z_{\rm MV}[\Lambda;\beta]=\sum_{\substack{n\in C^1(\Lambda,\mathbb{Z})\\ dn=0}}\ \prod_x\int_{-\pi}^{\pi}\frac{d\theta_x}{2\pi}\,e^{-\frac\beta2\|d\theta-2\pi n\|^2}:\tag{2.2}
$$
the Villain model with its sum restricted to flat $\mathbb{Z}$ gauge fields, the vortices removed configuration by configuration. A core energy $\kappa\sum v^2$ with κ → ∞ gives the same (2.2) (GLSS (B.5)); the multiplier form is the one we can dualize.

### 2.2 Exact self-duality on the torus [Proved.]

We dualize (2.1) with nothing dropped. One identity is needed beyond [[courses/generalized-symmetries-course/conventions|conventions]] §§2–3, the summation by parts across the Hodge map: for $\omega\in C^q(\Lambda)$ and $\tilde\phi\in C^{d-q-1}(\Lambda^*)$ in $d$ dimensions,
$$
\langle\tilde\phi,\star d\omega\rangle=(-1)^{q+1}\langle\tilde d\tilde\phi,\star\omega\rangle .\tag{2.3}
$$
Since ⋆ preserves the inner product, we may move $d$ across as δ, write $\delta=(-1)^{d(q+2)+1}\star d\star$ on $C^{q+1}(\Lambda)$ (inner ⋆ from Λ to Λ*, outer from Λ* to Λ), and return with $\star\star=(-1)^{q(d-q)}$ on $C^q$:
$$
\langle\tilde\phi,\star d\omega\rangle=\langle\delta\star^{-1}\tilde\phi,\omega\rangle=(-1)^{dq+1}\langle\star\tilde d\tilde\phi,\omega\rangle=(-1)^{dq+1+q(d-q)}\langle\tilde d\tilde\phi,\star\omega\rangle ,
$$
and $dq+1+q(d-q)\equiv q+1$ mod 2 (checked on random cochains for every $q$ in $d=2,3,4$). In $d=2$, $q=1$, the multiplier term is $\langle\tilde\theta,\star dn\rangle=\langle n,v\rangle$ with $v\equiv\star^{-1}\tilde d\tilde\theta\in C^1(\Lambda)$, the difference of $\tilde\theta$ across each link.

The weight is now a product over links of $e^{-\frac\beta2(u-2\pi n)^2+inv}$ with $u=(d\theta)_\ell$, and each factor is resummed exactly. Writing $nv=\frac{v}{2\pi}[u-(u-2\pi n)]$ and expanding the $2\pi$-periodic function $\phi\mapsto\sum_nf(\phi-2\pi n)$, $f(y)=e^{-\beta y^2/2-ivy/2\pi}$, in its Fourier series, with coefficients $\hat f(m)=\int dy\,f(y)e^{-imy}=\sqrt{2\pi/\beta}\,e^{-(m+v/2\pi)^2/2\beta}$,
$$
\sum_{n\in\mathbb{Z}}e^{-\frac\beta2(u-2\pi n)^2+inv}=\frac{e^{iuv/2\pi}}{\sqrt{2\pi\beta}}\sum_{m\in\mathbb{Z}}e^{-\frac1{2\beta}\left(m+\frac v{2\pi}\right)^2+imu}
=\frac1{\sqrt{2\pi\beta}}\sum_{m\in\mathbb{Z}}\exp\Big(-\frac{\tilde\beta}2(v-2\pi m)^2+\frac{i}{2\pi}\,u\,(v-2\pi m)\Big),\tag{2.4}
$$
where the last step relabels $m\to-m$ and $\tilde\beta=1/4\pi^2\beta$; at $v=0$ this is the Villain identity of [[courses/generalized-symmetries-course/conventions|conventions]] §3. On all $N_1$ links,
$$
Z_{\rm MV}[\Lambda;\beta]=(2\pi\beta)^{-N_1/2}\int\mathcal{D}\theta\,\mathcal{D}\tilde\theta\sum_{m\in C^1(\Lambda,\mathbb{Z})}\exp\Big(-\frac{\tilde\beta}2\|v-2\pi m\|^2+\frac{i}{2\pi}\langle d\theta,v\rangle-i\langle d\theta,m\rangle\Big),\tag{2.5}
$$
with the measures of (2.1). Both remaining terms yield to (2.3) at $q=0$. The cross term is $\langle d\theta,v\rangle=\langle\star d\theta,\tilde d\tilde\theta\rangle=-\langle\star\theta,\tilde d\tilde d\tilde\theta\rangle=0$: it is the lattice $\frac{i}{2\pi}\int d\theta\wedge d\tilde\theta$, a total derivative that vanishes because the torus has no boundary (F2). For the last term we transport the integer, $\tilde n\equiv\star m\in C^1(\Lambda^*,\mathbb{Z})$; then $\|v-2\pi m\|^2=\|\tilde d\tilde\theta-2\pi\tilde n\|^2$ and $-i\langle d\theta,m\rangle=-i\langle\tilde n,\star d\theta\rangle=i\langle\star\theta,\tilde d\tilde n\rangle$. Therefore
$$
Z_{\rm MV}[\Lambda;\beta]=(2\pi\beta)^{-N_1/2}\int\mathcal{D}\theta\,\mathcal{D}\tilde\theta\sum_{\tilde n\in C^1(\Lambda^*,\mathbb{Z})}\exp\Big(-\frac{\tilde\beta}2\|\tilde d\tilde\theta-2\pi\tilde n\|^2+i\langle\theta,\star\tilde d\tilde n\rangle\Big),\tag{2.6}
$$
where ⋆ maps $C^2(\Lambda^*)$ to $C^0(\Lambda)$ with $\star\star=+1$ in this degree. This is (2.1) on Λ*, whose dual is Λ, with the roles exchanged: $\tilde\theta$ is the dynamical boson, $\tilde n$ its $\mathbb{Z}$ gauge field, θ the multiplier that makes $\tilde n$ flat. With the same measure on both sides,
$$
\boxed{\ Z_{\rm MV}[\Lambda;\beta]=(2\pi\beta)^{-N_1/2}\,Z_{\rm MV}[\Lambda^*;\tilde\beta],\qquad\tilde\beta=\frac1{4\pi^2\beta},\ }\tag{2.7}
$$
or symmetrically $(2\pi\beta)^{N_1/4}Z_{\rm MV}[\Lambda;\beta]=(2\pi\tilde\beta)^{N_1/4}Z_{\rm MV}[\Lambda^*;\tilde\beta]$. Every term is accounted for: $(2\pi\beta)^{-1/2}$ per link, the cross term that vanishes on the closed torus, the zero modes of both compact fields, and the winding sectors, which sit inside the unconstrained sums over $n$ and $\tilde n$. The map is an involution with fixed point $\beta=1/2\pi$, and Figure 1 collects the moves. GLSS derive it (App. B.1.3) "ignoring the overall factor"; the factor is local (F1), and §4.3 and Week 13 need it.

```
  Λ :  θ (sites, compact)     n (links, ℤ gauge field)     θ̃ (dual sites, multiplier)
       weight  exp( −β/2 ‖dθ − 2πn‖²  +  i⟨θ̃, ⋆dn⟩ )
          │  (2.3)  i⟨θ̃, ⋆dn⟩ = i⟨n, v⟩ ,   v = ⋆⁻¹dθ̃
          │  (2.4)  Poisson on every n_ℓ :  (2πβ)^(−1/2) per link
          │         cross term (i/2π)⟨dθ, v⟩ = 0 on the closed torus
          │         ñ = ⋆m ;  −i⟨dθ, m⟩ = i⟨θ, ⋆dñ⟩
          ▼
  Λ*:  θ̃ (dual sites, compact)  ñ (dual links, ℤ gauge field)  θ (sites, multiplier)
       weight  exp( −β̃/2 ‖dθ̃ − 2πñ‖²  +  i⟨θ, ⋆dñ⟩ ),     β̃ = 1/4π²β
```
**Figure 1. The exact self-duality (2.7): the dynamical field and the multiplier exchange roles, and the $\mathbb{Z}$ gauge field moves from the links of Λ to the links of Λ*.**

### 2.3 The sectors, checked [Computed.]

Evaluating both sides in sectors shows where each factor of $2\pi\beta$ comes from. A closed integer 1-cochain is $n=dk+w_1M^{(1)}+w_2M^{(2)}$, with $w\in\mathbb{Z}^2$ and $M^{(\mu)}$ equal to 1 on the links $\ell_\mu(x)$ with $x_\mu=0$ (Sem I Week 3 §3). The sum over $k$ unfolds θ to $\phi=\theta-2\pi k\in\mathbb{R}^{N_0}$ modulo a common $2\pi$ shift, whose constant mode gives the Jacobian $\sqrt{N_0}$ of Sem I Week 3 Move 5, the other $N_0-1$ modes being Gaussian. Since $M^{(\mu)}=h^{(\mu)}/L_\mu+d\chi^{(\mu)}$, with $h^{(\mu)}$ equal to 1 on every μ-link, $\|h^{(1)}/L_1\|^2=L_2/L_1\equiv\rho$ and $\|h^{(2)}/L_2\|^2=1/\rho$, the shift $\phi\to\phi+2\pi w\cdot\chi$ leaves a harmonic part orthogonal to $d\phi$, and
$$
Z_{\rm MV}[\Lambda;\beta]=\sqrt{N_0}\,(2\pi\beta)^{-\frac{N_0-1}2}\big({\det}'\Delta\big)^{-1/2}\,\vartheta(2\pi\beta\rho)\,\vartheta(2\pi\beta/\rho),\qquad\vartheta(t)=\sum_{w\in\mathbb{Z}}e^{-\pi tw^2},\tag{2.8}
$$
with ${\det}'\Delta$ the product of the nonzero eigenvalues of the site Laplacian. Λ* is the same torus, so the right side of (2.7) is (2.8) at $\tilde\beta$. The Jacobi identity $\vartheta(t)=t^{-1/2}\vartheta(1/t)$ and $1/2\pi\beta=2\pi\tilde\beta$ give
$$
\vartheta(2\pi\beta\rho)\,\vartheta(2\pi\beta/\rho)=(2\pi\beta)^{-1}\,\vartheta(2\pi\tilde\beta/\rho)\,\vartheta(2\pi\tilde\beta\rho):
$$
the winding of θ around the first cycle, weighted by ρ, becomes the winding of $\tilde\theta$ around the second, the 90° rotation of the Hodge map. The fluctuations give $(2\pi\beta)^{-(N_0-1)/2}=(2\pi\beta)^{-(N_0-1)}(2\pi\tilde\beta)^{-(N_0-1)/2}$, and the Jacobian and determinant are common. Thus $Z_{\rm MV}[\Lambda;\beta]=(2\pi\beta)^{-N_0}Z_{\rm MV}[\Lambda^*;\tilde\beta]$, which is (2.7): $N_0-1$ factors from the fluctuations, one from the two winding sums. The momentum sectors of θ never appear separately; they are the windings of $\tilde\theta$.

For instance, on the 2×2 torus the Laplacian has eigenvalues 0, 4, 4, 8, so ${\det}'\Delta=128$, and at $\beta=\tfrac12$
$$
Z_{\rm MV}=2\,\pi^{-3/2}\,128^{-1/2}\,\vartheta(\pi)^2=3.175338649316\times10^{-2},\qquad\vartheta(\pi)=1.000103,
$$
while at $\tilde\beta=1/2\pi^2$ the same formula gives $\pi^4$ times this, the factor $(2\pi\beta)^{N_1/2}$. A brute-force evaluation of (2.2), summing the 1333 closed $n$ with $|n_\ell|\le2$ and integrating the three relative angles by the midpoint rule, reproduces all twelve digits at $\beta=\tfrac12$ and $\beta=1$. The identity (2.7) holds to $4\times10^{-15}$ in the logarithm on the 2×2, 2×3, 3×3 and 3×5 tori for $\beta\in\{0.05,\,0.1,\,1/2\pi,\,0.4,\,1,\,2\}$.

### 2.4 Two exact $U(1)$ symmetries [Proved.]

The momentum symmetry θ → θ + α is exact here as in the plain Villain model, a $U(1)$ because its $2\pi\mathbb{Z}$ part is a redundancy; its current is $\beta(d\theta-2\pi n)$, its operator the twist of [[sem2-week-01-symmetries-are-topological-operators|Sem II Week 1]] §2.2, its charged operators $e^{iq\theta}$.

The winding symmetry is the shift $\tilde\theta\to\tilde\theta+\tilde\alpha$, a symmetry of (2.1) because $\sum_P(dn)_P=0$ on a closed lattice, each link bounding two plaquettes with opposite signs. Its charge on a closed loop $C$ of Λ is
$$
Q_w(C)=\frac1{2\pi}\sum_C(d\theta-2\pi n)=-\sum_Cn ,\tag{2.9}
$$
the Wilson loop of the $\mathbb{Z}$ gauge field (GLSS (B.19)). For $C-C'=\partial D$, $Q_w(C)-Q_w(C')=-\sum_Ddn$: in the plain Villain model the enclosed vorticity breaks the symmetry explicitly ([[courses/generalized-symmetries-course/conventions|conventions]] §6), and in (2.1) it vanishes, so $U^{\rm w}_\alpha(C)=e^{i\alpha Q_w(C)}$ depends only on the homology class of $C$ in the complement of insertions. The charged objects are the vortex operators: $e^{iq\tilde\theta(\tilde x)}$ changes the constraint on the plaquette $P$ around $\tilde x$ to $(dn)_P=-q$, a vortex of counter-clockwise winding $2\pi q$ in the sign of [[courses/generalized-symmetries-course/conventions|conventions]] §4, and for a loop $C$ encircling $\tilde x$ once counter-clockwise, (2.9) and Stokes give
$$
\big\langle U^{\rm w}_\alpha(C)\,e^{iq\tilde\theta(\tilde x)}\cdots\big\rangle=e^{iq\alpha}\,\big\langle e^{iq\tilde\theta(\tilde x)}\cdots\big\rangle .\tag{2.10}
$$
Both are 0-form symmetries with local charged operators, as the form-degree table requires in $d=2$ (winding degree $d-2=0$). In the plain Villain model a vortex is a fluctuation that the sum creates by itself; in (2.1) it exists only where an operator puts it (Figure 2). The two symmetries carry an exact mixed anomaly (F4, Problem 5⋆).

```
      +-------+-------+-------+
      |       |       |       |          +    sites: θ_x (dynamical, compact)
      |   ·   |   ·   |   ·   |          ─ │  links: n_ℓ ∈ ℤ (gauge field, dn = 0)
      |       |       |       |          ·    dual sites: θ̃ (multiplier, compact)
      +-------+=======+-------+
      |       ‖       ‖       |          ⊗    e^{iqθ̃(x̃)} :  (dn)_P = −q on the
      |   ·   ‖   ⊗   ‖   ·   |               plaquette P around x̃
      |       ‖       ‖       |          ═ ‖  C = ∂P, counter-clockwise:
      +-------+=======+-------+               Q_w(C) = −Σ_C n = −(dn)_P = q
      |       |       |       |
      |   ·   |   ·   |   ·   |          any loop homologous to C in the
      +-------+-------+-------+          punctured torus measures the same q
```
**Figure 2. The modified Villain XY model on Λ and Λ*. The vortex operator $e^{iq\tilde\theta}$ sets $dn=-q$ on the surrounding plaquette, and the winding operator (2.9) on any loop around it measures $q$.**

## 3. Compact QED without monopoles

### 3.1 The construction [Proved.]

Consider the Villain gauge theory of [[courses/generalized-symmetries-course/conventions|conventions]] §4 in $d$ dimensions, $a\in C^1(\Lambda)$ over one period and $n\in C^2(\Lambda,\mathbb{Z})$, with a compact multiplier $\tilde\phi\in C^{d-3}(\Lambda^*)$:
$$
Z_{\rm MV}[\Lambda;\beta]=\int\mathcal{D}a\,\mathcal{D}\tilde\phi\sum_{n\in C^2(\Lambda,\mathbb{Z})}\exp\Big(-\frac\beta2\|da-2\pi n\|^2+i\langle\tilde\phi,\star dn\rangle\Big),\tag{3.1}
$$
where $\mathcal{D}a=\prod_\ell da_\ell/2\pi$, $\mathcal{D}\tilde\phi$ is the same over the $(d-3)$-cells of Λ*, and $\beta=1/(e^2a_{\rm lat}^{4-d})$. Besides the redundancies of [[courses/generalized-symmetries-course/conventions|conventions]] §4, the weight is invariant under $\tilde\phi\to\tilde\phi+2\pi\tilde k$ and, for $d\ge4$, under $\tilde\phi\to\tilde\phi+\tilde d\tilde\lambda$, by (2.3) and $d^2=0$. Integrating $\tilde\phi$ imposes $dn=0$: the monopole number $m=dn$ vanishes on every cube, and (3.1) is the monopole-free theory of Sem I Week 9 §1 and Week 12 §6.3, now defined by a local weight. The multiplier is a compact scalar σ on dual sites in $d=3$ and a compact gauge field ã on dual links in $d=4$. Lifting the constraint inserts $e^{-i\langle j,\tilde\phi\rangle}$ with $j=\star dn$, which is how the monopoles of Sem I Week 8 §6 couple to σ and ã; with the sign of (3.1) the multiplier is the dual photon of [[courses/generalized-symmetries-course/conventions|conventions]] §5, and (3.6) confirms its normalization. With nothing to screen charges or condense, (3.1) is a free compact photon: on $T^d$ its partition function is a determinant times a flux-sector sum (§3.3), analytic in β, and it is in the Coulomb phase at every coupling, with a massless photon also in $d=3$, where Polyakov's mass gap needed the monopole plasma ([[week-10-polyakov-mass-gap-area-law|Sem I Week 10]]; Problem 2).

### 3.2 The exact magnetic symmetry and the 't Hooft line [Proved for the static configuration; the general linking sign Sketched.]

The magnetic symmetry shifts the multiplier by a flat cochain, $\tilde\phi\to\tilde\phi+\tilde\lambda$ with $\tilde d\tilde\lambda=0$, which leaves (3.1) invariant since $\langle\tilde\lambda,\star dn\rangle=\pm\langle\tilde d\tilde\lambda,\star n\rangle=0$ by (2.3). Its degree is $d-3$, as the form-degree table of [[courses/generalized-symmetries-course/conventions|conventions]] §6 requires ([[higher-form-symmetries]]), and its operator lives on closed 2-surfaces Σ of Λ:
$$
U^{\rm m}_\alpha(\Sigma)=\exp\Big(\frac{i\alpha}{2\pi}\sum_\Sigma F\Big)=e^{-i\alpha\sum_\Sigma n},\qquad F=da-2\pi n ,\tag{3.2}
$$
the closed form $F/2\pi$ of the table written as the Wilson surface of the $\mathbb{Z}$ gauge field, since $\sum_\Sigma da=0$. For $\Sigma-\Sigma'=\partial V$, $\sum_\Sigma n-\sum_{\Sigma'}n=\sum_Vdn=0$: the operator is exactly topological. In the plain Villain theory the same difference counts the monopole worldlines through $V$, the explicit breaking of Sem I Week 11 §5.2, and [[sem2-week-03-spontaneous-breaking-of-higher-form-symmetries|Sem II Week 3]] §5.1(c) tied exactness to $dn=0$.

The charged objects are the Wilson operators of the multiplier. In $d=4$ the 't Hooft line on a closed dual loop $\tilde C$ is $T_m(\tilde C)=\exp\big(-im\sum_{\tilde C}\tilde a\big)$, which changes the constraint to $\star dn=mJ_{\tilde C}$, a monopole worldline of charge $m$ in the sense of Sem I Week 8 §5.3 ($j=\star dn$, $j_1=-m_{234}$, [[courses/generalized-symmetries-course/conventions|conventions]] §5). For a static line running in $+\tau$ (axis 1) through the spatial cube $c$, the shuffle sign of the Hodge map gives $(dn)_c=-m$, so the flux of $F$ out of $c$ is $+2\pi m$, and (3.2) on Σ = ∂c measures $-(dn)_c=m$ (Figure 3). For Σ = ∂V with $V$ a union of spatial cubes the count adds the crossings of $\tilde C$ through $V$:
$$
\big\langle U^{\rm m}_\alpha(\Sigma)\,T_m(\tilde C)\cdots\big\rangle=e^{i\alpha m\,{\rm Link}(\Sigma,\tilde C)}\big\langle T_m(\tilde C)\cdots\big\rangle ,\tag{3.3}
$$
with Link normalized as in [[courses/generalized-symmetries-course/conventions|conventions]] §6 ($+1$ for a line in $+\tau$ and the outward sphere); for general Σ and $\tilde C$ the sign follows from the intersection pairing of Sem II Week 1 §5.1. (Checked on the $3^4$ torus with the static pair of Sem I Week 12 §6.4: $j=+1$ on the dual time link through the cube at (1,0,0), whose outward flux is $+2\pi$.) In $d=3$, $e^{iq\sigma(\tilde x)}$ sets $(dn)_c=-q$, since a 3-cell has Hodge sign $+1$ there: a monopole of flux $+2\pi q$, as in [[courses/generalized-symmetries-course/conventions|conventions]] §5.

In Sem I Week 11 §5.2 the twisted sheet at $\alpha=2\pi m$ on an open dual surface $\tilde S$ was the relabeling $n\to n+m\Xi$, and the 't Hooft loop equalled 1. In (3.1) the relabeling changes the multiplier term by $e^{-im\langle\tilde a,\star d\Xi\rangle}$ with $\star d\Xi=\pm J_{\partial\tilde S}$: the twisted sheet is $T_{\pm m}(\partial\tilde S)$, its sheet invisible, a genuine line charged under (3.2). The electric symmetry is untouched, since the twisted sheets of Sem I Week 11 §5.1 act on $a$ alone. In (3.1) both 1-form symmetries of four-dimensional Maxwell theory are exact on a finite lattice, which answers the question left open by the seminar of Sem II Week 1 §8.

```
   one time slice, axes (x¹, x², x³);  C̃ runs along +τ, out of the slice

           +-----------+
          /|          /|        T_m(C̃) = exp(−im Σ_C̃ ã)   ⇒   ⋆dn = m J_C̃
         +-----------+ |
         | |    ⊙    | |        on the spatial cube c pierced by C̃ :
         | |   C̃     | |           (dn)_c = −m ,  flux of F out of c = +2πm
         | +---------|-+
         |/          |/         Σ = ∂c :  U^m_α(Σ) = e^{−iα Σ_Σ n} = e^{iαm}
         +-----------+
```
**Figure 3. The magnetic operator (3.2) on the boundary of a spatial cube measures the charge of the 't Hooft line that pierces it; deformations of ∂c that avoid $\tilde C$ give the same phase.**

> **Physical picture.** A Monte Carlo of the modified Villain theory never produces a monopole: its moves, $n\to n+dk$ and changes of the global fluxes, keep $dn=0$. The 't Hooft loop is a ratio of partition functions with the constraint $\star dn=mJ_{\tilde C}$, with a perimeter law set by the magnetic Coulomb self-energy of the probe [free-photon evaluation, not displayed]; in the plain Villain theory the same ratio is 1, because a monopole loop cutting Σ changes $\sum_\Sigma n$ by one unit and the invariance of (3.2) is lost.

### 3.3 Exact self-duality of four-dimensional Maxwell theory [Proved; the general degree Computed on small tori.]

Section 2.2 runs unchanged in $d=4$, with plaquettes in place of links; only signs move. By (2.3) at $q=2$, $v=-\star^{-1}\tilde d\tilde a$; (2.4) applies plaquette by plaquette; the cross term $\langle da,v\rangle=-\langle\star da,\tilde d\tilde a\rangle$ vanishes by (2.3) at $q=1$. With $\tilde n=-\star m$ the Villain term becomes $\frac{\tilde\beta}2\|\tilde d\tilde a-2\pi\tilde n\|^2$, and $-i\langle da,m\rangle=i\langle\tilde n,\star da\rangle=i\langle\star a,\tilde d\tilde n\rangle=-i\langle a,\star\tilde d\tilde n\rangle$, the last step because $\star\star=-1$ between $C^1(\Lambda)$ and $C^3(\Lambda^*)$. This is (3.1) on Λ* with multiplier $a^\vee=-a$, a relabeling of an integration variable, and
$$
\boxed{\ Z_{\rm MV}[\Lambda;\beta]=(2\pi\beta)^{-N_2/2}\,Z_{\rm MV}[\Lambda^*;\tilde\beta],\qquad\tilde\beta=\frac1{4\pi^2\beta},\quad\tilde e=\frac{2\pi}e .\ }\tag{3.4}
$$
For a $p$-form gauge field in $d$ dimensions the same steps give
$$
Z_p[\Lambda;\beta]=(2\pi\beta)^{-N_{p+1}/2}\,Z_{d-p-2}[\Lambda^*;\tilde\beta],\tag{3.5}
$$
GLSS (C.8) with its prefactor, a self-duality when $p=(d-2)/2$. We checked (3.5) by evaluating both sides in sectors: to $1.4\times10^{-14}$ in the logarithm for $d=4$, $p=1$ on the $2^4$ and $2^3\times3$ tori, and for $d=3$ (Maxwell ↔ XY, both directions) on the $2^3$ and $2^2\times3$ tori, at the six couplings of §2.3. On $T^4$ the sector form is $Z_{\rm MV}={\rm covol}\,(2\pi\beta)^{-r/2}\big({\det}'\delta d\big)^{-1/2}\prod_{\mu<\nu}\vartheta(2\pi\beta g_{\mu\nu})$, with ${\det}'\delta d$ the product of the $r=N_1-N_0-3$ nonzero eigenvalues of δd on 1-cochains, whose eigenvectors are the coexact cochains, covol the covolume of the closed integer 1-cochains, and $g_{\mu\nu}=L_\rho L_\sigma/L_\mu L_\nu$ ($\rho\sigma$ the complementary pair) the squared norm of the harmonic unit flux through the $(\mu\nu)$ 2-torus. Since $g_{\mu\nu}g_{\rho\sigma}=1$, the Jacobi identity maps the flux $w_{\mu\nu}$ to the dual flux through the complementary plane; the six sums give $(2\pi\beta)^{-3}$, the fluctuations $(2\pi\beta)^{-r}$, and $r+3=N_1-N_0=N_2/2$.

The fields are related as in Sem I Week 8 §5.4. Inserting $F_P$ inserts $-\frac{i}{\beta}$ times the Hubbard–Stratonovich variable of $e^{-\beta F_P^2/2}$, since $x\,e^{-\beta x^2/2}=(2\pi\beta)^{-1/2}\int db\,(-\tfrac{i}{\beta}b)\,e^{-b^2/2\beta+ibx}$, and the sum over $n_P$ pins that variable to $\frac1{2\pi}(v-2\pi m)_P=-\frac1{2\pi}(\star^{-1}\tilde F)_P$, with $\tilde F=\tilde d\tilde a-2\pi\tilde n$. Thus, inside correlators,
$$
F\simeq\frac{i}{2\pi\beta}\star\tilde F=2\pi i\tilde\beta\,\star\tilde F ,\tag{3.6}
$$
the relation of Sem I Week 8 §5.4 with the dual integer included; in $d=2$ the same steps give $d\theta-2\pi n\simeq\frac{i}{2\pi\beta}\star(\tilde d\tilde\theta-2\pi\tilde n)$.

## 4. The exact $\mathbb{Z}_N$ background of the electric 1-form symmetry

### 4.1 The coupling [Proved.]

Let $B\in C^2(\Lambda,\mathbb{Z})$ lift a $\mathbb{Z}_N$ 2-cocycle, $dB\in N\,C^3(\Lambda,\mathbb{Z})$. In $d=4$ we couple it to (3.1) through
$$
\exp\Big(-\frac\beta2\Big\|da-2\pi n-\frac{2\pi}NB\Big\|^2+i\Big\langle\tilde a,\star\Big(dn+\frac1NdB\Big)\Big\rangle\Big),\tag{4.1}
$$
with background gauge transformations
$$
\text{(i)}\ \ B\to B+d\lambda,\quad a\to a+\frac{2\pi}N\lambda\quad(\lambda\in C^1(\Lambda,\mathbb{Z}));\qquad
\text{(ii)}\ \ B\to B+N\nu,\quad n\to n-\nu\quad(\nu\in C^2(\Lambda,\mathbb{Z})).\tag{4.2}
$$
Both leave the Villain term invariant by inspection, and both leave $dn+\frac1NdB$ invariant; the shift of $a$ preserves its measure, the integrand being $2\pi$-periodic in each $a_\ell$, and the relabeling of $n$ preserves its sum. The constraint must carry $\frac1NdB$, because under (ii) $n$ shifts by a ν that need not be closed. It now reads $d\tilde B=0$ with $\tilde B\equiv Nn+B$: the dynamical integer and the background combine into one flat $\mathbb{Z}$ field, $F_B=da-\frac{2\pi}N\tilde B$, and $Z[B]$ depends only on $[B]\in H^2(\Lambda,\mathbb{Z}_N)$. For $B=k\Xi$, with Ξ dual to a closed dual surface, (4.1) is the twisted sheet of Sem I Week 11 §5.1 at $\alpha=2\pi k/N$, the operator of $\mathbb{Z}_N\subset U(1)^{(1)}_{\rm el}$, acting on Wilson lines by $\omega^{k\,{\rm Link}}$: a background is a network of symmetry operators ([[sem2-week-04-gauging-backgrounds-and-dual-symmetry|Sem II Week 4]] §2.1). The plain Villain theory carries the same coupling without a multiplier, but without the magnetic symmetry. In (4.1) the magnetic symmetry stays exact in the field-strength form of (3.2): since $dn=-dB/N$, the operator $e^{-i\alpha\sum_\Sigma n}$ is no longer topological, and the exact operator is $e^{\frac{i\alpha}{2\pi}\sum_\Sigma F_B}=e^{-\frac{i\alpha}N\sum_\Sigma\tilde B}$, topological because $d\tilde B=0$.

### 4.2 Fractional flux sectors on $T^4$ [Computed.]

The periods of $\tilde B$ are $\tilde w_{\mu\nu}=\bar b_{\mu\nu}+Nk_{\mu\nu}$, with $\bar b_{\mu\nu}\in\{0,\dots,N-1\}$ the periods of $B$ mod $N$ and $k\in\mathbb{Z}^6$ dynamical. Writing $\tilde B=\tilde B_0+N\eta$, with $\tilde B_0$ a closed lift of $B$ (one exists, as $H^3(T^4,\mathbb{Z})$ has no torsion) and η closed, the exact part of $\tilde B_0/N$ is absorbed by a real shift of the unfolded $a$, the Gaussian factor of §3.3 does not depend on $B$, and
$$
\frac{Z[B]}{Z[0]}=\prod_{\mu<\nu}\frac{\vartheta(2\pi\beta g_{\mu\nu};\bar b_{\mu\nu}/N)}{\vartheta(2\pi\beta g_{\mu\nu};0)},\qquad\vartheta(t;s)=\sum_{k\in\mathbb{Z}}e^{-\pi t(k+s)^2}.\tag{4.3}
$$
The magnetic flux through each 2-torus becomes fractional, $k+\bar b/N$: 't Hooft's twisted boundary conditions (Sem I Week 14), exact on the lattice and in a theory with an exact magnetic symmetry.

### 4.3 Gauging: $\beta\to\beta/N^2$ [Computed.]

Gauging $\mathbb{Z}_N^{(1)}$ with the normalization of Sem II Week 4 (2.4)–(2.5), $|H^0|/|H^1|=N^{-3}$ on $T^4$, sums (4.3) over the $N^6$ classes. The sum over $\bar b$ and $k$ is a sum over all $\tilde w\in\mathbb{Z}^6$ with weights $e^{-2\pi^2\beta g\tilde w^2/N^2}$, the flux sum at $\beta/N^2$, while $(2\pi\beta)^{-r/2}=N^{-r}(2\pi\beta/N^2)^{-r/2}$. Therefore
$$
\frac{|H^0|}{|H^1|}\sum_{[B]\in H^2(T^4,\mathbb{Z}_N)}Z_{\rm MV}[B;\beta]=N^{-3-r}\,Z_{\rm MV}[\beta/N^2]=N^{N_0-N_1}\,Z_{\rm MV}[\beta/N^2],\tag{4.4}
$$
checked to $10^{-12}$ on the $2^3\times3$ torus for $N=2,3$: gauging maps the coupling $e$ to $Ne$, with $a'=Na$ the gauge-invariant field, up to the local factor $N^{N_0-N_1}$. Combined with (3.4), gauging followed by duality maps β to $N^2/4\pi^2\beta$, with fixed point $\beta=N/2\pi$, that is $e^2=2\pi/N$. Section 12 states what Week 13 does with this fixed point.

## 5. The lattice θ-term, sealed

### 5.1 Periodicity without monopoles [Proved.]

Sem I Week 12 §6.2 wrote $Q_{\rm lat}=\frac1{8\pi^2}\sum F\cup F=\frac12\sum n\cup n-\frac1{4\pi}\sum(a\cup dn-dn\cup a)$ for every real $a$ and integer $n$ on $T^4$, §6.3 proved $Q_{\rm lat}={\rm Pf}(w)\equiv w_{12}w_{34}-w_{13}w_{24}+w_{14}w_{23}\in\mathbb{Z}$ when $dn=0$, with $w_{\mu\nu}$ the periods of $n$, and §6.4 found the crack: in the plain Villain theory monopoles make $Q_{\rm lat}$ non-integer and θ, θ + 2π define different lattice theories, a conclusion recorded there as [Heuristic.] and in [[courses/generalized-symmetries-course/conventions|conventions]] §10. In the modified Villain theory with θ,
$$
Z_{\rm MV}(\theta)=\int\mathcal{D}a\,\mathcal{D}\tilde a\sum_{n\in C^2(\Lambda,\mathbb{Z})}\exp\Big(-\frac\beta2\|F\|^2+i\langle\tilde a,\star dn\rangle+i\theta\,Q_{\rm lat}\Big),
$$
the integral over ã at fixed $(a,n)$ is $\delta_{dn,0}$, whatever multiplies it, so on every contributing configuration $Q_{\rm lat}={\rm Pf}(w)$, independent of $a$. With the sector form of §3.3,
$$
Z_{\rm MV}(\theta)={\rm covol}\,(2\pi\beta)^{-r/2}\big({\det}'\delta d\big)^{-1/2}\sum_{w\in\mathbb{Z}^6}\exp\Big(-2\pi^2\beta\sum_{\mu<\nu}g_{\mu\nu}w_{\mu\nu}^2+i\theta\,{\rm Pf}(w)\Big),\tag{5.1}
$$
and $Z_{\rm MV}(\theta+2\pi)=Z_{\rm MV}(\theta)$ term by term, at every β and on every torus. This seals the gap of Sem I Week 12 §6: the constraint that Week 12 had to assume is now part of the definition of the theory, imposed by an integral, and the lattice θ-term of [[courses/generalized-symmetries-course/conventions|conventions]] §10 is exactly $2\pi$-periodic. Flipping the three fluxes $w_{1\nu}$ (time reversal) reverses Pf(w), so (5.1) is even in θ, and at θ = π its weights $(-1)^{{\rm Pf}(w)}$ are real. (Checked: on the $2^2\times3^2$ torus, $Q_{\rm lat}$ from the cup product with random real $a$ and closed $n=w\cdot M+dk$ equals Pf(w) to twelve digits, for instance 8.000000000000 for $w=(3,1,1,3,1,2)$ in the order (12, 13, 14, 23, 24, 34).)

### 5.2 With the background: the Pontryagin square [Computed.]

With the background, $F_B=da-\frac{2\pi}N\tilde B$ and $d\tilde B=0$, so Sem I Week 12 §§6.2–6.3 with $n\to\tilde B/N$ give
$$
Q_{\rm lat}[F_B]=\frac1{2N^2}\sum\tilde B\cup\tilde B=\frac{{\rm Pf}(\tilde w)}{N^2},\qquad{\rm Pf}(\bar b+Nk)={\rm Pf}(\bar b)+N\,{\rm bil}(\bar b,k)+N^2\,{\rm Pf}(k),\tag{5.2}
$$
with ${\rm bil}(x,y)=x_{12}y_{34}+x_{34}y_{12}-x_{13}y_{24}-x_{24}y_{13}+x_{14}y_{23}+x_{23}y_{14}$. (Checked with random backgrounds and random real $a$: $Q_{\rm lat}=-0.500000000000$ for $N=2$ and $-0.666666666667$ for $N=3$, equal to ${\rm Pf}(\tilde w)/N^2$.) The shift θ → θ + 2π multiplies each term of (5.1) with background by $e^{2\pi i{\rm Pf}(\bar b)/N^2}\,\omega^{{\rm bil}(\bar b,k)}$, which depends on the dynamical fluxes: with a background on, θ → θ + 2π is not a symmetry of $Z[B]$. Up to a c-number, the second factor is a product of these exact magnetic operators on the 2-tori, at angles $\pm2\pi\bar b_{\mu\nu}/N$ fixed by the intersection form, so the shift turns the electric background into a magnetic one as well, the background form of the Witten effect $(0,1)\to(1,1)$ of Sem I Week 12 §5 [Heuristic as a continuum reading]. The shift θ → θ + 2πN instead multiplies every term by one phase,
$$
Z_{\rm MV}(\theta+2\pi N;B)=\exp\Big(\frac{2\pi i}N\,\frac{\int\mathcal{P}(B)}2\Big)\,Z_{\rm MV}(\theta;B),\tag{5.3}
$$
since for the closed lift the $\cup_1$ term of the Pontryagin square of [[courses/generalized-symmetries-course/conventions|conventions]] §8 vanishes, $\int\mathcal{P}(\tilde B)=2\,{\rm Pf}(\tilde w)$, and ${\rm Pf}(\tilde w)\equiv{\rm Pf}(\bar b)$ mod $N$. (Checked: for $N=2$, $\bar b_{12}=\bar b_{34}=1$, $Z(\theta+4\pi)/Z(\theta)=-1$ while $Z(\theta+2\pi)/Z(\theta)=-0.1003$ at θ = 0.4 for β = 0.3 and 0.7 (the ratio depends on θ); for $N=3$ the ratio is $e^{2\pi i{\rm Pf}(\bar b)/3}$ to ten digits.) This is the structure of [[sem2-week-06-mixed-anomalies-yang-mills-at-theta-pi|Sem II Week 6]] §4.1: a c-number phase built from the lattice Pontryagin square, shifting the counterterm label $p$ of [[courses/generalized-symmetries-course/conventions|conventions]] §10 by one unit. In $SU(N)$ the shift by 2π produced it, with label shift $N-1$; here the exact magnetic symmetry absorbs the fractional part, and the c-number appears at 2πN. Week 6 needed exactly such a regularization, in which the θ-shift and the background are both exact and the phase is a theorem of the finite lattice.

## 6. JKKN and BMK as exact statements

### 6.1 José–Kadanoff–Kirkpatrick–Nelson [Proved.]

JKKN split the Villain XY model into free spin waves and a neutral vortex Coulomb gas (Sem I Week 3 §§4–5). Inserting $1=\sum_v\delta_{\star dn,v}$ into the plain Villain sum and writing each delta as an integral over $\tilde\theta$ turns the split into one identity,
$$
Z_{\rm V}(\beta)=\sum_{v\in C^0(\Lambda^*,\mathbb{Z})}Z_{\rm MV}[\Lambda;\beta]\,\big\langle e^{-i\langle v,\tilde\theta\rangle}\big\rangle_\beta
=(2\pi\beta)^{-N_1/2}\sum_{v\in C^0(\Lambda^*,\mathbb{Z})}Z_{\rm MV}[\Lambda^*;\tilde\beta]\,\big\langle e^{-i\langle v,\tilde\theta\rangle}\big\rangle_{\tilde\beta},\tag{6.1}
$$
the second form by (2.7), whose Poisson step does not touch $\tilde\theta$. The Villain model at β is the exactly self-dual MV boson at $\tilde\beta$ with its vortex operators summed with unit weight, equivalently (2.1) with $\tilde\theta$ frozen at 0, the λ → ∞ end of GLSS's family (B.8), whose λ = 0 end is the MV model (Problem 6⋆).

The Coulomb gas is the Gaussian value of the vertex correlator. In the zero-winding sector of the dual boson, with propagator $G/\tilde\beta$, the zero mode of $\tilde\theta$ enforces $\sum v=0$ and the Gaussian gives $e^{-\frac1{2\tilde\beta}\langle v,G'v\rangle}=e^{-2\pi^2\beta\langle v,G'v\rangle}$, the exact lattice Coulomb gas of Sem I Week 3 §4, with $E_{\rm core}=2\pi^2\beta\kappa$ after Move 7. The windings of $\tilde\theta$ dress it with phases $e^{-2\pi i\langle v,\tilde w\cdot\tilde\chi\rangle}$ that couple the vortex dipole moment to the windings, the torus terms that JKKN's infinite plane does not see and Week 3 (F3) set aside. The exact content of JKKN is thus that vortices are the vertex operators of an exactly self-dual compact boson; the one approximation in the chain is the dilute-gas truncation of the sine-Gordon step (Sem I Week 3 §6).

### 6.2 Banks–Myerson–Kogut [Proved.]

BMK split four-dimensional Villain $U(1)$ into free photons and a gas of closed monopole loops, and derived its dual, a Villain theory on Λ* coupled to the monopole currents (Sem I Week 8 §§5–6). The same insertion with $j=\star dn\in C^1(\Lambda^*,\mathbb{Z})$, and (3.4), give
$$
Z_{\rm V}(\beta)=\sum_{j\in C^1(\Lambda^*,\mathbb{Z})}Z_{\rm MV}[\Lambda;\beta]\,\big\langle e^{-i\langle j,\tilde a\rangle}\big\rangle_\beta=(2\pi\beta)^{-N_2/2}\sum_{j\in C^1(\Lambda^*,\mathbb{Z})}Z_{\rm MV}[\Lambda^*;\tilde\beta]\,\big\langle e^{-i\langle j,\tilde a\rangle}\big\rangle_{\tilde\beta},\tag{6.2}
$$
whose last sum, with $a^\vee$ integrated, is the boxed identity of Sem I Week 8 §6 term by term. The exact symmetries supply its selection rules: invariance under $\tilde a\to\tilde a+\tilde d\tilde\lambda$ kills every $j$ with $\tilde\delta j\ne0$, and the magnetic shift of ã by a flat cochain kills every $j$ with net winding, the conditions $P_Wj=0$ that Week 8 §5.2 derived from the volume of gauge orbits.

In (6.2) the monopoles are dynamical charges of the dual photon, and the plain theory is not self-dual because only one side carries matter (Sem I Week 8 §6), while its $j=0$ term, the MV theory, is. The loop gas of Sem I Week 8 §5.5 is the Gaussian value of $\langle e^{-i\langle j,\tilde a\rangle}\rangle_{\tilde\beta}$ in the zero-flux sector, $e^{-2\pi^2\beta\sum_\mu\langle j_\mu,G'j_\mu\rangle}$, and the confinement transition of Sem I Week 11 belongs to the sum over $j$.

## 7. Seminar: Gorantla–Lam–Seiberg–Shao, presented by the instructor

**Format.** The first seminar of Block 4, presented by the instructor as the model in the format of syllabus §7. Students read the assigned parts and bring Problem 1.

**Parts.** GLSS, arXiv:2103.01257: §1.2; App. B.1.1–B.1.3 (the XY model, its symmetries, its T-duality) and B.1.5 (the Kosterlitz–Thouless transition); App. C.1–C.1.2 ($p$-form gauge theory, duality, symmetries). The fracton sections are optional on a first reading.

**The technical claim.** Promoting the Villain integer to a flat $\mathbb{Z}$ gauge field gives lattice models that share the symmetries, anomalies and dualities of their continuum limits exactly: XY self-duality under β ↔ 1/4π²β, $p$-form ↔ $(d-p-2)$-form duality, exact electric and magnetic symmetries with their mixed anomaly; the same formulation defines the exotic theories of the main text.

**What it needs from Semester I.** The Villain form and Poisson resummation (Sem I Week 3, [[courses/generalized-symmetries-course/conventions|conventions]] §3), the dual variables of Week 8, the twisted sheets of Week 11 §5.1, and the symmetry operators of Sem II Week 1.

**The step at the board.** The T-duality (B.20) → (B.24) with the overall factor restored: in twenty minutes, (2.3)–(2.7) and Figure 1; in ten, the 2×2 count of §2.3 with its factor $\pi^4$.

**For the discussion.** GLSS's sign translates as $\tilde\phi_{\rm GLSS}=-\tilde\theta$. Why is the Lagrangian of (B.6) not invariant under the winding shift although the action is, and how do (B.21)–(B.23) make this an anomaly (F4, Problem 5⋆)? What does B.1.5 say the BKT transition becomes in the family (B.8) (Problem 6⋆)?

**The open question it leaves for this course.** The main text applies the formulation to the XY-plaquette model, tensor gauge theories and the X-cube model; which of their exact lattice symmetries can be gauged on a submanifold, as Week 14 gauges ordinary ones, is the fracton item of the Block 5 open-problems session.

**On the course map.** The exact versions of the Semester I dualities (§6), and the lattice home of the symmetries and anomalies of Blocks 1–2.

## 8. Subtleties and fine print

**F1. The prefactor is local.** $(2\pi\beta)^{-N_1/2}$, $(2\pi\beta)^{-N_2/2}$ and $N^{N_0-N_1}$ in (2.7), (3.4) and (4.4) are products of one factor per cell, local counterterms. They cancel in normalized correlators, which is why GLSS can drop them, but they enter free energies, gauging normalizations, and the normalization of the composite of §4.3.

**F2. Boundaries.** The cross term of (2.5) and the summation by parts behind (2.6) are total differences. On a lattice with boundary they leave terms that couple θ and $\tilde\theta$ there, and the duality maps boundary conditions into one another; we have not derived that map, and (2.7) holds as written only on closed lattices.

**F3. The multiplier is compact.** Over $\mathbb{R}$, $\int d\tilde\theta\,e^{i\tilde\theta k}=2\pi\delta(k)$ is infinite at $k=0$ ([[courses/generalized-symmetries-course/conventions|conventions]] §3). The redundancy $\tilde\theta\to\tilde\theta+2\pi\tilde k$ makes the constraint a Kronecker delta with unit weight and lets $\tilde\theta$ be the dual compact boson; GLSS's real $\tilde\phi$ with this $\mathbb{Z}$ gauge symmetry is the same thing.

**F4. Weight, Lagrangian and the mixed anomaly.** The weight of (2.1) is invariant under the winding shift only after the sum over plaquettes; rewritten by (2.3) as $\langle\tilde d\tilde\theta,\star n\rangle$, the density is invariant but no longer invariant under $n\to n+dk$. With both symmetries coupled to backgrounds the obstruction survives every local counterterm: the momentum–winding anomaly (GLSS B.1.2, Problem 5⋆). Its four-dimensional electric–magnetic analogue is Sem II Week 1 Problem 7⋆⋆.

**F5. Periodicity and the Witten effect.** With a 't Hooft line inserted, $dn\ne0$ along $\tilde C$, the linear term of Sem I Week 12 §6.2 survives there, and the θ-term attaches to the line the holonomy factor of Week 12 §6.4. The theory is periodic while its line operators are relabeled, as in Sem I Week 12 §5 (Problem 9⋆⋆).

**F6. Tori and spin.** The integrality of Pf(w) uses the even intersection form of $T^4$ (Sem I Week 12 §6.3). On a four-manifold with odd intersection form $Q\in\frac12\mathbb{Z}$ ([[courses/generalized-symmetries-course/conventions|conventions]] §10) and the period would be 4π; every lattice of this course is a torus.

## 9. Common misconceptions

**"The modified Villain model is the XY model with very heavy vortices."** It is tempting because GLSS reach (2.2) from a core energy κ → ∞. At finite κ the vortices are dynamical and there is a BKT transition; at κ = ∞, which is (2.1), there are no vortex fluctuations, and the model is Gaussian and critical at every β.

**"Without monopoles, the 't Hooft loop is still trivial."** It is tempting because Sem I Week 11 §5.2 proved $\tilde W_m=1$ by relabeling the Villain integers. In (3.1) the relabeling changes the multiplier term, and the 't Hooft line is the Wilson line of the multiplier, a genuine operator with a perimeter law and charge $m$ under (3.2).

**"θ is $2\pi$-periodic, so it is unobservable."** It is tempting because $Z_{\rm MV}(\theta+2\pi)=Z_{\rm MV}(\theta)$. The θ-dependence of (5.1) at fixed θ is physical (Problem 3), the shift relabels line operators (F5), and with a $\mathbb{Z}_N$ background the shift by 2π is not a symmetry at all (§5.2).

## 10. Historical note

Villain (1975) introduced the periodic Gaussian for the planar magnet. José, Kadanoff, Kirkpatrick and Nelson (1977) used it to split the XY model exactly into spin waves and a vortex Coulomb gas and to obtain its discrete-Gaussian dual; Banks, Myerson and Kogut (1977) did the same for four-dimensional $U(1)$ with monopole loops. In both papers the defects are the variables of interest. Sulejmanpasic and Gattringer (2019), working on lattice θ-terms and magnetic matter, added the multiplier that forbids monopoles, and with it a θ-term with integer topological charge. Gorantla, Lam, Seiberg and Shao (2021) read the Villain integer as a $\mathbb{Z}$ gauge field, named the construction, stressed that its dualities and symmetries hold exactly on the finite lattice, and used it to define fracton models on the lattice. The prefactors and torus sectors of §§2.3, 3.3 and 4.3 are the course's own.

## 11. What to take away

1. **Technical:** a compact dual-lattice multiplier makes the Villain integer a flat $\mathbb{Z}$ gauge field, (2.1)–(2.2), (3.1). **Physical:** vortices and monopoles are removed configuration by configuration, by a constraint.
2. **Technical:** $Z_{\rm MV}[\Lambda;\beta]=(2\pi\beta)^{-N_1/2}Z_{\rm MV}[\Lambda^*;1/4\pi^2\beta]$, (2.7), and (3.5) in general. **Physical:** field and multiplier exchange roles, and so do the sectors of the two sides.
3. **Technical:** the winding and magnetic symmetries are Wilson loops and surfaces of the flat $\mathbb{Z}$ field, (2.9), (3.2), acting on $e^{iq\tilde\theta}$ and $T_m(\tilde C)$. **Physical:** both 1-form symmetries of four-dimensional Maxwell theory are exact on a finite lattice.
4. **Technical:** a $\mathbb{Z}_N$ background enters the constraint as $d(Nn+B)=0$, (4.1), gives fractional fluxes (4.3), and gauging maps β to β/N², (4.4). **Physical:** backgrounds, gaugings and dualities are exact lattice operations, with local prefactors (F1).
5. **Technical:** without monopoles $Q_{\rm lat}={\rm Pf}(w)\in\mathbb{Z}$ on every contributing configuration, (5.1); with a background, θ → θ + 2πN gives the Pontryagin-square phase (5.3). **Physical:** the gap of Sem I Week 12 §6 is sealed, and the structure of Sem II Week 6 becomes a lattice theorem.

## 12. Looking ahead

Week 13 turns dualities into operators. The Kramers–Wannier duality of Sem I Week 4 is implemented by a topological line that is not invertible, $D\times\bar D=1+\eta$, built by gauging on half of spacetime. One dimension up the same logic uses this week's two exact operations: at $\beta=N/2\pi$ the self-duality (3.4) composed with the gauging (4.4) maps MV Maxwell theory to itself, and the interface performing the composite on half of spacetime is the non-invertible duality defect of Choi–Córdova–Hsin–Lam–Shao and Kaidi–Ohmori–Zheng. Week 14 then gauges on a closed hypersurface of four-dimensional $\mathbb{Z}_N$ gauge theory, the wall of the group's manuscript, and gives the lines on it a finite cost.

## 13. Problem set

Problems 1–4 are the classroom core; 5⋆–7⋆ consolidate the self-study sections; 8⋆⋆–9⋆⋆ are research extensions.

### Core problems

**1. Vortex operators and the self-dual point** (extends §§2.2, 2.4). On the infinite lattice, or on the torus in the zero-winding sectors, consider $\langle e^{iq\tilde\theta(\tilde x)}e^{-iq\tilde\theta(\tilde y)}\rangle$ in the MV XY model. (a) Compute it on the direct side, integrating out $\tilde\theta$ and using the Coulomb energy of Sem I Week 3 §4. (b) Compute it on the dual side as a vertex correlator of the Gaussian boson at $\tilde\beta$, and compare. (c) With $a(r)=\frac1{2\pi}\ln r+\kappa$ ([[courses/generalized-symmetries-course/conventions|conventions]] §2), read off the scaling dimension of $e^{iq\tilde\theta}$, compare with that of $e^{iq\theta}$, and find the coupling at which dimensions and amplitudes coincide.

**2. Monopole operators in monopole-free QED₃** (extends §§3.1–3.3). In $d=3$ the multiplier of (3.1) is σ on the dual sites. (a) Show that σ → σ + α is an exact 0-form symmetry and write its operator. (b) Compute $\langle e^{i\sigma(\tilde x)}e^{-i\sigma(\tilde y)}\rangle$ on the infinite lattice twice: as the Gaussian action of a fixed monopole–antimonopole pair (Sem I Week 8 §4.4), and through (3.5), where the dual is the three-dimensional MV XY model at $\tilde\beta$. (c) Find the large-separation limit in terms of $G_3(0)$, decide whether the magnetic symmetry is spontaneously broken, and contrast the approach to the limit with the monopole plasma of Sem I Weeks 9–10.

**3. θ-dependence from flux sectors** (extends §5.1). On the symmetric $L^4$ torus, $g_{\mu\nu}=1$. (a) Show that $Z_{\rm MV}(\theta)/Z_{\rm MV}(0)$ depends on β and θ only. (b) Count the flux sectors with $\sum w^2=1$ and $2$ and their values of Pf(w). (c) Derive the leading large-β form of $F(\theta)-F(0)$, $F=-\ln Z$, and evaluate it at θ = π, β = ½.

**4. A $\mathbb{Z}_2$ twist** (extends §§4.1–4.2). Take $N=2$, the symmetric $L^4$ torus, and $\bar b_{12}=1$, the other periods zero. (a) Reduce (4.3) to a ratio of one-dimensional theta functions. (b) Poisson-resum both and show that the ratio is $\sum_m(-1)^me^{-m^2/2\beta}\big/\sum_me^{-m^2/2\beta}$; interpret $(-1)^m$ as a symmetry operator and say through which plane it measures flux. (c) Evaluate the ratio at β = ½ and β = 1 and compare with its large-β form.

### Starred problems

**5⋆. The momentum–winding anomaly** (extends §2.4 and F4). Couple (2.1) to backgrounds $(A,N)$ for momentum and $(\tilde A,\tilde N)$ for winding, translating GLSS (B.21) to the sign of (2.1), compute the variation of the weight under (B.22), and show that the counterterm $\frac{i}{2\pi}\langle\tilde A,\star A\rangle$ moves the anomaly between the two symmetries without removing it. *Hint:* GLSS (B.21)–(B.23) with $\tilde\phi_{\rm GLSS}=-\tilde\theta$; the continuum limit of the variation is $\frac{i}{2\pi}\int\tilde\alpha\,dA$ up to sign.

**6⋆. From MV to Villain** (extends §6.1). Multiply the weight of (2.1) by $e^{\lambda\sum_{\tilde x}\cos\tilde\theta_{\tilde x}}$, λ ≥ 0. Integrate out $\tilde\theta$ and show that each plaquette receives the weight $I_{|v_P|}(\lambda)$, $v=dn$; that λ = 0 gives (2.2); that $Z[\lambda]/I_0(\lambda)^{N_2}\to Z_{\rm V}$ as λ → ∞; and find the vortex fugacity at small λ. *Hint:* $e^{\lambda\cos x}=\sum_kI_k(\lambda)e^{ikx}$; compare GLSS (B.8)–(B.13).

**7⋆. The three-dimensional duality with its prefactor** (extends §3.3). Derive $Z^{\rm QED_3}_{\rm MV}[\Lambda;\beta]=(2\pi\beta)^{-N_2/2}Z^{\rm XY}_{\rm MV}[\Lambda^*;\tilde\beta]$ by running §2.2 with $q=2$ in $d=3$, identify the dual multiplier, and check the sign of $F\simeq\frac{i}{2\pi\beta}\star(\tilde d\sigma-2\pi\tilde n)$ against [[courses/generalized-symmetries-course/conventions|conventions]] §5. *Hint:* (2.3) at $q=2$ has sign $-1$, and $\star\star=+1$ between $C^0(\Lambda)$ and $C^3(\Lambda^*)$.

### ⋆⋆ problems

**8⋆⋆. The duality defect of lattice Maxwell theory.** *Known:* the exact maps (3.4) and (4.4), whose composite fixes β = N/2π (§4.3), and the continuum defect cited in §12 (arXiv:2111.01139, arXiv:2111.01141). *Explored:* the lattice interface that gauges $\mathbb{Z}_N^{(1)}$ on half of $T^4$ with the background of §4.1 and dualizes it with §3.3, at β = N/2π. *Sources:* the two papers' introductions, this note, Week 13. *Completion:* an explicit lattice operator on a 3-torus slice of the transfer matrix, with its fusion with its conjugate computed, local factors (F1) included.

**9⋆⋆. The lattice Witten effect for 't Hooft lines.** *Known:* Sem I Week 12 §6.4 computed the θ-term of a static monopole pair in the plain Villain theory; Sulejmanpasic and Gattringer demonstrate the Witten effect for magnetic matter; Sem I Week 12 Problem 8⋆⋆ posed the question before this week's tools. *Explored:* with $T(\tilde C)$ inserted in (3.1), the dependence of $e^{i\theta Q_{\rm lat}}$ on $a$ along the line and on $n$ through $\frac12\sum n\cup n$, and whether θ → θ + 2π maps $T(\tilde C)$ to a dyonic line exactly. *Sources:* Sem I Week 12 §6, Sulejmanpasic–Gattringer, §§3 and 5 of this note. *Completion:* an exact identity on $T^4$ relating $\langle T(\tilde C)\rangle_{\theta+2\pi}$ to $\langle T(\tilde C)W(C')\rangle_\theta$ for a specified push-off $C'$, verified numerically for one static pair.

## Self-study answer checkpoints

**Problem 1.** *Decisive step:* the insertion fixes $v=-q\delta_{\tilde x}+q\delta_{\tilde y}$, and the Gaussian over θ gives $e^{-2\pi^2\beta\langle v,G'v\rangle}$ with $\langle v,G'v\rangle=2q^2[G(0)-G(\tilde x-\tilde y)]$. *Result:* both sides give $e^{-4\pi^2\beta q^2a(r)}=e^{-4\pi^2\beta q^2\kappa}r^{-2\pi\beta q^2}$, so $\Delta[e^{iq\tilde\theta}]=\pi\beta q^2$, against $\Delta[e^{iq\theta}]=q^2/4\pi\beta$ with amplitude $e^{-q^2\kappa/\beta}$; both coincide at the self-dual point β = 1/2π, where the dimensions are $q^2/2$. *Common failure:* keeping only the cross term of $\langle v,G'v\rangle$ ($2\pi^2\beta$ in place of $4\pi^2\beta$), or using $1/\beta$ in place of $1/\tilde\beta$ in the dual propagator.

**Problem 2.** *Decisive step:* the insertion sets $(dn)_c=-1$ and $+1$ on two cubes, whose Coulomb energy is $2\pi^2\beta\langle v,G'v\rangle$, while on the dual side the propagator of σ is $G_3/\tilde\beta=4\pi^2\beta\,G_3$. *Result:* $e^{-4\pi^2\beta[G_3(0)-G_3(r)]}\to e^{-4\pi^2\beta G_3(0)}=e^{-2S_{\rm mono}}=e^{-9.98\beta}\ne0$, with $S_{\rm mono}=2\pi^2\beta G_3(0)=4.99\beta$ ([[courses/generalized-symmetries-course/conventions|conventions]] §5): long-range order of a charged operator of an exact symmetry, so the magnetic $U(1)^{(0)}$ is spontaneously broken, approached as the power law $4\pi^2\beta G_3(r)\simeq\pi\beta/r$ of a massless Goldstone boson (Sem II Week 3). In the plasma of Weeks 9–10 the symmetry is broken explicitly, $e^{i\sigma}$ also has an expectation value, and the approach is exponential, with the photon gapped. The operator of (a) is $e^{-i\alpha\sum_\Sigma n}$ on a closed surface Σ of Λ. *Common failure:* calling the symmetry 1-form because the theory is a gauge theory; its degree is $d-3=0$ and its charged objects are local.

**Problem 3.** *Decisive step:* the Gaussian factor of (5.1) is θ-independent and $g_{\mu\nu}=1$, so the ratio is $\sum_we^{-2\pi^2\beta|w|^2+i\theta{\rm Pf}(w)}/\sum_we^{-2\pi^2\beta|w|^2}$. *Result:* 12 sectors with $|w|^2=1$, all with Pf = 0; 60 with $|w|^2=2$, of which the 12 on complementary planes have Pf = ±1 (six each) and 48 have Pf = 0; so $F(\theta)-F(0)=12(1-\cos\theta)e^{-4\pi^2\beta}[1+O(e^{-2\pi^2\beta})]$, giving $24e^{-2\pi^2}=6.4207\times10^{-8}$ at θ = π, β = ½, against the exact sector sum $6.4194\times10^{-8}$. *Common failure:* assigning Pf ≠ 0 to two fluxes in planes that share a direction.

**Problem 4.** *Decisive step:* the five planes with $\bar b=0$ cancel, leaving $\vartheta(2\pi\beta;\tfrac12)/\vartheta(2\pi\beta;0)$, and the Jacobi identity turns the shift by ½ into the phase $e^{i\pi m}$. *Result:* the ratio is $\sum_m(-1)^me^{-m^2/2\beta}/\sum_me^{-m^2/2\beta}$, the $\mathbb{Z}_2$ electric operator acting on the dual flux $m$ through the complementary (34) plane, Poincaré dual to $\bar b_{12}$; numerically 0.169592 at β = ½ and 0.0143838 at β = 1, against the large-β form $2e^{-\pi^2\beta/2}=0.169610$ and $0.0143838$. *Common failure:* keeping $g\ne1$, or shifting the flux by $\bar b$ in place of $\bar b/N$.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester II Block 4. Written to the note-quality-template standard on 2026-10-02. Last revised 2026-10-03.*
