---
title: "Sem II Week 2 — Witten diagrams"
type: lecture-notes
course: syllabus
semester: 2
week: 2
block: 1
duration: "3 hours (lecture + seminar)"
status: drafting
modified: 2026-05-28
---

# Sem II Week 2 — Witten Diagrams

> *Sem I Wk 10 introduced the Witten-diagram rules and computed two- and three-point functions. This week takes them to **four points**, where dynamics beyond OPE coefficients lives: **contact** diagrams give $D$-functions, **exchange** diagrams give a single-trace conformal block plus a **double-trace tower** with $O(1/N^2)$ anomalous dimensions, and the whole thing is organised cleanly by the **bulk-to-bulk propagator's harmonic (Plancherel) decomposition** and by **Mellin amplitudes** — the closest thing CFT has to a momentum-space S-matrix. This is the technical engine of the modern bootstrap–holography interface.*

## Learning goals

By the end of this week, a student can:

1. Write the contact four-point Witten diagram and identify it as a $D$-function of the cross-ratios.
2. Define the bulk-to-bulk propagator and set up the exchange diagram via the split representation.
3. State the harmonic/Plancherel decomposition (principal vs discrete series).
4. Decompose an exchange diagram into the exchanged block + double-trace tower, and identify $O(1/N^2)$ anomalous dimensions.
5. State what the Mellin amplitude and the flat-space limit add.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Advanced AdS/CFT* §6** — *Witten Diagrams and Large-N Perturbation Theory*, plus three-point functions and cubic couplings.
- D'Hoker, Freedman, *Supersymmetric gauge theories and the AdS/CFT correspondence*, [arXiv:hep-th/0201253](https://arxiv.org/abs/hep-th/0201253) — $D$-functions, exchange diagrams.
- Penedones, *Writing CFT correlation functions as AdS scattering amplitudes*, [arXiv:1011.1485](https://arxiv.org/abs/1011.1485) — Mellin amplitudes & flat-space limit.

**Prerequisites.** [[week-10-bulk-correlators]] (rules, 2pt/3pt, bulk-to-boundary $K_\Delta$), [[week-03-ope-and-conformal-blocks]] (conformal blocks, crossing, the GFF double-trace tower), [[sem2-week-01-holographic-renormalisation-in-depth]].

**AQFT cross-reference.** None.

## 1. Contact diagrams and $D$-functions

The simplest four-point Witten diagram comes from a quartic bulk contact vertex $\tfrac{\mu}{4!}\phi^4$: a single integrated vertex with four bulk-to-boundary legs,

$$
A_{\rm contact} = -\mu\int_{\rm AdS} d^{d+1}z\,\sqrt g\,\prod_{i=1}^4 K_{\Delta_i}(z;x_i) \equiv (\text{prefactor})\times D_{\Delta_1\Delta_2\Delta_3\Delta_4}(u,v).
$$

The $D$-functions are the standard special functions of AdS amplitudes. Their key property: conformal covariance forces $D_{\Delta_1\dots\Delta_4}$ to depend only on the cross-ratios $u,v$ (after stripping the kinematic prefactor) — the Ward identity of [[week-03-ope-and-conformal-blocks|Wk 3]] realised diagrammatically. They are evaluated via Schwinger parameters (Exercise 4): exponentiate each $K_\Delta$, do the Gaussian bulk integral, and reduce to a parametric integral $\bar D_{\Delta_1\dots\Delta_4}(u,v)$. A contact diagram has **no single-trace exchange** — in the conformal-block language it is purely **double-trace** $[\mathcal{O}\mathcal{O}]_{n,\ell}$, the GFF tower of Wk 3 dressed by the contact interaction.

> **[Proven]** the contact diagram is finite, conformally covariant, and equals a $D$-function (§1; Exercise 4 evaluates $\bar D_{1111}$).

## 2. The bulk-to-bulk propagator and exchange diagrams

For diagrams with internal lines, one needs the **bulk-to-bulk propagator** $G_{\Delta_e}(z,z')$ — the regular Green's function of $(\Box-m_e^2)$ in AdS, $m_e^2L^2=\Delta_e(\Delta_e-d)$. It depends only on the AdS-invariant chordal distance and behaves as $G_{\Delta_e}\sim(\text{chordal})^{-\Delta_e}$ at short distance and $\sim z^{\Delta_e}$ near the boundary. The **exchange diagram** (cubic vertices joined by $G_{\Delta_e}$) is

$$
A_{\rm exch} = \int d^{d+1}z\,d^{d+1}z'\sqrt{g}\sqrt{g'}\;K_{\Delta_1}(z)K_{\Delta_2}(z)\,G_{\Delta_e}(z,z')\,K_{\Delta_3}(z')K_{\Delta_4}(z').
$$

The double bulk integral is hard directly; the **split representation** writes $G_{\Delta_e}$ as a spectral integral over a product of two bulk-to-boundary propagators glued at a common boundary point, turning the exchange into an integral of three-point-like structures — making the conformal-block content manifest (§4).

## 3. Harmonic (Plancherel) decomposition

Decompose $G_{\Delta_e}$ in **AdS harmonics** $\Omega_{\nu,\ell}(z,z')$ — the AdS analogue of plane waves, eigenfunctions of the Laplacian labelled by a "radial momentum" $\nu$ and spin $\ell$:

$$
G_{\Delta_e}(z,z') = \int_{-\infty}^{\infty} d\nu\;\frac{\Omega_{\nu,\ell}(z,z')}{(\Delta_e-\tfrac d2)^2 + \nu^2} + (\text{discrete}).
$$

The **principal series** ($\nu\in\mathbb{R}$, dimension $\tfrac d2+i\nu$) saturates the Plancherel measure; the pole at $\nu=\pm i(\Delta_e-\tfrac d2)$ picks out the exchanged operator (the **discrete series** / bound state). Closing the $\nu$-contour on the principal series produces the **conformal partial wave** expansion of the dual CFT (D'Hoker–Mathur) — the bulk Plancherel decomposition *is* the boundary CPW expansion. This is the cleanest bridge between bulk fields and boundary operators at the level of four-point functions.

> **[Stated-without-proof]** the Plancherel decomposition (principal + discrete series; D'Hoker–Mathur).

## 4. Conformal-block structure and double-trace anomalous dimensions

Decomposing the exchange diagram in the $s$-channel gives:

$$
A_{\rm exch}\big|_{s\text{-channel}} = \underbrace{C_{12e}C_{34e}\,g_{\Delta_e,\ell_e}(u,v)}_{\text{single-trace exchange}} \;+\; \underbrace{\sum_{n,\ell} a_{n,\ell}\,g_{2\Delta+2n+\ell}(u,v)}_{\text{double-trace tower}}.
$$

Two pieces of physics:

- The **single-trace block** of the exchanged $\mathcal{O}_e$, with coefficient = product of tree-level OPE coefficients (computed in [[week-10-bulk-correlators|Wk 10]]).
- The **double-trace tower** $[\mathcal{O}\mathcal{O}]_{n,\ell}$ (dimensions $2\Delta+2n+\ell$ at $N=\infty$), now with $O(1/N^2)$ shifts. Reading the *coefficient of $\log u$* in the small-$u$ expansion gives the **anomalous dimensions** $\gamma_{n,\ell}=O(1/N^2)$: the binding energy of the two-particle state from the bulk interaction. This is the boundary face of "$1/N^2$ = bulk interactions" ([[week-07-large-n-and-thooft-limit|Wk 7]]) made quantitative — a bulk exchange shifts the energies of two-particle states by a computable amount.

There is a **contact-term ambiguity**: an exchange diagram is defined up to adding contact diagrams (truncating the tower); only the full correlator, fixed by crossing, is physical. **Crossing symmetry** is the statement that the $s$- and $t$-channel decompositions agree — the constraint the bootstrap exploits.

> **[Sketched]** exchange = single-trace block + double-trace tower; $\gamma_{n,\ell}=O(1/N^2)$ from the $\log u$ coefficient (D'Hoker–Freedman; Heemskerk–Penedones–Polchinski–Sully).

## 5. Mellin amplitudes and the flat-space limit

Witten diagrams have a "momentum-space" representation: the **Mellin amplitude** $M(s,t)$, defined by writing the (stripped) correlator as a Mellin transform over the cross-ratios. In Mellin space the dictionary simplifies dramatically:

- a **contact** diagram is a **polynomial** in the Mellin variables;
- an **exchange** of $\mathcal{O}_e$ gives **poles** at $s=\Delta_e-\ell_e+2m$ ($m\ge0$) — the analogue of an S-matrix pole at a particle's mass, with the satellite poles the descendants;
- **crossing** is simple Mellin-variable symmetry.

In the limit of large operator dimensions / high energies, Penedones' **flat-space limit** relates $M(s,t)$ to the bulk **flat-space S-matrix**: $M\to$ scattering amplitude as $L\to\infty$. So Mellin amplitudes are literally "CFT amplitudes," and AdS becomes a calculable regulator for flat-space scattering. The Lorentzian inversion formula (which extracts CFT data analytically from the double discontinuity) is the modern sharpening — a Phase-3 / advanced topic.

> **[Stated-without-proof]** the Mellin representation, its pole/polynomial dictionary, and the flat-space limit (Penedones).

## 6. Key claims and proof status

- **[Proven]** contact diagram = conformally covariant $D$-function (§1).
- **[Stated-without-proof]** bulk-to-bulk propagator, split representation, Plancherel decomposition (§§2–3).
- **[Sketched]** exchange = single-trace block + double-trace tower with $O(1/N^2)$ anomalous dimensions (§4).
- **[Stated-without-proof]** Mellin amplitudes and the flat-space limit (§5).

*No coefficients in this note are uncertain at the stated level. (No `CHECK` items for Wk 2.)*

## 7. What to take away

- **Contact** diagrams = $D$-functions of $(u,v)$; pure **double-trace** in block language.
- **Exchange** diagrams use the **bulk-to-bulk propagator** $G_{\Delta_e}$; the split representation makes the block content manifest.
- **Plancherel decomposition** of $G_{\Delta_e}$ (principal + discrete series) = the boundary conformal-partial-wave expansion (D'Hoker–Mathur).
- Exchange = **single-trace block + double-trace tower**; the $\log u$ coefficient gives $O(1/N^2)$ **anomalous dimensions** (bulk binding energies) — "$1/N^2$ = bulk interactions" made quantitative.
- **Mellin amplitudes** = CFT momentum space (contacts → polynomials, exchanges → poles); the **flat-space limit** recovers the bulk S-matrix.

## Exercises

**Core.**

1. **Bulk-to-boundary propagator.** Write $K_\Delta$ in AdS$_5$ and verify $K_\Delta\to z^{d-\Delta}\delta^d(\vec x-\vec x_i)$ (cf. Wk 8/10).
2. **Contact integral.** Set up $D_{1111}$ in AdS$_2$, reduce to a function of $u$, and state the Ward identity enforcing this.
3. **Exchange block.** For $\Delta_e=4$, external $\Delta=2$ in AdS$_5$, identify the leading exchanged block and its Casimir $C_2=\Delta_e(\Delta_e-d)$; classify principal vs discrete series.

**Starred.**

4. $\star$ **$\bar D_{1111}$.** Evaluate $\bar D_{1111}(u,v)$ in $d=4$ via Schwinger parameters; confirm dependence on $u,v$ only.
5. $\star$ **Anomalous dimensions.** From the $\log u$ coefficient of an exchange diagram, extract the leading double-trace anomalous dimension $\gamma_{0,0}=O(1/N^2)$ and interpret it as a binding energy.

**Project.**

6. **Mellin & flat space.** Read Penedones 1011.1485; compute the Mellin amplitude of a contact and an exchange diagram, and take the flat-space limit to recover a $\phi^4$ contact / a particle-exchange amplitude.

## Connections to other parts of the wiki

- **Within the course.** Extends [[week-10-bulk-correlators]] to four points; block structure from [[week-03-ope-and-conformal-blocks]]; the double-trace tower from [[week-07-large-n-and-thooft-limit]]. The tree four-point is the input to loop/conical-defect computations in [[sem2-week-04-replica-trick-in-gravity]].
- **Concepts.** [[gkp-witten-formula]], [[holographic-dictionary]].
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 1. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*
