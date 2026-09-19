---
title: "Sem II Week 6 — JT gravity revisited: Page curve in a tractable model"
type: lecture-notes
course: syllabus
semester: 2
week: 6
block: 1
duration: "3 hours (lecture + seminar)"
status: drafting
modified: 2026-05-28
---

# Sem II Week 6 — JT Gravity Revisited: the Page Curve in a Tractable Model

> *Everything in Block 1 converges here on one explicit calculation. In **JT gravity coupled to a bath** — the cleanest model of an (eternal or evaporating) black hole — we compute the radiation entropy with the QES prescription of [[sem2-week-05-quantum-extremal-surfaces|Wk 5]] and watch the **Page curve** appear: an early no-island saddle gives the rising Hawking branch, a late island saddle saturates at $2S_{\rm BH}$, and the crossover is the Page time. Every quantity is explicit because the boundary theory is the soluble Schwarzian ([[week-15-jt-gravity-intro|Sem I Wk 15]]). This is the concrete realisation of the island formula of [[sem2-week-11-island-formula|Wk 11]].*

## Learning goals

By the end of this week, a student can:

1. Set up the eternal JT + bath geometry and the radiation region.
2. Recall the Schwarzian disk partition function and $S_{\rm BH}=S_0+2\pi^2C/\beta$.
3. **Compute** the no-island (Hawking) entropy via the 2d Calabrese–Cardy formula and show it rises.
4. **Extremise** the island saddle and obtain the saturation $S\approx2S_{\rm BH}$.
5. Read off the Page time and connect to replica wormholes.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Black Hole Information* §4** — *JT Gravity and the Schwarzian* and *The Page Curve in JT Gravity*. A BHI-track week despite sitting in Block 1.
- Almheiri, Engelhardt, Marolf, Maxfield (**AEMM**), [arXiv:1905.08762](https://arxiv.org/abs/1905.08762).
- Almheiri, Mahajan, Maldacena, Zhao, [arXiv:1908.10996](https://arxiv.org/abs/1908.10996).

**Prerequisites.** [[week-15-jt-gravity-intro]] (JT, Schwarzian), [[sem2-week-05-quantum-extremal-surfaces]] (QES), [[week-13-ryu-takayanagi]] (Calabrese–Cardy), [[sem2-week-11-island-formula]] (the island formula this realises).

**AQFT cross-reference.** None directly; the algebraic version is the crossed-product trace ([[crossed-product-and-island-formula]]).

## 1. The JT + bath setup

Take JT gravity ([[week-15-jt-gravity-intro|Sem I Wk 15]]) in the **eternal** (two-sided) configuration at inverse temperature $\beta$, glued at each boundary to a **non-gravitating** flat bath carrying a 2d CFT of central charge $c$. Hawking quanta produced in the gravitating throat stream into the baths; we collect the **radiation** in $R=(-\infty,b_-]\cup[b_+,\infty)$ (one semi-infinite interval per bath). The gravitating region is rigid AdS$_2$; all dynamics is the boundary Schwarzian plus the bath CFT. This is the simplest setting where $S_{\rm bulk}$ is computable in closed form (a 2d CFT interval entropy).

## 2. The Schwarzian partition function and $S_{\rm BH}$

From [[week-15-jt-gravity-intro|Sem I Wk 15]], the JT disk partition function is the Schwarzian path integral, exact at one loop:

$$
Z_{\rm disk}(\beta) = e^{S_0}\!\int_0^\infty dE\,\rho(E)\,e^{-\beta E},\qquad \rho(E)=\frac{\sinh(2\pi\sqrt{2CE})}{2\pi^2},
$$

with the saddle giving the black-hole entropy

$$
S_{\rm BH} = S_0 + \frac{2\pi^2 C}{\beta} = S_0 + \frac{\phi_h}{4G_N}.
$$

$S_0=\phi_0/4G_N$ is the extremal entropy; the $\beta$-dependent piece is the dynamical horizon entropy. For the two-sided geometry the relevant total is $2S_{\rm BH}$ (one horizon per side) — the area term that enters $S_{\rm gen}$.

## 3. No-island saddle: the rising Hawking branch (worked)

Apply the QES prescription with **no island** ($I=\varnothing$): $S(R)=S_{\rm bulk}(R)$, the entanglement entropy of the bath CFT on the radiation intervals in the eternal-black-hole state. Using the 2d Calabrese–Cardy formula in the (conformally transformed) two-sided geometry, each bath contributes

$$
S_{\rm bulk}(R)\big|_{\rm one\ side} \simeq \frac{c}{6}\,\log\!\Big[\sinh\frac{2\pi(t-b)}{\beta}\Big] + (\text{const}).
$$

Expand at late time $t\gg b,\beta$: $\sinh\to\tfrac12 e^{2\pi t/\beta}$, so $\tfrac{c}{6}\log\sinh\to\tfrac{c}{6}\cdot\tfrac{2\pi t}{\beta}=\tfrac{\pi c}{3\beta}t$ per side; summing both baths,

$$
S_{\rm no\text{-}island}(t) \simeq \frac{2\pi c}{3\beta}\,t + \dots
$$

— **linear, unbounded growth** (the rising Hawking branch). By itself it violates unitarity, eventually exceeding the black-hole entropy.

> **[Proven, given Calabrese–Cardy]** the no-island entropy grows linearly at rate $2\pi c/3\beta$ (§3; Exercise 2).

## 4. Island saddle: saturation at $2S_{\rm BH}$ (worked)

Now allow an **island** $I=[a_-,a_+]$ straddling the two sides, $\partial I$ near the horizons. The generalised entropy is

$$
S_{\rm gen}^{\rm island} = \underbrace{2S_{\rm BH}}_{\text{two }\partial I:\ 2(\phi_0+\phi(a))/4G_N} + S_{\rm bulk}(R\cup I).
$$

Extremise over the QES position $a$ (offset $\delta$ from the horizon). The dilaton/area term grows as $\partial I$ moves outward; the CFT term decreases as the island captures the interior partners of the collected radiation. Balancing the gradients (the [[sem2-week-05-quantum-extremal-surfaces|Wk 5]] condition $K^{(a)}/4G_N=-\partial S_{\rm bulk}$) places the QES **just outside the horizon**, at $\delta_\star\sim\beta/2\pi$ — "an island outside the horizon." At late times the island purifies the radiation, $S_{\rm bulk}(R\cup I)\to$ const, leaving

$$
\boxed{\;S_{\rm island} \simeq 2S_{\rm BH}\qquad(\text{time-independent}).\;}
$$

The factor 2 is one $S_{\rm BH}$ per side.

> **[Proven within the model]** the island extremisation and saturation $S_{\rm island}\simeq2S_{\rm BH}$ (§4; Exercise 3) — the explicit JT instance of the island formula ([[sem2-week-11-island-formula|Wk 11]]).

## 5. The Page curve and the Page time

The radiation entropy is the minimum:

$$
S(R,t) = \min\big\{\,\underbrace{\tfrac{2\pi c}{3\beta}\,t}_{\text{no island}},\ \underbrace{2S_{\rm BH}}_{\text{island}}\,\big\}.
$$

Rising linearly, then flat at $2S_{\rm BH}$ — the **Page curve**, from an explicit gravity calculation. The crossover (Page time) is where the branches meet, $\tfrac{2\pi c}{3\beta}t_{\rm Page}=2S_{\rm BH}$:

$$
\boxed{\;t_{\rm Page} = \frac{3\beta\,S_{\rm BH}}{\pi c}\;\sim\;\frac{S_0\,\beta}{c}\ (\text{up to }O(1)).\;}
$$

(With $S_{\rm BH}\approx S_0$ at leading order; $O(1)$ factors depend on two-sided bookkeeping.) Every number is explicit because the Schwarzian is soluble — why JT + bath is *the* model for the information problem.

**Replica-wormhole consistency.** The same answer arises from the gravitational path integral: the no-island saddle is the disconnected geometry, the island saddle is the **replica wormhole** ([[sem2-week-10-replica-wormholes|Wk 10]], PSSY), and the $\min$ is the saddle competition; the QES extremisation here is the $n\to1$ shadow of the wormhole. Two independent methods — QES and replica wormholes — give the identical Page curve in this model: the strongest evidence the island rule is correct.

> **[Proven, modulo Schwarzian-as-input]** the JT + bath Page curve from QES (AEMM); **[Stated-without-proof]** the replica-wormhole equivalence (PSSY; Wk 10).

## 6. Key claims and proof status

- **[Proven]** Schwarzian disk $Z(\beta)$, $\rho(E)$, $S_{\rm BH}=S_0+2\pi^2C/\beta$ (§2; Sem I Wk 15).
- **[Proven, given Calabrese–Cardy]** linear rising no-island entropy, rate $2\pi c/3\beta$ (§3).
- **[Proven within the model]** island saturation $S\simeq2S_{\rm BH}$, QES just outside the horizon (§4).
- **[Proven, modulo Schwarzian]** Page curve and $t_{\rm Page}=3\beta S_{\rm BH}/\pi c$ (§5); **[Stated-without-proof]** replica-wormhole equivalence.

*No coefficients in this note are uncertain at the stated level; the $O(1)$ in $t_{\rm Page}$ is two-sided bookkeeping, internally consistent given §§3–4 (no `CHECK`).*

## 7. What to take away

- **JT + bath** is the soluble model: rigid AdS$_2$ + Schwarzian + 2d CFT bath, $S_{\rm bulk}$ from Calabrese–Cardy.
- $S_{\rm BH}=S_0+2\pi^2C/\beta$; two-sided total $2S_{\rm BH}$.
- **No-island** (worked): $S\simeq\tfrac{2\pi c}{3\beta}t$ — rising.
- **Island** (worked): QES just outside the horizon, $S\simeq2S_{\rm BH}$ — plateau.
- **Page curve:** $S=\min\{\text{rising},2S_{\rm BH}\}$, $t_{\rm Page}=3\beta S_{\rm BH}/\pi c$. **Replica wormholes give the same answer** (Wk 10).

## Exercises

**Core.**

1. **Schwarzian saddle.** From $S_{\rm Sch}=-C\int_0^\beta\{f,\tau\}d\tau$, show $f=\tan(\pi\tau/\beta)$ gives $S_{\rm BH}\propto2\pi^2C/\beta$.
2. **Rising branch.** From $S_{\rm bulk}\simeq\tfrac{c}{6}\log\sinh\tfrac{2\pi(t-b)}{\beta}$ per bath, expand at $t\gg b,\beta$ to get $\tfrac{2\pi c}{3\beta}t$.
3. **Island saturation.** Extremise $S_{\rm gen}(b)=2S_{\rm BH}+S_{\rm CFT}(R\cup I)$ at late times; show $S\to2S_{\rm BH}$, QES $\sim\beta$ outside the horizon.

**Starred.**

4. $\star$ **Page time.** Equate the branches for $t_{\rm Page}=3\beta S_{\rm BH}/\pi c$; track the two-sided factors of 2.
5. $\star$ **Replica check.** Sketch the PSSY two-saddle computation in JT and show it reproduces §5.

**Project.**

6. **Evaporating JT.** Extend to an *evaporating* JT black hole (AEMM); show the plateau becomes a falling branch as $S_{\rm BH}(t)$ shrinks, completing the curve to zero.

## Connections to other parts of the wiki

- **Within the course.** Explicit realisation of [[sem2-week-05-quantum-extremal-surfaces]] and [[sem2-week-11-island-formula]]; built on [[week-15-jt-gravity-intro]] and [[week-13-ryu-takayanagi]]; same answer as [[sem2-week-10-replica-wormholes]].
- **Concepts.** [[jt-gravity]], [[page-curve]], [[quantum-extremal-surfaces]].
- **AQFT course cross-reference.** [[crossed-product-and-island-formula]].
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 1. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*
