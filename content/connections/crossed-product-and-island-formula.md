---
title: "Crossed product and the island formula"
type: connection
areas: [relative-entropy-qft, gauge-gravity-duality]
maturity: developing
modified: 2026-05-26
---

## The Link

Both the [[crossed-product-construction|crossed product]] (CPW, Witten 2022) and the **island formula** ([[quantum-extremal-surfaces]], Penington 2019; AEMM 2019) are mechanisms for producing a *finite, geometrically meaningful entropy* from a type III₁ algebra that has no intrinsic notion of trace or density matrix. The crossed product does this by *dressing* the algebra by its modular flow, promoting it to type II$_\infty$ and introducing a faithful semifinite trace whose entropy reproduces the generalised gravitational entropy $A/(4G_N) + S_{\text{out}}$. The island formula does this by *enlarging the entanglement wedge* of the radiation to include an island in the interior of the black hole, so that the QES prescription gives a Page-curve-compatible entropy. Liu's 2025 review and the recent AAJ work (arXiv:2501.01487) make the relation between these two mechanisms explicit at the algebraic level.

## Evidence

- **CPW** (Chandrasekaran-Penington-Witten 2022, arXiv:2209.10454) derives the generalised entropy from the crossed-product trace on the two-sided eternal AdS-Schwarzschild background dual to a thermofield-double state, in the large-$N$ regime where the single-trace algebra is type III₁.
- **AAJ** (Ahmad-Jefferson 2024/2025, arXiv:2501.01487) develops cocycle perturbation theory on the crossed-product algebra, including the Gao-Jafferis-Wall double-trace deformation — establishing that crossed-product entropies *do* receive the corrections that traversable-wormhole perturbations would produce in the bulk.
- **Liu's lectures** (arXiv:2510.07017) present the crossed product and the QES / island formula as two complementary entry points to the same physics, with the algebraic side providing structural understanding and the geometric side providing computational power.

## Gaps

- The island formula's derivation goes through Euclidean replica wormholes ([[replica-trick-gravity]]); the crossed product is a Lorentzian, algebraic construction. The relation between the two computational frameworks is understood only in special cases (one- and two-sided BHs, JT gravity).
- For evaporating black holes, the island formula is established but the crossed-product construction has not yet been carried out in full algebraic detail.
- The role of bulk-matter fields (vs. pure gravity) in the crossed-product side is subtle and only partially worked out.

## Potential Projects

- Apply AAJ cocycle perturbation theory to an island-formula calculation in JT gravity: verify that the leading correction to $S_{\text{gen}}$ matches the GJW double-trace deformation result.
- Extend the crossed-product construction to a one-sided evaporating BH; identify which step requires new input vs. which is automatic from the AAJ machinery.

## Related

- [[crossed-product-construction]]
- [[quantum-extremal-surfaces]]
- [[page-curve]]
- [[replica-trick-gravity]]
- [[araki-uhlmann-relative-entropy]]
- [[2025-liu-lectures-entanglement-vna]]
- [[gauge-gravity-duality]]
- [[type-iii-algebras-across-areas]]
