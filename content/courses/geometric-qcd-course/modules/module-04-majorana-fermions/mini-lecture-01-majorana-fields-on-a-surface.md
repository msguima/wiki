---
title: "Mini-Lecture IV.1: Majorana Fields on a Surface"
type: lecture-notes
course: geometric-qcd-course-guide
module: 4
lecture: "IV.1"
modified: 2026-10-05
---

# Mini-Lecture IV.1: Majorana Fields on a Surface

*We study Majorana quadratic forms and boundary projectors. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** III.5; the Grassmann bridge. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); Majorana quadratic forms and boundary projectors (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 92-96. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 4|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 92-96.

## The question

Before using a surface fermion determinant as a Wilson functional, we must specify its fields, quadratic operator, boundary domain, and normalization. This lecture builds those ingredients in a finite model and identifies the additional inputs in the IAS proposal.

## Majorana fields and the quadratic form

For real Grassmann components $\psi$, a quadratic action has the form

$$
S[\psi]=\frac12\psi^TA\psi,\qquad A^T=-A.
$$

The symmetric part of a matrix drops out because $\psi_i\psi_j=-\psi_j\psi_i$. In the continuum $A$ includes a charge-conjugation matrix, a Dirac operator, its mass profile, and its boundary domain. A Majorana integral is a Pfaffian; IV.3 derives the relation to a determinant. In Euclidean signature the reality condition and independent integration variables must be declared, rather than inferred from a Lorentzian phrase such as “its own antiparticle.”

The source uses two labels $\lambda=\pm1$ and a flat-coordinate mass profile $M(\xi)=m\sqrt{e(\xi)}$, where $e$ is a geometric density. In the source's schematic notation,

$$
A_0=\int d^2\xi\,
\left[\bar\psi_\lambda\sigma^k\partial_k\psi_\lambda+
m\sqrt e\,\bar\psi_\lambda\psi_\lambda\right].
$$

The integral covers both terms. The normalization relative to a real Majorana action depends on the independent components and charge-conjugation convention. The auxiliary mass $m$ in this module is distinct from the physical quark endpoint mass used in Module V.

## Boundary projector

The displayed source condition is $\sigma_3\psi_\lambda=\lambda\psi_\lambda$. Define $P_\lambda=(1+\lambda\sigma_3)/2$. Since $\sigma_3^2=1$,

$$
P_\lambda^2=P_\lambda,\qquad P_+P_-=0,\qquad
P_++P_-=1.
$$

For $\sigma_3=\operatorname{diag}(1,-1)$, $P_+$ retains the first spinor component and $P_-$ the second. This is an exact projector calculation.

A boundary condition also has to make the differential operator well defined. Integration by parts for a Dirac operator produces a boundary pairing proportional to $\int_{\partial\Sigma}\bar\psi\,\gamma^n\phi$. Its vanishing on the chosen domain, together with the appropriate ellipticity or self-adjointness requirement, must be checked. The displayed algebraic projector alone does not prove all those properties for an arbitrary curved boundary.

Nor does it prove that boundary states are occupied or that a classical repulsive force acts on paths. Those are interpretations of the proposed fermionic construction, not consequences of $P_\lambda^2=P_\lambda$.

## Worked two-component model

Take $A=\begin{pmatrix}0&m\\-m&0\end{pmatrix}$. The only surviving top-degree Grassmann term in the Gaussian integral is proportional to $m\psi_1\psi_2$, so the Pfaffian is $m$ after fixing the measure orientation. The determinant is $m^2$. At $m=0$ the inverse fails and the integral vanishes: zero modes affect normalization and cannot be hidden in a constant prefactor.

This elementary example explains why “large mass kills loops” does not determine the absolute determinant: the finite determinant here grows with $m$. A renormalized determinant can have a different limit only after its normalization is specified.

## Conformal geometry and the proposed invariance

A local metric can be written $g_{ab}=e^{2\rho}\delta_{ab}$ in conformal coordinates. This geometric statement does not make a massive determinant independent of $\rho$. IV.2 derives the spin connection, classical mass weights, and the variation that an anomaly counterterm would need to cancel.

The IAS claim that one may switch between flat and induced-metric gauges is used only conditionally until the massive operator, regulator, boundary terms, and multiplicities have been matched. The geometric surface supplying the density $e$ also retains the consistency problem demonstrated in III.5.

## Worked laboratory: one boundary component

For $\psi=(z_1,z_2)^T$, the condition $\sigma_3\psi=+\psi$ gives $z_2=0$ and leaves $z_1$ free. The complementary condition gives $z_1=0$. Algebraically, each projector has rank one.

For an operator domain this counting is only the first step. The boundary pairing depends on the normal matrix $\gamma^n$ and on the conjugate fields. It must vanish for every pair of allowed boundary values, not merely for a chosen sample vector.

## What is established

The antisymmetry of the quadratic form, projector identities, and finite Pfaffian are exact. The proposed surface theory is a source construction with its continuum domain and conformal equivalence still to be established.

## Looking ahead

IV.2 supplies the local spin geometry. IV.3 then shows exactly which loop sums belong to the logarithm of the partition function.

## Problem set

1. **Classroom core.** Write $P_+$ and $P_-$ as matrices.

2. **Self-study calculation.** Compute the determinant and Pfaffian of the two-component mass matrix.

3. **Self-study interpretation.** Does taking $m\to\infty$ force this determinant to zero?

4. **Research extension.** Specify a continuum boundary domain for the source operator.

## Answer checkpoints

1. They are $\operatorname{diag}(1,0)$ and $\operatorname{diag}(0,1)$.

2. They are $m^2$ and $m$, respectively, with the stated Pfaffian orientation.

3. No. This determinant grows as $m^2$. A renormalized limit depends on normalization and counterterms.

4. Completion: write the quadratic form, reality convention, boundary pairing, and the condition that removes its boundary term; distinguish that check from an ellipticity or spectral proof.

## Teaching note

Use the decisive step in problem 2 as the written exit check for IV.1; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-07-ope-matching-and-regge-physics|Previous note]] · [[mini-lecture-02-curved-surfaces-spinors-and-anomalies|Next note]] · [[geometric-qcd-course-guide|Course guide]]
