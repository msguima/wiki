---
title: "Week 2 — Transfer matrix, correlation length, and what a finite text can show"
type: lecture-notes
course: nn-llm-syllabus
semester: 1
week: 2
unit: 0
duration: "4 hours (2 hr lecture + 2 hr practical)"
status: draft
modified: 2026-09-19
---

# Week 2 — Transfer Matrix, Correlation Length, and What a Finite Text Can Show

*Notes for [[nn-llm-syllabus|the neural-networks course]], Unit 0. Written by an AI assistant under the researcher's supervision; see ai-authorship.*

*Week 1 fitted a distribution to observations with the context held fixed.
Make the context a preceding token and the fitting problem becomes a Markov
chain, which a physicist reads as a transfer matrix. This is the week where
the student's existing machinery does all the work — and where the course
first insists on the difference between what a calculation establishes and
what a finite corpus can show.*

---

## Learning goals

1. **Construct** a finite-context model as a stochastic matrix on blocks, and
   read its correlation length off the subleading eigenvalue.
2. **Derive** the correlation function of the two-letter chain and identify
   the Ising transfer matrix behind it.
3. Explain why the mutual information decays with half the correlation length,
   and when that factor fails.
4. State what a power-law fit over a finite range of separations in a corpus
   does and does not establish.

## Reading

**Primary text.** Chapter 1, §1.5 through §1.7, with the worked examples and
the empirical status box in §1.6.

**Primary literature**, through [[nn-llm-bibliography|the bibliography]]: Lin
and Tegmark (2017) for the measured dependence and the hierarchical
construction; Shannon (1951) for prediction as a measurement of redundancy;
Gage (1994) and Sennrich and collaborators (2016) for the tokenization
procedures of §1.7.

**Prerequisites.** Week 1. The one-dimensional Ising transfer matrix, at the
level of a first graduate course.

## A prediction with one token of context

Use $A=+1$ and $B=-1$ again, but now let the next token depend on the current
one. A **Markov chain** specifies a probability for each next state using only
the present state. A **transition matrix** collects these probabilities.
With columns denoting the current token and rows the next token, take

$$
\mathsf T=\begin{pmatrix}1-a&a\\a&1-a\end{pmatrix},\qquad 0<a<1/2.
$$

Each column sums to one. At $a=0.2$, $p(A\mid A)=0.8$ while
$p(A\mid B)=0.2$. In the stationary state both tokens occur half the time,
so ignoring context predicts $1/2$ for each. The ideal losses are

$$
\mathcal L_{\rm no\ context}=\log2\simeq0.693147,\qquad
 \mathcal L_{\rm one\ token}=-0.8\log0.8-0.2\log0.2\simeq0.500402.
$$

The gain is $0.192745$ nats per token. A marginally balanced source can
still be predictable: context identifies the more probable continuation.
The rest of the page calculates how this local dependence propagates.

## 1. Finite context as a matrix

An **$n$-gram model** predicts using only the preceding $n-1$ tokens.
Collect those tokens into one state. For a vocabulary of size $v$, there
are $v^{n-1}$ possible states. A step drops the oldest token and appends the
new one: for a two-token context, $AB\to BA$ or $AB\to BB$. The conditional
probabilities become entries of a stochastic matrix $\mathsf T$ on these
blocks. Stationarity means $\mathsf T\pi=\pi$ for the probability column
vector $\pi$. Below, $r_k$ and $l_k^{\mathsf T}$ are right and left
eigenvectors normalized by $l_k^{\mathsf T}r_j=\delta_{kj}$.

For a finite irreducible aperiodic chain the spectrum is $1 = \lambda_1$ with
$|\lambda_k| < 1$ for $k \ge 2$, and inserting the spectral decomposition of
$\mathsf T^d$ into a stationary two-point function gives the connected
correlation as a sum of decay channels. The rank-one piece reproduces the
disconnected product exactly and cancels against it; only the decaying modes
survive.

$$
\langle f(s_0) g(s_d)\rangle - \langle f\rangle\langle g\rangle = \sum_{k\ge2}\lambda_k^{\,d}\Big(\textstyle\sum_i g(i) r_k(i)\Big)\Big(\sum_j l_k(j)\pi(j) f(j)\Big)
$$

Each eigenvalue supplies its own rate $|\lambda_k|^d$; the two bracketed
factors measure how strongly the chosen observables couple to that mode. The
chain fixes the available rates, and the observables decide which of them
appear.

> **Physical picture.** Nothing here is new to the student, and that is the
> point of the week. This is the transfer matrix of a one-dimensional chain,
> with the correlation length read off the subleading eigenvalue exactly as
> in the Ising model. What has changed is only what the states mean: blocks of
> tokens instead of spin configurations. The useful consequence is that the
> student's instincts transfer wholesale — that distinct eigenvalue moduli can give
> different decay lengths, that complex eigenvalues give
> oscillations, that a Jordan block gives a polynomial prefactor. A degeneracy can give several modes with the same decay length; it does
> not create different lengths by itself. These statements apply to text
> generated by the specified finite-state model.

## 2. The chain that can be solved completely

Two letters, a switching probability $a < 1/2$, symmetric transitions. One
step keeps the sign with probability $1-a$ and reverses it with probability
$a$, so the conditional mean of the observable is multiplied by $1-2a$ at
every step, and

$$
C(d) = \langle s_0 s_d\rangle = (1-2a)^d, \qquad \xi = -\frac{1}{\log(1-2a)}.
$$

At $a = 0.2$ this gives $C(d) = 0.6^d$ and $\xi \simeq 1.958$ token steps. The
model uses exactly one token as context, while its correlations decay
with a characteristic length of nearly two token steps. **The
memory window and the correlation length are different quantities**, and the
whole of the week's caution follows from that one observation.

The Ising identification is explicit. The zero-field one-dimensional transfer
matrix has entries $\exp(K s's)$ with columns summing to $2\cosh K$; dividing
by that number produces exactly the chain above, with
$a = e^{-K}/2\cosh K$ and $1 - 2a = \tanh K$. The eigenvalue ratio of the
Ising transfer matrix is the subleading eigenvalue of the normalized Markov
matrix.

> **Physical picture.** Take the low-temperature limit and the point lands.
> As $K\to\infty$, $\tanh K \to 1$ and $\xi \sim \tfrac12 e^{2K}$ diverges: a
> nearest-neighbour chain, with an interaction reaching exactly one lattice
> spacing, develops a correlation length of arbitrarily many spacings. Nobody
> reading that concludes the Ising model has long-range interactions. The
> identical inference about a language model — long correlations, therefore
> long-range dependence built into the architecture — is made routinely, and
> this is the calculation that refuses it.

## 3. Mutual information, and the factor of two

Assigning numbers to token types is one way to build an observable, but for a
large vocabulary it is better to measure dependence without choosing labels.
The mutual information between two stationary positions separated by $d$ does
that.

Writing the joint law as $p(a)p(b)[1 + \varepsilon_{ab}(d)]$ and expanding,
normalization cancels the linear term and the leading contribution is
quadratic in $\varepsilon$. If a single dominant mode governs the joint
distribution then $\varepsilon(d) \propto \lambda_2^{\,d}$, and therefore

$$
I(d) \sim \text{const}\,|\lambda_2|^{2d} = \text{const}\,e^{-2d/\xi}.
$$

**The generic mutual-information decay length is half the ordinary
correlation length.** For the two-letter chain, put $r=(1-2a)^d$. Its stationary joint
probabilities are $p(s_0,s_d)=(1+r s_0s_d)/4$. Substituting in
$I=\sum p(s_0,s_d)\log[p(s_0,s_d)/(p(s_0)p(s_d))]$ gives

$$
I(d)=\frac{1+r}{2}\log(1+r)+\frac{1-r}{2}\log(1-r)
 =\frac{r^2}{2}+O(r^4).
$$

At $a=0.2,d=1$, $r=0.6$ and $I(1)=0.192745$, precisely the predictive
gain calculated above. At large $d$, $r$ is small, so the leading term decays
as $0.6^{2d}/2$. The expansion, unlike the preceding expression, is
asymptotic.

> **Physical picture.** The factor of two is not a convention. A correlation
> function is linear in the perturbation of the joint law away from the
> product, while mutual information is a relative entropy and therefore
> quadratic in it — the same reason a free-energy difference is quadratic in
> an order parameter that vanishes linearly. Anyone who reads a decay length
> off an $I(d)$ plot and compares it with a $\xi$ obtained from a correlation
> function is out by a factor of two before any data enters.

## 4. What a corpus can show

Lin and Tegmark report approximately algebraic dependence over finite ranges
of separation in several text corpora, and construct hierarchical generative
models in which recursive expansion produces behaviour of that kind. Those
models supply a mechanism for correlations over many scales.

The book's status box gives three separate reasons the measurement does not
establish an asymptotic law for a thing called language, and they are worth
keeping distinct.

1. **A corpus is an assembly of sources.** Mixing texts whose statistics
   differ can create apparent long-range dependence that no single source
   possesses.
2. **The plug-in estimate of $I(d)$ is biased upward.** Empirical frequencies
   fluctuate away from the product of the marginals even for independent
   variables, and the bias grows with the size of the vocabulary.
3. **A finite mixing chain has an exponential envelope asymptotically while
   tracking a much slower decay across any finite window.** The range actually
   observed leaves the asymptotics open.

> **Physical picture.** The third reason is the one a physicist should feel
> most sharply, because it is the finite-size problem in its usual form. Near
> a critical point a finite system shows power-law behaviour over the range of
> scales its size permits and crosses over beyond it; here the crossover scale
> is $\xi$ and the observation window is whatever the corpus supports. Reading
> criticality off a straight line on a log–log plot is the same error in both
> settings, and the remedy is the same: vary the system size, or in this case
> the corpus and the estimator, and see whether the slope moves.

## 5. The entropy rate and the unit of description

For a stationary finite-alphabet source define
$h_k=H(X_{k+1}\mid X_1,\ldots,X_k)$ and $h_0=H(X_1)$.
Conditioning and stationarity imply $h_{k+1}\le h_k$, while $h_k\ge0$.
Thus $h=\lim_k h_k$ exists and is the **entropy rate**. The chain rule gives

$$
\frac1T H(X_1,\ldots,X_T)=\frac1T\sum_{k=0}^{T-1}h_k\longrightarrow h.
$$

For our Markov chain, $h_k=h_1$ for all $k\ge1$, even though correlations
persist for arbitrarily large finite separations.

Shannon measured the redundancy of printed English by asking subjects to guess
successive characters. The value of the experiment is that redundancy is
measured *through prediction*, with source, alphabet and protocol stated — a
methodological point the course reuses in Week 13.

Tokenization changes the unit. A per-token number is not comparable across
tokenizers, and the conversion to a common unit requires the same underlying
text, the same boundary conventions and the same probability conventions.
Where several token sequences decode to the same text, the probability of one
chosen sequence is not the probability of the text.

A common unit makes comparisons interpretable. If a model assigns probability
$p$ to a specified text of $C$ characters, its loss per character is
$-\log p/C$. Changing the division into tokens changes the per-token number.
The per-character unit removes that unit mismatch, but it does not force
different fitted models to assign the same probability. It is a common unit,
not an invariant prediction across models.

## Checkpoints with answers

**1. What is $p(A_{t+2}\mid A_t)$ at $a=0.2$?** Either no switch or two
switches returns to $A$, so it is $0.8^2+0.2^2=0.68$. The mean sign is
$2(0.68)-1=0.36=C(2)$.

**2. Why can a one-token model have a long correlation length?** A local
influence is passed from token to token. As $a\to0^+$ the influence is
attenuated very slowly, although the transition rule still uses one token.

**3. Why does mutual information decay twice as fast in the weak-dependence
limit?** Its first-order term vanishes by normalization. The leading term is
quadratic in the departure of the joint law from a product.

---

## Subtleties and fine print

**Memory window and correlation length are independent.** The two-letter chain
has a one-token memory and $\xi \simeq 2$. The limit $a \to 0^+$ makes $\xi$
diverge while the memory window stays at one token, and what fails at $a=0$ is
irreducibility, not the memory.

**The factor of two has exceptions.** It assumes one dominant nonzero mode in
the joint distribution. An observable with zero overlap onto the leading mode can have a different
correlation length. Several modes, Jordan factors and finite-range transients
require examining the expansion directly. Degeneracy alone does not force the
factor of two to fail.

**Estimator bias is not a detail.** The upward bias of plug-in mutual
information grows with vocabulary size, which is exactly the regime of text.
Uncertainty should be estimated, or independent samples compared, before any
slope is fitted.

**A general transfer matrix is not symmetric.** The two-letter chain is easy
because its column sums are equal. A general block transition matrix need not
be symmetric, reversible or diagonalizable, and its normalization requires the
dominant eigenvector as well as the eigenvalue.

**Nothing here forbids long-range dependence in language.** The calculations
show that the evidence usually offered does not establish it. That is a
statement about the evidence, and the distinction matters for how the
laboratory result should be written up.

---

## Key claims and status

| Claim | Status |
|---|---|
| $C(d) = (1-2a)^d$ and $\xi = -1/\log(1-2a)$ for the two-letter chain | [Exact.] |
| $1-2a = \tanh K$: the chain is the normalized Ising transfer matrix | [Exact.] |
| Spectral form of the connected correlation function | [Exact] for a diagonalizable finite chain |
| $I(d) \sim \text{const}\,e^{-2d/\xi}$ | [Asymptotic] under the weak-dependence and dominant-mode assumptions |
| Exact $I(d)$ of the two-letter chain, beginning at $r^2/2$ | [Exact.] |
| A finite mixing chain has an exponential envelope asymptotically | [Exact.] |
| Approximately algebraic $I(d)$ over a measured range in corpora | [Empirical]; range and corpora as reported |
| Entropy rate as the limit of $h_k$ and of the block entropy per token | [Exact] under stationarity |

---

## What the week establishes

1. A closed-form correlation function and correlation length for a chain the
   student can diagonalize by hand, together with its exact identification
   with the Ising transfer matrix.
2. A closed-form mutual information for the same chain, and with it the factor
   of two between the two decay lengths, obtained without fitting a curve.
3. The spectral decomposition of a stationary correlation function into
   independent decay channels, with the roles of the chain and of the
   observables separated.
4. Three named and independent reasons why a finite-range fit in a corpus does
   not settle an asymptotic question.

**What to carry forward.** A one-step memory produces correlations over many
steps, so whatever long correlations in text establish, it is not that the
mechanism producing them is long-ranged. Two decay lengths measured from the
same chain differ by a factor of two for a structural reason — one observable
is linear in a perturbation, the other quadratic. And the honest form of a
measurement here names the window it covers, which is the discipline Week 13
will ask for again with model size in place of separation.

## The practical session — Laboratory 1

**Varied:** the switching probability $a$; the corpus, between a supplied text
sample, a shuffled version preserving token counts, and text generated by a
fitted finite-context model; and the separation $d$.
**Held fixed:** the held-out positions, the tokenizer and the boundary
convention, identical across every model scored.
**Measured:** the exact $C(d)$ and $I(d)$ of the chain against finite-sample
estimates of the same quantities; and, for the corpora, $I(d)$ with an
uncertainty estimate.

**Product:** an explanation of what the comparisons support, including a
statement of where estimation noise obscures the predicted tail. If estimation noise prevents resolution of the tail, report that limit
and the uncertainty supporting it. The protocol does not prescribe the outcome.

---

## Connections to other parts of the wiki

- [[week-01-inferring-a-distribution|Week 1]] supplies the loss and the
  mutual information used here; this week supplies the first source with a
  computable correlation structure.
- The same transfer-matrix machinery opens the wiki's generalized-symmetries
  course, where a rotor chain is diagonalized by character expansion
  ([[wiki/courses/generalized-symmetries-course/syllabus|course syllabus]],
  Semester I Week 1).
  A student who has taken either course recognizes the other's Week 1
  immediately.
- [[kramers-wannier-duality]] is the transformation that acts on the same
  one-dimensional Ising transfer matrix from the other side; the present
  course does not use it, and the link is offered as the natural continuation
  for a student who wants one.
- Week 13 reuses this week's discipline about windows and estimators, with
  model size in place of separation.
- nn-llm-unit-0 — the block skeleton this note implements.

---

[[nn-llm-start-here|Start here]] · [[nn-llm-week-map|All weeks]] · [[nn-llm-resources|Book and experiments]] · [[week-01-inferring-a-distribution|Previous week]] · [[week-03-perceptron-and-cover|Next week]]
