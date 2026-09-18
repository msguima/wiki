---
title: Bisognano–Wichmann Theorem
type: concept
areas: [relative-entropy-qft, bell-inequalities-qft]
aliases: [Bisognano-Wichmann, BW theorem, geometric modular action, modular Hamiltonian of the wedge]
modified: 2026-07-21
---

## Definition

The **Bisognano–Wichmann (BW) theorem** identifies the abstract [[tomita-takesaki-modular-theory|Tomita–Takesaki modular operator]] of the vacuum, for a **Rindler wedge** algebra, with a geometric symmetry: the modular flow is a **Lorentz boost**.

Concretely, let $\mathcal{A}(W_R)$ be the local algebra of the right wedge $W_R=\{x^1>|x^0|\}$ and $|\Omega\rangle$ the vacuum. Then $|\Omega\rangle$ is cyclic and separating for $\mathcal{A}(W_R)$ (by [[reeh-schlieder-theorem|Reeh–Schlieder]]), and the associated modular objects are
$$\Delta_\Omega^{it} = U(\Lambda_{W_R}(-2\pi t)), \qquad J_\Omega = \Theta,$$
i.e. the **modular Hamiltonian is $2\pi$ times the boost generator**,
$$\Delta_\Omega = e^{-2\pi K}, \qquad K = \text{boost generator of } W_R,$$
and the modular conjugation $J$ is the anti-unitary $CPT$-type reflection $\Theta$ exchanging $W_R$ with its causal complement $W_L$. On the $x^0=0$ slice the modular Hamiltonian is the boost-weighted energy density,
$$K_{\Omega,W_R} = \int_{x^1>0} d^{D-1}x\; x^1\, T_{00}(x).$$

Two structural consequences matter downstream:

1. **The modular flow is geometric** — it acts on operators as a boost, independent of the interaction details of the theory. It holds for any QFT satisfying the Wightman / [[haag-kastler-axioms|Haag–Kastler axioms]] with a covariant vacuum.
2. **The modular spectrum is continuous.** Since $K$ (a boost) has spectrum all of $\mathbb{R}$, $\log\Delta_\Omega=-2\pi K$ has full-line spectrum. This is the concrete manifestation of the [[type-iii-von-neumann-algebras|type III₁]] classification (continuous Connes invariant) for wedge algebras.

A conformal transformation maps the wedge result to the modular Hamiltonian of a **ball/sphere** in a CFT, extending BW-type control to spherical regions.

## Role in Research

Bisognano–Wichmann is the computational keystone that turns abstract modular theory into explicit formulas, and it appears at the root of every line in the program:

- **[[relative-entropy-qft|Relative entropy]].** BW gives the vacuum modular operator explicitly, which is the reference point for the [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] $S(\omega\Vert\Omega)=-\langle\xi_\omega,\log\Delta_{\Omega|\omega}\xi_\omega\rangle$. Its geometric form is what makes the free-field computations for coherent, squeezed, and cat states tractable. See [[relative-entropy-interacting-theories]] for the interacting-theory subtlety (BW gives the *vacuum* modular operator, not the relative one for excited states).
- **[[bell-inequalities-qft|Bell-CHSH]].** The modular conjugation $J=\Theta$ furnished by BW is exactly what maps Alice's wedge operators to Bob's in the complementary wedge, underlying the vacuum Bell-CHSH construction on [[rindler-wedges|Rindler wedges]].
- **[[entanglement-embezzlement|Embezzlement]] and type classification.** The continuous spectrum of $\Delta_\Omega$ *is* the type III₁ signature; BW is how the [[type-iii-von-neumann-algebras|type III₁]] property is given physical content ([[embezzlement-cost-relative-entropy]]).
- **[[magic-nonstabilizerness|Magic]].** In [[2026-benedetti-magic-in-qft|Benedetti–Dabholkar–Dalmonte]], the continuous BW spectrum is precisely the obstruction to a flat entanglement spectrum, hence the proof that physical QFT states carry magic.
- **[[gribov-zwanziger|Gribov–Zwanziger]] frontier.** Whether BW survives the [[gribov-horizon|Gribov-horizon]] restriction is open and load-bearing: much of the algebraic structure (Bell, relative entropy, magic) assumes it. See [[magic-and-the-gribov-horizon]] and Gap 4 of [[type-iii-algebras-across-areas]].

## Relations

- [[tomita-takesaki-modular-theory]] — BW is the identification of the vacuum modular objects for a wedge; it is the concrete input to the abstract theory
- [[type-iii-von-neumann-algebras]] — the continuous modular spectrum from BW is the physical realization of the type III₁ Connes invariant
- [[reeh-schlieder-theorem]] — supplies the cyclic-separating vacuum that BW's modular objects act on
- [[rindler-wedges]] — the region where the modular flow is exactly a boost
- [[araki-uhlmann-relative-entropy]] — uses the BW modular operator as the vacuum reference
- [[bell-chsh-inequality]] — uses the BW modular conjugation $J=\Theta$ to relate complementary-wedge operators
- [[magic-nonstabilizerness]] — the BW continuous spectrum forbids flat (stabilizer) spectra

## Papers

- J. Bisognano, E. Wichmann, *On the duality condition for a Hermitian scalar field*, J. Math. Phys. 16 (1975) 985; and *...for quantum fields*, J. Math. Phys. 17 (1976) 303 — the original theorem.
- Derived in the AQFT course: week-10-bisognano-wichmann.
- Used in [[2026-benedetti-magic-in-qft]], the group's Bell-CHSH and relative-entropy papers, and reviewed in [[2025-liu-lectures-entanglement-vna]].

## Notes

- BW requires Lorentz covariance and the standard analyticity (spectrum condition) of the vacuum. For *non-wedge* regions the modular flow is generally non-geometric; the wedge (and, conformally, the ball) are the special cases where it is a pure boost.
- The **scaling-algebra** formalism extends BW's control to the short-distance limit of *other* states: any state approximating the vacuum at short distances has a modular operator approaching the BW one, which is the technical step that lets [[2026-benedetti-magic-in-qft|the magic result]] cover all low-energy states, not just the vacuum.
- BW is the relativistic-QFT counterpart of the KMS/thermal interpretation of the Unruh effect: the boost modular flow at $2\pi$ periodicity in imaginary time is the Unruh temperature $T_U=a/2\pi$.
