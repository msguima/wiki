---
title: "Week 3 — The perceptron and the space of interactions"
type: lecture-notes
course: nn-llm-syllabus
semester: 1
week: 3
unit: 1
duration: "4 hours (2 hr lecture + 2 hr guided calculation)"
status: draft
modified: 2026-09-19
---

# Week 3 — The Perceptron and the Space of Interactions

*Notes for [[nn-llm-syllabus|the neural-networks course]], Unit 1. Written by an AI assistant under the researcher's supervision; see [[ai-authorship]].*

*We need an adjustable map from input numbers to prediction scores. A single
neuron is the smallest example. We will calculate its output and one training
step, compose neurons into a hidden layer, and then ask how many prescribed
labels a weight vector can represent. The last question leads to Cover's
counting formula and the statistical mechanics of learning.*

---

## Learning goals

1. Compute what a neuron outputs and carry out one weight update by hand.
2. Distinguish *finding* a solution from *counting* the solutions, and say
   why the second question is the one statistical mechanics answers.
3. **Derive** Cover's counting formula and its threshold $\alpha_c = 2$.
4. State what the threshold does and does not claim.

## Reading

**Primary text.** Chapter 2, §2.1 through §2.3.

**Primary literature**, through [[nn-llm-bibliography|the bibliography]]:
Cover (1965) for the counting; Engel and Van den Broeck (2001) for the
statistical-mechanical framing that Week 4 takes up.

**Prerequisites.** Weeks 1–2. Quenched disorder at the level of "the couplings
are drawn once and held fixed"; the rest is developed here.

## 1. A neuron, and one update

A **neuron** is a small adjustable function. Given numbers
$\boldsymbol x=(x_1,\ldots,x_N)$, form

$$
h=\sum_iw_ix_i+b.
$$

The **weights** $w_i$ specify how strongly each input contributes. The
**bias** $b$ is an additive offset. An **activation function** $f$ turns this
field into an output $a=f(h)$. With $f(h)=\operatorname{sign}h$ the output
is a class label, and the boundary $h=0$ is a hyperplane normal to
$\boldsymbol w$. With $f(h)=\tanh h$ the output varies smoothly.

To predict a binary label $\sigma=\pm1$, use the Week 1 distribution

$$
p(\sigma\mid\boldsymbol x)=\frac{e^{\sigma h}}{2\cosh h},\qquad
 \ell=\log(2\cosh h)-\sigma h.
$$

The loss depends on a weight through the field. The chain rule gives

$$
\frac{\partial\ell}{\partial w_i}
 =(\tanh h-\sigma)x_i,\qquad
 \frac{\partial\ell}{\partial b}=\tanh h-\sigma.
$$

The predicted mean is $\tanh h$ and the observed label is $\sigma$.
The factor $x_i$ tells how much changing that weight changes the field.

**Example.** Hold $\boldsymbol x=(1,-1)$ and $\sigma=+1$ fixed. Initially
$\boldsymbol w=0,b=0$, so $p(+\mid\boldsymbol x)=1/2$. With learning rate
$\eta=0.1$, the update $w_i\leftarrow w_i-\eta\partial_{w_i}\ell$ gives

$$
\boldsymbol w'=(0.1,-0.1),\qquad b'=0.1,\qquad h'=0.3.
$$

Thus $p'(+\mid\boldsymbol x)=1/(1+e^{-0.6})\simeq0.645656$ and the
loss falls from $0.693147$ to $0.437488$ nats. This establishes improvement
on this observation; performance on fresh inputs requires another test.

### A hidden layer and backpropagation

A **layer** is a collection of neurons acting on the same input. It is
**hidden** if its outputs are intermediate quantities rather than the final
prediction. Let

$$
a_j=\tanh h_j,\qquad h_j=\sum_iW_{ji}x_i+b_j,\qquad
 z=\sum_jv_ja_j+c.
$$

Use $z$ in place of $h$ in the binary distribution. Put
$\delta=\tanh z-\sigma$. The derivatives are

$$
\frac{\partial\ell}{\partial v_j}=\delta a_j,\quad
 \frac{\partial\ell}{\partial c}=\delta,\quad
 \frac{\partial\ell}{\partial W_{ji}}
 =\delta v_j(1-a_j^2)x_i,\quad
 \frac{\partial\ell}{\partial b_j}=\delta v_j(1-a_j^2).
$$

Read the third expression along its path: a weight changes $h_j$ by $x_i$,
$h_j$ changes $a_j$ by $1-a_j^2$, and $a_j$ changes $z$ by $v_j$.
**Backpropagation** organizes these chain-rule products from the final loss
back toward the inputs, reusing derivatives shared by several paths. It does
not require a new rule of calculus. The nonlinear activation matters:
composing only affine maps would still give a single affine map.

The vocabulary of neurons and layers is now fully specified by equations.
[[week-08-one-head-and-a-decoder|Week 8]] will use this same hidden-layer
construction separately at each text position.

## 2. From finding to counting

The change of question happens here, and it should be marked in the lecture.

Fix $P$ patterns and desired labels. The learning question is: does some
algorithm reach a weight vector that classifies them all? The **feasibility**
question is: does such a weight vector exist, and what fraction of weight
space consists of them? The second question has no algorithm in it.

The book sets it up on the homogeneous spherical perceptron, with the norm
fixed by $\boldsymbol w\cdot\boldsymbol w = N$. Fixing the norm is not cosmetic: at zero
margin it removes a scaling redundancy, and once a nonzero **margin** $\kappa$
is demanded it is essential, since otherwise every field could be inflated by
rescaling the weights. The factor $\sqrt N$ in the normalized field is derived
rather than asserted — the field is a sum of $N$ independent contributions
with variance $\sum_i w_i^2 = N$, so it grows like $\sqrt N$, and dividing
leaves a quantity against which a fixed $\kappa$ means the same thing at every
dimension.

Write the normalized field for pattern $\mu$ as

$$
u_\mu=\frac{\sigma^\mu\boldsymbol w\cdot\boldsymbol\xi^\mu}{\sqrt N}.
$$

Here $\boldsymbol\xi^\mu$ is an input vector and $\sigma^\mu$ its desired
sign. A **margin** $\kappa\ge0$ requires $u_\mu\ge\kappa$, providing a
buffer against the decision boundary. With $d\mu_N$ the normalized uniform
measure on $\boldsymbol w^2=N$, **Gardner's volume** is

$$
V=\int d\mu_N(\boldsymbol w)\prod_{\mu=1}^P\Theta(u_\mu-\kappa).
$$

The step function is one when a constraint is satisfied and zero otherwise;
the product keeps only weights satisfying them all. Thus $V$ is the fraction
of the sphere meeting every constraint. The patterns are **quenched disorder**: drawn once and held fixed
while the weight configurations are examined. The ratio $\alpha = P/N$ is the
**load**, and it is the same $\alpha$ the course uses in Weeks 4, 5 and 13.

> **Physical picture.** The quenched setup is the familiar one, and naming it
> as such saves a lot of confusion later. The patterns play the role the
> random couplings play in a spin glass: they are part of the *problem*, not
> part of the state, and an observable must be averaged over them after the
> thermodynamics is done, not before. The weight vector is the state, the
> sphere is its configuration space, and the constraints carve a region out of
> it. Everything in Weeks 3 and 4 is an attempt to measure that region.

## 3. Cover's counting

At zero margin the question can be answered exactly, with no thermodynamics at
all, and the book does so before introducing any replicas.

A **dichotomy** is one of the $2^P$ assignments of signs to the $P$ patterns.
Assume general position — every subset of at most $N$ pattern vectors is
linearly independent, which independent Gaussian vectors satisfy with
probability one. In weight space each equation $\boldsymbol w\cdot\boldsymbol\xi^\mu = 0$ is a
hyperplane, and together the hyperplanes cut the sphere into regions within
which all predicted signs are fixed. Their number is the number of realizable
dichotomies.

Adding a new hyperplane splits exactly the regions it intersects, and those
regions are counted by the same problem one dimension down. That gives the
recursion $C(P+1,N) = C(P,N) + C(P,N-1)$, and with $C(1,N)=2$, $C(P,1)=2$ for positive $P,N$, and Pascal's identity,

$$
C(P,N) = 2\sum_{k=0}^{N-1}\binom{P-1}{k}.
$$

Since labels are equally likely, the probability that a random assignment is
realizable is $C(P,N)/2^P$, which is the tail probability
$\Pr[B \le N-1]$ for $B \sim \mathrm{Binomial}(P-1,\tfrac12)$. Compare the threshold with the mean: their difference is
$N(1-\alpha/2)+O(1)$. At fixed $\alpha<2$ it is positive and grows like
$N$ for large $N$, while the fluctuation grows only like $\sqrt N$. So the probability is driven to one below $\alpha = 2$ and to
zero above it, and the crossover is resolved over a window of width of order
$N^{-1/2}$.

The formula is small enough to check by hand in two dimensions, and the check
is worth doing at the board. For $N = 2$, $P$ generic lines through the origin
cut the circle into $2P$ arcs, and $C(P,2) = 2[\binom{P-1}{0} + \binom{P-1}{1}]
= 2P$ agrees. At $P = 3$ that is six realizable dichotomies out of eight, and
at $P = 4$ it is eight out of sixteen — the realizability probability falling
through $1/2$ exactly at $P = 2N$, which is the threshold in its finite-$N$
form. The general statement $C(2N,N)/2^{2N} = 1/2$ is binomial symmetry and
holds at every $N$, not only asymptotically.

> **Physical picture.** This is a threshold with every ingredient a physicist
> would demand, and none of them imported: a sequence of systems indexed by
> $N$, an intensive control parameter $\alpha$, an order parameter in the
> realizability probability, and a crossover width that was *calculated*
> rather than fitted. The limiting step function is a consequence of a
> finite-$N$ counting formula. Week 13 uses exactly this list as the standard
> against which a claimed transition in a trained model is read, and the
> reason the standard has teeth is that here it is met in full.

## Checkpoints with answers

**1. Why replace the hard sign when training by derivatives?** Its derivative
is zero away from the boundary and undefined on it. The smooth probabilistic
loss supplies a derivative that measures the prediction error.

**2. Can a hidden linear layer add expressive power to a linear output?**
No: $v^{\mathsf T}(Wx+b)+c$ is another affine function of $x$. Nonlinearity
is what prevents that collapse.

**3. For three generic patterns in two dimensions, is every random labelling
separable?** No. Cover's formula gives six of eight, hence probability $3/4$.
The threshold at $P/N=2$ concerns the large-system limit; it is not a promise
for every finite dataset.

---

## Subtleties and fine print

**Feasibility is algorithm-independent; running time is not.** The threshold
says a separating weight vector exists below $\alpha = 2$. It says nothing
about whether a chosen procedure finds one, or how long it takes.

**$\alpha_c = 2$ is a statement about a typical random labelling.** It does not
say every labelling at $P = 2N$ is realizable. The finite-$N$ formula is the
exact statement; the threshold is its thermodynamic-limit consequence for
independent random labels.

**A vanishing volume is not infeasibility.** The normalized volume can already
be exponentially small below the threshold. That $V \to 0$ with $N$ does not
by itself mean solutions have ceased to exist, and Week 4 depends on keeping
the two apart.

**General position is an assumption, satisfied here with probability one.**
For structured patterns — repeated vectors, collinear sets — the count changes,
and the formula does not apply.

**Zero margin is a boundary case handled by convention.** Strict separation is
taken when counting; for generic patterns the boundary faces carry zero
spherical measure, so the convention does not affect the count.

---

## Key claims and status

| Claim | Status |
|---|---|
| Two-layer gradients by the chain rule, route by route | [Exact.] |
| The $\sqrt N$ normalization from $\boldsymbol w\cdot\boldsymbol w = N$ | [Exact], for independent unit-variance inputs |
| $C(P+1,N) = C(P,N) + C(P,N-1)$ | [Exact] in general position |
| $C(P,N) = 2\sum_{k<N}\binom{P-1}{k}$ | [Exact] at finite $N$ |
| $C(2N,N)/2^{2N} = 1/2$ | [Exact], by binomial symmetry |
| $\alpha_c = 2$ for independent random labels | [Thermodynamic limit], crossover width $O(N^{-1/2})$ |
| The hard sign gives no ordinary gradient | [Exact]; its derivative is zero almost everywhere |

---

## What the week establishes

1. A neuron is a hyperplane with a squashing function, and its learning rule is
   the Week 1 gradient with the input as a multiplier.
2. Fixing the weight norm is what makes a margin meaningful, and the $\sqrt N$
   in the normalized field follows from that constraint rather than being
   chosen.
3. The number of realizable dichotomies is exactly
   $2\sum_{k<N}\binom{P-1}{k}$, for any $P$ and $N$ in general position.
4. The realizability probability tends to a step at $\alpha = 2$, with a
   crossover window of width $O(N^{-1/2})$ — every ingredient computed, none
   fitted.

**What to carry forward.** The change from Unit 0 is a change of question:
from which distribution describes the data to how much of parameter space
satisfies a constraint. That second question is the one statistical mechanics
is built for, and Week 4 answers it again with a method whose limits are
assumptions rather than theorems. Keep Cover's answer in view while that
happens — it is the independent check.

## The practical session — guided calculation, part I

**Varied:** the number and direction of patterns, in two dimensions where the
regions can be drawn.
**Held fixed:** the spherical constraint and the zero-margin convention.
**Measured:** the number of regions the hyperplanes cut the circle into,
counted by hand, against $C(P,2) = 2P$.

**Product:** the drawn arcs for $P = 2, 3, 4$ with the admissible region
identified, the count checked against the formula, and the set-up of Gardner's
volume written out ready for Week 4.

---

## Connections to other parts of the wiki

- [[week-01-inferring-a-distribution|Week 1]] supplies the loss whose gradient
  drives the single update of §1.
- [[week-04-gardner-capacity|Week 4]] asks the same feasibility question at
  nonzero margin, where no exact count is available and the replica method
  enters.
- Week 13 uses the four ingredients of §3 as its standard for reading a
  claimed transition in a trained model.
- nn-llm-unit-1 — the block skeleton this note implements.

---

[[nn-llm-start-here|Start here]] · [[nn-llm-week-map|All weeks]] · [[nn-llm-resources|Book and experiments]] · [[week-02-transfer-matrix-and-finite-text|Previous week]] · [[week-04-gardner-capacity|Next week]]
