---
title: "Week 12 — θ-Terms, the Witten Effect, and Oblique Responses"
type: lecture-notes
course: syllabus
semester: 1
week: 12
block: C
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 8–11; the Villain formulation and cup products (Weeks 2, 8); electromagnetic duality
modified: 2026-07-01
---

# Week 12 — θ-Terms, the Witten Effect, and Oblique Responses

> *A θ-angle looks like a harmless total derivative, but on a compact gauge field it reorganizes the charge lattice: monopoles become dyons (the Witten effect), the theory is periodic in θ only up to a relabeling of charges (spectral flow), and at special angles dyons condense into oblique-confined phases. The lattice exposes a subtlety the continuum hides — the naive lattice θ-term is not 2π-periodic, and only the Villain/cochain construction repairs it. That crack is the one the modified Villain program of Semester II seals. Along the way, θ-electrodynamics is exactly the physics of topological insulators and Weyl semimetals, where this course meets the group's condensed-matter line.*

## 0. Reading

**Primary:** Witten, *Phys. Lett. B* 86 (1979) 283 (the Witten effect); Cardy & Rabinovici, *Nucl. Phys. B* 205 (1982) 1 (the $(n_e,n_m)$ lattice and oblique confinement).

**Secondary:**
- Wilczek, *Phys. Rev. Lett.* 58 (1987) 1799 — axion electrodynamics.
- The concept pages [[axionic-electrodynamics]] and the area [[condensed-matter-connections]].
- Gorantla–Lam–Seiberg–Shao, arXiv:2103.01257 — the modified-Villain θ-term (Semester II Week 12).

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]].

## 1. The θ-term

Maxwell theory admits a second, topological term,
$$
S_\theta = \frac{\theta}{8\pi^2}\int F\wedge F = \frac{\theta}{32\pi^2}\int d^4x\ \varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}.
$$
On a closed 4-manifold $\frac{1}{8\pi^2}\int F\wedge F = $ (instanton number) $\in\mathbb{Z}$ for a properly quantized flux, so $S_\theta$ shifts the action by $\theta\times$integer and the physics is periodic, $\theta\sim\theta+2\pi$. It is a total derivative and does not affect the classical equations of motion — but it is not invisible: it acts on the **spectrum of charges**.

## 2. The Witten effect [Computed.]

Turn on θ and ask what electric charge a magnetic monopole carries. The θ-term modifies the momentum conjugate to $a$: the electric field picks up a magnetic piece,
$$
\Pi_i = \frac{1}{e^2}E_i + \frac{\theta}{4\pi^2}B_i,
$$
so Gauss's law $\partial_i\Pi_i = \rho$ becomes, for the physical electric charge,
$$
\partial_i\Big(\frac{1}{e^2}E_i\Big) = \rho - \frac{\theta}{4\pi^2}\partial_i B_i .
$$
A monopole has $\partial_i B_i = 4\pi g\,\delta^{(3)}$ with $g$ its magnetic charge; it therefore sources electric charge. In units of the elementary charge, a dyon with integer magnetic number $n_m$ and integer "bare" electric number $n_e$ carries
$$
\boxed{\ q_e = n_e + \frac{\theta}{2\pi}\,n_m.\ }
$$
**Monopoles become dyons**: at $\theta\neq0$ a pure monopole ($n_e=0$, $n_m=1$) carries fractional electric charge $\theta/2\pi$.

> **Physical picture.** The θ-angle tilts the charge lattice. Plot allowed dyons as points $(q_e, n_m)$ in a plane: at $\theta=0$ they sit on the integer grid; turning on θ **shears** the grid, sliding each monopole's electric charge by $\theta/2\pi\cdot n_m$. Nothing is created or destroyed — the lattice is relabeled — which is exactly why the physics is periodic in θ, once we track what "periodic" means.

## 3. θ-periodicity as spectral flow [Computed.]

Under $\theta \to \theta + 2\pi$, the Witten formula gives
$$
q_e = n_e + \frac{\theta+2\pi}{2\pi}n_m = (n_e + n_m) + \frac{\theta}{2\pi}n_m .
$$
The charge lattice maps to itself with the relabeling $n_e \to n_e + n_m$ (a monopole picks up one unit of electric charge). The spectrum is unchanged; only the labels flow. This **spectral flow** is the precise sense in which the theory is $2\pi$-periodic: not that the Lagrangian returns to itself term by term, but that the physical spectrum does, after a $\mathrm{SL}(2,\mathbb{Z})$ relabeling.

## 4. The lattice θ-term: where the naive version fails

Here the lattice teaches a lesson the continuum obscures. A naive lattice θ-term — say a plaquette-based discretization of $F\tilde F$ built from $\cos(da)$ — is **not** $2\pi$-periodic in θ and does not assign integer instanton number, because the naive lattice field strength is not a closed integer cochain. The fix is the **Villain/cochain** construction: with $F = da - 2\pi n$ and the integer 2-cochain $n$, the properly quantized instanton number is built from the cup product
$$
\frac{1}{8\pi^2}\int F\wedge F \ \longrightarrow\ \tfrac12\sum n \cup n \ + \cdots \in \mathbb{Z},
$$
using the higher-cup conventions of [[week-02-lattice-cell-complex-cochains|Week 2]] (and [[courses/generalized-symmetries-course/conventions]]). Only with the integer field $n$ is the θ-term $2\pi$-periodic and the Witten effect exact on the lattice.

> **Physical picture.** This is the first place in the course where "the naive lattice discretization is wrong and the Villain form is right" is not a convenience but a necessity. The θ-term is a piece of *topology* (an instanton number), and topology on the lattice lives in the **integer** cochains, not in the real-valued plaquette angles. Semester II Week 12 (the **modified Villain** construction) makes this systematic: promoting $n$ to a constrained ℤ gauge field gives an exactly $2\pi$-periodic θ-term, exact θ-dependence, and exact higher-form symmetries — sealing the crack we have just found.

## 5. Oblique confinement and SL(2,ℤ) [Sketched.]

The dyon charge lattice $(n_e, n_m)$ carries an action of $\mathrm{SL}(2,\mathbb{Z})$: the generator $S$ is electric–magnetic duality ($e \leftrightarrow m$), and $T$ is $\theta\to\theta+2\pi$ (the spectral flow of §3). Cardy and Rabinovici mapped the resulting phase diagram: besides the Coulomb, Higgs (electric condensate), and confining (magnetic condensate) phases, there are **oblique-confined** phases where a **dyon** $(n_e, n_m)$ with both charges nonzero condenses. Each oblique phase confines the charges not aligned with the condensed dyon — a whole $\mathrm{SL}(2,\mathbb{Z})$ orbit of confining phases, organized by θ.

This is the abelian model of the rich θ-dependence expected in Yang–Mills, and it is where Semester II's mixed anomaly at $\theta=\pi$ (the ℤ_N 1-form symmetry vs time reversal) lives: the two-fold degeneracy at $\theta=\pi$ is the oblique-confinement / spontaneous-CP structure, seen here abelian and explicit.

## 6. Axionic electrodynamics and topological matter

Promote θ to a field $\theta(x)$. The term $\frac{\theta(x)}{8\pi^2}F\wedge F$ is then physical wherever $\theta$ varies:
- A **domain wall** between $\theta = 0$ and $\theta = 2\pi$ (or $0$ and $\pi$) carries a **quantum Hall response**: a surface Hall conductivity $\sigma_{xy} = \frac{\Delta\theta}{2\pi}\frac{e^2}{2\pi}$. This is the **topological magnetoelectric effect** of a **topological insulator** (bulk $\theta=\pi$, $T$-invariant).
- A **linearly varying** $\theta(x) = 2(\mathbf{b}\cdot\mathbf{x} - b_0 t)$ encodes the separation of Weyl nodes in a **Weyl semimetal**, producing the anomalous Hall and chiral-magnetic responses. Integrating out the Weyl fermions generates exactly this **[[axionic-electrodynamics|axionic electrodynamics]]**.

This is the point of contact with the group's [[condensed-matter-connections|condensed-matter line]]: the monopole operators, θ-terms, and effective actions built here are the same objects that describe topological insulators and Weyl (super)conductors — and, via the [[julia-toulouse-mechanism|Julia–Toulouse mechanism]] of [[week-11-monopole-condensation-4d|Week 11]], the same rank-changing condensation language.

## 7. What to take away

1. **The θ-term acts on the charge lattice.** The **Witten effect** $q_e = n_e + \frac{\theta}{2\pi}n_m$ turns monopoles into dyons; θ shears the lattice.
2. **θ-periodicity is spectral flow.** Under $\theta\to\theta+2\pi$ the spectrum returns after relabeling $n_e\to n_e+n_m$ — an $\mathrm{SL}(2,\mathbb{Z})$ operation, not term-by-term invariance.
3. **The naive lattice θ-term fails; Villain repairs it.** A proper, $2\pi$-periodic θ-term needs the integer cochain $n$ and cup products — the crack sealed by modified Villain in Semester II.
4. **θ-electrodynamics is topological matter.** Domain-wall Hall responses, topological insulators, and Weyl semimetals are axion electrodynamics — the bridge to the group's condensed-matter work.

## 8. Looking ahead: Block D

Block C studied pure gauge theory and its defects. Block D adds **dynamical matter**: the Fradkin–Shenker model, the Higgs–confinement complementarity, and the question the classics leave open — which corners of the gauge–Higgs diagram are genuinely distinct phases, and distinguished by *what*, once no local order parameter is available. Semester II answers "symmetry realization," and the deconfined corner turns out to be the toric code. Week 13 begins.

## 9. Problem set

**Core problems** (everyone).

**1. The Witten effect.**
(a) Derive $q_e = n_e + \frac{\theta}{2\pi}n_m$ from the θ-modified Gauss law, tracking the surface term at the monopole.
(b) Show a unit monopole at $\theta=\pi$ is a dyon of electric charge $\tfrac12$, and discuss the CP properties of the $\theta=\pi$ spectrum.

**2. Spectral flow.**
Show that $\theta\to\theta+2\pi$ maps the dyon spectrum to itself via $n_e\to n_e+n_m$, and exhibit this as the $T$ generator of $\mathrm{SL}(2,\mathbb{Z})$ acting on $(n_e,n_m)$.

**3. The lattice θ-term.**
Explain why a $\cos(da)$-based lattice θ-term is not $2\pi$-periodic, and write the Villain/cup-product instanton number $\frac12\sum n\cup n$ that is. (Full modified-Villain treatment: Semester II Week 12.)

**Starred problems.**

**4⋆. Oblique confinement.**
Using the $(n_e,n_m)$ lattice and the $\mathrm{SL}(2,\mathbb{Z})$ action, sketch the Cardy–Rabinovici phase diagram as a function of θ and coupling. Identify the dyon that condenses in an oblique phase and which charges it confines. Relate the $\theta=\pi$ structure to spontaneous CP breaking.

**5⋆. Domain-wall Hall response.**
For a wall between $\theta=0$ and $\theta=\pi$, integrate the axion term across the wall and derive the surface Hall conductivity $\sigma_{xy} = \frac{e^2}{4\pi}$. Connect to the topological-insulator magnetoelectric effect.

**6⋆⋆ (optional).**
For a Weyl semimetal with node separation $\mathbf{b}$, take $\theta(x) = 2\mathbf{b}\cdot\mathbf{x}$ and derive the anomalous Hall conductivity and the chiral magnetic effect from the axion term. Comment on how the ℤ (integer) structure of the underlying monopole/Villain field appears in the quantization of these responses. (This is the calculation behind the group's Weyl-superconductor papers; see [[condensed-matter-connections]].)

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block C. Last revised 2026-07-01.*
