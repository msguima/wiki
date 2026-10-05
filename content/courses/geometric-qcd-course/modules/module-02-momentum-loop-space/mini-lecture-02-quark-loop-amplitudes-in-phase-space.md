---
title: "Mini-Lecture II.2: Quark Loop Amplitudes in Phase Space"
type: lecture-notes
course: geometric-qcd-course-guide
module: 2
lecture: "II.2"
modified: 2026-10-05
---

# Mini-Lecture II.2: Quark Loop Amplitudes in Phase Space

*We study phase-space integration and spin ordering. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** I.2 and II.1; Gaussian completion of the square. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); phase-space integration and spin ordering (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked Source reconstruction explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 47-48. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 2|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 47-48.

## The question

What does a momentum-space spin factor mean, and how is an ordered exponential related to a propagator? We must keep the finite evolution parameter, its integral, and the spin trace separate. Confusing them would make even the free-particle limit wrong.

## Recall the properly ordered coordinate representation

I.2 derives the quadratic proper-time resolvent and a Gaussian coordinate kernel. In a non-Abelian background, the color connection and field-strength spin insertion generally belong to one ordered product. Two separately ordered exponentials cannot simply be multiplied when their insertions fail to commute.

A proposed change to phase-space variables must reproduce that ordered object, including the current vertices of the chosen correlation function. Its free limit provides a necessary check before any interacting interpretation.

## Finite evolution in the first-order Dirac representation

For real Euclidean momentum $p$, Hermitian gamma matrices obeying $\{\gamma_\mu,\gamma_\nu\}=2\delta_{\mu\nu}$, and $m_q>0$, define
$$
H(p)=m_q+i\gamma\cdot p.
$$
Its eigenvalues have positive real part $m_q$, so
$$
H(p)^{-1}=\int_0^\infty dT\,e^{-T H(p)}
=\frac{m_q-i\gamma\cdot p}{m_q^2+p^2}.
$$
The last identity follows from $(\gamma\cdot p)^2=p^2$. The integrand at one fixed $T$ is a matrix evolution operator, not the propagator. Taking $T\to\infty$ in that integrand gives zero for positive mass; it cannot replace the integral.

This first-order parameter has dimension inverse mass. The quadratic heat-kernel parameter in I.2 has dimension inverse mass squared and carries $e^{-m_q^2T}$. They are different representations of the resolvent; their symbols and measures must not be interchanged.

## A variable momentum path and its ordering

For a path $P(t)$ on a finite interval, define
$$
U_T[P]=\mathcal P\exp\!\left[-\int_0^Tdt\,(m_q+i\gamma\cdot P(t))\right],
\qquad K_T[P]=\operatorname{tr}_{\mathrm{spin}}U_T[P].
$$
On a finite partition, later slices stand on the left. Scalar mass commutes with all spin matrices, so it factors exactly:
$$
K_T[P]=e^{-m_qT}\operatorname{tr}_{\mathrm{spin}}
\mathcal P\exp\!\left[-i\int_0^Tdt\,\gamma\cdot P(t)\right].
$$
Momentum insertions at different slices generally do not commute. The spin trace does not justify deleting the ordering before the product is assembled. The laboratory illustrates this with Pauli matrices.

The source denotes its boundary spin factor by $K[P]$. A complete use of that notation must specify the total-parameter integration, the measure, and the observable. A propagator uses a resolvent integral; a logarithmic determinant has a different proper-time weight, and current correlators include their vertex insertions. An upper limit of infinity inside an unevaluated evolution exponent is not a substitute for these choices.

## The constant-momentum checkpoint

For $p\ne0$,
$$
e^{-iT\gamma\cdot p}
=\cos(T|p|)1-i\frac{\gamma\cdot p}{|p|}\sin(T|p|).
$$
Integrating after multiplication by $e^{-m_qT}$ gives $m_q/(m_q^2+p^2)$ for the cosine coefficient and $|p|/(m_q^2+p^2)$ for the sine coefficient. This reproduces the matrix resolvent above.

With four Dirac components, its spin trace is $4m_q/(m_q^2+p^2)$, since $\operatorname{tr}\gamma_\mu=0$. That scalar trace still does not replace a matrix propagator between arbitrary current vertices.

## External insertions and momentum routing

If momenta $q_k$ enter at ordered locations $t_k$, define $Q(t)=\sum_kq_k\Theta(t-t_k)$. Total momentum conservation makes $Q$ periodic around the closed loop, up to its choice of base point.

The source writes the amplitude schematically as an integral involving $W[P+Q]K[P]$. This organization puts external jumps in one chosen loop argument. It is a routing convention within the representation, not a statement that physical spin propagation is insensitive to injected momentum. A change of integration variables moves the shift between factors; the measure and current insertions must change consistently.

A complete derivation should specify which correlator is being computed, its spin/color vertices, the finite-slice measure, normalization, and the parameter integration, then recover the free result. Separating labels into a gauge factor and a spin factor is not a proof of ultraviolet finiteness.

## What is established

The first-order free resolvent, scalar-mass factorization, constant-momentum exponential, and scalar slice below are explicit finite calculations. The full phase-space loop amplitude and its gauge-field separation remain regulated source constructions until the additional inputs are supplied.

## Worked laboratory: integrating one momentum slice

For a scalar nonrelativistic slice with $\Delta t>0$ and mass $M>0$,
$$
\int\frac{dp}{2\pi}
\exp\left[ip\,\Delta x-\frac{\Delta t}{2M}p^2\right]
=\sqrt{\frac{M}{2\pi\Delta t}}
\exp\left[-\frac{M(\Delta x)^2}{2\Delta t}\right].
$$
Complete the square by shifting $p$ by $iM\Delta x/\Delta t$ under the Gaussian integral. The resulting coordinate increment variance is $\Delta t/M$. Multiplying slices produces the coordinate path weight, with its normalization fixed at every step.

This is an exact finite-slice scalar calculation, not the full Dirac rim. For a matrix Hamiltonian, factors at successive slices must remain ordered. If $A=\sigma_1$ and $B=\sigma_2$, then $AB=i\sigma_3$ while $BA=-i\sigma_3$. The spin trace may remove some commutators in a special product, but it cannot justify erasing ordering before the product is assembled.

The quark mass, auxiliary surface-fermion mass, and slice parameter have distinct roles. Keep them separate when comparing this Gaussian example with the first-order Dirac phase-space formula in the source.

## Problem set

1. **Classroom core.** Find the variance for $M=2$ and $\Delta t=1/4$.

2. **Self-study calculation.** Integrate the displayed coordinate kernel over $\Delta x$.

3. **Self-study interpretation.** Does the scalar slice derive the full spin factor?

4. **Research extension.** Construct a two-slice spin and color example for IAS pp. 47–48.

## Answer checkpoints

1. It is $\Delta t/M=1/8$.

2. The Gaussian integral cancels the prefactor, giving one.

3. No. It verifies the Gaussian part and its normalization. The Dirac matrix insertions require their own ordered representation.

4. Completion: retain the order of every matrix, evaluate the finite product, and state what additional limit would recover the formal continuum expression.

## Teaching note

Use the decisive step in problem 2 as the written exit check for II.2; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-01-why-momentum-loop-space|Previous note]] · [[mini-lecture-03-factorization-of-the-momentum-loop-measure|Next note]] · [[geometric-qcd-course-guide|Course guide]]
