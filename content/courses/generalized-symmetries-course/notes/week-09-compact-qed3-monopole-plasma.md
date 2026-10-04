---
title: "Week 9 — Compact QED₃ I: the Monopole Plasma"
type: lecture-notes
course: syllabus
semester: 1
week: 9
block: C
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 1–8; the three-dimensional duality and its monopole Coulomb gas (Week 8 §4); the sine-Gordon face of the XY duality (Week 3 §6); 3d electrostatics
modified: 2026-09-29
---

# Week 9 — Compact QED₃ I: the Monopole Plasma

> *[[week-08-dual-variables-abelian-gauge|Week 8]] rewrote compact QED in three dimensions, exactly, as a free dual photon and a Coulomb gas of monopoles sitting on the dual sites. This week we treat that gas as a plasma. We organize the monopole configurations into a dilute instanton gas and say precisely when it is dilute, with three ordered length scales and one small parameter, $\zeta/e^6$; we rewrite the gas as a sine-Gordon theory of the dual photon to second order in the fugacity; and we compute Debye screening on the gas side, $m_D^2=8\pi^2\zeta/e^2$. The dual photon carries the magnetic symmetry of three-dimensional Maxwell theory, a 0-form $U(1)$ whose charged operators are the local monopole operators $e^{i\sigma}$. Without monopoles the photon is the Goldstone boson of its spontaneous breaking; with them the symmetry is broken explicitly, at every coupling. [[week-10-polyakov-mass-gap-area-law|Week 10]] turns the screening into Polyakov's area law.*

### How to use this chapter

- **In class:** derive at the board, in this order, the flux jump that makes a monopole an instanton (§2.2, Figure 1) and the core estimate $r_0=0.315\,a_{\rm lat}$ (§2.3); the five steps from Week 8's exact gas to the grand-canonical Coulomb gas with pair coefficient $4\pi^2/e^2$ (§2.4); the three scales and their ratios (§2.5, Figure 2); the vertex normalization and the $O(\zeta^2)$ match (§§3.1–3.2); and Debye–Hückel with $m_D^2=8\pi^2\zeta/e^2$ (§4). In the second lecture: the magnetic 0-form symmetry, its local charged operators and the flux check (§5.1), its spontaneous breaking without monopoles (§5.2), the Ward identity with its contact term (§5.3), and the energy–entropy argument with Figure 3 (§6.1). The core Problems 1–3 extend §4, §§5.2–5.3 and §§3 and 5.
- **For self-study:** the continuum derivation of the dual photon (§2.1), what changes in three dimensions, including the dielectric renormalization of $e^2$ (§3.3), the rigorous statements (§6.2) and the fine print of §7. The one calculation to do alone is Table 1: recompute its $\beta=4$ row from $S_{\rm mono}=4.9887\,\beta$ and the definitions of §2.5, and check $\lambda_D/\bar r=2^{5/6}e/4\pi\zeta^{1/6}$ on the numbers.
- **Instructor checkpoint:** two errors recur at the board. The pair coefficient is $4\pi^2/e^2$ summed over unordered pairs, equivalently $2\pi^2/e^2$ over ordered ones; with half of it Debye–Hückel gives $m_D^2=4\pi^2\zeta/e^2$ and the comparison with the sine-Gordon mass in Week 10 fails (§§2.4, 4). And the magnetic symmetry of three-dimensional Maxwell theory is a 0-form $U(1)$ whose charged objects are the local operators $e^{iq\sigma(x)}$; a 1-form symmetry acting on 't Hooft lines is the four-dimensional statement of the same $(d-3)$-form rule (§5.1, Table 2).

## 0. Reading

**Primary:** Polyakov, *Phys. Lett. B* 59 (1975) 82, three pages: the three-dimensional part, where the Wilson loop is reduced to the free energy of a monopole plasma in the external field of the loop and the plasma is treated by the Debye method. Polyakov, *Nucl. Phys. B* 120 (1977) 429, the section on 2+1 dimensions, which Week 10 follows.

**Secondary:**
- Göpfert & Mack, *Commun. Math. Phys.* 82 (1982) 545, §1: the statement of results (Theorem 1, Corollary 2 and eq. (1.8)), readable without the proofs.
- Kogut, *Rev. Mod. Phys.* 51 (1979) 659, §VI; Savit, *Rev. Mod. Phys.* 52 (1980) 453, the sections on the $U(1)$ theories.
- Polyakov, *Gauge Fields and Strings* (1987), ch. 4.

**Optional research reading:** Grigorio, Guimaraes, Wotzasek, *Phys. Lett. B* 674 (2009) 213 [arXiv:0808.3698], monopoles in the presence of a Chern–Simons term in the Julia–Toulouse approach (Problem 6⋆⋆); Fröhlich & Spencer, *Commun. Math. Phys.* 81 (1981) 527, the rigorous two-dimensional Coulomb gas, for the contrast drawn in §6.

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]]. Signs and normalizations: [[courses/generalized-symmetries-course/conventions|conventions]] §§2–6. The exact duality used throughout is [[week-08-dual-variables-abelian-gauge|Week 8]] §4, cited by section and not rederived.

## 1. The question

Consider first the theory with the monopoles removed. In the dual variables of Week 8 it is the term $v=0$ of the exact identity of Week 8 §6, a free compact scalar with no sources; on the direct side it is the Villain theory with the constraint $dn=0$ (the modified Villain theory of Semester II Week 12). Its photon has a single polarization in three dimensions, carried by σ, and it is massless. Its static potential is the one computed in Week 8 Problem 1: two opposite unit charges at separation $R\gg a_{\rm lat}$ feel
$$
V(R)=\frac{e^2}{2\pi}\ln\frac{R}{a_{\rm lat}}+e^2\kappa ,
$$
where $\kappa=0.257343$ is the lattice constant of [[courses/generalized-symmetries-course/conventions|conventions]] §2. The potential grows without bound, so even the monopole-free theory confines static charges, logarithmically; this is the marginal case of the higher-form Coleman–Mermin–Wagner statement of [[courses/generalized-symmetries-course/conventions|conventions]] §6, by which the electric 1-form symmetry cannot break in $d=3$. What the monopole-free theory does have is a massless photon, and we call a phase with a massless photon a Coulomb phase.

The compact theory adds the monopoles. In three Euclidean dimensions a monopole is localized in time as well as in space, an instanton (§2.2), and Week 8 wrote the complete theory as the free dual photon times an exact neutral Coulomb gas of these instantons. The question of the week is what that gas does. If the monopoles stayed bound in neutral pairs at some coupling, the long-distance physics there would be that of the monopole-free theory, a Coulomb phase. If they form a plasma, the plasma screens, the photon acquires a mass, and Week 10 shows that the logarithm becomes a linear potential. In four dimensions both possibilities occur, at different couplings ([[week-11-monopole-condensation-4d|Week 11]]). In three dimensions only the plasma occurs, and the reason is subtler than the counting argument usually given for it (§6).

The units are fixed once. The gauge coupling $e^2$ has mass dimension one and $\beta=1/(e^2a_{\rm lat})$ is dimensionless; σ is dimensionless; the fugacity ζ is a number of monopoles per unit Euclidean volume, of mass dimension three. The continuum description has only these two dimensionful parameters, so every dimensionless property of the plasma is a function of the single combination $\zeta/e^6$, which on the lattice is $\beta^3e^{-S_{\rm mono}}=\beta^3e^{-4.99\beta}$.

## 2. From the exact gas to a dilute instanton gas

### 2.1 What Week 8 proved, and the dual photon in continuum form [Computed.]

We take from Week 8 two exact identities for the Villain theory ([[villain-action]]) on the periodic lattice. In the sector without electric flux windings ($w=0$; the other sectors are torus effects, Week 8 F4) the partition function is a free dual photon times a neutral Coulomb gas (Week 8 §4.4),
$$
Z^{(0)}=(2\pi\beta)^{-N_P/2}\,Z_{\rm ph}\sum_{\substack{v\in C^0(\Lambda^*,\mathbb{Z})\\ \sum v=0}}e^{-2\pi^2\beta\langle v,G'v\rangle},
$$
where $v_{c^*}=m_c=(dn)_c$ is the monopole number of the cube $c$ placed at the dual site $c^*$ at its center (Week 8 §4.3), $G'$ is the Green function of the dual lattice and $Z_{\rm ph}$ is the free dual-photon partition function. Before the Gaussian integral is done, the same identity reads (Week 8 §4.5)
$$
Z^{(0)}=\frac{(2\pi\beta)^{-N_P/2}}{(2\pi)^{N^*}}\sum_{v\in C^0(\Lambda^*,\mathbb{Z})}\ \int_{\mathbb{R}^{N^*}/2\pi\mathbb{Z}}d^{N^*}\sigma\ \exp\Big(-\frac{1}{8\pi^2\beta}\|d\sigma\|^2-i\langle v,\sigma\rangle\Big),
$$
where the dual photon σ couples to the monopoles as the sources $e^{-im_c\sigma(c^*)}$ and the integral over its zero mode enforces neutrality. Both are identities at every β. What they leave open is the statistical mechanics of the sum over $v$, which is the subject of this week.

The continuum reading of the second identity pins every normalization of [[courses/generalized-symmetries-course/conventions|conventions]] §5 in a few lines and shows where the periodicity of σ comes from (erratum E2). Write the Euclidean Maxwell action through $B_\mu=\frac12\epsilon_{\mu\nu\rho}F_{\nu\rho}$, with monopoles of integer charges $q_i$ at the points $x_i$, and impose the Bianchi identity with a multiplier,
$$
S=\int d^3x\,\Big[\frac{1}{2e^2}B^2+\frac{i}{2\pi}\,\sigma\,\big(\partial\cdot B-2\pi\rho_m\big)\Big],\qquad \rho_m(x)=\sum_iq_i\,\delta^3(x-x_i),
$$
where $\oint B\cdot dS=2\pi q$ is the flux of a charge $q$. The monopoles enter the weight as $e^{-S}\supset\exp\big(i\sum_iq_i\sigma(x_i)\big)$, the insertion $e^{iq\sigma}$ of [[courses/generalized-symmetries-course/conventions|conventions]] §5. Every $q_i$ is an integer, which is Dirac quantization $\oint F\in2\pi\mathbb{Z}$ (Week 8 §2.2), so the weight is invariant under $\sigma\to\sigma+2\pi$ and σ is an angle of period $2\pi$: a smaller period would forbid some of the allowed insertions, and a larger one would admit fractional magnetic charges, which integer electric charges exclude. Integrating by parts, the $B$-dependent terms are $\frac{1}{2e^2}B^2-\frac{i}{2\pi}B\cdot\partial\sigma$, stationary at
$$
B_\mu=\frac{ie^2}{2\pi}\,\partial_\mu\sigma ,
$$
and substituting back gives $\frac{1}{2e^2}\big(\frac{ie^2}{2\pi}\big)^2(\partial\sigma)^2-\frac{i}{2\pi}\cdot\frac{ie^2}{2\pi}(\partial\sigma)^2=\frac{e^2}{8\pi^2}(\partial\sigma)^2$. That is,
$$
S[\sigma]=\int d^3x\,\frac{e^2}{8\pi^2}(\partial\sigma)^2-i\sum_iq_i\,\sigma(x_i),\qquad \langle\sigma(x)\sigma(y)\rangle_0=\frac{4\pi^2}{e^2}\,G_3(x-y),
$$
where the covariance is the inverse of twice the stiffness and $G_3(x)=1/4\pi|x|$. This is the continuum limit of the lattice identity, in which $\frac{1}{8\pi^2\beta}\|d\sigma\|^2\to\frac{e^2}{8\pi^2}\int(\partial\sigma)^2$ (Week 8 §4.5) and the lattice covariance is $4\pi^2\beta\,G_3$ in lattice units. The lattice numbers $m_c$ are minus the magnetic charges, which is why they enter as $e^{-im_c\sigma}$ (F5).

### 2.2 The monopole is an instanton [Computed.]

On the lattice the statement is an identity. Let $S_\tau$ be the closed 2-chain of plaquettes spanned by the directions 1 and 2 at the time $x_3=\tau$ of the torus, oriented along $+\hat3$, and let $\Phi(\tau)=\sum_{P\in S_\tau}F_P$ be the flux of the Villain field strength $F=da-2\pi n$ through it. By Week 8 §2.2, $\Phi(\tau)=-2\pi\langle\mathbb{1}_{S_\tau},n\rangle\in2\pi\mathbb{Z}$. Two slices bound the slab $V$ of cubes between them, $S_{\tau_2}-S_{\tau_1}=\partial V$, so that
$$
\Phi(\tau_2)-\Phi(\tau_1)=\sum_{c\in V}(dF)(c)=-2\pi\sum_{c\in V}m_c=2\pi\sum_{c\in V}q_c ,
$$
where $q_c=-m_c$ is the magnetic charge of the cube. The total magnetic flux through space is quantized at every time and changes by $2\pi q$ exactly when the slice passes a monopole of charge $q$. In the continuum the field of the monopole is $B=q\,x/2|x|^3$ ([[courses/generalized-symmetries-course/conventions|conventions]] §5), and its flux through the plane $x_3=h$ is
$$
\int d^2x\,B_3=\frac{qh}{2}\int_0^\infty\frac{2\pi\rho\,d\rho}{(\rho^2+h^2)^{3/2}}=\pi q\,\operatorname{sgn}h ,
$$
so it jumps by $2\pi q$ as the slice crosses the event (Figure 1). Near the monopole the lattice field is fixed by symmetry: the six faces of the cube are equivalent, so each carries $2\pi q/6$, and this is the lattice Coulomb field $2\pi q\,[G_3(0)-G_3(\hat1)]$ on the dual link from the monopole to its neighbour, since $\Delta G_3=\delta$ gives $6G_3(0)-6G_3(\hat1)=1$.

```
                                  2πq/6
                                    ↑
                    +---------------+---------------+
                    |                               |
                    |                               |
        2πq/6  ←──  +               ⊕               +  ──→  2πq/6
                    |         dual site c*          |
                    |                               |
                    +---------------+---------------+
                                    ↓
                                  2πq/6
            (and 2πq/6 through each of the two faces parallel to the page)

    cube c of Λ in cross-section;  ⊕ : v = m_c = −q ;  Σ_{P∈∂c} F_P = −2π m_c = 2πq

    x₃ (Euclidean time)
     ↑   ─────────  slice above the event:  ∫ B₃ = +πq  ─────────
     |                       ⊕   the monopole at x₃ = 0
     |   ─────────  slice below the event:  ∫ B₃ = −πq  ─────────     jump: 2πq
```
**Figure 1. A monopole of charge $q$ is a flux-emitting dual site. The Villain field strength leaves the cube $c$ through its six faces, $2\pi q/6$ through each; far away the field is $B=q\,x/2|x|^3$, and the flux through a time slice jumps by $2\pi q$ as the slice crosses the event, which makes the monopole an instanton.**

In the Hamiltonian language of [[week-07-kogut-susskind-hamiltonian|Week 7]], with $x_3$ as time, the monopole is a tunnelling event. The flux through space is an integer multiple of $2\pi$ at each time, and a compact plaquette angle can change it by $2\pi$ only by passing through $\pm\pi$, over the maximum of its cosine potential; the one-plaquette tunnelling of Week 7 (§6.3 and its Problem 8⋆⋆) is the simplest instance. The Villain configurations with $dn\ne0$ are therefore the instanton sector of the theory, and the sum over $v$ is a gas of instantons.

> **Physical picture.** A simulation that recorded the flux through a spatial slice as a function of Euclidean time would see an integer, in units of $2\pi$, constant over long stretches and jumping by $\pm1$ at isolated events, at a rate of $2\zeta$ per unit spatial area and unit time at weak coupling. In the monopole-free theory it would never jump: the flux is the conserved charge of the magnetic symmetry (§5), and the instantons are the events that violate its conservation. The flux identity is exact on the lattice; the rate $2\zeta$ is the leading order of §2.4.

### 2.3 The monopole action: the lattice Coulomb estimate [Computed.]

Week 8 §4.4 derived the exact monopole action of the Villain theory, $S_{\rm mono}=2\pi^2G_3(0)\,\beta=4.99\,\beta$ with $G_3(0)=0.252731$, as the diagonal term of the Coulomb-gas exponent; there is no fluctuation determinant, because the photon and the monopoles decouple exactly. The continuum estimate shows what this number is. The Maxwell action of the Coulomb field outside a ball of radius $r_0$ is
$$
\frac{1}{2e^2}\int_{|x|>r_0}d^3x\,B^2=\frac{1}{2e^2}\int_{r_0}^\infty4\pi r^2\,dr\,\frac{q^2}{4r^4}=\frac{\pi q^2}{2e^2r_0}=\frac\pi2\,\frac{a_{\rm lat}}{r_0}\,q^2\beta ,
$$
which diverges as $r_0\to0$: in the continuum the monopole action is a pure short-distance quantity. Equating it with the lattice value $2\pi^2G_3(0)\,q^2\beta$ gives
$$
r_0=\frac{a_{\rm lat}}{4\pi G_3(0)}=0.315\,a_{\rm lat}.
$$
That is, the lattice replaces the divergent Coulomb self-energy by that of a charge smeared over a ball of about a third of a lattice spacing, and $G_3(0)=1/4\pi r_0$ is the lattice value of the Coulomb potential at zero separation. The same estimate places the action: the field beyond a distance $R$ carries the fraction $r_0/R$ of it, so more than two thirds of $S_{\rm mono}$ sit within one lattice spacing of the monopole, and a charge-$q$ monopole costs $q^2S_{\rm mono}$. Two consequences follow. The number 4.99 belongs to the Villain action; for the Wilson action the core differs, and only the long-distance Coulomb tail is common (Week 8 F5). And on a finite torus the zero mode lowers $G'(0)$, so small lattices see $S'_{\rm mono}=2\pi^2G'(0)\beta$, for instance $4.25\,\beta$ at $L=6$ (Week 8 F6).

### 2.4 The fugacity expansion, step by step [Controlled to leading order in $\zeta a_{\rm lat}^3=e^{-S_{\rm mono}}$.]

Each term of the sum over $v$ is the total Villain weight of the configurations with monopole numbers $m_c=v_{c^*}$ (Week 8 §4.3), so organizing the sum by occupied dual sites organizes the Villain configurations with $dn\ne0$ into an instanton gas. We go from the exact sum to the grand-canonical Coulomb gas in five steps and say at each step what is exact and what is dropped. The lattice is taken large enough that $G'\to G_3$ at fixed separations (Week 8 F6).

*Step 1 (exact).* Split the exponent into its diagonal and off-diagonal parts (Week 8, Move 7),
$$
e^{-2\pi^2\beta\langle v,G_3v\rangle}=\prod_{\tilde x}e^{-S_{\rm mono}v_{\tilde x}^2}\ \prod_{\{\tilde x,\tilde y\}}e^{-4\pi^2\beta\,v_{\tilde x}v_{\tilde y}\,G_3(\tilde x-\tilde y)},
$$
where the second product runs over unordered pairs of distinct dual sites.

*Step 2 (exact rewriting).* A configuration is a set of $N$ occupied sites with nonzero charges. Summing over ordered $N$-tuples of distinct sites and dividing by $N!$,
$$
\sum_{v:\ \sum v=0}=\sum_{N\ge0}\frac{1}{N!}\sum_{\substack{\tilde x_1,\dots,\tilde x_N\\ \text{distinct}}}\ \sum_{\substack{q_1,\dots,q_N\ne0\\ \sum_iq_i=0}},\qquad e^{-q^2S_{\rm mono}}=\big(\zeta a_{\rm lat}^3\big)^{q^2},
$$
so that a charge-$q$ monopole has the fugacity $\zeta_q=e^{-q^2S_{\rm mono}}/a_{\rm lat}^3$ per unit volume, and the pairs interact through $4\pi^2\beta\,q_iq_jG_3$, which in physical units is $\frac{4\pi^2}{e^2}q_iq_j\,G_3$ (Week 8 §4.4).

*Step 3 (truncation to unit charges).* We keep $q_i=\pm1$. A charge-2 site has the weight $(\zeta a^3)^4$, so the lightest neutral configuration that contains one, a $+2$ with two $-1$, enters at order $(\zeta a^3)^6$, against $(\zeta a^3)^2$ for the first pair; in the field theory of §3 it is the operator $2\zeta_2\cos2\sigma$ with $\zeta_2/\zeta=e^{-3S_{\rm mono}}$. In three dimensions this fugacity ratio is the only suppression (§3.3). With unit charges, the number of ways of choosing which $N_+$ of the $N$ labelled points carry $+1$ is $N!/N_+!N_-!$, so the combinatorial factor becomes $1/N_+!N_-!$ with $N_+=N_-$.

*Step 4 (continuum positions).* We replace $\sum_{\tilde x}\to\int d^3x/a_{\rm lat}^3$ and $4\pi^2\beta\,G_3(r/a_{\rm lat})\to\pi/e^2r$. The lattice Coulomb law is close to its asymptote beyond two lattice spacings: $4\pi rG_3(r)=1.078$, $1.038$ and $1.020$ at $r=2$, 3 and 4 along an axis, and $0.949$ at $(1,1,1)$, a relative deviation of about $0.3\,(a/r)^2$ along the axis. The error is therefore confined to charges within a few lattice spacings of one another, and one feature of that region must be kept. The continuum attraction $\pi/e^2r$ of an opposite pair is unbounded as $r\to0$, and the pair integral $\int d^3r\,e^{\pi/e^2r}$ diverges there, the collapse of a two-component Coulomb gas of point charges. The lattice bounds the attraction by its nearest-neighbour value $4\pi^2\beta\,G_3(\hat1)=3.40\,\beta$, so the continuum integrals carry a hard core $|x_i-x_j|\ge a_{\rm lat}$. The tight pairs inside a few lattice spacings are neutral and rare, and their only effect at long distances is a small renormalization of $e^2$ (§3.3).

*Step 5 (the grand-canonical Coulomb gas).* Assembling the four steps,
$$
\boxed{\ Z_{\rm gas}=\sum_{N_+=N_-}\frac{\zeta^{N_++N_-}}{N_+!\,N_-!}\int\prod_{i=1}^{N_++N_-}d^3x_i\ \exp\Big(-\frac{4\pi^2}{e^2}\sum_{i<j}q_iq_j\,G_3(x_i-x_j)\Big),\qquad \zeta=\frac{e^{-S_{\rm mono}}}{a_{\rm lat}^3},\ }
$$
where $q_i=+1$ for $i\le N_+$ and $-1$ otherwise, $G_3(x)=1/4\pi|x|$, and the hard core of Step 4 is understood. The coefficient is $4\pi^2/e^2$ for unordered pairs, equivalently $2\pi^2/e^2$ summed over ordered pairs $i\ne j$. It is the $4\pi^2\beta$ of Week 8 Move 7, and on the Maxwell side it is the energy $\frac{1}{2e^2}\int B^2$ of the field with $\partial\cdot B=2\pi\rho_m$, which equals $\frac{2\pi^2}{e^2}\sum_{i,j}q_iq_jG_3(x_i-x_j)$, self-energies included (§4). Neutrality $N_+=N_-$ is the zero-mode Kronecker delta of Week 8 Move 5. Opposite charges attract, like charges repel, and the Boltzmann factor of every pair tends to 1 at large separation. This is the monopole plasma of Polyakov (1975), with every constant fixed.

### 2.5 When the gas is dilute: three scales and one small parameter [Computed.]

At leading order in ζ the gas is ideal and each species has density ζ, so the monopole density is $n=2\zeta$ and the mean separation is $\bar r=(2\zeta)^{-1/3}$. Three other lengths compete with it. The core size is $a_{\rm lat}$ (in the Georgi–Glashow model of Week 10 it is the inverse $W$ mass). The Bjerrum length $\ell_B=\pi/e^2=\pi\beta\,a_{\rm lat}$ is the separation at which the Coulomb energy $\pi/e^2r$ of a pair equals one. The Debye length $\lambda_D=1/m_D$, with $m_D^2=8\pi^2\zeta/e^2$ derived in §4, is the range beyond which the plasma screens. The dilute plasma is the regime
$$
a_{\rm lat}\ \ll\ \ell_B\ \ll\ \bar r\ \ll\ \lambda_D ,
$$
and the ratios are
$$
\frac{\bar r}{a_{\rm lat}}=\big(2e^{-S_{\rm mono}}\big)^{-1/3},\qquad
\Gamma\equiv\frac{\ell_B}{\bar r}=2^{1/3}\pi\Big(\frac{\zeta}{e^6}\Big)^{1/3},\qquad
\frac{\lambda_D}{\bar r}=\frac{1}{\sqrt{4\pi\Gamma}}=\frac{2^{5/6}\,e}{4\pi\,\zeta^{1/6}},\qquad
\frac{\ell_B}{\lambda_D}=\frac{\pi m_D}{e^2}=2\sqrt2\,\pi^2\Big(\frac{\zeta}{e^6}\Big)^{1/2}.
$$
Each follows from the definitions in one line; for instance $(\bar r/\lambda_D)^2=8\pi^2\zeta\,(2\zeta)^{-2/3}/e^2=4\pi\cdot2^{1/3}\pi\,\zeta^{1/3}/e^2=4\pi\Gamma$. The plasma parameter Γ is the Coulomb energy of two monopoles at the mean separation, and $n\lambda_D^3=(4\pi\Gamma)^{-3/2}$ is the number of monopoles in a cube of side $\lambda_D$. The three plasma lengths involve only $e^2$ and ζ, so their ratios are powers of $\zeta/e^6$ alone, as dimensional analysis requires; the core enters only through $\zeta a^3=e^{-S_{\rm mono}}$ and $e^2a_{\rm lat}=1/\beta$. Table 1 evaluates the scales for the Villain theory from $S_{\rm mono}=4.9887\,\beta$, $\zeta a^3=e^{-S_{\rm mono}}$ and the formulas above.

| β | $S_{\rm mono}$ | $\zeta a^3$ | $\bar r/a$ | $\ell_B/a$ | $\lambda_D/a$ | $\zeta/e^6$ | Γ | $\lambda_D/\bar r$ | $n\lambda_D^3$ |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 9.98 | $4.6\times10^{-5}$ | 22 | 6.3 | 12 | $3.7\times10^{-4}$ | 0.28 | 0.53 | 0.15 |
| 3 | 14.97 | $3.2\times10^{-7}$ | 116 | 9.4 | 116 | $8.5\times10^{-6}$ | 0.081 | 0.99 | 0.98 |
| 4 | 19.95 | $2.2\times10^{-9}$ | 614 | 12.6 | $1.2\times10^{3}$ | $1.4\times10^{-7}$ | 0.020 | 1.97 | 7.7 |
| 5 | 24.94 | $1.5\times10^{-11}$ | $3.2\times10^{3}$ | 15.7 | $1.3\times10^{4}$ | $1.8\times10^{-9}$ | 0.0048 | 4.05 | 67 |
| 6 | 29.93 | $1.0\times10^{-13}$ | $1.7\times10^{4}$ | 18.8 | $1.5\times10^{5}$ | $2.2\times10^{-11}$ | 0.0011 | 8.49 | 613 |

**Table 1. The scales of the Villain monopole plasma, with $a=a_{\rm lat}$. The full ordering $a\ll\ell_B\ll\bar r\ll\lambda_D$ sets in between β = 4 and β = 5.**

The table makes three points. The gas is dilute early, with $\bar r=22\,a$ already at $\beta=2$. The plasma is weakly coupled later, with $\Gamma<0.1$ from $\beta\approx3$. And screening by many monopoles, $\lambda_D\gg\bar r$, comes last, because $\lambda_D/\bar r=2^{1/3}(8\pi^2\beta)^{-1/2}e^{S_{\rm mono}/6}$ grows only like $e^{0.83\beta}$: at $\beta=3$ the Debye length equals the mean separation, and at $\beta=2$ it is shorter, so there the linearized theory of §4 does not apply. The weak-coupling treatment of Weeks 9–10 is controlled as $\beta\to\infty$, with every correction suppressed by a positive power of $\zeta/e^6$ (F1). Figure 2 draws the hierarchy.

```
   a_lat              ℓ_B = π/e²               r̄ = (2ζ)^(−1/3)             λ_D = 1/m_D
     |--------------------|--------------------------|----------------------------|------>  length
   core               pair energy π/e²r          mean monopole               Debye screening
  (one cube)          equals one                 separation                  length

   r̄/a_lat = (2e^(−S_mono))^(−1/3)          ℓ_B/r̄ = Γ = 2^(1/3) π (ζ/e⁶)^(1/3)
   λ_D/r̄  = (4πΓ)^(−1/2) = 2^(5/6) e / (4π ζ^(1/6))          at β = 5:   1 : 16 : 3.2×10³ : 1.3×10⁴
```
**Figure 2. The three scales of the dilute monopole plasma, core size ≪ mean separation ≪ Debye length, with the Bjerrum length between the first two; every ratio among the plasma scales is a power of $\zeta/e^6$ (logarithmic axis, not to scale).**

## 3. The plasma as a field theory: sine-Gordon [Controlled to $O(\zeta^2)$ in the fugacity, both directions.]

### 3.1 The vertex normalization

The σ form of §2.1 makes the gas a field theory, exactly as in [[week-03-villain-form-xy-duality|Week 3]] §6. With $\langle\cdot\rangle_\sigma$ the normalized Gaussian average with weight $e^{-\|d\sigma\|^2/8\pi^2\beta}$, zero mode included, the covariance is $\langle\sigma_{\tilde x}\sigma_{\tilde y}\rangle_\sigma=4\pi^2\beta\,G_3(\tilde x-\tilde y)$, and for every neutral $v$
$$
\big\langle e^{-i\langle v,\sigma\rangle}\big\rangle_\sigma=e^{-\frac12(4\pi^2\beta)\langle v,G_3v\rangle}=e^{-2\pi^2\beta\langle v,G_3v\rangle},
$$
which is Week 8 Move 6 read backwards: the exact Coulomb weight. Truncating to $v_{\tilde x}\in\{0,\pm1\}$ (Step 3), $\sum_{v\in\{0,\pm1\}}e^{-iv\sigma}=1+2\cos\sigma$, so the truncated gas is exactly
$$
Z^{(0)}_{|v|\le1}=(2\pi\beta)^{-N_P/2}\,Z_{\rm ph}\,\Big\langle\prod_{\tilde x}\big(1+2\cos\sigma_{\tilde x}\big)\Big\rangle_\sigma .
$$
Here the vertices are bare, the coupling is $2\cos\sigma$ with unit coefficient per site, and the monopole action comes out of the self-contraction, $\langle e^{i\sigma_{\tilde x}}e^{-i\sigma_{\tilde y}}\rangle_\sigma=e^{-4\pi^2\beta[G_3(0)-G_3(\tilde x-\tilde y)]}=e^{-2S_{\rm mono}}\,e^{4\pi^2\beta G_3(\tilde x-\tilde y)}$. We normal-order at the lattice scale instead,
$$
V_\pm(\tilde x)\equiv e^{S_{\rm mono}}\,e^{\pm i\sigma_{\tilde x}},\qquad \big\langle V_+(\tilde x)V_-(\tilde y)\big\rangle_\sigma=e^{4\pi^2\beta\,G_3(\tilde x-\tilde y)}\ \xrightarrow{\ |\tilde x-\tilde y|\to\infty\ }\ 1,
$$
and with $V=\frac12(V_++V_-)$ the same identity reads $1+2\cos\sigma_{\tilde x}=1+2\zeta a_{\rm lat}^3\,V(\tilde x)$: the coupling is the fugacity, and $S_{\rm mono}$ is counted once, inside ζ. This is the scheme of [[courses/generalized-symmetries-course/conventions|conventions]] §5, and from now on $\cos\sigma$ means $V$. Unlike two dimensions, the self-contraction is finite here, so normal ordering is the finite rescaling by $e^{S_{\rm mono}}$. The last approximation is the exponentiation $\prod_{\tilde x}(1+2\zeta a^3V)\simeq\exp\big(2\zeta a^3\sum_{\tilde x}V\big)$, whose error consists of terms with two vertices on one site, which the lattice excludes and the continuum excludes by the hard core. With $a^3\sum_{\tilde x}\to\int d^3x$,
$$
\boxed{\ Z_{\rm gas}\simeq\int\mathcal{D}\sigma\ \exp\Big(-\int d^3x\,\Big[\frac{e^2}{8\pi^2}(\partial\sigma)^2-2\zeta\cos\sigma\Big]\Big),\qquad \zeta=\frac{e^{-S_{\rm mono}}}{a_{\rm lat}^3},\ }
$$
the three-dimensional sine-Gordon theory of the dual photon, with $\cos\sigma$ normal-ordered at the lattice scale.

### 3.2 The $O(\zeta^2)$ match, both directions

*From the gas to sine-Gordon.* The one-pair term of the gas, a $+$ at $\tilde x$ and a $-$ at $\tilde y$, has the exact weight $e^{-2S_{\rm mono}+4\pi^2\beta G_3(\tilde x-\tilde y)}=(\zeta a^3)^2\,\langle V_+(\tilde x)V_-(\tilde y)\rangle_\sigma$, which is the two-vertex term of $\langle\prod_{\tilde x}(1+2\zeta a^3V)\rangle_\sigma$, exactly.

*From sine-Gordon to the gas.* We expand the boxed weight to second order in ζ and contract with the Gaussian σ. The $O(\zeta)$ term vanishes by neutrality (the zero mode of σ), and at $O(\zeta^2)$ the same-sign products $\langle V_\pm V_\pm\rangle$ vanish for the same reason, so that
$$
\frac{(2\zeta)^2}{2}\int\!\!\int d^3x\,d^3x'\,\big\langle\cos\sigma(x)\cos\sigma(x')\big\rangle
=\frac{\zeta^2}{2}\int\!\!\int d^3x\,d^3x'\,\big[\langle V_+(x)V_-(x')\rangle+\langle V_-(x)V_+(x')\rangle\big]
=\zeta^2\int\!\!\int_{|x-x'|\ge a}d^3x\,d^3x'\ e^{\pi/e^2|x-x'|},
$$
which is the $N_+=N_-=1$ term of the boxed gas of §2.4, with the same $\zeta^2$, the same Coulomb factor $e^{+(4\pi^2/e^2)G_3}$ for an opposite pair, and the same hard core. $\square$ Higher orders match in the same way, term by term in a finite volume: at $O(\zeta^{2k})$ the Gaussian contraction of $k$ vertices $V_+$ and $k$ vertices $V_-$ is $\exp\big(-\frac{4\pi^2}{e^2}\sum_{i<j}q_iq_jG_3(x_i-x_j)\big)$, the Coulomb weight of that configuration.

### 3.3 What changes in three dimensions [Sketched; the numbers are Computed.]

Three differences from Week 3 matter for everything that follows.

*No vertex becomes irrelevant.* In two dimensions the vortex vertex has the scaling dimension $\pi\beta$, which crosses the marginal value 2, and the truncation to unit charges was justified by the dimensions (Week 3 F6). Here $\langle V_+(x)V_-(0)\rangle\to1$: a two-point function that tends to a nonzero constant belongs to an operator of dimension zero with a nonzero expectation value, the spontaneous breaking of §5.2. Every $\cos q\sigma$ is therefore strongly relevant at every β, the cosine is never irrelevant, and the truncation of Step 3 rests on the fugacity ratio $\zeta_2/\zeta=e^{-3S_{\rm mono}}$ alone.

*The pair weight is bounded.* The one-pair integral splits as $\zeta^2\int\!\!\int e^{\pi/e^2|x-x'|}=\zeta^2V^2+\zeta^2V\int d^3r\,\big(e^{\pi/e^2r}-1\big)$. The first term is two independent monopoles, the ideal gas; the energy of the pair never outweighs the entropy of its separation, which is the content of §6.1. The second term grows with the size of the system, because its integrand falls only like $\pi/e^2r$. That long-range part cancels at higher orders against the same-sign pairs of neutral four-monopole configurations, and the resummation of all such long-range parts is the Debye screening of §4, which produces corrections nonanalytic in ζ (the $\zeta^{3/2}$ of Problem 4⋆). The $O(\zeta^2)$ match is thus a statement at fixed finite volume, and the thermodynamic limit requires the resummation of §4.

*Tight pairs renormalize $e^2$.* An opposite pair on nearest-neighbour dual sites has the weight $w=e^{-2S_{\rm mono}+4\pi^2\beta G_3(\hat1)}=e^{-2\pi^2\beta/3}$, since $2G_3(0)-2G_3(\hat1)=\frac13$; it costs $6.58\,\beta$ against $9.98\,\beta$ for two separated monopoles, and the next pairs, at $(1,1,0)$ and beyond, cost $7.80\,\beta$ or more. In a slowly varying background σ, the two orientations of the pair on the dual link in direction μ contribute $w\big(e^{i\partial_\mu\sigma}+e^{-i\partial_\mu\sigma}\big)\simeq2w-w(\partial_\mu\sigma)^2$ to $\ln Z$, with $\partial_\mu\sigma$ the difference of σ across the link. Summed over links, this adds $w\,\|d\sigma\|^2$ to the action, against the stiffness term $\frac{1}{8\pi^2\beta}\|d\sigma\|^2$, so that
$$
\frac{e^2_{\rm eff}}{e^2}=1+8\pi^2\beta\,e^{-2\pi^2\beta/3}+\dots,
$$
where the dots are the farther pairs. The tight pairs are magnetic dipoles, and they screen the magnetic Coulomb law dielectrically, lowering the coefficient $4\pi^2/e^2$; the correction is $6\times10^{-7}$ at $\beta=3$ and negligible at weak coupling (F2).

## 4. Debye screening from the gas side [Controlled to leading order in $\zeta/e^6$.]

Consider a static test monopole of charge $Q$ at the origin, an external insertion $e^{iQ\sigma(0)}$, in the gas of §2.4. In the field of the other charges a charge $q$ at $x$ has the energy $q\,\varphi(x)$, with
$$
\varphi(x)=\frac{4\pi^2}{e^2}\int d^3y\,G_3(x-y)\,\rho(y),\qquad -\nabla^2\varphi=\frac{4\pi^2}{e^2}\,\rho ,
$$
where ρ is the magnetic charge density, test charge included. The coefficient is the unordered-pair coefficient of §2.4, because the energy of one charge collects each of its pairs once. The Debye–Hückel closure makes two approximations. (a) *Mean field:* the densities respond to the average potential, $n_\pm(x)=\zeta\,e^{\mp\varphi(x)}$, the grand-canonical Boltzmann factor at fugacity ζ; this neglects the correlations of each monopole with its neighbours, and it needs many monopoles within a screening length, $n\lambda_D^3\gg1$. (b) *Linearization:* $e^{\mp\varphi}\simeq1\mp\varphi$, valid where $|\varphi|\ll1$, which holds at the typical separation when $\Gamma\ll1$; the region $r\lesssim\ell_B$ where it fails contains a fraction $n\ell_B^3=\Gamma^3$ of the monopoles. Both conditions are powers of $\zeta/e^6$ (§2.5). Then $\rho=Q\,\delta^3(x)+n_+-n_-\simeq Q\,\delta^3(x)-2\zeta\varphi$, and
$$
\Big(-\nabla^2+\frac{8\pi^2\zeta}{e^2}\Big)\varphi=\frac{4\pi^2}{e^2}\,Q\,\delta^3(x),
$$
so that
$$
\boxed{\ m_D^2=\frac{8\pi^2\zeta}{e^2},\qquad \varphi(r)=\frac{\pi Q}{e^2}\,\frac{e^{-m_Dr}}{r}.\ }
$$
The magnetic field follows from φ. For a magnetostatic field $B=-\nabla\chi$ with $\partial\cdot B=2\pi\rho$, the energy $\frac{1}{2e^2}\int B^2=\frac{1}{2e^2}\int\chi\,(2\pi\rho)$ equals $\frac{2\pi^2}{e^2}\int\!\!\int\rho\,G_3\,\rho$, so the potential energy of a unit charge is $\varphi=\frac{2\pi}{e^2}\chi$ and
$$
B=-\frac{e^2}{2\pi}\nabla\varphi=\frac{Q}{2}\,(1+m_Dr)\,e^{-m_Dr}\,\frac{x}{r^3},
$$
which is the unscreened $Q\,x/2r^3$ for $r\ll\lambda_D$ and dies exponentially beyond. The induced charge $-2\zeta\varphi$ integrates to exactly $-Q$ (Problem 1): the plasma screens perfectly, and the flux of a test monopole does not reach infinity. The first corrections are of relative order $\ell_B/\lambda_D=\pi m_D/e^2=2\sqrt2\pi^2(\zeta/e^6)^{1/2}$; Problem 4⋆ computes one of them, the shift of the density at fixed ζ. A common error is to use the ordered-pair coefficient $2\pi^2/e^2$ in place of $4\pi^2/e^2$ in φ; the same steps then give $m_D^2=4\pi^2\zeta/e^2$, half the correct value.

On the field side the same number is the curvature of the sine-Gordon potential. Near its minimum $-2\zeta\cos\sigma\simeq-2\zeta+\zeta\sigma^2$, and with the stiffness $e^2/8\pi^2$ the linearized equation of motion $-\frac{e^2}{4\pi^2}\nabla^2\sigma+2\zeta\sigma=0$ gives the mass squared $8\pi^2\zeta/e^2$. [[week-10-polyakov-mass-gap-area-law|Week 10]] carries out that side in full, identifies $m_D$ with the photon mass $m_\gamma$ of [[courses/generalized-symmetries-course/conventions|conventions]] §5, and matches the screened propagator of σ to the potential above. The Debye mass also has a rigorous status [Stated — refs: Göpfert–Mack 1982, eq. (1.8a), footnote 4 and Theorem 4]. In their notation the coupling $\beta_{\rm GM}=4\pi^2/g^2$ is our $4\pi^2/e^2$ (a length), their lattice Coulomb potential at the origin is $v_{\rm Cb}(0)=0.2527/a_{\rm lat}$, our $G_3(0)/a_{\rm lat}$, and their $m_D^2a^2=(2\beta_{\rm GM}/a)\,e^{-\beta_{\rm GM}v_{\rm Cb}(0)/2}$ is $8\pi^2\beta\,e^{-S_{\rm mono}}$, which is exactly $8\pi^2\zeta/e^2$ with ζ in the lattice normal-ordering scheme. They identify $m_D^{-1}$ with the Debye–Hückel screening length of the Coulomb system and show that $m_D$ is asymptotically the mass gap.

> **Physical picture.** A test monopole placed in the plasma gathers a cloud of opposite charge of radius $\lambda_D$ that cancels its flux exactly, and the magnetic field it produces dies like $e^{-m_Dr}$. A measurement of the connected correlator of the magnetic field would see the same exponential, with $\lambda_D=1.3\times10^4\,a_{\rm lat}$ at $\beta=5$ (Table 1), so the dilute-plasma regime needs lattices far larger than $10^4$ sites per side before the screening is visible at all. Remove the monopoles and the cloud disappears, $B$ keeps its $1/r^2$ tail, and the photon is massless (§5.2). The computation is controlled to leading order in $\zeta/e^6$; Week 10 converts the screening of magnetic flux into the confinement of electric flux.

## 5. The magnetic symmetry in three dimensions

### 5.1 Current, charge and charged operators [Computed.]

The magnetic current of three-dimensional Maxwell theory is the Hodge dual of the field strength ([[courses/generalized-symmetries-course/conventions|conventions]] §5),
$$
j^\mu_{\rm mag}=\frac{1}{4\pi}\,\epsilon_{\mu\nu\rho}F_{\nu\rho}=\frac{B_\mu}{2\pi},\qquad \partial_\mu j^\mu_{\rm mag}=\frac{1}{2\pi}\,\partial\cdot B=\rho_m ,
$$
where the Bianchi identity $dF=0$ holds everywhere except at the monopoles. On the lattice the statement is exact: the flux of $F/2\pi$ out of a cube is $-m_c=q_c$ (Week 8 §2.1). The charge on a closed surface Σ, $Q(\Sigma)=\oint_\Sigma F/2\pi$, is an integer by Dirac quantization, and the symmetry operators are
$$
U_\alpha(\Sigma)=\exp\Big(i\alpha\oint_\Sigma\frac{F}{2\pi}\Big),\qquad \alpha\in\mathbb{R}/2\pi\mathbb{Z},
$$
supported on closed two-dimensional surfaces. A $q$-form symmetry in $d$ dimensions has its operators on closed $(d-q-1)$-dimensional surfaces and acts on $q$-dimensional objects ([[courses/generalized-symmetries-course/conventions|conventions]] §6), so with $d=3$ and surfaces of dimension two the degree is $q=0$. The magnetic symmetry of three-dimensional Maxwell theory is therefore an ordinary **0-form** $U(1)$, the $d=3$ case of the $(d-3)$-form rule of the master table (erratum E1), and its charged objects are points. In the dual variables it is the shift $\sigma\to\sigma+\alpha$ of the action $\frac{e^2}{8\pi^2}(\partial\sigma)^2$, whose Noether current $\frac{e^2}{4\pi^2}\partial_\mu\sigma$ equals $-i\,j^\mu_{\rm mag}$ by $B=\frac{ie^2}{2\pi}\partial\sigma$ (the $i$ of Euclidean signature, Week 8 §4.5). The charged operators are the **local** monopole operators $e^{iq\sigma(x)}$ ([[higher-form-symmetries]]).

We check the charge directly. In the Gaussian theory, for $\mathcal{O}=\prod_ke^{iq_k\sigma(y_k)}$ with $\sum_kq_k=0$, integration by parts gives $\langle\sigma(x)\,\mathcal{O}\rangle=i\sum_kq_k\langle\sigma(x)\sigma(y_k)\rangle_0\langle\mathcal{O}\rangle$, and with the covariance of §2.1
$$
\frac{\langle j_{\rm mag}(x)\,\mathcal{O}\rangle}{\langle\mathcal{O}\rangle}=\frac{ie^2}{4\pi^2}\,\partial_x\Big(i\,\frac{4\pi^2}{e^2}\sum_kq_k\,G_3(x-y_k)\Big)=\sum_kq_k\,\frac{x-y_k}{4\pi|x-y_k|^3}.
$$
The flux of $j_{\rm mag}$ through a small sphere around $y_k$ is $q_k$, and $B=2\pi j_{\rm mag}$ carries the flux $2\pi q_k$ of a charge-$q_k$ monopole, with the field $q_k(x-y_k)/2|x-y_k|^3$ of [[courses/generalized-symmetries-course/conventions|conventions]] §5. Therefore $U_\alpha(\Sigma)\,\mathcal{O}=e^{i\alpha\sum_{k\in\Sigma}q_k}\,\mathcal{O}$, with the sum over the insertions enclosed by Σ: in three dimensions the linking of a closed surface with a point is whether the surface encloses it. Table 2 sets the three-dimensional statement beside the four-dimensional one, as the check against the form-degree master table of [[courses/generalized-symmetries-course/conventions|conventions]] §6.

| | $d=3$ | $d=4$ |
|---|---|---|
| degree of the magnetic symmetry, $d-3$ | 0 | 1 |
| closed form (closed by the Bianchi identity) | $F/2\pi$, i.e. $j^\mu_{\rm mag}=B_\mu/2\pi$ | $F/2\pi$ |
| symmetry operators on | closed surfaces | closed surfaces |
| charged objects | local monopole operators $e^{iq\sigma(x)}$ | 't Hooft lines |
| dynamical monopoles | instantons, points of $\Lambda^*$ | worldlines, closed loops on $\Lambda^*$ |
| monopole-free theory | spontaneously broken; the photon is its Goldstone boson | spontaneously broken |
| compact QED | explicitly broken at every coupling (Weeks 9–10) | emergent and spontaneously broken in the Coulomb phase, explicitly broken in the confining phase (Week 11) |

**Table 2. The magnetic symmetry of $U(1)$ gauge theory in three and four Euclidean dimensions, by the $(d-3)$-form rule of [[courses/generalized-symmetries-course/conventions|conventions]] §6.**

### 5.2 Without monopoles: spontaneous breaking, and the photon as its Goldstone boson [Computed.]

In the monopole-free theory (the term $v=0$ of Week 8 §6, the Villain theory with $dn=0$) the symmetry is exact, and it is spontaneously broken. The monopole two-point function is Gaussian; in lattice units
$$
\big\langle e^{iq\sigma(x)}e^{-iq\sigma(0)}\big\rangle_0=e^{-4\pi^2q^2\beta\,[G_3(0)-G_3(x)]}=e^{-2q^2S_{\rm mono}}\,e^{4\pi^2q^2\beta\,G_3(x)}\ \xrightarrow{\ |x|\to\infty\ }\ e^{-2q^2S_{\rm mono}}\ne0,
$$
where in physical units the $x$-dependent factor is $e^{\pi q^2/e^2|x|}$. A two-point function of a charged local operator that tends to a nonzero constant is long-range order: by cluster decomposition $|\langle e^{iq\sigma}\rangle|=e^{-q^2S_{\rm mono}}$ in a pure state, and the $U(1)^{(0)}$ is spontaneously broken, with a circle of vacua labelled by the value of σ. (On the torus the zero-mode integral averages over the circle and the one-point function vanishes; the two-point function detects the order.) The Goldstone boson is σ itself, the single polarization of the three-dimensional photon, and it is massless because it is a Goldstone boson. Two checks close the section. A continuous 0-form symmetry can break in $d=3$, since the Coleman–Mermin–Wagner bound of [[courses/generalized-symmetries-course/conventions|conventions]] §6 forbids breaking only for $q\ge d-2=1$. And the normal-ordering factor of §3.1 is the inverse of the order parameter, $V_\pm=e^{\pm i\sigma}/|\langle e^{i\sigma}\rangle|$: the monopole fugacity $\zeta a^3=e^{-S_{\rm mono}}$ is the modulus of the monopole condensate of the monopole-free theory.

### 5.3 With monopoles: explicit breaking [Computed at the level of the effective action.]

With dynamical monopoles $\partial\cdot j_{\rm mag}=\rho_m\ne0$, and the charge is not conserved: by §2.2 the flux through a spatial slice jumps at every monopole, and for every closed surface $U_\alpha(\partial V)=e^{i\alpha Q_V}$, with $Q_V=\sum_{c\in V}q_c$ the net monopole charge inside, which depends on where the surface is drawn. The symmetry operator is no longer topological, and the symmetry is broken explicitly. In the sine-Gordon theory the breaking sits in the action, since $-2\zeta\cos\sigma$ is invariant under $\sigma\to\sigma+\alpha$ only for $\alpha\in2\pi\mathbb{Z}$, which acts trivially; no subgroup of the $U(1)$ survives. The Ward identity follows from the Schwinger–Dyson equation $\big\langle\frac{\delta S}{\delta\sigma(x)}\,\mathcal{O}\big\rangle=\big\langle\frac{\delta\mathcal{O}}{\delta\sigma(x)}\big\rangle$, with $\frac{\delta S}{\delta\sigma}=-\frac{e^2}{4\pi^2}\partial^2\sigma+2\zeta\sin\sigma$. For $\mathcal{O}=e^{iq\sigma(0)}\mathcal{O}'$, with $\mathcal{O}'$ supported away from $x$, multiplying by $i$ and using $j_{\rm mag}=\frac{ie^2}{4\pi^2}\partial\sigma$ gives, inside correlators,
$$
\partial\cdot j_{\rm mag}(x)=q\,\delta^3(x)+\zeta\big(e^{i\sigma(x)}-e^{-i\sigma(x)}\big),
$$
where the first term is the inserted monopole and the second is the plasma: $\zeta e^{i\sigma}$ creates a monopole of charge $+1$ anywhere, and $\zeta e^{-i\sigma}$ one of charge $-1$. This is the operator form of $\partial\cdot B=2\pi\rho_m$. The symmetry of which σ was the Goldstone boson is now broken by a term in the action, and the would-be Goldstone boson acquires the mass $m_D$ of §4: the photon of compact QED₃ is a pseudo-Goldstone boson. If only monopoles with charges in $N\mathbb{Z}$ occur, $\cos N\sigma$ keeps a $\mathbb{Z}_N^{(0)}$ (Problem 3). F3 lists what "explicitly broken" means as a measurement.

> **Physical picture.** The mechanism fits in one sentence: the photon of three-dimensional Maxwell theory is massless because it is the Goldstone boson of the magnetic $U(1)^{(0)}$, and compactness supplies the instantons that break that symmetry explicitly, so nothing protects the masslessness. As a statement about symmetries this is exact; as a statement about the size of the mass it is controlled at weak coupling, where $m_D/e^2\propto(\zeta/e^6)^{1/2}$. Drop the compactness and the symmetry is exact again, with a massless photon. For the research line of the course this is the three-dimensional prototype of defects whose proliferation changes the low-energy field content, the theme of the [[julia-toulouse-mechanism]] and of the [[condensation-defects]] of Semester II [Formal analogy: the plasma is a gas of instantons, and the analogy with the condensation of extended defects is structural].

## 6. No Coulomb phase at any coupling

### 6.1 The energy–entropy argument, done correctly [Heuristic.]

The argument often given, that a gas of points always has more entropy than energy, proves too much: the vortices of the two-dimensional XY model are points with a fixed core action as well, and they bind into dipoles below $T_{\rm BKT}$ ([[week-04-bkt-kramers-wannier-disorder|Week 4]]). What decides is how the energy of a pair grows with its separation, compared with the entropy of the separation (Figure 3). In two dimensions a vortex pair at separation $r$ costs $2\pi\beta\ln(r/a_0)$ plus its core energies (Week 3 §4), and its separation has the entropy $\ln(\pi r^2/a_0^2)$; both are logarithmic, so which one wins depends on β, and at large β the pairs stay bound. In three dimensions the energy of an opposite pair, measured from its nearest-neighbour value, is
$$
U(r)=4\pi^2\beta\,\big[G_3(\hat1)-G_3(r)\big]\ \le\ 4\pi^2\beta\,G_3(\hat1)=3.40\,\beta ,
$$
bounded at every separation, while the entropy of the separation grows up to $\ln(V/a_{\rm lat}^3)$. The total weight of the configurations in which the pair is separated by more than a fixed $R$, relative to those in which it is bound within $R$, is at least $\big(V-\frac{4\pi}{3}R^3\big)\big/\big(\frac{4\pi}{3}R^3\,e^{3.40\beta}\big)$ (volumes in units of $a_{\rm lat}^3$), which diverges as $V\to\infty$ at every β. A finite density of free monopoles is therefore present at every coupling, and a finite density of free magnetic charges screens (§4). The bound survives inside a medium of bound pairs, whose dielectric effect only rescales the Coulomb tail (§3.3). The argument is heuristic because it treats one pair in the background of the others.

```
  U(r) − U(a)
      ↑                                                   ..··´´   2d vortex pair: 2πβ ln(r/a₀)
      |                                           ..··´´           (logarithmic, like its entropy)
      |                                   ..··´´
      |                           ..··´´
      |                   ..··´´
 3.40β+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  bound 4π²β G₃(1̂) in d = 3
      |           ..··´´    ____________------------------------
      |       ..·´   ___--´´                                      3d monopole pair:
      |    .·´  _--´´                                             4π²β [G₃(1̂) − G₃(r)]
      |  .´ _-´
      | .´_´
      +-----------------------------------------------------------------→  ln r
      a
    entropy of the separation:  2 ln(r/a₀) in d = 2;  3 ln(r/a) in d = 3, up to ln(V/a³)
```
**Figure 3. Energy against entropy for one pair of opposite point defects. In two dimensions the pair energy grows logarithmically, as does the entropy of the separation, and at large β the pairs bind; in three dimensions it saturates at $3.40\,\beta$ while the entropy grows to $\ln V$, so the pairs unbind at every coupling.**

### 6.2 What is proved [Stated — refs.]

Three statements cover all couplings. At weak coupling, the dilute-gas treatment of §§2–4 and its continuation in Week 10 is Polyakov's calculation (1975; 1977), controlled in $\zeta/e^6$. At strong coupling the convergent strong-coupling expansion gives an area law directly, for every compact gauge group ([[week-06-wilson-action-strong-coupling|Week 6]]; Osterwalder–Seiler 1978). For every coupling, Göpfert and Mack (1982) proved it for the Villain action. Their Theorem 1 bounds the string tension from below at weak coupling, $\alpha\ge c\,m_D/\beta_{\rm GM}$, that is $\alpha\ge c\,e^2m_D/4\pi^2$ in our notation, with $m_D$ the Debye mass of §4; their Corollary 2 states that the string tension is positive for every value of the coupling, which follows from Theorem 1 because the string tension in lattice units decreases monotonically with β by a three-dimensional version of Guth's inequality. They work with the dual integer-height model, their "$\mathbb{Z}$-ferromagnet" (the height model of Week 8 §4.1), whose surface tension equals the string tension. Compact QED₃ therefore has no Coulomb phase at any coupling: the monopole-free theory, with its massless photon, is never its long-distance limit ([[confinement]]).

## 7. Subtleties and fine print

**F1 — The window of the dilute-gas treatment, and what $\zeta/e^6$ does not control.** On the lattice $\zeta/e^6=\beta^3e^{-4.99\beta}$ is small at both ends of the coupling range: its maximum is $0.011$, at $\beta=0.60$. A small $\zeta/e^6$ alone therefore does not make the gas dilute; at strong coupling $\zeta a^3\to1$ and the lattice is filled with monopoles. The weak-coupling regime needs two conditions: $e^2a_{\rm lat}=1/\beta\ll1$, which puts the core far inside the Bjerrum length, so that the continuum Coulomb law governs the interactions that matter, and $\zeta/e^6\ll1$, which orders the plasma scales. By Table 1 the full ordering holds from $\beta\approx4$–5, and the ratio $\lambda_D/\bar r$ grows only like $e^{S_{\rm mono}/6}$, so the expansion is asymptotic as $\beta\to\infty$ with every correction suppressed by a positive power of $\zeta/e^6$: for instance, the relative correction to the free energy is $(2\sqrt2\pi^2/3)(\zeta/e^6)^{1/2}$, which is $3.5\times10^{-3}$ at $\beta=4$ (Problem 4⋆).

**F2 — Which $e^2$ appears where.** (i) $\beta=1/(e^2a_{\rm lat})$ defines the bare coupling at the lattice scale, of mass dimension one, and $S_{\rm mono}=4.99\,\beta$ and ζ are written with it. (ii) The $e^2$ of the long-distance Coulomb law, of the stiffness $e^2/8\pi^2$ of the sine-Gordon theory and of $m_D^2=8\pi^2\zeta/e^2$ is the coupling of the effective theory at scales between $a_{\rm lat}$ and $\lambda_D$. For the Villain action it differs from the bare one only through the tight pairs of §3.3, $e^2_{\rm eff}/e^2=1+8\pi^2\beta e^{-2\pi^2\beta/3}$, exponentially close to one, because photon and monopoles decouple exactly. (iii) For the Wilson action the self-interactions of the cosine also renormalize $e^2$, by powers of $1/\beta$, and the monopole core changes, and with it the constant 4.99 (Week 8 F5, Week 3 F2); formulas that combine $S_{\rm mono}$ with $e^2$ then need the Villain-equivalent coupling. (iv) Göpfert and Mack, and Polyakov (1975), write the coupling as $g^2$; in Göpfert–Mack $\beta_{\rm GM}=4\pi^2/g^2$ is a length, $4\pi^2\beta\,a_{\rm lat}$ in our notation (§4).

**F3 — What "explicitly broken by dynamics" means operationally.** Nothing is added by hand: the compact lattice theory has no exact magnetic symmetry at all, and the breaking is carried by its own dynamical defects, with a strength ζ that is exponentially small at weak coupling, so the symmetry holds approximately at distances short compared with $\lambda_D$. Four measurements separate the monopole-free theory from the plasma. (a) Conservation: the flux through a spatial slice is constant in the first and jumps at the rate $2\zeta$ per unit area and unit time in the second (§2.2). (b) Topological operators: $\langle U_\alpha(\partial V)\rangle=1$ exactly in the first; in the second it decreases with the size of $\partial V$, by an area law at small α (Problem 5⋆). (c) Spectrum: a circle of vacua and a massless Goldstone boson in the first, a unique vacuum and the gap $m_D$ in the second. (d) Correlators: the connected monopole two-point function falls like $1/|x|$ in the first and like $e^{-m_D|x|}/|x|$ in the second (Problem 2). What does not separate them is $|\langle e^{i\sigma}\rangle|$, which is nonzero in both: in the plasma the cosine pins σ at zero, and the one-point function is nonzero with no spontaneous breaking.

**F4 — Finite temperature, a preview.** At temperature $T$ the Euclidean time is a circle of length $1/T$. At separations large compared with $1/T$ the image sum of $G_3$ is $-(T/2\pi)\ln\rho$ plus a constant, so the pair interaction of the monopoles becomes $-\frac{2\pi T}{e^2}\,q_iq_j\ln\rho$: the two-dimensional vortex gas of Weeks 3–4 at the effective stiffness $\beta_{\rm eff}=T/e^2$. By Week 4 the monopoles then bind when $\pi\beta_{\rm eff}>2$, that is above $T_c=2e^2/\pi$ at the Gaussian level (screening renormalizes the value, as in Week 4), and above $T_c$ the photon is massless again: a deconfinement transition of BKT type. The same number follows from the Polyakov loop: with $\theta=A_0/T$ the reduced action $\frac{1}{2e^2}\int d^3x\,(\partial_iA_0)^2$ is $\frac{T}{2e^2}\int d^2x\,(\partial\theta)^2$, an XY model of stiffness $T/e^2$ whose vortices are the monopoles. [Sketched: the reduction of the fugacity to two dimensions and the renormalization of $T_c$ are omitted; Week 10 develops the mechanism.]

**F5 — The sign bookkeeping $e^{-im_c\sigma}$.** The lattice monopole number is minus the magnetic charge, $q_c=-m_c$, because the flux out of the cube is $-2\pi m_c$ (Week 8 §2.1), so the sources $e^{-im_c\sigma}$ are the insertions $e^{iq_c\sigma}$ of [[courses/generalized-symmetries-course/conventions|conventions]] §5, and the Ward identity of §5.3 carries $+\rho_m=+\sum_iq_i\delta^3$. The sign is immaterial in the neutral, even sums of §§2–4, where only $\cos\sigma$ appears. It matters as soon as monopoles couple to something odd: a background field for the $U(1)^{(0)}$, a Chern–Simons term (Problem 6⋆⋆), or the θ-term and the Witten effect of [[week-12-theta-terms-witten-effect|Week 12]]. A wrong sign reverses the charge assigned to $e^{i\sigma}$ and the direction of the flux in Figure 1 (Week 8 F1).

**F6 — One monopole action, three appearances.** $S_{\rm mono}$ enters as (i) the diagonal term of the exact gas (Week 8 §4.4), (ii) the self-contraction of the bare vertices (§3.1), and (iii) $-\ln|\langle e^{i\sigma}\rangle|$ in the monopole-free theory (§5.2). These are one number, and a consistent scheme keeps it in exactly one place, as κ in Week 3 F5. With bare vertices the coupling is $2\cos\sigma$ per site; with vertices normal-ordered at the lattice scale it is $2\zeta\cos\sigma$. Combining ζ with bare vertices counts the action twice, which multiplies the fugacity by a spurious $e^{-S_{\rm mono}}$ and the photon mass by $e^{-S_{\rm mono}/2}$. The rigorous Debye mass of Göpfert and Mack (§4) is written with the normal-ordered ζ.

## 8. Common misconceptions

- **"The three-dimensional photon is massless because gauge invariance protects it."** It is tempting because in four-dimensional QED gauge invariance forbids the mass term $A_\mu A_\mu$ and perturbation theory never generates one. In three dimensions gauge-invariant masses exist: the cosine of the gauge-invariant dual photon, generated by the monopoles; the Chern–Simons term, with the topological mass $ke^2/2\pi$ (Problem 6⋆⋆); the Higgs mechanism. What keeps the monopole-free photon massless is the magnetic $U(1)^{(0)}$, whose Goldstone boson it is (§5.2), and the monopoles break that symmetry explicitly and give the photon the mass $m_D$ with gauge invariance intact throughout.
- **"Monopole operators are non-local objects."** It is tempting because on the direct lattice a monopole operator is a disorder operator, defined by forcing $dn$ at a cube with a Dirac string attached (Week 8 F1), and because in four dimensions the magnetic objects are 't Hooft lines. The Dirac string is invisible for integer electric charges (Week 8 §2.2), so the operator depends only on its endpoint, and in the dual variables it is $e^{i\sigma(x)}$, manifestly local. In $d=3$ the magnetic symmetry is 0-form and its charged objects are points (§5.1); the four-dimensional analogue is a line because there the magnetic symmetry is a 1-form symmetry (Week 11).
- **"Monopoles proliferate because a gas of points always has more entropy than energy."** It is tempting because a point defect has a fixed core action while the entropy grows with the volume. Two-dimensional vortices are points with a fixed core action too, and they bind below $T_{\rm BKT}$. The criterion is how the pair energy grows with the separation, logarithmically in two dimensions and not at all in three (§6.1), and the statement for all couplings is the theorem of Göpfert and Mack (§6.2).

## 9. Historical note

Polyakov's letter of 1975, "Compact gauge fields and the infrared catastrophe", set out the program in three pages. He defined compact electrodynamics on a lattice by an action periodic in the plaquette angle, observed that the periodicity lets the continuum field strength carry singular surfaces of flux $2\pi N$ at no cost, and in three dimensions identified the resulting finite-action configurations with a gas of Dirac monopoles, pseudo-particles whose density is proportional to $e^{-E/g^2}$. Inserting a Wilson loop, he reduced the problem to the free energy of the monopole plasma, at the temperature $g^2$, in the external field of the loop, solved it by the Debye method, correct for small $g^2$, and found a Debye correlation length with a photon mass $m^2\propto e^{-\epsilon/g^2}$ in lattice units and an area law, $W[C]\propto g^2mA$, which by Wilson's criterion is charge confinement in three-dimensional compact QED. In four dimensions the finite-action configurations are closed rings, whose dipole fields leave the correlation length infinite and give a perimeter law at small $g^2$; with Wilson's strong-coupling confinement, this implied a critical charge. The 1977 paper, "Quark confinement and topology of gauge groups", worked the three-dimensional mechanism out for compact QED in 2+1 dimensions treated as a variant of the Georgi–Glashow model, whose monopoles are instantons with a finite core, proved that charge is confined at small coupling and evaluated the force between charges, before turning to pseudoparticles in four-dimensional Yang–Mills theory (Week 8 §9). Five years later Göpfert and Mack made the three-dimensional statement a theorem for the Villain action at every coupling, with the Debye–Hückel mass of §4 as the scale of their lower bound on the string tension.

## 10. What to take away

1. **The monopole plasma is Week 8's exact Coulomb gas read as statistical mechanics:** fugacity $\zeta=e^{-S_{\rm mono}}/a_{\rm lat}^3$ with $S_{\rm mono}=2\pi^2G_3(0)\beta=4.99\,\beta$, pair interaction $\frac{4\pi^2}{e^2}q_iq_jG_3$ for unordered pairs. The truncation to unit charges and the continuum positions are the only approximations, each with a stated error. Physically, each monopole is an instanton at which the magnetic flux through space jumps by $2\pi$.
2. **The dilute plasma has ordered scales,** $a_{\rm lat}\ll\ell_B\ll\bar r\ll\lambda_D$, whose plasma ratios are powers of the single parameter $\zeta/e^6$, for instance $\lambda_D/\bar r=2^{5/6}e/4\pi\zeta^{1/6}$. For the Villain theory the ordering is reached only from $\beta\approx4$–5, and the treatment is asymptotic in weak coupling.
3. **The gas is the sine-Gordon theory** $\int\big[\frac{e^2}{8\pi^2}(\partial\sigma)^2-2\zeta\cos\sigma\big]$ to $O(\zeta^2)$, with $\cos\sigma$ normal-ordered at the lattice scale and $S_{\rm mono}$ counted once. The cosine is the amplitude for the vacuum to emit a monopole, and in three dimensions it is relevant at every coupling.
4. **The plasma screens,** $m_D^2=8\pi^2\zeta/e^2$, the Debye mass that Göpfert and Mack found rigorously; the flux of a test monopole dies within $\lambda_D$. Week 10 identifies $m_D$ with the photon mass.
5. **The magnetic symmetry of three-dimensional Maxwell theory is a 0-form $U(1)$** with current $B/2\pi$ and local charged operators $e^{iq\sigma}$. Without monopoles it is spontaneously broken and the photon is its Goldstone boson; the monopoles break it explicitly at every coupling, $\partial\cdot j_{\rm mag}=\rho_m\neq0$ with $\rho_m$ the monopole density, whose dilute-gas form is $\zeta(e^{i\sigma}-e^{-i\sigma})$. Because the pair energy is bounded (heuristic), and by the theorem of Göpfert and Mack, there is no Coulomb phase.

## 11. Looking ahead: Week 10

We hold a screening plasma, its sine-Gordon form and a Debye mass $m_D$, with the small parameter $\zeta/e^6$ that controls both. [[week-10-polyakov-mass-gap-area-law|Week 10]] inserts a Wilson loop. Through the duality it becomes a line around which σ winds (Week 8 Problem 1); the smooth part of σ must unwind that monodromy, and with the cosine present the cheapest way is a wall of σ spanning the loop, whose tension gives the area law. The Debye mass of §4 returns as the curvature of the sine-Gordon potential and as the photon mass $m_\gamma$, and the tension comes out proportional to $e^2m_\gamma$; Göpfert and Mack quote the same classical value, $8m_D/\beta_{\rm GM}=2e^2m_D/\pi^2$, below their Theorem 1. Week 11 then returns to four dimensions, where the monopoles are loops and a Coulomb phase exists.

## 12. Problem set

Problems 1–3 are the classroom core and use only §§2–5; Problems 4⋆ and 5⋆ are self-study consolidation, solvable from the note, each with a hint; Problem 6⋆⋆ is a research extension and states what is known, what is explored and what counts as completion. The duality itself was derived in Week 8 and is not set again.

**Core problems** (everyone).

**1. The Debye cloud and its flux** (extends §4).
(a) From the linearized solution, compute the induced charge density $\rho_{\rm ind}(r)$ around a test monopole of charge $Q$ and show that its integral is $-Q$.
(b) Compute the magnetic flux through a sphere of radius $R$ centred on the test charge, and identify the charge it encloses.
(c) For the Villain theory at $\beta=3$ and at $\beta=5$, give $\lambda_D$, $\bar r$, the number of monopoles in a Debye sphere $\frac{4\pi}{3}n\lambda_D^3$, and Γ, and decide at each coupling which of the two Debye–Hückel approximations of §4 is justified.
(*Hint:* use $2\pi\zeta/e^2=m_D^2/4\pi$, $B=-\frac{e^2}{2\pi}\nabla\varphi$, and Table 1.)

**2. Order parameter, spontaneous breaking and explicit breaking** (extends §§5.2–5.3).
(a) In the monopole-free theory on the infinite lattice, show that $|\langle e^{iq\sigma}\rangle|=e^{-q^2S_{\rm mono}}$, and relate it to the fugacity $\zeta_q$ of Step 2.
(b) Compute the connected two-point function $\langle e^{i\sigma(x)}e^{-i\sigma(0)}\rangle-|\langle e^{i\sigma}\rangle|^2$ at large $|x|$, in physical units, (i) in the monopole-free theory and (ii) in the plasma, in the Gaussian approximation to the sine-Gordon action, whose covariance is $\frac{4\pi^2}{e^2}\big(-\nabla^2+m_D^2\big)^{-1}$.
(c) Explain why $|\langle e^{i\sigma}\rangle|$ cannot distinguish the spontaneous breaking of (i) from the explicit breaking of (ii), and name two quantities that can.
(*Hint:* $\langle e^{iA}\rangle=e^{-\langle A^2\rangle/2}$ for a Gaussian $A$; in (ii) use $\int\frac{d^3k}{(2\pi)^3}\big[\frac{1}{k^2+m^2}-\frac1{k^2}\big]=-\frac{m}{4\pi}$ for the one-point function.)

**3. The $\mathbb{Z}_N$ remnant of the magnetic symmetry** (extends §§3 and 5). Restrict the Villain sum to monopole numbers in $N\mathbb{Z}$ by inserting $\prod_c\frac1N\sum_{k_c\in\mathbb{Z}_N}e^{2\pi ik_c(dn)_c/N}$.
(a) Show that the dual sum runs over $v\in N\,C^0(\Lambda^*,\mathbb{Z})$ with unchanged weights, and that the dilute gas becomes $\int\big[\frac{e^2}{8\pi^2}(\partial\sigma)^2-2\zeta_N\cos N\sigma\big]$; give $\zeta_N$ in the lattice normal-ordering scheme.
(b) Show that $U_\alpha(\partial V)$ is topological for $\alpha\in\frac{2\pi}{N}\mathbb{Z}$, so that the magnetic $U(1)^{(0)}$ is explicitly broken to $\mathbb{Z}_N^{(0)}$, and state the degree and the charged operators of the remnant.
(c) Find the vacua of the potential and the photon mass, and decide whether $\mathbb{Z}_N^{(0)}$ is spontaneously broken.
(*Hint:* (a) is the source argument of Week 8 §4.3 with $\eta=2\pi k/N$; for (b) use §5.3 with $Q_V\in N\mathbb{Z}$.)

**Starred problems.**

**4⋆. Beyond Debye–Hückel: the free energy and the density of the plasma** (extends §4 and §3.3).
(a) *Field side.* In the Gaussian approximation to the sine-Gordon theory, show that the free energy density relative to the monopole-free theory is $f=-2\zeta+\frac12\int\frac{d^3k}{(2\pi)^3}\ln\big(1+m_D^2/k^2\big)$, and evaluate it with a momentum cutoff Λ as $-2\zeta+\frac{m_D^2\Lambda}{4\pi^2}-\frac{m_D^3}{12\pi}$. Show that the term linear in $m_D^2$ is the $O(\zeta)$ self-contraction of a bare cosine, which the normal ordering of §3.1 has already put into ζ.
(b) *Gas side.* From the screened potential of §4, compute the potential of the cloud at the position of the test charge, $\varphi_{\rm ind}(0)=-\pi Qm_D/e^2$, and the excess chemical potential $\mu_{\rm ex}=\frac12Q^2\,(-\pi m_D/e^2)$ by the charging process; conclude that $n=2\zeta e^{-\mu_{\rm ex}}\simeq2\zeta\big(1+\frac{\pi m_D}{2e^2}\big)$, and integrate $\zeta\,\partial p/\partial\zeta=n$ to obtain the pressure $p=2\zeta+m_D^3/12\pi$. Compare with (a).
(c) Show that the relative correction is $\frac{m_D^3}{24\pi\zeta}=\frac{2\sqrt2\pi^2}{3}(\zeta/e^6)^{1/2}$, evaluate it at $\beta=4$ and 5, and explain why a term proportional to $\zeta^{3/2}$ cannot come from any finite order of the fugacity expansion.
(*Hint:* in (b) the charging factor $\frac12$ comes from switching the charge on from 0 to $Q$; in (c) look at the large-$r$ behaviour of the second virial coefficient, as in §3.3. In the Gaussian approximation $\langle\cos\sigma\rangle=e^{\pi m_D/2e^2}$, the same enhancement as in (b).)

**5⋆. The symmetry operator in the plasma: an area law** (extends §5.3 and F3).
(a) Add an external potential ψ coupled to the magnetic charges and derive, from the linearized mean-field equation, the charge structure factor $S(k)=2\zeta\,k^2/(k^2+m_D^2)$, using the classical fluctuation–response relation $\delta\langle\rho(k)\rangle=-S(k)\,\psi(k)$.
(b) For a slab of thickness $L$ and area $A$, show that $\langle Q_V^2\rangle=\frac{2\zeta A}{m_D}\big(1-e^{-m_DL}\big)$.
(c) To second order in α, conclude that $\langle U_\alpha(\partial V)\rangle\simeq\exp\big(-\frac{\alpha^2}{2}\,\zeta\lambda_D\,|\partial V|\big)$ for $L\gg\lambda_D$, and compare with the volume law $\exp[-2\zeta V(1-\cos\alpha)]$ of an unscreened ideal gas and with $\langle U_\alpha\rangle=1$ in the monopole-free theory. Which of the three behaviours is the operational signature of explicit breaking in a screening plasma?
(*Hint:* $\int_{-\infty}^{\infty}\frac{dk}{2\pi}\,\frac{1-\cos kL}{k^2+m^2}=\frac{1-e^{-mL}}{2m}$.)

**⋆⋆ problems** (research extension).

**6⋆⋆. Monopoles with a Chern–Simons term.** Add to the continuum Euclidean action of compact QED₃ a Chern–Simons term at integer level $k$, entering the weight as the phase $\exp\big(\frac{ik}{4\pi}\int a\wedge da\big)$, the analogue of the θ-term phase of [[courses/generalized-symmetries-course/conventions|conventions]] §10. *What is known:* the Maxwell–Chern–Simons photon has the topological mass $ke^2/2\pi$, and a magnetic flux $2\pi$ binds electric charge $k$; the group's paper (Grigorio, Guimaraes, Wotzasek, *Phys. Lett. B* 674 (2009) 213 [arXiv:0808.3698]) treats monopoles in the presence of the Chern–Simons term with the Julia–Toulouse approach. *What is explored:* what the Chern–Simons term does to the monopole plasma of this week and to the magnetic symmetry. (a) From the equations of motion, show that a monopole event, which changes the flux through space by $2\pi q$ (§2.2), must create electric charge $kq$, with the sign fixed in the orientation of [[courses/generalized-symmetries-course/conventions|conventions]] §1, so that $e^{i\sigma}$ alone is not gauge invariant and must end a Wilson line of charge $k$. (b) Derive the topological mass. (c) Estimate the action of a monopole–antimonopole pair at separation $R$ joined by such a line, and decide whether a Debye plasma of monopoles can form; say what follows for the area law of Week 10. (d) State the fate of the magnetic symmetry, checked against the master table. *Completion:* (a) and (b) derived with signs in the course's conventions; (c) a quantitative estimate with its cutoff dependence and a conclusion, labelled heuristic; (d) a one-page comparison with the effective theory obtained in the source. *Sources:* the note, Week 8 §2.2, and the paper cited.

## Self-study answer checkpoints

These checkpoints cover the core problems; starred and ⋆⋆ problems remain source-led.

1. (a) The decisive step is the linearized density: $\rho_{\rm ind}=-2\zeta\varphi=-\frac{Qm_D^2}{4\pi}\frac{e^{-m_Dr}}{r}$, and $\int d^3x\,\rho_{\rm ind}=-Qm_D^2\int_0^\infty r\,e^{-m_Dr}dr=-Q$: perfect screening. (b) $B=\frac Q2(1+m_Dr)e^{-m_Dr}\,x/r^3$, so $\Phi(R)=2\pi Q(1+m_DR)e^{-m_DR}$, which is $2\pi$ times the enclosed charge $Q+\int_{r<R}\rho_{\rm ind}=Q(1+m_DR)e^{-m_DR}$. (c) At $\beta=3$: $\lambda_D=116\,a$, $\bar r=116\,a$, about 4 monopoles in a Debye sphere, $\Gamma=0.081$; the linearization holds at the mean separation, but the mean-field step does not, since the cloud contains only a few monopoles. At $\beta=5$: $\lambda_D=1.31\times10^4\,a$, $\bar r=3.24\times10^3\,a$, about 280 monopoles in a Debye sphere, $\Gamma=4.8\times10^{-3}$; both hold. A common failure is to write the energy of one charge with the ordered-pair coefficient $2\pi^2/e^2$, which halves $m_D^2$; perfect screening survives the error, so (a) alone does not detect it.
2. (a) The decisive step is the Gaussian identity: $\langle e^{iq\sigma(x)}e^{-iq\sigma(0)}\rangle_0=e^{-4\pi^2q^2\beta[G_3(0)-G_3(x)]}\to e^{-2q^2S_{\rm mono}}$, so by cluster decomposition $|\langle e^{iq\sigma}\rangle|=e^{-q^2S_{\rm mono}}=\zeta_q\,a_{\rm lat}^3$: the fugacity of a charge-$q$ monopole is the charge-$q$ order parameter of the monopole-free theory. (b) (i) $e^{-2S_{\rm mono}}\big(e^{\pi/e^2|x|}-1\big)\to e^{-2S_{\rm mono}}\,\pi/e^2|x|$, the $1/|x|$ of the massless Goldstone propagator. (ii) With $G_m(r)=e^{-m_Dr}/4\pi r$, the connected function is $|\langle e^{i\sigma}\rangle|^2\big(e^{(\pi/e^2r)e^{-m_Dr}}-1\big)\to|\langle e^{i\sigma}\rangle|^2\,\frac{\pi}{e^2r}\,e^{-m_Dr}$, with $|\langle e^{i\sigma}\rangle|^2=e^{-2S_{\rm mono}}e^{\pi m_D/e^2}$: exponential decay at the rate $m_D$. (c) In both cases σ is localized, by spontaneous choice in (i) and by the cosine in (ii), so the one-point function is nonzero in both. The vacuum degeneracy (a circle against a point), the massless pole against the gap of (b), and whether $U_\alpha$ is topological (F3) distinguish them. A common failure is to read $\langle e^{i\sigma}\rangle\ne0$ in the plasma as spontaneous breaking.
3. (a) The inserted average is the source of Week 8 §4.3 with $\eta=2\pi k/N$ summed over $k$, which projects the dual sum onto $v\equiv0\pmod N$ and leaves the weights of the surviving $v$ unchanged. A site of charge $Nj$ weighs $e^{-N^2j^2S_{\rm mono}}$, so with the vertices $e^{N^2S_{\rm mono}}e^{\pm iN\sigma}$ normal-ordered at the lattice scale the coupling is $\zeta_N=e^{-N^2S_{\rm mono}}/a_{\rm lat}^3$. (b) Every configuration has $Q_V\in N\mathbb{Z}$, so $U_{2\pi j/N}(\partial V)=e^{2\pi ijQ_V/N}=1$ and these operators are topological: the remnant is $\mathbb{Z}_N^{(0)}$, a 0-form symmetry whose charged operators are local, $e^{i\sigma}$ with charge $1\bmod N$, an operator the dynamics never creates alone. (c) $-2\zeta_N\cos N\sigma$ has $N$ minima at $\sigma=2\pi j/N$, $j=0,\dots,N-1$, and near each $-2\zeta_N\cos N\sigma\simeq-2\zeta_N+N^2\zeta_N(\sigma-2\pi j/N)^2$, so $m^2=8\pi^2N^2\zeta_N/e^2$. The $\mathbb{Z}_N$ permutes the vacua, $\langle e^{i\sigma}\rangle\propto e^{2\pi ij/N}$ tells them apart, and $\mathbb{Z}_N^{(0)}$ is spontaneously broken, which a discrete 0-form symmetry can do in $d=3$. A common failure is to take $NS_{\rm mono}$ for the action of a charge-$N$ monopole in place of $N^2S_{\rm mono}$.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block C. Rewritten to the note-quality-template standard on 2026-09-28 (first draft 2026-07-01). Last revised 2026-09-29.*
