---
title: "Conventions — Statistical Physics of Neural Networks and Language Models"
type: course-standard
course: nn-llm-syllabus
modified: 2026-09-19
---

# Conventions

Binding notation for [[nn-llm-syllabus|the neural-networks course]] and every
weekly note under it. The conventions are those of the course's printed text,
and additional conventions are recorded here and defined locally on the page
that uses them. See [[nn-llm-glossary]] for terminology.

---

## 1. Logarithms and information units

Logarithms are natural. Information quantities are therefore in **nats**;
division by $\log 2$ converts to bits. Perplexity is $e^{\mathcal L}$ when loss is in nats and $2^{\mathcal L_2}$
when it is in bits. The logarithm base and exponent must agree.

## 2. Sequences, tokens and averages

- A sequence has $T$ tokens, $x_1,\dots,x_T$, with $x_t$ in a finite
  vocabulary $\mathcal V$. The prefix $x_1,\dots,x_{t-1}$ is written $x_{<t}$.
- A hat marks an empirical average over a finite sample:
  $\widehat{\mathcal L}$ is the training loss, $\mathcal L$ the expected loss.
  An expectation without a hat always has its distribution named.
- $q$ denotes the distribution the model is trying to describe — the source in
  Unit 0, the forward process in Unit 4. $p_\theta$ is always the model.

## 3. Loads and order parameters

- $\alpha = P/N$ throughout: patterns per weight in Units 1, samples per
  dimension in the interpolation-peak material. It is deliberately the same
  symbol, because it is the same ratio; Week 13 turns on the fact that two
  different thresholds live on it.
- $q_{ab}$ is the replica overlap and $q_{\mathrm{EA}}$ the Edwards–Anderson
  parameter, both in Unit 1.
- $c_{ij} = \boldsymbol x_i \cdot \boldsymbol x_j$ is the overlap between normalized token
  vectors in Unit 3. It is written $c$, not $q$, because $q$ is the number of
  Potts colors in the same unit.

## 4. Symbols that carry more than one meaning

Several symbols have different local roles. The following table records
the meanings used in the readings. Each is flagged in the text at the point of use, and a
weekly note that uses one must flag it again.

| Symbol | Meaning | Where |
|---|---|---|
| $H$ | Entropy (conditional, marginal or joint) | Units 0, 3 |
| $H(v)$ | Gaussian upper tail, $\int_v^\infty Dz$ | Unit 1, following Engel and Van den Broeck |
| $H$ | Matrix of token representations, one row per position | Unit 2 |
| $V$ | Feasible weight volume; value matrix | Units 1 and 2, respectively |
| $\alpha_k,\bar\alpha_k$ | Retained signal per step and its product, distinct from load $P/N$ | Unit 4 |
| $\beta$ | Softmax sharpness of a memory update; recurrent gain; inverse decoding temperature | Units 1, 2 |
| $\beta_{\mathrm{th}}$ | Physical inverse temperature of a bath | Unit 4 |
| $b_k$ | Noise schedule of the forward diffusion | Unit 4; the diffusion literature writes $\beta_k$ |

The decoding temperature is $\tau$, never $T$, which is reserved for the
sequence length.

## 5. Matrices and dimensions

State the shape of every object at first use. Representations are rows:
$H \in \mathbb R^{T\times d}$ has one token per row. Query, key and value
projections are $W_Q, W_K \in \mathbb R^{d\times d_k}$ and
$W_V \in \mathbb R^{d\times d_v}$. A note that writes a product without having
fixed the shapes is incomplete.

## 6. Status labels

The course inherits the wiki-wide set, and uses it in the same strict sense:
a label describes **what is on the page**, not what is true elsewhere.

- **[Exact.]** An identity, with no approximation and no limit taken.
- **[Asymptotic.]** A leading expression in a stated small-parameter or large-size
  limit, with the regime and omitted terms identified.
- **[Computed.]** A worked numerical example checked against its defining equations.
- **[Proposal.]** An architectural or theoretical suggestion; not an empirical result.
- **[Heuristic.]** An illustrative argument without a derivation for the target model.
- **[Stated — refs.]** A result quoted from the cited source with its hypotheses;
  the page does not claim to prove it.
- **[Approximation.]** An approximation whose control has not been established
  for the particular model or run being discussed.
- **[Thermodynamic limit.]** Holds as $N \to \infty$ at fixed intensive
  parameters; the finite-size behaviour is a separate statement.
- **[Replica-symmetric.]** Obtained through analytic continuation from integer
  replicas under a symmetry ansatz. Not a theorem.
- **[Controlled approximation.]** An approximation whose error is bounded by a
  named quantity, with that quantity stated.
- **[Model-specific.]** Exact within one explicitly delimited model; the list
  of ingredients whose removal breaks it is given.
- **[Empirical.]** Measured or fitted, with the range tested reported.

## 7. What the course does not assume

No Python, no prior machine learning, and no familiarity with the vocabulary.
A weekly note that uses *embedding*, *logit*, *head*, *teacher forcing*,
*ablation* or *cache* without defining it at first use has failed the
standard, however well the physics reads.

---

## Related

- [[nn-llm-syllabus]] — the course
- nn-llm-note-quality-template — the binding standard for weekly notes
