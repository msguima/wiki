---
title: "Lecture 25 — A specified JT gravity and bath model"
type: lecture-notes
edition: "2.2 — rewritten at the AQFT standard"
lecture: 25
semester: 2
week: 8
hours: 3
prerequisites: "Lectures 16, 23 and 24; the variation of a two-dimensional action and the Weyl factor of an entanglement entropy"
status: "rewritten 2026-09-30, pending instructor review; the JT equations from the action, the Schwarzian boundary action and its thermodynamics, the zero-temperature and thermal solutions, the Kruskal and Euclidean welding maps, and the generalized-entropy functional are exact calculations; the transparent coupling and the matter state are specified as the model; the island rule, the one-loop exactness of the Schwarzian and the evaporating model are stated with sources"
modified: 2026-09-30
---

# Lecture 25 — A specified JT gravity and bath model

> *To compute the entropy of Hawking radiation we need a gravitational system simple enough to solve and rich enough to have a black hole, a horizon and radiation that leaves it. Jackiw–Teitelboim gravity in two dimensions is such a system. Its metric is fixed to be AdS$_2$, and all its dynamics lies in a dilaton, whose value at a point plays the role of the horizon area, and in the shape of the boundary, whose action is the Schwarzian derivative. This lecture derives the equations of the theory from its action, reduces the boundary dynamics to the Schwarzian, and obtains the thermodynamics of the black hole from it. We then couple the gravitational region to a flat bath with the same conformal matter, with transparent boundary conditions, and show that the Euclidean geometry of the equilibrium state is conformal to the plane, so that the matter state is known exactly. Finally we specify the entropy to be computed, that of the radiation collected in the bath, and derive the generalized-entropy functional of a candidate island at zero temperature. Lecture 26 extremizes it.*

## How to use this lecture

**Classroom core, one meeting of three hours.** The history (§1, 10 minutes), the action and the equations (§2, 30 minutes), and the boundary and the Schwarzian (§3, 25 minutes) come before a 10-minute break. After it come the thermal solution and its two sides (§4, 20 minutes), the bath and the welding (§5, 25 minutes), and the entropy to be computed with its generalized-entropy functional (§6, 30 minutes), with 30 minutes for Checkpoints 1 and 2 and Problems 4–6; Problems 1–3 complete the core assignment. These allocations are proposals and have not been tested in class.

**Self-study.** The no-island entropy of the two-sided equilibrium state (§7), the evaporating model (§8), and Problems 7–12, including the Gauss–Bonnet term, the expansion of the extrinsic curvature, the Möbius invariance of the Schwarzian and the Kruskal form of the solution.

**Research extension.** The evaporating black hole and its energy balance, the Schwarzian density of states, and the stress tensor of the Hartle–Hawking and Boulware states, in Problems 13–15.

**Prerequisites.** Lecture 16 for the entanglement entropy of an interval and its cutoff, Lecture 23 for the thermofield double, Euclidean regularity and the Kruskal extension, Lecture 24 for the information problem. The variation of an action and the Weyl factor of a two-dimensional entanglement entropy.

**What this lecture establishes.** The equations of JT gravity with matter, the reduction of the boundary action to the Schwarzian, the thermodynamics of the thermal saddle, the zero-temperature and thermal solutions with their Kruskal form, the conformal map of the Euclidean equilibrium geometry to the plane, and the generalized-entropy functional of the zero-temperature island are exact calculations. The transparent coupling to the bath and the choice of matter state are the specification of the model. The island rule, the one-loop exactness of the Schwarzian and the results on evaporation are stated with sources.

## 0. Reading

**Primary.**

- A. Almheiri, J. Polchinski, [Models of AdS_2 Backreaction and Holography](https://arxiv.org/abs/1402.6334) (2014).
- J. Maldacena, D. Stanford, Z. Yang, [Conformal symmetry and its breaking in two dimensional Nearly Anti-de-Sitter space](https://arxiv.org/abs/1606.01857) (2016).
- A. Almheiri, N. Engelhardt, D. Marolf, H. Maxfield, [The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole](https://arxiv.org/abs/1905.08762) (2019).
- A. Almheiri, R. Mahajan, J. Maldacena, Y. Zhao, [The Page curve of Hawking radiation from semiclassical geometry](https://arxiv.org/abs/1908.10996) (2019).

**Secondary.**

- G. Penington, [Entanglement Wedge Reconstruction and the Information Paradox](https://arxiv.org/abs/1905.08255) (2019).
- A. Almheiri, R. Mahajan, J. Maldacena, [Islands outside the horizon](https://arxiv.org/abs/1910.11077) (2019).
- A. Almheiri, T. Hartman, J. Maldacena, E. Shaghoulian, A. Tajdini, [Replica Wormholes and the Entropy of Hawking Radiation](https://arxiv.org/abs/1911.12333) (2019), for the setup and, in Appendix B, the conformal welding.
- T. G. Mertens, G. J. Turiaci, [Solvable Models of Quantum Black Holes: A Review on Jackiw-Teitelboim Gravity](https://arxiv.org/abs/2210.10846) (2022).
- A. Almheiri, T. Hartman, J. Maldacena, E. Shaghoulian, A. Tajdini, [The entropy of Hawking radiation](https://arxiv.org/abs/2006.06872) (2020).

**Optional research reading.**

- K. Jensen, [Chaos in AdS$_2$ holography](https://arxiv.org/abs/1605.06098) (2016), and J. Engelsöy, T. G. Mertens, H. Verlinde, [An Investigation of AdS$_2$ Backreaction and Holography](https://arxiv.org/abs/1606.03438) (2016).
- D. Stanford, E. Witten, [Fermionic Localization of the Schwarzian Theory](https://arxiv.org/abs/1703.04612) (2017).
- N. Engelhardt, A. C. Wall, [Quantum Extremal Surfaces: Holographic Entanglement Entropy beyond the Classical Regime](https://arxiv.org/abs/1408.3203) (2014).

## 1. Which system's entropy will we calculate?

In 1983 Teitelboim, and in 1985 Jackiw, studied gravity in two dimensions with a scalar dilaton whose equation of motion fixes the curvature to a constant. The theory has no propagating gravitons, and for three decades it was mostly a laboratory for canonical quantization. Almheiri and Polchinski revived it in 2014 as the universal description of the near-horizon region of near-extremal black holes: dimensional reduction on the transverse sphere gives a dilaton that measures its size, the extremal entropy becomes a constant $S_0$, and the deviation from extremality is small and dynamical. Their question was how gravitational backreaction affects holography in AdS$_2$, where it is not a small effect at low energies. In 2016 Jensen, Maldacena, Stanford and Yang, and Engelsöy, Mertens and Verlinde found that the whole dynamics reduces to one degree of freedom, a reparametrization of the boundary time, governed by the Schwarzian action that also describes the low-energy limit of the SYK model. Stanford and Witten showed in 2017 that its path integral is one-loop exact.

The same theory became the arena of the information problem in 2019. Penington, for an AdS black hole evaporating through absorbing boundary conditions, and independently Almheiri, Engelhardt, Marolf and Maxfield, for a two-sided JT black hole coupled on one side to a heat sink, followed the quantum extremal surface of Engelhardt and Wall. At the Page time it jumps to just inside the event horizon, from the empty surface in Penington's one-sided setup and from near the original bifurcation point in the JT model, and the entanglement wedge of the radiation then contains most of the interior. Almheiri, Mahajan, Maldacena and Zhao turned this into a rule for computing the entropy of any system entangled with gravity, the island rule, and Almheiri, Mahajan and Maldacena applied it to a black hole in equilibrium with a bath, where the island extends outside the horizon. The replica derivation of the rule followed within months, and it is the subject of Lecture 27.

A formula for the entropy of radiation is meaningful only in a specified system. This lecture specifies one: the gravitational region, the matter, the bath, the state, the region of the bath that collects the radiation, and the conventions for cutoffs, before anything is extremized. We set the AdS$_2$ radius to one.

## 2. The action and the equations

The Euclidean action with an entropy-normalized dilaton $\varphi$ is

$$
I_{\mathrm{JT}}=-\frac{S_0}{4\pi}\left[\int_M\sqrt g\,R+2\int_{\partial M}\sqrt h\,K\right]-\frac1{4\pi}\int_M\sqrt g\,\varphi\,(R+2)-\frac1{2\pi}\int_{\partial M}\sqrt h\,\varphi\,(K-1)+I_{\mathrm{matter}}[g,\chi],
$$

where $K$ is the extrinsic curvature of the boundary and $\chi$ the matter fields. By the Gauss–Bonnet theorem the first bracket is $4\pi$ times the Euler characteristic, so the first term is $-S_0\,\chi(M)$: it has no local variation and weights each topology by $e^{S_0\chi}$ (Problem 7). The normalization is such that a point where the dilaton equals $\varphi$ contributes $S_0+\varphi$ to an entropy, as the thermal solution of §3 shows; a dilaton $\Phi$ with the conventional coefficient $1/16\pi G_2$ is related by $\varphi=\Phi/4G_2$. The matter does not couple to the dilaton.

Varying $\varphi$ gives

$$
R=-2 .
$$

The metric is locally AdS$_2$ everywhere, with or without matter. [Exact.] But the metric variation contains the dynamics. In two dimensions $R_{\mu\nu}=\frac12Rg_{\mu\nu}$ identically, so the Einstein tensor vanishes and the variation of $\sqrt g\,R$ reduces to the derivative terms $\sqrt g\,(g_{\mu\nu}\nabla^2-\nabla_\mu\nabla_\nu)\delta g^{\mu\nu}$; integrating by parts moves the derivatives onto $\varphi$. In Lorentzian signature, with the Lorentzian action $\frac1{4\pi}\int\sqrt{-g}\,\varphi(R+2)+\cdots$ and the stress tensor $T_{\mu\nu}=-\frac2{\sqrt{-g}}\frac{\delta S_{\mathrm{matter}}}{\delta g^{\mu\nu}}$, the result is

$$
\nabla_\mu\nabla_\nu\varphi-g_{\mu\nu}\nabla^2\varphi+g_{\mu\nu}\varphi=-2\pi\,T_{\mu\nu}.
$$

[Exact calculation (Problem 1).] In conformal gauge $ds^2=-e^{2\omega}dx^+dx^-$, the Christoffel symbols are $\Gamma^\pm_{\pm\pm}=2\partial_\pm\omega$, and the components read

$$
-e^{2\omega}\,\partial_\pm\!\left(e^{-2\omega}\partial_\pm\varphi\right)=2\pi\,T_{\pm\pm},
\qquad
2\,\partial_+\partial_-\varphi+e^{2\omega}\varphi=4\pi\,T_{+-} .
$$

The first pair is a focusing equation. Positive null energy makes $e^{-2\omega}\partial_\pm\varphi$ decrease along null rays, as the Raychaudhuri equation makes the area of a null congruence focus in higher dimensions: the dilaton is the area of the transverse sphere of the parent black hole. For conformal matter the trace $T^\mu_{\ \mu}$ is fixed by the anomaly and is constant on $R=-2$, so its only effect is a constant shift of $\varphi$, which we absorb into $S_0$.

Consider the Poincaré patch, $ds^2=(-dt^2+dz^2)/z^2$ with $z>0$. The source-free equations are solved by

$$
\varphi=\frac{\varphi_r}{z},\qquad\varphi_r>0,
$$

where $\varphi_r$ is the renormalized boundary value of the dilaton (Problem 3). The general vacuum solution is $\varphi=\bigl(\varphi_0+\varphi_1t+\varphi_2(z^2-t^2)\bigr)/z$, with constants $\varphi_0,\varphi_1,\varphi_2$, a three-parameter family on which the $SL(2,\mathbb R)$ isometries of AdS$_2$ act. Note that the metric carries no information about the black hole: which solution is a black hole, and where its horizon is, is decided by the dilaton.

## 3. The boundary, the Schwarzian and the thermodynamics

The gravitational region ends on a boundary curve on which we impose

$$
g_{uu}=\frac1{\epsilon^2},\qquad\varphi=\frac{\varphi_r}\epsilon,
$$

with $u$ the time of the boundary theory, so that the proper length of the boundary curve is $du/\epsilon$ as $\epsilon\to0$. In Euclidean Poincaré coordinates $ds^2=(dt^2+dz^2)/z^2$ the curve is $(t(u),z(u))$, and the first condition gives $z=\epsilon\,t'+\epsilon^3\,t''^2/2t'+O(\epsilon^5)$. On a solution the bulk term vanishes, and the extrinsic curvature of the curve is

$$
K=\frac{t'\,(t'^2+z'^2+z\,z'')-z\,z'\,t''}{(t'^2+z'^2)^{3/2}}=1+\epsilon^2\,\mathrm{Sch}(t,u)+O(\epsilon^4),
\qquad
\mathrm{Sch}(t,u)=\frac{t'''}{t'}-\frac32\left(\frac{t''}{t'}\right)^2 .
$$

[Exact calculation, checked symbolically for $t'>0$ (Problem 8).] The boundary term of the action becomes $-\frac1{2\pi}\int du\,\frac1\epsilon\cdot\frac{\varphi_r}\epsilon\cdot\epsilon^2\,\mathrm{Sch}$, and for a disk topology

$$
I=-S_0-\frac{\varphi_r}{2\pi}\int du\;\mathrm{Sch}(t,u) .
$$

Thus the dynamics of the theory is the dynamics of the boundary curve. The Schwarzian is invariant under the Möbius maps $t\to(pt+q)/(rt+s)$, which are the isometries of AdS$_2$ acting on the curve (Problem 9), so the physical degree of freedom is the reparametrization modulo $SL(2,\mathbb R)$. This is the pattern that Maldacena, Stanford and Yang identified: the reparametrization symmetry of AdS$_2$ is spontaneously broken by the geometry to $SL(2,\mathbb R)$ and explicitly broken by the dilaton, whose coefficient $\varphi_r$ sets the scale.

On a thermal circle $u\sim u+\beta$ the saddle is the curve $t=\tan(\pi u/\beta)$, which maps the circle to the boundary of the hyperbolic disk. Its Schwarzian is constant,

$$
\mathrm{Sch}\!\left(\tan\frac{\pi u}\beta,u\right)=\frac{2\pi^2}{\beta^2},
$$

and the action is $I=-S_0-\pi\varphi_r/\beta$. Therefore

$$
\log Z=S_0+\frac{\pi\varphi_r}\beta,
\qquad
E=-\partial_\beta\log Z=\pi\varphi_rT^2,
\qquad
S=(1-\beta\partial_\beta)\log Z=S_0+2\pi\varphi_r T .
$$

[Exact calculation at the saddle.] The entropy is linear in temperature, with specific heat $2\pi\varphi_rT$, the behavior of a near-extremal black hole, and $S_0$ is the entropy that remains at extremality. Stanford and Witten showed that the Schwarzian path integral is one-loop exact, with $Z(\beta)$ equal to $e^{S_0}(\varphi_r/2\pi\beta)^{3/2}e^{\pi\varphi_r/\beta}$ up to a constant; the one-loop factor matters at temperatures of order $1/\varphi_r$, where the semiclassical description ends. [Stated only — refs: Stanford–Witten 2017.]

The entropy has a geometric form. The Euclidean saddle is the hyperbolic disk $ds^2=d\rho^2+\sinh^2\!\rho\,d\theta^2$, $\theta\sim\theta+2\pi$, with the dilaton $\varphi=\varphi_h\cosh\rho$; near the boundary $\varphi\simeq\frac12\varphi_he^\rho$, and matching to $\varphi_r/\epsilon$ at the proper length $\beta/\epsilon$ of the boundary gives $\varphi_h=2\pi\varphi_r/\beta$. Thus

$$
S=S_0+\varphi_h ,
$$

the topological term plus the value of the dilaton at the horizon, the center of the disk. The dilaton at a point plays the role of the area divided by $4G_N$, and this is the normalization announced in §2.

**Checkpoint 1.** The metric of every solution is AdS$_2$. Where is the black hole?

**Answer.** In the dilaton and the boundary. The thermal saddle has a boundary curve of constant Schwarzian and a dilaton with a minimum at the center of the disk; in Lorentzian signature the minimum becomes the bifurcation point of a horizon, and the entropy is the value of the dilaton there, plus $S_0$.

## 4. The thermal solution and its two sides

In Lorentzian signature, with $\beta=2\pi$ as in the conventions sheet, the exterior of the black hole is

$$
ds^2=\frac{-dt^2+d\sigma^2}{\sinh^2\sigma},\qquad\varphi=\varphi_r\coth(-\sigma),\qquad\sigma<0,
$$

where the boundary is at $\sigma\to0^-$, with $\varphi\simeq\varphi_r/(-\sigma)$ there, and the horizon at $\sigma\to-\infty$, where the dilaton tends to $\varphi_h=\varphi_r$. For general $\beta$ one replaces $\sigma$ and $t$ by $2\pi\sigma/\beta$ and $2\pi t/\beta$, multiplies the metric by $(2\pi/\beta)^2$, and the dilaton becomes $\frac{2\pi\varphi_r}\beta\coth(-2\pi\sigma/\beta)$, with horizon value $2\pi\varphi_r/\beta$. The Kruskal coordinates $w^+=e^{t+\sigma}$, $w^-=-e^{\sigma-t}$ on the right exterior give

$$
ds^2=-\frac{4\,dw^+dw^-}{(1+w^+w^-)^2},
\qquad
\varphi=\varphi_r\,\frac{1-w^+w^-}{1+w^+w^-},
$$

a solution of the source-free equations on the whole region $|w^+w^-|<1$. [Exact calculation, checked symbolically (Problem 11).] The boundaries are the two branches of $w^+w^-=-1$, the horizons are $w^\pm=0$, and the dilaton decreases toward the future interior, vanishes at $w^+w^-=1$ and is negative beyond, where the area of the parent black hole falls below its extremal value; the figures cut the diagram there for definiteness. The left exterior, $w^+<0<w^-$, is reached with $w^+=-e^{\sigma-t}$ and $w^-=e^{\sigma+t}$, where $t$ is the future-directed time of the left boundary. The geometry is the two-sided black hole of Lecture 23, and the state of two boundary systems in the thermofield double is its dual, with the modular flow acting as the boost $w^\pm\to e^{\pm\eta}w^\pm$.

## 5. Coupling to a bath

So far the black hole is in equilibrium in a closed box: radiation reflects off the AdS$_2$ boundary and falls back in. To let it escape we glue a bath to the boundary. The bath is a half line of flat space carrying the same conformal field theory of central charge $c$ as the gravitational region, with no gravity. At zero temperature the metric is

$$
ds^2=\frac{-dt^2+d\sigma^2}{\sigma^2}\quad(\sigma<-\epsilon),
\qquad
ds^2=\frac{-dt^2+d\sigma^2}{\epsilon^2}\quad(\sigma>-\epsilon),
$$

continuous at the cutoff $\sigma=-\epsilon$ where the gravitational region ends. In the renormalized units used below the bath metric is multiplied by $\epsilon^2$, and as $\epsilon\to0$ the bath is the half line $\sigma>0$ with the flat metric. The boundary conditions are transparent: the matter fields are continuous across the junction, so that excitations cross it without reflection. The whole spacetime is conformal to flat space in the coordinates $(t,\sigma)$, and we take the matter in the vacuum of these coordinates. Near the junction the matter sees a smooth half-line of flat space glued to AdS$_2$, and the dilaton boundary condition of §3 still holds on the gravitational side.

The equilibrium state at temperature $1/\beta$ is prepared by a Euclidean path integral, and in equilibrium it can be written down exactly. With $\beta=2\pi$ the Euclidean geometry is the hyperbolic disk of §3 in the coordinates $(\sigma,\tau)$, $\sigma<0$, joined to the flat semi-infinite cylinder $\sigma>0$ of the bath. The map $w=e^{\sigma+i\tau}$ sends both to the plane: $d\sigma^2+d\tau^2=|dw|^2/|w|^2$, so the cylinder becomes the exterior of the unit circle with the metric $|dw|^2/|w|^2$, and

$$
\frac{d\sigma^2+d\tau^2}{\sinh^2\sigma}=\frac{4\,|dw|^2}{\bigl(1-|w|^2\bigr)^2},
$$

the Poincaré disk metric on $|w|<1$. [Exact calculation (Problem 10).] The glued geometry is conformal to the plane, $ds^2=\Omega^{-2}|dw|^2$, and the matter path integral on it is the vacuum on the $w$ plane up to the Weyl factor. Its Lorentzian continuation is the vacuum in the Kruskal coordinates $w^\pm$, the Hartle–Hawking state, thermal at $\beta=2\pi$ in both the black-hole exterior and the bath. The figure shows the two pictures.

![[ads-cft-jt-bath-geometry.svg|Left: the Euclidean geometry of the equilibrium state in the complex w plane, with the hyperbolic disk inside the unit circle carrying circular contours of the dilaton around the horizon at the center, and the flat bath outside, with radial lines of constant Euclidean time. Right: the Lorentzian two-sided black hole in compactified Kruskal coordinates, with the two boundaries as vertical lines, the horizons as diagonals, the curves where the dilaton vanishes at top and bottom, and a triangular flat bath attached on each side, extending to null infinity.]]

The simplicity of equilibrium has a precise origin. The boundary curve of the thermal saddle is a circle in the disk, and the cylinder of the bath is glued along a circle, so the combined surface is uniformized by the single map $w=e^{\sigma+i\tau}$. But when the state is prepared by a Euclidean path integral whose boundary curve is not a circle, as for the replica geometries of Lecture 27, the gravitational region and the bath must be glued by a conformal welding: a map of the combined surface to the plane, determined together with the boundary curve, since the matter stress tensor that moves the curve depends on the map. [Stated only — refs: Almheiri–Hartman–Maldacena–Shaghoulian–Tajdini 2019, Appendix B.] For the real-time evaporation of §8, Almheiri, Engelhardt, Marolf and Maxfield instead solve for the boundary reparametrization and its energy balance. We stay in equilibrium, where the welding is the exponential map.

**Checkpoint 2.** The metric of the bath is flat and the metric of the gravitational region is curved. Why is the matter state in the Hartle–Hawking case nevertheless the vacuum of a single coordinate?

**Answer.** A conformal field theory depends on the metric only through its conformal class, up to the Weyl anomaly, which contributes a known factor to the partition function and known terms to entropies. The whole Euclidean geometry is conformal to the plane, so the matter path integral is the vacuum on the plane dressed by the Weyl factor.

## 6. The entropy to be computed, and its functional

The system whose entropy we compute is a region $R$ of the bath. It carries no gravity, its algebra is the algebra of the matter fields in $R$, and its state is the restriction of the global state; its von Neumann entropy is a well-defined quantity of quantum field theory, up to the ultraviolet cutoff at its endpoints. Hawking's calculation computes it by treating the matter as a quantum field on the fixed geometry, and it finds the entropy of the matter in $R$. The island rule of Almheiri, Mahajan, Maldacena and Zhao states that the fine-grained entropy of $R$ is instead

$$
S(R)=\min_I\ \operatorname*{ext}_I\left[\sum_{p\in\partial I}\bigl(S_0+\varphi(p)\bigr)+S_{\mathrm{matter}}(R\cup I)\right],
$$

where $I$ is a region of the gravitational spacetime, possibly empty, the sum runs over its endpoints, and the matter entropy is that of the union in the semiclassical state. [Stated only — refs: Almheiri–Mahajan–Maldacena–Zhao 2019; derived from replica geometries in Lecture 27.] That is, the bracket is the generalized entropy of Lecture 21, with the dilaton in the role of the area, and the extremum is the quantum extremal surface of Engelhardt and Wall. The island $I$ belongs to the entanglement wedge of $R$: after the Page time, operators in the island can be reconstructed from the radiation, by the reasoning of Lectures 19–21.

At zero temperature, collect the radiation in

$$
R=[b,\infty),\qquad b>0,
$$

on the slice $t=0$, and consider a candidate island $I=(-\infty,-a]$ with $a>0$. In the pure matter state the complement of $I\cup R$ is the interval $[-a,b]$, so

$$
S_{\mathrm{matter}}(I\cup R)=S_{\mathrm{matter}}\bigl([-a,b]\bigr),
$$

and the union of two disjoint regions reduces to one interval. For a conformal field theory in a metric $ds^2=e^{2\omega}(-dt^2+d\sigma^2)$, in the vacuum of $(t,\sigma)$, the entropy of an interval with endpoints $\sigma_1,\sigma_2$ is $\frac c6\log\bigl((\sigma_2-\sigma_1)^2/\delta_1\delta_2\bigr)$ with coordinate cutoffs $\delta_i$. A proper cutoff $\epsilon_i$ corresponds to $\delta_i=\epsilon_ie^{-\omega_i}$, so

$$
S_{\mathrm{matter}}=\frac c6\log\frac{(\sigma_2-\sigma_1)^2\,e^{\omega_1+\omega_2}}{\epsilon_1\epsilon_2} .
$$

At $\sigma_1=-a$ the Poincaré factor is $e^{\omega_1}=1/a$, and in the bath it is one in the renormalized units. Therefore

$$
S_{\mathrm{matter}}\bigl([-a,b]\bigr)=\frac c6\log\frac{(a+b)^2}{a\,\epsilon_a\,\epsilon_b} .
$$

The cutoff $\epsilon_a$ at the gravitational endpoint is absorbed into the renormalization of $S_0$, with a fixed reference length, and the bath cutoff $\epsilon_b=\epsilon$ is kept. With the dilaton $\varphi_r/a$ at the endpoint,

$$
S_{\mathrm{gen}}(a)=S_0+\frac{\varphi_r}a+\frac c6\log\frac{(a+b)^2}{a\,\epsilon} .
$$

[Exact calculation of the functional; its use is the island rule.] The Weyl factor supplies the $-\log a$ in the matter term. Without it the matter entropy would grow with $a$ in a different way, and the extremum would move. The no-island candidate, $I=\emptyset$, is the entropy of the half-line $R$, whose complement contains the whole gravitational region; it has an infrared divergence at $\sigma\to-\infty$ that must be regulated separately and cannot be absorbed into $S_0$. Lecture 26 extremizes $S_{\mathrm{gen}}(a)$ and compares the candidates.

## 7. Self-study: the two-sided equilibrium and the no-island entropy

The thermal model of Lecture 26 uses both exteriors. Prepare the two-sided black hole of §4 with a bath on each side, in the Hartle–Hawking state, and let both baths evolve forward in their own time $t$. Collect the radiation $R=R_L\cup R_R$, with $R_{L,R}$ the half-lines $\sigma\geq b$ of the two baths at time $t$. The global state is the vacuum in the Kruskal coordinates $w^\pm$ with the metric $\Omega^{-2}(-dw^+dw^-)$, where

$$
\Omega=e^{\sigma}\ \ \text{in the baths},
\qquad
\Omega=e^{\sigma}\,|\sinh\sigma|\ \ \text{in the gravitational region},
$$

since $-dw^+dw^-=e^{2\sigma}(-dt^2+d\sigma^2)$. Without an island, the complement of $R$ is the single interval from the left bath point $P_L$ to the right one $P_R$, through both exteriors and the bridge. With $P_R=(e^{b+t},-e^{b-t})$ and $P_L=(-e^{b-t},e^{b+t})$ in $(w^+,w^-)$, the squared distance is $-\Delta w^+\Delta w^-=4e^{2b}\cosh^2t$, and each endpoint carries $\Omega^{-1}=e^{-b}$. Therefore

$$
S_{\mathrm{no\ island}}(t)=\frac c6\log\frac{4e^{2b}\cosh^2t\cdot e^{-2b}}{\epsilon^2}=\frac c3\log\bigl(2\cosh t\bigr)-\frac c3\log\epsilon .
$$

[Exact calculation.] The entropy grows linearly at late times, at the rate $c/3$ in these units, or $2\pi c/3\beta$ in general. Note that the black hole is in equilibrium, and its temperature does not change. What grows is the entanglement between the radiation and the black hole, as outgoing Hawking quanta enter the baths and ingoing bath quanta fall into the black hole, and without bound: this is the information paradox of Almheiri, Mahajan and Maldacena for a black hole in contact with a bath. The entropy of the two-sided black hole is finite, $2(S_0+\varphi_r)$, so the growth must stop, and Lecture 26 shows how.

## 8. Self-study: the evaporating model

Almheiri, Engelhardt, Marolf and Maxfield, and in a different setup Penington, let the black hole evaporate. A black hole at temperature $T_0$ is coupled at $u=0$ to a bath at zero temperature, and the outgoing radiation carries away energy while the bath sends nothing back. The boundary energy obeys a balance equation, and the black hole cools. A quantum extremal surface appears at the Page time just inside the event horizon, at an infalling time of about a scrambling time $\frac\beta{2\pi}\log S_{\mathrm{BH}}$ in the past, and it moves along with the horizon afterward; the entanglement wedge of the radiation then contains the interior behind it. Information thrown in disappears from the black hole's entanglement wedge after a scrambling time, as in the Hayden–Preskill model of Lecture 24. [Stated only — refs: Penington 2019; Almheiri–Engelhardt–Marolf–Maxfield 2019.] Almheiri, Mahajan, Maldacena and Zhao obtained the same results in a model where the matter itself has a holographic dual, so that the quantum extremal surface becomes a classical extremal surface in three dimensions, which connects the radiation to the interior. Problem 13 derives the energy balance.

## 9. What to take away

- **Exact:** varying the dilaton fixes $R=-2$; varying the metric gives $\nabla_\mu\nabla_\nu\varphi-g_{\mu\nu}\nabla^2\varphi+g_{\mu\nu}\varphi=-2\pi T_{\mu\nu}$, whose null components are focusing equations for the dilaton.
- **Exact calculation:** the boundary action is $-S_0-\frac{\varphi_r}{2\pi}\int du\,\mathrm{Sch}(t,u)$; the thermal saddle gives $\log Z=S_0+\pi\varphi_r/\beta$ and $S=S_0+\varphi_h$, the dilaton at the horizon.
- **Exact calculation:** the Euclidean equilibrium geometry of the black hole and its bath is conformal to the plane through $w=e^{\sigma+i\tau}$, so the matter is in the vacuum of the Kruskal coordinates, thermal on both sides.
- **Exact calculation:** at zero temperature the generalized entropy of the island $(-\infty,-a]$ with radiation $[b,\infty)$ is $S_0+\varphi_r/a+\frac c6\log\frac{(a+b)^2}{a\epsilon}$, and the no-island entropy of the two-sided equilibrium grows as $\frac c3\log(2\cosh t)$.
- **Stated only:** the island rule gives the fine-grained entropy of the radiation, and in the evaporating model the quantum extremal surface jumps at the Page time.

## 10. Looking ahead

Lecture 26 extremizes the functionals of §§6–7. At zero temperature the endpoint is the root of a quadratic equation and lies outside the horizon; in the two-sided equilibrium the island, derived from the free-fermion entropy of two intervals, saturates the growth of §7 at twice the black-hole entropy. Lecture 27 derives the island rule from the replica trick, where the island appears as the fixed-point set of a replica wormhole.

## 11. Problem set

### Classroom core

1. **The equations of motion.** Vary the Lorentzian action with respect to $\varphi$ and $g^{\mu\nu}$, using $R_{\mu\nu}=\frac12Rg_{\mu\nu}$ in two dimensions, and derive $R=-2$ and the dilaton equation.

2. **Conformal gauge.** For $ds^2=-e^{2\omega}dx^+dx^-$, compute $\nabla_\pm\nabla_\pm\varphi$ and derive the focusing equations and the $+-$ equation.

3. **Vacuum solutions.** Check that $\varphi=\varphi_r/z$ solves the source-free equations in the Poincaré patch, and that $\varphi=\varphi_r\coth(-\sigma)$ solves them in the metric $(-dt^2+d\sigma^2)/\sinh^2\sigma$.

4. **The thermal Schwarzian.** Compute $\mathrm{Sch}(\tan(\pi u/\beta),u)$ and derive $E$, $S$ and the specific heat from $I=-S_0-\frac{\varphi_r}{2\pi}\int\mathrm{Sch}$.

5. **The endpoint factor.** Why is the coordinate cutoff at $\sigma=-a$ equal to $a\,\epsilon_a$? Derive $S_{\mathrm{gen}}(a)$.

6. **Purity.** Identify the complement of $I\cup R$ at zero temperature, and explain why its entropy equals that of $I\cup R$.

### Self-study consolidation

7. **The topological term.** Use Gauss–Bonnet to show that the first term of the action is $-S_0\chi(M)$, and that the disk contributes $S_0$ to $\log Z$.

8. **The extrinsic curvature.** With $z=\epsilon t'+\epsilon^3t''^2/2t'$, verify $g_{uu}=\epsilon^{-2}+O(\epsilon^2)$ and $K=1+\epsilon^2\mathrm{Sch}(t,u)+O(\epsilon^4)$.

9. **Möbius invariance.** Show that $\mathrm{Sch}\bigl(\frac{pt+q}{rt+s},u\bigr)=\mathrm{Sch}(t,u)$ for $ps-qr=1$, and interpret the result.

10. **The welding map.** Verify the two metrics of §5 in the coordinate $w=e^{\sigma+i\tau}$, and find the Weyl factor $\Omega$ of the glued geometry.

11. **Kruskal form.** Verify the Kruskal metric and dilaton of §4, find where the dilaton vanishes, and write the left exterior in Kruskal coordinates.

12. **Ultraviolet and infrared.** Can the infrared divergence of the no-island entropy at zero temperature be absorbed into the renormalization of $S_0$?

### Research extension

13. **The evaporating black hole.** Couple the black hole at temperature $T_0$ to a bath at zero temperature at $u=0$. Using $E=-\frac{\varphi_r}{2\pi}\mathrm{Sch}(t,u)$ for the Lorentzian boundary curve and the outgoing flux $T_{uu}=-\frac c{24\pi}\mathrm{Sch}(t,u)$, derive the energy balance. *Known:* Almheiri, Engelhardt, Marolf and Maxfield, and Almheiri, Mahajan, Maldacena and Zhao, find exponential cooling. *Completion:* $E(u)=E_0e^{-ku}$ with $k=c/12\varphi_r$ in the normalization of this lecture, the condition $k\ll T_0$ for slow evaporation, and the time at which the no-island entropy of the radiation exceeds the Bekenstein–Hawking entropy.

14. **The Schwarzian density of states.** From $Z(\beta)\propto e^{S_0}\beta^{-3/2}e^{\pi\varphi_r/\beta}$, compute the density of states by an inverse Laplace transform and compare its logarithm with $S_0+2\pi\varphi_rT$ at large energy. *Known:* Stanford and Witten derive the exactness of the one-loop factor. *Completion:* $\rho(E)\propto e^{S_0}\sinh\bigl(2\sqrt{\pi\varphi_rE}\bigr)$, with its small-energy behavior interpreted.

15. **Hartle–Hawking and Boulware.** Compute the matter stress tensor in the thermal model for the vacuum in $w^\pm$ and for the vacuum in $(t,\sigma)$, in both coordinate systems. *Known:* the Hartle–Hawking state is regular at the horizon and carries a thermal flux $c/48\pi$ in each direction at $\beta=2\pi$, and the Boulware state has a divergent stress tensor at the horizon in Kruskal coordinates. *Completion:* the four components and the location of the divergence.

## 12. Answer checkpoints

1. The dilaton variation gives $R+2=0$. With $\delta\sqrt{-g}=-\frac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$ and $\delta(\sqrt{-g}R)\simeq\sqrt{-g}(g_{\mu\nu}\nabla^2-\nabla_\mu\nabla_\nu)\delta g^{\mu\nu}$, the metric variation gives $\frac1{4\pi}(g_{\mu\nu}\nabla^2\varphi-\nabla_\mu\nabla_\nu\varphi-g_{\mu\nu}\varphi)-\frac12T_{\mu\nu}=0$.

2. $g_{\pm\pm}=0$ and $\nabla_+\nabla_+\varphi=\partial_+^2\varphi-2\partial_+\omega\,\partial_+\varphi=e^{2\omega}\partial_+(e^{-2\omega}\partial_+\varphi)$. For the $+-$ component, $\nabla^2\varphi=-4e^{-2\omega}\partial_+\partial_-\varphi$ and $g_{+-}=-\frac12e^{2\omega}$.

3. The trace equation requires $\nabla^2\varphi=2\varphi$. For $\varphi_r/z$, $\nabla^2=z^2(-\partial_t^2+\partial_z^2)$ gives $2\varphi_r/z$. For $\coth(-\sigma)$, $\sinh^2\sigma\,\partial_\sigma^2\coth(-\sigma)=2\coth(-\sigma)$. The null components vanish in both cases (Problem 11 gives a uniform check).

4. $\mathrm{Sch}=2\pi^2/\beta^2$, so $I=-S_0-\pi\varphi_r/\beta$. Then $E=\pi\varphi_r/\beta^2$, $S=S_0+2\pi\varphi_r/\beta$, and $C=T\,dS/dT=2\pi\varphi_rT$.

5. At $\sigma=-a$ the metric is $(-dt^2+d\sigma^2)/a^2$, so a proper length $\epsilon_a$ is a coordinate length $a\epsilon_a$. Substituting into $\frac c6\log\frac{(a+b)^2}{\delta_a\delta_b}$ gives $\frac c6\log\frac{(a+b)^2}{a\epsilon_a\epsilon_b}$.

6. On the slice $t=0$ the matter lives on the whole line, and $I\cup R$ leaves out $[-a,b]$. In a pure state complementary regions have equal entropies.

7. $\int\sqrt gR+2\int\sqrt hK=4\pi\chi$. The disk has $\chi=1$, so $-I\supset S_0$.

8. $g_{uu}=(t'^2+z'^2)/z^2$ with $z'^2=\epsilon^2t''^2+O(\epsilon^4)$ and $z^2=\epsilon^2t'^2+\epsilon^4t''^2+O(\epsilon^6)$ gives $\epsilon^{-2}+O(\epsilon^2)$. Expanding $K$ in $\epsilon$ gives $1+\epsilon^2(t'''/t'-\frac32t''^2/t'^2)$ once $t'>0$.

9. The Schwarzian obeys the chain rule $\mathrm{Sch}(f\circ t,u)=t'^2\,\mathrm{Sch}(f,t)+\mathrm{Sch}(t,u)$, and $\mathrm{Sch}(f,t)=0$ for a Möbius map. The Möbius maps are the isometries of AdS$_2$ acting on the boundary curve, which do not change the physical state.

10. $|dw|^2=|w|^2(d\sigma^2+d\tau^2)$ and $|w|^2\sinh^2\sigma=\frac14(1-|w|^2)^2$. Thus $\Omega^{-1}=2/(1-|w|^2)$ inside and $\Omega^{-1}=1/|w|$ outside.

11. $-dw^+dw^-=e^{2\sigma}(-dt^2+d\sigma^2)$ and $1+w^+w^-=1-e^{2\sigma}$ give $4e^{2\sigma}/(1-e^{2\sigma})^2=1/\sinh^2\sigma$. The dilaton $\varphi_r(1+e^{2\sigma})/(1-e^{2\sigma})=\varphi_r\coth(-\sigma)$ vanishes at $w^+w^-=1$. The left exterior has $w^+=-e^{\sigma-t}$, $w^-=e^{\sigma+t}$.

12. No. The counterterm renormalizing $S_0$ is local at a gravitational endpoint and depends on the ultraviolet cutoff there; the infrared divergence comes from the far end of the complement and depends on how the half-line is regulated.

**Wiki connections.** [[jt-gravity|JT gravity]] · [[quantum-extremal-surfaces|quantum extremal surfaces]]
