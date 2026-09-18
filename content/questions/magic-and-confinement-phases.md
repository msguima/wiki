---
title: Is magic an order parameter for confinement and higher-form symmetry realization?
type: question
status: open
areas: [confinement-duality, condensed-matter-connections, relative-entropy-qft]
priority: medium
originated: 2026-07-21
---

## Statement

[[2026-benedetti-magic-in-qft|Benedetti–Dabholkar–Dalmonte]] show that [[magic-nonstabilizerness|magic]] sharply separates **local QFT** (necessarily magical, a net of [[type-iii-von-neumann-algebras|type III₁]] factors) from **TQFT** (can be a flat-spectrum stabilizer state — the [[toric-code|toric code]] is the paradigm, $Z[\mathcal{M}_n]=(Z[\mathcal{M}_1])^n D^{n-1}$). Since a deconfined gauge theory flows in the deep IR to a topological description while a confining one does not, **does the magic of the ground state behave as an order parameter across the confinement/deconfinement transition — and does it track the realization vs. breaking of the relevant [[higher-form-symmetries|higher-form symmetry]]?**

## Why It Matters

This lifts the paper's TQFT-vs-local-QFT boundary into the group's [[confinement-duality|confinement]] and generalized-symmetries programs, and connects three of its threads at once. Confinement is now understood as the (un)realization of a [[higher-form-symmetries|1-form symmetry]] (Wilson-line area vs. perimeter law); topological order is a flat-spectrum / low-magic regime; and [[entanglement-as-confinement-probe|entanglement has already been proposed]] as a confinement diagnostic. If magic drops in the deconfined/topological phase and is non-zero (or peaks) across the transition, it would be a **genuinely new, complexity-flavored order parameter** — distinct from the Wilson/'t Hooft loops and from entanglement entropy — with a clean many-body implementation. It also sharpens *why* topological phases are classically simulable (low magic) while genuine QFT phases are not.

## What We Know

- **Magic distinguishes the phases algebraically.** The flat-spectrum (stabilizer) sector is exactly the topological one in the paper's analysis, because TQFT is not a net of type III₁ factors. See [[magic-nonstabilizerness]], [[topological-order]], [[string-net-condensation]].
- **Lattice magic diagnostics exist.** Stabilizer Rényi entropy and anti-flatness have been computed across criticality and in gauge theories on the lattice (Tarabunga–Tirrito–Dalmonte 2023; Dalmonte is a co-author of the QFT paper) — the [[condensed-matter-qft-bridge|condensed-matter bridge]] makes these directly usable.
- **Higher-form-symmetry framing is in place.** The wiki already tracks confinement as [[higher-form-symmetries|higher-form symmetry]] realization and the [[wilson-loop|Wilson loop]] as the charged line; magic would be a state-property complement to these operator diagnostics.
- **Gribov-side sibling.** The closely-related question of whether the *specific* RGZ vacuum's magic differs is [[magic-and-the-gribov-horizon]]; this question is the broader phase-diagram / symmetry-realization framing.

## Possible Approaches

1. **Lattice gauge theory scan.** Compute the stabilizer Rényi entropy / anti-flatness of the ground state of a $\mathbb{Z}_N$ or $SU(N)$ lattice gauge theory across the confinement/deconfinement transition (Dalmonte-style Pauli–Markov sampling), and correlate with the Wilson-loop law.
2. **Toric code as the deconfined anchor.** Use the exactly-solvable [[toric-code|toric code]] / deconfined $\mathbb{Z}_2$ phase (zero magic, flat spectrum) as the reference, and perturb toward the confined phase to watch magic turn on.
3. **Higher-form order-parameter correspondence.** Ask whether the onset of magic coincides with the restoration of the 1-form symmetry (perimeter→area law), making the correspondence "magic ↔ 1-form symmetry realization" precise.
4. **Continuum reading.** Interpret the lattice result through the paper's algebraic lens: does approaching the topological IR correspond to the local algebra degenerating away from type III₁?

## Related Questions

- [[entanglement-as-confinement-probe]] — the parent question on entanglement/Bell as confinement order parameters.
- [[magic-and-the-gribov-horizon]] — the Gribov-vacuum-specific version.
- [[julia-toulouse-higher-form-symmetries]], [[non-invertible-symmetries-mcs]] — the generalized-symmetries context.
- [[magic-of-coherent-squeezed-cat-states]] — the free-field magic computation on the QFT side.
