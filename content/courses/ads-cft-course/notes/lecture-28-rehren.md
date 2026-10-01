---
title: "Lecture 28 — What algebraic holography establishes on fixed AdS"
type: lecture-notes
edition: "2.2 — rewritten at the AQFT standard"
lecture: 28
semester: 2
week: 11
hours: 3
prerequisites: "Lectures 9, 11, 13, 16, 18 and 22; nets of von Neumann algebras and the Bisognano–Wichmann theorem"
status: "rewritten 2026-09-30, pending instructor review; the region map of AdS3 with its four properties, the transfer of isotony, locality, covariance and modular structure, the triviality of the three-arc intersection for a Haag-dual, strongly additive boundary net, the failure of strong additivity for the generalized free field dual to a free bulk field, the AdS3 propagator and its boundary limit are proved or exact calculations; Rehren's theorem in general dimension, the conformal Bisognano–Wichmann theorem and the perturbative results of Dütsch and Rehren are stated with sources"
modified: 2026-09-30
---

# Lecture 28 — What algebraic holography establishes on fixed AdS

> *Every holographic statement of Lectures 18–27 relied on a gravitational path integral, a large-$N$ limit or a code subspace. In 1999 Rehren showed that one statement needs none of them. The isometry group of AdS acts on the boundary as the conformal group, and the wedges of AdS correspond one to one with the double cones of the boundary, preserving inclusions and causal complements; any net of algebras on one side therefore defines a net on the other. This lecture proves the region map in AdS$_3$, where it follows from the geodesics of Lecture 16, transfers isotony, locality, covariance and modular structure through it, and shows that the bulk modular flow of a wedge is the AdS–Rindler boost of Lecture 22. It then asks what the transported bulk theory contains in a compact region. For a boundary net with Haag duality and strong additivity, a compact region at the center of three arcs carries only multiples of the identity, while the generalized free field dual to a bulk free field, which fails strong additivity, carries the bulk field there. The exact correspondence thus separates the kinematics of holography from the property that makes bulk physics local.*

## How to use this lecture

**Classroom core, one meeting of three hours.** The history (§1, 10 minutes), the region map in AdS$_3$ (§2, 35 minutes), and the transfer of a net (§3, 25 minutes) come before a 10-minute break. After it come the modular structure (§4, 15 minutes), compact regions and the three arcs (§5, 30 minutes), and the free field with its boundary limit (§6, 25 minutes), with 30 minutes for Checkpoints 1 and 2 and Problems 4–6; Problems 1–3 complete the core assignment. These allocations are proposals and have not been tested in class.

**Self-study.** The comparison with semiclassical reconstruction (§7), what the route contributes (§8), and Problems 7–12, including the AdS$_3$ propagator, the two-qubit intersection and the Poincaré chart.

**Research extension.** A compact-region algebra for a concrete boundary net, asymptotically AdS spacetimes, and the boundary limit of an interacting bulk field, in Problems 13–15.

**Prerequisites.** Lecture 9 for nets of local algebras, Lecture 11 for the modular flow of a ball, Lecture 13 for the global and Poincaré charts, Lecture 16 for geodesics in AdS$_3$, Lecture 18 for causal wedges, the smearing kernel and the three arcs, Lecture 22 for the AdS–Rindler Killing vector. Nets of von Neumann algebras and the Bisognano–Wichmann theorem.

**What this lecture establishes.** In AdS$_3$, the map from boundary diamonds to bulk wedges, with its trace on the boundary, isotony, covariance and preservation of causal complements, is proved. The transfer of isotony, locality, covariance, vacuum and modular structure through the map, and the triviality of the three-arc intersection for a boundary net with Haag duality and strong additivity, are proved under the stated hypotheses, and so is the failure of strong additivity for the generalized free field dual to a free bulk field, whose net is identified with the transported net given the conformal Bisognano–Wichmann theorem. The AdS$_3$ propagator and its boundary limit are exact calculations. Rehren's theorem in general dimension, the conformal Bisognano–Wichmann theorem of Brunetti, Guido and Longo, and the perturbative results of Dütsch and Rehren are stated with sources.

## 0. Reading

**Primary.**

- K.-H. Rehren, [Algebraic Holography](https://arxiv.org/abs/hep-th/9905179) (1999).
- K.-H. Rehren, [Local Quantum Observables in the Anti-deSitter - Conformal QFT Correspondence](https://arxiv.org/abs/hep-th/0003120) (2000).
- R. Brunetti, D. Guido, R. Longo, [Modular Structure and Duality in Conformal Quantum Field Theory](https://arxiv.org/abs/funct-an/9302008) (1993).

**Secondary.**

- M. Dütsch, K.-H. Rehren, [Generalized free fields and the AdS-CFT correspondence](https://arxiv.org/abs/math-ph/0209035) (2002), and [A comment on the dual field in the AdS-CFT correspondence](https://arxiv.org/abs/hep-th/0204123) (2002).
- M. Bertola, J. Bros, U. Moschella, R. Schaeffer, [AdS/CFT correspondence for n-point functions](https://arxiv.org/abs/hep-th/9908140) (1999).
- R. Haag, *Local Quantum Physics* (Springer, 1996), chapters III and IV.

**Optional research reading.**

- K.-H. Rehren, [A Proof of the AdS-CFT Correspondence](https://arxiv.org/abs/hep-th/9910074) (1999).
- P. L. Ribeiro, [Structural and Dynamical Aspects of the AdS/CFT Correspondence: a Rigorous Approach](https://arxiv.org/abs/0712.0401) (2007).
- K.-H. Rehren, [QFT Lectures on AdS-CFT](https://arxiv.org/abs/hep-th/0411086) (2004).
- D. Guido, [Modular theory for the von Neumann algebras of Local Quantum Physics](https://arxiv.org/abs/0812.1511) (2008).
- P. D. Hislop, R. Longo, "Modular structure of the local algebras associated with the free massless scalar field theory," *Commun. Math. Phys.* 84 (1982) 71.

## 1. Can holography be formulated without a bulk path integral?

Haag and Kastler proposed in 1964 to describe a quantum field theory by the algebras of observables localized in regions of spacetime, a net $O\mapsto\mathcal A(O)$ subject to isotony, locality and covariance, and to treat fields as one way among others of generating them. The modular theory of Lectures 3 and 9 entered this framework through the theorem of Bisognano and Wichmann (Lecture 10), and in 1982 Hislop and Longo showed that for the free massless field the modular group of a double cone is a conformal transformation. Brunetti, Guido and Longo proved in 1993 that this holds for every conformal net, using a theorem of Borchers that Lecture 30 develops, and that such nets satisfy Haag duality on the universal cover of compactified Minkowski space.

After Maldacena's conjecture and Witten's dictionary, Rehren asked in 1999 what survives of the correspondence if one keeps only the symmetry and the causal structure. The group $SO(2,d)$ acts on AdS$_{d+1}$ by isometries and on its conformal boundary by conformal transformations. Rehren observed that a family of bulk regions, the wedges, is in one-to-one correspondence with the double cones of the boundary, compatibly with inclusions, causal complements and the group action, and he concluded that a covariant net on either side defines one on the other. His abstract calls this a rigorous and simple proof of a one-to-one correspondence between the two kinds of theories, which takes vacua to vacua and positive energy to positive energy. In a sequel of 2000 he gave an explicit identification of the local observables of the two theories. Bertola, Bros, Moschella and Schaeffer had shown in 1999 that a limiting procedure applied to the $n$-point functions of interacting fields on AdS produces conformal field theories on the boundary. In 2002 Dütsch and Rehren wrote an explicit formula relating the Klein–Gordon field on AdS to generalized free fields on the boundary, which they contrasted with the algebraic notion.

This lecture follows Rehren's argument in the one case where every step can be drawn, AdS$_3$, and then asks what it implies for bulk locality. The answer is the point of the lecture: the correspondence is exact and kinematic, and whether the bulk theory has local observables depends on a property of the boundary net that large-$N$ theories have and generic conformal field theories lack.

## 2. The region map in AdS$_3$

Write the Poincaré chart of AdS$_3$, with $L=1$, in light-cone coordinates $x^\pm=t\pm x$,

$$
ds^2=\frac{-dx^+dx^-+dz^2}{z^2},\qquad z>0 .
$$

The metric is conformal to the half-space $z>0$ of three-dimensional Minkowski space, and conformal factors do not change light cones. The half-space is convex, so a causal curve between two of its points can be replaced by the straight segment, which stays inside. Therefore two points of the Poincaré chart are causally related exactly when they are causally related in flat space. [Proved.]

A boundary double cone, or diamond, is

$$
D=\bigl\{a^+<x^+<b^+,\ a^-<x^-<b^-\bigr\},
$$

with past tip $a=(a^+,a^-)$ and future tip $b=(b^+,b^-)$. Its bulk wedge is the set of bulk points in the chronological future of $a$ and the chronological past of $b$, the causal wedge of Lecture 18. By the flat causal structure,

$$
W(D)=\Bigl\{(x^+,x^-,z):\ (x^+-a^+)(x^--a^-)>z^2,\ \ (b^+-x^+)(b^--x^-)>z^2,\ \ a^\pm<x^\pm<b^\pm\Bigr\},
$$

since a point lies in the future of the boundary point $a$ exactly when its squared flat interval to $a$ is negative and it lies later. [Exact.] For the diamond of the interval $|x|<R$ at $t=0$, the slice $t=0$ of $W(D)$ is $(R+x)(R-x)>z^2$, that is $x^2+z^2<R^2$: the half-disk bounded by the Ryu–Takayanagi geodesic, as in Lectures 18 and 22.

The map $D\mapsto W(D)$ has four properties.

*Trace on the boundary.* At $z=0$ the inequalities reduce to $a^\pm<x^\pm<b^\pm$. The wedge touches the boundary in the diamond $D$.

*Isotony.* If $D_1\subset D_2$, the tips of $D_1$ lie between those of $D_2$, and $W(D_1)\subset W(D_2)$.

*Covariance.* An isometry of AdS$_3$ preserves the causal order of the bulk and acts on the boundary as a conformal transformation, mapping tips to tips. Therefore $g\,W(D)=W(gD)$ for every $g$ in the isometry group.

*Causal complements.* Here the global structure matters. In global AdS$_3$ the boundary is the cylinder, a diamond is the domain of dependence of an arc of a Cauchy circle, and the causal complement of a diamond is the diamond of the complementary arc. By Lecture 18, §6, the causal wedge of an arc of half-width $\theta_0$ is the domain of dependence of the bulk region between the arc and its geodesic $\tanh\rho\cos\theta=\cos\theta_0$. The complementary arc, of half-width $\pi-\theta_0$ centered at $\theta=\pi$, has the geodesic $\tanh\rho\cos(\theta-\pi)=\cos(\pi-\theta_0)$, which is the same curve. The two bulk regions are thus complementary on the bulk Cauchy slice, and their domains of dependence are causal complements of each other:

$$
W(D')=W(D)' .
$$

[Proved, in AdS$_3$.] The figure shows the two regions. In AdS$_{d+1}$ the same four properties hold for wedges and double cones on the universal covering of the boundary, which is the content of Rehren's geometric lemma. [Stated only — refs: Rehren 1999.]

![[ads-cft-algebraic-holography.svg|Left: the slice of constant global time of AdS3 drawn as a disk, with a boundary arc D, its complementary arc D′, and the single geodesic that bounds both of their bulk wedges, the wedge of D on one side and the wedge of D′ on the other. Right: three equal arcs A, B and C, the geodesics of each arc, and the curved central triangle bounded by them, which lies in the wedges of the three pairs AB, BC and CA.]]

**Checkpoint 1.** Why must the property $W(D')=W(D)'$ be formulated on the boundary cylinder?

**Answer.** In two-dimensional Minkowski space, the Poincaré boundary of AdS$_3$, the causal complement of a diamond is disconnected, the union of two wedge-shaped regions on either side, and it is not a diamond. On the cylinder the two pieces join across the spatial infinity of the Minkowski patch into the diamond of the complementary arc, which also contains points outside the patch, and the region map, which acts on diamonds, can be applied to it.

## 3. Relabel a net

Consider a conformal net on the boundary cylinder: an assignment $D\mapsto\mathcal A_\partial(D)$ of von Neumann algebras on a Hilbert space $\mathcal H$, isotonous, local in the sense that algebras of causally disjoint diamonds commute, covariant under a positive-energy unitary representation $U$ of the conformal group of the cylinder, with an invariant vacuum $\Omega$. Rehren's construction defines the bulk wedge net by

$$
\mathcal A_{\mathrm{bulk}}\bigl(W(D)\bigr)=\mathcal A_\partial(D).
$$

The same algebra is assigned a second region. Its properties follow from §2.

**Proposition (transfer). Proved, given the region map.** The bulk wedge net is isotonous, local, covariant under the isometries of AdS through the same representation $U$, with the same vacuum and positive energy.

*Proof.* Isotony is the isotony of the region map followed by that of the boundary net. If two wedges are causally disjoint, $W(D_1)\subset W(D_2)'=W(D_2')$, and the trace property gives $D_1\subset D_2'$, so boundary locality makes the two algebras commute. Covariance follows from $gW(D)=W(gD)$ and $U(g)\mathcal A_\partial(D)U(g)^\dagger=\mathcal A_\partial(gD)$. The vacuum is the same vector, and the generator of global time in AdS is the conformal Hamiltonian on the cylinder, which is positive. $\square$

Conversely, an AdS-covariant net of wedge algebras defines a boundary net by the inverse assignment, and in general dimension the two constructions are inverse to each other. [Stated only — refs: Rehren 1999.] Two remarks keep the result in proportion. No bulk point is identified with a boundary point: the correspondence concerns families of regions. And properties of nets transfer as properties of nets: Haag duality on the boundary, $\mathcal A_\partial(D')=\mathcal A_\partial(D)'$, holds exactly when the bulk wedge net satisfies $\mathcal A_{\mathrm{bulk}}(W')=\mathcal A_{\mathrm{bulk}}(W)'$.

## 4. Modular structure comes along

The algebra and the vector are the same on both sides, so the Tomita operator, the modular operator and the modular conjugation are the same operators. For a conformal net, Brunetti, Guido and Longo proved that the modular group of a diamond is geometric,

$$
\Delta_D^{-is}=U\bigl(\Lambda_D(2\pi s)\bigr),
$$

where $\Lambda_D(\eta)$ is the one-parameter group of conformal transformations preserving $D$, the conformal boost generated by the vector field $\zeta$ of Lecture 11, and the modular conjugation implements a conformal reflection exchanging $D$ and $D'$. [Stated only — refs: Hislop–Longo 1982; Brunetti–Guido–Longo 1993.] The same unitaries act in the bulk as the isometries that preserve $W(D)$. These are the AdS–Rindler boosts of Lecture 22, whose Killing vector $\xi_B$ reduces at $z=0$ to $\zeta$. Therefore the modular group of the bulk wedge algebra in the vacuum is the AdS–Rindler boost of the wedge. [Proved, given the conformal Bisognano–Wichmann theorem.]

Note that this statement is exact and needs neither large $N$ nor a code subspace: it is the algebraic counterpart of the result of Lecture 21 that boundary modular flow acts as bulk modular flow in the entanglement wedge. The price is that the bulk theory is whatever net the boundary theory transports, with no further guarantee about what it contains.

**Checkpoint 2.** Which data must coincide for two modular operators to be identified?

**Answer.** The represented von Neumann algebra and the cyclic and separating vector. The same abstract algebra in two inequivalent representations, or with two different states, has different modular operators; in Rehren's construction both coincide by definition.

## 5. Local bulk regions require intersections

A compact bulk region $O$ is contained in many wedges, and an observable localized in $O$ should belong to all of them. The natural definition is

$$
\mathcal A_{\mathrm{bulk}}(O)=\bigcap_{W\supset O}\mathcal A_{\mathrm{bulk}}(W),
$$

which is isotonous, since a smaller region lies in more wedges and the intersection becomes smaller. The question is whether the intersection contains anything beyond multiples of the identity.

Consider the three arcs of Lecture 18, §6, three equal arcs $A$, $B$ and $C$ of the boundary circle of global AdS$_3$ at $\tau=0$. Each pair, such as $AB$, covers more than half the circle, and its wedge contains the center of AdS. The three geodesics bound an ideal triangle, shown in the figure, which reaches the boundary only at the three junction points of the arcs. Any compact region $O$ inside it lies in the three pair wedges, so

$$
\mathcal A_{\mathrm{bulk}}(O)\subset\mathcal A_\partial(AB)\cap\mathcal A_\partial(BC)\cap\mathcal A_\partial(CA).
$$

**Proposition (three arcs). Proved, under the stated hypotheses.** Suppose that the boundary net satisfies Haag duality for diamonds on the cylinder, $\mathcal A_\partial(D')=\mathcal A_\partial(D)'$; that it is strongly additive, so that the algebra of the union of two adjacent arcs with their common endpoint is generated by the two algebras; and that its diamond algebras are factors. Then

$$
\mathcal A_\partial(AB)\cap\mathcal A_\partial(BC)=\mathcal A_\partial(B),
\qquad
\mathcal A_\partial(AB)\cap\mathcal A_\partial(BC)\cap\mathcal A_\partial(CA)=\mathbb C\,1 .
$$

*Proof.* Haag duality gives $\mathcal A_\partial(AB)=\mathcal A_\partial(C)'$ and $\mathcal A_\partial(BC)=\mathcal A_\partial(A)'$. The commutant of a union is the intersection of commutants, so $\mathcal A_\partial(C)'\cap\mathcal A_\partial(A)'=\bigl(\mathcal A_\partial(C)\vee\mathcal A_\partial(A)\bigr)'$. The arcs $C$ and $A$ are adjacent, and strong additivity gives $\mathcal A_\partial(C)\vee\mathcal A_\partial(A)=\mathcal A_\partial(CA)$, whose commutant is $\mathcal A_\partial(B)$ by Haag duality. Finally $\mathcal A_\partial(B)\cap\mathcal A_\partial(CA)=\mathcal A_\partial(B)\cap\mathcal A_\partial(B)'$ is the center of a factor. $\square$

For such a boundary theory the transported bulk theory has no observable localized at the center of AdS, only multiples of the identity. [Proved.] The finite counterpart makes the mechanism visible: for three qubits, the algebras of the pairs $AB$ and $BC$ intersect in the algebra of $B$, of dimension four, and the three pair algebras intersect in the scalars. [Exact calculation, checked numerically.] Lecture 18, §6, used the same argument informally for the three arcs and resolved it with the three-qutrit code of Lecture 2. There, the operator at the center has a representative on each pair, and the representatives agree on the code subspace while differing as operators; the intersection of the three pair algebras is again trivial. Bulk locality is a property of how operators act on a subspace, and an exact correspondence of nets with these three properties cannot supply it.

The hypotheses are exactly where large-$N$ theories differ. Take for the bulk net the free scalar field of §6, with Weyl operators $W(f)=e^{i\phi(f)}$ and $[\phi(f),\phi(g)]=i\sigma(f,g)$, a number fixed by the commutator function, so that $W(f)W(g)=e^{-i\sigma(f,g)}W(g)W(f)$. If $f$ is supported in the domain of dependence of $O$, then $W(f)$ belongs to the algebra of every wedge that contains $O$, and the triple intersection is not trivial. The boundary dual of this net, the generalized free field of §6, must therefore violate a hypothesis of the proposition, and the violation can be seen directly. Choose $g$ also supported in the domain of dependence of $O$, with $\sigma(f,g)\notin2\pi\mathbb Z$, which a rescaling of $g$ arranges whenever $\sigma(f,g)\neq0$. Then $W(g)$ commutes with the algebras of the wedges $W(A)$ and $W(B)$, which are causally disjoint from its support, and therefore with $\mathcal A_\partial(A)\vee\mathcal A_\partial(B)$. But it does not commute with $W(f)$, which lies in $\mathcal A_\partial(AB)$. Thus

$$
\mathcal A_\partial(A)\vee\mathcal A_\partial(B)\neq\mathcal A_\partial(AB):
$$

the boundary algebra of two adjacent arcs, which §6 identifies with the algebra of the generalized free field, is larger than the algebra generated by the two arcs, because it contains bulk degrees of freedom that neither wedge reaches. [Proved, for the free bulk field, with the identification of §6.] Lecture 29 shows that single-trace operators of large-$N$ theories become generalized free fields in a precise limit, which is how they escape the proposition.

> **Physical picture: a center without a code subspace.** Each pair of arcs reconstructs the center of AdS. In the code of Lecture 18 the three reconstructions are different operators that agree on a subspace, and nothing requires them to agree elsewhere. An exact correspondence of nets has no subspace to restrict to: an observable at the center must be a single operator in the three pair algebras at once, and Haag duality with strong additivity leave only multiples of the identity. A boundary theory dual to local bulk physics must therefore violate one of these properties exactly, as the generalized free field does, or produce the center only on a subspace and only approximately, as large-$N$ theories are expected to do.

## 6. The free field and its boundary limit

Consider a scalar of mass $m^2=\Delta(\Delta-2)$ in Euclidean AdS$_3$. Its propagator depends only on the geodesic distance $\sigma$,

$$
G_\Delta(\sigma)=\frac{e^{-(\Delta-1)\sigma}}{4\pi\,\sinh\sigma},
\qquad
\cosh\sigma=\frac{z^2+z'^2+|x-x'|^2}{2zz'} ,
$$

where the second relation gives $\sigma$ between the points $(z,x)$ and $(z',x')$. The function solves $G''+2\coth\sigma\,G'=\Delta(\Delta-2)\,G$ for $\sigma>0$, the radial form of the Klein–Gordon equation on hyperbolic space, and behaves as $1/4\pi\sigma$ at short distance, the normalization of a unit point source. [Exact calculation, checked symbolically (Problem 10).] As both points approach the boundary, $\cosh\sigma\simeq|x-x'|^2/2zz'$ and $e^{-\sigma}\simeq zz'/|x-x'|^2$, so

$$
\lim_{z,z'\to0}\,(zz')^{-\Delta}\,G_\Delta=\frac1{2\pi\,|x-x'|^{2\Delta}} ,
$$

the two-point function of a conformal primary of dimension $\Delta$, with a normalization that in AdS$_3$ does not depend on $\Delta$. [Exact calculation, checked symbolically.] The boundary field $\mathcal O(x)=\lim z^{-\Delta}\phi(z,x)$, for the quantized bulk field in the vacuum, has this two-point function, and since the bulk field is free all its correlators are Gaussian: it is a generalized free field. For interacting bulk fields, Bertola, Bros, Moschella and Schaeffer obtained conformal boundary theories as limits of bulk $n$-point functions, and Dütsch and Rehren showed that in perturbation theory Witten graphs are boundary limits of the corresponding Feynman graphs, so that the dual correlation functions are limits of bulk correlation functions. [Stated only — refs: Bertola–Bros–Moschella–Schaeffer 1999; Dütsch–Rehren 2002, hep-th/0204123.] The generalized free field has no stress-energy tensor among its Wightman fields; Dütsch and Rehren constructed one as a singular limit, which still serves as a conserved density for the Poincaré generators. [Stated only — refs: Dütsch–Rehren 2002, math-ph/0209035.]

Rehren's map, applied to the net of the free bulk field, gives the net of this generalized free field on the boundary. The boundary field smeared in $D$ is a limit of bulk fields localized in $W(D)$, so the algebra it generates lies in $\mathcal A_{\mathrm{bulk}}(W(D))$. The algebra of the boundary field is invariant under the modular group of $\mathcal A_{\mathrm{bulk}}(W(D))$, which acts by the conformal boosts of $D$, and the vacuum is cyclic for it by the Reeh–Schlieder property, so Takesaki's theorem gives equality. [Proved, given the conformal Bisognano–Wichmann theorem.] Dütsch and Rehren wrote an explicit formula relating the Klein–Gordon field on AdS to the generalized free field and contrasted it with the algebraic notion, and the smearing kernels of Lecture 18 are later formulas of the same kind. [Stated only — refs: Dütsch–Rehren 2002, math-ph/0209035.] The algebraic identity of the wedge and diamond algebras does not require a pointwise kernel. Such a kernel exists as a real function for global reconstruction, and for an AdS–Rindler wedge it requires complexified boundary coordinates or the convolution kernels of Morrison (Lecture 18, §7). [Stated only — refs: Hamilton–Kabat–Lifschytz–Lowe 2006; Morrison 2014.]

## 7. Self-study: two meanings of a bulk–boundary map

In Rehren's construction the geometry is fixed and nets are transported exactly through a correspondence of regions. In semiclassical reconstruction, Lectures 18–21, an effective bulk algebra on a code subspace is identified with recoverable boundary observables. The geometry can then depend on the state, and area terms, gravitational dressing and finite-$N$ corrections enter. The vacuum ball makes the two descriptions look close, since its causal and entanglement wedges coincide and its modular flow is geometric. More general entanglement wedges, such as the two-interval transition of Lecture 19 or the islands of Lecture 26, do not follow from the fixed correspondence of wedges and double cones.

The comparison is productive when it asks which assumptions the two frameworks share. Both use locality and covariance; the semiclassical framework adds a code subspace, a large-$N$ limit and a dynamical geometry. The proposition of §5 locates the difference precisely: the exact framework with a strongly additive boundary net has no compact bulk observables, and the semiclassical framework obtains them on a subspace from a boundary theory whose relevant sector behaves as a generalized free field.

## 8. Self-study: what this route contributes

The algebraic starting point of the course has an exact continuum realization: a bulk–boundary relation can be formulated as a correspondence of region-indexed observables, without a string construction and without a path integral, and it carries modular structure exactly. Its limitation is equally instructive. A region map and covariance do not determine a gravitational action, Newton's constant, black-hole entropy or a sum over geometries; and on a fixed background there is no room for the state-dependent wedges of Lectures 19–27. Ribeiro extended the correspondence to a class of asymptotically AdS spacetimes of dimension greater than three, where the region map weakens and gravitational effects appear in the boundary theory. [Stated only — refs: Ribeiro 2007.]

## 9. What to take away

- **Proved, in AdS$_3$:** the map from boundary diamonds to bulk causal wedges touches the boundary in the diamond, preserves inclusions, commutes with the isometries, and takes causal complements to causal complements, the last because complementary arcs share their geodesic.
- **Proved, given the region map:** Rehren's relabeling $\mathcal A_{\mathrm{bulk}}(W(D))=\mathcal A_\partial(D)$ transfers isotony, locality, covariance, the vacuum and positive energy; in general dimension the correspondence is one to one (stated).
- **Proved, given the conformal Bisognano–Wichmann theorem:** the modular flow of a bulk wedge algebra in the vacuum is the AdS–Rindler boost of the wedge.
- **Proved, under Haag duality, strong additivity and factoriality:** the bulk algebra of a compact region at the center of three arcs is trivial. The generalized free field dual to a free bulk field carries bulk operators there, and its algebra on two adjacent arcs is larger than the algebra the arcs generate (proved).
- **Exact calculation:** the AdS$_3$ propagator $e^{-(\Delta-1)\sigma}/4\pi\sinh\sigma$ has the boundary limit $1/2\pi|x-x'|^{2\Delta}$, the two-point function of a generalized free field.

## 10. Looking ahead

Lecture 29 studies the boundary side of the last point. At large $N$, single-trace operators become generalized free fields whose two-point function depends on the state, and the algebra they generate changes type at the Hawking–Page transition: type I in thermal AdS, where the spectrum is discrete, and for the black hole, where it is continuous, a factor that is not of type I and that Leutheusser and Liu identified as type III$_1$. Lectures 30 and 31 then use nested algebras of this kind to construct translations that move operators across a horizon.

## 11. Problem set

### Classroom core

1. **Transfer isotony.** Write the two inclusions that the construction uses to show $\mathcal A_{\mathrm{bulk}}(W(D_1))\subset\mathcal A_{\mathrm{bulk}}(W(D_2))$.

2. **The wedge of a diamond.** Using the flat causal structure of the Poincaré chart, derive $W(D)$ for a diamond with tips $a$ and $b$, and show that its slice $t=0$ for $|x|<R$ is the half-disk $x^2+z^2<R^2$.

3. **Complementary arcs.** Show that the geodesics of an arc of half-width $\theta_0$ and of its complement coincide, and deduce $W(D')=W(D)'$.

4. **Locality transfer.** Show that the algebras of two causally disjoint bulk wedges commute, naming each property of the region map that you use.

5. **The three arcs.** Prove $\mathcal A_\partial(AB)\cap\mathcal A_\partial(BC)=\mathcal A_\partial(B)$ under Haag duality and strong additivity, and deduce that the triple intersection is trivial for factors.

6. **The boundary limit.** Derive $\lim(zz')^{-\Delta}G_\Delta=1/2\pi|x-x'|^{2\Delta}$ from the propagator of §6.

### Self-study consolidation

7. **Two qubits.** Prove that $(\mathcal B(\mathbb C^2)\otimes I)\cap(I\otimes\mathcal B(\mathbb C^2))=\mathbb C\,I$, and compute the dimensions of the pair intersections for three qubits.

8. **A smaller region.** Why is $O\mapsto\bigcap_{W\supset O}\mathcal A_{\mathrm{bulk}}(W)$ isotonous?

9. **Modular equality.** Rehren's bulk and boundary algebras have the same modular operator. Which hypothesis of §4 would fail if the bulk state were a thermal state of the global AdS Hamiltonian?

10. **The AdS$_3$ propagator.** Verify that $G_\Delta(\sigma)$ solves the radial Klein–Gordon equation with $m^2=\Delta(\Delta-2)$ and has the short-distance behavior of a unit source.

11. **Identify an overclaim.** Does Rehren's correspondence prove the Ryu–Takayanagi formula, or the smearing formula of Lecture 18? State what each would require in addition.

12. **The point at infinity.** At $t=0$ in the Poincaré chart, the causal complement of the half-disk $x^2+z^2<R^2$ contains points with arbitrarily large $z$. Which boundary region of the cylinder does it correspond to, and why does the Poincaré boundary not contain it as a single diamond?

### Research extension

13. **A compact-region algebra.** Choose a concrete boundary net, for instance the chiral current of Lecture 30 tensored with its antichiral partner, and decide whether the intersection algebra of a compact bulk region is trivial. *Known:* the proposition of §5 gives triviality under Haag duality, strong additivity and factoriality; generalized free fields violate strong additivity. *Completion:* the status of each hypothesis for the chosen net, with references, and the resulting intersection.

14. **Asymptotically AdS spacetimes.** Extend the region map to an asymptotically AdS$_3$ spacetime with a small perturbation of the metric. *Known:* Ribeiro extends Rehren's correspondence to a class of asymptotically AdS spacetimes of dimension greater than three and identifies which properties weaken; the three-dimensional case lies outside his class. *Completion:* the first-order change of the causal wedge of a diamond, and the property of §2 that fails first.

15. **An interacting bulk field.** Compute the tree-level three-point function of a cubically coupled bulk scalar in AdS$_3$ and its boundary limit. *Known:* Dütsch and Rehren show that the dual correlation functions are boundary limits of bulk correlation functions. *Completion:* the boundary three-point coefficient as a limit of the bulk Feynman integral, compared with the Witten-diagram result.

## 12. Answer checkpoints

1. First $D_1\subset D_2\Rightarrow W(D_1)\subset W(D_2)$ geometrically; then $\mathcal A_\partial(D_1)\subset\mathcal A_\partial(D_2)$ by isotony of the boundary net.

2. A bulk point is in the chronological future of $a$ when $-(x^+-a^+)(x^--a^-)+z^2<0$ and $x^+>a^+$; similarly for the past of $b$. At $t=0$, $x^\pm=\pm x$ and $a^\pm=-R$, $b^\pm=R$ give $(R+x)(R-x)>z^2$.

3. Under $\theta\to\theta+\pi$ and $\theta_0\to\pi-\theta_0$ the equation $\tanh\rho\cos\theta=\cos\theta_0$ becomes $-\tanh\rho\cos\theta=-\cos\theta_0$. The two bulk regions are the two sides of one curve on a Cauchy slice, and complementary regions of a Cauchy slice have causally complementary domains of dependence.

4. If $W(D_1)\subset W(D_2)'$, then $W(D_1)\subset W(D_2')$ by the complement property, and taking the boundary trace gives $D_1\subset D_2'$. Boundary locality then gives commutation.

5. $\mathcal A(C)'\cap\mathcal A(A)'=(\mathcal A(C)\vee\mathcal A(A))'=\mathcal A(CA)'=\mathcal A(B)$. Then $\mathcal A(B)\cap\mathcal A(CA)=\mathcal A(B)\cap\mathcal A(B)'=\mathbb C\,1$ for a factor.

6. Near the boundary $\sinh\sigma\simeq\frac12e^{\sigma}$, so $G\simeq\frac1{2\pi}e^{-\Delta\sigma}$, and $e^{-\sigma}\simeq1/(2\cosh\sigma)\simeq zz'/|x-x'|^2$. Thus $(zz')^{-\Delta}G\to\frac1{2\pi}|x-x'|^{-2\Delta}$.

7. An operator in both factors commutes with $\mathcal B(\mathbb C^2)\otimes I$ and $I\otimes\mathcal B(\mathbb C^2)$, which generate $\mathcal B(\mathbb C^4)$, so it is a scalar. For three qubits the pair intersection is $I\otimes\mathcal B(\mathbb C^2)\otimes I$, of dimension four, and the triple intersection has dimension one.

8. If $O_1\subset O_2$, every wedge containing $O_2$ contains $O_1$, so the intersection for $O_1$ runs over more algebras and is smaller.

9. The modular group of a wedge is geometric in the vacuum; in a thermal state of the global Hamiltonian the vector is different, and the theorem of Brunetti, Guido and Longo, which concerns the vacuum, no longer identifies the modular flow with a boost.

10. With $G=e^{-(\Delta-1)\sigma}/4\pi\sinh\sigma$, the combination $G''+2\coth\sigma\,G'-\Delta(\Delta-2)G$ vanishes identically, and $4\pi\sigma G\to1$ as $\sigma\to0$.

11. Neither. The Ryu–Takayanagi formula needs a gravitational entropy functional and its normalization by Newton's constant; the smearing formula needs a specific bulk field equation and a choice of kernel. Rehren's map supplies neither.

12. The complement of the half-disk is the wedge of the complementary arc of the cylinder, which contains the point at spatial infinity of the Poincaré boundary. On the Poincaré boundary its trace is the disconnected region $|x|>R$, whose two pieces are joined only through that point.

**Wiki connections.** [[haag-kastler-axioms|Haag–Kastler axioms]] · [[bisognano-wichmann-theorem|Bisognano–Wichmann theorem]] · [[subregion-subalgebra-duality|subregion–subalgebra duality]]
