---
title: "Lecture 27 — Replicas, competing saddles, and limits of the model"
type: lecture-notes
edition: "2.2 — rewritten at the AQFT standard"
lecture: 27
semester: 2
week: 10
hours: 3
prerequisites: "Lectures 16, 21, 24, 25 and 26; the replica trick and the Riemann–Hurwitz formula"
status: "rewritten 2026-09-30, pending instructor review; the replica identities, the permutation sum for the moments of a random state, the Riemann–Hurwitz count of the JT replica wormhole, the refined Rényi entropy of the JT disk and the envelope step of the cosmic-brane argument are exact calculations or elementary proofs; the Lewkowycz–Maldacena and Dong derivations, which assume a replica-symmetric saddle and Dong's identification of the conical quotient with a backreacted brane, and the replica-wormhole derivation of the island rule are sketched with sources; the West Coast model and the ensemble interpretation are stated"
modified: 2026-09-30
---

# Lecture 27 — Replicas, competing saddles, and limits of the model

> *An entropy is computed by the replica trick from the moments $\operatorname{Tr}\rho^n$, and in gravity the moments are path integrals whose boundary conditions glue $n$ copies of the system. Lewkowycz and Maldacena showed in 2013 that the smooth replicated geometry, divided by its replica symmetry, has a conical defect at a fixed surface, and that the entropy is the area of that surface divided by $4G_N$. Dong reinterpreted the defect as a cosmic brane whose tension vanishes as $n\to1$, so that the surface is extremal. This lecture derives both statements with one envelope argument, and checks Dong's formula exactly for the JT disk. For the radiation of Lectures 25–26 the gluing admits a second family of geometries, which connect the replicas through the gravitational region: the replica wormholes of Almheiri, Hartman, Maldacena, Shaghoulian and Tajdini and of Penington, Shenker, Stanford and Yang. Their fixed points are the island endpoints, and their topology produces the $2S_0$ of Lecture 26. The finite model of Lecture 24 has the same structure, as a sum over permutations whose two extreme terms are the two saddles. We close with what the replica calculation assumes and what it leaves open.*

## How to use this lecture

**Classroom core, one meeting of three hours.** The history (§1, 10 minutes), replica moments and their normalization (§2, 15 minutes), the permutation sum of random states (§3, 20 minutes), and the derivations of Lewkowycz–Maldacena and Dong (§4, 35 minutes) come before a 10-minute break. After it come the JT replica geometries (§5, 25 minutes), the origin of extremization (§6, 20 minutes), and the West Coast model (§7, 20 minutes), with 25 minutes for Checkpoints 1 and 2 and Problems 4–6; Problems 1–3 complete the core assignment. These allocations are proposals and have not been tested in class.

**Self-study.** Why “take the smaller entropy” is an approximation (§8), ensembles and factorization (§9), and Problems 7–12, including the refined Rényi entropy of the JT disk, the leading permutations and the Marchenko–Pastur entropy.

**Research extension.** The Rényi crossover of a finite model, the resolvent of the West Coast model, and the ensemble interpretation of the replica wormhole, in Problems 13–15.

**Prerequisites.** Lecture 16 for the replica trick and twist operators, Lecture 21 for generalized entropy, Lecture 24 for the Haar average, Lectures 25 and 26 for the JT model and its island. The Riemann–Hurwitz formula for branched covers.

**What this lecture establishes.** The replica identities with their normalization, the exact permutation sum for the moments of a random state, the Riemann–Hurwitz count $\chi=2-n$ of the two-endpoint replica wormhole with its $2S_0$, the refined Rényi entropy of the JT disk, and the envelope step of the cosmic-brane argument are exact calculations or elementary proofs. The Lewkowycz–Maldacena and Dong derivations rest on replica symmetry, analytic continuation and Dong's identification of the conical quotient with a backreacted brane, and are sketched; the derivation of the island rule from replica wormholes is sketched with its sources, and the West Coast model and the ensemble interpretation are stated.

## 0. Reading

**Primary.**

- A. Lewkowycz, J. Maldacena, [Generalized gravitational entropy](https://arxiv.org/abs/1304.4926) (2013).
- X. Dong, [The Gravity Dual of Renyi Entropy](https://arxiv.org/abs/1601.06788) (2016).
- A. Almheiri, T. Hartman, J. Maldacena, E. Shaghoulian, A. Tajdini, [Replica Wormholes and the Entropy of Hawking Radiation](https://arxiv.org/abs/1911.12333) (2019).
- G. Penington, S. H. Shenker, D. Stanford, Z. Yang, [Replica wormholes and the black hole interior](https://arxiv.org/abs/1911.11977) (2019).

**Secondary.**

- T. Faulkner, A. Lewkowycz, J. Maldacena, [Quantum corrections to holographic entanglement entropy](https://arxiv.org/abs/1307.2892) (2013).
- C. Callan, F. Wilczek, [On Geometric Entropy](https://arxiv.org/abs/hep-th/9401072) (1994), and C. Holzhey, F. Larsen, F. Wilczek, [Geometric and Renormalized Entropy in Conformal Field Theory](https://arxiv.org/abs/hep-th/9403108) (1994).
- D. V. Fursaev, S. N. Solodukhin, [On the Description of the Riemannian Geometry in the Presence of Conical Defects](https://arxiv.org/abs/hep-th/9501127) (1995).

**Optional research reading.**

- P. Saad, S. H. Shenker, D. Stanford, [JT gravity as a matrix integral](https://arxiv.org/abs/1903.11115) (2019), and D. Marolf, H. Maxfield, [Transcending the ensemble: baby universes, spacetime wormholes, and the order and disorder of black hole information](https://arxiv.org/abs/2002.08950) (2020).
- J. Maldacena, L. Maoz, [Wormholes in AdS](https://arxiv.org/abs/hep-th/0401024) (2004).
- X. Dong, A. Lewkowycz, [Entropy, Extremality, Euclidean Variations, and the Equations of Motion](https://arxiv.org/abs/1705.08453) (2017), and D. Stanford, [More quantum noise from wormholes](https://arxiv.org/abs/2008.08570) (2020).

## 1. Why can a second geometry change an entropy?

In 1994 Callan and Wilczek computed the entropy of a field restricted to half of space by placing it on a cone and differentiating the partition function with respect to the opening angle. Holzhey, Larsen and Wilczek obtained in the same way the logarithm $\frac c3\log(\ell/\epsilon)$ for an interval in two dimensions. The replica trick of Lecture 16 is the same idea in discrete form: the moments $\operatorname{Tr}\rho^n$ are partition functions on $n$-sheeted surfaces, and the entropy is their derivative at $n=1$. Fursaev and Solodukhin clarified in 1995 how curvature concentrates at a conical singularity, which is what the derivative picks up.

Lewkowycz and Maldacena applied the trick to the gravitational path integral in 2013. They considered a state prepared by a Euclidean path integral, replicated its boundary, and filled it with a smooth bulk saddle. Dividing by the replica symmetry produced a conical defect in the bulk, whose response to changing $n$ gave the area of a minimal surface. This explained the Ryu–Takayanagi formula of Lecture 16, and Faulkner, Lewkowycz and Maldacena extended it the same year to the first quantum correction. Dong found in 2016 that the replica geometries for integer $n$ are solutions with a cosmic brane of tension $(n-1)/4nG_N$, which made the Rényi entropies geometric as well. In 2019 two groups applied the same logic to the radiation of black holes coupled to an external system. Almheiri, Hartman, Maldacena, Shaghoulian and Tajdini, and Penington, Shenker, Stanford and Yang, found that the replica boundary conditions of the radiation admit saddles in which the gravitational regions of different replicas are joined. These replica wormholes give the island rule. Penington and collaborators also noted that the wormholes suggest an ensemble interpretation of the gravitational path integral, which Saad, Shenker and Stanford had found for JT gravity earlier that year.

## 2. Replica moments and their normalization

For a density matrix with eigenvalues $p_i$,

$$
\operatorname{Tr}\rho^n=\sum_ip_i^n,
\qquad
S_n=\frac1{1-n}\log\operatorname{Tr}\rho^n,
\qquad
S=-\partial_n\log\operatorname{Tr}\rho^n\Big|_{n=1},
$$

where the last identity holds whenever the entropy is finite and the moments are differentiable at $n=1$. A path integral computes an unnormalized quantity $Z_n$ with $\operatorname{Tr}\rho^n=Z_n/Z_1^n$, so

$$
S=\bigl(1-n\partial_n\bigr)\log Z_n\Big|_{n=1},
\qquad
\tilde S_n\equiv n^2\partial_n\!\left(\frac{n-1}nS_n\right)=\bigl(1-n\partial_n\bigr)\log Z_n .
$$

The refined Rényi entropy $\tilde S_n$ equals $S$ at $n=1$; for $\rho=e^{-K}/\operatorname{Tr}e^{-K}$ it is the von Neumann entropy of $\rho^n/\operatorname{Tr}\rho^n$, the same modular Hamiltonian at inverse temperature $n$. [Exact.] For instance, omitting the denominator $Z_1^n$ changes the answer by $\log Z_1$, which is large at a saddle of large action. For a qubit with probabilities $p$ and $1-p$, the derivative gives the binary entropy (Problem 2).

## 3. A finite analogue: the permutation sum

Lecture 24 computed the purity of the subsystem $R$ of dimension $m$ of a random pure state in dimension $D=mn$, and found two terms. The same structure holds for every moment. The average of $|\psi\rangle\langle\psi|^{\otimes \ell}$ over the Haar measure is proportional to the projector onto the symmetric subspace, which is the average of the permutation operators $P_\sigma$ of the $\ell$ copies, so

$$
\mathbb E\operatorname{Tr}\rho_R^\ell=\frac{1}{D(D+1)\cdots(D+\ell-1)}\sum_{\sigma\in S_\ell}m^{\#(\sigma\tau)}\,n^{\#(\sigma)} ,
$$

where $\tau$ is the cyclic permutation that computes the trace on $R$ and $\#(\cdot)$ counts cycles. [Exact calculation, checked for $\ell=2,3$.] At large dimensions the denominator is $D^\ell$, and two permutations stand out. The identity gives $m^{1-\ell}$, the moment of the maximally mixed state of $R$; the permutation $\sigma=\tau^{-1}$, which undoes the cyclic gluing, gives $n^{1-\ell}$, the moment of the maximally mixed state of $B$. For $m\ll n$ the identity dominates and $S(R)\simeq\log m$; for $m\gg n$ the other one dominates and $S(R)\simeq\log n$. [Controlled perturbative, in $m/n$ for $m\ll n$ and in $n/m$ for $m\gg n$.] Near $m\simeq n$ the permutations between the two, the non-crossing ones, contribute comparably. Their sum gives the Marchenko–Pastur distribution for the eigenvalues of $m\rho_R$, and from it the average entropy $\log m-m/2n$ for $m\leq n$, which is Page's result at large dimensions, with the deficit of half a nat at $m=n$ (Problem 12). [Stated only for the Marchenko–Pastur law, a standard result of random-matrix theory.]

Note that the two extreme permutations will be the two gravitational saddles. In one, each replica of the black hole closes on itself; in the other, the gluing of the radiation is undone inside the gravitational region. The finite model is an analogy until a gravitational calculation produces the same sum, and §7 describes a model where it does.

## 4. Generalized gravitational entropy and cosmic branes

Consider a state prepared by a Euclidean path integral on a manifold $M_1$, and the replica manifold $M_n$ that computes $\operatorname{Tr}\rho^n$, an $n$-fold cover of $M_1$ branched along the entangling surface. Suppose the dominant bulk saddle $B_n$ with boundary $M_n$ is smooth and preserves the $\mathbb Z_n$ symmetry that permutes the replicas. The quotient $\hat B_n=B_n/\mathbb Z_n$ has boundary $M_1$, and in the bulk it has a codimension-two fixed surface $\gamma_n$, around which the angle is $2\pi/n$. The quotient is smooth elsewhere, and since the action is local and $B_n$ is smooth,

$$
I[B_n]=n\,I_{\mathrm{reg}}[\hat B_n],
$$

where $I_{\mathrm{reg}}$ omits the tip, a regular point of $B_n$. The replica moment is then $\log\operatorname{Tr}\rho^n=-n\bigl(I_{\mathrm{reg}}[\hat B_n]-I[B_1]\bigr)$, and

$$
S_n=\frac n{n-1}\Bigl(I_{\mathrm{reg}}[\hat B_n]-I[B_1]\Bigr).
$$

To find how $I_{\mathrm{reg}}[\hat B_n]$ depends on $n$, Dong introduced the functional

$$
I_{\mathrm{tot}}[g;T]=I[g]+T\,A(\gamma),
$$

where $I[g]$ is the Einstein–Hilbert action including the curvature concentrated at a conical singularity on $\gamma$, and $T\,A(\gamma)$ is the Nambu–Goto action of a brane of tension $T$ on $\gamma$. The equations of $I_{\mathrm{tot}}$ are Einstein's equations away from $\gamma$, a conical deficit $8\pi G_NT$ at $\gamma$, as for a cosmic string, and the equation of motion of the brane in the backreacted geometry. Choose

$$
T_n=\frac{n-1}{4nG_N},
\qquad
8\pi G_NT_n=2\pi\left(1-\frac1n\right),
$$

so that the deficit matches the opening angle $2\pi/n$; the solution is $\hat B_n$. The conical curvature contributes $-\frac1{16\pi G_N}\cdot2\cdot2\pi\bigl(1-\frac1n\bigr)A=-T_nA$ to $I[\hat B_n]$, which cancels the brane term, so $I_{\mathrm{tot}}[\hat B_n;T_n]=I_{\mathrm{reg}}[\hat B_n]$. Since $\hat B_n$ extremizes $I_{\mathrm{tot}}$ at fixed $T$, only the explicit dependence on $T$ survives when $T$ varies, and

$$
\frac{d}{dn}I_{\mathrm{reg}}[\hat B_n]=A(\gamma_n)\,\frac{dT_n}{dn}=\frac{A(\gamma_n)}{4G_Nn^2} .
$$

[The envelope step is elementary (Problem 6); the stationarity of $I_{\mathrm{tot}}$ at $\hat B_n$ is Dong's identification, and it is assumed.] Two results follow. At $n\to1$,

$$
S=\frac{d}{dn}I_{\mathrm{reg}}[\hat B_n]\Big|_{n=1}=\frac{A(\gamma_1)}{4G_N},
$$

where $\gamma_1$ is the position of a brane of vanishing tension, which satisfies the brane equation in the unperturbed geometry: the trace of its extrinsic curvature vanishes, and $\gamma_1$ is an extremal surface. This is the Ryu–Takayanagi formula with its extremality condition. For integer $n$,

$$
\tilde S_n=n^2\partial_n\Bigl(I_{\mathrm{reg}}[\hat B_n]-I[B_1]\Bigr)=\frac{A(\gamma_n)}{4G_N},
$$

the area of the cosmic brane of tension $T_n$ at its backreacted position, which is Dong's formula. [Sketched — refs: Lewkowycz–Maldacena 2013; Dong 2016. The assumptions are the replica symmetry of the dominant saddle, the analytic continuation of the family $\hat B_n$ in $n$, and the regularity of the conical limit.]

> **Physical picture: a brane that measures entanglement.** Each Rényi entropy is carried by a brane whose tension grows from zero at $n=1$ to $1/4G_N$ as $n\to\infty$. A tense brane pulls the geometry toward itself; a tensionless one feels the geometry without deforming it and rests where its area is extremal. The von Neumann entropy is the area of the brane of zero tension, and the Rényi entropies measure how the geometry would respond if the brane had tension. The conical defect is a feature of the quotient: in the replicated geometry $B_n$ everything is smooth.

The JT disk gives an exact check. For a thermal state the replica manifold of the boundary is a circle of length $n\beta$, and the smooth bulk saddle $B_n$ is the hyperbolic disk of Lecture 25 at inverse temperature $n\beta$, with $\log Z_n=S_0+\pi\varphi_r/n\beta$. Then

$$
\tilde S_n=\bigl(1-n\partial_n\bigr)\log Z_n=S_0+\frac{2\pi\varphi_r}{n\beta},
$$

and the dilaton at the center of $B_n$, the fixed point of the rotation by $2\pi/n$, is $2\pi\varphi_r/n\beta$. [Exact calculation.] In fact, in JT gravity the role of $A/4G_N$ is played by $S_0+\varphi$, and the brane of Dong sits at the horizon of the replicated geometry, with the dilaton of that geometry.

**Checkpoint 1.** The conical defect of $\hat B_n$ has a curvature proportional to $1-1/n$. Why does its contribution to the action not give the entropy directly?

**Answer.** Because it is cancelled by the brane action on the solution: $I_{\mathrm{tot}}[\hat B_n]=I_{\mathrm{reg}}[\hat B_n]$. The entropy comes from the response of the smooth part of the action to a change of the opening angle, and the envelope argument shows that this response is the area times $dT_n/dn$.

## 5. The replica geometries of the radiation

Return to the radiation $R$ of Lectures 25–26. The moment $\operatorname{Tr}\rho_R^n$ is a path integral over $n$ copies of the whole Euclidean geometry, gravitational region and bath, with the $n$ baths glued cyclically along $R$. The bath is fixed and nongravitating; the gravitational regions are integrated over, subject to the dilaton and metric boundary conditions on each copy of the AdS$_2$ boundary. Two families of saddles compete.

In the Hawking saddle each replica keeps its own disk. The branch points lie only at the endpoints of $R$, in the bath, and the gravitational regions form $n$ disconnected disks, with Euler characteristic $n$. The topological term contributes $nS_0$ to $\log Z_n$, which cancels against $n\log Z_1$ in the normalized moment, and the matter entropy is that of $R$ alone in the fixed geometry: this saddle reproduces Hawking's growing entropy.

In the replica wormhole the gravitational regions of the replicas are joined. Its $\mathbb Z_n$ quotient is a single disk with branch points at the endpoints of $R$ and additional fixed points $w_1,\dots,w_q$ inside the gravitational region, where the quotient has conical defects of angle $2\pi/n$. The replica wormhole is an $n$-fold cover of the disk branched at the $q$ interior points, and by the Riemann–Hurwitz formula its Euler characteristic is

$$
\chi(B_n)=n\,\chi(\text{disk})-(n-1)\,q=n-(n-1)q .
$$

For the two-sided island of Lecture 26, $q=2$ and $\chi=2-n$. The topological term gives $\log Z_n\supset S_0(2-n)$ and $\log Z_1\supset S_0$, so

$$
-\partial_n\Bigl[S_0(2-n)-nS_0\Bigr]_{n=1}=2S_0 ,
$$

the two endpoint constants of Lecture 26; for the one-sided island at zero temperature, $q=1$ and the contribution is $S_0$. [Exact calculation.] The figure shows the quotients of the two saddles.

![[ads-cft-replica-saddles.svg|Left and center: the quotient of the two replica saddles drawn in the Euclidean plane of Lecture 25, with the gravitational disk inside the unit circle and the bath outside, and the cuts along the radiation regions on the real axis marked by branch points at their inner endpoints; in the replica wormhole a second cut along the island, between two conical points inside the disk, joins the replicas, and the Euler characteristics n and 2 minus n are indicated. Right: for a random state with black-hole dimension 64, the exact average entropy of the radiation as a function of the logarithm of its dimension, compared with the minimum of the two dominant saddles and with the second Rényi entropy from the average purity, showing a smooth transition at log 64.]]

The dilaton and the matter complete the picture. On the quotient each fixed point carries the cosmic-brane term of §4 in JT form, $\bigl(1-\frac1n\bigr)\bigl(S_0+\varphi(w_i)\bigr)$. The matter partition function on $B_n$ is a correlator of twist operators on the quotient, of dimension $\frac c{12}\bigl(n-\frac1n\bigr)$, at the endpoints of $R$ and at the $w_i$. Near $n=1$ the replica moment of the wormhole is

$$
-\log\operatorname{Tr}\rho_R^n=(n-1)\left[\sum_{i=1}^q\bigl(S_0+\varphi(w_i)\bigr)+S_{\mathrm{matter}}\bigl(R\cup I\bigr)\right]+O\bigl((n-1)^2\bigr),
$$

where $I$ is the region bounded by the $w_i$ and the matter entropy is computed in the unreplicated geometry, whose deformation by the defects is of order $n-1$. The bracket is the generalized entropy of Lecture 25, and the replica wormhole gives the island candidate. [Sketched — refs: Almheiri–Hartman–Maldacena–Shaghoulian–Tajdini 2019; Penington–Shenker–Stanford–Yang 2019.] At Lorentzian times $t\neq0$ the saddles are complex, since the fixed points move off the Euclidean section; the continuation is part of the prescription.

## 6. Why the generalized entropy is extremized

The positions $w_i$ are part of the saddle, and the action is stationary with respect to them. Near $n=1$ the action of the replica wormhole is

$$
I_n-nI_1=(n-1)\,S_{\mathrm{gen}}(w)+O\bigl((n-1)^2\bigr),
$$

and stationarity under a displacement of the fixed points gives

$$
0=\partial_{w}I_n=(n-1)\,\partial_wS_{\mathrm{gen}}+O\bigl((n-1)^2\bigr),
$$

so at leading order $\partial_wS_{\mathrm{gen}}=0$. That is, the fixed points are quantum extremal. This is the brane equation of §4 with the matter included, and it is the origin of the extremization of Lecture 26. The displacement of the unreplicated background does not contribute at first order, since $B_1$ is already a solution, as the displacement of the extremal surface dropped out in Lecture 22. [Sketched — refs: Lewkowycz–Maldacena 2013; Dong–Lewkowycz 2017.]

The argument locates the candidates and leaves their comparison open. Each extremum defines a saddle, and the saddles are compared by their actions: at leading order the entropy is the smaller generalized entropy, which is the minimization in the island rule. An extremum found by solving $\partial_wS_{\mathrm{gen}}=0$ must also correspond to an admissible replica geometry, which the equation alone does not guarantee.

**Checkpoint 2.** Does solving $\partial_wS_{\mathrm{gen}}=0$ establish that the island wins?

**Answer.** It establishes that the island saddle exists at leading order. Its dominance requires comparing its generalized entropy with that of every other admissible saddle, the Hawking saddle in particular, with the same normalization.

## 7. The West Coast model

Penington, Shenker, Stanford and Yang made the permutation sum of §3 exact in gravity. Their model is JT gravity with an end-of-the-world brane behind the horizon. The brane carries one of $k$ internal flavors, entangled with a radiation system of dimension $k$:

$$
|\Psi\rangle=\frac1{\sqrt k}\sum_{i=1}^k|\psi_i\rangle_B\,|i\rangle_R .
$$

The overlaps $\langle\psi_i|\psi_j\rangle$ are computed by the gravitational path integral with the brane as a boundary. In $\operatorname{Tr}\rho_R^n$ the flavor indices are contracted cyclically, and the geometries that contribute are labeled by permutations $\sigma\in S_n$, each cycle of $\sigma$ being a disk that joins the corresponding brane segments. In a microcanonical window of $e^{S}$ black-hole states, the moment becomes

$$
\operatorname{Tr}\rho_R^n\simeq\sum_{\sigma\in S_n}k^{\#(\sigma\tau)-n}\,e^{S(\#(\sigma)-n)} ,
$$

the leading form of the permutation sum of §3, with the radiation dimension $k$ in place of $m$ and the number $e^S$ of black-hole states in place of the dimension of $B$. [Stated only — refs: Penington–Shenker–Stanford–Yang 2019.] The disconnected geometry is the identity and the fully connected one is $\tau^{-1}$. Summing the planar geometries with a resolvent gives the Marchenko–Pastur spectrum and a Page curve that is smooth near $k=e^S$, where the dominance switches. The same paper shows that the replica wormhole gives the Petz map of Lecture 20 as an explicit reconstruction of the interior from the radiation.

Note that the model reproduces the Haar moments without any Haar average in the definition of the state. The gravitational path integral behaves as if the overlaps $\langle\psi_i|\psi_j\rangle$ were random variables with a Gaussian-like distribution of variance $e^{-S}$, and §9 explains what this suggests.

## 8. Self-study: why “take the smaller entropy” is an approximation

At a saddle of large action the partition function is a sum of exponentials, $Z_n\simeq\sum_se^{-I_n^{(s)}}$, and keeping the dominant term produces a sharp transition when two actions cross. But the finite model shows what happens near the crossing. Every permutation between the two extreme ones contributes, the transition is smooth over a window of order one in $\log k-\log e^S$, and at the crossing the entropy is half a nat below the minimum. The figure of §5 shows the exact average entropy against the minimum of the two saddles. The limits $n\to1$, large $S$ and late time need not commute, and one cannot normalize each candidate separately at $n=1$ and add them as independent density matrices: the saddles belong to one path integral, with one normalization.

The island rule is thus a controlled leading result, whose corrections are exponentially small in $S$ away from the transition and of order one near it. A result obtained near $n=1$ does not control all integer Rényi entropies. These can differ from the von Neumann entropy, as the second Rényi entropy in the figure shows, and away from $n=1$ they can be controlled by other saddles.

## 9. Self-study: ensembles and factorization

The replica wormhole connects different copies of the black hole through the gravitational region. If the boundary theory is a single quantum system, its moments factorize: the partition function on two disconnected boundaries is the product of the two, and a geometry that connects them seems to violate this. Maldacena and Maoz raised the puzzle for Euclidean wormholes in AdS in 2004. Saad, Shenker and Stanford found that the JT path integral, including all topologies, equals the genus expansion of a random-matrix integral, so that JT gravity is dual to an ensemble of quantum systems, and wormholes compute ensemble averages. [Stated only — refs: Saad–Shenker–Stanford 2019.] Marolf and Maxfield showed that the same structure appears as superselection sectors of baby universes, in which the ensemble is replaced by a choice of sector. [Stated only — refs: Marolf–Maxfield 2020.]

For the entropy of radiation the ensemble question matters little: the average of $\operatorname{Tr}\rho_R^n$ is what the replica wormhole computes, and the Page curve is self-averaging, with fluctuations suppressed by $e^{-S}$. For finer questions, such as the time dependence of a single correlator or the variance of the purity, the distinction between one theory and an ensemble is essential. Thus the calculation establishes a fine-grained entropy in a stated semiclassical model, including a saddle that a disconnected treatment misses. A microscopic unitary evolution, an efficient decoder, and all correlation functions of the radiation lie outside it.

## 10. What to take away

- **Exact:** replica moments must be normalized, $\operatorname{Tr}\rho^n=Z_n/Z_1^n$, and the refined Rényi entropy is $(1-n\partial_n)\log Z_n$; for the JT disk it equals $S_0$ plus the dilaton at the fixed point of the replica rotation.
- **Exact calculation:** the moments of a random state are a sum over permutations, $\sum_\sigma m^{\#(\sigma\tau)}n^{\#(\sigma)}$ over the rising factorial of $D$; the identity and the inverse cyclic permutation give $\log m$ and $\log n$.
- **Sketched, hypothesis-explicit:** assuming a replica-symmetric dominant saddle, its continuation in $n$, and Dong's identification of the conical quotient with a backreacted brane of tension $(n-1)/4nG_N$, the envelope argument gives $S=A(\gamma_1)/4G_N$ with $\gamma_1$ extremal and $\tilde S_n=A(\gamma_n)/4G_N$.
- **Exact calculation:** the two-endpoint replica wormhole has $\chi=2-n$, which gives the $2S_0$ of the island; near $n=1$ its fixed points carry $(1-\frac1n)(S_0+\varphi)$ and their stationarity is quantum extremality (sketched).
- **Stated only:** in the West Coast model the gravitational path integral reproduces the permutation sum and a smooth Page transition, and JT gravity is dual to an ensemble.

## 11. Looking ahead

Lectures 18–27 used the gravitational path integral as a tool, with its saddles, its continuation in $n$ and its topologies. Lecture 28 turns to what can be proved on a fixed AdS background without them: Rehren's algebraic holography, which matches the algebras of bulk wedges with those of boundary double cones exactly on fixed AdS; islands, like other state-dependent entanglement wedges, do not follow from that correspondence. Lectures 29–31 then study the large-$N$ algebras of the thermofield double of Lecture 23 and the modular structure that replaces geometric time.

## 12. Problem set

### Classroom core

1. **Normalization.** Why must $\operatorname{Tr}\rho^1=1$, and how does the denominator $Z_1^n$ enforce it? What error results from differentiating $\log Z_n$ alone?

2. **The qubit.** For eigenvalues $p$ and $1-p$, derive the binary entropy from $-\partial_n\log\operatorname{Tr}\rho^n$ at $n=1$, and compute $\tilde S_n$.

3. **The topological factor.** Reproduce the $2S_0$ of the two-endpoint wormhole and the $S_0$ of the one-endpoint case.

4. **Riemann–Hurwitz.** Derive $\chi=n\chi(\hat B)-(n-1)q$ for an $n$-fold cover branched at $q$ points by triangulating the quotient with the branch points as vertices.

5. **Deficit and tension.** Show that a deficit $2\pi(1-\frac1n)$ corresponds to $T_n=(n-1)/4nG_N$, and that the conical curvature of $\hat B_n$ cancels the brane action.

6. **The envelope step.** For $F(x;T)=f(x)+T\,g(x)$ and a stationary point $x_*(T)$, show that $\frac d{dT}F(x_*(T);T)=g(x_*(T))$, and use it to derive $\frac d{dn}I_{\mathrm{reg}}[\hat B_n]=A(\gamma_n)/4G_Nn^2$.

### Self-study consolidation

7. **The JT disk.** From $\log Z(\beta)=S_0+\pi\varphi_r/\beta$ compute $S_n$ and $\tilde S_n$ for the thermal state, and identify $\tilde S_n$ with the dilaton at the fixed point of the replicated disk.

8. **The leading permutations.** Show that the identity and $\tau^{-1}$ give $m^{1-\ell}$ and $n^{1-\ell}$, and that every other permutation is suppressed away from $m\simeq n$.

9. **Location versus dominance.** Explain why an extremum of $S_{\mathrm{gen}}$ is a candidate saddle and not yet the answer.

10. **Analytic continuation.** Why are the moments at integer $n$ insufficient to fix the derivative at $n=1$, and what additional input do the gravitational derivations use?

11. **Two saddles for the purity.** In the West Coast model with $k$ flavors and $e^S$ states, identify the two terms of $\operatorname{Tr}\rho_R^2\simeq\frac1k+e^{-S}$ with the Hawking saddle and the replica wormhole, and compare with $(m+n)/(mn+1)$.

12. **The Marchenko–Pastur entropy.** For the density $\rho(x)=\sqrt{(x_+-x)(x-x_-)}/2\pi rx$ with $x_\pm=(1\pm\sqrt r)^2$ and $r=m/n\leq1$, show that $\int x\log x\,\rho(x)\,dx=r/2$ at $r=1$, and derive the average entropy $\log m-\frac12$ at $m=n$.

### Research extension

13. **Rényi versus von Neumann.** Compare the second Rényi crossover of a random state with its von Neumann Page curve. *Known:* the second Rényi entropy is below the von Neumann entropy and has the same transition point at large dimensions. *Completion:* both curves for black-hole dimension $64$ from exact moments, with the maximal difference quantified before any gravitational analogy is drawn.

14. **The West Coast resolvent.** Sum the planar geometries of the West Coast model with a resolvent and obtain the spectrum of $\rho_R$ in the microcanonical ensemble. *Known:* Penington, Shenker, Stanford and Yang derive a Schwinger–Dyson equation whose solution in the microcanonical case is the Marchenko–Pastur law. *Completion:* the resolvent equation, its solution, and the entropy near $k=e^S$ compared with Page's exact formula at finite dimensions.

15. **The ensemble interpretation.** In the matrix-integral description of JT gravity, show that the replica wormhole computes the ensemble average of the purity of the radiation, and estimate its variance. *Known:* Saad, Shenker and Stanford establish the duality; Marolf and Maxfield give the baby-universe interpretation. *Completion:* the average and the variance of $\operatorname{Tr}\rho_R^2$ in a Gaussian model of the overlaps, with the variance shown to be suppressed by $e^{-2S}$.

## 13. Answer checkpoints

1. $\operatorname{Tr}\rho=1$ by definition, and $\operatorname{Tr}\rho^n=Z_n/Z_1^n$ is one at $n=1$ for any normalization of $Z_1$. Differentiating $\log Z_n$ alone gives $S-\log Z_1$.

2. $-\partial_n\log(p^n+(1-p)^n)=-\frac{p^n\log p+(1-p)^n\log(1-p)}{p^n+(1-p)^n}$, which at $n=1$ is the binary entropy. With $q_n=p^n/(p^n+(1-p)^n)$, $\tilde S_n=-q_n\log q_n-(1-q_n)\log(1-q_n)$.

3. $S_0(2-n)-nS_0=2S_0(1-n)$, whose negative derivative is $2S_0$. With $q=1$, $\chi=1$ and $S_0-nS_0=S_0(1-n)$ gives $S_0$.

4. A triangulation of the quotient with $V$ vertices, including the $q$ branch points, $E$ edges and $F$ faces lifts to one with $nV-(n-1)q$ vertices, $nE$ edges and $nF$ faces, since each branch point has a single preimage.

5. A brane of tension $T$ produces a deficit $8\pi G_NT$, which equals $2\pi(1-\frac1n)$ for $T_n$. The curvature at the tip contributes $\int\sqrt gR\supset2\cdot2\pi(1-\frac1n)A$, so the Einstein–Hilbert term gives $-\frac1{16\pi G_N}\cdot4\pi(1-\frac1n)A=-T_nA$.

6. $\frac{dF}{dT}=\partial_xF\,x_*'+g(x_*)$ and $\partial_xF=0$. With $F=I_{\mathrm{tot}}$, $g=A$ and $I_{\mathrm{tot}}[\hat B_n;T_n]=I_{\mathrm{reg}}[\hat B_n]$, the chain rule in $n$ gives $A(\gamma_n)\,dT_n/dn$ with $dT_n/dn=1/4G_Nn^2$.

7. $\log\operatorname{Tr}\rho^n=\log Z(n\beta)-n\log Z(\beta)=(1-n)S_0+\frac{\pi\varphi_r}\beta\bigl(\frac1n-n\bigr)$, so $S_n=S_0+\frac{\pi\varphi_r}\beta\frac{n+1}n$. Then $\tilde S_n=S_0+2\pi\varphi_r/n\beta$, the dilaton $2\pi\varphi_r/(n\beta)$ at the center of the disk of circumference $n\beta$ plus $S_0$.

8. The identity has $\#(\tau)=1$ and $\#(e)=\ell$, giving $mn^\ell/(mn)^\ell$; $\tau^{-1}$ has $\#(e)=\ell$ and $\#(\tau^{-1})=1$, giving $m^\ell n/(mn)^\ell$. Every permutation has $\#(\sigma\tau)+\#(\sigma)\leq\ell+1$, with equality exactly for the non-crossing ones. A non-crossing $\sigma$ with $\#(\sigma)=j$ contributes $(m/n)^{\ell-j}$ relative to the identity, which is small for $m\ll n$, and the others are further suppressed by powers of $1/mn$; near $m\simeq n$ the non-crossing terms are comparable.

9. The extremum identifies a saddle of the replica path integral at leading order; the answer is the saddle of least generalized entropy among all admissible ones, and an extremum may also fail to come from an admissible geometry.

10. Two analytic functions can agree at all integers and differ in their derivative at one, for example by $\sin(\pi n)$. The gravitational derivations assume that the family of saddles, continued in $n$, is the one that dominates near $n=1$, and replica symmetry.

11. The disconnected geometry contracts each replica's flavor with itself and gives $1/k$; the connected one undoes the cyclic contraction and gives $Z_2/Z_1^2\simeq e^{-S}$. The random-state formula gives $\frac1m+\frac1n$ at large dimensions, with $k$ in place of $m$ and $e^S$ in place of the dimension of $B$.

12. At $r=1$, $x_-=0$, $x_+=4$ and $\rho(x)=\sqrt{4-x}/2\pi\sqrt x$; the integral $\int_0^4x\log x\,\rho\,dx$ equals $\frac12$. With eigenvalues $\lambda=x/m$, $S=\log m-\int x\log x\,\rho(x)\,dx=\log m-\frac12$.

**Wiki connections.** [[replica-trick-gravity|replica trick in gravity]] · [[page-curve|Page curve]]
