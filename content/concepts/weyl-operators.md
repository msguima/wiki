---
title: Weyl Operators
type: concept
areas: [bell-inequalities-qft, relative-entropy-qft]
aliases: [Weyl unitaries, displacement operators]
modified: 2026-04-06
---

## Definition

Given a smeared field operator $\varphi(f) = \int d^dx\, f(x)\,\varphi(x)$ with $f$ a real-valued test function (smooth, compactly supported), the Weyl operator is the unitary

$$W(f) = e^{i\varphi(f)}.$$

Weyl operators satisfy the **Weyl algebra relations**:

$$W(f)\,W(g) = e^{-\frac{i}{2}\Delta(f,g)}\,W(f+g),$$

where $\Delta(f,g) = \int\!\int f(x)\,\Delta(x-y)\,g(y)\,d^dx\,d^dy$ is the smeared [[pauli-jordan-distribution|Pauli-Jordan distribution]]. The phase factor encodes the canonical commutation relations and encapsulates the causal structure: if $\text{supp}(f)$ and $\text{supp}(g)$ are spacelike separated, then $\Delta(f,g) = 0$ and the operators commute.

For the free scalar field vacuum, the expectation value takes the Gaussian form

$$\langle 0| W(f) |0\rangle = e^{-\frac{1}{2}\|f\|^2_+},$$

where $\|\cdot\|_+$ is the one-particle norm. This closed-form result makes Weyl operators particularly tractable for explicit computation.

Weyl operators generate the local von Neumann algebra $\mathcal{M}(\mathcal{O})$ associated to any open spacetime region $\mathcal{O}$ when $f$ ranges over test functions with $\text{supp}(f) \subset \mathcal{O}$.

## Role in Research

Weyl operators are the central technical tool in the quantum information program. They serve two primary roles:

1. **Dichotomic observables for Bell tests.** For Bell-CHSH experiments one needs bounded, self-adjoint operators with spectrum in $[-1,1]$. The operators $W(f) + W(f)^\dagger$ and $i(W(f) - W(f)^\dagger)$ (or more generally, real parts of shifted Weyl operators) serve as the "spin" observables for Alice and Bob. The 2023 Phys. Rev. D 108, 085026 paper (15 citations) developed the systematic framework using Weyl operators localized in [[rindler-wedges|Rindler wedges]], with Bob's operators obtained via [[tomita-takesaki-modular-theory|modular conjugation]] $J$ acting on Alice's algebra.

2. **State preparation.** [[coherent-states|Coherent states]], [[squeezed-states|squeezed states]], and [[cat-states|cat states]] are all defined through the action of Weyl operators (or products thereof) on the vacuum. The Araki-Uhlmann relative entropy between these excited states and the vacuum is computable in closed form using the Gaussian structure.

The bumpified Haar wavelet test functions used to achieve the Tsirelson bound for massless spinors (Phys. Rev. D 108, L081701) are specific choices of $f$ with compact support localized to one Rindler wedge, designed to be smooth while having sharp spatial concentration.

## Relations

- [[pauli-jordan-distribution]] — the Weyl algebra phase factor $\Delta(f,g)$ is the smeared Pauli-Jordan distribution; spacelike commutativity of Weyl operators follows from its support properties
- [[tomita-takesaki-modular-theory]] — modular conjugation $J$ maps $W(f)$ in Alice's algebra to Bob's corresponding operator; $\Delta^{it} W(f) \Delta^{-it}$ generates the modular flow
- [[bell-chsh-inequality]] — Weyl operators are the explicit dichotomic observables used to construct CHSH correlators in QFT
- [[araki-uhlmann-relative-entropy]] — relative entropy between coherent/squeezed states and the vacuum is computed via the Gaussian structure of Weyl operator expectation values
- [[type-iii-von-neumann-algebras]] — Weyl operators generate type III₁ algebras for local regions; there are no pure states in these algebras
- [[coherent-states]] — coherent states are eigenstates of annihilation operators, equivalently $W(f)|0\rangle$ for purely positive-frequency $f$
- [[rindler-wedges]] — Weyl operators with $\text{supp}(f)$ in the right Rindler wedge generate the algebra $\mathcal{M}(R)$

## Papers

See [[bell-inequalities-qft]] and [[relative-entropy-qft]] for full paper lists.

## Notes

- The Weyl algebra is a $C^*$-algebra; passing to von Neumann algebras requires taking weak closures in a specific representation (the vacuum GNS representation).
- In gauge theories one must work with gauge-invariant combinations of Weyl operators, which introduces additional complications. The BRST-invariant Bell-CHSH paper (SciPost Phys. 15, 2023) addresses this.
- The phase $\Delta(f,g)/2$ in the Weyl relation is purely imaginary for real $f,g$, preserving unitarity. This is the QFT incarnation of the Heisenberg commutation relation $[x,p] = i$.
- Distinct from the Weyl operators of representation theory (group-theoretic Weyl operators for finite groups); the QFT usage refers specifically to the exponentiated field operators.
