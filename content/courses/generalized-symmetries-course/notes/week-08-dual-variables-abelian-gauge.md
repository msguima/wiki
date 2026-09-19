---
title: "Week 8 — Midterm and Dual Variables for Abelian Gauge Theories"
type: lecture-notes
course: syllabus
semester: 1
week: 8
block: B
duration: 4 hours (2 hr midterm + 2 hr lecture)
prerequisites: Weeks 1–7; the Villain form and Poisson resummation (Week 3); the cochain calculus (Week 2)
modified: 2026-07-01
---

# Week 8 — Midterm and Dual Variables for Abelian Gauge Theories

> *Week 3 dualized the XY model and found a Coulomb gas of vortices. This week we run the identical machine on abelian gauge theory and find a gas of monopoles — points in three dimensions, worldlines in four. That one dimensional difference is the entire plot of Block C: the 3d monopole plasma confines by Polyakov's mechanism, the 4d monopole loops condense into a dual superconductor. The tools are exactly Week 2 and Week 3, now in one degree higher.*

## 0. The midterm (first two hours)

The in-class midterm covers Blocks A–B: a Villain/Poisson duality carried out in full; a strong-coupling Wilson-loop computation with a string tension extracted; an Elitzur-style argument; and a transfer-matrix-to-Hamiltonian derivation. Solutions are posted after the session. The remainder of this note is the second lecture.

## 1. Reading

**Primary:** Banks, Myerson, Kogut, *Nucl. Phys. B* 129 (1977) 493 (BMK) — the 4d abelian duality; §§1–2. Savit, *Rev. Mod. Phys.* 52 (1980) 453 — duality systematics, the table this week populates.

**Secondary:**
- Polyakov, *Nucl. Phys. B* 120 (1977) 429 — the 3d duality and confinement we set up here and execute in Weeks 9–10.
- Kogut, *Rev. Mod. Phys.* 51 (1979) 659, §VI.

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]].

## 2. The current (flux) representation [Computed.]

Take compact $U(1)$ in the **Villain form** (Week 3), now for a gauge field $a\in C^1(\Lambda,\mathbb{R})$:
$$
Z = \Big(\prod_\ell \int_{-\infty}^{\infty} da_\ell\Big)\sum_{n\in C^2(\Lambda,\mathbb{Z})}\exp\!\Big(-\frac{\beta}{2}\sum_P\big(da - 2\pi n\big)_P^2\Big),
$$
where the plaquette field strength $da$ is a 2-cochain and the integer $n$ (also a 2-cochain) implements the $2\pi$-periodicity of the compact photon. This is the exact analogue of the Villain XY model, one form-degree up (0-cochain $\theta$ → 1-cochain $a$; vorticity $dn\in C^2$ → monopole $dn\in C^3$).

Run the Week-3 recipe:

**Step 1 — Hubbard–Stratonovich** with a real 2-cochain $b$ (the dual field strength):
$$
e^{-\frac{\beta}{2}\|da-2\pi n\|^2} \propto \int\mathcal{D}b\ \exp\!\Big(-\frac{1}{2\beta}\|b\|^2 + i\,b\cdot(da - 2\pi n)\Big).
$$
**Step 2 — Poisson-resum $n$** (each plaquette integer), forcing $b$ to be an **integer** 2-cochain $b = m$, the dual flux.
**Step 3 — Integrate out $a$**, giving the **conservation constraint** $\delta m = 0$ (the dual flux is divergence-free). This is the current representation: $Z$ becomes a sum over conserved integer 2-cochains $m$, weighted by $e^{-\frac{1}{2\beta}\|m\|^2}$.

The gauge-invariant obstruction, as always, is the coboundary of the integer field: the **monopole density**
$$
m_{\text{mono}} = dn \in C^3(\Lambda,\mathbb{Z}).
$$
Its dual-lattice location is the whole point, and it depends on $d$.

## 3. Where the monopoles live [Computed.]

By Poincaré duality (Week 2 §5), a 3-cochain $dn\in C^3(\Lambda,\mathbb{Z})$ is dual to a $(d-3)$-cycle on $\Lambda^*$:
$$
\boxed{\ d=3:\ \ dn \text{ is a 3-cochain} \leftrightarrow \text{0-cycle} = \textbf{points (instantons)};\qquad d=4:\ \ dn \leftrightarrow \text{1-cycle} = \textbf{worldlines}.\ }
$$
Same equation $m_{\text{mono}} = dn$; the geometry of the defect is set by the spacetime dimension. This is the pivot of Block C.

### 3.1 Three dimensions: the dual photon [Computed.]

In $d=3$ the photon has one polarization; dualizing trades it for a **compact scalar** $\chi$ (the "dual photon") on dual sites. Solving $\delta m = 0$ off the monopoles gives $m = \star\, d\chi$ with $\chi$ compact, and the monopoles appear as points where $\chi$ winds. The result is
$$
Z_{3d} \;\cong\; \int\mathcal{D}\chi\ \exp\!\Big(-\int d^3x\ \Big[\frac{1}{2e_d^2}(\partial\chi)^2 - 2\zeta\cos\chi\Big]\Big),
$$
a 3d **sine-Gordon** theory: free dual photon plus a **monopole fugacity** $\zeta \sim e^{-S_{\text{mono}}}$ multiplying $\cos\chi$ (each monopole/antimonopole is an $e^{\pm i\chi}$ insertion). The shift symmetry $\chi\to\chi+\text{const}$ is the **magnetic symmetry**; the monopole term explicitly breaks it. This is *exactly* the starting point of Polyakov's confinement calculation (Week 9): the $\cos\chi$ term gaps the photon and produces an area law. The whole 3d story is the Week-3 XY duality read for a gauge field.

### 3.2 Four dimensions: dual photon and monopole loops [Computed.]

In $d=4$ the 2-cochain field strength is dual to a 2-cochain (self-dual degree, Week 2 Problem 6), so compact $U(1)$ dualizes to **another compact $U(1)$** — the magnetic photon — with the monopoles now **worldlines** (1-cycles on $\Lambda^*$). The Banks–Myerson–Kogut dual form writes $Z$ as a sum over monopole worldloops interacting via the 4d Coulomb ($1/r^2$) propagator, plus the dual photon. Whether the monopole loops are **dilute** (Coulomb phase, massless photon) or **condensed** (confining, dual superconductor) is an energy–entropy balance for loops — the subject of Week 11.

> **Physical picture.** Dimension decides the fate of the abelian photon. In 3d, monopoles are instantons: they always proliferate (a dilute gas of points has more entropy than energy at any coupling), so the photon is *always* gapped and compact QED₃ *always* confines — no Coulomb phase. In 4d, monopoles are worldlines with a genuine energy–entropy competition, so there is a real transition: a Coulomb phase (massless photon, deconfined) at weak coupling and a confining phase (condensed monopoles) at strong coupling. The Wilson-loop area law of Week 6 was the strong-coupling side of *this* transition. The dimensional fact "$dn$ is a point vs a loop" is the whole difference.

## 4. The duality table, gauge rows added

We can now extend the Week-3 dictionary to gauge theories:

| Direct theory | Dual theory | Defect | Fate |
|---|---|---|---|
| 2d XY (Week 3) | Coulomb gas / sine-Gordon | vortex $dn\in C^2$ (point) | BKT transition |
| 3d compact $U(1)$ | dual photon $\chi$ + $\cos\chi$ | monopole $dn\in C^3$ (point) | always confined (Wk 9–10) |
| 4d compact $U(1)$ | dual photon + monopole loops | monopole $dn\in C^3$ (loop) | Coulomb ↔ confining (Wk 11) |

One engine — Poisson resummation of the integer field on the appropriate cochain — generates every row. Semester II Week 12 makes each of these dualities **exact** (not just Villain-approximate) via the modified Villain construction, and re-reads the magnetic symmetry as a **higher-form symmetry**.

## 5. What to take away

1. **Abelian gauge duality is the XY duality, one degree up.** Villain $U(1)$ → Hubbard–Stratonovich → Poisson-resum the integer 2-cochain → conserved dual flux $\delta m = 0$; the monopole is $m_{\text{mono}} = dn$.
2. **Dimension sets the defect geometry.** $dn\in C^3$ is dual to points in $d=3$ (instantons) and to worldlines in $d=4$ — the organizing fact of Block C.
3. **3d dualizes to a sine-Gordon dual photon** with a monopole $\cos\chi$ that breaks the magnetic symmetry — Polyakov's starting point.
4. **4d dualizes to a magnetic photon plus monopole loops**, with a genuine Coulomb-to-confining transition — the dual superconductor.

## 6. Looking ahead: Block C

Block C is the physics heart of Semester I. Week 9 takes the 3d dual photon of §3.1 and computes the monopole plasma; Week 10 reproduces **Polyakov's mass gap and area law** in full — the signature calculation of the semester. Week 11 moves to 4d monopole condensation and the **dual superconductor**, where the [[julia-toulouse-mechanism|Julia–Toulouse mechanism]] makes its first appearance. Week 12 adds θ-terms and the Witten effect, exposing the first crack that only the modified Villain formulation (Semester II) repairs.

## 7. Problem set

**Core problems** (everyone).

**1. The abelian duality, in full.**
Carry out §2 Steps 1–3 for Villain $U(1)$ keeping all factors.
(a) Obtain the conserved dual flux $m$ with $\delta m = 0$ and weight $e^{-\|m\|^2/2\beta}$.
(b) Identify the monopole density $m_{\text{mono}} = dn$ and its dual-lattice support in $d=3$ and $d=4$.

**2. The 3d dual photon.**
Solve $\delta m = 0$ in $d=3$ via the compact scalar $\chi$ and derive the sine-Gordon form of §3.1, identifying the monopole fugacity $\zeta$ and the magnetic shift symmetry. Which operator is charged under the magnetic symmetry?

**3. Monopole action from the lattice Coulomb energy.**
Estimate the single-monopole action $S_{\text{mono}}$ in $d=3$ from the lattice Coulomb self-energy of a unit magnetic charge, and hence the fugacity $\zeta \sim e^{-S_{\text{mono}}}$.

**Starred problems.**

**4⋆. Banks–Myerson–Kogut in 4d.**
Derive the BMK dual form of 4d Villain $U(1)$: a sum over monopole worldloops interacting via the 4d Coulomb propagator, plus a free dual photon. Set up the loop energy–entropy balance and identify the coupling at which large loops proliferate (the confinement transition). (Executed physically in Week 11.)

**5⋆. Lattice Dirac quantization.**
Using the cochain linking pairing (Week 2), show that the electric and magnetic charges satisfy $e g \in 2\pi\mathbb{Z}$ on the lattice, and that the integer $n$ of the Villain form is exactly the Dirac string threading the plaquette.

**6⋆⋆ (optional).**
Show explicitly that compact $U(1)$ in $d=3$ has **no** Coulomb phase: estimate the monopole plasma's Debye mass at arbitrary coupling and argue it is always nonzero, so the photon is always gapped. Contrast with $d=4$, where the analogous estimate permits a massless (Coulomb) phase. This is the quantitative version of the §3 "physical picture."

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block B. Last revised 2026-07-01.*
