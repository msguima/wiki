---
title: Gribov Horizon
type: concept
areas: [gribov-zwanziger]
aliases: [Gribov region, first Gribov region, horizon boundary]
modified: 2026-04-06
---

## Definition

The **Gribov region** $\Omega$ is the set of gauge field configurations in Landau gauge ($\partial^\mu A^a_\mu = 0$) for which the **Faddeev-Popov operator**

$$M^{ab} = -\partial^\mu D^{ab}_\mu = -\partial^\mu(\partial_\mu\delta^{ab} + g f^{abc}A^c_\mu)$$

is **strictly positive definite**:

$$\Omega = \{A : \partial^\mu A^a_\mu = 0,\; M^{ab} > 0\}.$$

The **Gribov horizon** $\partial\Omega$ is the boundary of this region:

$$\partial\Omega = \{A : \partial^\mu A^a_\mu = 0,\; \text{first zero eigenvalue of }M^{ab}\text{ appears}\}.$$

**Zwanziger's theorem**: in the thermodynamic limit (infinite volume), the path integral is dominated by configurations that lie on or near the Gribov horizon $\partial\Omega$. This means the deep infrared physics of Yang-Mills theory is controlled by the boundary of the Gribov region.

The restriction of the functional integral to $\Omega$ is implemented by adding **Zwanziger's horizon function** to the Yang-Mills action:

$$h(A) = g^2 \int d^dx\, f^{abc} A^b_\mu\,(M^{-1})^{ad}\,f^{dec} A^e_\mu.$$

The horizon condition $\langle h(A)\rangle = d(N^2-1)$ (for gauge group $SU(N)$ in $d$ dimensions) self-consistently enforces the restriction. This condition determines the **Gribov mass parameter** $\gamma$ (the horizon parameter), which appears in the gluon propagator.

The resulting **GZ gluon propagator** in Landau gauge takes the infrared-suppressed form:

$$G^{ab}_{\mu\nu}(p) = \delta^{ab}\left(\delta_{\mu\nu} - \frac{p_\mu p_\nu}{p^2}\right)\frac{p^2}{p^4 + \gamma^4},$$

which is suppressed at $p \to 0$ (the Gribov mass $\gamma$ provides an effective infrared regulator) and exhibits [[spectral-positivity-violation|spectral positivity violation]] — a signal of gluon confinement.

## Role in Research

The Gribov horizon is the central object of the [[gribov-zwanziger]] research program. The restriction to $\Omega$ produces all the distinctive infrared features of the GZ framework:

- **Modified gluon propagator**: suppressed at $p=0$, violates Källén-Lehmann positivity.
- **Enhanced ghost propagator**: the ghost propagator is infrared-enhanced (more singular than the free propagator), consistent with the Gribov no-pole condition.
- **Kugo-Ojima confinement criterion**: the ghost enhancement is connected to the Kugo-Ojima criterion for confinement.

The all-order equivalence of the no-pole condition and the horizon condition (Phys. Lett. B 719, 2013; 43 citations) is one of the landmark results: Gribov's original 1978 approach (no-pole condition for the ghost) and Zwanziger's functional integral approach (horizon function) were shown to give the same physics to all orders in perturbation theory.

The open question of whether the Gribov horizon modifies **Bell-CHSH violations** in the non-abelian vacuum — whether the entanglement structure of the QCD vacuum is affected by the Gribov restriction — is a key open problem bridging [[gribov-zwanziger]] and [[bell-inequalities-qft]].

## Relations

- [[gribov-copies]] — the Gribov horizon bounds the region where the Faddeev-Popov operator is positive; copies with $M$ having zero eigenvalues lie on the horizon, and copies with negative eigenvalues lie outside $\Omega$
- [[refined-gribov-zwanziger]] — the RGZ theory incorporates dimension-two condensates on top of the GZ restriction to $\Omega$; the horizon condition is preserved in RGZ
- [[brst-symmetry]] — the discovery of exact BRST symmetry within the GZ framework (Phys. Rev. D 92, 2015; 92 citations) confirmed that the Gribov horizon restriction is physically consistent
- [[confinement]] — the modified gluon propagator due to the Gribov horizon restriction provides a propagator-level signal of gluon confinement through spectral positivity violation
- [[spectral-positivity-violation]] — the GZ gluon propagator does not admit a positive Källén-Lehmann spectral representation; this is a direct consequence of the horizon restriction
- [[bell-chsh-inequality]] — open question: whether the Gribov horizon modifies vacuum entanglement and Bell-CHSH violations in non-abelian gauge theories

## Papers

See [[gribov-zwanziger]] for full paper list.

## Notes

- The first Gribov region $\Omega$ is **convex** and still contains Gribov copies (multiple gauge-equivalent configurations satisfying $\partial A = 0$ can both lie in $\Omega$). The fundamental modular region $\Lambda \subset \Omega$ is the true gauge-fixing domain, but it is non-convex and computationally inaccessible.
- "Horizon" in the GZ sense is an analogy with the event horizon in general relativity: configurations near $\partial\Omega$ have infrared-divergent contributions that dominate the path integral, much as physics near a black hole horizon dominates certain observables.
- The Gribov mass $\gamma$ is not a free parameter — it is fixed self-consistently by the horizon condition. This self-consistency is what makes the GZ framework predictive rather than phenomenological.
- The phrase "no-pole condition" refers to Gribov's original requirement that the ghost propagator $\langle c^a c^b\rangle^{-1}(p) = M^{ab}(p)$ in Landau gauge have no poles at finite real $p^2 > 0$, which geometrically corresponds to $M > 0$ everywhere in field space — exactly the condition defining $\Omega$.
