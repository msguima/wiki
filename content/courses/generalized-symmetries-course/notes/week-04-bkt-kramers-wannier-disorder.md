---
title: "Week 4 — BKT, Kramers–Wannier, and the First Disorder Operators"
type: lecture-notes
course: syllabus
semester: 1
week: 4
block: A
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 1–3 (XY model, cochains, the exact Coulomb-gas duality); the 2d Ising model; elementary RG language
modified: 2026-07-07
---

# Week 4 — BKT, Kramers–Wannier, and the First Disorder Operators

> *Two stories close Block A, and they are secretly one. First: the Coulomb gas built in Week 3 ionizes — the Berezinskii–Kosterlitz–Thouless transition — and its renormalization group yields two predictions no Landau theory could produce: a universal jump in the stiffness and an essential singularity in the correlation length. Second: the 2d Ising model equals itself at the dual temperature — Kramers–Wannier — and the operator implementing the equality, the Kadanoff–Ceva disorder operator, is our first symmetry object living on an extended seam. Block A ends with the sentence the whole course elaborates: a duality is a statement about a wall.*

## 0. Reading

**Primary:** Kosterlitz & Thouless, *J. Phys. C* 6 (1973) 1181; Kosterlitz, *J. Phys. C* 7 (1974) 1046 (the RG). Kramers & Wannier, *Phys. Rev.* 60 (1941) 252. Kadanoff & Ceva, *Phys. Rev. B* 3 (1971) 3918.

**Secondary:**
- Kardar, *Statistical Physics of Fields*, §8.2–8.6 — the RG derivation in conventions matching ours.
- Nelson & Kosterlitz, *Phys. Rev. Lett.* 39 (1977) 1201 — the universal jump; Bishop & Reppy, *Phys. Rev. Lett.* 40 (1978) 1727 — its measurement.
- Fradkin, *Field Theories of Condensed Matter Physics*, 2nd ed., ch. 3 — order/disorder operators in the language Semester II uses.

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]]. Inputs from [[week-03-villain-form-xy-duality|Week 3]]: the Coulomb gas with (long-distance) fugacity $y = e^{-2\pi^2\beta\kappa}$, and the vortex-operator dimension $\Delta_{\rm vortex} = \pi\beta$.

## 1. The energy–entropy argument, sharpened [Computed.]

Week 1 §4.4 balanced one vortex's energy against its positional entropy:
$$
F_1 = E_1 - S_1 = (\pi\beta - 2)\,\ln\frac{L}{a_0},
$$
sign change at $\beta = 2/\pi$. Three sharpenings before the RG:

**(a) Higher charges never win first.** A charge-$q$ vortex has $F_q = (\pi\beta q^2 - 2)\ln(L/a_0)$: the unbinding threshold $\beta_q = 2/\pi q^2$ sits at *lower* β (higher temperature) for larger $q$ — by the time charge-2 vortices would unbind, charge-1 vortices have long since proliferated and screened everything. Only $|q| = 1$ matters. (Same conclusion from operator dimensions: $\Delta_q = \pi\beta q^2$, so $e^{2i\chi}$ is strongly irrelevant where $e^{i\chi}$ is marginal — Week 3, F6.)

**(b) What the estimate gets exactly right — and what it does not.** The argument balances the vortex energy against entropy using the *unscreened* stiffness, so the number it produces, "transition at $\pi\beta = 2$," is a statement about whichever stiffness actually multiplies the vortex logarithm at long distances. That is the **renormalized** stiffness $\beta_R$ — reduced below the bare β by the bound pairs themselves (§2). The exact, universal statement is therefore
$$
\pi\,\beta_R(T_{BKT}) = 2,
$$
the fixed-point condition of the RG below, while the **bare** critical coupling is model-dependent and sits *above* $2/\pi \approx 0.64$: Monte Carlo gives $\beta_c \approx 1.12$ for the cosine XY model and $\approx 0.75$ for the Villain model [Stated — refs]. Conflating the two is the single most common error in this subject; every "$\beta_{BKT} = 2/\pi$" in Weeks 1 and 3 is to be read as the marginality condition on the running stiffness, exact for $\beta_R$, heuristic for the bare coupling.

**(c) What the argument cannot give.** How the transition is approached (the flow), what is universal (the jump), the shape of $\xi(T)$ (essential singularity) — for these, renormalize.

> **Physical picture.** In a helium film, "a free vortex" is not an abstraction: it is a mobile hole in the condensate that can be dragged by a flow, and a single one moving across the film dissipates supercurrent. Below $T_{BKT}$, every vortex is chained to a partner and the pair moves without net phase slip: the film flows forever. The transition is, operationally, the onset of *free* phase-slip carriers — which is why the experimental signature is a jump in the dissipationless stiffness and a sudden onset of broadband dissipation, both seen in the torsional-oscillator data. Energy–entropy is deciding whether a phase-slip carrier can afford to leave home.

## 2. The Kosterlitz renormalization group

The physics: at low temperature the plasma consists of bound $\pm$ dipoles. A dipole of size $r$ is polarizable; a gas of polarizable dipoles is a **dielectric**; a dielectric screens the interaction between widely separated charges. So the effective stiffness measured at scale $r$, call it $\beta_R(r)$, *decreases* as more dipole sizes are integrated in — and the fugacity of larger pairs is in turn controlled by the screened stiffness. Two coupled flows.

### 2.1 The fugacity flow, derived [Computed.]

From Week 3 §6, the vortex insertion $e^{\pm i\chi}$ is a scaling operator of dimension $\Delta = \pi\beta_R$: its two-point function decays as $r^{-2\pi\beta_R}$. The fugacity term in the sine-Gordon action is $2y\sum_{\tilde x}\cos\chi \to 2y\int \frac{d^2x}{a^2}\cos\chi$. Rescale the cutoff $a \to a\,e^{\ell}$: the measure contributes $e^{2\ell}$, the operator's amplitude renormalizes as $e^{-\Delta \ell}$, so $y(\ell) = y\, e^{(2 - \pi\beta_R)\ell}$, i.e.
$$
\boxed{\ \frac{dy}{d\ell} = \big(2 - \pi\beta_R\big)\, y \ + O(y^3).\ }
$$
Relevant for $\pi\beta_R < 2$, irrelevant for $\pi\beta_R > 2$, marginal at the energy–entropy point — §1(b) made precise.

### 2.2 The stiffness flow: screening [Computed in structure; constant normalized to refs.]

Compute how bound pairs renormalize the interaction between two distant test charges at $x_1, x_2$. Write the test-charge potential field (per unit probe charge, β included) as $\phi(s) = -\ln|s - x_1| + \ln|s - x_2|$, so the bare interaction is $V_{\rm bare} = -2\pi\beta\ln|x_{12}| + \text{const}$. To $O(y^2)$, insert one $\pm$ pair: charges at $s \pm r/2$, statistical weight $y^2\,(r/a)^{-2\pi\beta}$ per $d^2s\,d^2r/a^4$ (Week 3 §4). Its coupling to the probes is, for $r$ small against $|s - x_i|$, a **dipole term**:
$$
\delta E(s, \vec r\,) = 2\pi\beta\,\big[\phi(s + \tfrac{\vec r}{2}) - \phi(s - \tfrac{\vec r}{2})\big] \;\simeq\; 2\pi\beta\; \vec r\cdot\vec\nabla\phi(s).
$$
Expand the pair's Boltzmann factor; integrating over the dipole's orientation φ (measure $\int_0^{2\pi} d\varphi$, part of $d^2r = r\,dr\,d\varphi$), the linear term drops and
$$
\int_0^{2\pi}\! d\varphi\;\Big[\tfrac12\,(\delta E)^2\Big]
= \tfrac12\,(2\pi\beta)^2\, r^2\,\big|\vec\nabla\phi(s)\big|^2 \int_0^{2\pi}\!d\varphi\,\cos^2\varphi
= \pi\,\cdot\, 2\pi^2\beta^2\; r^2\,\big|\vec\nabla\phi(s)\big|^2 .
$$
Re-exponentiating the dilute-gas sum over pair positions and sizes, the correction to the effective test-charge action is
$$
\delta V_{\rm eff} = -\,2\pi^3\beta^2 \left[\int_a^\infty \frac{r^3\,dr}{a^4}\; y^2\Big(\frac{r}{a}\Big)^{-2\pi\beta}\right] \int d^2s\; \big|\vec\nabla\phi(s)\big|^2 .
$$
The field-energy integral is **positive and grows logarithmically** — compute it honestly. Write $\phi = -\phi_1 + \phi_2$ with $\phi_i(s) = \ln|s - x_i|$; the self-pieces, cut off at the core $a$ and a large radius $R$, give $2\times 2\pi\ln(R/a)$; the cross piece, by Green's identity ($\nabla^2\phi_2 = 2\pi\delta_{x_2}$, boundary term at $R$),
$$
-2\!\int\! \vec\nabla\phi_1\!\cdot\!\vec\nabla\phi_2\, d^2s
= -2\Big[2\pi\ln R - 2\pi\ln|x_{12}|\Big],
$$
so the $R$-dependence cancels (as it must: a dipole field decays as $1/s^2$, making the integral IR-finite) and
$$
\int d^2s\,\big|\vec\nabla\phi\big|^2 = 4\pi\,\ln\frac{|x_{12}|}{a} .
$$
So the pairs renormalize precisely the *coefficient of the logarithm* — the stiffness — downward. Collecting: the bare attraction $V = 2\pi\beta\ln|x_{12}|$ becomes $2\pi\beta_R\ln|x_{12}|$ with
$$
2\pi\beta_R = 2\pi\beta - 8\pi^4\beta^2 \int_a^\infty \frac{dr}{a}\Big(\frac{r}{a}\Big)^{3-2\pi\beta} y^2
\qquad\Longleftrightarrow\qquad
\beta_R^{-1} = \beta^{-1} + 4\pi^3 \int_a^\infty \frac{dr}{a}\Big(\frac{r}{a}\Big)^{3-2\pi\beta} y^2 + O(y^4),
$$
the $r^3\,dr$ built from the polarizability ($r^2$) and the measure ($r\,dr$), **the constant $4\pi^3$ now derived, not imported**. The integral converges at large $r$ exactly when $\pi\beta > 2$ — in the dipole phase — and its scale-by-scale content defines the flow: cutting at $r = a\,e^{\ell}$ and differentiating,
$$
\boxed{\ \frac{d\beta_R^{-1}}{d\ell} = 4\pi^3\, y^2(\ell) + O(y^4).\ }
$$
Both the structure and the constant are now derived [Computed], and the result agrees with the standard references in matching conventions (Kosterlitz 1974; Kardar §8.3: pair energy $2\pi\beta\ln r$, fugacity per unit cell). A useful aside on the constant's status: rescaling $y \to y/\sqrt{c}$ leaves $dy/d\ell$'s equation invariant while replacing $4\pi^3 \to 4\pi^3 c$, so no *universal* prediction depends on its value — the jump, the exponent, and the essential singularity below would survive any error in it. What the constant does fix is the non-universal dictionary between microscopic fugacity and flow trajectory (used when matching lattice data).

### 2.3 The flow diagram, integrated [Computed.]

Linearize around the marginal point: set $x \equiv \pi\beta_R - 2$ (small). Then $d y/d\ell = -x\,y$, and from §2.2, $dx/d\ell = \pi\, d\beta_R/d\ell = -\pi\beta_R^2\, \frac{d\beta_R^{-1}}{d\ell} \simeq -\frac{4}{\pi}\cdot 4\pi^3\, y^2 = -16\pi^2\, y^2$ (using $\beta_R \simeq 2/\pi$). The system
$$
\frac{dx}{d\ell} = -16\pi^2 y^2,
\qquad
\frac{dy}{d\ell} = -x\,y
$$
conserves $\;C \equiv x^2 - 16\pi^2 y^2\;$ ($\frac{dC}{d\ell} = 2x(-16\pi^2y^2) - 32\pi^2 y(-xy) = 0$): the trajectories are **hyperbolae**, with separatrices $x = \pm 4\pi y$.

```
      y ↑
        │ \        ↖ flows          /
        │   \   (disordered side) /
        │     \                 /
        │       \             /   separatrix  x = +4πy
        │  C<0    \         /
        │           \     /        C>0 : flows into the
        │             \ /          fixed line y=0, x>0
   ─────┼──────────────╳───────────────────→ x = πβ_R − 2
        │           (BKT point)   ● ● ● ● ●  fixed line (QLRO)
```
**Figure 1. The Kosterlitz flow. Right of the separatrix: $y \to 0$, a line of Gaussian fixed points (the QLRO phase, one point per temperature). Left: $y$ grows — vortices proliferate — and the flow exits toward the disordered phase.**

Three consequences, each a genuine prediction:

**(i) A critical *phase*.** For $C > 0$, $x > 0$ (low $T$, small $y$), the flow terminates on the fixed line $y = 0$ at some $x_\infty = \sqrt{C} > 0$: the long-distance theory is a pure Gaussian with renormalized stiffness $\beta_R(\infty) = (2 + x_\infty)/\pi$. Every temperature below $T_{BKT}$ is critical, with continuously varying exponent $\eta = 1/2\pi\beta_R(\infty)$ — Week 1's QLRO, now with the vortex renormalization included.

**(ii) The universal jump [Computed].** As $T \to T_{BKT}^-$ along the line of initial conditions, the terminus $x_\infty \to 0^+$: the renormalized stiffness approaches
$$
\lim_{T\to T_{BKT}^-}\ \beta_R(\infty; T) = \frac{2}{\pi},
\qquad\text{i.e.}\qquad
\boxed{\ \frac{\rho_s(T_{BKT}^-)}{k_B T_{BKT}} = \frac{2}{\pi},\ }
$$
identifying $\beta_R = \rho_s/k_BT$ with the measurable superfluid stiffness (helicity modulus — Week 1 Problem 6, Week 3 Problem 4). Above the transition $\rho_s = 0$ (no QLRO): the stiffness **jumps** by the universal amount $2/\pi$, whatever the material, lattice, or microscopic coupling. Nelson–Kosterlitz predicted it; Bishop–Reppy's torsional-oscillator experiment on helium films measured it. A transition with no order parameter, certified by a universal number.

**(iii) The essential singularity [Computed].** Just above $T_{BKT}$, the initial condition sits slightly on the running side: $C = -b\,t$ with $t = (T - T_{BKT})/T_{BKT}$ small, $b > 0$. Integrate the flow along such a trajectory: with $16\pi^2y^2 = x^2 + bt$,
$$
\frac{dx}{d\ell} = -(x^2 + b\,t)
\quad\Longrightarrow\quad
\ell(x) = \frac{1}{\sqrt{bt}}\Big[\arctan\frac{x_0}{\sqrt{bt}} - \arctan\frac{x}{\sqrt{bt}}\Big],
$$
and the total flow time before $x$ runs to $O(-1)$ (vortices dense; stop the flow) is $\ell^* \simeq \pi/\sqrt{bt}$. The correlation length is the scale reached:
$$
\boxed{\ \xi \sim a_0\, e^{\ell^*} = a_0 \exp\!\Big(\frac{\rm const}{\sqrt{T - T_{BKT}}}\Big).\ }
$$
No power law: *all* thermodynamic exponents are washed out (the singular free energy $\sim \xi^{-2}$ has an essential singularity; specific heat is smooth through $T_{BKT}$, with only a non-singular bump above it). If a simulation or experiment fits a power-law divergence at a putative XY transition, it is measuring crossover, not asymptotics — a practical warning that follows directly from the flow.

> **Physical picture.** The dielectric metaphor is exact enough to compute with. Below $T_{BKT}$ the vortex gas is a polarizable medium of bound pairs: it *screens* (reduces $\beta_R$) but never *conducts* — test charges at infinity still feel a logarithm, merely with a renormalized coefficient. At $T_{BKT}$ the largest pairs ionize, the medium becomes a plasma, screening becomes complete (Debye), and the logarithm is cut off at $\xi$: free vortices at density $\xi^{-2}$ destroy the stiffness entirely. The jump is the statement that a logarithmic dielectric cannot fade away continuously: either the log survives (with coefficient $\ge 2/\pi$, else pairs ionize) or it is screened to zero. Nothing in between is self-consistent — that is the physics content of the separatrix.

## 3. Kramers–Wannier duality of the 2d Ising model

The second duality of Block A: the Ising model equals *itself* at a dual temperature. Everything is a $\mathbb{Z}_2$ shadow of Week 3 — with the coefficient group $\mathbb{Z}$ replaced by $\mathbb{Z}_2$, Poisson resummation becomes the two-term Fourier transform on $\mathbb{Z}_2$, and the "integer currents" become the loops below.

### 3.1 The high-temperature expansion [Computed.]

$Z = \sum_{\{s_x = \pm1\}} \prod_{\langle xy\rangle} e^{\beta s_x s_y}$ on the $L\times L$ torus: $N = L^2$ sites, $N_b = 2N$ bonds, $N_p = N$ plaquettes. Use the $\mathbb{Z}_2$ character identity per bond:
$$
e^{\beta s s'} = \cosh\beta\,\big(1 + t\, s s'\big),\qquad t \equiv \tanh\beta .
$$
Expand the product over bonds: each term selects a subset $\gamma$ of "occupied" bonds, contributing $t^{|\gamma|}\prod_{x} s_x^{\deg_\gamma(x)}$. Summing each $s_x = \pm 1$ kills every term where some site has odd degree and yields $2$ per site otherwise. The surviving subsets — every vertex of even degree — are exactly the **$\mathbb{Z}_2$ 1-cycles** of the lattice ($\partial\gamma = 0$ mod 2, Week 2 language):
$$
\boxed{\ Z = 2^N(\cosh\beta)^{2N} \sum_{\gamma\,\in\,\ker\partial_1\otimes\mathbb{Z}_2} t^{|\gamma|}.\ }
$$

```
   loops on Λ (high T):              walls on Λ* (low T):

   +--+  +--+--+                     + + + + + +        + : spins up
   |  |  |     |                     + +╔═══╗+ +        − : flipped cluster
   +--+  +--+--+                     + +║− −║+ +        ═ : domain wall on the
                                     + +╚═══╝+ +            dual lattice
   closed even-degree                + + + + + +
   bond sets, weight t^|γ|           closed dual cycles, weight e^{−2β|γ*|}
```
**Figure 2. The two expansions that Kramers–Wannier equates: high-temperature loops on the direct lattice ↔ low-temperature domain walls on the dual lattice.**

### 3.2 The low-temperature expansion [Computed.]

Expand instead around the two ground states. A configuration is specified by its ground state and the set of flipped-cluster boundaries: **domain walls**, which are even-degree bond sets on the **dual** lattice — $\mathbb{Z}_2$ 1-cycles $\gamma^*$ on $\Lambda^*$. Each wall bond costs $e^{-2\beta}$ relative to alignment:
$$
Z = 2\, e^{2N\beta} \sum_{\gamma^*} e^{-2\beta\,|\gamma^*|}
\qquad
\big(\gamma^* \text{ ranging over the realizable wall classes — see §3.4}\big).
$$

### 3.3 The duality and the self-dual point [Computed.]

Both expansions sum $\mathbb{Z}_2$ 1-cycles weighted by (small parameter)$^{\rm length}$ — one on Λ, one on $\Lambda^*$, and the square lattice is self-dual. Identify the weights:
$$
t = \tanh\beta \;\longleftrightarrow\; e^{-2\beta^*}.
$$
This relation is symmetric in disguise. Compute: $\cosh^2\beta\,(1-t^2) = 1$ gives $\cosh^2\beta = 1/(1-t^2)$, so
$$
\sinh 2\beta = 2t\cosh^2\beta = \frac{2t}{1-t^2},
\qquad
\sinh 2\beta^* = \frac{e^{2\beta^*} - e^{-2\beta^*}}{2} = \frac{t^{-1} - t}{2} = \frac{1-t^2}{2t},
$$
$$
\boxed{\ \sinh 2\beta \,\cdot\, \sinh 2\beta^* = 1 .\ }
$$
High temperature at β maps to low temperature at $\beta^*$ and vice versa. If the model has a single phase transition (it does — Peierls plus Onsager), it must sit at the **self-dual point**:
$$
\sinh 2\beta_c = 1 \quad\Longrightarrow\quad \beta_c = \tfrac12\ln(1+\sqrt2) = 0.4407\ldots
$$
Kramers and Wannier located $T_c$ **three years before Onsager solved the model** — the historical proof that duality is a computational weapon, not a curiosity.

> **Physical picture.** What has actually been proven is a *functional equation for the free energy*: $F(\beta) = F(\beta^*) + \text{analytic}$. Such an equation cannot by itself create a transition; it can only constrain where one sits — a single non-analyticity must live at the equation's fixed point. This is duality's general epistemic status, worth internalizing now: dualities relocate and constrain singularities, while independent physics (here Peierls' argument that a transition exists at all) supplies them. The same division of labor recurs for Wegner's self-dual 4d gauge theory ([[week-05-wegner-z2-gauge-theory|Week 5]]) and for every self-dual point of Semester II.

### 3.4 Boundary conditions, tracked honestly [Model proof.]

The torus hides a refinement that textbooks skip and Semester II needs. The two expansions do **not** sum the same homology classes:

- The **loop** expansion (§3.1) includes cycles of *every* class in $H_1(T^2,\mathbb{Z}_2) = \mathbb{Z}_2^2$ — nothing restricts windings.
- The **wall** expansion (§3.2) realizes only *null-homologous* walls: a wall is the boundary of the flipped region, and boundaries are trivial in homology (a band wrapped around the torus has *two* winding walls — total class zero mod 2). Winding-odd wall classes are unreachable by any spin configuration with periodic boundary conditions.

The fix: track the four **boundary-condition sectors**. Let $\epsilon = (\epsilon_1, \epsilon_2) \in \mathbb{Z}_2^2$ label periodic/antiperiodic conditions in the two directions (antiperiodic = a seam of flipped couplings along a cycle). In the loop expansion, the seam weights each class: $Z_\epsilon \propto \sum_\gamma t^{|\gamma|}\,(-1)^{\langle\epsilon,[\gamma]\rangle}$, with $\langle\cdot,\cdot\rangle$ the intersection pairing of Week 2 §8. In the wall expansion, the seam shifts which wall classes are realizable by exactly $[\epsilon]$. The leading entries of the bookkeeping, on an $L\times L$ torus (classes labelled by winding $[\gamma] \in \mathbb{Z}_2^2$; shortest representative lengths shown):

| contribution | class | length | weight in $Z_\epsilon$ (loop expansion) |
|---|---|---|---|
| empty configuration | $(0,0)$ | 0 | $+1$, every sector |
| smallest plaquette loop | $(0,0)$ | 4 | $+t^4$, every sector |
| straight $x$-winding loop | $(1,0)$ | $L$ | $(-1)^{\epsilon_1}\, t^L$ |
| straight $y$-winding loop | $(0,1)$ | $L$ | $(-1)^{\epsilon_2}\, t^L$ |
| both windings (crossed) | $(1,1)$ | $2L$ | $(-1)^{\epsilon_1 + \epsilon_2}\, t^{2L}$ |

Trivial-class terms enter every sector with the same sign; winding terms flip sign across sectors — so sector *sums* project onto homology classes: $\sum_\epsilon (-1)^{\langle\epsilon,h\rangle} Z_\epsilon$ keeps exactly the class-$h$ loops. Matching the two representations sector by sector gives the duality as a **$\mathbb{Z}_2$ Fourier transform on $H_1$**:
$$
\widetilde Z_{\tilde\epsilon}(\beta^*) \;=\; \frac{1}{2}\sum_{\epsilon\in\mathbb{Z}_2^2} (-1)^{\langle\epsilon,\tilde\epsilon\rangle}\; Z_\epsilon(\beta)
\quad\text{(up to the common analytic prefactor).}
$$
Verify at leading order: the trivial-class loops (both sides) match with weight $+1$ in every sector; the shortest winding loop (length $L$, class $(1,0)$) appears in $\sum_\epsilon$ with sign $\sum_{\epsilon_1}(-1)^{\epsilon_1\cdot 1} = 0$ unless the dual sector supplies the matching seam — exactly the wall-realizability rule. $\square$

Two lessons: (i) *dualities act on the space of boundary conditions/sectors*, generally mixing them by a discrete Fourier transform on homology — in Semester II this becomes "gauging maps the theory to its orbifold, and the sectors are the background holonomies"; (ii) the pairing that appears is once again the intersection form — the same "+1" of Week 2, Figure 3.

## 4. Kadanoff–Ceva disorder operators

Duality exchanges the spin $\sigma_x$ with an object living on dual sites: the **disorder operator** $\mu_{\tilde x}$.

### 4.1 Definition and well-definedness [Computed.]

$\mu_{\tilde x}\mu_{\tilde y}$ is defined by flipping the coupling $\beta \to -\beta$ on every bond crossed by a chosen dual path ("seam") $\tilde\gamma$ from $\tilde x$ to $\tilde y$:
$$
\langle \mu_{\tilde x}\,\mu_{\tilde y}\rangle \;=\; \frac{Z[\beta \to -\beta \text{ on } \tilde\gamma]}{Z}.
$$

```
        s      s      s      s
                                        seam  ̃γ (on the dual lattice):
        s   ~~╳~~~~~╳~~~~~   s          couplings crossed by ~~ are
              μ(x̃)     μ(ỹ)             flipped  β → −β
        s      s      s      s
```
**Figure 3. A disorder-operator pair: a seam of frustrated bonds joining two dual sites.**

**The seam is unobservable; its endpoints are not.** Deform $\tilde\gamma$ to $\tilde\gamma'$ across a site $x$: the two seams differ by the set of bonds around $x$, and flipping all couplings at one site is undone by the change of variables $s_x \to -s_x$ — a $\mathbb{Z}_2$ "gauge transformation" of the dummy spins. Hence $\langle\mu\mu\rangle$ depends only on $\tilde x, \tilde y$ [Computed]. What *cannot* be gauged away are the endpoints: there the frustration is genuine (an odd plaquette of flipped bonds), and that is where the physics sits. This seam/endpoint dichotomy is the prototype for every extended operator in the course — Dirac strings (Week 8), 't Hooft lines (Week 11), symmetry defects (Semester II).

### 4.2 The disorder correlator is the dual order correlator [Computed.]

Re-run the duality of §3 with the seam inserted; the weight bookkeeping is worth displaying. In the wall expansion of $Z[\beta\to-\beta \text{ on }\tilde\gamma]$, examine one seam bond: if no wall crosses it, the two spins agree and the flipped coupling costs $e^{-\beta} / e^{+\beta} = e^{-2\beta}$ relative to normal; if a wall *does* cross, the spins disagree and the flipped coupling *gains* $e^{+2\beta}$ relative to what a wall bond normally pays. Summarizing, with $u \equiv e^{-2\beta}$:

| bond type | no wall | wall |
|---|---|---|
| normal | $1$ | $u$ |
| seam | $u$ | $1$ |

The seam *rewards* walls: relabeling the wall variable on each seam bond (wall ↔ no-wall) restores the normal weights everywhere at the cost of changing the wall parity constraint precisely at the seam's **endpoints** — the sum becomes one over wall configurations with a single open wall ending at $\tilde x$ and $\tilde y$. But "open high-temperature graphs from $\tilde x$ to $\tilde y$ with weight $u^{|\gamma|}$" is exactly the §3.1 expansion of the **spin–spin correlator** on the dual lattice at the coupling $\beta^*$ with $\tanh\beta^* = u = e^{-2\beta}$ — the KW relation again. Hence, exactly:
$$
\boxed{\ \langle\mu_{\tilde x}\,\mu_{\tilde y}\rangle_{\beta} \;=\; \langle\sigma_{\tilde x}\,\sigma_{\tilde y}\rangle_{\beta^*}.\ }
$$
Consequences, read from known Ising behavior:
$$
T < T_c:\ \ \langle\mu\mu\rangle \xrightarrow{|\tilde x - \tilde y|\to\infty} 0 \ \ (\text{disorder "uncondensed"}),
\qquad
T > T_c:\ \ \langle\mu\mu\rangle \to m^*(\beta^*)^2 \ne 0 \ \ (\text{disorder condensed}),
$$
the exact mirror of $\langle\sigma\sigma\rangle$. The high-temperature phase, featureless to every local operator, has **long-range order of a non-local operator**. Phases invisible to Landau are visible to disorder operators — the diagnostic pattern of the entire course (Wegner's phases next week are distinguished exactly this way).

The complete dictionary of "what condenses where," assembled for later reuse:

| | $\langle\sigma\sigma\rangle$ | $\langle\mu\mu\rangle$ | fermion $\psi = \sigma\mu$ | phase name |
|---|---|---|---|---|
| $T < T_c$ | $\to m^2 \ne 0$ | $\to 0$ | massive | ordered ("μ confined") |
| $T = T_c$ | $r^{-1/4}$ | $r^{-1/4}$ | massless | self-dual critical point |
| $T > T_c$ | $\to 0$ | $\to \tilde m^2 \ne 0$ | massive | disordered ("σ confined") |

Order and disorder cannot condense simultaneously — their mutual semi-locality (§4.3) forbids it (a nonzero $\langle\sigma\rangle$ and $\langle\mu\rangle$ would contradict the crossing sign at long distance). Exactly one of the pair condenses in each gapped phase, and the critical point is where custody changes. This exclusivity — *mutually non-local operators cannot both condense* — recurs as the Wilson/'t Hooft perimeter-law dichotomy of gauge theory ([[week-05-wegner-z2-gauge-theory|Week 5]] onward) and as the anyon-condensation logic of Semester II. The Ising model is its two-state prototype.

### 4.3 The order–disorder algebra, and a fermion [Computed.]

Sharpest in the transfer-matrix (quantum spin chain) language, where the 2d classical model becomes the transverse-field Ising chain with Hilbert space $\bigotimes_i \mathbb{C}^2$ and
$$
\sigma_i = \sigma^z_i,
\qquad
\mu_{\tilde\imath} = \prod_{j \le i}\sigma^x_j
$$
(the disorder operator = flip all spins to the left of the dual site $\tilde\imath$ — the operator version of the seam). Two Pauli computations:

**Mutual semi-locality.** For any site $k$ and dual site $\tilde\imath$:
$$
\sigma^z_k\;\mu_{\tilde\imath} = \Big(\prod_{j\le i}\sigma^x_j\Big)\sigma^z_k \times
\begin{cases} (-1) & k \le i \quad(\text{the seam crosses } k)\\ (+1) & k > i \end{cases}
$$
directly from $\sigma^z\sigma^x = -\sigma^x\sigma^z$ at the crossing site. Order and disorder operators are **mutually non-local**: each is charged under the symmetry the other generates (μ is a half-space $\mathbb{Z}_2$ transformation; σ is $\mathbb{Z}_2$-odd). Neither is "more fundamental."

**The composite is a fermion.** Pair the order operator at site $i$ with the disorder operator at the dual site *to its left*:
$$
\psi_i \;=\; \mu_{i-\frac12}\,\sigma^z_i \;=\; \Big(\prod_{j < i}\sigma^x_j\Big)\,\sigma^z_i ,
\qquad
\bar\psi_i \;=\; \Big(\prod_{j < i}\sigma^x_j\Big)\,\sigma^y_i
$$
(string strictly to the left — pairing with $\mu_{i+\frac12}$ instead would put a $\sigma^x_i$ on top of the $\sigma^z_i$ and spoil Hermiticity by a stray factor of $i$). These are Hermitian and square to one: **Majorana operators**. Anticommutation, for $i < k$:
$$
\psi_i\,\psi_k = -\,\psi_k\,\psi_i,
$$
because exactly one crossing occurs — $\psi_k$'s string $\prod_{j<k}\sigma^x_j$ contains $\sigma^x_i$, which anticommutes with $\psi_i$'s $\sigma^z_i$, while $\psi_i$'s string ends before site $k$ [Computed]. **These are the Jordan–Wigner Majorana fermions**, and the "string" that makes a fermion out of two bosonic operators is the disorder seam.

> **Physical picture.** Statistics is not an intrinsic property of a particle here — it is a *relational* property of operator pairs. σ alone is bosonic; μ alone is bosonic; their bound state is a fermion because each factor is charged under the symmetry whose defect the other creates, and exchanging two composites forces one seam-crossing sign. This "statistics from mutual linking" is the exact mechanism by which the toric code's $e$–$m$ bound state $\varepsilon$ is a fermion (Semester II Week 8), and — in its continuum dress — by which flux–charge composites anywhere acquire anyonic phases. The Ising chain is the smallest laboratory where one can *compute* it, which is why we did. The free-fermion solvability of the 2d Ising model (Onsager, in modern dress) is the statement that $\psi$ has a quadratic Hamiltonian. We will not solve it here; the point for this course is structural: *order × disorder = fermion* is the first instance of the anyon/statistics-from-mutual-linking phenomenon that Semester II Week 8 develops for the toric code.

### 4.4 Duality as an operator: the defect preview [Stated with mechanism; derivation in Semester II Week 13.]

In chain language, Kramers–Wannier is the map of bond algebras
$$
\sigma^x_i \;\longmapsto\; \sigma^z_i\sigma^z_{i+1},
\qquad
\sigma^z_i\sigma^z_{i+1} \;\longmapsto\; \sigma^x_{i+1},
$$
which exchanges the transverse-field Ising Hamiltonian $H(g) = -\sum(\sigma^z\sigma^z + g\,\sigma^x)$ with $H(1/g)$ (up to rescaling) — fixed point at $g = 1$, the chain avatar of $\sinh2\beta_c = 1$. One can ask for the *operator* $D$ implementing the map: $D\,\sigma^x_i = \sigma^z_i\sigma^z_{i+1}\,D$, etc. It exists — but it cannot be unitary, and counting states shows why. Deep in the ordered phase ($g \ll 1$) the low-energy states are the symmetric and antisymmetric combinations $|{\uparrow\cdots\uparrow}\rangle \pm |{\downarrow\cdots\downarrow}\rangle$ — **two** nearly degenerate states, with $\mathbb{Z}_2$ charges $\eta = \pm1$. Their dual image ($g \gg 1$) is the unique paramagnetic ground state and... one state. The duality map preserves the $\mathbb{Z}_2$-**even** spectra of $H(g)$ and $H(1/g)$ but has nothing to match the odd states onto: it is two-to-one, forgetting the global charge. An operator implementing a two-to-one map must annihilate half the space. The resolution is that $D$ is **non-invertible**, obeying the fusion rule
$$
D\times\bar D \;=\; 1 + \eta,\qquad \eta = \prod_i \sigma^x_i
$$
(the *fusion algebra* of the defect lines: unnormalized sum of the identity line and the symmetry line). The Hilbert-space counterpart is
$$
D^\dagger D \;=\; 1 + \eta \;=\; 2\,P_{\rm even},\qquad P_{\rm even} = \tfrac12(1+\eta),
$$
proportional to — not equal to — the projector onto the $\mathbb{Z}_2$-even sector: $D$ annihilates the odd sector outright. (Keep the two statements distinct: fusion rules of topological lines carry no normalization; operator identities do. Conflating them produces "projectors" that fail to square to themselves.) Geometrically, $D$ is a **topological defect line** in the 2d model (Aasen–Mong–Fendley), and "the model is self-dual" becomes "the model contains a topological line with projector fusion." Constructing $D$ explicitly and computing this fusion is Semester II Week 13's mini-calculation; here it stands as Block A's closing thought: **every duality we have performed is secretly an operator inside the theory it acts on.**

## 5. Subtleties and fine print

**F1 — The jump, operationally.** For a helium film, $\beta_R = \hbar^2\rho_s/(m^2 k_B T)$ in laboratory units, and the prediction reads $\rho_s(T_{BKT}^-)/T_{BKT} = \frac{2}{\pi}\frac{m^2 k_B}{\hbar^2}$ — a combination of fundamental constants, *independent of the substrate and film thickness*. Bishop–Reppy's torsional oscillator confirmed both the value and its universality across films. Few statistical-mechanics predictions this sharp exist; it is the experimental signature that BKT physics is real and not a lattice artifact.

**F2 — Is the dilute-gas RG self-consistent for the XY model?** The flow was derived to $O(y^2)$; it is trustworthy only if $y$ is small near the transition. *Estimate* it from Week 3's long-distance matching (that fugacity is a normalization convention at the lattice scale, not an exact microscopic quantity — Week 3, Move 7): evaluating at the marginality stiffness $\pi\beta_R = 2$, $y \sim e^{-2\pi^2\beta_R\kappa} = e^{-4\pi\kappa} \approx e^{-3.2} \approx 0.04$ — small enough that the dilute expansion is self-consistent for the Villain model, with short-distance corrections shifting the number at the tens-of-percent level, not its smallness. Models with genuinely low vortex core costs (e.g. modified XY actions) can push $y$ large and convert the transition to first order [Stated — refs: Minnhagen, *Rev. Mod. Phys.* 59 (1987) 1001]; the *sine-Gordon universality* holds only in the dilute basin.

**F3 — What "$\beta_R$" is measured by.** The flow variable $\beta_R(\infty)$ is the coefficient of the long-distance logarithm — operationally the helicity modulus/stiffness (twisted boundary conditions, Week 3 Problem 4), *not* the bare coupling and *not* directly the exponent of any single microscopic correlator. Comparing simulations to the RG means comparing stiffnesses. (The correlator exponent is then $\eta = 1/2\pi\beta_R$.)

**F4 — Kramers–Wannier needs the square lattice's self-duality.** On the triangular lattice, duality maps to the honeycomb and back; locating $T_c$ then requires the star–triangle relation in addition. Self-duality is a happy accident of the square lattice; *duality itself* (the loop/wall Fourier transform of §3.4) is completely general — and it is the general statement that survives into Semester II.

**F5 — ⟨μ⟩ alone requires care.** A single disorder operator needs a seam to the boundary (or a partner); on the torus only *pairs* (or an even number) are defined — the $\mathbb{Z}_2$ version of "charge neutrality on compact space" from Week 3, F4. Statements like "$\langle\mu\rangle \ne 0$ in the disordered phase" implicitly mean the cluster-decomposed limit $\lim_{|\tilde x - \tilde y|\to\infty}\sqrt{\langle\mu\mu\rangle}$.

**F6 — The homology bookkeeping is physics, not pedantry.** The sector Fourier transform of §3.4 is exactly the structure that reappears as: modular covariance of sector partition functions; discrete gauging = summing sectors (Semester II Week 4); and the fermion's need for spin structures (the JW string of §4.3 is sector-sensitive — Problem 5). Skipping it produces wrong factors of 2 in every one of those places.

## 6. Common misconceptions

- **"BKT spontaneously breaks the U(1) symmetry."** Nothing breaks: $\langle\vec S\rangle = 0$ on both sides (Mermin–Wagner, Week 1). The transition separates two symmetric phases distinguished by stiffness and defect binding — the founding example of order beyond Landau.
- **"Below $T_{BKT}$ there are no vortices."** Bound pairs exist at every $T > 0$ with computable density $\sim y^2$; they are why $\beta_R < \beta$. What vanishes below the transition is the density of *free* vortices.
- **"$\xi$ diverges with some exponent ν."** No power law exists: $\xi \sim e^{c/\sqrt{t}}$ (§2.3). Finite-size or crossover fits produce effective "exponents" that drift with the fitting window — a well-documented trap in the simulation literature.
- **"The disorder operator is unphysical because it depends on an arbitrary seam."** Its *correlators* are seam-independent (§4.1) — exactly as gauge-dependent intermediate quantities produce gauge-invariant observables. The seam teaches, rather: extended unobservable strings with observable endpoints are how mutually non-local operator pairs coexist in one theory.

## 7. Historical note

Berezinskii (1971) and Kosterlitz–Thouless (1973) independently identified defect unbinding as a phase transition compatible with Mermin–Wagner; Kosterlitz (1974) supplied the RG, and Nelson–Kosterlitz (1977) extracted the universal jump, confirmed by Bishop–Reppy (1978). On the other strand: Kramers–Wannier (1941) found the duality and $T_c$; Onsager (1944) solved the model; Kadanoff–Ceva (1971) introduced disorder variables and the order–disorder algebra, explicitly anticipating the operator content of lattice gauge theories — Wegner's paper (Week 5) appeared the same year, and Fradkin–Susskind (1978) unified the two strands in the Hamiltonian language used in §4.3. The 2016 Nobel Prize (Thouless, Haldane, Kosterlitz) recognized, in large part, the circle of ideas in §§1–2.

## 8. What to take away

1. **The BKT flow is two equations with hyperbolic trajectories** — $dy/d\ell = (2-\pi\beta_R)y$ [derived from the Week-3 operator dimension] and $d\beta_R^{-1}/d\ell \propto y^2$ [screening; structure derived] — terminating on a fixed *line* (QLRO) or running away (plasma).
2. **Two universal signatures, both derived from the flow:** the stiffness jump $\rho_s/T_{BKT} = 2/\pi$ and the essential singularity $\xi \sim e^{c/\sqrt{T-T_{BKT}}}$; both measured, neither Landau-describable.
3. **Kramers–Wannier is the $\mathbb{Z}_2$ Fourier transform of Week 3's duality**: loops ↔ walls, $\sinh2\beta\sinh2\beta^* = 1$, $T_c$ located without solving the model — and on the torus the duality acts on boundary-condition sectors through the intersection form.
4. **Disorder operators complete the operator content:** $\langle\mu\mu\rangle_\beta = \langle\sigma\sigma\rangle_{\beta^*}$ [derived], order and disorder are mutually semi-local, their composite is the Jordan–Wigner fermion, and the duality itself is a non-invertible defect line — the seed sentence of Semester II.

## 9. Looking ahead: Block B

Week 5 gauges. Wegner's construction promotes the Ising $\mathbb{Z}_2$ to a local symmetry, Elitzur's theorem wipes out every local order parameter, and the model's two phases — provably distinct — are distinguishable only by the behavior of a loop: Wilson's criterion, four years before Wilson used it for quarks. The disorder operator of this week becomes the 't Hooft loop; the Fourier-on-sectors structure becomes the electric/magnetic flux sectors of gauge theory. Block A built the tools on spin systems; Block B aims them at gauge fields, where they were always headed.

## 10. Problem set

**Core problems** (everyone).

**1. Flow-diagram quantitative work.**
(a) Verify that $C = x^2 - 16\pi^2y^2$ is conserved by the linearized flow and classify the trajectories.
(b) A sample has bare couplings such that $x_0 = 0.1$, $y_0 = 0.005$ at scale $a_0$. Which phase is it in? Compute its $\beta_R(\infty)$ or its $\xi$, as appropriate.
(c) Show that on the critical trajectory $y(\ell) = y_0/(1 + 4\pi y_0\ell)$ — logarithmically slow decay — and deduce the multiplicative logarithmic correction to the spin correlator at exactly $T_{BKT}$ [famously $\langle\vec S\vec S\rangle \sim r^{-1/4}(\ln r)^{1/8}$; derive the mechanism, quote the exponent].

**2. The jump from the helicity modulus.**
Combine Week 3 Problem 4 (winding-sector theta functions) with the flow: show that finite-size stiffness data $\Upsilon(L, T)$ should be compared to $\frac{2}{\pi}T\big(1 + \frac{1}{2\ln(L/L_0)}\big)$ at the transition (the universal finite-size correction from the marginal flow), and explain why ignoring the log correction misidentifies $T_{BKT}$.

**3. Kramers–Wannier with a magnetic field.**
Add $h\sum_x s_x$. Show the duality maps it to a *seam-condensation* term (a sum over disorder-line insertions) rather than a dual magnetic field, and conclude that self-duality is broken for $h \ne 0$ — consistent with the transition becoming a crossover. What operator *is* dual to $h\sigma$? (Answer in the language of §4: the field couples to the order operator; its dual couples to μ.)

**4. Disorder correlator at criticality.**
At $\beta = \beta_c$, use $\langle\mu\mu\rangle_\beta = \langle\sigma\sigma\rangle_{\beta^*}$ and the known Ising exponent $\eta_{\rm Ising} = 1/4$ to fix the decay of $\langle\mu\mu\rangle$. Both σ and μ have dimension $1/8$ at the self-dual point: what symmetry of the critical theory exchanges them, and what does that predict for the fermion ψ's dimension? (Check: $1/8 + 1/8$ vs the free-fermion value $1/2$ — resolve the discrepancy by identifying which fusion channel the fermion sits in.)

**Starred problems.**

**5⋆. Spin structures from the Jordan–Wigner string.**
On a periodic chain of $N$ sites, show that the fermion $\psi_i$ of §4.3 obeys $\psi_{i+N} = -\eta\,\psi_i\,$-type boundary conditions: the fermionic sectors (NS/R — antiperiodic/periodic) are tied to the $\mathbb{Z}_2$ charge sectors η. Connect to the four bosonic sectors of §3.4: this is the 2d Ising model's spin-structure sum in microscopic form.

**6⋆. The defect commutes with the transfer matrix.**
Take the duality map of §4.4 at the self-dual point $g = 1$ and verify on generators that any operator $D$ satisfying the intertwining relations commutes with $H(1)$. Then show that $D$ must annihilate the $\mathbb{Z}_2$-odd sector (count ground states on both sides of the map), so $D^\dagger D$ projects — the non-invertibility, from pure representation theory, before any explicit construction. (The construction itself: Semester II Week 13.)

**7⋆⋆ (optional). The $\mathbb{Z}_N$ clock ladder.**
Combine Week 3 Problem 6 with this week: for the $\mathbb{Z}_N$ clock model, derive the sector-mixing rule of §3.4 (now a $\mathbb{Z}_N$ Fourier transform on $H_1(T^2,\mathbb{Z}_N)$), identify the $N$ disorder operators, and — for $N \ge 5$ — describe how the two BKT-like transitions bound a critical phase in which *both* order and disorder correlators decay algebraically. Tabulate which operators condense in each of the three phases; this table is the $N$-state warm-up for the phase classification language of Semester II.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block A. Rewritten to the note-quality-template standard 2026-07-07 (first draft 2026-07-01).*
