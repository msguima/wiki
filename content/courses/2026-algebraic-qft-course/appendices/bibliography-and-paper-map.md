---
title: "Appendix G — Bibliography and Paper Map"
type: appendix
course: syllabus
modified: 2026-06-11
---

# Bibliography and Paper Map

This appendix maps the main references to their role in the course. It is a *reading guide*, not a full bibliography of algebraic QFT.

## G.1 How to Read the References

The course uses three levels of reading:

**Core foundations.** Needed to understand the lecture notes. Mostly operator algebras, modular theory, and AQFT textbooks. Students should return to these throughout Semester I.

**Bridge papers.** Explain why type III, modular theory, and crossed products matter for modern QFT and gravity. Students should read selected sections rather than every technical proof.

**Research papers.** Semester II primary material. Students must identify, for each paper: the algebraic theorem used, the model calculation done, the holographic input assumed, and the open problem raised.

## G.2 Primary Paper Map (Semester II spine)

| Reference | Course use | Required sections | Main technical input | Proof status |
|---|---|---|---|---|
| Witten, *Notes on Some Entanglement Properties of QFT*, arXiv:1803.04993 | Semester I bridge | §§2–3 | algebraic entanglement framework; modular flow in QFT; explicit modular Hamiltonian for the type-I model. Our **modular-flow convention** is taken from §3 of this paper. | pedagogical source |
| Witten, *Gravity and the Crossed Product*, arXiv:2112.12828 | Semester II Block 1 (target) | §§2–4 | type III$_1$ → type II$_\infty$ via crossed product; ADM Hamiltonian as the dressing flow; generalized entropy as dressed-algebra entropy | target paper |
| Chandrasekaran–Penington–Witten (CPW), *Large $N$ algebras and generalized entropy*, arXiv:2209.10454 | Semester II Block 2 (target) | Large-$N$ algebra setup; crossed-product section; entropy section | two-sided eternal-BH version of Witten 2022; TFD vacuum; $H_R - H_L$ dressing | target paper |
| Chandrasekaran–Longo–Penington–Witten (CLPW), *An Algebra of Observables for de Sitter Space*, arXiv:2206.10780 | Semester II Block 5 aside (dS comparison) | Static-patch algebra + entropy sections | de Sitter type II$_1$ comparison case (compact horizon, observer Hamiltonian bounded below) | comparison paper |
| Hong Liu, *Lectures on entanglement, von Neumann algebras, and emergence of spacetime*, arXiv:2510.07017 | Semester II Block 3 (connective tissue) | §§3, 5, 7 | type III at large $N$; modular flow ↔ bulk Killing flow; algebraic ER=EPR | review / bridge |
| Ahmad & Jefferson (AAJ), *Algebraic perturbation theory: traversable wormholes and generalized entropy beyond subleading order*, arXiv:2501.01487 | Semester II Block 4 (target) | §§2–5 | Connes-cocycle perturbation of crossed products; GJW-deformed entropy; 20 corrections at quadratic order | research target |
| Gao–Jafferis–Wall, *Traversable Wormholes via a Double Trace Deformation*, JHEP 12 (2017) 151, arXiv:1608.05687 | Background for AAJ and MSY | Setup + double-trace deformation | physical GJW deformation; traversability mechanism in the bulk | imported gravity input |
| Maldacena–Stanford–Yang, *Diving into traversable wormholes*, arXiv:1704.05333 | Semester II Block 5 (bulk-side complement) | Conceptual and bulk-dynamics parts | bulk dynamics; ANEC violation; Shapiro time advance; teleportation interpretation | imported gravity input |
| Maldacena, *Eternal black holes in anti-de Sitter*, JHEP 04 (2003) 021, arXiv:hep-th/0106112 | Background for CPW (Week 15) | §§1–3 | eternal AdS-Schwarzschild ↔ TFD identification | foundational holographic input |

## G.3 Operator-Algebra Foundations

### Bratteli & Robinson, *Operator Algebras and Quantum Statistical Mechanics*, Vols. I & II

**Course use.** C\*-algebras, von Neumann algebras, KMS states, modular theory, equilibrium states, crossed products (Vol. I §2.7), KMS-equilibrium link (Vol. II §5.3).

**Reading strategy.** Main technical reference for Weeks 1–7. Do not try to read linearly on first pass; look up definitions and theorem statements as needed.

### Takesaki, *Theory of Operator Algebras*, Vols. I–III

**Course use.** Von Neumann algebra structure (Vol. I), Tomita–Takesaki theory (Vol. II Ch. VIII), crossed products and continuous cores (Vol. II Ch. X; Vol. III Ch. XII), weights and dual actions (Vol. III §VIII.3).

**Reading strategy.** Instructor reference for analytic details. Students use selected statements, not full proofs.

### Haag, *Local Quantum Physics*

**Course use.** Local nets (ch. II §5), Reeh–Schlieder context (ch. II §5.3), Bisognano–Wichmann (ch. V §4), AQFT conceptual discipline, two-sided algebras (ch. V §1).

**Reading strategy.** Use for the physical meaning of local algebras and type III behavior. Pair with the lecture notes rather than reading alone.

## G.4 Type III and Local QFT Algebras

### Connes, *Classification of injective factors*, *Ann. of Math.* 104 (1976) 73

**Course use.** Classification of hyperfinite (injective) factors except III$_1$.

**Reading strategy.** Instructor reference. Students need only the **statement** (Week 12 Theorem 2.5).

### Haagerup, *Connes' bicentralizer problem and uniqueness of the injective factor of type III$_1$*, *Acta Math.* 158 (1987) 95

**Course use.** Completes the classification by proving uniqueness of the hyperfinite III$_1$ factor.

**Reading strategy.** Statement only.

### Connes, *Une classification des facteurs de type III*, *Ann. Sci. ENS* 6 (1973) 133

**Course use.** Connes' S-invariant; the type III$_\lambda$ subclasses.

**Reading strategy.** §§1–2 (statements).

### The QFT-type-III$_1$ universality citation chain (Week 12)

| Paper | Role |
|---|---|
| Driessler, *Comm. Math. Phys.* 44 (1975) 133 and follow-ups | Modular-spectrum criteria forcing local algebras to be type III |
| Fredenhagen, *Comm. Math. Phys.* 97 (1985) 79 | Type III$_1$ under asymptotic-scale-invariance / modular-spectrum hypotheses |
| Doplicher & Longo, *Invent. Math.* 75 (1984) 493 | The split property |
| Buchholz & Wichmann, *Comm. Math. Phys.* 106 (1986) 321 | Nuclearity condition |
| **Buchholz, D'Antoni, Fredenhagen, *Comm. Math. Phys.* 111 (1987) 123** | **Universal type III$_1$ structure under nuclearity + split property** |
| Halvorson, *Algebraic quantum field theory*, arXiv:math-ph/0602036 | Readable survey of the citation chain |

**Common error to avoid:** Do **not** attribute the type III$_1$ universality theorem to Haag–Hugenholtz–Winnink (1967). HHW is about KMS/equilibrium states, not local-algebra classification.

## G.5 Free-Field QFT Foundations

### Streater & Wightman, *PCT, Spin and Statistics, and All That*

**Course use.** Wightman axioms (ch. 3), Reeh–Schlieder (§4.2), edge-of-the-wedge theorem (§2.5), reconstruction theorem.

**Reading strategy.** Compact and rigorous. Read alongside Week 8–9 lectures.

### Reed & Simon, *Methods of Modern Mathematical Physics*, Vol. II

**Course use.** Free scalar field rigorously (§X.7), edge-of-the-wedge (§IX.8), spectral theory.

**Reading strategy.** Reference; not for linear reading.

### Bisognano & Wichmann, *J. Math. Phys.* 16 (1975) 985; *J. Math. Phys.* 17 (1976) 303

**Course use.** The Bisognano–Wichmann theorem (Week 10): $\Delta_{W_R} = e^{-2\pi K}$ where $K$ is the boost generator.

**Reading strategy.** Statement and structural argument; technical proof skipped in this course.

### Borchers, *On revolutionizing quantum field theory with Tomita's modular theory*, *J. Math. Phys.* 41 (2000) 3604

**Course use.** Modernized exposition of Bisognano–Wichmann and its consequences.

**Reading strategy.** Useful synthesis; recommended for instructors.

## G.6 Bell–CHSH in QFT

### Summers & Werner, *J. Math. Phys.* 28 (1987) 2440; *Comm. Math. Phys.* 110 (1987) 247; *Lett. Math. Phys.* 33 (1995) 321

**Course use.** Tsirelson saturation of CHSH between spacelike-separated wedges (Week 11).

**Reading strategy.** §§1–3 of each paper. Take statements as input; structural argument explained in Week 11.

### Group's recent papers (De Fabritiis, Sorella, Guimarães, Roditi et al.)

**Course use.** Explicit Weyl-cosine observable construction for Bell–CHSH in 2D and 4D free scalar, Proca, gauge theories.

**Reading strategy.** Selected 2–3 papers; instructor selects. Read against Week 11 §4 (the explicit construction) and §6 (research-program connection).

## G.7 Crossed Product and Dressed Entropy

### Connes & Takesaki, *The flow of weights on factors of type III*, *Tôhoku Math. J.* 29 (1977) 473

**Course use.** Connes–Takesaki duality (Week 13 Theorem 4.1): type III$_1$ + modular flow → type II$_\infty$ via crossed product; trace exists and is unique up to scaling.

**Reading strategy.** Statement only; the proof requires Takesaki Vol. III machinery.

### Takesaki, Vol. III, Ch. VIII

**Course use.** Continuous cores; dual weights; the trace scaling formula.

**Reading strategy.** Reference; statements only.

## G.8 Required vs. Optional Reading by Week

**Semester I:**

| Week | Required | Optional |
|---|---|---|
| 1 | B–R Vol. I §§2.1–2.3 | Murphy ch. 1–3 |
| 2 | B–R Vol. I §2.4 | Takesaki Vol. I ch. V |
| 3 | B–R Vol. I §2.6 | Murray–vN 1936; Takesaki Vol. I ch. V |
| 4 | B–R Vol. II §5.3 (KMS) | Witten 1803.04993 §3 |
| 5 | B–R Vol. I §2.5; Takesaki Vol. II ch. VIII | Witten 1803.04993 §3 |
| 6 | B–R Vol. II §5.3 | Connes–Rovelli 1994 |
| 7 | B–R Vol. I §2.5 (relative modular); Ohya–Petz ch. 5 | Araki 1976 |
| 8 | Streater–Wightman ch. 3; Haag ch. II §5 | Reed–Simon Vol. II §X.7 |
| 9 | Streater–Wightman §4.2; Haag ch. II §5.3 | Witten 1803.04993 §2 |
| 10 | Bisognano–Wichmann 1975, 1976; Haag ch. V §4 | Borchers 2000 §3 |
| 11 | Summers–Werner 1987a,b | Group papers (selected) |
| 12 | Buchholz–D'Antoni–Fredenhagen 1987 | Halvorson 2006 |
| 13 | Takesaki Vol. II ch. X | Connes & Takesaki 1977; Liu §5 |
| 14 | Witten 2112.12828 §§3–4 | CPW 2209.10454 §3 |
| 15 | Maldacena 2003 §§1–3; CPW 2209.10454 §§2–3 | Liu §§5, 7 |

**Semester II:** see syllabus.md and individual block skeletons; primary papers are the four target papers (Witten 2022, CPW, Liu lectures, AAJ) plus Block 5 bulk-side complement (MSY, with GJW background).

## G.9 What to Extract from Each Sem II Target Paper

| Paper | What students must extract |
|---|---|
| Witten 2022 | (i) algebra at large $N$, (ii) why type III$_1$, (iii) ADM Hamiltonian as dressing flow, (iv) trace formula on crossed product, (v) generalized entropy formula. Identify what is algebraic theorem vs. holographic input. |
| CPW 2022 | (i) two-sided eternal BH dual to TFD, (ii) boundary algebras as type III$_1$, (iii) crossed product with $H_R - H_L$, (iv) dressed entropy = generalized entropy formula. Compare with Witten 2022 (one-sided). |
| Liu lectures | (i) modular flow ↔ bulk Killing flow dictionary, (ii) algebraic ER=EPR proposal, (iii) crossed-product framework in semiclassical limit. |
| AAJ 2025 | (i) Connes-cocycle expansion of crossed-product entropy, (ii) GJW double-trace deformation as a controlled perturbation, (iii) 20 quadratic-order corrections, (iv) which are universal vs. holography-specific. |
| MSY | (i) bulk traversable wormhole construction, (ii) Shapiro time advance, (iii) ANEC violation, (iv) what the bulk sees that the algebra doesn't. |

Each Sem II final-write-up topic asks students to write a critical exposition of one of these papers using the Block A–D toolkit.
