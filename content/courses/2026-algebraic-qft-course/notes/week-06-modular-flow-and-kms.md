---
title: "Week 6 — Modular Flow and the KMS Condition"
type: lecture-notes
course: syllabus
semester: 1
week: 6
block: B
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Week 5 (Tomita operator), Week 4 (KMS condition)
modified: 2026-06-11
---

# Week 6 — Modular Flow and the KMS Condition

> *Last week we built $\Delta$ and $J$. The theorem said that $\Delta^{-it}$ does something highly non-obvious: it sends the algebra back to itself. This week we give that fact its physical name. The automorphisms $\sigma_t(a)=\Delta^{-it}a\Delta^{it}$ are the **modular flow**, and the state that produced them is **KMS at inverse temperature $1$**. In finite dimensions this reduces to Gibbs calculus. In type III it is the **replacement** for Gibbs calculus — the only thermal notion that survives where density matrices do not. The Takesaki uniqueness theorem then says: this is the unique flow for which the state is at modular equilibrium. The course's whole approach to thermal/dynamical questions in QFT runs through this identification.*

## 0. Reading

**Primary:**
- Bratteli & Robinson, Vol. I, §2.5 (modular automorphisms; basic structure).
- Bratteli & Robinson, Vol. II, §5.3 (KMS states and the modular/KMS link; equilibrium statistical mechanics in operator algebras).

**Secondary:**
- Takesaki, *Theory of Operator Algebras II*, ch. VIII (Takesaki uniqueness theorem and consequences).
- Haag, *Local Quantum Physics*, ch. V (the QFT interpretation and the thermal-time hypothesis).

**Optional research reading:**
- Connes & Rovelli, "Von Neumann algebra automorphisms and time-thermodynamics relation in generally covariant quantum theories," *CQG* 11 (1994) 2899 — the thermal-time hypothesis.
- Borchers, "On revolutionizing quantum field theory with Tomita's modular theory," *J. Math. Phys.* 41 (2000) 3604 — AQFT viewpoint.
- Witten, "Notes on some entanglement properties of QFT," arXiv:1803.04993, §§3–4 — physics applications of modular theory.

## 1. Modular automorphisms

### 1.1 Construction

Let $\mathcal{M}\subset\mathcal{B}(\mathcal{H})$ be a von Neumann algebra and let $\Omega$ be cyclic and separating. Week 5 produced the closed Tomita operator
$$
S=J\Delta^{1/2}
$$
and Tomita-Takesaki gave (in our sign convention)
$$
\Delta^{-it}\,\mathcal{M}\,\Delta^{it}=\mathcal{M}, \qquad t \in \mathbb{R}.
$$
This says: the one-parameter family of unitaries $\Delta^{-it}$ implements automorphisms of $\mathcal{M}$ by conjugation.

**Definition 1.1.** The **modular automorphism group** of $(\mathcal{M},\Omega)$ is
$$
\sigma_t^\Omega(a)\;:=\;\Delta^{-it}\,a\,\Delta^{it},\qquad a\in\mathcal{M},\quad t\in\mathbb{R}.
$$

Equivalently, if $\omega(a)=\langle\Omega,a\Omega\rangle$, we write $\sigma_t^\omega$ — the modular automorphism group of the **state** $\omega$. We use the two notations interchangeably; the state is the algebraic object, the vector is its Hilbert-space realization.

### 1.2 Group properties

**Proposition 1.2. [Stated only — refs: B-R Vol. I §2.5.1.]** *The maps $\sigma_t^\omega$ form a $\sigma$-weakly continuous one-parameter group of $*$-automorphisms of $\mathcal{M}$:*
$$
\sigma_{t+s}^\omega=\sigma_t^\omega\circ\sigma_s^\omega,\qquad
\sigma_0^\omega=\mathrm{id},\qquad
\sigma_t^\omega(ab)=\sigma_t^\omega(a)\,\sigma_t^\omega(b), \qquad \sigma_t^\omega(a^*) = \sigma_t^\omega(a)^*.
$$

The group property follows formally from $\Delta^{-it}\,\Delta^{-is}=\Delta^{-i(t+s)}$ (functional calculus of the positive self-adjoint operator $\Delta$). The structural content — that conjugation by $\Delta^{-it}$ preserves $\mathcal{M}$ — is Tomita-Takesaki.

**$\sigma$-weak continuity** is a regularity condition: the map $t \mapsto \omega'(\sigma_t^\omega(a))$ is continuous in $t$ for every $a \in \mathcal{M}$ and every normal state $\omega'$. This is weaker than norm continuity but is the right notion for von Neumann algebras (in type III, the modular flow is *never* norm-continuous on the whole algebra — only on a dense subalgebra of "smooth" elements).

### 1.3 $\omega$-invariance

The modular flow leaves the defining state invariant:
$$
\omega(\sigma_t^\omega(a)) = \omega(a)
$$
for all $a \in \mathcal{M}$ and $t \in \mathbb{R}$. This is because $\Delta\,\Omega = \Omega$ (the vacuum is in the kernel of $\log\Delta$, which is the abstract content of "$\Omega$ is invariant under the modular flow"). Concretely:
$$
\omega(\sigma_t^\omega(a)) = \langle\Omega, \Delta^{-it} a\,\Delta^{it}\Omega\rangle = \langle\Delta^{it}\Omega, a\,\Delta^{it}\Omega\rangle = \langle\Omega, a\,\Omega\rangle = \omega(a).
$$

So $\sigma_t^\omega$ is an automorphism of $\mathcal{M}$ that *fixes* the state $\omega$. Every modular flow is a one-parameter family of "$\omega$-preserving automorphisms."

## 2. The modular KMS theorem

Week 4 defined the KMS condition using the upper strip:
$$
0\le\mathrm{Im}\,z\le\beta,
$$
with boundary values
$$
F_{a,b}(t)=\omega(a\sigma_t(b)),
\qquad
F_{a,b}(t+i\beta)=\omega(\sigma_t(b)\,a).
$$
This is a property of a state-flow pair $(\omega, \sigma)$ at a specific $\beta > 0$. The modular theorem sets $\beta=1$ and identifies the unique candidate flow.

### 2.1 The theorem

**Theorem 2.1 (Modular KMS theorem). [Stated only — refs: B-R Vol. II §5.3.1; Takesaki Vol. II Ch. VIII §1.]** *Let $\mathcal{M}$ be a von Neumann algebra and let $\omega$ be a faithful normal state. Then $\omega$ is KMS at $\beta=1$ for its modular automorphism group $\sigma_t^\omega$.*

Explicitly, for $a,b\in\mathcal{M}$ there is a bounded continuous function $F_{a,b}$ on the closed strip $\{0\le\mathrm{Im}\,z\le 1\}$, holomorphic in the interior, such that
$$
F_{a,b}(t)=\omega(a\sigma_t^\omega(b)),
\qquad
F_{a,b}(t+i)=\omega(\sigma_t^\omega(b)\,a).
$$

### 2.2 The uniqueness theorem

The KMS-modular link goes both ways:

**Theorem 2.2 (Takesaki uniqueness). [Stated only — refs: Takesaki Vol. II Theorem VIII.1.2.]** *Conversely, let $\omega$ be faithful and normal on $\mathcal{M}$. If a $\sigma$-weakly continuous one-parameter automorphism group $\alpha_t$ of $\mathcal{M}$ makes $\omega$ a KMS state at $\beta=1$, then*
$$
\alpha_t=\sigma_t^\omega.
$$

This is why the modular flow is **not merely one possible equilibrium dynamics**. For a faithful normal state, it is the **unique** $\sigma$-weakly continuous one-parameter automorphism group for which that state is KMS at $\beta=1$. The pair $(\mathcal{M}, \omega)$ canonically determines a flow; no external Hamiltonian or time-translation is needed.

> **Physical picture.** The uniqueness theorem inverts the usual logic of statistical mechanics. Ordinarily one *starts* with a clock (a Hamiltonian), and asks which states are in equilibrium with respect to it; many states qualify (one per temperature, per phase). Takesaki uniqueness says the reverse question has a *unique* answer: given the equilibrium state, there is exactly one clock with respect to which it is thermal at $\beta = 1$. A sufficiently complete thermometer determines the clock. The physical mechanism is the detailed-balance identity of Week 4 §2.2: the state's correlation functions $\omega(a\,\sigma_t(b))$ know all the Boltzmann ratios between all pairs of "levels," and a full set of Boltzmann ratios at known temperature reconstructs the energy differences — hence the generator, hence the flow. What is remarkable is that this reconstruction survives in type III, where there are no levels, no $\rho$, and no trace: the strip analyticity alone carries the full dynamical information.

### 2.3 Why this matters

The combination of Theorems 2.1 and 2.2 is a **rigidity** result. Two consequences:

- **No alternative thermal dynamics.** Once we have a faithful normal state on a vN algebra, there is exactly one $\sigma$-weakly continuous one-parameter flow that makes the state "thermal" in the KMS sense, at modular $\beta = 1$. (KMS at other $\beta$ for the modular flow would require a different state, by Theorem 2.2.)

- **State-dependent vs. external Hamiltonians.** In ordinary quantum mechanics, the time evolution $\alpha_t = \mathrm{Ad}(e^{itH})$ is determined by an externally chosen Hamiltonian $H$; states are then "thermal" for $\alpha_t$ at appropriate $\beta$. In modular theory, the flow is determined *by the state* — flipping the relationship. This is the algebraic root of the Connes–Rovelli "thermal time hypothesis" (§7).

## 3. Model proof: finite-dimensional KMS

Let $\mathcal{M}=M_n(\mathbb{C})$, let $\rho>0$ with $\mathrm{Tr}\rho=1$, and set
$$
\omega_\rho(a)=\mathrm{Tr}(\rho\, a).
$$
The state $\omega_\rho$ is faithful (since $\rho > 0$) and normal. The GNS representation can be carried out on the Hilbert–Schmidt space $\mathcal{H}_{\mathrm{HS}} = M_n(\mathbb{C})$ with cyclic-separating vector $\Omega_\rho = \rho^{1/2}$, and the modular operator computed in Week 5 is $\Delta_\rho = L_\rho R_{\rho^{-1}}$. The modular automorphism on $\mathcal{M}$ acts by
$$
\sigma_t^\rho(a)=\rho^{-it}\,a\,\rho^{it}
$$
(Week 5 §6.2, in our convention).

### 3.1 Verifying KMS at $\beta = 1$

**Proposition 3.1. [Model proof.]** *$\omega_\rho$ is KMS at $\beta=1$ for $\sigma^\rho$ in the upper-strip convention.*

**Proof.** For $a,b\in M_n(\mathbb{C})$, define
$$
F_{a,b}(z)=\mathrm{Tr}\!\left(\rho\, a\, \rho^{-iz}\,b\,\rho^{iz}\right).
$$

Since $\rho>0$ has finite spectrum, $\rho^{-iz}=e^{-iz\log\rho}$ is an entire matrix-valued function. Therefore $F_{a,b}$ is entire, hence holomorphic on the strip and continuous on its boundary.

**Boundary value at $z = t$.**
$$
F_{a,b}(t)=\mathrm{Tr}(\rho\,a\,\rho^{-it}b\,\rho^{it})
=\mathrm{Tr}(\rho\,a\,\sigma_t^\rho(b)) = \omega_\rho(a\,\sigma_t^\rho(b)).
$$

**Boundary value at $z = t + i$.** Compute $\rho^{-i(t+i)}=\rho^{-it+1}=\rho\,\rho^{-it}$ and $\rho^{i(t+i)}=\rho^{it-1}=\rho^{-1}\rho^{it}$. So
$$
\begin{aligned}
F_{a,b}(t+i)
&=\mathrm{Tr}\!\left(\rho\,a\,\rho\,\rho^{-it}\,b\,\rho^{-1}\rho^{it}\right)\\
&=\mathrm{Tr}\!\left(a\,\rho\,\rho^{-it}\,b\,\rho^{-1}\rho^{it}\,\rho\right) \qquad\text{(cyclicity, one rotation)}\\
&=\mathrm{Tr}\!\left(a\,\rho\,\rho^{-it}\,b\,\rho^{it}\right) \qquad\text{(}\rho^{-1}\rho^{it}\rho = \rho^{it}\text{, functions of }\rho\text{)}\\
&=\mathrm{Tr}\!\left(\rho\,\rho^{-it}\,b\,\rho^{it}\,a\right) \qquad\text{(cyclicity)}\\
&=\mathrm{Tr}\!\left(\rho\,\sigma_t^\rho(b)\,a\right)\\
&=\omega_\rho(\sigma_t^\rho(b)\,a).
\end{aligned}
$$

So $F_{a, b}(t) = \omega_\rho(a\sigma_t^\rho(b))$ and $F_{a,b}(t+i) = \omega_\rho(\sigma_t^\rho(b)\,a)$ — exactly the KMS at $\beta = 1$ identity in the upper strip. $\square$

### 3.2 Discussion of the proof

The proof is a sequence of trace cyclicities, exploiting that $\rho^{-iz}$ and $\rho^{iz}$ are both functions of $\rho$ and commute with $\rho$ itself. The crucial moment is when we use $\rho^{-1}\rho^{it}\rho = \rho^{it}$ — this is the place where the analytic continuation in $z$ to the upper strip gives a clean boundary value.

The classroom version is finite-dim; the full theorem (2.1) says the same strip identity persists when the trace expression no longer exists — i.e., when $\mathcal{M}$ is type II or III. In those cases, the proof uses the analytic structure of $\Delta^{-iz}$ on a dense subspace of "analytic-for-$\Delta$" vectors, but the structural identity is the same.

**The general mechanism, in one paragraph.** Where the trace computation above uses cyclicity, the general proof uses the two relations from Week 5: $\Delta^{1/2} a\Omega = J a^*\Omega$ (from $S = J\Delta^{1/2}$) and $\Delta\Omega = \Omega$. For $a, b \in \mathcal{M}$ define $F_{a,b}(z) := \langle a^*\Omega,\, \Delta^{-iz}\, b\,\Omega\rangle$. On vectors analytic for $\Delta$ this is holomorphic on the strip; at the real boundary, $F(t) = \langle a^*\Omega, \Delta^{-it} b \Delta^{it}\Omega\rangle = \omega(a\,\sigma_t(b))$. At the top boundary, insert $\Delta^{-i(t+i)} = \Delta\,\Delta^{-it}$ and use $\Delta = S^*S = (J\Delta^{1/2})^*(J\Delta^{1/2})$ to convert the extra $\Delta^{1/2}$ factors into Tomita flips: $\langle a^*\Omega, \Delta\, \sigma_t(b)\Omega\rangle = \langle \Delta^{1/2}a^*\Omega,\, \Delta^{1/2}\sigma_t(b)\Omega\rangle = \langle J a\Omega,\, J\sigma_t(b)^*\Omega\rangle = \langle \sigma_t(b)^*\Omega,\, a\Omega\rangle = \omega(\sigma_t(b)\,a)$, using anti-unitarity of $J$ in the second-to-last step. The KMS identity is thus a *two-line consequence of the polar decomposition* — all the analytic effort of the full proof goes into controlling domains, i.e. into showing enough vectors are analytic for $\Delta$ to make the formal manipulation legitimate. **[Sketched.]**

## 4. Relation to physical Gibbs evolution

The finite-dim modular flow has a clean physical interpretation when $\rho$ is a Gibbs density matrix.

### 4.1 Identification

Suppose $\rho$ is a Gibbs density matrix at physical inverse temperature $\beta$:
$$
\rho_\beta=\frac{e^{-\beta H}}{Z}, \qquad Z = \mathrm{Tr}(e^{-\beta H}).
$$
Then $\rho_\beta^{-it} = Z^{it}\,e^{i\beta tH}$, and the modular flow is
$$
\sigma_t^\rho(a)=\rho_\beta^{-it}\,a\,\rho_\beta^{it}
= Z^{it}\,e^{i\beta t H}\,a\,e^{-i\beta tH}\,Z^{-it} = e^{i\beta tH}\,a\, e^{-i\beta tH}.
$$
The scalar phases cancel.

The physical Heisenberg evolution at inverse temperature $\beta$ is
$$
\alpha_s(a)=e^{isH}\,a\,e^{-isH}.
$$
Comparing:
$$
\sigma_t^\rho=\alpha_{\beta t}.
$$

### 4.2 Modular time vs. physical time

So in our upper-strip convention, **modular time is the inverse-temperature rescaling of physical time, in the same direction**. The Gibbs state at physical inverse temperature $\beta$ is KMS at the *physical* $\beta$ for $\alpha$ (Week 4 §1.1 derivation) and equivalently KMS at $\beta_{\mathrm{mod}}=1$ for $\sigma^\rho$ (the modular flow obtained by rescaling).

The translation:
$$
\text{Gibbs state at inverse temperature }\beta
\quad\Longleftrightarrow\quad
\text{KMS state at }\beta_{\mathrm{mod}}=1\text{ for modular time}.
$$

### 4.3 Why the rescaling?

This is the algebraic content of the "thermal time hypothesis" (§7): there is a canonical *modular* time scale, intrinsic to the state, which differs from physical time by the temperature factor. Equivalently: in a thermal system, "modular time" is "physical time, measured in units of the thermal coherence time $1/(k_B T)$."

In QFT (Bisognano–Wichmann, Week 10), the same idea gives: modular time on a Rindler wedge is the boost-parameter time, related to the proper time of an accelerated observer by the Unruh-temperature factor.

## 5. Three benchmark examples

### 5.1 Non-tracial type-I state

Let
$$
\rho=\mathrm{diag}(p_1,\ldots,p_n),\qquad p_i>0, \quad \sum_i p_i = 1.
$$
For the matrix unit $E_{ij} = |e_i\rangle\langle e_j|$,
$$
\sigma_t^\rho(E_{ij}) = \rho^{-it} E_{ij} \rho^{it} = p_i^{-it} E_{ij}\,p_j^{it} = \left(\frac{p_j}{p_i}\right)^{it} E_{ij}.
$$
The diagonal matrix units $E_{ii}$ are *fixed* by the flow; the off-diagonal matrix units $E_{ij}$ for $i \neq j$ rotate with frequencies $\log p_j - \log p_i$.

**Periodicity.** If all log-ratios $\log p_j - \log p_i$ are commensurate (rational multiples of a common number), the flow is periodic. Generically (for irrational ratios), the flow is **not periodic** — it is an almost-periodic flow on the matrix algebra.

> **Physical picture.** This computation is *spectroscopy without a Hamiltonian*. The off-diagonal matrix units are coherences between "levels," and the modular flow makes them precess at frequencies $\log p_j - \log p_i$ — energy differences in units where $\beta = 1$, read off from the *populations* of the state rather than from any externally given $H$. Diagonal observables (functions of the populations) are modular-invariant: the thermal clock does not see what is already equilibrated. The fixed-point subalgebra of the modular flow (the *centralizer* $\mathcal{M}^\omega$, Problem 2) is therefore the algebra of observables that the state treats as conserved quantities. In type III$_1$ this centralizer is small precisely because everything carries modular frequency — the algebra is all coherence and no rest frame; the crossed product of Block D enlarges the system until a meaningful centralizer (and with it a trace) reappears.

**Powers state.** For the Powers state $\rho_\lambda = \mathrm{diag}(1, \lambda)/(1+\lambda)$ with $\lambda \in (0, 1)$, the ratio is $\lambda$, and the modular flow has period $T_\lambda = 2\pi/|\log\lambda|$ (Week 4 §7.4). On the infinite tensor product, this period survives and becomes the Connes T-invariant of the type III$_\lambda$ factor (Week 12).

### 5.2 Tracial state

For the normalized trace on $M_n(\mathbb{C})$,
$$
\rho=\frac{1}{n}\,1.
$$
Then $\rho^{-it} = n^{it}\,1$, and
$$
\sigma_t^\rho(a)=\rho^{-it}\,a\,\rho^{it} = (n^{it} 1)\, a\, (n^{-it} 1) = a.
$$
The trace is KMS for the trivial flow at every inverse temperature (Week 4 §5), and the modular flow agrees: $\sigma_t^\tau = \mathrm{id}$. In modular language, $\Delta_\tau = 1$.

The same statement holds in the tracial GNS representation of a finite factor $\mathcal{M}$ (e.g., the hyperfinite II$_1$ factor). On $L^2(\mathcal{M}, \tau)$,
$$
S[a]=[a^*],\qquad \Delta=1,\qquad \sigma_t^\tau=\mathrm{id}.
$$
This is the type II$_1$ situation: the modular dynamics is degenerate. Tracial states have no preferred thermal time — the modular clock is at rest.

### 5.3 Powers factor

Return to the Powers state from Week 4:
$$
\rho_\lambda=\frac{1}{1+\lambda}
\begin{pmatrix}
1&0\\0&\lambda
\end{pmatrix},
\qquad 0<\lambda<1.
$$
On a single copy of $M_2(\mathbb{C})$,
$$
\sigma_t^\lambda(E_{12})=\lambda^{it}\,E_{12},
\qquad
\sigma_t^\lambda(E_{21})=\lambda^{-it}\,E_{21}.
$$
(Here $E_{12}=|e_1\rangle\langle e_2|$, with $\rho$-eigenvalues $p_1=1/(1+\lambda)$, $p_2=\lambda/(1+\lambda)$, so $p_2/p_1 = \lambda$.)

The local modular flow has period
$$
T_\lambda=\frac{2\pi}{|\log\lambda|}.
$$

**On the infinite tensor product.** The modular flow on $\mathcal{R}_\lambda$ (the type III$_\lambda$ factor of Week 4 §7) is the product of single-site flows. The period $T_\lambda$ survives to the infinite-product GNS representation — every single site returns to identity at the same modular time, so the global flow is periodic at $T_\lambda$.

**Theorem 5.1 (Powers/Connes classification input). [Stated only — refs as Week 4 §7.3.]** *In the infinite tensor product GNS representation of $\omega_\lambda^{\otimes\infty}$, the von Neumann closure is the hyperfinite type III$_\lambda$ factor, and the modular-flow periodicity above is reflected in the Connes S-invariant: $S(\mathcal{R}_\lambda) = \{0\} \cup \{\lambda^n : n \in \mathbb{Z}\}$.*

We use this as a guide, not as a proof of type III classification (the actual proof requires more machinery). The important lesson for the course is that **non-tracial modular dynamics survives the infinite limit and becomes a type invariant**.

## 6. Intrinsic character of modular flow

The finite-dimensional formula
$$
\sigma_t^\rho(a)=\rho^{-it}\,a\,\rho^{it}
$$
looks representation-dependent because it uses a matrix $\rho$. The general theorem says the opposite.

### 6.1 Representation independence

**Proposition 6.1. [Stated only — refs: Takesaki Vol. II Ch. VIII §1.]** *Let $\omega$ be a faithful normal state on an abstract von Neumann algebra $\mathcal{M}$. The modular automorphism group $\sigma_t^\omega$ depends only on the pair $(\mathcal{M},\omega)$, not on the particular faithful representation used to construct it.*

More concretely: if $\pi_i:\mathcal{M}\to\mathcal{B}(\mathcal{H}_i)$ are two faithful normal representations carrying cyclic-separating vectors for the same state $\omega$, the resulting modular flows on $\mathcal{M}$ agree (after identifying the two representations via the abstract algebra).

### 6.2 Why this matters for QFT

This is the main reason modular theory belongs in an AQFT course. **Local algebras in QFT usually do not come with density matrices** — they are type III$_1$ (Week 12), so there is no faithful normal trace, and so no density matrix in the sense of "$\rho$ such that $\omega(a) = \mathrm{Tr}(\rho a)$." But:

- Faithful normal **states** exist (the vacuum, by Reeh–Schlieder).
- Faithful normal states have canonical modular **flows** (Tomita–Takesaki + Proposition 6.1).
- These flows are intrinsic to the algebra-state pair; they do not depend on any representation choice.

So even when the finite-dim formula $\sigma_t^\rho(a) = \rho^{-it} a \rho^{it}$ doesn't literally apply (because $\rho$ doesn't exist), the modular flow does. **This is the technical content of "modular theory works in any type."**

### 6.3 Computing modular flow in practice

In practice, one often computes the modular flow as follows:

1. **Find a Hilbert-space realization** with $\Omega$ cyclic-separating (e.g., the GNS representation, or the standard form of $\mathcal{M}$, or a physical representation like Fock space for QFT).
2. **Compute $\Delta$ explicitly** in that representation (via the Tomita operator + polar decomposition, Week 5).
3. **Define $\sigma_t^\omega(a) = \Delta^{-it} a \Delta^{it}$** and check that the result lies in $\mathcal{M}$.

For free QFT on the Rindler wedge, step 2 is solved by Bisognano–Wichmann: $\Delta = e^{-2\pi K}$ with $K$ the boost generator. This is the *only* general case in physics where step 2 has an explicit closed-form answer.

## 7. Type III and thermal time

For type I algebras, modular flow is density-matrix dynamics in disguise. For finite type II algebras with the trace, it is trivial. For type III algebras, there is **no faithful normal trace**, and modular flow cannot be dismissed as a trace artifact.

### 7.1 Careful wording

A few precision points worth dwelling on:

- **A type III algebra can have many one-parameter automorphism groups.** Modular flow is not "the only possible time." For example, the Bisognano–Wichmann modular flow on $\mathcal{A}(W_R)$ is the boost; one could also consider other Poincaré-subgroup actions on the same algebra. Each gives a different one-parameter dynamics.

- **For each faithful normal state $\omega$, $\sigma_t^\omega$ is *the* canonical time flow attached to $(\mathcal{M},\omega)$.** Two different states give two different modular flows.

- **The two flows are related by the Connes cocycle.** If one changes the state, the modular flow changes, but Connes' Radon–Nikodym theorem (Week 7) says different faithful normal states have modular flows related by an inner cocycle in $\mathcal{M}$. The cocycle is the noncommutative "Radon–Nikodym derivative."

### 7.2 The thermal-time hypothesis

This is the mathematical core behind the Connes-Rovelli (1994) **thermal-time hypothesis**:

> In a generally covariant setting, where no external Hamiltonian is preferred — for example, in canonical quantum gravity, where there is no preferred time coordinate — the **state** itself can supply a distinguished flow. Modular time is the algebraic substitute for external clock time.

The hypothesis: in any physical situation where one has an algebra of observables and a state (vacuum, thermal, ground state, ...), the *modular flow of that state* is the natural time evolution. There is no need to specify a Hamiltonian; the state does it for you.

This is philosophical but mathematically precise. Whether it gives the *right* physical time in any given situation is an open question. In QFT, Bisognano–Wichmann says that for a wedge in Wightman QFT with the Minkowski vacuum, the modular flow is the boost — which matches the natural "time" for accelerated observers. In curved spacetime / gravity, the picture is more delicate; this is one of the motivations for the Sem II Witten/CPW/AAJ program.

### 7.3 The AQFT slogan

For AQFT, the slogan becomes practical:

> "**In the Rindler wedge, Bisognano–Wichmann identifies the vacuum modular flow with Lorentz boosts.** In that special case, the abstract modular clock coincides with a geometric flow."

This is the structural anchor of all the Sem II calculations. Without Bisognano–Wichmann, modular flow would be an abstract object that one cannot compute. With it, modular flow becomes a geometric symmetry of spacetime, and the whole crossed-product machinery (Block D) becomes computable in specific physical models.

## 8. What to take away

- **Stated only:** Tomita-Takesaki makes $\sigma_t^\omega(a)=\Delta^{-it}a\Delta^{it}$ a $\sigma$-weakly continuous one-parameter automorphism group of $\mathcal{M}$.
- **Stated only (Theorem 2.1):** $\omega$ is KMS at $\beta=1$ for its own modular flow.
- **Stated only (Theorem 2.2):** Takesaki uniqueness — the modular flow is the *unique* one-parameter flow for which $\omega$ is KMS at $\beta = 1$.
- **Model proof:** for $M_n(\mathbb{C})$, KMS at $\beta=1$ upper-strip follows from $F_{a,b}(z)=\mathrm{Tr}(\rho\,a\,\rho^{-iz}b\,\rho^{iz})$ and trace cyclicity.
- **Computed here:** non-tracial density matrices rotate matrix units (with frequencies $\log p_j - \log p_i$); tracial states have trivial modular flow; Powers states have periodic modular flow with period $2\pi/|\log\lambda|$.
- **Intrinsic character:** modular flow depends only on the algebra-state pair, not on the representation.
- **Physical interpretation:** in type III, modular flow is the algebraic replacement for Gibbs evolution. The Connes–Rovelli thermal-time hypothesis takes this seriously as a substitute for external time in generally covariant settings.

## 9. Looking ahead

Week 7 asks how two different faithful normal states on the same algebra compare. The answer is the **Connes cocycle**:
$$
(D\omega/D\phi)_t.
$$
It is the noncommutative Radon-Nikodym derivative that converts $\sigma_t^\phi$ into $\sigma_t^\omega$ by inner-automorphism dressing. The same relative modular operator also gives **Araki-Uhlmann relative entropy** — the entropy notion that survives in type III, replacing $S(\rho) = -\mathrm{Tr}(\rho\log\rho)$ where the latter is undefined.

## 10. Problem set

**Core problems.**

**1. Finite-dimensional KMS, step by step.** Reproduce the proof of Proposition 3.1 in full detail. Check every equality at $z=t+i$, identifying each use of trace cyclicity and each combination of $\rho$-powers. Verify that the result is well-defined as $\rho \to 1/n$ (tracial limit) — does anything degenerate?

**2. Matrix-unit flow.** Let $\rho=\mathrm{diag}(p_1,\ldots,p_n)$. Show that
$$
\sigma_t^\rho(E_{ij})=\left(\frac{p_j}{p_i}\right)^{it}\,E_{ij}.
$$
Which elements of $M_n(\mathbb{C})$ are fixed by the flow? Identify the fixed-point subalgebra.

**3. Thermal qubit.** For $H=\mathrm{diag}(0,E)$ and $\rho_\beta=e^{-\beta H}/Z$, compute $\sigma_t^\rho(\sigma_x)$ and $\sigma_t^\rho(\sigma_y)$. Compare with the physical Heisenberg evolution $\alpha_s(\sigma_x), \alpha_s(\sigma_y)$ at $s = \beta t$. Verify the relation $\sigma_t^\rho = \alpha_{\beta t}$.

**4. Tracial modular flow.** In the GNS representation of a finite factor $(\mathcal{M},\tau)$, prove that $\Delta=1$ and $\sigma_t^\tau=\mathrm{id}$. (*Hint:* on the tracial GNS space $L^2(\mathcal{M}, \tau)$, the Tomita operator is $S[a] = [a^*]$ with $S^2 = 1$, so $\Delta = S^*S = 1$.)

**5. Powers period.** For $\rho_\lambda=\frac{1}{1+\lambda}\mathrm{diag}(1,\lambda)$, compute the smallest positive period of the modular flow on $E_{12}$. Compare with the period of the modular flow on a tensor product $\rho_\lambda \otimes \rho_\lambda$ (acting on $M_2 \otimes M_2$).

**6. Modular invariance of the state.** Verify directly that $\omega_\rho(\sigma_t^\rho(a)) = \omega_\rho(a)$ for all $a \in M_n(\mathbb{C})$ and $t \in \mathbb{R}$, using $\rho \cdot \rho^{-it} = \rho^{1-it}$ and trace cyclicity.

**Starred problems.**

**7\*. Periodicity criterion.** For $\rho=\mathrm{diag}(p_1,\ldots,p_n)$, find a necessary and sufficient condition on the $p_i$ for $\sigma_t^\rho$ to be periodic. (*Hint:* the flow is periodic iff all log-ratios $\log p_j - \log p_i$ are commensurate, i.e., lie in a common $\mathbb{Q}$-subspace of $\mathbb{R}$.)

**8\*. Takesaki uniqueness in finite dimensions.** Suppose $\omega_\rho$ is faithful on $M_n(\mathbb{C})$ and KMS at $\beta=1$ for a one-parameter group $\alpha_t=\mathrm{Ad}(e^{itK})$. Show that, up to an additive scalar in $K$,
$$
K=-\log\rho.
$$
Equivalently, $K = K_\omega$ is the modular Hamiltonian and $\sigma_t^\rho=\mathrm{Ad}(e^{itK_\omega})$. (*Hint:* use the KMS condition on matrix units $a = E_{ij}, b = E_{ji}$ to derive the energy weights, then conclude $K$ is diagonal in the $\rho$-eigenbasis with eigenvalues $-\log p_i$.)

**9\*. Inner versus outer.** In $M_n(\mathbb{C})$, every automorphism is inner (implemented by conjugation with a unitary). Explain why this makes modular flow less informative than in type III factors. Then state what it means for the image of $\sigma_t^\omega$ in $\mathrm{Out}(\mathcal{M}) = \mathrm{Aut}(\mathcal{M}) / \mathrm{Inn}(\mathcal{M})$ to be non-trivial (this is one form of the type III diagnostic).

**10\*. Modular flow on a tensor product.** Let $\rho \in M_n(\mathbb{C})$ and $\sigma \in M_m(\mathbb{C})$ both be faithful states. Compute the modular flow $\sigma_t^{\rho \otimes \sigma}$ on $M_n \otimes M_m$ and express it as $\sigma_t^\rho \otimes \sigma_t^\sigma$. Verify by direct computation that the KMS condition at $\beta = 1$ holds for the joint state.

**Project problems.**

**11. Thermal time memo.** Write a two-page note explaining the Connes-Rovelli thermal-time hypothesis using only concepts introduced in Weeks 4–6. Keep separate: theorem, interpretation, and speculative physics. Discuss whether the hypothesis is empirically distinguishable from "ordinary" external-Hamiltonian time evolution.

**12. Rindler preview.** Read the statement of the Bisognano-Wichmann theorem (Week 10 preview). Identify which part corresponds to $\Delta^{-it}$ (the modular operator → boost) and which part corresponds to $J$ (the modular conjugation → PCT × rotation) for the right-wedge algebra.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block B. Last revised 2026-06-11.*
