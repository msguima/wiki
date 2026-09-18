---
title: "Wormholes & Holography: An Introduction"
type: paper
authors: [Kundu]
year: 2022
arxiv: "2110.14958"
doi: "10.1140/epjc/s10052-022-10376-z"
journal: "Eur. Phys. J. C 82, 447"
areas: [gauge-gravity-duality]
status: published
---

## Summary

A long (89-page) pedagogical review by Arnab Kundu (Saha Institute) on wormholes and their role in holography and the black-hole information problem. It is an *introduction*, not a research paper: the goal is to take a reader with basic general relativity and quantum mechanics through the modern story in which wormholes — classical solutions connecting two (or more) asymptotic regions — encode **quantum entanglement** and act as the geometric carriers of **quantum information** in semiclassical gravity.

The review is organized around the Euclidean/Lorentzian divide:

- **Euclidean wormholes** (§4) are saddle points of the gravitational path integral connecting separate asymptotic boundaries. The headline example is the **eternal AdS black hole**, whose two-sided geometry (an Einstein–Rosen bridge) is dual to the [[thermofield-double-state|thermofield double state]] — a maximally entangled state of two copies of the boundary CFT. This makes "geometric connectivity ↔ entanglement" concrete and is the entry point to [[er-epr|ER=EPR]]. The same section treats the resolution of the information paradox via **replica wormholes** in [[jt-gravity|JT gravity]], which reproduce the [[page-curve|Page curve]] and the [[quantum-extremal-surfaces|island formula]], and the encoding of *multipartite* entanglement in **multi-boundary wormholes**.

- **Lorentzian wormholes** (§5) require violating the averaged null energy condition (ANEC); generic matter forbids them. The review explains how holography supplies a controlled mechanism: the **Gao–Jafferis–Wall** double-trace deformation $V = g\,\mathcal{O}_L \mathcal{O}_R$ couples the two boundaries, injects negative null energy, and renders the eternal-black-hole wormhole momentarily **[[traversable-wormholes|traversable]]**. It then covers the **Maldacena–Qi** eternal traversable wormhole (a ground state of two coupled SYK systems / nearly-AdS$_2$), braneworld constructions, and **regenesis** — the reappearance of a perturbation on the far side, i.e. the gravitational dual of a quantum **teleportation** protocol.

Because the whole narrative is built on type III$_1$-flavoured entanglement of the thermofield double, modular structure, and relative-entropy/generalized-entropy reasoning, the review sits directly adjacent to the group's [[bell-inequalities-qft|Bell-CHSH]] and [[relative-entropy-qft|relative entropy]] programs and to the algebraic-QFT course's Semester II material (GJW, MSY, CPW, AAJ).

## Key Results

*(This is a review; "results" below are the landmark results it collects and explains, with the standard original attributions.)*

1. **Eternal black hole = thermofield double = two-sided wormhole** (Maldacena 2003). The maximally extended AdS–Schwarzschild geometry has two asymptotic boundaries joined by a non-traversable Einstein–Rosen bridge; the dual state is the [[thermofield-double-state|TFD]] $|\mathrm{TFD}\rangle = Z^{-1/2}\sum_n e^{-\beta E_n/2}|n\rangle_L|n\rangle_R$. Entanglement between the two boundary CFTs *is* the bridge — the seed of [[er-epr|ER=EPR]].

2. **Euclidean wormhole solutions need a source of "repulsion."** In the explicit axion–dilaton constructions (§4.1), a scalar with the right kinetic sign makes the scale factor turn around and form a throat. These constrained-instanton saddles connect otherwise-decoupled boundaries and are the origin of the **factorization puzzle**: a connected $\langle Z_1 Z_2\rangle$ contribution that does not factorize into $\langle Z_1\rangle\langle Z_2\rangle$.

3. **Replica wormholes restore unitarity.** In [[jt-gravity|JT gravity]] with end-of-world branes, replica saddles dominate the gravitational [[replica-trick-gravity|replica computation]] of fine-grained entropy past the Page time, producing the [[page-curve|Page curve]] and matching the [[quantum-extremal-surfaces|quantum-extremal-surface / island]] prescription.

4. **Multi-boundary wormholes carry multipartite entanglement.** Higher-genus and multi-boundary geometries realize GHZ-like and pairwise entanglement patterns in the dual multi-party CFT state.

5. **ANEC violation is unavoidable for traversability** (§5.1). Classical matter obeying the null energy condition keeps the throat closed (defocusing requires $\int T_{kk}\,d\lambda < 0$). A traversable wormhole therefore demands a quantum, negative-energy source.

6. **Gao–Jafferis–Wall: traversability from a double-trace coupling** (GJW 2017). Turning on $V = g\,\mathcal{O}_L\mathcal{O}_R$ between the two boundaries of the eternal black hole produces a one-loop negative null energy that opens the throat for a signal to pass. This is the central "UV-complete example" (§5.2.1) and is the mechanism the group's course treats algebraically (AAJ as a Connes-cocycle perturbation).

7. **Maldacena–Qi eternal traversable wormhole** (§5.2.2). Two SYK dots coupled by a relevant operator have a near-AdS$_2$ ground state that is an *eternal* traversable wormhole — a steady-state entangled resource rather than a one-shot opening.

8. **Regenesis = gravitational teleportation** (§5.2.4). A perturbation thrown into one side, together with the coupling $V$, reappears as a reconstructable signal on the other side — the bulk dual of the Hayden–Preskill / quantum-teleportation protocol through the wormhole.

## Methods

- **Euclidean gravitational path integral / saddle-point (instanton) methods**, introduced gently via the §2 double-well quantum-mechanics analogy (instantons interpolating between vacua as a toy "wormhole").
- **AdS/CFT dictionary** and the [[ryu-takayanagi-formula|Ryu–Takayanagi]] / generalized-entropy ($S_{\rm gen} = \mathrm{Area}/4G_N + S_{\rm bulk}$) prescription for fine-grained entropy (§3).
- **Replica trick in gravity** with end-of-world branes in [[jt-gravity|JT gravity]] (§4.2.2).
- **Energy-condition / Raychaudhuri analysis** of geodesic focusing to derive the traversability obstruction (§5.1).
- **Double-trace boundary deformations** and one-loop stress-tensor computations for the GJW mechanism (§5.2).
- **Coupled-SYK / nearly-AdS$_2$ effective (Schwarzian) description** for the eternal traversable wormhole (§5.2.2).
- Appendices on AdS$_3$ isometries and the quotient/identification construction for multi-boundary geometries.

## Relevance

This paper is the natural pedagogical "front door" to the wormhole literature already threaded through the wiki, and it sharpens several contact points with the group's own programs:

- **It collects, in one place, the wormhole/traversability physics that the algebraic-QFT course covers piecewise.** GJW (§5.2.1), Maldacena–Qi (§5.2.2), and the TFD-as-wormhole picture (§4.2.1) are exactly the bulk-side inputs of Semester II Blocks 4–5 (AAJ, MSY). The review supplies the geometric intuition that the algebra "does not see" — precisely the algebra/bulk demarcation the syllabus flags.
- **The GJW coupling $V = g\,\mathcal{O}_L\mathcal{O}_R$ is a Connes-cocycle perturbation of the TFD modular flow.** This is the formal bridge to the group's [[relative-entropy-qft|relative-entropy]] and [[crossed-product-construction|crossed-product]] machinery — see [[relative-entropy-wormhole-opening]].
- **Bell-CHSH between the two boundaries.** The TFD is the canonical state on which the group already studies Bell-CHSH (course Sem II Wk 8). Traversability *adds signaling* between the two sides, raising the sharp question of whether opening the wormhole degrades the Tsirelson violation — see [[bell-chsh-across-traversable-wormhole]].
- **Regenesis ↔ embezzlement.** The eternal traversable wormhole is a steady entangled resource through which information passes; this resonates with [[entanglement-embezzlement|entanglement embezzlement]] in [[type-iii-von-neumann-algebras|type III$_1$]] algebras (Porfirio, Landim) — see [[wormholes-and-quantum-information-qft]].

## Questions Raised

1. Does the GJW double-trace coupling, treated as a cocycle perturbation, change the [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] between the TFD and the deformed state in a way computable in a free-field two-wedge analogue? → [[relative-entropy-wormhole-opening]]
2. Is there a quantitative trade-off between **traversability** (signaling across the throat) and **Bell-CHSH violation** (which presumes the two algebras commute)? → [[bell-chsh-across-traversable-wormhole]]
3. Can regenesis / wormhole teleportation be cast as an (approximate) embezzlement protocol on a type III$_1$ resource, giving the cost a relative-entropy meaning? → [[holographic-dual-embezzlement-protocol]]
4. Does the Euclidean-wormhole **factorization puzzle** have anything to say about, or borrow from, [[large-n-factorization|large-$N$ factorization]] of single-trace operators — the same factorization statement that makes the boundary algebra type III$_1$?

## Related Papers

- [[2025-liu-lectures-entanglement-vna]] — Liu's review; develops the algebraic ER=EPR and crossed-product side of the same story.
- Maldacena, Qi (2018), *Eternal traversable wormhole* (arXiv:1804.00491) — the §5.2.2 construction; already a key paper in [[gauge-gravity-duality]] and the AQFT course.
- Gao, Jafferis, Wall (2017), *Traversable wormholes via a double trace deformation* (arXiv:1608.05687) — the §5.2.1 mechanism; AQFT course Sem II Wk 11.
- Maldacena, Stanford, Yang (2017), *Diving into traversable wormholes* (arXiv:1704.05333) — AQFT course Sem II Wk 14.
- Ahmad, Jefferson (2025), *Algebraic perturbation theory: traversable wormholes and generalized entropy* (arXiv:2501.01487) — the algebraic/cocycle treatment of GJW; AQFT course Block 4.
- Maldacena (2003), *Eternal black holes in AdS* (arXiv:hep-th/0106112) — the TFD/eternal-BH foundation (held in Zotero, key UNERBER6).
