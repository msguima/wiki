---
title: Mermin Inequalities
type: concept
areas: [bell-inequalities-qft]
aliases: [Mermin inequality, multipartite Bell inequalities, Mermin-GHZ inequality]
modified: 2026-10-15
---

## Definition

**Mermin inequalities** are multipartite generalizations of the [[bell-chsh-inequality|Bell-CHSH inequality]] for $N \geq 3$ parties, designed to detect **genuine multipartite entanglement** — entanglement that cannot be decomposed into bipartite correlations.

For $N = 3$ parties (Alice, Bob, Charlie) each performing one of two measurements with outcomes $\pm 1$, the Mermin inequality takes the form

$$M_3 = \langle A_1 B_1 C_2\rangle + \langle A_1 B_2 C_1\rangle + \langle A_2 B_1 C_1\rangle - \langle A_2 B_2 C_2\rangle.$$

**Classical bound** (local hidden-variable theories): $|M_3| \leq 2$.

**Quantum bound** (Tsirelson-type): $|M_3| \leq 4$, achieved by the GHZ state $|\text{GHZ}\rangle = \frac{1}{\sqrt{2}}(|000\rangle + |111\rangle)$.

For general $N$ the Mermin operator involves $2^{N-1}$ correlator terms, and the local bound depends on the parity of $N$:

- Classical: $|M_N| \leq 2^{(N-1)/2}$ for $N$ odd, $|M_N| \leq 2^{N/2}$ for $N$ even.
- Quantum: $|M_N| \leq 2^{N-1}$ for $N$ odd, $2^{N-1/2}$ for $N$ even.

Either way the quantum maximum exceeds the local bound by a factor $2^{(N-1)/2}$, which is the exponential gap. For even $N$ reaching it needs the Ardehali–Klyshko form of the inequality rather than Mermin's original one, which is weaker there; the whole family is often cited as Mermin–Ardehali–Belinskii–Klyshko. At $N=2$ the bounds reduce to the CHSH pair, $2$ and $2\sqrt2$.

In the QFT setting, the multipartite scenario is set up with $N$ causally separated spacetime regions, each associated with a [[type-iii-von-neumann-algebras|type III₁]] local algebra. Dichotomic observables are again constructed from [[weyl-operators|Weyl operators]] in each region.

## Role in Research

The extension from bipartite [[bell-chsh-inequality|Bell-CHSH]] to multipartite Mermin inequalities was achieved in Phys. Rev. D 109, 045020 (2024), which shows that the Mermin inequality is violated in the vacuum of a scalar field across three (and more) causally separated Rindler-wedge regions.

The main results:

- Explicit computation of the Mermin correlator for the free scalar field vacuum in multiple Rindler wedges, using the [[weyl-operators|Weyl operator]] framework.
- Demonstration that the classical bound is violated, establishing genuine 3-partite entanglement in the QFT vacuum.
- The violation is mass-dependent: it decreases as $m \to \infty$ (massive fields are less entangled at large spacelike separations) and approaches its maximum in the massless limit.
- The construction uses the same [[tomita-takesaki-modular-theory|Tomita-Takesaki modular theory]] infrastructure as the bipartite CHSH case, with modular conjugation providing the mapping between algebras of different wedges.

This work establishes that vacuum entanglement in QFT is not merely bipartite but has a richer multipartite structure that Mermin inequalities can probe.

## Relations

- [[bell-chsh-inequality]] — the $N=2$ special case; Mermin inequalities are the direct multipartite generalization using the same Weyl operator dichotomic observables
- [[weyl-operators]] — the same construction (Weyl operators as dichotomic observables in each wedge) is used; the multipartite structure enters through the product structure of the correlators
- [[tomita-takesaki-modular-theory]] — modular conjugation provides the mapping between different wedge algebras needed for the multi-party construction
- [[rindler-wedges]] — $N$ causally separated Rindler-type regions provide the multipartite causal split; for $N \geq 3$ one uses multiple wedge-like regions or combinations of wedges and their causal complements
- [[type-iii-von-neumann-algebras]] — each local algebra is type III₁; genuine multipartite entanglement is a feature of the algebraic structure

## Papers

See [[bell-inequalities-qft]] for full paper list.

## Notes

- The Mermin inequality was introduced by Mermin in 1990 as a way to extend Bell's argument to three qubits. The GHZ (Greenberger-Horne-Zeilinger) state maximally violates it. The original paper by Mermin is often cited alongside the GHZ paper.
- The multipartite structure of vacuum entanglement in QFT is not merely a curiosity: it reflects the fact that the vacuum is a highly correlated state in which no finite subregion is "independent" of its environment.
- Common confusion: a Mermin violation does **not** by itself certify genuine $N$-partite non-locality. Hybrid models in which some parties share non-local correlations while the rest stay local can reproduce it, and ruling those out is what the Svetlichny inequality does. What a violation does establish is that the correlations are not fully local, and in the QFT setting that they extend across all $N$ regions at once.
- The exponential quantum-classical gap in Mermin inequalities ($2^{N-1}$ vs $2^{(N-1)/2}$) makes them exponentially more powerful than CHSH for certifying multipartite entanglement as $N$ grows.
