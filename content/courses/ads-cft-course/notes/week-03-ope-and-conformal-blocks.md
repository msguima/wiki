---
title: "Week 3 — OPE and conformal blocks"
type: lecture-notes
course: syllabus
semester: 1
week: 3
block: A
duration: "4 hours (2 lectures × 2 hours)"
status: final
modified: 2026-08-25
---

# Week 3 — OPE and Conformal Blocks

> *The first two weeks were representation theory of a single operator. Dynamics enters through the **operator product expansion**: two nearby operators are a convergent sum over the whole spectrum, with coefficients $C_{ijk}$ that — together with the dimensions $(\Delta,\ell)$ — constitute the complete "CFT data." We organise four-point functions into **conformal blocks**, kinematic functions fixed by symmetry (eigenfunctions of the conformal Casimir), times the dynamical squared-OPE-coefficients. Equating the block decompositions in different channels gives the **crossing equation** — the engine of the conformal bootstrap, and the precise statement that Witten diagrams (Week 8) must reproduce on the bulk side.*

## Learning goals

By the end of this week, a student can:

1. Write the CFT OPE and explain that conformal symmetry fixes the position dependence, leaving $C_{ijk}$ as data.
2. State why the OPE converges (radial quantisation; Pappadopulo–Rychkov–Espin–Rattazzi).
3. Define the cross-ratios $(u,v)$ and write a four-point function as prefactor $\times\,G(u,v)$.
4. Define conformal blocks as Casimir eigenfunctions with eigenvalue $\Delta(\Delta-d)+\ell(\ell+d-2)$, and write the block decomposition.
5. Write the crossing equation and explain how it constrains the spectrum (bootstrap preview).

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Modern CFT* §7** — the OPE as an operator algebra, conformal blocks, crossing. Generalised free fields are in §12, not here.
- Simmons-Duffin, *TASI Lectures on the Conformal Bootstrap*, [arXiv:1602.07982](https://arxiv.org/abs/1602.07982), §3 — the canonical treatment of blocks and crossing.
- Dolan, Osborn, *Conformal four point functions and the operator product expansion*, [arXiv:hep-th/0011040](https://arxiv.org/abs/hep-th/0011040) — closed-form blocks in $d=2,4$.

**Prerequisites.** [[week-01-conformal-algebra-and-primaries]] (primaries, $(\Delta,\ell)$, two-/three-point structure) and [[week-02-radial-quantisation-and-state-operator]] (the state-sum that makes the OPE converge).

**AQFT cross-reference.** None for Block A.

**What these notes add.** adscft.org §7 covers the OPE, blocks and the bootstrap; §12 covers generalised free fields. This note adds three things the site treats more briefly: the *convergence* of the OPE stated as the sharp property it is, with the radius made explicit, since this is the single most important structural difference between CFT and ordinary QFT; the Casimir-equation route to blocks, which is what makes them computable rather than merely definable; and the GFF spectrum $\Delta = 2\Delta_\phi + 2n + \ell$ written out, because that list of double-twist operators *is* the free bulk field's Fock space and it is the first thing Week 7 and Week 10 will need.

## 1. The operator product expansion

Two primaries at short separation expand in the full operator spectrum:

$$
\boxed{\;\mathcal{O}_i(x)\,\mathcal{O}_j(0) = \sum_k C_{ijk}\,|x|^{\Delta_k-\Delta_i-\Delta_j}\Big(\mathcal{O}_k(0) + \text{descendants}\Big).\;}
$$

Conformal symmetry fixes everything *except* the numbers $C_{ijk}$: the power of $|x|$ is set by dimensions, and the descendant tail (the $\partial\mathcal{O}_k$ terms) is fixed by conformal invariance once the leading coefficient is known. Moreover $C_{ijk}$ is exactly the **three-point coefficient**: inserting the OPE into $\langle\mathcal{O}_i\mathcal{O}_j\mathcal{O}_k\rangle$ and using the Week-1 two-point normalisation gives $\langle\mathcal{O}_i(x)\mathcal{O}_j(0)\mathcal{O}_k(y)\rangle \leadsto C_{ijk}$. So

$$
\text{CFT data} = \big\{(\Delta_a,\ell_a),\ C_{abc}\big\}.
$$

Specifying these numbers (subject to the constraints below) specifies the theory.


> **Physical picture.** The OPE in a CFT converges — it has a finite radius, like a Taylor series — whereas the operator product expansion of an ordinary QFT is asymptotic at best. This is not a technical refinement; it is the property that makes the bootstrap possible at all. Convergence means a four-point function can be *exactly* rewritten as a sum over exchanged primaries, so demanding that two different ways of doing the rewriting agree (crossing) is a genuine equation rather than an order-by-order matching. In the bulk the same statement reads: the sum over exchanged operators is the sum over bulk states propagating in the exchange channel, and its convergence is why a Witten diagram can be decomposed into blocks at all (Sem II Wk 2).

## 2. Convergence

The OPE is not an asymptotic expansion — it **converges**. In radial quantisation (Week 2), $\mathcal{O}_i(x)\mathcal{O}_j(0)|0\rangle$ is a state on a sphere of radius $\sim|x|$, expanded in the energy ($=\Delta$) eigenbasis. As long as no other operator insertion lies inside that sphere, the state-sum converges, and Pappadopulo–Rychkov–Espin–Rattazzi ([arXiv:1202.2064](https://arxiv.org/abs/1202.2064)) make this quantitative: the tail of the sum is exponentially suppressed in the dimension of the truncation. This is what lets the bootstrap truncate and bound the spectrum.

> **[Stated — refs.]** OPE convergence (PRER); the proof uses radial quantisation + analyticity of CFT correlators.


> **Physical picture.** The cross-ratios are what survives when the conformal group has moved three of the four points to $0$, $1$ and $\infty$ — which it always can. So a four-point function is a function of where the *fourth* point sits relative to a frame the symmetry has already fixed, and that is genuinely two numbers in any dimension. The bulk reading is direct: the cross-ratios are the invariant kinematics of a two-into-two scattering process in AdS, and their two independent directions are the analogues of Mandelstam $s$ and $t$. When Sem II Wk 2 decomposes an exchange Witten diagram into blocks, it is doing partial-wave analysis in exactly this variable.

## 3. Four-point functions and cross-ratios

With four points, conformal symmetry no longer fixes the correlator completely: there are two independent conformal invariants, the **cross-ratios**

$$
u = \frac{x_{12}^2\,x_{34}^2}{x_{13}^2\,x_{24}^2},\qquad
v = \frac{x_{14}^2\,x_{23}^2}{x_{13}^2\,x_{24}^2},\qquad x_{ij}\equiv x_i-x_j.
$$

For four identical scalars $\phi$ of dimension $\Delta_\phi$, symmetry reduces the correlator to a single function of $(u,v)$:

$$
\langle\phi(x_1)\phi(x_2)\phi(x_3)\phi(x_4)\rangle = \frac{1}{(x_{12}^2\,x_{34}^2)^{\Delta_\phi}}\,G(u,v).
$$

All the dynamics is in $G(u,v)$.


> **Physical picture.** A conformal block is bookkeeping, not dynamics: it packages the contribution of one primary *and its entire infinite tower of descendants* into a single function, using nothing but symmetry. All the dynamics sits in the coefficients multiplying the blocks. The reason blocks are computable is the Casimir trick — the quadratic Casimir of the conformal group acts diagonally on a multiplet, so the block is an eigenfunction of a known differential operator, and one solves an ODE rather than resumming a tower by hand. It is worth appreciating the division of labour this sets up, because the whole bootstrap rests on it: symmetry supplies the basis functions exactly, dynamics supplies only a list of numbers.

## 4. Conformal blocks as Casimir eigenfunctions

Apply the OPE in the **$s$-channel** $(12)(34)$: each exchanged primary $\mathcal{O}$ (and its descendants) contributes a fixed function of $(u,v)$ — the **conformal block** $g_{\Delta,\ell}(u,v)$ — times the squared OPE coefficient:

$$
\boxed{\;G(u,v) = \sum_{\mathcal{O}} C_{\phi\phi\mathcal{O}}^{2}\;g_{\Delta_\mathcal{O},\,\ell_\mathcal{O}}(u,v).\;}
$$

The block is pure kinematics. The cleanest characterisation: the quadratic conformal **Casimir** $\mathcal{C}_2=\tfrac12 L^{AB}L_{AB}$ commutes with all generators, so it acts on the exchanged family by a scalar; the block is its eigenfunction,

$$
\mathcal{C}_2\,g_{\Delta,\ell} = c_2(\Delta,\ell)\,g_{\Delta,\ell},\qquad
\boxed{\;c_2(\Delta,\ell) = \Delta(\Delta-d) + \ell(\ell+d-2).\;}
$$

(The eigenvalue is just $\mathcal{C}_2$ on the $(\Delta,\ell)$ representation — note $\Delta(\Delta-d)$ matches the bulk mass relation $m^2L^2=\Delta(\Delta-d)$ of Week 8, no accident.) Acting with the differential operator $\mathcal{C}_2$ on cross-ratio space turns this into a hypergeometric-type ODE whose solution is the block. In $d=2$ and $d=4$ it closes in elementary form (Dolan–Osborn): in $d=2$, with $u=z\bar z$, $v=(1-z)(1-\bar z)$,

$$
g_{h,\bar h}(z,\bar z) = k_{2h}(z)\,k_{2\bar h}(\bar z) + (z\leftrightarrow\bar z),\qquad
k_\beta(z) = z^{\beta/2}\,{}_2F_1\!\big(\tfrac\beta2,\tfrac\beta2;\beta;z\big),
$$

with $h=\tfrac{\Delta+\ell}{2}$, $\bar h=\tfrac{\Delta-\ell}{2}$.

> **[Sketched]** blocks are Casimir eigenfunctions and the eigenvalue $\Delta(\Delta-d)+\ell(\ell+d-2)$ (Casimir on the family). **[Stated — refs.]** the closed forms (Dolan–Osborn).

## 4b. Generalised free fields and the double-twist spectrum

The one OPE we can write down completely, and the one Weeks 7 and 10 will need. A **generalised free field** $\phi$ of dimension $\Delta_\phi$ is defined by declaring its two-point function to be the conformal one and *all* higher correlators to follow by Wick contraction. It is not free in any Lagrangian sense — there is no boundary equation of motion — but its correlators factorise, which is exactly the large-$N$ statement of Week 7.

What does $\phi\times\phi$ contain? Since every correlator is a sum of products of two-point functions, the only operators that can appear are the identity and the composites built from two $\phi$'s and derivatives. Counting them is straightforward. A composite with $\ell$ symmetrised traceless derivatives carrying spin and $n$ contracted pairs $\Box^n$ has dimension
$$
\Delta_{n,\ell} \;=\; \underbrace{2\Delta_\phi}_{\text{two }\phi\text{'s}} \;+\; \underbrace{2n}_{n\ \Box\text{'s}} \;+\; \underbrace{\ell}_{\ell\ \partial_\mu\text{'s}},
\qquad n,\ell = 0,1,2,\dots
$$
so that
$$
\boxed{\;\phi\times\phi \;=\; \mathbb{1} \;+\; \sum_{n,\ell}\,[\phi\phi]_{n,\ell},\qquad \Delta_{n,\ell}=2\Delta_\phi+2n+\ell.\;}
$$
These are the **double-twist** operators; the name is because the *twist* $\tau = \Delta - \ell = 2\Delta_\phi + 2n$ depends only on $n$, so they organise into towers of fixed twist. Note that for odd $\ell$ the composite vanishes by the symmetry of the two identical $\phi$'s, so only even spins appear.

> **Physical picture.** This spectrum is the boundary image of a *free field in the bulk*. A free bulk field has a Fock space of two-particle states labelled by a radial quantum number and an angular momentum, and $(n,\ell)$ are exactly those two labels; $\Delta_{n,\ell}=2\Delta_\phi+2n+\ell$ is the energy of two particles in AdS with $n$ radial excitations and relative angular momentum $\ell$, in units where the AdS box quantises energies to integers. The degeneracy of the list — every $\Delta$ an exact integer above $2\Delta_\phi$ — is the statement that the two bulk particles do not interact. Switching on $1/N$ (Week 7) lifts the degeneracy, and the *anomalous dimensions* $\gamma_{n,\ell}$ of the double-twists are the boundary measurement of the bulk interaction. This is the mechanism by which a list of boundary numbers encodes bulk dynamics, and it is worth carrying into Week 10 and Sem II Wk 2.

> **[Computed.]** the double-twist spectrum, by counting the operators Wick contraction can produce. **[Stated — refs: adscft.org *Modern CFT* §12.]** that the GFF OPE coefficients are likewise fixed by the contractions.


> **Physical picture.** Crossing is associativity of the OPE, and the reason it has teeth is convergence: both channel expansions are exact, so their equality is an exact equation on the spectrum and OPE coefficients — infinitely many constraints on infinitely many unknowns, but constraints that turn out to be sharp. What makes this remarkable is that no Lagrangian is involved anywhere. The bootstrap takes symmetry, unitarity and associativity and carves out the space of consistent theories directly. For this course the relevant consequence is that a "holographic CFT" will be characterised by *properties of its spectrum* — large $N$, a large gap — rather than by a construction, which is the question Week 7 opens and Sem II never fully closes.

## 5. Crossing and the bootstrap (preview)

The same four-point function can be expanded in the **$t$-channel** $(14)(23)$ instead of the $s$-channel. Associativity of the OPE demands the two give the same answer. For identical scalars this is the **crossing equation**:

$$
\boxed{\;\sum_{\mathcal{O}} C_{\phi\phi\mathcal{O}}^{2}\,\Big[\,v^{\Delta_\phi} g_{\Delta,\ell}(u,v) - u^{\Delta_\phi} g_{\Delta,\ell}(v,u)\,\Big] = 0.\;}
$$

This is a single functional equation constraining the *entire* spectrum $\{(\Delta,\ell)\}$ and OPE coefficients $\{C_{\phi\phi\mathcal{O}}^2\ge 0\}$. The **conformal bootstrap** turns it into numerical bounds: positivity of $C^2$ plus crossing carves out the allowed region of CFT data, famously pinning the 3d Ising model. We only preview this; the point for us is that crossing is the precise non-perturbative content a holographic dual must reproduce (Witten diagrams, Week 8 / Sem II Wk 2).

**Worked example: the generalised free field.** The one four-point function we can write down with no effort is that of a **generalised free field** (GFF) — a scalar $\phi$ of dimension $\Delta_\phi$ whose correlators are *all* Wick contractions of the two-point function. This is exactly the large-$N$ single-trace operator (Week 7), so the example is holographically central. The four-point function is the sum of the three pairings:

$$
\langle\phi(x_1)\phi(x_2)\phi(x_3)\phi(x_4)\rangle
= \frac{1}{x_{12}^{2\Delta_\phi}x_{34}^{2\Delta_\phi}} + \frac{1}{x_{13}^{2\Delta_\phi}x_{24}^{2\Delta_\phi}} + \frac{1}{x_{14}^{2\Delta_\phi}x_{23}^{2\Delta_\phi}}.
$$

Stripping the prefactor $(x_{12}^2 x_{34}^2)^{-\Delta_\phi}$ gives, in cross-ratios,

$$
G(u,v) = 1 + u^{\Delta_\phi} + \Big(\frac{u}{v}\Big)^{\Delta_\phi}.
$$

Decomposing this into $s$-channel conformal blocks identifies the operators exchanged in the $\phi\times\phi$ OPE: besides the identity ($\Delta=0$), an infinite tower of **double-trace** primaries

$$
[\phi\phi]_{n,\ell}\;\sim\;\phi\,\partial^{2n}\partial_{\mu_1}\!\cdots\partial_{\mu_\ell}\phi,\qquad
\Delta_{n,\ell} = 2\Delta_\phi + 2n + \ell,
$$

with $C^2$ determined by matching to $G(u,v)$. The absence of single-trace ($\Delta\ne$ double-trace) operators in this OPE is the hallmark of a GFF, and holographically it is the statement that the bulk dual is a *free* field in AdS (no bulk interactions, hence no new single-trace exchange). Turning on $1/N$ corrections / bulk interactions shifts the double-trace dimensions by **anomalous dimensions** $\gamma_{n,\ell}=O(1/N^2)$ — the CFT face of bulk binding energy (Sem II Wk 2, Witten diagrams). This worked spectrum is the bridge from this week's kinematics to the dynamics of holography.

## 6. Subtleties and fine print

**Convergence has a radius, and it matters.** The OPE of $\mathcal{O}(x)\mathcal{O}(0)$ converges inside the sphere reaching the nearest other insertion. In a four-point function this means the s-channel expansion converges in one region of cross-ratio space and the t-channel in another, with an overlap. Crossing is the statement that the two agree *in the overlap*, and arguments that ignore the domains prove nothing.

**Blocks are not observables.** A conformal block depends on a choice of channel; the four-point function does not. Statements like "the block has a singularity" are statements about the decomposition, not about physics, and the singularity is generally cancelled in the full sum.

**Generalised free fields are free only in the bulk.** A GFF has factorised correlators and a double-twist spectrum, but it is not a free field on the boundary in any Lagrangian sense — there is no boundary equation of motion. It is the $N=\infty$ limit of a genuinely interacting theory (Week 7), and the whole content of $1/N$ corrections is the anomalous dimensions that lift the double-twist degeneracy.

**Four points is where the symmetry stops, not where it fails.** The cross-ratios are conformal invariants, so a four-point function is *constrained* — it is a function of two variables rather than eight. The bootstrap exploits the constraint; it does not work around a loss of symmetry.

## 7. Key claims and proof status

- **[Stated — refs.]** OPE convergence (PRER) — §2.
- **[Proved.]** $C_{ijk}$ = three-point coefficient (§1, from the two-point normalisation).
- **[Sketched]** blocks as Casimir eigenfunctions, eigenvalue $\Delta(\Delta-d)+\ell(\ell+d-2)$ — §4.
- **[Stated — refs.]** Dolan–Osborn closed-form blocks ($d=2,4$) — §4.
- **[Proved.]** crossing equation from OPE associativity (§5); the bootstrap *bounds* are quoted, not derived.

*No coefficients in this note are uncertain. (No `CHECK` items for Wk 3.)*

## 8. What to take away

- The **OPE** $\mathcal{O}_i\mathcal{O}_j=\sum_k C_{ijk}|x|^{\dots}(\mathcal{O}_k+\text{desc.})$ is convergent; $C_{ijk}$ = three-point coefficients = the dynamical CFT data alongside $(\Delta,\ell)$.
- A four-point function is prefactor $\times\,G(u,v)$ in cross-ratios; $G=\sum_\mathcal{O}C^2_{\phi\phi\mathcal{O}}\,g_{\Delta,\ell}(u,v)$.
- **Conformal blocks** are Casimir eigenfunctions, $c_2(\Delta,\ell)=\Delta(\Delta-d)+\ell(\ell+d-2)$; closed-form in $d=2,4$.
- **Crossing** ($s=t$ channel) constrains all CFT data; positivity + crossing = the bootstrap.
- The block eigenvalue's $\Delta(\Delta-d)$ is the same combination as the bulk mass relation — a first whisper of Week 8.

5. **Convergence is the structural difference from ordinary QFT.** The OPE has a finite radius, so a four-point function is *exactly* a sum over exchanged primaries and crossing is a genuine equation rather than an order-by-order match.
6. **The double-twist spectrum $\Delta_{n,\ell}=2\Delta_\phi+2n+\ell$** (§4b, computed) is the boundary image of a free bulk field's two-particle Fock space, with $(n,\ell)$ the radial and angular quantum numbers. Its exact degeneracy says the bulk particles do not interact; $1/N$ lifts it, and the anomalous dimensions measure the bulk coupling.

## Exercises

**Core.**

1. **Free-scalar OPE.** Write $\phi(x)\phi(0)$ for the free scalar in $d=4$ ($\phi\phi\sim|x|^{-(d-2)}\mathbf{1}+\dots$); identify the leading and subleading operators and their dimensions.
2. **Casimir eigenvalue.** Show $\mathcal{C}_2\,g_{\Delta,\ell}=[\Delta(\Delta-d)+\ell(\ell+d-2)]\,g_{\Delta,\ell}$ by acting with $\mathcal{C}_2=\tfrac12 L^{AB}L_{AB}$ on a two-particle radial-quantisation state.
3. **2d block.** Use the Dolan–Osborn form to evaluate $g_{h,\bar h}$ for $h=\bar h=1$ at $z=\bar z=\tfrac12$.

**Starred.**

4. $\star$ **Crossing in free theory.** Write $F_{\Delta,\ell}=v^{\Delta_\phi}g_{\Delta,\ell}(u,v)-u^{\Delta_\phi}g_{\Delta,\ell}(v,u)$ and verify the crossing sum vanishes on the free-boson spectrum.
5. $\star$ **2d Ising.** With $\sigma$ ($\Delta=\tfrac18$) and $\epsilon$ ($\Delta=1$), write the $\sigma\sigma$ OPE and list the blocks in $\langle\sigma\sigma\sigma\sigma\rangle$.

**Project.**

6. **Bootstrap bound.** Read Simmons-Duffin §4; reproduce (numerically or conceptually) how crossing + unitarity bounds the dimension of the leading scalar in the $\phi\times\phi$ OPE. Relate to why a holographic CFT has a large gap to single-trace higher-spin operators (preview of large-$N$, Week 7).

## Connections to other parts of the wiki

- **Within the course.** Builds on [[week-01-conformal-algebra-and-primaries]], [[week-02-radial-quantisation-and-state-operator]]; leads into [[week-04-stress-tensor-and-central-charge]] (the $TT$ OPE defines $c$) and, via the bulk, [[week-08-gkp-witten-formula]] / [[gkp-witten-formula]] (Witten diagrams compute the same OPE data). The Casimir eigenvalue $\Delta(\Delta-d)$ reappears as the bulk mass$^2$.
- **AQFT course cross-reference.** None for Block A.
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block A. Reviewed and approved (status: final). Last revised 2026-05-28.*
