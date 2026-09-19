---
title: "Week 10 — Bulk computations of CFT correlators"
type: lecture-notes
course: syllabus
semester: 1
week: 10
block: B
duration: "4 hours (2 lectures × 2 hours)"
status: drafting
modified: 2026-05-28
---

# Week 10 — Bulk Computations of CFT Correlators

> *We now cash in the dictionary. With the GKP-Witten formula ([[week-08-gkp-witten-formula|Wk 8]]) and holographic renormalisation ([[week-09-holographic-renormalisation|Wk 9]]) in hand, correlators of single-trace operators are computed by **Witten diagrams** — Feynman diagrams in AdS with bulk-to-boundary propagators on external legs and integrated bulk vertices. We compute the two-point function explicitly (confirming the Week-1 $|x|^{-2\Delta}$ form, now with a calculable coefficient), then the three-point function from a cubic bulk vertex (confirming the conformally-fixed structure with an OPE coefficient $C_{123}$ fixed by the bulk coupling). This closes Block B: the boundary "CFT data" $\{(\Delta,\ell),C_{ijk}\}$ of Block A is now computed from bulk geometry and couplings.*

## Learning goals

By the end of this week, a student can:

1. State the Witten-diagram rules (external $K_\Delta$, internal bulk-to-bulk $G_\Delta$, integrated vertices).
2. **Compute** the holographic two-point function via Schwinger parameters and confirm $|x|^{-2\Delta}$.
3. Set up the three-point Witten diagram from a cubic vertex and explain why the bulk integral yields the conformally-fixed form.
4. Relate the OPE coefficient $C_{123}$ to the bulk coupling $\lambda$.
5. Summarise the Block B dictionary end-to-end.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *AdS/CFT Foundations* §7** — Witten diagrams, three-point functions and bulk couplings.
- Freedman, Mathur, Matusis, Rastelli (**FMMR**), [arXiv:hep-th/9804058](https://arxiv.org/abs/hep-th/9804058) — the original two- and three-point Witten-diagram computations.
- Penedones, *TASI lectures on AdS/CFT*, [arXiv:1608.04948](https://arxiv.org/abs/1608.04948) — modern treatment of Witten diagrams and Mellin space.

**Prerequisites.** [[week-08-gkp-witten-formula]] (bulk-to-boundary propagator $K_\Delta$, on-shell action), [[week-09-holographic-renormalisation]] (finite correlators), [[week-01-conformal-algebra-and-primaries]] (the two-/three-point forms being reproduced).

**AQFT cross-reference.** None for Block B.

## 1. Witten-diagram rules

To compute $\langle\mathcal{O}_1\cdots\mathcal{O}_n\rangle$ at tree level in the bulk:

- each **external operator** $\mathcal{O}_i(x_i)$ attaches a bulk-to-boundary propagator $K_{\Delta_i}(w;x_i)$ from the boundary point $x_i$ to a bulk point $w$;
- each **internal line** is a bulk-to-bulk propagator $G_{\Delta}(w,w')$ (the regular solution of $(\Box_w-m^2)G=\delta(w,w')/\sqrt g$);
- each **interaction vertex** (from the bulk action's cubic, quartic, … couplings) is **integrated over all of AdS**, $\int d^{d+1}w\,\sqrt g$.

These are ordinary Feynman rules, with "momentum integrals" replaced by integrals over AdS positions, and external wavefunctions replaced by $K_\Delta$. The diagrams are finite after the Week-9 renormalisation.

## 2. The two-point function (worked)

From the Week-8 on-shell action with $\phi=\int K_\Delta J$, the quadratic piece is $S_{\mathrm{ren}}[J]=-\tfrac12\int d^dx\,d^dy\,J(x)\,\Pi_\Delta(x-y)\,J(y)$, so $\langle\mathcal{O}(x)\mathcal{O}(y)\rangle=\Pi_\Delta(x-y)$. Evaluate $\Pi_\Delta$ from the propagator $K_\Delta=C_\Delta(z/(z^2+x^2))^\Delta$. Use the Schwinger representation

$$
\frac{1}{(z^2+|x|^2)^\Delta} = \frac{1}{\Gamma(\Delta)}\int_0^\infty dt\,t^{\Delta-1}\,e^{-t(z^2+|x|^2)},
$$

do the Gaussian $z$-integral and then the $t$-integral. There is, however, a cleaner route that gives the coefficient directly — read it off from the **response** (normalisable) falloff of $\phi=\int K_\Delta J$, using the dictionary $\langle\mathcal{O}\rangle=(2\Delta-d)\times(\text{coefficient of }z^\Delta)$ from [[week-08-gkp-witten-formula|Week 8]]:

1. At fixed $x\ne y$, expand the propagator as $z\to0$: $K_\Delta(z,x;y)=C_\Delta\big(\tfrac{z}{z^2+|x-y|^2}\big)^\Delta \to C_\Delta\,\dfrac{z^\Delta}{|x-y|^{2\Delta}}$, so its $z^\Delta$ coefficient is $C_\Delta/|x-y|^{2\Delta}$.
2. Hence $\phi$'s $z^\Delta$ coefficient is $C_\Delta\!\int d^dy\,\dfrac{J(y)}{|x-y|^{2\Delta}}$, and
$$
\langle\mathcal{O}(x)\rangle_J = (2\Delta-d)\,C_\Delta\!\int d^dy\,\frac{J(y)}{|x-y|^{2\Delta}}.
$$
3. Differentiate once more in $J$: $\langle\mathcal{O}(x)\mathcal{O}(y)\rangle=\dfrac{\delta\langle\mathcal{O}(x)\rangle_J}{\delta J(y)}$, giving

$$
\boxed{\;\langle\mathcal{O}(x)\mathcal{O}(y)\rangle = \frac{C_\mathcal{O}}{|x-y|^{2\Delta}},\qquad
C_\mathcal{O} = (2\Delta-d)\,C_\Delta = \frac{(2\Delta-d)\,\Gamma(\Delta)}{\pi^{d/2}\,\Gamma(\Delta-\tfrac d2)}.\;}
$$

The power $|x-y|^{-2\Delta}$ is forced by conformal invariance ([[week-01-conformal-algebra-and-primaries|Week 1]]); the bulk computes the *coefficient* $C_\mathcal{O}$ from $\Delta,d$ (and $L$, restored). The Schwinger route gives the same answer the long way; this is the shortcut.

> **[Proven]** $\langle\mathcal{O}\mathcal{O}\rangle\propto\lvert x\rvert^{-2\Delta}$ from the bulk (Schwinger-parameter evaluation; Exercises 1, 3).

## 3. The three-point function (worked sketch)

Add a cubic bulk coupling $\tfrac{\lambda}{3!}\phi_1\phi_2\phi_3$. The leading Witten diagram is a single integrated vertex with three external legs:

$$
\langle\mathcal{O}_1(x_1)\mathcal{O}_2(x_2)\mathcal{O}_3(x_3)\rangle
= -\lambda\int_{\mathrm{AdS}} d^{d+1}w\,\sqrt g\;K_{\Delta_1}(w;x_1)\,K_{\Delta_2}(w;x_2)\,K_{\Delta_3}(w;x_3).
$$

The AdS integral can be done (translate the vertex to the "origin" using an isometry, then a Schwinger/Symanzik star-triangle evaluation). The coordinate dependence comes out **exactly** as the conformally-fixed three-point structure of [[week-01-conformal-algebra-and-primaries|Week 1 §4]],

$$
\langle\mathcal{O}_1\mathcal{O}_2\mathcal{O}_3\rangle = \frac{C_{123}}{|x_{12}|^{\Delta_1+\Delta_2-\Delta_3}|x_{23}|^{\Delta_2+\Delta_3-\Delta_1}|x_{13}|^{\Delta_1+\Delta_3-\Delta_2}},
$$

with the OPE coefficient fixed by the bulk coupling and a standard ratio of Gamma functions (FMMR):

$$
C_{123} \;\propto\; \lambda\;\Gamma\!\Big(\tfrac{\Delta_1+\Delta_2+\Delta_3-d}{2}\Big)\,
\frac{\Gamma(\tfrac{\Delta_1+\Delta_2-\Delta_3}{2})\,\Gamma(\tfrac{\Delta_2+\Delta_3-\Delta_1}{2})\,\Gamma(\tfrac{\Delta_1+\Delta_3-\Delta_2}{2})}{\Gamma(\Delta_1)\Gamma(\Delta_2)\Gamma(\Delta_3)}.
$$

So the **dynamical** CFT datum $C_{123}$ — undetermined by symmetry in Block A — is computed here from a bulk coupling. This is the deepest consistency check of the dictionary at tree level: conformal symmetry fixes the *form*, and the bulk fixes the *coefficient*, matching the bootstrap structure of [[week-03-ope-and-conformal-blocks|Week 3]]. Four-point functions add **exchange** Witten diagrams (an internal $G_\Delta$ line), which decompose into conformal blocks plus contact terms — the subject of Sem II Wk 2.

> **[Sketched]** the three-point integral evaluates to the conformal form (star-triangle; FMMR). The exact Gamma-function coefficient is standard (FMMR eq. (5.x)); we quote its structure rather than re-derive it.

**Worked example: the four-point function and the exchange diagram.** Four-point functions are the first to carry dynamical information beyond OPE coefficients. With a quartic bulk vertex $\tfrac{\mu}{4!}\phi^4$, the **contact** Witten diagram is a single integrated vertex with four legs,

$$
A_{\rm contact}(x_i) = -\mu\int_{\rm AdS} d^{d+1}w\,\sqrt g\;\prod_{i=1}^4 K_{\Delta}(w;x_i) = \frac{D_{\Delta\Delta\Delta\Delta}(x_i)}{(\text{prefactor})},
$$

a standard **$D$-function** of the cross-ratios. With cubic couplings instead, the **exchange** diagram has two vertices joined by a bulk-to-bulk propagator $G_{\Delta_p}(w,w')$ — the regular solution of $(\Box_w-m_p^2)G_{\Delta_p}(w,w')=\delta(w,w')/\sqrt g$, which in AdS depends only on the geodesic/chordal distance and behaves as $G_{\Delta_p}\sim (\text{chordal})^{-\Delta_p}$ at short distance:

$$
A_{\rm exch}(x_i) = \int\! d^{d+1}w\,d^{d+1}w'\,\sqrt{g}\sqrt{g'}\;K_\Delta(w;x_1)K_\Delta(w;x_2)\,G_{\Delta_p}(w,w')\,K_\Delta(w';x_3)K_\Delta(w';x_4).
$$

Decomposing $A_{\rm exch}$ into $s$-channel [[week-03-ope-and-conformal-blocks|conformal blocks]] yields the block of the **exchanged single-trace** operator $\mathcal{O}_p$ (dimension $\Delta_p$) *plus* an infinite tower of **double-trace** blocks $[\mathcal{O}\mathcal{O}]_{n,\ell}$ — precisely the GFF tower of [[week-03-ope-and-conformal-blocks|Week 3 §5]] / [[week-07-large-n-and-thooft-limit|Week 7]], now acquiring $O(1/N^2)$ **anomalous dimensions** $\gamma_{n,\ell}$ from the bulk interaction. So a bulk contact/exchange interaction is read on the boundary as: (i) the exchanged operator's contribution, and (ii) a shift in the binding energies of two-particle states — the holographic content of "$1/N^2$ = bulk interactions." The systematic technology (split representation, Mellin amplitudes) is [[sem2-week-02-witten-diagrams|Sem II Wk 2]].

> **[Sketched]** contact = $D$-function; exchange = single-trace block + double-trace tower with $O(1/N^2)$ anomalous dimensions (cf. Week 3 GFF). The bulk-to-bulk propagator's short-distance behaviour $\sim(\text{chordal})^{-\Delta_p}$ is standard.

## 4. The Block B dictionary, assembled

Block B built the holographic dictionary end-to-end:

| Week | Ingredient |
|---|---|
| 6 | **Bulk geometry**: AdS, isometry $\mathrm{SO}(d,2)$ = boundary conformal group; $z$ = RG scale |
| 7 | **Large $N$**: planar dominance, single-trace = GFF, $G_N\sim1/N^2$; type III$_1$ |
| 8 | **GKP-W**: $Z_{\mathrm{CFT}}[J]=Z_{\mathrm{grav}}[\phi_\partial\to z^{d-\Delta}J]$; $\Delta(\Delta-d)=m^2L^2$ |
| 9 | **Renormalisation**: counterterms, FG expansion, $\langle T_{\mu\nu}\rangle$, anomaly $c=3L/2G$ |
| 10 | **Correlators**: Witten diagrams give $\langle\mathcal{O}\mathcal{O}\rangle\propto\lvert x\rvert^{-2\Delta}$ and $C_{123}(\lambda)$ |

The Block A "CFT data" $\{(\Delta,\ell),C_{ijk}\}$ is now produced from bulk masses, couplings, and geometry. **Block C** turns to physical probes: Wilson loops, finite temperature / black holes, and entanglement entropy (Ryu–Takayanagi) — the bridge to the Semester II quantum-information and black-hole-information material.

## 5. Key claims and proof status

- **[Proven]** holographic two-point function $\propto|x|^{-2\Delta}$ (Schwinger evaluation, §2).
- **[Sketched]** three-point contact diagram → conformal form with $C_{123}(\lambda)$ (star-triangle / FMMR, §3).
- **[Stated-without-proof]** loop-level / exchange diagrams harder; Sem II Wk 2 (§3 end).

*No coefficients in this note are uncertain at the level stated; the exact FMMR Gamma-coefficient for $C_{123}$ is quoted structurally and attributed, not re-derived.*

## 6. What to take away

- **Witten diagrams:** external $K_\Delta$, internal $G_\Delta$, vertices integrated over AdS — Feynman rules in AdS.
- **Two-point** (worked, Schwinger): $\langle\mathcal{O}\mathcal{O}\rangle=C_\mathcal{O}|x|^{-2\Delta}$, coefficient computed from $\Delta,d,L$.
- **Three-point** (cubic vertex): conformally-fixed form with $C_{123}\propto\lambda\times$(Gamma ratio) — the bulk computes the **dynamical** OPE coefficient.
- Symmetry fixes the *form*, the bulk fixes the *coefficient*: the dictionary reproduces and computes the Block A CFT data.
- **Block B complete**: geometry → large $N$ → GKP-W → renormalisation → correlators. Block C = probes (Wilson loops, black holes, RT).

## Exercises

**Core.**

1. **Two-point via Schwinger.** For $\Delta=\tfrac d2+1$, substitute two $K_\Delta$ into the on-shell action, use the Schwinger representation, do the $z$- then $t$-integral, and obtain $|x|^{-2\Delta}$.
2. **Three-point setup.** For a cubic vertex $\lambda\phi_1^2\phi_2$, write $\langle\mathcal{O}_1\mathcal{O}_1\mathcal{O}_2\rangle$ as a bulk integral of three $K$'s and identify which factor fixes the coordinate dependence.
3. **Coefficient.** Read off $C_\mathcal{O}$ from Exercise 1 in terms of $\Delta,d,L$ and check it matches the conformal normalisation of [[week-01-conformal-algebra-and-primaries|Week 1]].

**Starred.**

4. $\star$ **Star-triangle.** In AdS$_3$ with $\Delta_1=\Delta_2=\Delta_3=1$, evaluate the three-point bulk integral via the star-triangle identity and express $C_{123}$ in terms of $\lambda$.
5. $\star$ **Exchange diagram.** Set up (not fully evaluate) the four-point exchange Witten diagram with an internal $G_\Delta$; argue it decomposes into the conformal block of the exchanged operator plus double-trace contact terms (cf. [[week-03-ope-and-conformal-blocks|Wk 3]] GFF tower).

**Project.**

6. **Block B synthesis.** Write a 3–4 page synthesis tracing one number — say the $\langle\mathcal{O}\mathcal{O}\mathcal{O}\rangle$ coefficient — from a bulk Lagrangian coupling all the way to the boundary CFT datum, citing Wks 6–10. Connect to the bootstrap constraints of [[week-03-ope-and-conformal-blocks|Wk 3]].

## Connections to other parts of the wiki

- **Within the course.** Uses [[week-08-gkp-witten-formula]] and [[week-09-holographic-renormalisation]]; reproduces the correlators of [[week-01-conformal-algebra-and-primaries]] and the OPE/bootstrap data of [[week-03-ope-and-conformal-blocks]]. Closes Block B; **Block C** ([[week-11-wilson-loops]]–[[week-15-jt-gravity-intro]]) turns to probes. Exchange diagrams continue in [[sem2-week-02-witten-diagrams|Sem II Wk 2]].
- **Concepts.** [[gkp-witten-formula]], [[holographic-dictionary]].
- **AQFT course cross-reference.** None for Block B.
- **Area page.** [[gauge-gravity-duality]].

## Block B summary

Block B built the holographic dictionary: the bulk geometry and its $\mathrm{SO}(d,2)$ isometry (Wk 6); the large-$N$ limit that makes the bulk classical and single-trace operators generalised free fields (Wk 7); the GKP-Witten identification and the mass–dimension relation $\Delta(\Delta-d)=m^2L^2$ (Wk 8); holographic renormalisation and the anomaly $c=3L/2G$ (Wk 9); and Witten-diagram computations of two- and three-point functions (Wk 10). The boundary "CFT data" of Block A is now computed from bulk masses, couplings, and geometry. Block C applies the dictionary to physical probes — Wilson loops, black-hole thermodynamics, and entanglement entropy.

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block B. Draft (status: drafting) — pending expert review of physics and depth. Last revised 2026-05-28.*

*End of Sem I Block B.*
