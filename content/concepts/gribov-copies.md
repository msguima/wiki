---
title: Gribov Copies
type: concept
areas: [gribov-zwanziger]
aliases: [Gribov ambiguity, gauge copies, Gribov problem]
modified: 2026-04-06
---

## Definition

In a non-abelian gauge theory (e.g., Yang-Mills with gauge group $G = SU(N)$), two gauge field configurations $A_\mu^a$ and $A_\mu^{\prime\, a}$ are **Gribov copies** if:

1. They are related by a gauge transformation: $A^{\prime\,a}_\mu = A^g_\mu \equiv g^{-1}(\partial_\mu + A_\mu)g$ for some $g: \mathbb{R}^d \to G$.
2. Both satisfy the same gauge-fixing condition, e.g., Landau gauge $\partial^\mu A^a_\mu = 0$.

The existence of Gribov copies means the gauge-fixing condition does not uniquely pick one representative from each gauge orbit — the Faddeev-Popov procedure **over-counts** field configurations in the path integral. This was discovered by Gribov in 1978, who showed it occurs inevitably for non-abelian groups in Landau and Coulomb gauges.

Quantitatively, a Gribov copy $A'$ of a configuration $A$ satisfying $\partial^\mu A_\mu = 0$ satisfies:

$$\partial^\mu A^{\prime\,a}_\mu = 0 \quad \text{with} \quad A' = A + D_\mu^{ab}(A)\,\epsilon^b + O(\epsilon^2)$$

for some infinitesimal gauge parameter $\epsilon^a$. The condition $\partial^\mu D_\mu^{ab}(A)\,\epsilon^b = 0$ shows that copies are associated with **zero modes** of the Faddeev-Popov operator $M^{ab} = -\partial^\mu D^{ab}_\mu$.

The **Faddeev-Popov determinant** $\det M$ changes sign across the **Gribov horizon** $\partial\Omega$ (where $\det M = 0$), invalidating the perturbative expansion that assumes $\det M > 0$.

## Role in Research

Gribov copies are the central problem of the [[gribov-zwanziger]] research program, which dominated the research portfolio from 2011 to 2022. Their resolution via restriction to the **Gribov region** $\Omega$ is the foundation of the entire Gribov-Zwanziger (GZ) and [[refined-gribov-zwanziger|Refined Gribov-Zwanziger (RGZ)]] framework.

Key results depending on the Gribov copy analysis:

- **No-pole condition** (Gribov's original approach): requiring the ghost propagator to have no unphysical poles forces the path integral to remain within $\Omega$.
- **All-order equivalence of no-pole and horizon conditions** (Phys. Lett. B 719, 2013; 43 citations): proved that Gribov's no-pole condition and Zwanziger's horizon function approach are equivalent to all perturbative orders.
- **BRST consistency**: the discovery of an exact nilpotent [[brst-symmetry|BRST symmetry]] for the GZ action (Phys. Rev. D 92, 2015; 92 citations) showed that the restriction to $\Omega$ is physically consistent — Gribov copies, being gauge artifacts, do not contribute to physical observables when BRST symmetry is preserved.

An open question (listed in [[gribov-zwanziger]]) is the extent to which Gribov copies affect **gauge-invariant, physical observables**. While gauge-dependent quantities (propagators, vertices) are modified by the restriction, the physical spectrum should be copy-independent.

## Relations

- [[gribov-horizon]] — the boundary $\partial\Omega$ where the Faddeev-Popov operator $M$ first develops zero eigenvalues; copies are most problematic near this boundary
- [[refined-gribov-zwanziger]] — the RGZ theory is built on the Gribov copy resolution plus dimension-two condensates; Gribov copies motivate the entire RGZ framework
- [[brst-symmetry]] — BRST invariance is the key consistency check for the Gribov copy restriction; the discovery of exact BRST in GZ (Phys. Rev. D 92, 2015) resolved the long-standing concern that restricting the path integral breaks gauge invariance in an uncontrolled way
- [[confinement]] — the Gribov copy problem is intimately linked to confinement: the modified propagators in the restricted path integral exhibit [[spectral-positivity-violation|spectral positivity violation]], signaling gluon confinement
- [[spectral-positivity-violation]] — direct consequence of the Gribov restriction on the gluon propagator

## Papers

See [[gribov-zwanziger]] for full paper list.

## Notes

- Gribov copies exist in **all** non-abelian gauge theories in Landau gauge and Coulomb gauge; they are absent only in abelian (e.g., QED) theories where the gauge group is $U(1)$.
- The first Gribov region $\Omega$ (where $M > 0$) still contains Gribov copies — complete gauge fixation would require restricting to the **fundamental modular region** $\Lambda \subset \Omega$, the true global minimum of $\|A\|^2$ on each gauge orbit. The GZ approach uses $\Omega$ (more tractable) rather than $\Lambda$.
- Common confusion: "Gribov copies" is sometimes used loosely to mean any gauge ambiguity. Precisely, they are gauge-equivalent configurations that both satisfy the gauge-fixing condition — not just any two gauge-related configurations.
- The lattice gauge theory community has extensively studied Gribov copies numerically; the effect of different copy-selection algorithms on the gluon and ghost propagators is well-documented and provides non-perturbative evidence for the GZ picture.
