---
title: "Week 15 — The TFD and the Bridge to Semester II"
type: lecture-notes
course: syllabus
semester: 1
week: 15
block: D
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 10 (Bisognano-Wichmann), 12 (type III$_1$), 13-14 (crossed product, dressed entropy)
modified: 2026-08-24
---

# Week 15 — The TFD and the Bridge to Semester II

> *Semester I ends with the thermofield double, the finite-dimensional model that makes modular theory visible as a matrix calculation. We will then separate this literal tensor-product construction from its type III counterpart. In QFT the vacuum is cyclic and separating for one wedge algebra, the opposite wedge is its commutant, and the modular flow is geometric; there is no density matrix for either wedge and no literal Hilbert-space factorization into left and right Rindler factors. This distinction is the bridge to Semester II: Witten and CPW retain the modular structure of the TFD while replacing the type-I tensor product by a type-III standard form and then by its continuous core.*

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

### 0.1 How to use this master dossier

- **Classroom core:** §§1–4 and the take-home Problems 1–3. This route moves from the literal finite-dimensional TFD to the one-sided type-III standard form and then to Witten/CPW.
- **Full derivation / self-study:** §§5–6, take-home Problems 4–5, and additional Problems 1–7. This route checks the regulated Rindler-mode analogy, unitary cancellation, and the AAJ-method distinction.
- **Research extension:** §§7–10 and additional Problems 8–10. This route turns the Semester I toolkit into source-audited Semester II projects.

The central comparison is deliberately asymmetric: the finite-dimensional TFD is a model one can calculate with, while the continuum wedge theorem is the structural result one is allowed to export.

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
\Delta = \rho_R \otimes \rho_L^{-1}
= \frac{e^{-\beta H_R}}{Z(\beta)} \otimes Z(\beta)e^{\beta H_L}
= e^{-\beta(H_R-H_L)}.
$$
The constants cancel under modular flow: $\sigma_t^{\mathrm{TFD}}(a) = \Delta^{-it}\,a\,\Delta^{it} = e^{i\beta t(H_R - H_L)}\,a\,e^{-i\beta t(H_R - H_L)}$.

**Modular Hamiltonian.** The normalization constants cancel exactly:
$$
K_{\mathrm{TFD}}=-\log\Delta=\beta(H_R-H_L).
$$
It is the two-sided Hamiltonian difference, scaled by $\beta$.

### 1.3 What the TFD is (physically)

In statistical mechanics, the TFD is the **purification of the Gibbs state at temperature $1/\beta$**, with the purifying degree of freedom interpreted as a "fictitious copy" of the system. The two copies share entanglement; the entanglement entropy of either copy is the thermal entropy of the Gibbs state.

> **Physical picture: thermality = entanglement with an inaccessible copy.** The TFD makes a conceptual identity manifest: a thermal state is what an entangled pure state looks like when half of it is out of reach. The Boltzmann weights $e^{-\beta E_n}$ of the mixed Gibbs state become Schmidt coefficients $e^{-\beta E_n/2}$ of a pure state; tracing out the copy converts entanglement spectrum into thermal spectrum. Statistical ignorance and quantum entanglement are, for the observer confined to one side, *operationally indistinguishable*. There is also a constructive picture worth keeping in mind: the TFD is prepared by the **Euclidean path integral over half the thermal circle** — evolving for imaginary time $\beta/2$ from the identity produces precisely the weights $e^{-\beta E_n / 2}$. This is the same half-circle that appeared in Week 10's Euclidean reading of $\Delta^{1/2} = e^{-\pi K}$ (rotation by angle $\pi$ = half of $2\pi$): the Tomita operator's positive part *is* the half-thermal-circle evolution, and the TFD is its fixed vector. Modular theory, Euclidean preparation, and two-sided entanglement are one structure seen three ways.

In QFT, the analogy becomes structural rather than literal. The opposite wedge supplies the commutant of the right-wedge algebra, and the vacuum supplies its cyclic-separating vector. A mode regulator can turn this into an ordinary TFD tensor product, but the continuum theory itself does not factorize in that way.

In holography (§3), the TFD acquires a *gravitational* interpretation: it is the dual of the two-sided eternal AdS-Schwarzschild black hole. The two copies are the boundary algebras of the two asymptotic regions.

## 2. The TFD in QFT: free-field Rindler

### 2.1 The two-sided algebra

In the 2D massless free scalar, the right and left Rindler wedges $W_R,W_L$ are spacelike separated and their local algebras commute:
$$
[\mathcal{A}(W_R), \mathcal{A}(W_L)] = 0.
$$
By Bisognano–Wichmann (Week 10), the modular flow on $\mathcal A(W_R)$ is implemented in the vacuum representation by the **global** Lorentz-boost generator $K_{\rm boost}$. A regulated stress-tensor calculation may split it into right and left pieces proportional to integrals of $x^1T_{00}$ over the two half-spaces. In the continuum, however, those one-sided pieces need not exist as operators in the wedge algebras; the global boost unitary and the modular operator are the invariant objects.

### 2.2 The type III statement behind the TFD analogy

**Theorem 2.1 (Bisognano–Wichmann, one-sided standard form). [Stated only — refs: Bisognano–Wichmann 1975; Haag ch. V.]** *The Minkowski vacuum $|0_M\rangle$ is cyclic and separating for the right-wedge algebra $\mathcal A(W_R)$. With the course convention,*
$$
\Delta_{W_R}=e^{-2\pi K_{\rm boost}},
\qquad
\sigma_t(a)=e^{i2\pi tK_{\rm boost}}a e^{-i2\pi tK_{\rm boost}},
$$
*and, assuming wedge duality,*
$$
J\mathcal A(W_R)J=\mathcal A(W_R)'=\mathcal A(W_L).
$$

The cyclic-separating statement is for the **one-sided algebra** $\mathcal A(W_R)$, not for the joined algebra $\mathcal A(W_R)\vee\mathcal A(W_L)$. Under wedge duality the joined algebra is irreducible, typically $\mathcal B(\mathcal F)$, and no vector is separating for $\mathcal B(\mathcal F)$ when $\dim\mathcal F>1$.

The theorem has the same modular pattern as the finite-dimensional TFD: the commutant plays the role of the second side, and modular conjugation exchanges the sides. It is nevertheless misleading to write a continuum density matrix $e^{-2\pi K_R}/Z$ or to treat the Fock space as $\mathcal F_R\otimes\mathcal F_L$. Those objects appear only after a regulator or a modewise formalization.

In physical units, a uniformly accelerated observer with proper acceleration $a$ detects the Unruh temperature $T_U=a/(2\pi)$, so the inverse temperature is $\beta_U=2\pi/a$.

### 2.3 What we have

Combining the structural pieces:

| Object | Free scalar on Rindler-Rindler | Holographic eternal BH |
|---|---|---|
| Two-sided algebra | $\mathcal{A}(W_R), \mathcal{A}(W_L)$ | $\mathcal{A}_R, \mathcal{A}_L$ (large-$N$ single-trace) |
| Cyclic-separating vector | Minkowski vacuum for $\mathcal A(W_R)$ | TFD standard vector for the right algebra |
| Modular Hamiltonian | $2\pi K_{\rm boost}$; no separate continuum $K_R,K_L$ operators | $\beta_H\widehat H$, with $\widehat H=H_R-H_L$ well-defined in the TFD representation |
| Modular flow | Boost subgroup | ADM-time translation |
| Algebra type | type III$_1$ | type III$_1$ (large-$N$) |
| Modular crossed product | $\hat{\mathcal{A}}_R = \mathcal{A}(W_R) \rtimes_{\mathrm{boost}}\mathbb{R}$ | $\hat{\mathcal{A}}_R$ (Witten 2022) |
| Dressed algebra type | type II$_\infty$ | type II$_\infty$ |
| Core entropy | Trace entropy, when defined; matter UV law remains separate | $A/(4G_N) + S_{\mathrm{out}}+\mathrm{const}$ for the stated semiclassical construction |

This table is the structural bridge to Semester II. The free-field side verifies modular geometry and the type of the core; it does not by itself verify the gravitational coefficient $1/(4G_N)$.

## 3. The eternal black hole and gravity

### 3.1 The maximally-extended AdS-Schwarzschild geometry

The maximally-extended AdS-Schwarzschild geometry has two asymptotic boundaries connected by an Einstein-Rosen bridge. Each boundary supports a copy of the dual CFT. The two boundaries are causally disconnected (no observer in one boundary can signal to the other), but the bulk *geometry* connects them through the wormhole.

The geometry has:
- a **bifurcation surface** at the center of the wormhole (the horizon at the "tip" of the Penrose diagram);
- a **right asymptotic region** with its own CFT;
- a **left asymptotic region** with its own CFT;
- a **future interior** and a **past interior** behind the horizon.

### 3.2 Maldacena's identification

**Holographic identification 3.1 (Maldacena 2001). [Dictionary statement, not a mathematical theorem — ref: Maldacena, *JHEP* 04 (2003) 021.]** *The two-sided eternal AdS-Schwarzschild black hole is dual to the doubled CFT in the TFD state*
$$
|\mathrm{BH}\rangle \;\leftrightarrow\; |\mathrm{TFD}_{\beta_H}\rangle_{\mathrm{CFT}_R \otimes \mathrm{CFT}_L},
$$
*where $\beta_H=T_H^{-1}=2\pi/\kappa$ in terms of the horizon surface gravity $\kappa$.*

This has the same thermal/modular pattern as Bisognano–Wichmann, but it is a statement of the AdS/CFT dictionary rather than a consequence of the wedge theorem.

> **Physical picture.** Near a smooth bifurcate Killing horizon, the geometry is locally Rindler and Hawking temperature is the redshifted counterpart of Unruh temperature. Maldacena's construction adds global two-sided information: the TFD state is dual to the connected eternal-black-hole saddle. This motivates the broader idea that entanglement participates in bulk connectivity. It does not prove that continuously reducing boundary entanglement produces a smooth geometric “pinch-off,” nor that an arbitrary entangled state has a wormhole dual. Those are questions about the gravitational state and the code subspace, not consequences of Tomita–Takesaki theory.

### 3.3 The boundary algebras are type III$_1$

In the Leutheusser–Liu large-$N$ construction, the noncentral single-trace algebra on one side is a type III$_1$ factor and the TFD vector is cyclic and separating for it. This is a specific large-$N$ operator-algebraic limit, not a theorem that every large-$N$ single-trace algebra in every state is type III$_1$.

The modular operator satisfies $\Delta=e^{-\beta_H\widehat H}$ with $\widehat H=H_R-H_L$ well-defined in the TFD representation. On right-algebra elements its automorphism acts as right-boundary time translation. The individual $H_R$ and $H_L$ need not exist as operators in the strict large-$N$ TFD representation.

(This physical link between modular flow, boundary time, and the ADM-energy collective coordinate requires the holographic large-$N$ setup; it is developed in Witten 2022 and in Sem II Block 1.)

### 3.4 The dressed algebra is the gravitational algebra

Applying our Block D crossed-product construction gives
$$
\hat{\mathcal{A}}_R
:=
\mathcal{A}_R\rtimes_{\sigma^{\mathrm{TFD}}}\mathbb R.
$$
In the Witten regime, the modular automorphism acts physically as a rescaled right-boundary time translation and the added collective coordinate is related to black-hole energy. These identifications explain the shorthand “crossing by ADM time,” but the algebraic action in the formula is the modular action. The resulting core is a type II$_\infty$ factor.

**Result 3.2 (Witten 2022). [Stated only — refs: Witten 2112.12828 §§3.2–3.5.]** *Including the relevant perturbative $1/N$ collective coordinate enlarges the strict-large-$N$ type III$_1$ algebra to its type II$_\infty$ crossed product. The crossed product has a trace and densities; their entropy is defined up to a state-independent constant. Witten interprets that normalization relative to the entropy of the reference black hole.*

**Two distinct claims, carefully separated.** First, the *operator-algebraic* construction: take a type III$_1$ algebra $\mathcal{A}_R$ with modular flow $\sigma^{\mathrm{TFD}}_t$ and form the crossed product $\hat{\mathcal{A}}_R = \mathcal{A}_R \rtimes_{\sigma^{\mathrm{TFD}}}\mathbb{R}$ — a type II$_\infty$ algebra on which suitable normal states have trace entropy, defined up to an additive constant. This is Block D, no gravity yet.

Second, the *holographic realization*: in the relevant large-$N$ CFT, modular flow acts as a rescaled boundary-time translation, and the energy collective coordinate has an ADM interpretation. The more explicit equality between algebraic and generalized entropy,
$$
S_{\rm alg}=\frac{A}{4G_N}+S_{\rm out}+\mathrm{const},
$$
is established in the CPW construction discussed in §4, using semiclassical gravity in addition to the operator algebra.

Witten's contribution is the physical realization of the construction. The crossed product itself is structural; its identification with the algebra obtained after including the black-hole energy collective coordinate is the large-$N$ gravitational statement. Nonperturbatively at fixed integer $N$, one expects the full boundary algebra to return to type I.

## 4. Two-sided CPW: Sem II Block 2

CPW construct a type II$_\infty$ algebra appropriate to a microcanonical large-$N$ limit and identify its entropy with the generalized entropy of the black-hole bifurcation surface. The modular generator $\beta_H(H_R-H_L)$ is well-defined in the TFD representation, while the right and left algebras are arranged as commutants after the energy collective coordinate is included. Semester II Weeks 5–7 will derive this commutant construction carefully; it is not obtained by placing the same noncentral translation unitary in two allegedly commuting crossed products.

The free-field Rindler model verifies the modular and commutant structure. Replacing boost energy by ADM energy and matter entanglement by $A/(4G_N)+S_{\rm out}$ requires the semiclassical gravitational argument.

## 5. Ahmad–Jefferson: Sem II Block 4

The Ahmad–Jefferson (AAJ) construction of Sem II Block 4 is a **unitary deformation** of an algebra–state system and its crossed-product entropy. The setup is:

1. Start with a reference algebra–state system, its modular data, the associated type-II crossed product, and its entropy weight.
2. Transport the full system by a global unitary. In the gravitational application the interaction is the Gao–Jafferis–Wall double trace, with the sign and switching profile chosen so that the separate bulk calculation gives a traversable window.
3. Use unitary covariance to reconstruct the deformed modular charge and crossed product. The entropy weight acquires a deformation-dependent spectral reweighting and Jacobian.
4. Expand the modular charge by BCH and the weight/Jacobian in the deformation. In the current AAJ version, the result through $O(1/N^2)$ contains the GJW linear structure, **five additional linear structures**, and **fifteen quadratic structures**.

AAJ's expansion is not a Connes-cocycle series. The Connes cocycle from Week 7 remains a useful comparison when two faithful states are varied on one fixed algebra, but AAJ organize a transported algebra–state system through unitary covariance, a changed weight and Jacobian, and BCH nested commutators. Nor does the algebraic entropy series by itself compute the bulk signal time advance: matching individual terms to area, matter entropy, or causal response requires an additional gravitational calculation.

## 6. Worked computation: the regulated Rindler TFD

A modewise calculation that explains the TFD analogy. It is exact for a regulated mode decomposition; in the continuum it is formal because the Minkowski and Rindler representations are not related by a normalizable tensor-product vector.

### 6.1 Modes on Rindler-Rindler

In 2D massless, the field decomposes into right- and left-movers. We focus on the right-mover; the left-mover is identical with $x^- \leftrightarrow x^+$. Inside $W_R$, the right-mover has Rindler modes $b_\omega^R$ with $\omega > 0$ (Week 10 §4); inside $W_L$, Rindler modes $b_\omega^L$.

### 6.2 Bogoliubov coefficients

The Minkowski annihilation operator $a_k$ and the Rindler operators $b_\omega^R, b_\omega^L$ are related by Bogoliubov transformations:
$$
a_k = \int_0^\infty d\omega \left[ \tilde\alpha^R_{k\omega}\,b_\omega^R + \tilde\beta^R_{k\omega}\,(b_\omega^R)^\dagger + \tilde\alpha^L_{k\omega}\,b_\omega^L + \tilde\beta^L_{k\omega}\,(b_\omega^L)^\dagger \right],
$$
with the same $e^{\pi\omega/2}$ vs $e^{-\pi\omega/2}$ ratios as Week 10 §4.3.

### 6.3 The Minkowski vacuum in Rindler modes

With a regulator that makes the left/right mode factorization legitimate, the condition $a_k|0_M\rangle=0$ gives
$$
|0_M\rangle \;=\; \prod_{\omega > 0} \frac{1}{\sqrt{Z_\omega}}\,\sum_n e^{-\pi n\omega}\,\frac{(b_\omega^{L\dagger} b_\omega^{R\dagger})^n}{n!}\,|0_R\rangle\otimes|0_L\rangle,
$$
or, recasting in terms of two-sided number eigenstates $|n_\omega\rangle_R \otimes |n_\omega\rangle_L$ (using that $b^\dagger_R b^\dagger_L$ creates one quantum on each side):
$$
|0_M\rangle = \prod_\omega \frac{1}{\sqrt{Z_\omega}}\,\sum_{n_\omega} e^{-\pi n_\omega\,\omega}\,|n_\omega\rangle_R\otimes|n_\omega\rangle_L.
$$

Mode by mode this is the TFD form with $E_n=n\omega$ and $\beta=2\pi$. Removing the regulator does not produce a trace-class wedge density matrix; the exact continuum statement is Theorem 2.1.

### 6.4 Modular operator from the TFD form

At finite regulator, the type-I calculation gives
$$
\Delta = \prod_\omega \rho_\omega^R \otimes (\rho_\omega^L)^{-1} = e^{-2\pi (N_R - N_L)},
$$
where $N_R = \int d\omega\,\omega\,(b^R_\omega)^\dagger b^R_\omega$ is the Rindler-mode-number Hamiltonian on the right (and similarly $N_L$ on the left). The modular Hamiltonian is $K_{\mathrm{Mink}} = 2\pi(N_R - N_L)$.

The regulator-independent combination tends to the global boost generator. What survives in the continuum is $\Delta_{W_R}=e^{-2\pi K_{\rm boost}}$; the separate one-sided operators $N_R$ and $N_L$ are not elements of the continuum wedge algebras.

### 6.5 What this confirms

The calculation verifies, in a regulator and then structurally in the continuum, that:

- the modewise Schmidt weights are thermal with inverse Rindler temperature $2\pi$;
- the finite-regulator modular generator is the right-minus-left boost energy;
- the continuum modular flow is the geometric boost at rapidity $2\pi t$;
- the continuum theorem must be expressed in standard-form language rather than with a wedge density matrix.

This is the model that all of Sem II Block 2 (CPW) generalizes to the holographic eternal black hole. The substitutions:
- Global boost generator $K_{\rm boost}$ $\leftrightarrow$ the well-defined TFD generator $\widehat H=H_R-H_L$.
- $\beta = 2\pi$ Unruh $\leftrightarrow$ $\beta_H$ Hawking.
- Bifurcation surface (Minkowski's $\{x^0 = x^1 = 0\}$) $\leftrightarrow$ BH horizon (the Schwarzschild bifurcation sphere).
- 2D massless free scalar $\leftrightarrow$ holographic CFT at large $N$.

## 7. Sem II in one sentence

Combining Block D with the TFD identification:

> **Semester II asks when the modular crossed product (Week 13), applied to the one-sided algebra of a two-sided standard-form state, becomes a gravitational exterior algebra, and when its trace entropy (Week 14) agrees with generalized entropy.**

Each Sem II Block tackles a specific instance:

- **Block 1 (Witten 2022):** the right exterior algebra, its black-hole energy collective coordinate, and the emergence of the type II$_\infty$ crossed product with entropy defined up to a constant.
- **Block 2 (CPW):** the right crossed product and its dressed commutant in the TFD setting, with the explicit generalized-entropy matching.
- **Block 3 (Liu lectures):** structural overview; modular flow ↔ bulk Killing flow dictionary; algebraic ER=EPR.
- **Block 4 (AAJ):** unitary transport of the algebra–state system and its crossed-product weight; through $O(1/N^2)$ the current entropy expansion contains the GJW linear structure, five additional linear structures, and fifteen quadratic structures.
- **Block 5 (MSY + outlook):** bulk-side complement; honest scoping; what the algebra sees and what it doesn't.

Each block uses the Block D + Week 15 toolkit. **Semester I has built every algebraic ingredient needed for Semester II.**

## 8. What to take away

- **TFD definition:** $|\mathrm{TFD}_\beta\rangle = Z(\beta)^{-1/2}\sum_n e^{-\beta E_n/2}|n\rangle_R\otimes|n\rangle_L$, a purification of the Gibbs state.
- **Modular structure of TFD:** $\Delta=\rho_R\otimes\rho_L^{-1}$ and $K=\beta(H_R-H_L)$; the two normalization constants cancel exactly.
- **Stated only (Theorem 2.1):** the Minkowski vacuum is cyclic and separating for one wedge algebra, wedge modular flow is the boost, and modular conjugation maps the wedge algebra to its commutant. The literal TFD is a regulated, modewise model of this standard form.
- **Holographic dictionary (Maldacena):** the two-sided eternal black hole is dual to the doubled boundary CFT in the TFD state at Hawking temperature.
- **Stated only (Result 3.2, Witten):** the perturbatively enlarged exterior algebra is the type II$_\infty$ modular crossed product, with trace entropy defined up to a constant. CPW supplies the explicit generalized-entropy identification in its setup.
- **Worked verification (§6):** a regulated Rindler-mode calculation has TFD weights and a right-minus-left generator; the continuum limit is expressed by the global boost modular operator.
- **The Sem II structural question:** which physical systems realize the modular core as a dressed exterior algebra, and under which additional hypotheses does its entropy become generalized entropy?

## 9. The take-home final

A take-home final is assigned at the end of Week 15, due 4 weeks later (over the break before Sem II). It consolidates Sem I and lands students at the toolkit they need for Sem II Block 1.

**Problem 1: Modular operator for 4D massless scalar.** Compute the modular operator and Bisognano–Wichmann boost flow for the 4D massless free scalar restricted to the right Rindler wedge $W_R = \{x: x^1 > |x^0|\}$. (Generalize the 2D calculation of Week 10 §4.)

**Problem 2: Connes cocycle for vacuum vs. coherent state.** For the 2D massless free scalar on $W_R$, let $U=W(f)$ with real test function $f$ supported in $W_R$, and set $\omega_f(a)=\omega_0(U^*aU)$. Starting from the inner-perturbation identity
$$
(D\omega_f:D\omega_0)_t=U\,\sigma_t^{\omega_0}(U^*),
$$
use Bisognano–Wichmann and the Weyl relations to express the cocycle as a phase times a Weyl operator built from $f$ and its boost transform. Check the cocycle equation explicitly.

**Problem 3: Crossed-product variables and trace model.** Construct $\widehat{\mathcal A}(W_R)=\mathcal A(W_R)\rtimes_{\sigma}\mathbb R$ in the regular representation and identify the coordinate $q$, its multiplication operator $Q$, the momentum $P=-i\partial_q$, its Fourier variable $p$, the modular parameter $t$, the rapidity $u=2\pi t$, and the dual parameter $r$. Then verify $\widehat\tau\circ\theta_r=e^{-r}\widehat\tau$ in the exact inner-action Fourier model of Week 13. Explain why this model does not give a distributional diagonal formula for the genuine type-III core.

**Problem 4: Bell-CHSH on a regulated Rindler pair.** Choose the finite-mode or split-regulated setup of Week 11 and compute $\langle\mathcal C_{\rm CHSH}\rangle$ for a stated family of cosine-Weyl observables on the two sides. Optimize within that family and report the value as an explicit lower bound on the CHSH supremum. Compare it with $2$ and $2\sqrt2$. State separately whether any approach to Tsirelson saturation is proved, supported numerically, or imported from a general operator-algebraic theorem.

**Problem 5 (⋆): Coherent-state cancellation.** Let $U=\pi(W(f))$ with $f$ supported in $W_R$, and dress the vacuum and coherent state with the same clock. Prove that their core densities obey $D_f=UD_0U^*$ and hence have equal trace entropy. Use Week 14 to show that the relative-entropy and modular-energy terms cancel exactly. Then list two changes of setup that could produce a nonzero entropy difference.

### Why these five problems

Each problem will reappear in Sem II, expanded and applied to specific papers:

- **Problem 1** generalizes to higher dimensions (4D massless is the standard setting of CPW and AAJ).
- **Problem 2** supplies the fixed-algebra Connes-cocycle comparison used in Sem II to clarify how AAJ's unitary weight/Jacobian expansion is different.
- **Problem 3** fixes the representation dictionary needed to read the Witten and CPW formulas without mixing a coordinate with its conjugate momentum.
- **Problem 4** is the technical setup for the open question "Bell-CHSH in holographic settings."
- **Problem 5** is the unitary-invariance check that every later perturbative formula must pass.

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

**2. Modular operator of the finite-dimensional TFD.** Compute $\Delta$ for the right algebra and verify
$$
\Delta=(e^{-\beta H_R}/Z)\otimes(e^{-\beta H_L}/Z)^{-1},
\qquad
-\log\Delta=\beta(H_R-H_L).
$$
Show explicitly how the two factors of $Z$ cancel.

**3. Mode-by-mode TFD form of Minkowski vacuum.** Expand the formula §6.3 to order $n_\omega = 1$ and identify the structure: $|0_M\rangle \approx \prod_\omega(1 + e^{-\pi\omega}\,b^R_\omega{}^\dagger b^L_\omega{}^\dagger + O(e^{-2\pi\omega}))|0_R\rangle\otimes|0_L\rangle$.

**4. Flow on an algebra and its commutant.** Starting from $\Delta_{W_R}=e^{-2\pi K_{\rm boost}}$, show that $\operatorname{Ad}(\Delta^{-it})$ acts by rapidity $+2\pi t$ on $\mathcal A(W_R)$ and by the inverse modular flow on $\mathcal A(W_R)'=\mathcal A(W_L)$. Do not introduce a tensor-product factorization of the continuum Fock space.

**5. Reading bridge.** Read Maldacena 2003 §§1–3 (the eternal-BH/TFD identification). Identify the key claim and the level of evidence Maldacena gives.

**Starred problems.**

**6\*. Modular Hamiltonian on a one-sided thermal state.** For the Gibbs state $\rho_\beta = e^{-\beta H}/Z$ on a finite-dimensional system, viewed as a state on $\mathcal{B}(\mathcal{H})$, the modular Hamiltonian is $K_\beta = \beta H + \log Z$. Show that the dressed trace entropy of the Gibbs state, computed via the modular crossed product, is
$$
S_{\widehat\tau}(\widehat\rho_{\beta,\mathrm{dressed}})
=S_{\mathrm{thermal}}(\beta)+(\text{clock contribution}),
$$
where the clock contribution is $H(\mu)-\mathbb E_\mu[p]$ in the Fourier model, and $S_{\mathrm{thermal}}(\beta)=\beta\langle H\rangle_\beta+\log Z$.

**7\*. ER=EPR (heuristic, one-way audit).** In the eternal-black-hole example, a TFD-like faithful state supplies a one-sided standard pair and identifies the commutant with the opposite boundary algebra. Explain why $J\mathcal A_RJ=\mathcal A_R'$ is automatic for any standard pair and therefore cannot be an if-and-only-if criterion for a wormhole. What additional holographic input is needed before these modular data can be interpreted geometrically?

**8\*. JT gravity source audit.** Choose one explicit published or arXiv construction of a dressed/type-II algebra in Jackiw–Teitelboim gravity. Record its boundary conditions, observable algebra, trace normalization, and state class. Reproduce one displayed entropy relation from that source and label separately what is exact in the model and what is semiclassical. If the source states rather than derives the generalized-entropy match, report it as stated rather than “verified.”

**Project problems.**

**9. Read Witten 2022 in full.** Identify how each ingredient of our Block D (crossed product, outer shift, trace, density, and entropy normalization) maps onto Witten's exposition. Separate what Witten derives from what is supplied later by the CPW generalized-entropy calculation.

**10. Read CPW 2022 in full.** Identify the difference between Witten's single-sided story and CPW's two-sided TFD story. What does the two-sidedness add structurally?

## 12. Instructor checkpoints (internal)

### Take-home final

1. **Four-dimensional wedge:** the accepted structural answer is $\Delta_{W_R}=e^{-2\pi K_{\rm boost}}$ and $\sigma_t=\operatorname{Ad}e^{i2\pi tK_{\rm boost}}$, with the scalar field transformed by the Lorentz pullback. No one-sided Gibbs density matrix is introduced in the continuum.
2. **Coherent cocycle:** with $\sigma_t(W(f))=W(f_t)$,

$$
(D\omega_f:D\omega_0)_t
=W(f)W(-f_t)
=e^{iE(f,f_t)/2}W(f-f_t),
$$

for the Weyl convention in these notes. The Weyl phase and the modular composition law together verify the cocycle equation.
3. **Crossed-product variables:** the answer must distinguish $q,Q,P,p,t,u,r$ and recover $\widehat\tau\circ\theta_r=e^{-r}\widehat\tau$ only in the legitimate Fourier trace model.
4. **CHSH:** the reported optimized value is a lower bound for the chosen regulated family. It must be compared separately with the classical bound $2$, the Tsirelson bound $2\sqrt2$, and any general theorem being invoked.
5. **Coherent cancellation:** $D_f=UD_0U^*$ gives exact equality of trace entropies. Nonzero differences require, for example, a different clock distribution or a non-inner/state-dependent comparison.

### Additional problems

1. The partial trace leaves the diagonal weights $e^{-\beta E_n}/Z$.
2. $\Delta=\rho_R\otimes\rho_L^{-1}$; the two factors of $Z$ cancel, leaving $-\log\Delta=\beta(H_R-H_L)$.
3. The $n_\omega=1$ amplitude is $e^{-\pi\omega}$; the omitted normalization and two-particle terms begin at the indicated higher order mode by mode.
4. The right action has rapidity $+2\pi t$ in the course convention. On the commutant, the corresponding modular automorphism is the inverse flow; this does not require a continuum tensor factorization.
5. Maldacena supplies a holographic saddle/dictionary statement, not an operator-algebra theorem about every entangled state.
6. The answer is $S_{\rm thermal}+H(\mu)-\mathbb E[p]$, with $S_{\rm thermal}=\beta\langle H\rangle+\log Z$.
7. Standardness makes $J\mathcal A_RJ=\mathcal A_R'$ automatic. A geometric conclusion needs a holographic code-subspace identification and a controlled bulk state; Liu's later algebraic ER=EPR proposal adds still more hypotheses.
8. The JT audit is graded on source fidelity, explicit trace/state data, and honest status labels, not on claiming a universal JT theorem.
9. Witten supplies the perturbative energy-inclusive core, trace, densities, and normalization; the explicit controlled $S_{\rm alg}=S_{\rm gen}+\mathrm{const}$ matching belongs to CPW.
10. CPW add a strict microcanonical scaling, a physical relative timeshift, the right core together with its dressed commutant, and the horizon relative-entropy calculation.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block D. Last revised 2026-08-24. **End of Semester I.***
