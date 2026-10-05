---
title: "Mini-Lecture II.3: Factorization of the Momentum Loop Measure"
type: lecture-notes
course: geometric-qcd-course-guide
module: 2
lecture: "II.3"
modified: 2026-10-05
---

# Mini-Lecture II.3: Factorization of the Momentum Loop Measure

*We study closure constraints and factorization of a finite measure. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** II.1–II.2; delta functions under linear changes of variables. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); closure constraints and factorization of a finite measure (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked Source reconstruction explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 49-50. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 2|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 49-50.

## The question

How can a contact constraint become two closure constraints after a loop is cut? The finite answer is a change of variables with unit Jacobian. Extending it to a functional measure and claiming ultraviolet finiteness are separate steps.

## The two displacements

Split a polygon into blocks with displacements $s=\sum_{j\in A}h_j$ and $t=\sum_{j\in B}h_j$. Overall closure is $\delta^{(4)}(s+t)$. Requiring the first block to return to its starting point adds $\delta^{(4)}(s)$. On these constraint coordinates,
$$
\delta^{(4)}(s+t)\delta^{(4)}(s)
=\delta^{(4)}(s)\delta^{(4)}(t).
$$
The map $(s,t)\mapsto(s,s+t)$ has determinant one. Applying either side to a smooth compactly supported test function gives its value at $(0,0)$. The identity is therefore well-defined for independent constraint coordinates.

If the remaining measure and weight factorize between the two blocks, each block now carries its own closure constraint and the integral factorizes. Correlated weights, a common zero-mode volume, or singular redundant constraints can obstruct that conclusion. The contact delta has been incorporated into the measure; its distributional nature has not disappeared.

## Formal coordinate-loop notation

The source writes a tangent measure
$$
D_C=\delta^{(4)}\!\left(\int_0^{2\pi}\dot C\,d\theta\right)
\prod_\theta d^4\dot C(\theta).
$$
Since $C(\theta_2)-C(\theta_1)=\int_{\theta_1}^{\theta_2}\dot C\,d\theta$, the contact at a cut has precisely the form of the additional block constraint. Under the factorized-measure assumptions, source equation (34) becomes
$$
\delta^{(4)}\!\left(\int_{\theta_1}^{\theta_2}\dot C\,d\theta\right)D_C
=D_{C_{12}}D_{C_{21}}.
$$
This is a useful formal notation for the finite identity. An infinite product of Lebesgue measures does not itself define a continuum functional integral. Base-point integration, regulator, gauge volume, and normalization must be specified before the equality is used there.

## A tangent insertion becomes a source derivative

With the positive Fourier kernel $e^{i\int P\cdot\dot C}$,
$$
\frac{\delta}{\delta P_\nu(\theta)}e^{i\int P\cdot\dot C}
=i\dot C_\nu(\theta)e^{i\int P\cdot\dot C}.
$$
Thus multiplication by the coordinate tangent becomes $(1/i)\delta/\delta P_\nu$. This follows by differentiating the kernel; no integration by parts in the coordinate tangent is needed. Moving the derivative through an integral still requires its own convergence assumptions.

Suppose the regulated coordinate equation has coefficient $\lambda_{\mathrm{loop}}$ multiplying its split term. After the block-factorization step, its transform has schematically
$$
\mathcal F[\mathcal L_\nu W]
=\frac{\lambda_{\mathrm{loop}}}{i}\int d\theta\,
\frac{\delta}{\delta P_\nu(\theta)}
\left(W[P_{0,\theta}]W[P_{\theta,2\pi}]\right).
$$
The assignment of endpoint insertions must follow the same regulator on both sides. Defining the transformed left operator with the corresponding factor $i/\lambda_{\mathrm{loop}}$ produces the form displayed in source equation (36):
$$
\widehat{\mathcal L}_\nu[P]W[P]
=\int d\theta\,\frac{\delta}{\delta P_\nu(\theta)}
\left(W[P_{0,\theta}]W[P_{\theta,2\pi}]\right).
$$
This normalization dictionary must accompany the formula. The absence of an explicit $i$ or coupling in the last line does not mean those factors were absent from the transform.

## What changed and what did not

The source proposes that the transformed left operator acts by a kinematic momentum tensor. II.4 explains the finite ordered-integral algebra used to organize that tensor. Establishing the full functional transformation requires more than the scalar Fourier analogy.

The contact is represented as closure of the cut loops, while its tangent becomes a source derivative. This is a change in mathematical form. It does not by itself prove that all continuum integrals, cusp subtractions, or boundary terms are finite. The source's stronger finiteness claim needs a defined regulator and a controlled limit.

In particular, an ordinary Fourier transform preserves much of a distribution's singular information rather than annihilating it. A successful momentum representation must show where that information goes and why the desired observables are well-defined. The finite Gaussian calculation below establishes exactly the block-factorization step, with every integration specified.

## Worked laboratory: the contact constraint splits two blocks

Use four real increments $a,b,c,d$. Global closure is $\delta(a+b+c+d)$. A cut that closes the first block adds $\delta(a+b)$. For fixed remaining variables set $s=a+b$, $t=c+d$; on these constraint coordinates,
$$
\delta(s+t)\delta(s)=\delta(s)\delta(t).
$$
The linear map $(s,t)\mapsto(s,s+t)$ has determinant one. Testing both sides against a smooth function gives its value at $s=t=0$, proving the identity without treating deltas as ordinary functions.

For a factorized weight $e^{-(a^2+b^2+c^2+d^2)/2}$, the integral is
$$
\left(\int da\,db\,\delta(a+b)e^{-(a^2+b^2)/2}\right)^2
=\left(\int da\,e^{-a^2}\right)^2=\pi.
$$
Without the extra contact constraint the blocks remain coupled by global closure. Nonfactorizing weights or gauge-volume factors would also obstruct this elementary factorization. This identifies the assumptions behind the analogous formal loop-measure step.

## Problem set

1. **Classroom core.** Compute the determinant of $(s,t)\mapsto(s,s+t)$.

2. **Self-study calculation.** Evaluate each constrained Gaussian block.

3. **Self-study interpretation.** Why does global closure alone not factorize the two blocks?

4. **Research extension.** Repeat this construction for a polygonal loop in four dimensions.

## Answer checkpoints

1. It is one.

2. Set $b=-a$ using the delta. The integral becomes $\int e^{-a^2}da=\sqrt\pi$.

3. It imposes only $s+t=0$, allowing nonzero opposite displacements. Separate closure requires the contact constraint too.

4. Completion: show all vector constraints and Jacobians, fix the base-point translation, and identify any action or gauge factors that prevent a product measure.

## Teaching note

Use the decisive step in problem 2 as the written exit check for II.3; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-02-quark-loop-amplitudes-in-phase-space|Previous note]] · [[mini-lecture-04-kinematic-tensors-and-magnus-forms|Next note]] · [[geometric-qcd-course-guide|Course guide]]
