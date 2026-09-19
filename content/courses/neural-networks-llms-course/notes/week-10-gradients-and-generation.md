---
title: "Week 10 — Gradients, stochastic updates, generation"
type: lecture-notes
course: nn-llm-syllabus
semester: 1
week: 10
unit: 2
duration: "4 hours (2 hr lecture + 2 hr laboratory)"
status: draft
modified: 2026-09-19
---

# Week 10 — Gradients, Stochastic Updates, Generation

*Notes for [[nn-llm-syllabus|the neural-networks course]], Unit 2. Written by an AI assistant under the researcher's supervision; see ai-authorship.*

*The decoder now supplies a probability for an observed next token. We
will differentiate its loss, trace the error signal through its layers and
understand why training updates fluctuate when they use subsets of the data.
We then hold the learned parameters fixed and generate a sequence.*

---

## Learning goals

1. **Derive** the backward recursion for the sensitivities and say why a
   shared parameter receives a sum.
2. State what the diffusion approximation to stochastic gradient descent
   matches, and what it therefore does not control.
3. Give the condition under which a single effective temperature describes the
   parameter fluctuations.
4. Distinguish the negative log probability of a generated path from an action
   and from entropy production.

## Reading

**Primary text.** Chapter 3, §3.6 and §3.7.

**Primary literature**, through [[nn-llm-bibliography|the bibliography]]:
Mandt, Hoffman and Blei for the diffusion approximation and the role of its
assumptions.

**Prerequisites.** [[week-09-four-indices|Week 9]] for the index this week
runs along. [[week-01-inferring-a-distribution|Week 1]] for the loss and the
decoding temperature.

## One prediction becomes one training example

In [[week-08-one-head-and-a-decoder|Week 8]], the context $AB$ produced
$p(B\mid AB)=0.792412$. If the observed next token is $B$, the output-score
derivatives are $(p_A,p_B-1)\simeq(0.207588,-0.207588)$. A gradient step
lowers the score of $A$ and raises the score of $B$. That is the local error
signal whose influence we now trace back through the decoder.

## 1. Differentiating the finished function

Training uses observed next tokens as targets, and the causal mask is what
makes that consistent: all positions of a fixed sequence can be evaluated
together, because their inputs are known and the representation at position $t$ may use only $x_{\le t}$ to
predict the observed target $x_{t+1}$. The
practice is called **teacher forcing**, and the mask is what keeps the
training task the same as the generation task.

Every intermediate state depends on the parameters, so the loss derivative
must be propagated backward through them. Define the sensitivity of the loss
to a state; then a perturbation of that state reaches the loss only through
the next state, so its effect is the effect at the next state composed with
the map that carries it there. That is the backward recursion, and organizing
these products from the output toward the input is **backpropagation**.

Write a layer as $h^{\ell+1}=F_\ell(h^\ell,\theta_\ell)$, using column
coordinates here for the vectorized state. Let
$\delta^\ell=\nabla_{h^\ell}\mathcal L$. The chain rule gives

$$
\delta^\ell=(D_hF_\ell)^{\mathsf T}\delta^{\ell+1},\qquad
 \nabla_{\theta_\ell}\mathcal L=(D_\theta F_\ell)^{\mathsf T}\delta^{\ell+1}.
$$

If the same parameter is used in several layers, add the contributions from
all its uses. For example, $h_1=wx$, $h_2=wh_1=w^2x$ and
$\mathcal L=\tfrac12(h_2-y)^2$ give

$$
\frac{d\mathcal L}{dw}=2wx(w^2x-y).
$$

At $w=2,x=y=1$, this is $12$. Counting only the last use gives $6$:
half the derivative is missing. Backpropagation keeps both paths.

For an output distribution $p_a$ and observed label $y$, the boundary
condition is $\partial\ell/\partial z_a=p_a-\mathbf1_{a=y}$, derived in
Week 1. Together with the decoder equations and these chain rules, that
specifies how every differentiable component contributes to training.

> **Physical picture.** The backward recursion is an adjoint equation, and in
> the continuous limit of Week 9 it becomes one literally — integrated
> backwards from a terminal condition, with the transpose of the linearized
> forward map as its generator. A physicist has met this as the equation for a
> response function or a Green's function propagating backwards from where the
> observable sits. The forward pass carries the state; the backward pass
> carries the sensitivity of a single scalar to every state along the way, and
> the two are related by the same transpose that relates a propagator to its
> adjoint.

## 2. What makes a gradient update stochastic

The empirical loss is an average over examples, and a **mini-batch** is the
subset used to estimate its derivative in one update. The noise comes from
which examples were sampled. A **batch** contains the $B$ examples used
in one update; an **epoch** is one pass through a dataset. For independent
sampling with replacement at fixed parameters, let the covariance of one
example's gradient be $C$. Then

$$
\widehat g_B=\nabla\widehat{\mathcal L}+\zeta,\qquad
 \mathbb E\zeta=0,\qquad \operatorname{Cov}(\zeta)=C/B,\qquad
 \theta_{n+1}=\theta_n-\eta\widehat g_B.
$$

This is **stochastic gradient descent**. Its exact one-step conditional mean
and covariance are $-\eta\nabla\widehat{\mathcal L}$ and $\eta^2C/B$.

A small-step diffusion approximation uses the time increment $ds=\eta$:

$$
d\theta=-\nabla\widehat{\mathcal L}\,ds
 +\sqrt{\eta/B}\,C^{1/2}dW_s.
$$

Its frozen-coefficient increments match the two discrete moments above.
Approximating a whole trajectory additionally requires small steps, regular
coefficients and control of the batch-noise statistics. Matching moments is
not an equality of processes.

Near a quadratic minimum with positive Hessian $A$, write the displacement
as $u$. The linear diffusion has stationary covariance $\Sigma$ satisfying

$$
A\Sigma+\Sigma A=\eta C/B.
$$

For unit mobility, the Gibbs covariance $\Sigma=T A^{-1}$ solves this
balance precisely when $\eta C/B=2T I$. Anisotropic noise generally prevents
a single scalar temperature from describing the stationary fluctuations.

**A one-dimensional check.** Let the curvature be $h>0$ and the batch-gradient
noise variance be $c/B$. The discrete linear update has stationary variance

$$
\operatorname{Var}_{\rm disc}u=\frac{\eta c}{Bh(2-\eta h)},\qquad
 0<\eta h<2,
$$

obtained from $v=(1-\eta h)^2v+\eta^2c/B$. The diffusion instead gives
$\operatorname{Var}_{\rm diff}u=\eta c/(2Bh)$. Their ratio is
$1/(1-\eta h/2)$, so agreement is controlled by a small $\eta h$.

> **Physical picture.** The condition is a fluctuation–dissipation relation,
> and saying so turns a vague question into a checkable one. A single scalar
> temperature describes the stationary fluctuations when the noise covariance
> and the mobility stand in the required proportion — for unit mobility, when
> the noise is isotropic. When the noise is stronger along some directions
> than others, the stationary covariance is not proportional to the inverse
> curvature and no scalar $T$ reproduces it. The physicist's instinct that a
> temperature must be *defined* by such a relation rather than read off one
> variance is exactly the right instinct, and it supplies the test: measure
> the noise covariance and the curvature separately and check the proportion.

Two further cautions belong here. The stationary balance is an equation for a
covariance, not a statement that any state energy decreases along a
trajectory. And the density it produces describes fluctuations of the
*parameters*, which is a different object from the conditional distribution
over tokens, even though exponentials appear in both.

## 3. Generation, caches, and the cost of a path

After training, hold the parameters fixed. Evaluate on a prompt, draw a token,
append it, repeat. Changing the decoding temperature rescales the scores; the
objective and the parameters do not change. For positive decoding
temperature $\tau$,

$$
p_\tau(a\mid c)=\frac{e^{z_a(c)/\tau}}{\sum_b e^{z_b(c)/\tau}}.
$$

For a unique largest score, the limit $\tau\to0^+$ concentrates on that
token, agreeing with **greedy decoding**, which selects a maximum directly.
With tied maxima the softmax limit is uniform over the ties, while a greedy
implementation may use a particular tie-breaking rule. At large $\tau$ a
finite vocabulary with finite scores approaches a uniform distribution.

For scores $(\log3,0)$, $p_1(A)=3/4$, whereas
$p_2(A)=\sqrt3/(1+\sqrt3)\simeq0.633975$. A change of temperature changes
the sampling rule, not the learned parameters.

In a deterministic causal decoder, extending a prefix does not change earlier
representations at a fixed layer, so their keys and values can be **cached**, meaning stored and reused
instead of computed again.
Exact equivalence to recomputation requires the same weights, positional
convention, mask and numerical operations, with random training operations
disabled. Truncating a cache changes the available context, and reusing cached
states after changing weights is not exact.

For a stochastic transition rule the probability of a path is a product of
conditionals, and its negative logarithm is a **path cost**, measuring how
improbable that path is under the rule.

> **Physical picture.** Calling that cost an action is a useful bookkeeping
> convention and nothing more, and the book settles the matter with an example
> rather than an argument. Take a two-state chain with uniform initial
> distribution and symmetric transitions: a particular path and its time
> reverse have *equal* probability, so the log ratio of forward to reverse is
> zero, while the path cost itself is positive. A positive negative-log-
> probability is therefore not evidence of irreversibility. Identifying heat,
> work or entropy production requires a reverse experiment and, for a thermal
> reading, relations between transition rates and energy exchanges — which is
> exactly the structure Week 14 builds explicitly, and exactly what is absent
> here.

For a numerical instance, take the fair stationary two-state chain with
switching probability $0.2$. The path $(A,A,B)$ has probability
$\tfrac12(0.8)(0.2)=0.08$, as does its reverse $(B,A,A)$.
The path cost is $-\log0.08\simeq2.525729$, while the log ratio of forward
to reverse probabilities is zero.

The same discipline applies to another tempting word. Repeating a map is not a
renormalization transformation: one must say what is eliminated or
coarse-grained, what is rescaled, and which observables the transformation
preserves.

## Checkpoints with answers

**1. Why do shared weights receive a sum of gradients?** Changing that
parameter changes every occurrence. The total derivative includes each
causal path, as the $w^2x$ example makes explicit.

**2. What is stochastic about stochastic gradient descent?** The sampled
examples used to estimate the gradient. The randomness is not automatically
a thermal bath, and its covariance need not be isotropic.

**3. Does zero decoding temperature retrain the model?** No. It is a limit
of the output sampling rule. With a unique maximum it chooses the same token
as greedy decoding; tied maxima require care.

---

## Subtleties and fine print

**Matching two moments is not an identity.** The diffusion approximation
requires control of the step size, of the batch-noise variation, and of the
regularity of the coefficients. The book's exercise exhibits the discrete and
diffusion stationary variances differing at order $\eta h$.

**Sampling without replacement changes the noise.** It introduces a
finite-population correction and temporal dependence, neither of which the
matched moments describe.

**The Lyapunov balance is about a covariance.** It is not a descent statement
about a trajectory, and reading it as one imports a dynamics the equation does
not contain.

**Caching is exact only under stated conditions.** Same weights, same
positional convention, same mask, same numerics. Any recurrence directly in
hidden states can also make prompt processing sequential even when all prompt
tokens are known.

**The decoding temperature is not a training step.** It is an intervention on
a finished model, and Week 1 already made that point; it returns here because
this is where a student first has both objects in hand at once.

---

## Key claims and status

| Claim | Status |
|---|---|
| Backward recursion for the sensitivities | [Exact], by the chain rule |
| A shared parameter receives the sum over its uses | [Exact], by the worked example |
| Continuous adjoint from the residual step | [Controlled approximation], under the Week 9 hypotheses |
| Frozen-coefficient diffusion increments match the discrete mean and covariance | [Exact] frozen moment matching; [Approximation] to SGD, controlled only with the stated small-step hypotheses |
| Stationary covariance balance near a quadratic minimum | [Exact] for the linear diffusion it describes |
| A single effective temperature reproduces the stationary variances | Conditional: requires the stated noise–mobility relation; fails for anisotropic noise |
| Discrete and diffusion stationary variances differ at order $\eta h$ | [Exact], by the exercise |
| Forward and reverse of the two-state path have equal probability | [Exact]; a positive path cost is not irreversibility |

---

## What the week establishes

1. The backward recursion, with the reason a shared parameter accumulates a
   sum rather than taking its last use.
2. A diffusion approximation that matches exactly two moments of one update,
   with what it therefore does not control stated alongside.
3. A criterion, rather than an impression, for when an effective temperature
   exists: a fluctuation–dissipation relation between the noise covariance and
   the mobility.
4. A counterexample settling that the negative log probability of a generated
   path is neither an action in the physical sense nor an entropy production.

**What to carry forward.** Both temptations of this week have the same shape.
A familiar formula appears, the vocabulary that travels with it is imported,
and the import is not checked. The remedy is also the same in both cases and
is available: the vocabulary comes with a *criterion* — a
fluctuation–dissipation relation, a reverse experiment — and the criterion can
be tested. Unit 3 applies exactly this move to observables of trained models.

## The practical session — Laboratory 4, part III

**Varied:** the optimizer step, and then, with training finished, the decoding
temperature.
**Held fixed:** the data split; and after training, the parameters, which do
not move while the samples are drawn.
**Measured:** the fitting loss and the evaluation loss separately, both
against the optimizer step; the samples at several decoding temperatures; and
whether a cached and an uncached forward pass agree on the same prefix under
the conventions of §3.

**Product:** the two loss curves; samples at three temperatures with
commentary on how they change while the parameters do not; and the cache
agreement check. Implementing the decoder from scratch is an optional
extension, not a requirement.

---

## Connections to other parts of the wiki

- [[week-09-four-indices|Week 9]] separated the index this week runs along
  from the three it is most often confused with.
- [[week-01-inferring-a-distribution|Week 1]] supplies the loss, the decoding
  temperature, and the first warning about importing thermal vocabulary.
- Week 14 builds the thermal construction this week finds absent: an energy, a
  bath, a protocol and a reverse experiment, with a work identity that is
  exact because all four are specified.
- Week 13 applies the criterion-not-impression move of §2 to claims about
  trained models.
- nn-llm-unit-2 — the block skeleton this note implements.

---

[[nn-llm-start-here|Start here]] · [[nn-llm-week-map|All weeks]] · [[nn-llm-resources|Book and experiments]] · [[week-09-four-indices|Previous week]] · [[week-11-particles-on-a-sphere|Next week]]
