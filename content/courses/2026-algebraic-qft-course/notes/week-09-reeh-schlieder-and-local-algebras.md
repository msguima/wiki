---
title: "Week 9 — Local Algebras and the Reeh–Schlieder Theorem"
type: lecture-notes
course: syllabus
semester: 1
week: 9
block: C
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Week 8 (free-field algebras, Weyl operators)
modified: 2026-06-11
---

# Week 9 — Local Algebras and the Reeh–Schlieder Theorem

> *Last week we built the free-field local algebra. This week we discover that the vacuum is much more than a "ground state." It is **cyclic** and **separating** for the local algebra of any bounded open region. By Block B, that is exactly the input Tomita–Takesaki needs. Every local algebra in a Wightman QFT comes equipped with a canonical modular operator, modular conjugation, and modular flow — with respect to the **vacuum**. Reeh–Schlieder is the theorem that licenses the rest of the course.*

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

We will use Haag duality only when needed and will flag it as a separate hypothesis. For wedges in Wightman theories, it is automatic via Bisognano–Wichmann.

### 1.2 What the axioms encode

The five mandatory Haag–Kastler axioms encode three distinct physical principles:

- **Locality (axioms 1–3):** observables in spacelike-separated regions commute. This is Einstein causality at the operator-algebra level. No measurement here can disturb a measurement there if they are not in causal contact.
- **Symmetry (axioms 3–4):** the Poincaré group acts as automorphisms of the net, leaving the vacuum invariant. This is relativistic invariance.
- **Stability (axiom 5):** energy is bounded below; the spectrum lies in the forward light cone. This is the "no negative-energy ghost" condition.

These are minimal physical requirements. The whole structural content of AQFT — Reeh–Schlieder this week, Bisognano–Wichmann next week, type III$_1$ classification two weeks later — is the *consequences* of these axioms taken together.

> **Physical picture.** A point that deserves emphasis before any theorem: *in AQFT, the theory is the net, not the algebras.* Under the hypotheses of Week 12, the local algebra of every double cone in every reasonable QFT is the *same* abstract object — the unique hyperfinite type III$_1$ factor. Free scalar, interacting $\phi^4$, QCD: their double-cone algebras are isomorphic. What distinguishes one theory from another is the *relative position* of the algebras — the map $\mathcal{O} \mapsto \mathcal{A}(\mathcal{O})$, i.e. how the subalgebras sit inside each other and inside $\mathcal{B}(\mathcal{H})$, and how the Poincaré unitaries weave them together. This is a Copernican shift from the Lagrangian viewpoint, where the field content seems to carry the physics. It also explains why this course spends so long on a single algebra-with-state: all the model-independent physics (Unruh, type III, entanglement structure) lives at that level, and all the model-dependent physics lives in the net geometry.

## 2. The Reeh–Schlieder theorem

**Theorem 2.1 (Reeh–Schlieder 1961). [Stated only — refs: Reeh & Schlieder, *Nuovo Cimento* 22 (1961) 1051; Streater & Wightman §4.2.]** *Assume the Haag–Kastler axioms 1–5 plus the technical assumption that the field operators $\phi(x)$ are tempered (Wightman QFT). For every non-empty open region $\mathcal{O}$ of Minkowski space, the vacuum vector $\Omega$ is **cyclic** for the local algebra $\mathcal{A}(\mathcal{O})$:*
$$
\overline{\mathcal{A}(\mathcal{O})\,\Omega} = \mathcal{H}.
$$

**Reading the statement.** Every state on Hilbert space can be approximated arbitrarily well by acting on the vacuum with operators supported in an arbitrarily small region. The vacuum already "contains" the whole theory — any state can be reached from it by a *local* operation.

This is genuinely counter-intuitive. A naive picture of the vacuum as a "ground state with no excitations" would forbid cyclicity for a tiny region: one would expect that you need to act in many regions to build a generic state (e.g., a state with a particle far from $\mathcal{O}$). The theorem says that naive picture is wrong. The vacuum is a **globally entangled state**, and local operations near a point can produce excitations of arbitrarily long-range character. The price is that the operators required for distant excitations are not "physically intuitive" — they are weighted polynomials in the field that operate locally on the vacuum but produce non-local effects via the vacuum's entanglement structure.

### 2.1 Sketch of the proof

We give the proof for a *single field operator* $\phi(f)$ smeared in $\mathcal{O}$. The full theorem requires polynomials in fields, and the argument iterates straightforwardly.

Suppose, for contradiction, $\psi \in \mathcal{H}$ satisfies
$$
\langle\psi, \phi(x_1)\cdots\phi(x_n)\,\Omega\rangle = 0 \quad \text{for all } x_1, \ldots, x_n \in \mathcal{O},\; n \ge 0.
$$
We will derive $\psi = 0$.

**Step 1: holomorphy in the forward tube.** Consider the function
$$
F(x_1, \ldots, x_n) := \langle\psi, \phi(x_1)\cdots\phi(x_n)\,\Omega\rangle.
$$
Use the spectral condition (axiom 5) to insert factors $e^{i x_j \cdot P}$:
$$
\phi(x_j)\,\Omega = e^{i x_j \cdot P}\,\phi(0)\,e^{-i x_j \cdot P}\,\Omega = e^{i x_j\cdot P}\,\phi(0)\,\Omega
$$
(using vacuum invariance $P\Omega = 0$, hence $e^{-ix_j \cdot P}\Omega = \Omega$). For $\mathrm{Im}\,x_j$ in the **forward tube** $V_+ = \{y \in \mathbb{R}^{1,d} : y^0 > |\vec y\,|\}$ (and $y^0 > 0$), the operator $e^{i x_j \cdot P} = e^{-(\mathrm{Im}\,x_j)\cdot P}\,e^{i(\mathrm{Re}\,x_j)\cdot P}$ extends to a bounded operator because $e^{-(\mathrm{Im}\,x_j)\cdot P}$ damps positive-energy states (since $\mathrm{Im}\,x_j \in V_+$ and $P \in \overline{V_+}$ means $(\mathrm{Im}\,x_j) \cdot P > 0$).

Hence $F$ extends to a function on the **product forward tube**
$$
\mathcal{T}_n^+ := \{(z_1, \ldots, z_n) \in \mathbb{C}^{(1+d)n} : \mathrm{Im}\,z_{j+1} - \mathrm{Im}\,z_j \in V_+ \text{ for } j = 1, \ldots, n-1\,\},
$$
**holomorphic** in each $z_j$ separately on this domain.

**Step 2: vanishing on a real open set.** By assumption, $F = 0$ for all real $x_j \in \mathcal{O}$. The boundary of $\mathcal{T}_n^+$ in $\mathbb{R}^{(1+d)n}$ includes the real open set $\mathcal{O}^n$.

**Step 3: edge-of-the-wedge.** The **edge-of-the-wedge theorem** (Streater–Wightman §2.5; Reed–Simon Vol. II §IX.8) says: a function holomorphic in a tube domain (such as $\mathcal{T}_n^+$) with a real boundary, vanishing on a real open subset of that boundary, vanishes identically on the tube.

**Step 4: extension by analytic continuation.** Once $F \equiv 0$ on the product forward tube, analytic continuation in each variable separately (using the Schwarz reflection principle and the Wightman analyticity machinery — Streater–Wightman §3) gives $F \equiv 0$ for *all* real $x_j \in \mathbb{R}^{1,d}$.

**Step 5: conclude.** $F \equiv 0$ for all $x_1, \ldots, x_n \in \mathbb{R}^{1,d}$ means $\psi \perp \phi(x_1)\cdots\phi(x_n)\Omega$ for all $n$ and all $x_j$. The polynomials in field operators acting on $\Omega$ span a dense subspace of $\mathcal{H}$ (by the Wightman reconstruction theorem: the vacuum is cyclic for the full field algebra). Hence $\psi = 0$, contradicting our hypothesis. $\square$

### 2.2 What the proof uses

The argument relies on three structural facts:

1. **The spectral condition gives forward-tube holomorphy.** Energy positivity $P^0 \ge 0$ is what allows analytic continuation to imaginary times in the forward direction. Without it, the argument fails.

   *Physical aside:* this is the same mechanism that licenses Wick rotation. "Energy bounded below" means $e^{-\tau H}$ is a legitimate damping operator for $\tau > 0$, so correlators extend analytically to imaginary time — stability of the vacuum *is* Euclidean analyticity. Reeh–Schlieder is thus a cousin of the familiar fact that Euclidean correlators are real-analytic away from coincident points: an analytic function pinned to zero on an open set has no freedom left anywhere. The vacuum's rigidity under local probing is the operator-theoretic face of the analyticity that field theorists use daily.

2. **Edge-of-the-wedge converts "vanishes on real open set" into "vanishes everywhere on the tube."** This is a powerful theorem of several complex variables; the 1D analog is the trivial fact that a holomorphic function on the upper half-plane vanishing on a real interval is identically zero.

3. **Polynomials in field operators generate a dense subspace from $\Omega$.** This is the Wightman cyclicity of the vacuum for the *global* field algebra. The Reeh–Schlieder theorem then upgrades it from global cyclicity to local cyclicity.

None of these uses interaction structure or specific field content, only the Wightman/Haag–Kastler axioms. The theorem holds in **any** Wightman QFT.

## 3. Separating from cyclic via locality

**Theorem 3.1 (Reeh–Schlieder corollary). [Proved.]** *Assume Haag–Kastler 1–5. For every open region $\mathcal{O}$ whose causal complement $\mathcal{O}'$ is non-empty and open, the vacuum $\Omega$ is **separating** for $\mathcal{A}(\mathcal{O})$.*

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

By Lemma 1.2 of Week 5 (cyclic-separating ↔ faithful normal state), this is exactly the input Tomita–Takesaki needs.

**Corollary 3.2. [Proved.]** *Every local algebra $\mathcal{A}(\mathcal{O})$ in a Wightman QFT (with $\mathcal{O}$ open and $\mathcal{O}'$ non-empty open) carries a canonical modular operator $\Delta_\mathcal{O}$, modular conjugation $J_\mathcal{O}$, and modular flow $\sigma_t^\mathcal{O}(a) = \Delta_\mathcal{O}^{-it}\,a\,\Delta_\mathcal{O}^{it}$ (our upper-strip convention, Week 5) with respect to the vacuum.*

**This is the licensing theorem of the entire course.** Without Reeh–Schlieder, we would not know that the local algebras of QFT have modular structure with respect to the physically natural state. Tomita–Takesaki gives modular structure for *cyclic-separating* vectors; Reeh–Schlieder is what guarantees the vacuum is cyclic-separating for local algebras.

## 4. Implications and surprises

The Reeh–Schlieder theorem is **counter-intuitive** in three specific ways. Each one is worth dwelling on.

### 4.1 No "vacuum experiments" can be localized

Imagine an experimenter who could *only* perform measurements in a bounded laboratory $\mathcal{O}$ — i.e., who can implement any element of $\mathcal{A}(\mathcal{O})$, but nothing in the spacelike-separated complement. Naively, the experimenter is restricted to the "$\mathcal{O}$-part" of the vacuum. Reeh–Schlieder says no such restriction exists: the experimenter can approximate **any** vector in Hilbert space — including states with arbitrarily high energy, or with particles localized far away from $\mathcal{O}$.

This does **not** violate causality. A correct way to phrase it: the experimenter can *approximate* any global state, but the operators required to approximate a far-away particle state have wild non-local behaviour. They are *in* $\mathcal{A}(\mathcal{O})$ as elements of the algebra, but they do not have a "local realistic" interpretation as preparing a localized particle — they exploit the global entanglement of the vacuum.

A quantitative way to see why causality survives: the relevant operators $a \in \mathcal{A}(\mathcal{O})$ with $a\Omega \approx |\text{particle behind the moon}\rangle$ are *not unitary* (or, if unitarized, have enormous norm-versus-effect trade-offs). Acting with a non-unitary $a$ is not a physical operation but a *selective* one — it corresponds to a measurement plus postselection on an outcome whose vacuum probability $\|a\Omega\|^2/\|a\|^2$ is fantastically small. The experimenter "creates" the distant particle only in the conditioned ensemble, exactly as a Bell-pair measurement "creates" a definite distant spin: no signal, no energy transfer, only exploitation of correlations already present. The smaller the region $\mathcal{O}$ and the more distant the target excitation, the more violent the postselection — this is the operational price hidden in the innocent word "cyclic."

The classical analogue: every continuous function on $[0, 1]$ can be uniformly approximated by polynomials, but a polynomial that approximates $\sin(100\,x)$ on $[0, 1]$ has wild behaviour off $[0, 1]$ — its restriction to $[0, 1]$ is constrained but it carries "global" information.

**The lesson for relativistic QFT:** states are non-local; observables are local; the action of local observables on the vacuum produces non-local states.

### 4.2 No type-I local algebras

A simple corollary: the local algebra $\mathcal{A}(\mathcal{O})$ for a bounded open region **cannot be type I** in a relativistic QFT.

**Argument.** If $\mathcal{A}(\mathcal{O}) \cong \mathcal{B}(\mathcal{K})$ for some Hilbert space $\mathcal{K}$, then $\mathcal{H}$ would split as $\mathcal{K} \otimes \mathcal{K}'$ with $\mathcal{A}(\mathcal{O}') = 1 \otimes \mathcal{B}(\mathcal{K}')$ (by Haag duality + type-I structure — both required). The vacuum would have a Schmidt decomposition with strictly positive Schmidt coefficients (cyclic-separating). The corresponding vacuum entanglement entropy
$$
S_{\mathrm{vN}}(\rho_\mathcal{O}) = -\sum_n p_n \log p_n
$$
would be finite.

But it is a basic fact about QFT that vacuum entanglement entropy across **any** geometric cut **diverges in the UV** (the area law $S \sim \mathrm{Area}/\epsilon^{d-1}$ as $\epsilon \to 0$). So no type-I structure can accommodate it. $\square$

This argument suggests type II or III. Block C will narrow it further to type III$_1$ (Week 12, under explicit hypotheses).

### 4.3 The vacuum is "as far from product as possible"

In quantum information language: the vacuum is **maximally entangled** between spacelike-separated regions, in the strong sense that no bounded operator on one side can disentangle it. This is the source of:

- **Bell–CHSH saturation** at the Tsirelson bound between spacelike-separated wedges (Week 11, Summers–Werner);
- **Entanglement embezzlement** being *exact* in type III$_1$ (van Daele; Sem II);
- **Universal relative entropy structure** at the boundary (Araki–Uhlmann is well-defined; absolute entropy diverges).

These are not three independent observations but three faces of the same structural fact: the vacuum's global entanglement, made precise by Reeh–Schlieder + the type III$_1$ structure of bounded local algebras.

### 4.4 The "experimentalist's paradox"

A well-known philosophical conundrum: if the vacuum already "contains" every state in the sense of Reeh–Schlieder cyclicity, why can't we extract energy or particles from the vacuum by local operations? The answer is that the **operators** in $\mathcal{A}(\mathcal{O})$ that act on the vacuum to produce, say, a far-away electron state are not "physical local operations" in any reasonable sense. They are bounded operators (so legitimate elements of the algebra), but implementing them experimentally would require infinite expectation values of some other observable (the "fluctuation cost"). The vacuum is *energetically* stable; cyclicity is an algebraic statement, not an operational one.

This is sometimes phrased as: **Reeh–Schlieder cyclicity is mathematically generic but operationally inaccessible.** The two senses don't conflict; they describe different aspects of the same algebra.

## 5. Worked example: 2D free scalar in the wedge

We verify cyclic-separating for the right Rindler wedge $W_R = \{x: x^1 > |x^0|\}$ in the 2D massless free scalar, using the explicit mode decomposition of Week 8.

### 5.1 A dense set of states

Polynomials in $\phi(f)$ for $f$ supported in $W_R$, applied to $|0\rangle$, give the dense subspace
$$
\mathcal{D}_{W_R} := \mathrm{span}\!\left\{\phi(f_1)\cdots\phi(f_n)\,|0\rangle : f_j \in \mathcal{S}(W_R)_{\mathbb{R}}, n \in \mathbb{N}_0\right\}.
$$
We claim $\overline{\mathcal{D}_{W_R}} = \mathcal{H}$.

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

### 5.3 Density via Paley–Wiener

The Paley–Wiener theorem says: a function $g(k)$ in $L^2(\mathbb{R})$ extends to a holomorphic function on the upper half-plane with controlled growth iff its inverse Fourier transform $\check g(x)$ has support in $\{x \ge 0\}$. Combined with the structure of the Wightman tube argument, this implies the polynomials in field operators $\phi(f_j)$ with $f_j \in W_R$ produce a dense set of mode profiles in Fock space.

**Step-by-step.** A general one-particle Fock-space vector is $\int dk\, h(k)\,a_k^\dagger|0\rangle$ for some $h \in L^2$. Pick $f \in \mathcal{S}(W_R)_{\mathbb{R}}$ so that $\tilde f_R(k)$ approximates $\sqrt{4\pi k}\,h(k)$ on the support of interest; then $\phi(f)|0\rangle$ approximates $\int dk\, h(k)\,a_k^\dagger|0\rangle$. The full Paley–Wiener density argument extends this to the dense subspace of polynomials.

### 5.4 Separating via causal complement

$W_R' = W_L$. By Reeh–Schlieder cyclicity applied to $W_L$ (same argument), $\Omega$ is cyclic for $\mathcal{A}(W_L)$. By Theorem 3.1, $\Omega$ is separating for $\mathcal{A}(W_R)$.

### 5.5 What we have proved (for the 2D massless free scalar)

- $\Omega$ is cyclic for $\mathcal{A}(W_R)$.
- $\Omega$ is separating for $\mathcal{A}(W_R)$.
- Hence Tomita–Takesaki applies, and $\mathcal{A}(W_R)$ has canonical modular data $(\Delta_{W_R}, J_{W_R}, \sigma_t^{W_R})$ with respect to the vacuum.

This is the concrete verification that Tomita–Takesaki applies to wedge algebras of the free 2D massless scalar. Week 10 will compute the resulting modular operator explicitly via Bisognano–Wichmann.

## 6. Variations and limits

### 6.1 Other regions

Reeh–Schlieder works for **any** non-empty open region — not just wedges. So $\Omega$ is also cyclic for $\mathcal{A}(\mathcal{O})$ for:
- **Bounded double cones** $\mathcal{O}_r := \{x: |x^0| + |\vec x| < r\}$ (the diamond of radius $r$ around the origin).
- **Balls at fixed time** $\{x: x^0 = 0, |\vec x| < r\}$ — even single-time-slice regions.
- **Arbitrary unions of open regions**.

The cyclicity is robust. The *type* of the resulting local algebra varies with the region (next week and Week 12).

### 6.2 Beyond Wightman QFT

Reeh–Schlieder uses the Wightman analyticity machinery (tempered fields, forward-tube extension). For more general AQFT setups — say, Haag–Kastler nets without an explicit field operator — the analog holds under suitable axioms (existence of a vacuum, locality, covariance, spectral condition), but the proof is more abstract.

For QFT on **curved spacetimes**, an analog holds (Strohmaier–Verch) under microlocal analyticity conditions, but the structure depends on which "vacuum" one picks (in curved spacetime there is no preferred vacuum, generally).

### 6.3 Failure in non-relativistic QFT

For non-relativistic field theories — e.g., a free Schrödinger field — Reeh–Schlieder fails. The spectral condition (axiom 5) does not hold in the Lorentz-covariant sense; the "vacuum" (lowest-energy state) is local in a stricter sense, and cyclicity can be confined to one region.

Concretely: a free non-relativistic particle on a line has Galilean rather than Lorentz invariance; the algebra of position-localized operators has a natural cyclic vector only when the region is large enough to support a wavefunction. Bounded regions are too small.

This contrast is one of the deep features distinguishing relativistic from non-relativistic QFT.

## 7. What to take away

- **Stated only:** Reeh–Schlieder — the vacuum is cyclic for every non-empty local algebra $\mathcal{A}(\mathcal{O})$ in a Wightman QFT.
- **Proved (from cyclic + locality):** the vacuum is also separating, hence cyclic-separating, for every $\mathcal{A}(\mathcal{O})$ with non-empty open complement.
- **Consequence (Corollary 3.2):** every such local algebra has canonical Tomita–Takesaki data $(\Delta, J, \sigma_t)$ with respect to the vacuum.
- **No type-I local algebras:** Reeh–Schlieder + the divergence of vacuum entanglement entropy across any cut rules out type I for bounded regions.
- **Vacuum is maximally entangled:** the source of Tsirelson saturation, embezzlement, and universal relative-entropy structure between local algebras.
- **Operationally subtle:** cyclicity is algebraic; operators in $\mathcal{A}(\mathcal{O})$ that produce distant states are mathematically in the algebra but cannot be implemented experimentally in any local realistic sense.

## 8. Looking ahead

Week 10 is the central computational lecture of Block C: the **Bisognano–Wichmann theorem**, which identifies the modular operator of the vacuum on a Rindler-wedge algebra with the exponentiated Lorentz boost generator. This is the only general theorem in physics in which the modular operator is known *explicitly*. Every Sem II mini-calculation builds on it. The combination Reeh–Schlieder (this week) + Bisognano–Wichmann (next week) + type III$_1$ (Week 12) is the structural input for everything that follows.

## 9. Problem set

**Core problems.**

**1. Cyclic without spectral condition.** Show that *without* the spectral condition (axiom 5), Reeh–Schlieder fails. (*Hint:* construct a counterexample using a free non-relativistic particle on $\mathbb{R}$. The field algebra still has a local-net structure, but the ground state is not cyclic for compactly-supported observables.)

**2. Cyclic for a bounded region in 2D massless free scalar.** For the 2D massless scalar, take $\mathcal{O}$ to be a bounded square $[t_1, t_2] \times [s_1, s_2]$ with $s_1 > |t_2|$ (so $\mathcal{O} \subset W_R$). Sketch the Paley–Wiener argument that $\overline{\mathcal{A}(\mathcal{O})\,|0\rangle} = \mathcal{H}$. You don't need to make the analytic continuation rigorous; identify the input.

**3. Separating for double cones.** Let $\mathcal{O}_r = \{x: |x^0| + |\vec x| < r\}$ be a double cone of radius $r$ centered at the origin. Show that $\mathcal{O}_r' \neq \emptyset$, and conclude (via Theorem 3.1) that the vacuum is separating for $\mathcal{A}(\mathcal{O}_r)$.

**4. Haag duality for wedges (free scalar).** For the free 2D massless scalar, verify Haag duality for wedges:
$$
\mathcal{A}(W_R)' = \mathcal{A}(W_L).
$$
*Hint:* show both inclusions. $\mathcal{A}(W_L) \subset \mathcal{A}(W_R)'$ is locality. For the reverse, use the explicit mode decomposition into right- and left-movers (Week 8 §3.1) and the fact that wedges have "maximal" causal structure. Equivalently: use Bisognano–Wichmann (Week 10) to identify $J_{W_R}\mathcal{A}(W_R) J_{W_R} = \mathcal{A}(W_L)$.

**5. A non-Reeh–Schlieder example.** Construct a free *non-relativistic* field theory (e.g., a Schrödinger field on the line) and exhibit a vector orthogonal to $\mathcal{A}(\mathcal{O})\,\Omega$ for a bounded region $\mathcal{O}$, where $\Omega$ is the ground state. Identify which axiom (spectral condition?) fails.

**6. Vacuum entanglement entropy diverges.** For the 2D massless free scalar, use a UV regulator $\epsilon$ (lattice spacing or momentum cutoff) and compute the vacuum entanglement entropy across $x^1 = 0$ at fixed $x^0 = 0$. Show it diverges as $-c\log\epsilon + \text{const}$ for some positive $c$. (*This is the Calabrese–Cardy formula with $c$ the central charge; $c = 1$ for massless free scalar.*)

**Starred problems.**

**7\*. Edge of the wedge.** State the edge-of-the-wedge theorem precisely (Reed–Simon Vol. II §IX.8). Sketch the proof in the one-dimensional case: a function holomorphic in the upper half-plane and vanishing on a real interval is identically zero (Schwarz reflection). Where does the proof generalize cleanly to higher-dimensional tubes, and where is it delicate?

**8\*. Type-I rules out cyclic-separating without infinite entanglement.** Let $\mathcal{M} = M_n(\mathbb{C})$ on $\mathcal{K} \otimes \mathcal{K}$, and let $\Omega$ be a cyclic-separating vector for $\mathcal{M} \otimes 1$. Show that $\Omega$ has Schmidt rank exactly $n$ (full Schmidt rank), and compute the vN entropy of the reduction to $\mathcal{M}$ in terms of the Schmidt coefficients. Conclude that "cyclic-separating" plus "type I" forces strictly positive entanglement entropy — bounded above by $\log n$.

**9\*. Modular operator of the entire field algebra.** For the free scalar on Minkowski, let $\mathcal{A} = \mathcal{B}(\mathcal{H})$ (the entire bounded operator algebra; not a local algebra). Show that the modular operator of the vacuum is **trivial**: $\Delta = 1$. Why does this not contradict Bisognano–Wichmann?

**10\*. The vacuum vs. an excited state.** Let $|\psi\rangle = \phi(f)|0\rangle$ for $f$ supported in a small region. Is $|\psi\rangle$ cyclic-separating for $\mathcal{A}(\mathcal{O}')$ for the causal complement? Reeh–Schlieder gives cyclicity for the *vacuum* specifically; to what extent do excited states inherit cyclic-separating property? (*Hint:* if $f$ is supported in $\mathcal{O}$ and $\mathcal{O} \cap \mathcal{O}' = \emptyset$, then $|\psi\rangle$ is generally also cyclic for $\mathcal{A}(\mathcal{O}')$ by a similar argument.)

**11\*. Free scalar at finite volume.** For the free scalar on a torus $T^d$ (finite spatial volume), Reeh–Schlieder should fail because there is no spectral-condition tube. Yet the vacuum (lowest-energy state of the harmonic-oscillator-like spectrum) exists. Discuss informally: is the vacuum cyclic for local-region algebras? (Hint: at finite volume, the algebra is type I and the answer depends on the spectrum gap.)

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block C. Last revised 2026-06-11.*
