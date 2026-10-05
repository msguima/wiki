---
title: "Mini-Lecture III.4: Physical Vacuum and Instanton Language"
type: lecture-notes
course: geometric-qcd-course-guide
module: 3
lecture: "III.4"
modified: 2026-10-05
---

# Mini-Lecture III.4: Physical Vacuum and Instanton Language

*We study the difference between a self-dual field and a physical vacuum. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** III.2; action density and boundary conditions. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); the difference between a self-dual field and a physical vacuum (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked Source reconstruction explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), page 77. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 3|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, page 77.

## The question

What would justify interpreting a geometric area factor as a QCD vacuum? Self-duality and translation invariance are useful structural comparisons with instanton physics, but they do not determine a state or its correlations. This lecture separates that comparison from the stronger identification made on source page 77.

## Classical configurations and quantum states

A classical instanton is a smooth finite-action Euclidean Yang–Mills configuration with appropriate asymptotic conditions and nontrivial topological charge. A chosen representative has a center, scale, and gauge orientation. It is not itself a translation-invariant quantum vacuum.

A quantum state assigns expectation values to observables. Specifying such a state requires more than displaying a classical solution: one must give the measure or operator construction, normalization, boundary conditions, and the relevant positivity and symmetry properties. An instanton ensemble is one semiclassical framework for approximating contributions to those expectation values. It is not a general established identity for the full QCD vacuum.

## Why self-duality helps a classical action

Using the positive Euclidean inner product on Lie-algebra-valued two-forms, write $\|F\|^2=\int F\cdot F$ and $\chi=\pm1$. Since the Hodge star preserves the norm,
$$
\|F-\chi *F\|^2
=2\|F\|^2-2\chi\langle F,*F\rangle\ge0.
$$
Thus $\|F\|^2\ge\chi\langle F,*F\rangle$, with equality when $F=\chi *F$. To turn this into a topological action bound, one must additionally fix the trace normalization, require convergence of the integrals, and specify the behavior at infinity that quantizes the topological term.

The inequality is an algebraic fact. It does not make every self-dual field finite-action. The constant-field laboratory below supplies a direct counterexample to that mistaken inference.

## Translation invariance is a separate operation

For an illustrative finite-volume ensemble with periodic boundary conditions, let $w_{A_z}[C]$ be the loop evaluated in a fixed profile translated by $z$. Define
$$
\overline w[C]=\frac1V\int_V d^4z\,w_{A_z}[C].
$$
If $w_{A_z}[C+a]=w_{A_{z-a}}[C]$, shifting the integration variable proves $\overline w[C+a]=\overline w[C]$. This is an explicit way to restore translation invariance in this model. It does not determine the weights of scales, orientations, topological sectors, or interactions between configurations.

Many different ensembles can share that symmetry. A functional depending only on relative contour coordinates is also translation-invariant, but this does not prove that an instanton-moduli integral has been performed. Equality of the functionals would require equality of their values on a suitable class of contours, not merely matching a symmetry.

## The proposed vacuum dressing

The source considers
$$
W[C]=e^{-\kappa S_\chi[C]}W_0[C].
$$
Under the product-rule and additivity assumptions established conditionally in III.2–III.3, this dressing can preserve the form of the loop equation. The functional $S_\chi$ and its normalization remain additional data. A loop-equation solution must also satisfy the required state conditions before it is identified with a physical vacuum.

Page 77 interprets the geometric factor as an implicitly resummed instanton vacuum. A quantitative identification would require, at minimum, a specified instanton measure and the reproduction of loop observables, vacuum energy, and dependence on the topological angle $\theta$. None of those follows from translation invariance and the proposed duality alone.

There is also a prior issue: III.5 finds that the literal extended tensor does not have the asserted duality even on the circle. The intended geometric zero mode is therefore a premise still to be established, rather than an available example of the desired vacuum.

## What is established

The norm inequality, the finite-volume translation average, and the constant-field calculation are exact under their stated assumptions. They explain what the instanton analogy does and does not supply. The proposed geometric representation of the full QCD vacuum remains unresolved; this lecture does not promote the analogy to an equivalence.

## Worked laboratory: self-dual does not imply finite action

Take an Abelian field on $\mathbb R^4$ with constant components $F_{12}=F_{34}=B$, all other independent components zero. It is self-dual and solves the source-free Maxwell equation because all derivatives vanish. Its Euclidean action density is proportional to $F_{\mu\nu}F_{\mu\nu}=4B^2$.

On a box of side $L$ the action is proportional to $B^2L^4$, so it diverges as the box fills $\mathbb R^4$ for nonzero $B$. This exact example is not a finite-action instanton. It illustrates why self-duality, finite action, topological charge, and membership in a quantum vacuum ensemble are separate properties.

For non-Abelian instanton statements one must specify asymptotic boundary conditions and the bundle or gauge transformations at infinity. For a Wilson functional one additionally needs normalization, positivity or the relevant state conditions, and loop-equation compatibility. Calling an area factor “instanton-like” is an analogy until those ingredients are supplied.

## Problem set

1. **Classroom core.** Calculate $F_{\mu\nu}F_{\mu\nu}$ in the example.

2. **Self-study calculation.** How does the action change under $L\mapsto2L$?

3. **Self-study interpretation.** Does satisfying a classical equation select a unique quantum vacuum?

4. **Research extension.** Compare a genuine finite-action instanton with the constant example.

## Answer checkpoints

1. Each antisymmetric pair is counted twice: $2B^2+2B^2=4B^2$.

2. It increases by a factor of $16$ for the constant field.

3. No. State construction, boundary conditions, normalization, and quantum correlations are additional inputs.

4. Completion: state its boundary conditions, show convergence of its action integral, and explain which of those properties have or have not been established for the source's surface functional.

## Teaching note

Use the decisive step in problem 2 as the written exit check for III.4; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-03-additivity-and-the-goldschmidt-branch|Previous note]] · [[mini-lecture-05-constructing-the-hodge-dual-surface|Next note]] · [[geometric-qcd-course-guide|Course guide]]
