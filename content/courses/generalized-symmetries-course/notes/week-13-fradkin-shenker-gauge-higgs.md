---
title: "Week 13 — Fradkin–Shenker I: Gauge–Higgs Systems"
type: lecture-notes
course: syllabus
semester: 1
week: 13
block: D
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 5–12; Elitzur's theorem; the Ising model; strong-coupling expansions
modified: 2026-07-01
---

# Week 13 — Fradkin–Shenker I: Gauge–Higgs Systems

> *So far the gauge field has been alone. Add a charged matter field and the phase diagram changes character: the Higgs mechanism and confinement, which sound like opposites, turn out — for matter in the fundamental representation — to be two ends of a single analytically connected phase, with no boundary between them and no local order parameter to tell them apart. Fradkin and Shenker proved it in 1979, and the puzzle they left ("then what distinguishes the phases?") is the door into Semester II.*

## 0. Reading

**Primary:** Fradkin & Shenker, *Phys. Rev. D* 19 (1979) 3682 — the phase diagram and the complementarity theorem; §§I–IV. Osterwalder & Seiler, *Ann. Phys.* 110 (1978) 440 — the analyticity underpinning.

**Secondary:**
- Kogut, *Rev. Mod. Phys.* 51 (1979) 659, §XI (Higgs on the lattice).
- Fradkin, *Field Theories of Condensed Matter Physics*, 2nd ed., ch. 9.

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]].

## 1. Adding matter

Couple a Higgs field $\phi$ to the lattice gauge field. Keep it simplest — ℤ₂ gauge field $\sigma_\ell = \pm1$ and ℤ₂ matter $\phi_x = \pm1$ — so every statement is a clean generalization of [[week-05-wegner-z2-gauge-theory|Wegner's model]]:
$$
\boxed{\ S = -\beta\sum_P \prod_{\ell\in\partial P}\sigma_\ell \;-\; \kappa\sum_\ell \phi_x\,\sigma_\ell\,\phi_y,\qquad \ell = (x,y).\ }
$$
Two couplings: the **gauge coupling** $\beta$ (as before) and the **matter coupling** $\kappa$ (the hopping/Higgs term). The matter term $\phi_x\sigma_\ell\phi_y$ is gauge-invariant under $\phi_x\to\epsilon_x\phi_x$, $\sigma_\ell\to\epsilon_x\sigma_\ell\epsilon_y$. The matter here is in the **fundamental** (charge-1) representation of ℤ₂ — it carries the center charge, a fact that turns out to decide everything ([[week-14-fradkin-shenker-order-parameters|Week 14]]).

### 1.1 Unitary gauge

Fix the gauge $\phi_x \equiv +1$ everywhere (possible because $\phi$ is charged). The matter term becomes a **link mass** $-\kappa\sum_\ell \sigma_\ell$, and the model is a ℤ₂ gauge theory with an explicit symmetry-breaking field $\kappa$ on the links. The **Higgs phase** is where this "condenses" the links, $\langle\sigma_\ell\rangle_{\text{unitary}}\to1$ — a frozen, ordered gauge field. But note immediately: this is a *gauge-fixed* statement. Gauge-invariantly, Elitzur forbids $\langle\sigma_\ell\rangle$ from ordering (§2).

## 2. Elitzur still holds — no local order parameter

The matter coupling does not rescue local order parameters. Elitzur's theorem ([[week-05-wegner-z2-gauge-theory|Week 5]]) applies verbatim: for any gauge-non-invariant local operator (including $\phi_x$ and $\sigma_\ell$ separately),
$$
\langle\phi_x\rangle = 0,\qquad \langle\sigma_\ell\rangle = 0,\qquad \text{at all } (\beta,\kappa).
$$
"The Higgs field gets a VEV" is a gauge-fixed artifact; gauge-invariantly, **nothing local orders**, in either the Higgs or the confining regime. So the question "Higgs or confinement?" cannot be answered by a local order parameter — the same lesson as Wegner, now sharpened by the presence of matter that seemed to offer one.

> **Physical picture.** This is the crux of the whole Higgs story done honestly. In textbook treatments "the Higgs field condenses, $\langle\phi\rangle\neq0$" — but that statement lives in a fixed gauge and is not an invariant. Elitzur says the invariant content of "Higgs" is *not* an order parameter. The Higgs phase and the confining phase are both phases in which every local gauge-variant field averages to zero. Whether they are even *different* phases is now a genuine question — and the answer, for fundamental matter, is startling.

## 3. The Fradkin–Shenker phase diagram

Map the $(\beta,\kappa)$ plane through its limits [Computed — Problem 1]:

- **$\kappa = 0$ (no matter):** pure ℤ₂ gauge theory. In $d=3$ a confinement–deconfinement transition at $\beta_c$ (Wegner, Week 5).
- **$\beta = \infty$ (frozen gauge field):** $\sigma$ is pure gauge, the matter reduces to a **global Ising model** in $\kappa$, ordering at $\kappa_c$.
- **$\kappa = \infty$ (unitary gauge, frozen matter):** the link mass dominates — the **Higgs** limit.
- **$\beta = 0$ (strong gauge coupling):** confinement, with matter perturbing it.

Piecing these together, the plane has:
- a **free-charge / deconfined** region (large $\beta$, small $\kappa$),
- a **confining** region (small $\beta$, small $\kappa$),
- a **Higgs** region (large $\kappa$),

separated by transition lines that **do not enclose the Higgs region separately from the confining region**. There is a single transition line emanating from the pure-gauge point that **ends in a critical endpoint in the interior**, so one can pass continuously from deep Higgs to deep confinement *around* that endpoint without crossing any boundary.

## 4. The complementarity theorem [Sketched.]

**Theorem (Fradkin–Shenker, 1979). [Stated — refs; convergent-expansion proof.]** *For matter in the fundamental representation, the Higgs region and the confining region are contained in a single analytically connected phase: gauge-invariant local correlation functions are analytic along a path from deep Higgs to deep confinement.*

The proof (Osterwalder–Seiler / Fradkin–Shenker) shows that in the regime of large $\beta$ **or** large $\kappa$ the convergent cluster expansion for gauge-invariant observables has no singularity, so the free energy and all local correlators are analytic across the would-be boundary. **Higgs = confinement** is thus not a slogan but a theorem: for fundamental matter the two are *complementary descriptions of one phase*, not distinct phases.

## 5. String breaking: the Wilson criterion fails [Computed.]

The dynamical matter also kills the Wilson-loop diagnostic. With dynamical fundamental charges present, a long flux string between static probe charges is unstable: once its energy $\sigma_{\text{str}} R$ exceeds the pair-creation threshold ($\sim 2\times$ the matter mass), the string **breaks** by nucleating a matter–antimatter pair that screens the probes. The potential **saturates**, and the Wilson loop shows a **perimeter law everywhere**:
$$
\langle W(C)\rangle \sim e^{-\mu\,\mathrm{Perim}(C)}\qquad\text{for all }(\beta,\kappa)\text{ with fundamental matter.}
$$
The area law — the confinement order parameter of Blocks B–C — is simply **absent** when charges can be screened. The Wilson criterion works only in the pure gauge theory; add fundamental matter and it can no longer distinguish the phases. This is why a *new* idea (symmetry realization) is needed, and it is exactly what Semester II supplies.

> **Physical picture.** In real QCD the analogue is that light quarks screen the static potential: the linear rise of $V(R)$ bends over and flattens once it is energetically favorable to pop a quark–antiquark pair (string breaking, seen on the lattice). "Confinement" in the presence of dynamical quarks is therefore *not* the area law — it is the absence of colored asymptotic states, a subtler statement. Fradkin–Shenker is the clean toy model of this subtlety: with fundamental matter, Higgs and confinement are one phase, and the Wilson loop cannot tell you which regime you are in.

## 6. What to take away

1. **Matter adds a second coupling $\kappa$** to the gauge coupling $\beta$; the Higgs limit is a gauge-fixed statement, not an invariant one.
2. **Elitzur still forbids local order parameters** — $\langle\phi\rangle = \langle\sigma\rangle = 0$ everywhere, in Higgs and confining regimes alike.
3. **Complementarity (fundamental matter):** Higgs and confinement are one analytically connected phase — a theorem, not a slogan.
4. **The Wilson criterion fails with dynamical charges:** string breaking gives perimeter law everywhere. A new diagnostic is needed — the door into Semester II.

## 7. Looking ahead: Week 14

If Higgs and confinement are the same phase for fundamental matter, when *are* there distinct phases? Week 14 answers: it depends on the **center charge** of the matter. Center-neutral (higher-representation) matter leaves the center symmetry intact, and then genuinely distinct phases survive with no local order parameter — distinguished only by how a **1-form symmetry** is realized. We will find the arithmetic $\gcd(N,q)$ controlling the residual symmetry — the same arithmetic as the group's Julia–Toulouse construction — and see the deconfined corner revealed as topological order.

## 8. Problem set

**Core problems** (everyone).

**1. The phase diagram limits.**
Work out the four limits of §3 ($\kappa=0$, $\beta=\infty$, $\kappa=\infty$, $\beta=0$) for the ℤ₂ gauge–Higgs model, and sketch the $(\beta,\kappa)$ diagram with the transition lines and the critical endpoint.

**2. Elitzur with matter.**
Show $\langle\phi_x\rangle = 0$ and $\langle\sigma_\ell\rangle = 0$ at all $(\beta,\kappa)$, and identify the smallest gauge-invariant operators that *can* have nonzero expectation (e.g. $\phi_x\sigma_\ell\phi_y$, Wilson loops, $\phi_x(\prod\sigma)\phi_y$ along a path).

**3. String breaking.**
Estimate the string-breaking length $R_*$ at which $\sigma_{\text{str}} R_* \simeq 2 m_\phi$ and argue the Wilson loop crosses over from area to perimeter law at $R_*$. Why does this forbid a global area law with fundamental matter?

**Starred problems.**

**4⋆. The complementarity path.**
Construct an explicit path in the $(\beta,\kappa)$ plane from deep Higgs to deep confinement that avoids the transition line, and argue (via the convergent expansion in large $\beta$ or large $\kappa$) that gauge-invariant correlators are analytic along it.

**5⋆. Gauge-invariant Higgs operator.**
Show that the gauge-invariant composite that plays the role of the "Higgs condensate" is nonlocal (a matter field connected by a Wilson line to a probe), and discuss why its behavior does not constitute a local order parameter.

**6⋆⋆ (optional).**
Repeat the analysis for $U(1)$ gauge theory with a charge-1 scalar (the abelian Higgs model) in 4d, and locate the Coulomb, Higgs, and confining regions. Show the Higgs and confining regions are again connected for charge-1 matter, and contrast with charge-2 matter (next week).

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block D. Last revised 2026-07-01.*
