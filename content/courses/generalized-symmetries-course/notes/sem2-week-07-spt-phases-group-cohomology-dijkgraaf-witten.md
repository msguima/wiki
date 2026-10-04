---
title: "Sem II Week 7 — SPT Phases, Group Cohomology, Dijkgraaf–Witten"
type: lecture-notes
course: syllabus
semester: 2
week: 7
block: 2
duration: 4 hours (3 hr lectures + 1 hr seminar)
prerequisites: Sem II Weeks 2, 4 and 5; Semester I Weeks 2 and 7
modified: 2026-10-02
---

# Sem II Week 7 — SPT Phases, Group Cohomology, Dijkgraaf–Witten

> *[[sem2-week-05-thooft-anomalies-obstruction-as-physics|Sem II Week 5]] found 't Hooft anomalies on the boundary of a gapped bulk one dimension up. This week we construct that bulk, the symmetry-protected topological phases, classify it by group cohomology, and gauge it: in $2+1$ dimensions the two gauged $\mathbb{Z}_2$ phases are the toric code of [[week-07-kogut-susskind-hamiltonian|Sem I Week 7]] and the double semion, which Block 3 solves.*

### How to use this chapter

- **In class:** in the first hour derive the coboundary and the normalization lemma (§2.1), $H^3(\mathbb{Z}_2,U(1))$ (2.4)–(2.6), the AKLT transfer matrix (3.7)–(3.9) and the edge doublet (3.12) with Figures 1–2; Problems 1–2. In the second hour prove the inequality (4.1), the theorem (4.3), projectivity (4.5) and the edge action (4.6), and place AKLT and the cluster state in the classification (§§4.5–4.6); Problem 3. In the third hour derive the cone identity (5.3)–(5.4), the response (5.5), the cubic weight (5.7) with Figure 3, the partition function (6.1) and the anyon data of §§6.3–6.4, ending with (6.9); Problem 4. The seminar hour (§7) is Levin–Gu.
- **For self-study:** §4.3(d), the gauge invariance (5.8), §6.2 with Figure 4, §5.4, §§8–9 and Problems 5⋆–7⋆. The one calculation to do alone is the edge magnetization (3.13)–(3.14): iterate the transfer map on $E_{S^z}(\mathbb 1)$ and sum the series.
- **Instructor checkpoint:** two errors recur. The first is the order of composition: (4.3) is $u\cdot A=e^{i\theta}V^\dagger AV$, and the other order inverts the class (F2). The second is to look for the difference between the toric code and the double semion in their degeneracies, which agree (F3); it is in the spins of the fluxes, which (6.9) ties to the class of the associator.

## 0. Reading

**Primary:** Chen, Gu, Liu, Wen (CGLW), "Symmetry protected topological orders and the group cohomology of their symmetry group", *Phys. Rev. B* 87 (2013) 155114 [arXiv:1106.4772]: §I.C (summary), §IV.B (canonical form with an on-site symmetry), §V (classification of symmetry transformations), §VI.A (group cocycles), §X (equivalent cocycles give the same phase), Apps. B and D. Dijkgraaf, Witten (DW), "Topological gauge theories and group cohomology", *Commun. Math. Phys.* 129 (1990) 393, §6: the partition function (6.8)–(6.9), the lattice realization of §6.4, and in §6.6 the 2-cocycle $c_h$ of (6.32) and the 3-torus partition function (6.34)–(6.36).

**Secondary:** Affleck, Kennedy, Lieb, Tasaki (AKLT), "Rigorous results on valence-bond ground states in antiferromagnets", *Phys. Rev. Lett.* 59 (1987) 799. Pérez-García, Wolf, Sanz, Verstraete, Cirac, "String order and symmetries in quantum spin lattices", *Phys. Rev. Lett.* 100 (2008) 167202 [arXiv:0802.0447], the source of the theorem of §4.1. Kitaev, cond-mat/0506438, App. E ("Algebraic theory of anyons"), as a reference for pentagon, hexagons and spins.

**Seminar paper:** Levin, Gu, "Braiding statistics approach to symmetry-protected topological phases", *Phys. Rev. B* 86 (2012) 115109 [arXiv:1202.3120], §§I–III and V.A (§7).

**Optional research reading:** Chen, Gu, Wen, *Phys. Rev. B* 83 (2011) 035107 [arXiv:1008.3745] (the complete $1+1$d classification); Pollmann, Turner, Berg, Oshikawa, *Phys. Rev. B* 81 (2010) 064439 [arXiv:0910.1811] (the symmetries protecting the Haldane phase); Raussendorf, Briegel, *Phys. Rev. Lett.* 86 (2001) 5188, and Else, Schwarz, Bartlett, Doherty, *Phys. Rev. Lett.* 108 (2012) 240505 [arXiv:1201.4877] (cluster states and measurement-based computation); Levin, Wen, cond-mat/0404617 (the double semion as a string net); Vishwanath, Senthil, *Phys. Rev. X* 3 (2013) 011016 [arXiv:1209.3058] (phases beyond group cohomology).

Proof-status labels follow note-quality-template §4. The group-cohomology, matrix-product and anyon conventions (2.1), (3.3), (4.3), (6.4) and (6.8) are new to the course; they are fixed here and recorded in [[courses/generalized-symmetries-course/conventions|conventions]].

## 1. Motivation and setting

Consider two gapped spin-1 chains with unique ground states on a ring: $H=\sum_j(S^z_j)^2$, whose ground state is $|0\rangle^{\otimes N}$, and the Heisenberg chain, gapped as Haldane predicted for integer spin, or its soluble relative built by Affleck, Kennedy, Lieb and Tasaki. Neither breaks a symmetry or has a local order parameter, and neither has the torus degeneracy of [[topological-order]] ([[sem2-week-02-zn-gauge-theory-as-bf-theory|Sem II Week 2]]). On an open chain the AKLT chain carries a free spin $\tfrac12$ at each end. Without symmetry an end field removes these doublets and the chains can be deformed into each other through gapped states; with the $\mathbb{Z}_2\times\mathbb{Z}_2$ of π rotations imposed they cannot. This is a [[spt-phases|symmetry-protected topological (SPT) phase]]: for a symmetry $G$ in $d$ spacetime dimensions, a gapped phase with a unique $G$-symmetric ground state on every closed space, connected to a product state by a gapped path only if the path breaks $G$.

The week answers three questions. In $1+1$ dimensions the invariant is a class in $H^2(G,U(1))$, read off the action of $G$ on the virtual index of a matrix product state (§4), with AKLT worked to the end (§3). In higher dimensions it is a class in $H^d(G,U(1))$, the topological action an SPT contributes when $G$ is coupled to a background (§5). Gauging $G$ turns the SPT into a Dijkgraaf–Witten theory whose anyons remember the class (§6). The edge of §4.4 is the anomalous boundary of Week 5, and the response (5.5) is the inflow action that compensates it.

## 2. Group cohomology with $U(1)$ coefficients

### 2.1 Cochains, coboundaries and normalization [Proved.]

Let $G$ be finite, acting trivially on $U(1)$; the symmetries of this week are unitary. An $n$-cochain is a function $\omega:G^n\to U(1)$, with coboundary
$$
(\delta\omega)(g_1,\dots,g_{n+1})=\omega(g_2,\dots,g_{n+1})\,\prod_{i=1}^{n}\omega(g_1,\dots,g_ig_{i+1},\dots,g_{n+1})^{(-1)^i}\;\omega(g_1,\dots,g_n)^{(-1)^{n+1}},\tag{2.1}
$$
so that $\delta^2=1$ and $H^n(G,U(1))=Z^n/B^n$. In the degrees we use,
$$
(\delta\beta)(g,h)=\frac{\beta(g)\beta(h)}{\beta(gh)},\qquad
(\delta\alpha)(g,h,l)=\frac{\alpha(h,l)\,\alpha(g,hl)}{\alpha(gh,l)\,\alpha(g,h)},\qquad
(\delta\omega)(g,h,l,m)=\frac{\omega(h,l,m)\,\omega(g,hl,m)\,\omega(g,h,l)}{\omega(gh,l,m)\,\omega(g,h,lm)},\tag{2.2}
$$
with $gh\to g+h$ for an abelian group written additively. A 1-cocycle is a character. A 2-cocycle is the factor system of a projective representation, $V_gV_h=\omega(g,h)V_{gh}$: associativity is $\delta\omega=1$, and the rephasing $V_g\to\beta(g)V_g$ multiplies ω by $\delta\beta$ (Sem II Week 5 §3.1). A 3-cocycle is an associator: if objects labelled by $G$ fuse by the group law and $F(g,h,l)$ relates the groupings $(gh)l$ and $g(hl)$, the pentagon, $F(gh,l,m)F(g,h,lm)=F(g,h,l)F(g,hl,m)F(h,l,m)$, is $\delta F=1$.

A cochain is normalized if it equals 1 whenever an argument is the identity $e$. Evaluating $\delta\omega=1$ at $(e,e,l,m)$, $(g,h,e,e)$ and $(g,e,l,m)$ gives
$$
\omega(e,l,m)=\frac{\omega(e,e,lm)}{\omega(e,e,l)},\qquad \omega(g,h,e)=\frac{\omega(gh,e,e)}{\omega(h,e,e)},\qquad \omega(e,l,m)\,\omega(g,e,l)=\omega(g,e,lm),\tag{2.3}
$$
and the first at $l=m=e$ gives $\omega(e,e,e)=1$. For every 2-cochain, $(\delta\alpha)(e,h,l)=\alpha(e,hl)/\alpha(e,h)$ and $(\delta\alpha)(g,h,e)=\alpha(h,e)/\alpha(gh,e)$; so the choice $\alpha(e,h)=\omega(e,e,h)$, $\alpha(g,e)=\omega(g,e,e)^{-1}$, $\alpha=1$ elsewhere reproduces the first two relations of (2.3), and $\omega'=\omega/\delta\alpha$ is 1 whenever its first or last argument is $e$. The third relation for $\omega'$ then reads $\omega'(g,e,l)=\omega'(g,e,lm)$, and $l=e$ gives $\omega'(g,e,m)=\omega'(g,e,e)=1$. Conversely, if two normalized cocycles differ by $\delta\alpha$, the same two formulas force $\alpha(e,h)=\alpha(g,e)=\alpha(e,e)\equiv\kappa$, and $\alpha/\kappa$ is normalized with the same coboundary. Therefore $H^3$ may be computed with normalized cochains throughout. In degree 2 the argument is shorter: $\delta\alpha=1$ at $(e,e,l)$ and $(g,e,e)$ gives $\alpha(e,l)=\alpha(g,e)=\alpha(e,e)$, removed by the constant 1-cochain $\beta\equiv\alpha(e,e)$.

### 2.2 The low degrees of $\mathbb{Z}_2$ [Computed.]

For $\mathbb{Z}_2=\{0,1\}$ a normalized cochain of degree 1, 2 or 3 is fixed by $\beta(1)$, $\alpha(1,1)=v$ or $\omega(1,1,1)=w$. The 1-cocycles are the characters $\beta(1)=\pm1$, and $B^1$ is trivial: $H^1(\mathbb{Z}_2,U(1))=\mathbb{Z}_2$. For a normalized α the only condition with no vanishing argument, $(\delta\alpha)(1,1,1)=\alpha(1,1)\alpha(1,0)/[\alpha(0,1)\alpha(1,1)]=1$, holds identically, while $(\delta\beta)(1,1)=\beta(1)^2$ reaches every $v$. Therefore $H^2(\mathbb{Z}_2,U(1))=0$, and by §4 a single $\mathbb{Z}_2$ protects no $1+1$d SPT (Problem 2 treats $\mathbb{Z}_N$). For $\mathbb{Z}_2\times\mathbb{Z}_2$, $H^2=\mathbb{Z}_2$; its nontrivial class, detected by a commutator phase and forcing even-dimensional representations, is derived in [[sem2-week-05-thooft-anomalies-obstruction-as-physics|Sem II Week 5]] ('t Hooft anomalies: obstruction as physics) §§3.3–3.4, and §§4.5–4.6 use it.

### 2.3 $H^3(\mathbb{Z}_2,U(1))=\mathbb{Z}_2$ [Computed.]

The cocycle condition is $(\delta\omega)(g,h,l,m)=1$ at the 16 points of $\mathbb{Z}_2^4$. For a normalized ω, every point with a vanishing argument gives 1; at $(1,1,1,0)$, for instance, the factors of (2.2) are $\omega(1,1,0)\,\omega(1,0,0)\,\omega(1,1,1)/[\omega(0,1,0)\,\omega(1,1,1)]=1$. At the remaining point, where $hl=lm=gh=0$,
$$
(\delta\omega)(1,1,1,1)=\frac{\omega(1,1,1)\,\omega(1,0,1)\,\omega(1,1,1)}{\omega(0,1,1)\,\omega(1,1,0)}=w^2 .\tag{2.4}
$$
The normalized cocycles are $w=\pm1$, and the coboundary of a normalized 2-cochain is trivial, $(\delta\alpha)(1,1,1)=1$ as in §2.2. By the lemma of §2.1,
$$
H^3(\mathbb{Z}_2,U(1))=\{w:w^2=1\}=\mathbb{Z}_2,\qquad \omega(x,y,z)=(-1)^{xyz}\quad(x,y,z\in\{0,1\})\tag{2.5}
$$
representing the nontrivial class. A class can be read without normalizing first: since $(\delta\alpha)(1,0,1)=\alpha(0,1)/\alpha(1,0)$ and $(\delta\alpha)(1,1,1)=\alpha(1,0)/\alpha(0,1)$ for every α,
$$
I(\omega)=\omega(1,0,1)\,\omega(1,1,1)\tag{2.6}
$$
is coboundary invariant, with $I=-1$ for (2.5). Problem 5⋆ extends (2.5)–(2.6) to $\mathbb{Z}_N$.

We checked these groups by computer: with $H^n(G,U(1))\cong H^{n+1}(G,\mathbb{Z})$ for $n\ge1$, $H^n(G,U(1))$ is the torsion of the cokernel of the integer coboundary matrix $C^n\to C^{n+1}$, and the Smith normal forms give the entries of Table 1 (and $H^4(\mathbb{Z}_2,U(1))=0$). The cocycle (2.5) satisfies the condition at all 16 points, and for generic $w$ the only nonzero entry of $\delta\omega$ is (2.4).

| $G$ | $d=1$: $H^1$ | $d=2$: $H^2$ | $d=3$: $H^3$ |
|---|---|---|---|
| $\mathbb{Z}_2$ | $\mathbb{Z}_2$ | $0$ | $\mathbb{Z}_2$ |
| $\mathbb{Z}_2\times\mathbb{Z}_2$ | $\mathbb{Z}_2^2$ | $\mathbb{Z}_2$ | $\mathbb{Z}_2^3$ |
| $\mathbb{Z}_N$ ($N=3,4$) | $\mathbb{Z}_N$ | $0$ | $\mathbb{Z}_N$ |
| reading | charge of a $0+1$d state | $1+1$d SPT (§4) | $2+1$d SPT; gauged, DW (§6) |

**Table 1.** Low-degree cohomology (Smith normal forms) and its SPT reading, $d$ = spacetime dimension.

## 3. Matrix product states and the AKLT chain

### 3.1 Matrix product states and the transfer map

A translation-invariant matrix product state (MPS) on a ring of $N$ sites, with local dimension $d$ and bond dimension $D$, and its open-chain version are
$$
|\psi_N\rangle=\sum_{s}{\rm tr}\big(A^{s_1}\cdots A^{s_N}\big)\,|s_1\cdots s_N\rangle,\qquad A^s\in M_D(\mathbb{C}),\tag{3.1}
$$
$$
|\psi_{\alpha\beta}\rangle=\sum_{s}\langle\alpha|A^{s_1}\cdots A^{s_N}|\beta\rangle\,|s_1\cdots s_N\rangle,\qquad \alpha,\beta=1,\dots,D,\tag{3.2}
$$
as Figure 1 shows. The transfer map, its dual and its version with an operator $O$ inserted are
$$
E(X)=\sum_sA^sXA^{s\dagger},\qquad E^*(Y)=\sum_sA^{s\dagger}YA^s,\qquad E_O(X)=\sum_{s,s'}O_{ss'}\,A^{s'}XA^{s\dagger},\tag{3.3}
$$
where $O_{ss'}=\langle s|O|s'\rangle$. As a $D^2\times D^2$ matrix, $\mathbb{E}=\sum_sA^s\otimes\bar A^s$ acts on the vectorized $X$, $\langle\psi_N|\psi_N\rangle={\rm Tr}\,\mathbb{E}^N$, and in a product of insertions the maps compose with the leftmost site outermost.

```
           s_1       s_2               s_N
            |         |                 |
   alpha --[A]-------[A]---- . . . ----[A]-- beta        <alpha| A^{s_1} ... A^{s_N} |beta>

                 |                        +--[A]--+
   E(X) =     --[A]--                     |   |   |      E = sum_s A^s (x) conj(A^s)
             X   |   (sum over s)         +--[A*]-+
              --[A*]--
```
**Figure 1.** An MPS contracts tensors along the virtual (horizontal) index; the transfer map contracts one site of the ket with the same site of the bra, and every overlap or correlator is a composition of such maps.

The MPS is injective if for some $L$ the products $A^{s_1}\cdots A^{s_L}$ span $M_D$; it is normalized if, in addition,
$$
E(\mathbb 1)=\mathbb 1,\qquad E^*(\rho)=\rho\ \text{ for some }\rho>0,\ {\rm tr}\,\rho=1.\tag{3.4}
$$
Every injective MPS is brought to this form by $A^s\to\lambda MA^sM^{-1}$, which changes the state only by a factor [Stated — refs: Pérez-García et al. 2008; CGLW §IV.B]. For a normalized injective MPS, 1 is a simple eigenvalue of $E$ and every other eigenvalue has modulus below 1 (proved in §4.1), so $E^n(X)\to{\rm tr}(\rho X)\,\mathbb 1$, $\langle\psi_N|\psi_N\rangle\to1$, and on the infinite chain
$$
\langle O_jO'_{j+r}\rangle={\rm tr}\Big[\rho\,E_O\big(E^{r-1}(E_{O'}(\mathbb 1))\big)\Big],\qquad r\ge1 .\tag{3.5}
$$

### 3.2 The AKLT tensors and their transfer matrix [Computed.]

For spin 1, in the basis $m=+1,0,-1$, the AKLT tensors are
$$
A^{+1}=\sqrt{\tfrac23}\,\sigma^+,\qquad A^{0}=-\sqrt{\tfrac13}\,\sigma^z,\qquad A^{-1}=-\sqrt{\tfrac23}\,\sigma^-,\tag{3.6}
$$
where $\sigma^\pm=(\sigma^x\pm i\sigma^y)/2$. Since $\sigma^+\sigma^-+\sigma^-\sigma^+=\mathbb 1$, $\sum_sA^sA^{s\dagger}=\sum_sA^{s\dagger}A^s=\tfrac23\mathbb 1+\tfrac13\mathbb 1=\mathbb 1$: the MPS is normalized with $\rho=\mathbb 1/2$, and it is injective at $L=2$, where $A^{+1}A^{-1}\propto|{\uparrow}\rangle\langle{\uparrow}|$, $A^{-1}A^{+1}\propto|{\downarrow}\rangle\langle{\downarrow}|$, $A^{\pm1}A^0\propto\sigma^\pm$ span $M_2$. Using $\sigma^z\sigma^\pm=\pm\sigma^\pm$, $\sigma^z\sigma^+\sigma^z=-\sigma^+$ and $(\sigma^\pm)^2=0$,
$$
E(\sigma^z)=\tfrac23\sigma^+\sigma^z\sigma^-+\tfrac13\sigma^z\sigma^z\sigma^z+\tfrac23\sigma^-\sigma^z\sigma^+=-\tfrac23|{\uparrow}\rangle\langle{\uparrow}|+\tfrac13\sigma^z+\tfrac23|{\downarrow}\rangle\langle{\downarrow}|=-\tfrac13\sigma^z,
$$
$$
E(\sigma^+)=\tfrac23\sigma^+\sigma^+\sigma^-+\tfrac13\sigma^z\sigma^+\sigma^z+\tfrac23\sigma^-\sigma^+\sigma^+=-\tfrac13\sigma^+,\tag{3.7}
$$
and $E(\sigma^-)=-\sigma^-/3$ in the same way. So $E$ has the eigenvalue 1 on $\mathbb 1$ and $-\tfrac13$ on the three traceless directions: the correlation length is $\xi=1/\ln3$. The insertions of $S^z$ are
$$
E_{S^z}(\mathbb 1)=\tfrac23\sigma^+\sigma^--\tfrac23\sigma^-\sigma^+=\tfrac23\sigma^z,\qquad E_{S^z}(\sigma^z)=\tfrac23\sigma^+\sigma^z\sigma^--\tfrac23\sigma^-\sigma^z\sigma^+=-\tfrac23\mathbb 1,\tag{3.8}
$$
and (3.5) gives
$$
\langle S^z_jS^z_{j+r}\rangle={\rm tr}\Big[\tfrac{\mathbb 1}2\,E_{S^z}\Big(\big(-\tfrac13\big)^{r-1}\tfrac23\sigma^z\Big)\Big]=-\tfrac49\big(-\tfrac13\big)^{r-1}=\tfrac43\big(-\tfrac13\big)^{r}.\tag{3.9}
$$

The tensors (3.6) describe the valence-bond state of Figure 2, the ground state of
$$
H_{\rm AKLT}=\sum_j\Big[\mathbf S_j\cdot\mathbf S_{j+1}+\tfrac13(\mathbf S_j\cdot\mathbf S_{j+1})^2\Big]=\sum_j\Big(2P^{(2)}_{j,j+1}-\tfrac23\Big),\tag{3.10}
$$
where $P^{(2)}$ projects two spins 1 on total spin 2 (the identity follows from $\mathbf S_j\cdot\mathbf S_{j+1}=-2,-1,1$ at total spin $0,1,2$). Every state (3.2) is annihilated by every $P^{(2)}_{j,j+1}$: at fixed outer virtual indices, sites $j,j+1$ are in the state $\sum_{st}(A^sA^t)_{\alpha\beta}|st\rangle$, on which rotations act through the virtual indices as $\bar V\otimes V$ by (4.7)–(4.8), two spins $\tfrac12$, so the total spin is at most 1. The four states (3.2) are therefore ground states of energy $-\tfrac23(N-1)$. Exact diagonalization on six open sites gives four degenerate levels at $-10/3$, spanned by the states (3.2), and a gap to $-2.536$; (3.7)–(3.9) and the string order of Problem 1 were checked numerically from the tensors.

```
   site:      1             2             3                    N
          ( o   o )     ( o   o )     ( o   o )     ...    ( o   o )
            ^     \_____/     \_____/     \___  ...   ___/      ^
          free     singlet      singlet                      free
          spin 1/2                                         spin 1/2
```
**Figure 2.** The AKLT state: each spin 1 is the symmetric product of two virtual spins $\tfrac12$ (o), and neighbouring virtual spins form singlets; on an open chain the unpaired virtual spin at each end is the index α or β of (3.2).

### 3.3 The edge doublet from the transfer matrix [Computed.]

The overlaps of the states (3.2) are matrix elements of $E^N$:
$$
\langle\psi_{\alpha\beta}|\psi_{\alpha'\beta'}\rangle=\sum_{s}(A^{s_1}\cdots A^{s_N})_{\alpha'\beta'}\,\overline{(A^{s_1}\cdots A^{s_N})_{\alpha\beta}}=\langle\alpha'|\,E^N\big(|\beta'\rangle\langle\beta|\big)\,|\alpha\rangle .\tag{3.11}
$$
With $X=\tfrac12({\rm tr}X)\mathbb 1+X_0$, $X_0$ traceless, (3.7) gives $E^N(X)=\tfrac12({\rm tr}X)\mathbb 1+qX_0$ with $q=(-\tfrac13)^N$, and therefore
$$
G\equiv\big(\langle\psi_{\alpha\beta}|\psi_{\alpha'\beta'}\rangle\big)=\tfrac12(1-q)\,\mathbb 1_4+q\,|\Phi\rangle\langle\Phi|,\qquad|\Phi\rangle=\sum_\alpha|\alpha\alpha\rangle .\tag{3.12}
$$
Its eigenvalues are $\tfrac12(1-q)$ three times, orthogonal to Φ, and $\tfrac12(1+3q)$ on Φ. For $N=1$ the latter vanishes (a single spin 1 has no singlet); for every $N\ge2$ all four are positive. The four ground states are independent: two spins $\tfrac12$ at the ends, in the singlet Φ, invariant under the $\bar V_g\otimes V_g$ of (4.6), and the triplet, with norms differing by terms of order $3^{-N}$. We checked (3.12) against the Gram matrices for $N=1,\dots,7$.

The ends carry spin $\tfrac12$ literally. Since $A^{\pm1}\propto\sigma^\pm$ and $A^0\propto\sigma^z$, $\langle\alpha|A^s|\beta\rangle\ne0$ only if $m_\alpha=m_\beta+s$, with $m=\pm\tfrac12$ the virtual $S^z$; so $|\psi_{\alpha\beta}\rangle$ has $S^z_{\rm tot}=m_\alpha-m_\beta$. For $\alpha={\uparrow}$ and fixed $j$, as $N\to\infty$, $E^{N-j}(|\beta\rangle\langle\beta|)\to\tfrac12\mathbb 1$ and the norm tends to $\tfrac12$, so
$$
\langle S^z_j\rangle_{\uparrow}=\langle{\uparrow}|\,E^{j-1}\big(E_{S^z}(\mathbb 1)\big)\,|{\uparrow}\rangle=\tfrac23\big(-\tfrac13\big)^{j-1}=2(-1)^{j-1}3^{-j},\tag{3.13}
$$
$$
\sum_{j\ge1}\langle S^z_j\rangle_{\uparrow}=\frac{2/3}{1+1/3}=\frac12 .\tag{3.14}
$$
The left end carries $S^z=+\tfrac12$, spread over a few sites with alternating sign, and the right end carries $-m_\beta$, the conjugate representation (§4.4). On nine sites in $|\psi_{\uparrow\downarrow}\rangle$, with $S^z_{\rm tot}=1$, the exact profile is $0.6667,\,-0.2225,\,0.0750,\,-0.0274,\,0.0165,\dots$, symmetric about the centre, summing to 1.

> **Physical picture.** A simulation of an open spin-1 chain in the Haldane phase sees (3.13): magnetization $\pm\tfrac12$ attached to each end and decaying over ξ, in the four lowest states, which a generic Hamiltonian in the phase splits only by an amount of order $e^{-N/\xi}$ [Heuristic]. A field on one end, $hS^z_1$, would split its doublet, and the π rotations of §4.5 forbid it: the virtual index of (3.1) is a physical spin at an edge.

## 4. The classification of one-dimensional SPT phases

### 4.1 A symmetry acts on the virtual index [Proved.]

A unitary $u$ on $\mathbb{C}^d$ acts on tensors as $(u\cdot A)^s=\sum_{s'}u_{ss'}A^{s'}$, so that $u^{\otimes N}|\psi_N\rangle$ is the MPS of $u\cdot A$. Everything rests on one inequality. Let $B^s$ satisfy $\sum_sB^sB^{s\dagger}=\mathbb 1$ (for instance $B=u\cdot A$) and $\Phi(X)=\sum_sB^sXA^{s\dagger}$. The maps $W_A=\sum_s|s\rangle\otimes A^{s\dagger}$ and $W_B$, from $\mathbb{C}^D$ to $\mathbb{C}^d\otimes\mathbb{C}^D$, are isometries, $\Phi(X)=W_B^\dagger(\mathbb 1\otimes X)W_A$, and with the projector $Q=\mathbb 1-W_BW_B^\dagger$
$$
\Phi(X)^\dagger\Phi(X)=E(X^\dagger X)-W_A^\dagger(\mathbb 1\otimes X^\dagger)\,Q\,(\mathbb 1\otimes X)W_A\ \le\ E(X^\dagger X).\tag{4.1}
$$
Suppose $\Phi(X)=\lambda X$, $X\ne0$. Pairing (4.1) with ρ and using ${\rm tr}[\rho E(Y)]={\rm tr}[E^*(\rho)Y]={\rm tr}[\rho Y]$ gives $|\lambda|^2{\rm tr}(\rho X^\dagger X)\le{\rm tr}(\rho X^\dagger X)$, with ${\rm tr}(\rho X^\dagger X)>0$: $|\lambda|\le1$. If $|\lambda|=1$, the nonnegative operator $E(X^\dagger X)-X^\dagger X$ has zero trace against $\rho>0$ and vanishes; the last term of (4.1), equal to $(Q(\mathbb 1\otimes X)W_A)^\dagger Q(\mathbb 1\otimes X)W_A$, vanishes too, so $(\mathbb 1\otimes X)W_A=W_BW_B^\dagger(\mathbb 1\otimes X)W_A=\lambda W_BX$. In components,
$$
E(X^\dagger X)=X^\dagger X,\qquad XA^{s\dagger}=\lambda\,B^{s\dagger}X\quad\text{for all }s .\tag{4.2}
$$

Take first $B=A$. If $E(X)=\lambda X$ with $|\lambda|=1$, (4.2) gives $XM=\lambda^LMX$ for every product $M$ of $L$ adjoint tensors; these span $M_D$, so $M=\mathbb 1$ gives $\lambda^L=1$, $X$ is central, $X\propto\mathbb 1$, and $\lambda=1$. Finally, (4.1) and $X^\dagger X\le\|X\|^2\mathbb 1$ give $\|E(X)\|^2\le\|E(X^\dagger X)\|\le\|X\|^2$, so the powers of $E$ are bounded and there is no Jordan block at 1. Therefore 1 is a simple eigenvalue and the only one on the unit circle, as §3 used.

Now suppose $|\langle\psi_N|u^{\otimes N}|\psi_N\rangle|=\langle\psi_N|\psi_N\rangle$ for infinitely many $N$, as when $u^{\otimes N}|\psi_N\rangle=e^{i\alpha_N}|\psi_N\rangle$. With $B=u\cdot A$, $\sum_sB^sB^{s\dagger}=\mathbb 1$ by unitarity and $\langle\psi_N|u^{\otimes N}|\psi_N\rangle={\rm Tr}\,\Phi^N$. If every eigenvalue of Φ had modulus below 1, ${\rm Tr}\,\Phi^N\to0$ while $\langle\psi_N|\psi_N\rangle\to1$; so Φ has an eigenvalue $e^{i\theta}$. By (4.2) and the uniqueness just proved, $X^\dagger X=c\mathbb 1$, $X=\sqrt c\,U$ with $U$ unitary, and the adjoint of (4.2), $A^sX^\dagger=e^{-i\theta}X^\dagger B^s$, gives $B^s=e^{i\theta}UA^sU^\dagger$. With $V=U^\dagger$,
$$
u\cdot A^s=e^{i\theta}\,V^\dagger A^sV\qquad\text{for all }s,\tag{4.3}
$$
the theorem of Pérez-García, Wolf, Sanz, Verstraete and Cirac; conversely (4.3) gives $u^{\otimes N}|\psi_N\rangle=e^{iN\theta}|\psi_N\rangle$. $V$ is unique up to a phase: if $WA^s=e^{i\varphi}A^sW$ for all $s$ and $W\ne0$, then $WM=e^{iL\varphi}MW$ for every product of $L$ tensors, $M=\mathbb 1$ gives $e^{iL\varphi}=1$, and
$$
WA^s=e^{i\varphi}A^sW\ \ \forall s\quad\Longrightarrow\quad W\propto\mathbb 1,\quad e^{i\varphi}=1 ;\tag{4.4}
$$
two solutions $(\theta,V)$, $(\theta',V')$ of (4.3) give $W=V'V^\dagger$ with $WA^sW^\dagger=e^{i(\theta'-\theta)}A^s$, so $V'\propto V$ and $\theta'=\theta$.

### 4.2 Projectivity and the class $[\omega]\in H^2(G,U(1))$ [Proved.]

Let $u(g)$ be a unitary representation of $G$ under which every $|\psi_N\rangle$ is invariant up to a phase. Applying (4.3) twice, with $u(g)\cdot$ acting on the physical index only, gives $u(g)u(h)\cdot A^s=e^{i(\theta_g+\theta_h)}(V_gV_h)^\dagger A^s(V_gV_h)$, to be compared with $u(gh)\cdot A^s=e^{i\theta_{gh}}V_{gh}^\dagger A^sV_{gh}$. So $W=V_gV_hV_{gh}^\dagger$ satisfies $WA^s=e^{i(\theta_g+\theta_h-\theta_{gh})}A^sW$, and (4.4) gives
$$
V_gV_h=\omega(g,h)\,V_{gh},\qquad e^{i\theta_g}e^{i\theta_h}=e^{i\theta_{gh}} .\tag{4.5}
$$
The $V_g$ form a projective representation, $\omega\in Z^2(G,U(1))$, and $e^{i\theta_g}$ is a character, the charge per site. Since each $V_g$ is fixed up to a phase $\beta(g)$, ω is fixed up to $\delta\beta$: the MPS determines a class $[\omega]\in H^2(G,U(1))$.

### 4.3 The class is an invariant of the phase [Proved for (a)–(d); the converse Stated — refs: Chen–Gu–Wen 2011; CGLW §V.]

(a) *Gauge:* $A^s\to MA^sM^\dagger$, $M$ unitary, preserves (3.4) with $\rho\to M\rho M^\dagger$ and sends $V_g\to MV_gM^\dagger$. (b) *Blocking* $k$ sites, $A^{(s_1\dots s_k)}=A^{s_1}\cdots A^{s_k}$ with $u(g)^{\otimes k}$, keeps $V_g$ and sends $\theta_g\to k\theta_g$, so the charge per site is not an invariant of the internal symmetry (with translation imposed it is an extra label, CGLW §XII). (c) *Stacking:* $A\otimes A'$ is injective, with $V_g\otimes V'_g$ and cocycle $\omega\omega'$; the classes add, and a product state ($D=1$) adds nothing.

(d) *Continuity.* Along a continuous path $A(t)$ of normalized injective symmetric MPS with fixed $D$, the character $\theta_g(t)$, valued in a finite set, is constant, and $V_g(t)$ spans the one-dimensional, continuously varying solution space of (4.3); so $V_g(t)$ and $\omega(g,h;t)$ can be chosen continuous. The cocycles $Z^2$ form a closed subgroup of $U(1)^{|G|^2}$; $B^2=\delta\,U(1)^{|G|}$ is connected and has finite index $|H^2(G,U(1))|=|H^3(G,\mathbb{Z})|$ [Stated]. A closed subgroup of finite index is open, so $B^2$ is the identity component of $Z^2$ and every class is a union of components: a continuous path of cocycles stays in one class.

The converse, that injective MPS with the same class are connected by a gapped symmetric path after blocking and stacking with product states, and the statement that without symmetry every injective MPS is connected to a product state, are the theorems of Chen, Gu and Wen [Stated — refs]; the second is why the classification is entirely symmetry-protected.

### 4.4 The edge carries the projective representation [Proved; the protection Sketched.]

On the open chain, $\langle\alpha|V_g^\dagger(A^{s_1}\cdots A^{s_N})V_g|\beta\rangle=\sum(V_g^\dagger)_{\alpha\alpha'}(A^{s_1}\cdots A^{s_N})_{\alpha'\beta'}(V_g)_{\beta'\beta}$ with $(V_g^\dagger)_{\alpha\alpha'}=\overline{(V_g)_{\alpha'\alpha}}$, so (4.3) gives
$$
u(g)^{\otimes N}|\psi_{\alpha\beta}\rangle=e^{iN\theta_g}\sum_{\alpha'\beta'}\overline{(V_g)_{\alpha'\alpha}}\,(V_g)_{\beta'\beta}\,|\psi_{\alpha'\beta'}\rangle .\tag{4.6}
$$
The right end carries $V_g$, with cocycle ω, the left end $\bar V_g$, with $\omega^{-1}$, and the bulk only the linear factor $e^{iN\theta_g}$. This is the $1+1$d case of the inflow of [[sem2-week-05-thooft-anomalies-obstruction-as-physics|Sem II Week 5]]: each edge realizes $G$ with the anomaly $[\omega]^{\pm1}$, which the bulk compensates. If $[\omega]\ne0$ and $V_g$ is irreducible, Schur's lemma, valid for projective representations, makes every operator on the left-edge space that commutes with all $\bar V_g$ a multiple of $\mathbb 1$. A symmetric perturbation localized near the left end acts on the edge space, at first order and up to corrections of order $e^{-N/\xi}$ whose estimate we omit, as such an operator; it shifts the doublet without splitting it. Stability to all orders is [Stated — refs: Pollmann et al. 2010; Chen–Gu–Wen 2011]. For $\mathbb{Z}_2\times\mathbb{Z}_2$ in the nontrivial class every representation is even-dimensional (Week 5 §3.3), so each end keeps at least two states.

### 4.5 The AKLT chain in the classification [Computed.]

For rotations about $z$, $u=e^{-i\varphi S^z}$ gives $u\cdot A^s=e^{-i\varphi m_s}A^s$, and since $e^{-i\varphi\sigma^z/2}\sigma^\pm e^{i\varphi\sigma^z/2}=e^{\mp i\varphi}\sigma^\pm$,
$$
V(R_z(\varphi))=e^{i\varphi\sigma^z/2},\qquad\theta=0 .\tag{4.7}
$$
For the π rotation about $x$, $e^{-i\pi S^x}$ maps $|{\pm1}\rangle\to-|{\mp1}\rangle$ and $|0\rangle\to-|0\rangle$, so $u\cdot A^{\pm1}=-A^{\mp1}$ and $u\cdot A^0=-A^0$, which is $\sigma^xA^s\sigma^x$ by $\sigma^x\sigma^\pm\sigma^x=\sigma^\mp$, $\sigma^x\sigma^z\sigma^x=-\sigma^z$:
$$
V(R_x(\pi))=\sigma^x,\qquad\theta=0 .\tag{4.8}
$$
At $\varphi=2\pi$, (4.7) gives $V=-\mathbb 1$ for a rotation that is the identity on every physical spin: the virtual representation of $SO(3)$ is the projective spin $\tfrac12$ (numerically, $V_g=\overline{D^{1/2}(g)}=\sigma^yD^{1/2}(g)\sigma^y$ for a generic rotation). For $\mathbb{Z}_2\times\mathbb{Z}_2=\{1,R_x(\pi),R_y(\pi),R_z(\pi)\}$, with $V_x=\sigma^x$ and $V_z=i\sigma^z$,
$$
V_xV_zV_x^{-1}V_z^{-1}=-\mathbb 1 ,\tag{4.9}
$$
a phase that rephasing cannot change: AKLT is in the nontrivial class of $H^2(\mathbb{Z}_2\times\mathbb{Z}_2,U(1))=\mathbb{Z}_2$, and its edge spin is protected by the π rotations alone. Pollmann, Turner, Berg and Oshikawa showed that time reversal or bond-centred inversion protect it as well [Stated — refs]. We verified (4.7)–(4.9) by solving (4.3) as a linear system for $V$.

### 4.6 The cluster state in the classification [Computed.]

The cluster chain of [[sem2-week-05-thooft-anomalies-obstruction-as-physics|Sem II Week 5]] (5.1)–(5.2), $H_c=-\sum_jK_j$ with $K_j=Z_{j-1}X_jZ_{j+1}$ and symmetry generated by $U_a=\prod_{j\,{\rm odd}}X_j$ and $U_b=\prod_{j\,{\rm even}}X_j$, has the ground state $|C\rangle=\prod_jCZ_{j,j+1}|+\rangle^{\otimes N}=2^{-N/2}\sum_s\prod_j(-1)^{s_js_{j+1}}|s\rangle$ ($N$ even). Week 5 §5.2 computes its edge from the stabilizers; here we read its class off the bulk tensor. Since $\langle s|\pm_t\rangle=2^{-1/2}(-1)^{st}$, with $|\pm_0\rangle=|+\rangle$, $|\pm_1\rangle=|-\rangle$, the state is the MPS
$$
A^s=|\pm_s\rangle\langle s|,\qquad {\rm tr}(A^{s_1}\cdots A^{s_N})=\prod_j\langle s_j|\pm_{s_{j+1}}\rangle=2^{-N/2}\prod_j(-1)^{s_js_{j+1}} .\tag{4.10}
$$
It is normalized, $E(\mathbb 1)=\sum_s|\pm_s\rangle\langle\pm_s|=\mathbb 1$ and $E^*(\mathbb 1/2)=\mathbb 1/2$, and injective at $L=2$, where $A^sA^t=2^{-1/2}(-1)^{st}|\pm_s\rangle\langle t|$ form a basis of $M_2$. Since $E(X)=\sum_s\langle s|X|s\rangle\,|\pm_s\rangle\langle\pm_s|$, $E(\sigma^z)=\sigma^x$ and $E(\sigma^x)=E(\sigma^y)=0$: the eigenvalues are $1,0,0,0$. The symmetry is on-site for the block $B^{st}=A^sA^t$, where $U_a$ acts as $X\otimes\mathbb 1$ and $U_b$ as $\mathbb 1\otimes X$, and the identities
$$
\sum_{s'}X_{ss'}A^{s'}=A^{1-s}=ZA^sX,\qquad XA^t=(-1)^tA^t=A^tZ\tag{4.11}
$$
give $(X\otimes\mathbb 1)\cdot B^{st}=ZA^sXA^t=ZA^sA^tZ$ and $(\mathbb 1\otimes X)\cdot B^{st}=A^sZA^tX=XA^sA^tX$:
$$
V_a=Z,\qquad V_b=X,\qquad V_aV_bV_a^{-1}V_b^{-1}=-\mathbb 1 .\tag{4.12}
$$
The cluster state is in the nontrivial class, that of AKLT under $R_x(\pi)\leftrightarrow U_a$, $R_z(\pi)\leftrightarrow U_b$. On the left end, (4.6) represents $U_a$ by $\bar V_a=Z$ and $U_b$ by $\bar V_b=X$; Week 5 §5.2 writes the same edge algebra with $U_a$ as $\Sigma^x_L$, and the two differ by a Hadamard change of basis. We checked that (4.10) reproduces $\prod CZ|+\rangle^{\otimes8}$, that every $K_j$ and both sublattice symmetries fix it, and (4.12) by solving (4.3).

The cluster state is the resource of Raussendorf and Briegel's measurement-based computation: measuring site $j$ in the $X$ basis with outcome $\pm$ replaces $A^{s_j}$ by $\sum_s\langle\pm|s\rangle A^s=H/\sqrt2$ or $HZ/\sqrt2$, which teleports the virtual qubit, the space of the projective representation, one site with a known byproduct. Else, Schwarz, Bartlett and Doherty showed that this use as a quantum wire persists throughout the $\mathbb{Z}_2\times\mathbb{Z}_2$ SPT phase [Stated — refs].

## 5. Cocycle models in higher dimensions

### 5.1 The response of an SPT to a background [Proved.]

CGLW build an SPT in $d$ spacetime dimensions from $\omega\in Z^d(G,U(1))$ through its homogeneous form
$$
\nu(g_0,\dots,g_d)=\omega\big(g_0^{-1}g_1,\ \dots,\ g_{d-1}^{-1}g_d\big),\qquad\nu(gg_0,\dots,gg_d)=\nu(g_0,\dots,g_d),\tag{5.1}
$$
in which $\delta\omega=1$ reads
$$
\prod_{i=0}^{d+1}\nu(g_0,\dots,\widehat{g_i},\dots,g_{d+1})^{(-1)^i}=1 .\tag{5.2}
$$
Triangulate a closed oriented $d$-manifold $M$ with ordered vertices, place $g_v\in G$ on each vertex, and weight each $d$-simplex $\Delta=(v_0<\dots<v_d)$ by $\nu(g_{v_0},\dots,g_{v_d})^{s_\Delta}$, with $s_\Delta=\pm1$ its orientation relative to $M$. The condition (5.2) at $(g_*,g_0,\dots,g_d)$, solved for its first factor, is the cone identity
$$
\nu(g_0,\dots,g_d)=\prod_{j=0}^{d}\nu(g_*,g_0,\dots,\widehat{g_j},\dots,g_d)^{(-1)^j}\qquad\text{for every }g_*\in G ,\tag{5.3}
$$
whose factors are cones with apex $g_*$ over the faces of Δ. Over a closed $M$ every $(d-1)$-face occurs twice with opposite induced orientations, so the cones cancel:
$$
\prod_\Delta\nu(g_{v_0},\dots,g_{v_d})^{s_\Delta}=1\qquad\text{for every configuration }\{g_v\}.\tag{5.4}
$$
The normalized partition function is 1 on every closed $M$: the bulk is trivial.

A background is a flat $G$-connection $A_{vw}$ on the oriented links. The matter couples through the gauge-covariant combinations $g_v^{-1}A_{vw}g_w$, and the weight $\prod_\Delta\omega(g_{v_0}^{-1}A_{v_0v_1}g_{v_1},\dots)^{s_\Delta}$, which reduces to (5.4) at $A=1$, is invariant under $g_v\to h_vg_v$, $A_{vw}\to h_vA_{vw}h_w^{-1}$. It does not depend on the matter field: on the star of a vertex $v$, a ball, $A_{uw}=k_u^{-1}k_w$ is pure gauge, the weights around $v$ are $\nu(k_{v_0}g_{v_0},\dots)$ by (5.1), and (5.3) rewrites their product as cones over the link of $v$, where $g_v$ does not appear. Setting $g_v=1$, the response of the SPT to the background is
$$
Z_{\rm SPT}[A]=\prod_\Delta\omega\big(A_{v_0v_1},A_{v_1v_2},\dots,A_{v_{d-1}v_d}\big)^{s_\Delta},\tag{5.5}
$$
gauge invariant, equal to 1 for pure-gauge $A$, and a function of the holonomies alone: the topological action $\langle\gamma^*\omega,[M]\rangle$ of DW (6.9) in the triangulated form of their §6.4. We checked (5.2)–(5.3) for (2.5) at every point of $\mathbb{Z}_2^5$, and (5.2) for a representative of $H^2(\mathbb{Z}_2\times\mathbb{Z}_2,U(1))$.

### 5.2 Retriangulation and coboundaries [Proved; Pachner's theorem Stated.]

A Pachner move replaces some of the $d+2$ faces of a $(d+1)$-simplex, glued together, by the complementary ones; in $d=3$ the 2–3 move exchanges two tetrahedra sharing a triangle for three sharing an edge. The cocycle condition (5.2), read on the $(d+1)$-simplex, says that the two products of weights agree. Since any two triangulations of a closed PL manifold are related by Pachner moves, (5.5) does not depend on the triangulation. A coboundary $\omega\to\omega\,\delta\alpha$ multiplies (5.5) by a product of α's over $(d-1)$-faces in which every face occurs twice with opposite signs. So $Z_{\rm SPT}[A]$ depends only on $[\omega]$ and on the gauge class of $A$: cocycles are the data that give consistent topological weights, and cohomologous cocycles give the same weight on closed manifolds.

### 5.3 The $\mathbb{Z}_2$ weight on the cubic lattice [Proved.]

For $G=\mathbb{Z}_2$, $d=3$ and (2.5), the cubical cup product of [[courses/generalized-symmetries-course/conventions|conventions]] §8 does the triangulation. With $a\in C^1(\Lambda,\mathbb{Z}_2)$ lifted to $\{0,1\}$, the three terms of $(a\cup a)\cup a$ on a cube, each with the two-term rule for $a\cup a$, give
$$
(a\cup a\cup a)(x;123)=\sum_{\pi\in S_3}{\rm sgn}(\pi)\;a_{\pi_1}(x)\;a_{\pi_2}(x+\hat\pi_1)\;a_{\pi_3}(x+\hat\pi_1+\hat\pi_2),\tag{5.6}
$$
a sum over the six monotone paths from $x$ to $x+\hat1+\hat2+\hat3$ (Figure 3). Each path is the spine of a tetrahedron of the six-simplex triangulation of the cube that DW use for the 3-torus in §6.6, whose weight (6.35) has the same six terms. So
$$
Z_{\rm SPT}[a]=(-1)^{\sum_{\rm cubes}a\cup a\cup a}\tag{5.7}
$$
is (5.5) on that triangulation. Its gauge invariance is the Leibniz rule mod 2. For flat $a$ ($da\equiv0$ mod 2), $(a+d\lambda)^{\cup3}-a^{\cup3}$ is a sum of seven products containing $d\lambda$, each exact mod 2: for instance $d\lambda\cup a\cup a=d(\lambda\cup a\cup a)-\lambda\cup d(a\cup a)$ with $d(a\cup a)=da\cup a-a\cup da\equiv0$, and $d(a\cup\lambda\cup a)\equiv a\cup d\lambda\cup a$; the others follow alike, using associativity and that products of cocycles are cocycles mod 2. On a closed lattice the exact terms sum to zero:
$$
\sum_{\rm cubes}(a+d\lambda)^{\cup3}\equiv\sum_{\rm cubes}a^{\cup3}\pmod 2 .\tag{5.8}
$$
On the $3^3$ torus we checked associativity, (5.6) on a random cochain, and (5.8) for random λ on all eight holonomy classes. On the harmonic representatives of [[week-02-lattice-cell-complex-cochains|Sem I Week 2]], $\sum a^{\cup3}$ is even for every class, as DW (6.35) requires for $\mathbb{Z}_2$: on $T^3$ the response is trivial.

```
   x+y ------------- x+x+y        2d: (a u b)(P_xy(x)) = a_x(x) b_y(x+x) - a_y(x) b_x(x+y)
    |            /  |                 lower triangle: path x -> x+x -> x+x+y    sign +
    |   (-)    /    |                 upper triangle: path x -> x+y -> x+x+y    sign -
    |        /      |
    |      /   (+)  |             3d: paths x -> x+e(p1) -> x+e(p1)+e(p2) -> x+e1+e2+e3,
    |    /          |                 one per permutation p of (1,2,3), sign sgn(p):
    x ------------- x+x               123 +   231 +   312 +   132 -   213 -   321 -
```
**Figure 3.** The cubical cup product triangulates (the labels write $\hat x,\hat y$ as x, y). In two dimensions its two terms are the two triangles of the plaquette; in three, the six terms of (5.6) are the six tetrahedra sharing the main diagonal.

### 5.4 The classification statement [Stated — refs: CGLW §§VI, X.]

CGLW show that the construction of §5.1, made into a lattice Hamiltonian or path integral, gives for every class in $H^d(G,U(1))$ a gapped symmetric phase with trivial bulk, that cohomologous cocycles give the same phase, and that distinct classes give distinct phases, as (5.5) suggests: $[\omega]$ is the topological action of the background, which no local counterterm changes. In $d=2$ this is §4, where the classification is complete; in $d=3$ the $\mathbb{Z}_2$ case has one nontrivial phase, built by Levin and Gu (§7). The classification is incomplete in general: bosons with time reversal in $3+1$ dimensions have phases beyond group cohomology (Vishwanath and Senthil), and fermions need more structure. Since $H^4(\mathbb{Z}_2,U(1))=0$, there is no group-cohomology $\mathbb{Z}_2$ SPT in $3+1$ dimensions.

## 6. Dijkgraaf–Witten theory as a gauged SPT

### 6.1 The partition function [Proved; the $T^3$ value Computed.]

Gauging the SPT of §5.3 with the normalized sum of [[sem2-week-04-gauging-backgrounds-and-dual-symmetry|Sem II Week 4]] (2.4) for a 0-form symmetry, $\mathcal N=1/|C^0|$, gives the $\mathbb{Z}_2$ Dijkgraaf–Witten theory with class $k\in\{0,1\}$,
$$
Z_k(M)=\frac1{2^{N_0}}\sum_{a\in Z^1(\Lambda,\mathbb{Z}_2)}(-1)^{k\sum_{\rm cubes}a\cup a\cup a}=\frac1{|H^0|}\sum_{[a]\in H^1(M,\mathbb{Z}_2)}(-1)^{k\langle a^3,[M]\rangle},\tag{6.1}
$$
the second form by (5.8) and Week 4 (2.5). This is DW (6.8), $Z(M)=|G|^{-1}\sum_{\gamma\in{\rm Hom}(\pi_1(M),G)}W(\gamma)$, with ${\rm Hom}(\pi_1(M),\mathbb{Z}_2)=H^1(M,\mathbb{Z}_2)$. At $k=0$, $Z_0=|H^1|/|H^0|$ is the $\mathbb{Z}_2$ BF theory of [[sem2-week-02-zn-gauge-theory-as-bf-theory|Sem II Week 2]] in the normalization of [[courses/generalized-symmetries-course/conventions|conventions]] §7, whose Hamiltonian is the [[toric-code]] at the $\Gamma\to0$ point of [[week-07-kogut-susskind-hamiltonian|Sem I Week 7]] §8. At $k=1$ the gauge field carries the response of the SPT as a topological action. On $T^3$, since $\sum a^{\cup3}$ is even on every class,
$$
Z_0(T^3)=Z_1(T^3)=\tfrac12\cdot8=4,\tag{6.2}
$$
in agreement with DW (6.34)–(6.36), whose weight $W(g,h,l)=c_g(h,l)\,c_g(l,h)^{-1}$ is 1 for $\mathbb{Z}_2$. $Z(T^3)$ counts the states on $T^2$, that is the anyons: both theories have four. The dual symmetry of Week 4, $\mathbb{Z}_2^{(d-2)}=\mathbb{Z}_2^{(1)}$ for a 0-form symmetry gauged in $d=3$, is generated by the Wilson line $(-1)^{\oint a}$, the worldline of the pure charge of §6.3.

### 6.2 Flux lines and their associator [Sketched.]

A puncture of a spatial surface carries a flux $x\in\mathbb{Z}_2$, read by the Wilson loop around it, and fluxes fuse by addition. For three punctures with fluxes $x,y,z$ in a disc, the two bases labelled by the fusion trees $((xy)z)$ and $(x(yz))$ of Figure 4 are related by the amplitude of the gauge theory on the cobordism in which the tree changes; triangulated with the vertex order of the trees, the elementary change is one tetrahedron whose spine carries $(x,y,z)$ [Heuristic], with weight (5.5):
$$
F(x,y,z)=\omega(x,y,z)=(-1)^{kxyz}.\tag{6.3}
$$
We omit the triangulation of this cobordism; DW carry out the analogous construction for $Y\times S^1$, with three simplices, in their §6.6, and §6.3 checks the outcome against their (6.32). What we use is structural: the flux sector is $\mathbb{Z}_2$ with associator ω, and the 2–3 move of §5.2 is its pentagon equation.

```
     x     y     z                      x     y     z
      \   /     /                        \     \   /
      (x+y)    /         =  F(x,y,z)      \    (y+z)
         \    /                            \    /
           |                                 |
         x+y+z                             x+y+z
```
**Figure 4.** The F-move for three fluxes: for abelian fluxes the two fusion trees differ by the phase $F(x,y,z)$, which in the gauged SPT is the cocycle ω.

### 6.3 Anyons as fluxes with half-braidings [Proved, given (6.3) and the ansatz $R(X,Y)=\chi_X(y)$.]

An anyon $X$ has a flux $x_X$ and is otherwise characterized by how it braids with fluxes: the phase $R(X,Y)$ of the counterclockwise exchange of $X$ and $Y$ depends on $Y$ only through its flux, $R(X,Y)=\chi_X(y)$. (In the untwisted theory $\chi_X$ is the $\mathbb{Z}_2$ charge of $X$ and $R(X,Y)$ its Aharonov–Bohm phase in the flux of $Y$.) The associator is $F(X,Y,Z)=\omega(x,y,z)$, and the data must satisfy the pentagon, which is $\delta\omega=1$, and the two hexagons of Kitaev's App. E, which for abelian anyons in our conventions read
$$
F(Y,Z,X)\,R(X,Y\!\otimes\!Z)\,F(X,Y,Z)=R(X,Z)\,F(Y,X,Z)\,R(X,Y),
$$
$$
F(Z,X,Y)^{-1}\,R(X\!\otimes\!Y,Z)\,F(X,Y,Z)^{-1}=R(X,Z)\,F(X,Z,Y)^{-1}\,R(Y,Z),\tag{6.4}
$$
with $F(X,Y,Z)$ the phase of $(X\otimes Y)\otimes Z\to X\otimes(Y\otimes Z)$ and $R(X,Y)$ that of $X\otimes Y\to Y\otimes X$. With $F=\omega$ and $R(X,Y)=\chi_X(y)$, the first hexagon becomes
$$
\chi_X(y)\,\chi_X(z)=c_x(y,z)\,\chi_X(y+z),\qquad c_x(y,z)=\frac{\omega(x,y,z)\,\omega(y,z,x)}{\omega(y,x,z)},\tag{6.5}
$$
exactly DW (6.32), the 2-cocycle they obtained from three simplices of $Y\times S^1$: $\chi_X$ is a $c_x$-projective character. The second hexagon fixes the fusion of half-braidings,
$$
x_{X\otimes Y}=x+y,\qquad\chi_{X\otimes Y}(z)=\chi_X(z)\,\chi_Y(z)\,\frac{\omega(x,y,z)\,\omega(z,x,y)}{\omega(x,z,y)} .\tag{6.6}
$$
For (2.5), $c_0\equiv1$ and $c_1(y,z)=1$ unless $y=z=1$, where $c_1(1,1)=\omega(1,1,1)=(-1)^k$. So $\chi(0)=1$ and $\chi(1)^2=c_x(1,1)$:
$$
\text{flux }0:\ \chi_X(1)=\pm1;\qquad\text{flux }1:\ \chi_X(1)=\pm1\ \ (k=0),\qquad\chi_X(1)=\pm i\ \ (k=1).\tag{6.7}
$$
Each theory has four anyons, as $Z(T^3)=4$ requires; DW §6.6 counts them the same way, as fluxes with irreducible $c_x$-projective representations of their stabilizers.

### 6.4 The $F$ and $R$ data and the spin of the semion [Computed.]

The topological spin of an abelian anyon is its self-exchange,
$$
\theta_X=R(X,X)=\chi_X(x),\tag{6.8}
$$
and the monodromy is $R(X,Y)R(Y,X)=\theta_{X\otimes Y}/(\theta_X\theta_Y)$. With (6.6)–(6.8) the two theories are those of Table 2.

| | $k=0$: toric code | | | | $k=1$: double semion | | | |
|---|---|---|---|---|---|---|---|---|
| anyon | $1$ | $e$ | $m$ | $\varepsilon$ | $1$ | $b$ | $s$ | $\bar s$ |
| $(x,\chi(1))$ | $(0,1)$ | $(0,-1)$ | $(1,1)$ | $(1,-1)$ | $(0,1)$ | $(0,-1)$ | $(1,i)$ | $(1,-i)$ |
| $\theta$ | $1$ | $1$ | $1$ | $-1$ | $1$ | $1$ | $i$ | $-i$ |

**Table 2.** The two $\mathbb{Z}_2$ Dijkgraaf–Witten theories. Toric code: $F\equiv1$, $m\otimes m=1$, $m\otimes\varepsilon=e$, and $R(X,Y)=\chi_X(y)$ is $-1$ for $(X,Y)=(e,m),(e,\varepsilon),(\varepsilon,m),(\varepsilon,\varepsilon)$ and $1$ otherwise. Double semion: $F(X,Y,Z)=-1$ if $X,Y,Z\in\{s,\bar s\}$, else $1$; $s\otimes s=\bar s\otimes\bar s=1$ and $s\otimes\bar s=b$, since (6.6) gives $\chi_{s\otimes s}(1)=i\cdot i\cdot(-1)=1$; $R(s,s)=R(s,\bar s)=i$, $R(\bar s,\bar s)=R(\bar s,s)=-i$, $R(b,s)=R(b,\bar s)=-1$, else $1$.

In the toric code $e$ and $m$ are the star and plaquette violations of [[courses/generalized-symmetries-course/conventions|conventions]] §9, with braiding phase $R(e,m)R(m,e)=-1$. A change of basis of the fusion spaces, $u(X,Y)$, multiplies $F$ by $\delta u$ and $R(X,Y)$ by $u(X,Y)/u(Y,X)$ [Stated — refs: Kitaev, App. E]. Two quantities survive: $\theta_X=R(X,X)$, and, for an anyon $s$ with $s\otimes s=1$, the class of the restriction of $F$ to $\{1,s\}$, a 3-cocycle on $\mathbb{Z}_2$ with invariant $I=F(s,1,s)F(s,s,s)$ by (2.6). In a normalized gauge the first hexagon at $X=Y=Z=s$, with $R(s,1)=1$, reads $F(s,s,s)^2=R(s,s)^2F(s,s,s)$:
$$
\theta_s^2=F(s,s,s)=I .\tag{6.9}
$$
The spin of an anyon of order two squares to the class of its associator. In the toric code $F$ is trivial and $\theta_m,\theta_\varepsilon=\pm1$; in the gauged nontrivial SPT, $F$ on the flux sector is the nontrivial class of $H^3(\mathbb{Z}_2,U(1))$ and the hexagon forces $\theta_s=\pm i$: the flux is a semion. The spins $\{1,1,1,-1\}$ and $\{1,1,i,-i\}$ are gauge invariant and differ, so the theories are inequivalent, and (6.9) is the reason: the class of §2.3 reappears as the spin of the flux. The subtheory $\{1,s\}$, with $F(s,s,s)=-1$ and $R(s,s)=i$, is the semion theory, $\{1,\bar s\}$ its mirror image; $s$ and $\bar s$ braid trivially and the double semion is their product. Both theories are non-chiral: $\frac1{\mathcal D}\sum_X\theta_X=1$ with $\mathcal D=2$, so $c\equiv0$ mod 8 by Kitaev's App. E relation [Stated]. We checked by computer that (6.6) closes on (6.7), that the pentagon and both hexagons hold for all labels at $k=0,1$, the monodromy identity, and that the first hexagon on a $\mathbb{Z}_2$ fusion rule admits $R(s,s)=\pm1$ for $F(s,s,s)=1$ and only $\pm i$ for $F(s,s,s)=-1$.

> **Physical picture.** The spin of a charge–flux composite is the Aharonov–Bohm phase of its charge in its own flux, $e^{i\pi q}$ for a $\mathbb{Z}_2$ flux: $q=0$ gives $m$, $q=1$ gives ε. In the double semion the symmetry squares to $c_1(1,1)=-1$ on a flux, $\chi(1)=e^{\pm i\pi/2}$, as if the flux carried half a $\mathbb{Z}_2$ charge, and its spin is $e^{\pm i\pi/2}$. This is the $2+1$d version of the projective edge of §4.4: the symmetry is projective on a defect, and the bulk class forces it [Heuristic reading of (6.5)–(6.9)]. Levin and Gu use exactly this observable to tell their two paramagnets apart.

### 6.5 The Hamiltonians [Stated — refs; forward references.]

At $k=0$, gauging the paramagnet $-\sum\sigma^x$ operator by operator, as Week 4 §3 did for the Ising chain, gives the toric code $-\sum A_v-\sum B_p$ of [[courses/generalized-symmetries-course/conventions|conventions]] §9, which Sem II Week 8 solves completely. At $k=1$, Levin and Gu gauge their paramagnet $H_1$, whose site terms carry the phases $i^{(1-\sigma^z_q\sigma^z_{q'})/2}$, and obtain a model that maps onto the doubled-semion string net of Levin and Wen, the subject of Week 11 (forward reference). Week 10 treats the quantum doubles $D(G)$ and their modular data, the toric code being the simplest (forward reference); the twisted doubles $D^\omega(G)$, of which the double semion is the abelian $\mathbb{Z}_2$ case, are beyond the course.

## 7. Seminar: Levin–Gu, braiding statistics of gauged SPTs

**Format.** The presenter states the paper's technical claim, identifies what it needs from Semester I and reproduces one nontrivial step at the board; discussion follows, and the instructor places the result on the course map (syllabus §7). Every student reads the sections and brings Problem 4.

**Sections.** Levin–Gu §I, §II (the paramagnets $H_0=-\sum_p\sigma^x_p$ and $H_1=-\sum_pB_p$, eqs. (1)–(3)), §III (coupling to a $\mathbb{Z}_2$ gauge field; the statistics of π fluxes) and §V.A (the argument for protected edge modes).

**The technical claim.** $H_0$ and $H_1$ are $\mathbb{Z}_2$-symmetric paramagnets with unique gapped ground states in different phases: after minimal coupling to a $\mathbb{Z}_2$ gauge field the π fluxes of the gauged $H_0$ are bosons or fermions and those of the gauged $H_1$ are semions, so the two cannot be connected without breaking the symmetry or closing the gap.

**What it needs from Semester I.** The $\mathbb{Z}_2$ Kogut–Susskind Hamiltonian and its toric-code point (Sem I Week 7 §§7.1, 8); minimal coupling and the Gauss law, done for the Ising chain in Sem II Week 4 §3; braiding from linking (Sem II Week 2 §5).

**The step at the board.** Levin–Gu §III, eqs. (11)–(16): the string operators $V^0_\beta$ and $V^1_\beta$ that create pairs of π fluxes in the gauged $H_0$ and $H_1$; the relation $V_\beta V_\gamma|0\rangle=e^{2i\theta}V_\gamma V_\beta|0\rangle$ for a closed β crossing an open γ, which reads the statistical angle θ off the string algebra; and the conclusion that commuting strings, their (12), give $\theta\in\{0,\pi\}$ while anticommuting ones, their (16), give $\theta=\pm\pi/2$. The presenter closes by comparing $e^{2i\theta}=-1$ with (6.9), $\theta_s^2=F(s,s,s)=-1$. The mini-step of the week, the edge doublet (3.12) and the two theories of Table 2, is done in the lectures.

**For the discussion.** Levin and Gu identify the phase by gauging; the course reached the same distinction through the response (5.5), and the two must agree because (6.1) is the gauged form of (5.7). Their §V.A argues that a symmetric gapped edge would contradict the semionic statistics: compare with §4.4 and with the anomaly matching of Week 5.

**The open question it leaves for this course.** The $\mathbb{Z}_N$ Dijkgraaf–Witten theories with the cubical cup product of [[courses/generalized-symmetries-course/conventions|conventions]] §8 (Problem 8⋆⋆).

**On the course map.** The gauged $H_0$ is the deconfined phase of Sem I Week 5 at its soluble point; the gauged $H_1$ is a different deconfined $\mathbb{Z}_2$ gauge theory with the same degeneracy; Block 3 solves both.

## 8. Subtleties and fine print

**F1. Injectivity separates SPT from symmetry breaking.** The GHZ state, $A^s=|s\rangle\langle s|$, is not injective: its products span the diagonal matrices only, $E$ has the eigenvalue 1 twice, and the $V$ of (4.3) for $\prod X$ is not unique up to a phase ($V=X$ and $V=XZ$ both work), so no class is defined. It is a cat state of the two broken product states, and the injectivity hypothesis of §4 excludes it.

**F2. The order of composition.** With $u\cdot A=VAV^\dagger$ the same algebra gives $V_{gh}\propto V_hV_g$, with the transposed cocycle $\omega(h,g)$ and inverted commutator phases. For a finite abelian group a class is fixed by its commutator phases, so the transposed convention inverts the class: harmless for $\mathbb{Z}_2\times\mathbb{Z}_2$, a sign error for $\mathbb{Z}_N\times\mathbb{Z}_N$, $N>2$. The choice of ω or $\omega^{-1}$ in (6.3) is the same issue: immaterial for $\mathbb{Z}_2$, where $\omega=\omega^{-1}$, and the mirror theory, $k\to-k$, for $\mathbb{Z}_N$.

**F3. Same degeneracy, different theory.** Both theories have $Z(T^3)=4$ and, with four abelian anyons, $4^g$ states on $\Sigma_g$, the count of Sem II Week 2 §4 for $k=0$. A partition function separates them only on a 3-manifold with $\langle a^3,[M]\rangle\ne0$: with $H^*(\mathbb{RP}^3,\mathbb{Z}_2)=\mathbb{Z}_2[x]/(x^4)$ [Stated], (6.1) gives $Z_0(\mathbb{RP}^3)=\tfrac12(1+1)=1$ and $Z_1(\mathbb{RP}^3)=\tfrac12(1-1)=0$. These are $\tfrac14\sum_X\theta_X^2$, the value $(ST^2S)_{00}$ of a TQFT on $L(2,1)=\mathbb{RP}^3$ [Stated] with $S_{0X}=\tfrac12$: 1 for the toric-code spins and 0 for $\theta_s=\pm i$, a class-level check of §6.2.

**F4. Why the cubic formula is special to $\mathbb{Z}_2$.** For $\mathbb{Z}_N$ the representatives of $H^3$ are $\omega_k(x,y,z)=\exp\big(\tfrac{2\pi ik}{N}\,x\,{\rm carry}(y,z)\big)$, ${\rm carry}(y,z)=1$ if $y+z\ge N$ and 0 otherwise (Problem 5⋆). For $N=2$ the carry is $yz$, which makes (2.5) a triple product and (5.7) a triple cup product; for $N>2$ it is the Bockstein of the integer lift, and the cubical weight needs care (Problem 8⋆⋆). Throughout, the symmetries are unitary and the systems bosonic; antiunitary symmetries twist the coefficients.

## 9. Common misconceptions

**"An SPT has a trivial bulk, so gauging it gives the same theory as gauging a product state."** It is tempting because (5.4) makes the partition function 1 on every closed manifold. The bulk is trivial only without background; the response (5.5) is a nontrivial topological action, and gauging turns it into the double semion instead of the toric code.

**"The Haldane edge spin is protected by $SU(2)$."** It is tempting because AKLT is rotation invariant and its edge is a spin $\tfrac12$. Any symmetry whose virtual representation has a nontrivial class protects it, the π rotations by (4.9); and two stacked Haldane chains are rotation invariant with no protected edge (Problem 3).

## 10. Historical note

Haldane (1983) mapped the large-spin Heisenberg chain onto the O(3) nonlinear σ model with a topological angle $2\pi S$ and argued that integer-spin chains are gapped. Affleck, Kennedy, Lieb and Tasaki (1987) gave the rigorous example, the Hamiltonian (3.10) with the valence-bond ground state of Figure 2, unique on the ring, with exponentially decaying correlations and a gap. den Nijs and Rommelse (1989) found the hidden order measured by the string operator of Problem 1. The reading as symmetry protection came two decades later: Pollmann, Turner, Berg and Oshikawa (2010) identified the protecting symmetries through the entanglement spectrum, Chen, Gu and Wen (2011) classified gapped spin chains by projective representations using the theorem Pérez-García et al. had proved in 2008 in the context of string order, and Chen, Gu, Liu and Wen extended the construction to cocycles in every dimension. Dijkgraaf and Witten (1990) had met the same cocycles from gauge theory: they chose a class in $H^3(BG,U(1))\cong H^4(BG,\mathbb{Z})$ as the action of a finite-group gauge theory, realized it on triangulations with group elements on links (§6.4), and computed the cocycle (6.32) and the 3-torus partition function by hand, in the language of Hilbert spaces and projective representations. Levin and Gu (2012) joined the two lines by gauging an SPT and reading its class off the statistics of the fluxes.

## 11. What to take away

1. **Technical:** a symmetry of an injective MPS acts on the virtual index by conjugation, (4.3), through a projective representation whose class in $H^2(G,U(1))$ survives gauge, blocking, stacking with product states and deformation. **Physical:** the edge carries that representation, (4.6); the Haldane edge doublet is protected for this reason.
2. **Technical:** the AKLT transfer matrix, with spectrum $1,-\tfrac13,-\tfrac13,-\tfrac13$, gives $\xi=1/\ln3$, four independent edge states and the edge magnetization $2(-1)^{j-1}3^{-j}$ summing to $\tfrac12$. **Physical:** the virtual spin is a measurable spin $\tfrac12$ at each end.
3. **Technical:** $H^3(\mathbb{Z}_2,U(1))=\mathbb{Z}_2$ with representative $(-1)^{xyz}$; the cocycle condition is the Pachner move, and on the cubic lattice the weight is $(-1)^{\sum a\cup a\cup a}$. **Physical:** a higher-dimensional SPT is a topological action for the background of its symmetry.
4. **Technical:** gauging gives (6.1), whose anyons are fluxes with $c_x$-projective half-braidings, and $\theta_s^2=F(s,s,s)$. **Physical:** the double-semion fluxes are semions because their associator is the nontrivial class.

## 12. Looking ahead

Block 3 starts from the two theories of §6. Sem II Week 8 solves the toric code to the bone, with the anyons $e,m,\varepsilon$ of Table 2 as excitations of a Hamiltonian; Week 9 turns to long-range entanglement and error correction; Week 10 develops the quantum doubles of finite groups and their modular data, the toric code being the simplest (the twisted doubles behind the double semion are beyond the course); Week 11 builds the double semion as a string net. Block 2 closes here: the anomalies of Week 5 live on the boundaries of the SPT phases of this week, and gauging those phases produces the topological orders that Block 3 diagonalizes.

## 13. Problem set

Problems 1–4 are the classroom core; 5⋆–7⋆ consolidate the self-study sections; 8⋆⋆–9⋆⋆ are research extensions.

### Core problems

**1. String order of the AKLT chain** (extends §§3.2, 4.5). (a) Show that $E_\pi(X)\equiv\sum_se^{i\pi m_s}A^sXA^{s\dagger}=V^\dagger E(VX)$ with $V=i\sigma^z$, and deduce $E_\pi(\sigma^z)=\sigma^z$. (b) From (3.5) and (3.8), compute $\mathcal O(r)=\big\langle S^z_j\,e^{i\pi\sum_{j<l<j+r}S^z_l}\,S^z_{j+r}\big\rangle$ for $r\ge1$. (c) Explain from (4.8) why the same value is obtained with $x$ in place of $z$.

**2. No $1+1$d SPT for a cyclic group** (extends §§2.2, 4.2). (a) For a projective representation $V_n$ of $\mathbb{Z}_N$, show that $V_1^N=c\,\mathbb 1$ and construct phases $\beta(n)$ making $\beta(n)V_n$ linear. (b) Conclude $H^2(\mathbb{Z}_N,U(1))=0$ and that a $\mathbb{Z}_N$-symmetric injective MPS is in the trivial class. (c) Where does the argument fail for $\mathbb{Z}_N\times\mathbb{Z}_N$?

**3. Stacking Haldane chains** (extends §§4.3(c), 4.4, 4.5). (a) For two AKLT chains with the π rotations acting on both, show that the virtual operators are $V_a\otimes V_a$ and compute (4.9) for the stack. (b) Each end of the open double chain carries two spins $\tfrac12$; show that the symmetric coupling $J\,\mathbf S^{(1)}\cdot\mathbf S^{(2)}$, $J>0$, leaves a unique end state. (c) Stack an AKLT chain with a cluster chain blocked as in §4.6, with $R_x(\pi)\leftrightarrow U_a$, $R_z(\pi)\leftrightarrow U_b$: which class?

**4. Monodromy and Gauss sums** (extends §6.4). (a) From Table 2, compute $M_{XY}=\theta_{X\otimes Y}/(\theta_X\theta_Y)$ for both theories and check $M_{XY}=R(X,Y)R(Y,X)$. (b) Show that every toric-code anyon has $M_{XX}=1$ and find the double-semion anyons with $M_{XX}=-1$. (c) Compute $\frac1{\mathcal D}\sum_X\theta_X$, $\mathcal D=2$, for both.

### Starred problems

**5⋆. $H^3(\mathbb{Z}_N,U(1))=\mathbb{Z}_N$** (extends §2.3). (a) Show that $\omega_k(x,y,z)=\exp\big(\tfrac{2\pi ik}N\,x\,{\rm carry}(y,z)\big)$ is a 3-cocycle. (b) Show that $I(\omega)=\prod_{y=0}^{N-1}\omega(1,y,1)$ is coboundary invariant and $I(\omega_k)=e^{2\pi ik/N}$. (c) Conclude that the $\omega_k$ are pairwise inequivalent and, with $|H^3(\mathbb{Z}_N,U(1))|=N$ (Table 1 for $N=2,3,4$), exhaust the group. *Hint:* additively, δ of $\tfrac kN\,x\,{\rm carry}(y,z)$ is the integer $k\,{\rm carry}(w,x)\,{\rm carry}(y,z)$, by ${\rm carry}(x,y)+{\rm carry}(x+y,z)={\rm carry}(y,z)+{\rm carry}(x,y+z)$; in (b) the coboundary terms telescope around $y\to y+1$.

**6⋆. Spins of the $\mathbb{Z}_N$ theories** (extends §§6.3–6.4). With $\omega_k$ of Problem 5⋆, show $c_x(y,z)=\exp\big(\tfrac{2\pi ik}N\,x\,{\rm carry}(y,z)\big)$, solve (6.5), and show that the flux-$x$ anyons have $\theta_{(x,n)}=\exp\big(2\pi i(\tfrac{xn}N+\tfrac{kx^2}{N^2})\big)$, $n\in\mathbb{Z}_N$; check $N=2$, $k=1$ against Table 2. *Hint:* (6.5) at $z=1$ is the recursion $\chi(y+1)=\chi(y)\chi(1)/c_x(y,1)$, which closes only if $\chi(1)^N=e^{2\pi ikx/N}$.

**7⋆. The $1+1$d cocycle response on the torus** (extends §§5.1–5.2 and Sem II Week 5 §5.3). (a) For an abelian $G$ and $\omega\in Z^2(G,U(1))$, evaluate (5.5) on the one-plaquette torus split into the two triangles of Figure 3, with holonomies $g$ along $x$ and $h$ along $y$, and show that $Z_{\rm SPT}=\omega(g,h)/\omega(h,g)$, the commutator phase $c(g,h)$ of Week 5 (3.4). (b) Explain from §5.2 why the same value holds on the $L\times L$ torus. (c) For $\mathbb{Z}_2\times\mathbb{Z}_2$ and $\omega(g,h)=(-1)^{g_1h_2}$, show that the result is $(-1)^{g_1h_2+g_2h_1}$, the response (5.8) of Week 5, and explain with (4.6) why the torus response of the bulk is the commutator phase of the edge representation. *Hint:* the two triangles carry $\omega(g,h)^{+1}$ and $\omega(h,g)^{-1}$; for the general torus use triangulation independence and gauge invariance; DW §6.7 calls the ratio discrete torsion.

### ⋆⋆ problems

**8⋆⋆. $\mathbb{Z}_N$ Dijkgraaf–Witten theory on the cubic lattice.** *Known:* the simplicial weight of DW §6.4 and the $\mathbb{Z}_2$ cubical form (5.7). *Sources:* DW §6.4; Chen–Tata (arXiv:2106.05274) for higher cup products on hypercubic lattices, translated by [[courses/generalized-symmetries-course/conventions|conventions]] §8. *Explored:* whether $\exp\big(\tfrac{2\pi ik}{N^2}\sum_{\rm cubes}\tilde a\cup d\tilde a\big)$, with $\tilde a$ the $\{0,\dots,N-1\}$ lift, is invariant under $a\to a+d\lambda$ mod $N$, and how it compares with $\omega_k$ summed over the six tetrahedra of Figure 3, whose diagonal links the lattice lacks. *Completion:* a proof of gauge invariance or a counterexample on $T^3$ with $L\ge3$; if invariant, $Z_k(T^3)=N^2$ for every $k$ and the spins of Problem 6⋆ from a lattice computation.

**9⋆⋆. The SPT phase as a computational resource.** *Known:* teleportation along the cluster chain (§4.6) and the wire property throughout the $\mathbb{Z}_2\times\mathbb{Z}_2$ phase. *Sources:* Raussendorf–Briegel 2001; Else, Schwarz, Bartlett, Doherty 2012. *Explored:* how (4.3) controls the byproducts of a measurement, which applies $\sum_s\langle\phi|s\rangle A^s$ to the virtual space. *Completion:* for a normalized injective $\mathbb{Z}_2\times\mathbb{Z}_2$-symmetric MPS with $D=2$ in the nontrivial class, a derivation that measuring a generator's eigenbasis implements a fixed virtual unitary up to byproducts in $\{V_g\}$, reproducing $H$ and $HZ$ for (4.10), and the comparison with Else et al. for $D>2$.

## Self-study answer checkpoints

**Problem 1.** *Decisive step:* $e^{i\pi m_s}A^s=V^\dagger A^sV$ ($e^{i\pi S^z}=e^{-i\pi S^z}$ on spin 1), so $E_\pi(X)=V^\dagger E(VX)$ and $E_\pi(\sigma^z)=(-i\sigma^z)E(i\mathbb 1)=\sigma^z$: the string acts on the virtual space by $V$, which commutes with $\sigma^z$. *Result:* $\mathcal O(r)={\rm tr}\big[\tfrac{\mathbb 1}2E_{S^z}(\tfrac23\sigma^z)\big]=-\tfrac49$ for every $r\ge1$, equal to (3.9) at $r=1$; the same for $x$ by rotation covariance. *Common failure:* propagating the string sites with $E$ instead of $E_\pi$, which reproduces the decaying (3.9), or dropping $\rho=\mathbb 1/2$, which doubles the answer.

**Problem 2.** *Decisive step:* $V_0=\omega(0,0)\mathbb 1$ and $V_1V_n\propto V_{n+1}$, so $V_n\propto V_1^n$ for $0\le n<N$ and $V_1^N\propto\mathbb 1$; with $\mu^N=c$, $V'_n=(\mu^{-1}V_1)^n$ satisfies $V'_mV'_n=V'_{m+n\bmod N}$. *Result:* every 2-cocycle of $\mathbb{Z}_N$ is a coboundary and the class of a $\mathbb{Z}_N$-symmetric MPS is trivial; for $\mathbb{Z}_N\times\mathbb{Z}_N$ the commutator of the generators is rephasing invariant, $e^{2\pi i/N}$ for clock and shift. *Common failure:* rescaling only $V_1$ without fixing the other phases, or setting $V_1^N=\mathbb 1$ without the scalar $c$.

**Problem 3.** *Decisive step:* (4.3) layer by layer gives $(V\otimes V)^\dagger(A\otimes A)(V\otimes V)$. *Result:* (a) commutator $(-1)^2=+1$, trivial; (b) $\tfrac12\otimes\tfrac12=0\oplus1$, singlet at $-\tfrac34J$ below the triplet at $+\tfrac14J$, unique; (c) $V_a=\sigma^x\otimes Z$, $V_b=i\sigma^z\otimes X$, commutator $(-1)(-1)=+1$, trivial. *Common failure:* multiplying the classes of the two ends of one chain, inverse by (4.6), instead of those of the two layers at one end.

**Problem 4.** *Decisive step:* the fusion rules from (6.6), $s\otimes s=1$ and $s\otimes\bar s=b$. *Result:* rows of $M$ in the order $(1,e,m,\varepsilon)$: $(1,1,1,1)$, $(1,1,-1,-1)$, $(1,-1,1,-1)$, $(1,-1,-1,1)$; in the order $(1,b,s,\bar s)$: $(1,1,1,1)$, $(1,1,-1,-1)$, $(1,-1,-1,1)$, $(1,-1,1,-1)$, so $M_{ss}=M_{\bar s\bar s}=-1=\theta_s^{-2}$ and $M_{s\bar s}=1$; both Gauss sums equal 1. *Common failure:* normalizing by $\mathcal D^2=4$ instead of $\mathcal D=2$, which gives $\tfrac12$, not a phase.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester II Block 2. Written to the note-quality-template standard on 2026-10-02. Last revised 2026-10-02.*
