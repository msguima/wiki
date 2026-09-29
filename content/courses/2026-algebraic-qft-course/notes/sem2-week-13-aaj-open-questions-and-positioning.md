---
title: "Sem II Week 13 — Ahmad–Jefferson III: Open Questions and Positioning the Field"
type: lecture-notes
course: syllabus
semester: 2
week: 13
block: 4
duration: "master dossier: 4 hours of material; classroom core: 2-hour seminar + 1-hour office/self-study"
prerequisites: Sem II Wks 11–12 (AAJ framework, source audit, and computation protocol)
target_paper: "Ahmad & Jefferson, arXiv:2501.01487v2 §5"
modified: 2026-08-24
---

# Sem II Week 13 — Ahmad–Jefferson III: Open Questions and Positioning the Field

> *AAJ show that a crossed-product entropy can be followed under a unitary deformation of the full algebra-state system, and they apply the construction to a traversable wormhole through second order in the deformation and through $O(1/N^2)$. The next questions are not all questions AAJ themselves pose. This week therefore uses two labels: “AAJ outlook” for directions stated in §5, and “course-generated direction” for connections we propose after comparing the paper with modular reconstruction and entanglement [[entanglement-embezzlement|embezzlement]]. The distinction makes the literature map useful rather than decorative.*

> **Route through this master dossier.** **Classroom core (two-hour seminar):** §§1–3, ending with the claim-status and literature-positioning ledger. **Full derivation or self-study:** §4's catalyst calculation and the core exercises. **Research extension or office hour:** §5, the starred/project problems, and the proposal-building exercise that separates AAJ's outlook from course-generated directions. The aim is to teach how a research frontier is delimited, not merely how it is advertised.

## 0. Reading and corrected references

**Primary.**

- Ahmad and Jefferson, arXiv:2501.01487v2, §5, “Discussion: the fate of the algebraic approach in quantum gravity.” The paper has five numbered sections; there is no §6.
- Re-read Eqs. (77)–(78): five additional linear terms and fifteen quadratic terms, twenty new terms through quadratic order.

**Secondary.**

- CPW, arXiv:2209.10454, final discussion.
- T. Faulkner, M. Li, and H. Wang, “A modular toolkit for bulk reconstruction,” arXiv:1806.10560. The title and identifier should be kept together; arXiv:2206.00027 is not this paper.

**Embezzlement reading.**

- W. van Dam and P. Hayden, “Universal entanglement transformations without communication,” quant-ph/0201041.
- L. van Luijk, A. Stottmeister, R. F. Werner, and H. Wilming, “Embezzlement of entanglement, quantum fields, and the classification of von Neumann algebras,” arXiv:2401.07299.

## 1. What AAJ established

AAJ study type-III$_1$ algebra-state systems related by a unitary on the full algebra and its commutant. They transport the modular data, reconstruct the corresponding crossed products, and compute how the spectral weighting in the type-II trace changes. In the GJW application they obtain an entropy expansion containing

$$
5\ \text{additional }O(h)\text{ terms}
\quad\text{and}\quad
15\ O(h^2)\text{ terms},
$$

through $O(1/N^2)$. The original GJW first-law term is among the linear structures but is not counted among the five additional terms.

This achievement has a clear boundary:

- the deformation of the full system is unitary;
- the regional change is controlled perturbatively;
- the detailed application is a bilocal double-trace deformation;
- evaluating every term still requires a concrete boundary Hamiltonian/correlator input;
- the interpretation of the total type-II entropy as separate area and matter contributions is regime- and normalization-sensitive.

The reusable tool is not “a Connes-cocycle expansion.” It is the combination of unitary modular covariance, a changed trace weight/Jacobian, and a BCH expansion of the modular charge.

## 2. Outlook questions stated or directly motivated by AAJ §5

### 2.1 Beyond global unitary transformations

AAJ explicitly point to **quantum channels** as a natural extension. A global unitary that mixes an algebra with its commutant need not descend to unitary dynamics on either subsystem. In a type-I regulator the reduced map is a completely positive trace-preserving channel; the algebraic question is how to formulate the corresponding perturbative crossed product and entropy weighting without relying on a tensor-product partial trace.

**Concrete deliverable.** Start with a finite-dimensional Stinespring dilation, derive the subsystem channel, and identify which steps in AAJ's covariance argument fail when the effective map has more than one Kraus operator. Then state what operator-algebraic replacement would be needed.

### 2.2 Regions that move, fluctuate, or change topology

AAJ emphasize a basic tension: AQFT normally assigns an algebra to a fixed region, while in gravity the region and its QES can move under a perturbation. Controlled unitary deformation handles a small change, but a topology-changing or nongeometric regime is not covered.

The difficult question is therefore not simply whether $\mathcal A_R'=\mathcal A_L$ continues to hold. Tomita commutant relations are representation-theoretic and can survive many physically different geometries. One needs a rule that assigns algebras to quantum regions and compares those assignments across states.

**Concrete deliverable.** Define a family $h\mapsto(\mathcal A_h,\omega_h)$ and specify embeddings or channels between different $h$. Without such comparison maps, the phrase “the algebra changed type/topology” has no precise content.

### 2.3 Heavy operators and loss of semiclassical geometry

AAJ note that sufficiently heavy boundary excitations may leave the regime in which a smooth bulk region is available. The crossed product still has an abstract algebraic meaning, but the geometric interpretation of its modular charge may fail.

This gives a useful research boundary: determine which statements require only a standard pair and which require a semiclassical bulk. Semifiniteness of the continuous core belongs to the first column; “this term is a QES area shift” belongs to the second.

### 2.4 Evaporation as mixing of algebra and commutant

AAJ use the traversable wormhole as a controlled analog of information transfer between a black hole and radiation. The global process may be unitary while the effective one-sided description is nonunitary and nonlocal. Extending this picture to a genuinely evaporating one-sided black hole requires a state- and time-dependent algebraic assignment, not merely reusing the eternal-TFD formulas.

## 3. Course-generated directions

The directions below are motivated by AAJ but are not presented as claims from their §5.

### 3.1 Higher-order organization

AAJ give an all-orders formal expression for the perturbed weight and work out the entropy through $h^2$. A natural project is to develop a verified symbolic organization of $h^3$ terms. The goal is not to guess a number from “cocycle × logarithm × clock sectors,” but to expand AAJ's own weight/Jacobian formula, impose BCH order, and test the result against finite matrices.

**Status:** course-generated computational project.

### 3.2 Other interactions

Conserved-current or stress-tensor bilocals bring Ward identities and contact terms absent from a generic scalar double trace. One may ask which of AAJ's displayed structures simplify, which new renormalization data enter, and whether the unitary deformation still has a controlled regional interpretation.

**Status:** course-generated extension; the number of terms cannot be predicted without carrying out the expansion and fixing grouping conventions.

### 3.3 Bulk matching term by term

Terms containing $\beta_1$ or $\beta_2$ invite an area interpretation, while commutator terms can contain matter and quantum-gravity information. A rigorous term-by-term map to a Shapiro time advance or a changed QES requires a bulk calculation in the same state, normalization, and perturbative scheme.

**Status:** partially motivated by AAJ's interpretation, but the proposed detailed matching is open.

### 3.4 Embezzlement and the flow of weights

The strongest proven bridge between embezzlement and von Neumann-algebra type comes from van Luijk–Stottmeister–Werner–Wilming, not from AAJ. They define an operational worst-case error. A state is embezzling when the infimum error vanishes: arbitrary targets can be produced with arbitrarily small disturbance/error. In this sense type-III$_1$ factors are **universal embezzlers**, and every normal state is embezzling.

“Error infimum zero” must not be rewritten as “one finite protocol has literally zero error.” It means that for every tolerance $\epsilon>0$ there is an admissible protocol with error below $\epsilon$.

The paper relates embezzling states to invariant probability measures on the flow of weights. That suggests a genuine question for the course: how does passing from a type-III$_1$ algebra to its type-II$_\infty$ crossed product change the relevant operational invariants? This is much sharper than saying that the same Connes cocycle “implements both” AAJ perturbation and embezzlement. AAJ do not compute a Connes-cocycle protocol, and the embezzlement theorem is organized by the flow of weights.

**Status:** course-generated bridge to the group's research program.

## 4. Finite-dimensional embezzlement: what can be checked

### 4.1 The van Dam–Hayden family

The standard catalyst has Schmidt coefficients

$$
|\mu_n\rangle
=\frac1{\sqrt{H_n}}
\sum_{j=1}^n\frac1{\sqrt j}|j\rangle_A|j\rangle_B,
\qquad
H_n=\sum_{j=1}^n\frac1j.
$$

Its Schmidt probabilities $p_j=1/(jH_n)$ are approximately scale invariant over a long range. Van Dam and Hayden prove that for any fixed finite target state, local unitaries can produce the target while returning the catalyst with fidelity tending to one as $n\to\infty$; the error decreases only logarithmically in the catalyst size.

The useful hand calculation is not an alleged exact fidelity formula. It is the edge-mass estimate. Rescaling the index by a fixed target Schmidt rank $m$ changes $1/j$ approximately by the compensating factor $m$ away from the first and last few indices. The unmatched edge weight is bounded by a fixed harmonic sum divided by $H_n$:

$$
\text{edge weight}
\lesssim\frac{H_m}{H_n}
\xrightarrow[n\to\infty]{}0.
$$

This explains why a harmonic spectrum works. The precise fidelity/error bound should be cited to van Dam–Hayden rather than reconstructed from an informal pairing of Schmidt coefficients.

### 4.2 Why a flat catalyst fails

Let

$$
|\nu_n\rangle=\frac1{\sqrt n}\sum_{j=1}^n|jj\rangle.
$$

Its Schmidt rank is $n$. Adding a product ancilla does not change that rank, while the desired state $|\nu_n\rangle\otimes|\Phi^+\rangle$ has Schmidt rank $2n$ with uniform coefficients. Local unitaries preserve the Schmidt spectrum. Even after embedding in a larger space, the largest possible squared overlap of a rank-$n$ state with that rank-$2n$ uniform target is at most

$$
\left[
\sum_{j=1}^{n}
\left(\frac1{\sqrt n}\frac1{\sqrt{2n}}\right)
\right]^2
=\left(\frac1{\sqrt2}\right)^2
=\frac12.
$$

after optimal alignment of the nonzero Schmidt directions. Increasing $n$ does not improve the bound. Large rank alone is therefore insufficient; the slowly varying, scale-free tail is essential.

### 4.3 What type III$_1$ changes

The operator-algebraic theorem should be stated operationally:

> For a type-III$_1$ factor, every normal state is an embezzling state in the sense that the optimal worst-case error is zero.

The theorem is not proved by calling the modular spectrum a literal infinite Schmidt spectrum. That analogy is suggestive but can mislead because a type-III factor admits no underlying tensor-product density matrix of the kind used above. The proof uses the flow of weights and von Neumann-algebraic invariants.

## 5. A positioning matrix for final projects

| Direction | Exact starting point | Missing ingredient | Defensible deliverable |
|---|---|---|---|
| AAJ $h^3$ | v2 all-orders weight; BCH | controlled symbolic bookkeeping | verified finite-matrix expansion |
| Quantum-channel extension | AAJ §5 suggestion | crossed-product analog of reduced channel | finite Stinespring model + formal gap |
| Moving QES/algebra | unitary covariance | comparison maps between region algebras | precise family of inclusions/channels |
| Bulk term matching | Eqs. (77)–(78) | same-scheme gravity calculation | one term matched with assumptions |
| Holographic Bell | AQFT existence theorems | explicit boundary observables and theorem hypotheses | reproducible lower bound, no bridge iff |
| Crossed-product [[entanglement-embezzlement\|embezzlement]] | arXiv:2401.07299 invariants | type-II operational analysis | theorem-led literature memo or toy model |

This table forces a project to name both its controlled input and its missing step. That is what “positioning” should do.

## 6. Student presentations

Each student gives a ten-minute talk with four slides:

1. **Question.** One sentence, narrow enough to answer.
2. **Controlled input.** The theorem, equation, or finite model actually available.
3. **Proposed calculation.** A deliverable that can be checked.
4. **Scope ledger.** Exact/proved, numerical, heuristic, and open claims in separate rows.

Recommended topic forms:

- finite-regulator BCH/entropy perturbation following AAJ;
- explicit Bell lower bound for a specified observable family;
- operational embezzlement under passage to a crossed product;
- critical, equation-by-equation exposition of CPW, AAJ, or CLPW.

“Free-field cocycle perturbation reproducing AAJ” is no longer offered without qualification. A good version is “finite-regulator comparison between an Araki cocycle and AAJ's unitary BCH deformation.”

## 7. What to take away

- AAJ v2 ends with §5, not §6.
- AAJ's method is unitary crossed-product perturbation, not a Connes-cocycle expansion.
- Their new-term count is five linear plus fifteen quadratic.
- AAJ's stated outlook includes quantum channels and the problem of algebras attached to moving, fluctuating, or topology-changing regions.
- Higher-order diagrams, other bilocals, detailed bulk matching, and the embezzlement connection are useful **course-generated** directions unless a more specific source is supplied.
- Type-III$_1$ universal embezzlement is an arbitrarily-accurate operational theorem. It does not mean a single finite protocol has exactly zero error.
- The correct embezzlement source is van Luijk–Stottmeister–Werner–Wilming, arXiv:2401.07299; the finite catalyst is due to van Dam–Hayden, quant-ph/0201041.

## 8. Problem set

### Core problems

**1. Source/outlook split.** Make two lists from this week: statements directly present in AAJ §5 and course-generated research proposals. Verify each source statement by paragraph or footnote.

**2. Count audit.** Explain in one paragraph why “twenty quadratic corrections” is false. Reproduce the $2+2+2$ linear and $2+6+7$ quadratic groupings from Eqs. (77)–(78).

**3. Flat catalyst.** Prove the $1/2$ squared-overlap bound in §4.2 from Schmidt coefficients. State which assumptions about local operations are used.

**4. Harmonic edge estimate.** For fixed $m$, show $H_m/H_n\to0$. Explain why this is only intuition for the van Dam–Hayden construction and cite the source for the actual protocol error bound.

### Starred problems

**5*. Channel extension.** Work out a two-qubit global unitary whose reduced dynamics has two Kraus operators. Identify the precise step in AAJ's conjugation argument that cannot be copied for the reduced channel.

**6*. Embezzlement definition.** Read the definitions in arXiv:2401.07299. Distinguish “error zero,” “infimum error zero,” and “exact finite operation.” Which one appears in the universal-embezzler theorem?

**7*. Nonperturbative diagnostic.** Propose comparison maps for a family of region algebras $\mathcal A_h$. Explain why the bare relation $J\mathcal A_hJ=\mathcal A_h'$ cannot by itself decide whether a wormhole has changed topology.

### Project problem

**8. Final-topic presentation.** Deliver the four-slide talk of §6 and revise the written project scope in response to questions. Every claimed source result must carry an equation, theorem, or section pointer.

**Wiki connections.** [[bell-inequalities-qft|Bell inequalities in QFT]] (research area) · [[bell-chsh-in-holographic-setting|Bell–CHSH in holographic settings]] (open question)

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 4. Last revised 2026-08-24.*
