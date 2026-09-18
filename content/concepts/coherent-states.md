---
title: Coherent States
type: concept
areas: [bell-inequalities-qft, relative-entropy-qft]
aliases: [coherent state, Glauber coherent state, displacement state]
modified: 2026-04-06
---

## Definition

In quantum optics and QFT, a **coherent state** is an eigenstate of the annihilation operator:

$$a\,|\alpha\rangle = \alpha\,|\alpha\rangle, \quad \alpha \in \mathbb{C}.$$

Coherent states are the **minimum-uncertainty states**: they saturate the Heisenberg uncertainty relation $\Delta x\,\Delta p = \hbar/2$ with equal uncertainties in both quadratures (unlike [[squeezed-states|squeezed states]]).

In the **Weyl operator language**, the coherent state is the displaced vacuum:

$$|\alpha\rangle = W(\alpha)|0\rangle = D(\alpha)|0\rangle,$$

where $D(\alpha) = \exp(\alpha a^\dagger - \alpha^* a)$ is the displacement operator. In QFT with a smeared field, the coherent state associated with test function $f$ is

$$|\psi_f\rangle = W(f)|0\rangle,$$

corresponding to a classical field configuration $\langle\varphi(x)\rangle_f = \langle\psi_f|\varphi(x)|\psi_f\rangle \neq 0$.

The **expectation value of Weyl operators** in coherent states is:

$$\langle\psi_f|W(g)|\psi_f\rangle = e^{i\,\text{Re}\langle f,g\rangle_+}\,e^{-\frac{1}{2}\|g\|^2_+},$$

where $\langle f,g\rangle_+$ is the positive-frequency inner product. This Gaussian form makes all correlators exactly computable.

The **[[araki-uhlmann-relative-entropy|Araki-Uhlmann relative entropy]]** between a coherent state $\omega_f$ and the vacuum $\omega_0$ is

$$S(\omega_f\|\omega_0) = \|f\|^2_+,$$

the one-particle norm squared of the displacement function $f$.

## Role in Research

Coherent states appear in the quantum information program as the simplest excited states for which Bell-CHSH violations and relative entropy can be computed explicitly. They form a baseline against which [[squeezed-states|squeezed]] and [[cat-states|cat states]] are compared.

Key computations:

- **Bell-CHSH violation for coherent states**: The CHSH correlator is computed explicitly using the Gaussian expectation value formula. Coherent states produce Bell violations that depend on the displacement $f$ and the test functions used for the Weyl operators.

- **Relative entropy**: The formula $S(\omega_f\|\omega_0) = \|f\|^2_+$ gives a simple geometric interpretation: relative entropy is the squared distance in one-particle Hilbert space between the coherent displacement and the vacuum.

- **Comparison class for cat states**: The 2026 paper (Phys. Rev. D 113, 065008) computes Bell violations for [[cat-states|cat states]] $|\alpha\rangle + |-\alpha\rangle$, using coherent states as the building blocks and highlighting how quantum interference modifies the Bell correlator relative to the incoherent mixture of $|\alpha\rangle$ and $|-\alpha\rangle$ separately.

## Relations

- [[weyl-operators]] — coherent states are defined by $W(f)|0\rangle$; the Weyl algebra structure makes all expectation values exactly computable via Gaussian integrals
- [[araki-uhlmann-relative-entropy]] — $S(\omega_f\|\omega_0) = \|f\|^2_+$ is the prototype computable relative entropy, serving as the baseline for more complex states
- [[squeezed-states]] — squeezed states reduce uncertainty in one quadrature; they are Bogoliubov transformations of the vacuum rather than displacements; relative entropy involves Bogoliubov coefficients
- [[cat-states]] — cat states are superpositions of coherent states $|\alpha\rangle + |-\alpha\rangle$; their Bell violations and relative entropy differ from those of individual coherent states due to interference
- [[bell-chsh-inequality]] — explicit CHSH correlators for coherent states are computed in the quantum information program, providing benchmarks for optimization
- [[type-iii-von-neumann-algebras]] — even coherent states are mixed when restricted to local algebras; the type III₁ structure means there are no pure normal local states

## Papers

See [[bell-inequalities-qft]] and [[relative-entropy-qft]] for full paper lists.

## Notes

- Coherent states form an **overcomplete** basis: $\frac{1}{\pi}\int |\alpha\rangle\langle\alpha|\,d^2\alpha = \mathbf{1}$. This overcomplete resolution of identity (with the phase space measure $d^2\alpha$) is the basis of the Glauber-Sudarshan P-representation.
- Coherent states are not orthogonal: $|\langle\alpha|\beta\rangle|^2 = e^{-|\alpha-\beta|^2}$. This overlap is what makes [[cat-states|cat states]] ($|\alpha\rangle \pm |-\alpha\rangle$) physically interesting — for large $|\alpha|$ the two components are nearly orthogonal, approximating a genuine superposition of macroscopically distinct states.
- In QFT, the coherent state $W(f)|0\rangle$ is a Fock-space state only when $f$ has finite one-particle norm. For general $f$ (e.g., in the thermodynamic limit), it may be a unitarily inequivalent representation — an important subtlety for infinite-volume QFT.
