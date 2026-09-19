---
title: "Week 12 — Finite temperature: AdS-Schwarzschild and Hawking–Page"
type: lecture-notes
course: syllabus
semester: 1
week: 12
block: C
duration: "4 hours (2 lectures × 2 hours)"
status: drafting
modified: 2026-05-28
---

# Week 12 — Finite Temperature: AdS-Schwarzschild and Hawking–Page

> *Turn on a temperature. A thermal CFT is the Euclidean path integral on $S^1_\beta\times\mathbb{R}^{d-1}$ (or $S^1_\beta\times S^{d-1}$); holographically we sum over bulk geometries with that boundary. Two saddles compete — **thermal AdS** and the **AdS-Schwarzschild black hole** — and which dominates flips at the **Hawking–Page transition**, the bulk dual of **confinement/deconfinement** (Witten 1998). We derive the Hawking temperature from Euclidean smoothness and compare free energies. This finishes the deconfinement story begun with Wilson loops ([[week-11-wilson-loops|Week 11]]) and sets up finite-$T$ entanglement entropy ([[week-13-ryu-takayanagi|Week 13]]).*

## Learning goals

By the end of this week, a student can:

1. Explain why a thermal CFT corresponds to summing over bulk geometries with boundary $S^1_\beta\times(\text{space})$, with two competing saddles.
2. **Derive** the Hawking temperature $T_H=d\,r_h/(4\pi L^2)$ from Euclidean regularity.
3. State the Hawking–Page transition as a first-order exchange of dominance between thermal AdS and the black hole.
4. Identify the dual as confinement/deconfinement via the $O(1)\to O(N^2)$ free-energy jump.
5. Connect the entropy/Wilson-loop diagnostics across Weeks 11–12.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *AdS/CFT Foundations* §8** — black branes and thermal CFTs, the Hawking–Page transition, Euclidean free energy.
- Witten, *Anti-de Sitter space, thermal phase transition, and confinement in gauge theories*, [arXiv:hep-th/9803131](https://arxiv.org/abs/hep-th/9803131) — the deconfinement interpretation.
- Hawking, Page (1983), *Thermodynamics of black holes in anti-de Sitter space* — the original transition.

**Prerequisites.** [[week-06-ads-geometries]] (Euclidean AdS, thermal periodicity), [[week-09-holographic-renormalisation]] (on-shell action / free energy), [[week-07-large-n-and-thooft-limit]] ($O(N^2)$ counting), [[week-11-wilson-loops]] (the deconfinement story).

**AQFT cross-reference.** Light: a thermal state is a KMS state, the algebraic notion developed in AQFT 2026 Block B; this lecture takes the gravitational/thermodynamic view. The two meet in [[sem2-week-12-er-epr-and-tfd|Sem II Wk 12]] (TFD).

## 1. Thermal CFT and two bulk saddles

A CFT at inverse temperature $\beta$ is the Euclidean path integral with periodic time, on $S^1_\beta\times S^{d-1}$ (global) or $S^1_\beta\times\mathbb{R}^{d-1}$ (planar). The dictionary says: compute $Z(\beta)$ by summing bulk geometries whose conformal boundary is that space. At least two smooth saddles have the right boundary:

- **Thermal AdS** — global AdS with Euclidean time periodically identified ($\tau\sim\tau+\beta$). A "cigar" only at the AdS scale; the time circle never shrinks. Free energy $O(N^0)$.
- **AdS-Schwarzschild** — a black hole whose Euclidean time circle caps off smoothly at the horizon. Free energy $O(N^2)$.

$Z(\beta)\approx e^{-\beta F_{\rm AdS}}+e^{-\beta F_{\rm BH}}$ is dominated by whichever has the lower free energy — and that switches with temperature.

## 2. AdS-Schwarzschild and the Hawking temperature (worked)

The (global) AdS$_{d+1}$-Schwarzschild metric is

$$
ds^2 = f(r)\,dt^2 + \frac{dr^2}{f(r)} + r^2 d\Omega_{d-1}^2,\qquad
f(r) = \frac{r^2}{L^2} + 1 - \Big(\frac{r_h}{r}\Big)^{d-2}\Big(\frac{r_h^2}{L^2}+1\Big),
$$

with $f(r_h)=0$ defining the horizon. **Derive the temperature** from Euclidean regularity. Continue $t\to-i t_E$ and zoom in near $r_h$: $f(r)\approx f'(r_h)(r-r_h)$. Define a proper radial coordinate $\rho$ by $d\rho=dr/\sqrt{f}$, so $\rho\propto\sqrt{r-r_h}$ and $f\approx \tfrac14 f'(r_h)^2\rho^2$. The $(t_E,\rho)$ part becomes

$$
ds^2 \approx d\rho^2 + \Big(\tfrac{f'(r_h)}{2}\Big)^2\rho^2\,dt_E^2,
$$

which is flat $\mathbb{R}^2$ in polar form **only if** the angle $\tfrac{f'(r_h)}{2}t_E$ has period $2\pi$ — otherwise a conical singularity. Smoothness therefore fixes

$$
\boxed{\;\beta = \frac{4\pi}{f'(r_h)},\qquad T_H = \frac{f'(r_h)}{4\pi}.\;}
$$

Evaluate $f'(r_h)$ explicitly. Differentiating $f(r)=\tfrac{r^2}{L^2}+1-(r_h^2/L^2+1)(r_h/r)^{d-2}$,

$$
f'(r) = \frac{2r}{L^2} + (d-2)\Big(\tfrac{r_h^2}{L^2}+1\Big)\frac{r_h^{d-2}}{r^{d-1}},
$$

and at the horizon $r=r_h$ (where $r_h^{d-2}/r_h^{d-1}=1/r_h$),

$$
f'(r_h) = \frac{2r_h}{L^2} + (d-2)\Big(\tfrac{r_h}{L^2}+\tfrac{1}{r_h}\Big) = \frac{d\,r_h}{L^2} + \frac{d-2}{r_h}.
$$

For a **large** black hole $r_h\gg L$ the first term dominates, giving

$$
\boxed{\;T_H = \frac{d\,r_h}{4\pi L^2}\qquad(r_h\gg L).\;}
$$

(For $d=4$: $T_H=r_h/\pi L^2$.) A striking feature, special to AdS: $T_H$ **increases** with $r_h$ for large black holes — big AdS black holes have *positive* specific heat and are thermodynamically stable, unlike flat-space Schwarzschild. There is a minimum temperature $T_{\min}\sim1/L$ below which no black hole exists.

> **[Proven]** $T_H=f'(r_h)/4\pi$ (Euclidean smoothness) and the large-BH form $d\,r_h/4\pi L^2$ (Exercise 1).

## 3. The Hawking–Page transition

Compute the free energies $F=-T\log Z\approx T\,S_{\rm on\text{-}shell}^{\rm E}$ of the two saddles (holographically renormalised, [[week-09-holographic-renormalisation|Week 9]]; thermal AdS is the reference). The difference $\Delta F=F_{\rm BH}-F_{\rm AdS}$ is positive at low $T$ and negative at high $T$, crossing zero at a critical

$$
T_{HP}\sim \frac{d}{4\pi L}\quad(\text{global AdS; }O(1)\text{ coefficient}),
$$

<!-- CHECK: exact T_HP coefficient for global AdS_{d+1} (e.g. AdS5: T_HP = ?/(2 pi L)); confirm against Witten hep-th/9803131 before quoting a number. -->
so:

- $T<T_{HP}$: **thermal AdS dominates** — small black holes have higher free energy (and the minimum-$T$ black hole has negative specific heat); the saddle is horizon-free.
- $T>T_{HP}$: **the black hole dominates** — a large, stable black hole minimises $F$.

The two saddles do not deform into each other continuously: it is a **first-order** transition (the entropy, $\propto$ horizon area, jumps). This requires the **compact** boundary ($S^{d-1}$); on $\mathbb{R}^{d-1}$ (planar) the black hole dominates at all $T>0$ and there is no transition (a CFT on flat space has no scale to set $T_{HP}$).

> **[Sketched]** the first-order Hawking–Page transition (free-energy comparison; Exercise 2). The exact $T_{HP}$ coefficient is flagged.

## 4. Dual interpretation: confinement/deconfinement

Witten's reading: the Hawking–Page transition **is** the confinement/deconfinement transition of the boundary gauge theory on $S^{d-1}$.

- **Free energy.** Thermal AdS has $F=O(N^0)$ — the confined phase, where gauge invariance leaves only $O(1)$ colour-singlet states (glueballs). The black hole has $F=O(N^2)$ — the deconfined phase, where the $\sim N^2$ gluon degrees of freedom are liberated. The jump from $O(1)$ to $O(N^2)$ across $T_{HP}$ is the order parameter (using the $N$-counting of [[week-07-large-n-and-thooft-limit|Week 7]]).
- **Entropy.** $S_{\rm BH}=\mathrm{Area}/4G_N\sim N^2$ vs $S_{\rm thermal\,AdS}\sim N^0$ — the deconfined plasma has parametrically more entropy.
- **Wilson loops.** Below $T_{HP}$ the spatial Wilson loop has an area law (confining); above, a perimeter law (screened) — completing the [[week-11-wilson-loops|Week 11]] story. The horizon caps the worldsheet, giving the screening length $L_{\rm screening}\sim z_h$.

This is the first **phase transition** computed holographically, and the template for holographic thermodynamics throughout the subject.

> **[Stated-without-proof]** the deconfinement interpretation (Witten); the $O(N^2)$ jump is the diagnostic, given large-$N$ assumptions.

## 5. Key claims and proof status

- **[Proven]** Hawking temperature $T_H=f'(r_h)/4\pi=d\,r_h/4\pi L^2$ (Euclidean smoothness, §2).
- **[Sketched]** first-order Hawking–Page transition; **[CHECK-flagged]** exact $T_{HP}$ coefficient (§3).
- **[Stated-without-proof]** dual = confinement/deconfinement; $O(1)\to O(N^2)$ free-energy jump (§4).

### `CHECK` items (Wk 12)
1. **§3** — the exact $T_{HP}$ coefficient for global AdS$_{d+1}$ (the $T_H$ and large-BH results are unambiguous; only the transition temperature's numerical factor is flagged).

## 6. What to take away

- Thermal CFT ↔ sum over bulk saddles with thermal boundary; **thermal AdS** vs **AdS-Schwarzschild** compete.
- **Hawking $T$** from Euclidean smoothness: $\beta=4\pi/f'(r_h)$, $T_H=d\,r_h/4\pi L^2$ (large BH); big AdS black holes have **positive specific heat** (stable), with a minimum temperature $\sim1/L$.
- **Hawking–Page**: first-order exchange of dominance at $T_{HP}\sim 1/L$; needs a compact boundary.
- **Dual = confinement/deconfinement**: $F$ jumps $O(1)\to O(N^2)$; entropy $\sim N^2$; Wilson loop area→perimeter (completing Week 11).
- First phase transition computed holographically; template for holographic thermodynamics.

## Exercises

**Core.**

1. **Hawking temperature.** For AdS$_5$-Schwarzschild ($f(r)=r^2/L^2+1-M/r^2$, $f(r_h)=0$), derive $T_H$ from $\beta=4\pi/f'(r_h)$ and take the large-$r_h$ limit.
2. **Free-energy crossover.** Compute the (renormalised) Euclidean on-shell action of AdS$_5$-Schwarzschild relative to thermal AdS; show $\Delta F$ changes sign and identify $T_{HP}$ (flag the exact coefficient).
3. **$N$-counting.** Using [[week-07-large-n-and-thooft-limit|Week 7]], explain why $F=O(N^0)$ (confined) below and $O(N^2)$ (deconfined) above $T_{HP}$.

**Starred.**

4. $\star$ **Specific heat.** Show that large AdS black holes have $dS/dT>0$ (positive specific heat), unlike flat-space Schwarzschild, and locate the minimum-temperature black hole.
5. $\star$ **Planar case.** Show that on $\mathbb{R}^{d-1}$ there is no Hawking–Page transition (the black hole dominates for all $T>0$); relate to the absence of a scale in a flat-space CFT.

**Project.**

6. **Confinement order parameter.** Tie together the Wilson-loop area/perimeter law (Week 11), the $O(N^2)$ free-energy jump, and the Polyakov loop as deconfinement order parameters; connect to the group's confinement interests ([[confinement]]).

## Connections to other parts of the wiki

- **Within the course.** Completes the deconfinement story of [[week-11-wilson-loops]]; prerequisite for finite-$T$ entanglement in [[week-13-ryu-takayanagi]]. The AdS$_3$ (BTZ) counterpart and its Cardy entropy are [[sem2-week-07-ads2-ads3-essentials|Sem II Wk 7]] / [[week-05-2d-cft-essentials|Wk 5]]. The eternal two-sided black hole / TFD is [[sem2-week-12-er-epr-and-tfd|Sem II Wk 12]].
- **Concepts.** [[holographic-dictionary]].
- **Cross-area.** [[confinement]] — holographic confinement/deconfinement connects to the group's gauge-theory work.
- **Area page.** [[gauge-gravity-duality]] — the first holographic phase transition.

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block C. Draft (status: drafting) — pending expert review; see the `CHECK` item in §5 for the exact $T_{HP}$ coefficient. Last revised 2026-05-28.*
