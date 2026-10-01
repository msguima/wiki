---
title: "Lecture 4 — An entropy formula in a quantum code"
type: lecture-notes
course: syllabus
edition: "2.0"
semester: 1
week: 2
lecture: 4
duration: "2 hours; additional self-study material"
status: written — checked in the scope of the validation record
modified: 2026-09-28
---

# Lecture 4 — An entropy formula in a quantum code

The two-share decoder in Lecture 2 exposed a logical state together with an auxiliary state fixed by the encoding. Its entropy was therefore the logical entropy plus a constant. We now generalize that calculation in two steps. First, both sides will contain recoverable logical information. Second, the accessible algebra will have a center, allowing the additional entropy term to depend on a shared classical sector.

The result has the structure of an area term plus bulk entropy. We can derive that structure entirely within quantum mechanics. The calculation then makes a gravitational question precise: what additional input identifies the central term with the area of an extremal surface?

## How to use this lecture

**Classroom core, 120 minutes.** Review the qutrit entropy and construct the complementary code in Sections 1–3 (30 minutes); derive entropy additivity and work the four-qubit example in Sections 4–5 (30); introduce the center through the explicit three-level model in Section 8 (35); finish with the holographic comparison and discussion (25). Section 8 can be taught directly before the general formulas of Section 7.

**Self-study.** Derive the relative-entropy and modular identities in Section 6, then read the general direct-sum construction in Section 7. Verify that its formulas reproduce the three-level example. Work through the trace-convention discussion before interpreting any entropy attached to an algebra.

**Research extension.** Study the general equivalence between complementary recovery and the algebraic entropy formula in Harlow's paper. This lecture constructs and solves a family of codes; it does not prove that every code with the relevant property can be put in this form.

**Prerequisites.** [[lecture-01-observables-and-restricted-access|Lecture 1]] for restriction and centers, [[lecture-02-three-qutrit-code|Lecture 2]] for encoding and reconstruction, and [[lecture-03-modular-structure|Lecture 3]] for logarithms of density matrices.

**Reading.** Harlow, [arXiv:1607.03901](https://arxiv.org/abs/1607.03901), Sections 4–5 and Appendix A, is the primary source for the operator-algebra code structure. Jafferis, Lewkowycz, Maldacena, and Suh, [arXiv:1512.06431](https://arxiv.org/abs/1512.06431), is the later gravitational comparison.

**What this lecture proves.** The entropy, reconstruction, relative-entropy, and compressed modular identities are derived for the explicit finite codes below. Their geometric interpretation is additional input. No gravitational field equation or extremal-surface prescription is derived here.

## 1. What the three-qutrit code has already taught us

The decoder of Lecture 2 gave
$$
D_{12}\rho_{12}D_{12}^\dagger
=\rho\otimes I_3/3.
$$
If the logical eigenvalues are $\lambda_j$, the pair eigenvalues are $\lambda_j/3$ repeated three times. Hence
$$
S(\rho_{12})=S(\rho)+\log3.
$$
The extra term comes from the fixed entanglement between the second decoded register and the erased share. It is present even when the logical input is pure.

That example has only one logical system: the pair recovers all of it, while the remaining share recovers none of it. A spatial division of a bulk would generally leave observables on both sides. We therefore introduce two logical systems and arrange for each physical side to recover one of them.

The guiding calculation remains elementary. Tensor products multiply eigenvalues, direct sums collect distinct blocks, and the logarithm turns those operations into the terms of an entropy formula.

## 2. An explicit code with complementary recovery

Let the logical Hilbert space be
$$
\mathcal H_{\mathrm{code}}=\mathcal H_a\otimes\mathcal H_b.
$$
The physical systems contain additional registers:
$$
\mathcal H_A=\mathcal H_a\otimes\mathcal H_{a'},
\qquad
\mathcal H_B=\mathcal H_b\otimes\mathcal H_{b'}.
$$
The primes label auxiliary registers, not commutants. Choose a fixed normalized entangled vector
$$
|\chi\rangle_{a'b'}
=\sum_{r=1}^{k}\sqrt{\lambda_r}\,|r\rangle_{a'}|r\rangle_{b'},
\qquad \lambda_r>0,\qquad\sum_r\lambda_r=1.
$$
For simplicity, the auxiliary spaces have dimension $k$. The two reduced auxiliary states have the same spectrum:
$$
\chi_{a'}=\sum_r\lambda_r|r\rangle\langle r|,
\qquad
\chi_{b'}=\sum_r\lambda_r|r\rangle\langle r|.
$$
We may also apply arbitrary fixed unitaries $U_A$ and $U_B$ within the respective physical regions. Define the encoding by
$$
V|\psi\rangle_{ab}
=(U_A\otimes U_B)
\bigl(|\psi\rangle_{ab}\otimes|\chi\rangle_{a'b'}\bigr),
$$
with the tensor factors reordered as $(a,a')|(b,b')$ when interpreting the physical split $A|B$.

The normalization of $\chi$ and unitarity of $U_A,U_B$ imply $V^\dagger V=I$. Both the auxiliary state and the unitaries are part of the encoding and must be held fixed as the logical state varies.

### 2.1 Recovering the two logical algebras

On the logical space define
$$
\mathcal M=\mathcal B(\mathcal H_a)\otimes I_b,
\qquad
\mathcal M'=I_a\otimes\mathcal B(\mathcal H_b).
$$
The commutant is taken in $\mathcal B(\mathcal H_{\mathrm{code}})$. Lecture 1 proved the corresponding finite tensor-factor formula.

For any logical $O_a$, choose
$$
O_A=U_A(O_a\otimes I_{a'})U_A^\dagger.
$$
Then
$$
(O_A\otimes I_B)V=V(O_a\otimes I_b).
$$
The analogous formula with $U_B$ reconstructs every operator in $\mathcal M'$ on $B$. We call this **complementary recovery**: one logical algebra is recoverable on $A$, and its commutant is recoverable on the complementary physical system $B$.

This does not recover the same full quantum system on two disjoint regions. The two logical algebras commute. Their intersection here contains only multiples of the identity.

## 3. What a physical observer's state looks like

Let $\rho_{ab}$ be any logical density matrix, including an entangled or mixed state. Its physical encoding is
$$
\widetilde\rho_{AB}=V\rho_{ab}V^\dagger.
$$
After tracing out $B$, the unitary $U_B$ disappears from the partial trace. Tracing $b$ gives $\rho_a$, and tracing $b'$ gives $\chi_{a'}$. Therefore
$$
\boxed{
\widetilde\rho_A
=U_A(\rho_a\otimes\chi_{a'})U_A^\dagger.
}
$$
Similarly,
$$
\widetilde\rho_B
=U_B(\rho_b\otimes\chi_{b'})U_B^\dagger.
$$
No assumption of a product logical state was made. Correlations between $a$ and $b$ remain in the complete encoding, while each reduction contains the appropriate logical restriction.

> **Physical picture.** Decoding region $A$ separates the information that may vary with the logical preparation from correlations built into the encoding. The fixed auxiliary state contributes entropy to $A$ even when its logical state has no entropy. A local unitary can make the two registers difficult to recognize physically without changing this entropy bookkeeping.

**Checkpoint 1.** May $\chi$ be chosen separately for each input state while retaining this one encoding?

**Answer.** No. The displayed $V$ is a fixed linear map. Choosing a different auxiliary state depending on an unknown input would define a different operation and would invalidate the recovery and entropy statements as properties of this code.

## 4. Deriving the entropy identity

We use natural logarithms and $S(\rho)=-\operatorname{Tr}\rho\log\rho$. Let $r_i$ be the eigenvalues of $\rho_a$ and $\lambda_j$ those of $\chi_{a'}$. The product state has eigenvalues $r_i\lambda_j$, so
$$
\begin{aligned}
S(\widetilde\rho_A)
&=-\sum_{i,j}r_i\lambda_j\log(r_i\lambda_j)\\
&=-\sum_i r_i\log r_i\sum_j\lambda_j
-\sum_j\lambda_j\log\lambda_j\sum_i r_i\\
&=S(\rho_a)+S(\chi_{a'}).
\end{aligned}
$$
The physical unitary leaves the spectrum unchanged. This proves entropy additivity in the form needed here, including zero logical eigenvalues by continuity with $0\log0=0$.

Define a logical operator
$$
\mathcal L_A=S(\chi_{a'})\,I_{\mathrm{code}}.
$$
It lies in the center of $\mathcal M$. For the factor algebra in this example, being central forces it to be scalar. We obtain
$$
\boxed{
S(\widetilde\rho_A)
=\operatorname{Tr}(\rho_{ab}\mathcal L_A)+S(\rho_a).
}
$$
The same fixed term appears for $B$ because the two reductions of the pure auxiliary state have equal entropy.

**Exact calculation.** This formula holds for every logical state in the specified code. The term $\mathcal L_A$ is dimensionless entropy. Calling it an “area term” at this stage is a structural comparison.

For maximally entangled auxiliary registers of dimension $k$, $\lambda_j=1/k$ and $S(\chi_{a'})=\log k$. For unequal weights the term is smaller. Its value is determined by the encoding, not simply by the number of auxiliary levels.

## 5. A four-qubit model with local mixing

Take one logical qubit on each side and one auxiliary qubit on each side. Choose
$$
|\chi\rangle_{a'b'}
=\frac{|00\rangle+|11\rangle}{\sqrt2}.
$$
Let $U_A$ be the controlled-NOT gate with logical register $a$ as control and auxiliary register $a'$ as target:
$$
U_A|i,s\rangle=|i,s\mathbin{\oplus}i\rangle.
$$
Use the analogous gate on $B$. Here $\oplus$ is addition modulo two.

The logical basis vector $|i,j\rangle$ is encoded as
$$
V|i,j\rangle
=\frac1{\sqrt2}
\sum_{s=0}^{1}|i,s\mathbin{\oplus}i\rangle_A
|j,s\mathbin{\oplus}j\rangle_B.
$$
This gives four orthonormal code vectors in a 16-dimensional physical space. Undoing the controlled-NOT gates makes the logical and auxiliary factors explicit.

### 5.1 A numerical spectrum that can be checked by hand

Choose the logical state
$$
\rho_{ab}=
\begin{pmatrix}
3/4&0\\
0&1/4
\end{pmatrix}_a
\otimes |0\rangle\langle0|_b.
$$
The spectrum of $\widetilde\rho_A$ is
$$
\frac38,\quad\frac38,\quad\frac18,\quad\frac18.
$$
Thus
$$
S(\widetilde\rho_A)
=h(3/4)+\log2,
$$
where $h(p)=-p\log p-(1-p)\log(1-p)$. Region $B$ has entropy $\log2$ because its logical state is pure.

If the two logical qubits were instead in a Bell state, both $\rho_a$ and $\rho_b$ would be maximally mixed. Each physical region would have entropy $2\log2$, although the full encoded state would remain pure. One contribution comes from logical entanglement and the other from the fixed auxiliary pair.

### 5.2 The reconstruction really uses the physical region

Conjugating by the controlled-NOT gives
$$
X_a\longmapsto X_aX_{a'},\qquad
Z_a\longmapsto Z_a.
$$
For example, flipping the control flips the target in the conjugated action, which verifies the first identity on $|i,s\rangle$. The logical $X$ is spread across two physical qubits inside $A$. Nevertheless, it is fully reconstructable using $A$.

This elementary mixing illustrates why recoverability should be formulated in terms of an algebra and an encoding. A particular tensor factor in the physical register is not necessarily the logical system.

**Checkpoint 2.** Does the extra $\log2$ reveal a new logical qubit available to Alice?

**Answer.** No. It comes from the auxiliary state fixed across the entire code. Alice's region has an additional mixed register after decoding, but that register does not store an independently variable logical input.

## 6. Self-study: distinguishability and modular Hamiltonians

The entropy identity is not the only exact relation in this code. Two logical states undergo the same unitary mixing and acquire the same auxiliary factor. Their relative distinguishability on $A$ therefore depends only on their restrictions to $a$.

### 6.1 Relative entropy is unchanged by the fixed auxiliary state

For density matrices $\rho$ and $\sigma$ with compatible supports, define
$$
D(\rho\Vert\sigma)
=\operatorname{Tr}\rho(\log\rho-\log\sigma).
$$
It is assigned $+\infty$ when the support of $\rho$ is not contained in that of $\sigma$. Assume first that the reference $\sigma_a$ and auxiliary $\chi_{a'}$ are full rank.

The logarithm of a product is
$$
\log(\sigma_a\otimes\chi_{a'})
=(\log\sigma_a)\otimes I_{a'}
+I_a\otimes\log\chi_{a'}.
$$
This follows by applying both sides to product eigenvectors. The same formula holds for $\rho_a$ on its support. Unitary conjugation carries a matrix logarithm into the logarithm of the conjugated matrix.

Substitution gives
$$
\begin{aligned}
D(\widetilde\rho_A\Vert\widetilde\sigma_A)
&=\operatorname{Tr}\bigl[
(\rho_a\otimes\chi_{a'})
\bigl((\log\rho_a-\log\sigma_a)\otimes I_{a'}\bigr)
\bigr]\\
&=D(\rho_a\Vert\sigma_a).
\end{aligned}
$$
The two auxiliary logarithms cancel. Compatible lower-rank cases follow by restricting to the common auxiliary support; incompatible logical supports give $+\infty$ on both sides.

This equality can also be understood operationally. Region $A$ contains an exactly recoverable copy of the state on the algebra of $a$, together with a fixed factor carrying no additional information about which logical preparation was chosen.

The general data-processing inequality says that a quantum channel cannot increase relative entropy. We have not proved that theorem here. We have directly proved equality for this particular channel and supplied its recovery map.

### 6.2 A compressed modular-Hamiltonian identity

Let $K_A^\sigma=-\log\widetilde\sigma_A$ and $K_a^\sigma=-\log\sigma_a$. From the product logarithm,
$$
K_A^\sigma
=U_A\bigl(K_a^\sigma\otimes I_{a'}
+I_a\otimes K_\chi\bigr)U_A^\dagger,
\qquad K_\chi=-\log\chi_{a'}.
$$
Pull the operator back to the logical Hilbert space:
$$
\begin{aligned}
V^\dagger(K_A^\sigma\otimes I_B)V
&=K_a^\sigma\otimes I_b
+\langle\chi|K_\chi\otimes I_{b'}|\chi\rangle I_{\mathrm{code}}\\
&=K_a^\sigma\otimes I_b+\mathcal L_A.
\end{aligned}
$$
The expectation in the second term is $\operatorname{Tr}(\chi_{a'}K_\chi)=S(\chi_{a'})$.

Notice the operation used: this is a **compression** with $V^\dagger$ and $V$. If $\chi$ is not maximally entangled, $K_\chi\otimes I$ need not leave the auxiliary vector proportional to itself. The compressed modular identity alone is not an uncompressed intertwining identity. The reconstruction operators in Section 2 satisfied a stronger relation.

The identity also concerns a one-sided modular Hamiltonian. In the corresponding difference between $A$ and $B$, the equal auxiliary entropy terms cancel. This is consistent with the distinction between one-sided and full modular generators in Lecture 3.

### 6.3 The finite first law

Take a full-rank reference state $\sigma$ and a smooth variation
$$
\rho(\varepsilon)=\sigma+\varepsilon\,\delta\rho+O(\varepsilon^2),
\qquad \operatorname{Tr}\delta\rho=0.
$$
For a differentiable spectral function, the derivative of its trace is
$$
\delta\operatorname{Tr} f(\rho)
=\operatorname{Tr}\bigl(f'(\sigma)\delta\rho\bigr).
$$
One way to see this is to diagonalize $\sigma$: to first order, the trace sums the diagonal variations weighted by $f'$ at the eigenvalues; off-diagonal changes of eigenvectors do not change the trace. Within a degenerate eigenspace, the same formula uses the trace of the perturbation in that eigenspace.

For $f(x)=-x\log x$, this yields
$$
\delta S
=-\operatorname{Tr}\bigl((\log\sigma+I)\delta\rho\bigr)
=\operatorname{Tr}(\delta\rho K_\sigma).
$$
Thus
$$
\delta S=\delta\langle K_\sigma\rangle.
$$
The generator is that of the fixed reference state. This is a finite-dimensional first-order identity. It does not by itself imply a gravitational equation or prescribe where to extremize a surface.

## 7. Generalizing from a factor to an algebra with a center

In our first code, the central term is a scalar. To let it vary across states while keeping it central, introduce sectors labeled by $\alpha$:
$$
\mathcal H_{\mathrm{code}}
=\bigoplus_\alpha
\bigl(\mathcal H_{a_\alpha}\otimes\mathcal H_{b_\alpha}\bigr).
$$
A direct sum says that the state can occupy different mutually orthogonal sectors. Inside each sector there are two quantum systems. We specify the accessible logical algebra
$$
\mathcal M
=\bigoplus_\alpha
\bigl(\mathcal B(\mathcal H_{a_\alpha})\otimes I_{b_\alpha}\bigr).
$$
It contains no operator connecting two different sectors.

Its commutant on the code is
$$
\mathcal M'
=\bigoplus_\alpha
\bigl(I_{a_\alpha}\otimes\mathcal B(\mathcal H_{b_\alpha})\bigr),
$$
and the center is spanned by the sector projectors $P_\alpha$:
$$
Z(\mathcal M)=\left\{\sum_\alpha c_\alpha P_\alpha\right\}.
$$
To verify this, first commute with all $P_\alpha$ to eliminate off-diagonal sector blocks, then use the tensor-factor commutant calculation inside each block. The sector label is available in both algebras, while noncommuting quantum observables belong to their respective sides.

### 7.1 The state seen by the algebra

For a logical state $\rho$, define
$$
p_\alpha=\operatorname{Tr}(\rho P_\alpha),\qquad
\rho_{a_\alpha}
=\frac{\operatorname{Tr}_{b_\alpha}(P_\alpha\rho P_\alpha)}
{p_\alpha}
$$
when $p_\alpha>0$. Zero-probability sectors contribute zero to the formulas below.

An observable $O=\bigoplus_\alpha(O_{a_\alpha}\otimes I_{b_\alpha})$ has expectation
$$
\operatorname{Tr}(\rho O)
=\sum_\alpha p_\alpha
\operatorname{Tr}(\rho_{a_\alpha}O_{a_\alpha}).
$$
Off-diagonal coherences $P_\alpha\rho P_\beta$ with $\alpha\ne\beta$ do not enter. The restricted state is represented abstractly by the blocks $p_\alpha\rho_{a_\alpha}$.

Using the trace that counts each irreducible matrix block once, define its entropy as
$$
\boxed{
S_{\mathcal M}(\rho)
=H(p_\alpha)+\sum_\alpha p_\alpha S(\rho_{a_\alpha}),
}
$$
where $H(p_\alpha)=-\sum_\alpha p_\alpha\log p_\alpha$.

The formula follows from the eigenvalues $p_\alpha r_{\alpha j}$ of the block density matrices. Expanding $-\sum_{\alpha j}p_\alpha r_{\alpha j}\log(p_\alpha r_{\alpha j})$ gives the displayed classical and quantum terms.

This is not generally the entropy of the full logical matrix $\rho$. The algebra may omit observables that detect coherences between sectors or information in the $b_\alpha$ factors.

### 7.2 Why the trace convention must be stated

As an operator on the full code Hilbert space, $O_{a_\alpha}\otimes I_{b_\alpha}$ has an ordinary trace containing a factor $\dim\mathcal H_{b_\alpha}$. That multiplicity counts an inaccessible register.

If one represents the restricted state by the particular ambient extension
$$
\bigoplus_\alpha
p_\alpha\rho_{a_\alpha}\otimes
\frac{I_{b_\alpha}}{\dim\mathcal H_{b_\alpha}},
$$
its ordinary matrix entropy is
$$
S_{\mathcal M}(\rho)
+\sum_\alpha p_\alpha\log\dim\mathcal H_{b_\alpha}.
$$
It represents the same expectations on $\mathcal M$, but its entropy includes the chosen maximally mixed multiplicity registers. We use the first convention and declare it explicitly.

### 7.3 Encode each sector with its own fixed auxiliary state

Choose a fixed pure auxiliary state $\chi_\alpha$ in each sector. Let the physical $A$ and $B$ spaces each contain orthogonal copies of the sector label and the appropriate quantum and auxiliary registers. Encode sector $\alpha$ using the construction of Section 2, with local unitaries $U_{A,\alpha},U_{B,\alpha}$.

Concretely, choose
$$
\mathcal H_A=\bigoplus_\alpha
(\mathcal H_{a_\alpha}\otimes\mathcal H_{a'_\alpha}),
\qquad
\mathcal H_B=\bigoplus_\alpha
(\mathcal H_{b_\alpha}\otimes\mathcal H_{b'_\alpha}).
$$
A logical vector $\bigoplus_\alpha|\psi_\alpha\rangle$ is mapped to the sum of the sector encodings
$$
V\left(\bigoplus_\alpha|\psi_\alpha\rangle\right)
=\sum_\alpha (U_{A,\alpha}\otimes U_{B,\alpha})
\left(|\psi_\alpha\rangle_{a_\alpha b_\alpha}
\otimes|\chi_\alpha\rangle_{a'_\alpha b'_\alpha}\right),
$$
with the tensor reordering used in Section 2. Each term lies in the physical block with matching sector labels on $A$ and $B$. Normalization within sectors and orthogonality between them give $V^\dagger V=I$.

Because both physical sides record the sector in orthogonal subspaces, tracing out $B$ kills cross-sector coherences. Up to a block unitary on $A$,
$$
\widetilde\rho_A
\cong
\bigoplus_\alpha
p_\alpha\rho_{a_\alpha}\otimes\chi_{a'_\alpha}.
$$
The symbol $\cong$ here means unitary equivalence on the support; unused physical subspaces carry zero eigenvalues.

If $r_{\alpha j}$ and $\lambda_{\alpha s}$ are the eigenvalues of the two factors, the physical eigenvalues are $p_\alpha r_{\alpha j}\lambda_{\alpha s}$. Expanding their logarithms gives
$$
S(\widetilde\rho_A)
=H(p_\alpha)
+\sum_\alpha p_\alpha S(\rho_{a_\alpha})
+\sum_\alpha p_\alpha S(\chi_{a'_\alpha}).
$$
Define
$$
\mathcal L_A=\sum_\alpha S(\chi_{a'_\alpha})P_\alpha.
$$
This is central and may have different eigenvalues in different sectors. The result becomes
$$
\boxed{
S(\widetilde\rho_A)
=S_{\mathcal M}(\rho)
+\operatorname{Tr}(\rho\mathcal L_A).
}
$$
**Exact calculation.** The result holds for all states in the constructed code, including states with coherence between sectors. The restricted algebra and the physical reduction both discard that coherence in the specified way.

Complementary recovery is checked block by block. Both physical sides can measure $P_\alpha$; within that sector $A$ reconstructs $a_\alpha$ and $B$ reconstructs $b_\alpha$. Shared central information is classical within these algebras, so it does not contradict the noncommutative no-cloning argument.

## 8. A three-level example with a nonconstant central term

The direct-sum notation becomes concrete in a particularly small model. Take a logical qubit with basis $|0\rangle,|1\rangle$, and two physical qutrits. Define
$$
V|0\rangle=|0,0\rangle,\qquad
V|1\rangle=\frac{|1,1\rangle+|2,2\rangle}{\sqrt2}.
$$
The two images are orthonormal. The logical algebra we choose to recover separately on $A$ and $B$ is the diagonal algebra
$$
\mathcal M=\operatorname{span}\{P_0,P_1\},
\qquad P_\alpha=|\alpha\rangle\langle\alpha|.
$$
It is its own commutant on this two-dimensional logical space. The full logical matrix algebra also exists, but it is not recoverable from either physical side alone.

For the pure input
$$
|\psi\rangle=\sqrt p\,|0\rangle+
e^{i\varphi}\sqrt{1-p}\,|1\rangle,
$$
with $0\le p\le1$ and real $\varphi$, the physical state is
$$
V|\psi\rangle
=\sqrt p\,|0,0\rangle+
e^{i\varphi}\sqrt{\frac{1-p}{2}}
\bigl(|1,1\rangle+|2,2\rangle\bigr).
$$
The reduced state on either side is
$$
\widetilde\rho_A
=\operatorname{diag}\left(p,\frac{1-p}{2},\frac{1-p}{2}\right).
$$
The phase $\varphi$ is absent because all cross terms have orthogonal labels on the traced-out side.

### 8.1 Three entropies with different meanings

The full logical input is pure:
$$
S(\rho)=0.
$$
Its restriction to the diagonal logical algebra has probabilities $p,1-p$:
$$
S_{\mathcal M}(\rho)=h(p).
$$
The physical reduced state has entropy
$$
\begin{aligned}
S(\widetilde\rho_A)
&=-p\log p-(1-p)\log\frac{1-p}{2}\\
&=h(p)+(1-p)\log2.
\end{aligned}
$$
Thus the central operator is
$$
\mathcal L_A=(\log2)P_1.
$$
Sector 0 has a product auxiliary state and contributes zero; sector 1 contains one fixed maximally entangled pair and contributes $\log2$.

At $p=1/2$, the physical eigenvalues are $1/2,1/4,1/4$, so
$$
S(\widetilde\rho_A)=\frac32\log2,
\qquad
S_{\mathcal M}(\rho)=\log2,
\qquad
\langle\mathcal L_A\rangle=\frac12\log2.
$$
All three quantities can be checked from their defining matrices.

### 8.2 Which observables can each side reconstruct?

The logical observable $Z=P_0-P_1$ is represented on $A$ by
$$
Z_A=\operatorname{diag}(1,-1,-1).
$$
It is also represented by the same diagonal matrix on $B$. Direct action on the two encoded basis vectors verifies the intertwining identities.

The logical $X=|0\rangle\langle1|+|1\rangle\langle0|$ cannot be reconstructed on $A$ alone. The encoded $|+\rangle$ and $|-\rangle$ inputs have identical $A$ reductions, although they have logical $X$ expectations $+1$ and $-1$. If an $A$ representative of $X$ existed, those equal reductions would give different expectations of the same local operator, a contradiction.

> **Physical picture.** Each side can read the sector, and neither side can read the relative phase between sectors. The entropy formula counts the uncertain sector label and the fixed entanglement associated with that sector. It does not count a phase that the specified algebra cannot observe.

**Checkpoint 3.** Would replacing $S_{\mathcal M}(\rho)$ by $S(\rho)$ give the right formula for this pure logical input?

**Answer.** No. It would omit $h(p)$. The code's accessible algebra is diagonal, while the full logical state contains coherence between its sectors.

### 8.3 Relative entropy for the same example

For two inputs with sector probabilities $p$ and $q$, $0<q<1$, the physical relative entropy is
$$
\begin{aligned}
D(\widetilde\rho_A\Vert\widetilde\sigma_A)
&=p\log\frac pq
+2\frac{1-p}{2}
\log\frac{(1-p)/2}{(1-q)/2}\\
&=p\log\frac pq+(1-p)\log\frac{1-p}{1-q}.
\end{aligned}
$$
This equals the relative entropy of the restricted diagonal states. The factors of two cancel because the auxiliary state in each sector is fixed by the same encoding.

The full logical states may be distinct pure superpositions, for which full-matrix relative entropy is infinite. That does not contradict the displayed finite answer: different algebras are being compared.

## 9. The relation to holography, and the extra claims

The exact code relation is
$$
S(\widetilde\rho_A)
=S_{\mathcal M}(\rho)+\langle\mathcal L_A\rangle_\rho.
$$
Its holographic comparison is a semiclassical generalized-entropy relation involving an area contribution and bulk-field entropy. The algebraic structure suggests identifying the logical observables with an effective bulk algebra and $\mathcal L_A$ with an appropriately defined area operator divided by $4G_N$.

**Formal analogy and further input.** Our finite construction has established neither a metric nor the existence of a surface whose area equals $\mathcal L_A$. It has no rule for extremizing that area. It also has no continuum field dynamics, gravitational constraints, or expansion in Newton's constant.

The corresponding relative-entropy and modular-Hamiltonian relations acquire holographic content only after a bulk/boundary identification and its regime have been specified. The original [JLMS analysis](https://arxiv.org/abs/1512.06431) concerns the relation at leading order in the bulk gravitational coupling for the states and setting considered there.

Harlow's [operator-algebra analysis](https://arxiv.org/abs/1607.03901) explains a general relationship between recovery and entropy structure. Our notes have proved explicit model cases. A theorem establishing the general normal form is additional mathematical input; an extremal-surface interpretation is additional physical input.

These distinctions give us a program for the rest of the course. We must learn what a local QFT algebra contributes, how a boundary CFT supplies a semiclassical code, and why geometric extremization computes the entropy in that regime. The finite examples tell us which parts of the answer come from encoding alone.

## 10. What to take away

- Complementary recovery concerns an algebra and its commutant; it does not clone a full quantum system.
- Fixed auxiliary entanglement gives an additive entropy term in an explicit code.
- A center allows the term to depend on a shared sector while remaining central.
- Entropy of a state restricted to an algebra may differ from entropy of the full logical density matrix.
- Relative entropy and compressed modular Hamiltonians obey exact identities in these finite codes.
- Identifying the central term with geometric area and extremizing a surface require further holographic input.

The opening block is now complete. The next planned unit will develop algebras with sectors through constrained quantum systems and then examine a small tensor-network code. Those examples will prepare the passage from a few controlled observables to a pattern of regions and reconstructable algebras.

## 11. Problem set

### Classroom core

**1. Unequal auxiliary weights.** In the factor code, replace the auxiliary Bell pair by $\sqrt\lambda|00\rangle+\sqrt{1-\lambda}|11\rangle$, with $0<\lambda<1$. Find $\mathcal L_A$ and $S(\widetilde\rho_A)$ for a maximally mixed logical qubit on $a$.

**2. Reconstruct through a gate.** Verify the controlled-NOT conjugation rules $X_a\mapsto X_aX_{a'}$ and $Z_a\mapsto Z_a$ by their action on $|i,s\rangle$.

**3. A central entropy term.** In the three-level code, choose $p=1/3$. List the physical reduced eigenvalues and calculate $S(\widetilde\rho_A)$, $S_{\mathcal M}(\rho)$, and $\langle\mathcal L_A\rangle$.

**4. Phase information.** Show that changing $\varphi$ in Section 8 leaves every one-side expectation unchanged. Give a joint physical operator, defined using $V$, that detects the logical $X$ expectation.

### Self-study consolidation

**5. Relative entropy.** In the factor code, take $\rho_a=\operatorname{diag}(3/4,1/4)$, $\sigma_a=I/2$, and a maximally entangled auxiliary qubit pair. Evaluate both sides of the relative-entropy identity directly from their eigenvalues.

**6. Full state versus algebra.** In the three-level model with $p=1/2$, compare the pure coherent input $|+\rangle$ with the incoherent input $I/2$. Calculate their full logical entropies, their restricted algebraic entropies, and their physical reduced entropies.

**7. A state-dependent central expectation.** For the same model, differentiate $S(\widetilde\rho_A)=h(p)+(1-p)\log2$ with respect to $p$. Separate the derivative of the algebraic entropy from that of the central expectation.

### Research extension

**8. Add a genuine quantum sector.** Construct a direct-sum code with two sectors, each containing a logical qubit accessible on $A$, and choose different fixed auxiliary entropies in the two sectors. Write an explicit isometry, recover one noncommuting pair inside each sector, and verify the entropy identity for a mixed state with nonzero sector probabilities. Completion requires matrices or a fully specified basis map; no geometric interpretation is required.

## 12. Answer checkpoints

**1.** The central operator is $h(\lambda)I_{\mathrm{code}}$. For $\rho_a=I/2$, $S(\widetilde\rho_A)=\log2+h(\lambda)$. The endpoints correspond to a product auxiliary state and can be treated by continuity for entropy; logarithmic operator formulas need support restrictions there.

**2.** Controlled-NOT is its own inverse. Acting successively on $|i,s\rangle$ gives $|i\oplus1,s\oplus1\rangle$ for the conjugated $X_a$, and a phase $(-1)^i$ for the conjugated $Z_a$.

**3.** All three physical eigenvalues are $1/3$, so $S(\widetilde\rho_A)=\log3$. The algebraic entropy is
$$
h(1/3)=\log3-\frac23\log2,
$$
and the central expectation is $(2/3)\log2$.

**4.** Partial tracing removes all cross-sector terms, leaving the diagonal state independent of $\varphi$. The physical operator $VXV^\dagger$, extended by zero on the orthogonal complement of the code, has expectation $2\sqrt{p(1-p)}\cos\varphi$. It is generally supported jointly on $AB$.

**5.** On $a$,
$$
D(\rho_a\Vert I/2)
=\frac34\log\frac32+\frac14\log\frac12.
$$
On $A$, the spectra are $(3/8,3/8,1/8,1/8)$ and $(1/4,1/4,1/4,1/4)$. Grouping repeated terms produces exactly the same answer.

**6.** The full logical entropies are $0$ and $\log2$. Both restrictions to $\mathcal M$ have entropy $\log2$, and both physical reduced states have entropy $(3/2)\log2$. Restricting the algebra removes the coherence that distinguishes the full states.

**7.** For $0<p<1$,
$$
\frac{dS(\widetilde\rho_A)}{dp}
=\log\frac{1-p}{p}-\log2.
$$
The first term is $dS_{\mathcal M}/dp$ and the second is $d\langle\mathcal L_A\rangle/dp$. Central does not mean constant across states when the center contains more than the identity.

For Problem 8, a useful starting point is to keep the sector labels orthogonal on both physical sides, use a product auxiliary vector in sector 0, and a maximally entangled auxiliary pair in sector 1. The within-sector logical $X$ and $Z$ should satisfy the reconstruction intertwining identities.

---

Previous: [[lecture-03-modular-structure|Lecture 3]]. Return to the [[courses/ads-cft-course/syllabus|course route]] or the project guide.

**Wiki connections.** [[ryu-takayanagi-formula|Ryu–Takayanagi formula]] · [[subregion-subalgebra-duality|subregion–subalgebra duality]]
