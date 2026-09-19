---
title: "Sem II Week 5 — Quantum extremal surfaces"
type: lecture-notes
course: syllabus
semester: 2
week: 5
block: 1
duration: "3 hours (lecture + seminar)"
status: drafting
modified: 2026-05-28
---

# Sem II Week 5 — Quantum Extremal Surfaces

> *Ryu–Takayanagi/HRT and the Lewkowycz–Maldacena derivation ([[sem2-week-04-replica-trick-in-gravity|Wk 4]]) used only the classical **area**. But bulk quantum fields carry entropy too. This week upgrades RT to the **quantum extremal surface (QES)** prescription: extremise the **generalised entropy** $S_{\rm gen}=\mathrm{Area}/4G_N+S_{\rm bulk}$ — area *plus* the entanglement entropy of the bulk fields. FLM gives the first $1/N$ correction; Engelhardt–Wall make it all-orders. Applied to the radiation, the QES produces an **island** and the Page curve — the subject of [[sem2-week-11-island-formula|Wk 11]]/[[sem2-week-06-jt-gravity-page-curve|Wk 6]]. This week is the prescription itself and its derivation.*

## Learning goals

By the end of this week, a student can:

1. Motivate the generalised entropy $S_{\rm gen}=\mathrm{Area}/4G_N+S_{\rm bulk}$ and why RT needs correcting.
2. State the FLM first-order ($1/N$) correction to RT.
3. State the Engelhardt–Wall QES prescription (min-ext of $S_{\rm gen}$) and that it reduces to RT classically.
4. **Derive** QES from the replica trick with bulk matter (LM + $S_{\rm bulk}$).
5. Explain how the QES yields the island formula (forward to Wk 11).

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Black Hole Information* §2** — the *Quantum Extremal Surfaces* page; also *AdS/CFT Foundations* §9. Note this week is served by the BHI track, not the Advanced one.
- Faulkner, Lewkowycz, Maldacena (**FLM**), *Quantum corrections to holographic entanglement entropy*, [arXiv:1307.2892](https://arxiv.org/abs/1307.2892).
- Engelhardt, Wall (**EW**), *Quantum extremal surfaces: holographic entanglement entropy beyond the classical regime*, [arXiv:1408.3203](https://arxiv.org/abs/1408.3203).

**Prerequisites.** [[week-13-ryu-takayanagi]] (RT), [[week-14-hrt-and-subregion-subalgebra]] (HRT, entanglement wedge), [[sem2-week-04-replica-trick-in-gravity]] (LM derivation), [[sem2-week-13-quantum-focusing-anec]] (QFC, which underpins QES).

**AQFT cross-reference.** $S_{\rm bulk}$ is the von Neumann entropy of bulk fields across $\mathcal{X}$ — the type III$_1$ object of AQFT Block B; the generalised entropy is its UV-finite combination with the area.

## 1. Why RT needs correcting

RT gives $S(A)=\mathrm{Area}(\gamma_A)/4G_N$ — but this is the **leading** term in $G_N\sim1/N^2$. The bulk effective field theory has its own entanglement: the quantum fields in the entanglement wedge are entangled across $\gamma_A$ with those outside, contributing a **bulk entanglement entropy** $S_{\rm bulk}$ of order $N^0$ (one order down from the area's $N^2$). The natural UV-finite combination is the **generalised entropy**

$$
\boxed{\;S_{\rm gen}(\mathcal{X}) = \frac{\mathrm{Area}(\mathcal{X})}{4G_N} + S_{\rm bulk}(\Sigma_\mathcal{X}),\;}
$$

where $\Sigma_\mathcal{X}$ is the homology region bounded by $\mathcal{X}$. The area's UV divergence (from short-distance modes near $\mathcal{X}$) and $S_{\rm bulk}$'s UV divergence (the same modes) **cancel** in $S_{\rm gen}$ — exactly the renormalisation of Newton's constant. So $S_{\rm gen}$ is the physical, finite object; $\mathrm{Area}/4G_N$ alone is only its leading piece. Its monotonicity is guaranteed by the quantum focusing conjecture ([[sem2-week-13-quantum-focusing-anec|Wk 13]]).

## 2. The FLM first-order correction

At first order in $G_N$, FLM showed the quantum-corrected entropy is simply

$$
S(A) = \frac{\mathrm{Area}(\gamma_A)}{4G_N} + S_{\rm bulk}(\Sigma_{\gamma_A}) + \dots,
$$

evaluated on the **classical** RT surface $\gamma_A$ — area term plus the bulk entanglement entropy in the (classical) entanglement wedge. The derivation is the LM conical-defect computation of [[sem2-week-04-replica-trick-in-gravity|Wk 4]] *with the bulk matter included*: the replica path integral now has the bulk fields propagating on $\hat{\mathcal{B}}_n$, contributing their own $\mathrm{Tr}\,\rho_{\rm bulk}^n$, whose $n\to1$ limit is $S_{\rm bulk}$. This is the first quantum correction; the QES is what you get when you stop evaluating on the *classical* surface and re-extremise.

## 3. The Engelhardt–Wall QES prescription

EW promote the rule to all orders: the surface is fixed by extremising the *generalised* entropy, not the area:

$$
\boxed{\;S(A) = \min_{\mathcal{X}}\,\mathrm{ext}_{\mathcal{X}}\Big[\frac{\mathrm{Area}(\mathcal{X})}{4G_N} + S_{\rm bulk}(\Sigma_\mathcal{X})\Big],\;}
$$

over surfaces $\mathcal{X}$ anchored at $\partial A$ and homologous to $A$. The extremisation condition $\delta_\mathcal{X}S_{\rm gen}=0$ balances the area's classical pull against the gradient of the bulk entropy:

$$
\frac{1}{4G_N}\,\delta\,\mathrm{Area} + \delta S_{\rm bulk} = 0
\quad\Longleftrightarrow\quad
\frac{K^{(a)}}{4G_N} = -\,\partial^{(a)}S_{\rm bulk},
$$

i.e. the extrinsic-curvature trace $K^{(a)}$ (which vanished for the classical extremal surface) is now sourced by the bulk-entropy gradient. **Reduction to RT:** when $S_{\rm bulk}\ll\mathrm{Area}/4G_N$ (large $N$, weak bulk entanglement), $\delta S_{\rm bulk}$ is negligible and the condition collapses to $K^{(a)}=0$ — the classical extremal (RT/HRT) surface, with $S_{\rm bulk}$ a sub-leading correction. The "$\min$" over multiple extrema is the same competition as in RT, now of generalised entropies.

> **[Stated-without-proof]** the EW QES prescription; **[Sketched]** its reduction to RT and the extremality condition (§3).

## 4. Derivation from the replica trick with bulk matter (worked logic)

Why is it the *generalised* entropy that is extremised? Repeat the [[sem2-week-04-replica-trick-in-gravity|Wk 4]] LM computation, but keep the bulk quantum fields. The $\mathbb{Z}_n$-symmetric saddle's on-shell "action" now has two pieces:

1. the **gravitational** conical-defect action $\to \tfrac{n-1}{4G_N}\mathrm{Area}(\mathcal{C}_n)$ (as in Wk 4);
2. the **bulk-matter** replica partition function $\mathrm{Tr}\,\rho_{\rm bulk}^n$ on the defect geometry $\to (n-1)\,S_{\rm bulk}$ in the $n\to1$ limit.

Adding them, $-\partial_n(\dots)|_{n=1}$ gives $\mathrm{Area}(\mathcal{C}_1)/4G_N + S_{\rm bulk}=S_{\rm gen}$. Crucially, the location of $\mathcal{C}_n$ is now fixed by regularity of the *combined* (gravity + matter backreaction) saddle — and that condition is the extremisation of $S_{\rm gen}$, not of the area alone. So the replica trick *automatically* produces the QES rule once bulk matter is included. The QES is the LM surface of the matter-coupled problem.

> **[Sketched]** QES from replica + bulk matter (the two-piece on-shell action above; FLM/EW).

## 5. Application: islands and the Page curve (forward)

Apply the QES rule to a **radiation** region $R$ in a black-hole + bath system. There are two competing extrema:

- **No-island** ($\mathcal{X}$ near the horizon / empty island): $S_{\rm gen}\approx S^{\rm thermal}_{\rm rad}(t)$ — rising.
- **Island** ($\mathcal{X}=\partial I$ with $I$ a bulk region just inside the horizon): $S_{\rm gen}\approx 2S_{\rm BH}$ (two-sided) — flat.

The $\min$ switches at the **Page time**, giving the Page curve, and the winning island saddle is the **island formula**

$$
S(R)=\min_I\mathrm{ext}_I\Big[\frac{\mathrm{Area}(\partial I)}{4G_N}+S_{\rm bulk}(R\cup I)\Big].
$$

This is exactly [[sem2-week-11-island-formula|Wk 11]] (worked there in full) and the explicit JT calculation of [[sem2-week-06-jt-gravity-page-curve|Wk 6]]; here we only note that the island is the QES prescription applied to the radiation, with the island = the part of the entanglement wedge disconnected from $R$.

> **[Stated-without-proof]** the island formula as the radiation QES (derived/worked in Wks 6, 11).

## 6. Key claims and proof status

- **[Stated-without-proof]** $S_{\rm gen}=\mathrm{Area}/4G_N+S_{\rm bulk}$ is UV-finite (area divergence renormalises $G_N$) (§1).
- **[Sketched]** FLM first-order correction (LM + bulk matter) (§2).
- **[Stated-without-proof]** EW QES prescription; **[Sketched]** reduction to RT, extremality condition, and the replica-with-matter derivation (§§3–4).
- **[Stated-without-proof]** island formula as the radiation QES (§5; Wks 6, 11).

*No coefficients in this note are uncertain. (No `CHECK` items for Wk 5.)*

## 7. What to take away

- The physical object is the **generalised entropy** $S_{\rm gen}=\mathrm{Area}/4G_N+S_{\rm bulk}$ (UV-finite; area divergence renormalises $G_N$).
- **FLM:** at first order, $S=\mathrm{Area}_{\rm RT}/4G_N+S_{\rm bulk}$ on the classical surface.
- **Engelhardt–Wall QES:** $S=\min\,\mathrm{ext}\,S_{\rm gen}$ — extremise area *plus* bulk entropy; reduces to RT when $S_{\rm bulk}$ is subleading.
- The QES rule comes from the **replica trick with bulk matter** (LM + $\mathrm{Tr}\,\rho_{\rm bulk}^n$).
- Applied to radiation, the QES gives the **island** and the **Page curve** (Wks 6, 11).

## Exercises

**Core.**

1. **Two-saddle switch.** With $S_{{\rm gen},1}=A_1/4G_N+S_1^{\rm bulk}$ (no island) and $S_{{\rm gen},2}=A_2/4G_N+S_2^{\rm bulk}$ (island), find the radiation entropy at which the $\min$ switches; identify it as the Page time.
2. **Extremality condition.** Derive $K^{(a)}/4G_N=-\partial^{(a)}S_{\rm bulk}$ from $\delta_\mathcal{X}S_{\rm gen}=0$ and show it reduces to $K^{(a)}=0$ (RT) when $S_{\rm bulk}$ is negligible.
3. **Island formula.** From the QES rule for a radiation region, write the island formula and explain how $I$ arises as the bulk region minimising $S_{\rm gen}$.

**Starred.**

4. $\star$ **Replica + matter.** Repeat the Wk 4 conical-defect computation including the bulk-matter $\mathrm{Tr}\,\rho_{\rm bulk}^n$; show $-\partial_n|_{n=1}$ gives $S_{\rm gen}$ and that the surface is the QES.
5. $\star$ **UV cancellation.** Show explicitly that the leading area-law divergences of $\mathrm{Area}/4G_N$ and $S_{\rm bulk}$ cancel in $S_{\rm gen}$, renormalising $G_N$.

**Project.**

6. **EW in detail.** Read Engelhardt–Wall 1408.3203 and FLM 1307.2892; reproduce the QES prescription and the FLM correction, and connect to the island calculation of [[sem2-week-06-jt-gravity-page-curve|Wk 6]].

## Connections to other parts of the wiki

- **Within the course.** Upgrades [[week-13-ryu-takayanagi]]/[[week-14-hrt-and-subregion-subalgebra]]; built on [[sem2-week-04-replica-trick-in-gravity]] (LM); underpinned by [[sem2-week-13-quantum-focusing-anec]] (QFC); applied in [[sem2-week-06-jt-gravity-page-curve]] and [[sem2-week-11-island-formula]].
- **Concepts.** [[quantum-extremal-surfaces]], [[ryu-takayanagi-formula]], [[page-curve]].
- **AQFT course cross-reference.** $S_{\rm bulk}$ is the type III$_1$ von Neumann entropy of AQFT Block B; the algebraic version of $S_{\rm gen}$ is the crossed-product trace ([[crossed-product-and-island-formula]]).
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 1. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*
