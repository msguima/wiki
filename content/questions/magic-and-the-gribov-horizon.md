---
title: Does the Gribov horizon change the magic of the confining vacuum?
type: question
status: open
areas: [gribov-zwanziger, confinement-duality, relative-entropy-qft]
priority: medium
originated: 2026-07-21
---

## Statement

[[2026-benedetti-magic-in-qft|Benedetti–Dabholkar–Dalmonte]] prove that a local QFT vacuum is necessarily **[[magic-nonstabilizerness|magical]]** because it is cyclic-separating ([[reeh-schlieder-theorem|Reeh–Schlieder]]), has the continuous [[bisognano-wichmann-theorem|Bisognano–Wichmann]] modular spectrum, and lives on a [[type-iii-von-neumann-algebras|type III₁]] algebra. The **[[refined-gribov-zwanziger|Refined Gribov–Zwanziger]]** vacuum satisfies none of these hypotheses in an obvious way: the functional integral is restricted to the first Gribov region, the propagators have complex conjugate poles (no Källén–Lehmann positivity), and [[reeh-schlieder-theorem|Reeh–Schlieder]] is not known to hold. **Does the Gribov-horizon restriction change the magic content of the vacuum — and can magic (anti-flatness) therefore serve as an order parameter for confinement?**

## Why It Matters

This is the natural place where the paper's result **collides with the group's signature framework**, and only this group is positioned to push it. Two outcomes are both interesting:

- If the RGZ vacuum is *less* magical (flatter entanglement spectrum) than the standard vacuum, magic becomes a **new confinement diagnostic** — a departure from the universal "all physical states are magical" statement, signalling that the confining vacuum sits closer to the stabilizer / topological sector. The paper already isolates the stabilizer-compatible sector as **TQFT** (flat spectrum, not type III₁); a confining IR that flows toward a topological description ([[higher-form-symmetries|higher-form symmetry]] realization) would be expected to shed magic, tying to [[entanglement-as-confinement-probe]].
- If magic is *unchanged*, that is evidence the type III₁ + BW structure survives the Gribov restriction — a foundational algebraic fact the whole program tacitly assumes (Gap 4 of [[type-iii-algebras-across-areas]]) and which is currently open.

Either way it sharpens the boundary of validity of the magic universality theorem and connects the [[gribov-zwanziger]] and quantum-information lines.

## What We Know

- **RGZ modifies the vacuum non-trivially.** Complex-pole propagators, a soft BRST breaking, and the horizon function change the two-point structure that the modular operator is built from.
- **Reeh–Schlieder / BW status is open in RGZ.** The algebraic structure of the RGZ vacuum is itself unresolved — [[entanglement-as-confinement-probe]] flags that the Haag–Kastler axioms and Reeh–Schlieder are not straightforwardly applicable when the functional integral is restricted by the non-local horizon condition.
- **Anti-flatness is computable from a two-point function.** As in [[magic-of-coherent-squeezed-cat-states]], $F_2$ can be evaluated once the (modified) wedge reduced density matrix is known, so the RGZ computation is a modification of a computation the group can already do.
- **TQFT is the flat-spectrum exception.** The paper's own boundary case (topological theories can be stabilizer) is the conceptual anchor for expecting confinement — if it is a flow toward a topological IR — to reduce magic.

## Possible Approaches

1. **RGZ Rindler reduced state.** Build the wedge reduced density matrix from the RGZ (complex-pole) propagator and evaluate anti-flatness $F_2$; compare to the standard-vacuum value at matched cutoff.
2. **Modular operator under the horizon restriction.** Ask whether the restricted algebra still yields a continuous modular spectrum (type III₁) or acquires a gap / discrete component (a signature of a different algebraic type), which would show up as reduced anti-flatness.
3. **Confinement order-parameter test.** Track $F_2$ across a deconfinement transition (finite $T$, or as the Gribov parameter $\gamma\to 0$) and check whether magic behaves as an order parameter, alongside the Polyakov loop / [[wilson-loop|Wilson loop]] and [[higher-form-symmetries|higher-form symmetry]] realization.
4. **Consistency with positivity violation.** Relate any anti-flatness change to the [[spectral-positivity-violation|spectral positivity violation]] of the RGZ propagator — is lost magic tied to lost positivity?

## Related Questions

- [[entanglement-as-confinement-probe]] — the parent question on entanglement/Bell as confinement order parameters, and the RS/RGZ algebraic subtlety.
- [[magic-of-coherent-squeezed-cat-states]] — the standard-vacuum computation this modifies.
- [[bell-inequalities-with-gribov-horizon]] — the Bell-CHSH analogue of the same collision.
- [[gribov-copies-physical-observables]] — gauge-invariant observables under the Gribov restriction.
