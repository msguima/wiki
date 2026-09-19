---
title: "Sem II Week 1 — Holographic renormalisation in depth"
type: lecture-notes
course: syllabus
semester: 2
week: 1
block: 1
duration: "3 hours (lecture + seminar)"
status: drafting
modified: 2026-05-28
---

# Sem II Week 1 — Holographic Renormalisation in Depth

> *Semester II Block 1 sharpens the tools. We met holographic renormalisation in [[week-09-holographic-renormalisation|Sem I Wk 9]] — divergences as boundary UV, the Fefferman–Graham (FG) recursion, counterterms, the $d=2$ anomaly. This week makes it systematic and general: the **full FG expansion of the metric**, the **holographic stress tensor** $\langle T_{\mu\nu}\rangle$ from the response coefficient $g_{(d)}$, **operator mixing** when dimensions differ by integers, the **$d=4$ Weyl anomaly** from the FG log term, and **scheme equivalence** (Skenderis). These are the prerequisites for the modular Hamiltonian (Wk 3) and the replica/conical-defect action (Wk 4).*

## Learning goals

By the end of this week, a student can:

1. Write the general FG expansion of the bulk metric and identify free vs determined coefficients.
2. Explain the $\rho^{d/2}\log\rho$ term as the seed of the conformal anomaly.
3. Write the holographic stress tensor in terms of $g_{(d)}$ and state its conservation.
4. Derive the operator-mixing matrix when $\Delta_1-\Delta_2\in\mathbb{Z}$.
5. State scheme equivalence (renormalised correlators are scheme-independent).

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Advanced AdS/CFT* §6** — the *Holographic Renormalization* page; compare *AdS/CFT Foundations* §6, which is the gentler first pass.
- de Haro, Skenderis, Solodukhin, [arXiv:hep-th/0002230](https://arxiv.org/abs/hep-th/0002230) — the systematic FG/stress-tensor procedure.
- Skenderis, [arXiv:hep-th/0209067](https://arxiv.org/abs/hep-th/0209067) — the canonical review; scheme equivalence.

**Prerequisites.** [[week-09-holographic-renormalisation]] (the basics — FG recursion, leading counterterm, $d=2$ anomaly), [[week-08-gkp-witten-formula]] (dictionary, $\Delta(\Delta-d)=m^2L^2$). This week assumes Wk 9 and goes deeper.

**AQFT cross-reference.** None directly (faint parallel to operator mixing in [[week-13-crossed-product-construction|AQFT Wk 13]]).

## 1. The Fefferman–Graham expansion in general

Write the asymptotically-AdS metric in FG gauge (radial coordinate $\rho$, $\rho\to0$ the boundary):

$$
ds^2 = L^2\Big(\frac{d\rho^2}{4\rho^2} + \frac{1}{\rho}\,g_{\mu\nu}(x,\rho)\,dx^\mu dx^\nu\Big),
\quad
g_{\mu\nu}(x,\rho) = g_{(0)\mu\nu} + \rho\,g_{(2)\mu\nu} + \cdots + \rho^{d/2}\big(g_{(d)\mu\nu} + \log\rho\;h_{(d)\mu\nu}\big) + \cdots
$$

Plug into Einstein's equations and solve order by order in $\rho$:

- **$g_{(0)}$** is the boundary metric — the *source* (a fixed boundary condition).
- **$g_{(2)},g_{(4)},\dots$ up to $g_{(d-2)}$** are **determined locally** by $g_{(0)}$ (curvature tensors of $g_{(0)}$): e.g. $g_{(2)\mu\nu}=-\tfrac{1}{d-2}\big(R_{\mu\nu}-\tfrac{1}{2(d-1)}R g_{(0)\mu\nu}\big)$.
- **$g_{(d)}$** is the **response** — *not* fixed by $g_{(0)}$; it requires the full regular-in-the-interior solution and carries the dynamical one-point function $\langle T_{\mu\nu}\rangle$.
- **$h_{(d)}$** (the $\log\rho$ coefficient) appears **only in even $d$**; it is local in $g_{(0)}$ and is the **seed of the conformal anomaly** (its presence is why $g_{(d)}$ is only partly constrained, by $\nabla^\mu g_{(d)\mu\nu}$ and a trace condition).

This generalises the scalar FG recursion of [[week-09-holographic-renormalisation|Wk 9]] to the metric sector. The local/non-local split (source determined; response free) is the structural backbone.

> **[Stated-without-proof]** the FG expansion and the local determination of $g_{(2)},\dots,g_{(d-2)},h_{(d)}$ (de Haro–Skenderis–Solodukhin); $g_{(2)}$ shown.

## 2. The holographic stress tensor

The renormalised one-point function of the boundary stress tensor is the response coefficient:

$$
\boxed{\;\langle T_{\mu\nu}\rangle = -\frac{2}{\sqrt{g_{(0)}}}\frac{\delta S_{\rm ren}}{\delta g_{(0)}^{\mu\nu}} = \frac{d\,L^{d-1}}{16\pi G_N}\,g_{(d)\mu\nu} + X_{\mu\nu}[g_{(0)}],\;}
$$

where $X_{\mu\nu}$ is a **local** functional of the boundary curvature (scheme-dependent, present in even $d$). Two general properties follow from bulk diffeomorphism invariance, pushed to the boundary:

- **Conservation:** $\nabla^\mu\langle T_{\mu\nu}\rangle=0$ (away from anomaly insertions) — **[Proven]**, the diffeomorphism Ward identity.
- **Trace = anomaly:** $\langle T^\mu{}_\mu\rangle=\mathcal{A}[g_{(0)}]$, non-zero only in even $d$, fixed by $h_{(d)}$.

So $g_{(d)}$ is *the* dictionary entry for $\langle T_{\mu\nu}\rangle$, exactly as $\psi^{(0)}$ was for $\langle\mathcal{O}\rangle$ in Wk 9.

## 3. The $d=4$ Weyl anomaly (worked structure)

In even $d$ the $\rho^{d/2}\log\rho$ term obstructs Weyl invariance of $S_{\rm ren}$, giving the conformal anomaly. In $d=4$ it takes the standard two-invariant form

$$
\langle T^\mu{}_\mu\rangle = \frac{1}{16\pi^2}\big(c\,W^2 - a\,E_4\big),
$$

with $W^2$ the Weyl-tensor-squared and $E_4$ the Euler density. Computing the FG log term from the bulk gives both coefficients in terms of $L^3/G_N$, and — crucially — **$a=c$ at the two-derivative (Einstein) level**:

$$
a = c \;\propto\; \frac{L^3}{G_N}
$$

<!-- CHECK: exact a=c coefficient (e.g. a=c=pi L^3/8 G_5, and the N=4 value (N^2-1)/4); confirm normalisation against de Haro-Skenderis-Solodukhin before quoting a number. -->

The equality $a=c$ is the hallmark of a strongly-coupled large-$N$ CFT with a *two-derivative* (Einstein) gravity dual; splitting $a\ne c$ requires higher-curvature bulk terms ($R^2$, i.e. finite-$\lambda$ stringy corrections). This refines the $d=2$ Brown–Henneaux result $c=3L/2G$ of [[week-09-holographic-renormalisation|Wk 9]] to four dimensions.

> **[Sketched]** the $d=4$ anomaly from the FG log term, $a=c\propto L^3/G_N$; **exact coefficient flagged `CHECK`** (the structure and $a=c$ are robust; the numerical factor is scheme/normalisation).

## 4. Operator mixing (worked)

A subtlety invisible in the leading analysis: when two operators have dimensions $\Delta_1,\Delta_2$ with $\Delta_1-\Delta_2\in\mathbb{Z}_{>0}$ (or an operator and a curvature term of matching dimension), the near-boundary expansions overlap and the **counterterms mix their sources**. Concretely, the source $J_1$ of $\mathcal{O}_1$ can appear at the same order in $\rho$ as the VEV of $\mathcal{O}_2$, so subtracting the divergence of $\langle\mathcal{O}_1\rangle$ requires a counterterm $\propto J_2$ — and the renormalised operators are linear combinations,

$$
\langle\mathcal{O}_1\rangle_{\rm ren} = \langle\mathcal{O}_1\rangle - M\,J_2,
$$

with $M$ a **scheme-dependent mixing coefficient**. The freedom in $M$ is exactly the freedom to add a finite local counterterm; it is the holographic image of **operator mixing / scheme dependence** in ordinary QFT renormalisation (the analogue of mass mixing between operators of equal dimension). Physical, scheme-independent data — anomalous dimensions, OPE coefficients — are unaffected; only the off-diagonal normalisation shifts.

> **[Proven within the model]** the mixing arises when $\Delta_1-\Delta_2\in\mathbb{Z}$ (the overlapping-expansion argument); the coefficient $M$ is scheme data.

## 5. Scheme equivalence

Different choices of finite counterterms shift $g_{(d)}$ (hence $\langle T_{\mu\nu}\rangle$) and the mixing $M$ by **local** functionals of $g_{(0)}$. **Skenderis' theorem:** all *covariant* holographic-renormalisation schemes are related by such finite local counterterms, and therefore yield the **same renormalised $n$-point correlators** (for $n\ge2$, at separated points). The scheme ambiguity is precisely the renormalisation-scheme ambiguity of the dual QFT — local, and dropping out of physical observables. This legitimises "the" holographic renormalisation: the procedure is canonical up to the same freedom one always has in defining composite operators.

> **[Stated-without-proof]** scheme equivalence (Skenderis, hep-th/0209067).

## 6. Key claims and proof status

- **[Stated-without-proof]** general FG expansion; local determination of $g_{(2..d-2)},h_{(d)}$; $g_{(d)}$ free (§1).
- **[Proven]** conservation of the holographic stress tensor (diffeo Ward identity) (§2).
- **[Sketched, coefficient `CHECK`]** $d=4$ anomaly $a=c\propto L^3/G_N$ (§3).
- **[Proven within the model]** operator mixing for integer-separated dimensions (§4).
- **[Stated-without-proof]** scheme equivalence (§5).

### `CHECK` items (Wk 1)
1. **§3** — exact $d=4$ anomaly coefficient ($a=c=?\,L^3/G_5$; $N=4$ value); the $a=c$ structure is robust, only the numerical factor is flagged.

## 7. What to take away

- **General FG:** $g_{\mu\nu}(x,\rho)=g_{(0)}+\rho g_{(2)}+\dots+\rho^{d/2}(g_{(d)}+\log\rho\,h_{(d)})$; source $g_{(0)}$ and low coefficients are local, **$g_{(d)}$ is the free response**, $h_{(d)}$ (even $d$) is the anomaly seed.
- **Holographic stress tensor:** $\langle T_{\mu\nu}\rangle=\tfrac{dL^{d-1}}{16\pi G_N}g_{(d)\mu\nu}+(\text{local})$; conserved; trace = anomaly.
- **$d=4$ anomaly:** $\langle T^\mu_\mu\rangle=\tfrac{1}{16\pi^2}(cW^2-aE_4)$ with **$a=c\propto L^3/G_N$** at two-derivative order (refines $d=2$ Brown–Henneaux).
- **Operator mixing** appears when dimensions differ by integers; it is scheme (finite-local-counterterm) data.
- **Scheme equivalence** (Skenderis): all covariant schemes give the same physical correlators.

## Exercises

**Core.**

1. **Log term.** For a scalar with $\Delta=d=4$ in AdS$_5$, show a $z^4\log z$ term appears in the near-boundary expansion and explain its anomaly role (cf. Wk 9 resonance).
2. **Counterterm for $\Delta=4$.** Construct the counterterm rendering the on-shell action finite for $m^2L^2=-4$ in AdS$_5$ and verify the $\epsilon\to0$ limit is finite.
3. **$d=4$ anomaly.** From the FG expansion, derive the $d=4$ Weyl anomaly structure $\propto(L^3/G_N)(\text{curvature}^2)$, identify the $E_4$ and $W^2$ pieces, and read off $a=c$ (flag the numerical factor).

**Starred.**

4. $\star$ **$g_{(2)}$.** Derive $g_{(2)\mu\nu}=-\tfrac{1}{d-2}(R_{\mu\nu}-\tfrac{1}{2(d-1)}Rg_{(0)\mu\nu})$ from Einstein's equations at order $\rho$.
5. $\star$ **Mixing matrix.** For two scalars with $\Delta_1-\Delta_2=2$, derive the source-mixing coefficient and relate it to a finite local counterterm.

**Project.**

6. **Stress-tensor two-point.** Use the linearised FG expansion (perturb $g_{(0)}\to\eta+h$) to compute $\langle T_{\mu\nu}T_{\rho\sigma}\rangle$ holographically and match its $|x|^{-2d}$ structure and central charge to the CFT.

## Connections to other parts of the wiki

- **Within the course.** Deepens [[week-09-holographic-renormalisation]]; the holographic stress tensor and FG expansion feed [[sem2-week-03-modular-flow-on-subregions]] (modular Hamiltonian as a $T_{\mu\nu}$ integral) and [[sem2-week-04-replica-trick-in-gravity]] (conical-defect renormalised action). Refines the $d=2$ anomaly of [[week-05-2d-cft-essentials|Sem I Wk 5]] / Wk 9 to $d=4$.
- **Concepts.** [[gkp-witten-formula]], [[holographic-dictionary]].
- **AQFT course cross-reference.** Faint parallel to operator mixing in [[week-13-crossed-product-construction|AQFT Wk 13]].
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 1. Draft (status: drafting) — pending expert review; see the `CHECK` item in §6 for the exact $d=4$ anomaly coefficient. Last revised 2026-05-28.*
