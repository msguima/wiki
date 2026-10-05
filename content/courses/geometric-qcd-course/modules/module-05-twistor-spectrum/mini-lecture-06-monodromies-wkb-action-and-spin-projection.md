---
title: "Mini-Lecture V.6: Monodromies, WKB Action, and Spin Projection"
type: lecture-notes
course: geometric-qcd-course-guide
module: 5
lecture: "V.6"
modified: 2026-10-05
---

# Mini-Lecture V.6: Monodromies, WKB Action, and Spin Projection

*We study stationary phase, monodromy, and a regulated winding sum. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** V.5; stationary points and geometric series. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); stationary phase, monodromy, and a regulated winding sum (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 128-133. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 5|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 128-133.

## The question

Twistor monodromy suggests a spectral condition. We can calculate the finite monodromy, the stationary equations of the displayed phase, and a regulated winding sum. These calculations must be distinguished from a proof that all quantum corrections leave the spectrum unchanged.

## Monodromy and the rotation angle

For a spinor with components proportional to $z^a$ and $z^{-a}$, continuation once around $z=0$ gives

$$
M_a=\operatorname{diag}(e^{2\pi ia},e^{-2\pi ia}).
$$

An off-diagonal entry of a vector matrix $X$ transforms under $X\mapsto M_aXM_a^\dagger$ by $e^{4\pi ia}$. Thus the corresponding spatial rotation angle is $4\pi a$, reflecting the double cover from spinors to rotations. At $a=1/2$ the spinor changes sign but the vector returns to itself.

## A dimensionless stationary phase

Use the dimensionless variables of V.7: $\mathcal E=E/\sqrt\sigma$, $x=m/\sqrt\sigma$, and $K$ dimensionless. The source phase can be expressed as

$$
\Phi=2\pi\mathcal EK-\pi K^2F(\beta)
-4\pi xK\cos\beta-4\pi(J+q/2)
-\frac23(\tan\beta-\beta),
\qquad F(\beta)=\beta+\tfrac12\sin2\beta.
$$

All terms are dimensionless. The symbol for a dimensionful radius in an earlier source equation must not be substituted for $K$ without its accompanying powers of $\sigma$.

## Worked derivation of the parametric equations

Stationarity in $K$ gives

$$
0=\partial_K\Phi=2\pi\mathcal E-2\pi KF-4\pi x\cos\beta,
$$

or $\mathcal E=KF+2x\cos\beta$. Since $F'=2\cos^2\beta$, stationarity in $\beta$ gives

$$
-2\pi K^2\cos^2\beta+4\pi xK\sin\beta
-\frac23\tan^2\beta=0.
$$

For $0<\beta<\pi/2$, set $y=K\cos^2\beta/\sin\beta$. The last equation becomes

$$
y^2-2xy+\frac1{3\pi}=0.
$$

The source chooses the plus root $y=\bar x=x+\sqrt{x^2-1/(3\pi)}$. The discriminant gives the real-domain bound. The existence of the other root is algebraic; its physical selection requires the source's branch and stability conditions.

Finally substitute the energy equation into $\Phi=0$. The endpoint terms cancel, leaving

$$
J=\frac{K^2F}{4}-\frac{\tan\beta-\beta}{6\pi}-\frac q2.
$$

This reproduces the corrected V.7 parametrization. It is an exact stationary calculation within the proposed phase, not an independent derivation of that phase from QCD.

## Winding sums and order of limits

For $\epsilon>0$ the elementary regulated series is

$$
\sum_{k=1}^\infty e^{ikt-\epsilon k}
=\frac1{e^{\epsilon-it}-1}.
$$

Near $t=0$ its singular factor is $1/(\epsilon-it)$, but it also has periodic singularities as the regulator is removed. Integration ranges, projection, and the relation between $t$ and the on-shell phase determine what survives in an amplitude.

There is another instructive distinction:

$$
\int_{\mathbb R} da\,e^{ia\Phi}=2\pi\delta(\Phi),
\qquad
\int_0^\infty da\,e^{ia\Phi-\epsilon a}
=\frac1{\epsilon-i\Phi}.
$$

The domain and convergence prescription decide whether one obtains a delta distribution or a pole boundary value. A stationary condition alone does not specify this choice.

## Why a steep saddle is not an exact-WKB proof

For a nonsingular $d$-dimensional Gaussian Hessian, $\int d^d\xi\,e^{-k\xi^TH\xi/2}$ is proportional to $k^{-d/2}/\sqrt{\det H}$. Higher terms in the action generate corrections in inverse powers of $k$. An infinite-dimensional determinant additionally needs a regulator, boundary domain, and treatment of zero modes.

Linearity of a classical action in a monodromy parameter can impose $\Phi=0$ at a saddle. It does not alone derive an exact Bohr–Sommerfeld rule, eliminate every higher level, or show that fluctuations cannot shift the poles. The source acknowledges that a full transverse-Hessian analysis is needed. We retain exact WKB as conjectured within this construction.

## Worked laboratory: a finite Gaussian saddle

For $h>0$,
$$
\int_{\mathbb R}d\xi\,e^{-kh\xi^2/2}
=\sqrt{\frac{2\pi}{kh}}.
$$
If the action also contains $g\xi^4$, expansion of the exponential gives a relative first correction $-3g/(kh^2)$, because the Gaussian fourth moment is $3/(k^2h^2)$. The factor of $k$ multiplying the quartic action leaves an inverse-$k$ correction. A steep Hessian suppresses corrections in this model but does not make them vanish identically.

## What is established

The monodromy, stationary equations, and regulated geometric series are exact calculations. Their spectral interpretation requires an integration cycle, operator domain, and fluctuation analysis. The QCD identification also depends on the unresolved earlier geometric steps.

## Looking ahead

V.7 evaluates the resulting model and states precisely what a fit reproduction and a held-out prediction would test.

## Problem set

1. **Classroom core.** What is $M_a$ at $a=1/2$ and what does it do to a vector matrix?

2. **Self-study calculation.** Derive the quadratic equation for $y=K\cos^2\beta/\sin\beta$.

3. **Self-study interpretation.** Does the Gaussian prefactor prove exact WKB?

4. **Research extension.** Analyze the source's transverse Hessian near a branch-point saddle.

## Answer checkpoints

1. $M_a=-1_2$, so conjugation leaves the vector matrix unchanged.

2. Multiply $\partial_\beta\Phi=0$ by $\cos^2\beta/(2\pi\sin^2\beta)$ to obtain $-y^2+2xy-1/(3\pi)=0$.

3. No. Higher action terms, other saddles, zero modes, and the integration cycle can change the amplitude and spectral condition.

4. Completion: specify the operator domain, regulator, zero-mode removal, determinant and leading corrections, then test whether poles shift. The source's conjecture is not the premise to prove by assumption.

## Teaching note

Use the decisive step in problem 2 as the written exit check for V.6; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-05-minkowski-continuation-and-helicoids|Previous note]] · [[mini-lecture-07-regge-trajectories-and-fit-audit|Next note]] · [[geometric-qcd-course-guide|Course guide]]
