---
title: "Statistical Physics of Neural Networks and Language Models"
type: course
instructor: Marcelo S. Guimarães
institution: UERJ — Departamento de Física Teórica
duration: one semester (15 weeks, 60 hours)
audience: M.Sc. and Ph.D. students; open to final-year undergraduates
prerequisites: Statistical mechanics (ensembles, partition functions, transfer matrices); mathematical methods (linear algebra, Gaussian integrals, saddle point)
not assumed: neural networks, machine learning, Python, or any programming background
language: lectures in Portuguese; written materials in English
modified: 2026-09-19
---

# Statistical Physics of Neural Networks and Language Models

*Written by AI assistants under the scientific and pedagogical supervision of Marcelo S. Guimarães; see ai-authorship for the division of labour and the models involved.*

A one-semester topics course that uses a physicist's training in statistical
mechanics as the way into neural networks and language models. The student
arrives knowing ensembles, partition functions and collective phenomena, and
very possibly knowing nothing about tokens, gradients or attention. The aim is to understand the concepts that support an LLM architecture:
how text becomes vectors, how attention combines them, how a decoder predicts
probabilities and how training adjusts its parameters. Physical models provide
mechanisms and calculable examples along that route; computing terminology is
defined where it is needed.

**Begin with [[nn-llm-start-here|one complete small prediction]].** Then use
[[nn-llm-week-map]] for the semester sequence. [[nn-llm-resources]] opens the
companion PDF, the five browser experiments and the related wiki courses;
[[nn-llm-glossary]] is an optional lookup page.

The inheritance is real and not decorative. Hopfield's model predates the
field of deep learning; Gardner's capacity calculation is a replica
calculation; diffusion generative models were constructed explicitly from
non-equilibrium thermodynamics; and a memory update with keys equal to values
has the mathematical form of attention and admits a log-sum-exp energy. A
physics student can therefore reach the attention rule *from the inside*, by
deriving it, instead of accepting it as a definition.

---

## 1. Course architecture

| | Single semester — 15 weeks |
|---|---|
| **Format** | Lectures + practical sessions, in the same weekly block |
| **Hours/week** | 2 hr lectures + 2 hr practical (guided calculation or laboratory) |
| **Total** | 28 hr lectures + 28 hr practical + 4 hr project seminars = 60 hr |
| **Mode** | Instructor-led, with a student-led final week |
| **Anchor** | Inference on a two-state system → perceptron capacity → associative memory → attention → the full decoder → observables of trained models → diffusion |

The wiki and the printable notes provide two ways to study the same course.
Weekly pages contain definitions, essential derivations, worked examples and
answered checkpoints. The book offers longer treatments and exercise sets.
Neither programming nor constant switching between the two formats is a
prerequisite for understanding the main wiki argument. See §10.

---

## 2. Learning outcomes

By the end of the course a student should be able to:

1. Define tokens, context and conditional probabilities, derive the training
   loss from likelihood, and distinguish finite-sample loss from expected loss.
2. Calculate the output and gradient of a neuron, and explain backpropagation
   as the chain rule through intermediate representations.
3. Follow a supplied sequence through embeddings, position information,
   attention, residual sums, normalization, a feed-forward map and the
   vocabulary readout; compute a small example by hand.
4. Explain the difference between processing a layer, repeating an internal
   update, generating a token and changing parameters during training.
5. Reproduce Cover's count and follow Gardner's calculation, stating the
   replica continuation, symmetry ansatz and zero-margin check.
6. Explain Hopfield recall, its success criterion, and the fixed-memory energy
   construction whose update has the form of attention.
7. Define and measure observables of a trained model, and derive the central
   noise-to-score relation of a diffusion model using a Gaussian example.
8. Use these foundations to assess research claims and carry out a small
   calculation or measurement with an explicit model, protocol and scope.

---

## 3. Audience and prerequisites

The intended student has a graduate physicist's statistical mechanics and
mathematical methods, and may be meeting neural networks for the first time.
**No programming background is assumed.** The computational work is an
instrument for investigating models whose equations the student already
understands, and syntax instruction is kept out of the conceptual path.

Recommended but not required: a course in critical phenomena or quantum field
theory, for familiarity with saddle points and the thermodynamic limit; and
computational physics, for comfort with numerical experiment.

Class size is limited to 8–20 by the computational infrastructure.

---

## 4. Materials

**Primary text.** *Statistical Physics of Neural Networks and Language
Models: From the transfer matrix to the attention mechanism* — the
instructor's own lecture notes, in English, supplying every derivation in
full, with worked examples, checkpoints, exercises and answers. Available through [[nn-llm-resources|the reading and experiments page]];
see ai-authorship for its authorship disclosure.

**Statistical-mechanical background.**
- Engel and Van den Broeck, *Statistical Mechanics of Learning* — the reference for the perceptron capacity calculation, and the source of the $H(v)$ notation used in Week 4.
- Mézard, Parisi and Virasoro, *Spin Glass Theory and Beyond* — replica method.
- Bahri and collaborators, *Statistical Mechanics of Deep Learning* (Annu. Rev. Condens. Matter Phys. 11, 2020) — the survey that maps the territory.

**Machine-learning background, for the vocabulary.**
- Mehta and collaborators, *A high-bias, low-variance introduction to machine learning for physicists*.
- Prince, *Understanding Deep Learning*.

**Primary literature.** Assembled week by week in
[[nn-llm-bibliography|the course bibliography and paper map]]; the syllabus
never cites an arXiv identifier from memory.

**Executable material.** Five small browser experiments accompany the text and
run without installation; open them through [[nn-llm-resources]]. The full
laboratories remain separate protocols requiring implementation and testing.

---

## 5. Assessment

| Instrument | Weight |
|---|---|
| Laboratory reports 1–8 (best 7 of 8) | 40% |
| Seminar on one paper from the bibliography | 20% |
| Final project: paper-format report plus presentation | 40% |

The laboratories pose questions and specify controls; they do not prescribe
which curve must appear. A null result, a smooth trend where a threshold was
expected, or a protocol-dependent answer is an admissible outcome, and saying
so clearly is worth more than forcing a plot.

---

## 6. The fifteen weeks

Weeks 1–14 each have one 2-hour lecture and one 2-hour practical session;
Week 15 has four hours of seminars. Weekly
notes are catalogued in [[nn-llm-week-map|the week map]]; block-level plans
live in `skeletons/`.

### Unit 0 — The object, before the analogy (Weeks 1–2)

| Week | Lecture | Practical |
|---|---|---|
| 1 | Fitting a two-state system; why a loss is minimized; text, context and conditional probabilities | Small calculation and guided experiment, no programming prerequisite |
| 2 | Transfer matrix; correlation length; mutual information and power-law claims in text | Laboratory 1 |

### Unit 1 — Networks as many-body systems (Weeks 3–6)

| Week | Lecture | Practical |
|---|---|---|
| 3 | The perceptron and the space of interactions; Cover's counting | Replica calculation, part I |
| 4 | Gardner's capacity calculation | Replica calculation, part II |
| 5 | Hopfield dynamics; Amit–Gutfreund–Sompolinsky | Laboratory 2 |
| 6 | Dense associative memory; the attention rule derived from a log-sum-exp energy | Laboratory 3 |

### Unit 2 — Building the transformer (Weeks 7–10)

| Week | Lecture | Practical |
|---|---|---|
| 7 | Representations; positional encoding; relative position as a phase difference | Inspect provided blocks and predict their effects |
| 8 | Multi-head attention, normalization, the complete block, a forward pass by hand | Laboratory 4, part I |
| 9 | Residual flow, the continuous-depth limit, recurrence with controlled inputs | Laboratory 4, part II |
| 10 | The adjoint method; the diffusion approximation to stochastic gradient descent; sampling and temperature | Laboratory 4, part III |

### Unit 3 — Physics of what emerged (Weeks 11–13)

| Week | Lecture | Practical |
|---|---|---|
| 11 | Interacting particles on a sphere; rank collapse; the Kuramoto reduction | Laboratory 5 |
| 12 | Generalized Potts and the inverse problem; the positional–semantic transition in a solvable model | Laboratory 6 |
| 13 | Attention measurements, scaling laws, grokking and transition claims | Laboratory 7 |

### Unit 4 — Diffusion and non-equilibrium thermodynamics (Week 14)

| Week | Lecture | Practical |
|---|---|---|
| 14 | Gaussian corruption, the reverse conditional, score estimation, the reverse stochastic equation; the Ornstein–Uhlenbeck example and the reach of the thermal reading | Laboratory 8 and project supervision |

### Unit 5 — Projects (Week 15)

| Week | Activity |
|---|---|
| 15 | Student project presentations and the paper seminars (4 hr) |

### Material carried outside the lecture hours

Two substantial pieces sit in the text without lecture time assigned in the
current syllabus version:

- **[[nn-llm-linearized-learning|The linearized regime and the interpolation peak]]** — the neural tangent
  kernel, and the risk of a minimum-norm interpolator on both sides of the
  interpolation threshold. This is the natural sequel to Weeks 3 and 4: it
  takes up the two questions Cover and Gardner leave open, which admissible
  solution is selected and how it predicts, on the same load parameter
  $\alpha = P/N$. It is optional independent study. Giving it lecture hours would require
  a separate revision of the official syllabus.
- **The detailed steps of the replica calculation**, which belong to the two
  guided sessions of Weeks 3 and 4 rather than to the board.

---

## 7. Laboratories

| # | Week | Subject |
|---|---|---|
| 1 | 2 | Predictions, context and correlations: analytic two-outcome model, the two-token chain, and estimation noise in a finite text sample |
| 2 | 5 | Retrieval under increasing load, with a stated overlap criterion and update schedule |
| 3 | 6 | Mixture, retrieval, and the descent test for the continuous memory update |
| 4 | 8–10 | A small decoder in three parts: predict and inspect; vary one ingredient and measure what survives; train and then sample |
| 5 | 11 | Token clustering along depth: pair overlaps, mean direction, singular-value spectrum |
| 6 | 12 | Inferring known interactions: generate from a small Potts model, fit conditionals, compare couplings in a common gauge |
| 7 | 13 | Attention observables in a pretrained decoder, separating measurement from interpretation |
| 8 | 14 | Learn a distribution, then diagnose the error: prior mismatch, score error and time discretization, kept apart |

The laboratories are specified as protocols. Implementation, hardware sizing
and teaching trials remain to be done, and this should not be presented as
settled.

---

## 8. Recurring threads across the course

Four questions return in every unit, and the course is organized so that the
student meets each of them several times in different clothing.

- **What is varied and what is held fixed?** Fitting varies parameters with
  the data fixed; Hopfield recall varies the state with the couplings fixed;
  generation varies the sampled token with the trained model fixed; a
  temperature change is a fourth, separate intervention.
- **What kind of statement is this?** Exact identity, result in a stated
  limit, replica-symmetric ansatz, controlled approximation, or empirical
  observation. The text's status boxes carry the label; the weekly notes carry
  the same discipline.
- **Where does the analogy stop?** An energy that controls a specified
  dynamics in a specified state space does not thereby supply an energy for a
  whole architecture. This is the spine of Weeks 6 and 11.
- **What would distinguish a collective phenomenon from a plotting effect?**
  A sequence of systems, a control parameter, an order parameter, and a
  measured crossover width. Week 13 uses Cover's threshold from Week 3 as the
  standard of comparison.

---

## 9. Relation to the other courses and to the group's research

**To [[wiki/courses/generalized-symmetries-course/syllabus|the generalized-symmetries course]]
(`generalized-symmetries-course`).** The strongest technical overlap. That
course opens with compact variables, transfer matrices and the
character-expansion treatment of a rotor chain; this one opens with a transfer
matrix on a two-letter alphabet and reads the correlation length off the
subleading eigenvalue. The Ising connection is made explicit in Week 2 of this
course, and a student who has taken either will recognize the machinery
immediately.

**To [[wiki/courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]] (`2026-algebraic-qft-course`).** A
conceptual rather than technical overlap, and worth stating carefully.
Relative entropy appears in both — here as the Kullback–Leibler divergence
between a source and a fitted model in Week 1, and as the exact decay of
$D(q_t\Vert\pi)$ along an Ornstein–Uhlenbeck flow in Week 14; there as the
Araki–Uhlmann relative entropy of states on a von Neumann algebra. These are
the same quantity in different settings, classical and algebraic, and the
course does not claim more than that.

**To the group's research.** The inverse Potts problem of Week 12 is the
machinery of direct-coupling analysis, which students with a background in
statistical or biological physics recognize on sight, and the gauge freedom of
its couplings is a reparametrization of exactly the kind that recurs
throughout field theory. The replica calculation of Week 4 is the disordered-
systems technique the group's older confinement work sits beside.

---

## 10. Connection to the wiki

The wiki is a self-contained conceptual route with small calculations and
answered checkpoints. The [[nn-llm-resources|printable notes]] provide longer
proofs, exercises and protocols. When the formats disagree, inspect the
argument and record the correction; the format itself does not establish
correctness.

The teaching standard implements this
relationship. [[nn-llm-conventions]] records notation and
[[nn-llm-glossary]] supports lookup. Cross-course reading is optional and
assumes the whole `physics-wiki` repository is open as the vault, as explained
in [[nn-llm-resources]]. The master's project is a
separate optional research direction.

---

## 11. Risks and contingencies

- **The laboratories are protocols, not implementations.** Sizing a trainable
  decoder to the available equipment has not been done. The contingency is the
  one the syllabus already names: supply a pretrained model so that hardware
  limits do not block the physical analysis.
- **The replica calculation is the schedule risk.** It occupies two weeks of
  lecture and two guided sessions, and it is the most likely thing to overrun.
  The reduced 44-hour variant of the course collapses it into a single guided
  session and treats the solution space qualitatively.
- **No classroom trial has been run.** The lecture route through the book has
  not been timed. Nothing in these pages should be read as a tested schedule.
- **A topics course on a moving subject dates quickly.** The architectural
  proposals discussed in Week 9 were read at a particular date, which the
  notes record. Empirical claims from elsewhere in the literature are not
  transferred to them.

---

## 12. Outcomes

A student who finishes should be able to explain the construction and training
of a decoder language model from its mathematical ingredients, without a
computer-science prerequisite. They should be able to calculate a small
prediction, identify what each architectural component contributes and use
physical intuition with the assumptions that make it reliable.

Critical reading and small research projects build on that understanding:
state the model, the control parameter, the measured range or limiting regime,
and the evidence supporting a conclusion.

The final projects are intended to be small and real: a measurement on a
trained model with a stated protocol, a calculation in a solvable model, or a
careful negative result.
