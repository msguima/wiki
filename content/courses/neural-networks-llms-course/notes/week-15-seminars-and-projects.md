---
title: "Week 15 — Project seminars, and what the course established"
type: lecture-notes
course: nn-llm-syllabus
semester: 1
week: 15
unit: 5
duration: "4 hours of seminars"
status: draft
modified: 2026-09-19
---

# Week 15 — Project Seminars, and What the Course Established

*Notes for [[nn-llm-syllabus|the neural-networks course]], Unit 5. Written by an AI assistant under the researcher's supervision; see ai-authorship.*

*The last week has no lecture and no chapter behind it. Four hours of
twenty-minute seminars with questions, in the format of a conference
communication, and with them the end of the course. This note exists to do two
things the other fourteen could not: state what is being assessed and why, and
set out in one place the exact results the course established, which is the
inventory a student should leave holding.*

---

## Learning goals

1. Present a small original result in twenty minutes, in a form that survives
   questioning.
2. Judge a project of your own against the standard the course has used all
   semester: a stated model, a stated control parameter, a protocol fixed
   before the measurement, and an admissible negative result.
3. Say, for any claim met in the literature, what its control parameter is,
   what limit it takes, and which of its claims survive outside that limit.

## Reading

**No chapter.** The seminar paper comes from
[[nn-llm-bibliography|the course bibliography]], and the project follows one
of the topics in the syllabus or one agreed with the instructor.

**Worth rereading before the presentations:**
[[week-13-scaling-and-the-standard|Week 13]], for the four ingredients a
transition claim requires, and [[week-03-perceptron-and-cover|Week 3]], for
the case where they are all met.

## A final calculation to explain in your own words

Return to [[nn-llm-start-here]] and reproduce the $AB$ prediction from the
embedding vectors. Explain why attention is normalized over positions and
why the final probabilities are normalized over token labels. Identify the
parameters that could be trained and the quantities that change during
generation. This is a self-check of the course's main objective, not an
additional graded assignment.

**Checkpoint 1.** What changes if the observed target is $A$ instead of $B$?
The forward prediction stays $(0.207588,0.792412)$ because the context and
parameters are unchanged. The loss becomes $-\log0.207588\simeq1.572198$
nats instead of $0.232674$, and the score gradient becomes
$(p_A-1,p_B)$ instead of $(p_A,p_B-1)$.

**Checkpoint 2.** Which physical calculation explains the form of attention?
The fixed-memory log-sum-exp energy gives a weighted memory average and a
full-step descent proof. A general decoder uses separate keys and values,
changing states and additional sublayers, so that proof does not automatically
extend to the whole model.

**Checkpoint 3.** What knowledge is needed to reverse Gaussian corruption?
The marginal score of the noisy data. The population noise predictor provides
it as $s_k=-\epsilon_*/\sqrt{1-\bar\alpha_k}$, not as an unscaled equality.

## 1. The shape of the week

Four hours, entirely seminars. Twenty minutes with questions, in the format of
a conference communication. Two components are assessed here, and they are
different exercises.

**The paper seminar (20%).** One paper from the course bibliography, presented
and defended. The useful question to organize a seminar around is the one the
course has been asking all term: what does this paper's central claim require,
and does the paper supply it?

**The final project (40%).** A report in paper format, plus the presentation.
The syllabus is explicit about two things. The project has two admissible
modalities — reproduce a figure from one of the bibliography's papers, or
measure an observable in a small pretrained model — and **a literature review
is not accepted as a project**. The topics are sized for three to four weeks of
work in pairs.

Four of the syllabus's topics are reproductions with a known target: the
generalization-error figure for factored attention, the positional–semantic
transition on a histogram task, an exponential-capacity curve for a chosen
pattern ensemble, and an attention-entropy collapse with a stabilization test.
Four are open, with no guaranteed result: the auxiliary chain of a fixed
attention matrix, a recovery phase diagram for *correlated* memories taken
from a trained model's own representations, an operational definition of an
attention concentration scale tracked through depth, and information
persistence in a small recurrent architecture.

> **Physical picture.** The split between the two halves is the split between
> a measurement whose answer is known and one whose answer is not, and both
> are worth doing for different reasons. A reproduction teaches what it costs
> to make a published number appear — which conventions were unstated, which
> parameters mattered, how much scatter there is — and a student who has done
> one reads figures differently afterwards. An open topic teaches the harder
> thing, which is to define an observable before measuring it and then report
> what came out. The course's standing position is that a careful negative
> result is a complete answer, and Week 15 is where that position is either
> honoured or quietly abandoned.

## 2. The seminar the syllabus singles out

One topic was moved deliberately out of the lectures and into this week: the
renormalization group and deep learning, together with physical realizations
in analogue circuits, nonlinear optics and cavity QED. The syllabus gives the
reason and does not disguise it — the analogy with the renormalization group
is **the most seductive and the loosest** on the list, and a seminar defended
by a pair in front of the class, after the week in which scepticism was
discussed, serves it better than two hours of exposition.

A deep network composes maps, usually with different parameters at each layer.
Those maps need not discard variables or produce progressively coarser
representations. A proposed relation to the renormalization group must specify
what is eliminated, what is rescaled and which observables are preserved.
Only then can fixed points and relevant directions be compared. The layer
index alone does not supply this structure.

## 3. What the course established

The inventory, by unit, with the status each result carries. The table distinguishes calculations performed on the pages from results
quoted under an ansatz or a limit. The source pages give the assumptions.

| Result | Where | Status |
|---|---|---|
| Mean matching; curvature equals the variance | Wk 1 | [Exact] |
| Expected loss $=$ conditional entropy $+$ sum of relative entropies | Wk 1 | [Exact] |
| Gibbs algebra of a softmax layer at unit inverse temperature | Wk 1 | [Exact]; no bath, no limit, no temperature |
| $C(d) = (1-2a)^d$, $\xi = -1/\log(1-2a)$; the Ising identification | Wk 2 | [Exact] |
| Mutual information decays with half the correlation length | Wk 2 | [Asymptotic] in the stated weak-dependence regime |
| $C(P,N) = 2\sum_{k<N}\binom{P-1}{k}$; threshold $\alpha_c = 2$ | Wk 3 | [Exact] at finite $N$; [Thermodynamic limit] for the threshold |
| Gardner's capacity formula; $\alpha_c(1)\simeq0.5196$ | Wk 4 | [Replica-symmetric] |
| Risk of the minimum-norm interpolator; $\alpha_*=1-\sigma/\lVert\boldsymbol w_*\rVert$ | Wk 4, optional supplement | [Thermodynamic limit]; interior optimum requires $0<\sigma<\lVert\boldsymbol w_*\rVert$ |
| Hopfield energy falls at every actual flip | Wk 5 | [Exact], four hypotheses |
| $\alpha_c^{\rm RS}\simeq0.138$, overlap $\simeq0.97$ at the branch end | Wk 5 | [Replica-symmetric] |
| Descent by at least half the squared step for the memory update | Wk 6 | [Exact], every $\beta$, memories fixed |
| Gradient field iff $M^{\mathsf T}DX = X^{\mathsf T}DM$ everywhere | Wk 6 | [Exact] |
| Permutation equivariance of an unmasked layer; the rotation identity | Wk 7 | [Exact] |
| A decoder evaluated by hand to $p(B\mid AB)\simeq0.792412$ | Wk 8 | [Computed] inline |
| Euler bound; contraction $\beta^i$; descent at fixed current input | Wk 9 | [Controlled], [Exact], [Exact] |
| Diffusion approximation matching two moments of one update | Wk 10 | [Controlled approximation] |
| Monotone potential for the spherical dynamics | Wk 11 | [Model-specific] |
| $\dot c = 1-c^2$; $R_{\rm part} = 2/(1+c^2)$ | Wk 11 | [Exact] |
| Potts conditional costs $q$ terms; factored attention reproduces it | Wk 12 | [Exact] within the stated family |
| $0\le H_i^A\le\log i$; compute-optimal allocation; $P_{\rm all}=p^m$ | Wk 13 | [Exact], [Exact given the fit], [Exact] |
| Gaussian forward conditional; marginal score is rescaled optimal predicted noise | Wk 14 | [Exact] |
| Reverse-drift formula | Wk 14 | [Exact] theorem, stated hypotheses |
| Finite-state work identity | Wk 14 | [Model-specific] |

The small systems make the mechanisms visible: a fit to two outcomes, recall
of four spins, attention between two tokens and alignment of two particles.
Larger-model claims need their own evidence and hypotheses; reproducing a
small example calibrates a calculation without proving those claims.

---

## Subtleties and fine print

**A reproduction that fails is a result, and must be reported as one.** The
likely causes — an unstated convention, a parameter the paper did not report,
scatter larger than the effect — are findings about the literature, and
suppressing them to produce a matching figure is the one outcome the course
does not accept.

**Twenty minutes is a constraint on the claim, not only on the slides.** A
result that needs forty minutes to state its assumptions is a result whose
assumptions have not been sorted.

**The status label belongs in the talk.** A presentation that states a number
without saying whether it is exact, asymptotic, or measured has skipped the
step the whole course was about.

**The laboratories are protocols, not implementations.** Anyone building on
them should expect to size the computation and discover the gaps; that work
is legitimate project content and should be reported rather than hidden.

---

## What the week establishes

Nothing new, and that is the point. The week is where the student states
something in their own voice and defends it, and the table of §3 is what they
have to stand on.

**What to carry forward.** Explain how an LLM turns text into conditional
probabilities, calculate a small prediction and its training signal, and use
physical models to understand selected mechanisms with their assumptions in
view. These foundations also let you read research critically and design a
small measurement or calculation of your own.

## The session

**Varied:** nothing. This is the one week with no controls to set.
**Held fixed:** twenty minutes, questions afterwards, conference format.
**Measured:** by the instructor — whether the claim presented is stated with
its scope, whether the protocol was fixed before the measurement, and whether
a negative result, if one occurred, is reported as a result.

**Product:** the report in paper format, and the presentation.

---

## Connections to other parts of the wiki

- The master's project runs alongside the course for
  a student who wants a longer piece of work; its three candidate framings
  share the shape the projects here are judged by.
- [[week-13-scaling-and-the-standard|Week 13]] supplies the standard applied
  in §1, and [[week-03-perceptron-and-cover|Week 3]] the case that meets it.
- [[week-01-inferring-a-distribution|Week 1]] is where the first entry of the
  table of §3 was derived, and rereading it after fourteen weeks is a better
  use of an hour than it sounds.
- [[nn-llm-syllabus]] — the course, its assessment and its outcomes.
- ai-authorship — who wrote these pages, and what the supervision
  certifies.

---

[[nn-llm-start-here|Start here]] · [[nn-llm-week-map|All weeks]] · [[nn-llm-resources|Book and experiments]] · [[week-14-diffusion-and-thermodynamics|Previous week]]
