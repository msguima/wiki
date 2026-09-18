---
title: Non-invertible symmetries in Maxwell-Chern-Simons theories
type: question
status: open
areas:
  - confinement-duality
priority: low
originated: 2026-04-06
---

## Statement

[[non-invertible-symmetries-mcs|Maxwell-Chern-Simons]] (MCS) theory in 2+1 dimensions occupies a special position in the landscape of gauge theories: it is simultaneously massive (the Chern-Simons term gives the photon a gauge-invariant mass), topological at long distances, dual to the [[self-dual-model]], and admits both electric and magnetic excitations (anyons). Recent developments in the theory of [[non-invertible-symmetries-mcs|non-invertible symmetries]] — symmetries whose fusion rules are not those of a group — suggest that such theories may carry non-invertible symmetry structures that generalize the electromagnetic duality. What are the non-invertible symmetries of Maxwell-Chern-Simons theory, and what do they imply for its phase structure, spectrum, and connection to the [[julia-toulouse-mechanism]]?

## Why It Matters

Non-invertible symmetries have emerged as a major organizing principle in modern QFT, unifying diverse phenomena: duality defects in Maxwell theory (Choi-Cordova-Hsin-Lam-Shao, 2022), Tambara-Yamagami symmetries in 2d, fusion categories in topological phases, and non-invertible higher-form symmetries in gauge theories. In 3+1d Maxwell theory, the electromagnetic duality is not a symmetry in the standard sense (it maps electric to magnetic charges and thus permutes sectors); in the modern language, it is implemented by a [[topological-defect-line]] (or surface) that is non-invertible.

Maxwell-Chern-Simons in 2+1d is particularly natural for this analysis because:
1. It is exactly solvable and has a known dual (self-dual model) — a well-established example of a duality that acts on the Hilbert space.
2. The [[chern-simons-level]] $k$ controls anyon statistics: at level $k$, the theory has anyonic excitations with statistical phase $e^{i\pi/k}$. The fusion rules of these anyons are generally non-group-like, suggesting non-invertible symmetries.
3. The earlier work on Maxwell-Chern-Simons duality in noncommutative spaces (Phys. Lett. B 605, 2005) and the connection between Chern-Simons terms and [[julia-toulouse-mechanism]] (Phys. Rev. D 88, 2013) provide technical tools that can be deployed.
4. This connects the earliest research line (duality, 2003–2013) to one of the most active current frontiers, providing a natural revival and modernization of that program (Project 18).

## What We Know

**Maxwell-Chern-Simons — established:**
- MCS action in 2+1d: $S = \int d^3x \left[-\frac{1}{4e^2} F_{\mu\nu}F^{\mu\nu} + \frac{k}{4\pi} \epsilon^{\mu\nu\rho} A_\mu \partial_\nu A_\rho \right]$. The parameter $k$ is the Chern-Simons level; for $k \in \mathbb{Z}$, the theory is gauge-invariant under large gauge transformations.
- The photon acquires a gauge-invariant mass $m = ke^2/4\pi$; at energies below $m$, the theory flows to pure Chern-Simons theory, which is a topological field theory with anyon excitations.
- Duality between MCS and the self-dual model (Deser-Jackiw, 1984; Fradkin-Schaposnik, 1994): the two theories have identical S-matrices and partition functions. In Marcelo's thesis (2005), this duality was extended to noncommutative space.
- In the presence of magnetic monopoles (Julia-Toulouse context): monopoles in 2+1d are instantons (Polyakov monopoles), and the Chern-Simons term gives them an electric charge, leading to dyonic excitations. This was studied explicitly (Phys. Rev. D 88, 2013; Phys. Lett. B 674, 2009).

**Non-invertible symmetries — modern framework:**
- In 3+1d Maxwell theory, the duality symmetry $F \to \star F$ is not a conventional symmetry (it mixes electric and magnetic sectors, which are not gauge-invariant individually). It is implemented by a topological surface operator — a "duality defect" — that obeys non-group fusion rules: $\mathcal{D} \times \mathcal{D} = \bigoplus_q \mathcal{L}_q$ where $\mathcal{L}_q$ are line operators (Choi-Cordova-Hsin-Lam-Shao, 2022).
- In 2+1d, 0-form non-invertible symmetries are implemented by topological line operators (defect lines). The fusion of two defect lines can produce a sum of defect lines — a fusion category structure.
- For Chern-Simons theory at level $k$, the anyonic excitations define a modular tensor category (MTC). The symmetry of the theory (acting on the Hilbert space) is described by the Drinfeld center of the MTC, which is in general non-invertible.
- The interplay between the Maxwell (non-topological) term and the Chern-Simons term in MCS breaks the full anyon symmetry of pure CS theory — but some non-invertible symmetries may survive.

**Gap:** The non-invertible symmetry structure of MCS theory (as opposed to pure CS theory) has not been analyzed. The role of the Maxwell term in breaking or preserving non-invertible symmetries is unknown.

## Possible Approaches

1. **Topological defect line construction for MCS**: Following the method of Choi et al. for 3+1d Maxwell theory, construct the topological defect line implementing the MCS duality in 2+1d. This requires: (i) identifying the duality transformation as a map on the field space, (ii) constructing the corresponding topological operator, and (iii) computing its fusion rules with local and line operators of the theory.

2. **Level-rank duality connection**: MCS at level $k$ with gauge group $U(1)$ is related by level-rank duality to $U(1)_k$ CS theory with different matter content. This duality is itself a non-invertible symmetry (it is not a bijection on operators). Using the level-rank duality, map the non-invertible symmetry question in MCS to a known result in pure CS theory.

3. **Anyon condensation analysis**: The Julia-Toulouse mechanism in 2+1d corresponds to anyon condensation: when anyons with specific statistics condense, the theory transitions to a new topological phase. Anyon condensation is described by the theory of Lagrangian subgroups of the MTC — a well-developed mathematical framework. Applying this to MCS would identify which non-invertible symmetries are preserved and which are broken by Julia-Toulouse condensation.

4. **Symmetry TFT (SymTFT) approach**: The modern approach to generalized symmetries uses a "symmetry topological field theory" (SymTFT) in one higher dimension to classify all possible symmetry structures of a given theory. For MCS in 2+1d, the SymTFT lives in 3+1d and is related to the 4d $\mathbb{Z}_k$ gauge theory. Analyze the SymTFT to classify the non-invertible symmetries of MCS.

5. **Noncommutative MCS**: The earlier work on MCS duality in noncommutative space (Phys. Lett. B 605, 2005) may provide a deformation parameter that controls the non-invertible symmetry structure. In noncommutative geometry, the symmetry algebra is deformed, and non-invertible symmetries may appear or disappear as the noncommutativity parameter $\theta$ is varied.

## Related Questions

- [[julia-toulouse-higher-form-symmetries]] — The Julia-Toulouse mechanism in MCS is the starting point; this question asks about the finer symmetry structure
- [[entanglement-as-confinement-probe]] — Non-invertible symmetries and their breaking control topological phases, which are characterized by long-range entanglement
- [[higher-spin-bell-inequalities]] — The anyonic excitations of MCS are higher-spin objects in the sense of braid statistics; Bell inequalities for anyons are unexplored
