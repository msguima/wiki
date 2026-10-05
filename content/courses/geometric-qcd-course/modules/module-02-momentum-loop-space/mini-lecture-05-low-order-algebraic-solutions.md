---
title: "Mini-Lecture II.5: Topological Closure and Low-Order Algebraic Solutions"
type: lecture-notes
course: geometric-qcd-course-guide
module: 2
lecture: "II.5"
modified: 2026-10-05
---

# Mini-Lecture II.5: Topological Closure and Low-Order Algebraic Solutions

*We study pairing bases, free coefficients, and residual checks. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** II.4; elementary row reduction. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); pairing bases, free coefficients, and residual checks (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 54-55. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 2|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 54-55.

## The question

What would it mean to solve one order of the momentum loop equation? A displayed tensor is useful only after its basis, constraints, remaining free parameters, and substitution residual are identified. We construct the basis explicitly and use a complete small linear system to practice that procedure.

## Closing a cut path

Cut a closed path at $t=s$. The first piece has displacement $\Delta=P(s)-P(0)$ and the other has $-\Delta$. Their first iterated integrals do not separately vanish. A closing segment of displacement $-\Delta$ must be specified for the first piece. In distributional tangent notation it can be represented by a kick, but its placement and ordering affect higher iterated integrals.

For concatenated paths the tensor series obeys $I[P*Q]=I[P]\otimes I[Q]$. If $Q$ is a straight segment of displacement $-\Delta$, its degree-$k$ component is $(-\Delta)^{\otimes k}/k!$. Therefore

$$
I^{(n)}[P*Q]=\sum_{k=0}^n I^{(n-k)}[P]\otimes
\frac{(-\Delta)^{\otimes k}}{k!}.
$$

This gives a reproducible closure prescription. It cannot generally be replaced by subtracting one unqualified product $I^{(1)}I^{(n-1)}$. The IAS gap prescription must be translated into its own ordered or quotient basis before comparing coefficients.

## Counting and listing pairings

For even $n$, pair index $1$ with one of $n-1$ partners and pair the rest recursively. Thus $p_n=(n-1)p_{n-2}$ with $p_0=1$, or

$$
p_n=(n-1)!!=\frac{n!}{2^{n/2}(n/2)!}.
$$

These two expressions are equal. They count all labeled pairings, before imposing cyclic relations. They are not two competing notions of cyclic and noncyclic counting.

For $n=4$ the structures are $A=\delta_{12}\delta_{34}$, $B=\delta_{13}\delta_{24}$, and $C=\delta_{14}\delta_{23}$. For $n=6$ the complete list, grouped by the partner of $1$, is

$$
\begin{aligned}
&(12)(34)(56),\ (12)(35)(46),\ (12)(36)(45),\\
&(13)(24)(56),\ (13)(25)(46),\ (13)(26)(45),\\
&(14)(23)(56),\ (14)(25)(36),\ (14)(26)(35),\\
&(15)(23)(46),\ (15)(24)(36),\ (15)(26)(34),\\
&(16)(23)(45),\ (16)(24)(35),\ (16)(25)(34).
\end{aligned}
$$

Here $(ij)$ means $\delta_{\mu_i\mu_j}$. Linear independence must still be checked in the chosen dimension and symmetry sector, especially at higher ranks. The count is a combinatorial count, not by itself the rank of the tensor ansatz.

## Source formula and version boundary

The visual reading of IAS slide 55, equation (44), is

$$
W^{(4)}_{\mathrm{IAS}}=\frac16 B+c_{4,1}(A+B+C).
$$

The parenthesis starts after $c_{4,1}$; it is not multiplied by the preceding $1/6$. Appendix C of the March 23 version of Part II instead writes the free term proportional to $A+C$. These expressions differ in the coefficient of $B$ and must not be silently identified. The coefficient is displayed as free in the source family, not as a numerical value calculated in these notes. A comparison must specify whether the tensors are raw moments, connected coefficients, or quotient representatives.

The final line of the slide's sixth-order expression is obscured by its footer. The complete pairing list above includes $(14)(25)(36)$, which the earlier course transcription omitted. We do not reconstruct its coefficient from a clipped image or claim that a list of fifteen structures verifies the sixth-order loop equation.

## Worked linear system: free parameters and consistency

Consider coefficients $(a,b,c)$ constrained by

$$
a-c=0,\qquad b=\frac16,\qquad 2a-2c=0.
$$

The matrix and source are

$$
A_0=\begin{pmatrix}1&0&-1\\0&1&0\\2&0&-2\end{pmatrix},
\qquad b_0=\begin{pmatrix}0\\1/6\\0\end{pmatrix}.
$$

Subtract twice the first row from the third. The last row becomes $0=0$, so the rank is two and the solution is $(t,1/6,t)$. A substitution gives zero residual for every $t$. The homogeneous kernel is spanned by $(1,0,1)$.

This is a teaching model for solving a tensor ansatz; it is not a derivation of the source's momentum equation. If the third right-hand entry is changed to $1$, the last equation instead becomes $0=1$. The same equation count and unknown count now give no solution.

## A reproducible source calculation would require

Export the exact equations, ordered basis, closure map, cyclic and parity identifications, and lower-order free parameters. Assemble rational matrices; report both the matrix and augmented ranks; substitute the general solution. Save those inputs with the source version. A notebook's displayed answer without its basis and equations does not complete this task.

## Worked laboratory: pairings are not equation ranks

At $n=8$ the recursion for labeled pairings gives $7\cdot5\cdot3\cdot1=105$. This number counts candidate delta structures before symmetry and dimension relations. It does not tell us the number of equations or their rank. Conversely, adding lower-order free parameters can make a matching system have more unknowns than the number of eighth-order pairing coefficients alone.

The model system in the derivation has three equations but rank two. Its solution space is a line because one homogeneous direction survives. The residual, not the raw count, verifies every point on that line.

## What is established

The closure formula, pairing count, full sixth-order list, and model linear solve are exact. The low-order MLE solutions are source-reported results pending a convention-matched reproduction. This boundary is preserved in the exercise set.

## Looking ahead

II.6 uses the same row-reduction logic to distinguish overdetermination from a demonstrated obstruction.

## Problem set

1. **Classroom core.** Show that $6!/(2^3 3!)=5!!$.

2. **Self-study calculation.** Find the kernel of the displayed model matrix $A_0$.

3. **Self-study interpretation.** Why is the source's clipped sixth-order formula insufficient as a reproducible solution?

4. **Research extension.** Reconcile slide 55 with Part II Appendix C before solving the MLE.

## Answer checkpoints

1. Both equal $15$. These are two formulas for the same labeled pairing count.

2. Solving $a-c=0$ and $b=0$ gives $(a,b,c)=t(1,0,1)$.

3. The complete coefficient list, basis, equations, and residual are needed. Listing fifteen pairings does not determine their coefficients.

4. Completion: freeze both versions, state the tensor convention and quotient, and either provide a conversion explaining the differing $W^{(4)}$ terms or record an unresolved discrepancy. Do not choose a free coefficient by guesswork.

## Teaching note

Use the decisive step in problem 2 as the written exit check for II.5; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-04-kinematic-tensors-and-magnus-forms|Previous note]] · [[mini-lecture-06-breakdown-at-eighth-order|Next note]] · [[geometric-qcd-course-guide|Course guide]]
