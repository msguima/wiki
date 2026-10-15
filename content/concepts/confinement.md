---
title: Confinement
type: concept
areas: [gribov-zwanziger, confinement-duality]
aliases: [color confinement, quark confinement, gluon confinement]
modified: 2026-10-15
---

## Definition

**Confinement** (or **color confinement**) is the phenomenon that color-charged particles — quarks and gluons — are never observed as free asymptotic states. Only color-neutral bound states (hadrons: mesons, baryons, glueballs) appear in the physical spectrum of QCD.

Formally, confinement can be stated as the absence of isolated color-charged states from the physical Hilbert space $\mathcal{H}_{\text{phys}}$ (the [[brst-symmetry|BRST cohomology]]). The confining force grows linearly with distance (linear potential $V(r) \sim \sigma r$ at large $r$, where $\sigma \approx 0.18\,\text{GeV}^2$ is the string tension), leading to unbreakable chromoelectric flux tubes (strings) between quarks.

Confinement is not yet proven analytically from the QCD Lagrangian — the Millennium Prize Problem is the closely related existence and mass gap of Yang-Mills theory — but several mechanisms and signals are understood:

**1. Spectral positivity violation (GZ signal)**: The gluon propagator in the [[refined-gribov-zwanziger|RGZ framework]] does not admit a positive Källén-Lehmann spectral representation:

$$G(p^2) \neq \int_0^\infty \frac{\rho(\sigma)}{p^2 + \sigma}\,d\sigma, \quad \rho(\sigma) \geq 0.$$

Complex poles in the propagator (from the quartic GZ denominator) mean gluons cannot be produced as asymptotic physical particles — they are "confined to the propagator."

**2. Dual superconductor mechanism**: The QCD vacuum acts as a superconductor for magnetic (color-magnetic) charges. Condensation of magnetic monopoles leads to the dual Meissner effect, squeezing chromoelectric flux into tubes. See [[dual-superconductor]].

**3. Julia-Toulouse mechanism**: Proliferation and condensation of topological defects (monopoles, vortices) drives a transition to a confined phase. See [[julia-toulouse-mechanism]].

**Kugo-Ojima criterion**: in Landau gauge the criterion asks for a ghost propagator more singular than $1/p^2$ in the infrared (the "ghost enhancement") together with a gluon propagator vanishing at $p=0$, which is the scaling solution of the original GZ action. The lattice sees neither: the gluon propagator is finite and non-zero at $p=0$ and the ghost dressing function stays finite, the decoupling solution. Reproducing that behaviour is what the dimension-two condensates of [[refined-gribov-zwanziger|RGZ]] do, and the confinement signal then rests on the complex poles rather than on the enhancement.

## Role in Research

Confinement connects the [[gribov-zwanziger]] and [[confinement-duality]] research lines:

**From the GZ side**: The [[refined-gribov-zwanziger|RGZ]] framework provides a propagator-level signal: the gluon propagator has complex poles, violating Källén-Lehmann spectral positivity. This was developed across the 2011-2022 program, with glueball mass estimates (Phys. Lett. B 732, 2014) and spectral function studies (Eur. Phys. J. C 81, 2021).

**From the duality side**: The [[dual-superconductor|dual superconductor]] model and the [[julia-toulouse-mechanism|Julia-Toulouse mechanism]] provide complementary topological pictures of confinement, studied through the [[confinement-duality]] research line.

**Connection to quantum information**: An emerging question is whether [[bell-chsh-inequality|Bell-CHSH violations]] and [[araki-uhlmann-relative-entropy|relative entropy]] can serve as probes of the confinement phase transition — the "entanglement as a probe of confinement" direction listed as an open problem in both [[gribov-zwanziger]] and [[bell-inequalities-qft]].

## Relations

- [[spectral-positivity-violation]] — the most concrete propagator-level signal of gluon confinement within the GZ/RGZ framework; absence of positive Källén-Lehmann spectral representation
- [[refined-gribov-zwanziger]] — the RGZ propagator provides the technical implementation of the GZ confinement signal; complex poles encode the non-observability of gluons
- [[gribov-horizon]] — the Gribov horizon restriction produces the modified propagators that signal confinement; Zwanziger's theorem connects the horizon to the infrared behavior
- [[brst-symmetry]] — confinement in BRST language means quarks and gluons are not in the BRST cohomology; only gauge-invariant composite operators (hadrons) contribute to physical states
- [[dual-superconductor]] — the complementary topological mechanism of confinement via magnetic monopole condensation; chromo-electric flux tubes as the dual of the Abrikosov vortex
- [[julia-toulouse-mechanism]] — topological defect condensation as the field-theoretic mechanism driving the confinement phase transition

## Papers

See [[gribov-zwanziger]] and [[confinement-duality]] for full paper lists.

## Notes

- The Yang-Mills mass gap problem (proving that the Yang-Mills spectrum has a mass gap $\Delta > 0$) is a Millennium Prize Problem. Confinement is closely related but technically distinct — the mass gap implies no massless colored states, which is part of confinement.
- The order parameter for the deconfinement transition of the pure gauge theory at finite temperature is the Polyakov loop, charged under the $\mathbb{Z}_N$ center symmetry; the string tension vanishes above $T_c$ along with it. With dynamical quarks in the fundamental representation neither is an order parameter in the strict sense, because the center symmetry is explicitly broken.
- Common confusion: confinement applies to color-charged particles, not to all massive particles. The Higgs mechanism (in electroweak theory) also makes gauge bosons massive, but those particles are observable — Higgs-generated mass is not confinement.
- The relationship between the Gribov horizon and the string tension is not yet fully established analytically, though both the GZ propagator modifications and the lattice string tension arise from the same non-perturbative IR dynamics.
- The [[geometric-qcd-course-guide|geometric-QCD course]] reads critically Migdal's 2026 proposal to solve planar QCD through a Hodge-dual minimal surface, from which the confining string and the meson spectrum would follow; its [[courses/geometric-qcd-course/claim-status-map|claim map]] separates the calculations checked in the course from the open claims.
