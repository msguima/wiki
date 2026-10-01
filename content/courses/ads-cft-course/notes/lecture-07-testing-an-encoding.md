---
title: "Lecture 7 — When an encoding stops protecting information"
type: lecture-notes
edition: "2.1"
semester: 1
week: 5
lecture: 7
duration: "4 hours; consolidation and a worked finite-model project"
status: written; validation tracked in the course record
modified: 2026-09-29
---

# Lecture 7 — When an encoding stops protecting information

The opening models established exact identities. A useful test of understanding is to change one assumption and determine precisely which conclusions survive. We will deform the three-qutrit code by changing its amplitudes. The images of the logical basis remain orthogonal, but the symmetry between the shares disappears.

This gives a complete small project: specify an encoding, calculate the channels seen by different observers, construct one exact decoder, diagnose two failed recovery regions, and quantify the loss of phase information. It also prepares the later discussion of approximate bulk reconstruction.

## How to use this lecture

**Classroom core.** Meeting 1: students predict what unequal amplitudes might change (15 minutes), construct the new code (25), calculate all single-share states (40), and find the surviving decoder (40). Meeting 2: derive the imperfect decoder (35), measure its loss of distinguishability (35), compare the earlier models (25), and discuss project solutions (25).

**Self-study.** Reproduce the channel on every logical matrix unit. Check the limiting encodings and the small-deformation expansion. Write the difference between a state calculation and an all-input recovery statement in your own words.

**Research extension.** Optimize a recovery channel for a chosen unequal distribution, with the figure of merit and the reference system specified. The calculation of one decoder below does not claim such an optimization.

**Prerequisites.** Lectures 1–6. The only additional information-theoretic tool is binary state discrimination, introduced in Section 5.

**Sources and scope.** The undeformed construction is due to quantum secret sharing; see [Cleve–Gottesman–Lo, arXiv:quant-ph/9901025](https://arxiv.org/abs/quant-ph/9901025). The deformed family and calculations here are an exercise in the same finite framework. No statement about the size of holographic reconstruction errors follows from its deformation parameter.

## 1. Orthogonality does not guarantee erasure protection

Choose probabilities
$$
\lambda_r\ge0,\qquad \lambda_0+\lambda_1+\lambda_2=1,
$$
and define
$$
V_\lambda|i\rangle
=\sum_{r=0}^{2}\sqrt{\lambda_r}
|r,r+i,r+2i\rangle.
$$
As before, arithmetic is modulo three. Distinct logical labels use disjoint computational strings. Every codeword has norm one, so
$$
V_\lambda^\dagger V_\lambda=I.
$$
The map always preserves a complete logical state when all three physical shares are available.

For $\lambda_r=1/3$, it is the old code. For $\lambda=(1,0,0)$,
$$
V_\lambda|i\rangle=|0,i,2i\rangle.
$$
This endpoint plainly copies a computational label into two shares. It cannot preserve a relative phase after losing either of those shares. The interpolation therefore separates isometric encoding from error protection.

**Checkpoint 1.** Which property follows immediately from the isometry, and which requires a separate calculation?

**Answer.** Full-system inner products and logical distinguishability are preserved. Recoverability after tracing out a subsystem requires calculating that channel.

## 2. What each single observer sees

For share 1, trace an arbitrary encoded matrix unit:
$$
\operatorname{Tr}_{23}
V_\lambda|i\rangle\langle j|V_\lambda^\dagger
=\sum_{r,s}\sqrt{\lambda_r\lambda_s}
|r\rangle\langle s|\,
\delta_{r+i,s+j}\delta_{r+2i,s+2j}.
$$
Subtracting the two equality conditions gives $i=j$, then $r=s$. Hence
$$
\operatorname{Tr}_{23}
V_\lambda|i\rangle\langle j|V_\lambda^\dagger
=\delta_{ij}\sum_r\lambda_r|r\rangle\langle r|.
$$
Share 1 has a fixed state for every input.

The same trace on share 2 gives
$$
\operatorname{Tr}_{13}
V_\lambda|i\rangle\langle j|V_\lambda^\dagger
=\delta_{ij}\sum_r\lambda_r|r+i\rangle\langle r+i|.
$$
Share 3 gives the analogous shift by $2i$. Thus for a logical state $\rho$,
$$
\rho_2=\sum_{i,r}\rho_{ii}\lambda_r
|r+i\rangle\langle r+i|,
\qquad
\rho_3=\sum_{i,r}\rho_{ii}\lambda_r
|r+2i\rangle\langle r+2i|.
$$
They depend on logical populations, although neither sees logical coherences.

For a nonuniform $\lambda$, the three computational inputs give different cyclic permutations of the probabilities. The inaccessible share can now retain information about which logical component was present. That information can obstruct coherent recovery on its complement.

### 2.1 A numerical distribution

Take
$$
\lambda=(1/2,1/4,1/4).
$$
For input $|0\rangle$, share 2 has probabilities $(1/2,1/4,1/4)$. For input $|1\rangle$, they are $(1/4,1/2,1/4)$. Measuring the computational basis already distinguishes these distributions statistically.

For equal prior probabilities, the classical total-variation distance is
$$
T=\frac12\sum_b|p_b-q_b|=\frac14,
$$
and the optimal success probability is $(1+T)/2=5/8$. A single share does not reveal the entire input, but it reveals something. Perfect protection requires the relevant erased share to reveal nothing about any input.

## 3. One pair still recovers exactly

Retain shares 2 and 3. The ordered-pair decoder from Lecture 2 acts as
$$
D_{23}|r+i,r+2i\rangle
=|i,r\rangle.
$$
Therefore
$$
(D_{23}\otimes I_1)V_\lambda|i\rangle
=|i\rangle_{\mathrm{out}}\otimes
\sum_r\sqrt{\lambda_r}|r\rangle_{\mathrm{aux}}|r\rangle_1,
$$
where the tensor factors have been reordered to place the logical output first. The auxiliary state is independent of $i$.

For an arbitrary superposition, the same identity factors out the complete logical vector. It also holds with a reference system. After share 1 has been erased, decoding the pair gives
$$
D_{23}\rho_{23}D_{23}^\dagger
=\rho\otimes\operatorname{diag}(\lambda).
$$
Tracing the auxiliary output recovers $\rho$ exactly.

The pair entropy is
$$
S(\rho_{23})=S(\rho)+H(\lambda).
$$
This is the same mechanism as Lecture 4: fixed auxiliary entanglement contributes a fixed entropy. Maximal auxiliary entanglement is not required for this one region's exact recovery.

The other two recovery regions fail because the auxiliary state exposed by their old decoders depends on the logical label. We now calculate that dependence.

## 4. The old decoder becomes a dephasing channel

Keep shares 1 and 2 and apply $D_{12}$. On a logical basis vector,
$$
(D_{12}\otimes I_3)V_\lambda|i\rangle
=|i\rangle\otimes|\chi_i\rangle,
$$
where
$$
|\chi_i\rangle
=\sum_s\sqrt{\lambda_{s-2i}}|s,s\rangle.
$$
The index was relabeled as $s=r+2i$. If the probabilities are unequal, these auxiliary states depend on $i$.

Decode and discard the accessible auxiliary output. Tracing both auxiliary factors gives the channel
$$
|i\rangle\langle j|
\longmapsto
\langle\chi_j|\chi_i\rangle\,|i\rangle\langle j|.
$$
The overlap is one for $i=j$. For any distinct pair of qutrit labels, it is
$$
c_\lambda
=\sqrt{\lambda_0\lambda_1}
+\sqrt{\lambda_1\lambda_2}
+\sqrt{\lambda_2\lambda_0}.
$$
There are only the two nonzero cyclic shifts, and both yield the same real sum. Thus
$$
\boxed{
\mathcal R_{12}^{\mathrm{old}}\mathcal N_{12}(\rho)
=c_\lambda\rho+(1-c_\lambda)\operatorname{diag}(\rho).
}
$$
The populations survive. Every off-diagonal entry is reduced by the same factor.

By Cauchy–Schwarz, $c_\lambda\le1$, with equality only for the uniform distribution. It is nonnegative and vanishes at a distribution concentrated on one label.

For $\lambda=(1/2,1/4,1/4)$,
$$
c_\lambda=\frac1{\sqrt2}+\frac14\approx0.9571.
$$
For the equal superposition $|+\rangle_3=3^{-1/2}\sum_i|i\rangle$, the overlap fidelity of this decoded state with its input is
$$
\langle+|\rho_{\mathrm{out}}|+\rangle
=\frac{1+2c_\lambda}{3}.
$$
This number is close to one for that example. It is a statement about a specified input and decoder; it is not yet a worst-case channel bound.

> **Physical picture.** The auxiliary system has recorded a partial indication of the logical label. Discarding that record suppresses interference between labels. The unequal weights convert a perfect decoder into an exactly calculable dephasing process.

## 5. Could a better decoder restore everything?

A poor result from one decoder does not establish impossibility. We need a property of the accessible output itself. Consider the orthogonal logical states
$$
|\pm_{01}\rangle=\frac{|0\rangle\pm|1\rangle}{\sqrt2}.
$$
Their logical distinction is entirely a phase. After erasing share 3 and applying the unitary $D_{12}$, the accessible states split into blocks labeled by the auxiliary value $s$:
$$
\rho_\pm^{(s)}
=\frac12
\begin{pmatrix}
\lambda_s&
\pm\sqrt{\lambda_s\lambda_{s-2}}\\
\pm\sqrt{\lambda_s\lambda_{s-2}}&
\lambda_{s-2}
\end{pmatrix}.
$$
Their difference in each block has eigenvalues
$$
\pm\sqrt{\lambda_s\lambda_{s-2}}.
$$
For density matrices, define trace distance by
$$
T(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
$$
Adding the absolute eigenvalues over blocks gives
$$
\boxed{
T(\rho_+^{12},\rho_-^{12})=c_\lambda.
}
$$
The logical input distance was one. For nonuniform $\lambda$, it has become strictly smaller.

Why does this exclude every exact decoder? A measurement performed after a physical recovery channel is also an allowed measurement on its input: pull the effects back through the channel's adjoint. Processing cannot make two states more distinguishable than the best measurement already allowed on them.

More explicitly, a binary measurement with effect $0\le E\le I$ and equal priors succeeds with probability
$$
p_{\mathrm{succ}}
=\frac12+\frac12\operatorname{Tr}\bigl[E(\rho-\sigma)\bigr].
$$
Choosing the projector onto the positive eigenspace of $\rho-\sigma$ gives the maximum $(1+T)/2$. The displayed accessible states cannot be distinguished perfectly because $c_\lambda<1$. An exact decoder restoring the orthogonal logical states would permit perfect discrimination, a contradiction.

This is a recovery obstruction based on the actual channel, not on the shortcomings of our chosen decoder.

**Checkpoint 2.** Why would checking only inputs $|0\rangle,|1\rangle,|2\rangle$ miss this obstruction?

**Answer.** The old decoder restores those basis states exactly. The obstruction appears in the coherence between them.

## 6. A controlled small deformation

Set
$$
\lambda_i=\frac13+\varepsilon x_i,
\qquad \sum_i x_i=0,
$$
and keep $\varepsilon$ small enough that every probability is positive. Expanding
$$
\sqrt{\lambda_i}
=\frac1{\sqrt3}
\left(1+\frac32\varepsilon x_i
-\frac98\varepsilon^2x_i^2+O(\varepsilon^3)\right)
$$
and using
$$
c_\lambda=\frac12\left[
\left(\sum_i\sqrt{\lambda_i}\right)^2-1
\right]
$$
gives
$$
c_\lambda
=1-\frac98\varepsilon^2\sum_i x_i^2+O(\varepsilon^3).
$$
The first-order term vanishes because the probabilities remain normalized and the uniform distribution maximizes the overlap.

For $x=(1,-1,0)$, the leading loss is $1-c_\lambda=9\varepsilon^2/4$. This is a controlled expansion inside a finite model with an explicit positivity range. It supplies no relation between $\varepsilon$ and $1/N$ or $G_N$ in a gravitational theory.

## 7. Consolidating the algebraic language

The earlier examples answer different questions:

| Model | Accessible structure | What has been established |
|---|---|---|
| Bell pair | One tensor-factor algebra | Global distinctions may be invisible locally |
| Uniform qutrit code | Any two physical shares | Exact recovery on an entire logical space |
| Unequal qutrit code | Pair 23 versus pair 12 | Recovery can depend on amplitudes and region |
| Constrained four-qubit model | Direct sum of matrix algebras | A shared center can coexist with local quantum information |
| Two-vertex tensor state | Fixed state and graph cuts | A cut bounds entropy; saturation needs the state and tensors |
| Concatenated qutrit code | Selected boundary leaves | Connectivity controls which decoders can be composed |

A geometric picture may suggest a reconstruction region, but the accessible channel decides what is reconstructable. In finite systems this can be tested through matrix units, an entangled reference, or operational distinguishability. Later, continuum QFT will require replacing intrinsic local density matrices by states on algebras. The questions about access remain.

## 8. What to take away

A code can remain isometric while losing erasure protection. The absence of information in an erased share is tied to recovery on its complement. A decoder's fidelity is different from an impossibility bound against all decoders. Uniformity of a Schmidt spectrum is an assumption that can be varied and checked, not a decorative normalization.

![[ads-cft-deformed-code-recovery.svg|Recovery as the first encoding weight changes. Pair 23 remains exact; the plotted pair-12 overlap belongs to the explicit decoder, not an optimized decoder.]]

## 9. Problem set

### Classroom core

**1. An endpoint.** For $\lambda=(1,0,0)$, compute the three single-share channels and identify the one pair that recovers every input.

**2. Unequal entropy.** For a pure logical input, calculate $S(\rho_{23})$. Explain why it can vary with $\lambda$ even though recovery on 23 remains exact.

**3. Phase test.** Apply the old pair-12 decoder to $|\pm_{01}\rangle$. Compute the trace distance of the decoded logical states and their optimal discrimination probability.

### Self-study consolidation

**4. Reference test.** Encode one half of $|\Phi_3\rangle$. Apply the pair-12 decoder and compute the overlap of the output/reference state with $|\Phi_3\rangle$.

**5. Expansion.** Derive the coefficient $9/8$ in Section 6 without expanding each pair separately. Explain the absence of a linear term.

### Research extension

**6. Recovery objective.** Choose a nonuniform distribution. Formulate a worst-case entanglement-fidelity optimization over recovery channels. Specify input/output dimensions and complete-positivity and trace-preservation constraints. An explicit numerical optimum is optional; a claim of optimality requires a corresponding bound or certificate.

## 10. Answer checkpoints

**1.** Share 1 is fixed in $|0\rangle$. Shares 2 and 3 carry logical populations in their computational bases, with the third label permuted by $i\mapsto2i$. Pair 23 recovers the complete input; losing either share 2 or share 3 removes coherences.

**2.** $S(\rho_{23})=H(\lambda)$. This is auxiliary entropy exposed by an exact decoder. Its size does not measure an error in the recovered logical factor.

**3.** Both diagonals are $(1/2,1/2,0)$ and their off-diagonal entries are $\pm c_\lambda/2$. Their trace distance is $c_\lambda$ and success probability is $(1+c_\lambda)/2$.

**4.** The channel multiplies all six off-diagonal logical matrix units by $c_\lambda$ and leaves three diagonal units unchanged. The entanglement overlap is $(3+6c_\lambda)/9=(1+2c_\lambda)/3$.

**5.** Sum the three square-root expansions first. The linear term contains $\sum_i x_i=0$. Squaring the sum and using the identity for $c_\lambda$ gives the stated coefficient.

**6.** The recovery maps a nine-dimensional retained system to a logical qutrit. A Choi matrix for it must be positive and have output partial trace equal to the input identity. State whether the chosen objective is worst-case over logical/reference pure states or averaged over inputs; these are different problems. The obstruction in Section 5 is a useful independent consistency check.

---

Previous: [[lecture-06-tensor-networks-and-recovery|Lecture 6]]. Return to the [[courses/ads-cft-course/syllabus|syllabus]].
