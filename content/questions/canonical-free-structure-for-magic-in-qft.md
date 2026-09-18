---
title: Does a local QFT canonically supply the free structure that magic requires — or is magic irreducibly frame-dependent?
type: question
status: open
areas: [relative-entropy-qft, bell-inequalities-qft]
priority: high
originated: 2026-08-17
---

## Statement

[[magic-nonstabilizerness|Magic]] is not a property of a state on an algebra. It is a property of an **enriched object**
$$(\mathcal{M},\,\mathcal{W},\,\mathfrak{F},\,\mathfrak{O},\,\omega)$$
— algebra, distinguished Weyl (Pauli) system, free-state set, free-operation class, state. In finite dimensions the enrichment is handed to you: $\mathcal{W}=$ the Pauli group, $\mathfrak{F}=$ the stabilizer polytope, $\mathfrak{O}=$ stabilizer protocols. In a local QFT nothing hands it to you.

**The question:** does a Haag–Kastler net ([[haag-kastler-axioms]]) possess a canonical enrichment — one compatible with isotony, covariance, local normality, and the scaling limit — that can play the role of the Pauli/Clifford datum? Or can one prove that any such choice is necessarily regulator-, representation-, or model-dependent, and characterize the **minimal extra datum** that must be declared?

Sharply: modular theory supplies the divergences. It does not supply $\mathcal{W}$.

## Why It Matters

[[2026-benedetti-magic-in-qft|Benedetti–Dabholkar–Dalmonte]] established that every physical state of a local QFT is necessarily magical — a **witness**, forced by the continuous [[bisognano-wichmann-theorem|Bisognano–Wichmann]] spectrum and [[type-iii-von-neumann-algebras|type III₁]] structure. The natural next move is to make it **quantitative**: how much magic? That move is blocked, and this question is the blockage.

- The block is not technical difficulty. It is a **no-go**: no automorphism-invariant functional of $(B(\mathcal{H}),\rho)$ can be a faithful magic measure, because every automorphism of a finite type-I factor is inner while stabilizerness is invariant only under the Clifford normalizer. One qubit already settles it (see below).
- Type III₁ makes the situation *worse* for quantification, not better: if every faithful normal state has the same full positive modular spectral support, that support cannot order states by magic.
- Answering it either way is publishable. A canonical enrichment would be a genuinely new structure in AQFT; a proof that none exists, with the minimal declared datum characterized, is a clean structural theorem of exactly the kind the group's type III₁ programme produces.
- It is **the same problem as OQP 2.5** ([[free-states-and-operations-for-resource-theory-in-qft]]), reached independently from the magic side rather than the resource-theory side. That convergence is itself evidence the problem is the right one.

## What We Know

**The no-go is exact and elementary.** Let $\rho_\epsilon^+=(1-\epsilon)|+\rangle\langle+|+\epsilon\mathbf1/2$ and $\rho_\epsilon^A=T\rho_\epsilon^+T^\dagger$ with $T=\mathrm{diag}(1,e^{i\pi/4})$. Bloch vectors $(1-\epsilon)\hat x$ and $\frac{1-\epsilon}{\sqrt2}(1,1,0)$: the first sits inside the stabilizer octahedron always, the second outside for $0<\epsilon<1-1/\sqrt2$. Identical spectra, unitarily equivalent modular operators, opposite verdicts. *Qualification:* in a fixed representation with a fixed basis, $\Delta_\rho$ can encode $\rho$ and hence its magic — but the basis has then silently supplied $\mathcal{W}$. The obstruction is to an **intrinsic, covariant** definition, which is precisely what AQFT should demand.

**The obvious candidate for $\mathfrak{F}$ fails.** Replacing "stabilizer" by "quasifree" — the natural Pauli $\to$ [[weyl-operators|Weyl]], stabilizer $\to$ Gaussian dictionary — defines
$$N_O(\omega)=\inf_{\varphi\in\mathfrak{F}^{\mathrm{qf}}_O}S_{\mathcal{A}(O)}(\omega\Vert\varphi),$$
a perfectly good algebraic quantity. But a free-field vacuum **is** quasifree, so $N_O(\omega_0)=0$ — while that same vacuum is non-stabilizer by the anti-flatness criterion. So $N_O$ is *relative modular non-Gaussianity*, a third resource, not magic. Any proposal must survive this test.

**What survives the passage to type III.** The divergence machinery does: [[araki-uhlmann-relative-entropy|Araki relative entropy]] and Petz–Rényi divergences are built from $\Delta_{\varphi|\omega}$, so $M_{\mathfrak{F}}(\omega)=\inf_{\varphi\in\mathfrak{F}}[-\langle\xi_\omega,\log\Delta_{\varphi|\omega}\xi_\omega\rangle]$ is well-posed the moment $\mathfrak{F}$ is named, and positivity, faithfulness, convexity, and monotonicity under free channels all follow from general resource theory. That is the template. The content is entirely in $\mathfrak{F}$.

**What does not survive.** Mana needs a discrete Wigner frame and does not extend. Generalized robustness extends only order-theoretically, as $\inf_\varphi D_{\max}$, not as a spectral expectation. The [[magic-nonstabilizerness|stabilizer Rényi entropy]] rewrite $M_\alpha=\log d-D_\alpha(q_\psi\Vert u)$ on $\ell^\infty(\mathcal{P}_d)$ is exact but breaks at the first step in the continuum: **an infinite Weyl group has no uniform counting measure**.

Full development, benchmarks, and the claim ledger: quantum-magic-modular-qft-study.

## Possible Approaches

1. **Net-compatible axioms for $\mathfrak{F}_O$ (highest value).** Propose free-state families satisfying isotony under restriction, covariance, local normality, lower semicontinuity, stability under a declared class of local channels, and compatibility with spacelike composition. Then either exhibit one or prove the axioms are jointly unsatisfiable. Either outcome is a theorem.
2. **Split inclusions as the regulator.** For $\mathcal{A}(O_1)\subset\mathcal{N}\subset\mathcal{A}(O_2)$ with $\mathcal{N}$ type I, the split property supplies a genuine tensor factorization — hence a candidate finite Weyl frame. The question is whether the collar limit is choice-independent. **Main risk, and it is the whole game: dependence on which split factor.** This is the same route the OQP 2.5 page proposes; the two should be worked together.
3. **Formalize the three-way non-equivalence.** Turn "stabilizer magic $\ne$ non-Gaussianity $\ne$ modular anti-flatness" into a proposition with the free-field vacuum as the explicit separating example. Mathematically elementary, conceptually load-bearing, and it protects every downstream claim from the naming slippage the literature is already showing.
4. **Weyl-characteristic projective limit.** Replace the commutative Pauli-distribution picture by finite Weyl subspaces and take a projective limit. High novelty, low feasibility — the missing uniform measure is a real obstruction, not a technicality.
5. **Quantify the witness instead.** Ask whether regulator-independent Rényi mutual-information differences (the anti-flatness witnesses) bound any *operational* magic cost. This keeps the frame-independence that makes the Benedetti result attractive, at the price of giving up faithfulness.

## Related Questions

- [[free-states-and-operations-for-resource-theory-in-qft]] — OQP 2.5; the same question from the resource-theory side. Work jointly.
- [[relative-entropy-magic-inequality]] — downstream: any magic ↔ relative-entropy ↔ Bell inequality must first name its free set.
- [[magic-of-coherent-squeezed-cat-states]] — the concrete computation that this question tells you how to interpret (and how not to).
- [[resource-theory-monotones-in-qft]], [[holographic-resource-theory]] — sibling OQP resource-theory questions.
- [[quantum-information-in-infinite-dimensions]] — the umbrella problem (OQP 5.1).
- [[magic-and-confinement-phases]], [[magic-and-the-gribov-horizon]] — applications that need a *quantitative* magic, hence need this answered first.
