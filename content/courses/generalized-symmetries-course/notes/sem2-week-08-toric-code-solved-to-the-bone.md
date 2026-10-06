---
title: "Sem II Week 8 — The Toric Code, Solved to the Bone"
type: lecture-notes
course: syllabus
semester: 2
week: 8
block: 3
duration: 4 hours (3 hr lectures + 1 hr seminar, the first seminar of Block 3, presented by the instructor)
prerequisites: Sem II Weeks 2, 3 and 7; Semester I Weeks 2, 7 and 13–15
modified: 2026-10-04
---

# Sem II Week 8 — The Toric Code, Solved to the Bone

> *The [[toric-code]] has appeared three times in this course: at the Γ → 0 point of the $\mathbb{Z}_2$ Kogut–Susskind Hamiltonian in [[week-07-kogut-susskind-hamiltonian|Sem I Week 7]], as BF theory in [[sem2-week-02-zn-gauge-theory-as-bf-theory|Sem II Week 2]], and as the gauged trivial paramagnet in [[sem2-week-07-spt-phases-group-cohomology-dijkgraaf-witten|Sem II Week 7]]. This week we solve the lattice model with the Pauli algebra as the only input: the stabilizer group and its two relations, the $2^{2g}$ ground states on a surface of genus $g$, the string operators with every fusion and braiding rule, and the modular $S$ and $T$ matrices. Then we perturb it. Each field of the Fradkin–Shenker problem condenses one anyon and confines the other, so the phase diagram of [[week-13-fradkin-shenker-gauge-higgs|Sem I Week 13]] is a diagram of two anyon condensations. Sem II Week 9 builds on the logical operators of §3.4, and [[sem2-week-10-beyond-z2-quantum-doubles-modular-data-chern-simons|Sem II Week 10]] matches the modular data of §5 to a $K$-matrix.*

### How to use this chapter

- **In class:** in the first hour, the dimension theorem (2.3), then the spectrum (3.1)–(3.3) with Figure 1, the two relations (3.4)–(3.5), the count (3.6) and the logical operators (3.9)–(3.10) with Figure 2; Problem 1. In the second hour, the strings (4.1)–(4.2), fusion (4.3)–(4.5), braiding (4.6)–(4.7) and the T-junction (4.8)–(4.11) with Figure 3, then the bases (5.1)–(5.3) and $S$ (5.5); Problem 2. In the third hour, $T$ (5.6)–(5.8) and the modular relations (5.9), then §§7.1 and 7.3–7.5 with Figure 4; Problem 3. The seminar hour (§8) is Kitaev's section on materialized symmetry, presented by the instructor; students bring Problem 4.
- **For self-study:** §§3.5, 4.5, 6, 7.2 and 7.6, the fine print of §9 and Problems 5⋆–7⋆. The one calculation to do alone is the $S$ matrix by overlaps, (5.4)–(5.5), from (5.3).
- **Instructor checkpoint:** two errors recur. The Wilson loop along $x$ anticommutes with the electric cut along $y$, so the $m$-string that runs along $x$ belongs to the second qubit, (3.10) and F1. And $\theta_\varepsilon=-1$ is $\theta_e\theta_mM_{em}$, the mutual braiding of the constituents, which on the torus is the sign of one crossing in (5.8).

## 0. Reading

**Primary:** Kitaev, "Fault-tolerant quantum computation by anyons", quant-ph/9707021, *Ann. Phys.* 303 (2003) 2: in the arXiv text, whose introduction is unnumbered, §1 (toric codes, with the stability estimate), §2 (abelian anyons) and §3 (materialized symmetry, the seminar of §8); Sem II Week 2 §8 numbers these sections 2–4.

**Secondary:** Levin, Wen, *Phys. Rev. B* 67 (2003) 245316 [cond-mat/0302460], eq. (4) of §III and §V; Kitaev, *Ann. Phys.* 321 (2006) 2 [cond-mat/0506438], App. E.4–E.5; Trebst, Werner, Troyer, Shtengel, Nayak, *Phys. Rev. Lett.* 98 (2007) 070602 [cond-mat/0609048]; Tupitsyn, Kitaev, Prokof'ev, Stamp, *Phys. Rev. B* 82 (2010) 085114 [arXiv:0804.3175]. From the course: Sem I Weeks 7 (§§7–8) and 13 (§§6–7, 9, F5); Sem II Weeks 2 (§§3–4, 6.4, 7), [[sem2-week-03-spontaneous-breaking-of-higher-form-symmetries|3]] (§2) and 7 (§6.4).

**Optional research reading:** Bais, Slingerland, *Phys. Rev. B* 79 (2009) 045316 [arXiv:0808.0627]; Wen, *Int. J. Mod. Phys. B* 4 (1990) 239; Wen, Niu, *Phys. Rev. B* 41 (1990) 9377; Somoza, Serna, Nahum, *Phys. Rev. X* 11 (2021) 041008 [arXiv:2012.15845]; Dennis, Kitaev, Landahl, Preskill, quant-ph/0110143 (Week 9).

**Proof-status labels** as in note-quality-template §4. Signs are from [[courses/generalized-symmetries-course/conventions|conventions]] §§4, 6 and 9; $S$ and $T$ are those of Kitaev's App. E, (223) and (232)–(233), as in Sem II Week 10 (6.1). Every count, commutation phase and modular relation was checked by script with explicit stabilizer matrices or state vectors, named where used.

## 1. Motivation and setting

The deconfined phase of $\mathbb{Z}_2$ gauge theory in $2+1$ dimensions contains one point where every question has an exact answer: the electric term is off, the Gauss law is an energy, and the Hamiltonian is a sum of commuting operators. We use it to answer three questions with the Pauli algebra alone. Why does the number of ground states depend on the topology of space, and only on it? What are the fusion rules, braiding phases and spins of the excitations? What destroys the order under perturbation? The first answer is a third derivation of the degeneracy, after BF holonomies (Sem II Week 2 §§3–4) and the Dijkgraaf–Witten sum (Sem II Week 7 §6.1). The second fixes the modular data. The third is where the semesters meet: when the gap of a moving boson closes, the boson condenses, the anyon that braids with it is confined, and the [[topological-order]] is lost; these are the Higgs and confinement transitions of Sem I Week 13, seen from the anyons.

## 2. The stabilizer formalism [Proved.]

### 2.1 Pauli strings

On $n$ qubits let $X(a)Z(b)=\prod_jX_j^{a_j}\prod_jZ_j^{b_j}$, $a,b\in\mathbb{Z}_2^n$. Moving $Z(b)$ past $X(a')$ costs $(-1)^{b\cdot a'}$ and $X(a)$ past $Z(b')$ costs $(-1)^{a\cdot b'}$, so
$$
X(a)Z(b)\,X(a')Z(b')=(-1)^{a\cdot b'+b\cdot a'}\,X(a')Z(b')\,X(a)Z(b),\tag{2.1}
$$
where $a\cdot b'=\sum_ja_jb'_j$ mod 2; the exponent is a nondegenerate alternating form on $\mathbb{Z}_2^{2n}$.

### 2.2 The dimension theorem

A stabilizer group $\mathcal S$ is a group of commuting Hermitian Pauli strings, signs allowed, not containing $-1$; its code space is $V_{\mathcal S}=\{\psi:\ s\psi=\psi\ \forall s\in\mathcal S\}$. The operator
$$
\Pi=\frac1{|\mathcal S|}\sum_{s\in\mathcal S}s\tag{2.2}
$$
is Hermitian and satisfies $s\Pi=\Pi$ for $s\in\mathcal S$, since multiplication by $s$ permutes the group; so $\Pi^2=\Pi$ and Π projects onto $V_{\mathcal S}$. Every $s\neq1$ in $\mathcal S$ is ± a nontrivial, traceless Pauli string, since a scalar other than 1 would be $-1$ or square to it. Thus
$$
\dim V_{\mathcal S}={\rm tr}\,\Pi=\frac{2^n}{|\mathcal S|}=2^{n-r},\tag{2.3}
$$
with $|\mathcal S|=2^r$ and $r$ the rank over $\mathbb{Z}_2$ of the binary check matrix of the generators ($s\mapsto(a,b)$ is injective on $\mathcal S$). Applied to the group generated by $\sigma_ig_i$, for linearly independent generators $g_i$ and any signs $\sigma_i=\pm1$, the same argument gives
$$
\dim\{\psi:\ g_i\psi=\sigma_i\psi,\ i=1,\dots,r\}=2^{n-r}.\tag{2.4}
$$

### 2.3 Logical operators

The centralizer $\mathcal C(\mathcal S)$, the Pauli strings commuting with all of $\mathcal S$, maps $V_{\mathcal S}$ to itself, and elements differing by an element of $\mathcal S$ act identically on it. In binary language $\mathcal S$ is an $r$-dimensional subspace $W$ on which the form of (2.1) vanishes, $\mathcal C(\mathcal S)$ is $W^\perp$, of dimension $2n-r$, and $W\subset W^\perp$. The quotient $W^\perp/W$ has dimension $2(n-r)$ and a nondegenerate induced form, and therefore a symplectic basis: $k=n-r$ pairs $(\bar Z_i,\bar X_i)$ with $\bar Z_i\bar X_j=(-1)^{\delta_{ij}}\bar X_j\bar Z_i$, all other pairs commuting. This is Kitaev's description of the protected space by the operators commuting with the stabilizers modulo the ideal they generate.

## 3. The toric code on a closed surface

### 3.1 The Hamiltonian and its spectrum [Proved; the $2\times3$ spectrum Computed.]

Let Σ be a closed connected surface cellulated by $V$ vertices, $E$ edges and $F$ faces, with a qubit on each edge. On the $L_1\times L_2$ square torus, $h(x,y)$ is the link from $(x,y)$ to $(x+1,y)$, $v(x,y)$ the link from $(x,y)$ to $(x,y+1)$, and $p(x,y)$ the plaquette with lower-left corner $(x,y)$. With [[courses/generalized-symmetries-course/conventions|conventions]] §9,
$$
H_{\rm TC}=-\sum_vA_v-\sum_pB_p,\qquad A_{(x,y)}=X_{h(x,y)}X_{h(x-1,y)}X_{v(x,y)}X_{v(x,y-1)},\qquad B_{p(x,y)}=Z_{h(x,y)}Z_{v(x+1,y)}Z_{h(x,y+1)}Z_{v(x,y)} .\tag{3.1}
$$
A star and a plaquette share no link, or two when $v$ is a corner of $p$, so by (2.1) all terms commute, and $A_v^2=B_p^2=1$ (Figure 1). With eigenvalues $a_v,b_p=\pm1$,
$$
E=-\sum_va_v-\sum_pb_p=E_0+2(n_e+n_m),\qquad E_0=-(V+F),\tag{3.2}
$$
where $n_e$, $n_m$ count violated stars and plaquettes. Every link has two ends and borders two faces, so $\prod_vA_v=\prod_pB_p=1$ and $n_e$, $n_m$ are even. These are the only relations (§3.2), so (2.4), applied to all generators but one star and one plaquette, gives every allowed pattern the degeneracy $2^{E-V-F+2}$. On the $N$-site torus the level $E_0+2n$ is
$$
d_n=4\sum_{\substack{n_e+n_m=n\\ n_e,\,n_m\ {\rm even}}}\binom N{n_e}\binom N{n_m}\tag{3.3}
$$
times degenerate, with $\sum_nd_n=2^{2N}$. On the $2\times3$ torus, $d_n=4,120,1020,1808,1020,120,4$ at $E=-12,\dots,12$, as brute-force diagonalization of the $4096\times4096$ matrix confirms. A pair of anyons costs 4 at every separation: no string tension.

![[gs-s2w08-stabilizers-strings.svg|The star operator at a vertex v with X on its four links, the plaquette operator at p with Z on its four links, a string of Z on a direct path with an e at each end, and a string of X on the links crossed by a dual path with an m in each end plaquette]]

**Figure 1. The star and plaquette of (3.1) and the open strings of (4.1): $Z$ on a direct path puts an $e$ at each end; $X$ on the links crossed by a dual path puts an $m$ in each end plaquette.**

### 3.2 The two global relations [Proved.]

A product $\prod_vA_v^{\alpha_v}\prod_pB_p^{\beta_p}$, with $\alpha\in C^0(\Sigma,\mathbb{Z}_2)$ and $\beta\in C_2(\Sigma,\mathbb{Z}_2)$, equals $X(d\alpha)Z(\partial\beta)$, with $d$ the coboundary of [[courses/generalized-symmetries-course/conventions|conventions]] §1 mod 2 and ∂ the mod-2 boundary. It is the identity exactly when $d\alpha=0$, which makes α constant on the connected Σ, and $\partial\beta=0$, which makes β equal on the two faces bordering each edge and so constant. These are $H^0(\Sigma,\mathbb{Z}_2)=H_2(\Sigma,\mathbb{Z}_2)=\mathbb{Z}_2$, and they give exactly two relations,
$$
\prod_vA_v=1,\qquad\prod_pB_p=1,\tag{3.4}
$$
so that
$$
|\mathcal S|=2^{V-1}\cdot2^{F-1},\qquad r=V+F-2 .\tag{3.5}
$$
The only element of $\mathcal S$ proportional to the identity is the product with α, β constant, which is $+1$, a product of $X_\ell^2$ and $Z_\ell^2$; so $-1\notin\mathcal S$.

### 3.3 $2^{2g}$ ground states [Proved; checked by ranks over $\mathbb{Z}_2$.]

By (2.3) and (3.5) the ground space has dimension $2^{E-(V-1)-(F-1)}=2^{2-\chi}$, $\chi=V-E+F=2-2g$:
$$
\boxed{\ {\rm GSD}(\Sigma_g)=2^{2g}.\ }\tag{3.6}
$$
This is a second, lattice derivation of the BF count $N^{2g}$ of Sem II Week 2 §4 at $N=2$: there the degeneracy came from the holonomy algebra on $H_1(\Sigma_g,\mathbb{Z}_N)$, here from the Pauli algebra and the Euler characteristic, independently of the cellulation (Kitaev's irregular lattices; [[week-14-fradkin-shenker-order-parameters|Sem I Week 14]] §7 counted $r^{b_1}$ for charge-$q$ matter in the same way). The ranks of the check matrices over $\mathbb{Z}_2$, their Smith normal form over that field, confirm (3.5) on every $L_1\times L_2$ torus with $2\le L_i\le7$, and give $k=4$ on square-tiled surfaces of genus 2 (three squares glued as an L, $(V,E,F)=(1,6,3)$, refined to $(25,54,27)$) and $k=6$ on a six-square surface of genus 3 refined to $(20,48,24)$.

### 3.4 Logical operators [Proved.]

For a path γ of the direct lattice and a path $\tilde\gamma$ of the dual lattice let
$$
W(\gamma)=\prod_{\ell\in\gamma}Z_\ell,\qquad U(\tilde\gamma)=\prod_{\ell\,\pitchfork\,\tilde\gamma}X_\ell,\tag{3.7}
$$
the second over the links that $\tilde\gamma$ crosses (Sem II Week 2 (6.13) at $N=2$). $Z(z)$ commutes with every star exactly when $z$ is a 1-cycle, and the $Z$-type stabilizers are the $Z(\partial\beta)$, so the $Z$-type logical operators form $H_1(\Sigma,\mathbb{Z}_2)$; likewise the $X$-type ones are the closed $U(\tilde C)$ modulo stars, $H^1\cong H_1$. Since $X(x)Z(z)$ commutes with the stars exactly when $Z(z)$ does, and with the plaquettes exactly when $X(x)$ does, the logical group is $H_1\oplus H^1\cong\mathbb{Z}_2^{4g}$, and by (2.1)
$$
W(C)\,U(\tilde C)=(-1)^{I(C,\tilde C)}\,U(\tilde C)\,W(C),\tag{3.8}
$$
with $I(C,\tilde C)$, the number of links of $C$ crossed by $\tilde C$, the mod-2 intersection number. The closed $W(C)$ are Wilson loops; the closed $U(\tilde C)$ are the electric-flux operators $U_i$ of Sem I Week 7 §7.4, the generators of the electric $\mathbb{Z}_2^{(1)}$ of [[higher-form-symmetries]] ([[courses/generalized-symmetries-course/conventions|conventions]] §6). For a symplectic basis $(a_i,b_i)$ of $H_1(\Sigma_g,\mathbb{Z}_2)$, $a_i\cdot b_j=\delta_{ij}$, $a_i\cdot a_j=b_i\cdot b_j=0$, with isotopic dual curves $\tilde a_i,\tilde b_i$, the $2g$ logical qubits are
$$
(\bar Z_{2i-1},\bar X_{2i-1})=\big(W(a_i),\,U(\tilde b_i)\big),\qquad(\bar Z_{2i},\bar X_{2i})=\big(W(b_i),\,U(\tilde a_i)\big),\qquad i=1,\dots,g .\tag{3.9}
$$
On the $L_1\times L_2$ torus, with $C_x$ the row $y=0$, $C_y$ the column $x=0$, $\tilde C_y$ the dual line $x=\tfrac12$ and $\tilde C_x$ the dual line $y=\tfrac12$ (Figure 2),
$$
\boxed{\ \bar Z_1=W(C_x)=\prod_{x=0}^{L_1-1}Z_{h(x,0)},\quad \bar X_1=U(\tilde C_y)=\prod_{y=0}^{L_2-1}X_{h(0,y)},\quad \bar Z_2=W(C_y)=\prod_{y=0}^{L_2-1}Z_{v(0,y)},\quad \bar X_2=U(\tilde C_x)=\prod_{x=0}^{L_1-1}X_{v(x,0)},\ }\tag{3.10}
$$
of weights $L_1,L_2,L_2,L_1$. The pairs $(\bar Z_1,\bar X_1)$ and $(\bar Z_2,\bar X_2)$ share the single links $h(0,0)$ and $v(0,0)$ and anticommute, every other pair shares no link, and all four commute with every stabilizer (checked on the $3\times3$ torus): Kitaev's loops $c_{z1},c_{z2}$ and cuts $c_{x1},c_{x2}$.

![[gs-s2w08-logical-operators.svg|Three columns of the periodic lattice with Z on the row y=0 and on the column x=0, X on the links crossed by the dual lines y=1/2 and x=1/2, and the links h(0,0) and v(0,0) carrying both]]

**Figure 2. The logical operators (3.10), three columns of the periodic lattice. The links marked $ZX$ carry two of them: $h(0,0)$ carries $\bar Z_1$ and $\bar X_1$, $v(0,0)$ carries $\bar Z_2$ and $\bar X_2$.**

### 3.5 The four ground states on the torus [Computed.]

$|{\Uparrow}\rangle$, with every $Z_\ell=+1$, has all $B_p=1$ and $\bar Z_1=\bar Z_2=1$. With $G_A$ the group of the $2^{N-1}$ distinct products of stars, $\prod_v\frac{1+A_v}2=2^{1-N}\sum_{g\in G_A}g$, and distinct $g$ flip distinct sets of links, so
$$
|\Omega_{00}\rangle=2^{-(N-1)/2}\sum_{g\in G_A}g\,|{\Uparrow}\rangle,\qquad |\Omega_{s_1s_2}\rangle=\bar X_1^{s_1}\bar X_2^{s_2}\,|\Omega_{00}\rangle,\qquad \bar Z_i\,|\Omega_{s_1s_2}\rangle=(-1)^{s_i}|\Omega_{s_1s_2}\rangle .\tag{3.11}
$$
In the $Z$ basis, the basis of link variables $Z_\ell=U_\ell$, $|\Omega_{s_1s_2}\rangle$ is the equal-weight superposition of the flat $\mathbb{Z}_2$ connections with holonomies $(-1)^{s_1}$, $(-1)^{s_2}$ around $C_x$, $C_y$, Kitaev's eq. (3); in the electric basis it is the loop gas of Sem I Week 7 §8. On the $3\times3$ torus the four vectors of $2^{18}$ components are orthonormal and fixed by all eighteen stabilizers, and $|\Omega_{00}\rangle$ has 256 amplitudes, all $\frac1{16}$.

## 4. Anyons from string operators

### 4.1 Strings and their endpoints [Proved.]

For an open direct path γ from $v$ to $w$ and an open dual path $\tilde\gamma$ from plaquette $p$ to $q$, (2.1) gives
$$
A_u\,W(\gamma)=(-1)^{[u\in\partial\gamma]}\,W(\gamma)\,A_u,\qquad B_r\,U(\tilde\gamma)=(-1)^{[r\in\partial\tilde\gamma]}\,U(\tilde\gamma)\,B_r,\tag{4.1}
$$
while $W(\gamma)$ commutes with all plaquettes and $U(\tilde\gamma)$ with all stars: an interior vertex of γ touches two of its links, an endpoint one. So $W_e(\gamma)\equiv W(\gamma)$ creates $e$'s at $v$ and $w$ and $W_m(\tilde\gamma)\equiv U(\tilde\gamma)$ creates $m$'s in $p$ and $q$ (Figure 1), Kitaev's $S^z(t)$ and $S^x(t')$. An ε is an $e$ at $v$ with an $m$ in the plaquette $p(v)$ to its north-east, created by $W_\varepsilon=W_eW_m$. For two paths with $\gamma+\gamma'=\partial R$,
$$
W(\gamma')=W(\gamma)\prod_{p\in R}B_p,\tag{4.2}
$$
so they agree on every state with no $m$ in $R$, and dually with stars.

### 4.2 Superselection sectors and fusion [Proved.]

For a disk $R$ of plaquettes with interior vertices $R'$, the exact identities
$$
W(\partial R)=\prod_{p\in R}B_p,\qquad U(\partial\tilde R')=\prod_{v\in R'}A_v\tag{4.3}
$$
show that the boundary loops measure the $m$- and $e$-parities inside; operators on links strictly inside $R$ share no link with them and commute with both. The type $(q_e,q_m)$ of a region, $(+,+)=1$, $(-,+)=e$, $(+,-)=m$, $(-,-)=\varepsilon$, is therefore invariant under local operations inside it, and for disjoint regions the eigenvalues multiply:
$$
{\rm type}(R_1\cup R_2)={\rm type}(R_1)+{\rm type}(R_2)\in\mathbb{Z}_2\times\mathbb{Z}_2,\tag{4.4}
$$
the fusion algebra
$$
e\times e=m\times m=\varepsilon\times\varepsilon=1,\qquad e\times m=\varepsilon,\qquad e\times\varepsilon=m,\qquad m\times\varepsilon=e .\tag{4.5}
$$
Each anyon is its own antiparticle. On the sphere a fixed anyon configuration spans one state, (2.4) at $g=0$, so fusion has one channel, every $d_a=1$ and $\mathcal D^2=4$. Fusion is the product of strings: two $e$'s meeting at a vertex annihilate because $Z_\ell^2=1$.

### 4.3 Braiding [Computed.]

Create an $a$-pair by $W_a(\gamma)$ with one member inside a disk $R$ and the other far away, and carry $b$ around ∂R with $W_b(\partial R)$, a product of stabilizers by (4.3) that fixes the ground state Ω:
$$
W_b(\partial R)\,W_a(\gamma)\,|\Omega\rangle=M_{ba}\,W_a(\gamma)\,W_b(\partial R)\,|\Omega\rangle=M_{ba}\,W_a(\gamma)\,|\Omega\rangle,\tag{4.6}
$$
with $M_{ba}=\pm1$ the commutation sign of the strings. An $e$-loop and an open $m$-string share an odd number of links, since $\tilde\gamma$ starts inside and ends outside; two $e$-strings or two $m$-strings share no $Z$–$X$ pair; the ε-loop $W(\partial R)U(\partial\tilde R')$ collects one sign from each factor. With $a=(a_e,a_m)\in\mathbb{Z}_2^2$,
$$
M_{ab}=(-1)^{a_eb_m+a_mb_e},\qquad M=\begin{pmatrix}1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1\end{pmatrix}\quad\text{in the order }(1,e,m,\varepsilon),\tag{4.7}
$$
the braiding phase of [[courses/generalized-symmetries-course/conventions|conventions]] §9 and Kitaev's anticommutation of $S^x(c)$ with $S^z(t)$: the Aharonov–Bohm phase of a $\mathbb{Z}_2$ charge around a π flux. Checked on the $10\times10$ torus for all nine pairs of nontrivial strings.

### 4.4 Exchange statistics from the T-junction [Computed; the meaning of (4.8) Stated — refs: Levin–Wen 2003.]

Let $t_{ij}$ move a particle from site $j$ to a neighbour $i$. For three neighbours $j,k,l$ of $i$ in clockwise order, Levin and Wen define the statistics by
$$
t_{il}\,t_{ki}\,t_{ij}=e^{i\theta}\,t_{ij}\,t_{ki}\,t_{il} .\tag{4.8}
$$
Read from the right, both sides take particles at $j$ and $l$ to $i$ and $k$ through the same hops, but on the left the particle from $j$ ends at $k$ and on the right the one from $l$ does: the histories differ by one exchange, and Levin and Wen show that the ratio does not depend on the choice of hops (for fermions, $t_{ij}=c_i^\dagger c_j$, it is $-1$). For Pauli-string hops each pair commutes up to a sign λ, and reversing three factors exchanges each pair once:
$$
e^{i\theta}=\lambda(t_{il},t_{ki})\,\lambda(t_{il},t_{ij})\,\lambda(t_{ki},t_{ij}).\tag{4.9}
$$
An $e$ hops by one $Z$ and an $m$ by one $X$, so $\theta_e=\theta_m=1$. For ε at $(v,p(v))$, $v=(x,y)$, the hops east and north are
$$
t_x(v)=Z_{h(x,y)}\,X_{v(x+1,y)},\qquad t_y(v)=Z_{v(x,y)}\,X_{h(x,y+1)},\tag{4.10}
$$
each anticommuting with exactly the two stars and two plaquettes at its ends. At $o=(0,0)$ with $2=o+\hat x$, $3=o+\hat y$, $4=o-\hat x$, so that $(j,k,l)=(4,3,2)$ is clockwise (Figure 3), $t_{12}=t_x(o)$, $t_{31}=t_y(o)$ and $t_{14}=t_x(o-\hat x)$ overlap with $Z$ against $X$ only on $v(0,0)$, so
$$
\theta_\varepsilon=-1 .\tag{4.11}
$$
The script finds the same for the four three-legged junctions at a vertex and for the other pairing ($m$ to the south-west). This is Levin and Wen's §V computation for Kitaev's model.

![[gs-s2w08-t-junction.svg|Two plaquettes around the origin with the Z and X operators of the three hops of the epsilon particle, and the link v(0,0) carrying a Z from one hop and an X from another]]

**Figure 3. The T-junction for ε at $o$: the hops (4.10) toward sites 2 (east), 3 (north) and 4 (west). Only $v(0,0)$ carries a $Z$ from one hop and an $X$ from another, so one pair anticommutes and $\theta_\varepsilon=-1$.**

### 4.5 Spins, monodromies and the Dijkgraaf–Witten labels [Computed.]

With $\theta=(1,1,1,-1)$ and (4.7),
$$
\theta_{a\times b}=\theta_a\,\theta_b\,M_{ab}\tag{4.12}
$$
holds for all sixteen pairs, the monodromy relation of Sem II Week 7 §6.4. In particular $\theta_\varepsilon=\theta_e\theta_mM_{em}$: the spin of ε is the Aharonov–Bohm phase of its charge in its own flux. These are the data of Table 2 of [[sem2-week-07-spt-phases-group-cohomology-dijkgraaf-witten|Sem II Week 7]] at $k=0$, with the gauge field identified as $Z_\ell=(-1)^{a_\ell}$ and $B_p=(-1)^{(da)_p}$: $e=(0,-1)$ is the pure charge, $m=(1,1)$ the pure flux, and $F\equiv1$. The individual $R$-symbols depend on a basis of the fusion spaces, and the lattice computes their basis-independent combinations $M_{ab}$ and $\theta_a$. The double semion, with the same degeneracy, differs exactly here, with spins $(1,1,i,-i)$.

## 5. The modular data from the string algebra

### 5.1 Two bases of the torus [Computed.]

Let $|1\rangle_x$ be the ground state with both loops along $x$ trivial, $W_e(C_x)=\bar Z_1=1$ and $W_m(\tilde C_x)=\bar X_2=1$ (unique: they belong to different qubits), and define
$$
|a\rangle_x=W_a(C_y)\,|1\rangle_x,\qquad W_e(C_y)=\bar Z_2,\quad W_m(\tilde C_y)=\bar X_1,\quad W_\varepsilon(C_y)=\bar Z_2\bar X_1,\tag{5.1}
$$
where $W_\varepsilon(C)=W_e(C)W_m(\tilde C')$ with $\tilde C'$ a dual curve pushed off $C$. Since $C_x$ and $C_y$ cross once, strings along them commute up to the signs (4.7), so
$$
W_b(C_x)\,|a\rangle_x=M_{ba}\,|a\rangle_x :\tag{5.2}
$$
the $x$-loops detect an $a$-line along $C_y$. The second basis exchanges the cycles: $|1\rangle_y$ has $\bar Z_2=\bar X_1=1$ and $|a\rangle_y=W_a(C_x)|1\rangle_y$, with $W_e(C_x)=\bar Z_1$, $W_m(\tilde C_x)=\bar X_2$. In the basis $|s_1s_2\rangle$ of (3.11), with $|\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2$ and ${}_x\langle1|1\rangle_y>0$,
$$
|1\rangle_x=|0{+}\rangle,\ \ |e\rangle_x=|0{-}\rangle,\ \ |m\rangle_x=|1{+}\rangle,\ \ |\varepsilon\rangle_x=|1{-}\rangle;\qquad
|1\rangle_y=|{+}0\rangle,\ \ |e\rangle_y=|{-}0\rangle,\ \ |m\rangle_y=|{+}1\rangle,\ \ |\varepsilon\rangle_y=|{-}1\rangle .\tag{5.3}
$$

### 5.2 The $S$ matrix [Computed.]

The change of basis
$$
S_{ab}={}_x\langle a|b\rangle_y\tag{5.4}
$$
is a product of two single-qubit overlaps, each $\pm\frac1{\sqrt2}$, negative only for $\langle1|{-}\rangle$ and $\langle{-}|1\rangle$; for instance $S_{em}=\langle0|{+}\rangle\langle{-}|1\rangle=-\frac12$. Thus
$$
\boxed{\ S=\frac12\begin{pmatrix}1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1\end{pmatrix}=\frac{M}{\mathcal D},\qquad\mathcal D=2 .\ }\tag{5.5}
$$
Kitaev's App. E describes $S$ in these terms, as the transition between bases attached to Aharonov–Bohm measurements along two circles, and his (223), $S_{ab}=\mathcal D^{-1}\sum_cN^c_{a\bar b}\,d_c\,\theta_c/(\theta_a\theta_b)$, is $\mathcal D^{-1}M_{ab}^*$ for abelian anyons; the data here are real, so conjugation conventions do not enter. The lattice realizes $S$ as a symmetry: the $90^\circ$ rotation about a vertex of the $L\times L$ torus maps stars to stars and plaquettes to plaquettes, commutes with $H_{\rm TC}$ and the uniform fields of §7, and exchanges the classes of $C_x$ and $C_y$. On the $3\times3$ torus, with the qubits permuted explicitly, its matrix in the basis $|a\rangle_x$ is exactly (5.5).

### 5.3 The $T$ matrix [Computed.]

The Dehn twist $\tau_x$ fixes $C_x$ and sends $C_y$ to $C_y+C_x$. No lattice symmetry implements it; its action on the ground space is fixed up to one phase by its action on the loops, which carries the strings along $C_y$ to strings along $C_x+C_y$:
$$
\tau_x:\qquad\bar Z_1\to\bar Z_1,\qquad\bar X_2\to\bar X_2,\qquad\bar Z_2\to\bar Z_1\bar Z_2,\qquad\bar X_1\to\bar X_1\bar X_2 .\tag{5.6}
$$
The images obey the original commutation relations, so (5.6) is a unitary up to a phase, the logical CNOT controlled by the first qubit. It fixes $|1\rangle_x$ up to a phase, which we set to 1. Then $T|a\rangle_x=W_a(C_x+C_y)|1\rangle_x$, and with $\bar Z_1|1\rangle_x=\bar X_2|1\rangle_x=|1\rangle_x$,
$$
\begin{aligned}
T|e\rangle_x&=\bar Z_1\bar Z_2|1\rangle_x=|e\rangle_x,\qquad
T|m\rangle_x=\bar X_1\bar X_2|1\rangle_x=|m\rangle_x,\\
T|\varepsilon\rangle_x&=\bar Z_1\bar Z_2\bar X_1\bar X_2|1\rangle_x=\bar Z_2\,(\bar Z_1\bar X_1)\,|1\rangle_x=-\bar Z_2\bar X_1\bar Z_1|1\rangle_x=-|\varepsilon\rangle_x .
\end{aligned}\tag{5.7}
$$
So $T={\rm diag}(1,1,1,-1)={\rm diag}(\theta_a)$. The sign is the single crossing of the $e$-part of the twisted string with its $m$-part; as an identity on the ground space,
$$
W_\varepsilon(C_x)\,W_\varepsilon(C_y)=W_\varepsilon(C_y)\,W_\varepsilon(C_x)=-\,W_\varepsilon(C_x+C_y),\tag{5.8}
$$
while $e$- and $m$-loops multiply with a plus sign. On the $3\times3$ torus we checked (5.8) with the staircase loop through $(0,0),(1,0),(1,1),(2,1),(2,2),(0,2)$ and its pushed-off dual staircase, and the matrix of (5.6) computed from the explicit ground states is ${\rm diag}(1,1,1,-1)$. The local value (4.11) and the global one agree, as they must for a property of the anyon.

### 5.4 The modular relations [Computed; the general statements Stated — refs: Kitaev 2006, App. E.]

With $C_{ab}=\delta_{a\bar b}=\delta_{ab}$,
$$
S=S^{T},\qquad SS^\dagger=1,\qquad S^2=C,\qquad (ST)^3=\Theta\,C,\qquad \Theta=\frac1{\mathcal D}\sum_ad_a^2\theta_a=\frac{1+1+1-1}2=1,\tag{5.9}
$$
Kitaev's (232)–(233); by his (172), $\Theta=e^{2\pi ic_-/8}$, so $c_-\equiv0$ mod 8, as for any Hamiltonian real in the $Z$ basis, whose complex conjugation reverses the chirality. The Verlinde formula, his (228),
$$
N_{ab}^c=\sum_x\frac{S_{ax}S_{bx}S_{\bar cx}}{S_{1x}}=\frac14\sum_xM_{ax}M_{bx}M_{cx}=\delta_{c,a\times b},\tag{5.10}
$$
returns (4.5), the rows of $M$ being the characters of $\mathbb{Z}_2\times\mathbb{Z}_2$. All of (5.9)–(5.10) were checked numerically. [[sem2-week-10-beyond-z2-quantum-doubles-modular-data-chern-simons|Sem II Week 10]] §5.2 recovers θ and (4.7) from $K=\begin{pmatrix}0&2\\2&0\end{pmatrix}$ with the course signs of [[courses/generalized-symmetries-course/conventions|conventions]] §10: with $e=(1,0)$ and $m=(0,-1)$, $\theta_l=e^{-i\pi l^TK^{-1}l}$ and $B(l,l')=e^{-2\pi il^TK^{-1}l'}$ give $\theta=(1,1,1,-1)$ and $B(e,m)=M_{em}=-1$, and $|\det K|=4$ is (3.6) at $g=1$.

## 6. The gauge-theory dictionary, completed [Proved.]

Sem I Week 7 §8 identified $H_{\rm TC}$ with the Γ → 0 point of the Kogut–Susskind Hamiltonian with the Gauss law as an energy, and Sem I Week 13 §9 the toric code in fields with the gauge–Higgs model in unitary gauge. Table 1 completes the dictionary.

| lattice operator | toric code | $\mathbb{Z}_2$ gauge theory ([[courses/generalized-symmetries-course/conventions|conventions]] §4) |
|---|---|---|
| $X_\ell$ | creates or moves $m$ across ℓ | electric field $(-1)^{E_\ell}$ |
| $Z_\ell$ | creates or moves $e$ along ℓ | link variable $U_\ell$ |
| $A_v=-1$ | an $e$ at $v$ | Gauss operator $(-1)^{q_v}$: a charge |
| $B_p=-1$ | an $m$ in $p$ | a unit of flux: the vison of Sem I Week 7 §7.3 |
| open $W(\gamma)$, $U(\tilde\gamma)$ | $e$- and $m$-strings | open Wilson line; vison string $\mu^z_P\mu^z_{P'}$ |
| closed $W(C)$ | $\bar Z_i$ | Wilson loop: charged under the electric $\mathbb{Z}_2^{(1)}$, generator of the magnetic one |
| closed $U(\tilde C)$ | $\bar X_i$ | electric-flux operator $U_i$: generator of the electric $\mathbb{Z}_2^{(1)}$ |

**Table 1. Each operator of §§3–4 with its gauge-theory name.**

*The charged sectors are anyons.* The static-charge sectors of the Kogut–Susskind theory are the $e$-excitations of $H_{\rm TC}$, at energy $2|Q|$ for charges at $Q$, each $2^{2g}$-fold degenerate. On the $N$-site torus the physical space $A_v=1$ of Sem I Week 7 §7.4, of dimension $2^{N+1}$, is the sum over the $2^{N-1}$ allowed vison configurations of four-dimensional spaces, and its four electric-flux sectors are the eigenspaces of $\bar X_1,\bar X_2$. The matter that gauging adds (Sem II Week 7 §6.5) is removed by the unitary gauge of Sem I Week 13 §9, $A_v=\tau^x_v$, and restored by Kitaev's construction in §8.

*The two 1-form symmetries.* At Γ = J = 0 the $U(\tilde C)$ and $W(C)$ commute with $H_{\rm TC}$, and the ground space is the broken phase of both $\mathbb{Z}_2^{(1)}$, with clustering states $|\Omega_{s_1s_2}\rangle$ (Sem II Week 2 §§7, 9.5–9.6; Sem II Week 3 §2). The fields of §7 break them explicitly: $Z_\ell$, the hopping of dynamical charges, anticommutes with the $U(\tilde C)$ that cross ℓ, and $X_\ell$, the hopping of dynamical visons, with the Wilson loops through ℓ ([[courses/generalized-symmetries-course/conventions|conventions]] §6). In the deconfined phase both return as emergent symmetries, which is Kitaev's materialized symmetry (§8).

## 7. The perturbed toric code: two condensations

### 7.1 The fields move the anyons [Controlled to first order in $J/h$ and $\Gamma/K$; the critical values Stated — refs.]

With [[courses/generalized-symmetries-course/conventions|conventions]] §4 the toric code in two fields is
$$
H(h,K,\Gamma,J)=-h\sum_vA_v-K\sum_pB_p-\Gamma\sum_\ell X_\ell-J\sum_\ell Z_\ell ,\tag{7.1}
$$
the gauge–Higgs Hamiltonian of Sem I Week 13 §9 in unitary gauge, with e–m duality $(h,K,\Gamma,J)\to(K,h,J,\Gamma)$. By (4.1), $Z_\ell$ creates, moves or annihilates $e$'s at the ends of ℓ, and $X_\ell$ does the same for $m$ in the plaquettes sharing ℓ: $J$ is the kinetic energy of $e$, Γ that of $m$. For one $e$ far from its partner, $\langle w|H|v\rangle=-J$ between the states with the $e$ at the two ends of a link, and first-order degenerate perturbation theory gives
$$
E_e(\mathbf k)=2h-2J(\cos k_x+\cos k_y)+O(J^2/h),\qquad E_m(\mathbf k)=2K-2\Gamma(\cos k_x+\cos k_y)+O(\Gamma^2/K).\tag{7.2}
$$
The $e$ band reaches zero at $J=h/2$ to this order; the transition at Γ = 0 lies at
$$
J_c=\frac{h}{3.044}=0.3285\,h ,\tag{7.3}
$$
lower because the same $Z_\ell$ create pairs from the vacuum and dress particle and ground state; the number is the critical point of the transverse-field Ising model of §7.3 [Stated — refs: Blöte–Deng, *Phys. Rev. E* 66 (2002) 066110]. By duality $\Gamma_c=0.3285\,K$ at $J=0$.

### 7.2 Stability of the degeneracy [the lemma Proved; the size of the splitting Sketched; checked numerically.]

Kitaev's estimate rests on a lemma: *a Pauli string $O$ whose support contains no noncontractible cycle of either lattice has $\Pi O\Pi\in\{0,\pm\Pi\}$.* If $O$ anticommutes with a stabilizer $s$, $\Pi O\Pi=\Pi Os\Pi=-\Pi sO\Pi=0$. Otherwise $O\propto X(x)Z(z)$ with $z$ a cycle and $x$ crossed by a closed dual curve (§3.4), all their loops contractible, so both are boundaries and $O$ is ± a stabilizer. For a perturbation $V$ by single-qubit Pauli terms, such as the fields of (7.1), the order-$m$ effective Hamiltonian is a sum of terms $\Pi V\mathcal RV\cdots\mathcal RV\Pi$, with $\mathcal R=Q/(E_0-H_{\rm TC})$ a combination of projectors $\Pi_\sigma$ onto stabilizer eigenspaces; since $\Pi_\sigma P=P\Pi_{\sigma'}$ for a Pauli string $P$, each term is a number times $\Pi P_1\cdots P_m\Pi$, a multiple of Π for $m<\min(L_1,L_2)$ by the lemma. The first splitting comes at order $\min(L_1,L_2)$, from straight noncontractible strings; on the $L\times L$ torus
$$
H_{\rm eff}=E_0(\Gamma,J)-b_1\bar X_1-b_2\bar X_2-b'_1\bar Z_1-b'_2\bar Z_2+\dots,\qquad b_i=O(\Gamma^L),\qquad b'_i=O(J^L).\tag{7.4}
$$
Kitaev reads the coefficients as amplitudes for a virtual anyon to tunnel around the torus, $b\sim e^{-aL}$, and finds that two-spin terms split the degeneracy no earlier than order $\lceil L/2\rceil$; we do not control higher orders, so $e^{-L/\xi}$ throughout the phase is Sketched. At $J=0$ the $\bar X_i$ are conserved; diagonalizing $H(1,1,\Gamma,0)$ in each sector in the electric basis ($2^{F-1}$ states) for Γ from 0.02 to 0.08, the splittings scale as $\Gamma^{3.03}$ on the $3\times3$ torus and $\Gamma^{4.05}$ on the $4\times4$ torus, with the sectors $\bar X_i=-1$ higher.

### 7.3 $e$ condensation is the Higgs transition [Proved through the exact map; the universality Stated — refs.]

At Γ = 0 the plaquettes are conserved and the ground state is flux-free. There the bond-algebra map $Z_\ell\leftrightarrow\mu^z_v\mu^z_w$ for $\ell=\langle vw\rangle$ and $A_v\leftrightarrow\mu^x_v$ takes (7.1) to the transverse-field Ising model of the matter, $-h\sum\mu^x-J\sum\mu^z\mu^z$, in its sector $\prod_v\mu^x_v=1$ and with the boundary conditions of (c) below (Sem I Week 13 §9; F6). A product of bonds along a path is an open Wilson string, so the Ising order parameter is
$$
\langle W(\gamma_{vw})\rangle\ \longrightarrow\ {\rm const}\neq0\qquad(|v-w|\to\infty,\ J>J_c),\tag{7.5}
$$
the amplitude to create a distant $e$-pair; it decays exponentially in the toric-code phase and vanishes at $J=0$. Long-range order of the operator that creates $e$ is what *$e$ condenses* means, and the transition is the three-dimensional Ising transition at (7.3). Three consequences follow. (a) The $e$-parity of a region is no longer conserved and $e$ is absorbed by the condensate, $e\sim1$: Kitaev's Bose condensate of charged particles. (b) $m$ is confined: at $h\to0$ the ground state is $|{\Uparrow}\rangle$, and an $m$-pair at separation $R$ flips $R$ bonds, at energy $4K+2JR$, string tension $2J$; throughout the ordered phase the $m$-string is a line of reversed bonds $Z_\ell$, a domain wall of the Ising order, since by (4.7) the condensate amplitude changes sign across it [Heuristic away from $h=0$]. (c) The degeneracy is lifted: in the conserved sector $\bar Z_1=-1$ the product of the bonds around $C_x$ is $-1$, so the spins are antiperiodic along $x$, which costs the ordered phase a domain wall of length $L_2$ and the paramagnet only $O(J^{L_1})$ by (7.4); the sectors $\bar Z_i=\pm1$ are the four boundary conditions of the Ising model [the identification Proved; the energies Heuristic].

### 7.4 $m$ condensation is the confinement transition [Proved through the exact map; Stated — refs: Trebst et al. 2007.]

At $J=0$ the stars are conserved and the ground state is charge-free, where $H$ is the pure gauge theory of Sem I Week 7 §7.1 and the bond-algebra map $X_\ell\leftrightarrow\mu^z_P\mu^z_{P'}$, $B_P\leftrightarrow\mu^x_P$ of Week 7 §7.3 gives the dual transverse-field Ising model $-\Gamma\sum\mu^z\mu^z-K\sum\mu^x$ in its sector $\prod_P\mu^x_P=1$. For $\Gamma>\Gamma_c$ the vison string has long-range order,
$$
\langle U(\tilde\gamma_{PP'})\rangle\ \longrightarrow\ {\rm const}\neq0\qquad(|P-P'|\to\infty) :\tag{7.6}
$$
$m$ condenses. Dually, $e$ is confined with tension $2\Gamma$ at $K=0$, the strong-coupling tension of Sem I Week 7 §7.1 (Problem 3 adds the first correction), and the flux sectors $\bar X_i=\pm1$ split in proportion to $L$. Trebst et al. treat this problem as a loop gas whose closed electric loops (§3.5) acquire a tension from the field: the order survives small tension, and at large tension a continuous transition condenses the magnetic vortices and confines the charges [Stated — refs: Trebst et al. 2007].

### 7.5 The condensation rules [Stated — refs: Bais–Slingerland 2009; the toric-code cases Proved in §§7.3–7.4.]

In a theory of anyons a boson $a$, $\theta_a=1$, can condense; then $a$ is identified with the vacuum and $b$ with $b\times a$, anyons with $M_{ab}\neq1$ are confined, and the surviving classes form the anyons of the new phase [Stated — refs: Bais–Slingerland 2009]. In the toric code ε is a fermion, (4.11), and the fusion-closed sets of bosons with a nontrivial anyon are $\{1,e\}$ and $\{1,m\}$. Condensing $e$ confines $m$ and ε, which braid with $e$ by $-1$, and identifies $e$ with 1; condensing $m$ confines $e$ and ε. Both leave only the vacuum, with a unique ground state on the torus, as §7.3(c) found: the only two condensations end in the trivial phase.

### 7.6 Both fields: the Fradkin–Shenker diagram as a condensation diagram [Stated — refs: Tupitsyn et al. 2010; Sem I Week 13; the anyon reading Heuristic where marked.]

With both fields no string operator is conserved, and the diagram at $h=K=1$ (Figure 4) is the one of Sem I Week 13 §7, translated into (7.1) in its §9. The toric-code phase is bounded by the $m$-condensation (confinement) line from $(\Gamma_c,0)$ and the $e$-condensation (Higgs) line from $(0,J_c)$, which the duality exchanges. Tupitsyn et al. found by Monte Carlo on the three-dimensional gauge–Higgs model, up to $60^3$, that the two lines stay second order until they merge into a first-order line, and predict the same structure for the toric code in two fields, which they map onto an anisotropic gauge–Higgs model [Stated — refs: Tupitsyn et al. 2010]. M lies on the self-dual line Γ = J, the first-order segment follows it to an endpoint E, and beyond E the two regimes are one phase (Sem I Week 13 §§6–7).

This week adds the reading. The confinement line closes the $m$ gap with $e$ gapped, the Higgs line the $e$ gap with $m$ gapped, and both condensates end in the trivial theory of §7.5: complementarity in anyon language, since past either line no superselection sector survives to tell the regimes apart [exact on the edges Γ = 0 and $J=0$; Heuristic inside]. What distinguishes them is the transition that leads to each and the interface each forms with the toric code, which absorbs $e$'s in one case and $m$'s in the other: two boundaries of the toric code, met again in the planar code of Week 9 [Heuristic]. At M the two bosons becoming gapless are mutual semions, (4.7), so no description by two commuting local order parameters applies, the difficulty Tupitsyn et al. single out; the transition at M appears continuous [Stated — refs: Somoza, Serna, Nahum 2021; Sem I Week 13 §7.1].

![[gs-s2w08-phase-diagram.svg|Schematic phase diagram in the plane of the two fields: the toric-code region bounded by the e- and m-condensation lines, which meet at M on the self-dual line, and a first-order segment from M to E]]

**Figure 4. The toric code in two fields at $h=K=1$: the toric-code phase is bounded by the $m$- and $e$-condensation lines from $\Gamma_c=J_c\approx0.3285$, mirror images under the duality, which meet at M on the self-dual line; the first-order segment M–E follows it. Shapes and the positions of M and E are schematic.**

> **Physical picture.** A simulation that measures the two open strings sees the regimes of Figure 4: in the toric-code phase both $\langle W(\gamma_{vw})\rangle$ and $\langle U(\tilde\gamma_{PP'})\rangle$ decay exponentially, past the Higgs line the first saturates, past the confinement line the second, whose saturated value Problem 6⋆ computes. This is exact at the edges, where the Ising maps of §§7.3–7.4 hold; electric loops that proliferate at small tension and shrink at large tension are the heuristic loop-gas reading. For the research line, the confinement line is the simplest confinement by condensation of a magnetic defect, the $\mathbb{Z}_2$ form of the [[julia-toulouse-mechanism]], to which Sem II Weeks 14–15 return (forward reference).

## 8. Seminar: Kitaev (1997), materialized symmetry, presented by the instructor

**Format.** The first seminar of Block 3, presented by the instructor as the model, in the format of syllabus §7. Students read §§1–3 of the arXiv text and bring Problem 4.

**Sections.** §3 of the arXiv text, "Materialized symmetry: is that a miracle?", in full, with the stability estimate closing §1 and the tunnelling paragraph of §2. Sem II Week 2 §8 presented the first two sections and the opening of this one.

**The technical claim.** The perturbed toric code has no exact gauge symmetry, yet electric and magnetic charges are conserved mod 2 at long distances. Adding spins on vertices and faces and changing variables by a unitary $U$ writes any Hamiltonian in gauge-invariant form, Kitaev's (6)–(8), and this artificial symmetry becomes a conservation law when it is not broken; when the Higgs field condenses, charges condense and vortices are confined, and dually.

**What it needs from Semester I.** Unitary gauge with matter and Elitzur's theorem (Sem I Week 13 §§2, 9, F3), the dual Ising variables (Week 7 §7.3); from this note, §7.

**The step at the board.** Kitaev's (6)–(7), in ten minutes. With spins $v_s$ on vertices, $w_p$ on faces and edge labels $z_j$, the map $z_j\to z_j+\sum_{s\in\partial j}v_s$, $w_p\to w_p+\sum_{j\in\partial p}z_j$ is an involution $U$, since $\sum_{j\in\partial p}\sum_{s\in\partial j}v_s=0$ mod 2. Conjugated by $U$, $\sigma^x_s$ also flips $z_j$ on the edges at $s$, so $P_s=U\sigma^x_sU^\dagger=\sigma^x_sA_s$, and $\sigma^z_p=(-1)^{w_p}$ acquires $\sum_{j\in\partial p}z_j$ in the exponent, so $Q_p=\sigma^z_pB_p$. On $P_s=Q_p=1$ the stars and plaquettes equal $\sigma^x_s$ and $\sigma^z_p$, and $H_0\equiv-\sum_s\sigma^x_s-\sum_p\sigma^z_p$, his (8). $P_s=1$ is the Gauss law with matter of Sem I Week 13 §9 with $\sigma^x_s\leftrightarrow\tau^x_v$: the construction is the unitary gauge run backwards. Then, in fifteen minutes, the mini-step of the week: the count (3.4)–(3.6) and $S$, $T$ from the loop operators, (5.3)–(5.7).

**For the discussion.** Kitaev's criterion for the broken gauge symmetry, a nonzero $\langle\sigma^z_s\rangle$, depends on the gauge by Elitzur's theorem and Week 13 F3; its invariant form is the long-range order (7.5). He closes by asking whether vortices can be confined with the gauge symmetry unbroken and answers that apparently they cannot; within boson condensation §7.5 gives the reason, since only an anyon that braids with $m$ confines it, and of $e$ and ε only $e$ is a boson.

**The open question it leaves for this course.** Transitions out of the toric code that no single boson condensation describes: the point M (Problem 8⋆⋆), and perturbations that move ε, the anyon that cannot condense.

**On the course map.** The materialized symmetry is the pair of emergent 1-form symmetries of §6, and the charges conserved mod 2 are the sectors (4.3).

## 9. Subtleties and fine print

**F1. The choice of pairing.** A loop pairs with the cut that crosses it once, so the $m$-string $U(\tilde C_x)$ along $C_x$ pairs with $W(C_y)$. On $\Sigma_g$ a change of symplectic basis in (3.9) acts on the logical qubits by a Clifford unitary, of which (5.6) and the rotation of §5.2 are the $g=1$ cases.

**F2. Logical operators live on the ground space.** Homologous loops agree only on states with no anyons between them, (4.2), and their ratio is otherwise the braiding (4.6). The operators (3.10) are representatives modulo stabilizers; the minimal weight in a class is the code distance of Week 9.

**F3. Framing and the phase of $T$.** $W_\varepsilon(C)$ needs a pushed-off dual curve, and (5.8) records how the push-offs of $C_x$ and $C_y$ cross: the ε-loops represent $H_1(T^2,\mathbb{Z}_2)$ up to $(-1)^{C\cdot C'}$, a quadratic refinement of the intersection form with value θ_ε. The string algebra fixes $\theta_a/\theta_1$; Kitaev's App. E identifies the Dehn twist with $e^{-2\pi ic_-/24}T$, and here $c_-=0$.

**F4. The sign of the charge.** In $\mathbb{Z}_2$, $q\equiv-q$ and the Kogut–Susskind sign of [[courses/generalized-symmetries-course/conventions|conventions]] §4 is invisible. In a $\mathbb{Z}_N$ toric code with the clock and shift of [[courses/generalized-symmetries-course/conventions|conventions]] §4, $Z_\ell=U_\ell$ and $[E_\ell,U_\ell]=U_\ell$ give $X_\ell=\omega^{-E_\ell}$, so $G_x=\prod_iX_{(x-\hat i,i)}X^\dagger_{(x,i)}=\omega^{q_x}$ by the Gauss law of §4. From $X^{-1}ZX=\omega Z$, a link leaving $x$ has $G_xZ_\ell G_x^{-1}=\omega Z_\ell$ and a link entering $y$ has $G_yZ_\ell G_y^{-1}=\omega^{-1}Z_\ell$: the string $\prod_{\ell\in\gamma}Z_\ell$ from $x$ to $y$ creates Kogut–Susskind charges $q_x=+1$, $q_y=-1$, physical charges $-1$ and $+1$ [Proved].

**F5. Exact and asymptotic degeneracy.** The four states are exactly degenerate only at Γ = J = 0; in the phase the splitting starts at order $L$ (§7.2). Topological order belongs to the phase, through its gapped anyons and asymptotic degeneracy (Sem II Week 3); Week 9 adds entanglement.

**F6. Ising transitions in a sector.** The local operators of the toric code are the $\mathbb{Z}_2$-even operators of the two Ising models of §§7.3–7.4, since $\mu^z$ carries a string, so the transitions have the Ising exponents of the even observables while the Ising order parameter has no local counterpart. On the torus the flux-free spectrum at Γ = 0 is the even sector under all four boundary conditions of §7.3(c), against the even and odd sectors of one for the periodic Ising model [Proved for the operator map].

**F7. Other surfaces.** (3.6) holds as $2^{2-\chi}=2^{\dim H_1(\Sigma,\mathbb{Z}_2)}$ on every closed surface, orientable or not (Problem 1); with boundaries the boundary conditions enter, as in the planar code of Week 9.

## 10. Common misconceptions

- **"Spins multiply, $\theta_\varepsilon=\theta_e\theta_m=1$, so ε is a boson."** It is tempting because the spin of a composite of distant particles is the product of spins. The constituents of ε also braid, and (4.12) gives $\theta_\varepsilon=\theta_e\theta_mM_{em}=-1$, as the T-junction (4.11) confirms.
- **"The Higgs and confined phases are different phases, distinguished by which anyon has condensed."** It is tempting because the two edges of Figure 4 are exact $e$- and $m$-condensates. The regimes are one phase (Sem I Week 13 §6), both condensates are the trivial theory (§7.5), and what differs is the transition and the interface with the toric code [Heuristic, as in §7.6].
- **"The degeneracy needs the Gauss law imposed exactly."** It is tempting because Sem I Week 7 §7.4 found the four flux sectors with the Gauss law as a constraint. $H_{\rm TC}$ imposes it only as an energy, and the degeneracy survives every small local perturbation, split first at order $L$ (§7.2), which is Kitaev's point.

## 11. Historical note

Kitaev posted his paper in July 1997; it appeared in 2003 (*Ann. Phys.* 303, 2). Its language is that of quantum codes: the code TOR(k) on a $k\times k$ torus, stabilizers on vertices and faces, a protected subspace described by the operators commuting with them modulo an ideal, and a Hamiltonian that penalizes violated stabilizers. The anyons appear as endpoints of string operators, the degeneracy is rederived from their braiding by an argument Kitaev attributes to Einarsson, and the gauge-theory reading comes only in the third section, which wonders whether the emergent symmetry is a miracle; the non-abelian models of the rest of the paper belong to Week 10. The gauge theory was older: Wegner (1971), the Hamiltonian forms of Kogut–Susskind (1975) and Fradkin–Susskind (1978), the diagram of Fradkin and Shenker (1979), and Wen's naming of topological order (1990). Levin and Wen (2003) gave the hopping definition of statistics of §4.4, and Trebst et al. (2007) and Tupitsyn et al. (2010) studied the perturbed code numerically.

## 12. What to take away

1. **Technical:** $\dim V_{\mathcal S}=2^n/|\mathcal S|$, and stars and plaquettes satisfy exactly two relations, so ${\rm GSD}=2^{2g}$. **Physical:** the degeneracy counts independent noncontractible loops; the lattice drops out.
2. **Technical:** the logical operators are Wilson loops and electric cuts paired by the intersection form, (3.9)–(3.10). **Physical:** they are the order parameters and generators of the two broken 1-form symmetries.
3. **Technical:** fusion $\mathbb{Z}_2\times\mathbb{Z}_2$, $M_{ab}=(-1)^{a_eb_m+a_mb_e}$ and $\theta=(1,1,1,-1)$ follow from commuting Pauli strings. **Physical:** ε is a fermion because its charge sees its own flux.
4. **Technical:** $S=M/2$ relates the anyon bases of the two cycles and is the lattice rotation; $T={\rm diag}(\theta)$ is the Dehn twist; $(ST)^3=C$. **Physical:** the modular data are Aharonov–Bohm measurements on the torus, and Θ = 1 says the code is non-chiral.
5. **Technical:** $J$ moves $e$ and Γ moves $m$; each field condenses its boson through a three-dimensional Ising transition and confines the other anyon. **Physical:** the Fradkin–Shenker diagram is the diagram of two condensations of mutual semions, which end in one trivial phase.

## 13. Looking ahead: Sem II Weeks 9–11

Sem II Week 9 (Block 3) turns (3.10) into a code: the minimal weight $\min(L_1,L_2)$ is the distance, the lemma of §7.2 says no shorter operator acts on the ground space, and the loop-gas form (3.11) gives the disk Schmidt decomposition behind $\gamma=\ln2=\ln\mathcal D$. Week 11 reads the electric loop gas of §3.5 as the simplest string net.

## 14. Problem set

Problems 1–4 are the classroom core (Problem 4 is brought to the seminar); 5⋆–7⋆ consolidate the self-study sections; 8⋆⋆–9⋆⋆ are research extensions.

### Core problems

**1. Nonorientable surfaces** (extends §§3.2–3.4). (a) Show that the relations (3.4), and no others, hold on every closed connected surface with any cellulation, orientable or not, and conclude ${\rm GSD}=2^{2-\chi}$. (b) Evaluate it for the projective plane and the Klein bottle, and compare with $\dim H_1(\Sigma,\mathbb{Z}_2)$. (c) Realize $\mathbb{RP}^2$ as the $L\times L$ square, $L$ even, with $(0,y)\sim(L,L-y)$ and $(x,0)\sim(L-x,L)$. Exhibit a $Z$-type logical operator along the midline $y=L/2$ and an $X$-type logical operator anticommuting with it, and explain why one curve suffices.

**2. The second Dehn twist** (extends §§5.2–5.4). (a) Write the action of the twist $\tau_y$, which sends $C_x$ to $C_x+C_y$, on the operators (3.10). (b) With $\tau_y|1\rangle_y=|1\rangle_y$, compute its matrix $T_y$ in the basis $|a\rangle_x$. (c) Show $T_y=STS^{-1}$ and explain it with the rotation of §5.2. (d) Verify the braid relation $T\,T_y\,T=T_y\,T\,T_y$.

**3. The string tension of the confined anyon** (extends §7.4 and Sem I Week 7 §7.1). At $J=0$ and $K\ll\Gamma$, place static $e$'s at vertices $v$, $w$ of one row, a distance $d$ apart, on a large torus. (a) At $K=0$, find the energy of the lowest state with $A_v=A_w=-1$ relative to the ground state, and its degeneracy. (b) Compute the correction of order $K^2$ and read off the string tension. (c) Use the duality to state the result for two $m$'s at Γ = 0, $h\ll J$.

**4. The anisotropic torus** (extends §7.2). On the $L_1\times L_2$ torus, $L_1<L_2$, set $J=0$ and $h=K=1$. (a) Show that the eigenvalues of $\bar X_1$, $\bar X_2$ are conserved for every Γ. (b) Find the lowest order in Γ at which sectors differing in $\bar X_2$ have different ground energies, and the same for $\bar X_1$. (c) Write the effective Hamiltonian at those orders and say which sector is lowest for Γ > 0.

### Starred problems

**5⋆. The e–m duality on the torus** (extends §5.4 and Sem I Week 13 Problem 5⋆). (a) Send each link to the dual link crossing it, translate the dual lattice by $(-\tfrac12,-\tfrac12)$ onto the direct one, so $h(x,y)\to v(x,y-1)$ and $v(x,y)\to h(x-1,y)$, and conjugate every qubit by the Hadamard gate; show that $A_{(x,y)}\to B_{p(x-1,y-1)}$, $B_{p(x,y)}\to A_{(x,y)}$ and $H(h,K,\Gamma,J)\to H(K,h,J,\Gamma)$ on the $L\times L$ torus. (b) Find the action on (3.10) and on $|a\rangle_x$. (c) Show that the permutations of $\{1,e,m,\varepsilon\}$ preserving $S$ and $T$ are the identity and $e\leftrightarrow m$. *Hint:* in (b) replace the image strings by homologous representatives; in (c), $T$ fixes ε.

**6⋆. The $m$ condensate at strong field** (extends §7.4). At $J=0$, $h>0$, $K\ll\Gamma$: (a) find the ground state to first order in $K$ from $|{\Rightarrow}\rangle$, all $X_\ell=+1$; (b) show $\langle U(\tilde\gamma_{PP'})\rangle=1-K^2/(16\Gamma^2)+O(K^4/\Gamma^4)$ for every open dual path from $P$ to $P'\neq P$, whatever its length; (c) show $\langle W(\gamma_{vw})\rangle=0$ to all orders, and say which anyon has condensed. *Hint:* $B_p|{\Rightarrow}\rangle$ costs $8\Gamma$, and $U(\tilde\gamma)$ is diagonal in the electric basis and equals $-1$ on $B_p|{\Rightarrow}\rangle$ only for $p\in\{P,P'\}$.

**7⋆. The toric code at finite temperature** (extends §3.1 and Sem II Week 3 §4). (a) From (3.2), show that the Gibbs state on the $N$-site torus has $\langle W(\partial R)\rangle_\beta=(t^{|R|}+t^{N-|R|})/(1+t^N)$, $t=\tanh\beta$, for a contractible loop around $|R|$ plaquettes. (b) Conclude an area law at every $T>0$ as $N\to\infty$, and name the excitations responsible. (c) Compare with the bound of [[courses/generalized-symmetries-course/conventions|conventions]] §6 for discrete $q$-form symmetries, $q\ge d-1$. *Hint:* the $b_p$ are independent except for $\prod_pb_p=1$, imposed by $(1+\prod_pb_p)/2$.

### ⋆⋆ problems

**8⋆⋆. The multicritical point.** *Known:* Figure 4; the Monte Carlo diagram of the 3d gauge–Higgs model and the map of the toric code in two fields onto an anisotropic one (Tupitsyn et al.); the continuity of the self-dual transition (Somoza, Serna, Nahum). *Explored:* how the condensation lines meet at M, where two mutual semions become gapless together. *Completion:* the transfer-matrix derivation of the anisotropic couplings that correspond to (7.1), the matter version of Sem I Week 7 §7.1, and an exact diagonalization of $H(1,1,\Gamma,\Gamma)$ on the $3\times3$ and $4\times4$ tori locating the closing of the $e$ and $m$ gaps, compared with the published M and E. *Sources:* Tupitsyn et al. 2010; Somoza, Serna, Nahum 2021; Sem I Week 13 §7; Blöte–Deng 2002 for the single-field endpoints.

**9⋆⋆. The Fredenhagen–Marcu ratio as a condensation diagnostic.** *Known:* the Fredenhagen–Marcu order parameter separates the free-charge phase from the Higgs–confinement phase (Sem I Week 13 F5); (7.5) and (7.6) are the order parameters on the edges of Figure 4. *Explored:* an equal-time ratio for (7.1), the open string of length $R$ over the square root of the $R\times R$ Wilson loop, as one diagnostic that vanishes in the toric-code phase and stays finite past both lines. *Completion:* leading-order evaluations in each regime and on the first-order segment, with a check on the $4\times4$ torus. *Sources:* Fredenhagen, Marcu, *Commun. Math. Phys.* 92 (1983) 81 and *Phys. Rev. Lett.* 56 (1986) 223; Sem I Week 13 F5; Tupitsyn et al. 2010.

## Self-study answer checkpoints

**Problem 1.** *Decisive step:* with $\mathbb{Z}_2$ coefficients the sum of all faces is a 2-cycle on every closed surface, each edge bordering two faces or one face twice, so $\prod_pB_p=1$ survives where $H_2(\Sigma,\mathbb{Z})=0$ but $H_2(\Sigma,\mathbb{Z}_2)=\mathbb{Z}_2$. *Result:* ${\rm GSD}=2^{2-\chi}=2^{\dim H_1(\Sigma,\mathbb{Z}_2)}$: 2 on $\mathbb{RP}^2$, 4 on the Klein bottle. On $\mathbb{RP}^2$, $W$ on the midline (weight $L$) anticommutes with $U$ along the dual curve at height $L/2+\frac12$ to $x=j+\frac12$, down through $h(j,L/2)$, on at height $L/2-\frac12$ to the right edge, and back in at height $L/2+\frac12$ through the twisted gluing (weight $L+1$): the generator meets its own push-off once, $a\cdot a=1$. Checked for $L=4$ ($k=1$; the $4\times4$ and $3\times5$ Klein bottles give $k=2$). *Common failure:* dropping the plaquette relation, which gives $2^{1-\chi}$.

**Problem 2.** *Decisive step:* $\tau_y$ fixes $\bar Z_2$, $\bar X_1$ and sends $\bar Z_1\to\bar Z_1\bar Z_2$, $\bar X_2\to\bar X_2\bar X_1$, the logical CNOT controlled by the second qubit, which fixes $|1\rangle_y=|{+}0\rangle$. *Result:* in the order $(1,e,m,\varepsilon)$,
$$
T_y=\frac12\begin{pmatrix}1&1&1&-1\\1&1&-1&1\\1&-1&1&1\\-1&1&1&1\end{pmatrix}=STS^{-1},
$$
because the rotation, whose matrix is $S$, conjugates the twist along $x$ into the twist along $y$; the braid relation holds exactly. *Common failure:* transforming only the $e$-strings in (a), which breaks the commutation of $\bar Z_1$ with $\bar X_2$ and defines no unitary.

**Problem 3.** *Decisive step:* at $K=0$, $H$ is diagonal in the electric basis, and the lowest state with $A_v=A_w=-1$ has $X=-1$ on the straight path from $v$ to $w$. *Result:* (a) $4h+2\Gamma d$, nondegenerate; (b) each of the $2d$ plaquettes adjacent to the string costs $4\Gamma$ to flip instead of $8\Gamma$, so the shift relative to the vacuum is $2d\,[-K^2/(4\Gamma)+K^2/(8\Gamma)]=-dK^2/(4\Gamma)$, and $\sigma=2\Gamma-K^2/(4\Gamma)+O(K^4/\Gamma^3)$; (c) $4K+2Jd-dh^2/(4J)$, $\sigma_m=2J-h^2/(4J)$. Checked by exact diagonalization on the $4\times4$ torus for $d=1,2$. *Common failure:* omitting the vacuum's shift, $-K^2/(8\Gamma)$ per plaquette, which doubles the correction.

**Problem 4.** *Decisive step:* at $J=0$ both $\bar X_i$ commute with $H$, and by the lemma of §7.2 sector energies differ only through products of $X$ along noncontractible dual loops; the shortest representative of $\bar X_2=U(\tilde C_x)$ has weight $L_1$, that of $\bar X_1=U(\tilde C_y)$ weight $L_2$. *Result:* $H_{\rm eff}=E_0(\Gamma)-b_1\bar X_1-b_2\bar X_2$ with $b_2=O(\Gamma^{L_1})$ and $b_1=O(\Gamma^{L_2})$, both positive since an $L$-th order term carries $(-\Gamma)^L$ and $L-1$ negative resolvents, so $\bar X_1=\bar X_2=+1$ is lowest. On the $3\times4$ torus the splittings scale as $\Gamma^{3.02}$ and $\Gamma^{4.06}$. *Common failure:* giving $\bar X_1$ the weight $L_1$ because of its index; it is the cut along $y$.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester II Block 3. Written to the note-quality-template standard on 2026-10-02. Last revised 2026-10-04.*
