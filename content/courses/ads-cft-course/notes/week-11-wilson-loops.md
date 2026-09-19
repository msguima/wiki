---
title: "Week 11 — Wilson loops and the area-of-string prescription"
type: lecture-notes
course: syllabus
semester: 1
week: 11
block: C
duration: "4 hours (2 lectures × 2 hours)"
status: drafting
modified: 2026-05-28
---

# Week 11 — Wilson Loops and the Area-of-String Prescription

> *Block B built the dictionary for local single-trace operators; Block C applies it to physical probes. The first is the **Wilson loop** — a non-local, gauge-invariant operator measuring the phase a fundamental quark picks up around a loop. Its holographic dual is geometric and vivid: a **minimal-area string worldsheet** hanging into the bulk from the loop on the boundary. We compute the quark–antiquark potential, finding the strong-coupling hallmark $V(L)\propto-\sqrt\lambda/L$ (Coulombic, conformal), and see qualitatively how a black-hole horizon turns this into confinement/screening — the bridge to [[week-12-finite-temperature-ads-schwarzschild|Week 12]]. The minimal-surface technique here is also the warm-up for Ryu–Takayanagi ([[week-13-ryu-takayanagi|Week 13]]).*

## Learning goals

By the end of this week, a student can:

1. Define the Wilson loop and state its physical content (quark worldline) and gauge invariance.
2. State the area-of-string prescription $\langle W[\mathcal{C}]\rangle\approx e^{-S_{\rm NG}[\Sigma_\mathcal{C}]}$ and why it holds at large $N$, large $\lambda$.
3. **Derive** the minimal-surface profile for the static $q\bar q$ configuration and extract $V(L)\propto-\sqrt\lambda/L$.
4. Contrast the strong-coupling $\sqrt\lambda$ with the weak-coupling $\lambda$, and the conformal $1/L$ with confinement.
5. Explain qualitatively how AdS-Schwarzschild produces screening/confinement.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *AdS/CFT Foundations* §7** — the *Wilson Loops* page; *Advanced AdS/CFT* §7 for branes, defects and the baryon vertex.
- Maldacena, *Wilson loops in large N field theories*, [arXiv:hep-th/9803002](https://arxiv.org/abs/hep-th/9803002) — the original $q\bar q$ potential.
- AGMOO, [arXiv:hep-th/9905111](https://arxiv.org/abs/hep-th/9905111), §3.5.

**Prerequisites.** [[week-06-ads-geometries]] (Poincaré metric), [[week-07-large-n-and-thooft-limit]] (large $N$, large $\lambda$). Standard GR/variational calculus.

**AQFT cross-reference.** None — Wilson loops sit outside the algebraic framework.

## 1. The Wilson loop

For a closed curve $\mathcal{C}$, the Wilson loop is

$$
W[\mathcal{C}] = \frac1N\,\mathrm{Tr}\,\mathcal{P}\exp\!\Big(i\oint_\mathcal{C} A_\mu\,dx^\mu\Big),
$$

a gauge-invariant operator ($\mathcal{P}$ = path ordering). Physically it inserts the worldline of an infinitely heavy fundamental quark traversing $\mathcal{C}$. A rectangular loop of spatial width $L$ and temporal extent $T\to\infty$ measures the **static quark–antiquark potential**:

$$
\langle W[\mathcal{C}]\rangle \;\sim\; e^{-T\,V(L)}\qquad(T\to\infty),
$$

so $V(L)$ is read off from the loop expectation value. At *weak* coupling, one-gluon exchange gives a Coulomb potential $V(L)=-\tfrac{\lambda}{4\pi^2 L}$ (in $\mathcal{N}=4$). The holographic computation gives the *strong*-coupling answer.

## 2. The area-of-string prescription

In the dual string theory, a fundamental quark on the boundary is the endpoint of a fundamental string extending into the bulk. The Wilson loop therefore fixes the boundary of an open-string worldsheet, and

$$
\boxed{\;\langle W[\mathcal{C}]\rangle \;\approx\; e^{-S_{\rm NG}[\Sigma_\mathcal{C}]},\qquad
S_{\rm NG} = \frac{1}{2\pi\alpha'}\int d^2\sigma\,\sqrt{h},\;}
$$

where $\Sigma_\mathcal{C}$ is the minimal-area worldsheet ending on $\mathcal{C}\subset\partial\mathrm{AdS}$ and $h$ is the induced metric. At large $\lambda$ the string is heavy ($L^2/\alpha'=\sqrt\lambda$), so the path integral is dominated by the minimal-area saddle — a classical area problem. (A first-principles derivation needs string theory; we take the prescription as given and check it.)

## 3. The quark–antiquark potential (worked)

Take two static quarks at $x=\pm L/2$ in Poincaré AdS, $ds^2=\tfrac{L_{\rm AdS}^2}{z^2}(dz^2+dx^2+dt^2)$ (write $L_{\rm AdS}$ for the AdS radius to avoid clash with the separation $L$). The worldsheet is translation-invariant in $t$ with profile $z(x)$; the Nambu–Goto Lagrangian per unit time is

$$
\mathcal{L} = \frac{L_{\rm AdS}^2}{z^2}\sqrt{1+z'^2},\qquad z'=\frac{dz}{dx}.
$$

Since $\mathcal{L}$ has no explicit $x$-dependence, the "Hamiltonian" is conserved:

$$
\mathcal{H} = \mathcal{L} - z'\frac{\partial\mathcal{L}}{\partial z'} = \frac{L_{\rm AdS}^2}{z^2}\frac{1}{\sqrt{1+z'^2}} = \text{const} = \frac{L_{\rm AdS}^2}{z_*^2},
$$

evaluating the constant at the turning point $z=z_*$ (the deepest point, $z'=0$, at $x=0$). Solving for the slope,

$$
\boxed{\;z'(x) = \frac{\sqrt{z_*^4 - z^4}}{z^2}.\;}
$$

So the profile is **not** a semicircle (that is the flat-space answer) but an elliptic-integral curve. Integrating gives the separation in terms of the turning point:

$$
\frac{L}{2} = \int_0^{z_*}\frac{dz}{z'} = \int_0^{z_*}\frac{z^2\,dz}{\sqrt{z_*^4-z^4}} = z_*\int_0^1\frac{u^2\,du}{\sqrt{1-u^4}}\quad(u=z/z_*),
$$

The remaining integral is a **Beta function**: substituting $w=u^4$ ($du=\tfrac14 w^{-3/4}dw$, $u^2=w^{1/2}$),

$$
\int_0^1\frac{u^2\,du}{\sqrt{1-u^4}} = \frac14\int_0^1 w^{-1/4}(1-w)^{-1/2}\,dw = \frac14\,B\!\Big(\tfrac34,\tfrac12\Big) = \frac14\,\frac{\Gamma(\tfrac34)\Gamma(\tfrac12)}{\Gamma(\tfrac54)} = \frac{\sqrt{2\pi^3}}{\Gamma(1/4)^2},
$$

using $\Gamma(\tfrac12)=\sqrt\pi$, $\Gamma(\tfrac54)=\tfrac14\Gamma(\tfrac14)$, and the reflection identity $\Gamma(\tfrac14)\Gamma(\tfrac34)=\pi\sqrt2$. So $L=z_*\cdot 2\sqrt{2\pi^3}/\Gamma(1/4)^2$,

i.e. the deepest reach $z_*\propto L$ — the string probes a bulk depth set by the separation (UV/IR: larger $L$ ↔ deeper bulk ↔ IR). The on-shell area is UV-divergent (the strings go to $z=0$, the infinite bare quark mass); subtracting the two straight strings (the self-energy) renders it finite, and the result is the celebrated Maldacena potential:

$$
\boxed{\;V(L) = -\frac{4\pi^2\,\sqrt{\lambda}}{\Gamma(1/4)^4}\,\frac{1}{L}.\;}
$$

Two features carry the physics:

- **$\propto1/L$**: a pure Coulomb law with no scale — forced by conformal invariance (the vacuum CFT has no scale, so $V$ can only depend on $L$ by dimensions). This is the **deconfined/Coulomb phase**.
- **$\propto\sqrt\lambda$**: the strong-coupling signature, contrasting sharply with the weak-coupling $V\propto\lambda$. The crossover $\lambda\to\sqrt\lambda$ is a genuine prediction of the duality (and the non-analytic $\sqrt\lambda$ could never come from finite-order perturbation theory).

> **[Sketched]** the area-of-string prescription (string saddle point). **[Proven within the model]** the profile $z'(x)$, the relation $L\propto z_*$, and the scaling $V\propto-\sqrt\lambda/L$ (the variational computation above). The exact coefficient $4\pi^2/\Gamma(1/4)^4$ is Maldacena's standard result <!-- CHECK: exact numerical coefficient (and possible factor of sqrt(2)) against Maldacena hep-th/9803002 before quoting as final -->.

## 4. Confinement, screening, and deconfinement

The Coulomb law above is the vacuum (conformal) answer — **no confinement** in pure AdS, as expected for a CFT (a scale-invariant theory cannot have a string tension). Confinement requires breaking conformal invariance, which holography implements by **modifying the deep interior** of the geometry:

- A **confining geometry** (e.g. an IR wall, or a cutoff/cap at some $z=z_{\rm IR}$) stops the worldsheet from descending past $z_{\rm IR}$. For large $L$ the surface runs flat along the wall, and its area grows *linearly* in $L$: $V(L)\sim\sigma\,L$ with string tension $\sigma\sim L_{\rm AdS}^2/(2\pi\alpha'\,z_{\rm IR}^2)$ — **linear confinement**.
- At **finite temperature** (AdS-Schwarzschild, [[week-12-finite-temperature-ads-schwarzschild|Week 12]]), a horizon at $z=z_h$ caps the geometry. Beyond a screening length $L_{\rm screening}\sim z_h$ the connected worldsheet ceases to exist (it would fall through the horizon); the quarks are **screened** — the deconfined-plasma phase. The Hawking–Page transition (Week 12) between thermal AdS and the black hole is the bulk dual of the confinement/deconfinement transition.

> **[Stated-without-proof]** linear confinement in a confining geometry and screening at finite $T$; the qualitative worldsheet argument is given, the quantitative finite-$T$ computation is Week 12 / Exercise 4.

## 5. Key claims and proof status

- **[Sketched]** $\langle W\rangle\approx e^{-S_{\rm NG}[\Sigma]}$ at large $N$, large $\lambda$ (string saddle; §2).
- **[Proven within the model]** minimal-surface profile, $L\propto z_*$, and $V\propto-\sqrt\lambda/L$ (§3).
- **[CHECK-flagged]** the exact coefficient $4\pi^2/\Gamma(1/4)^4$ (Maldacena) — robust scaling, numerical factor to confirm.
- **[Stated-without-proof]** linear confinement / finite-$T$ screening (§4).

### `CHECK` items (Wk 11)
1. **§3** — the exact numerical coefficient of $V(L)$ ($4\pi^2/\Gamma(1/4)^4$, and whether a $\sqrt2$ appears) against Maldacena hep-th/9803002. The $\propto-\sqrt\lambda/L$ scaling is not in doubt.

## 6. What to take away

- The **Wilson loop** measures the static $q\bar q$ potential; its holographic dual is a **minimal-area string worldsheet** ending on the loop, $\langle W\rangle\approx e^{-S_{\rm NG}}$ (large $N$, large $\lambda$).
- **Worked**: conserved $\mathcal{H}$ gives $z'=\sqrt{z_*^4-z^4}/z^2$ (an elliptic curve, *not* a semicircle), $L\propto z_*$, and $V(L)=-\tfrac{4\pi^2\sqrt\lambda}{\Gamma(1/4)^4 L}$.
- **$1/L$** = conformal Coulomb (deconfined vacuum); **$\sqrt\lambda$** = strong-coupling, non-perturbative signature.
- **Confinement** needs a modified interior (IR wall → linear $V$); **finite $T$** (horizon) → screening; Hawking–Page (Week 12) = the bulk confinement/deconfinement transition.
- The minimal-surface method reappears for entanglement entropy in [[week-13-ryu-takayanagi|Week 13]].

## Exercises

**Core.**

1. **Minimal-surface ODE.** From $\mathcal{L}=\tfrac{L_{\rm AdS}^2}{z^2}\sqrt{1+z'^2}$, derive the conserved $\mathcal{H}$ and hence $z'=\sqrt{z_*^4-z^4}/z^2$. (Note: the flat-space minimal surface would be a semicircle $z=\sqrt{(L/2)^2-x^2}$ — show explicitly that it does **not** solve the AdS equation, and why.)
2. **Potential.** Compute $L(z_*)$ and the regularised area; subtract the straight-string self-energy and obtain $V(L)\propto-\sqrt\lambda/L$. (Aim for the coefficient; flag where the Beta-function/$\Gamma$ values enter.)
3. **Scaling check.** Confirm $V\propto-\sqrt\lambda/L$ is the unique scale-invariant possibility, given $\sqrt\lambda$ dimensionless and the vacuum CFT scaleless.

**Starred.**

4. $\star$ **Screening length.** In AdS-Schwarzschild with horizon $z_h$, argue that the connected worldsheet exists only for $L\lesssim L_{\rm screening}\sim z_h$; estimate $L_{\rm screening}$.
5. $\star$ **Confining wall.** For a geometry capped at $z=z_{\rm IR}$, show the large-$L$ worldsheet gives $V\sim\sigma L$ and identify $\sigma$.

**Project.**

6. **Confinement order parameter.** Connect the Wilson-loop area/perimeter law to the confinement/deconfinement transition and to the Hawking–Page transition of [[week-12-finite-temperature-ads-schwarzschild|Week 12]]; relate to the group's interest in confinement diagnostics ([[confinement]]).

## Connections to other parts of the wiki

- **Within the course.** Sequel: [[week-12-finite-temperature-ads-schwarzschild]] (Hawking–Page = confinement/deconfinement). The minimal-surface method is reused in [[week-13-ryu-takayanagi]]. Builds on [[week-06-ads-geometries]], [[week-07-large-n-and-thooft-limit]].
- **Concepts.** [[holographic-dictionary]] (Wilson loops are non-local probes beyond single-trace operators).
- **Cross-area.** [[confinement]] — the holographic confinement criterion connects to the group's gauge-theory work.
- **Area page.** [[gauge-gravity-duality]] — Wilson loops were among the earliest precision tests of the duality.

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block C. Draft (status: drafting) — pending expert review; see the `CHECK` item in §5 for the exact $V(L)$ coefficient. Last revised 2026-05-28.*
