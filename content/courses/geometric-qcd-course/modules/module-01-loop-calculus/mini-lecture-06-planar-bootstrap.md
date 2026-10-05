---
title: "Mini-Lecture I.6: The Bootstrap Generation of Planar Graphs"
type: lecture-notes
course: geometric-qcd-course-guide
module: 1
lecture: "I.6"
modified: 2026-10-05
---

# Mini-Lecture I.6: The Bootstrap Generation of Planar Graphs

*We study one-gluon exchange and a checked resolvent expansion. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** I.5; Gaussian gauge-field contraction. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); one-gluon exchange and a checked resolvent expansion (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 17, 19, 31-36. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 1|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 17, 19, 31-36.

## The physical question

The loop equation is nonlinear. What does its perturbative iteration reproduce, and what would a match to gauge-fixed perturbation theory require? We can calculate its first Wilson-loop term and a resolvent expansion explicitly. The all-orders equivalence asserted in the slides remains a source claim.

## A controlled first term

Use Hermitian generators with $\operatorname{tr}(T^aT^b)=\delta^{ab}/2$, a Euclidean gauge field, and $U[C]=\mathcal P e^{ig\oint A_\mu^aT^a dx^\mu}$. Expand to second order. The linear term averages to zero. In free Feynman gauge,

$$
\langle A_\mu^a(x)A_\nu^b(y)\rangle_0
=\delta^{ab}\delta_{\mu\nu}G(x-y),
\qquad G(r)=\frac{1}{4\pi^2r^2}.
$$

Since the contracted integrand is symmetric under exchange of the two contour parameters, the ordered integration region is half the square. Using $\sum_aT^aT^a=C_F1$, $C_F=(N_c^2-1)/(2N_c)$, we obtain

$$
W[C]=1-\frac{g^2C_F}{2}\oint_Cdx_\mu\oint_Cdy_\mu\,G(x-y)+O(g^4).
$$

The minus sign is $i^2$. This double integral requires a short-distance prescription near coincident points. At fixed $\lambda=g^2N_c$, its coefficient tends to $-\lambda/4$. The order and color factor can therefore be checked before attempting any resummation.

## Why the free kernel has this normalization

Away from $r=0$, the four-dimensional radial Laplacian gives $\Delta(r^{-2})=0$. On a ball of radius $\epsilon$,

$$
-\int_{B_\epsilon}\Delta G\,d^4x
=-\int_{\partial B_\epsilon}\partial_rG\,dS
=\frac{2}{4\pi^2\epsilon^3}(2\pi^2\epsilon^3)=1.
$$

Thus $-\Delta G=\delta^{(4)}$ distributionally. This flux calculation, rather than the equation away from the origin alone, determines the delta coefficient.

## Resolvents and the perturbative hierarchy

For a regulated invertible operator $K_0$, write $K=K_0+V$. If $\|K_0^{-1}V\|<1$, the Neumann series converges:

$$
K^{-1}=K_0^{-1}-K_0^{-1}VK_0^{-1}
+K_0^{-1}VK_0^{-1}VK_0^{-1}-\cdots.
$$

Multiplying on the left by $K$ cancels adjacent terms. Without the norm condition this is a formal perturbative expansion. Ordered products matter: $V$ cannot be commuted through $K_0^{-1}$.

Similarly, if $W=1+\lambda w_1+\lambda^2w_2+\cdots$, then the splitting product is

$$
W[C_1]W[C_2]
=1+\lambda(w_1[C_1]+w_1[C_2])
+\lambda^2(w_2[C_1]+w_2[C_2]+w_1[C_1]w_1[C_2])+\cdots.
$$

The second iteration does not consist solely of $w_1[C_1]w_1[C_2]$. This is an elementary but necessary bookkeeping step for comparing diagrams.

## Ghosts and what a matching calculation must do

Gauge fixing introduces the Faddeev–Popov operator $M=-\partial_\mu D_\mu$ in a covariant gauge and its determinant. Representing $\det M$ by anticommuting scalar fields $c,\bar c$ produces ghost propagators and ghost vertices. A closed ghost loop carries the Grassmann minus sign. A closed gluon loop does not.

Antisymmetry of $[A_\mu,A_\nu]$ controls color and vertex structure; it is not a derivation of ghost statistics. To establish the source's bootstrap claim one must specify a gauge, regulator, inverse kernel, and boundary conditions; recover gluon and ghost contributions with their symmetry factors; and check the relevant Ward or Slavnov–Taylor identities. The slides' graph sketches motivate this comparison but do not supply it at every order.

## Worked matrix example

Let $K_0=\operatorname{diag}(2,3)$ and $V=\epsilon\begin{pmatrix}0&1\\1&0\end{pmatrix}$. Direct inversion gives

$$
K^{-1}=\frac1{6-\epsilon^2}
\begin{pmatrix}3&-\epsilon\\-\epsilon&2\end{pmatrix}.
$$

Expansion yields diagonal entries $1/2+\epsilon^2/12$ and $1/3+\epsilon^2/18$, and off-diagonal entries $-\epsilon/6+O(\epsilon^3)$. The first three Neumann terms give exactly these coefficients. They exhibit propagation, one insertion, and two insertions without implying that every insertion already has a unique QCD diagram interpretation.

## Worked laboratory: a second-order hierarchy

For scalar test values $w_1[C_1]=2$, $w_1[C_2]=3$, $w_2[C_1]=5$, $w_2[C_2]=7$, multiplication of the two truncated series gives
$$
(1+2\lambda+5\lambda^2)(1+3\lambda+7\lambda^2)
=1+5\lambda+18\lambda^2+O(\lambda^3).
$$
The quadratic coefficient contains both second-order pieces and the product $2\cdot3$. This finite check is a useful guard against omitting terms in the nonlinear loop recursion.

## What is established

The free contour term, flux normalization, and finite-matrix expansion are controlled calculations. The reconstruction of the full gauge-fixed planar perturbation series is stated only from the IAS source, with the missing comparison specified above.

## Looking ahead

I.7 studies the singularities that the first contour integral already exposes. Momentum loop variables reorganize those singularities; they do not remove the obligation to define the functional measure.

## Problem set

1. **Classroom core.** Reproduce the coefficient $18$.

2. **Self-study calculation.** Check the finite-matrix inverse in the main derivation through order $\epsilon^2$.

3. **Self-study interpretation.** Which closed loop has the Grassmann minus sign in gauge-fixed perturbation theory?

4. **Research extension.** Design a one-loop match between the bootstrap and a gauge-fixed calculation.

## Answer checkpoints

1. It is $5+7+2\cdot3$.

2. Expand $(6-\epsilon^2)^{-1}=1/6+\epsilon^2/36+\cdots$. The diagonal corrections are $\epsilon^2/12$ and $\epsilon^2/18$, and the off-diagonal first term is $-\epsilon/6$.

3. A ghost loop, represented by anticommuting Faddeev–Popov fields. A gluon loop does not acquire that sign merely from being closed.

4. Completion: specify the regulator, gauge, observable, and all gluon and ghost contributions with symmetry factors. A list of superficially similar diagrams is insufficient.

## Teaching note

Use the decisive step in problem 2 as the written exit check for I.6; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-05-the-makeenko-migdal-equation|Previous note]] · [[mini-lecture-07-coordinate-space-catastrophe|Next note]] · [[geometric-qcd-course-guide|Course guide]]
