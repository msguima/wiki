---
title: Cat States
type: concept
areas: [bell-inequalities-qft]
aliases: [Schrödinger cat state, cat state, optical cat state]
modified: 2026-04-06
---

## Definition

A **cat state** (or Schrödinger cat state) is a superposition of two macroscopically distinct [[coherent-states|coherent states]]:

$$|\text{cat}_\pm\rangle \propto |\alpha\rangle \pm |-\alpha\rangle, \quad \alpha \in \mathbb{C},$$

with normalization $\mathcal{N}_\pm = \sqrt{2(1 \pm e^{-2|\alpha|^2})}$. The name refers to Schrödinger's thought experiment: for $|\alpha| \gg 1$ the states $|\alpha\rangle$ and $|-\alpha\rangle$ are nearly orthogonal ($|\langle\alpha|-\alpha\rangle| = e^{-2|\alpha|^2} \approx 0$) and represent macroscopically distinguishable field amplitudes — "dead" and "alive" superposed.

In the **Wigner function representation**, cat states have oscillatory interference fringes between the two coherent-state peaks — a hallmark of quantum superposition with no classical analogue.

The expectation value of a [[weyl-operators|Weyl operator]] $W(g)$ in the cat state $|\text{cat}_+\rangle$ is

$$\langle\text{cat}_+|W(g)|\text{cat}_+\rangle = \frac{e^{-\frac{1}{2}\|g\|^2}\bigl(\cosh(\text{Re}\langle 2\alpha, g\rangle_+) + \cos(\text{Im}\langle 2\alpha, g\rangle_+)\bigr)}{1 + e^{-2|\alpha|^2}},$$

where the interference between $\langle\alpha|W(g)|-\alpha\rangle$ cross terms produces oscillatory contributions absent in the incoherent mixture $\frac{1}{2}(|\alpha\rangle\langle\alpha| + |-\alpha\rangle\langle-\alpha|)$.

In QFT, the cat state is constructed as $W(f)|0\rangle + W(-f)|0\rangle$ for a test function $f$ with compact support, providing a well-localized field excitation.

## Role in Research

Cat states are the focus of the 2026 paper Phys. Rev. D 113, 065008, which computes [[bell-chsh-inequality|Bell-CHSH violations]] for cat states in QFT vacuum. The key findings:

1. **Interference-driven Bell violation.** The CHSH correlator for cat states includes interference cross-terms proportional to $\cos(\text{Im}\langle 2\alpha, g\rangle_+)$ that are absent for the incoherent mixture. These terms can either enhance or suppress Bell violation depending on the test function choice.

2. **New qualitative features.** Unlike [[coherent-states|coherent states]] (for which the CHSH correlator depends only on $\|g\|$ and $\|f\|$), cat state Bell correlators depend on the phase structure of $\langle f, g\rangle_+$, introducing new parameter space and optimization opportunities.

3. **Large-$|\alpha|$ limit.** For large amplitude $|\alpha| \gg 1$, the cat state approaches a superposition of macroscopically distinct field configurations. Bell violation in this regime tests quantum superposition of classically distinguishable states — connecting quantum information to the measurement problem.

4. **Connection to quantum interference.** The enhancement of Bell violation by quantum interference (compared to the incoherent mixture) is a concrete quantitative demonstration that quantum coherence — not merely entanglement — plays a role in Bell inequality violations in QFT.

## Relations

- [[coherent-states]] — cat states are superpositions of coherent states $|\alpha\rangle \pm |-\alpha\rangle$; Bell correlators for cat states contain the coherent-state correlators plus interference cross-terms
- [[weyl-operators]] — cat state expectation values of Weyl operators are computable in closed form as sums of Gaussian terms with interference; the Weyl algebra structure is essential
- [[bell-chsh-inequality]] — the 2026 paper explicitly computes the CHSH correlator for cat states, finding qualitatively new features from interference
- [[squeezed-states]] — complementary family of non-classical states; together with cat states they explore the space of non-Gaussian vs Gaussian-but-squeezed excitations
- [[araki-uhlmann-relative-entropy]] — relative entropy $S(\omega_{\text{cat}}\|\omega_0)$ can be computed for cat states; involves both the coherent-state contribution and interference corrections
- [[type-iii-von-neumann-algebras]] — in the type III₁ local algebra context, cat states (as global Fock-space states) restrict to mixed states when localized; their Bell properties are computed using the algebraic machinery

## Papers

See [[bell-inequalities-qft]] for full paper list. The primary cat state paper is Phys. Rev. D 113, 065008 (2026).

## Notes

- The normalization factor $e^{-2|\alpha|^2}$ in the denominator matters for small $|\alpha|$; for large $|\alpha|$ the even and odd cat states $|\text{cat}_\pm\rangle$ become equally normalized and nearly orthogonal.
- Cat states are experimentally realized in microwave cavity QED, superconducting qubits, and (approximately) in optical systems. They are highly sensitive to decoherence: even a single photon loss destroys the coherence between $|\alpha\rangle$ and $|-\alpha\rangle$.
- Common confusion: "cat state" in quantum information can sometimes refer to GHZ-type states (multi-qubit analogs). In the QFT context here, it specifically means $|\alpha\rangle \pm |-\alpha\rangle$ in terms of field coherent states.
- The Wigner function of a cat state is non-positive (it has regions where the quasi-probability distribution is negative), confirming its non-classical nature — in contrast to coherent and squeezed states whose Wigner functions are non-negative Gaussians.
