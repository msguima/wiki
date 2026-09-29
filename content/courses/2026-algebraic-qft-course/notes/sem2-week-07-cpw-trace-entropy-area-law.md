---
title: "Sem II Week 7 — CPW Trace Entropy and Generalized Entropy"
type: lecture-notes
course: syllabus
semester: 2
week: 7
block: 2
duration: "master dossier: 4 hours of material; classroom core: 2-hour seminar + 1-hour office/self-study"
prerequisites: Sem II Wks 5–6; Sem I Wks 13–14
target_paper: "Chandrasekaran, Penington, Witten, arXiv:2209.10454 §§2.2–3"
modified: 2026-08-24
---

# Sem II Week 7 — CPW Trace Entropy and Generalized Entropy

> *The type II$_\infty$ trace makes entropy possible, but CPW's main result is not merely that the entropy exists. They construct a controlled class of semiclassical states, compute the corresponding density in the right algebra, and show that its trace entropy agrees with the generalized entropy of the black-hole bifurcation surface up to a state-independent constant. The energy-distribution entropy, the bulk relative entropy, and the horizon-area response enter separately. This separation is the calculation.*

## 0. Reading

**Primary:**

- CPW, “Large $N$ algebras and generalized entropy,” arXiv:2209.10454, §§2.2–3.
- Sem II Week 6 for $\mathcal N_L=\mathcal N_R'$.

**Background:**

- Witten, arXiv:2112.12828, §§3.4–3.5.
- Wall, arXiv:1105.3445, for horizon generalized entropy and relative entropy.
- Bombelli et al. and Srednicki for the separate regulated matter area law.

### 0.1 How to use this master dossier

- **Classroom core:** §§1–4.2 and Problems 1–5. This route derives the three-term CPW entropy formula and shows exactly where the horizon equation enters.
- **Full derivation / self-study:** §§4.3–8 and Problems 6–10. This route reconstructs the density, checks inner-unitary cancellation, audits right/left counting, and keeps the ADM wavepacket scale separate from the matter UV cutoff.
- **Research extension:** Problems 11–12, using §§3–4 and 8 as the source-comparison spine. This route turns the chapter into a source-scope map suitable for a written exposition of CPW and its relation to Witten.

The guiding discipline is to keep three ledgers side by side: operator algebra, semiclassical gravity, and state preparation. The final equality is persuasive only when no term silently moves from one ledger to another.

## 1. Algebraic setup

Let $\mathcal A_{R,0}$ be the type III$_1$ algebra of right-exterior fluctuations about the reference eternal black hole, and let $\Psi$ be the equilibrium TFD standard vector. CPW's microcanonical scaling includes a renormalized right ADM energy $h_R$ with $O(1)$ fluctuations. The enlarged algebra

$$
\mathcal A_R
\cong
\mathcal A_{R,0}\rtimes_{\sigma^\Psi}\mathbb R
$$

is a type II$_\infty$ factor. The left algebra is its commutant,

$$
\mathcal A_L=\mathcal A_R'.
$$

There is no joint tensor-factor entropy of “right plus left” in this construction. We compute the entropy of a state restricted to the right type II factor; the left factor organizes its commutant.

The right trace is faithful, normal, semifinite, and unique up to scale. CPW's convention has a shift of the energy coordinate rescale the trace. In the course convention this is the familiar law

$$
\widehat\tau\circ\theta_r=e^{-r}\widehat\tau.
$$

### 1.1 CPW notation versus the course notation

CPW use

$$
x=h_L,
\qquad
p_{\rm CPW}=-i\partial_x,
\qquad
h_\Psi=-\log\Delta,
\qquad
\beta_Hh_R=\beta_Hx+h_\Psi.
$$

Their $x$ is the left-energy multiplication coordinate and their $p_{\rm CPW}$ is the relative timeshift. The course's regular coordinate is $q$, with $Q$ multiplying by $q$ and $P=-i\partial_q$; after Fourier transform, the spectral variable of $P$ is called $p$. The exact Fourier/sign map derived in Week 6 is

$$
\boxed{p=-\beta_Hx,\qquad Q=\frac{p_{\rm CPW}}{\beta_H}.}
$$

Consequently, for $\beta_H>0$, the pushforward of the positive measure is

$$
e^{\beta_Hx}\,|dx|
=\frac1{\beta_H}e^{-p}\,dp,
$$

where $p$ is integrated with increasing orientation. The factor $1/\beta_H$ is absorbed into the trace normalization. This is why CPW's $e^{\beta_Hx}$ trace and the course's $e^{-p}$ trace have the same scaling law. It is also why calling CPW's $p_{\rm CPW}$ an energy would reverse the physical roles of the canonical pair.

## 2. CPW's class of semiclassical states

### 2.1 Energy wavepacket

CPW consider states of the form

$$
|\widehat\Phi\rangle
{}={}
\int_{-\infty}^{\infty}dx\,
\varepsilon^{1/2}g(\varepsilon x)
|\Phi\rangle\otimes|x\rangle,
$$

where $\Phi$ is a state of the bulk QFT fluctuations, $g\in L^2(\mathbb R)$ is normalized, and $\varepsilon\ll1$. To keep the course symbol $p$ reserved for the Fourier spectral variable, denote the probability density of the energy collective coordinate by

$$
\mu_\varepsilon(x)=\varepsilon|g(\varepsilon x)|^2.
$$

Its width is $O(1/\varepsilon)$. The state is assumed to vary slowly enough across the relevant $O(1)$ energy range that the $O(\varepsilon)$ expansion is controlled.

### 2.2 Why this is not a clock cutoff

The parameter $\varepsilon$ controls the spread of the ADM-energy wavepacket. It is not the short-distance cutoff of the matter field. In particular,

$$
H(\mu_\varepsilon)
{}={}
-\int \mu_\varepsilon(x)\log \mu_\varepsilon(x)dx
{}={}
H(|g|^2)-\log\varepsilon.
$$

This is the differential entropy of a collective coordinate. The matter UV divergence is instead encoded in the renormalized combination of horizon area and bulk entropy.

## 3. The CPW entropy formula

### 3.1 Relative modular notation

Let $\Delta_{\Psi|\Phi}$ be the relative modular operator for the reference state $\Psi$ and the excited state $\Phi$ on $\mathcal A_{R,0}$. Define

$$
h_{\Psi|\Phi}:=-\log\Delta_{\Psi|\Phi}.
$$

With CPW's ordering convention,

$$
S_{\rm rel}(\Phi\Vert\Psi)
{}={}
\langle\Phi|h_{\Psi|\Phi}|\Phi\rangle.
$$

### 3.2 The affiliated density and the slow-variation step

In CPW's asymmetric $x$-representation, the density of the state in §2 is, with the displayed ordering,

$$
\rho_{\widehat\Phi}
\approx
\varepsilon\,
\overline g(\varepsilon h_R)\,
e^{-\beta_Hx}\,
\Delta_{\Phi|\Psi}\,
g(\varepsilon h_R).
$$

This is a positive operator affiliated with the right type II factor and normalized by the CPW trace to the working order. It is not an ordinary trace-class operator on the original type III algebra. The approximation uses that $g(\varepsilon y)$ varies on the broad scale $1/\varepsilon$: commuting it through an operator that changes the energy by $O(1)$ produces an $O(\varepsilon)$ correction.

Taking the logarithm while preserving the operator order is the subtle step. CPW use the relative modular cocycle to compare the core built from $\Psi$ with the one adapted to $\Phi$. Their controlled result can be organized as

$$
\log\rho_{\widehat\Phi}
\approx
-\beta_Hh_R
+h_{\Psi|\Phi}
-h_\Phi
+\log\!\left[\varepsilon|g(\varepsilon h_R)|^2\right]
+O(\varepsilon),
$$

where $h_\Phi=-\log\Delta_\Phi$ and $\langle\Phi|h_\Phi|\Phi\rangle=0$. The relative modular identity behind the rearrangement is the infinitesimal cocycle relation

$$
h_\Psi-h_{\Phi|\Psi}
=h_{\Psi|\Phi}-h_\Phi.
$$

This is the precise place where the Connes cocycle enters CPW's density derivation. It is not a license to call every later deformation calculation a cocycle expansion.

### 3.3 Entropy to controlled order

For the states of §2, CPW derive

$$
\boxed{
S(\widehat\Phi)_{\mathcal A_R}
{}={}
\beta_H\langle h_R\rangle_{\widehat\Phi}
-S_{\rm rel}(\Phi\Vert\Psi)_{\mathcal A_{R,0}}
-\left\langle
\log\!\left[\varepsilon|g(\varepsilon h_R)|^2\right]
\right\rangle_{\widehat\Phi}
+O(\varepsilon).}
$$

The three terms have distinct origins:

1. $\beta_H\langle h_R\rangle$ is the mean energy contribution.
2. $-S_{\rm rel}(\Phi\Vert\Psi)$ records how the bulk fluctuation state differs from equilibrium.
3. $-\langle\log \mu_\varepsilon(h_R)\rangle$ is the entropy of the energy wavepacket.

This is the detailed version of “modular energy minus relative entropy plus clock entropy.”

The derivation is now one line, but every ingredient has already been earned:

$$
S(\widehat\Phi)_{\mathcal A_R}
=-\langle\widehat\Phi|\log\rho_{\widehat\Phi}|\widehat\Phi\rangle.
$$

Insert the result of §3.2, use $\langle h_\Phi\rangle_\Phi=0$, and identify $\langle h_{\Psi|\Phi}\rangle_\Phi$ with $S_{\rm rel}(\Phi\Vert\Psi)$. The $O(\varepsilon)$ remainder includes precisely the commutators and state-identification corrections suppressed by the broad wavepacket.

### 3.4 Trace normalization

If the trace is rescaled by $e^c$, the density is rescaled by $e^{-c}$ and

$$
S(\widehat\Phi)_{\mathcal A_R}
\longmapsto
S(\widehat\Phi)_{\mathcal A_R}+c.
$$

The ambiguity is independent of $\Phi$. It is therefore meaningful to compare two states using the same normalization.

## 4. Why this equals generalized entropy

### 4.1 Relative entropy on the horizon

For the stationary reference black hole, excitations outside the horizon eventually fall through it. Raychaudhuri's equation relates the resulting area change to the null energy flux. In the special setting used by CPW, this gives a relation between the relative entropy of the exterior state and a difference of generalized entropies between the bifurcation surface $b$ and a late horizon cut:

$$
S_{\rm rel}(\Phi\Vert\Psi)
{}={}
S_{\rm gen}(\infty)-S_{\rm gen}(b).
$$

This is a gravitational input. It uses the semiclassical horizon equations, the relaxation assumption, and the reference equilibrium state.

The mechanism can be displayed without pretending to reproduce every geometric coefficient. Let $v$ be an affine parameter on a stationary horizon generator and $k^a=(\partial_v)^a$. Linearizing Raychaudhuri around a horizon with vanishing background expansion and shear gives

$$
\frac{d\theta}{dv}
=-8\pi G_N\,\langle T_{kk}\rangle
+O(G_N^2),
$$

where the quadratic expansion and shear terms are beyond the working order. Impose the teleological late-time boundary condition $\theta(\infty)=0$. Then

$$
\theta(v)
=8\pi G_N\int_v^\infty
\langle T_{kk}(v')\rangle\,dv'.
$$

Integrating once more along the horizon relates the area change to the weighted null-energy integral. The same weighted integral is the modular-energy change for the equilibrium horizon algebra. Schematically, with the orientation fixed as above,

$$
\frac{\Delta A}{4G_N}=\Delta\langle K_\Psi\rangle.
$$

On the QFT side, relative entropy obeys

$$
S_{\rm rel}(\Phi\Vert\Psi)
=\Delta\langle K_\Psi\rangle-\Delta S_{\rm bulk}.
$$

Combining the two equations turns “modular energy minus bulk entropy” into a difference of generalized entropies. CPW's precise choice of initial and late cuts yields the sign in the boxed relation above. The derivation requires the stationary reference, linearized semiclassical Einstein equation, late-time boundary condition, and relaxation; it is not a theorem about an arbitrary null surface.

### 4.2 Late-time energy and area

At late time, the exterior matter has relaxed and the ADM energy controls the stationary horizon area. Over the $O(1)$ energy range of the wavepacket,

$$
\frac{A}{4G_N}
{}={}
\frac{A_0}{4G_N}+\beta_H h_R+O(G_N).
$$

The energy-distribution term accounts for the entropy of area/energy fluctuations. Combining these statements with §3 gives

$$
\boxed{
S(\widehat\Phi)_{\mathcal A_R}
{}={}
S_{\rm gen}(b)+\text{const}+O(\varepsilon)+O(G_N),}
$$

where

$$
S_{\rm gen}(b)=\frac{A(\partial b)}{4G_N}+S_{\rm bulk}(b).
$$

The constant diverges as $G_N\to0$, exactly as one expects for a type II$_\infty$ entropy obtained by subtracting a universal divergent piece.

It is useful to perform the cancellation as a ledger. Write

$$
H_{\rm ADM}
:=-\left\langle\log\left[\varepsilon|g(\varepsilon h_R)|^2\right]\right\rangle.
$$

At the late cut, relaxation and the black-hole first law identify

$$
S_{\rm gen}(\infty)
=\beta_H\langle h_R\rangle+H_{\rm ADM}+C
$$

to the working order. The first term is the mean area response, the second is the classical entropy of the broad energy distribution, and $C$ fixes the reference area and trace normalization. Therefore

$$
\begin{aligned}
S(\widehat\Phi)_{\mathcal A_R}
&=\beta_H\langle h_R\rangle+H_{\rm ADM}
-S_{\rm rel}(\Phi\Vert\Psi)+O(\varepsilon)\\
&=S_{\rm gen}(\infty)-C
-\big[S_{\rm gen}(\infty)-S_{\rm gen}(b)\big]
+O(\varepsilon)\\
&=S_{\rm gen}(b)+\text{const}+O(\varepsilon).
\end{aligned}
$$

This is the didactic heart of CPW's Eq. (3.19): the late-cut generalized entropy appears twice and cancels. What remains is the generalized entropy of the bifurcation surface, plus the unavoidable state-independent normalization.

### 4.3 Claim status

- **Exact operator-algebraic:** $\mathcal A_R$ is type II$_\infty$ in the stated large-$N$ construction; it has a trace and densities.
- **Controlled semiclassical:** the CPW entropy formula for the slowly varying energy wavepacket, through $O(\varepsilon)$.
- **Semiclassical gravitational:** equality with $S_{\rm gen}$ in the $G_N\to0$ black-hole regime and under the relaxation assumptions.
- **Not claimed:** an exact fixed-$N$ identity for the full CFT, or a derivation of microscopic black-hole state counting.

## 5. The inner-unitary check

Take a unitary $U\in\mathcal A_{R,0}\subset\mathcal A_R$ and define $|\Phi\rangle=U|\Psi\rangle$, keeping the same energy wavepacket. The corresponding type-II density is unitarily conjugate to the reference density, so

$$
S(U\widehat\Psi)_{\mathcal A_R}=S(\widehat\Psi)_{\mathcal A_R}.
$$

The CPW formula must reproduce this. For a broad smooth wavepacket, changing an $O(1)$ bulk excitation changes the last, wavepacket term only at $O(\varepsilon)$. Consequently the displayed leading terms obey

$$
S_{\rm rel}(U\Psi\Vert\Psi)
{}={}
\beta_H\left(\langle h_R\rangle_{U\Psi}-\langle h_R\rangle_\Psi\right)
+O(\varepsilon).
$$

Hence the energy and relative-entropy contributions cancel at the controlled order. Exact unitary invariance says that the omitted corrections, including any change in the wavepacket expectation, cancel as well.

For a local Weyl coherent state $U=W(f)$ in the right wedge, this is the correct free-field check. The excitation may carry positive boost energy and have positive relative entropy, but its entropy on the right algebra does not change under the inner unitary.

> **Physical interpretation.** A local unitary rearranges the right degrees of freedom without changing their entropy. In the gravitational description, the bulk-matter and area responses must compensate. The cancellation is not an inconvenience; it is a stringent test of the generalized-entropy dictionary.

## 6. The area law and renormalization

### 6.1 Matter entropy

Before gravity is included, the regulated vacuum entropy of a $3+1$-dimensional field across a smooth surface has

$$
S_{\rm bulk}(\epsilon)
{}={}
c_2\frac{A}{\epsilon^2}+\cdots.
$$

In $1+1$ dimensions the corresponding CFT divergence is logarithmic. These are short-distance matter effects.

### 6.2 Generalized entropy

In semiclassical gravity, divergences in $S_{\rm bulk}$ are absorbed into the renormalization of gravitational couplings, including the coefficient of the area term. Neither $A/(4G_N)$ nor $S_{\rm bulk}$ is separately regulator-independent; their generalized-entropy combination is the physical quantity.

The type II trace entropy packages this renormalized combination up to one constant. It does not identify the matter cutoff $\epsilon$ with the energy-wavepacket parameter $\varepsilon$, and it does not obtain $A/(4G_N)$ from a one-dimensional Shannon entropy.

## 7. Right and left without double counting

Because $\mathcal A_L=\mathcal A_R'$, the two algebras describe complementary operator content in the standard representation. In a symmetric TFD state their entropies agree after compatible choices of trace normalization. This does not mean that one should add them and obtain twice the horizon area.

The generalized entropy associated with the right exterior uses the bifurcation surface once. The left exterior uses the same geometric surface from the complementary side. They are two restrictions of one state, not two independent horizon contributions.

## 8. Exact Fourier shadow

The finite-dimensional Fourier model of Semester II Week 4 remains a useful audit. For a system state $\rho$ and energy distribution $\mu(p)$,

$$
S_{\widehat\tau}=S(\rho)+H(\mu)-\mathbb E[p].
$$

Use the exact map $p=-\beta_Hx$. If the control model's probability density is chosen as the pushforward of CPW's $\mu_\varepsilon(x)$, then

$$
-\mathbb E[p]=\beta_H\mathbb E[x],
$$

while differential entropy changes under the rescaling by

$$
H(\mu_p)=H(\mu_\varepsilon)+\log\beta_H.
$$

The $+\log\beta_H$ is state-independent and can be absorbed into the trace normalization. Thus the last two terms reproduce the same “mean energy plus distribution entropy” structure as §3. The shift from $x$ to the physical right energy $h_R=x+h_\Psi/\beta_H$ brings in the modular contribution, which in the genuine type-III calculation is organized by the relative modular operator. What the toy model lacks is precisely that relative modular structure and the gravitational horizon relation.

## 9. What to take away

- CPW compute entropy for a controlled energy-wavepacket state, not for an unspecified “clock vector.”
- Their formula separates mean ADM energy, bulk relative entropy, and energy-distribution entropy.
- The energy-wavepacket parameter $\varepsilon$ is not the matter UV cutoff $\epsilon$.
- Trace rescaling by $e^c$ shifts entropy by $+c$.
- Generalized entropy follows after adding the semiclassical horizon-relative-entropy relation and the area-energy first law.
- A right-local inner unitary leaves the type-II entropy unchanged; modular energy and relative entropy cancel.
- The right and left algebras are commutants. Their use of the same bifurcation surface does not double the area term.

## 10. Looking ahead

Week 8 studies Bell correlations between the right algebra and its commutant. The algebraic prerequisites are now clean: bounded observables commute across the pair, while the state supplies the correlations. Neither the commutant relation nor type III$_1$ alone fixes the CHSH value for a specified quartet of observables.

## 11. Problem set

**Core problems.**

**1. Energy-wavepacket entropy.** For $\mu_\varepsilon(x)=\varepsilon|g(\varepsilon x)|^2$, prove $H(\mu_\varepsilon)=H(|g|^2)-\log\varepsilon$.

**2. CPW formula bookkeeping.** Rewrite the boxed formula of §3.3 as “mean energy $-$ relative entropy $+$ distribution entropy.” State the approximation associated with each equality.

**3. Trace normalization.** Derive the $+c$ entropy shift under $\widehat\tau\to e^c\widehat\tau$.

**4. Inner-unitary cancellation.** For $|\Phi\rangle=U|\Psi\rangle$ and an unchanged broad wavepacket, use exact type-II entropy invariance and the CPW expansion to derive the leading equality between relative entropy and the ADM-energy change. Estimate why the change of the wavepacket term is $O(\varepsilon)$, and explain what must cancel it at the next order.

**5. No double counting.** Explain why equal right and left entropies in a symmetric state do not imply a generalized entropy with $2A/(4G_N)$.

**Starred problems.**

**6\*. CPW density.** Read CPW §3.2 and reproduce the affiliated density operator for $|\widehat\Phi\rangle$ through $O(\varepsilon)$. Mark where the Connes cocycle is used.

**7\*. Horizon derivation.** Reproduce CPW's use of the linearized Raychaudhuri equation to obtain the area-energy relation. List the boundary condition at late affine time.

**8\*. Gaussian energy profile.** Take $|g(y)|^2$ Gaussian. Compute all wavepacket terms in §3.2, including their $\varepsilon$ dependence, without interpreting $\varepsilon$ as a UV cutoff.

**9\*. Coherent Rindler check.** Let $U=W(f)$ with support in $W_R$. Explain why $U$ is inner for the right wedge algebra and show that the increase in boost modular energy equals the Araki relative entropy. Do not claim a nonzero entropy difference.

**10\*. Two independent scales.** Introduce symbols $\varepsilon_{\rm ADM}$ for the inverse wavepacket width and $\epsilon_{\rm UV}$ for the matter regulator. Track them through the CPW wavepacket and a regulated free-field entropy. Identify which dependence belongs to the chosen family of states and which is absorbed by UV renormalization; do not identify the two scales.

**Project problems.**

**11. CPW derivation map.** Write a six-page derivation of CPW's Eq. (3.19), with separate columns for operator-algebra, semiclassical-gravity, and relaxation assumptions.

**12. Comparison with Witten.** Compare Witten's canonical-ensemble collective coordinate with CPW's microcanonical scaling. Explain why their trace formulas have the same continuous-core structure even though the physical energy variables are introduced differently.

## 12. Instructor checkpoints (internal)

1. **Wavepacket entropy:** substitute $y=\varepsilon x$ to obtain $H(\mu_\varepsilon)=H(|g|^2)-\log\varepsilon$.
2. **Three-term ledger:** the distribution term is exactly $H(\mu_\varepsilon)$ at the probability-law level; replacing the affiliated density and logarithm by the displayed CPW expression carries the $O(\varepsilon)$ control. The generalized-entropy interpretation is a separate semiclassical step.
3. **Normalization:** $D'=e^{-c}D$ under $\widehat\tau'=e^c\widehat\tau$, so $S'=S+c$.
4. **Inner unitary:** exact trace entropy is invariant. For $F(y)=\log[\varepsilon|g(\varepsilon y)|^2]$, an $O(1)$ energy shift changes $F$ by $O(\varepsilon)$ when the logarithmic derivative is controlled. The complete omitted terms must restore exact cancellation.
5. **No double counting:** $\mathcal A_L=\mathcal A_R'$ describes the complementary restriction in one standard representation. The same bifurcation surface appears once in either generalized entropy; the two restrictions are not independent geometric systems to be summed.
6. **Density:** the accepted ordering is $\varepsilon\bar g(\varepsilon h_R)e^{-\beta_Hx}\Delta_{\Phi|\Psi}g(\varepsilon h_R)$ to $O(\varepsilon)$. The cocycle derivative supplies $h_\Psi-h_{\Phi|\Psi}=h_{\Psi|\Phi}-h_\Phi$.
7. **Horizon derivation:** linearize Raychaudhuri, impose $\theta(\infty)=0$, integrate twice, and match the weighted null-energy integral to the equilibrium modular Hamiltonian. Missing the late boundary condition leaves the integration constant undetermined.
8. **Gaussian:** if $|g(y)|^2$ has mean $m$ and variance $s^2$, then $x$ has mean $m/\varepsilon$, variance $s^2/\varepsilon^2$, and entropy $\tfrac12\log(2\pi e s^2)-\log\varepsilon$. The mean-energy term inherits the $m/\varepsilon$ contribution; for the usual centered profile $m=0$.
9. **Coherent state:** $W(f)$ is a unitary of the right algebra for $\operatorname{supp}f\subset W_R$. Same-clock conjugation gives $\Delta S=0$, hence relative entropy equals the boost modular-energy increase.
10. **Two scales:** $\varepsilon_{\rm ADM}$ labels a family of broad energy states and appears in differential entropy; $\epsilon_{\rm UV}$ is a spacetime regulator and appears in $A/\epsilon_{\rm UV}^2$ in four dimensions. Only the latter participates in UV coupling renormalization.
11. **Derivation-map rubric:** the final cancellation must show $S_{\rm gen}(\infty)$ appearing both in the late energy/distribution ledger and in $S_{\rm rel}=S_{\rm gen}(\infty)-S_{\rm gen}(b)$.
12. **Witten comparison:** Witten retains the perturbative modular action around a leading canonical central variable; CPW keep an $O(1)$ noncentral energy in the strict microcanonical limit. Both yield covariant representations of the same continuous-core pattern.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 2. Last revised 2026-08-24.*
