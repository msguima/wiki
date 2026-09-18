---
title: "Universality of Magic in Local Quantum Field Theory"
type: paper
authors: [Benedetti, Dabholkar, Dalmonte]
year: 2026
arxiv: "2607.16403"
areas: [relative-entropy-qft, bell-inequalities-qft, condensed-matter-connections, gauge-gravity-duality]
status: preprint
---

## Summary

A short, sharp **hep-th** paper (Valentin Benedetti, Atish Dabholkar, Marcello Dalmonte; ICTP Trieste + INFN + Bologna; 27 pp, 17 Jul 2026) proving a clean structural fact: **no stabilizer state on a lattice can flow, in the continuum limit, to the vacuum of a local QFT — or to any state that resembles the vacuum at short distances.** Since a flat entanglement spectrum is a *necessary* condition for a state to be a stabilizer state, and physical QFT states provably cannot have a flat spectrum, every physically relevant QFT state carries **non-zero [[magic-nonstabilizerness|magic]]** (nonstabilizerness). Simulating QFT states on a quantum computer therefore *necessarily* requires resources beyond stabilizer states and Clifford gates — the Gottesman–Knill "classically simulable" sector can never reach the continuum vacuum.

The engine of the argument is exactly the algebraic machinery this wiki is built around. The [[reeh-schlieder-theorem|Reeh–Schlieder theorem]] makes the vacuum (and low-energy states near it) **cyclic and separating** for every local algebra; the [[bisognano-wichmann-theorem|Bisognano–Wichmann theorem]] fixes the vacuum modular operator on a wedge to $\Delta_\Omega = e^{-2\pi K}$ with $K$ the boost generator, whose spectrum is the *continuous* real line; and the **type III₁** nature of local algebras ([[type-iii-von-neumann-algebras]]) forces the Connes invariant $S(\mathcal{A}) = \{0\}\cup\mathbb{R}^+$ to be continuous. A flat entanglement spectrum corresponds to a modular operator proportional to the identity (trivial modular flow) — a type-I / discrete feature that a faithful normal state on a type III₁ algebra simply cannot have. Magic in QFT is, in one sentence, **a shadow of type III₁**.

This makes the paper an unusually direct outside contact with the group's program: it takes the same objects — cyclic-separating states, the vacuum modular Hamiltonian, Rindler-wedge reduced structure, free-field Bogoliubov coefficients — that drive the [[bell-inequalities-qft|Bell-CHSH]] and [[relative-entropy-qft|Araki–Uhlmann relative entropy]] lines, and reads a *new* quantum-information resource off them. Notably, Atish Dabholkar is also the contributor whose Strings 2026 question asks for a modular-invariant entanglement entropy in gravity — the same modular-theory frontier from the string-theory side.

## Key Results

**1. Flat entanglement spectrum ⟺ stabilizer (the QI input).** For a pure stabilizer state on a qudit chain, the reduced density matrix on any spatial region is proportional to a projector, so all Rényi entropies coincide: $S_n(A) = \log\lambda_A$, independent of $n$ (§2.2). This flatness is preserved under Clifford operations and even holds for disconnected regions, hence extends to the **Rényi mutual information** $I_n(A_1,A_2)$ — a UV-finite, regulator-independent quantity whose flatness must survive the continuum limit. Non-flatness is a *witness* of magic (Tirrito et al. 2024); the $n=2$ **anti-flatness** $F_2(\rho_A)$ lower-bounds the distance to the stabilizer set, $F_2(\rho_A)/8 \le \min_{\sigma\in\mathrm{STAB}}\lVert\psi-\sigma\rVert$ (Cao et al. 2024).

**2. The QFT vacuum is magical (Bisognano–Wichmann route).** A regularized-lattice computation of the wedge modular Hamiltonian $K_{\Omega,A} = \int_A d^{D-1}x\, x^1 H(x)$ shows that demanding a flat spectrum forces every non-diagonal piece of the energy density to vanish, collapsing the Hamiltonian to a multiple of the identity. A Lorentz-invariant QFT with a non-trivial Hamiltonian therefore **cannot** have a flat vacuum spectrum (§3.1). A parallel **replica-trick** argument: flatness would require $Z[\mathcal{M}_{n,A}] = (Z[\mathcal{M}])^n/\lambda_A^{n-1}$, impossible when local degrees of freedom feel the conical defect.

**3. III₁ factors as the root of magic (the algebraic core, §3.2).** Every cyclic-separating vector defines a faithful normal state; by [[reeh-schlieder-theorem|Reeh–Schlieder]] the vacuum and states approximating it at short distances (k-particle states, conformal primaries and descendants) are all cyclic-separating; by the continuous Connes spectrum of type III₁ their modular operators have continuous spectrum; hence their entanglement spectra cannot be flat. Run backwards: any lattice stabilizer string that survives the continuum limit must converge to the identity, because the only local operator annihilating a cyclic-separating vector is zero.

**4. TQFT is the exception.** A topological QFT *can* be a stabilizer state (the toric code is the paradigm): its replica partition function scales as $Z[\mathcal{M}_n] = (Z[\mathcal{M}_1])^n D^{n-1}$ with $D$ the total quantum dimension, and it is **not** a net of type III₁ factors (no local observables). Thus **magic sharply separates local QFT from TQFT**, purely by algebraic type — a distinction non-Gaussianity (free vs. interacting) does not see.

**5. Explicit examples (§4).**
- *CFT vacuum:* the Rényi mutual information between disjoint intervals has genuinely $n$-dependent coefficients (e.g. free scalar in $D=4$, eq. 4.12–4.13), so the CFT vacuum is "always magical"; the $n\to 0$ limit of $S_n$ for a sphere likewise carries non-trivial $n$-dependence in its universal (cutoff-independent) coefficient.
- *Free-boson particle states in Rindler:* using the two-mode-squeezed representation of the Minkowski vacuum and Bogoliubov/Unruh operators, the reduced density matrices of Unruh particle states $|N\rangle$ follow a Pascal distribution; the anti-flatness $F_n$ peaks at intermediate $q_\omega=e^{-\omega/T_U}$ and, strikingly, the spectrum becomes **flatter as $N\to\infty$** (though that limit is a singular, non-Fock state).

**6. Holography (§5).** Fixed-area states (RT / gravitational path integral) have flat spectra and are stabilizer-like tensor-network states — but the boundary CFT is a net of type III₁ algebras, so there are no *faithful* flat-spectrum states; bulk physical states, being cyclic-separating even under weak gravity, are magical, with non-flat subleading Rényi corrections from the modified cosmic-brane prescription. The Hartle–Hawking (not Boulware) vacuum is the physical near-horizon state and is magical; in string theory the string length acts as the lattice cutoff and the conclusion persists.

## Methods

- **Algebraic QFT:** [[type-iii-von-neumann-algebras|type III₁ factors]], the Connes invariant $S(\mathcal{A})$, [[tomita-takesaki-modular-theory|Tomita–Takesaki modular theory]], [[reeh-schlieder-theorem|Reeh–Schlieder]], [[bisognano-wichmann-theorem|Bisognano–Wichmann]], the **scaling-algebra** formalism for the short-distance approach to the BW modular operator.
- **Entanglement techniques:** [[replica-trick-gravity|replica trick]] / conical-defect partition functions, modular Hamiltonians for wedges and spheres (conformal mapping), Rényi entropies and the $n\to 0$ continuation, [[rindler-wedges|Rindler]] reduced density matrices via Bogoliubov coefficients.
- **Quantum-information / resource theory:** stabilizer formalism on qudit chains, the generalized Pauli/Clifford groups, entanglement-spectrum **flatness** and **anti-flatness** $F_n$ as magic witnesses, the stabilizer-distance bound.
- **Condensed-matter bridge:** qudit spin chains, string nets, MPS-magic literature (White–Cao–Swingle; Tarabunga–Tirrito–Dalmonte; Haug–Piroli) — the lattice side where these diagnostics were developed.

## Relevance

This paper hands the group a **new III₁-rooted resource to compute with the tools it already owns**, and it strengthens the "type III₁ as the common thread" thesis directly.

- **[[relative-entropy-qft]] — same modular machinery, new observable.** The wedge modular Hamiltonian and the free-field Rindler reduced structure are exactly what the Araki–Uhlmann relative-entropy computations for coherent, squeezed, and cat states already use. The anti-flatness $F_2$ is a *drop-in* new quantity computable from the same two-point functions — see the follow-up [[magic-of-coherent-squeezed-cat-states]].
- **[[type-iii-algebras-across-areas]] — a fourth vertex.** Magic joins Bell violation, relative entropy, and embezzlement as a resource whose presence is forced by type III₁. The natural conceptual question is whether these are quantitatively related — a magic ↔ relative-entropy inequality on III₁, tracked in [[relative-entropy-magic-inequality]].
- **[[bell-inequalities-qft]] — shared root.** The cyclic-separating/BW structure that guarantees vacuum Bell-CHSH violation is the *same* structure that guarantees magic; both are readings of the continuous modular spectrum. Cat states, which the group has shown produce qualitatively new Bell features, are a natural place to look for enhanced magic.
- **[[gribov-zwanziger]] / [[confinement-duality]] — a genuinely new diagnostic.** The result assumes standard type III₁ + BW + Reeh–Schlieder. Whether the [[gribov-horizon|Gribov-horizon]] restriction preserves them (the RGZ vacuum's modified propagators and the open status of Reeh–Schlieder there — cf. [[entanglement-as-confinement-probe]]) makes **magic a candidate confinement probe**: [[magic-and-the-gribov-horizon]].
- **[[gauge-gravity-duality]] — resource theory in holography.** Fixed-area (stabilizer) vs. physical (magical) states connect to the group's [[holographic-resource-theory|holographic resource theory]] and [[holographic-dual-embezzlement-protocol|embezzlement]] work, where fixed-area states are the flat-spectrum reference; and it answers, concretely, part of the Goto et al. call for a QFT resource theory ([[resource-theory-monotones-in-qft]], [[free-states-and-operations-for-resource-theory-in-qft]]).
- **[[condensed-matter-connections]].** The lattice-magic diagnostics (anti-flatness, stabilizer Rényi entropy) come from the many-body community (Dalmonte is an author); the continuum-limit statement is a clean instance of the [[condensed-matter-qft-bridge]].

## Questions Raised

1. What is the magic (anti-flatness $F_2$) of the group's **coherent, squeezed, and cat states** in the Rindler wedge, computed from the same Bogoliubov data as their relative-entropy results — and do cat states *maximize* magic where large-$N$ particle states flatten it? → [[magic-of-coherent-squeezed-cat-states]]
2. Is there a quantitative **inequality relating magic, Araki–Uhlmann relative entropy, and the Bell-CHSH value** for a state on a type III₁ algebra — making the "common thread" precise? → [[relative-entropy-magic-inequality]], and Gap 3 / Project 1 of [[type-iii-algebras-across-areas]].
3. Does the **Gribov-horizon restriction** change the magic of the confining vacuum — i.e. can magic serve as an order parameter for confinement / a diagnostic that the RGZ vacuum departs from the standard type III₁ + BW structure? → [[magic-and-the-gribov-horizon]]
4. How does the magic of the two-sided (TFD / Hartle–Hawking) state change when a **traversable wormhole** is opened by a GJW deformation (a Connes cocycle) — alongside the group's Bell-CHSH and relative-entropy analyses of the same operation? → [[magic-across-traversable-wormhole]]
5. Does the onset of magic track the **confinement / higher-form-symmetry** transition between a local gauge theory and its deep-IR TQFT — i.e. is magic a confinement order parameter (with the anti-flatness witness promoted to an intrinsic measure via Clifford orbits, flagged by the authors as undeveloped in a QFT context)? → [[magic-and-confinement-phases]], cf. [[entanglement-as-confinement-probe]].
6. Is the holographic **embezzlement cost / capacity** related to magic — the departure from the flat-spectrum **fixed-area** (stabilizer-like) states that both frameworks privilege? → [[holographic-fixed-area-magic-embezzlement]]

## Related Papers

- [[2026-goto-rethinking-qi-gravity-fields]] — the QI-in-gravity agenda; this paper concretely answers part of its "resource theory in QFT" theme with a fully-worked resource (magic).
- [[2025-liu-lectures-entanglement-vna]] — the type III₁ / modular / crossed-product background the argument rests on.
- strings-2026-open-questions — Dabholkar's Strings 2026 question on modular-invariant entanglement entropy in gravity (same author, same modular frontier).
- Tirrito, Tarabunga, Lami et al. (2024), *Quantifying nonstabilizerness through entanglement spectrum flatness*, PRA 109 L040401 [2304.01175] — the flatness/anti-flatness witness lifted here to QFT.
- Cao, Cheng, Hamma, Leone, Munizzi, Oliviero (2025), *Gravitational Backreaction is Magical*, PRX Quantum 6 040375 [2403.07056] — the $F_2$ stabilizer-distance bound and the holographic magic story.
- White, Cao, Swingle (2021), *Conformal field theories are magical*, PRB 103 075145 [2007.01303] — magic in CFT on the lattice.
- Chemissany, Gesteau, Jahn, Murphy, Shaposhnik (2025), *On infinite tensor networks, complementary recovery and type II factors* [2504.00096] — the type II / tensor-network side of the holographic discussion (Gesteau again; cf. strings-2026-open-questions).

## See Also

- [[magic-nonstabilizerness]] — the concept page.
- [[type-iii-algebras-across-areas]] — updated to carry magic as a fourth III₁-rooted resource.
- [[bisognano-wichmann-theorem]], [[reeh-schlieder-theorem]], [[type-iii-von-neumann-algebras]] — the three structural inputs.
