---
title: BRST Symmetry
type: concept
areas: [gribov-zwanziger, bell-inequalities-qft]
aliases: [BRST, Becchi-Rouet-Stora-Tyutin symmetry, BRST invariance, nilpotent BRST]
modified: 2026-04-06
---

## Definition

**BRST symmetry** (Becchi-Rouet-Stora-Tyutin) is the global fermionic symmetry that emerges after gauge-fixing in a gauge theory. It replaces the original gauge invariance in the gauge-fixed action and encodes all physical content of the gauge theory.

Given a Yang-Mills theory with gauge field $A^a_\mu$, the Faddeev-Popov procedure introduces ghost fields $c^a$ (anticommuting, Grassmann), antighost fields $\bar{c}^a$, and a Nakanishi-Lautrup auxiliary field $b^a$. The **BRST transformation** $s$ acts as:

$$s A^a_\mu = -D^{ab}_\mu c^b = -(\partial_\mu c^a + g f^{abc} A^b_\mu c^c),$$
$$s c^a = \frac{g}{2}f^{abc}c^b c^c,$$
$$s \bar{c}^a = b^a, \quad s b^a = 0.$$

The key property is **nilpotency**: $s^2 = 0$ (acting on any field). This follows from the Jacobi identity for the structure constants $f^{abc}$.

Physical states are in the **BRST cohomology**: the kernel of $s$ modulo the image of $s$:

$$\mathcal{H}_{\text{phys}} = \ker s / \text{im}\, s.$$

Gauge invariance of physical observables translates to BRST invariance: $s\mathcal{O} = 0$ implies $\mathcal{O}$ is physical.

**Soft breaking of BRST in GZ theory**: the original GZ action is not strictly BRST-invariant because the horizon function $h(A)$ transforms non-trivially under $s$. The breaking is "soft" — it involves operators of dimension $\leq 4$ with coefficient $\gamma^2$ (the Gribov mass), so it vanishes perturbatively as $\gamma \to 0$.

**Exact nilpotent BRST in GZ** (Capri, Guimaraes et al., 2015): by introducing modified auxiliary fields, an exact nilpotent BRST symmetry $\tilde{s}$ with $\tilde{s}^2 = 0$ was constructed for the full GZ action in linear covariant gauges. This is the central theoretical result of the [[gribov-zwanziger]] program.

## Role in Research

BRST symmetry plays two distinct roles:

**1. In the Gribov-Zwanziger program.** The discovery of exact nilpotent BRST for the GZ action (Phys. Rev. D 92, 2015; **92 citations** — the most-cited paper in the portfolio) resolved the longstanding question of whether the Gribov restriction is physically consistent. Without an exact BRST symmetry, one could not define the physical state space via cohomology, and the entire framework would lack a proper gauge-theoretic basis. The result established that the restriction to the Gribov region is fully compatible with the BRST structure.

Follow-up papers:
- Complete local formulation (Phys. Rev. D 94, 2016; 63 citations).
- More on nonperturbative quantization (Phys. Rev. D 93, 2016; 49 citations).
- Nielsen identities and gauge-parameter independence within GZ (Phys. Rev. D 95, 2017; 47 citations).

**2. In the Bell inequality program.** The BRST-invariant Bell-CHSH paper (SciPost Phys. 15, 2023; 4 citations) was the first formulation of Bell-CHSH in gauge theories that respects BRST invariance. Since physical observables must be BRST-closed, the dichotomic operators entering the CHSH correlator must be constructed from BRST-invariant combinations of fields — a non-trivial requirement in gauge-fixed Yang-Mills theory.

## Relations

- [[gribov-copies]] — BRST consistency was the key concern raised by the Gribov restriction: does restricting the functional integral to $\Omega$ break gauge invariance (BRST) in an uncontrolled way? The answer is no, due to the exact BRST result
- [[gribov-horizon]] — the Gribov mass $\gamma$ appears in the soft BRST breaking term; the exact BRST construction modifies the field content to restore nilpotency
- [[refined-gribov-zwanziger]] — the exact BRST result applies to the full RGZ action with condensates; BRST invariance constrains which condensates are allowed
- [[confinement]] — BRST cohomology defines the physical spectrum; gluon confinement means the gluon field $A^a_\mu$ is not in the BRST cohomology (it is not gauge-invariant), consistent with its non-observation as an asymptotic state
- [[bell-chsh-inequality]] — in gauge theories, Bell observables must be BRST-invariant to be physical; this constrains the construction of dichotomic operators in QFT Bell tests
- [[spectral-positivity-violation]] — spectral positivity violation of the gluon propagator is consistent with BRST: the gluon is not a physical state (not in the BRST cohomology)

## Papers

See [[gribov-zwanziger]] and [[bell-inequalities-qft]] for full paper lists.

## Notes

- The acronym BRST comes from the four independent discoverers: Becchi, Rouet, Stora (1974-75) and Tyutin (1975, published later). In the West the paper is cited as BRS; in the East as T. The combined BRST attribution is now universal.
- Nilpotency $s^2 = 0$ makes BRST a cohomological structure: physical observables are cohomology classes. This is analogous to de Rham cohomology in differential geometry.
- Common confusion: "soft BRST breaking" in GZ does not mean the theory is inconsistent. It means the breaking is controlled by a mass parameter $\gamma$ and can in principle be treated as a deformation of the BRST-exact theory. The exact BRST result shows one can do better: the breaking is entirely an artifact of not using the right field variables.
- In the BRST-invariant Bell-CHSH context (SciPost 2023), the Proca field (massive vector field) plays a special role: it can be mapped to a scalar theory by gauge-invariant projection, allowing extension of the free scalar Bell results to the vector case.
