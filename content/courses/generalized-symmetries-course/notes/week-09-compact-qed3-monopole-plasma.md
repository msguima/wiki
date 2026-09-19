---
title: "Week 9 — Compact QED₃ I: the Monopole Plasma"
type: lecture-notes
course: syllabus
semester: 1
week: 9
block: C
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 1–8; the Villain duality (Weeks 3, 8); sine-Gordon; 3d electrostatics
modified: 2026-07-01
---

# Week 9 — Compact QED₃ I: the Monopole Plasma

> *Week 8 dualized compact QED in three dimensions and found a dual photon dressed by monopole instantons. This week we take that plasma seriously: the monopoles are a gas of magnetic charges with a 3d Coulomb interaction, and the dual photon carries a magnetic symmetry that the monopoles explicitly break. Everything is now in place for next week's payoff — Polyakov's demonstration that this plasma gaps the photon and confines charge, permanently, at every coupling.*

## 0. Reading

**Primary:** Polyakov, *Nucl. Phys. B* 120 (1977) 429 — the founding calculation; and Polyakov, *Gauge Fields and Strings* (1987), ch. 4. Set up here, executed in [[week-10-polyakov-mass-gap-area-law|Week 10]].

**Secondary:**
- Kogut, *Rev. Mod. Phys.* 51 (1979) 659, §VI.
- Banks, Myerson, Kogut, *Nucl. Phys. B* 129 (1977) 493 — the lattice duality underpinning §2.

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]].

## 1. The setup: compact QED in three dimensions

Compact $U(1)$ gauge theory in $d=3$ (Euclidean) is the Villain theory of [[week-08-dual-variables-abelian-gauge|Week 8]],
$$
Z = \Big(\prod_\ell \int da_\ell\Big)\sum_{n\in C^2(\mathbb{Z})} e^{-\frac{\beta}{2}\|da - 2\pi n\|^2},\qquad \beta = \frac{1}{e^2 a}\ (\text{lattice}),
$$
with $e^2$ the 3d gauge coupling (dimension of **mass**). The photon in 3d has a single transverse polarization; classically it is a free massless field, and a naive continuum treatment would predict a Coulomb phase with a logarithmic (in 3d: linear-in-nothing) potential and deconfined charges. The compactness — the integer $n$ — changes this completely.

## 2. Duality to the dual photon [Computed.]

Run the Week-8 duality in $d=3$. Poisson-resumming $n$ and integrating out $a$ trades the gauge field for a **compact scalar** $\sigma$ — the **dual photon** — via
$$
\text{(field strength)}\quad \tfrac{1}{2}\varepsilon_{\mu\nu\rho}F^{\nu\rho} \ \propto\ \partial_\mu\sigma,\qquad \sigma \sim \sigma + 2\pi.
$$
The smooth (spin-wave) part gives a free scalar; the monopoles — the plaquette-cube obstructions $dn\in C^3$, which by Poincaré duality are **points** in 3d — appear as vertex insertions $e^{\pm i\sigma}$. Summing over monopole number with fugacity $\zeta$ yields
$$
\boxed{\ S[\sigma] = \int d^3x\ \Big[\frac{e^2}{8\pi^2}(\partial\sigma)^2 \;-\; 2\zeta\cos\sigma\Big].\ }
$$
(The coefficient $e^2/8\pi^2$ is convention-dependent at $O(1)$; what matters is that the dual-photon stiffness $\propto e^2$ and the monopole term is a cosine.) This is 3d **sine-Gordon**, the exact analogue of the vortex sine-Gordon of [[week-03-villain-form-xy-duality|Week 3]] — one dimension up, with monopoles in place of vortices.

### 2.1 The magnetic symmetry [Computed.]

The free part has a shift symmetry
$$
\sigma \to \sigma + c,
$$
whose Noether current is $j^{\text{mag}}_\mu \propto \partial_\mu\sigma \propto \varepsilon_{\mu\nu\rho}F^{\nu\rho}$ — the **magnetic** current, conserved by the Bianchi identity $dF = 0$. This is a genuine global $U(1)$ symmetry of Maxwell theory: the **magnetic 0-form symmetry** in 3d (in Semester II language, the "$U(1)^{(d-2)}$ magnetic symmetry," here $d-2 = 1$... a 1-form symmetry whose charged objects are the 't Hooft lines; in the dual-scalar description it presents as the shift symmetry of $\sigma$). The operator charged under it is the **monopole operator** $e^{i\sigma}$, which inserts one unit of magnetic flux.

**The monopoles explicitly break it.** The term $2\zeta\cos\sigma = \zeta(e^{i\sigma} + e^{-i\sigma})$ is not shift-invariant: proliferating monopoles is exactly turning on an explicit breaking of the magnetic symmetry. Hold this thought — in [[week-10-polyakov-mass-gap-area-law|Week 10]] it is why the would-be Goldstone boson (the photon) is gapped, and in Semester II it is the statement that the magnetic **higher-form symmetry** is explicitly broken by dynamical monopoles.

> **Physical picture.** In the Coulomb (deconfined) phase a photon is the Goldstone boson of a *spontaneously broken* magnetic symmetry — massless, as Goldstone's theorem demands. Monopoles break that symmetry *explicitly*. A Goldstone boson whose symmetry is explicitly broken becomes a pseudo-Goldstone with a mass — and that mass is the photon gap Polyakov computes. The entire confinement mechanism is "the magnetic symmetry is broken explicitly, so the photon is not protected."

## 3. The monopole plasma

Read the same object as a **classical gas**. The monopoles are magnetic charges $q_i = \pm1$ at points $r_i$; expanding $Z$ in powers of the fugacity $\zeta$ (the fugacity expansion of $\cos\sigma$, exactly as in Week 3) gives a **grand-canonical Coulomb gas**:
$$
Z \;\propto\; \sum_{N}\frac{\zeta^N}{N!}\sum_{\{q_i=\pm1\}}\int \prod_i d^3r_i\ \exp\!\Big(-\frac{(2\pi)^2}{2e^2}\sum_{i<j} q_i q_j\, G_3(r_i - r_j)\Big),
$$
with $G_3$ the 3d Coulomb Green function,
$$
G_3(r) = \frac{1}{4\pi |r|}\qquad(-\nabla^2 G_3 = \delta^{(3)}).
$$
So the monopoles interact by a genuine **$1/r$ Coulomb law** (not the 2d logarithm of the vortices) — the 3d massless propagator. The gas is neutral overall ($\sum_i q_i = 0$).

### 3.1 The monopole action and fugacity [Sketched.]

The single-monopole weight is $\zeta \sim e^{-S_{\text{mono}}}$, with the action fixed by the lattice Coulomb self-energy of a unit magnetic charge:
$$
S_{\text{mono}} \sim \frac{c}{e^2 a}\qquad(c = O(1)\ \text{lattice constant}).
$$
At weak coupling ($e^2 a$ small) $S_{\text{mono}}$ is large and monopoles are dilute; at strong coupling they are dense. But — crucially, and unlike 4d — **a 3d gas of instanton points always has more entropy than energy**: the fugacity is nonzero at every coupling, and the plasma is always in a screening phase.

> **Physical picture (why 3d always confines).** A monopole in 3d is a point (an instanton). A dilute gas of points is entropically cheap — there is no line tension to overcome, only a fixed action per point — so monopoles proliferate for any $\zeta > 0$, i.e. at every coupling. The plasma therefore always screens (Debye), always gaps the photon, and always confines. There is **no Coulomb phase** of compact QED₃. Contrast 4d ([[week-11-monopole-condensation-4d|Week 11]]), where the monopole is a worldline with a genuine tension, so a real deconfined phase exists. This is the dimensional fact of Week 8, now a phase-diagram statement.

## 4. What the plasma will do (preview of Week 10)

Two consequences follow from the plasma, both computed next week:

1. **Debye screening → a photon mass.** A plasma of charges screens the Coulomb interaction over a Debye length $m_\gamma^{-1}$; in the dual-scalar language, expanding $\cos\sigma$ around its minimum gives $\sigma$ a mass $m_\gamma \propto \sqrt\zeta \propto e^{-S_{\text{mono}}/2}$. The photon is gapped — exponentially weakly, but nonzero at all couplings.

2. **The Wilson loop becomes a domain wall → an area law.** A Wilson loop is a source that forces $\sigma$ to jump by $2\pi$ across a spanning surface. Minimizing the sine-Gordon energy of that jump gives a domain wall of finite tension, hence $\langle W(C)\rangle \sim e^{-\sigma_{\text{str}}\,\mathrm{Area}(C)}$ — confinement.

## 5. What to take away

1. **Compact QED₃ dualizes to sine-Gordon for the dual photon**, $S = \int[\frac{e^2}{8\pi^2}(\partial\sigma)^2 - 2\zeta\cos\sigma]$ — the Week-3 vortex duality, one dimension up.
2. **The dual photon carries the magnetic symmetry** $\sigma\to\sigma+c$; the monopole operator $e^{i\sigma}$ is charged under it, and the $\cos\sigma$ term is that symmetry **explicitly broken** by dynamical monopoles.
3. **The monopoles are a 3d Coulomb gas** ($1/r$ interaction, fugacity $\zeta \sim e^{-S_{\text{mono}}}$), which in 3d proliferates at every coupling — no Coulomb phase.
4. **The plasma will gap the photon and confine** (Week 10): a mass $\propto e^{-S_{\text{mono}}/2}$ and a Wilson-loop area law.

## 6. Looking ahead: Week 10

Week 10 is the central computational lecture of Semester I. We compute the Debye/photon mass explicitly, then insert a Wilson loop, solve the sine-Gordon domain-wall problem it creates, and extract the string tension — reproducing Polyakov's result that compact QED₃ confines permanently. Every constant will be tracked; this is the calculation the semester is built toward.

## 7. Problem set

**Core problems** (everyone).

**1. The 3d duality in detail.**
Carry out the Week-8 recipe in $d=3$ to obtain $S[\sigma] = \int[\frac{e^2}{8\pi^2}(\partial\sigma)^2 - 2\zeta\cos\sigma]$. Track how the dual-photon stiffness comes out $\propto e^2$ and identify the monopole vertex $e^{i\sigma}$.

**2. The magnetic current.**
Show $j^{\text{mag}}_\mu \propto \varepsilon_{\mu\nu\rho}F^{\nu\rho} \propto \partial_\mu\sigma$ is conserved by the Bianchi identity, that $e^{i\sigma}$ carries one unit of its charge, and that $\cos\sigma$ breaks the symmetry explicitly. Which correlator would be the order parameter for the magnetic symmetry?

**3. The Coulomb gas.**
Derive the grand-canonical Coulomb-gas form of §3 from the fugacity expansion of $\cos\sigma$, and identify the $1/r$ interaction with the 3d massless propagator. Why is the gas neutral?

**Starred problems.**

**4⋆. Monopole self-energy.**
Estimate $S_{\text{mono}}$ from the lattice Coulomb self-energy of a unit magnetic charge and hence $\zeta \sim e^{-S_{\text{mono}}}$. Show $S_{\text{mono}} \sim c/(e^2 a)$ and discuss the weak- and strong-coupling limits.

**5⋆. No Coulomb phase in 3d.**
Argue, from the entropy of a dilute gas of instanton points versus its action, that the monopole fugacity is nonzero at every coupling, so compact QED₃ has no deconfined phase. Contrast the loop energy–entropy balance in 4d (Week 11).

**6⋆⋆ (optional).**
Include a Chern–Simons term $\frac{k}{4\pi}\int a\, da$ and show it gives the dual photon a mass and *gaps the monopoles out* (they become confined), so that for $k\neq0$ compact QED₃ does **not** confine electric charge. Relate this to the fate of the magnetic symmetry when a Chern–Simons term is present. (A preview of the interplay of θ-like terms and confinement, Week 12.)

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block C. Last revised 2026-07-01.*
