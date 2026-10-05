---
title: "Mini-Lecture V.1: From Quark Phase Space to Spectrum"
type: lecture-notes
course: geometric-qcd-course-guide
module: 5
lecture: "V.1"
modified: 2026-10-05
---

# Mini-Lecture V.1: From Quark Phase Space to Spectrum

*We study poles, model assumptions, and the chiral limit. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** II.2 and IV.7; elementary spectral representations. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); poles, model assumptions, and the chiral limit (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 111-112. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 5|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 111-112.

## The question

How can a functional of quark-loop phase space produce a mass spectrum? The remaining lectures propose a measure, a classical phase, and a rule for extracting poles. Each step has a different evidential status.

## A spectrum from a correlator

In a theory with a positive spectral representation, a Euclidean two-point function has schematically

$$
G(p_E^2)=\int_0^\infty\frac{\rho(s)\,ds}{p_E^2+s},
\qquad \rho(s)\ge0.
$$

An isolated stable state contributes $\rho(s)=Z\delta(s-M^2)$, giving $G=Z/(p_E^2+M^2)$. Analytic continuation locates the associated pole. Positivity, analytic continuation, and the operator creating the state are physical inputs; a stationary action by itself does not establish all of them.

For the model $G(p_E^2)=2/(p_E^2+9)+1/(p_E^2+25)$ in fixed mass units, the spectral measure is $2\delta(s-9)+\delta(s-25)$. There are two positive-residue masses, $3$ and $5$. Reading off these poles is an exact calculation within this example.

## The proposed route

V.2 changes variables from loop data to spinors and examines a Jacobian with a gauge zero mode. V.3 computes the radial measure and a local Dirac Fourier kernel. V.4 derives the equation of a proposed Liouville action. V.5 constructs a real rotating surface. V.6 derives a stationary spectral parametrization and distinguishes it from an exact-WKB proof. V.7 evaluates that parametrization and designs a fit audit.

The cancellation of two local scale weights in V.3 does not eliminate the scale-dependent action in V.4. A real Lorentzian surface in V.5 does not itself prove spectral positivity. A fit in V.7 tests a parametrized model and does not retroactively prove the geometric identities in Module III.

## Chiral symmetry and the pion

The source's light-pion difficulty is a limitation of its proposed spectrum. It must not be described as a general exclusion of Goldstone bosons by the planar limit. In the usual large-$N_c$ chiral counting, $f_\pi^2$ and the quark condensate are both of order $N_c$. Their ratio can therefore remain of order one, and the pion mass tends to zero with the light quark masses in the chirally broken theory.

The schematic relation

$$
f_\pi^2m_\pi^2\propto(m_u+m_d)|\langle\bar q q\rangle|
$$

illustrates this scaling without fixing flavor conventions for its coefficient. It does not demand a $1/N_c$ correction to permit a massless Goldstone. The source model's positive endpoint mass parameter is not the same observable as a pion mass or a renormalized current quark mass.

## Worked laboratory: large-color chiral scaling

Write $f_\pi^2=N_c f_0^2$ and $|\langle\bar q q\rangle|=N_c C_0$ in a schematic chiral relation. The factors of $N_c$ cancel, giving $m_\pi^2\propto(m_u+m_d)C_0/f_0^2$. The limit of vanishing quark masses can therefore give a massless mode at large $N_c$.

This scaling calculation does not derive chiral symmetry breaking. It demonstrates why the assertion that large $N_c$ generically forbids its Goldstone bosons is incorrect.

## What is established

The two-pole example is exact and the chiral scaling is a standard framework input, with a primary reference in the bibliography. The twistor construction and its QCD identification remain conditional on the earlier claims and their unresolved checks.

## Looking ahead

V.2 starts with a finite matrix spectrum so that the Jacobian's zero mode is visible before any infinite product of measures is invoked.

## Problem set

1. **Classroom core.** Read the masses from $G=2/(p_E^2+9)+1/(p_E^2+25)$.

2. **Self-study calculation.** Cancel the large-$N_c$ factors in the laboratory relation.

3. **Self-study interpretation.** Does a successful fit establish spectral positivity or a QCD derivation?

4. **Research extension.** Map each step from the phase-space amplitude to a spectral pole.

## Answer checkpoints

1. They are $3$ and $5$ in the chosen units, with residues $2$ and $1$.

2. The ratio of condensate to $f_\pi^2$ is $C_0/f_0^2$, of order one.

3. No. Those depend on the underlying state, operator construction, and analytic properties.

4. Completion: identify the operator, continuation, positivity assumptions, saddle approximation, and fit inputs; mark which implications have actually been derived.

## Teaching note

Use the decisive step in problem 2 as the written exit check for V.1; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-07-induced-qcd-and-asymptotic-freedom|Previous note]] · [[mini-lecture-02-twistor-parametrization-of-the-measure|Next note]] · [[geometric-qcd-course-guide|Course guide]]
