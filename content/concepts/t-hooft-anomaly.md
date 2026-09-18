---
title: "'t Hooft Anomaly"
type: concept
areas: [confinement-duality, condensed-matter-connections]
aliases: ["'t Hooft anomaly", anomaly matching, anomaly inflow, mixed anomaly, Lieb-Schultz-Mattis]
modified: 2026-07-01
---

## Definition

A **'t Hooft anomaly** is an obstruction to gauging a global symmetry: a phase acquired by the partition function $Z[A]$ under a background gauge transformation that no local counterterm built from the background $A$ can remove. Unlike a dynamical anomaly, the symmetry is preserved — but the theory cannot be coupled consistently to a background for it without a partner in one higher dimension.

Two properties make anomalies powerful:

- **Anomaly matching** ('t Hooft): the anomaly is renormalization-group invariant, so the UV and IR must reproduce it. A trivially gapped symmetric vacuum is forbidden when the anomaly is nonzero — the IR must break the symmetry, be gapless, or carry a nontrivial topological sector.
- **Anomaly inflow**: the non-invariance is cancelled by a bulk symmetry-protected topological (SPT) phase in $d+1$ dimensions whose boundary is the anomalous theory. "An anomaly is the boundary of an SPT."

Anomalies need not be exotic. A symmetry realized **projectively** on the Hilbert space is the 0+1d germ; the **Lieb–Schultz–Mattis** theorem is a lattice mixed anomaly between translation and internal symmetry, forbidding a unique gapped ground state for a half-integer-spin chain.

## Role in Research

Anomalies enter the [[higher-form-symmetries|generalized-symmetry]] program as sharp, RG-stable constraints on phase diagrams. The centerpiece example in the course is **Yang–Mills at $\theta = \pi$**: a mixed anomaly between the $\mathbb{Z}_N$ 1-form center symmetry and time reversal (Gaiotto–Kapustin–Komargodski–Seiberg) forbids a trivially gapped, $T$-symmetric, confining vacuum. On the lattice the anomaly is a fractional instanton number in the presence of a 2-form background, built from the cup product $B\cup B$ (Pontryagin square).

- Mixed anomalies with higher-form symmetries directly constrain confinement scenarios in the group's [[confinement-duality]] program.
- The modified [[villain-action|Villain]] construction realizes these anomalies exactly on a finite lattice.

## Relations

- [[higher-form-symmetries]] — anomalies of and mixed anomalies with $p$-form symmetries
- [[spt-phases]] — inflow: the anomalous theory lives on the boundary of a bulk SPT
- [[lattice-gauge-theory]] — the θ = π anomaly as fractional instanton number with a center background
- [[villain-action]] — exact lattice backgrounds that make the anomaly visible without a continuum limit

## Papers

't Hooft (1980, anomaly matching); Gaiotto–Kapustin–Komargodski–Seiberg, JHEP 05 (2017) 091 [arXiv:1703.00501]; Lieb–Schultz–Mattis (1961), Oshikawa (2000), Hastings (2004). See the course bibliography.

## Notes

- The Pontryagin square $\mathcal{P}(B)$ is the honest lattice object; the non-commutativity of the cup product is what carries the anomaly, so it must not be "simplified away."
- LSM being an anomaly is the clean statement that "an anomaly can live in an ordinary spin chain" — anomalies are not the exclusive property of chiral gauge theories.
