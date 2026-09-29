---
title: "Week 13 — The Crossed Product Construction"
type: lecture-notes
course: syllabus
semester: 1
week: 13
block: D
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 4–6 (KMS, Tomita–Takesaki, modular flow), Week 12 (type III$_1$)
modified: 2026-09-29
---

# Week 13 — The Crossed Product Construction

> *Block C closed with a structural problem: local QFT algebras are typically type III$_1$, so they possess neither a trace nor density matrices relative to a trace. The modular crossed product replaces the original algebra by its **continuous core**, a type II$_\infty$ factor carrying a faithful normal semifinite trace. This does not make the type-III entropy finite by decree. It gives us a different, enlarged algebra on which trace-based entropy can be defined when the positive and negative parts are under control; the answer may be finite or extended-real. The core is independent, up to the canonical Connes-cocycle isomorphism, of the faithful state used to construct it. Its interpretation as a gravitationally dressed algebra is an additional physical statement, developed in Semester II.*

## 0. Reading

**Primary:**
- Takesaki, *Theory of Operator Algebras II*, ch. X (crossed products of vN algebras; the operator-algebra foundation).
- Bratteli & Robinson, *Operator Algebras and Quantum Statistical Mechanics* (background on operator-algebraic dynamics and crossed products; use Takesaki for the von Neumann continuous core and dual weights).

**Secondary:**
- Connes, *Noncommutative Geometry*, ch. V §1 (the modular crossed product in Connes' classification).
- Takesaki, *Theory of Operator Algebras II*, ch. X (crossed products, dual weights, and duality).

**Optional research reading:**
- Witten, "Gravity and the crossed product," *JHEP* 10 (2022) 008, arXiv:2112.12828 — the headline paper applying the crossed product to large-$N$ gravity. The Sem II Block 1 reading.
- Liu, "Lectures on entanglement, von Neumann algebras, and emergence of spacetime," arXiv:2510.07017, §V — pedagogical exposition of the crossed product in the holographic context.
- M. Takesaki, "Duality for crossed products and the structure of von Neumann algebras of type III," *Acta Math.* 131 (1973) 249–310 — the original duality theorem and the semifinite structure of the modular crossed product.
- Connes & Takesaki, "The flow of weights on factors of type III," *Tôhoku Math. J.* 29 (1977) 473 — the flow of weights: the centre of the core and the dual action on it, which separate the type-III subclasses.

### 0.1 How to use this master dossier

- **Classroom core:** §§1–2, 3.1–3.2, and 4, with Problems 1 and 3–5. This route builds the regular representation, dual action, canonical trace, and type-promotion theorem.
- **Full derivation / self-study:** §§3.3–3.4 and 5–7, with Problems 2 and 6–8. This route derives the inner-action model, diagnoses the type III$_\lambda$ centre, and keeps the Rindler trace at the correct theorem level.
- **Research extension:** Problems 9–10 and §7.4. This route translates Witten and Liu into the course's seven-symbol convention.

The course convention sheet is Appendix D. When a student changes representation, the scalar coordinate and the operator acting by multiplication must be renamed explicitly before any trace formula is used.

## 1. Why a crossed product?

### 1.1 The structural problem

A type III$_1$ algebra has no trace. The standard quantum-mechanical machinery — represent the state by $\rho$, compute $\mathrm{Tr}(\rho\,O)$ for an observable $O$, compute $S(\rho) = -\mathrm{Tr}(\rho\log\rho)$ for the entropy — does not literally apply. We have:

- **No intrinsic density element.** A normal state on a type-III algebra is a linear functional, but it is not represented by a density element relative to a trace on the algebra itself, because that trace does not exist. In a chosen ambient type-I representation one may still write noncanonical trace-class representatives; they are representation-dependent bookkeeping, not intrinsic density matrices of $\mathcal M$.
- **No von Neumann entropy.** Without a trace, the formula $S(\rho) = -\mathrm{Tr}(\rho\log\rho)$ is undefined.
- **No tracial structure.** Murray–vN comparison of projections has no "size" function; only the partial order.

The Araki–Uhlmann relative entropy $S(\omega\|\phi)$ from Week 7 survives — it does not need a trace — but the *absolute* entropy $S(\omega)$ does not.

### 1.2 The fix

The crossed product is a structural construction that:

1. Takes the original type III algebra $\mathcal{M}$;
2. Picks a one-parameter automorphism group (canonically: the **modular flow** $\sigma^\omega_t$ of a faithful normal state $\omega$);
3. Forms the **crossed product** $\hat{\mathcal{M}} := \mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R}$ on $\mathcal{H} \otimes L^2(\mathbb{R})$;
4. For a type III$_1$ factor, produces a *type II$_\infty$ factor* with a faithful normal semifinite trace.

On the dressed algebra $\hat{\mathcal{M}}$:
- **Normal states have densities** relative to the trace.
- **Trace entropy can be defined** when the corresponding positive and negative parts do not produce an indeterminate $\infty-\infty$; it may be finite or extended-real.
- **The original algebra embeds** as a subalgebra: $\mathcal{M} \subset \hat{\mathcal{M}}$, but as a subalgebra of $\hat{\mathcal{M}}$ alone, $\mathcal{M}$ is still type III. The trace is finite only on the *extended* algebra that includes the modular clock.

The price is an additional $L^2(\mathbb R)$ representation factor. It is useful to call it a clock, but we should remember the logical order: $L^2(\mathbb R)$ first realizes the group action; it becomes a physical clock only when a model identifies its canonical variables with an observer time, an ADM collective coordinate, or another relational degree of freedom.

### 1.3 Physical interpretation

The auxiliary $L^2(\mathbb{R})$ factor is often called the **modular clock**. In Sem II, the crossed-product machinery becomes physical when its canonical variables are related to:

- **An observer's clock** (CLPW de Sitter, where the dressing is by the observer's worldline Hamiltonian);
- **The ADM Hamiltonian** of a gravitational theory (Witten 2022 / CPW eternal black hole);
- **The boost modular flow** of a Rindler wedge (the free-field Bisognano–Wichmann model, used here as an algebraic analogue rather than a gravitational clock).

The crossed-product construction is the *algebraic skeleton* of these physical dressings. The operator-algebraic theorem and the gravitational interpretation are distinct layers: the former is exact, while the latter requires the hypotheses of the physical model.

## 2. Definition

### 2.1 General crossed product

Let $\mathcal{M} \subset \mathcal{B}(\mathcal{H})$ be a von Neumann algebra and let $\alpha : \mathbb{R} \to \mathrm{Aut}(\mathcal{M})$ be a $\sigma$-weakly continuous one-parameter automorphism group. Examples include $\alpha=\sigma^\omega$, the modular flow, and a physical Heisenberg evolution.

Before writing the representation, we fix seven symbols that will remain in force through Semester II:

| Symbol | Meaning |
|---|---|
| $t$ | dimensionless parameter of $\alpha_t$; for modular flow, the KMS inverse temperature is $1$ |
| $u$ | physical time or rapidity, related by $u=\beta t$; for Rindler, $u=2\pi t$ |
| $q$ | scalar coordinate in the regular representation $L^2(\mathbb R_q)$ |
| $Q$ | multiplication by $q$: $(Q\xi)(q)=q\xi(q)$ |
| $P=-i\partial_q$ | momentum conjugate to $Q$, with $[Q,P]=i$ |
| $p$ | Fourier spectral variable of $P$ |
| $r$ | parameter of the dual action $\theta_r$ |

Thus $q$, $Q$, $P$, and $p$ are related, but they are not interchangeable.

**Definition 2.1 (Crossed product).** The **crossed product** $\mathcal{M} \rtimes_\alpha \mathbb{R}$ is the von Neumann algebra on $\mathcal{H} \otimes L^2(\mathbb{R})$ generated by:

- $\pi(a)$ for $a \in \mathcal{M}$, where
$$
(\pi(a)\,\xi)(q) := \alpha_{-q}(a)\,\xi(q), \qquad \xi \in \mathcal{H} \otimes L^2(\mathbb{R}),
$$
i.e., $\pi(a)$ acts on the "fibre at $q$" by the $\alpha_{-q}$-rotated element of $\mathcal{M}$.

- $\lambda(t)$ for $t \in \mathbb{R}$, where
$$
(\lambda(t)\,\xi)(q) := \xi(q-t),
$$
i.e., $\lambda(t)=e^{-itP}$, with $P=-i\partial_q$. Notice that $P$ is the generator of translation; $Q$ is the coordinate operator $(Q\xi)(q)=q\xi(q)$.

**Key commutation relation.** For all $a \in \mathcal{M}$ and $t \in \mathbb{R}$,
$$
\lambda(t)\,\pi(a)\,\lambda(t)^* = \pi(\alpha_t(a)).
$$

**Proof.** $(\lambda(t)\pi(a)\lambda(t)^*\xi)(q)=(\pi(a)\lambda(t)^*\xi)(q-t)=\alpha_{-(q-t)}(a)(\lambda(t)^*\xi)(q-t)=\alpha_{t-q}(a)\xi(q)=\pi(\alpha_t(a))\xi(q)$. $\square$

So the translation $\lambda(t)$ implements $\alpha_t$ as an **inner** automorphism on $\pi(\mathcal{M})$ inside $\mathcal{M} \rtimes_\alpha \mathbb{R}$. The crossed-product algebra contains both $\pi(\mathcal{M})$ and the implementer $\lambda(t)$, so the flow becomes inner inside the larger algebra.

> **Physical picture: relational observables, with a scope warning.** The formula $(\pi(a)\xi)(q)=\alpha_{-q}(a)\xi(q)$ has the form of “the observable $a$ referred to the reading $q$.” In constrained models one can indeed derive a crossed product as a relational observable algebra on a system-plus-clock space. However, that derivation requires a specified constraint and a specified physical clock. The abstract crossed product alone neither proves gravitational dressing nor removes the matter UV divergence. What it proves is sharper: the flow is inner in the enlarged algebra, and the modular core is semifinite.

### 2.2 What it does

The construction has three main effects:

1. **It inner-ifies the flow.** An outer automorphism of $\mathcal{M}$ becomes inner on $\mathcal{M} \rtimes_\alpha \mathbb{R}$. For type III$_1$ algebras, the modular flow is genuinely outer; the crossed product makes it inner on the dressed algebra.

2. **It can change the type.** When $\alpha$ is the modular flow $\sigma^\omega$ on a type III$_1$ algebra, the crossed product is type II$_\infty$. This is **Takesaki's structure theorem** for the continuous core (§4 below). The crossed product **removes the type-III obstruction**.

3. **It adjoins a clock.** The auxiliary $L^2(\mathbb{R})$ factor and the translation operator $\lambda(t)$ together encode a one-parameter group of "clock states." Physical observables in the dressed algebra can be conditioned on the clock reading.

### 2.3 The modular crossed product

When $\alpha = \sigma^\omega$ is specifically the modular flow of a faithful normal state $\omega$, we call $\mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R}$ the **modular crossed product**. This is the canonical case — the choice of state $\omega$ is the only input, and the resulting dressed algebra has the structural properties below.

## 3. The dual action and the trace

### 3.1 The dual action of $\hat{\mathbb{R}}$

The crossed product comes equipped with a canonical second one-parameter group — the **dual action**. For $r \in \mathbb{R}$, define $\theta_r$ on $\mathcal{M} \rtimes_\alpha \mathbb{R}$ by:
$$
\theta_r(\pi(a)) = \pi(a), \qquad \theta_r(\lambda(t)) = e^{itr}\,\lambda(t).
$$

In the ambient algebra on $\mathcal H\otimes L^2(\mathbb R_q)$, $\theta_r$ is implemented by $1\otimes e^{irQ}$. Since $e^{irQ}Pe^{-irQ}=P-r$, it translates the Fourier variable:
$$
\theta_r(f(P))=f(P-r).
$$
It does **not** translate the regular-representation coordinate $Q$. This distinction will prevent the most common sign and representation error in the worked examples.

**Key fact.** The fixed-point algebra of the dual action,
$$
(\mathcal{M} \rtimes_\alpha \mathbb{R})^{\hat{\mathbb{R}}} := \{x \in \mathcal{M} \rtimes_\alpha \mathbb{R} : \theta_r(x) = x \text{ for all } r\},
$$
is exactly $\pi(\mathcal{M})$. **Takesaki duality** (next subsection) extends this observation.

### 3.2 The trace

**Theorem 3.1 (Canonical trace on the continuous core). [Stated only — refs: Takesaki, *Acta Math.* 131 (1973) 249; Takesaki Vol. II ch. X; Connes–Takesaki 1977.]** *Let $\omega$ be a faithful normal state or weight on $\mathcal M$. The continuous core $\widehat{\mathcal M}=\mathcal M\rtimes_{\sigma^\omega}\mathbb R$ is semifinite and carries a faithful normal semifinite trace $\widehat\tau$ satisfying*
$$
\hat\tau \circ \theta_r = e^{-r}\,\hat\tau.
$$

For a compact definition of weights and of faithfulness, normality, and
semifiniteness, see [[functional-analysis-survival-kit|Appendix A §A.5.1]].

In particular, the trace is not dual-invariant. When $\mathcal M$ is a type III$_1$ factor, the core is a type II$_\infty$ factor and its trace is unique up to a positive scalar. For the other type-III subtypes the core has a nontrivial centre, so “unique up to one scalar” is no longer the complete statement.

> **Physical picture.** In the exact Fourier model the dual action shifts the dimensionless auxiliary spectral variable $p$. The measure $e^{-p}dp$ therefore acquires the factor $e^{-r}$ under $p\mapsto p-r$. A physical construction may identify a signed rescaling of this variable with an energy collective coordinate. Changing the trace normalization changes the zero of every trace entropy by the same amount. This is the algebraic origin of the additive constant encountered in gravity, although the crossed product by itself does not identify that constant with an area counterterm.

### 3.3 Explicit formula in the type-I case

The trace formula in general is delicate (involves the Plancherel theorem and the dual-weight construction). In the type-I worked example below, we can write a more explicit form:

**Type-I trace formula.** Let $\mathcal{M} = \mathcal{B}(\mathcal{H})$ with faithful normal state $\omega(\cdot) = \mathrm{Tr}(\rho\,\cdot)$. The modular flow is $\sigma^\omega_t = \mathrm{Ad}(\rho^{-it})$ (Week 5 §5.3). After untwisting the inner action and Fourier transforming the $L^2(\mathbb R_q)$ factor,
$$
\widehat{\mathcal M}\cong\mathcal B(\mathcal H)\bar\otimes L^\infty(\mathbb R_p),
$$
where $p$ is the spectral variable of $P$. On positive simple tensors in the natural trace ideal,
$$
\hat\tau(a \otimes f(P)) = \mathrm{Tr}(a) \int_{-\infty}^\infty f(p)\,e^{-p}\,dp,
$$
where $\mathrm{Tr}$ is the operator trace on $\mathcal{B}(\mathcal H)$. This formula is an exact model of the canonical trace scaling; it is not a diagonal-vector formula in the original $q$-coordinate representation, in which $Q$ acts by multiplication.

This is semifinite, not finite. For example, it is finite on finite-rank positive $a$ and compactly supported positive $f$, but diverges on $1\otimes1$.

The dual action is $\theta_r(a\otimes f(P))=a\otimes f(P-r)$, and one checks
$$
\hat\tau(\theta_r(a \otimes f(P))) = \mathrm{Tr}(a)\int f(p-r)e^{-p}dp=e^{-r}\hat\tau(a\otimes f(P)).
$$
Matches Theorem 3.1.

### 3.4 Why there is no analogous vector formula in type III

For a genuine type III core, the canonical trace is constructed from the dual weight and noncommutative Radon–Nikodym theory. It is tempting to write it as a vector functional of $\Omega\otimes e^{-q/2}$, but $e^{-q/2}\notin L^2(\mathbb R)$ and a formal “regularization” does not turn that expression into a proof. We will therefore use two levels of statement throughout the course:

1. **Type III core:** existence, faithfulness, semifiniteness, and dual scaling are exact abstract theorems.
2. **Inner-action Fourier model:** the weighted integral of §3.3 is an exact computation on a concrete trace ideal.

This separation is didactically important. The model explains the measure and the signs; the theorem supplies the conclusion in the QFT case.

## 4. The type-promotion theorem

### 4.1 Takesaki's theorem and the flow of weights

**Theorem 4.1 (continuous-core structure). [Stated only — refs: Takesaki, *Acta Math.* 131 (1973) 249; Connes & Takesaki, *Tôhoku Math. J.* 29 (1977) 473; Takesaki, Vol. II, chs. X and XII.]** *Let $\mathcal{M}$ be a type III$_1$ factor with faithful normal state $\omega$ and modular flow $\sigma^\omega$. Then $\hat{\mathcal{M}} := \mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R}$ is a type II$_\infty$ factor.*

Equivalently: type III$_1$ + modular flow → type II$_\infty$, structurally. The "obstruction to a trace" is removed by the crossed product.

The two references supply different parts of this statement. Takesaki (1973) proved that the modular crossed product is semifinite, with a trace scaled by the dual action, and proved the duality theorem of §4.2. Connes and Takesaki (1977) studied the restriction of the dual action to the centre of the core, the **flow of weights**; the centre is trivial exactly for type III$_1$, which is the factor statement.

**More generally:** the core of every type III factor is semifinite and of type II. The distinction between the subtypes survives in its centre and in the induced flow of weights. For type III$_1$ the centre is trivial, hence the core is a II$_\infty$ factor. For type III$_\lambda$, $0<\lambda<1$, and type III$_0$, the core has a nontrivial centre and must not be called a factor.

### 4.2 Takesaki duality

Crossing once more by the dual action gives the full Takesaki duality statement:

$$
(\mathcal M\rtimes_{\sigma^\omega}\mathbb R)\rtimes_\theta\mathbb R
\cong
\mathcal M\bar\otimes\mathcal B(L^2(\mathbb R)).
$$

Thus the double crossed product returns a stable amplification of the original algebra. The factor $\mathcal B(L^2(\mathbb R))$ belongs to the **second** crossing; it is not the result of the first crossed product by an inner modular action.

Together with §4.1 this is Takesaki's structure theorem in the form needed here: up to the stabilization in the display, a type III factor is the crossed product of its semifinite core by the trace-scaling dual action. For a hyperfinite type III$_1$ source, the core is the hyperfinite type II$_\infty$ factor. For the other subtypes, the dual action on the centre of the core, the Connes–Takesaki flow of weights, is essential classifying data.

### 4.3 Why this matters

For our course:

- Type III$_1$ algebras (Week 12) admit faithful normal states, but no trace.
- Their crossed products by the modular flow are type II$_\infty$ factors, with a unique-up-to-scaling semifinite trace.
- This permits the definition of **dressed entropy** for states whose trace densities have finite entropy (Week 14), up to a state-independent additive constant.
- In the Witten/CPW setting, the action remains the relevant modular flow, while the added collective coordinate is related physically to ADM energy and its conjugate timeshift. Under additional semiclassical hypotheses, the resulting algebraic entropy matches generalized entropy up to a state-independent constant.

Theorem 4.1 is the **structural backbone of Sem II**.

## 5. Worked example: type-I crossed product

The cleanest non-trivial worked example.

### 5.1 Setup

Let $\mathcal{M} = \mathcal{B}(\mathcal{H})$ with $\dim\mathcal{H} = n < \infty$ for concreteness (the $n = \infty$ case is similar). Let $\omega(a) = \mathrm{Tr}(\rho\,a)$ for a strictly positive density matrix $\rho$ with $\mathrm{Tr}\rho = 1$. The modular flow is
$$
\sigma^\omega_t(a) = \rho^{-it}\,a\,\rho^{it} \qquad (\text{Week 5 §5.3}).
$$
This is **inner** (implemented by $\rho^{-it} \in \mathcal{M}$, which is a unitary in $\mathcal{B}(\mathcal{H})$). For finite-dim type I, the modular flow is always inner, so this is a degenerate case algebraically — but the crossed-product construction still works mechanically and is illuminating.

### 5.2 Constructing the crossed product

On $\mathcal{H} \otimes L^2(\mathbb{R})$, define:
$$
\pi(a) := \int^\oplus \sigma^\omega_{-q}(a)\,dq, \qquad (\pi(a)\xi)(q)=\rho^{iq}a\rho^{-iq}\xi(q),
$$
$$
\lambda(t) := 1 \otimes U_t, \qquad (\lambda(t)\xi)(q)=\xi(q-t).
$$

**Trick: unitary equivalence.** Since the flow is inner, define $V := \int^\oplus \rho^{-iq}\,dq$ — a unitary on $\mathcal{H} \otimes L^2(\mathbb{R}_q)$ that conjugates the modular flow into the trivial flow on the first factor:
$$
V\,\pi(a)\,V^* = a \otimes 1.
$$
And on the translation:
$$
V\,\lambda(t)\,V^* = \rho^{-it} \otimes U_t.
$$
(Verify by direct computation.)

After this unitary transformation, the crossed product is the vN algebra generated by $\{a \otimes 1: a \in \mathcal{B}(\mathcal{H})\}$ and $\{\rho^{-it} \otimes U_t: t \in \mathbb{R}\}$. Taking the WOT-closure:
$$
\mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R} \;\cong\; \mathcal{B}(\mathcal{H}) \otimes L^\infty(\mathbb{R}),
$$
where the second factor is the algebra $L^\infty(\mathbb R_p)$ of bounded functions of the spectral variable $p$ of $P$. The isomorphism uses the Fourier transform, which turns translations in $q$ into multiplication in $p$.

### 5.3 Type

$\mathcal{B}(\mathcal{H}) \otimes L^\infty(\mathbb{R})$ is type I (the tensor product of a type I factor with an abelian vN algebra). For $\dim\mathcal{H}=n$, it is a homogeneous type-I$_n$ algebra with diffuse centre, not a factor.

This is *not* a factor — it has center $1 \otimes L^\infty(\mathbb{R})$. Theorem 4.1 is a statement about type III sources; in the type I case here, the crossed product is a *factor-decomposed* type I algebra, not a single type II$_\infty$ factor. The type promotion happens only when the modular flow is genuinely outer.

### 5.4 Trace

The canonical trace on $\mathcal{B}(\mathcal{H}) \otimes L^\infty(\mathbb{R}_p)$ is the product of the operator trace and the dual-action-scaling measure:
$$
\hat\tau(a \otimes f(P)) = \mathrm{Tr}(a)\,\int_{-\infty}^\infty f(p)\,e^{-p}\,dp.
$$
This is semifinite: finite, for example, for finite-rank positive $a$ and compactly supported positive $f$, and divergent on $1 \otimes 1$.

### 5.5 Lesson

In the type-I case the crossed product just produces a tensor product with $L^\infty(\mathbb{R})$. The type doesn't change in a meaningful way. The content of Theorem 4.1 appears only when the modular flow is **outer**, which is the type III case.

## 6. Worked example: Powers factor (type III$_\lambda$)

The Powers factor $\mathcal{R}_\lambda$ (Week 4 §7) for $\lambda \in (0, 1)$ is type III$_\lambda$. Its modular flow is **outer** (more precisely, the corresponding modular automorphism of the abstract algebra is not inner, even though it can be implemented by unitaries on the GNS Hilbert space — those unitaries are not in $\mathcal{R}_\lambda$).

### 6.1 The crossed product

Form $\widehat{\mathcal R_\lambda}:=\mathcal R_\lambda\rtimes_{\sigma^{\omega_\lambda}}\mathbb R$ on the GNS Hilbert space tensored with $L^2(\mathbb R)$. By Takesaki's structure theorem, this is a semifinite type-II algebra.

### 6.2 Structural form

The dual action $\theta_r$ scales the trace by $e^{-r}$. The fixed-point subalgebra $(\hat{\mathcal{R}_\lambda})^{\hat{\mathbb{R}}}$ is $\pi(\mathcal{R}_\lambda)$, type III$_\lambda$ again.

Unlike the III$_1$ case, $\widehat{\mathcal R_\lambda}$ is not a factor. Its centre carries a periodic flow whose period is $|\log\lambda|$ in the usual normalization. The central decomposition has type II$_\infty$ fibres. This is how the discrete scale $\lambda^{\mathbb Z}$ reappears in the continuous core: the core is semifinite, but the flow of weights remembers the original subtype.

### 6.3 Lesson

The Powers factor gives a concrete model where:
- The original algebra is type III (specifically III$_\lambda$, but the same works for III$_1$ replacing the discrete spectrum with a continuous one).
- The modular flow is outer.
- The crossed product is a genuinely nontrivial semifinite type-II algebra with nontrivial centre; it is not the inner-action tensor-product model.
- The trace is semifinite, well-defined.

For the hyperfinite **type III$_1$** case relevant to local QFT, the centre disappears. The core is then the hyperfinite type II$_\infty$ factor, and its trace is unique up to scaling.

## 7. The free-field Rindler crossed product

The central QFT example is obtained by taking a type III$_1$ wedge algebra and crossing by its boost modular flow. Here the theorem is exact, but the convenient weighted integral of §5 is only a model; the wedge algebra cannot be untwisted as an inner action.

### 7.1 Setup

Let $\mathcal{M} = \mathcal{A}(W_R)$ be the local algebra of the right Rindler wedge in a vacuum QFT satisfying the Bisognano–Wichmann hypotheses. The modular flow is the boost:
$$
\sigma^\omega_t(a) = e^{i\cdot 2\pi tK}\,a\,e^{-i\cdot 2\pi tK}, \qquad K = \text{boost generator}.
$$
(In our convention, with $\sigma_t = \mathrm{Ad}(\Delta^{-it})$ and $\Delta = e^{-2\pi K}$.)

### 7.2 The crossed product

Form $\widehat{\mathcal A}(W_R):=\mathcal A(W_R)\rtimes_{\sigma^\omega}\mathbb R$ on $\mathcal F\otimes L^2(\mathbb R_q)$. The scalar $q$ is the regular-representation coordinate, $Q$ is multiplication by $q$, the automorphism parameter is $t$, and the physical rapidity is $u=2\pi t$.

By Theorem 4.1, $\hat{\mathcal{A}}(W_R)$ is a type II$_\infty$ algebra.

### 7.3 What can be computed explicitly

By Theorem 4.1, $\widehat{\mathcal A}(W_R)$ is a type II$_\infty$ factor and has a canonical trace with $\widehat\tau\circ\theta_r=e^{-r}\widehat\tau$. There is no general formula obtained by inserting distributional vectors $|0_M\rangle\otimes|\delta_q\rangle$ along the $Q$-diagonal. In particular, the multiplier $g(Q)$ used in such a formula need not belong to the crossed product.

What we can compute exactly is the Fourier model of §5, where the auxiliary $P$-spectrum has measure $e^{-p}dp$. For a normalization comparison define $E:=p/(2\pi)$. If a physical model identifies this auxiliary coordinate with a boost-energy collective variable, then, up to the overall Jacobian absorbed in the trace normalization,
$$
e^{-p}dp\propto e^{-2\pi E}dE.
$$
This reproduces the **form** of the Unruh factor without identifying either $E$ with the matter boost generator or $p$ with the coordinate $Q$. Semester II Week 4 will use this exact model as a diagnostic and will keep the genuine type-III trace at the theorem level.

### 7.4 Why this is the workhorse

This explicit free-field Rindler crossed product is the model used in:

- **Witten 2022** (Sem II Block 1): the modular crossed product of the strict-large-$N$ exterior algebra, with its collective variable identified with the black-hole energy sector.
- **CPW 2022** (Sem II Block 2): a right crossed product together with its dressed commutant for the eternal black hole; the well-defined two-sided generator is $H_R-H_L$, while $H_R$ and $H_L$ separately do not survive the same limit as operators.
- **Ahmad–Jefferson 2025** (Sem II Block 4): unitary transport of an algebra–state system, with the crossed-product weight and spectral Jacobian expanded by BCH. The Connes cocycle of Week 7 is a useful fixed-algebra comparison, not AAJ's expansion parameter.

In each case, the free-field wedge supplies the exact modular action and the exact type of the core. Trace calculations are explicit only after choosing a controlled model or a specified class of lifted states. This distinction will be maintained in Week 14 and Semester II.

## 8. What to take away

- **Definition and covariance check:** the crossed product $\mathcal{M} \rtimes_\alpha \mathbb{R}$ is the von Neumann algebra on $\mathcal{H} \otimes L^2(\mathbb{R})$ generated by $\pi(a)$ (fiberwise action by $\alpha_{-q}$) and $\lambda(t)$ (translation), with $\lambda(t)\pi(a)\lambda(t)^*=\pi(\alpha_t(a))$.
- **Stated only (Theorem 4.1; Takesaki 1973, Connes–Takesaki 1977):** for a type III$_1$ factor $\mathcal{M}$ with modular flow $\sigma^\omega$, the crossed product $\hat{\mathcal{M}}$ is a type II$_\infty$ factor with a faithful normal semifinite trace, unique up to scaling.
- **Stated only (Theorem 3.1):** the dual action $\theta_r$ of $\hat{\mathbb{R}}$ on $\hat{\mathcal{M}}$ scales the trace: $\hat\tau \circ \theta_r = e^{-r}\hat\tau$.
- **Worked (type I):** crossed product of $\mathcal{B}(\mathcal{H})$ by inner modular flow is $\mathcal{B}(\mathcal{H}) \otimes L^\infty(\mathbb{R})$. The type doesn't promote — type promotion happens only for outer flows.
- **Subtype warning:** the core of a III$_\lambda$ factor with $\lambda<1$ has nontrivial centre; only III$_1$ gives a factor.
- **The Semester II workhorse:** $\mathcal{A}(W_R)\rtimes_{\mathrm{boost}}\mathbb R$ is an exact type II$_\infty$ core. Its trace is known abstractly; $e^{-2\pi E}dE$ is an exact Fourier-model diagnostic, not a distributional diagonal formula on the type-III core.

## 9. Looking ahead

Week 14 defines trace entropy on the type II$_\infty$ core. We first prove the exact semifinite identity “entropy difference = minus relative entropy plus modular-energy difference.” We then state the additional hypothesis required to identify the relative entropy of lifted core states with the Araki relative entropy on the original type III algebra. Finally, we test all signs in the exact inner-action Fourier model.

## 10. Problem set

**Core problems.**

**1. Verify the crossed-product commutation relation.** For the abstract crossed product $\mathcal{M} \rtimes_\alpha \mathbb{R}$, compute $\lambda(t)\,\pi(a)\,\lambda(t)^*$ explicitly using the definitions of $\pi(a)$ and $\lambda(t)$ in §2.1, and verify $\lambda(t)\pi(a)\lambda(t)^* = \pi(\alpha_t(a))$.

**2. Crossed product of $M_2(\mathbb{C})$ by an inner flow.** Let $\mathcal{M} = M_2(\mathbb{C})$, $\rho = \mathrm{diag}(\eta, 1-\eta)$ with $\eta \in (0, 1)$, $\sigma_t = \mathrm{Ad}(\rho^{-it})$. Construct $\mathcal{M} \rtimes_\sigma \mathbb{R}$ explicitly on $\mathbb{C}^2 \otimes L^2(\mathbb{R})$. Use the unitary $V$ of §5.2 to identify the result as $M_2(\mathbb{C}) \otimes L^\infty(\mathbb{R})$.

**3. Trace-scaling by the dual action.** In the Fourier model $\widehat{\mathcal M}=\mathcal B(\mathcal H)\bar\otimes L^\infty(\mathbb R_p)$, take finite-rank $a\geq0$ and compactly supported $f\geq0$. Starting from $\theta_r(f(P))=f(P-r)$, verify $\widehat\tau\circ\theta_r=e^{-r}\widehat\tau$. State explicitly where the change of variables is made.

**4. The original algebra inside the crossed product.** On finite Fourier sums $x=\int \pi(a_t)\lambda(t)dt$, verify that dual invariance eliminates every nonzero Fourier mode. Use the standard density theorem for crossed products to conclude, as a stated final step, that $(\mathcal M\rtimes_\alpha\mathbb R)^\theta=\pi(\mathcal M)$.

**5. Inner-ification.** Show that the automorphism $\alpha_t$ on $\mathcal{M}$, lifted to $\pi(\alpha_t(\cdot))$ on $\pi(\mathcal{M}) \subset \mathcal{M} \rtimes_\alpha \mathbb{R}$, is **inner** in the larger algebra — implemented by the unitary $\lambda(t)$. Why is this useful when $\alpha$ is outer on $\mathcal{M}$ alone?

**Starred problems.**

**6\*. Core of the Powers factor.** For $\lambda\in(0,1)$, explain why $\mathcal R_\lambda\rtimes_{\sigma^{\omega_\lambda}}\mathbb R$ cannot be a factor. Identify the period $|\log\lambda|$ of the flow on its centre and contrast this with the trivial centre of the III$_1$ core.

**7\*. Trace uniqueness.** Let $\mathcal M$ be a type III$_1$ factor. Use the uniqueness of a faithful normal semifinite trace on a type II$_\infty$ factor, up to a positive scalar, to prove uniqueness for its core. Explain why the same one-scalar argument does not apply to the nonfactor core of III$_\lambda$, $\lambda<1$.

**8\*. Rindler normalization dictionary.** Construct $\mathcal A(W_R)\rtimes_{\sigma^\omega}\mathbb R$ in the regular representation and write $q,Q,P,t,u=2\pi t,p$, and $r$ beside their definitions. In the **separate** inner-action Fourier model, define $E=p/(2\pi)$ and derive $e^{-p}dp\propto e^{-2\pi E}dE$. Explain why this comparison neither identifies $p$ with the matter boost generator nor licenses a $\delta_q$ diagonal formula for the trace of the genuine type-III core.

**Project problems.**

**9. Reading bridge.** Read Witten 2022 §§3.2–3.5. His presentation is already Fourier transformed relative to our regular representation: compare $e^{itX_{\rm W}}$ with $\lambda(t)=e^{-itP}$ to obtain the operator map $X_{\rm W}=-P$, hence the spectral relation $X_{\rm W}=-p$, and then show that $P_{\rm W}=-i\partial_{X_{\rm W}}$ corresponds to $Q=i\partial_p$. Locate his trace formula in §3.4 and entropy formula in §3.5. Record every sign change required by the course convention, and explain why $X_{\rm W}$ must not simultaneously be identified with our regular coordinate $q$.

**10. Liu lectures preview.** Read Liu §V (the lectures, arXiv:2510.07017). Compare Liu's pedagogical exposition of the crossed product with this lecture. Identify any places where the conventions differ.

## 11. Instructor checkpoints (internal)

1. The shift convention gives $\alpha_{-(q-t)}=\alpha_{-q}\alpha_t$.
2. $V(q)=\rho^{-iq}$ makes $\pi(a)$ constant and sends $\lambda(t)$ to $\rho^{-it}\lambda(t)$; since $\rho^{it}$ is already in $M_2$, the generated group algebra is $L^\infty(\mathbb R_p)$ after Fourier transform.
3. The substitution $p'=p-r$ produces $e^{-r}$; using $q$ as the dummy Fourier variable should be avoided.
4. Dual invariance kills every $t\neq0$ Fourier mode. Extending from the analytic/Fourier core to the von Neumann algebra uses the standard density theorem.
5. $\lambda(t)$ implements $\pi\circ\alpha_t$ by inner conjugation in the crossed product even when no implementing unitary lies in $\mathcal M$.
6. For III$_\lambda$, $0<\lambda<1$, the flow of weights on the core centre has period $|\log\lambda|$ in the usual modular normalization; hence the core is not a factor.
7. A II$_\infty$ factor has its faithful normal semifinite trace unique up to one positive scalar. A nonfactor core permits central reweighting, so one scalar is insufficient.
8. The expected list is $t,u,q,Q,P,p,r$; the $e^{-2\pi E}$ expression is only the rescaled inner-action Fourier measure.
9. As operators, $X_{\rm W}=-P$ and $P_{\rm W}=Q$; in the $P$-spectral representation this reads $X_{\rm W}=-p$. Witten's trace is evaluated on his analytic trace domain, not on a $\delta_q$ diagonal.
10. Accept convention differences only when the student supplies an explicit map; in particular, Liu's source notation must not overwrite the course meanings of $q,p,t,r$.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block D. Last revised 2026-09-29.*
