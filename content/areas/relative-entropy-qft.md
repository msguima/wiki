---
title: Araki-Uhlmann Relative Entropy in Quantum Field Theory
type: area
status: active
modified: 2026-04-06
---

## Overview

Launched in 2025 as a natural extension of the [[bell-inequalities-qft|Bell inequality program]], this line investigates [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]] in relativistic quantum field theory. Relative entropy S(ω‖φ) measures the distinguishability between two quantum states and, unlike von Neumann entropy, is well-defined for the [[type-iii-von-neumann-algebras|type III₁ von Neumann algebras]] that characterize local algebras of observables in QFT. This makes it the natural information-theoretic quantity for relativistic settings.

The program derives closed-form and numerical results for the relative entropy between various excited states — [[coherent-states|coherent states]], [[squeezed-states|squeezed states]], and [[cat-states|cat states]] — and the vacuum of the free massive scalar field. A central technical finding is that relative entropy for coherent states is controlled by the [[pauli-jordan-distribution|smeared Pauli-Jordan distribution]], linking the information-theoretic quantity to the causal structure of spacetime. Dependence on mass, region size, and spacetime dimension is being systematically mapped out.

This is an active and rapidly developing line, with clear open directions toward interacting theories, gauge fields, and connections to confinement and [[entanglement-embezzlement|entanglement embezzlement]].

## Key Results

### Analytical Results

- **Relative entropy of coherent states in (1+1)d** (Nucl. Phys. B 1018, 2025): Closed-form expression showing that S(ω_f‖ω_0) is proportional to the smeared [[pauli-jordan-distribution|Pauli-Jordan distribution]] Δ(f, f). The result verifies positivity, monotonic increase with region size, and monotonic decrease with increasing mass.
- **Single-mode squeezed states** (Eur. Phys. J. C 85, 2025): Closed-form expression for [[squeezed-states|squeezed states]] constructed via Bogoliubov transformations. The result exhibits qualitatively different mass and region-size dependence compared to coherent states.
- **Relative entropy between two coherent states** (Eur. Phys. J. C 85, 2025): Generalization beyond vacuum-to-excited comparisons; the relative entropy grows linearly with the spatial distance between the two localized excitations and decreases with mass.

### Numerical Results

- **Numerical framework for (1+1)d Minkowski spacetime** (Nucl. Phys. B 1018, 2025): Systematic numerical evaluation for [[coherent-states|coherent states]], cross-checking analytical results and enabling exploration of parameter regimes not tractable analytically.
- **Mass dependence across dimensions d = 1, 2, 3** (arXiv:2511.20244): The monotonic decay with mass seen in (1+1)d is modified in higher dimensions; the dimension-dependence of the relative entropy is non-trivial and physically revealing.

## Open Problems

1. **[[relative-entropy-interacting-theories|Relative entropy in interacting theories]]**: All current results are for free fields. Extending to interacting QFTs — where modular operators are far less explicit — is a major open challenge.
2. **Relative entropy as a probe of confinement**: Whether S(ω‖φ) changes qualitatively across a confinement/deconfinement transition in a gauge theory, making it a candidate order parameter. See [[entanglement-as-confinement-probe]].
3. **[[embezzlement-cost-relative-entropy|Embezzlement cost via relative entropy]]**: In [[type-iii-von-neumann-algebras|type III₁]] algebras, [[entanglement-embezzlement|entanglement embezzlement]] is possible without any cost measured by standard entanglement monotones. Relative entropy may provide a more refined measure of the cost.
4. **Relative entropy for gauge fields and BRST-invariant states**: Extending the formalism to gauge theories requires identifying the correct gauge-invariant or [[brst-symmetry|BRST]]-invariant sector.
5. **Entanglement monotones from relative entropy**: Constructing entanglement monotones for QFT states using relative entropy as a building block (e.g., relative entropy of entanglement).

## Key Concepts

- **[[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]]**: Defined as S(ω‖φ) = −⟨Ω, log Δ_{Φ,Ω} Ω⟩, where Δ_{Φ,Ω} is the relative modular operator associated with two states ω and φ on the algebra. Generalizes the classical Kullback-Leibler divergence and the quantum von Neumann relative entropy to the algebraic setting of [[type-iii-von-neumann-algebras|type III algebras]], where individual entropies are infinite but differences are finite.
- **[[pauli-jordan-distribution|Smeared Pauli-Jordan distribution]]**: The commutator function Δ(f, g) = ⟨0|[φ(f), φ(g)]|0⟩ of the free scalar field, smeared against test functions f, g. It encodes the causal structure and appears as the fundamental building block in closed-form expressions for relative entropy of [[coherent-states|coherent states]].
- **[[coherent-states|Coherent states]]**: States of the form W(f)|0⟩, where W(f) = exp(iφ(f)) is a [[weyl-operators|Weyl operator]]. They represent localized excitations above the vacuum and are the primary class of states for which explicit relative entropy formulas have been derived.
- **[[squeezed-states|Squeezed states]]**: States produced by Bogoliubov transformations that reduce uncertainty in one quadrature below the vacuum level. Relevant in quantum optics and cosmology (squeezed vacua in inflation).
- **[[cat-states|Cat states]]**: Superpositions of coherent states |α⟩ + |−α⟩. The interference terms from superposition introduce new qualitative features in the relative entropy not present for individual coherent states.
- **[[tomita-takesaki-modular-theory|Tomita-Takesaki modular theory]]**: The relative modular operator Δ_{Φ,Ω} is computed within the Tomita-Takesaki framework, making modular theory the central technical tool for all results in this area.
- **[[type-iii-von-neumann-algebras|Type III₁ von Neumann algebras]]**: Local algebras in QFT belong to this class. Standard von Neumann entropy is infinite (ultraviolet divergent) for any state, but [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]] is finite and well-defined, making it the physically correct information quantity for local regions in QFT.

## Key Papers

| Paper | Journal | arXiv | Year |
|-------|---------|-------|------|
| Numerical analysis of Araki-Uhlmann relative entropy (coherent states, (1+1)d) | Nucl. Phys. B 1018 | 2502.09796 | 2025 |
| Relative entropy of squeezed states | Eur. Phys. J. C 85 | 2504.13148 | 2025 |
| Relative entropy between two coherent states | Eur. Phys. J. C 85 | 2508.17165 | 2025 |
| Mass dependence of relative entropy across dimensions | preprint | 2511.20244 | 2025 |
| [[2025-liu-lectures-entanglement-vna\|Lectures on entanglement, von Neumann algebras, and emergence of spacetime]] (review) | preprint | 2510.07017 | 2025 |

*General reference:* xiyin-qft-monograph — Vols I (AQFT axioms), X (KMS/thermal states), and XII (Unruh effect, locally covariant QFT, Hadamard states) for the modular-theory background.

## Connections

- **[[bell-inequalities-qft]]**: This line is a direct outgrowth of the Bell inequality program; the same [[weyl-operators|Weyl operator]] and [[tomita-takesaki-modular-theory|modular theory]] machinery is applied here. The 2025 papers on relative entropy emerged from the same collaboration that produced the 2023–2024 Bell-CHSH results.
- **[[type-iii-algebras-across-areas]]**: The [[type-iii-von-neumann-algebras|type III₁ algebra]] structure is the algebraic foundation for why relative entropy (rather than von Neumann entropy) is the right quantity in QFT, connecting this area to the broader algebraic QFT framework used across multiple research lines.
- **[[entanglement-probes-of-phases]]**: Relative entropy is a natural candidate probe of quantum phase transitions, including the confinement/deconfinement transition in gauge theories. See [[entanglement-as-confinement-probe]].
- **[[condensed-matter-qft-bridge]]**: Araki-Uhlmann relative entropy has appeared in the many-body and condensed matter literature as well (e.g., in the context of quantum thermodynamics and resource theories), providing a bridge to [[condensed-matter-connections]].
- **[[wormholes-and-quantum-information-qft]]**: The Gao–Jafferis–Wall coupling that opens a [[traversable-wormholes|traversable wormhole]] is a Connes-cocycle perturbation of the [[thermofield-double-state|TFD]] — the same object computed here — making [[relative-entropy-wormhole-opening|the relative entropy of wormhole opening]] a directly tractable extension of the program (motivated by [[2021-kundu-wormholes-holography|Kundu's review]]).
- **[[gravity-qi-open-problems]]**: [[2026-goto-rethinking-qi-gravity-fields|Goto et al.]] call for "quantum information theory in infinite-dimensional Hilbert spaces" (their Theme 4); the finite Araki-Uhlmann relative entropy computed here — well-defined precisely where von Neumann entropy diverges — is a concrete piece of exactly that program.

### Collaborators

- [[silvio-paolo-sorella]] ([[uerj]]) — co-author of all papers
- [[itzhak-roditi]] ([[cbpf]]) — co-author of all papers
- [[leticia-palhares|Arthur F. Vieira]] ([[uerj]]) — co-author of all relative entropy papers
- ismael-porfirio ([[uerj]]) — PhD student; embezzlement and type III₁ algebras
- erick-landim ([[uerj]]) — PhD student; von Neumann algebras, embezzlement, many-body theory
