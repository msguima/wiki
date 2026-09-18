---
title: "Condensed Matter and QFT Quantum Information: Shared Mathematical Structures"
type: connection
areas: [condensed-matter-connections, bell-inequalities-qft]
maturity: speculative
modified: 2026-04-06
---

## The Link

Topological materials — Weyl semimetals, topological insulators, topological superconductors — are described by effective field theories that share deep mathematical structures with the relativistic QFT quantum information program. This is not an analogy but a precise overlap: the same operator-algebraic tools (modular theory, von Neumann algebras, entanglement measures) appear in the rigorous treatment of both systems, while the same physical phenomena (anomalies, defect operators, axionic couplings) connect the condensed matter and high-energy descriptions. The speculative claim of this connection page is that the quantum information techniques developed for Bell-CHSH and relative entropy in relativistic QFT can be profitably exported to topological materials, and conversely that the condensed matter context provides new physical intuition and concrete models for the relativistic program.

The first and most direct link is through axionic electrodynamics. The [[axionic-electrodynamics|topological magnetoelectric effect (TME)]] in topological insulators is described by adding a term θE·B to the Maxwell action — the same theta-term that appears in QCD in the context of the strong CP problem and topological susceptibility. In the Weyl superconductor work (Phys. Rev. B 103, 2021), the relative phase between Weyl nodes becomes a dynamical pseudo-axion field that modifies the photon propagator. This is a direct relativistic QFT calculation applied to a condensed matter system. The axionic coupling affects the commutation relations of the electromagnetic field operators — it changes what the local algebra of observables is — which has immediate consequences for entanglement and Bell inequalities. Specifically, the [[axionic-electrodynamics|TME]] modifies the equal-time commutators of E and B, which would alter the algebra used to build [[weyl-operators|Weyl operators]] W(f) = exp(i∫f·A) for the Bell-CHSH construction.

The second link is through topological order. [[bf-theory|BF theory]], which appeared in the confinement-duality work as the effective description of the condensed-defect phase (Phys. Rev. D 86, 2012), is also the standard effective theory of intrinsic topological order in (2+1) dimensions — the long-wavelength theory of the fractional quantum Hall effect and of quantum spin liquids. In (3+1) dimensions, BF theory describes topological insulators. The mathematical structure of BF theory — its local algebra, its ground state degeneracy on non-simply-connected manifolds, its anyonic excitations — has been extensively studied in the condensed matter context. Importing these results into the relativistic QFT setting, and vice versa, is the content of this bridge.

The third link is through entanglement in many-body systems. The condensed matter community has developed a rich theory of entanglement entropy in many-body systems, including area laws, topological entanglement entropy (the constant subleading term in entanglement entropy that diagnoses topological order), and entanglement spectrum. These are not directly computed using [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]] or [[tomita-takesaki-modular-theory|Tomita-Takesaki modular theory]] — they typically use the replica trick and reduced density matrices — but the underlying algebraic structures are related. Erick Landim's thesis on von Neumann algebras, embezzlement, and many-body theory is the current vehicle for making this connection precise within the research program.

## Evidence

- **Massive photon in axionic Weyl superconductors** (Phys. Rev. B 103, 2021; 4 citations): Direct computation of how the dynamical pseudo-axion modifies the photon propagator. This propagator modification is of the same type as the Gribov correction but with different physics — it comes from integrating out the fermionic modes of the Weyl nodes. The same Weyl operator methods used in the Bell program could be applied here.
- **Multivalued fields and monopole operators in topological superconductors** (Ann. Phys. 419, 2020; 2 citations): The monopole (disorder) operator is the condensed matter analog of the 't Hooft operator in gauge theories. Its vacuum expectation value diagnoses topological order. Computing it requires non-perturbative techniques — exactly the kind developed in the QFT quantum information program.
- **BF theory from Julia-Toulouse condensation** (Phys. Rev. D 86, 2012; 11 citations): Establishes a direct derivation of topological BF theory from defect condensation. Since BF theory describes topological order in condensed matter, this creates a direct path from the confinement program to the condensed matter context.
- **Effective field theories for Weyl superconductors** (Ann. Phys. 374, 2016; 8 citations): The effective electromagnetic description of Weyl superconductors involves p-form gauge fields and duality transformations — the same mathematical toolkit used in the massive p-form and duality papers in the confinement program.
- **Topological entanglement entropy** (Kitaev-Preskill, Levin-Wen, 2006): The topological entanglement entropy S_topo = −ln D (where D is the total quantum dimension) is a key diagnostic for topological order. This is a purely entanglement-based probe of a quantum phase, and it is precisely the kind of connection between entanglement measures and phase structure that the [[entanglement-probes-of-phases|entanglement probes of phases]] connection explores in the gauge theory context.
- **Chiral anomaly in Weyl semimetals**: The chiral anomaly, familiar from QFT, has a direct condensed matter manifestation in Weyl semimetals — the anomalous Hall effect and negative magnetoresistance. The chiral anomaly modifies the commutation relations of currents, which affects operator algebras. This is a concrete route from anomaly physics to the algebraic structure studied in the Bell program.

## Gaps

The primary gap is that no paper in the portfolio has yet directly applied [[weyl-operators|Weyl operators]], [[tomita-takesaki-modular-theory|Tomita-Takesaki modular theory]], or [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]] to a condensed matter system. The condensed matter work in the portfolio uses QFT methods (effective field theories, duality, path integrals) but not the quantum-information-theoretic algebraic methods of the Bell and relative entropy programs. Bridging this requires:

1. **Identifying the appropriate algebra**: In relativistic QFT, the local algebra M(O) is a type III₁ factor. In a lattice condensed matter system, it is type I (matrix algebras). The continuum limit of the lattice system, and the question of what algebraic type it approaches, is non-trivial and is the subject of Erick Landim's thesis.

2. **Axionic modification of Weyl operator algebra**: The theta-term E·B modifies the commutation relations of the electromagnetic field. Working out the precise modification to the algebra generated by [[weyl-operators|Weyl operators]] W(f) = exp(i∫f·A) in the presence of an axionic coupling requires a careful canonical analysis that has not been done.

3. **Entanglement across a Weyl node**: In a Weyl semimetal, the two Weyl nodes of opposite chirality are spatially separated in momentum space. The entanglement between left-movers and right-movers across the Fermi arc surface states is a physically interesting quantity that could be studied using the Bell-CHSH or relative entropy methods.

4. **Topological entanglement entropy vs. Araki-Uhlmann**: The topological entanglement entropy computed in condensed matter uses the replica trick and von Neumann entropy. The Araki-Uhlmann relative entropy is defined differently and applies in type III settings. Understanding the precise relationship between these two measures — and whether one can recover topological entanglement entropy from an Araki-Uhlmann quantity — is a fundamental open problem.

5. **Physical observability in condensed matter**: In relativistic QFT, Bell-CHSH violations are computed but not directly measured. In condensed matter, quantum information experiments are far more accessible. Whether the Bell-CHSH observable constructed from axionic-electromagnetic Weyl operators has a concrete condensed matter implementation is an open question with potentially significant experimental relevance.

## Potential Projects

1. **Weyl operator algebra in axionic electrodynamics**: Compute the algebra generated by W(f) = exp(i∫f·A) in theta-electrodynamics (Maxwell + theta·E·B). Specifically, determine the modified commutation relations [W(f), W(g)] when the theta-term is present, and work out how the vacuum expectation value ⟨W(f)⟩_theta differs from the standard Gaussian result. This is technically accessible and would produce the first concrete Bell-CHSH analysis in a topological insulator effective theory.

2. **Bell-CHSH in a Weyl semimetal model**: Take the effective fermionic model of Phys. Rev. B 103, 2021 and construct Bell-CHSH operators from the fermionic modes of opposite chirality (localized near opposite Weyl points). This parallels the spinor Bell-CHSH computation of Phys. Rev. D 108, L081701 (2023) but in the condensed matter context.

3. **Relative entropy between topological and trivial phases**: Compute the Araki-Uhlmann relative entropy S(ω_top‖ω_trivial) between the ground state of a topological insulator (theta = π) and that of a trivial insulator (theta = 0) at the effective field theory level. This would give a relative entropy-based probe of the topological phase transition.

4. **Type III limit of topological matter**: Study the algebraic type of the local observable algebra of a Weyl superconductor effective field theory in the continuum limit. Does it approach type III₁ (as in relativistic QFT)? If so, Araki-Uhlmann relative entropy and embezzlement are well-defined, and the full machinery of the relativistic Bell program applies. This is the foundational question for the condensed matter bridge and connects directly to Erick Landim's thesis.

5. **Topological entanglement entropy from Araki-Uhlmann relative entropy**: Attempt to recover the topological entanglement entropy S_topo of BF theory (which should give the quantum dimension D of the anyonic theory) from an Araki-Uhlmann relative entropy computation in the BF field theory. This would unify the condensed matter and relativistic QFT entanglement diagnostics.

6. **Axionic electrodynamics and modular Hamiltonian**: Derive the modular Hamiltonian for the vacuum state of axionic electrodynamics (theta-Maxwell theory) in a Rindler wedge, generalizing the standard result (2π times the boost generator) to the theta ≠ 0 case. This would give the full Tomita-Takesaki modular theory for topological insulator effective field theories.

## Related

### Areas
- [[condensed-matter-connections]]
- [[bell-inequalities-qft]]
- [[relative-entropy-qft]]
- [[confinement-duality]]

### Connections
- [[type-iii-algebras-across-areas]]
- [[entanglement-probes-of-phases]]
- [[julia-toulouse-meets-generalized-symmetries]]

### Concepts
- [[weyl-operators]]
- [[tomita-takesaki-modular-theory]]
- [[araki-uhlmann-relative-entropy]]
- [[type-iii-von-neumann-algebras]]
- [[axionic-electrodynamics|topological magnetoelectric effect]]
- [[axionic-electrodynamics]]
- [[bf-theory]]
- [[topological-order]]
- [[topological-entanglement-entropy]]
- [[bell-chsh-inequality]]
- [[rindler-wedges]]
- [[tomita-takesaki-modular-theory|modular Hamiltonian]]
- [[chiral-anomaly]]
- [[magnetic-monopoles]]

### Questions
- [[type-iii-algebras-across-areas|type III structure in gauge theories]]
- [[entanglement-as-confinement-probe]]
- [[weyl-operators-in-topological-materials]]

### Entities
- [[silvio-paolo-sorella]]
- erick-landim
- ismael-porfirio
- [[clovis-wotzasek]]
- [[breno-chrispim]]
- [[rodrigo-bruni]]
