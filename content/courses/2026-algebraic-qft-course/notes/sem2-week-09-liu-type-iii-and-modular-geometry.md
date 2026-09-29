---
title: "Sem II Week 9 — Liu Lectures I: Type III at Large N and Modular Flow as Geometry"
type: lecture-notes
course: syllabus
semester: 2
week: 9
block: 3
duration: "master dossier: 4 hours of material; classroom core: 2-hour seminar + 1-hour office/self-study"
prerequisites: Sem II Wks 1–8 (Witten 2022, CPW); Sem I Wks 10, 12, 13 (Bisognano–Wichmann, type III$_1$, crossed product)
target_paper: "Hong Liu, Lectures on entanglement, von Neumann algebras, and emergence of spacetime, arXiv:2510.07017"
modified: 2026-08-24
---

# Sem II Week 9 — Liu Lectures I: Type III at Large $N$ and Modular Flow as Geometry

> *Blocks 1–2 gave us two worked examples of the same machine: Witten 2022 (single-sided) and CPW (two-sided). Both identified a holographic boundary algebra as type III$_1$, then dressed its modular flow by a crossed product. Block 3 steps back and reads Hong Liu's lecture notes (arXiv:2510.07017), the cleanest modern synthesis of the whole program. This week covers two structural pillars: (i) the representation-theoretic mechanism by which type III$_1$ can emerge in the specified large-$N$ GNS limits; and (ii) the conditional modular-flow/bulk-flow dictionary in symmetric holographic examples. An unbounded Hamiltonian spectrum alone classifies no von Neumann algebra. The Casini–Huerta–Myers ball modular Hamiltonian—supplementary to Liu's discussion—is the concrete touchstone we carry into Block 4.*

> **Route through this master dossier.** **Classroom core (two-hour seminar):** §§2.1–2.2 and 3, followed by the statement and central steps of the CHM derivation in §4. **Full derivation or self-study:** §§2.3 and 4 in full, including the null-coordinate flow, then Problems 1–5. **Research extension or office hour:** §5, the starred/project problems, and the primary-source route through Liu §§VI–VIII and Hislop–Longo/CHM. The board route emphasizes what is proved, what is imported, and what is a geometric dictionary.

## 0. Reading

**Primary:**
- Hong Liu, "Lectures on entanglement, von Neumann algebras, and emergence of spacetime," **arXiv:2510.07017**:
  - §§II–IV: operator-algebra, type, and modular-flow background;
  - §VI, especially §§VI.1–VI.3 and VI.6: the algebraic formulation of large-$N$ AdS/CFT and conserved-charge corrections;
  - §VII, especially §VII.2: subregion–subalgebra duality and reconstruction;
  - §VIII, especially §§VIII.1–VIII.3: emergence of causal structure, modular time, and the conditional algebraic ER=EPR proposal.

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

1. **They unify the large-$N$ and crossed-product spine.** Liu provides the language in which the course compares Witten and CPW. We then extend that comparison to AAJ as a later perturbative development; Liu's cited sections do not present AAJ's target framework. The course-built organizing diagram of Week 10 makes this extension explicit.

2. **They make the large-$N$ → type III logic explicit.** Blocks 1–2 *asserted* that the boundary single-trace algebra is type III$_1$ (Block 1 §4.2, hypothesis-explicit). Liu §VI explains the large-$N$ algebraic formulation, while §§VII–VIII connect it to the Leutheusser–Liu emergence-of-time and subregion programs.

3. **They install the dictionary.** "Modular flow = bulk geometric flow" is a useful slogan when its hypotheses are visible. Liu §§VII–VIII formulate the algebra/region and emergent-geometry claims; CHM and Hislop–Longo provide the supplementary exact ball example developed below.

This block is therefore **consolidation, not new content**. Students who have done Blocks 1–2 should find Liu mostly familiar—the value is in the synthesis. The seminar format assigns selected passages from §§VI–VIII, with §§II–IV routed only when background is needed.

## 2. Type III at large $N$: the structural story

### 2.1 The three faces of type III

Recall from Sem I (Wks 3, 12) that a type III factor can be recognized by the following intrinsic features:

- **No trace.** There is no faithful normal semifinite trace.
- **All projections infinite.** Every nonzero projection is Murray–von Neumann equivalent to a proper subprojection of itself.
- **No intrinsic density matrices.** Because the factor has no faithful normal semifinite trace, a normal state cannot be represented by a density element $\rho\in\mathcal M$ relative to such a trace. In a concrete representation a normal functional may still be written using an ambient trace-class operator on $\mathcal B(\mathcal H)$; that is not an intrinsic density matrix of $\mathcal M$.

Liu §IV adds a fourth, modular-theoretic face:

- **Connes spectrum is maximal (for III$_1$).** The invariant
  $$
  S(\mathcal M)=\bigcap_{\varphi}\operatorname{spec}(\Delta_\varphi)
  $$
  (with the appropriate faithful normal weights/states in the standard definition) is $[0,\infty)$. Since each $\Delta_\varphi$ is positive, this equality of the intersection forces $\operatorname{spec}(\Delta_\varphi)=[0,\infty)$ for every faithful normal state/weight entering that definition; correspondingly the logarithmic modular spectrum fills $\mathbb R$. The conclusion should not be transferred to a nonfaithful state, a support-restricted construction, or an unrelated effective Hamiltonian merely called “modular.”

> **Heuristic physical picture—not an equivalence theorem.** Continuum vacuum entanglement across a sharp boundary involves arbitrarily short scales, and cutoff entropies typically diverge. This picture is compatible with the absence of minimal projections and of an intrinsic semifinite trace in local type-III algebras. But “no shortest wavelength,” “no minimal projection,” “divergent regulated entropy,” and “type III” are not pairwise mathematical equivalences. Nor does energy being unbounded above imply a type. The classification requires the algebra, its representation, and the relevant modular/Connes invariants. The heuristic is useful because it tells us what physical structure the theorem is encoding; it must not replace the theorem.

### 2.2 How large $N$ produces it

At finite $N$, the **global** boundary theory in its ordinary Hilbert-space representation is expected to generate a type-I algebra, and on a compact spatial slice its thermal partition function can be trace class. This does not make sharp local continuum algebras finite dimensional: local subregion algebras may remain type III even at finite $N$. The large-$N$ discussion below concerns the emergent single-trace algebra in the specified GNS limit, not every possible boundary algebra.

The relevant large-$N$ limit can change the type. Liu §VI (following Leutheusser–Liu) frames it as follows:

**Large-$N$ type statement used in this block. [Stated only and hypothesis-explicit; refs: Liu §VI; Leutheusser–Liu arXiv:2110.05497, 2112.12156.]** *For the thermal large-$N$ single-trace GNS representations analyzed in these sources, the resulting von Neumann algebras can be type III$_1$. Restoring finite-$N$ relations changes the relevant global algebraic description, but it does not justify a blanket statement about all sharp local CFT subregions.*

The mechanism, structurally:

1. At $N = \infty$, single-trace correlators factorize (Block 1 §3.3): the algebra is a **generalized free field** with a fixed two-point function.
2. The relevant boundary region (one side of the eternal BH, or a time band) sees the GFF modes with a **thermal, continuous** spectrum — the boundary two-point function in the BTZ/TFD state is the thermal correlator (Block 1 §6).
3. The type is then established from the full representation and its modular/Connes invariants. A continuous two-point spectral density is important evidence in the examples, but the spectrum of one modular operator is not by itself a classification proof.

The next subsection gives a finite-mode and infinite-product **diagnostic model**. It illustrates how Boltzmann ratios enter modular spectra; it is not a substitute for the source's large-$N$ representation-theoretic argument.

### 2.3 Toy ITPFI diagnostic: what mode ratios can teach us

An infinite tensor product of matrix algebras in a product state is an ITPFI factor. Such models are useful because their modular spectra can be computed directly. The classification of a particular ITPFI factor, however, depends on the entire asymptotic eigenvalue sequence (and the associated ratio-set/flow-of-weights data), not just on spotting two ratios in one state.

**Setup.** Take one mode of frequency $\omega$ at inverse temperature $\beta$, and truncate it to its lowest two levels, so the one-mode algebra is $M_2(\mathbb{C})$ in the Gibbs state
$$
\phi_\lambda = \frac{1}{1+\lambda}\begin{pmatrix}1 & 0\\ 0 & \lambda\end{pmatrix}, \qquad \lambda := e^{-\beta\omega} \in (0,1).
$$
The full one-sided algebra of a GFF with mode frequencies $\{\omega_k\}$ is then modelled by the infinite tensor product
$$
\mathcal{M} = \bigotimes_{k}\big(M_2(\mathbb{C}),\, \phi_{\lambda_k}\big), \qquad \lambda_k = e^{-\beta\omega_k},
$$
built in the GNS representation of the product state $\phi = \bigotimes_k \phi_{\lambda_k}$. The two-level truncation is a genuine restriction on the model. For the narrower ratio-group diagnostic used below, however, a harmonic-oscillator Gibbs state has ratios $e^{-\beta\omega n}$ and therefore generates the same multiplicative group as $\lambda=e^{-\beta\omega}$. Its literal one-mode modular spectrum has more points, so only the generated group—not the full spectrum—is being preserved by this truncation.

**The modular spectrum of one factor.** For a finite-dimensional algebra in a faithful state with density $\rho$, the modular operator on $\mathcal{H} = M_2 \cong \mathbb{C}^2\otimes\mathbb{C}^2$ is $\Delta = \rho\otimes\rho^{-1}$ (Sem I Wk 5 §3), so its eigenvalues are the **ratios** of the eigenvalues of $\rho$. With $\rho$ having eigenvalues proportional to $1$ and $\lambda$,
$$
\mathrm{spec}\,\Delta_{\phi_\lambda} = \{\lambda^{-1},\, 1,\, 1,\, \lambda\}.
$$
The state's overall normalization drops out, which is why only the ratio $\lambda$ matters.

**A product-state modular-spectrum diagnostic.** On finite tensor subproducts the modular eigenvalues multiply. Consequently the closure
$$
G_\lambda:=\overline{\Big\{\textstyle\prod_k \lambda_k^{n_k} \;:\; n_k\in\mathbb{Z},\ \text{finitely many nonzero}\Big\}}
$$
records the multiplicative ratios visible in the chosen product state. One must not silently identify $\{0\}\cup G_\lambda$ with Connes' invariant $S(\mathcal M)$: $S(\mathcal M)$ is an intersection over weights/states, and proving equality requires the ITPFI classification theorem plus its hypotheses.

**Benchmark (i)—the Powers construction.** If every factor has the same eigenvalue ratio $\lambda=e^{-\beta\omega_0}$ and infinitely many factors are present, the standard Powers construction gives
$$
S(\mathcal M)=\{0\}\cup\lambda^{\mathbb Z},
\qquad
\mathcal M\text{ is type III}_\lambda.
$$
This conclusion uses the known Powers-factor theorem; the elementary ratio calculation is its visible input, not its full proof.

**Benchmark (ii)—dense ratios.** If the asymptotic product contains infinitely recurring incommensurate ratios with the regularity assumptions needed by the ITPFI theorem, then $G_\lambda$ can be dense in $\mathbb R_{>0}$. The relevant classification theorem can then yield
$$
S(\mathcal M)=[0,\infty),
\qquad
\mathcal M\text{ is type III}_1.
$$
Density of integer combinations follows from the elementary irrational-ratio argument; the passage from that density to $S(\mathcal M)$ is the non-elementary step.

**Benchmark (iii)—finite products.** With only finitely many tensor factors, the algebra is a matrix algebra, hence type I, however irrational its energy ratios may be. This is the quickest demonstration that a dense subgroup appearing in a modular spectrum is not by itself enough to prove type III$_1$.

The safe conclusion is therefore conditional: Boltzmann ratios help diagnose an infinite product, but the type is decided by the von Neumann algebra in its limiting representation and the appropriate Connes invariants. The large-$N$ result should be cited to the full argument in Liu and Leutheusser–Liu, not presented as an automatic consequence of “continuous frequencies.”

> **Physical picture.** The toy model shows why an infinite hierarchy of modular ratios matters. In the holographic examples, continuous large-$N$ spectral data and thermal modular dynamics accompany the type-III$_1$ representation. It is tempting to translate this immediately into horizon absorption, but that is a physical interpretation, not the operator-algebraic classification theorem: quasinormal spectra, finite-volume recurrences, and Connes invariants are distinct objects and should be compared rather than identified.

### 2.4 Why this matters downstream

The type III$_1$ structure is what makes the modular crossed product a type-II$_\infty$ factor (Sem I Wk 13). If the starting factor were type I, its modular automorphisms would be inner; the analogous crossed product would untwist to a tensor product with an abelian factor and would not produce the same outer-flow type promotion. Ordinary density-matrix entropies might already exist in that type-I setting, so the physics would be different—not nonexistent. The interest of the Witten/CPW construction is precisely that the relevant semiclassical algebra is type III$_1$, while the crossed product supplies a trace only after the modular generator is adjoined.

## 3. Modular flow as bulk geometric flow

### 3.1 The dictionary

The relevant content of Liu §§VII–VIII is a dictionary entry that Blocks 1–2 used in special cases:

**Modular-flow/geometric-flow dictionary. [Conditional; refs: Liu §§VII–VIII; supplementary exact examples: CHM arXiv:1102.0440 and Hislop–Longo 1982.]** *In the symmetric examples where the algebra/state pair and its bulk wedge admit the required (conformal) Killing symmetry, boundary modular flow is represented semiclassically by the corresponding bulk geometric flow fixing the RT surface. For generic states or regions, modular flow still exists but need not be local or geometric.*

Instances we have already met:

| Setting | Boundary region | Bulk Killing flow $\zeta$ | Reference |
|---|---|---|---|
| Free QFT, Rindler wedge | half-space | Lorentz boost | Bisognano–Wichmann, Sem I Wk 10 |
| Eternal BH, one boundary | full boundary | horizon boost ($\partial_t$) | CPW, Sem II Wk 5 |
| CFT vacuum, ball | ball of radius $R$ | conformal Killing vector | Casini–Huerta–Myers, this week |

> **Physical picture.** The dictionary says the *intrinsic thermal time* of a region (its modular flow, defined purely from the state and the algebra — Sem I Wk 6) can coincide with a geometric symmetry. For Rindler wedges, and for vacuum balls in a CFT, this is an exact QFT statement under the theorem's hypotheses. For the eternal black hole it is a holographic/semiclassical identification in the chosen code subspace, not a consequence of Tomita--Takesaki alone. For a generic region the modular flow still exists but is usually nongeometric and nonlocal. The tractable examples are special precisely because additional symmetry turns the abstract flow into a spacetime motion.

### 3.2 Generalizing Bisognano–Wichmann

Bisognano–Wichmann (Sem I Wk 10) is the dictionary's free-field, flat-space instance: the modular flow of the Rindler wedge is the boost, with modular Hamiltonian $K = 2\pi K_{\rm boost}$ and the famous $2\pi$ (Unruh temperature). Liu's dictionary is the holographic generalization:

- **B–W (flat space):** modular flow on $\mathcal{A}(W_R)$ = boost. Proven from Wightman axioms.
- **Holographic symmetric cases:** boundary modular flow is matched to bulk geometric flow under large-$N$, code-subspace, and geometric-symmetry assumptions.

The conceptual content is identical: a thermal-looking restricted vacuum, whose modular flow is a spacetime symmetry fixing the entangling surface. The difference is that B–W is a theorem about a fixed QFT, while Liu's version is a statement about the bulk dual of a large-$N$ boundary theory.

## 4. The Casini–Huerta–Myers ball modular Hamiltonian

The concrete worked example of the dictionary, and the one we carry into Block 4.

### 4.1 The statement

**Theorem 4.1 (Casini–Huerta–Myers). [Proved below in $d=2$ from Bisognano–Wichmann plus conformal invariance; general $d$ by the same argument — refs: CHM arXiv:1102.0440; Hislop–Longo 1982.]** *Let $\mathcal{O} = B_R$ be a ball of radius $R$ at fixed time in the vacuum of a CFT$_d$ on Minkowski space. The conventional one-sided vacuum modular charge—the generator of the restricted automorphism on $\mathcal A(B_R)$—is local:*
$$
K_{B_R} = 2\pi \int_{B_R} \frac{R^2 - r^2}{2R}\, T_{00}(\vec x)\, d^{d-1}x+c\mathbf 1,
$$
*where $r = |\vec x|$, $T_{00}$ is the energy density, and the scalar $c$ fixes the normalization of the state (formally, the analogue of a $\log Z$ term). It drops out of $\operatorname{Ad}e^{itK_{B_R}}$. On the standard GNS Hilbert space, the genuine operator $-\log\Delta_{B_R}$ is the difference of this charge and the corresponding commutant/complement charge. The modular flow restricted to $\mathcal A(B_R)$ is a one-parameter group of conformal transformations preserving the diamond (the conformal boost fixing $\partial B_R$).*

The profile $(R^2 - r^2)/(2R)$ vanishes on $\partial B_R$ (the entangling surface) and is maximal at the center — the modular flow slows to a stop at the boundary and runs fastest at the center, exactly as a conformal boost does.

The proof is short and worth doing because it shows the structural lineage of the CHM formula: Bisognano–Wichmann is transported by a conformal map. CHM adds the holographic thermal/hyperbolic-space interpretation and its use in the entropy argument; the local modular-Hamiltonian formula itself follows from the conformal equivalence of the diamond and wedge.

### 4.2 The conformal map from wedge to diamond

We work in $d = 2$, where the map is a Möbius transformation on each null coordinate and every step can be written down. Use null coordinates $x^\pm = x \pm t$, in which

- the **right Rindler wedge** $W = \{x > |t|\}$ is $\{x^+ > 0,\ x^- > 0\}$,
- the **causal diamond** $D_R$ of the interval $(-R,R)$ at $t = 0$, namely $\{|y| + |t| < R\}$, is $\{-R < y^\pm < R\}$.

In two dimensions any pair of maps $x^+ \mapsto y^+(x^+)$, $x^- \mapsto y^-(x^-)$ is a conformal transformation. Introduce an arbitrary length $L>0$ and the dimensionless wedge coordinates $\xi^\pm=x^\pm/L$; the final diamond flow will not depend on $L$. We need one Möbius map carrying $(0,\infty)$ onto $(-R,R)$. Take
$$
y^\pm = R\,\frac{\xi^\pm - 1}{\xi^\pm + 1},
\qquad\text{with inverse}\qquad
\xi^\pm = \frac{R + y^\pm}{R - y^\pm},
$$
which sends $x^\pm=0$ (equivalently $\xi^\pm=0$) to $y^\pm=-R$ and $x^\pm\to\infty$ to $y^\pm\to R$, monotonically. Thus it maps $W$ onto $D_R$ and, being a Möbius map on each null line, it is conformal. The scale $L$ only chooses which wedge point maps to the center of the diamond.

Now push the boost forward. The boost of rapidity $\lambda$ acts on null coordinates by $x^\pm \mapsto e^{\pm\lambda}x^\pm$, so its Killing vector is $\zeta_W = x^+\partial_+ - x^-\partial_-$. Differentiating the map,
$$
\frac{dy^\pm}{d\xi^\pm} = \frac{2R}{(\xi^\pm+1)^2},
\qquad
\frac{d\xi^\pm}{d\lambda} = \pm \xi^\pm,
$$
and using $\xi^\pm + 1 = 2R/(R - y^\pm)$ from the inverse map, we obtain
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

First, Bisognano–Wichmann (Sem I Wk 10, and [[courses/2026-algebraic-qft-course/conventions]]): on the standard Hilbert space the vacuum modular operator of the right wedge obeys
$$
-\log\Delta_W=2\pi K_{\rm global}
=2\pi(K_R-K_L),
$$
where $K_{\rm global}$ is the global Lorentz-boost generator. Its restriction to the right wedge algebra is implemented by the conventional one-sided charge
$$
K_{W_R}^{\rm one\mbox{-}sided}
:=2\pi K_R
=2\pi\int_0^\infty x\,T_{00}(x)\,dx+c\mathbf1,
$$
where $K_R$ in the preceding decomposition is the unnormalized right boost-energy piece. The left/complement contribution commutes with $\mathcal A(W_R)$, so $-\log\Delta_W$ and $K_{W_R}^{\rm one\mbox{-}sided}$ implement the same automorphism on right observables, but they are not the same operator. This notation also prevents an accidental second factor of $2\pi$: $K_R$ is unnormalized, whereas $K_{W_R}^{\rm one\mbox{-}sided}=2\pi K_R$ is the conventional modular charge.

Second, conformal invariance: the CFT$_2$ vacuum is invariant under the Möbius map of §4.2, and that map carries $\mathcal{A}(W)$ onto $\mathcal{A}(D_R)$. Modular data are determined by the pair (algebra, state), so a transformation preserving the state and mapping one algebra onto the other must carry the modular flow of the first onto the modular flow of the second. The modular flow of $\mathcal{A}(D_R)$ in the vacuum is therefore the flow along $\zeta_D$, at the same rate — modular time $t$ ↔ flow parameter $2\pi t$.

The one-sided generator of the $\zeta_D$-flow on the slice $t = 0$ is $\int \zeta_D^t\,T_{00}\,dy$, so
$$
K_{D_R} \;=\; 2\pi \int_{-R}^{R} \frac{R^2 - y^2}{2R}\; T_{00}(y)\,dy ,
$$
up to the scalar normalization $c\mathbf 1$, which does not affect the flow. This is Theorem 4.1 in $d=2$. $\square$

> **Physical picture.** The derivation explains why the wedge and vacuum ball are members of one symmetry family. A CFT has enough symmetry to move the wedge onto a diamond, so the diamond inherits a local $K$. Generic regions lack that symmetry and their modular Hamiltonians are usually nonlocal. The parabolic profile is the linear Rindler profile seen through a Möbius map; this does not exclude other solvable modular Hamiltonians obtained by different methods.

### 4.4 General $d$

In $d > 2$ the map is a special conformal transformation rather than a chiral Möbius map, but the structure is identical, and the resulting conformal Killing vector is the direct analogue of the boxed formula above with $y$ replaced by the radius $r = |\vec x|$:
$$
\zeta_D = \frac{1}{2R}\Big[\big(R^2 - t^2 - r^2\big)\,\partial_t - 2\,r\,t\,\partial_r\Big]
= \frac{1}{2R}\big(R^2 P_0 - K_0\big),
$$
where $P_0 = \partial_t$ generates time translations and $K_0$ is the special conformal generator in the time direction. That the two expressions agree is a one-line check: with mostly-plus signature $K_0 = x^2\partial_t - 2x_0(x\cdot\partial) = (t^2+r^2)\partial_t + 2rt\,\partial_r$, so $\tfrac{1}{2R}(R^2\partial_t - K_0)$ is the displayed vector field. Since $\zeta_D$ is a fixed linear combination of conformal generators, it is a conformal Killing vector for any $d$, and the pullback argument of §4.3 goes through verbatim, giving
$$
K_{B_R} = 2\pi\int_{B_R}\frac{R^2-r^2}{2R}\,T_{00}(\vec x)\,d^{d-1}x+c\mathbf 1 .
$$

### 4.5 The Rindler limit as a check

The formula must degenerate to Bisognano–Wichmann when the ball grows into a half-space, and it does. Shift the center to $x_0 = R$ and let $R\to\infty$ holding $\xi = R - x_0 + x$ fixed, so that $r = R - \xi$ and
$$
\frac{R^2 - r^2}{2R} = \frac{(R-r)(R+r)}{2R} = \frac{\xi\,(2R - \xi)}{2R} \;\xrightarrow[R\to\infty]{}\; \xi .
$$
The parabolic weight straightens into the linear Rindler weight, and
$$
K_{B_R}^{\rm one\mbox{-}sided} \;\longrightarrow\; 2\pi\int_{\xi>0}\xi\,T_{00}(\xi)\,d^{d-1}x+c\mathbf1,
$$
the conventional right-wedge modular charge. Subtracting the complementary charge reconstructs the global standard-space generator $2\pi(K_R-K_L)$. This closes the circle: we obtained CHM from Bisognano–Wichmann by a conformal map, and CHM returns its restricted wedge flow in the half-space limit.

### 4.6 The bulk Killing vector

In pure AdS$_{d+1}$, the boundary ball $B_R$ has a bulk **entanglement wedge** bounded by the RT surface (a hemisphere anchored on $\partial B_R$). There is a bulk Killing vector $\zeta_{\rm bulk}$ that (i) restricts to $\zeta_D$ on the boundary and (ii) vanishes on the RT surface. The bulk modular flow is the boost-like geometric flow along $\zeta_{\rm bulk}$; the boundary modular flow is its restriction. This is the explicit bulk realization of Liu's dictionary. Near the fixed surface the local picture is Rindler-like, with the RT surface playing the role of a bifurcation surface—not an axis of a rigid Euclidean rotation.

> **Physical picture.** Two features carry physical weight in this symmetric example. First, **locality**: $K_{B_R}$ is an integral of the local energy density because the vacuum, the CFT, and the ball furnish the required conformal symmetry. Second, the weight vanishes at the ball's entangling surface, consistently with that surface being fixed by the conformal modular flow. Neither feature should be promoted to a universal formula for generic modular Hamiltonians, and the localization of a gravitational area term requires the separate holographic entropy dictionary. The GJW deformation studied later changes the state/algebraic setup; its time-advance interpretation is not derived from this weight alone.

## 5. Subregion–subalgebra duality

Liu §VII packages the dictionary into a duality between bulk regions and boundary subalgebras.

**Subregion–subalgebra duality (Liu §VII). [Hypothesis-explicit.]** *A boundary subregion $\mathcal{O}$ corresponds to a boundary subalgebra $\mathcal{A}(\mathcal{O})$; the bulk dual is the entanglement wedge $W_{\mathcal{O}}$, and bulk operators in $W_{\mathcal{O}}$ are reconstructible from $\mathcal{A}(\mathcal{O})$ in the stated code-subspace/approximation regime. Inclusions of regions correspond to inclusions of algebras; causal complements correspond to commutants when the required duality holds.*

> **Physical picture.** This is the algebraic skeleton of the Ryu–Takayanagi / entanglement-wedge-reconstruction circle of ideas. The slogan “access to $\mathcal A(\mathcal O)$ corresponds to reconstructibility in $W_{\mathcal O}$” is code-subspace and approximation dependent. When Haag duality holds, commutants match complementary algebras. Its failure can signal extra superselection or generalized-symmetry structure; identifying that failure with a particular entanglement shadow or RT transition requires an additional holographic argument.

See §5 below and Liu §VII for the subregion–subalgebra connection used in the group's program.

## 6. What to take away

- **Type III at large $N$ (source result under its stated GNS hypotheses):** the thermal large-$N$ single-trace algebras studied by Liu and Leutheusser–Liu can be type III$_1$. The ITPFI exercise illustrates modular ratios but is not the proof of that result.
- **Regime dictionary:** strict large-$N$ single-trace limits can produce type III$_1$ factors; retaining the leading gravitational fluctuation in the Witten/CPW construction produces a type-II$_\infty$ crossed product. Exact finite-$N$ and sharp local-subregion statements must be treated separately.
- **Modular flow = bulk geometric flow (the dictionary):** the boundary modular flow of a geometrically nice region is the bulk Killing flow fixing the RT surface. Bisognano–Wichmann (boost) and CPW (horizon boost) are special cases.
- **Casini–Huerta–Myers (supplementary source; derived here, $d=2$ complete):** for a ball in the CFT vacuum, $K_{B_R}=2\pi\int (R^2-r^2)/(2R)\,T_{00}+c\mathbf1$ is local up to its scalar normalization. It is Bisognano–Wichmann transported by a conformal map and returns to the wedge formula in the half-space limit.
- **Subregion–subalgebra duality:** boundary subalgebras ↔ bulk entanglement wedges; commutants ↔ causal complements (under Haag duality).
- This block is **synthesis**: the same crossed-product machine, three geometries. The organizing diagram comes in Week 10.

## 7. Looking ahead

Week 10 completes the Liu block: the crossed product as "adding a clock that witnesses time," the **semiclassical reduction** $S_{\rm vN} \to A/4G_N + S_{\rm out}$ done two ways and shown to agree, and the **algebraic ER=EPR** criterion. We also draw a **course synthesis diagram**: Liu supplies the Witten/CPW spine, and the course adds AAJ as a later perturbative comparison. Students carry that map into Block 4, where the dressed algebra is finally *perturbed*. The final-write-up draft is due at the end of Week 10.

## 8. Problem set

**Core problems.**

**1. The diamond flow is complete.** Using the boxed $\zeta_D$ of §4.2, verify directly that $\zeta_D$ is null and tangent on the null boundary $|y|+|t|=R$. It vanishes at the interval endpoints $(t,y)=(0,\pm R)$ and at the future/past diamond tips $(t,y)=(\pm R,0)$. Do **not** assume that an orbit starting at $t=0$ remains on that slice. Instead, put
$$
\xi_0=\frac{R+y_0}{R-y_0},
\qquad
\xi^\pm(\lambda)=e^{\pm\lambda}\xi_0,
\qquad
y^\pm(\lambda)=R\frac{\xi^\pm(\lambda)-1}{\xi^\pm(\lambda)+1}.
$$
Recover $t(\lambda)$ and $y(\lambda)$ from $y^\pm=y\pm t$. Show that the orbit approaches $(R,0)$ as $\lambda\to+\infty$ and $(-R,0)$ as $\lambda\to-\infty$, reaching neither tip at finite flow parameter. This is the correct completeness statement.

**2. Two intervals, and why the derivation stops.** The §4.2 argument used one Möbius map carrying the wedge onto one diamond. Explain why no conformal transformation carries a wedge onto the union of *two* disjoint diamonds, and hence why the CHM derivation gives nothing for two intervals. (This is the structural reason for the non-locality quoted in Problem 6*.)

**3. Modular ratios are not yet a type proof.** Compute $G_\lambda$ for (i) infinitely many identical ratios $e^{-\beta\omega_0}$; (ii) infinitely recurring frequencies $\omega_0$ and $\sqrt2\omega_0$; and (iii) a finite tensor product containing those same two frequencies. Use the known Powers theorem only in case (i). Explain why case (iii) is type I despite its irrational ratio data, and identify the extra ITPFI classification input needed before declaring case (ii) type III$_1$.

**4. Dictionary table.** Reconstruct the dictionary table of §3.1 from memory and add a fourth row for a generic (non-symmetric) boundary region: what is known about its modular flow? (Answer: exists by Tomita–Takesaki, but acts non-geometrically; no closed form.)

**Starred problems.**

**5\*. Non-vacuum ball.** The CHM formula is the modular Hamiltonian $K_0$ of the *vacuum* restriction. For a differentiable family of nearby states, prove the first-law statement $\delta S=\delta\langle K_0\rangle$ from the fact that relative entropy about the reference state begins at second order. The modular Hamiltonian of the perturbed state generally has its own state-dependent correction, but the first-law formula does not require computing it and does not imply that the full non-vacuum modular flow remains local.

**6\*. Modular flow for two intervals.** In a free-field example, describe the nonlocal terms that couple two disjoint intervals and explain why the one-ball conformal-map derivation no longer applies. Separately, state what additional large-$c$ holographic input is needed to discuss a mutual-information/RT phase transition; do not derive that transition from nonlocality alone.

**Project problems.**

**7. Final-write-up draft.** (Due end of Week 10.) Produce a ≥10-page draft of your chosen final topic (Block 2 §7 options). Incomplete is fine; the goal is to surface scope/understanding problems before Block 4.

**Wiki connections.** [[subregion-subalgebra-duality|subregion–subalgebra duality]]

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 3. Last revised 2026-08-24.*
