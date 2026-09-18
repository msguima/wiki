---
title: Spectral Positivity Violation
type: concept
areas: [gribov-zwanziger]
aliases: [positivity violation, Källén-Lehmann violation, spectral condition violation]
modified: 2026-04-06
---

## Definition

For a quantum field $\varphi$ in a physically acceptable (unitary) theory, the two-point function must admit a **Källén-Lehmann spectral representation**:

$$\langle\varphi(x)\varphi(y)\rangle = \int_0^\infty \rho(\sigma)\,\Delta_+(x-y; \sigma)\,d\sigma,$$

where $\Delta_+(x-y;\sigma)$ is the positive-frequency part of the Pauli-Jordan propagator for mass $\sqrt{\sigma}$, and $\rho(\sigma) \geq 0$ is the **spectral density**. In Euclidean momentum space, this translates to

$$G(p^2) = \int_0^\infty \frac{\rho(\sigma)}{p^2 + \sigma}\,d\sigma,$$

with $\rho(\sigma) \geq 0$. This representation is a consequence of unitarity, Poincaré covariance, and microcausality.

A propagator **violates spectral positivity** (or violates the Källén-Lehmann representation) when no such decomposition with $\rho(\sigma) \geq 0$ exists. Equivalently, if the propagator $G(p^2)$ has complex poles (poles not on the positive real $p^2$ axis), or if its inverse Fourier transform takes negative values at some separations, then $\rho(\sigma)$ must be negative somewhere — a violation.

The **GZ gluon propagator** in Landau gauge:

$$G_{\text{GZ}}(p^2) = \frac{p^2}{p^4 + \gamma^4}$$

has complex poles at $p^2 = \pm i\gamma^2$ — two complex conjugate poles on the imaginary $p^2$ axis. These cannot be written as a positive spectral integral. The **RGZ gluon propagator**:

$$G_{\text{RGZ}}(p^2) = \frac{p^2 + M^2}{p^4 + (m^2+M^2)p^2 + m^2 M^2 + \gamma^4}$$

similarly has complex poles for appropriate parameter values, maintaining the positivity violation.

The physical interpretation is that the corresponding field **does not create or annihilate physical asymptotic particle states** — it is confined.

## Role in Research

Spectral positivity violation is the primary **propagator-level signal of [[confinement]]** in the [[gribov-zwanziger|Gribov-Zwanziger framework]]. It is a concrete, computable consequence of the Gribov horizon restriction on the Yang-Mills path integral.

Key results:

- The GZ gluon propagator violates Källén-Lehmann positivity by construction (complex poles from the Gribov mass $\gamma$); this was recognized by Gribov and Zwanziger as a confinement signal.

- The RGZ gluon propagator also violates positivity; the complex poles shift in position but do not disappear when dimension-two condensates are included.

- **Lattice confirmation**: lattice QCD measurements of the gluon propagator in Landau gauge are consistent with positivity violation — the Euclidean propagator has a zero crossing at intermediate momenta (a necessary condition for positivity violation in Euclidean space).

- **Spectral functions of gauge-invariant operators** (Eur. Phys. J. C 81, 2021): positivity is **not** violated for gauge-invariant composite operators (e.g., $F^2_{\mu\nu}$), consistent with the expectation that only gauge-charged fields are confined.

- **SU(2) Higgs system** (Phys. Rev. D 88, 2013; 27 citations): semiclassical analysis of the Higgs-Yang-Mills system near the Gribov horizon, studying how the phase structure (Higgs vs. confined phase) is reflected in the spectral properties.

## Relations

- [[confinement]] — spectral positivity violation is the GZ/RGZ confinement signal; its absence for gauge-invariant operators is consistent with the idea that only colored fields are confined
- [[refined-gribov-zwanziger]] — the RGZ propagator formula is the explicit source of complex poles; mass parameters $m^2, M^2, \gamma^4$ determine whether poles are real (no confinement) or complex (confinement)
- [[gribov-horizon]] — the Gribov mass $\gamma^4$ appearing in the denominator of the GZ propagator comes directly from the horizon restriction; it is the technical source of complex poles
- [[brst-symmetry]] — BRST consistency of the spectral positivity violation: the gluon field $A^a_\mu$ is not in the BRST cohomology, so its non-appearance as a physical asymptotic state is expected and consistent

## Papers

See [[gribov-zwanziger]] for full paper list.

## Notes

- Spectral positivity violation is a **necessary** but not **sufficient** condition for confinement in the strict sense. It confirms that the gluon does not appear as an asymptotic state, but does not by itself prove that quarks form bound hadrons or that the string tension is non-zero.
- The Oehme-Zimmermann superconvergence relation: for a propagator violating positivity, the spectral density $\rho(\sigma)$ (defined in the distributional sense, allowing negative values) must satisfy $\int_0^\infty \rho(\sigma)\,d\sigma = 0$, i.e., the sum rule vanishes. This is a characteristic "fingerprint" of positivity violation.
- Common confusion: the gluon propagator being finite at $p=0$ (as seen on the lattice) does not imply positivity restoration. The GZ/RGZ propagators are finite at $p=0$ but still violate Källén-Lehmann positivity due to complex poles.
- The quark propagator is also expected to violate spectral positivity (quark confinement), but this is harder to study analytically because quarks couple to the Higgs-like symmetry breaking in QCD. The focus in the GZ program has been on the gluon propagator.
