---
title: "Lecture 30 — Nested algebras and half-sided modular inclusions"
type: lecture-notes
edition: "2.2 — rewritten at the AQFT standard"
lecture: 30
semester: 2
week: 13
hours: 3
prerequisites: "Lectures 3, 9, 10, 28 and 29; Takesaki's theorem, one-parameter unitary groups and their generators"
status: "rewritten 2026-09-30, pending instructor review; the composition of two dilations, the one-particle structure of the chiral current with its dilations, translations, affine relation and generators, the KMS property of the dilation flow, Wiesbrock's product in the model, the relation between the modular Hamiltonians of two half-lines and the finite-dimensional obstruction are exact calculations or proofs; Borchers' theorem is sketched; Wiesbrock's theorem, the type III1 property, the Möbius construction and the null-plane results are stated with sources"
modified: 2026-09-30
---

# Lecture 30 — Nested algebras and half-sided modular inclusions

> *A von Neumann algebra with a cyclic and separating vector has one modular flow. Lecture 29 found that the large-$N$ algebras of the black-hole phase are factors not of type I, which Leutheusser and Liu identified as type III$_1$, with outer modular flows and no density matrices, and this lecture asks what two such algebras, one inside the other, can do together. Borchers proved in 1992 that if a unitary group with positive generator and an invariant vacuum maps an algebra into itself for positive arguments, then the modular group of the algebra dilates it. Wiesbrock proved the converse in 1993: if the modular flow of the larger algebra compresses the smaller one into itself for positive modular time, then the two modular flows generate a translation with positive generator, and the smaller algebra is the translate of the larger one. We develop both theorems in the chiral current on a light ray, where the two flows are dilations about two points and every relation can be computed, and we prove that no finite-dimensional system realizes them. The difference of two modular Hamiltonians is then a positive operator, which in a conformal theory is the averaged null energy, and this is how a null direction can be recovered from algebraic data alone.*

## How to use this lecture

**Classroom core, one meeting of three hours.** The history (§1, 10 minutes), two clocks on a light ray (§2, 15 minutes), and the chiral current with its dilations and translations (§3, 30 minutes) come before a 10-minute break. After it come the theorems of Borchers and Wiesbrock (§4, 35 minutes), what the hypotheses exclude (§5, 15 minutes), and a null translation recovered from two modular Hamiltonians (§6, 25 minutes), with 40 minutes for Checkpoints 1 and 2 and Problems 4–6; Problems 1–3 complete the core assignment. These allocations are proposals and have not been tested in class.

**Self-study.** Standard inclusions and the Möbius group (§7), inclusions in the black-hole interior (§8), and Problems 7–12, including Wiesbrock's product, the strip of analyticity and the truncated relation.

**Research extension.** The quantum null energy condition from inclusions, the Möbius group of a standard inclusion, and a double-trace inclusion, in Problems 13–15.

**Prerequisites.** Lecture 3 for modular operators and conjugations, Lecture 9 for Weyl operators and the Reeh–Schlieder property, Lecture 10 for the Bisognano–Wichmann theorem and the upper-strip KMS convention, Lecture 28 for the conformal modular flow of Brunetti, Guido and Longo, Lecture 29 for quasi-free states and the type of large-$N$ algebras. Takesaki's theorem, one-parameter unitary groups and their generators.

**What this lecture establishes.** The composition of two dilations into a translation, the one-particle structure of the chiral current with its dilations, translations, affine relation and generators, the KMS property of the dilation flow, Wiesbrock's product computed in the model, the relation $\hat K_a-\hat K_b=2\pi(b-a)P$ between modular Hamiltonians of half-lines, and the impossibility of a nontrivial realization in finite dimensions are exact calculations or proofs. Borchers' theorem is sketched through the analyticity argument that produces the factor $2\pi$. Wiesbrock's theorem, the type III$_1$ property of algebras with half-sided translations, the Möbius group of a standard inclusion and the modular Hamiltonians of null cuts are stated with sources.

## 0. Reading

**Primary.**

- H. J. Borchers, "On revolutionizing quantum field theory with Tomita's modular theory," *J. Math. Phys.* 41 (2000) 3604, sections II.2–II.6.
- H.-W. Wiesbrock, "Half-sided modular inclusions of von Neumann algebras," *Commun. Math. Phys.* 157 (1993) 83; erratum 184 (1997) 683.
- H. Araki, L. Zsidó, [Extension of the structure theorem of Borchers and its application to half-sided modular inclusions](https://arxiv.org/abs/math/0412061) (2004).

**Secondary.**

- H. J. Borchers, "The CPT-theorem in two-dimensional theories of local observables," *Commun. Math. Phys.* 143 (1992) 315.
- M. Florig, "On Borchers' theorem," *Lett. Math. Phys.* 46 (1998) 289.
- H. J. Borchers, "Half-sided translations and the type of von Neumann algebras," *Lett. Math. Phys.* 44 (1998) 283.
- H. Casini, E. Teste, G. Torroba, [Modular Hamiltonians on the null plane and the Markov property of the vacuum state](https://arxiv.org/abs/1703.10656) (2017).
- R. Brunetti, D. Guido, R. Longo, [Modular localization and Wigner particles](https://arxiv.org/abs/math-ph/0203021) (2002).

**Optional research reading.**

- F. Ceyhan, T. Faulkner, [Recovering the QNEC from the ANEC](https://arxiv.org/abs/1812.04683) (2018).
- R. Jefferson, [Comments on black hole interiors and modular inclusions](https://arxiv.org/abs/1811.08900) (2018).
- D. Guido, R. Longo, H.-W. Wiesbrock, [Extensions of Conformal Nets and Superselection Structures](https://arxiv.org/abs/hep-th/9703129) (1997).

## 1. Can two modular clocks define a translation?

The Bisognano–Wichmann theorem of 1975 identified the modular group of a wedge in the vacuum with its boosts (Lecture 10), and until 1992 the identification ran in one direction, from a known geometric action to the modular group. Borchers reversed it that year. He showed that the relation between the boosts of a wedge and the lightlike translations that map the wedge into itself follows from the algebra alone. A unitary group with positive generator that fixes the vacuum and maps the wedge algebra into itself for positive arguments is dilated by the modular group, exactly as a null translation is rescaled by a boost. The theorem was the input for the conformal Bisognano–Wichmann theorem of Brunetti, Guido and Longo that Lecture 28 used, and Florig later gave it a proof that uses functions of one variable.

Wiesbrock asked in 1993 for the converse, and found it in a property of two algebras. If $\mathcal N\subset\mathcal M$ share a cyclic and separating vector and the modular flow of $\mathcal M$ compresses $\mathcal N$ into itself for positive modular time, the two modular groups generate a translation with positive generator. He called the property a half-sided modular inclusion, and gave conditions under which a single inclusion of this kind reconstructs a chiral conformal field theory. Araki and Zsidó later filled a gap in his proof and extended the theorem to weights. In this century the structure entered high-energy physics through the averaged null energy. Casini, Teste and Torroba found in 2017 that the modular Hamiltonians of regions cut along a null plane are local integrals of the stress tensor, and Ceyhan and Faulkner derived the quantum null energy condition from half-sided inclusions in 2018. In 2021 Leutheusser and Liu used the inclusions of large-$N$ algebras to construct time evolutions inside a black hole, the subject of Lecture 31.

## 2. Two clocks on a light ray

Consider a light ray with coordinate $u$ and the half-lines $(0,\infty)\supset(1,\infty)$. The dilation about a point $b$ with parameter $s$,

$$
d_b(s):\ u\longmapsto b+e^{2\pi s}(u-b),
$$

preserves $(b,\infty)$. Section 3 identifies $d_0$ with the modular flow of the algebra of $(0,\infty)$ in the vacuum, and $d_1$ with that of $(1,\infty)$. Two observations contain the whole lecture in classical form. First, the flow about $0$ compresses the smaller half-line for one sign of $s$ only:

$$
d_0(s)\bigl((1,\infty)\bigr)=(e^{2\pi s},\infty)\subset(1,\infty)\quad\text{for }s\geq0 .
$$

Second, running one clock forward and the other backward by the same amount leaves only a translation,

$$
d_0(s)\circ d_1(-s):\ u\longmapsto e^{2\pi s}\bigl(1+e^{-2\pi s}(u-1)\bigr)=u+\bigl(e^{2\pi s}-1\bigr).
$$

[Exact (Problem 1).] The two dilations generate the affine group of the line, and the translations are the part on which they disagree. Figure (a) shows the orbits of the two flows.

![[ads-cft-half-sided-inclusions.svg|Left: orbits of the two modular flows on the light ray against the modular parameter s, dilations about u equal to 0 as solid curves and dilations about u equal to 1 as dashed curves; the half-line u greater than 1 is the region of N, and the band between 0 and 1 belongs to M and not to N. Right: the relative defect of the relation i(K,P) equal to 2πP for wave packets on a finite grid in log p, as a function of the packet center; it is small in the interior of the grid and grows sharply at both edges.]]

## 3. The chiral current on a light ray

The model is the chiral current of a two-dimensional massless scalar, a field $j(u)$ on the light ray with vacuum two-point function

$$
\langle\Omega|j(u)j(v)|\Omega\rangle=-\frac1{2\pi\,(u-v-i0)^2}=\int_0^\infty\frac{p\,dp}{2\pi}\,e^{-ip(u-v)} ,
$$

and commutator $[j(u),j(v)]=i\,\delta'(u-v)$. [Exact calculation, checked symbolically (Problem 2).] For a real test function $g$, the smeared field $j(g)=\int g\,j$ creates the one-particle vector $\tilde g(p)=\int g(v)\,e^{ipv}\,dv$, restricted to $p>0$, in the space

$$
\mathfrak h=L^2\Bigl(\mathbb R_+,\frac{p\,dp}{2\pi}\Bigr),\qquad \langle g,h\rangle=\int_0^\infty\frac{p\,dp}{2\pi}\,\overline{\tilde g(p)}\,\tilde h(p) ,
$$

and $[j(g),j(h)]=i\int g\,h'\,du$. The vacuum is quasi-free in the sense of Lecture 29, and the algebra $\mathcal A(I)$ of an interval or half-line $I$ is generated by the Weyl operators $e^{ij(g)}$ with $\operatorname{supp}g\subset I$. By the Reeh–Schlieder property, $\Omega$ is cyclic and separating for $\mathcal A((b,\infty))$.

Translations and dilations act on test functions by $g(u)\mapsto g(u-a)$ and $g(u)\mapsto g(u/\lambda)$, with $\lambda=e^{2\pi s}$; the current has dimension one, so $j(u)\mapsto\lambda\,j(\lambda u)$. On one-particle vectors,

$$
\bigl(U(a)\tilde g\bigr)(p)=e^{ipa}\,\tilde g(p),\qquad \bigl(D(s)\tilde g\bigr)(p)=\lambda\,\tilde g(\lambda p) .
$$

[Exact.] Both are unitary on $\mathfrak h$: for $D(s)$ the substitution $p'=\lambda p$ turns $\lambda^2p\,dp$ into $p'\,dp'$. The generator of $U(a)=e^{iaP}$ is multiplication by $p$, which is positive. Direct substitution gives the affine relation

$$
D(s)\,U(a)\,D(s)^\dagger=U\bigl(e^{2\pi s}a\bigr).
$$

Writing $D(s)=e^{isK}$, differentiation at $s=0$ gives $iK\tilde g=2\pi(\tilde g+p\,\tilde g')$, and therefore

$$
K=-2\pi i\Bigl(1+p\frac{d}{dp}\Bigr),\qquad i[K,P]=2\pi P,\qquad U(b)\,K\,U(b)^\dagger=K-2\pi b\,P .
$$

[Exact calculation, checked symbolically (Problem 5).] The constant $1$ in $K$ makes it symmetric for the measure $p\,dp$.

Now identify the modular group. For $u,v>0$, the dilated two-point function $F(s)=\langle\Omega|j(u)\,\lambda j(\lambda v)|\Omega\rangle=-\lambda/2\pi(u-\lambda v-i0)^2$ continues in $z=s+i\theta$ to

$$
F(z)=-\frac{e^{2\pi z}}{2\pi\,(u-e^{2\pi z}v)^2},
$$

which is analytic in the strip $0<\theta<1$, since $e^{2\pi z}v$ is real and positive only on its edges. At $\theta\to1^-$ the denominator approaches $u-\lambda v$ from the side opposite to the one at $\theta\to0^+$, and $F(s+i)=\langle\Omega|\lambda j(\lambda v)\,j(u)|\Omega\rangle$. This is the upper-strip KMS condition of Lecture 10 at unit modular temperature. [Exact calculation, checked numerically.] For a quasi-free state the condition on two-point functions extends to the Weyl operators, and by Takesaki's theorem the dilation flow is the modular group:

$$
\Delta_{\mathcal M}^{-is}=D(s)\quad\text{for }\mathcal M=\mathcal A((0,\infty)).
$$

[Exact calculation for the two-point function. The extension to the Weyl algebra, standard for quasi-free states, is stated only — refs: Brunetti–Guido–Longo 1993, which gives the same modular group.] It agrees with the conformal Bisognano–Wichmann theorem of Lecture 28. For $\mathcal N=\mathcal A((1,\infty))=U(1)\,\mathcal M\,U(1)^\dagger$, which shares the vacuum, $\Delta_{\mathcal N}^{-is}=U(1)D(s)U(1)^\dagger$ is the dilation about $1$, and the modular Hamiltonians $\hat K=-\log\Delta$ are

$$
\hat K_{\mathcal M}=K,\qquad \hat K_{\mathcal N}=K-2\pi P .
$$

The two flows compose as in §2. On one-particle vectors,

$$
\Delta_{\mathcal M}^{-is}\,\Delta_{\mathcal N}^{is}=D(s)\,U(1)\,D(s)^\dagger\,U(1)^\dagger=U\bigl(e^{2\pi s}\bigr)\,U(-1)=U\bigl(e^{2\pi s}-1\bigr).
$$

[Exact (Problem 7).]

**Checkpoint 1.** Is $\Delta_{\mathcal M}^{-is}\,\mathcal N\,\Delta_{\mathcal M}^{is}$ contained in $\mathcal N$ for $s<0$?

**Answer.** No. For $s<0$ the dilation maps $(1,\infty)$ onto $(e^{2\pi s},\infty)$, which contains $(1,\infty)$ and the interval $(e^{2\pi s},1)$, and the image algebra contains operators of that interval, which do not belong to $\mathcal N$. The compression holds for one sign of $s$ only.

## 4. The theorems of Borchers and Wiesbrock

The model shows the structure; the theorems show that it is forced by the algebras.

**Theorem (Borchers). Sketched.** Let $\mathcal M$ be a von Neumann algebra with a cyclic and separating vector $\Omega$, and let $U(a)=e^{iaP}$ be a strongly continuous unitary group with $P\geq0$, $U(a)\Omega=\Omega$, and $U(a)\,\mathcal M\,U(a)^\dagger\subset\mathcal M$ for $a\geq0$. Then, for all real $s$ and $a$,

$$
\Delta^{-is}\,U(a)\,\Delta^{is}=U\bigl(e^{2\pi s}a\bigr),\qquad J\,U(a)\,J=U(-a).
$$

[Sketched — refs: Borchers 1992; Florig 1998; Borchers 2000.]

*Sketch.* Positivity of $P$ makes $a\mapsto U(a)$ analytic and contractive in the upper half-plane, since $\|e^{iaP}\|=1$ for real $a$ and $e^{iaP}$ decays for $\operatorname{Im}a>0$. The map $a=e^{2\pi z}$ takes the strip $0<\operatorname{Im}z<\frac12$ onto the upper half-plane, so $W(z)=U(e^{2\pi z})$ is analytic and bounded in the strip, with unitary boundary values $W(s)=U(e^{2\pi s})$ and $W(s+\frac i2)=U(-e^{2\pi s})$. On the lower edge $W$ maps $\mathcal M$ into itself; on the upper edge it maps $\mathcal M'$ into itself, because the inclusion for $a\geq0$ implies $U(a)\,\mathcal M'\,U(a)^\dagger\subset\mathcal M'$ for $a\leq0$ (Problem 12). The strip of width $\frac12$ is the domain in which $\Delta^{1/2}$-analyticity holds for the modular group, and Borchers' second fundamental relation turns a family with these properties into the covariance law $\Delta^{-it}W(s)\Delta^{it}=W(s+t)$. Setting $a=e^{2\pi s}$ gives the dilation law for $a>0$, and the conjugation and analyticity extend it to $a<0$. $\square$

The factor $2\pi$ thus has a precise origin: it is the factor that maps the strip of modular analyticity, of width $\frac12$, onto the half-plane of positive-energy analyticity.

**Theorem (Wiesbrock). Stated only.** Let $\mathcal N\subset\mathcal M$ be von Neumann algebras with a common cyclic and separating vector $\Omega$, and suppose

$$
\Delta_{\mathcal M}^{-is}\,\mathcal N\,\Delta_{\mathcal M}^{is}\subset\mathcal N\qquad\text{for }s\geq0 .
$$

Then there is a unique strongly continuous unitary group $U(a)=e^{iaP}$ with $P\geq0$ and $U(a)\Omega=\Omega$, such that $U(a)\,\mathcal M\,U(a)^\dagger\subset\mathcal M$ for $a\geq0$, $\mathcal N=U(1)\,\mathcal M\,U(1)^\dagger$, and

$$
\Delta_{\mathcal M}^{-is}\,\Delta_{\mathcal N}^{is}=U\bigl(e^{2\pi s}-1\bigr).
$$

[Stated only — refs: Wiesbrock 1993; Araki–Zsidó 2004; Borchers 2000.] The proof defines $U$ on $a>-1$ by the last formula, as in the model, and shows that the products $\Delta_{\mathcal M}^{-is}\Delta_{\mathcal N}^{is}$ for different $s$ commute and add, using the two fundamental relations of Borchers; the group then extends to all $a$, and its generator is positive. In Borchers' terminology $U$ is a half-sided translation of $\mathcal M$, and the two theorems say that half-sided translations and half-sided modular inclusions are the same structure seen from two sides.

Two consequences follow at once, and a third is a separate theorem. The modular flow of the translated algebra is the translated flow, $\Delta_{\mathcal N}^{-is}=U(1)\Delta_{\mathcal M}^{-is}U(1)^\dagger$, because $U(1)$ fixes $\Omega$. Differentiating the dilation law on a common core gives

$$
i\,[\hat K_{\mathcal M},P]=2\pi P,\qquad \hat K_{\mathcal N}=\hat K_{\mathcal M}-2\pi P ,
$$

so that the generator of the translation is the difference of two modular Hamiltonians divided by $2\pi$, a positive operator although each of the two has spectrum $\mathbb R$. And the algebra cannot be finite: if, in addition, $\Omega$ is the only vector invariant under $U$ and $P\neq0$, then $\mathcal M$ is a factor of type III$_1$. [Stated only — refs: Borchers 1998; Borchers 2000, Theorem V.3.2.] The large-$N$ algebras of the black-hole phase carry half-sided translations, as Leutheusser and Liu found and Lecture 31 shows in a model, and this theorem is one route to their type.

## 5. What the hypotheses exclude

Each hypothesis does work. The compression must be one-sided: if $\Delta_{\mathcal M}^{-is}\mathcal N\Delta_{\mathcal M}^{is}\subset\mathcal N$ for all real $s$, then $\mathcal N$ is invariant under the modular group of $\mathcal M$, and since $\Omega$ is cyclic for $\mathcal N$, Takesaki's theorem on invariant subalgebras gives $\mathcal N=\mathcal M$ (Problem 9). The vector must be common to both algebras, since the construction compares their modular operators. And the system must be infinite.

**Proposition (no finite realization). Proved.** If $K$ and $P$ are Hermitian matrices with $P\geq0$ and $i[K,P]=2\pi P$, then $P=0$.

*Proof.* The trace of a commutator of matrices vanishes, so $2\pi\operatorname{Tr}P=i\operatorname{Tr}[K,P]=0$. A positive matrix with zero trace is zero. $\square$

The conclusion holds without positivity, which only the trace argument needs: in an eigenbasis of $K$ the relation reads $(k_m-k_n)P_{mn}=-2\pi i\,P_{mn}$, and since $k_m-k_n$ is real every entry of $P$ vanishes, whatever its sign.

The same conclusion holds for bounded operators with the group law itself: if $e^{isK}Pe^{-isK}=e^{2\pi s}P$ with $P$ bounded and $K$ self-adjoint, then $\|P\|=e^{2\pi s}\|P\|$ for every $s$, so $P=0$. The finite models of the first semester can therefore illustrate a modular clock, a code and a recovery map, but no finite system has two nested algebras whose modular flows produce a translation. A truncation can approximate the relation on a chosen set of vectors and must break it elsewhere. Figure (b) shows this for the model of §3 written in $x=\log p$, where $K=-2\pi i\,\partial_x$ and $P=e^x$ on $L^2(\mathbb R,dx)$: on a grid of $600$ points with $|x|\leq6$ and a central difference for $\partial_x$, the relative defect $\|(i[K,P]-2\pi P)v\|/\|2\pi Pv\|$ of a wave packet $v$ is small in the interior and large near the edges. The trace argument requires the relation to fail somewhere. For smooth packets the truncation puts the failure at the edges, and packets that vary on the scale of the grid carry the rest, since the diagonal of the discrete commutator vanishes identically while that of $2\pi P$ does not. [Numerical, in a defined model.]

**Checkpoint 2.** In the model, $\hat K_{\mathcal M}$ and $\hat K_{\mathcal N}$ both have spectrum $\mathbb R$, and their difference $2\pi P$ is positive. Which hypothesis of Wiesbrock's theorem produces the sign?

**Answer.** The inclusion $\mathcal N\subset\mathcal M$ itself. For any inclusion with a common cyclic and separating vector, $\Delta_{\mathcal N}\geq\Delta_{\mathcal M}$ in the sense of forms (Borchers 2000, eq. II.1.3), and since the logarithm is operator monotone, $\hat K_{\mathcal M}-\hat K_{\mathcal N}\geq0$; Wiesbrock's theorem identifies the difference with $2\pi P$. The direction of the compression decides whether $U(a)$ maps $\mathcal M$ into itself for $a\geq0$, as here, or for $a\leq0$, as in Lecture 31, where $\hat K_{\mathcal M}-\hat K_{\mathcal N}=2\pi bP$ is again positive.

## 6. A null translation from two modular Hamiltonians

Return to the model and consider all the half-lines $(b,\infty)$. Their modular Hamiltonians satisfy $\hat K_b=U(b)\hat K_0U(b)^\dagger=\hat K_0-2\pi bP$, so for $a<b$

$$
\hat K_a-\hat K_b=2\pi(b-a)\,P\geq0 .
$$

[Exact.] The modular Hamiltonian decreases as the cut moves forward along the ray, and its rate of change is $-2\pi P$. In the chiral theory with stress tensor $T(u)$ the generators are local,

$$
\hat K_b=2\pi\int_{-\infty}^\infty(u-b)\,T(u)\,du,\qquad P=\int_{-\infty}^\infty T(u)\,du ,
$$

the second being the averaged null energy along the ray. [Stated only — refs: Lecture 10; Casini–Teste–Torroba 2017.] The two expressions are the full modular Hamiltonians, which act on both sides of the cut with opposite signs, as $-\log\Delta$ always does. Positivity of $P$ is thus the averaged null energy condition on the ray, and the theorems of §4 tie it to the inclusion of the two algebras: given the half-sided inclusion, Wiesbrock's theorem produces a positive generator, and given a positive generator, Borchers' theorem produces the modular covariance.

In higher dimensions the algebra of the region above a cut $\lambda=\gamma(y)$ of a null plane, with $y$ the transverse coordinates, has the local modular Hamiltonian

$$
\hat K_\gamma=2\pi\int d^{d-2}y\int_{-\infty}^\infty d\lambda\,\bigl(\lambda-\gamma(y)\bigr)\,T_{\lambda\lambda}(\lambda,y),
$$

where $\lambda$ is the affine parameter along the null generators. [Stated only — refs: Casini–Teste–Torroba 2017.] The modular flow of the region above $\gamma_1$ moves each null generator by $\lambda\mapsto\gamma_1+e^{2\pi s}(\lambda-\gamma_1)$, so it compresses the region above a later cut $\gamma_2\geq\gamma_1$ for $s\geq0$, and the two modular Hamiltonians differ by $2\pi\int d^{d-2}y\,(\gamma_2-\gamma_1)(y)\int T_{\lambda\lambda}\,d\lambda$, a weighted integral of the null energy. Ceyhan and Faulkner used inclusions of this kind, together with relative modular flow, to derive the quantum null energy condition from the averaged one. [Stated only — refs: Ceyhan–Faulkner 2018.]

> **Physical picture: a null translation is the mismatch of two clocks.** Each algebra comes with its own modular clock, the boost about its own edge. Run the clock of the larger algebra forward and that of the smaller one backward by the same amount: every point returns except for a shift along the ray. The two clocks agree about everything but a translation, and the translation is null and has positive energy because the edges are ordered along a light ray. In a theory where the algebras are known and the geometry is not, this is how a null direction, and an affine parameter along it, can be read off from modular data.

## 7. Self-study: standard inclusions and the Möbius group

An inclusion is called standard when $\Omega$ is also cyclic for the relative commutant $\mathcal N'\cap\mathcal M$. In the model the relative commutant contains the algebra of the interval $(0,1)$, whose modular flow is the Möbius flow fixing $0$ and $1$. The three modular groups of $\mathcal M$, $\mathcal N$ and $\mathcal N'\cap\mathcal M$ generate the dilations about two points and a third one-parameter group, which together generate $PSL(2,\mathbb R)$. Wiesbrock formulated conditions under which this is general: a standard half-sided modular inclusion then determines a local net on the circle, covariant under a positive-energy representation of the Möbius group. [Stated only — refs: Wiesbrock 1993; erratum 1997.] Guido, Longo and Wiesbrock showed with these methods that the dual net of a conformal net on the line is again conformal, for a new representation of the Möbius group. [Stated only — refs: Guido–Longo–Wiesbrock 1997.]

A conformal field theory on a light ray can thus be specified by two algebras and a vector, without fields and without a stress tensor. This is the converse of Lecture 28, where a net was given and its modular structure computed.

## 8. Self-study: inclusions behind a horizon

In the thermofield double at large $N$, the algebra of single-trace operators of one boundary at times earlier than $t_0$ is included in the algebra of all times. The modular flow of the larger algebra is time translation (Lecture 23), and for negative modular time it moves the band of earlier times into itself, so the inclusion is half-sided with the opposite sign to §4. Leutheusser and Liu identified half-sided inclusions of this kind among the large-$N$ algebras of the black-hole phase and used them to construct translations that move operators along a null direction across the future horizon. [Stated only — refs: Leutheusser–Liu 2021.] Jefferson showed that the traversable wormhole produced by a double-trace coupling of the two boundaries can be described as a modular inclusion of the exterior algebras, with a nontrivial relative commutant that corresponds to a new region deep in the bulk. [Stated only — refs: Jefferson 2018.] Lecture 31 constructs the first of these structures exactly in the outgoing sector of the JT model of Lecture 25.

## 9. What to take away

- **Exact:** the dilations about two points of a light ray compose into a translation, $d_0(s)\circ d_1(-s)=u\mapsto u+e^{2\pi s}-1$, and the flow about $0$ compresses the half-line $(1,\infty)$ for $s\geq0$ only.
- **Exact, in the chiral current:** dilations $\lambda\tilde g(\lambda p)$ and translations $e^{ipa}$ on $L^2(\mathbb R_+,p\,dp/2\pi)$ satisfy the affine relation, with $K=-2\pi i(1+p\,d/dp)$, $i[K,P]=2\pi P$ and $\hat K_{\mathcal N}=\hat K_{\mathcal M}-2\pi P$; the dilation flow satisfies the KMS condition and is the modular group of the half-line.
- **Sketched:** Borchers' theorem, a positive translation that maps an algebra into itself is dilated by its modular group; the factor $2\pi$ maps the modular strip of width $\frac12$ onto the upper half-plane.
- **Stated:** Wiesbrock's converse, $\Delta_{\mathcal M}^{-is}\Delta_{\mathcal N}^{is}=U(e^{2\pi s}-1)$ for a half-sided modular inclusion, and the type III$_1$ property of algebras with half-sided translations.
- **Proved:** no finite-dimensional system realizes the structure; in the chiral current $\hat K_a-\hat K_b=2\pi(b-a)P\geq0$ for nested half-lines (exact), and the identification of $P$ with the averaged null energy is stated.

## 10. Looking ahead

Lecture 31 applies Wiesbrock's theorem to the outgoing sector of the JT model of Lecture 25. The algebra of the right boundary at times before $t_0$ sits inside the algebra of all times, the inclusion is half-sided, and the translation it generates continues the outgoing coordinate past the future horizon. That construction is the algebraic model of emergent time.

## 11. Problem set

### Classroom core

1. **Two dilations.** Compute $d_0(s)\circ d_b(-s)$ for a general $b$, and show that $d_0(s)$ maps $(b,\infty)$ into itself for $s\geq0$ when $b>0$.

2. **The current in momentum space.** Show that $\int_0^\infty\frac{p\,dp}{2\pi}e^{-ip(x-i\epsilon)}=-1/2\pi(x-i\epsilon)^2$, and derive $[j(u),j(v)]=i\delta'(u-v)$ and $[j(g),j(h)]=i\int g\,h'$.

3. **Unitarity and the affine relation.** Verify that $D(s)$ is unitary on $L^2(\mathbb R_+,p\,dp/2\pi)$ and that $D(s)U(a)D(s)^\dagger=U(e^{2\pi s}a)$.

4. **The KMS condition.** For $u,v>0$, verify that $F(z)=-e^{2\pi z}/2\pi(u-e^{2\pi z}v)^2$ is analytic for $0<\operatorname{Im}z<1$, and that its boundary values at $\operatorname{Im}z=0$ and $1$ are the two orderings of the dilated two-point function.

5. **The generators.** Derive $K=-2\pi i(1+p\,d/dp)$, show that it is symmetric on smooth functions of compact support in $(0,\infty)$, and verify $i[K,P]=2\pi P$ and $U(b)KU(b)^\dagger=K-2\pi bP$.

6. **No finite realization.** Prove the proposition of §5, and show that boundedness of $P$ with the group law already forces $P=0$. Why does the trace argument need $P\geq0$?

### Self-study consolidation

7. **Wiesbrock's product.** In the model, compute $\Delta_{\mathcal M}^{-is}\Delta_{\mathcal N}^{is}$ on one-particle vectors and verify $U(e^{2\pi s}-1)\,U(e^{2\pi t}-1)=U(e^{2\pi s}+e^{2\pi t}-2)$.

8. **The strip and the half-plane.** Show that $z\mapsto e^{2\pi z}$ maps $0<\operatorname{Im}z<\frac12$ onto the upper half-plane, and that $e^{iaP}$ with $P\geq0$ is a contraction for $\operatorname{Im}a\geq0$.

9. **Compression for all times.** Suppose $\Delta_{\mathcal M}^{-is}\mathcal N\Delta_{\mathcal M}^{is}\subset\mathcal N$ for all real $s$. Show that equality holds for every $s$, and use Takesaki's theorem, that a von Neumann subalgebra invariant under the modular group and with $\Omega$ cyclic coincides with $\mathcal M$, to conclude $\mathcal N=\mathcal M$.

10. **Modular Hamiltonians of half-lines.** From $\hat K_b=\hat K_0-2\pi bP$, derive $\hat K_a-\hat K_b=2\pi(b-a)P$, and compute $\langle g,(\hat K_a-\hat K_b)\,g\rangle$ for a one-particle vector in terms of $\tilde g$.

11. **The truncated relation.** In the variable $x=\log p$, show that $L^2(\mathbb R_+,p\,dp)\to L^2(\mathbb R,dx)$, $\tilde g\mapsto e^x\tilde g(e^x)$, is unitary and turns $K$ into $-2\pi i\,\partial_x$. Explain why a central difference on a finite grid satisfies the relation to second order in the spacing in the interior and fails at the edges.

12. **Two compressions.** Show that $U(a)\mathcal MU(a)^\dagger\subset\mathcal M$ for $a\geq0$ implies $U(a)\mathcal M'U(a)^\dagger\subset\mathcal M'$ for $a\leq0$, and describe both statements geometrically for $\mathcal M=\mathcal A((0,\infty))$.

### Research extension

13. **The quantum null energy condition.** *Known:* Ceyhan and Faulkner derive the quantum null energy condition from the averaged one using half-sided inclusions and relative modular flow. *Completion:* a direct verification in the chiral current for coherent states, where the relative entropy of a cut is computable, with the second variation in the cut position written in terms of the profile of the state.

14. **The Möbius group of a standard inclusion.** *Known:* Wiesbrock showed that a standard half-sided modular inclusion determines a Möbius-covariant net on the circle. *Completion:* in the chiral current, the modular group of $\mathcal A((0,1))$ as a one-particle operator, and an explicit check that the three generators close into the Lie algebra of $PSL(2,\mathbb R)$.

15. **A double-trace inclusion.** *Known:* Jefferson describes the Gao–Jafferis–Wall wormhole as a modular inclusion of exterior algebras with a nontrivial relative commutant. *Completion:* a chiral model in which a unitary coupling of two light rays shifts the outgoing sector, the resulting inclusion, and the algebra that plays the role of the new bulk region.

## 12. Answer checkpoints

1. $d_0(s)\circ d_b(-s)(u)=e^{2\pi s}\bigl(b+e^{-2\pi s}(u-b)\bigr)=u+b(e^{2\pi s}-1)$, a translation. For $s\geq0$ and $u>b>0$, $e^{2\pi s}u\geq u>b$.

2. $\int_0^\infty p\,e^{-ipy}\,dp=1/(iy)^2=-1/y^2$ for $\operatorname{Im}y<0$, with $y=x-i\epsilon$. The commutator is $\int_{\mathbb R}\frac{p\,dp}{2\pi}e^{-ipx}=i\,\partial_x\delta(x)$. Smearing, $\int\!\!\int g(u)h(v)\,i\delta'(u-v)=-i\int g'h=i\int g\,h'$.

3. $\int_0^\infty p\,|\lambda\tilde g(\lambda p)|^2dp=\int_0^\infty p'|\tilde g(p')|^2dp'$ with $p'=\lambda p$. Then $D(s)U(a)D(s)^\dagger\tilde g(p)=\lambda\,e^{i\lambda pa}\,\lambda^{-1}\tilde g(p)=e^{i(\lambda a)p}\tilde g(p)$.

4. For $0<\operatorname{Im}z<1$, $e^{2\pi z}$ is not a positive real number, so the denominator does not vanish. As $\operatorname{Im}z\to0^+$, $u-e^{2\pi z}v\to u-\lambda v-i0$, the ordering $j(u)\,j(\lambda v)$; as $\operatorname{Im}z\to1^-$, it tends to $u-\lambda v+i0$, the opposite ordering.

5. $\frac{d}{ds}\lambda\tilde g(\lambda p)|_{s=0}=2\pi(\tilde g+p\tilde g')=iK\tilde g$. Symmetry: $\int p\,\bar f(1+p\partial_p)g\,dp+\int p\,\overline{(1+p\partial_p)f}\,g\,dp=\int\partial_p(p^2\bar fg)\,dp=0$, so $K=-2\pi i(1+p\partial_p)$ is symmetric. $[1+p\partial_p,p]=p$ gives $i[K,P]=2\pi P$; conjugation by $e^{ipb}$ adds $p\,\partial_p(e^{-ipb})e^{ipb}=-ibp$ inside, giving $K-2\pi bP$.

6. The trace argument as in §5. With the group law, $\|P\|=\|e^{isK}Pe^{-isK}\|=e^{2\pi s}\|P\|$ for all $s$. The trace argument needs $P\geq0$ because $\operatorname{Tr}P=0$ alone allows indefinite $P$. The relation itself has no nonzero solution even without positivity: in an eigenbasis of $K$, $(k_m-k_n)P_{mn}=-2\pi iP_{mn}$ with $k_m-k_n$ real.

7. $D(s)U(1)D(s)^\dagger=U(e^{2\pi s})$, so the product is $U(e^{2\pi s})U(-1)=U(e^{2\pi s}-1)$. The group property is $U(x)U(y)=U(x+y)$ with $x=e^{2\pi s}-1$ and $y=e^{2\pi t}-1$.

8. With $z=s+i\theta$, $e^{2\pi z}=e^{2\pi s}e^{2\pi i\theta}$ has argument in $(0,\pi)$ for $0<\theta<\frac12$, and every point of the upper half-plane arises once. For $\operatorname{Im}a\geq0$, $|e^{iap}|=e^{-p\operatorname{Im}a}\leq1$ on the spectrum of $P$.

9. Applying the inclusion at $-s$ and conjugating by $\Delta_{\mathcal M}^{-is}$ gives the reverse inclusion, so $\Delta_{\mathcal M}^{-is}\mathcal N\Delta_{\mathcal M}^{is}=\mathcal N$ for all $s$. The subalgebra is invariant under the modular group and $\Omega$ is cyclic for it, so Takesaki's theorem gives $\mathcal N=\mathcal M$.

10. $\hat K_a-\hat K_b=(\hat K_0-2\pi aP)-(\hat K_0-2\pi bP)=2\pi(b-a)P$, and $\langle g,(\hat K_a-\hat K_b)g\rangle=2\pi(b-a)\int_0^\infty\frac{p\,dp}{2\pi}\,p\,|\tilde g(p)|^2\geq0$.

11. $\int|e^x\tilde g(e^x)|^2dx=\int p\,|\tilde g(p)|^2dp$ with $p=e^x$, and $e^x(1+\partial_x)\bigl(e^{-x}\phi\bigr)=\partial_x\phi$, so $K\mapsto-2\pi i\partial_x$. For a smooth packet far from the edges the central difference reproduces $\partial_x(e^x\phi)-e^x\partial_x\phi=e^x\phi$ up to terms of second order in the spacing, and near the edges the truncated difference operator loses neighbors. The traces of the two sides disagree on every grid, and the deficit sits in the vectors that vary on the scale of the spacing.

12. Taking commutants of $U(a)\mathcal MU(a)^\dagger\subset\mathcal M$ gives $\mathcal M'\subset U(a)\mathcal M'U(a)^\dagger$, that is $U(-a)\mathcal M'U(-a)^\dagger\subset\mathcal M'$. Geometrically, translating $(0,\infty)$ forward keeps it inside itself, and translating its complement $(-\infty,0)$ backward keeps that inside itself.

**Wiki connections.** [[tomita-takesaki-modular-theory|Tomita–Takesaki modular theory]] · [[type-iii-von-neumann-algebras|type III₁ von Neumann algebras]] · [[traversable-wormholes|traversable wormholes]]
