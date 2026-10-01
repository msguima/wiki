---
title: "Lecture 26 — An island saddle calculated explicitly"
type: lecture-notes
edition: "2.2 — rewritten at the AQFT standard"
lecture: 26
semester: 2
week: 9
hours: 3
prerequisites: "Lectures 16, 21, 23 and 25; bosonization of a free Dirac fermion in two dimensions, which is used and stated"
status: "rewritten 2026-09-30, pending instructor review; the zero-temperature quantum extremal point and its stability, the Lorentzian character of the extremum, the Kruskal form of the two-interval free-fermion entropy with its mutual information, the late-time island and the Page time are exact calculations or controlled approximations of the stated functional; the free-fermion formula is sketched through the replica trick and bosonization with its source; the island rule is stated"
modified: 2026-09-30
---

# Lecture 26 — An island saddle calculated explicitly

> *Lecture 25 specified a black hole, a bath and the entropy to be computed, and it reduced the island rule to the extremization of an explicit functional. This lecture carries out the extremization. At zero temperature the quantum extremal point is the root of a quadratic equation, a minimum in space and a maximum in time, and it lies outside the horizon. For the two-sided black hole in equilibrium with two baths, the entropy of the radiation requires the entropy of two intervals in the Hartle–Hawking state. We derive it for free Dirac fermions from the replica trick and bosonization, following Casini, Fosco and Huerta, and transform it to the Kruskal coordinates of Lecture 25. The mutual information between the two sides decays at late times, so the late-time answer is the same for every conformal field theory. Without an island the entropy grows linearly forever; with the island it saturates at twice the Bekenstein–Hawking entropy, and the transition happens at the Page time $3\beta S_{\mathrm{BH}}/\pi c$.*

## How to use this lecture

**Classroom core, one meeting of three hours.** The history (§1, 10 minutes), the zero-temperature extremum (§2, 25 minutes), its stability and limits (§3, 15 minutes), and the time direction (§4, 15 minutes) come before a 10-minute break. After it come the free-fermion entropy of several intervals (§5, 30 minutes), its transformation to the thermal background (§6, 25 minutes), and the late-time island and the Page time (§7, 25 minutes), with 25 minutes for Checkpoints 1 and 2 and Problems 4–6; Problems 1–3 complete the core assignment. These allocations are proposals and have not been tested in class.

**Self-study.** The island outside the horizon and causality (§8), what the calculation establishes (§9), and Problems 7–12, including the mutual information of the two sides, the Page time in general units and the dilaton at the island endpoint.

**Research extension.** The finite-time extremization of the exact functional, islands in higher dimensions, and a holographic matter theory, in Problems 13–15.

**Prerequisites.** Lecture 16 for the entropy of an interval and the replica trick, Lecture 21 for generalized entropy, Lectures 16 and 19 (§8 of each) for quantum extremal surfaces, Lecture 23 for the thermofield double, Lecture 25 for the model and its functional. Bosonization of a free Dirac fermion is used and stated.

**What this lecture establishes.** The zero-temperature quantum extremal point, its stability and its Lorentzian character are exact properties of the stated functional. The Kruskal form of the two-interval entropy of the free fermion, the mutual information between the two sides, the late-time island equation and its solution for large dilaton, and the Page time are exact calculations or controlled approximations of that functional. The multi-interval formula of the free fermion is sketched through the replica trick and bosonization, with its source. The island rule itself is stated in Lecture 25 and derived in Lecture 27.

## 0. Reading

**Primary.**

- A. Almheiri, R. Mahajan, J. Maldacena, [Islands outside the horizon](https://arxiv.org/abs/1910.11077) (2019).
- A. Almheiri, T. Hartman, J. Maldacena, E. Shaghoulian, A. Tajdini, [Replica Wormholes and the Entropy of Hawking Radiation](https://arxiv.org/abs/1911.12333) (2019), §§2–5.
- H. Casini, C. D. Fosco, M. Huerta, [Entanglement and alpha entropies for a massive Dirac field in two dimensions](https://arxiv.org/abs/cond-mat/0505563) (2005).

**Secondary.**

- H. Casini, M. Huerta, [Entanglement entropy in free quantum field theory](https://arxiv.org/abs/0905.2562) (2009), for the multi-interval formula and its derivations.
- P. Calabrese, J. Cardy, [Entanglement Entropy and Quantum Field Theory](https://arxiv.org/abs/hep-th/0405152) (2004), for twist fields and the Weyl factor.
- A. Almheiri, T. Hartman, J. Maldacena, E. Shaghoulian, A. Tajdini, [The entropy of Hawking radiation](https://arxiv.org/abs/2006.06872) (2020).

**Optional research reading.**

- A. Almheiri, R. Mahajan, J. E. Santos, [Entanglement islands in higher dimensions](https://arxiv.org/abs/1911.09666) (2019), and K. Hashimoto, N. Iizuka, Y. Matsuo, [Islands in Schwarzschild black holes](https://arxiv.org/abs/2004.05863) (2020).
- H. Z. Chen, Z. Fisher, J. Hernandez, R. C. Myers, S.-M. Ruan, [Information Flow in Black Hole Evaporation](https://arxiv.org/abs/1911.03402) (2019).
- M. Headrick, [Entanglement Renyi entropies in holographic theories](https://arxiv.org/abs/1006.0047) (2010), for two intervals in a holographic conformal field theory.

## 1. Does the proposed island actually extremize the entropy?

The island rule was stated in 2019 by Almheiri, Mahajan, Maldacena and Zhao, in a model where the matter has a holographic dual of its own. Almheiri, Mahajan and Maldacena then asked what it gives for a black hole that does not evaporate. They took the eternal JT black hole of Lecture 25, joined to baths at the same temperature in the Hartle–Hawking state, and found a clean version of the paradox. In Hawking's calculation the entropy of the radiation collected in the two baths grows linearly forever, while the system that purifies it has a finite entropy. The island saves unitarity, and it has a surprising location, partly outside the horizon, which raised a question about causality that they answered with the quantum focusing conjecture. A few weeks later Almheiri, Hartman, Maldacena, Shaghoulian and Tajdini derived the rule from replica wormholes and worked the same examples at zero and finite temperature.

The calculation needs the entropy of several intervals, which in a general conformal field theory depends on the full operator content. Calabrese and Cardy proposed in 2004 a formula for every conformal field theory, the single-interval formula of Lecture 16 extended with a mutual-information term. It fails in general, and Casini, Fosco and Huerta showed in 2005 that it is exact for the massless Dirac fermion, by diagonalizing the replica twist and bosonizing to a free massless scalar. Almheiri, Hartman, Maldacena, Shaghoulian and Tajdini used it in 2019 to write the finite-time entropy of the radiation for free fermions. We use it to make the thermal calculation exact at all times, and we show that its late-time limit is universal.

## 2. The zero-temperature extremum

Lecture 25 derived the generalized entropy of the island $(-\infty,-a]$ with the radiation $[b,\infty)$,

$$
S_{\mathrm{gen}}(a)=S_0+\frac{\varphi_r}a+\frac c6\log\frac{(a+b)^2}{a\,\epsilon}.
$$

Its derivative is

$$
\frac{dS_{\mathrm{gen}}}{da}=-\frac{\varphi_r}{a^2}+\frac c6\left(\frac2{a+b}-\frac1a\right)=\frac c6\,\frac{a^2-(b+k)\,a-kb}{a^2\,(a+b)},
\qquad
k=\frac{6\varphi_r}c ,
$$

and the extremality condition is the quadratic equation

$$
a\,(a-b)=k\,(a+b),
$$

whose roots have product $-kb<0$. The admissible root is

$$
a_*=\frac{b+k+\sqrt{b^2+6bk+k^2}}2 .
$$

[Exact, for the stated functional.] Since $a_*(a_*-b)=k(a_*+b)>0$, the endpoint obeys $a_*>b$: the island reaches farther into the gravitational region than the radiation reaches into the bath. In fact the status of the result is the status of the functional, a semiclassical generalized entropy; the quadratic is solved without approximation.

## 3. Stability and limits

The denominator of the derivative is positive, and at the positive root the numerator crosses zero with slope $2a_*-(b+k)=\sqrt{b^2+6bk+k^2}>0$, so $S_{\mathrm{gen}}''(a_*)>0$. The functional tends to $+\infty$ as $a\to0$, because of the dilaton, and grows logarithmically as $a\to\infty$, so $a_*$ is the unique minimum along the slice $t=0$. For $k\gg b$ the endpoint is at $a_*=k+2b+O(b^2/k)$, and for $b\gg k$ at $a_*=b+2k+O(k^2/b)$. As a numerical checkpoint, $b=1$ and $k=6$ give $a_*=(7+\sqrt{73})/2\simeq7.7720$.

Note that the constant $S_0$ does not move the endpoint, since it is independent of $a$. But it enters the value, and the value is what the island candidate is compared with. The Poincaré horizon is at $\sigma\to-\infty$, so the quantum extremal point at $\sigma=-a_*$ lies outside it, and the island reaches from the endpoint to the horizon.

## 4. Extremize time as well as space

The extremum must be taken over spacetime positions. Let the bath endpoint be at time $t_b$ and the island endpoint at $t_a$. In the vacuum of $(t,\sigma)$ the squared distance is $(a+b)^2-(t_a-t_b)^2$, and

$$
S_{\mathrm{gen}}(a,t_a)=S_0+\frac{\varphi_r}a+\frac c6\log\frac{(a+b)^2-(t_a-t_b)^2}{a\,\epsilon} ,
$$

since the dilaton $\varphi_r/a$ is static. Differentiating,

$$
\partial_{t_a}S_{\mathrm{gen}}=-\frac c3\,\frac{t_a-t_b}{(a+b)^2-(t_a-t_b)^2},
\qquad
\partial_{t_a}^2S_{\mathrm{gen}}\Big|_{t_a=t_b}=-\frac c3\,\frac1{(a+b)^2} .
$$

The extremum is at $t_a=t_b$, a minimum in the spatial direction and a maximum in the time direction. [Exact.] Thus the quantum extremal surface is a saddle of the generalized entropy on spacetime, as the Ryu–Takayanagi surfaces of Lecture 16 are saddles of the area in Lorentzian signature. The rule is to extremize and then to minimize over the extrema; a minimization over all spacetime positions would find no minimum.

**Checkpoint 1.** Why can the extremum not be a minimum in the time direction?

**Answer.** Moving the island endpoint in time along with the bath point makes the interval between them more nearly null, and the squared distance $(a+b)^2-(t_a-t_b)^2$ decreases. The matter entropy therefore decreases away from $t_a=t_b$, and the extremum is a maximum in time.

## 5. The free fermion on several intervals

Consider a massless Dirac fermion in two dimensions, with central charge $c=1$, in its vacuum on the line, and the region $V=\bigcup_{i=1}^N(a_i,b_i)$. The replica moment $\operatorname{Tr}\rho_V^n$ is the partition function of $n$ copies $\psi_1,\dots,\psi_n$ glued cyclically across $V$: crossing $V$ maps $\psi_j$ to $\psi_{j+1}$, with a sign in the last copy fixed by the fermionic trace. The gluing matrix is diagonalized by a discrete Fourier transform in the copy index, with eigenvalues $e^{2\pi iq/n}$ for $q=-\frac{n-1}2,\dots,\frac{n-1}2$. The moment therefore factorizes,

$$
\operatorname{Tr}\rho_V^n=\prod_qZ_q ,
$$

where $Z_q$ is the partition function of a single Dirac fermion that acquires the phase $e^{2\pi iq/n}$ around each $a_i$ and the inverse phase around each $b_i$. [Exact.] Such a phase is created by a vortex of the $U(1)$ symmetry of the fermion, and by bosonization the vortex of flux $2\pi q/n$ is a vertex operator $e^{i(q/n)\phi}$ of the boson $\phi$ dual to the fermion, distinct from the dilaton $\varphi$, of scaling dimension $(q/n)^2$. With the vertex correlator $\bigl\langle\prod_je^{i\alpha_j\phi(x_j)}\bigr\rangle=\prod_{i<j}|x_i-x_j|^{2\alpha_i\alpha_j}$, charge $+q/n$ at each $a_i$ and $-q/n$ at each $b_i$, and a short-distance cutoff $\epsilon$,

$$
\log Z_q=-2\left(\frac qn\right)^2X,
\qquad
X=\sum_{i,j}\log|b_i-a_j|-\sum_{i<j}\log|a_i-a_j|-\sum_{i<j}\log|b_i-b_j|-N\log\epsilon .
$$

The sum over sectors uses $\sum_qq^2=n(n^2-1)/12$, so

$$
\log\operatorname{Tr}\rho_V^n=-\frac{n^2-1}{6n}\,X,
\qquad
S(V)=-\partial_n\log\operatorname{Tr}\rho_V^n\Big|_{n=1}=\frac X3 .
$$

[Sketched — refs: Casini–Fosco–Huerta 2005; Casini–Huerta 2009. The identification of the twisted sectors with vertex operators is the step taken from bosonization.] For $N=1$ this is $\frac13\log(\ell/\epsilon)$, the formula of Lecture 16 with $c=1$; for $c$ Dirac fermions the result is multiplied by $c$. For two intervals $A=(a_1,b_1)$ and $B=(a_2,b_2)$ the formula reads $S(A\cup B)=S(A)+S(B)-\mathcal I(A{:}B)$, with

$$
\mathcal I(A{:}B)=\frac c3\log\frac{|a_1-a_2|\,|b_1-b_2|}{|b_1-a_2|\,|b_2-a_1|},
$$

positive for disjoint intervals and vanishing as they separate. In a general conformal field theory the mutual information of two intervals is a different function of their cross-ratio, which depends on the operator content; the single-interval entropies are universal. The derivation extends to the Lorentzian plane, with $|x-y|^2$ replaced by the invariant squared distance $-\Delta w^+\Delta w^-$ for spacelike separations. It extends to a conformally flat metric $e^{2\omega}(-dw^+dw^-)$ by the Weyl factor of Lecture 25: each endpoint contributes $\frac c6\,\omega$ at that endpoint.

## 6. The thermal entropy in Kruskal coordinates

Return to the two-sided black hole of Lecture 25, §7, with $\beta=2\pi$, the two baths in the Hartle–Hawking state, and both evolved forward to time $t$. The radiation is $R=R_L\cup R_R$, the half-lines $\sigma\geq b$ of the two baths at time $t$. The island candidate is the region $I$ between the points $Q_L$ and $Q_R$ at $\sigma=-a$ in the two exteriors, at time $t_a$, joined through the interior. In the pure global state $S(I\cup R)$ equals the entropy of the complement, the two intervals $[P_L,Q_L]$ and $[Q_R,P_R]$ from each bath point to the island endpoint on the same side. In the Kruskal coordinates $(w^+,w^-)$,

$$
P_R=\bigl(e^{b+t},-e^{b-t}\bigr),\quad
Q_R=\bigl(e^{-a+t_a},-e^{-a-t_a}\bigr),\quad
P_L=\bigl(-e^{b-t},e^{b+t}\bigr),\quad
Q_L=\bigl(-e^{-a-t_a},e^{-a+t_a}\bigr).
$$

The squared distances follow from $-\Delta w^+\Delta w^-$. The two intervals have

$$
d^2(P_L,Q_L)=d^2(Q_R,P_R)=2\,e^{b-a}\bigl[\cosh(a+b)-\cosh(t_a-t)\bigr],
$$

and the pairs across the two sides have

$$
d^2(P_L,P_R)=4e^{2b}\cosh^2t,\qquad
d^2(Q_L,Q_R)=4e^{-2a}\cosh^2t_a,\qquad
d^2(P_L,Q_R)=d^2(Q_L,P_R)=4e^{b-a}\cosh\tfrac{a+b-t_a-t}2\cosh\tfrac{a+b+t_a+t}2 .
$$

The Weyl factor of the metric $e^{2\omega}(-dw^+dw^-)$ is $e^{\omega}=e^{-b}$ at the bath points and $e^{\omega}=e^a/\sinh a$ at the island points. Inserting them in the formula of §5 gives

$$
S_{\mathrm{matter}}(a,t_a;t)=\frac c3\log\left[\frac{2\cosh t_a\cosh t\,\bigl|\cosh(a+b)-\cosh(t_a-t)\bigr|}{\sinh a\,\cosh\frac{a+b-t_a-t}2\,\cosh\frac{a+b+t_a+t}2}\right]+C_R ,
$$

where $C_R=-\frac c3\log\epsilon$ collects the cutoffs of the two bath points, and the cutoffs at the island points are absorbed into $2S_0$. [Exact calculation for $c$ free Dirac fermions, checked numerically against the direct evaluation of the formula of §5.] The same formula appears in §5 of the replica-wormhole paper of Almheiri, Hartman, Maldacena, Shaghoulian and Tajdini. The mutual information between the two intervals is

$$
\mathcal I(L{:}R)=\frac c3\log\frac{\cosh\frac{a+b-t_a-t}2\,\cosh\frac{a+b+t_a+t}2}{\cosh t_a\,\cosh t},
$$

in which the Weyl factors cancel. At $t=t_a=0$ it is $\frac{2c}3\log\cosh\frac{a+b}2$, and for $t_a+t\gg a+b$ it decays exponentially. The generalized entropy of the island candidate is

$$
S_{\mathrm{island}}(a,t_a;t)=2S_0+2\varphi_r\coth a+S_{\mathrm{matter}}(a,t_a;t),
$$

with the static dilaton of Lecture 25 at both endpoints. The no-island candidate is the entropy of the single interval from $P_L$ to $P_R$, derived in Lecture 25, §7,

$$
S_{\mathrm{no\ island}}(t)=\frac c3\log\bigl(2\cosh t\bigr)+C_R .
$$

Note that the two candidates share the constant $C_R$, which cancels when they are compared.

## 7. The late-time island and the Page time

At late times, $t_a+t\gg a+b$, the mutual information vanishes, and the matter entropy becomes the sum of two single-interval entropies,

$$
S_{\mathrm{matter}}\simeq\frac c3\log\frac{2\bigl[\cosh(a+b)-\cosh(t_a-t)\bigr]}{\sinh a}+C_R ,
$$

which is the same for every conformal field theory of central charge $c$, since single-interval entropies are universal. The time equation now gives $t_a=t$, a maximum in time as in §4, and at $t_a=t$ the bracket is $4\sinh^2\frac{a+b}2$. The spatial equation is $-2\varphi_r/\sinh^2a+\frac c3\bigl(\coth\frac{a+b}2-\coth a\bigr)=0$, which with $\coth x-\coth y=\sinh(y-x)/\sinh x\sinh y$ becomes

$$
\sinh a=\frac{6\varphi_r}c\,\frac{\sinh\frac{a+b}2}{\sinh\frac{a-b}2} .
$$

[Exact, in the late-time regime.] For $\varphi_r\gg c$ the solution is large, and

$$
a_*\simeq b+\log\frac{12\varphi_r}c .
$$

[Controlled perturbative, in $c/\varphi_r$.] The endpoint lies outside the horizon, which is at $\sigma\to-\infty$, and its dilaton exceeds the horizon value by $2\varphi_re^{-2a_*}\simeq c^2e^{-2b}/72\varphi_r$ (Problem 12). At the extremum,

$$
S_{\mathrm{island}}\simeq2S_0+2\varphi_r\coth a_*+\frac c3\log\frac{4\sinh^2\frac{a_*+b}2}{\sinh a_*}+C_R ,
$$

which is independent of time. For large $a_*$, $4\sinh^2\frac{a_*+b}2\simeq e^{a_*+b}$ and $\sinh a_*\simeq\frac12e^{a_*}$, so the matter term is $\frac c3(b+\log2)$, and the dilaton term is $2\varphi_r+c^2e^{-2b}/36\varphi_r$. The island entropy is therefore $2(S_0+\varphi_r)=2S_{\mathrm{BH}}$, twice the Bekenstein–Hawking entropy of one side, plus $\frac c3(b+\log2)+c^2e^{-2b}/36\varphi_r+C_R$: the logarithm of $\varphi_r/c$ in the endpoint cancels from the value.

The fine-grained entropy of the radiation is the smaller of the two candidates. The no-island entropy grows as $\frac c3t$ at late times and reaches the island value at the Page time,

$$
t_{\mathrm{Page}}\simeq\frac{6S_{\mathrm{BH}}}c+b+\log2,
\qquad\text{or}\qquad
t_{\mathrm{Page}}\simeq\frac{3\beta\,S_{\mathrm{BH}}}{\pi c}+b+\frac\beta{2\pi}\log2
$$

with $\beta$ restored, since the rate is then $2\pi c/3\beta$. [Controlled perturbative, in $c/S_{\mathrm{BH}}$ and $c/\varphi_r$.] The crossing lies in the late-time regime whenever $S_{\mathrm{BH}}/c$ is large compared with $a_*+b$, and then the whole calculation is consistent. The entropy rises and then stays at the island value, near $2S_{\mathrm{BH}}$, because the black hole is in equilibrium and keeps exchanging radiation with the baths. The figure shows the two candidates and their minimum, and the positions of the radiation and the island at a late time.

![[ads-cft-island-page-curve.svg|Left: a schematic of the compactified Kruskal diagram of the two-sided black hole with its two baths, drawn at a moderate time for legibility, since at the Page time the endpoints crowd toward the upper corners, with the radiation regions as thick curves running from the bath points to spatial infinity in both baths, and the island as a thick segment through the interior between two endpoints just outside the horizons. Right: the entropy of the radiation divided by c as a function of bath time, with the linear growth of the no-island candidate, the island candidate drawn where the late-time approximation holds, and their minimum, which follows the growth until the Page time and then stays at the island value.]]

**Checkpoint 2.** The late-time island entropy was computed with free fermions. Why does it hold for every conformal field theory of central charge $c$, while the entropy at finite times does not?

**Answer.** At late times the mutual information between the two sides vanishes, and the matter entropy is the sum of two single-interval entropies, which depend only on $c$. At finite times the mutual information contributes, and it is a function of the cross-ratio that depends on the operator content of the theory.

## 8. Self-study: an island outside the horizon

A part of the island lies in the exterior of the black hole, where the black-hole system at the AdS$_2$ boundary can send signals. Since the island belongs to the entanglement wedge of the radiation, this suggests possible causality paradoxes, and Almheiri, Mahajan and Maldacena showed that they are avoided because of the quantum focusing conjecture. [Stated only — refs: Almheiri–Mahajan–Maldacena 2019.] The general property behind such arguments was observed by Engelhardt and Wall: a quantum extremal surface lies outside the causal domain of influence of the region and of its complement. [Stated only — refs: Engelhardt–Wall 2014.] Quantitatively, the endpoint is close to the horizon in the sense of the dilaton, by an amount of order $c^2/\varphi_r$. In Kruskal coordinates it sits at $w^-=-e^{-a_*-t}$, just outside the future horizon $w^-=0$, while its Schwarzschild coordinate is at the finite distance $a_*\simeq b+\log(12\varphi_r/c)$ from the boundary.

## 9. Self-study: what the calculation establishes

We have an explicit quantum extremal point at zero temperature. For the equilibrium black hole we have a competing island saddle whose late-time value is universal, and whose crossing with the no-island saddle falls in the regime where the approximations hold. The calculation uses the island rule and the semiclassical matter state. It reproduces the bound $S(R)\leq2S_{\mathrm{BH}}$ that unitarity demands of a finite system, in the same way the Page curve of Lecture 24 respects the dimension bound. It does not construct a decoder for the radiation, and it does not follow a black hole whose mass decreases; for that one needs the evaporating model of Lecture 25, §8.

Before the Page time the island candidate is larger, and the no-island saddle dominates. But at early times the exact functional of §6 must be extremized at finite times, where the island extremum may move off the real section or may not exist. The plateau value of §7 should not be extrapolated to early times to draw a smooth curve. Problem 13 carries out the finite-time extremization.

## 10. What to take away

- **Exact, for the stated functional:** at zero temperature the quantum extremal point is $a_*=\frac12\bigl(b+k+\sqrt{b^2+6bk+k^2}\bigr)$ with $k=6\varphi_r/c$, a minimum in space and a maximum in time, outside the horizon.
- **Sketched, with the source:** for $c$ free Dirac fermions, $S(\bigcup_i(a_i,b_i))=\frac c3\bigl[\sum_{i,j}\log|b_i-a_j|-\sum_{i<j}\log|a_i-a_j|-\sum_{i<j}\log|b_i-b_j|-N\log\epsilon\bigr]$, from the replica trick and bosonization.
- **Exact calculation:** in the two-sided equilibrium the island's matter entropy is the formula of §6, and the mutual information between the two sides decays at late times, so the late-time answer is universal.
- **Controlled perturbative:** the late-time island has $a_*\simeq b+\log(12\varphi_r/c)$ and entropy $2S_{\mathrm{BH}}+\frac c3(b+\log2)$ up to terms of order $c^2/\varphi_r$, and it takes over from the linearly growing no-island entropy at $t_{\mathrm{Page}}\simeq3\beta S_{\mathrm{BH}}/\pi c$ at leading order.

## 11. Looking ahead

Lecture 27 derives the rule used here. The replica trick for the radiation, applied to the gravitational path integral, admits geometries in which the replicas are connected through the gravitational region. Their fixed points are the endpoints of the island, and the conical defects there produce the dilaton terms of the generalized entropy. That is, the extremization of §§2–4 is the equation of motion of those defects as the number of replicas tends to one.

## 12. Problem set

### Classroom core

1. **The zero-temperature equation.** Derive the quadratic equation for the endpoint and discard the negative root.

2. **Stability.** Show that the positive root is a spatial minimum, and compute $a_*$ for $b=1$, $k=6$.

3. **Time extremality.** Compute $\partial_{t_a}^2S_{\mathrm{gen}}$ at $t_a=t_b$ in the zero-temperature model, and interpret its sign.

4. **The replica sum.** Show that $\sum_{q=-(n-1)/2}^{(n-1)/2}q^2=n(n^2-1)/12$, and derive $S=X/3$ from $\log\operatorname{Tr}\rho^n=-\frac{n^2-1}{6n}X$.

5. **Kruskal distances.** Compute the six squared distances of §6 and the Weyl factors, and derive $S_{\mathrm{matter}}(a,t_a;t)$.

6. **The late-time island.** Derive the equation $\sinh a=\frac{6\varphi_r}c\sinh\frac{a+b}2/\sinh\frac{a-b}2$ and its solution for $\varphi_r\gg c$.

### Self-study consolidation

7. **A constant that matters.** Why can $S_0$ change which candidate dominates without changing the endpoint?

8. **Mutual information of the two sides.** Derive $\mathcal I(L{:}R)$ from the formula of §5, and find its values at $t=t_a=0$ and at late times.

9. **The crossing regime.** What must hold for the Page time to lie in the late-time regime, and for no omitted saddle to win?

10. **Restoring the temperature.** Redo the late-time analysis with general $\beta$, and show that $t_{\mathrm{Page}}\simeq3\beta S_{\mathrm{BH}}/\pi c$.

11. **Two intervals on the line.** For $A=(0,1)$ and $B=(x,x+1)$, compute the free-fermion mutual information and its limits as $x\to1$ and $x\to\infty$.

12. **The dilaton at the endpoint.** Show that $\varphi(-a_*)-\varphi_h\simeq2\varphi_re^{-2a_*}\simeq c^2e^{-2b}/72\varphi_r$, and compare the distance of the endpoint from the horizon in the dilaton and in $\sigma$.

### Research extension

13. **Finite-time extremization.** Extremize $S_{\mathrm{island}}(a,t_a;t)$ numerically at finite $t$, checking both derivatives and the saddle character. *Known:* at late times the extremum approaches the solution of §7; at early times it can leave the real section. *Completion:* the island branch as a function of $t$ for $\varphi_r/c=10$, $b=1$, with the time from which a real extremum exists.

14. **Islands in higher dimensions.** Set up the generalized entropy of the radiation for a four-dimensional Schwarzschild black hole with an s-wave matter sector, and find the late-time island. *Known:* Almheiri, Mahajan and Santos find islands for eternal black holes coupled to baths in higher dimensions, and Hashimoto, Iizuka and Matsuo find a late-time island outside the horizon of an asymptotically flat Schwarzschild black hole, with a Page time of order $S_{\mathrm{BH}}/c$ in units of the inverse temperature. *Completion:* the endpoint location at leading order in $G_N$ and the Page time, compared with the two-dimensional result.

15. **A holographic matter theory.** Replace the free fermion by a holographic conformal field theory, for which the mutual information of two intervals follows from the minimal geodesics of Lecture 19. *Known:* the single-interval entropies are universal, and Headrick describes the two-interval entropies and Rényi entropies of holographic theories. *Completion:* the finite-time island entropy for the holographic theory, compared with the fermion, and the time from which the two agree.

## 13. Answer checkpoints

1. Multiplying the derivative by $6a^2(a+b)/c$ gives $a^2-(b+k)a-kb=0$. The roots have product $-kb<0$, so exactly one is positive.

2. The numerator crosses zero with slope $\sqrt{b^2+6bk+k^2}>0$ and the denominator is positive. For $b=1$, $k=6$, $a_*=(7+\sqrt{73})/2\simeq7.7720$.

3. $-\frac c3(a+b)^{-2}$. Moving the endpoint in time shortens the proper distance to the bath point, so the extremum is a maximum in time.

4. For odd $n$ the sum is $2\sum_{q=1}^{(n-1)/2}q^2$, and the same polynomial results for even $n$ with half-integer $q$. Then $\partial_n\frac{n^2-1}{6n}=\frac{n^2+1}{6n^2}$, which is $\frac13$ at $n=1$.

5. For example $-\Delta w^+\Delta w^-$ for $P_L,Q_L$ is $(e^{b-t}-e^{-a-t_a})(e^{b+t}-e^{-a+t_a})=2e^{b-a}[\cosh(a+b)-\cosh(t_a-t)]$. With $\frac12\log d^2$ added for the two same-side pairs and for $(P_L,P_R)$ and $(Q_L,Q_R)$, and subtracted for $(P_L,Q_R)$ and $(Q_L,P_R)$, the Weyl terms $\frac12\sum\omega=a-b-\log\sinh a$, and $e^{\omega}$ as stated, the result follows.

6. At $t_a=t$ the matter term is $\frac c3\log\frac{4\sinh^2\frac{a+b}2}{\sinh a}$; differentiating and using the identity for $\coth x-\coth y$ gives the equation. For large $a$, $\sinh a\simeq\frac12e^a$ and the ratio of sines tends to $e^b$.

7. $S_0$ drops out of the derivatives and remains in the value, which is compared between candidates.

8. $\mathcal I=\frac c3\cdot\frac12\log\frac{d^2(P_L,Q_R)\,d^2(Q_L,P_R)}{d^2(Q_L,Q_R)\,d^2(P_L,P_R)}$. At $t=t_a=0$ it is $\frac{2c}3\log\cosh\frac{a+b}2$, and for $t_a=t\gg a+b$ it is of order $e^{-2t+a+b}$.

9. $t_{\mathrm{Page}}$ must exceed $a_*+b$ by a large factor, the large-dilaton approximation must hold, and no other saddle with a smaller generalized entropy may exist, which the replica analysis of Lecture 27 addresses.

10. With the metric $(2\pi/\beta)^2(-dt^2+d\sigma^2)/\sinh^2(2\pi\sigma/\beta)$, all formulas hold with $t\to2\pi t/\beta$, $\sigma\to2\pi\sigma/\beta$, and $\varphi_r\to2\pi\varphi_r/\beta$ in the dilaton. The growth rate becomes $2\pi c/3\beta$, and equating $\frac{2\pi c}{3\beta}t$ with $2S_{\mathrm{BH}}$ gives the result.

11. $\mathcal I=\frac c3\log\frac{x\cdot x}{(x-1)(x+1)}=\frac c3\log\frac{x^2}{x^2-1}$, which diverges as $x\to1$, when the intervals touch, and decays as $\frac c3x^{-2}$ at large separation.

12. $\coth a-1\simeq2e^{-2a}$ for large $a$, and $e^{-2a_*}\simeq c^2e^{-2b}/144\varphi_r^2$. The dilaton offset vanishes as $\varphi_r/c\to\infty$, while the coordinate distance $\sigma$ from the boundary, $a_*$, grows as $\log(\varphi_r/c)$; the horizon is at infinite $\sigma$, so the endpoint is outside it.

**Wiki connections.** [[quantum-extremal-surfaces|quantum extremal surfaces]] · [[page-curve|Page curve]] · [[jt-gravity|JT gravity]]
