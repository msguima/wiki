---
title: "Appendix A — Functional-Analysis Survival Kit"
type: appendix
course: syllabus
modified: 2026-09-29
---

# Functional-Analysis Survival Kit

This appendix collects the analytic facts used repeatedly in the course. It is **not a replacement** for a functional-analysis course. It is the minimum toolkit a student needs in order to read the lecture notes without stopping every page.

## A.1 Hilbert-Space Conventions

Inner products are linear in the *second* slot:
$$
\langle \xi, \lambda\eta\rangle = \lambda\langle\xi, \eta\rangle, \qquad \langle \lambda\xi, \eta\rangle = \overline{\lambda}\langle\xi, \eta\rangle.
$$
For a bounded operator $T$ on a Hilbert space $\mathcal{H}$, the adjoint $T^*$ is defined by $\langle\xi, T\eta\rangle = \langle T^*\xi, \eta\rangle$.

Key classes:
- $T$ is **self-adjoint** if $T = T^*$.
- $T$ is **positive** if $\langle\xi, T\xi\rangle \ge 0$ for all $\xi$.
- $U$ is **unitary** if $U^*U = UU^* = 1$.
- $P$ is a **projection** if $P = P^* = P^2$.

When $P$ is a projection, $P\mathcal{H}$ is a closed subspace; every closed subspace has an orthogonal projection.

## A.2 Bounded and Unbounded Operators

The course mostly uses bounded operator algebras, but QFT fields are unbounded before smearing or exponentiation.

A **bounded operator** $T$ satisfies $\|T\xi\| \le C\|\xi\|$ for all $\xi$; the smallest such $C$ is the operator norm $\|T\|$.

An **unbounded operator** $A$ is a pair $(A, \mathrm{Dom}\,A)$ where $\mathrm{Dom}\,A$ is a dense subspace and $A$ is linear on it. Domain questions matter for fields $\phi(f)$ and for logarithms like $\log\Delta$, but the von Neumann algebra itself is built from *bounded* operators.

**Course rule:**
- Use unbounded fields as motivation and for formal calculations.
- Use bounded Weyl operators $W(f) = e^{i\phi(f)}$, spectral projections, modular unitaries $\Delta^{-it}$, and von Neumann algebras for exact algebraic statements.

### A.2.1 Graphs, closedness, and closability

For an unbounded operator, the formula for the action is only half of the
definition. The domain is part of the operator. Thus two operators can act by
the same differential expression and still be different because their
domains, boundary conditions, or closures differ.

The **graph** of $A$ is
$$
\Gamma(A):=\{(\xi,A\xi):\xi\in\operatorname{Dom}A\}
\subset\mathcal H\oplus\mathcal H.
$$
The operator is **closed** when $\Gamma(A)$ is closed. Equivalently, whenever
$\xi_n\to\xi$ and $A\xi_n\to\eta$, one has
$\xi\in\operatorname{Dom}A$ and $A\xi=\eta$.

The operator is **closable** when the closure of its graph is still the graph
of an operator, denoted $\overline A$. The practical test is
$$
\xi_n\to0,\qquad A\xi_n\to\eta
\quad\Longrightarrow\quad
\eta=0.
$$
If this implication failed, the closed graph would assign both $0$ and
$\eta\ne0$ to the zero vector, so it could not define an operator.

> **Physical picture.** Closing an operator adds limits that were already
> forced by the original action. It does not choose arbitrary new boundary
> conditions. In Week 5 the preliminary Tomita map $S_0$ is first defined on
> the algebraic domain $\mathcal M\Omega$. Proving that $S_0$ is closable is
> what licenses the closed operator $S=\overline{S_0}$ and hence its polar
> decomposition. Writing $S=J\Delta^{1/2}$ before that step would hide the
> main domain question.

### A.2.2 Adjoints, including conjugate-linear operators

For a densely defined linear operator $A$, a vector
$\eta$ belongs to $\operatorname{Dom}A^*$ when there is a vector $\zeta$ such
that
$$
\langle\eta,A\xi\rangle=\langle\zeta,\xi\rangle
\qquad
\text{for every }\xi\in\operatorname{Dom}A.
$$
Then $A^*\eta:=\zeta$. The representing vector is unique because the domain
of $A$ is dense. The adjoint is always closed, and a densely defined linear
operator is closable exactly when $\operatorname{Dom}A^*$ is dense; in that
case $\overline A=A^{**}$.

The Tomita map is **conjugate-linear**. With the course convention that the
inner product is linear in its second slot, the conjugate-linear adjoint is
defined by
$$
\langle\eta,S\xi\rangle
=\langle\xi,S^*\eta\rangle.
$$
This reversal of the two vectors is not decoration: importing the
linear-adjoint formula without changing it produces the wrong conjugations.
Week 5 carries out the Tomita calculation in this convention.

### A.2.3 Graph norm and cores

On $\operatorname{Dom}A$, define the **graph norm**
$$
\|\xi\|_A
:=\big(\|\xi\|^2+\|A\xi\|^2\big)^{1/2}.
$$
The operator $A$ is closed exactly when its domain is complete in this norm.
A subspace $\mathcal D_0\subset\operatorname{Dom}A$ is a **core** for $A$ if
it is graph-norm dense in $\operatorname{Dom}A$. Equivalently, closing the
restriction $A|_{\mathcal D_0}$ recovers $A$.

This is the precise meaning of statements such as “prove the identity first
on $\mathcal M\Omega$ and then extend by closure.” Ordinary Hilbert-space
density is not enough: one must approximate both $\xi$ and $A\xi$.

### A.2.4 A domain checklist

Before manipulating unbounded operators, ask:

1. What is the domain of each operator?
2. Is the proposed product defined on a dense common domain?
3. Is the operator closed or at least closable?
4. Is the identity being proved on a core, or only on an unspecified dense
   set?
5. Does the functional calculus use a bounded function, or is a new domain
   required?

The bounded modular unitaries $\Delta^{it}$ are defined everywhere even when
$\Delta$ and $\log\Delta$ are unbounded. This is why exact modular-flow
statements are normally written with $\Delta^{it}$, while entropy expressions
involving $\log\Delta$ carry explicit domain or integrability conditions.

## A.3 The Spectral Theorem

If $A=A^*$ is self-adjoint, there is a projection-valued measure $E_A$ on
$\mathbb R$ such that
$$
A = \int_{\mathbb{R}} \lambda\, dE_A(\lambda), \qquad f(A) = \int_{\mathbb{R}} f(\lambda)\, dE_A(\lambda)
$$
for bounded Borel $f$; unbounded Borel functions are also allowed on their
natural domains. If a symmetric operator is only **essentially**
self-adjoint, this theorem applies to its unique self-adjoint closure. The
spectrum is
$\sigma(A)=\{\lambda\in\mathbb R:E_A(B)\ne0\text{ for every open }B\ni
\lambda\}$.

**Used throughout the course for:**
- $\rho^{it}$ via $\rho > 0$, $\rho^{it} = e^{it\log\rho}$ (functional calculus).
- $\Delta^{-it}$ via $\Delta$ positive self-adjoint.
- $e^{-\beta H}$ for the Gibbs density.
- $K_{\mathrm{GNS}}=-\log\Delta$ as the modular Hamiltonian on standard
  form, with $\log\Delta$ itself appearing in relative-entropy formulas.

## A.4 Topologies on $\mathcal{B}(\mathcal{H})$

We use four topologies. They are written with sequences for readability;
nets are required for the general topological statements.

**Norm topology.** $T_i\to T$ iff $\|T_i-T\|\to0$. Strongest of the four.

**Strong operator topology (SOT).** $T_i\to T$ iff $T_i\xi\to T\xi$ for every
$\xi\in\mathcal H$. It is weaker than norm (and strictly weaker in infinite
dimension).

**Weak operator topology (WOT).** $T_i\to T$ iff
$\langle\eta,T_i\xi\rangle\to\langle\eta,T\xi\rangle$ for every
$\xi,\eta$. It is weaker than SOT.

**$\sigma$-weak (ultraweak) topology.** $T_i\to T$ iff
$\operatorname{Tr}(CT_i)\to\operatorname{Tr}(CT)$ for every trace-class
$C$. On norm-bounded subsets of $\mathcal B(\mathcal H)$ it agrees with WOT;
as a topology on the whole space it is finer. It is the weak-* topology
defined by the predual and therefore the natural topology for normal
functionals.

A **von Neumann algebra** is a unital $*$-subalgebra of $\mathcal{B}(\mathcal{H})$ closed in WOT (equivalently, SOT, equivalently $\sigma$-weak). Norm-closure gives only a C\*-algebra, not generally a vN algebra. The equivalence concerns which \*-algebras are closed: for a unital \*-algebra all three closures equal the bicommutant (Week 2, Theorem 4.1 and §4.2), while the three topologies themselves remain different. Week 2 §3 explains why the definition is stated with WOT.

*Physical reading (Week 2 §2):* norm convergence controls all unit-vector
matrix elements uniformly, whereas WOT tests each chosen pair of vectors. The
comparison is operationally suggestive, but WOT closure should not be defined
as "what no experiment can distinguish": finite experimental precision is a
different notion. Mathematically, WOT closure supplies the spectral
projections and bounded limits needed for an algebra of observables.

**Key fact (Sakai).** A C\*-algebra $\mathcal{A}$ is \*-isomorphic to a vN algebra iff it has a predual: there is a Banach space $\mathcal{A}_*$ with $\mathcal{A} = (\mathcal{A}_*)^*$. Such C\*-algebras are called W\*-algebras. The definition above is concrete, but the $\sigma$-weak topology and the normal states are intrinsic to the algebra and do not depend on the chosen faithful normal representation.

## A.5 States, Normal States, Predual

A **state** on a C\*-algebra $\mathcal{A}$ is a positive linear functional $\omega: \mathcal{A} \to \mathbb{C}$ with $\omega(1) = 1$.

A state $\omega$ on a vN algebra $\mathcal{M}$ is **normal** if it is $\sigma$-weakly continuous; equivalently if it is order-continuous: $\omega(\sup_\alpha a_\alpha) = \sup_\alpha \omega(a_\alpha)$ for increasing nets of positive operators.

The predual $\mathcal{M}_*$ is the space of normal linear functionals; $\mathcal{M} = (\mathcal{M}_*)^*$.

**For $\mathcal M=\mathcal B(\mathcal H)$:**
$\mathcal M_*\cong\mathcal T(\mathcal H)$, and every normal state is represented
by a unique trace-class density operator. General type-I von Neumann algebras
have the corresponding direct-integral version of this statement.

**For type III:** $\mathcal M_*$ is still the Banach space of normal
functionals, but there is no intrinsic density $h\in\mathcal M$ relative to a
faithful normal semifinite trace, because no such trace exists. In a concrete
embedding $\mathcal M\subset\mathcal B(\mathcal H)$ a normal functional may be
extended and represented by an ambient trace-class operator; that
representation is nonunique and is not a reduced density matrix belonging to
the local algebra.

### A.5.1 Weights and semifiniteness

A **weight** on a von Neumann algebra $\mathcal M$ is a map
$$
\varphi:\mathcal M_+\longrightarrow[0,+\infty]
$$
that is additive and positively homogeneous on the positive cone. A state is
a finite normalized weight; the point of allowing $+\infty$ is that an
infinite algebra may have a useful integration theory without a finite trace.

The weight is:

- **faithful** if $x\geq0$ and $\varphi(x)=0$ imply $x=0$;
- **normal** if $x_i\uparrow x$ implies
  $\varphi(x_i)\uparrow\varphi(x)$ for increasing nets in $\mathcal M_+$;
- **semifinite** if, for every $x\in\mathcal M_+$,
  $$
  \varphi(x)=\sup\{\varphi(y):0\leq y\leq x,
  \ \varphi(y)<\infty\};
  $$
- **tracial** if $\varphi(u^*xu)=\varphi(x)$ for every unitary
  $u\in\mathcal M$ and $x\in\mathcal M_+$.

Thus a faithful normal semifinite trace is an invariant integration rule that
is locally finite on enough positive elements, even when $\tau(1)=+\infty$.
Type III factors admit faithful normal weights but no faithful normal
semifinite trace. Their continuous cores do admit such a trace.

### A.5.2 Affiliated and measurable operators

A closed densely defined operator $T$ is **affiliated** with $\mathcal M$ if
it commutes with the commutant in the domain-sensitive sense
$$
u'T\subset Tu'
\qquad\text{for every unitary }u'\in\mathcal M'.
$$
For self-adjoint $T$, this is equivalent to requiring all spectral
projections of $T$ to lie in $\mathcal M$. Affiliation is the correct meaning
of saying that an unbounded observable or density “belongs to” a von Neumann
algebra.

Given a faithful normal semifinite trace $\tau$, an affiliated operator $T$
is **$\tau$-measurable** when its domain is $\tau$-dense: for every
$\epsilon>0$ there is a projection $e\in\mathcal M$ such that
$$
e\mathcal H\subset\operatorname{Dom}T,
\qquad \tau(1-e)<\epsilon.
$$
The noncommutative space $L^1(\mathcal M,\tau)$ consists of the appropriate
$\tau$-measurable affiliated operators with finite trace norm. A normal state
on a semifinite algebra has a positive density $h\in L^1(\mathcal M,\tau)$
with $\tau(h)=1$; $h$ need not be a bounded element of $\mathcal M$. This is
the setting of the core densities and entropies used in Weeks 13--14.

## A.6 GNS Construction (Recap from Week 1)

Given a state $\omega$ on a C\*-algebra $\mathcal{A}$:
1. The sesquilinear form $\langle a, b\rangle_\omega := \omega(a^*b)$ on $\mathcal{A}$ is positive semi-definite.
2. Quotient by the null space $\mathcal{N}_\omega = \{a: \omega(a^*a) = 0\}$ to get a pre-Hilbert space $\mathcal{A}/\mathcal{N}_\omega$.
3. Complete to a Hilbert space $\mathcal{H}_\omega$.
4. Left multiplication by $\mathcal{A}$ defines a $*$-representation $\pi_\omega: \mathcal{A} \to \mathcal{B}(\mathcal{H}_\omega)$.
5. The image of $1 \in \mathcal{A}$ is a cyclic vector $\Omega_\omega \in \mathcal{H}_\omega$ with $\omega(a) = \langle\Omega_\omega, \pi_\omega(a)\,\Omega_\omega\rangle$.

The GNS triple $(\mathcal{H}_\omega, \pi_\omega, \Omega_\omega)$ is unique up to unitary equivalence.

If the normal extension of $\omega$ to
$\pi_\omega(\mathcal A)''$ is faithful, then $\Omega_\omega$ is separating
for that von Neumann algebra, and conversely. Faithfulness on the original
C*-algebra makes $\pi_\omega$ faithful but should not be substituted silently
for faithfulness of the normal extension.

The state is **factorial** when $\pi_\omega(\mathcal A)''$ has trivial center.
This is weaker than irreducibility: an irreducible representation has
$\pi_\omega(\mathcal A)'=\mathbb C1$, hence
$\pi_\omega(\mathcal A)''=\mathcal B(\mathcal H_\omega)$, whereas a type II or
type III factor representation is factorial but not irreducible in this
sense. Pure states, not general factorial states, give irreducible GNS
representations.

## A.7 Trace-Class and Hilbert–Schmidt Operators

The **Hilbert–Schmidt** operators $\mathcal{HS}(\mathcal{H})$ are those with $\sum_i \|Te_i\|^2 < \infty$ for any orthonormal basis. They form a two-sided ideal in $\mathcal{B}(\mathcal{H})$.

The **trace-class** operators $\mathcal{T}(\mathcal{H})$ are those with $\sum_i \langle e_i, |T|\,e_i\rangle < \infty$. They form a two-sided ideal in $\mathcal{B}(\mathcal{H})$ and $\mathcal{T}(\mathcal{H}) \subset \mathcal{HS}(\mathcal{H}) \subset \mathcal{K}(\mathcal{H})$ (compact) $\subset \mathcal{B}(\mathcal{H})$.

The trace $\mathrm{Tr}: \mathcal{T}(\mathcal{H}) \to \mathbb{C}$ is the standard sum-of-diagonal-entries, basis-independent.

**In Week 7 §3**: the Hilbert–Schmidt space $\mathcal{HS}(\mathcal{H}) = M_n(\mathbb{C})$ (finite-dim case) is used as the GNS Hilbert space for type-I states, with left multiplication as the representation. This is the natural setting for explicit modular-operator and relative-modular-operator computations.

## A.8 Tensor Products

The **algebraic tensor product** $\mathcal{H}_1 \otimes_{\mathrm{alg}} \mathcal{H}_2$ has a natural inner product $\langle\xi_1\otimes\xi_2, \eta_1\otimes\eta_2\rangle = \langle\xi_1,\eta_1\rangle\langle\xi_2,\eta_2\rangle$. Completing gives the **Hilbert-space tensor product** $\mathcal{H}_1 \otimes \mathcal{H}_2$.

For vN algebras: $\mathcal{M}_1 \overline\otimes \mathcal{M}_2$ is the **spatial tensor product**, the WOT-closure of $\mathcal{M}_1 \otimes_{\mathrm{alg}} \mathcal{M}_2$ on $\mathcal{H}_1 \otimes \mathcal{H}_2$.

**Commutant theorem.** $(\mathcal{M}_1 \overline\otimes \mathcal{M}_2)' = \mathcal{M}_1' \overline\otimes \mathcal{M}_2'$ (this works in the spatial tensor product; abstract tensor products are more delicate).

In AQFT there is generally no canonical factorization
$\mathcal H=\mathcal H(\mathcal O)\otimes\mathcal H(\mathcal O')$ whose first
factor carries the bounded-region algebra. Type III local structure is one
way this failure becomes visible. Under the split property, **strictly
separated** regions admit an intermediate type-I factor and a corresponding
tensor-product implementation; this does not create a sharp tensor split
between a region and its touching causal complement. Type-I regulators also
permit tensor reasoning, with regulator dependence stated explicitly.

## A.9 Polar Decomposition

A closed densely-defined operator $T$ has a unique polar decomposition $T = V|T|$, where $|T| = (T^*T)^{1/2} \ge 0$ and $V$ is a partial isometry with initial space $\overline{\mathrm{ran}\,|T|}$ and final space $\overline{\mathrm{ran}\,T}$.

For conjugate-linear $T$ (e.g., the Tomita operator $S$), the same decomposition holds with $V$ antiunitary. In the cyclic-separating setting, $V$ extends to an antiunitary on the full Hilbert space — this is the modular conjugation $J$.

**Used in:**
- Tomita operator polar decomposition $S = J\Delta^{1/2}$ (Week 5 §3).
- Connes cocycle existence (Week 7 §4).

## A.10 Analytic Vectors and the Analytic Subalgebra

For a self-adjoint $A$ generating $U(t)=e^{itA}$, a vector
$\xi\in\bigcap_{n\ge0}\operatorname{Dom}(A^n)$ is **analytic** for $A$ if
$\sum_n |t|^n\|A^n\xi\|/n!<\infty$ for $|t|$ in some neighborhood of zero.
Every self-adjoint operator has a dense set of analytic vectors, for example
vectors with compact spectral support.

For such a vector the power series for $U(z)\xi$ converges locally in complex
$z$; entire analytic vectors have convergence for all $z$. Separately, an
element $a$ is analytic for an automorphism group $\alpha_t$ when
$t\mapsto\alpha_t(a)$ has the required complex continuation. These analytic
elements form the convenient dense subalgebra used in KMS arguments. The KMS
condition itself concerns analytic continuation of correlation functions and
does not say that every vector is analytic.

*Physical reading:* for a positive-energy Hamiltonian, spectral positivity
helps control Euclidean-time factors such as $e^{-\tau H}$. Modular generators
are generally not bounded below, so their strip analyticity comes instead
from the Tomita--Takesaki/KMS structure and the domains of powers of
$\Delta$. Thus a formal expression such as $\Delta^{1/2}a\Omega$ is licensed
by a domain or analytic-element statement, not by a generic Wick-rotation
rule.

## A.11 What's Used Where

| Topic | Used in |
|---|---|
| Spectral theorem | Throughout; especially Weeks 4, 5, 6 (modular operator), 10 (boost generator) |
| Bounded vs. unbounded | Weeks 8 (smeared fields), 5 (Tomita operator), 10 (boost) |
| Closed/closable operators, graph norms, cores | Week 5 (Tomita operator), Week 7 (relative modular operator) |
| Topologies (WOT/SOT) | Week 2 (vN algebra definition) |
| Predual / normal states | Weeks 2, 12 (type III; no density matrix as operator means via predual) |
| Weights, affiliation, $\tau$-measurability | Weeks 3, 13, 14 (semifinite traces and core densities) |
| GNS | Week 1 (foundation), all subsequent weeks |
| Trace-class | Week 7 (Hilbert–Schmidt GNS for type I) |
| Tensor products | Week 5 (type-I modular), Week 9 (no factorization for AQFT), Week 13 (crossed product on $\mathcal{H} \otimes L^2(\mathbb{R})$) |
| Polar decomposition | Week 5 (Tomita operator), Week 7 (Connes cocycle) |
| Analytic vectors | Weeks 4, 6, 14 (KMS strip analytic continuations) |

## A.12 Suggested Reading

For students who need a full functional-analysis text:

- Reed & Simon, *Methods of Modern Mathematical Physics*, Vol. I (functional analysis) and Vol. II (Fourier analysis, self-adjointness). The standard reference.
- Conway, *A Course in Functional Analysis*. More accessible introduction.
- Pedersen, *Analysis Now*. Compact alternative.

For operator algebras specifically:
- Murphy, *C\*-algebras and Operator Theory*. Friendly first text.
- Bratteli & Robinson Vol. I, ch. 2. Course's primary reference.
