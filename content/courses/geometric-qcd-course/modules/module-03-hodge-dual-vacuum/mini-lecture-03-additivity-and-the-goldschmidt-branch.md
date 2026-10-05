---
title: "Mini-Lecture III.3: Additivity and the Goldschmidt Branch"
type: lecture-notes
course: geometric-qcd-course-guide
module: 3
lecture: "III.3"
modified: 2026-10-05
---

# Mini-Lecture III.3: Additivity and the Goldschmidt Branch

*We study additive dressing and competing surface areas. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** III.2; matrix traces and elementary surface area. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); additive dressing and competing surface areas (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 73-76. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 3|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 73-76.

## The question

Why does an area dressing need additivity at a splitting point? The issue is compatibility between two sides of a functional equation. It does not follow from an identity equating a Wilson loop on a concatenated contour with a product of Wilson loops.

## Deriving the compatibility condition

Write the planar equation schematically as

$$
\mathcal L W[C]=\lambda\int K(C;x,y)W[C_{xy}]W[C_{yx}].
$$

Let $W=e^{-\kappa S}F$ and assume the regulated chain rule and $\mathcal LS=0$ from III.2. The left side is $e^{-\kappa S[C]}\mathcal LF[C]$. The right side is

$$
\lambda\int K(C;x,y)
e^{-\kappa(S[C_{xy}]+S[C_{yx}])}
F[C_{xy}]F[C_{yx}].
$$

For a real $S$ and nonzero $\kappa$, the common dressing cancels pointwise at the allowed splittings if

$$
S[C]=S[C_{xy}]+S[C_{yx}].
$$

What remains is the original equation for $F$. We have proved compatibility of a multiplicative ansatz under the hypotheses. We have not proved $F[C]=F[C_{xy}]F[C_{yx}]$ or $W[C]=W[C_{xy}]W[C_{yx}]$.

## Worked counterexample: a trace is not multiplicative

Let $U=V=\operatorname{diag}(i,-i)$ in $SU(2)$. Then $\operatorname{tr}U/2=\operatorname{tr}V/2=0$, but $UV=-1$ and $\operatorname{tr}(UV)/2=-1$. Repeating these blocks gives the same discrepancy at arbitrarily large even dimension.

Large-$N_c$ factorization concerns expectation values of products of normalized traces, under the usual large-$N_c$ assumptions. It does not turn the normalized trace of a product into a product of traces. The example separates this algebraic distinction from any assumption about a gauge ensemble.

## The geometric branches

Two planar disks of radii $R_1,R_2$ have total area $\pi(R_1^2+R_2^2)$. This is an explicitly additive candidate when the two lobes are assigned separate spanning surfaces.

For two equal coaxial circles of radius $R$ in planes separated by $h$, a catenoid can be written $r(z)=a\cosh(z/a)$, $-h/2\le z\le h/2$, with $R=a\cosh(h/(2a))$. Its area follows from $r'= \sinh(z/a)$:

$$
A_{\mathrm{cat}}=2\pi\int_{-h/2}^{h/2}r\sqrt{1+r'^2}\,dz
=\pi ah+\pi a^2\sinh(h/a).
$$

The disconnected disks have $A_{\mathrm{disks}}=2\pi R^2$. Existence, area comparison, and stability of a connected solution are distinct questions. These two-boundary surfaces are a useful model of competing topologies; they are not automatically the solution for every self-intersecting single contour.

For example, at $h=2a$, $R=a\cosh1$. The two areas divided by $\pi a^2$ are $2+\sinh2\approx5.627$ and $2\cosh^21\approx4.762$. The disconnected candidate is smaller for these parameters. This is a calculation, not a universal preference for disconnection.

## What the Goldschmidt selection would mean

The source selects an additive branch to implement its dressing ansatz. That is a condition within the construction. It is not a general theorem that every connected worldsheet is forbidden in planar QCD. A cylinder has genus zero and two boundaries, so topological suppression must count boundaries as well as handles.

Likewise, a bridge existence theorem requires hypotheses about the surfaces, boundary perturbation, and convergence. Weak convergence of surfaces alone does not imply alignment of their tangent tensors at every shrinking neck. IV.6 keeps that matching as an explicit input.

## Worked laboratory: a numerical area comparison

Set the catenoid parameter $a=1$ and separation $h=2$. The boundary radius is $R=\cosh1$. Direct substitution gives $A_{\mathrm{cat}}/\pi=2+\sinh2\approx5.627$ and $A_{\mathrm{disks}}/\pi=2\cosh^21\approx4.762$. Thus the disconnected candidate has lower area in this example.

Changing $h/a$ changes the comparison and can also affect existence and stability. This calculation concerns two coaxial boundary circles. A claim about a self-intersecting Wilson contour needs its own boundary and topological admissibility conditions.

## What is established

The dressing compatibility, matrix counterexample, disk area, and catenoid area are exact within their stated models. Selection, stability, and uniqueness of the QCD branch remain source claims. No general minimal-surface theorem is used here without specifying the surface class.

## Looking ahead

III.4 distinguishes a geometric ansatz from a physical vacuum. III.5 then tests the proposed area tensor and the conformal boundary problem directly.

## Problem set

1. **Classroom core.** Evaluate $\operatorname{tr}(UV)/2$ for the matrices in the derivation.

2. **Self-study calculation.** Derive the catenoid area integral.

3. **Self-study interpretation.** What factorizes when the geometric area is additive?

4. **Research extension.** State an applicable bridge or minimal-surface theorem with its hypotheses.

## Answer checkpoints

1. $UV=-1_2$, so the normalized trace is $-1$ although both individual normalized traces vanish.

2. $r=a\cosh(z/a)$ and $\sqrt{1+r'^2}=\cosh(z/a)$. Integrating $2\pi a\cosh^2(z/a)$ yields $\pi ah+\pi a^2\sinh(h/a)$.

3. The exponential dressing. Multiplicativity of a single traced holonomy does not follow.

4. Completion: name the surface class, boundary perturbation, convergence topology, and exact conclusion. Check separately whether it implies the tangent alignment used in IV.6.

## Teaching note

Use the decisive step in problem 2 as the written exit check for III.3; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-02-area-derivatives-and-self-dual-zero-modes|Previous note]] · [[mini-lecture-04-physical-vacuum-and-instanton-language|Next note]] · [[geometric-qcd-course-guide|Course guide]]
