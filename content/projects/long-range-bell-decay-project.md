---
title: "Project — The β(L) decay law for vacuum Bell-CHSH violation (OQP #12)"
type: project
status: proposed
target: "IQOQI Open Quantum Problem #12 (R. Verch)"
priority: highest
duration: ~12 months
linked_question: long-range-bell-decay
modified: 2026-06-19
---

# Project: The β(L) decay law for vacuum Bell-CHSH violation

**Target: IQOQI Open Quantum Problem #12 (Verch) — [[long-range-bell-decay]]. The spine of the three-project OQP program.**

> This is the rare case where a *named* open problem sits directly on machinery the group has already published. The proved endpoint (Summers–Werner, $L\to 0$) and the group's finite-$L$ [[weyl-operators|Weyl-operator]] results are the two ends of the same curve; this project fills in the middle and pins the decay rate.

## 1. Thesis statement

Establish the functional form and decay rate of the maximal vacuum [[bell-chsh-inequality|CHSH]] violation $\beta(L)$ between two spacelike-separated regions, as a two-sided estimate: a **lower bound** $\beta(L)\ge 2\sqrt{1+c(L)^2}$ from explicit [[weyl-operators|Weyl-operator]] constructions, and an **upper bound** $\beta(L)-2 \le F(L)$ from nuclearity / split-property estimates. This resolves the quantitative half of Verch's problem and ties the decay class (exponential vs. power-law) to the mass gap.

## 2. Why it fits the group (assets already in hand)

- **Core method exists** — Phys. Rev. D 108, 085026 (2023): [[weyl-operators|Weyl operators]] + [[tomita-takesaki-modular-theory|Tomita–Takesaki]], with Bob's observables generated from Alice's by modular conjugation $J$. This *is* the engine.
- **Compact-region results** — Eur. Phys. J. C 85 (2025): Bell-CHSH in [[causal-diamonds|causal diamonds]], the right geometry for finite separation $L$.
- **Optimization toolkit** — Phys. Rev. D 112 (2025): the characterized class of bounded Hermitian dichotomic operators that *optimize* the violation; needed to make $\beta(L)$ a genuine supremum.
- **Numerics** — Phys. Rev. D 110 (2024): systematic evaluation across mass, dimension, test function.
- **Proved endpoint** — Summers–Werner: $\beta = 2\sqrt{2}$ at region tangency ($L\to 0$), from [[type-iii-von-neumann-algebras|type III₁]] + Reeh–Schlieder.

## 3. Phased plan (~12 months)

### Phase 0 — Precise formulation (2–3 wks)
Define $\beta(L)$ as a supremum over admissible dichotomic pairs in two diamonds at separation $L$. Catalog status: PROVED at $L\to0$, OPEN for $L>0$. **Deliverable:** formal problem-statement note → the seeded question [[long-range-bell-decay]].

### Phase 1 — Lower bound: the violation persists (4–6 wks)
Use the modular-conjugation construction (PRD 108) and the optimal operator class (PRD 112) to compute $\beta_{\text{lower}}(L)$ for two diamonds, extending Eur. Phys. J. C 85 to explicit $L$-dependence. Extract the leading law: **massive scalar $\to e^{-mL}$; massless $\to L^{-p}$**, with $c(L)$ set by the smeared [[pauli-jordan-distribution|Pauli–Jordan]] correlator. Validate with the PRD 110 numerics. **Deliverable:** explicit lower bound — *standalone paper #1, ships regardless of Phase 2.* **People:** ismael-porfirio / erick-landim (analytics + numerics), [[silvio-paolo-sorella]], [[itzhak-roditi]].

### Phase 2 — Upper bound: the hard, novel step (8–12 wks)
Bound the supremum over **all** observables. Route: Tsirelson's bound expresses the maximal CHSH value between $\mathcal{A}(\mathcal{O}_A)$ and $\mathcal{A}(\mathcal{O}_B)$ through a maximal-correlation / operator-norm quantity; control it with **Buchholz–Wichmann–Yngvason nuclearity** and the **split property**. For massive free fields the split property gives exponential clustering $\Rightarrow \beta(L)-2 \le C\,e^{-mL}$, matching the Phase-1 class. **Deliverable:** rigorous upper bound (CMP/LMP-grade if it closes). *This is where Rainer Verch (or a Fewster-style AQFT collaborator) is decisive.*

### Phase 3 — Synthesis & extensions (4–6 wks)
Combine into the $\beta(L)$ decay-law theorem (or sharp two-sided estimate). Extend to: massless (power-law tied to *failure* of the split property — a clean physical dichotomy), higher spin (reuse the massless-spinor Haar-wavelet machinery, PRD 108 L081701; cf. [[higher-spin-bell-inequalities]]), and the Rindler/thermal setting. **Deliverable:** headline paper answering OQP #12.

## 4. Go / no-go decision points

- **After Phase 1:** the lower-bound paper ships unconditionally → guaranteed progress on OQP #12 even if Phase 2 stalls.
- **After Phase 2:** if nuclearity proves intractable, fall back to "sharp lower bound + strong numerics + conjectured matching upper bound." Still a citable advance on the named problem.

## 5. Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| Nuclearity/split machinery too heavy | Medium-high | Partner with Verch; Phase 1 is a complete standalone result |
| Massless case resists | Medium | Scope to massive first; massless as a follow-up |
| sup-over-all-observables not reducible to a tractable quantity | Medium | Use the PRD 112 operator class to argue near-optimality of the Weyl family, converting the gap into a controlled estimate |

## 6. Targets & people

PRL (headline) + PRD or CMP (long companion). Lead: Marcelo + [[silvio-paolo-sorella]]; students ismael-porfirio / erick-landim; external **Rainer Verch** (decisive for Phase 2), [[david-dudal]] optional.

## 7. Connection to existing wiki questions

- [[long-range-bell-decay]] — the open problem this project executes
- [[higher-spin-bell-inequalities]] — folded in at Phase 3
- [[impossible-measurements-qft]] — whether the optimal observables are operationally realizable

## 8. Sequencing within the OQP program

The **spine**. [[bell-in-type-iii-project]] (companion, OQP #1/26/32) rides in this project's slipstream — same Weyl/modular toolkit and people, near-free marginal cost. [[embezzlement-capacity-project]] (OQP #48) runs in parallel on a separate track. The one external dependency worth securing early is Verch's involvement for Phase 2.

## 9. Suggested next actions

1. Email Verch to warm up the AQFT side *before* the lower-bound work finishes.
2. Assign Phase 1 analytics to ismael-porfirio / erick-landim; reuse the PRD 110 numerical code.
3. Draft the Phase 0 formulation note from the PRD 108 / Eur. Phys. J. C 85 results.

---

*Project plan committed 2026-06-19. Companion to [[bell-in-type-iii-project]]; parallel to [[embezzlement-capacity-project]]. Part of the [[bell-inequalities-qft]] line.*
