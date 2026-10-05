---
title: "Mini-Lecture II.6: Breakdown at W⁽⁸⁾"
type: lecture-notes
course: geometric-qcd-course-guide
module: 2
lecture: "II.6"
modified: 2026-10-05
---

# Mini-Lecture II.6: Breakdown at $W^{(8)}$

*We study an inconsistency certificate rather than a count. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** II.5; row and column spaces. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); an inconsistency certificate rather than a count (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 56-58. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 2|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 56-58.

## The question

When does failure of an algebraic ansatz imply a mathematical obstruction? More equations than unknowns is insufficient. The decisive issue is whether the source vector belongs to the image of the coefficient matrix.

## Exact consistency and a certificate

For $Ax=b$ over the rationals or reals, a solution exists precisely when

$$
\operatorname{rank}A=\operatorname{rank}[A\mid b].
$$

To see this, the columns of $A$ span all attainable right-hand sides. Adding $b$ raises the rank exactly when $b$ lies outside that span. Equivalently, inconsistency can be demonstrated by a row vector $y^T$ satisfying

$$
y^TA=0,\qquad y^Tb\ne0.
$$

If $Ax=b$ existed, multiplication by $y^T$ would give $0=y^Tb$, a contradiction. This is a small, independently checkable certificate; it is stronger evidence than a solver message or a count.

## Worked calculation

Take

$$
A=\begin{pmatrix}1&1\\2&2\\1&-1\end{pmatrix}.
$$

For $b=(1,2,0)^T$, the first and third equations give $x_1=x_2=1/2$, and the second is satisfied. Three equations in two unknowns are consistent.

For $\widetilde b=(1,3,0)^T$, take $y=(-2,1,0)^T$. Direct multiplication gives $y^TA=(0,0)$ and $y^T\widetilde b=1$. The obstruction is now certified. Row reduction gives a third pivot in $[A\mid\widetilde b]$, whereas $A$ has two pivots.

Floating-point near-zero singular values require a tolerance and a stability analysis. When entries are rational, exact row reduction avoids that ambiguity. Large matrices can also be tested modulo several primes, but modular rank evidence requires careful reconstruction before claiming an exact rational certificate.

## Applying this standard to the reported eighth-order failure

The IAS slides report a failure at $W^{(8)}$. Part II, Appendix C, supplies a rank table: at eighth order it reports 379 equations, 212 unknowns, rank 82, and an augmented-rank increase of one. These are source-reported diagnostics. The matrix and certificate have not been independently reproduced in this course.

The report would establish inconsistency of the specified finite system if its construction and ranks are verified. It would not by itself prove that every one-dimensional loop representation fails, that all analytic functionals are excluded, or that one particular replacement geometry is unique. Those conclusions require an exhaustive ansatz and an argument connecting it to the proposed continuum solution.

## Why vector equations carry more information

If $E_\nu=0$ is a vector equation, contracting with a fixed vector $v_\nu$ gives one scalar equation. In two dimensions take $v=(1,0)$ and $E=(0,1)$: $v\cdot E=0$ although $E\ne0$. This illustrates information loss under contraction. It does not establish that the uncontracted equations are independent, nor does multiplying a scalar count by four compute a matrix rank.

## Source-audit protocol

Start with the source notebook linked in the bibliography and freeze its version. Export the matrices at orders four and six first, retaining lower-order free parameters. Check residuals and dimensions there before approaching order eight. At eighth order, provide either an exact augmented-rank calculation with preserved inputs or an explicit left-null witness. Then document exactly which cyclic, shuffle, parity, and dimension identities were imposed.

Completion is a reproducible finite-system result with a statement of its ansatz. Reproducing only the table's dimensions is a preliminary check. A negative result for that ansatz remains useful even when no uniqueness conclusion follows.

## Worked laboratory: changing only the source vector

For the matrix in the derivation, the vector $y=(-2,1,0)$ annihilates every column. Consequently every compatible source must obey $b_2=2b_1$. The third entry is unconstrained by this witness and determines the difference $x_1-x_2$. This explicitly describes the image of the matrix: a plane in $\mathbb R^3$. Moving from $(1,2,0)$ to $(1,3,0)$ leaves that plane.

## What is established

The rank criterion, certificate, and vector counterexample are proved here. The eighth-order obstruction is a reported calculation, not a calculation newly certified by these notes.

## Looking ahead

II.7 studies possible nonanalytic behavior and infinite-dimensional representations without turning a failed finite ansatz into a proof of either.

## Problem set

1. **Classroom core.** Compute $y^T(1,3,0)^T$.

2. **Self-study calculation.** Solve the compatible system for source $(1,2,2)^T$.

3. **Self-study interpretation.** What additional claim is needed to exclude every analytic representation?

4. **Research extension.** Extract an exact left-null certificate for the reported eighth-order system.

## Answer checkpoints

1. It is $-2+3=1$, certifying inconsistency.

2. $x_1+x_2=1$ and $x_1-x_2=2$ give $(3/2,-1/2)$.

3. That the chosen finite ansatz and all constraints exhaust the relevant analytic class. A rank failure in one specified ansatz is narrower.

4. Completion: preserve the matrix, source, basis map, and a rational $y$ with $y^TA=0$ and $y^Tb\ne0$. If those inputs are unavailable, report the missing inputs; the published rank table alone is not an independent certificate.

## Teaching note

Use the decisive step in problem 2 as the written exit check for II.6; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-05-low-order-algebraic-solutions|Previous note]] · [[mini-lecture-07-nonanalytic-vacuum-and-q-and-a|Next note]] · [[geometric-qcd-course-guide|Course guide]]
