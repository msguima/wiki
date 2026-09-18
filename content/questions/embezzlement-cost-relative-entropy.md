---
title: What is the cost of entanglement embezzlement quantified via relative entropy?
type: question
status: open
areas:
  - bell-inequalities-qft
  - relative-entropy-qft
priority: high
originated: 2026-04-06
---

## Statement

Entanglement embezzlement in [[type-iii-von-neumann-algebras]] refers to the ability to extract entanglement from a catalyst state without degrading it — a feature that is exact (not approximate) precisely because type III₁ algebras have no minimal entanglement. But "no cost" is a statement about state fidelity, not about all information-theoretic quantities. What is the cost of embezzlement when measured by [[araki-uhlmann-relative-entropy]]? Is there a relative-entropy lower bound on the disturbance caused to the catalyst state by an embezzlement protocol constructed from [[weyl-operators]] in relativistic QFT?

## Why It Matters

The type III₁ structure of local von Neumann algebras in relativistic QFT — established by the [[bisognano-wichmann-theorem]] and Connes's structure theorem — implies that ideal entanglement embezzlement is possible in the strict algebraic sense. This has been recognized as a fundamental feature distinguishing QFT from finite-dimensional quantum information. However, the operational content of "no cost" depends critically on the distance measure used. In finite dimensions, embezzlement has a well-defined cost in terms of fidelity loss, and relative entropy is the operationally preferred measure (it controls hypothesis testing error exponents via the [[quantum-stein-lemma]]).

Computing the relative entropy cost of specific embezzlement protocols in QFT would:
1. Provide a quantitative, operationally meaningful measure of the type III₁ "resource."
2. Connect the abstract algebraic fact (type III₁ allows exact embezzlement) to a computable number using the tools already developed for [[araki-uhlmann-relative-entropy]] in free-field QFT.
3. Clarify what aspect of the QFT vacuum structure makes embezzlement possible, potentially linking it to the [[tomita-takesaki-modular-theory|modular Hamiltonian]] and [[tomita-takesaki-modular-theory]].

This is actively being pursued by ismael-porfirio and erick-landim within the group.

## What We Know

**Type III algebras and embezzlement:**
- Local algebras of bounded regions in relativistic QFT are [[type-iii-von-neumann-algebras]] of the hyperfinite type III₁ factor (under standard assumptions). This was established by Haag, Hugenholtz, and Winnink; made precise by Connes; and given physical content by [[bisognano-wichmann-theorem]].
- Type III₁ algebras have no minimal projections and no trace, so the notion of "degradation" used in finite-dimensional embezzlement (which requires a finite-dimensional density matrix) does not directly apply.
- The [[van-dam-hayden]] embezzlement protocol and its generalizations require a catalyst state drawn from an infinite-dimensional family; in QFT, such states are naturally available from the type III₁ structure.

**Relative entropy in free QFT (what is established):**
- [[araki-uhlmann-relative-entropy]] between coherent states and the vacuum in (1+1)d: closed-form expression proportional to the smeared [[pauli-jordan-distribution]] (Nucl. Phys. B 1018, 2025).
- Relative entropy of single-mode squeezed states above the vacuum: closed form (Eur. Phys. J. C 85, 2025).
- Relative entropy between two coherent states in spacelike separated diamond regions: linear increase with spatial separation, decreasing with mass (Eur. Phys. J. C 85, 2025).
- Mass and dimension dependence systematically studied (arXiv:2511.20244).

**Gap:** No embezzlement protocol has yet been explicitly constructed in the [[weyl-operators|Weyl operator formalism]], and no relative entropy cost has been computed for any such protocol.

## Possible Approaches

1. **Explicit protocol construction**: Use [[weyl-operators]] W(f) localized in Rindler wedges to construct a unitary that transfers entanglement from the vacuum to an auxiliary system. The natural candidate is a unitary built from the [[tomita-takesaki-modular-theory]] unitaries $\Delta^{it}$, which are defined intrinsically by the vacuum. Compute the relative entropy between the pre- and post-protocol catalyst states using the Araki formula.

2. **Relative modular operator approach**: The relative entropy $S(\omega||\varphi) = -\langle \Omega, \log \Delta_{\Phi,\Omega} \Omega \rangle$ is expressed directly in terms of the relative modular operator $\Delta_{\Phi,\Omega}$. If the post-protocol state $\Phi$ is close to the vacuum $\Omega$ in some sense, first-order perturbation theory in the modular operator may give an analytic handle on the cost.

3. **Lower bound from data processing**: Use the data-processing inequality for relative entropy together with the known relative entropy between coherent states (already computed) to bound the cost of any embezzlement protocol that produces a coherent state output. This would give a lower bound without specifying the protocol.

4. **Many-body / thermodynamic limit**: In the [[van-dam-hayden]] approach, cost vanishes in the limit of an infinitely large catalyst. Compute how fast the relative entropy cost decreases as the catalyst system size (regulated by a UV cutoff or finite volume) grows, and determine whether the type III₁ limit is approached from above or below.

5. **Connection with modular Hamiltonian**: Since $\log \Delta_\Omega = -K_\Omega$ where $K_\Omega$ is the [[tomita-takesaki-modular-theory|modular Hamiltonian]], the relative entropy of an embezzlement protocol's output state relative to the vacuum is expressible as an expectation value of the modular Hamiltonian. For Rindler wedges, this is related to the Rindler energy (boost generator), giving a physical interpretation of the cost.

## Related Questions

- [[entanglement-as-confinement-probe]] — Relative entropy as a phase-transition probe; shares the relative entropy toolkit
- [[relative-entropy-interacting-theories]] — The embezzlement cost question in interacting theories requires computing relative entropy beyond free fields
- [[bell-inequalities-with-gribov-horizon]] — Related use of algebraic QFT tools in gauge-theory context
- [[impossible-measurements-qft]] — Operational limitations on measurements bound what embezzlement protocols are physically realizable
