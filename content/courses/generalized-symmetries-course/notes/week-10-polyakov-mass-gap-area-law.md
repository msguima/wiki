---
title: "Week 10 — Compact QED₃ II: the Mass Gap and the Area Law"
type: lecture-notes
course: syllabus
semester: 1
week: 10
block: C
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Week 9 (the monopole plasma and dual-photon sine-Gordon); solitons; Gaussian screening
modified: 2026-07-01
---

# Week 10 — Compact QED₃ II: the Mass Gap and the Area Law

> *This is the calculation the semester is built toward. Polyakov's 1977 result — that compact electrodynamics in three dimensions confines charge permanently, at every coupling, through a monopole plasma — is the first fully controlled demonstration of confinement in any gauge theory. We reproduce it in two moves: the plasma Debye-screens the photon into a massive pseudo-Goldstone, and a Wilson loop becomes a sine-Gordon domain wall whose tension is the string tension. Track every constant.*

## 0. Reading

**Primary:** Polyakov, *Nucl. Phys. B* 120 (1977) 429; *Gauge Fields and Strings*, ch. 4. This note is a guided reconstruction.

**Secondary:**
- Kogut, *Rev. Mod. Phys.* 51 (1979) 659, §VI.
- Shifman, *Advanced Topics in QFT*, ch. on the Polyakov mechanism.

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]]. This note continues [[week-09-compact-qed3-monopole-plasma|Week 9]] directly; we start from its dual action.

## 1. The starting point

From [[week-09-compact-qed3-monopole-plasma|Week 9]], compact QED₃ is the sine-Gordon theory of the dual photon $\sigma$ (a compact scalar, $\sigma\sim\sigma+2\pi$):
$$
S[\sigma] = \int d^3x\ \Big[\, A\,(\partial\sigma)^2 - 2\zeta\cos\sigma\,\Big],\qquad A \equiv \frac{e^2}{8\pi^2},\quad \zeta \sim e^{-S_{\text{mono}}}.
$$
The free part is the massless photon; the $\cos\sigma$ is the monopole gas, which explicitly breaks the magnetic shift symmetry. We now compute its two consequences.

## 2. The photon mass gap [Computed.]

Expand $\cos\sigma$ around its minimum $\sigma = 0$:
$$
-2\zeta\cos\sigma = -2\zeta + \zeta\,\sigma^2 + O(\sigma^4).
$$
The quadratic action is $\int d^3x\,[A(\partial\sigma)^2 + \zeta\sigma^2]$, a massive scalar. Reading the propagator $\propto (A k^2 + \zeta)^{-1}$, the mass is the ratio of the potential curvature to the kinetic coefficient:
$$
\boxed{\ m_\gamma^2 = \frac{\zeta}{A} = \frac{8\pi^2\zeta}{e^2},\qquad m_\gamma = \frac{2\pi}{e}\sqrt{2\zeta}\ \propto\ e^{-S_{\text{mono}}/2}.\ }
$$
**The photon is gapped.** In three dimensions a massless $U(1)$ photon is *unstable* to monopoles: the plasma Debye-screens it over a length $m_\gamma^{-1}$. The gap is exponentially small at weak coupling (where $S_{\text{mono}} \sim c/e^2 a$ is large) but strictly nonzero at every coupling.

> **Physical picture.** This is the pseudo-Goldstone story of Week 9 made quantitative. The photon *would* be the massless Goldstone of the spontaneously broken magnetic symmetry; the monopole term breaks that symmetry explicitly, so the Goldstone acquires a mass $m_\gamma \propto \sqrt{\text{(explicit breaking)}} = \sqrt\zeta$. There is no massless photon and no long-range Coulomb force in compact QED₃ — a striking failure of the naive continuum theory, entirely due to compactness.

## 3. The Wilson loop as a domain wall [Computed.]

Now insert a Wilson loop $W(C) = \exp\!\big(i\oint_C a\big)$ of unit charge and compute $\langle W(C)\rangle$ in the dual variables.

### 3.1 The source

In the dual description the electric field is $E \propto \partial\sigma$, so a static electric charge is a source for $\sigma$, and a Wilson loop $C$ imposes that $\sigma$ has **monodromy $2\pi$** around $C$: passing once around the loop, $\sigma$ advances by $2\pi$. Equivalently, choosing a surface $\Sigma$ with $\partial\Sigma = C$, the loop forces $\sigma$ to **jump by $2\pi$** across $\Sigma$:
$$
\sigma \to \sigma + 2\pi\,\theta_\Sigma,\qquad \theta_\Sigma = \text{step function across } \Sigma.
$$
The physical answer cannot depend on the choice of $\Sigma$ (the jump is $2\pi$, invisible to $\cos\sigma$ and to $e^{i\sigma}$) — but the *minimal-action* configuration localizes the variation of $\sigma$ near a definite surface, the flux sheet.

### 3.2 The domain-wall solution and its tension

Minimize $S[\sigma]$ subject to the $2\pi$ jump across $\Sigma$. Far from $\Sigma$, $\sigma \to 0$ (or $2\pi$) on either side; across it, $\sigma$ interpolates $0 \to 2\pi$. This is a **sine-Gordon kink** in the coordinate $\xi$ normal to $\Sigma$, with the profile solving $2A\,\sigma'' = 2\zeta\sin\sigma$, i.e. thickness $\sim m_\gamma^{-1}$.

The wall's **energy per unit area** — the string tension — follows from the Bogomolny/virial identity $A\sigma'^2 = U(\sigma)$ with $U = 2\zeta(1-\cos\sigma)$:
$$
\sigma_{\text{str}} = \int d\xi\,\big[A\sigma'^2 + U\big] = \int_0^{2\pi}\!\! 2\sqrt{A\,U(\sigma)}\ d\sigma = 2\sqrt{2A\zeta}\int_0^{2\pi}\!\!\sqrt{1-\cos\sigma}\ d\sigma = 16\sqrt{A\zeta}.
$$
Using $\int_0^{2\pi}\sqrt{1-\cos\sigma}\,d\sigma = 4\sqrt2$ and $A = e^2/8\pi^2$,
$$
\boxed{\ \sigma_{\text{str}} = 16\sqrt{A\zeta} = \frac{8}{\pi\sqrt2}\,e\sqrt\zeta \ \propto\ e\, e^{-S_{\text{mono}}/2}.\ }
$$

### 3.3 The area law and permanent confinement

The minimal wall spans $\Sigma$, so its total action is $\sigma_{\text{str}} \times \mathrm{Area}(\Sigma_{\min}) = \sigma_{\text{str}}\,\mathrm{Area}(C)$, giving
$$
\boxed{\ \langle W(C)\rangle \sim e^{-\sigma_{\text{str}}\,\mathrm{Area}(C)}.\ }
$$
A rectangular $R\times T$ loop then yields a static potential $V(R) = \sigma_{\text{str}} R$ — **linear confinement**. Because $\sigma_{\text{str}} \propto e^{-S_{\text{mono}}/2} > 0$ at *every* coupling, compact QED₃ **confines permanently**: there is no deconfined phase, in sharp contrast to 4d.

### 3.4 The two scales

Both observables carry the same exponential $e^{-S_{\text{mono}}/2}$:
$$
m_\gamma \propto \frac{\sqrt\zeta}{e},\qquad \sigma_{\text{str}} \propto e\sqrt\zeta,\qquad \frac{\sigma_{\text{str}}}{m_\gamma} \propto e^2\ (\text{a mass, as it must be in 3d}).
$$
The photon gap sets the flux-tube thickness ($\sim m_\gamma^{-1}$); the string tension sets its energy per length. A confining string of transverse size $m_\gamma^{-1}$ and tension $\sigma_{\text{str}}$ — the whole picture, from one plasma.

## 4. Why this is a landmark

Polyakov's calculation is the first place where confinement is **derived**, not modeled:
- It is fully controlled (weak coupling, dilute plasma, every approximation justified).
- It exhibits the mechanism concretely: monopole condensation → photon mass → flux tube → area law.
- It is *the* proof of concept for the dual-superconductor idea, realized exactly here.

Its limitations are equally instructive: it is abelian, three-dimensional, and relies on the monopole gas being dilute and classical. The 4d non-abelian problem (real QCD) has no such controlled instanton computation — which is why the lattice (Block B) and the modern symmetry viewpoint (Semester II) matter. But the *picture* — confinement as the dual Meissner effect of condensed magnetic objects — is Polyakov's, and it generalizes.

> **Physical picture (the whole semester in one paragraph).** Compactness forces monopoles (Week 1's lesson, one dimension up). Duality turns the photon into a scalar whose shift symmetry is the magnetic symmetry (Weeks 3, 8, 9). Monopoles break that symmetry explicitly, gapping the photon (this week, §2). A Wilson loop is then a domain wall of the dual scalar, with an area law (§3). Every step used a tool built earlier in the semester; the result is permanent confinement. This is why Block A's abstractions were worth it.

## 5. What to take away

1. **The plasma gaps the photon:** $m_\gamma^2 = 8\pi^2\zeta/e^2$, $m_\gamma \propto e^{-S_{\text{mono}}/2}$ — a pseudo-Goldstone mass from explicit breaking of the magnetic symmetry.
2. **A Wilson loop is a sine-Gordon domain wall.** Its tension $\sigma_{\text{str}} = 16\sqrt{A\zeta} \propto e\,e^{-S_{\text{mono}}/2}$ gives $\langle W\rangle \sim e^{-\sigma_{\text{str}}\mathrm{Area}}$.
3. **Compact QED₃ confines permanently** — no deconfined phase, at any coupling — the dimensional opposite of 4d.
4. **This is confinement derived.** The dual-superconductor mechanism, realized exactly, and the template Block C's 4d discussion and Semester II generalize.

## 6. Looking ahead: Week 11

Week 10 was 3d, where monopoles are points and always proliferate. Week 11 moves to **four dimensions**, where monopoles are worldlines with a genuine energy–entropy competition: a real transition between a Coulomb phase (dilute loops, massless photon) and a confining phase (condensed loops). There we meet the **dual superconductor** in its original 4d form and the first appearance of the [[julia-toulouse-mechanism|Julia–Toulouse mechanism]] — the rank-changing condensation that this course's research frontier is built on.

## 7. Problem set

**Core problems** (everyone).

**1. The mass gap, in full.**
(a) Derive $m_\gamma^2 = 8\pi^2\zeta/e^2$ from the quadratic expansion of the sine-Gordon action.
(b) Interpret $m_\gamma$ as a Debye mass of the monopole plasma directly (screening of a test magnetic charge) and confirm the two computations agree.

**2. The domain-wall string tension.**
(a) Solve the sine-Gordon kink profile for the $0\to2\pi$ jump and confirm its thickness $\sim m_\gamma^{-1}$.
(b) Compute $\sigma_{\text{str}} = 16\sqrt{A\zeta}$ via the Bogomolny identity, evaluating $\int_0^{2\pi}\sqrt{1-\cos\sigma}\,d\sigma = 4\sqrt2$.
(c) Obtain $\langle W(C)\rangle \sim e^{-\sigma_{\text{str}}\mathrm{Area}}$ and the linear potential $V(R) = \sigma_{\text{str}} R$.

**3. Independence of the surface.**
Show that $\langle W(C)\rangle$ does not depend on the choice of spanning surface $\Sigma$ (the $2\pi$ jump is invisible to $\cos\sigma$), and explain why the minimal surface nonetheless controls the leading exponential.

**Starred problems.**

**4⋆. Finite-temperature deconfinement.**
At finite temperature $T$, compactify Euclidean time and dimensionally reduce to 2d. Show the dual photon becomes a 2d compact scalar, the monopoles become vortices, and a **BKT transition** (Week 4!) separates a low-$T$ confined phase from a high-$T$ deconfined phase. Identify the deconfinement temperature in terms of $e^2$. (Compact QED₃ *does* deconfine at finite $T$, via the 2d Coulomb gas.)

**5⋆. The string tension / mass-gap ratio.**
Compute $\sigma_{\text{str}}/m_\gamma$ and show it is $\propto e^2$ (a mass in 3d). Interpret the flux tube as an object of transverse size $m_\gamma^{-1}$ and energy density $\sim \sigma_{\text{str}} m_\gamma$.

**6⋆⋆ (optional).**
Redo the Wilson-loop calculation for a charge-$q$ probe and show the string tension scales with $q$ in a way that saturates (screening by the plasma) — i.e. compute the $q$-dependence of the domain-wall tension for a $2\pi q$ jump, and discuss $N$-ality / string breaking in the abelian plasma.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block C. Last revised 2026-07-01.*
