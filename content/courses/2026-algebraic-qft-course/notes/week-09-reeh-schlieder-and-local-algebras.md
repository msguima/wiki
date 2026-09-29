---
title: "Week 9 — Local Algebras and the Reeh–Schlieder Theorem"
type: lecture-notes
course: syllabus
semester: 1
week: 9
block: C
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Week 8 (free-field algebras, Weyl operators)
modified: 2026-08-24
---

# Week 9 — Local Algebras and the Reeh–Schlieder Theorem

> *Last week we built the free-field local algebra. This week we discover that the vacuum is much more than a ground state. It is cyclic for every nonempty open region in a Wightman QFT and, when the causal complement contains a nonempty open region, it is also separating. That is exactly the input Tomita–Takesaki needs. Reeh–Schlieder is therefore the theorem that licenses vacuum modular theory for local algebras.*

### How to use this chapter

- **In class:** state the net and spectrum hypotheses before the theorem, walk through the analytic-continuation mechanism as a proof sketch, and derive separatingness from locality only after identifying a nonempty causal complement.
- **For self-study:** write a three-column list headed theorem, operational consequence, and tempting overstatement. Use it to separate dense state preparation from unitary preparation, signaling, and type classification.
- **Instructor checkpoint:** require students to explain why Reeh–Schlieder does not rule out type I$_\infty$, why an ambient rank-one density operator is not an intrinsic local density matrix, and why a finite torus is not automatically a finite-mode theory.

## 0. Reading

**Primary:**
- Streater & Wightman, *PCT, Spin and Statistics, and All That*, §4.2 (Reeh–Schlieder, classical exposition).
- Haag, *Local Quantum Physics*, ch. II §5.3 and ch. III §1 (the algebraic statement and consequences).

**Secondary:**
- Reed & Simon, *Methods of Modern Mathematical Physics*, Vol. II, §IX.8 (edge of the wedge theorem in detail).
- Borchers, "On revolutionizing quantum field theory with Tomita's modular theory" *J. Math. Phys.* 41 (2000) 3604, §2 (modular consequences of Reeh–Schlieder).

**Optional research reading:**
- Witten, "Notes on some entanglement properties of QFT," arXiv:1803.04993, §2 (modern algebraic introduction).
- Summers, "Yet more ado about nothing: the remarkable relativistic vacuum state," arXiv:0802.1854, §3 (philosophical/structural review of vacuum properties).
- Redhead, "More ado about nothing," *Foundations of Physics* 25 (1995) 123 (philosophy of vacuum nonlocality).

## 1. The Haag–Kastler axioms

Last week we built a specific net of local algebras for the free scalar. We now state the axioms that *any* AQFT model should satisfy. These are the **Haag–Kastler axioms**, an abstraction of Wightman's framework into algebraic form.

**Definition 1.1 (Local net of vN algebras).** A **local net** of von Neumann algebras on Minkowski space $\mathbb{R}^{1,d}$ consists of:
- a Hilbert space $\mathcal{H}$;
- a von Neumann algebra $\mathcal{A}(\mathcal{O}) \subset \mathcal{B}(\mathcal{H})$ for each open region $\mathcal{O} \subset \mathbb{R}^{1,d}$;
- a strongly continuous unitary representation $U(\Lambda)$ of the proper orthochronous Poincaré group $\mathcal{P}_+^\uparrow$ on $\mathcal{H}$;
- a Poincaré-invariant unit vector $\Omega \in \mathcal{H}$, the **vacuum**.

These data satisfy:

1. **Isotony:** $\mathcal{O}_1 \subset \mathcal{O}_2 \implies \mathcal{A}(\mathcal{O}_1) \subset \mathcal{A}(\mathcal{O}_2)$.

2. **Locality (Einstein causality):** if $\mathcal{O}_1$ and $\mathcal{O}_2$ are spacelike separated (every $x \in \mathcal{O}_1$ is spacelike-related to every $y \in \mathcal{O}_2$), then $[\mathcal{A}(\mathcal{O}_1), \mathcal{A}(\mathcal{O}_2)] = 0$.

3. **Covariance:** $U(\Lambda)\,\mathcal{A}(\mathcal{O})\,U(\Lambda)^* = \mathcal{A}(\Lambda \mathcal{O})$ for all $\Lambda \in \mathcal{P}_+^\uparrow$.

4. **Vacuum:** $U(\Lambda)\Omega = \Omega$ for all $\Lambda \in \mathcal{P}_+^\uparrow$.

5. **Spectral condition (energy positivity):** the generator $P^0$ of time translations is positive ($P^0 \ge 0$); the joint spectrum of $(P^0, P^1, \ldots, P^d)$ lies in the forward light cone $\overline{V_+} = \{p: p^0 \ge |\vec p\,|\}$.

The free scalar of Week 8 satisfies all five — items 1, 2, 3 were established explicitly there; items 4, 5 are properties of the Fock representation built on the standard Minkowski vacuum.

### 1.1 The sixth optional axiom: Haag duality

6. **Haag duality (when it holds):** $\mathcal{A}(\mathcal{O})' = \mathcal{A}(\mathcal{O}')$, where $\mathcal{O}'$ is the **causal complement** of $\mathcal{O}$ — the (open) set of points spacelike-separated from every point of $\mathcal{O}$.

Haag duality strengthens locality (which says only $\mathcal{A}(\mathcal{O}') \subset \mathcal{A}(\mathcal{O})'$) to an equality. It holds in the free scalar for **wedges** (proved by Bisognano–Wichmann, Week 10) and for **double cones** in many cases; it can fail for non-simply-connected regions, where one has the strictly weaker *essential duality*.

We will use Haag duality only when needed and will flag it as a separate hypothesis. For wedge algebras, the Bisognano–Wichmann theorem implies wedge duality when its field-theoretic hypotheses hold.

### 1.2 What the axioms encode

The five mandatory Haag–Kastler axioms encode three distinct physical principles:

- **Locality (axioms 1–3):** observables in spacelike-separated regions commute. This is Einstein causality at the operator-algebra level. No measurement here can disturb a measurement there if they are not in causal contact.
- **Symmetry (axioms 3–4):** the Poincaré group acts as automorphisms of the net, leaving the vacuum invariant. This is relativistic invariance.
- **Stability (axiom 5):** energy is bounded below; the spectrum lies in the forward light cone. This is the "no negative-energy ghost" condition.

These are the core physical requirements, but later structural theorems require additional hypotheses. Reeh–Schlieder uses the Wightman/global-cyclicity and analyticity framework; Bisognano–Wichmann uses its own field-theoretic assumptions; the type III$_1$ and hyperfiniteness results of Week 12 require scaling and phase-space input. We will state those additions rather than hide them inside the phrase “reasonable QFT.”

> **Physical picture.** In AQFT, the theory is the **net**, not the isomorphism class of one local algebra. For models satisfying the phase-space and scaling hypotheses stated carefully in Week 12, local factors are isomorphic to the unique hyperfinite type III$_1$ factor. The physical information then lies in how these copies are nested, how spacelike complements are related, which state is chosen, and how spacetime symmetries act. This is not a theorem about every informal “reasonable QFT,” and it should not be applied to unconstructed four-dimensional models such as QCD as if their Haag–Kastler nets were already under mathematical control.

## 2. The Reeh–Schlieder theorem

**Theorem 2.1 (Reeh–Schlieder 1961). [Stated only — refs: Reeh & Schlieder, *Nuovo Cimento* 22 (1961) 1051; Streater & Wightman §4.2.]** *Let a Wightman QFT satisfy Poincaré covariance, the spectrum condition, locality, and the Wightman vacuum-cyclicity axiom for the global field algebra. Then, for every nonempty open region $\mathcal{O}\subset\mathbb{R}^{1,d}$, the vacuum vector $\Omega$ is cyclic for the local algebra:*
$$
\overline{\mathcal{A}(\mathcal{O})\,\Omega} = \mathcal{H}.
$$

**Reading the statement.** Every vector can be approximated in Hilbert-space norm by vectors $a\Omega$ with $a\in\mathcal{A}(\mathcal{O})$. This is a density statement. It does not say that every target can be prepared deterministically by a local unitary, with bounded cost, or with a success probability controlled uniformly in the target.

This is genuinely counter-intuitive. A naive picture of the vacuum as a "ground state with no excitations" would forbid cyclicity for a tiny region: one would expect that you need to act in many regions to build a generic state (e.g., a state with a particle far from $\mathcal{O}$). The theorem says that naive picture is wrong. The vacuum is a **globally entangled state**, and local operations near a point can produce excitations of arbitrarily long-range character. The price is that the operators required for distant excitations are not "physically intuitive" — they are weighted polynomials in the field that operate locally on the vacuum but produce non-local effects via the vacuum's entanglement structure.

### 2.1 Sketch of the proof

**Proof status. [Mechanism only.]** The following roadmap isolates the analytic idea. A rigorous proof treats Wightman distributions, ordered difference variables, common invariant domains, and boundary values in several complex variables. The displayed point-field expressions are mnemonic notation for smeared distributions.

The roadmap is written with point-field products as shorthand. The full proof is formulated for smeared Wightman distributions and all polynomial degrees.

Suppose, for contradiction, $\psi \in \mathcal{H}$ satisfies
$$
\langle\psi, \phi(x_1)\cdots\phi(x_n)\,\Omega\rangle = 0 \quad \text{for all } x_1, \ldots, x_n \in \mathcal{O},\; n \ge 0.
$$
We will derive $\psi = 0$.

**Step 1: holomorphy in the forward tube.** Consider the function
$$
F(x_1, \ldots, x_n) := \langle\psi, \phi(x_1)\cdots\phi(x_n)\,\Omega\rangle.
$$
Here the mostly-plus convention needs one explicit sign guardrail. Define
$$
Q(a):=a^0H-\vec a\cdot\vec P=-a\cdot P,
\qquad
U(a)=e^{iQ(a)}.
$$
Then $\phi(a)=U(a)\phi(0)U(a)^*$ and $U(a)\Omega=\Omega$. If $z=a+iy$ with $y$ in the forward cone $V_+=\{y:y^0>|\vec y\,|\}$, the spectral condition gives
$$
Q(y)=y^0H-\vec y\cdot\vec P\ge0,
\qquad
U(z)=e^{iQ(a)}e^{-Q(y)},
$$
so the imaginary translation is damping. In an ordered product one first rewrites the fields in translation-difference variables. The same estimate applies to every intermediate difference whenever $\operatorname{Im}z_{j+1}-\operatorname{Im}z_j\in V_+$.

Hence $F$ extends to a function on the **product forward tube**
$$
\mathcal{T}_n^+ := \{(z_1, \ldots, z_n) \in \mathbb{C}^{(1+d)n} : \mathrm{Im}\,z_{j+1} - \mathrm{Im}\,z_j \in V_+ \text{ for } j = 1, \ldots, n-1\,\},
$$
**holomorphic** in each $z_j$ separately on this domain.

**Step 2: vanishing on a real open set.** By assumption, $F = 0$ for all real $x_j \in \mathcal{O}$. The boundary of $\mathcal{T}_n^+$ in $\mathbb{R}^{(1+d)n}$ includes the real open set $\mathcal{O}^n$.

**Step 3: edge-of-the-wedge.** The **edge-of-the-wedge theorem** (Streater–Wightman §2.5; Reed–Simon Vol. II §IX.8) says: a function holomorphic in a tube domain (such as $\mathcal{T}_n^+$) with a real boundary, vanishing on a real open subset of that boundary, vanishes identically on the tube.

**Step 4: extension by analytic continuation.** Once $F \equiv 0$ on the product tube, the Wightman uniqueness/edge-of-the-wedge machinery extends the vanishing to all real configurations at which the boundary distribution is evaluated. This is not an elementary pointwise Schwarz-reflection argument; the rigorous statement is about distributional boundary values in several complex variables.

**Step 5: conclude.** $F \equiv 0$ for all $x_1, \ldots, x_n \in \mathbb{R}^{1,d}$ means $\psi \perp \phi(x_1)\cdots\phi(x_n)\Omega$ for all $n$ and all $x_j$. The polynomials in field operators acting on $\Omega$ span a dense subspace of $\mathcal{H}$ (by the Wightman reconstruction theorem: the vacuum is cyclic for the full field algebra). Hence $\psi = 0$, contradicting our hypothesis. $\square$

### 2.2 What the proof uses

The argument relies on three structural facts:

1. **The spectral condition gives forward-tube holomorphy.** Energy positivity $P^0 \ge 0$ is what allows analytic continuation to imaginary times in the forward direction. Without it, the argument fails.

   *Physical aside:* this is the same mechanism that licenses Wick rotation. "Energy bounded below" means $e^{-\tau H}$ is a legitimate damping operator for $\tau > 0$, so correlators extend analytically to imaginary time — stability of the vacuum *is* Euclidean analyticity. Reeh–Schlieder is thus a cousin of the familiar fact that Euclidean correlators are real-analytic away from coincident points: an analytic function pinned to zero on an open set has no freedom left anywhere. The vacuum's rigidity under local probing is the operator-theoretic face of the analyticity that field theorists use daily.

2. **Edge-of-the-wedge converts "vanishes on real open set" into "vanishes everywhere on the tube."** This is a powerful theorem of several complex variables; the 1D analog is the trivial fact that a holomorphic function on the upper half-plane vanishing on a real interval is identically zero.

3. **Polynomials in field operators generate a dense subspace from $\Omega$.** This is the Wightman cyclicity of the vacuum for the *global* field algebra. The Reeh–Schlieder theorem then upgrades it from global cyclicity to local cyclicity.

None of these uses interaction structure or specific field content. What is used is the **standard Wightman package**, including global vacuum cyclicity and the analytic consequences of the spectrum condition; the five elementary net axioms listed in §1 are not, by themselves, a substitute for that package.

## 3. Separating from cyclic via locality

**Theorem 3.1 (Reeh–Schlieder corollary). [Proved, given Theorem 2.1.]** *Under the hypotheses of Theorem 2.1, let $\mathcal{O}$ have a causal complement containing a nonempty open region. Then the vacuum $\Omega$ is separating for $\mathcal{A}(\mathcal{O})$.*

**Proof.** Take $a \in \mathcal{A}(\mathcal{O})$ with $a\,\Omega = 0$. We show $a = 0$.

For any $b \in \mathcal{A}(\mathcal{O}')$, locality (axiom 2) gives $[a, b] = 0$, so
$$
a\,b\,\Omega = b\,a\,\Omega = 0.
$$
Hence $a$ annihilates the subspace $\mathcal{A}(\mathcal{O}')\,\Omega$.

By Reeh–Schlieder (Theorem 2.1) applied to the open set $\mathcal{O}'$ (which is non-empty open by hypothesis), $\overline{\mathcal{A}(\mathcal{O}')\,\Omega} = \mathcal{H}$. So $a$ annihilates a dense subspace of $\mathcal{H}$.

Since $a$ is bounded and annihilates a dense subspace, $a = 0$. $\square$

### 3.1 The corollary chain

Combining Theorems 2.1 and 3.1: **every "good" local algebra** — i.e., $\mathcal{A}(\mathcal{O})$ for an open region $\mathcal{O}$ with non-empty open complement $\mathcal{O}'$ — **has the vacuum as a cyclic-separating vector**.

By Week 5, separatingness makes the vacuum vector state faithful on $\mathcal{A}(\mathcal{O})$, while cyclicity supplies the dense Tomita domain. This is exactly the input Tomita–Takesaki needs.

**Corollary 3.2. [Proved.]** *Every local algebra $\mathcal{A}(\mathcal{O})$ in a Wightman QFT (with $\mathcal{O}$ open and $\mathcal{O}'$ non-empty open) carries a canonical modular operator $\Delta_{\mathcal{O}}$, modular conjugation $J_{\mathcal{O}}$, and modular flow $\sigma_t^{\mathcal{O}}(a) = \Delta_{\mathcal{O}}^{-it}\,a\,\Delta_{\mathcal{O}}^{it}$ (our upper-strip convention, Week 5) with respect to the vacuum.*

**This is the licensing theorem of the entire course.** Without Reeh–Schlieder, we would not know that the local algebras of QFT have modular structure with respect to the physically natural state. Tomita–Takesaki gives modular structure for *cyclic-separating* vectors; Reeh–Schlieder is what guarantees the vacuum is cyclic-separating for local algebras.

## 4. Implications and surprises

The Reeh–Schlieder theorem is counter-intuitive, but its exact content is narrower than several slogans built around it. Three distinctions keep the physics honest.

### 4.1 Dense local orbits are not deterministic preparation protocols

Reeh–Schlieder says that for every target vector $\psi$ and every $\varepsilon>0$, some $a\in\mathcal{A}(\mathcal{O})$ satisfies $\|a\Omega-\psi\|<\varepsilon$. It does not say that $a$ is unitary, that $\|a\|$ remains controlled along an approximation sequence, or that $a$ is itself a deterministic quantum channel.

After rescaling, any bounded $a$ can be made a contraction $k=a/\|a\|$ and used as one Kraus operator of a local measurement. Conditional on that outcome, the post-measurement vector is proportional to $a\Omega$; its success probability is $\|a\Omega\|^2/\|a\|^2$. This is a perfectly legitimate **selective** operation, not an unphysical one. What fails is deterministic remote preparation. The nonselective operation—including all outcomes—cannot be used for superluminal signaling because it acts locally and commutes with spacelike-separated observables.

Reeh–Schlieder itself gives no universal rate for the success probability. Quantitative energy, distance, and localization costs require additional estimates. The theorem supplies density; it does not supply an efficient protocol.

### 4.2 Reeh–Schlieder does not by itself determine the factor type

It is tempting to argue that a cyclic-separating vacuum rules out type I. That implication is false. A type I$_\infty$ factor can have cyclic-separating vectors in a standard or suitably amplified representation. In the bipartite model
$$
\mathcal{B}(\mathcal{K})\otimes1\subset
\mathcal{B}(\mathcal{K}\otimes\mathcal{K}),
$$
a vector with all Schmidt coefficients nonzero is cyclic and separating. Its reduced density matrix may have finite **or infinite** von Neumann entropy. Thus neither Reeh–Schlieder nor entropy divergence alone excludes type I$_\infty$.

The UV area-law divergence remains valuable physical evidence that a sharp continuum cut does not behave like an ordinary tensor factorization. The rigorous type-III conclusions, however, use further input: scaling limits or modular-spectrum results for the type, and nuclearity/split or related phase-space conditions for hyperfiniteness. Week 12 keeps those logical steps separate.

### 4.3 Strong vacuum correlations are not one universal notion of “maximal”

“Maximally entangled” has a precise finite-dimensional meaning and should not be used as a synonym for cyclic and separating. The latter is a full-support condition. Bell maximality, universal embezzlement, and entropy properties are separate theorems with separate hypotheses:

- Summers–Werner maximal Bell correlations apply to complementary wedges under specified net hypotheses; stronger all-normal-state statements require injectivity.
- Type III$_1$ universal embezzlement is an **arbitrarily accurate approximate** statement, not exact finite-step conversion.
- Araki relative entropy exists for normal states on any von Neumann algebra, not only type III$_1$.

Reeh–Schlieder is an essential ingredient in this landscape because it supplies a standard vacuum vector. It is not, by itself, the proof of all three phenomena.

### 4.4 Why there is no paradox

Locality constrains **operations and observable statistics**, whereas Reeh–Schlieder describes the norm closure of a set of **unnormalized vectors**. Postselection can change conditional distant correlations, just as in ordinary entanglement theory, while the averaged local channel leaves spacelike-separated expectation values unchanged. Energy positivity remains intact. Once the levels—vector density, selective operation, and nonselective signaling protocol—are distinguished, there is no conflict with causality.

## 5. Worked analytic illustration: 2D free field in the wedge

We illustrate the analytic mechanism for the right Rindler wedge $W_R = \{x: x^1 > |x^0|\}$. To avoid the massless zero mode, use the derivative field or restrict to the zero-integral test-function algebra described in Week 8. This section is a **sketch**, not an independent proof replacing Theorem 2.1.

### 5.1 A dense set of states

Polynomials in $\phi(f)$ for $f$ supported in $W_R$, applied to $|0\rangle$, give the dense subspace
$$
\mathcal{D}_{W_R} := \mathrm{span}\!\left\{\phi(f_1)\cdots\phi(f_n)\,|0\rangle : f_j \in \mathcal{S}(W_R)_{\mathbb{R}}, n \in \mathbb{N}_0\right\}.
$$
The Reeh–Schlieder theorem gives $\overline{\mathcal{D}_{W_R}}=\mathcal{H}$ after the usual domain and infrared qualifications. The next two subsections explain why one-sided support leads to the required analyticity.

### 5.2 Fourier modes

In 2D massless, decompose $\phi$ into right-moving and left-moving parts:
$$
\phi(x^0, x^1) = \phi_R(x^-) + \phi_L(x^+), \qquad x^\pm = x^0 \pm x^1.
$$
A real test function $f$ supported in $W_R = \{x^1 > |x^0|\}$ has light-cone Fourier modes
$$
\tilde f_R(k^-) = \int dx^-\,f_R(x^-)\,e^{ik^- x^-}, \qquad \tilde f_L(k^+) = \int dx^+\,f_L(x^+)\,e^{ik^+ x^+},
$$
where $f_{R/L}$ are the right/left-moving parts of $f$. For $f$ supported in $W_R$ (with $x^- < 0, x^+ > 0$ throughout the support), the Fourier transforms $\tilde f_{R/L}$ are *boundary values* of functions holomorphic in upper-half-plane-like domains (one-sided support → one-sided analyticity).

### 5.3 Density via an annihilator test

The Paley–Wiener/Hardy-space principle needed here is a **uniqueness** statement: a positive-frequency boundary value is constrained by holomorphy, so if it vanishes distributionally on a nonempty interval, it vanishes everywhere. It does not say that an arbitrary momentum wavefunction is exactly the Fourier transform of one compact wedge-supported test function.

Here is the correct density test in the one-particle sector. Let $h$ be orthogonal to every vector $\phi(f)\Omega$ with $\operatorname{supp}f\subset W_R$. Then the positive-frequency distribution
$$
F_h(x):=\langle h,\phi(x)\Omega\rangle
$$
obeys $F_h(f)=0$ for every such $f$, hence vanishes on the open wedge. The spectral condition makes $F_h$ the boundary value of a holomorphic function in the corresponding tube. Uniqueness then gives $F_h=0$ globally, so $h=0$. The orthogonal complement of the wedge-created one-particle vectors is therefore trivial, which is exactly their density. Repeating the annihilator argument for all polynomial degrees gives the Fock-space statement. This is the mode-space shadow of the Reeh–Schlieder proof, not an independent constructive recipe with a controlled approximation cost.

### 5.4 Separating via causal complement

$W_R' = W_L$. By Reeh–Schlieder cyclicity applied to $W_L$ (same argument), $\Omega$ is cyclic for $\mathcal{A}(W_L)$. By Theorem 3.1, $\Omega$ is separating for $\mathcal{A}(W_R)$.

### 5.5 What the theorem plus the illustration establishes

- **By Reeh–Schlieder:** $\Omega$ is cyclic for $\mathcal{A}(W_R)$.
- **By locality plus cyclicity of the left wedge:** $\Omega$ is separating for $\mathcal{A}(W_R)$.
- **Therefore:** Tomita–Takesaki applies and supplies $(\Delta_{W_R},J_{W_R},\sigma_t^{W_R})$.

The Paley–Wiener discussion makes the density mechanism visible, but the rigorous justification remains the cited theorem. Week 10 identifies the resulting modular objects geometrically.

## 6. Variations and limits

### 6.1 Other regions

Reeh–Schlieder works for **any** non-empty open region — not just wedges. So $\Omega$ is also cyclic for $\mathcal{A}(\mathcal{O})$ for:
- **Bounded double cones** $\mathcal{O}_r := \{x: |x^0| + |\vec x| < r\}$ (the diamond of radius $r$ around the origin).
- **Open spacetime neighborhoods of a time-zero ball.** A ball at exactly $x^0=0$ is not an open spacetime region and does not by itself label a Haag–Kastler algebra. Under a time-slice/additivity axiom, its causal development is the relevant double cone.
- **Arbitrary unions of open regions**.

The cyclicity is robust. The modular data certainly vary with the region. Under the common hypotheses of Week 12, however, many nontrivial local factors have the same abstract hyperfinite type III$_1$ isomorphism class; what varies is their position in the net.

### 6.2 Beyond Wightman QFT

Reeh–Schlieder uses the Wightman analyticity machinery (tempered fields, forward-tube extension). For more general AQFT setups — say, Haag–Kastler nets without an explicit field operator — the analog holds under suitable axioms (existence of a vacuum, locality, covariance, spectral condition), but the proof is more abstract.

For QFT on **curved spacetimes**, an analog holds (Strohmaier–Verch) under microlocal analyticity conditions, but the structure depends on which "vacuum" one picks (in curved spacetime there is no preferred vacuum, generally).

### 6.3 A nonrelativistic counterexample

There is no blanket Reeh–Schlieder theorem for nonrelativistic theories. In the standard free Schrödinger-field representation, the one-particle decomposition $L^2(\mathbb{R}^d)=L^2(\mathcal{O})\oplus L^2(\mathcal{O}^c)$ induces a Fock tensor product, and the vacuum is a product vector. The algebra generated by the modes in $\mathcal{O}$ cannot create particles in the complementary Fock factor, so its vacuum orbit is not dense.

This example lacks relativistic locality and the forward-light-cone spectrum/analyticity used in Theorem 2.1. It shows that those hypotheses do real work. It does not establish the logically stronger—and false—claim that removing the spectrum condition forces every conceivable net to lose cyclicity.

This contrast is one of the deep features distinguishing relativistic from non-relativistic QFT.

## 7. What to take away

- **Stated only:** Reeh–Schlieder — the vacuum is cyclic for every non-empty local algebra $\mathcal{A}(\mathcal{O})$ in a Wightman QFT.
- **Proved (from cyclic + locality):** the vacuum is also separating, hence cyclic-separating, for every $\mathcal{A}(\mathcal{O})$ with non-empty open complement.
- **Consequence (Corollary 3.2):** every such local algebra has canonical Tomita–Takesaki data $(\Delta, J, \sigma_t)$ with respect to the vacuum.
- **Proof boundary:** Reeh–Schlieder alone does not determine whether the local factor is type I, II, or III; Week 12 adds the required scaling and phase-space input.
- **Entanglement boundary:** cyclic-separating is not synonymous with finite-dimensional maximal entanglement. Bell and embezzlement statements require their own hypotheses.
- **Operational meaning:** a contraction in $\mathcal{A}(\mathcal{O})$ can be a legitimate postselected Kraus operator, but vector-density does not imply deterministic remote preparation or signaling.

## 8. Looking ahead

Week 10 is the central computational lecture of Block C: the **Bisognano–Wichmann theorem**, which identifies the vacuum wedge modular operator with the exponentiated Lorentz boost generator. It is the principal model-independent geometric modular-flow theorem used in this course. Other explicit modular flows exist when additional symmetry is present, notably vacuum balls in conformal field theory. The combination Reeh–Schlieder, Bisognano–Wichmann, and the scoped type III$_1$ results of Week 12 is the structural input for what follows.

## 9. Problem set

**Core problems.**

**1. What is lost without the relativistic spectral condition?** The absence of the spectrum condition does not logically force every model to violate Reeh–Schlieder; it removes the theorem's analytic mechanism. Construct a counterexample using the nonrelativistic bosonic Fock factorization
$$
\mathcal{F}(L^2(\mathbb{R}^d))
\cong
\mathcal{F}(L^2(\mathcal{O}))\otimes
\mathcal{F}(L^2(\mathcal{O}^c)).
$$
Take the local algebra $\mathcal{B}(\mathcal{F}(L^2(\mathcal{O})))\otimes1$ and the product Fock vacuum. Exhibit a vector orthogonal to its local orbit and identify which relativistic assumptions are absent.

**2. Cyclicity for a bounded region in two dimensions.** Use the massless derivative field (or impose the zero-integral smearing condition) and let $\mathcal{O}$ be a nonempty open double cone with closure inside $W_R$. Sketch the Paley–Wiener/forward-tube argument for $\overline{\mathcal{A}(\mathcal{O})\Omega}=\mathcal{H}$. Identify explicitly where positive energy, global vacuum cyclicity, and openness of $\mathcal{O}$ enter.

**3. Separating for double cones.** Let $\mathcal{O}_r = \{x: |x^0| + |\vec x| < r\}$ be a double cone of radius $r$ centered at the origin. Show that $\mathcal{O}_r' \neq \emptyset$, and conclude (via Theorem 3.1) that the vacuum is separating for $\mathcal{A}(\mathcal{O}_r)$.

**4. Haag duality for wedges (theorem-guided).** For the free two-dimensional derivative field, first prove from locality that
$$
\mathcal{A}(W_L)\subset\mathcal{A}(W_R)'.
$$
Then state the Bisognano–Wichmann modular-conjugation result needed for the reverse inclusion and show how Tomita's identity $J\mathcal{A}(W_R)J=\mathcal{A}(W_R)'$ yields wedge duality. Do not treat “maximal causal structure” as a proof.

**5. A product-state spin-chain counterexample.** Let
$$
\mathfrak A=\overline{\bigcup_{\Lambda\Subset\mathbb Z}
\bigotimes_{n\in\Lambda}M_2(\mathbb C)}^{\|\cdot\|}
$$
be the quasi-local algebra of a spin-$1/2$ chain, and let $\omega_0$ be the pure product state with reference vector $|0\rangle$ at every site. In its GNS representation, take a finite interval $\Lambda$ and identify
$$
\mathcal H\cong\mathcal H_\Lambda\otimes\mathcal H_{\Lambda^c},
\qquad
\Omega=\Omega_\Lambda\otimes\Omega_{\Lambda^c},
\qquad
\pi(\mathfrak A(\Lambda))''=\mathcal B(\mathcal H_\Lambda)\otimes1.
$$
Determine the closure of $\pi(\mathfrak A(\Lambda))''\Omega$. Then choose a site $j\notin\Lambda$, flip that spin to $|1\rangle_j$, and prove that the resulting vector is orthogonal to the whole local orbit. Explain why this product-state lattice example does not contradict Reeh–Schlieder: it has neither relativistic covariance with a forward-cone spectrum nor the tube analyticity of the Wightman vacuum.

**6. Regulated CFT entropy—and why it is not a type proof.** For a two-dimensional CFT vacuum on the line, use the replica result for an interval of length $\ell$,
$$
S(\ell)=\frac{c}{3}\log\frac{\ell}{\epsilon}+\text{constant},
$$
with $c=1$ for the free boson after its infrared sector is specified. Explain why a half-line requires an infrared prescription and may carry a different coefficient depending on boundary conditions. Finally, explain why divergence as $\epsilon\to0$ is physical evidence for the absence of a sharp type-I tensor factorization but does not, by itself, prove the local algebra is type III.

**Starred problems.**

**7\*. Edge of the wedge.** State the edge-of-the-wedge theorem precisely (Reed–Simon Vol. II §IX.8). Sketch the proof in the one-dimensional case: a function holomorphic in the upper half-plane and vanishing on a real interval is identically zero (Schwarz reflection). Where does the proof generalize cleanly to higher-dimensional tubes, and where is it delicate?

**8\*. Cyclic-separating vectors in a type-I model.** Let $\mathcal{M}=M_n(\mathbb{C})$ act as $\mathcal{M}\otimes1$ on $\mathbb{C}^n\otimes\mathbb{C}^n$. Show that $\Omega$ is cyclic and separating iff its Schmidt rank is $n$. Compute the entropy in terms of the Schmidt coefficients and show that it can be arbitrarily close to $0$ while all coefficients remain nonzero, whereas it equals $\log n$ only for equal coefficients. This exercise is the finite-dimensional reason not to identify cyclic-separating with maximally entangled.

**9\*. Why the vacuum has no Tomita operator for $\mathcal{B}(\mathcal{H})$ in its defining representation.** Assume $\dim\mathcal{H}>1$ and let $\Omega\in\mathcal{H}$ be a unit vector.
(a) Find a nonzero projection $p\in\mathcal{B}(\mathcal{H})$ with $p\Omega=0$.
(b) Conclude that $\Omega$ is not separating, so the vacuum Tomita construction for $(\mathcal{B}(\mathcal{H}),\Omega)$ is unavailable; it is wrong to assign it $\Delta=1$.
(c) Compare with the standard Hilbert–Schmidt representation of $M_n$, where the tracial vector is cyclic-separating and has $\Delta=1$. Explain why neither fact conflicts with Bisognano–Wichmann for a local wedge factor.

**10\*. A bounded local excitation.** Let $\psi=W(f)\Omega$ with real $f$ supported in $\mathcal{O}$, and let $\mathcal{N}=\mathcal{A}(\mathcal{O}')$. By locality, $W(f)\in\mathcal{N}'$.
(a) Prove that if $\Omega$ is cyclic for $\mathcal{N}$, then $\psi$ is cyclic for $\mathcal{N}$.
(b) Prove the analogous separating statement.
(c) Explain why this argument uses the bounded unitary $W(f)$ and does not establish a blanket theorem for arbitrary unbounded vectors $\phi(f)\Omega$ or arbitrary excited states.

**11\*. Compact spatial volume versus a finite-mode cutoff.** A continuum free field on $\mathbb{R}\times T^d$ still has positive energy and infinitely many ultraviolet modes; compact spatial volume alone neither removes the relevant analyticity nor makes sharp local algebras type I. Compare:

- the continuum theory on the torus, where Reeh–Schlieder-type arguments can persist for nonempty spacetime regions; and
- a UV and finite-mode truncation, whose global oscillator algebra is type I but whose band-limited fields no longer define a strictly local net.

Identify exactly which premise changes in the second model. Do not infer failure of Reeh–Schlieder merely from compact spatial volume or a spectral gap.

## Self-study answer checkpoints

These checkpoints cover the core problems. Starred, project, and explicitly research-level problems remain source-led; they should be completed with the references and hypotheses named in the problem.

1. The local orbit is contained in
   $$
   \mathcal F(L^2(\mathcal O))\otimes\mathbb C\Omega_{\mathcal O^c}.
   $$
   A one-particle vector $\Omega_{\mathcal O}\otimes a^*(h)\Omega_{\mathcal O^c}$ with $0\ne h\in L^2(\mathcal O^c)$ is orthogonal to it. The relativistic forward-cone spectrum, locality structure, and resulting tube analyticity are absent.
2. If $\Psi\perp\mathcal A(\mathcal O)\Omega$, the relevant vacuum matrix elements vanish when all insertions lie in the open region $\mathcal O$. Positive energy supplies forward-tube holomorphy, and openness permits edge-of-the-wedge continuation; the continued functions vanish for arbitrary translates. Global vacuum cyclicity then forces $\Psi=0$, so $\overline{\mathcal A(\mathcal O)\Omega}=\mathcal H$.
3. At $t=0$, every point $(0,\vec y)$ with $|\vec y|>r$ has an open neighborhood spacelike to $\mathcal O_r$, so $\mathcal O_r'$ contains a nonempty open set. Cyclicity for its algebra and locality then give: $A\Omega=0$ with $A\in\mathcal A(\mathcal O_r)$ implies $A=0$.
4. Locality gives $\mathcal A(W_L)\subseteq\mathcal A(W_R)'$. Bisognano--Wichmann identifies $J\mathcal A(W_R)J$ geometrically with $\mathcal A(W_L)$, whereas Tomita's theorem identifies the same algebra with $\mathcal A(W_R)'$. These two identities supply the reverse inclusion and hence wedge duality.
5. For the product-state chain,
   $$
   \overline{\pi(\mathfrak A(\Lambda))''\Omega}
   =\mathcal H_\Lambda\otimes\mathbb C\Omega_{\Lambda^c}.
   $$
   If $j\notin\Lambda$, the vector with spin $j$ in $|1\rangle_j$ and every other complementary spin in $|0\rangle$ is orthogonal to this subspace. Thus the product vacuum is not locally cyclic; the missing relativistic analytic structure is the essential distinction.
6. For $c=1$ the regulated interval result is
   $$
   S(\ell)=\frac13\log\frac{\ell}{\epsilon}+\text{constant}.
   $$
   A half-line needs an infrared scale or boundary prescription, so its coefficient and additive term cannot be inferred from the displayed interval formula alone. In either case, cutoff divergence is evidence about short-distance correlations, not an operator-algebraic proof of type III.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block C. Last revised 2026-08-24.*
