---
title: "Week 7 — Representations and position"
type: lecture-notes
course: nn-llm-syllabus
semester: 1
week: 7
unit: 2
duration: "4 hours (2 hr lecture + 2 hr practical)"
status: draft
modified: 2026-09-19
---

# Week 7 — Representations and Position

*Notes for [[nn-llm-syllabus|the neural-networks course]], Unit 2. Written by an AI assistant under the researcher's supervision; see [[ai-authorship]].*

*Attention acts on vectors, while text arrives as discrete labels in a
particular order. We first assign each label a vector, then supply information
about position. A permutation calculation and a two-dimensional rotation show
precisely what each construction contributes.*

---

## Learning goals

1. Explain what an embedding is, and why no invariant meaning attaches to an
   individual coordinate without a separate test.
2. **Derive** the permutation equivariance of an unmasked attention layer, and
   say what it forces.
3. **Derive** the relative-position identity for rotary encodings.
4. State what a set of rotation frequencies must satisfy before it can be said
   to distinguish every separation.

## Reading

**Primary text.** Chapter 3, §3.1 and §3.2.

**Primary literature**, through [[nn-llm-bibliography|the bibliography]]: Su
and collaborators for rotary position embeddings; Vaswani and collaborators
(2017) for the architecture the unit assembles.

**Prerequisites.** Unit 1, and in particular
[[week-06-attention-from-an-energy|Week 6]], whose update this unit embeds in
a full layer. Rotations in the plane.

## From text to numbers

A **tokenizer** is a specified rule that splits text into units and assigns an
integer label to each unit. The integer is an address in a table, not a
measured magnitude: token 20 is not twice token 10. This week constructs the
vectors that a layer can act on and the information that locates them in a
sequence. Use [[nn-llm-start-here]] for the complete two-token prediction.

## 1. What a token becomes

A token is a discrete label, and matrix multiplication needs numbers. The
**one-hot representation** places a single one in the position identifying the
token and zeros elsewhere, introducing no similarity between labels at all. An
**embedding** is a learned vector assigned to each label, and multiplying a
one-hot row vector by the embedding table simply selects a row.
For a vocabulary $(A,B,\text{.})$ and a two-component representation, choose

$$
E=\begin{pmatrix}1&0\\0&1\\1/2&1/2\end{pmatrix},\qquad
 e_B=(0,1,0),\qquad e_BE=(0,1).
$$

Here $E$ has shape $3\times2$. For the context $AB$, stacking the selected
rows gives $H=I_2$, the input used in the overview. The entries of $E$ are
learned parameters in a full model; these values are a fixed teaching example.

The representation dimension need not equal the vocabulary size, and after a
layer has mixed information across positions the vector at a position depends
on more than the identity of its own token — a **contextual representation**.
The word *hidden* in "hidden state" means internal to the calculation, not an
unobserved physical degree of freedom inferred from an experiment.

Coordinates require care. If a representation is replaced by $S\boldsymbol h$ for an
invertible $S$, an adjacent linear map can absorb $S^{-1}$, and the overall
function at that interface is unchanged.

For example, doubling a coordinate and halving the corresponding coefficient
in a downstream linear map leaves that map's output unchanged. A component
therefore acquires an interpretation only through evidence about the whole
calculation. An arbitrary basis change is not automatically a symmetry of the
full network, because nonlinearities and normalization need not commute with
it. No gauge-theory analogy is needed to use this linear-algebra fact.

## 2. Why position has to be put in by hand

The sequences $AB$ and $BA$ contain the same labels and need not mean the same
thing. An unmasked attention layer without positional information transforms their
representations in a specific way: its output rows follow the permutation.
That is **equivariance**, not equality of the two ordered output arrays.

Each of the query, key and value matrices is built by multiplying the
representation matrix on the right, so permuting the rows of the input
permutes theirs the same way. The scores become $\Pi Q K^{\mathsf T}\Pi^{\mathsf
T}$, which relabels both the rows and the entries within each row; a row-wise
softmax acts on each row separately and is blind to the order of entries
inside it, so it commutes with that relabelling; and multiplying by the
permuted values restores a single $\Pi$ on the left. Hence

$$
\mathrm{Attn}(\Pi H) = \Pi\,\mathrm{Attn}(H).
$$

More explicitly, if $A(H)=\operatorname{softmax}_{\rm row}
(QK^{\mathsf T}/\sqrt{d_k})$, then

$$
A(\Pi H)=\Pi A(H)\Pi^{\mathsf T},\qquad
 A(\Pi H)(\Pi V)=\Pi A(H)V.
$$

The output follows the permutation. A readout that averages over positions
would give the same result for $AB$ and $BA$; a readout selecting a particular
row need not. The layer has no independent positional coordinate, but it has
not made the ordered arrays identical.

> **Physical picture.** This is an explicit symmetry-breaking problem, and
> naming it that way makes the design space legible. The layer as written is
> equivariant under the symmetric group acting on positions. The task is not:
> word order carries meaning. So the symmetry must be broken, and it must be
> broken by adding something that is not permutation-covariant — a term that
> knows *which* position it sits at. Adding a position-dependent vector to the
> input does that. Rotating queries and keys by position-dependent angles does
> it differently. Both are explicit breakings of the same symmetry, and the
> choice between them is a choice about what the broken theory looks like, not
> about whether to break it.

A causal mask already introduces an ordering, through which prefixes each
position can access. It does not make an explicit representation of relative
distance redundant, and the book is careful to say so: access to a prefix is a
weaker statement than knowledge of a separation.

## 3. Relative position as a phase

Take the second route. In a two-dimensional plane, rotate the query at
position $i$ and the key at position $j$ by angles proportional to their
positions. Orthogonality and composition of rotations then give

$$
(\boldsymbol q_i')^{\mathsf T}\boldsymbol k_j' = \boldsymbol q_i^{\mathsf T} R\big((j-i)\omega\big)\,\boldsymbol k_j,
$$

To see each step, use column vectors within one rotation plane:
$q_i'=R(i\omega)q_i$, $k_j'=R(j\omega)k_j$ and
$R(i\omega)^{\mathsf T}R(j\omega)=R((j-i)\omega)$.
Thus the **positional rotation factor** depends on $j-i$. The whole score
also depends on the content vectors $q_i$ and $k_j$; it is not a function of
separation alone. In even dimension one applies independent rotations to
pairs of coordinates with a chosen frequency for each plane, which is the
construction underlying **rotary position embeddings**.

For a concrete example, at $\omega = \pi/2$
the positional contribution to a dot product of aligned unit vectors is
$\cos((j-i)\pi/2)$, taking the values $1, 0, -1$ at separations $0, 1, 2$. The
rotation preserves each norm while changing the comparison between positions.

> **Physical picture.** A quantity that depends on a difference of positions,
> realized by giving each position a phase and reading off the relative phase,
> is the most familiar construction in physics. It is translation invariance
> implemented in the way a momentum representation implements it: absolute
> phase is convention, phase difference is physical. The consequence a
> physicist should anticipate is also the familiar one — a single frequency is
> periodic, so separations differing by a full period are identified, exactly
> as a single Fourier mode cannot resolve a lattice beyond its own wavelength.
> Several frequencies help for the same reason several modes do.

## Checkpoints with answers

**1. Must the embedding dimension equal the vocabulary size?** No. The
example table has three rows but two components in each row. A row is selected
by the label; the representation dimension is a separate design choice.

**2. What does equivariance predict for a swapped two-token input?** Swap
the two output rows as well. It does not predict that each row stays fixed.

**3. With $\omega=\pi/2$ and $q_i=k_j=(1,0)$, which separations give equal
scores?** The score is $\cos((j-i)\pi/2)$, so separations zero and four both
give one. Multiple frequencies can remove some coincidences, subject to the
chosen frequencies and finite numerical precision.

---

## Subtleties and fine print

**Several frequencies do not automatically resolve everything.** The set
removes the coincidence only if no separation within the context length is a
common period of all of them, which is a statement about the chosen
frequencies *together with* the length, and must be checked for the actual
set. Extrapolation to context lengths beyond those trained on is a further
question the identity says nothing about.

**The identity is about scores, not about values.** Rotating queries and keys
gives the relative-position dependence; values are not rotated, and enter only
after the weights have been determined.

**The causal mask and positional encoding do different jobs.** The mask
restricts *which* positions are accessible. The encoding supplies *how far
away* they are. Neither substitutes for the other.

**A coordinate has no meaning until a test gives it one.** The redundancy of
§1 is the reason. A claim about what a direction represents needs evidence
that survives the transformations the architecture admits, and identifying
which those are is itself work.

**Equivariance is a property of the layer as written.** Add positional
information, or a mask, and the statement no longer holds — which is the
point. It is quoted here to motivate the addition, not as a property of the
models students will measure in Unit 3.

---

## Key claims and status

| Claim | Status |
|---|---|
| Multiplying a one-hot vector by the embedding table selects a row | [Exact.] |
| $\mathrm{Attn}(\Pi H) = \Pi\,\mathrm{Attn}(H)$ for an unmasked layer without positions | [Exact.] |
| A row-wise softmax commutes with the relabelling induced by $\Pi$ | [Exact.] |
| $(\boldsymbol q_i')^{\mathsf T}\boldsymbol k_j' = \boldsymbol q_i^{\mathsf T}R((j-i)\omega)\boldsymbol k_j$ | [Exact.] |
| A single frequency identifies separations differing by $2\pi/\omega$ | [Exact.] |
| Several frequencies distinguish every separation in a context | Conditional; depends on the frequency set and the length, and must be checked |
| An invertible change of basis is absorbed at a linear interface | [Exact] at that interface; does not extend through nonlinearities in general |

---

## What the week establishes

1. An embedding is a table lookup, and the representation dimension is
   independent of the vocabulary size.
2. An unmasked attention layer without positional information is exactly
   equivariant under permutations of the sequence, so order must be supplied
   by an explicit breaking.
3. Rotating queries and keys by position-proportional angles makes their
   positional factor depend on separation. The content vectors still enter
   the score.
4. A single rotation frequency is periodic, and what a set of frequencies
   resolves is a checkable property of the set and the context length.

**What to carry forward.** Two habits. First, ask what symmetry a layer has
before asking what it computes — the permutation argument took four lines and
determined an entire design decision. Second, treat coordinates as
conventions until something has been shown to be invariant. Unit 3 measures
quantities built out of these coordinates, and the question of which of those
measurements survive a change of basis is one the course returns to in Week 11.

## The practical session

**Varied:** the order of tokens in a short sequence; the rotation frequency
$\omega$; and the separation between two positions.
**Held fixed:** the provided blocks, the embedding table, and the projections —
nothing is trained in this session.
**Measured:** the output of an unmasked layer before and after a permutation
of the input rows, checked against the equivariance statement entry by entry;
and the positional contribution to a score as a function of separation, at one
frequency and at several.

**Product:** a demonstration that the permuted output equals the permuted
original to numerical precision; the separation at which a single frequency
first repeats; and a statement of what a chosen multi-frequency set resolves
within a given context length. Predict each result before running the block —
the session is designed for prediction first.

---

## Connections to other parts of the wiki

- [[week-06-attention-from-an-energy|Week 6]] supplies the operation this unit
  embeds in a layer, and the caution about identifying it with an energy.
- [[week-08-one-head-and-a-decoder|Week 8]] assembles the head, the mask and
  the readout, and computes a forward pass by hand.
- Week 11 measures observables built from the coordinates introduced here, and
  the redundancy of §1 is what makes some of those measurements
  basis-dependent.
- nn-llm-unit-2 — the block skeleton this note implements.

---

[[nn-llm-start-here|Start here]] · [[nn-llm-week-map|All weeks]] · [[nn-llm-resources|Book and experiments]] · [[week-06-attention-from-an-energy|Previous week]] · [[week-08-one-head-and-a-decoder|Next week]]
