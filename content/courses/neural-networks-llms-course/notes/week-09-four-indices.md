---
title: "Week 9 — Four indices: depth, iteration, position, training step"
type: lecture-notes
course: nn-llm-syllabus
semester: 1
week: 9
unit: 2
duration: "4 hours (2 hr lecture + 2 hr laboratory)"
status: draft
modified: 2026-09-19
---

# Week 9 — Four Indices: Depth, Iteration, Position, Training Step

*Notes for [[nn-llm-syllabus|the neural-networks course]], Unit 2. Written by an AI assistant under the researcher's supervision; see ai-authorship.*

*Processing a layer, repeating an internal update, appending a token and
changing parameters are different operations. We separate their indices and
then calculate when repeated updates approximate an ODE and how a perturbation
propagates through a simple recurrent state.*

---

## Learning goals

1. Name the four indices and say what advances when each increases.
2. **State** the hypotheses under which a stack of residual blocks has a
   controlled continuous-depth limit, and what the error bound is.
3. **Derive** the contraction estimate for a driven scalar memory, and say
   what it does and does not establish about recurrence.
4. Read a recurrent-transformer proposal against those distinctions.

## Reading

**Primary text.** Chapter 3, §3.5, including the recurrence discussion of
§3.5.2 and the architecture reading of §3.5.3.

**Primary literature**, through [[nn-llm-bibliography|the bibliography]]: Chen
and collaborators for neural ODEs; Dehghani and collaborators for Universal
Transformers; Fan and collaborators for feedback memory; Geiping and
collaborators for a trained recurrent-depth model; Zhang's technical note,
in the version consulted on 2026-09-13.

**Prerequisites.** [[week-08-one-head-and-a-decoder|Week 8]] for the block
being iterated. [[week-06-attention-from-an-energy|Week 6]] §5 for the driven
scalar map.

## A concrete sequence of operations

Supply the context $AB$. Passing it through block 1 and then block 2 changes
**depth**, while the supplied tokens and all parameters remain fixed.
Repeating block 2 with shared weights changes an **internal iteration**.
Appending a generated $B$ changes **token position** and the available context.
Using an observed target to adjust a weight changes the **training step**.
These are four different experiments even when each is implemented by a loop.

## 1. Four indices

Layer depth $\ell$ advances when a representation passes to the next layer of
a fixed network. Internal iteration $r$ advances when an update is repeated
before an output is produced. Token position $i$ advances when a token is
consumed or generated, which changes the available context. Training step $n$
advances when the parameters change.

With different layer parameters, depth evolution is a composition of
*different* maps. With shared parameters and every other input held fixed,
internal iteration can be the repeated application of one map. Across token
positions the inputs, the positional operations and the available memories
all change, and parameter sharing does not remove those changes.

| Index | What changes | What is fixed in the comparison |
|---|---|---|
| Layer $\ell$ | The representation and usually the layer's map | The supplied sequence and the trained parameter collection |
| Internal iteration $r$ | The internal state | The repeated map and, for an autonomous iteration, all external inputs |
| Token position $i$ | The accessible prefix and positional operations | The model parameters during generation |
| Training step $n$ | The parameter collection | The training rule and dataset; the selected batch can vary |

A sequence of different layer maps is a **nonautonomous dynamical system**:
its rule depends on the step. A fixed map gives an autonomous one. Both are
legitimate dynamical systems. Fixed points of a single map cannot simply be
assigned to a changing family of maps, and a continuous-depth limit requires
a specified family and scaling.

## 2. When is depth a continuous variable?

For total depth coordinate $S$, set $\Delta s=S/L$ and $s_\ell=\ell\Delta s$.
Consider the family

$$
h_{\ell+1}=h_\ell+\Delta s\,f(s_\ell,h_\ell),\qquad
 \frac{dh}{ds}=f(s,h),\quad h(0)=h_0.
$$

Suppose $f$ is uniformly Lipschitz in $h$ with constant $K$, sufficiently
regular in $s$, and the relevant trajectories stay in a region where the
one-step Taylor remainder is bounded by $C\Delta s^2$. Subtracting the exact
ODE step from the discrete one gives

$$
e_{\ell+1}\le(1+K\Delta s)e_\ell+C\Delta s^2,
 \qquad e_\ell=\|h_\ell-h(s_\ell)\|.
$$

Starting with $e_0=0$ and summing the geometric series yields

$$
e_L\le\frac{C}{K}(e^{KS}-1)\Delta s
$$

for $K>0$, with the continuous $K\to0$ limit $CS\Delta s$.
This is a controlled first-order approximation. A single trained stack does
not establish this family, scaling or uniform bound.

**Example.** For $dh/ds=-h$, the continuous solution is $h(s)=h_0e^{-s}$.
Euler gives $h_{\ell+1}=(1-\Delta s)h_\ell$. At $\Delta s=0.5$ the
amplitude shrinks by half each step; at $\Delta s=3$ it doubles while
alternating sign. Residual form alone does not inherit the ODE's stability.

> **Physical picture.** This is the continuum limit of a lattice theory, with
> the hypotheses in their usual places. A lattice model approaches a continuum
> field theory when the spacing goes to zero *with the couplings scaled
> appropriately*, and the scaling is what makes the limit exist. Here $\Delta
> s = S/L$ is the spacing and the factor $\Delta s$ multiplying the update is
> the scaling. A trained network is a lattice model at fixed spacing with
> order-one couplings, and nobody would describe such a thing as a continuum
> theory on the grounds that it has many sites. The quantity to measure, before
> treating depth as continuous, is the size of one layer's update against the
> norm of the representation it updates.

## 3. Recurrence as a question about memory

A recurrent rule uses its previous state in computing the next one, which
provides a route by which earlier inputs can affect later outputs. Whether
anything survives along that route is a separate question, and the book poses
it on a scalar map driven by an input sequence.

Hold the parameter $\beta>0$ fixed and prescribe inputs $u_i$. Define

$$
a_{i+1}=\tanh(\beta a_i+u_i).
$$

Two facts follow by differentiation. Because the
derivative of $\tanh$ is bounded by one, two states exposed to *identical*
inputs satisfy $|a_i - \tilde a_i| \le \beta^i |a_0 - \tilde a_0|$: for $\beta
< 1$ every initial distinction is suppressed geometrically. And the local
sensitivity is a product of factors $\beta(1 - a_{k+1}^2)$, so a long path
through the computation need not yield a large derivative — saturation near
$|a| = 1$ can strongly attenuate perturbations even when $\beta>1$. Explicitly,

$$
\frac{\partial a_m}{\partial a_0}
 =\prod_{k=0}^{m-1}\beta(1-a_{k+1}^2).
$$

For $\beta=1/2$, initial states separated by one are separated by at most
$2^{-10}\simeq0.000977$ after ten equal-input steps. A measurement with
resolution $0.001$ can no longer reliably resolve this difference.
This is an operational statement about sensitivity and resolution. An exactly
known noiseless invertible map can retain information despite a tiny
derivative; attenuation is not by itself an information-theoretic erasure
proof.

For constant input, a fixed point obeys $a_*=\tanh(\beta a_*+u)$.
Implicit differentiation gives

$$
\frac{da_*}{du}=\frac{1-a_*^2}{1-\beta(1-a_*^2)}.
$$

On the stable zero-input branch with $\beta<1$, $a_*=0$ and the response
is $1/(1-\beta)$. A large response near one is a property of this fixed-point
branch, distinct from how many iterations are performed.

At a **fixed** input $u$, the energy

$$
E_u(a)=\tfrac12a^2-\beta^{-1}\log[2\cosh(\beta a+u)]
$$

obeys the same descent inequality as Week 6. If $u$ changes, the comparison
also contains $E_{u_{i+1}}(a_{i+1})-E_{u_i}(a_{i+1})$, which has no fixed
sign. The proof therefore supplies no common decreasing energy for an
arbitrary driven sequence.

A computational path says an early input can enter a later calculation.
The derivative says how strongly a perturbation propagates along that path.
To measure retained information one must additionally specify noise,
precision, a readout or an information measure. Counting internal iterations
alone answers none of those questions.

## 4. Reading the architectures

Several routes introduce recurrence into a transformer: repeating computation
across depth, carrying a feedback memory across positions, or spending extra
internal iterations on a token before emitting the next one. They differ in
*what is repeated* and *what state is carried*, and the book insists that
comparisons be made at matched computational budgets and tasks.

Zhang's Recurrent Looped Transformer is read as an architectural proposal
inspected on 2026-09-13, with no measured performance in the version
consulted. The scalar map of §3 is the course's teaching example and not a
reduction derived from it. Empirical results from other recurrent
architectures do not transfer to it.

The useful discipline here is the one the section closes on: with a fixed
prompt supplied externally, such an architecture is generally a driven
sequence of maps; with generated inputs, an enlarged state must include
everything needed to determine future transitions, including caches and
position, and its size may grow with the context. Neither case reduces to the
iteration of one fixed map on a fixed latent vector.

## Checkpoints with answers

**1. Does sharing weights make generated text an autonomous iteration on one
fixed hidden vector?** No. The context, position and available memories also
change. An autonomous description must include every state variable needed
for future transitions.

**2. Does doubling the number of residual blocks approach an ODE?** Only in
a specified family with the update scaled as $S/L$ and the regularity bounds
above. Duplicating arbitrary finite blocks supplies no such guarantee.

**3. Does a derivative of $10^{-6}$ prove that six decimal digits of
information have been destroyed?** No. It measures local sensitivity in the
chosen coordinates. Recoverability depends on readout noise and precision;
information-theoretic loss needs a separate analysis.

---

## Subtleties and fine print

**Shared parameters do not make a system autonomous.** They make the *map*
the same; they do not make the inputs, the positional operations or the
available memories the same. Only when everything else is fixed is the
iteration $F^r$.

**A longer path is not better memory.** §3 is the demonstration. This is the
claim most often made implicitly, by reporting a computation count as though
it were a capability.

**The energy inequality holds at fixed current input only.** Quoting it for a
driven trajectory is exactly the error of carrying an argument across an index
it does not apply to.

**The continuous limit needs a family, not a network.** The bound of §2 is
about a sequence of networks indexed by $L$. A single stack has no $L$ to send
anywhere.

**An architectural proposal is not a result.** The reading of §4 is dated
deliberately. A proposal with no reported measurements is a question to
investigate, and the course's own scalar model is a teaching device, not
evidence about it either way.

---

## Key claims and status

| Claim | Status |
|---|---|
| The four indices advance four different things | [Exact] by definition; the point is that arguments do not transfer |
| Euler error proportional to $\Delta s$, constant set by $K$ and $S$ | [Controlled approximation]; every hypothesis used |
| A stable ODE can have an unstable discretization at large step | [Exact], by the worked example |
| $\lvert a_i - \tilde a_i\rvert \le \beta^i\lvert a_0 - \tilde a_0\rvert$ for identical inputs | [Exact] for $0<\beta<1$ |
| Sensitivity as a product of $\beta(1-a_{k+1}^2)$ | [Exact.] |
| Response $1/(1-\beta)$ at the origin for constant input | [Exact.] |
| Descent inequality at fixed current input | [Exact]; the driven case has no fixed sign |
| Recurrent Looped Transformer as inspected | [Proposal]: no reported performance in the version consulted on 2026-09-13 |

---

## What the week establishes

1. Four indices, four categories of dynamical system, and the arguments that
   apply to each.
2. A continuous-depth limit with an explicit error bound, together with the
   hypotheses it needs — none of which a single trained stack supplies.
3. A geometric contraction of initial distinctions under identical inputs, and
   a sensitivity product showing why a long computational path can carry
   a very small perturbation. Information retention needs an additional
   operational definition.
4. That the fixed-input energy inequality does not extend to a driven
   trajectory, so recurrence has no common decreasing energy in general.

**What to carry forward.** The pattern behind every caution in this week is
one thing: an argument established along one index being quoted along another.
Depth is not iteration, iteration is not position, and none of the three is
training time. Carrying that habit into Unit 3 is what makes the measurements
there interpretable, because the same error appears in the literature on
trained models in a different costume.

## The practical session — Laboratory 4, part II

**Varied:** one ingredient at a time — position information, a single head,
the residual branch, or the number of internal iterations.
**Held fixed:** the data split and the evaluation contexts, identical across
every intervention; and, declared each time, whether the weights were held
fixed or retrained, since those answer different questions.
**Measured:** conditional loss, the relevant intermediate vectors, and
computational cost; then, in the browser recurrence experiment, how long a
perturbation of the initial state survives under controlled inputs.

**Product:** a table of interventions against measured loss and cost; and the
measured persistence set against the bound of §3, with any discrepancy
explained. A configuration that costs more and measures the same is a result,
and should be reported as one.

---

## Connections to other parts of the wiki

- [[week-08-one-head-and-a-decoder|Week 8]] supplies the block whose iteration
  this week studies.
- [[week-06-attention-from-an-energy|Week 6]] supplies the undriven map and
  its bifurcation, and the descent inequality this week shows does not survive
  driving.
- [[week-10-gradients-and-generation|Week 10]] takes up the fourth index,
  training time, and the stochastic process on it.
- Week 13 meets the same error — an argument quoted outside the regime that
  established it — in the setting of scaling and emergence.
- nn-llm-unit-2 — the block skeleton this note implements.

---

[[nn-llm-start-here|Start here]] · [[nn-llm-week-map|All weeks]] · [[nn-llm-resources|Book and experiments]] · [[week-08-one-head-and-a-decoder|Previous week]] · [[week-10-gradients-and-generation|Next week]]
