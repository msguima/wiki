---
title: Refined Gribov-Zwanziger Theory
type: concept
areas: [gribov-zwanziger]
aliases: [RGZ theory, Refined Gribov-Zwanziger, RGZ framework]
modified: 2026-04-06
---

## Definition

The **Refined Gribov-Zwanziger (RGZ)** theory is an extension of the Gribov-Zwanziger (GZ) framework that incorporates non-perturbative **dimension-two condensates** formed by the auxiliary fields introduced to localize the horizon function.

Starting from the GZ action with auxiliary fields $(\varphi^{ab}_\mu, \bar{\varphi}^{ab}_\mu, \omega^{ab}_\mu, \bar{\omega}^{ab}_\mu)$ (localizing the non-local horizon function), the RGZ theory includes dynamically generated condensates:

1. **Gluon condensate**: $\langle A^a_\mu A^a_\mu\rangle \neq 0$, a dimension-two gauge-field condensate.
2. **Auxiliary field condensate**: $\langle\bar{\varphi}^{ab}_\mu\varphi^{ab}_\mu - \bar{\omega}^{ab}_\mu\omega^{ab}_\mu\rangle \neq 0$.

These condensates are incorporated by adding mass parameters $m^2$ and $M^2$ to the action:

$$S_{\text{RGZ}} = S_{\text{GZ}} + \int d^4x\left(m^2 A^a_\mu A^a_\mu + M^2(\bar{\varphi}^{ab}_\mu\varphi^{ab}_\mu - \bar{\omega}^{ab}_\mu\omega^{ab}_\mu)\right).$$

The resulting **RGZ gluon propagator** in Landau gauge is

$$G(p^2) = \frac{p^2 + M^2}{p^4 + (m^2 + M^2)p^2 + m^2 M^2 + \gamma^4},$$

which is a **massive-type (Yukawa-like) propagator** at large $p^2$ and remains infrared-suppressed. The denominator is a quartic polynomial whose roots give the (complex) gluon "mass poles" — complex poles signal [[spectral-positivity-violation|spectral positivity violation]] and gluon confinement.

This propagator is in quantitative agreement with **lattice QCD** gluon propagator data in both Landau gauge (4d SU(2) and SU(3)) and Coulomb gauge, with the parameters $\{m^2, M^2, \gamma^4\}$ fit from lattice data.

The RGZ ghost propagator is also modified:

$$G_{\text{ghost}}(p^2) = \frac{p^2 + M^2}{p^2(p^2 + M^2) + \gamma^4},$$

showing a less singular infrared behavior than the pure GZ ghost propagator, consistent with lattice data showing a finite (non-divergent) ghost propagator in the infrared.

## Role in Research

RGZ is the culmination of the [[gribov-zwanziger]] research program developed from roughly 2011-2022. Key results:

- **Glueball mass estimates** (Phys. Lett. B 732, 2014; 21 citations): the RGZ propagator was used to estimate glueball masses via Padé methods; the inputs are the complex poles of the RGZ gluon propagator.

- **Linear covariant gauges**: the RGZ framework was extended to linear covariant gauges (parameterized by $\xi$), where the [[gribov-copies|Gribov copies]] problem is equally severe. The exact nilpotent [[brst-symmetry|BRST symmetry]] for this extension (Phys. Rev. D 92, 2015; 92 citations) is the most-cited paper in the portfolio.

- **Ghost-gluon vertex at general kinematics** (Phys. Rev. D 109, 2024; with [[marcela-pelaez]]): the most recent RGZ paper, comparing RGZ predictions for the ghost-gluon vertex at off-symmetry-point kinematics with lattice data.

- **Extensions**: N=1 super Yang-Mills, noncommutative QED, higher-dimensional Yang-Mills, Higgs-Yang-Mills system — all studied within the RGZ framework.

## Relations

- [[gribov-copies]] — the GZ restriction to the first Gribov region is the foundation on which RGZ is built; dimension-two condensates are generated within the restricted path integral
- [[gribov-horizon]] — the horizon condition (Zwanziger's self-consistent horizon equation) is preserved in RGZ; the Gribov mass $\gamma$ remains as a parameter alongside the condensate masses $m^2, M^2$
- [[brst-symmetry]] — the exact nilpotent BRST symmetry for the RGZ/GZ action is the central consistency result of the program; without it, the restriction to $\Omega$ would lack gauge-theoretic justification
- [[confinement]] — the complex poles of the RGZ gluon propagator provide a concrete mechanism for gluon confinement at the propagator level; the propagator cannot be written as a positive Källén-Lehmann spectral density
- [[spectral-positivity-violation]] — the RGZ gluon propagator violates spectral positivity (has complex poles); this is the signal of confinement in the RGZ framework

## Papers

See [[gribov-zwanziger]] for full paper list.

## Notes

- The "refinement" in RGZ refers to the inclusion of dimension-two condensates that were neglected in the original GZ framework. These condensates are dynamically generated (analogous to chiral symmetry breaking condensates in QCD) and modify the propagators quantitatively.
- The parameters $\{m^2, M^2, \gamma\}$ are not all independent: $\gamma$ is fixed by the horizon condition, and $m^2, M^2$ arise from separate gap equations for the condensates. In practice, they are often fit to lattice data.
- Common confusion: RGZ is not a new gauge-fixing scheme — it uses Landau gauge (or linear covariant gauges). It is an improved approximation to the restricted path integral that includes the leading non-perturbative effects from condensate formation.
- The quantitative agreement of the RGZ propagator with lattice QCD data (for both gluon and ghost propagators) is the main empirical validation of the framework. The agreement is good for SU(2) and SU(3) in 4 dimensions.
