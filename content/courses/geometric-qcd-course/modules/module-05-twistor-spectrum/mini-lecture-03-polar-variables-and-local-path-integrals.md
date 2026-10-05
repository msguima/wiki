---
title: "Mini-Lecture V.3: Polar Variables and Local Path Integrals"
type: lecture-notes
course: geometric-qcd-course-guide
module: 5
lecture: "V.3"
modified: 2026-10-05
---

# Mini-Lecture V.3: Polar Variables and Local Path Integrals

*We study radial integration and the massless Dirac kernel. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** V.2; constrained Gaussian measures and Fourier transforms. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); radial integration and the massless Dirac kernel (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 118-123. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 5|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 118-123.

## The question

How can the spinor radial measure and the local momentum integral carry opposite scale weights? We calculate both in finite dimensions, retaining their constants and convergence prescriptions before making a functional interpretation.

## Radial variables and the constraint

A complex two-component spinor has four real components. Write $\lambda=u\xi$, $\mu=v\eta$, where $u,v>0$ and $\xi^\dagger\xi=\eta^\dagger\eta=1$. Flat measures give

$$
d^4\lambda\,d^4\mu
=u^3v^3\,du\,dv\,d\Omega_\xi\,d\Omega_\eta.
$$

Impose $\delta(u^2-v^2)$. On the positive half-line, $\delta(u^2-v^2)=\delta(v-u)/(2u)$, so integration over $v$ leaves $u^5du/2$ times the angular measure. Gauge-orbit factors must be treated separately as in V.2.

Set $\rho=2\log u$. Then $du=\frac12e^{\rho/2}d\rho$, and

$$
u^5du=\frac12e^{3\rho}d\rho.
$$

Thus the constrained pair measure contributes $e^{3\rho}d\rho/4$, up to angular and gauge normalization. The constant factors may cancel in normalized quantities, but the equality without the factor $1/2$ in $u^5du$ would be incorrect.

## The inverse Dirac operator needs a prescription

For Euclidean Hermitian gamma matrices,

$$
(i\gamma\cdot q)^{-1}=-\frac{i\gamma\cdot q}{q^2},
\qquad q\ne0.
$$

An undamped integral $\int_0^\infty ds\,e^{-si\gamma\cdot q}$ does not converge as an ordinary integral. Introduce $\epsilon>0$ first:

$$
\int_0^\infty ds\,e^{-s(\epsilon+i\gamma\cdot q)}
=(\epsilon+i\gamma\cdot q)^{-1}.
$$

The limit $\epsilon\downarrow0$ is taken with a specified distributional prescription. Zero momentum, zero modes, and coincident position require separate treatment.

## Worked Fourier transform

With the Fourier measure $d^4q/(2\pi)^4$, the massless scalar Green function is $G(\tau)=1/(4\pi^2\tau^2)$ away from $\tau=0$. Differentiating under the regulated Fourier integral gives

$$
I(\tau)=\int\frac{d^4q}{(2\pi)^4}
e^{iq\cdot\tau}(i\gamma\cdot q)^{-1}
=-\gamma\cdot\partial_\tau G(\tau)
=\frac{\gamma\cdot\tau}{2\pi^2(\tau^2)^2}.
$$

The derivative supplies $-2\tau_\mu/|\tau|^4$, which fixes the sign. In this convention there is no remaining factor of $i$ in the coordinate-space kernel. Other Fourier and gamma conventions must be translated before comparing source formulas.

Under $\tau\mapsto e^\rho\tau$, the numerator scales as $e^\rho$ and the denominator as $e^{4\rho}$, so $I(e^\rho\tau)=e^{-3\rho}I(\tau)$. This weight is independent of any special normalized spinor identity for $\tau^2$.

## What the cancellation establishes

The radial factor $e^{3\rho}$ and the local kernel factor $e^{-3\rho}$ cancel their scale weights. This is an exact homogeneity statement for the finite-dimensional factors above. It is not yet invariance of the full functional measure, determinant, regulator, or action. A product over infinitely many points can generate additional local terms when regulated.

## Worked laboratory: checking homogeneity without spinor identities

For $\tau=(r,0,0,0)$ with $r>0$, the coordinate kernel is $I(\tau)=\gamma_1/(2\pi^2r^3)$. Replacing $r$ by $2r$ divides it by eight. The spinor radial measure at $\rho\mapsto\rho+\log2$ gains a factor eight. Their product has zero local scale weight.

This test avoids a potentially convention-dependent identity for a normalized twistor bilinear. It checks exactly the homogeneity used in the local cancellation.

## What is established

The constrained radial measure, resolvent prescription, and noncoincident Fourier kernel are calculated explicitly. Their assembly into the full twistor measure remains conditional on the gauge fixing and geometric inputs of V.2 and Module III.

## Looking ahead

V.4 retains the scale-dependent action and derives its variation. Removing a radial weight does not remove the dynamics of the radial variable.

## Problem set

1. **Classroom core.** Transform $u^5du$ under $\rho=2\log u$.

2. **Self-study calculation.** Compute the kernel scale factor for $\rho=\log3$.

3. **Self-study interpretation.** Why is a damping prescription needed for the proper-time integral of $i\gamma\cdot q$?

4. **Research extension.** Keep the regulator through the local Fourier integration.

## Answer checkpoints

1. It becomes $\tfrac12e^{3\rho}d\rho$.

2. It is $e^{-3\log3}=1/27$.

3. Its eigenvalues are purely imaginary for real Euclidean momentum, so the undamped positive-time exponential does not decay.

4. Completion: specify the distributional limit, contact terms, normalization, and zero-mode handling. A pointwise noncoincident kernel alone is not the full functional measure.

## Teaching note

Use the decisive step in problem 2 as the written exit check for V.3; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-02-twistor-parametrization-of-the-measure|Previous note]] · [[mini-lecture-04-liouville-term-and-scale-cancellation|Next note]] · [[geometric-qcd-course-guide|Course guide]]
