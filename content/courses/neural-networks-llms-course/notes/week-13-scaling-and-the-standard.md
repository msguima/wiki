---
title: "Week 13 — Scaling, grokking, and the standard of a transition"
type: lecture-notes
course: nn-llm-syllabus
semester: 1
week: 13
unit: 3
duration: "4 hours (2 hr lecture + 2 hr laboratory)"
status: draft
modified: 2026-09-19
---

# Week 13 — Scaling, Grokking, and the Standard of a Transition

*Notes for [[nn-llm-syllabus|the neural-networks course]], Unit 3. Written by an AI assistant under the researcher's supervision; see ai-authorship.*

*We can now compute a decoder's prediction and describe its training. This
week asks how to measure attention concentration and how the prediction loss
changes with model size and data. Simple calculations will distinguish an
architectural mechanism, an empirical scaling fit and a limiting transition.*

---

## Learning goals

1. Measure attention concentration with a stated accessibility baseline, and
   say what the measurement alone establishes.
2. Explain why an auxiliary Markov chain built from an attention matrix is
   useful and what it is not.
3. **Derive** the compute-optimal allocation from an assumed loss model, and
   separate what is exact from what is fitted.
4. Apply the four-ingredient standard to a claimed transition.

## Reading

**Primary text.** Chapter 4, §4.5 and §4.6.

**Primary literature**, through [[nn-llm-bibliography|the bibliography]]: Zhai
and collaborators on attention entropy and training instability; Kaplan and
collaborators, and Hoffmann and collaborators, on scaling; Power and
collaborators on grokking; Schaeffer, Miranda and Koyejo on metrics and
emergent abilities.

**Prerequisites.** [[week-03-perceptron-and-cover|Week 3]], whose threshold is
this week's standard. [[week-11-particles-on-a-sphere|Week 11]] for the
observables and the resampling discipline.

## From a computed model to a measured one

Begin with a fixed decoder, a fixed evaluation set and a named quantity.
Attention entropy concerns which positions are consulted; next-token loss
concerns prediction; a compute budget concerns the operations used to train
or run the model. None can stand in for the other two. These definitions
make the physical questions precise enough to calculate or measure.

## 1. Attention concentration, measured honestly

The entropy of one attention row is bounded above by the logarithm of the
number of positions that row can reach — the relative entropy to the uniform
distribution on accessible positions is nonnegative, which is the Week 1
inequality applied to a row. Its exponential is an effective number of
consulted positions. If row $i$ can access $m_i$ positions, define

$$
H_i^A=-\sum_{j:A_{ij}>0}A_{ij}\log A_{ij},\qquad
 n_{\rm eff}=e^{H_i^A},\qquad 0\le H_i^A\le\log m_i.
$$

The bound follows from $D(A_i\Vert\text{uniform})=\log m_i-H_i^A\ge0$.
For $m_i>1$ the ratio $H_i^A/\log m_i$ lies between zero and one. At
$m_i=1$ report $H_i^A=0$ and omit the ratio, which would be $0/0$.

The number of accessible positions is therefore part of the measurement.
Uniform attention at position 2 has entropy $\log 2$; at position 100 it has
$\log 100$. Comparing rows at different positions requires reporting the
normalized quantity as well as the raw one, and the first row has zero entropy
by construction and should not be classified as pathological concentration.

An **attention sink** is a position receiving substantial attention from many
queries. Its baseline is affected by accessibility too: the book's exercise
shows that with uniform attention in every accessible row, the first position
still receives the most mass, simply because every later query can reach it.
No learned content is required to produce this accessibility bias.
For a uniform causal matrix, $A_{ij}=1/i$ when $j\le i$, the total received
mass is $M_j=\sum_{i=j}^T1/i$. At $T=3$ these masses are
$(11/6,5/6,1/3)$, largest at the first position despite uniform rows.
Whether a measured position is called a sink should be judged relative to
this baseline.

> **Physical picture.** The exponential of an entropy counts, in the way
> $e^S$ counts microstates: an effective number of positions actually
> consulted. What makes the accessibility baseline essential is that the count
> is over a set whose size varies along the sequence, so comparing raw
> entropies across positions is comparing counts drawn from different-sized
> sets. The correct analogue is an entropy per degree of freedom, and the
> exercise showing a sink arising from accessibility alone is the null model
> every sink measurement needs.

Connections between very low attention entropy and training instability have
been investigated empirically. The scalar observable alone establishes
neither instability nor poor prediction, and a row with low entropy need not
choose the same position as another row — concentration and a shared sink are
different observations. Nor does a large weight determine the contribution to
the output, since the value vector and the subsequent projections also matter.

## 2. An auxiliary chain, and what it is for

For a fixed sequence, layer and head, the attention matrix is row-stochastic,
so one can define a random walk on positions. It is worth being explicit that
this walk is a construction of ours: its index is neither token generation nor
layer depth, and the transformer recomputes matrices and applies value maps,
residuals and nonlinearities rather than evolving by powers of one matrix.

For a fully causal mask with positive accessible entries, the walk moves only
toward earlier positions or stays put, and position 1 is absorbing. Splitting
off the absorbing state gives the mean absorption times from the transient
ones by a linear solve. For example, fix

$$
A=\begin{pmatrix}1&0&0\\1/2&1/2&0\\1/4&1/4&1/2\end{pmatrix}.
$$

With $t_1=0$, first-step conditioning gives
$t_2=1+t_2/2$ and $t_3=1+t_2/4+t_3/2$, hence $t_2=2,t_3=3$.
More generally, if $Q$ is the transient submatrix, $t=\boldsymbol1+Qt$,
so $t=(I-Q)^{-1}\boldsymbol1$ when its spectral radius is below one.

> **Physical picture.** The stationary distribution of this walk is entirely
> uninformative — all the mass sits on position 1 — and the transient
> structure is where everything is. That is a familiar situation: for an
> absorbing chain the equilibrium state is trivial and the physics is in the
> approach, so one measures mean first-passage times rather than an
> equilibrium average. It is also the reason the irreversibility measure
> constructed for stationary chains gives zero here: on the absorbing class
> only a self-transition carries probability. During the transient, allowed
> backward jumps have forbidden reversals, so a naive path ratio has infinite
> contributions and is not a finite dissipation measurement. Grouping
> positions by token type does not fix this, because the grouped process need
> not be Markov.

## 3. Scaling laws, and what follows exactly from a fit

A **scaling law** describes how an observable changes when a resource is
varied. The fits of Kaplan and collaborators and of Hoffmann and collaborators
depend on their training and evaluation protocols; they are useful empirical
relations rather than universal exponents established by a thermodynamic
limit.

Take an illustrative fit for loss as a function of parameter count $n$ and
training-token count $D$:

$$
\mathcal L(n,D)=\mathcal L_\infty+A n^{-a}+B D^{-b},\qquad
 A,B,a,b>0.
$$

Assume a training cost $C=k nD$ with $k>0$. At fixed $C$, substitute
$D=C/(kn)$ and differentiate the excess loss:

$$
-aA n^{-a-1}+bB(k/C)^b n^{b-1}=0.
$$

There is a unique minimum, since one term falls and the other rises with
$n$. It gives

$$
n_* =\left(\frac{aA}{bB}\right)^{1/(a+b)}
 (C/k)^{b/(a+b)},\qquad D_* =\frac{C}{kn_*}.
$$

This optimization is exact **given the assumed fit and cost model**.
The exponents, coefficients and fitting range must come from data.
$\mathcal L_\infty$ is a fit offset, not an independently measured entropy
of language. Repeated internal blocks may increase computation without
increasing independent parameter count, requiring a different cost model.

**Example.** With $A=B=k=1$ and $a=b=1/2$, $n_*=D_*=\sqrt C$.
At $C=1$ the fitted excess loss is two; at $C=16$ each resource is four
and the excess loss is one. Everything changes smoothly. Equal exponents
other than $1/2$ would give a different loss reduction; a power law alone
is not a critical point.

## 4. Sudden improvement, and where it can come from

On some small algorithmic datasets a network first fits its training examples
while performing poorly on held-out cases, and much later its held-out
accuracy improves. The pattern is called **grokking**, and modular addition is
the standard example: the rule is fully known, and the model sees only a
subset of pairs.

A useful measurement protocol is to record training and
held-out losses *and* accuracies against optimizer step, with a fixed split of
distinct pairs, repeated over initializations and data fractions, and with any
regularization reported since it changes the optimization problem. Delayed
generalization is a phenomenon to explain. It does not follow from a falling
training loss, does not occur for every task or optimizer, and is not by
itself a thermodynamic transition.

Then the sharpest point of the week. Suppose each of $m$ required answers is
independently correct with probability $p$, and the metric awards credit only
when all are. Its expected value is $p^m$, and for $m = 20$ raising $p$
smoothly from $0.8$ to $0.9$ to $0.95$ moves the score from about $0.012$ to
$0.12$ to $0.36$. An all-or-nothing plot looks far sharper than the change in
per-answer competence. There is an even simpler discontinuity: greedy accuracy
on one binary item is a step function of $p$ at one half, while its log loss
is smooth throughout.

> **Physical picture.** Changing the metric does not change the model. This is
> the same phenomenon as defining an order parameter through a threshold: a
> smoothly varying underlying quantity, passed through a sharp function,
> produces a sharp-looking curve, and the sharpness belongs to the function.
> A physicist asked whether a transition is real would instinctively look at
> the *underlying* observable and at how the sharpness scales with system
> size; here the underlying observable is the held-out log loss, and $p^m$
> tells you that the apparent threshold moves with $m$ rather than with
> anything about the model.

## 5. The standard

These notes already contain a transition with every ingredient such a claim
requires, and Week 3 is where it was derived. Cover's counting has a sequence
of systems indexed by $N$; a control parameter $\alpha = P/N$; an order
parameter in the probability that a random labelling is realizable; and a
crossover whose width was *calculated* and shrinks like $N^{-1/2}$. Its
limiting step follows from a finite-$N$ counting formula, with no curve fitted
anywhere.

Read a claimed transition against that list. A model-size axis supplies a
sequence of systems and a control parameter, so two of the four are usually
present. The order parameter is most often missing: accuracy under a chosen
metric is a score, and becomes an order parameter only once tied to a quantity
whose limiting behaviour is being claimed. The crossover width is missing more
often still, since it needs several sizes with repeated runs and an estimate of
the scatter. Without those two, the figure records that a score rose.

A theorem about a global optimum also does not imply that a chosen optimizer
reaches it on the time scale of an experiment — a distinction Week 3 already
made about feasibility and search, arriving here in a new costume.

## Checkpoints with answers

**1. Does zero attention entropy in the first causal row indicate a failure?**
No. That row can access only itself, so zero is its maximum as well as its
minimum entropy.

**2. Why can the first position receive the most attention without learning?**
Every subsequent query can reach it. Summing uniform rows already gives
$M_1>M_2>\cdots>M_T$.

**3. Does the optimal-allocation formula prove empirical exponents?** No.
It derives the optimum conditional on their values and on the cost model.
Measurement and algebra play different roles.

---

## Subtleties and fine print

**Attention entropy, log likelihood and thermodynamic entropy production are
three quantities.** A sink is not a heat reservoir by definition, and the
auxiliary walk is useful when its observables answer a stated question about
attention, not as a thermal model.

**The metric criticism does not settle the question.** Showing that a choice of
metric can manufacture sharpness rules out one explanation. It does not rule
out every qualitative change in learned mechanisms, and the book says so.

**Scaling fits are protocol-dependent.** Training recipe, evaluation set,
tokenizer and the range of sizes actually tested all enter. Reporting the
range tested is part of reporting the result.

**The asymptotic offset is a fit parameter.** Reading it as the entropy of
language imports a claim that no fit establishes, and Week 1 supplies exactly
what such a claim would require.

**Repeated blocks break the cost model.** Before drawing an efficiency
conclusion about a recurrent architecture, the cost model must be rewritten;
Week 9 explains why the parameter count and the computation count come apart.

---

## Key claims and status

| Claim | Status |
|---|---|
| $0 \le H_i^A \le \log i$ on a fully causal prefix | [Exact], from the Week 1 inequality |
| A sink arises from accessibility alone, with no learned content | [Exact], by the uniform-attention exercise |
| Absorption times of the auxiliary chain | [Exact] for the stated matrix |
| The stationary irreversibility measure vanishes on the absorbing class | [Exact.] |
| Compute-optimal allocation from the assumed loss and cost models | [Exact] given the fit; inherits every assumption of it |
| Scaling exponents | [Empirical]; protocol-dependent, over the range tested |
| $P_{\rm all} = p^m$ for $m$ independent items | [Exact] under independence; real task errors may be correlated |
| Greedy accuracy is a step in $p$ while log loss is smooth | [Exact.] |
| Delayed generalization on small algorithmic datasets | [Empirical]; task- and optimizer-dependent |

---

## What the week establishes

1. An entropy bound for an attention row, with the accessibility baseline that
   makes cross-position comparison meaningful, and a null model in which a
   sink appears from accessibility alone.
2. An auxiliary chain whose stationary state is trivial and whose transient
   times are informative, together with the reason a thermal reading of it
   fails.
3. A compute-optimal allocation that follows exactly from an assumed fit, with
   the boundary between the exact step and the fitted input drawn.
4. That an all-or-nothing metric turns a smooth change in competence into a
   sharp curve, exactly, with the sharpness belonging to the metric.
5. A four-ingredient standard for a transition claim, met in full by a result
   the course derived in Week 3.

**What to carry forward.** Understanding the architecture now lets you choose
an observable, identify what it measures and calculate a useful baseline.
That also supports critical reading: state the control parameter, the range
or limit examined and the assumptions behind a claim. This is a use of the
course's conceptual foundation, alongside the ability to compute a prediction
and explain how training changes it.

## The practical session — Laboratory 7

**Varied:** the layer and head, across the whole pretrained decoder; the
attention score scale; and, separately, the decoding temperature.
**Held fixed:** the evaluation contexts, identical throughout; and the
accessibility baseline, reported alongside every entropy.
**Measured:** attention-row entropy as a map over layer and head; the entropy
response to rescaling the scores, kept distinct from the response to the
decoding temperature, which acts on the output logits; positions of equal
accessibility compared using the normalized entropy; and the mass absorbed by
the positions that receive attention from many queries.

**Product:** an entropy map over layer and head, and the entropy as a function
of the score scale. For a scaling or grokking study, both continuous losses
and task accuracy plotted with repeated runs, and the range actually tested
reported.

A null result, a smooth trend, or a threshold that turns out to depend on the
protocol is an admissible outcome and should be written up as one.

---

## Connections to other parts of the wiki

- [[week-03-perceptron-and-cover|Week 3]] supplies the standard of §5, and the
  feasibility-versus-search distinction that returns here.
- [[week-01-inferring-a-distribution|Week 1]] supplies the inequality behind
  the entropy bound, and what a claim about the entropy of language would
  require.
- [[week-09-four-indices|Week 9]] explains why a repeated-block architecture
  breaks the cost model of §3.
- [[week-12-inverse-potts-and-attention|Week 12]] is the contrasting case,
  where a known answer exists and a recovery claim can be checked.
- nn-llm-unit-3 — the block skeleton this note implements.

---

[[nn-llm-start-here|Start here]] · [[nn-llm-week-map|All weeks]] · [[nn-llm-resources|Book and experiments]] · [[week-12-inverse-potts-and-attention|Previous week]] · [[week-14-diffusion-and-thermodynamics|Next week]]
