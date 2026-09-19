---
title: "Week 7 — Connes Cocycle and Araki-Uhlmann Relative Entropy"
type: lecture-notes
course: syllabus
semester: 1
week: 7
block: B
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 5–6 (Tomita operator and modular flow)
modified: 2026-06-11
---

# Week 7 — Connes Cocycle and Araki-Uhlmann Relative Entropy

> *A single faithful normal state gives a modular flow. Physics rarely gives us just one state. We perturb the vacuum, compare thermal states, restrict states to subalgebras, and ask whether one state can be distinguished from another. Week 7 supplies the comparison calculus: the relative modular operator, the Connes cocycle, and Araki-Uhlmann relative entropy.*

## 0. Reading

**Primary:**
- Bratteli & Robinson, Vol. I, §2.5, for relative modular operators and the Radon-Nikodym theorem.
- Ohya & Petz, *Quantum Entropy and Its Use*, ch. 5, for finite-dimensional relative entropy and monotonicity.

**Secondary:**
- Takesaki, *Theory of Operator Algebras II*, sections on spatial derivatives and Connes cocycles.
- Witten, "Notes on some entanglement properties of QFT," arXiv:1803.04993, §3–4.

**Optional research reading:**
- Araki, "Relative entropy of states of von Neumann algebras," *Publ. RIMS* 11 (1976).
- Connes, "Une classification des facteurs de type III," *Ann. Sci. ENS* 6 (1973).

## 1. Why compare modular flows?

Let $\omega$ and $\phi$ be two faithful normal states on the same von Neumann algebra $\mathcal{M}$. Week 6 gives two flows:
$$
\sigma_t^\omega,\qquad \sigma_t^\phi.
$$
The basic question is:

> What operator converts the $\phi$-clock into the $\omega$-clock?

In classical probability, comparing two measures uses a Radon-Nikodym derivative $d\omega/d\phi$. In noncommutative probability, the derivative is no longer a single positive function. It becomes a one-parameter family of unitaries:
$$
(D\omega/D\phi)_t.
$$
This is the Connes cocycle.

The same comparison object produces relative entropy. In type III, where neither state has a density matrix with respect to a trace, this is the entropy that remains.

## 2. Relative Tomita operators

For the cleanest statement, put $\mathcal{M}$ in a standard representation and choose cyclic-separating vector representatives $\Omega_\omega$ and $\Omega_\phi$ for $\omega$ and $\phi$.

**Definition 2.1.** The **relative Tomita operator** $S_{\omega,\phi}$ is initially defined on $\mathcal{M}\Omega_\phi$ by
$$
S_{\omega,\phi}(a\Omega_\phi)=a^*\Omega_\omega,\qquad a\in\mathcal{M}.
$$
It is closable. Its polar data define the **relative modular operator**
$$
\Delta_{\omega,\phi}:=S_{\omega,\phi}^*S_{\omega,\phi}.
$$

**Proof status. [Stated only — refs: Araki 1976; B-R Vol. I §2.5; Takesaki Vol. II Ch. VIII.]** Closability and representation-independent construction parallel Week 5 but require the standard form of a von Neumann algebra or spatial derivatives to avoid representation artifacts.

When $\omega=\phi$, this reduces to the ordinary Tomita operator and ordinary modular operator:
$$
\Delta_{\omega,\omega}=\Delta_\omega.
$$

> **Physical picture.** The ordinary modular operator measured the thermal weights of one state against itself; the relative modular operator measures *one state's excitations weighted by another state's thermal structure*. In the finite-dimensional formula of §3, $\Delta_{\omega,\phi} = L_\rho R_{\sigma^{-1}}$: the "numerator" state supplies the weights, the "denominator" state supplies the reference orbit. The physics use-case is exactly the situations where two states coexist: a perturbed vacuum compared to the vacuum, a black-hole microstate compared to the Hartle–Hawking state, an excited wedge state compared to Rindler. Everything this week — cocycle, relative entropy — is a different scalar or unitary extracted from this single object. It is worth internalizing that $\Delta_{\omega,\phi}$ exists for *any* pair of faithful normal states on *any* von Neumann algebra: the comparison calculus never needs a trace, which is why it is the toolset that survives in QFT.

## 3. Finite-dimensional model

Let $\mathcal{M}=M_n(\mathbb{C})$ and let $\rho,\sigma>0$ be density matrices. Work in the Hilbert-Schmidt space
$$
\mathcal{H}_{HS}=M_n(\mathbb{C}),\qquad
\langle X,Y\rangle=\mathrm{Tr}(X^*Y).
$$
The algebra acts by left multiplication:
$$
L_aX=aX.
$$
The vector representing $\omega_\rho$ is $\Omega_\rho=\rho^{1/2}$, since
$$
\langle \rho^{1/2},L_a\rho^{1/2}\rangle=\mathrm{Tr}(\rho a).
$$

### 3.1 Relative modular operator

For $X=a\sigma^{1/2}$,
$$
S_{\rho,\sigma}X=a^*\rho^{1/2}.
$$
One checks (Problem 1) that
$$
\boxed{\Delta_{\rho,\sigma}(X)=\rho X\sigma^{-1}.}
$$
Equivalently,
$$
\Delta_{\rho,\sigma}=L_\rho R_{\sigma^{-1}},
$$
where $R_bX=Xb$ is right multiplication.

This formula is the finite-dimensional template. The left density matrix belongs to the numerator state; the right density matrix belongs to the reference state.

### 3.2 Ordinary modular operator

Putting $\rho=\sigma$ gives
$$
\Delta_\sigma(X)=\sigma X\sigma^{-1}.
$$
Therefore the modular flow on the left algebra is
$$
\sigma_t^\sigma(a)=\sigma^{-it}\,a\,\sigma^{it},
$$
as in Week 6 (in our upper-strip $\beta=+1$ convention; note the minus sign on the exponent of $\Delta_\sigma^{-it}$).

## 4. The Connes cocycle

**Definition 4.1.** The **Connes cocycle derivative** of $\omega$ with respect to $\phi$ is
$$
\boxed{(D\omega/D\phi)_t:=\Delta_{\omega,\phi}^{-it}\,\Delta_\phi^{it}.}
$$
(Sign convention matches our Week 5 §4: $\sigma^\omega_t = \mathrm{Ad}(\Delta_\omega^{-it})$.)

**Theorem 4.2 (Connes Radon-Nikodym theorem). [Stated only — refs: Connes 1973; Takesaki Vol. II Ch. VIII.]** For faithful normal states $\omega,\phi$ on $\mathcal{M}$,
$$
(D\omega/D\phi)_t\in\mathcal{M}
$$
is a strongly continuous family of unitaries satisfying the cocycle identity
$$
(D\omega/D\phi)_{t+s}
=(D\omega/D\phi)_t\,
\sigma_t^\phi\!\left((D\omega/D\phi)_s\right).
$$
It intertwines the modular flows:
$$
\sigma_t^\omega(a)
=(D\omega/D\phi)_t\,\sigma_t^\phi(a)\,(D\omega/D\phi)_t^*.
$$

This is the noncommutative Radon-Nikodym theorem in the form we need later.

**Corollary 4.3 (state-independence of the modular flow modulo inner automorphisms). [Proved, given Theorem 4.2.]** *Since the cocycle is a unitary in $\mathcal{M}$, the intertwining relation says $\sigma_t^\omega$ and $\sigma_t^\phi$ differ by an inner automorphism at each $t$. Hence the image of the modular flow in the outer automorphism group,*
$$
\delta : \mathbb{R} \to \mathrm{Out}(\mathcal{M}) = \mathrm{Aut}(\mathcal{M})/\mathrm{Inn}(\mathcal{M}),
$$
*is the **same for every faithful normal state**. A von Neumann algebra carries a canonical one-parameter subgroup of $\mathrm{Out}(\mathcal{M})$ — a dynamics intrinsic to the algebra itself.*

> **Physical picture.** This corollary upgrades the slogan of Week 6 ("the state determines its time") to something stronger and stranger: *the algebra alone determines time, up to locally implementable adjustments.* Changing the state changes the modular flow only by conjugation with unitaries inside $\mathcal{M}$ — operations an observer with access to $\mathcal{M}$ can perform herself. What she cannot change is the outer class $\delta_t$. For type I and II algebras, $\delta_t$ is trivial (modular flows are inner): time must come from outside, as a Hamiltonian. For type III, $\delta_t$ is *nontrivial*: a type III algebra ticks on its own, and no choice of state, no local unitary dressing, can stop it. This is the precise sense in which a QFT local algebra "has dynamics built in" — and the kernel and periodicity of $\delta$ are exactly Connes' T-invariant, classifying III$_\lambda$ (periodic $\delta$) versus III$_1$ ($\delta$ injective). The classification of Week 3 §6 is thus revealed as a classification of *intrinsic clocks*.

### 4.1 Finite-dimensional verification

Using the Hilbert-Schmidt formulas,
$$
\Delta_{\rho,\sigma}^{-it}=L_{\rho^{-it}}R_{\sigma^{it}},
\qquad
\Delta_\sigma^{it}=L_{\sigma^{it}}R_{\sigma^{-it}}.
$$
Thus
$$
\Delta_{\rho,\sigma}^{-it}\Delta_\sigma^{it}
=L_{\rho^{-it}\sigma^{it}}.
$$
So the cocycle is represented inside $\mathcal{M}$ by
$$
\boxed{u_t=(D\omega_\rho/D\omega_\sigma)_t=\rho^{-it}\,\sigma^{it}.}
$$

The cocycle identity becomes
$$
u_{t+s}=u_t\,\sigma_t^\sigma(u_s).
$$
Indeed,
$$
\begin{aligned}
u_t\,\sigma_t^\sigma(u_s)
&=\rho^{-it}\sigma^{it}\,
\sigma^{-it}(\rho^{-is}\sigma^{is})\sigma^{it}\\
&=\rho^{-it}\rho^{-is}\sigma^{is}\sigma^{it}\\
&=\rho^{-i(t+s)}\sigma^{i(t+s)}
=u_{t+s}.
\end{aligned}
$$
The intertwining identity is just as direct:
$$
\begin{aligned}
u_t\,\sigma_t^\sigma(a)\,u_t^*
&=\rho^{-it}\sigma^{it}\,
\sigma^{-it}a\sigma^{it}\,
\sigma^{-it}\rho^{it}\\
&=\rho^{-it}\,a\,\rho^{it}
=\sigma_t^\rho(a).
\end{aligned}
$$

This calculation is worth memorizing. It is the finite-dimensional version of the machinery used in cocycle-perturbation theory.

## 5. Araki-Uhlmann relative entropy

The same relative modular operator defines relative entropy.

**Definition 5.1.** The **Araki-Uhlmann relative entropy** of $\omega$ with respect to $\phi$ is
$$
\boxed{
S(\omega\|\phi)
:=-\langle\Omega_\omega,\log\Delta_{\phi,\omega}\,\Omega_\omega\rangle.
}
$$
If the vector is outside the domain of $\log\Delta_{\phi,\omega}$ in the relevant sense, the value is $+\infty$.

The order of the indices matters. The definition uses $\Delta_{\phi,\omega}$, not $\Delta_{\omega,\phi}$.

**Theorem 5.2. [Stated only — refs: Araki 1976.]** For normal states on a von Neumann algebra:
$$
S(\omega\|\phi)\ge 0,
$$
with equality iff $\omega=\phi$ under the usual support assumptions. It is monotone under restriction to subalgebras:
$$
S(\omega|_{\mathcal{N}}\|\phi|_{\mathcal{N}})
\le
S(\omega|_{\mathcal{M}}\|\phi|_{\mathcal{M}})
\qquad
(\mathcal{N}\subset\mathcal{M}).
$$

Monotonicity is the algebraic form of data processing: throwing away observables cannot make two states easier to distinguish.

> **Physical picture.** Relative entropy has a sharp operational meaning that explains every property in Theorem 5.2. By the quantum Stein lemma, $S(\omega\|\phi)$ is the optimal exponential rate at which an observer can rule out the hypothesis "the system is in state $\phi$" when it is actually in state $\omega$: after $n$ measurements on independent copies, the probability of mistaking $\omega$ for $\phi$ decays as $e^{-n S(\omega\|\phi)}$. Positivity then says distinguishing takes work; $S = 0$ iff $\omega = \phi$ says only identical states are indistinguishable; $S = +\infty$ (which happens when $\omega$ assigns probability to events that $\phi$ forbids — the support condition, cf. Problem 9\*) says a single measurement can separate them. Monotonicity under restriction is now obvious physics: an observer with fewer observables can only distinguish more slowly. The asymmetry $S(\omega\|\phi) \neq S(\phi\|\omega)$ is also operational — false-alarm and missed-detection errors are inequivalent. In QFT applications the slogan is: *relative entropy measures how distinguishable a state is from the vacuum using only measurements inside a region*, and monotonicity under shrinking the region is what drives the Bekenstein-bound and ANEC arguments of the research literature.

## 6. Finite-dimensional entropy calculation

Let $\omega_\rho(a)=\mathrm{Tr}(\rho a)$ and $\omega_\sigma(a)=\mathrm{Tr}(\sigma a)$ with $\rho,\sigma>0$. We compute $S(\omega_\rho\|\omega_\sigma)$ from Definition 5.1.

Since
$$
\Delta_{\sigma,\rho}=L_\sigma R_{\rho^{-1}},
$$
we have
$$
\log\Delta_{\sigma,\rho}=L_{\log\sigma}-R_{\log\rho}.
$$
Acting on $\Omega_\rho=\rho^{1/2}$,
$$
\log\Delta_{\sigma,\rho}\,\rho^{1/2}
=\log\sigma\,\rho^{1/2}-\rho^{1/2}\log\rho.
$$
Therefore
$$
\begin{aligned}
S(\omega_\rho\|\omega_\sigma)
&=-\left\langle\rho^{1/2},
\log\Delta_{\sigma,\rho}\,\rho^{1/2}\right\rangle\\
&=-\mathrm{Tr}\!\left(\rho^{1/2}\log\sigma\,\rho^{1/2}\right)
+\mathrm{Tr}\!\left(\rho\log\rho\right)\\
&=\boxed{\mathrm{Tr}\rho(\log\rho-\log\sigma)}.
\end{aligned}
$$

So Araki-Uhlmann relative entropy reduces exactly to the usual Umegaki relative entropy in finite dimensions. (The convention sign-flip that appears in the cocycle does not affect the entropy formula — entropy is built from $\log\Delta$, which is convention-independent in the operator-theoretic sense.)

## 7. Worked example: two thermal states

Let
$$
\rho_\beta=\frac{e^{-\beta H}}{Z(\beta)},
\qquad
Z(\beta)=\mathrm{Tr}(e^{-\beta H}),
$$
and compare $\rho_{\beta_1}$ with $\rho_{\beta_2}$ for the same Hamiltonian.

Since
$$
\log\rho_\beta=-\beta H-\log Z(\beta),
$$
we get
$$
\begin{aligned}
S(\rho_{\beta_1}\|\rho_{\beta_2})
&=\mathrm{Tr}\rho_{\beta_1}
\left[
(-\beta_1 H-\log Z(\beta_1))
-(-\beta_2 H-\log Z(\beta_2))
\right]\\
&=(\beta_2-\beta_1)\langle H\rangle_{\beta_1}
+\log Z(\beta_2)-\log Z(\beta_1).
\end{aligned}
$$

Equivalently, using $F(\beta)=-(1/\beta)\log Z(\beta)$,
$$
S(\rho_{\beta_1}\|\rho_{\beta_2})
=(\beta_2-\beta_1)\langle H\rangle_{\beta_1}
-\beta_2 F(\beta_2)+\beta_1 F(\beta_1).
$$

This is not just a formula. It says relative entropy between thermal states is a free-energy comparison measured in the state $\rho_{\beta_1}$.

**Second-order expansion: relative entropy as heat capacity.** Set $\beta_2 = \beta_1 + \delta\beta$ and expand. The first-order term vanishes — differentiate the formula in $\beta_2$ at $\beta_2 = \beta_1$ using $\partial_\beta \log Z = -\langle H\rangle_\beta$, and the two contributions cancel. This is positivity at work: $S \ge 0$ with equality at $\delta\beta = 0$ forces the expansion to start at quadratic order. The quadratic term is
$$
S(\rho_{\beta_1}\|\rho_{\beta_1 + \delta\beta}) = \tfrac{1}{2}\,(\delta\beta)^2\,\big(\langle H^2\rangle_{\beta_1} - \langle H\rangle_{\beta_1}^2\big) + O(\delta\beta^3),
$$
the energy variance — i.e. $C/\beta^2$ in terms of the heat capacity $C$. So for nearby temperatures, relative entropy is the thermodynamic metric: distinguishability of neighboring thermal states is controlled by the system's energy fluctuations, the same quantity that controls how sharply temperature can be measured. This is the simplest instance of the general principle that the second variation of $S(\omega\|\phi)$ defines an information metric (Kubo–Mori/Bogoliubov) on the state space — the structure underlying "first law of entanglement" calculations in QFT.

## 8. Why this survives in type III

Von Neumann entropy
$$
S(\rho)=-\mathrm{Tr}(\rho\log\rho)
$$
requires a density matrix and a trace. Under the nuclearity and split-property hypotheses discussed in Block C, local QFT algebras are type III$_1$ factors. There is no canonical trace, hence no local density matrix relative to such a trace and no regulator-independent local von Neumann entropy.

Relative entropy does not suffer this failure. Araki's definition uses the relative modular operator, which is available for normal states on von Neumann algebras of any type.

The course will use this distinction repeatedly:

- **Not available in type III:** local entanglement entropy as $-\mathrm{Tr}(\rho\log\rho)$ without a regulator or split inclusion.
- **Available in type III:** $S(\omega\|\phi)$ for two normal states on the same local algebra.
- **Bridge to crossed products:** after adjoining a modular clock, one can recover a semifinite trace on a dressed algebra; Block D explains this carefully.

## 9. Relation to perturbation theory

Suppose $\omega_s$ is a differentiable family of faithful normal states with $\omega_0=\phi$. The cocycle
$$
u_t(s)=(D\omega_s/D\phi)_t
$$
measures how the modular flow changes under the perturbation:
$$
\sigma_t^{\omega_s}
=\mathrm{Ad}(u_t(s))\circ\sigma_t^\phi.
$$
Differentiating in $s$ gives a modular response operator. This is the abstract seed of cocycle perturbation theory, used in research literature (e.g., recent algebraic-perturbation work on wormhole entropy).

We will not develop that perturbation theory here. The point for now is simpler: the object that gets perturbed in research-level applications is the Connes cocycle from this week.

## 10. What to take away

- **Stated only:** the relative Tomita operator gives a relative modular operator $\Delta_{\omega,\phi}$ for two faithful normal states.
- **Stated only:** the Connes cocycle $(D\omega/D\phi)_t$ lies in $\mathcal{M}$ and intertwines the two modular flows.
- **Model proof:** in finite dimensions, $(D\omega_\rho/D\omega_\sigma)_t=\rho^{-it}\sigma^{it}$ (our sign convention).
- **Computed here:** Araki-Uhlmann relative entropy reduces to $\mathrm{Tr}\rho(\log\rho-\log\sigma)$ for matrices.
- **Research arc:** relative entropy and cocycles are the type-III-safe tools that replace density matrices and von Neumann entropy in local QFT.

## 11. Looking ahead

Block C applies the machinery to free QFT. Week 8 introduces Weyl algebras and the free scalar field; Week 9 brings in Reeh-Schlieder, which supplies cyclic-separating vectors for local algebras; Week 10 identifies a modular flow geometrically through Bisognano-Wichmann. The abstract objects $S$, $J$, $\Delta$, and $(D\omega/D\phi)_t$ will stop looking abstract.

## 12. Problem set

**Core problems.**

**1. Relative modular operator in Hilbert-Schmidt form.** Let $\rho,\sigma>0$ on $M_n(\mathbb{C})$. Starting from
$$
S_{\rho,\sigma}(a\sigma^{1/2})=a^*\rho^{1/2},
$$
verify that
$$
\Delta_{\rho,\sigma}(X)=\rho X\sigma^{-1}.
$$

**2. Cocycle identity.** With $u_t=\rho^{-it}\sigma^{it}$ and $\sigma_t^\sigma(a)=\sigma^{-it}a\sigma^{it}$, prove
$$
u_{t+s}=u_t\,\sigma_t^\sigma(u_s).
$$

**3. Intertwining.** Prove directly that
$$
\sigma_t^\rho(a)=u_t\,\sigma_t^\sigma(a)\,u_t^*.
$$

**4. Relative entropy.** Derive
$$
S(\omega_\rho\|\omega_\sigma)=\mathrm{Tr}\rho(\log\rho-\log\sigma)
$$
from the Araki-Uhlmann definition.

**5. Two thermal states.** For $H=\mathrm{diag}(0,E)$, compute $S(\rho_{\beta_1}\|\rho_{\beta_2})$ explicitly as a function of $\beta_1,\beta_2,E$.

**Starred problems.**

**6\*. Commuting states.** Suppose $\rho$ and $\sigma$ commute. Show that the Connes cocycle is a one-parameter unitary group:
$$
u_{t+s}=u_t u_s.
$$
Explain why the cocycle identity is genuinely more general when $\rho$ and $\sigma$ do not commute.

**7\*. Positivity in finite dimensions.** Prove Klein's inequality
$$
\mathrm{Tr}\rho(\log\rho-\log\sigma)\ge \mathrm{Tr}(\rho-\sigma),
$$
and use it to prove $S(\rho\|\sigma)\ge 0$ for density matrices.

**8\*. Monotonicity for partial trace.** State the data-processing inequality
$$
S(\rho_{AB}\|\sigma_{AB})\ge S(\rho_A\|\sigma_A).
$$
Prove it in the special case where $\rho_{AB}$ and $\sigma_{AB}$ are block-diagonal classical-quantum states.

**9\*. Relative entropy for displaced Gaussian states.** For a single harmonic oscillator, compare two displaced thermal Gaussian states with the same nonzero covariance and displacements $\alpha,\beta$. Compute the relative entropy and identify the coefficient of $|\alpha-\beta|^2$. Then explain why the pure coherent-vector case on $\mathcal{B}(\mathcal{H})$ has a support singularity when $\alpha\neq\beta$.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block B. Last revised 2026-06-11.*
