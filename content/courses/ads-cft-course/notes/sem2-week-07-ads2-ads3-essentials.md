---
title: "Sem II Week 7 — AdS2/CFT1 and AdS3/CFT2 essentials"
type: lecture-notes
course: syllabus
semester: 2
week: 7
block: 1
duration: "3 hours (lecture + seminar)"
status: drafting
modified: 2026-05-28
---

# Sem II Week 7 — AdS₂/CFT₁ and AdS₃/CFT₂ Essentials

> *Block 1 closes by anchoring the abstract machinery in the two **soluble** low-dimensional cases. **AdS₃/CFT₂** is where holography is sharpest: Brown–Henneaux shows the asymptotic symmetry is two Virasoros with $c=3\ell/2G_N$, and the **BTZ** black hole's Bekenstein–Hawking entropy is reproduced exactly by **Cardy** — the cleanest microscopic black-hole entropy count. **AdS₂/CFT₁** is where holography is subtlest: there is no honest 1d CFT, only the Schwarzian, and the SYK model realises it. We derive Brown–Henneaux and the BTZ=Cardy match, and explain the AdS₂ story.*

## Learning goals

By the end of this week, a student can:

1. Explain why AdS₂ has no proper CFT₁ dual, and the Schwarzian/SYK resolution.
2. Relate near-extremal black-hole throats (AdS₂×$S^2$) to JT gravity and $S_0$.
3. **Derive** the Brown–Henneaux central charge $c=3\ell/2G_N$ from asymptotic symmetries.
4. Write the BTZ metric, compute $T_H$ and $S_{\rm BH}$, and **verify** BTZ = Cardy.
5. State the SYK conformal-symmetry-breaking pattern.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Advanced AdS/CFT* §14** — *AdS3/CFT2 and Brown-Henneaux*; *AdS/CFT Foundations* §10 is the cleaner first read, and the Guides carry a fuller *AdS3/CFT2 Guide*.
- Brown, Henneaux, *Central charges in the canonical realization of asymptotic symmetries*, Commun. Math. Phys. 104 (1986) 207.
- Strominger, *Black hole entropy from near-horizon microstates*, [arXiv:hep-th/9712251](https://arxiv.org/abs/hep-th/9712251).

**Prerequisites.** [[week-05-2d-cft-essentials]] (Virasoro, Cardy), [[week-12-finite-temperature-ads-schwarzschild]] (AdS black holes, $T_H$), [[week-15-jt-gravity-intro]] (JT/Schwarzian), [[week-09-holographic-renormalisation]] (holographic $c=3L/2G$). Asymptotic symmetry groups / surface charges.

**AQFT cross-reference.** Structural parallel to the Virasoro/chiral-algebra discussion; not developed here.

## 1. AdS₂ subtleties and SYK

AdS₂ is the $d=1$ case, and it is genuinely singular as a holographic setup: the boundary is a *point* (two disconnected points for global AdS₂), not a manifold, so there is no honest 1d "CFT" — and AdS₂ suffers from **fragmentation** (any finite energy backreacts and destroys the throat). The resolution is **near**-AdS₂ (NAdS₂): keep the leading dilaton correction, and the only boundary degree of freedom is the **Schwarzian** mode $f(\tau)$ ([[week-15-jt-gravity-intro|Sem I Wk 15]]). At finite temperature the $\mathrm{SL}(2,\mathbb{R})$ isometry is **softly broken to $\mathrm{U}(1)$** (time translation), and the Schwarzian is the (pseudo-)Goldstone of that breaking.

**SYK** realises exactly this: $N$ Majorana fermions with random $q$-body couplings flow at low energy to a strongly-interacting fixed point with emergent reparametrisation symmetry broken to $\mathrm{SL}(2,\mathbb{R})$, and the low-energy effective action is the **Schwarzian** $S=-N\alpha_S\mathcal{J}\!\int d\tau\{f,\tau\}$. So SYK is a concrete quantum-mechanical "CFT₁" dual to NAdS₂/JT, with $N$ playing the role of $1/G_N$.

> **[Stated-without-proof]** the absence of a standard CFT₁ dual and the Schwarzian/SYK resolution (Almheiri–Polchinski; Maldacena–Stanford–Yang).

## 2. Near-extremal throats and JT

Extremal Reissner–Nordström and Kerr–Newman black holes develop an **AdS₂×$S^2$** near-horizon geometry. Dimensionally reducing on the $S^2$ gives **JT gravity**, with the dilaton = the sphere's area and $S_0$ = the **extremal** Bekenstein–Hawking entropy. So the JT model of Block 1/2 is not a toy but the universal description of the near-extremal regime of real higher-dimensional black holes — which is why the Page-curve calculation of [[sem2-week-06-jt-gravity-page-curve|Wk 6]] has physical reach.

## 3. Brown–Henneaux (worked logic)

In AdS₃ gravity with **Brown–Henneaux boundary conditions** (metric deviations falling off appropriately at the boundary), the asymptotic Killing vectors that preserve the boundary conditions form **two copies of the Virasoro algebra** (left and right movers) — *not* just the finite $\mathrm{SL}(2,\mathbb{R})\times\mathrm{SL}(2,\mathbb{R})$. Computing the Poisson-bracket algebra of the associated **Regge–Teitelboim surface charges** $L_m$, one finds a central extension:

$$
\{L_m,L_n\} = (m-n)L_{m+n} + \frac{c}{12}m(m^2-1)\delta_{m+n,0},\qquad
\boxed{\;c = \frac{3\ell}{2G_N}.\;}
$$

So **3d gravity has a boundary CFT₂ with central charge $c=3\ell/2G_N$** — discovered by Brown–Henneaux in 1986, a decade before Maldacena, and the first concrete instance of holography. This is the same $c$ obtained from the holographic Weyl anomaly ([[week-09-holographic-renormalisation|Wk 9]]) and used in the RT interval entropy ([[week-13-ryu-takayanagi|Wk 13]]) — now from the asymptotic symmetry algebra.

> **[Sketched]** Brown–Henneaux $c=3\ell/2G_N$ from the surface-charge algebra (§3; Exercise 1); the $m^3$ central term is the hallmark.

## 4. BTZ and the Cardy match (worked)

The **BTZ** black hole is the AdS₃ black hole, with inner/outer horizons $r_\pm$:

$$
M = \frac{r_+^2+r_-^2}{8G_N\ell^2},\quad
J = \frac{r_+ r_-}{4G_N\ell},\quad
T_H = \frac{r_+^2-r_-^2}{2\pi\ell^2 r_+},\quad
S_{\rm BH} = \frac{2\pi r_+}{4G_N} = \frac{\pi r_+}{2G_N}.
$$

**Reproduce $S_{\rm BH}$ from Cardy.** Split into left/right movers with $E_L=\tfrac{M\ell+J}{2}$, $E_R=\tfrac{M\ell-J}{2}$. The Cardy formula ([[week-05-2d-cft-essentials|Wk 5]]) with $c=\bar c=3\ell/2G_N$ gives

$$
S_{\rm Cardy} = 2\pi\sqrt{\frac{c\,E_L}{6}} + 2\pi\sqrt{\frac{c\,E_R}{6}}.
$$

Take the non-rotating case ($r_-=0$, $J=0$, $E_L=E_R=\tfrac{M\ell}{2}=\tfrac{r_+^2}{16G_N\ell}$): each term is $2\pi\sqrt{\tfrac{1}{6}\cdot\tfrac{3\ell}{2G_N}\cdot\tfrac{r_+^2}{16G_N\ell}} = 2\pi\sqrt{\tfrac{r_+^2}{64G_N^2}} = \tfrac{\pi r_+}{4G_N}$, and the two sum to

$$
\boxed{\;S_{\rm Cardy} = \frac{\pi r_+}{2G_N} = S_{\rm BH}.\;}
$$

**Exact agreement** — Strominger's count, the cleanest microscopic black-hole entropy in the subject (the rotating case works identically with $E_{L,R}$). The number of CFT₂ microstates at energy $E$, given by Cardy, equals the horizon area in Planck units. This is the AdS₃ refinement of the BTZ exercise of [[week-05-2d-cft-essentials|Sem I Wk 5]], now with the full Brown–Henneaux derivation behind it.

> **[Sketched]** Brown–Henneaux; **[Proven, given Cardy]** BTZ $=$ Cardy entropy (§4; Exercises 2–3). The BTZ mass/temperature/entropy formulas are standard.

## 5. Key claims and proof status

- **[Stated-without-proof]** no standard CFT₁ dual to AdS₂; Schwarzian/SYK resolution; $\mathrm{SL}(2,\mathbb{R})\to\mathrm{U}(1)$ breaking (§1).
- **[Stated-without-proof]** near-extremal throats reduce to JT; $S_0=$ extremal entropy (§2).
- **[Sketched]** Brown–Henneaux $c=3\ell/2G_N$ from surface charges (§3).
- **[Proven, given Cardy]** BTZ entropy $=$ Cardy entropy (§4).

*No coefficients in this note are uncertain. (The BTZ/Brown–Henneaux/Cardy formulas are standard and the BTZ$=$Cardy match is worked; no `CHECK` items for Wk 7.)*

## 6. What to take away

- **AdS₂/CFT₁** has no honest 1d CFT — only the **Schwarzian**, realised by **SYK**; $\mathrm{SL}(2,\mathbb{R})\to\mathrm{U}(1)$ at $T>0$. Near-extremal black-hole throats are AdS₂×$S^2$ → **JT** ($S_0$ = extremal entropy).
- **Brown–Henneaux:** AdS₃'s asymptotic symmetry is two Virasoros with $c=3\ell/2G_N$ — holography, found in 1986.
- **BTZ = Cardy (worked):** $S_{\rm BH}=\pi r_+/2G_N$ is reproduced exactly by Cardy with $c=3\ell/2G_N$ and $E_{L,R}$ — Strominger's microscopic count.
- One $c$, three derivations: $\langle TT\rangle$ OPE (Wk 4/5), holographic anomaly (Wk 9), asymptotic symmetries (here) — all $3\ell/2G_N$.

## Exercises

**Core.**

1. **Brown–Henneaux.** Compute the surface-charge algebra $\{L_m,L_n\}$ for AdS₃ asymptotic Killing vectors; show the central term $\propto m^3$ with $c=3\ell/2G_N$.
2. **BTZ thermodynamics.** For non-rotating BTZ ($r_-=0$), demand Euclidean smoothness to get $T_H=r_+/2\pi\ell^2$ and $S_{\rm BH}=\pi r_+/2G_N$.
3. **Cardy match.** Plug $c=3\ell/2G_N$ and $E=M=r_+^2/8G_N\ell^2$ into $S_{\rm Cardy}=2\pi\sqrt{cE/6}$ (×2 for $L,R$) and verify $S_{\rm Cardy}=S_{\rm BH}$.

**Starred.**

4. $\star$ **SYK Schwarzian.** For SYK ($N$ Majoranas, $q$-body coupling), state the low-energy Schwarzian action, identify $\mathrm{SL}(2,\mathbb{R})\to\mathrm{U}(1)$, and explain why the Schwarzian mode is the Goldstone.
5. $\star$ **Rotating BTZ.** Redo Exercise 3 for $J\ne0$ using $E_{L,R}=(M\ell\pm J)/2$ and verify $S_{\rm Cardy}=2\pi r_+/4G_N$.

**Project.**

6. **Strominger's count.** Read Strominger hep-th/9712251; reproduce the BTZ=Cardy derivation in full, and write a 3-page note tying it to the RT interval entropy of [[week-13-ryu-takayanagi|Wk 13]] and the $c$-derivations of Wks 4, 5, 9.

## Connections to other parts of the wiki

- **Within the course.** Closes Block 1. $c=3\ell/2G_N$ ties to [[week-09-holographic-renormalisation]] (anomaly), [[week-05-2d-cft-essentials]] (Cardy), [[week-13-ryu-takayanagi]] (RT). JT/Schwarzian from [[week-15-jt-gravity-intro]], [[sem2-week-06-jt-gravity-page-curve]]. Block 2 opens at [[sem2-week-08-hawking-radiation-info-problem]].
- **Concepts.** [[jt-gravity]], [[page-curve]] (BTZ thermodynamics underlies the JT model).
- **Open questions.** A proper CFT₁ dual to AdS₂ (open; [[jt-gravity]]); SYK–random-matrix (Phase 3).
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 1. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*

*End of Sem II Block 1 — and of the AdS/CFT course's lecture-note set: all 30 weeks drafted.*
