---
title: "Week 14 — Dressed Entropy and the Modular Boundary Term"
type: lecture-notes
course: syllabus
semester: 1
week: 14
block: D
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Week 13 (crossed product), Week 7 (Connes cocycle + Araki–Uhlmann)
modified: 2026-06-11
---

# Week 14 — Dressed Entropy and the Modular Boundary Term

> *Week 13 gave us a trace where there had been none: by adjoining a modular clock to a type III$_1$ algebra, the dressed algebra is type II$_\infty$ with a faithful normal semifinite trace, unique up to scaling. This week we use that trace to define a **dressed entropy** — and prove the central technical result of the entire course: differences of dressed entropies between two normal states reproduce the **Araki–Uhlmann relative entropy** of Week 7, plus a finite **modular boundary term** carried by the clock. This boundary term is what every Sem II paper computes. In the free-field Rindler model, the dressed entropy reproduces the **generalized entropy formula** $S_{\mathrm{gen}} = A/(4 G_N) + S_{\mathrm{out}}$ that motivates the entire algebraic-gravity program.*

## 0. Reading

**Primary:**
- Witten, "Gravity and the crossed product," *JHEP* 10 (2022) 008, arXiv:2112.12828, §§3–4 — the dressed entropy and the generalized entropy.
- Bratteli & Robinson, Vol. I, §2.7 (dual weights, dressed entropy as von Neumann entropy on a type II$_\infty$ algebra).

**Secondary:**
- Chandrasekaran, Penington, Witten (CPW), "Large $N$ algebras and generalized entropy," arXiv:2209.10454, §3 — two-sided black hole version, dressed entropy = generalized entropy.
- Liu, "Lectures on entanglement, von Neumann algebras, and emergence of spacetime," arXiv:2510.07017, §§5–6 — pedagogical exposition.

**Optional research reading:**
- Ahmad & Jefferson, "Algebraic perturbation theory: traversable wormholes and generalized entropy beyond subleading order," arXiv:2501.01487 — perturbations of the dressed entropy.
- Faulkner, Li, Wang, "A modular toolkit for bulk reconstruction," *JHEP* 04 (2019) 119, arXiv:1806.10560 — modular tools in holography.
- Jensen, Sorce, Speranza, "Generalized entropy for general subregions in quantum gravity," arXiv:2306.01837 — extension of CPW.

## 1. Setup

### 1.1 Recap

Week 13 constructed, for a type III$_1$ von Neumann algebra $\mathcal{M}$ with faithful normal state $\omega$ and modular flow $\sigma^\omega$, the **modular crossed product**
$$
\hat{\mathcal{M}} \;:=\; \mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R}
$$
on $\mathcal{H} \otimes L^2(\mathbb{R}_s)$. By Connes–Takesaki, $\hat{\mathcal{M}}$ is type II$_\infty$. It carries a faithful normal semifinite trace $\hat\tau$, unique up to rescaling, satisfying the dual-scaling relation $\hat\tau \circ \theta_r = e^{-r}\,\hat\tau$.

The original algebra $\mathcal{M}$ embeds as a subalgebra via $\pi$, but the embedding $\pi(\mathcal{M}) \subset \hat{\mathcal{M}}$ is *not* trace-class: the trace on $\hat{\mathcal{M}}$ restricted to $\pi(\mathcal{M})$ is divergent on any non-zero element. The trace becomes finite only on operators that depend non-trivially on the clock $L^2(\mathbb{R}_s)$.

### 1.2 Why dressed entropy

On the type II$_\infty$ dressed algebra, we can do something we could not do on $\mathcal{M}$ alone: write a **von Neumann entropy**. Given a normal state $\hat\rho$ on $\hat{\mathcal{M}}$ with density $\hat\rho_d$ relative to the trace ($\hat\rho(x) = \hat\tau(\hat\rho_d\,x)$), define
$$
S_{\mathrm{vN}}(\hat\rho) := -\hat\tau(\hat\rho_d \log\hat\rho_d).
$$

The standard quantum-mechanical entropy formula, **on the dressed algebra**.

The catch: the trace $\hat\tau$ is only unique up to scaling, so $S_{\mathrm{vN}}(\hat\rho)$ is well-defined only **up to a state-independent additive constant**. Different choices of scaling shift all dressed entropies by the same constant. This is fine for *differences*, which are the physically meaningful quantities.

### 1.3 What we will prove

The two main results of this week:

1. **Dressed entropy is well-defined** (modulo additive constant) on the crossed product.
2. **Differences of dressed entropies reproduce Araki–Uhlmann + a modular boundary term:**
$$
\boxed{S_{\mathrm{vN}}(\hat\rho_\omega) - S_{\mathrm{vN}}(\hat\rho_\phi) \;=\; -\,S(\omega \| \phi) + (\text{modular boundary term}).}
$$
The boundary term is finite, computable, and is the technical object of the Sem II papers.

## 2. The dressed entropy formula

### 2.1 Definition

**Definition 2.1.** Let $\hat\rho$ be a normal positive linear functional on $\hat{\mathcal{M}}$ (type II$_\infty$) with $\hat\rho(x) = \hat\tau(\hat\rho_d\,x)$ for a positive operator $\hat\rho_d$ affiliated with $\hat{\mathcal{M}}$ (the **density** of $\hat\rho$). The **von Neumann entropy** of $\hat\rho$ is
$$
S_{\mathrm{vN}}(\hat\rho) := -\hat\tau(\hat\rho_d\,\log\hat\rho_d),
$$
where the right side is finite (or $+\infty$) by the spectral theorem.

### 2.2 Existence of the density

The trace $\hat\tau$ is faithful, normal, semifinite on $\hat{\mathcal{M}}$ (Theorem 3.1 of Week 13). Every normal positive linear functional $\hat\rho$ on a semifinite vN algebra has a density with respect to a faithful normal semifinite trace — this is the noncommutative Radon-Nikodym theorem.

**Lemma 2.2. [Stated only — refs: Takesaki Vol. II §V.2.]** *For any normal positive linear functional $\hat\rho$ on $\hat{\mathcal{M}}$, there exists a positive operator $\hat\rho_d$ affiliated with $\hat{\mathcal{M}}$ such that $\hat\rho(x) = \hat\tau(\hat\rho_d\,x)$ for all $x$ in a dense subalgebra. The density $\hat\rho_d$ is uniquely determined by $\hat\rho$.*

Note: $\hat\rho_d$ need not be bounded (it can be unbounded for unbounded states), but it is *affiliated* with $\hat{\mathcal{M}}$ (its spectral projections lie in $\hat{\mathcal{M}}$).

### 2.3 Properties

The dressed entropy $S_{\mathrm{vN}}$ satisfies the standard properties of the Umegaki entropy in finite dimensions:

- **Positivity (under normalization):** for a normalized state $\hat\rho$ (i.e., $\hat\rho(1) = 1$, so $\hat\tau(\hat\rho_d) = 1$), $S_{\mathrm{vN}}(\hat\rho)$ can take any real value, including negative. In a type II$_\infty$ algebra, normalized states have densities that are *not* trace-class on $\hat{\mathcal{M}}$ as a whole, so the entropy is unbounded.
- **Concavity:** $S_{\mathrm{vN}}(\alpha\hat\rho_1 + (1-\alpha)\hat\rho_2) \ge \alpha S_{\mathrm{vN}}(\hat\rho_1) + (1-\alpha)S_{\mathrm{vN}}(\hat\rho_2)$ for $\alpha \in [0, 1]$.
- **Invariance:** $S_{\mathrm{vN}}$ depends on the choice of trace $\hat\tau$. Rescaling $\hat\tau \to c\hat\tau$ shifts $S_{\mathrm{vN}} \to S_{\mathrm{vN}} - \log c$ (state-independent additive shift). So *differences* of $S_{\mathrm{vN}}$ between two states are well-defined.

The state-independent additive ambiguity is real, and it is the reason the Sem II literature talks about "generalized entropy up to a constant" or "dressed entropy modulo an additive ambiguity that drops out in differences."

> **Physical picture: why adjoining a clock renders entropy finite.** The bare type III entropy diverges because the vacuum contains entangled pairs at *every* UV scale, and a sharp geometric cut counts all of them. The dressed algebra blurs the cut. Its observables are relational — "field value when the clock reads $s$" — and a physical clock is a quantum system with energy fluctuations, hence intrinsic time uncertainty. Conditioning on the clock effectively *smears the location of the horizon* (in the Rindler model: the boost-time origin, and with it the bifurcation surface, acquires quantum spread). The deepest UV pairs straddling the cut are no longer sharply assigned to one side, so the count terminates. The entropy that remains is finite but normalization-dependent — exactly the structure of $S_{\rm gen}$: a divergent matter entropy and a counterterm-like area piece whose split is regulator-convention, while differences are physical. Witten's slogan compresses this: *in gravity there are no sharp subregions, only subregions relative to an observer, and that is why gravitational entropy is finite.*

## 3. The relation to Araki–Uhlmann

The dressed entropy on $\hat{\mathcal{M}}$ is related, but **not identical**, to the Araki–Uhlmann relative entropy on $\mathcal{M}$ from Week 7.

### 3.1 The relation theorem

**Theorem 3.1 (Dressed entropy ↔ Araki–Uhlmann + boundary term). [Stated only — refs: Witten 2022 §4; CPW 2022 §3.]** *Let $\omega, \phi$ be two faithful normal states on $\mathcal{M}$, and let $\hat\rho_\omega, \hat\rho_\phi$ be the corresponding dressed states on $\hat{\mathcal{M}}$ (constructed via the modular crossed product, with a fixed normalization of the clock). Then*
$$
S_{\mathrm{vN}}(\hat\rho_\omega) - S_{\mathrm{vN}}(\hat\rho_\phi) \;=\; -\,S(\omega \| \phi) + \mathcal{B}(\omega, \phi),
$$
*where $S(\omega\|\phi)$ is the Araki–Uhlmann relative entropy (Week 7) and $\mathcal{B}(\omega, \phi)$ is the **modular boundary term** — finite, computable from the modular Hamiltonians of $\omega$ and $\phi$ as expectation values in the clock $\mathcal{H}_{\mathrm{clock}} = L^2(\mathbb{R}_s)$.*

The sign of $-S(\omega\|\phi)$ on the RHS is because the relative entropy is non-negative ($\omega \neq \phi$ states have $S(\omega\|\phi) > 0$, so the dressed-entropy difference is *less than* the boundary term — the relative entropy "absorbs" some of the entropy).

### 3.2 What the boundary term is

The modular boundary term is the **relative modular energy** of $\omega$ measured with respect to the modular flow of the *reference* state $\phi$:
$$
\mathcal{B}(\omega, \phi) \;=\; \omega(K_\phi) - \phi(K_\phi) \;=\; \mathrm{Tr}((\rho_\omega - \rho_\phi)\,K_\phi),
$$
where $K_\phi = -\log\rho_\phi$ is the modular Hamiltonian of the **reference** state $\phi$ (formally; well-defined as a self-adjoint operator on the GNS Hilbert space via spectral theory).

**Important sign / index conventions.** The boundary term uses the modular Hamiltonian of $\phi$ (the second argument), not of $\omega$. It vanishes when $\omega = \phi$, and is generally non-zero otherwise. The combination $\mathcal{B}(\omega, \phi) = \omega(K_\phi) - \phi(K_\phi)$ involves only **differences** of $K_\phi$ expectations, so the choice of overall additive scalar in $K_\phi$ (which is ambiguous up to $\log Z$ in the finite-dim derivation) drops out.

In type III, the individual terms $\omega(K_\phi)$ and $\phi(K_\phi) = -\mathrm{Tr}(\rho_\phi\log\rho_\phi) = S_{\mathrm{vN}}(\phi)$ are formally divergent in the cut-off-free limit, but their **difference** $\mathcal{B}$ is finite. This is the algebraic content of "subtraction renormalization" for entanglement entropy in QFT.

> **Physical picture: the first law of entanglement.** Rearranged, Theorem 3.1 reads
> $$
> \Delta S_{\mathrm{vN}} = \Delta\langle K_\phi\rangle - S(\omega\|\phi),
> $$
> with $\Delta\langle K_\phi\rangle = \mathcal{B}$ the change in modular energy. This is a thermodynamic identity: at modular temperature $\beta = 1$, "$\Delta S = \Delta E - \Delta F$," with the relative entropy playing the role of the free-energy excess of $\omega$ over equilibrium. Two standard limits make it familiar. *Linear order:* for $\omega = \phi + \delta\phi$, $S(\omega\|\phi) = O(\delta^2)$ (Week 7 §7), so $\delta S = \delta\langle K_\phi\rangle$ — the **first law of entanglement entropy**, the equality of entropy and modular-energy variations that, fed through the holographic dictionary, yields the linearized Einstein equations (Faulkner et al.). *Positivity:* since $S(\omega\|\phi) \ge 0$, we get $\Delta S \le \Delta\langle K\rangle$ — the **Bekenstein bound** in its modern form (Casini): the entropy a state can carry above the vacuum is bounded by its modular energy. The boundary term is thus not a technical residue; it is the energy side of the thermodynamics of entanglement, and the Sem II papers are exercises in tracking it through gravitational dressings.

### 3.3 Comparison with the QFT story

Recall (Week 12) that in a type III$_1$ algebra:
- $-\hat\tau(\hat\rho_d\log\hat\rho_d)$ — Umegaki entropy on the dressed algebra — is well-defined.
- $-\mathrm{Tr}(\rho\log\rho)$ — naive vN entropy on the original algebra — is **not** well-defined (no trace, no density matrix). In a regulated theory it diverges as a UV cutoff is removed.

The dressed entropy is the "regulated" version, where the regulator is the modular clock. Differences of dressed entropies are finite and recover the type-III-safe relative entropy.

### 3.4 Connection to the generalized entropy

In a **holographic** setting (Sem II Block 1), the dressed entropy on $\hat{\mathcal{M}}_{\mathrm{boundary}}$ equals the **generalized entropy** of the bulk:
$$
S_{\mathrm{vN}}(\hat\rho_\omega) = \frac{A_{\mathrm{horizon}}}{4 G_N} + S_{\mathrm{out}}(\rho_\omega) + \text{const},
$$
where:
- $A_{\mathrm{horizon}}$ is the area of the bulk horizon dual to the boundary subregion;
- $S_{\mathrm{out}}$ is the entropy of bulk quantum fields outside the horizon;
- $\text{const}$ is the state-independent additive ambiguity from the trace normalization (§2.3).

This identification — dressed entropy $=$ generalized entropy — is the **central technical result of Witten 2022**. It gives the holographic dressed entropy a *physical* interpretation as the gravitational area-plus-bulk-entanglement formula of Bekenstein, Hawking, Ryu, Takayanagi.

## 4. Worked example: type-I dressed algebra

### 4.1 Setup

Take $\mathcal{M} = \mathcal{B}(\mathcal{H})$ with $\dim\mathcal{H} = n$, and $\omega(a) = \mathrm{Tr}(\rho\,a)$ a faithful state. The dressed algebra (Week 13 §5) is $\hat{\mathcal{M}} \cong \mathcal{B}(\mathcal{H}) \otimes L^\infty(\mathbb{R}_s)$, with trace
$$
\hat\tau(a \otimes f) = \mathrm{Tr}(a)\,\int f(s)\,e^{-s}\,ds.
$$

### 4.2 The dressed state

The natural dressing of $\omega$ to $\hat\omega$ on $\hat{\mathcal{M}}$ is to tensor with a normalized clock state:
$$
\hat\omega(a \otimes f) := \omega(a)\,\mu(f),
$$
where $\mu(f) = \int f(s)\,\mu(s)\,ds$ is the expectation against a probability measure $\mu$ on $\mathbb{R}_s$ — the "clock state."

For the canonical choice $\mu(s) = e^{-s}\,\mathbf{1}_{s > 0}$ (exponential on the positive half-line, normalized — heuristic, since this is the dual-weight measure), the dressed state takes the form
$$
\hat\omega = \omega \otimes \mu, \qquad \hat\rho_d = \rho \otimes \mu_d,
$$
where $\mu_d(s) = \mu(s)\cdot e^{s}$ (so that $\hat\tau(\hat\rho_d \cdot)$ reproduces $\hat\omega$).

### 4.3 The dressed entropy

The Umegaki entropy on the dressed algebra is
$$
S_{\mathrm{vN}}(\hat\omega) = -\hat\tau(\hat\rho_d \log\hat\rho_d) = -\mathrm{Tr}(\rho\log\rho)\cdot\mu(1) + (\text{measure entropy}).
$$
For a normalized $\mu$, $\mu(1) = 1$, so the first term is just $S_{\mathrm{vN}}(\omega) = -\mathrm{Tr}(\rho\log\rho)$, the original Umegaki entropy.

The second term (measure entropy) is $-\int\mu(s)\log\mu(s)\,ds$ for the clock measure $\mu$. This is the **modular boundary term in the type-I case** — entirely from the clock.

So for product dressed states,
$$
S_{\mathrm{vN}}(\hat\omega) = S_{\mathrm{vN}}(\omega) + S_{\mathrm{clock}}(\mu).
$$

The dressed entropy is the original entropy plus a clock contribution. In type I this is straightforward; in type III the original $S_{\mathrm{vN}}(\omega)$ is undefined and the "splitting" is more subtle.

### 4.4 Difference of two dressed states

For two states $\hat\omega = \omega \otimes \mu$ and $\hat\phi = \phi \otimes \mu$ (same clock $\mu$, different system states):
$$
S_{\mathrm{vN}}(\hat\omega) - S_{\mathrm{vN}}(\hat\phi) = S_{\mathrm{vN}}(\omega) - S_{\mathrm{vN}}(\phi).
$$
The clock contributions cancel.

Now compare with Araki–Uhlmann:
$$
S(\omega\|\phi) = \mathrm{Tr}(\rho_\omega(\log\rho_\omega - \log\rho_\phi)) = \mathrm{Tr}(\rho_\omega\log\rho_\omega) - \mathrm{Tr}(\rho_\omega\log\rho_\phi)
$$
(Week 7 §6). Rearranging,
$$
\mathrm{Tr}(\rho_\omega\log\rho_\omega) = S(\omega\|\phi) + \mathrm{Tr}(\rho_\omega\log\rho_\phi).
$$
The dressed-entropy difference is then
$$
\begin{aligned}
S_{\mathrm{vN}}(\omega) - S_{\mathrm{vN}}(\phi)
&= -\mathrm{Tr}(\rho_\omega\log\rho_\omega) + \mathrm{Tr}(\rho_\phi\log\rho_\phi) \\
&= -S(\omega\|\phi) - \mathrm{Tr}(\rho_\omega\log\rho_\phi) + \mathrm{Tr}(\rho_\phi\log\rho_\phi) \\
&= -S(\omega\|\phi) + \mathrm{Tr}((\rho_\phi - \rho_\omega)\log\rho_\phi) \\
&= -S(\omega\|\phi) - \mathrm{Tr}((\rho_\phi - \rho_\omega)\,K_\phi) \\
&= -S(\omega\|\phi) + \mathrm{Tr}((\rho_\omega - \rho_\phi)\,K_\phi),
\end{aligned}
$$
using $\log\rho_\phi = -K_\phi$. The last expression is
$$
\boxed{S_{\mathrm{vN}}(\omega) - S_{\mathrm{vN}}(\phi) = -S(\omega\|\phi) + \big(\omega(K_\phi) - \phi(K_\phi)\big),}
$$
where $K_\phi = -\log\rho_\phi$ is the modular Hamiltonian of the **reference** state $\phi$. The second term is the **modular boundary term** $\mathcal{B}(\omega, \phi) = \omega(K_\phi) - \phi(K_\phi) = \mathrm{Tr}((\rho_\omega - \rho_\phi)K_\phi)$. ✓

This verifies Theorem 3.1 in the type-I case: dressed-entropy difference = $-$ Araki–Uhlmann + modular boundary term.

**Sanity check.** Setting $\omega = \phi$: both sides vanish — left side trivially, right side because $S(\omega\|\omega) = 0$ and $\mathcal{B}(\omega, \omega) = 0$. ✓

**Sign convention.** The combination $\mathcal{B}(\omega, \phi)$ is sometimes called the **relative modular energy** of $\omega$ with respect to the reference flow $\sigma^\phi$. It is the expectation of $K_\phi$ in the state $\omega$ minus its expectation in the reference state $\phi$ — exactly what one would call "energy excess of $\omega$ above the reference state, measured by the reference Hamiltonian."

## 5. Worked example: free-field Rindler

The most important worked example for the Sem II program.

### 5.1 Setup

Let $\mathcal{M} = \mathcal{A}(W_R)$ for the 2D massless free scalar, with vacuum state $\omega = \omega_0$ (Minkowski). By Bisognano–Wichmann (Week 10), $\sigma^{\omega_0}_t = $ boost flow with rapidity $2\pi t$, so the modular Hamiltonian is $K_{\omega_0} = 2\pi K_{\mathrm{boost}}$ where $K_{\mathrm{boost}} = \int_0^\infty x^1 T^{00}\,dx^1$ is the boost generator.

Form $\hat{\mathcal{M}} = \mathcal{A}(W_R) \rtimes_{\sigma^{\omega_0}}\mathbb{R}$ on $\mathcal{F} \otimes L^2(\mathbb{R}_s)$. By Connes–Takesaki, type II$_\infty$.

### 5.2 The trace

The trace on $\hat{\mathcal{M}}$ is the integral kernel from Week 13 §7.3:
$$
\hat\tau(a) = \int_{-\infty}^\infty e^{-2\pi s}\,\langle 0_M \otimes \delta_s\,|\,a\,|\,0_M \otimes \delta_s\rangle\,ds.
$$
The factor $e^{-2\pi s}$ encodes the Unruh-temperature Boltzmann weight.

### 5.3 The dressed vacuum

The natural dressing of $\omega_0$ to $\hat\omega_0$ on $\hat{\mathcal{M}}$ uses the *unique* clock-state factorization that respects the dual-action structure. In practice, $\hat\omega_0$ is implemented by a vector $|\hat 0\rangle \in \mathcal{F} \otimes L^2(\mathbb{R}_s)$ of the form $|0_M\rangle \otimes |h\rangle$ where $h \in L^2(\mathbb{R}_s)$ is a *clock wavefunction* — a normalized state of the modular clock.

For the standard normalization, $h(s) = \pi^{-1/4}e^{-s^2/2}$ (a Gaussian) or $h(s) = \mathbf{1}_{s > 0}\,e^{-\pi s}$ (exponential cutoff at zero), depending on convention. Both give the same dressed entropy *up to the universal additive constant*.

### 5.4 Computing the dressed vacuum entropy

The vacuum density on $\hat{\mathcal{M}}$ satisfies $\hat\rho_d = \mathbf{1}_{\mathcal{F}} \otimes e^{-2\pi X}$ (modulo regulariztion), where $X$ is the position operator on $L^2(\mathbb{R}_s)$. This is because the dressed vacuum is supposed to match the Bisognano–Wichmann thermal state at $\beta = 2\pi$.

The dressed entropy is then
$$
S_{\mathrm{vN}}(\hat\omega_0) = -\hat\tau(\hat\rho_d \log\hat\rho_d) = -\hat\tau(\hat\rho_d \cdot (-2\pi X)) = 2\pi\,\langle X\rangle_{\hat\omega_0}.
$$
This is a finite number (under appropriate regularization), proportional to the modular Hamiltonian's expectation value in the clock.

### 5.5 A coherent-state excitation

Consider a coherent state $|\alpha\rangle = e^{i\phi(f)}|0_M\rangle$ for a test function $f$ supported in $W_R$. The corresponding state $\omega_\alpha$ on $\mathcal{A}(W_R)$ differs from $\omega_0$ by a Weyl-operator dressing. The Araki–Uhlmann relative entropy (Week 7 §7 generalized) is
$$
S(\omega_\alpha \| \omega_0) = \tfrac{1}{2}\,\sigma(f, \mathcal{F}f),
$$
where $\sigma$ is the symplectic form and $\mathcal{F}$ is a positive operator related to the modular Hamiltonian.

The dressed state $\hat\rho_{\omega_\alpha}$ on $\hat{\mathcal{M}}$ has dressed entropy
$$
S_{\mathrm{vN}}(\hat\rho_{\omega_\alpha}) - S_{\mathrm{vN}}(\hat\omega_0) = -S(\omega_\alpha\|\omega_0) + \mathcal{B}(\omega_\alpha, \omega_0),
$$
where the modular boundary term $\mathcal{B}$ is finite and computable.

### 5.6 The area law in this model

Now, **the punchline**. In the limit where the test function $f$ has support pushed toward the bifurcation surface (the boost-limit, Week 11 §4.4), the relative entropy and the boundary term combine:
$$
S_{\mathrm{vN}}(\hat\omega_0) \;\sim\; 2\pi\,\langle K_{\mathrm{boost}}\rangle_{\hat\omega_0} \;=\; 2\pi \cdot \frac{c\,L}{\epsilon} + \text{finite},
$$
where $L$ is the size of the wedge boundary, $\epsilon$ is a UV regulator, and $c$ is a universal coefficient ($c = 1$ for free 2D massless scalar). The divergent part scales as **the area of the wedge boundary** divided by a regulator — this is the **area law** of vacuum entanglement entropy, recovered from the dressed entropy of the modular crossed product.

In a 4D massless free scalar, the same calculation gives the standard 4D area-law divergence $S \sim A/\epsilon^2$. And in a holographic setting (Sem II), this becomes literally the Bekenstein–Hawking $A/(4 G_N)$ via the holographic dictionary.

**The area-law divergence is recovered algebraically from the modular crossed product.** In the free-field Rindler model, the divergent piece of the dressed vacuum entropy reproduces the standard UV-divergent vacuum entanglement entropy with the correct area scaling. Identifying this with the gravitational $A/(4G_N)$ in a *holographic* setting requires an additional input — the holographic dictionary at large $N$ — which is the content of Witten 2022 and is developed in Sem II Block 1. The crossed product alone does not produce gravity; it produces the algebraic skeleton that, in a holographic theory, equals the gravitational dressing.

## 6. The structural lesson

The crossed product + dressed entropy story gives:

1. **A trace where there was none.** On the dressed algebra $\hat{\mathcal{M}}$, the trace $\hat\tau$ exists and is unique up to scaling.

2. **A von Neumann entropy where there was none.** $S_{\mathrm{vN}}(\hat\rho) = -\hat\tau(\hat\rho_d\log\hat\rho_d)$, finite up to a state-independent additive constant.

3. **A precise relation to type-III-safe quantities.** Differences of dressed entropies = Araki–Uhlmann + modular boundary term, and both ingredients are well-defined on the original algebra $\mathcal{M}$.

4. **An area law in the free-field model.** The dressed vacuum entropy on the Rindler wedge has the expected $\mathrm{area}/\epsilon^{d-1}$ divergence, matching the standard QFT entanglement-entropy scaling.

5. **A bridge to holography.** Under the additional input of the holographic dictionary at large $N$ (Witten 2022), the dressed entropy of a boundary subregion equals the **generalized entropy** $A/(4G_N) + S_{\mathrm{out}}$ of the corresponding bulk wedge. This identification — *dressed entropy = generalized entropy* — is a theorem of holographic QFT, separate from the operator-algebraic construction of the crossed product itself.

This is the algebraic skeleton on which the entire Sem II program is built.

## 7. What to take away

- **Definition:** dressed entropy $S_{\mathrm{vN}}(\hat\rho) = -\hat\tau(\hat\rho_d\log\hat\rho_d)$ on the type II$_\infty$ dressed algebra, where $\hat\rho_d$ is the density of $\hat\rho$ relative to the dressed trace.
- **Modulo additive constant:** $S_{\mathrm{vN}}$ is well-defined up to a state-independent additive shift coming from the trace's $e^{-r}$ rescaling under the dual action.
- **Stated only (Theorem 3.1):** differences of dressed entropies = $-$ Araki–Uhlmann relative entropy + modular boundary term. The boundary term is finite and is the central object of Sem II.
- **Worked (type I):** $S_{\mathrm{vN}}(\hat\omega) = S_{\mathrm{vN}}(\omega) + S_{\mathrm{clock}}(\mu)$ for product dressed states.
- **Worked (free-field Rindler):** $S_{\mathrm{vN}}(\hat\omega_0) \sim$ area-law divergence of vacuum entanglement entropy, as expected.
- **Holographic punchline (Witten 2022; requires holographic dictionary as additional input):** in a CFT-gravity duality at large $N$, dressed entropy of boundary subregion = generalized entropy of bulk wedge $= A/(4 G_N) + S_{\mathrm{out}}$. This identification is a theorem of holographic QFT; it equates the algebraic dressed entropy with the gravitational Bekenstein–Hawking + Ryu–Takayanagi formula.

## 8. Looking ahead

Week 15 closes Block D and prepares the bridge to Sem II by introducing the **thermofield double** (TFD) state and its role in two-sided constructions. The Minkowski vacuum, viewed across the two-sided Rindler split, is literally the TFD of the boost Hamiltonian. The two-sided eternal black hole in holography is dual to a CFT in the TFD state. The dressing by the ADM Hamiltonian (Sem II Block 1) of the boundary algebra is the gravitational counterpart of the modular crossed product. **All of Sem II is, in one sentence, the application of the Block D machinery to specific physical settings.**

## 9. Problem set

**Core problems.**

**1. Density of a dressed state.** For $\hat{\mathcal{M}} = \mathcal{B}(\mathcal{H}) \otimes L^\infty(\mathbb{R})$ and $\hat\omega = \omega \otimes \mu$ with $\omega(a) = \mathrm{Tr}(\rho a)$ and $\mu(f) = \int f(s)\mu(s)\,ds$, identify the density $\hat\rho_d$ with respect to the trace $\hat\tau(a \otimes f) = \mathrm{Tr}(a)\int f(s)e^{-s}\,ds$. (*Hint:* solve $\hat\tau(\hat\rho_d \cdot (a \otimes f)) = \omega(a)\mu(f)$ for $\hat\rho_d$.)

**2. Dressed entropy of a product state.** Compute $S_{\mathrm{vN}}(\hat\omega)$ for $\hat\omega = \omega \otimes \mu$ as in §4.3. Verify $S_{\mathrm{vN}}(\hat\omega) = S_{\mathrm{vN}}(\omega) + S_{\mathrm{clock}}(\mu)$ explicitly.

**3. Difference of dressed entropies in type I.** Verify Theorem 3.1 in the type-I case: for $\hat\omega = \omega \otimes \mu, \hat\phi = \phi \otimes \mu$,
$$
S_{\mathrm{vN}}(\hat\omega) - S_{\mathrm{vN}}(\hat\phi) = -S(\omega\|\phi) + \mathcal{B}(\omega, \phi)
$$
with $\mathcal{B}(\omega, \phi) = \omega(K_\phi) - \phi(K_\phi) = \mathrm{Tr}((\rho_\omega - \rho_\phi)K_\phi)$ where $K_\phi = -\log\rho_\phi$ is the modular Hamiltonian of the reference state $\phi$.

**4. Vanishing boundary term.** Show that the modular boundary term $\mathcal{B}(\omega, \phi)$ vanishes when $\omega$ and $\phi$ have the same modular flow (equivalently: the same modular Hamiltonian, up to additive scalar). In this case, dressed-entropy difference = $-$ Araki–Uhlmann.

**5. Area-law warmup.** For the free 2D massless scalar restricted to the half-line $\{x^1 > 0\}$ at fixed time, use a UV regulator $\epsilon$ and compute the leading-order dressed vacuum entropy. Show it diverges as $c\log\epsilon + \text{const}$ for the central charge $c = 1$. This is the 2D analog of the 4D area law.

**Starred problems.**

**6\*. Dressed entropy of a coherent state in free-field Rindler.** For a Weyl-operator coherent state $|\alpha\rangle = e^{i\phi(f)}|0_M\rangle$ with $f$ supported in $W_R$, compute the dressed-entropy difference $S_{\mathrm{vN}}(\hat\rho_\alpha) - S_{\mathrm{vN}}(\hat\omega_0)$ to leading order in $|\alpha|$. Express the result in terms of $\sigma(f, f)$ (symplectic form) and a boundary term involving the modular Hamiltonian.

**7\*. Verify the boost-limit.** Show that in the limit where $f$ approaches the bifurcation surface (boost rapidity $\eta \to \infty$), the modular boundary term in Problem 6 becomes the dominant contribution to the dressed entropy.

**8\*. Holographic identification.** In a 2D CFT with $c = 1$ on a boundary interval $I = [-L, L]$ at fixed time, the bulk dual is an AdS$_3$ wedge. The vacuum is dual to pure AdS$_3$; the dressed entropy of the boundary interval should equal $\frac{c}{3}\log(2L/\epsilon)$ (Calabrese–Cardy) plus the bulk RT contribution. Verify the area-law part of this and discuss what "$S_{\mathrm{out}}$" looks like in this exactly-solvable setting.

**Project problems.**

**9. Read Witten 2022 §4 (generalized entropy).** Reproduce the identification $S_{\mathrm{vN}}(\hat\rho) = A/(4 G_N) + S_{\mathrm{out}} + \text{const}$ in the holographic setting. Identify each ingredient (modular Hamiltonian, ADM dressing, trace formula).

**10. Read AAJ §2–3 (algebraic perturbation theory).** Identify how the Connes cocycle (Week 7) enters as a perturbation around the unperturbed dressed entropy. Verify that the AAJ "leading correction" is the modular boundary term computed perturbatively in the deformation parameter.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block D. Last revised 2026-06-11.*
