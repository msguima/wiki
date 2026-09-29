---
title: "Week 14 — Dressed Entropy and the Modular-Energy Term"
type: lecture-notes
course: syllabus
semester: 1
week: 14
block: D
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Week 13 (crossed product), Week 7 (Connes cocycle + Araki–Uhlmann)
modified: 2026-08-24
---

# Week 14 — Dressed Entropy and the Modular-Energy Term

> *The continuous core gives us a trace, but a trace is only the beginning of the entropy problem. We must still specify a normal state on the core, find its density relative to the trace, and control the positive and negative parts of $-D\log D$. This week separates three statements that are often merged too quickly. First, entropy on a semifinite algebra is an exact trace-theoretic construction. Second, “entropy difference = minus relative entropy plus modular-energy difference” is an exact algebraic identity for two densities in the same semifinite algebra. Third, identifying this result with $A/(4G_N)+S_{\rm out}$ is a physical theorem requiring the gravitational setting. The type-I Fourier model lets us verify every sign without pretending that a type III wedge has a density matrix.*

## 0. Reading

**Primary:**

- Witten, “Gravity and the crossed product,” arXiv:2112.12828, §§3.4–3.5 (trace, density matrices, and entropy).
- Takesaki, *Theory of Operator Algebras II*, ch. X and §V.2 (continuous cores and noncommutative Radon–Nikodym theory).

**Secondary:**

- Chandrasekaran, Penington, Witten (CPW), arXiv:2209.10454, §§2.2–3 (type-II entropy and generalized entropy).
- Ahmad and Jefferson, arXiv:2306.07323 (crossed products for QFT subregions, with the gravity-independent scope made explicit).

**Optional research reading:**

- Araki, “Relative entropy of states of von Neumann algebras,” *Publ. RIMS* **11** (1976) 809.
- Casini, “Relative entropy and the Bekenstein bound,” *Class. Quantum Grav.* **25** (2008) 205021, arXiv:0804.2182.

### 0.1 How to use this master dossier

- **Classroom core:** §§1–3 and Problems 1–6. This route derives the trace-rescaling sign, the exact product entropy, and the entropy-difference identity.
- **Full derivation / self-study:** §§4–5 and Problems 7–9. This route checks coherent-state cancellation and separates clock width from the matter UV cutoff.
- **Research extension:** §6 and Problems 10–11. This route maps the abstract identities to Witten and CPW while keeping the gravitational input explicit.

For every entropy formula, first name the algebra, trace, density, and domain. Only then ask for a geometric interpretation.

## 1. What the trace does—and does not—give us

### 1.1 The continuous core

Let $\mathcal M$ be a type III$_1$ factor, $\omega$ a faithful normal state, and

$$
\widehat{\mathcal M}
{}={}
\mathcal M\rtimes_{\sigma^\omega}\mathbb R
$$

its continuous core. By Week 13, $\widehat{\mathcal M}$ is a type II$_\infty$ factor with a faithful normal semifinite trace $\widehat\tau$ satisfying

$$
\widehat\tau\circ\theta_r=e^{-r}\widehat\tau.
$$

The word **semifinite** matters. The identity has infinite trace, but sufficiently many positive operators have finite trace that every positive element can be approximated from below by finite-trace ones.

### 1.2 Densities relative to a semifinite trace

Let $\widehat\omega$ be a normal positive functional on $\widehat{\mathcal M}$. The noncommutative Radon–Nikodym theorem gives a positive $\widehat\tau$-measurable operator $D_{\widehat\omega}$, affiliated with $\widehat{\mathcal M}$, such that

$$
\widehat\omega(x)=\widehat\tau(D_{\widehat\omega}x)
$$

on the natural domain. If $\widehat\omega$ is normalized, then $\widehat\tau(D_{\widehat\omega})=1$.

[[functional-analysis-survival-kit|Appendix A §A.5.2]] defines affiliation and
$\widehat\tau$-measurability; in particular, $D_{\widehat\omega}$ need not be
a bounded element of the core.

The trace entropy is

$$
S_{\widehat\tau}(\widehat\omega)
:=
-\widehat\tau(D_{\widehat\omega}\log D_{\widehat\omega}).
$$

If both parts are finite, the entropy is a real number. If exactly one part is finite, it is well-defined as $+\infty$ or $-\infty$; if both are infinite, the expression is undefined as $\infty-\infty$. Thus the existence of a trace does not imply that every normal state has finite entropy.

### 1.3 Trace normalization and the sign of the entropy shift

Suppose we replace the trace by $\widehat\tau'=c\widehat\tau$, $c>0$, while keeping the state fixed. Its density becomes $D'=D/c$, because

$$
\widehat\tau'(D'x)=c\widehat\tau\!\left(\frac Dc x\right)=\widehat\omega(x).
$$

Therefore

$$
\begin{aligned}
S_{\widehat\tau'}(\widehat\omega)
&=-c\widehat\tau\!\left(\frac Dc\log\frac Dc\right)\\
&=-\widehat\tau(D\log D)+\log c\,\widehat\tau(D)\\
&=S_{\widehat\tau}(\widehat\omega)+\log c.
\end{aligned}
$$

Hence

$$
\boxed{\widehat\tau\longmapsto c\widehat\tau
\quad\Longrightarrow\quad
S\longmapsto S+\log c.}
$$

Every normalized state shifts by the same constant, so entropy differences are unchanged.

> **Physical interpretation.** The additive constant is a normalization ambiguity of the type II$_\infty$ trace. In a gravitational application it can be matched to a renormalization convention for generalized entropy. This match is meaningful, but it is not supplied by the operator-algebra theorem alone.

## 2. Exact laboratory: the inner-action Fourier model

The genuine type III core is best treated abstractly. To see the density and entropy without hiding a representation change, we use the exact type-I model of Week 13.

### 2.1 Algebra and trace

Take $\mathcal M=\mathcal B(\mathcal H)$, with $\dim\mathcal H<\infty$ for convenience, and a faithful state $\omega(a)=\operatorname{Tr}(\rho a)$. After untwisting the inner modular action and Fourier transforming the regular coordinate $q$, the core is

$$
\widehat{\mathcal M}
\cong
\mathcal B(\mathcal H)\bar\otimes L^\infty(\mathbb R_p),
$$

with trace

$$
\widehat\tau(a\otimes f(P))
{}={}
\operatorname{Tr}(a)\int_{\mathbb R} f(p)e^{-p}dp.
$$

Here $p$ is the spectral variable of $P=-i\partial_q$. It is not the regular-representation coordinate $q$ on which $Q$ acts by multiplication.

### 2.2 A product state and its density

Let $\mu(p)dp$ be a probability distribution and define

$$
\widehat\omega(a\otimes f(P))
{}={}
\operatorname{Tr}(\rho a)\int_{\mathbb R}\mu(p)f(p)dp.
$$

To solve $\widehat\omega(x)=\widehat\tau(Dx)$, compare the two integrals. The density is

$$
\boxed{D(p)=\rho\,\mu(p)e^p.}
$$

The sign of $e^p$ is forced: it cancels the $e^{-p}$ in the trace.

### 2.3 Product entropy

Because $\rho$ and $\mu(P)e^P$ commute,

$$
\log D=\log\rho+\log\mu(P)+P.
$$

Substituting in the entropy gives

$$
\begin{aligned}
S_{\widehat\tau}(\widehat\omega)
&=-\operatorname{Tr}(\rho\log\rho)
-\int\mu(p)\log\mu(p)dp
-\int p\mu(p)dp\\
&=S(\rho)+H(\mu)-\mathbb E_\mu[p].
\end{aligned}
$$

Thus

$$
\boxed{S_{\widehat\tau}(\rho\otimes\mu)
=S(\rho)+H(\mu)-\mathbb E_\mu[p].}
$$

The last term is not optional. Calling $H(\mu)$ alone “the clock entropy” hides the contribution produced by the trace weight.

### 2.4 Gaussian clock distribution

For

$$
\mu(p)=\frac{1}{\sqrt{2\pi}\sigma}
\exp\!\left[-\frac{(p-p_0)^2}{2\sigma^2}\right],
$$

we have

$$
H(\mu)=\frac12\log(2\pi e\sigma^2),
\qquad
\mathbb E[p]=p_0.
$$

Therefore

$$
\boxed{S_{\widehat\tau}=S(\rho)
+\frac12\log(2\pi e\sigma^2)-p_0.}
$$

As $\sigma\to0$, the differential entropy tends to $-\infty$. A sharp clock does **not** generate the positive UV area-law divergence of matter entanglement.

### 2.5 Exponential distribution

For $\mu(p)=\kappa e^{-\kappa p}\mathbf1_{p\geq0}$,

$$
H(\mu)=1-\log\kappa,
\qquad
\mathbb E[p]=\frac1\kappa,
$$

and hence

$$
S_{\widehat\tau}=S(\rho)+1-\log\kappa-\frac1\kappa.
$$

This second example makes clear which part is distribution-dependent and which part is structural.

## 3. The exact entropy-difference identity

### 3.1 Derivation in a semifinite algebra

Let $D_\omega$ and $D_\phi$ be faithful normalized densities in the same semifinite algebra, relative to the same trace. Their Umegaki relative entropy is

$$
S(D_\omega\Vert D_\phi)
{}={}
\widehat\tau\!\left[D_\omega(\log D_\omega-\log D_\phi)\right].
$$

Introduce the reference modular Hamiltonian

$$
K_\phi:=-\log D_\phi.
$$

Then

$$
\begin{aligned}
S_{\widehat\tau}(D_\omega)-S_{\widehat\tau}(D_\phi)
&=-\widehat\tau(D_\omega\log D_\omega)
+\widehat\tau(D_\phi\log D_\phi)\\
&=-S(D_\omega\Vert D_\phi)
+\widehat\tau\!\left[(D_\omega-D_\phi)K_\phi\right].
\end{aligned}
$$

Therefore

$$
\boxed{
\Delta S
{}={}
-S(D_\omega\Vert D_\phi)+\Delta\langle K_\phi\rangle.}
$$

This identity is exact whenever the displayed quantities are defined. It is simply the relative-entropy identity written so that the entropy difference is isolated.

### 3.2 Relation to the original type III algebra

The relative entropy in §3.1 is the relative entropy of **two states on the core**. To replace it by the Araki relative entropy $S_{\mathcal M}(\omega\Vert\phi)$ of states on the original type III algebra, one must specify how $\omega$ and $\phi$ are lifted to $\widehat{\mathcal M}$ and prove that the chosen lift preserves the relevant relative entropy.

Witten constructs particular classical-quantum densities directly on the crossed product, while CPW proves the relative-entropy relation needed in its specified semiclassical setup. Neither result says that two arbitrary extensions preserve the relative entropy merely because they restrict to $\omega$ and $\phi$ on $\mathcal M$. We will consequently use the following status labels:

- **Proved:** the semifinite identity of §3.1.
- **Construction-dependent:** identification of the core relative entropy with the Araki relative entropy on $\mathcal M$.
- **Holographic:** identification of $\Delta\langle K_\phi\rangle$ with an area variation.

### 3.3 First law and positivity

For a differentiable family $D(\varepsilon)=D_\phi+\varepsilon\dot D+O(\varepsilon^2)$, relative entropy begins at second order. Hence the linearized identity is

$$
\delta S=\delta\langle K_\phi\rangle.
$$

At finite separation, positivity gives

$$
\Delta S\leq\Delta\langle K_\phi\rangle.
$$

These are, respectively, the first law of entanglement and the relative-entropy form of the Bekenstein bound. Their content is independent of the crossed product; the core supplies a trace-based entropy with which the same relation can be written.

## 4. The coherent-state consistency check

The most useful check is also the simplest. It prevents us from assigning a spurious entropy change to an inner unitary excitation.

### 4.1 Same clock, unitary in the algebra

Let $U\in\widehat{\mathcal M}$ be unitary and let

$$
D_U=UD_0U^*.
$$

Traciality and functional calculus give

$$
\begin{aligned}
S_{\widehat\tau}(D_U)
&=-\widehat\tau\!\left(UD_0U^*\,U(\log D_0)U^*\right)\\
&=-\widehat\tau(D_0\log D_0)
=S_{\widehat\tau}(D_0).
\end{aligned}
$$

Thus an inner conjugation changes the state but not its trace entropy.

### 4.2 Weyl coherent state in a wedge

If $f$ is supported in $W_R$, then $W(f)\in\mathcal A(W_R)$ and $\pi(W(f))\in\widehat{\mathcal A}(W_R)$. Dressing the vacuum and the coherent state with the same clock and the same core identification gives

$$
D_f=\pi(W(f))D_0\pi(W(f))^*,
$$

so

$$
\boxed{S_{\widehat\tau}(D_f)-S_{\widehat\tau}(D_0)=0.}
$$

The two terms on the right-hand side of the entropy-difference identity do not vanish separately. They cancel:

$$
S(D_f\Vert D_0)
{}={}
\widehat\tau\!\left[(D_f-D_0)K_0\right].
$$

For a wedge coherent state this is the familiar statement that the relative entropy equals the increase in vacuum modular energy, because a local unitary does not change the entropy of the state restricted to that algebra.

### 4.3 How to obtain a nonzero difference

A nonzero dressed-entropy difference requires changing something beyond an inner conjugation with a fixed clock. Examples include:

1. two densities not related by a unitary in the algebra;
2. different clock distributions $\mu$;
3. a unitary lying outside the algebra whose entropy is being computed;
4. comparing state-dependent realizations of the core through a nontrivial cocycle identification.

Each case must be stated explicitly. Otherwise the nonzero “relative-entropy term plus boundary term” contradicts unitary invariance.

## 5. Matter UV entropy is separate from clock entropy

### 5.1 The regulated QFT result

The ultraviolet divergence of entanglement entropy comes from short-distance matter correlations across an entangling surface. It is already present before a clock is introduced.

For a $1+1$-dimensional CFT, the vacuum entropy of an interval of length $\ell$ is

$$
S_{\rm matter}(\ell)
{}={}
\frac c3\log\frac{\ell}{\epsilon}+\text{const},
$$

while a half-line with an infrared scale $L$ has the corresponding one-boundary coefficient $c/6$. In $3+1$ dimensions the leading divergence has the form

$$
S_{\rm matter}
{}={}
c_2\frac{A}{\epsilon^2}+\text{subleading terms},
$$

where $c_2$ depends on the regulator. The logarithmic and area divergences are matter-sector statements.

### 5.2 What the crossed product changes

The crossed product supplies a semifinite trace and makes a renormalized entropy of suitable core states meaningful up to one constant. It does not derive the matter area law from the width $\sigma$ of a one-dimensional clock distribution. The two scales have different meanings:

| Quantity | Meaning |
|---|---|
| $\epsilon$ | short-distance regulator of matter modes near the entangling surface |
| $\sigma$ | width of a chosen probability distribution in modular-energy space |

They may become related in a particular gravitational state, but such a relation is additional physics, not a consequence of the continuous-core theorem.

## 6. The gravitational identification

Witten constructs the relevant type II$_\infty$ algebra, trace, and classical-quantum densities, and interprets the additive normalization relative to a reference black-hole entropy. CPW supplies the more explicit generalized-entropy matching: for its class of semiclassical states, the algebraic entropy has the form

$$
S_{\rm alg}
{}={}
\frac{A}{4G_N}+S_{\rm out}+\text{const}
$$

in the stated semiclassical regime. The logical ingredients are:

1. **Operator algebra:** the relevant algebra is a crossed product and therefore carries a semifinite trace.
2. **State construction:** a classical-quantum wavefunction for the energy collective coordinate determines a density in that algebra.
3. **Gravity:** the first law and the bulk equations relate the energy term to the variation of $A/(4G_N)$.
4. **Quantum fields:** relative entropy controls the finite change in $S_{\rm out}$.

Only the first item is a general theorem about every modular crossed product. The remaining items encode the semiclassical black-hole setting. Keeping them separate makes the result stronger, not weaker, because one can see exactly where gravity enters.

## 7. What to take away

- A normal state on the core has a density relative to the semifinite trace, but its entropy need not be finite.
- Under $\widehat\tau\to c\widehat\tau$, every normalized-state entropy shifts by $+\log c$.
- In the exact inner-action Fourier model,

$$
S(\rho\otimes\mu)=S(\rho)+H(\mu)-\mathbb E_\mu[p].
$$

- For two densities in the same semifinite algebra,

$$
\Delta S=-S(D_\omega\Vert D_\phi)+\Delta\langle K_\phi\rangle
$$

is an exact identity.
- Replacing the core relative entropy by Araki relative entropy on the original type III algebra requires a specified, relative-entropy-preserving lift.
- A same-clock coherent excitation implemented by a unitary in the algebra has exactly zero entropy difference; relative entropy and modular energy cancel.
- Clock width is not the matter UV cutoff. In $1+1$ dimensions the matter divergence is logarithmic; in $3+1$ it begins with $A/\epsilon^2$.
- The equality with generalized entropy is a semiclassical-gravity result, not an automatic consequence of adjoining $L^2(\mathbb R)$.

## 8. Looking ahead

Week 15 introduces the finite-dimensional thermofield double and then explains what survives in type III QFT. The key distinction will be the same one used here: a finite-dimensional TFD is a literal vector in a tensor product with density matrices on either side, whereas the vacuum standard form of a wedge algebra is thermofield-like without a Hilbert-space factorization.

## 9. Problem set

**Core problems.**

**1. Trace rescaling.** Starting from $\widehat\tau'=c\widehat\tau$, derive $D'=D/c$ and $S_{\widehat\tau'}=S_{\widehat\tau}+\log c$. Check the result on a one-dimensional example.

**2. Density in the Fourier model.** For $\widehat\omega(a\otimes f)=\operatorname{Tr}(\rho a)\int\mu(p)f(p)dp$, derive $D(p)=\rho\mu(p)e^p$ from the defining Radon–Nikodym relation.

**3. Product entropy.** Compute $-\widehat\tau(D\log D)$ and recover

$$
S_{\widehat\tau}=S(\rho)+H(\mu)-\mathbb E[p].
$$

Explain why dropping the last term changes entropy differences when the mean modular energy changes.

**4. Gaussian and exponential profiles.** Verify the formulas of §§2.4–2.5. For the Gaussian, compute $\partial S/\partial p_0$ and $\partial S/\partial\sigma$. Interpret the signs without invoking a matter cutoff.

**5. Entropy-difference identity.** Starting only from the definitions of entropy and relative entropy, derive §3.1 line by line. State the integrability assumptions required for every term.

**6. Inner-unitary cancellation.** Let $D_U=UDU^*$ with $U$ unitary. Prove $S(D_U)=S(D)$ and then use the entropy-difference identity to show

$$
S(D_U\Vert D)=\widehat\tau[(D_U-D)(-\log D)].
$$

**Starred problems.**

**7\*. Coherent wedge excitation.** Let $U=\pi(W(f))$ for $f$ supported in $W_R$. Prove that a same-clock dressed state is related to the dressed vacuum by inner conjugation. Explain which hypothesis any proposed nonzero same-clock entropy difference would have to violate.

**8\*. Two different lifts.** Construct two product lifts of the same finite-dimensional system state using clock distributions $\mu$ and $\nu$. Compute the entropy difference and show explicitly why the restriction to the original algebra does not determine the core entropy.

**9\*. Matter area law.** Derive the $c/3$ logarithm for a $1+1$ CFT interval from the replica result, or review a standard derivation. Then give a dimensional argument for the leading $A/\epsilon^2$ term in $3+1$ dimensions. Explain why neither follows from $H(\mu)$.

**Project problems.**

**10. Witten source map.** Read Witten §§3.3–3.5. His representation uses multiplication by $X_{\rm W}$, whereas our regular representation uses $\lambda(t)=e^{-itP}$. Derive the operator map $X_{\rm W}=-P$, hence the spectral relation $X_{\rm W}=-p$, and $P_{\rm W}=-i\partial_{X_{\rm W}}=Q$ after the corresponding Fourier/sign change. Then match his $g(X_{\rm W})$, $K$, trace, and density matrix to the course dictionary. Record which formulas are exact in Witten's classical-quantum state construction and which statements in this lecture are the more abstract operator-algebraic version.

**11. CPW source map.** Read CPW §§2.2–3. Identify the formula showing that $\widehat\tau\mapsto e^c\widehat\tau$ shifts entropy by $+c$---equivalently, $\widehat\tau\mapsto c\widehat\tau$ for $c>0$ shifts it by $+\log c$---and locate the independent inputs used to identify algebraic entropy with generalized entropy.

## 10. Instructor checkpoints (internal)

1. $D'=D/c$ and $S'=S+\log c$; in a one-dimensional algebra this follows from normalizing the unique state against the rescaled trace.
2. Comparing the Radon–Nikodym integrands forces $D(p)=\rho\mu(p)e^p$.
3. The three logarithms give $S(\rho)$, $H(\mu)$, and $-\mathbb E[p]$ separately. The last changes whenever the mean changes.
4. Gaussian: $\partial_{p_0}S=-1$, $\partial_\sigma S=1/\sigma$. Exponential: $H=1-\log\kappa$ and $\mathbb E[p]=1/\kappa$.
5. Expand the relative entropy definition and collect $-\log D_\phi$; all traces of unbounded logarithms must be finite or consistently extended-real.
6. Functional calculus plus traciality gives $S(UDU^*)=S(D)$ and hence the exact cancellation identity.
7. For $\operatorname{supp}f\subset W_R$, $\pi(W(f))$ is a unitary in the core. A nonzero answer must change the clock, the algebra/core identification, or the innerness assumption.
8. The two restrictions to $\mathcal M$ agree, while the answer differs by $H(\mu)-H(\nu)-\mathbb E_\mu[p]+\mathbb E_\nu[p]$.
9. The $1+1$ result is logarithmic; transverse cell counting gives $A/\epsilon^2$ in $3+1$. Neither depends on the one-dimensional clock width.
10. Witten's operator map is $X_{\rm W}=-P$ and $P_{\rm W}=Q$; on the $P$-spectrum this becomes $X_{\rm W}=-p$. These statements hold only after Fourier/sign change, and $g(X_{\rm W})$ must not be rewritten as multiplication by $g(q)$.
11. CPW's $+c$ shift is exact for the parameterization $\widehat\tau\mapsto e^c\widehat\tau$ (or $+\log c$ for $\widehat\tau\mapsto c\widehat\tau$); the generalized-entropy equality additionally uses horizon relative entropy, the first law/area response, and relaxation.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block D. Last revised 2026-08-24.*
