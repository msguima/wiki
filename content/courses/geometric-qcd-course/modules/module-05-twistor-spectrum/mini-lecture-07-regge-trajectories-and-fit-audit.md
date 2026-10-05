---
title: "Mini-Lecture V.7: Regge Trajectories and Fit Audit"
type: lecture-notes
course: geometric-qcd-course-guide
module: 5
lecture: "V.7"
modified: 2026-10-05
---

# Mini-Lecture V.7: Regge Trajectories and Fit Audit

*We study Regge checks, units, and a reproducible fit audit. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** V.6; asymptotic expansion and residual statistics. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); Regge checks, units, and a reproducible fit audit (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 134-142. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 5|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 134-142.

## The question

What can be checked directly in the proposed spectral formula, and what requires the original fit data and a physical derivation? We first transcribe the parametric equations with their units, calculate limits and a numerical point, then separate fit quality from prediction.

## The parametric model

In the notation of IAS slide 134, set $x=m/\sqrt\sigma$, let $0<\beta<\pi/2$, and define

$$
\bar x=x+\sqrt{x^2-\frac1{3\pi}},\qquad
K=\frac{\bar x\sin\beta}{\cos^2\beta},\qquad
F(\beta)=\beta+\frac12\sin2\beta.
$$

The real branch requires $x\ge1/\sqrt{3\pi}$. The equations are

$$
\mathcal E:=\frac E{\sqrt\sigma}=KF(\beta)+2x\cos\beta,
\qquad
J=\frac{K^2}{4}F(\beta)-\frac{\tan\beta-\beta}{6\pi}-\frac q2.
$$

Here $q$ is the source's discrete index, with its pseudoscalar/vector assignment as specified in the source. The endpoint energy $2x\cos\beta$ is outside the factor $K$, and the drag term is outside $K^2/4$. The spin shift is $-q/2$, not $-\sqrt K/2$.

These formulas define a model that can be evaluated exactly once its parameters are supplied. Their identification with QCD inherits the unresolved geometric and spectral assumptions of the earlier modules.

## Worked numerical checkpoint

Take $x=1$, $\beta=0.5$, $q=0$. First compute the discriminant, then $\bar x$, $K$, and $F$, and substitute without rounding intermediate quantities. The result is

$$
\mathcal E=2.8702364096,\qquad J=0.3351497574.
$$

Changing only $q$ from $0$ to $-1$ increases $J$ by $1/2$ and leaves $\mathcal E$ fixed. This isolates the role of the topological shift. It is a numerical check of the displayed parametrization, not a fit to a hadron.

## Threshold expansion

Use $\sin\beta=\beta-\beta^3/6+\cdots$, $\cos\beta=1-\beta^2/2+\cdots$, and $F=2\beta-\frac23\beta^3+\cdots$. Then

$$
\mathcal E=2x+(2\bar x-x)\beta^2+O(\beta^4),
$$

$$
J+\frac q2=
\left(\frac{\bar x^2}{2}-\frac1{18\pi}\right)\beta^3+O(\beta^5).
$$

The first result comes from $KF=2\bar x\beta^2+O(\beta^4)$ and $2x\cos\beta=2x-x\beta^2+O(\beta^4)$. The second uses $\tan\beta-\beta=\beta^3/3+O(\beta^5)$. Eliminating $\beta$ gives the local hook

$$
J+\frac q2=
\frac{\bar x^2/2-1/(18\pi)}{(2\bar x-x)^{3/2}}
(\mathcal E-2x)^{3/2}
+O((\mathcal E-2x)^{5/2}).
$$

At the lower bound on $x$, $\bar x=x$, not $2x$. This is a bound on the model's real parameter domain, and does not itself derive QCD chiral symmetry breaking.

## High-energy slope

Put $\epsilon=\pi/2-\beta$. To leading order $K\sim\bar x/\epsilon^2$, $F\to\pi/2$, and $\mathcal E\sim\pi K/2$. Hence

$$
J\sim\frac{\pi K^2}{8}\sim\frac{\mathcal E^2}{2\pi}
=\frac{E^2}{2\pi\sigma}.
$$

The drag is subleading at this order. Further coefficients must be obtained by a consistent inversion of the same parametric equations. The earlier course's dimensionally inconsistent asymptotic expressions are not retained.

## Units and the reported fit

The source reports $\sqrt\sigma\simeq417\ \mathrm{MeV}$, so $\sigma\simeq0.173889\ \mathrm{GeV}^2$. A string tension has units of mass squared. Reporting $\sigma=417\ \mathrm{MeV}$ confuses the tension with its square root.

The slides report a five-parameter description of 36 states across 13 families and an RMS relative mass discrepancy of about $8.1\%$ after excluding the pion from that metric. Those figures are source-reported; the original optimization and state table have not been reproduced here. Families included in the global fit are in-sample comparisons even when their formula introduces no additional parameter.

The size of $1/N_c^2$ at $N_c=3$ is about $11\%$. Similarity of that number to a fit residual does not derive a theoretical uncertainty distribution or establish the origin of the residuals. Sea-quark effects, widths, state assignments, and asymptotic expansion coefficients require their own analysis.

## A complete audit design

Preserve a table with each state's identifier, $J^{PC}$ where applicable, mass, uncertainty, family, source edition, inclusion decision, and assigned $q$. Specify the actual optimized objective: an action-phase residual is not identical to a mass residual. Save the five fitted parameters, optimizer settings, initializations, and all residuals.

For relative mass residuals $r_i=(M_i^{\mathrm{model}}-M_i^{\mathrm{obs}})/M_i^{\mathrm{obs}}$, compute $\sqrt{\sum_i r_i^2/n}$ on the explicitly stated set. Report excluded states alongside the metric, and distinguish this unweighted RMS from a chi-squared statistic using experimental uncertainties.

For prediction, reserve a family or states before fitting. Refit the remaining data and report held-out errors without retuning. Comparing such a result with a simple linear Regge baseline would test whether the additional structure improves predictive performance. The source's global-fit numbers do not perform this test.

## The pion and the claim boundary

Spontaneous chiral symmetry breaking and Goldstone bosons can occur in the large-$N_c$ limit; the light pion is not generically a nonplanar effect. The proposed geometric spectrum's treatment of chiral dynamics is a limitation of that construction. The chiral large-$N_c$ reference in the bibliography provides the appropriate framework.

## Worked laboratory: RMS is not a prediction score by itself

For three measured masses $(1,2,4)$ and model values $(1.1,1.8,4.4)$ in the same units, the relative residuals are $(0.1,-0.1,0.1)$. Their unweighted RMS is $0.1$, or $10\%$. If the parameters were fitted to those three masses, this is an in-sample diagnostic.

If the third state was withheld before fitting, its $10\%$ error is one held-out result, while the first two errors still describe the training set. Neither quantity is a chi-squared without an uncertainty model. Publishing the inclusion rule prevents a residual statistic from silently changing its meaning.

## What is established

The corrected transcription, parameter domain, sample point, units, threshold expansion, and leading Regge slope are checked calculations within the model. Exact WKB, the complete QCD derivation, the eighth-order obstruction, and the reported global fit retain the separate status recorded in the claim map.

## Looking back

The course has developed tools for testing a proposed chain of arguments: loop calculus, tensor algebra, constrained geometry, determinants, distributional limits, and spectral diagnostics. A useful final report identifies which links have been reproduced and which still require an independent construction.

<!-- generated-figures -->
## Figures for the calculation

![[geometric-qcd-regge-model.svg|Corrected parametric model at three chosen dimensionless masses. No PDG data are shown and no fit has been performed.]]

<!-- /generated-figures -->

## Problem set

1. **Classroom core.** Convert $\sqrt\sigma=0.417\ \mathrm{GeV}$ into $\sigma$.

2. **Self-study calculation.** Use $\partial_K\Phi=0$ and $\Phi=0$ to derive the spin formula.

3. **Self-study interpretation.** Does using no new family-specific parameter make a globally fitted family held out?

4. **Research extension.** Reproduce the source fit, then perform a separate prediction test.

## Answer checkpoints

1. $\sigma=0.173889\ \mathrm{GeV}^2$.

2. Substitute $\mathcal E=KF+2x\cos\beta$; the mass terms cancel and $\Phi=\pi K^2F-4\pi(J+q/2)-\tfrac23(\tan\beta-\beta)$ gives the result.

3. No. Held-out status depends on whether its data were excluded before optimization.

4. Completion: preserve the state table, uncertainty and exclusion rules, objective, parameters, optimizer and residuals. For prediction, hold out data before fitting and report errors without retuning. The current course does not claim this research audit has been completed.

## Teaching note

Use the decisive step in problem 2 as the written exit check for V.7; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-06-monodromies-wkb-action-and-spin-projection|Previous note]] · [[geometric-qcd-course-guide|Course guide]]
