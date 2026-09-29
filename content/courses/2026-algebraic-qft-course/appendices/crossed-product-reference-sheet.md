---
title: "Appendix D — Crossed-Product Reference Sheet"
type: appendix
course: syllabus
modified: 2026-08-24
---

# Crossed-Product Reference Sheet

This sheet fixes the notation used in Weeks 13–15 and throughout Semester II. The point of the notation is not cosmetic: the regular-representation coordinate, its conjugate momentum, modular time, physical time, and the parameter of the dual action play different roles.

## D.1 Seven symbols that must not be conflated

| Symbol | Meaning | Where it appears |
|---|---|---|
| $t$ | dimensionless parameter of the automorphism $\alpha_t$; for a modular crossed product, $\alpha_t=\sigma_t^\omega$ | $\lambda(t)$ and the covariance relation |
| $u$ | physical time or rapidity | $u=\beta t$; for a Rindler wedge, $u=2\pi t$ |
| $q$ | scalar coordinate in the regular representation | argument of $\xi(q)$ in $L^2(\mathbb R_q)$ |
| $Q$ | multiplication by $q$: $(Q\xi)(q)=q\xi(q)$ | implementation of the dual action in the ambient algebra |
| $P$ | momentum conjugate to $Q$: $P=-i\partial_q$, $[Q,P]=i$ | generator of $\lambda(t)=e^{-itP}$ |
| $p$ | Fourier spectral variable of $P$ | multiplication variable after Fourier transform; the trace model uses $e^{-p}dp$ |
| $r$ | parameter of the dual action $\theta_r$ | $\theta_r(\lambda(t))=e^{itr}\lambda(t)$ |

Thus $q$ is a scalar coordinate and $Q$ is the operator that multiplies by it, while $p$ is the Fourier-dual scalar variable and $P$ is the operator whose spectral value is $p$. A function $g(Q)$ is multiplication by $g(q)$; a function $f(P)$ becomes multiplication by $f(p)$ only after Fourier transform. They are not interchangeable.

## D.2 Setup and regular representation

Let $\mathcal M\subset\mathcal B(\mathcal H)$ be a von Neumann algebra and let $\alpha:\mathbb R\to\operatorname{Aut}(\mathcal M)$ be a $\sigma$-weakly continuous action. On $\mathcal H\otimes L^2(\mathbb R_q)$ define

$$
(\pi_\alpha(a)\xi)(q)=\alpha_{-q}(a)\xi(q),
\qquad
(\lambda(t)\xi)(q)=\xi(q-t).
$$

Since $P=-i\partial_q$, the second formula is $\lambda(t)=e^{-itP}$. The crossed product is

$$
\mathcal M\rtimes_\alpha\mathbb R
:=
\{\pi_\alpha(\mathcal M),\lambda(t):t\in\mathbb R\}^{\prime\prime}.
$$

The defining covariance relation is

$$
\lambda(t)\pi_\alpha(a)\lambda(t)^*
{}={}
\pi_\alpha(\alpha_t(a)).
$$

This relation says precisely that the action becomes inner after passing to the crossed product. Calling $q$ a physical clock reading is an additional interpretation, appropriate only when the physical construction supplies such a clock or relational degree of freedom.

## D.3 The dual action

The dual action $\theta:\mathbb R\to\operatorname{Aut}(\mathcal M\rtimes_\alpha\mathbb R)$ is fixed by

$$
\theta_r(\pi_\alpha(a))=\pi_\alpha(a),
\qquad
\theta_r(\lambda(t))=e^{itr}\lambda(t).
$$

In the regular representation it is implemented in the ambient algebra by $1\otimes e^{irQ}$. Since

$$
e^{irQ}Pe^{-irQ}=P-r,
$$

the same action is a translation of the Fourier variable:

$$
\theta_r(f(P))=f(P-r).
$$

The fixed-point algebra is

$$
(\mathcal M\rtimes_\alpha\mathbb R)^\theta=\pi_\alpha(\mathcal M).
$$

## D.4 Modular crossed product and continuous core

For a faithful normal state or weight $\omega$, the course convention is

$$
\sigma_t^\omega(a)=\Delta_\omega^{-it}a\Delta_\omega^{it}.
$$

The modular crossed product

$$
c_\omega(\mathcal M):=\mathcal M\rtimes_{\sigma^\omega}\mathbb R
$$

is called the continuous core. Cores obtained from two faithful normal weights are canonically isomorphic up to the Connes-cocycle identification. This state independence concerns the algebra up to canonical isomorphism; a particular realization and a particular lifted state still depend on choices.

## D.5 Type and centre of the core

The continuous core is semifinite. The factor statement requires care:

- If $\mathcal M$ is a type III$_1$ factor, $c_\omega(\mathcal M)$ is a type II$_\infty$ factor.
- If $\mathcal M$ is type III$_\lambda$ with $0\leq\lambda<1$, its core is a semifinite type-II algebra with a nontrivial centre. The induced action on that centre is the flow of weights. It is therefore incorrect to call the whole core a factor in these cases.
- If $\mathcal M$ is semifinite, every modular automorphism group is inner. Crossing by that inner action gives

$$
\mathcal M\rtimes_{\sigma^\omega}\mathbb R
\cong
\mathcal M\,\bar\otimes\,L^\infty(\mathbb R),
$$

not $\mathcal M\bar\otimes\mathcal B(L^2(\mathbb R))$. The latter algebra appears after crossing once more by the dual action.

For a hyperfinite type III$_1$ source, the core is the hyperfinite type II$_\infty$ factor.

## D.6 Canonical trace and its scaling

The continuous core has a faithful normal semifinite trace $\widehat\tau$ satisfying the course normalization

$$
\boxed{\widehat\tau\circ\theta_r=e^{-r}\widehat\tau.}
$$

For a type II$_\infty$ factor this trace is unique up to a positive multiplicative constant. The formula is an abstract theorem; in a general type III representation the trace is not a vector functional of a non-normalizable vector such as $\Omega\otimes e^{-q/2}$.

## D.7 Exact inner-action Fourier model

Let $\mathcal M=\mathcal B(\mathcal H)$ and $\omega(a)=\operatorname{Tr}(\rho a)$ with $\rho>0$. Since

$$
\sigma_t^\omega(a)=\rho^{-it}a\rho^{it}
$$

is inner, an untwisting unitary followed by Fourier transform gives

$$
\mathcal M\rtimes_{\sigma^\omega}\mathbb R
\cong
\mathcal B(\mathcal H)\bar\otimes L^\infty(\mathbb R_p).
$$

Here $p$ is the spectral variable of $P$, not the original coordinate $q$. On positive simple tensors in its natural trace ideal,

$$
\boxed{
\widehat\tau(a\otimes f(P))
{}={}
\operatorname{Tr}(a)\int_{\mathbb R}f(p)e^{-p}\,dp .}
$$

Because $\theta_r(f(P))=f(P-r)$,

$$
\widehat\tau(\theta_r(a\otimes f(P)))
{}={}
\operatorname{Tr}(a)\int f(p-r)e^{-p}dp
{}={}
e^{-r}\widehat\tau(a\otimes f(P)).
$$

Compactly supported positive $f$ and finite-rank positive $a$ give a concrete $\widehat\tau$-finite core. Notice that a generic $g(Q)$ is not an element of the abelian factor $L^\infty(P)$ in this model.

For a normalization comparison one may define $E:=p/\beta$, after which the same weight is $e^{-\beta E}dE$ up to an overall constant. Calling $E$ a **physical** energy requires a further model-dependent identification. For Rindler flow $u=2\pi t$, the comparison weight is $e^{-2\pi E}dE$. The factor $2\pi$ comes from rescaling the spectral variable, not from replacing the coordinate $Q$ by modular time or from proving that $E$ is the matter boost generator.

## D.8 Product-state density and entropy in the exact model

Let $\rho$ be a density matrix on $\mathcal H$ and let $\mu(p)dp$ be a probability distribution with the required integrability. The product state

$$
\widehat\omega(a\otimes f)=\operatorname{Tr}(\rho a)\int\mu(p)f(p)dp
$$

has density, relative to $\widehat\tau$,

$$
D_{\widehat\omega}(p)=\rho\,\mu(p)e^p.
$$

Consequently,

$$
\boxed{
S_{\widehat\tau}(\widehat\omega)
{}={}
S(\rho)+H(\mu)-\mathbb E_\mu[p],}
$$

where

$$
H(\mu)=-\int\mu(p)\log\mu(p)dp.
$$

The last term is part of the entropy. It cannot be discarded or renamed as a normalization constant when the mean of $p$ changes from state to state.

## D.9 Trace rescaling

If $\widehat\tau'=c\widehat\tau$, the density of a fixed normalized state becomes $D'=D/c$. Therefore

$$
S_{\widehat\tau'}(D')
{}={}
-c\widehat\tau\!\left(\frac Dc\log\frac Dc\right)
{}={}
S_{\widehat\tau}(D)+\log c.
$$

Thus trace rescaling shifts every normalized-state entropy by $+\log c$. Entropy differences computed with the same trace normalization are unchanged.

## D.10 Entropy-difference identity: exact scope

For two faithful densities $D_\omega,D_\phi$ in the same semifinite algebra with the same trace, whenever the displayed terms are well defined (or after a stated common regularization),

$$
S(D_\omega\Vert D_\phi)
{}={}
\widehat\tau\!\left[D_\omega(\log D_\omega-\log D_\phi)\right].
$$

Writing $K_\phi=-\log D_\phi$ gives the exact identity

$$
\boxed{
S_{\widehat\tau}(D_\omega)-S_{\widehat\tau}(D_\phi)
{}={}
-S(D_\omega\Vert D_\phi)
+\widehat\tau\!\left[(D_\omega-D_\phi)K_\phi\right].}
$$

This is the precise semifinite version of “minus relative entropy plus modular-energy difference.” To replace the relative entropy on the right by the Araki relative entropy of two states on the original type III algebra, one must specify a lift to the core that preserves that relative entropy. It is not a statement about arbitrary pairs of extensions.

## D.11 Inner-unitary check

If $D_\omega=UD_\phi U^*$ for a unitary $U$ in the same semifinite algebra, then traciality implies

$$
S_{\widehat\tau}(D_\omega)=S_{\widehat\tau}(D_\phi).
$$

The entropy-difference identity therefore yields an exact cancellation,

$$
S(D_\omega\Vert D_\phi)
{}={}
\widehat\tau\!\left[(D_\omega-D_\phi)K_\phi\right].
$$

This is the correct consistency check for a Weyl coherent excitation implemented by a unitary belonging to the algebra and dressed with the same clock. A nonzero entropy difference requires a different comparison: for example, a non-inner excitation relative to the chosen algebra, a changed clock distribution, or a state-dependent identification of two cores.

## D.12 Takesaki duality

The full duality statement is

$$
(\mathcal M\rtimes_\alpha\mathbb R)\rtimes_\theta\mathbb R
\cong
\mathcal M\bar\otimes\mathcal B(L^2(\mathbb R)).
$$

The second tensor factor is the stabilization produced by the second crossing. It should not be inserted into the first crossed product of an inner action.

## D.13 Common pitfalls

1. $Q$ and $P$ are conjugate operators, not two names for the same clock observable.
2. The dual action is a phase on $\lambda(t)$, or equivalently a translation of the $P$-spectrum. It is not a translation of $Q$ in the regular representation.
3. The weighted integral $e^{-p}dp$ belongs to the Fourier variable in the exact inner-action model. A formal $\delta_q$ diagonal is not a proof of the trace formula for a type III core.
4. For a type III factor, the continuous core is a factor precisely in the type III$_1$ case relevant here; III$_0$ and III$_\lambda$, $0<\lambda<1$, retain a nontrivial centre.
5. The crossed product is an algebraic construction. Its identification with a gravitationally dressed algebra requires the physical hypotheses of Witten, CPW, CLPW, or the relevant model.
6. Clock width and the matter UV cutoff are independent. In $1+1$ dimensions matter entanglement is logarithmic; in $3+1$ dimensions its leading divergence is proportional to $A/\epsilon^2$.
7. Under $\widehat\tau\to c\widehat\tau$, entropy shifts by $+\log c$.

## D.14 Use in the course

| Week | Main use |
|---|---|
| 13 | Definition, dual action, core, exact inner-action Fourier model |
| 14 | Semifinite entropy, product-state formula, entropy-difference identity |
| 15 | One-sided modular standard form and the TFD analogy |
| Sem II 2–4 | Witten construction, with physical variables matched to the abstract dictionary |
| Sem II 6–7 | CPW right algebra and its commutant; generalized entropy |
| Sem II 10–13 | Structural synthesis and perturbations |

---

*Reference sheet for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]]. Last revised 2026-08-24.*
