---
title: "The gravity/QI open-problems agenda (Goto et al.) and the group's toolkit"
type: connection
areas: [gauge-gravity-duality, bell-inequalities-qft, relative-entropy-qft]
maturity: developing
modified: 2026-06-30
---

## The Link

[[2026-goto-rethinking-qi-gravity-fields|Goto et al. (arXiv:2606.30853)]] is a curated open-problems agenda from the **holography/QI community**, organized into four themes: operational characterization of observables, the role of observers, quantum error correction, and the infinite-dimensionality of Hilbert spaces. Read against the group's programs, it is a second, independent open-problems list — a holography-side sibling of the IQOQI triage that produced [[long-range-bell-decay-project]], [[bell-in-type-iii-project]], and [[embezzlement-capacity-project]].

The striking fact is the overlap. Two of the four themes are *exactly* where the group's flat-space, type III₁, modular-theory toolkit already operates:

- **Theme 4 (infinite-dimensional Hilbert spaces / type II–III algebras)** is the algebraic home of the group's [[relative-entropy-qft|Araki–Uhlmann relative entropy]], [[entanglement-embezzlement|embezzlement]], and [[crossed-product-construction|crossed-product]] work.
- **Theme 1 (operational characterization / resource theory in holography)** is the thesis of the group's [[embezzlement-capacity-project|generalized-entropy-as-capacity]] result.

The other two themes (observers, QEC) are where the group is a well-positioned *consumer* rather than a producer.

## Evidence

- **Finite information on type III₁ is already built.** The group's 2025 papers compute [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] for [[coherent-states|coherent]], [[squeezed-states|squeezed]], and [[cat-states|cat]] states — finite quantities on algebras where von Neumann entropy is UV-divergent. That is a concrete instance of the "QI in infinite dimensions" the paper's §5 asks for, not a promissory note.
- **Embezzlement is native to III₁.** The group (Porfirio, Landim) studies [[entanglement-embezzlement|embezzlement]] in [[type-iii-von-neumann-algebras|type III₁]] and the [[embezzlement-capacity-lower-bound|rate/capacity]] question; van Luijk–Stottmeister–Werner–Wilming (2024) established embezzlement in QFT. This is Theme 4 machinery in hand.
- **Operational characterization, made into a theorem.** The [[holographic-dual-embezzlement-protocol|holographic-embezzlement manuscript]] proves a bound $1-F_d \lesssim \log d / S_{\text{gen}}$ and conjectures a matching lower bound that would make **generalized entropy the operational capacity** — a literal answer to Theme 1's "characterize holographic observables by the tasks they enable."
- **Tsirelson is the III₁ Bell obstruction.** Theme 4 names the Tsirelson problem (tensor vs. commuting-operator correlations, $\mathrm{MIP}^*=\mathrm{RE}$). Wedge algebras commute but do not tensor-factorize — exactly the commuting-operator setting — which is the algebraic crux of [[bell-in-type-iii-project]] and the ceiling on [[long-range-bell-decay|vacuum Bell-CHSH]].
- **The observer's algebra is course material.** Theme 2's dynamical, type-II observer is CLPW/CPW ([[crossed-product-construction|crossed product]]), taught in AQFT Semester II (syllabus).

## Gaps

- **The group's results are free / generalized-free field; the paper's are holographic.** The honest bridge is to present the free-field type III₁ computations as *models* of the infinite-dimensional QI the paper wants, flagging what is genuinely holographic input (as the [[wormholes-and-quantum-information-qft|wormholes thread]] already does).
- **Capacity, not yet proved.** The generalized-entropy-as-capacity claim is a *bound* until the [[embezzlement-capacity-lower-bound|lower bound]] is closed; Theme 1's "operational characterization" is only fully answered when it is.
- **Themes 2–3 need bulk input the flat-space toolkit does not supply.** Observer backreaction and non-isometric codes are bulk/holographic statements; the group can consume but not (yet) derive them.
- **Tsirelson link is structural, not yet computed.** That wedge algebras are commuting-operator is clear; whether the commuting-operator vs. tensor distinction changes any *number* the group computes (e.g. the achievable CHSH value or its $L$-decay) is open.

## Potential Projects

- **P1 — Position note: "the group's relative entropy + embezzlement work as QI in infinite dimensions" (most immediate).** Frame the 2025 relative-entropy papers and the embezzlement-capacity manuscript explicitly against §5 of Goto et al.; a short perspective/letter staking the claim that finite Araki–Uhlmann quantities *are* the infinite-dimensional QI the agenda calls for. Low technical risk, high visibility.
- **P2 — Tsirelson obstruction for vacuum Bell-CHSH (most fundamental).** Make precise whether the commuting-operator character of wedge algebras (vs. any tensor-factorized model) constrains the achievable Bell-CHSH value or its [[long-range-bell-decay|β(L) decay]]. Feeds [[bell-in-type-iii-project]] directly.
- **P3 — Generalized entropy as operational capacity (most distinctive).** Close the [[embezzlement-capacity-lower-bound|lower bound]] so the [[embezzlement-capacity-project|capacity result]] answers Theme 1's operational-characterization challenge with a theorem, not a slogan.
- **P4 — Observer-algebra Bell-CHSH (most speculative).** Redo a Bell-CHSH / relative-entropy computation on the type-II crossed-product "observer's algebra," giving a bounded-energy physical observer and possibly sidestepping [[impossible-measurements-qft|impossible measurements]]. Connects Theme 2 to [[bell-chsh-in-holographic-setting]].

## Related

- [[2026-goto-rethinking-qi-gravity-fields]] — the paper page carries the full catalogue of all 20 problem pages, grouped by theme.
- strings-2026-open-questions — the string-theory community's parallel open-problems list (Ooguri, Strings 2026); the QI/QG subset (Dabholkar EE-in-gravity, Gesteau emergence, Chester finite-N, Takayanagi holography-as-quantum-computer) maps this agenda from the other side.
- The group-tractable spin-offs: [[quantum-information-in-infinite-dimensions]] (5.1), [[tsirelson-problem-vacuum-bell-chsh]], [[relative-entropy-embezzlement-as-infinite-dim-qi]], [[observer-algebra-bell-chsh]], [[dynamical-observer-backreaction-and-algebra]] (3.4), [[holographic-resource-theory]] (2.8), [[qft-correlators-as-information-tasks]] (2.3).
- [[long-range-bell-decay-project]], [[bell-in-type-iii-project]], [[embezzlement-capacity-project]]
- [[wormholes-and-quantum-information-qft]], [[type-iii-algebras-across-areas]], [[holographic-bell-program]], [[crossed-product-and-island-formula]]
- [[embezzlement-capacity-lower-bound]], [[holographic-dual-embezzlement-protocol]], [[bell-chsh-in-holographic-setting]], [[long-range-bell-decay]]
- [[gauge-gravity-duality]], [[bell-inequalities-qft]], [[relative-entropy-qft]]
