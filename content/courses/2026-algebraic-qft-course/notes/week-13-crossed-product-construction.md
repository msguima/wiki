---
title: "Week 13 — The Crossed Product Construction"
type: lecture-notes
course: syllabus
semester: 1
week: 13
block: D
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 4–6 (KMS, Tomita–Takesaki, modular flow), Week 12 (type III$_1$)
modified: 2026-06-11
---

# Week 13 — The Crossed Product Construction

> *Block C closed with a structural problem: the local algebras of QFT are type III$_1$, and there is no trace, no density matrix, no von Neumann entropy. Algebraic QFT has the right framework for asking thermal questions (Araki–Uhlmann relative entropy), but the basic notions of finite-dim quantum mechanics — $\rho$, $S(\rho) = -\mathrm{Tr}(\rho\log\rho)$ — are gone. The **crossed product** is the structural fix: adjoin a "modular clock" to the algebra, and the dressed algebra is type II$_\infty$ with a faithful normal semifinite trace. The fix is canonical; it depends only on the algebra-state pair. This is the algebraic content of "gravity dresses the local algebra" — the same construction that drives Witten 2022 and the rest of Sem II.*

## 0. Reading

**Primary:**
- Takesaki, *Theory of Operator Algebras II*, ch. X (crossed products of vN algebras; the operator-algebra foundation).
- Bratteli & Robinson, Vol. I, §2.7 (crossed products and dual weights; clean physics-friendly treatment).

**Secondary:**
- Connes, *Noncommutative Geometry*, ch. V §1 (the modular crossed product in Connes' classification).
- Takesaki, *Theory of Operator Algebras III*, §VIII.3 (Takesaki duality and structure theorems).

**Optional research reading:**
- Witten, "Gravity and the crossed product," *JHEP* 10 (2022) 008, arXiv:2112.12828 — the headline paper applying the crossed product to large-$N$ gravity. The Sem II Block 1 reading.
- Liu, "Lectures on entanglement, von Neumann algebras, and emergence of spacetime," arXiv:2510.07017, §5 — pedagogical exposition of the crossed product in the holographic context.
- Connes & Takesaki, "The flow of weights on factors of type III," *Tôhoku Math. J.* 29 (1977) 473 — the original duality theorem.

## 1. Why a crossed product?

### 1.1 The structural problem

A type III$_1$ algebra has no trace. The standard quantum-mechanical machinery — represent the state by $\rho$, compute $\mathrm{Tr}(\rho\,O)$ for an observable $O$, compute $S(\rho) = -\mathrm{Tr}(\rho\log\rho)$ for the entropy — does not literally apply. We have:

- **No density matrices.** States are linear functionals; they have no "diagonal matrix elements" in the trace-class sense.
- **No von Neumann entropy.** Without a trace, the formula $S(\rho) = -\mathrm{Tr}(\rho\log\rho)$ is undefined.
- **No tracial structure.** Murray–vN comparison of projections has no "size" function; only the partial order.

The Araki–Uhlmann relative entropy $S(\omega\|\phi)$ from Week 7 survives — it does not need a trace — but the *absolute* entropy $S(\omega)$ does not.

### 1.2 The fix

The crossed product is a structural construction that:

1. Takes the original type III algebra $\mathcal{M}$;
2. Picks a one-parameter automorphism group (canonically: the **modular flow** $\sigma^\omega_t$ of a faithful normal state $\omega$);
3. Forms the **crossed product** $\hat{\mathcal{M}} := \mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R}$ on $\mathcal{H} \otimes L^2(\mathbb{R})$;
4. Produces a *type II$_\infty$* algebra with a *faithful normal semifinite trace*.

On the dressed algebra $\hat{\mathcal{M}}$:
- **Density matrices exist** (relative to the trace).
- **Von Neumann entropy is defined**, up to a state-independent additive constant.
- **The original algebra embeds** as a subalgebra: $\mathcal{M} \subset \hat{\mathcal{M}}$, but as a subalgebra of $\hat{\mathcal{M}}$ alone, $\mathcal{M}$ is still type III. The trace is finite only on the *extended* algebra that includes the modular clock.

The price: we have added a "fictitious" or "auxiliary" degree of freedom — an $L^2(\mathbb{R})$ Hilbert space carrying the modular flow as a translation. Algebraically this is the price for restoring trace-based methods.

### 1.3 Physical interpretation

The auxiliary $L^2(\mathbb{R})$ factor is the **modular clock**. In Sem II, the crossed-product machinery becomes physical when this clock is identified with:

- **An observer's clock** (CLPW de Sitter, where the dressing is by the observer's worldline Hamiltonian);
- **The ADM Hamiltonian** of a gravitational theory (Witten 2022 / CPW eternal black hole);
- **The boost generator** of a Rindler observer (the free-field Bisognano–Wichmann model).

The crossed-product construction is the *algebraic skeleton* of all these physical dressings. They differ in *which one-parameter group* is dressed, not in the structural construction.

## 2. Definition

### 2.1 General crossed product

Let $\mathcal{M} \subset \mathcal{B}(\mathcal{H})$ be a von Neumann algebra and let $\alpha : \mathbb{R} \to \mathrm{Aut}(\mathcal{M})$ be a $\sigma$-weakly continuous one-parameter automorphism group. (Examples: $\alpha = \sigma^\omega$ the modular flow, or $\alpha$ = a physical Heisenberg evolution.)

**Definition 2.1 (Crossed product).** The **crossed product** $\mathcal{M} \rtimes_\alpha \mathbb{R}$ is the von Neumann algebra on $\mathcal{H} \otimes L^2(\mathbb{R})$ generated by:

- $\pi(a)$ for $a \in \mathcal{M}$, where
$$
(\pi(a)\,\xi)(s) := \alpha_{-s}(a)\,\xi(s), \qquad \xi \in \mathcal{H} \otimes L^2(\mathbb{R}),
$$
i.e., $\pi(a)$ acts on the "fibre at $s$" by the $\alpha_{-s}$-rotated element of $\mathcal{M}$.

- $\lambda(t)$ for $t \in \mathbb{R}$, where
$$
(\lambda(t)\,\xi)(s) := \xi(s - t),
$$
i.e., $\lambda(t) = 1 \otimes U_t$ where $U_t$ is the translation operator on $L^2(\mathbb{R})$.

**Key commutation relation.** For all $a \in \mathcal{M}$ and $t \in \mathbb{R}$,
$$
\lambda(t)\,\pi(a)\,\lambda(t)^* = \pi(\alpha_t(a)).
$$

**Proof.** $(\lambda(t)\pi(a)\lambda(t)^*\xi)(s) = (\pi(a)\lambda(t)^*\xi)(s - t) = \alpha_{-(s-t)}(a)(\lambda(t)^*\xi)(s-t) = \alpha_{t-s}(a)\,\xi(s) = \pi(\alpha_t(a))\xi(s)$. $\square$

So the translation $\lambda(t)$ implements $\alpha_t$ as an **inner** automorphism on $\pi(\mathcal{M})$ inside $\mathcal{M} \rtimes_\alpha \mathbb{R}$. The crossed-product algebra contains both $\pi(\mathcal{M})$ and the implementer $\lambda(t)$, so the flow becomes inner inside the larger algebra.

> **Physical picture: relational (dressed) observables.** Read the definition of $\pi(a)$ as a *relational observable*: $(\pi(a)\xi)(s) = \alpha_{-s}(a)\,\xi(s)$ is "the observable $a$, evaluated relative to the clock reading $s$" — the operator is rotated back by the flow exactly as far as the clock has advanced. This is the algebraic form of gravitational dressing. In a theory with a constraint (time-reparametrization invariance, the Hamiltonian constraint of gravity), bare operators $a \otimes 1$ are not physical because they do not commute with the constraint; the physical operators are those *correlated with a clock*: "the field when the clock shows $s$." One checks that $\pi(a)$ and $\lambda(t)$ are precisely the operators on $\mathcal{H}\otimes L^2(\mathbb{R})$ that commute with the total constraint generator (the sum of the flow generator on $\mathcal{H}$ and the clock momentum) — so **the crossed product is the algebra of constraint-invariant observables of the system + clock**. This is how Witten 2022 derives it: imposing the linearized gravitational constraint on (QFT $\otimes$ observer's clock) yields $\mathcal{M}\rtimes_{\sigma^\omega}\mathbb{R}$, and the miracle of Connes–Takesaki — type III becomes type II — is then the statement that *gauging time makes entropy finite*.

### 2.2 What it does

The construction has three main effects:

1. **It inner-ifies the flow.** An outer automorphism of $\mathcal{M}$ becomes inner on $\mathcal{M} \rtimes_\alpha \mathbb{R}$. For type III$_1$ algebras, the modular flow is genuinely outer; the crossed product makes it inner on the dressed algebra.

2. **It can change the type.** When $\alpha$ is the modular flow $\sigma^\omega$ on a type III$_1$ algebra, the crossed product is type II$_\infty$. This is the **Connes–Takesaki duality theorem** (§4 below). The crossed product **removes the type-III obstruction**.

3. **It adjoins a clock.** The auxiliary $L^2(\mathbb{R})$ factor and the translation operator $\lambda(t)$ together encode a one-parameter group of "clock states." Physical observables in the dressed algebra can be conditioned on the clock reading.

### 2.3 The modular crossed product

When $\alpha = \sigma^\omega$ is specifically the modular flow of a faithful normal state $\omega$, we call $\mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R}$ the **modular crossed product**. This is the canonical case — the choice of state $\omega$ is the only input, and the resulting dressed algebra has the structural properties below.

## 3. The dual action and the trace

### 3.1 The dual action of $\hat{\mathbb{R}}$

The crossed product comes equipped with a canonical second one-parameter group — the **dual action**. For $r \in \mathbb{R}$, define $\theta_r$ on $\mathcal{M} \rtimes_\alpha \mathbb{R}$ by:
$$
\theta_r(\pi(a)) = \pi(a), \qquad \theta_r(\lambda(t)) = e^{itr}\,\lambda(t).
$$

This extends to an automorphism of the whole crossed product. Geometrically, $\theta_r$ is multiplication by $e^{itr}$ on the translation generator; equivalently, by Fourier duality, it is translation by $-r$ on the Pontryagin-dual variable.

**Key fact.** The fixed-point algebra of the dual action,
$$
(\mathcal{M} \rtimes_\alpha \mathbb{R})^{\hat{\mathbb{R}}} := \{x \in \mathcal{M} \rtimes_\alpha \mathbb{R} : \theta_r(x) = x \text{ for all } r\},
$$
is exactly $\pi(\mathcal{M})$. **Takesaki duality** (next subsection) extends this observation.

### 3.2 The trace

**Theorem 3.1 (Existence of the trace). [Stated only — refs: Takesaki Vol. II §X.1, Vol. III §VIII.3; Bratteli–Robinson Vol. I §2.7.]** *Let $\mathcal{M}$ be a von Neumann algebra, $\omega$ a faithful normal state, $\sigma^\omega$ the modular flow. Then $\hat{\mathcal{M}} := \mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R}$ admits a faithful normal semifinite trace $\hat\tau$, unique up to rescaling. The dual action scales the trace:*
$$
\hat\tau \circ \theta_r = e^{-r}\,\hat\tau.
$$

In particular, the trace is *not* dual-invariant — the dual action rescales it. This rescaling is the "modular weight" carried by the clock.

> **Physical picture.** The trace-scaling identity is the algebraic statement that *the modular clock has no preferred zero*. Shifting the origin of modular time by $r$ (the dual action) multiplies the counting measure by the Boltzmann factor $e^{-r}$ — exactly as shifting the zero of energy rescales a partition function by $e^{-\beta\Delta E}$. Two consequences propagate into Sem II. (1) The trace, hence the dressed density matrix and dressed entropy, is defined only up to an overall scale, i.e. the entropy only up to a *state-independent additive constant* — which matches gravity, where $S_{\rm gen} = A/4G_N + S_{\rm out}$ has a renormalization ambiguity that cancels in differences. (2) The pair (type II$_\infty$ algebra, trace-scaling $\mathbb{R}$-action) is Connes–Takesaki's *flow of weights* — the complete classifying data of the original type III factor. Nothing is lost in the dressing: the type III algebra can be reconstructed from its dressed form (Takesaki duality, §4.2), so the crossed product is a change of description, not a change of physics.

### 3.3 Explicit formula in the type-I case

The trace formula in general is delicate (involves the Plancherel theorem and the dual-weight construction). In the type-I worked example below, we can write a more explicit form:

**Type-I trace formula.** Let $\mathcal{M} = \mathcal{B}(\mathcal{H})$ with faithful normal state $\omega(\cdot) = \mathrm{Tr}(\rho\,\cdot)$. The modular flow is $\sigma^\omega_t = \mathrm{Ad}(\rho^{-it})$ (Week 5 §6). The crossed product is $\hat{\mathcal{M}} = \mathcal{B}(\mathcal{H}) \otimes L^\infty(\mathbb{R})$ (after a Fourier-conjugation; see §5 below). The trace on this algebra is
$$
\hat\tau(a \otimes f) = \mathrm{Tr}(a) \cdot \int_{-\infty}^\infty f(s)\,e^{-s}\,ds,
$$
where $\mathrm{Tr}$ is the operator trace on $\mathcal{B}(\mathcal{H})$ and the $e^{-s}$ weight is the canonical (logarithmic) Haar-derived weight on $\mathbb{R}$.

This is **semifinite**, not finite: it is finite on operators of the form $(\text{trace-class}) \otimes (\text{exponentially-decaying-at-large-}s)$, but diverges on the full identity $1 \otimes 1$.

The dual action of $r \in \mathbb{R}$ on this trace is $\theta_r(a \otimes f)(s) = a \otimes f(s - r)$, and one checks
$$
\hat\tau(\theta_r(a \otimes f)) = \int f(s - r) e^{-s} ds = e^{-r} \int f(u) e^{-u} du = e^{-r}\,\hat\tau(a \otimes f).
$$
Matches Theorem 3.1.

### 3.4 The trace on the modular crossed product

In the type III case, the dressed trace has no closed-form expression in general, but it can be characterized abstractly via the **dual weight**: given the GNS data $(\mathcal{H}, \Omega, \Delta)$ for $(\mathcal{M}, \omega)$, the trace on $\hat{\mathcal{M}}$ is
$$
\hat\tau(x) = \langle \Omega \otimes h\,|\, x\,|\,\Omega \otimes h\rangle, \qquad h(s) := e^{-s/2}
$$
**(modulo regularization).** The function $h \in L^2(\mathbb{R})$ is not square-integrable in the strict sense — it diverges at $s = -\infty$ — so this formula must be regulated by restricting to a dense subspace of operators $x$ where the integral is finite. The result, properly interpreted, is the dressed semifinite trace.

In the type-I case (§3.3), this regulated formula reduces to the explicit one. In the type III case, the regulation is more delicate but the abstract trace exists by Theorem 3.1.

## 4. The type-promotion theorem

### 4.1 Connes–Takesaki

**Theorem 4.1 (Connes–Takesaki duality). [Stated only — refs: Connes & Takesaki, *Tôhoku Math. J.* 29 (1977) 473; Takesaki Vol. III §VIII.3.]** *Let $\mathcal{M}$ be a type III$_1$ factor with faithful normal state $\omega$ and modular flow $\sigma^\omega$. Then $\hat{\mathcal{M}} := \mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R}$ is a type II$_\infty$ factor.*

Equivalently: type III$_1$ + modular flow → type II$_\infty$, structurally. The "obstruction to a trace" is removed by the crossed product.

**More generally:** $\mathcal{M}$ of type III$_\lambda$ for $\lambda \in (0, 1]$ gives $\hat{\mathcal{M}}$ of type II$_\infty$. Type III$_0$ also gives type II$_\infty$ but with more subtle structure (Takesaki Vol. III). The theorem is uniform across all type III subtypes.

### 4.2 Takesaki duality

There is a **converse**: given a type II$_\infty$ vN algebra $\mathcal{N}$ with a one-parameter automorphism group $\theta$ that scales the trace by $e^{-r}$, one can form $\mathcal{N} \rtimes_\theta \mathbb{R}$ to recover the original type III algebra (up to isomorphism). This is the full Takesaki duality:

$$
\mathcal{M} \;\overset{\rtimes_{\sigma^\omega}\mathbb{R}}{\longrightarrow}\; \hat{\mathcal{M}} \;\overset{\rtimes_\theta \mathbb{R}}{\longrightarrow}\; \mathcal{M}.
$$

(The composition of two crossed products with a single one-parameter group, paired with the dual action, returns the original algebra.)

This is the **Connes–Takesaki structure theorem**: every type III factor is canonically a crossed product of a type II$_\infty$ algebra by an $\mathbb{R}$-action that scales the trace. For type III$_1$, the resulting type II$_\infty$ algebra is *the* hyperfinite type II$_\infty$ (assuming hyperfinite III$_1$ source, Week 12), and the trace-scaling action is essentially unique.

### 4.3 Why this matters

For our course:

- Type III$_1$ algebras (Week 12) admit faithful normal states, but no trace.
- Their crossed products by the modular flow are type II$_\infty$, with a unique-up-to-scaling semifinite trace.
- This makes the **dressed entropy** well-defined (Week 14), up to a state-independent additive constant.
- The same construction applied to the boundary algebras of a holographic CFT — with the modular flow replaced by the ADM Hamiltonian — gives the gravitational dressed entropy = generalized entropy of Witten 2022 (Sem II Block 1).

The Connes–Takesaki theorem is the **structural backbone of Sem II**.

## 5. Worked example: type-I crossed product

The cleanest non-trivial worked example.

### 5.1 Setup

Let $\mathcal{M} = \mathcal{B}(\mathcal{H})$ with $\dim\mathcal{H} = n < \infty$ for concreteness (the $n = \infty$ case is similar). Let $\omega(a) = \mathrm{Tr}(\rho\,a)$ for a strictly positive density matrix $\rho$ with $\mathrm{Tr}\rho = 1$. The modular flow is
$$
\sigma^\omega_t(a) = \rho^{-it}\,a\,\rho^{it} \qquad (\text{Week 5 §6.2}).
$$
This is **inner** (implemented by $\rho^{-it} \in \mathcal{M}$, which is a unitary in $\mathcal{B}(\mathcal{H})$). For finite-dim type I, the modular flow is always inner, so this is a degenerate case algebraically — but the crossed-product construction still works mechanically and is illuminating.

### 5.2 Constructing the crossed product

On $\mathcal{H} \otimes L^2(\mathbb{R})$, define:
$$
\pi(a) := \int^\oplus \sigma^\omega_{-s}(a)\,ds, \qquad (\pi(a)\xi)(s) = \rho^{is} a\rho^{-is}\,\xi(s),
$$
$$
\lambda(t) := 1 \otimes U_t, \qquad (\lambda(t)\xi)(s) = \xi(s - t).
$$

**Trick: unitary equivalence.** Since the flow is inner, define $V := \int^\oplus \rho^{-is}\,ds$ — a unitary on $\mathcal{H} \otimes L^2(\mathbb{R})$ that conjugates the modular flow into the trivial flow on the first factor:
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
where the second factor is the vN algebra of bounded multiplication operators on $L^2(\mathbb{R})$ (the abelian fixed-point algebra of $U_t$). The isomorphism is the Fourier transform on $L^2(\mathbb{R})$ identifying translations with multiplications.

### 5.3 Type

$\mathcal{B}(\mathcal{H}) \otimes L^\infty(\mathbb{R})$ is type I (the tensor product of a type I factor with an abelian vN algebra). For $\dim\mathcal{H} = n$, this is type I$_n \otimes L^\infty(\mathbb{R})$, which is type I$_n$ in the sense of factors but has uncountable center.

This is *not* a factor — it has center $1 \otimes L^\infty(\mathbb{R})$. The full Connes–Takesaki theorem statement (Theorem 4.1) is for type III sources; in the type I case here, the crossed product is a *factor-decomposed* type I algebra, not a single type II$_\infty$ factor. The type promotion happens only when the modular flow is genuinely outer.

### 5.4 Trace

The trace on $\mathcal{B}(\mathcal{H}) \otimes L^\infty(\mathbb{R})$ is the product of the operator trace and a measure on $\mathbb{R}$ with $e^{-s}$ density (the dual-action-scaling weight):
$$
\hat\tau(a \otimes f) = \mathrm{Tr}(a)\,\int_{-\infty}^\infty f(s)\,e^{-s}\,ds.
$$
This is semifinite: finite on $a \otimes f$ with $f$ exponentially-decaying-at-large-$s$, divergent on $1 \otimes 1$.

### 5.5 Lesson

In the type-I case the crossed product just produces a tensor product with $L^\infty(\mathbb{R})$. The type doesn't change in a meaningful way. The Connes–Takesaki theorem's content kicks in only when the modular flow is **outer**, which is the type III case.

## 6. Worked example: Powers factor (type III$_\lambda$)

The Powers factor $\mathcal{R}_\lambda$ (Week 4 §7) for $\lambda \in (0, 1)$ is type III$_\lambda$. Its modular flow is **outer** (more precisely, the corresponding modular automorphism of the abstract algebra is not inner, even though it can be implemented by unitaries on the GNS Hilbert space — those unitaries are not in $\mathcal{R}_\lambda$).

### 6.1 The crossed product

Form $\hat{\mathcal{R}_\lambda} := \mathcal{R}_\lambda \rtimes_{\sigma^{\omega_\lambda}}\mathbb{R}$ on the GNS Hilbert space tensored with $L^2(\mathbb{R})$. By Connes–Takesaki, this is type II$_\infty$.

### 6.2 Structural form

The dual action $\theta_r$ scales the trace by $e^{-r}$. The fixed-point subalgebra $(\hat{\mathcal{R}_\lambda})^{\hat{\mathbb{R}}}$ is $\pi(\mathcal{R}_\lambda)$, type III$_\lambda$ again.

The dressed algebra $\hat{\mathcal{R}_\lambda}$ is the hyperfinite type II$_\infty$ factor $\mathcal{R}_{0,1} = \mathcal{R} \otimes \mathcal{B}(\ell^2)$ (Murray–vN unique). The $\mathbb{R}$-action of $\theta_r$ that scales the trace is the "flow of weights" of $\mathcal{R}_\lambda$ — a discrete-spectrum action with eigenvalues $\{\lambda^n: n \in \mathbb{Z}\}$ exactly matching the S-invariant.

### 6.3 Lesson

The Powers factor gives a concrete model where:
- The original algebra is type III (specifically III$_\lambda$, but the same works for III$_1$ replacing the discrete spectrum with a continuous one).
- The modular flow is outer.
- The crossed product is genuinely type II$_\infty$, no longer a tensor product.
- The trace is semifinite, well-defined.

For the **type III$_1$** case relevant to QFT, the same machinery applies, with the discrete S-invariant of III$_\lambda$ replaced by the continuous $[0, \infty)$ of III$_1$. The dressed algebra is the hyperfinite type II$_\infty$ factor, and the trace is unique up to scaling.

## 7. The free-field Rindler crossed product

The single most important example for the Sem II program: take a type-III$_1$ wedge algebra in a free QFT and form its crossed product by the boost flow.

### 7.1 Setup

Let $\mathcal{M} = \mathcal{A}(W_R)$ be the local algebra of the right Rindler wedge in the 2D massless free scalar. By Bisognano–Wichmann (Week 10), the modular flow is the boost:
$$
\sigma^\omega_t(a) = e^{i\cdot 2\pi tK}\,a\,e^{-i\cdot 2\pi tK}, \qquad K = \text{boost generator}.
$$
(In our convention, with $\sigma_t = \mathrm{Ad}(\Delta^{-it})$ and $\Delta = e^{-2\pi K}$.)

### 7.2 The crossed product

Form $\hat{\mathcal{A}}(W_R) := \mathcal{A}(W_R) \rtimes_{\sigma^\omega}\mathbb{R}$ on $\mathcal{F} \otimes L^2(\mathbb{R}_s)$, where $\mathcal{F}$ is the Fock space and $s$ is the "modular time" variable for the $L^2(\mathbb{R})$ factor.

By Connes–Takesaki (Theorem 4.1), $\hat{\mathcal{A}}(W_R)$ is a type II$_\infty$ algebra.

### 7.3 The trace as an integral kernel

The semifinite trace on $\hat{\mathcal{A}}(W_R)$ can be written as an integral kernel:
$$
\hat\tau(a) = \int_{-\infty}^\infty e^{-2\pi s}\,\langle 0_M \otimes \delta_s\,|\,a\,|\,0_M \otimes \delta_s\rangle\,ds
$$
(modulo regularization — the $|0_M \otimes \delta_s\rangle$ "states" are not normalizable, but the integral over $s$ with the $e^{-2\pi s}$ weight is well-defined for a dense set of operators $a \in \hat{\mathcal{A}}(W_R)$).

The factor $e^{-2\pi s}$ is the **modular weight** corresponding to the $\beta_R = 2\pi$ Rindler temperature.

### 7.4 Why this is the workhorse

This explicit free-field Rindler crossed product is the model used in:

- **Witten 2022** (Sem II Block 1): same construction, but with the boost generator $K$ replaced by the ADM Hamiltonian in a large-$N$ holographic CFT.
- **CPW 2022** (Sem II Block 2): same construction, applied to the two-sided eternal black hole (TFD vacuum, two-sided boost generator $K_R - K_L$).
- **Ahmad–Jefferson 2025** (Sem II Block 4): perturbations of the same construction via the Connes cocycle (Week 7).

In each case, the explicit free-field calculation is the *check* — the only setting where everything is computable. Week 14 computes the dressed entropy in this model; Sem II Mini-Calculations 1, 2, 3 all use the same setup.

## 8. What to take away

- **Definition (proved here in finite-dim):** the crossed product $\mathcal{M} \rtimes_\alpha \mathbb{R}$ is the von Neumann algebra on $\mathcal{H} \otimes L^2(\mathbb{R})$ generated by $\pi(a)$ (fiberwise action by $\alpha_{-s}$) and $\lambda(t)$ (translation), with the commutation $\lambda(t)\pi(a)\lambda(t)^* = \pi(\alpha_t(a))$.
- **Stated only (Connes–Takesaki Theorem 4.1):** for a type III$_1$ algebra $\mathcal{M}$ with modular flow $\sigma^\omega$, the crossed product $\hat{\mathcal{M}}$ is type II$_\infty$ with a faithful normal semifinite trace, unique up to scaling.
- **Stated only (Theorem 3.1):** the dual action $\theta_r$ of $\hat{\mathbb{R}}$ on $\hat{\mathcal{M}}$ scales the trace: $\hat\tau \circ \theta_r = e^{-r}\hat\tau$.
- **Worked (type I):** crossed product of $\mathcal{B}(\mathcal{H})$ by inner modular flow is $\mathcal{B}(\mathcal{H}) \otimes L^\infty(\mathbb{R})$. The type doesn't promote — type promotion happens only for outer flows.
- **Worked (Powers):** crossed product of $\mathcal{R}_\lambda$ by its outer modular flow is the hyperfinite type II$_\infty$ factor.
- **The Sem II workhorse:** $\mathcal{A}(W_R) \rtimes_{\mathrm{boost}}\mathbb{R}$, with trace given by an explicit integral kernel involving $e^{-2\pi s}$. This is the model for every dressed-entropy computation in the recent literature.

## 9. Looking ahead

Week 14 defines the **dressed entropy** on the type II$_\infty$ algebra $\hat{\mathcal{M}}$ and proves that **differences** of dressed entropies between two states reproduce Araki–Uhlmann relative entropy **plus a "modular boundary term."** This boundary term is finite, computable, and is the central technical object of the Sem II papers (Witten 2022, CPW, AAJ). For the free-field Rindler model (§7), we'll compute the dressed entropy explicitly and verify the boundary-term formula.

## 10. Problem set

**Core problems.**

**1. Verify the crossed-product commutation relation.** For the abstract crossed product $\mathcal{M} \rtimes_\alpha \mathbb{R}$, compute $\lambda(t)\,\pi(a)\,\lambda(t)^*$ explicitly using the definitions of $\pi(a)$ and $\lambda(t)$ in §2.1, and verify $\lambda(t)\pi(a)\lambda(t)^* = \pi(\alpha_t(a))$.

**2. Crossed product of $M_2(\mathbb{C})$ by an inner flow.** Let $\mathcal{M} = M_2(\mathbb{C})$, $\rho = \mathrm{diag}(p, 1-p)$ with $p \in (0, 1)$, $\sigma_t = \mathrm{Ad}(\rho^{-it})$. Construct $\mathcal{M} \rtimes_\sigma \mathbb{R}$ explicitly on $\mathbb{C}^2 \otimes L^2(\mathbb{R})$. Use the unitary $V$ of §5.2 to identify the result as $M_2(\mathbb{C}) \otimes L^\infty(\mathbb{R})$.

**3. Trace-scaling by the dual action.** For the type-I case $\hat{\mathcal{M}} = \mathcal{B}(\mathcal{H}) \otimes L^\infty(\mathbb{R})$ with $\hat\tau(a \otimes f) = \mathrm{Tr}(a)\int f(s)e^{-s}ds$, compute $\hat\tau(\theta_r(a \otimes f))$ for the dual action $\theta_r(a \otimes f)(s) = a \otimes f(s - r)$ and verify $\hat\tau \circ \theta_r = e^{-r}\hat\tau$.

**4. The original algebra inside the crossed product.** Show that $\pi(\mathcal{M})$ is a *proper* vN subalgebra of $\mathcal{M} \rtimes_\alpha \mathbb{R}$, equal to the fixed-point algebra under the dual action: $\pi(\mathcal{M}) = (\mathcal{M} \rtimes_\alpha \mathbb{R})^{\hat{\mathbb{R}}}$.

**5. Inner-ification.** Show that the automorphism $\alpha_t$ on $\mathcal{M}$, lifted to $\pi(\alpha_t(\cdot))$ on $\pi(\mathcal{M}) \subset \mathcal{M} \rtimes_\alpha \mathbb{R}$, is **inner** in the larger algebra — implemented by the unitary $\lambda(t)$. Why is this useful when $\alpha$ is outer on $\mathcal{M}$ alone?

**Starred problems.**

**6\*. Crossed product of the Powers factor.** Construct $\mathcal{R}_\lambda \rtimes_{\sigma^{\omega_\lambda}}\mathbb{R}$ for $\lambda \in (0, 1)$. State (without proof) that the result is the hyperfinite type II$_\infty$ factor. Identify the "flow of weights" — the discrete-spectrum action of $\hat{\mathbb{R}}$ that scales the trace.

**7\*. Trace uniqueness.** Show that the trace on $\mathcal{M} \rtimes_{\sigma^\omega}\mathbb{R}$ for $\mathcal{M}$ a factor is unique up to scaling. (*Hint:* uses the structure of type II$_\infty$ factors and that the trace is dual-action-equivariant.)

**8\*. Free-field Rindler crossed product.** Construct $\mathcal{A}(W_R) \rtimes_{\mathrm{boost}}\mathbb{R}$ for the 2D massless free scalar. Verify the trace formula
$$
\hat\tau(a) = \int_{-\infty}^\infty e^{-2\pi s}\,\langle 0_M \otimes \delta_s\,|\,a\,|\,0_M \otimes \delta_s\rangle\,ds
$$
on a dense subspace of operators $a = W(f) \otimes g(X)$ where $g(X)$ is a bounded function of the position operator on $L^2(\mathbb{R}_s)$.

**Project problems.**

**9. Reading bridge.** Read Witten 2022 §3 (the crossed-product construction in the holographic setting). Identify the precise crossed product Witten uses, and match each ingredient to the abstract construction of this lecture. Where does Bisognano–Wichmann appear? Where does the trace formula appear?

**10. Liu lectures preview.** Read Liu §5 (the lectures, arXiv:2510.07017). Compare Liu's pedagogical exposition of the crossed product with this lecture. Identify any places where the conventions differ.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block D. Last revised 2026-06-11.*
