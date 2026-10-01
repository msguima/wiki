---
title: "Lecture 31 — An algebraic model of emergent time"
type: lecture-notes
edition: "2.2 — rewritten at the AQFT standard"
lecture: 31
semester: 2
week: 14
hours: 3
prerequisites: "Lectures 23, 25, 29 and 30; Kruskal coordinates, the Hartle–Hawking state and half-sided modular inclusions"
status: "rewritten 2026-09-30, pending instructor review; the action of boundary time on Kruskal coordinates, the boundary algebras of the outgoing sector, their modular flows, the half-sided inclusion of the band of earlier times, the product of modular unitaries and the Kruskal translation across the future horizon, the second sector with the two-dimensional translation group, and the thermal flux of the Hartle–Hawking state are exact calculations in the JT model of Lecture 25; the obstruction at finite N follows from Borchers' theorem of Lecture 30; the proposal of Leutheusser and Liu, the type II algebras of JT gravity and the observer algebras are stated with sources"
modified: 2026-09-30
---

# Lecture 31 — An algebraic model of emergent time

> *The Hamiltonian of a boundary moves operators along the Killing time of the black hole, and the Killing time stops at the horizon: every orbit approaches it and none crosses. Leutheusser and Liu proposed in 2021 that at large $N$ the boundary theory nevertheless contains time evolutions that cross the horizon, built from the modular operators of two boundary algebras, the algebra of all times and the algebra of the times before a given instant. This lecture constructs the proposal exactly in the JT model of Lecture 25, for the outgoing sector of the matter, which in the Hartle–Hawking state is a chiral field in its vacuum on the Kruskal coordinate $w^-$. The right boundary at all times sees the half-line $w^-<0$, the band of earlier times sees a smaller half-line, the inclusion is half-sided, and the translation of Lecture 30 is the Kruskal translation, which carries boundary operators across the future horizon into the interior. With the ingoing sector the construction recovers the translations of the whole Kruskal plane. We close with what has emerged, a null and a timelike direction and the causal structure near the horizon, and with what has not, proper time, the metric, and anything at finite $N$, where the boundary algebra is of type I and the structure cannot exist.*

## How to use this lecture

**Classroom core, one meeting of three hours.** The history (§1, 10 minutes), the Killing clock at the horizon (§2, 15 minutes), and the outgoing sector with its two boundary algebras (§3, 25 minutes) come before a 10-minute break. After it come the translation that crosses the horizon (§4, 35 minutes), the second sector and the Kruskal plane (§5, 20 minutes), and what the model establishes (§6, 25 minutes), with 40 minutes for Checkpoints 1 and 2 and Problems 4–6; Problems 1–3 complete the core assignment. These allocations are proposals and have not been tested in class.

**Self-study.** Finite $N$ and the crossed product (§7), observers and their clocks (§8), and Problems 7–12, including the ingoing sector, the thermal flux of the Hartle–Hawking state and the finite-$N$ obstruction.

**Research extension.** Excited states, the gravitational dressing of the JT model, and the evaporating black hole, in Problems 13–15.

**Prerequisites.** Lecture 23 for the thermofield double and its modular flow, Lecture 25 for the JT model with its bath, its Kruskal coordinates and the Hartle–Hawking state, Lecture 29 for the type of large-$N$ algebras, Lecture 30 for the chiral current and the theorems of Borchers and Wiesbrock. Kruskal coordinates and the Schwarzian transformation of a stress tensor.

**What this lecture establishes.** In the JT model of Lecture 25, the action of boundary time on Kruskal coordinates, the identification of the boundary algebras of the outgoing sector with half-lines of $w^-$, their modular flows, the half-sided inclusion of the band of earlier times, the product of modular unitaries, the Kruskal translation across the future horizon, the second sector with its two-dimensional translation group, and the thermal flux of the Hartle–Hawking state are exact calculations. That no such structure exists when the boundary algebra is a type I factor in a faithful normal state follows from Borchers' theorem of Lecture 30. The proposal of Leutheusser and Liu for large-$N$ theories, the type II algebras of JT gravity and the algebras of observers are stated with sources.

## 0. Reading

**Primary.**

- S. Leutheusser, H. Liu, [Emergent times in holographic duality](https://arxiv.org/abs/2112.12156) (2021).
- S. Leutheusser, H. Liu, [Causal connectability between quantum systems and the black hole interior in holographic duality](https://arxiv.org/abs/2110.05497) (2021).

**Secondary.**

- G. Penington, E. Witten, [Algebras and States in JT Gravity](https://arxiv.org/abs/2301.07257) (2023).
- E. Witten, [Gravity and the Crossed Product](https://arxiv.org/abs/2112.12828) (2021).
- B. S. Kay, R. M. Wald, "Theorems on the uniqueness and thermal properties of stationary, nonsingular, quasifree states on spacetimes with a bifurcate Killing horizon," *Phys. Rep.* 207 (1991) 49.

**Optional research reading.**

- V. Chandrasekaran, R. Longo, G. Penington, E. Witten, [An Algebra of Observables for de Sitter Space](https://arxiv.org/abs/2206.10780) (2022).
- E. Witten, [Algebras, Regions, and Observers](https://arxiv.org/abs/2303.02837) (2023).
- V. Chandrasekaran, G. Penington, E. Witten, [Large N algebras and generalized entropy](https://arxiv.org/abs/2209.10454) (2022).
- H. Liu, [Lectures on entanglement, von Neumann algebras, and emergence of spacetime](https://arxiv.org/abs/2510.07017) (2025), sections IV.5 and VIII.

## 1. Can a boundary clock run past the horizon?

Kruskal and Szekeres found in 1960 coordinates in which the Schwarzschild metric is regular across the horizon, and in which the Killing time of the exterior is a boost of the Kruskal plane. An observer at fixed radius measures the Killing time, and an infalling observer crosses the horizon at a finite proper time while the Killing time diverges. In 1976 Unruh, and Hartle and Hawking, studied the states of quantum fields that are regular at the horizon, defined as vacua with respect to Kruskal coordinates. Kay and Wald proved in 1991 that a stationary quasifree state regular on a bifurcate Killing horizon is unique and thermal at the Hawking temperature. The modular flow of the exterior in that state is the Killing flow, as in Lecture 23.

In holography the Killing time is the time of the boundary, and the boundary Hamiltonian generates it. Every boundary operator evolved by it stays outside the horizon, which made the description of the interior from the boundary a long-standing question, approached by Papadodimas and Raju through state-dependent mirror operators (Lecture 29). Leutheusser and Liu proposed in 2021 a different answer. At infinite $N$ the algebra of single-trace operators of one boundary is of type III$_1$, the algebra of the times after a given instant, or before it, is a proper subalgebra, and the inclusion is half-sided. Wiesbrock's theorem of Lecture 30 then produces a new one-parameter group, with positive generator, that is not generated by the boundary Hamiltonian and moves operators across the horizon. They called such groups emergent times. Witten showed in the same year that $1/N$ corrections turn the algebra into a crossed product of type II$_\infty$, and Chandrasekaran, Longo, Penington and Witten related a similar algebra to the clock of an observer in de Sitter space. Penington and Witten found in 2023 that the algebra of boundary observables of JT gravity with matter is of type II$_\infty$.

This lecture builds the proposal in the one model of the course where every step can be computed, the outgoing sector of the matter in the JT model of Lecture 25.

## 2. The Killing clock stops at the horizon

Recall the Kruskal coordinates of Lecture 25, §4. On the right exterior, with the boundary at $\sigma\to0^-$ and the bath at $\sigma>0$,

$$
w^+=e^{t+\sigma},\qquad w^-=-e^{\sigma-t},\qquad ds^2=-\frac{4\,dw^+dw^-}{(1+w^+w^-)^2},
$$

the future horizon is $w^-=0$, the past horizon $w^+=0$, and the left exterior has $w^+<0<w^-$, with $w^+=-e^{\sigma-t}$ and $w^-=e^{\sigma+t}$. A translation of the boundary time by $\tau$ acts as

$$
w^+\longmapsto e^{\tau}w^+,\qquad w^-\longmapsto e^{-\tau}w^- ,
$$

the boost of the Kruskal plane. [Exact.] A point of the right exterior approaches $w^-=0$ as $\tau\to\infty$ and never reaches it: multiplication by a positive number does not change the sign of $w^-$. An infalling light ray, at fixed $w^+$, crosses $w^-=0$ at a finite value of its affine parameter, which near the horizon is proportional to $w^-$. The boundary clock and the infalling clock agree outside up to a reparametrization that diverges at the horizon.

The thermofield double of the two boundaries is the Hartle–Hawking state, the vacuum of the matter in the coordinates $w^\pm$ (Lecture 25, §5), thermal at $\beta=2\pi$. Its modular flow for the right exterior is the boost, by Lecture 23. So the modular clock of the right boundary is the Killing clock, and it stops at the horizon.

## 3. The outgoing sector and two boundary algebras

Let the matter contain a free boson. Its right-moving current $j(w^-)$, a function of $w^-$ alone, is the chiral current of Lecture 30, §3, with $u=w^-$. In the Hartle–Hawking state it is in its vacuum on the whole $w^-$ line, since the matter state is the vacuum of the flat coordinates $w^\pm$ and the Weyl factor of the metric changes neither the algebra nor the state. A line of constant $w^-<0$ runs through the right exterior and leaves through the boundary into the right bath, so the right-moving modes are outgoing on the right. A line of constant $w^->0$ comes in from the left bath through the left exterior and continues into the future interior.

At the right boundary, $\sigma=0$, the outgoing field at time $t$ is the chiral field at $w^-=-e^{-t}$. A band of boundary times $t_1<t<t_2$ therefore generates the algebra of the interval $(-e^{-t_1},-e^{-t_2})$ of the chiral current. Two such algebras are the subject of the lecture:

$$
\mathcal M=\mathcal A_{\mathrm{out}}\bigl((-\infty,0)\bigr),\qquad \mathcal N=\mathcal A_{\mathrm{out}}\bigl((-\infty,-b)\bigr),\qquad b=e^{-t_0},
$$

the outgoing operators of the right boundary at all times and at the times before $t_0$. [Exact.] Within the outgoing sector, Haag duality for the chiral current gives $\mathcal M'=\mathcal A_{\mathrm{out}}((0,\infty))$, the right-movers of the left exterior and the interior.

The modular flow of $\mathcal M$ follows from Lecture 30. The flow of $\mathcal A((0,\infty))$ is the dilation $w\mapsto e^{2\pi s}w$, and since $\mathcal M$ is its commutant, $\Delta_{\mathcal M}=\Delta_{\mathcal M'}^{-1}$ and

$$
\Delta_{\mathcal M}^{-is}:\ w^-\longmapsto e^{-2\pi s}w^- ,
$$

which by §2 is the forward boundary time translation by $\tau=2\pi s$. [Proved.] The modular flow of $\mathcal N$ is the dilation about $-b$, since $\mathcal N=U(-b)\,\mathcal M\,U(-b)^\dagger$ for the translation $U(a)$ of $w^-$, which fixes the vacuum. The flow of $\mathcal M$ moves the edge of $\mathcal N$ from $-b$ to $-be^{-2\pi s}$, so that

$$
\Delta_{\mathcal M}^{-is}\,\mathcal N\,\Delta_{\mathcal M}^{is}=\mathcal A_{\mathrm{out}}\bigl((-\infty,-be^{-2\pi s})\bigr)\subset\mathcal N\qquad\text{for }s\leq0 .
$$

[Exact.] Evolving backward in boundary time pushes the band of earlier times into itself, and evolving forward does not. The inclusion is half-sided, with the opposite sign to the statement of Lecture 30, §4, which is the same theorem applied to the reflected line.

**Checkpoint 1.** Which boundary times does the interval $(-e^{-t_1},-e^{-t_2})$ of $w^-$ describe, and why is the algebra of a finite band a proper subalgebra of the algebra of all times?

**Answer.** The times $t_1<t<t_2$, since $w^-=-e^{-t}$ increases with $t$. The outgoing operators of the band are the chiral field on that interval, and the field on the rest of the half-line, which crosses the boundary at other times, commutes with them and is not generated by them. The outgoing sector has no dynamics that would relate different values of $w^-$, so no finite band determines the rest.

## 4. The translation that crosses the horizon

Apply Wiesbrock's theorem, in the reflected form. It produces the translation group $U(a)=e^{iaP}$ of the $w^-$ line, with $P\geq0$ the generator of Kruskal translations of the outgoing sector, $U(a)\,\mathcal M\,U(a)^\dagger=\mathcal A_{\mathrm{out}}((-\infty,a))\subset\mathcal M$ for $a\leq0$, and $\mathcal N=U(-b)\,\mathcal M\,U(-b)^\dagger$. The product of the two modular unitaries is computed as in Lecture 30, §3. An operator at $w$ is moved by $\Delta_{\mathcal N}^{is}$ to $-b+e^{2\pi s}(w+b)$ and then by $\Delta_{\mathcal M}^{-is}$ to $w+b(1-e^{-2\pi s})$, so

$$
\Delta_{\mathcal M}^{-is}\,\Delta_{\mathcal N}^{is}=U\bigl(b\,(1-e^{-2\pi s})\bigr),\qquad \hat K_{\mathcal M}-\hat K_{\mathcal N}=2\pi b\,P .
$$

[Exact calculation, checked in the course scripts.] The two operators on the left are boundary objects, modular operators of two algebras of boundary operators in the boundary state. The translation is therefore defined by boundary data alone, and it is not a function of the boundary Hamiltonian.

Now follow an operator. An outgoing operator of the right boundary at time $t_1$ sits at $w^-=-e^{-t_1}$, and $U(a)$ moves it to $w^-=a-e^{-t_1}$. For $a<e^{-t_1}$ it is still a boundary operator, at the time

$$
t_1'=-\log\bigl(e^{-t_1}-a\bigr),
$$

a reparametrization of boundary time that reaches $t_1'=\infty$ at $a=e^{-t_1}$. For $a>e^{-t_1}$ it has crossed the future horizon: it sits at $w^->0$, on a null line through the future interior, and it belongs to $\mathcal M'$, outside the algebra of the right boundary. [Exact.] The figure shows the band of times before $t_0$, the null line $w^-=-e^{-t_0}$ that bounds its outgoing sector, and the same edge after a translation with $a>e^{-t_0}$.

![[ads-cft-emergent-time.svg|Penrose diagram of the two-sided JT black hole with a bath on each side. On the right boundary the band of times before t0 is marked, and the outgoing null line w minus equal to minus e to the minus t0, through the boundary at t0, bounds the region of the outgoing modes of the band, shaded below it. After a Kruskal translation by a, the same edge has moved to the null line w minus equal to a minus e to the minus t0, which crosses the future horizon w minus equal to zero and runs through the future interior and the left exterior; the region swept by the translation is shaded, and an arrow shows the direction of the motion.]]

Two features of the formula deserve attention. The products of modular unitaries alone give $a=b(1-e^{-2\pi s})<b$, so they move the edge of $\mathcal N$ up to the horizon only in the limit $s\to\infty$, while they already move the edge of $\mathcal M$ to $a>0$ for every $s>0$. And translations by $a\geq b$, which carry the whole band across, are obtained from the group law, $U(a)=U(a/n)^n$; the group extends the products beyond the range $a<b$ that they cover.

> **Physical picture: an infalling clock assembled from two exterior clocks.** The clock of the right boundary is the boost, which slows to a halt at the horizon. The band of earlier times has a clock of its own, the boost about the point where its last outgoing ray leaves the boundary. Running the two clocks against each other cancels the boosts and leaves the Kruskal translation, which has no fixed point at the horizon and carries outgoing operators through it. Neither exterior clock crosses, and the clock of an observer who does is built from both.

**Checkpoint 2.** Why can no product $\Delta_{\mathcal M}^{-is}\Delta_{\mathcal N}^{is}$ move an operator of the band across the horizon, while such products move operators of $\mathcal M$ across?

**Answer.** The product is $U(a)$ with $a=b(1-e^{-2\pi s})<b$. An operator of the band sits at $w^-<-b$ and moves to $w^-<a-b<0$. An operator of $\mathcal M$ near the horizon, at $w^-=-\epsilon$ with $\epsilon<a$, moves to $w^->0$. Larger translations require the group law.

## 5. The second sector and the Kruskal plane

The left-moving current $\bar{\jmath}(w^+)$ is the ingoing sector on the right: at the boundary $w^+=e^t$, and lines of constant $w^+>0$ run from the bath through the boundary into the right exterior and the future interior. The ingoing operators of the right boundary at all times generate $\mathcal A_{\mathrm{in}}((0,\infty))$, and those at times after $t_0$ generate $\mathcal A_{\mathrm{in}}((e^{t_0},\infty))$. The modular flow of the larger algebra is $w^+\mapsto e^{2\pi s}w^+$, forward time translation again, and it compresses the later band for $s\geq0$. This is the orientation of Lecture 30, §4 without reflection, and Wiesbrock's theorem gives the translations $U_+(a)$ of $w^+$, with positive generator $P_+$, which move ingoing operators of the right boundary backward across the past horizon $w^+=0$. [Exact.]

The two sectors together generate the algebra $\mathcal M_R=\mathcal A_{\mathrm{in}}((0,\infty))\vee\mathcal A_{\mathrm{out}}((-\infty,0))$ of the right exterior wedge $\{w^+>0,\ w^-<0\}$ of the matter. The translations $U_+(a_+)$ and $U_-(a_-)=U(a_-)$ commute, have positive generators, fix the vacuum, and map $\mathcal M_R$ into itself when $a_+\geq0\geq a_-$. They form the translation group of a two-dimensional Minkowski space with null coordinates $w^\pm$, and $\mathcal M_R$ is the algebra of a wedge in it, whose modular group is the boost $w^\pm\mapsto e^{\pm2\pi s}w^\pm$, as Borchers' theorem requires. [Exact.] Borchers observed that two commuting half-sided translations of opposite signs always define a Poincaré-covariant net of this kind on two-dimensional Minkowski space, with double cones obtained as intersections of translated wedges, although it is not known in general whether the vacuum is cyclic for the double-cone algebras, which may also fail weak additivity. [Stated only — refs: Borchers 2000, section II.7.]

The timelike translation $U_+(a)U_-(a)$, with positive generator $P_++P_-$, moves the edge of the right wedge from the bifurcation point $w^\pm=0$ to $w^\pm=a$, which for $a>0$ lies in the future interior. The algebra of the right exterior is carried to the algebra of a wedge whose edge is behind the horizon. The two boundary sectors, their bands of earlier and later times, and the Hartle–Hawking state determine in this way the translations of the whole Kruskal plane.

## 6. What the model establishes

Three things have emerged from boundary data in the model, and each comes with a qualification.

A null direction and a parameter along it, the Kruskal coordinate $w^-$ of the outgoing sector, emerge from the inclusion of §3. The coordinate $w^-$ is affine for the flat metric $-dw^+dw^-$ of the matter; for the JT metric the affine parameter along a line of constant $w^+$ obeys $d\lambda\propto(1+w^+w^-)^{-2}dw^-$, so $w^-$ is affine only on the horizon $w^+=0$ and approximately near $w^+w^-=0$. The Kruskal translation is an automorphism of the matter algebra that preserves the state and acts geometrically. It is a symmetry of the conformal matter in its state; the conformal factor $(1+w^+w^-)^{-2}$ of the JT metric changes under $w^\pm\to w^\pm+a$ (Problem 9), so the translation is not an isometry. What emerges is therefore the conformal structure of the Kruskal plane, its null directions and its causal order, and the proper time of an infalling observer, which needs the conformal factor, is not determined.

The model is exact at $G_N\to0$, with the geometry fixed and the matter free, which is the analogue of infinite $N$. For a holographic boundary theory at finite $N$ the structure cannot exist. The algebra of one boundary is then $\mathcal B(\mathcal H)$, of type I, with the boundary Hamiltonian in it, and by the time-slice property of Lecture 29, §7, the band of earlier times generates the same algebra, so the inclusion is trivial. More generally, a type I factor in a faithful normal state admits no nontrivial half-sided translation: its modular operator has a complete set of eigenvectors, and the dilation law of Borchers' theorem forces every half-sided translation to fix each of them (Problem 11); Lecture 30, §5, is the finite-dimensional case. [Proved, given Borchers' theorem and the time-slice property.] In JT gravity quantized exactly the boundary algebra is of type II$_\infty$ (§7), and the type III$_1$ theorem of Lecture 30, §4, excludes there a half-sided translation with a unique invariant vector. This is the algebraic form of the claim of Leutheusser and Liu that a sharp horizon, and the time evolutions that cross it, emerge only in the limit. [Stated only — refs: Leutheusser–Liu 2021.]

The construction depends on the state. It used the Hartle–Hawking state, in which the modular operators of the two bands are geometric. For a state with finitely many excitations the modular operators change, and the relative modular operators and the Connes cocycle of the AQFT course relate the two descriptions; whether the inclusion stays half-sided is a property of the state (Problem 13). In the holographic proposal of Leutheusser and Liu the same three steps are taken in the large-$N$ algebra of single-trace operators of Lecture 29, with the bulk identification supplied by the reconstruction of Lectures 18–21. [Stated only — refs: Leutheusser–Liu 2021.]

## 7. Self-study: finite $N$ and the crossed product

Witten observed that at order $1/N$ the boundary Hamiltonian, which at infinite $N$ becomes central after subtracting its expectation value and rescaling, rejoins the algebra of single-trace operators. The resulting algebra is the crossed product of the type III$_1$ algebra by its modular group, of type II$_\infty$, with a trace and density matrices whose entropies are generalized entropies up to a constant. [Stated only — refs: Witten 2021; Chandrasekaran–Penington–Witten 2022.] In JT gravity with matter, quantized exactly, Penington and Witten found that the algebra of observables of one boundary, which contains its Hamiltonian, is a factor of type II$_\infty$. [Stated only — refs: Penington–Witten 2023.]

The proposition of Lecture 29, §5 allows decaying correlators in type II$_\infty$, and the theorems of Lecture 30 allow half-sided translations with a unique invariant vector only in type III$_1$. The emergent times of this lecture therefore live in the type III$_1$ algebra and do not survive unchanged in the crossed product; how they are modified by the gravitational dressing is Problem 14.

## 8. Self-study: observers and their clocks

Chandrasekaran, Longo, Penington and Witten described the static patch of de Sitter space by the algebra of operators dressed to the worldline of an observer, who carries a clock. The algebra is of type II$_1$, and its maximum-entropy state is empty de Sitter space. [Stated only — refs: Chandrasekaran–Longo–Penington–Witten 2022.] Witten then argued that the algebra along the worldline of an observer is a good substitute for the algebra of a region when gravity is present, using the timelike tube theorem of quantum field theory. [Stated only — refs: Witten 2023.] In both constructions a clock is part of the observable algebra. In the construction of this lecture the clock is assembled from the modular structure of two algebras that an exterior observer already has, and the comparison of the two notions is open.

## 9. What to take away

- **Exact:** boundary time acts on the Kruskal coordinates as the boost $w^\pm\mapsto e^{\pm\tau}w^\pm$ and never moves a point across $w^-=0$.
- **Exact, in the JT model:** the outgoing operators of the right boundary at all times and at times before $t_0$ generate the chiral algebras of $(-\infty,0)$ and $(-\infty,-e^{-t_0})$; the modular flow of the first is forward time translation, and it compresses the second for $s\leq0$.
- **Exact:** $\Delta_{\mathcal M}^{-is}\Delta_{\mathcal N}^{is}=U(b(1-e^{-2\pi s}))$ and $\hat K_{\mathcal M}-\hat K_{\mathcal N}=2\pi bP$; the Kruskal translation, built from boundary modular data, moves outgoing operators across the future horizon.
- **Exact:** with the ingoing sector, two commuting half-sided translations of opposite signs give the translations of the Kruskal plane, and a timelike translation moves the edge of the exterior wedge into the future interior.
- **Proved, given Borchers' theorem:** no such structure exists in a type I factor in a faithful normal state, so the construction requires infinite $N$; what emerges is the conformal structure of the Kruskal plane, and proper time does not.

## 10. Looking ahead

Lecture 32 closes the course by retracing the chain from a recoverable observable in a finite code to the algebras of this lecture, and by sorting the claims of the semester by their status.

## 11. Problem set

### Classroom core

1. **Boundary time on Kruskal coordinates.** Show that $t\to t+\tau$ acts as $w^\pm\to e^{\pm\tau}w^\pm$ on the right exterior, and that no finite $\tau$ moves a point across $w^-=0$.

2. **Boundary bands.** Identify the intervals of $w^-$ generated by the outgoing operators of the right boundary at all times, at times before $t_0$, and at times in $(t_1,t_2)$.

3. **The modular flow of a past half-line.** Using $\mathcal A((-\infty,0))=\mathcal A((0,\infty))'$ and $\Delta_{\mathcal M'}=\Delta_{\mathcal M}^{-1}$, show that the modular flow of $\mathcal A((-\infty,0))$ is $w\mapsto e^{-2\pi s}w$, and identify it with boundary time translation.

4. **A half-sided inclusion.** Show that $\Delta_{\mathcal M}^{-is}\mathcal N\Delta_{\mathcal M}^{is}\subset\mathcal N$ exactly for $s\leq0$, and that $\mathcal N=U(-b)\mathcal MU(-b)^\dagger$.

5. **The product of modular unitaries.** Compute $\Delta_{\mathcal M}^{-is}\Delta_{\mathcal N}^{is}$ by following the localization of an operator, find the range of translations it produces, and derive $\hat K_{\mathcal M}-\hat K_{\mathcal N}=2\pi bP$.

6. **Crossing the horizon.** For an outgoing operator of the right boundary at time $t_1$, find the translations that keep it on the boundary and the boundary time at which it then sits, and the translations that move it into the future interior.

### Self-study consolidation

7. **The ingoing sector.** Show that the ingoing operators of the right boundary at times after $t_0$ generate $\mathcal A_{\mathrm{in}}((e^{t_0},\infty))$, that the modular flow of $\mathcal A_{\mathrm{in}}((0,\infty))$ compresses it for $s\geq0$, and that the resulting translations move ingoing operators across the past horizon.

8. **Two translations.** Show that $U_+(a_+)U_-(a_-)$ maps the right wedge algebra into itself when $a_+\geq0\geq a_-$, and find the image of the bifurcation point under the timelike translation with $a_+=a_-=a$.

9. **Not an isometry.** Show that $w^\pm\to w^\pm+a$ does not preserve the metric $-4\,dw^+dw^-/(1+w^+w^-)^2$, and that it preserves the vacuum of the matter in the coordinates $w^\pm$.

10. **A thermal flux from a vacuum.** With $w^-=-e^{-u}$, $u=t-\sigma$, and $T_{w^-w^-}=0$ in the Hartle–Hawking state, use $T_{uu}=(\partial_uw^-)^2T_{w^-w^-}-\frac c{24\pi}\{w^-,u\}$ to show that the outgoing flux in boundary time is $c/48\pi$, thermal at $\beta=2\pi$.

11. **The finite-$N$ obstruction.** Suppose the algebra of one boundary is a type I factor $\mathcal M$ in a faithful normal state, and $U(a)$ is a half-sided translation of $\mathcal M$: positive generator, $U(a)\Omega=\Omega$, and $U(a)\mathcal MU(a)^\dagger\subset\mathcal M$ for $a\geq0$. Using Borchers' theorem of Lecture 30, §4, and the eigenvectors of $\Delta$, show that $U(a)=1$.

12. **Classify the claims.** Decide which of the following hold in the model, and why: the boundary Hamiltonian evolves operators into the interior; the construction gives the proper time of an infalling observer; the construction uses only boundary data; the construction works at finite $N$.

### Research extension

13. **Excited states.** *Known:* relative modular flow and the Connes cocycle relate the modular operators of two faithful states; Leutheusser and Liu discuss the dependence of emergent times on the state. *Completion:* for a coherent state of the outgoing current, the modular operators of $\mathcal M$ and $\mathcal N$, a decision whether the inclusion remains half-sided, and the resulting translation if it does.

14. **Gravitational dressing.** *Known:* Penington and Witten show that the boundary algebra of JT gravity with matter is of type II$_\infty$, with the Hamiltonians included. *Completion:* the fate of the half-sided inclusion of §3 when the boundary particle is quantized, and the operator that obstructs it.

15. **An evaporating black hole.** *Known:* in the evaporating model of Lecture 25, §8, the state is not the Hartle–Hawking state, and the outgoing sector is in the vacuum of a different coordinate. *Completion:* the modular flow of the band algebras in that state, whether the inclusion is half-sided, and the coordinate that the resulting translation moves.

## 12. Answer checkpoints

1. $w^+=e^{t+\sigma}\to e^{\tau}w^+$ and $w^-=-e^{\sigma-t}\to e^{-\tau}w^-$. Multiplying $w^-<0$ by $e^{-\tau}>0$ keeps it negative.

2. With $w^-=-e^{-t}$ at the boundary: all times give $(-\infty,0)$, times before $t_0$ give $(-\infty,-e^{-t_0})$, and times in $(t_1,t_2)$ give $(-e^{-t_1},-e^{-t_2})$.

3. $\Delta_{\mathcal M}^{-is}=\Delta_{\mathcal M'}^{is}=D(-s)$, the dilation $w\mapsto e^{-2\pi s}w$. On the boundary $w^-=-e^{-t}\mapsto-e^{-t-2\pi s}$, which is $t\mapsto t+2\pi s$.

4. The image of $(-\infty,-b)$ is $(-\infty,-be^{-2\pi s})$, contained in $(-\infty,-b)$ exactly when $be^{-2\pi s}\geq b$, that is $s\leq0$. Translating $(-\infty,0)$ by $-b$ gives $(-\infty,-b)$, and $U(-b)$ fixes the vacuum.

5. The localization moves as $w\mapsto-b+e^{2\pi s}(w+b)\mapsto w+b(1-e^{-2\pi s})$, so the product is $U(b(1-e^{-2\pi s}))$, with range $(-\infty,b)$. Differentiating at $s=0$ gives $\hat K_{\mathcal M}-\hat K_{\mathcal N}=2\pi bP$, since $b(1-e^{-2\pi s})\simeq2\pi bs$.

6. The operator moves to $w^-=a-e^{-t_1}$. For $a<e^{-t_1}$ it sits on the boundary at $t_1'=-\log(e^{-t_1}-a)$; for $a>e^{-t_1}$ it is at $w^->0$, in the future interior.

7. At the boundary $w^+=e^t$, so $t>t_0$ gives $(e^{t_0},\infty)$. The flow $w^+\mapsto e^{2\pi s}w^+$ maps it to $(e^{t_0+2\pi s},\infty)$, contained in it for $s\geq0$. The translations are $w^+\to w^++a$, and for $a<-w^+$ an operator crosses $w^+=0$.

8. The wedge $\{w^+>0,\ w^-<0\}$ is mapped to $\{w^+>a_+,\ w^-<a_-\}$, inside it when $a_+\geq0\geq a_-$. The bifurcation point goes to $w^\pm=a$, in the future interior for $a>0$.

9. The factor $(1+w^+w^-)^{-2}$ becomes $(1+(w^++a)(w^-+a))^{-2}$, which differs unless $a=0$, while $dw^+dw^-$ is unchanged. The matter state is the vacuum of the flat metric $-dw^+dw^-$, which is invariant under translations.

10. $\{w^-,u\}=\partial_u^3w^-/\partial_uw^--\frac32(\partial_u^2w^-/\partial_uw^-)^2=1-\frac32=-\frac12$, so $T_{uu}=c/48\pi$, the flux of a thermal chiral field at $\beta=2\pi$.

11. If $\Delta\psi=\lambda\psi$, then $\langle\psi,U(e^{2\pi s}a)\psi\rangle=\langle\psi,\Delta^{-is}U(a)\Delta^{is}\psi\rangle=\langle\psi,U(a)\psi\rangle$ for every $s$. The function is constant on each half-line and, by continuity at $a=0$, equals $\|\psi\|^2$, so $U(a)\psi=\psi$. The eigenvectors of $\Delta=\rho\otimes\bar{\rho}^{-1}$ span the Hilbert space, and $U(a)=1$.

12. The boundary Hamiltonian does not: it generates the boost. Proper time is not determined, since the conformal factor does not emerge. The construction uses only boundary data, the two band algebras and the state. It does not work at finite $N$, by Problem 11.

**Wiki connections.** [[jt-gravity|JT gravity]] · [[crossed-product-construction|crossed product]] · [[thermofield-double-state|thermofield double]]
