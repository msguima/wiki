---
title: "Week 10 — Compact QED₃ II: the Mass Gap and the Area Law"
type: lecture-notes
course: syllabus
semester: 1
week: 10
block: C
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Week 8 (the exact three-dimensional duality and the monopole Coulomb gas); Week 9 (the monopole plasma and the dual-photon sine-Gordon theory); solitons; Gaussian screening
modified: 2026-09-29
---

# Week 10 — Compact QED₃ II: the Mass Gap and the Area Law

> *This is the calculation the semester has been building toward. [[week-03-villain-form-xy-duality|Week 3]] and [[week-08-dual-variables-abelian-gauge|Week 8]] rewrote compact abelian theories exactly in dual variables, and [[week-09-compact-qed3-monopole-plasma|Week 9]] organized the three-dimensional monopoles into a dilute plasma with a sine-Gordon description. This week we compute what the plasma does. It gives the photon a mass, and it turns a Wilson loop into a vortex line of the dual photon whose unwinding costs an area, so that static charges are confined with a tension exponentially small in the inverse coupling. Each step is either exact or, at weak coupling, controlled by one small parameter, $\zeta/e^6$, and every constant is on the page. [[week-11-monopole-condensation-4d|Week 11]] asks the same questions in four dimensions, where the monopoles are loops and the answer depends on the coupling.*

### How to use this chapter

- **In class:** in the first lecture, the starting point (§2) and the photon mass from both faces (§§3.1–3.2), ending with the identity between the sine-Gordon saddle and the Poisson–Boltzmann equation of the plasma (§3.3); then the Wilson loop carried through the moves of Week 8 to the boxed dual form and the vortex line (§§4.1–4.3). In the second lecture, the monopole phase and the solid angle (§4.4), the loop in the plasma (§4.5), the unwinding, the kink, the Bogomolny bound and the tension (§§5.1–5.3), the area law (§5.4) and the charge-$q$ result (§6.1), closing with Figure 3. The core Problems 1–3 extend §4.4, §§5.3 and 6.1, and F3.
- **For self-study:** the lattice demonstration of §5.5, surface independence and the symmetry reading (§§6.2–6.3), the validity chain (§7), the fine print F1–F7 and the historical note. The one calculation to do alone is §5.5: relax the literal jump on a chain and on a wrapped strip, recover $\sigma_{\rm str}=16Km_\gamma$ to the quoted lattice accuracy, and extract the logarithm of the perimeter term.
- **Instructor checkpoint:** two errors recur at the board. The Wilson loop is a vortex line of σ (§4.3). A literal $2\pi$ jump of σ across a spanning surface, which is often imposed and then minimized, is invisible to $\cos\sigma$ and is a relabelling of the integer heights; the tension is the cost of the smooth unwinding (§5.1). And the monopole Coulomb coefficient is $(4\pi^2/e^2)\sum_{i<j}$; with half of it the Debye mass comes out as $4\pi^2\zeta/e^2$ and the deconfinement temperature doubles to $4e^2/\pi$ (§3.2, F4).

## 0. Reading

**Primary:** Polyakov, *Phys. Lett. B* 59 (1975) 82, all three pages: compact QED on a three-dimensional lattice, its monopoles, their gas treated as a plasma by Debye's method at small coupling, the photon mass and the area law for planar contours, and, in four dimensions, closed monopole rings with a perimeter law at small coupling. Polyakov, *Nucl. Phys. B* 120 (1977) 429, the sections on 2+1 dimensions, for the full account, and *Gauge Fields and Strings* (1987), ch. 4. This note rebuilds the calculation in the Villain variables of [[week-08-dual-variables-abelian-gauge|Week 8]] rather than in Polyakov's.

**Secondary:**
- Kogut, *Rev. Mod. Phys.* 51 (1979) 659, §VI.
- Göpfert & Mack, *Commun. Math. Phys.* 82 (1982) 545, §1 (pp. 545–550): Theorem 1 and Corollary 2 state what is rigorously known, and eqs. (1.3) and (1.8) fix the notation that F7 translates.

**Optional research reading:** Wilson, *Phys. Rev. D* 10 (1974) 2445, and Osterwalder & Seiler, *Ann. Phys.* 110 (1978) 440, for the strong-coupling area law; Svetitsky & Yaffe, *Nucl. Phys. B* 210 (1982) 423, for the universality argument behind F4.

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]]. Normalizations: [[courses/generalized-symmetries-course/conventions|conventions]] §§3–6. We write $K\equiv e^2/8\pi^2$ for the dual-photon stiffness of [[courses/generalized-symmetries-course/conventions|conventions]] §5; the letter $A$ is reserved for the area of a loop and $P$ for its perimeter.

## 1. The question

Consider two static charges $\pm q$ at distance $R$ in three-dimensional compact QED. [[week-06-wilson-action-strong-coupling|Week 6]] showed that at strong coupling every compact lattice gauge theory confines them, with an area law from the character expansion. That result says nothing about the continuum. In three dimensions $e^2$ has mass dimension one and $\beta=1/(e^2a_{\rm lat})$, so the continuum limit $a_{\rm lat}\to0$ at fixed $e^2$ is the weak-coupling limit $\beta\to\infty$. There perturbation theory sees an almost free photon and the logarithmic potential of noncompact electrodynamics, $V(R)=\frac{q^2e^2}{2\pi}\ln(R/a_{\rm lat})+{\rm const}$ (Week 8, Problem 1), the marginal case of [[courses/generalized-symmetries-course/conventions|conventions]] §6. The only objects it misses are the monopoles, each with weight $e^{-4.99\beta}$.

The question of the week is whether these rare events change the physics at long distances. Polyakov's answer is that they change it completely. The monopoles form a plasma that screens magnetic fields over a length $m_\gamma^{-1}\propto e^{S_{\rm mono}/2}$, and the same plasma confines electric charge with a tension $\sigma_{\rm str}=(2/\pi^2)\,e^2m_\gamma$. Both effects are exponentially small at weak coupling, and both are nonzero. We compute the photon mass (§3) and the Wilson loop (§§4–6) with every constant, and we identify the single parameter that controls every approximation at weak coupling (§7). The step on which everything rests is §4, what a Wilson loop becomes in the dual variables: a vortex line of the dual photon, whose unwinding costs an area.

## 2. The starting point: the exact dual photon and the dilute plasma

[[week-08-dual-variables-abelian-gauge|Week 8]] (§4.5) rewrote the Villain partition function on the $L^3$ torus exactly,
$$
Z=\frac{(2\pi\beta)^{-N_P/2}}{(2\pi)^{N^*}}\sum_{w\in\mathbb{Z}^3}\ \sum_{v\in C^0(\Lambda^*,\mathbb{Z})}\int_{\mathbb{R}^{N^*}/2\pi\mathbb{Z}}d^{N^*}\sigma\ \exp\Big(-\frac1{8\pi^2\beta}\big\|d\sigma-2\pi w\cdot\tilde M\big\|^2-i\langle v,\sigma\rangle\Big),\qquad v=\star dn,
$$
where σ is the dual photon on the $N^*$ dual sites (the cube centers), $w$ labels the electric flux sectors, and the integers $v_{c^*}=m_c$ are the monopole numbers of the cubes. Integrating σ gives the monopole Coulomb gas, with $S_{\rm mono}=2\pi^2G_3(0)\beta=4.99\,\beta$ per unit monopole and pair interaction $4\pi^2\beta\,q_iq_jG_3$. In physical units, with the magnetic charges $q_i=-m_c$ of [[courses/generalized-symmetries-course/conventions|conventions]] §5 and $G(r)=1/4\pi r$, the interaction energy is
$$
E_{\rm int}=\frac{4\pi^2}{e^2}\sum_{i<j}q_iq_j\,G(x_i-x_j)=\frac{2\pi^2}{e^2}\sum_{i\ne j}q_iq_j\,G(x_i-x_j),
$$
the coefficient on which the Debye match of §3.2 depends. [[week-09-compact-qed3-monopole-plasma|Week 9]] organized this gas as a dilute instanton gas (its §2) and showed (its §3) that at distances large compared with $a_{\rm lat}$ it is the sine-Gordon theory
$$
S[\sigma]=\int d^3x\,\Big[K(\partial\sigma)^2-2\zeta\cos\sigma\Big],\qquad K\equiv\frac{e^2}{8\pi^2},\qquad \zeta=\frac{e^{-S_{\rm mono}}}{a_{\rm lat}^3},
$$
where $2\zeta\cos\sigma$ is the grand-canonical sum over unit monopoles inserted as $e^{\pm i\sigma}$, and ζ is the fugacity per unit volume of each species with vertex operators normal-ordered at the lattice scale ([[courses/generalized-symmetries-course/conventions|conventions]] §5). Dimensions: σ is dimensionless, $K$ and $e^2$ have mass dimension one, and ζ has mass dimension three. The only dimensionless combination of the couplings is therefore
$$
\frac{\zeta}{e^6}=\beta^3e^{-4.99\beta},
$$
exponentially small at weak coupling. §7 shows that on the weak-coupling branch it controls every approximation of the week; it is small at strong coupling too, where the gas is dense, so it controls nothing there without the condition $\beta\gg1$ (Week 9 F1). The kinetic term alone is invariant under $\sigma\to\sigma+c$, the magnetic $U(1)^{(0)}$ of the form-degree table ([[courses/generalized-symmetries-course/conventions|conventions]] §6, [[higher-form-symmetries]]), a 0-form symmetry in $d=3$ whose charged operators are the local monopole operators $e^{iq\sigma}$. The cosine breaks it explicitly, and both results of the week follow from that breaking.

## 3. The photon mass from both faces [Computed.]

### 3.1 The field face

Expanding the cosine around its minimum σ = 0,
$$
-2\zeta\cos\sigma=-2\zeta+\zeta\sigma^2-\frac{\zeta}{12}\sigma^4+O(\sigma^6),
$$
the quadratic action is $\int\big[K(\partial\sigma)^2+\zeta\sigma^2\big]=\frac12\int\sigma\,(-2K\nabla^2+2\zeta)\,\sigma$, and the propagator is
$$
\langle\sigma(x)\sigma(0)\rangle=\int\frac{d^3k}{(2\pi)^3}\,\frac{e^{ik\cdot x}}{2K(k^2+m_\gamma^2)}=\frac{e^{-m_\gamma|x|}}{8\pi K|x|},
$$
where
$$
\boxed{\ m_\gamma^2=\frac{\zeta}{K}=\frac{8\pi^2\zeta}{e^2},\qquad m_\gamma=\frac{2\pi\sqrt{2\zeta}}{e},\qquad (m_\gamma a_{\rm lat})^2=8\pi^2\beta\,e^{-4.99\beta}.\ }
$$
Through $B_\mu=\frac{ie^2}{2\pi}\partial_\mu\sigma$ the magnetic-field correlator inherits the factor $e^{-m_\gamma r}$: the $1/r^3$ correlations of the massless photon are cut off at the Debye length $m_\gamma^{-1}$, which at weak coupling is exponentially long in lattice units ($1/m_\gamma a_{\rm lat}\simeq1.2\times10^3$ at β = 4).

### 3.2 The gas face: Debye–Hückel with the Coulomb coefficient of §2

Place a test monopole of charge $q_0$ at the origin. The energy of a plasma monopole of charge $q$ at $x$ is $q\,\psi(x)$, where, by $E_{\rm int}$ of §2 and $-\nabla^2G=\delta^3$,
$$
-\nabla^2\psi=\frac{4\pi^2}{e^2}\Big[q_0\,\delta^3(x)+\rho(x)\Big],
$$
and ρ is the mean magnetic charge density of the plasma. In the dilute plasma each species has the Boltzmann density $n_\pm(x)=\zeta e^{\mp\psi(x)}$, so that $\rho=n_+-n_-=-2\zeta\sinh\psi$, and the mean potential obeys the Poisson–Boltzmann equation
$$
-\nabla^2\psi+\frac{8\pi^2\zeta}{e^2}\sinh\psi=\frac{4\pi^2q_0}{e^2}\,\delta^3(x).
$$
Far from the test charge $|\psi|\ll1$, and the equation linearizes (Debye–Hückel),
$$
\big(-\nabla^2+m_D^2\big)\psi=\frac{4\pi^2q_0}{e^2}\,\delta^3(x),\qquad m_D^2=\frac{4\pi^2}{e^2}\cdot2\zeta=\frac{8\pi^2\zeta}{e^2}=m_\gamma^2,\qquad \psi(r)=\frac{\pi q_0}{e^2}\,\frac{e^{-m_\gamma r}}{r}.
$$
The two faces agree. The linearization needs $\pi/(e^2r)\ll1$, that is, $r\gg\ell_B\equiv\pi/e^2$, the distance at which the Coulomb energy of two unit monopoles equals one; this holds at $r\sim m_\gamma^{-1}$ because $m_\gamma\ell_B=2\sqrt2\,\pi^2(\zeta/e^6)^{1/2}\ll1$. With the coefficient $2\pi^2/e^2$ for $i<j$ the same computation gives $4\pi^2\zeta/e^2$ and the match fails, so the Debye mass is a sharp test of the Coulomb normalization. Week 9 §4 derives Debye–Hückel from the gas in full and checks $m_D$ against the rigorous result of Göpfert and Mack; here we need its result and the following identity.

### 3.3 One equation: the sine-Gordon saddle is the Poisson–Boltzmann equation

Insert the test monopole on the field side as the operator $e^{iq_0\sigma(0)}$. The saddle of $S[\sigma]-iq_0\sigma(0)$ solves
$$
-2K\nabla^2\sigma+2\zeta\sin\sigma=iq_0\,\delta^3(x),
$$
and with $\sigma=i\psi$, using $\sin(i\psi)=i\sinh\psi$ and dividing by $2Ki$,
$$
-\nabla^2\psi+\frac{\zeta}{K}\sinh\psi=\frac{q_0}{2K}\,\delta^3(x).
$$
Since $\zeta/K=8\pi^2\zeta/e^2$ and $1/2K=4\pi^2/e^2$, this is the Poisson–Boltzmann equation of §3.2 identically, nonlinearity included. The saddle of the sine-Gordon theory is the mean-field theory of the plasma, its value at imaginary σ is the mean potential, and the fluctuations around the saddle are the correlations that mean field neglects, suppressed by the parameter of §7. That is why the Debye mass, the curvature of the cosine and the pole of the propagator are one number.

> **Physical picture.** Without monopoles σ is the Goldstone boson of the spontaneously broken magnetic $U(1)^{(0)}$, and the photon is massless. The fugacity breaks the symmetry explicitly, and the mass obeys $m_\gamma^2=\zeta/K$, explicit breaking over stiffness, with the structure of the pion-mass relation [Formal analogy.]. A simulation deep in the dilute regime would see plaquette–plaquette correlators decay as $e^{-m_\gamma r}$ with $m_\gamma a_{\rm lat}$ from the box of §3.1, which requires lattices much larger than the Debye length, $10^3$–$10^4$ sites across at β = 4–5 (§7). What the plasma screens is magnetic charge; electric charge is not screened in this theory at all (F3).

## 4. The Wilson loop through the duality [Proved. for §§4.1–4.4]

This section carries a Wilson loop through the moves of [[week-08-dual-variables-abelian-gauge|Week 8]] §§3–4, line by line. It completes Week 8's Problem 1, which stopped at the sector without monopoles.

### 4.1 The source through Moves 1–3

Let $C$ be a closed loop of links with oriented indicator $J_C\in C^1(\Lambda,\mathbb{Z})$, and let Σ be an integer 2-chain with $\partial\Sigma=C$ and indicator $\mathbb{1}_\Sigma$, so that $\delta\mathbb{1}_\Sigma=J_C$ (Week 8 §2.2). Insert $W_q(C)=e^{iq\langle J_C,a\rangle}$ with $q\in\mathbb{Z}$:
$$
Z[W_q]=\prod_\ell\int_{-\pi}^{\pi}\frac{da_\ell}{2\pi}\sum_{n\in C^2(\Lambda,\mathbb{Z})}\exp\Big(-\frac\beta2\|da-2\pi n\|^2+iq\langle J_C,a\rangle\Big),\qquad \langle W_q(C)\rangle=\frac{Z[W_q]}{Z}.
$$
Moves 1 and 2 (Hubbard–Stratonovich on each plaquette, and the Dirac comb) do not touch the insertion and give
$$
Z[W_q]=(2\pi\beta)^{-N_P/2}\prod_\ell\int_{-\pi}^{\pi}\frac{da_\ell}{2\pi}\sum_{b\in C^2(\Lambda,\mathbb{Z})}e^{-\frac1{2\beta}\|b\|^2+i\langle\delta b+qJ_C,\,a\rangle}.
$$
Move 3 integrates each $a_\ell$ over one period, $\int_{-\pi}^{\pi}\frac{da_\ell}{2\pi}\,e^{i[(\delta b)_\ell+qJ_C(\ell)]a_\ell}=\delta_{(\delta b)_\ell,\,-qJ_C(\ell)}$, so the electric flux is closed except along $C$,
$$
\delta b=-q\,J_C ,
$$
which is Gauss's law with the static charges. Since $\delta\mathbb{1}_\Sigma=J_C$, the general solution is $b=b'-q\mathbb{1}_\Sigma$ with $\delta b'=0$, and Week 8 §4.1 writes $b'=\star(d\tilde h+w\cdot\tilde M)$ with integer heights $\tilde h$ on the dual sites. With $\star\star=+1$ and $\|\star f\|=\|f\|$,
$$
Z[W_q]=(2\pi\beta)^{-N_P/2}\sum_{w\in\mathbb{Z}^3}\ \sum_{\tilde h\in\mathbb{Z}^{N^*}/\mathbb{Z}\cdot\mathbb{1}}\exp\Big(-\frac1{2\beta}\big\|d\tilde h+w\cdot\tilde M-q\star\mathbb{1}_\Sigma\big\|^2\Big),
$$
where $\star\mathbb{1}_\Sigma\in C^1(\Lambda^*,\mathbb{Z})$ is 1 on the dual links that pierce Σ along its right-handed normal and 0 elsewhere (the shuffle signs of [[courses/generalized-symmetries-course/conventions|conventions]] §2 see to the orientation). At strong coupling the leading term is $\tilde h=0$, $w=0$: the flux sheet $b=-q\mathbb{1}_\Sigma$ on the smallest Σ, of weight $e^{-q^2|\Sigma|/2\beta}$, which is the strong-coupling area law of the Villain action with tension $q^2/2\beta$ per plaquette. At weak coupling the heights take over: heights that jump by $q$ across Σ cancel the sheet, and replacing Σ by $\Sigma+\partial V$ is the relabelling $\tilde h\to\tilde h-q\star\mathbb{1}_V$ (Week 8, Problem 1(b)).

### 4.2 Heights, Poisson resummation and the dual form

Moves 4 and 5 act on the heights and are unchanged; only the resummed function changes, $F(\tilde\varphi)=\exp\big(-\frac1{2\beta}\|d\tilde\varphi+w\cdot\tilde M-q\star\mathbb{1}_\Sigma\|^2\big)$. With $\sigma=-2\pi\tilde\varphi$ we have $\frac1{2\beta}\|{-d\sigma/2\pi}+X\|^2=\frac1{8\pi^2\beta}\|d\sigma-2\pi X\|^2$ for any real 1-cochain $X$, and therefore
$$
\boxed{\ Z[W_q]=\frac{(2\pi\beta)^{-N_P/2}}{(2\pi)^{N^*}}\sum_{w\in\mathbb{Z}^3}\ \sum_{v\in C^0(\Lambda^*,\mathbb{Z})}\int_{\mathbb{R}^{N^*}/2\pi\mathbb{Z}}d^{N^*}\sigma\ \exp\Big(-\frac1{8\pi^2\beta}\big\|d\sigma-2\pi\tilde n\big\|^2-i\langle v,\sigma\rangle\Big),\qquad \tilde n=w\cdot\tilde M-q\star\mathbb{1}_\Sigma .\ }
$$
This is the formula of §2 with a single change: the integer 1-cochain $\tilde n$ that accompanies $d\sigma$ acquires the term $-q\star\mathbb{1}_\Sigma$. The monopole sources $e^{-i\langle v,\sigma\rangle}$ are untouched.

### 4.3 The Wilson loop is a vortex line of σ

In the language of Week 8 §6, compact QED₃ is the vortex-free Villain XY model of σ: without the loop, $\tilde n=w\cdot\tilde M$ is closed. With the loop,
$$
d\tilde n=-q\,d\star\mathbb{1}_\Sigma=-q\star\delta\mathbb{1}_\Sigma=-q\star J_C,
$$
where we used $d\tilde M=0$ and, from [[courses/generalized-symmetries-course/conventions|conventions]] §2, $\delta=+\star d\star$ on 2-cochains in $d=3$ (the sign $(-1)^{d(p+1)+1}$ at $p=2$) together with $\star\star=+1$, so that $\star\delta\mathbb{1}_\Sigma=d\star\mathbb{1}_\Sigma$. By the vorticity rule of [[courses/generalized-symmetries-course/conventions|conventions]] §4, $d(d\sigma-2\pi\tilde n)=-2\pi\,d\tilde n$, the branch-reduced gradient of σ circulates around the dual plaquette $\ell^*$ pierced by a link ℓ of $C$ as
$$
\sum_{\partial\ell^*}\big(d\sigma-2\pi\tilde n\big)=2\pi q\,(\star J_C)(\ell^*)=2\pi q\,\epsilon\,J_C(\ell),
$$
and the shuffle sign ε orients $\ell^*$ with its right-handed normal along ℓ. Therefore
$$
\boxed{\ \text{a Wilson loop of charge }q\text{ is a vortex line of the dual photon along }C\text{: }\sigma\text{ winds by }2\pi q\text{ around }C\text{ in the right-handed sense.}\ }
$$
The monopoles are the sources $e^{-im_c\sigma}$, local operators at the cube centers; the electric charges are vortex lines, the objects charged under the winding symmetry of σ, whose degree is $d-2=1$ and which is the electric 1-form symmetry of $a$ ([[courses/generalized-symmetries-course/conventions|conventions]] §6, Week 8 §6). The spanning surface enters only through the particular solution. Replacing Σ by $\Sigma+\partial V$ changes $\tilde n$ by $q\,d\star\mathbb{1}_V$ (by $\star\delta\eta=-d\star\eta$ for $\eta\in C^3$, [[courses/generalized-symmetries-course/conventions|conventions]] §5), an exact integer cochain, and the change of variables $\sigma\to\sigma-2\pi q\star\mathbb{1}_V$, a shift by multiples of $2\pi$ at the dual sites inside $V$, restores the integrand, the factor $e^{-i\langle v,\sigma\rangle}$ included because $v$ is integer. The identity $d\star\mathbb{1}_\Sigma=\star J_C$ was checked cell by cell on the $24^3$ torus for an $8\times8$ loop.

### 4.4 The phase of the monopoles and the solid angle

The vortex form hides the monopoles' point of view. To expose it, decompose $\star\mathbb{1}_\Sigma$ on the dual lattice by Hodge (Week 2 §6),
$$
\star\mathbb{1}_\Sigma=d\omega_\Sigma+c_C+h_\Sigma,\qquad \omega_\Sigma=G'\,\delta\star\mathbb{1}_\Sigma,\qquad c_C=\delta\,G'\star J_C,
$$
where $G'$ inverts the Laplacian on the complement of its kernel and $h_\Sigma$ is harmonic. The two formulas follow by applying δ and $d$ to both sides: $\delta\star\mathbb{1}_\Sigma=\delta d\omega_\Sigma=\Delta\omega_\Sigma$, since $\delta c_C=0$ and $\delta h_\Sigma=0$; and $d\star\mathbb{1}_\Sigma=dc_C=(\Delta-\delta d)G'\star J_C=\star J_C$, since $d\star J_C=\pm\star\delta J_C=0$ for a closed loop. Only $d\omega_\Sigma$ and $h_\Sigma$ depend on Σ. In the sector $w=0$,
$$
d\sigma+2\pi q\star\mathbb{1}_\Sigma=d\sigma'+2\pi q\,(c_C+h_\Sigma),\qquad \sigma'\equiv\sigma+2\pi q\,\omega_\Sigma ,
$$
a sum of an exact, a coexact and a harmonic cochain, which are mutually orthogonal, so that
$$
\frac1{8\pi^2\beta}\big\|d\sigma+2\pi q\star\mathbb{1}_\Sigma\big\|^2=\frac1{8\pi^2\beta}\|d\sigma'\|^2+\frac{q^2}{2\beta}\Big(\|c_C\|^2+\|h_\Sigma\|^2\Big),\qquad \|c_C\|^2=\langle\star J_C,G'\star J_C\rangle=\langle J_C,GJ_C\rangle,
$$
where the last equalities use $\|\delta G'\star J_C\|^2=\langle G'\star J_C,\,d\delta G'\star J_C\rangle$, $d\delta=\Delta-\delta d$ once more, and the fact that ⋆ intertwines the Laplacians, which act on each component as the site Laplacian. The passage to σ′ is a translation of the integration variable ($\omega_\Sigma$ has zero mean, so the zero mode is untouched), and it moves the Σ-dependence into the source, $-i\langle v,\sigma\rangle=-i\langle v,\sigma'\rangle+2\pi iq\langle v,\omega_\Sigma\rangle$. The σ′ integral is Week 8's Move 6 and gives $Z_{\rm ph}\,e^{-2\pi^2\beta\langle v,G'v\rangle}$. On the infinite lattice, where $\|h_\Sigma\|^2=\sum_\mu A_\mu^2/L^3\to0$ ($A_\mu$ the signed area of the projection of Σ on the plane normal to μ) and the sectors $w\ne0$ are suppressed (F5), dividing by $Z$ gives
$$
\boxed{\ \langle W_q(C)\rangle=e^{-\frac{q^2}{2\beta}\langle J_C,GJ_C\rangle}\ \Big\langle\exp\Big(-iq\sum_iq_i\,\eta_C(x_i)\Big)\Big\rangle_{\rm gas},\qquad \eta_C\equiv2\pi\,\omega_\Sigma\ \ ({\rm mod}\ 2\pi),\ }
$$
where the average is over the exact Coulomb gas of Week 8 §4.4 and $q_i=-m_c$ are the magnetic charges at the sites $x_i=c^*$.

The first factor is the free-photon value of Week 8's Problem 1(c), $\exp\big[-\frac{q^2e^2}2\oint_C\oint_C\frac{dl\cdot dl'}{4\pi|l-l'|}\big]$ in physical units: photons and monopoles decouple exactly, and the monopoles enter through the phase alone. That phase is geometric. In the continuum $\delta\star\mathbb{1}_\Sigma$ becomes $-\nabla\cdot(\hat n\,\delta_\Sigma)$, a dipole layer on Σ, and
$$
\omega_\Sigma(x)=-\int d^3y\,G(x-y)\,\nabla_y\cdot\big(\hat n\,\delta_\Sigma(y)\big)=\int_\Sigma dS_y\,\hat n\cdot\nabla_yG(x-y)=\frac1{4\pi}\int_\Sigma dS_y\,\frac{\hat n\cdot(x-y)}{|x-y|^3}=\frac{\Omega_C(x)}{4\pi},
$$
where $\Omega_C(x)$ is the solid angle that a surface spanning $C$ subtends at $x$, positive on the side into which the right-handed normal of $C$ points. Therefore
$$
\eta_C(x)=\tfrac12\,\Omega_C(x),
$$
half the solid angle. It jumps by $2\pi$ across the spanning surface, so $e^{i\eta_C}$ is continuous and depends on $C$ alone: changing Σ to $\Sigma+\partial V$ changes $\omega_\Sigma$ by $-\star\mathbb{1}_V$ plus a constant, an integer at every site, which the phase does not see (the constant drops out by neutrality, $\sum_iq_i=0$). On the lattice we computed $\omega_\Sigma$ by fast Fourier transform for an $8\times8$ loop and compared $2\pi\omega_\Sigma$ with $\Omega_C/2$ on the $72^3$ torus at the dual sites offset by $(\frac12,\frac12,z)$ lattice spacings from the center of the loop: at $z=\frac12$, 2.7700 against 2.7835; at $z=6.5$, 0.5526 against 0.5516; the differences reach a few per cent only within a spacing or two of the edges. On the $24^3$ torus $\|c_C\|^2=14.80845$ equals $\langle J_C,GJ_C\rangle$ to all digits shown, and the Σ-shift of $\omega_\Sigma$ is $-\star\mathbb{1}_V$ up to a constant, exactly.

> **Physical picture.** The phase $-q_i\eta_C(x_i)=-\frac12q_i\Omega_C(x_i)$ is the magnetic flux of monopole $i$ through the loop: its total flux $2\pi q_i$ times the fraction of the sphere that the spanning surface covers, with the sign of the normal. The boxed formula is therefore $W_q=e^{iq\int_\Sigma F}$ evaluated in the monopole background, the Aharonov–Bohm phase of the probe around the monopoles' flux, times the photon part; this reading is exact. As a monopole is carried once around $C$ its phase winds by $2\pi q$, the monodromy seen from the monopole side. Without screening, a monopole anywhere within a distance $R$ of a loop of size $R$ shifts the phase by $O(1)$, and the loop decays with a volume law, $e^{-c\,\zeta R^3}$ (Problem 1). In the plasma the flux of each monopole is neutralized by its screening cloud beyond $m_\gamma^{-1}$, so only monopoles within about $m_\gamma^{-1}$ of the wall randomize the phase, and $-\ln\langle W\rangle\sim\zeta\,m_\gamma^{-1}A=\sqrt{K\zeta}\,A$, the parametric form of the tension derived in §5 [Heuristic.].

### 4.5 The loop in the dilute plasma [Computed within the dilute-plasma description of Week 9 §3.]

The dilute-plasma rewriting of Week 9 §3 applies to the gas with the phases, each vertex $\zeta e^{iq_i\sigma(x_i)}$ now multiplied by $e^{-iqq_i\eta_C(x_i)}$; summing over $q_i=\pm1$ replaces $2\zeta\cos\sigma$ by $2\zeta\cos(\sigma-q\eta_C)$, and
$$
\langle W_q(C)\rangle=\exp\Big[-\frac{q^2e^2}{2}\oint_C\oint_C\frac{dl\cdot dl'}{4\pi|l-l'|}\Big]\ \frac{\mathcal Z[q\eta_C]}{\mathcal Z[0]},\qquad \mathcal Z[\eta]=\int\mathcal D\sigma\ \exp\Big(-\int d^3x\,\big[K(\partial\sigma)^2-2\zeta\cos(\sigma-\eta)\big]\Big).
$$
In the presence of the loop, $\cos\sigma$ becomes $\cos(\sigma-q\eta_C)$ with $\eta_C$ half the solid angle. The same statement in the vortex form of §4.3 follows by a change of variables. Let $\hat\eta_C$ be the continuous, multivalued version of $\eta_C$; since $\eta_C$ jumps by $+2\pi$ across the spanning surface along the normal, $\hat\eta_C$ winds by $-2\pi$ around $C$ in the right-handed sense, and $\sigma_C\equiv\sigma-q\hat\eta_C$ winds by $+2\pi q$. Then $\cos(\sigma-q\eta_C)=\cos\sigma_C$ and
$$
\int K(\partial\sigma)^2=\int K(\partial\sigma_C)^2-Kq^2\int(\partial\hat\eta_C)^2,
$$
because the cross terms reduce to $\int\partial\sigma\cdot\partial\hat\eta_C$, which vanishes: σ is single-valued, and $\partial\hat\eta_C$ is single-valued and divergence-free, being $2\pi$ times the Biot–Savart field $B_C$ of a unit current along $C$ up to sign. The Neumann formula for the inductance, $\int B_C^2=\oint\oint\frac{dl\cdot dl'}{4\pi|l-l'|}$, gives $Kq^2\int(\partial\hat\eta_C)^2=4\pi^2Kq^2\oint\oint\frac{dl\cdot dl'}{4\pi|l-l'|}=\frac{q^2e^2}2\oint\oint\frac{dl\cdot dl'}{4\pi|l-l'|}$, which cancels the Coulomb prefactor. Therefore
$$
\boxed{\ \langle W_q(C)\rangle=\frac{1}{\mathcal Z[0]}\int_{\sigma\ \text{winding }2\pi q\text{ around }C}\mathcal D\sigma\ \exp\Big(-\int d^3x\,\big[K(\partial\sigma)^2-2\zeta\cos\sigma\big]\Big),\ }
$$
the continuum form of §4.3: the Coulomb self-energy of the loop is the gradient energy of the vortex, and the monopoles see the loop only through the winding.

## 5. The wall and the area law

### 5.1 Unwinding the monodromy

Consider the saddle point of the last boxed functional for a large planar loop, $R\gg m_\gamma^{-1}$. A finite-action configuration approaches a vacuum $\sigma\in2\pi\mathbb{Z}$ far from $C$ and winds by $2\pi q$ around $C$. The two requirements are compatible only if σ leaves the vacuum on every path that links $C$: along such a path the lift of σ gains $2\pi q$, so it passes through $\pi$ (mod $2\pi$) at least $|q|$ times, and the set where $\sigma\equiv\pi$ contains a surface bounded by $C$. That surface is the wall. Its position is decided by minimizing the action, and nothing ties it to Σ. Figure 1 shows the cross-section.

The literal jump is the configuration that the lattice formula suggests, and it has to be kept apart from the wall. Take $\sigma=0$ in the boxed formula of §4.2: the lift jumps by $2\pi q$ across Σ, $\cos\sigma=1$ everywhere, and the monopoles do not see it. Its only cost is the gradient term on the dual links through Σ, $\frac1{8\pi^2\beta}(2\pi q)^2=\frac{q^2}{2\beta}$ per plaquette, which is the strong-coupling flux sheet of §4.1, with tension $q^2e^2/2a_{\rm lat}$ in physical units, divergent in the continuum. Spreading the unwinding over a length ℓ costs gradient energy $\sim4\pi^2q^2K/\ell$ and potential energy $\sim\zeta\ell$ per unit area; the balance is at $\ell\sim m_\gamma^{-1}$ and lowers the cost to $\sim\sqrt{K\zeta}$, exponentially small. §§5.2–5.3 do the balance exactly.

```
                              σ ≈ 2π   (the vacuum, ≡ 0)
            ↺
          ⊙ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ⊗
          ┆              σ ≈ 0   (the same vacuum)          ┆
          ┆                                                 ┆
          └┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

   ⊙ ⊗   the loop C crossing the page (out, in); σ winds by +2π around each crossing (↺ at ⊙)
   ━━━   the wall: σ passes through π on the flat disk; thickness ≈ 1.76/m_γ (Figure 2)
   ┄┄┄   a spanning surface Σ of the lattice formula, carrying ñ = −q⋆1_Σ: the literal jump,
         invisible to cos σ and removed by a 2π shift of σ in the region V between Σ and the disk
```
**Figure 1. Cross-section of a planar Wilson loop in the vortex picture. The action is spent in the band where the smooth field unwinds, located by minimization on the minimal surface; the surface Σ that carries the literal jump costs nothing in the cosine and can be moved at will.**

### 5.2 The kink [Computed.]

Deep inside a large planar loop the saddle depends only on the coordinate ξ normal to the wall. Subtracting the vacuum energy, the action per unit area is
$$
\frac SA=\int_{-\infty}^{\infty}d\xi\,\Big[K\sigma'^2+U(\sigma)\Big],\qquad U(\sigma)=2\zeta(1-\cos\sigma)=4\zeta\sin^2\frac\sigma2,
$$
with $\sigma(-\infty)=0$ and $\sigma(+\infty)=2\pi$ for $q=1$. The Euler–Lagrange equation is $2K\sigma''=U'(\sigma)=2\zeta\sin\sigma$, that is, $\sigma''=m_\gamma^2\sin\sigma$. Multiplying by $2K\sigma'$ and integrating, $K\sigma'^2-U(\sigma)$ is constant along ξ, and the boundary conditions ($\sigma'\to0$ and $U\to0$ at both ends) set the constant to zero:
$$
K\sigma'^2=U(\sigma)\quad\Longrightarrow\quad \sigma'=2m_\gamma\sin\frac\sigma2\qquad(0<\sigma<2\pi),
$$
where $\sqrt{U/K}=2\sqrt{\zeta/K}\,\sin\frac\sigma2$. Separating variables, $\int\frac{d\sigma}{2\sin(\sigma/2)}=\ln\tan\frac\sigma4=m_\gamma(\xi-\xi_0)$, so that
$$
\boxed{\ \sigma(\xi)=4\arctan e^{m_\gamma(\xi-\xi_0)},\qquad \sigma'(\xi)=\frac{2m_\gamma}{\cosh m_\gamma(\xi-\xi_0)},\qquad \varepsilon(\xi)\equiv K\sigma'^2+U=\frac{8Km_\gamma^2}{\cosh^2m_\gamma(\xi-\xi_0)} .\ }
$$
The center $\xi_0$ is a free collective coordinate, the translation zero mode of the wall. As Figure 2 shows, σ runs from $\pi/2$ to $3\pi/2$ over $2\,{\rm arccosh}\sqrt2/m_\gamma=1.763/m_\gamma$, which is also the full width at half maximum of ε; the rms width of ε is $\pi/(\sqrt{12}\,m_\gamma)=0.907/m_\gamma$. The thickness of the wall is the Debye length.

```
  2π ┤                                             •   •
     │                                     •   •
     │                                 •
     │                             •
   π ┤  · · · · · · · · · · · ·•· · · · · · · · · · · · · · ·
     │                     •
     │                 •
     │         •   •
   0 ┤ •   •
     └─┬───────┬───────┬───────┬───────┬───────┬───────┬────────▶ m_γξ
      −3      −2      −1       0      +1      +2      +3

   m_γξ :   −3     −2     −1      0     +1     +2     +3
   σ/π  :  0.06   0.17   0.45   1.00   1.55   1.83   1.94
   ε/ε₀ :  0.01   0.07   0.42   1.00   0.42   0.07   0.01       ε₀ = 8Km_γ²
```
**Figure 2. The unit wall $\sigma=4\arctan e^{m_\gamma\xi}$ (points at steps of $0.5/m_\gamma$) and its action density $\varepsilon=\varepsilon_0\cosh^{-2}m_\gamma\xi$: the field unwinds by $2\pi$ over a few Debye lengths, and half of ε is gradient energy, half potential energy.**

### 5.3 The Bogomolny bound and the tension [Computed.]

Before evaluating the action we prove that the kink is the minimum. For every configuration,
$$
K\sigma'^2+U(\sigma)=\big(\sqrt K\,\sigma'-\sqrt{U(\sigma)}\big)^2+2\sqrt{KU(\sigma)}\;\sigma'\ \ge\ 2\sqrt{KU(\sigma)}\;\sigma' ,
$$
so that
$$
\int d\xi\,\big[K\sigma'^2+U\big]\ \ge\ \int d\xi\,2\sqrt{KU(\sigma(\xi))}\;\sigma'(\xi)=\mathcal W\big(\sigma(+\infty)\big)-\mathcal W\big(\sigma(-\infty)\big),\qquad \mathcal W(s)=\int_0^s2\sqrt{KU(t)}\,dt,
$$
a bound that depends on the endpoints alone (the substitution $t=\sigma(\xi)$ holds whether or not σ is monotonic), with equality if and only if $\sqrt K\sigma'=\sqrt U$, the first-order equation of §5.2. This is the Bogomolny bound, and §5.2 found the configuration that saturates it. For $0\to2\pi$, with $\sqrt{KU(t)}=2\sqrt{K\zeta}\,\sin\frac t2$ on $[0,2\pi]$,
$$
\mathcal W(2\pi)=4\sqrt{K\zeta}\int_0^{2\pi}\sin\frac t2\,dt=4\sqrt{K\zeta}\,\Big[-2\cos\frac t2\Big]_0^{2\pi}=4\sqrt{K\zeta}\,(2+2)=16\sqrt{K\zeta},
$$
equivalently $2\sqrt{2K\zeta}\int_0^{2\pi}\sqrt{1-\cos t}\,dt$ with $\int_0^{2\pi}\sqrt{1-\cos t}\,dt=4\sqrt2$. The same number follows from the profile: by $K\sigma'^2=U$ the action density is $2K\sigma'^2$, and $\int2K\sigma'^2d\xi=8Km_\gamma^2\int\cosh^{-2}(m_\gamma\xi)\,d\xi=8Km_\gamma^2\cdot\frac2{m_\gamma}=16Km_\gamma$. With $\sqrt K=e/2\sqrt2\pi$ and $m_\gamma=\sqrt{\zeta/K}$,
$$
\boxed{\ \sigma_{\rm str}=16\sqrt{K\zeta}=16K\,m_\gamma=\frac{4\sqrt2}{\pi}\,e\sqrt\zeta=\frac{2}{\pi^2}\,e^2m_\gamma,\qquad \sigma_{\rm str}\,a_{\rm lat}^2=\frac{2}{\pi^2\beta}\,m_\gamma a_{\rm lat}.\ }
$$
Half of the tension is gradient energy and half potential energy, pointwise, by $K\sigma'^2=U$. The ratio $\sigma_{\rm str}/m_\gamma^2=16K/m_\gamma$ is large in the regime of validity (§7): the wall is heavy on the scale of its own thickness, which is what makes it semiclassical.

### 5.4 The area law [Proved at the classical level for planar loops; Controlled to leading order in $(\zeta/e^6)^{1/2}$.]

For a planar loop the kink gives the area law through a two-sided argument at the classical level.

*Lower bound.* Put $C$ in the plane $z=0$, bounding a region $D$ of area $A$. For $(x,y)\in D$ the vertical line through $(x,y)$, closed by a large arc on which σ sits in one vacuum, links $C$ once, so σ gains $2\pi q$ along it. Dropping the transverse gradients, which are non-negative, and the lines outside $D$, the Bogomolny bound on each line gives
$$
S-S_{\rm vac}\ \ge\ \int_Ddx\,dy\int_{-\infty}^{\infty}dz\,\Big[K(\partial_z\sigma)^2+U(\sigma)\Big]\ \ge\ A\,\big|\mathcal W(2\pi q)\big|=|q|\,\sigma_{\rm str}\,A,
$$
where $\mathcal W(2\pi q)=q\,\mathcal W(2\pi)$ because the integrand of $\mathcal W$ is $2\pi$-periodic.

*Upper bound.* The trial configuration equal to the kink in $z$ inside $D$, at distances larger than a few $m_\gamma^{-1}$ from $C$, joined to the vortex profile $\sigma\simeq q\times(\text{azimuthal angle around }C)$ near the loop, has action $|q|\sigma_{\rm str}A+O(P)$ for $q=\pm1$ (§6.1 builds the configuration for $|q|\ge2$). The perimeter term is the vortex self-energy: the gradient $q/r$ integrated from the lattice core to the wall thickness, beyond which the wall takes over, gives $2\pi Kq^2\ln(1/m_\gamma a_{\rm lat})+O(K)$ per unit length. With $2\pi K=e^2/4\pi$,
$$
\boxed{\ \langle W_q(C)\rangle=\exp\Big[-|q|\,\sigma_{\rm str}\,A(C)-\mu_q\,P(C)+o(P)\Big],\qquad \mu_q=\frac{q^2e^2}{4\pi}\,\ln\frac1{m_\gamma a_{\rm lat}}+O(q^2e^2),\ }
$$
at leading order in the semiclassical expansion. For a $T\times R$ rectangle with $T\gg R\gg m_\gamma^{-1}$ the static potential is linear,
$$
V(R)=|q|\,\sigma_{\rm str}\,R+{\rm const},
$$
while for $a_{\rm lat}\ll R\ll m_\gamma^{-1}$ it is the logarithm of Week 8's Problem 1. The crossover sits at $R\sim m_\gamma^{-1}$, where both are of order $e^2$, since $\sigma_{\rm str}/m_\gamma=2e^2/\pi^2$.

### 5.5 A lattice demonstration [Computed.]

The difference between the literal jump and the wall shows up in a minimization that anyone can repeat. Take σ real on the dual sites of a periodic lattice, with the classical action of §4.2 at $w=0$, $K\sum_{\tilde\ell}(d\sigma-2\pi\tilde n)^2+2\zeta\sum_{\tilde x}(1-\cos\sigma)$ with $\tilde n=-\star\mathbb{1}_\Sigma$ fixed; set $K=1$ in lattice units (the classical action is proportional to $K$) and $\zeta=m^2$, so that $m=m_\gamma a_{\rm lat}$; start from $\sigma=0$, the literal jump; and minimize with any gradient method (we used L-BFGS).

1. *Chain.* 400 sites with $\tilde n=-1$ on one link and $m=0.4$: the action drops from $4\pi^2=39.478$ to $6.38562$, against $16m=6.4$ in the continuum. The relative difference, $2.2\times10^{-3}$, is the lattice correction; it decreases like $m^2$, to $5.57\times10^{-4}$ at $m=0.2$ and $1.39\times10^{-4}$ at $m=0.1$ on the same chain.
2. *Wrapped strip.* Σ is a strip of width $R$ that wraps the torus in one direction, so that $C$ is two antiparallel lines and the problem reduces to a $160\times96$ cross-section. At $m=0.4$ the action per unit length is $6.38583\,R+24.14$ for $R=16$ to $40$, with successive slopes $6.38629$, $6.38565$ and $6.38562$, the tension of the chain. The intercept is the energy of the two vortex lines; repeating at $m=0.2$ and $0.1$ with the lattice scaled by $1/m$, the intercept minus $4\pi K\ln(1/m)$ is $12.631$, $12.660$ and $12.665$, which confirms the coefficient $2\pi K$ of the logarithm in $\mu_1$.
3. *Two spanning surfaces.* On the $36^3$ torus with a $12\times12$ square loop and $m=0.5$, take Σ flat (144 plaquettes) or $\Sigma+\partial V$, the open box of height 5 over it (384 plaquettes). The literal jumps cost $5684.9$ and $15159.7$; both relax to $1629.1435$, the two fields agree in $\cos\sigma$ to $6\times10^{-8}$, and in both runs σ passes through π between the two dual sites adjacent to the flat square, so the wall sits on the minimal surface whichever surface carried the literal jump. Of the final action, $7.9717\times144=1147.9$ is the lattice tension at $m=0.5$ times the area, and the rest is perimeter.

## 6. Charges, surfaces and symmetry

### 6.1 Charge $q$ [Computed at the classical level; the upper bound is Sketched.]

For $|q|\ge2$ the lower bound of §5.4 still gives $|q|\sigma_{\rm str}A$, but no single wall saturates it. The first-order equation $\sqrt K\sigma'=\sqrt U=2\sqrt\zeta\,|\sin\frac\sigma2|$ has fixed points at every multiple of $2\pi$, so a solution that leaves 0 reaches $2\pi$ only as $\xi\to\infty$ and never continues to $4\pi$. The infimum is approached by $|q|$ unit walls at large mutual distances $d$: their action per unit area is $|q|\sigma_{\rm str}$ plus an interaction that decays as $e^{-m_\gamma d}$ and is repulsive for walls of the same orientation (Problem 2 computes it). In a finite loop the walls are pinned to $C$ and bulge apart in the middle; a separation of order $m_\gamma^{-1}\ln(m_\gamma R)$ makes the repulsion and the extra area, of order $\sigma_{\rm str}d^2$ per wall, both subleading in $A$. With caps that bulge to this separation the walls still overlap on a fraction $\simeq1/(2\ln m_\gamma R)$ of the area, so the excess over $|q|\sigma_{\rm str}A$ is $o(A)$ only by a logarithm; walls that separate within about $d$ of $C$ bring it down to $O(Pd)$, with $P$ the perimeter of $C$. Therefore
$$
\boxed{\ \sigma_{{\rm str},q}=|q|\,\sigma_{\rm str}\quad\text{at leading order in the semiclassical expansion,}\ }
$$
exactly additive, with no saturation and no string breaking at any separation. The dependence on $q$ is linear at weak coupling, while the Villain strong-coupling tension $q^2/2\beta$ of §4.1 is quadratic; neither saturates, because nothing in pure compact QED₃ can end electric flux (F3).

### 6.2 Surface independence, precisely [Proved.]

Three statements of different status are involved. (1) *Exact:* $\langle W_q(C)\rangle$ depends on $C$ alone. Σ enters the boxed formulas of §§4.2 and 4.4 only through $\tilde n$ and $\omega_\Sigma$, whose changes under $\Sigma\to\Sigma+\partial V$ are $q\,d\star\mathbb{1}_V$ and $-\star\mathbb{1}_V$ plus a constant, integer-valued, and they are absorbed by a shift of σ by $2\pi q\star\mathbb{1}_V$, which is invisible because σ is compact and the monopole charges are integers. In the dual variables surface independence is the compactness of σ, the magnetic half of Dirac quantization (Week 8 §4.5). (2) *Geometric:* the tension sits where σ passes through π, on a surface bounded by $C$ whose position is fixed by minimization (§§5.1 and 5.5). (3) *Dynamical:* for planar loops the bound of §5.4 selects the flat disk, at the classical level; for a smooth non-planar loop whose curvature radius exceeds $m_\gamma^{-1}$, the thin wall is a membrane of tension $|q|\sigma_{\rm str}$ that minimizes its area, so $A(C)$ is the area of the minimal surface, the soap film, with corrections of relative order $1/m_\gamma R_{\rm curv}$ [Heuristic.].

### 6.3 The symmetry reading

In the language of [[courses/generalized-symmetries-course/conventions|conventions]] §6, pure compact QED₃ has an exact electric $U(1)^{(1)}$, with current $\star F/e^2$, because it has no dynamical charges. The area law says that this symmetry is unbroken, with charged lines of tension $|q|\sigma_{\rm str}$. The magnetic $U(1)^{(0)}$ is broken explicitly by ζ, and the photon is its pseudo-Goldstone boson, with $m_\gamma^2=\zeta/K$. In the dual variables the electric 1-form symmetry is the winding symmetry of σ: the Wilson lines are its vortex lines, and the monopoles, which are sources $e^{\pm i\sigma}$, leave it exact. The symmetry that the monopoles break is the one whose would-be Goldstone boson is the photon, and that breaking is what confines. The mechanism shares with the [[dual-superconductor]] one essential feature, electric flux squeezed into a tube by magnetic objects. It differs in the others: the magnetic objects are instantons of a plasma, the tube is a sine-Gordon wall, and no condensate breaks a magnetic symmetry spontaneously [Formal analogy.].

## 7. The validity chain [Controlled to leading order in $(\zeta/e^6)^{1/2}$ at $\beta\gg1$.]

The result rests on five steps, each with a condition. On the weak-coupling branch $\beta\gg1$, which puts the monopole core far inside the Bjerrum length ($\ell_B/a_{\rm lat}=\pi\beta$) and makes the gas dilute, every remaining condition is a power of $\zeta/e^6=\beta^3e^{-4.99\beta}$. The branch condition matters, because $\zeta/e^6$ is also small at strong coupling, with maximum 0.011 at β = 0.60, where the lattice is filled with monopoles (Week 9 F1).

0. *Exact rewriting* (Week 8 and §4): the Villain theory with the loop is the Coulomb gas with the phases of §4.4, at every β, with no approximation.
1. *Dilute gas* (Week 9 §2.4): monopoles of charge $|q_i|\ge2$ and overlapping cores are neglected. The density is $n=2\zeta$ and $n a_{\rm lat}^3=2e^{-4.99\beta}$, so the corrections are $O(e^{-S_{\rm mono}})$.
2. *Mean field* (§3; Week 9 §§2.5 and 4): many monopoles per Debye volume. With $\zeta=Km_\gamma^2$ the Debye number is
$$
N_D=\frac{n}{m_\gamma^3}=\frac{2\zeta}{m_\gamma^3}=\frac{2K}{m_\gamma}=\frac{1}{8\sqrt2\,\pi^3}\Big(\frac{e^6}{\zeta}\Big)^{1/2},
$$
the Debye length over the mean separation $\bar r=n^{-1/3}$ is $2^{5/6}e/(4\pi\zeta^{1/6})$, and the linearization of §3.2 needs $m_\gamma\ell_B=2\sqrt2\,\pi^2(\zeta/e^6)^{1/2}\ll1$.
3. *Semiclassical wall:* rescaling $x=y/m_\gamma$ turns the action into $\frac{K}{m_\gamma}\int d^3y\,\big[(\partial_y\sigma)^2-2\cos\sigma\big]$, so the loop-counting parameter is $\hbar_{\rm eff}=m_\gamma/K=2/N_D=16\sqrt2\,\pi^3(\zeta/e^6)^{1/2}\simeq702\,(\zeta/e^6)^{1/2}$, and the action of the wall per Debye area is $\sigma_{\rm str}/m_\gamma^2=16K/m_\gamma=8N_D$. Loop corrections to $\sigma_{\rm str}$ and $m_\gamma$ are of relative order $1/N_D$; their coefficients are not computed here.
4. *Thin wall:* $m_\gamma R\gg1$, a condition on the size of the loop, met at any coupling once $R$ is large enough.

Steps 2 and 3 have the same parameter, $N_D\gg1$: the plasma is weakly coupled exactly when its sine-Gordon description is semiclassical. The table puts numbers on the window for the Villain action, with $\zeta=e^{-4.99\beta}/a_{\rm lat}^3$.

| β | $\zeta/e^6$ | $N_D$ | $\bar r\,m_\gamma$ | $1/m_\gamma a_{\rm lat}$ | $\sigma_{\rm str}a_{\rm lat}^2$ |
|---|---|---|---|---|---|
| 3 | $8.5\times10^{-6}$ | 0.98 | 1.0 | 116 | $5.8\times10^{-4}$ |
| 4 | $1.4\times10^{-7}$ | 7.7 | 0.51 | $1.2\times10^{3}$ | $4.2\times10^{-5}$ |
| 5 | $1.8\times10^{-9}$ | 67 | 0.25 | $1.3\times10^{4}$ | $3.1\times10^{-6}$ |
| 6 | $2.2\times10^{-11}$ | 613 | 0.12 | $1.5\times10^{5}$ | $2.3\times10^{-7}$ |

The factor $8\sqrt2\pi^3\simeq351$ in $N_D$ means that the controlled regime begins only around β ≈ 4–5, where the Debye length is $10^3$–$10^4$ lattice spacings, in agreement with the ordering of scales in Week 9 §2.5. The formulas of §§3–6 are thus controlled at weak coupling, to leading order in $(\zeta/e^6)^{1/2}$; they are not claimed for β ≲ 3, where the scales are not ordered, nor at strong coupling, where the gas is dense. That compact QED₃ confines at every coupling is a theorem of Göpfert and Mack for the Villain action [Stated — refs.]; at strong coupling the character expansion of Week 6 already shows it. Figure 3 collects the scales.

```
   S_mono = 2π²G₃(0)β = 4.99 β                    monopole action (Week 8)
        │   ζ = e^(−S_mono)/a_lat³
        ▼
   ζ/e⁶ = β³ e^(−4.99β)  ≪ 1  (at β ≫ 1)          the one small parameter
        │   m_γ² = ζ/K = 8π²ζ/e²
        ▼
   m_γ = 2π√(2ζ)/e                                photon mass = Debye mass = inverse wall thickness
        │   σ_str = 16K m_γ = (2/π²) e² m_γ
        ▼
   σ_str                                          string tension;  σ_str/m_γ² = 8 N_D ≫ 1

   lengths:  a_lat  ≪  ℓ_B = π/e²  ≪  r̄ = (2ζ)^(−1/3)  ≪  m_γ⁻¹  ≪  R
   ratios:   ℓ_B/a_lat = πβ ;   ℓ_B/r̄ ∝ (ζ/e⁶)^(1/3) ;   r̄ m_γ ∝ (ζ/e⁶)^(1/6) ;   N_D = 2K/m_γ ∝ (ζ/e⁶)^(−1/2)
```
**Figure 3. The scales of Polyakov's mechanism: on the weak-coupling branch every ratio of couplings is a power of $\zeta/e^6$, and every ordering of lengths used in §§3–6 holds when it is small.**

## 8. Subtleties and fine print

**F1 — The fugacity and its prefactor.** In the Villain theory the weight $e^{-S_{\rm mono}}$ of a monopole is exact: photon and monopoles decouple and there is no fluctuation determinant (Week 8 §4.4). The only scheme choice is the scale at which vertex operators are normal-ordered; in three dimensions the self-contraction $\langle\sigma^2\rangle$ is finite, so a change of scale rescales ζ by a finite factor and changes none of the results, which depend on ζ alone (Week 9 F6 keeps the monopole action in exactly one place). For the Wilson action the dual weights are not Gaussian and the monopoles interact with the photon at short distances (Week 8 F5), which changes the core action and multiplies ζ by a β-dependent prefactor. In Polyakov's continuum realization, the Georgi–Glashow model, the monopole-instanton is a smooth solution of action $S_0$, and ζ is $e^{-S_0}$ times a one-loop factor, the fluctuation determinant around the instanton together with the Jacobian of its collective coordinates [Stated — refs: Polyakov 1977; *Gauge Fields and Strings*, ch. 4]. Every formula of this note holds with the corresponding ζ.

**F2 — The width of the string.** The width is $m_\gamma^{-1}$ up to the factors of §5.2. In the Hamiltonian picture the Euclidean wall is the world-sheet of the flux tube; on a static configuration $|E|=\frac{e^2}{2\pi}|\nabla\sigma|$, the $i$ of $B_\mu=\frac{ie^2}{2\pi}\partial_\mu\sigma$ disappearing in real time, so the electric field along a straight string at $y=0$ is $E(y)=\frac{e^2m_\gamma}{\pi}\,{\rm sech}(m_\gamma y)$. It carries one unit of flux, $\int E\,dy=e^2$, and its energy $\int\frac{E^2}{2e^2}dy=e^2m_\gamma/\pi^2$ is half the tension; the other half is the free energy of the polarized plasma. Beyond the classical profile the wall fluctuates as a membrane of tension $\sigma_{\rm str}$, and capillary waves broaden it as $\langle h^2\rangle\simeq\frac{1}{2\pi\sigma_{\rm str}}\ln(m_\gamma R)$ [Heuristic.]; this exceeds the intrinsic width squared only when $\ln(m_\gamma R)\gtrsim2\pi\sigma_{\rm str}/m_\gamma^2=16\pi N_D$, that is, for no loop of practical size.

**F3 — Why there is no $N$-ality in $U(1)$.** The electric 1-form symmetry of pure compact QED is $U(1)^{(1)}$, exact because there are no dynamical charges, and a Wilson loop of charge $q$ carries the charge $q\in\mathbb{Z}$. A string can break only by ending on dynamical charges, which would break the 1-form symmetry explicitly ([[courses/generalized-symmetries-course/conventions|conventions]] §6, the SSB criterion and its presupposition). The monopoles are magnetic: they screen magnetic charge (§3.2) and cannot end electric flux. So every $q\ne0$ has $\sigma_{{\rm str},q}=|q|\sigma_{\rm str}>0$, with no saturation and no breaking. In $SU(N)$ the 1-form symmetry is the center $\mathbb{Z}_N$, only the $N$-ality is conserved, and adjoint strings break by gluon pair creation ([[week-06-wilson-action-strong-coupling|Week 6]]). In the Georgi–Glashow model the W bosons carry twice the charge of a fundamental quark, which leaves only $\mathbb{Z}_2^{(1)}$ and lets even-charge strings break (Problem 3). A charge-$q$ problem in pure compact QED₃ that asks for saturation by plasma screening therefore rests on a false premise.

**F4 — Finite temperature and deconfinement** [Controlled to leading order in the monopole fugacity.]. At temperature $T$ the Euclidean time is a circle of length $1/T$. For the static mode $a_0$ the Polyakov loop is $P=e^{i\theta}$ with $\theta=a_0/T$, compact because large gauge transformations shift $a_0$ by $2\pi T$, and the Maxwell action reduces to
$$
\frac1{2e^2}\int_0^{1/T}\!d\tau\int d^2x\,(\partial_ia_0)^2=\frac{T}{2e^2}\int d^2x\,(\partial_i\theta)^2,\qquad \beta_{XY}=\frac{T}{e^2},
$$
a two-dimensional XY model in the normalization of [[week-04-bkt-kramers-wannier-disorder|Week 4]]. Its vortices are the monopoles: if θ winds by $2\pi$ around a point $x_0$, the flux through the torus formed by a small circle around $x_0$ and the thermal circle is $2\pi$, so a monopole sits inside. By the BKT criterion $\pi\beta_R=2$, with $\beta_R\simeq\beta_{XY}$ at small fugacity,
$$
T_c=\frac{2e^2}{\pi},
$$
the value previewed in Week 9 F4. Below $T_c$ the monopoles are free, the Polyakov-loop correlator decays exponentially and charges are confined; above it they bind into pairs, $\langle P(x)P^\dagger(0)\rangle\propto|x|^{-e^2/2\pi T}$, and the potential is the logarithm $\frac{e^2}{2\pi}\ln r$, with $\eta=1/4$ at $T_c$. The reduction is consistent, since $T_c\gg m_\gamma$: the thermal circle is short on the Debye length. The dual-photon route (Problem 5⋆) gives the same $T_c$; with the Coulomb coefficient halved it gives $4e^2/\pi$. The BKT character of the transition is the Svetitsky–Yaffe expectation for a $U(1)$ center in two dimensions [Stated — refs.]. Spatial Wilson loops keep an area law above $T_c$, with tension $e^2T/2$ from the two-dimensional Maxwell theory of $a_i$, so deconfinement is defined by the Polyakov loop.

**F5 — The torus.** On the $L^3$ torus the boxed formula of §4.2 is exact, sectors included. The harmonic part $h_\Sigma$ contributes $\frac{q^2}{2\beta}\sum_\mu A_\mu^2/L^3$, and the flux sectors $w\ne0$, weighted by $e^{-L|w|^2/2\beta}$ (Week 8 F4), couple to the loop through the cross term $\frac{q}{\beta}\sum_\mu w_\mu A_\mu/L$. Both vanish as $L\to\infty$ at fixed $C$, which is the order of limits used in §4.4; a loop comparable to the torus sees the flux sectors.

**F6 — What is universal.** The ratio $\sigma_{\rm str}/Km_\gamma=16$ belongs to the pure cosine. A second harmonic, from doubly charged monopoles, changes it at first order (Problem 4⋆), and so does any change of the monopole core. What survives within the dilute regime is the structure: the area law, the width $\propto m_\gamma^{-1}$, and the additivity $\sigma_{{\rm str},q}=|q|\sigma_{\rm str}$, which holds for any $2\pi$-periodic $U$ with one vacuum per period because $\mathcal W(2\pi q)=q\mathcal W(2\pi)$.

**F7 — Which continuum limit.** At fixed $e^2$, $a_{\rm lat}\to0$ is $\beta\to\infty$, where $\zeta/e^6\to0$ and $m_\gamma/e^2\to0$ faster than any power: the continuum theory at fixed $e^2$ is free Maxwell theory, and confinement sets in only at distances $m_\gamma^{-1}$ that recede to infinity. Göpfert and Mack take instead $a_{\rm lat}\to0$ at fixed $m_D$, and show that the limit is a free scalar of mass $m_D$ with string tension divergent in units of $m_D^2$ [Stated — refs.]; in our variables $N_D\to\infty$ and $\sigma_{\rm str}/m_\gamma^2=8N_D$. Their notation translates as follows: their β is $4\pi^2/g^2=1/2K$ (their eq. (1.3)), their $m_D$ (eq. (1.8a)) is our $m_\gamma$ with $\zeta=e^{-4.99\beta}/a_{\rm lat}^3$, and the classical approximation they quote, $8m_D/\beta_{\rm GM}=2e^2m_D/\pi^2$, is our $16Km_\gamma$. Their Theorem 1 bounds the tension from below by a constant times $m_D/\beta_{\rm GM}$ at weak coupling, with the constant undetermined, and their Corollary 2 extends positivity to every coupling by monotonicity in β.

## 9. Common misconceptions

- **"Confinement in compact QED₃ is a strong-coupling effect."** It is tempting because the only area law derived before this week is the strong-coupling one of Week 6, and because a plasma sounds like a disordered, strongly fluctuating system. Polyakov's result is a weak-coupling statement, controlled on the branch $\beta\gg1$ by $\zeta/e^6=\beta^3e^{-4.99\beta}\to0$ (§7): the plasma is dilute and weakly coupled, $N_D\gg1$, and the tension is exponentially small in $1/e^2a_{\rm lat}$ and nonzero. At strong coupling the theory also confines, for a different reason (Week 6), and the Göpfert–Mack theorem connects the two regimes.
- **"The area law depends on the choice of spanning surface."** It is tempting because the lattice formulas carry an explicit Σ and because the wall is drawn on a surface. $\langle W\rangle$ is exactly independent of Σ, by the compactness of σ and the integrality of the monopole charges (§6.2); Σ carries only a literal jump that is a relabelling, and the wall settles on the minimal surface (§5.5, item 3).
- **"The plasma screens the probes, so the tension of a charge-$q$ loop saturates and long strings break."** It is tempting because the plasma does screen (§3.2) and because adjoint strings break in $SU(N)$. The plasma screens magnetic charge; electric flux can end only on electric charges, which pure compact QED₃ lacks, and $\sigma_{{\rm str},q}=|q|\sigma_{\rm str}$ at every distance (§6.1, F3).
- **"A Wilson loop is a source of the dual photon, and its tension is the cost of a $2\pi$ jump of σ across a surface."** It is tempting because in the original variables a charge is a source, and the jump is what the lattice formula displays. In the dual variables the charge is a vortex line (§4.3); the literal jump costs nothing in the cosine and is a relabelling, and the tension is the cost of unwinding the vortex on the length $m_\gamma^{-1}$ (§5.1).

## 10. Historical note

Polyakov's letter of 1975 contains the whole mechanism in three pages. For compact abelian gauge theory on a three-dimensional lattice he identified the monopoles as the relevant classical configurations, treated their gas as a plasma at "temperature" $g^2$ by Debye's method at small $g^2$, found a photon mass exponentially small in $1/g^2$ in lattice units, and obtained an area law for planar Wilson contours, which he read, following Wilson, as charge confinement. In four dimensions he showed that the monopoles form closed rings with only dipole forces, found a perimeter law at small $g^2$, and concluded that a phase transition must separate this regime from Wilson's strong-coupling confinement. The 1977 paper in *Nuclear Physics B* gives the full account, including the Georgi–Glashow model in 2+1 dimensions, where the monopoles are smooth instantons, and then turns to the pseudoparticles of four-dimensional Yang–Mills theory; there the suggestion that a similar mechanism confines was an argument without a controlled calculation, and it has remained one. Wilson (1974) had derived the area law at strong coupling for every compact lattice gauge theory, and Osterwalder and Seiler (1978) made it rigorous by proving the strong-coupling expansion convergent; what Polyakov added was a controlled derivation at weak coupling, in the regime connected to the continuum. Göpfert and Mack (1982) then proved, for the Villain action, that the tension is positive at every coupling, with a weak-coupling lower bound of the form found here and an undetermined constant, and they noted that the classical approximation gives the constant of §5.3 (F7).

## 11. What to take away

1. **The plasma gaps the photon.** $m_\gamma^2=\zeta/K=8\pi^2\zeta/e^2$ comes out of the curvature of the cosine and out of Debye–Hückel, because the sine-Gordon saddle is the Poisson–Boltzmann equation of the plasma. Physically, the explicit breaking of the magnetic $U(1)^{(0)}$ gives its would-be Goldstone boson a mass.
2. **A Wilson loop is a vortex line of σ.** Exactly: Move 3 gives $\delta b=-qJ_C$, and the dual Villain integer acquires $d\tilde n=-q\star J_C$. Seen from the monopoles, the loop is the phase $e^{-iqq_i\Omega_C/2}$, the Aharonov–Bohm phase of their flux, and in the plasma $\cos\sigma$ becomes $\cos(\sigma-q\eta_C)$.
3. **The tension is the cost of unwinding.** The kink $4\arctan e^{m_\gamma\xi}$ saturates the Bogomolny bound, and $\sigma_{\rm str}=16\sqrt{K\zeta}=(2/\pi^2)\,e^2m_\gamma$. The literal jump on Σ costs nothing in the cosine and is a relabelling; $\langle W\rangle$ depends on $C$ alone, and the wall sits on the minimal surface.
4. **Charges add.** $\sigma_{{\rm str},q}=|q|\sigma_{\rm str}$, with no saturation and no string breaking, because the electric $U(1)^{(1)}$ is exact and the plasma is magnetic.
5. **The control is one number.** Every step is exact or, on the weak-coupling branch, controlled by $\zeta/e^6$ through $N_D=2K/m_\gamma\gg1$; the window opens around β ≈ 4–5, and confinement at every coupling is the Göpfert–Mack theorem.

## 12. Looking ahead: Week 11

In three dimensions the monopoles are points of spacetime, instantons whose plasma exists at every weak coupling and confines. In four dimensions they are worldlines, the closed loops $j=\star dn$ of Week 8 §5, and Polyakov's letter already found that at small coupling they leave the photon massless. [[week-11-monopole-condensation-4d|Week 11]] asks when these loops proliferate, finds the energy–entropy competition that separates a Coulomb phase from a confining one, meets the 't Hooft loop as the four-dimensional disorder operator and the [[dual-superconductor]] in its original setting, and introduces the [[julia-toulouse-mechanism|Julia–Toulouse mechanism]], the rank-changing condensation on which the research line of the course is built.

## 13. Problem set

Problems 1–3 are the classroom core and use only §§3–6 and F3; Problems 4⋆ and 5⋆ are self-study consolidation, solvable from the note, each with a hint; Problem 6⋆⋆ is a research extension and states what is known, what is explored and what counts as completion. The mass gap, the kink and its tension, and surface independence are derived in the text and are not set again.

**Core problems** (everyone).

**1. Unscreened monopoles give a volume law** (extends §4.4). Treat the monopoles as independent by keeping the first order in ζ of the plasma form of §4.5.
(a) Show that $\ln\langle W_q(C)\rangle=-\frac{q^2e^2}2\oint\oint\frac{dl\cdot dl'}{4\pi|l-l'|}-2\zeta\int d^3x\,\big[1-\cos q\eta_C(x)\big]+O(\zeta^2)$, and explain why a term of first order in ζ exists in three dimensions although the lattice gas is neutral.
(b) For a circle of radius $R$ show that the integral equals $c(q)R^3$ with $c(q)$ finite, using $\Omega_C\simeq\pi R^2\cos\theta/r^2$ at large distance.
(c) Numerical quadrature gives $c(1)\simeq10.34$ and $c(2)\simeq26.38$. Compare with the area law of §5.4 and find the radius at which the two forms cross.
(d) Explain in two sentences why screening turns the volume law into an area law, and why the $q$-dependence in (a) is not linear while that of §6.1 is.
(*Hint:* in the Gaussian theory with normal-ordered vertex operators, $\langle{:}e^{\pm i(\sigma-q\eta)}{:}\rangle=e^{\mp iq\eta}$.)

**2. The wall between two loops** (extends §§5.3 and 6.1). Take two coaxial planar loops $C_1$ and $C_2$ of the same large area $A$, in parallel planes at distance $d$, with $m_\gamma^{-1}\ll d\ll\sqrt A$.
(a) For equal orientations σ winds by $4\pi$ along the common axis; for opposite orientations (the product $W(C_1)W(C_2)^\dagger$) it returns to its initial vacuum. Write the two superposition profiles built from the unit kink and compute their action per unit area to leading order in $e^{-m_\gamma d}$.
(b) For equal orientations deduce $\ln\big[\langle W(C_1)W(C_2)\rangle/\langle W(C_1)\rangle\langle W(C_2)\rangle\big]$, and explain why its decay rate in $d$ is $m_\gamma$.
(c) Use the sign found in (a) to justify the statement of §6.1 that the two unit walls of a charge-2 loop separate.
(d) Test the claim that the opposite-orientation pair has $\ln\big[\langle W(C_1)W(C_2)^\dagger\rangle/\langle W(C_1)\rangle\langle W(C_2)\rangle\big]=+4\sigma_{\rm str}A\,e^{-m_\gamma d}$: is the configuration of two flat walls the saddle when $m_\gamma^{-1}\ll d\ll\sqrt A$?
(*Hint:* the kink tails are $4e^{m_\gamma\xi}$ and $2\pi-4e^{-m_\gamma\xi}$. Split the line at the midpoint, expand the action of each half to first order in the tail of the other kink, and integrate by parts with the equation of motion; only boundary terms at the midpoint survive.)

**3. Charge-2 probes, done correctly** (extends §6.1 and F3). Add to compact QED₃ a dynamical field of electric charge 2 and mass $M$, heavy on the scale $e^2$; in the Georgi–Glashow model of Polyakov (1977) the W bosons carry twice the charge of a fundamental quark.
(a) Which subgroup of the electric $U(1)^{(1)}$ survives, and which Wilson loops remain charged under it? Use [[courses/generalized-symmetries-course/conventions|conventions]] §6.
(b) For static charges $\pm2$ at distance $R$, compare the energy of the string with that of the configuration in which a dynamical pair screens them, and estimate the breaking distance.
(c) Give the asymptotic tensions of $W_1$, $W_2$ and $W_3$.
(d) Say why none of (a)–(c) happens in pure compact QED₃, and why the monopole plasma does not change that conclusion.

**Starred problems.**

**4⋆. A second harmonic and the first correction to the tension** (extends §5.3 and F6). Suppose the plasma also contains monopoles of charge ±2 with fugacity $\zeta_2$, $|\zeta_2|\ll\zeta$, so that $U(\sigma)=2\zeta(1-\cos\sigma)+2\zeta_2(1-\cos2\sigma)$.
(a) Show that the Bogomolny construction of §5.3 applies unchanged while the vacua stay at $2\pi\mathbb{Z}$, and that $\sigma_{\rm str}=16\sqrt{K\zeta}\,\big[1+\frac23\,\zeta_2/\zeta+O(\zeta_2^2/\zeta^2)\big]$.
(b) Show that $m_\gamma^2=(\zeta+4\zeta_2)/K$ and that $\sigma_{\rm str}/16Km_\gamma=1-\frac43\,\zeta_2/\zeta+\dots$, so that the ratio of §5.3 is not universal.
(c) Estimate $\zeta_2/\zeta$ for the Villain gas, where a doubly charged monopole on one dual site has action $4S_{\rm mono}$, and compare the correction with the loop corrections of §7.
(*Hint:* expand $\sqrt U$ to first order in $\zeta_2$, with $1-\cos2\sigma=4\sin^2\frac\sigma2\cos^2\frac\sigma2$.)

**5⋆. Deconfinement from the dual photon** (extends F4).
(a) Show that at temperature $T$ the monopole pair interaction at separations $r\gg1/T$ becomes $-\frac{2\pi T}{e^2}q_iq_j\ln r+{\rm const}$.
(b) Identify the resulting two-dimensional gas with the vortex gas of an XY model at $\beta_{XY}=T/e^2$, and check this against the reduction $K/T=1/(8\pi^2\beta_{XY})$ of the sine-Gordon action and the dictionary of [[courses/generalized-symmetries-course/conventions|conventions]] §5.
(c) Show that the coefficient $2\pi^2/e^2$ for $i<j$ would give $T_c=4e^2/\pi$.
(d) Compute the exponent $\eta(T)$ of the Polyakov-loop correlator above $T_c$ and its value at $T_c$, and show that spatial Wilson loops obey an area law with tension $e^2T/2$ above $T_c$ even without monopoles.
(*Hint:* periodize $G$ in Euclidean time; the zero Matsubara mode gives $T\,G_2(r)$ with $G_2(r)=-\frac1{2\pi}\ln r+{\rm const}$. In (d) a spatial loop at high $T$ is a Wilson loop of the two-dimensional Maxwell theory of $a_i$ with coupling $e^2T$.)

**⋆⋆ problems** (research extension).

**6⋆⋆. Göpfert–Mack against the semiclassics.** *What is known:* Göpfert and Mack prove for the Villain action that the string tension is positive at every coupling and, at weak coupling, bounded below by a constant times $m_D/\beta_{\rm GM}$ with the constant undetermined, while the classical approximation to their effective action gives the constant 8, which is §5.3 (F7). *What is explored:* which steps of the chain of §7 their proof controls and which it bypasses, and whether the constant can be pinned. *Completion:* (i) a dictionary between their notation (their β, the $\mathbb{Z}$-ferromagnet, $m_D$, their effective action) and this note's ($K$, ζ, $m_\gamma$, $\sigma_{\rm str}$), with $\beta_{\rm GM}=1/2K$, $m_D=m_\gamma$ and $8m_D/\beta_{\rm GM}=16Km_\gamma$ checked; (ii) a one-page account of how the statement at every coupling follows from their Theorem 1 and the monotonicity of the tension in β, and of what their continuum limit at fixed $m_D$ means for $N_D$; (iii) a clearly labelled heuristic assessment of whether 8 is the true asymptotic constant. *Sources:* Göpfert–Mack (1982), §1 and the sections containing Theorems 1 and 4; Week 9 §§4 and 6.2; §7 of this note.

## Self-study answer checkpoints

These checkpoints cover the core problems; starred and ⋆⋆ problems remain source-led.

1. (a) The decisive step is the expansion of $\mathcal Z[q\eta_C]/\mathcal Z[0]=\big\langle\exp\big(2\zeta\int[\cos(\sigma-q\eta_C)-\cos\sigma]\big)\big\rangle$ to first order, with $\langle{:}\cos(\sigma-q\eta_C){:}\rangle=\cos q\eta_C$, which gives $-2\zeta\int(1-\cos q\eta_C)$. A first-order term exists because an isolated monopole has finite action in three dimensions ($G_3(0)$ is finite), so neutrality is a global constraint that costs nothing locally in infinite volume. (b) At large $r$, $1-\cos(q\Omega_C/2)\simeq q^2\Omega_C^2/8\propto r^{-4}$, which is integrable, and scaling $x=Ru$ gives $c(q)R^3$: a volume law. (c) $2\zeta c(q)R^3=|q|\sigma_{\rm str}\pi R^2$ at $R_\times=8\pi|q|/(c(q)\,m_\gamma)$, that is, $R_\times\simeq2.43/m_\gamma$ for $q=1$ and $1.91/m_\gamma$ for $q=2$: the independent-monopole form holds for $R\ll m_\gamma^{-1}$ and the area law for $R\gg m_\gamma^{-1}$. (d) The screening cloud cancels a monopole's flux beyond $m_\gamma^{-1}$, so only monopoles within $m_\gamma^{-1}$ of the wall count, giving $\zeta A/m_\gamma\propto\sqrt{K\zeta}A$; the first-order phase average $1-\cos q\eta$ is not linear in $q$ ($c(2)/c(1)\simeq2.55$), while the wall tension is fixed by the winding $2\pi q$ and is additive. A common failure is to impose neutrality pair by pair and conclude that there is no term of order ζ.
2. (a) Same orientation: $\sigma=\sigma_{\rm k}(\xi)+\sigma_{\rm k}(\xi-d)$; opposite: $\sigma=\sigma_{\rm k}(\xi)-\sigma_{\rm k}(\xi-d)$, with $\sigma_{\rm k}=4\arctan e^{m_\gamma\xi}$. The tail overlap gives the action per unit area $2\sigma_{\rm str}\pm4\sigma_{\rm str}e^{-m_\gamma d}$, with $4\sigma_{\rm str}=64Km_\gamma=(8/\pi^2)\,e^2m_\gamma$, plus for equal orientations and minus for opposite ones (the superposition ansatz gives 0.9992 and $-1.0008$ times this at $m_\gamma d=10$). (b) $\ln[\cdots]=-4\sigma_{\rm str}A\,e^{-m_\gamma d}$; the connected loop–loop correlator decays as $e^{-m_\gamma d}$ because the lightest excitation that couples to the loops is the massive dual photon. (c) Two walls of the same orientation repel, so the charge-2 wall splits into two unit walls that move apart until the pinning at $C$ stops them. (d) Kink and antikink attract, and the wall lowers its action by becoming the tube that joins $C_1$ to $C_2$, of area $\simeq Pd\ll2A$ with $P$ the perimeter of the loops. Then $\langle W(C_1)W(C_2)^\dagger\rangle\simeq\exp[-\sigma_{\rm str}Pd+O(P)]$ and $\ln[\cdots]\simeq\sigma_{\rm str}(2A-Pd)$, positive and of order $A$, far above $4\sigma_{\rm str}A\,e^{-m_\gamma d}$, so the two flat walls are not the saddle for $m_\gamma^{-1}\ll d\ll\sqrt A$. Comparing the actions $\sigma_{\rm str}Pd$ and $2\sigma_{\rm str}A$ of the two trial configurations puts the crossover at $d\simeq2A/P$, which is $R$ for circles of radius $R$; the tube dominates below it, and the two disks with the attraction of (a) above it [Heuristic]. A common failure is to superpose two kinks with the same sign for opposite orientations, to evaluate the overlap at the cores instead of the tails, or to accept the two flat walls in (d) without comparing them with the tube.
3. (a) Charge-2 matter lets Wilson lines of even charge end, which leaves $\mathbb{Z}_2^{(1)}$, acting on $W_q$ by $(-1)^q$; loops of odd charge remain charged. (b) The string costs $2\sigma_{\rm str}R$ and a screening pair $2M$, so it breaks at $R_{\rm b}\simeq M/\sigma_{\rm str}$ [Heuristic]. (c) For $R\to\infty$: $W_1$ keeps $\sigma_{\rm str}$; $W_2$ goes over to a perimeter law; $W_3$ breaks to charge 1 and keeps $\sigma_{\rm str}$. (d) Without charged matter the electric $U(1)^{(1)}$ is exact and nothing can end the flux; the monopoles are magnetic and screen only magnetic charge, so $\sigma_{{\rm str},q}=|q|\sigma_{\rm str}$ at every $R$. A common failure is to attribute the breaking in (b) to the monopole plasma, or to use $N$-ality language for $U(1)$ without matter.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block C. Rewritten to the note-quality-template standard on 2026-09-28 (first draft 2026-07-01). Last revised 2026-09-29.*
