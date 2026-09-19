---
title: "Sem II Week 5 — The TFD as a Type III$_1$ KMS State"
type: lecture-notes
course: syllabus
semester: 2
week: 5
block: 2
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Sem II Wks 1–4 (Witten 2022); Sem I Wks 10, 12, 15 (Bisognano–Wichmann, type III$_1$, TFD)
target_paper: "Chandrasekaran, Penington, Witten (CPW), arXiv:2209.10454 §2"
modified: 2026-06-11
---

# Sem II Week 5 — The TFD as a Type III$_1$ KMS State

> *Block 1 developed Witten 2022 in its single-sided form: take the boundary algebra $\mathcal{A}_R$ of a holographic CFT, dress by the ADM flow, and the dressed entropy reproduces the bulk generalized entropy. Block 2 extends this to the **two-sided eternal black hole**: the bulk is the maximally extended AdS-Schwarzschild geometry with two asymptotic regions, and the dual boundary state is the **thermofield double** (TFD) of the two boundary CFTs. This week we develop the two-sided structure: TFD as the cyclic-separating vector for both algebras $\mathcal{A}_R, \mathcal{A}_L$; modular Hamiltonian on $\mathcal{A}_R$ given by $\beta_H(H_R - H_L)$ (not just $\beta_H H_R$); KMS at the Hawking temperature. The free-field Rindler-Rindler analog runs in parallel throughout. Weeks 6–7 use this structure to build the CPW dressed algebra and identify the dressed entropy with $S_{\mathrm{gen}}$.*

## 0. Reading

**Primary:**
- Chandrasekaran, Penington, Witten (CPW), "Large $N$ algebras and generalized entropy," arXiv:2209.10454, **§§2–3** (the two-sided eternal BH and the boundary single-trace algebras).
- Sem I Wk 15 (TFD bridge to Sem II).

**Secondary:**
- Maldacena, "Eternal black holes in anti-de Sitter," arXiv:hep-th/0106112 — the foundational TFD/eternal-BH identification.
- Liu, arXiv:2510.07017, **§§7–8** (algebraic ER=EPR, two-sided structures).

**Optional research reading:**
- Leutheusser & Liu, arXiv:2110.05497 (causal connectability between the two sides).
- Israel, "Thermo-field dynamics of black holes," *Phys. Lett. A* 57 (1976) 107 (the original TFD construction in black-hole physics).
- Maldacena & Susskind, "Cool horizons for entangled black holes," arXiv:1306.0533 (ER=EPR).

## 1. The two-sided eternal black hole

### 1.1 The geometry

The **maximally extended AdS-Schwarzschild black hole** in $(d+1)$ dimensions has the metric
$$
ds^2 = -f(r)\,dt^2 + \frac{dr^2}{f(r)} + r^2\,d\Omega_{d-1}^2, \qquad f(r) = 1 - \frac{r_h^{d-2}}{r^{d-2}} + \frac{r^2}{\ell^2},
$$
extended through the horizon at $r = r_h$ to its full Penrose diagram. The diagram has four regions:

- **Right exterior** (region I): an asymptotically AdS region with a CFT$_d$ on its boundary at $r \to \infty$.
- **Left exterior** (region III): a mirror copy of the right exterior, with a second CFT$_d$ on its boundary.
- **Future interior** (region II): the part of the geometry behind the horizon, inside the future light cone of the bifurcation surface.
- **Past interior** (region IV): the mirror of region II.

The two exteriors are **causally disconnected** — no timelike curve connects them — but they are **bulk-geometrically connected** through the Einstein–Rosen bridge.

### 1.2 The bifurcation surface

At the center of the Penrose diagram, the Killing vector $\partial_t$ vanishes. This codimension-2 locus is the **bifurcation surface** $\Sigma$, topologically $S^{d-1}$ (the angular sphere at $r = r_h, t = 0$).

The bifurcation surface plays two roles:

- It is the **horizon** of the black hole: the boundary between regions I and II (and between III and IV).
- It is the **edge of the entanglement wedge** of either boundary: the surface anchoring the Ryu–Takayanagi formula.

### 1.3 The Hawking temperature

The surface gravity at the horizon gives the **Hawking temperature**:
$$
T_H = \frac{f'(r_h)}{4\pi} = \frac{1}{4\pi}\cdot\frac{(d-2)r_h + d r_h^3/\ell^2}{r_h}.
$$
In units where $\ell = 1$, for a "large" black hole ($r_h \gg 1$), $T_H \sim r_h/(2\pi)$.

The **inverse Hawking temperature** $\beta_H = 1/T_H$ enters as the periodicity of imaginary time in the Euclidean continuation of the geometry. It is the universal scale in the two-sided story.

### 1.4 Maldacena's duality

**Theorem 1.1 (Maldacena 2001). [Stated only — refs: hep-th/0106112.]** *The two-sided eternal AdS-Schwarzschild BH is holographically dual to the boundary CFT$_d \otimes$ CFT$_d$ in the thermofield double state*
$$
|\mathrm{TFD}_{\beta_H}\rangle = \frac{1}{\sqrt{Z(\beta_H)}}\sum_n e^{-\beta_H E_n/2}\,|n\rangle_R \otimes |n\rangle_L,
$$
*where $|n\rangle_R, |n\rangle_L$ are energy eigenstates of the right and left CFTs (with the same Hamiltonian spectrum).*

This is the **foundational identification** of the entire Sem II program. The two-sided geometry has a single state-level dual: the boundary CFTs in the TFD.

## 2. The two boundary algebras

### 2.1 Setup

At large $N$, each boundary supports a CFT$_d$ with single-trace algebra. We denote:

- $\mathcal{A}_R$: the algebra of single-trace operators on the right boundary at a fixed time slice.
- $\mathcal{A}_L$: same on the left boundary.

These are the **two-sided boundary single-trace algebras**. At $N = \infty$ (classical-gravity limit), each is type III$_1$ on the appropriate Hilbert space (Week 1 Theorem 4.1).

### 2.2 Causal complementarity

The right and left boundaries are causally disconnected (§1.1). At the operator-algebra level, this means:
$$
[\mathcal{A}_R, \mathcal{A}_L] = 0.
$$
Any right-boundary operator commutes with any left-boundary operator. This is the algebraic content of "the two CFTs are non-interacting."

In holographic terms: causal complementarity on the boundary corresponds to **bulk causal separation** between the two asymptotic regions through the wormhole.

### 2.3 Combined algebra

The joint algebra is the von Neumann tensor product or, more precisely, the algebra generated by both:
$$
\mathcal{A}_R \vee \mathcal{A}_L := (\mathcal{A}_R \cup \mathcal{A}_L)'',
$$
acting on the doubled Hilbert space $\mathcal{H}_R \otimes \mathcal{H}_L$. Under causal complementarity, this is essentially $\mathcal{A}_R \otimes \mathcal{A}_L$ as von Neumann algebras.

The TFD vacuum lives on this doubled Hilbert space and is the canonical state for the two-sided story.

## 3. The TFD as cyclic-separating

### 3.1 Statement

**Theorem 3.1 (TFD cyclic-separating for $\mathcal{A}_R$). [Stated only — refs: CPW §2; Sem I Wk 15 §1.2 for the finite-dim version.]** *The TFD vector $|\mathrm{TFD}_{\beta_H}\rangle \in \mathcal{H}_R \otimes \mathcal{H}_L$ is cyclic and separating for $\mathcal{A}_R \otimes 1 \subset \mathcal{B}(\mathcal{H}_R \otimes \mathcal{H}_L)$ at large $N$, under the type-III$_1$ hypothesis on $\mathcal{A}_R$.*

By symmetry, the same is true for $1 \otimes \mathcal{A}_L$ — and indeed for either as a subalgebra of the joint $\mathcal{A}_R \vee \mathcal{A}_L$.

### 3.2 The Tomita–Takesaki data

By Sem I Wk 5 (Tomita–Takesaki theorem) and cyclic-separating from Theorem 3.1, we obtain:

- A **modular operator** $\Delta_{\mathrm{TFD}}$ on $\mathcal{H}_R \otimes \mathcal{H}_L$, positive self-adjoint.
- A **modular conjugation** $J_{\mathrm{TFD}}$, antiunitary.
- A **modular flow** $\sigma_t^{\mathrm{TFD}}(a) := \Delta_{\mathrm{TFD}}^{-it}\,a\,\Delta_{\mathrm{TFD}}^{it}$ on $\mathcal{A}_R$.

The TFD vector is **KMS at $\beta = +1$** for $\sigma^{\mathrm{TFD}}$, in our upper-strip convention (Sem I Wk 6).

### 3.3 Modular Hamiltonian = $\beta_H(H_R - H_L)$

In finite dimensions (Sem I Wk 15 §1.2), the modular operator of the TFD is
$$
\Delta_{\mathrm{TFD}} = \rho_R \otimes \rho_R^{-1} = e^{-\beta_H(H_R - H_L)}\cdot\frac{1}{Z(\beta_H)^2},
$$
and the modular Hamiltonian is
$$
K_{\mathrm{TFD}} = -\log\Delta_{\mathrm{TFD}} = \beta_H(H_R - H_L) + 2\log Z(\beta_H).
$$

In the large-$N$ holographic setting, the same identification holds (CPW §2, hypothesis-explicit):
$$
\boxed{K_{\mathrm{TFD}} = \beta_H\,(H_R - H_L) + \text{(additive scalar)}.}
$$

**The crucial structural feature.** In Block 1 we worked with the single-sided modular Hamiltonian $\beta_H H_R$ — appropriate for the single-sided story. The two-sided version is $\beta_H(H_R - H_L)$. The presence of $-H_L$ is **not** a typo: it is the algebraic content of the bulk **boost** at the bifurcation surface.

> **Physical picture: only the difference exists.** In the genuinely type III setting, the split $K_{\mathrm{TFD}} = \beta_H H_R - \beta_H H_L$ is *formal*: the one-sided generators do not exist as self-adjoint operators on the doubled Hilbert space. The would-be $H_R$ alone is the integral of the stress tensor against a profile that ends sharply at the entangling surface, and its fluctuations in the TFD diverge — the same UV pile-up of straddling modes that drives the area law and the type III structure. Only the *combination* $H_R - H_L$, whose profile passes smoothly (antisymmetrically) through the bifurcation surface, is a well-defined generator: the divergences of the two halves cancel against each other. This is the operator-level face of three familiar facts: the one-sided modular Hamiltonian of a QFT region is not an operator but a sesquilinear form; "the energy of the right wedge" is cutoff-dependent while boost energy is not; and the crossed-product clock of Week 6 will be needed precisely because no one-sided generator is available to be conditioned on. The finite-dimensional TFD formulas, where $H_R$ and $H_L$ separately exist, should be read as a regulated model of this situation — trustworthy for the difference, misleading for the parts.

### 3.4 The two-sided boost interpretation

In the bulk, the Killing vector $\partial_t$ that generates time translation on the right boundary also generates *backward* time translation on the left boundary (by the time-reversal symmetry of the maximally extended geometry). This is the **two-sided boost**: $H_R$ on the right minus $H_L$ on the left.

In the free-field Rindler analog (Sem I Wk 15 §2), the analog is the **Lorentz boost** in the $(x^0, x^1)$-plane: it generates positive time translation in $W_R$ and negative time translation in $W_L$, with the bifurcation surface $\{x^0 = x^1 = 0\}$ fixed.

This identification — bulk boost = $H_R - H_L$ = $\beta_H^{-1}$ × modular Hamiltonian — is the **holographic Bisognano–Wichmann theorem**. It generalizes the free-field Bisognano–Wichmann to large-$N$ holographic settings.

## 4. KMS at the Hawking temperature

### 4.1 The KMS condition

The modular flow $\sigma^{\mathrm{TFD}}_t = \mathrm{Ad}(\Delta_{\mathrm{TFD}}^{-it}) = \mathrm{Ad}(e^{i\beta_H t(H_R - H_L)})$ acts on $a \in \mathcal{A}_R$ as **time evolution by $\beta_H t$ on the right**, with the left-side rotation acting trivially because $a \in \mathcal{A}_R$ commutes with $H_L$.

So for $a \in \mathcal{A}_R$:
$$
\sigma^{\mathrm{TFD}}_t(a) = e^{i\beta_H t\,H_R}\,a\,e^{-i\beta_H t\,H_R} = \alpha^{H_R}_{\beta_H t}(a).
$$

Identifying $u = \beta_H t$, the modular flow $\sigma^{\mathrm{TFD}}$ on $\mathcal{A}_R$ is the **ADM time translation** with rapidity $u$. The modular time $t$ is the dimensionless time, related to ADM time by $u = \beta_H t$.

### 4.2 KMS at $\beta_H$

The TFD is KMS at modular $\beta = 1$ for $\sigma^{\mathrm{TFD}}$ (Sem I Wk 6 Theorem 2.1). Translating to ADM time $u = \beta_H t$, this is KMS at inverse temperature $\beta_H$ for the ADM time flow:
$$
\omega_{\mathrm{TFD}}(a\,\alpha^{H_R}_u(b)) \text{ extends to } 0 \le \mathrm{Im}\,u \le \beta_H, \text{ with } \omega_{\mathrm{TFD}}(a\,\alpha^{H_R}_{u+i\beta_H}(b)) = \omega_{\mathrm{TFD}}(\alpha^{H_R}_u(b)\,a).
$$

**The TFD vacuum is KMS at the Hawking temperature for ADM time translation on the right boundary.** This is the holographic Unruh effect.

### 4.3 Comparison with single-sided story

In Block 1, the modular Hamiltonian on $\mathcal{A}_R$ was $\beta_H H_R$. Here it is $\beta_H(H_R - H_L)$. **Both are correct**, in the appropriate setting:

- **Single-sided story (Block 1):** view $\mathcal{A}_R$ as living on $\mathcal{H}_R$ alone. The TFD restricted to $\mathcal{A}_R$ gives the thermal density matrix $\rho_R = e^{-\beta_H H_R}/Z$. The modular Hamiltonian (for the GNS Hilbert space of $\omega_R$) is $\beta_H H_R$ (one-sided).
- **Two-sided story (Block 2):** view $\mathcal{A}_R$ as a subalgebra of $\mathcal{B}(\mathcal{H}_R \otimes \mathcal{H}_L)$. The TFD on the doubled space has modular Hamiltonian $\beta_H(H_R - H_L)$ (two-sided).

The relation: the two are *equivalent* on $\mathcal{A}_R$ in the appropriate GNS representations, because $H_L$ acts as zero on operators in $\mathcal{A}_R \otimes 1$, so $\beta_H(H_R - H_L)$ and $\beta_H H_R$ generate the same automorphism of $\mathcal{A}_R$.

The full modular Hamiltonian $\beta_H(H_R - H_L)$ acts on the full doubled Hilbert space $\mathcal{H}_R \otimes \mathcal{H}_L$ — that's where the two-sided structure becomes essential.

## 5. Modular conjugation: ER=EPR

### 5.1 The modular conjugation $J_{\mathrm{TFD}}$

By Sem I Wk 5, the Tomita–Takesaki theorem gives an antiunitary modular conjugation $J_{\mathrm{TFD}}$ on $\mathcal{H}_R \otimes \mathcal{H}_L$.

**Theorem 5.1 ($J_{\mathrm{TFD}}$ swaps the two sides). [Stated only — refs: Sem I Wk 15 §1.2; CPW §2.]** *The modular conjugation $J_{\mathrm{TFD}}$ maps $\mathcal{A}_R \otimes 1$ onto $1 \otimes \mathcal{A}_L$ (and vice versa):*
$$
J_{\mathrm{TFD}}\,(\mathcal{A}_R \otimes 1)\,J_{\mathrm{TFD}}^* = 1 \otimes \mathcal{A}_L = (\mathcal{A}_R)'.
$$

So Haag duality holds for the two boundary algebras: each is the commutant of the other in $\mathcal{B}(\mathcal{H}_R \otimes \mathcal{H}_L)$.

### 5.2 Algebraic ER=EPR

The structural picture:

- $\mathcal{A}_R, \mathcal{A}_L$ are causally disconnected (cannot communicate).
- $|\mathrm{TFD}\rangle$ is cyclic-separating for both.
- $J_{\mathrm{TFD}}$ realizes a canonical isomorphism between them.

This is the **algebraic content of ER=EPR**: two boundary algebras are connected by a bulk Einstein-Rosen bridge **if and only if** there is a cyclic-separating vector on the joint algebra with a modular conjugation swapping them. The bulk geometric connection is encoded in the algebraic Tomita–Takesaki structure.

**Maldacena–Susskind's heuristic (ER=EPR):** "An Einstein-Rosen bridge is dual to maximally entangled EPR-like states." The algebraic version: ER bridges ↔ cyclic-separating two-sided states with $J\mathcal{A}_R J = \mathcal{A}_L$. The TFD is the canonical example.

### 5.3 What ER=EPR is not

This is **not** the claim that *any* entanglement generates a bulk wormhole geometry — that's a much stronger conjecture about bulk reconstruction from boundary entanglement. The algebraic statement is more modest: in the eternal BH setting, the TFD's modular structure encodes the bridge, and conversely the bridge is "what the TFD sees."

The Sem II Block 3 (Liu lectures) discusses the algebraic ER=EPR proposal in more detail.

## 6. Worked example: free-field Rindler-Rindler

The two-sided analog of the Sem I Wk 15 §2 free-field Rindler model. Same machinery, two sides.

### 6.1 Setup

Take the 4D massless free scalar field on Minkowski space. The two-sided wedge algebra is
$$
\mathcal{A}(W_R) \vee \mathcal{A}(W_L) \subset \mathcal{B}(\mathcal{F})
$$
acting on the Fock space $\mathcal{F}$. The Minkowski vacuum $|0_M\rangle$ is the cyclic-separating vector (Sem I Wk 9).

### 6.2 Minkowski vacuum is the TFD

**Theorem 6.1 (Two-sided Bisognano–Wichmann; Sem I Wk 15 §2). [Stated only — verified in Sem I Wk 15 §6 by Bogoliubov.]** *The Minkowski vacuum, restricted to $\mathcal{A}(W_R) \vee \mathcal{A}(W_L)$, is the TFD of the boost Hamiltonian at Unruh temperature $\beta = 2\pi$:*
$$
|0_M\rangle = \prod_\omega \frac{1}{\sqrt{Z_\omega}}\sum_{n_\omega} e^{-\pi n_\omega \omega}\,|n_\omega\rangle_R \otimes |n_\omega\rangle_L.
$$
*The modular Hamiltonian on $\mathcal{A}(W_R)$ is*
$$
K_{0_M} = 2\pi(K_R - K_L),
$$
*where $K_R, K_L$ are the boost generators on the right and left wedges. The modular flow is the (two-sided) Lorentz boost.*

### 6.3 KMS at $\beta = 2\pi$

The Minkowski vacuum is KMS at modular $\beta = 1$ for $\sigma^{0_M}_t = \mathrm{Ad}(e^{2\pi i t(K_R - K_L)})$, which after rescaling $s = 2\pi t$ is KMS at $\beta = 2\pi$ for the boost flow with rapidity $s$.

This is the **two-sided** Bisognano–Wichmann + Unruh effect. Each side individually looks thermal at $\beta = 2\pi$; the joint structure is the TFD at $\beta = 2\pi$ of the boost generator.

### 6.4 Modular conjugation: PCT

By Bisognano–Wichmann (Sem I Wk 10 §6), the modular conjugation is **PCT**:
$$
J_{0_M} = \Theta \cdot R_\perp(\pi),
$$
where $\Theta$ is the antiunitary CPT operator and $R_\perp(\pi)$ is a $\pi$-rotation in the perpendicular directions $(x^2, x^3)$ (for $d = 4$). This swaps $W_R$ with $W_L$ and gives Haag duality.

In 2D ($d = 1$), $J_{0_M} = \Theta$ (no perpendicular rotation needed), and $\Theta$ acts as $(x^0, x^1) \to (-x^0, -x^1)$, swapping $W_R \leftrightarrow W_L$.

### 6.5 The free-field analog mirror

The dictionary between the gravitational and free-field analog settings:

| CPW (gravitational) | Free-field Rindler-Rindler |
|---|---|
| Right CFT boundary | Right Rindler wedge $W_R$ |
| Left CFT boundary | Left Rindler wedge $W_L$ |
| Bifurcation surface (BH horizon) | Bifurcation surface $\{x^0 = x^1 = 0\}$ |
| TFD at $\beta_H$ | Minkowski vacuum $\lvert 0_M\rangle$ = TFD at $\beta = 2\pi$ |
| $H_R - H_L$ (two-sided ADM) | $K_R - K_L$ (two-sided boost) |
| Modular Hamiltonian $\beta_H(H_R - H_L)$ | Modular Hamiltonian $2\pi(K_R - K_L)$ |
| Modular flow = ADM time difference | Modular flow = Lorentz boost |
| Algebraic ER=EPR | Lorentz-boost Haag duality |

Every entry on the right is **explicitly computable** in the free-field theory. The gravitational case is structurally identical with the ADM Hamiltonian replacing the boost generator.

## 7. Why $-H_L$? An invariance argument

A pedagogically helpful aside: why does the **difference** $H_R - H_L$ appear in the modular Hamiltonian, rather than just $H_R$ on the right?

### 7.1 TFD invariance

The TFD is invariant under the combined right + left time translation that subtracts:
$$
\big[\,H_R - H_L,\,|\mathrm{TFD}\rangle\,\big] = 0.
$$
**Proof.** $H_R$ acts as $\sum_n E_n |n\rangle_R\langle n|_R$, similarly $H_L$. On the TFD,
$$
H_R|\mathrm{TFD}\rangle = \sum_n \frac{E_n e^{-\beta_H E_n/2}}{\sqrt{Z}}\,|n\rangle_R\otimes|n\rangle_L = H_L|\mathrm{TFD}\rangle,
$$
since the sum is symmetric in the index $n$ and $H_L$ acts on the left with the same eigenvalue. Hence $(H_R - H_L)|\mathrm{TFD}\rangle = 0$. $\square$

So $H_R - H_L$ annihilates the TFD, while $H_R + H_L$ does not. The difference is the **boost-like** generator that fixes the TFD (and the bifurcation surface in the bulk picture).

### 7.2 Modular Hamiltonian fixes the modular state

By Tomita–Takesaki, the modular Hamiltonian $K_\Omega$ annihilates the modular vector $\Omega$ (up to scalar). So whatever the modular Hamiltonian of the TFD is, it must annihilate the TFD. The natural candidate is $\beta_H(H_R - H_L)$, consistent with the explicit finite-dim calculation in §3.3.

This is a *consistency check* on the identification $K_{\mathrm{TFD}} = \beta_H(H_R - H_L)$, not a derivation — but it's a useful sanity check.

### 7.3 Bulk interpretation

In the bulk, the Killing vector field $\xi = \partial_t$ that generates ADM time on the right boundary continues across the horizon (with sign flip) to generate ADM time *backwards* on the left boundary. This is the **boost Killing vector** of the maximally extended geometry, which fixes the bifurcation surface.

On the boundary CFT, this Killing vector projects to $H_R$ on the right and $-H_L$ on the left, i.e., the bulk Killing vector is dual to $H_R - H_L$. This is the **boost-symmetry** of the eternal BH.

So the modular Hamiltonian $\beta_H(H_R - H_L)$ has a clean bulk interpretation: it is $\beta_H$ times the boundary projection of the bulk Killing vector at the bifurcation surface. This is the holographic Bisognano–Wichmann theorem.

## 8. Discussion: two-sided modular structure

### 8.1 What the TFD knows

The TFD vacuum, viewed as a state on $\mathcal{A}_R \vee \mathcal{A}_L$, knows:

1. The **right CFT's reduced state**: a thermal Gibbs state at $\beta_H$ (the bulk Hawking effect from the perspective of an observer outside the BH).
2. The **modular Hamiltonian** $\beta_H(H_R - H_L)$, which equals the bulk Killing flow at the bifurcation surface.
3. The **Haag duality** $J\mathcal{A}_R J = \mathcal{A}_L$, which encodes the wormhole connection.

Each piece corresponds to a structural feature of the bulk: Hawking thermality, boost invariance, ER bridge.

### 8.2 What's the same as Block 1

The Block 2 setup is the two-sided extension of Block 1:

| Block 1 (single-sided) | Block 2 (two-sided) |
|---|---|
| Algebra $\mathcal{A}_R$ alone | Joint $\mathcal{A}_R \vee \mathcal{A}_L$ |
| Cyclic-separating: one-sided thermal state | TFD vacuum |
| Modular Hamiltonian: $\beta_H H_R$ | $\beta_H(H_R - H_L)$ |
| Modular flow on $\mathcal{A}_R$: ADM time on right | Same (when restricted to $\mathcal{A}_R$) |
| Type III$_1$: yes | Yes (each side) |
| KMS at $\beta_H$: yes | Yes (each side) |

For the **single-side restriction to $\mathcal{A}_R$ alone**, the two stories are *equivalent* — the modular flow on $\mathcal{A}_R$ generated by $\beta_H(H_R - H_L)$ equals the one generated by $\beta_H H_R$ (since $H_L$ commutes with $\mathcal{A}_R$).

The new structural content in Block 2 is the **joint** structure: how the two sides relate to each other under modular conjugation, what the joint algebra is, and how dressing works on it.

### 8.3 What's new in Block 2

Beyond Block 1, Block 2 will address:

1. **The CPW dressing** (Week 6): both algebras dressed in a way that respects the two-sided structure.
2. **Joint dressed entropy** (Week 7): the dressed entropy formula now for a two-sided state, and how it relates to the bulk generalized entropy of the eternal-BH geometry.
3. **Bell–CHSH between two sides** (Week 8): the algebraic content of "the TFD is maximally entangled across the bifurcation horizon."

These are the new things the two-sided structure unlocks.

## 9. What to take away

- **Two-sided eternal BH (Maldacena 2001):** dual to the boundary CFTs in the TFD state at the Hawking temperature.
- **TFD as cyclic-separating** (stated only, hypothesis-explicit): for both $\mathcal{A}_R$ and $\mathcal{A}_L$ at large $N$, under the type-III$_1$ hypothesis. Licenses Tomita–Takesaki on the joint algebra.
- **Modular Hamiltonian = $\beta_H(H_R - H_L)$:** the two-sided modular Hamiltonian, projecting to $\beta_H H_R$ when restricted to $\mathcal{A}_R$ alone.
- **KMS at $\beta_H$** for ADM time translation on either side. Holographic Unruh effect.
- **Modular conjugation = PCT/boost-reflection** in the free-field analog; algebraic ER=EPR in the gravitational case.
- **Free-field Rindler-Rindler analog**: explicit verification of every structural feature (Sem I Wk 15 §6 gave the Bogoliubov derivation).
- **Why $-H_L$:** the TFD is annihilated by $H_R - H_L$, not by $H_R$ alone. This is the algebraic content of "the TFD is boost-invariant."

## 10. Looking ahead

Week 6 builds the **CPW dressed algebra**: form the crossed product by the ADM Hamiltonian and verify type II$_\infty$ promotion. The construction is structurally identical to Block 1 Week 2 (Witten 2022 single-sided), with the key subtlety of which Hamiltonian to dress by — single-sided $H_R$, or two-sided $H_R - H_L$? Week 7 then computes the dressed entropy and verifies the area law in the free-field two-sided Rindler analog. Week 8 closes the block with Bell–CHSH between the two sides.

## 11. Problem set

**Core problems.**

**1. TFD reduced state.** Verify directly that $\mathrm{Tr}_L(|\mathrm{TFD}_{\beta_H}\rangle\langle\mathrm{TFD}_{\beta_H}|) = e^{-\beta_H H_R}/Z(\beta_H)$ in finite dimensions. Conclude that the right CFT's reduced state is the Gibbs state at $\beta_H$.

**2. Modular operator of the TFD.** In finite dimensions, verify $\Delta_{\mathrm{TFD}} = (e^{-\beta_H H_R}/Z) \otimes (e^{-\beta_H H_L}/Z)^{-1}$. Compute $K_{\mathrm{TFD}} = -\log\Delta_{\mathrm{TFD}}$ and show it equals $\beta_H(H_R - H_L) + 2\log Z(\beta_H)$.

**3. The TFD is annihilated by $H_R - H_L$.** Verify $(H_R - H_L)|\mathrm{TFD}_{\beta_H}\rangle = 0$ from the explicit form. Why does this not hold for $H_R + H_L$?

**4. Two-sided modular flow.** Show that for $a \in \mathcal{A}_R \otimes 1$, the modular flow $\sigma^{\mathrm{TFD}}_t(a) = e^{i\beta_H t(H_R - H_L)}\,a\,e^{-i\beta_H t(H_R - H_L)}$ reduces to $e^{i\beta_H t H_R}\,a\,e^{-i\beta_H t H_R}$ (one-sided ADM time on the right). Where does $H_L$ go?

**5. Modular conjugation in 2D massless free scalar.** Verify directly that for the 2D massless free scalar restricted to two-sided Rindler ($W_R \cup W_L$), the modular conjugation is the antiunitary CPT operator $\Theta$, and that $\Theta\mathcal{A}(W_R)\Theta = \mathcal{A}(W_L)$.

**Starred problems.**

**6\*. KMS at $\beta_H$.** Take a (formal) thermal correlator $\langle\mathcal{O}(x)\mathcal{O}(y)\rangle_{\mathrm{TFD}}$ in a 2D CFT on the eternal BTZ boundary. Show that this correlator is periodic in imaginary boundary time with period $\beta_H = 2\pi r_h/\ell^2$. (*Hint:* use the conformal mapping from the plane to the cylinder.)

**7\*. Read CPW §2.** Identify the precise hypotheses CPW use for the two-sided large-$N$ structure. Compare with our Theorem 3.1.

**8\*. Read Maldacena 2001 §§1–3.** Identify the precise argument for the eternal BH ↔ TFD duality. Where does the holographic dictionary enter, and where is it taken as input?

**9\*. Boundary Killing vector.** Sketch a derivation of the identification $K_{\mathrm{TFD}}^{(R)} = \beta_H H_R$ from the bulk Killing vector $\partial_t$ in the maximally extended AdS-Schwarzschild geometry. (*Hint:* the boundary projection of $\partial_t$ generates ADM time on the right boundary; $\beta_H$ comes from the surface gravity.)

**Project problems.**

**10. Connection to Liu §§7–8.** Liu (arXiv:2510.07017) §§7–8 discuss the algebraic ER=EPR proposal. Write a 5-page exposition comparing CPW's two-sided modular structure (this week) with Liu's algebraic ER=EPR criterion.

**11. Higher-genus generalization.** Sketch what changes in the two-sided story if we replace the eternal AdS-Schwarzschild by an eternal AdS black hole at higher genus (e.g., a torus boundary). What's the analog of the TFD? How does the modular Hamiltonian change?

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 2. Last revised 2026-06-11.*
