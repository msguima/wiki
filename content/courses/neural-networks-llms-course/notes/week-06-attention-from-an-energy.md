---
title: "Week 6 — Dense memory, and attention derived from an energy"
type: lecture-notes
course: nn-llm-syllabus
semester: 1
week: 6
unit: 1
duration: "4 hours (2 hr lecture + 2 hr laboratory)"
status: draft
modified: 2026-09-19
---

# Week 6 — Dense Memory, and Attention Derived from an Energy

*Notes for [[nn-llm-syllabus|the neural-networks course]], Unit 1. Written by an AI assistant under the researcher's supervision; see ai-authorship.*

*A continuous memory can retrieve a weighted average of stored vectors.
Starting from an energy, we will derive those weights and prove descent for
the fixed-memory update. Allowing the vectors used for comparison and retrieval
to differ gives the attention operation used in a transformer.*

---

## Learning goals

1. Explain what resource a capacity statement counts, and why exponential
   capacity does not mean exponential information in a coupling matrix.
2. **Derive** the continuous recall update and **prove** that a full step
   decreases its energy, for every $\beta > 0$.
3. Identify the attention operation in that update, and state the exact
   condition under which a more general attention field has a potential.
4. Say what changes when the keys themselves move.

## Reading

**Primary text.** Chapter 2, §2.8 through §2.11.

**Primary literature**, through [[nn-llm-bibliography|the bibliography]]:
Krotov and Hopfield (2016); Demircigil and collaborators (2017); Ramsauer and
collaborators (2021); Vaswani and collaborators (2017) for the scaled
dot-product convention; Hoover and collaborators (2023) for an architecture
with its own explicitly defined energy. Krotov (2023) and Krotov and
collaborators (2025) are the reviews to read after the meeting.

**Prerequisites.** [[week-05-hopfield-and-capacity|Week 5]]. The log-sum-exp
function and its gradient, from [[week-01-inferring-a-distribution|Week 1]].

## The question to keep in view

How can a state retrieve information from several stored vectors without
choosing one in advance? We will compute a similarity score for each memory,
normalize those scores into weights and average the memories. This operation
becomes attention when the scoring vectors and the retrieved vectors are
allowed to differ. The derivation below also identifies the special case in
which repeated retrieval decreases a known energy.

## 1. Dense memory, and what a capacity counts

The Hopfield energy is quadratic in the pattern overlaps. Replacing the square
by a more rapidly growing function rewards a large overlap more sharply, and
expanding the result produces interactions among more than two spins at a
time. Krotov and Hopfield developed this route to **dense associative
memory**.

For suitable independent-pattern ensembles and retrieval definitions, a
degree-$n$ interaction supports capacity scales whose leading power is
$N^{n-1}$, and exponential interactions support $P = e^{cN}$ for suitable
positive $c$. These are model-dependent asymptotic statements, and the
distinction between retrieving a *typical* pattern and retrieving *all* of
them simultaneously is essential to them.

The book's reading note is the part to dwell on. The Hebbian model summarizes
its memories in an $N\times N$ coupling matrix. A dense-memory implementation
may instead retain the $P$ patterns explicitly, which is $PN$ stored numbers
and comparable work for a direct overlap evaluation. Exponential capacity as a
function of state dimension therefore does not imply exponential information
held in $N^2$ fixed-precision couplings.

> **Physical picture.** Ask, every time, what is being counted. "Capacity" in
> Week 5 counted attractors of a dynamics whose couplings were an $N \times N$
> object built once and then the only thing stored. "Capacity" here counts
> patterns the energy can distinguish, in a construction that may be holding
> all of them in memory. Both are legitimate and they are not the same
> quantity, and the difference is not a subtlety — it is the whole content of
> the comparison. The same question recurs in Week 13 about scaling laws,
> where the resource is compute.

## 2. A continuous memory, and a descent proof

Let the evolving state be a vector $\xi \in \mathbb R^d$ and collect $P$ fixed
memories as the rows of $X$. The score vector $X\xi$ holds the dot product of
the current state with each memory. The energy

$$
E(\xi) = \tfrac12 \xi^{\mathsf T}\xi - \mathrm{lse}_\beta(X\xi)
$$

rewards alignment with high-scoring memories through the second term while the
first prevents escape to infinite norm. Using the gradient of $\mathrm{lse}$
established in Week 1, the stationarity condition gives the update

$$
\xi_{\rm new} = X^{\mathsf T}\,\mathrm{softmax}(\beta X\xi),
$$

which scores the memories, converts the scores into positive normalized
weights, and returns a weighted mean of the memories. Every new state lies in
their convex hull.

To prove descent, write $f(\xi)=\operatorname{lse}_\beta(X\xi)$.
Convexity gives $f(y)\ge f(\xi)+\nabla f(\xi)\cdot(y-\xi)$, so

$$
E(y)\le U_\xi(y):=\tfrac12\|y\|^2-f(\xi)
 -\nabla f(\xi)\cdot(y-\xi),\qquad U_\xi(\xi)=E(\xi).
$$

The right side is a quadratic with minimum at $y=\nabla f(\xi)
=X^{\mathsf T}\operatorname{softmax}(\beta X\xi)=\xi_{\rm new}$.
Completing its square gives
$U_\xi(\xi_{\rm new})=U_\xi(\xi)-\tfrac12\|\xi_{\rm new}-\xi\|^2$.
Combining the two relations proves

$$
E(\xi_{\rm new}) \le E(\xi) - \tfrac12\lVert\xi_{\rm new}-\xi\rVert^2.
$$

This holds for every $\beta > 0$ with $X$ fixed. Bounded iterates plus the
inequality force the step differences to vanish, and any accumulation point is
stationary.

> **Physical picture.** Read the update as a thermal average and it stops
> being mysterious. The softmax weights are Boltzmann factors over the memory
> index, with $-\xi\cdot\boldsymbol x_\mu$ playing the role of the energy of memory
> $\mu$ and $\beta$ the inverse temperature *of that average*. The new state
> is then $\langle\boldsymbol x\rangle_\beta$, the ensemble mean of the memories. At
> small $\beta$ every memory contributes and the average sits near the
> centroid; at large $\beta$ the memory with the largest dot product
> dominates, if that maximum is unique. It is also the nearest in Euclidean
> distance when the memories have equal norms. Without that norm condition,
> a large dot product is not the same as a small distance. Nothing here is a bath and nothing is extensive —
> $\beta$ is a sharpness parameter of a finite weighted mean — but the
> intuition for how the mean moves with $\beta$ is exactly the familiar one.

## 3. Mixture and retrieval: a bifurcation, not a phase transition

Take two antipodal unit memories. After one update the state is parallel to
them, so a single scalar $a$ suffices, and the energy and update reduce to

$$
E(a) = \tfrac{a^2}{2} - \tfrac1\beta\log\big(2\cosh\beta a\big), \qquad a_{\rm new} = \tanh(\beta a).
$$

For example, start at $a=0.5$. At $\beta=0.5$ one update gives
$\tanh(0.25)\simeq0.244919$, moving toward the symmetric mixture.
At $\beta=2$ it gives $\tanh(1)\simeq0.761594$, moving toward the positive
memory. The slope $\beta\operatorname{sech}^2(\beta a)$ determines whether
small differences in state grow or shrink locally.

The mixture $a = 0$ has curvature $1-\beta$ and loses linear stability at
$\beta = 1$, where two nonzero stable fixed points appear, with $a^2 \simeq
3(\beta-1)/\beta^3$ near threshold. At finite $\beta$ the retrieved values
satisfy $|a| < 1$: retrieval is never exact at finite sharpness.

> **Physical picture.** $a_{\rm new} = \tanh(\beta a)$ is the mean-field
> ferromagnet's self-consistency equation, the bifurcation sits at $\beta = 1$
> exactly where $T_c$ sits, and the square-root growth of the order parameter
> is the familiar exponent. A physicist will recognize all of it in a second,
> which is precisely why the book stops to say what it is not. There is no
> extensive system here and no $N \to \infty$: this is the bifurcation of a
> one-dimensional map, and its partition function — a sum over two memories —
> is analytic in $\beta$ throughout. The resemblance is a resemblance of
> equations. Calling it a phase transition would import a thermodynamic limit
> that nothing has supplied.

## 4. What the identification with attention establishes

Attention uses a query to weight a collection of available items. **Keys** are
the vectors used to compute the scores, **values** the vectors combined with
the resulting weights, and a **head** is one such set of projections and
weighted averaging. Scaled dot-product attention uses $\beta = 1/\sqrt{d_k}$,
which is the initialization argument of Week 8 and not a measured temperature.

If the values are the keys, the attention output is *exactly* the continuous
memory update of §2, with the memories fixed. Independent query and key
projections do not obstruct that reading. So the identification is real, and
it is exact in the state space where it was proved.

Now push it. For general values, the update field is $g(\xi) = M^{\mathsf
T}\mathrm{softmax}(\beta X\xi)$, whose Jacobian is $\beta M^{\mathsf T} D X$
with $D = \mathrm{diag}(p) - pp^{\mathsf T}$. A continuously differentiable
field on $\mathbb R^d$ is a Euclidean gradient field precisely when its
Jacobian is symmetric everywhere, so the condition is

$$
M^{\mathsf T} D X = X^{\mathsf T} D M \quad\text{for every attainable } p.
$$

Taking $M = X$ satisfies it. So does $M = cX + \boldsymbol 1 b^{\mathsf T}$, since
$D\boldsymbol1 = 0$. For an explicit counterexample take $\beta=1$,

$$
X=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
M=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
$$

At $\xi=0$ the weights are $p=(1/2,1/2)$ and

$$
J_g(0)=M^{\mathsf T}DX=\frac14\begin{pmatrix}1&-1\\0&0\end{pmatrix}.
$$

The off-diagonal derivatives disagree, so no scalar Euclidean potential has
$g$ as its gradient on $\mathbb R^2$. The test assumes values and keys have
the same dimension as the state; a map into another dimension is not a
vector field on that state space.

This is the familiar curl-free test for a potential. If $g=\nabla f$, then
$\xi-g(\xi)=\nabla(\|\xi\|^2/2-f)$ is a candidate energy gradient.
That identifies a potential; it does not yet show that the full iteration
$\xi\mapsto g(\xi)$ decreases it. The majorization argument above supplies
that extra result for the fixed-memory choice $M=X$.

Two further restrictions close the section. In **self-attention** the queries
and the available items come from the same sequence, so if the sequence
evolves the keys themselves change, and a candidate energy for the whole
sequence must be differentiated accounting for each vector appearing as both
query and key — derivatives the fixed-memory proof does not contain. And a
transformer applies successive layers, generally with different parameters: a
sequence of maps that each decrease *different* energies does not decrease one
common energy, and parameter sharing is neither necessary nor sufficient for
one to exist.

## 5. When new inputs keep arriving

Recall so far has meant evolving a state against fixed memories. §2.11 asks
what happens when new information arrives before recall has finished, and
reduces the question to a scalar driven map, $a_{i+1} = \tanh(\beta a_i +
u_i)$. Holding $\beta$ fixed does not make the input constant. For $0 < \beta
< 1$ the derivative with respect to the previous state is bounded by $\beta$,
so two states exposed to the same inputs become less distinguishable at every
step.

That is the bridge into Unit 2, and Week 9 develops it: a route through the
computation is not the same thing as retained information.

## Checkpoints with answers

**1. Where does the new state lie?** In the convex hull of the fixed memories,
because all weights are nonnegative and sum to one. It need not equal any
single memory.

**2. Are keys and values doing the same job?** Keys determine the weights;
values are what those weights average. They coincide in the energy-derived
model. Attention allows them to differ, as the explicit matrix example shows.

**3. Why is finding a potential insufficient for a full-step descent claim?**
A gradient direction gives a local decrease for a sufficiently small step.
A finite iteration needs its own step-size or majorization argument.

---

## Subtleties and fine print

**Descent is not retrieval.** The inequality of §2 guarantees the energy falls
and the steps shrink. It does not guarantee convergence to a single memory,
and a unique limit requires further conditions.

**The energy lives in query space with the memories fixed.** Quoting the
descent result without that qualification is the most common misuse of it, and
§4 is the demonstration of what goes wrong.

**A potential does not imply a finite step descends it.** The family $M = cX +
\boldsymbol1 b^{\mathsf T}$ has an explicit potential, and that alone says nothing
about whether the *iteration* decreases it. The majorization inequality is
what supplies that for $M = X$, and it has to be redone otherwise.

**The scaling $\beta = 1/\sqrt{d_k}$ is an initialization argument.** It
moderates the growth of score fluctuations with dimension under an assumption
of independent unit-variance coordinates. Learned queries and keys need not
satisfy that assumption.

**Architectures with their own energy must be read on their own terms.** The
Energy Transformer defines an energy and a dynamics explicitly; conclusions
about it follow from its definitions, not from the fixed-memory proof here.

---

## Key claims and status

| Claim | Status |
|---|---|
| Degree-$n$ interactions give capacity scales with leading power $N^{n-1}$ | [Model-specific]; ensemble and retrieval criterion dependent |
| Exponential interactions support $P = e^{cN}$ for suitable $c$ | [Model-specific]; not a universal maximum |
| $\nabla_\xi E = \xi - X^{\mathsf T}\mathrm{softmax}(\beta X\xi)$ | [Exact.] |
| $E(\xi_{\rm new}) \le E(\xi) - \tfrac12\lVert\xi_{\rm new}-\xi\rVert^2$ | [Exact] for every $\beta>0$, $X$ fixed |
| Every update lies in the convex hull of the memories | [Exact.] |
| Mixture loses stability at $\beta = 1$; $a^2\simeq3(\beta-1)/\beta^3$ | [Exact] stability boundary; [Asymptotic] amplitude near the bifurcation |
| Key-equals-value attention *is* the memory update | [Exact] in the stated state space |
| Gradient field iff $M^{\mathsf T}DX = X^{\mathsf T}DM$ everywhere | [Exact]; $M=X$ sufficient, not necessary |
| A general attention field need not have a potential | [Exact], by the $2\times2$ counterexample |
| Contraction of the driven scalar map for $0<\beta<1$ | [Exact.] |

---

## What the week establishes

1. A capacity statement counts a resource, and the resource differs between
   the Hebbian and dense constructions even when the word does not.
2. The continuous memory update is the gradient-based fixed-point iteration of
   an explicit energy, and a *full* step decreases that energy by at least
   half the squared step, for every sharpness and every fixed memory set.
3. With values equal to keys, that update is the attention operation exactly —
   the derivation the course was built towards.
4. For general values, having a potential is equivalent to a symmetry
   condition on the Jacobian at every attainable state, which some attention
   fields satisfy and others demonstrably violate.

**What to carry forward.** The identification is real and it is narrow, and
both halves matter. A student who leaves with only the first half will read
every transformer as an energy-descent machine; one who leaves with only the
second will miss that the course's central derivation went through. The
honest summary is the one the book gives: an update with an energy in memory
space does not by itself supply an energy for an entire transformer.

## The practical session — Laboratory 3

**Varied:** the sharpness $\beta$, in the antipodal two-memory system; then
the value matrix $M$, with the keys $X$ held fixed.
**Held fixed:** the memory set, the norm convention, and the state space —
declared explicitly, since the whole point is that the results are statements
about a state space.
**Measured:** the fixed points against the bifurcation at $\beta = 1$; the
energy at every update, checked against the descent inequality term by term;
and the antisymmetric part of the Jacobian as $M$ is moved away from $X$.

**Product:** the fixed-point diagram with the bifurcation located; a table of
$E(\xi_{\rm new})$ against $E(\xi) - \tfrac12\lVert\Delta\xi\rVert^2$ showing
the inequality holding; and the value matrix at which the antisymmetric part
first becomes nonzero, with the potential lost.

A larger-memory experiment must state its pattern ensemble, norm convention,
noise level and retrieval criterion. A finite sweep establishes neither
exponential capacity nor its absence.

---

## Connections to other parts of the wiki

- [[week-05-hopfield-and-capacity|Week 5]] supplies the discrete construction
  this week makes continuous, and the capacity whose resource §1 contrasts.
- [[week-01-inferring-a-distribution|Week 1]] supplies the log-sum-exp
  gradient used in §2, and the warning about the Gibbs reading that §3
  applies again.
- Week 8 builds the full attention layer whose special case §4 identifies, and
  supplies the $1/\sqrt{d_k}$ argument.
- Week 9 develops the driven map of §5 into the course's treatment of
  recurrence and memory.
- Week 11 studies a particle dynamics on the sphere whose monotone function is
  proved separately, precisely because the fixed-memory proof does not extend
  to it.
- nn-llm-unit-1 — the block skeleton this note implements.

---

[[nn-llm-start-here|Start here]] · [[nn-llm-week-map|All weeks]] · [[nn-llm-resources|Book and experiments]] · [[week-05-hopfield-and-capacity|Previous week]] · [[week-07-representations-and-position|Next week]]
