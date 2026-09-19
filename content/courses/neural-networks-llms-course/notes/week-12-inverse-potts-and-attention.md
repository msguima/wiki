---
title: "Week 12 — The inverse Potts problem and factored attention"
type: lecture-notes
course: nn-llm-syllabus
semester: 1
week: 12
unit: 3
duration: "4 hours (2 hr lecture + 2 hr laboratory)"
status: draft
modified: 2026-09-19
---

# Week 12 — The Inverse Potts Problem and Factored Attention

*Notes for [[nn-llm-syllabus|the neural-networks course]], Unit 3. Written by an AI assistant under the researcher's supervision; see ai-authorship.*

*A Potts model supplies a source whose conditional probabilities can be
calculated exactly. We use it to understand prediction of a missing spin,
fitting by conditional losses and a restricted attention map. Known couplings
make it possible to test what a fit actually recovers.*

---

## Learning goals

1. **Derive** the single-site conditional of a Potts model and explain why the
   partition function cancels.
2. Explain why a sum of conditional losses is a legitimate fitting criterion
   and what it is not.
3. **Identify** the restricted attention whose scores reproduce a Potts
   conditional, and state the conditions for a common joint model.
4. Fix the gauge freedom of the couplings, and say what recovering a coupling
   can mean.

## Reading

**Primary text.** Chapter 4, §4.3 and §4.4, including the gauge accounting of
§4.3.3.

**Primary literature**, through [[nn-llm-bibliography|the bibliography]]:
Rende, Gerace, Laio and Goldt for the factored-attention correspondence; Cui
and collaborators for the solvable attention model of §4.

**Prerequisites.** [[week-01-inferring-a-distribution|Week 1]] for the
cross-entropy decomposition, which is applied here to conditionals.
[[week-11-particles-on-a-sphere|Week 11]].

## Predict a missing spin

In a language model we predict a token from observed tokens. A closely related
physical problem predicts one spin from its neighbours. Here the full source
is specified, so we can calculate the right answer and examine what fitting
recovers. We use $q$ for the number of Potts colours; it is not the overlap
$c_{ij}$ of Week 11.

## 1. The conditional that costs $q$ terms

In the direct problem, couplings determine a distribution over configurations.
In the **inverse problem**, observed configurations are used to infer
couplings — the same reversal of roles between parameters and observations
that Week 1 performed on a two-state system.

Let $s_i$ be the colour of a Potts spin at site $i$, with $q$ colours, and let
the log weight carry fields and pairwise interactions, with inverse
temperature absorbed into the dimensionless parameters:

$$
p(s)=\frac1Z\exp\left[\sum_i h_i(s_i)+\sum_{i<j}J_{ij}(s_i,s_j)\right].
$$

For reversed indices define $J_{ji}(b,a)=J_{ij}(a,b)$. There are $T$ sites. The normalizer sums over $q^T$ configurations and
rapidly becomes hopeless.

Now ask a different question. To predict one missing spin, hold every other
spin fixed and compare the weights obtained by changing only that one. Every
term not containing it cancels between numerator and denominator, and what
remains is a softmax over $q$ scores, each a field plus a sum of couplings to
the observed neighbours. **Only $q$ possibilities are normalized, whatever the
size of the configuration space.** Explicitly, with $s_{\setminus i}$
denoting all spins except $i$,

$$
z_i(a)=h_i(a)+\sum_{j\ne i}J_{ij}(a,s_j),\qquad
p(s_i=a\mid s_{\setminus i})=\frac{e^{z_i(a)}}{\sum_{b=1}^q e^{z_i(b)}}.
$$

The cost of **normalizing** is $q$ terms. Computing all scores also sums over
the neighbours and is not independent of the system size.

> **Physical picture.** This is the move that makes direct-coupling analysis
> work, and it is one a physicist has made many times without naming it: a
> local field is cheap where a free energy is expensive. Computing $Z$ means
> summing over the whole configuration space; computing the conditional at one
> site means summing over the states of that site, with everything else held
> as a boundary condition. The exponential cost lives entirely in the
> normalization of the *joint*, and asking a conditional question never touches
> it. Students who have done contact prediction in proteins will recognize
> the entire construction on sight.

For three binary spins $s_i=\pm1$, take
$p(s)\propto e^{K(s_1s_2+s_2s_3)}$, with $K=\tfrac12\log3$.
Holding the neighbours fixed gives

$$
p(s_2=+1\mid s_1,s_3)=\frac1{1+e^{-2K(s_1+s_3)}}.
$$

For $(s_1,s_3)=(+1,+1)$ this is $1/(1+1/9)=9/10$.
For opposite neighbours their fields cancel and the answer is $1/2$.
All eight configurations can be enumerated to check the cancellation of $Z$.

## 2. Pseudolikelihood: a criterion, not a factorization

Given observed configurations, fit the parameters by minimizing the average
negative log conditional over all sites and samples. This is the negative log
**pseudolikelihood**, and it avoids $Z$ entirely. For $M$ configurations,

$$
\widehat{\mathcal L}_{\rm PL}(\theta)
 =-\frac1{MT}\sum_{\mu=1}^M\sum_{i=1}^T
 \log p_\theta(s_i^\mu\mid s_{\setminus i}^\mu).
$$

This is distinct from the chain-rule likelihood of a left-to-right decoder:
here the conditional can see both sides of the missing site.

It is a fitting criterion. The terms within one configuration are generally
dependent, and the product is *not* a factorization of the joint distribution
into independent observations. What makes it legitimate is the population
statement: applying the Week 1 cross-entropy decomposition to each conditional
shows the population criterion is minimized by matching the true conditionals,
if the model can represent them. The data distribution stays fixed and the
fitted parameters vary, exactly as in Week 1.

For strictly positive distributions on a finite configuration space, all
single-site conditionals determine the joint. The argument is a chain of
ratios: for configurations differing at one site, the ratio of joint
probabilities equals the ratio of their conditionals there; connect any two
configurations by single-site changes, multiply, and normalization fixes the
constant. That does *not* prove separately fitted, unconstrained conditional
models are mutually compatible — parameter sharing and interaction symmetry
are what make them describe one joint model.

## 3. The bridge to factored attention

Rende and collaborators study a restricted attention in which position
determines the weights and token identity determines the values. The algebra
is visible without a full transformer. Encode a colour as a one-hot vector,
choose position weights independent of content, and let a factorized score be
a field plus a weighted sum of a shared colour matrix applied to the
neighbours' encodings. Writing the one-hot colour at site $j$ as $e_{s_j}$ gives

$$
z_i=h_i+\sum_{j\ne i}A_{ij}Ue_{s_j},\qquad
 z_i(a)=h_i(a)+\sum_{j\ne i}A_{ij}U_{a,s_j}.
$$

Thus its components have the Potts form with $J_{ij}(a,b)=A_{ij}U_{ab}$,
and a final softmax supplies the conditional. Masking one site
and training on its true colour gives precisely the pseudolikelihood.

The identification is exact *within that family*, and the qualifications are
the content. Softmax position weights are nonnegative and row-normalized, so
zeros require a mask or a limiting score. A shared colour matrix and any
readout gains restrict the factorization further. To obtain a common pairwise
joint distribution one needs $J_{ij}(a,b) = J_{ji}(b,a)$ up to transformations
absorbable in the fields — symmetric $A$ with zero diagonal and symmetric $U$
suffices. Arbitrary directed conditionals need not satisfy it.

Two further differences close the section. Ordinary content-dependent
self-attention has weights that change with the very colours being
conditioned on, which the factorization does not. And predicting a masked site
uses both its preceding and following sites, whereas autoregressive training
uses only a prefix. The two objectives should not be silently identified.

> **Physical picture.** The correspondence is a statement about a *restricted*
> architecture, and the restriction is exactly the physics. An effective pair
> coupling that factorizes as a position factor times a colour factor is a
> separable interaction, and separability is a strong assumption that a
> general pair coupling does not satisfy. So the right reading is not "attention
> is an inverse Potts solver" but "a separable attention is exactly a
> separable Potts model, and the separability is testable". The book's worked
> example is the test in its simplest form: uniform position weights and a
> colour matrix proportional to the identity give a conditional favouring
> colours frequent among the neighbours, and direct enumeration for two sites
> at two colours confirms the number.

## 4. Gauge freedom, and what recovery means

Different parameter tables can define the same probability law. This
redundancy is a **gauge freedom**, and it is a reparametrization rather than
an additional interaction. Before comparing two inferred coupling tensors, fix
the same convention.

For each $q\times q$ coupling table define the row means $r_a$, column
means $c_b$ and total mean $m$. Then

$$
J^0_{ab}=J_{ab}-r_a-c_b+m,\qquad
 \sum_a J^0_{ab}=\sum_bJ^0_{ab}=0.
$$

Since $J_{ab}=J^0_{ab}+r_a+c_b-m$, add $r_a$ to the field at the first
site and $c_b$ to the field at the second; the remaining constant changes
only the partition function. This explicitly preserves the probability law.
For $J=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, the means are
$r=(1.5,3.5)$, $c=(2,3)$, $m=2.5$, so $J^0=0$. The apparent pair
interaction consists entirely of single-site terms. The removed pieces are absorbed into the fields at the two sites
and a constant into $Z$, so the resulting distributions agree exactly. Raw
parameter correlations nevertheless change under the transformation, and for a
factored model one should compare the *effective* tensor $A_{ij}U_{ab}$ rather
than interpreting either factor alone.

This is a freedom to describe one probability law by several parameter
tables. Comparing the zero-sum parts removes that ambiguity. The word
*gauge* refers to this specific reparametrization; a field-theory analogy is
not required for the calculation.

## 5. What a learning transition would mean

Position and content offer different predictive strategies: a rule that always
consults the previous position uses position, while a rule searching for a
matching content feature can transfer across positions. To make the competition
measurable one defines synthetic data with a known content direction and
compares the learned direction with the planted one — a task-defined order
parameter, not a universal observable for language understanding.

In the solvable attention model of Cui and collaborators, tied low-rank query
and key matrices, a specified high-dimensional data distribution and a
proportional sample-size limit permit an analysis of the global
empirical-loss optimum, and the competition changes as the sample-to-dimension
ratio is varied. That setting gives a definite meaning to a learning
transition; its assumptions and its relation to actual optimization dynamics
must be read separately.

For orientation, a Landau form such as
$F(m)=a m^2/2+b m^4/4$, with $b>0$, has minima $m=0$ for $a>0$ and
$m=\pm\sqrt{-a/b}$ for $a<0$. This is an illustrative calculation only: it is not derived for that model and supplies neither its
threshold nor its transition order. What it does supply is a reminder of what
a proposed effective objective would give. And the honest standard is nearby —
Cover's counting in Week 3 has a sequence of systems, a control parameter, an
order parameter and a calculated crossover width, with a limiting step
following from a finite-$N$ formula and no curve fitted. That is what a
transition claim should be read against, and Week 13 makes the reading.

## Checkpoints with answers

**1. Why does the partition function disappear from a conditional?** Every
candidate value of the missing spin carries the same factor $1/Z$. Terms
that do not involve that spin are also common to numerator and denominator.

**2. Is pseudolikelihood the joint probability of a configuration?** Generally
not. Its factors condition on overlapping sets of spins. Its justification is
the population conditional-loss criterion, not independence of those factors.

**3. What interaction remains in the table $\begin{pmatrix}1&2\\3&4\end{pmatrix}$
after fixing the zero-sum convention?** None: all entries of $J^0$ vanish.
The original law is reproduced with shifted single-site fields.

---

## Subtleties and fine print

**The pseudolikelihood terms are dependent.** The criterion is legitimate by
its population minimizer, not by a factorization argument. Quoting it as a
likelihood is wrong.

**Conditionals determine the joint; fitted conditionals need not be
compatible.** The ratio-chain argument is about the true positive
distribution. Separately fitted unconstrained models can fail the joint
consistency test, and the book's exercise on two binary variables exhibits the
necessary condition.

**Check that the generating couplings lie in the fitted family.** A poor
recovery outside the family is a model limitation and not an optimization
failure, and the laboratory is instructed to verify the containment first.

**Masked-site and autoregressive objectives differ.** One sees both sides, the
other a prefix. Results about either do not transfer to the other without
argument.

**Identifiability and regularization must be declared before a recovery
claim.** Varying sample size and regularization together makes the result
uninterpretable; the laboratory varies them separately for that reason.

---

## Key claims and status

| Claim | Status |
|---|---|
| Single-site conditional as a softmax over $q$ scores; $Z$ cancels | [Exact] for any Potts model |
| Population pseudolikelihood minimized by matching true conditionals | [Exact] if the family contains them |
| Positive single-site conditionals determine the joint | [Exact] on a finite configuration space |
| $J_{ij}(a,b) = A_{ij}U_{ab}$ for the factored score | [Exact] within the stated family |
| Symmetric $A$ with zero diagonal and symmetric $U$ gives a common joint model | [Exact]; sufficient, not necessary |
| Zero-sum gauge leaves the distribution unchanged | [Exact.] |
| A $2\times2$ pair coupling can be pure gauge | [Exact], by the exercise |
| Positional–semantic transition in the solvable model | [Stated — refs]; tied low-rank matrices, specified data, proportional limit |
| The Landau form | [Heuristic]; offered for orientation and explicitly not derived for that model |

---

## What the week establishes

1. A conditional question costs $q$ terms to normalize whatever the size of
   the configuration space, which is why the inverse problem is tractable at
   all.
2. Pseudolikelihood is a criterion whose population minimizer matches the true
   conditionals, and is not a factorization of the joint.
3. A separable attention reproduces a separable Potts conditional exactly, with
   stated symmetry conditions for a common joint model — and does not reach
   content-dependent self-attention.
4. The couplings carry a gauge freedom that can be fixed explicitly, and a
   recovery claim means nothing until it is.

**What to carry forward.** This is the one week where a claim about what a
network learned can be checked against a known answer, and the checking
procedure is the transferable part: verify the truth lies in the fitted
family, fix the gauge, vary sample size and regularization separately, and
compare effective quantities rather than factors. Week 13 measures a model
where no known answer exists, and the contrast is the point.

## The practical session — Laboratory 6

**Varied:** the sample size, and — separately, never together — the
regularization strength.
**Held fixed:** the generating Potts model and its couplings, chosen by hand;
the gauge convention, fixed on both the true and the inferred tensors; and the
held-out set used to evaluate conditional loss.
**Measured:** held-out conditional loss; and the effective coupling tensor
$A_{ij}U_{ab}$ against the true couplings after the common gauge choice.

**Product:** a recovery map over sample size and coupling strength with the
gauge convention stated; the held-out conditional loss alongside it; and an
explicit account of which failures are model limitations and which are
optimization failures.

Generate independent configurations, or account for Monte Carlo
autocorrelation. Check first that the data-generating couplings belong to the
fitted family.

---

## Connections to other parts of the wiki

- [[week-01-inferring-a-distribution|Week 1]] supplies the cross-entropy
  decomposition applied here to conditionals.
- [[week-11-particles-on-a-sphere|Week 11]] measured a trained model against an
  idealization; this week measures a fit against a known answer.
- [[week-03-perceptron-and-cover|Week 3]] supplies the standard against which
  §5 reads a transition claim, and Week 13 applies it.
- [[week-13-scaling-and-the-standard|Week 13]] takes the same discipline into
  a setting where no known answer is available.
- nn-llm-unit-3 — the block skeleton this note implements.

---

[[nn-llm-start-here|Start here]] · [[nn-llm-week-map|All weeks]] · [[nn-llm-resources|Book and experiments]] · [[week-11-particles-on-a-sphere|Previous week]] · [[week-13-scaling-and-the-standard|Next week]]
