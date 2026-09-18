---
title: Dual Superconductor
type: concept
areas: [confinement-duality, condensed-matter-connections]
aliases: [dual superconductor model, magnetic monopole condensation, chromoelectric flux tube]
modified: 2026-04-06
---

## Definition

The **dual superconductor** is a model of [[confinement]] in which the QCD vacuum behaves as a **superconductor for magnetic (color-magnetic) charges**, producing the dual of the Meissner effect.

In an ordinary **superconductor**, the condensation of Cooper pairs (electric charge carriers) expels magnetic fields (Meissner effect) and forces any magnetic flux into quantized Abrikosov vortex tubes. Dualizing this picture:

- Replace electric charges $\leftrightarrow$ magnetic monopoles.
- Replace the condensate of Cooper pairs $\leftrightarrow$ condensate of magnetic monopoles.
- Replace expelled magnetic flux $\leftrightarrow$ expelled chromoelectric flux.

In the **dual superconductor picture** (Nambu 1974, 't Hooft 1975, Mandelstam 1976):

1. The QCD vacuum contains a condensate of **color-magnetic monopoles**: $\langle\phi_{\text{mag}}\rangle \neq 0$.
2. This condensate screens magnetic charges (dual Meissner effect) and forces chromoelectric flux between a quark-antiquark pair into a **chromoelectric flux tube** (string).
3. The string has constant energy per unit length (string tension $\sigma \approx 0.18\,\text{GeV}^2$), giving the linear confining potential $V(r) = \sigma r$.

The effective Lagrangian for the dual superconductor is the **dual Ginzburg-Landau theory**:

$$\mathcal{L}_{\text{dual}} = |D_\mu\phi|^2 - V(|\phi|) - \frac{1}{4}\tilde{F}^2_{\mu\nu},$$

where $\tilde{F}_{\mu\nu} = \frac{1}{2}\epsilon_{\mu\nu\rho\sigma}F^{\rho\sigma}$ is the dual field strength and $\phi$ is the monopole condensate field. The vortex solutions of this theory are chromoelectric flux tubes (dual Abrikosov vortices).

The dual superconductor mechanism is often called **Abelian dominance** in the non-abelian case: numerical lattice evidence suggests that after gauge-fixing to the maximal Abelian gauge, the $U(1)^{N-1}$ Abelian degrees of freedom of $SU(N)$ dominate the string tension.

## Role in Research

The dual superconductor is studied within the [[confinement-duality]] research line as the primary topological picture of confinement, complementary to the [[gribov-zwanziger|Gribov-Zwanziger]] propagator approach.

Key connections:

- **Julia-Toulouse mechanism**: the condensation of magnetic monopoles driving the dual superconductor phase is precisely an instance of the [[julia-toulouse-mechanism|Julia-Toulouse mechanism]]. The proliferation and condensation of monopoles is the topological phase transition described by Julia and Toulouse.

- **Axionic electrodynamics**: when both electric and magnetic condensates are present (dyonic condensation), the effective theory includes [[axionic-electrodynamics|axionic]] terms mixing electric and magnetic fields.

- **Connection to RGZ**: the dual superconductor and the GZ/RGZ framework both describe confinement, but operate at different levels. A theoretical bridge between the two (relating the Gribov mass $\gamma$ to the monopole condensate $\langle\phi_{\text{mag}}\rangle$ and string tension $\sigma$) remains an open problem.

## Relations

- [[julia-toulouse-mechanism]] — the dual superconductor is the outcome of the Julia-Toulouse mechanism applied to magnetic monopole condensation in $(3+1)$d Yang-Mills theory
- [[confinement]] — the dual superconductor provides the physical mechanism: chromoelectric flux tube formation and linear confinement potential
- [[axionic-electrodynamics]] — axionic couplings arise when both electric and magnetic condensates coexist (dyons); the dual superconductor with dyonic condensate leads to axionic terms in the effective theory
- [[refined-gribov-zwanziger]] — complementary description of confinement; connecting the string tension to the RGZ Gribov mass is an open problem
- [[spectral-positivity-violation]] — both approaches describe confinement: dual superconductor via the linear potential and string, RGZ via spectral positivity violation; they should be two faces of the same phenomenon

## Papers

See [[confinement-duality]] and [[condensed-matter-connections]] for full paper lists.

## Notes

- The dual superconductor scenario is supported by lattice QCD simulations in the maximal Abelian gauge, which show monopole condensation and Abelian dominance of the string tension. However, the gauge dependence of these findings (the results depend on the maximal Abelian gauge fixing) means the connection to the gauge-invariant physical picture is not fully settled.
- The Abrikosov vortex of a type-II superconductor carries magnetic flux $\Phi = 2\pi/e$; its chromoelectric dual (the QCD string) carries chromoelectric flux $\sigma r$.
- Common confusion: the dual superconductor model requires **magnetic** monopoles in QCD, which are not fundamental fields in the QCD Lagrangian. They are topological solitons ('t Hooft-Polyakov monopoles in the UV-completed theory, or effective degrees of freedom in the low-energy theory). Their existence as dynamical objects is non-perturbative and established only indirectly.
- The BPS monopole (Bogomolny-Prasad-Sommerfield) in $\mathcal{N}=2$ super-Yang-Mills is the analytically controllable version of these ideas: Seiberg and Witten (1994) proved that the dual superconductor mechanism operates exactly in the $\mathcal{N}=2$ theory, providing the first rigorous demonstration of confinement via monopole condensation in a gauge theory.
