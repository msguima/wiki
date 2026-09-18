---
title: Araki-Uhlmann Relative Entropy
type: concept
areas: [relative-entropy-qft, bell-inequalities-qft]
aliases: [relative entropy, modular relative entropy, Araki relative entropy]
modified: 2026-04-06
---

## Definition

Let $\mathcal{M}$ be a von Neumann algebra with cyclic and separating vectors $\Omega$ and $\Phi$ representing states $\omega(a) = \langle\Omega, a\,\Omega\rangle$ and $\varphi(a) = \langle\Phi, a\,\Phi\rangle$. The **relative modular operator** $\Delta_{\Phi,\Omega}$ is defined through the polar decomposition of the antilinear operator

$$S_{\Phi,\Omega}:\; a\Omega \mapsto a^*\Phi, \quad a \in \mathcal{M}.$$

The **Araki-Uhlmann relative entropy** of $\omega$ with respect to $\varphi$ is

$$S(\omega\|\varphi) = -\langle\Omega,\, \log\Delta_{\Phi,\Omega}\,\Omega\rangle.$$

When $\mathcal{M} = B(\mathcal{H})$ and the states are given by density matrices $\rho, \sigma$, this reduces to the von Neumann relative entropy $S(\rho\|\sigma) = \text{tr}(\rho\log\rho - \rho\log\sigma)$.

Key properties:

- **Non-negativity**: $S(\omega\|\varphi) \geq 0$, with equality iff $\omega = \varphi$.
- **Monotonicity (data processing)**: For any unital completely positive map $\Phi: \mathcal{M} \to \mathcal{N}$, one has $S(\omega\circ\Phi \| \varphi\circ\Phi) \leq S(\omega\|\varphi)$.
- **Lower semi-continuity** in both arguments in the weak-* topology.
- **Divergence for singular states**: $S(\omega\|\varphi) = +\infty$ if $\omega$ is not absolutely continuous with respect to $\varphi$.

For coherent states $\omega_f$ (corresponding to displacement by $f$) relative to the vacuum $\omega_0$, one obtains the explicit formula

$$S(\omega_f\|\omega_0) = \|f\|^2_+,$$

where $\|f\|_+$ is the one-particle norm (the norm in the positive-frequency subspace). This Gaussian result is the computational workhorse in Marcelo's relative entropy program.

## Role in Research

The [[relative-entropy-qft]] research line (launched 2025) applies Araki-Uhlmann relative entropy to study information-theoretic properties of the QFT vacuum and excited states. Relative entropy is the only well-defined entropy-like quantity for [[type-iii-von-neumann-algebras|type III₁ algebras]], making it the appropriate measure where von Neumann entropy $-\text{tr}(\rho\log\rho)$ is undefined (infinite or ill-defined due to the absence of a trace).

Concrete results include:

- Closed-form relative entropy between coherent/squeezed/cat states and the vacuum for free scalar and Proca fields.
- Computation of the relative entropy between states localized in one [[rindler-wedges|Rindler wedge]] and the Minkowski vacuum, recovering and generalizing known results on the Unruh effect in the algebraic framework.
- Connection to [[bell-chsh-inequality|Bell-CHSH violations]]: the relative entropy quantifies the "distance" from the vacuum, and Bell violation is maximal near the vacuum (small relative entropy regime).
- Relevance to [[entanglement-embezzlement|entanglement embezzlement]]: the cost of extracting entanglement is bounded below by relative entropy quantities.

## Relations

- [[tomita-takesaki-modular-theory]] — the relative modular operator $\Delta_{\Phi,\Omega}$ is the central object; Araki-Uhlmann relative entropy is defined entirely within the Tomita-Takesaki framework
- [[type-iii-von-neumann-algebras]] — relative entropy is well-defined for type III algebras even though von Neumann entropy is not; this is the key reason for using it in AQFT
- [[weyl-operators]] — Gaussian structure of Weyl operator expectation values enables closed-form computation of relative entropy for coherent/squeezed states
- [[entanglement-embezzlement]] — relative entropy provides a lower bound on the cost of embezzlement protocols; in type III₁ algebras the bound can be zero (exact embezzlement)
- [[coherent-states]] — the simplest case: $S(\omega_f\|\omega_0) = \|f\|^2_+$ with explicit one-particle norm
- [[squeezed-states]] — relative entropy for squeezed states involves the Bogoliubov coefficients, computable in closed form
- [[rindler-wedges]] — relative entropy of the restriction of the Minkowski vacuum to one wedge provides an algebraic route to the Unruh entropy

## Papers

See [[relative-entropy-qft]] and [[bell-inequalities-qft]] for full paper lists.

## Notes

- Araki defined this quantity in 1976 for general von Neumann algebras; Uhlmann extended it further. "Araki-Uhlmann" is the standard attribution in the AQFT literature.
- Common confusion: the relative entropy $S(\omega\|\varphi)$ is asymmetric; $S(\omega\|\varphi) \neq S(\varphi\|\omega)$ in general. It is not a distance, but a divergence.
- The formula $S(\omega\|\varphi) = -\langle\Omega,\log\Delta_{\Phi,\Omega}\Omega\rangle$ is formally analogous to $\text{tr}(\rho\log\rho - \rho\log\sigma)$ but requires no trace — which is precisely why it works for type III algebras.
- For states on the same algebra with $\varphi$ invariant under the modular flow of $\omega$, Petz's theorem characterizes when equality holds in data processing: equality iff the states are "sufficient" for the subalgebra.
- **Connection to gravitational entropy** ([[2025-liu-lectures-entanglement-vna]]): Liu's review establishes that the Araki-Uhlmann relative entropy on a type III$_1$ algebra is related, via the [[crossed-product-construction|crossed product construction]], to a well-defined von Neumann entropy on the resulting type II$_\infty$ algebra. In the holographic context, this von Neumann entropy is the generalized gravitational entropy (Bekenstein-Hawking area term + bulk entanglement). This provides a gravitational interpretation of the same quantity computed in Marcelo's flat-space QFT program: the relative entropy between excited states and the vacuum is, algebraically, the same object that yields gravitational entropy when the algebra is "dressed" by the crossed product. The relationship goes through the modular Hamiltonian: $S(\omega\|\varphi)$ involves $\log\Delta_{\Phi,\Omega}$, and the crossed product uses the modular flow $\sigma_s$ generated by $\Delta$ to construct the type II$_\infty$ algebra on which entropy is defined via a trace.
