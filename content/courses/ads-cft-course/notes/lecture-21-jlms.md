---
title: "Lecture 21 — Relative entropy across the holographic dictionary"
type: lecture-notes
edition: "2.2 — rewritten at the AQFT standard"
lecture: 21
semester: 2
week: 4
hours: 3
prerequisites: "Lectures 4, 5, 16, 19 and 20"
status: "rewritten 2026-09-30, pending instructor review; the sector-code identities and one direction of Harlow's equivalence proved in finite dimensions, the semiclassical JLMS argument sketched from the quantum-corrected Ryu–Takayanagi formula"
modified: 2026-09-30
---

# Lecture 21 — Relative entropy across the holographic dictionary

> *Holographic entropy contains a large geometric term, the area of the Ryu–Takayanagi surface in Planck units. Yet the relative entropy of two nearby boundary states equals the relative entropy of the corresponding bulk states, with no area term at all. Jafferis, Lewkowycz, Maldacena and Suh derived this from the quantum-corrected Ryu–Takayanagi formula of Faulkner, Lewkowycz and Maldacena, and Harlow showed that the same structure holds exactly in every quantum error-correcting code with complementary recovery. We derive the cancellation exactly in a code with sectors and a nontrivial center, where the area appears as a central operator whose expectation value cancels between entropy and modular energy. We then prove that a Ryu–Takayanagi formula with a central area implies the equality of relative entropies, by the same first-law argument that Jafferis and collaborators use in gravity, and we state Harlow's equivalence in full. With Lecture 20 this explains entanglement-wedge reconstruction, which Dong, Harlow and Wall proved with operator-algebra error correction.*

## How to use this lecture

**Classroom core, one meeting of three hours.** The history (§1, 10 minutes), the decoded form of the states (§2, 20 minutes), the sector-by-sector logarithm (§3, 25 minutes), and the modular Hamiltonian (§4, 20 minutes) come before a 10-minute break. After it come Harlow's equivalence (§5, 35 minutes) and the holographic argument (§6, 30 minutes), with 30 minutes for Checkpoints 1 and 2 and Problems 4–6; Problems 1–3 complete the core assignment. These allocations are proposals and have not been tested in class.

**Self-study.** The two-sector example (§7), stability and state dependence near a transition (§8), and Problems 7–12, including the action of boundary modular flow on reconstructed operators.

**Research extension.** An approximate version for a stable semiclassical wedge, the relative entropy of a ball at second order as bulk canonical energy, and the extension to infinite dimensions, in Problems 13–15.

**Prerequisites.** Lecture 4 for algebraic codes and the algebraic entropy, Lecture 5 for centers, Lecture 16 for the Ryu–Takayanagi prescription, Lecture 19 for entanglement wedges, Lecture 20 for the equality theorem, Lecture 11, §6, for the first law in finite dimensions.

**What this lecture establishes.** The entropy, relative-entropy and modular-Hamiltonian identities of the sector code are proved exactly, and so is the implication from a Ryu–Takayanagi formula with a central area to the equality of relative entropies and the modular-Hamiltonian identity. The other two directions of Harlow's equivalence are sketched with the sources. The holographic relation of Jafferis, Lewkowycz, Maldacena and Suh is sketched from the formula of Faulkner, Lewkowycz and Maldacena, which is stated only.

## 0. Reading

**Primary.**

- D. L. Jafferis, A. Lewkowycz, J. Maldacena, S. J. Suh, [Relative entropy equals bulk relative entropy](https://arxiv.org/abs/1512.06431) (2015).
- D. Harlow, [The Ryu-Takayanagi Formula from Quantum Error Correction](https://arxiv.org/abs/1607.03901) (2016), Sections 4–5.
- T. Faulkner, A. Lewkowycz, J. Maldacena, [Quantum corrections to holographic entanglement entropy](https://arxiv.org/abs/1307.2892) (2013).

**Secondary.**

- X. Dong, D. Harlow, A. C. Wall, [Reconstruction of Bulk Operators within the Entanglement Wedge in Gauge-Gravity Duality](https://arxiv.org/abs/1601.05416) (2016).
- A. Almheiri, X. Dong, D. Harlow, [Bulk Locality and Quantum Error Correction in AdS/CFT](https://arxiv.org/abs/1411.7041) (2014).
- D. Harlow, [TASI Lectures on the Emergence of the Bulk in AdS/CFT](https://arxiv.org/abs/1802.01040) (2018).

**Optional research reading.**

- M. J. Kang, D. K. Kolchmeyer, [Holographic Relative Entropy in Infinite-dimensional Hilbert Spaces](https://arxiv.org/abs/1811.05482) (2018).
- N. Lashkari, M. Van Raamsdonk, [Canonical Energy is Quantum Fisher Information](https://arxiv.org/abs/1508.00897) (2015).
- J. Cotler, P. Hayden, G. Penington, G. Salton, B. Swingle, M. Walter, [Entanglement Wedge Reconstruction via Universal Recovery Channels](https://arxiv.org/abs/1704.05839) (2017).
- C. Bény, A. Kempf, D. W. Kribs, [Generalization of Quantum Error Correction via the Heisenberg Picture](https://arxiv.org/abs/quant-ph/0608071) (2006), and [Quantum Error Correction of Observables](https://arxiv.org/abs/0705.1574) (2007).

## 1. Why does the area disappear from distinguishability?

In 2013 Faulkner, Lewkowycz and Maldacena computed the first quantum correction to the Ryu–Takayanagi formula. The minimal surface divides the bulk into two regions, and the correction is, up to local terms at the surface, the entanglement entropy of the bulk fields between them,

$$
S(\rho_A)=\frac{\langle\widehat{\operatorname{Area}}(\gamma_A)\rangle_\rho}{4G_N}+S_{\mathrm{bulk}}(\rho_a)+\cdots,
$$

where $a$ is the bulk region of the entanglement wedge, the dots stand for local terms at the surface and counterterms, and the formula holds to order $G_N^0$. Two years later Jafferis, Lewkowycz, Maldacena and Suh drew the consequence for relative entropy. Applying the first law to both sides for every nearby state, they argued that the boundary modular Hamiltonian is the area operator plus the bulk modular Hamiltonian, and therefore that boundary relative entropy equals bulk relative entropy. They also argued that boundary modular flow acts as bulk modular flow in the entanglement wedge. Dong, Harlow and Wall combined the relative-entropy equality with the error-correction language of Almheiri, Dong and Harlow in 2016 and proved that every bulk operator in the entanglement wedge can be reconstructed on the boundary region.

Harlow then asked in the same year what these relations are, stripped of gravity. He showed that in any quantum error-correcting code with complementary recovery a version of the quantum-corrected Ryu–Takayanagi formula holds, with an area operator in the center of the recoverable algebra, and that complementary recovery, this formula, and the equality of relative entropies are equivalent. Lecture 4 constructed codes of this kind. This lecture uses them to derive the cancellation of the area exactly, and then follows the holographic argument, whose structure is the same.

## 2. Write the states in their decoded form

Let the recoverable algebra be

$$
\mathcal M=\bigoplus_\alpha\mathcal B(\mathcal H_{a_\alpha})\otimes I_{\bar a_\alpha}.
$$

A state restricted to $\mathcal M$ consists of sector probabilities $p_\alpha$ and normalized matrices $\rho_\alpha$ on $a_\alpha$. In an exact code with complementary recovery, the physical region has, for a logical state $\rho$, the decoded form

$$
\rho_A=U_A\left[\bigoplus_\alpha p_\alpha\,\rho_\alpha\otimes\chi_\alpha\right]U_A^\dagger,
$$

where $U_A$ is a unitary of the region and $\chi_\alpha$ is a fixed auxiliary state, the same for every logical input, which may depend on the sector. Take a faithful reference with probabilities $q_\alpha$ and matrices $\sigma_\alpha$. The algebraic entropy of Lecture 4 is

$$
S_{\mathcal M}(\rho)=H(p)+\sum_\alpha p_\alpha S(\rho_\alpha),
$$

and the physical entropy is

$$
S(\rho_A)=S_{\mathcal M}(\rho)+\sum_\alpha p_\alpha S(\chi_\alpha)=S_{\mathcal M}(\rho)+\langle\mathcal L\rangle_\rho,
\qquad
\mathcal L=\bigoplus_\alpha S(\chi_\alpha)\,I_\alpha .
$$

The operator $\mathcal L$ is central in $\mathcal M$, and it plays the role of the area operator divided by $4G_N$. Its expectation value changes when the sector probabilities change, although $\mathcal L$ is a fixed operator on the code.

## 3. Take the logarithm sector by sector

On each supported block,

$$
\log\left(p_\alpha\,\rho_\alpha\otimes\chi_\alpha\right)=\log p_\alpha+\log\rho_\alpha+\log\chi_\alpha,
$$

where each term acts on its own factor of the block. The same $\log\chi_\alpha$ appears in the reference, since $\chi_\alpha$ does not depend on the logical state, so it cancels in the difference of logarithms:

$$
D(\rho_A\Vert\sigma_A)=\sum_\alpha p_\alpha\log\frac{p_\alpha}{q_\alpha}+\sum_\alpha p_\alpha D(\rho_\alpha\Vert\sigma_\alpha)=D_{\mathcal M}(\rho\Vert\sigma).
$$

The right-hand side is the relative entropy of the two states restricted to $\mathcal M$, the sum of the classical distinguishability of the central label and of the quantum distinguishability within each sector. Coherences between sectors do not belong to the restricted algebra and enter neither side. Note that no limit, saddle point or gravitational interpretation was used: this is an exact identity for the stated encoded states. [Proved.]

**Checkpoint 1.** Where did the cancellation of the auxiliary states use that $\chi_\alpha$ is independent of the logical state?

**Answer.** In the difference $\log(p_\alpha\rho_\alpha\otimes\chi_\alpha)-\log(q_\alpha\sigma_\alpha\otimes\chi_\alpha)$. If the auxiliary state depended on the input, the two logarithms would contain different $\log\chi_\alpha$, and additional distinguishability could hide in the auxiliary factor (Problem 8).

## 4. The modular Hamiltonian contains the same information

The regional modular Hamiltonian of the reference is $K_A^\sigma=-\log\sigma_A$. Compressed to the code, or evaluated in any code state,

$$
V^\dagger K_A^\sigma V=K_{\mathcal M}^\sigma+\mathcal L,
\qquad
K_{\mathcal M}^\sigma=\bigoplus_\alpha\left[-\log q_\alpha-\log\sigma_\alpha\right]\otimes I_{\bar a_\alpha},
$$

on the support of the code. The auxiliary contribution becomes $S(\chi_\alpha)$ because the code places $\chi_\alpha$ on the auxiliary factor, where the expectation value of $-\log\chi_\alpha$ is $-\operatorname{Tr}\chi_\alpha\log\chi_\alpha$. This is a compressed identity. It does not claim that $K_A^\sigma$ acts as a multiple of the identity on auxiliary excitations outside the code.

Combining it with the entropy identity of §2,

$$
\Delta\langle K_A^\sigma\rangle-\Delta S_A=\Delta\langle K_{\mathcal M}^\sigma\rangle-\Delta S_{\mathcal M},
$$

where the differences are taken between $\rho$ and $\sigma$. The central term cancels even though its expectation value changes between the two states: it enters the modular energy and the entropy with the same coefficient.

## 5. Harlow's equivalence

The structure of §§2–4 is not an accident of the chosen codes. Let $V:\mathcal H_{\mathrm{code}}\to\mathcal H_A\otimes\mathcal H_{\bar A}$ be an isometry and $\mathcal M$ a von Neumann algebra on the code, with commutant $\mathcal M'$.

**Theorem (Harlow, 2016). Stated only — refs: Harlow 2016, Sections 4–5; one direction proved below.** In finite dimensions the following are equivalent.

1. *Complementary recovery.* Every operator of $\mathcal M$ has a representative on $A$ and every operator of $\mathcal M'$ one on $\bar A$, in the sense of the intertwining relation $O_AV=VO$ of Lecture 2.
2. *A Ryu–Takayanagi formula.* There is an operator $\mathcal L_A$ in the center of $\mathcal M$ such that $S(\rho_A)=\operatorname{Tr}(\rho\mathcal L_A)+S_{\mathcal M}(\rho)$ and $S(\rho_{\bar A})=\operatorname{Tr}(\rho\mathcal L_A)+S_{\mathcal M'}(\rho)$ for every code state.
3. *Equality of relative entropies.* $D(\rho_A\Vert\sigma_A)=D_{\mathcal M}(\rho\Vert\sigma)$ and $D(\rho_{\bar A}\Vert\sigma_{\bar A})=D_{\mathcal M'}(\rho\Vert\sigma)$ for all code states.

The direction from (1) to (2) uses a structure lemma: with complementary recovery the code takes the decoded form of §2 on both sides, with the auxiliary states $\chi_\alpha$ entangled between $A$ and $\bar A$. The computation of §2 then gives (2). The direction from (3) to (1) is the theorem of Dong, Harlow and Wall in Harlow's algebraic form. Its proof applies the equality for $\bar A$ to the states $e^{i\lambda O}\rho e^{-i\lambda O}$ with $O\in\mathcal M$, which agree on $\mathcal M'$. Their restrictions to $\bar A$ therefore cannot depend on $\lambda$, so that every operator on $\bar A$ compresses into $\mathcal M'$, and the theorem of operator-algebra error correction of Bény, Kempf and Kribs then provides the representatives on $A$. [Sketched — refs: Dong–Harlow–Wall 2016; Harlow 2016, §5.]

The direction from (2) to (3) is the argument that Jafferis and collaborators use in gravity, and it can be proved here in a few lines. [Proved, for every faithful reference $\sigma$; the full theorem supplies the rest.] Fix a faithful reference $\sigma$ and consider code states $\rho(\lambda)=\sigma+\lambda\,\delta\rho$, with $\delta\rho$ traceless and Hermitian. The first law of Lecture 11, §6, applied on the region and in the algebra, gives

$$
\frac{d}{d\lambda}S(\rho_A)\Big|_0=\operatorname{Tr}\left(\delta\rho\,V^\dagger K_A^\sigma V\right),
\qquad
\frac{d}{d\lambda}S_{\mathcal M}(\rho)\Big|_0=\operatorname{Tr}\left(\delta\rho\,K_{\mathcal M}^\sigma\right).
$$

Differentiating the formula (2) and using these, $\operatorname{Tr}\bigl[\delta\rho\,(V^\dagger K_A^\sigma V-\mathcal L_A-K_{\mathcal M}^\sigma)\bigr]=0$ for every traceless Hermitian $\delta\rho$ on the code. Therefore

$$
V^\dagger K_A^\sigma V=\mathcal L_A+K_{\mathcal M}^\sigma+c\,I
$$

on the code, with $c$ a constant, which vanishes: at $\rho=\sigma$ the formula (2) gives $\langle K_A^\sigma\rangle_\sigma=S(\sigma_A)=\operatorname{Tr}(\sigma\mathcal L_A)+\langle K_{\mathcal M}^\sigma\rangle_\sigma$. This is the modular-Hamiltonian identity of §4, now derived from the entropy formula alone. Relative entropy is a difference of modular energy and entropy, $D(\rho_A\Vert\sigma_A)=\Delta\langle K_A^\sigma\rangle-\Delta S_A$, and substituting the two identities,

$$
D(\rho_A\Vert\sigma_A)=\Delta\langle\mathcal L_A+K_{\mathcal M}^\sigma\rangle-\Delta\langle\mathcal L_A\rangle-\Delta S_{\mathcal M}=\Delta\langle K_{\mathcal M}^\sigma\rangle-\Delta S_{\mathcal M}=D_{\mathcal M}(\rho\Vert\sigma).
$$

The central term cancels. $\square$

**Checkpoint 2.** Where does the centrality of $\mathcal L_A$ enter?

**Answer.** Not in the first-law argument, which cancels $\mathcal L_A$ whatever it is. A term fixed by the restriction of $\rho$ to $\mathcal M$ requires $\mathcal L_A\in\mathcal M$, and the same operator must also serve the formula for $\bar A$ and $\mathcal M'$, so it lies in $\mathcal M\cap\mathcal M'$, the center. Centrality also makes the area-like term drop out of the modular flow of $\mathcal M$ (Problem 11).

## 6. The holographic argument

In gravity the role of formula (2) is played by the formula of Faulkner, Lewkowycz and Maldacena. [Stated only — refs: Faulkner–Lewkowycz–Maldacena 2013.] Jafferis, Lewkowycz, Maldacena and Suh apply the argument of §5 to a code subspace of states near a reference state, small bulk perturbations of a fixed geometry. Two facts make the gravitational version work. The extremal surface moves when the state changes, but its displacement does not contribute to the first variation of the area, because the surface is extremal; the same stationarity argument returns in Lecture 22, §3. And the area operator commutes with the bulk operators of the entanglement wedge at leading order, which makes it central for the algebra of the wedge. The first law on the boundary and in the bulk then gives

$$
K_A\big|_{\mathrm{code}}=\frac{\widehat{\operatorname{Area}}(\gamma_A)}{4G_N}+K_a^{\mathrm{bulk}}+\text{local terms at }\gamma_A+O(G_N),
$$

and the difference of modular energy and entropy gives

$$
D_A^{\mathrm{boundary}}(\rho\Vert\sigma)=D_a^{\mathrm{bulk}}(\rho\Vert\sigma)+O(G_N).
$$

[Sketched — refs: Jafferis–Lewkowycz–Maldacena–Suh 2015.] The area term and the local terms at the surface cancel between modular energy and entropy, exactly as the central operator $\mathcal L$ did in §4. The finite code therefore explains why an area-like contribution can enter the entropy and the modular energy and drop out of the relative entropy. But it does not derive the gravitational area operator, and it does not prove the gravitational relation, which is a statement at leading order in $G_N$ for a stated code subspace, with renormalization, gravitational constraints and possible surface terms treated consistently.

The same identity gives a statement about modular flow. Since the area operator is central in the wedge algebra, its flow acts trivially there, and $e^{isK_A}$ acts on reconstructed operators as the bulk modular flow $e^{isK_a^{\mathrm{bulk}}}$. In the sector code this is exact (Problem 10). It is the gravitational counterpart of the identity of Lecture 20, §5, on Connes cocycles, $\mathcal N^\dagger(\widetilde\sigma^{it}\widetilde\rho^{-it})=\sigma^{it}\rho^{-it}$, which says that a channel preserving relative entropy carries relative modular flows into each other. The equality of relative entropies for the entanglement wedge is the input of the reconstruction theorem of Dong, Harlow and Wall, who combined it with operator-algebra error correction. [Stated only — refs: Dong–Harlow–Wall 2016.]

> **Physical picture: the area as a classical label.** In the code the central operator $\mathcal L$ records which sector the state is in, and each sector carries its own amount of auxiliary entanglement between the region and its complement. The area of the Ryu–Takayanagi surface plays that role in gravity: to leading order it commutes with everything in the wedge, and it measures the entanglement of the degrees of freedom at the surface that no bulk operator in the wedge can see. Relative entropy asks how well two states can be told apart by operators in the wedge, and those operators are blind to the label's auxiliary entanglement. This is an interpretation of the exact finite identity and of the sketched gravitational one; the identification of edge modes at the surface with the auxiliary factors is Harlow's proposal.

## 7. Self-study: a two-sector example

Let both quantum sector states be fixed and equal between $\rho$ and $\sigma$, and let the sector probabilities be $(p,1-p)$ and $(q,1-q)$, with auxiliary entropies $s_0$ and $s_1$. Then

$$
D_A(\rho\Vert\sigma)=p\log\frac pq+(1-p)\log\frac{1-p}{1-q},
\qquad
\Delta\langle\mathcal L\rangle=(p-q)(s_0-s_1).
$$

The entropy difference and the modular-energy difference both contain the second expression, and their difference does not. The cancellation is therefore not restricted to states with the same expected area-like term. If $s_0=s_1$, the central term is constant on the code, a useful special case; assuming it from the start would hide how central sectors work.

## 8. Self-study: stability and state dependence

Lecture 20 connected preservation of relative entropy with recovery in finite dimensions, and Harlow's theorem shows that the equality of this lecture is equivalent to complementary recovery. Several qualifications remain in holography. The bulk algebra can have a center, so one recovers an algebra with a center, which need not be a tensor factor. The gravitational effective theory is regulated and perturbative, and the equality holds to the order at which it is derived. An approximate equality must hold with the uniformity needed for the desired recovery statement, which is what the universal recovery channels of Lecture 20, §7, supply.

Near a transition of the kind found in Lecture 19, changing the input can change the entanglement wedge and with it the algebra. One should either restrict to a stable branch, where the same surface dominates for every state of the code, or include the dependence of the wedge on the state explicitly. A single identity for a fixed algebra cannot be assumed across competing geometries without explanation.

## 9. What to take away

- **Proved:** in a code with sectors and fixed auxiliary states, $S(\rho_A)=S_{\mathcal M}(\rho)+\langle\mathcal L\rangle_\rho$ with a central $\mathcal L$, $V^\dagger K_A^\sigma V=K_{\mathcal M}^\sigma+\mathcal L$, and $D(\rho_A\Vert\sigma_A)=D_{\mathcal M}(\rho\Vert\sigma)$.
- **Proved:** a Ryu–Takayanagi formula with a central area operator, valid for every code state, implies the modular-Hamiltonian identity and the equality of relative entropies, by the first law.
- **Stated only, with two directions sketched and one proved:** Harlow's theorem, the equivalence of complementary recovery, the formula with a central area, and the equality of relative entropies.
- **Sketched:** in holography the formula of Faulkner, Lewkowycz and Maldacena gives $K_A=\widehat{\operatorname{Area}}/4G_N+K_a^{\mathrm{bulk}}+\cdots$ and boundary relative entropy equal to bulk relative entropy at leading order in $G_N$; boundary modular flow acts as bulk modular flow in the wedge.

## 10. Looking ahead

Lecture 22 takes the first law in the opposite direction. There the entropy is the area and the modular energy is known from the boundary, and requiring the first law for every ball constrains the bulk metric; in the language of this lecture it is the statement that the modular-Hamiltonian identity holds at first order around the vacuum. Lectures 25–27 use the generalized entropy $\langle\widehat{\operatorname{Area}}\rangle/4G_N+S_{\mathrm{bulk}}$ of §1 to locate the quantum extremal surface of a black hole and its radiation, and Lecture 29 returns to the algebra of the entanglement wedge at large $N$.

## 11. Problem set

### Classroom core

1. **A direct-sum logarithm.** Explain why the classical term $\sum_\alpha p_\alpha\log(p_\alpha/q_\alpha)$ appears in $D(\rho_A\Vert\sigma_A)$.

2. **Fixed versus state dependent.** Can $\langle\mathcal L\rangle$ vary while $\mathcal L$ is a fixed operator?

3. **Compression versus a global identity.** What does $V^\dagger K_AV$ retain, and what does it not determine?

4. **The sector identity.** For two sectors with $\rho_\alpha=\sigma_\alpha$ and auxiliary states $\chi_0=|0\rangle\langle0|$ and $\chi_1=I_2/2$, compute $S(\rho_A)$, $S_{\mathcal M}(\rho)$ and $\langle\mathcal L\rangle$ for sector probabilities $(p,1-p)$.

5. **The central term in two differences.** In the setting of Problem 4, compute $\Delta\langle K_A^\sigma\rangle$ and $\Delta S_A$ separately between $p$ and $q$, and check that their difference is $D_{\mathcal M}$.

6. **From the formula to relative entropy.** Starting from $S(\rho_A)=\langle\mathcal L\rangle_\rho+S_{\mathcal M}(\rho)$ and $V^\dagger K_A^\sigma V=\mathcal L+K_{\mathcal M}^\sigma+cI$, derive $D(\rho_A\Vert\sigma_A)=D_{\mathcal M}(\rho\Vert\sigma)$ in two lines.

### Self-study consolidation

7. **Classical distinguishability only.** Evaluate the two-sector example of §7 for $p=\frac12$ and $q=\frac14$.

8. **A changing auxiliary state.** Suppose $\chi_\alpha$ also changes with the logical input. Which step of §3 fails, and in which direction does the inequality between $D(\rho_A\Vert\sigma_A)$ and $D_{\mathcal M}(\rho\Vert\sigma)$ go?

9. **The first law in an algebra.** Prove $\frac{d}{d\lambda}S_{\mathcal M}(\rho(\lambda))|_0=\operatorname{Tr}(\delta\rho\,K_{\mathcal M}^\sigma)$ from the direct-sum form of the restricted state.

10. **Modular flow of a reconstruction.** In the decoded form, let $O_A=U_A[\bigoplus_\alpha O_\alpha\otimes I]U_A^\dagger$ represent $O\in\mathcal M$. Show that $e^{isK_A^\sigma}O_Ae^{-isK_A^\sigma}$ represents $e^{isK_{\mathcal M}^\sigma}Oe^{-isK_{\mathcal M}^\sigma}$.

11. **A central operator flows trivially.** Show that $e^{is\mathcal L}Oe^{-is\mathcal L}=O$ for every $O\in\mathcal M$, and conclude that the area-like term does not affect the modular flow of the algebra.

12. **Multiplicities.** Show that $D_{\mathcal M}(\rho\Vert\sigma)$ does not depend on the dimensions of the factors $\bar a_\alpha$, while an entropy computed with the ambient trace does.

### Research extension

13. **An approximate version.** Formulate a controlled approximate equality of relative entropies for a stable semiclassical wedge, and the recovery statement it implies. *Known:* Cotler and collaborators derive entanglement-wedge reconstruction from an approximate equality using universal recovery channels. *Completion:* a statement that specifies the perturbative order, the reference state, the code family, the algebra and the error criterion, with the resulting bound on the recovery fidelity.

14. **Relative entropy at second order.** For a ball in a holographic CFT, the relative entropy between a perturbed state and the vacuum is quadratic in the perturbation. Show, for a linearized metric perturbation, that it equals the canonical energy of the perturbation in the AdS–Rindler wedge. *Known:* Lashkari and Van Raamsdonk prove that the quantum Fisher information of the ball equals the canonical energy. *Completion:* the argument with the Iyer–Wald form of Lecture 22, and a check of positivity for one explicit perturbation.

15. **Infinite dimensions.** Extend the equivalence of complementary recovery and equality of relative entropies to von Neumann algebras on infinite-dimensional spaces. *Known:* Kang and Kolchmeyer prove it for general von Neumann algebras, type III$_1$ included, assuming that code vectors cyclic and separating for the bulk algebra are dense and remain cyclic and separating after encoding; the formula (2) has no direct type-III analogue. *Completion:* the statement with its hypotheses, and a type-I example with an infinite-dimensional center where (2) can also be written.

## 12. Answer checkpoints

1. Each block carries the scalar weight $p_\alpha$, and $\log(p_\alpha\rho_\alpha\otimes\chi_\alpha)$ contains $\log p_\alpha$ times the identity of the block. The term is lost if every block is normalized and the weights are forgotten.

2. Yes. Changing $p_\alpha$ changes $\sum_\alpha p_\alpha S(\chi_\alpha)$, although $\mathcal L=\bigoplus_\alpha S(\chi_\alpha)I_\alpha$ is fixed.

3. The matrix elements of $K_A$ between code states. It says nothing about the action of $K_A$ on states orthogonal to the code.

4. $S_{\mathcal M}(\rho)=h(p)+\sum_\alpha p_\alpha S(\rho_\alpha)$ with $h(p)=-p\log p-(1-p)\log(1-p)$, and $\langle\mathcal L\rangle=p\cdot0+(1-p)\log2$, so $S(\rho_A)=h(p)+\sum_\alpha p_\alpha S(\rho_\alpha)+(1-p)\log2$.

5. With $\rho_\alpha=\sigma_\alpha$, $\Delta\langle K_A^\sigma\rangle=\sum_\alpha(p_\alpha-q_\alpha)[-\log q_\alpha+S(\sigma_\alpha)+S(\chi_\alpha)]$, and $\Delta S_A=h(p)-h(q)+\sum_\alpha(p_\alpha-q_\alpha)[S(\sigma_\alpha)+S(\chi_\alpha)]$. The terms in $S(\sigma_\alpha)$ and $S(\chi_\alpha)$ cancel in the difference, which is $-\sum_\alpha(p_\alpha-q_\alpha)\log q_\alpha-h(p)+h(q)=\sum_\alpha p_\alpha\log(p_\alpha/q_\alpha)$.

6. $D(\rho_A\Vert\sigma_A)=\Delta\langle K_A^\sigma\rangle-\Delta S_A=\Delta\langle\mathcal L+K_{\mathcal M}^\sigma\rangle-\Delta\langle\mathcal L\rangle-\Delta S_{\mathcal M}=\Delta\langle K_{\mathcal M}^\sigma\rangle-\Delta S_{\mathcal M}$, which is $D_{\mathcal M}(\rho\Vert\sigma)$; the constant cancels in the difference.

7. $D=\frac12\log2+\frac12\log\frac23=\frac12\log\frac43$, independent of $s_0$ and $s_1$.

8. The logarithms of the auxiliary states no longer cancel. With auxiliary states $\chi_\alpha^\rho$ and $\chi_\alpha^\sigma$, the computation of §3 gives $D(\rho_A\Vert\sigma_A)=D_{\mathcal M}(\rho\Vert\sigma)+\sum_\alpha p_\alpha D(\chi_\alpha^\rho\Vert\chi_\alpha^\sigma)\geq D_{\mathcal M}(\rho\Vert\sigma)$: the region distinguishes the states better than the algebra does, because information about the input leaks into the auxiliary factor.

9. The restricted state is $\bigoplus_\alpha p_\alpha\rho_\alpha$ on $\bigoplus_\alpha a_\alpha$, and $S_{\mathcal M}$ is the von Neumann entropy of this block-diagonal matrix. The first law for a matrix, $\frac d{d\lambda}S=-\operatorname{Tr}(\delta\rho_{\mathcal M}\log\sigma_{\mathcal M})$, gives $\operatorname{Tr}(\delta\rho\,K_{\mathcal M}^\sigma)$, because $K_{\mathcal M}^\sigma$ is the logarithm of the block-diagonal reference and the traceless $\delta\rho$ removes the identity term.

10. In the decoded form $K_A^\sigma=U_A[\bigoplus_\alpha(-\log q_\alpha-\log\sigma_\alpha)\otimes I-I\otimes\log\chi_\alpha]U_A^\dagger$ on the supported blocks. The terms $\log q_\alpha$ and $\log\chi_\alpha$ commute with $O_\alpha\otimes I$, so the conjugation acts only through $\sigma_\alpha^{-is}O_\alpha\sigma_\alpha^{is}$, which is the modular flow of $O$ in $\mathcal M$.

11. $\mathcal L$ is a multiple of the identity in each block, so it commutes with every block-diagonal $O=\bigoplus_\alpha O_\alpha\otimes I$. Adding $\mathcal L$ to $K_{\mathcal M}^\sigma$ therefore leaves $e^{isK}Oe^{-isK}$ unchanged.

12. $D_{\mathcal M}=\sum_\alpha p_\alpha\log(p_\alpha/q_\alpha)+\sum_\alpha p_\alpha D(\rho_\alpha\Vert\sigma_\alpha)$ involves only the states on the factors $a_\alpha$. An entropy computed with the ambient trace treats $\rho_\alpha\otimes I_{\bar a_\alpha}/d_{\bar a_\alpha}$ and adds $\sum_\alpha p_\alpha\log d_{\bar a_\alpha}$, which depends on the multiplicities; the term cancels in relative entropy.

**Wiki connections.** [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] · [[subregion-subalgebra-duality|subregion–subalgebra duality]] · [[ryu-takayanagi-formula|Ryu–Takayanagi formula]]
