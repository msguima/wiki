---
title: "Sem II Week 11 — String-Net Condensation: Wen's Mechanism for Emergent Gauge Fields"
type: lecture-notes
course: syllabus
semester: 2
week: 11
block: 3
duration: 4 hours (3 hr lectures + 1 hr seminar)
prerequisites: Sem II Weeks 2, 3, 7, 8 and 10; Semester I Weeks 4, 5 and 7
modified: 2026-10-03
---

# Sem II Week 11 — String-Net Condensation: Wen's Mechanism for Emergent Gauge Fields

> *[[week-07-kogut-susskind-hamiltonian|Sem I Week 7]] drew the electric field of $\mathbb{Z}_2$ gauge theory as closed strings, and [[sem2-week-08-toric-code-solved-to-the-bone|Sem II Week 8]] wrote the [[toric-code]] ground state as an equal-weight gas of them. Levin and Wen run the argument backwards: string types, branching rules and $F$-symbols are the input; a fixed-point wave function, a commuting-projector Hamiltonian, and gauge theory with its charges are the output. We do this completely for the two $\mathbb{Z}_2$ string nets, the toric code and the double semion of [[sem2-week-07-spt-phases-group-cohomology-dijkgraaf-witten|Sem II Week 7]], evaluate the Wilson loop inside the wave function, and state the content of the doubled Ising phase. Block 3 closes here.*

### How to use this chapter

- **In class:** in the first lecture define the input data (§2.1), the $F$-move and the pentagon (2.1)–(2.3), and enumerate the $\mathbb{Z}_2$ pentagon with Table 1 down to (2.4); then the local rules (§3.1), their $\mathbb{Z}_2$ form (3.1)–(3.3) with Figure 2, the planarity lemma (§3.3) and the loop gases (3.4); Problems 1 and 2. In the second lecture derive the plaquette term as a sequence of $F$-moves (§4.2, Figure 3, (4.3)–(4.4)), the Hamiltonians (4.5) and their ground states (§4.3), the Wilson loop at the fixed point (5.1)–(5.3), the exact formula (5.7) and the bounds (5.8); Problems 3 and 4. In the third lecture: the perimeter coefficient (5.9) with Figure 4, Wen's mechanism (§6) and the doubled Ising content (§7). The seminar hour (§9) is Levin–Wen.
- **For self-study:** §2.4, the torus statements of §4.3, the Hamiltonian route (5.10)–(5.11), §§10–11 and Problems 5⋆–7⋆. Mini-calculation 4 (§8) is handed in at the end of the week; the one calculation to do alone is its Sub-task 2, the 128 configurations of the coronene patch.
- **Instructor checkpoint:** two errors recur. The first is to read the loop value $d_1=-1$ of the double semion as a negative quantum dimension (F1, M1). The second is to use $(-1)^{N}$ off the plane, where the lemma of §3.3 fails (F2).

## 0. Reading

**Primary:** Levin, Wen (LW), "String-net condensation: A physical mechanism for topological phases", *Phys. Rev. B* 71 (2005) 045110 [cond-mat/0404617]: §II (gauge theories as string nets, eqs. (1)–(2)), §IV.A (local rules (4)–(7), self-consistency conditions (9)), §IV.B (the Hamiltonian (11)–(15)), §VI.A (the $\mathbb{Z}_2$ string nets, eqs. (34)–(49)) and App. C. It is the seminar paper of §9.

**Secondary:** Kitaev, "Anyons in an exactly solved model and beyond", *Ann. Phys.* 321 (2006) 2 [cond-mat/0506438], §§10.3–10.6 and 11 (Ising data; section numbers of the *Annals* version) and App. E.1–E.2 ($F$-moves, coherence, Frobenius–Schur indicator); Sem II Weeks 7 (§§2.3, 6.3–6.4), 8 and 10; Sem I Week 7 §§5, 7–8, Week 5 §5 and Week 4 §3.1.

**Optional research reading:** Levin, Wen, "Fermions, strings, and gauge fields in lattice spin models", *Phys. Rev. B* 67 (2003) 245316 [cond-mat/0302460]; LW §V ($3+1$ dimensions); Kirillov, Balsam, "Turaev–Viro invariants as an extended TQFT", arXiv:1004.1533 (the theorem behind §7); Wen, *Quantum Field Theory of Many-Body Systems* (2004), closing chapter; Trebst et al., *Phys. Rev. Lett.* 98 (2007) 070602 [cond-mat/0609048] (the loop gas with tension as a Hamiltonian problem); Castelnovo, Chamon, "Quantum topological phase transition at the microscopic level", *Phys. Rev. B* 77 (2008) 054433 [arXiv:0707.2084] (the transition of a tension-deformed toric code, F6).

Proof-status labels follow note-quality-template §4. The string basis $n_\ell=(1-X_\ell)/2$, the six-index $F$-symbol (2.1), the loop value $d_s$, the reconnection sign $f$, the plaquette coefficient (4.3)–(4.4), the wave-function tension ζ and the auxiliary Ising coupling $K$ of §5 are new to the course; they are fixed here and recorded in [[courses/generalized-symmetries-course/conventions|conventions]] §§6 and 9.

## 1. Motivation and setting

Semester I put gauge fields in by hand: Wegner made the Ising flip local, and Kogut and Susskind wrote the Hamiltonian whose $\mathbb{Z}_2$ electric field draws closed strings, few and short at strong coupling, fluctuating at every scale in the deconfined phase, the simplest [[topological-order]] (Sem I Week 7 §§5, 8; Sem I Week 5 §5). Wen's proposal reverses the order. Start from a local spin model whose low-energy configurations are nets of strings, with no gauge field in the definition; if the strings condense, the long-distance theory is a gauge theory, the string ends are its charges, and the gauge group is read off the rules by which strings branch and recombine ([[string-net-condensation]]). The questions of the week: which data define a consistent condensate (§2); which wave function and which exactly soluble Hamiltonian they determine (§§3–4); how the condensate shows up in the Wilson loop (§5); and what else comes out (§§6–7). Category theory stays offstage: $F$-symbols are the coefficients of a local move on pictures, and consistency is checked by enumeration.

## 2. The input data

### 2.1 Strings, labels and branching rules

A string net on the honeycomb lattice has on each link a label $s\in\{0,1,\dots,N\}$, with 0 the null string and $1,\dots,N$ the string types; in our examples every string is its own dual (unoriented). The branching rules $\delta_{ijk}\in\{0,1\}$ list the triples allowed at a vertex, with $\delta_{ij0}=\delta_{ij}$ so that a string may pass through; in fusion language $\delta_{ijk}=N_{ij}^{\,k}$. For $\mathbb{Z}_2$ there is one string type and $\delta_{ijk}=1$ exactly when $i+j+k$ is even: at a trivalent vertex nothing or two strings meet, and the allowed configurations are sets of disjoint closed loops.

Each link is then a qubit, and we follow LW §II and the electric basis of Sem I Week 7: a link is occupied when $X_\ell=-1$, $n_\ell=\tfrac12(1-X_\ell)$, so $Z_\ell$ adds or removes the string. The branching rule is the star $A_v=\prod_{\ell\ni v}X_\ell=+1$ of [[courses/generalized-symmetries-course/conventions|conventions]] §9, and an allowed configuration $\mathcal X$ (the set of occupied links) is a $\mathbb{Z}_2$ 1-cycle. We write $|\mathcal X\rangle$ for the electric-basis state, $N(\mathcal X)$ for its number of loops and $L(\mathcal X)$ for its number of occupied links; Figure 1 names the links around a hexagon.

```
                l2            l1
                  \          /
                   v2 ---- v1
                  /    e1    \
              e2 /            \ e6
      l3 ---- v3       p       v6 ---- l6
                 \            /
              e3  \          / e5
                   v4 ---- v5
                  /    e4    \
                l4            l5
```
**Figure 1. A hexagon $p$: vertices $v_k$ counterclockwise, edges $e_k$ from $v_k$ to $v_{k+1}$, legs $l_k$; the boundary edges at $v_k$ are $e_{k-1}$ and $e_k$ ($e_0\equiv e_6$).**

### 2.2 The $F$-move and the pentagon [Proved for the abelian reduction.]

Three strings $a,b,c$ enter a disc from below and $d$ leaves on top. Inside, either $a,b$ join first into $e$, or $b,c$ join first into $f$; the $F$-move changes basis,
$$
|((ab)_e\,c)_d\rangle=\sum_f\,[F^{abc}_d]_{ef}\;|(a\,(bc)_f)_d\rangle,\tag{2.1}
$$
the map $(X\otimes Y)\otimes Z\to X\otimes(Y\otimes Z)$ of [[courses/generalized-symmetries-course/conventions|conventions]] §6 in components, zero unless all four vertices are allowed. With four incoming strings and outgoing $e$, the basis vector $(((ab)_fc)_gd)_e$ reaches $(a(b(cd)_l)_k)_e$ in two moves ($F^{fcd}_e$, then $F^{abl}_e$) or in three ($F^{abc}_g$ inside, then $F^{ahd}_e$, then $F^{bcd}_k$ inside). The coefficient must not depend on the route:
$$
[F^{fcd}_e]_{gl}\,[F^{abl}_e]_{fk}=\sum_h\,[F^{abc}_g]_{fh}\,[F^{ahd}_e]_{gk}\,[F^{bcd}_k]_{hl}.\tag{2.2}
$$
That this pentagon makes every sequence of moves consistent is MacLane's coherence theorem [Stated — refs: Kitaev App. E.1; LW App. B]. When every fusion has one channel, write $F(a,b,c)\equiv[F^{abc}_{a+b+c}]_{a+b,\,b+c}$; each sum in (2.2) has one term, and
$$
F(a+b,c,d)\,F(a,b,c+d)=F(a,b,c)\,F(a,b+c,d)\,F(b,c,d),\tag{2.3}
$$
the cocycle condition of [[courses/generalized-symmetries-course/conventions|conventions]] §6 and Sem II Week 7 §2.1. A change of basis multiplies $F$ by $\delta u$ (Week 7 §6.4); in a normalized gauge $F=1$ when a label is 0.

### 2.3 The $\mathbb{Z}_2$ pentagon by enumeration [Computed.]

A normalized $\mathbb{Z}_2$ $F$ has one unknown, $f\equiv F(1,1,1)$. Table 1 runs through the 16 quadruples of (2.3): eleven contain no triple $(1,1,1)$, four contain $f$ once on each side, and only $(1,1,1,1)$ constrains $f$.

| $(a,b,c,d)$ | $F(a{+}b,c,d)\,F(a,b,c{+}d)$ | $F(a,b,c)\,F(a,b{+}c,d)\,F(b,c,d)$ |
|---|---|---|
| $(0,1,1,1)$ | $f\cdot1$ | $1\cdot1\cdot f$ |
| $(1,0,1,1)$ | $f\cdot1$ | $1\cdot f\cdot1$ |
| $(1,1,0,1)$ | $1\cdot f$ | $1\cdot f\cdot1$ |
| $(1,1,1,0)$ | $1\cdot f$ | $f\cdot1\cdot1$ |
| $(1,1,1,1)$ | $1\cdot1$ | $f\cdot1\cdot f$ |
| the other eleven | $1$ | $1$ |

**Table 1.** The $\mathbb{Z}_2$ pentagon (2.3) for a normalized $F$.

The last row gives
$$
f^2=1,\qquad f=\pm1.\tag{2.4}
$$
These are the two classes of $H^3(\mathbb{Z}_2,U(1))$ (Week 7 §2.3): $f=+1$ is the input of the toric code, $f=-1$, $\omega=(-1)^{xyz}$, that of the double semion (Week 7 Table 2), and since $F(s,s,s)$ is gauge invariant among normalized gauges (Week 7 (6.9)) no change of basis connects them. We checked by computer the six-index form (2.2) over all labels: 16 admissible instances, all exact for $f=\pm1$; for $f=i$ only $(1,1,1,1)$ fails, with residual 2.

### 2.4 Two non-abelian inputs [Stated — refs: Kitaev 2006 §§10.3–10.6 and eq. (187); LW §VI.B; the pentagons Computed.]

Fibonacci has labels $\{0,\tau\}$, $\tau\otimes\tau=0\oplus\tau$; Ising has $\{0,\sigma,\psi\}$, $\sigma\otimes\sigma=0\oplus\psi$, $\sigma\otimes\psi=\sigma$, $\psi\otimes\psi=0$ (0 is the null string; the anyon tables of §7 write 1 for the trivial anyon). With $\phi=(1+\sqrt5)/2$ and bases $(0,\tau)$, $(0,\psi)$,
$$
[F^{\tau\tau\tau}_\tau]=\begin{pmatrix}\phi^{-1}&\phi^{-1/2}\\ \phi^{-1/2}&-\phi^{-1}\end{pmatrix},\qquad
[F^{\sigma\sigma\sigma}_\sigma]=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
[F^{\sigma\psi\sigma}_\psi]_{\sigma\sigma}=[F^{\psi\sigma\psi}_\sigma]_{\sigma\sigma}=-1,\tag{2.5}
$$
every other admissible $F$ being 1. We checked (2.2) on all 50 admissible label sets of Fibonacci and all 136 of Ising, with residuals below $2.3\times10^{-16}$; Problem 1 derives the Fibonacci matrix. For a self-dual label the vacuum entry defines the quantum dimension and the Frobenius–Schur indicator $\kappa_a=\pm1$ (Kitaev eq. (187)):
$$
[F^{aaa}_a]_{00}=\kappa_a/d_a,\tag{2.6}
$$
so $d_\tau=\phi$, $d_\sigma=\sqrt2$, $d_\psi=1$ with $\kappa=+1$, while the $\mathbb{Z}_2$ string has quantum dimension 1 and $\kappa=f$; the dimensions agree with the largest eigenvalues of the fusion matrices (checked).

## 3. The fixed-point wave function

### 3.1 The local rules [Stated — refs: LW §IV.A, eqs. (4)–(7) and (9).]

LW argue that a condensed phase flows under coarse-graining to a fixed point whose amplitudes $\Phi(\mathcal X)$ depend only on the topology of the picture, and fix it by four rules inside any disc, the outside held fixed: **(R1)** isotopy leaves Φ unchanged (LW (4)); **(R2)** an empty contractible loop of type $s$ is erased at the price $d_s$ (LW (5)); **(R3)** a string that splits in two and recombines into a string of a different type has amplitude zero (LW (6)); **(R4)** two vertices joined by an internal string $m$ equal $\sum_nF^{ijm}_{kln}$ times the four legs joined the other way by $n$ (LW (7)). LW's $F^{ijm}_{kln}$ is (2.1) in a symmetric normalization with vertex factors $\sqrt{d_s}$, and their (9) contains the pentagon. For $\mathbb{Z}_2$ everything reduces to two numbers.

### 3.2 The $\mathbb{Z}_2$ rules and their consistency [Proved.]

For $\mathbb{Z}_2$ every vertex is a string passing through or nothing, so after erasing null strings a picture is a set of loops, (R3) reduces to (R2), and the $F$-moves with a null leg are isotopies with coefficient 1 (LW (34)). One move is left. Take two arcs crossing a disc with endpoints $a,b$ on top and $c,d$ below, let $\mathcal X_\parallel$ pair them $(ac)(bd)$ and $\mathcal X_=$ pair them $(ab)(cd)$, the outside being the same (Figure 2(a)). Rule (R4) with four legs 1 and null internal string is the reconnection
$$
\Phi(\mathcal X_\parallel)=f\,\Phi(\mathcal X_=).\tag{3.1}
$$
Two reconnections return to $\mathcal X_\parallel$, so $f^2=1$. A small loop read as two arcs closed by a cap and a cup becomes two loops after one reconnection (Figure 2(b)), so $d_1=f\,d_1^2$:
$$
d_1\,f=1,\qquad f^2=1,\qquad d_1=f=\pm1,\tag{3.2}
$$
as LW (34) state. The reconnection is also the associator of Week 7: the trees $((11)_01)_1$ and $(1(11)_0)_1$ of (2.1), null strings erased, are the two non-crossing pairings of four endpoints in a disc (Figure 2(c)), one reconnection apart, so with (R1)
$$
F(1,1,1)=[F^{111}_1]_{00}=f=d_1 .\tag{3.3}
$$
The loop value is the invariant $I=F(s,s,s)$ of Week 7 (6.9): $+1$ for the toric code, $-1$ for the double semion.

```
 (a)  a     b               a     b        (b)  .----.            .----.
      |     |                \___/              |    |    = f x   '----'
      |     |      =  f x                       |    |            .----.
      |     |                 ___               '----'            '----'
      |     |                /   \             one loop = f x (two loops):  d1 = f d1^2
      c     d               c     d

 (c)        top: 1                         top: 1
              |                              |
       .--.   |                              |   .--.
       |  |   |          =   f  x            |   |  |
       1  1   1                              1   1  1
    ((11)_0 1)_1                          (1(11)_0)_1
```
**Figure 2. The $\mathbb{Z}_2$ rules: (a) the reconnection (3.1), outside unchanged; (b) a loop read as two arcs gives two loops, so $d_1f=1$; (c) the trees of (2.1) for three strings 1 with total 1, null strings erased, one reconnection apart, so $F(1,1,1)=f$.**

### 3.3 A reconnection changes the number of loops by one [Proved.]

**Lemma.** If $\mathcal X_\parallel$ and $\mathcal X_=$ differ by one reconnection inside a disc $D$ of the plane, then $N(\mathcal X_\parallel)-N(\mathcal X_=)=\pm1$.

*Proof.* The two arcs inside $D$ are disjoint, so on $\partial D$ the endpoints of each are adjacent; call the cyclic order $a_1,a_2,b_1,b_2$, with arcs $a_1a_2$ and $b_1b_2$. The reconnection joins $a_2b_1$ and $b_2a_1$, the only other non-crossing pairing. Outside $D$ the loops join the four endpoints by two disjoint arcs, and since the complement of $D$ on the sphere is a disc, they too form a non-crossing pairing. If the inside arcs belong to different loops, the outside arcs join $a_1a_2$ and $b_1b_2$, and after reconnection $a_2\to b_1\to b_2\to a_1\to a_2$ is one loop: $N$ drops by one. If they belong to the same loop, no outside arc joins $a_1$ to $a_2$ (it would close the loop without the other inside arc), so the outside pairing is $(a_2b_1)(b_2a_1)$, the crossing one being excluded; after reconnection each new inside arc closes with the outside arc on its endpoints, and $N$ rises by one. ∎

The planar input is that outside arcs cannot cross; on a torus they can (F2, Problem 6⋆).

### 3.4 The two loop gases [Proved.]

On a disc or the plane,
$$
\Phi(\mathcal X)=d_1^{\,N(\mathcal X)}\,\Phi(\emptyset),\qquad \Phi_{\rm TC}(\mathcal X)=1,\qquad \Phi_{\rm DS}(\mathcal X)=(-1)^{N(\mathcal X)},\tag{3.4}
$$
which is LW (36). *Uniqueness:* disjoint loops in the plane have an innermost one, erased by (R2) at the price $d_1$; repeating reduces every configuration to the empty one. *Existence:* $d_1^N$ obeys (R1) and (R2), and it obeys (3.1) because $N(\mathcal X_\parallel)=N(\mathcal X_=)\pm1$ by the lemma and $d_1^{\pm1}=f$ by (3.2). On the honeycomb $N(\mathcal X)$ is the number of connected components of the occupied links. For $d_1=1$ this is the equal-weight loop gas of Sem II Week 8 and of the toric-code point of Sem I Week 7 §8; for $d_1=-1$ every loop carries a sign.

## 4. The Levin–Wen Hamiltonian

### 4.1 Vertex and plaquette terms [Stated — refs: LW (11)–(15); the $\mathbb{Z}_2$ case Proved in §§4.2–4.3.]

LW's Hamiltonian is
$$
H=-\sum_vQ_v-\sum_pB_p,\qquad B_p=\sum_sa_s\,B_p^s,\qquad a_s=\frac{d_s}{\mathcal D^2},\qquad \mathcal D^2=\sum_sd_s^2 ,\tag{4.1}
$$
with $Q_v$ the projector onto allowed branchings (LW (12)) and $B_p^s$ the operator that inserts an empty $s$-loop in $p$ and reduces the picture to a lattice configuration with the rules, its matrix elements being products of six $F$-symbols (LW (13)–(14), App. C). LW state that for solutions of (9) obeying their unitarity condition (15) all terms are commuting projectors and the ground state has $Q_v=B_p=1$ with amplitudes Φ. For $\mathbb{Z}_2$, $\mathcal D^2=2$ and
$$
Q_v=\tfrac12\,(1+A_v),\qquad B_p=\tfrac12\,(1+d_1B_p^1).\tag{4.2}
$$

### 4.2 The plaquette term as a sequence of $F$-moves [Proved.]

Draw an empty 1-loop just inside $p$ and push it onto the six edges (Figure 3). Along an empty edge this is an isotopy. Along an occupied edge the loop and the string run parallel, and one reconnection (3.1), coefficient $f$, empties the middle of the edge and turns both arcs back near its endpoints. At $v_k$ the outcome depends on $(n_{e_{k-1}},n_{e_k},n_{l_k})$: a vertex $(0,0,0)$ becomes $(1,1,0)$; $(1,0,1)$ becomes $(0,1,1)$, the string from $l_k$ turning into the loop's arc along $e_k$, and vice versa; both with no factor. A vertex $(1,1,0)$ is left with a small closed loop hugging its corner and enclosing nothing, which (R2) erases with a factor $d_1$; it becomes $(0,0,0)$.

```
 vertex v_k with its leg pointing out of p; '=' occupied edge, '|' occupied leg, ':' empty leg

        :                  |                  |                  :
   =====+=====        =====+                  +=====        -----+-----
 (1,1,0) -> (0,0,0)  (1,0,1) -> (0,1,1)  (0,1,1) -> (1,0,1)  (0,0,0) -> (1,1,0)
   factor d_1           factor 1            factor 1            factor 1

 plus one factor f for each occupied edge of p (the reconnection that empties it)
```
**Figure 3. The plaquette operator as moves: insert a loop, reconnect it with each occupied edge (factor $f$), erase the corner loops at vertices $(1,1,0)$ (factor $d_1$); every edge of $p$ flips and no leg changes.**

So $B_p^1|\mathcal X\rangle=c_p(\mathcal X)\,|\mathcal X+\partial p\rangle$ with
$$
c_p(\mathcal X)=f^{\,n_{\rm occ}}\,d_1^{\,n_{110}},\tag{4.3}
$$
$n_{\rm occ}$ the occupied edges of $p$ and $n_{110}$ the vertices of $p$ with both boundary edges occupied. If $\mathcal X\cap\partial p$ is neither empty nor all of $\partial p$, the occupied edges form $m$ runs; a run of $r$ edges has $r-1$ interior vertices of type $(1,1,0)$ and ends at two vertices whose legs are occupied, and by the branching rule no other leg of $p$ is. Then $n_{\rm occ}+n_{110}=\sum_{\rm runs}(2r-1)\equiv m$ mod 2 and $n_{\rm legs}=2m$; for the empty and the full boundary $n_{\rm legs}=0$ and $n_{\rm occ}+n_{110}\in\{0,12\}$. With $f=d_1$, therefore,
$$
c_p(\mathcal X)=d_1^{\,n_{\rm legs}/2},\qquad B_p^1=\prod_{\ell\in\partial p}Z_\ell\;\prod_{k=1}^{6}\big(\sqrt{d_1}\big)^{\,n_{l_k}},\qquad \sqrt{-1}=i,\tag{4.4}
$$
which is LW (38). Since Φ obeys the rules, evaluating $\mathcal X\cup{\rm loop}$ two ways gives $d_1\Phi(\mathcal X)=c_p(\mathcal X)\,\Phi(\mathcal X+\partial p)$. We checked by computer that $f^{n_{\rm occ}}d_1^{n_{110}}$, $d_1^{n_{\rm legs}/2}$ and $d_1\Phi(\mathcal X)/\Phi(\mathcal X+\partial p)$ agree for all 896 pairs $(p,\mathcal X)$ of the coronene patch (seven hexagons, 24 vertices, 30 links, 128 closed configurations) and both signs of $d_1$, and that the first two agree for all 98,304 pairs of the $3\times4$ honeycomb torus.

### 4.3 The two $\mathbb{Z}_2$ Hamiltonians and their ground states [Proved; the torus counts Computed.]

With (4.2) and (4.4),
$$
H_{\rm TC}^{\rm SN}=-\sum_v\frac{1+A_v}2-\sum_p\frac{1+\prod_{\ell\in\partial p}Z_\ell}2,\qquad
H_{\rm DS}=-\sum_v\frac{1+A_v}2-\sum_pP_p\,\frac{1-\prod_{\ell\in\partial p}Z_\ell\prod_{k}i^{\,n_{l_k}}}2,\tag{4.5}
$$
with $P_p=\prod_kQ_{v_k}$. The first is half the toric code of [[courses/generalized-symmetries-course/conventions|conventions]] §9 plus a constant; the second is LW (40) up to factors of 2, a constant and the projector (F4). On the closed subspace, where all $A_v=1$:

(a) $B_p^1$ is Hermitian and squares to 1: legs do not flip, so $c_p(\mathcal X+\partial p)=c_p(\mathcal X)$ and $c_p^2=d_1^{n_{\rm legs}}=1$.

(b) $[B_p^1,B_q^1]=0$. Non-adjacent plaquettes do not touch each other's links. For adjacent ones $c_p,c_q$ depend only on links in a disc around $p\cup q$; completing the configuration outside to a closed planar one, $c_p=d_1\Phi(\mathcal X)/\Phi(\mathcal X+\partial p)$, and both orderings give $d_1^2\Phi(\mathcal X)/\Phi(\mathcal X+\partial p+\partial q)$.

(c) Since $\Phi=\pm1$,
$$
B_p^1|\Phi\rangle=\sum_{\mathcal X}\Phi(\mathcal X)\,c_p(\mathcal X)\,|\mathcal X+\partial p\rangle=d_1\sum_{\mathcal X}\frac{\Phi(\mathcal X)^2}{\Phi(\mathcal X+\partial p)}\,|\mathcal X+\partial p\rangle=d_1|\Phi\rangle,
$$
so $B_p=\tfrac12(1+d_1^2)=1$ on $|\Phi\rangle$. On a planar patch the closed configurations are the boundaries $\partial S$ of sets of hexagons and the flips act freely and transitively on them, so the ground state is unique and $n$ violated plaquettes have degeneracy $\binom{N_p}{n}$. On the coronene we found by diagonalization the ground state (3.4) and levels $-7+n$ of $-\sum_pB_p$ with degeneracies $\binom7n$, $n=0,\dots,7$, for both signs. On the $3\times4$ torus (24 vertices, 36 links, 12 plaquettes, 8192 closed configurations in four homology classes) each model has four ground states, one per class, and $\prod_pB_p^1=+1$ in every class, as $d_1^{12}=1$ requires (F2).

## 5. The Wilson loop inside the wave function

### 5.1 At the fixed point [Proved.]

The Wilson loop of $U_\ell=Z_\ell$ ([[courses/generalized-symmetries-course/conventions|conventions]] §§4, 9) is $W(C)=\prod_{\ell\in C}Z_\ell$, which inserts a string, $W(C)|\mathcal X\rangle=|\mathcal X+C\rangle$. For any state Ψ of the closed subspace
$$
\langle W(C)\rangle_\Psi=\frac{\sum_{\mathcal X}\Psi(\mathcal X)^*\,\Psi(\mathcal X+C)}{\sum_{\mathcal X}|\Psi(\mathcal X)|^2},\tag{5.1}
$$
a ratio of two sums over string nets, the denominator being the norm. For $\Phi_{\rm TC}$ and contractible $C=\partial S$, $\mathcal X\mapsto\mathcal X+C$ is a bijection of each class and $\langle W(C)\rangle=1$: a perimeter law with vanishing coefficient. In the double semion the closed string is $W_{\rm DS}(C)=\prod_{p\in S}B_p^1$; its coefficient telescopes to $d_1^{|S|}\Phi(\mathcal X)/\Phi(\mathcal X+C)$, so
$$
\langle W_{\rm DS}(C)\rangle_{\Phi_{\rm DS}}=d_1^{\,|S|}=(-1)^{|S|}.\tag{5.2}
$$
For the toric code $W(C)=\prod_{p\in S}B_p^1$, with $B_p^1=\prod_{\partial p}Z$ and every interior link appearing twice; in a basis of flux eigenstates, $b_p=\tfrac12(1-B_p^1)$, any state with all $A_v=1$ has
$$
\langle W(C)\rangle=1-2\,{\rm Prob}\Big(\sum_{p\in S}b_p\ \text{odd}\Big):\tag{5.3}
$$
the Wilson loop measures the parity of the fluxes in $S$, and at the fixed point there are none.

### 5.2 The norm is an Ising model [Proved.]

Give each string a tension in the wave function,
$$
|\Psi_\zeta\rangle\propto e^{\frac\zeta2\sum_\ell X_\ell}|\Phi\rangle,\qquad \Psi_\zeta(\mathcal X)\propto e^{-\zeta L(\mathcal X)}\,\Phi(\mathcal X),\qquad \zeta\ge0,\tag{5.4}
$$
since $\sum_\ell X_\ell=E-2L(\mathcal X)$ with $E$ links; to first order this is the toric code with an electric term at $\zeta=\Gamma/2$ (§5.3). The norm is a loop gas with fugacity $t=e^{-2\zeta}$ per link, and on a planar patch the high-temperature expansion of [[week-04-bkt-kramers-wannier-disorder|Sem I Week 4]] §3.1, $e^{Kss'}=\cosh K\,(1+t\,ss')$, with Ising spins $s_v$ on the $V$ vertices, gives
$$
\sum_{\mathcal X}t^{L(\mathcal X)}=\frac{Z_{\rm Ising}(K)}{2^V\cosh^EK},\qquad \tanh K=e^{-2\zeta};\tag{5.5}
$$
the signs of the double semion drop out. In (5.1), $L(\mathcal X)+L(\mathcal X+C)=2L(\mathcal X)+|C|-2L_C(\mathcal X)$, with $L_C$ the occupied links of $C$, so
$$
\langle W(C)\rangle_\zeta=e^{-\zeta|C|}\,\frac{\sum_{\mathcal X}t^{\,L(\mathcal X)-L_C(\mathcal X)}}{\sum_{\mathcal X}t^{\,L(\mathcal X)}} .\tag{5.6}
$$
The numerator is the loop gas with fugacity 1 on $C$. In Ising form each link of $C$ carries $1+s_is_j$ instead of $1+t\,s_is_j$, and $(1+s_is_j)/(1+t\,s_is_j)$ is $2/(1+t)$ for $s_i=s_j$ and 0 otherwise; with $e^{-\zeta}\cdot2/(1+e^{-2\zeta})=1/\cosh\zeta$,
$$
\langle W(C)\rangle_\zeta=(\cosh\zeta)^{-|C|}\;P_K(C),\tag{5.7}
$$
where $P_K(C)$ is the Ising probability that all spins along $C$ are equal. Since $P_K\le1$, and the numerator of (5.6) is termwise at least the denominator ($t\le1$, all terms non-negative),
$$
e^{-\zeta|C|}\ \le\ \langle W(C)\rangle_\zeta\ \le\ (\cosh\zeta)^{-|C|}.\tag{5.8}
$$
Both bounds are perimeter laws: for every ζ, the dressed string net has no area law. We checked (5.7) on the coronene against direct enumeration of the $2^{24}$ Ising configurations ($|C|=6,10,18$; $\zeta=0.1,0.3,0.7$; agreement to $3\times10^{-15}$), and that $\langle W_{\rm DS}(C)\rangle_\zeta=d_1^{|S|}\langle W(C)\rangle_\zeta$, as the telescoped coefficient and $\Phi^2=1$ imply.

### 5.3 The perimeter coefficient [Controlled to $O(\zeta^3)$ and to $O(\Gamma^2)$.]

For small ζ the Ising model is deep in its ordered phase, $e^{-2K}=(1-t)/(1+t)=\tanh\zeta$. In the cluster expansion about an aligned state a flipped spin of degree 3 costs $e^{-6K}=\tanh^3\zeta$ and connected clusters of two or more cost at least $e^{-8K}$; the constraint removes exactly the single flips at the $|C|$ vertices of $C$. For $C$ away from the patch boundary, $\ln P_K(C)=-|C|\tanh^3\zeta+O(|C|\tanh^4\zeta)$ and
$$
\mu\equiv-\frac{\ln\langle W(C)\rangle_\zeta}{|C|}=\ln\cosh\zeta+\tanh^3\zeta+O(\zeta^4)=\frac{\zeta^2}2+\zeta^3+O(\zeta^4).\tag{5.9}
$$
On the 19-hexagon patch ($2^{19}$ configurations) we found $(\mu-\ln\cosh\zeta)/\tanh^3\zeta=1.010,\ 1.021,\ 1.043$ for the hexagon loop at $\zeta=0.005,0.01,0.02$, and $1.034,\ 1.070,\ 1.148$ for the 18-link loop around the coronene: the limit is 1, and the shape enters at $O(\zeta^4)$.

The Hamiltonian route gives the same leading term, by the mechanism of Figure 4. In $H=-\sum_vA_v-\sum_pB_p^1-\Gamma\sum_\ell X_\ell$, the $\mathbb{Z}_2$ Kogut–Susskind Hamiltonian of [[courses/generalized-symmetries-course/conventions|conventions]] §4 with energetic Gauss law, $X_\ell$ commutes with every $A_v$ and anticommutes with the two $B_p^1$ containing ℓ, so $X_\ell|\Phi\rangle$ costs 4 and
$$
|\Psi\rangle=|\Phi\rangle+\frac\Gamma4\sum_\ell X_\ell|\Phi\rangle+|\Psi_2\rangle+O(\Gamma^3),\tag{5.10}
$$
which is (5.4) at $\zeta=\Gamma/2$ to this order. The $X_\ell|\Phi\rangle$ are orthonormal (two hexagons share at most one link), $W(C)$ anticommutes with $X_\ell$ for $\ell\in C$ and commutes otherwise, and $W(C)|\Phi\rangle=|\Phi\rangle$, so
$$
\langle W(C)\rangle=\frac{1+\frac{\Gamma^2}{16}(E-2|C|)+2{\rm Re}\langle\Phi|\Psi_2\rangle}{1+\frac{\Gamma^2}{16}E+2{\rm Re}\langle\Phi|\Psi_2\rangle}+O(\Gamma^3)=1-\frac{\Gamma^2}8\,|C|+O(\Gamma^3),\qquad \mu=\frac{\Gamma^2}8+O(\Gamma^3),\tag{5.11}
$$
equal to $\zeta^2/2$ at $\zeta=\Gamma/2$. Exact diagonalization on the $3\times4$ torus (trivial class, 2048 states), with μ from a two-hexagon and a one-hexagon loop, gives $\mu/(\Gamma^2/8)=1.0103,\ 1.0212,\ 1.0451$ at $\Gamma=0.005,0.01,0.02$. The next term distinguishes the two states: $(\mu-\Gamma^2/8)/\Gamma^3\to0.26$ in the diagonalization (Problem 7⋆ derives $\tfrac14$), against $\tfrac18$ from (5.9); the dressing (5.4) is exact only to first order (F7).

```
                    ______
                   /      \
            ______/   q    \______
           /      \   x    /      \
          /        \__l___/        \
          \        /======\        /
           \______/=      =\______/
                  \=  p0  =/
                   \= x  =/
                    \====/
```
**Figure 4. $C=\partial p_0$ (doubled lines) and a link ℓ of $C$ shared with $q$: the term $\frac\Gamma4X_\ell$ of (5.10) puts a virtual flux pair (x) on $p_0$ and $q$, one inside $S$ and one outside, which reverses $W(C)$ by (5.3).**

> **Physical picture.** The Wilson loop counts, mod 2, the visons inside $C$ (5.3). In the deconfined phase they appear as tightly bound virtual pairs, and a pair counts only when it straddles $C$, so $\ln\langle W\rangle\propto-|C|$, exactly at $O(\Gamma^2)$ by (5.11). This is the equal-time slice of [[week-05-wegner-z2-gauge-theory|Sem I Week 5]] §5, where a reversed link of $C$ is the smallest vison loop linking $C$ and gives $\mu=2e^{-8\beta}$. Confinement needs free visons, which randomize the parity inside $S$ (Problem 4), that is amplitudes that grow with enclosed area, as in the strong-coupling vacuum of Sem I Week 7 §5; local link weights such as (5.4) cannot produce them, by (5.8). Within the family (5.4), by contrast, the equal-time perimeter law holds at every ζ and does not by itself detect condensation (F6); the symmetry reading is in §6.

## 6. Whence gauge theory: Wen's mechanism [Stated — refs: LW §§II, IV.B, V; the $\mathbb{Z}_2$ statements Proved in §§3–5.]

LW §II reads the $\mathbb{Z}_2$ Kogut–Susskind theory as a theory of strings, with $\Gamma$ as tension, $\prod_{\partial p}Z$ as kinetic term and Gauss's law as closure, in the dictionary of Sem II Week 8 §6 (Table 1); its tensionless endpoint is the $d_1=1$ string net of §4.3. For $U(1)$ the flux lines carry oriented integers that add to zero at a vertex; for a group $G$ they carry irreducible representations whose product at a vertex contains the trivial one. Conversely (LW §IV.B), with $G$'s irreducible representations as labels, their dimensions as $d_s$ and $6j$ symbols as $F$, $Q_v$ and $B_p$ become the charge and flux projectors of lattice gauge theory without electric term, the quantum double $D(G)$ of [[sem2-week-10-beyond-z2-quantum-doubles-modular-data-chern-simons|Sem II Week 10]]; LW §VI.C find the eight quasiparticles of $D(S_3)$ this way. Other solutions of the pentagon give other phases: $f=-1$ the twisted $\mathbb{Z}_2$ gauge theory of Week 7, and (2.5) phases with irrational quantum dimensions, which no discrete gauge theory has.

For $\mathbb{Z}_2$ the mechanism comes down to three statements. The gauge field is the condensate: the ground state (3.4) is a gas of electric flux lines. The charges are its boundaries: an open string $\prod_{\ell\in\gamma}Z_\ell$ violates only the two vertex terms at its ends (Problem 3). Near the toric-code point the condensate breaks the electric 1-form symmetry spontaneously ([[sem2-week-03-spontaneous-breaking-of-higher-form-symmetries|Sem II Week 3]]), with the perimeter law (5.11) as order parameter; in $d=3$ this symmetry is 1-form, with Wilson lines charged and dual-lattice lines $\prod X$ as symmetry operators, as the form-degree table of [[courses/generalized-symmetries-course/conventions|conventions]] §6 requires. Within the dressed family (5.4) the same diagnostic does not separate condensed from dilute loops (F6) [Heuristic beyond (5.11)].

> **Physical picture.** Gauge field and charges have one origin: the condensed strings are flux lines, and where a string ends the branching rule fails, which is a nonzero divergence, that is a charge [exact for $\mathbb{Z}_2$ by Problem 3 and §4.3]. In $3+1$ dimensions string nets that obey LW's symmetry condition (32) give gauge theories whose charges are bosons or fermions, so gauge bosons and fermions emerge together [Stated — refs: LW §V and their 2003 paper].

## 7. Beyond $\mathbb{Z}_2$: the doubled Ising phase [Stated — refs: LW §§I, VII; Kitaev 2006 §§10–11; Kirillov–Balsam; the numbers Computed.]

LW call string-net phases "doubled": a sum of two TQFTs of opposite chirality, invariant under parity and time reversal (LW §I). Precisely, the string net on a fusion category $\mathcal C$ realizes its Drinfeld center $Z(\mathcal C)$, with $\mathcal D_{Z(\mathcal C)}=\mathcal D_{\mathcal C}^2$, and $Z(\mathcal C)\simeq\mathcal C\times\bar{\mathcal C}$ when $\mathcal C$ is a modular anyon theory; Kirillov and Balsam prove the identification for the Turaev–Viro state sum. The $\mathbb{Z}_2$ inputs have $\mathcal D_{\mathcal C}^2=2$ and both phases $\mathcal D=2$ (Week 10). The Ising input (2.5) has $\mathcal D_{\mathcal C}^2=4$ and, as an anyon theory, $\theta_\sigma=e^{i\pi/8}$, $\theta_\psi=-1$ (Kitaev §§10.6, 11); its double has the nine anyons $(a,\bar b)$ of Table 2, $d_{(a,\bar b)}=d_ad_b$, $\theta_{(a,\bar b)}=\theta_a\theta_b^*$.

| $(a,\bar b)$ | $(1,\bar1)$ | $(1,\bar\sigma)$ | $(1,\bar\psi)$ | $(\sigma,\bar1)$ | $(\sigma,\bar\sigma)$ | $(\sigma,\bar\psi)$ | $(\psi,\bar1)$ | $(\psi,\bar\sigma)$ | $(\psi,\bar\psi)$ |
|---|---|---|---|---|---|---|---|---|---|
| $d$ | 1 | $\sqrt2$ | 1 | $\sqrt2$ | 2 | $\sqrt2$ | 1 | $\sqrt2$ | 1 |
| θ | 1 | $e^{-i\pi/8}$ | $-1$ | $e^{i\pi/8}$ | 1 | $-e^{i\pi/8}$ | $-1$ | $-e^{-i\pi/8}$ | 1 |

**Table 2.** The doubled Ising phase.

With the definitions of Sem II Week 10,
$$
\mathcal D^2=\Big(\sum_ad_a^2\Big)^2=16,\qquad \mathcal D=4,\qquad \Theta=\frac1{\mathcal D}\sum d^2\theta=\frac14\,\Big|\sum_ad_a^2\theta_a\Big|^2=\frac14\,\big|1+2e^{i\pi/8}-1\big|^2=1,\tag{7.1}
$$
so $c\equiv0$ mod 8: the Ising layer alone has $\Theta=e^{i\pi/8}$, $c=\tfrac12$, and its mirror cancels it. We checked (7.1) by computer, with the spins obtained from Ising $R$-symbols that satisfy both hexagon equations. For Fibonacci, LW's "doubled Yang–Lee" model of §VI.B (spins $e^{\mp4\pi i/5}$, LW (52)), the same count gives four anyons with $d=1,\phi,\phi,\phi^2$ and $\mathcal D=1+\phi^2\approx3.618$. Chirality cancellation is what allows a string net to exist: a sum of commuting local projectors need have no gapless modes at a cut, which a chiral phase would carry [Heuristic; the edge side is Sem II Week 10 §8].

## 8. Mini-calculation 4 (hand-in)

### 8.1 Scope

Everything is exact on finite patches and small tori: the coronene (7 hexagons), the 19-hexagon patch (54 vertices, 72 links) and the $3\times4$ honeycomb torus in brick-wall form. Nothing is claimed about continuum limits; the non-abelian data of Sub-task 1 are imported from §2.4.

### 8.2 Variable dictionary

The gauge-theory reading of $n_\ell$, $A_v$, $\prod_{\partial p}Z$ and $W(C)$ is that of Sem II Week 8 §6 (Table 1); the new entries are

| symbol | string net (§§2–4) | norm (§5.2) |
|---|---|---|
| $Q_v=\frac12(1+A_v)$, $B_p^1$ | branching rule; loop insertion and $F$-moves | closed loops; flips $\partial p$ |
| $f=d_1$ | reconnection sign, loop value | drops out |
| ζ, $t=e^{-2\zeta}$ | tension in the wave function, $\Gamma/2$ at first order | fugacity, $\tanh K$ |
| $W(C)$ | string inserted along $C$ | fugacity 1 on $C$ |

### 8.3 Sub-tasks

**Sub-task 1: the pentagon by enumeration.** Code (2.2) for multiplicity-free data and run it on $\mathbb{Z}_2$ with $f=1,-1,i$, on Fibonacci and on Ising (2.5). *Deliverable:* the number of admissible label sets and the largest residual. *Checkpoint:* 16, 50 and 136 sets; residual 0 for $f=\pm1$, below $2.3\times10^{-16}$ for Fibonacci and Ising; for $f=i$ only $(1,1,1,1)$ fails, residual 2.

**Sub-task 2: the loop gases on the coronene.** Enumerate the 128 closed configurations, compute $N(\mathcal X)$, build $B_p^1$ from (4.4), verify $(B_p^1)^2=1$, the commutators and (4.3) against $d_1\Phi(\mathcal X)/\Phi(\mathcal X+\partial p)$, and diagonalize $-\sum_pB_p$ on the closed subspace for both $d_1$. *Deliverable:* the histogram of $N$, the spectrum, the normalized overlap $\langle\Phi_{\rm TC}|\Phi_{\rm DS}\rangle$. *Checkpoint:* $N=0,1,2,3$ occur $1,94,31,2$ times; levels $-7+n$ with degeneracies $\binom7n$ and ground state (3.4); $\sum_{\mathcal X}(-1)^{N(\mathcal X)}=-64$, overlap $-\tfrac12$.

**Sub-task 3: the torus.** On the $3\times4$ torus sort the 8192 closed configurations by winding parities, find the ground states of both models in each class, test $(-1)^N$, and exhibit a reconnection that leaves $N$ unchanged. *Deliverable:* ground states per class and the counterexample. *Checkpoint:* 2048 configurations and one ground state per class for each model, $\prod_pB_p^1=+1$ in every class; $(-1)^N$ is the double-semion ground state in the trivial class (residual $\sim10^{-14}$) and fails in the other three (residual about 3).

**Sub-task 4: the perimeter law in the norm.** On the 19-hexagon patch compute $\langle W(C)\rangle_\zeta$ from (5.1) for the loops around one hexagon, two, three in a triangle, three in a row and the coronene ($|C|=6,10,12,14,18$), check (5.7) on the coronene by enumerating the Ising configurations, and extract μ. *Deliverable:* μ against $|C|$ and ζ. *Checkpoint:* at $\zeta=0.1$, $\mu=0.006469,\ 0.006683,\ 0.006820,\ 0.006773,\ 0.007124$, between $\ln\cosh\zeta=0.004992$ and $\zeta$, as (5.8) requires; (5.7) holds to $10^{-14}$; $(\mu-\ln\cosh\zeta)/\tanh^3\zeta\to1$ as $\zeta\to0$.

**Sub-task 5: the Hamiltonian check.** Diagonalize $-\sum_pB_p^1-\Gamma\sum_\ell X_\ell$ in the trivial class of the $3\times4$ torus and compute $\langle W\rangle$ for a one-hexagon and a two-hexagon loop. *Deliverable:* μ against Γ. *Checkpoint:* $\mu/(\Gamma^2/8)=1.0103,\ 1.0212,\ 1.0451,\ 1.1371$ at $\Gamma=0.005,0.01,0.02,0.05$; $1-\langle W(\partial p)\rangle=1.897\times10^{-5}$ at $\Gamma=0.005$, against $12\Gamma^2/16=1.875\times10^{-5}$ from (5.11).

### 8.4 What is proved, modeled and imported

Proved: (2.3)–(2.4), §3, §4 for $\mathbb{Z}_2$, and (5.1)–(5.8). Controlled: (5.9) to $O(\zeta^3)$, (5.11) to $O(\Gamma^2)$. Computed: every number above. Modeled: the dressing (5.4). Imported: the data (2.5).

## 9. Seminar: Levin–Wen, string-net condensation

**Format.** As in syllabus §7: the presenter states the technical claim, identifies what it needs from Semester I and reproduces one step at the board; the instructor places the result on the course map. Every student reads LW §II, §IV.A–B, §VI.A and App. C, and brings Problem 3.

**The technical claim.** Every solution $(F,d)$ of LW (9) obeying (15) defines a fixed-point wave function through (4)–(7) and an exactly soluble honeycomb Hamiltonian (11) with that ground state; the phases so obtained are the doubled topological phases, and the deconfined phases of lattice gauge theories are the case of $6j$ symbols.

**What it needs from Semester I.** The $\mathbb{Z}_2$ Kogut–Susskind Hamiltonian, its electric strings and its toric-code point (Sem I Week 7 §§7–8); the perimeter law of the deconfined phase (Sem I Week 5 §5); and the double semion and toric code of Sem II Weeks 7 and 8.

**The step at the board.** LW §VI.A: from (34) to the wave functions (36), $\Phi_\pm=(\pm1)^{X_c}$, and to the magnetic terms (38)–(40), with the leg factor $i^{(1-\sigma^x_j)/2}$ from App. C compared with Figure 3 and (4.4).

**For the discussion.** (i) LW (40) omits the projector $P_p$ (F4). (ii) After (43) LW call the end of the open $W_2=\prod_{\rm edges}\sigma^z$ a magnetic flux; with the Gauss law of their own §II, which is ours, that end violates $Q_I$ and is a charge, and the $e\leftrightarrow m$ symmetry of the toric code means (42)–(43) cannot decide the name. (iii) The 2003 paper's fermions at string ends, against the exchange statistics of Sem II Week 8.

**The open question it leaves for this course.** LW §VII close by asking for an analogous picture of chiral phases. String nets give $c\equiv0$; the chiral phases of Sem II Week 10 need something else.

**On the course map.** The input $F$ is the anomaly class of Week 7, the output the deconfined phase of Semester I read as the breaking of Week 3, and the Ising input returns in Block 4 as the fusion of the Kramers–Wannier defect.

## 10. Subtleties and fine print

**F1. Loop values and quantum dimensions.** By (2.6) and (3.3) the loop value of (R2) is $\kappa_s$ times the quantum dimension: the semion string has loop value $-1$ while every anyon of the double semion has quantum dimension 1, and $\mathcal D^2=\sum_sd_s^2$ and the norm of Φ do not see the sign. In §§2–5 the label 1 is the $\mathbb{Z}_2$ string and $d_1$ its loop value; in §7, 1 is the trivial anyon and $d_a$ a quantum dimension.

**F2. The plane and the torus.** The lemma of §3.3 needs non-crossing outside arcs. On the torus a reconnection involving non-contractible strands can leave $N$ unchanged, and then $(-1)^N$ violates (3.1); on the $3\times4$ torus this happens in all three classes with odd winding. The model still has one ground state per class, with amplitudes other than $(-1)^N$ there, and the local rules do not fix the relative phases of the four states.

**F3. Trivalence.** At a 4-valent vertex with four strings the two planar resolutions are one reconnection apart, so $d_1^N$ is ambiguous by $d_1$ (Problem 2). The toric code lives on the square lattice because $d_1=1$; the double semion needs a trivalent lattice or a resolution rule.

**F4. The projector in the double semion.** With an odd number of charges at the vertices of $p$, $n_{\rm legs}$ is odd and $\prod_ki^{n_{l_k}}=\pm i$: without $P_p$ the operator of (4.5) squares to $-1$ there and is not Hermitian. LW remark that $P_p$ may be dropped without changing the physics; that holds for $d_1=1$, but as written their (40) is Hermitian only on the closed subspace, and we keep $P_p$.

**F5. What the fixed point fixes.** The loop gas is one point of the deconfined phase; μ is non-universal, and the universal content is the long-distance structure (degeneracy, anyons, the entanglement entropy of Sem II Week 9).

**F6. Dressing and dynamics.** The tension (5.4) matches the perturbed toric code at first order, so μ agrees at $O(\Gamma^2)$ and differs at $O(\Gamma^3)$, and the confinement transition of the perturbed toric code (Sem II Week 8; Trebst et al.) lies outside every wave function of that form. The family has a transition of its own: the norm (5.5) is the honeycomb Ising model, critical at $\tanh K_c=1/\sqrt3$, that is $\zeta_c=\tfrac14\ln3\approx0.275$ [Stated]. Beyond $\zeta_c$ the loops are dilute, and for the analogous square-lattice deformation Castelnovo and Chamon find that the topological entropy vanishes there. Since (5.8) gives a perimeter law on both sides of $\zeta_c$, the equal-time Wilson loop does not see this transition.

## 11. Common misconceptions

**M1.** "The double semion differs from the toric code in its loops." Tempting because $\Phi_{\rm DS}=(-1)^N$. But $|\Phi_{\rm DS}|^2=|\Phi_{\rm TC}|^2$, so all diagonal correlators in the string basis agree, also after the dressing (5.4); they differ in off-diagonal operators, the sign $d_1^{|S|}$ of (5.2), and in the anyon spins (Week 7 (6.9)).

**M2.** "The anyons of a string net are its string types." Tempting because both are labelled by the input data. The $\mathbb{Z}_2$ input has two labels and four anyons, the Ising input three labels and nine: the anyons are those of the center of §7.

## 12. Historical note

Levin and Wen posted the paper in April 2004 (*Phys. Rev. B*, 2005), within Wen's program of reading gauge bosons and fermions as collective modes of spin models; the 2003 paper with Levin had found fermions at the ends of condensed strings. The 2004 paper turns the mechanism into a classification, in a physicist's language: a fixed-point wave function defined by graphical rules motivated by renormalization, consistency conditions (9) derived in App. B, the observation that the solutions are "tensor categories", with $6j$ symbols of groups giving gauge theories and those of quantum groups doubled Chern–Simons theories, honeycomb Hamiltonians, and quasiparticles as string operators solving their (22). Its examples are the two $\mathbb{Z}_2$ string nets (the double semion appearing as $U(1)\times U(1)$ Chern–Simons theory with $K={\rm diag}(2,-2)$), the Fibonacci model, and $\mathbb{Z}_3$ and $S_3$ models; the doubled Ising model of §7 is not among them.

## 13. What to take away

1. **Technical:** a string net is fixed by labels, branching rules and $F$-symbols obeying the pentagon; for $\mathbb{Z}_2$ a normalized $F$ has one entry, $f^2=1$. **Physical:** the $\mathbb{Z}_2$ string condensates are counted by the anomaly classes of Week 7.
2. **Technical:** on the plane the local rules fix $\Phi=d_1^N$ with $d_1=f$. **Physical:** the condensate superposes loops of every size with amplitudes that depend only on topology.
3. **Technical:** the plaquette term is a loop insertion followed by $F$-moves, with coefficient $d_1^{n_{\rm legs}/2}$, and (4.5) are commuting projectors with the loop gases as ground states. **Physical:** $B_p$ is a string kinetic energy, $Q_v$ Gauss's law, and the fixed point has no tension.
4. **Technical:** $\langle W\rangle=1$ (TC) and $d_1^{|S|}$ (DS) at the fixed point, (5.7)–(5.9) with a tension, $\mu=\Gamma^2/8$ for the perturbed toric code. **Physical:** the perimeter law counts virtual vison pairs straddling $C$, as in Sem I Week 5.
5. **Technical:** with $6j$ symbols a string net is lattice gauge theory; the Ising input gives nine anyons with $\mathcal D=4$ and $\Theta=1$. **Physical:** a gauge field and its charges emerge together, as a condensate and its boundaries, and the phases are non-chiral.

## 14. Looking ahead: Block 4

Week 12 builds the modified Villain formulation, in which $\mathbb{Z}_N$ gauge theory on the lattice is exactly the BF theory of [[sem2-week-02-zn-gauge-theory-as-bf-theory|Sem II Week 2]], with exact electric and magnetic 1-form symmetries (forward reference). Week 13 makes Kramers–Wannier duality a defect $D$ with $D\times D=1+\eta$, the fusion rule $\sigma\otimes\sigma=0\oplus\psi$ of §2.4, and Aasen, Mong and Fendley build the lattice defects with the $F$-symbols (2.5) (forward reference). Block 5 condenses anyons, as Problem 8⋆⋆ does, on the way to [[condensation-defects]].

## 15. Problem set

Problems 1–4 are the classroom core; 5⋆–7⋆ consolidate the self-study sections; 8⋆⋆–9⋆⋆ are research extensions.

### Core problems

**1. The Fibonacci pentagon** (extends §§2.2–2.4). Take labels $\{0,\tau\}$, $\tau\otimes\tau=0\oplus\tau$, and every admissible $F$ equal to 1 except $[F^{\tau\tau\tau}_\tau]=\begin{pmatrix}A&B\\C&E\end{pmatrix}$ in the basis $(0,\tau)$. (a) Evaluate (2.2) with $a=b=c=d=\tau$ for $(e;f,g,l,k)=(\tau;\tau,0,\tau,0)$, $(0;0,\tau,0,\tau)$ and $(0;0,\tau,\tau,\tau)$, and show $A=BC$, $A^2+BC=1$ and $B(A+E)=0$. (b) Solve with $B\neq0$. (c) In the gauge $B=C$, which solution is real, and what is $d_\tau$ by (2.6)? Compare with LW (50) and their unitarity condition (15).

**2. Strings on the square lattice** (extends §§3.3–3.4 and F3). The $\mathbb{Z}_2$ branching rule on the square lattice allows 0, 2 or 4 strings at a vertex. (a) At a vertex with four strings, show that the two non-crossing pairings of the strands differ by one reconnection. (b) Conclude that $d_1^N$ is well defined for $d_1=1$ and ambiguous by a sign for $d_1=-1$. (c) Split every vertex into two trivalent vertices joined by a new link, N and W links on one, S and E on the other; show that the branching rule fixes the new link, so every closed configuration lifts uniquely and $d_1^N$ is defined on the split lattice.

**3. Charges and fluxes of the $\mathbb{Z}_2$ string nets** (extends §4.3 and §6). (a) In $H^{\rm SN}_{\rm TC}$, show that $S(\gamma)=\prod_{\ell\in\gamma}Z_\ell$ along a path from $v$ to $v'\neq v$ commutes with every $B_p$ and with every $A_u$ except $A_v$, $A_{v'}$, and find the energy of $S(\gamma)|\Phi\rangle$ above the ground state. (b) Show that the product of $X_\ell$ over the links crossed by a dual path from $p$ to $p'$ commutes with all $A_v$ and all $B_q^1$ except $B_p^1$, $B_{p'}^1$, for both signs of $d_1$, and find its energy. (c) In the double semion let γ enter $\partial p$ through the leg $l_j$ and leave through $l_k$, its ends away from $p$; show that $B_p^1S(\gamma)=(-1)^{1-n_{l_j}-n_{l_k}}S(\gamma)B_p^1$ on closed configurations, and compute $\langle\Phi_{\rm DS}|S(\gamma)^\dagger B_pS(\gamma)|\Phi_{\rm DS}\rangle$.

**4. Free and bound visons** (extends §§5.1 and 5.3). (a) If each plaquette of $S$ carries a flux independently with probability ρ, show from (5.3) that $\langle W(C)\rangle=(1-2\rho)^{|S|}$. (b) If fluxes come only in pairs on the two plaquettes sharing a link, independently on each link with probability $\rho_2$, show that $\langle W(C)\rangle=(1-2\rho_2)^{|C|}$. (c) Identify $\rho_2$ in (5.10) and recover (5.11); then compute $\langle B_p^1\rangle$ in the electric vacuum, all $X_\ell=+1$, and place it in (a) or (b).

### Starred problems

**5⋆. The doubled Ising anyons** (extends §7). (a) Decompose $(\sigma,\bar\sigma)\otimes(\sigma,\bar\sigma)$ and check $d_{(\sigma,\bar\sigma)}^2$ against the dimensions of the products. (b) Verify (7.1) from Table 2 and compute Θ for the Ising theory alone. (c) Compute the monodromy $\theta_{X\otimes Y}/(\theta_X\theta_Y)$ of $X=(\psi,\bar\psi)$ with every $Y$. *Hint:* everything factorizes over the two layers; use the definitions of Sem II Week 10.

**6⋆. The double semion on the torus** (extends §§3.3, 4.3 and F2). (a) Draw a reconnection on the torus that leaves $N$ unchanged and conclude that $(-1)^N$ violates (3.1) in a class with odd winding. (b) Show that within a class the $N_p$ flips obey one relation, and that a joint eigenvector of all $B_p^1$ with eigenvalue $d_1$ exists, and is unique, exactly when $\prod_pB_p^1=d_1^{N_p}$ there. (c) Check $\prod_pB_p^1=+1$ in the trivial class of the $3\times4$ torus from (4.4). *Hint:* (a) uses the outside pairing excluded in §3.3; in (b) the flips form $\mathbb{Z}_2^{N_p-1}$, acting freely and transitively.

**7⋆. The perturbed toric code at second order** (extends §5.3). For $H=-\sum A_v-\sum B_p^1-\Gamma\sum X_\ell$, find the second-order amplitude of $X_{\ell''}|\Phi\rangle$ and show that $\mu=\Gamma^2/8+\Gamma^3/4+O(\Gamma^4)$; compare with the diagonalization of §5.3 and with (5.9) at $\zeta=\Gamma/2$. *Hint:* if ℓ, ℓ′, ℓ″ meet at $v$, then $X_\ell X_{\ell'}=A_vX_{\ell''}$; two vertices and two orderings each contribute $\Gamma^2/16$.

### ⋆⋆ problems

**8⋆⋆. Condensing $(\psi,\bar\psi)$ in the doubled Ising phase.** *Known:* Table 2; the condensation rules stated in Sem II Week 8 and the $\mathbb{Z}_N$ case of Sem II Week 10 (its Problem 9⋆⋆). *Sources:* those notes; Kitaev 2006 §§10–11. *Explored:* which anyons are confined, which identified, and how $(\sigma,\bar\sigma)$, fixed under fusion with $(\psi,\bar\psi)$, splits. *Completion:* the anyons of the condensed phase with $d$, θ and $S$, identified with the toric code ($\mathcal D=4\to2$), and the image of each surviving anyon of Table 2.

**9⋆⋆. The Fibonacci string net on the coronene.** *Known:* LW (11)–(15), App. C, the data (2.5) and LW (51)–(53). *Sources:* LW §§IV.B, VI.B, App. C. *Explored:* the operators $B_p^\tau$ built from six $F$-moves, on the admissible configurations of the coronene. *Completion:* a numerical verification that the $B_p$ are commuting projectors with a unique ground state on the patch, the amplitudes of one- and two-hexagon τ-loops expressed through $d_\tau=\phi$, and the torus degeneracy compared with the four anyons of the doubled Fibonacci phase.

## Self-study answer checkpoints

**Problem 1.** *Decisive step:* in the first label set the left side is $[F^{\tau\tau\tau}_\tau]_{0\tau}[F^{\tau\tau\tau}_\tau]_{\tau0}=BC$ and the right side has only $h=\tau$, giving $A$; in the second the left side is 1 and the right side sums $h=0,\tau$ to $A^2+BC$; in the third the left side vanishes, since $F^{0\tau\tau}_0$ needs $l=0$, and the right side is $AB+BE$. *Result:* $A^2+A-1=0$, so $A=\phi^{-1}$ or $-\phi$, with $E=-A$, $BC=A$; with $B=C$ the real solution is $A=\phi^{-1}$, $B=\phi^{-1/2}$, the matrix (2.5), and $d_\tau=\phi$; the other has $d=-\phi^{-1}$, LW's $\gamma_-$, excluded by (15). *Common failure:* taking $e=\tau$ in all three sets, which returns $A=BC$ three times.

**Problem 2.** *Decisive step:* the two resolutions are the two non-crossing pairings of four endpoints on a disc around the vertex, so the lemma of §3.3 gives $\Delta N=\pm1$. *Result:* the readings of $d_1^N$ differ by $d_1^{\pm1}$, which is 1 for the toric code and $-1$ for the double semion; on the split lattice $n_m\equiv n_N+n_W\equiv n_S+n_E$ mod 2, consistent because the four links have even total, and with four strings $n_m=0$ and the pairing is $(NW)(SE)$. *Common failure:* letting the strands cross at the vertex, where $N$ has no planar meaning.

**Problem 3.** *Decisive step:* $Z_\ell$ anticommutes with $A_u$ exactly when $u$ is an endpoint of ℓ, and interior vertices of γ meet two of its links; $X_\ell$ anticommutes with $B_q^1$ exactly when ℓ is an edge of $q$, and commutes with the diagonal leg factors. *Result:* (a) energy $+2$, two vertex projectors dropping to 0; (b) $+2$ for both $d_1$; (c) flipping both legs changes $n_{\rm legs}$ by $2-2(n_{l_j}+n_{l_k})$, so $c_p$ changes by $(-1)^{1-n_{l_j}-n_{l_k}}$; in the loop gas the two legs are independent fair bits, the phase averages to zero, and $\langle B_p\rangle=\tfrac12$: the bare string leaves plaquette excitations along γ. *Common failure:* treating the leg factor as a constant, which would make $S(\gamma)$ commute with $H_{\rm DS}$ away from its ends.

**Problem 4.** *Decisive step:* a pair on ℓ changes the parity of the fluxes in $S$ exactly when one of its plaquettes is in $S$, that is when $\ell\in C$. *Result:* (a) $(1-2\rho)^{|S|}$, an area law with $\sigma=-\ln(1-2\rho)$ per plaquette; (b) $(1-2\rho_2)^{|C|}$, a perimeter law with $\mu=-\ln(1-2\rho_2)=2\rho_2+O(\rho_2^2)$; (c) $\rho_2=(\Gamma/4)^2$, so $\mu=\Gamma^2/8$ as in (5.11); in the electric vacuum $\langle B_p^1\rangle=\langle\prod_{\partial p}Z\rangle=0$, case (a) with $\rho=\tfrac12$, and $\langle W(C)\rangle=0$: the strong-coupling end of Sem I Week 7 §5. *Common failure:* counting pairs with both plaquettes inside $S$, which do not change the parity.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester II Block 3. Written to the note-quality-template standard on 2026-10-02. Last revised 2026-10-03.*
