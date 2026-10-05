---
title: "Mini-Lecture I.4: Loop Derivatives and Area Derivatives"
type: lecture-notes
course: geometric-qcd-course-guide
module: 1
lecture: "I.4"
modified: 2026-10-05
---

# Mini-Lecture I.4: Loop Derivatives and Area Derivatives

*We study plaquette insertions and the conditional product rule. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** I.3; commutators and oriented area. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); plaquette insertions and the conditional product rule (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 13-14. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 1|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 13-14.

## The physical question

How can a variation of a contour measure the gauge curvature? We first calculate a small rectangular holonomy, then use point-separated insertions to define the loop operator. This order keeps the geometry, signs, and regularity assumptions visible.

## Ordered insertions and conventions

For this lecture use the source's ordered-product convention: later parameters stand on the left, $U(b,a)=\mathcal P\exp\int_a^b d\theta\,\dot C_\mu D_\mu$, and $\mathcal F_{\mu\nu}=[D_\mu,D_\nu]$. This is an algebraic transport convention. Translating to the parallel section convention $D=\partial+\mathcal A$, $U=\mathcal P e^{-\int\mathcal A}$ of I.2 reverses the oriented infinitesimal transport. The same orientation must be used for the area element. See the course conventions.

Varying one factor in a time-sliced ordered product gives

$$
\frac{\delta U(b,a)}{\delta\dot C_\mu(\theta)}
=U(b,\theta)D_\mu U(\theta,a).
$$

Keep the two derivative positions separated until their order is fixed. An oriented area insertion is defined here by

$$
A_{\mu\nu}(\theta)=
\frac{\delta^2}{\delta\dot C_\mu(\theta+0)\delta\dot C_\nu(\theta-0)}
-\frac{\delta^2}{\delta\dot C_\nu(\theta+0)\delta\dot C_\mu(\theta-0)}.
$$

It inserts $D_\mu D_\nu-D_\nu D_\mu=\mathcal F_{\mu\nu}$ with our ordering. Reversing the two point labels reverses the area orientation; the source sometimes writes that alternative convention. Neither convention changes the need for the difference of the two neighboring dot derivatives below.

## Worked derivation: a small plaquette

Put $X=aD_\mu$, $Y=bD_\nu$, with $a,b$ small. Multiplying the four Taylor series in

$$
e^Xe^Ye^{-X}e^{-Y}
$$

through bilinear order gives $1+XY-YX+O(a^2b,ab^2)$: the linear terms and pure squares cancel. Hence

$$
U_\square=1+ab\,\mathcal F_{\mu\nu}+O(a^2b,ab^2).
$$

The sign changes when the rectangle is traversed in the opposite direction. Inserting this rectangle at $\theta$ in a large loop gives the curvature surrounded by the remaining holonomy. One must retain those transport factors:

$$
A_{\mu\nu}W[C]=\frac1{N_c}
\left\langle\operatorname{tr}\,
U(2\pi,\theta)\mathcal F_{\mu\nu}U(\theta,0)\right\rangle.
$$

A bare trace of a commutator vanishes in finite dimensions. It is not the insertion appearing here.

## The loop operator

Define the discontinuity of a dot derivative by

$$
\Delta_\mu(\theta)=
\frac{\delta}{\delta\dot C_\mu(\theta+0)}
-\frac{\delta}{\delta\dot C_\mu(\theta-0)}.
$$

Then the vector operator and its tangent contraction are

$$
\mathcal L_\nu(\theta)=\Delta_\mu(\theta)A_{\mu\nu}(\theta),
\qquad
L=\oint d\theta\,\dot C_\nu(\theta)\mathcal L_\nu(\theta).
$$

This is the composition of a difference with an area derivative. The two dot derivatives are not multiplied together and an area derivative is not subtracted from that product. Acting on the ordered insertion yields $[D_\mu,\mathcal F_{\mu\nu}]$, again with the surrounding holonomy. This is the connection with the Yang–Mills equation.

## What the product rule requires

An ordinary second-order differential operator need not be a derivation. Here the useful product rule relies on a discontinuity prescription. Assume that $F$ and $G$ have first dot derivatives continuous across the insertion, while their ordered second derivatives admit finite antisymmetric limits. In $A_{\mu\nu}(FG)$ the cross terms built from first derivatives then cancel after antisymmetrization, leaving $(A_{\mu\nu}F)G+F(A_{\mu\nu}G)$.

Apply $\Delta_\mu$ to this expression. The terms $(A_{\mu\nu}F)\Delta_\mu G$ and $(\Delta_\mu F)A_{\mu\nu}G$ vanish by continuity. Thus

$$
\mathcal L_\nu(FG)=(\mathcal L_\nu F)G+F(\mathcal L_\nu G)
$$

on this regularity class, provided the regulated limits and products exist. Extension to singular Wilson-loop distributions is an additional analytic problem. The matrix identity $[X,AB]=[X,A]B+A[X,B]$ motivates the rule but alone does not establish that extension.

Under the same hypotheses the chain rule gives

$$
\mathcal L_\nu(e^{-\kappa S}F)
=e^{-\kappa S}\mathcal L_\nu F
-\kappa e^{-\kappa S}F\,\mathcal L_\nu S.
$$

If $\mathcal L_\nu S=0$, the dressing passes through the left side of a loop equation. Compatibility with its splitting term additionally needs the area additivity discussed in III.3. A zero mode alone is not a solution of the inhomogeneous Makeenko–Migdal equation.

## A useful comparison

For $D_x=d/dx$, $D_x(FG)=F'G+FG'$. For $D_x^2$ there is the extra term $2F'G'$. Taking $F=G=x$ gives $D_x^2(x^2)=2$ while $F''G+FG''=0$. This simple calculation explains why the regulated product argument above is necessary.

## Worked laboratory: retaining the surrounding holonomy

Let $X=\sigma_1$, $Y=\sigma_2$, and choose the surrounding matrix $U=\sigma_3$. Since $[X,Y]=2i\sigma_3$, we have
$$
\operatorname{tr}[X,Y]=0,\qquad
\operatorname{tr}(U[X,Y])=4i.
$$
The second expression is an insertion into a nontrivial ordered product. Dropping that product would erase the observable. The example also shows why the equation of motion must be inserted with its color structure instead of replacing it by a bare trace.

## What is established

The plaquette expansion and ordered insertion algebra are exact through the stated orders in the side lengths. The product rule is a formal result under the explicitly stated continuity and limit assumptions. The physical continuum domain is not constructed in these notes.

## Looking ahead

I.5 inserts this operator into a regulated Schwinger–Dyson identity. Module III asks whether a proposed geometric area supplies a zero mode and satisfies the additional splitting requirement.

## Problem set

1. **Classroom core.** Compute the two traces in the laboratory.

2. **Self-study calculation.** Evaluate $d^2(x^2)/dx^2$ and compare with the proposed first-order product rule.

3. **Self-study interpretation.** State the extra condition needed to dress the right side of the MM equation.

4. **Research extension.** Examine point splitting on IAS pp. 13–14 and the zero-mode discussion on pp. 70–72.

## Answer checkpoints

1. $\operatorname{tr}\sigma_3=0$ and $\sigma_3^2=1$ give $0$ and $4i$.

2. The derivative is $2$, whereas $x''x+xx''=0$. The missing cross term is $2x'x'=2$.

3. Area additivity at the supported splitting: $S[C]=S[C_{xy}]+S[C_{yx}]$. A left-side zero mode alone is insufficient.

4. Completion: specify a class of functionals, the order of limits, and the continuity assumptions used to cancel product cross terms. An unqualified appeal to the matrix commutator identity is not a completion.

## Teaching note

Use the decisive step in problem 2 as the written exit check for I.4; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-03-holonomy-and-parallel-transport|Previous note]] · [[mini-lecture-05-the-makeenko-migdal-equation|Next note]] · [[geometric-qcd-course-guide|Course guide]]
