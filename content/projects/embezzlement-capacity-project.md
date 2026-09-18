---
title: "Project — Holographic embezzlement capacity & the entanglement cost of f-routing (OQP #48)"
type: project
status: proposed
target: "IQOQI Open Quantum Problem #48 (A. May)"
priority: high
duration: ~12–15 months (parallel track)
linked_question: embezzlement-capacity-lower-bound
modified: 2026-06-19
---

# Project: Holographic embezzlement capacity & the entanglement cost of f-routing

**Target: IQOQI Open Quantum Problem #48 (Alex May, *The entanglement cost of f-routing*). Parallel track to the Bell projects; feeds the wormholes ↔ QI thread.**

> Unlike the other two projects this one is already partly in flight: a manuscript is drafted for [[holographic-dual-embezzlement-protocol]], and the open question [[embezzlement-capacity-lower-bound]] *is* the capacity statement. The group's advantage over May's discrete (rank / span-program) cutting edge is the [[type-iii-von-neumann-algebras|type III$_1$]] continuum and the [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] toolkit.

## 1. Thesis statement

Derive an operationally meaningful **lower bound on the entanglement cost of f-routing / non-local quantum computation in the continuum (type III$_1$) limit**, using [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] and the [[crossed-product-construction|crossed-product]] (type II$_\infty$) construction, and determine whether the holographic **generalized entropy is the operational capacity** — closing [[embezzlement-capacity-lower-bound]]. This complements the *discrete* rank/span-program bounds (ITCS 2025) with a *continuum* algebraic bound.

## 2. Why it fits the group (already mid-flight)

- A manuscript is **drafted** for [[holographic-dual-embezzlement-protocol]] (catalyst geometry, bulk operation, cost theorem).
- The open question [[embezzlement-capacity-lower-bound]] is the capacity statement.
- Relative-entropy results for coherent / squeezed states (Eur. Phys. J. C 85; Nucl. Phys. B 1018) give the cost toolkit; the cocycle-perturbation machinery (the algebraic-QFT course Master's project, Phase C1) computes [[entanglement-embezzlement|embezzlement]] cost on the [[crossed-product-construction|crossed product]] directly.
- Students ismael-porfirio (embezzlement) and erick-landim (vN algebras, many-body) are already on exactly this material.

## 3. Phased plan (~12–15 months)

### Phase 0 — Dictionary (3–4 wks)
Map f-routing ↔ conditional disclosure of secrets ↔ non-local computation, and the ITCS-2025 rank lower bound. Identify the continuum limit in which "entanglement cost" becomes a type III$_1$ relative-entropy quantity. **Deliverable:** positioning note linking May's problem to the embezzlement program; tie into the drafted manuscript.

### Phase 1 — Relative-entropy lower bound (6–8 wks)
Via the [[crossed-product-construction|crossed product]] (III$_1\to$ II$_\infty$, trace restored), define a finite cost for the routing/embezzlement operation and bound it below by [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] using monotonicity / data-processing. Builds on the coherent-state relative-entropy results. **Deliverable:** a continuum lower bound — *standalone result, independent of the capacity claim.* **People:** ismael-porfirio, erick-landim.

### Phase 2 — Capacity theorem (6–8 wks)
Test whether the Phase-1 bound matches the holographic generalized-entropy rate from the drafted manuscript. Match $\Rightarrow$ generalized entropy is the operational capacity (the headline of [[embezzlement-capacity-lower-bound]]); gap $\Rightarrow$ a sharp, publishable gap statement. **Deliverable:** capacity theorem or quantified gap.

### Phase 3 — Bridge to May's discrete bounds (3–4 wks)
Show the continuum bound is the scaling limit of the rank bound — or that it captures structure the rank bound misses. **Deliverable:** paper bridging QI-cryptography and AQFT.

## 4. Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| Continuum limit of f-routing cost is non-standard | High | Phase 1 relative-entropy bound stands alone; doesn't depend on the holographic claim |
| Holographic capacity match fails | Medium | Drafted manuscript de-risks Phase 2; a gap result is still publishable |

## 5. Targets & people

JHEP / Quantum / PRD. Lead: Marcelo + ismael-porfirio + erick-landim. This is the project that feeds the wormholes ↔ QI research thread directly.

## 6. Connection to existing wiki questions

- [[embezzlement-capacity-lower-bound]] — the capacity question this project closes
- [[holographic-dual-embezzlement-protocol]] — the drafted manuscript this project builds on
- [[embezzlement-cost-relative-entropy]] — the relative-entropy cost toolkit
- [[relative-entropy-interacting-theories]] — the cocycle route beyond free fields

## 7. Sequencing within the OQP program

Parallel track, driven by ismael-porfirio / erick-landim plus the drafted manuscript — does not compete with the [[long-range-bell-decay-project]] spine for the senior-collaborator bottleneck.

---

*Project plan committed 2026-06-19. Parallel to [[long-range-bell-decay-project]] and [[bell-in-type-iii-project]]. Part of the [[relative-entropy-qft]] and [[bell-inequalities-qft]] lines.*
