---
title: "Mini-Lecture IV.5: Large Mass Limit and the A-Term"
type: lecture-notes
course: geometric-qcd-course-guide
module: 4
lecture: "IV.5"
modified: 2026-10-05
---

# Mini-Lecture IV.5: Large Mass Limit and the A-Term

*We study large-mass locality and the range of a derivative expansion. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** IV.3–IV.4; Fourier kernels and asymptotic series. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); large-mass locality and the range of a derivative expansion (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked Source reconstruction explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 104-105. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 4|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 104-105.

## The question

When does a heavy auxiliary field produce a local expansion, and how can a Bianchi identity remove one term in a loop equation? Source pages 104–105 propose an A-term cancellation. We first establish the finite identities and scale conditions, then identify the additional matching required by that proposal.

## Locality requires a scale hierarchy

A massive propagator suppresses long distances. An expansion in local geometric invariants is controlled only when the geometric and external momentum scales are small relative to $m$. Besides $m\gg\Lambda_{\mathrm{QCD}}$, a curved surface needs, schematically, $|\mathcal R|/m^2\ll1$ and analogous conditions on derivatives and boundary curvature.

A short-distance approximation can fail near a shrinking neck, a cusp, a boundary singularity, or momenta of order $m$. Those are particularly relevant here because the loop equation probes contact configurations. It is not enough to state that every small-loop integral becomes the same universal constant.

The laboratory below derives a propagator expansion with an explicit remainder. Its restricted momentum domain illustrates why uniformity must be checked before exchanging an expansion with an integral.

## A determinant and its logarithm have different second variations

Let $Z$ be a nonzero regulated partition function and set $H=\log Z$. For two ordinary source variables, or commuting regulated variations labeled $l,r$, the chain rule gives
$$
\delta_l Z=Z\,\delta_l H,
\qquad
\delta_l\delta_r Z
=Z\left((\delta_lH)(\delta_rH)+\delta_l\delta_rH\right).
$$
The first term is a product of one-point insertions; the second is connected. This is the finite identity underlying the disconnected/connected split taught in IV.3. The source's A and B diagrams must be matched to it with their full insertion and contact prescriptions.

For the ansatz $Z=e^{-\kappa S}$ the same identity becomes
$$
\delta_l\delta_r Z
=Z\left(\kappa^2(\delta_lS)(\delta_rS)-\kappa\delta_l\delta_rS\right).
$$
A product of two first area derivatives is therefore not interchangeable with a second derivative of the area. Keeping this distinction matters when the source changes from a product of tangent tensors to a divergence of an area derivative.

As a finite check, take $S(x,y)=xy$. Then $S_x=y$, $S_y=x$, and $S_{xy}=1$, whereas $S_xS_y=xy$. Direct differentiation yields $Z_{xy}=(\kappa^2xy-\kappa)Z$. At the origin the product term is zero but the mixed second derivative remains $-\kappa$.

## The proposed A-term reduction

Source pages 104–105 split the second area variation into diagrams with two separate small loops and diagrams with a loop connecting two boundary points. Their proposed local limit contains tangent tensors $T_{\mu\nu}(l)$ and $T_{\alpha\beta}(r)$ and the remaining determinant. The identification of a tangent insertion with an area derivative is a geometric input, including its sign and normalization.

To reach the claimed cancellation, one needs a regulated relation of the schematic form
$$
\int_C dx^\beta\,
\frac{\delta}{\delta\sigma_{\mu\beta}(x)}
B_{\mu\nu}(l)=-\partial_\mu B_{\mu\nu}(l),
\qquad
B_{\mu\nu}=\frac{\delta S}{\delta\sigma_{\mu\nu}}.
$$
This formula is a source matching step, not an identity for arbitrary functionals. Its domain, coincident-point subtractions, endpoint terms, and exchange of limits must be supplied. One must also show that it acts on the correct second-variation structure above.

## What a Bianchi identity would imply

If a two-form $B$ satisfies both $*B=\chi B$ and $\partial_\mu(*B)_{\mu\nu}=0$, then
$$
\partial_\mu B_{\mu\nu}
=\chi\partial_\mu(*B)_{\mu\nu}=0.
$$
This implication is exact. A covariant version applies to gauge curvature as in III.2. Its application to the proposed area derivative requires that derivative to exist and obey the two premises in the same regulated setting.

The literal extended tensor in III.5 fails its duality test. Even after that issue is repaired, the A-term matching and contact limits would need to be derived. We therefore retain the source's cancellation as conditional. IV.6 separately tests the normalization of a radial contact model; that test does not complete the missing determinant calculation.

## Worked laboratory: where a local expansion is controlled

For a scalar massive propagator,
$$
G_m(p)=\frac1{m^2+p^2}
=\frac1{m^2}-\frac{p^2}{m^4}
+\frac{p^4}{m^4(m^2+p^2)}.
$$
This identity follows by two steps of polynomial division, so the remainder is explicit. If $|p|\le M$ with $M/m\ll1$, the remainder is at most $M^4/m^6$. Fourier transformation turns the polynomial terms into delta functions and their derivatives, explaining local effective expansions.

The bound is not uniform when the momentum integration extends without restriction to $|p|\sim m$ or beyond. A local expansion under an ultraviolet divergent integral therefore needs a regulator and matching of the hard-momentum contribution.

Likewise an exact contraction of a regulated A-term with a Bianchi identity can vanish in its domain, but this does not establish the source's entire large-mass limit, especially when contact terms and the geometric construction remain unresolved.

## Problem set

1. **Classroom core.** Verify the remainder by multiplying the displayed identity by $m^2+p^2$.

2. **Self-study calculation.** Bound the remainder for $|p|\le M$.

3. **Self-study interpretation.** Why can one not automatically integrate the truncated series over all momenta?

4. **Research extension.** Formulate the A-term limit with a regulator.

## Answer checkpoints

1. The product is one; the $p^4/m^4$ terms cancel.

2. The denominator is at least $m^6$, giving $M^4/m^6$.

3. The small parameter is $p^2/m^2$, which is not small uniformly on the full integration domain.

4. Completion: retain the tensor indices, separate bounded and large momenta, justify the Bianchi contraction and interchange of limits, and identify any contact remainder.

## Teaching note

Use the decisive step in problem 2 as the written exit check for IV.5; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-04-pauli-cancellation-and-planarity|Previous note]] · [[mini-lecture-06-whites-bridge-and-the-contact-term|Next note]] · [[geometric-qcd-course-guide|Course guide]]
