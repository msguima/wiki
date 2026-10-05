---
title: "Mini-Lecture III.6: Twistor Factorization and Parity"
type: lecture-notes
course: geometric-qcd-course-guide
module: 3
lecture: "III.6"
modified: 2026-10-05
---

# Mini-Lecture III.6: Twistor Factorization and Parity

*We study factorization of a complex null vector. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** III.5; Pauli matrices and rank-one matrices. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); factorization of a complex null vector (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked Source reconstruction explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 82-84. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 3|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 82-84.

## The question

How does a complex null vector become a product of two spinors, and which geometric conclusions follow from that factorization? The rank-one matrix identity is exact. The proposed QCD area derivative and a restriction to one active chirality require additional arguments.

## The Euclidean spinor dictionary

Use Pauli matrices and define
$$
V(v)=v_4\,1+i\sum_{j=1}^3v_j\sigma_j.
$$
Then $\det V=v_\mu v_\mu$, where the square is complex bilinear. A nonzero complex null vector gives a rank-one matrix, so locally
$$
V(v)=\lambda\mu^T.
$$
For instance, choose any nonzero column of $V$ as $\lambda$. Rank one makes the other column proportional to it, and those two proportionality coefficients form $\mu^T$. Choosing a different nonzero column gives another patch. At $v=0$ the rank changes and this parametrization is not unique.

The spin group is $\operatorname{Spin}(4)=SU(2)_+\times SU(2)_-$. The rotation group $SO(4)$ is its quotient by the common two-element center. A spinor factorization uses the covering group; it is not an equality between $SO(4)$ and the direct product.

## Norms and the ordinary conformal metric

Taking the Frobenius norm of the matrix gives
$$
\operatorname{tr}(V^\dagger V)=2\sum_\mu|v_\mu|^2
=(\lambda^\dagger\lambda)(\mu^\dagger\mu).
$$
The first equality follows from $\operatorname{tr}(\sigma_i\sigma_j)=2\delta_{ij}$ and $\operatorname{tr}\sigma_i=0$. The second follows by multiplying the rank-one factors.

For the real conformal map $Y=f+\bar f$ with $v=f'$ and $v\cdot v=0$, III.5 gives
$$
g_{uu}=g_{vv}=2|f'|^2
=(\lambda^\dagger\lambda)(\mu^\dagger\mu),\qquad g_{uv}=0.
$$
The ordinary area density in these coordinates is the same product. This fixes the normalization for the dictionary used here. It must not be replaced by an expression containing $\sqrt{|f'|^2}$ without redefining the density and its dimensions. The source's extended area is a different functional, with the unresolved tensor issue in III.5.

## The rescaling freedom

The transformation $(\lambda,\mu)\mapsto(c\lambda,c^{-1}\mu)$ leaves $V$ fixed for any nonzero complex $c$. Where both norms are positive, choose $|c|^4=(\mu^\dagger\mu)/(\lambda^\dagger\lambda)$ to make the rescaled norms equal. An opposite phase remains: $c=e^{i\varphi}$.

This is the local origin of the rescaling and phase redundancies discussed in V.2. A measure calculation still needs real coordinates, gauge conditions, the orbit measure, and treatment of zeros and patch transitions. A rank count does not fix those factors.

## Unit vectors from the spinors

For a nonzero two-component spinor $\lambda$, define
$$
n_i=\frac{\lambda^\dagger\sigma_i\lambda}{\lambda^\dagger\lambda}.
$$
Writing $\lambda=(a,b)^T$ gives the numerator $(2\operatorname{Re}\bar a b,2\operatorname{Im}\bar a b,|a|^2-|b|^2)$. Its squared length is
$$
4|a|^2|b|^2+(|a|^2-|b|^2)^2=(|a|^2+|b|^2)^2.
$$
Thus $n$ is a real unit vector. It is invariant under nonzero complex rescaling of $\lambda$ and parametrizes the associated projective spinor direction. A second spinor gives a second unit vector.

The source calls these the two Gauss maps and proposes an area-derivative expression involving them and the 't Hooft tensors. The unit-vector identity is verified here. Its identification with the derivative of the specific extended area must be derived independently; it does not follow from the rank-one factorization.

## Chirality and parity

Generic holomorphic rank-one matrices may have both $\lambda(z)$ and $\mu(z)$ varying. Pages 82–83 propose special sectors with one factor frozen. Factorization alone imposes no such restriction, and the failed extended-tensor identity cannot be used to derive it.

Suppose parity interchanges two well-defined functionals, $S_+[PC]=S_-[C]$ and $S_-[PC]=S_+[C]$. Then
$$
S[C]=\frac12(S_+[C]+S_-[C])
$$
is parity invariant by substitution. This is a conditional symmetry argument. It does not prove that the two functionals exist with all the required loop properties or that averaging their actions is the unique physical state construction. Averaging exponentials, for example, generally gives a different functional from exponentiating the average.

The source intends a parity-invariant vacuum at zero topological angle. Its chiral construction and its use in the spectrum remain proposals. The ordinary area and the extended area must be compared using explicit definitions and the same regulator; the spinor algebra does not prove a uniqueness theorem excluding other surface representations.

## Worked laboratory: an explicit Euclidean null factorization

Use $V(v)=v_4\,1+i(v_1\sigma_1+v_2\sigma_2+v_3\sigma_3)$. The Pauli identity gives
$$
\det V=v_4^2+v_1^2+v_2^2+v_3^2.
$$
The square here is complex bilinear. A nonzero null vector therefore gives a nonzero rank-one matrix, which factors as $V=\lambda\mu^T$. Conversely, every rank-one factorization has zero determinant.

For the circle tangent $v=(1/2,-i/2,0,0)$, direct substitution gives
$$
V=\begin{pmatrix}0&0\\i&0\end{pmatrix}
=\begin{pmatrix}0\\i\end{pmatrix}(1\quad0).
$$
The rescaling $(\lambda,\mu)\mapsto(c\lambda,c^{-1}\mu)$, $c\ne0$, leaves $V$ fixed. Equal spinor norms fix the magnitude of this redundancy where both spinors are nonzero; an opposite phase remains.

This is an exact local algebraic parametrization. Reality conditions, zeros, transition functions, the measure, and the existence of the intended surface remain additional problems. In particular it does not repair the extended tensor inconsistency found in III.5.

## Problem set

1. **Classroom core.** Check that the circle tangent is complex null.

2. **Self-study calculation.** Multiply the two spinors in the displayed factorization.

3. **Self-study interpretation.** Why is a real Euclidean null vector necessarily zero but this vector is not?

4. **Research extension.** Patch this factorization across zeros of a holomorphic tangent.

## Answer checkpoints

1. $(1/2)^2+(-i/2)^2=1/4-1/4=0$.

2. The outer product has the single nonzero entry $V_{21}=i$.

3. A real sum of squares is nonnegative; complex bilinear squares can cancel. The Hermitian norm of the example is $1/2$.

4. Completion: give local spinor choices, transition rescalings, and behavior near at least one zero. A pointwise rank-one factorization alone does not supply a global nonsingular measure.

## Teaching note

Use the decisive step in problem 2 as the written exit check for III.6; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-05-constructing-the-hodge-dual-surface|Previous note]] · [[mini-lecture-07-ope-matching-and-regge-physics|Next note]] · [[geometric-qcd-course-guide|Course guide]]
