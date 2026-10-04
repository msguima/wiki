---
title: "Sem II Week 9 — Long-Range Entanglement and Error Correction"
type: lecture-notes
course: syllabus
semester: 2
week: 9
block: 3
duration: 4 hours (3 hr lectures + 1 hr seminar)
prerequisites: Sem II Weeks 3, 7 and 8; Semester I Weeks 4, 5 and 7
modified: 2026-10-03
---

# Sem II Week 9 — Long-Range Entanglement and Error Correction

> *[[sem2-week-08-toric-code-solved-to-the-bone|Sem II Week 8]] solved the [[toric-code]]. This week asks what kind of state its ground state is and what its degeneracy is good for. We define long-range entanglement by local-unitary circuits and prove that no shallow circuit prepares a toric-code ground state from a product state; we carry out the Schmidt decomposition across a disk, $S=|\partial A|\ln2-\ln2$, and isolate the constant with the constructions of Kitaev–Preskill and of Levin–Wen, $\gamma=\ln2=\ln\mathcal D$; and we read the ground space as a memory, with logical operators as homology classes, the distance, the planar code, and decoding as a random-bond Ising model. [[sem2-week-10-beyond-z2-quantum-doubles-modular-data-chern-simons|Sem II Week 10]] carries γ to the quantum doubles.*

### How to use this chapter

- **In class:** first hour, the light cone (2.1)–(2.3), the definition (2.4), the theorem (2.5) and the Schmidt decomposition of a group state (3.1)–(3.4); Problem 1. Second hour, the boundary counting (3.5)–(3.8) with Figure 1, Kitaev–Preskill (4.1)–(4.2) with Figure 2 and Table 1, and Levin–Wen (4.3)–(4.4) with Figure 3; Problem 2. Third hour, the distance (5.2)–(5.3), recovery (5.4), the planar code (5.6)–(5.8) with Figure 4, and the random-bond Ising model (6.1)–(6.5) with Figure 5 and §6.3; Problems 3 and 4. The seminar (§8) is Kitaev–Preskill and Levin–Wen.
- **For self-study:** §§3.4, 4.4, 5.4, 6.4–6.5, §9 and Problems 5⋆–7⋆. Mini-calculation 3 (§7) is due at the end of the week; the calculation to do alone is its Sub-task 1.
- **Instructor checkpoint:** two errors recur. One is reading γ off a single region, whose constant depends on the boundary count (F3); even the combinations (4.1) and (4.4) need regions in which no star touches four of them (Problem 2). The other is taking the distance for the threshold (§10, third item).

## 0. Reading

**Primary:** Kitaev, Preskill (KP), *Phys. Rev. Lett.* 96 (2006) 110404 [hep-th/0510092], and Levin, Wen (LW), *Phys. Rev. Lett.* 96 (2006) 110405 [cond-mat/0510613], both in full; Chen, Gu, Wen (CGW), *Phys. Rev. B* 82 (2010) 155138 [arXiv:1004.3835], §§II–V; Dennis, Kitaev, Landahl, Preskill (DKLP), "Topological quantum memory", *J. Math. Phys.* 43 (2002) 4452 [quant-ph/0110143], §§I, III.A–B and IV, eqs. (41)–(43).

**Secondary:** Hamma, Ionicioiu, Zanardi (HIZ), *Phys. Rev. A* 71 (2005) 022315 [quant-ph/0409073]; Bravyi, Kitaev, quant-ph/9811052 (planar codes); Bravyi, Hastings, Verstraete (BHV), *Phys. Rev. Lett.* 97 (2006) 050401 [quant-ph/0603121]. Course: [[sem2-week-08-toric-code-solved-to-the-bone|Sem II Week 8]] §§2–5, 7.2; [[sem2-week-07-spt-phases-group-cohomology-dijkgraaf-witten|Sem II Week 7]] §§4.3, 4.6; [[sem2-week-03-spontaneous-breaking-of-higher-form-symmetries|Sem II Week 3]] §2; [[week-04-bkt-kramers-wannier-disorder|Sem I Week 4]] §3.4; [[week-05-wegner-z2-gauge-theory|Sem I Week 5]] §7.

**Optional research reading:** Honecker, Picco, Pujol (HPP), *Phys. Rev. Lett.* 87 (2001) 047201 [cond-mat/0010143]; Wang, Harrington, Preskill (WHP), *Ann. Phys.* 303 (2003) 31 [quant-ph/0207088]; Bravyi, Hastings, Michalakis (BHM), *J. Math. Phys.* 51 (2010) 093512 [arXiv:1001.0344]; Zou, Haah, *Phys. Rev. B* 94 (2016) 075151 [arXiv:1604.06101]; Preskill, *Lecture Notes*, ch. 9.

**Proof-status labels** as in note-quality-template §4; lattice labels, logical operators and the natural logarithm from [[courses/generalized-symmetries-course/conventions|conventions]] §9. Every entropy, Schmidt spectrum, distance and decoding count was checked by script, with exact ranks over $\mathbb{Z}_2$ or explicit state vectors, named where used.

## 1. Motivation and setting

Week 8 leaves two questions. The first is what distinguishes the toric-code ground state from a paramagnet, when no local order parameter exists ([[week-05-wegner-z2-gauge-theory|Sem I Week 5]]) and the 1-form symmetries of [[sem2-week-03-spontaneous-breaking-of-higher-form-symmetries|Sem II Week 3]] are exact only at the solvable point (Week 8 F5). CGW answer from the wavefunction alone: [[topological-order]] is entanglement that no circuit of bounded depth removes. KP and LW extract a number from it, the constant $-\gamma$ in the entropy of a disk. The second question is how good the degenerate ground space is as a memory, and DKLP answer it with statistical mechanics. The setting and notation are those of Week 8 (3.1)–(3.11): the $L_1\times L_2$ torus, $n=2L_1L_2$ qubits, $N=L_1L_2$ stars, the stabilizer group $\mathcal S$ and the code space $V_{\mathcal S}$.

## 2. Local-unitary circuits and long-range entanglement

### 2.1 Circuits and light cones [Proved.]

Place the qubits at the link midpoints and measure distances with the maximum norm on the torus. Following CGW §V, a layer of range $l$ is a product $U^{(k)}=\prod_iu^{(k)}_i$ of unitaries on disjoint sets of diameter at most $l$, and a circuit of depth $M$ is
$$
U=U^{(M)}\cdots U^{(1)} .\tag{2.1}
$$
In $U^{(k)\dagger}OU^{(k)}$ the factors that miss ${\rm supp}\,O$ cancel against their adjoints, and those that meet it lie within $l$ of it. Iterating over the layers, for $O$ supported on $X$,
$$
{\rm supp}\big(U^\dagger OU\big)\subset N_R(X)\equiv\{\text{qubits within }R\text{ of }X\},\qquad R=Ml,\tag{2.2}
$$
the light-cone radius. For $|\psi\rangle=U|\Omega\rangle$, with $|\Omega\rangle$ a product state, and $O_X$, $O_Y$ at distance greater than $2R$, the conjugated operators have disjoint supports, over which $|\Omega\rangle$ factorizes:
$$
\langle\psi|O_XO_Y|\psi\rangle=\langle\Omega|U^\dagger O_XU\,U^\dagger O_YU|\Omega\rangle=\langle\psi|O_X|\psi\rangle\langle\psi|O_Y|\psi\rangle .\tag{2.3}
$$

### 2.2 Phases and long-range entanglement [Definitions; the gapped-path equivalence Stated — refs: CGW §III.]

CGW §III argue that two gapped ground states are in the same phase exactly when a local-unitary evolution, the quasi-adiabatic continuation of a gapped path of Hamiltonians, relates them, and §V relates such evolutions to circuits of finite depth. Their §IV defines a family $|\psi_L\rangle$ on systems of linear size $L$ to be **short-range entangled** (SRE) if
$$
|\psi_L\rangle=U_L\,|\Omega_L\rangle\tag{2.4}
$$
for product states $|\Omega_L\rangle$ and circuits $U_L$ whose depth and range do not depend on $L$, and **long-range entangled** (LRE) otherwise. All SRE states form one phase, and topological order is a pattern of long-range entanglement. The cluster chain of Week 7 §4.6 is SRE, made by two layers of $CZ$ gates on alternating bonds, and yet a nontrivial SPT: its gates break the symmetry, and its projective class (Week 7 §4.3) cannot change under symmetric circuits (CGW §VI). Without symmetry every injective matrix-product state is SRE (Week 7 §4.3), so one-dimensional gapped states have no topological order.

### 2.3 The toric code is long-range entangled [Model proof.]

The statement concerns every state of the code space:
$$
\boxed{\ \text{if }4R<\min(L_1,L_2)-1,\text{ no state of }V_{\mathcal S}\text{ equals }U|\Omega\rangle\text{ with }|\Omega\rangle\text{ a product state and }U\text{ of light-cone radius }R.\ }\tag{2.5}
$$
Suppose $|\psi\rangle=U|\Omega\rangle\in V_{\mathcal S}$. Let $W=\bar Z_1=W(C_x)$ run along the row $y=0$ and $W'$ along the row $y'=\lfloor L_2/2\rfloor$. The rows bound an annulus $R'$ of plaquettes, so by Week 8 (4.2)
$$
W'=W\prod_{p\in R'}B_p ,\tag{2.6}
$$
and on $V_{\mathcal S}$ the operator $W'$ acts as $W$ and $WW'$ as 1. By (2.2), $P=U^\dagger WU$ and $P'=U^\dagger W'U$ are supported within heights $R$ of 0 and of $y'$, whose cyclic distance $\lfloor L_2/2\rfloor\ge(L_2-1)/2$ exceeds $2R$; the supports are disjoint. With $z=\langle\psi|W|\psi\rangle$,
$$
1=\langle\psi|WW'|\psi\rangle=\langle\Omega|PP'|\Omega\rangle=\langle\Omega|P|\Omega\rangle\langle\Omega|P'|\Omega\rangle=\langle\psi|W|\psi\rangle\langle\psi|W'|\psi\rangle=z^2 .\tag{2.7}
$$
Since $W^2=1$, $\|(W-z)\psi\|^2=1-z^2=0$, and $|\psi\rangle$ is an eigenvector of $\bar Z_1$ with $z=\pm1$. The cuts $U(\tilde C_y)$ through $x=\tfrac12$ and $x=\tfrac12+\lfloor L_1/2\rfloor$, which differ by the stars between them, make it an eigenvector of $\bar X_1$ with eigenvalue $\xi=\pm1$. But $\bar Z_1\bar X_1=-\bar X_1\bar Z_1$ (Week 8 (3.8)), so $z\xi=-\xi z$, a contradiction. ∎

The proof needs only distant homologous copies of two anticommuting logical operators: a shallow circuit can make one nonlocal observable sharp, as $|{\Uparrow}\rangle$ does for every Wilson loop, but not two anticommuting ones (Problem 7⋆ treats the planar code). For Hamiltonian evolution, BHV prove with Lieb–Robinson bounds that creating topological order from a product state takes a time growing with the system size [Stated — refs: BHV].

## 3. The Schmidt decomposition across a disk

### 3.1 Group states [Proved.]

Let $\mathcal G$ be a group of $X$-type Pauli strings and $|{\Uparrow}\rangle$ the state with every $Z=+1$. Distinct elements flip distinct sets of qubits, so
$$
|\Psi_{\mathcal G}\rangle=|\mathcal G|^{-1/2}\sum_{g\in\mathcal G}g\,|{\Uparrow}\rangle\tag{3.1}
$$
is a normalized sum of orthonormal basis states; $|\Omega_{00}\rangle$ of Week 8 (3.11) is (3.1) with $\mathcal G$ generated by the stars, $|\mathcal G|=2^{N-1}$ (there called $G_A$; here $A$ is a region). For complementary sets of qubits $A$, $B$, write $g=g_A\otimes g_B$ and
$$
\mathcal G_A=\{g\in\mathcal G:\ g_B=1\},\qquad \mathcal G_B=\{g\in\mathcal G:\ g_A=1\}.\tag{3.2}
$$
They meet only in 1. With a representative κ in each coset of $\mathcal G_A\mathcal G_B$, every element is uniquely $g=\kappa ab$, $a\in\mathcal G_A$, $b\in\mathcal G_B$, with $g_A=\kappa_Aa_A$ and $g_B=\kappa_Bb_B$, so
$$
|\Psi_{\mathcal G}\rangle=\sum_\kappa\lambda\,|\phi^A_\kappa\rangle|\phi^B_\kappa\rangle,\qquad |\phi^A_\kappa\rangle=\frac{\sum_{a\in\mathcal G_A}\kappa_Aa_A|{\Uparrow}_A\rangle}{|\mathcal G_A|^{1/2}},\quad |\phi^B_\kappa\rangle=\frac{\sum_{b\in\mathcal G_B}\kappa_Bb_B|{\Uparrow}_B\rangle}{|\mathcal G_B|^{1/2}},\quad \lambda^2=\frac{|\mathcal G_A||\mathcal G_B|}{|\mathcal G|}.\tag{3.3}
$$
The $|\phi^A_\kappa\rangle$ are orthonormal: if $\kappa_Aa_A=\kappa'_Aa'_A$, then $g=\kappa a$ and $g'=\kappa'a'$ have equal $A$-parts, $gg'\in\mathcal G_B$, and κ, κ′ lie in one coset; likewise on $B$. So (3.3) is a Schmidt decomposition with $|\mathcal G|/(|\mathcal G_A||\mathcal G_B|)$ equal coefficients, and
$$
S(A)=\ln\frac{|\mathcal G|}{|\mathcal G_A|\,|\mathcal G_B|} ,\tag{3.4}
$$
the result of HIZ for group states.

### 3.2 Boundary-constraint counting [Proved.]

Let $R$ be the $(a+1)\times(b+1)$ rectangle of vertices with corner $(0,0)$, $a\le L_1-2$, $b\le L_2-2$, let $A$ be the links with both ends in $R$ and $B$ the rest (Figure 1). A **boundary star** acts on links of both $A$ and $B$; their set $\partial A$ is the $2(a+b)$ perimeter vertices of $R$. The stars of the $(a-1)(b-1)$ interior vertices $R^\circ$ lie in $\mathcal G_A$ and those outside $R$ in $\mathcal G_B$, so every element of $\mathcal G$ is $\big(\prod_{v\in\Sigma}A_v\big)ab$ with $\Sigma\subset\partial A$: the cosets are labelled by subsets of boundary stars, at most $2^{|\partial A|}$. One relation holds, since the product of the stars of $R$ is $X$ on the links with one end in $R$, all in $B$:
$$
\prod_{v\in R}A_v\in\mathcal G_B\qquad\Longrightarrow\qquad \prod_{v\in\partial A}A_v=\prod_{v\in R^\circ}A_v\prod_{v\in R}A_v\in\mathcal G_A\mathcal G_B .\tag{3.5}
$$
There is no other. Write $\prod_{v\in\alpha}A_v=X(\delta\alpha)$, δα being the links with exactly one end in α. If $\prod_{v\in\Sigma}A_v=X(\delta\alpha_a)X(\delta\alpha_b)$ with $\delta\alpha_a\subset A$, $\delta\alpha_b\subset B$, then $1_\Sigma+\alpha_a+\alpha_b$ is constant. Now $\alpha_a$ is constant along the links of $B$, which connect $\partial A$ with the outside, and $\alpha_b$ along the links of $A$, which connect $R$; so $1_\Sigma$ is constant on $\partial A$, and Σ is empty or all of $\partial A$. There are $2^{|\partial A|-1}$ cosets and
$$
\boxed{\ S(A)=|\partial A|\ln2-\ln2=(2a+2b-1)\ln2 .\ }\tag{3.6}
$$
For any bipartition the same reasoning gives $|\mathcal G_A|=2^{N-|V(\Gamma_B)|+c(\Gamma_B)-1}$, where $\Gamma_B$ is the graph of the links of $B$ with their endpoints and $c$ counts components (α is constant on each component of $\Gamma_B$ and free elsewhere, α and its complement giving one element); with the same for $\mathcal G_B$ and $|V(\Gamma_A)|+|V(\Gamma_B)|-N=|\partial A|$, the state $|\Omega_{00}\rangle$ has
$$
S(A)=\big(|\partial A|-c(\Gamma_A)-c(\Gamma_B)+1\big)\ln2 .\tag{3.7}
$$
A disk has $c=1$ twice; an annulus has $c(\Gamma_B)=2$ and two disjoint disks $c(\Gamma_A)=2$, both giving $|\partial A|-2$. Checks: the spectrum of $\rho_A$ computed from the $2^{15}$ configurations of $|\Omega_{00}\rangle$ on the $4\times4$ torus for $a=b=2$ has 128 eigenvalues, all $\frac1{128}$; the $3\times3$ and $3\times4$ tori give 8 and 32 equal eigenvalues for $(a,b)=(1,1)$ and $(1,2)$; and (3.10) below reproduces (3.7) on 300 random bipartitions of the $5\times4$ torus.

```
                  │               │               │
       ───────────◆═══════════════◆═══════════════◆───────────
                  ║               ║               ║
                  ║               ║               ║
       ───────────◆═══════════════●═══════════════◆───────────
                  ║               ║               ║
                  ║               ║               ║
       ───────────◆═══════════════◆═══════════════◆───────────
                  │               │               │
      ═ ║ : the 12 links of A     ─ │ : the 12 links of B touching R
      ◆ : the 8 boundary stars    ● : the interior star, in 𝒢_A
```
**Figure 1. The disk for $a=b=2$. The product of the nine stars of $R$ is $X$ on the twelve thin links, all in $B$, the single relation (3.5); $S(A)=(8-1)\ln2$.**

### 3.3 The Gauss-law reading [Proved.]

The ground state $|\Omega_{++}\rangle=\frac12\sum_s|\Omega_{s_1s_2}\rangle$, with $\bar X_1=\bar X_2=1$, is (3.1) with $X$ and $Z$ exchanged: the plaquette group acting on the state with every $X=+1$, the electric loop gas of [[week-07-kogut-susskind-hamiltonian|Sem I Week 7]] §8. Lemma (3.4) with plaquettes, cut by the boundary at the $2(a+b)$ outside plaquettes adjacent to the perimeter, gives (3.6) again, and the labels acquire a meaning. Let $\pi_v$ be the parity of the string links of $A$ at the boundary star $v$; since $A_v=1$ makes string degrees even, it is also the parity of strings leaving $R$ at $v$. Each link of $A$ has both ends in $R$ and interior degrees are even, so for a configuration $c$
$$
\sum_{v\in\partial A}\pi_v\equiv\sum_{v\in R}\deg_A(v)=2|c\cap A|\equiv0\pmod2 :\tag{3.8}
$$
the electric flux out of a charge-free disk is even, and the labels are the $2^{|\partial A|-1}$ even boundary patterns.

> **Physical picture.** Each cut star carries one bit, whether a string crosses the boundary there, and Gauss's law integrated over the disk removes one bit. That constraint lives on the whole boundary, no single star sees it, and it is the entire $-\ln2$ of (3.6) [exact for the toric code; its survival in the phase is §4.4].

### 3.4 Every ground state, and a second derivation [Proved.]

A stabilizer state on $n$ qubits is fixed by a group $\mathcal S_\psi$ of $2^n$ Pauli strings (here stars, plaquettes and two logical operators), and $|\psi\rangle\langle\psi|=2^{-n}\sum_{s\in\mathcal S_\psi}s$ by Week 8 (2.2). Tracing out $B$ kills every $s$ with a nontrivial factor on $B$, Pauli strings being traceless, and gives ${\rm tr}_Bs=2^{|B|}s_A$ on the subgroup $(\mathcal S_\psi)_A$ supported in $A$:
$$
\rho_A=2^{-|A|}\sum_{s\in(\mathcal S_\psi)_A}s=\frac{|(\mathcal S_\psi)_A|}{2^{|A|}}\,\Pi_A ,\tag{3.9}
$$
with $\Pi_A$ the projector onto the joint $+1$ eigenspace of $(\mathcal S_\psi)_A$, of dimension $2^{|A|}/|(\mathcal S_\psi)_A|$. So every Rényi entropy equals the von Neumann one,
$$
S(A)=\big(|A|-\log_2|(\mathcal S_\psi)_A|\big)\ln2 .\tag{3.10}
$$
For the disk, $|A|=2ab+a+b$, and $(\mathcal S_\psi)_A$ is generated by the $ab$ plaquettes inside $R$ and the $(a-1)(b-1)$ stars of $R^\circ$: the counting of §3.2 and its dual exclude other stabilizers, and no logical operator fits in a disk. Thus $S=(2ab+a+b-ab-(a-1)(b-1))\ln2$, (3.6) again, in every stabilizer ground state. For superpositions, the lemma of Week 8 §7.2 gives $\Pi O\Pi\in\{0,\pm\Pi\}$ for Pauli strings $O$ in $A$, so ${\rm tr}(\rho_AO)$ is the same on all of $V_{\mathcal S}$, and so is $\rho_A$: a disk cannot tell the ground states apart. Check: ranks over $\mathbb{Z}_2$ give (3.6) in $|\Omega_{00}\rangle$, $|\Omega_{++}\rangle$ and $|1\rangle_x$ of Week 8 (5.3) for disks up to $a=b=4$ on the $8\times8$ torus and $(a,b)=(5,3)$ on the $10\times9$ torus.

## 4. The topological entanglement entropy

### 4.1 The constant and the boundary

KP, eqs. (1)–(3): for a disk with smooth boundary of length $L\gg\xi$ in a gapped two-dimensional medium, $S=\alpha L-\gamma+\cdots$, with α nonuniversal, $\gamma=\ln\mathcal D$ and $\mathcal D^2=\sum_ad_a^2$ over the superselection sectors. For the toric code $\mathcal D=2$ (Week 8 §4.2), and KP note that $\gamma=\ln2$ had been found by HIZ. (3.6) has this form, and the combinations below isolate γ by cancelling the boundary terms identically (F3).

### 4.2 Kitaev–Preskill [Proved for the toric code.]

KP divide a disk into regions $A$, $B$, $C$ meeting at a point, with exterior $D$ (their Fig. 1), and form their eq. (5),
$$
S_{\rm topo}=S_A+S_B+S_C-S_{AB}-S_{BC}-S_{AC}+S_{ABC}.\tag{4.1}
$$
With $\alpha L-\gamma$ for each region the interface lengths cancel and the constants give $-3\gamma+3\gamma-\gamma=-\gamma$. On the lattice let $T(v)\subset\{A,B,C,D\}$ be the regions containing links of the star $v$; then $v\in\partial X$ exactly when $T(v)$ meets $X$ and its complement. Table 1 tallies the signs $\epsilon_X=\pm1$ of (4.1) over the regions with $v\in\partial X$.

| $T(v)$ | regions $X$ with $v\in\partial X$ | $\sum\epsilon_X$ |
|---|---|---|
| one region | none | 0 |
| $\{A,D\}$ | $A$, $AB$, $AC$, $ABC$ | $1-1-1+1=0$ |
| $\{A,B\}$ | $A$, $B$, $AC$, $BC$ | $1+1-1-1=0$ |
| $\{A,B,D\}$ | $A$, $B$, $AB$, $AC$, $BC$, $ABC$ | $1+1-1-1-1+1=0$ |
| $\{A,B,C\}$ | all except $ABC$ | $3-3=0$ |
| $\{A,B,C,D\}$ | all seven | $+1$ |

**Table 1. One star's contribution to $\sum_X\epsilon_X|\partial X|$; other cases follow by permuting $A$, $B$, $C$.**

If every region of (4.1) and its complement are connected, so that $c=1$ throughout (3.7), and no star touches all four regions, then $\sum_X\epsilon_X|\partial X|=0$, $\sum_X\epsilon_X=1$, and
$$
S_{\rm topo}=\sum_X\epsilon_X\big(|\partial X|-1\big)\ln2=-\ln2,\qquad\boxed{\ \gamma=\ln2=\ln\mathcal D .\ }\tag{4.2}
$$
All regions lie in one disk, so by §3.4 every ground state gives the same values. Check (Figure 2): on the $16\times16$ torus, with the disk of links with both ends in the vertex square $3\le x,y\le13$, $A$ its links with midpoint $x<8.25$, $B$ the remaining ones with midpoint $y>8.25$ and $C$ the rest, (3.10) gives $(S_A,S_B,S_C,S_{AB},S_{BC},S_{AC},S_{ABC})=(29,18,19,39,29,38,39)\ln2$, each $|\partial X|-1$, and $S_{\rm topo}=-\ln2$ in $|\Omega_{00}\rangle$, $|\Omega_{++}\rangle$ and $|1\rangle_x$. A star where four regions meet adds $\ln2$ (Problem 2).

```
                                  D
          ┌──────────────────────○──────────────────────┐
          │                      │           B          │
          │           A          ●──────────────────────○
          │                      │           C          │
          └──────────────────────○──────────────────────┘
```
**Figure 2. The regions of the check: the disk $ABC$ cut by $x=8.25$ and, to its right, by $y=8.25$; ● joins $A$, $B$, $C$, and ○ are the junctions with $D$. No star touches four regions.**

### 4.3 Levin–Wen [Proved for the toric code.]

LW take an annulus $A_1$, the annulus cut at the top, $A_2$, cut at the bottom, $A_3$, and cut at both, $A_4$ (Figure 3), and state in their eq. (1) that $(S_1-S_2)-(S_3-S_4)=-\ln\mathcal D^2$, with their $\mathcal D=\sum_id_i^2$ over string types, 2 for the $\mathbb{Z}_2$ string net. $S_1-S_2$ and $S_3-S_4$ are the entropy changes on closing the top cut with the bottom closed and open; with only local correlations they agree. For the toric code, (3.7) gives
$$
S_1=\big(|\partial A_1|-2\big)\ln2,\qquad S_2=\big(|\partial A_2|-1\big)\ln2,\qquad S_3=\big(|\partial A_3|-1\big)\ln2,\qquad S_4=\big(|\partial A_4|-2\big)\ln2 ,\tag{4.3}
$$
with $c(\Gamma_B)=2$ for the annulus and $c(\Gamma_A)=2$ for $A_4$. The stars changed by closing the top cut are the same in $A_2\to A_1$ as in $A_4\to A_3$, and likewise at the bottom, so $|\partial A_1|-|\partial A_2|-|\partial A_3|+|\partial A_4|=0$ and
$$
\boxed{\ (S_1-S_2)-(S_3-S_4)=(-2+1+1-2)\ln2=-2\gamma .\ }\tag{4.4}
$$
LW compute on the honeycomb lattice with each boundary link split in two and find $S_R=(n-j)\log2$ for $n$ split links and $j$ boundary curves; (3.7) is that formula with stars, since $c(\Gamma_A)+c(\Gamma_B)-1$ counts the boundary curves of a planar region. Check: on the $16\times16$ torus, with $A_1$ the links whose midpoint $m$ has $2.2<\|m-(8,8)\|_\infty<5.8$ and the cuts its links with $|m_x-8|<1.2$ above and below the center, $(S_1,S_2,S_3,S_4)=(58,59,59,58)\ln2$, with 60 boundary stars each.

```
        A₁               A₂               A₃               A₄
   ┌─────────┐      ┌───┐ ┌───┐      ┌─────────┐      ┌───┐ ┌───┐
   │ ┌─────┐ │      │ ┌─┘ └─┐ │      │ ┌─────┐ │      │ ┌─┘ └─┐ │
   │ │     │ │      │ │     │ │      │ │     │ │      │ │     │ │
   │ └─────┘ │      │ └─────┘ │      │ └─┐ ┌─┘ │      │ └─┐ ┌─┘ │
   └─────────┘      └─────────┘      └───┘ └───┘      └───┘ └───┘
```
**Figure 3. The Levin–Wen regions: the annulus, cut at the top, at the bottom, and at both.**

> **Physical picture.** A Wilson loop inside the annulus equals the product of the plaquettes it encloses, 1 on every ground state: no $m$ in the hole (Week 8 (4.3)). It lies in $A_1$ and is cut in $A_2$; its definite value is a second Gauss constraint, the flux through the inner boundary even separately from the outer one, which is the extra $-\ln2$ of $S_1$. Away from the solvable point LW use a fattened string operator [Heuristic beyond the toric code].

### 4.4 Why the constant is universal [Stated — refs: KP; LW.]

KP argue that $S_{\rm topo}$ is a topological invariant of the arrangement, since deforming an interface or moving a junction changes the entropies by local amounts that cancel in (4.1), and that it is constant along gapped paths while ξ stays small compared with the regions; their $\gamma=\ln\mathcal D$ comes from topological field theory on a doubled surface, $2S_{\rm topo}=4S_3-3S_4$ for spheres with three and four punctures. LW derive their eq. (1) for all string-net models. (4.2) and (4.4) are exact; γ = ln 2 in the whole toric-code phase rests on these arguments.

## 5. The code: logical operators, distance, recovery

### 5.1 Logical operators are homology classes

Week 8 §3.4 identified the logical group $\mathcal C(\mathcal S)/\langle i,\mathcal S\rangle$ with $H_1\oplus H^1$ of the surface: Wilson loops modulo plaquettes and electric cuts modulo stars. A stabilizer code is an $[\![n,k,d]\!]$ code, with $k$ logical qubits and distance
$$
d=\min\big\{|{\rm supp}\,P|:\ P\in\mathcal C(\mathcal S)\setminus\langle i,\mathcal S\rangle\big\}.\tag{5.1}
$$

### 5.2 The distance [Proved.]

Let $Z(z)$ commute with every star, so that $z$ is a $\mathbb{Z}_2$ 1-cycle, and let $n_x(z)$ count its horizontal links $h(x,y)$ in column $x$. Summing the degrees of $z$ over the vertices $(x+1,y)$, each vertical link of that column contributes 2 and each $h(x,y)$ or $h(x+1,y)$ contributes 1, so
$$
n_x(z)\equiv n_{x+1}(z)\pmod 2 .\tag{5.2}
$$
The common parity is the number of links of $z$ crossed by the dual line $x=\tfrac12$, the commutation sign with $\bar X_1$: $z$ winds in $x$ exactly when it is odd, and then every column contains a link of $z$, $|z|\ge L_1$. A cycle winding in $y$ has a vertical link in every row, $|z|\ge L_2$. The dual argument bounds $X$-type operators, and a nontrivial $X(x)Z(z)$ has weight at least $\max(|x|,|z|)$. The straight loops of Week 8 (3.10) attain the bound:
$$
\boxed{\ d=\min(L_1,L_2):\ \text{the toric code is a }[\![2L_1L_2,\,2,\,\min(L_1,L_2)]\!]\text{ code.}\ }\tag{5.3}
$$
Check: enumerating the cycle spaces of the $3\times3$, $3\times4$, $4\times4$, $4\times5$ and $2\times5$ tori gives minimal weights $(L_1,L_2,L_1+L_2)$ for the classes winding in $x$, in $y$ and in both.

### 5.3 Recovery [Proved.]

The syndrome of a Pauli error $E$ is the set of violated generators, the anyons $E$ creates (Week 8 (4.1)). A decoder applies $R_\sigma$ with the same syndrome; then $R_\sigma E\in\mathcal C(\mathcal S)$, and recovery succeeds when $R_\sigma E\in\langle i,\mathcal S\rangle$. If $R_\sigma$ has minimal weight and $2|E|<d$,
$$
|R_\sigma E|\le|R_\sigma|+|E|\le2|E|<d\qquad\Longrightarrow\qquad R_\sigma E\in\langle i,\mathcal S\rangle\tag{5.4}
$$
by (5.1); combinations of such strings are corrected too, since syndrome measurement projects onto one syndrome. In anyon language the decoder pairs the anyons by strings, and it fails exactly when error and correction strings together form a noncontractible loop, a nontrivial logical operator by Week 8 §3.4.

### 5.4 A protected memory [Proved for Pauli strings; the splitting Sketched in Week 8 §7.2; Stated — refs: BHM.]

For $O$ supported on fewer than $d$ qubits,
$$
\Pi\,O\,\Pi=c(O)\,\Pi :\tag{5.5}
$$
each Pauli string in $O$ either anticommutes with a stabilizer and gives 0, or by (5.1) lies in $\langle i,\mathcal S\rangle$. This extends the statement of §3.4 from disks to every set of fewer than $d$ qubits, and local perturbations split the ground states no earlier than at order $d$, Week 8 (7.4). BHM prove the rigorous form for commuting-projector codes that include the toric code: below a constant perturbation strength the lowest band stays gapped and has width exponentially small in the system size [Stated — refs: BHM].

### 5.5 The planar code: rough and smooth edges [Proved.]

Take vertices $(x,y)$ with $1\le x\le L-1$, $0\le y\le L-1$; horizontal links $h(x,y)$ with $0\le x\le L-1$, $0\le y\le L-1$, those with $x=0$ and $x=L-1$ dangling; vertical links $v(x,y)$ with $1\le x\le L-1$, $0\le y\le L-2$; a star at every vertex and plaquettes $p(x,y)$ for $0\le x\le L-1$, $0\le y\le L-2$. This is the planar code of DKLP §III.B, after Bravyi and Kitaev (Figure 4): the left and right edges are **rough** (dangling links, three-link plaquettes), the top and bottom **smooth** (complete plaquettes, three-link stars). Here $n=L^2+(L-1)^2$, with $L(L-1)$ stars and $L(L-1)$ plaquettes, all independent: $X(\delta\alpha)=1$ forces α constant on the connected vertex graph and zero at the dangling links, and $Z(\partial\beta)=1$ forces β constant and zero on the plaquettes whose boundary links lie on a smooth edge. So
$$
k=L^2+(L-1)^2-2L(L-1)=1,\tag{5.6}
$$
with the logical pair
$$
\bar Z=\prod_{x=0}^{L-1}Z_{h(x,y_0)},\qquad \bar X=\prod_{y=0}^{L-1}X_{h(x_0,y)} ,\tag{5.7}
$$
a $Z$-string from rough edge to rough edge and an $X$-string on the dual line $x=x_0+\tfrac12$ from smooth edge to smooth edge, sharing $h(x_0,y_0)$. The argument of §5.2 holds with the stars of columns $1,\dots,L-1$ relating the $L$ columns of horizontal links, and dually with the plaquettes of each row relating its two rows of horizontal links, so
$$
\boxed{\ \text{the planar code is an }[\![L^2+(L-1)^2,\,1,\,L]\!]\text{ code,}\ }\tag{5.8}
$$
as DKLP state (check: ranks and enumeration for $L=2,3,4$). A $Z$-string ends on a rough edge without creating an $e$, the missing endpoint having no star, and an $X$-string ends on a smooth edge without creating an $m$, as DKLP describe for defects: the edges are condensates in the sense of Week 8 §7.5, and $\bar Z$, $\bar X$ carry $e$ and $m$ between them (Problem 3).

```
               x=0           x=1           x=2
    y=2   ╌╌╌─────────+──────X──────+─────────╌╌╌     smooth edge
                      │             │
    y=1   ╌╌╌─────────+──────X──────+─────────╌╌╌
                      │             │
    y=0   ╌╌╌────Z────+──────✱──────+────Z────╌╌╌     smooth edge
        rough edge                       rough edge
```
**Figure 4. The planar code for $L=3$: nine horizontal links, three dangling (╌) at each rough edge, and four vertical links. $\bar Z$ is $Z$ on the row $y=0$; $\bar X$ is $X$ on the links $h(1,y)$, crossed by the dual line $x=\tfrac32$; ✱ marks $h(1,0)$, which carries both.**

## 6. Decoding as statistical mechanics

### 6.1 The error model

DKLP §IV.A take independent $X$ and $Z$ errors at rate $p$ on each qubit. Every generator is a product of $X$'s or of $Z$'s, so $X$ errors are seen only by plaquettes and decoded separately; we take $X$ errors and perfect syndromes. An error is a set $E$ of links with
$$
{\rm Prob}(E)=p^{|E|}(1-p)^{n-|E|} ;\tag{6.1}
$$
its syndrome $S$ is the set of plaquettes with an odd number of links in $E$, the $m$'s at the ends of $E$ read as a dual chain. A decoder chooses $E'$ with the same syndrome; recovery succeeds when $E\oplus E'$ is a product of stars δα and fails when it is homologous to $\bar X_1$, $\bar X_2$ or $\bar X_1\bar X_2$ (Figure 5). The optimal decoder picks the most probable class given $S$.

```
            v(0)    v(1)    v(2)    v(3)    v(4)    v(5)
         +───────+───────+───────+───────+───────+───────+
         │       │   ■   X       X   ■   │       │       │
         +───────+───────+───────+───────+───────+───────+
           p(0)    p(1)    p(2)    p(3)    p(4)    p(5)
   E = X on v(2), v(3); m's in p(1), p(3)
   E′ = E:                       E ⊕ E′ = ∅               success
   E′ = X on v(4), v(5), v(0), v(1):  E ⊕ E′ ~ X̄₂         failure
```
**Figure 5. One row of plaquettes of the $6\times6$ torus. Both corrections have the syndrome of $E$; the second closes the pair around the torus, and $E\oplus E'$ is the row of vertical links, a representative of $\bar X_2$.**

### 6.2 The random-bond Ising model [the identity Proved; Stated — refs: DKLP §IV.]

Fix $E_0$ with syndrome $S$. The chains with syndrome $S$ in its class are $E=E_0\oplus\delta\alpha$, with α and its complement giving the same chain. Put spins $s_v=(-1)^{\alpha_v}$ on the vertices and $\eta_\ell=-1$ for $\ell\in E_0$, $+1$ otherwise. A link $\ell=\langle uv\rangle$ lies in δα exactly when $s_us_v=-1$, so
$$
[\ell\in E]=\tfrac12\big(1-\eta_\ell\,s_us_v\big).\tag{6.2}
$$
With $e^{-2K}=p/(1-p)$ and $(1-p)e^{-K}=\sqrt{p(1-p)}$,
$$
{\rm Prob}(E)=(1-p)^ne^{-2K|E|}=\big(p(1-p)\big)^{n/2}\exp\Big(K\sum_\ell\eta_\ell s_us_v\Big),\tag{6.3}
$$
and summing over the class,
$$
\boxed{\ {\rm Prob}\big([E_0],S\big)=\tfrac12\big(p(1-p)\big)^{n/2}\,Z_{\rm RBIM}(K;\eta),\qquad Z_{\rm RBIM}(K;\eta)=\sum_s\exp\Big(K\sum_{\ell=\langle uv\rangle}\eta_\ell\,s_us_v\Big).\ }\tag{6.4}
$$
The quenched disorder is the error itself, each bond antiferromagnetic with probability $p$, at the coupling $e^{-2K}=p/(1-p)$: the Nishimori line of the $\pm J$ random-bond Ising model, DKLP's $e^{-2J}=p/(1-p)$. Another class is $E_0\oplus\tilde c$, with $\tilde c$ the column $h(0,y)$ representing $\bar X_1$ or the row $v(x,0)$ representing $\bar X_2$; adding $\tilde c$ reverses the bonds on a seam across the torus, an antiperiodic boundary condition τ:
$$
\frac{{\rm Prob}([E_0\oplus\tilde c]\,|\,S)}{{\rm Prob}([E_0]\,|\,S)}=\frac{Z_{\rm RBIM}(K;\eta\tau)}{Z_{\rm RBIM}(K;\eta)}=e^{-\Delta F},\tag{6.5}
$$
Δ$F$ being the free energy of the domain wall the seam forces. The choice of $E_0$ within its class does not matter, by the gauge symmetry $s_v\to-s_v$, $\eta_\ell\to-\eta_\ell$ on the links at $v$, the move that made the pinned interface of [[week-05-wegner-z2-gauge-theory|Sem I Week 5]] §7.2 independent of its surface; the four classes are the four torus boundary conditions of the Ising model of [[week-04-bkt-kramers-wannier-disorder|Sem I Week 4]] §3.4. Check: on the $3\times3$ torus at $p=0.08$, summing (6.1) over all $2^{18}$ error sets reproduces $\tfrac12(p(1-p))^9Z_{\rm RBIM}$, computed over all $2^9$ spin configurations, to ten digits, in every class, for three choices of $E_0$.

### 6.3 The threshold logic [Sketched; numbers Stated — refs: DKLP; HPP; WHP.]

(i) By (6.5) the optimal decoder fails with probability equal to a disorder average, over η drawn with the error statistics, of the weight of the wrong classes: an average on the Nishimori line. (ii) In the ferromagnetic phase the seam forces a domain wall of length at least $L$, $\Delta F\simeq\sigma L$ for typical η, and failure vanishes as $L\to\infty$; DKLP state that the correct class is then separated from the others by a free energy linear in $L$. (iii) In the paramagnetic phase $\Delta F\to0$, the four classes become equally likely and failure tends to $\tfrac34$. (iv) The threshold is the Nishimori point, where the Nishimori line crosses the phase boundary. The omitted step is the control of the disorder average, the statement that typical and averaged domain-wall free energies scale alike (DKLP §IV.E–G). From the domain-wall free energy computed with transfer matrices, HPP place the Nishimori point at $p_c=0.1094\pm0.0002$, the value DKLP quote as their (41); DKLP compare it with $p=0.1100$, where the rate $1-2H_2(p)$ achievable by codes of this type vanishes, their (42)–(43). The minimum-weight decoder minimizes $|E'|$, the energy, and its threshold is the zero-temperature transition, $p_{c0}=0.1031\pm0.0001$ (WHP).

### 6.4 A threshold exists: a Peierls bound [Proved.]

For the minimum-weight decoder on the $L\times L$ torus, suppose recovery fails. Then $E\oplus E'$ is an even subgraph of the dual lattice with nontrivial class, a union of link-disjoint simple dual cycles of which one, $C$, is noncontractible, so $|C|\ge L$ by (5.3). Since $E'\oplus C$ has the syndrome of $E'$, minimality gives $|E'|\le|E'|-|E'\cap C|+|C\setminus E'|$, and each link of $C$ lies in exactly one of $E$, $E'$, so $C\setminus E'=C\cap E$ and
$$
|C\cap E|\ \ge\ |C\cap E'|\qquad\Longrightarrow\qquad|C\cap E|\ge\tfrac12|C| .\tag{6.6}
$$
A fixed set of ℓ links holds at least ℓ/2 errors with probability $\sum_{k\ge\ell/2}\binom\ell kp^k(1-p)^{\ell-k}\le2^\ell(p(1-p))^{\ell/2}$ for $p\le\tfrac12$, each term being at most $\binom\ell k(p(1-p))^{\ell/2}$. A simple dual cycle of length ℓ is traced by a non-backtracking walk from one of its $L^2$ dual vertices, with at most $4\cdot3^{\ell-1}$ walks from each, so
$$
{\rm Prob}({\rm failure})\le\sum_{\ell\ge L}L^2\,4\cdot3^{\ell-1}\big(4p(1-p)\big)^{\ell/2}=\frac{4L^2}{3}\,\frac{x^L}{1-x},\qquad x=6\sqrt{p(1-p)} ,\tag{6.7}
$$
which vanishes as $L\to\infty$ for $x<1$, that is, $p<\tfrac12\big(1-\sqrt{8/9}\big)=0.0286$. The bound is crude (at $p=0.01$ its right side is $2.9\times10^{-2}$ for $L=21$ and $3.6\times10^{-6}$ for $L=41$); DKLP §V refine such counting with self-avoiding walks.

### 6.5 Faulty measurements: a random-plaquette gauge theory [Stated — refs: DKLP §IV; WHP.]

If each syndrome bit is also wrong with probability $q$, the decoder works with the syndrome history in spacetime: qubit errors are links within time slices, measurement errors links along time, and histories with the same boundary lie in one class when they differ by the boundary of a set of plaquettes. The sum over a class is then a three-dimensional $\mathbb{Z}_2$ gauge theory with quenched random plaquette signs on a Nishimori line, whose confinement–Higgs transition is the threshold. Imperfect syndromes cannot help, so $p_c<0.11$ for every $q>0$; DKLP §V prove $p_c\ge0.0114$ for $p=q$, and WHP find the zero-temperature transition, a lower bound, at $p_{c0}=0.0293\pm0.0002$. The model is Wegner's theory of [[week-05-wegner-z2-gauge-theory|Sem I Week 5]] with random signs, and the memory works in its ordered, deconfined phase; Problem 6⋆ derives the mapping.

## 7. Mini-calculation 3 (hand-in)

### 7.1 Scope

Exact on finite tori, using §§3–5 and the stabilizer formalism of Week 8 §2. Nothing is claimed about the perturbed phase, where γ = ln 2 rests on §4.4, and no numerical input from the literature is used.

### 7.2 Variable dictionary

| symbol | meaning | where |
|---|---|---|
| $A$, $B$ | complementary sets of links | §3.1 |
| $\partial A$, $\lvert\partial A\rvert$ | stars acting on both $A$ and $B$; their number | §3.2 |
| $\mathcal G$; $\mathcal G_A$, $\mathcal G_B$ | the star group; its elements acting only on $A$, only on $B$ | (3.2) |
| $\Gamma_A$, $c(\Gamma_A)$ | the graph of the links of $A$; its number of components | (3.7) |
| $(\mathcal S_\psi)_A$ | stabilizers of $\lvert\psi\rangle$ supported in $A$ | (3.9) |
| $S_{\rm topo}$ | the Kitaev–Preskill combination | (4.1) |
| $d$ | the distance | (5.1) |

### 7.3 Sub-tasks

**Sub-task 1: the Schmidt decomposition, explicitly.** On the $4\times4$ torus, build $|\Omega_{00}\rangle$ as its $2^{15}$ configurations in the $Z$ basis, take $A$ the twelve links with both ends in the vertex square $0\le x,y\le2$ (Figure 1), and compute $\rho_A$ by grouping configurations by their restriction to $B$. Give coset representatives of $\mathcal G/\mathcal G_A\mathcal G_B$ as products of boundary stars and verify (3.3). *Deliverable:* the 128 labels and the spectrum of $\rho_A$. *Checkpoint:* Schmidt rank $128=2^7$, all eigenvalues $\frac1{128}$, $S=7\ln2=4.852030$; on the $3\times3$ torus a single plaquette gives rank 8 and $S=3\ln2=2.079442$.

**Sub-task 2: the constraint across the cut.** For the $a\times b$ disk derive (3.6) by the counting of §3.2, then evaluate (3.10) by hand and show that the counts agree. *Deliverable:* both derivations. *Checkpoint:* $|A|=2ab+a+b$, $\log_2|\mathcal S_A|=ab+(a-1)(b-1)$, $S=(2a+2b-1)\ln2$; for $a=2$, $b=3$, $S=9\ln2=6.238325$.

**Sub-task 3: γ two ways.** On the $16\times16$ torus evaluate (3.10) by ranks over $\mathbb{Z}_2$ for the regions of the checks in §§4.2 and 4.3, in $|\Omega_{00}\rangle$ and in $|1\rangle_x$. *Deliverable:* the eleven entropies, the boundary-star counts and both combinations. *Checkpoint:* $(29,18,19,39,29,38,39)\ln2$ for the seven regions of (4.1), boundary counts one larger, $S_{\rm topo}=-\ln2$; $(58,59,59,58)\ln2$ with 60 boundary stars each, and (4.4); identical in both states, so $\gamma=\ln2$.

**Sub-task 4: the distance.** Prove (5.3), confirm it by enumerating the cycle spaces of the $3\times3$, $3\times4$ and $4\times4$ tori, and repeat for the planar code with $L=3$. *Deliverable:* the proof and the minimal weight in each class. *Checkpoint:* cycle spaces of dimension 10, 13, 17; minimal weights $(L_1,L_2,L_1+L_2)$; $d=3,3,4$. The $L=3$ planar code has 13 qubits, 6 independent stars and 6 independent plaquettes, $k=1$, and minimal $\bar Z$, $\bar X$ of weight 3.

### 7.4 What is proved, modeled and imported

Proved on every finite torus: (3.4), (3.6), (3.7), (3.10), (4.2), (4.4) and (5.3), all counting statements. Computed: the numbers of Sub-tasks 1, 3 and 4. Imported: nothing.

## 8. Seminar: Kitaev–Preskill and Levin–Wen

**Format.** Two presenters, one per four-page paper, in the format of syllabus §7, then a joint discussion. Everyone reads both papers and brings Problem 2.

**Sections.** KP in full: eqs. (1)–(5), Fig. 1, the invariance argument, the doubled-surface computation in outline. LW in full: eq. (1), Figs. 1–3, the toric-code example, the string-net result.

**The technical claim.** A gapped two-dimensional medium has $S=\alpha L-\gamma$ for a disk, $\gamma=\ln\mathcal D$ (KP (1)–(3)); the combination (4.1) cancels α and is a topological invariant and universal (KP); for string-net states $(S_1-S_2)-(S_3-S_4)=-\ln\mathcal D^2$ (LW (1)).

**What it needs from Semester I.** The electric loop gas of [[week-07-kogut-susskind-hamiltonian|Sem I Week 7]] §8 and the $\mathbb{Z}_2$ Gauss law; from Semester II, $\mathcal D$ from Week 8 §4 and §§3–4 of this note.

**The step at the board.** LW's toric-code computation: split the boundary links (their Fig. 3), decompose the loop gas over the even boundary patterns, their eq. (2), obtain $S_R=(n-1)\log2$ and compare with (3.6) and (3.8); then $S_R=(n-j)\log2$ for the four regions, against (4.3).

**For the discussion.** Why KP's regions may meet only at junctions of three (Problem 2); what the annulus knows that a disk does not (§4.3); what a smooth deformation of the Hamiltonian requires on the lattice.

**The open question it leaves for this course.** Neither paper proves that $S_{\rm topo}\neq0$ implies long-range entanglement in the sense of (2.4); spurious constants (F4, Problem 8⋆⋆) make the question real.

**On the course map.** $\mathcal D$ is the total quantum dimension of Week 8 §4.2, which normalizes $S=M/\mathcal D$ in Week 8 (5.5); for Week 10's quantum doubles $\mathcal D=|G|$; LW's strings are the string nets of Week 11.

## 9. Subtleties and fine print

**F1. Cat states.** By (2.3) an SRE state has no connected correlations beyond $2R$, so the GHZ state, a sum of two product states, is LRE. CGW's classification concerns gapped ground states, applied with a degenerate ground space to the states that cluster, here the two product states. (2.5) needs no such choice: it excludes every state of $V_{\mathcal S}$, all of which cluster for local operators by (5.5).

**F2. Ancillas.** CGW let circuits act together with ancillas in a product state, so that systems of different sizes can be compared; the proof of (2.5) is unchanged.

**F3. The constant of one region.** The split of (3.6) into $\ln2$ per star and $-\ln2$ depends on the boundary measure: in terms of the $2(a+b)+4$ links of $B$ touching $R$ the same entropy is $(n_{\rm link}-5)\ln2$, and LW's split links give another count. Only combinations that cancel every boundary term, (4.1) or (4.4), with regions meeting as in Figures 2 and 3, determine γ.

**F4. Spurious constants.** Zou and Haah show that a class of short-range entangled states on a cylinder have Rényi entropies of index α ≥ 2 equal to $aL-\gamma$ with $\gamma>0$, which the usual extrapolation would call topological; the effect is tied to a one-dimensional SPT order that appears after disentangling the spins far from the cut. For stabilizer states, (3.9) makes all Rényi entropies equal, so a spurious constant in one would appear in all.

**F5. Regions that wrap.** (3.7) holds in $|\Omega_{00}\rangle$ for every bipartition, but the entropy of a region containing noncontractible loops depends on the ground state; for a strip around the torus the states $|a\rangle_x$ of Week 8 (5.1) minimize it (Problem 5⋆).

**F6. Away from the fixed point.** In the perturbed code of Week 8 §7 the logical operators become dressed strings of width of order ξ, the splitting is of order $e^{-L/\xi}$ (§5.4), α changes, and γ = ln 2 holds only for large regions (§4.4), while the exact counts of §§3–5 hold at the solvable point.

**F7. Decoder and noise.** The threshold depends on the decoder (0.1094 for the optimal one against 0.1031 for minimum weight, §6.3) and on the noise: decoding $X$ and $Z$ errors separately assumes that they are independent, and correlated noise changes the statistical model.

## 10. Common misconceptions

**"Topological order means a nonzero topological entanglement entropy."** It is tempting because γ is the most quoted diagnostic. Topological order is long-range entanglement, (2.4), proved for the toric code by (2.5); γ is a diagnostic of it, with the caveats of F4.

**"Short-range entangled states are trivial."** It is tempting because without symmetry all SRE states form one phase. With a symmetry imposed they need not be: the cluster chain of §2.2 is SRE and a nontrivial SPT.

**"Distance $L$ means protection only when errors are as rare as $1/L^2$ per qubit."** It is tempting because (5.4) is the only guarantee valid for every error. Distance $L$ guarantees the correction of $\lfloor(L-1)/2\rfloor$ errors placed by an adversary, while a rate $p$ below threshold produces about $2pL^2$ of them, and these are corrected with probability tending to one, (6.7) and §6.3, because they form small clusters.

## 11. Historical note

Kitaev introduced the toric code as a quantum code in 1997, and Bravyi and Kitaev (1998) put codes on lattices with boundary. DKLP (posted October 2001) wrote the fault-tolerance paper behind §§5–6: planar codes with rough and smooth edges, recovery as the random-bond Ising model on the Nishimori line and, with faulty measurements, as a disordered three-dimensional gauge theory, and threshold bounds from self-avoiding walks. HIZ (2004) found the entropy of the toric code to be the boundary length up to an additive constant, which they related to topological order. KP (posted 11 October 2005) and LW (23 October 2005) independently identified the constant as a universal invariant, in back-to-back letters of 2006, KP noting the earlier toric-code value of HIZ. BHV (2006) showed with Lieb–Robinson bounds that topological order cannot be created quickly from a product state, and CGW (2010) made local-unitary equivalence the definition of a gapped phase.

## 12. What to take away

1. **Technical:** a circuit of depth $M$ and range $l$ moves supports by at most $Ml$, (2.2), and SRE means made from a product state by such a circuit, (2.4). **Physical:** such states cannot make two anticommuting nonlocal observables sharp, so the toric code is LRE, (2.5).
2. **Technical:** a group state has $|\mathcal G|/(|\mathcal G_A||\mathcal G_B|)$ equal Schmidt coefficients, (3.4), and a disk has $S=|\partial A|\ln2-\ln2$, (3.6). **Physical:** one bit per cut star, minus the bit fixed by Gauss's law, (3.8).
3. **Technical:** the KP and LW combinations cancel the boundary terms star by star and give $-\ln2$ and $-2\ln2$, (4.2) and (4.4). **Physical:** $\gamma=\ln\mathcal D$ is read from the wavefunction alone.
4. **Technical:** the toric code is $[\![2L_1L_2,2,\min(L_1,L_2)]\!]$ and the planar code $[\![L^2+(L-1)^2,1,L]\!]$. **Physical:** logical operators are homology classes, rough and smooth edges absorb $e$ and $m$, and nothing on fewer than $d$ qubits sees the encoded information, (5.5).
5. **Technical:** decoding classes have random-bond Ising weights on the Nishimori line, (6.4)–(6.5), and a threshold exists, (6.7). **Physical:** the memory is the ordered phase, where a seam around the torus costs free energy proportional to $L$.

## 13. Looking ahead: Sem II Week 10

[[sem2-week-10-beyond-z2-quantum-doubles-modular-data-chern-simons|Sem II Week 10]] passes to $\mathbb{Z}_N$, where §3 gives $\ln N$ per boundary star (Problem 1), and to finite groups, whose quantum doubles have $\mathcal D=|G|$ and so $\gamma=\ln|G|$ by KP's formula; it also compares §5.4 with Wen and Niu. Week 11 reads the loop gas of §3.3 as the simplest string net, with LW's $\mathcal D=\sum_id_i^2$.

## 14. Problem set

*Routing: Problems 1–4 are the classroom core (Problem 2 is brought to the seminar), 5⋆–7⋆ are self-study consolidation, and 8⋆⋆–9⋆⋆ are research extensions.*

### Core problems

**1. The $\mathbb{Z}_N$ toric code** (extends §§3.1–3.2). With the clock and shift of [[courses/generalized-symmetries-course/conventions|conventions]] §§6, 9 and the stars $G_v=\prod_iX_{(v-\hat i,i)}X^\dagger_{(v,i)}$ of Week 8 F4, let $|\Psi\rangle\propto\sum_{g\in\mathcal G}g|0\cdots0\rangle$, $\mathcal G$ generated by the stars and every $Z_\ell=1$ on $|0\cdots0\rangle$. (a) Show that $|\Psi\rangle$ is a ground state and that (3.3)–(3.4) hold, with $gg'^{-1}$ in place of $gg'$ in the orthogonality argument. (b) Show $S(A)=(|\partial A|-1)\ln N$ for the disk of §3.2 and compare γ with $\ln\mathcal D$ for $N^2$ abelian anyons. (c) For $N=3$ on the $3\times3$ torus and $A$ a plaquette, give the number of configurations, the Schmidt rank and $S$.

**2. A star where four regions meet** (extends §4.2). (a) If each region of (4.1) and its complement are connected in the sense of (3.7), show $S_{\rm topo}=(n_4-1)\ln2$, with $n_4$ the number of stars whose links lie in four different regions. (b) On a large torus take the disk of links with both ends in $0\le x,y\le6$; let $C$ be its links with midpoint $y<3$ together with $v(3,3)$, $v(3,4)$, $v(3,5)$, $A$ the remaining links with midpoint $x<3$, and $B$ the rest. Find $n_4$ and $S_{\rm topo}$. (c) Which assumption of KP fails, and how must lattice regions be drawn?

**3. Other patches** (extends §5.5). (a) For the $L_1\times L_2$ patch with rough left and right edges and smooth top and bottom (vertices $1\le x\le L_1-1$, $0\le y\le L_2-1$; horizontal links $0\le x\le L_1-1$, $0\le y\le L_2-1$; vertical links $1\le x\le L_1-1$, $0\le y\le L_2-2$), find $n$, the independent stars and plaquettes, $k$, and the weights of the shortest $\bar Z$ and $\bar X$. (b) For the $(L_1+1)\times(L_2+1)$ grid of vertices with all its links, so that every edge is smooth, find $k$ and explain it with the boundary condensates. (c) Which anyon does each kind of edge absorb, and which string ends on it?

**4. Failure at small error rates** (extends §§5.3, 6.4). $X$ errors at rate $p$ on the $L\times L$ torus, $L$ odd, perfect syndromes, minimum-weight decoder. (a) Show that no error of weight at most $(L-1)/2$ causes failure. (b) Show that an error of weight $w=(L+1)/2$ causes failure exactly when it lies on one of the $2L$ straight dual loops of length $L$, and that the decoder meets no ties at this weight. (c) Conclude ${\rm Prob}({\rm failure})=2L\binom{L}{(L+1)/2}p^{(L+1)/2}+O\big(p^{(L+3)/2}\big)$, evaluate the coefficient for $L=3,5$ and compare with (6.7).

### Starred problems

**5⋆. Cylinder cuts and minimal-entropy states** (extends §3.4, F5 and Week 8 §5). For $A$ the links with both ends in the rows $y=0,1$ of the $L\times L$ torus: (a) by (3.10), $S=(2L-1)\ln2$ in $|\Omega_{s_1s_2}\rangle$, $(2L-2)\ln2$ in $|a\rangle_x$ and $2L\ln2$ in $|a\rangle_y$; (b) $\sum_ac_a|a\rangle_x$ has $S=(2L-2)\ln2-\sum_a|c_a|^2\ln|c_a|^2$; (c) the minimal-entropy states for this cut are the eigenstates of anyon flux along $x$, and the overlaps of the minimal bases of the two cuts give $S$ of Week 8 (5.5). *Hint:* $\bar Z_1$ and $\bar X_2$ have representatives inside $A$ and inside $B$; those in $B$ make ${\rm tr}_B|a\rangle\langle b|$ vanish for $a\neq b$, those in $A$ separate the remaining blocks.

**6⋆. Faulty measurements** (extends §6.2 to §6.5). Let $\Lambda_3$ be the dual lattice of the torus times discrete time, with qubit errors on links within slices (rate $p$) and measurement errors on links along time (rate $q$). Show that chains in one class with a given boundary differ by boundaries of plaquette sets of $\Lambda_3$, and that the probability of a class is proportional to the partition function of a $\mathbb{Z}_2$ gauge theory on the lattice dual to $\Lambda_3$, with plaquette couplings $\eta_PK_P$, $e^{-2K_P}=p/(1-p)$ on time-like and $q/(1-q)$ on space-like plaquettes, η fixed by a reference chain. Identify the gauge invariance and the phase in which the memory works. *Hint:* repeat (6.2)–(6.4) with 2-chains in place of α, and dualize as in [[week-05-wegner-z2-gauge-theory|Sem I Week 5]] §7.1.

**7⋆. The planar code is long-range entangled** (extends §2.3 to §5.5). Adapt (2.5) to the planar code, find the largest light-cone radius it excludes, and explain the difference from the torus. *Hint:* the rows $y=0$ and $y=L-1$ carry homologous $\bar Z$'s whose product is the product of all plaquettes, and they need not wrap.

### ⋆⋆ problems

**8⋆⋆. Spurious topological entropy.** *Known:* KP and LW argue that their combinations equal $-\gamma$ and $-2\gamma$ for regions large compared with ξ; Zou and Haah exhibit short-range entangled states with spurious constants in cylinder Rényi entropies. *Explored:* the conditions on regions under which the KP or LW combination certifies long-range entanglement in the sense of (2.4). *Sources:* KP; LW; CGW §§IV–V; Zou–Haah. *Completion:* a stabilizer state made by a circuit of bounded depth whose KP or LW combination is nonzero for some geometry, verified with (3.10), and a modified geometry or criterion that gives 0 for it and $-\ln2$ for the toric code.

**9⋆⋆. Optimal decoding and the Nishimori point.** *Known:* (6.4)–(6.5); $p_c=0.1094\pm0.0002$ (HPP) and $p_{c0}=0.1031\pm0.0001$ (WHP). *Explored:* finite-size estimates of both thresholds from the failure rates of the two decoders. *Sources:* DKLP §IV; HPP; WHP. *Completion:* the optimal decoder through transfer-matrix values of $Z_{\rm RBIM}(K;\eta\tau)$ for the four classes, the minimum-weight decoder by matching, failure rates with error bars on tori up to $L=16$, and threshold estimates from the crossings, compared with the published values.

## Self-study answer checkpoints

**Problem 1.** *Decisive step:* the elements of $\mathcal G$ are the shifts $X(\delta\alpha)$, $\alpha\in\mathbb{Z}_N^N$, distinct up to a common constant, so they move $|0\cdots0\rangle$ to distinct basis states, and the plaquette holonomies fix $|0\cdots0\rangle$ and commute with the stars; (3.3) uses only that the group acts freely on basis states. In §3.2 the cosets are labelled by α on $\partial A$ modulo a common shift. *Result:* $N^{|\partial A|-1}$ equal coefficients, $S=(|\partial A|-1)\ln N$, $\gamma=\ln N=\ln\mathcal D$ with $\mathcal D^2=N^2$; for $N=3$ and a plaquette, $3^8=6561$ configurations, Schmidt rank 27, $S=3\ln3=3.295837$ (for $N=4$, rank 64). *Common failure:* omitting the relation, which gives $|\partial A|\ln N$.

**Problem 2.** *Decisive step:* only the last row of Table 1 is nonzero, and $\sum_X\epsilon_X=1$ when every $c=1$. *Result:* (a) $S_{\rm topo}=(n_4-1)\ln2$. (b) The star $(3,6)$ has $h(2,6)\in A$, $h(3,6)\in B$, $v(3,5)\in C$, $v(3,6)\in D$ and is the only such star: $n_4=1$, $S_{\rm topo}=0$, with $(S_A,S_B,S_C,S_{AB},S_{BC},S_{AC},S_{ABC})=(11,11,20,19,23,23,23)\ln2$ and every region and complement connected. (c) KP's regions meet along interfaces and at junctions of three, smooth on the scale of ξ; on the lattice no star may touch four regions. *Common failure:* forgetting that this star is a boundary star of all seven regions.

**Problem 3.** *Decisive step:* the independence argument of §5.5, and in (b) the relation $\prod_vA_v=1$, restored because every link now has two endpoints. *Result:* (a) $n=L_1L_2+(L_1-1)(L_2-1)$, $(L_1-1)L_2$ stars and $L_1(L_2-1)$ plaquettes, all independent, $k=1$, shortest $\bar Z$ of weight $L_1$ and $\bar X$ of weight $L_2$; for $(3,4)$, $n=18$ with weights 3 and 4. (b) $n=L_1(L_2+1)+L_2(L_1+1)$, star rank $(L_1+1)(L_2+1)-1$, $L_1L_2$ plaquettes, $k=0$ ($n=24$ for $3\times3$): an $X$-string between smooth edges is the product of the stars on one side, and a $Z$-string has no rough edge to end on. (c) Rough edges absorb $e$, where $Z$-strings end; smooth edges absorb $m$, where dual $X$-strings end. *Common failure:* missing the relation in (b), which gives $k=-1$.

**Problem 4.** *Decisive step:* by (6.6) failure needs a noncontractible $C\subset E\oplus E'$ with $L\le|C|\le2w=L+1$. For odd $L$ no noncontractible cycle has length $L+1$: winding in one direction gives an odd number of links in each of $L$ columns plus an even number of transverse links, an odd total, and winding in both needs $2L$. So $C$ is straight and $E\subset C$; conversely $C\setminus E$ has weight $(L-1)/2$, while any chain in the class of $E$ with its syndrome has weight at least $(L+1)/2$, since with $C\setminus E$ it forms a noncontractible cycle. *Result:* (a) from (5.4); (b) the straight loops are link-disjoint, so exactly $2L\binom{L}{(L+1)/2}$ errors of weight $w$ fail; (c) $18p^2$ for $L=3$ and $100p^3$ for $L=5$, confirmed by minimum-weight decoding of every error of weight $(L-1)/2$ and $(L+1)/2$, with no failures at the lower weight and no ties at either; ties do occur at higher weight (for $L=3$, already at weight 3). *Common failure:* counting only the $L$ rows of vertical links.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester II Block 3. Written to the note-quality-template standard on 2026-10-02. Last revised 2026-10-03.*
