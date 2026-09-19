---
title: "Week 2 — Radial quantisation and the state–operator correspondence"
type: lecture-notes
course: syllabus
semester: 1
week: 2
block: A
duration: "4 hours (2 lectures × 2 hours)"
status: final
modified: 2026-08-25
---

# Week 2 — Radial Quantisation and the State–Operator Correspondence

> *Last week's symmetry was kinematic; this week it becomes a Hilbert space. The trick is to quantise a CFT not on flat time slices but on **spheres of fixed radius**, with the radius playing the role of time. The dilatation $D$ becomes the Hamiltonian, and the central result — the **state–operator correspondence** — is that every local operator $\mathcal{O}(0)$ is a state $|\mathcal{O}\rangle$ and vice versa, with the operator's scaling dimension equal to the state's energy. This is the structural fact that makes the OPE converge (Week 3) and that underlies all of conformal representation theory.*

## Learning goals

By the end of this week, a student can:

1. Write the conformal map between $\mathbb{R}^d$ and the cylinder $\mathbb{R}\times S^{d-1}$ and explain why $D$ is the cylinder Hamiltonian.
2. Set up radial quantisation: Hilbert space on $S^{d-1}$, the vacuum, the radial (BPZ) adjoint.
3. State and use the state–operator bijection $|\mathcal{O}\rangle=\mathcal{O}(0)|0\rangle$.
4. Show the cylinder energy of $|\mathcal{O}\rangle$ equals $\Delta$, and that $|\partial_\mu\mathcal{O}\rangle$ has energy $\Delta+1$.
5. Translate to the 2d $z=e^w$ picture, setting up Virasoro (Week 5).

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Modern CFT* §6** — radial quantisation, inner products and conjugation, unitarity bounds.
- Rychkov, [arXiv:1601.05000](https://arxiv.org/abs/1601.05000), Ch. 2 — the radial-quantisation Hilbert space.
- Simmons-Duffin, *TASI Lectures on the Conformal Bootstrap*, [arXiv:1602.07982](https://arxiv.org/abs/1602.07982), §2 — explicit radial-quantisation formulas.

**Prerequisites.** [[week-01-conformal-algebra-and-primaries]] ($[D,P_\mu]=iP_\mu$ and the primary/descendant structure are used directly); canonical quantisation on slices.

**AQFT cross-reference.** The cyclicity of the vacuum (Reeh–Schlieder) is the operator-algebra counterpart of the state–operator map; made rigorous only in Sem II — see [[week-05-tomita-operator|AQFT Wk 5]]. For now, treat $|0\rangle$ operationally.

**What these notes add.** adscft.org §6 sets up radial quantisation and the unitarity bounds; this note does not re-derive that material. It adds the picture of the map — the figure in §1, which is what most students actually need and which prose cannot substitute for — the energy-equals-dimension commutator done explicitly, and the link forward to Reeh–Schlieder in the AQFT course, which is where the state–operator correspondence stops being a trick and becomes a theorem about algebras.

## 1. Cylinder ↔ plane: the conformal map

Write flat $\mathbb{R}^d$ in radial coordinates, $ds^2 = dr^2 + r^2\,d\Omega_{d-1}^2$, and substitute $r=e^\tau$ (so $dr=e^\tau d\tau$):

$$
ds^2_{\mathbb{R}^d} = e^{2\tau}\big(d\tau^2 + d\Omega_{d-1}^2\big) = e^{2\tau}\,ds^2_{\mathrm{cyl}}.
$$

So flat space is **Weyl-equivalent** to the cylinder $\mathbb{R}_\tau\times S^{d-1}$, with conformal factor $\Omega=e^\tau=r$. A CFT does not see the Weyl factor (up to the anomaly of Week 4), so it can be quantised on either geometry.

The payoff: a **dilatation** $r\to\lambda r$ is a **time translation** $\tau\to\tau+\log\lambda$ on the cylinder. Hence the dilatation generator is the cylinder Hamiltonian,

$$
\boxed{\;H_{\mathrm{cyl}} = D.\;}
$$

Concentric spheres on the plane are constant-$\tau$ slices on the cylinder; the origin $r=0$ is the infinite past $\tau\to-\infty$, and $r=\infty$ the infinite future.


```
        plane (radial slices)                 cylinder  R x S^{d-1}
                                                  |     |
             . - - - .                            |  o  |   <- tau = log r
          .     ___     .                         |     |
        .     /     \     .          w = log z    |-----|   <- constant-tau slice
       .     |   x   |     .        ----------->  |     |
        .     \ ___ /     .                       |  o  |
          .             .                         |     |
             ' - - - '                            |     |
        origin = operator insertion               tau -> -infinity  = the state
```
**Figure 1. The map $w=\log z$ carries the punctured plane to the cylinder. Circles of constant radius become constant-$\tau$ slices; the operator sitting at the origin recedes to $\tau\to-\infty$ and becomes an incoming state.**

The figure is the content of the whole week. An operator inserted at a *point* is, after the map, a boundary condition in the infinite past — and a boundary condition in the infinite past is exactly what one means by an in-state.

> **Physical picture.** Radial quantisation is not a formal trick; it is the observation that a CFT has no scale and therefore no preferred notion of "equal time". In an ordinary QFT you slice spacetime by constant $t$ because the Hamiltonian generates translations in $t$. In a CFT the dilatation operator is just as good a generator, so you may slice by constant *radius* instead, and the operator that evolves you between slices is $D$ rather than $H$. Everything unusual about CFT quantisation follows from this one substitution: energies become dimensions, the vacuum sits at the origin, and the sphere at infinity is the other end of time. On the cylinder the picture is completely ordinary — it is a QFT on $\mathbb{R}\times S^{d-1}$ with a genuine Hamiltonian — which is why the cylinder is where intuition should live and the plane is where computations are easier.

## 2. Radial quantisation

**Hilbert space.** Quantise on a sphere $S^{d-1}$ of fixed radius; states live on the sphere, and "time evolution" is dilation outward. The **vacuum** $|0\rangle$ is the state prepared by the path integral over the interior disk with no insertions — equivalently the $\tau\to-\infty$ (origin) state, annihilated by $P_\mu$, $D$, $M_{\mu\nu}$, $K_\mu$ (the full conformal group fixes the origin and the vacuum).

**Radial adjoint.** Hermitian conjugation must be compatible with the radial "time." The Euclidean/BPZ adjoint acts on the plane by the inversion $x^\mu\to x^\mu/x^2$ composed with complex conjugation, and on the generators gives

$$
D^\dagger = D,\qquad P_\mu^\dagger = K_\mu,\qquad M_{\mu\nu}^\dagger = M_{\mu\nu}.
$$

So $K_\mu$ is literally the Hermitian conjugate of $P_\mu$: raising and lowering are adjoints. The inner product built from this adjoint is what unitarity (Week 1) constrains.

## 3. The state–operator correspondence (worked)

Define the state created by inserting $\mathcal{O}$ at the origin:

$$
\boxed{\;|\mathcal{O}\rangle := \lim_{x\to 0}\mathcal{O}(x)\,|0\rangle = \mathcal{O}(0)\,|0\rangle.\;}
$$

In the path integral this is the state on a sphere surrounding the origin, with $\mathcal{O}$ inserted inside — a perfectly regular boundary condition. The map is a **bijection**: conversely, any state on $S^{d-1}$ is prepared by *some* (possibly non-local-looking, but expandable in local operators) insertion at the origin. So

$$
\{\text{local operators}\}\;\;\longleftrightarrow\;\;\{\text{states in }\mathcal{H}_{S^{d-1}}\}.
$$

**Energy = dimension (worked).** Use $D|0\rangle=0$ and the primary transformation $[D,\mathcal{O}(0)] = i\Delta\,\mathcal{O}(0)$ (Week 1):

$$
D\,|\mathcal{O}\rangle = D\,\mathcal{O}(0)|0\rangle = [D,\mathcal{O}(0)]\,|0\rangle + \mathcal{O}(0)\,D|0\rangle = i\Delta\,\mathcal{O}(0)|0\rangle = i\Delta\,|\mathcal{O}\rangle.
$$

With the Hermitian Hamiltonian $H_{\mathrm{cyl}}=-iD$ (so that $-iD$ has real spectrum), the cylinder **energy** of $|\mathcal{O}\rangle$ is exactly the scaling **dimension** $\Delta$. A heavy operator is a high-energy state on the sphere.

> **[Proved.]** the bijection (path-integral regularity at the origin) and energy $=$ dimension (the commutator computation above). **[Stated — refs.]** the Weyl-anomaly shift of the vacuum energy in even $d$ (the sphere Casimir energy), a state-independent constant we suppress; it is a Week-4 effect.

> **Physical picture.** The correspondence is a bijection, and the two directions fail differently if you weaken the hypotheses. Operator $\to$ state is the easy direction: insert it at the origin, do the path integral over the interior of a small ball, read off the wavefunctional on the boundary sphere. State $\to$ operator is the direction that uses conformal symmetry essentially — you must be able to shrink the sphere to a point without changing the answer, and that is scale invariance. In a theory with a mass scale the shrinking changes things and the map dies, which is why nothing like this exists in generic QFT. The practical upshot is the one that matters for holography: the *spectrum* of a CFT on a sphere and its *operator content* are the same list of numbers, so a bulk field's mass (Week 8) and a boundary operator's dimension are the same datum seen twice.

**Worked example: the free scalar.** Make the map concrete for the free scalar in $d$ dimensions, $\Delta_\phi=\tfrac{d-2}{2}$ (Week 1). The mode expansion on a sphere of radius $r$ organises $\phi$ into modes of definite angular momentum on $S^{d-1}$; the lowest mode, taken to the origin, creates the primary state $|\phi\rangle=\phi(0)|0\rangle$ with $H_{\rm cyl}$-energy $\Delta_\phi$. The next states are the descendants $|\partial_\mu\phi\rangle=P_\mu|\phi\rangle$ at energy $\Delta_\phi+1$. The **shortening** that makes $\phi$ saturate the unitarity bound appears here as a *null* level-2 descendant: the equation of motion $\Box\phi=0$ means

$$
P^2|\phi\rangle = |\Box\phi\rangle = 0,
$$

so the would-be level-2 scalar descendant has zero norm and drops out of the Hilbert space. (For an *interacting* scalar above the bound, $P^2|\phi\rangle\ne0$ and that state survives.) This is the radial-quantisation face of "free field = saturated unitarity bound = null descendant," and it is exactly the level-2 computation deferred in Week 1 §5. Composite primaries like $:\!\phi^2\!:$ (dimension $2\Delta_\phi=d-2$) appear as new lowest-weight states not reachable by acting with $P_\mu$ on $|\phi\rangle$ — each primary starts a fresh tower.

## 4. Descendants as a tower

Acting with $P_\mu$ raises the energy by one unit (because $[D,P_\mu]=iP_\mu$):

$$
P_\mu|\mathcal{O}\rangle = |\partial_\mu\mathcal{O}\rangle,\qquad H_{\mathrm{cyl}}\,|\partial_\mu\mathcal{O}\rangle = (\Delta+1)\,|\partial_\mu\mathcal{O}\rangle,
$$

while $K_\mu$ lowers it, and on a **primary** $K_\mu|\mathcal{O}\rangle=0$ (lowest-weight condition). The primary plus its $P$-descendants thus forms a **lowest-weight module** — the conformal multiplet — graded by energy:

$$
|\mathcal{O}\rangle,\quad P_\mu|\mathcal{O}\rangle,\quad P_\mu P_\nu|\mathcal{O}\rangle,\ \dots\qquad(\text{energies }\Delta,\ \Delta+1,\ \Delta+2,\dots).
$$

This is the same object that becomes a **Verma module** in 2d (Week 5). Unitarity = positivity of the BPZ inner product on this tower; positivity of the level-1 norms is precisely the Week-1 unitarity bound.

> **[Stated — refs: Rychkov §3.]** positivity of the radial inner product on primaries ⟺ the Week-1 unitarity bounds.

> **Physical picture.** The tower of descendants is the CFT's version of a Fock space built on a single-particle state, with $P_\mu$ as the creation operator and $\Delta$ as the energy. What is different is that the tower is not free: the norms are fixed by the algebra, and when one of them hits zero the representation is reducible and a *null state* appears. A null state is not a pathology but an equation — it says some descendant vanishes identically, i.e. the operator obeys a differential equation. This is how free fields, conserved currents and the stress tensor all arise as saturation cases (Week 1 §5), and in $d=2$ it is how the minimal models arise (Week 5 §3).

## 5. The 2d preview

In $d=2$, write the cylinder coordinate $w=\tau+i\sigma$ and map to the plane by $z=e^{w}$. The radial-quantisation "time" $\tau=\log|z|$ is the radial direction on the $z$-plane, and the dilatation is $z\partial_z+\bar z\partial_{\bar z}$. A 2d primary of weights $(h,\bar h)$ then has

$$
L_0|h\rangle = h|h\rangle,\qquad \bar L_0|\bar h\rangle = \bar h|\bar h\rangle,\qquad \Delta = h+\bar h,\quad \ell = h-\bar h,
$$

where $L_0,\bar L_0$ are the zero modes of the (anti)holomorphic stress tensor. This is the bridge to the Virasoro representation theory of Week 5: the radial-quantisation tower *is* the Verma module $L_{-n_1}\cdots|h\rangle$.

> **Physical picture: what the $d=2$ case adds.** Everything above works in any dimension, but in $d=2$ the map $w=\log z$ does something extra: because *every* holomorphic map is conformal there, the single dilatation $D$ is embedded in an infinite tower $L_n$, and radial quantisation produces not one Hamiltonian but a whole Virasoro algebra acting on the sphere at each radius. The state–operator correspondence survives unchanged; what changes is that the multiplets are now Virasoro modules rather than $\mathfrak{so}(d,2)$ multiplets, and they can be *degenerate* — some descendants vanish. That degeneracy is what makes the minimal models exactly solvable and what makes AdS$_3$/CFT$_2$ the case where holography can be checked rather than assumed (Week 5, and Sem II Wk 7).

## 6. Subtleties and fine print

**The Casimir energy is a real effect, not a nuisance.** Suppressing the sphere's vacuum energy is legitimate here because it is state-independent, but in even $d$ it is precisely the Weyl anomaly of Week 4, and in $d=2$ it is the $-c/24$ that makes the Cardy formula work (Week 5 §4). "A constant we drop" in this note is "the central charge" two weeks later. Track it.

**Euclidean throughout.** Radial quantisation is a Euclidean construction, and the inner product it defines is the reflection-positive one. Statements like $P_\mu^\dagger = K_\mu$ hold with respect to *that* inner product and not the naive Lorentzian adjoint. Continuation to Lorentzian signature is standard but is not free; it is where the distinction between the causal and entanglement wedges eventually lives (Week 14).

**"Radius" is not a physical scale.** Nothing depends on the radius of the sphere used to define the state, and this is scale invariance doing work rather than a convention. If you find yourself needing to specify the radius, either the theory is not conformal or the operator is not a local primary.

**The map is singular at two points.** $w=\log z$ is ill-defined at $z=0$ and $z=\infty$, which is exactly why those two points carry the in- and out-states rather than ordinary field data. Any argument that treats the origin as a generic point of the plane has lost the content of the week.

## 7. Key claims and proof status

- **[Proved.]** $H_{\mathrm{cyl}}=D$ from the Weyl map $\mathbb{R}^d\!\to\!\mathbb{R}\times S^{d-1}$ (§1).
- **[Proved.]** state–operator bijection and energy $=$ dimension (§3).
- **[Proved.]** descendant energies $\Delta+n$ and $K_\mu$-annihilation of primaries (§4).
- **[Stated — refs.]** radial-inner-product positivity ⟺ unitarity bounds (§4).

*No coefficients in this note are uncertain. (No `CHECK` items for Wk 2.)*

## 8. What to take away

- Quantise on **spheres**, radius = time; the dilatation $D$ is the Hamiltonian, and flat space is Weyl-equivalent to the cylinder $\mathbb{R}\times S^{d-1}$.
- **State–operator correspondence:** $|\mathcal{O}\rangle=\mathcal{O}(0)|0\rangle$ is a bijection; cylinder energy $=$ scaling dimension $\Delta$.
- $P_\mu$ raises energy by 1 ($|\partial_\mu\mathcal{O}\rangle$), $K_\mu=P_\mu^\dagger$ lowers it; a primary is the lowest-weight vector of an energy-graded multiplet.
- In 2d, $z=e^w$ turns the multiplet into a **Verma module** with $L_0=h$, $\bar L_0=\bar h$ — the setup for Week 5.

5. **The map is the content** (Figure 1). An operator at a point becomes a boundary condition in the infinite past, which is what an in-state is. Slicing by radius rather than time is legitimate because a CFT has no scale to prefer one over the other.
6. **The bijection's two directions fail differently.** Operator $\to$ state needs only a path integral; state $\to$ operator needs scale invariance to shrink the sphere. This is why nothing like the correspondence exists in a theory with a mass.
7. **The suppressed constant is the central charge.** The sphere Casimir energy dropped here is $-c/24$, and it is what makes Cardy work two weeks later.

## Exercises

**Core.**

1. **The map.** Derive $ds^2_{\mathbb{R}^d}=e^{2\tau}(d\tau^2+d\Omega_{d-1}^2)$ from $r=e^\tau$, and identify dilatations with cylinder time translations.
2. **Descendant energy.** Show $P_\mu|\mathcal{O}\rangle$ has energy $\Delta+1$ and $K_\mu|\mathcal{O}\rangle=0$ for a primary.
3. **Free-scalar spectrum.** For the free scalar ($\Delta=\tfrac{d-2}{2}$) in $d=4$, list all operators of dimension $\le 3$ in the radial Hilbert space and classify primary vs descendant.

**Starred.**

4. $\star$ **2d weights.** Using $z=e^w$, show a 2d primary of weight $h$ has $L_0$-eigenvalue $h$ (and $\bar L_0=\bar h$). Connect to $\Delta=h+\bar h$, $\ell=h-\bar h$.
5. $\star$ **BPZ adjoint.** Verify $P_\mu^\dagger=K_\mu$ under the inversion-based radial adjoint, and explain why this makes $H_{\mathrm{cyl}}=-iD$ Hermitian.

**Project.**

6. **Regularity at the origin.** Explain why the path integral preparing $|\mathcal{O}\rangle$ is well-defined despite the sphere collapsing to a point, and what role operator ordering / the OPE plays. (Feeds Week 3's OPE-convergence argument.)

## Connections to other parts of the wiki

- **Within the course.** Builds on [[week-01-conformal-algebra-and-primaries]]; the energy $=$ dimension result powers OPE convergence in [[week-03-ope-and-conformal-blocks]], and the Verma-module preview sets up [[week-05-2d-cft-essentials]].
- **AQFT course cross-reference.** The vacuum's cyclicity (Reeh–Schlieder) is the algebraic counterpart of state–operator; see [[week-05-tomita-operator|AQFT Wk 5]] (Sem II rigour).
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester I Block A. Reviewed and approved (status: final). Last revised 2026-05-28.*
