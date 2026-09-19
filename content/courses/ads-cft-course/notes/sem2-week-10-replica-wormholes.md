---
title: "Sem II Week 10 — Replica wormholes"
type: lecture-notes
course: syllabus
semester: 2
week: 10
block: 2
duration: "3 hours (lecture + seminar)"
status: drafting
modified: 2026-05-28
---

# Sem II Week 10 — Replica Wormholes

> *Week 9 gave the Page-curve target; this week supplies the gravitational mechanism that hits it. Computing $\mathrm{Tr}\,\rho_{\rm rad}^n$ with the gravitational path integral, one finds **two competing saddles**: the disconnected geometry (which reproduces Hawking's rising entropy) and a **replica wormhole** that connects the $n$ replicas through the bulk (which gives the falling branch). Their exchange of dominance at the Page time *is* the turnover, and the $n\to1$ limit of the wormhole saddle is precisely the island formula. This is the path-integral derivation that legitimises the island rule of [[sem2-week-11-island-formula|Week 11]].*

## Learning goals

By the end of this week, a student can:

1. Set up the gravitational replica path integral $\mathrm{Tr}\,\rho_{\rm rad}^n=Z_n/Z_1^n$ as a sum over bulk saddles.
2. Describe the disconnected (Hawking) and connected (replica-wormhole) saddles and their topologies.
3. Explain the saddle exchange at the Page time and how it produces the turnover.
4. Derive the island formula as the $n\to1$ limit of the wormhole saddle.
5. State what is rigorous vs. saddle-point in this argument.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Black Hole Information* §4** — the *Replica Wormholes* page.
- Almheiri, Hartman, Maldacena, Shaghoulian, Tajdini (**AHMST**), *Replica wormholes and the entropy of Hawking radiation*, [arXiv:1911.12333](https://arxiv.org/abs/1911.12333).
- Penington, Shenker, Stanford, Yang (**PSSY**), *Replica wormholes and the black hole interior*, [arXiv:1911.11977](https://arxiv.org/abs/1911.11977).

**Prerequisites.** [[sem2-week-04-replica-trick-in-gravity]] (the gravitational replica trick / Lewkowycz–Maldacena), [[sem2-week-09-page-curve]] (the target), [[sem2-week-06-jt-gravity-page-curve]] (the JT + bath model), [[sem2-week-05-quantum-extremal-surfaces]] (QES). Replica/Rényi entropies.

**AQFT cross-reference.** None directly; the von Neumann limit relates to the relative-entropy framework of AQFT Block B.

## 1. The gravitational replica trick, recalled

To get $S_{\rm rad}=-\partial_n\mathrm{Tr}\,\rho_{\rm rad}^n|_{n=1}$, compute $\mathrm{Tr}\,\rho_{\rm rad}^n$. As in [[week-13-ryu-takayanagi|Week 13]] / [[sem2-week-04-replica-trick-in-gravity|Sem II Wk 4]], $\mathrm{Tr}\,\rho_{\rm rad}^n$ is a path integral on $n$ copies of the system, **cyclically glued along the radiation region** $R$. Schematically

$$
\mathrm{Tr}\,\rho_{\rm rad}^n = \frac{Z_n}{Z_1^{\,n}},
$$

where $Z_n$ is the partition function with these $n$-fold replica boundary conditions. The new feature relative to ordinary QFT: in **gravity**, the bulk filling these boundary conditions is *summed over*, and topologically distinct bulk geometries (saddles) compete.

## 2. The two saddles (JT + bath)

Take the JT + bath model ([[sem2-week-06-jt-gravity-page-curve|Wk 6]]). The $n$-replica boundary admits (at least) two bulk saddles:

- **Disconnected (Hawking) saddle.** $n$ independent copies of the single-replica geometry, glued only through the *non-gravitating* bath. Then $Z_n^{\rm disc}=(Z_1)^n$, so $\mathrm{Tr}\,\rho_{\rm rad}^n=1\cdot$(bath factor) and the entropy is just the bath-CFT entanglement entropy — the **rising Hawking branch** $S^{\rm thermal}_{\rm rad}(t)$, which grows without bound.
- **Connected (replica wormhole) saddle.** A single connected bulk geometry whose throat links the $n$ replicas through the *gravitating* region — a wormhole with $\mathbb{Z}_n$ replica symmetry. Its topology differs from $n$ disjoint disks; the gravitational action is lowered by the $e^{S_0}$ (extremal-entropy) weighting of the connected horizon.

Schematically the two on-shell actions scale as

$$
-\log Z_n^{\rm disc} \sim n\,S^{\rm thermal}_{\rm rad}(t),\qquad
-\log Z_n^{\rm conn} \sim S_0 + (\text{bulk-matter on the wormhole}),
$$

so the disconnected action grows with $t$ (more radiation collected) while the connected action is roughly $t$-independent (set by the horizon $S_0$).

## 3. The topological phase transition = the turnover

The path integral is dominated by the saddle of **least action**:

- **Early** ($t<t_{\rm Page}$): $n\,S^{\rm thermal}_{\rm rad}(t)<S_0$, so the **disconnected** saddle wins ⟹ rising Hawking entropy.
- **Late** ($t>t_{\rm Page}$): the growing disconnected action exceeds the wormhole's ⟹ the **connected** saddle wins ⟹ entropy frozen near $S_{\rm BH}$ (falling branch as the horizon shrinks).

The crossover — a genuine **first-order transition between bulk topologies** — is the **Page time**. The radiation entropy computed from $\min$ of the two saddle actions is exactly the Page curve of [[sem2-week-09-page-curve|Week 9]]. Crucially, this required no new local physics: the turnover came from a *different geometry* dominating the sum, invisible to any local effective-field-theory expansion (it is an $O(e^{-S_0})\sim O(e^{-1/G_N})$ effect). The replica wormhole *is* the "non-perturbative correction" Week 9 said was needed.

## 4. The $n\to1$ limit gives the island formula

Now connect to the island rule. Extremise the connected-saddle action over the locations where the wormhole attaches in the bulk — the **replica-symmetric fixed points** $\{x_i\}$. At finite $n$ these are the endpoints of the $\mathbb{Z}_n$-symmetric wormhole; the saddle-point (extremality) condition for their location is *precisely the QES condition* ([[sem2-week-05-quantum-extremal-surfaces|Wk 5]]). Carrying out the analytic continuation $n\to1$ of $S_n=(1-n)^{-1}\log(Z_n/Z_1^n)$ on the connected saddle, the fixed point becomes the **quantum extremal surface** $\partial I$, and the on-shell value reduces to

$$
\boxed{\;S_{\rm rad} = \min\Big[\,\frac{\mathrm{Area}(\partial I)}{4G_N} + S_{\rm bulk}(\mathrm{rad}\cup I)\,\Big]\;}
$$

— the **island formula** ([[sem2-week-11-island-formula|Wk 11]]). The two saddles map onto the two terms of the island rule's $\min$: the disconnected saddle is the no-island ($I=\varnothing$) answer, the connected wormhole is the island answer. So the island formula is not an extra postulate — it is the $n\to1$ shadow of the replica-wormhole saddle competition. (This parallels Lewkowycz–Maldacena's $n\to1$ derivation of RT in [[sem2-week-04-replica-trick-in-gravity|Wk 4]], now with the extra island piece.)

> **[Sketched]** the two saddles and their action scalings (§2). **[Stated-without-proof]** that the connected saddle dominates past $t_{\rm Page}$ (AHMST/PSSY) and that its $n\to1$ limit gives the island formula (§4). These are saddle-point evaluations of the gravitational path integral — controlled, but not theorems; the island rule's status is exactly the status of this computation.

## 5. What is rigorous here

A caution worth stating plainly. "Replica wormholes derive the island formula" means: *within the saddle-point approximation to the (Euclidean) gravitational path integral, including connected topologies, the dominant saddle reproduces the island/QES answer.* It does **not** mean a first-principles proof from a complete theory of quantum gravity — the gravitational path integral itself is only semiclassically defined, and the sum over topologies raises its own puzzles (e.g. the **factorisation problem**: wormholes connecting different boundaries threaten the factorisation of decoupled partition functions, pointing to an ensemble interpretation — cf. the JT matrix model of [[week-15-jt-gravity-intro|Wk 15]]). What is solid is that the *same* saddle competition reproduces both the Page curve and the island rule, consistently, in every soluble model. That convergence is the evidence.

## 6. Key claims and proof status

- **[Sketched]** disconnected and connected ($\mathbb{Z}_n$ wormhole) saddles of $Z_n$ in JT + bath (§2).
- **[Stated-without-proof]** wormhole dominates past $t_{\rm Page}$ ⟹ descending branch (AHMST/PSSY) (§3).
- **[Stated-without-proof]** $n\to1$ of the connected saddle = island formula (§4).
- **[Stated]** the saddle-point/ensemble caveats (§5).

*No coefficients in this note are uncertain at the stated level. (No `CHECK` items for Wk 10.)*

## 7. What to take away

- $\mathrm{Tr}\,\rho_{\rm rad}^n=Z_n/Z_1^n$ in gravity is a **sum over bulk saddles**, with topologically distinct geometries competing.
- **Two saddles:** disconnected (Hawking, rising) vs **replica wormhole** (connected, $\sim S_0$, falling). Their action crossing at $t_{\rm Page}$ is a **topological phase transition** — the turnover.
- The turnover is **non-perturbative** ($O(e^{-S_0})$), invisible locally — the correction Week 9 demanded.
- The **$n\to1$ limit** of the wormhole saddle *is* the island formula; the two saddles are the two terms of its $\min$. This **derives** the island rule (cf. LM's derivation of RT).
- Caveat: it is a saddle-point statement; the topology sum hints at an **ensemble** (factorisation problem; JT matrix model).

## Exercises

**Core.**

1. **Wormhole topology.** For the $n$-replica JT + bath path integral, describe the connected saddle: how the $\mathbb{Z}_n$ symmetry acts, where the wormhole attaches, and how it differs topologically from $n$ disks.
2. **Action crossing.** With $-\log Z_n^{\rm disc}\sim n S^{\rm thermal}_{\rm rad}(t)$ and $-\log Z_n^{\rm conn}\sim S_0+\dots$, locate the Page time as the action crossing and confirm it matches [[sem2-week-09-page-curve|Week 9]].
3. **$n\to1$.** Carry out the analytic continuation of $S_n=(1-n)^{-1}\log(Z_n/Z_1^n)$ on the connected saddle and show the extremality condition for the wormhole endpoints becomes the QES condition, yielding the island formula.

**Starred.**

4. $\star$ **Two terms = two saddles.** Show explicitly that the disconnected saddle gives the $I=\varnothing$ term and the connected saddle gives the island term of the island formula's $\min$.
5. $\star$ **Factorisation problem.** Explain how wormholes connecting distinct boundaries spoil naive factorisation $Z[\partial_1\cup\partial_2]=Z[\partial_1]Z[\partial_2]$, and how an ensemble average (à la the JT matrix model, [[week-15-jt-gravity-intro|Wk 15]]) restores consistency.

**Project.**

6. **PSSY in detail.** Read PSSY §2; reproduce the two-saddle computation in the West-coast/PSSY model and the resulting Page curve; write a 3-page note tying it to the island formula of [[sem2-week-11-island-formula|Wk 11]].

## Connections to other parts of the wiki

- **Within the course.** Builds on [[sem2-week-04-replica-trick-in-gravity]] (LM) and [[sem2-week-06-jt-gravity-page-curve]] (JT + bath); reproduces the [[sem2-week-09-page-curve|Page curve]]; derives the [[sem2-week-11-island-formula|island formula]]. The ensemble caveat connects to [[week-15-jt-gravity-intro|Wk 15]] (JT matrix model).
- **Concepts.** [[replica-trick-gravity]], [[page-curve]], [[quantum-extremal-surfaces]].
- **Open questions.** The factorisation problem / ensemble interpretation; [[crossed-product-and-island-formula]] (algebraic angle).
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 2. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*
