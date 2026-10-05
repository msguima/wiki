---
title: "Mini-Lecture II.7: Nonanalytic Vacuum and Q&A Boundaries"
type: lecture-notes
course: geometric-qcd-course-guide
module: 2
lecture: "II.7"
modified: 2026-10-05
---

# Mini-Lecture II.7: Nonanalytic Vacuum and Q&A Boundaries

*We study Gaussian analyticity and the free-word representation. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** II.6; Hilbert-space bases and adjoints. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); Gaussian analyticity and the free-word representation (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 59-65. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 2|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 59-65.

## The question

The momentum-loop ansatz raises two different questions: can the relevant functional be expanded near a reference loop, and what operator representation could realize it? We study a Gaussian functional and a free-word representation to avoid drawing unsupported conclusions from path roughness or infinite dimension.

## Rough paths can have analytic source dependence

Let $X$ be a centered Gaussian variable of variance $v$. Completing the square gives

$$
\langle e^{itX}\rangle=e^{-vt^2/2}.
$$

Its Taylor series converges for every finite complex $t$. For a Gaussian generalized field $\xi$ and an admissible test function $j$, the same argument gives

$$
\left\langle e^{i\xi(j)}\right\rangle
=\exp[-\langle j,Qj\rangle/2].
$$

White noise has no pointwise values, but this characteristic functional is analytic along every admissible finite source direction with finite covariance. Consequently divergent pointwise velocities of Brownian paths do not alone prove nonanalyticity of a smeared loop functional.

To establish nonanalyticity one needs a topology on the source space and a failure of differentiability or convergence there. For example, the ordinary function $e^{-|t|}$ fails to be differentiable at $t=0$; its cusp is a directly demonstrable obstruction. Such a calculation has not been supplied for the complete QCD loop measure.

## Free words and creation operators

Let $\mathcal H$ have an orthonormal basis consisting of the empty word $|\varnothing\rangle$ and all finite words $|i_1\cdots i_n\rangle$ in $d$ letters. Define the left creation operator by

$$
a_i^\dagger|w\rangle=|iw\rangle,
$$

and its adjoint by $a_i|\varnothing\rangle=0$, $a_i|jw\rangle=\delta_{ij}|w\rangle$. Applying their product to every basis vector proves

$$
a_i a_j^\dagger=\delta_{ij}1,\qquad
\sum_{i=1}^d a_i^\dagger a_i=1-|\varnothing\rangle\langle\varnothing|.
$$

This is the full Fock-space, or Toeplitz–Cuntz, representation. The second relation differs from the Cuntz quotient by the vacuum projection; terminology must respect that distinction.

Creation operators do not commute:

$$
a_1^\dagger a_2^\dagger|\varnothing\rangle=|12\rangle,\qquad
a_2^\dagger a_1^\dagger|\varnothing\rangle=|21\rangle.
$$

The two vectors are orthogonal, so their difference has squared norm two. The number operator is separately defined by $N|w\rangle=|w|\,|w\rangle$; it is not $\sum_i a_i^\dagger a_i$.

## A finite representation obstruction

Suppose $d\ge2$ and all $a_i$ were square finite matrices obeying $a_i a_i^\dagger=1$. Then each $a_i$ is invertible, with inverse $a_i^\dagger$. But $a_1a_2^\dagger=0$ would imply $a_2^\dagger=0$, contradicting $a_2a_2^\dagger=1$. Thus these relations have no nontrivial square finite-matrix realization.

This proves a representation statement. It does not prove that every finite-matrix approximation to a master field is useless or that the physical loop functional must be nonanalytic.

## States, traces, and Cayley–Hamilton

The vacuum state $\omega(B)=\langle\varnothing|B|\varnothing\rangle$ is normalized. It is not tracial: $\omega(a_i a_i^\dagger)=1$ but $\omega(a_i^\dagger a_i)=0$. An ordinary Hilbert-space trace of the identity is infinite. A source formula using a trace must therefore specify a different state, a tracial construction, or a regulator before it can be evaluated.

Cayley–Hamilton says that powers of a finite matrix reduce to a finite basis. It does not truncate its exponential as a Taylor polynomial. For $X=\operatorname{diag}(1,-1)$, $X^2=1$, but

$$
e^{tX}=\cosh t\,1+\sinh t\,X,
$$

which contains all orders in $t$. This distinction prevents an erroneous argument for nonanalyticity.

## Worked laboratory: the vacuum is a state, not a trace

For one creation operator, $\|a_i^\dagger|\varnothing\rangle\|^2=1$. Therefore $\omega(a_i a_i^\dagger)=1$. But $a_i|\varnothing\rangle=0$, so $\omega(a_i^\dagger a_i)=0$. This single pair of products disproves traciality.

For a word of length two, $\sum_i a_i^\dagger a_i$ returns the same word once, whereas the number operator returns twice the word. Thus the projection onto nonempty words and the length operator differ even on elementary basis states.

## What is established

The Gaussian example, free-word relations, finite-matrix obstruction, and exponential reduction are exact calculations. Whether a particular master-field construction yields the source's continuum QCD functional is a separate research question.

## Looking ahead

Module III introduces a proposed geometric replacement. Its merit must be tested through its explicit constraints and loop equation, not inferred solely from the limitations of the previous ansatz.

## Problem set

1. **Classroom core.** Compute $\|\,|12\rangle-|21\rangle\,\|^2$.

2. **Self-study calculation.** Derive $e^{tX}$ for $X^2=1$ by separating even and odd powers.

3. **Self-study interpretation.** Why does white-noise roughness not prove nonanalytic source dependence?

4. **Research extension.** Specify the state and topology in a proposed master-field representation.

## Answer checkpoints

1. It equals two, because the distinct word states are orthonormal.

2. The even powers sum to $\cosh t\,1$ and the odd powers to $\sinh t\,X$.

3. For admissible smeared sources the Gaussian characteristic functional is an exponential of a finite quadratic form.

4. Completion: identify the operator algebra, normalized state, trace status, allowed sources, and one correlation function. Any nonanalyticity claim must be tested in that stated source topology.

## Teaching note

Use the decisive step in problem 2 as the written exit check for II.7; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-06-breakdown-at-eighth-order|Previous note]] · [[mini-lecture-01-why-four-dimensional-geometry-enters|Next note]] · [[geometric-qcd-course-guide|Course guide]]
