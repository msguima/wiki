---
title: "Mini-Lecture IV.3: Determinants as Loop Sums"
type: lecture-notes
course: geometric-qcd-course-guide
module: 4
lecture: "IV.3"
modified: 2026-10-05
---

# Mini-Lecture IV.3: Determinants as Loop Sums

*We study Pfaffians and connected versus disconnected loops. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** IV.1–IV.2; finite determinants and Grassmann integration. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); Pfaffians and connected versus disconnected loops (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 99-100. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 4|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 99-100.

## The question

Which object sums connected fermion loops: a determinant, its logarithm, or a Pfaffian? We begin with finite Grassmann integrals so that the combinatorics is explicit before applying the idea to a surface.

## Gaussian integrals

For independent complex Grassmann variables and a fixed integration orientation,

$$
\int \prod_i d\bar\psi_i\,d\psi_i\,
e^{-\bar\psi M\psi}=\det M.
$$

Only the term containing every Grassmann variable survives. Its alternating permutation sum is the determinant. For $2n$ real Grassmann variables with an antisymmetric matrix $A$, the corresponding Gaussian is $\operatorname{Pf}A$, with the measure sign fixed consistently, and $(\operatorname{Pf}A)^2=\det A$.

For two real variables, $A=\begin{pmatrix}0&a\\-a&0\end{pmatrix}$ has Pfaffian $a$ and determinant $a^2$. The sign of the Pfaffian is extra information; choosing a square root of a determinant without a prescription loses it.

A positive complex bosonic Gaussian gives a constant times $(\det M)^{-1}$; a real Gaussian gives $(\det M)^{-1/2}$. Neither is a permanent. The difference between bosonic and fermionic contractions does not change these Gaussian identities.

## Connected loops from a trace logarithm

Let $M=1-H$, with spectral radius less than one. Diagonalization, or the convergent power series for the logarithm, gives

$$
\log\det(1-H)=\operatorname{Tr}\log(1-H)
=-\sum_{n=1}^\infty\frac{\operatorname{Tr}H^n}{n}.
$$

The trace sums closed walks of length $n$ through matrix indices. The factor $1/n$ removes the choice of starting point around a rooted walk, with the series itself supplying the correct multiplicities. Exponentiating generates collections of connected loops:

$$
\det(1-H)=
\exp\left[-\sum_{n\ge1}\frac{\operatorname{Tr}H^n}{n}\right].
$$

A Majorana theory contributes a Pfaffian; formally its logarithm is half the trace logarithm of the antisymmetric operator, with its phase or sign tracked separately. Thus a single-loop sum belongs to a logarithm, while the partition function includes disconnected collections.

## Worked example: two sites

Take $H=\begin{pmatrix}0&t\\t&0\end{pmatrix}$. Odd traces vanish and $\operatorname{Tr}H^{2k}=2t^{2k}$. Therefore

$$
\log\det(1-H)=-\sum_{k\ge1}\frac{t^{2k}}k
=\log(1-t^2),\qquad \det(1-H)=1-t^2.
$$

The infinitely many connected repeated walks exponentiate to the finite determinant. At $t=1/2$, the determinant is $3/4$, whereas the first connected term alone is $-1/4$. Confusing these quantities would change even the normalization of a proposed loop functional.

## Spin transport and crossings

A spinor acquires a minus sign under a $2\pi$ frame rotation. For an immersed planar closed curve, the total tangent rotation is $2\pi w$ with integer turning number $w$, and the spin phase is $(-1)^w$. A simple oriented circle has $w=\pm1$; a standard figure-eight has $w=0$.

This relative sign motivates the source's crossing cancellation. On a curved surface, spin connection holonomy, curvature, spin structure, and boundary conditions also enter. Gauss–Bonnet includes bulk curvature and boundary turning; it is not a general formula identifying the complete holonomy solely with the number of crossings on every surface with holes.

Likewise $e^{-m\ell}$ is the leading length-dependent suppression in an appropriate large-mass saddle. It is not the exact full continuum worldline weight: fluctuation determinants, spin transport, proper-time integration, and regulators remain.

## Worked laboratory: a four-variable Pfaffian

For an antisymmetric $4\times4$ matrix with independent entries $A_{12}=a$, $A_{13}=b$, $A_{14}=c$, $A_{23}=d$, $A_{24}=e$, $A_{34}=f$, the three pairings give
$$
\operatorname{Pf}A=af-be+cd.
$$
The relative signs are the permutation parities needed to put the four Grassmann variables in the chosen order. With $(a,b,c,d,e,f)=(1,2,3,4,5,6)$ the result is $6-10+12=8$, and the determinant is $64$. This is a finite check of the pairing signs used in a Majorana Gaussian.

## What is established

The Gaussian identities and two-site loop expansion are exact finite calculations. The passage to the source's surface determinant is formal and requires the analytic and geometric inputs stated in IV.1–IV.2. A claimed cancellation of all nonplanar configurations needs a weight-preserving pairing of the full regulated configurations, examined next.

## Looking ahead

IV.4 uses an elementary Grassmann cancellation to teach the local mechanism while keeping the global planarity claim separate.

## Problem set

1. **Classroom core.** Evaluate the displayed Pfaffian for the supplied entries.

2. **Self-study calculation.** Use the two-site model to distinguish $\det(1-H)$ from $\log\det(1-H)$ at $t=1/2$.

3. **Self-study interpretation.** What Gaussian quantity do bosons produce?

4. **Research extension.** Translate the source loop sum into a regulated determinant or Pfaffian.

## Answer checkpoints

1. It is $8$.

2. The determinant is $3/4$; its logarithm is $\log(3/4)$. The first connected term alone is $-1/4$.

3. An inverse determinant for a complex Gaussian, or an inverse square root for a real Gaussian, up to normalization; not a permanent.

4. Completion: specify whether each sum is connected, its symmetry factors, spin holonomy, and normalization. Verify the relation first on a finite graph.

## Teaching note

Use the decisive step in problem 2 as the written exit check for IV.3; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-02-curved-surfaces-spinors-and-anomalies|Previous note]] · [[mini-lecture-04-pauli-cancellation-and-planarity|Next note]] · [[geometric-qcd-course-guide|Course guide]]
