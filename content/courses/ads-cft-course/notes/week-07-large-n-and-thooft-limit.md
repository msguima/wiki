---
title: "Week 7 — Large-N gauge theory and the 't Hooft limit"
type: lecture-notes
course: syllabus
semester: 1
week: 7
block: B
duration: "4 hours (2 lectures × 2 hours)"
status: drafting
modified: 2026-05-28
---

# Week 7 — Large-$N$ Gauge Theory and the 't Hooft Limit

> *Why is a strongly-coupled gauge theory dual to **classical** gravity? The answer is the 't Hooft limit. Holding $\lambda=g^2N$ fixed and sending $N\to\infty$ organises the Feynman expansion by the **topology** of ribbon graphs: planar diagrams dominate, and $1/N$ becomes a genus-counting (loop-counting) parameter — the bulk $G_N$. In this limit single-trace operators **factorise** and behave as generalised free fields (the GFF of [[week-03-ope-and-conformal-blocks|Week 3]]), and their algebra becomes **type III$_1$** — the structural fact the whole Semester II algebraic program (and the group's own work) rests on. This is the most conceptually important week of Block B.*

## Learning goals

By the end of this week, a student can:

1. State the 't Hooft limit ($N\to\infty$, $\lambda=g^2N$ fixed) and explain why it is the sensible one.
2. **Derive** the genus scaling $N^{2-2g}$ of a vacuum diagram by double-line counting.
3. Define single-trace operators and state large-$N$ factorisation $\langle\mathcal{O}_1\cdots\mathcal{O}_n\rangle_c = O(N^{2-n})$.
4. Explain why single-trace operators are generalised free fields at $N=\infty$, linking to the GFF of Week 3.
5. State that the single-trace algebra is type III$_1$ at $N=\infty$ and why $1/N$ is the quantum-gravity parameter.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *AdS/CFT Foundations* §2** — the 't Hooft limit, single-trace operators and factorisation. *Modern CFT* §12 for the planar expansion and generalised free fields.
- 't Hooft, *A planar diagram theory for strong interactions*, Nucl. Phys. B72 (1974) 461 — the founding paper.
- AGMOO, [arXiv:hep-th/9905111](https://arxiv.org/abs/hep-th/9905111), §1.2 — in the holographic context.

**Prerequisites.** [[week-06-ads-geometries]] (the bulk this dual lives in); [[week-03-ope-and-conformal-blocks]] (the GFF four-point function — single-trace operators realise exactly that structure).

**AQFT cross-reference.** The type III$_1$ statement of §5 is developed rigorously in the AQFT course; this week's `holography-large-n-primer` §E.2 (AQFT appendices) is the lightweight companion, and Sem II builds the crossed-product machinery on top.

## 1. The 't Hooft limit

Take a $\mathrm{U}(N)$ (or $\mathrm{SU}(N)$) gauge theory with coupling $g$. Naively $N\to\infty$ at fixed $g$ is singular (each gluon loop brings a factor $g^2 N$). 't Hooft's insight: hold

$$
\boxed{\;\lambda \equiv g^2 N\ \text{fixed},\qquad N\to\infty.\;}
$$

Then $\lambda$ controls the loop expansion *within* a given topology, and $1/N$ controls the topology. To see this, normalise the action à la 't Hooft, $S=\tfrac{N}{\lambda}\,\mathrm{Tr}(\dots)$, so the propagator carries $\lambda/N$ and each vertex carries $N/\lambda$.

## 2. Double-line counting and the genus expansion (worked)

Adjoint fields $\Phi^i{}_j$ carry a fundamental and an antifundamental index, so a propagator is a **double line** (two oppositely-directed index lines). A Feynman diagram becomes a **ribbon graph** that triangulates a surface. Count powers of $N$:

- each **propagator** (edge $E$): $\lambda/N$;
- each **vertex** ($V$): $N/\lambda$;
- each **closed index loop** (face $F$): a free color sum $\sum_{i=1}^N = N$.

So a vacuum diagram scales as

$$
\Big(\tfrac{N}{\lambda}\Big)^{V}\Big(\tfrac{\lambda}{N}\Big)^{E} N^{F}
= N^{\,V-E+F}\,\lambda^{\,E-V}
= N^{\chi}\,\lambda^{E-V},
$$

where $\chi = V-E+F$ is the **Euler characteristic** of the surface the ribbon graph tiles. By Euler's formula $\chi = 2-2g$ ($g$ = genus), so

$$
\boxed{\;\text{amplitude} \sim \sum_{g=0}^{\infty} N^{2-2g}\,f_g(\lambda).\;}
$$

**Planar dominance:** the leading term is $g=0$ ($\chi=2$, a sphere) — the planar diagrams. Higher genus is suppressed by $N^{-2g}$. This is the exact analogue of the string-theory genus expansion with $g_s\sim 1/N$ — the first quantitative hint that the dual is a *string/gravity* theory, with $1/N$ playing the role of the gravitational ($G_N$) coupling.

**Worked example: the "sunset" diagram, planar vs non-planar.** Take the vacuum diagram with two cubic vertices joined by three propagators (the sunset/theta graph): $V=2$, $E=3$. Drawn **planarly** on the sphere, the three double-line propagators bound three index loops — $F=3$ — so

$$
\chi = V-E+F = 2-3+3 = 2 \;\Rightarrow\; N^{\chi}=N^2\quad(g=0).
$$

Now redraw the *same* graph with one propagator's double lines **crossed** (a non-planar embedding): the crossing merges index loops, leaving $F=1$, so

$$
\chi = 2-3+1 = 0 \;\Rightarrow\; N^{0}\quad(g=1,\ \text{torus}).
$$

Same vertices and edges, same power of $\lambda$ ($\lambda^{E-V}=\lambda$), but the non-planar version is down by $N^{0}/N^{2}=1/N^{2}$ — one handle costs $N^{-2}$. This single example is the whole mechanism: topology, read off as $V-E+F$, controls the power of $N$.

> **[Proven]** the $N^{2-2g}$ scaling, by the $V-E+F=\chi$ counting above and the worked sunset example (Exercise 1 generalises).

## 3. Single-trace operators and factorisation

The natural gauge-invariant operators are **single-trace**, $\mathcal{O}_k\sim\mathrm{Tr}(\Phi^k)$, normalised so the connected two-point function is $O(1)$:

$$
\boxed{\;\langle\mathcal{O}_1\cdots\mathcal{O}_n\rangle_{\mathrm{conn}} = O\!\big(N^{2-n}\big).\;}
$$

(Same genus counting: a connected correlator with $n$ external single-traces sits on a sphere with $n$ boundaries, $\chi=2-n$.) So the **connected** $n$-point function is suppressed for $n\ge3$: $\langle\mathcal{O}\mathcal{O}\rangle_c=O(1)$, $\langle\mathcal{O}\mathcal{O}\mathcal{O}\rangle_c=O(1/N)$, and so on. Consequently the *full* correlators **factorise**:

$$
\langle\mathcal{O}_1\mathcal{O}_2\mathcal{O}_3\mathcal{O}_4\rangle = \langle\mathcal{O}_1\mathcal{O}_2\rangle\langle\mathcal{O}_3\mathcal{O}_4\rangle + (\text{perms}) + O(1/N^2),
$$

i.e. single-trace operators behave like **Gaussian random variables** at leading order — a [[large-n-factorization|generalised free field]]. This is *exactly* the GFF whose four-point function and double-trace tower $[\mathcal{O}\mathcal{O}]_{n,\ell}$ we worked out in [[week-03-ope-and-conformal-blocks|Week 3 §5]]. Holographically: a GFF boundary operator is dual to a **free bulk field** in AdS; the $O(1/N^2)$ corrections to factorisation are bulk interactions (Witten diagrams, Wk 8 / Sem II Wk 2), and the double-trace anomalous dimensions are bulk binding energies.

**Worked example: connected vs disconnected in a matrix model.** Make factorisation concrete in the Gaussian Hermitian matrix model with the 't Hooft normalisation $S=\tfrac{N}{2}\mathrm{Tr}\,M^2$ (so the propagator is $\langle M^i{}_j M^k{}_l\rangle=\tfrac1N\delta^i_l\delta^k_j$). Consider the single-trace $\mathcal{O}=\mathrm{Tr}\,M^2$.

- *One-point:* $\langle\mathrm{Tr}\,M^2\rangle = \langle M^i{}_j M^j{}_i\rangle = \tfrac1N\delta^i_j\delta^j_i = \tfrac1N\cdot N^2 = N$. So $\langle\mathcal{O}\rangle=O(N)$.
- *Connected two-point:* $\langle\mathrm{Tr}\,M^2\,\mathrm{Tr}\,M^2\rangle_c$ comes from the two Wick contractions linking the two traces; each gives $\tfrac{1}{N^2}$ with index loops contributing $N^2$, so $\langle\mathcal{O}\mathcal{O}\rangle_c = O(N^0)=O(1)$.
- *Disconnected:* $\langle\mathcal{O}\rangle^2 = O(N^2)$.

So the full $\langle\mathcal{O}\mathcal{O}\rangle = \underbrace{O(N^2)}_{\text{disconnected}} + \underbrace{O(1)}_{\text{connected}}$, the connected piece suppressed by $1/N^2$ — exactly $\langle\mathcal{O}\mathcal{O}\rangle_c/\langle\mathcal{O}\rangle^2 = O(N^{-2})$. The *normalised* fluctuation $\delta\mathcal{O}=\mathcal{O}-\langle\mathcal{O}\rangle$ has $O(1)$ variance and, by the same counting, an $O(1/N)$ three-point function: it is a generalised free field with Gaussian statistics up to $1/N$. This is the matrix-model face of "single-trace = GFF," and the $1/N$ here is literally the genus-suppression of §2.

> **[Proven]** the matrix-model scalings above (Wick counting). **[Stated-without-proof]** the general factorisation $\langle\cdots\rangle_c=O(N^{2-n})$ (genus counting of §2 applied to correlators).

## 4. Large $N$ = classical gravity

The genus expansion $\sum_g N^{2-2g}f_g(\lambda)$ is structurally a **closed-string genus expansion** with $g_s\sim1/N$. In the holographic dual:

- $N=\infty$ ⟺ **classical** (tree-level) gravity in the bulk;
- $1/N^2$ ⟺ bulk quantum-gravity loops, $G_N\sim 1/N^2$ (in AdS units);
- large $\lambda$ ⟺ the bulk is weakly curved (the supergravity/two-derivative regime), with $\alpha'/L^2\sim\lambda^{-1/2}$ stringy corrections.

So the regime where the bulk is ordinary (weakly-coupled, weakly-curved) classical gravity is **large $N$, large $\lambda$** — precisely where the boundary gauge theory is strongly coupled and intractable. This is the source of the duality's power and of its difficulty: the two descriptions are useful in opposite regimes.

## 5. The algebra at $N=\infty$: type III$_1$

Here is the structural payload, and the bridge to Semester II and to the group's own program. At strict $N=\infty$, the algebra generated by single-trace operators on a boundary subregion is a **generalised free field algebra**, and under mild conditions it is a **type III$_1$ von Neumann factor** — no trace, no density matrix, exactly the algebraic class of local QFT algebras ([[type-iii-von-neumann-algebras]], [[subregion-subalgebra-duality]]).

- At **finite $N$** the boundary theory has a finite-dimensional Hilbert space per region (type I); the type III$_1$ structure is an emergent feature of the $N\to\infty$ limit.
- The $1/N^2$ corrections are what the **crossed-product** construction (Witten 2022 / CPW) organises: dressing the type III$_1$ algebra by its modular flow produces a type II$_\infty$ algebra with a finite (generalised) entropy. That is the holographic image of "$N=\infty$ classical gravity + $1/N^2$ quantum corrections."

So the emergence of type III$_1$ *is* the emergence of smooth classical bulk geometry; the algebraic and geometric statements of "large $N$ = classical gravity" are the same statement.

> **[Stated-without-proof]** type III$_1$ at $N=\infty$, type I at finite $N$ (Sem II; Liu lectures; AQFT course). The crossed-product promotion to II$_\infty$ is the Sem II Block 1 result.

## 6. Key claims and proof status

- **[Proven]** genus scaling $N^{2-2g}$ by double-line counting (§2).
- **[Stated-without-proof]** factorisation $\langle\cdots\rangle_c=O(N^{2-n})$; single-trace = GFF (§3).
- **[Stated-without-proof]** $1/N^2 = G_N$; large-$N$-large-$\lambda$ = weakly-curved classical gravity (§4).
- **[Stated-without-proof]** single-trace algebra type III$_1$ at $N=\infty$ (§5).

*No coefficients in this note are uncertain. (No `CHECK` items for Wk 7.)*

## 7. What to take away

- **'t Hooft limit:** $N\to\infty$, $\lambda=g^2N$ fixed; $1/N$ counts genus/topology, $\lambda$ counts loops within a topology.
- **Genus expansion** $\sum_g N^{2-2g}f_g(\lambda)$ from double-line counting ($N^\chi=N^{2-2g}$); planar dominates ⟹ string/gravity dual with $g_s\sim1/N$.
- **Single-trace factorisation** $\langle\cdots\rangle_c=O(N^{2-n})$ ⟹ single-trace = **generalised free field** = free bulk field; $1/N^2$ = bulk interactions (the Week 3 GFF made dynamical).
- **Large $N$ = classical gravity:** $G_N\sim1/N^2$; the useful bulk regime (large $N$, large $\lambda$) is the intractable boundary regime.
- **Type III$_1$ at $N=\infty$** is the algebraic face of emergent classical geometry — the Sem II / crossed-product starting point.

## Exercises

**Core.**

1. **Genus counting.** For a chosen vacuum diagram in $\phi^3$ (or $\phi^4$) matrix theory, count $V,E,F$, compute $\chi=V-E+F$, and verify the $N^{2-2g}$ scaling. Do one planar and one non-planar example.
2. **Connected vs disconnected.** For single-trace $\mathcal{O}$ normalised to $\langle\mathcal{O}\mathcal{O}\rangle_c=O(1)$, show $\langle\mathcal{O}\mathcal{O}\mathcal{O}\rangle_c=O(1/N)$ and that the full $\langle\mathcal{O}^4\rangle$ is dominated by the disconnected $O(1)$ pieces with $O(1/N^2)$ connected correction.
3. **Vacuum polarisation.** In a $\mathrm{U}(N)$ theory, count the $N$-scaling of the planar vs leading non-planar contribution to a single-trace two-point function and confirm their ratio is $1/N^2$.

**Starred.**

4. $\star$ **GFF match.** Show that large-$N$ factorisation reproduces the generalised-free-field four-point function of [[week-03-ope-and-conformal-blocks|Week 3 §5]], and identify the double-trace operators $[\mathcal{O}\mathcal{O}]_{n,\ell}$ as the leading new primaries in the $\mathcal{O}\times\mathcal{O}$ OPE.
5. $\star$ **String coupling.** Argue from the genus expansion that the dual string coupling is $g_s\sim1/N$ and relate $G_N\sim g_s^2\sim1/N^2$ in AdS units.

**Project.**

6. **Type III$_1$ emergence.** Read the [[holography-large-n-primer|AQFT holography primer]] §E.2–E.3 (and Liu §3); explain why the single-trace algebra is type I at finite $N$ and type III$_1$ at $N=\infty$, and how the crossed product (Sem II) reintroduces a trace. Connect to [[crossed-product-and-island-formula]].

## Connections to other parts of the wiki

- **Within the course.** Prerequisite for [[week-08-gkp-witten-formula]] (GKP-W operates in this large-$N$, large-$\lambda$ limit; single-trace $\mathcal{O}$ are its boundary operators). The GFF structure is from [[week-03-ope-and-conformal-blocks]]; the type III$_1$ thread continues into [[sem2-week-03-modular-flow-on-subregions|Sem II Wk 3]] and [[sem2-week-12-er-epr-and-tfd|Wk 12]].
- **AQFT course cross-reference.** [[holography-large-n-primer|AQFT holography-large-N primer]] §E.2; the type III$_1$ / crossed-product machinery is AQFT Sem II.
- **Open questions raised.** [[crossed-product-and-island-formula]] (algebraic large-$N$); [[holographic-dual-embezzlement-protocol]] (the $1/N^2$ corrections to exact-at-$N=\infty$ statements).
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block B. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*
