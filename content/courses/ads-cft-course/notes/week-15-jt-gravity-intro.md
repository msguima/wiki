---
title: "Week 15 — JT gravity: the soluble laboratory"
type: lecture-notes
course: syllabus
semester: 1
week: 15
block: C
duration: "4 hours (2 lectures × 2 hours)"
status: drafting
modified: 2026-05-28
---

# Week 15 — JT Gravity: the Soluble Laboratory

> *Semester I closes with the model that makes all of Semester II computable. **Jackiw–Teitelboim gravity** is 2d dilaton gravity in nearly-AdS$_2$: the dilaton freezes the bulk to rigid AdS$_2$, and *all* the dynamics lives on the boundary as a **Schwarzian** theory. JT is exactly solvable, arises universally as the near-extremal / SYK low-energy limit, and is the cleanest arena for the Page curve, replica wormholes, and islands of Semester II. This week derives the Schwarzian reduction and its consequences, and hands the baton to Sem II.*

## Learning goals

By the end of this week, a student can:

1. Write the JT action and explain the role of the dilaton and the topological term.
2. **Derive** that the dilaton EOM freezes the bulk to AdS$_2$ ($R=-2/L^2$).
3. State the reduction to the boundary **Schwarzian** action and its $\mathrm{SL}(2,\mathbb{R})$ invariance.
4. State the exact Schwarzian density of states and its low/high-energy behaviour.
5. Explain the SYK connection and why JT is the Semester II laboratory.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Black Hole Information* §4** — the *JT Gravity and the Schwarzian* page. adscft.org has no standalone JT chapter; the Guides page *AdS2/CFT1: JT gravity and the SYK model* is the fuller treatment.
- Almheiri, Polchinski, *Models of AdS$_2$ backreaction and holography*, [arXiv:1402.6334](https://arxiv.org/abs/1402.6334) — JT/NAdS$_2$.
- Maldacena, Stanford, Yang, *Conformal symmetry and its breaking in two-dimensional nearly anti-de Sitter space*, [arXiv:1606.01857](https://arxiv.org/abs/1606.01857) — the Schwarzian.

**Prerequisites.** [[week-06-ads-geometries]] (AdS), [[week-09-holographic-renormalisation]] (boundary terms/GHY), [[week-05-2d-cft-essentials]] (the Schwarzian appeared there in the $T$-transformation). Standard GR (extrinsic curvature, Gibbons–Hawking).

**AQFT cross-reference.** None at this stage; the algebraic side of AdS$_2$ (type II$_1$ at finite $N$, crossed products) is Semester II material.

## 1. The JT action

JT gravity is the simplest 2d gravity with a non-trivial dilaton $\phi$:

$$
\boxed{\;S_{\rm JT} = -\,S_0\,\chi - \frac{1}{2}\Big[\int_\mathcal{M}\!\sqrt g\,\phi\,(R+2) + 2\int_{\partial\mathcal{M}}\!\sqrt h\,\phi_b\,(K-1)\Big]\;}
$$

(units $L=1$; $\chi=2-2g-b$ the Euler characteristic, $K$ the boundary extrinsic curvature, $\phi_b$ the boundary dilaton value). Three pieces:

- $-S_0\chi$ is **topological** ($S_0=\phi_0/4G_N$): it weights surfaces by $e^{S_0\chi}=e^{S_0(2-2g)}$, so $e^{-S_0}$ is the genus-counting parameter — the JT analogue of $1/N$ ([[week-07-large-n-and-thooft-limit|Week 7]]). $S_0$ is the extremal entropy.
- the bulk $\phi(R+2)$ term, with $\phi$ a Lagrange multiplier;
- the boundary Gibbons–Hawking term, which carries the dynamics.

JT is not ad hoc: it is the **universal** near-horizon, near-extremal limit of higher-dimensional black holes (the throat is AdS$_2\times$(sphere), and the dilaton is the sphere's size).

## 2. The dilaton freezes the bulk (worked)

Vary $S_{\rm JT}$ with respect to $\phi$. The bulk term gives, immediately,

$$
\frac{\delta S}{\delta\phi}=0\ \Rightarrow\ R+2=0\ \Rightarrow\ R=-2\quad(\text{i.e. }R=-2/L^2),
$$

so the dilaton is a Lagrange multiplier **forcing the bulk to be rigid AdS$_2$** — there is no bulk graviton, no local 2d dynamics. Varying with respect to the metric then gives the dilaton equation $\nabla_\mu\nabla_\nu\phi - g_{\mu\nu}\nabla^2\phi + g_{\mu\nu}\phi = 0$, which determines $\phi(x)$ on the fixed AdS$_2$ background (it grows linearly toward the boundary). With the geometry frozen, **all dynamics is in how the boundary curve is embedded in rigid AdS$_2$** — that is the only freedom left.

> **[Proven]** $R=-2$ from the dilaton EOM (Exercise 1); the bulk is rigid AdS$_2$.

## 3. The Schwarzian boundary action

Place the boundary at large proper distance (a cutoff curve in AdS$_2$), parametrised by boundary proper time $u$; its shape is encoded by the reparametrisation $t(u)$ relating boundary time to the AdS$_2$ Poincaré time. Evaluating the JT action on-shell (dilaton integrated out, the GHY term expanded in the boundary embedding) leaves a boundary action for $t(u)$:

$$
\boxed{\;S_{\rm bdy} = -C\int du\;\{t(u),u\},\qquad
\{t,u\} = \frac{t'''}{t'} - \frac{3}{2}\Big(\frac{t''}{t'}\Big)^2,\;}
$$

with coupling $C=\phi_b/(8\pi G_N)$ (the boundary value of the dilaton). $\{t,u\}$ is the **Schwarzian derivative**. Its key property — the **chain rule** $\{f\circ g,u\}=\{f,g\}\,(g')^2+\{g,u\}$ — implies the action is invariant under global $\mathrm{SL}(2,\mathbb{R})$ Möbius transformations $t\mapsto\tfrac{at+b}{ct+d}$ ($ad-bc=1$), since $\{(at+b)/(ct+d),u\}=\{t,u\}$. So the Schwarzian theory has the full reparametrisation symmetry of the boundary **spontaneously and explicitly broken to $\mathrm{SL}(2,\mathbb{R})$** — the AdS$_2$ isometry group. The Schwarzian mode is the (pseudo-)Goldstone of this breaking; this pattern is exactly the symmetry-breaking of nearly-AdS$_2$ and the source of the model's universality.

**Worked: the Schwarzian of a Möbius map vanishes.** Verify $\mathrm{SL}(2,\mathbb{R})$ invariance directly. For $M(t)=\tfrac{at+b}{ct+d}$ with $ad-bc=1$, differentiate:

$$
M' = \frac{ad-bc}{(ct+d)^2} = \frac{1}{(ct+d)^2},\quad
M'' = \frac{-2c}{(ct+d)^3},\quad
M''' = \frac{6c^2}{(ct+d)^4}.
$$

Assemble the Schwarzian:

$$
\{M,t\} = \frac{M'''}{M'} - \frac32\Big(\frac{M''}{M'}\Big)^2
= \frac{6c^2}{(ct+d)^2} - \frac32\Big(\frac{-2c}{ct+d}\Big)^2
= \frac{6c^2}{(ct+d)^2} - \frac{6c^2}{(ct+d)^2} = 0.
$$

So $\{M,t\}=0$ for any Möbius $M$. The chain rule $\{M\circ t,u\}=\{M,t\}\,(t')^2+\{t,u\}=\{t,u\}$ then shows the action $-C\!\int\{t,u\}\,du$ is **invariant** under $t\mapsto M(t)$ — exactly the $\mathrm{SL}(2,\mathbb{R})$ residual symmetry, with the Möbius maps acting as the unbroken AdS$_2$ isometries.

> **[Sketched]** the on-shell reduction to the Schwarzian (dilaton integrated out, GHY expanded; Exercise 2). **[Proven]** $\mathrm{SL}(2,\mathbb{R})$ invariance (the $\{M,t\}=0$ computation above). **[Stated-without-proof]** universality of the Schwarzian IR (Almheiri–Polchinski).

## 4. Exact solvability and random matrices

The Schwarzian path integral is **one-loop exact** (it is a particular coadjoint-orbit / localisation computation). The disk partition function and density of states are

$$
Z_{\rm disk}(\beta)\propto\Big(\frac{C}{\beta}\Big)^{3/2}e^{2\pi^2 C/\beta},\qquad
\rho(E)\propto \sinh\!\big(2\pi\sqrt{2C E}\big).
$$

Read the density carefully: at **low** energy $\rho(E)\propto\sqrt{E}$ (a smooth spectral edge at $E=0$ — *not* exponential), while at **high** energy $\rho(E)\sim e^{2\pi\sqrt{2CE}}$ (the Cardy-like exponential growth, the JT version of [[week-05-2d-cft-essentials|Week 5]]'s Cardy formula). This exact control is why JT is the laboratory of choice.

Beyond the disk, **summing over bulk topologies** (the $e^{S_0\chi}$ expansion) reorganises JT gravity into a **random-matrix integral** (Saad–Shenker–Stanford): the genus expansion of JT equals the topological expansion of a double-scaled matrix model, and the boundary "theory" is an *ensemble* rather than a single Hamiltonian. The higher-topology contributions — handles, and crucially **wormholes** connecting boundaries — are exactly the [[sem2-week-10-replica-wormholes|replica wormholes]] that produce the Page curve. JT is where "sum over geometries" becomes a controlled, computable statement.

> **[Stated-without-proof]** the exact $Z_{\rm disk}$, $\rho(E)$, and the matrix-model dual (Saad–Shenker–Stanford); the corrected low-energy edge $\rho\propto\sqrt E$ is the exact Schwarzian result.

## 5. SYK and the bridge to Semester II

The **Sachdev–Ye–Kitaev** model — $N$ Majorana fermions with random all-to-all couplings — has, at low energy and large $N$, an emergent reparametrisation symmetry broken to $\mathrm{SL}(2,\mathbb{R})$, with effective action *exactly the Schwarzian*. SYK is thus a concrete quantum-mechanical system holographically dual to JT/NAdS$_2$, with $N$ (more precisely $N/\mathcal{J}$ at strong coupling) playing the role of $1/G_N$ — and the disorder average is the field-theory face of JT's ensemble/matrix-model nature.

This closes Semester I and sets up Semester II: JT + a non-gravitating bath is the model for the **Page curve** ([[sem2-week-06-jt-gravity-page-curve|Sem II Wk 6]], [[sem2-week-09-page-curve|Wk 9]]); JT topology change gives **replica wormholes** ([[sem2-week-10-replica-wormholes|Wk 10]]) and the **island formula** ([[sem2-week-11-island-formula|Wk 11]]); and the AdS$_2$/SYK pairing is revisited in [[sem2-week-07-ads2-ads3-essentials|Sem II Wk 7]]. Everything hard about black-hole information becomes computable here.

## 6. Key claims and proof status

- **[Proven]** dilaton EOM $\Rightarrow R=-2$ (rigid AdS$_2$) (§2).
- **[Sketched]** reduction to the Schwarzian $-C\int\{t,u\}\,du$; **[Proven]** its $\mathrm{SL}(2,\mathbb{R})$ invariance (§3).
- **[Stated-without-proof]** exact $\rho(E)\propto\sinh(2\pi\sqrt{2CE})$, $Z_{\rm disk}$, and the matrix-model dual (§4).
- **[Stated-without-proof]** SYK ↔ Schwarzian/JT (§5).

*No coefficients in this note are uncertain at the stated level. (The exact Schwarzian $Z$/$\rho$ are standard, attributed; corrected the skeleton's low-energy density to the exact $\sqrt E$ edge.)*

## 7. What to take away

- **JT** = 2d dilaton gravity; the dilaton **freezes the bulk to rigid AdS$_2$** ($R=-2$); all dynamics is on the boundary.
- The boundary theory is the **Schwarzian** $S=-C\int\{t,u\}\,du$, with reparametrisations **broken to $\mathrm{SL}(2,\mathbb{R})$** (the AdS$_2$ isometry); the Schwarzian mode is the Goldstone of nearly-AdS$_2$.
- It is **exactly solvable**: $\rho(E)\propto\sinh(2\pi\sqrt{2CE})$ ($\sqrt E$ edge, $e^{2\pi\sqrt{2CE}}$ Cardy growth); topology sum = **matrix model** (Saad–Shenker–Stanford), wormholes included.
- **SYK** realises the Schwarzian; $1/N\leftrightarrow G_N$, disorder average $\leftrightarrow$ ensemble.
- JT is the **Semester II laboratory**: Page curve, replica wormholes, islands all become computable. *End of Semester I.*

## Exercises

**Core.**

1. **Dilaton EOM.** Vary $S_{\rm JT}$ w.r.t. $\phi$; obtain $R+2=0$ and verify AdS$_2$ ($R=-2$) solves it.
2. **Schwarzian reduction.** For a constant-$r$ cutoff curve in Poincaré AdS$_2$, compute $K$ and show the GHY boundary action reduces (as $r_c\to\infty$) to $-C\int\{t,u\}\,du$ plus a constant.
3. **$\mathrm{SL}(2)$ invariance.** Using the Schwarzian chain rule, verify $\{(at+b)/(ct+d),u\}=\{t,u\}$ for $ad-bc=1$, hence the action's $\mathrm{SL}(2,\mathbb{R})$ invariance.

**Starred.**

4. $\star$ **Spectral density.** From $Z_{\rm disk}(\beta)\propto(C/\beta)^{3/2}e^{2\pi^2C/\beta}$, inverse-Laplace-transform to obtain $\rho(E)\propto\sinh(2\pi\sqrt{2CE})$; check the $\sqrt E$ edge and the high-$E$ exponential.
5. $\star$ **SYK parallel.** Describe the SYK low-energy effective action, the reparametrisation breaking to $\mathrm{SL}(2,\mathbb{R})$, and identify the SYK parameter playing the role of $1/G_N$.

**Project.**

6. **Topology and wormholes.** Read Saad–Shenker–Stanford ([arXiv:1903.11115](https://arxiv.org/abs/1903.11115)); explain how the JT genus expansion becomes a matrix integral and how wormhole topologies set up the [[sem2-week-10-replica-wormholes|replica-wormhole]] / Page-curve story of Semester II.

## Connections to other parts of the wiki

- **Within the course.** Closes Block C and Semester I; the Schwarzian first appeared in [[week-05-2d-cft-essentials|Wk 5]] (the $T$-transformation). Forward: [[sem2-week-06-jt-gravity-page-curve|Sem II Wk 6]] (Page curve in JT + bath), [[sem2-week-04-replica-trick-in-gravity|Wk 4]] / [[sem2-week-10-replica-wormholes|Wk 10]] (replica wormholes), [[sem2-week-11-island-formula|Wk 11]] (islands), [[sem2-week-07-ads2-ads3-essentials|Wk 7]] (AdS$_2$/SYK).
- **Concepts.** [[jt-gravity]], [[holographic-dictionary]], [[page-curve]].
- **AQFT course cross-reference.** None at this stage; algebraic AdS$_2$ (type II$_1$, crossed products) is Sem II.
- **Area page.** [[gauge-gravity-duality]] — JT is the most tractable instance of the duality, the testing ground for Sem II's quantum-gravity ideas.

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block C. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*

*End of Sem I Block C — and of Semester I.*
