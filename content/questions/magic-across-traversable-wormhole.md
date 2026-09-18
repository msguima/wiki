---
title: How does opening a traversable wormhole change the magic of the two-sided state?
type: question
status: open
areas: [relative-entropy-qft, gauge-gravity-duality]
priority: medium
originated: 2026-07-21
---

## Statement

The two-sided [[thermofield-double|thermofield double]] (TFD) — dual to the eternal black hole, with the Hartle–Hawking state as its near-horizon vacuum — is a cyclic-separating state on a [[type-iii-von-neumann-algebras|type III₁]] algebra and therefore, by [[2026-benedetti-magic-in-qft|Benedetti–Dabholkar–Dalmonte]], carries non-zero [[magic-nonstabilizerness|magic]]. Opening a **[[traversable-wormholes|traversable wormhole]]** via a Gao–Jafferis–Wall (GJW) double-trace deformation acts on the two sides as a **Connes cocycle** that reshapes the modular flow. **How does the magic (anti-flatness $F_2$) of the two-sided state change when the wormhole is opened — does traversability increase or decrease it?**

## Why It Matters

The group's [[wormholes-and-quantum-information-qft|wormholes ↔ QI thread]] already asks how the GJW opening affects two III₁-rooted resources — the [[bell-chsh-across-traversable-wormhole|Bell-CHSH violation]] and the [[relative-entropy-wormhole-opening|Araki–Uhlmann relative entropy]] (as a Connes cocycle). Magic is the newly-identified third resource read off the *same* modular data, so its behavior under the *same* operation is the natural next entry — and it comes with a concrete geometric hook: the magic paper's §5 contrasts flat-spectrum **fixed-area** (stabilizer-like) states with the non-flat physical states, and the Hartle–Hawking (not Boulware) vacuum is singled out as the magical, physical one. A result of the form "opening the wormhole moves the state toward/away from the stabilizer (fixed-area) sector" would give a **quantum-information reading of traversability** and slot directly into the existing wormhole questions.

## What We Know

- **GJW = Connes cocycle.** The double-trace deformation implementing the wormhole opening is naturally a cocycle relating the deformed and undeformed modular structures — the framing already used in [[relative-entropy-wormhole-opening]].
- **Magic is modular data.** Anti-flatness is a functional of the (relative) modular operator, so the cocycle that changes the modular flow is exactly what changes the magic; the computation reuses the [[relative-entropy-wormhole-opening]] machinery.
- **Fixed-area vs. physical states.** [[2026-benedetti-magic-in-qft|The paper]] shows fixed-area states are flat/stabilizer-like and physical (cyclic-separating) states get non-flat subleading Rényi corrections via the modified cosmic-brane prescription — the language in which a "magic of the wormhole" statement would be phrased.
- **TFD baseline.** The TFD is a two-mode-squeezed state, so its wedge reduced structure — and hence a baseline anti-flatness — is computable by the same free-field methods as [[magic-of-coherent-squeezed-cat-states]].

## Possible Approaches

1. **Cocycle computation of $\Delta F_2$.** Compute the anti-flatness of the two-sided state before and after the GJW deformation using the Connes-cocycle relation between the two modular operators; extract the sign and magnitude of the change.
2. **Free-field TFD model.** In a free-field / generalized-free-field model of the two sides, build the deformed reduced density matrix explicitly (as for coherent/squeezed states) and evaluate $F_2$ directly, paralleling the group's relative-entropy-of-opening computation.
3. **Fixed-area basis reading.** Express the deformed state in the fixed-area (flat) basis and quantify its departure — the "magic distance" from the nearest fixed-area state — as the traversability is dialed.
4. **Triangulate with Bell and relative entropy.** Plot magic, Bell-CHSH, and relative entropy of opening together as functions of the GJW coupling to see whether they move coherently (feeding [[relative-entropy-magic-inequality]]).

## Related Questions

- [[relative-entropy-wormhole-opening]], [[bell-chsh-across-traversable-wormhole]] — the sibling resources under the same GJW operation.
- [[magic-of-coherent-squeezed-cat-states]] — the free-field anti-flatness machinery reused here.
- [[holographic-fixed-area-magic-embezzlement]] — the fixed-area/embezzlement angle on the same holographic magic.
- [[relative-entropy-magic-inequality]] — whether the three resources move together.
