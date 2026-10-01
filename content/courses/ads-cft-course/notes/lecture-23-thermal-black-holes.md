---
title: "Lecture 23 — Thermal states, horizons, and two-sided geometry"
type: lecture-notes
edition: "2.2 — rewritten at the AQFT standard"
lecture: 23
semester: 2
week: 6
hours: 3
prerequisites: "Lectures 3, 10, 12, 13 and 16; the Euclidean path integral of a Gibbs state"
status: "rewritten 2026-09-30, pending instructor review; the thermofield double and its modular operator, the Euclidean temperature, the thermodynamics and Euclidean action of AdS–Schwarzschild in every dimension, the BTZ saddles and the time average of a finite-system correlator are exact calculations; the eternal-black-hole duality and the dominance of the least-action saddle are stated with sources"
modified: 2026-09-30
---

# Lecture 23 — Thermal states, horizons, and two-sided geometry

> *A Gibbs state can be written as the restriction of a pure state on two copies of the system, the thermofield double. Israel noticed in 1976 that the maximally extended black hole, with its two exteriors, carries exactly this structure, and Maldacena proposed in 2001 that the eternal black hole in AdS is dual to two conformal field theories in the thermofield double. This lecture develops the two sides of that statement. On the quantum side we compute the modular operator of the thermofield double and find that its flow is the two-sided Killing flow of the black hole. On the gravitational side we obtain the temperature from the regularity of the Euclidean geometry, compute the Euclidean action of AdS–Schwarzschild in every dimension, and derive from it the mass, the Bekenstein–Hawking entropy and the Hawking–Page transition. In three dimensions the two saddles are exchanged by a modular transformation and reproduce Cardy's formula. The lecture closes with Maldacena's version of the information problem: correlators decay forever in the semiclassical black hole, while in any system with a discrete spectrum their time average stays positive.*

## How to use this lecture

**Classroom core, one meeting of three hours.** The history (§1, 10 minutes), the thermofield double and its modular operator (§2, 25 minutes), the eternal black hole and its Euclidean preparation (§3, 15 minutes), and the temperature and thermodynamics of AdS–Schwarzschild (§4, 25 minutes) come before a 10-minute break. After it come the Euclidean action and the Hawking–Page transition (§5, 35 minutes), the BTZ saddles and Cardy's formula (§6, 15 minutes), and late-time correlators (§7, 20 minutes), with 25 minutes for Checkpoints 1 and 2 and Problems 4–6; Problems 1–3 complete the core assignment. These allocations are proposals and have not been tested in class.

**Self-study.** What the two-sided geometry requires beyond entanglement (§8), and Problems 7–12, including the thermodynamics from the action, the boundary terms, the modular exchange of the BTZ saddles and the time average of a correlator.

**Research extension.** The spectral form factor of a random Hamiltonian, the growth of two-sided entanglement, and the late-time contribution of thermal AdS, in Problems 13–15.

**Prerequisites.** Lecture 3 for modular operators in finite dimensions, Lecture 10 for the KMS condition and the Unruh modes, Lecture 12 for Cardy's formula, Lecture 13 for global AdS, Lecture 16 for the BTZ black hole and $c=3L/2G_N$. The Euclidean path integral of a Gibbs state.

**What this lecture establishes.** The modular operator of the thermofield double and its two-sided flow, the Euclidean temperature of a static black hole, the thermodynamics of AdS–Schwarzschild in every dimension obtained from its Euclidean action, the Hawking–Page temperature, the exchange of the BTZ saddles by $\beta\to4\pi^2L^2/\beta$, and the time average of a correlator in a system with discrete spectrum are exact calculations. The duality between the eternal black hole and the thermofield double, the rule that the saddle of least action dominates at large $N$, and the interpretation of the transition as deconfinement are stated with sources.

## 0. Reading

**Primary.**

- J. M. Maldacena, [Eternal Black Holes in AdS](https://arxiv.org/abs/hep-th/0106112) (2001).
- E. Witten, [Anti-de Sitter Space, Thermal Phase Transition, And Confinement In Gauge Theories](https://arxiv.org/abs/hep-th/9803131) (1998).
- S. W. Hawking, D. N. Page, *Thermodynamics of black holes in anti-de Sitter space*, Commun. Math. Phys. 87 (1983) 577.

**Secondary.**

- G. W. Gibbons, S. W. Hawking, *Action integrals and partition functions in quantum gravity*, Phys. Rev. D 15 (1977) 2752.
- W. Israel, *Thermo-field dynamics of black holes*, Phys. Lett. A 57 (1976) 107.
- M. Bañados, C. Teitelboim, J. Zanelli, [The Black Hole in Three Dimensional Space Time](https://arxiv.org/abs/hep-th/9204099) (1992), and M. Bañados, M. Henneaux, C. Teitelboim, J. Zanelli, [Geometry of the 2+1 Black Hole](https://arxiv.org/abs/gr-qc/9302012) (1993).
- A. Strominger, [Black Hole Entropy from Near-Horizon Microstates](https://arxiv.org/abs/hep-th/9712251) (1997).

**Optional research reading.**

- G. T. Horowitz, V. E. Hubeny, [Quasinormal Modes of AdS Black Holes and the Approach to Thermal Equilibrium](https://arxiv.org/abs/hep-th/9909056) (1999), and D. Birmingham, I. Sachs, S. N. Solodukhin, [Conformal Field Theory Interpretation of Black Hole Quasi-normal Modes](https://arxiv.org/abs/hep-th/0112055) (2001).
- J. L. F. Barbón, E. Rabinovici, [Very Long Time Scales and Black Hole Thermal Equilibrium](https://arxiv.org/abs/hep-th/0308063) (2003), and J. S. Cotler et al., [Black Holes and Random Matrices](https://arxiv.org/abs/1611.04650) (2016).
- T. Hartman, C. A. Keller, B. Stoica, [Universal Spectrum of 2d Conformal Field Theory in the Large c Limit](https://arxiv.org/abs/1405.5137) (2014).
- M. Van Raamsdonk, [Building up spacetime with quantum entanglement](https://arxiv.org/abs/1005.3035) (2010); T. Hartman, J. Maldacena, [Time Evolution of Entanglement Entropy from Black Hole Interiors](https://arxiv.org/abs/1303.1080) (2013); P. Gao, D. L. Jafferis, A. C. Wall, [Traversable Wormholes via a Double Trace Deformation](https://arxiv.org/abs/1608.05687) (2016).

## 1. What does a thermal density matrix hide?

In 1972 Bekenstein proposed that a black hole carries an entropy proportional to the area of its horizon, and two years later Hawking found that black holes radiate at the temperature $T=\kappa/2\pi$, fixed by the surface gravity $\kappa$, which set the coefficient: $S=A/4G_N$. The thermal character of the radiation had an origin that became clear through two papers of 1976. Hartle and Hawking derived the radiation from a path integral continued to imaginary time, and Israel observed that the maximally extended Schwarzschild spacetime, with two exteriors joined through the horizon, realizes the thermofield dynamics that Takahashi and Umezawa had introduced the year before: a thermal state obtained as the restriction of a pure state on a doubled system. In 1977 Gibbons and Hawking turned the Euclidean continuation into a method. The partition function of a gravitational system is a path integral over Euclidean geometries with a circle of length $\beta$ at infinity, and the classical action of the black-hole saddle already knows its free energy and its entropy.

In anti-de Sitter space the method has a sharper outcome. Hawking and Page showed in 1983 that large AdS black holes have positive specific heat and that, above a temperature of the order of the inverse AdS radius, the black hole has a lower action than a gas of radiation in empty AdS, so that the canonical ensemble undergoes a first-order transition. Witten recognized in 1998 that in $\mathcal N=4$ super Yang–Mills theory on a sphere this is the transition between a confined phase, with a free energy of order one, and a deconfined phase, with a free energy of order $N^2$. In three dimensions Bañados, Teitelboim and Zanelli had found black holes in 1992, and Strominger reproduced their entropy in 1997 from Cardy's formula with the Brown–Henneaux central charge. Maldacena then proposed in 2001 that the eternal AdS black hole is dual to two copies of the conformal field theory in the thermofield double, and he used the duality to state a version of the information problem that survives in equilibrium.

This lecture follows that sequence. The quantum statements come first, since they hold in any system, and the gravitational statements are then calculations with one classical geometry and its Euclidean action.

## 2. Purify a Gibbs state

Consider a system with Hamiltonian $H$, energy eigenstates $H|n\rangle=E_n|n\rangle$, and a second copy obtained with an antiunitary map $\Theta$, so that $|\bar n\rangle=\Theta|n\rangle$ and $H_L=\Theta H\Theta^{-1}$ satisfy $H_L|\bar n\rangle=E_n|\bar n\rangle$. The thermofield double is

$$
|\mathrm{TFD}_\beta\rangle=\frac1{\sqrt{Z(\beta)}}\sum_ne^{-\beta E_n/2}\,|n\rangle_R\,|\bar n\rangle_L,
\qquad
Z(\beta)=\sum_ne^{-\beta E_n},
$$

where the labels $R$ and $L$ anticipate the right and left exteriors of the black hole. The restriction to the right copy is the Gibbs state, $\rho_R=e^{-\beta H_R}/Z$, and the restriction to the left copy is $\rho_L=e^{-\beta H_L}/Z$. Note that the antiunitary map fixes the phases of the pairing, and with it the correlations between the two copies; a different pairing produces another purification of the same Gibbs state (§8).

The Schmidt coefficients are $\sqrt{p_n}$ with $p_n=e^{-\beta E_n}/Z$, all positive when the spectrum is discrete and $Z(\beta)$ is finite, so the vector is cyclic and separating for the algebra of each copy. Lecture 3 computed the modular operator of such a vector,

$$
\Delta=\rho_R\otimes\rho_L^{-1}=e^{-\beta(H_R-H_L)},
\qquad
\widehat K=-\log\Delta=\beta\,(H_R-H_L),
$$

and the modular flow of the conventions sheet acts on the two algebras as

$$
\Delta^{-is}A_R\,\Delta^{is}=e^{i\beta sH_R}A_Re^{-i\beta sH_R},
\qquad
\Delta^{-is}A_L\,\Delta^{is}=e^{-i\beta sH_L}A_Le^{i\beta sH_L}.
$$

[Exact.] The flow advances the right copy by the physical time $\beta s$ and moves the left copy backward by the same amount. Its generator annihilates the state, $(H_R-H_L)|\mathrm{TFD}\rangle=0$, since each term of the sum is multiplied by $e^{-i(E_n-E_n)t}=1$. The correlators $F(s)=\langle A_R\,\Delta^{-is}B_R\Delta^{is}\rangle$ satisfy the KMS condition of Lecture 10 in the upper strip, which is the statement that the right copy alone is in equilibrium at temperature $1/\beta$.

But moving both copies forward is a different operation. The operator $e^{-i(H_R+H_L)t}$ multiplies each term by $e^{-2iE_nt}$, and the overlap with the initial state is

$$
\langle\mathrm{TFD}_\beta|e^{-i(H_R+H_L)t}|\mathrm{TFD}_\beta\rangle=\frac{Z(\beta+2it)}{Z(\beta)} ,
$$

an analytically continued partition function whose modulus starts at one and never exceeds it. [Exact.] The square of its modulus is the spectral form factor at time $2t$, which returns in §7 and in Problem 13. The reduced states of the two copies are unchanged by this evolution, while their correlations change; in the black hole the change is the growth of the interior along the slices that join the two boundaries at equal times, which Hartman and Maldacena related to the linear growth of two-sided entanglement.

For a harmonic oscillator of frequency $\omega$, with $q=e^{-\beta\omega}$,

$$
|\mathrm{TFD}\rangle=\sqrt{1-q}\,\sum_{n=0}^\infty q^{n/2}|n\rangle_R|n\rangle_L,
\qquad
\bar n=\frac q{1-q},
\qquad
S(\rho_R)=(\bar n+1)\log(\bar n+1)-\bar n\log\bar n ,
$$

where $\bar n$ is the mean occupation. This two-mode squeezed state is the one that Lecture 10 found for each pair of Unruh modes in the two Rindler wedges, with $q=e^{-2\pi\omega/a}$, and it is the state of each Hawking pair in Lecture 24.

**Checkpoint 1.** The right Hamiltonian $H_R$ generates a symmetry of the right algebra that preserves $\rho_R$. Why does $e^{-iH_Rt}$ alone change the thermofield double?

**Answer.** It multiplies each term by $e^{-iE_nt}$, which changes the relative phases of the pairs and with them the two-sided correlations. Among the combinations $aH_R+bH_L$, only the multiples of $H_R-H_L=\widehat K/\beta$ leave every term invariant.

## 3. The eternal black hole

Consider a static metric

$$
ds^2=-f(r)\,dt^2+\frac{dr^2}{f(r)}+r^2d\Omega_{d-1}^2,
$$

where $f$ has a simple zero at the horizon $r_+$, with $f'(r_+)=2\kappa$. The tortoise coordinate $r_*=\int dr/f$ tends to $-\infty$ at the horizon, and the null coordinates $U=-e^{-\kappa(t-r_*)}$ and $V=e^{\kappa(t+r_*)}$ cover the exterior as the quadrant $U<0<V$. The metric is regular across $U=0$ and $V=0$ in these coordinates, and its maximal extension contains four regions: the right exterior, a left exterior with $U>0>V$, and a future and a past interior. For the nonrotating BTZ black hole of Lecture 16 the extension is explicit,

$$
ds^2=\frac{-4L^2\,dU\,dV+r_+^2\,(1-UV)^2\,d\varphi^2}{(1+UV)^2},
\qquad
r=r_+\,\frac{1-UV}{1+UV},
$$

with the boundary at $UV=-1$ and the singularity $r=0$ at $UV=1$. [Exact calculation, checked symbolically.] The time translation $t\to t+\eta$ acts as $U\to e^{-\kappa\eta}U$, $V\to e^{\kappa\eta}V$. It moves the right exterior toward the future and the left exterior toward the past, and it fixes the bifurcation surface $U=V=0$: the boost of the Kruskal plane, with the same orientation as the modular flow of §2.

![[ads-cft-thermal-black-holes.svg|Left: the Penrose diagram of the nonrotating BTZ black hole, a square with the two boundaries as vertical sides, the singularities at top and bottom, and the horizons as diagonals, with Killing orbits running upward in the right exterior and downward in the left exterior and the t equal to zero slice across the bridge. Center: the free energy of AdS5–Schwarzschild relative to thermal AdS as a function of temperature, with the small and large black-hole branches meeting at the minimum temperature and the large branch crossing zero at the Hawking–Page temperature. Right: the normalized correlator of a finite system of dimension 1200 on logarithmic axes, following an exponential decay and then fluctuating about the root-mean-square value of its exact time average.]]

The Euclidean continuation $t=-i\tau$ explains why the two exteriors belong to one state. The thermofield double is prepared by the Euclidean evolution over half the thermal circle,

$$
\langle m|_R\,\langle\bar n|_L\,\mathrm{TFD}_\beta\rangle=\frac{1}{\sqrt{Z}}\,\langle m|e^{-\beta H/2}|n\rangle ,
$$

that is, its wavefunction is a path integral on an interval of Euclidean time $\beta/2$ whose two ends are the two copies. In gravity the corresponding saddle is half of the Euclidean black hole, whose $(r,\tau)$ plane is a disk with the horizon at the center. The boundary of the half disk is the diameter $\tau\in\{0,\beta/2\}$, which passes through the center and continues to the $t=0$ slice of the Lorentzian geometry: the Einstein–Rosen bridge joining the two exteriors. Maldacena proposed that the two conformal field theories in the thermofield double are exactly dual to the eternal AdS black hole, with the modular flow of §2 dual to the Killing flow. [Stated only — refs: Israel 1976; Maldacena 2001.] For AdS–Schwarzschild in more than three dimensions the Penrose diagram is no longer a square, since the singularities bow inward, but the causal structure of the exteriors, the horizons and the bifurcation surface is the same.

> **Physical picture: one state, two clocks.** An observer outside each boundary measures the Gibbs state and has no access to the other copy. The two copies are entangled pair by pair, and the geometry records the entanglement as a connected spatial slice. The symmetry of the state is the boost of the Kruskal plane, forward on one side and backward on the other; evolving both boundaries forward stretches the bridge. The duality is a conjecture about specific holographic theories. The quantum statements of §2, including the two-sided modular flow, hold for any system with a discrete spectrum.

## 4. Temperature from regularity, and the thermodynamics of AdS–Schwarzschild

Near a simple zero of $f$, set $r-r_+=\kappa\rho^2/2$. The Euclidean metric in the $(r,\tau)$ plane becomes

$$
d\rho^2+\kappa^2\rho^2\,d\tau^2 ,
$$

where corrections are of order $\rho^2$ relative to these terms. The plane is smooth at $\rho=0$ only if $\kappa\tau$ has period $2\pi$; any other period leaves a conical singularity. Therefore

$$
\beta=\frac{2\pi}\kappa=\frac{4\pi}{f'(r_+)} .
$$

[Exact.] The temperature at infinity of a smooth Euclidean black hole is fixed by its geometry, and it coincides with Hawking's $T=\kappa/2\pi$.

Consider now the AdS–Schwarzschild black hole in $d+1$ dimensions,

$$
f(r)=1+\frac{r^2}{L^2}-\frac{\mu}{r^{d-2}},
\qquad
\mu=r_+^{d-2}\left(1+\frac{r_+^2}{L^2}\right),
$$

where the second relation expresses the mass parameter through the horizon radius. Its temperature is

$$
T=\frac{d\,r_+^2+(d-2)L^2}{4\pi L^2\,r_+} .
$$

[Exact calculation, checked symbolically for $d=2,\dots,5$.] For $d\geq3$ the temperature diverges both as $r_+\to0$ and as $r_+\to\infty$ and has a minimum,

$$
T_{\min}=\frac{\sqrt{d(d-2)}}{2\pi L}\qquad\text{at}\qquad r_+=L\sqrt{\frac{d-2}d}.
$$

Below $T_{\min}$ no black hole exists; above it there are two, a small one with $r_+<L\sqrt{(d-2)/d}$ and a large one. For instance, in $d=2$ the formula gives the BTZ temperature $T=r_+/2\pi L^2$ with a single branch.

The mass and the entropy follow from the Euclidean action in the next section, and they are

$$
M=\frac{(d-1)\,\Omega_{d-1}\,\mu}{16\pi G_N},
\qquad
S=\frac{\Omega_{d-1}\,r_+^{d-1}}{4G_N}=\frac{A}{4G_N},
$$

where $\Omega_{d-1}$ is the volume of the unit sphere and $M$ is measured from thermal AdS. One checks the first law $dM=T\,dS$ directly: both sides equal $\frac{(d-1)\Omega_{d-1}}{16\pi G_N}\bigl(d\,r_+^{d-1}/L^2+(d-2)\,r_+^{d-3}\bigr)dr_+$ (Problem 7). The specific heat $dM/dT$ has the sign of $dT/dr_+$, negative on the small branch, as for a Schwarzschild black hole in flat space, and positive on the large branch. The AdS boundary acts as a box, and a black hole with $r_+>L\sqrt{(d-2)/d}$, comparable to the AdS radius, heats up when it gains energy.

## 5. The Euclidean action and the Hawking–Page transition

Gibbons and Hawking identified the partition function with the gravitational path integral at fixed boundary data, $Z(\beta)\simeq\sum e^{-I}$ over the saddles, so that the free energy of the dominant saddle is $F=I/\beta$. The Euclidean action is

$$
I=-\frac1{16\pi G_N}\int d^{d+1}x\,\sqrt g\,\bigl(R-2\Lambda\bigr)-\frac1{8\pi G_N}\int d^dx\,\sqrt h\,K+\cdots,
\qquad
\Lambda=-\frac{d(d-1)}{2L^2},
$$

where the dots are the counterterms of holographic renormalization, and we compute the difference between the black hole and thermal AdS, the geometry with $\mu=0$ and a periodic Euclidean time. On a solution $R=-d(d+1)/L^2$, so the bulk integrand is constant,

$$
-\frac1{16\pi G_N}\left(R-2\Lambda\right)=\frac{d}{8\pi G_N L^2},
$$

and the bulk action is proportional to the regulated volume. Cut both geometries at $r=R_c$. The metric determinant is $r^{d-1}$ times the sphere, so the black hole has volume $\beta\,\Omega_{d-1}(R_c^d-r_+^d)/d$, since its Euclidean geometry ends at the horizon, and thermal AdS has volume $\beta'\,\Omega_{d-1}R_c^d/d$. The period $\beta'$ is fixed by requiring the same proper length of the thermal circle at the cutoff, $\beta'\sqrt{1+R_c^2/L^2}=\beta\sqrt{f(R_c)}$, which gives $\beta'=\beta\bigl(1-\mu L^2/2R_c^d+\cdots\bigr)$. Therefore

$$
I_{\mathrm{BH}}-I_{\mathrm{AdS}}
=\frac{\beta\,\Omega_{d-1}}{8\pi G_NL^2}\left(-r_+^d+\frac{\mu L^2}2\right)
=\frac{\beta\,\Omega_{d-1}\,r_+^{d-2}\,(L^2-r_+^2)}{16\pi G_N\,L^2}
$$

as $R_c\to\infty$. The Gibbons–Hawking terms of the two geometries differ by a quantity that vanishes in the limit, and the counterterms cancel between them. [Exact calculation, checked symbolically for $d=2,\dots,5$, including the boundary terms (Problem 9).]

This single function of $r_+$ contains the thermodynamics. With $\beta(r_+)$ from §4, the energy $E=\partial_\beta I$ is the mass $M$ of §4 and the entropy $S=\beta E-I$ is $\Omega_{d-1}r_+^{d-1}/4G_N$, a quarter of the horizon area (Problem 7). The Euclidean action knows the Bekenstein–Hawking entropy without any statement about microstates, which was the observation of Gibbons and Hawking. The free energy relative to thermal AdS is

$$
F=\frac{\Omega_{d-1}\,r_+^{d-2}\,(L^2-r_+^2)}{16\pi G_N\,L^2},
$$

negative exactly when $r_+>L$. The black hole with $r_+=L$ has the temperature

$$
T_{\mathrm{HP}}=\frac{d-1}{2\pi L} ,
$$

and since $(d-1)^2>d(d-2)$, the Hawking–Page temperature lies above $T_{\min}$. Below $T_{\min}$ only thermal AdS exists. Between $T_{\min}$ and $T_{\mathrm{HP}}$ the large black hole exists and is locally stable, but thermal AdS has the lower action. Above $T_{\mathrm{HP}}$ the large black hole dominates. [Exact calculation for the actions; the dominance of the least-action saddle is the leading semiclassical approximation.] The figure shows the two branches in AdS$_5$. The entropy jumps at $T_{\mathrm{HP}}$ from the entropy of a gas of gravitons, of order one, to $A/4G_N$, so the transition is of first order.

In fact, in the dual theory $L^{d-1}/G_N$ counts the degrees of freedom; for $\mathcal N=4$ super Yang–Mills it is proportional to $N^2$. Witten identified the phase above $T_{\mathrm{HP}}$, with a free energy of order $N^2$, as deconfined, and the phase below it, with a free energy of order one, as confined. The order parameter is the Polyakov loop around the thermal circle. Its expectation value vanishes in thermal AdS, where the circle is not contractible in the bulk and no string worldsheet can end on it, and it is nonzero in the black-hole phase, where the circle bounds a disk. [Stated only — refs: Witten 1998.] For a large black hole with $r_+\gg L$, the entropy grows as $r_+^{d-1}\propto T^{d-1}$, the scaling of a thermal gas in a conformal field theory on the sphere, which is how the duality makes the entropy of a large AdS black hole extensive in the boundary volume.

**Checkpoint 2.** Between $T_{\min}$ and $T_{\mathrm{HP}}$ the large black hole has positive specific heat. Why is it nevertheless not the equilibrium state of the canonical ensemble?

**Answer.** Local stability compares the black hole with nearby black holes. The canonical ensemble compares all saddles with the same boundary data, and in this range thermal AdS has the smaller Euclidean action, so it dominates the partition function by a factor $e^{-\Delta I}$ with $\Delta I$ of order $N^2$.

## 6. BTZ: two saddles related by a modular transformation

In three dimensions the general formulas give $f=(r^2-r_+^2)/L^2$ once $\mu=1+r_+^2/L^2$, and thermal AdS$_3$ is global AdS, whose mass $-1/8G_N$ is the Casimir energy of the boundary circle. With $r_+=2\pi L^2/\beta$, the action difference is

$$
I_{\mathrm{BTZ}}-I_{\mathrm{AdS}}=\frac{\beta\,(L^2-r_+^2)}{8G_NL^2}=\frac{c}{12}\left(\frac\beta L-\frac{4\pi^2L}\beta\right),
$$

where $c=3L/2G_N$. Thermal AdS contributes $\log Z_{\mathrm{AdS}}=\frac c{12}\frac\beta L$, the vacuum energy $-c/12L$ of a circle of circumference $2\pi L$ times $\beta$, and therefore

$$
\log Z_{\mathrm{BTZ}}=\frac c{12}\,\frac{4\pi^2L}{\beta} .
$$

[Exact calculation.] The two saddles are exchanged by $\beta\to4\pi^2L^2/\beta$, the modular transformation that inverts the modular parameter of the boundary torus, which exchanges the contractible and the noncontractible cycles in the bulk solid torus. The transition occurs at the self-dual point $\beta=2\pi L$, $T_{\mathrm{HP}}=1/2\pi L$, as the general formula predicts for $d=2$. Above it,

$$
S=\left(1-\beta\partial_\beta\right)\log Z_{\mathrm{BTZ}}=\frac{2\pi^2c}{3}\,L\,T=\frac{\pi r_+}{2G_N}=\frac{2\pi r_+}{4G_N},
$$

which is Cardy's formula of Lecture 12 for a circle of circumference $2\pi L$ and the Bekenstein–Hawking entropy of the BTZ horizon. Strominger's derivation used the asymptotic Virasoro symmetry and Cardy's formula at high temperature. Hartman, Keller and Stoica showed that in a conformal field theory with large $c$ and a sparse spectrum of light operators the free energy equals the larger of the two expressions at every temperature. [Stated only — refs: Strominger 1997; Hartman–Keller–Stoica 2014.]

## 7. Late times: decay against recurrence

Maldacena used the thermofield double to formulate a version of the information problem that needs no evaporation. Consider a probe field in the black hole and its two-point function at late times. In the bulk the field falls through the horizon, and the correlator decays exponentially, governed by the quasinormal frequencies of Horowitz and Hubeny. For the planar BTZ black hole the decay is exact. A scalar primary of dimension $\Delta$ in a two-dimensional conformal field theory on a line at temperature $1/\beta$ has, after the map $z=e^{2\pi w/\beta}$ from the plane,

$$
G(t)=\bigl\langle\mathcal O(t,0)\,\mathcal O(0,0)\bigr\rangle_\beta=\left(\frac\pi\beta\right)^{2\Delta}\Bigl[i\sinh\!\bigl(\pi(t-i\epsilon)/\beta\bigr)\Bigr]^{-2\Delta},
\qquad
|G(t)|\longrightarrow\left(\frac{2\pi}{\beta}\right)^{2\Delta}e^{-2\pi\Delta t/\beta},
$$

where the $i\epsilon$ orders the operators, the power is taken on the principal branch, and the limit is $t\gg\beta$. [Exact calculation (Problem 11).] Birmingham, Sachs and Solodukhin matched the poles of the corresponding retarded function with the quasinormal frequencies of BTZ.

Now take any system with a discrete spectrum, such as a conformal field theory on a circle at finite $N$. In the energy basis,

$$
G(t)=\sum_{m,n}p_m\,|\mathcal O_{mn}|^2\,e^{i(E_m-E_n)t},
$$

where $p_m=e^{-\beta E_m}/Z$ and $\mathcal O_{mn}=\langle m|\mathcal O|n\rangle$. This is a quasi-periodic function of time. If the gaps are nondegenerate, so that $E_m-E_n=E_{m'}-E_{n'}$ only for $(m,n)=(m',n')$ or $m=n$, $m'=n'$, its long-time average is

$$
\lim_{\mathcal T\to\infty}\frac1{\mathcal T}\int_0^{\mathcal T}|G(t)|^2\,dt=\sum_{m\neq n}p_m^2\,|\mathcal O_{mn}|^4+\Bigl(\sum_mp_m\,|\mathcal O_{mm}|^2\Bigr)^2 ,
$$

a positive number unless $\mathcal O$ vanishes (Problem 12). [Exact.] For an operator with $\langle\mathcal O\rangle_\beta=0$ whose matrix elements are spread over the thermal window, as in a chaotic system, each $|\mathcal O_{mn}|^2$ is of order $e^{-S}$, and the average is of order $e^{-2S}$ relative to $|G(0)|^2$. [Heuristic.] The correlator cannot decay forever: $|G(t)/G(0)|$ decays to a plateau of order $e^{-S}$ and fluctuates about it, and at much later times it returns arbitrarily close to its initial value. The figure shows a finite model with dimension $1200$ and matrix elements chosen to decay as $e^{-\Gamma t}$ at early times; the decay stops at the root-mean-square value of the exact time average, which halves when the dimension doubles.

But the semiclassical bulk, whose correlators decay through quasinormal modes as if the spectrum were continuous, misses an effect of order $e^{-S}$ in the correlator. Maldacena suggested that the discrepancy is resolved by other saddles of the gravitational path integral, such as thermal AdS, whose contribution does not decay. Barbón and Rabinovici found that the thermal AdS saddle indeed restores the time-averaged bound, while the time dependence of the recurrences requires further configurations. [Stated only — refs: Maldacena 2001; Barbón–Rabinovici 2003.] Later work on the spectral form factor attributed the late-time structure to the random-matrix statistics of the spectrum, with a plateau at the value $Z(2\beta)/Z(\beta)^2$ (Problem 13). The lesson for the rest of the semester is the order of magnitude: a single classical geometry reproduces coarse-grained thermal physics at leading order and misses effects of order $e^{-S}$, and those effects decide questions about information. Lectures 25–27 will find a second saddle that changes an entropy at leading order in $1/G_N$.

## 8. Self-study: what the two-sided geometry requires

The entanglement between the two copies is fixed by the Schmidt coefficients, and a unitary $V_L$ acting on the left copy alone preserves it: $\rho_R$ is unchanged. The state $V_L|\mathrm{TFD}\rangle$ has the same spectrum of $\rho_R$, and in general very different two-sided correlators. Only special purifications, prepared by a Euclidean path integral or by a short time evolution from it, have the smooth geometry of the eternal black hole; a generic unitary on one side produces a state whose bulk description, if it has one, contains matter or shock waves behind the horizon. [Heuristic.] Entanglement is necessary for the bridge, and Van Raamsdonk argued from the mutual information and the Ryu–Takayanagi formula that decreasing it pinches the geometry apart. [Heuristic — refs: Van Raamsdonk 2010.]

Note that the bridge cannot be traversed while the two theories are decoupled. For an operation on the right with Kraus operators $\{K_i\}$ and any left observable $A_L$,

$$
\sum_i\langle\psi|K_i^\dagger A_L\,K_i|\psi\rangle=\langle\psi|A_L\,\textstyle\sum_iK_i^\dagger K_i|\psi\rangle=\langle\psi|A_L|\psi\rangle,
$$

since $A_L$ commutes with every $K_i$. [Proved.] No choice on the right changes a left expectation value, whatever the entanglement. Gao, Jafferis and Wall showed that a coupling between the two boundaries, of the double-trace form $e^{ig\,\mathcal O_L\mathcal O_R}$, produces negative averaged null energy in the bulk and makes the wormhole traversable; the signal then goes through the coupling. [Stated only — refs: Gao–Jafferis–Wall 2016.]

## 9. What to take away

- **Exact:** the modular operator of the thermofield double is $e^{-\beta(H_R-H_L)}$, and its flow advances the right copy and moves the left copy backward, as the boost of the Kruskal plane does; evolution with $H_R+H_L$ has the return amplitude $Z(\beta+2it)/Z(\beta)$.
- **Exact calculation:** the temperature of a smooth Euclidean black hole is $4\pi/f'(r_+)$; for AdS–Schwarzschild the Euclidean action $\beta\Omega_{d-1}r_+^{d-2}(L^2-r_+^2)/16\pi G_NL^2$ gives the mass, the entropy $A/4G_N$ and the Hawking–Page temperature $(d-1)/2\pi L$.
- **Exact calculation:** the two BTZ saddles are exchanged by $\beta\to4\pi^2L^2/\beta$, and the black-hole saddle reproduces Cardy's formula; for a large-$c$ theory with a sparse light spectrum this is the free energy at every temperature (stated).
- **Exact:** in any system with discrete spectrum the time average of $|G(t)|^2$ is positive; for a chaotic system it is of order $e^{-2S}$ (a heuristic estimate), while the semiclassical black hole gives exponential decay forever.
- **Stated only:** the eternal AdS black hole is dual to the thermofield double of two conformal field theories, and the Hawking–Page transition is the deconfinement transition of the dual gauge theory.

## 10. Looking ahead

Lecture 24 turns from equilibrium to evaporation. Hawking's calculation produces pairs in the two-mode squeezed state of §2, one partner outside and one inside, and the entropy of the radiation grows without bound; Page's analysis of random states shows what unitarity requires instead, and the model of Hayden and Preskill shows how fast information can return. Lectures 25–27 then calculate the entropy of radiation in a specified gravitational model and find the second saddle. Lecture 29 returns to the thermofield double above the Hawking–Page temperature, where Leutheusser and Liu argue that the algebra of single-trace operators of one boundary becomes a type III$_1$ factor at large $N$. The continuous spectrum behind the decay of §7 is a symptom of that limit, and Lecture 29 explains what more the classification requires.

## 11. Problem set

### Classroom core

1. **The oscillator double.** Normalize the oscillator thermofield double, compute $\bar n$ and $S(\rho_R)$, and check that $S\to\log(1/\beta\omega)+1$ at high temperature.

2. **Two-sided modular flow.** Verify $\Delta^{-is}A_R\Delta^{is}=e^{i\beta sH_R}A_Re^{-i\beta sH_R}$ and $\Delta^{-is}A_L\Delta^{is}=e^{-i\beta sH_L}A_Le^{i\beta sH_L}$ for $\Delta=\rho_R\otimes\rho_L^{-1}$.

3. **The return amplitude.** Show that $\langle\mathrm{TFD}|e^{-i(H_R+H_L)t}|\mathrm{TFD}\rangle=Z(\beta+2it)/Z(\beta)$, and evaluate it for the oscillator.

4. **Euclidean regularity.** Derive $\beta=4\pi/f'(r_+)$ from the near-horizon metric, apply it to AdS–Schwarzschild, and find $T_{\min}$.

5. **Volume subtraction.** Derive $I_{\mathrm{BH}}-I_{\mathrm{AdS}}$ from the regulated volumes and the matching of periods.

6. **The Hawking–Page temperature.** Show that the free energy changes sign at $r_+=L$, compute $T_{\mathrm{HP}}$, and verify $T_{\mathrm{HP}}>T_{\min}$ for $d\geq3$.

### Self-study consolidation

7. **Thermodynamics from the action.** From $I(\beta)$, compute $E=\partial_\beta I$ and $S=\beta E-I$, and check $dM=T\,dS$.

8. **Specific heat.** Show that $dM/dT$ is negative on the small branch and positive on the large one, and find where it diverges.

9. **Boundary terms.** For $f$ and matched periods, show that $\int\sqrt h\,K$ differs between the black hole and thermal AdS by a quantity that vanishes as $R_c\to\infty$.

10. **Modular exchange.** Compute $\log Z_{\mathrm{BTZ}}$ and $\log Z_{\mathrm{AdS}}$ in terms of $c$, show that they are exchanged by $\beta\to4\pi^2L^2/\beta$, and derive the Cardy entropy.

11. **The thermal correlator.** Map the plane correlator $|z_1-z_2|^{-2\Delta}$ of a scalar primary to the thermal cylinder with $z=e^{2\pi w/\beta}$, continue to real time, and obtain the decay rate $2\pi\Delta/\beta$.

12. **The time average.** Derive the long-time average of $|G(t)|^2$ for nondegenerate gaps, and explain why it is positive.

### Research extension

13. **Spectral form factor.** For a random Hamiltonian from the Gaussian unitary ensemble, compute $|Z(\beta+it)|^2/Z(\beta)^2$ numerically and identify its initial decay, the linear ramp and the plateau at $Z(2\beta)/Z(\beta)^2$. *Known:* Cotler and collaborators found this structure in the SYK model and conjectured it for large AdS black holes. *Completion:* the three regimes for dimension $1000$, with the time at which the plateau begins compared with the inverse mean level spacing.

14. **Two-sided entanglement growth.** For two conformal field theories on lines in the thermofield double, compute the entropy of the union of the two half-lines $x>b$ on both sides after evolving both forward by $t$. *Known:* Hartman and Maldacena found linear growth at late times, reproduced by a geodesic through the interior of planar BTZ. *Completion:* the result $\frac c3\log\cosh\frac{2\pi t}\beta$ up to a constant, from both the boundary and the bulk; Lecture 26 uses it.

15. **The thermal AdS contribution.** Estimate the late-time value of the correlator from the sum of the black-hole and thermal-AdS saddles, and compare with the time average of §7. *Known:* Barbón and Rabinovici showed that the second saddle restores the time-averaged bound and does not reproduce the recurrences. *Completion:* the two estimates as functions of $N$ and $T$ for $\mathcal N=4$ super Yang–Mills above the Hawking–Page temperature, with the continuum estimate of the bound used by Barbón and Rabinovici compared with the counting of §7 under nondegenerate gaps.

## 12. Answer checkpoints

1. $(1-q)\sum_nq^n=1$. Differentiating the geometric series gives $\bar n=\sum_nn(1-q)q^n=q/(1-q)$. At high temperature $\bar n\simeq1/\beta\omega$ and $(\bar n+1)\log(\bar n+1)-\bar n\log\bar n=\log\bar n+1+O(1/\bar n)$.

2. $\Delta^{-is}=\rho_R^{-is}\otimes\rho_L^{is}=e^{i\beta sH_R}\otimes e^{-i\beta sH_L}$ up to scalar factors that cancel. The right factor acts on $A_R$ and the left one on $A_L$, with opposite signs.

3. Each term acquires $e^{-2iE_nt}$, so the overlap is $\sum_np_ne^{-2iE_nt}=Z(\beta+2it)/Z(\beta)$. For the oscillator, with zero-point energy omitted, $(1-q)/(1-qe^{-2i\omega t})$, of modulus $(1-q)/\sqrt{1-2q\cos2\omega t+q^2}$, which returns to one at $t=\pi/\omega$.

4. With $r-r_+=\kappa\rho^2/2$, $f\simeq2\kappa(r-r_+)=\kappa^2\rho^2$ and $dr^2/f=d\rho^2$. Regularity requires $\kappa\beta=2\pi$. For AdS–Schwarzschild $f'(r_+)=\bigl(d\,r_+^2+(d-2)L^2\bigr)/L^2r_+$, and $dT/dr_+=0$ at $r_+^2=(d-2)L^2/d$.

5. The bulk integrand is $d/8\pi G_NL^2$. The volumes are $\beta\Omega(R_c^d-r_+^d)/d$ and $\beta'\Omega R_c^d/d$ with $\beta'\simeq\beta(1-\mu L^2/2R_c^d)$. The difference is $\frac{\beta\Omega}{8\pi G_NL^2}\bigl(-r_+^d+\mu L^2/2\bigr)$, and substituting $\mu$ gives the stated result.

6. $F\propto r_+^{d-2}(L^2-r_+^2)$ changes sign at $r_+=L$, where $T=(2d-2)/4\pi L$. Then $(d-1)^2-d(d-2)=1>0$.

7. $E=\frac{dI/dr_+}{d\beta/dr_+}=\frac{(d-1)\Omega\mu}{16\pi G_N}$ and $\beta E-I=\frac{\Omega r_+^{d-1}}{4G_N}$. Both sides of the first law equal $\frac{(d-1)\Omega}{16\pi G_N}\bigl(dr_+^{d-1}/L^2+(d-2)r_+^{d-3}\bigr)dr_+$.

8. $dM/dr_+>0$ always, and $dT/dr_+=\bigl(d\,r_+^2-(d-2)L^2\bigr)/4\pi L^2r_+^2$ changes sign at the minimum temperature, where the specific heat diverges.

9. $\int\sqrt hK=\beta\Omega\sqrt f\,\partial_r(r^{d-1}\sqrt f)$ at $r=R_c$. With $f_{\mathrm{BH}}=f_{\mathrm{AdS}}-\mu/r^{d-2}$ and $\beta'/\beta\simeq1-\mu/2R_c^{d-2}f_{\mathrm{AdS}}$, the terms of order $\mu$ are $-(d-1)\mu+\frac{d-2}2\mu+\frac d2\mu=0$, and the rest vanishes as $R_c\to\infty$.

10. $\log Z_{\mathrm{AdS}}=\frac c{12}\frac\beta L$ and $\log Z_{\mathrm{BTZ}}=\frac c{12}\frac{4\pi^2L}\beta$; the substitution exchanges them. $S=(1-\beta\partial_\beta)\log Z_{\mathrm{BTZ}}=\frac{2\pi^2cL}{3\beta}$.

11. On the cylinder, $|z_1-z_2|^{-2\Delta}|z_1'z_2'|^{\Delta}$ gives $\bigl(\frac{\pi}{\beta}\bigr)^{2\Delta}|\sinh\frac{\pi(w_1-w_2)}\beta|^{-2\Delta}$ for $h=\bar h=\Delta/2$. At equal positions $w_1-w_2=i\tau$ and $\sinh(i\pi\tau/\beta)=i\sin(\pi\tau/\beta)$, so $G_E(\tau)=\bigl(\pi/\beta\sin(\pi\tau/\beta)\bigr)^{2\Delta}$. The continuation $\tau=\epsilon+it$ gives $\sin\bigl(\pi(\epsilon+it)/\beta\bigr)=i\sinh\bigl(\pi(t-i\epsilon)/\beta\bigr)$, whose modulus grows as $\frac12e^{\pi t/\beta}$.

12. The average of $e^{i(E_m-E_n-E_{m'}+E_{n'})t}$ is one on the resonant pairs and zero otherwise. The two resonant families overlap at $m=n=m'=n'$, which is counted once. Each term is nonnegative, and the diagonal sum vanishes only if every $\mathcal O_{mn}$ with $p_m>0$ vanishes.

**Wiki connections.** [[thermofield-double-state|thermofield double]] · [[er-epr|ER=EPR]] · [[traversable-wormholes|traversable wormholes]]
