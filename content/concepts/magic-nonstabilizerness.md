---
title: Magic (Nonstabilizerness)
type: concept
areas: [relative-entropy-qft, bell-inequalities-qft, condensed-matter-connections]
aliases: [magic, nonstabilizerness, non-stabilizer-ness, stabilizer Rényi entropy, anti-flatness]
modified: 2026-08-18
---

## Definition

**Magic** (or **nonstabilizerness**) is the quantum-information resource that quantifies how far a quantum state is from the set of **stabilizer states**. Stabilizer states are the states preparable from a reference state using only **Clifford operations** (the normalizer of the Pauli group); by the **Gottesman–Knill theorem** they can be simulated classically in polynomial time. Magic is therefore the ingredient a state must have to enable a genuine quantum-computational advantage / universal quantum computation (Bravyi–Kitaev): Clifford + magic = universality.

Magic is a **property of a single state**, not a correlation between subsystems — this is what distinguishes it sharply from **entanglement**. A stabilizer state can be maximally entangled (a Bell pair is a stabilizer state) yet has *zero* magic; conversely magic can be large in a product state. The two resources are independent in general, but linked through one structural fact used heavily in QFT:

> **Flatness ⟺ stabilizer (necessary condition).** For a pure stabilizer state, the reduced density matrix on any region is proportional to a projector, so all its **Rényi entropies coincide**: the *entanglement spectrum is flat*, $S_n(A)=\log\lambda_A$ independent of the Rényi index $n$, and stays flat under Clifford operations. Hence a **non-flat entanglement spectrum is a witness of magic** (Tirrito et al. 2024).

**Anti-flatness.** A convenient $n$-resolved witness is
$$F_n(\rho_A) = \mathrm{Tr}(\rho_A^{n+1})\,\mathrm{Tr}(\rho_A^{n-1}) - \mathrm{Tr}(\rho_A^n)^2,$$
which vanishes iff the spectrum is flat. The $n=2$ case is the most informative: after averaging over a Clifford orbit it reproduces the **linearized stabilizer entropy**, and it lower-bounds the distance to the stabilizer set, $F_2(\rho_A)/8 \le \min_{\sigma\in\mathrm{STAB}}\lVert\psi-\sigma\rVert$ (Cao et al. 2024).

### The resource theory in one line

Magic is the entanglement-theory machine with different gears: free states $\to$ the **stabilizer polytope** $\mathrm{STAB}=\mathrm{conv}\{\text{pure stabilizer states}\}$ (in place of separable states), free operations $\to$ **stabilizer protocols** (Cliffords, Pauli measurements, stabilizer ancillas, partial trace, feed-forward — exactly the Gottesman–Knill-simulable set, in place of LOCC), and a monotone is any $M$ vanishing on the free set and non-increasing under the free operations. The full datum is therefore *not* $(\mathcal{M},\rho)$ but
$$(\mathcal{M},\,\mathcal{P},\,\mathfrak{F}_\mathcal{P},\,\mathfrak{O}_\mathcal{P},\,\rho),$$
and the whole difficulty of exporting magic to QFT is that a net supplies the first and last entries but not the middle three ([[canonical-free-structure-for-magic-in-qft]]).

| Measure | Domain | Additivity | Computability | Operational meaning |
|---|---|---|---|---|
| Relative entropy of magic $M_{\mathrm{rel}}=\min_{\sigma\in\mathrm{STAB}}D(\rho\Vert\sigma)$ | mixed | non-additive | hard (convex opt.) | distinguishability from the free set — **the modular-native one** |
| Robustness $\mathrm{RoM}$ ($\ell_1$ of a signed stabilizer expansion) | mixed | sub­multiplicative | LP, few qubits | quasiprobability simulation cost, $N_{\text{samples}}\sim\mathrm{RoM}^2$ |
| Stabilizer extent $\xi$ | pure | multiplicative (few-qubit) | LP, few qubits | stabilizer-rank simulation cost |
| Mana $\mathcal{M}=\log\lVert W_\rho\rVert_1$ | odd qudits | **additive** | easy | Wigner negativity; distillation bounds |
| Stabilizer Rényi entropy $M_\alpha$ | pure | additive | **easy** ($4^n$ Pauli moments) | chaos diagnostics; measurable by randomized measurements |

There is no best measure, only a division of labour: $M_\alpha$ is the workhorse (tractable, replica-friendly, field-theory portable), $\mathrm{RoM}$/$\xi$/mana carry the sharpest operational meanings, and $M_{\mathrm{rel}}$ is the one that survives the passage to type III. For qubits mana is unavailable — no qubit Wigner function is simultaneously Clifford-covariant and non-negative exactly on the stabilizer states.

$M_\alpha$ deserves its own gloss, because it is the one that reaches field theory. With $q_\psi(P)=\frac1d\langle\psi|P|\psi\rangle^2$ the **Pauli probability distribution** (normalized by Parseval, $\sum_P\langle P\rangle^2=d$), $M_\alpha(\psi)=H_\alpha(q_\psi)-\log d$; a stabilizer state has $q_\psi$ uniform on the $d$ elements of its stabilizer group, so $M_\alpha=0$. Magic is thus the **delocalization of the state in the Pauli frame** — operator-space participation — which is why it couples naturally to operator spreading and chaos, and why Hoshino–Oshikawa–Ashida can write it as a replicated path integral with a line defect whose universal constant is an Affleck–Ludwig $g$ factor.

## Role in Research

Magic entered this wiki through [[2026-benedetti-magic-in-qft|Benedetti–Dabholkar–Dalmonte (2026)]], which proves that **every physically relevant state of a local QFT necessarily has non-zero magic**. The result is not a lattice statement dressed up — it is forced by the same algebraic structure the group's whole program relies on:

- By the [[reeh-schlieder-theorem|Reeh–Schlieder theorem]], the vacuum and states resembling it at short distances are **cyclic and separating** for every local algebra, hence define **faithful normal states**.
- By the [[bisognano-wichmann-theorem|Bisognano–Wichmann theorem]], the vacuum wedge modular operator is $\Delta_\Omega=e^{-2\pi K}$ ($K$ = boost generator), whose spectrum is the **continuous** real line.
- Because local algebras are [[type-iii-von-neumann-algebras|type III₁]], the Connes invariant $S(\mathcal{A})=\{0\}\cup\mathbb{R}^+$ is continuous.

A flat entanglement spectrum requires a modular operator proportional to the identity (trivial modular flow) — a **type-I / discrete** feature incompatible with a faithful normal state on a type III₁ factor. So **magic in QFT is a shadow of type III₁**, exactly the property that also makes vacuum [[bell-chsh-inequality|Bell-CHSH]] violation natural and makes the [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] the right entropy. This places magic as a **fourth vertex** on the [[type-iii-algebras-across-areas|type III₁ common-thread]] diagram alongside Bell violation, relative entropy, and [[entanglement-embezzlement|embezzlement]].

Two features make it immediately actionable for the group:

1. **It is computable with tools already in hand.** The anti-flatness $F_2$ is read off the *same* Rindler-wedge reduced density matrices and free-field Bogoliubov coefficients used in the relative-entropy and Bell-CHSH computations — so the group's coherent / squeezed / [[cat-states|cat states]] can be assigned a magic content directly ([[magic-of-coherent-squeezed-cat-states]]).
2. **It is a phase diagnostic.** Magic sharply separates **local QFT** (magical, type III₁) from **TQFT** (can be stabilizer: the [[toric-code|toric code]] has a flat spectrum, $Z[\mathcal{M}_n]=(Z[\mathcal{M}_1])^n D^{n-1}$, and is *not* a net of type III₁ factors). This is a different cut than non-Gaussianity (free vs. interacting), and it links to [[topological-order]], [[string-net-condensation]], and confinement / [[higher-form-symmetries|higher-form symmetry]] ([[entanglement-as-confinement-probe]]).

## Relations

- [[type-iii-von-neumann-algebras]] — the continuous Connes spectrum of type III₁ is precisely what forbids the flat spectrum of a stabilizer state; magic is forced by the algebraic type
- [[bisognano-wichmann-theorem]] — fixes the continuous-spectrum vacuum modular operator that makes the spectrum non-flat
- [[reeh-schlieder-theorem]] — guarantees physical states are cyclic-separating (faithful normal), the hypothesis of the argument
- [[tomita-takesaki-modular-theory]] — trivial modular flow ⟺ flat spectrum ⟺ stabilizer; non-trivial modular flow ⟺ magic
- [[araki-uhlmann-relative-entropy]] — the other III₁-native quantity, and the one that carries the relative modular operator $\Delta_{\sigma|\rho}$ in which $M_{\mathrm{rel}}$ is exactly expressible; a putative magic ↔ relative-entropy inequality is [[relative-entropy-magic-inequality]]
- [[canonical-free-structure-for-magic-in-qft]] — the structural blockage between the witness and a quantitative measure; quantum-magic-modular-qft-study is the internal study that establishes it
- [[weyl-operators]] — the continuum Weyl system that the Pauli group is the finite model of; the stabilizer formalism *is* finite Heisenberg–Weyl theory, with $(\Gamma,\sigma)$ replaced by $(\mathbb{Z}_2^{2n},[\cdot,\cdot])$ and stabilizer states = Lagrangean subspace + sign pattern
- [[bell-chsh-inequality]] — shares the cyclic-separating / BW root; both are readings of the continuous modular spectrum
- [[entanglement-embezzlement]] — sibling III₁-rooted resource in the [[type-iii-algebras-across-areas|common-thread]] program
- [[rindler-wedges]], [[squeezed-states]], [[cat-states]] — the free-field setting where anti-flatness is explicitly computable
- [[replica-trick-gravity]] — the replica/conical-defect route to the same non-flatness conclusion
- [[topological-order]], [[toric-code]], [[string-net-condensation]] — the TQFT sector where stabilizer (flat) states *are* allowed

## Papers

- [[2026-benedetti-magic-in-qft]] — universality of magic in local QFT (the source; full references therein).
- quantum-magic-modular-qft-study — internal study (Aug 2026): the modular formulation, the frame-dependence no-go, the three-resource taxonomy, and verified single-qubit benchmarks.
- Foundational QI: Bravyi–Kitaev (2005), Howard–Wallman–Veitch–Emerson (2014); resource theory: Veitch–Mousavian–Gottesman–Emerson (2014, $M_{\mathrm{rel}}$ and mana), Howard–Campbell (2017) and Heinrich–Gross (2019, robustness), Bravyi–Gosset (2016) and Bravyi et al. (2019, extent), Leone–Oliviero–Hamma (2022, SRE) with monotonicity for $\alpha\ge2$ by Leone–Bittel (2024), Deckers et al. (2026, closest stabilizer states and nonadditivity of $M_{\mathrm{rel}}$).
- Witnesses: Tirrito et al. (2024, anti-flatness), Cao et al. (2024, stabilizer-distance bound and holographic magic); CFT/lattice: White–Cao–Swingle (2021), Hoshino–Oshikawa–Ashida (2026), Tarabunga–Tirrito–Dalmonte (2023), Matsuda–Hoshino–Ashida (2026, convolution MRE unifying spins/bosons/fermions); chaos/gravity: García-García–Liu–Zheng (2026, fermionic anti-flatness in SYK with a gravity dual).

## Notes

- **Frame-dependence, stated precisely.** Stabilizerness depends on the choice of Pauli/Weyl frame, and this is not a lattice artefact that the algebraic description washes out — it is a **no-go**. No functional of the abstract pair $(B(\mathcal{H}),\rho)$ alone can be a faithful magic measure: every automorphism of a finite type-I factor is inner, so $\rho$ and $U\rho U^\dagger$ are abstractly isomorphic, while stabilizerness is invariant only under the Clifford normalizer. One qubit settles it — $\rho_\epsilon^+$ and $T\rho_\epsilon^+T^\dagger$ have identical spectra and unitarily equivalent modular operators, yet the first is free and the second is magic for $0<\epsilon<1-1/\sqrt2$. The right reading of the QFT statements is therefore: the **witness** (non-flatness) is frame-independent and rests only on modular structure; a **quantitative monotone** is not, and still requires the frame as declared data. See [[canonical-free-structure-for-magic-in-qft]] and quantum-magic-modular-qft-study.
- **Three resources, one name — and they are provably inequivalent.** (i) *Stabilizer magic*, free set = the stabilizer polytope; (ii) *non-Gaussianity*, free set = quasifree/Gaussian states; (iii) *modular anti-flatness*, where flat spectra are the excluded free-like behaviour. The separating example is the free-field vacuum itself: it **is** quasifree, so any quasifree-distance measure returns **zero** — yet it has nontrivial local modular structure and is non-stabilizer by the anti-flatness criterion. So "distance to Gaussian" is not QFT magic, and the Weyl $\to$ Pauli, quasifree $\to$ stabilizer dictionary is an analogy, not an equality. Entanglement is a fourth, independent axis (a Bell pair is a maximally entangled stabilizer state).
- **Large-$N$ particle states flatten.** Benedetti et al. find the anti-flatness of Unruh $N$-particle states *decreases* as $N\to\infty$, seemingly approaching a flat (stabilizer-like) spectrum — but that limit is a singular state outside Fock space, so it does not violate the universality result. Whether *superposition* states (cat states) run the opposite way is an open computation ([[magic-of-coherent-squeezed-cat-states]]).
- **Measure vs. witness.** Flatness/anti-flatness is a *witness* (necessary condition). Turning it into an intrinsic *measure* of magic in QFT — via averaging over Clifford orbits — is flagged by the authors as not yet developed in a QFT context, and is itself a research target. The 2026-08 study makes the gap structural rather than merely undeveloped: type III₁ supplies the obstruction but no Pauli group, no Clifford normalizer, no convex free set, no free operations, and no operational task; and if every faithful normal state shares the same full positive modular spectral support, that support cannot order states by magic at all.
- **What *does* transfer to type III.** The divergence machinery. In Type-I standard form, $M_{\mathrm{rel}}(\rho)=\inf_{\sigma\in\mathrm{STAB}}[-\langle\rho^{1/2},\log\Delta_{\sigma|\rho}\,\rho^{1/2}\rangle]$ with $\Delta_{\sigma|\rho}=L_\sigma R_{\rho^{-1}}$ — an exact rewrite whose form is unchanged on any von Neumann algebra once a free set is named. Stabilizer Rényi entropy likewise: $M_\alpha=\log d-D_\alpha(q_\psi\Vert u)$ is a classical Rényi divergence on the commutative $\ell^\infty(\mathcal{P}_d)$. Both are reformulations, not new monotones, and the second has a hard continuum obstruction — an infinite Weyl group has no uniform counting measure.
