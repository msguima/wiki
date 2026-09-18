---
title: Does opening a traversable wormhole degrade the Bell-CHSH violation between its two sides?
type: question
status: partially-answered
areas: [bell-inequalities-qft, gauge-gravity-duality]
priority: medium
originated: 2026-06-04
---

## Statement

A maximal [[bell-chsh-inequality|Bell-CHSH]] violation (Tsirelson value $2\sqrt 2$) between two regions in a QFT vacuum — the Summers–Werner result the group works with — relies on the two algebras being **mutually commuting** (spacelike, no signaling). A [[traversable-wormholes|traversable wormhole]] is precisely a configuration in which a signal *can* pass between the two sides: the Gao–Jafferis–Wall coupling $V = g\,\mathcal{O}_L\mathcal{O}_R$ partially breaks the strict commutativity of $\mathcal{A}_L$ and $\mathcal{A}_R$. **Question:** as the coupling $g$ is turned on (opening the throat), does the achievable Bell-CHSH violation between the two boundary/wedge algebras *decrease*, and is there a quantitative trade-off "more traversability ⇒ less violation"?

## Why It Matters

- It is a sharp, *distinctive* question: it crosses the group's signature [[bell-inequalities-qft|Bell-CHSH program]] with the wormhole literature, in a way no existing wiki page covers (the [[holographic-bell-program]] and [[bell-chsh-in-holographic-setting]] consider Bell tests on a *fixed* TFD; this asks what *deforming* it does).
- It probes a genuine conceptual tension at the heart of [[er-epr|ER=EPR]]: if entanglement "is" the wormhole, what happens to the entanglement diagnostic when we use that entanglement to *signal*? A monotone trade-off would be a clean, quantitative face of the monogamy-like intuition that "using" the channel costs correlation.
- The flat-space version is computable now (vacuum on two [[rindler-wedges|wedges]] = [[thermofield-double-state|TFD]], plus a [[weyl-operators|Weyl]]-bilinear perturbation), so the question is testable, not just rhetorical.

## What We Know

- **Undeformed baseline:** complementary wedges in the vacuum/TFD give maximal violation via modular conjugation $J$ (Summers–Werner; group's Phys. Rev. D 108, 085026). This is the $g=0$ endpoint.
- **Signaling breaks the premise:** once $[\mathcal{A}_L,\mathcal{A}_R]\neq 0$ effectively (the coupling correlates the two sides through dynamics, not just the state), the CHSH operator's algebraic derivation of the bound no longer applies unchanged. Whether the *value* drops, and how fast, is open.
- **Monogamy heuristic:** in finite systems, entanglement that is "spent" on a channel is unavailable for maximal Bell violation. Whether a type III$_1$ analogue holds — and whether embezzlement evades it — is unknown.

## Possible Approaches

1. **Perturbed correlator.** Compute $\langle\mathrm{TFD}|\,e^{iV}\,\mathcal{C}\,e^{-iV}|\mathrm{TFD}\rangle$ for the Weyl-built CHSH operator $\mathcal{C}$ with $V = g\,W(f_L)W(f_R)$, in the free-field two-wedge model, to $O(g^2)$. Look for a definite-sign correction to the Tsirelson value.
2. **Modular re-derivation.** Track how the coupling deforms the modular conjugation/relative modular operator (same cocycle as [[relative-entropy-wormhole-opening]]) and feed the deformed $J$ into the Bob-operator construction; see whether the optimized violation is bounded by a $g$-dependent ceiling.
3. **Toy/finite check.** A two-mode (coupled-oscillator) caricature of the TFD with a tunable $L$–$R$ coupling, where both the "signaling capacity" and the CHSH value are elementary, to establish the qualitative trade-off before the field-theory computation.

## Progress (2026-06-04): leading-order result and a corrected framing

A leading-order pass **corrects the hypothesis above** ("the violation drops"). Model the opening as $U=e^{-iV}$, $V=g\,\phi(f_L)\phi(f_R)$. In the Heisenberg picture Alice's operator $A(g)=U^\dagger A U$ ($A\in\mathcal A_R$) develops a nonzero commutator with Bob's $B\in\mathcal A_L$:

$$[A(g),B] = ig\,[\mathcal O_L,B]\,[\mathcal O_R,A] + O(g^2) = -\,ig\,\Delta(f_L,f_B)\,\Delta(f_R,f_A)\,BA + O(g^2),$$

using $[\phi(f),W(h)]=i\Delta(f,h)W(h)$ in the free field. So the inter-wedge **signaling capacity** is a product of two Pauli–Jordan smearings,

$$\kappa(g) \equiv \lVert[A(g),B]\rVert \simeq g\,|\Delta(f_L,f_B)|\,|\Delta(f_R,f_A)|,$$

nonzero iff the coupling's right support is causally linked to Alice's region and its left support to Bob's. **This $\kappa$ is the regenesis signal.**

**Corrected conclusion.** The Tsirelson proof ($\mathcal C^2=4\mathbb 1-[A_1,A_2][B_1,B_2]$) needs $[A_i,B_j]=0$. Once $[A_i,B_j]=O(g)$, the ceiling *rises* into the PR-box regime $(2\sqrt2,4]$ — opening the wormhole does **not** lower the CHSH number (type III$_1$ keeps $\geq 2\sqrt2$ available, and signaling can push higher). What degrades is the **certification**: a CHSH value only witnesses entanglement under no-signaling, which now fails at order $\kappa(g)$. The sharp statement is therefore: *traversability converts Bell-certified wormhole entanglement into communicable correlation at rate $\kappa(g)$* — the entanglement that **is** the [[er-epr|ER bridge]] is exactly what stops being certifiable once the bridge is used to signal. The order parameter is the gap between $\langle\mathcal C\rangle$ and the signaling-fakeable part $f(\kappa)=O(\kappa)$.

**Next:** evaluate $\kappa(g)$ and the re-optimized $\langle\mathcal C\rangle_g$ in an explicit (1+1)d geometry (fixed $m$, chosen coupling supports/boost-time separation) with the group's Pauli–Jordan numerics; plot certified-violation vs. $\kappa$. Shares all inputs with [[relative-entropy-wormhole-opening]].

## Related Questions

- [[relative-entropy-wormhole-opening]] — same deformation, relative-entropy observable; shares the cocycle computation.
- [[bell-chsh-in-holographic-setting]] — Bell-CHSH on the undeformed holographic TFD.
- [[higher-spin-bell-inequalities]] — extending the Weyl/CHSH construction to the operators $\mathcal{O}_{L,R}$ that appear in the coupling.

Tracked under the [[wormholes-and-quantum-information-qft]] connection.
