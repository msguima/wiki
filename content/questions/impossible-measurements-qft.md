---
title: What are the limitations of ideal measurements in relativistic QFT?
type: question
status: open
areas:
  - bell-inequalities-qft
priority: medium
originated: 2026-04-06
---

## Statement

In quantum mechanics, ideal (projective) measurements are idealized operations that instantaneously collapse the wavefunction onto an eigenstate of the measured observable. In relativistic QFT, such instantaneous operations are problematic: they can signal superluminally, violate causality, or be inconsistent with the [[haag-kastler-axioms]]. Which observables in QFT admit ideal measurements, which admit approximate measurements, and which are fundamentally impossible to measure? What are the implications for the Bell-CHSH program, where the "Alice" and "Bob" operations are modeled as measurements of [[weyl-operators]]?

## Why It Matters

The Bell-CHSH inequality tests in QFT are typically formulated as thought experiments: Alice and Bob each measure a dichotomic observable localized in their respective spacetime regions, and the correlations of their outcomes are compared with the classical bound of 2. But what does it mean to "measure" a Weyl operator $W(f) = \exp(i\phi(f))$ in relativistic QFT? The field operator $\phi(f)$ is an unbounded operator, and $W(f)$ is bounded and unitary, but performing a projective measurement of $W(f)$ in real time requires a physical interaction between the field and an apparatus that:
1. Does not disturb the field outside the localization region of $f$.
2. Does not create superluminal signals.
3. Produces a definite, reproducible outcome.

The Sorkin-Bostelmann-Fewster arguments show that certain idealized field measurements are impossible — they would violate causality. The Unruh-DeWitt detector model provides an operational, causal alternative to ideal measurement. Understanding which measurements are possible shapes the experimental interpretation of Bell-CHSH violations in QFT: if Alice's measurement is not operationally realizable, the violation is a formal fact about correlators, not a testable prediction.

This question has implications for:
- The physical interpretation of all Bell-inequality violations computed in the program.
- The design of realistic detector models (e.g., [[unruh-dewitt-detectors]]) that approximate ideal measurements.
- The relationship between entanglement measures (which may require ideal measurements) and physical observables.

## What We Know

**The Sorkin no-go theorem (1993):**
- Sorkin showed that ideal projective measurements of local observables in QFT can lead to superluminal signaling: if Alice performs an ideal measurement of a local observable $O_A$ in region $\mathcal{R}_A$, then a measurement by Bob in a spacelike separated region $\mathcal{R}_B$ can detect Alice's intervention, violating causality.
- The mechanism is the collapse postulate: after Alice's measurement, the state changes globally (not just in $\mathcal{R}_A$), and this global change can be detected by Bob.

**Fewster-Verch measurement framework:**
- Fewster and Verch have developed an algebraic framework for "selective" and "non-selective" measurements in AQFT that is causally consistent. In this framework, measurements are modeled as local unitary evolutions (not projections), and the "outcome" is obtained by coupling the field to a probe system.
- Not all observables admit such causal measurements: the class of "measurable" observables (in the Fewster-Verch sense) is strictly smaller than the full local algebra. In particular, observables that are intrinsically "non-selective" (e.g., the vacuum projector) are not directly measurable.

**Unruh-DeWitt detector as operational measurement:**
- The [[unruh-dewitt-detectors]] model couples a two-level system (the detector) to the field via a local interaction $H_{\text{int}}(t) = \lambda \chi(t) \mu(\tau) \otimes \phi(x(\tau))$. After the interaction, measuring the detector's two-level observable gives indirect information about the field. This is causally consistent.
- Bell-CHSH experiments using Unruh-DeWitt detectors have been studied in the program (JHEP 2024, Universe 2024), and the resulting Bell violations are related to but different from the direct Weyl operator correlators.

**What is not known:**
- A complete classification of which observables in local QFT (specifically [[type-iii-von-neumann-algebras]]) are "measurable" in the Fewster-Verch sense.
- Whether the specific Weyl operators $W(f)$ used in the Bell-CHSH program admit operational measurements — or whether they are formal objects whose correlators can only be inferred indirectly.
- How the gap between ideal and operational measurements affects the quantitative Bell violation: does the Unruh-DeWitt model always give a smaller violation than the ideal Weyl operator computation?

## Possible Approaches

1. **Classification of measurable operators in type III algebras**: Using the Fewster-Verch framework, determine which elements of the local von Neumann algebra $\mathcal{A}(\mathcal{O})$ admit causally consistent measurements. In particular, check whether [[weyl-operators]] $W(f)$ with $\text{supp}(f) \subset \mathcal{O}$ are measurable. This is a mathematical physics question with a potentially sharp answer.

2. **Comparison of Weyl and Unruh-DeWitt Bell violations**: In the cases where both computations are available (scalar field, Rindler geometry), compare the Bell-CHSH violation from the ideal Weyl computation with the Unruh-DeWitt detector computation. Determine the ratio as a function of the coupling strength $\lambda$, the detector switching function $\chi(t)$, and the field mass $m$. This comparison quantifies the "measurement gap."

3. **Regularization and finite-time measurements**: Replace the instantaneous projection with a finite-duration von Neumann measurement (Gaussian in time). Compute the Bell violation as a function of measurement duration $T$ and show that the ideal result is recovered as $T \to 0^+$, with corrections of order $T/\tau$ where $\tau$ is the natural timescale of the field (inverse mass). This provides a smooth interpolation between ideal and physical measurements.

4. **Bostelmann-Fewster "impossible measurements" catalogue**: Systematically apply the Bostelmann-Fewster analysis to the specific observables used in the Bell-CHSH program. Identify which are possible and which are not, and for the impossible ones, find the closest operationally achievable observable and estimate the Bell violation for that observable.

5. **Connection with the split property**: The [[split-property]] (which holds for free massive fields) ensures that for any two spacelike separated bounded regions, the joint algebra factors as a product. This is related to the ability to perform independent measurements in the two regions. For massless fields or theories without a mass gap, the split property may fail, complicating the measurement picture.

## Related Questions

- [[higher-spin-bell-inequalities]] — Ideal measurement limitations are more severe for higher-spin fields, which have more constrained localization properties
- [[embezzlement-cost-relative-entropy]] — Operational limitations on measurements bound what information can be extracted from embezzlement protocols
- [[entanglement-as-confinement-probe]] — If entanglement measures require impossible measurements, the phase-transition probe program needs operational reformulation
- [[bell-inequalities-with-gribov-horizon]] — Measurement limitations in gauge theories are compounded by the Gribov problem
