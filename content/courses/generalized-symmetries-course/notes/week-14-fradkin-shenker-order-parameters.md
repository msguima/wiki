---
title: "Week 14 — Fradkin–Shenker II: Order Parameters Beyond Landau"
type: lecture-notes
course: syllabus
semester: 1
week: 14
block: D
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 5–13; center symmetry; the Polyakov loop; gcd/modular arithmetic
modified: 2026-07-01
---

# Week 14 — Fradkin–Shenker II: Order Parameters Beyond Landau

> *Last week's puzzle: with fundamental matter, Higgs and confinement are one phase with no local order parameter. This week's resolution begins: whether there are distinct phases at all depends on the matter's charge under the center. Center-neutral matter leaves a symmetry intact — a 1-form symmetry acting on Wilson lines — and its realization distinguishes phases that no local field can. The arithmetic that controls it, $\gcd(N,q)$, is exactly the arithmetic of the group's Julia–Toulouse construction. Semester I ends one step from naming the whole subject.*

## 0. Reading

**Primary:** Fradkin & Shenker, *Phys. Rev. D* 19 (1979) 3682 (§V, higher representations); 't Hooft, *Nucl. Phys. B* 138 (1978) 1 (electric/magnetic flux). Svetitsky & Yaffe, *Nucl. Phys. B* 210 (1982) 423 (center symmetry and deconfinement).

**Secondary:**
- Greensite, *An Introduction to the Confinement Problem*, chs. on center symmetry and the Fradkin–Shenker diagram.
- The concept pages [[higher-form-symmetries]], [[toric-code]], [[topological-order]] (Semester II language, previewed here).

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]].

## 1. Center symmetry and the charge of the matter

Generalize from ℤ₂ to $\mathbb{Z}_N$ (or the center $\mathbb{Z}_N\subset SU(N)$). The **center symmetry** is a global symmetry acting on Wilson lines: a symmetry operation multiplies a charge-$k$ Wilson line by $\omega^k$, $\omega = e^{2\pi i/N}$. In [[week-05-wegner-z2-gauge-theory|pure gauge theory]] it is exact, and — as we will make precise in Semester II — it is a **1-form symmetry**, its charged objects being the Wilson lines themselves.

The decisive question is how dynamical matter of charge $q$ affects it:
- **Fundamental matter ($q=1$):** screens every Wilson line; the center symmetry is **completely broken**. (This is why Higgs = confinement last week.)
- **Center-neutral matter ($q\equiv0 \bmod N$, e.g. adjoint):** carries no center charge; the center symmetry is **untouched**. Distinct phases, separated by how the center is realized, then survive.
- **General charge $q$:** the residual symmetry is a subgroup, computed next.

## 2. The residual 1-form symmetry: $\gcd(N,q)$ [Computed.]

Charge-$q$ matter can end a charge-$q$ Wilson line (screening), so the line $W_q$ is no longer a genuine, unbreakable operator. The center symmetry must therefore act **trivially** on $W_q$: a surviving symmetry element $s\in\mathbb{Z}_N$ needs $\omega^{qs} = 1$, i.e.
$$
qs \equiv 0 \pmod N.
$$
The solutions form the subgroup $\tfrac{N}{\gcd(N,q)}\mathbb{Z}_N \cong \mathbb{Z}_{\gcd(N,q)}$. Hence
$$
\boxed{\ \text{residual 1-form symmetry} \;=\; \mathbb{Z}_{\gcd(N,q)}.\ }
$$
Checks: $q=1 \Rightarrow \gcd=1 \Rightarrow$ trivial (fully screened, Higgs=confinement); $q=N \Rightarrow \gcd=N \Rightarrow$ full $\mathbb{Z}_N$ (center-neutral matter, symmetry intact); general $q$ leaves $\mathbb{Z}_d$ with $d=\gcd(N,q)$.

> **Physical picture (and the research tie-in).** This $\gcd(N,q)$ is *exactly* the arithmetic of the group's Julia–Toulouse construction: there one gauges a subgroup $H = \langle k\rangle \subset \mathbb{Z}_N$ with $d = \gcd(N,k)$ and residual annihilator $\mathrm{Ann}(H) \cong \mathbb{Z}_d$. Screening by charge-$q$ matter and gauging a charge-$k$ subgroup are two faces of the same modular bookkeeping. A student who understands why charge-$q$ matter leaves a $\mathbb{Z}_{\gcd(N,q)}$ 1-form symmetry already understands the residual-symmetry half of the manuscript's central claim. Semester II Block 5 and the master-project make this precise; the seed is here, in a 1979 phase diagram.

## 3. The Polyakov loop and finite-temperature deconfinement [Computed.]

When the center is a good symmetry, it *does* have an order parameter — a **nonlocal** one. At finite temperature (Euclidean time compactified to a circle of length $1/T$), the **Polyakov loop**
$$
P(\vec x) = \operatorname{tr}\prod_{t}U_{(\vec x,\,t)}
$$
wraps the thermal circle and is charged under the center. Its expectation is the deconfinement order parameter:
$$
\langle P\rangle = 0 \ \Leftrightarrow\ \text{confined (center unbroken)},\qquad \langle P\rangle \neq 0 \ \Leftrightarrow\ \text{deconfined (center spontaneously broken)}.
$$
This is a genuine spontaneous breaking of a global symmetry — and it does not contradict Elitzur, because the center is a *global* (1-form) symmetry, not a local one. **Svetitsky–Yaffe:** the deconfinement transition of a $(d{+}1)$-dimensional gauge theory is in the universality class of a $\mathbb{Z}_N$ spin model in $d$ dimensions — the center symmetry made manifest.

## 4. 't Hooft flux sectors [Sketched.]

On a spatial torus $T^{d-1}$, the gauge theory's states organize into **'t Hooft flux sectors** labelled by electric and magnetic fluxes valued in $\mathbb{Z}_N \times \mathbb{Z}_N$ (per pair of cycles). These are the finite-volume fingerprint of the center 1-form symmetry: the electric flux is the eigenvalue of the symmetry operator wrapping a cycle, the magnetic flux is the 't Hooft-loop label. In Semester II (Block 1) this is exactly the clock–shift algebra on $H_1(T^{d-1},\mathbb{Z}_N)$ (seeded in [[week-02-lattice-cell-complex-cochains|Week 2]]), and the ground-state degeneracy it forces is the topological order of the deconfined phase.

## 5. The honest open question the classics leave

Assemble the Fradkin–Shenker picture with center charge in view:
- **Fundamental matter:** center fully broken; Higgs = confinement; **no** invariant distinction (Week 13).
- **Center-neutral matter:** center intact; genuinely distinct phases with **no local order parameter**, distinguished only by the realization of the center 1-form symmetry.

The classics could go this far and no further: they had the extended operators (Wilson, 't Hooft, Polyakov), they knew the center mattered, but they lacked the language to say "a phase is characterized by which higher-form symmetries are spontaneously broken." That language is Semester II. And the punchline it delivers: the **deconfined corner** of the diagram — center 1-form symmetry spontaneously broken — is a **topologically ordered** phase, the [[toric-code|toric code]] for $\mathbb{Z}_N = \mathbb{Z}_2$. The Landau paradigm did not fail; it was incomplete, and the completion is generalized symmetry.

> **Physical picture.** Everything in Semester I has been pushing toward one reframing. Confinement is not "the area law" (dynamical matter breaks it); it is "the electric 1-form symmetry is unbroken." Deconfinement is "the electric 1-form symmetry is spontaneously broken," and the resulting degenerate vacuum is topological order. The Higgs phase is "a 1-form symmetry Higgsed to a subgroup." The whole zoo — Wegner, Polyakov, Fradkin–Shenker — is the realization theory of higher-form symmetries, and we are one week from saying so.

## 6. What to take away

1. **The matter's center charge decides the phases.** Fundamental matter breaks the center completely (Higgs=confinement); center-neutral matter leaves it intact (distinct phases survive).
2. **Residual 1-form symmetry $= \mathbb{Z}_{\gcd(N,q)}$** for charge-$q$ matter — the same $\gcd$ arithmetic as the group's Julia–Toulouse construction and the master-project.
3. **The Polyakov loop** is the (nonlocal) order parameter for center symmetry and finite-$T$ deconfinement; its breaking does not violate Elitzur because the center is global.
4. **The deconfined phase is topological order.** The classics had the phenomena; Semester II supplies the language (higher-form symmetry, its spontaneous breaking, the toric code).

## 7. Looking ahead: Week 15

Week 15 consolidates Semester I: every duality and criterion restated as a statement about operators supported on closed submanifolds, a catalogue of the transitions with no local order parameter, and the take-home final. Then Semester II opens by giving the common thread its name — a symmetry is a topological operator — and the entire semester reorganizes into the theory of generalized symmetries.

## 8. Problem set

**Core problems** (everyone).

**1. Residual symmetry from screening.**
Derive the residual 1-form symmetry $\mathbb{Z}_{\gcd(N,q)}$ for $\mathbb{Z}_N$ gauge theory with charge-$q$ matter, by requiring the center to act trivially on the screened line $W_q$. Tabulate the answer for $N=4$ and $q=1,2,3,4$, and identify which Wilson lines remain genuine in each case.

**2. Polyakov loop.**
(a) Show $P(\vec x)$ is charged under the center and that $\langle P\rangle$ is a center order parameter.
(b) Compute the Polyakov-loop correlator at strong coupling and extract the (finite-$T$) string tension. Why is $\langle P\rangle$ nonlocal, and why does that evade Elitzur?

**3. The deconfined corner.**
For $\mathbb{Z}_2$ gauge + center-neutral matter, argue that the deconfined phase has a 2-fold (on $T^2$: 4-fold) ground-state degeneracy and identify it with the toric code. (Full treatment: Semester II Week 8.)

**Starred problems.**

**4⋆. 't Hooft flux on $T^3$.**
Construct the electric and magnetic flux sectors $\mathbb{Z}_N\times\mathbb{Z}_N$ on the spatial torus and show they realize the clock–shift algebra of Week 2. Relate the count to the ground-state degeneracy of the deconfined phase.

**5⋆. Charge-2 abelian Higgs.**
For $U(1)$ gauge theory with a charge-2 scalar, show the residual 1-form symmetry is $\mathbb{Z}_2$ and that the Higgs phase is a $\mathbb{Z}_2$ topological order (Hansson–Oganesyan–Sondhi: "a superconductor is topologically ordered"). Contrast with the charge-1 case of Week 13.

**6⋆⋆ (optional).**
Connect explicitly to the master-project: for $\mathbb{Z}_N$ with $H=\langle k\rangle$, show that gauging $H$ and screening by charge-$k$ matter leave the *same* residual data ($\mathbb{Z}_{\gcd(N,k)}$ and its annihilator), and articulate in what sense "screening" and "gauging a subgroup" are dual operations. (This is the bridge from Semester I to the group's research frontier.)

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block D. Last revised 2026-07-01.*
