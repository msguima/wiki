---
title: "Week 15 — The TFD and the Bridge to Semester II"
type: lecture-notes
course: syllabus
semester: 1
week: 15
block: D
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 10 (Bisognano-Wichmann), 12 (type III$_1$), 13-14 (crossed product, dressed entropy)
modified: 2026-06-11
---

# Week 15 — The TFD and the Bridge to Semester II

> *Semester I ends here. We have built the algebraic-QFT toolkit (Blocks A–C) and the crossed-product machinery (Block D). This week, we put them together in the specific construction that Semester II will use repeatedly: the **thermofield double** state. The TFD is the cyclic-separating vector for a two-sided pair of commuting algebras whose modular flow is the **boost** (in free QFT) or the **ADM Hamiltonian** (in holography). The TFD is what the eternal black hole's bulk geometry is dual to. Witten 2022, CPW 2022, and Ahmad–Jefferson 2025 all start here — by applying our Block D crossed-product machinery to a two-sided algebra in the TFD vacuum. **The entire Semester II program is one sentence: dress the modular flow of the TFD on a two-sided boundary algebra, and compute the dressed entropy.***

## 0. Reading

**Primary:**
- Maldacena, "Eternal black holes in anti-de Sitter," *JHEP* 04 (2003) 021, arXiv:hep-th/0106112 — the foundational TFD/eternal-BH identification.
- Chandrasekaran, Penington, Witten (CPW), "Large $N$ algebras and generalized entropy," arXiv:2209.10454 §§2–3 (the two-sided crossed-product story; Sem II Block 2).
- Witten, "Gravity and the crossed product," arXiv:2112.12828 §§2–3 (the single-sided story; Sem II Block 1).

**Secondary:**
- Israel, "Thermo-field dynamics of black holes," *Phys. Lett. A* 57 (1976) 107 — the original TFD construction.
- Haag, *Local Quantum Physics*, ch. V §1 (two-sided algebras and the TFD in algebraic terms).

**Optional research reading:**
- Maldacena & Susskind, "Cool horizons for entangled black holes," *Fortsch. Phys.* 61 (2013) 781, arXiv:1306.0533 (ER=EPR).
- Van Raamsdonk, "Building up spacetime with quantum entanglement," *Gen. Rel. Grav.* 42 (2010) 2323 (spacetime from entanglement).
- Liu, "Lectures on entanglement, von Neumann algebras, and emergence of spacetime," arXiv:2510.07017 (the Sem II Block 3 connective-tissue paper).

## 1. The thermofield double state

### 1.1 Definition (finite-dimensional)

Let $\mathcal{H}_R$ be a Hilbert space with Hamiltonian $H_R$ and orthonormal energy eigenbasis $|n\rangle_R$ with $H_R|n\rangle_R = E_n|n\rangle_R$. Double the system: $\mathcal{H}_{\mathrm{total}} = \mathcal{H}_R \otimes \mathcal{H}_L$ where $\mathcal{H}_L$ is a copy of $\mathcal{H}_R$ with basis $|n\rangle_L$.

**Definition 1.1.** The **thermofield double (TFD)** state at inverse temperature $\beta$ is
$$
|\mathrm{TFD}_\beta\rangle \;:=\; \frac{1}{\sqrt{Z(\beta)}}\,\sum_n e^{-\beta E_n/2}\,|n\rangle_R \otimes |n\rangle_L \;\in\; \mathcal{H}_R \otimes \mathcal{H}_L,
$$
where $Z(\beta) = \sum_n e^{-\beta E_n} = \mathrm{Tr}_{\mathcal{H}_R}(e^{-\beta H_R})$ is the partition function (assumed finite).

### 1.2 Properties

**Reduced state.** Tracing out $\mathcal{H}_L$:
$$
\rho_R = \mathrm{Tr}_{\mathcal{H}_L}(|\mathrm{TFD}_\beta\rangle\langle\mathrm{TFD}_\beta|) = \frac{e^{-\beta H_R}}{Z(\beta)},
$$
the **Gibbs state** at inverse temperature $\beta$. The TFD is a **purification** of the Gibbs state.

**Cyclic-separating.** For the right algebra $\mathcal{B}(\mathcal{H}_R) \otimes 1 \subset \mathcal{B}(\mathcal{H}_R \otimes \mathcal{H}_L)$, the vector $|\mathrm{TFD}_\beta\rangle$ is cyclic-separating (in finite dimensions, when all $e^{-\beta E_n/2} > 0$). By Week 5, this licenses Tomita–Takesaki.

**Modular operator.** By the standard type-I modular computation (Week 5 §5), the modular operator of $|\mathrm{TFD}_\beta\rangle$ for the right algebra is
$$
\Delta = \rho_R \otimes \rho_R^{-1} = \frac{e^{-\beta H_R}}{Z(\beta)} \otimes \frac{Z(\beta)}{e^{-\beta H_L}} = e^{-\beta(H_R - H_L)} \cdot (\text{constants}).
$$
The constants cancel under modular flow: $\sigma_t^{\mathrm{TFD}}(a) = \Delta^{-it}\,a\,\Delta^{it} = e^{i\beta t(H_R - H_L)}\,a\,e^{-i\beta t(H_R - H_L)}$.

**Modular Hamiltonian.** $K_{\mathrm{TFD}} = -\log\Delta = \beta(H_R - H_L) + \text{const}$. This is the **two-sided Hamiltonian** $H_R - H_L$, scaled by $\beta$.

### 1.3 What the TFD is (physically)

In statistical mechanics, the TFD is the **purification of the Gibbs state at temperature $1/\beta$**, with the purifying degree of freedom interpreted as a "fictitious copy" of the system. The two copies share entanglement; the entanglement entropy of either copy is the thermal entropy of the Gibbs state.

> **Physical picture: thermality = entanglement with an inaccessible copy.** The TFD makes a conceptual identity manifest: a thermal state is what an entangled pure state looks like when half of it is out of reach. The Boltzmann weights $e^{-\beta E_n}$ of the mixed Gibbs state become Schmidt coefficients $e^{-\beta E_n/2}$ of a pure state; tracing out the copy converts entanglement spectrum into thermal spectrum. Statistical ignorance and quantum entanglement are, for the observer confined to one side, *operationally indistinguishable*. There is also a constructive picture worth keeping in mind: the TFD is prepared by the **Euclidean path integral over half the thermal circle** — evolving for imaginary time $\beta/2$ from the identity produces precisely the weights $e^{-\beta E_n / 2}$. This is the same half-circle that appeared in Week 10's Euclidean reading of $\Delta^{1/2} = e^{-\pi K}$ (rotation by angle $\pi$ = half of $2\pi$): the Tomita operator's positive part *is* the half-thermal-circle evolution, and the TFD is its fixed vector. Modular theory, Euclidean preparation, and two-sided entanglement are one structure seen three ways.

In QFT (next subsection), the TFD acquires a *physical* interpretation: it is the Minkowski vacuum viewed across a two-sided Rindler split. The "fictitious copy" is the algebra of the *other* wedge.

In holography (§3), the TFD acquires a *gravitational* interpretation: it is the dual of the two-sided eternal AdS-Schwarzschild black hole. The two copies are the boundary algebras of the two asymptotic regions.

## 2. The TFD in QFT: free-field Rindler

### 2.1 The two-sided algebra

In the 2D massless free scalar, the right and left Rindler wedges $W_R, W_L$ are spacelike-separated and their local algebras commute:
$$
[\mathcal{A}(W_R), \mathcal{A}(W_L)] = 0.
$$
By Bisognano–Wichmann (Week 10), the modular flow on $\mathcal{A}(W_R)$ is the boost subgroup, generated by $K_R = \int_0^\infty x^1 T^{00}\,dx^1$ (where the integral is over the wedge). Similarly, the modular flow on $\mathcal{A}(W_L)$ is generated by $K_L = -\int_{-\infty}^0 (-x^1) T^{00}\,dx^1$.

### 2.2 The Minkowski vacuum is a TFD

**Theorem 2.1 (Bisognano–Wichmann TFD identification). [Stated only — refs: Bisognano–Wichmann 1975; Haag ch. V §1.]** *The Minkowski vacuum $|0_M\rangle$, restricted to the combined algebra $\mathcal{A}(W_R) \otimes \mathcal{A}(W_L)$, is cyclic-separating, and its modular operator for the right algebra $\mathcal{A}(W_R)$ is*
$$
\Delta_{\mathrm{Mink}}^{(W_R)} = e^{-2\pi (K_R - K_L)},
$$
*so the modular Hamiltonian is $K_{\mathrm{Mink}} = 2\pi(K_R - K_L)$, the boost generator in our convention.*

This is the **two-sided** version of Bisognano–Wichmann (Week 10). The Minkowski vacuum *is* the TFD of the boost Hamiltonian at Rindler "temperature" $T = 1/(2\pi)$.

In physical units, taking a Rindler observer with acceleration $a = 1$ (lapse $\xi_0 = 1$), the Rindler "temperature" $2\pi$ is the Unruh temperature, and the TFD identification is the algebraic content of the Unruh effect.

### 2.3 What we have

Combining the structural pieces:

| Object | Free scalar on Rindler-Rindler | Holographic eternal BH |
|---|---|---|
| Two-sided algebra | $\mathcal{A}(W_R), \mathcal{A}(W_L)$ | $\mathcal{A}_R, \mathcal{A}_L$ (large-$N$ single-trace) |
| Cyclic-separating vector | Minkowski vacuum $\lvert 0_M\rangle$ | TFD of dual CFT |
| Modular Hamiltonian | $K_R - K_L$ (boost) | $H_R - H_L$ (ADM) |
| Modular flow | Boost subgroup | ADM-time translation |
| Algebra type | type III$_1$ | type III$_1$ (large-$N$) |
| Modular crossed product | $\hat{\mathcal{A}}_R = \mathcal{A}(W_R) \rtimes_{\mathrm{boost}}\mathbb{R}$ | $\hat{\mathcal{A}}_R$ (Witten 2022) |
| Dressed algebra type | type II$_\infty$ | type II$_\infty$ |
| Dressed entropy | Area law via boost | $A/(4G_N) + S_{\mathrm{out}}$ |

**This table is the entire structure of Sem II in compact form.** Each entry on the holography side is what Sem II Blocks 1, 2, 4 develop in detail. Each entry on the free-field side is the model verification that the holographic side is right.

## 3. The eternal black hole and gravity

### 3.1 The maximally-extended AdS-Schwarzschild geometry

The maximally-extended AdS-Schwarzschild geometry has two asymptotic boundaries connected by an Einstein-Rosen bridge. Each boundary supports a copy of the dual CFT. The two boundaries are causally disconnected (no observer in one boundary can signal to the other), but the bulk *geometry* connects them through the wormhole.

The geometry has:
- a **bifurcation surface** at the center of the wormhole (the horizon at the "tip" of the Penrose diagram);
- a **right asymptotic region** with its own CFT;
- a **left asymptotic region** with its own CFT;
- a **future interior** and a **past interior** behind the horizon.

### 3.2 Maldacena's identification

**Theorem 3.1 (Maldacena 2001). [Stated only — refs: Maldacena, *JHEP* 04 (2003) 021.]** *The two-sided eternal AdS-Schwarzschild black hole is dual to the dual-CFT in the TFD state*
$$
|\mathrm{BH}\rangle \;\leftrightarrow\; |\mathrm{TFD}_{\beta_H}\rangle_{\mathrm{CFT}_R \otimes \mathrm{CFT}_L},
$$
*where $\beta_H = 2\pi r_H / (\text{constants})$ is the inverse Hawking temperature.*

This is the holographic counterpart of the Bisognano–Wichmann TFD identification (Theorem 2.1). It says: gravitational thermal physics in the bulk = TFD physics on the boundary.

> **Physical picture.** The dictionary between §2 and §3 is tighter than an analogy — it is the same modular geometry at two scales. Near its bifurcation surface, the eternal black hole *is* Rindler space: the near-horizon metric is flat, the Killing horizon is a Rindler horizon, and Hawking temperature is Unruh temperature measured at the redshifted asymptotic clock. What Maldacena's identification adds is *global, two-sided* content: the entanglement pattern of the TFD between the two boundary CFTs is dual to the *geometric connectedness* of the bulk (the Einstein–Rosen bridge). Disentangle the two CFTs (replace TFD by a product of two thermal states) and the bridge pinches off — two disconnected spacetimes. This is the seed of ER=EPR and Van Raamsdonk's "spacetime from entanglement": the wormhole's spatial connectivity is the geometrization of the Schmidt coefficients $e^{-\beta E_n/2}$. In algebraic terms — the language this course supplies — the bulk geometry is dual to the *modular structure* of the boundary pair $(\mathcal{A}_R, \mathcal{A}_L, |\mathrm{TFD}\rangle)$, with the horizon at the fixed locus of the modular flow.

### 3.3 The boundary algebras are type III$_1$

At large $N$ (the classical-gravity limit), the algebras of single-trace operators on each boundary CFT are type III$_1$ — by the standard hypothesis-explicit type-III$_1$ universality theorem (Week 12). The TFD is their cyclic-separating vector.

The modular flow on the right algebra $\mathcal{A}_R$, in the TFD vacuum, is the **time-translation by the ADM Hamiltonian** of the right asymptotic region — analogous to how the modular flow on $\mathcal{A}(W_R)$ in the Minkowski vacuum is the boost.

(This identification — modular flow = ADM Hamiltonian — at large $N$ requires the holographic CFT setup; it is the central insight of Witten 2022 and is developed in Sem II Block 1.)

### 3.4 The dressed algebra is the gravitational algebra

Applying our Block D crossed-product construction:
$$
\hat{\mathcal{A}}_R \;:=\; \mathcal{A}_R \rtimes_{\sigma^{\mathrm{TFD}}}\mathbb{R} \;=\; \mathcal{A}_R \rtimes_{\mathrm{ADM\,time}}\mathbb{R}
$$
is a type II$_\infty$ algebra. Witten's central claim:

**Theorem 3.2 (Witten 2022). [Stated only — refs: Witten 2112.12828 §§3–4.]** *In the large-$N$ holographic CFT, the dressed algebra $\hat{\mathcal{A}}_R$ is the algebra of gravitationally dressed observables associated to the right asymptotic region. Its dressed entropy reproduces the generalized entropy:*
$$
S_{\mathrm{vN}}(\hat\rho) \;=\; \frac{A_{\mathrm{horizon}}}{4 G_N} + S_{\mathrm{out}}(\rho) + \text{const}.
$$

**Two distinct claims, carefully separated.** First, the *operator-algebraic* construction: take a type III$_1$ algebra $\mathcal{A}_R$ with modular flow $\sigma^{\mathrm{TFD}}_t$ and form the crossed product $\hat{\mathcal{A}}_R = \mathcal{A}_R \rtimes_{\sigma^{\mathrm{TFD}}}\mathbb{R}$ — a type II$_\infty$ algebra with dressed entropy $S_{\mathrm{vN}}(\hat\rho)$ well-defined up to additive constant. This is Block D, no gravity yet.

Second, the *holographic identification*: in the large-$N$ limit of a holographic CFT, the modular flow of the TFD on the boundary single-trace algebra is the ADM-time-translation, and the dressed entropy equals the generalized entropy $A/(4G_N) + S_{\mathrm{out}} + \mathrm{const}$. This identification requires the holographic dictionary, the large-$N$ limit, and the AdS/CFT framework — it is a **physics input** beyond the operator-algebraic construction.

Witten 2022's contribution is the identification, not the algebraic construction. The algebraic construction is structural (Connes–Takesaki, Week 13); the holographic identification is the physical content that makes it apply to gravity. **The crossed product is not literally "the gravitational dressing"** at the operator-algebra level — it is the algebraic construction that, in the holographic setting, *equals* the gravitational dressing of observables modulo bulk gauge constraints. The equality is a theorem of holographic QFT, not of operator algebras alone.

## 4. Two-sided CPW: Sem II Block 2

The CPW (Chandrasekaran–Penington–Witten) construction of Sem II Block 2 is the two-sided version of Witten 2022. The setup is identical except:
- The dressing operator is $H_R - H_L$ (the two-sided ADM Hamiltonian) instead of just $H_R$.
- The cyclic-separating vector is the TFD vacuum.
- The dressed algebra is type II$_\infty$, with the modular flow now identified with $\beta_H(H_R - H_L)$.
- The dressed entropy is the generalized entropy with the area term coming from the bifurcation-surface horizon.

The structural equivalence with the free-field Rindler-Rindler model (§2 above) is exact: replace boost by ADM, replace bifurcation surface by black-hole horizon, replace area law by gravitational area-times-$1/(4G_N)$.

## 5. Ahmad–Jefferson: Sem II Block 4

The Ahmad–Jefferson (AAJ) construction of Sem II Block 4 is **perturbations** of the CPW dressed-entropy story. The setup:

1. Start with the unperturbed TFD vacuum + dressed algebra $\hat{\mathcal{A}}_R$ + dressed entropy $S_{\mathrm{vN}}(\hat\rho_{\mathrm{TFD}})$.
2. Perturb by a **Gao–Jafferis–Wall deformation**: a double-trace operator $V = g\,\mathcal{O}_L\,\mathcal{O}_R$ that *traversifies* the wormhole.
3. The perturbed state $\omega_V$ is related to the unperturbed state $\omega_0$ by the **Connes cocycle** (Week 7): $u_t = (D\omega_V / D\omega_0)_t$.
4. The perturbed dressed entropy is computed to order $g^2$ — and AAJ identify **20 distinct corrections** at this order.

AAJ's central technical input is exactly the **Connes cocycle** from Week 7. Their machinery is **perturbation theory on the dressed algebra**, with the cocycle as the expansion parameter. The structural picture is the Block D crossed product of Weeks 13–14, perturbed.

## 6. Worked computation: Minkowski vacuum as TFD

A concrete verification of Theorem 2.1 in the 2D massless free scalar.

### 6.1 Modes on Rindler-Rindler

In 2D massless, the field decomposes into right- and left-movers. We focus on the right-mover; the left-mover is identical with $x^- \leftrightarrow x^+$. Inside $W_R$, the right-mover has Rindler modes $b_\omega^R$ with $\omega > 0$ (Week 10 §4); inside $W_L$, Rindler modes $b_\omega^L$.

### 6.2 Bogoliubov coefficients

The Minkowski annihilation operator $a_k$ and the Rindler operators $b_\omega^R, b_\omega^L$ are related by Bogoliubov transformations:
$$
a_k = \int_0^\infty d\omega \left[ \tilde\alpha^R_{k\omega}\,b_\omega^R + \tilde\beta^R_{k\omega}\,(b_\omega^R)^\dagger + \tilde\alpha^L_{k\omega}\,b_\omega^L + \tilde\beta^L_{k\omega}\,(b_\omega^L)^\dagger \right],
$$
with the same $e^{\pi\omega/2}$ vs $e^{-\pi\omega/2}$ ratios as Week 10 §4.3.

### 6.3 The Minkowski vacuum in Rindler modes

The condition $a_k|0_M\rangle = 0$ for all $k$ translates, after the Bogoliubov transformation, to a constraint on the Rindler-mode content of $|0_M\rangle$. Solving:
$$
|0_M\rangle \;=\; \prod_{\omega > 0} \frac{1}{\sqrt{Z_\omega}}\,\sum_n e^{-\pi n\omega}\,\frac{(b_\omega^L^\dagger b_\omega^R^\dagger)^n}{n!}\,|0_R\rangle\otimes|0_L\rangle,
$$
or, recasting in terms of two-sided number eigenstates $|n_\omega\rangle_R \otimes |n_\omega\rangle_L$ (using that $b^\dagger_R b^\dagger_L$ creates one quantum on each side):
$$
|0_M\rangle = \prod_\omega \frac{1}{\sqrt{Z_\omega}}\,\sum_{n_\omega} e^{-\pi n_\omega\,\omega}\,|n_\omega\rangle_R\otimes|n_\omega\rangle_L.
$$

This is *exactly* the TFD form (Definition 1.1) with $E_n = n\omega$ and $\beta = 2\pi$ (per mode). The Minkowski vacuum *is* the TFD of the Rindler-mode Hamiltonian, at the Unruh-temperature $T_U = 1/(2\pi)$ (in Rindler units; $T_U = a/(2\pi)$ in physical units).

### 6.4 Modular operator from the TFD form

Given the TFD form (§6.3), the modular operator is computed via the standard type-I bipartite-state modular calculation (Week 5 §5.2):
$$
\Delta = \prod_\omega \rho_\omega^R \otimes (\rho_\omega^L)^{-1} = e^{-2\pi (N_R - N_L)},
$$
where $N_R = \int d\omega\,\omega\,(b^R_\omega)^\dagger b^R_\omega$ is the Rindler-mode-number Hamiltonian on the right (and similarly $N_L$ on the left). The modular Hamiltonian is $K_{\mathrm{Mink}} = 2\pi(N_R - N_L)$.

Identifying $N_R$ with the boost generator $K_R$ (which it equals modulo regularization, since both are integrals of the stress tensor weighted by $x^1$ inside $W_R$), we recover Theorem 2.1: $\Delta_{\mathrm{Mink}}^{(W_R)} = e^{-2\pi(K_R - K_L)}$.

### 6.5 What this confirms

The free-field Rindler-Rindler model **explicitly verifies** that:
- The Minkowski vacuum is the TFD of the boost Hamiltonian at $\beta = 2\pi$.
- Its modular Hamiltonian is $K_R - K_L$ (the two-sided boost generator).
- The modular flow is the joint left/right boost at modular rapidity $2\pi t$.

This is the model that all of Sem II Block 2 (CPW) generalizes to the holographic eternal black hole. The substitutions:
- Boost generator $K_R - K_L$ $\leftrightarrow$ ADM Hamiltonian $H_R - H_L$.
- $\beta = 2\pi$ Unruh $\leftrightarrow$ $\beta_H$ Hawking.
- Bifurcation surface (Minkowski's $\{x^0 = x^1 = 0\}$) $\leftrightarrow$ BH horizon (the Schwarzschild bifurcation sphere).
- 2D massless free scalar $\leftrightarrow$ holographic CFT at large $N$.

## 7. Sem II in one sentence

Combining Block D with the TFD identification:

> **Semester II = "apply the modular crossed product (Week 13) to a two-sided algebra in the TFD vacuum (this week), compute the dressed entropy (Week 14), and identify it with the generalized entropy of a bulk gravitational dual."**

Each Sem II Block tackles a specific instance:

- **Block 1 (Witten 2022):** single-sided story; dressed algebra of a single boundary algebra; dressed entropy = $A_{\mathrm{horizon}}/(4G_N) + S_{\mathrm{out}}$.
- **Block 2 (CPW):** two-sided story; TFD vacuum; same crossed product applied to the eternal BH; dressed entropy = same generalized entropy.
- **Block 3 (Liu lectures):** structural overview; modular flow ↔ bulk Killing flow dictionary; algebraic ER=EPR.
- **Block 4 (AAJ):** perturbations of the dressed entropy via Connes cocycle; 20 distinct corrections at order $g^2$ from a GJW deformation.
- **Block 5 (MSY + outlook):** bulk-side complement; honest scoping; what the algebra sees and what it doesn't.

Each block uses the Block D + Week 15 toolkit. **Semester I has built every algebraic ingredient needed for Semester II.**

## 8. What to take away

- **TFD definition:** $|\mathrm{TFD}_\beta\rangle = Z(\beta)^{-1/2}\sum_n e^{-\beta E_n/2}|n\rangle_R\otimes|n\rangle_L$, a purification of the Gibbs state.
- **Modular structure of TFD:** $\Delta = \rho_R \otimes \rho_R^{-1}$, modular Hamiltonian $K = \beta(H_R - H_L)$ (up to additive constant).
- **Stated only (Theorem 2.1):** the Minkowski vacuum in 2D free scalar is the TFD of the boost Hamiltonian at $\beta = 2\pi$; modular flow = two-sided boost.
- **Stated only (Theorem 3.1, Maldacena):** the two-sided eternal BH is dual to the boundary CFT in the TFD state at Hawking temperature.
- **Stated only (Theorem 3.2, Witten 2022):** dressed algebra (crossed product by ADM time) is type II$_\infty$ with dressed entropy = generalized entropy.
- **Worked verification (free-field Rindler-Rindler, §6):** the Minkowski vacuum has the explicit TFD form in Rindler modes, with modular Hamiltonian $K_R - K_L$.
- **The Sem II structural picture:** dress the modular flow of the TFD on a two-sided algebra; dressed entropy is the generalized entropy. Every Sem II paper applies this to a specific physical setting.

## 9. The take-home final

A take-home final is assigned at the end of Week 15, due 4 weeks later (over the break before Sem II). It consolidates Sem I and lands students at the toolkit they need for Sem II Block 1.

**Problem 1: Modular operator for 4D massless scalar.** Compute the modular operator and Bisognano–Wichmann boost flow for the 4D massless free scalar restricted to the right Rindler wedge $W_R = \{x: x^1 > |x^0|\}$. (Generalize the 2D calculation of Week 10 §4.)

**Problem 2: Connes cocycle for vacuum vs. coherent state.** For the 2D massless free scalar on $W_R$, compute the Connes cocycle $u_t = (D\omega_\alpha / D\omega_0)_t$ between the Minkowski vacuum $\omega_0$ and a coherent state $\omega_\alpha$ obtained by Weyl-operator dressing: $|\alpha\rangle = e^{i\phi(f)}|0_M\rangle$ for a test function $f \in W_R$. Express $u_t$ in terms of $f$ and the boost generator.

**Problem 3: Crossed product trace formula.** Construct the crossed product $\hat{\mathcal{A}}(W_R) = \mathcal{A}(W_R) \rtimes_{\mathrm{boost}}\mathbb{R}$ for the 2D massless free scalar. Verify the trace formula
$$
\hat\tau(a) = \int e^{-2\pi s}\,\langle 0_M \otimes \delta_s\,|\,a\,|\,0_M \otimes \delta_s\rangle\,ds
$$
on a dense subspace of operators of the form $a = W(f) \otimes g(X)$ with $f \in W_R$ and $g$ bounded.

**Problem 4: Bell-CHSH on the TFD vacuum.** For the TFD vacuum on the two-sided Rindler-Rindler algebra in 2D massless free scalar, compute $\langle\mathcal{C}_{\mathrm{CHSH}}\rangle$ between $\mathcal{A}(W_R)$ and $\mathcal{A}(W_L)$ for an optimized choice of cosine-Weyl observables (Week 11 §4). Verify approach to Tsirelson saturation as the test functions are boosted toward the bifurcation surface.

**Problem 5 (⋆): Dressed entropy difference for coherent state.** Compute the dressed-entropy difference between the vacuum and a coherent state on the crossed product algebra of Problem 3:
$$
S_{\mathrm{vN}}(\hat\rho_\alpha) - S_{\mathrm{vN}}(\hat\omega_0) = -S(\omega_\alpha\|\omega_0) + \mathcal{B}(\omega_\alpha, \omega_0).
$$
Compute each side explicitly to leading order in $|\alpha|$ and verify Theorem 3.1 of Week 14.

### Why these five problems

Each problem will reappear in Sem II, expanded and applied to specific papers:

- **Problem 1** generalizes to higher dimensions (4D massless is the standard setting of CPW and AAJ).
- **Problem 2** is the structural input for AAJ's perturbation expansion.
- **Problem 3** is *the* mini-calculation that Witten 2022, CPW, and AAJ all use as a free-field analogue.
- **Problem 4** is the technical setup for the open question "Bell-CHSH in holographic settings."
- **Problem 5** is the central technical content of AAJ's leading-order result.

After the take-home final, students enter Sem II with everything in hand.

## 10. End of Semester I

Sem I has built the algebraic-QFT toolkit needed to read the recent research literature. Students enter Sem II equipped with:

- **Block A** (Weeks 1–4): C\*-algebras, von Neumann algebras, type classification (I, II, III), KMS condition, Powers factor.
- **Block B** (Weeks 5–7): Tomita–Takesaki theorem, modular flow, KMS for the modular flow, Connes cocycle, Araki–Uhlmann relative entropy.
- **Block C** (Weeks 8–12): Free-field algebras, Weyl operators, Reeh–Schlieder, Bisognano–Wichmann, Bell–CHSH, type III$_1$ classification.
- **Block D** (Weeks 13–15): Crossed product, dressed trace and dressed entropy, modular boundary term, TFD bridge to gravity.

This is enough to begin Sem II Block 1 (Witten 2022) without further algebraic background. The remaining work in Sem II is **physical**: identifying the right modular flow in each holographic setting, identifying the right two-sided algebra, identifying the right perturbation, and connecting the dressed entropy to bulk geometric quantities.

## 11. Problem set (additional to the take-home final)

**Core problems.**

**1. TFD reduced state.** Verify that $\mathrm{Tr}_L(|\mathrm{TFD}_\beta\rangle\langle\mathrm{TFD}_\beta|) = e^{-\beta H_R}/Z(\beta)$ in finite dimensions.

**2. Modular operator of the finite-dim TFD.** Compute the modular operator $\Delta$ of $|\mathrm{TFD}_\beta\rangle$ for the right algebra $\mathcal{B}(\mathcal{H}_R) \otimes 1$. Verify $\Delta = (e^{-\beta H_R}/Z) \otimes (e^{-\beta H_L}/Z)^{-1}$ and $K = -\log\Delta = \beta(H_R - H_L) + 2\log Z$.

**3. Mode-by-mode TFD form of Minkowski vacuum.** Expand the formula §6.3 to order $n_\omega = 1$ and identify the structure: $|0_M\rangle \approx \prod_\omega(1 + e^{-\pi\omega}\,b^R_\omega{}^\dagger b^L_\omega{}^\dagger + O(e^{-2\pi\omega}))|0_R\rangle\otimes|0_L\rangle$.

**4. Two-sided modular flow.** Show that the modular flow on $\mathcal{A}(W_R)$ in the Minkowski vacuum, when extended to the two-sided algebra, is the joint flow generated by $K_R - K_L$. Specifically: $\sigma_t^{\mathrm{Mink}}(a_R \otimes 1) = (\text{boost}_t a_R) \otimes 1$ and $\sigma_t^{\mathrm{Mink}}(1 \otimes a_L) = 1 \otimes (\text{boost}_{-t} a_L)$.

**5. Reading bridge.** Read Maldacena 2003 §§1–3 (the eternal-BH/TFD identification). Identify the key claim and the level of evidence Maldacena gives.

**Starred problems.**

**6\*. Modular Hamiltonian on a one-sided thermal state.** For the Gibbs state $\rho_\beta = e^{-\beta H}/Z$ on a finite-dim system, viewed as a state on $\mathcal{B}(\mathcal{H})$, the modular Hamiltonian is $K_\beta = \beta H + \log Z$. Show that the dressed entropy of the Gibbs state, computed via the modular crossed product, is
$$
S_{\mathrm{vN}}(\hat\rho_{\beta, \mathrm{dressed}}) = S_{\mathrm{thermal}}(\beta) + (\text{clock contribution}),
$$
where $S_{\mathrm{thermal}}(\beta) = -\mathrm{Tr}(\rho_\beta\log\rho_\beta) = \beta\langle H\rangle_\beta + \log Z$ is the standard thermal entropy.

**7\*. ER=EPR (heuristic).** The Maldacena–Susskind ER=EPR proposal says that two boundary CFTs are "Einstein-Rosen-bridge-connected" in the bulk iff they share a TFD-like entangled state. Discuss informally: how does this manifest at the algebraic level (in terms of cyclic-separating vectors and modular structures)?

**8\*. Generalized entropy in 2D toy model.** In the 2D Jackiw-Teitelboim (JT) gravity model, the bulk has a specific algebraic dual. Look up the dressed-algebra structure and verify that the dressed entropy reproduces the JT generalized entropy.

**Project problems.**

**9. Read Witten 2022 in full.** Identify how each ingredient of our Block D (crossed product, dual action, dressed entropy, area law) maps onto Witten's exposition.

**10. Read CPW 2022 in full.** Identify the difference between Witten's single-sided story and CPW's two-sided TFD story. What does the two-sidedness add structurally?

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block D. Last revised 2026-06-11. **End of Semester I.***
