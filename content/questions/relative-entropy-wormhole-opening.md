---
title: What is the Araki-Uhlmann relative entropy of opening a traversable wormhole?
type: question
status: open
areas: [relative-entropy-qft, gauge-gravity-duality]
priority: medium
originated: 2026-06-04
---

## Statement

The Gao–Jafferis–Wall double-trace deformation $V = g\,\mathcal{O}_L\mathcal{O}_R$ that makes the eternal-black-hole wormhole [[traversable-wormholes|traversable]] is a **Connes-cocycle perturbation** of the [[thermofield-double-state|thermofield double]] modular flow (made explicit by Ahmad–Jefferson). The group already computes [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] $S(\omega\|\varphi) = -\langle\Omega,\log\Delta_{\Phi,\Omega}\,\Omega\rangle$ in closed form for free-field states. **Question:** in a free-field two-[[rindler-wedges|wedge]] analogue of the TFD, perturbed by $V = g\,W(f_L)W(f_R)$, what is the relative entropy $S(\omega_V\|\omega)$ between the deformed and undeformed states to $O(g^2)$, and can it be read as the "cost of opening the throat"?

## Why It Matters

- It turns the wormhole-traversability story into a calculation the group can actually do, using exactly the [[weyl-operators|Weyl operator]] + cocycle machinery of the [[relative-entropy-qft|relative-entropy program]] and AQFT course Sem I Wk 7 / Sem II Wk 12.
- It would give an **information-theoretic meaning to traversability**: relative entropy measures distinguishability between the open-throat and closed-throat states, and its $g$-dependence quantifies how far the deformation pushes the state.
- It is the controlled, flat-space mirror of Ahmad–Jefferson's holographic generalized-entropy corrections — a way to separate the **algebraic** content (which the group owns) from the **holographic** content (taken on trust). See [[wormholes-and-quantum-information-qft]] (project P1).

## What We Know

- For a single [[coherent-states|coherent state]] $W(f)|0\rangle$, $S(\omega_f\|\omega_0) \propto \Delta(f,f)$, the smeared [[pauli-jordan-distribution|Pauli–Jordan distribution]] (Nucl. Phys. B 1018, 2025). The two-coherent-state and squeezed-state cases are also closed-form.
- The Connes cocycle $(D\omega_V/D\omega)_t$ has a known perturbative expansion (Sem I Wk 7; Ahmad–Jefferson §2–3). The first non-trivial relative-entropy correction is $O(g^2)$ because the $O(g)$ term is a one-point function that vanishes by symmetry for a suitable $V$.
- The Bisognano–Wichmann identification (vacuum on two wedges = TFD at the Unruh temperature) guarantees the free-field analogue is a faithful model of the boundary modular data.

## Possible Approaches

1. **Direct cocycle expansion.** Expand $\log\Delta_{\Phi_V,\Omega}$ in $g$ using the cocycle series; the bilinear Weyl perturbation $V = g\,W(f_L)W(f_R)$ keeps every term a Gaussian integral against the two-point/Pauli–Jordan data, so the $O(g^2)$ coefficient should be a double smearing of $\Delta$ and the Wightman function.
2. **Reuse the squeezed-state technology.** $W(f_L)W(f_R)$ acting on the TFD is closely related to a two-mode squeezing of the wedge pair; the existing squeezed-state relative-entropy result (EPJC 85, 2025) may port over with the modular data of the wedge replacing the single-mode Bogoliubov coefficients.
3. **Cross-check numerically.** The group's (1+1)d numerical framework (Nucl. Phys. B 1018) can validate the analytic $O(g^2)$ coefficient and explore the mass / wedge-separation dependence — the same knobs already mapped for coherent states.

## Related Questions

- [[bell-chsh-across-traversable-wormhole]] — the Bell-CHSH counterpart of the same deformation.
- [[relative-entropy-interacting-theories]] — the GJW $\mathcal{O}_L\mathcal{O}_R$ coupling is the kind of interaction that motivates going beyond free fields.
- [[embezzlement-cost-relative-entropy]] — relative entropy as the cost measure for type III$_1$ resource manipulation.

Tracked under the [[wormholes-and-quantum-information-qft]] connection.
