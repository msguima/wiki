---
title: "Week 11 — Bell–CHSH Inequalities in QFT"
type: lecture-notes
course: syllabus
semester: 1
week: 11
block: C
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 8–10 (Weyl algebras, Reeh–Schlieder, Bisognano–Wichmann)
modified: 2026-08-24
---

# Week 11 — Bell–CHSH Inequalities in QFT

> *Bell inequalities are usually presented for two qubits. In AQFT they are formulated for two commuting local algebras. The strongest theorem used here concerns complementary wedges: under weak net assumptions, every vector state has maximal Bell correlation for suitable observables in the two wedge algebras; injectivity extends the conclusion to normal density-matrix states on the ambient Hilbert space. This is not a theorem about every pair of separated bounded regions, nor a consequence of type III$_1$ alone. The distinction between the structural supremum and explicit observable families organizes the lecture.*

### How to use this chapter

- **In class:** prove the finite-dimensional Tsirelson bound, define the Bell supremum for commuting algebras, and state Summers–Werner with its wedge and injectivity hypotheses before turning to explicit Weyl families.
- **For self-study:** reproduce the exact quasifree cosine correlator in §4.2 and one source-checked numerical row in §4.5. Mark every result as structural supremum, analytic value for an ansatz, or numerical lower bound.
- **Instructor checkpoint:** ask why a fixed boost cannot move a packet to the bifurcation point, why type III$_1$ alone does not determine Bell correlations, and why type-I systems can still attain $2\sqrt2$ in special states.

## 0. Reading

**Primary:**
- Summers & Werner, “Bell's inequalities and quantum field theory. I. General setting,” *J. Math. Phys.* **28** (1987) 2440–2447, DOI 10.1063/1.527733.
- Summers & Werner, “Bell's inequalities and quantum field theory. II. Bell's inequalities are maximally violated in the vacuum,” *J. Math. Phys.* **28** (1987) 2448–2456, DOI 10.1063/1.527734.
- Summers & Werner, “Maximal violation of Bell's inequalities is generic in quantum field theory,” *Comm. Math. Phys.* **110** (1987) 247–259, DOI 10.1007/BF01207366.

**Secondary:**
- Summers, "On the independence of local algebras in quantum field theory," *Rev. Math. Phys.* 2 (1990) 201 — survey of statistical independence and Bell-type inequalities.
- Haag, *Local Quantum Physics*, ch. V §5 (statistical independence of complementary algebras).

**Group's research (course-tied):**
- Dudal, De Fabritiis, Guimarães, Roditi & Sorella, “Maximal violation … via bumpified Haar wavelets,” *Phys. Rev. D* **108** (2023) L081701, arXiv:2307.04611 — massless spinor field.
- De Fabritiis et al., “Weyl operators, Tomita–Takesaki theory, and Bell-CHSH inequality violations,” *Phys. Rev. D* **108** (2023) 085026, arXiv:2309.02941 — free real scalar field.
- De Fabritiis et al., “Numerical approach to the Bell-CHSH inequality in quantum field theory,” *Phys. Rev. D* **110** (2024) 065006, arXiv:2406.20033 — scalar Gaussian numerical search.
- Guimarães, Roditi & Sorella, “On a class of bounded Hermitian operators for the Bell-CHSH inequality in Quantum Field Theory,” arXiv:2506.00504 — scalar field and tangent diamonds.

**Optional research reading:**
- Tsirelson, "Quantum generalizations of Bell's inequality," *Lett. Math. Phys.* 4 (1980) 93 — the original Tsirelson bound.
- Werner, "Quantum states with Einstein–Podolsky–Rosen correlations admitting a hidden-variable model," *Phys. Rev. A* 40 (1989) 4277 — what is and isn't classically simulable.

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

**Proof.** First take the *dichotomic* case $A_i^2 = B_j^2 = 1$. Squaring the CHSH operator and using $[A_i, B_j] = 0$, all cross terms cancel except one:
$$
\mathcal{C}_{\mathrm{CHSH}}^2 = 4 - [A_1, A_2]\,[B_1, B_2]
$$
(expand and check: the diagonal terms give $4$ and the off-diagonal terms assemble into the product of commutators). Then $\|[A_1,A_2]\|\le2$ and similarly for $B$, so $\|\mathcal C_{\mathrm{CHSH}}\|\le2\sqrt2$.

For general self-adjoint contractions, write
$$
\mathcal C_{\mathrm{CHSH}}
{}={}
\begin{bmatrix}A_1&A_2\end{bmatrix}
\begin{bmatrix}B_1+B_2\\ B_1-B_2\end{bmatrix}.
$$
The row norm is at most $\sqrt{\|A_1^2+A_2^2\|}\le\sqrt2$, while the squared column norm is
$$
\left\|(B_1+B_2)^2+(B_1-B_2)^2\right\|
=2\|B_1^2+B_2^2\|\le4.
$$
Therefore $\|\mathcal C_{\mathrm{CHSH}}\|\le2\sqrt2$, and every state expectation obeys the same bound. $\square$

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

For complementary QFT wedges, Summers–Werner prove a much stronger genericity statement about the **supremum over local observables**. Positive spacelike separation changes the problem: maximal Bell correlation can decay with distance in massive theories, so one must not replace “complementary wedges” by “any two spacelike-separated regions.”

## 2. The Summers–Werner theorem

### 2.1 Bell value for a pair of commuting algebras

For commuting von Neumann algebras $\mathcal M,\mathcal N$ and a state $\omega$, define the raw CHSH Bell value
$$
\beta_{\mathrm{CHSH}}(\omega;\mathcal M,\mathcal N)
:=
\sup\left\{
|\omega(\mathcal C_{\mathrm{CHSH}})|:
A_i\in\mathcal M_{\mathrm{sa}},\
B_j\in\mathcal N_{\mathrm{sa}},\
\|A_i\|,\|B_j\|\le1
\right\}.
$$
The classical bound is $2$ and the universal quantum bound is $2\sqrt2$. Calling the correlations **maximal** means that this supremum equals $2\sqrt2$; it does not automatically mean that one quadruple attains it.

### 2.2 The precise wedge theorem

**Theorem 2.1 (Summers–Werner 1987, generic maximal violation). [Stated only; DOI 10.1007/BF01207366.]** *Under weak technical assumptions on a local net that are satisfied by nets associated with quantum fields obeying the standard axioms, let $W$ and $W'$ be complementary wedges. Then every vector state $\omega_\psi(a)=\langle\psi,a\psi\rangle$ satisfies*
$$
\boxed{
\beta_{\mathrm{CHSH}}\!\left(
\omega_\psi;\mathcal A(W),\mathcal A(W')
\right)=2\sqrt2.
}
$$
*If, in addition, the wedge algebras are injective, the same maximal value holds for every normal state on $\mathcal B(\mathcal H)$ induced by a density matrix.*

The vacuum result for free Bose and Fermi fields was established in the companion *J. Math. Phys.* paper II. The *Comm. Math. Phys.* theorem is stronger: it is generic over vector states and over standard QFT nets, but it remains a statement about **complementary wedge-shaped regions**. The injectivity hypothesis is what licenses the all-normal-density-matrix-state extension.

### 2.3 What the theorem does not say

- It does not say that every pair of spacelike-separated bounded regions is maximally correlated. In massive theories the maximal Bell correlation can decay with positive separation.
- It does not follow from “both algebras are type III$_1$” alone. Their relative position in the net, wedge complementarity, and the theorem's technical assumptions matter.
- It does not identify a particular simple observable family that reaches the supremum.
- It does not imply that a fixed UV-regulated vacuum has maximal Bell value. It only leaves open the usual type-I possibility of choosing another state and observables that attain $2\sqrt2$.

### 2.4 Contrast with finite-dimensional quantum mechanics

| Setting | Fixed state | Maximum over admissible local observables |
|---|---|---|
| Two-qubit singlet | maximally entangled pure state | $2\sqrt2$ |
| Generic two-qubit mixed state | state-dependent | often $\le2$, sometimes between $2$ and $2\sqrt2$ |
| Type-I bipartite system, optimized also over states | choose a Bell pair in a two-qubit sector | $2\sqrt2$ |
| Complementary QFT wedges, vector state under Summers–Werner hypotheses | **every** vector state | $2\sqrt2$ as a supremum |
| Complementary injective wedge algebras | every ambient normal density-matrix state | $2\sqrt2$ as a supremum |

The remarkable QFT statement is therefore genericity for a fixed geometric pair of algebras—not a larger universal quantum bound and not a prohibition on type-I saturation.

## 3. What physical intuition survives?

Three exact statements should remain separate:

1. Reeh–Schlieder supplies strong vector-density properties for the vacuum.
2. Bisognano–Wichmann makes the vacuum a KMS state for wedge boosts at inverse rapidity temperature $2\pi$.
3. Summers–Werner fixes the Bell supremum for complementary wedges under its own hypotheses.

A regulator can make the formal expression $\rho_R\propto e^{-2\pi K_R}$ meaningful in a type-I approximation, and short-distance correlations across the common wedge horizon then provide useful intuition. But the Unruh temperature is finite, not “infinite temperature,” and a regulator limit plus divergent entropy is not a proof of either type III$_1$ or Bell maximality. Positive separation also matters: once a collar separates the regions, clustering can suppress Bell correlations. The picture of an inexhaustible hierarchy of correlations near a shared boundary is helpful; the theorem, not the picture, establishes the supremum.

## 4. Explicit calculations: what can be obtained from chosen fields

The theorem fixes a supremum over **all** admissible local contractions. A calculation with a selected family asks a different question: how large a violation can *these* observables produce? Keeping the two levels separate prevents an existence theorem from being mistaken for an optimization result.

### 4.1 Local Weyl-cosine contractions

Let $f\in C_c^\infty(W_R;\mathbb R)$ and $g\in C_c^\infty(W_L;\mathbb R)$. The Weyl operator $W(\alpha f)=e^{i\alpha\phi(f)}$ is unitary, and its Hermitian part
$$
A(f,\alpha):=\frac{W(\alpha f)+W(\alpha f)^*}{2}
=\cos\!\big(\alpha\phi(f)\big)
$$
is a self-adjoint contraction in $\mathcal A(W_R)$. Define $B(g,\beta)$ analogously in $\mathcal A(W_L)$. Locality gives $[A(f,\alpha),B(g,\beta)]=0$.

These observables are **not dichotomic in the strict sense**: generally $A(f,\alpha)^2\ne1$. That causes no problem for CHSH, because the definition uses self-adjoint contractions. If a construction requires outcomes exactly $\pm1$, one must instead use self-adjoint unitaries, for example suitable spectral signs, or another explicitly bounded Hermitian construction.

There is an infrared point peculiar to the massless scalar in $1+1$ dimensions. The unsmeared scalar vacuum does not define a positive Wightman field on arbitrary test functions. One may work with the derivative field, impose the infrared-safe condition $\int f=0$, or retain a mass/zero-mode regulator until the end. The formulas below assume one of these choices.

### 4.2 Mostly-plus Wightman prescription and the exact Gaussian formula

With $\eta=\operatorname{diag}(-1,+1)$, a convenient representative of the massless two-point distribution is
$$
W_2(x-y)
=-\frac{1}{4\pi}
\log\!\left[
\mu_{\mathrm{IR}}^2
\left(-\big(x^0-y^0-i0\big)^2+\big(x^1-y^1\big)^2\right)
\right],
$$
up to the familiar additive infrared constant. That constant drops out for zero-integral smearings. The $-i0$ belongs to the **time difference inside the square**; writing an undirected $i\epsilon$ beside $(x-y)^2$ hides the positive-frequency prescription.

Write
$$
C(f,g):=\operatorname{Re}\langle0|\phi(f)\phi(g)|0\rangle .
$$
For the quasifree vacuum,
$$
\langle0|W(h)|0\rangle=e^{-C(h,h)/2}.
$$
If $f$ and $g$ are spacelike separated, their symplectic pairing vanishes. Expanding the two cosines then gives the exact identity
$$
\begin{aligned}
&\langle0|\cos(\alpha\phi(f))\cos(\beta\phi(g))|0\rangle\\
&\quad=\frac12\!\left[
e^{-\frac12 C(\alpha f+\beta g,\alpha f+\beta g)}
+e^{-\frac12 C(\alpha f-\beta g,\alpha f-\beta g)}
\right]\\
&\quad=e^{-\frac12[\alpha^2C(f,f)+\beta^2C(g,g)]}
\cosh\!\big(\alpha\beta C(f,g)\big).
\end{aligned}
$$
This is an **exact model calculation**, not yet a Bell-violation result.

### 4.3 From four covariances to one CHSH value

Choose $f_1,f_2\in C_c^\infty(W_R;\mathbb R)$ and $g_1,g_2\in C_c^\infty(W_L;\mathbb R)$, with the infrared qualification above, and set
$$
A_i=\cos(\alpha_i\phi(f_i)),
\qquad
B_j=\cos(\beta_j\phi(g_j)).
$$
The four terms in $\langle\mathcal C_{\mathrm{CHSH}}\rangle$ are obtained from the preceding formula. Thus a concrete calculation needs the covariance matrix
$$
C(f_i,f_k),\qquad C(g_j,g_\ell),\qquad C(f_i,g_j),
$$
together with the amplitudes. The formula reduces the problem to finite-dimensional optimization once these smeared distributions are known.

What it does **not** prove is that the cosine family reaches $2\sqrt2$. The Summers–Werner supremum ranges over the whole unit ball of each wedge algebra. A convenient subfamily may violate CHSH and still have a strictly smaller supremum.

### 4.4 A boost does not move a fixed packet to the bifurcation point

Right-wedge Rindler coordinates are
$$
x^0=\xi\sinh\eta,
\qquad
x^1=\xi\cosh\eta,
\qquad \xi>0.
$$
A Lorentz boost shifts $\eta$ and leaves $\xi$ fixed. Consequently, a fixed compact packet does **not** approach $(x^0,x^1)=(0,0)$ under a large boost; its center runs toward null infinity. The same point follows from vacuum invariance: if all four observables are transformed by the same global boost, their CHSH expectation is unchanged.

To probe shorter distances from the common wedge edge, one needs a new localization sequence—for example supports with radial scale $\xi_n\to0$—not merely the modular orbit of one packet. The structural theorem guarantees the Bell supremum under its hypotheses, but does not identify that supremum with a particular boost orbit or with “infinitely thin wavelets at the bifurcation surface.”

> **Physical picture, explicitly heuristic.** Short-distance correlations across a common boundary are a useful guide when designing test functions. They should not be turned into literal Bell pairs sitting on the horizon: a type-III local algebra has no canonical tensor-product decomposition into such pairs. The picture motivates a scaling search; the algebraic theorem supplies the conclusion.

### 4.5 A source-checked numerical benchmark

The 2024 scalar-field paper arXiv:2406.20033 used Gaussian functions and a Weyl-unitary Bell expression, with the classical normalization $2$. Gaussians are not compactly supported. The authors therefore tested locality numerically through the smeared Pauli–Jordan function and retained configurations below a threshold of $10^{-10}$. The resulting locality is numerical/approximate, not the exact support statement used in the Haag–Kastler theorem.

The largest reported values in Table 1 are:

| mass parameter $m$ | reported Bell value |
|---:|---:|
| $1.5$ | $2.00148$ |
| $1$ | $2.00722$ |
| $0.1$ | $2.06382$ |
| $0.01$ | $2.10044$ |
| $0.001$ | $2.12661$ |
| $0.0001$ | $2.13046$ |

These numbers establish violations for the sampled configurations. They are numerical lower bounds on the optimized value of that chosen ansatz, not evidence that the ansatz reaches $2\sqrt2$. Their mass dependence is physically consistent with clustering for the effectively separated packets.

The 2025 paper arXiv:2506.00504 instead constructs bounded Hermitian operators from Weyl operators and studies tangent diamonds in $1+1$ dimensions. Its analytic modular construction and its numerical test-function construction must also be distinguished: the paper reports, for one displayed numerical bounded-Hermitian family, a value $2.752$, while using a very small mass as an infrared regulator.

## 5. Where the structural theorem does its work

**Proof status: stated, not reproduced.** The Summers–Werner argument is a substantial operator-algebraic theorem. It should not be replaced by a three-line appeal to “type III$_1$ plus full modular spectrum.” In particular:

- Reeh–Schlieder gives cyclicity and, with locality for a complementary region, separatingness. It does not itself manufacture CHSH observables.
- Bisognano–Wichmann identifies wedge modular flow geometrically. The Bell theorem is not a formal corollary of $\Delta=e^{-2\pi K}$.
- Type III$_1$ is compatible with the required abundance of local operators, but the abstract type of two commuting factors does not determine their relative position or their Bell correlations.
- A statement about the spectrum of one modular operator is not a license to posit ordinary projections satisfying $\sigma_t(P)=e^{i\lambda t}P$; that equation would usually be incompatible with $P=P^2$ unless the phase is trivial.

The reliable roadmap is therefore:

1. formulate the Bell coefficient for the concrete commuting pair of wedge algebras;
2. use the locality, covariance, spectrum, and nontriviality assumptions appearing in the original papers;
3. obtain maximal correlation for complementary wedges, first in the free-field vacuum analysis and then in the generic vector-state theorem;
4. add injectivity when extending the conclusion to all normal states induced by density matrices on $\mathcal B(\mathcal H)$.

This roadmap explains the role of the ingredients without simulating a proof. It also explains why neither an arbitrary pair of type-III$_1$ factors nor an arbitrary pair of separated double cones inherits the conclusion automatically.

## 6. Connection to the research program

The recent papers have different fields, observable classes, and proof status. They should be read one by one rather than blended into a single “wavelet construction.”

- **arXiv:2307.04611 / PRD 108, L081701.** Free massless spinor field in $1+1$ dimensions. A finite Haar-wavelet optimization is bumpified with a Planck-taper window to obtain smooth compactly supported test functions to arbitrary precision. The reported violations can be made arbitrarily close to the maximal value within that construction.
- **arXiv:2309.02941 / PRD 108, 085026.** Free real scalar field. The paper combines Tomita–Takesaki theory with direct correlators of Weyl operators to establish violations.
- **arXiv:2406.20033 / PRD 110, 065006.** Massive scalar numerical search with Gaussian profiles and an explicit numerical Pauli–Jordan check. The verified Table 1 values are listed in §4.5.
- **arXiv:2506.00504.** Bounded Hermitian operators built from Weyl operators, with analytic modular and numerical analyses for tangent diamonds in $1+1$ dimensions. This is the closest match to the standard self-adjoint-contraction formulation used in §1.

The methodological lesson is useful beyond these examples: specify the field, region, observable class, exact-versus-numerical locality criterion, and optimization domain before quoting a Bell value.

**Open project.** For holographic boundary regions, one would first have to state the commuting algebra pair and the state, and then ask whether an appropriate wedge or tangent-region theorem applies. A failure of one explicit ansatz to saturate would not by itself diagnose bulk topology; that would require an independent theorem relating the optimized Bell coefficient to the bulk structure.

## 7. What to take away

- **Proved in the cited literature:** under the precise Summers–Werner hypotheses, complementary wedge algebras have raw CHSH supremum $2\sqrt2$ in every vector state; injectivity yields the stated extension to ambient normal density-matrix states.
- **Exact calculation:** quasifree Weyl expectations reduce chosen Bell correlators to smeared two-point functions. This does not by itself optimize over the local algebras.
- **Numerical evidence:** finite test-function searches provide lower bounds for specified ansätze and tolerances. They should be reported with their regulator and locality checks.
- **Geometry:** a boost changes Rindler time at fixed Rindler radius. Approaching the common edge requires a scaling/localization sequence, not the boost orbit of a fixed packet.
- **Scope:** type III$_1$, Reeh–Schlieder, and Bisognano–Wichmann illuminate the result, but no one of them alone is the Summers–Werner theorem. Type-I systems can also attain $2\sqrt2$ in suitable states.

## 8. Looking ahead

Week 12 closes Block C by explaining the **type III$_1$ classification** of local algebras under explicit phase-space and scaling hypotheses. We separate the route to injectivity/hyperfiniteness from the route to the Connes type, then discuss what the result does—and does not—imply for density matrices, entropy, Bell correlation, and crossed products.

## 9. Problem set

**Core problems.**

**1. CHSH expectation in finite-dimensional QM (warmup).** For the singlet $|\psi^-\rangle$ on $\mathbb C^2\otimes\mathbb C^2$, first prove
$$
\langle\psi^-|(\vec a\cdot\vec\sigma)\otimes(\vec b\cdot\vec\sigma)|\psi^-\rangle=-\vec a\cdot\vec b.
$$
In the $xz$-plane choose Alice's angles $0,\pi/2$ and Bob's angles $\pi/4,-\pi/4$. For the sign convention of §1, show that the CHSH expectation is $-2\sqrt2$, hence its absolute value is $2\sqrt2$. Then reverse both Bob observables and recover the positive value used in §1.3. **Checkpoint:** the relevant Alice–Bob separations are $\pi/4$ or $3\pi/4$; the four settings are not all mutually separated by $45^\circ$.

**2. Tsirelson bound (proof in finite-dim).** For commuting self-adjoint $A_i \in \mathcal{B}(\mathcal{H}_A)$, $B_j \in \mathcal{B}(\mathcal{H}_B)$ with $A_i^2 = B_j^2 = 1$ (dichotomic), prove the operator identity
$$
\mathcal{C}_{\mathrm{CHSH}}^2 = 4 - [A_1, A_2]\,[B_1, B_2],
$$
hence $\|\mathcal{C}_{\mathrm{CHSH}}\| \le \sqrt{4 + \|[A_1, A_2]\|\,\|[B_1, B_2]\|} \le 2\sqrt 2$. Then reproduce the row/column norm argument of §1.2 for general self-adjoint contractions. Do not assume that a contraction is a convex combination of two self-adjoint unitaries.

**3. Locality from spacelike $\sigma$.** Let $f_R\in C_c^\infty(W_R;\mathbb R)$ and $g_L\in C_c^\infty(W_L;\mathbb R)$, with the infrared-safe restriction of §4.1 in the massless $1+1$-dimensional model. Verify directly that $[\cos(\alpha\phi(f_R)),\cos(\beta\phi(g_L))]=0$. Use the Weyl relation and the spacelike vanishing of $\sigma(f_R,g_L)$.

**4. A reproducible cosine-Weyl calculation.** Suppose two spacelike-separated, infrared-safe smearing functions have normalized covariance
$$
C(f,f)=C(g,g)=1,
\qquad C(f,g)=c,
\qquad |c|<1.
$$
Use §4.2 to compute
$$
\langle0|\cos(\alpha\phi(f))\cos(\alpha\phi(g))|0\rangle
$$
and verify the limits $\alpha\to0$ and $\alpha\to\infty$. Explain exactly where the strict inequality $|c|<1$ is used. **Extension:** choose compact zero-integral bumps, evaluate the three covariances numerically, and compare with the normalized model.

**5. Read one group paper.** Pick one paper in §6. Record: the field, spacetime dimension, region pair, observable class, state, optimization variables, exact or numerical locality test, and largest reported Bell value. End with two sentences separating what the paper proves from what its displayed ansatz demonstrates.

**6. Real versus imaginary part of $W_2(f,g)$.** For compact, infrared-safe $f$ and $g$ with spacelike-separated supports, show that $\operatorname{Im}W_2(f,g)=\sigma(f,g)/2=0$, while $\operatorname{Re}W_2(f,g)$ need not vanish. Explain why locality constrains the commutator, not the symmetric vacuum correlation.

**Starred problems.**

**7\*. Audit the proposed boost limit.** Starting from $x^0=\xi\sinh\eta$, $x^1=\xi\cosh\eta$, prove that a boost preserves $\xi$ and carries a fixed center toward null infinity as $|\eta|\to\infty$. Next use $U(\Lambda(s))|0\rangle=|0\rangle$ to show that applying the **same** boost to all four observables leaves the vacuum CHSH value unchanged. Finally propose a genuine scaling sequence with $\xi_n\to0$, and list the covariance estimates one would still need before claiming convergence to $2\sqrt2$.

**8\*. Mass and theorem scope.** For the free massive scalar, use Bisognano–Wichmann to explain why the wedge modular action remains geometric. Separately use the large-spacelike-distance asymptotics of the Bessel function in the two-point function to show why a fixed, positively separated packet ansatz has mass-suppressed correlations. Explain why the first statement concerns the full wedge algebra while the second concerns one restricted observable family; neither provides a universal “rate of approach” to the Summers–Werner supremum.

**9\*. Joint boosts and modular notation.** Let $\alpha_s=\operatorname{Ad}U(\Lambda(s))$. Show algebraically that
$$
\alpha_s(\mathcal C[A_1,A_2;B_1,B_2])
=\mathcal C[\alpha_s(A_1),\alpha_s(A_2);\alpha_s(B_1),\alpha_s(B_2)].
$$
Use boost invariance of the vacuum to prove equality of the two expectations. Finally translate $s=2\pi t$ into the course convention $\sigma_t^{W_R}=\operatorname{Ad}\Delta_{W_R}^{-it}$. **Checkpoint:** this is a common global boost of both wedge algebras, not an independently chosen opposite boost on each side.

**10\*. What a type-I regulator does and does not imply.** Consider $M_2(\mathbb C)\otimes M_2(\mathbb C)$. Show that the Bell state and observables of Problem 1 attain $2\sqrt2$, whereas the maximally mixed state gives zero for all traceless Pauli choices and cannot violate CHSH. Conclude that type I does not force a strict gap below Tsirelson; the value depends on the state and observable pair. Then explain why a finite-mode cutoff of a continuum field does not, by itself, supply strictly local tensor factors or a universal formula depending only on $L\Lambda$.

**Project problems.**

**11. Bell–CHSH in a holographic setting.** Read the [[sem2-week-08-bell-chsh-on-tfd|Semester II Week 8 project brief]]. Specify a boundary state and a pair of commuting boundary algebras before choosing observables. State whether the regions are complementary, tangent, or positively separated. Design one computable lower bound using a restricted observable family, and list the extra argument needed before interpreting non-saturation as a statement about the bulk.

**12. Reproduce a documented numerical benchmark.** Reproduce one row of Table 1 of arXiv:2406.20033 or the displayed bounded-Hermitian value in arXiv:2506.00504. Record integration tolerances, the Pauli–Jordan residual, parameter-search range, and random seed where applicable. Report the result as a reproducible numerical lower bound for the stated ansatz, not as a proof of the structural supremum.

## Self-study answer checkpoints

These checkpoints cover the core problems. Starred, project, and explicitly research-level problems remain source-led; they should be completed with the references and hypotheses named in the problem.

1. The four correlations are $-\cos(\theta_A-\theta_B)$. For the stated angles they are $-1/\sqrt2,-1/\sqrt2,-1/\sqrt2,+1/\sqrt2$, so
   $$
   \langle\mathcal C_{\mathrm{CHSH}}\rangle=-2\sqrt2.
   $$
   Reversing both Bob observables changes the overall sign and gives $+2\sqrt2$.
2. Expansion using $[A_i,B_j]=0$ gives
   $$
   \mathcal C_{\mathrm{CHSH}}^2=4-[A_1,A_2][B_1,B_2].
   $$
   Since each commutator has norm at most $2$, $\|\mathcal C_{\mathrm{CHSH}}\|\le2\sqrt2$. For general contractions, the row norm is at most $\sqrt2$ and the column norm at most $2$, giving the same bound without a dichotomic decomposition.
3. Spacelike separation gives $\sigma(f_R,g_L)=0$, hence every $W(\pm\alpha f_R)$ commutes with every $W(\pm\beta g_L)$. The two cosines are linear combinations of these Weyl operators, so their commutator vanishes.
4. The exact normalized correlator is
   $$
   \langle\cos(\alpha\phi(f))\cos(\alpha\phi(g))\rangle
   =e^{-\alpha^2}\cosh(c\alpha^2)
   =\frac12\!\left[e^{-(1-c)\alpha^2}+e^{-(1+c)\alpha^2}\right].
   $$
   It tends to $1$ as $\alpha\to0$ and to $0$ as $\alpha\to\infty$. The strict condition $|c|<1$ makes both decay exponents positive; at $|c|=1$ one term would not decay.
5. There is no paper-independent numerical answer. A satisfactory record must reproduce the field, dimension, algebra pair, state, observable ansatz, optimization domain, locality test, and quoted value from the chosen source. Its concluding distinction should read: the structural statement concerns the supremum over the full local unit balls, whereas the displayed construction establishes only what its specified ansatz and optimization actually attain.
6. For real smearings,
   $$
   W_2(f,g)-W_2(g,f)=2i\operatorname{Im}W_2(f,g)=i\sigma(f,g).
   $$
   Thus spacelike separation forces $\operatorname{Im}W_2(f,g)=0$, while the symmetric covariance $\operatorname{Re}W_2(f,g)$ may remain nonzero. Locality removes the commutator, not the vacuum correlation.

**Wiki connections.** [[bell-chsh-in-holographic-setting|Bell–CHSH in holographic settings]] (open question)

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block C. Last revised 2026-08-24.*
