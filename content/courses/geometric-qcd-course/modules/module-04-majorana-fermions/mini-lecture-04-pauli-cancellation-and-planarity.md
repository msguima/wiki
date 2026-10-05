---
title: "Mini-Lecture IV.4: Pauli Cancellation and Planarity"
type: lecture-notes
course: geometric-qcd-course-guide
module: 4
lecture: "IV.4"
modified: 2026-10-05
---

# Mini-Lecture IV.4: Pauli Cancellation and Planarity

*We study a local Grassmann cancellation and its global limitation. The worked calculation and its limitations are the classroom target; the longer source reconstruction supports independent study.*

## How to use this lecture

**Prerequisites:** IV.3; antisymmetric products. Review the relevant [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridge]] before starting.

- **Classroom core, 90 minutes:** question and prerequisites (10); a local Grassmann cancellation and its global limitation (25); worked calculation or laboratory (30); problems 1–2 (20); written exit check (5).
- **Self-study, approximately 2–3 hours:** reconstruct the algebra in the main text, work through the laboratory, then solve problems 1–3 before reading the answer checkpoints. The estimate is provisional.
- **Research extension:** problem 4 states the source-dependent task and what counts as completion. Its open claims are not assumed in the classroom assessment.

The classroom result is the explicitly calculated model or conditional derivation below. Retained sections marked Source reconstruction explain the IAS argument and identify provenance; that label does not certify the argument. The [[courses/geometric-qcd-course/claim-status-map|claim map]] records the research limits. The literal extended-surface identity fails the circle check in III.5; geometric QCD conclusions depending on it remain conditional.

## Reading

- **Primary:** [IAS lectures](https://www.ias.edu/sites/default/files/IASQCDLectures_0.pdf), pages 100-103. Consult the page images when an equation is clipped or extraction is ambiguous.
- **Gentler route:** the [[courses/geometric-qcd-course/appendices/prerequisite-bridges|prerequisite bridges]], followed by this lecture's worked calculation.
- **Optional research:** the [[courses/geometric-qcd-course/bibliography#Module 4|bibliography and version map]] identifies the primary papers for this module and their role.


## Source Pages

Primary source: `IASQCDLectures.pdf`, pages 100-103.

## The Question

Why do the slides claim that Fermi statistics remove non-planar intersections?

## Notation

- Planar vertex: two loop segments touching without crossing.
- Non-planar vertex: two loop segments crossing.
- $(-1)^\nu$: the Fermi sign (IV.3).
- $(\bar{\psi}_R\psi_R)^2=0$: the Pauli-principle algebraic identity (p100).
- $\psi_R$: the right-handed component of the Elfin field.
- Vdovichenko rearrangement: sum over vertices instead of loops (IV.3).
- 't Hooft planar diagrams: the double-line planar expansion of large-$N_c$ QCD (I.1).

## Derivation

### Step 1 — Two types of vertices: planar and non-planar (p100)

After the Vdovichenko rearrangement (IV.3), the loop sum is a sum over *vertices* — points where two loop segments meet. The slide (p100, figure — consult the source PDF) shows two types:

- **Planar touching (upper figure):** two segments approach, touch at a point, and separate on the *same* side — no crossing. The local topology is that of two lines tangent at a point, not two lines crossing.
- **Non-planar crossing (lower figure):** two segments cross — one passes *over* the other. The local topology is that of two lines intersecting at a point, with four outgoing legs.

These are local configurations in the source drawing. Graph-theoretic planarity concerns an embedding of the complete ribbon graph, including its cyclic order; a crossing in one drawing is not by itself a proof of nonzero genus.

*What is being used:* the Vdovichenko vertex classification. **Status: Source reconstruction.**

### Step 2 — The cancellation: non-planar cancels planar (p100)

The proposed cancellation (p100): the non-planar vertex and the planar vertex contribute with *opposite signs*, and they *exactly cancel*. The mechanism:

- A **non-planar crossing** increases the self-intersection number $\nu$ by 1, contributing a factor $(-1)^{\nu+1}=-(-1)^\nu$ — a *sign flip* relative to the non-crossing case.
- A **planar touching** does *not* increase $\nu$ (the segments touch but do not cross — the intersection number is unchanged), contributing a factor $(-1)^\nu$ — *no sign flip*.
- The source assumes the two contributions (crossing and touching) have the *same* magnitude (they involve the same local loop segments, just arranged differently) but *opposite* signs — so they cancel.

The slide (p100) states: "The non-planar vertex exactly cancels the first planar vertex! Terms with intersecting lines are algebraically annihilated by terms with parallel touching lines of opposite orientation."

*What is being used:* the Fermi sign $(-1)^\nu$ and the vertex classification. **Status: **`slide claim`** — the cancellation is described but the detailed combinatorial proof (showing the exact cancellation for all vertex types, not just the simplest) is not fully exhibited in the PDF.**

### Step 3 — The algebraic identity: $(\bar{\psi}_R\psi_R)^2=0$ (p100)

For a single pair of independent Grassmann generators $\bar\theta,\theta$, the even bilinear $b=\bar\theta\theta$ has square $b^2=-\bar\theta^2\theta^2=0$. Its parity is even; its nilpotence follows from using the same generators twice.

For several components, $B=\sum_a\bar\theta_a\theta_a$ need not obey $B^2=0$: cross terms with different labels survive. Thus the displayed source identity applies only after the relevant one-state or one-component reduction has been justified. A global path cancellation additionally needs equal weights and a sign-reversing correspondence, as the laboratory explains.

### Step 4 — The Ising-model analogy (p100)

The slide (p100) draws the analogy with the **2D Ising model**: "In case of the Ising model, these curves were phase boundaries between domains of spin $\pm 1/2$ (non-oriented curves). In our case, these are oriented curves tracking double line of gluon indices in planar graphs of QCD."

In the Ising model, the Vdovichenko loops are *domain walls* — the boundaries between regions of up-spin and down-spin. They are non-oriented (no direction on the wall). In the Elfin theory, the loops are *oriented* — they track the double-line color flow of 't Hooft's planar diagrams (I.1). The orientation is what connects the Elfin loops to the planar QCD graphs: the oriented loops *are* the double-line color flow.

*What is being used:* the Vdovichenko/Ising analogy. **Status: `standard` (Vdovichenko 1963); `interpretive` (the identification of Elfin loops with 't Hooft double lines).**

### Step 5 — The emergent planar string (p101)

After the cancellation (Step 2), only *non-intersecting* loops survive — a hierarchy of trapped loops, each moving in the free space left by the others (p101, figure — consult the source PDF). The slide (p101) describes:

- "By discarding all non-planar configurations, the functional integral reduces to a hierarchy of trapped loops moving in the free space left by others."
- "A time slice of this picture (red line) describes a string with Elf pairs $(\psi,\bar{\psi})$ moving between neighbors."
- "This exactly matches the topological structure of 't Hooft's planar diagram expansion, but rigorously preserves gauge invariance!"

The time slice (p101) is the **planar string**: at each instant, the surface is cut by a line (the time slice), and the intersection points are Elf pairs — quark-antiquark pairs connected by the string. The forces between the quark and antiquark are mediated by *fluctuations of elves* (p101): "in perturbative QCD these were gluons, but here, on a minimal surface, these forces are mediated by fluctuations of elves, summing these planar QCD gluon graphs into fermion determinants."

The projection of the 4D gluon graphs onto the 2D minimal surface (p101) "makes the planar QCD solvable by powerful methods of two-dimensional field theory and conformal anomalies."

*What is being used:* the hierarchy of trapped loops and the time-slice picture. **Status: **`slide claim`** — the emergence of the planar string is the central claim of IV.4; the mechanism (Pauli cancellation) is described, but the full proof that the surviving hierarchy *is* the 't Hooft planar expansion is not in the PDF.**

### Step 6 — Loop equations on the minimal surface: setup (p102-p103)

IV.5–IV.6 examine the proposed area derivatives and the additional matching needed to recover the MM equation. They establish finite identities and a normalized radial model, while leaving the full surface-determinant derivation conditional. The setup (p102-p103):

**First area derivative (source page 102, equation (92)).** The source proposes
$$
\frac{\delta Z}{\delta\sigma_{\mu\nu}(x_1)}
=-m\int\mathcal D\Gamma_{11}\,T_{\mu\nu}(1)\,
Z[S_{\mathrm{in}}]Z[S_{\mathrm{out}}]e^{-ml_{11}}.
$$
A path $\Gamma$ cuts the surface into two pieces. The source identifies the area variation with a loop touching the boundary; this requires its geometric and determinant prescriptions.

**Second area derivative (source page 103).** The proposed diagrams contain two separate loops, labeled the A-term, or one loop connecting two boundary points, labeled the B-term. IV.5 distinguishes this diagrammatic matching from the exact second-variation identity for a regulated partition function.

*What is being used:* the area-derivative structure of the determinant. **Status: Source reconstruction (the structure); the detailed matching is IV.5-IV.6.**

## Worked laboratory: exclusion at one state

Let $\theta_1,\theta_2$ be Grassmann generators. Moving the third generator past the second gives
$$
\theta_1\theta_2\theta_1\theta_2
=-\theta_1^2\theta_2^2=0.
$$
This is exact exclusion of repeated identical Grassmann states. In contrast $\theta_1\theta_2\theta_3\theta_4$ need not vanish when all four generators are distinct.

In a fermion path representation, spin, internal labels, orientation, and boundary conditions determine whether two geometric configurations use the same states and have equal magnitudes. A spatial crossing alone does not force the two amplitudes to cancel. To prove a global cancellation one needs an explicit pairing of configurations, opposite signs, equal remaining weights, and control of fixed configurations.

The local calculation explains why the source mechanism is plausible as a combinatorial proposal, while keeping the claim that all nonplanar contributions disappear at its proper scope.

## What Was Proved, What Was Assumed

| Claim | Status |
|---|---|
| Two vertex types: planar (touching) and non-planar (crossing) | Source reconstruction |
| The proposed crossing sign supplies opposite signs | Source representation; equal magnitudes and a complete pairing still required |
| The non-planar vertex exactly cancels the planar vertex (the proposed cancellation) | **`slide claim`** — described but not fully proven combinatorially |
| The square of a bilinear made from one Grassmann pair vanishes | Exact local calculation; multi-component sums need not vanish |
| After cancellation, only non-intersecting (planar) loops survive | **`slide claim`** |
| The surviving hierarchy is the 't Hooft planar diagram expansion | **`slide claim`** |
| The forces are mediated by Elf fluctuations (gluon graphs summed into the determinant) | **`slide claim`** |
| First and second area derivatives of $Z[S]$ split into $A$-term (disconnected) and $B$-term (connected) | Source reconstruction |

## Common Traps

- **Reading the cancellation as proven.** The mechanism (Fermi sign + Grassmann algebra) is standard, but the *exact* combinatorial cancellation for all vertex types (not just the simplest) is `slide claim`. The slides show the simplest case and state the general result.

- **Conflating the Ising domain walls with the Elfin loops.** They are analogous (both use Vdovichenko) but different: Ising domain walls are non-oriented; Elfin loops are oriented (they track the color flow). The orientation is what connects to the planar QCD graphs.

- **Treating the "emergent planar string" as a derivation.** It is a *claim* — the hierarchy of trapped loops *looks like* the 't Hooft planar expansion, but a proof that it *is* the planar expansion (with the correct graph weights and combinatorial factors) is not in the PDF.

- **Confusing chirality with one independent Grassmann state.** Even with one chirality, distinct internal components can give nonzero cross terms. The boundary domain and component reduction must be established before invoking the single-pair identity.

## Source Map

| Subsection | Source page | Slide equations |
|---|---|---|
| Cancellation of intersections: planar vs. non-planar vertices; $(\bar{\psi}_R\psi_R)^2=0$; Ising analogy | p100 | (prose, figure) |
| Emergence of the planar string; trapped loops; time slice = Elf pairs; 't Hooft planar expansion | p101 | (prose, figure) |
| First area derivative of $Z[S]$; path $\Gamma$ cuts surface | p102 | eq (91), eq (92) |
| Second area derivative: $A$-term (disconnected) and $B$-term (connected) | p103 | (figures) |

## Problem set

1. **Classroom core.** Reduce $\theta_1\theta_2\theta_1\theta_2$.

2. **Self-study calculation.** Does the same argument kill a product of four distinct generators?

3. **Self-study interpretation.** List the data needed for a sign-reversing cancellation of paths.

4. **Research extension.** Construct such a pairing for a finite regulated surface graph.

## Answer checkpoints

1. One interchange yields $-\theta_1^2\theta_2^2=0$.

2. No. That product is a nonzero basis element of the Grassmann algebra.

3. A pairing or involution, opposite signs, equal magnitudes and measures, and a treatment of fixed points and boundary configurations.

4. Completion: enumerate the configurations and show cancellation with all spin and internal labels retained. A finite example is not an all-orders continuum proof.

## Teaching note

Use the decisive step in problem 2 as the written exit check for IV.4; assign problem 3 only after students have named the assumptions. Grade the research extension by its documented method and justified conclusion, including an unresolved result when evidence is missing. The timing above awaits classroom rehearsal.

[[mini-lecture-03-determinants-as-loop-sums|Previous note]] · [[mini-lecture-05-large-mass-limit-and-the-a-term|Next note]] · [[geometric-qcd-course-guide|Course guide]]
