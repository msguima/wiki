---
title: "Week 4 — Gardner's capacity calculation"
type: lecture-notes
course: nn-llm-syllabus
semester: 1
week: 4
unit: 1
duration: "4 hours (2 hr lecture + 2 hr guided calculation)"
status: draft
modified: 2026-09-19
---

# Week 4 — Gardner's Capacity Calculation

*Notes for [[nn-llm-syllabus|the neural-networks course]], Unit 1. Written by an AI assistant under the researcher's supervision; see ai-authorship.*

*Week 3 answered the feasibility question exactly, at zero margin, by
counting regions. Demand a margin and the counting stops working, and the
question becomes one of measuring a volume in a high-dimensional space with
quenched disorder — which is the problem the replica method was invented for.
This is the week where the course's subject and the student's training
coincide most completely, and also the week where the course is most careful
about what a method establishes.*

---

## Learning goals

1. Say why the quenched average $\overline{\log V}$ is the object of interest
   and not $\log\overline V$.
2. **Follow** the replica calculation from integer moments to the
   replica-symmetric saddle, naming which step is exact and which is an
   assumption.
3. **Derive** the capacity formula and recover $\alpha_c(0) = 2$ as an
   independent check.
4. State what the linearized regime and the interpolation peak add to the two
   questions Cover and Gardner leave open.

## Reading

**Primary text.** Chapter 2, §2.4 for the calculation, and §2.5 for the
supplement of §5 below. §2.5 has no lecture hours in the current syllabus
document and is optional independent study.

**Primary literature**, through [[nn-llm-bibliography|the bibliography]]:
Gardner (1988) and Gardner and Derrida (1988); Engel and Van den Broeck (2001)
for the full treatment; Mézard, Parisi and Virasoro (1987) for the replica
method itself. For §5: Jacot, Gabriel and Hongler; Chizat, Oyallon and Bach;
Belkin and collaborators; Hastie and collaborators. The bibliography now links the six previously pending arXiv records, checked
on 2026-09-19.

**Prerequisites.** [[week-03-perceptron-and-cover|Week 3]]. Saddle-point
evaluation of an integral with an extensive exponent. Gaussian integrals.

## The problem and the reading route

Keep the spherical weight vector and normalized fields of
[[week-03-perceptron-and-cover|Week 3]]:
$\boldsymbol w^2=N$ and $u_\mu=\sigma^\mu\boldsymbol w\cdot
\boldsymbol\xi^\mu/\sqrt N$. The patterns have independent standard Gaussian
components and independent random signs. We ask for the largest load
$\alpha=P/N$ admitting $u_\mu\ge\kappa$ for all patterns, with **$\kappa\ge0$**.

Follow the volume, its replicated moment, the overlap matrix and finally the
$q\to1$ boundary. The replica-symmetric calculation is displayed below;
its continuation and symmetry ansatz are assumptions, not a proof of the
capacity theorem. The optional generalization supplement at the end has no
allocated lecture hours in the current syllabus.

## 1. Why the logarithm is averaged, and not the volume

The volume $V$ of admissible weights depends on the patterns, which are drawn
once and held. On the typical satisfiable branch, $V$ scales exponentially with $N$,
so $\log V \sim Ns$ defines an entropy density of solutions. The usual
quenched calculation aims to characterize that typical logarithm. A
regularization is needed before identifying it with a finite-$N$ average.

Averaging $V$ first would give something else. A few unusually favourable
pattern sets can dominate $\overline V$ while contributing nothing to what a
typical sample looks like, so $\log\overline V$ is not the typical entropy. For a positive
regularized volume, Jensen's inequality gives
$\overline{\log V}\le\log\overline V$; a capacity conclusion needs
additional analysis.

The state is a weight vector, the disorder is the fixed set of patterns, and
the constraints remove regions of the sphere. This is the familiar
quenched-disorder setup. Whether an entropy concentrates around a typical
value is a property to establish for this ensemble, not a consequence of
calling it a free energy.

## 2. The replica identity, and one subtlety before it

For a positive random variable $W$ with sufficient integrability, expand $W^n = e^{n\log W} = 1 + n\log W + \mathcal O(n^2)$,
average term by term, and differentiate at $n = 0$. The attraction is on the
right-hand side — an average of a logarithm, which we cannot compute, has
been traded for a moment, which we can.

In symbols,

$$
\overline{\log W}=\left.\partial_n\overline{W^n}\right|_{n=0}.
$$

For instance, $W_\epsilon=V+\epsilon$ with $\epsilon>0$ makes this identity
well-defined at finite $N$. Applying the replica method to a hard feasible
volume needs further care. When the ensemble permits infeasible finite-$N$ samples, those samples have
$V=0$ and $\log V=-\infty$. For example, this occurs with sufficiently
many random zero-margin constraints; it does not occur for every $P,N,\kappa$. An unregularized finite-$N$
average of the logarithm is therefore not a finite typical entropy, and a positive regularizer can be introduced, with the physics calculation
extracting a typical satisfiable branch through large-$N$, small-regularizer
and $n \to 0$ limits taken in an order that is itself part of the method.

> **Physical picture.** Note what kind of object the "number of replicas" is.
> For integer $n$, $\overline{V^n}$ is the honest partition function of $n$
> copies of the weight vector exposed to the *same* patterns, and the coupling
> between copies is induced entirely by that shared disorder. Everything up to
> this point is a calculation about a real system of $n$ interacting copies.
> What is not a calculation about any system is the continuation of that
> answer to $n \to 0$, and the discipline of the week is to keep the two kinds
> of statement apart.

## 3. Overlaps, the saddle, and the symmetry ansatz

For positive integer $n$ the moment factorizes over patterns, because
different patterns are independent. For one pattern the $n$ fields are jointly
Gaussian with covariance $q_{ab} = \boldsymbol w^a\cdot\boldsymbol w^b/N$, so **all** the
dependence on the weights enters through the Gram matrix of the replicas. That
matrix is the order parameter.

Inserting a delta function for each pair and integrating out the weights at
fixed Gram matrix gives a density proportional to $(\det Q)^{(N-n-1)/2}$, and
the moment becomes an integral over $Q$ with an extensive exponent:

$$
\overline{V^n} \asymp \int \mathrm d Q\, \exp N\Big[\tfrac12\log\det Q + \alpha\log\Phi_n(Q)\Big].
$$

The two terms have a direct meaning and the lecture should stop on them: the
first is the geometric multiplicity of weight configurations with prescribed
mutual angles, the second the probability that such a configuration meets the
constraints. The factor $N$ permits a saddle-point evaluation.

The **replica-symmetric ansatz** sets $q_{ab} = q$ off the diagonal. It is an
assumption about where the saddle sits, not a consequence of the permutation
symmetry of the problem, and must be checked separately from that symmetry.

For one pattern the replica fields have covariance $Q$. Their simultaneous
constraint probability is
$\Phi_n(Q)=\mathbb E_Q\prod_{a=1}^n\Theta(u_a-\kappa)$.
On the replica-symmetric branch, write

$$
Q=(1-q)I+q\boldsymbol1\boldsymbol1^{\mathsf T},\qquad
 u_a=\sqrt q\,z+\sqrt{1-q}\,z_a,
$$

where $z,z_a$ are independent standard Gaussians and this representation
uses $0\le q<1$. The eigenvalues of $Q$ are $1-q$, with multiplicity
$n-1$, and $1+(n-1)q$, with multiplicity one. Consequently

$$
\log\det Q=(n-1)\log(1-q)+\log(1-q+nq)
 =n\left[\log(1-q)+\frac{q}{1-q}\right]+O(n^2).
$$

Define $Dz=e^{-z^2/2}dz/\sqrt{2\pi}$ and
$H(v)=\int_v^\infty Dz$, the Gaussian tail. **Here $H$ is not the entropy
of Week 1.** Conditioning on the shared Gaussian $z$ gives

$$
\Phi_n(q)=\int Dz\,H\!\left(\frac{\kappa-\sqrt q\,z}{\sqrt{1-q}}\right)^n.
$$

After the formal continuation to $n\to0$, the coefficient of $n$ in the
exponent has the two pieces

$$
G_S(q)=\frac12\left[\log(1-q)+\frac{q}{1-q}\right],\qquad
G_E(q)=\int Dz\log H\!\left(\frac{\kappa-\sqrt q\,z}{\sqrt{1-q}}\right).
$$

The replica-symmetric entropy is obtained from the stationary value of
$G_S+\alpha G_E$, with the appropriate branch and limit prescription.
The notation $\asymp$ above retained only the leading exponential order;
normalization factors independent of $Q$ do not affect the saddle.

Increasing overlap makes several replicas more likely to satisfy **the same
pattern together**. Different patterns remain independent. This is the
competition with the geometric cost encoded by $\log\det Q$; satisfying one
pattern does not make a new independent pattern easier.

## 4. The capacity boundary

On the replica-symmetric branch, feasibility ends as $q \to 1$: the mutual angular separation of typical solutions tends to zero on this
branch. This overlap statement alone is not a finite-$N$ uniqueness proof. Writing $\varepsilon = 1 - q$, use $\log H(v)=-v^2/2+O(\log v)$ as $v\to+\infty$.
The region $z<\kappa$ supplies the divergent part of $G_E$:

$$
G_E=-\frac{1}{2\varepsilon}\int_{-\infty}^{\kappa}Dz\,(\kappa-z)^2
 +O(|\log\varepsilon|),\qquad
 G_S=\frac{1}{2\varepsilon}+O(|\log\varepsilon|).
$$

Set $t=-z$ to obtain $A(\kappa)$ below. The sum becomes

$$
G_S + \alpha G_E = \frac{1 - \alpha A(\kappa)}{2\varepsilon} + \mathcal O(|\log\varepsilon|),
$$

with the geometric term supplying the $1$ and the constraints the $-\alpha A$.
Stationarity in $q$ turns that into a second-order pole whose vanishing as
$\varepsilon \to 0$ requires the residue to vanish, and the capacity follows:

$$
\frac{1}{\alpha_c(\kappa)} = A(\kappa) = \int_{-\kappa}^{\infty} Dt\,(t+\kappa)^2.
$$

At $\kappa = 0$ Gaussian symmetry gives $A = 1/2$ and $\alpha_c = 2$ — the
number Week 3 obtained by counting regions, with no replicas and no
continuation. That agreement is the week's most important single fact, and it
is a *check on a method*, not a justification of the operations the method
used. Integration by parts gives the useful closed form

$$
A(\kappa)=(1+\kappa^2)\Phi(\kappa)+\kappa\varphi(\kappa),
$$

where $\varphi$ is the standard Gaussian density and $\Phi=1-H$ its
cumulative distribution. At $\kappa = 1$ it gives $\alpha_c \simeq 0.5196$: a larger
buffer from the boundary accommodates fewer random assignments.

> **Physical picture.** The word "replica" appears in this group's research in
> a different construction, and the two are worth holding apart deliberately.
> The [[replica-trick-gravity|gravitational replica trick]] computes Rényi
> entropies from $n$-fold replicated geometries and continues $n \to 1$ to
> reach a von Neumann entropy; this one computes moments of a volume over $n$
> replicated weight vectors and continues $n \to 0$ to reach a quenched free
> energy. Different limits, different objects replicated, different physics.
> What they share is the move that carries the risk in both cases — integer
> moments computed honestly, then continued in $n$ — and in both cases the
> continuation is an assumption rather than a theorem. A student who has met
> that fact here will recognize it in the holography course.

## 5. Optional study: fitting and generalization

Cover and Gardner ask whether suitable weights exist. A learning rule asks
which weights are reached, and generalization asks how they predict fresh
observations. The [[nn-llm-linearized-learning|linearized-learning supplement]]
derives the tangent-kernel evolution and works through a solvable noisy
linear model. It includes the distinction between the interpolation threshold
$\alpha=1$ and the random sign-feasibility threshold $\alpha=2$.
These values belong to specified ensembles; their ratio is not a universal
conversion between equality and inequality constraints.

This supplement remains independent study. It adds no meeting or assessment
requirement to the current syllabus.

## Checkpoints with answers

**1. What is shared between replicas?** The random patterns. The weight
vectors are separate integration variables, so their response to the same
pattern is correlated through their overlap.

**2. Which line first requires more than an integer number of copies?**
Extracting the derivative at $n=0$ from an expression computed for positive
integers requires a justified continuation, or here a stated replica
prescription. The integer moment by itself does not specify that continuation.

**3. Why does $\kappa=0$ recover two?**
$A(0)=\int_0^\infty Dt\,t^2=1/2$ by Gaussian symmetry and unit variance.
Thus $1/A(0)=2$, agreeing with Cover's independent counting result.

---

## Subtleties and fine print

**Which steps are exact.** The integer-moment construction, the factorization
over patterns, the Gaussian field covariance and the identification of $Q$ as
the order parameter are all exact for Gaussian patterns at integer $n$. The
continuation to $n \to 0$, the order of limits, and the replica-symmetric
ansatz are not.

**The ansatz is an assumption about the saddle.** Permutation symmetry of the
replicas does not imply a permutation-symmetric saddle. In other disordered
systems it fails, and the machinery for what replaces it is outside this
course.

**A check is not a justification.** Recovering $\alpha_c(0) = 2$ shows that the
method reproduces a known answer in one case. It does not license the same
operations for binary weights, structured patterns, or any other ensemble,
each of which requires its own analysis.

**Capacity is not memory.** The result concerns a specified family of random
patterns with random labels and a specified retrieval criterion. Week 5 asks a
different question about a different construction and gets a very different
number, and the two do not contradict each other.

**The supplement of §5 has no lecture hours.** It is optional independent study. Giving it a meeting requires revising the course's official syllabus
document, which is an open decision.

---

## Key claims and status

| Claim | Status |
|---|---|
| $\overline{\log W} = \partial_n\overline{W^n}\vert_{n=0}$ | [Exact] for positive $W$ with enough integrability |
| Factorization of $\overline{V^n}$ over patterns; $Q$ as the order parameter | [Exact] at integer $n$, Gaussian patterns |
| $\rho_N(Q)\propto(\det Q)^{(N-n-1)/2}$ | [Exact] at integer $n$ |
| Saddle-point form with extensive exponent | [Asymptotic] leading exponential order at fixed integer replica number |
| $q_{ab} = q$ off the diagonal | [Replica-symmetric] — an assumption |
| $1/\alpha_c(\kappa) = \int_{-\kappa}^{\infty}Dt\,(t+\kappa)^2$ | [Replica-symmetric] |
| $\alpha_c(0) = 2$, agreeing with Week 3 | [Exact] by Week 3's counting; here a check on the method |
| $\alpha_c(1)\simeq0.5196$ | [Replica-symmetric] |
| Tangent-kernel flow $\boldsymbol r(t) = e^{-Kt}\boldsymbol r(0)$ | [Exact] for the linearized model; [Controlled approximation] for the network, with the drift as the control |
| Risk of the minimum-norm interpolator on both sides of $\alpha=1$ | [Thermodynamic limit], isotropic Gaussian inputs; optimal ridge removes the peak |

---

## What the week establishes

1. The quenched average is the object with an extensive logarithm, and the
   replica identity reaches it from integer moments by an elementary
   expansion.
2. All dependence on the weights enters through the Gram matrix of the
   replicas, which reduces the problem to a saddle point in one order
   parameter under the symmetry ansatz.
3. The capacity formula, with $\alpha_c(0) = 2$ recovered independently and
   $\alpha_c(1) \simeq 0.5196$ as the effect of demanding a margin.
4. The distinction between feasibility, the result of a learning rule and
   prediction on fresh observations. The last two questions are developed in
   the optional supplement.

**What to carry forward.** Two things, and they pull in opposite directions.
The method is powerful enough to answer a question counting cannot reach, and
it reproduces the one answer that can be checked independently. The continuation, choice of saddle and exchanges of limits require
assumptions, which the course labels as such
and will keep labelling. Holding both at once is the skill this week exists to
build.

## The practical session — guided calculation, part II

**Varied:** the margin $\kappa$, and the replica index $n$ through the steps
where it is still an integer.
**Held fixed:** the pattern ensemble — independent standard Gaussians with
independent equally likely labels, so that the labels can be absorbed.
**Measured:** nothing numerical. The session is a derivation carried out on
paper: the determinant expansion to first order in $n$, the shared-Gaussian
representation of the correlated fields, and the $q \to 1$ balance.

**Product:** the two eigenvalues of the replica-symmetric matrix with their
multiplicities; the coefficient of $n$ in $\log\det Q$; the closed form
$A(\kappa) = (1+\kappa^2)\Phi(\kappa) + \kappa\varphi(\kappa)$ with
$\alpha_c(1)$ evaluated; and a written statement of which equalities hold at
integer $n$ and which require the continuation.

---

## Connections to other parts of the wiki

- [[week-03-perceptron-and-cover|Week 3]] supplies the independent check at
  zero margin, and the counting whose thresholds §5 contrasts with.
- [[week-05-hopfield-and-capacity|Week 5]] changes the question again: the
  couplings are held fixed and the state evolves, and the capacity that
  results has a different meaning and a different number.
- [[replica-trick-gravity|The gravitational replica trick]] shares this week's
  technical move and little else; §4 states the comparison precisely, and the
  wiki's gauge/gravity course develops that side
  ([[wiki/courses/ads-cft-course/syllabus|course syllabus]], Semester II).
- Week 13 reads claimed transitions in trained models against the standard
  Week 3 sets and §5 sharpens.
- nn-llm-unit-1 — the block skeleton this note implements.

---

[[nn-llm-start-here|Start here]] · [[nn-llm-week-map|All weeks]] · [[nn-llm-resources|Book and experiments]] · [[week-03-perceptron-and-cover|Previous week]] · [[week-05-hopfield-and-capacity|Next week]]
