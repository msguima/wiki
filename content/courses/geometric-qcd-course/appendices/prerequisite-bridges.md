---
title: "Prerequisite bridges — Geometric QCD"
type: appendix
course: geometric-qcd-course-guide
modified: 2026-10-05
---

# Prerequisite bridges

These short calculations prepare the operations used later. Work the diagnostic before reading its answer. A missed check points to a specific bridge to revisit.

## 1. Matrix algebra and Gaussian integrals

For finite matrices, $\operatorname{tr}(AB)=\operatorname{tr}(BA)$ follows by exchanging the two summed indices. It does not imply $\operatorname{tr}(AB)=\operatorname{tr}A\,\operatorname{tr}B$. With $A=B=\sigma_3$, the left side is $2$ and the right side is zero.

The Pauli matrices satisfy $\sigma_i\sigma_j=\delta_{ij}1+i\epsilon_{ijk}\sigma_k$. Therefore $(p\cdot\sigma)^2=p^2 1$ for real $p$, since the antisymmetric epsilon contraction with $p_ip_j$ vanishes. This is the finite version of the gamma-algebra step in the Dirac resolvent.

For $a>0$, completing the square gives
$$
\int_{\mathbb R}e^{-ax^2/2+jx}\,dx
=\sqrt{\frac{2\pi}{a}}e^{j^2/(2a)}.
$$
For real $j$ the shifted Gaussian is immediate. Imaginary $j$ gives the Fourier transform by analytic continuation of this convergent Gaussian identity. Differentiating in $j$ at zero gives $\langle x^2\rangle=1/a$.

**Diagnostic.** Compute $\operatorname{tr}[\sigma_1,\sigma_2]$ and $\operatorname{tr}(\sigma_3[\sigma_1,\sigma_2])$; then find the variance of a normalized weight $e^{-2x^2}$.

**Answer.** The commutator is $2i\sigma_3$, so the traces are zero and $4i$. The Gaussian has $a=4$, hence variance $1/4$.

## 2. Fourier transforms and distributions

A distribution is defined by its action on test functions. For the delta, $\int\delta(x)\varphi(x)\,dx=\varphi(0)$; for its derivative, $\int\delta'(x)\varphi(x)\,dx=-\varphi'(0)$. These are definitions, not evaluations of an infinite function at a point.

For $\widehat f(p)=\int e^{ipx}f(x)\,dx$, integration by parts gives $\widehat{f'}=-ip\widehat f$. A normalized Gaussian of variance $\epsilon$ has transform $e^{-\epsilon p^2/2}$ and tends to the delta against smooth test functions.

In four dimensions a radial integral uses $d^4x=2\pi^2r^3dr$. Thus normalization cannot be read off from the one-dimensional graph of a radial kernel. IV.6 uses precisely this measure.

**Diagnostic.** Normalize $Ae^{-ar}$ on $\mathbb R^4$, $a>0$.

**Answer.** Its integral is $2\pi^2A(3!)/a^4=12\pi^2A/a^4$. Unit normalization requires $A=a^4/(12\pi^2)$. At $a=2m$ this gives $4m^4/(3\pi^2)$.

## 3. Linear systems and proof by certificate

The equation $Ax=b$ asks whether $b$ lies in the column space of $A$. Row reduction must act on the augmented matrix, since a zero row in $A$ can carry a nonzero right-hand side. A witness $y^TA=0$, $y^Tb\ne0$ proves inconsistency in one multiplication.

More equations than unknowns does not imply failure. Duplicate equations add no rank. Fewer equations than unknowns does not guarantee success either: a row $0=1$ is impossible at any size.

**Diagnostic.** Solve $x+y=1$, $2x+2y=2$, and then replace the second right-hand side by $3$.

**Answer.** Initially $(x,y)=(t,1-t)$ for arbitrary $t$. After the change, subtracting twice the first equation gives $0=1$. The witness is $(-2,1)$.

## 4. Forms, Hodge star, and complex boundary data

A two-form is $B=\frac12B_{\mu\nu}dx^\mu\wedge dx^\nu$ with antisymmetric components. In oriented Euclidean four-space, $*dx^{12}=dx^{34}$ and $*dx^{13}=-dx^{24}$. The sign is determined by the orientation of the complementary pair.

The bilinear square of a complex vector differs from its Hermitian norm. For $v=(1,i)$, $v\cdot v=0$, but $v^\dagger v=2$. This is the distinction in the conformal null constraint.

A real boundary function $C(\theta)=A\cos n\theta$ has holomorphic extension $f(z)=Az^n/2$ with $2\operatorname{Re}f=C$. Its real harmonic extension damps the mode by $r^n$. A vector of such harmonic functions need not be a conformal parametrization; III.5 checks this explicitly.

**Diagnostic.** Is $dx^{12}$ self-dual? Does $f(z)=(2z,-iz)/2$ satisfy $f'\cdot f'=0$?

**Answer.** No to both. The star of $dx^{12}$ is $dx^{34}$, and the complex square is $(4-1)/4=3/4$.

## 5. Grassmann variables and Gaussian integrals

Grassmann generators obey $\theta_i\theta_j=-\theta_j\theta_i$, so $\theta_i^2=0$. Integration selects the coefficient of the generator: $\int d\theta\,1=0$ and $\int d\theta\,\theta=1$. An orientation of the multiple integration measure fixes all overall signs.

For a single pair, $(\bar\theta\theta)^2=0$. For $B=\bar\theta_1\theta_1+\bar\theta_2\theta_2$, however, the even bilinears commute and $B^2=2\bar\theta_1\theta_1\bar\theta_2\theta_2$ need not vanish. “Grassmann” alone does not imply that every composite squares to zero.

The alternating pairings of a real antisymmetric quadratic form define its Pfaffian. For four variables, $\operatorname{Pf}A=A_{12}A_{34}-A_{13}A_{24}+A_{14}A_{23}$. Squaring it gives the determinant.

**Diagnostic.** If only $A_{12}=2$ and $A_{34}=3$ are nonzero above the diagonal, find the Pfaffian and determinant.

**Answer.** They are $6$ and $36$. The matrix consists of two independent antisymmetric blocks.

## 6. Variations and boundary terms

For a scalar field,
$$
\delta\int_D\frac12|\nabla\rho|^2
=-\int_D\Delta\rho\,\delta\rho
+\int_{\partial D}\partial_n\rho\,\delta\rho.
$$
The first term determines the bulk equation. The second either vanishes because the boundary values are fixed or combines with a boundary action to determine a natural boundary equation. The two choices describe different variational problems.

**Diagnostic.** Vary $\int_D[\frac12|\nabla\rho|^2+\sigma e^{2\rho}]+\int_{\partial D}me^\rho$ with free boundary data.

**Answer.** The bulk equation is $-\Delta\rho+2\sigma e^{2\rho}=0$ and the boundary equation is $\partial_n\rho+me^\rho=0$. The coefficients in V.4 differ because its kinetic normalization differs.

## 7. Stationary phase, exactness, and fit statistics

A Gaussian saddle is exactly integrable. Adding higher powers of the fluctuation generally adds corrections, even when the Hessian is large. Real stationary trajectories and exact quantization are therefore distinct claims.

A fit residual $r_i=(M_i^{\mathrm{model}}-M_i^{\mathrm{obs}})/M_i^{\mathrm{obs}}$ is dimensionless. Its unweighted RMS is $\sqrt{\sum_i r_i^2/n}$. Experimental error bars enter a different statistic, such as a specified chi-squared. A model error estimate is another distinct input.

**Diagnostic.** For residuals $(0.1,-0.2)$, calculate the RMS. Is it held-out evidence if both points were used to choose the parameters?

**Answer.** The RMS is $\sqrt{0.025}\simeq0.1581$. It is an in-sample diagnostic when both points were fitted.
