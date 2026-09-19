---
title: "Week 11 — Bell–CHSH Inequalities in QFT"
type: lecture-notes
course: syllabus
semester: 1
week: 11
block: C
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 8–10 (Weyl algebras, Reeh–Schlieder, Bisognano–Wichmann)
modified: 2026-06-11
---

# Week 11 — Bell–CHSH Inequalities in QFT

> *Bell inequalities are usually presented as a statement about two qubits in an entangled state. In QFT they become a statement about **complementary local algebras**: the Summers–Werner theorem says that for any pair of spacelike-separated regions, the **vacuum** saturates the Tsirelson bound $2\sqrt 2$. There is no need for state preparation: the vacuum already is maximally Bell-violating between any two wedges. The mechanism is the type III$_1$ structure of local algebras (next week) combined with Bisognano–Wichmann (last week). This lecture is the direct foundation for the group's research line on Bell–CHSH in QFT.*

## 0. Reading

**Primary:**
- Summers & Werner, "Bell's inequalities and quantum field theory," *J. Math. Phys.* 28 (1987) 2440 — the foundational paper.
- Summers & Werner, "Maximal violation of Bell's inequalities is generic in quantum field theory," *Comm. Math. Phys.* 110 (1987) 247 — the generic-violation theorem.
- Summers & Werner, "Bell's inequalities in algebraic quantum field theory," *Lett. Math. Phys.* 33 (1995) 321 — the refined statement under (N) + (SP).

**Secondary:**
- Summers, "On the independence of local algebras in quantum field theory," *Rev. Math. Phys.* 2 (1990) 201 — survey of statistical independence and Bell-type inequalities.
- Haag, *Local Quantum Physics*, ch. V §5 (statistical independence of complementary algebras).

**Group's research (course-tied):**
- De Fabritiis, Sorella, Roditi, Guimarães et al., recent papers on Bell-CHSH in free scalar, Proca, and gauge theories — concrete observable constructions; instructor selects 2–3.

**Optional research reading:**
- Tsirelson, "Quantum generalizations of Bell's inequality," *Lett. Math. Phys.* 4 (1980) 93 — the original Tsirelson bound.
- Werner, "Quantum states with Einstein–Podolsky–Rosen correlations admitting a hidden-variable model," *Phys. Rev. A* 40 (1989) 4277 — what is and isn't classically simulable.
- Hayden, Jozsa, Petz, Winter, "Structure of states which satisfy strong subadditivity of quantum entropy with equality," *Comm. Math. Phys.* 246 (2004) 359 — type III$_1$ as the unique setting for various optimal quantum-information tasks.

## 1. The CHSH inequality and the Tsirelson bound

### 1.1 The classical Bell bound

Consider two observers, Alice and Bob, each with two binary measurement choices. Let $A_1, A_2$ denote Alice's measurement outcomes (random variables taking values in $\{-1, +1\}$), and $B_1, B_2$ Bob's. The **CHSH expression** is
$$
\mathcal{C}_{\mathrm{CHSH}} := A_1 B_1 + A_1 B_2 + A_2 B_1 - A_2 B_2.
$$
At each round of the experiment, $A_i, B_j \in \{-1, +1\}$ are individual outcomes. A simple casework shows that in *any* classical scenario (assignments $A_i, B_j$ from a joint distribution),
$$
|\mathcal{C}_{\mathrm{CHSH}}| \le 2.
$$
Hence
$$
\big|\mathbb{E}[\mathcal{C}_{\mathrm{CHSH}}]\big| \le 2,
$$
the **classical bound**. This holds in any **local hidden-variable theory** where the joint distribution of $A_1, A_2, B_1, B_2$ exists.

**Proof.** For any $A_i, B_j \in \{\pm 1\}$, $A_1(B_1 + B_2) + A_2(B_1 - B_2)$ equals either $\pm 2A_1$ or $\pm 2A_2$, so $|\mathcal{C}_{\mathrm{CHSH}}| \le 2$. $\square$

### 1.2 The quantum (Tsirelson) bound

In quantum mechanics, $A_i$ and $B_j$ are bounded self-adjoint operators (not random variables), and $\mathbb{E}[\cdot]$ is the expectation in a state $\omega$:
$$
\langle\mathcal{C}_{\mathrm{CHSH}}\rangle_\omega := \omega(A_1 B_1) + \omega(A_1 B_2) + \omega(A_2 B_1) - \omega(A_2 B_2).
$$
For commuting subalgebras $\mathcal{M}_A, \mathcal{M}_B \subset \mathcal{B}(\mathcal{H})$ (Alice and Bob's operators) with $A_i, B_j$ self-adjoint and spectrum in $[-1, 1]$:

**Theorem 1.1 (Tsirelson 1980). [Proved.]** $|\langle\mathcal{C}_{\mathrm{CHSH}}\rangle_\omega| \le 2\sqrt 2$ for any state $\omega$.

**Proof sketch.** First take the *dichotomic* case $A_i^2 = B_j^2 = 1$. Squaring the CHSH operator and using $[A_i, B_j] = 0$ (commutativity of Alice and Bob), all cross terms cancel except one:
$$
\mathcal{C}_{\mathrm{CHSH}}^2 = 4 - [A_1, A_2]\,[B_1, B_2]
$$
(expand and check: the $A_i^2 = B_j^2 = 1$ condition kills the diagonal terms into the constant 4, and the surviving off-diagonal terms assemble into the product of commutators). Then $\|[A_1, A_2]\| \le 2\|A_1\|\|A_2\| = 2$ and similarly for $B$, so $\|\mathcal{C}_{\mathrm{CHSH}}^2\| \le 4 + 4 = 8$ and $\|\mathcal{C}_{\mathrm{CHSH}}\| \le 2\sqrt 2$. The general spectrum-in-$[-1,1]$ case reduces to the dichotomic case: any self-adjoint contraction is a convex combination (an average over a dilation) of self-adjoint unitaries, and the CHSH expectation is affine in each observable, so the supremum is attained on dichotomic quadruples. $\square$

This is the **Tsirelson bound**, the quantum-mechanical replacement for the classical bound.

> **Physical picture.** The squared identity is a precise accounting of *where quantum violation comes from*. The classical bound 2 is recovered when either commutator vanishes: if Alice's two measurement choices are compatible (or Bob's), a joint distribution for her outcomes exists and the hidden-variable argument applies — no violation, regardless of entanglement. Conversely, noncommutativity alone is not enough: the term $[A_1,A_2][B_1,B_2]$ contributes to the *expectation* only if the state correlates Alice's and Bob's commutators, which is an entanglement property. So CHSH violation requires three things at once — incompatible observables on the left, incompatible observables on the right, and a state that entangles the two incompatibilities — and the formula shows the maximum is reached when both commutators have norm 2 and the state aligns them perfectly. The Summers–Werner theorem below says that QFT wedge algebras, in the vacuum, supply all three ingredients in their extremal form, with no preparation.

### 1.3 Saturation in standard QM

The Tsirelson bound is **achievable** in finite-dimensional QM. The textbook example: take Alice and Bob each holding a qubit, in the singlet state
$$
|\psi^-\rangle = \tfrac{1}{\sqrt 2}\,(|01\rangle - |10\rangle).
$$
Choose Alice's measurements as $A_1 = \sigma_z$, $A_2 = \sigma_x$; Bob's as $B_1 = (-\sigma_z - \sigma_x)/\sqrt 2$, $B_2 = (-\sigma_z + \sigma_x)/\sqrt 2$. Then
$$
\langle\psi^-|\,\mathcal{C}_{\mathrm{CHSH}}\,|\psi^-\rangle = 2\sqrt 2.
$$
**The singlet saturates Tsirelson.** Other states give weaker violations or none.

In QFT, the story is radically different: the **vacuum** plays the role of the singlet, between **any** two spacelike-separated regions. This is the content of Summers–Werner.

## 2. The Summers–Werner theorem

### 2.1 Statement

**Theorem 2.1 (Summers–Werner). [Stated only — refs: Summers–Werner 1987a, 1987b, 1995.]** *Assume the Haag–Kastler axioms (Weeks 8–9) together with type III$_1$ structure of the local algebras (Week 12 — provided by (N) + (SP)). Let $\mathcal{A}(W_R), \mathcal{A}(W_L)$ be the local algebras of complementary right and left Rindler wedges. For every $\epsilon > 0$, there exist self-adjoint $A_1, A_2 \in \mathcal{A}(W_R)$ and $B_1, B_2 \in \mathcal{A}(W_L)$, each with spectrum in $[-1, 1]$, such that*
$$
\big|\,\langle 0\,|\,\mathcal{C}_{\mathrm{CHSH}}(A_1, A_2, B_1, B_2)\,|0\rangle\,\big| \;\ge\; 2\sqrt 2 - \epsilon.
$$

**Stronger forms (Summers–Werner 1987b, 1995). [Stated only — hypothesis-explicit; refs as above.]** Under the Haag–Kastler axioms plus the nuclearity (N) + split-property (SP) of Week 12, plus the assumption that the local algebras are type III$_1$:
- The supremum $\sup |\langle\mathcal{C}_{\mathrm{CHSH}}\rangle_\omega|$ over admissible quadruples is exactly $2\sqrt 2$ for every faithful normal state $\omega$ on the joint algebra $\mathcal{A}(W_R) \vee \mathcal{A}(W_L)$, not just the vacuum.
- The same holds for any pair of spacelike-separated wedge-like regions (regions whose local algebras admit Bisognano–Wichmann-style modular flow), not only Rindler wedges.
- The supremum is approached arbitrarily closely but not generally attained by any concrete bounded-spectrum quadruple; the limit involves the modular flow of Bisognano–Wichmann.

The "every faithful normal state" claim is a non-trivial structural property of type III$_1$ algebras with commuting subalgebras admitting a joint cyclic-separating vector — it does **not** hold without these hypotheses. In particular, in a UV-regulated (type-I) version of the theory, Tsirelson saturation fails on generic states.

### 2.2 Structural ingredients

The Summers–Werner proof uses three structural inputs from previous weeks:

1. **Reeh–Schlieder (Week 9):** the vacuum is cyclic-separating for $\mathcal{A}(W_R)$, hence faithful normal.
2. **Bisognano–Wichmann (Week 10):** the modular flow on $\mathcal{A}(W_R)$ is the boost subgroup, with full real spectrum.
3. **Type III$_1$ (Week 12, anticipated):** the wedge algebras are "as non-tracial as possible," with rich projection lattice.

Item 3 is the heart of the matter. In a type III$_1$ factor, the projection lattice has "enough room" — combined with the commuting pair $\mathcal{A}(W_R), \mathcal{A}(W_L)$ — to find a quadruple of observables saturating any bound below $2\sqrt 2$. In type I (e.g., finite-dim QM with the singlet), saturation is achievable but isolated to specific maximally entangled states; in type III$_1$, **every** faithful normal state saturates.

### 2.3 Contrast with finite-dimensional QM

The qualitative difference is worth dwelling on:

| Setting | Algebra type | When does Tsirelson saturate? |
|---|---|---|
| Finite-dim QM | type I$_n$ | only on maximally entangled states (e.g., singlet) |
| Generic mixed-state QM | type I | not generically; needs careful state engineering |
| QFT wedge algebras | type III$_1$ (under (N) + (SP)) | every faithful normal state on the joint two-sided algebra, including vacuum |

This is the algebraic content of "the vacuum is maximally entangled" in QFT. **Bell–CHSH saturation is not a finely-tuned property; it is a structural consequence of the algebra type.**

## 3. The heuristic: why is the vacuum so entangled?

Reeh–Schlieder (Week 9) already told us that the vacuum is non-local: local operations near a point can produce any global state. Bisognano–Wichmann (Week 10) added a sharper picture: the vacuum, restricted to a wedge, is **thermal** at the Unruh temperature $T_U = a/(2\pi)$ relative to wedge-restricted observers.

Putting these together: the **regulated** density matrix of the vacuum restricted to $\mathcal{A}(W_R)$ would be (formally)
$$
\rho_{W_R}^{\mathrm{reg}} \;\propto\; e^{-2\pi K_{\mathrm{reg}}},
$$
i.e., a Gibbs state at the Unruh "temperature" with modular Hamiltonian $K$. In a finite-dim regularization, this looks like a thermal state with non-trivial entropy. In the **unregulated** limit, the regulator pushes the entanglement entropy to infinity, and the algebra becomes type III$_1$.

The Tsirelson saturation is the algebraic content of: *the vacuum, when restricted to one side of a spacelike split, behaves like an infinite-temperature thermal state* — except that the right notion of "infinite temperature" is the type-III$_1$ algebra of the wedge, where every state is similarly thermal-like.

**This is why QFT differs structurally from finite-dim QM.** In finite-dim QM, "maximally entangled" is a special property of certain states (the singlet, the maximally mixed state on a bipartite system). In QFT, "maximally entangled" is the generic property of *every* state on a wedge — it is built into the algebra, not into the state.

## 4. Explicit construction in the 2D massless free scalar

The Summers–Werner theorem is existence; for the group's research program, we want **explicit observables**. The standard construction uses **Weyl-cosine observables** built from bumpified Haar wavelets.

### 4.1 Dichotomic Weyl observables

Take real test functions $f \in \mathcal{S}(W_R)_{\mathbb{R}}$, $g \in \mathcal{S}(W_L)_{\mathbb{R}}$, and a real parameter $\alpha > 0$. The Weyl operator $W(\alpha f) = e^{i\alpha\phi(f)}$ is unitary; its Hermitian part is the **dichotomic observable**
$$
A(f, \alpha) := \frac{W(\alpha f) + W(\alpha f)^*}{2} = \cos(\alpha\,\phi(f)).
$$
$A(f, \alpha)$ is self-adjoint with spectrum in $[-1, 1]$ (since $\cos$ takes values in $[-1, 1]$). It is in $\mathcal{A}(W_R)$ (since both $W(\alpha f)$ and $W(\alpha f)^*$ are).

Similarly define $B(g, \beta) := \cos(\beta\phi(g)) \in \mathcal{A}(W_L)$ for $g \in W_L$.

These are *not* projections (no $\pm 1$ eigenvalues); they are bounded self-adjoint elements with spectrum in $[-1, 1]$. The Summers–Werner framework requires only spectrum-in-$[-1,1]$, not strict $\pm 1$ eigenvalues, so cosines suffice.

### 4.2 Vacuum two-point functions

Using the Gaussian character of the vacuum (Week 8 §4.2):
$$
\langle 0\,|\,\cos(\alpha\phi(f))\,|0\rangle = \tfrac{1}{2}\left(\langle 0|e^{i\alpha\phi(f)}|0\rangle + \langle 0|e^{-i\alpha\phi(f)}|0\rangle\right) = e^{-\alpha^2 W(f, f)/2},
$$
where $W(f, f) = \langle 0|\phi(f)^2|0\rangle$ is the vacuum two-point function (real and positive for real $f$, Week 8 §3).

A useful identity for the two-cosine correlator (proved by expanding cosines into exponentials and using Weyl-relation BCH cancellations):
$$
\langle 0\,|\,\cos(\alpha\phi(f))\cos(\beta\phi(g))\,|0\rangle = \tfrac{1}{2}\left(e^{-\frac{1}{2}\,\mathcal{Q}_+(f, g; \alpha, \beta)} + e^{-\frac{1}{2}\,\mathcal{Q}_-(f, g; \alpha, \beta)}\right),
$$
where
$$
\mathcal{Q}_\pm(f, g; \alpha, \beta) = \alpha^2 W(f, f) + \beta^2 W(g, g) \pm 2\alpha\beta\, \mathrm{Re}\,W(f, g).
$$
For real $f, g$, the symplectic-form part $\mathrm{Im}\,W(f, g)$ drops out for spacelike-separated $f, g$ (Week 8 §3 — $\sigma(f, g) = 0$ when supports are spacelike). So when $f \subset W_R$ and $g \subset W_L$, only $\mathrm{Re}\,W(f, g)$ enters.

### 4.3 The CHSH expectation in the vacuum

Pick four test functions: $f_1, f_2 \in \mathcal{S}(W_R)$, $g_1, g_2 \in \mathcal{S}(W_L)$, all real, and a common amplitude $\alpha$. Let
$$
A_i = \cos(\alpha\phi(f_i)), \qquad B_j = \cos(\alpha\phi(g_j)).
$$

The CHSH expectation in the vacuum is
$$
\langle 0\,|\,\mathcal{C}_{\mathrm{CHSH}}\,|0\rangle = \sum_{i, j} \pm \langle A_i B_j\rangle = \sum_{i, j} \pm\,\tfrac{1}{2}\!\left(e^{-\frac{1}{2}\mathcal{Q}_+^{(ij)}} + e^{-\frac{1}{2}\mathcal{Q}_-^{(ij)}}\right),
$$
with signs as in $\mathcal{C}_{\mathrm{CHSH}} = A_1 B_1 + A_1 B_2 + A_2 B_1 - A_2 B_2$. Each $\mathcal{Q}_\pm^{(ij)}$ involves the Wightman matrix element $W(f_i, g_j)$ which is a 2D integral over the test-function supports.

By appropriate choice of $f_i, g_j$ (in particular: by **boosting** $f_i$ toward the bifurcation surface and tuning the wavelet parameters), one can drive the inner products to extremal configurations and approach $2\sqrt 2$.

### 4.4 Approach to Tsirelson: the boost-limit procedure

Concretely (Summers–Werner 1987; De Fabritiis et al.):

1. **Fix wavelet bases** on $W_R$ and $W_L$. Use **bumpified Haar wavelets** centered at $(\tau_R, \xi_R) \in W_R$ and $(\tau_L, \xi_L) \in W_L$ with a common width $\sigma$.

2. **Boost the wavelets toward the bifurcation surface** $\{x^0 = x^1 = 0\}$. The boost parameter $\eta$ is the rapidity in the $(x^0, x^1)$ plane. As $\eta \to \infty$, the centers $\xi_R(\eta) \to 0^+$ (on the future null boundary of $W_R$) and $\xi_L(\eta) \to 0^-$ (on the future null boundary of $W_L$).

3. **Compute the Wightman correlator** $W(f_i, g_j)$ in the boost-limit. The correlator approaches a fixed extremal value because the boosted wavelets approach the bifurcation surface.

4. **The CHSH expectation approaches $2\sqrt 2$** from below, never attaining it for finite wavelet parameters.

The Summers–Werner **saturation** statement is the supremum claim:
$$
\sup_{f_i, g_j, \alpha} \big|\langle 0|\mathcal{C}_{\mathrm{CHSH}}|0\rangle\big| = 2\sqrt 2,
$$
attained as $\eta \to \infty$, and corresponding to "infinitely thin wavelets at the bifurcation surface."

The boost-limit is **exactly** the modular flow on the wedge algebras (Bisognano–Wichmann, Week 10), and this is the algebraic content of "saturating Tsirelson requires the full modular structure."

> **Physical picture.** Why must the wavelets crowd toward the bifurcation surface? Because that is where the vacuum's Bell pairs live. The entanglement of the vacuum across the cut is dominated by UV modes straddling the entangling surface — the same modes whose accumulation produces the area-law divergence (Week 9 §4.2) and the type III$_1$ structure (Week 12). A wavelet pair deep inside the two wedges sees only the exponential tail of these correlations and yields a sub-maximal violation; boosting the pair toward $x^0 = x^1 = 0$ zooms into shorter and shorter straddling modes, each of which is an ever-better approximation to a perfect Bell pair. Saturation is reached only in the limit — there is no "last Bell pair," just an inexhaustible scaling tower of them. This is the operational face of the type III$_1$ statement that the vacuum's entanglement is *infinite but nowhere locally cashable*: any finite experiment extracts $2\sqrt 2 - \epsilon$, never $2\sqrt 2$.

### 4.5 Worked example: two wavelets and explicit numbers

For concreteness: take 2D massless free scalar, and pick

- $f_1, f_2 \in W_R$ — Gaussian bumps with centers $(\tau_1, \xi_1) = (0.5, 1.5)$ and $(\tau_2, \xi_2) = (-0.5, 1.5)$, width $\sigma = 0.2$.
- $g_1, g_2 \in W_L$ — Gaussian bumps with centers $(-\tau_j, -\xi_j)$, mirrored in $W_L$.
- amplitude $\alpha = 1$.

The Wightman correlator for the 2D massless scalar is $W(x, y) = -(4\pi)^{-1}\log[\,-(x-y)^2 + i\epsilon(y^0 - x^0)\,]$. Smearing against the Gaussian bumps gives finite real-and-imaginary parts; in this configuration $W(f_i, g_j)$ is real (because of the mirror symmetry), and $\mathrm{Re}\,W(f_i, g_j)$ is order $\sim -0.1$ to $-0.5$ depending on the bump separation.

A numerical evaluation (typical of the group's papers) gives $\langle 0|\mathcal{C}_{\mathrm{CHSH}}|0\rangle \approx 2.1$ to $2.4$ in this configuration. Boosting the wavelets by rapidity $\eta$ and re-optimizing increases this toward $2\sqrt 2 \approx 2.828$. The group's papers report concrete numerical values for various configurations of wavelet parameters; verifying these is a Problem-set exercise.

## 5. The structural argument (no explicit wavelets)

The Summers–Werner proof does **not** require wavelets. The argument is algebraic and works uniformly across QFTs satisfying the axioms.

**Structural argument (sketch).** 

1. By Reeh–Schlieder + Bisognano–Wichmann, $\mathcal{A}(W_R)$ has a faithful normal modular state (the vacuum) with explicit modular operator $\Delta_{W_R} = e^{-2\pi K}$.

2. In a type III$_1$ factor with such a state, the **modular flow has full real spectrum** (Week 12). The projection lattice contains projections of every "modular weight": for each $\lambda \in \mathbb{R}$, there are projections $P_\lambda$ with $\sigma_t^{W_R}(P_\lambda) = e^{i\lambda t} P_\lambda$ in a generalized sense.

3. The richness of the modular projection structure, combined with the commuting wedge algebras $\mathcal{A}(W_R), \mathcal{A}(W_L)$, allows construction of dichotomic quadruples saturating Tsirelson. The key technical lemma (Summers–Werner 1987b): for any two commuting type III$_1$ factors $\mathcal{M}, \mathcal{N}$ with a cyclic-separating vector for $\mathcal{M} \vee \mathcal{N}$, the **maximally violating** quadruple exists by a density argument in the joint projection lattice.

**This argument:**
- is algebraic — no wavelets, no specific test functions;
- works uniformly for any Wightman QFT under (N) + (SP);
- gives the conclusion in any spacetime dimension;
- holds for any pair of spacelike-separated wedge-like regions;
- does **not** tell you *which* observables saturate — only that they exist.

The explicit wavelet construction of §4 is needed for the *constructive* form of the saturation, which is what the group's research papers compute.

## 6. Connection to the research program

The group's papers — De Fabritiis, Guimarães, Roditi, Sorella, and collaborators — sit precisely at the **explicit observable** side of Summers–Werner. The pattern in each paper:

1. **Pick a QFT** (free scalar, free Dirac, free Proca, ..).
2. **Pick a wedge pair** (or two spacelike-separated regions).
3. **Construct dichotomic observables** $A_i, B_j$ from Weyl-cosine or related operators with bumpified Haar wavelet test functions.
4. **Compute $\langle 0|\mathcal{C}_{\mathrm{CHSH}}|0\rangle$** as a function of wavelet parameters.
5. **Optimize** over parameters to maximize the violation.
6. **Compare** with the Summers–Werner bound $2\sqrt 2$.

Concrete topics covered in recent group papers:

- **Bell-CHSH inequality, local realism and quantum field theory** (and follow-ups) — explicit computation in 2D and 4D free scalar.
- **Massive scalar field** (mass $m > 0$): the wedge modular structure is unchanged, but correlators decay differently, leading to different rate of approach to Tsirelson.
- **Proca field** (massive vector): different field content, same algebraic structure, similar saturation pattern.
- **Gauge fields** (BRST formulation): the algebra structure is more delicate due to gauge invariance; explicit construction works after BRST cohomology.

**Open question** (wiki: [[bell-chsh-in-holographic-setting]]): does the Tsirelson saturation extend to the **boundary algebras of a holographic CFT**, and does the violation pattern probe topological features of the bulk? This is a research-level question with no consensus answer; it is one of the natural extensions for a final-paper topic.

## 7. What to take away

- **Stated only (Summers–Werner):** the vacuum saturates the Tsirelson bound for CHSH expectations between any two spacelike-separated wedge-like regions in any Wightman QFT under (N) + (SP). The supremum is $2\sqrt 2$ and is approached as a limit.
- **Computed (model proof in the 2D massless free scalar):** the CHSH expectation for cosine-Weyl observables built from real wedge-supported test functions approaches $2\sqrt 2$ in the boost-rapidity limit.
- **Structural inputs:** Reeh–Schlieder + Bisognano–Wichmann + type III$_1$. The full real spectrum of the modular flow is the algebraic source of saturation.
- **Distinction from QM (hypothesis-explicit):** in finite-dim QM, Tsirelson is achievable only on special maximally entangled states; in QFT, under (N) + (SP) + type III$_1$ structure on wedge-like algebras, it is approachable by faithful normal states on the joint two-sided algebra. The "every state" version of saturation requires the type-III$_1$ hypothesis on both sides; it fails in any UV-regulated (type-I) approximation.
- **Research-program anchor:** the group's explicit wavelet constructions sit on the "constructive" side of Summers–Werner. Open question — Bell-CHSH in holographic settings.

## 8. Looking ahead

Week 12 closes Block C by completing the **type III$_1$ classification** of QFT local algebras. We state the precise hypothesis-explicit theorem (Buchholz–D'Antoni–Fredenhagen, building on Driessler and Fredenhagen) and discuss why type III$_1$ — rather than I, II, or III$_\lambda$ for $\lambda < 1$ — is the structurally inevitable type for relativistic QFT. The implications for entropy, density matrices, and crossed products set up Block D's central construction.

## 9. Problem set

**Core problems.**

**1. CHSH expectation in finite-dim QM (warmup).** For the singlet $|\psi^-\rangle$ on $\mathbb{C}^2 \otimes \mathbb{C}^2$, with $A_i = \vec a_i \cdot \vec\sigma$ and $B_j = \vec b_j \cdot \vec\sigma$ for unit vectors $\vec a_i, \vec b_j$ in the $xz$-plane, compute $\langle\psi^-|\mathcal{C}_{\mathrm{CHSH}}|\psi^-\rangle$ and show it equals $2\sqrt 2$ when the four unit vectors are placed at angles $0, \pi/2, \pi/4, 3\pi/4$. Verify the geometric interpretation: the four vectors at $45°$ separations.

**2. Tsirelson bound (proof in finite-dim).** For commuting self-adjoint $A_i \in \mathcal{B}(\mathcal{H}_A)$, $B_j \in \mathcal{B}(\mathcal{H}_B)$ with $A_i^2 = B_j^2 = 1$ (dichotomic), prove the operator identity
$$
\mathcal{C}_{\mathrm{CHSH}}^2 = 4 - [A_1, A_2]\,[B_1, B_2],
$$
hence $\|\mathcal{C}_{\mathrm{CHSH}}\| \le \sqrt{4 + \|[A_1, A_2]\|\,\|[B_1, B_2]\|} \le 2\sqrt 2$. Then extend the bound to general self-adjoint contractions (spectrum in $[-1,1]$) by an affinity/convexity argument as in §1.2.

**3. Locality from spacelike $\sigma$.** For $f_R \subset W_R$ and $g_L \subset W_L$ in the 2D massless free scalar, verify directly that $[\cos(\alpha\phi(f_R)), \cos(\beta\phi(g_L))] = 0$. Use the Weyl relation $W(f)W(g) = e^{-i\sigma(f,g)/2}W(f+g)$ and the spacelike vanishing of $\sigma$.

**4. Compute $\langle A_1 B_1\rangle$ for cosine-Weyl observables.** In the 2D massless free scalar, take $f_1 \in W_R$ and $g_1 \in W_L$ as Gaussian bumps with parameters $(\tau, s; \sigma)$ and $(-\tau, -s; \sigma)$. Compute
$$
\langle 0\,|\,\cos(\alpha\phi(f_1))\,\cos(\alpha\phi(g_1))\,|0\rangle
$$
as a function of $\alpha, \tau, s, \sigma$ using the Gaussian formula in §4.2. Verify that for $\alpha \to 0$ the expectation goes to 1 and for $\alpha \to \infty$ it goes to 0.

**5. Read one group paper.** Pick a recent De Fabritiis–Sorella et al. paper on Bell-CHSH in QFT. Identify the precise observable construction (test functions, amplitude $\alpha$, wedge configuration), the parameters being optimized, and the highest $\langle\mathcal{C}_{\mathrm{CHSH}}\rangle$ value reported. Verify the parameter choices are consistent with the algebraic framework here.

**6. Real-vs-imaginary part of $W(f, g)$ for spacelike $f, g$.** Show explicitly that for $f \in W_R$ and $g \in W_L$ in the 2D massless free scalar, the imaginary part $\mathrm{Im}\,W(f, g)$ (= $\sigma(f, g)/2$) vanishes, while the real part $\mathrm{Re}\,W(f, g)$ is generically nonzero. (*Hint:* use the Pauli-Jordan support and the symmetric two-point function formulas of Week 8.)

**Starred problems.**

**7\*. Boost-limit of the CHSH expectation.** For the 2D massless free scalar, fix four real Gaussian wavelets supported in $W_R$ and $W_L$, then boost the $W_R$ wavelets by rapidity $\eta$ (and the $W_L$ wavelets by $-\eta$). Compute the limit of $\langle 0|\mathcal{C}_{\mathrm{CHSH}}|0\rangle$ as $\eta \to \infty$. Verify it approaches $2\sqrt 2$. (*Hint:* the Wightman correlator $W(f^\eta, g^{-\eta})$ approaches a fixed extremal value involving the bifurcation-surface correlator.)

**8\*. Massive scalar.** Repeat the analysis for the 2D *massive* free scalar (mass $m > 0$). Show that the Tsirelson saturation still holds (the modular structure on wedges is unchanged), but that the rate of approach to $2\sqrt 2$ depends on $m$. (*Hint:* the massive two-point function involves Bessel functions and decays exponentially with $m \cdot d$ where $d$ is the spacelike separation, modifying the optimization.)

**9\*. The Bell–CHSH operator on the modular flow.** Show that $\sigma_t^{W_R}(\mathcal{C}_{\mathrm{CHSH}}) = \mathcal{C}_{\mathrm{CHSH}}'$, where $\mathcal{C}_{\mathrm{CHSH}}'$ is the CHSH operator built from boosted observables (and dual-boosted on the $W_L$ side via the commutant). Use this to argue that the CHSH expectation in the vacuum is **invariant** under joint modular flow on the two wedges.

**10\*. Type-I would not saturate.** Take a finite-dim regulator of the free 2D massless scalar (e.g., a box of size $L$ with periodic boundary conditions, momentum cutoff $\Lambda$). Show that the local algebras at this regulated level are type I, and the maximum CHSH value over all admissible observables and states is *strictly less than* $2\sqrt 2$. Compute the leading dependence on $L\Lambda$. (*Hint:* type I$_n$ factors have Tsirelson supremum $2\sqrt 2$ only on highly specific states; on a generic regulated vacuum it falls short.)

**Project problems.**

**11. Bell–CHSH in holographic settings.** Read the wiki open question [[bell-chsh-in-holographic-setting]]. Identify a candidate test of "Bell-CHSH between two boundary subregions of a holographic CFT." What would maximally violating observables look like? What would non-saturation tell us about the bulk?

**12. Reproduce one group calculation.** Take a specific paper from the De Fabritiis–Sorella program (instructor selects). Reproduce one of the numerical CHSH violation calculations using the wavelet construction of this lecture. Compare the numbers; discuss any discrepancies.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block C. Last revised 2026-06-11.*
