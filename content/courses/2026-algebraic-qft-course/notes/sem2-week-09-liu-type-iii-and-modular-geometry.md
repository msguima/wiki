---
title: "Sem II Week 9 — Liu Lectures I: Type III at Large N and Modular Flow as Geometry"
type: lecture-notes
course: syllabus
semester: 2
week: 9
block: 3
duration: 4 hours (seminar with student presentations)
prerequisites: Sem II Wks 1–8 (Witten 2022, CPW); Sem I Wks 10, 12, 13 (Bisognano–Wichmann, type III$_1$, crossed product)
target_paper: "Hong Liu, Lectures on entanglement, von Neumann algebras, and emergence of spacetime, arXiv:2510.07017"
modified: 2026-08-23
---

# Sem II Week 9 — Liu Lectures I: Type III at Large $N$ and Modular Flow as Geometry

> *Blocks 1–2 gave us two worked examples of the same machine: Witten 2022 (single-sided) and CPW (two-sided). Both identified a holographic boundary algebra as type III$_1$, then dressed its modular flow by a crossed product. Block 3 steps back and reads Hong Liu's lecture notes (arXiv:2510.07017), the cleanest modern synthesis of the whole program. This week covers two structural pillars: (i) **why type III appears at large $N$** — not as a technical accident but as the algebraic translation of "energy unbounded above, no local trace"; and (ii) the **modular-flow-equals-bulk-geometric-flow dictionary**, of which Bisognano–Wichmann (Sem I Wk 10) and the ADM/boost identifications (Blocks 1–2) are special cases. The Casini–Huerta–Myers ball modular Hamiltonian is the concrete touchstone we carry into Block 4.*

## 0. Reading

**Primary:**
- Hong Liu, "Lectures on entanglement, von Neumann algebras, and emergence of spacetime," **arXiv:2510.07017**, §1 (introduction/motivation), §3 (type III at large $N$), §4 (modular flow ↔ bulk geometric flow).

**Secondary / gentler:**
- Sem I Wk 10 (Bisognano–Wichmann) and Wk 12 (type III$_1$ classification) — the free-field/axiomatic versions of what Liu does holographically.
- Witten, "Notes on some entanglement properties of QFT," arXiv:1803.04993, §§4–5.

**Optional research reading:**
- Casini, Huerta, Myers, "Towards a derivation of holographic entanglement entropy," *JHEP* 05 (2011) 036, arXiv:1102.0440 (the ball modular Hamiltonian).
- Leutheusser, Liu, "Causal connectability between quantum systems and the black hole interior in large-$N$ gauge theories," arXiv:2110.05497; "Emergent times in holographic duality," arXiv:2112.12156 (the original large-$N$ type-III analysis).
- Hislop, Longo, "Modular structure of the local algebras associated with the free massless scalar field theory," *Comm. Math. Phys.* 84 (1982) 71.

## 1. Why a "lectures" block

Two weeks on a pedagogical review, in the middle of a research-paper course, deserves a justification.

Liu's lectures do three things no single research paper does:

1. **They unify.** Witten 2022 (Block 1), CPW (Block 2), and AAJ (Block 4) look like three different constructions. Liu shows they are one construction — the modular crossed product — applied to three geometries. The organizing diagram of Week 10 is worth the price of admission.

2. **They make the large-$N$ → type III logic explicit.** Blocks 1–2 *asserted* that the boundary single-trace algebra is type III$_1$ (Block 1 Theorem 4.1, hypothesis-explicit). Liu §3 explains *why*, structurally, and connects it to the Leutheusser–Liu emergence-of-time program.

3. **They install the dictionary.** "Modular flow = bulk geometric flow" is the single most useful slogan in the field. Liu §4 states it precisely and gives the Casini–Huerta–Myers ball example as the canonical instance.

This block is therefore **consolidation, not new content**. Students who have done Blocks 1–2 should find Liu mostly familiar — the value is in the synthesis. The seminar format (students present §3 and §4) is appropriate.

## 2. Type III at large $N$: the structural story

### 2.1 The three faces of type III

Recall from Sem I (Wks 3, 12) that a type III factor is characterized by any of the following equivalent conditions:

- **No trace.** There is no faithful normal semifinite trace.
- **All projections infinite.** Every nonzero projection is Murray–von Neumann equivalent to a proper subprojection of itself.
- **No density matrices.** No normal state is of the form $\omega(a) = \mathrm{Tr}(\rho a)$.

Liu §3 adds a fourth, physics-facing face, which is the one that explains *why QFT lands here*:

- **Modular spectrum is all of $\mathbb{R}$ (for III$_1$).** The generator $K = -\log\Delta$ of the modular flow has continuous, unbounded, two-sided spectrum on every cyclic-separating state.

> **Physical picture.** Type III is the operator-algebraic signature of *unbounded energy with no ground state inside the region*. A type-I algebra has a trace because it has minimal projections — "atoms," smallest yes/no questions — and you can count them. A local region of a relativistic QFT has no smallest excitation: the vacuum entangles modes at every scale across the entangling surface, so there is always a finer excitation localized nearer the boundary. "No minimal projection" *is* "no shortest-wavelength mode," and "no trace" *is* "the entanglement entropy across the boundary diverges." The same physics that makes the area law divergent (Sem I Wk 12) makes the algebra type III. This is not a pathology to regulate away; it is the structural fingerprint of a continuum field theory with a sharp boundary.

### 2.2 How large $N$ produces it

At finite $N$, a holographic CFT on a compact spatial slice has a discrete energy spectrum and a finite-dimensional (or at least trace-class) algebra — type I. The boundary single-trace algebra has a density matrix; everything is conventional quantum mechanics.

The large-$N$ limit changes the type. Liu §3 (following Leutheusser–Liu) frames it as follows:

**Theorem 2.1 (Type III emergence at large $N$). [Stated only — hypothesis-explicit; refs: Liu §3; Leutheusser–Liu arXiv:2110.05497, 2112.12156.]** *In a holographic CFT with a large-$N$ limit in which single-trace operators become generalized free fields (Block 1 §3), the boundary single-trace algebra associated with a time band (or a Rindler-like boundary region) of the eternal black hole is, at $N = \infty$, a type III$_1$ von Neumann factor. At finite $N$ the algebra is type I.*

The mechanism, structurally:

1. At $N = \infty$, single-trace correlators factorize (Block 1 Theorem 3.2): the algebra is a **generalized free field** with a fixed two-point function.
2. The relevant boundary region (one side of the eternal BH, or a time band) sees the GFF modes with a **thermal, continuous** spectrum — the boundary two-point function in the BTZ/TFD state is the thermal correlator (Block 1 §6).
3. The modular flow of this thermal GFF state has continuous unbounded spectrum (the ADM/boost generator), so the algebra is III$_1$ (Sem I Wk 12 mechanism).

Step 3 is the one worth doing rather than asserting, because it is where the type is actually decided. The next subsection carries it out in the controlled case where the modes are discrete, which is enough to exhibit the whole mechanism.

### 2.3 Model proof: how the mode spectrum fixes the type

A thermal generalized free field is an infinite collection of independent thermal oscillators. Restricted to one side, its algebra is an **infinite tensor product of type I factors in a product state** — an Araki–Woods (ITPFI) factor — and for these the type is completely determined by the frequencies. We compute it.

**Setup.** Take one mode of frequency $\omega$ at inverse temperature $\beta$, and truncate it to its lowest two levels, so the one-mode algebra is $M_2(\mathbb{C})$ in the Gibbs state
$$
\phi_\lambda = \frac{1}{1+\lambda}\begin{pmatrix}1 & 0\\ 0 & \lambda\end{pmatrix}, \qquad \lambda := e^{-\beta\omega} \in (0,1).
$$
The full one-sided algebra of a GFF with mode frequencies $\{\omega_k\}$ is then modelled by the infinite tensor product
$$
\mathcal{M} = \bigotimes_{k}\big(M_2(\mathbb{C}),\, \phi_{\lambda_k}\big), \qquad \lambda_k = e^{-\beta\omega_k},
$$
built in the GNS representation of the product state $\phi = \bigotimes_k \phi_{\lambda_k}$. Note that the two-level truncation is a genuine restriction on the model and not on the argument: the harmonic-oscillator Gibbs state has eigenvalue ratios $e^{-\beta\omega n}$, which generate the same multiplicative group as $\lambda = e^{-\beta\omega}$, so the spectrum computed below is unchanged.

**The modular spectrum of one factor.** For a finite-dimensional algebra in a faithful state with density $\rho$, the modular operator on $\mathcal{H} = M_2 \cong \mathbb{C}^2\otimes\mathbb{C}^2$ is $\Delta = \rho\otimes\rho^{-1}$ (Sem I Wk 5 §3), so its eigenvalues are the **ratios** of the eigenvalues of $\rho$. With $\rho$ having eigenvalues proportional to $1$ and $\lambda$,
$$
\mathrm{spec}\,\Delta_{\phi_\lambda} = \{\lambda^{-1},\, 1,\, 1,\, \lambda\}.
$$
The state's overall normalization drops out, which is why only the ratio $\lambda$ matters.

**The modular spectrum of the product.** Modular operators of a tensor product in a product state multiply, $\Delta_\phi = \bigotimes_k \Delta_{\phi_{\lambda_k}}$, so the spectrum of $\Delta_\phi$ is the closure of the set of finite products of the individual eigenvalues:
$$
\mathrm{spec}\,\Delta_\phi = \overline{\Big\{\textstyle\prod_k \lambda_k^{n_k} \;:\; n_k\in\mathbb{Z},\ \text{finitely many nonzero}\Big\}}.
$$
This closure is a closed multiplicative subgroup of $\mathbb{R}_{>0}$, and Connes' invariant $S(\mathcal{M})$ — the intersection of the modular spectra over all faithful normal states — is exactly this group together with $0$. Closed subgroups of $\mathbb{R}_{>0}$ come in only three kinds, and they are precisely the three type III cases.

**Case (i) — all frequencies equal, $\omega_k \equiv \omega_0$.** Every $\lambda_k = \lambda = e^{-\beta\omega_0}$, the generated group is $\lambda^{\mathbb{Z}}$, which is discrete, and
$$
S(\mathcal{M}) = \{0\}\cup\lambda^{\mathbb{Z}} \quad\Longrightarrow\quad \mathcal{M} \ \text{is type III}_\lambda .
$$
This is the Powers factor $R_\lambda$ of Sem I Wk 3 — the standard example of a type III$_\lambda$ factor, here obtained as the thermal algebra of infinitely many copies of one oscillator.

**Case (ii) — two incommensurate frequencies.** Suppose the spectrum contains $\omega_1$ and $\omega_2$ with $\omega_1/\omega_2$ irrational. The generated group contains $e^{-\beta(n_1\omega_1 + n_2\omega_2)}$ for all integers $n_1, n_2$, and by Weyl's equidistribution theorem $\{n_1\omega_1 + n_2\omega_2\}$ is dense in $\mathbb{R}$. Thus the group is dense, its closure is all of $\mathbb{R}_{>0}$, and
$$
S(\mathcal{M}) = [0,\infty) \quad\Longrightarrow\quad \mathcal{M}\ \text{is type III}_1 .
$$

**Case (iii) — a continuum of frequencies.** A fortiori dense, so type III$_1$. This is the GFF case: at $N=\infty$ the single-trace two-point function has a continuous spectral density, the mode frequencies fill an interval, and the algebra is III$_1$. $\square$ **[Model proof — two-level truncation of a discrete mode set; the continuum statement is the $N=\infty$ GFF case, refs: Araki–Woods 1968; Liu §3.]**

Note what decided the answer: not the size of the algebra, but whether the set of Boltzmann ratios $\{e^{-\beta\omega_k}\}$ generates a discrete or a dense subgroup of $\mathbb{R}_{>0}$. Finite $N$ on a compact slice gives a discrete spectrum with a gap and only finitely many modes below any energy, which is the type I case; the large-$N$ limit fills in the continuum, and the type jumps to III$_1$.

> **Physical picture.** The computation says the type is a statement about *level spacings*, not about dimensions. A finite-$N$ CFT on a sphere has energies spaced by $O(1)$, so its thermal state has a discrete, gapped set of Boltzmann weights — countably many "atoms" the trace can count. Taking $N\to\infty$ collapses the spacing to zero: the single-trace spectrum becomes continuous, the Boltzmann ratios fill $\mathbb{R}_{>0}$, and there is no scale at which the counting can start. In the bulk this is the statement that the horizon has a continuous absorption spectrum — a quasinormal-mode continuum rather than a discrete line spectrum — which is exactly what distinguishes a genuine black hole from a very hot star. Type III$_1$ is the algebra's way of recording that the horizon absorbs at every frequency.

### 2.4 Why this matters downstream

The type III$_1$ structure is what makes the crossed product non-trivial (Sem I Wk 13: dressing an *outer* flow promotes the type; dressing an inner flow does not). If the boundary algebra were type I, the whole Witten/CPW/AAJ program would collapse to ordinary density-matrix quantum mechanics. The interest of the program is precisely that classical-gravity boundary algebras are type III$_1$, so the gravitational entropy must be *manufactured* by the crossed product rather than read off a density matrix.

## 3. Modular flow as bulk geometric flow

### 3.1 The dictionary

The central content of Liu §4 is a dictionary entry that Blocks 1–2 used in special cases:

**The modular-flow/geometric-flow dictionary (Liu §4). [Hypothesis-explicit; refs: Liu §4; CHM arXiv:1102.0440; Hislop–Longo 1982.]** *For a boundary subregion $\mathcal{O}$ whose bulk causal/entanglement wedge $W_\mathcal{O}$ admits a Killing vector $\zeta$ fixing the RT surface and generating a flow that preserves $W_\mathcal{O}$, the boundary modular flow $\sigma_t^{\mathcal{O}}$ of the vacuum (or the relevant cyclic-separating state) is implemented in the bulk by the geometric flow along $\zeta$.*

Instances we have already met:

| Setting | Boundary region | Bulk Killing flow $\zeta$ | Reference |
|---|---|---|---|
| Free QFT, Rindler wedge | half-space | Lorentz boost | Bisognano–Wichmann, Sem I Wk 10 |
| Eternal BH, one boundary | full boundary | horizon boost ($\partial_t$) | CPW, Sem II Wk 5 |
| CFT vacuum, ball | ball of radius $R$ | conformal Killing vector | Casini–Huerta–Myers, this week |

> **Physical picture.** The dictionary says the *intrinsic thermal time* of a region (its modular flow, defined purely from the state and the algebra — Sem I Wk 6) coincides with a *geometric symmetry* of the dual bulk. This is remarkable: the modular flow is defined with no reference to dynamics, geometry, or a Hamiltonian, yet it turns out to move points around in the bulk along a Killing orbit. The slogan "modular flow = bulk geometric flow" is the dynamical core of holography — kinematics on the boundary (Tomita–Takesaki) is geometry in the bulk. It is exact only when the wedge has the requisite Killing symmetry (Rindler, ball-in-vacuum, eternal BH); for a generic region the modular flow exists but acts non-geometrically (non-locally) — a fact we flag carefully, because the whole subject's tractability rests on choosing geometrically nice regions.

### 3.2 Generalizing Bisognano–Wichmann

Bisognano–Wichmann (Sem I Wk 10) is the dictionary's free-field, flat-space instance: the modular flow of the Rindler wedge is the boost, with modular Hamiltonian $K = 2\pi K_{\rm boost}$ and the famous $2\pi$ (Unruh temperature). Liu's dictionary is the holographic generalization:

- **B–W (flat space):** modular flow on $\mathcal{A}(W_R)$ = boost. Proven from Wightman axioms.
- **Liu (holographic):** modular flow on a boundary subregion = bulk Killing flow on the dual wedge. Established under the large-$N$ + geometric-symmetry hypotheses, using the bulk equations of motion.

The conceptual content is identical: a thermal-looking restricted vacuum, whose modular flow is a spacetime symmetry fixing the entangling surface. The difference is that B–W is a theorem about a fixed QFT, while Liu's version is a statement about the bulk dual of a large-$N$ boundary theory.

## 4. The Casini–Huerta–Myers ball modular Hamiltonian

The concrete worked example of the dictionary, and the one we carry into Block 4.

### 4.1 The statement

**Theorem 4.1 (Casini–Huerta–Myers). [Proved below in $d=2$ from Bisognano–Wichmann plus conformal invariance; general $d$ by the same argument — refs: CHM arXiv:1102.0440; Hislop–Longo 1982.]** *Let $\mathcal{O} = B_R$ be a ball of radius $R$ at fixed time in the vacuum of a CFT$_d$ on Minkowski space. The vacuum modular Hamiltonian of $\mathcal{A}(B_R)$ is local, given by an integral of the energy density weighted by a parabolic profile:*
$$
K_{B_R} = 2\pi \int_{B_R} \frac{R^2 - r^2}{2R}\, T_{00}(\vec x)\, d^{d-1}x,
$$
*where $r = |\vec x|$ and $T_{00}$ is the energy density. The modular flow $\sigma^{B_R}_t$ generated by $K_{B_R}$ is a one-parameter group of conformal transformations preserving $B_R$ (the conformal boost fixing the boundary sphere $\partial B_R$).*

The profile $(R^2 - r^2)/(2R)$ vanishes on $\partial B_R$ (the entangling surface) and is maximal at the center — the modular flow slows to a stop at the boundary and runs fastest at the center, exactly as a conformal boost does.

The proof is short and it is worth doing, because it shows that CHM carries no independent content: it is Bisognano–Wichmann transported by a conformal map. Everything hinges on the fact that the causal diamond of a ball and the Rindler wedge are conformally equivalent, and that a CFT vacuum does not notice the difference.

### 4.2 The conformal map from wedge to diamond

We work in $d = 2$, where the map is a Möbius transformation on each null coordinate and every step can be written down. Use null coordinates $x^\pm = x \pm t$, in which

- the **right Rindler wedge** $W = \{x > |t|\}$ is $\{x^+ > 0,\ x^- > 0\}$,
- the **causal diamond** $D_R$ of the interval $(-R,R)$ at $t = 0$, namely $\{|y| + |t| < R\}$, is $\{-R < y^\pm < R\}$.

In two dimensions any pair of maps $x^+ \mapsto y^+(x^+)$, $x^- \mapsto y^-(x^-)$ is a conformal transformation, so we need one Möbius map carrying $(0,\infty)$ onto $(-R,R)$. Take
$$
y^\pm = R\,\frac{x^\pm - 1}{x^\pm + 1},
\qquad\text{with inverse}\qquad
x^\pm = \frac{R + y^\pm}{R - y^\pm},
$$
which sends $x^\pm = 0 \mapsto y^\pm = -R$ and $x^\pm \to \infty \mapsto y^\pm \to R$, monotonically. Thus it maps $W$ onto $D_R$ and, being a Möbius map on each null line, it is conformal.

Now push the boost forward. The boost of rapidity $\lambda$ acts on null coordinates by $x^\pm \mapsto e^{\pm\lambda}x^\pm$, so its Killing vector is $\zeta_W = x^+\partial_+ - x^-\partial_-$. Differentiating the map,
$$
\frac{dy^\pm}{dx^\pm} = \frac{2R}{(x^\pm+1)^2},
\qquad
\frac{dx^\pm}{d\lambda} = \pm x^\pm,
$$
and using $x^\pm + 1 = 2R/(R - y^\pm)$ from the inverse map, we obtain
$$
\frac{dy^\pm}{d\lambda}
= \pm\,\frac{R + y^\pm}{R - y^\pm}\cdot 2R \cdot \frac{(R-y^\pm)^2}{4R^2}
= \pm\,\frac{R^2 - (y^\pm)^2}{2R}.
$$
So the boost is carried into the vector field
$$
\zeta_D = \frac{R^2 - (y^+)^2}{2R}\,\partial_+ \;-\; \frac{R^2 - (y^-)^2}{2R}\,\partial_- ,
$$
which is the conformal Killing vector of the diamond. Converting with $y^\pm = y \pm t$ and $\partial_\pm = \tfrac12(\partial_y \pm \partial_t)$, and using $(y^+)^2 + (y^-)^2 = 2(y^2+t^2)$ together with $(y^-)^2 - (y^+)^2 = -4yt$, the two null components combine into
$$
\boxed{\;\zeta_D = \frac{1}{2R}\Big[\big(R^2 - t^2 - y^2\big)\,\partial_t \;-\; 2\,y\,t\,\partial_y\Big].\;}
$$
This is exact, not a small-$t$ expansion. Note that $\zeta_D$ vanishes at $y = \pm R$, $t=0$: the endpoints of the interval are fixed points of the flow, which is why the flow maps $D_R$ into itself. On the slice $t = 0$ it reduces to
$$
\zeta_D\big|_{t=0} = \frac{R^2 - y^2}{2R}\,\partial_t ,
$$
purely timelike, with the parabolic profile already visible.

### 4.3 The modular Hamiltonian by pullback

Two inputs finish the argument.

First, Bisognano–Wichmann (Sem I Wk 10, and [[courses/2026-algebraic-qft-course/conventions]]): on the wedge algebra the vacuum modular flow is the boost, at the rate modular time $t$ ↔ rapidity $2\pi t$, with modular Hamiltonian
$$
K_W = 2\pi K_{\rm boost} = 2\pi\int_0^\infty x\,T_{00}(x)\,dx \qquad (d=2).
$$

Second, conformal invariance: the CFT$_2$ vacuum is invariant under the Möbius map of §4.2, and that map carries $\mathcal{A}(W)$ onto $\mathcal{A}(D_R)$. Modular data are determined by the pair (algebra, state), so a transformation preserving the state and mapping one algebra onto the other must carry the modular flow of the first onto the modular flow of the second. The modular flow of $\mathcal{A}(D_R)$ in the vacuum is therefore the flow along $\zeta_D$, at the same rate — modular time $t$ ↔ flow parameter $2\pi t$.

The generator of the $\zeta_D$-flow on the slice $t = 0$ is $\int \zeta_D^t\,T_{00}\,dy$, so
$$
K_{D_R} \;=\; 2\pi \int_{-R}^{R} \frac{R^2 - y^2}{2R}\; T_{00}(y)\,dy ,
$$
which is Theorem 4.1 in $d=2$. $\square$

> **Physical picture.** The derivation explains why CHM looks like a "second" closed-form modular Hamiltonian and is really the first one in disguise. Bisognano–Wichmann is the only modular Hamiltonian we ever compute from scratch; every other closed form in this subject is obtained by moving it with a symmetry. A CFT has enough symmetry to move the wedge onto a diamond, so the diamond inherits a local $K$. A generic region in a generic theory has no symmetry connecting it to a wedge, which is exactly why no closed form exists there — and why the subject keeps returning to wedges, balls, and horizons. The parabolic profile is nothing but the linear Rindler profile $x$ seen through a Möbius map.

### 4.4 General $d$

In $d > 2$ the map is a special conformal transformation rather than a chiral Möbius map, but the structure is identical, and the resulting conformal Killing vector is the direct analogue of the boxed formula above with $y$ replaced by the radius $r = |\vec x|$:
$$
\zeta_D = \frac{1}{2R}\Big[\big(R^2 - t^2 - r^2\big)\,\partial_t - 2\,r\,t\,\partial_r\Big]
= \frac{1}{2R}\big(R^2 P_0 - K_0\big),
$$
where $P_0 = \partial_t$ generates time translations and $K_0$ is the special conformal generator in the time direction. That the two expressions agree is a one-line check: with mostly-plus signature $K_0 = x^2\partial_t - 2x_0(x\cdot\partial) = (t^2+r^2)\partial_t + 2rt\,\partial_r$, so $\tfrac{1}{2R}(R^2\partial_t - K_0)$ is the displayed vector field. Since $\zeta_D$ is a fixed linear combination of conformal generators, it is a conformal Killing vector for any $d$, and the pullback argument of §4.3 goes through verbatim, giving
$$
K_{B_R} = 2\pi\int_{B_R}\frac{R^2-r^2}{2R}\,T_{00}(\vec x)\,d^{d-1}x .
$$

### 4.5 The Rindler limit as a check

The formula must degenerate to Bisognano–Wichmann when the ball grows into a half-space, and it does. Shift the center to $x_0 = R$ and let $R\to\infty$ holding $\xi = R - x_0 + x$ fixed, so that $r = R - \xi$ and
$$
\frac{R^2 - r^2}{2R} = \frac{(R-r)(R+r)}{2R} = \frac{\xi\,(2R - \xi)}{2R} \;\xrightarrow[R\to\infty]{}\; \xi .
$$
The parabolic weight straightens into the linear Rindler weight, and
$$
K_{B_R} \;\longrightarrow\; 2\pi\int_{\xi>0}\xi\,T_{00}(\xi)\,d^{d-1}x = 2\pi K_{\rm boost},
$$
the wedge modular Hamiltonian. This closes the circle: we obtained CHM from Bisognano–Wichmann by a conformal map, and CHM returns it in the limit where the map becomes the identity.

### 4.6 The bulk Killing vector

In pure AdS$_{d+1}$, the boundary ball $B_R$ has a bulk **entanglement wedge** bounded by the RT surface (a hemisphere anchored on $\partial B_R$). There is a bulk Killing vector $\zeta_{\rm bulk}$ that (i) restricts to $\zeta_D$ on the boundary and (ii) fixes the RT surface. The bulk modular flow is the geometric flow along $\zeta_{\rm bulk}$; the boundary modular flow is its restriction. This is the explicit bulk realization of Liu's dictionary, and the picture to keep in mind: *the boundary ball's thermal time is a rigid rotation of its bulk wedge about the RT surface.*

> **Physical picture.** The CHM formula is the closest the subject comes to a *closed-form modular Hamiltonian* outside the wedge case. Two features carry physical weight. First, **locality**: $K_{B_R}$ is an integral of the local energy density, so the vacuum modular flow of a ball is a genuine geometric flow — this is the special feature of the vacuum plus a CFT plus a ball, where the required conformal symmetry exists. For a generic region or state, $K$ is non-local and no such formula exists. Second, the **weight vanishing at the entangling surface** is universal and physical: modular time grinds to a halt at the boundary, which is why the entangling surface is a fixed point of the flow and why the area term in the generalized entropy localizes there. When we perturb the state in Block 4 (the GJW deformation), it is precisely this boundary-anchored structure that shifts, producing the Shapiro-time-advance analog.

## 5. Subregion–subalgebra duality

Liu §4 packages the dictionary into a duality between bulk regions and boundary subalgebras.

**Subregion–subalgebra duality (Liu §4). [Hypothesis-explicit.]** *A boundary subregion $\mathcal{O}$ corresponds to a boundary subalgebra $\mathcal{A}(\mathcal{O})$; the bulk dual is the entanglement wedge $W_\mathcal{O}$, and bulk operators in $W_\mathcal{O}$ are reconstructible from $\mathcal{A}(\mathcal{O})$ (entanglement-wedge reconstruction). Inclusions of regions correspond to inclusions of algebras; causal complements correspond to commutants (when Haag duality holds).*

> **Physical picture.** This is the algebraic skeleton of the Ryu–Takayanagi / entanglement-wedge-reconstruction circle of ideas. "Which bulk region does a boundary observer with access to $\mathcal{A}(\mathcal{O})$ control?" is answered by "the entanglement wedge $W_\mathcal{O}$." The commutant $\mathcal{A}(\mathcal{O})' = \mathcal{A}(\mathcal{O}')$ (Haag duality) is dual to "the complementary wedge"; the failure of Haag duality (when it occurs) is dual to a bulk region — the *entanglement shadow* — that neither side reconstructs, the algebraic signature of a nontrivial RT phase transition or a bulk region behind both horizons. We use the clean (Haag-dual) version; the subtleties are exactly where current research lives.

[[subregion-subalgebra-duality|See the wiki page on subregion–subalgebra duality]] for the connection to the group's program.

## 6. What to take away

- **Type III at large $N$ (stated only for the holographic algebra; model proof for the mechanism):** the $N = \infty$ boundary single-trace algebra of a holographic CFT is type III$_1$; finite $N$ gives type I. The mechanism is decided by the Boltzmann ratios $\{e^{-\beta\omega_k}\}$: a discrete subgroup of $\mathbb{R}_{>0}$ gives III$_\lambda$, a dense one gives III$_1$ (§2.3). The transition is the algebraic content of "classical gravity vs. quantum gravity."
- **$1/N$ as $\hbar_{\rm bulk}$:** classical gravity ($1/N = 0$) ↔ type III$_1$; the crossed product keeps one gravitational mode and lands at semiclassical gravity ↔ type II$_\infty$.
- **Modular flow = bulk geometric flow (the dictionary):** the boundary modular flow of a geometrically nice region is the bulk Killing flow fixing the RT surface. Bisognano–Wichmann (boost) and CPW (horizon boost) are special cases.
- **Casini–Huerta–Myers (derived, $d=2$ complete):** for a ball in the CFT vacuum, $K_{B_R} = 2\pi\int (R^2 - r^2)/(2R)\,T_{00}$ — a *local* modular Hamiltonian. It is Bisognano–Wichmann transported by the conformal map $y^\pm = R(x^\pm-1)/(x^\pm+1)$, and it degenerates back to $2\pi K_{\rm boost}$ as $R\to\infty$. Every closed-form modular Hamiltonian in this subject is the wedge answer moved by a symmetry.
- **Subregion–subalgebra duality:** boundary subalgebras ↔ bulk entanglement wedges; commutants ↔ causal complements (under Haag duality).
- This block is **synthesis**: the same crossed-product machine, three geometries. The organizing diagram comes in Week 10.

## 7. Looking ahead

Week 10 completes the Liu block: the crossed product as "adding a clock that witnesses time," the **semiclassical reduction** $S_{\rm vN} \to A/4G_N + S_{\rm out}$ done two ways and shown to agree, and the **algebraic ER=EPR** criterion. We also draw Liu's organizing diagram placing Witten 2022, CPW, and AAJ relative to one another — the map students carry into Block 4 (AAJ), where the dressed algebra is finally *perturbed*. The final-write-up draft is due at the end of Week 10.

## 8. Problem set

**Core problems.**

**1. The diamond flow is complete.** Using the boxed $\zeta_D$ of §4.2, verify directly that $\zeta_D$ is null on the boundary of the diamond (i.e. $\zeta_D\cdot\zeta_D = 0$ on $|y|+|t| = R$) and vanishes at the two tips of the entangling surface $y=\pm R,\ t=0$. Then integrate the flow on the slice $t=0$ and show that a point starting at $y_0 \in (-R,R)$ takes infinite flow parameter to reach $y = \pm R$ — modular time never leaves the diamond.

**2. Two intervals, and why the derivation stops.** The §4.2 argument used one Möbius map carrying the wedge onto one diamond. Explain why no conformal transformation carries a wedge onto the union of *two* disjoint diamonds, and hence why the CHM derivation gives nothing for two intervals. (This is the structural reason for the non-locality quoted in Problem 6*.)

**3. Type from the mode spectrum.** Using the §2.3 criterion, determine the type in each case and justify by computing the closed subgroup of $\mathbb{R}_{>0}$ generated by the Boltzmann ratios: (i) frequencies $\omega_k = k\omega_0$, $k = 1,2,3,\dots$; (ii) frequencies $\omega_k \in \{\omega_0, \sqrt2\,\omega_0\}$; (iii) a single mode of frequency $\omega_0$ (finitely many tensor factors). Then say in one sentence which of these models a finite-$N$ CFT on a sphere and which models the $N=\infty$ limit.

**4. Dictionary table.** Reconstruct the dictionary table of §3.1 from memory and add a fourth row for a generic (non-symmetric) boundary region: what is known about its modular flow? (Answer: exists by Tomita–Takesaki, but acts non-geometrically; no closed form.)

**Starred problems.**

**5\*. Non-vacuum ball.** The CHM formula is for the *vacuum*. State what is known if the global state is a low-energy excitation of the vacuum (first-law/linearized regime): the modular Hamiltonian acquires a state-dependent correction $\delta K$, and $\delta\langle K\rangle = \delta S_{\rm EE}$ to first order (the "first law of entanglement"). Sketch why this follows from $\delta S = \delta\langle K\rangle$ at first order (positivity of relative entropy, Sem I Wk 7).

**6\*. Modular flow non-geometric for two intervals.** For two disjoint intervals in the CFT$_2$ vacuum, the modular Hamiltonian is **non-local** (it couples the two intervals). State this (Casini–Huerta for free fields) and explain why it breaks the naive dictionary — and why this is the algebraic origin of the mutual-information phase transition.

**Project problems.**

**7. Final-write-up draft.** (Due end of Week 10.) Produce a ≥10-page draft of your chosen final topic (Block 2 §7 options). Incomplete is fine; the goal is to surface scope/understanding problems before Block 4.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 3. Last revised 2026-08-23.*
