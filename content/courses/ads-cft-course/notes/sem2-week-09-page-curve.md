---
title: "Sem II Week 9 — The Page curve"
type: lecture-notes
course: syllabus
semester: 2
week: 9
block: 2
duration: "3 hours (lecture + seminar)"
status: drafting
modified: 2026-05-28
---

# Sem II Week 9 — The Page Curve

> *Week 8 left us needing a precise target: what *should* the fine-grained entropy of Hawking radiation do if evaporation is unitary? **Page's theorem** answers it from pure quantum information — a small subsystem of a random pure state is nearly maximally mixed, so the radiation entropy must rise, peak when the radiation and black hole have equal entropy (the **Page time**), then fall back to zero. We derive Page's average-entropy formula explicitly, assemble the Page curve, and explain why Hawking's semiclassical calculation cannot reproduce the turnover — setting up the replica-wormhole ([[sem2-week-10-replica-wormholes|Week 10]]) and island ([[sem2-week-11-island-formula|Week 11]]) resolutions.*

## Learning goals

By the end of this week, a student can:

1. **Derive** Page's average-entropy formula $\langle S_A\rangle\approx\log d_A - d_A/(2d_B)$ for $d_A\le d_B$.
2. Assemble the Page curve from the rising (thermal) and falling ($S_{\rm BH}$) branches and locate the Page time.
3. State $t_{\rm Page}\sim t_{\rm evap}/2$ for a fast scrambler.
4. Explain why Hawking's independent-quanta calculation gives a monotonic entropy.
5. State (referring to Week 11) how the radiation's entanglement wedge / island produces the descending branch.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Black Hole Information* §1** — the *Page Curve and Fine-Grained Entropy* page — same chapter as Week 8, not a separate one.
- Page, *Average entropy of a subsystem*, [arXiv:gr-qc/9305007](https://arxiv.org/abs/gr-qc/9305007) and *Information in black hole radiation*, [arXiv:hep-th/9306083](https://arxiv.org/abs/hep-th/9306083).
- Almheiri, Hartman, Maldacena, Shaghoulian, Tajdini, [arXiv:2006.06872](https://arxiv.org/abs/2006.06872), §2.

**Prerequisites.** [[sem2-week-08-hawking-radiation-info-problem]] (the paradox), [[sem2-week-05-quantum-extremal-surfaces]] (QES), [[sem2-week-11-island-formula]] (the island calculation this week motivates). Density matrices, Rényi/von Neumann entropy, Haar averaging.

**AQFT cross-reference.** The monotonicity underlying the curve is the algebraic relative-entropy monotonicity of [[week-07-connes-cocycle-and-relative-entropy|AQFT Wk 7]].

## 1. Page's theorem (worked)

Take a bipartite system $\mathcal{H}_A\otimes\mathcal{H}_B$, $\dim=d_A,d_B$ with $d_A\le d_B$, in a **Haar-random pure state** $|\psi\rangle$. How entangled is $A$ with $B$ on average?

**Compute the average purity** $\langle\mathrm{Tr}\,\rho_A^2\rangle$. Writing $\mathrm{Tr}\,\rho_A^2=\mathrm{Tr}\big[(\rho_A\otimes\rho_A)\,\mathbb{S}_A\big]$ with $\mathbb{S}_A$ the swap on two copies of $A$, and Haar-averaging the two copies of $|\psi\rangle\langle\psi|$ (the standard formula $\overline{|\psi\rangle\langle\psi|^{\otimes2}}=\tfrac{1}{D(D+1)}(\mathbb{1}+\mathbb{S})$ with $D=d_Ad_B$), one finds

$$
\boxed{\;\langle\mathrm{Tr}\,\rho_A^2\rangle = \frac{d_A+d_B}{d_Ad_B+1}.\;}
$$

For $d_A\le d_B$ this is $\approx \dfrac{1}{d_A}+\dfrac{1}{d_B}$. The **second Rényi entropy** is then

$$
S_2(A) = -\log\langle\mathrm{Tr}\,\rho_A^2\rangle \approx -\log\Big(\tfrac{1}{d_A}+\tfrac{1}{d_B}\Big) = \log d_A - \log\Big(1+\tfrac{d_A}{d_B}\Big) \approx \log d_A - \frac{d_A}{d_B}.
$$

The von Neumann entropy, computed by Page's full Haar average over *all* moments (the $n\to1$ continuation), gives the same structure with the famous factor of $\tfrac12$:

$$
\boxed{\;\langle S_A\rangle = \log d_A - \frac{d_A}{2 d_B} + O\!\big((d_Ad_B)^{-1}\big)\qquad(d_A\le d_B).\;}
$$

**Read the physics:** for $d_A\ll d_B$, $\langle S_A\rangle\approx\log d_A$ — the smaller subsystem is **nearly maximally mixed** (entropy $=\log$ of its dimension), with only an exponentially small deficit $d_A/2d_B$ from purity. A random pure state entangles its subsystems as much as kinematically possible. By $A\leftrightarrow B$ symmetry, $\langle S\rangle$ as a function of subsystem size **rises to a maximum at half the total** ($d_A=d_B$) and falls — the kinematic shape behind the Page curve.

> **[Proven]** the purity $\langle\mathrm{Tr}\,\rho_A^2\rangle=(d_A+d_B)/(d_Ad_B+1)$ and the Rényi-2 entropy (worked above); **[Stated-without-proof]** the exact vN coefficient $\tfrac12$ (Page's full average; Exercise 1).

## 2. The Page curve for evaporation

Model the evaporating black hole as a quantum system of initial dimension $e^{S_0}$ ($S_0=$ initial Bekenstein–Hawking entropy) slowly transferring its Hilbert space to the radiation. At time $t$, let the radiation have effective dimension $d_R(t)$ (growing) and the remaining black hole $d_{\rm BH}(t)$ (shrinking), with $d_R\,d_{\rm BH}\approx e^{S_0}$ for a pure global state. Apply Page's theorem to the radiation:

- **Early** ($d_R\ll d_{\rm BH}$): $S_{\rm rad}\approx\log d_R = S_{\rm rad}^{\rm thermal}$ — the radiation is nearly maximally mixed, its entropy growing as quanta accumulate (the **rising/Hawking branch**).
- **Late** ($d_R\gg d_{\rm BH}$): now the *black hole* is the small subsystem, so $S_{\rm rad}=S_{\rm BH}\approx\log d_{\rm BH}=S_{\rm BH}(t)$ — the radiation entropy tracks the *shrinking* black-hole entropy (the **falling branch**).

The fine-grained radiation entropy is the smaller of the two,

$$
\boxed{\;S_{\rm rad}(t) \approx \min\big\{\,S_{\rm rad}^{\rm thermal}(t),\ S_{\rm BH}(t)\,\big\},\;}
$$

rising, peaking at the **Page time** $t_{\rm Page}$ where the two branches cross ($S_{\rm rad}^{\rm thermal}=S_{\rm BH}$, both $\approx S_0/2$), then falling to zero as the black hole disappears. This is the **Page curve**. For a fast-scrambling black hole the crossing is at roughly half the total evaporation,

$$
t_{\rm Page} \sim \frac{S_0\,\beta}{2\pi} \sim \frac{t_{\rm evap}}{2}.
$$

## 3. Why Hawking's calculation misses the turnover

Hawking's semiclassical computation ([[sem2-week-08-hawking-radiation-info-problem|Week 8]]) treats **each emitted quantum independently**: every Hawking pair adds its $\sim\log2$ of entanglement entropy to the radiation, so $S_{\rm rad}^{\rm Hawking}(t)$ grows **monotonically**, crossing $S_0$ and continuing up — it never turns over. It correctly gives the *rising* branch but is blind to the constraint that $S_{\rm rad}$ cannot exceed the shrinking $S_{\rm BH}$.

The failure is **non-local and non-perturbative**. No small, local modification of the near-horizon effective field theory can bend the curve down — the turnover is a *global* statement about the gravitational path integral, requiring saddles (replica wormholes) that connect different replicas/regions. This is why the resolution waited so long: it is invisible to any order of local semiclassical perturbation theory, appearing only at $O(e^{-1/G_N})\sim O(e^{-N^2})$ in the path integral.

## 4. The descending branch from the radiation's entanglement wedge

The modern resolution (Weeks 10–11): apply the **QES/island** prescription to the radiation. Past the Page time, the entanglement wedge of the radiation $R$ acquires a disconnected **island** $I$ just inside the horizon, and

$$
S_{\rm rad} = \min_I\,\mathrm{ext}_I\Big[\frac{\mathrm{Area}(\partial I)}{4G_N} + S_{\rm bulk}(R\cup I)\Big].
$$

The no-island saddle gives the rising branch; the island saddle gives $S_{\rm rad}\approx S_{\rm BH}$ (the falling branch). Their $\min$ is exactly the Page curve of §2 — now derived from gravity. The full computation is [[sem2-week-11-island-formula|Week 11]] (already in hand); the saddle that *makes the island appear* is the replica wormhole of [[sem2-week-10-replica-wormholes|Week 10]]. So Page's information-theoretic curve and the gravitational island computation agree — the central success of the program.

> **[Sketched]** the island/QES origin of the descending branch (full treatment in Weeks 10–11; the island formula is derived in Week 11).

## 5. Key claims and proof status

- **[Proven]** $\langle\mathrm{Tr}\,\rho_A^2\rangle=(d_A+d_B)/(d_Ad_B+1)$ and $S_2\approx\log d_A-d_A/d_B$ (§1).
- **[Stated-without-proof]** Page's exact vN formula $\langle S_A\rangle=\log d_A-d_A/2d_B$ (full Haar average).
- **[Stated-without-proof]** $t_{\rm Page}\sim S_0\beta/2\pi\sim t_{\rm evap}/2$ for a fast scrambler (§2).
- **[Proven]** Hawking's monotonic growth from independent-quanta emission (§3).
- **[Sketched]** the island descending branch (Weeks 10–11) (§4).

*No coefficients in this note are uncertain at the stated level. (No `CHECK` items for Wk 9.)*

## 6. What to take away

- **Page's theorem (worked):** $\langle\mathrm{Tr}\rho_A^2\rangle=(d_A+d_B)/(d_Ad_B+1)$ ⟹ $\langle S_A\rangle\approx\log d_A-d_A/2d_B$; a small subsystem of a random pure state is **nearly maximally mixed**.
- **Page curve:** $S_{\rm rad}\approx\min\{S^{\rm thermal}_{\rm rad},S_{\rm BH}\}$ — rise, peak at $t_{\rm Page}$ (where $S_{\rm rad}=S_{\rm BH}\approx S_0/2$), fall to 0. $t_{\rm Page}\sim t_{\rm evap}/2$.
- **Hawking** treats quanta independently ⟹ monotonic entropy, missing the turnover; the fix is **non-local/non-perturbative** ($O(e^{-N^2})$).
- The **island/QES** prescription (Weeks 10–11) gives the descending branch from gravity, reproducing Page's curve.

## Exercises

**Core.**

1. **Page formula.** Reproduce $\langle\mathrm{Tr}\,\rho_A^2\rangle=(d_A+d_B)/(d_Ad_B+1)$ from the Haar swap formula; expand for $d_A\le d_B$ and obtain $S_2\approx\log d_A-d_A/d_B$. (Then quote Page's vN result with the $\tfrac12$.)
2. **Page time vs lifetime.** For a 4d fast scrambler emitting one quantum per scrambling time $t_*\sim M\log M$, estimate $t_{\rm Page}$ and compare to $t_{\rm evap}\sim M^3$ (Planck units); confirm $t_{\rm Page}\sim t_{\rm evap}/2$ up to logs.
3. **Two-sided saturation.** In eternal AdS-Schwarzschild + bath, use the QES rule ([[sem2-week-05-quantum-extremal-surfaces|Wk 5]]) to identify the no-island and island candidates and show the island wins at late times, saturating $S_{\rm rad}\to2S_{\rm BH}$ (cf. [[sem2-week-11-island-formula|Wk 11]]).

**Starred.**

4. $\star$ **Random-state model.** Simulate (or argue) the Page curve for a Haar-random unitary "evaporation" of $S_0$ qubits and verify the rise/peak/fall and the $S_0/2$ peak.
5. $\star$ **Monotonicity.** Connect the necessity of the turnover to relative-entropy monotonicity ([[week-07-connes-cocycle-and-relative-entropy|AQFT Wk 7]]).

**Project.**

6. **Page's papers.** Read Page 1993; reproduce the full average-entropy derivation (all moments, $n\to1$) and the $-d_A/2d_B$ coefficient; write a 2-page note connecting it to the gravitational island calculation of [[sem2-week-11-island-formula|Wk 11]].

## Connections to other parts of the wiki

- **Within the course.** The quantitative target for [[sem2-week-10-replica-wormholes]] and [[sem2-week-11-island-formula]]; back-link [[sem2-week-08-hawking-radiation-info-problem]]; QES tool from [[sem2-week-05-quantum-extremal-surfaces]].
- **Concepts.** [[page-curve]], [[quantum-extremal-surfaces]].
- **AQFT course cross-reference.** [[week-07-connes-cocycle-and-relative-entropy|AQFT Wk 7]] (relative-entropy monotonicity behind the curve).
- **Open questions.** [[bell-chsh-in-holographic-setting]] (quantum-information structure of the radiation).
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 2. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*
