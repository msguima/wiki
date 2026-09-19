---
title: "Week 1 — Conformal algebra and primary operators"
type: lecture-notes
course: syllabus
semester: 1
week: 1
block: A
duration: "4 hours (2 lectures × 2 hours)"
status: final
modified: 2026-08-25
---

# Week 1 — Conformal Algebra and Primary Operators

> *The course opens with kinematics. Before any AdS, any holography, we need the symmetry the boundary theory carries: conformal invariance. This week we solve the conformal Killing equation to find the generators, assemble them into the conformal algebra and recognise it as $\mathfrak{so}(d+1,1)$, define **primary** operators and their descendants, and derive what conformal symmetry alone fixes — the form of two-point functions and the unitarity bounds on dimensions. Everything here is group theory; dynamics waits for the OPE (Week 3). No operator-algebra machinery yet — that is a Semester II concern.*

## Learning goals

By the end of this week, a student can:

1. State the conformal-algebra commutators and identify each generator ($P_\mu, K_\mu, D, M_{\mu\nu}$) with a geometric transformation.
2. Explain why the $d\ge 3$ conformal algebra is $\mathfrak{so}(d,2)$ (Lorentzian) / $\mathfrak{so}(d+1,1)$ (Euclidean), and write the embedding-space realisation.
3. Distinguish quasi-primary from primary operators and write the finite + infinitesimal primary transformation law.
4. **Derive** the scalar two-point function $C_\mathcal{O}|x|^{-2\Delta}$ from the Ward identities.
5. **Derive** the level-1 descendant norm and state the unitarity bounds $\Delta\ge\tfrac{d-2}{2}$ (scalars), $\Delta\ge\ell+d-2$ ($\ell\ge1$), naming the saturating operators.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Modern CFT* §§3–5** — §3 for the conformal algebra and embedding space, §4 for primaries and Ward identities, §5 for the two-point function.
- Rychkov, *EPFL Lectures on CFT in $D\ge3$*, [arXiv:1601.05000](https://arxiv.org/abs/1601.05000), Ch. 1–2; §3 for the full unitarity-bound proof.
- Polchinski, *String Theory* Vol. 1, §2.1–2.2 — the conformal Killing equation.

**Prerequisites.** Standard QFT (Poincaré symmetry, free-field Wightman functions, reps of $\mathrm{SO}(1,d-1)$); Lie-algebra commutators and highest-weight reps.

**AQFT cross-reference.** None — Block A is purely kinematic. The von Neumann-algebra / modular machinery enters only in Semester II, where the *same* conformal symmetry reappears as the symmetry of a [[type-iii-von-neumann-algebras|type III$_1$]] boundary algebra.

**What these notes add.** adscft.org §§3–5 give the conformal algebra and the correlator constraints cleanly, and this note does not repeat them. What it adds is threefold: the four-family solution of the Killing equation done by *counting* rather than quoted, so the number $\tfrac{(d+1)(d+2)}{2}$ is earned; the embedding-space realisation written out far enough to see $\mathfrak{so}(d,2)$ — which is the AdS isometry group, and therefore the first structural fact of the whole course; and the two- and three-point functions derived in one continuous argument so that the exact place where the symmetry runs out, at four points, is visible. Read the site for breadth, this note for those three.

## 1. Conformal transformations

A conformal transformation preserves the metric up to a local scale: $g_{\mu\nu}(x)\to\Omega(x)^2 g_{\mu\nu}(x)$. Infinitesimally, $x^\mu\to x^\mu+\epsilon^\mu(x)$ is conformal iff $\epsilon$ solves the **conformal Killing equation**

$$
\boxed{\;\partial_\mu\epsilon_\nu+\partial_\nu\epsilon_\mu = \frac{2}{d}\,(\partial\!\cdot\!\epsilon)\,\delta_{\mu\nu}.\;}
$$

**Solving it for $d\ge3$.** Taking a further derivative and symmetrising shows $\partial_\mu\partial_\nu\partial_\rho\epsilon_\sigma=0$ for $d>2$: $\epsilon$ is at most **quadratic** in $x$. Matching the three polynomial orders to the equation gives exactly four families:

| order in $x$ | $\epsilon^\mu$ | transformation | generator | count |
|---|---|---|---|---|
| $0$ | $a^\mu$ | translation | $P_\mu$ | $d$ |
| $1$ (antisym.) | $\omega^\mu{}_\nu x^\nu$ | rotation | $M_{\mu\nu}$ | $\tfrac{d(d-1)}{2}$ |
| $1$ (trace) | $\lambda\,x^\mu$ | dilatation | $D$ | $1$ |
| $2$ | $2(b\!\cdot\!x)x^\mu - x^2 b^\mu$ | special conformal (SCT) | $K_\mu$ | $d$ |

Total $\tfrac{(d+1)(d+2)}{2}=\dim\mathfrak{so}(d+1,1)$. The finite SCT is

$$
x'^\mu = \frac{x^\mu - b^\mu x^2}{1 - 2\,b\!\cdot\!x + b^2 x^2} = I\big(I(x)-b\big),
$$

i.e. an **inversion** $I:x^\mu\mapsto x^\mu/x^2$, a translation by $-b$, and another inversion. Equivalently $K_\mu = I\,P_\mu\,I$. The inversion is the one conformal map not continuously connected to the identity, and it is the workhorse behind most CFT manipulations (and the Casimir map of Week 3).

> **Physical picture.** The count is not a coincidence of polynomial degrees. A conformal transformation is one that preserves angles, and in $d>2$ the demand that angles be preserved *everywhere* is so rigid that only finitely many transformations survive — you may translate, rotate, rescale, and invert-translate-invert, and nothing else. Two dimensions are the exception precisely because the Killing equation there becomes the Cauchy–Riemann equations, whose solutions are all holomorphic maps: infinitely many. That single fact is why $d=2$ carries Virasoro (Week 5) and why every other dimension carries only the finite algebra below. When you later hear that AdS$_3$/CFT$_2$ is "special", this is the root of it.

> **[Proved.]** the solution count, by directly solving the Killing equation ($\partial^3\epsilon=0$ for $d>2$). Exercise 2 asks for the $d=3$ case explicitly as a check, not as the missing step.

## 2. The conformal algebra

Acting on fields, the generators obey (Euclidean conventions):

$$
\begin{aligned}
&[D,P_\mu]=iP_\mu, \qquad [D,K_\mu]=-iK_\mu, \qquad [D,M_{\mu\nu}]=0,\\
&[K_\mu,P_\nu]=2i\big(\delta_{\mu\nu}D - M_{\mu\nu}\big),\\
&[M_{\mu\nu},P_\rho]=i\big(\delta_{\nu\rho}P_\mu-\delta_{\mu\rho}P_\nu\big),\qquad
[M_{\mu\nu},K_\rho]=i\big(\delta_{\nu\rho}K_\mu-\delta_{\mu\rho}K_\nu\big),\\
&[P_\mu,P_\nu]=[K_\mu,K_\nu]=0.
\end{aligned}
$$

The first line is the crucial structure: $D$ grades the algebra, $P_\mu$ raising and $K_\mu$ lowering the dilatation eigenvalue by one.

**Embedding-space realisation.** The cleanest way to see $\mathfrak{so}(d+1,1)$ is to linearise the action on a null cone in $\mathbb{R}^{d+1,1}$. Introduce coordinates $X^A=(X^+,X^-,X^\mu)$, $A=+,-,1,\dots,d$, with metric $ds^2 = -dX^+dX^- + dX^\mu dX_\mu$, and put the CFT on the projective null cone $X^2=0$, $X\sim\lambda X$, parametrised by $X^A=(X^+,X^-,X^\mu)=(1,\,x^2,\,x^\mu)$ (the "Poincaré section"). Rotations $L_{AB}=-L_{BA}$ of $\mathbb{R}^{d+1,1}$ then act as conformal transformations of $x$, under the identification

$$
L_{\mu\nu}=M_{\mu\nu},\quad
L_{\mu,+}=\tfrac12(P_\mu-K_\mu),\quad
L_{\mu,-}=\tfrac12(P_\mu+K_\mu),\quad
L_{+-}=D.
$$

Substituting these into the $\mathfrak{so}(d+1,1)$ relations $[L_{AB},L_{CD}]=i(\eta_{AD}L_{BC}+\eta_{BC}L_{AD}-\eta_{AC}L_{BD}-\eta_{BD}L_{AC})$ reproduces the conformal commutators above; for instance $[L_{\mu,-},L_{\nu,+}]$ unpacks to $[K_\mu,P_\nu]=2i(\delta_{\mu\nu}D-M_{\mu\nu})$ (**Exercise 5**). In Lorentzian signature the embedding space is $\mathbb{R}^{d,2}$ and the group is $\mathrm{SO}(d,2)$ — the *same* group whose isometries act on $\mathrm{AdS}_{d+1}$, the first structural hint of the duality.

> **Physical picture.** Stop on that last sentence, because it is the single most important observation in Block A. The symmetry group of a $d$-dimensional CFT and the isometry group of a $(d{+}1)$-dimensional anti-de Sitter space are *the same group*, $\mathrm{SO}(d,2)$. Nothing has been assumed about holography to get this — it is a statement about two independent pieces of geometry that happen to coincide. The duality does not create this match; it explains it, by saying the two descriptions are of one system. Everything in Semester I after Week 6 is the work of turning a coincidence of symmetry groups into a dictionary between observables. Note also what the embedding does operationally: it linearises the action. Conformal transformations act non-linearly on $x^\mu$ and horribly on correlators, but they are plain rotations on the null cone, which is why embedding space is where the messy identities become one-liners.

> **[Model proof.]** the isomorphism, by matching commutators under the embedding; one bracket is unpacked in the text and Exercise 5 asks for a second.

## 3. Primary and descendant operators

Diagonalise $D$: an operator at the origin has definite dimension if $[D,\mathcal{O}(0)]=i\Delta\,\mathcal{O}(0)$. Since $K_\mu$ lowers $\Delta$ and there is a floor (§5), every multiplet has a bottom.

- A **primary** $\mathcal{O}$ is annihilated by the lowering operator at the origin, $[K_\mu,\mathcal{O}(0)]=0$, transforming in an irrep $(\Delta,\ell)$ of $D\times\mathfrak{so}(d)$.
- **Descendants** are raised: $P_{\mu_1}\!\cdots P_{\mu_n}\mathcal{O}$ = derivatives $\partial_{\mu_1}\!\cdots\partial_{\mu_n}\mathcal{O}$, dimension $\Delta+n$.
- A **quasi-primary** transforms covariantly under the *global* group $\mathrm{SO}(d+1,1)$. In $d\ge3$ primary = quasi-primary; the distinction matters only in $d=2$, where the global $\mathrm{SL}(2)$ sits inside the infinite Virasoro (Week 5).

**Finite transformation law.** Under a conformal map $x\to x'$ with Jacobian factor $\Omega(x)=|\partial x'/\partial x|^{1/d}$, a scalar primary of dimension $\Delta$ transforms as

$$
\mathcal{O}(x)\ \to\ \Omega(x)^{-\Delta}\,\mathcal{O}(x'),
$$

with a spin rotation $R^\ell{}_{\ell'}$ adjoined for $\ell\ne0$. Infinitesimally this is $\delta\mathcal{O}=-(\epsilon\!\cdot\!\partial + \tfrac{\Delta}{d}\partial\!\cdot\!\epsilon)\mathcal{O}$ + (spin), the operator form of the generator action. A primary plus its descendants is an **irreducible, $D$-graded conformal multiplet**; the full operator content is a (generically infinite) sum of such multiplets — the spectrum.

> **Physical picture.** The structure is exactly a highest-weight representation, with $D$ playing the role energy plays in an ordinary Hamiltonian problem: $P_\mu$ raises it, $K_\mu$ lowers it, and unitarity supplies a floor so every tower has a bottom. What is unusual, compared with ordinary QFT, is that this organises the *entire* operator content — there is no separate "field content" and "bound-state spectrum", only primaries and their descendants. This is why a CFT is specified by a list of numbers, $\{(\Delta_i,\ell_i), C_{ijk}\}$, rather than by a Lagrangian, and why the bootstrap can hope to constrain theories with no Lagrangian at all. In the bulk, a primary will turn out to be a field and its dimension a mass (Week 8).

**That a derivative is never primary** takes three lines, so we do it rather than assert it. Writing $\partial_\nu\mathcal{O}(0) \propto [P_\nu,\mathcal{O}(0)]$ and acting with the lowering operator, the Jacobi identity gives
$$
\big[K_\mu,[P_\nu,\mathcal{O}(0)]\big] = \big[[K_\mu,P_\nu],\mathcal{O}(0)\big] + \big[P_\nu,[K_\mu,\mathcal{O}(0)]\big],
$$
where the second term vanishes because $\mathcal{O}$ is primary. Using $[K_\mu,P_\nu] = 2i(\delta_{\mu\nu}D - M_{\mu\nu})$ and then $[D,\mathcal{O}(0)]=i\Delta\mathcal{O}(0)$, $[M_{\mu\nu},\mathcal{O}(0)]=0$ for a scalar,
$$
\big[K_\mu,[P_\nu,\mathcal{O}(0)]\big] = 2i\big(i\Delta\,\delta_{\mu\nu}\big)\mathcal{O}(0) = -2\Delta\,\delta_{\mu\nu}\,\mathcal{O}(0) \;\neq\; 0
$$
for any $\Delta\neq0$. So $\partial_\nu\mathcal{O}$ is not annihilated by $K_\mu$ and is not primary. Note that the obstruction is proportional to $\Delta$ itself: the identity operator, with $\Delta=0$, is the one case where the argument fails, and indeed $\partial_\mu\mathbb{1}=0$.

> **[Proved.]** $\partial_\mu\mathcal{O}$ is a non-primary descendant of dimension $\Delta+1$ (the three lines above). **[Stated — refs: Rychkov §2.]** the finite transformation law of primaries.

## 4. Two-point functions from the Ward identities (worked)

Conformal symmetry fixes low-point functions. For two scalar primaries $\mathcal{O}_1,\mathcal{O}_2$ work through the constraints on $G(x_1,x_2)=\langle\mathcal{O}_1(x_1)\mathcal{O}_2(x_2)\rangle$:

1. **Translations** ($P$): $G$ depends only on $x_{12}=x_1-x_2$.
2. **Rotations** ($M$): $G$ depends only on $|x_{12}|$.
3. **Dilatations** ($D$): under $x\to\lambda x$ each $\mathcal{O}_i$ scales by $\lambda^{-\Delta_i}$, so $G(\lambda x_{12})=\lambda^{-\Delta_1-\Delta_2}G(x_{12})$, forcing $G=C\,|x_{12}|^{-\Delta_1-\Delta_2}$.
4. **Special conformal** ($K$): under the inversion $x\to x/x^2$, $|x_{12}|^2\to |x_{12}|^2/(x_1^2 x_2^2)$ and each $\mathcal{O}_i$ picks up $(x_i^2)^{\Delta_i}$. Invariance of $G$ then requires the powers of $x_1^2$ and $x_2^2$ to match, i.e. $\Delta_1=\Delta_2$.

Combining, with the standard normalisation $C_\mathcal{O}=1$,

$$
\boxed{\;\langle\mathcal{O}(x)\,\mathcal{O}(0)\rangle = \frac{C_\mathcal{O}}{|x|^{2\Delta}},\qquad \langle\mathcal{O}_1\mathcal{O}_2\rangle = 0\ \text{ if }\Delta_1\ne\Delta_2.\;}
$$

So operators of different dimension do not mix, and the two-point function is completely fixed.

**Worked example: the three-point function.** The same logic, applied to three scalar primaries, fixes the correlator up to a single number. Translations + rotations make it a function of the three distances $x_{12},x_{23},x_{13}$; scaling under $x\to\lambda x$ requires total weight $-(\Delta_1+\Delta_2+\Delta_3)$; and SCT-invariance distributes the powers uniquely. The unique solution is

$$
\langle\mathcal{O}_1(x_1)\mathcal{O}_2(x_2)\mathcal{O}_3(x_3)\rangle
= \frac{C_{123}}{|x_{12}|^{\Delta_1+\Delta_2-\Delta_3}\,|x_{23}|^{\Delta_2+\Delta_3-\Delta_1}\,|x_{13}|^{\Delta_1+\Delta_3-\Delta_2}}.
$$

Check the exponents: the total power of $x_{12}$, summed over the pair $(1,2)$, must give each operator its dimension. Operator $1$ sits in $x_{12}$ and $x_{13}$, with combined power $\tfrac12[(\Delta_1+\Delta_2-\Delta_3)+(\Delta_1+\Delta_3-\Delta_2)] = \Delta_1$ ✓ (and likewise for $2,3$), which is exactly the scaling weight each primary must carry. The single undetermined constant $C_{123}$ is the **OPE coefficient** of Week 3 — the first piece of genuinely dynamical CFT data (everything up to here was pure kinematics). Four-point functions are the first correlators not fixed by symmetry: they retain a free function of the two conformal cross-ratios (Week 3).

> **Physical picture.** Here is where the symmetry runs out, and it is worth being precise about why. With $n$ points you have $nd$ coordinates and the conformal group has $\tfrac{(d+1)(d+2)}{2}$ parameters; up to three points the group is large enough to move any configuration to any other, so the correlator can only be a constant times a fixed kinematic factor. At four points it is not: two combinations of the coordinates — the cross-ratios $u,v$ — survive every conformal transformation, and the correlator may depend on them arbitrarily. So the four-point function is where dynamics enters and where the bootstrap does its work. In the bulk this is the same statement as: two- and three-point functions come from the free bulk field and its cubic vertex, whereas the four-point function needs an exchange diagram and therefore knows about the bulk spectrum (Sem II Wk 2).

> **[Proved.]** the two-point form by the four steps above (the SCT step is the non-trivial one — it kills cross-dimension mixing), and the three-point form by the exponent-counting argument; only $C_{123}$ is left free.

## 5. Unitarity bounds (worked at level 1)

In a unitary (reflection-positive) CFT, descendant states have non-negative norm. Compute the **level-1** norm of a scalar primary state $|\mathcal{O}\rangle$ (radial quantisation, Week 2; here just use $P_\mu^\dagger=K_\mu$):

$$
\big\|P_\mu|\mathcal{O}\rangle\big\|^2 = \langle\mathcal{O}|K_\mu P_\nu|\mathcal{O}\rangle
= \langle\mathcal{O}|[K_\mu,P_\nu]|\mathcal{O}\rangle
= 2\langle\mathcal{O}|\big(\delta_{\mu\nu}D - M_{\mu\nu}\big)|\mathcal{O}\rangle,
$$

using $K_\mu|\mathcal{O}\rangle$-then-$P_\nu$ and $P_\nu^\dagger = K_\nu$, plus $K_\mu|\mathcal{O}\rangle=0$ to drop the reordered term. For a **scalar** ($M_{\mu\nu}|\mathcal{O}\rangle=0$, $D\to\Delta$) this is $2\Delta\,\delta_{\mu\nu}\ge0$, giving $\Delta\ge0$ (saturated by the identity). The sharper bound comes from the **level-2** descendant $P^2|\mathcal{O}\rangle$, whose norm positivity tightens the scalar bound to $\Delta\ge\tfrac{d-2}{2}$ (saturation = the null state $\Box\phi=0$, the free scalar). The general spin-$\ell$ analysis (positivity of the level-1 norm in the $(\Delta,\ell)$ rep) gives:

$$
\boxed{\;\Delta\ge\frac{d-2}{2}\ \ (\ell=0),\qquad
\Delta\ge\ell+d-2\ \ (\ell\ge1).\;}
$$

Saturation = a null descendant = a **conservation law / free field**:

- scalar $\Delta=\tfrac{d-2}{2}$: free scalar ($\Box\phi=0$);
- $\ell=1$, $\Delta=d-1$: conserved current $\partial^\mu J_\mu=0$;
- $\ell=2$, $\Delta=d$: stress tensor $\partial^\mu T_{\mu\nu}=0$ (Week 4).

Example: a free real scalar in $d=4$ has $\Delta_\phi=1=\tfrac{d-2}{2}$ (saturates); the composite $:\!\phi^2\!:$ has $\Delta=2$, $\ell=0$, comfortably above the bound $1$ — it saturates nothing.

> **[Proved.]** the level-1 scalar norm $=2\Delta\delta_{\mu\nu}$ (above), giving $\Delta\ge0$. **[Stated — refs: Rychkov §3.]** the sharper bounds $\tfrac{d-2}{2}$, $\ell+d-2$, which require the level-2 and full-spin analysis.

## 6. Subtleties and fine print

**Primary versus quasi-primary.** In $d\ge3$ the two coincide and the distinction is pedantry. In $d=2$ it is not: the global $\mathrm{SL}(2,\mathbb{C})$ sits inside the infinite Virasoro algebra, and an operator can transform covariantly under the global subgroup while failing to under the full local algebra. Quasi-primary means the former, primary the latter, and the stress tensor itself is the standard example of quasi-primary-but-not-primary (Week 4). Everything in this note is $d\ge3$; carry the distinction into Week 5 and not before.

**Where the unitarity bounds actually come from.** The level-1 computation in §5 gives only $\Delta\ge0$. The sharp scalar bound $\Delta\ge\tfrac{d-2}{2}$ needs the level-2 norm, and the spinning bounds need the full $(\Delta,\ell)$ analysis. Do not quote the sharp bounds as though this note proved them — the label in §7 says [Stated — refs] for exactly this reason. What *is* proved here is the mechanism: bounds come from norms of descendants, and saturation means a null state, which means a differential equation on the operator (free field, conserved current, conserved stress tensor).

**Reflection positivity is not manifest.** "Unitary" in Euclidean signature means reflection-positive, and the inner product used in §5 is the radial-quantisation one that Week 2 constructs. The manipulation $P_\mu^\dagger = K_\mu$ is a *consequence* of that construction, not a definition, and it is the only place in this note where Euclidean signature does real work. A student who finds §5 slippery should read Week 2 first and return.

**The identity operator is the degenerate case throughout.** It has $\Delta=0$, saturates the scalar bound trivially, is the one operator whose derivative vanishes (§3), and is the reason two-point functions of distinct operators can be set to zero by choice of basis rather than by symmetry alone. It is worth checking every general statement in this note against $\mathbb{1}$; several of them acquire an exception.

**Conventions for the algebra.** The commutators in §2 are Euclidean and carry explicit factors of $i$; roughly half the literature uses anti-Hermitian generators and drops them. Nothing physical depends on the choice, but signs in the Ward identities do, so stay inside [[courses/ads-cft-course/conventions]] and convert at the boundary of the course rather than mid-derivation.

## 7. Key claims and proof status

- **[Proved.]** generator count $\tfrac{(d+1)(d+2)}{2}$ from the Killing equation (§1).
- **[Proved.]** conformal algebra $\cong\mathfrak{so}(d+1,1)$ / $\mathfrak{so}(d,2)$ via embedding coordinates (§2).
- **[Proved.]** $\partial_\mu\mathcal{O}$ is a non-primary descendant (§3, inline). **[Stated — refs.]** the finite transformation law.
- **[Proved.]** scalar two-point function $C_\mathcal{O}|x|^{-2\Delta}$ from the Ward identities (§4).
- **[Proved.]** level-1 scalar descendant norm $2\Delta\delta_{\mu\nu}$, giving $\Delta\ge0$ (§5). **[Stated — refs: Rychkov §3.]** the sharp bounds $\tfrac{d-2}{2}$ and $\ell+d-2$, which need level-2 and the full spin analysis.

*No coefficients in this note are uncertain. (No `CHECK` items for Wk 1.)*

## 8. What to take away

- Conformal symmetry in $d\ge3$ has $\tfrac{(d+1)(d+2)}{2}$ generators forming $\mathfrak{so}(d+1,1)$; the embedding group $\mathrm{SO}(d,2)$ is the AdS$_{d+1}$ isometry group — the first hint of the duality.
- $D$ grades the algebra; $P_\mu$ raises, $K_\mu=I P_\mu I$ lowers the dimension.
- **Primary** = $K$-annihilated lowest-weight $(\Delta,\ell)$; descendants = derivatives; finite law $\mathcal{O}\to\Omega^{-\Delta}\mathcal{O}$.
- Symmetry **fixes** $\langle\mathcal{O}\mathcal{O}\rangle = C_\mathcal{O}|x|^{-2\Delta}$ (and forbids cross-dimension mixing); CFT data $=\{(\Delta,\ell),C_{ijk}\}$.
- **Unitarity bounds** $\Delta\ge\tfrac{d-2}{2}$ (scalar), $\Delta\ge\ell+d-2$ ($\ell\ge1$); saturation = free field / current / stress tensor.

6. **$\mathfrak{so}(d,2)$ is the AdS$_{d+1}$ isometry group.** This is the single most important line in Block A. The match is a fact about two independent pieces of geometry; the duality does not create it, it explains it. Everything after Week 6 turns the coincidence into a dictionary.
7. **A derivative is never primary, and the obstruction is $\Delta$ itself** (§3, proved inline): $[K_\mu,[P_\nu,\mathcal{O}]] = -2\Delta\delta_{\mu\nu}\mathcal{O}$. The identity operator is the one exception, and it is the exception to several other statements in this note too.
8. **Symmetry stops at four points.** Two- and three-point functions are fixed up to constants; the four-point function retains a free function of two cross-ratios. That is where dynamics lives, and where the bootstrap and the bulk exchange diagram both operate.

## Exercises

**Core.**

1. **SCT commutator.** Verify $[K_\mu,P_\nu]=2i(\delta_{\mu\nu}D-M_{\mu\nu})$ from $K_\mu=I P_\mu I$.
2. **Killing equation in $d=3$.** Solve it, count solutions, match each to a generator.
3. **Derivative is a descendant.** Show $\partial_\mu\mathcal{O}$ has dimension $\Delta+1$ and is not $K$-annihilated.
4. **Two-point function.** Reproduce §4: derive $C_\mathcal{O}|x|^{-2\Delta}$ and the $\Delta_1=\Delta_2$ condition; do the SCT/inversion step in full.

**Starred.**

5. $\star$ **Embedding check.** Using $L_{\mu,\pm}=\tfrac12(P_\mu\mp K_\mu)$, $L_{+-}=D$, verify $[K_\mu,P_\nu]=2i(\delta_{\mu\nu}D-M_{\mu\nu})$ from the $\mathfrak{so}(d+1,1)$ relations.
6. $\star$ **Level-2 scalar bound.** Compute the norm of $P^2|\mathcal{O}\rangle$ (and the mixing with the trace) to derive the sharp scalar bound $\Delta\ge\tfrac{d-2}{2}$; identify the null state at the free-scalar value.

**Project.**

7. **Currents and stress tensor.** Show the $\ell=1$ bound $\Delta=d-1$ is saturated by a conserved current and the $\ell=2$ bound $\Delta=d$ by the stress tensor; preview how Week 4 builds $T_{\mu\nu}$ as the $(\Delta,\ell)=(d,2)$ primary.

## Connections to other parts of the wiki

- **Within the course.** Leads into [[week-02-radial-quantisation-and-state-operator]] (primary states are radial-quantisation inputs); $(\Delta,\ell)$ recurs throughout; the stress tensor of §5 is built in [[week-04-stress-tensor-and-central-charge]]; the embedding $\mathrm{SO}(d,2)$ becomes the AdS isometry group in [[week-06-ads-geometries|Wk 6]].
- **AQFT course cross-reference.** None for Block A — see [[tomita-takesaki-modular-theory]] for where operator-algebra machinery enters (Sem II).
- **Area page.** [[gauge-gravity-duality]] — the conformal symmetry here is the symmetry of the boundary theory in AdS/CFT.

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block A. Reviewed and approved (status: final). Last revised 2026-05-28.*
