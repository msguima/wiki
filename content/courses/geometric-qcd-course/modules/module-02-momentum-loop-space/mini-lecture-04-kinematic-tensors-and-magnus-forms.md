---
title: "Mini-Lecture II.4: Kinematic Tensors, Shuffle Ideals, and Magnus Forms"
type: lecture-notes
course: geometric-qcd-course-guide
module: 2
lecture: "II.4"
modified: 2026-10-05
---

# Mini-Lecture II.4: Kinematic Tensors, Shuffle Ideals, and Magnus Forms

*We study the shuffle identity and the nonzero rectangle area. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** II.3; ordered integrals and matrix commutators. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); the shuffle identity and the nonzero rectangle area (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 51-53. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 2|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 51-53.

## The question: which expansion is being used?

A path-ordered exponential has an expansion in ordered tensor integrals. Its logarithm has a Lie-series expansion involving commutators. Both appear near the momentum loop equation, and both are sometimes called Magnus objects in the source. They must be distinguished before any coefficient is set to zero.

## Ordered integrals and shuffle multiplication

For a smooth path $P:[0,1]\to\mathbb R^d$, define

$$
I^{\mu_1\cdots\mu_n}[P]=
\int_{0<t_1<\cdots<t_n<1}
dP^{\mu_1}(t_1)\cdots dP^{\mu_n}(t_n).
$$

The first level is $I^\mu=P^\mu(1)-P^\mu(0)$. To multiply two first levels, partition the square of integration into its two triangles:

$$
I^\mu I^\nu=I^{\mu\nu}+I^{\nu\mu}.
$$

The diagonal has measure zero for a smooth path. Higher products sum over all interleavings that preserve the internal order of each factor: this is the shuffle identity. For a closed path, $I^\mu=0$, so the symmetric part of $I^{\mu\nu}$ vanishes. The antisymmetric part need not vanish.

## Worked calculation: the rectangular path

Take the positively oriented rectangle $(0,0)\to(a,0)\to(a,b)\to(0,b)\to(0,0)$. Since the path begins at the origin,

$$
I^{xy}=\oint P_x\,dP_y=ab,\qquad
I^{yx}=\oint P_y\,dP_x=-ab.
$$

On the right edge $P_x=a$ and $P_y$ rises from $0$ to $b$; the left edge has $P_x=0$. This gives the first result. On the upper edge $P_y=b$ while $P_x$ decreases by $a$, giving the second. Closedness is satisfied, and the shuffle sum is zero, but the second level contains the signed area.

For constant noncommuting matrices $X,Y$, the corresponding ordered product, in the explicitly chosen convention, is $U=e^{aX}e^{bY}e^{-aX}e^{-bY}$. Its logarithm starts at

$$
\log U=ab[X,Y]+O(a^2b,ab^2).
$$

Thus closedness does not eliminate the second logarithmic Magnus term either. Reversing the path reverses the leading area and commutator.

## Why a cubic tensor nevertheless enters the loop operator

The cubic structure comes from $[D_\mu,[D_\mu,D_\nu]]$, not from the absence of every lower iterated integral. Expand this nested commutator:

$$
[D_\mu,[D_\mu,D_\nu]]
=D_\mu D_\mu D_\nu-2D_\mu D_\nu D_\mu+D_\nu D_\mu D_\mu.
$$

In an ordered basis $D_\alpha D_\beta D_\gamma$, its coefficient is

$$
T_\nu^{\alpha\beta\gamma}
=\delta_{\alpha\beta}\delta_{\gamma\nu}
-2\delta_{\alpha\gamma}\delta_{\beta\nu}
+\delta_{\beta\gamma}\delta_{\alpha\nu}.
$$

This elementary expansion identifies which index contractions must be retained when matching the momentum equation. Its precise action on the source's ordered integrals requires the same point-splitting and closure convention as that equation.

## Coefficients and integrals are different objects

In an expression $W[P]=\sum_n W^{(n)}_{\mu_1\cdots\mu_n}I^{\mu_1\cdots\mu_n}[P]$, a contraction can vanish on closed paths even though the coefficient tensor is nonzero. For instance $W^{(2)}_{\mu\nu}=c\delta_{\mu\nu}$ gives $c\sum_\mu I^{\mu\mu}=0$. This does not prove $c=0$. It describes a redundancy of this closed-path representation.

Likewise a tensor basis quotient by shuffle relations is a specified algebraic quotient; it is not permission to discard any term whose name resembles a shuffle product. The recursion in II.5 must state its basis and free coefficients before its rank is meaningful.

## Worked laboratory: scaling the rectangle

The rectangle calculation has a simple homogeneity check. Replacing $P$ by $sP$ multiplies every differential by $s$, so $I^{(n)}[sP]=s^nI^{(n)}[P]$. At $a=2$, $b=3$, $I^{xy}=6$ and $I^{yx}=-6$; doubling the whole loop gives $24$ and $-24$. This distinguishes the degree of an ordered integral from the degree of the operator contracting it.

## What is established

The shuffle relation, rectangle, and cubic tensor are exact calculations for smooth paths and finite matrices. Their extension to rough paths requires a prescription for iterated integrals. The full momentum loop equation is treated as the regulated source equation from II.3.

## Looking ahead

II.5 builds the pairing basis and separates source formulas from a reproduced linear system. II.6 explains what an actual inconsistency certificate would contain.

<!-- generated-figures -->
## Figures for the calculation

![[geometric-qcd-ordered-rectangle.svg|The oriented 2 by 3 rectangle has zero first-level displacement and a nonzero antisymmetric second ordered integral.]]

<!-- /generated-figures -->

## Problem set

1. **Classroom core.** Calculate $I^{xy}$ and $I^{yx}$ for sides $2,3$.

2. **Self-study calculation.** Expand $[X,[X,Y]]$ into ordered words.

3. **Self-study interpretation.** Does $I^\mu=0$ imply that a coefficient tensor $W^{(2)}$ vanishes?

4. **Research extension.** Compare the source's “Magnus forms” with iterated integrals and the logarithmic Magnus series.

## Answer checkpoints

1. They are $6$ and $-6$.

2. $X^2Y-2XYX+YX^2$.

3. No. For example a symmetric coefficient can contract to zero with the antisymmetric second level while itself being nonzero.

4. Completion: give definitions, ordering, and the conversion through degree three. Identify which object the source coefficient contracts; do not equate the series merely by name.

## Teaching note

Use the decisive step in problem 2 as the written exit check for II.4; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-03-factorization-of-the-momentum-loop-measure|Previous note]] · [[mini-lecture-05-low-order-algebraic-solutions|Next note]] · [[geometric-qcd-course-guide|Course guide]]
