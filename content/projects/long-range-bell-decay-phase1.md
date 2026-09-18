---
title: "Draft — Phase 0/1: the β(L) decay law of the vacuum Bell–CHSH violation"
type: project
status: draft-for-review (corrected v2)
parent: long-range-bell-decay-project
target: "IQOQI Open Quantum Problem #12 (Verch)"
modified: 2026-06-19
---

# Decay of the vacuum Bell–CHSH violation with spacelike separation

**Working draft (Phase 0 problem statement + Phase 1 analysis) for [[long-range-bell-decay-project]]. Grounded in the group's own formalism: PRD 108 (2023) 085026 [arXiv:2309.02941] and EPJC 85 (2025) 334 [arXiv:2411.03485].**

> **⚠ Correction (2026-06-19, v2).** The v1 of this note claimed the violation decays at rate $m$ (linear in the cross-correlator). **That was wrong.** The Bell violation is *quadratic* in the residual cross-correlation, so the rate is $2m$, not $m$ — and even that is a *conjectured* sharp rate, not a derived one. The error was treating the leading $L$-dependence as the linear term of the four-Gaussian sum; in fact that linear term does **not** produce a genuine CHSH violation (it is killed by the Horodecki threshold, §4). The exact reorganization in §3 survives; §§4–5 are rewritten. See the companion rebuilt theory sections (`…-theory-v2-sections-3-5.md`).

> **Evidence labels:** `[Exact]`, `[Derived]`, `[Conjectured]`, `[Open]`, `[Stated — ref]`.

---

## 1. Problem statement (Phase 0)

Free real scalar of mass $m$ in $(1+d)$D Minkowski space. For two spacelike-separated regions $\mathcal{O}_A,\mathcal{O}_B$ at separation $L$, define

$$
\beta(L) = \sup\big|\langle 0|\,\mathcal{C}\,|0\rangle\big|,
\qquad
\mathcal{C} = A_1B_1 + A_1B_2 + A_2B_1 - A_2B_2,
$$

over bounded Hermitian $A_i\in\mathcal{A}(\mathcal{O}_A)$, $B_j\in\mathcal{A}(\mathcal{O}_B)$ with $\|A_i\|,\|B_j\|\le1$.

**Known endpoint `[Proved]`.** Summers–Werner: for tangent regions ($L\to0^+$), [[type-iii-von-neumann-algebras|type III$_1$]] + [[rindler-wedges|Reeh–Schlieder]] force $\beta = 2\sqrt2$.

**Open (Verch, OQP #12).** $\beta(L)$ for $L>0$: that $\beta(L)\to2$ as $L\to\infty$, the rate, and — a subtlety surfaced in v2 — whether $\beta(L)>2$ strictly for *all* finite $L$ or terminates at a finite threshold $L_0$.

**The concrete gap.** In arXiv:2411.03485 the separation is not a control variable (Table 1 fixes geometry; isolated violations $\approx2.07$–$2.10$). This note makes $L$ the variable.

---

## 2. Setup and notation

Following arXiv:2309.02941:

- **Lorentz-invariant inner product** (their Eq. 13): $\langle h|h'\rangle = \int \frac{d^dk}{(2\pi)^d}\frac{1}{2\omega_k}\hat h^{*}\hat h'$, $\omega_k=\sqrt{\vec k^2+m^2}$. Symmetric part $H(h,h')=\mathrm{Re}\langle h|h'\rangle$ (smeared Wightman/Hadamard); antisymmetric part the [[pauli-jordan-distribution|Pauli–Jordan]] $\Delta(h,h')=2\,\mathrm{Im}\langle h|h'\rangle$.
- **Microcausality.** Spacelike supports $\Rightarrow \Delta(h,h')=0 \Rightarrow \langle h|h'\rangle = H(h,h')$ real — the Weyl phase drops, correlators are real Gaussians.
- **Weyl operators** ([[weyl-operators]], $\mathcal{A}_h=e^{i\phi(h)}$) with $\langle 0|\mathcal{A}_h|0\rangle = e^{-\frac12\|h\|^2}$, $\|h\|^2\equiv H(h,h)$.
- **Bob via [[tomita-takesaki-modular-theory|modular conjugation]]** $J$: $J\mathcal{A}_hJ=e^{-i\phi(jh)}$, $jh$ in the complementary region. *This modular reflection is what creates the genuine cross-region entanglement — see §4.*
- **Geometry** (arXiv:2411.03485): Alice's [[causal-diamonds|diamond]] carries $f,f'$; Bob's $g,g'$; compact bumps.

---

## 3. The CHSH correlator as a function of $L$ (exact reorganization — unchanged)

The master formula (arXiv:2411.03485, Eq. 17), with $\|f_i+g_j\|^2 = \|f_i\|^2+\|g_j\|^2+2H(f_i,g_j)$:

$$
\langle 0|\mathcal{C}|0\rangle
= e^{-\frac12\|f+g\|^2} + e^{-\frac12\|f'+g\|^2} + e^{-\frac12\|f+g'\|^2} - e^{-\frac12\|f'+g'\|^2}.
\tag{3.1}
$$

Translate Bob's diamond by $L$: self-norms are $L$-independent; only the cross terms move,

$$
\chi_{ij}(L)\equiv H(f_i,\,g_{j,L})
=\iint f_i(x)\,\mathsf{W}(x-y)\,g_j(y-L\hat e)\,d^{D}x\,d^{D}y .
\tag{3.2}
$$

With equal self-norms $\nu$,

$$
\langle 0|\mathcal{C}(L)|0\rangle
= e^{-\nu}\Big[\,e^{-\chi_{11}}+e^{-\chi_{12}}+e^{-\chi_{21}}-e^{-\chi_{22}}\,\Big].
\tag{3.3}
$$

`[Exact within this Weyl family.]` This reorganization is correct and useful — but, as §4 shows, **this particular family (bare Weyl, equal norms) does not by itself produce a violation**; it is not the lower bound.

---

## 4. The decay law (corrected)

**(a) Cluster limit `[Exact]`.** $\chi_{ij}(L)\to0$, so $\langle\mathcal{C}(L)\rangle\to 2e^{-\nu}\le 2$. The construction (3.3) extinguishes — consistent with Verch's claim, but note it tends to $2e^{-\nu}<2$, i.e. *below* the classical bound: this family does not violate at large $L$.

**(b) The linear term is not the violation `[Corrected]`.** Expanding (3.3), $\langle\mathcal{C}(L)\rangle = 2e^{-\nu} - e^{-\nu}X(L)+O(X^2)$ with $X=\chi_{11}+\chi_{12}+\chi_{21}-\chi_{22}$. The v1 note read off "$\beta-2\sim X\sim e^{-mL}$" from this. **This is wrong:** the $L$-independent piece is $2e^{-\nu}<2$, so the linear term must first cover the deficit $2(1-e^{-\nu})$ before any violation appears — and a numerical scan confirms (3.3) never exceeds 2 (exactly as the cos/sin family in the v1 theory draft fails the Horodecki condition $t_1^2+t_2^2>1$). Genuine violation lives in the **correlation-matrix singular-value structure**, $\beta=2\sqrt{t_1^2+t_2^2}$, and is therefore **quadratic** in the residual cross-correlation $c(L)$.

**(c) Quadratic rate `[Conjectured]`.** Writing the surviving violation as $\beta(L)-2 \sim c(L)^2$ with $c(L)$ the cross-region two-point function (3.2), the spacelike asymptotics of $\mathsf{W}$ give

$$
\boxed{\;\beta(L)-2 \ \sim\ C\,e^{-2mL}\ \ (\text{massive}),
\qquad \sim\ C\,L^{-2(d-1)}\ \ (\text{massless},\,d\ge2).\;}
\tag{4.1}
$$

The rate is **$2m$** — twice the mass — because $\beta-2$ is quadratic in a correlator that decays at rate $m$. `[Conjectured — see §5 for the rigorous bound that forces it, and the open lower bound.]`

| Field | $\mathsf{W}(s)$, large spacelike $s$ | $c(L)$ | $\beta-2$ |
|---|---|---|---|
| massive, $d=1$ | $\frac{1}{2\pi}K_0(ms)\sim\frac{e^{-ms}}{2\sqrt{2\pi ms}}$ | $\sim e^{-mL}$ | $\sim e^{-2mL}$ |
| massive, $d\ge2$ | $\sim e^{-ms}/s^{(d-1)/2}$ | $\sim e^{-mL}/L^{(d-1)/2}$ | $\sim e^{-2mL}$ |
| massless, $d\ge2$ | $\sim s^{-(d-1)}$ | $\sim L^{-(d-1)}$ | $\sim L^{-2(d-1)}$ |

---

## 5. The two bounds (corrected: upper bound is the spine)

**Upper bound — rigorous backbone `[Derived modulo standard clustering]`.** Tsirelson/Landau bounds the CHSH supremum by the vacuum maximal correlation $\mathcal{M}(\omega_0;L)=\sup\{|\omega_0(AB)-\omega_0(A)\omega_0(B)|:\|A\|,\|B\|\le1\}$; Buchholz–Wichmann–Yngvason nuclearity gives exponential clustering $\mathcal{M}(\omega_0;L)\le Ce^{-mL}$ (massive). Hence $\beta(L)\to2$, gap-controlled. Under the quadratic Tsirelson form $\beta\le2\sqrt{1+\mathcal{M}^2}$ this sharpens to $\beta(L)-2\le C'e^{-2mL}$ `[Conjectured-leaning]`; the safe rigorous statement is $\beta(L)-2 = O(e^{-mL})$.

**Lower bound — `[Open]`.** No closed-form construction yet achieves $\beta(L)>2$ at finite $L$ with a known $L$-scaling. What is known: (i) tangency $\beta\to2\sqrt2$ `[Proved]`; (ii) numerics $\approx2.07$–$2.10$ at small $L$ `[Numerical, EPJC 85]`; (iii) the equal-norm bare-Weyl family (§4b) and the cos/sin family **do not work**. Open question, sharper than Verch's: does the violation persist for all finite $L$ (tail $\sim e^{-2mL}$), or terminate at a threshold $L_0$ where $t_1^2+t_2^2$ drops below 1? This is the genuine content of the lower bound and the target of the modular-construction computation.

**Massless dichotomy `[Stated]`.** Polynomial clustering (no gap) $\Rightarrow \beta-2\lesssim L^{-2(d-1)}$. *Caveat:* the contrast is **exponential vs. polynomial clustering**, i.e. the *rate*, which tracks the mass gap — not the existence of the split property (which holds for the free massless field in $d\ge3$). The clean punchline survives: **the Bell-violation falloff measures the mass gap.**

---

## 6. Concrete next computations (Phase 1 execution)

1. Build the **modular-conjugation** correlation matrix $T_{ij}(L)$ for two diamonds and compute its singular values $t_1(L),t_2(L)$ — this is the object that actually violates (not (3.3)).
2. Determine whether $t_1(L)^2+t_2(L)^2>1$ for all finite $L$ (tail) or only $L<L_0$ (threshold). This settles the open lower bound.
3. Fit the resulting $\beta(L)-2$ to $e^{-2mL}$ with the existing pipeline (arXiv:2406.20033); sweep $m,d$ (arXiv:2511.20244).
4. Phase 2: make the upper bound (Tsirelson maximal-correlation $\to$ CHSH-pair) rigorous with Verch/Fewster.

---

## References

1. R. Verch, *Bell inequalities for long range vacuum correlations*, IQOQI Open Quantum Problem #12.
2. S. J. Summers, R. Werner, Commun. Math. Phys. **110** (1987) 247; J. Math. Phys. **28** (1987) 2440, 2448.
3. P. De Fabritiis et al., Phys. Rev. D **108** (2023) 085026, arXiv:2309.02941.
4. M. S. Guimarães, I. Roditi, S. P. Sorella, Eur. Phys. J. C **85** (2025) 334, arXiv:2411.03485.
5. M. S. Guimarães, I. Roditi, S. P. Sorella, Phys. Rev. D **112** (2025) 085009, arXiv:2506.00504.
6. P. De Fabritiis et al., Phys. Rev. D **110** (2024) 065006, arXiv:2406.20033.
7. B. S. Cirel'son (Tsirelson), Lett. Math. Phys. **4** (1980) 93; L. J. Landau, Phys. Lett. A **120** (1987) 54.
8. D. Buchholz, E. H. Wichmann, Commun. Math. Phys. **106** (1986) 321.

---

*Draft v2 (corrected), 2026-06-19. The §3 reorganization is exact; the decay rate is $2m$ (conjectured sharp), with the lower bound open. Companion to [[long-range-bell-decay-project]].*
