---
title: "Sem II Week 8 — Bell-CHSH Between the Two Sides: Exact Model and Continuum Protocol"
type: lecture-notes
course: syllabus
semester: 2
week: 8
block: 2
duration: "master dossier: 4 hours of material; classroom core: 2-hour seminar + 1-hour office/self-study"
prerequisites: Sem II Wks 5–7 (CPW); Sem I Wk 11 (Bell-CHSH in QFT)
target_paper: "Summers–Werner Bell correlations; CPW for the two-sided algebraic setting"
modified: 2026-08-24
---

# Sem II Week 8 — Bell-CHSH Between the Two Sides

> *The TFD has strong correlations across two commuting algebras. That sentence is true, but it does not yet tell us which four observables violate a Bell inequality, by how much, or what the violation says about a bulk bridge. This week keeps those questions separate. We first solve a two-mode TFD exactly. We then turn the free-field calculation into a reproducible covariance-matrix protocol. Finally, we state the operator-algebraic maximality results at their proper level: they are existence theorems under specific AQFT hypotheses, not proofs that every convenient family of smeared fields reaches $2\sqrt2$, and not an if-and-only-if test for a wormhole.*

> **Route through this master dossier.** **Classroom core (two-hour seminar):** §§1–3, then the observable-class distinction that opens §4. **Full derivation or self-study:** the continuum covariance protocol in §4 and Problems 1–7. **Research extension or office hour:** §§5–7, the source-audit exercise, and the project problem. The exact two-mode solution is the board calculation; the Summers–Werner theorem and holographic interpretation remain visibly separate layers.

## 0. Reading and source map

**Primary.**

- Sem I Week 11 for the CHSH operator, Tsirelson's bound, and the course statement of the Summers–Werner results.
- S. J. Summers, “Yet More Ado About Nothing: The Remarkable Relativistic Vacuum State,” arXiv:0802.1854, especially the discussion of Bell correlations and its original references.
- S. J. Summers and R. Werner, “Maximal violation of Bell's inequalities is generic in quantum field theory,” *Commun. Math. Phys.* **110** (1987) 247–259, especially Theorem 2.3, Corollary 3.1, and Theorem 3.2.
- S. J. Summers and R. Werner, “Bell's inequalities and quantum field theory. II. Bell's inequalities are maximally violated in the vacuum,” *J. Math. Phys.* **28** (1987) 2448–2456, for the vacuum result that preceded the generic-vector theorem.
- CPW, arXiv:2209.10454, for the two-sided large-$N$ algebraic setting. CPW does not supply the explicit CHSH calculation developed here.

**Optional constructive reading.**

- A paper chosen by the instructor that gives explicit smeared-field Bell operators. Record its exact observable class, spacetime dimension, mass, state, and achieved numerical value before importing any conclusion into this dossier.
- B. S. Tsirelson, *Lett. Math. Phys.* **4** (1980) 93, for the quantum bound.

**Source boundary.** The two-qubit calculation in §3 is an exact course model. The Gaussian formula in §4 is an exact free-field identity once its covariance data are specified. The geometric and holographic discussion in §§6–7 is interpretation, not a theorem extracted from either calculation.

## 1. What is the Bell question here?

Let $\mathcal A_R$ and $\mathcal A_L$ be commuting von Neumann algebras represented on one Hilbert space, and let $\omega$ be the TFD state. Choose self-adjoint contractions

$$
A_1,A_2\in\mathcal A_R,
\qquad
B_1,B_2\in\mathcal A_L,
\qquad
\|A_i\|,\|B_j\|\leq1.
$$

The CHSH operator is

$$
\mathcal C
=A_1(B_1+B_2)+A_2(B_1-B_2).
$$

Because the two algebras commute, the $A$ and $B$ operators describe compatible measurements made on opposite sides. A local hidden-variable model obeys

$$
|\omega(\mathcal C)|\leq2,
$$

whereas quantum mechanics gives the operator bound

$$
\|\mathcal C\|\leq2\sqrt2.
$$

Three claims must not be conflated:

1. **A chosen quartet violates CHSH:** $|\omega(\mathcal C)|>2$.
2. **The state-algebra pair has maximal Bell value:** the supremum over allowed quartets is $2\sqrt2$.
3. **A particular ansatz reaches the supremum:** for example, four cosine-Weyl contractions do so.

The second statement does not imply the third. An existence proof may use projections, partial isometries, or limiting sequences quite different from the ansatz we would like to evaluate numerically.

## 2. What the algebraic theorems do—and do not—say

Summers and Werner established a particularly strong result for **complementary wedges**, not an unqualified result for any two type-III factors.

> **Complementary-wedge vector-state theorem.** Let $W$ be a wedge and $W'$ its causal complement. For a local Poincaré-covariant net satisfying the spectrum condition and the technical field/net hypotheses stated in Summers–Werner, *Commun. Math. Phys.* **110** (1987) 247, Theorem 3.2, every vector state on the vacuum Hilbert space has maximal Bell value for $\mathcal A(W)$ and $\mathcal A(W')$. In the present unnormalized CHSH convention the supremum is $2\sqrt2$. Corollary 3.1 gives the closely related route from a type-III$_1$ wedge factor plus wedge duality $\mathcal A(W')=\mathcal A(W)'$.

> **Normal-state extension.** Their Theorem 2.3, together with the QFT application in §III of the same paper, extends maximality from vector states to all normal states on $\mathcal B(\mathcal H)$ represented by density matrices when the complementary wedge algebras satisfy the additional injectivity/strong-stability and duality hypotheses. Injectivity is therefore an extra input, not a synonym for type III$_1$.

These hypotheses matter. “Both algebras are type III$_1$” is not, by itself, the theorem. One must specify their complementary-wedge position, the representation/state class, wedge duality or the paper's alternative hypotheses, and—when claiming the all-normal-state version—injectivity. Likewise, maximality does not say that every pair of dichotomic observables is optimal; most choices are not.

This distinction is useful in class. Type III structure explains why finite-dimensional intuition is too restrictive and why the local algebras contain extremely rich operator families. The explicit construction of good measurement settings remains a separate problem.

### Instructor checkpoint

Ask students to classify each sentence below:

- “The Bell supremum is $2\sqrt2$.” — an optimization statement.
- “These four operators give $2.41$.” — a constructive lower bound.
- “These cosine operators approach $2\sqrt2$.” — a convergence claim requiring a proof or reproducible computation.
- “The bulk is connected.” — a holographic interpretation requiring additional input.

The lesson is not merely caution. It tells us exactly what a calculation must deliver.

## 3. Exact mini-calculation: one TFD mode

The cleanest finite-dimensional model keeps a single two-level mode on each side. It will not reproduce a type III algebra, but it gives an exact answer and makes the temperature dependence visible.

### 3.1 State

Let the excited level have energy $\omega$ and set

$$
q=e^{-\beta\omega/2}.
$$

The normalized two-mode TFD is

$$
|\psi_q\rangle
=\frac{|00\rangle+q|11\rangle}{\sqrt{1+q^2}}.
$$

Its one-sided reduced state is thermal:

$$
\rho_R
=\frac{|0\rangle\langle0|+e^{-\beta\omega}|1\rangle\langle1|}
{1+e^{-\beta\omega}}.
$$

Define

$$
C_q:=\frac{2q}{1+q^2}
=\operatorname{sech}\!\left(\frac{\beta\omega}{2}\right).
$$

For this pure two-qubit state, $C_q$ is also the concurrence. Direct multiplication gives

$$
\langle\sigma_z\otimes\sigma_z\rangle=1,
\qquad
\langle\sigma_x\otimes\sigma_x\rangle=C_q,
\qquad
\langle\sigma_y\otimes\sigma_y\rangle=-C_q.
$$

### 3.2 Optimal observables and exact CHSH value

Choose

$$
A_1=\sigma_z,
\qquad
A_2=\sigma_x,
$$

and

$$
B_1=\frac{\sigma_z+C_q\sigma_x}{\sqrt{1+C_q^2}},
\qquad
B_2=\frac{\sigma_z-C_q\sigma_x}{\sqrt{1+C_q^2}}.
$$

Each is a dichotomic observable. Since

$$
B_1+B_2=\frac{2\sigma_z}{\sqrt{1+C_q^2}},
\qquad
B_1-B_2=\frac{2C_q\sigma_x}{\sqrt{1+C_q^2}},
$$

we obtain

$$
\begin{aligned}
\langle\mathcal C\rangle_q
&=\frac{2}{\sqrt{1+C_q^2}}
\left(
\langle\sigma_z\otimes\sigma_z\rangle
+C_q\langle\sigma_x\otimes\sigma_x\rangle
\right)\\
&=2\sqrt{1+C_q^2}\\
&=2\sqrt{1+\operatorname{sech}^2(\beta\omega/2)}.
\end{aligned}
$$

This is the maximal CHSH value for the state. It is larger than $2$ for every finite $\beta\omega$, tends to $2\sqrt2$ when $\beta\omega\to0$, and tends to $2$ when $\beta\omega\to\infty$.

### 3.3 What this model teaches

The approach to Tsirelson's value here is a **high-temperature or low-frequency limit**, not a statement about boosting a fixed wave packet toward a bifurcation surface. A Lorentz boost translates Rindler time while preserving the Rindler radial coordinate; it does not by itself move a fixed support to the horizon. Any continuum localization limit must therefore be defined independently and checked on the test functions and their covariances.

The model also prevents an overly quick slogan. An entangled TFD mode violates CHSH, but maximal violation appears only in the maximally entangled limit. A field theory has infinitely many modes and a type III local algebra, so the algebraic supremum can behave differently from any fixed mode or fixed observable family.

## 4. Continuum free field: an honest computation protocol

We now use the right and left Rindler wedge algebras of a free scalar in the Minkowski vacuum. The vacuum is cyclic and separating for each one-sided wedge algebra, and the two wedge algebras commute. This is the controlled analog of the two-sided setup.

### 4.1 Weyl and cosine operators

For a real test function $f$, let

$$
W(f)=e^{i\phi(f)}.
$$

Choose $f_i$ supported in $W_R$ and $g_j$ supported in $W_L$. The bounded self-adjoint contractions

$$
A_i=\cos\!\big(\alpha_i\phi(f_i)\big),
\qquad
B_j=\cos\!\big(\beta_j\phi(g_j)\big)
$$

belong to their respective local algebras. They are not generally dichotomic: their spectra need not be only $\{+1,-1\}$. They are nevertheless legitimate contractions for a CHSH test. If a project requires sharp binary measurements, students must replace them with spectral sign operators or projections and redo the expectation-value calculation.

### 4.2 Gaussian input

Fix conventions by writing the vacuum Weyl functional as

$$
\omega_0(W(h))=\exp\!\left[-\frac12\mu(h,h)\right],
$$

and the Weyl relation as

$$
W(h)W(k)=e^{-i\sigma(h,k)/2}W(h+k).
$$

Here $\mu$ is the real symmetric covariance and $\sigma$ is the symplectic form. Opposite-wedge supports are spacelike separated, so

$$
\sigma(f_i,g_j)=0.
$$

Expanding each cosine into two Weyl operators gives the checkable identity

$$
E_{ij}:=\omega_0(A_iB_j)
=\exp\!\left[-\frac12\left(
\alpha_i^2\mu(f_i,f_i)+\beta_j^2\mu(g_j,g_j)
\right)\right]
\cosh\!\left(\alpha_i\beta_j\mu(f_i,g_j)\right).
$$

Therefore

$$
\omega_0(\mathcal C)=E_{11}+E_{12}+E_{21}-E_{22}.
$$

No numerical value follows until the four test functions, four strengths, field mass, spacetime dimension, and covariance convention have been supplied.

### 4.3 Reproducibility checklist

A continuum mini-project is complete only if it records:

1. the field, dimension, mass, state, and two-point-function normalization;
2. explicit smooth compactly supported $f_1,f_2,g_1,g_2$;
3. a verified support plot or analytic support bounds;
4. the covariance and symplectic data needed for all same-side and cross-side products;
5. quadrature domain, tolerances, and convergence under refinement;
6. the four $E_{ij}$ and the resulting CHSH value;
7. an optimization domain fixed before quoting a maximum;
8. a distinction between a lower bound obtained by the ansatz and the algebraic supremum.

This protocol is less spectacular than an invented asymptotic formula, but it is scientifically useful: another student can reproduce it, change the smearing functions, and see exactly where a violation comes from.

### 4.4 Why a common boost is not an optimization parameter

The Minkowski vacuum is invariant under boosts. If all four smearings are transformed by the same boost, their covariance matrix is unchanged; consequently the CHSH expectation is unchanged. In Rindler coordinates a boost shifts the time coordinate and leaves the radial coordinate fixed. Thus a statement such as “boost all bumps and they approach the bifurcation surface” is incorrect.

One may instead study a genuine **localization family** whose supports shrink toward a horizon, or use modularly transformed operators on only one side. Either procedure changes the relative covariance data and may be interesting, but it must be stated precisely. No universal monotonic approach to $2\sqrt2$ follows from modular flow alone.

## 5. From constructive lower bounds to algebraic maximality

The exact mode calculation and the Gaussian protocol play different roles.

| Question | Exact two-mode model | Continuum cosine protocol | AQFT theorem |
|---|---|---|---|
| Are the observables explicit? | Yes | Yes, after smearings are given | Not necessarily |
| Is the value checkable? | Analytically | Analytically/numerically | The supremum is proved |
| Does it model type III locality? | No | Yes, through local field algebras | Yes, under theorem hypotheses |
| Does it prove this ansatz is optimal? | Yes for the chosen state | No | No |
| Does it establish a bulk bridge? | No | No | No |

This table is the didactic center of the week. “Existence,” “construction,” and “geometric interpretation” are three layers of one research problem, not interchangeable phrasings of the same result.

### Connection to the group's work

If the instructor assigns a De Fabritiis–Sorella–Roditi–Guimarães paper, use it as a source-specific case study. Students should extract rather than guess:

- whether the local observables are Weyl operators, cosine contractions, projections, or pseudospin operators;
- whether the result is analytic, numerical, or an optimized lower bound;
- whether the geometry is wedges, double cones, or another region pair;
- the reported value and its numerical uncertainty;
- whether a limit to $2\sqrt2$ is proved or merely suggested by data.

This preserves the genuine connection to the research program without assigning a number or asymptotic law to an unspecified paper.

## 6. What does Bell violation say about ER=EPR?

The eternal black hole and its TFD boundary state provide the motivating example: a semiclassical bridge and strong cross-boundary correlations occur together. Bell violation is a sharp way to demonstrate that those correlations do not admit a local hidden-variable description for the chosen measurements.

It is not, however, a bridge detector.

- **Not sufficient:** opposite wedges in the Minkowski vacuum possess strong and sometimes maximal Bell correlations, but the QFT calculation alone does not assert an Einstein–Rosen bridge.
- **Not necessary in a fixed experiment:** a poor quartet of observables may give no violation even when the state has a known connected holographic dual.
- **Not a reconstruction theorem:** the same CHSH number discards almost all information in the state and the net of algebras.

Thus Bell correlation can be one useful datum in an ER=EPR discussion, but bulk connectivity additionally requires holographic dynamics, a semiclassical code subspace, and reconstruction of the geometry. The disciplined conclusion is “compatible with and diagnostically interesting for the TFD bridge,” not “Bell saturation if and only if wormhole.”

## 7. Research directions with honest deliverables

### 7.1 Holographic Bell operators

Choose two commuting boundary subalgebras and a state with a controlled bulk dual. Establish the exact algebraic hypotheses before invoking a maximality theorem. Then construct a finite family of boundary observables and report a reproducible lower bound. A comparison with entanglement wedge connectivity belongs in the interpretation section, not in the theorem statement.

### 7.2 Dressed versus undressed algebras

The crossed product changes the algebra type and introduces a trace, but Tsirelson's operator bound remains $2\sqrt2$. A tractable question is whether a chosen undressed quartet embeds into the dressed algebra with the same state correlations, and which clock correlations appear when the observables themselves carry dressing.

### 7.3 Embezzlement

Van Dam and Hayden introduced finite-dimensional approximate embezzling families. Van Luijk, Stottmeister, Werner, and Wilming, arXiv:2401.07299, characterize universal embezzlement for von Neumann algebras and show a strong type-III$_1$ result in an operational, arbitrarily-accurate sense. A project should ask what survives in the type-II crossed product. It should not call the protocol exact at finite error or attribute the result to “van Daele.”

### 7.4 Finite-regulator perturbation project

For students heading toward AAJ, replace the vague request “compute the free-field cocycle to second order” by a finite-regulator task: choose a density matrix, a bounded perturbation, and four Bell observables; compute the perturbed expectations from nested commutators; and compare with exact matrix exponentiation. Week 11 explains how this course reconstruction differs from AAJ's own unitary perturbation calculation.

## 8. What to take away

- The CHSH question is an optimization over four contractions in two commuting algebras.
- Type-III AQFT maximality theorems are powerful existence statements whose geometry, state, and algebraic hypotheses must be quoted.
- A theorem about the supremum does not prove that a cosine-Weyl ansatz is optimal.
- The two-mode TFD has the exact maximum

$$
2\sqrt{1+\operatorname{sech}^2(\beta\omega/2)}.
$$

- For opposite-wedge Gaussian fields, a cosine-pair expectation is determined by a finite covariance matrix; this gives an honest computation protocol.
- A common Lorentz boost does not move Rindler support toward the horizon and cannot change a boost-invariant vacuum covariance matrix.
- Bell violation is neither a sufficient bridge criterion nor guaranteed for every measurement choice in a bridge state.

## 9. Problem set

### Core problems

**1. Derive the mode correlations.** Starting from $|\psi_q\rangle$, compute the three Pauli correlators in §3.1 and verify the normalization of $\rho_R$.

**2. Derive the optimal value.** Insert the four observables of §3.2 into $\mathcal C$. Show directly that each $B_j$ squares to the identity and that the expectation is $2\sqrt{1+C_q^2}$. Evaluate the limits $\beta\omega\to0$ and $\beta\omega\to\infty$.

**3. Locate the violation.** For which finite values of $\beta\omega$ is the exact mode value strictly larger than $2$? Explain why the limiting zero-temperature product state does not violate CHSH.

**4. Derive the cosine formula.** Expand $\cos(\alpha\phi(f))\cos(\beta\phi(g))$ into four Weyl products. Using $\sigma(f,g)=0$, derive the formula for $E_{ij}$ in §4.2.

**5. Covariance-matrix audit.** The instructor supplies a positive covariance dataset and the four self-covariances. Check positivity/uncertainty compatibility, compute all $E_{ij}$, and state whether the chosen contractions violate CHSH. Do not optimize beyond the supplied domain.

### Starred problems

**6*. Common-boost invariance.** Prove from Poincaré covariance and vacuum invariance that applying the same boost to all smearings leaves every $E_{ij}$ unchanged. Explain in Rindler coordinates why the boost does not change the radial coordinate.

**7*. Sharp observables.** Replace one cosine contraction by $\operatorname{sgn}[\cos(\alpha\phi(f))]$ using bounded functional calculus. In a quasifree state, the joint law of finitely many commuting smeared fields is still Gaussian, so these expectations are determined in principle by the relevant covariance (and, for noncommuting ordered products, by the symplectic data and ordering prescription). What is lost is the simple four-Weyl/cosh formula of §4.2. Derive a defensible protocol using a multivariate Gaussian integral or a convergent Fourier approximation to the periodic sign function, and state how the discontinuity set and numerical convergence are controlled.

**8*. Source audit.** Choose one constructive QFT Bell paper. Prepare a one-page ledger with columns “theorem,” “observable family,” “state,” “region geometry,” “analytic/numerical,” and “reported bound.” Reproduce one table entry or figure point.

**9*. Theorem hypotheses.** Return to the precise Summers–Werner theorem assigned in Sem I Week 11. List every hypothesis and mark which are established, assumed, or unknown for the large-$N$ boundary algebras used by CPW.

### Project problem

**10. Bell data and geometry.** Write a five-page memo explaining why a CHSH value is too coarse to reconstruct a bulk geometry. Propose one additional algebraic or modular datum that could be compared across states, and label the proposal as heuristic unless you can supply a theorem.

**Wiki connections.** [[bell-chsh-in-holographic-setting|Bell–CHSH in holographic settings]] (open question)

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 2. Last revised 2026-08-24.*

*End of Sem II Block 2.*
