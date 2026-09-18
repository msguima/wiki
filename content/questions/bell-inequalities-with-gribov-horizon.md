---
title: How do Bell-CHSH violations behave in the presence of the Gribov horizon?
type: question
status: open
areas:
  - bell-inequalities-qft
  - gribov-zwanziger
priority: high
originated: 2026-04-06
---

## Statement

In relativistic QFT, Bell-CHSH violations are computed as vacuum expectation values of products of [[weyl-operators]] localized in causally separated regions. In non-abelian Yang-Mills theory, the functional integral must be restricted to the [[gribov-horizon|Gribov region]] Ω — or, in the [[refined-gribov-zwanziger]] framework, supplemented by dimension-two condensates — to avoid the Gribov copy problem. How does this restriction modify the Bell-CHSH operator expectation values? Does the [[gribov-horizon]] suppress, enhance, or qualitatively change the pattern of Bell inequality violations?

## Why It Matters

This question is the direct bridge between the two main research lines. In free scalar field theory, Bell-CHSH violations up to the Tsirelson bound have been demonstrated using the [[weyl-operators|Weyl operator formalism]] combined with [[tomita-takesaki-modular-theory]]. In gauge theories, the BRST-invariant formulation of Bell-CHSH (SciPost Phys. 15, 2023) provides the framework — but all explicit computations to date have been at the perturbative level, ignoring the Gribov problem. Since the [[gribov-horizon]] is an intrinsically non-perturbative effect that modifies the gluon propagator at all momenta (the [[gribov-zwanziger|Gribov propagator]] $k^2/(k^4 + \gamma^4)$ has support at all scales), one expects it to modify any observable computed in the vacuum, including Bell correlators.

If the Gribov horizon suppresses Bell violations, this would be consistent with the intuition that confinement "hides" quantum correlations. If it enhances them, this would suggest a novel form of non-local vacuum entanglement driven by the non-perturbative gauge structure. Either result would be new and physically significant.

## What We Know

**Established in the Bell-inequality program:**
- For the free massive scalar field, Bell-CHSH violations have the form $\mathcal{B} = 2\sqrt{1 + |\langle W(f) W(g) \rangle|^2}$ (schematically), where the two-point Weyl correlator is $\langle W(f)W(g)\rangle = \exp(-\frac{1}{2}\|f\|^2 - \frac{1}{2}\|g\|^2 - \langle f,g\rangle)$ with the inner product given by the [[pauli-jordan-distribution]] (Phys. Rev. D 108, 085026).
- The violation decreases with increasing mass and with increasing spacelike separation between the Alice and Bob regions. The [[rindler-wedges|Rindler wedge]] geometry is the natural setting.
- The BRST-invariant construction uses Weyl operators $W(f) = \exp(i \int f^\mu A_\mu)$ smeared with transverse test functions, giving observables that are insensitive to gauge transformations (SciPost Phys. 15, 2023).

**Established in the Gribov-Zwanziger program:**
- The gluon propagator in Landau gauge in the [[refined-gribov-zwanziger]] theory has the form $D(k^2) = (k^2 + M^2)/((k^2 + M^2)(k^2 + m^2) + \lambda^4)$ with parameters $M, m, \lambda$ fixed by gap equations and dimension-two condensates. This propagator has no K\"{a}ll\'{e}n-Lehmann representation with positive spectral weight — it violates [[spectral-positivity-violation|spectral positivity]].
- The violation of spectral positivity is a necessary condition for confinement in the Oehme-Zimmermann sense, but it modifies the analytic structure of propagators in a way that must be tracked carefully when computing vacuum expectation values.
- An exact nilpotent [[brst-symmetry]] for the GZ action in linear covariant gauges exists (Phys. Rev. D 92, 2015), which provides the BRST cohomology needed to identify physical observables.

**What is missing:** The Weyl operator two-point function $\langle W(f) W(g) \rangle_{\text{RGZ}}$ in the RGZ vacuum has not been computed. This requires evaluating $\exp(i \int f^\mu A_\mu)$ against the RGZ path integral — a non-trivial task because the [[zwanziger-horizon-function]] introduces a non-local, non-polynomial term in the action.

## Possible Approaches

1. **RGZ propagator as Weyl correlator input**: Express the Weyl operator two-point function in terms of the full gluon propagator (valid to leading order in a cumulant expansion). Substitute the RGZ propagator $D_{\text{RGZ}}(k^2)$ and evaluate numerically. The Gribov mass $\gamma$ appears as a parameter; one can study how the Bell violation $\mathcal{B}(\gamma)$ varies from the perturbative value ($\gamma = 0$, free field) to the self-consistent value ($\gamma = \gamma_*$).

2. **Localized horizon function**: Use the localized form of the [[zwanziger-horizon-function]] (involving auxiliary fields $\varphi, \bar\varphi, \omega, \bar\omega$) to write the RGZ action in local form. Then compute the Weyl correlator as a functional integral over the extended field space. In the quadratic (Gaussian) approximation for the auxiliary fields, the computation reduces to evaluating a determinant — feasible analytically.

3. **David Dudal collaboration**: Leverage the existing collaboration with [[david-dudal]] (Ghent), who is expert in both the RGZ framework and has co-authored Bell inequality papers. The computation would combine technical expertise from both research lines.

4. **Lattice measurement**: Compute the CHSH correlator in SU(2) lattice gauge theory in Landau gauge, comparing configurations in the first Gribov region (restricted by the [[no-pole-condition]]) with unrestricted configurations. This would give a non-perturbative, first-principles answer.

5. **Spectral representation approach**: Even when the gluon propagator lacks a positive Källén-Lehmann representation, one can write a generalized spectral representation with a signed spectral function $\rho(\mu^2)$ (which may take negative values). The Bell correlator is then a weighted integral of this spectral function with a kernel that depends on the test functions and the spacetime geometry. Determining the sign and magnitude of the correction from the Gribov structure is a concrete analytical task.

## Related Questions

- [[entanglement-as-confinement-probe]] — The broader program of using entanglement as a confinement order parameter
- [[gribov-copies-physical-observables]] — Understanding which observables are physical in the presence of Gribov copies is a prerequisite
- [[higher-spin-bell-inequalities]] — Extension to higher-spin/non-abelian gauge fields shares the gauge theory Bell-CHSH setup
- [[relative-entropy-interacting-theories]] — Relative entropy in interacting theories is the complementary quantum information quantity in this program
