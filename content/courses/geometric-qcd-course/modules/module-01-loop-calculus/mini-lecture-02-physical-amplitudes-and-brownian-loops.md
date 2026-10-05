---
title: "Mini-Lecture I.2: Physical Amplitudes and Brownian Quark Loops"
type: lecture-notes
course: geometric-qcd-course-guide
module: 1
lecture: "I.2"
modified: 2026-10-05
---

# Mini-Lecture I.2: Physical Amplitudes and Brownian Quark Loops

*We study the proper-time resolvent and the Brownian bridge. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** Euclidean gamma algebra and Gaussian integrals. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); the proper-time resolvent and the Brownian bridge (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 5-6. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 1|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 5-6.

## The physical question

A prescribed Wilson contour is useful, but a quark current correlator integrates over particle trajectories. We need to understand why those trajectories carry a holonomy, how spin enters, and why a smooth contour is only a regulated approximation. The calculation below fixes the proper-time sign before introducing any path integral.

## Conventions and the resolvent

We use Euclidean Hermitian gamma matrices, an anti-Hermitian connection $\mathcal A_\mu$, and $D_\mu=\partial_\mu+\mathcal A_\mu$. Write $\mathcal F_{\mu\nu}=[D_\mu,D_\nu]$ and $\sigma_{\mu\nu}=[\gamma_\mu,\gamma_\nu]/2$. Then

$$
\not D^2=D^2+\frac12\sigma_{\mu\nu}\mathcal F_{\mu\nu}.
$$

Indeed, the symmetric gamma product gives $D^2$. Its antisymmetric part gives $[\gamma_\mu,\gamma_\nu][D_\mu,D_\nu]/4$. There is no extra factor of $i$ in $\mathcal F$; in the Hermitian-field convention $\mathcal A=igA$, it is already contained in $\mathcal F=igF$.

For a positive mass and an anti-self-adjoint regulated $\not D$, define $H=m^2-\not D^2$. Its eigenvalues are $m^2+\omega^2>0$, so

$$
(\not D+m)^{-1}=(m-\not D)H^{-1}
=(m-\not D)\int_0^\infty dT\,e^{-TH}.
$$

Multiplication by $\not D+m$ verifies this identity: $(\not D+m)(m-\not D)=H$. The integral is $H^{-1}$ because $-\partial_T e^{-TH}=He^{-TH}$ and the endpoint values are $1$ and $0$. If instead the denominator is written $\not D^2-m^2$, its proper-time integral has an overall minus sign. These two conventions cannot be mixed.

## From a Gaussian kernel to paths

In the free theory, Fourier transformation gives

$$
K_T(x,y)=\int\frac{d^4p}{(2\pi)^4}e^{ip\cdot(x-y)-Tp^2}
=\frac{e^{-|x-y|^2/(4T)}}{(4\pi T)^2}.
$$

Complete the square in each momentum component to obtain the last equality. The normalization follows by integrating over $x$: every one-dimensional Gaussian has variance $2T$ and unit integral. Insert $N-1$ position resolutions of the identity in $e^{T\partial^2}=(e^{\Delta T\partial^2})^N$, with $\Delta T=T/N$. The product of kernels is

$$
\prod_{j=1}^N(4\pi\Delta T)^{-2}
\exp\left[-\sum_{j=1}^N\frac{|x_j-x_{j-1}|^2}{4\Delta T}\right].
$$

This is the precise finite-slice meaning of the formal weight $\exp[-\int\dot x^2/4]$. A typical increment is of order $\sqrt{\Delta T}$, whereas its difference quotient is of order $(\Delta T)^{-1/2}$. Thus the continuum trajectory has no ordinary velocity.

For $D=\partial+\mathcal A$, parallel transport from $y$ to $x$ is $U(x,y)=\mathcal P\exp[-\int_y^x\mathcal A_\mu dx^\mu]$. A time-sliced heat kernel also inserts the matrix potential $\sigma\mathcal F/2$. Schematically its spin and color weight is one ordered exponential,

$$
\mathcal P\exp\int_0^T ds\left[-\dot x^\mu\mathcal A_\mu(x(s))
+\frac12\sigma_{\mu\nu}\mathcal F_{\mu\nu}(x(s))\right].
$$

The two terms generally fail to commute. Splitting this into independent Wilson and spin exponentials is unjustified unless the spin insertion is expressed in a parallel-transported frame with the corresponding ordering retained. A stochastic prescription and a regulator are needed for the Brownian integral; the finite-slice expression is the starting point.

## Closing the paths in a current correlator

For a flavor current, Wick contraction in a fixed background gives a connected term

$$
\langle J_\mu(x)J_\nu(y)\rangle_{\mathrm{conn}}
=-\left\langle\operatorname{tr}
[\gamma_\mu S(x,y;A)\gamma_\nu S(y,x;A)]\right\rangle_A .
$$

Two propagators close the trajectory. The minus sign here is the fermionic contraction sign. The trace includes spin and color, and the gauge average has not yet been evaluated. This explains why loop functionals enter amplitudes without asserting that a spin-dependent gauge average factors into a scalar $W[C]$ times an independent spin number.

If $v=\dot x$, an external insertion $e^{iq\cdot(x(s_2)-x(s_1))}$ becomes $e^{iq\cdot\int_{s_1}^{s_2}v\,ds}$. It does not involve $\int\dot v$. The slides use additional phase-space notation; II.2 treats that representation separately. A rescaling of proper time can change the coefficient $1/4$ to $1/2$, but then all mass and momentum factors must be rescaled together.

## Worked example: the free propagator and a Brownian bridge

At momentum $p$,

$$
S(p)=\frac{m-i\gamma\cdot p}{m^2+p^2},\qquad
(m+i\gamma\cdot p)S(p)=1.
$$

The second equality uses $(\gamma\cdot p)^2=p^2$ and cancels the cross terms. At $p^2=1$, $m=2$, the proper-time scalar integral is $1/5$. The inverse of $-p^2-m^2$ is $-1/5$, which detects the sign error without any gauge-field calculation.

For a closed Gaussian path of duration $T$, one coordinate of the bridge has covariance

$$
\langle x(s)x(t)\rangle=2\left(\min(s,t)-\frac{st}{T}\right).
$$

It vanishes at both endpoints and gives $\langle x(s)^2\rangle=2s(1-s/T)$. The bridge therefore fluctuates in the interior while closing exactly. This is the elementary model behind the closed-path measure.

> **Physical picture.** The loop in a quark amplitude is sampled by the propagator. Smooth test loops remain useful for defining geometry and variations, but the amplitude requires the regulated ensemble of rough paths and its spin weight.

## Worked laboratory: a smeared velocity

Although a Brownian bridge has no pointwise velocity, its finite increment is meaningful. From the covariance in the derivation,
$$
\operatorname{Var}[x(t)-x(s)]
=2(t-s)\left(1-\frac{t-s}{T}\right),\quad s<t.
$$
To obtain it, add the two variances and subtract twice the covariance. At $T=1$, $s=1/4$, $t=3/4$, the answer is $1/2$. Dividing by $(t-s)^2$ shows that the difference-quotient variance diverges as the interval shrinks. The integrated quantity remains finite. This is why a source coupled to an increment can be well defined even when a formal velocity at a point is not.

## What is established

The resolvent identity, free kernel, and bridge covariance are exact calculations. The non-Abelian worldline expression is a regulated formal representation; its continuum use requires a specified domain and renormalization. Roughness alone does not prove nonanalytic dependence on a smooth source: Gaussian characteristic functionals provide a counterexample, developed in II.7.

## Looking ahead

I.3 constructs holonomy by ordered transport. I.4 then uses small contour insertions to define the loop derivatives that enter the Schwinger–Dyson equation.

## Problem set

1. **Classroom core.** Evaluate $\int_0^\infty e^{-5T}\,dT$ and identify the sign of the inverse of $-5$.

2. **Self-study calculation.** Derive the bridge increment variance and evaluate it at the laboratory parameters.

3. **Self-study interpretation.** Can the color and spin terms always be split into two separately ordered exponentials?

4. **Research extension.** Compare the finite-slice heat kernel with the phase-space prescription on IAS pp. 47–48.

## Answer checkpoints

1. The integral is $1/5$; $(-5)^{-1}=-1/5$.

2. Use $C(t,t)+C(s,s)-2C(t,s)$ with $C(s,t)=2(\min(s,t)-st/T)$. The result is $1/2$.

3. No. Their matrix insertions generally do not commute. One needs common ordering or a parallel-transported interaction representation.

4. Completion: state the regulator, integration variables, ordering, and mass normalization, and recover the free propagator before drawing conclusions about interacting amplitudes.

## Teaching note

Use the decisive step in problem 2 as the written exit check for I.2; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-01-large-n-and-wilson-loops|Previous note]] · [[mini-lecture-03-holonomy-and-parallel-transport|Next note]] · [[geometric-qcd-course-guide|Course guide]]
