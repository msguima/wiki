---
title: Can relative entropy computations be extended beyond free field theories?
type: question
status: open
areas:
  - relative-entropy-qft
priority: medium
originated: 2026-04-06
---

## Statement

All closed-form results for [[araki-uhlmann-relative-entropy]] in the research program have been obtained for free fields (free massive scalar in (1+1)d and higher dimensions, with coherent, squeezed, and cat state excitations). Can these methods be extended to interacting theories — and if so, which classes of interactions are tractable? In particular, can the relative entropy between gauge-invariant states in Yang-Mills theory, or between states in the [[refined-gribov-zwanziger]] vacuum, be computed analytically or semi-analytically?

## Why It Matters

The [[araki-uhlmann-relative-entropy]] $S(\omega||\varphi)$ is the most operationally fundamental measure of distinguishability in quantum information theory: it controls the asymptotic error exponent for hypothesis testing (quantum Stein lemma), and it satisfies the strongest monotonicity properties (data processing inequality). In free-field QFT, it is computable because the [[tomita-takesaki-modular-theory|relative modular operator]] $\Delta_{\Phi,\Omega}$ can be expressed in terms of the two-point function (Bogoliubov transformation structure). In interacting theories, the modular operator involves all $n$-point correlators, and no closed form is known in general.

Extending relative entropy computations to interacting theories would:
- Enable the program of using relative entropy as a phase-transition probe (see [[entanglement-as-confinement-probe]]).
- Allow computation of the [[embezzlement-cost-relative-entropy]] for physically realistic gauge theories.
- Connect to the [[tomita-takesaki-modular-theory]] program in constructive QFT, where the modular operator for interacting theories is an active area of mathematical physics research.
- Make contact with the [[holographic-relative-entropy]] program (Faulkner, Lewkowycz, Maldacena), where relative entropy in CFTs is computed via the Ryu-Takayanagi formula.

## What We Know

**Free-field results (established in the program):**
- For the free massive scalar, the relative modular operator factorizes: $\Delta_{\Phi,\Omega} = \Delta_\Phi \Delta_\Omega^{-1}$, and both factors can be expressed in terms of the two-point function via Bogoliubov transformations.
- Relative entropy of coherent states: $S(W(f)\Omega || \Omega) \propto \text{Im}\,\Delta(f,f)$ where $\Delta(f,g)$ is the smeared [[pauli-jordan-distribution]] (Nucl. Phys. B 1018, 2025).
- Relative entropy of squeezed states: closed form in terms of Bogoliubov coefficients (Eur. Phys. J. C 85, 2025).
- Cat states: the interference terms introduce non-Gaussian corrections; results exist but are structurally more complex.
- Mass and dimension dependence: studied systematically in arXiv:2511.20244.

**Structural results from mathematical physics:**
- [[bisognano-wichmann-theorem]]: for wedge regions in the vacuum of a local QFT satisfying [[haag-kastler-axioms]], the modular operator is $\Delta_\Omega = e^{-2\pi K}$ where $K$ is the boost generator (Rindler Hamiltonian). This holds for any QFT (free or interacting), but gives the modular operator of the vacuum, not the relative modular operator for an excited state.
- Araki's perturbation theory: if $\Phi = \exp(h) \cdot \Omega$ for a self-adjoint $h$ affiliated with the algebra, the relative entropy can be computed perturbatively in $h$. This applies to coherent states in free theories but is formal for interacting theories.
- For 2d integrable theories (S-matrix bootstrap), some properties of the modular operator have been studied using the KMS condition and TCP invariance, but no closed-form relative entropy is known.

**Perturbative interacting theories:**
- At weak coupling $\lambda \phi^4$, corrections to free-field relative entropy can in principle be computed using the Schwinger-Dyson equations and Wick's theorem. The leading correction is $O(\lambda)$ and involves the connected four-point function. No such computation has been carried out in the program.

## Possible Approaches

1. **Perturbation theory in coupling constant**: For $\lambda \phi^4$ theory or for Yang-Mills at weak coupling, compute relative entropy to first order in the coupling. The perturbative expansion of the [[tomita-takesaki-modular-theory|relative modular operator]] generates a series in the connected $n$-point functions. At $O(\lambda)$, only the four-point connected function contributes. This is technically demanding but conceptually straightforward.

2. **2d integrable theories**: In integrable field theories (sine-Gordon, Thirring, Ising model off-critical), form factor methods give exact $n$-point functions. Use these to construct the modular operator perturbatively around the free fixed point, and compute relative entropy between particle states and the vacuum. The form factor bootstrap provides a systematic expansion in terms of the particle spectrum.

3. **RGZ vacuum as non-perturbative input**: In the [[refined-gribov-zwanziger]] framework, the gluon propagator is known non-perturbatively (it fits lattice data). Treat the RGZ propagator as the effective two-point function and compute relative entropy in the "quasi-free" approximation where all higher connected correlators are neglected. This is not exact but gives a physically motivated estimate of the corrections from the Gribov structure.

4. **Holographic approach**: For strongly coupled large-$N$ gauge theories with a holographic dual, the relative entropy between excited states and the ground state is computable via the Ryu-Takayanagi formula extended to excited states (Faulkner-Lewkowycz-Maldacena). This gives non-perturbative, strongly coupled results — though in a regime far from QCD.

5. **Numerical approach**: Extend the numerical framework already developed for free fields (Nucl. Phys. B 1018, 2025) to interacting theories regulated on a lattice. The [[tomita-takesaki-modular-theory|modular Hamiltonian]] can be approximated numerically by the reduced density matrix on a spatial interval, from which relative entropy is computed as $S(\rho||\sigma) = \text{tr}(\rho \log \rho) - \text{tr}(\rho \log \sigma)$ using the eigenvalue decomposition.

6. **Monotonicity constraints**: Even without a closed-form result, the data-processing inequality and monotonicity of relative entropy under coarse-graining constrain the interacting-theory relative entropy to lie within bounds set by the free-field result. Determining how tight these bounds are is a tractable preliminary step.

## Related Questions

- [[embezzlement-cost-relative-entropy]] — Embezzlement cost in physically realistic (interacting) QFTs requires this extension
- [[entanglement-as-confinement-probe]] — Phase-transition probe via relative entropy requires extending to the confined phase of Yang-Mills
- [[bell-inequalities-with-gribov-horizon]] — Bell violations in the RGZ vacuum is the complementary question using the same interacting framework
- [[gribov-copies-physical-observables]] — Identifying physical observables for relative entropy computation in gauge theories
