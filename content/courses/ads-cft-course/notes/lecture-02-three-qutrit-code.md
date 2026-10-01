---
title: "Lecture 2 — A quantum system hidden in three qutrits"
type: lecture-notes
course: syllabus
edition: "2.0"
semester: 1
week: 1
lecture: 2
duration: "2 hours; additional self-study material"
status: written — checked in the scope of the validation record
modified: 2026-09-28
---

# Lecture 2 — A quantum system hidden in three qutrits

In Lecture 1, information about a preparation could be absent from every single-system state and present in correlations. We now ask for more: can those correlations protect an unknown quantum state against losing a physical subsystem?

The word “unknown” is essential. A decoder must recover every superposition and must continue to work when the input is entangled with another system. Recovering a classical label from a list of basis states is not sufficient. We will build an encoding that meets the stronger requirement using three qutrits, each with basis $|0\rangle,|1\rangle,|2\rangle$.

This is our first model of reconstruction from overlapping regions. Everything can be checked with finite matrices. The model has no gravitational dynamics; its role is to isolate the encoding structure that later appears in discussions of bulk reconstruction.

## How to use this lecture

**Classroom core, 120 minutes.** The repetition-code comparison and encoding take 25 minutes, the one-share calculation 25, the decoder 30, and operator reconstruction plus no-cloning 25. Use the remaining 15 minutes for a worked input and the exit question. Sections 6 and 8 provide additional derivations for the problem session or self-study.

**Self-study.** Follow every off-diagonal matrix unit through the partial trace. Check the inverse of the decoder map. Verify one logical $X$ and one logical $Z$ representative on all three encoded basis vectors. Then repeat the argument with a reference system.

**Research extension.** Compare exact erasure correction with approximate recovery or with recovery of only a subalgebra. The latter will be our focus in Lecture 4.

**Prerequisites.** [[lecture-01-observables-and-restricted-access|Lecture 1]], especially state restriction, partial traces, and joint correlations. All arithmetic on qutrit labels below is modulo three.

**Reading.** Cleve, Gottesman, and Lo, [arXiv:quant-ph/9901025](https://arxiv.org/abs/quant-ph/9901025), introduces quantum secret sharing. Harlow's [TASI lectures, arXiv:1802.01040](https://arxiv.org/abs/1802.01040), Section 4.2, use this code to explain holographic reconstruction. The connection with bulk locality was developed by Almheiri, Dong, and Harlow, [arXiv:1411.7041](https://arxiv.org/abs/1411.7041).

**What this lecture imports.** The code is a known construction, credited above. We prove its encoding, erasure, and reconstruction properties here. We do not import a general quantum-error-correction theorem as a substitute for calculating the decoder.

## 1. Why ordinary repetition loses a quantum phase

For a classical bit, repetition is useful: encode $0$ as $000$ and $1$ as $111$. If one bit is lost, either of the remaining bits still reveals the original label.

The corresponding quantum isometry would send
$$
\alpha|0\rangle+\beta|1\rangle
\longmapsto
\alpha|000\rangle+\beta|111\rangle.
$$
This operation is allowed: it is an encoding, not a map that creates three independent copies of an unknown state. But tracing out the third qubit gives
$$
|\alpha|^2|00\rangle\langle00|
+|\beta|^2|11\rangle\langle11|.
$$
The cross term $|000\rangle\langle111|$ vanishes under the trace because $\langle1|0\rangle=0$ on the lost qubit. The remaining state retains the populations and loses their relative phase.

In particular, the inputs $|+\rangle$ and $|-\rangle$ produce the same two-qubit state after this erasure. No decoder can map that one output state back to two distinguishable inputs. The repetition encoding protects some classical information, but it does not correct this quantum erasure.

The lost subsystem has learned something about the input: whether its computational-basis label was $0$ or $1$. For a superposition, that record destroys the phase accessible to the survivors. Our next encoding will make every individual share independent of the logical input.

## 2. Constructing the encoding

Let the logical Hilbert space be $\mathcal H_{\mathrm{code}}=\mathbb C^3$. We encode it into
$$
\mathcal H_{\mathrm{physical}}
=\mathbb C^3_1\otimes\mathbb C^3_2\otimes\mathbb C^3_3.
$$
Subscripts $1,2,3$ label physical shares. Define
$$
V|i\rangle=|\widetilde i\rangle
=\frac1{\sqrt3}\sum_{r=0}^{2}
|r,\ r+i,\ r+2i\rangle.
$$
The three encoded basis states are
$$
\begin{aligned}
|\widetilde0\rangle
&=\frac{|000\rangle+|111\rangle+|222\rangle}{\sqrt3},\\
|\widetilde1\rangle
&=\frac{|012\rangle+|120\rangle+|201\rangle}{\sqrt3},\\
|\widetilde2\rangle
&=\frac{|021\rangle+|102\rangle+|210\rangle}{\sqrt3}.
\end{aligned}
$$
There are nine different computational-basis strings in this list. Within each encoded vector they are orthogonal, giving unit norm. Between two different encoded vectors there is no common string, giving zero overlap. Therefore
$$
\langle\widetilde i|\widetilde j\rangle=\delta_{ij},
\qquad V^\dagger V=I_{\mathrm{code}}.
$$
This proves that $V$ is an **isometry**. It preserves inner products and hence all quantum information if the full output remains available.

The image of $V$ is a three-dimensional **code subspace** of the 27-dimensional physical Hilbert space. The projector onto it is
$$
P=VV^\dagger
=\sum_{i=0}^{2}|\widetilde i\rangle\langle\widetilde i|.
$$
The other 24 dimensions are physical states outside this encoding. Our reconstruction identities will be statements on the image of $V$, not arbitrary identities on the full 27-dimensional space.

> **Physical picture.** A code specifies a controlled set of allowed preparations inside a larger system. Different physical operators may act in the same way on all allowed preparations while acting differently elsewhere. This freedom will let a logical observable have several physical representatives.

For an unknown input $|\psi\rangle=\sum_i c_i|i\rangle$, the encoded state is $V|\psi\rangle=\sum_i c_i|\widetilde i\rangle$. For a mixed input $\rho$, it is $V\rho V^\dagger$. No step of the encoding depends on the coefficients or eigenvectors of the input.

**Checkpoint 1.** Is $V$ unitary?

**Answer.** It is an isometry from a three-dimensional space to a 27-dimensional one. Thus $V^\dagger V=I_3$, but $VV^\dagger=P\ne I_{27}$. It can be implemented by a unitary on a larger input including prepared auxiliary systems; it is not a square unitary by itself.

## 3. Every individual share forgets the logical state

To establish this for every input, it is enough to calculate the channel on all matrix units $|i\rangle\langle j|$. Diagonal units test populations; off-diagonal units test coherences. Omitting the second group would repeat the mistake of the repetition-code argument.

For the first share,
$$
\begin{aligned}
\operatorname{Tr}_{23}
|\widetilde i\rangle\langle\widetilde j|
&=\frac13\sum_{r,s}
|r\rangle\langle s|\,
\langle s+j|r+i\rangle\,
\langle s+2j|r+2i\rangle.
\end{aligned}
$$
The two inner products require
$$
r+i=s+j,\qquad r+2i=s+2j.
$$
Subtracting gives $i=j$, and either equation then gives $r=s$. Hence
$$
\boxed{
\operatorname{Tr}_{23}
|\widetilde i\rangle\langle\widetilde j|
=\delta_{ij}\frac{I_1}{3}.
}
$$
For an arbitrary logical density matrix $\rho=\sum_{ij}\rho_{ij}|i\rangle\langle j|$,
$$
\rho_1
=\sum_{ij}\rho_{ij}\delta_{ij}\frac{I_1}{3}
=\frac{I_1}{3}.
$$
The final step uses $\operatorname{Tr}\rho=1$.

The code is invariant under cyclic permutations of the three shares. To check this directly, write
$$
(r,\ r+i,\ r+2i)\longmapsto
(r+i,\ r+2i,\ r)
$$
and relabel $r'=r+i$. The result is again $(r',r'+i,r'+2i)$. Therefore
$$
\rho_1=\rho_2=\rho_3=I_3/3
$$
for every encoded input.

**Exact calculation.** Each single-share channel is the constant channel $\rho\mapsto I_3/3$. This is equality of states on the entire single-share algebra.

### 3.1 What this says about an arbitrary local operator

For an operator $x_1$ on share 1,
$$
\begin{aligned}
\langle\widetilde j|x_1\otimes I_{23}|\widetilde i\rangle
&=\operatorname{Tr}\left(
x_1\,\operatorname{Tr}_{23}
|\widetilde i\rangle\langle\widetilde j|
\right)\\
&=\delta_{ij}\frac{\operatorname{Tr}x_1}{3}.
\end{aligned}
$$
Thus
$$
V^\dagger(x_1\otimes I_{23})V
=\frac{\operatorname{Tr}x_1}{3}I_{\mathrm{code}}.
$$
Compression of every one-share operator is scalar on the code. This does **not** say that the physical operator preserves the code: it can send vectors partly or entirely outside it. It says that no measurement on this one share distinguishes logical states.

**Checkpoint 2.** Why did we compute $\operatorname{Tr}_{23}|\widetilde i\rangle\langle\widetilde j|$ for $i\ne j$?

**Answer.** Equal marginals for three encoded basis states would not rule out a dependence on the phases of a superposition. Vanishing off-diagonal reductions establishes independence from every coherence as well.

## 4. Two shares recover the entire state

Now lose share 3 and retain shares 1 and 2. We will exhibit a unitary decoder on those two shares.

For physical basis labels $a,b$, define
$$
D_{12}|a,b\rangle
=|b-a,\ 2b-a\rangle.
$$
This is a permutation of the nine basis states. Indeed, given output labels $u,v$, the input is
$$
a=v-2u,\qquad b=v-u.
$$
All equations are modulo three. Therefore the map is invertible and $D_{12}$ is unitary.

Apply it to the first two entries of an encoded term:
$$
D_{12}|r,r+i\rangle
=|i,r+2i\rangle.
$$
The complete transformed codeword is
$$
\begin{aligned}
(D_{12}\otimes I_3)|\widetilde i\rangle
&=\frac1{\sqrt3}\sum_r
|i\rangle_1|r+2i\rangle_2|r+2i\rangle_3\\
&=|i\rangle_1\otimes|\Phi_3\rangle_{23},
\end{aligned}
$$
where
$$
|\Phi_3\rangle_{23}
=\frac1{\sqrt3}\sum_{s=0}^{2}|s,s\rangle.
$$
The second line relabels the summation variable $s=r+2i$. The auxiliary entangled state is the same for all logical labels.

By linearity,
$$
\boxed{
(D_{12}\otimes I_3)V|\psi\rangle
=|\psi\rangle_1\otimes|\Phi_3\rangle_{23}.
}
$$
The unknown input has become a separate output factor. This identity is the recovery proof.

### 4.1 Recovery after the erasure has already occurred

Since the decoder acts only on the surviving shares, it does not require access to share 3. Taking its trace in the preceding identity gives
$$
D_{12}\rho_{12}D_{12}^\dagger
=\rho\otimes\frac{I_2}{3}.
$$
Discard the second output register to obtain
$$
\mathcal R_{12}(\rho_{12})
=\operatorname{Tr}_2
\bigl(D_{12}\rho_{12}D_{12}^\dagger\bigr)
=\rho.
$$
The subscript on $I_2$ labels share 2; its dimension is three. The equality holds for all mixed logical states as well as pure inputs.

### 4.2 The other surviving pairs

Cyclic symmetry gives the other decoders. On ordered pairs $(2,3)$ and $(3,1)$ use the same rule
$$
|a,b\rangle\longmapsto|b-a,2b-a\rangle.
$$
For $(2,3)$, the first output is $(r+2i)-(r+i)=i$ and the second is $r$, which matches the remaining share 1. For $(3,1)$, the first output is $r-(r+2i)=-2i=i$ and the second matches share 2 after the same arithmetic. Each pair yields the logical qutrit and an auxiliary register.

We have thus corrected the erasure of any **known** single share. The location of the loss tells us which decoder to apply.

> **Physical picture.** Each physical share is individually maximally mixed, but the pair contains more than its two marginals. The decoder rearranges the pair's correlations into an explicit logical register and a fixed auxiliary state. Recoverability is a statement about that rearrangement, not about finding a physical share that already contains the input.

**Worked input.** If $|\psi\rangle=(|0\rangle+i|2\rangle)/\sqrt2$, the encoded vector is $(|\widetilde0\rangle+i|\widetilde2\rangle)/\sqrt2$. After decoding shares 1 and 2 it becomes
$$
\frac{|0\rangle+i|2\rangle}{\sqrt2}
\otimes|\Phi_3\rangle.
$$
The relative phase $i$ survives. The same phase would be lost after a single erasure in the repetition construction of Section 1.

## 5. Reconstructing observables in different regions

Recovery of the state implies that every logical observable has a representative on a surviving pair. Let $O$ act on the logical qutrit and define
$$
O_{12}
=D_{12}^\dagger(O\otimes I_2)D_{12}.
$$
Using the decoder identity,
$$
(O_{12}\otimes I_3)V=VO.
$$
This **intertwining identity** says that applying the physical representative to an encoded state has exactly the same effect as applying the logical operator before encoding.

Cyclic decoders define $O_{23}$ and $O_{31}$ with the same property. They need not be equal on the full physical Hilbert space. Their actions agree on every vector in the specified code.

### 5.1 Two operators that can be checked by inspection

Write $\zeta=e^{2\pi i/3}$ and define logical qutrit operators
$$
X|i\rangle=|i+1\rangle,\qquad
Z|i\rangle=\zeta^i|i\rangle.
$$
They obey $ZX=\zeta XZ$. A representative of $Z$ on shares 1 and 2 is
$$
Z_{12}=Z_1^{-1}Z_2.
$$
On a codeword term its phase is $\zeta^{-r}\zeta^{r+i}=\zeta^i$, independent of $r$. Thus $Z_{12}|\widetilde i\rangle=\zeta^i|\widetilde i\rangle$.

A representative of $X$ is
$$
X_{12}=X_1X_2^2.
$$
It changes a term to
$$
|r+1,\ r+i+2,\ r+2i\rangle.
$$
Setting $r'=r+1$ rewrites this as $|r',r'+(i+1),r'+2(i+1)\rangle$. Therefore $X_{12}|\widetilde i\rangle=|\widetilde{i+1}\rangle$.

The other pair representatives are
$$
\begin{aligned}
Z_{23}&=Z_2^{-1}Z_3,& X_{23}&=X_2X_3^2,\\
Z_{31}&=Z_3^{-1}Z_1,& X_{31}&=X_3X_1^2.
\end{aligned}
$$
These explicit formulas make the freedom of representation visible. For example, $Z_{12}$ and $Z_{23}$ act differently on $|100\rangle$, which lies outside the code, but agree on every encoded state.

### 5.2 Why two disjoint regions cannot both hold a full logical algebra

The three authorized pairs overlap. Suppose instead that two disjoint regions reconstructed all logical operators. Choose logical operators $X$ and $Z$ with $[X,Z]\ne0$. Their disjoint physical representatives would commute, so
$$
[X_A,Z_B]V=V[X,Z]=0.
$$
Since $V$ is an isometry, this would imply $[X,Z]=0$, a contradiction.

This argument uses reconstruction as an intertwining relation, not merely matching expectations in one state. A commuting subalgebra can be shared by disjoint regions; a full noncommutative matrix algebra cannot be reconstructed on both in this way. The distinction will explain why central information can be shared in Lecture 4.

## 6. A reference system tests genuine quantum recovery

An unknown input may be entangled with a reference $R_0$ that we cannot control. Write a general pure reference/input state as
$$
|\Psi\rangle_{R_0a}
=\sum_i|u_i\rangle_{R_0}|i\rangle_a.
$$
The vectors $|u_i\rangle$ need not be orthogonal or normalized separately. Encoding and then decoding gives
$$
\begin{aligned}
(I_{R_0}\otimes D_{12}\otimes I_3)
(I_{R_0}\otimes V)|\Psi\rangle
&=\sum_i|u_i\rangle|i\rangle_1
\otimes|\Phi_3\rangle_{23}\\
&=|\Psi\rangle_{R_01}\otimes|\Phi_3\rangle_{23}.
\end{aligned}
$$
The original reference/input entanglement is restored. This is a stronger check than recovering a selection of isolated states.

The one-share result also implies decoupling from the reference. Applying the matrix-unit identity of Section 3 yields
$$
\rho_{R_03}=\rho_{R_0}\otimes\frac{I_3}{3}.
$$
The erased share has no correlation with the reference that records the logical input. Our explicit decoder shows how the complementary pair retains that input.

**Checkpoint 3.** Are identical one-share marginals for a few tested input states sufficient to establish quantum recovery?

**Answer.** No. One must control the whole input operator space or prove a recovery identity on the full code. The matrix-unit calculation and the reference-system calculation do so here.

## 7. No-cloning and the meaning of an erasure

The decoder can be applied to shares 1 and 2, or to shares 2 and 3. This does not produce two independently accessible copies. The operations share a physical subsystem and need not preserve the alternative encoding structure after one has been used.

For comparison, a hypothetical universal cloning isometry would satisfy
$$
U|\psi\rangle|0\rangle=|\psi\rangle|\psi\rangle.
$$
Preservation of inner products would then require
$$
\langle\phi|\psi\rangle
=\langle\phi|\psi\rangle^2
$$
for all normalized inputs. For an overlap strictly between zero and one, this is impossible. The three-qutrit code instead stores a single logical system with several ways of accessing it.

There is also an important distinction between a known erasure and an arbitrary unknown error. Our decoder knows which share is missing. If a surviving qutrit has also been changed by an unknown operation, the displayed recovery identity no longer applies. The code does not correct every unknown single-qutrit error.

An elementary obstruction follows from $X_1X_2^2V=VX$. Put $E_1=X_1^{-1}$ and $E_2=X_2^2$. Both are single-share errors, and
$$
E_2V=E_1VX.
$$
Consequently $E_2V|0\rangle=E_1V|1\rangle$: the same corrupted physical vector can arise from logical input $|0\rangle$ with error $E_2$, or input $|1\rangle$ with error $E_1$. A decoder that is not told which error occurred would have to send that one vector to two different recovered states. This is impossible. The obstruction does not require a general error-correction theorem; it uses the reconstruction identity we already checked.

## 8. Optional calculation: entropy before and after decoding

Let $S(\rho)=-\operatorname{Tr}\rho\log\rho$, using natural logarithms and $0\log0=0$. If $\lambda_k$ are the logical eigenvalues, the decoded pair $\rho\otimes I_3/3$ has eigenvalues $\lambda_k/3$, each repeated three times. Therefore
$$
\begin{aligned}
S(\rho_{12})
&=-\sum_k3\frac{\lambda_k}{3}
\log\frac{\lambda_k}{3}\\
&=S(\rho)+\log3.
\end{aligned}
$$
Unitary decoding does not change these eigenvalues. Each individual share has entropy $\log3$, while the full encoded state has entropy $S(\rho)$ because an isometry preserves the nonzero spectrum:
$$
S(\rho_1)=\log3,\qquad
S(\rho_{12})=S(\rho)+\log3,\qquad
S(V\rho V^\dagger)=S(\rho).
$$
For a pure logical input, the pair entropy is $\log3$. For a maximally mixed input, it is $2\log3$. The extra $\log3$ comes from the fixed auxiliary entanglement exposed by the decoder.

This is the first entropy formula we will later compare with an area term. It is an exact identity for this code. There is no geometrical surface in its derivation.

For completeness, the mutual information between shares 1 and 2 is
$$
I(1:2)=S(\rho_1)+S(\rho_2)-S(\rho_{12})
=\log3-S(\rho).
$$
It is largest for pure logical inputs and vanishes for the maximally mixed logical input. Reconstruction still works in the latter case: the recovery channel is defined on all inputs, including their correlations with a reference.

## 9. What the holographic analogy captures

The code suggests a useful dictionary:

| Exact object in this model | Role in the holographic comparison |
|---|---|
| Logical qutrit | One effective bulk degree of freedom |
| Three physical shares | Boundary degrees of freedom |
| Authorized pair | A boundary region able to reconstruct that degree of freedom |
| Logical operator | An effective bulk observable |
| Different pair representatives | Different boundary reconstructions on the same code |
| Fixed auxiliary entropy | A precursor of an area-like contribution |

**Formal analogy.** This dictionary organizes a comparison; it does not establish AdS/CFT. The code has no AdS metric, local field dynamics, continuum limit, or Einstein equation. It does not select which quantum field theories possess a semiclassical gravitational dual.

Nor does it define a full pattern of entanglement wedges for many bulk regions. It has only one logical site. A tensor network can supply a richer pattern of encodings, while additional dynamical and geometric assumptions remain to be examined.

The result we should carry forward is precise: a logical observable can have several physical reconstructions that agree on a code, and the sets supporting them can overlap without violating no-cloning.

## 10. What to take away

- The encoding is an isometry into a proper subspace of the physical Hilbert space.
- Every single-share channel is constant on the entire logical operator space.
- The explicit two-share decoder recovers every input, including its entanglement with a reference.
- Operator reconstruction is equality of actions on a specified code subspace.
- Overlapping recovery regions are compatible with no-cloning; disjoint recovery of a full noncommutative algebra is not.
- The entropy identity is exact within the model and does not itself give a spacetime geometry.

The next lecture changes the question. We will keep a bipartite state fixed and ask what algebraic structure is determined by that state together with the observables on one side. This leads to modular theory through a calculation with Schmidt coefficients.

## 11. Problem set

### Classroom core

**1. Isometry and phase information.** Verify $V^\dagger V=I$ from the displayed codewords. Explain why checking only the three diagonal reductions is insufficient to prove that one share has no logical information.

**2. Decode a known basis input.** Apply $D_{12}$ term by term to $|\widetilde1\rangle$. Check that the result is $|1\rangle\otimes|\Phi_3\rangle$. Find the input basis pair that maps to output $|2,1\rangle$.

**3. Recover a logical observable.** Check that $Z_2^{-1}Z_3$ reconstructs $Z$. Find the commutation relation of $Z_{12}$ and $X_{12}$.

**4. Entropy of a mixed input.** Take $\rho=\operatorname{diag}(1/2,1/3,1/6)$. List all nine eigenvalues of $\rho_{12}$ and compute its entropy in terms of $S(\rho)$.

### Self-study consolidation

**5. Reference correlations.** Start with the maximally entangled logical/reference state $3^{-1/2}\sum_i|i\rangle_{R_0}|i\rangle_a$. Show that $I(R_0:1)=0$ and $I(R_0:12)=2\log3$ after encoding.

**6. Outside the code.** Evaluate $Z_{12}$ and $Z_{23}$ on $|100\rangle$. Explain why the results do not contradict reconstruction.

**7. Repetition versus the qutrit code.** For each encoding, compare the outputs after erasing one share for two inputs differing only by a relative phase. Identify the matrix-unit calculation that makes the difference.

### Research extension

**8. Imperfect access.** Replace the perfect pair output by
$$
\mathcal N_\eta(\rho_{12})
=(1-\eta)\rho_{12}+\eta I_{12}/9,
\qquad 0\le\eta\le1.
$$
Apply the same decoder and compute the resulting logical channel. Determine its fidelity on a pure input. Completion means an exact expression for this specified noise model, not a general theorem about approximate holographic reconstruction.

## 12. Answer checkpoints

**1.** Distinct codewords contain disjoint basis strings, and each has three equal-amplitude terms. Thus they are orthonormal. Off-diagonal reductions control the output of input coherences; without them, a superposition could still be distinguishable on one share.

**2.** The pairs $(0,1),(1,2),(2,0)$ map to $(1,2),(1,0),(1,1)$, respectively. The untouched third labels are $2,0,1$, so the last two registers form $|\Phi_3\rangle$. For output $(u,v)=(2,1)$, the inverse gives $(a,b)=(0,2)$ modulo three.

**3.** Each term acquires $\zeta^{-(r+i)+(r+2i)}=\zeta^i$. The two-share Weyl operators satisfy $Z_{12}X_{12}=\zeta X_{12}Z_{12}$, since the phase is $\zeta^{-1+2}=\zeta$.

**4.** The eigenvalues are $1/6$ three times, $1/9$ three times, and $1/18$ three times. Their sum is one and their entropy is $S(\rho)+\log3$.

**5.** The state on $R_01$ is $(I_{R_0}/3)\otimes(I_1/3)$, giving zero mutual information. After decoding 12, the state on $R_0$ and the recovered register is pure maximally entangled, while the second decoded register is $I_3/3$. Thus $S(R_0)=\log3$, $S(12)=2\log3$, and $S(R_012)=\log3$, giving $I(R_0:12)=2\log3$.

**6.** $Z_{12}|100\rangle=\zeta^{-1}|100\rangle$ and $Z_{23}|100\rangle=|100\rangle$. Reconstruction equates their actions only on $V\mathcal H_{\mathrm{code}}$, and $|100\rangle$ is outside that space.

**7.** Repetition erases $|000\rangle\langle111|$ and therefore the relative phase. In the qutrit encoding the lost share contains no logical information, and the explicit pair decoder retains every logical matrix unit. Vanishing one-share coherences is compatible with surviving pair coherences.

**8.** A unitary leaves $I_{12}/9$ invariant. After decoding and discarding the auxiliary register,
$$
\rho\longmapsto(1-\eta)\rho+\eta I_3/3.
$$
For a pure input $|\psi\rangle$, the overlap fidelity $\langle\psi|\rho_{\mathrm{out}}|\psi\rangle$ is $1-2\eta/3$. This formula concerns the stated depolarizing mixture.

---

Previous: [[lecture-01-observables-and-restricted-access|Lecture 1]]. Next: [[lecture-03-modular-structure|Lecture 3 — Modular structure]]. Return to the [[courses/ads-cft-course/syllabus|course route]].

**Wiki connections.** [[subregion-subalgebra-duality|subregion–subalgebra duality]] · [[holographic-dictionary|holographic dictionary]]
