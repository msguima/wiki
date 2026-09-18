---
title: Pauli-Jordan Distribution
type: concept
areas: [bell-inequalities-qft]
aliases: [commutator function, Pauli-Jordan function, causal propagator]
modified: 2026-04-06
---

## Definition

For a free scalar field $\varphi(x)$ of mass $m$ in $(d+1)$-dimensional Minkowski spacetime, the **Pauli-Jordan distribution** (also called the commutator function or causal propagator) is

$$\Delta(x-y) = [\varphi(x),\, \varphi(y)]$$

as a distributional identity on test function space. In momentum space, for mass $m$:

$$\tilde{\Delta}(k) = -2\pi i\, \text{sgn}(k^0)\,\delta(k^2 + m^2),$$

and in position space (for $m=0$ in $d=3+1$):

$$\Delta(x-y) = \frac{1}{2\pi}\,\text{sgn}(x^0-y^0)\,\delta\bigl((x-y)^2\bigr).$$

The **defining properties** are:

1. **Antisymmetry**: $\Delta(x-y) = -\Delta(y-x)$.
2. **Lorentz invariance**: $\Delta(\Lambda x) = \Delta(x)$ for all Lorentz transformations $\Lambda$.
3. **Microcausality (support property)**: $\Delta(x-y) = 0$ whenever $x-y$ is spacelike, i.e., $(x-y)^2 > 0$ (using signature $(-,+,+,+)$). This is the mathematical expression of Einstein causality.
4. **Initial data**: $\Delta(0,\mathbf{x}) = 0$ and $\partial_0\Delta(0,\mathbf{x}) = \delta^{(d)}(\mathbf{x})$.

The relation to other propagators: $\Delta = \Delta_R - \Delta_A$ (retarded minus advanced propagator), and $\Delta(x-y) = -2\,\text{Im}\, G_F(x-y)$ where $G_F$ is the Feynman propagator (on the real axis; technically a distribution).

The **smeared version** used in the Weyl algebra is

$$\Delta(f,g) = \int\!\int f(x)\,\Delta(x-y)\,g(y)\,d^{d+1}x\,d^{d+1}y$$

for real test functions $f,g$. This is the symplectic form on the space of test functions, and it controls the phase in the [[weyl-operators|Weyl algebra]] relation:

$$W(f)\,W(g) = e^{-\frac{i}{2}\Delta(f,g)}\,W(f+g).$$

## Role in Research

The Pauli-Jordan distribution plays a foundational role in two aspects of the quantum information program:

1. **Weyl algebra construction.** The symplectic form $\Delta(f,g)$ is the structural datum of the canonical commutation relations. It determines when Weyl operators commute (spacelike supports), which is the algebraic expression of microcausality and underlies the causal structure of the bipartite Bell test.

2. **Localization of observables.** A Weyl operator $W(f)$ is localized in the spacetime region $\text{supp}(f)$. The support properties of $\Delta$ ensure that $W(f)$ commutes with $W(g)$ whenever $\text{supp}(f)$ is spacelike to $\text{supp}(g)$ — this is the content of Haag's local commutativity. Verifying that test functions have appropriate support (within a [[rindler-wedges|Rindler wedge]] or [[causal-diamonds|causal diamond]]) and computing $\Delta(f,g)$ are standard steps in the research program.

The choice of test functions $f$ (bumpified Haar wavelets, Gaussian profiles, etc.) directly affects both the value of $\Delta(f,g)$ and the resulting Bell correlators, making the explicit form of $\Delta$ a computational input to every paper in the Bell inequality program.

## Relations

- [[weyl-operators]] — the Weyl algebra relation $W(f)W(g) = e^{-\frac{i}{2}\Delta(f,g)}W(f+g)$ is controlled by the smeared Pauli-Jordan distribution; $\Delta(f,g)=0$ for spacelike-supported pairs implies microcausality
- [[bell-chsh-inequality]] — the construction of commuting (spacelike) observables for Alice and Bob relies on $\Delta(f,g) = 0$ for test functions supported in causally separated regions
- [[rindler-wedges]] — test functions localized in the right wedge $R$ give Weyl operators localized in $R$; the Pauli-Jordan distribution's vanishing on spacelike pairs underpins the independence of $\mathcal{M}(R)$ and $\mathcal{M}(L)$
- [[causal-diamonds]] — same localization argument applies to diamond regions

## Papers

See [[bell-inequalities-qft]] for full paper list.

## Notes

- The Pauli-Jordan distribution is a distribution, not a function — it requires smearing with test functions to give well-defined numbers. The Wightman axioms require test functions to be Schwartz class ($\mathscr{S}$) or compactly supported ($\mathcal{D}$).
- For the massive scalar field in $(3+1)$ dimensions, $\Delta(x-y)$ is supported on and inside the light cone (in contrast to the massless case where it is supported exactly on the light cone). This distinction affects whether correlations decay for large spacelike separations.
- Notation varies: some sources write $\Delta^{(1)}$ or $D$ for the commutator function. The notation $\Delta$ used here is standard in the algebraic QFT literature following Haag.
- The Pauli-Jordan distribution is not the same as the Hadamard two-point function $G^{(1)}(x,y) = \langle\varphi(x)\varphi(y)\rangle$, which is not antisymmetric and carries more information (state-dependent); $\Delta = 2i\,\text{Im}\,G^{(1)}$ by antisymmetry.
