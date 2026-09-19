---
title: "Sem II Week 8 — Bell-CHSH Between the Two Sides (Mini-Calc 3)"
type: lecture-notes
course: syllabus
semester: 2
week: 8
block: 2
duration: 4 hours (computational lecture + discussion)
prerequisites: Sem II Wks 5–7 (CPW); Sem I Wk 11 (Bell-CHSH in QFT)
target_paper: "CPW; De Fabritiis–Sorella–Guimarães–Roditi recent papers"
modified: 2026-06-11
---

# Sem II Week 8 — Bell-CHSH Between the Two Sides (Mini-Calc 3)

> *Block 2 closes with the algebraic content of "ER=EPR." The two-sided TFD vacuum on $\mathcal{A}_R \otimes \mathcal{A}_L$ is maximally entangled in the type-III$_1$ sense — by Summers-Werner (Sem I Wk 11), every pair of dichotomic observables built from boundary single-trace operators can be optimized to saturate the Tsirelson bound. Today we make this concrete: take cosine-Weyl observables on the free-field Rindler-Rindler analog, compute $\langle\mathrm{TFD}|\mathcal{C}_{\mathrm{CHSH}}|\mathrm{TFD}\rangle$, and show the approach to $2\sqrt 2$. The setup is **exactly** the bumpified-Haar-wavelet program of De Fabritiis, Sorella, Roditi, Guimarães et al. — this is where the group's research connects directly to CPW. Block 2 ends; students enter Block 3 (Liu lectures) with the full two-sided CPW machinery in hand.*

## 0. Reading

**Primary:**
- Sem I Wk 11 (Bell-CHSH in QFT; Summers-Werner).
- One or two recent De Fabritiis-Sorella-Roditi-Guimarães Bell-CHSH papers (instructor selects).

**Secondary:**
- Sem II Wks 5–7 (TFD as cyclic-separating, dressed entropy).
- Summers, "Yet more ado about nothing," arXiv:0802.1854 §3.

**Optional research reading:**
- Werner, "Quantum states with EPR correlations admitting a hidden-variable model," *Phys. Rev. A* 40 (1989) 4277 (Werner states).
- Tsirelson, "Quantum generalizations of Bell's inequality," *Lett. Math. Phys.* 4 (1980) 93 (original Tsirelson bound).
- The wiki open question [[bell-chsh-in-holographic-setting|Bell-CHSH in holographic settings]].

## 1. The setup

### 1.1 Two-sided algebras

From Block 2:

- Two-sided boundary algebras $\mathcal{A}_R, \mathcal{A}_L$ at large $N$, both type III$_1$.
- TFD vacuum $|\mathrm{TFD}\rangle$ cyclic-separating for both.
- Causally complementary: $[\mathcal{A}_R, \mathcal{A}_L] = 0$.

In the free-field analog: $\mathcal{A}(W_R), \mathcal{A}(W_L)$ on Fock space, with Minkowski vacuum as the TFD of the boost.

### 1.2 The Bell-CHSH question

The Bell-CHSH operator (Sem I Wk 11):
$$
\mathcal{C}_{\mathrm{CHSH}}(A_1, A_2, B_1, B_2) = A_1 B_1 + A_1 B_2 + A_2 B_1 - A_2 B_2,
$$
with $A_i \in \mathcal{A}_R$ self-adjoint, $\sigma(A_i) \subset [-1, 1]$; similarly $B_j \in \mathcal{A}_L$.

By Sem I Wk 11 Theorem 1.2:
- Classical (LHV) bound: $|\langle\mathcal{C}\rangle| \le 2$.
- Tsirelson (quantum) bound: $|\langle\mathcal{C}\rangle| \le 2\sqrt 2$.

By Summers-Werner (Sem I Wk 11 Theorem 2.1):
- In the TFD vacuum, the Tsirelson bound is **approached** by an optimal choice of dichotomic Weyl-cosine observables, with the limit involving the boost-modular flow.

This week we make the calculation explicit in the free-field analog.

### 1.3 ER=EPR connection

The pedagogical hook of this lecture:

**Bell-CHSH saturation in the TFD vacuum is the algebraic content of "the two sides are maximally entangled," i.e., of ER=EPR.**

Concretely: a TFD vacuum that did *not* maximally entangle the two algebras would correspond to a *disconnected* bulk geometry. The maximal entanglement (saturation of Tsirelson) is what makes the wormhole "present" in the algebraic structure.

## 2. The cosine-Weyl observables (recap from Sem I Wk 11)

### 2.1 Definition

For real test functions $f \in \mathcal{S}(W_R)_\mathbb{R}, g \in \mathcal{S}(W_L)_\mathbb{R}$ and real parameter $\alpha > 0$:
$$
A(f, \alpha) = \cos(\alpha\phi(f)) = \tfrac{1}{2}(W(\alpha f) + W(\alpha f)^*),
$$
similarly $B(g, \beta) = \cos(\beta\phi(g))$.

These are bounded self-adjoint operators in $\mathcal{A}(W_R), \mathcal{A}(W_L)$ respectively, with spectrum in $[-1, 1]$.

### 2.2 Vacuum expectations

By Sem I Wk 11 §4.2, the vacuum two-point function of two cosines:
$$
\langle 0_M|\cos(\alpha\phi(f))\cos(\beta\phi(g))|0_M\rangle = \tfrac{1}{2}\big(e^{-(\alpha^2 W(f,f) + \beta^2 W(g,g) + 2\alpha\beta\,W(f,g))/2} + (g \to -g)\big).
$$

For $f \in W_R, g \in W_L$ (spacelike separated): $W(f, g)$ is *real* (the imaginary part $\sigma(f, g)$ vanishes by spacelike separation), so the formula simplifies to
$$
\langle 0_M|A(f, \alpha)B(g, \beta)|0_M\rangle = \tfrac{1}{2}\big(e^{-Q_+/2} + e^{-Q_-/2}\big),
$$
$Q_\pm = \alpha^2 W(f,f) + \beta^2 W(g,g) \pm 2\alpha\beta\,\mathrm{Re}\,W(f, g)$.

This is the structural formula for cosine-Weyl correlations.

## 3. The Bell-CHSH expectation

### 3.1 The four-correlator combination

The CHSH operator is the difference combination:
$$
\langle\mathcal{C}\rangle = \langle A_1 B_1\rangle + \langle A_1 B_2\rangle + \langle A_2 B_1\rangle - \langle A_2 B_2\rangle.
$$
Each $\langle A_i B_j\rangle = \langle 0_M|\cos(\alpha\phi(f_i))\cos(\alpha\phi(g_j))|0_M\rangle$ is given by the formula in §2.2.

### 3.2 Strategy

The strategy from Summers-Werner:
1. Choose **four** test functions: $f_1, f_2 \in W_R$ and $g_1, g_2 \in W_L$.
2. The free parameters are: positions and widths of the bumps, plus the cosine strength $\alpha$.
3. Optimize over these parameters to maximize $|\langle\mathcal{C}\rangle|$.
4. **Boost the test functions** toward the bifurcation surface: as boost rapidity $\eta \to \infty$, $|\langle\mathcal{C}\rangle| \to 2\sqrt 2$.

### 3.3 Numerical answer (qualitative)

Without doing the full optimization (which is the content of the group's research papers), the qualitative behavior:

- **Compact, well-separated bumps:** $|\langle\mathcal{C}\rangle| \approx 0$ (no significant correlation).
- **Bumps approaching the bifurcation surface:** $|\langle\mathcal{C}\rangle| \to 2\sqrt 2$.

The transition is continuous as the wavelet parameters tune. The group's papers (e.g., De Fabritiis-Roditi-Sorella, ~2023–2024) compute $|\langle\mathcal{C}\rangle|$ explicitly for specific bumpified-Haar-wavelet configurations and report values up to $\approx 2.7$–$2.8$, very close to $2\sqrt 2 \approx 2.828$.

### 3.4 The boost-limit

The optimal limit is **boost rapidity $\eta \to \infty$**, where the test functions are "squeezed" toward the bifurcation surface in the boost direction. Concretely:

- Take a reference $f^0$ at boost-coordinate $\xi_0 = 1$.
- The boosted version is $f^\eta = f^0 \circ \Lambda^{\mathrm{boost}}(\eta)$ at $\xi = e^{-\eta}$, getting arbitrarily close to the bifurcation surface as $\eta \to \infty$.

In this limit:
- $W(f^\eta, f^\eta) \to \infty$ logarithmically (the test function approaches a delta on the horizon).
- $W(f^\eta, g^\eta)$ tunes to give $|\langle\mathcal{C}\rangle| \to 2\sqrt 2$.

The boost-limit is **exactly the modular flow** of the wedge algebra (Sem I Wk 10), so Tsirelson saturation requires the full modular structure. This is the algebraic content of Summers-Werner.

## 4. Worked computation: the 2D massless analog

A more explicit form to bring out the structure. Take the **2D massless free scalar** (which is more tractable than 4D for analytical work).

### 4.1 Bumpified Haar wavelets

A bumpified Haar wavelet is a smooth approximation of the discontinuous Haar wavelet
$$
h_{\mathrm{Haar}}(x) = \mathbf{1}_{[0, 1/2]}(x) - \mathbf{1}_{[1/2, 1]}(x).
$$
A "bumpified" version $\tilde h$ is the Haar wavelet convolved with a smooth bump function — preserving the rough shape but smoothing the discontinuities. Used as test functions $f, g$ in the cosine-Weyl construction.

> **Physical picture: why wavelets?** The choice is not aesthetic. A CHSH experiment needs each observer's two measurement settings to be *strongly incompatible* (Sem I Wk 11: the violation is bounded by the commutator norms $\|[A_1, A_2]\|$), while the pair across the horizon must couple to *strongly correlated* vacuum modes. Wavelets optimize both at once: their vanishing integral ($\int h = 0$) removes the IR-dominated zero-mode of the 2D massless field (which would otherwise swamp the correlators with divergent, setting-independent noise), and their localized oscillation selects a narrow band of boost frequencies — precisely the straddling modes whose Unruh-thermal entanglement drives the violation. Smoothing ("bumpification") keeps the test functions in $\mathcal{S}(W_R)$ so the smeared fields are honest self-adjoint operators. In short: Haar shape = mode selectivity and incompatibility; bump smoothing = operator-theoretic legality.

### 4.2 Locations

Place:
- $f_1$ bumpified at $(t_1, s_1)$ in $W_R$.
- $f_2$ bumpified at $(t_2, s_2)$ in $W_R$.
- $g_1$ bumpified at $(-t_1, -s_1)$ in $W_L$ (mirror of $f_1$).
- $g_2$ bumpified at $(-t_2, -s_2)$ in $W_L$ (mirror of $f_2$).

The mirror-pair choice maximizes the natural two-sided correlations (since the TFD identifies $|n\rangle_R\otimes|n\rangle_L$ symmetrically).

### 4.3 Two-point functions

For the 2D massless free scalar, the Wightman two-point function is logarithmic:
$$
W(x, y) = -\frac{1}{4\pi}\log\!\big|(x^0 - y^0 - i\epsilon)^2 - (x^1 - y^1)^2\big|.
$$
Integrated against bumpified Haar wavelets, this gives finite numerical values for $W(f_i, g_j)$ depending on the bump positions.

### 4.4 Approach to Tsirelson

The asymptotic structural form (Summers-Werner):
$$
|\langle\mathcal{C}\rangle|^2 \approx 8 - \mathrm{const}\cdot e^{-\pi\omega_{\max}},
$$
where $\omega_{\max}$ is the dominant boost-frequency contribution. As $\omega_{\max} \to \infty$ (boost-limit), $|\langle\mathcal{C}\rangle|^2 \to 8$, i.e. $|\langle\mathcal{C}\rangle| \to 2\sqrt 2$ — Tsirelson saturation from below.

(Aside: the ceiling $8$ is the operator bound $\|\mathcal{C}\|^2 \le 4 + \|[A_1,A_2]\|\,\|[B_1,B_2]\| \le 8$ from Sem I Wk 11 §1.2 — the classical 4 plus the maximal commutator contribution 4. The exponential deficit $e^{-\pi\omega_{\max}}$ is a Boltzmann factor at the Unruh temperature: the imperfection of the Bell pair formed by modes of boost frequency $\omega_{\max}$ straddling the horizon. Boosting deeper recruits higher-frequency, more perfectly entangled straddling pairs, exponentially closing the gap.)

## 5. The group's research program

The above is the **mathematical** setup. The group's research papers (De Fabritiis, Sorella, Roditi, Guimarães et al.) develop the **constructive** side:

### 5.1 What they compute

For specific bumpified-Haar-wavelet test functions, the group computes:
1. $W(f_i, g_j)$ exactly (numerical integration of the 2D Klein–Gordon Wightman function against the wavelet bumps).
2. The CHSH expectation $\langle 0_M|\mathcal{C}|0_M\rangle$ as a function of the wavelet positions.
3. Optimization over a parametric family of wavelets.
4. Report the highest achievable $|\langle\mathcal{C}\rangle|$ in specific configurations.

### 5.2 What this shows

The group's papers demonstrate that:

- **Real numerical values** of $|\langle\mathcal{C}\rangle|$ up to $\approx 2.7$–$2.8$ are achievable with simple wavelet test functions.
- The approach to $2\sqrt 2$ is monotonic in boost rapidity (as expected from the modular structure).
- The **scaling** of the approach matches the Summers-Werner asymptotic.

This is **constructive evidence** for Summers-Werner saturation — an algebraic existence theorem is here made operational with explicit observables.

### 5.3 Extensions

The same machinery extends to:
- **Massive free scalar:** same wedge modular flow, different correlator decay.
- **Proca field (massive vector):** different but still tractable algebra.
- **Higher dimensions:** 4D massless scalar (relevant to the actual eternal-BH calculation).

The Block 2 problem set (Problem 5 below) asks students to read one such paper and verify a numerical value.

### 5.4 Wiki connection: holographic Bell-CHSH

The wiki open question [[bell-chsh-in-holographic-setting]] asks whether the Bell-CHSH saturation extends to *holographic* boundary subregions (rather than just free-field wedges). The structural prediction from Summers-Werner is yes — under the hypothesis that the boundary single-trace algebra is type III$_1$ (Week 1 Theorem 4.1). The free-field analog of Week 8 is a controlled verification of the structural mechanism.

## 6. ER=EPR: the algebraic content

### 6.1 The Maldacena-Susskind proposal

ER=EPR (Maldacena-Susskind, arXiv:1306.0533) proposes:

> Two CFTs are connected by an Einstein-Rosen bridge in the bulk if and only if they are entangled in a TFD-like way on the boundary.

This is a heuristic with several proposed formal statements. The Block 2 / Week 8 algebraic version:

**Algebraic ER=EPR (CPW-style):** *Two boundary algebras $\mathcal{A}_R, \mathcal{A}_L$ are dual to a single connected bulk geometry (with an ER bridge) if and only if there exists a cyclic-separating vector on the joint algebra whose modular conjugation $J$ satisfies $J\mathcal{A}_R J = \mathcal{A}_L$.*

The Bell-CHSH saturation is **necessary but not sufficient** for this: maximal Bell-CHSH violation requires type III$_1$ + commuting subalgebras + cyclic-separating vector. Together these encode the algebraic content of the wormhole.

### 6.2 Why the saturation is the wormhole

Heuristic: a maximally entangled TFD state corresponds to a *bulk* state with the two boundaries glued together through the bridge. A *less entangled* state (e.g., a tensor product of two independent thermal states) corresponds to *two disconnected* bulk geometries.

The Bell-CHSH saturation distinguishes these: maximal violation requires the type-III$_1$ joint structure, which only the **connected geometry** provides. So Bell saturation $\Leftrightarrow$ wormhole present.

### 6.3 What this is not

This is **not** a derivation of the bulk geometry from boundary entanglement (which would require much more — bulk reconstruction). It is an algebraic *necessary condition* for the bulk wormhole to be present in the dual.

In the **other direction**: bulk reconstruction goes from boundary algebras + state to bulk geometry. The CPW dressed-algebra construction (Weeks 6–7) is the algebraic side; the bulk reconstruction is a separate program (e.g., Faulkner-Lewkowycz-Maldacena 2013; Almheiri-Dong-Harlow 2014).

## 7. Final write-up topic options

The end of Block 2 is the point in the course where students commit to **final write-up topics**. Per the course design (Sem II syllabus §5), each student writes a 15–20 page exposition of one technical topic by end of Week 14.

### 7.1 Topic options

Four directions, each connecting to a different part of the course:

**Option 1: Free-field cocycle perturbation.** Compute perturbations of the dressed entropy via the Connes cocycle (Sem I Wk 7). Setup: take the dressed Rindler algebra $\hat{\mathcal{A}}(W_R)$; perturb the modular flow by a small deformation $\delta H$ (e.g., a quench, a Gao-Jafferis-Wall double-trace, or a localized excitation). Compute the perturbed dressed entropy to order $g^2$. Connect to the AAJ Block 4 setup.

**Option 2: Bell-CHSH in holographic settings.** Address the wiki open question [[bell-chsh-in-holographic-setting]]. Setup: take a holographic CFT at large $N$, two spacelike boundary regions, and ask whether the Tsirelson bound is saturated. What does this say about the bulk geometry? Speculative direction — but the algebraic setup is fully developed in Week 11 + Week 8 of this course.

**Option 3: Embezzlement on the crossed product.** Read recent work on entanglement embezzlement in type III$_1$ algebras (e.g., van Daele 2022). What does the crossed-product construction (Block D) add to the embezzlement story? Are dressed algebras still capable of exact embezzlement?

**Option 4: Critical exposition.** A clean, mathematically careful exposition of one of: CPW 2022 (the paper studied this block), CLPW 2022 (de Sitter; Block 5 Wk 14 aside), or AAJ 2025 (Block 4). The exposition should:
- Identify the key algebraic ingredients (modular structure, crossed product, dressed entropy).
- Identify the holographic / physics inputs (large-$N$ identifications, first laws).
- Verify one explicit calculation from the paper.

### 7.2 Choosing a topic

Topics are confirmed at end of Wk 8. Students should:
- Commit by end of Wk 8 to one of Options 1–4.
- Draft a 1-page proposal by end of Wk 10 (mid-Block 3, when Liu lectures contextual material is fresh).
- Submit a draft by end of Wk 13 (after AAJ).
- Submit final by end of Wk 15.

## 8. What we don't do

A few honest exclusions in Block 2:

### 8.1 The bulk gravitational calculation

Block 2 (and Block 1) consistently keeps the **bulk gravitational calculation separate** from the algebraic structure. We do not:
- Derive the Hawking temperature from the bulk Euclidean action.
- Compute $A/(4G_N)$ from the bulk Einstein-Hilbert action.
- Verify the first law $\delta M = T_H \delta S_{\mathrm{BH}}$ from the bulk side.

These are inputs to Witten 2022 / CPW from the **gravitational** side of the AdS/CFT duality. The course assumes them as known and uses them as inputs.

### 8.2 The path-integral / replica derivation

CPW §5 (the "core technical result") involves a careful matching between bulk path integrals (replica method) and algebraic trace formulas. This is a deep technical point that we do not develop. The structural conclusion — dressed entropy = generalized entropy — is taken as the Witten-CPW-stated result, and we focus on its algebraic structure.

### 8.3 The QES prescription

The CPW dressed-entropy formula gives $S_{\mathrm{vN}}$ at a *fixed* choice of bulk surface (the BH horizon). The QES prescription (Engelhardt-Wall 2014; Penington 2019; Almheiri-Engelhardt-Marolf-Maxfield 2019) extremizes over surfaces. This is a separate development that we do not pursue.

## 9. End-of-block synthesis

Block 2 has accomplished:

1. **Identified the TFD as the cyclic-separating vector** of the two-sided boundary algebras (Wk 5). Modular Hamiltonian = $\beta_H(H_R - H_L)$, the bulk-boost Killing generator.

2. **Constructed the CPW dressed algebras** (Wk 6): $\hat{\mathcal{A}}_R, \hat{\mathcal{A}}_L$, type II$_\infty$, commuting on the dressed Hilbert space, single-clock structure.

3. **Verified the dressed-entropy = generalized-entropy identification** in the free-field analog (Wk 7). Same as Block 1 (Witten 2022) but with the two-sided horizon and bulk-interior bulk entropy.

4. **Confirmed Bell-CHSH saturation between the two sides** (this week). Computational connection to the group's bumpified-Haar-wavelet research program. Algebraic content of ER=EPR.

We are now halfway through Semester II. Block 3 (Liu lectures) is connective tissue: it provides Liu's structural overview of the entire program (large $N$ → type III → crossed product → algebraic ER=EPR), giving students a synthesizing perspective before Block 4's AAJ perturbation theory.

## 10. What to take away

- **Two-sided CPW Bell-CHSH:** dichotomic Weyl-cosine observables on $\mathcal{A}(W_R) \otimes \mathcal{A}(W_L)$ in the TFD vacuum approach Tsirelson saturation $|\langle\mathcal{C}\rangle| \to 2\sqrt 2$.
- **Algebraic content of ER=EPR:** maximal Bell violation in the TFD ↔ type III$_1$ joint structure ↔ connected bulk geometry with ER bridge.
- **Group's research program** (De Fabritiis-Sorella-Roditi-Guimarães et al.) is the **constructive** side of Summers-Werner: explicit bumpified-Haar-wavelet observables achieving $\sim 2.7$–$2.8$ in 2D massless.
- **Boost-limit / modular-limit:** Tsirelson saturation requires the boost-modular flow of the wedge — i.e., the full modular structure of the two-sided algebra.
- **Open question:** does Bell-CHSH saturation extend to holographic boundary subregions? See [[bell-chsh-in-holographic-setting]].

## 11. Looking ahead

Block 3 (Liu lectures, Wks 9–10) is connective tissue. Liu (arXiv:2510.07017) provides:
- A pedagogical overview of "type III at large $N$" (Wk 9 covers Liu §§3–4: type III at large $N$ + modular flow as bulk geometric flow).
- The algebraic ER=EPR proposal made precise (Wk 10 covers Liu §§5–8: crossed products in holography, semiclassical limits, algebraic ER=EPR).

Block 3 should feel like a *consolidation* of Blocks 1–2 rather than new content. By the time students reach Block 4 (AAJ, Wks 11–13), they will have read Witten 2022, CPW, and Liu's lectures, with explicit free-field analog calculations for each.

## 12. Problem set

**Core problems.**

**1. Vacuum two-cosine correlator.** Compute $\langle 0_M|\cos(\alpha\phi(f))\cos(\beta\phi(g))|0_M\rangle$ for the 2D massless free scalar with simple Gaussian $f, g$. Verify the form §2.2.

**2. Spacelike vanishing of $\sigma$.** For $f \in W_R, g \in W_L$ (spacelike separated), verify $\sigma(f, g) = 0$. (Used to simplify the two-cosine correlator.)

**3. Bell-CHSH for mirror-symmetric wavelets.** Take 2D massless free scalar, four wavelets in the configuration §4.2 (mirror pairs across the bifurcation surface). Compute $\langle 0_M|\mathcal{C}|0_M\rangle$ analytically for small bumps, and verify $|\langle\mathcal{C}\rangle| < 2\sqrt 2$.

**4. Approach to Tsirelson.** Boost the bumps toward the bifurcation surface (parameter $\eta$). Compute $|\langle\mathcal{C}\rangle|$ as a function of $\eta$ and verify $|\langle\mathcal{C}\rangle| \to 2\sqrt 2$ as $\eta \to \infty$.

**5. Read one group paper.** Pick one recent De Fabritiis-Sorella-Roditi-Guimarães paper. Identify the precise observable construction and the highest reported $|\langle\mathcal{C}\rangle|$. Reproduce one numerical computation.

**Starred problems.**

**6\*. Bell-CHSH in 4D.** Repeat the structural calculation for the 4D massless free scalar. Identify what changes (transverse modes, Bessel-function correlators) but verify the same structural approach to Tsirelson.

**7\*. The dressed Bell-CHSH.** Compute $\langle\mathrm{TFD}|\mathcal{C}|\mathrm{TFD}\rangle$ for cosine-Weyl observables on the **dressed** algebras $\hat{\mathcal{A}}(W_R), \hat{\mathcal{A}}(W_L)$. Does the dressing change the bound, or is the saturation preserved?

**8\*. Massive scalar Tsirelson saturation.** Repeat §3 for the 2D massive free scalar. Show that Tsirelson saturation still holds (the modular structure of wedges is mass-independent), but that the rate of approach depends on $m$.

**9\*. Read the wiki open question.** Read [[bell-chsh-in-holographic-setting]] in detail. What's a concrete proposal for "Bell-CHSH between two spacelike boundary subregions of a holographic CFT"? What would maximally-violating observables look like?

**Project / final-writeup problems.**

**10. Choose final write-up topic.** From §7.1, commit to one of:
- Free-field cocycle perturbation (Option 1).
- Bell-CHSH in holographic settings (Option 2).
- Embezzlement on the crossed product (Option 3).
- Critical exposition of CPW / CLPW / AAJ (Option 4).

Submit a 1-paragraph proposal by end of Wk 9.

**11. Block 2 end-of-block writeup.** Each student writes a 3-page synthesis of Block 2 covering: (i) the TFD as cyclic-separating; (ii) the CPW dressed algebra; (iii) the dressed-entropy / area-law identification; (iv) the Bell-CHSH saturation. Submit by end of Wk 9.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 2. Last revised 2026-06-11.*

*End of Sem II Block 2.*
