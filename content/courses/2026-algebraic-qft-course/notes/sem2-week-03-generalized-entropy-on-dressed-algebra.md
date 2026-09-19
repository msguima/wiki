---
title: "Sem II Week 3 — Generalized Entropy on the Dressed Algebra"
type: lecture-notes
course: syllabus
semester: 2
week: 3
block: 1
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Sem II Weeks 1–2; Sem I Wk 14 (dressed entropy); Sem I Wk 15 (TFD bridge)
target_paper: "Witten, arXiv:2112.12828 §4"
modified: 2026-06-11
---

# Sem II Week 3 — Generalized Entropy on the Dressed Algebra

> *Last week we built the dressed boundary algebra $\hat{\mathcal{A}}_R = \mathcal{A}_R \rtimes_{\mathrm{ADM}}\mathbb{R}$ — type II$_\infty$ with a faithful normal semifinite trace. This week we use that trace to define a **dressed von Neumann entropy** and prove Witten 2022's central claim: in the holographic setting at large $N$, the dressed entropy equals the gravitational **generalized entropy** $A/(4G_N) + S_{\mathrm{out}}$ up to a state-independent additive constant. The derivation has two ingredients — the Block D dressed-entropy formula (Sem I Wk 14 Theorem 3.1) and a **holographic identification of the modular boundary term with the area term** — and Witten 2022's contribution is the second.*

## 0. Reading

**Primary:**
- Witten, "Gravity and the crossed product," arXiv:2112.12828, **§4** (the dressed entropy and the generalized entropy identification).
- Sem I Wk 14 (Block D dressed entropy formula and Theorem 3.1).

**Secondary:**
- Liu, arXiv:2510.07017, **§§6–7** (semiclassical limits, generalized entropy in holography).
- Lewkowycz & Maldacena, "Generalized gravitational entropy," *JHEP* 08 (2013) 090, arXiv:1304.4926 (the canonical derivation of generalized entropy from the bulk replica trick).

**Optional research reading:**
- Faulkner, Lewkowycz, Maldacena, "Quantum corrections to holographic entanglement entropy," *JHEP* 11 (2013) 074, arXiv:1307.2892 (the bulk-entropy term $S_{\mathrm{out}}$).
- Engelhardt & Wall, "Quantum extremal surfaces: holographic entanglement entropy beyond the classical regime," *JHEP* 01 (2015) 073, arXiv:1408.3203 (extremal surface formulation).

## 1. Recap and setup

### 1.1 What we have

From Week 2:

- The dressed algebra $\hat{\mathcal{A}}_R = \mathcal{A}_R \rtimes_{\mathrm{ADM}}\mathbb{R}$ is **type II$_\infty$** with faithful normal semifinite trace $\hat\tau$.
- The original boundary algebra embeds via $\pi: \mathcal{A}_R \hookrightarrow \hat{\mathcal{A}}_R$ as the fixed-point subalgebra of the dual action.
- The modular flow $\sigma^{\mathrm{TFD}}$ becomes inner on $\hat{\mathcal{A}}_R$ via the clock unitary $\lambda(t)$.
- Trace formula: $\hat\tau(a) = \int e^{-\beta_H s}\,\langle\mathrm{TFD}\otimes\delta_s\,|\,a\,|\,\mathrm{TFD}\otimes\delta_s\rangle\,ds$.

From Sem I Wk 14:

- On the dressed algebra, the von Neumann entropy is $S_{\mathrm{vN}}(\hat\rho) = -\hat\tau(\hat\rho_d\,\log\hat\rho_d)$, finite up to a state-independent additive constant from trace rescaling.
- Theorem 3.1: dressed-entropy differences = $-S(\omega\|\phi) + \mathcal{B}(\omega, \phi)$ where $\mathcal{B}(\omega, \phi) = \omega(K_\phi) - \phi(K_\phi)$ is the modular boundary term.

### 1.2 What Witten 2022 §4 adds

The new physics input this week:

**Witten's identification.** *In the holographic setting at large $N$, the dressed von Neumann entropy on $\hat{\mathcal{A}}_R$ equals the bulk generalized entropy:*
$$
S_{\mathrm{vN}}(\hat\rho) \;=\; \frac{A_{\mathrm{horizon}}}{4 G_N} + S_{\mathrm{out}}(\rho) + \mathrm{const}.
$$

The construction is structurally:

1. Take the boundary subregion.
2. Form the dressed algebra (Week 2).
3. Compute the dressed entropy on this algebra.
4. **Recognize:** the divergent piece reproduces $A/(4G_N)$ — the Bekenstein–Hawking entropy of the horizon; the finite piece reproduces $S_{\mathrm{out}}$ — the bulk entanglement entropy outside the horizon.

The identification is the **holographic-dictionary input** beyond the algebra-level construction.

### 1.3 Strategy of this lecture

We do not derive Witten's identification line-by-line from scratch — it requires holographic-dictionary input we have not built up (see §6 below). Instead:

1. **§2:** Write the dressed entropy on $\hat{\mathcal{A}}_R$ and identify its structural pieces.
2. **§3:** Recall the Block D modular-boundary-term formula (Sem I Wk 14 §3) and apply it.
3. **§4:** Witten's holographic identification: modular boundary term = area term modulo a state-independent constant.
4. **§5:** The generalized-entropy formula as Witten's central claim.
5. **§6:** Consistency checks via the free-field Rindler analog (full computation in Week 4).

## 2. The dressed entropy

### 2.1 Definition

The dressed boundary algebra $\hat{\mathcal{A}}_R$ is type II$_\infty$, so any normal state $\hat\rho$ on $\hat{\mathcal{A}}_R$ has a density $\hat\rho_d$ relative to the trace $\hat\tau$ (Sem I Wk 14 §2.2):
$$
\hat\rho(x) = \hat\tau(\hat\rho_d\,x) \quad \text{for all } x \in \hat{\mathcal{A}}_R.
$$

**Definition 2.1.** The **dressed von Neumann entropy** of $\hat\rho$ is
$$
S_{\mathrm{vN}}(\hat\rho) := -\hat\tau(\hat\rho_d\,\log\hat\rho_d).
$$

This is well-defined (finite or $+\infty$) and depends on the choice of trace $\hat\tau$ only up to a state-independent additive constant.

### 2.2 The TFD dressed state

The canonical reference state is the dressing of the TFD vacuum:
$$
\hat\rho_{\mathrm{TFD}}(a) := \langle\mathrm{TFD}\otimes h\,|\,a\,|\,\mathrm{TFD}\otimes h\rangle, \qquad a \in \hat{\mathcal{A}}_R,
$$
where $h \in L^2(\mathbb{R}_s)$ is a clock state — say a Gaussian or exponential cutoff. (The precise choice affects only the additive constant.)

The density $\hat\rho_d^{\mathrm{TFD}}$ relative to $\hat\tau$ satisfies $\hat\rho_d^{\mathrm{TFD}} \propto |h(X)|^2 \cdot e^{\beta_H X}$ on the clock dimension (schematically; details in §5 below).

### 2.3 The state-independent constant

Rescaling the trace $\hat\tau \to c\hat\tau$ shifts $S_{\mathrm{vN}} \to S_{\mathrm{vN}} - \log c$ (Sem I Wk 14 §2.3). All dressed entropies shift by the same constant — so **differences** $S_{\mathrm{vN}}(\hat\rho_1) - S_{\mathrm{vN}}(\hat\rho_2)$ are trace-rescaling invariant and unambiguous.

The additive constant absorbs the choice of clock normalization, the regulator implicit in the trace kernel, and (in the holographic case) the choice of additive normalization of the gravitational free energy. It is **not physically irrelevant**: the Bekenstein–Hawking entropy formula $A/(4G_N)$ has a canonical absolute normalization fixed by the on-shell gravitational action. The match with $S_{\mathrm{vN}}$ is up to this single global constant.

## 3. Differences and the modular boundary term

The most useful formula is for differences, where the constant drops out.

### 3.1 The Block D formula

**Theorem 3.1 (Block D dressed-entropy difference, Sem I Wk 14). [Stated only.]** *For two faithful normal states $\omega, \phi$ on $\mathcal{A}_R$ and their dressings $\hat\rho_\omega, \hat\rho_\phi$ on $\hat{\mathcal{A}}_R$ (constructed with a fixed clock normalization),*
$$
S_{\mathrm{vN}}(\hat\rho_\omega) - S_{\mathrm{vN}}(\hat\rho_\phi) = -S(\omega\|\phi) + \mathcal{B}(\omega, \phi),
$$
*where $S(\omega\|\phi)$ is the Araki–Uhlmann relative entropy on $\mathcal{A}_R$ and $\mathcal{B}(\omega, \phi) = \omega(K_\phi) - \phi(K_\phi)$ is the modular boundary term, with $K_\phi = -\log\rho_\phi$ the modular Hamiltonian of the reference state.*

### 3.2 In the holographic setting

Specializing to the holographic case with $\omega = $ excited state and $\phi = $ TFD vacuum:
$$
S_{\mathrm{vN}}(\hat\rho_\omega) - S_{\mathrm{vN}}(\hat\rho_{\mathrm{TFD}}) = -S(\omega\|\omega_{\mathrm{TFD}}) + \big(\omega(K_{\mathrm{TFD}}) - \omega_{\mathrm{TFD}}(K_{\mathrm{TFD}})\big),
$$
where $K_{\mathrm{TFD}} = -\log\rho_{\mathrm{TFD}}$ is the modular Hamiltonian of the TFD on $\mathcal{A}_R$.

### 3.3 What the modular boundary term is

By Witten 2022 §2 (and Week 1 Theorem 5.1), the modular Hamiltonian on $\mathcal{A}_R$ in the TFD vacuum is **proportional to the ADM Hamiltonian**:
$$
K_{\mathrm{TFD}} = \beta_H\,H_R + \mathrm{const}.
$$

(The constant is the offset $-\log Z(\beta_H)$ from the formal Gibbs density $\rho_{\mathrm{TFD}} = e^{-\beta_H H_R}/Z$; it drops out in $\mathcal{B}$.)

So the modular boundary term is the **ADM-energy difference between $\omega$ and the TFD vacuum**, multiplied by $\beta_H$:
$$
\mathcal{B}(\omega, \omega_{\mathrm{TFD}}) = \beta_H\,\big(\omega(H_R) - \omega_{\mathrm{TFD}}(H_R)\big).
$$

This is the **first law of thermodynamics applied to the boundary**: the modular-Hamiltonian expectation is the average energy at inverse temperature $\beta_H$. Differences between two states are $\beta_H \times$ energy differences.

## 4. Witten's holographic identification

### 4.1 The first-law structure on both sides

In the **boundary** algebraic setting:
$$
S_{\mathrm{vN}}(\hat\rho_\omega) - S_{\mathrm{vN}}(\hat\rho_{\mathrm{TFD}}) = -S(\omega\|\omega_{\mathrm{TFD}}) + \beta_H \cdot \big(\omega(H_R) - \omega_{\mathrm{TFD}}(H_R)\big).
$$

In the **bulk** gravitational setting, the **first law of black-hole thermodynamics** says:
$$
\delta S_{\mathrm{BH}} = \beta_H\,\delta M_{\mathrm{ADM}} - (\text{work terms}),
$$
where $S_{\mathrm{BH}} = A_{\mathrm{horizon}}/(4 G_N)$. For a small perturbation from the TFD reference, the entropy variation $\delta S_{\mathrm{BH}}$ relates to the ADM-mass variation $\delta M$ via the inverse Hawking temperature.

**Witten's identification (§4):** the **modular boundary term** in the algebraic formula equals the **classical area variation** $\beta_H \cdot \delta M = \delta(A/(4G_N))$:
$$
\mathcal{B}(\omega, \omega_{\mathrm{TFD}}) = \beta_H\big(\omega(H_R) - \omega_{\mathrm{TFD}}(H_R)\big) \;\overset{?}{=}\; \delta\!\left(\frac{A_{\mathrm{horizon}}}{4 G_N}\right).
$$

This is **not** a structural identity — it requires the holographic dictionary, specifically that ADM-mass perturbations on the boundary correspond to horizon-area changes in the bulk. The Smarr formula and the first law of black-hole thermodynamics give this correspondence, and Witten 2022 §4 invokes it.

### 4.2 The Araki–Uhlmann relative entropy = bulk entanglement difference

The other piece of the difference formula is $-S(\omega\|\omega_{\mathrm{TFD}})$. By the bulk-side identification (Faulkner–Lewkowycz–Maldacena 2013, Jafferis–Lewkowycz–Maldacena–Suh 2015):

**The Araki–Uhlmann relative entropy of two boundary states on $\mathcal{A}_R$ equals the bulk relative entropy of the dual bulk states across the horizon.**

For small excitations of the TFD vacuum, this is:
$$
S(\omega\|\omega_{\mathrm{TFD}}) = S(\omega_{\mathrm{out, bulk}}\,\|\,\omega_{\mathrm{TFD,out,bulk}}) + O(1/N^2),
$$
where the right side is the relative entropy of bulk states on the exterior region of the horizon.

Equivalently, for the dressed-entropy difference:
$$
S_{\mathrm{vN}}(\hat\rho_\omega) - S_{\mathrm{vN}}(\hat\rho_{\mathrm{TFD}}) = -S(\omega_{\mathrm{out}} \| \omega_{\mathrm{TFD, out}}) + \delta\!\left(\frac{A_{\mathrm{horizon}}}{4G_N}\right),
$$
which rearranges to
$$
S_{\mathrm{vN}}(\hat\rho_\omega) - S_{\mathrm{vN}}(\hat\rho_{\mathrm{TFD}}) = \delta S_{\mathrm{gen}},
$$
where $\delta S_{\mathrm{gen}} = \delta(A/(4G_N)) + \delta S_{\mathrm{out}}$ is the change in generalized entropy.

### 4.3 The full generalized-entropy formula

Integrating over a path of states from TFD to $\omega$, and absorbing the integration constant into the state-independent additive ambiguity:
$$
\boxed{S_{\mathrm{vN}}(\hat\rho) \;=\; \frac{A_{\mathrm{horizon}}}{4 G_N} + S_{\mathrm{out}}(\rho) + \mathrm{const}.}
$$

**This is Witten 2022's central result.** The dressed entropy of the boundary algebra at large $N$ equals the generalized entropy of the bulk wedge.

> **Physical picture: why $S_{\rm gen}$ is better-defined than its parts.** A long-standing semiclassical observation (Bekenstein; sharpened by Wall) is that the two terms of $S_{\mathrm{gen}} = A/4G_N + S_{\mathrm{out}}$ are separately cutoff-dependent — the UV divergence of $S_{\mathrm{out}}$ is absorbed by the renormalization of $G_N$ in the area term — while their *sum* is cutoff-independent. Before the crossed product, this looked like a fortunate conspiracy. The algebraic result explains it structurally: the two terms are not independent objects at all, but a regulator-dependent *split* of a single well-defined quantity — the type II von Neumann entropy of the dressed algebra. $S_{\mathrm{out}}$ alone is ill-defined because it is the entropy of a type III algebra; $A/4G_N$ alone is the modular/clock contribution whose normalization is the trace-rescaling ambiguity; only the combination is an invariant of $(\hat{\mathcal{A}}_R, \hat\rho)$. The moral, in one line: **generalized entropy is not "area plus matter entropy" — it is the entropy of the gravitationally dressed algebra, which only decomposes into those two pieces after a choice of regulator.** This is arguably the deepest conceptual payoff of the entire course.

## 5. Structural separation: what's algebraic, what's holographic

It is important to keep the algebraic and physics pieces separate (Codex audit caution; Sem II Wk 15 §3.4).

### 5.1 The algebraic part

The Block D dressed-entropy formula
$$
S_{\mathrm{vN}}(\hat\rho_\omega) - S_{\mathrm{vN}}(\hat\rho_\phi) = -S(\omega\|\phi) + \mathcal{B}(\omega, \phi)
$$
is **purely operator-algebraic** (Sem I Wk 14 Theorem 3.1). It requires no holographic input. It holds for any type III$_1$ algebra with modular crossed product.

### 5.2 The holographic part

The identification $\mathcal{B}(\omega, \omega_{\mathrm{TFD}}) = \delta(A/(4G_N))$ is **specifically holographic**. It requires:

1. The boundary CFT is dual to a bulk gravity theory at large $N$.
2. The modular Hamiltonian of the boundary subregion equals (proportional to) the ADM Hamiltonian.
3. ADM-mass variations equal $\beta_H^{-1} \cdot$ horizon-area variations (first law of black-hole thermodynamics).

Similarly, $S(\omega\|\omega_{\mathrm{TFD}}) = S(\omega_{\mathrm{out}}\|\omega_{\mathrm{TFD, out}})$ is **holographic** (Faulkner–Lewkowycz–Maldacena), not algebraic. It uses the bulk-boundary correspondence at the level of relative entropy across the horizon.

### 5.3 Why both pieces are needed

The algebraic part alone gives:
$$
\Delta S_{\mathrm{vN}} = -S(\omega\|\phi) + \mathcal{B}(\omega, \phi),
$$
which is a statement about boundary states only. The holographic input maps both pieces to bulk quantities:
$$
-S(\omega\|\phi) \to -S(\omega_{\mathrm{out}}\|\phi_{\mathrm{out}}), \qquad \mathcal{B}(\omega, \phi) \to \delta(A/(4G_N)).
$$
Combined: $\Delta S_{\mathrm{vN}} = \Delta S_{\mathrm{out}} + \Delta(A/(4G_N)) = \Delta S_{\mathrm{gen}}$, recovering the generalized entropy.

**The algebraic crossed product is not literally "gravity"** — it is the operator-algebraic skeleton. The gravitational identification is an additional theorem of holographic QFT.

## 6. Worked example (preview): free-field Rindler

Week 4 does this in full; here we preview the structure.

In the free-field Rindler analog (Sem I Wk 14 §5):
- $\mathcal{A}_R \to \mathcal{A}(W_R)$ (right Rindler wedge of 4D massless free scalar).
- $H_R \to K_R = 2\pi K_{\mathrm{boost}}$ (the boost generator; Bisognano–Wichmann).
- $\beta_H \to 2\pi$ (Unruh temperature for unit acceleration).
- Modular Hamiltonian: $K_{\mathrm{TFD}} = 2\pi K_{\mathrm{boost}}$ in this case.

### 6.1 The dressed-vacuum entropy

For the Minkowski vacuum on $\mathcal{A}(W_R)$ dressed to $\hat\omega_0$ on $\hat{\mathcal{A}}(W_R)$:

The dressed entropy of $\hat\omega_0$ is dominated by a divergent contribution from the modular Hamiltonian's expectation:
$$
S_{\mathrm{vN}}(\hat\omega_0) \sim 2\pi\,\langle K_{\mathrm{boost}}\rangle_{\hat\omega_0} \sim \frac{2\pi \cdot \text{(boundary area)}}{\epsilon^{d-1}} + \mathrm{finite},
$$
where $\epsilon$ is a UV regulator. This is exactly the standard area-law divergence of vacuum entanglement entropy in QFT (Bombelli et al. 1986; Srednicki 1993).

### 6.2 The free-field area law

The leading divergent term scales as the **area of the wedge boundary** divided by a UV cutoff. This is the algebraic analog of $A/(4G_N)$:
$$
S_{\mathrm{vN}}(\hat\omega_0)\big|_{\mathrm{div}} = c \cdot \frac{A_{\mathrm{wedge\,boundary}}}{\epsilon^{d-1}}, \quad c = O(1).
$$

In the gravitational case, $\epsilon \to \ell_{\mathrm{Planck}}$ and $c \to 1/4$, giving the Bekenstein–Hawking area law $A/(4G_N)$. The match is **not** algebraically automatic — it requires identifying the UV regulator with the Planck length and adopting the gravitational normalization for $G_N$.

### 6.3 The coherent-state correction

For a coherent state $|\alpha\rangle = e^{i\phi(f)}|0_M\rangle$ with $f \in W_R$:
$$
S_{\mathrm{vN}}(\hat\rho_\alpha) - S_{\mathrm{vN}}(\hat\omega_0) = -S(\omega_\alpha\|\omega_0) + \mathcal{B}(\omega_\alpha, \omega_0).
$$
The Araki–Uhlmann relative entropy is computable from the symplectic form (Sem I Wk 7 §7):
$$
S(\omega_\alpha\|\omega_0) = \tfrac{1}{2}\sigma(f, \mathcal{F}f),
$$
and the boundary term is the difference of boost-Hamiltonian expectations between the coherent state and the vacuum.

Both pieces are **finite** (the divergent area term cancels in the difference). This is what makes the dressed entropy useful: differences are well-defined and computable even though absolute entropies have UV-divergent area terms.

## 7. Bulk extrema and the RT surface

A brief mention for connection to the broader holographic-entropy literature.

### 7.1 Choice of horizon

In the simplest case (e.g., the eternal AdS-Schwarzschild BH), the **horizon** of the bulk is unambiguous: the bifurcation surface where the Killing vector that generates ADM time vanishes.

For more general boundary subregions in a holographic CFT, the relevant horizon is the **Ryu–Takayanagi extremal surface** $\gamma_{\mathrm{RT}}$ — the minimal-area surface in the bulk anchored at the boundary subregion's boundary $\partial\mathcal{O}_{\mathrm{boundary}}$.

### 7.2 Quantum extremal surface

Including bulk quantum corrections, the **quantum extremal surface** (QES) extremizes the *generalized entropy*:
$$
S_{\mathrm{gen}}(\gamma) := \frac{A(\gamma)}{4G_N} + S_{\mathrm{out}}(\gamma).
$$
The QES prescription (Engelhardt–Wall 2014, refined by Penington 2019 / Almheiri–Engelhardt–Marolf–Maxfield 2019) is to extremize over choices of $\gamma$.

The Witten 2022 dressed-entropy formula reproduces $S_{\mathrm{gen}}$ at a *given* horizon. The choice of which horizon to use — the QES prescription — is a separate input.

### 7.3 Scope of Witten 2022

Witten 2022 derives the *formula* $S_{\mathrm{vN}} = S_{\mathrm{gen}}$ for a *fixed* boundary subregion with a clear modular flow. It does **not** address:

- How to choose the subregion (this is the QES question).
- Page-curve evolution and the island formula (Almheiri et al. 2019).
- Replica wormholes (Penington–Shenker–Stanford–Yang 2019).

These extensions take Witten 2022's structural formula and apply it to physically interesting scenarios. We will not pursue them in this course.

## 8. Discussion: what does it mean?

A few interpretive comments before Week 4's explicit computation.

### 8.1 The dressed entropy is the gravitational entropy

The dressed entropy on $\hat{\mathcal{A}}_R$ is not just an algebraic artifact — it is **the gravitational entropy of the corresponding bulk wedge**, equal to $A/(4G_N) + S_{\mathrm{out}}$ up to a state-independent constant.

This is the algebraic content of "the boundary CFT computes the bulk entropy" — sharpened from the heuristic Ryu–Takayanagi formula to a precise statement about the dressed-algebra structure.

### 8.2 What goes wrong at finite $N$

At finite $N$, the boundary algebra is type I (Week 1 §4.3). The dressed-algebra construction is trivial (Week 2 §3.3): no type promotion, just a tensor product with $L^\infty(\mathbb{R})$. The dressed entropy reduces to the original boundary vN entropy plus a clock contribution, **without** the area term.

The area law $A/(4G_N)$ specifically emerges in the **$N \to \infty$ limit** (classical gravity), where the modular flow becomes outer and the crossed product is non-trivial. This is consistent with the bulk picture: classical gravity has the BH entropy formula; quantum gravity (at finite $N$) has $1/N$ corrections.

### 8.3 The role of the modular Hamiltonian

The key identification $K_{\mathrm{TFD}} = \beta_H H_R$ (modular Hamiltonian = ADM Hamiltonian × $\beta_H$) is the holographic analog of Bisognano–Wichmann. It says the modular structure of the boundary subregion is geometrically/holographically determined by the bulk gravity.

This identification is what makes the boundary modular boundary term $\mathcal{B}$ map to the bulk area term $\delta(A/(4G_N))$. Without it, the Block D formula would still give a difference formula, but with no obvious gravitational interpretation.

## 9. What to take away

- **Dressed entropy** on the type II$_\infty$ algebra $\hat{\mathcal{A}}_R$: $S_{\mathrm{vN}}(\hat\rho) = -\hat\tau(\hat\rho_d\log\hat\rho_d)$, defined up to state-independent additive constant.
- **Block D dressed-entropy formula** (Sem I Wk 14 Theorem 3.1; algebraic, no holography needed):
$$
S_{\mathrm{vN}}(\hat\rho_\omega) - S_{\mathrm{vN}}(\hat\rho_\phi) = -S(\omega\|\phi) + \mathcal{B}(\omega, \phi).
$$
- **Modular Hamiltonian in TFD = $\beta_H H_R$** (Week 1 Theorem 5.1) makes the modular boundary term equal to $\beta_H \cdot \Delta$(ADM energy).
- **Witten's holographic identification (Witten 2022 §4):** in the holographic setting, the modular boundary term equals the classical area variation: $\mathcal{B}(\omega, \omega_{\mathrm{TFD}}) = \delta(A/(4G_N))$. Combined with the Faulkner–Lewkowycz–Maldacena identification of Araki–Uhlmann with bulk-entanglement difference, this gives:
$$
S_{\mathrm{vN}}(\hat\rho) = \frac{A_{\mathrm{horizon}}}{4G_N} + S_{\mathrm{out}}(\rho) + \mathrm{const}.
$$
- **The identification is holographic, not purely algebraic.** Algebraic part: Block D formula. Holographic part: modular = ADM, $\beta_H$ first law, FLM relative-entropy identification.
- **The Witten construction does not address** quantum extremal surfaces, Page-curve evolution, or replica wormholes — these are downstream developments.
- **Free-field Rindler analog** has every step computable; Week 4 makes it explicit.

## 10. Looking ahead

Week 4 is the **computational climax** of Block 1: the full Witten free-field Rindler analog. Concretely:

1. Construct $\hat{\mathcal{A}}(W_R)$ explicitly.
2. Write the trace as an integral kernel.
3. Compute $S_{\mathrm{vN}}$ for the dressed vacuum (area-law divergence).
4. Compute $S_{\mathrm{vN}}$ for a coherent state (finite difference).
5. Verify the Block D formula and identify each piece with the gravitational analog.

Every step uses only Sem I machinery (Bisognano–Wichmann, modular flow, Connes cocycle, dressed entropy). The students should be able to execute every step from the Sem I notes alone — this is the verification that Sem I has prepared them adequately for the Sem II literature.

## 11. Problem set

**Core problems.**

**1. Verify the Block D formula in finite dimensions.** For $\mathcal{M} = M_n(\mathbb{C})$ with two density matrices $\rho_\omega, \rho_\phi$, compute the LHS and RHS of
$$
S_{\mathrm{vN}}(\hat\rho_\omega) - S_{\mathrm{vN}}(\hat\rho_\phi) = -S(\omega\|\phi) + \mathcal{B}(\omega, \phi)
$$
explicitly and check the sign of the modular boundary term $\mathcal{B} = \omega(K_\phi) - \phi(K_\phi)$.

**2. Modular Hamiltonian for TFD = $\beta_H H_R$.** In finite dimensions, the TFD is $|\mathrm{TFD}\rangle = Z^{-1/2}\sum_n e^{-\beta_H E_n/2}|n\rangle_R\otimes|n\rangle_L$. Verify directly that the modular operator $\Delta = e^{-\beta_H(H_R - H_L)}$ (Sem I Wk 15 §1.2), so $K_{\mathrm{TFD}} = -\log\Delta = \beta_H(H_R - H_L) + \mathrm{const}$. On the right subalgebra alone (with $H_L$ acting as scalar), this reduces to $K_{\mathrm{TFD}}^{(R)} = \beta_H H_R + \mathrm{const}$.

**3. ADM-energy boundary term.** For a coherent excitation of the boundary CFT with $\langle H_R\rangle - \langle H_R\rangle_{\mathrm{TFD}} = \Delta E$, compute the modular boundary term $\mathcal{B}(\omega_{\mathrm{coh}}, \omega_{\mathrm{TFD}})$ and express in terms of $\Delta E$ and $\beta_H$.

**4. Read Witten 2022 §4.** Identify the precise step where Witten invokes the first law $\delta M = T_H\,\delta S$ on the gravitational side to identify the modular boundary term with the area variation.

**5. The state-independent constant.** Convince yourself that the additive constant in $S_{\mathrm{vN}}(\hat\rho) = A/(4G_N) + S_{\mathrm{out}} + \mathrm{const}$ is genuinely state-independent (depends only on the algebra and the trace normalization, not on $\rho$). What goes wrong if you try to determine it absolutely?

**Starred problems.**

**6\*. The FLM identification.** Read Faulkner–Lewkowycz–Maldacena, arXiv:1307.2892, §§1–2. Identify the precise statement that the boundary Araki–Uhlmann relative entropy equals the bulk relative entropy (in the appropriate dual region). This is the second holographic input to Witten 2022 §4.

**7\*. Bulk dressing and the JLMS formula.** Read Jafferis–Lewkowycz–Maldacena–Suh, arXiv:1512.06431. JLMS proved $S_{\mathrm{boundary}} = S_{\mathrm{bulk}} + \frac{1}{4G_N}\langle A_{\mathrm{RT}}\rangle$ at the level of relative entropy. Compare with the Witten 2022 dressed-entropy formula and identify the structural overlap.

**8\*. Quantum extremal surfaces.** Read Engelhardt–Wall, arXiv:1408.3203 §1. Identify the prescription: extremize $S_{\mathrm{gen}}(\gamma) = A(\gamma)/(4G_N) + S_{\mathrm{out}}(\gamma)$ over bulk surfaces $\gamma$. Where in the Witten 2022 framework does the *choice of extremization* enter?

**9\*. Finite $N$ corrections.** Heuristically, what's the leading $1/N$ correction to $S_{\mathrm{vN}}(\hat\rho) = A/(4G_N) + S_{\mathrm{out}} + \mathrm{const}$? Where would you expect the $1/N$ correction to enter — in the area term, the bulk-entropy term, or the additive constant?

**Project problems.**

**10. Read Liu §6.** Liu's lectures §6 (arXiv:2510.07017) summarize the Witten-2022 dressed-entropy story with extensive pedagogical commentary. Write a 5-page exposition reproducing the central derivation $S_{\mathrm{vN}} = S_{\mathrm{gen}}$, separating cleanly the algebraic and holographic inputs.

**11. Bridge to AAJ Block 4.** Ahmad–Jefferson Block 4 will compute the *second-order* correction to the dressed entropy from a Gao–Jafferis–Wall double-trace deformation. Sketch how the AAJ machinery builds on the Block 1 Wk 3 dressed-entropy formula plus the Sem I Wk 7 Connes cocycle.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 1. Last revised 2026-06-11.*
