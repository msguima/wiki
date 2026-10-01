---
title: "Lecture 1 — Observables and restricted access"
type: lecture-notes
course: syllabus
edition: "2.0"
semester: 1
week: 1
lecture: 1
duration: "2 hours; additional self-study material"
status: written — checked in the scope of the validation record
modified: 2026-09-28
---

# Lecture 1 — Observables and restricted access

Suppose two laboratories receive parts of a quantum system. The complete system has been prepared in one of two orthogonal states, so a suitable measurement can distinguish the preparations perfectly. Yet the observer in either laboratory, working alone, obtains exactly the same statistics in the two cases. Where is the distinction stored?

This question is already meaningful for two qubits. It is also a useful starting point for holography: before discussing how a boundary region reconstructs part of a bulk spacetime, we must understand how information can be present in a system and absent from the observables available to a particular observer. We will turn that statement into a calculation and then into a definition.

## How to use this lecture

**Classroom core, 120 minutes.** Work through the Bell-state experiment and partial trace in Sections 1–2 (35 minutes), observables and state restriction in Sections 3–4 (30 minutes), no-signaling in Section 5 (20 minutes), and the concrete commutant/center examples in Section 6 (20 minutes). Reserve 15 minutes for the checkpoints and a recap. These are proposed allocations, not a measured teaching time.

**Self-study.** Read all sections. Write out at least one partial trace as a sum over basis indices. Derive the commutant using the optional calculation in Section 7. Complete Problems 1–6 and compare with the answer checkpoints.

**Research extension.** Section 8 explains which definitions survive in QFT and which tensor-product constructions require additional hypotheses. The extension is orientation; no classification theorem is needed for the calculations here.

**Prerequisites.** Vectors, tensor products, Hermitian matrices, Born probabilities, and density matrices. We recall the required probability interpretation as we use it.

**Reading.** The lecture is self-contained. For the later algebraic perspective, see Witten, [arXiv:1803.04993](https://arxiv.org/abs/1803.04993), especially the finite-system discussion, and Harlow, [arXiv:1607.03901](https://arxiv.org/abs/1607.03901), Appendix A. The [[opening-block-reading-map|reading map]] explains their roles.

**What this lecture establishes.** All calculations through Section 7 concern finite-dimensional quantum systems and are exact. The final QFT discussion states the boundary of this model; it does not derive the type of a continuum local algebra.

## 1. A distinction that one observer cannot see

Let Alice possess a qubit $A$ and Bob a qubit $B$. Their joint Hilbert space is
$$
\mathcal H_{AB}=\mathbb C^2\otimes\mathbb C^2.
$$
The four basis vectors are $|00\rangle,|01\rangle,|10\rangle,|11\rangle$, with Alice's label first. Consider the two preparations
$$
|\Phi_+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},
\qquad
|\Phi_-\rangle=\frac{|00\rangle-|11\rangle}{\sqrt2}.
$$
They are orthogonal:
$$
\langle\Phi_+|\Phi_-\rangle=\frac{1-1}{2}=0.
$$
A measurement with projectors onto these two vectors can therefore distinguish them. The issue is whether Alice can perform such a measurement using only her qubit.

### 1.1 Start with a general local observable

An arbitrary Hermitian qubit observable has the form
$$
x_A=
\begin{pmatrix}
a&b\\
b^*&d
\end{pmatrix},
\qquad a,d\in\mathbb R.
$$
When applied to the complete system, it is $x_A\otimes I_B$. Expanding the expectation value gives
$$
\begin{aligned}
\langle\Phi_\pm|x_A\otimes I_B|\Phi_\pm\rangle
&=\frac12\bigl(
\langle0|x_A|0\rangle+
\langle1|x_A|1\rangle
\bigr)\\
&=\frac{a+d}{2}.
\end{aligned}
$$
The two cross terms vanish because they contain $\langle0|1\rangle_B=0$. The relative sign between $|00\rangle$ and $|11\rangle$ has disappeared from every local expectation value.

The same conclusion holds for all Alice's measurement probabilities. A measurement outcome can be represented by an effect $e_A$, a positive operator with $0\le e_A\le I_A$, and its probability is the expectation of $e_A\otimes I_B$. Since the calculation holds for every such operator, changing the local measurement cannot reveal the preparation.

This is stronger than saying that Alice has chosen an inconvenient basis. It rules out every measurement confined to her system.

### 1.2 A correlation retains the distinction

Define the Pauli matrix
$$
X=|0\rangle\langle1|+|1\rangle\langle0|.
$$
Since $X\otimes X$ exchanges $|00\rangle$ and $|11\rangle$,
$$
(X\otimes X)|\Phi_\pm\rangle=\pm|\Phi_\pm\rangle.
$$
Thus
$$
\langle X_A X_B\rangle_{\Phi_+}=1,\qquad
\langle X_A X_B\rangle_{\Phi_-}=-1.
$$
Alice and Bob can each measure $X$ and later compare their records. The product of their outcomes distinguishes the preparations. Alice's outcome alone remains a uniformly random sign.

> **Physical picture.** The missing information is a relation between records. Alice's apparatus is not defective, and no precision improvement helps her infer the sign from her own outcome. The observable that carries the distinction involves both laboratories. Access to correlations is an additional physical resource.

**Checkpoint 1.** Would measuring $Z_AZ_B$ distinguish the states, where $Z|0\rangle=|0\rangle$ and $Z|1\rangle=-|1\rangle$?

**Answer.** No. Both $|00\rangle$ and $|11\rangle$ have $Z_AZ_B=+1$, so both Bell states give $+1$ with certainty. Some joint observables distinguish the states; joint support by itself does not guarantee that a chosen observable does.

## 2. The partial trace is a record of accessible statistics

The density matrix of a pure state is $|\psi\rangle\langle\psi|$. For a general preparation we use a positive matrix $\rho_{AB}$ with unit trace. Its expectation rule is
$$
\langle x\rangle=\operatorname{Tr}_{AB}(\rho_{AB}x).
$$
We want a smaller matrix that reproduces every expectation value Alice can obtain. This requirement defines the reduced state:
$$
\operatorname{Tr}_{AB}\bigl(\rho_{AB}(x_A\otimes I_B)\bigr)
=\operatorname{Tr}_A(\rho_Ax_A)
\quad\text{for all }x_A.
$$
The phrase “for all” matters. A state is a prescription for all measurement statistics, not just for one chosen observable.

### 2.1 Deriving the formula

Expand the joint matrix in an orthonormal product basis:
$$
\rho_{AB}
=\sum_{i,j,\mu,\nu}\rho_{i\mu,j\nu}
|i\rangle\langle j|\otimes|\mu\rangle\langle\nu|.
$$
Taking the trace against $x_A\otimes I_B$ produces
$$
\operatorname{Tr}_{AB}\bigl(\rho_{AB}(x_A\otimes I_B)\bigr)
=\sum_{i,j,\mu}\rho_{i\mu,j\mu}\langle j|x_A|i\rangle.
$$
This has the desired form if
$$
\boxed{
\rho_A=\operatorname{Tr}_B\rho_{AB}
=\sum_{i,j,\mu}\rho_{i\mu,j\mu}|i\rangle\langle j|.
}
$$
The partial trace contracts Bob's bra and ket indices. It does not sum Alice's indices or delete entries according to whether a state looks entangled.

We can check the properties needed for a state. Its trace is
$$
\operatorname{Tr}_A\rho_A
=\sum_{i,\mu}\rho_{i\mu,i\mu}=1.
$$
For any vector $|v\rangle_A$,
$$
\langle v|\rho_A|v\rangle
=\sum_\mu\langle v,\mu|\rho_{AB}|v,\mu\rangle\ge0,
$$
so $\rho_A$ is positive. These two facts establish that the construction gives a valid density matrix.

### 2.2 Applying it to the Bell states

The joint matrices are
$$
\rho_{AB}^{\pm}
=\frac12\bigl(
|00\rangle\langle00|+
|11\rangle\langle11|
\pm|00\rangle\langle11|
\pm|11\rangle\langle00|
\bigr).
$$
For an elementary product,
$$
\operatorname{Tr}_B
\bigl(|i,\mu\rangle\langle j,\nu|\bigr)
=\delta_{\mu\nu}|i\rangle\langle j|.
$$
The cross terms therefore vanish and
$$
\rho_A^+=\rho_A^-=\frac12
\bigl(|0\rangle\langle0|+|1\rangle\langle1|\bigr)
=\frac{I_A}{2}.
$$
We have recovered the result of Section 1 in a form that will apply to much larger systems.

### 2.3 Restricted access and uncertainty about preparation

The globally pure Bell state and the mixed preparation
$$
\rho_{\mathrm{mix}}
=\frac12|00\rangle\langle00|
+\frac12|11\rangle\langle11|
$$
have the same reduced states. They differ on joint observables: $\langle X_AX_B\rangle_{\mathrm{mix}}=0$, whereas the Bell values are $\pm1$.

Thus a mixed reduced state does not tell Alice whether the complete preparation was mixed. It expresses the statistics available at her level of access. The interpretation of the global state requires more information.

**Checkpoint 2.** Suppose Alice can measure every qubit observable and finds $\rho_A=I_A/2$. Has she demonstrated that her qubit is entangled with Bob's?

**Answer.** No. The product state $(I_A/2)\otimes(I_B/2)$ has the same local statistics. Entanglement is a statement about the joint state and the specified division into systems.

## 3. From a list of measurements to an algebra

For Alice's laboratory, the operators we have been using form
$$
\mathcal M_A=\mathcal B(\mathcal H_A)\otimes I_B.
$$
Here $\mathcal B(\mathcal H_A)$ is simply the set of all matrices on $\mathcal H_A$. The tensor factor $I_B$ expresses the restriction on access.

We retain complex matrices, not only Hermitian ones. Every complex matrix decomposes as
$$
x=\frac{x+x^\dagger}{2}
+i\frac{x-x^\dagger}{2i},
$$
so knowing expectations of Hermitian observables determines the expectation of every matrix. Complex matrices also include transition operators such as $|0\rangle\langle1|$, which simplify calculations.

A unital $*$-algebra is a collection closed under linear combinations, products, and adjoints, and containing the identity. In finite dimensions these requirements are enough for our purposes. We are not yet introducing norm completions or the analytic definition of a von Neumann algebra.

Why keep products? They preserve the composition structure of operations and the relations between observables. A list containing $X$ and $Z$ but excluding their product would omit information about how those operators fit together. The product of noncommuting observables need not itself be a Hermitian observable, and its expectation is not automatically the statistics of a sequential measurement. An actual measurement sequence also requires a specification of state disturbance.

### 3.1 A state as an expectation functional

Instead of identifying a state with a particular density matrix, define the map
$$
\omega_\rho(x)=\operatorname{Tr}(\rho x).
$$
It is linear and satisfies
$$
\omega_\rho(I)=1,\qquad
\omega_\rho(x^\dagger x)\ge0.
$$
The first property normalizes probabilities. The second gives positivity for positive measurement effects.

We call any normalized positive linear functional on the specified algebra a **state**. In the finite matrix examples it can be represented by a density matrix. The functional language makes explicit which observables the state is being asked to evaluate.

### 3.2 Restricting a state

If only $\mathcal M_A$ is accessible, the available state is the restricted functional
$$
\omega_A=\omega_\rho|_{\mathcal M_A}.
$$
The partial-trace identity says that $\rho_A$ represents this functional on Alice's matrix algebra. The restriction is the conceptual operation; the partial trace is its convenient implementation for the tensor-product system at hand.

> **Physical picture.** Think of a state as a book of predicted answers to measurement questions. Choosing an accessible algebra specifies which questions may be asked. Restriction keeps those answers. It does not assert that inaccessible correlations have physically disappeared.

This distinction will matter in Lecture 2. There, a logical state can be recovered from certain sets of physical systems even though it is absent from the statistics of every individual system.

## 4. Operationally indistinguishable states

Two states $\rho$ and $\sigma$ are indistinguishable on an accessible algebra $\mathcal M$ when
$$
\omega_\rho(x)=\omega_\sigma(x)
\qquad\text{for every }x\in\mathcal M.
$$
Equivalently, their restrictions to $\mathcal M$ are equal. For Alice's full qubit algebra this is precisely $\rho_A=\sigma_A$.

**Model proof.** Equality of reduced states immediately gives equality of all local expectations. Conversely, if all local expectations agree, test with the Hermitian combinations of matrix units $E_{ij}+E_{ji}$ and $i(E_{ij}-E_{ji})$, and with $E_{ii}$. These determine every matrix entry, so the reduced matrices must agree.

### 4.1 Restricted access can occur within one qubit

Suppose an apparatus can only resolve the computational basis. Its algebra is
$$
\mathcal D=\{a|0\rangle\langle0|+b|1\rangle\langle1|:
a,b\in\mathbb C\}.
$$
For
$$
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad
|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2},
$$
we obtain
$$
\langle+|d|+\rangle=\langle-|d|-\rangle=\frac{a+b}{2}
\quad(d\in\mathcal D).
$$
The two states become distinguishable as soon as $X$ is available. No second physical system was needed to create restricted access.

This is one reason the algebraic language is broader than a tensor-factor description. The accessible information may be limited by the observables one controls, not only by the spatial location of a subsystem.

### 4.2 A classical comparison

Two classical probability distributions on a pair of bits can agree on each individual bit and disagree on their correlation. For example,
$$
p(00)=p(11)=\frac12,\qquad
q(01)=q(10)=\frac12
$$
have uniform single-bit marginals. A joint parity measurement distinguishes them.

This analogy explains why matching marginals is compatible with different joint states. Quantum theory adds another feature: the observables needed to access different aspects of a state may fail to commute. In the Bell example, the off-diagonal coherence is visible in the $X_AX_B$ correlation. A classical mixture with the same $Z$-basis probabilities does not retain it.

**Checkpoint 3.** Can the state on $\mathcal D$ distinguish the pure vector $|+\rangle$ from the mixed matrix $I/2$?

**Answer.** No. Both assign probability $1/2$ to each computational-basis outcome. Purity of a global preparation and purity of its restriction to a smaller algebra are different questions.

## 5. Correlations do not provide a signaling channel

Bob can alter correlations and can condition states on his measurement outcomes. Neither fact lets him alter Alice's unconditioned statistics by a local trace-preserving operation.

To see this without a verbal argument, represent Bob's operation by matrices $B_\mu$ satisfying
$$
\sum_\mu B_\mu^\dagger B_\mu=I_B.
$$
The resulting joint state, when Bob's outcome is not selected, is
$$
\rho'_{AB}
=\sum_\mu(I_A\otimes B_\mu)\rho_{AB}
(I_A\otimes B_\mu^\dagger).
$$
Such a map is a completely positive trace-preserving quantum channel. For this calculation, the displayed representation and completeness relation are all we need.

For any Alice observable,
$$
\begin{aligned}
\operatorname{Tr}\bigl(\rho'_{AB}(x_A\otimes I_B)\bigr)
&=\sum_\mu\operatorname{Tr}\bigl(
\rho_{AB}(x_A\otimes B_\mu^\dagger B_\mu)
\bigr)\\
&=\operatorname{Tr}\bigl(\rho_{AB}(x_A\otimes I_B)\bigr).
\end{aligned}
$$
The first step uses cyclicity of the full trace and commutation between operators on separate factors. The second uses completeness. Therefore $\rho'_A=\rho_A$.

**Model proof.** This proves no-signaling for unconditioned local channels in the finite tensor-product setting. It does not assume that the initial state is separable.

### 5.1 Conditioning is a different operation

If Bob measures $Z$ on $|\Phi_+\rangle$, outcome $0$ leaves Alice in $|0\rangle$ and outcome $1$ leaves her in $|1\rangle$. Each outcome occurs with probability $1/2$. Before learning which outcome occurred, Alice must average:
$$
\frac12|0\rangle\langle0|+\frac12|1\rangle\langle1|
=\frac{I_A}{2}.
$$
The selected outcome corresponds to a map that is not trace preserving; its trace is the probability of that outcome. Normalizing the selected state is conditional probability. Bob must communicate the record if Alice is to know which conditional ensemble describes her data.

> **Physical picture.** Correlation permits predictions conditioned on another record. Signaling requires control over a change in the receiver's unconditioned statistics. The trace-preserving calculation separates these two statements. The same distinction will be needed when entanglement and wormholes appear in the later course.

## 6. Commutants and centers, with small matrices

We need two pieces of algebraic vocabulary before the later encoding examples.

The **commutant** of $\mathcal M$ in $\mathcal B(\mathcal H)$ is
$$
\mathcal M'
=\{y\in\mathcal B(\mathcal H):yx=xy
\text{ for every }x\in\mathcal M\}.
$$
It contains the operators compatible, in the commutation sense, with all of $\mathcal M$. It does not by definition specify an independent laboratory.

For a tensor-product system,
$$
\bigl(\mathcal B(\mathcal H_A)\otimes I_B\bigr)'
=I_A\otimes\mathcal B(\mathcal H_B).
$$
One inclusion follows immediately because different tensor factors commute. Section 7 proves the converse. In this example the commutant coincides with Bob's full algebra.

The **center** is the part of an algebra that commutes with the whole algebra:
$$
Z(\mathcal M)=\mathcal M\cap\mathcal M'.
$$
For a full matrix algebra, its only central matrices are scalar multiples of the identity. An algebra with this property is called a **factor**.

For the diagonal qubit algebra $\mathcal D$, every element commutes with every other element. Moreover, within $M_2(\mathbb C)$ its commutant is itself. Thus
$$
\mathcal D'=\mathcal D,\qquad Z(\mathcal D)=\mathcal D.
$$
This algebra describes one classical two-outcome variable. In Lecture 4 we will encounter algebras with classical sector labels and quantum matrices inside each sector.

| Accessible algebra and ambient space | Commutant | Center | Information described |
|---|---|---|---|
| $M_2(\mathbb C)$ in $M_2(\mathbb C)$ | $\mathbb C I$ | $\mathbb C I$ | All qubit observables |
| $\mathcal D$ in $M_2(\mathbb C)$ | $\mathcal D$ | $\mathcal D$ | A classical computational-basis label |
| $M_2(\mathbb C)\otimes I$ in $M_4(\mathbb C)$ | $I\otimes M_2(\mathbb C)$ | $\mathbb C I$ | All observables of one of two qubits |

**Checkpoint 4.** Does a trivial center mean that a state is pure or unentangled?

**Answer.** No. The center is a property of the algebra. The same factor $M_2(\mathbb C)$ admits pure states, mixed states, and restrictions of entangled bipartite states.

## 7. Optional derivation: the tensor-factor commutant

Let $E_{ij}=|i\rangle\langle j|$ be matrix units on $A$. Any operator on $AB$ can be written
$$
Y=\sum_{i,j}E_{ij}\otimes Y_{ij},
$$
where $Y_{ij}$ acts on $B$.

Suppose $Y$ commutes with every $E_{kk}\otimes I_B$. Multiplication by $E_{kk}$ from the left selects row $k$, while multiplication from the right selects column $k$. Equality forces $Y_{ij}=0$ whenever $i\ne j$. Hence
$$
Y=\sum_iE_{ii}\otimes Y_i.
$$
Now require commutation with $E_{kl}\otimes I_B$. The products are
$$
Y(E_{kl}\otimes I_B)=E_{kl}\otimes Y_k,
\qquad
(E_{kl}\otimes I_B)Y=E_{kl}\otimes Y_l.
$$
Thus $Y_k=Y_l$ for all $k,l$, and
$$
Y=I_A\otimes Y_B.
$$
This proves the claimed commutant formula. The calculation also shows why the ambient space must be specified. In the full two-qubit space Alice's commutant is large; inside Alice's own full matrix algebra it contains only scalars.

## 8. What survives when we move toward QFT?

The definitions of an algebra, a state, a restriction, a commutant, and a center do not depend on writing a Hilbert space as a spatial tensor product. That is the useful part of today's construction for QFT.

The partial-trace representation did depend on such a product and on a trace on the local matrix algebra. In broad classes of continuum relativistic QFT, local algebras are type III under the relevant hypotheses. They do not carry a nonzero normal semifinite trace. Consequently there is no intrinsic local density matrix relative to such a trace. The restricted state still exists as a positive functional.

This does not deny that a global vector can be written as a rank-one density operator on its ambient Hilbert space. The claim concerns the local algebra and a putative local trace. Keeping those objects distinct avoids an apparent contradiction.

We will approach the continuum through controlled examples later. Today we do not classify any infinite algebra. Every algebra actually constructed in this lecture is finite dimensional.

**Stated only — source and scope.** Witten's [QFT entanglement notes](https://arxiv.org/abs/1803.04993) explain the local-algebra problem and its modular formulation. Type III is not a synonym for holography, and finite $N$ in a gauge theory is not a spatial ultraviolet regulator.

There is also no holographic duality hidden in the Bell example. It establishes restricted distinguishability and the role of joint observables. A theory of spatial regions, dynamics, and a bulk/boundary map remains to be supplied.

## 9. What to take away

- A reduced state is characterized by the complete statistics of the accessible observables.
- Two different global states may have identical restrictions to an algebra.
- Restriction to an algebra includes ordinary partial traces but can also describe restricted access within one physical system.
- Local trace-preserving operations leave the other system's unconditioned statistics unchanged.
- A commutant depends on the ambient algebra; a center describes observables commuting with the whole accessible algebra.
- These are exact finite-system statements. Their eventual QFT and gravitational uses require further input.

The next lecture turns the first observation into a construction. We will encode an unknown qutrit so that each individual share has exactly the same reduced state for every input, while any pair of shares can recover that input.

## 10. Problem set

### Classroom core

**1. All Bell states.** For $|\Psi_\pm\rangle=(|01\rangle\pm|10\rangle)/\sqrt2$, calculate both reduced states and the expectations of $X_AX_B$ and $Z_AZ_B$. Which two commuting joint observables distinguish all four Bell states?

**2. An unequal Schmidt pair.** Let
$$
|\psi_p\rangle=\sqrt p\,|00\rangle+\sqrt{1-p}\,|11\rangle,
\qquad 0\le p\le1.
$$
Find $\rho_A$, $\langle Z_A\rangle$, and $\langle X_AX_B\rangle$. Determine when $\rho_A$ is pure.

**3. Dephasing and records.** Bob applies the two-outcome channel with $B_0=|0\rangle\langle0|$ and $B_1=|1\rangle\langle1|$ to $|\Phi_+\rangle$. Calculate the unconditioned joint state, Alice's reduced state, and the two conditional Alice states.

### Self-study consolidation

**4. Accessible tomography.** Write $\rho=(I+r_xX+r_yY+r_zZ)/2$. Which components can be determined using only $\mathcal D$? Give two different states with the same restriction to $\mathcal D$.

**5. A small commutant.** Write a general complex $2\times2$ matrix and solve $[Y,Z]=0$. Then impose $[Y,X]=0$ as well. Compare the answers with the second and first rows of the table in Section 6.

**6. Restricted state versus chosen extension.** Show that the two-qubit matrices $\rho_A\otimes I_B/2$ and $\rho_A\otimes|0\rangle\langle0|_B$ represent the same state on $\mathcal M_A$. Explain why the restricted state does not choose one of these global extensions.

### Research extension

**7. An operational dictionary.** Choose a finite experiment with incomplete access: a two-spin experiment, a dephasing apparatus, or a known-subsystem erasure. Specify the Hilbert space, the accessible algebra, two indistinguishable preparations, and an additional observable that distinguishes them. Completion means an explicit calculation of the relevant probabilities. A claim about a continuum QFT or a gravitational dual is not required.

## 11. Answer checkpoints

**1.** Each reduced state is $I/2$. The ordered pairs $(\langle XX\rangle,\langle ZZ\rangle)$ are $(+1,+1)$ for $\Phi_+$, $(-1,+1)$ for $\Phi_-$, $(+1,-1)$ for $\Psi_+$, and $(-1,-1)$ for $\Psi_-$. The two joint operators commute because the two minus signs from $XZ=-ZX$ cancel. Their joint eigenvalues distinguish the Bell basis.

**2.** The partial trace is $\operatorname{diag}(p,1-p)$, so $\langle Z_A\rangle=2p-1$. Acting with $XX$ exchanges the two terms and gives $\langle XX\rangle=2\sqrt{p(1-p)}$. The reduced state is pure only at $p=0$ or $p=1$.

**3.** The channel removes the cross terms:
$$
\rho'_{AB}=\frac12|00\rangle\langle00|
+\frac12|11\rangle\langle11|.
$$
Alice still has $I/2$. Conditional on Bob's outcome she has $|0\rangle\langle0|$ or $|1\rangle\langle1|$. The record determines the conditioning; the averaged channel does not transmit it.

**4.** The accessible probabilities are $(1+r_z)/2$ and $(1-r_z)/2$. The coefficients $r_x,r_y$ are unavailable. For example, $|+\rangle$ and $|-\rangle$ both have $r_z=0$.

**5.** Commutation with $Z$ sets the two off-diagonal entries of $Y$ to zero. A diagonal $Y=\operatorname{diag}(a,d)$ commutes with $X$ only when $a=d$. Thus the first commutant is $\mathcal D$ and the second is $\mathbb C I$.

**6.** Both give $\operatorname{Tr}(\rho_Ax_A)$ when evaluated on $x_A\otimes I_B$, because both Bob matrices have unit trace. They differ, for example, on Bob's $Z$. Equality on the accessible algebra leaves those additional statistics undetermined.

For Problem 7, verify equality for every generator of the specified algebra and its linear span, not just for a single convenient measurement.

---

Next: [[lecture-02-three-qutrit-code|Lecture 2 — A quantum system hidden in three qutrits]]. Return to the [[courses/ads-cft-course/syllabus|course route]].
