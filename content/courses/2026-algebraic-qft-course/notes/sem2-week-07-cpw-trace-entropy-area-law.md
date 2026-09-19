---
title: "Sem II Week 7 — Trace, Entropy, and the Area Law (CPW Mini-Calc 2)"
type: lecture-notes
course: syllabus
semester: 2
week: 7
block: 2
duration: 4 hours (computational lecture + problem session)
prerequisites: Sem II Wks 5–6 (TFD, CPW dressing); Sem I Wks 13–14 (crossed product, dressed entropy)
target_paper: "Chandrasekaran, Penington, Witten (CPW), arXiv:2209.10454 §4"
modified: 2026-06-11
---

# Sem II Week 7 — Trace, Entropy, and the Area Law (CPW Mini-Calc 2)

> *Last week we built the CPW dressed algebras $\hat{\mathcal{A}}_R, \hat{\mathcal{A}}_L$ for the two-sided eternal black hole. This week we compute the **dressed entropy** of the TFD vacuum and a coherent state in the free-field Rindler-Rindler analog, recovering the gravitational area law of the eternal-BH horizon. Like the Block 1 Wk 4 mini-calc, but **with both sides at once**: the trace is on the joint dressed algebra; the divergent part of the dressed vacuum entropy reproduces the **bifurcation-surface area** divided by a UV regulator (the eternal-BH analog of $A_{\mathrm{horizon}}/(4G_N)$); the coherent-state difference reproduces $-S(\omega_\alpha\|\omega_{\mathrm{TFD}}) + \mathcal{B}(\omega_\alpha, \omega_{\mathrm{TFD}})$ via Block D Theorem 3.1. The structural picture is "Witten 2022 with two sides." This is the CPW analog of Block 1's mini-calc.*

## 0. Reading

**Primary:**
- Chandrasekaran, Penington, Witten (CPW), arXiv:2209.10454, **§4** (the dressed entropy and generalized entropy identification).
- Sem II Wk 6 (the CPW dressed algebra).
- Sem II Wk 3 (Block 1 derivation of the single-sided dressed entropy = generalized entropy).

**Secondary:**
- Witten, arXiv:2112.12828, §4.
- Liu, arXiv:2510.07017, §6.

**Optional research reading:**
- Faulkner, Lewkowycz, Maldacena, arXiv:1307.2892 (bulk relative entropy = boundary Araki-Uhlmann).
- Jafferis, Lewkowycz, Maldacena, Suh, arXiv:1512.06431 (JLMS: bulk-boundary entropy relation).

## 1. Setup recap

From Week 6:

- $\hat{\mathcal{A}}_R = \mathcal{A}_R \rtimes_{\sigma^{\mathrm{TFD}}}\mathbb{R}$ on $\mathcal{H}_R \otimes \mathcal{H}_L \otimes L^2(\mathbb{R}_s)$, type II$_\infty$.
- $\hat{\mathcal{A}}_L$ analogous; commutes with $\hat{\mathcal{A}}_R$.
- Single clock $L^2(\mathbb{R}_s)$ corresponding to bulk-boost direction.
- Trace formula: $\hat\tau_R(a) = \int e^{-\beta_H s}\langle\mathrm{TFD} \otimes \delta_s|a|\mathrm{TFD}\otimes\delta_s\rangle ds$.

This week we compute the dressed entropy explicitly.

## 2. The dressed entropy and Witten's identification (recap)

From Block 1 Week 3:

**Witten's claim (CPW §4 in two-sided form).** *In the holographic large-$N$ setting, the dressed entropy on $\hat{\mathcal{A}}_R$ in the TFD vacuum equals the bulk generalized entropy:*
$$
\boxed{S_{\mathrm{vN}}(\hat\rho_{\mathrm{TFD}}) = \frac{A_{\mathrm{horizon}}}{4G_N} + S_{\mathrm{out}} + \mathrm{const},}
$$
*where $A_{\mathrm{horizon}}$ is the area of the bifurcation surface (the BH horizon at $r = r_h, t = 0$).*

For two-sided CPW, both $\hat{\mathcal{A}}_R$ and $\hat{\mathcal{A}}_L$ separately have dressed entropies of this form — with the **same** horizon area (the bifurcation surface is shared between the two sides).

### 2.1 Structural derivation: same as Block 1

The argument from Block 1 Week 3 works **identically** in the two-sided setting:

1. **Block D dressed-entropy formula** (Sem I Wk 14 Theorem 3.1):
$$
S_{\mathrm{vN}}(\hat\rho_\omega) - S_{\mathrm{vN}}(\hat\rho_\phi) = -S(\omega\|\phi) + \mathcal{B}(\omega, \phi),
$$
with $\mathcal{B}(\omega, \phi) = \omega(K_\phi) - \phi(K_\phi)$, $K_\phi = -\log\rho_\phi$.

2. **Modular Hamiltonian in TFD** = $\beta_H H_R$ (when restricted to $\mathcal{A}_R$ alone; see Wk 5 §3.3 and Wk 6 §2.2).

3. **Modular boundary term**: $\mathcal{B}(\omega, \omega_{\mathrm{TFD}}) = \beta_H \cdot \big(\omega(H_R) - \omega_{\mathrm{TFD}}(H_R)\big)$.

4. **Holographic identification** (Witten / CPW): the modular boundary term equals $\delta(A/(4G_N))$ via the first law of BH thermodynamics; the Araki–Uhlmann piece equals $\delta S_{\mathrm{out}}$ via FLM.

Integrating along a path of states gives $S_{\mathrm{vN}} = A/(4G_N) + S_{\mathrm{out}} + \mathrm{const}$.

**The two-sided structure adds:**

- The horizon involved is the *bifurcation surface* (where both sides meet).
- The bulk Hilbert space includes both interiors (regions II and IV) — these contribute to $S_{\mathrm{out}}$.
- There are *two* dressed entropies, one per side. By the two-sided structure, they have the same divergent area piece (same horizon) but possibly different bulk-entropy pieces (e.g., different excitations on each boundary).

## 3. The free-field two-sided trace

We now do the explicit computation in the free-field Rindler-Rindler analog. This is **Mini-Calc 2** of the skeleton.

### 3.1 The dressed Hilbert space

Setup (from Week 6 §6): 4D massless free scalar on Minkowski space; $\mathcal{A}(W_R), \mathcal{A}(W_L)$ on Fock space $\mathcal{F}$; Minkowski vacuum is the TFD of the boost; modular Hamiltonian $2\pi(K_R - K_L)$; modular flow on $\mathcal{A}(W_R)$ is the boost.

The dressed algebra: $\hat{\mathcal{A}}(W_R)$ on $\mathcal{F} \otimes L^2(\mathbb{R}_s)$.

### 3.2 The trace

The trace formula (Block 1 Wk 4 §3):
$$
\hat\tau_R(a) = \int_{-\infty}^\infty e^{-2\pi s}\,\langle 0_M\otimes\delta_s\,|\,a\,|\,0_M\otimes\delta_s\rangle\,ds.
$$
Same as Block 1; the only change is the interpretation: $|0_M\rangle$ now plays the role of the two-sided TFD, not just a single-sided thermal state.

For $a = \pi_R(W(f)) \otimes g(X)$ with $f \in W_R$ and $g$ bounded measurable:
$$
\hat\tau_R(\pi_R(W(f)) \otimes g(X)) = \langle 0_M|W(f)|0_M\rangle \cdot \int e^{-2\pi s} g(s)\,ds.
$$

This factorizes into Weyl-vacuum-expectation (which is the Gaussian $e^{-W(f, f)/2}$) and clock integral. Semifinite, not finite.

### 3.3 The same trace for both sides

By the $\mathbb{Z}_2$ symmetry of the eternal-BH geometry, the left-side trace is structurally identical:
$$
\hat\tau_L(b) = \int_{-\infty}^\infty e^{-2\pi s}\,\langle 0_M\otimes\delta_{-s}\,|\,b\,|\,0_M\otimes\delta_{-s}\rangle\,ds.
$$
(The $-s$ comes from the opposite-direction modular flow on $\mathcal{A}_L$; equivalently, the clock variable runs backward.)

For computational purposes in the symmetric case (both sides excited symmetrically), the two traces give the same numerical answer.

## 4. The dressed TFD entropy: area law

### 4.1 The dressed TFD state

Define $\hat\omega_{\mathrm{TFD}}$ on $\hat{\mathcal{A}}(W_R)$:
$$
\hat\omega_{\mathrm{TFD}}(a) := \langle 0_M \otimes h\,|\,a\,|\,0_M \otimes h\rangle,
$$
with $h \in L^2(\mathbb{R}_s)$ normalized.

### 4.2 The density relative to the trace

By the same calculation as Block 1 Wk 4 §4.2, the density of $\hat\omega_{\mathrm{TFD}}$ relative to $\hat\tau_R$ is
$$
\hat\rho_d^{\mathrm{TFD}} = 1_\mathcal{F} \otimes |h(s)|^2\,e^{2\pi s}.
$$

### 4.3 Dressed TFD entropy

By the formula derived in Block 1 Wk 4 §4.4:
$$
S_{\mathrm{vN}}(\hat\omega_{\mathrm{TFD}}) = S_{\mathrm{clock}}(h) - 2\pi\,\langle X\rangle_h,
$$
where $S_{\mathrm{clock}}(h) = -\int|h(s)|^2\log|h(s)|^2 ds$ is the Shannon entropy of the clock and $\langle X\rangle_h = \int s|h(s)|^2 ds$ is the clock-position expectation.

**Identification with the gravitational area law.** The term $-2\pi\langle X\rangle_h$ is the **modular-Hamiltonian expectation** in the dressed vacuum. In the gravitational case (with $2\pi \to \beta_H$ and the corresponding rescaling), this becomes
$$
-\beta_H\,\langle X\rangle_h \;\xrightarrow{\text{holographic}}\; -\delta\!\left(\frac{A_{\mathrm{horizon}}}{4G_N}\right).
$$

(Sign caveats: the absolute sign depends on the choice of clock state; for the natural "ground-clock" choice $h$ peaked near $s = 0$, $\langle X\rangle_h \approx 0$ and the entropy is dominated by $S_{\mathrm{clock}}$. The UV-divergent area-law piece emerges when $h$ is sharply peaked, with $S_{\mathrm{clock}}(h)$ diverging like $\log\sigma$ where $\sigma$ is the clock width.)

The structural conclusion: the divergent piece of the dressed TFD entropy scales as the **transverse area** of the wedge boundary in 4D, divided by a UV regulator. Identifying the regulator with $\ell_{\mathrm{Planck}}$, this is the algebraic origin of $A/(4G_N)$.

## 5. Coherent-state difference

### 5.1 Setup

Take a coherent state $|\alpha\rangle = W(f)|0_M\rangle$ with $f$ supported in $W_R$. The corresponding state on $\mathcal{A}(W_R)$ is $\omega_\alpha$.

Dress: $\hat\rho_\alpha(a) = \langle\alpha \otimes h\,|\,a\,|\,\alpha \otimes h\rangle$ with the *same* clock state $h$.

### 5.2 Dressed-entropy difference

By Block D Theorem 3.1:
$$
S_{\mathrm{vN}}(\hat\rho_\alpha) - S_{\mathrm{vN}}(\hat\omega_{\mathrm{TFD}}) = -S(\omega_\alpha\|\omega_0) + \mathcal{B}(\omega_\alpha, \omega_0),
$$
where $\omega_0 = \omega_{\mathrm{TFD}}$ here (the Minkowski vacuum restricted to $\mathcal{A}(W_R)$).

### 5.3 The Araki-Uhlmann piece

By Sem I Wk 7 §7.3 (Araki–Uhlmann for coherent states in free-field theory):
$$
S(\omega_\alpha\|\omega_0) = \pi\,\sigma(f, P f),
$$
where $P = \tanh(\pi K_{\mathrm{boost}})$ is a positive operator from the modular Hamiltonian.

For small $f$, this scales as $\|f\|^2$ (in an appropriate norm). For $f$ approaching the wedge boundary (boost-limit), it diverges.

### 5.4 The modular boundary term

$\mathcal{B}(\omega_\alpha, \omega_0) = \omega_\alpha(K_{\omega_0}) - \omega_0(K_{\omega_0}) = 2\pi(\omega_\alpha(K_{\mathrm{boost}}) - 0)$, since $\omega_0(K_{\mathrm{boost}}) = 0$ (vacuum-annihilated).

$\omega_\alpha(K_{\mathrm{boost}}) = \langle 0|W(f)^* K_{\mathrm{boost}} W(f)|0\rangle$ — the "boost-energy" carried by the coherent excitation. For a Gaussian bump $f$ at fixed position $\xi_0$ in $W_R$, this is **finite** and scales as $|f|^2 \cdot \xi_0$ (the boost energy at boost-coordinate $\xi_0$).

### 5.5 Result

$$
S_{\mathrm{vN}}(\hat\rho_\alpha) - S_{\mathrm{vN}}(\hat\omega_{\mathrm{TFD}}) = -\pi\sigma(f, Pf) + 2\pi\,\omega_\alpha(K_{\mathrm{boost}}).
$$

**Both pieces finite** for compactly-supported $f$. The UV-divergent area-law piece cancels in the difference. This is the algebraic-entropy difference between a coherent excitation and the dressed TFD vacuum.

### 5.6 Identification with bulk-side $\Delta S_{\mathrm{gen}}$

Under the holographic dictionary:
- $-\pi\sigma(f, Pf) \to -\delta S_{\mathrm{out}}$ (the bulk-entanglement piece, by FLM).
- $2\pi\,\omega_\alpha(K_{\mathrm{boost}}) \to \delta(A/(4G_N))$ (the area piece, by the first law).

So $S_{\mathrm{vN}}(\hat\rho_\alpha) - S_{\mathrm{vN}}(\hat\omega_{\mathrm{TFD}}) = \delta S_{\mathrm{out}} + \delta(A/(4G_N)) = \delta S_{\mathrm{gen}}$, the bulk generalized-entropy difference.

**Verified.** In the free-field two-sided Rindler analog, the dressed-entropy formula reproduces the algebraic structure of $S_{\mathrm{gen}}$.

## 6. Area-law check in detail

A more pedagogical version of §4's structural statement. We will identify the leading $\epsilon$-divergence of $S_{\mathrm{vN}}(\hat\omega_{\mathrm{TFD}})$ with the wedge boundary area.

### 6.1 The naive vacuum entanglement

In QFT, the entanglement entropy of the vacuum state across a co-dimension-1 surface is *divergent*. For a $d$-dimensional QFT in flat spacetime, the leading divergence scales as $A/\epsilon^{d-1}$ where $A$ is the area of the surface and $\epsilon$ is a UV regulator (e.g., a lattice spacing or short-distance cutoff). This is the **area law** of vacuum entanglement entropy (Bombelli et al. 1986; Srednicki 1993).

For 4D massless free scalar restricted to $W_R$, the area of the wedge boundary is *infinite* (it is the whole $\{x^1 = 0\}$ hyperplane). But for a *finite* region (e.g., a sphere of radius $R$ at $x^1 = 0$ at fixed time), the area is $4\pi R^2$ and the leading divergence is $4\pi R^2 / \epsilon^2$.

### 6.2 Recovering this from the dressed entropy

The dressed TFD entropy $S_{\mathrm{vN}}(\hat\omega_{\mathrm{TFD}}) = S_{\mathrm{clock}}(h) - 2\pi\langle X\rangle_h$ is a **1-dimensional** quantity (1D modular-time clock). The transverse 2D area at the wedge boundary is **not** directly encoded in this formula — instead, it would emerge in a fully-mode-resolved calculation that includes the transverse modes (frequencies of the field perpendicular to the boost direction).

In a coarse pedagogical sense: the modular structure of the wedge algebra has a *1-parameter* modular flow (the boost rapidity), but the full vacuum entanglement involves *all modes* of the free scalar. The dressed-entropy formula captures the modular sector; the full area law requires integrating over transverse modes.

A more careful calculation (Bombelli–Koul–Lee–Sorkin, Srednicki):
$$
S_{\mathrm{vN}}^{\mathrm{full}}(\hat\omega_{\mathrm{TFD}}) = \int \rho(\omega)\,S_\omega\,d\omega \cdot A_\perp / \epsilon^2 + \text{subleading},
$$
where $\rho(\omega)$ is a density of transverse modes, $S_\omega$ is the per-mode contribution, and $A_\perp$ is the transverse area. The integral over $\omega$ gives a UV-divergent prefactor; multiplied by $A_\perp$ gives the area-law divergence.

### 6.3 The structural takeaway

The 1D modular-time clock captures the **structural** part of the area law (logarithmic divergence in $\sigma \to 0$); the full multi-dimensional area law $A/\epsilon^{d-1}$ requires resolving all transverse modes.

The CPW (and Witten 2022) dressed-entropy formula gives the algebraic **skeleton** of the area law. The full coefficient, with the right area-of-transverse-section dimension, requires the full QFT regulator. We do not derive the full coefficient $1/(4G_N)$ from the algebraic structure alone — that's the holographic dictionary input.

### 6.4 Match with Block 1 Wk 4

This is the same conclusion as Block 1 Wk 4 §4.4: **the dressed entropy has the structural form of $S_{\mathrm{gen}}$, but the coefficient $1/(4G_N)$ comes from the holographic dictionary, not from the algebra alone.**

The CPW two-sided case adds: the divergent area piece is the **same** on both sides (because both algebras share the bifurcation surface), and the total generalized entropy for the two-sided BH is *one copy* of $A/(4G_N)$ (not two), consistent with the bulk fact that the eternal BH has a single horizon.

## 7. Comparison with the single-sided story

### 7.1 What's the same

The structural derivation in §2 and the mini-calc in §3–5 are **identical** to Block 1 Wk 4. Algebraically, two-sided CPW = single-sided Witten 2022, with the joint Hilbert space $\mathcal{H}_R \otimes \mathcal{H}_L$ replacing $\mathcal{H}_R$.

### 7.2 What's new

The two-sided structure adds:

1. **The horizon is the bifurcation surface**, shared between the two sides. In the single-sided story (Block 1), the "horizon" was a hypothetical entanglement surface (e.g., the RT surface for the boundary subregion); in the two-sided story, it is the unambiguous BH horizon of the eternal-BH geometry.

2. **Two dressed entropies, one structure.** $S_{\mathrm{vN}}(\hat\rho^{R}_{\mathrm{TFD}}) = S_{\mathrm{vN}}(\hat\rho^{L}_{\mathrm{TFD}})$ by symmetry, but both equal the *same* $A_{\mathrm{horizon}}/(4G_N) + S_{\mathrm{out}}$. The two-sided structure makes this redundancy manifest.

3. **The bulk interior contribution.** $S_{\mathrm{out}}$ now includes bulk fields in the interior regions (II and IV in the Penrose diagram), not just the exterior. The bulk-entanglement piece is genuinely two-sided.

### 7.3 What's NOT new

The algebraic computation is **not new** — every step uses Block D + Block 1 machinery. The novelty of CPW (relative to Witten 2022) is the **physical setting** (eternal BH, TFD), not the algebraic technique.

This is consistent with Block 2's structural goal: extend Witten 2022 to the two-sided BH, identify what new physical content emerges (the bulk-Killing-vector structure, ER=EPR, etc.), but reuse the operator-algebra machinery wholesale.

## 8. Bell-CHSH preview

A brief look ahead to Week 8.

The two-sided structure has one **purely new** content not available in the single-sided setting: **Bell-type correlations between the two sides**. The Minkowski vacuum is maximally entangled between $\mathcal{A}(W_R)$ and $\mathcal{A}(W_L)$ in the algebraic sense (Sem I Wk 11: Tsirelson saturation). The two-sided structure makes this a *physically interesting* statement about the eternal BH.

Week 8 computes the Bell-CHSH correlator $\langle\mathrm{TFD}|\mathcal{C}|\mathrm{TFD}\rangle$ for cosine-Weyl observables on the two-sided wedge algebras. This is Mini-Calc 3 of the skeleton.

The connection: **ER=EPR and Bell-CHSH saturation are two faces of the same algebraic structure**. The TFD's modular Hamiltonian $\beta_H(H_R - H_L)$ and the resulting type III$_1$ joint structure are what allow both the Tsirelson saturation (Sem I Wk 11) and the ER bridge (this block).

> **Physical picture.** Bell–CHSH gives the two-sided story an *operational* edge that entropy formulas lack. Entropies are not observables — no single experiment measures $S_{\mathrm{gen}}$. A CHSH correlator, by contrast, is a finite combination of bounded expectation values: something two observers, one outside each asymptotic region, could in principle measure by exchanging classical records. Saturation of the Tsirelson bound between the two boundary algebras is therefore an *operational certificate* of the maximal entanglement that ER=EPR geometrizes. If a candidate microstate geometry failed to saturate (as a product of two thermal states would, having no cross-correlations at all), the failure would be detectable by bounded measurements. Week 8 builds exactly this certificate in the free-field analog.

## 9. What to take away

- **Dressed entropy on $\hat{\mathcal{A}}_R$ in TFD vacuum:** $S_{\mathrm{vN}}(\hat\omega_{\mathrm{TFD}}) = S_{\mathrm{clock}}(h) - 2\pi\langle X\rangle_h$ in the free-field analog.
- **Witten-CPW identification (Witten 2022 §4 + CPW §4):** in the holographic large-$N$ setting, $S_{\mathrm{vN}}(\hat\rho_{\mathrm{TFD}}) = A_{\mathrm{horizon}}/(4G_N) + S_{\mathrm{out}} + \mathrm{const}$. Same horizon (the bifurcation surface) for both sides.
- **Algebraic vs. holographic content:** the *structural form* $S_{\mathrm{vN}} = $ (modular energy) $-$ (Araki–Uhlmann) $+$ const is algebraic (Block D Theorem 3.1). The *coefficient $1/(4G_N)$* and the identification with the gravitational area come from the holographic dictionary, not from the algebra alone.
- **Coherent-state difference:** $S_{\mathrm{vN}}(\hat\rho_\alpha) - S_{\mathrm{vN}}(\hat\omega_{\mathrm{TFD}}) = -\pi\sigma(f, Pf) + 2\pi\,\omega_\alpha(K_{\mathrm{boost}})$, both pieces finite. Verifies $\delta S_{\mathrm{gen}} = \delta S_{\mathrm{out}} + \delta(A/(4G_N))$ structurally.
- **Area-law structural recovery:** the dressed-entropy formula captures the structural part of the area law (logarithmic divergence in clock width), but the full multi-dimensional area requires resolving transverse QFT modes.
- **CPW = Witten 2022 with two sides:** algebraically identical to Block 1; new physics is the two-sided/TFD physical setting (eternal-BH horizon, bulk Killing vector, ER=EPR).

## 10. Looking ahead

Week 8 closes Block 2 with **Bell-CHSH between the two sides** — the algebraic content of "ER=EPR." Concretely: take cosine-Weyl observables on $\mathcal{A}(W_R)$ and $\mathcal{A}(W_L)$ in the Minkowski vacuum and compute $\langle\mathrm{TFD}|\mathcal{C}_{\mathrm{CHSH}}|\mathrm{TFD}\rangle$. By Summers-Werner (Sem I Wk 11), this approaches the Tsirelson bound $2\sqrt 2$. The mini-calc gives explicit numerical values from the bumpified-Haar-wavelet construction of the group's research program.

## 11. Problem set

**Core problems.**

**1. Two-sided trace formula.** Verify the trace formula
$$
\hat\tau_R(a) = \int e^{-2\pi s}\langle 0_M\otimes\delta_s|a|0_M\otimes\delta_s\rangle ds
$$
on the two-sided dressed algebra $\hat{\mathcal{A}}(W_R)$ for operators $a = \pi_R(W(f)) \otimes g(X)$. Compare with the Block 1 Wk 4 §3 single-sided formula — they're identical.

**2. Dressed TFD entropy.** Compute $S_{\mathrm{vN}}(\hat\omega_{\mathrm{TFD}}) = S_{\mathrm{clock}}(h) - 2\pi\langle X\rangle_h$ for the Gaussian clock $h(s) = (2\pi\sigma^2)^{-1/4} e^{-s^2/(4\sigma^2)}$ and verify the area-law-like divergence as $\sigma \to 0$.

**3. Coherent-state difference.** Take $|\alpha\rangle = W(f)|0_M\rangle$ with $f$ a Gaussian bump in $W_R$ at boost coordinate $\xi_0$. Compute $\omega_\alpha(K_{\mathrm{boost}})$ to leading order in $|f|^2$ and verify it is finite.

**4. Verify Block D Theorem 3.1 in the free-field two-sided setting.** Combine Problem 2 (vacuum entropy) and Problem 3 (coherent-state boundary term) and verify
$$
S_{\mathrm{vN}}(\hat\rho_\alpha) - S_{\mathrm{vN}}(\hat\omega_{\mathrm{TFD}}) = -\pi\sigma(f, Pf) + 2\pi\omega_\alpha(K_{\mathrm{boost}})
$$
for small $|f|^2$.

**5. Read CPW §4.** Identify CPW's explicit form of the dressed-entropy formula and the identification with $A/(4G_N) + S_{\mathrm{out}}$. Compare with our exposition.

**Starred problems.**

**6\*. The area-of-bifurcation-surface in 4D Rindler.** For the right Rindler wedge in 4D Minkowski space, the bifurcation surface is $\{x^0 = x^1 = 0\}$ — an infinite 2-plane. Truncating to a sphere of radius $R$ in the transverse $(x^2, x^3)$ directions, the area is $\pi R^2$. Sketch how this area enters the leading divergence of the vacuum entanglement entropy. Compare with the Bombelli-Koul-Lee-Sorkin 1986 result.

**7\*. Two-sided coherent excitation.** Take a coherent state with separate excitations $f_R \in W_R$ and $f_L \in W_L$. Compute $S_{\mathrm{vN}}(\hat\rho_{\alpha_R, \alpha_L}) - S_{\mathrm{vN}}(\hat\omega_{\mathrm{TFD}})$ for the two-sided state. How does the result split between the two sides?

**8\*. Eternal-BH bulk-entropy piece.** In the eternal AdS-Schwarzschild BH, the bulk fields in the *interior* regions (II and IV) contribute to $S_{\mathrm{out}}$. Sketch what this looks like in the bulk picture: which bulk modes are responsible? (See CPW §4 for the precise statement.)

**9\*. The state-independent constant.** In CPW §4, the state-independent constant in $S_{\mathrm{vN}} = A/(4G_N) + S_{\mathrm{out}} + \mathrm{const}$ depends on which clock state $h$ is chosen for the dressing. Identify the dependence: how does shifting $h$ shift the constant?

**Project problems.**

**10. Read CPW §§4–5.** Identify the precise hypotheses CPW use for the generalized-entropy identification. Compare with Witten 2022 §4 (single-sided) and identify the structural overlap.

**11. Quantum extremal surface prescription.** Read Engelhardt-Wall 2014 (arXiv:1408.3203) §§1–2. Identify how the CPW dressed-entropy formula relates to the QES prescription of extremizing $S_{\mathrm{gen}}(\gamma)$ over bulk surfaces. Where does the *choice* of $\gamma$ enter the dressed-entropy framework? (The CPW story fixes $\gamma = $ horizon, so the extremization is trivial there.)

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 2. Last revised 2026-06-11.*
