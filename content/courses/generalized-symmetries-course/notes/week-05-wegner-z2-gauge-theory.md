---
title: "Week 5 — Wegner's ℤ₂ Gauge Theory: Phases Without a Local Order Parameter"
type: lecture-notes
course: syllabus
semester: 1
week: 5
block: B
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 1–4 (cochains, duality, Kramers–Wannier, disorder operators); the 2d Ising model
modified: 2026-07-01
---

# Week 5 — Wegner's ℤ₂ Gauge Theory: Phases Without a Local Order Parameter

> *In 1971 Wegner gauged the Ising model and found something that should not have existed in the Landau worldview: a phase transition with no local order parameter, on either side of which every local field has zero expectation value. He needed a new diagnostic — a Wilson loop, before Wilson — and what he had discovered was topological order, half a century before the name. Block B begins here, and the whole modern story of confinement and topological matter is the working-out of Wegner's puzzle.*

## 0. Reading

**Primary:** Wegner, *J. Math. Phys.* 12 (1971) 2259 — the founding paper; §§1–3. Kogut, *Rev. Mod. Phys.* 51 (1979) 659, §§IV–V — the review telling.

**Secondary:**
- Fradkin, *Field Theories of Condensed Matter Physics*, 2nd ed., ch. 9 — ℤ₂ gauge theory and its dualities.
- Kogut & Susskind, *Phys. Rev. D* 11 (1975) 395 — for the Hamiltonian version we build in [[week-07-kogut-susskind-hamiltonian|Week 7]].

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]]. Cochain conventions from [[week-02-lattice-cell-complex-cochains|Week 2]].

## 1. Gauging the Ising model

Take the Ising ℤ₂ global symmetry $s_x \to \epsilon\, s_x$ ($\epsilon = \pm1$ everywhere) and make it **local**: $s_x \to \epsilon_x s_x$ with an independent $\epsilon_x = \pm1$ at each site. The nearest-neighbor term $s_x s_y$ is not invariant; to fix it we introduce a **gauge field** on links — a variable $\sigma_\ell = \pm 1$ for each link $\ell = (x,y)$ — transforming as
$$
\sigma_\ell \to \epsilon_x\, \sigma_\ell\, \epsilon_y .
$$
Then $s_x \sigma_\ell s_y$ is gauge-invariant. The **pure gauge theory** drops the matter $s$ entirely and keeps the smallest gauge-invariant object built from links alone — the product around a plaquette:
$$
\sigma_P = \prod_{\ell\in\partial P}\sigma_\ell = (d\sigma)_P \ (\text{in additive } \mathbb{Z}_2 \text{ notation}),
$$
which is gauge-invariant because each site variable $\epsilon_x$ appears twice. **Wegner's ℤ₂ gauge theory** is
$$
\boxed{\ Z = \sum_{\{\sigma_\ell = \pm1\}} \exp\!\Big(\beta \sum_P \sigma_P\Big),\qquad \sigma_P = \prod_{\ell\in\partial P}\sigma_\ell.\ }
$$
In cochain language ([[week-02-lattice-cell-complex-cochains|Week 2]]) $\sigma$ is a $\mathbb{Z}_2$ 1-cochain, $\sigma_P = (d\sigma)_P$ is the field strength, and gauge transformations act by $\sigma \to \sigma + d\epsilon$. This is the lattice ℤ₂ analogue of $F = dA$ with $A \to A + d\lambda$.

## 2. Elitzur's theorem: local symmetries do not break

### 2.1 Statement and consequence

The first surprise is a no-go theorem.

**Theorem (Elitzur, 1975). [Computed — see §2.2.]** *In a lattice gauge theory, the expectation value of any gauge-non-invariant local operator vanishes identically, at all couplings:*
$$
\langle \sigma_\ell\rangle = 0 \quad\text{exactly, for all } \beta.
$$

So the link field — the natural "order parameter" by analogy with the Ising magnetization $\langle s\rangle$ — is useless: it is zero everywhere, in every phase. A gauge theory **cannot** be diagnosed by a local order parameter. This is not a statement about a particular phase; it is a structural fact forced by local symmetry.

### 2.2 Proof [Computed.]

Add a small gauge-non-invariant source $h$ coupling to $\sigma_\ell$ and compute $\langle\sigma_\ell\rangle_h$; Elitzur's theorem is that $\lim_{h\to0}\langle\sigma_\ell\rangle_h = 0$ **uniformly in the volume** (so no spontaneous breaking can sneak in through the thermodynamic limit).

The mechanism: perform the gauge transformation $\epsilon_x = \pm1$ at a *single* endpoint $x$ of $\ell$, summing over its two values. The gauge-invariant plaquette action is unchanged; only the source term and the link flip. Since $\sigma_\ell \to \epsilon_x\sigma_\ell$ is odd under $\epsilon_x\to-\epsilon_x$, the average over $\epsilon_x=\pm1$ of the source-weighted expectation is bounded by the source strength alone:
$$
|\langle\sigma_\ell\rangle_h| \ \le\ \tanh(c\, h) \ \xrightarrow{h\to0}\ 0,
$$
with $c$ fixed by the local coordination number and **independent of the system size**. The point is that a single site's gauge freedom is a *zero-dimensional* system, and a zero-dimensional system cannot order. [The careful bound is Problem 1.] $\square$

> **Physical picture.** Elitzur is the reason this whole course exists. In a theory with local symmetry, "is the symmetry broken?" is not answered by any local field — every candidate averages to zero. You are forced to extended, gauge-invariant operators: Wilson loops, 't Hooft loops, Polyakov lines. The entire modern language of generalized symmetry is the systematic development of "the right observables are extended," and it starts with Elitzur telling us the local ones are dead.

## 3. The Wilson loop, before Wilson

The surviving gauge-invariant observables built from $\sigma$ alone are products around **closed loops** $C$:
$$
W(C) = \prod_{\ell\in C}\sigma_\ell .
$$
$W(C)$ is gauge-invariant (each site on $C$ meets two loop links, so every $\epsilon_x$ cancels). Its expectation distinguishes the phases by how it scales with the loop's **geometry**:
$$
\langle W(C)\rangle \sim \begin{cases} e^{-\sigma_{\text{str}}\,\mathrm{Area}(C)} & \textbf{confining (area law)} \\ e^{-\mu\,\mathrm{Perim}(C)} & \textbf{deconfining (perimeter law)} \end{cases}
$$
The area law says the energy of a static charge–anticharge pair on the loop grows **linearly** with separation (the area of a rectangular loop is separation × time): a confining string. The perimeter law says the pair energy saturates: free charges.

### 3.1 Strong coupling: the area law [Computed.]

At small $\beta$, expand the Boltzmann weight per plaquette (ℤ₂ version of the high-$T$ expansion, Week 4):
$$
e^{\beta\sigma_P} = \cosh\beta\,(1 + \sigma_P\tanh\beta).
$$
Then $\langle W(C)\rangle = \big\langle \prod_{\ell\in C}\sigma_\ell \big\rangle$. Summing over each $\sigma_\ell = \pm1$ kills any term in which a link appears an **odd** number of times. The loop $C$ contributes each of its links once; to cancel them we must supply each with one more factor, drawn from the $\sigma_P\tanh\beta$ terms — i.e. we must **tile a surface** spanning $C$ with plaquettes. The minimal tiling has $\mathrm{Area}(C)$ plaquettes, so
$$
\langle W(C)\rangle \simeq (\tanh\beta)^{\mathrm{Area}(C)} = e^{-\sigma_{\text{str}}\,\mathrm{Area}(C)},\qquad \sigma_{\text{str}} = -\ln\tanh\beta .
$$
**Confinement is generic at strong coupling.** The string tension $\sigma_{\text{str}} = -\ln\tanh\beta \to \infty$ as $\beta\to0$ and decreases as $\beta$ grows; whether it survives to weak coupling is the phase-transition question.

### 3.2 Weak coupling and the transition

At large $\beta$ the fluctuations of $\sigma$ around a flat ($\sigma_P = +1$) configuration are small, and one finds a **perimeter law** (Problem 2): the loop cost becomes proportional to its length, and static charges deconfine. In $d\ge3$ these two behaviors are separated by a genuine phase transition. In $d=2$ the gauge theory is trivial (every configuration is pure gauge up to global data) and always "confining" in a degenerate sense.

## 4. Self-duality and the map to the Ising model

Wegner also found the ℤ₂ gauge theory's **dual**, generalizing Kramers–Wannier ([[week-04-bkt-kramers-wannier-disorder|Week 4]]).

**In $d=3$:** the 3d ℤ₂ gauge theory is dual to the **3d Ising model**. [Sketched; Problem 3.] The high-temperature (small-$\beta$) surface expansion of the gauge theory — sums over closed surfaces (2-cycles) — maps, by Poincaré duality on the dual lattice, to the low-temperature domain-wall expansion of the Ising model, whose domain walls are also closed surfaces. The dictionary is $\tanh\beta_{\text{gauge}} = e^{-2\beta^*_{\text{Ising}}}$, and the gauge theory's confinement–deconfinement transition sits at the image of the 3d Ising critical point.

**In $d=4$:** the 4d ℤ₂ gauge theory is **self-dual** — gauge theory maps to gauge theory — with the self-dual point locating its transition. (The $d=4$ self-duality is the ℤ₂ ancestor of the electric–magnetic self-duality of 4d Maxwell in Semester II.)

> **Physical picture.** The 3d duality is profound: the *deconfined* phase of the gauge theory is the *ordered* phase of a dual Ising spin. But the gauge theory has **no** local order parameter (Elitzur), while the dual Ising has the obvious one $\langle s\rangle$. The same physics is "hidden-variable ordered" on one side and "order-parameter ordered" on the other. The order parameter of the gauge theory is *nonlocal* — a disorder operator / 't Hooft loop, the direct analogue of Kadanoff–Ceva $\mu$ from Week 4. Semester II names the gauge-side order: spontaneously broken 1-form symmetry.

## 5. What Wegner actually discovered

Assemble the pieces:
- A phase transition **with no local order parameter** (Elitzur kills every local candidate on both sides).
- Diagnosed only by an **extended** operator (the Wilson loop), through its area-vs-perimeter geometry.
- With a **dual** description in which the transition looks like ordinary Ising ordering.

This is **topological order**, discovered in 1971 — the same phenomenon we will meet as the deconfined phase of ℤ₂ gauge theory, as Kitaev's toric code, and as the $B$-side of the Fradkin–Shenker diagram. Wegner had the physics; the language (1-form symmetry, long-range entanglement, anyons) took fifty years. Block B and Semester II supply that language.

## 6. What to take away

1. **Gauging trades a global symmetry for a link field with a local redundancy.** The gauge-invariant content is the plaquette flux $\sigma_P = (d\sigma)_P$ — the ℤ₂ field strength.
2. **Elitzur: local symmetries never break.** No gauge-variant local operator can order; the diagnostics of gauge theory are unavoidably extended.
3. **The Wilson loop diagnoses phases by geometry.** Area law = confinement (linear potential), perimeter law = deconfinement; strong coupling always confines.
4. **Wegner's transition is topological order, 1971.** No local order parameter, an extended diagnostic, and an Ising-like dual — the template for the whole course.

## 7. Looking ahead: Week 6

Wegner's ℤ₂ is the simplest gauge group. Week 6 replaces it with the continuous groups of real gauge theory — $U(1)$ and $SU(N)$ — and develops the tool that makes strong coupling computable there: **Haar integration and the character expansion**. The Wilson loop area law and the string tension get computed for continuous groups, and we meet the roughening transition and the handoff to Monte Carlo. The logic — Elitzur, extended operators, area vs perimeter — carries over unchanged; only the group-theory bookkeeping is new.

## 8. Problem set

**Core problems** (everyone).

**1. Elitzur's theorem, the careful bound.**
(a) Introduce a source $h\sum_\ell \sigma_\ell$ and show, by summing over a single endpoint gauge transformation, that $|\langle\sigma_\ell\rangle_h| \le \tanh(ch)$ with $c$ volume-independent.
(b) Conclude $\langle\sigma_\ell\rangle = 0$ in the $h\to0$ limit uniformly in volume. Contrast with the Ising magnetization, where the analogous bound is *not* volume-independent and ordering survives.

**2. Wilson loop, both laws.**
(a) Derive $\langle W(C)\rangle \simeq (\tanh\beta)^{\mathrm{Area}}$ at small $\beta$ in $d=3$; extract $\sigma_{\text{str}}(\beta)$ and its first correction (the next tiling).
(b) At large $\beta$, expand around $\sigma_P = +1$ and show a perimeter law; interpret the perimeter coefficient as a (subtractable) self-energy of the static charges.
(c) Argue that a perimeter law can be removed by a local redefinition of the loop but an area law cannot — so the area law is the invariant statement of confinement.

**3. The 3d duality.**
Set up the surface (small-$\beta$) expansion of the 3d ℤ₂ gauge theory and the domain-wall (low-$T$) expansion of the 3d Ising model, and match them via Poincaré duality on the dual lattice to obtain $\tanh\beta_{\text{gauge}} = e^{-2\beta^*_{\text{Ising}}}$. Locate the gauge transition from the known 3d Ising $\beta_c$.

**Starred problems.**

**4⋆. The 't Hooft loop as the gauge-side disorder operator.**
Construct the ℤ₂ **'t Hooft loop** $\tilde W(\tilde C)$ on the dual lattice: the operator that flips $\beta\to-\beta$ on the plaquettes pierced by a dual loop $\tilde C$ (equivalently, inserts a unit of magnetic flux through $\tilde C$). (a) Show it is gauge-invariant. (b) Compute its expectation in each phase and show it is the *disorder* dual of the Wilson loop (area law when $W$ has perimeter law and vice versa). (c) Relate $\tilde W$ to the Kadanoff–Ceva $\mu$ of Week 4.

**5⋆. Global structure on the torus.**
On $T^3$, classify the ℤ₂ gauge theory's flat configurations by $H^1(T^3,\mathbb{Z}_2) = \mathbb{Z}_2^3$ and count the resulting near-degenerate low-energy states in the deconfined phase. (This is the ground-state degeneracy that Semester II reads as spontaneously broken 1-form symmetry / topological order.)

**6⋆⋆ (optional).**
Show that the 4d ℤ₂ gauge theory is self-dual, identify the self-dual coupling, and discuss why self-duality alone does not prove there is a *single* transition there (contrast the 3d gauge/Ising case). What extra input fixes the order of the 4d transition?

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block B. Last revised 2026-07-01.*
