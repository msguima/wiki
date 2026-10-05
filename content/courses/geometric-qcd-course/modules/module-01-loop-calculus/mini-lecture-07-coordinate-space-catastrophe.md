---
title: "Mini-Lecture I.7: Coordinate-Space Contact Singularities"
type: lecture-notes
course: geometric-qcd-course-guide
module: 1
lecture: "I.7"
modified: 2026-10-05
---

# Mini-Lecture I.7: Coordinate-Space Contact Singularities

*We study the crossing logarithm and operator mixing. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** I.6; polar coordinates and distributions. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); the crossing logarithm and operator mixing (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 20-30, 37-42. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 1|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 20-30, 37-42.

## The question

The loop equation contains distributions evaluated on contours. Why is renormalizing a single prescribed contour insufficient to define the entire equation? We examine a crossing integral before considering momentum variables.

## Smooth segments, cusps, and crossings

A Wilson loop is a gauge-invariant observable once its regulator and renormalization are specified. Smooth contours, cusps, and self-intersections have different ultraviolet structures. A difficulty in one proposed functional equation does not imply that Wilson loops are unphysical or that gauge theory cannot be renormalized.

For a smooth contour the coincident-segment singularity already appears in the one-gluon integral of I.6. A cusp introduces dependence on the angle between adjacent tangents. At a self-intersection, several reconnections of the color transport can mix under renormalization. The natural renormalization object can therefore be a matrix acting on a family of contour operators.

If $W_i^{\mathrm{bare}}=Z_{ij}W_j^{\mathrm{ren}}$, differentiation gives

$$
\delta W_i^{\mathrm{bare}}=(\delta Z_{ij})W_j^{\mathrm{ren}}
+Z_{ij}\delta W_j^{\mathrm{ren}}.
$$

A contour derivative does not in general commute with subtraction of geometric divergences. This is the structural issue behind the source's criticism of a naive scalar, multiplicative subtraction.

## Worked crossing integral

Near a transverse crossing, approximate the two segments by $x=su$, $y=tv$, where $u,v$ are unit vectors and $u\cdot v=\cos\phi$, with $0<\phi<\pi$. Their squared separation is

$$
|x-y|^2=s^2+t^2-2st\cos\phi.
$$

Set $a=s-t\cos\phi$, $b=t\sin\phi$. The Jacobian is $|\sin\phi|$, so in an annular neighborhood of the origin,

$$
\int\frac{ds\,dt}{|su-tv|^2}
=\frac1{|\sin\phi|}\int_\epsilon^L\frac{r\,dr}{r^2}\int_0^{2\pi}d\vartheta
=\frac{2\pi}{|\sin\phi|}\log\frac L\epsilon.
$$

The gluon numerator adds the tangent contraction $\cos\phi$, and the full contour geometry sets the integration domains and finite parts. This local model demonstrates a logarithmic singularity with angular dependence. Parallel tangents are a degenerate limit of this calculation and require separate analysis.

## Why a contact term needs a prescription

The four-dimensional delta distribution in the MM equation is integrated along a one-dimensional contour. At a self-crossing the embedding has multiple preimages; at the diagonal it has an entire local coincidence structure. Writing $\delta^{(4)}(0)$ as a number or simply discarding it does not define either contribution.

One can start from a lattice, smearing, or point-splitting regulator and ask whether the renormalized equation has a well-defined limit. Each choice must specify how the loop derivatives, splitting term, and operator mixing are related. Different formal expressions may agree only after that matching.

## What momentum variables change

A Fourier transform turns derivatives into momentum factors and contact distributions into algebraic expressions. It can make a hierarchy easier to organize. The transform still needs a space of test functionals, a measure, normalization, and control of limits. Disappearance of an explicit coordinate delta is not alone a proof of ultraviolet finiteness.

The IAS proposal develops this reorganization in Module II. We treat it as a formal change of variables with specific algebraic consequences, then test those consequences separately.

## Worked laboratory: varying a subtraction

In a scalar model let $Z(\phi,\epsilon)=1+g^2c(\phi)\log(1/\epsilon)$ and $W_{\mathrm{bare}}=ZW_{\mathrm{ren}}$. Differentiation in the crossing angle gives
$$
\partial_\phi W_{\mathrm{bare}}
=g^2c'(\phi)\log(1/\epsilon)\,W_{\mathrm{ren}}
+Z\,\partial_\phi W_{\mathrm{ren}}.
$$
Even if $W_{\mathrm{ren}}$ is finite, subtracting first and differentiating first are not interchangeable without the first term. The matrix-mixing case has the same product rule with indices.

## What is established

The crossing logarithm and differentiated mixing relation are explicit calculations. A general obstruction to every coordinate-space renormalization is not proved here. The source's stronger rhetoric is replaced by the precise limitation of the naive subtraction scheme.

## Looking ahead

II.1 begins with a finite Fourier transform where normalization and derivative signs can be checked directly.

## Problem set

1. **Classroom core.** Compute the crossing integral's coefficient at $\phi=\pi/6$ before the tangent numerator.

2. **Self-study calculation.** Differentiate the model subtraction explicitly.

3. **Self-study interpretation.** Does this example prove that renormalized Wilson loops do not exist?

4. **Research extension.** Formulate one regulated crossing problem in coordinate space.

## Answer checkpoints

1. $2\pi/|\sin(\pi/6)|=4\pi$.

2. The derivative of $Z$ is $g^2c'(\phi)\log(1/\epsilon)$, giving the additional term displayed above.

3. No. It shows why a naive contour-dependent subtraction does not automatically commute with the loop derivatives.

4. Completion: give the contour, regulator, operator basis, mixing prescription, and limiting quantity. The result may be an obstruction to that prescription, not a universal impossibility statement.

## Teaching note

Use the decisive step in problem 2 as the written exit check for I.7; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-06-planar-bootstrap|Previous note]] · [[mini-lecture-01-why-momentum-loop-space|Next note]] · [[geometric-qcd-course-guide|Course guide]]
