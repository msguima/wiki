---
title: "Week 4 — Stress tensor, central charge, conformal anomalies"
type: lecture-notes
course: syllabus
semester: 1
week: 4
block: A
duration: "4 hours (2 lectures × 2 hours)"
status: final
modified: 2026-08-25
---

# Week 4 — Stress Tensor, Central Charge, Conformal Anomalies

> *The stress tensor is the one operator every CFT must contain — it generates the conformal symmetry itself. This week we treat $T_{\mu\nu}$ as the conserved, traceless, spin-2 primary of dimension $d$, extract the **central charge** $c$ from its self-OPE in 2d, and see that the classical tracelessness $T^\mu_\mu=0$ fails on a curved background: the **conformal (Weyl) anomaly**, with the same coefficient $c$. We end with the RG-monotonicity theorems ($c$-theorem in 2d, $a$-theorem in 4d) that make these coefficients count "degrees of freedom." On the AdS side, $c$ is the Brown–Henneaux central charge $\propto L/G_N$ (Sem II Wk 7).*
>
> *Convention note: the central charge is **defined** unambiguously by the $\langle TT\rangle$ OPE coefficient below. The numerical prefactors of the curved-space trace anomalies depend on the normalisation of $T$ (factors of $2\pi$) and of the curvature invariants; those are flagged `CHECK` rather than asserted in one fixed scheme.*

## Learning goals

By the end of this week, a student can:

1. State that $T_{\mu\nu}$ is the conserved, traceless, dimension-$d$, spin-2 primary, and write the 2d chiral decomposition $T(z),\bar T(\bar z)$.
2. **Define** $c$ via $\langle T(z)T(0)\rangle=(c/2)/z^4$ and compute $c=1$ for the free boson.
3. State the 2d trace anomaly $\langle T^\mu_\mu\rangle=\tfrac{c}{12}R$ and the 4d $a,c$ structure, with the same $c$ as the OPE.
4. Integrate the 2d anomaly on $S^2$ via Gauss–Bonnet.
5. State the $c$-theorem (2d) and $a$-theorem (4d) and what they say about RG flows.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Modern CFT* §4, §10** — the stress tensor and conserved currents in §4; the Weyl anomaly in §10.
- di Francesco, Mathieu, Sénéchal, *Conformal Field Theory*, Ch. 5 — the 2d $TT$ OPE and trace anomaly.
- Polchinski, *String Theory* Vol. 1, §2 — stress tensor and Ward identities.

**Prerequisites.** [[week-03-ope-and-conformal-blocks]] (OPE language); [[week-01-conformal-algebra-and-primaries]] (the $\Delta=d$, $\ell=2$ slot is the stress tensor — Week 1 §5).

**AQFT cross-reference.** None for Block A.

**What these notes add.** adscft.org covers the stress tensor in *Modern CFT* §4 and the Weyl anomaly in §10, in that order and some distance apart. This note puts them together, because they are one subject: the $z^{-4}$ term in the $TT$ OPE, the Schwarzian in the transformation law, the $-c/24$ Casimir energy on the cylinder and the trace anomaly are four faces of the same number. The free-boson contraction and the Schwarzian computation are done here so that $c$ is something the student has produced rather than met.

## 1. The stress tensor as a primary

Every local QFT has a symmetric stress tensor $T_{\mu\nu}$ with $\partial^\mu T_{\mu\nu}=0$ (translation invariance). In a CFT it is additionally **traceless**, $T^\mu{}_\mu=0$ on flat space (scale + special-conformal invariance), and it is the dimension-$d$, spin-2 primary that *saturates* the Week-1 unitarity bound $\Delta\ge\ell+d-2$ at $\ell=2$. It generates the conformal Ward identities: insertions of $T_{\mu\nu}$ in a correlator implement infinitesimal conformal transformations of the other operators.

In **2d** the conservation + tracelessness make $T_{\mu\nu}$ effectively chiral: in complex coordinates $z=x^1+ix^2$, $T_{z\bar z}=T_{\bar z z}=0$ and conservation gives $\partial_{\bar z}T_{zz}=0$. So

$$
T(z)\equiv T_{zz}(z)\ \text{(holomorphic)},\qquad \bar T(\bar z)\equiv T_{\bar z\bar z}(\bar z)\ \text{(antiholomorphic)},
$$

each a function of one variable. This chirality is what makes 2d so powerful (Week 5).


> **Physical picture.** The stress tensor is the one operator every local theory has, because it is the response to varying the metric — so whatever universal data a CFT carries is most likely to be found in its correlators. Conformal symmetry fixes $\langle TT\rangle$ up to a single constant, and that constant is $c$. It is worth noticing how little input this needs: no Lagrangian, no spectrum, just the statement that a conserved traceless spin-2 operator exists. Everything else this week — the anomaly, the Casimir energy, the Cardy formula next week, Brown–Henneaux in Week 9 — is that one number, re-encountered.

## 2. Central charge from the $TT$ OPE

The stress tensor is *not* a primary under the full 2d conformal (Virasoro) symmetry — it transforms with an anomalous (Schwarzian) piece. This shows up in its self-OPE, whose most singular term defines the **central charge**:

$$
\boxed{\;\langle T(z)\,T(0)\rangle = \frac{c/2}{z^4},\qquad
T(z)T(0)\sim \frac{c/2}{z^4} + \frac{2\,T(0)}{z^2} + \frac{\partial T(0)}{z} + \cdots\;}
$$

The $z^{-2}$ and $z^{-1}$ terms are fixed by $T$ being a weight-2 quasi-primary; the $z^{-4}$ term — forbidden for a genuine primary — is the central term, and its coefficient *is* $c$. This definition is convention-fixed and unambiguous.

**Free boson ($c=1$, worked).** Take $T(z)=-\tfrac12\,{:}\partial\phi\,\partial\phi{:}(z)$ with $\langle\partial\phi(z)\partial\phi(0)\rangle=-1/z^2$. Wick-contracting the two normal-ordered bilinears, the fully-contracted (c-number) term is

$$
\langle T(z)T(0)\rangle = \tfrac14\cdot 2\,\langle\partial\phi(z)\partial\phi(0)\rangle^2 = \tfrac12\Big(\!-\tfrac1{z^2}\Big)^2 = \frac{1/2}{z^4}\ \Rightarrow\ c=1.
$$

Similarly $c=\tfrac12$ for a free Majorana fermion and $c=1$ for a free Dirac fermion. The central charge counts (a normalisation of) the field content — it is a "degrees of freedom" measure.

> **[Proved.]** the $TT$ OPE structure and the free-boson $c=1$ (Wick contraction above).

**Worked example: the Schwarzian and the cylinder Casimir energy.** The $z^{-4}$ term means $T$ is *not* a primary: under a holomorphic map $z\to w(z)$ it transforms with an anomalous (Schwarzian) piece,

$$
T'(w) = \Big(\frac{dz}{dw}\Big)^{2} T(z) + \frac{c}{12}\,\{z;w\},
\qquad
\{z;w\} = \frac{z'''}{z'} - \frac{3}{2}\Big(\frac{z''}{z'}\Big)^{2}.
$$

Apply this to the plane→cylinder map $z=e^{w}$ of [[week-02-radial-quantisation-and-state-operator|Week 2]]. Compute the Schwarzian: with $z'=z$, $z''=z$, $z'''=z$, one gets $\{e^w;w\} = 1 - \tfrac32 = -\tfrac12$. Hence the cylinder stress tensor (using $dz/dw = z$, so $(dz/dw)^2 T = z^2 T$) is

$$
T_{\rm cyl}(w) = z^2\,T_{\rm plane}(z) - \frac{c}{24}.
$$

The constant $-c/24$ is the **Casimir energy of the vacuum on the cylinder** $S^1\times\mathbb{R}$ — a direct, measurable consequence of the central charge, and exactly the $-c/24$ shift in $L_0$ that appears in the torus partition function and the Cardy formula (Week 5). So $c$ is not only the $\langle TT\rangle$ coefficient; it is the ground-state energy on a circle. (This is also the precise sense in which the vacuum energy shift suppressed in Week 2 §3 is "a Week-4 anomaly effect.")


> **Physical picture.** The central charge is best understood as an obstruction rather than a count. There is no regulator that respects Weyl invariance, and $c$ measures by how much: put the theory on a curved background, and the trace of the stress tensor fails to vanish by a term proportional to $c$ times the curvature. That the same number governs the $z^{-4}$ term of the $TT$ OPE, the Schwarzian in the transformation law, and the $-c/24$ Casimir energy is not a coincidence — each is the anomaly seen through a different map. The "counts degrees of freedom" reading ($c=1$ per boson, $\tfrac12$ per Majorana fermion) is true and useful but is downstream of this: more fields, more failure to regulate Weyl-invariantly. In the bulk, $c$ will turn out to be a *geometric* quantity, $3L/2G_N$ (Week 9), so a boundary anomaly coefficient becomes a bulk length in Newton units — one of the sharpest entries in the whole dictionary.

## 3. The conformal (Weyl) anomaly

Classically $T^\mu{}_\mu=0$; quantum-mechanically, coupling to a curved background metric breaks Weyl invariance and the trace acquires a curvature-dependent expectation value — the **conformal anomaly**.

**2d.** $\langle T^\mu{}_\mu\rangle = \dfrac{c}{12}\,R$, with $R$ the Ricci scalar and the *same* $c$ as in §2, in the curvature convention of [[courses/ads-cft-course/conventions]] where the round sphere has $R>0$. The overall sign and the placement of $2\pi$'s are genuinely convention-dependent in the literature — some references write $c\,R/24\pi$ with $T$ normalised differently — so the course pins one choice and uses it everywhere. This one is fixed by [[week-09-holographic-renormalisation|Week 9]], which *derives* the same coefficient holographically and gets $+c/12$ with $c=3L/2G_N$; anything else here would contradict that derivation.

**4d.** Two independent invariants appear, the Weyl-squared $W^2$ and the Euler density $E_4$:

$$
\langle T^\mu{}_\mu\rangle = \frac{c}{16\pi^2}\,W^2 - \frac{a}{16\pi^2}\,E_4,
$$

defining the $c$- and $a$-anomalies. Free-field values (scheme-dependent): a real scalar has $(a,c)\propto(1/360,\,1/120)$ in the standard normalisation. 

**$S^2$ check.** Integrating the 2d anomaly over a round $S^2$ and using Gauss–Bonnet $\tfrac{1}{4\pi}\!\int\!\sqrt g\,R = \chi(S^2)=2$ gives $\int\!\sqrt g\,\langle T^\mu{}_\mu\rangle \propto c\,\chi$ — the anomaly is topological in 2d, controlled by $c$ times the Euler characteristic.

> **[Stated — refs; 2d coefficient pinned in [[courses/ads-cft-course/conventions]] and derived in [[week-09-holographic-renormalisation|Week 9]].]** the anomaly forms. **[Proved.]** the topological $\propto c\chi$ structure on $S^2$ via


> **Physical picture.** Monotonicity theorems say the anomaly coefficient decreases along renormalisation-group flow, and the reading is that RG flow integrates out degrees of freedom and cannot create them. What matters for this course is *which* coefficient. In $d=2$ there is only $c$ and Zamolodchikov's theorem is clean. In $d=4$ there are two, $a$ and $c$, and only $a$ obeys a theorem (Komargodski–Schwimmer); $c$ can go either way. Getting this backwards is a common error, and it matters holographically because the two are computed by different bulk quantities and coincide only for the most symmetric duals — for $\mathcal{N}=4$ SYM $a=c$, which is why the distinction is invisible in the canonical example and bites as soon as one leaves it.

## 4. RG monotonicity: the $c$- and $a$-theorems

The anomaly coefficients are not just labels — they decrease under renormalisation-group flow, making precise the idea that "RG integrates out degrees of freedom."

- **Zamolodchikov $c$-theorem (2d, 1986):** there is a $c$-function $c(\mu)$ with $\mu\,\partial_\mu c\le 0$, equal to $c_{\rm CFT}$ at fixed points; hence $c_{\rm UV}\ge c_{\rm IR}$. Proof uses positivity of the $\langle TT\rangle$ spectral representation.
- **Komargodski–Schwimmer $a$-theorem (4d, 2011):** the *Euler* ($a$) anomaly is monotone, $a_{\rm UV}\ge a_{\rm IR}$ — **not** $c$. Proof uses a dilaton effective action + dispersion relation.

> **[Stated — refs.]** both theorems (cited).

## 4b. Subtleties and fine print

**$T$ is quasi-primary, not primary.** The $z^{-4}$ term is exactly the failure, and it is why the Schwarzian appears in the finite transformation law. Any argument that treats $T$ as a primary will lose the Casimir energy and therefore Cardy (Week 5).

**$a$ versus $c$ in $d=4$.** Only $a$ obeys a monotonicity theorem. They are equal for $\mathcal{N}=4$ SYM, which is the case the course uses most, so the distinction is easy to forget and easy to get wrong when leaving that example.

**Normalisation of $c$ is a convention with a fixed anchor.** $c=1$ for a free boson fixes it; other normalisations differ by factors that propagate into Brown–Henneaux. When comparing with a reference, check its free-boson value first.

**The anomaly is a statement about the background, not the state.** $\langle T^\mu_{\ \mu}\rangle \propto c\,R$ holds in any state; it is a property of the theory coupled to curvature. Excitation-dependent pieces of $\langle T_{\mu\nu}\rangle$ are separate and do not carry $c$.

**Only even $d$ has a trace anomaly of this type.** In odd $d$ the local trace anomaly vanishes and the analogous RG monotone is the sphere free energy $F$, not an anomaly coefficient. Nothing in this week transfers to odd $d$ unchanged.

## 6. Key claims and proof status

- **[Proved.]** $T$ is the conserved traceless $\Delta=d$, $\ell=2$ primary; 2d chiral split (§1).
- **[Proved.]** $c$ defined by $\langle TT\rangle=(c/2)/z^4$; free boson $c=1$ (§2).
- **[Stated — refs; coefficient fixed by the Week-9 derivation.]** 2d anomaly $\langle T^\mu_\mu\rangle=\tfrac{c}{12}R$, and the 4d $a,c$ structure (§3).
- **[Proved.]** topological $\propto c\chi$ on $S^2$ (Gauss–Bonnet, §3).
- **[Stated — refs.]** $c$-theorem (2d), $a$-theorem (4d) (§4).

### Resolved conventions (Wk 4)

1. **§3 — the 2d trace-anomaly coefficient.** Previously flagged uncertain, and previously written with the *opposite sign* to [[week-09-holographic-renormalisation|Week 9]], which derives it. Resolved 2026-08-25: the course fixes $\langle T^\mu{}_\mu\rangle = \tfrac{c}{12}R$ with the round sphere at $R>0$ and $c=1$ for a free boson, pinned in [[courses/ads-cft-course/conventions]]. Both notes now agree; a different sign elsewhere in the wiki is an error, not a convention.
2. **§3 — 4d free-field $a,c$ values and the $16\pi^2$ normalisation.** Still scheme-dependent and still quoted from the literature rather than derived here. This is a genuine [Stated — refs] item, not an uncertainty: the convention-free content is that $a$ and $c$ are independent in $d=4$ and that only $a$ is monotonic.

The convention-free content of this week — the $(c/2)/z^4$ definition of $c$, the free-boson $c=1$ contraction, the Schwarzian and the $-c/24$ Casimir energy, the topological $S^2$ result, and the RG monotonicity structure — is independent of all of the above.

## 7. What to take away

- $T_{\mu\nu}$: conserved, traceless, $\Delta=d$, $\ell=2$ primary; in 2d it splits into holomorphic $T(z)$ and antiholomorphic $\bar T(\bar z)$.
- **Central charge** defined by $\langle T(z)T(0)\rangle=(c/2)/z^4$; $c=1$ free boson, $\tfrac12$ Majorana.
- **Conformal anomaly:** $\langle T^\mu_\mu\rangle=\tfrac{c}{12}R$ in 2d (same $c$); 4d has independent $a,c$. Prefactors are scheme-dependent (flagged).
- On $S^2$ the 2d anomaly integrates to $\propto c\,\chi$ (Gauss–Bonnet).
- **$c$-theorem** (2d) / **$a$-theorem** (4d): the anomaly decreases UV→IR — a count of degrees of freedom.
- Holographically $c\propto L/G_N$ (Brown–Henneaux; Sem II Wk 7).

5. **$c$ has four faces and they are one number:** the $z^{-4}$ term in $\langle TT\rangle$, the Schwarzian in the transformation law, the $-c/24$ Casimir energy on the cylinder, and the trace anomaly. It is an obstruction to Weyl-invariant regularisation, and the degree-of-freedom count is downstream of that.
6. **In $d=4$ only $a$ obeys a monotonicity theorem, not $c$.** They coincide for $\mathcal{N}=4$ SYM, which is why the distinction is invisible in the canonical example and easy to get wrong outside it.

## Exercises

**Core.**

1. **Ward identity.** Derive $\partial_{\bar z}\langle T(z)\,\mathcal{O}_1\cdots\rangle = -\sum_i \delta^{(2)}(z-z_i)\big[\partial_{z_i}+\tfrac{h_i}{z-z_i}\big]\langle\cdots\rangle$ from $T$ as the metric response.
2. **Free boson $c$.** From $T=-\tfrac12{:}\partial\phi\partial\phi{:}$ and $\langle\partial\phi\partial\phi\rangle=-1/z^2$, reproduce $\langle TT\rangle=(1/2)/z^4$, i.e. $c=1$.
3. **Gauss–Bonnet.** Using $\langle T^\mu_\mu\rangle=\tfrac{c}{12}R$, show $\int_{S^2}\sqrt g\,\langle T^\mu_\mu\rangle\propto c\,\chi(S^2)$; get the proportionality constant in your chosen scheme.

**Starred.**

4. $\star$ **4d ratios.** Look up $a,c$ for a free Dirac fermion and a photon; verify the photon has $a/c\neq1$ and discuss $a/c$ as an interacting-theory diagnostic.
5. $\star$ **Zamolodchikov metric.** Show $g_{ij}=x^{2d}\langle\mathcal{O}_i(x)\mathcal{O}_j(0)\rangle$ reduces at a fixed point to the two-point normalisation, and relate $c$ to $g_{TT}$ in 2d (state the convention).

**Project.**

6. **Holographic $c$.** Anticipate Sem II Wk 7: derive (or read) the Brown–Henneaux $c=3L/2G_N$ and check it matches the 2d anomaly structure here; relate to the RT interval entropy $\tfrac{c}{3}\log(\ell/\epsilon)$ of [[week-13-ryu-takayanagi|Wk 13]].

## Connections to other parts of the wiki

- **Within the course.** Uses [[week-03-ope-and-conformal-blocks]]; the $TT$ OPE here is the input to the **Virasoro algebra** of [[week-05-2d-cft-essentials]]. The central charge reappears in [[week-13-ryu-takayanagi|Wk 13]] (RT interval entropy $\propto c$) and [[sem2-week-07-ads2-ads3-essentials|Sem II Wk 7]] (Brown–Henneaux $c\propto L/G_N$).
- **AQFT course cross-reference.** None for Block A.
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block A. Reviewed and approved (status: final); the `CHECK` items in §5 are scheme-dependent anomaly prefactors to confirm in a later pass. Last revised 2026-05-28.*
