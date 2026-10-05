---
title: "Mini-Lecture III.1: Why Four-Dimensional Geometry Enters"
type: lecture-notes
course: geometric-qcd-course-guide
module: 3
lecture: "III.1"
modified: 2026-10-05
---

# Mini-Lecture III.1: Why Four-Dimensional Geometry Enters

*We study four-dimensional two-forms and what an ansatz must supply. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** II.6–II.7; the Hodge-star bridge. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); four-dimensional two-forms and what an ansatz must supply (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked Source reconstruction explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 66-69. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 3|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 66-69.

## The question

What does four-dimensional geometry add to the loop equation, and what must still be proved before a geometric functional can represent a vacuum? The useful new object is the Hodge star on two-forms. It provides a sufficient route from a Bianchi identity to a homogeneous equation. It does not select a quantum state by itself.

## From an algebraic obstruction to a new ansatz

II.6 distinguished a reported rank obstruction in a specified Taylor ansatz from a universal impossibility theorem. II.7 showed that neither infinite dimension nor rough paths alone prove nonanalyticity. The source's move to geometry is a proposed new representation after those algebraic difficulties. It is not forced by counting scalar and vector equations.

The relevant source pages are 67–69. Their proposed construction is developed in III.2–III.5 and tested directly in III.5. The exact algebra of two-forms below remains useful even when the proposed realization fails that test.

## Homogeneous and inhomogeneous equations

Write a regulated loop equation schematically as $\mathcal L_\nu W=\mathcal R_\nu[W]$, where $\mathcal R$ includes contour splitting and is nonlinear in $W$. A homogeneous zero mode satisfies $\mathcal L_\nu Z=0$. Unless $\mathcal R_\nu[Z]$ also vanishes, it is not a solution of the full equation.

Suppose, on a common regulated domain, that $\mathcal L_\nu$ has the product and chain rules stated in I.4. Then for a fixed constant $\kappa$,
$$
\mathcal L_\nu e^{-\kappa S}
=-\kappa e^{-\kappa S}\mathcal L_\nu S.
$$
Thus $\mathcal L_\nu S=0$ is sufficient for this exponential to be a homogeneous zero mode. For the dressing $W=ZW_0$ to preserve the splitting equation, one also needs $Z[C]=Z[C_{xy}]Z[C_{yx}]$ at the supported cut. III.3 derives the corresponding area-additivity condition.

These are conditional algebraic implications. A differential operator of genuine second order ordinarily has additional product terms; I.4 explains which point-splitting assumptions are needed here. Also, a functional Fourier transform preserves an equation only after the operator, measure, and domains have been transformed together. Using the same symbol on both sides of the transform is not a proof of equivalence.

## The classical gauge-field comparison

The loop insertion in I.4 contains parallel transport:
$$
\mathcal L_\nu w[C]\propto
\frac1{N_c}\operatorname{tr}\!\left(
U(C_{sx})[D_\mu,\mathcal F_{\mu\nu}](x)U(C_{xs})\right).
$$
The overall sign follows the area orientation. The important structure is the covariant-divergence insertion inside the transported trace. A bare trace of a commutator would vanish in finite dimensions and cannot replace it.

A background satisfying $[D_\mu,\mathcal F_{\mu\nu}]=0$ therefore gives a vanishing insertion wherever this regulated dictionary applies. This is the source-free classical Yang–Mills equation: the contracted covariant divergence vanishes. It does **not** require every component to be covariantly constant, which would impose $D_\alpha\mathcal F_{\mu\nu}=0$ for every index.

The converse needs care. A vanishing traced insertion for one loop does not imply that the inserted matrix vanishes. For example $\operatorname{tr}\sigma_3=0$ although $\sigma_3\ne0$. Recovering a field equation from all transported traces would need a completeness argument and a specified field class. Identifying that background with the quantum large-color vacuum needs still more: a state and all of its loop correlations.

## Why four dimensions are special for this route

On oriented Euclidean four-space, the Hodge star maps a two-form to another two-form:
$$
(*B)_{\mu\nu}=\frac12\epsilon_{\mu\nu\rho\sigma}B_{\rho\sigma},
\qquad *^2B=B.
$$
Consequently the six-dimensional space of two-forms splits into three-dimensional eigenspaces with eigenvalues $+1$ and $-1$. A Bianchi identity constrains the divergence of $*B$. If $*B=\chi B$ with $\chi=\pm1$, it also constrains the divergence of $B$. III.2 derives this implication for curvature and states the analogous hypotheses for an area derivative.

A surface in four-space does not automatically supply such a two-form. Its ordinary tangent bivector is decomposable, whereas a nonzero real Euclidean self-dual two-form is not: $B\wedge B=B\wedge *B$ is positive, while a simple bivector wedges with itself to zero. The proposed extended tensor is supposed to overcome this distinction, but its literal definition fails the circle calculation in III.5.

## What the source proposal must provide

The source proposes a boundary-determined area functional rather than an independent sum over all bulk embeddings. To make this representation work, it must establish the surface's existence and boundary data, the area variation, the required duality and Bianchi identities, and compatibility with contour splitting. Harmonic extension, conformality, and duality are distinct steps.

Historical difficulties with particular fluctuating-surface models motivate the choice; they do not exclude every other QCD string representation. Nor does fixing a classical surface establish its uniqueness or quantum stability.

The classroom result is the two-form decomposition below. The zero-mode dressing is conditional on explicit operator hypotheses. The identification of the resulting functional with a quantum vacuum remains a source proposal, with a concrete unresolved geometric premise.

## Worked laboratory: the two chiral subspaces

In oriented Euclidean four-space, the six independent two-forms split into two three-dimensional eigenspaces of the Hodge star. One self-dual basis is
$$
B_1=dx^1\wedge dx^2+dx^3\wedge dx^4,\quad
B_2=dx^1\wedge dx^3-dx^2\wedge dx^4,\quad
B_3=dx^1\wedge dx^4+dx^2\wedge dx^3.
$$
Changing the relative signs gives an anti-self-dual basis. For example $*(dx^1\wedge dx^3)=-dx^2\wedge dx^4$, so $*B_2=B_2$.

The projectors $P_\pm=(1\pm*)/2$ obey $P_\pm^2=P_\pm$ and $P_+P_-=0$ because $*^2=1$. A plane's tangent bivector $Q=dx^1\wedge dx^2$ splits as $P_+Q=(dx^{12}+dx^{34})/2$ and $P_-Q=(dx^{12}-dx^{34})/2$. Neither part alone is the original tangent area.

This exact decomposition explains why four dimensions offer a useful duality operation on two-forms. It does not establish that a particular surface functional has the required dual area derivative, or that failure of another ansatz uniquely selects it. III.5 tests that additional claim directly.

## Problem set

1. **Classroom core.** Compute $*B_2$.

2. **Self-study calculation.** Prove $P_+P_-=0$.

3. **Self-study interpretation.** Does the dimension of these eigenspaces prove a QCD vacuum construction?

4. **Research extension.** List the hypotheses connecting a proposed surface to III.2.

## Answer checkpoints

1. Use $*dx^{13}=-dx^{24}$ and $*dx^{24}=-dx^{13}$, giving $B_2$.

2. $(1+*)(1-*)/4=(1-*^2)/4=0$.

3. No. It is kinematics. Existence, boundary data, area variation, and the loop equation remain to be checked.

4. Completion: give a functional domain, area derivative, Bianchi identity, duality, and splitting condition, and identify which are actually demonstrated by the chosen source.

## Teaching note

Use the decisive step in problem 2 as the written exit check for III.1; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-07-nonanalytic-vacuum-and-q-and-a|Previous note]] · [[mini-lecture-02-area-derivatives-and-self-dual-zero-modes|Next note]] · [[geometric-qcd-course-guide|Course guide]]
