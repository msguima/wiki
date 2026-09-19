---
title: "Week 1 — C*-algebras, States, and the GNS Construction"
type: lecture-notes
course: syllabus
semester: 1
week: 1
block: A
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Hilbert spaces, bounded operators, basic functional analysis
modified: 2026-06-11
---

# Week 1 — C\*-algebras, States, and the GNS Construction

> *We could have started this course with operators on a Hilbert space, defined a "physical theory" as a Hilbert space plus a Hamiltonian, and proceeded as in any quantum mechanics class. We do not. The reason — which will become precise in Block C — is that quantum field theory has no natural Hilbert space: it has many, and they are mutually inequivalent. The algebraic language is the one that survives.*

## 0. Reading

**Primary:** Bratteli & Robinson Vol. I, §2.1–2.3 (definitions of C\*-algebras and states), §2.3.3 (GNS construction).

**Secondary:**
- Murphy, *C\*-algebras and Operator Theory*, ch. 1–3 — gentler than B&R; recommended for first reading.
- Takesaki Vol. I, ch. I — terse but authoritative.

**For the curious:** Connes, *Noncommutative Geometry*, ch. I.1 for the Gelfand–Naimark theorem in geometric perspective.

**Proof-status labels.** Theorems in this note carry inline labels in the standard course convention (introduced systematically in Week 3 and codified in the note-quality template and [[courses/2026-algebraic-qft-course/conventions|conventions.md]]):

- **[Proved.]** Full proof given in the notes.
- **[Sketched.]** Main ideas given; some analytic details skipped.
- **[Stated only — refs.]** Theorem cited from the literature with reference.

## 1. Motivation: why algebras?

In a finite-dimensional quantum system, the observables are Hermitian matrices in $M_n(\mathbb{C})$, the states are density matrices, and there is essentially one Hilbert space, $\mathbb{C}^n$. The algebra of observables, the Hilbert space, and the state space are interconvertible, and we usually do not distinguish them.

In quantum field theory this neat picture fails, for three reasons that motivate the algebraic approach:

1. **Hilbert spaces are non-unique.** The Stone–von Neumann theorem fails in infinite dimensions: distinct representations of the canonical commutation relations need not be unitarily equivalent. The free scalar field in two different vacuum states (e.g., a Minkowski vacuum versus a Rindler vacuum) gives non-isomorphic Hilbert spaces. Picking one Hilbert space is a *choice*, not a structural feature of the theory.

2. **Local algebras have no traces.** As we will see in Block C (Week 12), the algebra of observables localized in a bounded spacetime region of relativistic QFT is a [[type-iii-von-neumann-algebras|type III₁ factor]], for which there is no trace and no notion of "density matrix." Standard quantum-mechanical reasoning ("the state is given by a density matrix $\rho$") simply cannot be applied. The algebraic framework supplies the right substitute: states are linear functionals.

3. **Modular theory needs algebras.** The whole content of the [[tomita-takesaki-modular-theory|Tomita–Takesaki theorem]] (Block B) is a structural statement about von Neumann algebras together with a cyclic and separating vector. Without the algebra, there is no statement.

This week sets up the foundations. We define C\*-algebras (the algebraic object), states (the linear functionals that play the role of "expectation values"), and the GNS construction (the canonical bridge from a state on an algebra to a Hilbert-space representation). The whole rest of the course is built on this.

## 2. Banach algebras

### 2.1 Definitions

**Definition 2.1.** A *Banach algebra* is a complex vector space $\mathcal{A}$ equipped with:
- An associative bilinear product $\mathcal{A} \times \mathcal{A} \to \mathcal{A}$, $(a,b) \mapsto ab$;
- A norm $\|\cdot\|$ for which $\mathcal{A}$ is a Banach space (i.e., complete);
- The submultiplicativity property $\|ab\| \le \|a\|\,\|b\|$ for all $a,b \in \mathcal{A}$.

If there exists $1 \in \mathcal{A}$ with $1 \cdot a = a \cdot 1 = a$ for all $a$, we say $\mathcal{A}$ is *unital* and call $1$ the unit. We will assume unital throughout unless explicitly stated otherwise; the non-unital case can be handled by *unitization* (adjoining an external identity), which we touch on in Problem 2.

**Definition 2.2.** A *\*-algebra* is a Banach algebra $\mathcal{A}$ together with an *involution* $a \mapsto a^*$ satisfying:
1. $(a^*)^* = a$ (involutive),
2. $(a + \lambda b)^* = a^* + \overline{\lambda}\, b^*$ for $\lambda \in \mathbb{C}$ (conjugate-linear),
3. $(ab)^* = b^* a^*$ (antimultiplicative).

We do **not** yet require any compatibility between $\|\cdot\|$ and $*$. The whole point of the C\*-condition (§4) is to impose exactly such a compatibility.

### 2.2 Examples

**Example 2.3 (Bounded operators).** Let $\mathcal{H}$ be a Hilbert space. The space $\mathcal{B}(\mathcal{H})$ of bounded linear operators on $\mathcal{H}$ is a unital Banach \*-algebra under composition, the operator norm, and the adjoint operation $T \mapsto T^*$. Submultiplicativity is the standard $\|ST\| \le \|S\|\|T\|$.

**Example 2.4 (Continuous functions).** Let $X$ be a compact Hausdorff space. The space $C(X)$ of continuous $\mathbb{C}$-valued functions on $X$, equipped with pointwise multiplication, the supremum norm $\|f\|_\infty = \sup_{x \in X} |f(x)|$, and pointwise complex conjugation $f^*(x) = \overline{f(x)}$, is a unital commutative Banach \*-algebra.

**Example 2.5 (Matrices).** The space $M_n(\mathbb{C})$ of complex $n \times n$ matrices, with matrix multiplication, the operator norm (i.e., the largest singular value), and the conjugate-transpose, is a finite-dimensional Banach \*-algebra. This is the special case $\mathcal{H} = \mathbb{C}^n$ of Example 2.3.

**Example 2.6 (Bounded measurable functions).** Let $(X, \Sigma, \mu)$ be a $\sigma$-finite measure space. The space $L^\infty(X, \mu)$ of essentially bounded measurable functions modulo equality $\mu$-almost-everywhere, with pointwise operations, the essential supremum norm, and pointwise conjugation, is a unital commutative Banach \*-algebra.

We will eventually see that Examples 2.3–2.6 are *all* the C\*-algebras up to representation: this is the content of the Gelfand–Naimark theorems (§5).

### 2.3 The spectrum

**Definition 2.7.** Let $\mathcal{A}$ be a unital Banach algebra and $a \in \mathcal{A}$. The *resolvent set* of $a$ is
$$
\rho(a) = \{\lambda \in \mathbb{C} : a - \lambda 1 \text{ is invertible in } \mathcal{A}\},
$$
and the *spectrum* of $a$ is its complement, $\sigma(a) = \mathbb{C} \setminus \rho(a)$.

> **Physical picture.** The spectrum is the algebraic substitute for "the set of possible measurement outcomes." In $M_n(\mathbb{C})$ it is the set of eigenvalues; in $C(X)$ it is the range of the function; in $\mathcal{B}(\mathcal{H})$ it contains the eigenvalues plus the continuous spectrum that physicists handle with "generalized eigenstates." The definition through *invertibility* is what makes the notion representation-independent: whether $a - \lambda 1$ has an inverse is a question about the algebra alone, asked without ever mentioning vectors or wave functions. When we later say "the spectrum of the modular operator determines the type of the algebra" (Week 12), it is exactly this representation-free notion of outcome set that does the work.

**Theorem 2.8. [Proved.]** *For any $a \in \mathcal{A}$, the spectrum $\sigma(a)$ is a non-empty compact subset of $\mathbb{C}$ contained in the closed disk of radius $\|a\|$.*

**Proof.** *Boundedness.* If $|\lambda| > \|a\|$, the Neumann series
$$
R(\lambda) := \sum_{n=0}^\infty \lambda^{-n-1} a^n
$$
converges absolutely in $\mathcal{A}$, since $\|\lambda^{-n-1} a^n\| \le |\lambda|^{-1} (\|a\|/|\lambda|)^n$ is geometric with ratio $< 1$ and $\mathcal{A}$ is complete. Multiplying term by term and telescoping, $(\lambda 1 - a) R(\lambda) = R(\lambda)(\lambda 1 - a) = 1$. Hence $\lambda \in \rho(a)$, so $\sigma(a)$ lies in the closed disk of radius $\|a\|$.

*Closedness.* Invertible elements form an open set: if $x$ is invertible and $\|y - x\| < \|x^{-1}\|^{-1}$, then $y = x(1 - x^{-1}(x-y))$ with $\|x^{-1}(x - y)\| < 1$, so the Neumann series for $(1 - x^{-1}(x-y))^{-1}$ converges and $y$ is invertible. Applying this to $x = \lambda 1 - a$ shows $\rho(a)$ is open.

*Non-emptiness.* On $\rho(a)$ the resolvent $\lambda \mapsto (\lambda 1 - a)^{-1}$ is holomorphic as a Banach-space-valued function: the identity
$$
(\lambda 1 - a)^{-1} - (\mu 1 - a)^{-1} = (\mu - \lambda)\,(\lambda 1 - a)^{-1}(\mu 1 - a)^{-1}
$$
(the resolvent identity) shows the difference quotient converges in norm as $\mu \to \lambda$. For $|\lambda| > \|a\|$ the Neumann series gives $\|(\lambda 1 - a)^{-1}\| \le (|\lambda| - \|a\|)^{-1} \to 0$ at infinity. If $\sigma(a)$ were empty, then for every bounded functional $\varphi \in \mathcal{A}^*$ the scalar function $\varphi((\lambda 1 - a)^{-1})$ would be entire and vanish at infinity, hence identically zero by Liouville. Since bounded functionals separate points (Hahn–Banach), $(\lambda 1 - a)^{-1} = 0$ for all $\lambda$ — contradicting $(\lambda 1 - a)^{-1}(\lambda 1 - a) = 1$. $\square$

Non-emptiness: the resolvent function $\lambda \mapsto (\lambda 1 - a)^{-1}$ is holomorphic on $\rho(a)$ and tends to $0$ at infinity. If $\sigma(a)$ were empty, the resolvent would be a bounded entire $\mathcal{A}$-valued function vanishing at infinity, hence identically zero by Liouville's theorem in Banach-valued holomorphy, contradicting $(\lambda 1 - a)^{-1} \cdot (\lambda 1 - a) = 1$. $\square$

The number
$$
r(a) = \sup\{|\lambda| : \lambda \in \sigma(a)\}
$$
is called the *spectral radius*. We will need one classical fact about it.

**Theorem 2.9 (Beurling–Gelfand spectral radius formula). [Sketched.]** *In any unital Banach algebra,*
$$
r(a) = \lim_{n \to \infty} \|a^n\|^{1/n},
$$
*and the limit exists.*

**Sketch of proof.** For the lower bound: if $\lambda \in \sigma(a)$ then $\lambda^n \in \sigma(a^n)$ (factor $\lambda^n 1 - a^n = (\lambda 1 - a)\,q(a)$ with $q$ a polynomial; if $\lambda^n 1 - a^n$ were invertible, $\lambda 1 - a$ would have a one-sided inverse on each side, hence be invertible). Then $|\lambda|^n \le \|a^n\|$ by Theorem 2.8, so $r(a) \le \liminf_n \|a^n\|^{1/n}$. For the upper bound: the resolvent is holomorphic on $\{|\lambda| > r(a)\}$, so its Laurent expansion $\sum_n \lambda^{-n-1} a^n$ — valid a priori only for $|\lambda| > \|a\|$ — converges on the whole region $|\lambda| > r(a)$ by Banach-valued holomorphy. Convergence of the series forces $\|\lambda^{-n-1} a^n\| \to 0$, hence $\limsup_n \|a^n\|^{1/n} \le |\lambda|$ for every $|\lambda| > r(a)$. Existence of the limit follows from comparing the two bounds. $\square$

This formula is the engine behind the rigidity of C\*-algebras: it expresses a purely algebraic quantity (the spectral radius) as a purely metric limit. We use it in Lemma 4.3 below, where it forces the C\*-norm to be an algebraic invariant.

## 3. Self-adjoint, normal, unitary, positive

In a \*-algebra $\mathcal{A}$, certain elements are distinguished by their relation to the involution.

**Definition 3.1.** An element $a \in \mathcal{A}$ is:
- *Self-adjoint* (or *Hermitian*) if $a = a^*$;
- *Normal* if $a a^* = a^* a$;
- *Unitary* if $a a^* = a^* a = 1$;
- *Positive* if $a = b^* b$ for some $b \in \mathcal{A}$.

Self-adjoints generalize Hermitian operators (real spectrum, real expectation values). Unitaries generalize unitary operators. Normals generalize operators that admit a spectral decomposition.

> **Physical picture.** The involution is where the physics enters the algebra. Self-adjoint elements are the *observables* — the things a lab can measure, with real outcomes (Theorem 4.5 below makes "real outcomes" a theorem, not an axiom). Unitaries are the *symmetries and time evolutions* — the operations that can be undone. Positive elements are the *intensities*: counts, probabilities, energies-above-ground-state, anything that can only come out non-negative. The decomposition $a = h + ik$ of Lemma 3.2 says the full algebra is just the complexification of its observables, so nothing physical is lost by keeping the non-self-adjoint elements around — and much computational convenience is gained, exactly as with raising/lowering operators in quantum mechanics.

**Lemma 3.2. [Proved — direct verification.]** *In a \*-algebra, any element decomposes uniquely as $a = h + ik$ with $h, k$ self-adjoint, namely $h = (a + a^*)/2$ and $k = (a - a^*)/(2i)$.*

This is the algebraic analogue of the real-imaginary decomposition of complex numbers. Consequently, any \*-algebra is the complex linear span of its self-adjoint elements, and any positive linear functional (defined below) is determined by its values on self-adjoints.

## 4. C\*-algebras

### 4.1 The C\*-identity

We have not yet related the norm to the involution. The single axiom doing all the work is:

**Definition 4.1.** A Banach \*-algebra $\mathcal{A}$ is a *C\*-algebra* if
$$
\boxed{\| a^* a \| = \|a\|^2 \qquad \text{for all } a \in \mathcal{A}.}
$$
This is called the *C\*-identity*.

The C\*-identity is innocuous-looking but extraordinarily restrictive. Its consequences propagate everywhere.

> **Physical picture.** The C\*-identity is the statement that *the norm of an observable is the largest value it can be measured to take*. For a self-adjoint $a$, Lemma 4.3 below gives $\|a\| = r(a) = \sup\{|\lambda| : \lambda \in \sigma(a)\}$ — the norm is the extreme measurement outcome, not an arbitrary metric bookkeeping device. Corollary 4.4 then says the metric structure of the theory is *determined* by the physics (which combinations of observables are invertible), with no freedom left over. Contrast a generic Banach \*-algebra, where many inequivalent norms can coexist on the same algebra: there, "size" is a convention. In a C\*-algebra, size is spectroscopy.

**Lemma 4.2. [Proved.]** *In a C\*-algebra, $\|a^*\| = \|a\|$ for all $a$.*

**Proof.** From $\|a\|^2 = \|a^* a\| \le \|a^*\| \|a\|$ we get $\|a\| \le \|a^*\|$. Replacing $a$ by $a^*$ gives the reverse, so $\|a^*\| = \|a\|$. $\square$

**Lemma 4.3. [Proved.]** *If $a$ is self-adjoint in a C\*-algebra, then $\|a\| = r(a)$.*

**Proof.** Since $a^* = a$, the C\*-identity gives $\|a^2\| = \|a^* a\| = \|a\|^2$. By induction, $\|a^{2^n}\| = \|a\|^{2^n}$. Theorem 2.9 (the limit exists, so any subsequence computes it): $r(a) = \lim_{n} \|a^n\|^{1/n} = \lim_n \|a^{2^n}\|^{1/2^n} = \|a\|$. $\square$

**Corollary 4.4. [Proved.]** *The norm on a C\*-algebra is uniquely determined by the algebraic structure.*

**Proof.** For any $a$, the element $a^* a$ is self-adjoint, so $\|a^* a\| = r(a^* a)$ by Lemma 4.3. The spectrum $\sigma(a^*a)$ is purely algebraic (depends only on which $a^*a - \lambda 1$ are invertible), and $\|a\|^2 = \|a^*a\| = r(a^*a)$ then determines $\|a\|$ uniquely. $\square$

This corollary is striking: in a Banach algebra one might equip the same underlying \*-algebra with many different submultiplicative norms; the C\*-identity rules this out.

### 4.2 Examples are C\*-algebras

It is straightforward to verify that Examples 2.3–2.6 are all C\*-algebras:

- $\mathcal{B}(\mathcal{H})$: the C\*-identity is the standard identity $\|T^* T\| = \|T\|^2$ on bounded operators (proved via $\|T\|^2 = \sup_{\|\xi\|=1} \|T\xi\|^2 = \sup \langle\xi, T^*T\xi\rangle = \|T^*T\|$ when $T^*T$ is self-adjoint).
- $C(X)$: $\|f^*f\|_\infty = \sup |f|^2 = \|f\|_\infty^2$.
- $M_n(\mathbb{C})$: special case of $\mathcal{B}(\mathcal{H})$.
- $L^\infty(X, \mu)$: as for $C(X)$.

### 4.3 Spectrum and self-adjointness

**Theorem 4.5. [Proved.]** *In a C\*-algebra, the spectrum of a self-adjoint element lies in $\mathbb{R}$.*

**Proof.** Let $a = a^*$ and $\lambda = \alpha + i\beta \in \sigma(a)$ with $\alpha, \beta \in \mathbb{R}$. The element $a + it \cdot 1$ for real $t$ is normal, with spectrum $\sigma(a) + it$. Hence $\alpha + i(\beta + t) \in \sigma(a + it)$. Therefore
$$
|\alpha + i(\beta + t)|^2 \le \|a + it\|^2 = \|(a+it)^*(a+it)\| = \|a^2 + t^2\| \le \|a\|^2 + t^2.
$$
Expanding the LHS: $\alpha^2 + (\beta+t)^2 \le \|a\|^2 + t^2$, i.e., $\alpha^2 + \beta^2 + 2\beta t \le \|a\|^2$. As $t \to \pm\infty$, the inequality fails unless $\beta = 0$. $\square$

**Corollary 4.6. [Stated only — follows from Theorem 4.5 applied to $u^*u = 1$.]** *In a C\*-algebra, the spectrum of a unitary lies in the unit circle $\{|\lambda| = 1\}$.*

### 4.4 Positive elements: an order structure

**Theorem 4.7. [Sketched — refs: Bratteli–Robinson Vol. I §2.2.4.]** *In a unital C\*-algebra, the following are equivalent for a self-adjoint $a$:*
(i) $a = b^* b$ *for some* $b \in \mathcal{A}$;
(ii) $\sigma(a) \subset [0, \infty)$;
(iii) $a = c^2$ *for some self-adjoint* $c$.

We write $a \ge 0$ when these hold and call such $a$ *positive*. The set $\mathcal{A}_+$ of positive elements is a closed convex cone and gives $\mathcal{A}_{sa}$ (self-adjoints) the structure of an ordered real Banach space: $a \le b$ means $b - a \in \mathcal{A}_+$.

> **Physical picture.** The equivalence (i) $\Leftrightarrow$ (ii) is the algebraic version of a familiar quantum-mechanical fact: an observable whose measured values are always non-negative is exactly one that can be written as "something dagger something" — an intensity, $|{\rm amplitude}|^2$. The order structure $a \le b$ is operational: it means every state assigns $a$ a smaller expectation value than $b$ (once states are defined in §6, check this as an exercise). Everything probabilistic in the algebraic framework — positivity of states, Cauchy–Schwarz, the GNS inner product — flows through this cone. It is also the structure that survives in type III algebras when density matrices do not: we can always say which observables dominate which, even when we cannot write $\mathrm{Tr}(\rho\, a)$.

Sketch: (iii) $\Rightarrow$ (i) is trivial ($b = c$). (i) $\Rightarrow$ (ii) requires showing $b^*b$ has non-negative spectrum, which follows from polar decomposition arguments. (ii) $\Rightarrow$ (iii) uses the *continuous functional calculus*: when $\sigma(a) \subset [0, \infty)$ we can take $\sqrt{a}$ as a self-adjoint element via $f(a)$ for $f(t) = \sqrt{t}$. The continuous functional calculus is the assignment $f \mapsto f(a)$ for $f \in C(\sigma(a))$ and self-adjoint $a$, satisfying $(fg)(a) = f(a) g(a)$, $\overline{f}(a) = f(a)^*$, etc.; we will use it freely in the rest of the course. (See Bratteli–Robinson Thm 2.1.13.)

## 5. Two foundational theorems (statements only)

We mention these as motivation; we do not prove them in this course.

**Theorem 5.1 (Gelfand–Naimark, commutative case). [Stated only — refs: Bratteli–Robinson Vol. I §2.3.2; Murphy ch. 2.]** *Every unital commutative C\*-algebra $\mathcal{A}$ is isometrically \*-isomorphic to $C(X)$ for some compact Hausdorff space $X$, namely the spectrum (Gelfand spectrum) of $\mathcal{A}$.*

This says: commutative C\*-algebras and compact Hausdorff spaces are the same thing, viewed two ways. The "noncommutative space" interpretation underlying noncommutative geometry follows: a non-commutative C\*-algebra is interpreted as the algebra of "continuous functions on a non-existent space."

**Theorem 5.2 (Gelfand–Naimark, general case). [Stated only — proof essentially the GNS construction of §7 applied to a separating family of states; refs: Bratteli–Robinson Vol. I §2.3.5.]** *Every C\*-algebra is isometrically \*-isomorphic to a norm-closed \*-subalgebra of $\mathcal{B}(\mathcal{H})$ for some Hilbert space $\mathcal{H}$.*

This says: any abstract C\*-algebra is concretely a subalgebra of bounded operators on some Hilbert space. The proof is the GNS construction (§7) applied to a "rich enough" family of states.

These two theorems frame the course: the first says C\*-algebras generalize topology; the second says they always come from operators on Hilbert spaces. Modular theory (Block B) and type classification (Block C) live in the second world.

## 6. States

### 6.1 Definition

**Definition 6.1.** A *state* on a unital C\*-algebra $\mathcal{A}$ is a linear functional $\omega : \mathcal{A} \to \mathbb{C}$ satisfying:
1. *Positivity:* $\omega(a^* a) \ge 0$ for all $a \in \mathcal{A}$;
2. *Normalization:* $\omega(1) = 1$.

The state space, denoted $\mathcal{S}(\mathcal{A})$, is a convex subset of the dual $\mathcal{A}^*$.

It is a non-trivial fact that any state is automatically continuous, with $\|\omega\|_{\mathcal{A}^*} = \omega(1) = 1$. The key mechanism is worth seeing: for self-adjoint $a$ with $\|a\| \le 1$, the element $1 - a$ is positive (its spectrum lies in $[0,2]$ by Lemma 4.3 and Theorem 4.5, and positivity is spectral by Theorem 4.7), so $\omega(1-a) \ge 0$, i.e. $\omega(a) \le 1$; the same for $1 + a$ gives $|\omega(a)| \le 1$. The general element is then controlled by Cauchy–Schwarz, $|\omega(a)|^2 = |\omega(1^* a)|^2 \le \omega(1)\,\omega(a^*a) \le \|a^* a\| = \|a\|^2$. Continuity of states is thus a *consequence of positivity plus the spectral control the C\*-identity provides* — nothing needs to be assumed about $\omega$ beyond algebra. (Problem 7\*\* asks for the careful version.)

> **Physical picture.** A state is a *preparation procedure*, described entirely by the statistics it produces. The lab never hands you a vector in a Hilbert space; it hands you a list of expectation values of the observables you measured. Definition 6.1 takes that operational data — a positive, normalized assignment of numbers to observables — as the primitive notion. Vectors and density matrices are *derived* objects, reconstructed (when possible) by the GNS construction of §7. This inversion of logic is precisely what lets the formalism survive in QFT, where a single preparation (say, the Minkowski vacuum restricted to a Rindler wedge) admits no density-matrix description at all, yet remains a perfectly good state in the present sense.

### 6.2 The role of $\omega$ as expectation value

Given an observable $a \in \mathcal{A}_{sa}$, the number $\omega(a)$ is the *expectation value* of $a$ in the state $\omega$. The variance is $\omega(a^2) - \omega(a)^2$, and so on. All quantum-mechanical statistics is recovered from these moments.

This is *exactly* the role density matrices play in quantum mechanics: $\omega_\rho(a) = \mathrm{Tr}(\rho a)$. The algebraic framework abstracts this away from a specific Hilbert space.

### 6.3 Examples

**Example 6.2 (Vector states).** Let $\pi : \mathcal{A} \to \mathcal{B}(\mathcal{H})$ be a representation and $\xi \in \mathcal{H}$ a unit vector. Then
$$
\omega_\xi(a) := \langle \xi, \pi(a) \xi \rangle
$$
is a state. Positivity: $\omega_\xi(a^*a) = \|\pi(a)\xi\|^2 \ge 0$. Normalization: $\omega_\xi(1) = \|\xi\|^2 = 1$.

**Example 6.3 (Density-matrix states).** Same setting, $\rho$ a positive trace-class operator with $\mathrm{Tr}(\rho) = 1$. Then $\omega_\rho(a) = \mathrm{Tr}(\rho \pi(a))$ is a state. This generalizes Example 6.2: vector states are the case of rank-one $\rho$.

**Example 6.4 (Probability measures on $C(X)$).** Let $\mu$ be a probability measure on a compact Hausdorff space $X$. Then
$$
\omega_\mu(f) = \int_X f \, d\mu
$$
is a state on $C(X)$, and conversely (Riesz representation theorem): *every* state on $C(X)$ is of this form for a unique Borel probability measure $\mu$. The state space of $C(X)$ is the set of probability measures on $X$, classical probability theory inside the algebraic framework.

**Example 6.5 (Tracial state on $M_n(\mathbb{C})$).** The functional $\tau(a) = \frac{1}{n} \mathrm{Tr}(a)$ is a state on $M_n(\mathbb{C})$. It is *tracial*: $\tau(ab) = \tau(ba)$. We will see in Block A (Week 3) that the existence of a tracial state forces an algebra to be of type $\mathrm{I}$ or $\mathrm{II}$, never type $\mathrm{III}$.

### 6.4 Pure and mixed states

**Definition 6.6.** A state $\omega$ is *pure* if it cannot be written as a non-trivial convex combination of states: $\omega = t \omega_1 + (1-t) \omega_2$ with $\omega_1, \omega_2 \in \mathcal{S}(\mathcal{A})$ and $t \in (0,1)$ implies $\omega_1 = \omega_2 = \omega$.

The pure states are the *extreme points* of the convex set $\mathcal{S}(\mathcal{A})$. Krein–Milman ensures there are enough of them to recover the full state space by closure-of-convex-hull.

**Fact 6.7.** *On $\mathcal{B}(\mathcal{H})$, the pure states are exactly the vector states (Example 6.2). On a commutative algebra $C(X)$, the pure states are exactly the Dirac measures $\delta_x$, $x \in X$.*

This already exhibits a striking algebraic phenomenon: in commutative algebras, the pure states are *points* of the underlying space — i.e., classical configurations with no quantum superposition. In non-commutative algebras, the pure states are *vectors*, i.e., genuinely quantum states. The non-commutativity of $\mathcal{A}$ measures the "quantumness" of the system.

## 7. The GNS construction

We come to the centerpiece of the week. The GNS construction takes a state on a C\*-algebra and produces a Hilbert-space representation in which the state is realized as a vector state. It is functorial, canonical, and the foundation of essentially everything in the algebraic framework. Tomita–Takesaki theory in Block B is built on it.

> **Physical picture.** GNS is the rigorous version of a construction every field theorist already knows: *build the Hilbert space by acting with fields on the vacuum*. In canonical QFT one populates Fock space as $\phi(f_1)\cdots\phi(f_n)|0\rangle$; the inner products of such vectors are the vacuum correlation functions $\langle 0|\phi(f_1)^\dagger \cdots |0\rangle$. GNS says: that procedure needs nothing but the correlation functions themselves. Hand me the expectation functional $\omega$ (the full set of "Wightman functions" of the algebra), and I will manufacture the Hilbert space, the operators, and the vacuum vector, canonically and uniquely. This is the same logic as the Wightman reconstruction theorem, stripped to its algebraic skeleton. It also explains the central moral of the week: *the state picks the Hilbert space*. Different phases of a theory — different temperatures, different vacua, spontaneously broken versus unbroken — give inequivalent GNS representations of the same algebra. The Hilbert space is not part of the kinematics; it is part of the state.

### 7.1 Setup

Fix a C\*-algebra $\mathcal{A}$ and a state $\omega$ on $\mathcal{A}$. We will construct:
- A Hilbert space $\mathcal{H}_\omega$;
- A \*-representation $\pi_\omega : \mathcal{A} \to \mathcal{B}(\mathcal{H}_\omega)$;
- A unit vector $\Omega_\omega \in \mathcal{H}_\omega$ that is *cyclic* (the linear span of $\pi_\omega(\mathcal{A}) \Omega_\omega$ is dense in $\mathcal{H}_\omega$);

such that
$$
\omega(a) = \langle \Omega_\omega, \pi_\omega(a) \Omega_\omega \rangle \quad \text{for all } a \in \mathcal{A}.
$$

The triple $(\pi_\omega, \mathcal{H}_\omega, \Omega_\omega)$ is the *GNS triple* associated to $\omega$.

### 7.2 The construction

**Step 1: a sesquilinear form.** Define on $\mathcal{A}$ a sesquilinear form by
$$
\langle a, b \rangle_\omega := \omega(a^* b).
$$
This is *positive semidefinite*: $\langle a, a\rangle_\omega = \omega(a^* a) \ge 0$. (Note: with this convention the form is $\mathbb{C}$-linear in the second slot, conjugate-linear in the first, matching the physics convention.)

The Cauchy–Schwarz inequality holds: $|\langle a, b \rangle_\omega|^2 \le \langle a, a\rangle_\omega \langle b, b\rangle_\omega$.

**Step 2: factor out the null space.** Define
$$
\mathcal{N}_\omega := \{ a \in \mathcal{A} : \omega(a^* a) = 0 \}.
$$
By Cauchy–Schwarz, $a \in \mathcal{N}_\omega$ iff $\omega(b^* a) = 0$ for all $b \in \mathcal{A}$. Hence $\mathcal{N}_\omega$ is a *left ideal* in $\mathcal{A}$: if $a \in \mathcal{N}_\omega$ and $c \in \mathcal{A}$, then $\omega((ca)^* (ca)) = \omega(a^* c^* c a) \le \|c^* c\| \omega(a^* a) = 0$, so $ca \in \mathcal{N}_\omega$. (The inequality $\omega(a^* c^* c a) \le \|c^* c\| \omega(a^* a)$ uses that $c^* c$ is positive and bounded by $\|c^* c\| \cdot 1$; rearranging gives a positive functional applied to a positive element. Careful: this uses positivity of the state crucially.)

> **Physical picture.** The null space $\mathcal{N}_\omega$ consists of the operations the state cannot see: $a \in \mathcal{N}_\omega$ means the "excited vector" $a\Omega$ has zero norm, i.e. acting with $a$ on this preparation produces nothing detectable in any correlation function. Quotienting by $\mathcal{N}_\omega$ is the statement that two operators which produce identical statistics on top of $\omega$ define the same physical excitation *of this state* — even if they are very different elements of the abstract algebra. This is why the same algebra can yield wildly different Hilbert spaces from different states: each state erases a different set of distinctions. (For a faithful state, nothing is erased: $\mathcal{N}_\omega = 0$, as in the tracial example of §8.2. Faithfulness becomes the "separating" condition in Week 5.)

The quotient $\mathcal{A} / \mathcal{N}_\omega$ inherits a positive-definite inner product from $\langle\cdot,\cdot\rangle_\omega$:
$$
\langle [a], [b] \rangle := \omega(a^* b),
$$
where $[a]$ denotes the equivalence class of $a$. Well-definedness uses the left-ideal property: if $a \sim a'$ and $b \sim b'$ then $\omega(a^* b) = \omega(a'^* b')$.

**Step 3: complete to a Hilbert space.** Let $\mathcal{H}_\omega$ be the completion of $\mathcal{A}/\mathcal{N}_\omega$ with respect to this inner product.

**Step 4: define the representation.** For $a \in \mathcal{A}$, define $\pi_\omega(a) : \mathcal{A}/\mathcal{N}_\omega \to \mathcal{A}/\mathcal{N}_\omega$ by left multiplication:
$$
\pi_\omega(a)[b] := [ab].
$$
Well-definedness uses, again, that $\mathcal{N}_\omega$ is a left ideal. Boundedness: $\|\pi_\omega(a) [b]\|^2 = \omega(b^* a^* a b) \le \|a\|^2 \omega(b^* b) = \|a\|^2 \|[b]\|^2$, so $\pi_\omega(a)$ extends uniquely to a bounded operator on $\mathcal{H}_\omega$ with $\|\pi_\omega(a)\| \le \|a\|$.

Linearity, multiplicativity, and the \*-property $\pi_\omega(a^*) = \pi_\omega(a)^*$ are direct calculations.

**Step 5: identify the cyclic vector.** Let $\Omega_\omega := [1] \in \mathcal{A}/\mathcal{N}_\omega \subset \mathcal{H}_\omega$. Then:
- $\|\Omega_\omega\|^2 = \omega(1^* \cdot 1) = \omega(1) = 1$, so $\Omega_\omega$ is a unit vector.
- $\pi_\omega(a) \Omega_\omega = [a]$ for all $a$, so $\pi_\omega(\mathcal{A}) \Omega_\omega = \mathcal{A}/\mathcal{N}_\omega$, which is dense in $\mathcal{H}_\omega$ by construction. Hence $\Omega_\omega$ is cyclic.
- $\langle \Omega_\omega, \pi_\omega(a) \Omega_\omega \rangle = \langle [1], [a] \rangle = \omega(1^* a) = \omega(a)$. $\square$

We have proved:

**Theorem 7.1 (GNS). [Proved — see §7.1 construction above.]** *For any state $\omega$ on a unital C\*-algebra $\mathcal{A}$, there exists a Hilbert space $\mathcal{H}_\omega$, a \*-representation $\pi_\omega : \mathcal{A} \to \mathcal{B}(\mathcal{H}_\omega)$, and a cyclic unit vector $\Omega_\omega \in \mathcal{H}_\omega$ such that $\omega(a) = \langle \Omega_\omega, \pi_\omega(a) \Omega_\omega\rangle$ for all $a$.*

### 7.3 Uniqueness

**Theorem 7.2 (Uniqueness of GNS). [Proved.]** *Suppose $(\pi, \mathcal{H}, \Omega)$ is any \*-representation with cyclic unit vector $\Omega$ such that $\omega(a) = \langle \Omega, \pi(a) \Omega\rangle$. Then there is a unique unitary $U : \mathcal{H}_\omega \to \mathcal{H}$ such that $U \Omega_\omega = \Omega$ and $U \pi_\omega(a) U^{-1} = \pi(a)$ for all $a$.*

**Proof.** Define $U$ on the dense subspace $\pi_\omega(\mathcal{A}) \Omega_\omega$ by $U \pi_\omega(a)\Omega_\omega := \pi(a) \Omega$. To show this is well-defined and isometric, compute:
$$
\langle \pi(a)\Omega, \pi(b)\Omega \rangle_{\mathcal{H}} = \langle \Omega, \pi(a^* b) \Omega \rangle = \omega(a^* b) = \langle \Omega_\omega, \pi_\omega(a^* b) \Omega_\omega \rangle = \langle \pi_\omega(a) \Omega_\omega, \pi_\omega(b) \Omega_\omega \rangle.
$$
So $U$ extends to an isometry $\mathcal{H}_\omega \to \mathcal{H}$. Surjectivity: $U(\pi_\omega(\mathcal{A}) \Omega_\omega) = \pi(\mathcal{A}) \Omega$, which is dense in $\mathcal{H}$ by cyclicity of $\Omega$. The intertwining property is direct. $\square$

This uniqueness justifies calling $(\pi_\omega, \mathcal{H}_\omega, \Omega_\omega)$ "the" GNS representation.

**Remark 7.2a (faithfulness of the representation).** The GNS representation need not be injective: $\ker \pi_\omega = \{a : \omega(b^* a^* a\, b) = 0 \ \forall b\}$ can be a nonzero two-sided ideal. If $\omega$ is faithful ($\omega(a^*a) = 0 \Rightarrow a = 0$), then $\pi_\omega$ is injective, and since an injective \*-homomorphism of C\*-algebras is automatically isometric (a consequence of Corollary 4.4: both norms compute the same spectral radius), $\pi_\omega$ embeds $\mathcal{A}$ isometrically into $\mathcal{B}(\mathcal{H}_\omega)$. This is the mechanism behind the Gelfand–Naimark Theorem 5.2: take a separating family of states $\{\omega_i\}$ (one exists by Hahn–Banach), form $\bigoplus_i \pi_{\omega_i}$, and the direct sum is injective, hence isometric. The abstract-versus-concrete distinction for C\*-algebras thus evaporates — which is why we will move freely between the two pictures all course.

### 7.4 Pure states and irreducible representations

**Theorem 7.3. [Stated only — refs: Bratteli–Robinson Vol. I §2.3.8; proof uses Schur's lemma in vN-algebra form.]** *The GNS representation $\pi_\omega$ is irreducible if and only if $\omega$ is pure.*

(A representation is irreducible if it has no closed invariant subspaces other than $\{0\}$ and the whole space.) The proof uses Schur's lemma in von Neumann algebra form; we will not give it here.

This is a clean structural correspondence: pure states ↔ irreducible representations. In the commutative case (Example 6.4), pure states are points $x \in X$, and the corresponding irreducible representations are 1-dimensional, given by $\pi_x(f) = f(x) \in \mathbb{C}$. In the non-commutative case, irreducible representations can be arbitrarily large.

## 8. Worked examples of GNS

### 8.1 Vector states on $\mathcal{B}(\mathcal{H})$

Let $\mathcal{A} = \mathcal{B}(\mathcal{H})$ with $\mathcal{H}$ a Hilbert space, and let $\omega_\xi(a) = \langle \xi, a \xi\rangle$ for a unit vector $\xi \in \mathcal{H}$.

Identifying the GNS data: take $\mathcal{H}_\omega = \mathcal{H}$, $\pi_\omega = \mathrm{id}$, $\Omega_\omega = \xi$. The cyclicity of $\xi$ is automatic when $\xi$ is a *cyclic* vector for $\mathcal{B}(\mathcal{H})$, which it is whenever $\mathcal{H}$ is the closed span of $\mathcal{B}(\mathcal{H}) \xi = \mathcal{H}$ — trivially true. So GNS recovers the original Hilbert space.

If $\xi$ is not cyclic for $\mathcal{B}(\mathcal{H})$ (impossible for $\mathcal{B}(\mathcal{H})$ acting on the whole space, but possible for sub-algebras), then $\mathcal{H}_\omega$ is the cyclic subspace $\overline{\pi(\mathcal{A}) \xi}$.

### 8.2 The tracial state on $M_2(\mathbb{C})$

Let $\mathcal{A} = M_2(\mathbb{C})$ and $\tau(a) = \frac{1}{2} \mathrm{Tr}(a)$. We construct GNS explicitly.

**Sesquilinear form.** For $a, b \in M_2(\mathbb{C})$:
$$
\langle a, b\rangle_\tau = \tau(a^* b) = \frac{1}{2} \mathrm{Tr}(a^* b).
$$
This is the (rescaled) Hilbert–Schmidt inner product.

**Null space.** $\tau(a^* a) = \frac{1}{2} \sum_{i,j} |a_{ij}|^2 = 0$ implies $a = 0$. Hence $\mathcal{N}_\tau = \{0\}$.

**Hilbert space.** $\mathcal{H}_\tau = M_2(\mathbb{C})$ with the inner product $\langle a, b\rangle_\tau = \frac{1}{2} \mathrm{Tr}(a^* b)$. As a Hilbert space, $\mathcal{H}_\tau \cong \mathbb{C}^4$.

**Representation.** $\pi_\tau(a)$ acts on $\mathcal{H}_\tau$ by left multiplication. As an operator on $\mathbb{C}^4 \cong \mathbb{C}^2 \otimes \mathbb{C}^2$, it acts as $a \otimes 1$.

**Cyclic vector.** $\Omega_\tau = 1 \in M_2(\mathbb{C})$. Identifying $1$ with $\frac{1}{\sqrt 2}(|0\rangle\otimes|0\rangle + |1\rangle\otimes|1\rangle) \in \mathbb{C}^2 \otimes \mathbb{C}^2$, this is exactly the maximally entangled Bell state on a doubled system.

The GNS representation of the tracial state is "left multiplication" on the algebra, regarded as a Hilbert space via Hilbert–Schmidt; the cyclic vector is the maximally entangled state on the doubled Hilbert space. This will reappear in Week 6 as the prototype for KMS states and modular theory: $\Omega_\tau$ is *both cyclic and separating* for $\pi_\tau(M_2(\mathbb{C}))$, and the modular operator turns out to be the identity (the state is tracial). The tracial structure is the toy model for type $\mathrm{II}$ algebras.

### 8.3 A point-evaluation state on $C(X)$

Let $\mathcal{A} = C(X)$ for $X$ compact Hausdorff, and pick $x_0 \in X$. The state $\omega = \delta_{x_0}$ is $\omega(f) = f(x_0)$.

**Null space.** $\omega(f^* f) = |f(x_0)|^2 = 0$ iff $f(x_0) = 0$. So $\mathcal{N}_\omega = \{f : f(x_0) = 0\}$ — a maximal ideal of codimension 1 in $C(X)$.

**Quotient.** $C(X)/\mathcal{N}_\omega \cong \mathbb{C}$ via $f \mapsto f(x_0)$.

**Hilbert space.** $\mathcal{H}_\omega = \mathbb{C}$.

**Representation.** $\pi_\omega(f) = f(x_0) \cdot 1$ on $\mathbb{C}$. 1-dimensional, irreducible. (Consistent with Theorem 7.3: $\delta_{x_0}$ is a pure state.)

**Cyclic vector.** $\Omega_\omega = 1 \in \mathbb{C}$.

The whole representation collapses to the evaluation map $f \mapsto f(x_0)$. This illustrates how, in commutative algebras, GNS tends to be "degenerate" — irreducible representations are 1-dimensional. The interesting examples are non-commutative.

### 8.4 A non-pure state on $M_2(\mathbb{C})$ (preview of type $\mathrm{II}$)

Recall the Pauli matrices $\sigma_x, \sigma_y, \sigma_z$. Consider the state $\omega(a) = \frac{1}{2}\langle e_1, a e_1\rangle + \frac{1}{2}\langle e_2, a e_2\rangle = \frac{1}{2}\mathrm{Tr}(a) = \tau(a)$. We already constructed this in §8.2.

Note that this state is *not pure* — it is the average of the two pure vector states $\omega_{e_1}$ and $\omega_{e_2}$, where $e_1, e_2$ are the standard basis vectors. Yet by Theorem 7.3 the corresponding GNS representation is reducible. Indeed, the Hilbert space $\mathcal{H}_\tau \cong \mathbb{C}^4$ decomposes under $\pi_\tau$ as $\mathbb{C}^2 \oplus \mathbb{C}^2$ (left multiplication by $a$ acts on each column independently), with $\pi_\tau(a)$ acting as $a$ on each $\mathbb{C}^2$.

This decomposition is the explicit construction underlying the *type $\mathrm{II}_1$ structure*: two copies of the irreducible representation glued together by the trace. In this finite-dimensional case the pieces are visible; in the genuinely $\mathrm{II}_1$ case (e.g., the hyperfinite $\mathrm{II}_1$ factor, Week 3) the decomposition is "continuous" and the algebra is genuinely non-trivially type $\mathrm{II}$.

## 9. What to take away

Three structural facts run the rest of the course:

1. **The algebraic framework.** Observables form a C\*-algebra; states are positive normalized linear functionals; everything is defined without picking a Hilbert space first.

2. **GNS is the bridge.** Any state on any C\*-algebra produces a canonical Hilbert space representation. This is how we move between the algebraic and the Hilbert-space pictures whenever convenient.

3. **The non-commutativity is the physics.** In commutative algebras (classical probability), pure states are points; states are probability measures; everything is determined by an underlying space. In non-commutative algebras (quantum), pure states are vectors in a representation; the representation depends on the state (different states can give *non-equivalent* GNS representations). This is the source of all subtlety in QFT, including the type-III phenomena we will meet in Block C.

## 10. Looking ahead: Week 2

Next week we strengthen "C\*-algebra" to "von Neumann algebra" by closing in the weak operator topology rather than the norm topology. The price is that von Neumann algebras come with a representation built in (you cannot define a vN algebra abstractly the way you can a C\*-algebra without losing information). The benefit is a much richer structure: every vN algebra has a wealth of projections that generate it, and the order structure on projections leads to the Murray–von Neumann classification (Week 3). Tomita–Takesaki (Block B) and the type-III classification of QFT algebras (Block C) all live in the von Neumann setting.

## 11. Problem set

**Core problems** (everyone).

**1. Banach-algebra warm-ups.**
(a) Show that in any Banach algebra, the spectrum of $a$ is contained in the closed disk of radius $\|a\|$ centered at $0$. Where does completeness enter?
(b) Show that for $a \in M_n(\mathbb{C})$, the spectrum coincides with the set of eigenvalues, and the spectral radius $r(a)$ equals $\max\{|\lambda| : \lambda \text{ eigenvalue}\}$.

**2. Unitization (a hands-on encounter with the non-unital case).**
Let $\mathcal{A}$ be a non-unital Banach \*-algebra. Define $\widetilde{\mathcal{A}} = \mathcal{A} \oplus \mathbb{C}$ as a vector space, with multiplication $(a, \lambda)(b, \mu) = (ab + \lambda b + \mu a, \lambda \mu)$ and involution $(a, \lambda)^* = (a^*, \overline\lambda)$.
(a) Verify that $\widetilde{\mathcal{A}}$ is a unital \*-algebra and embed $\mathcal{A}$ into it as $a \mapsto (a, 0)$.
(b) Show that with the norm $\|(a,\lambda)\| = \|a\| + |\lambda|$, $\widetilde{\mathcal{A}}$ is a unital Banach \*-algebra.
(c) (Harder.) When $\mathcal{A}$ is a C\*-algebra, the norm in (b) does *not* give $\widetilde{\mathcal{A}}$ the C\*-property in general. Find the correct norm by interpreting elements of $\widetilde{\mathcal{A}}$ as operators on $\mathcal{A}$ via $(a,\lambda) \cdot b := ab + \lambda b$. (Hint: think of $\widetilde{\mathcal{A}}$ inside $\mathcal{B}(\mathcal{A})$.)

**3. The C\*-identity has teeth.**
(a) Show that in a C\*-algebra, $\|a\|^2 = \|a^* a\| = \|a a^*\|$.
(b) Deduce that if $a$ is normal, then $\|a^n\| = \|a\|^n$ and hence $r(a) = \|a\|$.
(c) Use (b) to show that the spectrum of a unitary lies in the unit circle.

**4. GNS for the tracial state, completed.**
(a) Verify all the steps in §8.2: that $\mathcal{N}_\tau = 0$, that the Hilbert space is the rescaled Hilbert–Schmidt space, that left multiplication is bounded with $\|\pi_\tau(a)\| = \|a\|$ (operator norm).
(b) Show that the cyclic vector $\Omega_\tau$ is *also* cyclic for the *commutant* $\pi_\tau(M_2(\mathbb{C}))'$ — i.e., it is *cyclic and separating*. (The commutant $\pi_\tau(M_2(\mathbb{C}))'$ acts on $\mathcal{H}_\tau$ by *right* multiplication.)
(c) Compute the modular conjugation $J : \mathcal{H}_\tau \to \mathcal{H}_\tau$ defined by $J [a] = [a^*]$. Verify that $J$ is anti-unitary, $J^2 = 1$, and $J \pi_\tau(a) J = \pi_\tau(a^*)^*$ — the "right multiplication" form. (This is a preview of Tomita–Takesaki, Week 5, in the simplest possible case where the modular operator is trivial.)

**Starred problems** (Ph.D. expected; ambitious M.Sc. encouraged).

**5\*. Pure states are vector states (the easy direction).**
Let $\xi \in \mathcal{H}$ be a unit vector and $\omega_\xi(a) = \langle \xi, a \xi\rangle$ on $\mathcal{B}(\mathcal{H})$. Show $\omega_\xi$ is pure.
(*Hint:* if $\omega_\xi = t \omega_1 + (1-t) \omega_2$, the first task is to show that $\omega_1$ and $\omega_2$ are also vector states, by writing them as $\omega_i(a) = \mathrm{Tr}(\rho_i a)$ for positive trace-class $\rho_i$ summing to the rank-one projection onto $\xi$.)

**6\*. A non-pure state and its GNS decomposition.**
Take $\omega = \frac{1}{2} \omega_{e_1} + \frac{1}{2} \omega_{e_2}$ on $M_2(\mathbb{C})$ as in §8.4.
(a) Compute the GNS representation of $\omega$ explicitly and identify the decomposition into two copies of the defining representation.
(b) Find the projection in $\pi_\omega(M_2(\mathbb{C}))'$ (the commutant) onto the first copy.
(c) Discuss: how does this 2-fold decomposition reflect that $\omega$ is the equal-weights mixture of two pure states? Generalize to $\omega = \sum_i p_i \omega_{e_i}$ with $\sum p_i = 1$.

**7\*\* (Optional, very hard).** Prove that every state on a C\*-algebra is bounded with norm 1 (i.e., $\sup_{\|a\| \le 1} |\omega(a)| = 1$), using only the positivity and normalization axioms. (*Hint:* the key step is to control $|\omega(a)|^2 \le \omega(a^* a)$ via Cauchy–Schwarz, then iterate using $a^* a$ self-adjoint and $\|a^*a\| = \|a\|^2$.)

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block A. Last revised 2026-06-11.*
