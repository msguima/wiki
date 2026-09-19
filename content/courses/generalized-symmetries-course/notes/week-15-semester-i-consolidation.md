---
title: "Week 15 — Consolidation: Everything Was Symmetry All Along"
type: lecture-notes
course: syllabus
semester: 1
week: 15
block: D
duration: 4 hours (2 hr synthesis lecture + take-home final assigned)
prerequisites: All of Semester I (Weeks 1–14)
modified: 2026-07-01
---

# Week 15 — Consolidation: Everything Was Symmetry All Along

> *No new technique this week — a change of viewpoint. Look back over fourteen weeks and one pattern is everywhere: the physics lived not in local fields but in operators supported on closed loops and surfaces, and the phases were distinguished by how those operators behaved. Wilson loops, 't Hooft loops, Polyakov lines, disorder operators, vortices, monopoles — all of them are either charged extended objects or the symmetry generators that act on them. Semester II gives this one name. This week we assemble the evidence.*

## 0. Reading

**Primary:** none new — this is a retrospective. Recommended forward reading before Semester II: Gaiotto, Kapustin, Seiberg, Willett, *JHEP* 02 (2015) 172 [arXiv:1412.5148], §1 (the introduction that names the subject).

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]]. The Semester II Block 1 skeleton is the immediate sequel.

## 1. The thesis, in one sentence

$$
\textit{A phase is characterized by which extended (closed-submanifold) operators can be detected, and how the symmetries acting on them are realized.}
$$

Local order parameters — the Landau paradigm — are the special case where the extended operator is a point (a 0-form symmetry acting on a local field). Everything in Semester I that Landau could not describe was a *higher* case. Semester II is the systematic theory; Semester I was the evidence.

## 2. The transitions with no local order parameter

Every phase transition of Semester I that resisted a Landau description, tabulated with what actually changes:

| Transition | Week | What changes | Diagnosed by |
|---|---|---|---|
| BKT (XY vortex unbinding) | [[week-04-bkt-kramers-wannier-disorder|4]] | vortices bound → free | stiffness jump; vortex fugacity RG |
| Wegner ℤ₂ gauge | [[week-05-wegner-z2-gauge-theory|5]] | Wilson loop area → perimeter | Wilson loop; dual Ising order |
| Compact QED₃ (always confined) | [[week-10-polyakov-mass-gap-area-law|10]] | photon massless → gapped (never) | area law; dual-photon mass |
| Compact $U(1)$ 4d (Coulomb ↔ confining) | [[week-11-monopole-condensation-4d|11]] | monopole loops dilute → condensed | Wilson/'t Hooft loops |
| Fradkin–Shenker interior | [[week-13-fradkin-shenker-gauge-higgs|13]]–[[week-14-fradkin-shenker-order-parameters|14]] | center 1-form symmetry realization | Polyakov loop; (no local OP) |

Not one of these is a local-order-parameter transition. Every one is the (de)confinement of an extended operator or the (un)binding of a topological defect. The Landau order parameter appears in this table exactly zero times.

## 3. The extended operators, reorganized

Relist every extended operator of the semester as either a **charged object** or a **symmetry generator** — the GKSW dictionary, avant la lettre:

| Operator | First seen | Role (Semester II reading) |
|---|---|---|
| Wilson loop $W(C)$ | [[week-05-wegner-z2-gauge-theory|5]] | charged line of the electric 1-form symmetry |
| 't Hooft loop $\tilde W(\tilde C)$ | [[week-11-monopole-condensation-4d|11]] | charged line of the magnetic 1-form symmetry / its generator |
| Polyakov loop $P$ | [[week-14-fradkin-shenker-order-parameters|14]] | order parameter for center symmetry |
| Kadanoff–Ceva $\mu$ | [[week-04-bkt-kramers-wannier-disorder|4]] | disorder operator; charged under the dual symmetry |
| Vortex $v = dn$ | [[week-03-villain-form-xy-duality|3]] | charged under the magnetic/winding symmetry |
| Monopole $m = dn$ | [[week-08-dual-variables-abelian-gauge|8]], [[week-11-monopole-condensation-4d|11]] | charged under the magnetic symmetry |
| Symmetry surface $U_g(\Sigma)$ | (implicit) | generator; acts on the above by linking |

The single organizing statement Semester II opens with: **a symmetry is a topological operator, and it acts on its charged objects by linking in spacetime.** Every row above is an instance we have already computed.

## 4. Duality is Poisson resummation

The other spine of the semester. Every duality we performed was one manipulation — Poisson-resum an integer cochain, solve the resulting conservation constraint on the dual lattice:

| Direct theory | Dual | Defect | Week |
|---|---|---|---|
| 2d XY | Coulomb gas / sine-Gordon | vortex (point) | [[week-03-villain-form-xy-duality|3]] |
| 2d Ising | Ising (self-dual) | disorder $\mu$ | [[week-04-bkt-kramers-wannier-disorder|4]] |
| 3d ℤ₂ gauge | 3d Ising | 't Hooft loop | [[week-05-wegner-z2-gauge-theory|5]] |
| 3d compact $U(1)$ | dual photon + $\cos\sigma$ | monopole (point) | [[week-08-dual-variables-abelian-gauge|8]]–[[week-10-polyakov-mass-gap-area-law|10]] |
| 4d compact $U(1)$ | dual photon + monopole loops | monopole (loop) | [[week-08-dual-variables-abelian-gauge|8]], [[week-11-monopole-condensation-4d|11]] |

One engine, five rows, coefficient group $\mathbb{Z}$ or $\mathbb{Z}_N$ or $\mathbb{Z}_2$ as needed. Semester II Week 12 makes every one of these **exact** (modified Villain) and re-reads the "defect" column as a **higher-form symmetry** being explicitly broken or gauged.

## 5. The four threads, gathered

The recurring threads flagged in the syllabus, now visibly one investigation:
1. **Duality is Poisson resummation** — §4.
2. **Symmetries live on topological operators** — §3.
3. **Condensation changes the theory** — vortex unbinding (Wk 4), monopole condensation (Wks 10–11), Higgs (Wk 13); each a defect ensemble proliferating, each changing the effective description. This thread runs straight into the group's [[julia-toulouse-mechanism|Julia–Toulouse]] research line.
4. **Cohomology is the bookkeeping** — cochains and Poincaré duality (Wk 2) underlie every flux sector, defect location, and ground-state count.

## 6. What to take away

1. **Semester I was the theory of extended operators**, told before its name. Landau order parameters describe the $p=0$ corner of a larger structure.
2. **The transitions that mattered had no local order parameter** — they were (de)confinements of loops and (un)bindings of defects.
3. **Every extended operator is a charged object or a symmetry generator**, and duality is one Poisson-resummation move. Semester II names both.

## 7. Take-home final

Five problems, spanning the semester. Core track attempts 1–4; starred track all five. Two weeks.

**Problem 1 — A duality chain.**
Starting from the 2d Villain XY model, carry the duality all the way to sine-Gordon, then repeat for 3d compact $U(1)$ to the dual-photon $\cos\sigma$ theory. Track every boundary term and identify, in each case, the defect, the dual field, and the coupling inversion.

**Problem 2 — Strong coupling with matter.**
For ℤ₂ (or $SU(2)$) gauge theory with fundamental matter, compute the Wilson loop to two orders in the strong-coupling expansion, exhibit string breaking, and show the area law is replaced by perimeter law beyond the breaking length $R_*$. Estimate $R_*$.

**Problem 3 — Polyakov confinement.**
Reproduce the compact-QED₃ mass gap $m_\gamma^2 = 8\pi^2\zeta/e^2$ and the Wilson-loop string tension $\sigma_{\text{str}} = 16\sqrt{A\zeta}$, and show both scale as $e^{-S_{\text{mono}}/2}$. Then argue (energy–entropy for loops) why the 4d theory has a genuine Coulomb phase but the 3d theory does not.

**Problem 4 — A duality with a defect.**
Set up the Kramers–Wannier duality defect on the Ising transfer matrix, verify it is topological at the self-dual point, and compute the fusion $D\times\bar D = 1 + \eta$. Explain in words why the appearance of a *projector* (not an inverse) means $D$ generates a non-invertible symmetry. (This problem prefigures Semester II Week 13.)

**Problem 5 (⋆) — Residual symmetry and the research frontier.**
For $\mathbb{Z}_N$ gauge theory with charge-$q$ matter, derive the residual 1-form symmetry $\mathbb{Z}_{\gcd(N,q)}$. Then connect to the master-project: show that gauging the subgroup $H=\langle q\rangle$ leaves the same residual data, and articulate the sense in which screening and subgroup gauging are dual. Comment on how this is the Semester I seed of the group's Julia–Toulouse-as-higher-gauging program.

## 8. Looking ahead: Semester II

Semester II opens (Block 1) by defining a symmetry as a topological operator and a $p$-form symmetry by the dimension of its charged objects. Immediately, every table above is reorganized: confinement becomes an unbroken 1-form symmetry, deconfinement its spontaneous breaking, the deconfined vacuum a topological order, and the Julia–Toulouse condensation of Block C a gauging of a higher-form symmetry on a submanifold. The tools are all built. What changes is that we finally have the words.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block D — the close of Semester I. Last revised 2026-07-01.*
