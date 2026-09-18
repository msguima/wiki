---
title: String-Net Condensation
type: concept
areas: [condensed-matter-connections]
aliases: [string-net condensation, string-nets, Levin-Wen model, Wen string-net]
modified: 2026-07-01
---

## Definition

**String-net condensation** (Levin–Wen, 2005) is a microscopic mechanism that produces topologically ordered phases and, with them, emergent gauge fields and their charges. The ground state is a coherent superposition — a "condensate" — of fluctuating networks of strings, whose amplitudes are fixed so that the state is invariant under local deformations.

A string-net model is specified by combinatorial data, presented operationally without category theory:

- **String types** and **fusion rules** $N_{ab}^c$ (which strings can merge at a vertex),
- **$F$-symbols** $F^{abc}_d$ (the amplitude for local recoupling moves), constrained by the **pentagon identity**.

The Hamiltonian enforces the branching rules (vertex terms) and $F$-move invariance (plaquette terms), and is a sum of commuting projectors like the [[toric-code]]. The simplest case — two string types with trivial $F$ — *is* the toric code (the $\mathbb{Z}_2$ string-net). Richer data (Fibonacci, doubled Ising) yields non-abelian anyons.

## Role in Research

String-net condensation is Wen's answer to "where do gauge fields come from": a deconfined gauge theory is a condensate of its own electric strings, so the gauge field and its charges emerge together from a bosonic spin system. In the [[condensed-matter-connections]] line and the generalized-symmetries course it closes the loop opened by Kogut–Susskind — the electric flux strings of [[lattice-gauge-theory]] are the strings that condense — and provides the general framework in which the [[toric-code]] is just the smallest example.

- It realizes all non-chiral (doubled) [[topological-order|topological orders]] from local, exactly solvable Hamiltonians.
- The $F$-symbol data is the same fusion-category input that governs the fusion of anyons and of [[condensation-defects]].

## Relations

- [[toric-code]] — the $\mathbb{Z}_2$ string-net; the simplest condensate
- [[topological-order]] — string-net condensation is the general mechanism producing it
- [[higher-form-symmetries]] — the condensed strings are the charged objects of the emergent gauge symmetry
- [[lattice-gauge-theory]] — Kogut–Susskind electric strings are what condense

## Papers

Levin–Wen, "String-net condensation," Phys. Rev. B 71 (2005) 045110 [cond-mat/0404617]; Wen, *Quantum Field Theory of Many-Body Systems* (2004). See the course bibliography.

## Notes

- "Condensation" here is condensation of extended objects (strings), the higher-form analogue of ordinary Bose condensation of particles — the same generalization that underlies [[condensation-defects]] and the [[julia-toulouse-mechanism]].
- String-net models produce only **non-chiral** topological orders (the doubled theories); genuinely chiral phases like the Laughlin state need extra input (a chiral edge), which is why the framework naturally yields "doubled Ising" rather than Ising.
