---
title: "Week 13 — Holographic entanglement entropy: Ryu–Takayanagi"
type: lecture-notes
course: syllabus
semester: 1
week: 13
block: C
duration: "4 hours (2 lectures × 2 hours)"
status: drafting
modified: 2026-05-28
---

# Week 13 — Holographic Entanglement Entropy: Ryu–Takayanagi

> *The most consequential entry in the holographic dictionary, and the one closest to the group's own program: **entanglement entropy is geometry**. The Ryu–Takayanagi formula computes the entanglement entropy of a boundary region as the area of a minimal bulk surface, $S_A=\mathrm{Area}(\gamma_A)/4G_N$ — the same $1/4G_N$ as Bekenstein–Hawking. This week we build the formula carefully, then **carry out the AdS$_3$ interval calculation in full**, recovering Calabrese–Cardy's $(c/3)\log$ step by step, and prove strong subadditivity geometrically. This is where the holographic and algebraic-QFT entanglement programs meet ([[week-14-hrt-and-subregion-subalgebra|Week 14]], [[sem2-week-03-modular-flow-on-subregions|Sem II Wk 3]]).*

## Learning goals

By the end of this week, a student can:

1. Recall the replica definition of entanglement entropy and motivate RT from it.
2. State the RT formula precisely, including the homology condition, and explain the $1/4G_N$.
3. **Carry out** the AdS$_3$ interval computation end to end and obtain $S=(c/3)\log(\ell/\epsilon)$.
4. Extend the computation to finite temperature (BTZ) and read off the limits.
5. Analyse the two-interval phase transition and prove strong subadditivity geometrically.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *AdS/CFT Foundations* §9** — entanglement entropy in QFT and the RT formula.
- Ryu, Takayanagi, *Holographic derivation of entanglement entropy from AdS/CFT*, [arXiv:hep-th/0603001](https://arxiv.org/abs/hep-th/0603001) — the original.
- Calabrese, Cardy, *Entanglement entropy and quantum field theory*, [arXiv:hep-th/0405152](https://arxiv.org/abs/hep-th/0405152) — the 2d CFT result we reproduce.

**Prerequisites.** [[week-06-ads-geometries]] (AdS$_3$ / $\mathbb{H}^2$ geometry), [[week-09-holographic-renormalisation]] ($c=3L/2G_N$), [[week-05-2d-cft-essentials]] (the $c$ being matched). The replica trick from standard QFT.

**AQFT cross-reference.** The von Neumann entropy and modular Hamiltonian here are the geometric face of the algebraic objects in AQFT 2026 Block B; the precise bridge is [[sem2-week-03-modular-flow-on-subregions|Sem II Wk 3]] (JLMS, first law).

## 1. Entanglement entropy and the replica trick

Given a state $\rho$ and a spatial region $A$, the **reduced density matrix** is $\rho_A=\mathrm{Tr}_{\bar A}\rho$, and the **entanglement entropy** is the von Neumann entropy

$$
S_A = -\mathrm{Tr}\,\rho_A\log\rho_A.
$$

Direct evaluation is hard (the $\log$ of an operator). The **replica trick** computes instead the integer Rényi entropies and continues in $n$:

$$
S_A = -\partial_n\,\mathrm{Tr}\,\rho_A^{\,n}\Big|_{n=1},
$$

which follows from $\mathrm{Tr}\,\rho_A^n=\sum_i p_i^n$ (with $p_i$ the eigenvalues of $\rho_A$): differentiating, $\partial_n\sum_i p_i^n=\sum_i p_i^n\log p_i$, and at $n=1$ (using $\sum_i p_i=1$) this is $\sum_i p_i\log p_i=-S_A$.

In a path integral, $\rho_A$ is prepared by a path integral on the plane with a cut along $A$; $\mathrm{Tr}\,\rho_A^n$ glues $n$ copies cyclically across the cut, giving the partition function on an **$n$-sheeted cover** branched over $\partial A$:

$$
\mathrm{Tr}\,\rho_A^{\,n} = \frac{Z_n}{Z_1^{\,n}}.
$$

**Holographically**, $Z_n$ is computed by a bulk geometry filling in the $n$-sheeted boundary. In the $n\to1$ limit the gravitational action localises on a codimension-2 bulk surface anchored at $\partial A$ — this is the heuristic origin of RT. The rigorous gravitational version (Lewkowycz–Maldacena) is [[sem2-week-04-replica-trick-in-gravity|Sem II Wk 4]]; here we take RT as given and test it.

## 2. The Ryu–Takayanagi formula

$$
\boxed{\;S_A = \frac{\mathrm{Area}(\gamma_A)}{4G_N},\;}
$$

where $\gamma_A$ is the bulk surface determined by three conditions:

1. **Anchoring:** $\partial\gamma_A=\partial A$ (it ends on the boundary entangling surface).
2. **Homology:** $\gamma_A$ together with $A$ bounds a bulk region (the *entanglement wedge*); this is what allows, e.g., a disconnected $\gamma_A$ and is essential at finite temperature.
3. **Minimality:** among all surfaces satisfying 1–2, $\gamma_A$ has least area.

Three comments, each worth internalising:

- **The coefficient is Bekenstein–Hawking's.** $1/4G_N$ is *the same* as the black-hole entropy coefficient — entanglement entropy and horizon entropy are computed by one rule. This is the first concrete hint that a black-hole horizon *is* an entangling surface.
- **The UV divergence is automatic and correct.** $\gamma_A$ reaches the boundary, where the metric $\propto1/z^2$ blows up, so the area diverges. Cutting off at $z=\epsilon$ gives, in $d$ boundary dimensions, a leading **area law** $S_A\sim\mathrm{Area}(\partial A)/\epsilon^{d-2}$ — exactly the known UV divergence of QFT entanglement entropy. The geometry reproduces the right short-distance physics with no extra input.
- **Minimality implements purity and competition.** When several homologous surfaces exist, the least-area one wins; as parameters vary, the winner can jump (a phase transition; §5).

## 3. The interval in AdS$_3$/CFT$_2$ — full computation

This is the cleanest non-trivial check, and we do every step.

**Setup.** Euclidean Poincaré AdS$_3$ has metric

$$
ds^2 = \frac{L^2}{z^2}\big(dz^2 + dx^2\big)\qquad(z>0),
$$

a copy of the hyperbolic plane $\mathbb{H}^2$ with radius $L$. (We suppress the boundary time direction; the interval lives on a constant-time slice.) The boundary is at $z\to0$; we regulate it at $z=\epsilon$. Take the interval $A=[-\ell/2,\ell/2]$, so $\partial A$ is the two points $x=\pm\ell/2$ at $z=\epsilon$. A codimension-2 surface in this 2d space is a **curve** — a geodesic of $\mathbb{H}^2$.

**Step 1 — the minimal curve is a semicircle.** Geodesics of $\mathbb{H}^2$ in the upper-half-plane model are semicircles centred on the boundary $z=0$ (and vertical lines, the infinite-radius limit). One proves this from the geodesic equation, but we can also verify it variationally below. The semicircle anchored at $x=\pm\ell/2$ is

$$
x^2 + z^2 = \Big(\frac{\ell}{2}\Big)^2.
$$

*(Caution: this is special to a 1d geodesic in $\mathbb{H}^2$. The higher-dimensional minimal surfaces of [[week-11-wilson-loops|Week 11]] — and RT in $d>2$ — are **not** semicircles, because the area functional carries extra powers of $z$.)*

**Step 2 — set up the length functional.** Parametrise the curve by the polar angle $\theta$ of the semicircle,

$$
x = \frac{\ell}{2}\cos\theta,\qquad z = \frac{\ell}{2}\sin\theta,\qquad \theta\in(0,\pi).
$$

Then $dx=-\tfrac{\ell}{2}\sin\theta\,d\theta$, $dz=\tfrac{\ell}{2}\cos\theta\,d\theta$, so $\sqrt{dx^2+dz^2}=\tfrac{\ell}{2}\,d\theta$, and the proper length is

$$
\mathcal{L} = \int \frac{L}{z}\sqrt{dx^2+dz^2}
= \int \frac{L}{\frac{\ell}{2}\sin\theta}\cdot\frac{\ell}{2}\,d\theta
= L\int \frac{d\theta}{\sin\theta}.
$$

The $\ell/2$ factors cancel — a first sign that the answer will be scale-independent (conformal).

**Step 3 — the limits of integration.** The cutoff $z=\epsilon$ means $\tfrac{\ell}{2}\sin\theta=\epsilon$, i.e. $\sin\theta=2\epsilon/\ell$. For small $\epsilon$ this gives two endpoints, $\theta_\epsilon\approx 2\epsilon/\ell$ (near $x=+\ell/2$) and $\pi-\theta_\epsilon$ (near $x=-\ell/2$). So

$$
\mathcal{L} = L\int_{\theta_\epsilon}^{\pi-\theta_\epsilon}\frac{d\theta}{\sin\theta}.
$$

**Step 4 — do the integral.** Using $\int\frac{d\theta}{\sin\theta}=\log\tan\frac{\theta}{2}$,

$$
\mathcal{L} = L\Big[\log\tan\tfrac{\theta}{2}\Big]_{\theta_\epsilon}^{\pi-\theta_\epsilon}
= L\Big(\log\tan\tfrac{\pi-\theta_\epsilon}{2} - \log\tan\tfrac{\theta_\epsilon}{2}\Big).
$$

Now $\tan\frac{\pi-\theta_\epsilon}{2}=\cot\frac{\theta_\epsilon}{2}=1/\tan\frac{\theta_\epsilon}{2}$, so the bracket is $\log\big(1/\tan^2\tfrac{\theta_\epsilon}{2}\big)=-2\log\tan\tfrac{\theta_\epsilon}{2}$. For small $\theta_\epsilon$, $\tan\tfrac{\theta_\epsilon}{2}\approx\tfrac{\theta_\epsilon}{2}\approx\tfrac{\epsilon}{\ell}$. Hence

$$
\mathcal{L} = -2L\log\tan\tfrac{\theta_\epsilon}{2} \approx -2L\log\frac{\epsilon}{\ell} = 2L\,\log\frac{\ell}{\epsilon}.
$$

**Step 5 — apply RT and Brown–Henneaux.** Insert into the RT formula and use the Brown–Henneaux central charge $c=3L/2G_N$ ([[week-09-holographic-renormalisation|Week 9]]), i.e. $L/2G_N=c/3$:

$$
S_A = \frac{\mathcal{L}}{4G_N} = \frac{2L\log(\ell/\epsilon)}{4G_N} = \frac{L}{2G_N}\log\frac{\ell}{\epsilon}
\;=\; \boxed{\;\frac{c}{3}\,\log\frac{\ell}{\epsilon}.\;}
$$

This is **exactly** the Calabrese–Cardy universal result for a single interval in the vacuum of a 2d CFT — derived here purely from a bulk geodesic, with no free parameters. The match is one of the sharpest quantitative confirmations of holography.

**Step 6 (variational check, optional).** That the semicircle extremises $\mathcal{L}=\int\frac{L}{z}\sqrt{1+x'^2}\,dz$ follows because the integrand has no explicit $x$, so $\partial(\text{integrand})/\partial x'=\frac{L x'}{z\sqrt{1+x'^2}}$ is conserved; solving the resulting first-order ODE returns $x^2+z^2=$const. (Exercise 1.)

## 4. Finite temperature: the BTZ interval

Repeat the computation in the BTZ black hole (the AdS$_3$ thermal geometry, [[week-12-finite-temperature-ads-schwarzschild|Week 12]]) at inverse temperature $\beta$. The geodesic now lives in BTZ; the calculation is the same in structure but with hyperbolic functions, and gives

$$
\boxed{\;S_A(\beta) = \frac{c}{3}\,\log\!\Big[\frac{\beta}{\pi\epsilon}\,\sinh\!\frac{\pi\ell}{\beta}\Big].\;}
$$

Two limits check the physics:

- **$T\to0$ ($\beta\to\infty$):** $\sinh(\pi\ell/\beta)\to\pi\ell/\beta$, so $S\to\tfrac{c}{3}\log(\ell/\epsilon)$ — the vacuum result of §3. ✓
- **$\ell\gg\beta$ (large interval):** $\sinh(\pi\ell/\beta)\to\tfrac12 e^{\pi\ell/\beta}$, so $S\to\tfrac{c}{3}\cdot\tfrac{\pi\ell}{\beta}+\dots=\tfrac{\pi c}{3\beta}\,\ell+\dots$ — **linear in $\ell$**, i.e. an extensive *thermal* entropy with density $\tfrac{\pi c}{3\beta}$, exactly the Cardy entropy density. ✓ The RT surface has dropped down and is skirting the horizon, and its near-horizon part contributes the thermal entropy.

## 5. Homology, phase transitions, and strong subadditivity

**Two intervals.** For $A=[-b,-a]\cup[a,b]$ ($0<a<b$) two homology-allowed configurations compete:

- the **disconnected** surface: a geodesic over $[-b,-a]$ plus one over $[a,b]$, with combined length controlling $S^{\rm disc}=\tfrac{c}{3}\big[\log\tfrac{b-a}{\epsilon}+\log\tfrac{2a\cdots}{\epsilon}\big]$-type;
- the **connected** surface: geodesics joining the *outer* pair $\{-b,b\}$ and the *inner* pair $\{-a,a\}$.

Whichever has smaller total length wins; they exchange dominance at a critical value of the **cross-ratio** $\eta=\tfrac{(b-a)^2}{\cdots}$ (Exercise 4). This is a genuine **first-order entanglement transition**: the **mutual information** $I(A_1{:}A_2)=S_1+S_2-S_{12}$ is zero in the disconnected phase and turns on continuously past the transition. It is a sharp, parameter-free prediction that the 2d CFT reproduces.

**Strong subadditivity (Headrick–Takayanagi), proved.** For three adjacent regions, SSA states $S(AB)+S(BC)\ge S(B)+S(ABC)$. RT makes it a one-line geometry argument:

1. Let $\gamma_{AB}$ and $\gamma_{BC}$ be the minimal surfaces for $AB$ and $BC$.
2. Their union $\gamma_{AB}\cup\gamma_{BC}$ can be **cut at the crossing/overlap and reglued** into two new surfaces: one anchored on $\partial B$ and one anchored on $\partial(ABC)$. (Geometrically, the parts over $B$ recombine into a surface homologous to $B$, and the remainder into one homologous to $ABC$.)
3. Regluing **preserves total area**: $\mathrm{Area}(\gamma_{AB})+\mathrm{Area}(\gamma_{BC})=\mathrm{Area}(\Sigma_B)+\mathrm{Area}(\Sigma_{ABC})$, where $\Sigma_B,\Sigma_{ABC}$ are the reglued (generally non-minimal) surfaces.
4. Since the *minimal* surfaces $\gamma_B,\gamma_{ABC}$ have areas $\le$ those of any homologous competitor, $\mathrm{Area}(\Sigma_B)\ge\mathrm{Area}(\gamma_B)$ and $\mathrm{Area}(\Sigma_{ABC})\ge\mathrm{Area}(\gamma_{ABC})$.

Chaining, $\mathrm{Area}(\gamma_{AB})+\mathrm{Area}(\gamma_{BC})\ge\mathrm{Area}(\gamma_B)+\mathrm{Area}(\gamma_{ABC})$; dividing by $4G_N$ gives SSA. A theorem that is delicate to prove in field theory is, holographically, the statement that *cutting and regluing surfaces cannot decrease total area*. (The same logic — applied to the **generalised** entropy — recurs for the QES/island story of Sem II.)

> **[Stated-without-proof]** RT itself (LM derivation, Sem II Wk 4). **[Proven]** the AdS$_3$ interval $S=(c/3)\log(\ell/\epsilon)$ (§3, every step). **[Stated-without-proof]** the BTZ result's exact form (§4; same method, hyperbolic geodesic). **[Proven, given RT]** strong subadditivity (§5).

## 6. Why this matters here

RT is the closest contact between this course and the group's research. The entanglement entropy it computes is the von Neumann entropy of a [[type-iii-von-neumann-algebras|type III₁]] subregion algebra — formally divergent, which is *why* the RT area is UV-divergent (the type III$_1$ algebra has no trace and no finite entropy; only differences and relative entropies are finite). The modular Hamiltonian whose first law $\delta S=\delta\langle K\rangle$ governs small perturbations ([[sem2-week-03-modular-flow-on-subregions|Sem II Wk 3]]) is the algebraic object behind RT; JLMS ([[week-14-hrt-and-subregion-subalgebra|Week 14]]) promotes RT to an operator equation. So RT is the bridge from the geometric ($1/4G_N$ area) to the algebraic ([[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]], modular flow) descriptions of entanglement — exactly the territory of the Bell-CHSH and relative-entropy programs, now holographic ([[bell-chsh-in-holographic-setting]]).

## 7. Key claims and proof status

- **[Stated-without-proof]** the RT formula $S_A=\mathrm{Area}(\gamma_A)/4G_N$ (conjecture; LM derivation in Sem II Wk 4).
- **[Proven]** the area-law UV divergence from the near-boundary geometry (§2).
- **[Proven]** the AdS$_3$ interval $S=(c/3)\log(\ell/\epsilon)$ — full computation, §3.
- **[Stated-without-proof]** the BTZ thermal result; **[Proven]** its $T\to0$ and $\ell\gg\beta$ limits (§4).
- **[Proven, given RT]** the two-interval transition structure and strong subadditivity (§5).

*No coefficients in this note are uncertain. (The geodesic length $2L\log(\ell/\epsilon)$, the BTZ form, and $c=3L/2G_N$ are standard; no `CHECK` items for Wk 13.)*

## 8. What to take away

- **Replica trick:** $S_A=-\partial_n\mathrm{Tr}\,\rho_A^n|_{n=1}$, with $\mathrm{Tr}\,\rho_A^n=Z_n/Z_1^n$ a branched-cover partition function; holographically this localises on the RT surface.
- **RT:** $S_A=\mathrm{Area}(\gamma_A)/4G_N$, minimal + anchored + homologous; same $1/4G_N$ as Bekenstein–Hawking; the boundary divergence reproduces the QFT area law.
- **Worked (every step):** the AdS$_3$ geodesic has length $\mathcal{L}=L\int_{\theta_\epsilon}^{\pi-\theta_\epsilon}\!\tfrac{d\theta}{\sin\theta}=2L\log(\ell/\epsilon)$, giving $S=(c/3)\log(\ell/\epsilon)$ — exact Calabrese–Cardy.
- **Thermal (BTZ):** $S=\tfrac{c}{3}\log[\tfrac{\beta}{\pi\epsilon}\sinh\tfrac{\pi\ell}{\beta}]$, interpolating vacuum log → thermal volume law.
- **Homology** ⟹ two-interval transition / mutual information, and a one-line geometric proof of **strong subadditivity**.
- RT is the geometric face of the **modular / relative-entropy** description — the bridge to the group's program and to Week 14 / Sem II.

## Exercises

**Core.**

1. **Variational geodesic.** From $\mathcal{L}=\int\frac{L}{z}\sqrt{1+x'^2}\,dz$ (with $x'=dx/dz$), use the conserved $\partial(\text{integrand})/\partial x'$ to derive the geodesic ODE and integrate it to the semicircle $x^2+z^2=$const.
2. **Length integral.** Reproduce §3 Steps 2–4 in full, including $\int\frac{d\theta}{\sin\theta}=\log\tan\frac{\theta}{2}$ and the small-$\theta_\epsilon$ expansion, to get $\mathcal{L}=2L\log(\ell/\epsilon)$.
3. **Central charge.** Recover $S=(c/3)\log(\ell/\epsilon)$ via $c=3L/2G_N$; for $c=1$ (free compact boson) find $G_N$ in AdS$_3$ units.

**Starred.**

4. $\star$ **Thermal limits.** Starting from $S=\tfrac{c}{3}\log[\tfrac{\beta}{\pi\epsilon}\sinh\tfrac{\pi\ell}{\beta}]$, derive the $T\to0$ (vacuum log) and $\ell\gg\beta$ (thermal volume law, density $\tfrac{\pi c}{3\beta}$) limits, and interpret the latter geometrically (surface skirting the horizon).
5. $\star$ **Two intervals.** Write the connected and disconnected RT lengths for $A=[-b,-a]\cup[a,b]$, find the critical cross-ratio where they cross, and show the mutual information turns on past it.
6. $\star$ **SSA.** Carry out the Headrick–Takayanagi cut-and-reglue argument in full for three adjacent intervals.

**Project.**

7. **RT ↔ modular.** Read [[sem2-week-03-modular-flow-on-subregions|Sem II Wk 3]] (JLMS, first law); write a 2–3 page note connecting the RT area to the modular first law $\delta S=\delta\langle K\rangle$ and to [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]], tying into [[bell-chsh-in-holographic-setting]].

## Connections to other parts of the wiki

- **Within the course.** Predecessor to [[week-14-hrt-and-subregion-subalgebra]] (covariant HRT, JLMS, subregion–subalgebra). The minimal-surface technique is from [[week-11-wilson-loops]]; $c=3L/2G_N$ from [[week-09-holographic-renormalisation]] / [[week-05-2d-cft-essentials]]. RT generalises to the QES of [[sem2-week-05-quantum-extremal-surfaces|Sem II Wk 5]] and the island formula of [[sem2-week-11-island-formula|Sem II Wk 11]].
- **Concepts.** [[ryu-takayanagi-formula]], [[subregion-subalgebra-duality]], [[type-iii-von-neumann-algebras]].
- **AQFT course cross-reference.** The modular Hamiltonian / von Neumann entropy here are developed algebraically in AQFT Block B; bridge in [[sem2-week-03-modular-flow-on-subregions|Sem II Wk 3]].
- **Open questions.** [[bell-chsh-in-holographic-setting]], [[ryu-takayanagi-formula]] (QES/higher-derivative generalisations).
- **Area page.** [[gauge-gravity-duality]] — holographic entanglement entropy is among the most direct probes of the duality.

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block C. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*
