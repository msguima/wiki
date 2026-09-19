---
title: "Week 2 — The Lattice as a Cell Complex: Chains, Cochains, and Duality"
type: lecture-notes
course: syllabus
semester: 1
week: 2
block: A
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Linear algebra (kernels, images, quotients, adjoints); Week 1; comfort with finite abelian groups
modified: 2026-07-07
---

# Week 2 — The Lattice as a Cell Complex: Chains, Cochains, and Duality

> *This is the week the course stands on. Every duality we perform, every ground-state degeneracy we count, every anomaly we match, is an application of the finite linear algebra set up here. There is no point-set topology in it — only oriented cells, two matrices $\partial$ and $d$ obeying $\partial^2 = d^2 = 0$, and the bookkeeping that relates a lattice to its dual. We will compute the homology of a torus by hand, matrices displayed; prove the Hodge decomposition in eight lines; and meet the single intersection number whose operator avatar, in Semester II, is the ground-state degeneracy of topological matter. Learn it now; spend it all semester.*

## 0. Reading

**Primary:** these notes are self-contained. Second pass: the [[cochain-calculus-survival-kit|survival kit]] appendix, a lookup sheet distilled from this week.

**Secondary:**
- Nakahara, *Geometry, Topology and Physics*, 2nd ed., §§3.1–3.4, 6.1 — the continuum (manifold) story behind the lattice one, for students who want it.
- Gorantla, Lam, Seiberg, Shao, arXiv:2103.01257, appendices — the modern physics conventions for lattice cochains; [[courses/generalized-symmetries-course/conventions]] follows them.

**Optional research reading:** Chen & Tata, arXiv:2106.05274 — higher cup products on hypercubic lattices (used in Semester II Weeks 6–7).

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]].

## 1. Why we need this

Week 1 left two debts. We said a vortex "lives on a plaquette" and its charge is "the curl of θ," and we said Poisson resummation trades a field for a "dual-lattice" object. Both statements need a language in which *field*, *curl*, *plaquette*, and *dual lattice* are precise finite objects that a computation can grab. That language — the cell complex and its cochains — costs one lecture to build and pays interest every week for two semesters:

- Week 3: the vorticity is $dn$, an integer 2-cochain; the duality is Poisson resummation of a 1-cochain.
- Weeks 8–11: the monopole is $dn$, an integer 3-cochain; its dual-lattice geometry (point vs worldline) decides the phase diagram.
- Semester II: ground-state degeneracies are $|H^1(\Sigma,\mathbb{Z}_N)|$; anomalies are cup products; higher gauging is a sum over cocycles on a submanifold.

The pattern to hold on to: **a $p$-form field is a function on $p$-cells; the exterior derivative is a signed sum over a boundary; topology is the failure of "closed ⟹ exact"; duality is the dictionary between a lattice and its dual.** All four are matrices and index bookkeeping. None requires a limit.

## 2. Cells, chains, and the boundary operator

### 2.1 The cell complex and orientations

A hypercubic lattice $\Lambda \subset \mathbb{Z}^d$ is a **cell complex**: it consists of

- **0-cells** (sites), **1-cells** (links), **2-cells** (plaquettes), … , **$p$-cells** (elementary $p$-cubes).

Every cell carries a fixed **orientation**, chosen once and used forever: links point along $+\hat\mu$; the $p$-cell spanned by directions $\hat\mu_1 < \cdots < \hat\mu_p$ is oriented by that ordered tuple (for a plaquette in the 12-plane: counterclockwise when $\hat 1$ points right and $\hat 2$ up). On the torus $T^d$ we identify $x \sim x + L\hat\mu$, making the complex finite.

```
        ℓ_top
      x+ê2 ────→─── x+ê1+ê2
        │               │
  ℓ_left↑    P(x)       ↑ ℓ_right          all links oriented along +ê1, +ê2;
        │  (oriented    │                  plaquette oriented counterclockwise:
        x ────→─── x+ê1                    ∂P = ℓ_bot + ℓ_right − ℓ_top − ℓ_left
        ℓ_bot
```
**Figure 1. The oriented plaquette $P(x)$ and its boundary. Signs record whether a boundary link's own orientation agrees (+) or disagrees (−) with the counterclockwise traversal.**

### 2.2 Chains and $\partial$

A **$p$-chain** is a formal integer combination of oriented $p$-cells, $c = \sum_i n_i\sigma_i$; they form the free abelian group $C_p(\Lambda,\mathbb{Z})$. The **boundary operator** $\partial : C_p \to C_{p-1}$ assigns to each cell its oriented boundary:
$$
\partial\,(\text{link } x \to x{+}\hat\mu) = (x{+}\hat\mu) - x,
\qquad
\partial\, P(x) = \ell_{\rm bot} + \ell_{\rm right} - \ell_{\rm top} - \ell_{\rm left}
$$
(Figure 1), and in general with signs $(-1)^{\text{position}}$ dictated by the ordered-tuple orientation.

**The one identity everything rests on:** $\partial^2 = 0$. Check it on Figure 1, symbol by symbol [Proved for the plaquette; the general case is the same cancellation]:
$$
\partial(\partial P) = \big[(x{+}\hat1) - x\big] + \big[(x{+}\hat1{+}\hat2) - (x{+}\hat1)\big] - \big[(x{+}\hat1{+}\hat2) - (x{+}\hat2)\big] - \big[(x{+}\hat2) - x\big] = 0 .
$$
Each corner appears exactly twice, once with each sign. "The boundary of a boundary is empty."

## 3. Cochains and the coboundary operator

### 3.1 Cochains are fields

A **$p$-cochain** with coefficients in an abelian group $G$ is a $G$-valued function on oriented $p$-cells: $f \in C^p(\Lambda, G)$, with $f(-\sigma) = -f(\sigma)$ under orientation reversal. This is exactly what a physicist means by a **$p$-form field on the lattice**:

| cochain degree | field | examples in this course |
|---|---|---|
| 0 (sites) | scalar | $\theta_x$ (XY), heights $h$, dual photon $\sigma$ |
| 1 (links) | gauge field | $a_\ell$, the Villain integer $n_\ell$ (Week 3) |
| 2 (plaquettes) | field strength / 2-form | $(da)_P$, vorticity, $\mathbb{Z}_N$ backgrounds $B$ |
| 3 (cubes) | 3-form | monopole density $dn$ in gauge theory |

Coefficients used: $\mathbb{Z}$, $\mathbb{R}$, $U(1) = \mathbb{R}/2\pi\mathbb{Z}$, $\mathbb{Z}_N$. The **pairing** of a cochain with a chain,
$$
\langle f, c\rangle = \sum_i n_i\, f(\sigma_i)\quad\text{for } c = \sum_i n_i \sigma_i,
$$
is the lattice version of $\int_c f$.

### 3.2 The coboundary $d$: Stokes as a definition

Define $d : C^p \to C^{p+1}$ by declaring the **discrete Stokes theorem** to hold identically:
$$
\boxed{\ \langle df,\, c\rangle \;=\; \langle f,\, \partial c\rangle \quad \text{for all chains } c.\ }
$$
Unpacked: $(df)$ on a $(p{+}1)$-cell is the signed sum of $f$ over that cell's boundary. Concretely,
$$
(d\varphi)(x\to x{+}\hat\mu) = \varphi_{x+\hat\mu} - \varphi_x \quad(\text{gradient}),
\qquad
(da)\big(P(x)\big) = a_{\rm bot} + a_{\rm right} - a_{\rm top} - a_{\rm left} \quad(\text{curl / field strength}),
$$
and on 2-cochains, the signed sum over a cube's six faces (divergence of a 2-form). Because $\partial^2 = 0$,
$$
\langle d^2 f, c\rangle = \langle f, \partial^2 c\rangle = 0 \quad\text{for all } c
\qquad\Longrightarrow\qquad
\boxed{\ d^2 = 0.\ }
$$
"Curl of a gradient vanishes"; "divergence of a curl vanishes"; the Bianchi identity — all of them are this one line, and on the lattice they are *exact algebra*, not smooth-function theorems.

> **Physical picture.** The field strength $F = da$ of any lattice gauge field is automatically closed, $dF = 0$ — Bianchi with no equations of motion invoked. So where do magnetic monopoles come from? From compactness: when the gauge field is an angle, the honest field strength is $F = da - 2\pi n$ with an integer 2-cochain $n$ recording branch choices, and $dF = -2\pi\,dn$ need not vanish. The monopole density is literally $d^2$-of-a-multivalued-object — zero for a globally defined field, quantized and localized when the field is a chart. Weeks 8–11 are this sentence, unpacked with couplings attached.

### 3.3 The inner product and the codifferential

Give $C^p(\Lambda,\mathbb{R})$ the inner product $\langle f, g\rangle = \sum_{p\text{-cells}} f(\sigma) g(\sigma)$. The **codifferential** $\delta : C^p \to C^{p-1}$ is the adjoint of $d$:
$$
\langle \delta f,\, g\rangle = \langle f,\, dg\rangle \qquad \text{for all } g \in C^{p-1}.
$$
On a 1-cochain $m$, $(\delta m)_x = \sum_{\mu}\big(m_{(x-\hat\mu\to x)} - m_{(x\to x+\hat\mu)}\big)$ — the lattice (in-minus-out) divergence, up to the overall sign convention fixed in [[courses/generalized-symmetries-course/conventions]]. $\delta^2 = 0$ follows by adjointness. The **lattice Laplacian** is
$$
\Delta = \delta d + d\delta \quad(\text{on 0-cochains: the standard 5-point/7-point Laplacian}),
$$
and its kernel — the **harmonic cochains** — will turn out to be exactly the topology (§6).

## 4. Homology and cohomology, computed by hand

### 4.1 Definitions

- $f$ is **closed** if $df = 0$; **exact** if $f = dg$. Exact ⟹ closed (since $d^2 = 0$).
- **Cohomology:** $H^p(\Lambda, G) = \ker d\big|_{C^p} \,/\, \operatorname{im} d\big|_{C^{p-1}}$ — closed modulo exact.
- **Homology:** $H_p(\Lambda, G) = \ker\partial\big|_{C_p} \,/\, \operatorname{im}\partial\big|_{C_{p+1}}$ — cycles modulo boundaries.

$H^p$ measures *global* field configurations: closed fields that are not the coboundary of anything — invisible to all local data, detectable only by integrating around non-contractible cycles.

> **Physical picture.** In gauge-theory words: exact = pure gauge ($a = d\lambda$), closed = flat ($da = 0$), and $H^1$ = flat-but-not-pure-gauge = the physically distinct Wilson-line holonomies around non-contractible loops. On a torus these are the moduli that label degenerate ground states of a topological phase (Semester II Week 2). Cohomology is not an abstraction bolted onto the physics; it is the *count of vacua*, and this week's central skill is computing it.

### 4.2 The 2×2 torus, matrices displayed [Computed.]

We compute $H_\bullet(T^2, \mathbb{Z})$ on the smallest nontrivial lattice: the $2\times2$ periodic square lattice. Cells: 4 sites $s_{ij}$, 8 links (4 $x$-links $\ell^x_{ij}$, 4 $y$-links $\ell^y_{ij}$), 4 plaquettes $P_{ij}$, indices $i,j \in \{0,1\}$ mod 2.

**The matrix $\partial_1$** (8 columns = links, 4 rows = sites $s_{00}, s_{10}, s_{01}, s_{11}$), from $\partial\ell^x_{ij} = s_{i+1,j} - s_{ij}$, $\partial\ell^y_{ij} = s_{i,j+1} - s_{ij}$:

$$
\partial_1 = \begin{pmatrix}
 & \ell^x_{00} & \ell^x_{10} & \ell^x_{01} & \ell^x_{11} & \ell^y_{00} & \ell^y_{10} & \ell^y_{01} & \ell^y_{11}\\
s_{00} & -1 & +1 & 0 & 0 & -1 & 0 & +1 & 0\\
s_{10} & +1 & -1 & 0 & 0 & 0 & -1 & 0 & +1\\
s_{01} & 0 & 0 & -1 & +1 & +1 & 0 & -1 & 0\\
s_{11} & 0 & 0 & +1 & -1 & 0 & +1 & 0 & -1
\end{pmatrix}
$$

Each column sums to zero (every link has one head, one tail), so $\operatorname{rank}\partial_1 \le 3$; and the three columns $\ell^x_{00}, \ell^y_{00}, \ell^y_{10}$ are visibly independent, so
$$
\operatorname{rank}\partial_1 = 3,\qquad
H_0 = C_0/\operatorname{im}\partial_1 = \mathbb{Z}^4/\mathbb{Z}^3 = \mathbb{Z}
$$
— one connected component, as it must be. ($\operatorname{im}\partial_1$ = all site chains with total coefficient zero.)

**The matrix $\partial_2$** (4 columns = plaquettes, 8 rows = links), from $\partial P_{ij} = \ell^x_{ij} + \ell^y_{i+1,j} - \ell^x_{i,j+1} - \ell^y_{ij}$:

$$
\partial_2 = \begin{pmatrix}
 & P_{00} & P_{10} & P_{01} & P_{11}\\
\ell^x_{00} & +1 & 0 & -1 & 0\\
\ell^x_{10} & 0 & +1 & 0 & -1\\
\ell^x_{01} & -1 & 0 & +1 & 0\\
\ell^x_{11} & 0 & -1 & 0 & +1\\
\ell^y_{00} & -1 & +1 & 0 & 0\\
\ell^y_{10} & +1 & -1 & 0 & 0\\
\ell^y_{01} & 0 & 0 & -1 & +1\\
\ell^y_{11} & 0 & 0 & +1 & -1
\end{pmatrix}
$$

**Kernel of $\partial_2$:** a combination $\sum c_{ij}P_{ij}$ has zero boundary iff (row $\ell^x_{00}$) $c_{00} = c_{01}$, (row $\ell^x_{10}$) $c_{10} = c_{11}$, (row $\ell^y_{00}$) $c_{00} = c_{10}$, (row $\ell^y_{01}$) $c_{01} = c_{11}$ — i.e. all $c_{ij}$ equal. So
$$
\ker\partial_2 = \mathbb{Z}\cdot\big(P_{00}{+}P_{10}{+}P_{01}{+}P_{11}\big),\qquad
H_2 = \ker\partial_2 = \mathbb{Z},
\qquad \operatorname{rank}\partial_2 = 4 - 1 = 3.
$$
The generator of $H_2$ is the whole surface — the "volume cycle" of the torus.

**$H_1$, the interesting one:**
$$
\dim\ker\partial_1 = 8 - \operatorname{rank}\partial_1 = 5,\qquad
\operatorname{rank}\operatorname{im}\partial_2 = 3
\qquad\Longrightarrow\qquad
H_1 \cong \mathbb{Z}^{5-3} = \mathbb{Z}^2 \quad(\text{no torsion; see below}).
$$
Explicit generators of the kernel: the two **winding loops**
$$
A = \ell^x_{00} + \ell^x_{10}\ (\text{around the } x\text{-direction}),\qquad
B = \ell^y_{00} + \ell^y_{01}\ (\text{around } y),
$$
plus three plaquette boundaries $\partial P_{00}, \partial P_{10}, \partial P_{01}$. Modding out the boundaries leaves exactly $A$ and $B$:
$$
\boxed{\ H_1(T^2,\mathbb{Z}) = \mathbb{Z}\,[A] \oplus \mathbb{Z}\,[B].\ }
$$

**Torsion, systematically.** The complete algorithm is the **Smith normal form**: any integer matrix $M$ can be brought to $\mathrm{diag}(d_1, d_2, \ldots, 0, \ldots)$ with $d_1 \mid d_2 \mid \cdots$ (the invariant factors) by invertible integer row/column operations, and
$$
H_p \;\cong\; \mathbb{Z}^{\,n_p - r_p - r_{p+1}}\ \oplus\ \bigoplus_i \mathbb{Z}_{d_i^{(p+1)}}\quad(\text{over the invariant factors } d_i > 1 \text{ of } \partial_{p+1}),
$$
with $n_p$ the number of $p$-cells and $r_p = \operatorname{rank}\partial_p$.

**The reduction, performed.** Run it on $\partial_2$ above; integer row/column operations only. Use column $P_{00}$ and its $+1$ in row $\ell^x_{00}$ as the first pivot: clear that row's other entry by the column operation $P_{01} \to P_{01} + P_{00}$, then clear column $P_{00}$'s remaining entries by row operations ($\ell^x_{01} \to \ell^x_{01} + \ell^x_{00}$, $\ell^y_{00} \to \ell^y_{00} + \ell^x_{00}$, $\ell^y_{10} \to \ell^y_{10} - \ell^x_{00}$). The first row and column are now $(1, 0, 0, 0)$. Repeat with the $+1$ of the reduced $P_{10}$ column (row $\ell^x_{10}$), then with the reduced $P_{01}$ column (its surviving $\pm1$, e.g. in the modified $\ell^y_{01}$ row). After three pivots — each with pivot entry $\pm1$, so each invariant factor is 1 — the fourth column has been emptied by the relation $P_{00} + P_{10} + P_{01} + P_{11} \mapsto 0$:
$$
\mathrm{SNF}(\partial_2) = \mathrm{diag}(1, 1, 1, 0),
\qquad\text{and identically}\qquad
\mathrm{SNF}(\partial_1) = \mathrm{diag}(1, 1, 1, 0).
$$
Feed the formula: $H_1 = \mathbb{Z}^{\,8 - 3 - 3} \oplus (\text{nothing, since all } d_i = 1) = \mathbb{Z}^2$, confirming the constructive computation. The algorithm is fully mechanical — this is the sense in which "computing the topology" is something one can hand to a computer algebra system, and the invariant factors are where any torsion would have announced itself.

> **Physical picture.** What did the matrices just compute? $\ker\partial_1$ is the space of conserved currents on this lattice; $\operatorname{im}\partial_2$ is the subspace realizable as local eddies (plaquette circulations). The quotient — two surviving generators — says: *on a torus there are exactly two ways for current to flow that no arrangement of local eddies can produce*, the two global circulations. A superconducting loop's persistent current modes, the winding sectors of Week 3, the flux sectors of a gauge theory on $T^2$: all are this quotient, computed once here with integer row reduction. When a topological-order paper says "the ground-state degeneracy is $|H_1(\Sigma,\mathbb{Z}_N)|$," this small linear algebra is the entire geometric content.

For our matrices all invariant factors equal 1, so no torsion appears — as befits the torus. A space where torsion *does* appear is the Klein bottle, $H_1(K,\mathbb{Z}) = \mathbb{Z}\oplus\mathbb{Z}_2$: Problem 4 has you produce the invariant factor 2 by the same algorithm. Torsion is not exotica: $\mathbb{Z}_N$ gauge theories live on exactly this kind of arithmetic.

### 4.3 The general torus, the fast way [Computed.]

For $H^p(T^d)$ at any size, use the **minimal cell structure**: one $d$-cube with opposite faces identified. It has exactly $\binom{d}{p}$ $p$-cells (one per choice of $p$ directions), and *every* boundary map vanishes — each cell's boundary cancels in pairs under the identification (exactly the mechanism seen in $\partial P$ summing to zero... for the $1\times1$ torus: $\partial\ell = x - x = 0$, $\partial P = \ell^x + \ell^y - \ell^x - \ell^y = 0$). With $\partial = 0$ and $d = 0$, homology = chains and cohomology = cochains:
$$
\boxed{\ H^p(T^d, G) \;\cong\; G^{\binom{d}{p}},\qquad b_p = \binom{d}{p}.\ }
$$

| | $b_0$ | $b_1$ | $b_2$ | $b_3$ | $b_4$ |
|---|---|---|---|---|---|
| $T^2$ | 1 | 2 | 1 | — | — |
| $T^3$ | 1 | 3 | 3 | 1 | — |
| $T^4$ | 1 | 4 | 6 | 4 | 1 |

With $G = \mathbb{Z}_N$: $H^1(T^d,\mathbb{Z}_N) = \mathbb{Z}_N^{\,d}$, the counting that becomes $\mathrm{GSD} = N^{2g}$ for $\mathbb{Z}_N$ gauge theory on a genus-$g$ surface (Semester II Week 2), and $H^2(T^4,\mathbb{Z}_N) = \mathbb{Z}_N^6$, the space of 't Hooft-flux backgrounds in Semester II Week 6.

**Why the fine $2\times2$ answer and the minimal answer agree** [Sketched.]: homology is a homotopy invariant — refining a cell decomposition does not change it. The mechanism, without the machinery: subdividing a cell adds equal numbers of new generators and new relations (each new face is killed by a new boundary), so kernels-mod-images are unchanged; the formal proof organizes this bookkeeping into chain homotopies, which we state and do not need [named gap; Nakahara §3.3]. Operationally: **compute on the coarsest complex available; put fields on the finest.**

## 5. The dual lattice

### 5.1 Construction and the degree flip

The **dual lattice** $\Lambda^*$ places a site at the center of each $d$-cell of $\Lambda$; in general,
$$
p\text{-cell of }\Lambda \ \longleftrightarrow\ (d{-}p)\text{-cell of }\Lambda^* \quad(\text{the unique dual cell it pierces}).
$$

```
    +-------+-------+          Λ : sites +, links —— , plaquettes (squares)
    |       |       |          Λ*: sites ·  (at plaquette centers),
    |   ·   |   ·   |               dual links (vertical/horizontal thru Λ-links)
    |       |       |
    +-------+-------+          In d=2:  site ↔ dual plaquette,
    |       |       |                   link ↔ dual link (rotated 90°),
    |   ·   |   ·   |                   plaquette ↔ dual site.
    |       |       |
    +-------+-------+
```
**Figure 2. Direct and dual lattices in $d=2$. Every object of degree $p$ has a shadow of degree $d-p$.**

In $d=3$: sites↔cubes, links↔plaquettes, plaquettes↔links, cubes↔sites. In $d=4$: plaquettes↔plaquettes — degree 2 is **self-dual**, the structural reason electric–magnetic duality is special to four dimensions ([[week-08-dual-variables-abelian-gauge|Week 8]]).

### 5.2 $\delta = \pm\star d\,\star$, verified in $d=2$ [Computed.]

Define $\star : C^p(\Lambda) \to C^{d-p}(\Lambda^*)$ by transporting values to dual cells, $(\star m)(\sigma^*) = m(\sigma)$, with orientations fixed by rotating $+90°$ in $d=2$ (general signs in [[courses/generalized-symmetries-course/conventions]]). Claim: the divergence $\delta$ on $\Lambda$ is the curl $d$ on $\Lambda^*$, up to sign. Check at a site $x$ with its four links; the dual plaquette $x^*$ surrounds $x$, and its boundary consists of the four dual links crossing those four links:
$$
(d\,\star m)(x^*) = \star m\big(\text{4 dual links, oriented ccw}\big)
= m(\ell_{x,\rm in}^{(1)}) + m(\ell^{(2)}_{x,\rm in}) - m(\ell^{(1)}_{x,\rm out}) - m(\ell^{(2)}_{x,\rm out})
= -(\delta m)_x,
$$
matching the in-minus-out divergence of §3.3 up to the promised sign. One picture is worth the index chase: **rotating a vector field by 90° turns its divergence into a curl** — the lattice version of that freshman fact, and the entire content of "$\delta = \pm\star d\star$."

### 5.3 Poincaré duality

$$
\boxed{\ H^p(T^d, G) \;\cong\; H_{d-p}(T^d, G).\ }
$$
A closed $p$-cochain on $\Lambda$ *is* a $(d{-}p)$-cycle on $\Lambda^*$ (transport by $\star$; closedness becomes cycle-ness by §5.2). Check against §4: $H^1(T^2) = \mathbb{Z}^2 = H_1(T^2)$ ✓. The physical payoff is the **defect-geometry flip**: a defect defined by a $(p{+}1)$-cochain equation $dn \ne 0$ *lives on* a $(d{-}p{-}1)$-cycle of the dual lattice:

| object | cochain eq. | $d=2$ | $d=3$ | $d=4$ |
|---|---|---|---|---|
| vortex of a compact scalar | $v = dn,\ n \in C^1$ | point | line | sheet |
| monopole of a compact gauge field | $m = dn,\ n \in C^2$ | — | **point** (instanton) | **worldline** |

The boxed row of Block C: the same equation $dn$, read in $d=3$ vs $d=4$, gives Polyakov's instanton plasma vs the dual superconductor's loop condensate. Geometry, not dynamics, makes them different problems.

## 6. Hodge theory: harmonic = topological [Proved.]

**Theorem (discrete Hodge decomposition).** *On a finite complex, with the inner product of §3.3,*
$$
C^p \;=\; \operatorname{im} d \ \oplus\ \operatorname{im}\delta\ \oplus\ \mathcal{H}^p,
\qquad
\mathcal{H}^p \equiv \ker\Delta\big|_{C^p} = \{h : dh = 0 \text{ and } \delta h = 0\},
$$
*orthogonal direct sum, and $\mathcal{H}^p \cong H^p(\Lambda,\mathbb{R})$; in particular $\dim\ker\Delta|_{C^p} = b_p$.*

**Proof.** (i) *Orthogonality:* $\langle d\alpha, \delta\beta\rangle = \langle d(d\alpha), \beta\rangle = 0$ by $d^2 = 0$ and adjointness. (ii) *Harmonic ⟺ closed and co-closed:* $\langle h, \Delta h\rangle = \langle h, \delta d h\rangle + \langle h, d\delta h\rangle = \|dh\|^2 + \|\delta h\|^2$, so $\Delta h = 0$ iff both vanish. (iii) *The complement:* $h \perp \operatorname{im} d \iff \langle h, d\alpha\rangle = \langle \delta h, \alpha\rangle = 0\ \forall\alpha \iff \delta h = 0$; likewise $h \perp \operatorname{im}\delta \iff dh = 0$. So $(\operatorname{im} d \oplus \operatorname{im}\delta)^\perp = \mathcal{H}^p$, giving the decomposition (finite dimensions: orthogonal complement always splits). (iv) *Harmonics compute cohomology:* let $f$ be closed and decompose $f = d\alpha + \delta\beta + h$. Then $0 = df = d\delta\beta$, so $0 = \langle d\delta\beta, \beta\rangle = \|\delta\beta\|^2$ and the coexact piece vanishes: every closed $f$ is (exact) + (harmonic), and the harmonic part is unique in its class ($h - h' = d\alpha$ with both harmonic ⟹ $\|d\alpha\|^2 = \langle h - h', d\alpha\rangle = \langle \delta(h-h'), \alpha\rangle = 0$). Hence $\mathcal{H}^p \cong H^p$. $\square$

**Worked: the harmonic 1-cochains of $T^2$** [Computed.] Take $h^{(x)}$ = value 1 on every $x$-link, 0 on every $y$-link. Then $(dh^{(x)})(P) = 1 + 0 - 1 - 0 = 0$ on every plaquette (Figure 1's signs), and $(\delta h^{(x)})_x = 1 - 1 = 0$ at every site (one incoming, one outgoing $x$-link). Harmonic. Likewise $h^{(y)}$. These two span $\mathcal{H}^1$: $\dim = b_1 = 2$ ✓ — the two "constant winds" around the torus, the zero modes of the Laplacian, the flat connections. Topology as the kernel of a matrix you can diagonalize.

> **Physical picture.** Hodge is the statement that *every field configuration splits into gauge junk + local physics + topology*: $f = d\alpha$ (pure gauge / gradient part) $+\ \delta\beta$ (the part sourced by local currents) $+\ h$ (the finitely many global modes no local operation reaches). In Week 3 exactly this split separates spin waves ($\delta\beta$-type fluctuations) from winding sectors ($h$) and lets the vortices be counted cleanly; the zero mode that enforces charge neutrality in the Coulomb gas is the $b_0 = 1$ harmonic constant on the dual lattice. When a numerical collaborator says "we fix the zero modes," this decomposition is what they are fixing.

## 7. Poisson resummation on cochains: the duality engine

### 7.1 The identity, proved [Model proof.]

**Claim:** for $f$ Schwartz (rapid decay suffices),
$$
\sum_{n\in\mathbb{Z}} f(n) = \sum_{w\in\mathbb{Z}}\int_{-\infty}^{\infty} dx\, f(x)\, e^{2\pi i w x}.
$$
**Proof.** The Dirac comb $\Sha(x) = \sum_n \delta(x - n)$ is periodic with period 1, so it has a Fourier series $\Sha(x) = \sum_w c_w e^{2\pi i w x}$ with
$$
c_w = \int_0^1 \Sha(x)\, e^{-2\pi i w x}\, dx = e^{-2\pi i w\cdot 0} = 1
$$
(exactly one delta, at $x = 0$, sits in the fundamental domain). Hence $\Sha = \sum_w e^{2\pi i w x}$ as tempered distributions, and integrating $f$ against both sides gives the claim; Schwartz decay justifies the interchanges [named gap: distributional convergence, standard]. $\square$

The Gaussian case was *derived independently* in Week 1 §6 by the method of images — same identity, mechanism attached.

### 7.2 The recipe (memorize)

Every abelian duality in this course is the following four moves, applied to an integer cochain (the engine fires in [[week-03-villain-form-xy-duality|Week 3]], [[week-08-dual-variables-abelian-gauge|Week 8]], and — made exact — in Semester II Week 12):

1. **Villain form:** write the compact theory with an explicit integer $p$-cochain $n$.
2. **Poisson-resum** $n$ (one comb per cell): a dual integer variable appears, one per *dual* $(d{-}p)$-cell.
3. **Integrate the original field:** it now appears linearly; integrating it out imposes a **constraint** (current conservation, $\delta(\cdot) = 0$) on the dual variable.
4. **Solve the constraint** with the toolkit of this week: Hodge-decompose; the co-closed variable is $d$(dual potential) up to harmonic sectors, *except* at defects, which remain as the sources of the dual theory.

Steps 3–4 are where §§5–6 earn their keep: "solve $\delta m = 0$" *means* "apply Hodge on the dual lattice and keep track of $b_p$ harmonic pieces."

## 8. The intersection pairing: one integer, seed of a Hilbert space

On $T^2$, the two homology generators $A$ (the $x$-winding loop) and $B$ (the $y$-winding loop) intersect once:
$$
A\cdot A = 0,\qquad B\cdot B = 0,\qquad A\cdot B = 1 .
$$

```
            ┌──────────────┐
            │      B ↑     │        A : loop winding in x
            │        │     │        B : loop winding in y
       A ───┼────────╳─────┼───→    ╳ : the single intersection,
            │        │     │             A·B = 1
            │        │     │
            └──────────────┘        (opposite edges identified)
```
**Figure 3. The intersection form of the torus. This single "+1" is the origin of the clock–shift algebra.**

Signed intersection counting extends to a bilinear pairing $H_p \times H_{d-p} \to \mathbb{Z}$ (or $\mathbb{Z}_N$) on any $T^d$; it is the homological face of the linking of operators in spacetime. **Preview of its operator life** [Heuristic here; derived in Semester II Week 2]: in $\mathbb{Z}_N$ gauge theory, let $Z$ = the operator measuring the holonomy along $A$, and $X$ = the operator that shifts that holonomy (equivalently, measures/creates flux along $B$). Because $B$ must cross $A$ exactly once to close, reordering the two operations differs by one unit of $\mathbb{Z}_N$ phase:
$$
Z\,X = \omega\, X\, Z,\qquad \omega = e^{2\pi i/N}.
$$
This clock–shift algebra has a unique irreducible representation, of dimension $N$. Proof in three lines [Proved]: $Z$ is unitary with $Z^N = 1$, so its eigenvalues are $N$-th roots of unity; the relation $ZX = \omega XZ$ says $X$ maps the $\lambda$-eigenspace of $Z$ to the $\omega\lambda$-eigenspace, cyclically permuting all $N$ eigenvalues; so every eigenvalue appears with equal multiplicity, and irreducibility forces multiplicity one — dimension exactly $N$. Any theory realizing the algebra on its ground states therefore has $N$-fold degeneracy per conjugate cycle pair.

On a **genus-$g$ surface** the intersection form has a symplectic normal form: $2g$ cycle generators $A_1, B_1, \ldots, A_g, B_g$ with $A_i\cdot B_j = \delta_{ij}$ and all other intersections zero. Now count operators in a $\mathbb{Z}_N$ gauge theory, which carries **two species** of loop operator — electric (Wilson) and magnetic (dual/'t Hooft) lines, both wrappable on any cycle. The pairs (electric on $A_i$, magnetic on $B_i$) and (electric on $B_i$, magnetic on $A_i$) each realize one clock–shift algebra, they mutually commute (their cycles either coincide in species or intersect evenly), and no other independent pair exists: **two algebras per handle**, hence ground-state dimension $N^2$ per handle,
$$
\mathrm{GSD} = N^{2g}.
$$
Two assumptions entered that count, and both are theory-dependent: that the ground-state algebra is *generated* by the two loop species, and that no relation collapses it — both established for $\mathbb{Z}_N$ gauge theory in its deconfined phase in Semester II Week 2, where the operators are constructed. The homological input — the symplectic basis and one "+1" per handle — is complete here. That is topological order's ground-state count, and its entire kinematic origin is Figure 3.

## 9. Cup product: a first meeting [Computed for the low-degree case.]

Semester II needs one more product: the **cup product** $\cup : C^p \times C^q \to C^{p+q}$, the lattice wedge. The full hypercubic definition is Chen–Tata's ([[courses/generalized-symmetries-course/conventions]] §5); here is the flavor in low degree, enough to compute with. For a 0-cochain $f$ and 1-cochain $\beta$:
$$
(f\cup\beta)(\ell_{x\to y}) = f(x)\,\beta(\ell),
\qquad
(\beta\cup f)(\ell_{x\to y}) = \beta(\ell)\, f(y)
$$
("front value" vs "back value"), and for two 1-cochains on the plaquette $P(x)$ of Figure 1:
$$
(\alpha\cup\beta)\big(P(x)\big) = \alpha\big(\ell^x_{\,x}\big)\,\beta\big(\ell^y_{\,x+\hat1}\big)
$$
(the "lower-left path / upper-right path" split). The general hypercubic rule for two 1-cochains in any $d$, needed in Semester II, is the **same single term** on each plaquette: for $\mu < \nu$,
$$
(\alpha\cup\beta)\big(P_{\mu\nu}(x)\big) = \alpha\big(\ell_\mu(x)\big)\,\beta\big(\ell_\nu(x{+}\hat\mu)\big)
$$
— "first factor on the early leg of the lower path, second on the late leg." **No antisymmetrization**: the cup product is genuinely not graded-commutative on the lattice, and that is a feature (below). For slowly varying fields, the antisymmetric part $\tfrac12(\alpha\cup\beta - \beta\cup\alpha)$ reproduces the continuum wedge $\alpha\wedge\beta$, while the symmetric part is a lattice artifact that a $d$-exact term absorbs — continuum limits see the wedge, exact lattice identities need the full cup. Two facts, verifiable directly from these formulas:

**Leibniz** [Computed for $(f,\beta)$]: the claim is $d(f\cup\beta) = df\cup\beta + f\cup d\beta$ on the plaquette $P(x)$ of Figure 1. Write out both sides with the tail (front-value) rule. Left side — the boundary sum of $(f\cup\beta)(\ell) = f(\mathrm{tail}(\ell))\,\beta(\ell)$, with Figure 1's signs and tails ($\ell_{\rm bot}, \ell_{\rm right}, \ell_{\rm top}, \ell_{\rm left}$ have tails $x,\, x{+}\hat1,\, x{+}\hat2,\, x$):
$$
d(f\cup\beta)(P) = f(x)\beta_{\rm bot} + f(x{+}\hat1)\beta_{\rm right} - f(x{+}\hat2)\beta_{\rm top} - f(x)\beta_{\rm left}.
$$
Right side — first term $(df\cup\beta)(P) = df(\ell^x_{\,x})\,\beta(\ell^y_{\,x+\hat1}) = \big[f(x{+}\hat1) - f(x)\big]\beta_{\rm right}$; second term $(f\cup d\beta)(P) = f(x)\,(d\beta)(P) = f(x)\big[\beta_{\rm bot} + \beta_{\rm right} - \beta_{\rm top} - \beta_{\rm left}\big]$. Sum:
$$
f(x{+}\hat1)\beta_{\rm right} + f(x)\beta_{\rm bot} - f(x)\beta_{\rm top} - f(x)\beta_{\rm left}.
$$
Comparing term by term, seven of the eight entries match; the mismatch is confined to the top link, $\big[f(x) - f(x{+}\hat2)\big]\beta_{\rm top}$. **Read the failure correctly:** it does not mean lattice products cannot obey Leibniz — it means our simplified leg-pairing above is not yet a consistent cup product. The full cubical conventions (Chen–Tata; adopted in [[courses/generalized-symmetries-course/conventions]] §5) assign the evaluation vertices of the $0\!\cup\!1$ and $1\!\cup\!1$ products so that these eight terms cancel *exactly*, and Leibniz $d(\alpha\cup\beta) = d\alpha\cup\beta + (-1)^p\,\alpha\cup d\beta$ holds on the nose [Stated — refs: Chen–Tata §2]. The computation above is retained deliberately as the cautionary exhibit: **on the lattice, evaluation-vertex conventions are load-bearing — one careless leg choice breaks a product rule by a boundary term.** (Where genuinely irreducible corrections *do* appear is graded commutativity, next paragraph: there the leftover is the higher cup $\cup_1$, and no convention removes it.) [Computed — the eight-term bookkeeping above; Problem 5(a) runs the same audit for two 1-cochains under the full conventions.]

**Non-commutativity is physical:**
$$
(f\cup\beta - \beta\cup f)(\ell_{x\to y}) = \big(f(x) - f(y)\big)\beta(\ell) = -(df\cup_{\phantom{1}}\!\beta)\text{-type term},
$$
i.e. the failure to commute is a *coboundary-controlled* term (in general: $\alpha\cup\beta - (-1)^{pq}\beta\cup\alpha = \pm\, d(\alpha\cup_1\beta) \pm \cdots$ with the higher cup product $\cup_1$ [Stated — refs: Chen–Tata]). On the lattice, "forms don't quite commute" is not a defect of the discretization: that controlled non-commutativity *carries the 't Hooft anomalies* of Semester II Week 6 (the Pontryagin square $\mathcal{P}(B)$ is built exactly from $B\cup B$ and $B\cup_1 dB$). Do not "simplify" cup products by pretending they commute; the physics lives in the correction.

## 10. Subtleties and fine print

**F1 — Orientations are chosen once, then never renegotiated.** Every sign in $\partial$, $d$, $\delta$, $\star$, and $\cup$ descends from the single global orientation convention of §2.1. Mid-calculation re-derivations of signs are the leading cause of "duality off by a sign" errors; the professional habit is to fix conventions (ours: [[courses/generalized-symmetries-course/conventions]] §§1–2, following Gorantla–Lam–Seiberg–Shao) and *transport* signs, never re-decide them.

**F2 — Coarse for topology, fine for fields.** Homology is homotopy-invariant (§4.3), so compute it on the minimal complex; but *fields* (cochains with actions) live on the fine lattice, where entropy and local dynamics reside. The two-lattice discipline — count global sectors coarsely, integrate fluctuations finely — is exactly how Week 3 separates winding sectors from spin waves.

**F3 — Torsion exists, and $\mathbb{Z}_N$ physics feels it.** On $T^d$ all homology is free, but on non-orientable or twisted spaces invariant factors $> 1$ appear ($H_1(\text{Klein}) = \mathbb{Z}\oplus\mathbb{Z}_2$, Problem 4). Then coefficients matter: $H^p(X,\mathbb{Z}_N)$ is *not* just "$b_p$ copies of $\mathbb{Z}_N$" — torsion contributes extra pieces (universal-coefficient bookkeeping [Stated — refs: Nakahara §3.4]). $\mathbb{Z}_N$ gauge theories on such spaces have ground-state counts sensitive to this arithmetic; on tori we are safe, and we will say so whenever we use it.

**F4 — The dual lattice is a different complex, not a shifted copy.** Objects do not "also live" on $\Lambda^*$; they live on $\Lambda$ *or* on $\Lambda^*$, and $\star$ is a map, with orientation content (§5.2's sign), between the two. Monopoles are dual-lattice objects, full stop; drawing both lattices (Figure 2) before any duality computation prevents the most common category error in this subject.

**F5 — Boundary conditions are part of the complex.** Everything above assumed the torus. Open boundaries change $H_\bullet$ (relative homology enters), and physical statements like "neutrality is enforced by the zero mode" depend on it. The course works on $T^d$ by default precisely to keep the harmonic bookkeeping clean; when a result depends on that choice we flag it.

**F6 — Cohomology with compact coefficients has its own integers.** A $U(1)$-valued cochain is not an $\mathbb{R}$-valued one: closedness mod $2\pi$, not closedness, is the gauge-invariant statement, and the integer "branch sheets" ($n$ in the Villain form) are exactly the difference. The clean formalization — $U(1) \cong \mathbb{R}/2\pi\mathbb{Z}$ cochains ↔ pairs $(\mathbb{R}\text{-cochain}, \mathbb{Z}\text{-cochain})$ — *is* the Villain substitution of Week 3.

## 11. Common misconceptions

- **"$d$ is a finite-difference approximation to the continuum derivative."** No: on the lattice, $d$, $\partial^2 = 0$, Stokes, and Bianchi are *exact*. The continuum is the limit of the lattice here, not the other way around; nothing this week has discretization error.
- **"Homology depends on which lattice/triangulation you chose."** It does not (§4.3) — that invariance is precisely why it deserves the name *topology* and why the $2\times2$ computation of §4.2 already gives the answer for every size.
- **"The dual lattice is just the original shifted by half a lattice spacing."** Its *sites* are; the structure is not — degrees flip ($p \leftrightarrow d{-}p$), orientations transform, and divergences become curls (§5.2). Treating $\Lambda^*$ as a shifted $\Lambda$ collapses the distinction that makes electric–magnetic duality nontrivial.

## 12. What to take away

1. **Fields are cochains; $d$ is Stokes-by-definition; $d^2 = 0$ is Bianchi.** Gradient, curl, and divergence are one operator in three degrees, exactly, with no continuum limit taken.
2. **Topology is finite linear algebra.** $H_\bullet(T^2)$ computed from two displayed integer matrices; $H^p(T^d, G) = G^{\binom{d}{p}}$ from the minimal complex; Smith normal form as the general algorithm, torsion included.
3. **Hodge splits every field into gauge + local + global** [Proved], and the global (harmonic) part has dimension $b_p$ — topology as the kernel of a Laplacian. This split is the anatomy of every duality ahead.
4. **The dual lattice flips degree,** turning defect equations $dn \ne 0$ into points, lines, or sheets depending on $d$ — the single fact that organizes Block C.
5. **One intersection number ($A\cdot B = 1$) seeds the clock–shift algebra** and hence the ground-state degeneracy of topological order; the cup product's controlled non-commutativity will carry the anomalies. The kinematics of Semester II is already on this page.

## 13. Looking ahead: Week 3

The engine is assembled: Villain form (integer cochains), Poisson resummation (proved), Hodge (proved), dual lattice (built). Week 3 fires it at the 2d XY model and carries the José–Kadanoff–Kirkpatrick–Nelson duality through with every constant on the page: the exact rewriting into a height model, the second resummation producing spin waves and vortex charges, the zero mode enforcing neutrality, the lattice Green function constant of Week 1 becoming the vortex fugacity — ending at the Coulomb gas whose unbinding, in Week 4, is BKT.

## 14. Problem set

**Core problems** (everyone).

**1. Boundary matrices on $T^2$, size $3\times3$.**
Repeat §4.2 on the $3\times3$ torus far enough to confirm $\operatorname{rank}\partial_1 = 8$, $\dim\ker\partial_2 = 1$, and $H_1 = \mathbb{Z}^2$ again. (Set up the matrices; compute ranks by exhibiting pivots, not by brute force.) Where in your computation is homotopy invariance visible?

**2. Cohomology of $T^3$.**
(a) On the minimal complex of $T^3$, list the cells, confirm all boundary maps vanish, and read off $b_p = (1,3,3,1)$.
(b) On a fine $L^3$ lattice, exhibit explicit generators: the three winding 1-cochains and the three "sheet" 2-cochains, and verify closedness and non-exactness of each.
(c) Verify Poincaré duality $H^1 \cong H_2$ by matching your generators across the dual lattice.

**3. Laplacian zero modes.**
(a) Write $\Delta$ on 0-cochains of the $2\times2$ torus as an explicit $4\times4$ matrix and confirm its kernel is the constants ($b_0 = 1$).
(b) Verify that $h^{(x)}, h^{(y)}$ of §6 are annihilated by the 1-cochain Laplacian $\Delta_1 = \delta d + d\delta$ (compute both terms separately).

**4⋆. Torsion: the Klein bottle.**
Build the minimal cell complex of the Klein bottle: one site, two links $a, b$, one 2-cell glued along the edge word $a\,b\,a\,b^{-1}$ (the orientation-reversing identification). Show $\partial P = 2a$ directly from the edge word, write $\partial_2$ as a $2\times1$ integer matrix, compute its Smith normal form, extract the invariant factor 2, and conclude $H_1 = \mathbb{Z}\oplus\mathbb{Z}_2$. Then compute $H^1(K,\mathbb{Z}_2)$ and note it has *more* elements than the free part alone would give — the universal-coefficient phenomenon of F3.

**5⋆. Cup products by hand.**
(a) Using the full cubical conventions of [[courses/generalized-symmetries-course/conventions]] §5 (Chen–Tata), verify Leibniz $d(\alpha\cup\beta) = d\alpha\cup\beta - \alpha\cup d\beta$ for two 1-cochains on a single cube in $d=3$ — the same eight-term audit performed in §9 for $(f,\beta)$, one degree up, where the sign $(-1)^p$ first bites.
(b) For two 1-cochains, compute $(\alpha\cup\beta - \beta\cup\alpha)(P)$ explicitly and exhibit it as a "boundary-controlled" term.
(c) On $T^2$, evaluate $\sum_P (h^{(x)}\cup h^{(y)})(P)$ and $\sum_P (h^{(y)}\cup h^{(x)})(P)$ for the harmonic cochains of §6, and interpret the answers via the intersection form of §8 (the cup product is Poincaré-dual to intersection).

**6⋆. Self-dual degree in $d = 4$.**
Show that 2-cochains map to 2-cochains under $\star$ in $d=4$, decompose $C^2 \otimes \mathbb{R}$ into $\star$-eigenspaces (self-dual/anti-self-dual), and explain in one paragraph why this makes $d=4$ the natural home of electric–magnetic duality and of θ-angles (both to be exploited in Weeks 8 and 12). What are the analogous self-dual degrees in $d = 2$ and $d = 6$, and for what field content?

**7⋆⋆ (optional). Hodge with a metric.**
Redo the Hodge proof of §6 with a nontrivial diagonal metric (weights $w_\sigma > 0$ per cell in the inner product) and show the decomposition survives with $\delta$ replaced by its weighted adjoint. Anisotropic couplings ($\beta_x \ne \beta_y$) in Week 3's model are exactly such weights — this problem is why the duality machinery survives anisotropy.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block A. Rewritten to the note-quality-template standard 2026-07-07 (first draft 2026-07-01).*
