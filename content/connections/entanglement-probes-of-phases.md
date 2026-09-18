---
title: "Entanglement as a Probe of Phase Transitions in Gauge Theories"
type: connection
areas: [bell-inequalities-qft, relative-entropy-qft, gribov-zwanziger]
maturity: developing
modified: 2026-04-06
---

## The Link

The standard order parameters for phase transitions in gauge theories — the Polyakov loop, the Wilson loop area law, the chiral condensate — are gauge-invariant but not always directly measurable or unambiguous across all frameworks. A complementary proposal, which has gained significant traction in recent years, is that quantum information measures — Bell-CHSH violations, entanglement entropy, relative entropy — can serve as diagnostics or even order parameters for phase transitions, including the confinement-deconfinement transition. This connection page explores whether the tools developed in the active quantum information program can be deployed on the confinement problem, specifically in the [[gribov-zwanziger|Gribov-Zwanziger framework]] where the confinement mechanism is most concretely implemented in this research portfolio.

The core idea is that phase transitions are, at their root, reorganizations of the quantum state — changes in which degrees of freedom are entangled, how strongly, and across which spatial scales. In a confined phase, color-electric flux is concentrated in narrow tubes between quarks, and the vacuum is a condensate of magnetic monopoles (in the dual superconductor picture). In a deconfined phase, the flux spreads freely. These different vacuum structures should be reflected in different entanglement profiles across spacelike separated regions. If so, the Bell-CHSH violation B between two Rindler wedges, or the [[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]] S(ω_T‖ω_0) between states at temperature T and at zero temperature, would exhibit non-analytic behavior at the phase transition point — a sharp change in the entanglement landscape.

Within the [[gribov-zwanziger|Gribov-Zwanziger framework]], this question becomes concrete. The GZ theory implements confinement by restricting the path integral to the first Gribov region, which deforms the gluon propagator to one with complex poles and no positive spectral representation. This deformation is controlled by the Gribov mass parameter γ, fixed self-consistently by the gap equation (horizon condition). The transition from γ = 0 (perturbative vacuum) to γ ≠ 0 (confined vacuum) is precisely the kind of vacuum reorganization that should show up in entanglement measures. Moreover, the [[refined-gribov-zwanziger|RGZ]] framework at finite temperature, while not yet fully developed, would in principle allow a study of how Bell violations and relative entropy evolve across the deconfinement temperature T_c.

A further ingredient comes from the [[relative-entropy-qft|relative entropy program]]: the Araki-Uhlmann relative entropy between coherent, squeezed, and cat states and the vacuum has already been computed explicitly. These computations reveal how relative entropy depends on mass, dimension, and state parameters. The next step — computing relative entropy between states in different *phases* of a gauge theory — is a natural but technically demanding extension.

## Evidence

- **Entanglement entropy and confinement in lattice QCD**: A substantial literature (not in the research portfolio but strongly related) has studied entanglement entropy across a spatial boundary in lattice gauge theories and found signatures of the deconfinement transition. This provides external validation of the general hypothesis.
- **GZ propagator and spectral positivity**: The gluon propagator in the GZ theory, D(p²) ~ (p² + m²_GZ)/(p⁴ + m⁴_GZ), violates the Källén-Lehmann spectral positivity. This is an unambiguous propagator-level signal of confinement. Since vacuum expectation values of [[weyl-operators|Weyl operators]] depend directly on the propagator through ⟨W(f)⟩ = exp(−½‖f‖²_D), the modification of D directly modifies the Bell-CHSH computations.
- **Mass dependence of relative entropy** (arXiv:2511.20244): The 2025 paper on mass dependence of relative entropy across dimensions already establishes that the relative entropy between states in QFT is sensitive to the mass parameter of the theory. Since the GZ theory introduces an effective Gribov mass, this work establishes the technical feasibility of extending to the GZ setting.
- **BRST-invariant Bell-CHSH in gauge theories** (SciPost Phys. 15, 2023): Demonstrates that gauge-invariant Bell observables exist, which is the necessary precondition for using them as phase diagnostics.
- **Phase structure at the Gribov horizon** (Phys. Rev. D 88, 2013; 27 citations): The semiclassical analysis of SU(2) Yang-Mills-Higgs near the Gribov horizon revealed distinct phases separated by the horizon. This suggests that the Gribov parameter γ already encodes phase structure, and that entanglement quantities sensitive to γ would be sensitive to these phases.
- **Bell inequality violations as open direction**: Both the [[bell-inequalities-qft|bell area file]] and the [[gribov-zwanziger|gribov area file]] explicitly list "entanglement as a probe of confinement" and "Bell inequalities with Gribov horizon" as open problems, reflecting the research group's recognition of this connection.

## Gaps

The primary technical gap is the absence of any computation of Bell-CHSH violations or relative entropy in a genuinely interacting gauge theory at the quantum level, even at leading order. All existing computations in the Bell and relative entropy programs work with free fields — the scalar, Dirac, and Proca fields, for which the vacuum is Gaussian and expectation values of Weyl operators are computable in closed form. The GZ theory is interacting in the sense that the horizon function introduces non-Gaussian corrections to the vacuum state.

A second gap is thermodynamic: to study a phase transition, one needs the theory at finite temperature. The [[refined-gribov-zwanziger|RGZ framework]] at finite temperature is an active but incomplete research direction (listed as open problem 4 in the gribov-zwanziger area file). Without a controlled finite-temperature GZ framework, it is not possible to track Bell violations or relative entropy across the deconfinement temperature.

A third gap is the question of which quantum information measure is most sensitive to the confinement transition. Bell-CHSH, relative entropy, and entanglement entropy all measure different aspects of the quantum state. The confined vacuum might produce a large relative entropy signature but a small change in Bell violation, or vice versa. Without a theoretical argument for which measure is best, one would need to compute all of them.

A fourth gap is definitional: "Bell violation as an order parameter" requires that B be (a) well-defined across the transition, (b) non-analytic at the critical point or at least sharply different between phases, and (c) not trivially equivalent to an existing order parameter. None of these properties has been established.

## Potential Projects

1. **GZ correction to Bell-CHSH at leading order in γ²**: Expand the vacuum expectation value ⟨W(f)⟩_GZ in powers of the Gribov mass γ², using the known GZ propagator. At leading order, the correction to the Bell-CHSH value is computable analytically. This would be the first concrete quantitative connection between the Gribov parameter and a Bell inequality.

2. **Relative entropy between GZ vacuum and perturbative vacuum**: Formulate the Araki-Uhlmann relative entropy S(ω_GZ‖ω_FP) between the Gribov-Zwanziger vacuum and the Faddeev-Popov (perturbative) vacuum. If the two vacua can be related by a Bogoliubov transformation (as is plausible at leading order in γ²), this relative entropy can be computed using the methods already developed in the relative entropy program.

3. **Finite-temperature Bell-CHSH in the RGZ framework**: Extend the Bell-CHSH computation to finite temperature using the thermal (KMS) state for the RGZ theory. This requires the finite-temperature RGZ propagator, which is under development in the portfolio. Track B(T) as a function of temperature through the deconfinement transition T_c.

4. **Comparison with Polyakov loop**: Compute both the Bell-CHSH violation and the Polyakov loop expectation value in the same framework (GZ at finite temperature) and study whether they have the same critical behavior at T_c. If they do, Bell violation is equivalent to an existing order parameter; if they don't, it captures genuinely new physics.

5. **Entanglement entropy across the Gribov horizon in Yang-Mills-Higgs**: Use the phase structure established in Phys. Rev. D 88, 2013 to study entanglement entropy (via the replica trick applied to the GZ action) as a function of the Higgs field parameters. The two distinct phases separated by the Gribov horizon should show different entanglement profiles.

6. **Review and synthesis**: Write a review article on entanglement-based diagnostics for confinement, covering the lattice literature, the GZ-based approach, and the algebraic QFT perspective. This would position the research group at the intersection of these fields.

## Related

### Areas
- [[bell-inequalities-qft]]
- [[relative-entropy-qft]]
- [[gribov-zwanziger]]
- [[confinement-duality]]

### Connections
- [[bell-meets-gribov]]
- [[type-iii-algebras-across-areas]]
- [[julia-toulouse-meets-generalized-symmetries]]

### Concepts
- [[bell-chsh-inequality]]
- [[araki-uhlmann-relative-entropy]]
- [[weyl-operators]]
- [[gribov-horizon]]
- [[refined-gribov-zwanziger]]
- [[spectral-positivity-violation]]
- [[confinement]]
- [[type-iii-von-neumann-algebras]]
- [[tomita-takesaki-modular-theory]]
- [[brst-symmetry]]
- [[tomita-takesaki-modular-theory|modular Hamiltonian]]
- [[wilson-loop]]
- [[polyakov-loop]]

### Questions
- [[entanglement-as-confinement-probe]]
- [[bell-inequalities-with-gribov-horizon]]
- [[gribov-copies-physical-observables]]

### Entities
- [[silvio-paolo-sorella]]
- [[david-dudal]]
- [[leticia-palhares]]
- [[itzhak-roditi]]
