---
title: "Immersion program — speaking the language of the entanglement–symmetries–holography school"
type: project
status: active
priority: high
duration: ~18 months (phase 0 from 2026-07)
modified: 2026-07-05
---

# Immersion program: speaking the language of the entanglement–symmetries–holography school

A personal fluency program for the research culture of eleven authors: Witten, Komargodski, Shao, Swingle, Hong Liu, Maldacena, Harlow, Stanford, Yonekura, Calabrese, Casini. The goal is not a new research project; it is to read their new papers the week they appear, follow any seminar in the area, and write in the register. Every arXiv ID below was verified against the arXiv API on 2026-07-05.

**Where this sits in the wiki.** The three reading tracks below are the personal traversal of ground the three graduate courses cover institutionally: Track A runs parallel to Generalized Symmetries and Topological Matter (`wiki/courses/generalized-symmetries-course/syllabus.md`), Track B to Estrutura Algébrica da TQC (`wiki/courses/2026-algebraic-qft-course/syllabus.md`), Track C to Gauge/Gravity Duality (`wiki/courses/ads-cft-course/syllabus.md`). The OQP pages ([[long-range-bell-decay-project]], [[bell-in-type-iii-project]], [[embezzlement-capacity-project]]) are the research arm; this page is the reading-and-culture arm that feeds them.

---

## 1. One school, three dialects

Eleven names, but one connected intellectual community organized around a single question, *what do quantum information and symmetry tell us about quantum field theory and gravity?* They cite each other constantly, share workshops and students, and Witten is the hub who has written natively in all three of its dialects.

**Dialect A — symmetry, anomaly, topology.** Komargodski, Shao, Yonekura, Witten. Symmetries as topological operators, 't Hooft anomalies as constraints on RG flow, cobordism and index theory as the bookkeeping of phases.

**Dialect B — entanglement and algebras in QFT.** Casini, Calabrese, Witten, and lately [[hong-liu|Hong Liu]]. Replica computations, modular theory, the type classification, entropic proofs of QFT theorems.

**Dialect C — holography, chaos, gravity as information.** Maldacena, Harlow, Stanford, Swingle, Liu. AdS/CFT, quantum error correction, SYK and [[jt-gravity|JT gravity]], out-of-time-order correlators, the [[page-curve|Page curve]].

Underneath all three sits a shared grammar: Euclidean path integrals cut and glued along surfaces, conformal field theory, large N, and the vocabulary of quantum information.

The group already owns a real piece of dialect B: [[tomita-takesaki-modular-theory|Tomita–Takesaki]], [[type-iii-von-neumann-algebras|type III₁]], [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]], [[weyl-operators|Weyl algebras]], [[entanglement-embezzlement|embezzlement]]. That's the beachhead. The plan builds outward from it rather than starting over.

---

## 2. Phase 0 (months 1–3): the shared grammar

Goal: open any paper by these eleven and parse the introduction without stalling.

**2d CFT and the replica trick** (the biggest gap for someone trained in AQFT):
- J. Cardy, *Conformal Field Theory and Statistical Mechanics*, arXiv:0807.3472. Short, and in Cardy's plain style.
- P. Calabrese, J. Cardy, *Entanglement entropy and conformal field theory*, arXiv:0905.4013. Do the single-interval computation by hand, twist fields and all.

**Higher-dimensional CFT**, pick one: S. Rychkov, *EPFL Lectures on CFT in D ≥ 3*, arXiv:1601.05000, or D. Simmons-Duffin, *TASI Lectures on the Conformal Bootstrap*, arXiv:1602.07982. Conformal symmetry, primaries, and the OPE are what's needed; the numerical bootstrap itself is optional. (Semester I of the AdS/CFT course covers the same grammar in course form.)

**Quantum information, hep-th register:** E. Witten, *A Mini-Introduction To Information Theory*, arXiv:1805.11965. Known material rewritten in his voice; reading it is style study as much as physics. Preskill's Ph219 notes stay on the shelf as reference.

**Algebras, the bridge documents:**
- E. Witten, *Notes on Some Entanglement Properties of Quantum Field Theory*, arXiv:1803.04993. The translation manual between AQFT training and hep-th. Deep read.
- J. Sorce, *Notes on the type classification of von Neumann algebras*, arXiv:2302.01958. Written for exactly this audience.
- H. Casini, M. Huerta, *Lectures on entanglement in quantum field theory*, arXiv:2201.13310.

**Holography, first contact:** J. Maldacena, *TASI 2003 Lectures on AdS/CFT*, arXiv:hep-th/0309246, alongside Hong Liu's MIT course 8.821 (*String Theory and Holographic Duality*, video lectures on MIT OCW). The course doubles as listening immersion. J. McGreevy, *Holographic duality with a view toward many-body physics*, arXiv:0909.0518, if a condensed-matter voice helps.

Start the daily and weekly rituals of section 6 on day one, not after the reading. Immersion means hearing the language before you can fully parse it.

---

## 3. Phase 1 (months 4–9): three tracks in parallel

Run the tracks side by side, roughly one paper per track per fortnight, using the triage of section 5. "Deep" means reproduce the calculations in a notebook. Only about 15 papers below carry that label; the rest are careful reads or scans. The ordering within each track is deliberate.

### Track A — symmetry, anomaly, topology

Feeds [[julia-toulouse-higher-form-symmetries]] and [[non-invertible-symmetries-mcs]] directly; the generalized-symmetries course is its institutional arm, and [[julia-toulouse-mechanism]] is where it re-enters the group's own history.

1. D. Gaiotto, A. Kapustin, N. Seiberg, B. Willett, *Generalized Global Symmetries*, arXiv:1412.5148. The founding document. **Deep**; work the Maxwell-theory example until the electric and magnetic 1-form symmetries are yours.
2. S.-H. Shao, *What's Done Cannot Be Undone: TASI Lectures on Non-Invertible Symmetries*, arXiv:2308.00747. **Deep.** The Ising and compact-boson examples are this school's teaching laboratory.
3. A. Kapustin, N. Seiberg, *Coupling a QFT to a TQFT and Duality*, arXiv:1401.0740. Careful. Where the symmetry ⇄ topological-sector dictionary gets fixed.
4. D. Gaiotto, A. Kapustin, Z. Komargodski, N. Seiberg, *Theta, Time Reversal, and Temperature*, arXiv:1703.00501. **Deep.** Anomaly matching used as a dynamical weapon.
5. Z. Komargodski, A. Schwimmer, *On Renormalization Group Flows in Four Dimensions*, arXiv:1107.3987. Careful. The a-theorem.
6. Z. Komargodski, *Baryons as Quantum Hall Droplets*, arXiv:1812.09253. Scan, then return. How he thinks off-road.
7. E. Witten, *Fermion Path Integrals And Topological Phases*, arXiv:1508.04715. **Deep** if the projects demand eta invariants; careful otherwise.
8. E. Witten, K. Yonekura, *Anomaly Inflow and the η-Invariant*, arXiv:1909.08775. **Deep.** The modern anomaly reference and a masterclass in the writing this program treats as the ideal (section 7).
9. K. Yonekura, *Dai-Freed theorem and topological phases of matter*, arXiv:1607.01873; *On the cobordism classification of symmetry protected topological phases*, arXiv:1803.10796. Careful.
10. Orientation surveys, scan: C. Córdova, T. Dumitrescu, K. Intriligator, S.-H. Shao, *Snowmass White Paper: Generalized Symmetries*, arXiv:2205.09545; J. McGreevy, *Generalized Symmetries in Condensed Matter*, arXiv:2204.03045.

### Track B — entanglement and algebras (home turf, extended)

Semester II of the algebraic-QFT course is this track's seminar arm; several entries below are its set texts.

1. P. Calabrese, J. Cardy, *Entanglement Entropy and Quantum Field Theory*, arXiv:hep-th/0405152, and *Time-dependence of correlation functions following a quantum quench*, arXiv:cond-mat/0601225. **Deep**: replicas, twist fields, the quasiparticle picture.
2. H. Casini, M. Huerta, *Entanglement entropy in free quantum field theory*, arXiv:0905.2562. **Deep.** Their real-time toolkit; it plugs straight into the group's correlation-matrix numerics.
3. The entropic-proof template: H. Casini, M. Huerta, *A c-theorem for the entanglement entropy*, arXiv:cond-mat/0610375; *On the RG running of the entanglement entropy of a circle*, arXiv:1202.5650; H. Casini, *Relative entropy and the Bekenstein bound*, arXiv:0804.2182. **Deep** on at least one; the Bekenstein paper is closest to the group's relative-entropy work.
4. T. Faulkner, R. Leigh, O. Parrikar, H. Wang, *Modular Hamiltonians for Deformed Half-Spaces and the ANEC*, arXiv:1605.08072. Careful.
5. H. Casini, M. Huerta, J. Magán, D. Pontello, *Entanglement entropy and superselection sectors. Part I*, arXiv:1905.10487. **Deep.** This is where Track A and Track B literally meet: symmetries seen through algebras of regions.
6. S. Hollands, K. Sanders, *Entanglement measures and their properties in QFT*, arXiv:1702.04924. Reference.
7. The Witten [[crossed-product-construction|crossed-product]] line, in order: *Why Does QFT In Curved Spacetime Make Sense?...*, arXiv:2112.11614; *Gravity and the Crossed Product*, arXiv:2112.12828; Chandrasekaran–Longo–Penington–Witten, *An Algebra of Observables for de Sitter Space*, arXiv:2206.10780; Chandrasekaran–Penington–Witten, *Large N algebras and generalized entropy*, arXiv:2209.10454; the survey *Algebras, Regions, and Observers*, arXiv:2303.02837, works as either entrance or exit. **Deep.** This is the frontier the embezzlement program borders, and the spine of the algebraic-QFT course's Semester II.
8. S. Leutheusser, H. Liu, *Causal connectability... and the black hole interior*, arXiv:2110.05497, and *Subregion-subalgebra duality: emergence of space and time in holography*, arXiv:2212.13266. **Deep.** See [[subregion-subalgebra-duality]] and [[large-n-factorization]].
9. L. van Luijk, A. Stottmeister, R. Werner, H. Wilming, arXiv:2401.07292 and arXiv:2401.07299. Known ground; reread them *after* the Witten–Liu line and notice how the same type-III facts carry different meanings in the two communities. That noticing is fluency.
10. Calabrese's current program, careful/scan via his INSPIRE page: symmetry-resolved entanglement; entanglement asymmetry and the quantum Mpemba effect. It ties entanglement to symmetry, Track B to Track A, and it's computable with tools the group already has.

### Track C — holography, chaos, gravity as information

The AdS/CFT course is this track in course form; this list is the fast personal traversal.

1. J. Maldacena, *The Large N Limit of Superconformal Field Theories and Supergravity*, arXiv:hep-th/9711200 (sections 1–3), with E. Witten, *Anti De Sitter Space And Holography*, arXiv:hep-th/9802150. Careful; the goal is the [[holographic-dictionary|dictionary]] and the [[gkp-witten-formula|GKP–Witten formula]], not the brane engineering.
2. Geometry from entanglement: [[ryu-takayanagi-formula|Ryu–Takayanagi]], arXiv:hep-th/0603001; Hubeny–Rangamani–Takayanagi, arXiv:0705.0016; M. Van Raamsdonk, *Building up spacetime with quantum entanglement*, arXiv:1005.3035; B. Swingle, *Entanglement Renormalization and Holography*, arXiv:0905.1317. Careful; Swingle's tensor-network reading is the conceptual one.
3. D. Harlow, *Jerusalem Lectures on Black Holes and Quantum Information*, arXiv:1409.1231. **Deep.** Then J. Maldacena, *Eternal Black Holes in AdS*, arXiv:hep-th/0106112 (the [[thermofield-double-state|thermofield double]] as the two-sided black hole); AMPS, *Black Holes: Complementarity or Firewalls?*, arXiv:1207.3123; Maldacena–Susskind, *Cool horizons for entangled black holes*, arXiv:1306.0533 ([[er-epr|ER=EPR]]).
4. Error correction: Almheiri–Dong–Harlow, arXiv:1411.7041 (**deep**); D. Harlow, *The Ryu-Takayanagi Formula from Quantum Error Correction*, arXiv:1607.03901; *TASI Lectures on the Emergence of the Bulk*, arXiv:1802.01040.
5. Chaos: Shenker–Stanford, *Black holes and the butterfly effect*, arXiv:1306.0622; Maldacena–Shenker–Stanford, *A bound on chaos*, arXiv:1503.01409 (**deep**); B. Swingle, *Unscrambling the physics of out-of-time-order correlators*, Nature Physics (2018), as the many-body companion.
6. SYK and JT: Maldacena–Stanford, arXiv:1604.07818, read with G. Sárosi, *AdS₂ holography and the SYK model*, arXiv:1711.08482 as guide; Maldacena–Qi, *Eternal traversable wormhole*, arXiv:1804.00491 (see [[traversable-wormholes]]); Saad–Shenker–Stanford, *JT gravity as a matrix integral*, arXiv:1903.11115, and Stanford–Witten, arXiv:1907.03363, careful/scan.
7. The Page-curve era: Penington–Shenker–Stanford–Yang, *Replica wormholes and the black hole interior*, arXiv:1911.11977 (see [[replica-trick-gravity]] and [[quantum-extremal-surfaces]]); Almheiri–Hartman–Maldacena–Shaghoulian–Tajdini, *The entropy of Hawking radiation*, arXiv:2006.06872. Careful.
8. Bridges back to Track B: Liu–Suh, *Entanglement Tsunami*, arXiv:1305.7244; M. Headrick, *Lectures on entanglement entropy in field theory and holography*, arXiv:1907.08126.

Note the loop built into the ordering: Track C ends where Track B ends, at the algebraic reformulation of holography (Witten, Leutheusser–Liu). All three tracks converge on the frontier where the group's embezzlement program already lives ([[holographic-dual-embezzlement-protocol]], [[crossed-product-and-island-formula]]). That's not an accident; it's why this particular list of authors forms a coherent school for this group specifically.

---

## 4. Phase 2 (months 10–18): production

Reading alone never produced fluency in any language.

- **Same-week reading.** New papers by the eleven (add Seiberg, Tachikawa, Penington, Magán, Huerta, Faulkner, Wall to the watchlist) get read the week they appear, tracing references backward only when actually blocked.
- **Replication projects**, two or three, small and matched to existing tools: redo a crossed-product entropy computation in a quasifree toy model reusing the group's numerical machinery (feeds [[embezzlement-cost-relative-entropy]]); compute a symmetry-resolved entropy for a free field with the correlation-matrix code; work out the non-invertible defect structure of Maxwell–Chern–Simons at small k, which is [[non-invertible-symmetries-mcs]] verbatim.
- **One internal seminar per quarter** in the school's register, with notes written like a Witten appendix.
- **Schools.** PiTP at the IAS (the 2018 edition, "From Qubits to Spacetime", has its lectures online and is itself a syllabus), TASI, Les Houches; regionally, watch the ICTP-SAIFR program in São Paulo, which runs schools on exactly these topics. Writing the application is immersion too: it forces a statement of interests in the school's language.
- **Contact.** Write to authors when there's a real question or genuine overlap, early and politely. This community answers serious email from people who have clearly read the paper.

---

## 5. How to read (triage discipline)

Four levels, applied ruthlessly:

- **Deep** (~15 papers above): reproduce every calculation; nothing skipped.
- **Careful**: introduction, results, one derivation re-done.
- **Scan**: abstract, introduction, conclusions; one line in the journal.
- **Note-only**: log the reference and move on.

For each deep paper, do the INSPIRE walk: identify its 3–5 parents from the introduction, then at least 3 children from "cited by", one journal line each. Fluency is mostly knowing the citation graph, not memorizing nodes.

Keep a **notation ledger**. The hep-th and AQFT communities genuinely clash: metric signatures, the sign in the modular Hamiltonian, factors of 2π in modular flow, mathematicians' "factor" vs. physicists' loose "algebra". One page per clash, with explicit conversion rules. This is unglamorous and it is half the language. (The wiki's notation conventions in `docs/assistant-playbook.md` are the group-side anchor.)

Keep a **folklore log**. Every time a paper says "it is well known that" with no citation, write the claim down; later, find the source or mark it folklore. That list is where referee questions and small papers come from.

---

## 6. Daily and weekly rituals

Daily, 20–30 minutes: the new listings for hep-th and quant-ph, plus cond-mat.stat-mech cross-lists for the Calabrese-adjacent material. Every title gets read; every abstract by the eleven or their frequent co-authors gets read same-day. One-line log per noted paper.

Weekly, one talk, watched actively (pause at each transition, predict what comes next, resume): IAS High Energy Theory seminars, KITP program talks, the Simons Center (SCGP) video portal, Strings conference talks, and early on, Liu's 8.821 lectures. Papers never show the spoken register, which questions get asked, what an audience challenges, how people hedge. Talks do.

Weekly, one page written: the week's deep paper summarized in the author's own voice, minimal equations. Production, not just comprehension. This is the step everyone skips and the reason most people can read this literature but not speak it.

**The phrasebook.** A running glossary of terms of art, each entry carrying (a) a definition, (b) where first encountered, (c) the move it enables. Seed entries: 't Hooft anomaly matching; stacking an SPT; gauging/orbifolding; SymTFT; topological defect line; condensation defect; half-space gauging; twist field; replica trick; modular flow; half-sided modular inclusion; crossed product; type II∞ factor; split property; code subspace; entanglement wedge; quantum extremal surface; island; OTOC; scrambling time; ramp and plateau; ensemble average; generalized free field; large-N factorization; Page time; Petz recovery. Entries that grow past a few lines graduate into `wiki/concepts/` pages.

**Results to know cold** (recite without notes; the list grows): the interval entropy (c/3)log(ℓ/ε) and where each piece comes from; the quasiparticle picture of entanglement growth after a quench; Bisognano–Wichmann (wedge modular flow = boosts); type III₁ for local algebras and which crossed products land in II∞; RT, HRT, QES statements; the chaos bound λ ≤ 2πT; [[page-curve|Page-curve]] timing; Maxwell theory's two 1-form symmetries and their mixed anomaly; the a-, c-, and F-theorem statements with proof sketches; [[entanglement-embezzlement|embezzlement]] ⇔ type III₁, the group's home result.

---

## 7. The writing apprenticeship (Witten and Yonekura)

The explicit ideal for this program's writing is Witten and Yonekura. What dissection shows:

**Witten.** Introductions state the question in words before any formula appears, explain why the naive approach fails, say exactly what will be shown, and close with a prose roadmap. Sections open by recapping where the argument stands. Each paragraph does one job. Important points are made twice, once physically and once precisely, and he tells you which register you're in. Notation arrives just before use, never in a front-loaded glossary. Mathematical precision is spent exactly where it changes the conclusion (which algebra type, which invariant) and nowhere else.

**Yonekura**, and Witten–Yonekura arXiv:1909.08775 jointly: conventions pinned completely (orientations, signs, spin structures) so the reader never guesses; heavy bookkeeping exiled to appendices so the main text reads linearly; honest flags on what is not proven.

The practice loop:
- Monthly: reverse-outline one introduction, one line per paragraph (start with arXiv:1803.04993, 2112.12828, 1909.08775). The skeleton that emerges is the template.
- Quarterly: take one section of a current group draft (the embezzlement manuscript is the natural subject) and rewrite it to the template; diff against the original; keep what improved.
- After every deep paper, the five-line referee note: claim, method, weakest step, what would break it, one question you'd ask the author. Asking that last line out loud at seminars is the fastest entry into the culture.

---

## 8. Author cheat sheet: signature moves

| Author | Reaches for first |
|---|---|
| Witten | simplest nontrivial example; the same point from two or three angles; rigor only where it pays |
| Maldacena | a black-hole thought experiment; consistency pushed until it becomes a conjecture |
| Komargodski | match the anomaly, constrain the phase diagram; RG monotones |
| Shao | the symmetry as a topological operator; minimal lattice model (Ising) first |
| Yonekura | put it on a manifold with boundary; cobordism and index theory as bookkeeping |
| Casini | algebras assigned to regions; entropy inequalities as proofs of QFT theorems |
| Calabrese | exact replica computation in 2d; universal scaling function; lattice check |
| Harlow | operational definitions: what can an observer measure; error correction |
| Stanford | a solvable model (SYK, JT) pushed to an exact answer; chaos as geometry; ensembles |
| Swingle | tensor-network picture; many-body probes (OTOCs) of holographic ideas |
| Hong Liu | EFT reasoning joined to algebras; time and space emerging from subalgebra structure |

---

## 9. Milestones

- End of phase 0: any abstract by the eleven can be placed on the map in one sentence.
- Mid phase 1: seminars in these areas are followable at speaker speed, including the audience's questions.
- End of phase 1: given a fresh Witten or Yonekura abstract, the section structure is predictable before the PDF opens. Try it; it's a real test.
- Phase 2: one replication note exists; one section of group writing has survived the Witten-template rewrite; new papers by the eleven get read the week they appear.

A calibration, so the plan stays honest: research-depth command of all three dialects is a multi-year affair, and nobody on the list has it uniformly either. Eighteen months of this schedule buys real fluency: reading their new papers the week they appear, following any seminar in the area, writing in the register. That is what "speaking the language" means, and it's enough to work at the frontier where these dialects now converge, which is the frontier the group's own program is already on.

---

## Related

- Courses: the three syllabi under `wiki/courses/` (generalized symmetries; algebraic QFT; AdS/CFT) are the institutional arms of tracks A, B, C respectively.
- Projects: [[long-range-bell-decay-project]], [[bell-in-type-iii-project]], [[embezzlement-capacity-project]]
- Questions this program feeds: [[julia-toulouse-higher-form-symmetries]], [[non-invertible-symmetries-mcs]], [[impossible-measurements-qft]], [[embezzlement-cost-relative-entropy]]
- Concepts most exercised: [[entanglement-embezzlement]], [[type-iii-von-neumann-algebras]], [[crossed-product-construction]], [[subregion-subalgebra-duality]], [[ryu-takayanagi-formula]], [[quantum-extremal-surfaces]], [[julia-toulouse-mechanism]]
