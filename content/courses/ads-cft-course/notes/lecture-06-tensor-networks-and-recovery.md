---
title: "Lecture 6 — Tensor networks as explicit encodings"
type: lecture-notes
edition: "2.1"
semester: 1
week: 4
lecture: 6
duration: "4 hours; two meetings and additional self-study"
status: written; validation tracked in the course record
modified: 2026-09-29
---

# Lecture 6 — Tensor networks as explicit encodings

A tensor-network drawing is useful only if its lines and vertices stand for specified linear maps. Otherwise an apparent relation between geometry and information may be a property of the picture rather than of a quantum state.

We will use the three-qutrit encoding from Lecture 2 as our only building block. First we turn it into a four-leg state and verify its entanglement. Then we join two copies, calculate entropies, and determine when a cut bound is saturated. Finally we concatenate encoders and recover an unknown input from selected boundary shares.

Two objects must remain distinct throughout: a network preparing one fixed state, and a network encoding a family of logical states. Entropy is a property of a state and a partition. Recovery is a property of a channel on an entire specified input space.

## How to use this lecture

**Classroom core.** Meeting 1: tensor notation and the four-qutrit state (40 minutes), its two-leg reductions (35), and a two-vertex state with an entropy calculation (45). Meeting 2: prove the cut bound (30), construct the concatenated encoder (35), compare an authorized and an unauthorized region (35), and discuss the limits of the geometric analogy (20).

**Self-study.** Check all six choices of two legs in the four-qutrit state. Derive the nonuniform-bond counterexample. Track the recovery maps with an external reference.

**Research extension.** Enumerate the six-boundary state entropies and compare them with the four possible assignments of its two internal vertices to a graph cut. This is a small finite computation; no continuum limit is required.

**Prerequisites.** Lectures 2 and 4, elementary matrix rank, and the Schmidt decomposition.

**Reading.** Pastawski, Yoshida, Harlow, and Preskill, [arXiv:1503.06237](https://arxiv.org/abs/1503.06237), develops perfect-tensor holographic codes. The particular networks below are completely specified and calculated here. We do not assume that every tensor network obeys an exact geometric entropy formula.

## 1. A tensor is a table of amplitudes

Recall the isometry
$$
V|i\rangle=\frac1{\sqrt3}\sum_{r=0}^{2}
|r,r+i,r+2i\rangle.
$$
All labels are modulo three. Its coefficients are a four-index array,
$$
V_{abc;i}
=\frac1{\sqrt3}\delta_{b,a+i}\delta_{c,a+2i}.
$$
The semicolon distinguishes the input label from the output labels. A line in a diagram represents one index. Joining an output line to an input line means summing their common index, exactly as in matrix multiplication.

For example, if $V$ is followed by another map $W$ on its first output, the new coefficient is
$$
T_{xyzbc;i}=\sum_a W_{xyz;a}V_{abc;i}.
$$
The drawing saves space, but the sum defines the object. It also reveals the dimensions: there is one logical qutrit and five output qutrits.

An isometry obeys $V^\dagger V=I$. Consequently composing isometries gives another isometry. This elementary fact will provide the normalization of the concatenated code without summing thousands of components.

## 2. Turn the encoder into a four-party state

Introduce a reference qutrit $R$ and maximally entangle it with the input:
$$
|T\rangle
=\frac1{\sqrt3}\sum_i|i\rangle_RV|i\rangle
=\frac13\sum_{i,r}|i,r,r+i,r+2i\rangle.
$$
The nine basis strings are distinct, so the state is normalized. Name its four output labels
$$
x_0=i,\qquad x_1=r,\qquad x_2=r+i,\qquad x_3=r+2i.
$$
Each is a linear function of $(i,r)$ over arithmetic modulo three.

Any two of these functions determine $(i,r)$ uniquely. For instance, $x_1,x_2$ give $r=x_1$ and $i=x_2-x_1$; $x_2,x_3$ give $i=x_3-x_2$ and $r=2x_2-x_3$. The other cases work because the corresponding two-by-two coefficient matrices have nonzero determinant modulo three.

Now retain any two legs and trace the other two. In an off-diagonal term labeled by $(i,r)$ and $(j,s)$, the trace requires equality of the two discarded labels. Their invertibility forces $i=j,r=s$. Thus no off-diagonal term survives. The retained pair takes all nine possible values exactly once, each with probability $1/9$:
$$
\boxed{\rho_{\text{any two legs}}=I_9/9.}
$$
Every single leg is $I_3/3$. The two-versus-two Schmidt coefficients are all $1/3$.

**Definition used here.** A normalized four-leg state with maximally mixed reductions on every pair is an absolutely maximally entangled four-party state. Its coefficient array is called a perfect tensor because reshaping any two legs as inputs and the other two as outputs gives a map proportional to a unitary.

The proportionality matters. Our normalized state has coefficients $1/3$, so its two-to-two matrix $T$ obeys $T^\dagger T=I_9/9$. The unitary map is $3T$. As a one-to-three encoding, the normalized isometry is $V$, not the same coefficient array without rescaling.

**Checkpoint 1.** Does the maximal mixing of every pair imply that all four parties are jointly maximally mixed?

**Answer.** No. The full state is pure. These are restrictions of one entangled vector to smaller algebras.

## 3. Join two encoders through a maximally entangled bond

Take two triples of physical qutrits, called $L_1,L_2,L_3$ and $R_1,R_2,R_3$. Prepare
$$
|\Psi\rangle
=\frac1{\sqrt3}\sum_{i=0}^{2}
V|i\rangle_L\otimes V|i\rangle_R.
$$
This means: prepare a Bell pair of virtual qutrits, then encode each member into three physical shares.

In coefficients,
$$
|\Psi\rangle
=\frac1{3\sqrt3}
\sum_{i,r,s}
|r,r+i,r+2i\rangle_L
|s,s+i,s+2i\rangle_R.
$$
The 27 strings are distinct and have equal amplitudes. A diagram has two internal vertices connected by one bond of dimension three, with three boundary legs emerging from each vertex. No additional tensors are left unspecified.

Because the three vectors $V|i\rangle_L$ are orthonormal, the first expression is already a Schmidt decomposition between the complete left and right triples:
$$
\rho_L=\frac13VV^\dagger,\qquad S(L)=\log3.
$$
The reduced matrix has rank three in a 27-dimensional Hilbert space. Its entropy counts the shared virtual qutrit, not the number of physical output registers.

### 3.1 Other boundary regions

Any single boundary qutrit has entropy $\log3$. Any two boundary qutrits have entropy $2\log3$, whether they lie on the same or different vertices.

For two on the same side, the input to $V$ is $I_3/3$ and Lecture 2's decoder gives $I_9/9$. For one on each side, both one-share channels erase all logical matrix units except their trace. Their joint output is therefore $I_3/3\otimes I_3/3$, even though the virtual input was entangled.

Three qutrits exhibit a useful distinction:
$$
S(L_1L_2L_3)=\log3,\qquad
S(L_1L_2R_1)=3\log3.
$$
To verify the second formula directly, its retained labels are $(r,r+i,s)$, which determine $(i,r,s)$ uniquely. Its discarded labels are $(r+2i,s+i,s+2i)$ and are also invertible functions of those variables. The partial trace is therefore $I_{27}/27$.

By purity, entropies for four and five retained qutrits equal those of their two- and one-qutrit complements. The complete list follows without diagonalizing a 729-by-729 density matrix.

> **Physical picture.** Three outputs belonging to one encoded virtual qutrit contain much redundant structure. Three outputs crossing the two encoders can cut through more independent entanglement. Counting boundary registers alone does not determine entropy.

## 4. What a cut proves

Consider a pure tensor-network state and a cut separating boundary region $A$ from its complement. Suppose the cut crosses bonds with dimensions $d_1,\ldots,d_m$. Group all crossed indices into one label $\alpha$ taking
$$
D=\prod_{j=1}^{m}d_j
$$
values. Contracting the tensors on each side gives
$$
|\psi\rangle=\sum_{\alpha=1}^{D}
|u_\alpha\rangle_A|v_\alpha\rangle_{\bar A}.
$$
The vectors need not be orthogonal. Nevertheless, $\rho_A$ is supported on the span of at most $D$ vectors, so
$$
\operatorname{rank}\rho_A\le D.
$$
For a normalized rank-$r$ density matrix with eigenvalues $\lambda_k$, the entropy is at most $\log r$, with equality only when all nonzero eigenvalues equal $1/r$. One proof compares the probabilities with the uniform distribution:
$$
\sum_k\lambda_k\log\frac{\lambda_k}{1/r}
=\log r-S(\rho_A)\ge0.
$$
The classical inequality follows from $\log x\le x-1$ or convexity. Hence every cut gives
$$
\boxed{
S(A)\le\sum_{j\in\text{cut}}\log d_j.
}
$$
Minimizing over cuts improves the bound. This is a rank argument; it does not yet prove equality.

### 4.1 The equality condition

If both families in the cut decomposition are orthonormal, up to a common normalization, and the bond weights are uniform, the expression is a flat Schmidt decomposition. Then $S(A)=\log D$.

For the complete left triple of our two-vertex state, both sides are the isometry $V$, and the single bond is maximally entangled. This gives equality with the one-bond cut.

For $L_1L_2R_1$, the minimal cut crosses three dimension-three bonds. One can check this by assigning each of the two vertices to either side of the partition: there are only four assignments. The entropy calculation above gives $3\log3$, again saturating the bound.

The invertible finite-field maps establish the other cases in this particular network. We have not proved saturation for arbitrary graphs, tensors, bulk states, or disconnected boundary regions.

### 4.2 Same graph, smaller entropy

Replace the virtual Bell pair by
$$
|\chi\rangle=\sum_i\sqrt{p_i}|i,i\rangle,
\qquad p_i>0,\quad \sum_ip_i=1.
$$
The state becomes $\sum_i\sqrt{p_i}V|i\rangle_LV|i\rangle_R$. Its left entropy is
$$
S(L)=H(p_0,p_1,p_2)\le\log3,
$$
strictly smaller unless all weights are equal. The cut still has dimension three.

For $p=(1/2,1/3,1/6)$, the Schmidt rank saturates the dimension bound, but the entropy does not. Even full rank is insufficient: the Schmidt spectrum must also be flat.

**Checkpoint 2.** What has failed when a minimal cut exceeds the entropy?

**Answer.** Nothing has failed in the rank bound. Its saturation requires additional properties of the tensors and the state.

## 5. A network that encodes an unknown state

Now compose the encoder with three more copies:
$$
\mathcal V=(V\otimes V\otimes V)V.
$$
The first $V$ maps the logical qutrit into three intermediate shares. Each intermediate share is encoded into its own block of three leaves. Label the leaves $B_{j1},B_{j2},B_{j3}$, where $j=1,2,3$ labels the block.

The full map sends one qutrit into nine:
$$
\mathcal V^\dagger\mathcal V
=V^\dagger(V^\dagger V)^{\otimes3}V=I.
$$
The network is a code, because its input remains variable.

### 5.1 Four appropriately placed leaves recover the input

Keep two leaves in block 1 and two in block 2. Apply Lecture 2's decoder independently within each block. This recovers intermediate shares 1 and 2, with auxiliary registers that can be discarded.

Then apply the outer two-share decoder to those recovered intermediate shares. The composition of recovery channels obeys
$$
\mathcal R_A\!\left(
\operatorname{Tr}_{\bar A}\mathcal V\rho\mathcal V^\dagger
\right)=\rho
$$
for every logical input, including inputs entangled with a reference.

No state-dependent choice is needed. Each step is the same linear channel that was already proved to recover all matrix units.

A logical observable is reconstructed by composing the corresponding Heisenberg maps in reverse order. In this way operator pushing means an intertwining identity, not a guess based on proximity in the drawing.

### 5.2 Five badly placed leaves can reveal nothing

Instead keep all three leaves of block 1, one leaf of block 2, and one leaf of block 3. The last two blocks each pass through a constant one-share channel. On arbitrary outer matrix units, those channels retain only the trace. The surviving complete block therefore carries the outer share-1 state, which is itself $I_3/3$ for every input.

The entire accessible output is
$$
V(I_3/3)V^\dagger
\otimes I_3/3\otimes I_3/3,
$$
independent of $\rho$. This five-leaf region cannot reconstruct even one nonconstant logical expectation.

Four leaves can suffice, while another set of five contains no logical information. Recovery depends on the access pattern, not only its size.

**Checkpoint 3.** Does this contradict monotonicity of recoverability under adding accessible shares?

**Answer.** No. The unauthorized five-leaf region does not contain the authorized four-leaf region. If a region contains a recoverable subregion, one can discard the extra shares and use the existing decoder.

## 6. From this model toward holography

The networks isolate several features that later recur in bulk reconstruction: redundant encodings, different boundary representatives of one logical operator, and entropy bounds controlled by internal connections. Their exact content can be checked without interpreting the drawing as a spacetime.

A geometric interpretation requires more. Our tree has no Lorentzian causal structure, boundary Hamiltonian, or continuum limit. The two-vertex state has no variable bulk degrees of freedom at all. A minimal graph cut becomes an entropy formula only under conditions such as those we explicitly verified.

In networks with logical bulk inputs, fixing those inputs, mixing them, or entangling them with a reference changes the entropy problem. The logical contribution derived in Lecture 4 must be retained when appropriate. Counting only virtual bonds can omit it.

The purpose of these limitations is constructive: they identify what QFT locality, a holographic dictionary, and gravitational dynamics must add to an information-theoretic encoding.

## 7. What to take away

Every network in this lecture has a basis map. The perfect-tensor property follows from invertibility of finite-field label maps. A cut bounds entropy through Schmidt rank; equality also requires the right spectrum. Concatenation produces an explicit recovery channel, and differently arranged boundary shares can have radically different access to the logical state.

## 8. Problem set

### Classroom core

**1. An unfamiliar pair.** Given $x_0=i$ and $x_3=r+2i$, solve for $(i,r)$. Explain why this is enough to calculate the corresponding two-leg reduction of $|T\rangle$.

**2. The cut bound.** A cut crosses bonds of dimensions $2,3,5$. What upper bound follows for the entropy? State two reasons it might be strict.

**3. Recover the tree input.** Keep leaves 2 and 3 in block 2 and leaves 3 and 1 in block 3. Specify the three ordered-pair decoders needed to recover the root input.

### Self-study consolidation

**4. A nonuniform bond.** For $p=(1/2,1/3,1/6)$, compute $H(p)$ and compare it with $\log3$. Does the Schmidt rank change?

**5. A complete block.** Show that the three-leaf region consisting of block 2 alone carries no information about the root input. Why does keeping an entire inner block not suffice?

### Research extension

**6. Exhaust the small graph.** For every nonempty proper subset of the six boundary legs of $|\Psi\rangle$, calculate its entropy by reshaping the coefficient tensor. Compare with the minimal graph cut. State the tensor and normalization used so the result is reproducible.

## 9. Answer checkpoints

**1.** $r=x_3-2x_0$. The complementary pair is also an invertible function of $(i,r)$, which removes every off-diagonal term upon tracing. The retained labels run uniformly over all nine pairs.

**2.** $S\le\log30$. The vectors generated by the cut may be linearly dependent, reducing the Schmidt rank; even at rank 30 the Schmidt weights may be nonuniform.

**3.** Use $D_{23}$ in block 2 and $D_{31}$ in block 3, then $D_{23}$ on the recovered outer shares. The output locations must be relabeled according to the ordered pairs before composing the maps.

**4.** $H(p)=\frac23\log2+\frac12\log3$, approximately $1.0114$, below $\log3\approx1.0986$. All three probabilities are nonzero, so the rank remains three.

**5.** Its state is $V(I_3/3)V^\dagger$. Decoding the inner block recovers one outer share; a single outer share has no root information.

**6.** Singles have entropy $\log3$ and pairs $2\log3$. A triple containing all outputs of one vertex has entropy $\log3$; every other triple has $3\log3$. Use purity for four- and five-leg regions. These values saturate the cuts of this particular two-vertex graph. The unequal-weight example shows why the result cannot be inferred from its graph alone.

---

Previous: [[lecture-05-constraints-and-regional-algebras|Lecture 5]]. Return to the [[courses/ads-cft-course/syllabus|syllabus]].

**Wiki connections.** [[ryu-takayanagi-formula|Ryu–Takayanagi formula]]
