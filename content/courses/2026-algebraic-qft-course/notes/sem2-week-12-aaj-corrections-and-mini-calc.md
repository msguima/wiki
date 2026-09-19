---
title: "Sem II Week 12 — Ahmad–Jefferson II: Corrections Beyond Subleading Order (Mini-Calc 4)"
type: lecture-notes
course: syllabus
semester: 2
week: 12
block: 4
duration: 4 hours (computational lecture — the central mini-calculation)
prerequisites: Sem II Wk 11 (cocycle perturbation, GJW); Sem I Wks 7, 14
target_paper: "Ahmad & Jefferson, arXiv:2501.01487 §§4–5"
modified: 2026-08-23
---

# Sem II Week 12 — Ahmad–Jefferson II: Corrections Beyond Subleading Order (Mini-Calc 4)

> *This is the technical centerpiece of Semester II. Last week we built the cocycle perturbation series and the free-field GJW analog. This week we compute: take the dressed Rindler-Rindler algebra, perturb the dressed TFD state by the GJW-analog cocycle, and evaluate the **dressed-entropy correction to second order in $g$**. Ahmad–Jefferson find **20 distinct corrections at quadratic order** in the holographic setting; we organize them, compute the free-field analog of the leading ones explicitly, and identify which survive without holographic input and which are holography-specific. This is **Mini-Calc 4**, and the full write-up is the basis for the student's final paper.*

## 0. Reading

**Primary:**
- Ahmad & Jefferson, arXiv:2501.01487, **§§4–5** (the second-order corrections; the enumeration of 20 terms).
- Sem II Wk 11 (cocycle perturbation series, GJW analog).
- Sem I Wk 14 (dressed entropy and the $-S(\omega\|\phi) + \mathcal{B}(\omega,\phi)$ structure).

**Secondary / gentler:**
- Sem II Wks 3, 7 (Witten/CPW dressed-entropy mini-calcs — the unperturbed versions of this one).
- Sem I Wk 7 (relative entropy second-order = energy variance; the heat-capacity physical picture).

**Optional research reading:**
- Lashkari, Liu, Rajagopal, "Perturbation theory for the logarithm of a positive operator," arXiv:1811.05619.
- Faulkner, Li, "Bulk locality from modular flow," arXiv:1806.10560.

## 1. The structure of the calculation

### 1.1 What we compute

We want
$$
\Delta S := S_{\mathrm{vN}}(\hat\omega_V) - S_{\mathrm{vN}}(\hat\omega_0)
$$
to second order in the GJW coupling $g$, where $\hat\omega_0$ is the dressed TFD-analog vacuum and $\hat\omega_V$ is its cocycle-perturbation by $V = g\,W(f_L)W(f_R)$ (Sem II Wk 11 §5).

### 1.2 The organizing identity

The whole calculation hangs on the Sem I Wk 14 dressed-entropy difference formula:
$$
S_{\mathrm{vN}}(\hat\omega_V) - S_{\mathrm{vN}}(\hat\omega_0) = -S(\omega_V\|\omega_0) + \mathcal{B}(\omega_V, \omega_0),
$$
with the modular boundary term $\mathcal{B}(\omega_V,\omega_0) = \omega_V(K_0) - \omega_0(K_0)$, $K_0 = -\log\rho_0$ the unperturbed modular Hamiltonian (template §Convention Rules: reference state's modular Hamiltonian).

So $\Delta S$ splits into two perturbative pieces:
$$
\boxed{\Delta S = \underbrace{-S(\omega_V\|\omega_0)}_{\text{relative-entropy piece}} + \underbrace{\big[\omega_V(K_0) - \omega_0(K_0)\big]}_{\text{modular-energy / boundary piece}}.}
$$

> **Physical picture.** The two pieces have the same split as the generalized entropy itself (Sem II Wk 10 §2.1): the boundary/modular-energy piece is the **area** response — how much the perturbation changes the expectation of the (unperturbed) modular Hamiltonian, i.e. the horizon-area shift via the first law; the relative-entropy piece is the **bulk-matter** response, the distinguishability of the perturbed state from the vacuum. AAJ's "20 corrections" are the distinct ways these two pieces receive contributions at order $g^2$ once you expand $\omega_V$ via the cocycle. Computing $\Delta S$ is therefore computing $\delta S_{\rm gen}$ for the traversed wormhole — area-shift plus matter-entropy-shift — at second order.

### 1.3 Order counting, and what actually vanishes at first order

The cocycle is $u_t = 1 + u^{(1)} + u^{(2)} + \cdots$ with $u^{(n)} = O(g^n)$ (Sem II Wk 11 §2.2), and the perturbed state expands as $\omega_V = \omega_0 + g\,\omega^{(1)} + g^2\,\omega^{(2)} + \cdots$. Expanding the organizing identity term by term:

**The relative-entropy piece starts at $g^2$.** Relative entropy is non-negative and vanishes only when the two states coincide, so as a function of $g$ it has a minimum at $g=0$; its Taylor expansion therefore has no linear term. This is a genuine consequence of positivity and holds for any perturbation.

**The boundary piece starts at $g^1$ in general.** Positivity says nothing about $\mathcal{B}$, and in general $\mathcal{B}$ does have a linear term. Computing it in the type-I model with $\rho_V \propto e^{-(K_0+V)}$, the Kubo (Duhamel) formula gives $\delta\rho = -\int_0^1 d\lambda\,\rho_0^{1-\lambda}\big(V - \langle V\rangle_0\big)\rho_0^{\lambda}$ at first order, and since $\rho_0$ commutes with $K_0$ the $\lambda$-integral is trivial under the trace:
$$
\mathcal{B}^{(1)} = \mathrm{Tr}\big(\delta\rho\,K_0\big) = -\Big(\langle V K_0\rangle_0 - \langle V\rangle_0\langle K_0\rangle_0\Big).
$$
So at first order the whole effect is the boundary term,
$$
\boxed{\;\Delta S^{(1)} = \mathcal{B}^{(1)} = \delta\langle K_0\rangle,\;}
$$
which is the **first law of entanglement**: to linear order the entropy change equals the modular-energy change. It is not zero as a matter of principle, and saying so would be the wrong lesson to take from positivity of relative entropy.

**Why it nevertheless vanishes for GJW.** The leading effect in the GJW problem *is* $O(g^2)$, but for a specific structural reason worth isolating. **[Proved, given the stated hypothesis.]** Suppose the perturbation is invariant under the modular conjugation of the unperturbed state, $JVJ = V$. For the TFD this is the statement that the coupling treats the two boundaries symmetrically, and it holds for $V = g\,\mathcal{O}_L\mathcal{O}_R$ with matched operators, since $J$ exchanges the two sides and the two factors commute:
$$
J\,(\mathcal{O}_L\mathcal{O}_R)\,J = (J\mathcal{O}_LJ)(J\mathcal{O}_RJ) = \mathcal{O}_R\mathcal{O}_L = \mathcal{O}_L\mathcal{O}_R .
$$
Now use two standard facts: $J\Omega = \Omega$, and $J K_0 J = -K_0$ (because $J\Delta J = \Delta^{-1}$, Sem I Wk 5). For an antiunitary $J$ fixing $\Omega$, expectation values obey $\langle JAJ\rangle_0 = \overline{\langle A\rangle_0}$. Since $\rho_0$ commutes with $K_0$ we have $\langle VK_0\rangle_0 = \langle K_0V\rangle_0 = \tfrac12\langle\{V,K_0\}\rangle_0$, which is real, so
$$
\langle VK_0\rangle_0 = \overline{\langle VK_0\rangle_0} = \big\langle J(VK_0)J\big\rangle_0 = \big\langle V\,(-K_0)\big\rangle_0 = -\langle VK_0\rangle_0
\;\Longrightarrow\; \langle VK_0\rangle_0 = 0 .
$$
The same argument applied to $K_0$ alone gives $\langle K_0\rangle_0 = 0$. Hence $\mathcal{B}^{(1)} = 0$, and the leading correction is $O(g^2)$. $\square$

> **Physical picture.** The vanishing is a symmetry statement, not a positivity statement, and the distinction matters when the symmetry is broken. $K_0$ for the TFD is $\beta_H(H_R - H_L)$ — an *antisymmetric* quantity, boosting one side forward and the other backward — while a symmetric coupling is even under the exchange. An even perturbation cannot shift the expectation of an odd operator, so the first-order area response is zero and the wormhole's leading reaction is quadratic in the coupling. Turn on an *asymmetric* deformation — couple the boundaries with unequal weights — and a first-order term reappears, with the throat responding linearly. This is worth remembering, because the $O(g^2)$ counting that organizes all of AAJ is a consequence of a symmetry that a more general deformation would not respect.

## 2. The leading correction, computed in a model

Before assembling the free-field calculation, it is worth doing the whole thing once in a setting where every quantity is a $2\times2$ matrix and all three terms of the organizing identity come out in closed form. This is the Week 11 warmup, now carried through to the entropy. **[Computed — model case, every step inline.]**

### 2.1 Setup

Take $\mathcal{M} = M_2(\mathbb{C})$ with $K = \mathrm{diag}(0,\varepsilon)$, so that
$$
\rho_0 = \frac{1}{Z_0}\begin{pmatrix}1&0\\0&e^{-\varepsilon}\end{pmatrix},\qquad Z_0 = 1 + e^{-\varepsilon},\qquad K_0 = -\log\rho_0 = K + \log Z_0,
$$
and perturb with the off-diagonal $V = v\,\sigma_x$, so that $\rho_V = e^{-(K+V)}/Z_V$. Note that $V$ is off-diagonal in the modular eigenbasis, which is this model's version of the symmetry hypothesis above: $\langle V\rangle_0 = 0$ and $\langle VK_0\rangle_0 = 0$, because a purely off-diagonal matrix has no diagonal part to pair with a diagonal $\rho_0K_0$. So the first-order term vanishes here too, and the leading effect is $O(v^2)$.

### 2.2 The spectrum

Everything follows from diagonalizing $K + V = \begin{pmatrix}0&v\\v&\varepsilon\end{pmatrix}$, whose eigenvalues are
$$
E_\pm = \frac{\varepsilon \pm \sqrt{\varepsilon^2+4v^2}}{2}
= \begin{cases}\varepsilon + \dfrac{v^2}{\varepsilon} + O(v^4)\\[2mm] -\dfrac{v^2}{\varepsilon} + O(v^4).\end{cases}
$$
Writing $\delta := v^2/\varepsilon$, the perturbation pushes the two levels apart by $2\delta$ — ordinary level repulsion, and the only effect that survives at this order.

### 2.3 The three quantities

Using $S_{\mathrm{vN}} = \log Z + \langle E\rangle$ for a Gibbs state and expanding to first order in $\delta$ (which is already $O(v^2)$),
$$
Z_V = e^{\delta} + e^{-\varepsilon-\delta} = Z_0 + \delta\big(1 - e^{-\varepsilon}\big) + O(v^4),
$$
and carrying the same expansion through $\langle E\rangle_V$ and collecting terms, the entropy difference is
$$
\Delta S = -\frac{2v^2 e^{-\varepsilon}}{\big(1+e^{-\varepsilon}\big)^2} + O(v^4)
\;=\; \boxed{\;-\frac{v^{2}}{2\cosh^{2}(\varepsilon/2)}\;} + O(v^4).
$$
For the two pieces separately, the relative entropy at second order is most easily obtained from the Kubo–Mori formula of §2.4 below, which gives
$$
S(\omega_V\|\omega_0) = \frac{v^{2}}{\varepsilon}\tanh\frac{\varepsilon}{2} + O(v^4),
$$
and the boundary term then follows from the identity $\mathcal{B} = \Delta S + S(\omega_V\|\omega_0)$:
$$
\mathcal{B}(\omega_V,\omega_0) = \frac{v^{2}}{\varepsilon}\tanh\frac{\varepsilon}{2} \;-\; \frac{v^{2}}{2\cosh^{2}(\varepsilon/2)} + O(v^4).
$$

**Three checks.** Each of these can be verified independently, and each catches a different kind of error.

1. *Sign.* $\Delta S < 0$ for all $\varepsilon$ and all $v \ne 0$. Level repulsion sharpens the eigenvalue distribution, so the state becomes more pure and the entropy falls. Note that $S(\omega_V\|\omega_0) > 0$, as positivity requires.
2. *Infinite temperature, $\varepsilon\to0$.* Here $\rho_0 = \mathbb{1}/2$ and $K_0$ is a multiple of the identity, so $\mathcal{B} \to 0$ identically and $\Delta S = -S(\omega_V\|\omega_0) \to -v^2/2$. This can be checked against the exact answer at $\varepsilon = 0$: the eigenvalues of $V$ are $\pm v$, so $S = \log(2\cosh v) - v\tanh v = \log 2 - v^2/2 + O(v^4)$, which agrees.
3. *Zero temperature, $\varepsilon\to\infty$.* Now $\Delta S \to -2v^2e^{-\varepsilon} \to 0$: a pure state has no entropy to lose. Both $\mathcal{B}$ and $S(\omega_V\|\omega_0)$ tend to $v^2/\varepsilon$, which is exactly second-order Rayleigh–Schrödinger: the excited level is populated with probability $(v/\varepsilon)^2$ and carries modular energy $\varepsilon$.

### 2.4 The Kubo–Mori metric, stated correctly and checked

The second-order relative entropy of nearby states is governed by the **Kubo–Mori (Bogoliubov) metric**. In the type-I model, for $\rho_V = \rho_0 + \delta\rho$ with $\mathrm{Tr}\,\delta\rho = 0$,
$$
S(\omega_V\|\omega_0) = \frac{1}{2}\int_0^\infty \! ds\;\mathrm{Tr}\Big[\delta\rho\,\big(\rho_0+s\big)^{-1}\delta\rho\,\big(\rho_0+s\big)^{-1}\Big] + O(\delta\rho^3),
$$
where the $s$-integral is the integral representation of the derivative of the logarithm, $\log$ being the source of all the non-commutativity. The expression is manifestly positive, which is the second-order face of $S \ge 0$.

Applying it to the model: at first order the Kubo formula gives $\delta\rho$ purely off-diagonal, with
$$
(\delta\rho)_{12} = (\delta\rho)_{21} = -\frac{v\,(1-e^{-\varepsilon})}{Z_0\,\varepsilon} =: w .
$$
With $\rho_0 = \mathrm{diag}(p_1,p_2)$ and $\delta\rho = w(E_{12}+E_{21})$, the trace evaluates to $2w^2/\big[(p_1+s)(p_2+s)\big]$, so
$$
S(\omega_V\|\omega_0) = w^{2}\!\int_0^\infty\!\frac{ds}{(p_1+s)(p_2+s)} = w^{2}\,\frac{\log(p_1/p_2)}{p_1-p_2}
= w^{2}\,\frac{\varepsilon\,Z_0}{1-e^{-\varepsilon}} = \frac{v^{2}}{\varepsilon}\,\frac{1-e^{-\varepsilon}}{1+e^{-\varepsilon}},
$$
which is $\tfrac{v^2}{\varepsilon}\tanh(\varepsilon/2)$, the value quoted in §2.3. The metric formula and the direct diagonalization agree.

> **Physical picture.** The model already contains the whole structure AAJ organize in the holographic setting. The **relative-entropy piece** grows like $v^2/\varepsilon$ at low temperature and saturates at $v^2/2$ at high temperature — it measures how distinguishable the perturbed state has become, and it always lowers the dressed entropy. The **boundary piece** measures how much modular energy the perturbation deposited, and it always raises it. Their competition is decided by the temperature: at $\varepsilon\to0$ the boundary term switches off entirely and the entropy strictly decreases, while at large $\varepsilon$ the two nearly cancel and $\Delta S$ is exponentially small. In the wormhole problem the same two numbers are the area response and the bulk-matter response, and the same competition decides whether the traversal raises or lowers $S_{\rm gen}$. What the model does not have is a clock sector, which is where the genuinely gravitational corrections live.

## 3. The 20 corrections

### 3.1 Where they come from, and how to count them

AAJ §§4–5 enumerate the distinct $O(g^2)$ contributions. They arise from the combinatorics of expanding, to second order, three nested structures:

1. the cocycle $u_t = 1 + u^{(1)} + u^{(2)}$, which reaches order $g^2$ in two ways — one insertion of $u^{(2)}$, or two of $u^{(1)}$;
2. the logarithm $\log\hat\rho_V$ in the entropy, whose expansion around $\hat\rho_0$ does not truncate because $\delta\hat\rho$ does not commute with $\hat\rho_0$ (the Lashkari–Liu–Rajagopal expansion, and the source of the $s$-integral we met in §2.4);
3. the trace pairing on the dressed algebra, which factorizes into a matter sector and a clock sector.

**How the counting works.** It is worth seeing the shape of the enumeration rather than accepting a number. Each $O(g^2)$ term is specified by three independent choices:

- **Where the two insertions sit.** With two perturbation insertions and two sectors (matter $m$, clock $c$), the unordered assignments are $(m,m)$, $(m,c)$, $(c,c)$ — three families. This is the grouping AAJ use to organize the result.
- **Which expansion produced them.** A given family receives contributions both from $u^{(2)}$ (one second-order cocycle insertion) and from $u^{(1)}\!\cdot u^{(1)}$ (two first-order ones), and these are genuinely different terms because the modular-time integrals differ — nested $\int_0^t\!\int_0^{s_1}$ versus factorized $\int_0^t\!\int_0^t$.
- **How the modular flow connects them.** Within each of the above, the two insertions may be separated by the modular flow in either order, and the non-commutativity of $\delta\hat\rho$ with $\hat\rho_0$ means the $\lambda$- or $s$-integral of the log expansion does not collapse — so orderings that would be identical classically remain distinct.

Multiplying these choices and discarding those that vanish by the symmetry argument of §1.3 is what produces AAJ's enumeration. **A caution on the number itself:** "20" is AAJ's count under *their* grouping conventions — what counts as one term rather than two depends on whether one keeps the $\lambda$-integrals unevaluated, whether Hermitian conjugate pairs are counted once or twice, and whether clock-sector terms that differ only by which side's clock is used are identified. Reproducing exactly 20 is an exercise against §§4–5 of the paper, and it is Problem 5\* below. What the course asserts independently is the *structure*: three sectors, two cocycle routes into each, and orderings that do not collapse. **[Stated — refs: AAJ §§4–5. The count is theirs; the structural decomposition is what we use.]**

> **Physical picture.** Twenty looks like a lot, but the structure is simple: each correction is one way of distributing two insertions of the perturbation across (matter, matter), (matter, clock), or (clock, clock), with the modular flow connecting them at various modular-time orderings. The "beyond subleading order" in AAJ's title means precisely this — the leading ($g^2$) generalized-entropy change is not a single term but a structured sum, and getting it right requires tracking how the perturbation reshuffles *both* the bulk matter entanglement *and* the horizon area, including their cross-talk. The cross terms $(m,c)$ are the most interesting: they are where "the matter falling in changes the area, which changes the matter entanglement" is encoded algebraically. Note that the model of §2 has only the $(m,m)$ family, which is why it produced a single clean answer rather than a sum.

### 3.2 Which survive in the free-field analog

The skeleton's key question. Of the 20:

- **Matter-sector terms survive.** They are computable from Bisognano–Wichmann modular data alone — the free-field analog reproduces them via the boost-evolved Weyl bilinears (§4 below).
- **Clock/area-sector terms partially survive.** The clock sector exists in the free-field crossed product (Sem II Wk 6–7), so the modular-energy shift is computable; but its *identification with $\delta A/4G_N$* needs the holographic dictionary.
- **Cross terms requiring the full holographic algebra do not survive.** Terms that mix the genuine type III$_1$ holographic structure with the gravitational clock in a way that has no Bisognano–Wichmann counterpart are **holography-specific** — the free-field analog cannot see them.

**Claim (Example-only / hypothesis-explicit). [Refs: AAJ §5.]** *In the free-field Rindler-Rindler analog, the matter-sector and clock-sector corrections to $\Delta S$ are reproduced exactly; the holography-specific cross terms are absent. The free-field calculation therefore captures the *structure* of AAJ's result but not the full bulk content.*

This is the honest scoping the course maintains throughout: the free-field analog is a controlled laboratory that reproduces the algebraic skeleton, with the holographic-specific physics flagged as input.

## 4. Mini-Calc 4: the free-field computation

The deliverable. (Skeleton's Mini-Calc 4 — students compute parts, instructor consolidates.)

### 4.1 Setup

- **Algebra:** $\hat{\mathcal{A}}(W_R) = \mathcal{A}(W_R)\rtimes_{\rm boost}\mathbb{R}$, the dressed Rindler algebra (Sem II Wk 6).
- **Unperturbed state:** $\hat\omega_0$ = dressed TFD-analog (Minkowski vacuum × clock wavefunction $h$), Sem II Wk 7 §4.
- **Perturbation:** $V = g\,W(f_L)W(f_R)$ with bumpified Haar wavelet test functions $f_L \in W_L$, $f_R \in W_R$ (Sem II Wk 8, Wk 11 §5).

### 4.2 Tasks

1. **Cocycle.** Write $u_t$ to first order (Sem II Wk 11 §5.3): the boost-evolved Weyl bilinear. Compute the relevant matrix elements via the symplectic form $\sigma(f_L\circ\Lambda, f_R\circ\Lambda)$.

2. **Perturbed state.** Build $\hat\omega_V$ from $u_t$ and $\hat\omega_0$. The Gaussian structure of the free field makes all expectations computable in closed form (products of Weyl two-point functions, Sem II Wk 8 §2).

3. **Relative-entropy piece.** Compute $S(\omega_V\|\omega_0)$ to $O(g^2)$ using the Kubo–Mori metric (§2.4). For the free field this is a Gaussian integral over the symplectic data:
$$
S(\omega_V\|\omega_0) = \tfrac{1}{2}g^2\,\sigma(f_L, f_R)\,P\,\sigma(f_L, f_R) + O(g^3),
$$
with $P$ a positive kernel built from $\tanh(\pi K_{\rm boost})$ (Sem II Wk 7 §5.3).

4. **Modular-energy piece.** Compute $\omega_V(K_0) - \omega_0(K_0)$ to $O(g^2)$, with $K_0 = 2\pi K_{\rm boost}$ the boost modular Hamiltonian. This is the boost-energy injected by the deformation.

5. **Assemble $\Delta S$.** Combine: $\Delta S = g^2(\text{boost-energy shift} - \tfrac12\,\text{Kubo–Mori})$. Both pieces are explicit functions of the wavelet test functions.

6. **Compare with AAJ.** Identify which of the 20 corrections this reproduces (the matter-sector and clock-sector ones) and which are absent (holography-specific cross terms).

### 4.3 The leading correction, explicitly

Assembling the pieces, the free-field analog gives
$$
\Delta S = g^{2}\Big(\underbrace{2\pi\,\big\langle \delta K_{\rm boost}\big\rangle}_{\text{modular-energy / area}} \;-\; \underbrace{\tfrac{1}{2}\,\big\|\sqrt{P}\,\varsigma(f_L,f_R)\big\|^{2}}_{\text{Kubo–Mori / matter}}\Big) + O(g^{3}),
$$
with $\varsigma$ the symplectic form of the boosted test functions and $P$ the positive kernel built from $\tanh(\pi K_{\rm boost})$ (Sem II Wk 7 §5.3). Both pieces are explicit functionals of the wavelet test functions, finite, and sign-definite: the boost-energy term is positive (energy injected), the Kubo–Mori term negative (distinguishability increases).

The structure is exactly the model result of §2.3 with the two-level modular spectrum replaced by the continuous boost spectrum. The dictionary between the two is worth writing down, because it is the fastest way to see what the free-field calculation adds and what it does not:

| Model (§2) | Free-field analog (§4) |
|---|---|
| level splitting $\varepsilon$ | continuous boost spectrum, weight $\tanh(\pi K_{\rm boost})$ |
| $S(\omega_V\Vert \omega_0) = \tfrac{v^2}{\varepsilon}\tanh\tfrac{\varepsilon}{2}$ | $\tfrac12 g^2\Vert \sqrt P\,\varsigma(f_L,f_R)\Vert ^2$ — the same $\tanh$ weight, integrated over the spectrum |
| $\mathcal{B} = \langle K\rangle_V - \langle K\rangle_0$, a number | $2\pi g^2\langle\delta K_{\rm boost}\rangle$, a test-function functional |
| no clock sector | clock sector present (Sem II Wk 6–7), carrying the area interpretation |

The $\tanh$ is not a coincidence: it is the same Kubo–Mori denominator $\log(p_1/p_2)/(p_1-p_2)$ of §2.4, evaluated on a thermal spectrum rather than on two levels. This is why the model computation is worth doing first — the free-field answer is its continuum limit, and a student who has done §2 by hand knows what every factor in §4.3 is doing.

### 4.4 Deliverable

Each student writes 2 pages of their assigned part (cocycle / relative-entropy piece / modular-energy piece / assembly / AAJ comparison). The instructor consolidates into the full Mini-Calc 4 writeup, which is the technical basis for the final paper.

## 5. What to take away

- **Organizing identity:** $\Delta S = -S(\omega_V\|\omega_0) + [\omega_V(K_0) - \omega_0(K_0)]$ — matter-entropy piece plus modular-energy/area piece, the perturbative $\delta S_{\rm gen}$.
- **First order is the first law, not zero:** $\Delta S^{(1)} = \delta\langle K_0\rangle$. Positivity of relative entropy kills only the relative-entropy piece's linear term. For GJW the boundary term's linear piece vanishes as well, but by a *symmetry* argument — $JVJ = V$ while $JK_0J = -K_0$ — and an asymmetric deformation would restore it.
- **The 20 corrections** are the distinct $O(g^2)$ contributions from expanding cocycle × log × trace-pairing, grouped into matter / clock / cross-sector terms.
- **Free-field analog (example-only):** reproduces the matter- and clock-sector corrections exactly via boost-evolved Weyl bilinears; the holography-specific cross terms are absent. The analog captures the structure, not the full bulk content.
- **Model result, in closed form (§2):** for $M_2$ with $K = \mathrm{diag}(0,\varepsilon)$ and $V = v\sigma_x$,
$$
\Delta S = -\frac{v^2}{2\cosh^2(\varepsilon/2)},\qquad
S(\omega_V\|\omega_0) = \frac{v^2}{\varepsilon}\tanh\frac{\varepsilon}{2},\qquad
\mathcal{B} = S(\omega_V\|\omega_0) + \Delta S,
$$
checked against direct diagonalization, against the Kubo–Mori metric, and in both temperature limits. The free-field answer is this with the two-level spectrum replaced by the boost continuum.
- **Mini-Calc 4 result:** $\Delta S = g^2(\text{boost-energy shift} - \tfrac12\,\text{Kubo–Mori})$, finite and explicit — the competition deciding the sign of the generalized-entropy change under traversal.

## 6. Looking ahead

Week 13 closes Block 4 with **AAJ's open-question landscape**: beyond perturbative regimes, higher-order corrections, the bulk interpretation of each algebraic term, other deformations, and the connection to entanglement embezzlement (the group's program). Students present their final-write-up topics for group feedback and refine their plans against AAJ's frontier. Block 5 (MSY) then supplies the bulk side of the same traversal, so the algebra/bulk comparison can be made honestly.

## 7. Problem set

**Core problems.**

**1. Break the symmetry.** Take the asymmetric deformation $V = g\,(\mathcal{O}_L\mathcal{O}_R + c\,\mathcal{O}_R^2)$ with $c \ne 0$, which is *not* invariant under $J$. Show that the §1.3 argument no longer forces $\langle VK_0\rangle_0 = 0$, and hence that $\Delta S$ now has a first-order term equal to $\delta\langle K_0\rangle$. What does a linear-in-$g$ area response mean physically for the wormhole?

**2. Relative-entropy piece.** For the free-field GJW analog, compute $S(\omega_V\|\omega_0)$ to $O(g^2)$ as a Gaussian functional of $\varsigma(f_L, f_R)$, using the §2.4 metric. Identify the positive kernel $P$ in terms of $\tanh(\pi K_{\rm boost})$, and check that your answer reduces to the §2.3 model result when the boost spectrum is replaced by two levels.

**3. Modular-energy piece.** Compute $\omega_V(K_0) - \omega_0(K_0)$ to $O(g^2)$ with $K_0 = 2\pi K_{\rm boost}$. Show it is the boost energy injected by the deformation and that it is positive.

**4. Assemble $\Delta S$.** Combine Problems 2 and 3 into the leading $\Delta S$. Discuss the sign competition between the two pieces.

**Starred problems.**

**5\*. Reproduce the count.** Read AAJ §§4–5 and reconstruct their enumeration of the twenty $O(g^2)$ corrections, using the three choices set out in §3.1. State explicitly the grouping conventions they adopt — whether $\lambda$-integrals are left unevaluated, whether Hermitian-conjugate pairs are counted once or twice, whether the two clocks are identified — and say how the total would change under a different convention. Then classify each term as matter / clock / cross sector and state which the free-field analog reproduces.

**6\*. Kubo–Mori = Fisher.** Starting from the §2.4 integral formula, show that when $\delta\rho$ commutes with $\rho_0$ the $s$-integral collapses and the metric reduces to the classical Fisher information $\sum_j (\delta p_j)^2/p_j$. Then explain why the model of §2, where $\delta\rho$ is purely *off*-diagonal, is the opposite extreme, and why its answer carries the factor $\tanh(\varepsilon/2)/\varepsilon$ instead of $1/p_j$. Relate to the energy-variance/heat-capacity result of Sem I Wk 7.

**Project problems.**

**7. Mini-Calc 4 writeup.** Complete your assigned 2-page part of Mini-Calc 4. This is the technical core of your final paper; write it to publication standard.

**8\*\*. Higher order (hard, optional).** Sketch what changes at $O(g^3)$: the cocycle gets $u^{(3)}$, the log expansion a cubic term, and new orderings appear. Estimate the number of distinct corrections (AAJ stop at $g^2$; the higher-order enumeration is open — Block 5 Wk 13).

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 4. Last revised 2026-08-23.*
