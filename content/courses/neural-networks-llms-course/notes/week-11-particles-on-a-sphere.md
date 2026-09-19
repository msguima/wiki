---
title: "Week 11 — Particles on a sphere, and observables of a trained model"
type: lecture-notes
course: nn-llm-syllabus
semester: 1
week: 11
unit: 3
duration: "4 hours (2 hr lecture + 2 hr laboratory)"
status: draft
modified: 2026-09-19
---

# Week 11 — Particles on a Sphere, and Observables of a Trained Model

*Notes for [[nn-llm-syllabus|the neural-networks course]], Unit 3. Written by an AI assistant under the researcher's supervision; see [[ai-authorship]].*

*A trained model is now in hand, and it produces vectors and attention
matrices by the thousand. Which of those numbers mean something? This meeting
answers by doing the calculation first: an idealized dynamics of unit vectors
where collective behaviour can be derived exactly, and only then the
measurements, read against it. The order matters. A picture of vectors forming
groups is suggestive and specifies no mechanism.*

---

## Learning goals

1. Distinguish token alignment, matrix rank, clustering and consensus as four
   different observables, and give a configuration separating them.
2. **Prove** that the specified spherical dynamics has a monotone function,
   and list the ingredients whose removal removes the proof.
3. **Derive** the exact two-particle alignment law and the participation rank
   along its trajectory.
4. Say which of these observables survive a change of basis.

## Reading

**Primary text.** Chapter 4, §4.1 and §4.2.

**Primary literature**, through [[nn-llm-bibliography|the bibliography]]:
Geshkovski and collaborators for the interacting-particle view; Dong,
Cordonnier and Loukas for rank loss in a different, explicitly restricted
architecture; Radford and collaborators for the pretrained decoder the
laboratories measure.

**Prerequisites.** [[week-08-one-head-and-a-decoder|Week 8]], whose
normalization discussion is what makes the sphere here an idealization rather
than a description.

## What will be measured?

A hidden representation is a vector computed inside the network. Two such
vectors can be nearly parallel, span only a few directions, or form separated
groups. These are different geometric statements. We first define quantities
that distinguish them, then study a specified unit-vector dynamics where
their evolution can be calculated. None requires identifying a component of
a hidden vector with a named semantic property.

## 1. What is fixed when a model is inspected

Freeze the parameters. The laboratories of this unit measure a released
pretrained decoder rather than one trained in the course, in the small
configuration described by Radford and collaborators — small enough to inspect
on ordinary equipment and public enough that a measurement can be repeated.
Another model serves equally well provided its layer count, head count,
tokenizer and context limit are recorded, since every observable below depends
on all four.

Then choose evaluation sequences and record the representations and attention
matrices. An average over tokens in one sentence is not an average over
independently sampled sentences, and when estimating uncertainty one resamples
independent sequences or documents rather than treating all token pairs as
independent.

Four observables, and they are not interchangeable. The **overlap** $c_{ij} =
\boldsymbol x_i\cdot\boldsymbol x_j$ between normalized token directions measures alignment.
The **mean direction** and its squared magnitude summarize the average pair
overlap. The **participation rank** measures the effective spread across singular
directions, weighting their sizes rather than counting only nonzero ones. And
*clustering*, *consensus* and *rank collapse* are three further descriptions
that overlap without being the same.

Put the normalized nonzero vectors in the rows of $X$, with $T$ rows.
Let $\lambda_a$ be the eigenvalues of $X^{\mathsf T}X$ (the squared singular
values of $X$). Define

$$
\bar x=\frac1T\sum_i x_i,\qquad
 \|\bar x\|^2=\frac1{T^2}\sum_{i,j}c_{ij},\qquad
 R_{\rm part}=\frac{(\sum_a\lambda_a)^2}{\sum_a\lambda_a^2}.
$$

The **algebraic rank** counts nonzero $\lambda_a$; participation rank weights
their sizes and can be noninteger. **Consensus** means all directions agree;
**clustering** means specified groups of nearby directions. A clustering claim
must specify a distance and a grouping rule.

A four-vector example separates them. Take two pairs pointing
along $\pm\boldsymbol u$: they form two perfectly separated groups, every row lies in
the same one-dimensional subspace, the participation rank is one, and the mean
direction vanishes. Make all four identical and the rank is still one but the
mean direction has unit length. Rank one does not distinguish the two.

Orthogonal basis changes preserve Euclidean overlaps and singular values.
A nonorthogonal invertible change can alter angles and participation rank,
while **algebraic rank remains unchanged**. For example, $X=I_2$ has rank
two and participation rank two; multiplying by $\operatorname{diag}(2,1)$
leaves algebraic rank two but gives eigenvalues $(4,1)$ and participation
rank $25/17\simeq1.470588$. Whether rows are normalized or centred must
also be stated. Normalized overlaps are invariant under positive rescaling
of individual vectors, but not under arbitrary changes of metric.

## 2. A dynamics that can be solved

Normalization suggests an idealization: let each token be a unit vector moving
on a sphere. The book defines a dynamics on that state space rather than
obtaining it by deleting parameters from a decoder, and the distinction is the
whole of §3 below.

To preserve the norm, project each proposed velocity onto the tangent plane.
The weights are softmax weights of the mutual dot products, all pairs
including self-pairs are allowed, values equal the vectors used as keys, and
there are no learned projections, no positional operation and no mask. The
tangential projection makes the motion a rotation, and the norms are conserved
exactly.

Write every ingredient explicitly, with $\beta>0$:

$$
P_i=I-x_ix_i^{\mathsf T},\qquad Z_i=\sum_j e^{\beta x_i\cdot x_j},\qquad
 A_{ij}=\frac{e^{\beta x_i\cdot x_j}}{Z_i},\qquad
 \dot x_i=P_i\sum_j A_{ij}x_j.
$$

Since $x_i\cdot P_iv=0$, $d\|x_i\|^2/ds=0$: initially unit vectors stay
unit. Now define

$$
\Phi(X)=\frac1{2\beta}\sum_{i,j}e^{\beta x_i\cdot x_j}.
$$

Differentiating both occurrences of $x_i$ in the sum gives
$\nabla_i\Phi=\sum_j e^{\beta x_i\cdot x_j}x_j$.
The self-term is removed by $P_i x_i=0$, and
$\dot x_i=Z_i^{-1}P_i\nabla_i\Phi$. Therefore

$$
\frac{d\Phi}{ds}=\sum_i\nabla_i\Phi\cdot\dot x_i
 =\sum_i\frac{\|P_i\nabla_i\Phi\|^2}{Z_i}\ge0.
$$

This proof uses symmetric pair scores and projected motion on the sphere.
It does not require a fixed-memory argument from Week 6.

> **Physical picture.** This is a gradient flow with a metric, and reading it
> that way is what makes the result feel inevitable rather than lucky. The
> velocity is the tangential gradient of a potential, rescaled by a positive
> state-dependent factor $Z_i^{-1}$ — a **mobility**. A gradient flow with
> positive mobilities monotonically increases its potential, which is an
> H-theorem for this model, and the sign is fixed by the mobility being
> positive rather than by anything about attention. What the theorem gives is
> monotonicity plus compactness, hence convergence of $\Phi$. What it does not
> give is a classification of the stationary states, or a guarantee that every
> initial condition reaches consensus.

## 3. Two particles, exactly

At vanishing sharpness the weights become uniform, and for two particles the
overlap obeys a closed equation. Differentiating it and substituting the
velocities, using that both vectors are unit, gives

$$
\dot x_1=\tfrac12(x_2-cx_1),\qquad
 \dot x_2=\tfrac12(x_1-cx_2),\qquad
 \dot c=\dot x_1\cdot x_2+x_1\cdot\dot x_2=1-c^2.
$$

Integrating $dc/(1-c^2)=ds$ yields

$$
c(s) = \tanh\big[s + \mathrm{artanh}\,c(0)\big], \qquad -1 < c(0) < 1.
$$

Every non-antipodal pair approaches alignment. The exactly antipodal pair is
stationary and unstable, and it must not be lost by dividing by $1-c^2$ during
the integration.

The $2\times2$ Gram matrix has diagonal entries one and off-diagonal
entries $c$, so its eigenvalues are $1\pm c$. Consequently
$R_{\rm part}=2/(1+c^2)$. For an initially orthogonal pair it falls from
two toward one. For $-1<c(0)<0$, it first rises to two as $c$ passes through
zero, then falls. Monotone alignment does not imply monotone participation
rank for every initial condition. Two initially orthogonal vectors reach
$c = 0.9$ at $s = \tfrac12\log 19 \simeq 1.47$.

On a circle the same dynamics reduces exactly to an angular equation whose
right-hand side is

$$
\dot\phi_i=\sum_j A_{ij}\sin(\phi_j-\phi_i),\qquad
 x_i=(\cos\phi_i,\sin\phi_i).
$$

This follows by dotting the vector velocity with the unit tangent
$(-\sin\phi_i,\cos\phi_i)$.

> **Physical picture.** At uniform weights that is the identical-frequency
> attractive Kuramoto model in a rotating frame, and the student who has met
> synchronization will read the alignment as phase locking. The honest caveat
> is the interesting part: at nonzero sharpness the coefficients depend on the
> phases themselves, so the system is not Kuramoto with a fixed coupling — it
> is a Kuramoto-like model whose couplings are functions of the state.
> Natural frequencies, learned projections and masking would each specify a
> different model again. The reduction is exact; the identification with a
> standard model holds in one limit.

## 4. What the large-$T$ description would require

For many particles the velocity can be written as an integral against the
empirical measure, which is exact for the finite measure, and the candidate
large-$T$ description is a continuity equation on the sphere expressing
conservation of particle number. Convergence of empirical measures, its rate,
and the interchange of the large-$T$ and long-depth limits all require
additional analysis. A finite cloud of token vectors does not establish those
limits.

The rank-loss results of Dong, Cordonnier and Loukas concern a different
discrete architecture with explicit restrictions on its components, and should
be read with the role of residual connections and local nonlinear maps in
view. The two-particle law here neither proves their rate nor implies that the
full decoder of Week 8 must lose its useful representations.

## Checkpoints with answers

**1. Can rank one mean two opposed clusters rather than consensus?** Yes.
The rows $(u,u,-u,-u)$ span one line, but their mean is zero. Rows
$(u,u,u,u)$ have the same rank and a unit mean.

**2. What happens to algebraic rank under an invertible basis change?** It
is unchanged. Participation rank and normalized angles need not be; they
also use a metric or relative singular-value sizes.

**3. If two unit vectors have $c=-1/2$, what is their participation rank?**
$2/(1+1/4)=1.6$. As uniform-weight dynamics raises $c$ toward zero, that
rank rises to two before declining toward one.

---

## Subtleties and fine print

**The sphere is an idealization, entered knowingly.** Week 8 showed a residual
sum leaving the normalization sphere within a single block. This model is a
specified reduction with its own state space, not a description of a trained
decoder's hidden states.

**An overlap histogram is not a spin-glass overlap distribution.** It records
how many pairs have a given similarity in a chosen basis. Reading it as the
thermodynamic $P(q)$ requires an ensemble and a corresponding identification,
neither of which a single trained model supplies.

**Monotonicity does not classify the attractors.** $\Phi$ increases and is
bounded, so it converges. Which configurations it converges to, and from
which basins, is a further question.

**Every ingredient in §2 is load-bearing.** General key and value projections,
or a causal mask, alter the argument. The proof is for unit vectors on a
product of spheres with a symmetric exponential kernel and values equal to
keys.

**Uncertainty comes from resampling sequences, not token pairs.** Token pairs
within a sentence are dependent, and treating them as independent
observations understates the error on every quantity in §1.

---

## Key claims and status

| Claim | Status |
|---|---|
| Norms conserved by the tangential projection | [Exact.] |
| $\mathrm d\Phi/\mathrm ds = \sum_i\lVert P_i\nabla_i\Phi\rVert^2/Z_i \ge 0$ | [Model-specific]: unit vectors, symmetric exponential kernel, values equal keys, no projections, no mask |
| $\dot c = 1 - c^2$ and $c(s) = \tanh[s + \mathrm{artanh}\,c(0)]$ | [Exact] at uniform weights |
| $R_{\rm part} = 2/(1+c^2)$ for two unit vectors | [Exact.] |
| Exact angular reduction to a $\sin(\phi_j-\phi_i)$ form | [Exact]; identical-frequency Kuramoto only at uniform weights |
| Two groups and one aligned group both give rank one | [Exact], by the four-vector example |
| Continuity equation as the large-$T$ description | Candidate; convergence and limit interchange not established here |
| Rank loss in pure attention networks | [Stated — refs]; a different architecture with its own restrictions |

---

## What the week establishes

1. Four distinct observables, with an explicit four-vector configuration on
   which rank and mean direction disagree.
2. A monotone function for the specified spherical dynamics, proved as a
   gradient flow with positive mobilities, together with the list of
   ingredients whose removal removes it.
3. An exact alignment law for two particles, with the participation rank along
   the same trajectory in closed form and a calculable time scale.
4. An exact angular reduction that becomes Kuramoto in one limit and is
   state-dependent otherwise.

**What to carry forward.** Two things, and the second is the unit's spine.
Calculate in the idealization first, then measure — so that a measurement has
something to be read against. And ask of every reported observable whether it
would change under a transformation the architecture admits: Week 7 supplied
the transformations, this week supplies the observables, and Week 13 is where
the answer decides whether a claim survives.

## The practical session — Laboratory 5

**Varied:** the layer, from the embedding through to the final block; and the
model state, between the trained weights, the initialization, and the trained
weights with one component removed.
**Held fixed:** the evaluation sequences, identical across every condition;
and the declared choice of whether rows were centred before computing the
rank.
**Measured:** the distribution of normalized pair overlaps, the mean
direction, and the singular-value spectrum, layer by layer.

**Product:** overlap histograms by layer and a clustering order parameter
against depth, with the centring stated; the same quantities at
initialization for comparison; and a statement of which of the reported
numbers would change under a non-orthogonal change of basis.

The two-particle calculation is a calibration example. The trained model is
not required to reproduce it, and a finite group pattern is not a
thermodynamic phase.

---

## Connections to other parts of the wiki

- [[week-08-one-head-and-a-decoder|Week 8]] showed a state leaving the
  normalization sphere, which is why §2 is an idealization.
- [[week-07-representations-and-position|Week 7]] supplies the coordinate
  freedom against which §1 asks which observables are invariant.
- [[week-06-attention-from-an-energy|Week 6]] proved a descent result for
  *fixed* memories; here the keys move with the state, which is why §2 needs
  its own proof.
- [[week-12-inverse-potts-and-attention|Week 12]] turns to a model where both
  the generating distribution and the fitted conditionals can be written down.
- nn-llm-unit-3 — the block skeleton this note implements.

---

[[nn-llm-start-here|Start here]] · [[nn-llm-week-map|All weeks]] · [[nn-llm-resources|Book and experiments]] · [[week-10-gradients-and-generation|Previous week]] · [[week-12-inverse-potts-and-attention|Next week]]
