---
title: "Appendix G — Bibliography and Paper Map"
type: appendix
course: syllabus
modified: 2026-09-29
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
| Witten, *Gravity and the Crossed Product*, arXiv:2112.12828 | Semester II Block 1 (target) | §§2–3.5 required; §4 optional | strict-$N=\infty$ large-$N$ algebra; central rescaled energy in the extended algebra; perturbative $1/N$ crossed product and type II$_\infty$; trace in §3.4 and entropy in §3.5 | target paper; keep the two regimes separate |
| Chandrasekaran–Penington–Witten (CPW), *Large $N$ algebras and generalized entropy*, arXiv:2209.10454 | Semester II Block 2 (target) | §§2–3 for the microcanonical large-$N$ algebra and entropy; later sections by project | strict microcanonical large-$N$ construction without Witten's perturbative $1/N$ series; right/dressed type-II algebra; entropy of the stated semiclassical states equals the generalized entropy of the bifurcation surface up to a constant | target paper; holographic inputs explicit |
| Chandrasekaran–Longo–Penington–Witten (CLPW), *An Algebra of Observables for de Sitter Space*, arXiv:2206.10780 | Semester II Block 5 aside | §§1.2, 2.3–2.4, 3; §5 for the black-hole contrast | add an observer with $H_{\rm obs}=q\geq0$; in the standard core use $\Pi=\Theta(-H-x)$; on the de Sitter reference vector this gives the finite half-line trace and a type-II$_1$ corner with maximum tracial state | comparison paper; no finite-dimensional/compact-horizon inference |
| Hong Liu, *Lectures on entanglement, von Neumann algebras, and emergence of spacetime*, arXiv:2510.07017 | Semester II Block 3 (connective tissue) | §§II–IV background; §§V–IX selected as routed in Weeks 9–10, especially §§VI–VIII | large-$N$ operator algebras; crossed products; subregion–subalgebra duality; modular/geometric flow in symmetric regimes; conditional algebraic ER=EPR and quantum-gravity models | review / bridge; distinguish theorem from proposal |
| Ahmad & Jefferson (AAJ), *Algebraic perturbation theory: traversable wormholes and generalized entropy beyond subleading order*, arXiv:2501.01487v2 | Semester II Block 4 (target) | §2 review; §3 general perturbation; §4 GJW application; §5 discussion | unitary covariance of modular data; changed spectral weight and Jacobian; BCH nested commutators; five additional linear terms plus fifteen quadratic terms through $O(1/N^2)$ | research target; no §6 and not a Connes-cocycle expansion |
| Gao–Jafferis–Wall, *Traversable Wormholes via a Double Trace Deformation*, JHEP 12 (2017) 151, arXiv:1608.05687 | Background for AAJ and MSY | setup and controlled linear-order calculation | double-trace deformation, negative averaged null energy, and traversability for the suitable sign/profile | imported gravity input; linear order in the deformation |
| Maldacena–Stanford–Yang, *Diving into traversable wormholes*, arXiv:1704.05333 | Semester II Block 5 (bulk-side complement) | Conceptual and bulk-dynamics parts | bulk dynamics; negative horizon-averaged null energy in the coupled setup; Shapiro time advance; teleportation interpretation | imported gravity input; do not infer a violation of an unrelated single-QFT ANEC theorem |
| Maldacena, *Eternal black holes in anti-de Sitter*, JHEP 04 (2003) 021, arXiv:hep-th/0106112 | Background for CPW (Week 15) | §§1–3 | eternal AdS-Schwarzschild ↔ TFD identification | foundational holographic input |
| Faulkner–Li–Wang, *A modular toolkit for bulk reconstruction*, arXiv:1806.10560 | Modular-reconstruction comparison | selected sections by project | modular-flow tools for bulk reconstruction | optional bridge; do not cite as arXiv:2206.00027 |

## G.3 Operator-Algebra Foundations

### Bratteli & Robinson, *Operator Algebras and Quantum Statistical Mechanics*, Vols. I & II

**Course use.** C\*-algebras, von Neumann algebras, KMS states, modular theory, equilibrium states, crossed products (Vol. I §2.7), KMS-equilibrium link (Vol. II §5.3).

**Reading strategy.** Main technical reference for Weeks 1–7. Do not try to read linearly on first pass; look up definitions and theorem statements as needed.

### Takesaki, *Theory of Operator Algebras*, Vols. I–III

**Course use.** Von Neumann algebra structure (Vol. I); the Tomita operator and standard-form theorem (Vol. II Ch. VI); modular automorphism groups (Vol. II Ch. VIII); crossed products and duality (Vol. II Ch. X); and the structure of type-III algebras (Vol. II Ch. XII). These are chapter-level routes verified against the Volume II table of contents; no unverified subsection is assigned here.

**Reading strategy.** Instructor reference for analytic details. Students use selected statements, not full proofs.

### Haag, *Local Quantum Physics*

**Course use.** Local nets (ch. II §5), Reeh–Schlieder context (ch. II §5.3), Bisognano–Wichmann (ch. V §4), AQFT conceptual discipline, two-sided algebras (ch. V §1).

**Reading strategy.** Use for the physical meaning of local algebras and type III behavior. Pair with the lecture notes rather than reading alone.

## G.4 Type III and Local QFT Algebras

### Connes, *Classification of injective factors*, *Ann. of Math.* 104 (1976) 73

**Course use.** Classification of hyperfinite (injective) factors except III$_1$.

**Reading strategy.** Instructor reference. Students need only the **statement** summarized in Week 12 §2.5.

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
| **Buchholz, D'Antoni, Fredenhagen, *Comm. Math. Phys.* 111 (1987) 123** | **Hyperfinite universal form from the relevant phase-space/split/approximation hypotheses; the general statement retains the centre. Type III$_1$ requires separate scaling or modular-spectrum input.** |
| Halvorson, *Algebraic quantum field theory*, arXiv:math-ph/0602036 | Readable survey of the citation chain |

The chain has two logically independent inputs. Nuclearity/split/approximation results supply the hyperfinite universal-form side; scaling or modular-spectrum theorems supply the III$_1$ side. Only after factoriality removes the centre and the classification theorem is invoked may one identify the local factor with the unique hyperfinite III$_1$ factor.

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

### Summers & Werner: *J. Math. Phys.* 28 (1987) 2440–2447 (Part I); *J. Math. Phys.* 28 (1987) 2448–2456 (Part II); *Comm. Math. Phys.* 110 (1987) 247–259; *Lett. Math. Phys.* 33 (1995) 321

**Course use.** Maximal Bell-correlation results for specified spacelike-separated local-algebra configurations (Semester I Week 11 and Semester II Week 8). In *Comm. Math. Phys.* **110**, Theorem 3.2 gives complementary-wedge maximality for every vector state under the paper's net/field hypotheses; Theorem 2.3 and its §III application give the injectivity-based extension to normal density-matrix states.

**Reading strategy.** Read the exact theorem assigned by the instructor and record its state, region geometry, and algebraic hypotheses. Do not infer that every quartet of dichotomic observables—or the cosine-Weyl ansatz in particular—is optimal.

### Group's recent papers (De Fabritiis, Sorella, Guimarães, Roditi et al.)

**Course use.** Source-specific constructive Bell examples from the group's program.

**Reading strategy.** The instructor supplies exact bibliographic entries rather than a floating “recent papers” label. For each paper, extract the observable family, field/dimension, state and regions, analytic versus numerical status, optimization domain, and achieved lower bound. Do not transfer a reported value or asymptotic law between different observable classes.

## G.7 Crossed Product and Dressed Entropy

### Takesaki, *Duality for crossed products and the structure of von Neumann algebras of type III*, *Acta Math.* 131 (1973) 249–310

**Course use.** The source of Week 13 Theorem 4.1 and of the duality theorem in Week 13 §4.2: the modular crossed product is semifinite, its trace is scaled by the dual action, and crossing again by the dual action gives back the original algebra up to stabilization. Witten's crossed-product paper cites it for the III$_1$ → II$_\infty$ statement.

**Reading strategy.** Statement only; the proof is routed through Takesaki Vol. II.

### Connes & Takesaki, *The flow of weights on factors of type III*, *Tôhoku Math. J.* 29 (1977) 473

**Course use.** The flow of weights: the dual action restricted to the centre of the core. Its triviality characterizes type III$_1$, which is why the core of a III$_1$ factor is a factor (Week 13 Theorem 4.1), while III$_\lambda$ and III$_0$ keep a nontrivial centre.

**Reading strategy.** Statement only; the proof uses the crossed-product and type-III machinery routed through Takesaki Vol. II.

### Takesaki, Vol. II, Chs. X and XII

**Course use.** Chapter X supplies crossed products and duality; Chapter XII supplies the type-III structural context. Together they are the instructor route for the continuous core, dual weights, and trace-scaling statements used in Week 13.

**Reading strategy.** Reference; statements only.

## G.8 Entanglement Embezzlement

### van Dam & Hayden, *Universal entanglement transformations without communication*, quant-ph/0201041

**Course use.** Finite-dimensional harmonic catalyst and its arbitrarily accurate large-rank limit.

**Reading strategy.** Use the paper for the protocol and error/fidelity bounds. The harmonic edge estimate in Semester II Week 13 is intuition, not a replacement proof.

### van Luijk, Stottmeister, Werner & Wilming, *Embezzlement of entanglement, quantum fields, and the classification of von Neumann algebras*, arXiv:2401.07299

**Course use.** Operational embezzlement invariants for von Neumann algebras; type-III$_1$ factors as universal embezzlers, with every normal state embezzling.

**Reading strategy.** Quote the definition: the optimal worst-case error has infimum zero, so protocols exist with arbitrarily small error. Do not rewrite this as a single finite protocol with literal zero error, and do not attribute the theorem to “van Daele.”

## G.9 Required vs. Optional Reading by Week

**Semester I:**

| Week | Required | Optional |
|---|---|---|
| 1 | B–R Vol. I §§2.1–2.3 | Murphy ch. 1–3 |
| 2 | B–R Vol. I §2.4 | Takesaki Vol. I ch. V |
| 3 | B–R Vol. I §2.6 | Murray–vN 1936; Takesaki Vol. I ch. V |
| 4 | B–R Vol. II §5.3 (KMS) | Witten 1803.04993 §3 |
| 5 | B–R Vol. I §2.5; Takesaki Vol. II ch. VI | Witten 1803.04993 §3 |
| 6 | B–R Vol. II §5.3 | Takesaki Vol. II ch. VIII; Connes–Rovelli 1994 |
| 7 | Takesaki Vol. II chs. VIII–IX; Ohya–Petz ch. 5 | Araki 1976; B–R Vol. I §2.5 only for the single-state Tomita background |
| 8 | Streater–Wightman ch. 3; Haag ch. II §5 | Reed–Simon Vol. II §X.7 |
| 9 | Streater–Wightman §4.2; Haag ch. II §5.3 | Witten 1803.04993 §2 |
| 10 | Bisognano–Wichmann 1975, 1976; Haag ch. V §4 | Borchers 2000 §3 |
| 11 | Summers–Werner 1987a,b | Group papers (selected) |
| 12 | Buchholz–D'Antoni–Fredenhagen 1987 | Halvorson 2006 |
| 13 | Takesaki Vol. II ch. X | Takesaki 1973; Connes & Takesaki 1977; Liu §V |
| 14 | Witten 2112.12828 §§3.1, 3.4–3.5 | Witten §4 (other conserved charges); CPW entropy comparison |
| 15 | Maldacena 2003 §§1–3; CPW 2209.10454 §§2–3 | Liu §§V, VII–VIII |

**Semester II:** see syllabus.md and individual block skeletons; primary papers are the four target papers (Witten 2022, CPW, Liu lectures, AAJ) plus Block 5 bulk-side complement (MSY, with GJW background).

## G.10 What to Extract from Each Sem II Target Paper

| Paper | What students must extract |
|---|---|
| Witten 2022 | (i) strict-$N=\infty$ type-III$_1$ algebra; (ii) why the rescaled energy is central in the strict extended algebra; (iii) how the relevant order-by-order $1/N$ correction—displayed as $U+\widehat h/(\beta N)$—produces the perturbatively corrected type-II$_\infty$ crossed product, while physical gravitational corrections are organized with $G_N\sim1/N^2$; (iv) trace in §3.4; (v) density matrices and entropy in §3.5; (vi) why §4 concerns other conserved charges. Separate exact finite $N$ (expected type I) from both asymptotic regimes. |
| CPW 2022 | (i) the thermal GNS construction and one-sided standardness; (ii) full two-sided modular charge versus formal one-sided charges; (iii) the strict microcanonical large-$N$ crossed-product/type-II construction, distinct from Witten's perturbative series; (iv) entropy of the relevant right/dressed algebra and its generalized-entropy interpretation for the stated semiclassical states; (v) which steps are algebraic and which are holographic. Do not apply cyclic-separating language to the joint algebra without checking it. |
| Liu lectures | (i) §§VI–VIII large-$N$, subregion, and emergent-geometry claims; (ii) the hypotheses under which modular flow is geometric; (iii) §V crossed products and §IX gravitational models; (iv) the conditional classical/quantum-volatile and $\alpha'$ qualifications of §VIII.3, rather than a generic iff bridge theorem. |
| AAJ 2025 v2 | (i) §2 crossed-product review; (ii) §3 unitary covariance and changed expectation-value weight/Jacobian; (iii) BCH expansion of the modular charge; (iv) §4 GJW application; (v) one recovered GJW linear structure plus five additional linear terms; (vi) fifteen quadratic terms; (vii) §5 outlook, including channels and moving regions. Do not replace this with the course's separate Araki-cocycle reconstruction. |
| MSY | (i) bulk traversable-wormhole construction; (ii) the geodesic time advance in a fixed sign/coordinate convention; (iii) negative horizon-averaged null energy for the specified coupling profile; (iv) what the bulk sees that the algebraic entropy expansion does not. |

Each Sem II final-write-up topic asks students to write a critical exposition of one of these papers using the Block A–D toolkit.
