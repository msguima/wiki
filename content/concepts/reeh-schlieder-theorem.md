---
title: Reeh–Schlieder Theorem
type: concept
areas: [relative-entropy-qft, bell-inequalities-qft]
aliases: [Reeh-Schlieder, cyclic and separating vacuum, vacuum is cyclic]
modified: 2026-07-21
---

## Definition

The **Reeh–Schlieder (RS) theorem** states that in a QFT satisfying the Wightman / [[haag-kastler-axioms|Haag–Kastler axioms]], the vacuum $|\Omega\rangle$ is **cyclic** and **separating** for the local algebra $\mathcal{A}(\mathcal{O})$ of *any* open spacetime region $\mathcal{O}$, no matter how small.

- **Cyclic:** $\{a|\Omega\rangle : a\in\mathcal{A}(\mathcal{O})\}$ is dense in the full Hilbert space $\mathcal{H}$. Acting with operators localized in a tiny region can approximate *any* global state — including states describing particles arbitrarily far away.
- **Separating:** if $a|\Omega\rangle = 0$ for $a\in\mathcal{A}(\mathcal{O})$ then $a=0$. No non-zero local operator annihilates the vacuum.

The two properties are dual: $|\Omega\rangle$ is cyclic for $\mathcal{A}(\mathcal{O})$ iff it is separating for the commutant $\mathcal{A}(\mathcal{O})'$, which by **Haag duality** is $\mathcal{A}(\mathcal{O}')$ (the causal complement). The proof rests on the **analyticity** of vacuum correlators in the energy (the spectrum condition): the vacuum has no lowest-energy localized excitation to annihilate.

The physically decisive corollary: **a cyclic-separating vector defines a faithful normal state**, which is exactly the hypothesis of [[tomita-takesaki-modular-theory|Tomita–Takesaki modular theory]]. Moreover RS holds not only for the vacuum but for any state of **bounded energy** (finite energy states are also cyclic-separating), and any state that resembles the vacuum at short distances inherits the property — so it covers essentially all physical states: $k$-particle states, conformal primaries and descendants, etc.

## Role in Research

Reeh–Schlieder is the theorem that guarantees the group's modular-theoretic machinery *applies at all*, and it recurs as a hypothesis across the program:

- **Modular theory is available everywhere.** Because RS makes the vacuum cyclic-separating for every local algebra, [[tomita-takesaki-modular-theory|Tomita–Takesaki]] theory — and hence the [[bisognano-wichmann-theorem|Bisognano–Wichmann]] modular operator, the [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]], and the [[bell-chsh-inequality|Bell-CHSH]] construction — is defined on the algebra of *any* region.
- **Vacuum entanglement / Bell violation.** RS is the original source of the statement that the vacuum is entangled across any bipartition, which is what allows vacuum Bell-CHSH violation on complementary [[rindler-wedges|wedges]].
- **[[magic-nonstabilizerness|Magic]].** In [[2026-benedetti-magic-in-qft|Benedetti–Dabholkar–Dalmonte]], RS is the step that upgrades "the vacuum is magical" to "*every physical state* is magical": all cyclic-separating (faithful normal) states have a continuous modular spectrum and hence a non-flat entanglement spectrum.
- **[[gribov-zwanziger|Gribov–Zwanziger]] frontier.** RS assumes the standard axioms; whether it holds for the RGZ/confining vacuum, where the functional integral is restricted by the non-local horizon condition, is itself an open problem — see [[entanglement-as-confinement-probe]] and [[magic-and-the-gribov-horizon]].
- **Impossible measurements.** RS-driven non-locality (a local operation can affect distant expectation values) is part of the tension behind [[impossible-measurements-qft|impossible measurements]] in relativistic QFT.

## Relations

- [[tomita-takesaki-modular-theory]] — RS supplies the cyclic-separating vector that modular theory requires
- [[bisognano-wichmann-theorem]] — RS provides the cyclic-separating vacuum whose wedge modular flow BW identifies with a boost
- [[type-iii-von-neumann-algebras]] — that *every* faithful normal state is cyclic-separating (no pure states) is a hallmark of type III₁; RS is how this shows up for the vacuum
- [[araki-uhlmann-relative-entropy]] — well-defined precisely because RS guarantees faithful normal states
- [[magic-nonstabilizerness]] — RS extends "magical" from the vacuum to all low-energy states
- [[rindler-wedges]], [[causal-diamonds]] — the local regions for which the vacuum is cyclic-separating

## Papers

- H. Reeh, S. Schlieder, *Bemerkungen zur Unitäräquivalenz von Lorentzinvarianten Feldern*, Nuovo Cimento 22 (1961) 1051 — the original theorem.
- E. Witten, *Notes on some entanglement properties of QFT*, Rev. Mod. Phys. 90 (2018) 045003 [1803.04993] — modern pedagogical account (cyclic-separating, modular theory, type III).
- Derived in the AQFT course: [[week-09-reeh-schlieder-and-local-algebras]].
- Used as a hypothesis in [[2026-benedetti-magic-in-qft]] and the group's Bell / relative-entropy work; reviewed in [[2025-liu-lectures-entanglement-vna]].

## Notes

- RS is often stated as "the vacuum is highly entangled" but the precise content is *cyclicity/separability*, which is stronger and more useful: it is the exact hypothesis of modular theory, not merely a statement about entanglement magnitude.
- The theorem is sometimes felt to be paradoxical (local operators "create" distant particles), but the operators required are highly non-local in effect and enormous in norm; RS constrains what is *possible in principle*, not what is achievable with bounded resources — again the backdrop to [[impossible-measurements-qft]].
- RS fails for theories without a mass gap in the naive form only through domain/technical subtleties; the cyclic-separating conclusion is robust for standard QFTs and is what the algebraic program uses.
