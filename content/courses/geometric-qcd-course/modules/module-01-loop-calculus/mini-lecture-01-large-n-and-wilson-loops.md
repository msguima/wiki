---
title: "Mini-Lecture I.1: Large-Nc QCD and Wilson Loops"
type: lecture-notes
course: geometric-qcd-course-guide
module: 1
lecture: "I.1"
modified: 2026-10-05
---

# Mini-Lecture I.1: Large-$N_c$ QCD and Wilson Loops

*We study ribbon counting and normalized traces. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** matrix traces, gauge transformations, and the Gaussian integral bridge. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); ribbon counting and normalized traces (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked Source reconstruction explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 4-6. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 1|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 4-6.

## The question

Why are traced parallel transports natural observables of a gauge theory, and why does their large-color expansion suggest a surface description? We derive gauge invariance first, then count powers of color. The existence of a string representation is a further dynamical question.

## A Wilson line from parallel transport

Use a Hermitian gauge potential $A_\mu$, the anti-Hermitian connection $\mathcal A_\mu=igA_\mu$, and $D_\mu=\partial_\mu+\mathcal A_\mu$. A color vector along $x(s)$ is parallel when
$$
\frac{dw}{ds}=-\dot x^\mu\mathcal A_\mu(x(s))w.
$$
One small step gives $w(s+\Delta s)=[1-\Delta s\,\dot x^\mu\mathcal A_\mu+O(\Delta s^2)]w(s)$. Multiplication of successive steps puts later parameters on the left. The resulting transport is
$$
U(y,x)=\mathcal P\exp\!\left(-\int_x^y\mathcal A_\mu dz^\mu\right).
$$
The ordinary exponential of the matrix integral also exists, but generally does not solve this equation: it fails to retain the order of noncommuting insertions. I.3 checks the difference at second order.

Under $w(x)\mapsto S(x)w(x)$, covariance requires
$$
D_\mu\mapsto S D_\mu S^{-1},\qquad
\mathcal A_\mu\mapsto S\mathcal A_\mu S^{-1}+S\partial_\mu S^{-1}.
$$
It follows directly from the transport equation and its initial condition that $U(y,x)\mapsto S(y)U(y,x)S^{-1}(x)$.

For a closed contour based at $x$, the endpoints coincide. Cyclicity of the trace removes the conjugation, making
$$
w_C[A]=\frac1{N_c}\operatorname{tr}U_C[A],\qquad W[C]=\langle w_C[A]\rangle
$$
gauge invariant. The first expression is an observable in a specified background; the second includes the gauge-field expectation. They must not be interchanged when deriving the loop equation.

An open line is covariant at two endpoints. It can enter a gauge-invariant observable such as $\bar q(y)U(y,x)q(x)$. Thus closedness is sufficient for the traced-loop observable, rather than a prohibition on all gauge-invariant observables containing open transport.

The source writes a positive exponent using its ordered covariant-derivative convention. Signs, contour orientation, and ordering must be translated together. I.3 gives an explicit inverse-transport convention instead of simply dropping the sign in this equation.

## Color counting with one consistent action convention

Rescale the field so that the pure-gauge action has an overall factor $N_c/\lambda$, with $\lambda=g^2N_c$ held fixed. In this convention every propagator supplies $\lambda/N_c$, every interaction vertex supplies $N_c/\lambda$, and every closed color-index face supplies $N_c$. Cubic and quartic vertices both carry that common action prefactor; mixing this convention with canonical-field vertex rules would give incorrect powers.

For a connected vacuum ribbon graph,
$$
(N_c/\lambda)^V(\lambda/N_c)^E N_c^F
=N_c^{V-E+F}\lambda^{E-V}.
$$
The thickened graph is an orientable surface, so $V-E+F=2-2h$ for genus $h$. Consequently the color factor is $N_c^{2-2h}$ and each additional handle suppresses the graph by $N_c^{-2}$ at fixed coupling. Momentum integrals and symmetry factors are not determined by this topological counting.

With $b$ external trace boundaries the corresponding power before trace normalization is $N_c^{2-2h-b}$. Dividing each trace by $N_c$ gives
$$
N_c^{2-2h-2b}.
$$
A normalized single-trace disk has $(h,b)=(0,1)$ and is order one. A connected cylinder has $(h,b)=(0,2)$ and is order $N_c^{-2}$. The cylinder has no handle: its suppression relative to two disconnected disks comes from connectedness and the two boundary normalizations, not from genus one.

## Factorization and its scope

For two normalized loop observables in the usual topological expansion,
$$
W_2(C_1,C_2)=\langle w_{C_1}w_{C_2}\rangle,
\qquad
W_{2,c}=W_2-W[C_1]W[C_2]=O(N_c^{-2}).
$$
It is the full correlator that factorizes at leading order; the connected correlator is suppressed. This closes the leading Makeenko–Migdal splitting equation on a single-loop expectation, subject to its regulator and contact prescription.

The counting alone does not establish confinement, a mass gap, or a continuum string measure. It assumes the usual fixed-'t Hooft-coupling expansion and does not justify every nonperturbative exchange of limits.

## Why surfaces enter, and what remains to construct

Ribbon graphs provide a surface topology. Their dual graphs can be viewed as discretizations of a worldsheet, which motivates a possible representation
$$
W[C]=\int_{\partial X=C}\mathcal D X\,e^{-S_{\mathrm{eff}}[X]}.
$$
Matching a topology is only the beginning. Such a representation would need the correct weights, measure, boundary conditions, regularization, and observable dictionary. The source's geometric-QCD program proposes those additional structures; the following modules test its steps.

## The ultraviolet problem

A smooth Wilson loop can have regulator-dependent perimeter divergences. Corners add angle-dependent cusp divergences, and self-intersections require a contact and operator-mixing prescription. For example a logarithmic cusp term has the form $\log W\sim-\Gamma_{\mathrm{cusp}}(\gamma)\log(\Lambda_{\mathrm{UV}}L)$ in a stated regulator. Renormalization therefore changes how contour variations act.

I.7 calculates a local crossing logarithm and the derivative of an angle-dependent subtraction. That exposes a problem with a naive multiplicative prescription; it does not rule out every coordinate-space formulation.

Physical current correlators also integrate over trajectories rather than fixing one smooth contour. In the proper-time representation of I.2, Brownian paths have no ordinary tangent. A smooth-contour identity must therefore be regulated before it is used under that trajectory integral. Roughness motivates this care without proving nonanalytic dependence on every source.

## Worked laboratory: a color-counting example

Take a connected orientable ribbon graph with $V$ vertices, $E$ edges, $F$ color faces, genus $h$, and $b$ trace boundaries. In the rescaled action convention, vertices supply $N_c$, propagators supply $N_c^{-1}$, and closed color faces supply $N_c$. Its net color factor is $N_c^{V-E+F}=N_c^{2-2h-b}$ before normalizing external traces. The equality is Euler's formula for the thickened graph.

A disk has $(h,b)=(0,1)$ and contributes $N_c$ to one unnormalized trace, hence order one to $w_C=N_c^{-1}\operatorname{tr}U_C$. A connected cylinder has $(h,b)=(0,2)$ and contributes order one before normalization, hence $N_c^{-2}$ for two normalized traces. Two disconnected disks instead contribute $N_c^2/N_c^2=1$. This is the topological origin of the relative connected suppression.

For an exact finite check, let $U=\operatorname{diag}(e^{i\alpha},e^{-i\alpha})$. Its normalized trace is $\cos\alpha$; conjugation by any invertible matrix leaves the trace unchanged. Gauge invariance follows from conjugation at the base point, whereas large-$N_c$ factorization concerns an ensemble and its expansion. They are different statements.

The counting assumes the usual fixed-'t Hooft-coupling topological expansion. It does not make a continuum local algebra finite-dimensional or establish confinement.

## Problem set

1. **Classroom core.** Compute the normalized trace of $U$ at $\alpha=\pi/3$.

2. **Self-study calculation.** Compare two disconnected disks with a connected cylinder for normalized traces.

3. **Self-study interpretation.** Does trace conjugation invariance prove an area law?

4. **Research extension.** Use the primary 't Hooft reading to trace the counting for one ribbon graph with a handle.

## Answer checkpoints

1. It is $(e^{i\pi/3}+e^{-i\pi/3})/2=1/2$.

2. The disks contribute order one; the cylinder contributes $N_c^{-2}$. The cylinder has genus zero and two boundaries.

3. No. It proves gauge invariance of the observable. Area-law behavior is dynamical and depends on the state and regime.

4. Completion: draw the graph, identify $V,E,F,b$, verify the Euler characteristic, and exhibit the extra $N_c^{-2}$ relative to the corresponding planar topology. No confinement claim follows from this exercise.

## Teaching note

Use the decisive step in problem 2 as the written exit check for I.1; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-02-physical-amplitudes-and-brownian-loops|Next note]] · [[geometric-qcd-course-guide|Course guide]]

**Wiki connections.** [[wilson-loop|Wilson loop]] · [[large-n-factorization|large-N factorization]]
