---
title: Bell-CHSH Inequality
type: concept
areas: [bell-inequalities-qft]
aliases: [CHSH inequality, Bell inequality, Tsirelson bound]
modified: 2026-04-06
---

## Definition

Consider a bipartite scenario with two parties (Alice and Bob) each performing one of two measurements. Alice's observables $A_1, A_2$ and Bob's observables $B_1, B_2$ are Hermitian operators with eigenvalues in $\{-1, +1\}$ (dichotomic). The **CHSH combination** is

$$\mathcal{C} = \langle A_1 B_1\rangle + \langle A_1 B_2\rangle + \langle A_2 B_1\rangle - \langle A_2 B_2\rangle.$$

**Classical (local hidden-variable) bound:** $|\mathcal{C}| \leq 2$. This follows from the assumption that outcomes are determined by hidden variables $\lambda$ with local statistics: $|A_i(\lambda)B_j(\lambda)| \leq 1$ implies $|\mathcal{C}| \leq 2$ by triangle inequality.

**Tsirelson bound:** In quantum mechanics, $|\mathcal{C}| \leq 2\sqrt{2} \approx 2.828$. This is a tight bound, achieved by the singlet state with optimal measurement settings.

In **quantum field theory**, the dichotomic operators are not spin operators but bounded functions of field operators. A natural choice is $A_1 = W(f_1) + W(f_1)^\dagger$ and $A_2 = i(W(f_1) - W(f_1)^\dagger)$ built from a [[weyl-operators|Weyl operator]], which are unitaries with spectrum on the unit circle — one must work with their real and imaginary parts or more refined bounded operators with $\|A\| \leq 1$. The key result (Phys. Rev. D 108, 085026; 2023) shows that for the free scalar field vacuum in Rindler wedges, the CHSH combination can reach the Tsirelson bound.

## Role in Research

Bell-CHSH violations in QFT are the central object of study in the [[bell-inequalities-qft]] research line, which has produced 21+ publications since 2023.

Key results:

- **Maximal violation (Tsirelson bound)** achieved for massless spinors using bumpified Haar wavelets as test functions (Phys. Rev. D 108, L081701; 10 citations). The bound $2\sqrt{2}$ is saturated, confirming the QFT vacuum saturates quantum information limits.

- **Systematic Weyl + Tomita-Takesaki framework** (Phys. Rev. D 108, 085026; 15 citations): Alice's observables are Weyl operators in the right [[rindler-wedges|Rindler wedge]]; Bob's are obtained via [[tomita-takesaki-modular-theory|modular conjugation]] $J$, which maps $\mathcal{M}(R)$ to $\mathcal{M}(L)$.

- **BRST-invariant Bell-CHSH in gauge theories** (SciPost Phys. 15, 2023): First formulation compatible with [[brst-symmetry|BRST symmetry]], necessary for working in gauge-fixed non-abelian Yang-Mills theory.

- **Extension to [[causal-diamonds|causal diamonds]]** (Eur. Phys. J. C 85, 2025): Goes beyond the infinite Rindler wedge to compact diamond regions, which are more physically accessible.

- **[[cat-states|Cat states]]** (Phys. Rev. D 113, 065008; 2026): Superpositions of coherent states produce Bell violations with new interference-driven features.

- **Mass and dimension dependence**: The violation generically exceeds 2 for any non-zero mass, with the maximum 2√2 approached in the massless limit for certain test functions.

## Relations

- [[weyl-operators]] — the dichotomic observables used in QFT Bell tests are constructed from Weyl operators; the closed-form vacuum expectation values make the CHSH correlator computable
- [[tomita-takesaki-modular-theory]] — modular conjugation $J$ maps Alice's wedge algebra to Bob's, providing a systematic construction of the bipartite setup
- [[rindler-wedges]] — the standard causal regions for the bipartite split in QFT Bell tests; complementary wedges R and L are spacelike separated
- [[causal-diamonds]] — compact alternative to Rindler wedges; important for realistic experimental relevance
- [[mermin-inequalities]] — multipartite generalization to three or more parties; uses the same Weyl operator machinery
- [[type-iii-von-neumann-algebras]] — the type III₁ structure of local algebras guarantees existence of cyclic separating states and underlies the embezzlement connection
- [[coherent-states]], [[squeezed-states]], [[cat-states]] — excited states for which CHSH violations are computed explicitly and compared with the vacuum result
- [[brst-symmetry]] — in gauge theories, Bell observables must respect BRST invariance to be physical

## Papers

See [[bell-inequalities-qft]] for full paper list.

## Notes

- The CHSH combination is named after Clauser, Horne, Shimony, and Holt (1969). Bell's original 1964 inequality is slightly different; CHSH is the standard form for bipartite two-setting experiments.
- In the QFT setting, Alice and Bob's measurement regions must be **spacelike separated** (or at least causally disjoint) for the Bell inequality to be physically meaningful. The locality assumption is automatic from microcausality.
- Common confusion: the Tsirelson bound $2\sqrt{2}$ is not achievable in all quantum states or with all observables — it requires optimization over measurement operators. In QFT, reaching it requires specific test function choices.
- The question of whether Bell violations in gauge theories are modified by the [[gribov-horizon|Gribov horizon]] is an open problem; see [[bell-inequalities-qft]] open problems.
