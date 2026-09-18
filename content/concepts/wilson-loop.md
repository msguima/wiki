---
title: Wilson Loop
type: concept
areas: [confinement-duality]
aliases: [Wilson loops, Wilson line, "'t Hooft loop", Polyakov loop]
modified: 2026-07-01
---

## Definition

The **Wilson loop** is the gauge-invariant trace of the parallel transport around a closed curve $C$,
$$W_r(C) = \mathrm{tr}_r\, \mathcal{P}\exp\!\Big(i\oint_C A\Big) = \mathrm{tr}_r \prod_{\ell\in C} U_\ell,$$
in representation $r$ of the gauge group. It is the order parameter that survives Elitzur's theorem: since no local gauge-variant operator can acquire a vacuum expectation value, the diagnostics of gauge theory must be extended and gauge-invariant.

Its behavior classifies the phase through the response to the loop's geometry:

- **Area law** $\langle W(C)\rangle \sim e^{-\sigma\,\mathrm{Area}(C)}$ — confinement, with string tension $\sigma$; the quark–antiquark potential is linear, $V(R) = \sigma R$.
- **Perimeter law** $\langle W(C)\rangle \sim e^{-\mu\,\mathrm{Perim}(C)}$ — deconfinement / Coulomb or Higgs phase.

Companion operators: the **'t Hooft loop** (a disorder operator creating magnetic flux, supported on the dual lattice) and the **Polyakov loop** (a Wilson line wrapping the thermal time circle, whose expectation value is the finite-temperature deconfinement order parameter).

## Role in Research

In the modern reading developed in the generalized-symmetries course, the Wilson loop is the charged object of a 1-form symmetry, and its area/perimeter dichotomy is the statement that the 1-form [[higher-form-symmetries|symmetry]] is unbroken (confined) or spontaneously broken (deconfined). This reframing is what connects the group's historical [[confinement-duality]] work to the current higher-gauging program.

- The Wilson-loop area law is computed directly in the strong-coupling expansion of [[lattice-gauge-theory]].
- Its dual, the 't Hooft loop, is the order parameter for the magnetic symmetry condensed in the [[dual-superconductor]].
- When a Wilson line of charge $q$ crosses a [[condensation-defects|condensation defect]], its fate (intact, screened, or ending on the wall) is fixed by the annihilator arithmetic of the group's Julia–Toulouse construction.

## Relations

- [[lattice-gauge-theory]] — the setting where area/perimeter laws are computed
- [[higher-form-symmetries]] — the Wilson loop is the charged line of a 1-form symmetry
- [[confinement]] — the area law is the defining signal of confinement
- [[dual-superconductor]] — the 't Hooft loop is the disorder operator dual to the Wilson loop
- [[condensation-defects]] — endpoint rules for Wilson lines crossing a higher-gauging wall

## Papers

Wilson (1974) introduced the loop and the confinement criterion; 't Hooft, Nucl. Phys. B 138 (1978) 1, introduced the disorder loop and the electric/magnetic flux classification. See [[confinement-duality]].

## Notes

- With dynamical charges in the fundamental representation the area law is destroyed by string breaking — the Wilson criterion fails, which is exactly why the Fradkin–Shenker Higgs and confining regions are analytically connected.
- The Wilson loop was flagged as a needed concept page by cross-references in [[entanglement-probes-of-phases]] and related question pages; this page fills that gap.
- "Wilson line" (open) vs "Wilson loop" (closed): the open line is gauge-variant and only becomes a genuine operator when its endpoints carry compensating charges or attach to defects.
