---
title: "Conventions for the algebraic route"
type: course-note
edition: "2.1"
modified: 2026-09-30
---

# Course conventions

These conventions govern the new lecture notes. The earlier week-numbered drafts predate them and require translation and review before reuse.

## Systems, algebras, and states

Capital letters $A,B$ name physical systems or accessible regions; lower-case $a,b$ name logical systems. A reference system is denoted $R_0$. The same distinction is repeated locally when a new model is introduced.

$\mathcal B(\mathcal H)$ denotes all linear operators when $\mathcal H$ is finite dimensional, and all bounded operators otherwise. An observable is a self-adjoint element of the specified algebra $\mathcal M$. A state is a positive normalized linear functional $\omega$; in the finite matrix examples, $\omega(x)=\operatorname{Tr}(\rho x)$.

The commutant $\mathcal M'$ is taken in the stated ambient operator algebra. The center is $Z(\mathcal M)=\mathcal M\cap\mathcal M'$. A code commutant is taken on the logical/code Hilbert space unless another ambient space is explicitly specified. It need not be a geometric complement.

Partial traces satisfy
$$
\operatorname{Tr}_{AB}\bigl(\rho_{AB}(x_A\otimes I_B)\bigr)
=\operatorname{Tr}_A(\rho_Ax_A).
$$
Qutrit arithmetic is modulo three. For a qubit, $Z=\operatorname{diag}(1,-1)$ and $X|j\rangle=|1-j\rangle$. For a qutrit, $X|j\rangle=|j+1\rangle$, $Z|j\rangle=\zeta^j|j\rangle$, with $\zeta=e^{2\pi i/3}$.

## Entropy and distinguishability

All logarithms are natural; entropies are in nats. Divide by $\log 2$ for bits.
$$
S(\rho)=-\operatorname{Tr}\rho\log\rho,\qquad
D(\rho\Vert\sigma)=\operatorname{Tr}\rho(\log\rho-\log\sigma).
$$
We use $0\log0=0$. Relative entropy is $+\infty$ if the support of $\rho$ is not contained in that of $\sigma$. Full-rank reference states are used when an unrestricted matrix logarithm is needed.

For a finite algebra
$$
\mathcal M=\bigoplus_\alpha
\bigl(\mathcal B(\mathcal H_{a_\alpha})\otimes I_{b_\alpha}\bigr),
$$
the specified algebraic entropy is
$$
S_{\mathcal M}(\rho)=H(p_\alpha)+\sum_\alpha p_\alpha S(\rho_{a_\alpha}).
$$
This uses the trace that counts each irreducible matrix block once. Taking the ordinary ambient trace over its multiplicity space is a different convention and adds multiplicity terms. Lecture 4 derives the formula and explains its use.

In type III we do not use an intrinsic density matrix or trace entropy for a local algebra. States and Araki relative entropy remain available; relative entropy can be infinite. A regulator, a split inclusion, and a large-$N$ limit are different constructions.

## Encoding and reconstruction

An encoding $V:\mathcal H_{\mathrm{code}}\to\mathcal H_{\mathrm{physical}}$ is an isometry, $V^\dagger V=I$. The code projector is $P=VV^\dagger$.

A physical operator $O_A$ reconstructs a logical operator $O$ if
$$
(O_A\otimes I_{\bar A})V=VO.
$$
This is a statement on the whole specified code, including states entangled with a reference. Agreement on one vector or agreement of compressed matrix elements alone does not establish this intertwining identity.

An erasure removes a known subsystem. It is not the same noise problem as an arbitrary error at an unknown position.

## Modular structure and KMS

For a faithful bipartite Schmidt vector in finite dimensions,
$$
\Omega=\sum_j\sqrt{p_j}|j\rangle_A|j\rangle_B,\qquad p_j>0,
$$
we use
$$
S_T(x\Omega)=x^\dagger\Omega,\quad
S_T=J\Delta^{1/2},\quad
\Delta=\rho_A\otimes\rho_B^{-1}.
$$
The subscript distinguishes the Tomita map $S_T$ from entropy $S$.

The modular flow agrees with the canonical AQFT course:
$$
\sigma_t^\omega(x)=\Delta^{-it}x\Delta^{it}.
$$
On the $A$ algebra this is $\rho_A^{-it}x\rho_A^{it}$. Define
$$
K_A=-\log\rho_A,\qquad
\widehat K=-\log\Delta=K_A\otimes I-I\otimes K_B.
$$
The full modular generator $\widehat K$ is not the one-sided operator $K_A$, and $\Delta$ is not $\rho_A$.

The upper-strip KMS convention is
$$
F_{a,b}(t)=\omega(a\sigma_t(b)),\qquad
F_{a,b}(t+i)=\omega(\sigma_t(b)a).
$$
The strip has dimensionless height one for this modular parameter. For a Gibbs state $\rho_\beta=e^{-\beta H}/Z$ and physical Heisenberg evolution $\alpha_s(x)=e^{isH}xe^{-isH}$,
$$
\sigma_t^\beta=\alpha_{\beta t}.
$$
Thus physical time is $s=\beta t$. A source using the opposite modular-flow sign must be translated before a formula is imported.

For the Rindler wedge of Lecture 10, $U(\Lambda(u))=e^{iuK}$ and $\Delta_W=e^{-2\pi K}$; modular time corresponds to rapidity $u=2\pi t$. Here $K$ is the full boost generator, as in the AQFT course (edition 2.1 of this course called it $B$). A one-sided stress-tensor expression requires its own regulated or algebraic interpretation.

## Geometry and the dictionary

We use $\hbar=c=k_B=1$ and the mostly-plus Lorentzian signature. The AdS radius $L$ is retained when checking dimensions:
$$
ds^2=\frac{L^2}{z^2}(-dt_{\mathrm{phys}}^2+d\mathbf x^2+dz^2).
$$
The finite-code operator $\mathcal L_A$ is dimensionless and has units of entropy. Its identification with $\widehat{\operatorname{Area}}/(4G_N)$ is additional holographic input.

For the Euclidean source convention,
$$
Z_{\mathrm{CFT}}[J]=\left\langle e^{\int J\mathcal O}\right\rangle,
\qquad
Z_{\mathrm{grav}}[J]\simeq e^{-I_{\mathrm{ren}}[\phi_{\mathrm{cl}}[J]]}.
$$
The bulk saddle is an approximation. In the standard scalar quantization,
$$
m^2L^2=\Delta_{\mathcal O}(\Delta_{\mathcal O}-d),\qquad
\phi\sim z^{d-\Delta_{\mathcal O}}J+z^{\Delta_{\mathcal O}}A+\cdots.
$$
The response coefficient $A$ is proportional to the expectation value; the proportionality depends on action normalization and counterterms and must be derived in the relevant lecture. We do not set it to one by omission.

The active notes do not import the historical $cR/12$ anomaly formula. A future anomaly calculation must declare its action, stress-tensor normalization, curvature convention, and factors of $2\pi$.

Large-$N$ fluctuations are normalized by the scaling of their connected two-point function, not by a universal prefactor in front of a trace. Their normalization depends on the action and field conventions. Local type-III structure in a continuum theory must not be equated with the emergence of a particular large-$N$ single-trace representation.

## Recovery, replicas, and the JT example

Root fidelity is $F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1$. Bounds written with $-2\log F$ use this convention; squared fidelity changes the coefficient. Inverses in the Petz map are supported inverses, and a completion outside the relevant output support must be declared.

Replica moments are normalized: $\operatorname{Tr}\rho^n=\mathcal Z_n/\mathcal Z_1^n$. An unnormalized path integral cannot be differentiated as if its value at one were automatically one.

Lectures 25–27 set the AdS$_2$ radius to one and use an entropy-normalized dilaton $\varphi=\Phi/(4G_2)$. A gravitational endpoint contributes $S_0+\varphi$. The renormalized endpoint counterterm and the radiation cutoff are held fixed when comparing saddles. The thermal calculation sets $\beta=2\pi$ until physical time is restored explicitly. It is an equilibrium model.

For half-sided inclusions, Lectures 30–31 choose $\sigma_s=\operatorname{Ad}\Delta^{-is}$, compression for $s\geq0$, and $U(a)=e^{iaP}$ with $P\geq0$. The relation is
$$
\Delta^{-is}U(a)\Delta^{is}=U(e^{2\pi s}a).
$$
The half-line moves from $(0,\infty)$ to $(a,\infty)$ for positive $a$. A source with the opposite half-sided orientation needs the corresponding sign translation.
