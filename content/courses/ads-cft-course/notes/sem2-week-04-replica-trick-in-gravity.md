---
title: "Sem II Week 4 — The gravitational replica trick (Lewkowycz–Maldacena)"
type: lecture-notes
course: syllabus
semester: 2
week: 4
block: 1
duration: "3 hours (lecture + seminar)"
status: drafting
modified: 2026-05-28
---

# Sem II Week 4 — The Gravitational Replica Trick (Lewkowycz–Maldacena)

> *Ryu–Takayanagi was stated, not derived, in [[week-13-ryu-takayanagi|Sem I Wk 13]]. This week derives it. Computing $\mathrm{Tr}\,\rho_A^n$ with the gravitational path integral, the dominant bulk saddle is a $\mathbb{Z}_n$-symmetric geometry whose $\mathbb{Z}_n$ quotient carries a **conical defect** along a codimension-2 surface; the $n\to1$ limit localises the action on that surface and **regularity forces it to be the minimal (extremal) surface** — the RT formula falls out. We do the conical-defect computation, check it against the 2d twist-operator result, and state the Dong generalisation. This is the engine reused for replica wormholes in [[sem2-week-10-replica-wormholes|Week 10]].*

## Learning goals

By the end of this week, a student can:

1. Write $\mathrm{Tr}\,\rho_A^n=Z_n/Z_1^n$ and its branched-cover path-integral meaning.
2. Describe the $\mathbb{Z}_n$-symmetric bulk saddle and the conical defect on its quotient.
3. **Derive** $S_A=\mathrm{Area}(\mathcal{C}_1)/4G_N$ from the conical-defect action in the $n\to1$ limit.
4. Show regularity at $n=1$ imposes the extremal-surface equation.
5. State the 2d twist-operator check and the Dong (higher-curvature) generalisation.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Advanced AdS/CFT* §12** — *Quantum Corrections, JLMS, and Replica Methods*; *Black Hole Information* §2 for Rényi entropy, replicas and cosmic branes.
- Lewkowycz, Maldacena, *Generalized gravitational entropy*, [arXiv:1304.4926](https://arxiv.org/abs/1304.4926) — **the anchor**.
- Dong, *Holographic entanglement entropy for general higher derivative gravity*, [arXiv:1310.5713](https://arxiv.org/abs/1310.5713).

**Prerequisites.** [[week-13-ryu-takayanagi]] (RT statement, the AdS$_3$ interval), [[sem2-week-01-holographic-renormalisation-in-depth]] (renormalised bulk action). The QFT replica trick.

**AQFT cross-reference.** None directly; the $n\to1$/von-Neumann limit relates to the relative-entropy framework of AQFT Block B.

## 1. The replica trick, recalled

For a region $A$ in a state $|\Psi\rangle$, $\rho_A=\mathrm{Tr}_{\bar A}|\Psi\rangle\langle\Psi|$, the Rényi entropies are $S_n=\tfrac{1}{1-n}\log\mathrm{Tr}\,\rho_A^n$ and $S_A=\lim_{n\to1}S_n=-\partial_n\mathrm{Tr}\,\rho_A^n|_{n=1}$. In the path integral, $\mathrm{Tr}\,\rho_A^n$ is the partition function on the **$n$-sheeted branched cover** $\mathcal{M}_n$ of Euclidean spacetime, branched over the entangling surface $\partial A$:

$$
\mathrm{Tr}\,\rho_A^n = \frac{Z[\mathcal{M}_n]}{Z[\mathcal{M}_1]^n}.
$$

## 2. The gravitational saddle and its conical defect

Holographically, $Z[\mathcal{M}_n]$ is computed by the dominant **bulk** saddle $\mathcal{B}_n$ that fills in $\mathcal{M}_n$ — a smooth bulk geometry asymptoting to the $n$-sheeted boundary. Assume it inherits the boundary's $\mathbb{Z}_n$ replica symmetry. Pass to the quotient $\hat{\mathcal{B}}_n=\mathcal{B}_n/\mathbb{Z}_n$: a single-sheeted bulk, but with a **conical defect** of opening angle $2\pi/n$ (deficit $2\pi(1-\tfrac1n)$) along the codimension-2 **fixed-point surface** $\mathcal{C}_n$ — the bulk image of $\partial A$. The key point: the geometry is smooth on $\mathcal{B}_n$, so on $\hat{\mathcal{B}}_n$ all curvature beyond the conical tip is regular, and the entropy will be controlled entirely by $\mathcal{C}_n$.

## 3. The Lewkowycz–Maldacena derivation (worked)

Evaluate $\log Z_n=-S_{\rm grav}[\hat{\mathcal{B}}_n]$ (times $n$, accounting for the quotient). The conical defect contributes a localised piece to the Einstein–Hilbert action: a cone of deficit $\delta=2\pi(1-\tfrac1n)$ sources a delta-function curvature $\int\sqrt g\,R\supset 2\delta\cdot\mathrm{Area}(\mathcal{C}_n)$, so

$$
S_{\rm grav}^{\rm conical} = -\frac{1}{16\pi G_N}\int\sqrt g\,R \supset -\frac{1}{16\pi G_N}\,2\cdot 2\pi\Big(1-\tfrac1n\Big)\,\mathrm{Area}(\mathcal{C}_n) = -\frac{(1-\tfrac1n)}{4G_N}\,\mathrm{Area}(\mathcal{C}_n).
$$

Therefore $\log Z_n - n\log Z_1$ has, at the defect, the contribution $-n\cdot S_{\rm grav}^{\rm conical}\sim \tfrac{n-1}{4G_N}\mathrm{Area}(\mathcal{C}_n)$ (to linear order in $n-1$, with $\mathcal{C}_n\to\mathcal{C}_1$). The entropy is the replica derivative:

$$
\boxed{\;S_A = -\partial_n\Big(\log Z_n - n\log Z_1\Big)\Big|_{n=1} = \frac{\mathrm{Area}(\mathcal{C}_1)}{4G_N}.\;}
$$

— **the Ryu–Takayanagi formula, derived.** This is the gravitational analogue of how a 2d CFT twist operator's dimension produces the entanglement entropy.

> **[Sketched]** the LM derivation (the conical-defect action above + the $n\to1$ limit; assumes a $\mathbb{Z}_n$-symmetric, $n$-analytic saddle).

## 4. Regularity ⟹ the extremal-surface equation

What fixes the *location* of $\mathcal{C}_1$? The condition that the bulk geometry $\mathcal{B}_n$ be **smooth** (no conical defect upstairs, on the $n$-fold cover where the geometry is genuinely smooth). Imposing the Einstein equations near the tip of the cone as $n\to1$, the leading constraint is that the **trace of the extrinsic curvature of $\mathcal{C}_1$ vanishes**, $K^{(a)}=0$ — which is exactly the **extremal-area condition** $\delta\,\mathrm{Area}(\mathcal{C})=0$. So:

- the *value* of the entropy is $\mathrm{Area}/4G_N$ (from §3);
- the *surface* is the **extremal/minimal** one (from regularity).

Together these are the full RT/HRT prescription of [[week-13-ryu-takayanagi|Wk 13]]/[[week-14-hrt-and-subregion-subalgebra|Wk 14]], now first-principles (modulo the saddle assumptions). The homology condition arises because $\mathcal{C}_1$ must bound a bulk region together with $A$ (the fixed-point locus of the quotient).

> **[Stated-without-proof]** regularity at $n=1$ ⟹ $K^{(a)}=0$ ⟹ extremal surface (LM; Exercise 3).

## 5. The 2d twist-operator check

In a 2d CFT the same computation is done by **twist operators**. $\mathrm{Tr}\,\rho_A^n$ for an interval $A=[-\ell/2,\ell/2]$ equals the two-point function of twist operators $\sigma_n,\bar\sigma_n$ at the endpoints, which are primaries of total dimension

$$
\Delta_n = \frac{c}{12}\Big(n-\frac1n\Big).
$$

So $\mathrm{Tr}\,\rho_A^n\sim(\ell/\epsilon)^{-2\Delta_n}\cdot\,$wait, $\sim(\ell/\epsilon)^{-\,(c/6)(n-1/n)}$, and

$$
S_n = \frac{1}{1-n}\log\mathrm{Tr}\,\rho_A^n = \frac{c}{6}\,\frac{n-1/n}{n-1}\log\frac{\ell}{\epsilon} = \frac{c}{6}\,\frac{n+1}{n}\log\frac{\ell}{\epsilon}
\xrightarrow{n\to1} \frac{c}{3}\log\frac{\ell}{\epsilon},
$$

reproducing the Calabrese–Cardy / RT result of [[week-13-ryu-takayanagi|Wk 13]]. The twist-operator dimension $\Delta_n$ is the CFT face of the conical-defect action: both are linear in $(n-1)$ near $n=1$ with a coefficient that becomes the entropy. This consistency between the bulk conical defect and the boundary twist operator is a sharp check of the LM logic.

> **[Proven]** the 2d twist-operator computation $S\to(c/3)\log(\ell/\epsilon)$ (given $\Delta_n=\tfrac{c}{12}(n-1/n)$; Exercise 1).

## 6. Continuation in $n$, and higher curvature

Two important caveats/extensions:

- **Analyticity in $n$.** LM assumes the $\mathbb{Z}_n$-symmetric saddle is the dominant one and that the action continues analytically to $n=1$. **This can fail:** other saddles (notably **replica wormholes**, [[sem2-week-10-replica-wormholes|Week 10]]) can dominate, breaking the naive continuation — exactly what produces the Page-curve turnover. The LM derivation is the "disconnected/dominant-saddle" story; replica wormholes are the rest.
- **Higher-curvature gravity (Dong).** For a general diffeomorphism-invariant theory the area is replaced by the **Dong entropy** = Wald entropy + extrinsic-curvature ("anomaly") corrections. E.g. Gauss–Bonnet adds a topological term $\delta S=\tfrac{\alpha}{4G_N}\int_{\mathcal{C}}R[\mathcal{C}]$ (the intrinsic Ricci scalar of the surface). The LM argument extends to any such theory; only the entropy functional changes (Exercise 4).

> **[Stated-without-proof]** the analyticity caveat (replica wormholes, Wk 10) and the Dong formula (1310.5713).

## 7. Key claims and proof status

- **[Sketched]** LM derivation $S_A=\mathrm{Area}(\mathcal{C}_1)/4G_N$ from the conical-defect action (§3).
- **[Stated-without-proof]** regularity ⟹ extremal surface (§4).
- **[Proven]** the 2d twist-operator check $\to(c/3)\log$ (§5).
- **[Stated-without-proof]** $n$-analyticity caveat (replica wormholes) and the Dong formula (§6).

*No coefficients in this note are uncertain. (No `CHECK` items for Wk 4.)*

## 8. What to take away

- $\mathrm{Tr}\,\rho_A^n=Z_n/Z_1^n$ (branched cover); the bulk saddle's $\mathbb{Z}_n$ quotient has a **conical defect** of deficit $2\pi(1-\tfrac1n)$ on $\mathcal{C}_n$.
- **Conical-defect action** gives $S_A=-\partial_n(\log Z_n-n\log Z_1)|_{n=1}=\mathrm{Area}(\mathcal{C}_1)/4G_N$ — **RT, derived**.
- **Regularity** at $n=1$ forces $K^{(a)}=0$, the **extremal-surface** equation — so RT's "minimal surface" is a consequence, not an input.
- **2d check:** twist operators $\Delta_n=\tfrac{c}{12}(n-1/n)$ reproduce $S\to(c/3)\log(\ell/\epsilon)$.
- **Caveats:** the derivation assumes the dominant analytic saddle — **replica wormholes** (Wk 10) are the exception; **Dong** generalises area → Wald + extrinsic corrections.

## Exercises

**Core.**

1. **Twist operators.** For a 2d CFT interval, describe $\mathcal{M}_n$ and show the twist operators have $\Delta_n=\tfrac{c}{12}(n-1/n)$; hence $S_n=\tfrac{c}{6}\tfrac{n+1}{n}\log(\ell/\epsilon)\to\tfrac{c}{3}\log(\ell/\epsilon)$.
2. **Conical action.** Compute the conical-defect contribution to the Einstein–Hilbert action at linear order in $(1-n)$ and obtain $-\partial_n|_{n=1}=\mathrm{Area}(\mathcal{C}_1)/4G_N$.
3. **Extremality from regularity.** Show that demanding smoothness of $\mathcal{B}_n$ at the tip as $n\to1$ gives $K^{(a)}=0$ (vanishing extrinsic-curvature trace), i.e. $\delta\,\mathrm{Area}=0$.

**Starred.**

4. $\star$ **Dong / Gauss–Bonnet.** State the Dong entropy formula; for Gauss–Bonnet in AdS$_5$ compute $\delta S=\tfrac{\alpha}{4G_N}\int_{\mathcal{C}}R[\mathcal{C}]$ for a spherical surface.
5. $\star$ **Modular Hamiltonian.** Relate the conical-defect action to $\delta\langle K\rangle$ and the first law $\delta S=\delta\langle K\rangle$ ([[sem2-week-03-modular-flow-on-subregions|Wk 3]]).

**Project.**

6. **LM in detail.** Read Lewkowycz–Maldacena 1304.4926; reproduce the cosmic-brane/tension-$\to0$ derivation and write a 3-page note connecting it to the replica-wormhole saddle of [[sem2-week-10-replica-wormholes|Wk 10]] (where analyticity fails).

## Connections to other parts of the wiki

- **Within the course.** Derives [[week-13-ryu-takayanagi]] / [[week-14-hrt-and-subregion-subalgebra]]; uses the renormalised action of [[sem2-week-01-holographic-renormalisation-in-depth]]; the analyticity caveat is the [[sem2-week-10-replica-wormholes|replica-wormhole]] story; the first-law link is [[sem2-week-03-modular-flow-on-subregions|Wk 3]].
- **Concepts.** [[replica-trick-gravity]], [[ryu-takayanagi-formula]].
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 1. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*
