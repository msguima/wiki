---
title: "Sem II Week 4 — Rindler Crossed Product: Exact Checks and Honest Limits"
type: lecture-notes
course: syllabus
semester: 2
week: 4
block: 1
duration: "master dossier: 4 hours of material; classroom core: 2-hour seminar + 1-hour office/self-study"
prerequisites: Sem II Weeks 1–3; Sem I Weeks 8–15
target_paper: "course-built Rindler audit of Witten, arXiv:2112.12828 §§3.4–3.5"
modified: 2026-09-29
---

# Sem II Week 4 — Rindler Crossed Product: Exact Checks and Honest Limits

> *The purpose of a mini-calculation is to expose the mechanism, not to decorate an abstract theorem with a formal integral. We therefore divide the calculation into three layers. The Rindler wedge gives an exact type III$_1$ algebra and exact geometric modular flow. The inner-action Fourier model gives an exact trace, density, and entropy calculation. A regulated free field gives the familiar matter area law. These layers fit together, but none can substitute for the others. In particular, the width of the crossed-product clock is not the matter UV cutoff, and a same-clock Weyl excitation has exactly the same trace entropy as the vacuum because it is an inner unitary conjugation.*

## 0. Reading

**Primary:**

- Witten, “Gravity and the crossed product,” arXiv:2112.12828, §§3.3–3.5. Section 4 concerns other conserved charges; it is not a free-field section.
- Sem I Weeks 13–14 and Appendix D.

**Free-field background:**

- Bisognano and Wichmann, *J. Math. Phys.* **16** (1975) 985 and **17** (1976) 303.
- Bombelli, Koul, Lee, Sorkin, *Phys. Rev. D* **34** (1986) 373.
- Srednicki, *Phys. Rev. Lett.* **71** (1993) 666.

### 0.1 How to use this master dossier

- **Classroom core:** §§1–2, 3.1–3.3, 4.1–4.2, and 5.1–5.3, with Problems 1–5. This route puts one exact theorem, one exact trace model, and one exact cancellation on the board.
- **Full derivation / self-study:** §§3.4, 4.3, 5.4, and 6, with Problems 6–10. This route audits units, trace normalization, non-inner comparisons, and the independent matter regulator.
- **Research extension:** §§7–8 and Problems 11–12. This route asks which conclusions survive in Witten's gravitational setting and which require genuinely new bulk input.

The chapter is intentionally layered. A student should always be able to label a displayed equation as an exact wedge-algebra statement, an exact inner-action control calculation, a regulated QFT statement, or a gravitational comparison.

## 1. Scope of the calculation

### 1.1 Exact QFT input

We use the course's mostly-plus convention $\eta_{\mu\nu}=\operatorname{diag}(-1,+1,+1,+1)$. For the right Rindler wedge

$$
W_R=\{x\in\mathbb R^{1,3}:x^1>|x^0|\},
$$

let $\mathcal A(W_R)$ be the vacuum wedge algebra of a free scalar field. Under the usual hypotheses it is the hyperfinite type III$_1$ factor. Bisognano–Wichmann gives

$$
\Delta_{W_R}=e^{-2\pi K_{\rm boost}},
\qquad
\sigma_t(a)=e^{i2\pi tK_{\rm boost}}a e^{-i2\pi tK_{\rm boost}}.
$$

Therefore

$$
\widehat{\mathcal A}(W_R)
:=
\mathcal A(W_R)\rtimes_\sigma\mathbb R
$$

is a type II$_\infty$ factor with a faithful normal semifinite trace. These statements are exact.

For orientation, take the real Klein–Gordon field with

$$
(\Box-m^2)\phi=0,
\qquad
\Box=-\partial_0^2+\nabla^2,
$$

and form Weyl operators $W(f)=e^{i\phi(f)}$ from real test functions modulo the field equation. With $E$ the causal propagator,

$$
W(f)W(g)=e^{-iE(f,g)/2}W(f+g).
$$

If $\Lambda(u)$ is the boost in the $(x^0,x^1)$ plane and $f_u(x):=f(\Lambda(-u)x)$, covariance gives

$$
e^{iuK_{\rm boost}}W(f)e^{-iuK_{\rm boost}}=W(f_u).
$$

The displayed Bisognano–Wichmann convention therefore says $\sigma_t(W(f))=W(f_{2\pi t})$. Writing the pullback explicitly is useful: it fixes the sign in $f_{-2\pi q}$ below instead of leaving the sign to memory.

### 1.2 What is not being claimed

There is no ordinary density matrix for the vacuum restricted to $\mathcal A(W_R)$. Nor will we derive the canonical trace by inserting nonnormalizable vectors $|0_M\rangle\otimes|\delta_q\rangle$. Finally, the free scalar does not contain Newton's constant, so it cannot derive the coefficient $1/(4G_N)$.

The calculation instead checks:

1. the crossed-product covariance and all convention signs;
2. the canonical trace scaling in an exact Fourier model;
3. the density and entropy of explicit product states in that model;
4. unitary invariance for a local coherent excitation;
5. the independent origin of the matter UV area law.

### 1.3 Variable dictionary

| Symbol | Meaning |
|---|---|
| $t$ | dimensionless modular parameter |
| $u=2\pi t$ | physical boost rapidity |
| $q$ | scalar coordinate in the regular representation |
| $Q$ | multiplication operator, $(Q\xi)(q)=q\xi(q)$ |
| $P=-i\partial_q$ | conjugate momentum; $\lambda(t)=e^{-itP}$ |
| $p$ | spectral variable of $P$ after Fourier transform |
| $r$ | dual-action parameter |

Calling $P$ “position” or treating $g(P)$ as multiplication by $g(q)$ would invalidate the trace calculation.

## 2. Sub-task 1: construct the Rindler core

On $\mathcal F\otimes L^2(\mathbb R_q)$ define

$$
(\pi(W(f))\xi)(q)=\sigma_{-q}(W(f))\xi(q),
\qquad
(\lambda(t)\xi)(q)=\xi(q-t).
$$

Since the modular action is geometric,

$$
\sigma_{-q}(W(f))=W(f_{-2\pi q}),
$$

where the subscript of $f_{-2\pi q}$ is a **physical rapidity**. This distinction matters: $q$ is the regular-representation coordinate, while $-2\pi q$ is the rapidity selected by the modular parameter $-q$.

The covariance check is

$$
\begin{aligned}
(\lambda(t)\pi(W(f))\lambda(t)^*\xi)(q)
&=\sigma_{-(q-t)}(W(f))\xi(q)\\
&=(\pi(\sigma_t(W(f)))\xi)(q).
\end{aligned}
$$

Thus

$$
\lambda(t)\pi(W(f))\lambda(t)^*=\pi(\sigma_t(W(f))).
$$

The dual action is

$$
\theta_r(\pi(a))=\pi(a),
\qquad
\theta_r(\lambda(t))=e^{itr}\lambda(t),
$$

implemented in the ambient algebra by $e^{irQ}$. In the $P$-spectrum it is $p\mapsto p-r$.

## 3. Sub-task 2: exact trace calculation in the Fourier model

### 3.1 Why we change models

For the type III wedge, the existence of $\widehat\tau$ is an abstract theorem. To compute a weighted integral without hiding domain questions, replace the wedge algebra temporarily by $M_n(\mathbb C)$ with a faithful density matrix $\rho$. The modular action is inner, so the crossed product can be untwisted and Fourier transformed:

$$
M_n(\mathbb C)\rtimes_{\sigma^\rho}\mathbb R
\cong
M_n(\mathbb C)\bar\otimes L^\infty(\mathbb R_p).
$$

This is a type-I algebra with centre; it is not the Rindler core. It is nevertheless the right laboratory for the trace formula.

The unitary equivalence can be seen directly. In the regular representation,

$$
(\pi_\rho(a)\xi)(q)=\rho^{iq}a\rho^{-iq}\xi(q).
$$

Define the decomposable unitary

$$
(V\xi)(q)=\rho^{-iq}\xi(q).
$$

Then

$$
V\pi_\rho(a)V^*=a\otimes1,
\qquad
V\lambda(t)V^*=\rho^{-it}\otimes\lambda(t).
$$

Because $\rho^{it}\in M_n(\mathbb C)$, the algebra generated by $a\otimes1$ and $\rho^{-it}\otimes\lambda(t)$ is the same as the algebra generated by $M_n(\mathbb C)\otimes1$ and $1\otimes\lambda(t)$. Fourier transformation sends the abelian group von Neumann algebra generated by $\lambda(t)$ to $L^\infty(\mathbb R_p)$. This derivation explains both features of the model: the crossed product has a centre because the original action was inner, and $p$—not $q$—is the multiplication variable in the final trace formula.

### 3.2 A genuine trace ideal

Let $a\geq0$ be a matrix and let $f\geq0$ be bounded with compact support. Then

$$
\widehat\tau(a\otimes f(P))
{}={}
\operatorname{Tr}(a)\int_{\mathbb R}f(p)e^{-p}dp
<\infty.
$$

Finite linear combinations of such positive elements generate a concrete $\widehat\tau$-finite ideal. No distributional vectors and no unspecified “regularization” are required.

### 3.3 Dual scaling

Because $\theta_r(f(P))=f(P-r)$,

$$
\begin{aligned}
\widehat\tau(\theta_r(a\otimes f(P)))
&=\operatorname{Tr}(a)\int f(p-r)e^{-p}dp\\
&=e^{-r}\operatorname{Tr}(a)\int f(p')e^{-p'}dp'\\
&=e^{-r}\widehat\tau(a\otimes f(P)).
\end{aligned}
$$

This proves the scaling law in the model with the same normalization used for the type III core.

### 3.4 Rindler normalization

The variable $p$ belongs to the **auxiliary Fourier model**. To compare normalizations, define $E:=p/(2\pi)$; if a physical construction identifies this auxiliary spectral coordinate with a boost-energy collective variable, then

$$
e^{-p}dp=2\pi e^{-2\pi E}dE.
$$

The constant $2\pi$ is absorbed into the arbitrary normalization of the type II$_\infty$ trace. This reproduces the form of the Unruh weight in the comparison variable $E$, not a derivation that the auxiliary $p$ equals the matter boost generator. In either case it is not a weight $e^{-2\pi q}$ on the regular coordinate $q$.

## 4. Sub-task 3: density and entropy of an explicit state

### 4.1 Product state

Choose a probability density $\mu(p)$ and define

$$
\widehat\omega(a\otimes f(P))
{}={}
\operatorname{Tr}(\rho a)\int\mu(p)f(p)dp.
$$

Relative to $\widehat\tau$, its density is

$$
D(p)=\rho\mu(p)e^p.
$$

Indeed,

$$
\widehat\tau(D(a\otimes f(P)))
{}={}
\operatorname{Tr}(\rho a)\int\mu(p)f(p)dp.
$$

### 4.2 Entropy

Assume $S(\rho)<\infty$, $\int\mu|\log\mu|<\infty$, and $\int|p|\mu(p)dp<\infty$. Since the matrix and abelian factors commute,

$$
\log D(p)=\log\rho+\log\mu(p)+p.
$$

The trace weight cancels the density factor before the logarithm is averaged:

$$
\begin{aligned}
S_{\widehat\tau}(\widehat\omega)
&=-\int e^{-p}\operatorname{Tr}\!\left[\rho\mu(p)e^p
\big(\log\rho+\log\mu(p)+p\big)\right]dp\\
&=-\operatorname{Tr}(\rho\log\rho)
-\int\mu(p)\log\mu(p)dp
-\int p\mu(p)dp.
\end{aligned}
$$

Therefore

$$
\boxed{
S_{\widehat\tau}(\widehat\omega)
{}={}
S(\rho)+H(\mu)-\mathbb E_\mu[p].}
$$

For a Gaussian with mean $p_0$ and width $\sigma$,

$$
S_{\widehat\tau}
{}={}
S(\rho)+\frac12\log(2\pi e\sigma^2)-p_0.
$$

The mean term comes from the nonuniform trace measure; it must be retained.

If the displayed integrability assumptions fail, the entropy can be extended-real or undefined through an $\infty-\infty$ subtraction. The algebra supplies a trace; it does not guarantee that every normal state's entropy is a finite real number.

### 4.3 Trace rescaling audit

For $\widehat\tau'=c\widehat\tau$, the same state has density $D'=D/c$, and

$$
S_{\widehat\tau'}=S_{\widehat\tau}+\log c.
$$

This sign agrees with Witten and CPW after translating their trace convention.

## 5. Sub-task 4: coherent-state cancellation

### 5.1 The state is an inner conjugate

Let $f$ be real and supported in $W_R$. Then $W(f)\in\mathcal A(W_R)$, and its image $U=\pi(W(f))$ is a unitary in the core. If the vacuum lift has density $D_0$ and the coherent state uses the same clock and the same core identification, then

$$
D_f=UD_0U^*.
$$

### 5.2 Entropy is invariant

Functional calculus gives $\log D_f=U(\log D_0)U^*$, so

$$
\begin{aligned}
S_{\widehat\tau}(D_f)
&=-\widehat\tau(UD_0\log D_0U^*)\\
&=-\widehat\tau(D_0\log D_0)
=S_{\widehat\tau}(D_0).
\end{aligned}
$$

Hence

$$
\boxed{S_{\widehat\tau}(D_f)-S_{\widehat\tau}(D_0)=0.}
$$

### 5.3 Relative entropy and modular energy cancel

Applying the exact entropy-difference identity,

$$
0
{}={}
-S(D_f\Vert D_0)
+\widehat\tau[(D_f-D_0)K_0],
\qquad
K_0=-\log D_0.
$$

Thus

$$
\boxed{S(D_f\Vert D_0)=\Delta\langle K_0\rangle.}
$$

This is the correct coherent-state result for an inner Weyl excitation. A formula with two nonzero terms is not wrong if the terms cancel; it is wrong if it presents their sum as an independent nonzero entropy change.

### 5.4 When a nonzero answer is possible

A nonzero result can arise if the excitation is not inner relative to the chosen algebra, if the clock distribution changes, or if two state-dependent cores are compared through a nontrivial cocycle identification. The calculation must say which mechanism is present.

## 6. Sub-task 5: the matter area law

### 6.1 The regulated free-field entropy

The matter vacuum entropy is computed in a regulated type-I approximation to the local QFT. In $3+1$ dimensions,

$$
S_{\rm matter}(W_R;\epsilon)
{}={}
c_2\frac{A_\perp}{\epsilon^2}
+c_{\log}\log\frac{L}{\epsilon}+\cdots,
$$

where $c_2$ is regulator-dependent. For the infinite Rindler plane it is more natural to quote entropy per unit transverse area.

A lattice count explains the power without pretending to determine the coefficient. Discretize each transverse direction with spacing $\epsilon$. A patch of entangling surface of area $A_\perp$ meets approximately

$$
N_\perp\sim\frac{A_\perp}{\epsilon^2}
$$

independent near-boundary transverse cells. Local vacuum correlations across the cut give an $O(1)$ entropy per regulated cell, so the leading contribution scales as $N_\perp$. The precise $c_2$ depends on the regulator and field content. For a flat plane in a massless conformal theory, a universal logarithmic term need not be present; logarithms arise when masses, curvature, corners, or other scales supply the required dimensionless ratio. The leading four-dimensional statement relevant here is the area law.

In $1+1$ dimensions there is no transverse area. A CFT interval has

$$
S_{\rm interval}
{}={}
\frac c3\log\frac{\ell}{\epsilon}+\text{const},
$$

and a half-line has the corresponding one-boundary coefficient $c/6$ after introducing an infrared scale.

Thus “logarithmic divergence” is the characteristic $1+1$-dimensional statement, whereas “area divided by $\epsilon^2$” is the leading $3+1$-dimensional statement. Writing one formula for both dimensions hides the geometry that the divergence is measuring.

### 6.2 Why this is not the clock entropy

For a Gaussian $\mu$, the clock contribution is

$$
H(\mu)=\log\sigma+\frac12\log(2\pi e),
$$

which tends to $-\infty$ as $\sigma\to0$. The matter entropy tends to $+\infty$ as $\epsilon\to0$. Besides the opposite sign, the four-dimensional matter divergence carries a transverse area. A one-dimensional clock distribution cannot produce that factor.

Therefore

$$
\boxed{\sigma\ \text{and}\ \epsilon\ \text{are independent scales}.}
$$

The crossed product provides a renormalized trace framework; it does not manufacture the matter UV area law.

## 7. Comparison with Witten's gravitational construction

| Layer | Rindler/QFT statement | Witten statement |
|---|---|---|
| Algebra | $\mathcal A(W_R)$ is type III$_1$ | strict-$N$ noncentral algebra is type III$_1$ |
| Modular flow | exact boost by $u=2\pi t$ | TFD modular flow generated by $\beta_H\widehat H$ |
| Core | type II$_\infty$ by Takesaki's structure theorem | perturbative energy-inclusive algebra is type II$_\infty$ |
| Trace | abstract on type III core; exact in Fourier model | explicit on Witten's classical-quantum trace domain |
| Entropy | exact semifinite identity | black-hole entropy up to a constant for the specified states |
| UV law | independent regulated matter calculation | gravitational area term fixed by the semiclassical dictionary |

The free-field construction verifies the algebraic mechanism and the convention signs. It does not verify Witten's gravitational identification in a theory without gravity.

## 8. What is proved, modeled, and imported

- **Proved in the QFT setup:** Bisognano–Wichmann modular flow; type III$_1$ wedge algebra under the stated hypotheses; type II$_\infty$ continuous core.
- **Computed exactly in the inner-action model:** trace ideal, dual scaling, product-state density, entropy, and trace-rescaling sign.
- **Computed exactly for the coherent lift:** unitary invariance and relative-entropy/modular-energy cancellation.
- **Imported from regulated QFT:** the logarithmic $1+1$ law and the $A/\epsilon^2$ leading divergence in $3+1$.
- **Not derived here:** $1/(4G_N)$, the black-hole area response, or the full Witten entropy formula.

## 9. What to take away

- $q$ is the regular coordinate, $Q$ multiplies by $q$, and $P=-i\partial_q$. The trace weight belongs to the Fourier variable $p$, not to $q$.
- The canonical law is $\widehat\tau\circ\theta_r=e^{-r}\widehat\tau$.
- A valid trace check uses a genuine trace ideal, such as finite-rank matrices tensored with compactly supported functions of $P$.
- Product entropy is $S(\rho)+H(\mu)-\mathbb E[p]$.
- Same-clock inner Weyl excitation implies zero entropy difference and exact cancellation between relative entropy and modular energy.
- Clock width and matter cutoff are distinct. The crossed product does not derive the free-field area law.
- The Rindler example tests the algebraic skeleton; gravity supplies the generalized-entropy interpretation.

## 10. Problem set

**Core problems.**

**1. Covariance.** Verify the crossed-product covariance on a Schwartz vector and track the boost pullback convention for $f_{-2\pi q}$.

**2. Canonical pair.** Show $[Q,P]=i$, $\lambda(t)=e^{-itP}$, and $e^{irQ}Pe^{-irQ}=P-r$. Deduce the dual action on $f(P)$.

**3. Trace ideal.** Choose $a\geq0$ in $M_2(\mathbb C)$ and $f(p)=\mathbf1_{[-L,L]}(p)$. Compute $\widehat\tau(a\otimes f(P))$ and its dual transform explicitly.

**4. Gaussian density.** Derive $D(p)=\rho\mu(p)e^p$ and $S=S(\rho)+\frac12\log(2\pi e\sigma^2)-p_0$.

**5. Coherent cancellation.** Starting from $D_f=UD_0U^*$, prove entropy invariance and the equality of relative entropy and modular-energy increase.

**6. Two scales.** Make a two-column dimensional-analysis table for the distribution width $\sigma$ and the matter regulator $\epsilon$. Explain why a scalar width in modular-energy space cannot supply $A_\perp/\epsilon^2$.

**Starred problems.**

**7\*. Witten's trace.** Reproduce Witten's §3.4 trace formula and translate it with $p=-X$. State the analytic or decay assumptions on the operator.

**8\*. Non-inner comparison.** Give a finite-dimensional pair of faithful densities not related by unitary conjugation. Compute $\Delta S$, relative entropy, and the modular-energy term, and verify the exact identity numerically or symbolically.

**9\*. Regulated Rindler modes.** Introduce a transverse lattice cutoff and explain how the number of near-boundary oscillators scales as $A_\perp/\epsilon^2$. Keep this calculation separate from the clock distribution.

**10\*. Cocycle variant.** Describe how a state-dependent core identification can turn a simple product lift into a non-product lift. Identify the point at which the inner-unitary cancellation no longer applies.

**Project problems.**

**11. Block-1 final writeup.** Write a 7–10 page account with three explicitly labeled layers: exact Rindler modular theory, exact Fourier trace model, and gravitational interpretation. Any statement crossing from one layer to another must name the extra assumption.

**12. Reproducibility appendix.** Prepare a one-page convention sheet containing $t,u,q,Q,P,p,r$, the two Fourier conventions, the trace weight, and the entropy-rescaling sign. Another student should be able to reproduce every sign from that page alone.

## 11. Instructor checkpoints (internal)

1. **Covariance:** $\lambda(t)^*$ first sends $q$ to $q+t$; the subsequent translation produces $\sigma_{-(q-t)}=\sigma_{-q}\sigma_t$. With $f_u(x)=f(\Lambda(-u)x)$, the fibre smearing is $f_{-2\pi q}$ if the rapidity label is written explicitly.
2. **Canonical pair:** on $C_c^\infty$, $[Q,P]=i$; Baker–Campbell–Hausdorff gives $e^{irQ}Pe^{-irQ}=P-r$, hence $\theta_r(f(P))=f(P-r)$.
3. **Trace ideal:** for $f=\mathbf1_{[-L,L]}$, $\widehat\tau(a\otimes f)=\operatorname{Tr}(a)(e^L-e^{-L})$. Its dual transform has support $[r-L,r+L]$ and trace $e^{-r}\operatorname{Tr}(a)(e^L-e^{-L})$.
4. **Gaussian:** $D=\rho\mu e^p$; the $e^p$ cancels the trace weight. The entropy is $S(\rho)+\tfrac12\log(2\pi e\sigma^2)-p_0$.
5. **Coherent cancellation:** functional calculus gives $\log(UD_0U^*)=U\log D_0U^*$ and traciality gives $\Delta S=0$. The exact difference identity then forces $S(D_f\Vert D_0)=\Delta\langle K_0\rangle$.
6. **Two scales:** $\sigma$ is a width in the dimensionless auxiliary $p$ variable; $\epsilon$ is a spacetime length cutoff. Only the latter combines with $A_\perp$ to give $A_\perp/\epsilon^2$.
7. **Witten trace:** the accepted derivation uses his analytic strip and contour shift; a diagonal $\delta_q$ matrix element receives no credit.
8. **Non-inner pair:** for commuting faithful matrices with eigenvalues $r_i$ and $s_i$, check $\Delta S=-\sum_i r_i\log r_i+\sum_i s_i\log s_i$, $S(r\Vert s)=\sum_i r_i\log(r_i/s_i)$, and $\Delta\langle K_s\rangle=-\sum_i(r_i-s_i)\log s_i$. These satisfy the identity term by term.
9. **Rindler lattice:** the number of transverse cells meeting the cut is $N_\perp\sim A_\perp/\epsilon^2$; an $O(1)$ short-distance contribution per cell yields the leading area scaling, not its regulator-dependent coefficient.
10. **Cocycle variant:** the state-change isomorphism modifies the group implementer by a relative modular cocycle. After this joint transformation the lifted density need not equal $UD_0U^*$ for one unitary in one fixed core, so the inner-unitary proof no longer applies.
11. **Final-writeup rubric:** each cross-layer arrow must name the new input; in particular, the free field never supplies $G_N$.
12. **Convention sheet:** it must include $\sigma_t=\operatorname{Ad}\Delta^{-it}$, $\lambda(t)=e^{-itP}$, $p=-X_{\rm W}$, and $\widehat\tau\circ\theta_r=e^{-r}\widehat\tau$.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 1. Last revised 2026-09-29.*

*End of Sem II Block 1.*
