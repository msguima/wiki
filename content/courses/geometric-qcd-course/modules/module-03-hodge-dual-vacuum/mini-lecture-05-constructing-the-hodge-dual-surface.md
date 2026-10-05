---
title: "Mini-Lecture III.5: Constructing the Hodge-Dual Surface"
type: lecture-notes
course: geometric-qcd-course-guide
module: 3
lecture: "III.5"
modified: 2026-10-05
---

# Mini-Lecture III.5: Constructing the Hodge-Dual Surface

*We study harmonic extension, conformality, and the tensor test. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** III.1–III.3; Fourier modes and complex differentiation. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); harmonic extension, conformality, and the tensor test (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked **Source reconstruction** explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 78-81. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 3|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 78-81.

## The problem and the order of the construction

We want a surface attached to a prescribed closed curve, a parametrization in which its equations simplify, and an area derivative with the duality required by III.2. These are separate tasks. We first solve the harmonic boundary problem, then test conformality, then test the proposed extended tensor. This calculation is the pedagogical pilot for the revised course.

## Fourier modes and the disk Dirichlet problem

Let $C(\theta)$ be a real smooth periodic vector with Fourier coefficients $C_n$:

$$
C(\theta)=C_0+\sum_{n>0}\left(C_ne^{in\theta}+\overline{C_n}e^{-in\theta}\right).
$$

Define the periodic Hilbert transform by $H[e^{in\theta}]=-i\,\operatorname{sgn}(n)e^{in\theta}$, with $H[1]=0$. It follows that $H[\cos n\theta]=\sin n\theta$ and $H[\sin n\theta]=-\cos n\theta$ for $n>0$.

The holomorphic extension is

$$
f(z)=\frac{C_0}{2}+\sum_{n>0}C_nz^n,\qquad
f(e^{i\theta})=\frac12(C+iHC).
$$

Taking its real part verifies $2\operatorname{Re}f(e^{i\theta})=C(\theta)$. The real map $Y=f+\bar f$ is harmonic because $\partial_z\partial_{\bar z}Y=0$. An imaginary constant in $f$ does not change $Y$ and is fixed here to zero.

Orthogonality of angular modes gives a useful normalization check:

$$
\int_D|f'(z)|^2\,dudv=\pi\sum_{n>0}n|C_n|^2.
$$

Indeed $\int_0^1r^{2n-2}r\,dr=1/(2n)$, which multiplies $2\pi n^2|C_n|^2$. With the stated Hilbert convention,

$$
\int_0^{2\pi} C'(\theta)\cdot HC(\theta)\,d\theta
=-4\pi\sum_{n>0}n|C_n|^2.
$$

Thus the disk integral is minus one quarter of this boundary integral. A sign or measure normalization imported from a source must pass the circle test below.

## Harmonic does not yet mean conformal

Write $z=u+iv$. Differentiation gives $Y_u=f'+\bar f'$ and $Y_v=i(f'-\bar f')$. Hence

$$
g_{uu}-g_{vv}=4\operatorname{Re}(f'\cdot f'),\qquad
g_{uv}=-2\operatorname{Im}(f'\cdot f').
$$

The induced metric is conformal in $(u,v)$ precisely when $f'\cdot f'=0$. In complex coordinates this is $g_{zz}=0$, while $g_{z\bar z}$ is generally nonzero. Notice that $f'\cdot f'$ is a complex bilinear square and $|f'|^2=f'\cdot\bar f'$ is a positive Hermitian norm.

## Worked example: the circle

Take $C(\theta)=(R\cos\theta,R\sin\theta,0,0)$. Its only positive Fourier mode is $(R,-iR,0,0)/2$, so

$$
f(z)=\frac R2(z,-iz,0,0),\qquad
Y(u,v)=(Ru,Rv,0,0).
$$

Then $f'\cdot f'=R^2(1+(-i)^2)/4=0$ and $|f'|^2=R^2/2$. The metric is $R^2(du^2+dv^2)$, the ordinary disk area is $\pi R^2$, and $\int_D|f'|^2=\pi R^2/2$. Also $\int C'\cdot HC=-2\pi R^2$, confirming the factor and sign above.

The Dirichlet energy $E_D=\frac12\int_D(|Y_u|^2+|Y_v|^2)$ equals $2\int_D|f'|^2=\pi R^2$. Conformality makes the Dirichlet energy equal to the ordinary area in this example.

## Worked counterexample: a fixed ellipse parametrization

Now take $C(\theta)=(a\cos\theta,b\sin\theta,0,0)$ with positive $a,b$. The same harmonic construction gives

$$
f(z)=\frac12(az,-ibz,0,0),\quad
f'\cdot f'=\frac{a^2-b^2}{4},\quad
Y(u,v)=(au,bv,0,0).
$$

Unless $a=b$, the map is not conformal: $g_{uu}=a^2$, $g_{vv}=b^2$, $g_{uv}=0$. Its image is the filled ellipse with area $\pi ab$, but

$$
E_D=\frac{\pi}{2}(a^2+b^2),\qquad
E_D-A=\frac{\pi}{2}(a-b)^2.
$$

For $a=2$, $b=1$, the excess is $\pi/2$. No numerical minimizer is needed to see the failure. Holomorphic extension of an arbitrarily parametrized boundary does not enforce the null constraint.

## What boundary reparametrization must do

For the geometric contour rather than its fixed labeling, replace $C(\theta)$ by $C(\phi(\theta))$, with $\phi$ an orientation-preserving boundary homeomorphism in an appropriate regularity class. Harmonic extension then depends on $\phi$. The Plateau–Douglas variational problem also varies that boundary correspondence; it is not exhausted by one Hilbert transform.

A computational approximation uses a finite Fourier representation of $\phi$, fixes the disk's conformal automorphism freedom, and minimizes the harmonic energy while checking monotonicity and convergence. The conformal residual $\|f'\cdot f'\|$ must decrease together with the energy. A change of coordinates cannot be invoked to claim that a fixed, nonconformal harmonic map already satisfies the constraint.

## The extended tensor: an additional source consistency test

Slides 78–79 define, with $\epsilon_{1234}=1$,

$$
\eta^{\chi,i}_{\mu\nu}
=\delta_{i\mu}\delta_{\nu4}-\delta_{i\nu}\delta_{\mu4}
+\chi\epsilon_{i\mu\nu4},\quad
X^i_\mu=\eta^{\chi,i}_{\mu\nu}Y_\nu,\quad
\Sigma_{\mu\nu}=\sum_i
(\partial_uX^i_\mu\partial_vX^i_\nu-\partial_vX^i_\mu\partial_uX^i_\nu).
$$

The source asserts that this construction yields a $\chi$-self-dual tensor. We can test the literal formulas on the unit circle map $Y=(u,v,0,0)$, which already satisfies the null condition.

For $\chi=+1$, the ordered tangent pairs $(X^i_u,X^i_v)$ are

$$
(-e_4,-e_3),\qquad(e_3,-e_4),\qquad(-e_2,e_1).
$$

Their bivectors are $-e_3\wedge e_4$, $-e_3\wedge e_4$, and $e_1\wedge e_2$. Consequently,

$$
\Sigma=e_1\wedge e_2-2e_3\wedge e_4,\qquad
*\Sigma=e_3\wedge e_4-2e_1\wedge e_2\ne\Sigma.
$$

For $\chi=-1$ the second coefficient changes sign, giving $\Sigma_{12}=1$, $\Sigma_{34}=2$, which likewise fails $*\Sigma=-\Sigma$. Reversing orientation changes signs but does not repair the unequal magnitudes. The accompanying verification script performs these contractions directly from the displayed Kronecker and epsilon formula.

Thus the claimed automatic duality does not follow from the literal definitions supplied in the slides. A missing projection or a changed definition might be intended, but inserting one would alter the construction and would require a new variation of the area and boundary terms. We leave that research step open. A general statement about Kähler forms does not repair this explicit tensor calculation.

## Worked laboratory: a second Fourier mode

For one real component $C(\theta)=A\cos(n\theta)$, $n>0$, the positive coefficient is $C_n=A/2$. Thus $f(z)=Az^n/2$ and
$$
\int_D|f'|^2=\frac{\pi nA^2}{4}.
$$
Direct integration of $|Anz^{n-1}/2|^2$ gives the same result. The energy grows linearly with the boundary frequency at fixed amplitude. Harmonic extension damps the mode in the interior as $r^n$, but high-frequency boundary data still cost more Dirichlet energy.

This extension solves the scalar boundary problem. It supplies no automatic cancellation of a vector map's bilinear null constraint.

## What is established

The Fourier extension, metric identities, circle, ellipse, and tensor counterexample are exact calculations under the declared conventions. They establish a source consistency problem, not a proof that no geometric construction can work. The proposed area normalization, self-dual area derivative, and exact QCD zero mode remain conditional until that problem and the boundary variational problem are resolved.

> **Physical picture.** Harmonic extension smooths the boundary data into the disk. Conformality balances the two tangent directions. Hodge duality constrains a spacetime two-form. Solving one of these problems does not solve the other two.

## Looking ahead

III.6 can still teach factorization of a complex null vector as an exact algebraic result. Its interpretation as the parametrization of this particular QCD vacuum retains the limitation identified here.

<!-- generated-figures -->
## Figures for the calculation

![[geometric-qcd-circle-ellipse.svg|Images of a disk coordinate grid under the stated harmonic maps. For the ellipse the two tangent lengths differ; a separate boundary correspondence is needed for conformality.]]

![[geometric-qcd-source-tensor-test.svg|Direct substitution of the unit-circle map into the literal extended tensor. The tensor and its proposed duality transform disagree for either chirality.]]

<!-- /generated-figures -->

## Problem set

1. **Classroom core.** Find the disk integral for $A=2$, $n=3$.

2. **Self-study calculation.** Compute $E_D-A$ for the ellipse with $a=2$, $b=1$.

3. **Self-study interpretation.** Does imposing the circle's null condition repair the source tensor identity?

4. **Research extension.** Investigate a possible repair of the extended tensor definition.

## Answer checkpoints

1. It is $3\pi$.

2. $E_D=5\pi/2$, $A=2\pi$, and the excess is $\pi/2$.

3. No. The circle already has $f'\cdot f'=0$, yet the literal extended tensor has $(\Sigma_{12},\Sigma_{34})=(1,-2)$ for $\chi=+1$, so it is not self-dual.

4. Completion: state the changed definition, recompute its duality and area variation, and check the same boundary example. Adding a projection without redoing the variational argument is not a verified repair.

## Teaching note

Use the decisive step in problem 2 as the written exit check for III.5; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-04-physical-vacuum-and-instanton-language|Previous note]] · [[mini-lecture-06-twistor-factorization-and-parity|Next note]] · [[geometric-qcd-course-guide|Course guide]]
