---
title: How do Gribov copies manifest in gauge-invariant observables?
type: question
status: open
areas:
  - gribov-zwanziger
priority: low
originated: 2026-04-06
---

## Statement

In non-abelian gauge theories, [[gribov-copies]] are distinct gauge field configurations that are related by gauge transformations and satisfy the same gauge condition (e.g., Landau gauge $\partial_\mu A^\mu = 0$). The Faddeev-Popov quantization procedure overcounts, and the [[gribov-zwanziger]] framework corrects this by restricting to the first [[gribov-horizon|Gribov region]] Ω. But physically observable quantities must be gauge-invariant. The question is: do different prescriptions for handling Gribov copies — restricting to Ω, restricting to the fundamental modular region, or using other gauges — give identical results for gauge-invariant observables? And if not, which prescription is correct, and why?

## Why It Matters

This is a foundational question for the entire Gribov-Zwanziger program. The standard argument is that physical observables are gauge-invariant and hence insensitive to the gauge-fixing prescription, so Gribov copies are "irrelevant" for physics. This argument works in perturbation theory (where Gribov copies are exponentially suppressed at high energies) but fails non-perturbatively. There are two known cases where Gribov copies do affect gauge-invariant quantities:

1. **Vacuum energy**: Different Gribov regions contribute with different weights to the functional integral, shifting the vacuum energy. The [[zwanziger-horizon-function]] acts as a deformation of the vacuum that changes the value of gauge-invariant condensates.
2. **Spectral functions of composite operators**: Even for gauge-invariant composite operators $O = \text{tr}(F_{\mu\nu}F^{\mu\nu})$ or $O = \bar\psi \psi$, the spectral function depends on the gauge-fixing procedure through loop corrections, as established in arXiv work with Dudal and collaborators (Eur. Phys. J. C 81, 2021).

Understanding precisely which gauge-invariant observables carry Gribov dependence — and by how much — is essential for:
- Connecting [[gribov-zwanziger]] predictions to lattice measurements.
- Determining whether entanglement and Bell-inequality measures (which depend on the vacuum state) are Gribov-sensitive.
- Resolving the question of whether the [[refined-gribov-zwanziger]] framework is a genuine improvement over Faddeev-Popov quantization at the level of physical predictions.

## What We Know

**The Gribov problem — basics:**
- In Landau gauge, the [[faddeev-popov-operator]] $-\partial_\mu D^\mu$ has zero modes at the [[gribov-horizon]] $\partial\Omega$. The standard Faddeev-Popov determinant vanishes there, invalidating the perturbative gauge-fixing.
- Gribov's original proposal (1978) restricts the functional integral to the first Gribov region Ω, where the Faddeev-Popov operator is positive definite. But Ω is not free of gauge copies either — there exist copies within Ω.
- The smallest copy-free region is the **fundamental modular region** Γ ⊂ Ω, defined by the absolute minimum of $\|A\|^2 = \int d^dx A_\mu^a A_\mu^a$ along each gauge orbit. Computing functional integrals over Γ is not feasible analytically.

**Established results on gauge-invariant quantities:**
- Glueball mass estimates from the RGZ propagators via Padé approximation (Phys. Lett. B 732, 2014) depend on the [[gribov-zwanziger|Gribov parameter]] $\gamma$ — they change when Ω-restriction is applied vs. Faddeev-Popov. This is a gauge-invariant quantity (glueball masses are physical) that is explicitly Gribov-dependent in the approximation scheme.
- [[spectral-positivity-violation|spectral positivity]] violation of the gluon propagator (a gauge-dependent quantity) is thought to be a necessary condition for confinement of gluons. The relationship between this gauge-dependent signal and gauge-invariant confinement criteria (Wilson loop area law) is not fully established.
- The [[brst-symmetry]] of the GZ action in linear covariant gauges (Phys. Rev. D 92, 2015) guarantees that the BRST cohomology (physical sector) is gauge-fixing independent at the formal level, but this relies on the existence of the nilpotent BRST charge, which may be ill-defined when the [[gribov-horizon]] is present.

**Nielsen identities:**
- [[nielsen-identities]] express the gauge-parameter independence of physical correlators. They have been derived in the GZ framework (Phys. Rev. D 95, 2017), but their validity requires the BRST symmetry to be exact — which it is in the linear-covariant-gauge formulation of GZ, but not in all gauges.

## Possible Approaches

1. **Lattice comparison across gauges**: Compute physical observables (string tension, glueball masses, hadron spectrum) on the lattice in Landau gauge, Coulomb gauge, and maximal Abelian gauge, with and without Gribov copy restriction. This is technically accessible and directly tests whether the prescription matters.

2. **Stochastic quantization**: In Zwanziger's stochastic quantization approach, the restriction to the Gribov horizon emerges naturally as a boundary condition on the Langevin equation, without requiring a gauge-fixing prescription. Physical observables are then defined without reference to a specific gauge. Comparing stochastic quantization results with RGZ results for gauge-invariant quantities tests the prescription independence.

3. **Operator product expansion analysis**: The OPE for composite gauge-invariant operators like $\text{tr}(F^2)$ receives corrections proportional to the dimension-two condensate $\langle A^2 \rangle$, which is itself gauge-dependent. However, its effect on gauge-invariant OPE coefficients can be tracked using the [[brst-symmetry|BRST Ward identities]] to determine whether any physical residue remains.

4. **Entanglement and Bell measures as probes**: If Bell-CHSH violations or relative entropy computed in the RGZ vacuum differ from those in the Faddeev-Popov vacuum, this provides a direct signal that Gribov copies affect quantum information measures — which are formally gauge-invariant when constructed from BRST-invariant operators. This connects to [[bell-inequalities-with-gribov-horizon]] and [[entanglement-as-confinement-probe]].

5. **Algebraic construction of gauge-invariant algebra**: Use the [[brst-symmetry|BRST cohomology]] to systematically identify the algebra of gauge-invariant observables within the RGZ framework. Determine which operators have expectation values that depend on $\gamma$ (the Gribov mass) and which are $\gamma$-independent. Any $\gamma$-dependent gauge-invariant observable is a signal that Gribov copies matter physically.

## Related Questions

- [[bell-inequalities-with-gribov-horizon]] — Bell correlators as gauge-invariant (BRST-invariant) observables sensitive to Gribov structure
- [[entanglement-as-confinement-probe]] — Entanglement as a gauge-invariant probe of the confinement phase
- [[relative-entropy-interacting-theories]] — Relative entropy computation in the RGZ vacuum requires knowing which states are gauge-invariant
- [[bell-inequalities-with-gribov-horizon]] — Complementary approach: CHSH as a probe of Gribov physics
