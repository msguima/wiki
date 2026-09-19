---
title: "Optional — Linearized learning and the interpolation peak"
type: supplementary-notes
course: nn-llm-syllabus
status: draft
modified: 2026-09-19
---

# Linearized learning and the interpolation peak

This supplement to [[week-04-gardner-capacity|Week 4]] has no assigned lecture
hours in the current syllabus. It separates existence, training and fresh-data
prediction in models simple enough to calculate. See Chapter 2 §2.5 in
[[nn-llm-resources|the companion notes]] for the longer treatment and
[[nn-llm-bibliography]] for the underlying literature.

## A fixed feature map turns training into a matrix equation

Let $f_\theta(x)$ be a scalar prediction. Near initial parameters $\theta_0$,
a first-order expansion is

$$
f_\theta(x)\simeq f_{\theta_0}(x)+\phi(x)^{\mathsf T}(\theta-\theta_0),
 \qquad \phi(x)=\nabla_\theta f_{\theta_0}(x).
$$

The components of $\phi(x)$ measure how each parameter changes the initial
prediction. In this **linearized model** they are held fixed. On $P$ training
examples define $r_\mu=f_\theta(x^\mu)-y^\mu$ and use loss
$\mathcal L=\tfrac12\sum_\mu r_\mu^2$. Gradient flow is
$\dot\theta=-\sum_\mu\phi(x^\mu)r_\mu$. Differentiating each residual gives

$$
\dot r_\nu=-\sum_\mu K_{\nu\mu}r_\mu,\qquad
 K_{\nu\mu}=\phi(x^\nu)^{\mathsf T}\phi(x^\mu),\qquad
 r(t)=e^{-Kt}r(0).
$$

$K$ is a Gram matrix and is positive semidefinite. It is called the **neural
tangent kernel** on these observations. An eigenmode with eigenvalue $\lambda$
decays as $e^{-\lambda t}$; a zero mode cannot be fitted by this feature map.
Using the mean loss instead rescales time by $P$.

For example, with $K=\operatorname{diag}(2,0)$ and $r(0)=(1,1)$,
$r(t)=(e^{-2t},1)$. One error can decrease while the other remains. This
solution is exact for the fixed-feature model. In the nonlinear network the
features generally move, so a small measured kernel drift is needed to use
it as a controlled approximation. Small parameter motion alone, without a
scale and derivative bound, does not establish small output error.

## A noisy linear teacher

Take $x^\mu\in\mathbb R^N$ with independent standard Gaussian components and
observations $y^\mu=w_*\cdot x^\mu+\sigma\epsilon^\mu$, with independent
unit Gaussian $\epsilon^\mu$. Fit by least squares, choosing the minimum-norm
solution when several minimizers exist. Define the signal-prediction risk
on a fresh independent input by

$$
R=\mathbb E_x[((\widehat w-w_*)\cdot x)^2]
 =\|\widehat w-w_*\|^2.
$$

This excludes the fresh observation's own noise variance $\sigma^2$.
In the proportional limit $P,N\to\infty$, $\alpha=P/N\ne1$, with a
fixed signal norm, the asymptotic risk for this isotropic ensemble is

$$
R(\alpha)=\begin{cases}
 \|w_*\|^2(1-\alpha)+\dfrac{\sigma^2\alpha}{1-\alpha},&0<\alpha<1,\\
 \dfrac{\sigma^2}{\alpha-1},&\alpha>1.
 \end{cases}
$$

This random-matrix result is quoted with its assumptions, rather than derived
here. Below one, the unseen component of the teacher contributes the first
term, and fitting observation noise contributes the second. At nonzero noise
the risk diverges near one because the nearly singular design matrix
amplifies that noise. This is an asymptotic statement, not an infinity in
every finite training run.

For $0<\sigma<\|w_*\|$, differentiating the lower branch gives an interior
minimum:

$$
R'(\alpha)=-\|w_*\|^2+\frac{\sigma^2}{(1-\alpha)^2}=0,
\qquad \alpha_*=1-\frac{\sigma}{\|w_*\|}.
$$

With $\|w_*\|=1$ and $\sigma=0.3$, $\alpha_*=0.7$ and $R=0.51$.
If $\sigma\ge\|w_*\|$, there is no interior minimum in $0<\alpha<1$.
If $\sigma=0$, there is no noise divergence: the lower branch decreases to
zero, and sufficiently many noiseless independent equations identify the
teacher. These qualifications are essential to interpreting the curve.

The interpolation threshold at one concerns real equations in this Gaussian
linear model. Cover's threshold at two concerns random sign constraints in
general position. Their values do not define a universal ratio for other
models or data distributions.

**Checkpoint.** Does zero training error imply zero risk? No. For
$\alpha=0.5$, signal norm one and $\sigma=0.3$, interpolation is possible
while $R=0.5+0.09=0.59$. Fitting observed labels and predicting an unseen
signal are different questions.
