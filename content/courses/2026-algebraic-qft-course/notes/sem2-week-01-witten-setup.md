---
title: "Sem II Week 1 — Witten Setup: Large N, Single-Trace Operators, and the Emergence of Type III"
type: lecture-notes
course: syllabus
semester: 2
week: 1
block: 1
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Sem I complete; especially Weeks 10 (Bisognano–Wichmann), 12 (type III_1), 13 (crossed product), 14 (dressed entropy), 15 (TFD)
target_paper: "Witten, JHEP 10 (2022) 008, arXiv:2112.12828"
modified: 2026-06-11
---

# Sem II Week 1 — Witten Setup: Large $N$, Single-Trace Operators, and the Emergence of Type III

> *Semester II opens with Witten's "Gravity and the Crossed Product" (arXiv:2112.12828). The paper has a clean architecture: at large $N$ a holographic CFT's boundary single-trace algebra becomes type III$_1$; gauging the ADM time generator (= the modular flow at large $N$) by the crossed product gives a type II$_\infty$ algebra with a faithful normal semifinite trace; the dressed entropy equals the generalized entropy $A/(4G_N) + S_{\mathrm{out}}$ up to an additive constant. This week we set up the **large-$N$ side** of the story: why the boundary algebra is type III$_1$, how the modular flow emerges from the ADM Hamiltonian, and how the abstract crossed product of Block D applies. Weeks 2–3 build the construction; Week 4 verifies the whole thing in the free-field Rindler analogue, where every step is computable.*

## 0. Reading

**Primary:**
- Witten, "Gravity and the crossed product," JHEP 10 (2022) 008, **arXiv:2112.12828**, §§1–2 (the setup and large-$N$ algebra).
- Liu, "Lectures on entanglement, von Neumann algebras, and emergence of spacetime," **arXiv:2510.07017**, §§1–2 (type III at large $N$, holographic dictionary; the recommended companion reading).

**Secondary:**
- Aharony, Gubser, Maldacena, Ooguri, Oz, "Large $N$ field theories, string theory and gravity," *Phys. Rep.* 323 (2000) 183 — the standard holographic background.
- Witten, "Notes on some entanglement properties of QFT," arXiv:1803.04993, §§1–3 — modular theory in QFT (Sem I primary).

**Optional research reading:**
- Leutheusser & Liu, "Causal Connectability Between Quantum Systems and the Black Hole Interior in Large-N Gauge Theories," arXiv:2110.05497 — emergence of type III at large $N$, with explicit examples.
- Faulkner, Li, Wang, "A modular toolkit for bulk reconstruction," *JHEP* 04 (2019) 119, arXiv:1806.10560 — modular flow in holographic settings.

## 1. Why this paper

Witten 2022 is the structural anchor of the entire algebraic-gravity program. It does **two things** that the rest of Semester II builds on:

1. **Identifies the type-III$_1$ structure of holographic boundary algebras at large $N$.** This is the physical version of the Sem I Block C structural theorem: under the holographic dictionary, the boundary single-trace algebra of a CFT dual to bulk gravity is type III$_1$. The hypotheses required for this identification — namely, large $N$ and well-defined Gaussian factorization — are the holographic analog of nuclearity + split property.

2. **Applies the Block D crossed-product machinery to the gravitational dressing.** The modular flow of the boundary algebra at large $N$ is identified with the ADM Hamiltonian (the boundary time translation, up to gauge redundancy). Crossing the algebra with this flow gives a type II$_\infty$ algebra. The dressed entropy on this algebra is the generalized entropy of the bulk — the same area-plus-bulk-entanglement formula that runs through the Ryu–Takayanagi / Lewkowycz–Maldacena story.

The combination is the punchline: **bulk gravitational entropy is the dressed-algebra entropy of the boundary single-trace algebra, under the modular crossed product.**

**Why study this paper.** It is the first paper to make the structural connection between Sem I's operator-algebraic machinery (modular theory, crossed products, dressed entropy) and the holographic entropy formulas of bulk gravity (Bekenstein–Hawking, Ryu–Takayanagi). It made type III von Neumann algebras a tool of practical use in gravitational physics, not just an abstract feature of QFT.

**Course strategy.** We do not try to prove Witten 2022 line by line; instead, we follow its **structural arc** and check every algebraic step in the free-field Rindler analog (Week 4), where the holographic dictionary is replaced by Bisognano–Wichmann. The pattern Witten 2022 → CPW → AAJ uses repeatedly in Semester II is **"the operator-algebraic construction is provided by Block D; the holographic identification is the new physics input."**

## 2. Recap: what Block D provides

Block D (Sem I Weeks 13–15) gave us the algebraic toolkit. Recall the structure:

**Modular crossed product (Week 13).** Given a vN algebra $\mathcal{M}$ with faithful normal state $\omega$ and modular flow $\sigma^\omega_t = \Delta_\omega^{-it}\,\cdot\,\Delta_\omega^{it}$ (our upper-strip $\beta = +1$ convention), the modular crossed product is
$$
\hat{\mathcal{M}} \;:=\; \mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R}
$$
acting on $\mathcal{H} \otimes L^2(\mathbb{R})$, generated by $\pi(a) = \int^\oplus \sigma^\omega_{-s}(a)\,ds$ and $\lambda(t) = 1 \otimes U_t$ with $\lambda(t)\pi(a)\lambda(t)^* = \pi(\sigma^\omega_t(a))$.

**Connes–Takesaki theorem (Week 13).** If $\mathcal{M}$ is type III$_1$, then $\hat{\mathcal{M}}$ is **type II$_\infty$**, with a faithful normal semifinite trace $\hat\tau$, unique up to rescaling, satisfying $\hat\tau \circ \theta_r = e^{-r}\,\hat\tau$ under the dual action.

**Dressed entropy (Week 14).** $S_{\mathrm{vN}}(\hat\rho) = -\hat\tau(\hat\rho_d\,\log\hat\rho_d)$ is well-defined modulo an additive constant. Differences between two dressed states satisfy
$$
S_{\mathrm{vN}}(\hat\rho_\omega) - S_{\mathrm{vN}}(\hat\rho_\phi) = -S(\omega\|\phi) + \mathcal{B}(\omega, \phi), \qquad \mathcal{B}(\omega, \phi) = \omega(K_\phi) - \phi(K_\phi).
$$

**Free-field Rindler workhorse (Week 14 §5; Week 15 §6).** For the free 2D massless scalar on $\mathcal{A}(W_R)$, Bisognano–Wichmann gives the explicit modular flow $\sigma_t^{W_R}$, and the crossed product is computable in closed form with trace kernel involving $e^{-2\pi s}$.

**The missing ingredient (this block).** To apply this machinery to gravity, we need to know **what algebra to start with** and **what flow to dress by**. Witten 2022's contribution is the identification: the algebra is the large-$N$ single-trace algebra of a holographic CFT; the flow is the ADM time translation, which equals the modular flow of the boundary subregion.

## 3. Large-$N$ field theory

A holographic CFT (e.g., $\mathcal{N} = 4$ super-Yang–Mills with gauge group $\mathrm{U}(N)$ or $\mathrm{SU}(N)$) has a large-$N$ limit in which the gauge group becomes infinite-dimensional. This limit is governed by the **'t Hooft expansion**.

### 3.1 'T Hooft expansion

Consider a $\mathrm{U}(N)$ gauge theory with coupling $g$. The 't Hooft coupling is $\lambda := g^2 N$, held fixed as $N \to \infty$. In this limit:

- **Planar diagrams dominate.** Feynman diagrams that can be drawn on a sphere (genus 0) are leading order; higher-genus diagrams are suppressed by $1/N^2$.
- **The expansion is in $1/N$**, with $\lambda$ as a separate (independent) parameter that controls the strength of the planar interactions.

For correlators of gauge-invariant operators:
$$
\langle\mathcal{O}_1\mathcal{O}_2\cdots\mathcal{O}_k\rangle = N^{2-2g}\,f_{\text{planar}}(\lambda) + N^{-2g}\,f_{1\text{-loop}}(\lambda) + \cdots
$$
where $g$ is the genus of the dominant diagram topology.

### 3.2 Single-trace operators

**Definition 3.1.** A **single-trace operator** in a $\mathrm{U}(N)$ gauge theory is
$$
\mathcal{O}(x) := \frac{1}{N}\mathrm{Tr}\!\big(\Phi_{i_1}(x)\,\Phi_{i_2}(x)\,\cdots\,\Phi_{i_k}(x)\big),
$$
for some matrix-valued fields $\Phi_i$ in the theory. The $1/N$ normalization is chosen so that the connected two-point function $\langle\mathcal{O}\,\mathcal{O}\rangle$ stays $O(1)$ as $N \to \infty$.

**Multi-trace operators** are products of single-traces: $\mathcal{O}_1(x)\,\mathcal{O}_2(x)$, etc.

### 3.3 Large-$N$ factorization

**Theorem 3.2 (Large-$N$ factorization). [Stated only — refs: 't Hooft 1974; standard large-$N$ texts.]** *In a $\mathrm{U}(N)$ gauge theory, connected correlators of $k$ single-trace operators are*
$$
\langle\mathcal{O}_1\cdots\mathcal{O}_k\rangle_{\mathrm{conn}} = O(N^{2-k}).
$$
*Hence as $N \to \infty$, $k$-point functions factorize:*
$$
\langle\mathcal{O}_1\mathcal{O}_2\mathcal{O}_3\mathcal{O}_4\rangle \to \langle\mathcal{O}_1\mathcal{O}_2\rangle\langle\mathcal{O}_3\mathcal{O}_4\rangle + \langle\mathcal{O}_1\mathcal{O}_3\rangle\langle\mathcal{O}_2\mathcal{O}_4\rangle + \langle\mathcal{O}_1\mathcal{O}_4\rangle\langle\mathcal{O}_2\mathcal{O}_3\rangle + O(1/N^2).
$$

The four-point function factorizes into sums of products of two-point functions — exactly Wick's theorem for a Gaussian random variable. The algebra of single-trace operators at $N = \infty$ is **a generalized free field**: a (non-Lagrangian) field whose $n$-point functions are determined by Wick contraction with a given two-point function.

This is the key structural input. The algebra is *not* the original gauge theory's algebra; it is the **leading large-$N$ limit**, which has Gaussian (free-field-like) correlation structure but inherits its two-point function from the underlying CFT.

### 3.4 Generalized free fields

**Definition 3.3.** A **generalized free field** (GFF) on a spacetime $M$ is a quantum field whose correlation functions are Gaussian:
$$
\langle\mathcal{O}(x_1)\cdots\mathcal{O}(x_{2k})\rangle = \sum_{\text{pairings}}\,\prod_{\text{pairs }(i, j)} W(x_i, x_j),
$$
with $W(x, y)$ a positive Wightman two-point function. Odd correlators vanish.

The two-point function $W(x, y)$ is the only input. A free scalar field is a GFF with the standard Klein–Gordon $W$; the single-trace operator at large $N$ is a GFF with the CFT's two-point function as input.

**Key difference from a free Lagrangian field.** The GFF generally does not satisfy any local equation of motion. There is no Lagrangian; only a two-point function. This is exactly the structural feature of large-$N$ single-trace operators.

> **Physical picture: why Gaussianity is "the bulk".** Large-$N$ factorization is not a technical curiosity — it is *where the bulk comes from*. A Gaussian operator algebra is, by the Week 8 dictionary, a free field; the question is "a free field on what spacetime?" The answer is fixed by the only data a GFF has, its two-point function — and the holographic CFT's thermal two-point function is exactly that of a free field propagating on the *bulk black-hole geometry*, evaluated at the boundary. So the single-trace GFF at $N = \infty$ *is* the boundary avatar of free bulk quantum fields on a fixed gravitational background: planar factorization = bulk Fock space; $1/N$ corrections = bulk interactions ($1/N \sim \sqrt{G_N}$, gravitational self-coupling); the absence of a boundary equation of motion for the GFF reflects that the operator really satisfies a wave equation in one *more* dimension. This is the algebraic restatement of "the bulk is the large-$N$ master field," and it explains why operator-algebraic statements about the GFF algebra (its type, its modular flow) translate directly into geometric statements about the bulk (horizons, Killing flows).

## 4. The boundary single-trace algebra

### 4.1 Setup

Consider a holographic CFT$_d$ dual to a $(d+1)$-dimensional bulk gravity theory. Choose a boundary subregion (e.g., one side of an eternal AdS-Schwarzschild black hole) and consider the algebra of single-trace operators smeared in that region.

At large $N$, this algebra is a Weyl-algebra-like object generated by Gaussian-correlated operators. The boundary subregion $\mathcal{O}$ has an associated local algebra $\mathcal{A}_R(\mathcal{O})$ in the GFF representation.

### 4.2 Type III$_1$ at large $N$

**Theorem 4.1 (Type III$_1$ at large $N$). [Stated only — hypothesis-explicit; refs: Witten 2022 §2; Leutheusser–Liu 2021.]** *Let the holographic CFT have a well-defined large-$N$ limit with single-trace GFF structure. Then for a boundary subregion $\mathcal{O}$ whose causal complement is non-empty open, the algebra $\mathcal{A}_R(\mathcal{O})$ at $N = \infty$ is a type III$_1$ factor.*

**Why this is the right hypothesis.** The conditions are:

1. **Single-trace GFF structure** at $N = \infty$. This is the holographic analog of "Wightman QFT" — the operators have well-defined Gaussian correlators determined by a two-point function.

2. **The boundary subregion has a Rindler-like or wedge-like causal structure**, so the modular flow on $\mathcal{A}_R(\mathcal{O})$ is geometric. This is the analog of Bisognano–Wichmann (Sem I Wk 10).

3. **No infrared divergence** from the boundary. For non-compact boundaries (Poincaré patch of AdS), the boundary single-trace algebra inherits the type III$_1$ structure from the Bisognano–Wichmann argument applied at the AdS boundary.

The hypotheses are the holographic analog of nuclearity + split property (Sem I Wk 12). The conclusion is the same.

### 4.3 At finite $N$ the algebra is type I

At finite $N$, the boundary CFT has a finite-dimensional Hilbert space if the subregion is compact, or a separable Hilbert space with density-matrix-trace if not. The algebra is **type I**: $\mathcal{A}_R(\mathcal{O}) \cong \mathcal{B}(\mathcal{H}_R)$ for the appropriate boundary Hilbert space.

The transition from type I (finite $N$) to type III$_1$ (large $N$) is the algebraic content of "classical gravity emerges in the $N \to \infty$ limit." Quantum gravity at finite $N$ has type-I algebras with density matrices; classical gravity has type-III$_1$ algebras with no density matrices but with modular structure and the crossed-product fix.

### 4.4 $1/N$ as $\hbar$

A useful heuristic from Witten 2022 and Liu's lectures: **$1/N$ plays the role of $\hbar$ in the bulk.** Specifically:

- At $1/N = 0$: classical gravity in the bulk, type III$_1$ algebra on the boundary. The modular flow is *outer*; no traces, no density matrices.
- At $1/N > 0$: quantum gravity in the bulk, type I algebra on the boundary. The modular flow becomes inner (the ADM Hamiltonian is in the algebra); a density matrix and trace exist, with $1/N$-suppressed corrections.

The crossed-product construction of Witten 2022 is *intermediate*: it lives at $1/N = 0$ (classical gravity, type III$_1$) but **dresses the algebra** with the modular clock to get a type II$_\infty$ algebra with a trace. This dressed trace is the natural object to compare to bulk-gravity entropy formulas, which themselves arise from semiclassical (large-$N$) computations.

> **Physical picture: the type transition is the emergence of a horizon.** At finite $N$ nothing forbids reconstructing the full state from one boundary: the algebra is type I, every state has a density matrix, and "behind the horizon" is just a complicated but accessible part of one big Hilbert space. At $N = \infty$ the algebra degrades to type III$_1$ — and this degradation *is* the horizon becoming causally absolute. Three diagnostics line up. (1) *Information:* no density matrix for one side = no complete local accounting of the state = a genuine exterior/interior split. (2) *Dynamics:* the ADM time flow turns outer — time evolution can no longer be generated from inside the one-sided algebra, just as exterior Schwarzschild time translation cannot move anything across the horizon. (3) *Thermality:* the intrinsic modular clock of type III$_1$ (Week 7 Corollary 4.3) is the Hawking temperature made algebra-intrinsic. Leutheusser–Liu sharpened this into a signal: the emergence of type III$_1$ at large $N$ in the thermal regime above the Hawking–Page transition is the *boundary algebra's way of registering that a black hole horizon has formed in the bulk.* Sharp horizons are a strict-$N=\infty$ idealization, which is precisely why finite-$N$ quantum gravity is expected to resolve the information problem that the idealization creates.

## 5. The modular flow at large $N$

The crucial structural input: at large $N$, the **modular flow of the boundary subregion** equals the **time translation generated by the ADM Hamiltonian**.

### 5.1 The ADM Hamiltonian

In the bulk gravity theory, the **ADM Hamiltonian** $H_{\mathrm{ADM}}$ is the energy of a configuration as measured at the asymptotic boundary. For an asymptotically AdS spacetime with a boundary time coordinate $t$, $H_{\mathrm{ADM}}$ generates time translation on the boundary.

On the boundary CFT, the ADM Hamiltonian corresponds to a quasi-local Hamiltonian $H_R$ that generates time translation of operators smeared in the right subregion. At finite $N$, $H_R$ is an *inner* element of the algebra $\mathcal{B}(\mathcal{H}_R)$. At infinite $N$, $H_R$ is *outer*: it generates an automorphism of $\mathcal{A}_R$ that does not come from any element of $\mathcal{A}_R$.

### 5.2 Modular flow = ADM time

**Theorem 5.1 (Witten 2022 §2). [Stated only.]** *At large $N$, the modular flow $\sigma^{\mathrm{TFD}}_t$ of the TFD state on $\mathcal{A}_R$ coincides with the time translation generated by $\beta_H\,H_R$ (where $\beta_H$ is the Hawking inverse temperature). On the right algebra of the two-sided eternal BH, this is the $\mathrm{ADM}$ time on the right boundary.*

**Equivalently:** $\sigma^{\mathrm{TFD}}_t = \alpha_{+\beta_H t}^{H_R}$ in our convention, where $\alpha_s^{H_R}(a) = e^{isH_R}\,a\,e^{-isH_R}$.

This is the holographic generalization of Bisognano–Wichmann (Sem I Wk 10): in the free-field Rindler case, the modular flow on the wedge algebra is the Lorentz boost; in the holographic case, the modular flow on the boundary subregion is the ADM time translation. The identification is at large $N$ and uses the holographic dictionary.

### 5.3 The structural picture

We now have all the algebraic pieces:

| Object | Free-field Rindler (Sem I) | Holographic large-$N$ (Witten 2022) |
|---|---|---|
| Algebra | $\mathcal{A}(W_R)$, type III$_1$ | $\mathcal{A}_R$, type III$_1$ at large $N$ |
| State | Minkowski vacuum (TFD of boost) | TFD vacuum |
| Modular flow | boost $\sigma_t^{W_R}$ | ADM time $\alpha^{H_R}_{\beta_H t}$ |
| Modular Hamiltonian | $2\pi K_{\mathrm{boost}}$ | $\beta_H H_R$ |
| KMS temperature | Unruh $T_U = 1/(2\pi)$ | Hawking $T_H = 1/\beta_H$ |
| Crossed product algebra | $\hat{\mathcal{A}}(W_R) = \mathcal{A}(W_R)\rtimes_{\mathrm{boost}}\mathbb{R}$ | $\hat{\mathcal{A}}_R = \mathcal{A}_R \rtimes_{\mathrm{ADM}}\mathbb{R}$ |
| Type of dressed algebra | type II$_\infty$ | type II$_\infty$ |
| Dressed entropy | area law + finite difference | generalized entropy $A/(4G_N) + S_{\mathrm{out}}$ |

The free-field Rindler model is the **complete algebraic skeleton** of the holographic case. Every operator-algebraic step is computable on both sides. The Sem II Block 1 mini-calculation in Week 4 makes this concrete.

## 6. Worked computation: 2D BTZ analog

The cleanest concrete example: 2D CFT on the eternal BTZ black hole boundary.

### 6.1 BTZ black hole

The 3D Bañados–Teitelboim–Zanelli black hole is the simplest non-trivial AdS$_3$ black hole, with metric
$$
ds^2 = -\frac{r^2 - r_h^2}{\ell^2}\,dt^2 + \frac{\ell^2}{r^2 - r_h^2}\,dr^2 + r^2\,d\varphi^2,
$$
where $\ell$ is the AdS radius and $r_h$ is the horizon radius. The Hawking temperature is $T_H = r_h/(2\pi\ell^2)$.

The **two-sided BTZ** is the maximally extended version, with two asymptotic boundaries (left and right). The boundary CFT$_2$ lives on a cylinder $\mathbb{R}_t \times S^1_\varphi$ on each boundary.

### 6.2 Boundary CFT and single-trace operators

For a holographic CFT$_2$ at large $N$, single-trace primaries $\mathcal{O}_\Delta$ of conformal dimension $\Delta$ have boundary two-point functions (in the BTZ thermal state):
$$
\langle\mathcal{O}_\Delta(t_1, \varphi_1)\,\mathcal{O}_\Delta(t_2, \varphi_2)\rangle_{\mathrm{BTZ}} \propto \frac{1}{[\cosh(\beta^{-1}(t_1 - t_2)) - \cos(\varphi_1 - \varphi_2)]^\Delta},
$$
with $\beta = 1/T_H$. This is the standard CFT$_2$ thermal correlator at inverse temperature $\beta$, computed by the conformal transformation from the plane to the cylinder.

The boundary single-trace algebra is generated by smearings $\mathcal{O}_\Delta(f) = \int d^2x\,f(x)\,\mathcal{O}_\Delta(x)$, with the GFF structure determined by the above two-point function.

### 6.3 Modular structure

The boundary subregion is the right asymptotic region $\{t \in \mathbb{R}, \varphi \in S^1\}$, with $r \to \infty$. The single-trace algebra is the GFF algebra at $N = \infty$.

The **TFD vacuum** at $\beta = \beta_H$ is the cyclic-separating state. The modular flow on the right algebra is $\sigma^{\mathrm{TFD}}_t = \alpha^{H_R}_{\beta_H t}$, the ADM time translation. This identification is checked at the level of two-point functions: the TFD two-point function is periodic in imaginary $t$ with period $\beta_H$, which is the KMS condition at inverse temperature $\beta_H$ for the ADM time flow.

The two-point function on the right side, restricted to one boundary, looks thermal at $\beta_H$. This is the holographic analog of "the Minkowski vacuum looks thermal at the Unruh temperature to a Rindler observer."

### 6.4 Type III$_1$ for the BTZ boundary subregion

**[Stated only — refs: Witten 2022 §2; Liu lectures §3.]** *Under the hypotheses of Theorem 4.1 (large-$N$ GFF + Rindler-like causal structure), the boundary single-trace algebra on the right asymptotic region of two-sided BTZ at large $N$ is a type III$_1$ factor.*

The argument follows the Sem I Wk 12 template: the modular flow has full real spectrum (the ADM Hamiltonian $H_R$ has unbounded spectrum on the GFF Hilbert space), so the modular S-invariant is $[0, \infty)$, and the algebra is III$_1$. The CFT conformal invariance plus large-$N$ factorization play the role of nuclearity + split property.

## 7. Discussion: $1/N$ as the gravitational expansion

A few interpretive remarks before Week 2's construction:

### 7.1 The two limits

- **$1/N = 0$:** classical gravity in the bulk; type III$_1$ boundary algebra; modular flow is outer (= ADM time, which is not an inner element of the boundary algebra).
- **$1/N > 0$:** quantum gravity in the bulk; type I boundary algebra; ADM Hamiltonian is inner.

The crossed-product construction (Week 2) lives at $1/N = 0$ but **dresses** the algebra to get a type II$_\infty$ algebra. This dressed algebra has a finite-trace structure that matches **semiclassical** gravity (leading order in $1/N$ around the classical solution).

### 7.2 Why this is the right framework

The Witten 2022 construction is a **structural** statement: the dressed entropy of the boundary algebra equals the generalized entropy of the bulk wedge, **regardless of the specific CFT or bulk theory**, as long as the large-$N$ + Bisognano–Wichmann-like structure holds.

This is the analog of "Bisognano–Wichmann holds for any Wightman QFT" (Sem I Wk 10). The universality of the construction is what makes it a structural anchor of the rest of Sem II.

### 7.3 What's missing (next-week preview)

The Witten 2022 setup gives us:

1. ✓ The algebra: boundary single-trace algebra at large $N$.
2. ✓ The flow: ADM time translation = modular flow.
3. ✗ The crossed product itself: not yet constructed.
4. ✗ The dressed entropy formula: not yet derived.
5. ✗ Identification with generalized entropy: Witten's key claim, pending.

Weeks 2–3 build the missing pieces. Week 4 verifies them in the free-field analog.

## 8. What to take away

- **Witten 2022 architecture (stated only, made structural):** at large $N$, the boundary single-trace algebra of a holographic CFT is type III$_1$; the modular flow of the TFD vacuum is the ADM time translation; the crossed product by this flow is type II$_\infty$ with a faithful normal semifinite trace; the dressed entropy equals the generalized entropy modulo a state-independent additive constant.
- **Large-$N$ factorization** turns single-trace operators into a Gaussian random field (GFF) at $N = \infty$. The boundary algebra is the GFF algebra.
- **Type III$_1$ at large $N$ is hypothesis-explicit:** requires GFF structure + Rindler/wedge-like causal structure + Bisognano–Wichmann-like modular flow. The holographic analog of nuclearity + split property.
- **$1/N$ plays the role of $\hbar$:** at $1/N = 0$, type III$_1$ on the boundary ↔ classical gravity in the bulk. At $1/N > 0$, type I ↔ quantum gravity. The dressed-algebra construction is intermediate, capturing semiclassical gravity.
- **Modular flow = ADM time** at large $N$ — the holographic generalization of Bisognano–Wichmann.
- **The free-field Rindler model (Sem I Wk 14–15) is the complete algebraic skeleton** of the Witten 2022 construction. Every step is parallel.

## 9. Looking ahead

Week 2 turns the setup into Witten's central construction: form the crossed product $\hat{\mathcal{A}}_R = \mathcal{A}_R \rtimes_{\mathrm{ADM}}\mathbb{R}$, verify the type promotion (III$_1 \to$ II$_\infty$) via Connes–Takesaki, and identify the trace. Week 3 derives the dressed entropy. Week 4 verifies every step in the free-field Rindler model where the calculation is fully explicit.

## 10. Problem set

**Core problems.**

**1. Wick contractions in a GFF.** For a generalized free field with two-point function $W(x, y)$, prove that
$$
\langle\mathcal{O}(x_1)\,\mathcal{O}(x_2)\,\mathcal{O}(x_3)\,\mathcal{O}(x_4)\rangle = W(x_1, x_2)W(x_3, x_4) + W(x_1, x_3)W(x_2, x_4) + W(x_1, x_4)W(x_2, x_3),
$$
i.e., the four-point function factorizes into the three Wick contractions. Compare with the free scalar field's four-point function (Sem I Wk 8).

**2. The 't Hooft expansion for $\mathrm{Tr}(\Phi^2)\,\mathrm{Tr}(\Phi^2)$.** In a $\mathrm{U}(N)$ matrix theory with $\Phi$ a Hermitian random matrix and Gaussian measure $e^{-N\,\mathrm{Tr}(\Phi^2)/2}$, compute the leading $1/N$ behavior of $\langle\mathrm{Tr}(\Phi^2)\,\mathrm{Tr}(\Phi^2)\rangle_{\mathrm{connected}}$. (*Hint:* the connected part is $O(N^0)$, while the disconnected is $O(N^2)$, illustrating large-$N$ factorization.)

**3. Identify the single-trace algebra in a finite-dim CFT.** Take a $\mathrm{U}(2)$ matrix model (which has $N = 2$). Explicitly compute the algebra generated by $\frac{1}{2}\mathrm{Tr}(\Phi)$ and $\frac{1}{2}\mathrm{Tr}(\Phi^2)$ acting on the Hilbert space of $2\times 2$ Hermitian matrices. Verify that this is a type I algebra (sub-algebra of $M_4(\mathbb{C})$ at most).

**4. BTZ two-point function.** Verify the BTZ thermal two-point function formula in §6.2 by conformal transformation: start from a planar CFT$_2$ with $W_{\mathrm{plane}}(x_1, x_2) \propto (x_{12})^{-2\Delta}$ and apply the conformal map to the cylinder at finite temperature.

**5. Read Witten 2022 §1–2.** Identify the precise definition of the boundary single-trace algebra Witten uses, the hypotheses he makes (analyticity, Bisognano–Wichmann-like properties), and the structural argument for type III$_1$. Compare with our Theorem 4.1.

**Starred problems.**

**6\*. Read Liu's §1–2.** Liu (arXiv:2510.07017) gives the most pedagogical exposition of "type III at large $N$." Identify Liu's key argument for why the single-trace algebra is type III at $N = \infty$. Compare with Witten's argument.

**7\*. KMS at $\beta_H$ for the TFD.** Show that the boundary TFD two-point function is periodic in imaginary $t$ with period $\beta_H$, and hence is KMS at $\beta_H$ for the ADM time flow. This is the holographic analog of "Minkowski vacuum is KMS at $\beta = 2\pi$ for the boost" (Sem I Wk 10).

**8\*. Finite-$N$ corrections.** Sketch the structure of $1/N$ corrections to the GFF correlators. Show that connected $k$-point functions for $k > 2$ scale as $1/N^{k-2}$, hence the algebra becomes non-Gaussian at finite $N$.

**9\*. The Leutheusser–Liu approach.** Read Leutheusser & Liu, arXiv:2110.05497, §§1–3. Identify their construction of the type-III boundary algebra and how it differs from Witten 2022's. In particular: where does the "type III emerges at large $N$" structurally come from in their framework?

**Project problems.**

**10. Self-contained writeup.** Write a 5-page exposition of the large-$N$ type-III$_1$ result for a non-specialist physics graduate student. Identify which steps are CFT input, which are large-$N$ structural arguments, and which are operator-algebraic. Cite Witten 2022 and Liu lectures.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 1. Last revised 2026-06-11.*
