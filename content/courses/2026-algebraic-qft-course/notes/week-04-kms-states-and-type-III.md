---
title: "Week 4 — KMS States, the Modular Interpretation, Type III Preview"
type: lecture-notes
course: syllabus
semester: 1
week: 4
block: A
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 1–3 (C*-algebras, vN algebras, type classification)
modified: 2026-06-11
---

# Week 4 — KMS States, the Modular Interpretation, Type III Preview

> *Last week we classified factors and saw that type III admits no trace. The standard quantum-mechanical notion of thermal equilibrium — the Gibbs state $\rho_\beta = e^{-\beta H}/Z$ — therefore makes no sense in type III. This week we develop the algebraic substitute: the **KMS condition**. It is a condition on a state alone, with no Hamiltonian explicitly invoked, that captures all the operational content of "thermal equilibrium" — and it survives in type III. The Tomita-Takesaki theorem (Block B) will say that **for any faithful normal state on a vN algebra** there is a canonical one-parameter automorphism group — the modular flow — for which the state is KMS at $\beta = 1$. The whole machinery of modular theory grows out of this single observation.*

## 0. Reading

**Primary:**
- Bratteli & Robinson Vol. II, §5.3 (KMS condition and equilibrium states).
- Witten, "Notes on some entanglement properties of QFT," arXiv:1803.04993, §3.

**Secondary:**
- Haag, *Local Quantum Physics*, ch. V.
- Powers, "Representations of uniformly hyperfinite algebras…," *Annals* 86 (1967) — original construction of type III$_\lambda$.
- Connes & Rovelli, "Von Neumann algebra automorphisms and time-thermodynamics relation in generally covariant quantum theories," *CQG* 11 (1994) — for the "thermal time" interpretation we sketch in §6.

## 1. From Gibbs to KMS: a finite-dimensional warmup

In ordinary quantum mechanics on a finite-dimensional Hilbert space $\mathcal{H}$ with Hamiltonian $H = H^*$, the *Gibbs state* at inverse temperature $\beta$ is
$$
\rho_\beta = \frac{e^{-\beta H}}{Z(\beta)}, \quad Z(\beta) = \mathrm{Tr}(e^{-\beta H}).
$$
The expectation value of any observable $A \in \mathcal{B}(\mathcal{H})$ is $\omega_\beta(A) = \mathrm{Tr}(\rho_\beta A)$. Heisenberg evolution: $A_t := e^{itH} A e^{-itH}$.

### 1.1 The KMS identity

**The key calculation.** Fix $\beta > 0$. For any $a, b \in \mathcal{B}(\mathcal{H})$ define the function
$$
F(z) := \omega_\beta\big(a\,\sigma_z(b)\big) = \frac{1}{Z}\,\mathrm{Tr}\!\big(e^{-\beta H}\, a\, e^{izH} b\, e^{-izH}\big), \qquad z \in \mathbb{C},
$$
where $\sigma_z(b) := e^{izH} b\, e^{-izH}$ is the analytic continuation of the Heisenberg evolution. In finite dimensions $F$ is **entire**: the matrix exponentials are entire functions of $z$, and the trace is a continuous linear functional. On the real axis $F(t) = \omega_\beta(a\sigma_t(b))$, recovering the usual expectation value.

**The KMS identity.** *The boundary value at $z = t + i\beta$ is*
$$
F(t + i\beta) = \omega_\beta\big(\sigma_t(b)\, a\big). \tag{$*$}
$$

**Proof of ($*$).** Substitute $z = t + i\beta$ and split the exponentials:
$$
F(t + i\beta) = \frac{1}{Z}\,\mathrm{Tr}\!\big(e^{-\beta H}\, a\, e^{itH} e^{-\beta H}\, b\, e^{-itH} e^{\beta H}\big).
$$
Move the rightmost $e^{\beta H}$ around the trace by cyclicity, where it cancels the leftmost $e^{-\beta H}$:
$$
= \frac{1}{Z}\,\mathrm{Tr}\!\big(a\, e^{itH} e^{-\beta H}\, b\, e^{-itH}\big).
$$
Now move $e^{-itH}$ around the trace and combine with $e^{itH}$ to form $\sigma_{-t}(a) = e^{-itH}a\,e^{itH}$:
$$
= \frac{1}{Z}\,\mathrm{Tr}\!\big(\sigma_{-t}(a)\, e^{-\beta H}\, b\big) = \frac{1}{Z}\,\mathrm{Tr}\!\big(e^{-\beta H}\, b\, \sigma_{-t}(a)\big) = \omega_\beta\!\big(b\,\sigma_{-t}(a)\big).
$$
Finally, $\omega_\beta$ is $\sigma_t$-invariant ($\rho_\beta$ commutes with $H$, so $\omega_\beta(\sigma_t(\cdot)) = \omega_\beta(\cdot)$), and $\sigma_t(b\,\sigma_{-t}(a)) = \sigma_t(b)\,a$, so
$$
\omega_\beta\!\big(b\,\sigma_{-t}(a)\big) = \omega_\beta\!\big(\sigma_t(b)\, a\big). \qquad\square
$$

### 1.2 The structure of the KMS identity

Equation ($*$) — together with the holomorphic interpolation $F$ — has three crucial features:

1. **No reference to $\rho_\beta$ explicitly.** The boundary values $F(t) = \omega_\beta(a\sigma_t(b))$ and $F(t+i\beta) = \omega_\beta(\sigma_t(b)a)$ are computable from the state alone — the density matrix has dropped out.

2. **Holomorphic structure on the upper strip.** $F(z)$ extends to a holomorphic function on $\{0 \le \mathrm{Im}\,z \le \beta\}$ — entire in finite dimensions, holomorphic-on-the-strip in the general C\*-algebraic setting (Definition 2.1).

3. **Trace cyclicity is the engine.** The proof uses only cyclicity of the trace and the fact that $\rho_\beta$ is a function of $H$. In type III there is no trace and no density matrix, but the abstract KMS condition — the existence of a holomorphic $F$ with these boundary values — still makes sense. That is the abstraction we now make.

## 2. The KMS condition

**Definition 2.1.** Let $\mathcal{A}$ be a C\*-algebra with a one-parameter automorphism group $\sigma : \mathbb{R} \to \mathrm{Aut}(\mathcal{A})$, $t \mapsto \sigma_t$, such that $t \mapsto \sigma_t(a)$ is norm-continuous for every $a \in \mathcal{A}$. A state $\omega$ on $\mathcal{A}$ is *KMS at inverse temperature $\beta$* with respect to $\sigma$ if for every $a, b \in \mathcal{A}$, there is a function $F_{a,b}(z)$:
- holomorphic on the open strip $\{z \in \mathbb{C} : 0 < \mathrm{Im}\, z < \beta\}$,
- continuous on the closed strip $\{0 \le \mathrm{Im}\, z \le \beta\}$,
- bounded on the strip,
- with boundary values $F_{a,b}(t) = \omega(a \sigma_t(b))$ and $F_{a,b}(t + i\beta) = \omega(\sigma_t(b)\, a)$ for $t \in \mathbb{R}$.

The condition encodes Eq. ($*$) abstractly: the function $t \mapsto \omega(a\sigma_t(b))$ on the real axis coincides at $t + i\beta$ with $\omega(\sigma_t(b)a)$, with a holomorphic interpolation in between.

> **Physical picture.** The analytic strip is *imaginary time*. A physicist meets the KMS condition as the statement that thermal correlation functions are periodic in imaginary time with period $\beta$ — the Matsubara/Euclidean-path-integral structure: $\langle a(0)\, b(i\beta)\rangle_\beta = \langle b(0)\, a(0)\rangle_\beta$ up to ordering, i.e. translating one operator all the way across the thermal circle swaps the operator order. Definition 2.1 is exactly this, stated so that no path integral, no trace, and no density matrix are required: all that survives is the *analyticity of correlators in a strip of width $\beta$* plus the boundary identification. That this survives is no accident — analyticity statements are statements about correlation functions, and correlation functions are exactly what a state provides. The strip width being $\beta$ also explains physically why higher temperature is "less analytic": at $T \to \infty$ the strip collapses and the condition degenerates to traciality (§5), while at $T \to 0$ the strip becomes a half-plane — the boundary of the KMS family is the spectrum condition of the vacuum.

#### Detailed balance, derived

The slogan "KMS = detailed balance" can be made exact in two lines of Fourier analysis. Define the two correlation functions
$$
G_+(t) := \omega(a\,\sigma_t(b)), \qquad G_-(t) := \omega(\sigma_t(b)\,a),
$$
physically: the amplitude for the system to *absorb* the perturbation $b$ and later release it into $a$, in the two possible operator orders. KMS says $G_-(t) = G_+(t + i\beta)$ via the holomorphic interpolant. Writing $G_\pm(t) = \frac{1}{2\pi}\int d\nu\, e^{-i\nu t}\, \hat G_\pm(\nu)$ and shifting the contour through the strip (justified by boundedness and analyticity of $F_{a,b}$),
$$
\boxed{\;\hat G_-(\nu) = e^{-\beta\nu}\, \hat G_+(\nu).\;}
$$
The Fourier components at frequency $\nu$ — the rates for processes in which the system *gives up* energy $\nu$ versus *absorbs* it — are related by the Boltzmann factor $e^{-\beta\nu}$. This is detailed balance, the Einstein relation between emission and absorption, derived from the strip analyticity alone. In the finite-dimensional model it reduces to $\omega(E_{jj})/\omega(E_{ii}) = e^{-\beta(E_j - E_i)}$, the Step-1 computation of Theorem 3.1 below. In QFT, this identity applied to the Rindler modular flow *is* the statement that an accelerated detector's excitation and de-excitation rates have thermal ratios — the operational form of the Unruh effect.

### 2.1 Remarks and conventions

- **Sign convention.** Many references (including Bratteli–Robinson) use $\beta > 0$ and an "upper strip" (as written above). Some references invert. Be careful.
- **Strip width = inverse temperature.** $\beta = 1/k_B T$. Higher temperature → narrower strip.
- **Locality in $a, b$.** Just one pair of analytic functions per pair of observables. Hence verifying KMS is a "local" condition on observable pairs.
- **Norm continuity of $\sigma_t$.** This is a regularity assumption; it ensures $t \mapsto \omega(a\sigma_t(b))$ is continuous on the real axis. In QFT, $\sigma_t$ is the modular flow, and norm continuity is automatic for "nice" observables.

### 2.2 What KMS captures

The KMS condition is the algebraic content of *thermal equilibrium*. To see this, recall that in a Gibbs state, the response to a small perturbation $V$ at time $0$ is given by linear response theory:
$$
\delta\omega(A; t) \propto \int_0^t \omega([\sigma_s(V), A_t]) ds + \text{higher order}.
$$
The KMS condition ($*$) makes this response *time-translation invariant* and *passively determined*: the state cannot be exploited as an energy source. (This is the *passivity* of thermal states; see Pusz–Woronowicz.)

The KMS condition is also the algebraic content of *detailed balance*: the relative populations of different states are determined by their energy difference and the temperature, regardless of the path between them.

## 3. KMS in finite dimensions = Gibbs

**Theorem 3.1 (KMS uniqueness in finite dimensions).** *Let $\mathcal{A} = \mathcal{B}(\mathcal{H})$ with $\dim\mathcal{H} < \infty$, $H = H^* \in \mathcal{A}$, and $\sigma_t = \mathrm{Ad}\,e^{itH}$. Then a state $\omega$ on $\mathcal{A}$ is KMS at $\beta$ for $\sigma$ iff $\omega = \omega_{\rho_\beta}$ where $\rho_\beta = e^{-\beta H}/\mathrm{Tr}(e^{-\beta H})$.*

**Proof.** *Direction (⇐).* Suppose $\omega = \omega_{\rho_\beta}$. The function $F_{a,b}(z) := \frac{1}{Z}\mathrm{Tr}(e^{-\beta H} a\, e^{izH} b\, e^{-izH})$ is the entire holomorphic extension constructed in §1.1, with boundary values $F_{a,b}(t) = \omega_{\rho_\beta}(a\sigma_t(b))$ and $F_{a,b}(t + i\beta) = \omega_{\rho_\beta}(\sigma_t(b) a)$ established there. Boundedness on the strip $0 \le \mathrm{Im}\,z \le \beta$ holds because $\rho_\beta$, $e^{-\beta H}$, $a$, $b$, and the Heisenberg evolution are all bounded operators on the finite-dimensional $\mathcal{H}$.

*Direction (⇒).* Suppose $\omega$ is KMS at $\beta$ for $\sigma_t = \mathrm{Ad}\,e^{itH}$. Diagonalize $H$ in an orthonormal basis $\{|i\rangle\}_{i=1}^n$ with $H|i\rangle = E_i|i\rangle$, and let $E_{ij} := |i\rangle\langle j|$ be the matrix units. Then $\sigma_t(E_{ij}) = e^{it(E_i - E_j)} E_{ij}$.

**Step 1: diagonal weighting.** Fix $i \neq j$ and take $a = E_{ij}$, $b = E_{ji}$. Then $a b = E_{ii}$ and $b a = E_{jj}$, and
$$
F_{a,b}(t) = \omega(a \sigma_t(b)) = e^{it(E_j - E_i)}\,\omega(E_{ii}).
$$
The unique entire function extending this is $F_{a,b}(z) = e^{iz(E_j - E_i)}\,\omega(E_{ii})$. The KMS boundary condition at $z = t + i\beta$ demands
$$
e^{(it - \beta)(E_j - E_i)}\,\omega(E_{ii}) = \omega(\sigma_t(b)\, a) = e^{it(E_j - E_i)}\,\omega(E_{jj}),
$$
which after dividing through by $e^{it(E_j - E_i)}$ gives
$$
e^{-\beta(E_j - E_i)}\,\omega(E_{ii}) = \omega(E_{jj}).
$$
Equivalently $\omega(E_{ii}) \propto e^{-\beta E_i}$ — the **thermal weighting**.

**Step 2: off-diagonal vanishing.** Fix $i \neq l$ and take $a = E_{il}$, $b = E_{ll}$. Since $b$ is diagonal in the energy basis, $\sigma_t(b) = b$, and
$$
F_{a,b}(t) = \omega(a b) = \omega(E_{il} E_{ll}) = \omega(E_{il})
$$
is **constant in $t$**. The unique entire extension is therefore the constant $\omega(E_{il})$, so the KMS boundary condition gives
$$
\omega(E_{il}) = \omega(\sigma_t(b)\, a) = \omega(E_{ll}\, E_{il}) = 0.
$$
Hence $\omega(E_{il}) = 0$ for all $i \neq l$.

**Step 3: assembly.** Combining Steps 1 and 2, $\omega(E_{ij}) = \delta_{ij}\, e^{-\beta E_i}/Z$ with $Z = \sum_k e^{-\beta E_k}$ fixed by normalization $\omega(I) = 1$. By linearity, $\omega(\cdot) = \mathrm{Tr}(\rho_\beta\,\cdot) = \omega_{\rho_\beta}(\cdot)$. $\square$

*Remark.* Step 2 (off-diagonal vanishing) is the part most often glossed over. Without it, the diagonal weighting alone does not pin down $\omega$: a state can have the right diagonal entries but non-zero coherences. The KMS condition, applied to a non-diagonal $a$ paired with a *diagonal* $b$, forces those coherences to vanish.

*Remark on energy degeneracies.* If $E_i = E_l$ with $i \neq l$, Step 2 still works: $b = E_{ll}$ is diagonal, $\sigma_t(b) = b$, and the constant-$F$ argument gives $\omega(E_{il}) = 0$. Step 1's exponential argument is unchanged whether or not $E_i \neq E_j$.

This theorem says: in finite dimensions, the KMS condition picks out exactly the Gibbs states. It is a *characterization* of thermal equilibrium that uses only the algebraic structure $(\mathcal{A}, \sigma_t, \omega)$ and doesn't presuppose any specific Hilbert-space realization.

## 4. KMS in QFT: the example we need

In QFT — and especially for type III algebras — the KMS condition is far more general than Gibbs. The state $\omega$ in question is typically the vacuum, restricted to a wedge or other unbounded region; the flow $\sigma_t$ is typically the modular flow generated by Tomita-Takesaki.

The leading example, which we will work out fully in Week 10:

**Example 4.1 (Bisognano–Wichmann, preview).** Let $\mathcal{A}(W_R)$ be the local algebra of the right Rindler wedge in a free Wightman QFT, and let $\sigma_t$ be the *boost* automorphism (boost the algebra in the $(t, x^1)$ plane by parameter $-2\pi t$). The vacuum state $\omega_0$ restricted to $\mathcal{A}(W_R)$ is *KMS at $\beta = 1$* with respect to $\sigma$.

Equivalently, in physical units: the vacuum looks thermal at temperature $T_U = a/2\pi$ to a uniformly accelerated observer with proper acceleration $a$. This is the *Unruh effect*, here re-expressed as a KMS condition. The local algebra $\mathcal{A}(W_R)$ is type III$_1$, so there is no Gibbs density matrix — only the algebraic KMS condition.

This example is the prototype for everything in Block C and beyond. The KMS condition is the *only* characterization of thermal-equilibrium in type III, and Tomita-Takesaki + Bisognano-Wichmann tell us where to look. The boost is the canonical modular flow of the Rindler-wedge algebra.

**Example 4.2 (Two-sided Rindler — preview of TFD).** Let $\mathcal{A}(W_R), \mathcal{A}(W_L)$ be the algebras of the right and left Rindler wedges. The Minkowski vacuum, restricted to the *combined* algebra $\mathcal{A}(W_R) \otimes \mathcal{A}(W_L)$, is the *thermofield double* state of the boost generator. This will be the central example for Sem II Block 2 (CPW).

**Example 4.3 (Tolman–Ehrenfest).** In a curved spacetime with a stationary observer, the local temperature $T_{loc}$ depends on position via the gravitational redshift. The KMS condition is *local*: the algebra of observables in a small region around the observer satisfies KMS at the local temperature, even though the global temperature is not uniform. This is the algebraic version of the Tolman–Ehrenfest law.

## 5. The trace as a KMS state at all temperatures

**Proposition 5.1.** *Let $\tau$ be a faithful normal trace on a type II factor $\mathcal{M}$ (e.g., the hyperfinite II$_1$ factor). Let $\sigma_t = \mathrm{id}$ (the trivial automorphism group). Then $\tau$ is KMS at every $\beta \in \mathbb{R}$.*

**Proof.** With $\sigma_t = \mathrm{id}$, the function $t \mapsto \tau(a\sigma_t(b)) = \tau(ab)$ is constant. By tracial property, $\tau(ab) = \tau(ba)$, which is the value at $t = 0$ — and at $t + i\beta$ — and at every $t$. The constant function $F(z) := \tau(ab)$ is trivially holomorphic on any strip and has boundary values $F(t) = \tau(ab) = \tau(a\sigma_t(b))$ and $F(t + i\beta) = \tau(ab) = \tau(ba) = \tau(\sigma_t(b)a)$. $\square$

This is striking: the tracial state is KMS at *all* temperatures simultaneously, but with the trivial flow. Physically: type II factors with the trace flow have no notion of "thermal time" — the modular dynamics is degenerate. This is the algebraic content of "the trace is a uniform measure."

> **Physical picture.** A cleaner way to say it: the trace is the *infinite-temperature* state. At $\beta = 0$ the Gibbs weight $e^{-\beta H}$ is flat regardless of $H$ — all microstates equally likely, all detailed-balance ratios equal to 1 ($\hat G_- = \hat G_+$ in the boxed identity of §2.2). A state that is "KMS at every $\beta$ for the trivial flow" and a state that is "KMS at $\beta = 0$" are the same degeneracy seen from two angles: when the strip width is zero, or the flow is trivial, the analyticity condition carries no dynamical information and only traciality $\omega(ab) = \omega(ba)$ remains. The hierarchy of types now acquires a thermal reading: type II = algebras that *can* reach infinite temperature (a trace exists); type III = algebras for which infinite temperature is unreachable — every state has nontrivial thermal structure, every clock ticks.

In type III, by contrast, every *faithful normal* state has a non-trivial modular flow — non-trivial in the strong sense that it is *outer* (not implementable by any unitary inside $\mathcal{M}$). This is part of the Tomita-Takesaki theorem, applied to states represented by cyclic-separating vectors. The modular flow encodes a unique notion of thermal time intrinsic to the algebra-state pair.

## 6. The Tomita-Takesaki preview

**Theorem 6.1 (Preview of Tomita-Takesaki, full statement Week 5).** *Let $\mathcal{M}$ be a vN algebra and $\Omega$ a cyclic-separating vector for $\mathcal{M}$. Let $\omega(a) := \langle\Omega, a\Omega\rangle$ be the corresponding faithful normal state. There is a canonical positive operator $\Delta_\omega$ on the Hilbert space — the **modular operator** — and a canonical one-parameter automorphism group of $\mathcal{M}$,*
$$
\sigma^\omega_t(a) \;:=\; \Delta_\omega^{-it}\, a\, \Delta_\omega^{it},
$$
*the **modular automorphism group**, for which $\omega$ is KMS at $\beta = 1$ in the sense of Definition 2.1.*

**Sign convention.** We have chosen $\sigma^\omega_t = \mathrm{Ad}(\Delta_\omega^{-it})$ specifically so that $\beta = +1$ in our upper-strip Definition 2.1. The opposite convention $\sigma^\omega_t = \mathrm{Ad}(\Delta_\omega^{+it})$ also appears in the literature (e.g., Bratteli-Robinson Vol. II) and gives KMS at $\beta = -1$. The two are related by $t \to -t$: the same automorphism group running in opposite directions. Pick a convention and enforce it; we use $\beta = +1$ throughout this course.

This theorem is the central result of Block B. We highlight three of its features now:

### 6.1 The modular flow is canonical

The modular flow depends only on $\mathcal{M}$ and $\omega$ — no Hamiltonian needs to be chosen externally. In QFT, this means: for any vacuum state on any local algebra, there is a canonical "thermal time" determined by the algebra-state pair.

The modular flow is *intrinsic* in the strongest sense: if $\mathcal{M}_1 \cong \mathcal{M}_2$ as vN algebras and $\omega_1, \omega_2$ are corresponding states, then the modular flows are isomorphic. There is no choice of Hamiltonian or any external structure required.

### 6.2 It works in any type

The construction goes through for type I, II, and III. In type I:
- For $\mathcal{M} = \mathcal{B}(\mathcal{H}_R) \otimes 1$ acting on $\mathcal{H}_R \otimes \mathcal{H}_L$, and $\Omega$ a generic cyclic-separating vector (a purification of a faithful density matrix $\rho_\Omega$ on $\mathcal{H}_R$), the modular operator is $\Delta_\Omega = \rho_\Omega \otimes \rho_\Omega^{-1}$ (where $\rho_\Omega^{-1}$ acts on $\mathcal{H}_L$ via the GNS isomorphism).
- The modular flow on $\mathcal{B}(\mathcal{H}_R) \otimes 1$ is $\sigma^\omega_t(a) = \rho_\Omega^{-it}\, a\, \rho_\Omega^{it} = \mathrm{Ad}(e^{itK_\omega})(a)$, the Heisenberg evolution generated by the **modular Hamiltonian** $K_\omega := -\ln\rho_\Omega$ (a positive operator). One checks directly that $\omega(a\sigma_t(b))$ analytically continues to $\omega(\sigma_t(b)a)$ at $\beta = 1$, exactly as in §1.1.
- For the maximally mixed state (= tracial state), $\rho_\Omega \propto 1$, so $K_\omega \propto 1$ and the modular flow is trivial.

In type III: the modular flow is genuinely non-trivial; in fact, it is *outer* (cannot be implemented by an inner unitary in $\mathcal{M}$). Type III has a distinguished one-parameter family of dynamics built into the algebra-state pair.

### 6.3 It is non-trivial in type III

When $\mathcal{M}$ is type III, the modular flow is genuinely outer. This is the Connes–Takesaki content: type III is the unique class of factors where the modular flow has a non-trivial *cohomological* structure (as a 1-cocycle on $\mathbb{R}$), and the cohomology class is the *Connes invariant* of the type III subtype.

For type III$_1$ (the QFT case), the modular spectrum is $\mathbb{R}$ — the most non-trivial possible. This is what makes QFT inherently dynamical at the algebraic level, and why the [[2025-liu-lectures-entanglement-vna|holographic dictionary]] has such a rich structure.

### 6.4 The "thermal time" interpretation

Connes and Rovelli (1994) proposed the *thermal time hypothesis*: in a generally covariant quantum theory (gravity + matter), there is no preferred external time; rather, time emerges from the modular flow of the state we are in. The KMS condition is the "ground rule" — every physically reasonable state must be KMS for *some* flow at some temperature, and that flow is the time. In type III (the natural setting for QFT in gravity), the modular flow exists canonically; choose a state and time emerges.

This interpretation is philosophical but mathematically precise. We will use it as a guiding intuition throughout the rest of the course, especially in Block D and Sem II.

## 7. Construction of a type III factor: Powers' construction

We close the week by constructing a concrete type III factor, the *Powers factor* $\mathcal{R}_\lambda$. This will give us a hands-on example of a type III algebra with a non-trivial modular flow.

### 7.1 The setup

Fix $\lambda \in (0, 1)$. On $M_2(\mathbb{C})$, define the state
$$
\omega_\lambda(a) := \frac{1}{1+\lambda}\langle e_1, a e_1\rangle + \frac{\lambda}{1+\lambda}\langle e_2, a e_2\rangle = \mathrm{Tr}\left( \rho_\lambda \, a \right), \quad \rho_\lambda := \frac{1}{1+\lambda}\begin{pmatrix} 1 & 0 \\ 0 & \lambda\end{pmatrix}.
$$
This is a state with density matrix $\rho_\lambda$. *Crucially*, $\omega_\lambda$ is **not** the trace (unless $\lambda = 1$).

The state $\omega_\lambda$ can be written as a *Gibbs state* for the Hamiltonian $H = \mathrm{diag}(0, -\log\lambda)$ at $\beta = 1$: $\rho_\lambda = e^{-H}/Z$ with $Z = 1 + \lambda$. The modular flow on $M_2(\mathbb{C})$ is $\sigma_t^{\omega_\lambda}(a) = e^{itH} a e^{-itH}$, and it is periodic with period $\frac{2\pi}{|\log\lambda|}$ — the smallest $T$ with $e^{iTH} = 1$ on the spectrum of $H$.

### 7.2 The infinite tensor product

Consider the inductive limit $\bigotimes_{n=1}^N M_2(\mathbb{C})$ as $N \to \infty$, in the state $\omega_\lambda^{\otimes\infty}$ — the consistent product state. The C\*-completion is the *uniformly hyperfinite C\*-algebra* (UHF) of type $2^\infty$.

Form the GNS representation $\pi : (\text{UHF}) \to \mathcal{B}(\mathcal{H})$ of the state $\omega_\lambda^{\otimes\infty}$. The Hilbert space $\mathcal{H}$ is the completion of the UHF algebra in the inner product $\langle a, b\rangle = \omega_\lambda^{\otimes\infty}(b^*a)$. Take the WOT-closure $\mathcal{R}_\lambda := \pi(\text{UHF})''$.

This is the *Araki–Woods construction* (or, as Powers studied it, an *ITPFI* — infinite tensor product of finite type I — construction).

> **Physical picture.** Think of $\mathcal{R}_\lambda$ as a half-infinite spin chain in which every site is independently thermalized: each $M_2(\mathbb{C})$ carries the same two-level Gibbs state at fixed temperature. Why does this change the *type*? Because the GNS construction builds the Hilbert space from the state (Week 1), and an infinite product state remembers its entanglement structure asymptotically. In the tracial case each site is purified by a maximally entangled pair, and the accumulated entanglement is "uniform" — coarse counting survives, and a trace exists in the limit. In the non-tracial case each site's purification is a *tilted* entangled pair with Schmidt ratio $\lambda$; infinitely many tilted pairs compound into a state whose Boltzmann-weight ratios $\lambda^n$ ($n \in \mathbb{Z}$) are visible at arbitrarily large $n$ and cannot be undone by any operation acting on finitely many sites. The thermal tilt becomes a property *of the algebra*, not of the state — which is precisely the Connes invariant $S(\mathcal{R}_\lambda) = \{0\}\cup\{\lambda^n\}$. The same mechanism, with a continuum of local "temperatures" replacing the single ratio $\lambda$, is how QFT local algebras end up type III$_1$: the vacuum is an infinitely-entangled product of tilted pairs across every scale (Week 12).

### 7.3 The Powers factor

**Theorem 7.1 (Powers 1967).** *For $\lambda \in (0, 1)$, the algebra $\mathcal{R}_\lambda$ is a **hyperfinite type III$_\lambda$ factor**. Different values of $\lambda \in (0,1)$ give non-isomorphic algebras.*

**Theorem 7.2.** *For $\lambda = 1$ (the tracial case), $\mathcal{R}_1 = \mathcal{R}$, the hyperfinite II$_1$ factor.*

**Why $\mathcal{R}_\lambda$ is type III for $\lambda \in (0,1)$ — the invariant-level argument.** Powers' theorem is delicate to prove from scratch and we treat it as a **black box** (full proof: Powers 1967; Bratteli-Robinson Vol. II §6.2; Takesaki Vol. III Ch. XII). What we *can* do honestly is identify the invariant that distinguishes $\mathcal{R}_\lambda$ from type II$_1$ and from the other type-III subtypes — without simulating a proof we have not given.

The relevant invariant is the **period of the modular flow**. Apply Theorem 6.1 (Tomita-Takesaki preview) to the GNS representation of $\omega_\lambda^{\otimes\infty}$. The cyclic-separating vector is the GNS vector $\Omega_\lambda$, the modular Hamiltonian on a single tensor factor is $K_{\omega_\lambda} = -\ln\rho_\lambda = \mathrm{diag}(0, -\log\lambda) + (\log(1+\lambda))\, I$, and the modular flow on that factor is
$$
\sigma^{\omega_\lambda}_t(a) = \rho_\lambda^{-it}\, a\, \rho_\lambda^{it} = e^{itH}\, a\, e^{-itH}, \qquad H = \mathrm{diag}(0, -\log\lambda).
$$
This is **periodic in $t$ with period $T_\lambda = 2\pi/|\log\lambda|$** — at $t = T_\lambda$ the unitary $\rho_\lambda^{-iT_\lambda}$ is a scalar phase, so $\mathrm{Ad}(\rho_\lambda^{-iT_\lambda}) = \mathrm{id}$.

The modular flow on the full ITPFI $\mathcal{R}_\lambda$ is the infinite tensor product of these single-site flows, and is therefore *also periodic with period $T_\lambda$* (every site returns to the identity simultaneously). For $\lambda \in (0,1)$ this period is finite and non-zero — distinguishing $\mathcal{R}_\lambda$ from:

- **Type II$_1$** (e.g., the hyperfinite II$_1$ factor on the tracial state): the modular flow is *trivial*, so every $t$ is a period — the periodicity invariant is degenerate.
- **Type III$_1$** (the QFT case): the modular flow has *no* period — its spectrum is all of $\mathbb{R}$.
- **Type III$_0$**: degenerate limit, no useful period.

Powers' theorem says this finite, non-zero period — and the value of $\lambda$ — is enough to place $\mathcal{R}_\lambda$ in the *Connes type-III$_\lambda$ class*. In fact, distinct values of $\lambda \in (0,1)$ give *non-isomorphic* algebras: $\mathcal{R}_\lambda \cong \mathcal{R}_{\lambda'}$ iff $\lambda = \lambda'$.

**On the absence of a faithful normal trace.** The structural fact that no faithful normal trace exists on $\mathcal{R}_\lambda$ for $\lambda \neq 1$ is a separate part of Powers' theorem and we do *not* prove it here. Naive arguments using the GNS vector state $\omega_\lambda^{\otimes\infty}$ as a "trace witness" fail — Murray-von Neumann equivalence of projections is internal to the algebra (existence of a partial isometry $u \in \mathcal{R}_\lambda$ with $u^* u = p$, $u u^* = q$), and a non-tracial vector state cannot certify or rule out such equivalences. The correct argument goes through the type classification of the relative commutant of the asymptotic tail algebra, and is in the references above.

The contrast is striking:
- **$\lambda = 1$ (tracial state):** $\rho_1 = \frac{1}{2} I$, $\omega_1$ is the tracial state. The algebra is type II$_1$, with a trace and continuous-dimension projections.
- **$\lambda \in (0, 1)$ (non-tracial state):** $\rho_\lambda$ is non-tracial. The algebra is type III$_\lambda$, with no trace and all projections infinite.

A small change in the state — moving away from the tracial point — *qualitatively* changes the algebraic type. This is one of the most surprising facts in operator algebra theory and has no analog in finite-dimensional quantum mechanics.

### 7.4 The modular flow on the Powers factor

By Tomita-Takesaki (Week 5), the modular automorphism group $\sigma^\omega_t$ on $\mathcal{R}_\lambda$ is a non-trivial one-parameter group. Its key invariant:

**Theorem 7.3.** *On $\mathcal{R}_\lambda$, the modular flow is **periodic** with period $T_\lambda = \frac{2\pi}{|\log\lambda|}$. The modular flow on each tensor factor is the local Gibbs flow $\sigma^{\omega_\lambda}_t(a) = \rho_\lambda^{-it}\, a\, \rho_\lambda^{it}$ (in the $\beta = +1$ convention of §6.1).*

The full modular flow is the infinite product of these local flows. At time $T_\lambda$, each local flow has completed one period, returning to the identity. So the global modular flow is also periodic with period $T_\lambda$.

This identifies *Connes' invariant* of the type III$_\lambda$ factor with the period of the modular flow. The boundary cases:
- $\lambda \to 1$: $T_\lambda \to \infty$, flow becomes trivial — recovers the trivial-flow type II$_1$ case.
- $\lambda \to 0$: $T_\lambda \to 0$, flow becomes infinitely fast — the type III$_0$ case (limit is degenerate).
- $\lambda$ between: nontrivial periodic flow.

For type III$_1$ (the QFT case), the modular flow has *no period*: its spectrum is all of $\mathbb{R}$. This is the algebraic content of "thermal time runs forever, with no return to the starting state." We will see this concretely in Week 10 (Bisognano–Wichmann gives the boost flow, which has no period since the boost generator has full real spectrum).

### 7.5 Interpolating between the types

The family $\mathcal{R}_\lambda$ for $\lambda \in (0, 1]$ provides a continuous (in some sense) interpolation between type II$_1$ and the various type III$_\lambda$. As $\lambda \to 1$:
- The state $\omega_\lambda$ approaches the trace.
- The modular flow period goes to $\infty$.
- The type changes from III$_\lambda$ to II$_1$.

This continuous family is exceptional — most parameter changes in operator algebras are discrete (algebras either are or aren't isomorphic, with no in-between). The Powers family is a counterexample, showing that *types* can be parameterized continuously.

## 8. Where this leaves us

We now have:
- The KMS condition as the algebraic notion of thermal equilibrium.
- The verification that KMS = Gibbs in finite dimensions.
- The preview that Tomita-Takesaki, applied to a faithful normal state $\omega$ (equivalently, a cyclic-separating vector in a standard representation), produces the state's canonical modular flow $\sigma^\omega_t$; the state is KMS for this flow at $\beta = 1$ in our convention.
- A concrete type III factor (the Powers factor) and its modular flow's period (Connes' invariant).
- The thermal time interpretation: modular flow is the algebraic clock.

Block B picks up exactly here: it constructs the modular operator $\Delta$ and modular conjugation $J$ from a cyclic-separating vector, proves Tomita-Takesaki, and develops the Connes cocycle and Araki-Uhlmann relative entropy. Block C applies all this to QFT.

## 9. Looking ahead: Week 5

Next week we begin Block B with the central technical construction: given a cyclic-separating vector $\Omega$ for a vN algebra $\mathcal{M}$, define the *Tomita operator* $S$ by $Sa\Omega = a^*\Omega$, polar-decompose $S = J\Delta^{1/2}$, and identify $\Delta$ as the modular operator and $J$ as the modular conjugation. We compute these explicitly for type I (everything reduces to density-matrix language) and prove the key parts of Tomita's theorem in the type I case. The full type III statement is stated only, with references.

## 10. Problem set

**Core problems.**

**1. KMS for the Gibbs state.**
Let $\mathcal{H} = \mathbb{C}^2$, $H = \mathrm{diag}(0, E)$ with $E > 0$, $\sigma_t = \mathrm{Ad}\,e^{itH}$.
(a) Verify the KMS condition for the Gibbs state $\omega_\beta(a) = \mathrm{Tr}(\rho_\beta a)$ explicitly: pick $a = \sigma_x$, $b = \sigma_y$, compute $\omega_\beta(a \sigma_t(b))$ on the real axis and verify the holomorphic extension to $t \to t + i\beta$.
(b) Show that any other state on $M_2(\mathbb{C})$ that satisfies KMS at $\beta$ for this $\sigma_t$ must equal $\omega_\beta$. (*Hint:* follow the matrix-units argument of Theorem 3.1's $(\Rightarrow)$ direction with $H = \mathrm{diag}(0, E)$ — diagonal weighting from $a = E_{12}, b = E_{21}$, off-diagonal vanishing from $a = E_{12}, b = E_{22}$.)

**2. The trace as KMS for the trivial flow.**
On $M_n(\mathbb{C})$ with $\sigma_t = \mathrm{id}$, verify the KMS condition for the normalized trace $\tau$ at every $\beta \in \mathbb{R}$. Specifically: identify the function $F_{a,b}(z)$ explicitly and verify the boundary conditions.

**3. KMS detailed balance.**
On $M_n(\mathbb{C})$ with $H, \sigma_t = \mathrm{Ad}\,e^{itH}$:
(a) For energy eigenstates $|\xi\rangle, |\xi'\rangle$ with $H\xi = E\xi, H\xi' = E'\xi'$, show that the KMS condition forces $\omega(|\xi\rangle\langle\xi|) / \omega(|\xi'\rangle\langle\xi'|) = e^{-\beta(E - E')}$ — the thermal weighting.
(b) Use (a) to give a complete proof of Theorem 3.1 (that KMS at $\beta$ on $M_n(\mathbb{C})$ implies $\omega = \omega_{\rho_\beta}$).

**4. Powers factor: non-traciality.**
For the Powers state $\omega_\lambda^{\otimes\infty}$ on $\bigotimes_{n=1}^\infty M_2(\mathbb{C})$ with $\lambda \in (0,1)$:
(a) Find specific $a, b \in \mathcal{A}_\infty$ with $\omega_\lambda^{\otimes\infty}(ab) \neq \omega_\lambda^{\otimes\infty}(ba)$, demonstrating non-traciality.
(b) Compute $\omega_\lambda^{\otimes\infty}(a\sigma_t(b))$ for $a, b$ on a single tensor factor and identify the periodic oscillation period $T_\lambda = 2\pi/|\log\lambda|$.

**5. Connes invariant as a periodicity.**
For the Powers factor $\mathcal{R}_\lambda$, the modular period is $T_\lambda = 2\pi/|\log\lambda|$. Verify:
(a) $T_\lambda \to \infty$ as $\lambda \to 1$ (i.e., the flow becomes trivial).
(b) $T_\lambda \to 0$ as $\lambda \to 0$ (i.e., the flow becomes very fast).
(c) $T_{1/2} = 2\pi/\log 2 \approx 9.06$. Compute explicitly the modular flow at $t = T_{1/2}/4 \approx 2.26$ on the simplest non-trivial element (e.g., a single-site $\sigma_x$).

**6. KMS in QFT (warmup for Bisognano–Wichmann).**
Anticipating Week 10: consider a free 2D massless scalar field in the right Rindler wedge. The vacuum two-point function is $W(x,y) \propto \log|(x-y)^2|$ (with appropriate $i\epsilon$). The boost generator on the wedge is $K = \int_0^\infty x^1 T^{00}(x^1) dx^1$.
(a) Compute $W(x, y)$ for $x, y$ in the wedge.
(b) Verify formally that the boost flow $\sigma_t = \mathrm{Ad}(e^{2\pi i t K})$ acts on Weyl operators by $W(f) \mapsto W(f \circ B_{2\pi t})$ where $B_s$ is the boost.
(c) Check that the vacuum state, restricted to wedge observables, is KMS at $\beta = 1$ for this flow. (*Just outline; full details Week 10.*)

**Starred problems.**

**7\*. The KMS condition determines the dynamics.**
Suppose $\omega$ is a faithful state on $\mathcal{B}(\mathcal{H})$ ($\dim\mathcal{H} < \infty$) and $\omega$ is KMS at $\beta = 1$ for some one-parameter group $\sigma_t$. Show that $\sigma_t$ is uniquely determined by $\omega$. (*Hint:* identify $\sigma_t = \mathrm{Ad}\,e^{itK}$ with $K$ determined by $\omega$ via $\rho = e^{-K}$.) State the analogous result on a finite-dim type II factor.

**8\*. KMS implies passivity (Pusz–Woronowicz).**
A state $\omega$ on $\mathcal{B}(\mathcal{H})$ is *passive* (with respect to $\sigma_t = \mathrm{Ad}\,e^{itH}$) if $\omega(U^* H U) \ge \omega(H)$ for every unitary $U$ — i.e., one cannot extract energy from $\omega$ by a unitary process.
(a) Show that the Gibbs state at any $\beta > 0$ is passive.
(b) State (without proof) the converse Pusz–Woronowicz theorem: a faithful normal passive state is KMS at *some* $\beta \ge 0$. Look up the proof for reference.

**9\*. Modular flow on a tensor product.**
Verify that for $\mathcal{M} = M_n(\mathbb{C})$ and a generic non-tracial state $\omega = \omega_\rho$, the modular flow in the course convention ($\sigma^\omega_t = \mathrm{Ad}(\Delta^{-it})$, §6.1) is $\sigma^\omega_t(a) = \rho^{-it} a \rho^{it}$. Compute the period (if any) of this flow for $\rho = \mathrm{diag}(\rho_1, \ldots, \rho_n)$.

**10\*\* (Optional, hard).** Read the original Powers paper (1967) and reproduce the proof that $\mathcal{R}_\lambda$ for distinct $\lambda \in (0, 1)$ are non-isomorphic. The key invariant is the *Connes invariant* $S(\mathcal{M})$, computable from the modular spectrum $\sigma(-\log\Delta)$. In fact, $S(\mathcal{R}_\lambda) = \{0\} \cup \{\lambda^n : n \in \mathbb{Z}\}$ — a discrete set when $\lambda \in (0,1)$, vs. all of $\mathbb{R}_+$ for type III$_1$.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block A. Last revised 2026-06-11. End of Block A — the foundations of operator algebras.*
