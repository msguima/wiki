---
title: Extension of Bell-CHSH inequalities to higher-spin and non-abelian gauge fields
type: question
status: open
areas:
  - bell-inequalities-qft
priority: medium
originated: 2026-04-06
---

## Statement

The Bell-CHSH program in QFT has been developed primarily for the free massive scalar field and, to a lesser extent, for spin-1/2 (massless spinors) and spin-1 (Proca/Maxwell) fields. For higher-spin fields — massive spin-3/2 (Rarita-Schwinger), spin-2 (linearized gravity), and arbitrary-spin fields — and for non-abelian Yang-Mills gauge fields, the construction of bounded Hermitian dichotomic operators from [[weyl-operators]] requires new ingredients. What is the maximal Bell-CHSH violation achievable for these fields, and how does the spin and gauge group structure enter the violation amplitude?

## Why It Matters

The spin dependence of Bell violations is a fundamental question connecting quantum information to the representation theory of the Lorentz group. For finite-dimensional quantum systems, it is known that higher-spin singlet states generally allow larger violations of Bell inequalities than spin-1/2 pairs, but the relationship saturates and is not monotone. In relativistic QFT, the "spin" is encoded in the two-point Wightman function through the tensor/spinor structure of the field, and the Weyl operator construction must be adapted accordingly.

For non-abelian Yang-Mills fields, there are additional complications from gauge invariance: the Weyl operators must be constructed from [[brst-symmetry|BRST-invariant operators]] (gauge-invariant combinations), and the non-abelian nature introduces interactions even at the classical level (via the non-abelian field strength). Understanding Bell violations in this setting is essential for:
- Connecting the Bell-CHSH program to QCD phenomenology.
- Understanding whether non-abelian color correlations contribute to or suppress Bell violations relative to the abelian (QED) case.
- Probing the structure of the Yang-Mills vacuum, and whether non-abelian entanglement is qualitatively different from the abelian case.

Prior work has established Bell violations for the free massive scalar (Phys. Rev. D 108, 085026), maximal violation via [[haar-wavelets]] for massless spinors (Phys. Rev. D 108, L081701), spin-1 [[unruh-dewitt-detectors]] (Universe 10, 2024), and a general class of bounded Hermitian operators (Phys. Rev. D 112, 2025). The extension to higher spin and non-abelian fields is listed explicitly as a future direction in the program.

## What We Know

**Established in the program:**
- Scalar field (spin 0): Bell-CHSH violation computed analytically using [[weyl-operators]] in Rindler and diamond regions. Violation decreases with mass and spatial separation. The Tsirelson bound 2√2 is achieved in the massless limit with optimized test functions ([[haar-wavelets]]).
- Massless spinors (spin 1/2): Maximal violation via bumpified Haar wavelets (Phys. Rev. D 108, L081701). The spinor structure allows a richer family of dichotomic operators.
- Spin-1 Unruh-DeWitt detectors: Bell-CHSH computed for detectors coupled to a spin-1 (Proca) field (Universe 10, 2024). The polarization degrees of freedom enter through the detector-field coupling.
- General bounded Hermitian operators: A systematic class of dichotomic observables constructed from [[weyl-operators]] with general test functions has been identified (Phys. Rev. D 112, 2025), providing a framework for extension to arbitrary fields.

**From representation theory:**
- The two-point Wightman function for a spin-$s$ field has the tensorial/spinorial structure dictated by the $(j_1, j_2)$ representation of the Lorentz group. For the free field, all higher-point functions follow from Wick's theorem, so the Bell correlator is expressed in terms of this two-point function.
- For the massive spin-2 field (Fierz-Pauli), the two-point function is $W_{\mu\nu,\rho\sigma}(x-y) = \langle 0 | h_{\mu\nu}(x) h_{\rho\sigma}(y) | 0\rangle$ and is proportional to the spin-2 projection of the massless propagator with a mass-dependent correction.

**Non-abelian case — what is missing:**
- For Yang-Mills fields, the Weyl operator $W(f) = \exp(i \int f^\mu A_\mu^a T^a)$ with $T^a$ in some representation of the gauge group $G$ is not gauge-invariant. The gauge-invariant version requires a path-ordered exponential (Wilson loop), which is non-local and breaks the smearing structure needed for the [[tomita-takesaki-modular-theory]] construction.
- The [[brst-symmetry|BRST-invariant formulation]] (SciPost Phys. 15, 2023) provides a way around this in Landau gauge, but the resulting operators are more complex, and the computation of their vacuum expectation values requires non-perturbative input.

## Possible Approaches

1. **Spin-3/2 (Rarita-Schwinger) field**: Generalize the massless-spinor construction to the Rarita-Schwinger field. The key step is constructing a Weyl-type operator from a smeared spin-3/2 field and computing its vacuum expectation value. The consistency constraints of the Rarita-Schwinger equation (which in the massless case require gauge invariance) must be handled carefully.

2. **Linearized gravity (spin-2)**: The free spin-2 field (Fierz-Pauli/linearized graviton) has a [[weyl-operators|Weyl operator formalism]] analogue. The dichotomic observables are constructed from the smeared metric perturbation. The transverse-traceless decomposition provides the gauge-invariant degrees of freedom. This is technically tractable and would be the first Bell computation in a gravitational context.

3. **Abelian tower — arbitrary spin**: Use the Weinberg-Fronsdal higher-spin formalism to construct smeared field operators for arbitrary integer and half-integer spin, compute the two-point Wightman function, and extract the Bell correlator. The result should depend on spin through the polarization sum and the specific form of the propagator.

4. **Non-abelian case via BRST**: Extend the BRST-invariant Bell-CHSH construction to the non-abelian case by working in Landau gauge and using the nilpotent BRST charge of the GZ action. The BRST-invariant operators are elements of the BRST cohomology; computing their two-point functions requires knowledge of the full non-perturbative propagator. Combine with the RGZ propagator as input.

5. **Color factor analysis**: At weak coupling, the non-abelian Bell correlator $\langle W^a(f) W^b(g) \rangle$ carries color indices that are contracted with the test functions. The color structure enters through the Casimir of the representation. Determining the leading color-dependent correction to the scalar Bell violation is a perturbative calculation.

## Related Questions

- [[bell-inequalities-with-gribov-horizon]] — The non-abelian gauge field case with Gribov corrections
- [[impossible-measurements-qft]] — Higher-spin fields introduce new subtleties for ideal measurement in QFT
- [[entanglement-as-confinement-probe]] — Non-abelian gauge field Bell violations as probes of color confinement
- [[embezzlement-cost-relative-entropy]] — Embezzlement in higher-spin theories may have different costs due to different type III₁ structures
