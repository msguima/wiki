---
title: "Mini-Lecture IV.2: Curved Surfaces, Spinors, and Anomalies"
type: lecture-notes
course: geometric-qcd-course-guide
module: 4
lecture: "IV.2"
modified: 2026-10-05
---

# Mini-Lecture IV.2: Curved Surfaces, Spinors, and Anomalies

*We study spin connection, Weyl weights, and the anomaly boundary. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** IV.1; differential forms and integration by parts. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); spin connection, Weyl weights, and the anomaly boundary (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 96-98. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 4|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 96-98.

## The question

How does a two-dimensional spinor respond to a conformal metric, and what must be checked before a conformal factor can be called a gauge variable? We derive the local geometry explicitly, then separate classical covariance from the determinant anomaly and the model's proposed cancellation.

## Zweibein and connection

Take $ds^2=e^{2\rho}(du^2+dv^2)$, coframe $e^1=e^\rho du$, $e^2=e^\rho dv$, and $\epsilon_{12}=1$. The inverse frame is $e_a{}^k=e^{-\rho}\delta_a{}^k$. These two objects must not be interchanged.

Write $\omega=\omega^1{}_2=-\omega^2{}_1$. The torsion-free equations are

$$
de^1+\omega\wedge e^2=0,\qquad
de^2-\omega\wedge e^1=0.
$$

The first equation gives $-\rho_v+\omega_u=0$ and the second $\rho_u+\omega_v=0$. Thus

$$
\omega_u=\rho_v,\qquad\omega_v=-\rho_u.
$$

With Pauli matrices and spinor derivative $\nabla_k=\partial_k+i\omega_k\sigma_3/2$, we find

$$
D_\rho=e^{-\rho}\sigma^k\left(\partial_k+\frac12\partial_k\rho\right)
=e^{-3\rho/2}D_0e^{+\rho/2}.
$$

The last equality follows by applying both sides to a test spinor and differentiating the exponential. The sign of the right multiplier is positive. For constant $\rho=c$, it reduces to $D_\rho=e^{-c}D_0$, as required by the inverse frame. A formula with two negative multipliers would instead scale as $e^{-2c}$ and fails this check.

## Curvature and a local example

Since $d\omega=-(\rho_{uu}+\rho_{vv})du\wedge dv$, our curvature convention gives

$$
R=-2e^{-2\rho}(\rho_{uu}+\rho_{vv}).
$$

For $\rho=\alpha(u^2+v^2)$, $\Delta\rho=4\alpha$, so $R=-8\alpha e^{-2\alpha(u^2+v^2)}$. At the origin the sign is negative for positive $\alpha$. This is a direct model calculation, not an assumption that every worldsheet has this curvature.

## Classical Weyl weights and the mass

Under $\rho\mapsto\rho+\omega$, the massless action $\int d^2x\sqrt g\,\bar\psi D_\rho\psi$ is invariant if $\psi,\bar\psi$ each scale by $e^{-\omega/2}$. The measure contributes $e^{2\omega}$ and the Dirac transformation supplies the compensating weights. A constant physical mass term transforms with a remaining $e^\omega$:

$$
\int d^2x\sqrt g\,m\bar\psi\psi
\longmapsto\int d^2x\sqrt g\,m e^\omega\bar\psi\psi.
$$

It is not Weyl invariant unless the mass is also treated as a spurion of weight $-1$. The source uses an additional geometric density, denoted $e$. It must be distinguished from $\sqrt g=e^{2\rho}$.

If the mass profile is $m\sqrt e$ in flat coordinates and is to become the constant $m$ at $\rho=\log\sqrt e$, the covariant profile consistent with these endpoints is $M_\rho=m\sqrt e\,e^{-\rho}$. Substituting either endpoint verifies this statement. The printed source action and its claimed gauge equivalence therefore need a convention and normalization audit; copying a factor while discarding $\sqrt e$ is not a valid derivation.

## Quantum measure and the anomaly

Even in the massless theory, the determinant requires regularization. Its conformal variation contains a curvature term and, for a surface with boundary, boundary terms determined by the boundary condition. A single real Majorana field has half the determinant degrees of freedom of a complex Dirac field. Multiplicities, chiral sectors, zero modes, boundary conditions, and the definition of the effective action all matter for the coefficient.

To verify a proposed cancellation, write the regulated determinant variation and the variation of the counterterm in the same convention. Match bulk and boundary terms separately, including finite normalization conditions. Merely mentioning Pauli–Villars regularization does not establish cancellation.

For a simple compactly supported conformal perturbation, consider

$$
S_L[\rho]=c_L\int d^2x\,|\nabla\rho|^2.
$$

Integration by parts gives $\delta S_L=-2c_L\int\delta\rho\,\Delta\rho$. Since $\sqrt gR=-2\Delta\rho$, this is $c_L\int\sqrt gR\,\delta\rho$. This exact variation tells us which coefficient the determinant must supply with the opposite sign. A boundary adds $2c_L\int_{\partial D}\delta\rho\,\partial_n\rho$ and cannot be ignored without a boundary condition.

## Worked laboratory: a constant Weyl rescaling

For $\rho=c$ constant, the spin connection vanishes and the inverse frame multiplies $D_0$ by $e^{-c}$. The transformation $e^{-3c/2}D_0e^{c/2}$ has exactly that weight. At $c=\log2$, all eigenvalues of the massless Dirac operator on a correspondingly rescaled compact geometry scale by $1/2$, subject to the mapped boundary domain.

A constant physical mass does not scale with those eigenvalues unless it is transformed as a spurion. This is a simple diagnostic for an alleged equality between massive determinants in two conformal gauges.

## What is established

The connection, Dirac transformation, curvature, mass weights, and counterterm variation are derived here. The source's full massive determinant, boundary terms, and cancellation are stated only as a proposed construction. In particular, $\rho$-independence is not a generic property of a massive Majorana determinant.

## Looking ahead

IV.3 develops determinants and Pfaffians in finite dimensions, where their normalization and connected-loop interpretation can be checked without a continuum regulator.

## Problem set

1. **Classroom core.** Find $D_\rho/D_0$ for constant $\rho=\log2$.

2. **Self-study calculation.** Derive the boundary contribution in $\delta S_L$.

3. **Self-study interpretation.** Why does a bulk central-charge coefficient not settle the full cancellation?

4. **Research extension.** Audit the source's conformal action on pp. 94–98.

## Answer checkpoints

1. The scale factor is $1/2$.

2. Integration by parts gives $2c_L\int_{\partial D}\delta\rho\,\partial_n\rho$ in addition to $-2c_L\int_D\delta\rho\Delta\rho$.

3. Boundary terms, multiplicities, zero modes, mass transformation, and finite normalization also enter the regulated determinant.

4. Completion: check both proposed gauge endpoints and the constant-Weyl test, and match every bulk and boundary variation in one convention. Record any discrepancy instead of identifying unlike mass profiles.

## Teaching note

Use the decisive step in problem 2 as the written exit check for IV.2; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-01-majorana-fields-on-a-surface|Previous note]] · [[mini-lecture-03-determinants-as-loop-sums|Next note]] · [[geometric-qcd-course-guide|Course guide]]
