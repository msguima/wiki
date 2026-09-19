---
title: "Week 1 — Inferring a distribution from observations"
type: lecture-notes
course: nn-llm-syllabus
semester: 1
week: 1
unit: 0
duration: "4 hours (2 hr lecture + 2 hr practical)"
status: draft
modified: 2026-09-19
---

# Week 1 — Inferring a distribution from observations

Suppose the same text fragment is followed by $A$ three times and by $B$ once.
What probabilities should a model assign on the next occurrence? The first
step toward an LLM is to make this small inference explicit. The architecture
will later supply a much richer dependence on the preceding text.

Course: [[nn-llm-syllabus]]. Overview: [[nn-llm-start-here]].
Authorship and supervision: [[ai-authorship]].

## Learning goals and reading

By the end of the page you should be able to fit a two-outcome distribution,
perform one parameter update, distinguish sample loss from expected loss, and
turn arbitrary real scores into probabilities. The derivations below require
only elementary probability and differentiation.

For more exercises, see [[nn-llm-resources|the companion notes]], Chapter 1,
§§1.1–1.4. Shannon's papers are listed in [[nn-llm-bibliography]].

## 1. What is observed, and what is adjusted?

A **token** is a chosen unit of text, such as a character, word or word part.
The **vocabulary** is the finite set of possible tokens. A **corpus** is a
collection of observed texts. The **context** is the part already supplied,
and the **target** is the next token that was actually observed.

For now hold the context fixed and use only two possible targets. Write
$A\leftrightarrow s=+1$ and $B\leftrightarrow s=-1$. Introduce a real
adjustable **parameter** $\theta$ and define

$$
p_\theta(s)=\frac{e^{\theta s}}{Z(\theta)},\qquad
 Z(\theta)=e^\theta+e^{-\theta}=2\cosh\theta.
$$

This is the familiar two-state Gibbs formula. Here $s$ labels a token and
$\theta$ is adjusted from observations; no magnetic moment or heat bath is
being assumed. Positive $\theta$ favours $A$, and $\theta=0$ gives equal
probabilities. We know how to compute the mean given a field:
$\langle s\rangle_\theta=\partial_\theta\log Z=\tanh\theta$.
Fitting asks for the field that reproduces an observed mean.

## 2. Why minimize a logarithmic loss?

Treat the $M$ targets in this one-context example as independent draws.
If $n_+$ of them are positive and $n_-$ negative, their **likelihood** is

$$
\prod_{m=1}^M p_\theta(s_m)
 =p_\theta(+)^{n_+}p_\theta(-)^{n_-},\qquad M=n_++n_-.
$$

The likelihood is a function of the parameter for the fixed observed data.
We choose a parameter that makes those observations probable. Taking a
logarithm preserves the maximizing value and turns the product into a sum.
Changing the sign turns maximization into minimization. Dividing by $M$
makes the scale comparable across sample sizes. The resulting **loss** is

$$
\widehat{\mathcal L}(\theta)
 =-\frac1M\sum_{m=1}^M\log p_\theta(s_m)
 =\log(2\cosh\theta)-\theta\widehat m,\qquad
 \widehat m=\frac{n_+-n_-}{M}.
$$

The hat marks a quantity computed from a finite sample. Natural logarithms
give units of **nats**. Differentiate only $\theta$; the observations stay fixed:

$$
\widehat{\mathcal L}'=\tanh\theta-\widehat m,\qquad
 \widehat{\mathcal L}''=1-\tanh^2\theta
 =\operatorname{Var}_\theta(s)>0.
$$

The stationary condition is mean matching. For $n_+,n_->0$ the unique minimum is

$$
\tanh\theta_*=\widehat m,\qquad
 \theta_*=\frac12\log\frac{n_+}{n_-},\qquad
 p_{\theta_*}(+)=\frac{n_+}{M}.
$$

For three $A$'s and one $B$, $\widehat m=1/2$, $\theta_*=\tfrac12\log3
\simeq0.549306$, and $p_{\theta_*}(A)=3/4$. The loss falls from $\log2
\simeq0.693147$ at $\theta=0$ to $0.562335$ nats. If one count is zero,
the optimal probability is on the boundary and requires an infinite field;
there is no finite minimizing $\theta$.

### One step toward the fit

**Gradient descent** adjusts a parameter against the derivative of its loss:

$$
\theta_{r+1}=\theta_r-\eta\widehat{\mathcal L}'(\theta_r),\qquad \eta>0.
$$

The **learning rate** $\eta$ sets the step size; $r$ counts updates. Starting
at zero with $\eta=1$, the three-to-one sample gives $\theta_1=1/2$ and
$p_{\theta_1}(A)=1/(1+e^{-1})\simeq0.731059$. The prediction moves toward
the observed frequency because the predicted mean was too small.

Since $\widehat{\mathcal L}''\le1$, Taylor's inequality gives

$$
\widehat{\mathcal L}(\theta-\eta g)
 \le \widehat{\mathcal L}(\theta)-\eta(1-\eta/2)g^2,
 \qquad g=\widehat{\mathcal L}'(\theta).
$$

Thus $0<\eta<2$ guarantees a decrease away from a stationary point for this
loss. This bound uses the maximum susceptibility of the two-state model.
It is not a universal learning-rate prescription for a neural network.

## 3. The source, and what a finite sample can tell us

A **source** is an idealized distribution $q(c,x)$ over contexts $c$ and
next tokens $x$. A model supplies $p_\theta(x\mid c)$. Its **expected loss**
averages over fresh draws from that source:

$$
\mathcal L(\theta)=-\sum_{c,x}q(c,x)\log p_\theta(x\mid c).
$$

Add and subtract $\log q(x\mid c)$ inside the sum:

$$
\begin{aligned}
\mathcal L(\theta)
&=-\sum_{c,x}q(c,x)\log q(x\mid c)
 +\sum_{c,x}q(c,x)\log\frac{q(x\mid c)}{p_\theta(x\mid c)}\\
&=H_q(X\mid C)+\sum_cq(c)D\big(q(\cdot\mid c)\Vert p_\theta(\cdot\mid c)\big).
\end{aligned}
$$

Here $H_q$ is the source's conditional entropy and
$D(q\Vert p)=\sum_xq_x\log(q_x/p_x)$ is relative entropy. The convention
$0\log0=0$ is understood; if the model assigns zero probability to an event
of positive source probability, the loss is infinite. Concavity of the
logarithm gives $D\ge0$, with equality only for identical distributions.

The source entropy does not depend on the model parameters. The remaining
term measures mismatch. Reducing **expected** loss is therefore exactly
reducing this mismatch. Training instead reduces a **sample** loss; whether
that improves fresh predictions is a separate question called
**generalization**. This is why observations kept out of fitting, called
**test data**, are useful.

### A finite test loss can lie below the entropy

Take a fair source $q=(1/2,1/2)$ and a fixed model $p=(3/4,1/4)$.
Its expected loss is $-\tfrac12\log(3/4)-\tfrac12\log(1/4)
\simeq0.836988$, larger than $H(q)=\log2$ as required.
But an independent test sample of four draws can contain three $A$'s and
one $B$, with probability $4/16=1/4$. Its sample loss is $0.562335$,
which is below $\log2$. There is no contradiction: the entropy bound applies
to the source average, not to each finite sample.

The model's own entropy, $H(p)=-\sum_xp_x\log p_x$, is yet another average.
It happens to equal $0.562335$ here because the sample frequencies equal
$p$. The general cross-entropy decomposition contains **$H(q)$**, not $H(p)$.

## 4. From two outcomes to a vocabulary: softmax

For each possible next token $x$, let the model produce a real **score** or
**logit** $z_x(c)$. A score is not a probability. The **softmax** map makes
these scores positive and normalized:

$$
p_\theta(x\mid c)=\frac{e^{z_x(c)}}{\sum_y e^{z_y(c)}}.
$$

With scores $(\log3,0)$ for $(A,B)$, softmax gives $(3/4,1/4)$, the same
fit as before. Adding any common constant to both scores leaves the result
unchanged. Only score differences affect the probabilities.

The logarithm of the denominator is the **log-sum-exp** function. For later
use allow a positive scale $\beta$:

$$
\operatorname{lse}_\beta(z)=\frac1\beta\log\sum_xe^{\beta z_x},\qquad
 \frac{\partial\operatorname{lse}_\beta}{\partial z_x}
 =\frac{e^{\beta z_x}}{\sum_y e^{\beta z_y}}.
$$

At $\beta=1$, the loss for one observed target $y$ is
$\ell=\operatorname{lse}_1(z)-z_y$. Its derivative is

$$
\frac{\partial\ell}{\partial z_x}=p_x-\mathbf1_{x=y}.
$$

The indicator is one for the observed token and zero otherwise. This is the
multiclass version of the predicted-minus-observed mean in §2, and it is the
starting point for training a decoder in [[week-10-gradients-and-generation|Week 10]].

Setting $E_x=-z_x$ makes softmax a Gibbs measure at unit inverse temperature:
$F=-\log\sum_xe^{-E_x}$ and $\ell=E_y-F$. The identity lets us use partition
function derivatives. It does not supply a heat bath, an equilibrium dynamics
or a thermodynamic limit. Convexity in the scores also does not imply
convexity in the weights of the network that produces them.

## 5. A sequence, context and perplexity

For a sequence $x_1,\ldots,x_T$, probability's chain rule gives

$$
p_\theta(x_1,\ldots,x_T)=\prod_{t=1}^T
 p_\theta(x_t\mid x_1,\ldots,x_{t-1}).
$$

No independence between successive tokens is assumed. Taking $-\log$ and
dividing by $T$ yields the mean next-token loss. During training these
contexts come from observed text. During generation the chosen tokens are
appended to form subsequent contexts, while the parameters remain fixed.

**Perplexity** is $\exp(\widehat{\mathcal L})$, the inverse geometric mean
probability assigned to observed targets. For an ideal predictor of $k$
equally likely alternatives it equals $k$. With mismatch it is not a literal
count: a model $(0.9,0.1)$ on a fair source has population cross-entropy
$-\tfrac12\log(0.09)$ and its exponential is $10/3>2$.

For ideal predictors, the benefit of context is exactly

$$
H_q(X)-H_q(X\mid C)=I_q(X;C)\ge0.
$$

An imperfect model may fail to realize that benefit. [[week-02-transfer-matrix-and-finite-text|Week 2]] computes it for a source whose correlations are known.

## Checkpoints with answers

**1. Which quantity is fixed in the derivative of the sample loss?**
The observed mean $\widehat m$. Only $\theta$ is varied. Differentiating the
data as though they changed with the model would solve a different problem.

**2. Why is a highly confident model not necessarily accurate?**
Concentration makes $H(p)$ small, but a wrong confident prediction has a large
$-\log p_y$. Accuracy concerns an average over observations, not over the
model's preferred outcomes.

**3. Does a test loss below $H_q(X\mid C)$ prove an error?**
No. The four-draw example above gives a counterexample with a known nonzero
probability. Repeated independent test samples estimate the expected loss;
one fluctuation does not change its bound.

**4. What changes if all vocabulary scores increase by ten?**
Nothing in the probabilities or loss: the common factor $e^{10}$ cancels.
This is the freedom to choose an effective energy zero.

## What the week establishes

Maximum likelihood gives a concrete loss and a mean-matching condition.
Softmax generalizes the two-state construction to any finite vocabulary.
The source-average loss separates irreducible uncertainty from model
mismatch. These exact identities will remain true when a neural network
produces the scores; the difficulty will lie in estimating and optimizing them.

## The practical session

A guided calculation with no programming prerequisite, followed by the first
browser experiment, which runs without installation.

**Varied:** the observed proportion $\widehat m$, the initial parameter
$\theta$, and the step size $\eta$.
**Held fixed:** the family of distributions and the fitting criterion.
**Measured:** the loss curve against the analytic optimum $\theta_*$, and
whether a step with $\eta$ at or above $2$ behaves as the bound predicts.

**Product:** the fitted $\theta_*$ for at least three samples, checked against
$\tfrac12\log(n_+/n_-)$, plus one worked instance of a step size that fails and
an explanation of why the bound permitted it to.

---

## Connections to other parts of the wiki

- [[week-02-transfer-matrix-and-finite-text|Week 2]] takes this two-state
  system and makes its context a preceding token, which turns the fit into a
  transfer matrix.
- The relative entropy of §3 is the classical case of the quantity that
  appears in the group's research as the
  [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] of states
  on a von Neumann algebra, catalogued in the
  [[relative-entropy-qft|relative-entropy area page]] — the same quantity in
  different settings, classical and algebraic, and no more than that.
- The decomposition of §3 returns in Week 12 for the single-site conditionals
  of a Potts model, and in Week 14, where the same inequality is what makes a
  variational bound a bound.
- nn-llm-unit-0 — the block skeleton this note implements.
- [[nn-llm-conventions]] — notation, including the symbols that carry more
  than one meaning.

---

[[nn-llm-start-here|Start here]] · [[nn-llm-week-map|All weeks]] · [[nn-llm-resources|Book and experiments]] · [[week-02-transfer-matrix-and-finite-text|Next week]]
