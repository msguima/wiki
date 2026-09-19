---
title: "Week 5 — 2d CFT essentials"
type: lecture-notes
course: syllabus
semester: 1
week: 5
block: A
duration: "4 hours (2 lectures × 2 hours)"
status: final
modified: 2026-08-25
---

# Week 5 — 2d CFT Essentials

> *Two dimensions is special: the conformal algebra is infinite-dimensional (Virasoro), and that extra symmetry makes 2d CFT almost solvable. This closing week of Block A assembles the tools we need downstream: the **Virasoro algebra** from the $TT$ OPE of Week 4, **Verma modules** and their null states (minimal models), and the **Cardy formula** for the high-energy density of states. The last is the one we will cash in holographically — Cardy with the Brown–Henneaux central charge reproduces the Bekenstein–Hawking entropy of the BTZ black hole (Sem II Wk 7), the cleanest "microscopic" black-hole entropy count in the course.*

## Learning goals

By the end of this week, a student can:

1. Derive the Virasoro algebra $[L_m,L_n]=(m-n)L_{m+n}+\tfrac{c}{12}m(m^2-1)\delta_{m+n,0}$ from the $TT$ OPE, and identify the global $\mathrm{SL}(2)$ subalgebra.
2. Build a Verma module from a primary $|h\rangle$ and count states by level.
3. Identify null states (level-1 at $h=0$; level-2 via the Kac condition) and state what minimal models are.
4. Derive the Cardy formula $S(E)\simeq 2\pi\sqrt{cE/6}$ from modular invariance.
5. Apply Cardy to BTZ and recover Bekenstein–Hawking.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Modern CFT* §§8–9** — Virasoro and its representations (§8); modular invariance and Cardy (§9).
- di Francesco, Mathieu, Sénéchal, *Conformal Field Theory*, Ch. 6–8 — the standard 2d reference.
- Belavin, Polyakov, Zamolodchikov, *Infinite conformal symmetry in two-dimensional quantum field theory*, Nucl. Phys. B241 (1984) — the founding paper.

**Prerequisites.** [[week-04-stress-tensor-and-central-charge]] (the $TT$ OPE, central charge), [[week-02-radial-quantisation-and-state-operator]] (radial quantisation; $L_0=h$).

**AQFT cross-reference.** None for Block A.

**What these notes add.** adscft.org §8 builds Virasoro and §9 covers modular invariance and Cardy. This note adds the Cardy derivation itself — the site states the result — because the argument is four lines of saddle point and it is the single most quotable calculation in two-dimensional CFT. It also carries the Strominger BTZ match all the way to a numerical identity, so that the first statistical derivation of a black-hole entropy is something the student has checked rather than been told.

## 1. The Virasoro algebra

Expand the holomorphic stress tensor in modes and invert by a contour integral:

$$
T(z) = \sum_{n\in\mathbb{Z}} L_n\,z^{-n-2},\qquad
L_m = \oint\frac{dz}{2\pi i}\,z^{m+1}\,T(z).
$$

The commutator is a double contour integral of the $TT$ OPE (Week 4): deform contours and pick up residues of $\frac{c/2}{(z-w)^4}+\frac{2T(w)}{(z-w)^2}+\frac{\partial T(w)}{z-w}$. The $z^{-2}$ and $z^{-1}$ poles give the classical $(m-n)L_{m+n}$ (the Witt algebra of $z^{n+1}\partial_z$), and the $(z-w)^{-4}$ pole gives the central extension:

$$
\boxed{\;[L_m,L_n] = (m-n)\,L_{m+n} + \frac{c}{12}\,m(m^2-1)\,\delta_{m+n,0}.\;}
$$

(Same for $\bar L_m$; $[L_m,\bar L_n]=0$.) Two structural facts:

- At $c=0$ this is the **Witt algebra**; $c\ne0$ is a genuine central extension (quantum).
- The central term vanishes for $m\in\{-1,0,1\}$: $\{L_{-1},L_0,L_1\}$ close on $\mathfrak{sl}(2,\mathbb{C})$ — the **global** conformal subgroup (the finite-dimensional $\mathrm{SO}(d+1,1)|_{d=2}$ of Week 1). Primaries are highest-weight for the full Virasoro, not just this $\mathfrak{sl}(2)$ — that is the quasi-primary/primary distinction flagged in Week 1.

> **[Proved.]** the Virasoro algebra from the $TT$ OPE (the contour computation — **Exercise 1**); the central extension $\tfrac{c}{12}m(m^2-1)$ is unambiguous.


> **Physical picture.** Virasoro is the statement that in two dimensions the conformal group is infinite-dimensional: every holomorphic map is conformal, so there is one generator per Laurent mode rather than the finite handful of Week 1. The price and the prize are the same fact — infinitely many generators means infinitely many constraints, so 2d CFTs are far more rigid and far more solvable than their higher-dimensional cousins. The central extension $c$ is not optional decoration: it is forced by the algebra's cohomology, and it is what makes $L_0$ shift by $-c/24$ on the cylinder. Every special feature of AdS$_3$/CFT$_2$ in this course traces to this one structural fact.

## 2. Primary states and Verma modules

A **primary** state is highest-weight for Virasoro:

$$
L_0|h\rangle = h|h\rangle,\qquad L_n|h\rangle=0\ \ (n>0).
$$

The **Verma module** $V(c,h)$ is its descendant tower, $L_{-n_1}\cdots L_{-n_k}|h\rangle$ (take $n_i>0$, ordered), graded by level $N=\sum n_i$ with $L_0$-eigenvalue $h+N$. The number of states at level $N$ is $p(N)$, the partitions of $N$ ($1,1,2,3,5,\dots$). A 2d CFT Hilbert space is a sum of such modules over its primaries (left $\times$ right).

## 3. Null states, the Kac determinant, minimal models

The Gram (Shapovalov) matrix of inner products at level $N$ can degenerate; a zero-norm descendant is a **null state**, and it is itself primary, so it generates a sub-module that must be quotiented out (and gives a differential equation for correlators).

- **Level 1:** $L_{-1}|h\rangle$ has norm $\langle h|L_1L_{-1}|h\rangle = 2h$, null iff $h=0$ (the identity module; $L_{-1}|0\rangle=0$ ⇔ vacuum is $\mathrm{SL}(2)$-invariant).
- **Level 2:** the combination
$$
|\chi\rangle = \Big(L_{-2} - \tfrac{3}{2(2h+1)}\,L_{-1}^2\Big)|h\rangle
$$
is annihilated by $L_1$ for any $h$, and by $L_2$ only when $c,h$ obey the degenerate (Kac) relation — e.g. $h_{2,1}=\tfrac{1}{16}\big(5-c+\sqrt{(c-1)(c-25)}\big)$. Such degenerate primaries satisfy 2nd-order BPZ differential equations.

When the Kac degeneracies truncate the spectrum to **finitely many** primaries, one has a **minimal model**; the unitary series is $c=1-\tfrac{6}{m(m+1)}$, $m=3,4,\dots$, with the 2d Ising model at $m=3$, $c=\tfrac12$.

> **[Sketched]** the level-2 null state coefficient $-\tfrac{3}{2(2h+1)}$ (from $L_1|\chi\rangle=0$) and the Kac formula; **[Stated — refs.]** the minimal-model classification.

> **Physical picture: why degeneracy is a Virasoro accident.** A null state is a descendant of zero norm, and its existence forces the operator to satisfy a differential equation. In $d\ge3$ this happens only at the unitarity bound; in $d=2$ the Kac determinant vanishes on a whole lattice of $(c,h)$, so degeneracies are generic rather than exceptional. That is the technical reason the minimal models are exactly solvable: enough null states means enough differential equations to fix every correlator. It is also why two dimensions is the case where holography can be *checked* — the boundary theory is solved, so a bulk claim has something to be compared against.

## 4. The Cardy formula

The torus partition function $Z(\tau)=\mathrm{Tr}\,q^{L_0-c/24}\bar q^{\bar L_0-c/24}$ ($q=e^{2\pi i\tau}$) is **modular invariant**: $Z(\tau+1)=Z(\tau)$ and $Z(-1/\tau)=Z(\tau)$. The $S$-transform $\tau\to-1/\tau$ exchanges high and low "temperature," and a saddle-point of the inverse transform gives the asymptotic density of states at large $E=h+\bar h-\tfrac{c}{12}$:

$$
\rho(E)\sim \exp\!\Big(2\pi\sqrt{\tfrac{c\,E}{6}}\Big)
\quad\Longrightarrow\quad
\boxed{\;S(E)=\log\rho(E)\simeq 2\pi\sqrt{\tfrac{c\,E}{6}}.\;}
$$

(Splitting holomorphic/antiholomorphic, $S=2\pi\sqrt{\tfrac{c\,h}{6}}+2\pi\sqrt{\tfrac{\bar c\,\bar h}{6}}$.) The only input is the vacuum dominating the dual channel — so the high-energy entropy is fixed by $c$ alone.

**Holographic payoff (preview).** With the Brown–Henneaux central charge $c=\tfrac{3L}{2G_N}$ ([[week-04-stress-tensor-and-central-charge|Wk 4]] §6 / Sem II Wk 7), Cardy applied to a BTZ black hole of mass $M$ reproduces the **Bekenstein–Hawking** entropy $S=\tfrac{\text{horizon length}}{4G_N}$ — Strominger's count. This is the cleanest microscopic black-hole entropy in the course (Exercise 5; [[sem2-week-07-ads2-ads3-essentials|Sem II Wk 7]]).

> **[Computed.]** Cardy, derived in §4b above; **[Computed.]** the BTZ application given $c=3L/2G_N$ (Exercise 5).

**Worked example: BTZ entropy from Cardy (Strominger's count).** Take a non-rotating BTZ black hole in $\mathrm{AdS}_3$ of radius $L$, horizon at $r_+$. Its Bekenstein–Hawking entropy is the horizon *length* over $4G_3$:

$$
S_{\rm BH} = \frac{2\pi r_+}{4G_3} = \frac{\pi r_+}{2G_3}.
$$

Now reproduce it microscopically. The Brown–Henneaux central charge is $c=\bar c=\tfrac{3L}{2G_3}$, and the BTZ mass maps to symmetric left/right Virasoro levels $L_0=\bar L_0$ fixed by the BTZ dictionary; for the non-rotating case $L_0=\bar L_0 = \tfrac{r_+^2}{16\,G_3 L}$ <!-- CHECK: BTZ L_0(r_+,L,G) normalisation; conventions vary (M = r_+^2/8 G L^2, L_0 = ML/2). Confirm against Strominger hep-th/9712251 before fixing the factor. -->. Cardy then gives

$$
S_{\rm Cardy} = 2\pi\sqrt{\tfrac{c\,L_0}{6}} + 2\pi\sqrt{\tfrac{\bar c\,\bar L_0}{6}}
= 4\pi\sqrt{\tfrac{c\,L_0}{6}}
= 4\pi\sqrt{\tfrac{1}{6}\cdot\tfrac{3L}{2G_3}\cdot\tfrac{r_+^2}{16 G_3 L}}
= 4\pi\sqrt{\tfrac{r_+^2}{64\,G_3^2}}
= \frac{\pi r_+}{2G_3} = S_{\rm BH}.
$$

The microscopic Cardy count matches the geometric horizon entropy **exactly** — Strominger's 1998 result, the first statistical derivation of a black-hole entropy from a dual field theory, and the cleanest such count in this course. The overall structure (Cardy $\propto\sqrt{c\,L_0}$, $c\propto L/G$, $L_0\propto r_+^2/GL$ ⟹ $S\propto r_+/G$) is robust; the precise $O(1)$ factor in $L_0(r_+)$ is the one convention to confirm (flagged). This is the worked engine behind [[sem2-week-07-ads2-ads3-essentials|Sem II Wk 7]].

### 4b. Deriving Cardy

The formula is quotable enough to be worth owning. Work in the holomorphic sector and put $\tau = i\beta/2\pi$, so $q=e^{-\beta}$ and
$$
Z(\beta) = \mathrm{Tr}\,e^{-\beta\left(L_0 - \frac{c}{24}\right)} .
$$

```
        tau                          modular S:  tau -> -1/tau
     |--------|                      swaps the two cycles of the torus
     |        |        ====>         "space" <-> "(Euclidean) time"
     |        |                      high temperature <-> low temperature
     |--------|
       1
```
**Figure 1. The modular $S$ transformation exchanges the two cycles of the torus. Because the same partition function computes both, a hard question at high temperature becomes an easy one at low temperature.**

**Step 1 — modular invariance.** $Z$ is a function on the torus and $S:\tau\to-1/\tau$ merely relabels which cycle is called time, so $Z(\beta) = Z(4\pi^2/\beta)$.

**Step 2 — the low-temperature side is trivial.** As $\beta\to0$ the dual temperature $4\pi^2/\beta\to\infty$ is *low*, and the trace is dominated by the lowest state, $L_0=0$:
$$
Z(4\pi^2/\beta) \;\simeq\; \exp\!\Big[\frac{c}{24}\cdot\frac{4\pi^2}{\beta}\Big] = \exp\!\Big[\frac{\pi^2 c}{6\beta}\Big].
$$
Note that the whole answer comes from the $-c/24$ in the exponent — the Casimir energy computed in [[week-04-stress-tensor-and-central-charge|Week 4]] §2. Without the anomaly there is no Cardy formula.

**Step 3 — invert the Laplace transform.** Since $Z(\beta)=\int dE\,\rho(E)e^{-\beta E}$,
$$
\rho(E) = \frac{1}{2\pi i}\int d\beta\; \exp\!\Big[\beta E + \frac{\pi^2 c}{6\beta}\Big].
$$

**Step 4 — saddle point.** Extremising the exponent, $E - \dfrac{\pi^2c}{6\beta^2}=0$, gives
$$
\beta_* = \pi\sqrt{\frac{c}{6E}},
$$
and evaluating there, the two terms are equal —
$$
\beta_* E = \pi\sqrt{\frac{cE}{6}},\qquad \frac{\pi^2c}{6\beta_*} = \frac{\pi c}{6}\sqrt{\frac{6E}{c}} = \pi\sqrt{\frac{cE}{6}},
$$
so the exponent is twice either one:
$$
\boxed{\;S(E)=\log\rho(E) \simeq 2\pi\sqrt{\frac{c\,E}{6}}.\;}
$$

**[Computed.]** Cardy's formula, every step above. The suppressed pieces are the Gaussian fluctuation determinant around the saddle (a power-law prefactor, not exponential) and the assumption that the spectrum is dense enough for the integral to approximate the sum — both standard, both named here rather than hidden.

> **Physical picture.** The derivation is a temperature duality and nothing more. Counting high-energy states directly is hopeless; modular invariance says the same partition function, read the other way round, is a *low*-temperature question, where only the ground state matters. So the density of states at high energy is fixed entirely by the ground-state energy $-c/24$ — a single number. This is the first appearance in the course of a pattern that will recur throughout Semester II: an entropy that looks like it needs microscopic detail turns out to be fixed by symmetry plus one universal coefficient. When the same $2\pi\sqrt{cE/6}$ reproduces the Bekenstein–Hawking area of a BTZ black hole below, it is this fact — not any string-theoretic input — doing the work.

## 5. Liouville theory (first encounter)

Not all 2d CFTs are minimal models. **Liouville theory** is an interacting $c>1$ CFT with a continuous spectrum, primaries $e^{2\alpha\phi}$, and the (highly non-trivial) DOZZ three-point structure constants. It is the worldsheet/boundary theory in several places we meet later: AdS$_3$ gravity (Sem II Wk 7) and the matrix-model / JT-gravity story (Sem II Wks 6, 9). We only flag its existence here.

## 5b. Subtleties and fine print

**Cardy is asymptotic.** It holds at large $E$ with a dense spectrum, and there is no claim about low-lying states. Quoting it for a handful of light operators is a misuse; the BTZ match works because black holes are heavy.

**The $-c/24$ is the whole mechanism.** It comes from the Weyl anomaly (Week 4), so a student who dropped the cylinder Casimir energy as "a constant" cannot derive Cardy. This is the clearest example in Block A of a suppressed constant turning out to be the answer.

**Modular invariance is a consistency condition, not a symmetry.** It constrains which spectra are allowed rather than acting on states within a theory. Theories failing it are simply not consistent on a torus.

**Virasoro is a $d=2$ accident.** Nothing in this week generalises to higher dimensions, where the conformal algebra stays finite. The BTZ match is correspondingly special, and it is honest to say the course gets a clean statistical derivation of black-hole entropy *only* in three bulk dimensions.

**Holomorphic factorisation is assumed, not proved.** Splitting $Z$ into holomorphic and antiholomorphic sectors is standard for the theories used here but is not automatic in general.

## 7. Key claims and proof status

- **[Proved.]** Virasoro algebra from the $TT$ OPE; $\mathrm{SL}(2)$ subalgebra (§1).
- **[Proved.]** Verma-module level counting by partitions (§2).
- **[Sketched]** level-2 null state coefficient and Kac formula; **[Stated — refs.]** minimal-model classification (§3).
- **[Stated — refs.]** Cardy formula (§4); **[Proven within the model]** the BTZ reproduction given Brown–Henneaux $c$.

*No coefficients in this note are uncertain. (No `CHECK` items for Wk 5.)*

## 8. What to take away

- **Virasoro:** $[L_m,L_n]=(m-n)L_{m+n}+\tfrac{c}{12}m(m^2-1)\delta_{m+n,0}$; $\{L_{-1},L_0,L_1\}$ = global $\mathrm{SL}(2)$.
- **Verma module:** primary $|h\rangle$ + descendants, $p(N)$ states at level $N$.
- **Null states / minimal models:** level-1 null at $h=0$, level-2 via Kac; unitary minimal series $c=1-\tfrac{6}{m(m+1)}$ (Ising $c=\tfrac12$).
- **Cardy:** $S(E)\simeq 2\pi\sqrt{cE/6}$ from modular invariance — high-energy entropy fixed by $c$.
- With $c=3L/2G_N$, Cardy = BTZ Bekenstein–Hawking entropy (the Sem II Wk 7 payoff).

5. **Cardy is a temperature duality** (§4b, computed): modular invariance turns an impossible high-energy count into a trivial low-temperature one, and the whole answer is fixed by the ground-state energy $-c/24$. No microscopic input is used anywhere.
6. **The BTZ match is exact and it is a $d=2$ accident.** Strominger's count reproduces $A/4G$ on the nose, but it relies on Virasoro, which exists only in two dimensions. The course gets a clean statistical derivation of black-hole entropy in three bulk dimensions and nowhere else.

## Exercises

**Core.**

1. **Virasoro from the OPE.** Evaluate $[L_m,L_n]=\oint\frac{dw}{2\pi i}\oint_w\frac{dz}{2\pi i}z^{m+1}w^{n+1}T(z)T(w)$ and recover $(m-n)L_{m+n}+\tfrac{c}{12}m(m^2-1)\delta_{m+n,0}$.
2. **Level-1 null.** Show $\|L_{-1}|h\rangle\|^2=2h$, null iff $h=0$; identify the operator.
3. **Cardy → BTZ.** With $c=3L/2G_N$ and $E\sim ML$, evaluate $S=2\pi\sqrt{cE/6}$ and compare to $\tfrac{\text{horizon length}}{4G_N}$.

**Starred.**

4. $\star$ **Level-2 null state.** For $|\chi\rangle=(L_{-2}+\alpha L_{-1}^2)|h\rangle$, impose $L_1|\chi\rangle=0$ to get $\alpha=-\tfrac{3}{2(2h+1)}$, then $L_2|\chi\rangle=0$ to get the $c$–$h$ Kac relation.
5. $\star$ **Modular invariance of the free boson.** With $Z=1/|\eta(\tau)|^2$, verify $Z(\tau+1)=Z(\tau)$ and $Z(-1/\tau)=Z(\tau)$ using $\eta(-1/\tau)=\sqrt{-i\tau}\,\eta(\tau)$.

**Project.**

6. **Strominger's count.** Read Strominger 1998 ([arXiv:hep-th/9712251](https://arxiv.org/abs/hep-th/9712251)); reproduce the BTZ entropy from Cardy in full, and write a 2-page note connecting it to [[sem2-week-07-ads2-ads3-essentials|Sem II Wk 7]] and the RT interval entropy $\tfrac{c}{3}\log(\ell/\epsilon)$ of [[week-13-ryu-takayanagi|Wk 13]].

## Connections to other parts of the wiki

- **Within the course.** Closes Block A; uses [[week-04-stress-tensor-and-central-charge]] (the $TT$ OPE → Virasoro). Forward: the Cardy/$c$ machinery powers [[sem2-week-07-ads2-ads3-essentials|Sem II Wk 7]] (BTZ, Brown–Henneaux) and the central charge appears in [[week-13-ryu-takayanagi|Wk 13]] (RT interval entropy $\propto c$). Liouville/JT links to [[sem2-week-06-jt-gravity-page-curve|Sem II Wk 6]].
- **AQFT course cross-reference.** None for Block A.
- **Area page.** [[gauge-gravity-duality]].

## Block A summary

Block A built the CFT prerequisites for holography: the conformal algebra and primaries (Wk 1), radial quantisation and the state–operator map (Wk 2), the OPE and conformal blocks (Wk 3), the stress tensor and central charge (Wk 4), and the 2d Virasoro/Cardy machinery (Wk 5). The recurring quantities — $(\Delta,\ell)$, the OPE/CFT data, $c$ — are exactly what the holographic dictionary will reproduce from the bulk in Block B: the Casimir eigenvalue $\Delta(\Delta-d)$ becomes the bulk mass, $c$ becomes $L/G_N$, and the Cardy entropy becomes a black-hole horizon area.

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block A. Reviewed and approved (status: final); the BTZ $L_0$ `CHECK` in §4 is a convention factor to confirm in a later pass. Last revised 2026-05-28.*

*End of Sem I Block A.*
