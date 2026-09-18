---
title: Subregion-Subalgebra Duality
type: concept
areas: [bell-inequalities-qft, relative-entropy-qft, gauge-gravity-duality]
aliases: [entanglement wedge reconstruction]
modified: 2026-04-07
---

## Definition

**Subregion-subalgebra duality** is the identification, in the AdS/CFT correspondence, of a bulk spacetime region $R$ with a boundary subalgebra $\mathcal{M}_R$ of observables. Concretely, for a boundary subregion $A$, there exists a bulk region $\mathcal{E}(A)$ --- the **entanglement wedge** --- such that the algebra of bulk operators in $\mathcal{E}(A)$ is isomorphic to the boundary algebra $\mathcal{M}_A$:

$$\mathcal{M}_{\text{bulk}}(\mathcal{E}(A)) \cong \mathcal{M}_{\text{bdy}}(A).$$

In the large $N$ limit of the boundary CFT, these boundary subalgebras are [[type-iii-von-neumann-algebras|type III$_1$ von Neumann algebras]], so the bulk causal structure is encoded in the commutant structure of type III$_1$ factors on the boundary:

$$\mathcal{M}_R' = \mathcal{M}_{R'}$$

where $R'$ is the causal complement of $R$ in the bulk. This is a holographic version of [[haag-duality|Haag duality]].

The entanglement wedge $\mathcal{E}(A)$ is bounded by the **Ryu-Takayanagi (RT) surface** (or its covariant generalization, the HRT surface), which is the minimal-area extremal surface anchored to the boundary of $A$. The area of this surface gives the leading contribution to the entanglement entropy via the RT formula $S(A) = \text{Area}(\gamma_A)/(4G_N)$.

## Role in Research

Subregion-subalgebra duality provides a bridge between Marcelo's algebraic QFT tools and holographic physics:

**Same algebraic setting.** The type III$_1$ boundary algebras in AdS/CFT are the same kind of algebras on which the [[bell-inequalities-qft|Bell-CHSH program]] and [[relative-entropy-qft|relative entropy program]] operate. The [[weyl-operators|Weyl operator]] constructions and [[tomita-takesaki-modular-theory|modular theory]] tools developed for flat-space QFT are, in principle, applicable to the boundary algebras of holographic CFTs. Whether this leads to computable results that probe bulk structure is an open question (see [[bell-chsh-in-holographic-setting]]).

**Modular flow = bulk time evolution.** In the holographic setting, the modular automorphism group $\sigma_s$ of a boundary subalgebra generates a geometric flow in the bulk. For [[rindler-wedges|Rindler-like wedges]] on the boundary, this is related to bulk boosts, echoing the Bisognano-Wichmann theorem for flat-space QFT. Half-sided modular translations reconstruct the full bulk causal structure from boundary data.

**Crossed product and gravitational entropy.** Via the [[crossed-product-construction|crossed product construction]], the type III$_1$ boundary algebra $\mathcal{M}_A$ is promoted to a type II$_\infty$ algebra $\hat{\mathcal{M}}_A$, and the trace on $\hat{\mathcal{M}}_A$ recovers the generalized gravitational entropy. This connects [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]] on the type III$_1$ algebra to the gravitational entropy formula.

## Relations

- [[type-iii-von-neumann-algebras]] --- boundary subalgebras in the large $N$ limit are type III$_1$ factors
- [[tomita-takesaki-modular-theory]] --- modular flows of boundary algebras generate bulk geometric flows
- [[crossed-product-construction]] --- promotes the type III$_1$ boundary algebra to type II$_\infty$, giving gravitational entropy
- [[araki-uhlmann-relative-entropy]] --- well-defined on the type III$_1$ boundary algebras; related to gravitational entropy via the crossed product
- [[rindler-wedges]] --- the simplest example of subregion-subalgebra duality, where the Rindler wedge algebra has modular flow equal to the boost
- [[haag-duality]] --- subregion-subalgebra duality is the holographic extension of Haag duality for local algebras
- [[gauge-gravity-duality]] --- area page collecting the AdS/CFT setting in which this duality is formulated.

## Papers

- [[2025-liu-lectures-entanglement-vna]] --- comprehensive review covering the algebraic formulation of subregion-subalgebra duality and its connection to gravitational entropy
- Ryu-Takayanagi (2006) --- original derivation of the holographic entanglement entropy formula
- Jafferis, Lewkowycz, Maldacena, Suh (2016) --- entanglement wedge reconstruction and its relation to modular flows

See also [[bell-inequalities-qft]] and [[relative-entropy-qft]] for the broader program.

## Notes

- Subregion-subalgebra duality goes beyond the simpler statement of "entanglement wedge reconstruction" by making the algebraic structure precise: it is not just that bulk operators can be reconstructed on the boundary, but that the reconstructed operators form a type III$_1$ von Neumann algebra with specific modular properties.
- The duality breaks down away from the large $N$ limit: at finite $N$, the boundary algebra is type I (finite-dimensional) and the bulk semiclassical description fails. The type I $\to$ type III$_1$ transition as $N \to \infty$ is the algebraic signature of the emergence of smooth bulk spacetime.
- For Marcelo's program, the key observation is that the algebraic tools (Weyl operators, modular conjugation, relative entropy) are universal across type III$_1$ algebras, whether they arise from flat-space QFT or from holographic boundary theories. The physics is different, but the mathematics is the same.
