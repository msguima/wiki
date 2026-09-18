---
title: Is there an inequality relating magic, relative entropy, and Bell-CHSH on type III₁ algebras?
type: question
status: open
areas: [relative-entropy-qft, bell-inequalities-qft]
priority: medium
originated: 2026-07-21
---

## Statement

The [[type-iii-von-neumann-algebras|type III₁]] structure of local algebras forces three quantum-information resources to be simultaneously present in any physical state: [[bell-chsh-inequality|Bell-CHSH]] violation, finite [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] $S(\omega\Vert\Omega)$, and now [[magic-nonstabilizerness|magic]] (anti-flatness $F_2$). **Are they quantitatively related?** Is there an inequality of the form
$$F_2(\omega) \;\le\; g\big(S(\omega\Vert\Omega)\big), \qquad \text{or} \qquad \mathcal{B}(\omega) \;\le\; f\big(S(\omega\Vert\Omega),\,F_2(\omega)\big),$$
tying the magic, the relative entropy, and the maximal Bell-CHSH value $\mathcal{B}(\omega)$ of a state $\omega$ on a wedge algebra?

## Why It Matters

The "[[type-iii-algebras-across-areas|type III₁ as the common thread]]" connection is currently **structural** — the three resources share a root — but not **quantitative**: no inequality ties their magnitudes. [[2026-benedetti-magic-in-qft|Benedetti et al.]] adds magic as a third III₁-forced resource, which makes the case for a unifying inequality stronger and gives a third measurable to correlate. Even a one-directional bound (e.g. "small relative entropy to the vacuum ⇒ bounded magic") would convert the common-thread narrative into a theorem and would be a genuinely new result at the QI/QFT interface. It directly answers Gap 3 / Project 1 of [[type-iii-algebras-across-areas]] — extended from two resources to three.

## What We Know

- **All three vanish/are-forced together at the structural level.** A flat spectrum (no magic) requires trivial modular flow, which contradicts the continuous [[bisognano-wichmann-theorem|Bisognano–Wichmann]] spectrum that also drives Bell violation and gives the relative entropy its modular definition.
- **Relative entropy already correlates with Bell in examples.** For coherent/squeezed/cat states the group has both $S(\omega\Vert\Omega)$ and the Bell-CHSH value; adding $F_2$ (via [[magic-of-coherent-squeezed-cat-states]]) gives the first empirical scatter of all three.
- **Finite-dimensional analogues exist.** Magic-vs-entanglement separations (Gu–Oliviero–Leone 2025) and stabilizer-distance bounds (Cao et al. 2024) suggest the *form* such inequalities can take; the challenge is the type III₁ (no density matrix, no trace) setting where only relative entropy and modular quantities survive.
- **Modular flow is the shared variable.** All three quantities are functionals of the (relative) modular operator, so a modular-theoretic inequality is the natural target.
- **One side of the inequality is already modular — exactly, and for free.** The relative entropy of magic *is* a relative-modular optimization: $M_{\mathrm{rel}}(\rho)=\inf_{\sigma\in\mathrm{STAB}}[-\langle\rho^{1/2},\log\Delta_{\sigma|\rho}\rho^{1/2}\rangle]$, with $\Delta_{\sigma|\rho}=L_\sigma R_{\rho^{-1}}$ in Type-I standard form, and the expression is unchanged on a type III algebra. That is a rewrite, not a result (quantum-magic-modular-qft-study, Kill test 3) — but it means the target inequality can be posed entirely in $\Delta$-language from the start.
- **The obstruction is asymmetry of the two sides.** $S(\omega\Vert\Omega)$ is intrinsic to $(\mathcal{A},\omega,\Omega)$; magic is not — it is frame-dependent, and no automorphism-invariant functional of $(\mathcal{A},\omega)$ can be a faithful magic measure. An inequality relating them is therefore **conditional on a declared free set** $\mathfrak{F}$, and its content will sit largely in that choice. Posing it without naming $\mathfrak{F}$ compares a frame-dependent quantity to a frame-independent one. See [[canonical-free-structure-for-magic-in-qft]].
- **Exact finite-dimensional anchors exist.** Verified benchmarks for the noisy $T$-injection line — closed-form $M_{\mathrm{rel}}$, its optimizer, and the full relative-modular spectrum $\{q/p,\,q/(1-p),\,(1-q)/p,\,(1-q)/(1-p)\}$ — are recorded in quantum-magic-modular-qft-study and are the natural sanity check for any conjectured bound before it is pushed to the continuum.

## Possible Approaches

1. **Empirical first.** Use the [[magic-of-coherent-squeezed-cat-states]] data to plot $F_2$ vs. $S(\omega\Vert\Omega)$ vs. $\mathcal{B}(\omega)$ across a parametrized family; look for an envelope. A conjectured inequality with a clean saturating family is a strong paper on its own.
2. **Modular-operator bounds.** Express $F_2$ and $S(\omega\Vert\Omega)$ through the spectrum of the relative modular operator $\Delta_{\Omega|\omega}$ and seek an operator inequality (e.g. via monotonicity of relative entropy under the conditional expectation onto a stabilizer-like subalgebra).
3. **Clifford-orbit averaging.** Since $F_2$ becomes the linearized stabilizer entropy after Clifford averaging, ask whether the QFT analogue of that average is controlled by a relative entropy to the "nearest flat" (Rindler/Boulware-like) reference state.
4. **Contrast with non-Gaussianity.** Check whether the inequality distinguishes magic from non-Gaussianity — i.e. whether interacting-theory corrections enter through $S(\omega\Vert\Omega)$ differently than through $F_2$.

## Related Questions

- [[canonical-free-structure-for-magic-in-qft]] — **upstream**: names the free set this inequality is conditional on.
- [[magic-of-coherent-squeezed-cat-states]] — supplies the data.
- [[embezzlement-cost-relative-entropy]] — the fourth III₁ resource (embezzlement cost) that a full unification would include.
- [[long-range-bell-decay]] — whether magic tracks the $\beta(L)$ decay of the Bell violation with separation.
- [[relative-entropy-interacting-theories]] — the interacting-theory regime where the inequality would be tested.
