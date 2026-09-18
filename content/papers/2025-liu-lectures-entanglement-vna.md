---
title: "Lectures on entanglement, von Neumann algebras, and emergence of spacetime"
type: paper
authors: [Liu]
year: 2025
arxiv: "2510.07017"
areas: [bell-inequalities-qft, relative-entropy-qft]
status: preprint
---

## Summary

This is a major ~110-page review by [[hong-liu|Hong Liu]] (MIT), expanded from lectures given at TASI 2023, an NYU workshop (2023), the Asian Winter School (2023), and an ICMS Edinburgh meeting (2025). The review is organized around a single unifying thesis: the classification of von Neumann algebras into types I, II, and III is fundamentally a classification of entanglement types, and this classification governs both the information-theoretic structure of quantum field theory and the emergence of spacetime in quantum gravity.

**Part 1 (Sections II-V)** provides a self-contained and pedagogically rich treatment of [[type-iii-von-neumann-algebras|von Neumann algebra]] fundamentals. The exposition begins with a concrete, physically transparent example: an entangled spin chain in the $N \to \infty$ limit, where the algebra transitions from type I (finite $N$) through type III$_\lambda$ to type III$_1$ as the thermodynamic limit is taken. This example makes the otherwise abstract classification tangible. The review then develops [[tomita-takesaki-modular-theory|Tomita-Takesaki modular theory]] in detail, covering the modular operator $\Delta$, modular conjugation $J$, the modular automorphism group $\sigma_s$, and the KMS condition. A key message is that for type III algebras there is no trace, no density matrix, and no von Neumann entropy --- the modular structure replaces all standard entanglement measures. Relative modular flows and [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]] $S(\omega\|\varphi) = -\langle\Omega, \log\Delta_{\Phi,\Omega}\,\Omega\rangle$ are developed as the correct information-theoretic quantities. The [[crossed-product-construction|crossed product construction]] $\hat{\mathcal{M}} = \mathcal{M} \rtimes_\sigma \mathbb{R}$ is presented as the mechanism by which a type III$_1$ algebra can be "dressed" to produce a type II$_\infty$ algebra, restoring a semifinite trace and making entropy well-defined. The Connes classification via invariants $S(\mathcal{M})$ and $T(\mathcal{M})$ is reviewed, with type III$_1$ characterized by $S(\mathcal{M}) = \mathbb{R}^+$.

**Part 2 (Sections VI-IX)** applies this algebraic machinery to quantum gravity via AdS/CFT. In the large $N$ limit, boundary algebras of a holographic CFT undergo a type I $\to$ type III$_1$ transition. The [[subregion-subalgebra-duality]] identifies bulk spacetime regions $R$ with emergent type III$_1$ boundary subalgebras $\mathcal{M}_R$, so that the causal structure of the bulk is encoded in the commutant structure of boundary algebras. Modular flows and half-sided modular translations are shown to generate time evolution in the bulk. An algebraic formulation of ER=EPR is presented: spacetime connectivity is equivalent to algebraic commutant structure. The [[crossed-product-construction|crossed product]] $\hat{\mathcal{M}} = \mathcal{M} \rtimes_\sigma \mathbb{R}$ turns the type III$_1$ boundary algebra into type II$_\infty$, and the resulting trace gives rise to gravitational entropy --- recovering the Bekenstein-Hawking entropy for black holes and the Gibbons-Hawking entropy for de Sitter space. The review concludes with speculative proposals for AQFT as a framework for background-independent quantum gravity via an $(A, S)$ formulation (algebra + state, without fixed background geometry).

## Key Results

1. **Von Neumann algebra type = entanglement type.** The classification into types I, II, III is reframed as a classification of the structure of entanglement: type I corresponds to finite-dimensional entanglement (density matrices exist), type II to semifinite entanglement (trace exists but no minimal projections), and type III to infinite long-range entanglement (no trace, no density matrix).

2. **Entangled spin example of type III emergence.** A concrete $N$-spin chain model shows how the local algebra transitions from type I at finite $N$ to type III$_\lambda$ and then type III$_1$ as $N \to \infty$. This provides a physically transparent route to understanding an otherwise abstract classification.

3. **Modular structure as replacement for density matrices.** In type III algebras, the Tomita-Takesaki modular operator $\Delta$ and conjugation $J$ replace the density matrix formalism entirely. The modular Hamiltonian $K = -\log\Delta$ generates a one-parameter automorphism group $\sigma_s(A) = \Delta^{-is} A \Delta^{is}$ satisfying the KMS condition $f_{AB}(s) = f_{BA}(-s-i)$, which characterizes thermal behavior emerging from entanglement.

4. **Crossed product restores entropy.** The modular crossed product $\hat{\mathcal{M}} = \mathcal{M} \rtimes_\sigma \mathbb{R}$ promotes a type III$_1$ factor to type II$_\infty$, introducing a semifinite trace that makes von Neumann entropy well-defined. This is the algebraic mechanism underlying gravitational entropy.

5. **Connes invariants for classification.** The Connes spectrum $S(\mathcal{M})$ (closure of the spectrum of $\log\Delta$ for any faithful normal state) and $T(\mathcal{M})$ (the kernel of the modular automorphism in the outer automorphism group) classify type III factors: type III$_1$ has $S(\mathcal{M}) = \mathbb{R}^+$, meaning the modular Hamiltonian has full-line spectrum.

6. **Type I $\to$ type III$_1$ transition in holography.** At finite $N$, the boundary CFT algebra for a subregion is type I (finite-dimensional Hilbert space). In the $N \to \infty$ limit, it becomes type III$_1$, mirroring the emergence of a smooth bulk spacetime from the boundary theory.

7. **Subregion-subalgebra duality.** Bulk spacetime regions $R$ in AdS/CFT are identified with emergent type III$_1$ boundary subalgebras $\mathcal{M}_R$. Bulk causal structure is encoded in the commutant structure: $\mathcal{M}_R' = \mathcal{M}_{R'}$ (Haag duality for emergent regions).

8. **Algebraic ER=EPR.** Spacetime connectivity (Einstein-Rosen bridge) is reformulated as a statement about the algebraic commutant structure of boundary subalgebras. Two boundary regions are "connected" in the bulk iff their algebras fail to commute, i.e., they share nontrivial correlations encoded in the algebraic structure.

9. **Gravitational entropy from crossed product.** The crossed product of the type III$_1$ boundary algebra with its modular automorphism group produces a type II$_\infty$ algebra with a semifinite trace. The entropy computed from this trace reproduces the generalized gravitational entropy (Bekenstein-Hawking + bulk entanglement entropy) for black holes, de Sitter horizons, and general subregions.

10. **AQFT as quantum gravity framework.** The review speculates that algebraic QFT, formulated as an $(A, S)$ pair (abstract algebra + state) without reference to a background spacetime, may provide a framework for background-independent quantum gravity. Spacetime emerges from the algebraic and entanglement structure rather than being put in by hand.

## Methods

- **Algebraic quantum field theory (AQFT):** The entire framework is set in the Haag-Kastler axiomatic setting, where observables are organized into local von Neumann algebras $\mathcal{M}(\mathcal{O})$ assigned to spacetime regions $\mathcal{O}$.
- **Tomita-Takesaki modular theory:** Systematic use of the modular operator $\Delta$, conjugation $J$, and modular Hamiltonian $K = -\log\Delta$ as the primary tools for both entanglement characterization and spacetime reconstruction.
- **GNS construction:** States are represented as vectors in GNS Hilbert spaces; the review emphasizes the role of cyclic separating vectors for type III algebras.
- **Crossed product construction:** $\hat{\mathcal{M}} = \mathcal{M} \rtimes_\sigma \mathbb{R}$ is used to promote type III algebras to type II, enabling trace-based entropy computations.
- **Half-sided modular inclusions:** Used to reconstruct bulk causal structure from boundary algebra inclusions, connecting modular flows to geometric translations in the bulk.
- **Connes classification:** The invariants $S(\mathcal{M})$ and $T(\mathcal{M})$ are used to distinguish type III subtypes and track the type transition in the large $N$ limit.

## Relevance

This review is directly relevant to Marcelo's quantum information program on multiple fronts:

**Bell-CHSH program.** The construction of Bob's operators from Alice's via the modular conjugation $J$, which is the backbone of the Weyl operator Bell-CHSH framework (Phys. Rev. D 108, 085026; 2023), is placed here in the broader context of Tomita-Takesaki theory for type III$_1$ algebras. Liu's review makes explicit that $J$ maps the algebra to its commutant $J\mathcal{M}J = \mathcal{M}'$, and that this mapping is the algebraic expression of complementarity between causally separated regions. The pedagogical treatment of the entangled spin example and the modular automorphism group provides new intuition for why the construction works and what its limitations are.

**Relative entropy program.** Marcelo's group computes [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]] for [[coherent-states|coherent states]], [[squeezed-states|squeezed states]], and [[cat-states|cat states]] relative to the vacuum. Liu reviews the same quantity in the algebraic setting and then connects it to gravitational entropy via the [[crossed-product-construction|crossed product construction]]: the relative entropy on the type III$_1$ algebra is related, through the crossed product, to a well-defined von Neumann entropy on the type II$_\infty$ algebra. This provides a gravitational interpretation of the same quantity Marcelo computes in flat-space QFT.

**Entanglement embezzlement.** Ismael Porfirio's PhD work on [[entanglement-embezzlement|entanglement embezzlement]] in type III$_1$ algebras receives important context from this review. Liu explains physically why the type III$_1$ structure enables exact embezzlement: in the $N \to \infty$ limit of the spin chain, all faithful normal states become equivalent, and there are no "minimal" states from which entanglement cannot be extracted. The [[crossed-product-construction|crossed product construction]], which turns type III$_1$ into type II$_\infty$, is directly relevant to making the cost of embezzlement quantifiable --- in the type II$_\infty$ algebra, a trace exists and one can meaningfully assign an entropy cost to embezzlement protocols.

**New territory.** The [[subregion-subalgebra-duality]] and algebraic ER=EPR open potential directions for applying [[weyl-operators|Weyl operator]] Bell tests and relative entropy computations in holographic settings. The type III$_1$ boundary algebras in AdS/CFT are the same kind of algebras on which Marcelo's formalism operates. Whether the Bell-CHSH and relative entropy techniques developed for flat-space QFT can probe holographic spacetime structure is an open question (see [[bell-chsh-in-holographic-setting]]).

## Questions Raised

1. Can the [[crossed-product-construction|crossed product construction]] be used to define a finite entropy cost for [[entanglement-embezzlement|embezzlement]] in QFT, by passing from the type III$_1$ local algebra to the type II$_\infty$ crossed product? This would give a precise answer to the question [[embezzlement-cost-relative-entropy]].

2. Does the type I $\to$ type III$_1$ transition in the large $N$ limit of holographic CFTs have an analog in the Gribov-Zwanziger framework, where the gauge-fixed theory has modified propagators and a restricted configuration space? See [[type-iii-algebras-across-areas|type III structure in gauge theories]].

3. Can the [[bell-chsh-inequality|Bell-CHSH tests]] constructed via [[weyl-operators|Weyl operators]] and modular conjugation $J$ be applied to the emergent type III$_1$ boundary algebras in AdS/CFT to probe bulk causal structure? See [[bell-chsh-in-holographic-setting]].

4. The algebraic ER=EPR proposal (spacetime connectivity $\leftrightarrow$ algebraic commutant structure) suggests that entanglement measures like relative entropy could detect spacetime topology changes. Is this computationally accessible in simple holographic models?

5. The $(A, S)$ formulation of quantum gravity (algebra + state, no background spacetime) is highly speculative but conceptually aligned with the AQFT tools used in Marcelo's program. Could the flat-space Weyl algebra constructions serve as a testing ground for this formalism?

## Related Papers

- [[bell-inequalities-qft]] area papers, especially the foundational Phys. Rev. D 108, 085026 (2023) on Weyl operators and Tomita-Takesaki for Bell-CHSH
- [[relative-entropy-qft]] area papers, especially the Nucl. Phys. B 1018 (2025) on Araki-Uhlmann relative entropy for coherent states
- Chandrasekaran, Penington, Witten (2022-2023) on gravitational algebras and type II structure in quantum gravity (referenced extensively in Liu's review)
- Witten, "Gravity and the crossed product" (2022) --- the gravitational crossed product construction that Liu's review builds upon
- Haag, "Local Quantum Physics" (1996) --- the foundational AQFT reference that Liu's review modernizes and extends
- Longo, "An analogue of the Kac-Wakimoto formula and black hole conditional entropy" (2019) --- algebraic entropy in AQFT
