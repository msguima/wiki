---
title: "Sem II Week 6 — CPW: The Right Algebra and Its Commutant"
type: lecture-notes
course: syllabus
semester: 2
week: 6
block: 2
duration: "master dossier: 4 hours of material; classroom core: 2-hour seminar + 1-hour office/self-study"
prerequisites: Sem II Wk 5 (TFD modular structure); Sem I Wks 13–15
target_paper: "Chandrasekaran, Penington, Witten, arXiv:2209.10454 §§2.2–2.3"
modified: 2026-08-24
---

# Sem II Week 6 — CPW: The Right Algebra and Its Commutant

> *A two-sided black hole does not require us to place the same clock translation inside two commuting algebras. That construction cannot work: the translation is noncentral and implements modular flow. CPW instead build one right type II$_\infty$ algebra and define the left algebra as its commutant. In the regular representation the commutant contains a **dressed** translation, not the bare right translation. This week derives that statement directly on generators and then matches it to CPW's energy/timeshift variables.*

## 0. Reading

**Primary:**

- CPW, “Large $N$ algebras and generalized entropy,” arXiv:2209.10454, §§2.2–2.3.
- Witten, arXiv:2112.12828, §3.1, especially the construction of commuting left and right algebras.

**Background:**

- Sem I Week 13 and Appendix D.
- Sem II Week 2 for the distinction between the TFD generator and the individual boundary Hamiltonians.

### 0.1 What the student should be able to do

By the end of the week, the student should be able to do four things without relying on a picture of two tensor factors:

1. construct the right crossed product in the regular representation;
2. derive the generators that lie in its commutant;
3. explain why the same bare translation cannot be assigned to both commuting factors;
4. translate, with all signs and units visible, between the course variables and CPW's energy/timeshift variables.

- **Classroom core:** §§1–4 and Problems 1–6. Derive the right core, its commutant, and the CPW dictionary.
- **Full derivation / self-study:** §§5–8 and Problems 7–10. Separate physical time from modular time, verify the exact Rindler realization, and audit the tempting wrong constructions.
- **Research extension:** Problems 11–12, using §§4.1–4.3 as the source-comparison template. Produce either the full CPW commutant note or a bounded-observable Bell bridge.

## 1. Starting data

Let

$$
\mathcal M:=\mathcal A_{R,0}
$$

be the right strict-large-$N$ type III$_1$ factor in the TFD standard representation $(\mathcal H_{\rm TFD},\Omega)$. Assume Haag/TFD duality in this representation:

$$
\mathcal M'=\mathcal A_{L,0}.
$$

The modular operator is

$$
\Delta=e^{-\beta_H\widehat H},
\qquad
\widehat H=H_R-H_L,
$$

where the difference has a large-$N$ limit even though the individual subtracted Hamiltonians need not. The course modular convention is

$$
\sigma_t(a)=\Delta^{-it}a\Delta^{it}.
$$

On $\mathcal M'$ the same modular operator generates the inverse flow:

$$
\sigma_t'(b)=\Delta^{it}b\Delta^{-it}.
$$

Two cautions belong here, before any calculation.

First, $\mathcal H_{\rm TFD}$ denotes the standard Hilbert-space representation selected by the TFD state. The commutant relation $\mathcal M'=\mathcal A_{L,0}$ is the algebraic statement we need; no continuum factorization $\mathcal H_{\rm TFD}=\mathcal H_L\otimes\mathcal H_R$ is being assumed. Second, $\widehat H$ is the well-defined two-sided generator in the limiting representation. Writing it as $H_R-H_L$ records its physical origin, but does not license us to manipulate $H_R$ and $H_L$ separately when those operators fail to survive the limit.

## 2. The right crossed product

### 2.1 Regular representation

Before writing the representation, fix the dictionary. The symbols in the middle column belong to the course convention; the final two CPW symbols will enter only in §4.

| Symbol | Role |
|---|---|
| $t$ | dimensionless modular parameter |
| $u=\beta_Ht$ | physical boundary time in the equilibrium black-hole application |
| $q$ | scalar coordinate of the regular representation |
| $Q$ | multiplication by $q$ |
| $P=-i\partial_q$ | momentum conjugate to $Q$ |
| $p$ | Fourier spectral variable of $P$ |
| $r$ | parameter of the dual action |

In particular, $q$ is not an operator name, $Q$ is not a physical energy, and $p$ is not CPW's timeshift variable. Keeping those three sentences in view prevents most of the sign errors in this week.

On

$$
\widehat{\mathcal H}=\mathcal H_{\rm TFD}\otimes L^2(\mathbb R_q)
$$

define

$$
(\pi_R(a)\xi)(q)=\sigma_{-q}(a)\xi(q),
\qquad
(\lambda(t)\xi)(q)=\xi(q-t).
$$

With $(Q\xi)(q)=q\xi(q)$ and $P=-i\partial_q$,

$$
\lambda(t)=e^{-itP},
\qquad
[Q,P]=i.
$$

Indeed, on $C_c^\infty(\mathbb R_q)$,

$$
[Q,P]\xi(q)
=-iq\xi'(q)+i\frac{d}{dq}\big(q\xi(q)\big)
=i\xi(q).
$$

Exponentiating $P$ gives the translation in the displayed convention:

$$
(e^{-itP}\xi)(q)=\xi(q-t).
$$

This elementary check fixes the sign of every later covariance formula.

The right dressed algebra is

$$
\mathcal N_R
:=
\mathcal M\rtimes_\sigma\mathbb R
{}={}
\{\pi_R(\mathcal M),\lambda(t):t\in\mathbb R\}^{\prime\prime}.
$$

The covariance relation is

$$
\lambda(t)\pi_R(a)\lambda(t)^*=\pi_R(\sigma_t(a)).
$$

To see the relation rather than merely quote it, apply both sides to $\xi$:

$$
\begin{aligned}
(\lambda(t)\pi_R(a)\lambda(t)^*\xi)(q)
&=\sigma_{-(q-t)}(a)\xi(q)\\
&=\sigma_{-q}(\sigma_t(a))\xi(q).
\end{aligned}
$$

Since $\mathcal M$ is type III$_1$, $\mathcal N_R$ is a type II$_\infty$ factor.

> **Status of the type statement.** This is the continuous-core theorem for a type III$_1$ factor. It is not inferred from the displayed representation alone. For a type I algebra, whose modular action is inner, the analogous crossed product is $\mathcal M\bar\otimes L^\infty(\mathbb R)$ and has a centre; the type-III hypothesis is doing the work.

### 2.2 What “one clock” means

There is one auxiliary canonical pair $(Q,P)$ in this representation. This does not mean that both the right algebra and its commutant contain the bare translation $\lambda(t)$. Indeed, if $\lambda(t)$ belonged to both, it would lie in the centre of the factor $\mathcal N_R$, which is impossible for $t\neq0$ because it implements nontrivial modular flow.

The correct question is therefore not “one clock or two clocks?” but:

> How is the same auxiliary canonical pair represented in the right algebra and in its commutant?

## 3. Deriving the left algebra as the commutant

### 3.1 The easy generators

For $b\in\mathcal M'$, let

$$
\pi_L(b):=b\otimes1.
$$

This commutes with $\pi_R(a)$ because $\sigma_{-q}(a)\in\mathcal M$ on every fibre, and it commutes with $\lambda(t)$ because it is independent of $q$. Thus

$$
\pi_L(\mathcal M')\subset\mathcal N_R'.
$$

These generators alone do not exhaust the commutant: $\mathcal N_R'$ must itself be a type II$_\infty$ factor.

### 3.2 The dressed left translation

Define

$$
\rho(t):=\Delta^{it}\otimes\lambda(t).
$$

It commutes with the bare translations because $\lambda(t)$ is an abelian representation of $\mathbb R$. To check commutation with $\pi_R(a)$, act on a vector:

$$
\begin{aligned}
(\rho(t)\pi_R(a)\rho(t)^*\xi)(q)
&=\Delta^{it}\sigma_{-(q-t)}(a)\Delta^{-it}\xi(q)\\
&=\sigma_{-t}(\sigma_{t-q}(a))\xi(q)\\
&=\sigma_{-q}(a)\xi(q)\\
&=(\pi_R(a)\xi)(q).
\end{aligned}
$$

Hence $\rho(t)\in\mathcal N_R'$.

### 3.3 The commutant theorem

The standard commutant theorem for crossed products gives

$$
\boxed{
\mathcal N_L
:=
\mathcal N_R'
{}={}
\{\pi_L(\mathcal M'),\rho(t):t\in\mathbb R\}^{\prime\prime}.}
$$

The left algebra is therefore a crossed-product realization of the commutant with the inverse modular action. It is also a type II$_\infty$ factor.

The generator calculation proves the inclusion from right to left in the boxed formula. Equality is the content of the crossed-product commutant theorem. This distinction is useful in class: checking commutators never proves that one has found the entire commutant. One needs the standard theorem—or an equivalent double-commutant argument using the regular representation—to rule out missing operators.

The decisive distinction is

$$
\lambda(t)\in\mathcal N_R,
\qquad
\rho(t)=\Delta^{it}\otimes\lambda(t)\in\mathcal N_L.
$$

The two group unitaries use the same $L^2(\mathbb R)$ translation, but the left one is dressed by the system modular implementer. This dressing is exactly what makes the algebras commute.

### 3.4 Left covariance

For $b\in\mathcal M'$,

$$
\rho(t)\pi_L(b)\rho(t)^*
{}={}
\Delta^{it}b\Delta^{-it}\otimes1
{}={}
\pi_L(\sigma_t'(b)).
$$

Thus $\rho(t)$ implements the inverse modular flow appropriate to the left side.

## 4. Matching the abstract commutant to CPW

### 4.1 CPW variables

CPW work in a microcanonical large-$N$ scaling in which the renormalized right and left energies have $O(1)$ fluctuations. Their notation is

$$
x=h_L,
\qquad
p_{\rm CPW}=-i\partial_x,
\qquad
[x,p_{\rm CPW}]=i.
$$

Thus $x$ is an **energy multiplication variable**, whereas $p_{\rm CPW}$ is the relative boundary timeshift. Neither is the course variable with the same printed letter. The two-sided QFT generator is $\widehat h$, and CPW identify

$$
h_\Psi:=-\log\Delta=\beta_H\widehat h,
\qquad
\boxed{\beta_Hh_R=\beta_Hx+h_\Psi.}
$$

This is the key relation. The right energy is not a second independent clock observable placed beside $x$: it is the sum of the left energy coordinate and the modular generator. Since energies are unbounded, statements such as “$h_R$ belongs to the algebra” mean that its bounded spectral functions, or equivalently its spectral projections, are affiliated with and generate the von Neumann algebra.

In CPW's asymmetric presentation the two algebras are generated schematically by

$$
\mathcal A_R
=\{\mathcal A_{R,0},h_R\}^{\prime\prime},
$$

and

$$
\mathcal A_L
=\left\{
x,
e^{ip_{\rm CPW}\widehat h}\mathcal A_{L,0}e^{-ip_{\rm CPW}\widehat h}
\right\}^{\prime\prime}.
$$

The notation $\{\mathcal A_{R,0},h_R\}^{\prime\prime}$ is shorthand for generation by $\mathcal A_{R,0}$ and the bounded functional calculus of $h_R$. The same qualification applies to $x$. The left QFT operators are conjugated because an operator dressed to one asymptotic boundary must be shifted by the physical relative timeshift to be dressed to the other boundary.

This is the physical version of the abstract formula

$$
\mathcal N_R'=\{\mathcal M'\otimes1,\Delta^{it}\otimes\lambda(t)\}^{\prime\prime}.
$$

The extra modular factor in $\rho(t)$ is the regular-representation counterpart of CPW's conjugation of left operators by the timeshift and the two-sided generator.

### 4.2 Deriving the source-to-course dictionary

The dictionary is not a verbal analogy; it follows from a unitary change of representation. Set $h_\Psi=-\log\Delta$ and define the decomposable unitary

$$
(U\xi)(q)=e^{iqh_\Psi}\xi(q)=\Delta^{-iq}\xi(q).
$$

It untwists the system algebra:

$$
U\pi_R(a)U^*=a\otimes1.
$$

For the right translation,

$$
U\lambda(t)U^*
=e^{ith_\Psi}\otimes\lambda(t).
$$

After Fourier transforming $q$, the operator $P$ is multiplication by the course variable $p$, so

$$
U\lambda(t)U^*
=e^{it(h_\Psi-p)}.
$$

CPW's right group unitary is $e^{it(h_\Psi+\beta_Hx)}=e^{it\beta_Hh_R}$. Therefore the exact sign-and-scale map is

$$
\boxed{p=-\beta_Hx,\qquad Q=\frac{p_{\rm CPW}}{\beta_H}.}
$$

The second identity follows from $Q=i\partial_p$ in the chosen Fourier convention and $p=-\beta_Hx$. It is now clear why the two symbols called $p$ must never be identified: course $p$ is the Fourier energy coordinate, while $p_{\rm CPW}$ is the conjugate timeshift.

The left generators transform just as cleanly. Since

$$
U\rho(t)U^*=\lambda(t),
$$

their bounded functional calculus becomes the multiplication algebra generated by $x=-p/\beta_H$. Meanwhile

$$
U(b\otimes1)U^*
=e^{iQh_\Psi}b e^{-iQh_\Psi}
=e^{ip_{\rm CPW}\widehat h}b e^{-ip_{\rm CPW}\widehat h},
$$

where $h_\Psi=\beta_H\widehat h$ was used in the last step. This reproduces CPW's left dressing exactly. The regular commutant formula and CPW's asymmetric energy/timeshift formula are therefore unitarily equivalent descriptions of the same pair.

### 4.3 Symmetric and asymmetric presentations

Witten and CPW sometimes use an asymmetric presentation because it makes the right algebra simple and puts the dressing on the left. A unitary conjugation can distribute half of the dressing to each side, producing a symmetric presentation. The two presentations are unitarily equivalent.

This explains why a diagram that writes two bare crossed products side by side is too crude. The pair is determined jointly by

$$
(\mathcal N_R,\mathcal N_L)=(\mathcal N_R,\mathcal N_R').
$$

## 5. Physical time and the modular parameter

The modular parameter $t$ is dimensionless. On the right algebra, physical boundary time is

$$
u=\beta_Ht.
$$

The unitary $\lambda(u/\beta_H)$ implements the right modular automorphism inside $\mathcal N_R$. This statement does not require the individual operator $H_R$ to exist in the strict-large-$N$ TFD representation.

On the left commutant, $\rho(u/\beta_H)$ implements the opposite physical time orientation. The opposite sign is encoded by the commutant modular action, not by putting $\lambda(-t)$ into a second algebra.

## 6. Free-field Rindler realization

Let $\mathcal M=\mathcal A(W_R)$ and assume wedge duality $\mathcal M'=\mathcal A(W_L)$. Bisognano–Wichmann gives

$$
\Delta=e^{-2\pi K_{\rm boost}}.
$$

The right core is

$$
\mathcal N_R
{}={}
\{\pi_R(\mathcal A(W_R)),\lambda(t)\}^{\prime\prime},
$$

and its commutant is

$$
\mathcal N_L
{}={}
\{\mathcal A(W_L)\otimes1,
e^{-i2\pi tK_{\rm boost}}\otimes\lambda(t)
\}^{\prime\prime}.
$$

The sign in the modular factor follows from $\Delta^{it}=e^{-i2\pi tK_{\rm boost}}$. Commutativity is now a generator-level theorem, not an appeal to the claim that the clock is “central.”

### 6.1 Direct generator checks

For $a\in\mathcal A(W_R)$ and $b\in\mathcal A(W_L)$:

$$
[\pi_R(a),b\otimes1]=0,
$$

by wedge duality,

$$
[\lambda(t),b\otimes1]=0,
$$

because $b$ is constant in $q$, and

$$
[\pi_R(a),e^{-i2\pi tK_{\rm boost}}\otimes\lambda(t)]=0
$$

by the calculation in §3.2. These relations generate $[\mathcal N_R,\mathcal N_L]=0$.

### 6.2 What is and is not explicit

The type and commutant are exact. The canonical traces on $\mathcal N_R$ and $\mathcal N_L$ exist abstractly and are unique up to separate scales. We do not use a $\delta_q$ integral kernel for either trace. Semester II Week 7 will compute entropy in the exact inner-action Fourier laboratory and then state CPW's gravitational identification with its hypotheses.

## 7. State independence

If $\Omega_1$ and $\Omega_2$ are faithful standard vectors for $\mathcal M$, their modular actions are cocycle conjugate. Consequently,

$$
\mathcal M\rtimes_{\sigma^{\Omega_1}}\mathbb R
\cong
\mathcal M\rtimes_{\sigma^{\Omega_2}}\mathbb R.
$$

This is the state independence of the continuous core. It should be read as a canonical isomorphism, not literal equality of the represented algebras. Once the right cores are identified, their commutants are identified as well.

The result is what makes perturbation theory possible: the perturbed state can be studied in one algebraic core. However, the cocycle identification may entangle the system and auxiliary variables, so one must not assume that a product clock state remains a product.

## 8. Common wrong constructions

### 8.1 Same bare translation in both algebras

If both alleged commuting algebras contain $\lambda(t)$, then $\lambda(t)$ lies in their intersection. If one is the other's commutant and the right algebra is a factor, that intersection is $\mathbb C1$. But $\lambda(t)$ is not scalar for $t\neq0$. Contradiction.

### 8.2 Calling $\lambda(t)$ central

$\lambda(t)$ satisfies

$$
\lambda(t)\pi_R(a)\lambda(t)^*=\pi_R(\sigma_t(a)),
$$

so it is central only if the flow is trivial. The noncentrality is the point of the crossed product.

### 8.3 Two independent clocks without a physical reason

Two clocks produce a different enlarged system and generally a different constraint structure. Such a construction may be useful in another model, but it is not CPW's one-energy-collective-coordinate algebra and cannot be introduced merely to make commutativity obvious.

## 9. What to take away

- Build the right core $\mathcal N_R=\mathcal M\rtimes_\sigma\mathbb R$ first.
- Define the left dressed algebra as $\mathcal N_L=\mathcal N_R'$.
- In the regular representation,

$$
\mathcal N_L
{}={}
\{\mathcal M'\otimes1,\Delta^{it}\otimes\lambda(t)\}^{\prime\prime}.
$$

- The right contains $\lambda(t)$; the left contains the dressed unitary $\Delta^{it}\otimes\lambda(t)$. They do not both contain the same bare noncentral translation.
- One auxiliary canonical pair can support both algebras because it is embedded differently on the two sides.
- Physical time is $u=\beta_Ht$; the separate $H_R$ and $H_L$ need not exist in the strict-large-$N$ representation.
- The free-field wedge realizes the same commutant construction exactly.

## 10. Looking ahead

Week 7 studies trace entropy on the right type II$_\infty$ algebra and CPW's identification with generalized entropy. The two-sided novelty is not a “joint entropy” on two tensor factors. It is the existence of a right factor and a geometrically meaningful commutant sharing the black-hole collective coordinate.

## 11. Problem set

**Core problems.**

**1. Right covariance.** Verify $\lambda(t)\pi_R(a)\lambda(t)^*=\pi_R(\sigma_t(a))$.

**2. Easy commutant.** Prove $b\otimes1$ commutes with both $\pi_R(a)$ and $\lambda(t)$ for every $b\in\mathcal M'$.

**3. Dressed left translation.** Starting from $\rho(t)=\Delta^{it}\otimes\lambda(t)$, reproduce §3.2 and show that $\rho(t)$ commutes with $\pi_R(a)$ and $\lambda(v)$ for every group parameter $v$. Keep $u=\beta_Ht$ reserved for physical time.

**4. Left covariance.** Show $\rho(t)(b\otimes1)\rho(t)^*=\Delta^{it}b\Delta^{-it}\otimes1$.

**5. Why the bare-clock proposal fails.** Assume $\mathcal N_R$ and $\mathcal N_L=\mathcal N_R'$ both contain $\lambda(t)$. Use factoriality to derive a contradiction.

**6. Rindler signs.** Substitute $\Delta=e^{-2\pi K_{\rm boost}}$ into $\rho(t)$ and verify every sign in §6.

**Starred problems.**

**7\*. Commutant theorem.** Starting from the generator inclusions proved here, consult the crossed-product commutant theorem and identify the step required to establish equality rather than only inclusion.

**8\*. Symmetric presentation.** Let $(V\xi)(q)=\Delta^{-iq/2}\xi(q)$. Conjugate every right and left generator by $V$ and show that the two group unitaries become $\Delta^{-it/2}\otimes\lambda(t)$ and $\Delta^{it/2}\otimes\lambda(t)$. Compare with Witten's symmetric formulas for the two algebras.

**9\*. CPW energy/timeshift dictionary.** Read CPW §2.2. Match their $x$, $p$, and $\widehat h$ to the abstract regular-representation variables, noting that the match involves a Fourier transform and convention-dependent signs.

**10\*. Two-clock countermodel.** On $\mathcal H_{\rm TFD}\otimes L^2(\mathbb R_{q_R})\otimes L^2(\mathbb R_{q_L})$, build the right regular core using only $q_R$ and the left regular core for the inverse commutant action using only $q_L$. Show that the two represented cores commute. Each core is a factor under the III$_1$ hypothesis, but the construction carries two independent dual actions and two canonical pairs. Explain why commutativity alone does not make either represented core the full commutant of the other, and why this is not CPW's one-timeshift system.

**Project problems.**

**11. CPW construction note.** Write a five-page account deriving $\mathcal N_L=\mathcal N_R'$ in both the abstract regular representation and CPW's energy/timeshift representation. The two derivations must meet in an explicit dictionary.

**12. Bell bridge.** Explain which bounded observables from $\mathcal N_R$ and $\mathcal N_L$ could enter a CHSH operator. State why the commutant relation is necessary for locality, and why it does not by itself guarantee Tsirelson saturation in a chosen state.

## 12. Instructor checkpoints (internal)

1. **Right covariance:** the fibre calculation must end with $\sigma_{-q}(\sigma_t(a))$.
2. **Easy commutant:** $b\in\mathcal M'$ commutes with every $\sigma_{-q}(a)\in\mathcal M$, and $b\otimes1$ is independent of $q$.
3. **Dressed translation:** conjugation by $\rho(t)$ gives $\sigma_{-t}\sigma_{t-q}(a)=\sigma_{-q}(a)$; $\rho(t)$ commutes with $\lambda(v)$ because the translation group is abelian and the modular factor acts on the other tensor factor.
4. **Left covariance:** it is exactly $\operatorname{Ad}\Delta^{it}$ on $\mathcal M'$, the inverse of the course right modular action.
5. **Bare-clock failure:** if the same $\lambda(t)$ lies in $\mathcal N_R$ and $\mathcal N_R'$, factoriality makes it scalar; covariance shows it is non-scalar whenever the modular action is nontrivial.
6. **Rindler signs:** $\Delta^{it}=e^{-i2\pi tK_{\rm boost}}$, so the left unitary is $e^{-i2\pi tK_{\rm boost}}\otimes\lambda(t)$.
7. **Commutant theorem:** generator commutation proves only inclusion. Equality is the standard regular crossed-product commutant theorem.
8. **Symmetric presentation:** $V\lambda(t)V^*=\Delta^{-it/2}\lambda(t)$ and $V\rho(t)V^*=\Delta^{it/2}\lambda(t)$.
9. **CPW dictionary:** $h_\Psi=-\log\Delta=\beta_H\widehat h$, $p=-\beta_Hx$, and $p_{\rm CPW}=\beta_HQ$. The source $p_{\rm CPW}$ is a timeshift, not course Fourier momentum.
10. **Two-clock model:** the separate variables make commutativity easy but leave two independent dual shifts and an extra relative-clock sector. A commutant equality is not obtained merely from the inclusion of two commuting cores.
11. **Construction note rubric:** the unitary $U(q)=\Delta^{-iq}$ and the Fourier transform must explicitly turn the regular right generator into $e^{it(h_\Psi-p)}=e^{it\beta_Hh_R}$ and the left generators into CPW's $x$ plus timeshift-dressed $\mathcal A_{L,0}$.
12. **Bell bridge:** use bounded self-adjoint contractions or unitaries in the two commuting factors. The algebraic commutant relation supplies cross-commutativity; the state and chosen observables determine the numerical CHSH value.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 2. Last revised 2026-08-24.*
