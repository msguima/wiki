---
title: "Mini-Lecture III.7: OPE Matching and Regge Physics"
type: lecture-notes
course: geometric-qcd-course-guide
module: 3
lecture: "III.7"
modified: 2026-10-05
---

# Mini-Lecture III.7: OPE Matching and Regge Physics

*We study the OPE tensor contraction and dimensional scales. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** III.2; matrix traces and operator dimensions. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); the OPE tensor contraction and dimensional scales (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked Source reconstruction explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 85-91. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 3|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 85-91.

## The question

How could a short-distance observable determine a proposed area scale, and how does a rotating classical surface generate a Regge slope? Both steps need normalizations. We calculate the tensor contraction and the classical model explicitly, while keeping their identification with the source's QCD construction conditional.

## The short-distance tensor

Two area insertions in a Wilson loop give field-strength insertions with connecting transporters. In the source's leading short-distance model their tensor structure is
$$
\frac{I_{\mu\lambda}I_{\nu\rho}-I_{\nu\lambda}I_{\mu\rho}}{|x|^4},
\qquad I_{\mu\lambda}=\delta_{\mu\lambda}-2n_\mu n_\lambda,
\qquad n=x/|x|.
$$
A coupling-dependent coefficient and the relevant traced observable accompany this expression. The power follows from the engineering dimensions of two field strengths in four dimensions. In an interacting theory, running, operator mixing, and contact terms require separate treatment.

Contract this tensor with
$$
\Pi_{\mu\nu\lambda\rho}
=\frac12(\delta_{\mu\lambda}\delta_{\nu\rho}-\delta_{\nu\lambda}\delta_{\mu\rho}).
$$
The first delta product gives $[(\operatorname{tr}I)^2-\operatorname{tr}I^2]/2$. The second, including its minus sign and exchanging the antisymmetric indices, gives the same amount. Hence
$$
S(d)=(\operatorname{tr}I)^2-\operatorname{tr}I^2.
$$
Using $n^Tn=1$,
$$
I^2=(1-2nn^T)^2=1,\qquad \operatorname{tr}I=d-2,
$$
so $S(d)=(d-2)^2-d=(d-1)(d-4)$. The displayed leading tensor therefore has zero contraction at $d=4$. The laboratory evaluates the same invariant in a diagonal basis.

## What the condensate matching assumes

Source page 86 matches the remaining dimension-four condensate contribution to a second geometric area variation and reports
$$
\kappa^2=\frac{\pi^2}{8N_c}
\left\langle\frac{\alpha_s}{\pi}(G^a_{\mu\nu})^2\right\rangle.
$$
The expectation bracket was previously misread as an extra factor $D$; no such factor belongs in this transcription. Here the condensate includes the explicit coupling factor. A quoted value for this quantity cannot be substituted into an unweighted $\langle G^2\rangle$ without translating conventions.

If the condensate has mass dimension four, then $\kappa$ has mass dimension two, consistent with $e^{-\kappa S}$ for an area $S$. Dimensional consistency does not fix the numerical coefficient. That coefficient requires the correct area normalization, insertion normalization, and the full matching prescription.

The source identifies its physical tension as $\sigma=2\sqrt2\,\kappa$. This is part of that geometric matching. The tensor failure in III.5 prevents treating the identification as an independently established QCD prediction. The cancellation of one leading tensor structure also does not establish that the condensate is the only surviving term in the full OPE.

## The momentum-space dressing

In a finite Fourier transform, multiplication by an area factor becomes convolution. The source formally applies this rule as
$$
W[P]=\int DQ\,G[P-Q]W_0[Q],
\qquad
G[Q]=\int D_C\,e^{-\kappa S[C]+i\int Q\cdot\dot C}.
$$
The construction needs a defined measure and a transformed operator domain. Neither nonanalyticity of $G$ nor a solution of the full momentum loop equation follows from writing the convolution. Brownian roughness alone is also insufficient, as II.7 demonstrates.

## A classical rotating model with an explicit slope

Use Minkowski signature $(+---)$ and
$$
X(\tau,r)=(\tau,r\cos\omega\tau,r\sin\omega\tau,0),
\qquad -R\le r\le R.
$$
Its induced metric is $\operatorname{diag}(1-\omega^2r^2,-1)$, with vanishing cross term. V.5 checks this directly. For tension $\sigma$ and two endpoint masses $m_q$, the Nambu–Goto model has the Lagrangian per unit target time
$$
L=-2\sigma\int_0^Rdr\,\sqrt{1-\omega^2r^2}
-2m_q\sqrt{1-\omega^2R^2}.
$$
It is a Lagrangian, not the full time-integrated action. At zero angular speed its potential is $2\sigma R$ plus endpoint rest masses; the total separation is $2R$.

For this specified model the energy and angular momentum are
$$
E=2\sigma\int_0^R\frac{dr}{\sqrt{1-\omega^2r^2}}
+\frac{2m_q}{\sqrt{1-v^2}},
$$
$$
J=2\sigma\omega\int_0^R\frac{r^2dr}{\sqrt{1-\omega^2r^2}}
+\frac{2m_q\omega R^2}{\sqrt{1-v^2}},\qquad v=\omega R.
$$
The bulk integrals follow by the substitution $r=\sin\theta/\omega$. In the exactly massless-endpoint model the free endpoints move at $v=1$, so
$$
E=\frac{\pi\sigma}{\omega},\qquad
J=\frac{\pi\sigma}{2\omega^2},\qquad E^2=2\pi\sigma J.
$$
This is the classical slope of the displayed rotating model. It does not fix intercepts, quantum fluctuations, or the validity of the source's exact-WKB spectrum. The same classical slope can occur in different models, so observing it does not prove the absence of string vibrations or select a unique microscopic representation.

## Status of the module

The reflection contraction and classical slope are explicit calculations. The geometric condensate matching, proposed momentum kernel, and vacuum interpretation require the source's additional hypotheses. The intended boundary-determined surface has an unresolved tensor premise. Subsequent fermion and spectrum lectures retain that limitation while developing their independent finite examples.

## Worked laboratory: the reflection matrix

Choose the unit vector $n=(1,0,\ldots,0)$. Then $I=1-2nn^T=\operatorname{diag}(-1,1,\ldots,1)$, so $I^2=1$, $\operatorname{tr}I=d-2$, and $\operatorname{tr}I^2=d$. The contraction is
$$
(\operatorname{tr}I)^2-\operatorname{tr}I^2=(d-2)^2-d=(d-1)(d-4).
$$
For $d=3,4,5$ the values are $-2,0,4$. Rotating $n$ conjugates the matrix and preserves these traces. The cancellation therefore does not depend on a special direction.

The identity cancels the stated leading tensor structure in four dimensions. It does not by itself remove logarithmic running, contact counterterms, or every operator in a full QCD OPE. Matching a condensate to a geometric tension also requires the normalization of that geometric functional.

## Problem set

1. **Classroom core.** Compute $I^2$ directly using $n^Tn=1$.

2. **Self-study calculation.** Evaluate the tensor contraction in dimensions three and five.

3. **Self-study interpretation.** What are the units of $\kappa$ if $\kappa^2$ matches a dimension-four condensate?

4. **Research extension.** Audit the condensate matching on slide 86.

## Answer checkpoints

1. $(1-2nn^T)^2=1-4nn^T+4n(n^Tn)n^T=1$.

2. It is $-2$ and $4$, respectively.

3. $\kappa$ has mass dimension two. It multiplies an area of mass dimension minus two in an exponential.

4. Completion: fix field and coupling conventions, the area normalization, renormalization scale and operator definition, and identify which part is source input versus independently derived. The tensor cancellation alone does not complete the matching.

## Teaching note

Use the decisive step in problem 2 as the written exit check for III.7; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-06-twistor-factorization-and-parity|Previous note]] · [[mini-lecture-01-majorana-fields-on-a-surface|Next note]] · [[geometric-qcd-course-guide|Course guide]]
