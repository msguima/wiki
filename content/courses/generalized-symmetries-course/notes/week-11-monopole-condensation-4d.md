---
title: "Week 11 — Compact U(1) in 4d: Monopole Condensation and the Dual Superconductor"
type: lecture-notes
course: syllabus
semester: 1
week: 11
block: C
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 8–10; energy–entropy arguments (Week 4); the Villain 4d duality (Week 8)
modified: 2026-07-01
---

# Week 11 — Compact U(1) in 4d: Monopole Condensation and the Dual Superconductor

> *In three dimensions monopoles are points and always proliferate, so compact QED always confines. In four dimensions they are worldlines with a real line tension, and a line tension can lose to entropy only above a threshold — so there is a genuine transition: a Coulomb phase of dilute loops and a confining phase of condensed ones. The confining vacuum is a superconductor for magnetic charge, and describing what condenses there — a proliferating ensemble of monopole worldlines — is where the Julia–Toulouse mechanism, and this course's research frontier, begins.*

## 0. Reading

**Primary:** Banks, Myerson, Kogut, *Nucl. Phys. B* 129 (1977) 493 (BMK); Guth, *Phys. Rev. D* 21 (1980) 2291 (existence of the Coulomb phase). For the dual-superconductor picture: Nambu, *Phys. Rev. D* 10 (1974) 4262; Mandelstam, *Phys. Rept.* 23 (1976) 245; 't Hooft (1975, Gribov proceedings).

**Secondary:**
- Quevedo & Trugenberger, *Nucl. Phys. B* 501 (1997) 143 [hep-th/9604196] — the Julia–Toulouse mechanism in field-theory form; see [[julia-toulouse-mechanism]].
- The concept pages [[dual-superconductor]] and [[julia-toulouse-mechanism]].

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]].

## 1. Monopoles are worldlines in 4d

From [[week-08-dual-variables-abelian-gauge|Week 8]], the monopole density $m_{\text{mono}} = dn \in C^3(\Lambda,\mathbb{Z})$ in $d=4$ is Poincaré-dual to a **1-cycle** on $\Lambda^*$: monopoles trace out **closed worldlines**. The Banks–Myerson–Kogut dual form writes the partition function as a sum over these monopole worldloops interacting through the 4d Coulomb ($1/r^2$) propagator, together with a free dual photon. The phase of the theory is decided by the statistical mechanics of the loop gas.

## 2. Energy–entropy for loops [Computed.]

This is the Week-4 argument, promoted from points to loops. A monopole worldloop of length $L$ (lattice units) carries:
- **Action** $S = \rho\,L$, with line tension $\rho \sim \dfrac{\text{const}}{e^2}$ (the Coulomb self-energy per unit length of the magnetic current).
- **Entropy** $S_{\text{ent}} = L\ln\mu$, where $\mu$ is the loop connectivity constant (the number of ways to extend a self-avoiding walk by one step; $\mu = O(2d-1)$ in $d=4$).

The free energy per unit length is
$$
f = \rho - \ln\mu.
$$
- $\rho > \ln\mu$ (**weak coupling**, small $e^2$): long loops are suppressed; only small, dilute loops survive. The photon stays **massless** — a **Coulomb phase**, with deconfined charges.
- $\rho < \ln\mu$ (**strong coupling**, large $e^2$): loops of arbitrary length proliferate — monopoles **condense**. The photon is gapped and charges **confine**.

The transition sits at $\rho = \ln\mu$. Unlike 3d, both phases are real:

**Guth's theorem [Stated — refs: Guth 1980].** *4d compact $U(1)$ has a genuine Coulomb phase at weak coupling* — the massless photon survives, monopoles do not condense, and the theory reproduces free Maxwell at long distance. The strong-coupling side is the confining phase whose area law we computed in [[week-06-wilson-action-strong-coupling|Week 6]]. The lattice transition between them is (weakly) first order.

> **Physical picture.** The one-dimensional difference from Week 9 changes the phase diagram entirely. A point defect has no tension to pay — only a fixed action — so a gas of points always proliferates (3d: always confined). A line defect must pay a tension per unit length, and a tension can be beaten by entropy only when the entropy per length $\ln\mu$ exceeds it — so there is a threshold (4d: a real Coulomb-to-confining transition). "Monopoles condense" means "monopole worldlines proliferate into arbitrarily long loops," the exact 4d analogue of vortex unbinding at BKT.

## 3. The dual superconductor

The confining phase has a name and a picture (Nambu, Mandelstam, 't Hooft): the vacuum is a **superconductor for magnetic charge**. Condensed monopoles are a magnetic charge condensate $\langle\phi_{\text{mag}}\rangle \neq 0$, and by the **dual Meissner effect** they expel and squeeze **electric** flux into thin tubes.

### 3.1 The dual Ginzburg–Landau description [Sketched.]

Model the condensate by a dual Ginzburg–Landau theory for a magnetically charged scalar $\phi$ coupled to the **dual** photon $\tilde a$:
$$
\mathcal{L}_{\text{dual}} = |\tilde D\phi|^2 - V(|\phi|) - \tfrac14 \tilde F_{\mu\nu}^2,\qquad \tilde D = \partial - i g\tilde a,
$$
with $V$ driving $\langle\phi\rangle\neq0$. Its **Abrikosov vortex** carries **electric** flux (the dual of the ordinary magnetic Abrikosov vortex) — this is the confining string. A quark–antiquark pair is joined by such a tube, of tension
$$
\sigma_{\text{str}} \sim |\langle\phi_{\text{mag}}\rangle|^2 \times (\text{logs, type-II}),
$$
giving the linear potential $V(R) = \sigma_{\text{str}} R$. The QCD flux tube is the dual Abrikosov vortex; confinement is the dual Meissner effect.

### 3.2 The 't Hooft loop and the magnetic symmetry

The disorder operator dual to the Wilson loop is the **'t Hooft loop** $\tilde W(\tilde C)$ — the worldline of a magnetic charge / the operator creating a unit of magnetic flux through $\tilde C$. It is the charged object of the **magnetic 1-form symmetry** (Bianchi $dF=0$). The two loops have complementary laws:
$$
\text{Coulomb phase:}\ \langle W\rangle\ \text{perimeter},\ \langle\tilde W\rangle\ \text{area};\qquad \text{confining phase:}\ \langle W\rangle\ \text{area},\ \langle\tilde W\rangle\ \text{perimeter}.
$$
In Semester II language: the Coulomb phase spontaneously breaks the magnetic 1-form symmetry (photon = its Goldstone), while the confining phase spontaneously breaks the **electric** 1-form symmetry (monopole condensate). The 't Hooft loop is the direct 4d descendant of the Kadanoff–Ceva disorder operator $\mu$ of [[week-04-bkt-kramers-wannier-disorder|Week 4]].

## 4. The Julia–Toulouse mechanism (first appearance)

What, precisely, is the low-energy theory of the condensed phase? The monopoles are a proliferating ensemble of **worldlines**; their condensate is naturally described not by a scalar but by an antisymmetric-tensor (**Kalb–Ramond**) 2-form field $B$ dual to the monopole current. Integrating in the condensate, the photon $F = da$ couples to $B$ through a **BF term** and becomes **massive**:
$$
\mathcal{L}_{\text{eff}} \ \sim\ B\wedge F + \tfrac{1}{2m^2}|dB|^2 + \cdots,
$$
a topologically massive / BF theory with no propagating long-range photon — confinement, encoded topologically.

This rank-changing condensation — a $p$-form defect ensemble condensing and changing the effective field content — is the **[[julia-toulouse-mechanism|Julia–Toulouse mechanism]]** (Quevedo–Trugenberger; and the UERJ group's 2009–2013 series). It is the direct field-theoretic implementation of the [[dual-superconductor]], and it is the object Semester II re-reads in the language of higher-form symmetry and condensation defects. The whole research frontier of this course — the group's manuscript on Julia–Toulouse condensation as higher gauging — is the modern life of the mechanism introduced on this page.

> **Physical picture.** "Monopole condensation" sounds like a scalar getting a VEV, but the honest statement is that a gas of *extended* objects (worldlines) proliferates, and the right order parameter is a *higher-form* field. That is the germ of generalized symmetry: the condensing object is extended, so the symmetry it breaks is higher-form, and the effective theory is topological (BF). Polyakov's 3d story (Week 10) is the point-defect version; this is the line-defect version; Semester II is the general theory of both.

## 5. Lattice Dirac quantization [Computed.]

The consistency of electric and magnetic charges is automatic on the lattice. The Villain integer $n$ (the Dirac string) threads plaquettes; requiring the Wilson loop $e^{ie\oint a}$ to be insensitive to the location of a monopole's Dirac string forces
$$
e\,g \in 2\pi\mathbb{Z},
$$
the **Dirac quantization** condition, here a statement about the integer cochain linking pairing of [[week-02-lattice-cell-complex-cochains|Week 2]]. The magnetic charge is quantized because $n$ is an integer.

## 6. What to take away

1. **4d monopoles are worldlines**, with an energy–entropy balance $f = \rho - \ln\mu$: a Coulomb phase (dilute loops, massless photon) and a confining phase (condensed loops). Guth proved the Coulomb phase is real — unlike 3d.
2. **The confining vacuum is a dual superconductor.** Condensed magnetic charge expels electric flux into Abrikosov-vortex tubes; the QCD string is the dual Abrikosov vortex, tension $\sim|\langle\phi_{\text{mag}}\rangle|^2$.
3. **The 't Hooft loop is the disorder operator** of the magnetic 1-form symmetry — the 4d descendant of Kadanoff–Ceva $\mu$.
4. **Monopole condensation is the Julia–Toulouse mechanism**: an extended-defect ensemble condensing into a higher-form (BF) effective theory — the seed of this course's research frontier.

## 7. Looking ahead: Week 12

Week 12 closes Block C with **θ-terms and the Witten effect**. We will find that the naive lattice θ-term is ill-defined, and that only the Villain/cochain formulation repairs it — the first crack that the modified Villain construction of Semester II fully seals. Along the way: dyons and the Witten effect, θ-periodicity as spectral flow, oblique confinement, and axionic electrodynamics, where this line meets the group's [[condensed-matter-connections|condensed-matter]] work.

## 8. Problem set

**Core problems** (everyone).

**1. Loop energy–entropy.**
(a) Estimate the monopole line tension $\rho$ from the 4d Coulomb self-energy of a unit magnetic current.
(b) Write the free energy per length $f = \rho - \ln\mu$ and locate the condensation threshold; identify which coupling regime confines and check consistency with the Week 6 strong-coupling area law.

**2. The two loops.**
Tabulate the area/perimeter behavior of the Wilson and 't Hooft loops in the Coulomb and confining phases, and state each phase's spontaneously broken (electric or magnetic) 1-form symmetry.

**3. Dirac quantization on the lattice.**
Derive $eg \in 2\pi\mathbb{Z}$ from requiring the Wilson loop to be blind to the position of a monopole's Dirac string (the Villain integer $n$), using the cochain linking pairing.

**Starred problems.**

**4⋆. Dual Ginzburg–Landau vortex.**
In the dual GL theory, construct the electric Abrikosov vortex (the confining string) and estimate its tension in terms of $\langle\phi_{\text{mag}}\rangle$ and the dual gauge coupling. Distinguish type-I and type-II regimes and the corresponding string–string interactions.

**5⋆. The BF effective theory.**
Starting from the condensed monopole worldline ensemble, derive the BF/topologically-massive effective Lagrangian $\mathcal{L} \sim B\wedge F + \frac{1}{2m^2}|dB|^2$ and show the photon acquires a mass. Identify the rank change (1-form photon → 2-form $B$) as the Julia–Toulouse mechanism. (This is the calculation the group's research line generalizes.)

**6⋆⋆ (optional).**
Discuss what changes for $SU(N)$: why the abelian dual-superconductor picture requires an "abelian projection" (maximal abelian gauge), what "abelian dominance" means on the lattice, and why the gauge-dependence of the monopoles is the central open issue in taking this picture literally for QCD.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block C. Last revised 2026-07-01.*
