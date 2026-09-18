---
title: Can entanglement and Bell violations serve as order parameters for confinement?
type: question
status: open
areas:
  - bell-inequalities-qft
  - gribov-zwanziger
priority: high
originated: 2026-04-06
---

## Statement

Can Bell-CHSH violation amplitudes and Araki-Uhlmann [[araki-uhlmann-relative-entropy|relative entropy]] serve as genuine order parameters that distinguish the confined phase of a non-abelian gauge theory from the deconfined (or Higgs) phase? More precisely: does the [[gribov-horizon]] — which enforces restriction of the functional integral to the first [[gribov-horizon|Gribov region]] and is responsible for spectral positivity violation in gluon propagators — leave a detectable imprint on entanglement measures computed for gauge-invariant operators?

## Why It Matters

Confinement in QCD remains one of the seven Millennium Prize Problems. The standard diagnostic tools — Wilson loop area law, Polyakov loop expectation value, spectral positivity violation of the gluon propagator — are each beset by subtleties: they are gauge-dependent, require large-distance asymptotics, or fail to distinguish the confined from the Higgs phase in certain parameter ranges (the [[fradkin-shenker]] continuity argument). An entanglement-based order parameter would be genuinely gauge-invariant if constructed from [[brst-symmetry|BRST-invariant operators]], computable within algebraic QFT, and potentially sensitive to the phase structure in a way that complements propagator-based criteria. This question sits at the intersection of the two most active research lines: [[bell-inequalities-qft]] and [[gribov-zwanziger]].

The [[refined-gribov-zwanziger]] (RGZ) framework already produces massive-type gluon propagators whose spectral functions violate positivity — a necessary (but not sufficient) condition for confinement. Whether this positivity violation propagates into entanglement measures between causally separated regions is completely open.

## What We Know

**From the Bell-inequality program:**
- The vacuum of a free relativistic QFT is highly entangled: Bell-CHSH violations up to the Tsirelson bound 2√2 have been demonstrated for the free massive scalar using [[weyl-operators]] and [[tomita-takesaki-modular-theory]] (Phys. Rev. D 108, 085026).
- [[araki-uhlmann-relative-entropy]] is well-defined for the [[type-iii-von-neumann-algebras]] that appear in local QFT and has been computed analytically for coherent and squeezed states above the free-field vacuum.
- A [[brst-symmetry|BRST-invariant formulation]] of Bell-CHSH for gauge theories exists (SciPost Phys. 15, 2023), providing the technical scaffolding needed to extend to confined phases.

**From the Gribov-Zwanziger program:**
- Restriction to the [[gribov-horizon|Gribov region]] modifies the gluon propagator from a massless pole to a [[gribov-zwanziger|Gribov propagator]] of the form $k^2/(k^4 + \gamma^4)$, which has no particle interpretation (no positive spectral weight).
- The [[refined-gribov-zwanziger]] theory incorporates dimension-two condensates $\langle A_\mu A^\mu \rangle$ and $\langle \bar\phi\phi \rangle$, yielding propagators that fit lattice data in Landau gauge.
- Entanglement properties of the RGZ vacuum — a vacuum built over a functional integral restricted to the [[gribov-horizon|Gribov region]] — have not been computed.

**Structural tension:**
The algebraic QFT framework assumes the [[reeh-schlieder-theorem]] and the standard [[haag-kastler-axioms]], which are not straightforwardly applicable when the functional integral is restricted by a non-local constraint (the horizon condition). Formulating the algebraic structure of the RGZ vacuum is itself an open problem. See also [[gribov-copies-physical-observables]] for the related question of gauge-invariant observables.

## Possible Approaches

1. **Effective propagator approach**: Use the RGZ gluon propagator as input to compute two-point Wightman functions; from these, extract the Bell-CHSH operator expectation values following the [[weyl-operators|Weyl operator formalism]]. The absence of a Källén-Lehmann spectral representation makes this non-trivial but not impossible — one can work directly with Euclidean correlators continued to Minkowski signature, provided positivity of the resulting kernel is tracked carefully.

2. **Lattice computation**: Compute [[entanglement-entropy]] between spatial half-spaces in SU(3) lattice gauge theory across the deconfinement transition (varying temperature or through a bulk transition), using the replica trick or the [[casini-huerta]] method adapted to non-abelian lattice gauge theory. Compare with the Bell-CHSH signal extracted from [[wilson-loop]] correlators.

3. **Toy model — Gribov copies in 0+1d**: Construct a quantum mechanical toy model with a Gribov-like restriction (compact configuration space with residual gauge freedom) and compute Bell violations exactly. This calibrates intuition before tackling 3+1d gauge theory.

4. **Relative entropy as phase probe**: Compute [[araki-uhlmann-relative-entropy]] between the RGZ vacuum and the perturbative (unconstrained) vacuum using the relationship between the horizon function and the modular Hamiltonian. The monotonicity and data-processing inequalities for relative entropy would constrain how much the confinement phase can differ from the free phase.

5. **BRST-invariant operator construction**: Extend the existing BRST-invariant Bell-CHSH formalism to include the Zwanziger horizon term and compute the change in violation amplitude as the Gribov mass parameter $\gamma$ (the [[gribov-zwanziger|Gribov parameter]]) is varied from zero to its self-consistent value.

## Related Questions

- [[bell-inequalities-with-gribov-horizon]] — The more technically focused question of CHSH behavior near the boundary of the Gribov region
- [[gribov-copies-physical-observables]] — Necessary prerequisite: understanding what gauge-invariant observables are accessible in the presence of Gribov copies
- [[relative-entropy-interacting-theories]] — Relative entropy in interacting (non-free) theories is needed for any computation in RGZ
- [[embezzlement-cost-relative-entropy]] — Relative entropy quantification of embezzlement cost may provide a complementary order parameter
- [[impossible-measurements-qft]] — Measurement limitations in relativistic QFT constrain what entanglement probes are operationally accessible
