---
title: "Sem II Week 1 — Symmetries Are Topological Operators"
type: lecture-notes
course: syllabus
semester: 2
week: 1
block: 1
duration: 4 hours (3 hr lectures + 1 hr seminar, presented by the instructor as the model for the block)
prerequisites: Semester I, in particular Weeks 2, 4, 5, 7–11 and 15
modified: 2026-10-02
---

# Sem II Week 1 — Symmetries Are Topological Operators

> *Semester I manipulated symmetry operators long before it named them: the seam of Kramers and Wannier, Wegner's flipped sheet, the twisted sheet of compact QED, the electric-flux operators of Kogut and Susskind. [[week-15-semester-i-consolidation|Week 15]] stated the definitions of Gaiotto, Kapustin, Seiberg and Willett and translated Wegner's theory into them. This week derives what Week 15 stated. We obtain the topological operator of a 0-form symmetry from its Noether current with every contact term accounted for, derive Maxwell's two currents and their Ward identities with the factor of $i$ that Euclidean signature puts into one of them, compute the action of the electric symmetry on Wilson loops twice, on the lattice through the intersection pairing and in the continuum through the canonical commutator, and show why higher-form symmetry groups are abelian. Week 2 applies the same machinery to $\mathbb{Z}_N$ gauge theory, where the operators wrapping the cycles of a torus generate its ground states.*

### How to use this chapter

- **In class:** derive §2 at the board in its three steps: the Ward identity (2.3) with its contact term, the twist (2.5)–(2.6), and the counterterm of the compact scalar, (2.8)–(2.9). Then §3, the two currents, with the Euclidean Gauss law (3.1) and the slice relation (3.2)–(3.3). Then the linking action twice, on the lattice (§§5.1–5.2 with the worked example of Figure 3) and in the continuum (§§6.2–6.3, the commutator and the slab). §4 closes the lecture if time remains. Problems 1–3 are the classroom core. The seminar hour (§8) is presented by the instructor.
- **For self-study:** §5.3 (the Hamiltonian lattice and the transfer-matrix bridge), §4 in full, §7, §§9–10, and Problems 4⋆–6⋆. The one calculation to do alone is Problem 2, the four dual loops of a plaquette, with every sign taken from the Hodge map.
- **Instructor checkpoint:** two errors recur. The first is to insert $\exp(i\alpha\oint\star F/e^2)$ into a Euclidean path integral and expect a phase: by (3.1) the Euclidean flux is imaginary inside correlators, so that operator gives a real factor $e^{-\alpha q}$; the Euclidean operator is $\exp(\alpha\oint\star F/e^2)$ times a counterterm, and its restriction to a time slice is the real-time $\exp(i\alpha\Phi_E)$ (F1). The second is to treat the minus sign of the equal-time relation (6.3) as an error, since the spacetime relation (5.6) has a plus: the two signs are related by the orientation of the slab of §6.3.

## 0. Reading

**Primary:** Gaiotto, Kapustin, Seiberg, Willett (GKSW), "Generalized global symmetries", *JHEP* 02 (2015) 172 [arXiv:1412.5148]: §2 (pp. 5–9; through eq. (2.4) for the lecture, the rest for the seminar), §3 (pp. 9–12) and §4.1 (pp. 12–14). Appendix F (pp. 56–57) is read for F7.

**Secondary:** [[week-15-semester-i-consolidation|Week 15]] §2, which states the definitions derived here; [[week-11-monopole-condensation-4d|Week 11]] §5, the twisted sheet and the equal-time algebra in $d=4$; [[week-07-kogut-susskind-hamiltonian|Week 7]] §§3–4 with Kogut, *Rev. Mod. Phys.* 51 (1979) 659, §VI.C, for the Hamiltonian lattice; McGreevy, arXiv:2204.03045, the companion of Semester II, for higher-form symmetries in lattice language.

**Optional research reading:** Sulejmanpasic & Gattringer, arXiv:1901.02637, and Gorantla, Lam, Seiberg, Shao, arXiv:2103.01257 (Villain sections), on lattice theories in which both symmetries of Maxwell theory are exact (Semester II Week 12; Problem 7⋆⋆); Kapustin & Seiberg, arXiv:1401.0740, §§1–3, on backgrounds (Semester II Week 4).

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]]. Every sign and normalization is from [[courses/generalized-symmetries-course/conventions|conventions]], every degree from its §6, and the lattice linking number is the one [[courses/generalized-symmetries-course/conventions|conventions]] §6 defines. Three signs that [[courses/generalized-symmetries-course/conventions|conventions]] §§4 and 6 now record are derived here: the Euclidean form of the electric operator (F1), the orientations that make a continuum linking number $+1$ (§6.1), and the dictionary between the Kogut–Susskind operators and the continuum fields (F3).

## 1. Motivation and setting

Noether's theorem starts from a continuous symmetry and ends with a conserved current and a charge, the integral of the current over space. The charge commutes with the Hamiltonian, and its exponential $e^{i\alpha Q}$ implements the symmetry on states. Gaiotto, Kapustin, Seiberg and Willett turned the logic around. Conservation lets the charge be integrated over any closed codimension-1 surface $M$ of Euclidean spacetime, and the resulting operator $U_\alpha(M)$ depends on $M$ only through the insertions it surrounds. GKSW keep this topological dependence, together with the group law of fusion, as the definition of a symmetry; the current becomes one way of building $U$, available for continuous groups. The definition extends at once to operators on closed submanifolds of higher codimension, and these are the $p$-form symmetries whose charged objects are $p$-dimensional ([[higher-form-symmetries]]).

Semester I contains the operators but not the derivation that connects them to currents, with the normalizations and signs that make the linking statement exact. The question of the week is therefore concrete: in what sense are Wegner's flipped sheet, the twisted sheet of compact QED, the Kogut–Susskind flux operator and the magnetic flux through a closed surface the same kind of object as $e^{i\alpha Q}$, and what exact phase do they produce on a Wilson loop? The answer is
$$
\langle U_\alpha(\Sigma)\,W_q(C)\cdots\rangle=e^{iq\alpha\,{\rm Link}(C,\Sigma)}\,\langle W_q(C)\cdots\rangle ,\tag{1.1}
$$
where Σ bounds a region that contains no other insertion, together with its equal-time form (6.3). The rest of the note derives both.

## 2. From a Noether current to a topological operator [Proved.; the model computation Computed.]

### 2.1 The Ward identity and its contact term

Consider a Euclidean theory of fields φ with action $S[\varphi]$ and measure $D\varphi$, invariant under a continuous symmetry $\varphi\to\varphi+\epsilon\,\delta\varphi$, and assume that the measure is invariant (no anomaly). Promote ε to a function $\epsilon(x)$ of compact support. The action is invariant for constant ε, so its variation can involve only derivatives of ε, and to first order
$$
S[\varphi+\epsilon\,\delta\varphi]=S[\varphi]+\int d^dx\;\partial_\mu\epsilon(x)\,K^\mu(x)+O(\epsilon^2),\tag{2.1}
$$
which defines the Noether current $K^\mu$ up to an improvement $K^\mu\to K^\mu+\partial_\nu B^{\mu\nu}$ with $B$ antisymmetric. Insert operators $\mathcal O_k(x_k)$ with variations $\delta\mathcal O_k$, write $X=\prod_k\mathcal O_k(x_k)$, and change variables $\varphi\to\varphi+\epsilon\,\delta\varphi$ in $\int D\varphi\,e^{-S}X$. The integral does not change, so its first-order variation vanishes,
$$
0=-\int d^dx\,\partial_\mu\epsilon\,\langle K^\mu(x)X\rangle+\sum_k\epsilon(x_k)\,\big\langle\delta\mathcal O_k\textstyle\prod_{j\ne k}\mathcal O_j\big\rangle .
$$
Integrating the first term by parts and using that ε is arbitrary, we obtain the Ward identity
$$
\partial_\mu\langle K^\mu(x)\,X\rangle=-\sum_k\delta^d(x-x_k)\,\big\langle\delta\mathcal O_k\textstyle\prod_{j\ne k}\mathcal O_j\big\rangle .\tag{2.2}
$$
For operators of definite charge, $\delta\mathcal O_k=iq_k\mathcal O_k$, and in terms of the **Euclidean current** $j_E^\mu\equiv iK^\mu$ it reads
$$
\partial_\mu\langle j_E^\mu(x)\,X\rangle=\sum_kq_k\,\delta^d(x-x_k)\,\langle X\rangle .\tag{2.3}
$$
The factor of $i$ is the Wick rotation of a Hermitian charge density, as §2.3 shows: $K^\mu$ is real on Euclidean configurations, and the operator that measures charge through a phase is built from $iK^\mu$.

Equation (2.3) is an identity between distributions, and its right side is a sum of contact terms whose coefficients the symmetry fixes: they are the charges. Other contact terms in $\langle j_E^\mu(x)\mathcal O(y)\rangle$ depend on how the product is defined at coincident points. A term $c\,\partial^\mu\delta^d(x-y)\,\mathcal O'(y)$, for instance, changes the divergence by $c\,\partial^2\delta^d(x-y)\,\mathcal O'(y)$, whose integral over any region with $y$ off its boundary vanishes; an improvement changes $\star j_E$ by an exact form, whose integral over a closed surface vanishes. Thus the integrated identity is universal. For a region $V$ whose boundary avoids the insertions,
$$
\oint_{\partial V}\langle\star j_E\,X\rangle=\Big(\sum_{x_k\in V}q_k\Big)\langle X\rangle ,\tag{2.4}
$$
where $\oint_{\partial V}\star j_E=\oint_{\partial V}j_E\cdot n\,dS$ with $n$ the outward normal. Deforming $\partial V$ changes the left side only when the boundary crosses an insertion, and the change is the charge of that insertion. This is the infinitesimal content of a topological operator.

### 2.2 The finite operator is a twist, and it carries a counterterm

To exponentiate we use the finite transformation with a step-function parameter, which is GKSW's description of $U_g(M)$ as a discontinuity of the fields across $M$ by the symmetry transformation (GKSW §2). Let $g_\theta\varphi$ be the field transformed by the angle θ, and $g_{\alpha1_V}\varphi$ the field transformed by α inside $V$ and left alone outside. Define
$$
U_\alpha(\partial V)\equiv\exp\Big\{S[\varphi]-S\big[g_{-\alpha1_V}\varphi\big]\Big\}.\tag{2.5}
$$
In $\int D\varphi\,e^{-S}X$ substitute $\varphi=g_{\alpha1_V}\varphi'$. The measure is invariant, the action becomes $S[\varphi']+\{S[g_{\alpha1_V}\varphi']-S[\varphi']\}$, and each insertion inside $V$ acquires $e^{i\alpha q_k}$. Renaming $\alpha\to-\alpha$ we obtain, exactly and for every α,
$$
\big\langle U_\alpha(\partial V)\,X\big\rangle=e^{\,i\alpha\sum_{x_k\in V}q_k}\,\langle X\rangle .\tag{2.6}
$$
Note that the exponent of (2.5) depends on φ only near $\partial V$: the integrand of $S[g_{-\alpha1_V}\varphi]-S[\varphi]$ vanishes wherever $1_V$ is locally constant, because the action is invariant under constant transformations. Expanding with (2.1) at $\epsilon=-\alpha1_V$ and using $\partial_\mu1_V=-n_\mu\,\delta_{\partial V}$,
$$
U_\alpha(\partial V)=\exp\Big\{-\alpha\oint_{\partial V}K\cdot n\,dS+O(\alpha^2)\Big\}=\exp\Big\{i\alpha\oint_{\partial V}\star j_E+O(\alpha^2)\Big\},\tag{2.7}
$$
where the $O(\alpha^2)$ terms are local functionals on $\partial V$, built from products such as $(\partial1_V)^2$ that are singular on the surface. They are the contact terms of finite α. The exponentiated charge alone is therefore not yet the symmetry operator, and the twist (2.5) supplies the counterterms that make it one.

**Model computation: the compact scalar** [Computed.]. Take the Villain XY model of [[week-03-villain-form-xy-duality|Week 3]], $S=\frac\beta2\|d\theta-2\pi n\|^2$, with the shift symmetry $\delta\theta=1$ and charged operators $e^{iq\theta_x}$. The rotation by $-\alpha$ inside $V$ is $\theta\to\theta-\alpha1_V$, with $1_V\in C^0(\Lambda)$ the indicator of the sites of $V$, and (2.5) gives
$$
U_\alpha(\partial V)=\exp\Big\{\alpha\beta\,\langle d\theta-2\pi n,\,d1_V\rangle-\frac{\alpha^2\beta}{2}\,\|d1_V\|^2\Big\},\tag{2.8}
$$
where $(d1_V)_\ell=-1$ on links leaving $V$, $+1$ on links entering it, and $\|d1_V\|^2=|\partial V|$ counts the links that cross the boundary. The linear term is $-\alpha$ times the net outward flux of the lattice Noether current $K=\beta(d\theta-2\pi n)$, which is (2.7); the quadratic term is the counterterm. In the spin-wave theory on a torus, with $\langle\theta\theta^T\rangle=G'/\beta$ ([[courses/generalized-symmetries-course/conventions|conventions]] §2), the linear term $X\equiv\alpha\beta\langle d\theta,d1_V\rangle$ and a charged pair $Y\equiv q(\theta_x-\theta_y)$ satisfy
$$
\langle X^2\rangle=\alpha^2\beta\,\|d1_V\|^2,\qquad \langle XY\rangle=q\alpha\,\langle 1_V,\Delta G'(\delta_x-\delta_y)\rangle=q\alpha\big[1_V(x)-1_V(y)\big],\tag{2.9}
$$
because the covariance of $d\theta$ is $dG'\delta/\beta$, the projector onto exact 1-cochains divided by β, and $d1_V$ is exact. Gaussian integration then gives $\langle e^{X}\rangle=e^{\alpha^2\beta|\partial V|/2}$, which the counterterm cancels exactly, so $\langle U_\alpha\rangle=1$; and $\langle U_\alpha\,e^{iq(\theta_x-\theta_y)}\rangle=e^{iq\alpha[1_V(x)-1_V(y)]}\langle e^{iq(\theta_x-\theta_y)}\rangle$, which is (2.6). Without the counterterm the bare exponentiated charge has expectation $e^{\alpha^2\beta|\partial V|/2}$, a perimeter law that depends on the shape of $\partial V$. We checked (2.9) numerically on a $6\times6$ torus with a $3\times3$ block ($|\partial V|=12$), to machine precision. In the Villain model with vortices (2.6) still holds exactly, since the substitution leaves the integers $n$ alone: the shift symmetry of the XY model is exact, and it is the winding symmetry that the vortices break ([[courses/generalized-symmetries-course/conventions|conventions]] §6).

### 2.3 Topological invariance and the Hamiltonian reading

By (2.6), two regions $V$ and $V'$ that differ by a region without insertions give the same correlators, and moving the surface across an insertion of charge $q$ multiplies the correlator by $e^{i\alpha q}$, as Figure 1 shows. That is the contact term of (2.3), integrated.

![[gs-s2w01-support-deformation.svg|Two nested closed surfaces, the inner one enclosing the insertion x1 and the outer one enclosing x1 and x2, with arrows deforming the inner surface across x2]]

**Figure 1. Deforming the support of a 0-form symmetry operator changes a correlator only when the support crosses a charged insertion; crossing $x_2$ multiplies it by $e^{i\alpha q_2}$.**

To read (2.5) in a Hamiltonian, take $V$ to be the slab $\tau_1<\tau<\tau_2$, whose boundary is the slice $\tau_2$ with outward normal $+\hat\tau$ and the slice $\tau_1$ with outward normal $-\hat\tau$. In the continuum spin-wave theory the linear term of (2.8) on the upper slice is $-\alpha\beta\int d^{d-1}x\,\partial_\tau\theta$. With $\tau=it$, so that $\partial_\tau=-i\partial_t$, and the canonical momentum $\Pi_\theta=\beta\partial_t\theta$, this is
$$
-\alpha\beta\int d^{d-1}x\,\partial_\tau\theta=i\alpha\int d^{d-1}x\,\Pi_\theta=i\alpha Q ,
$$
so the upper slice carries $e^{i\alpha Q}$ and the lower one $e^{-i\alpha Q}$, and the slab conjugates every operator between them, $e^{i\alpha Q}\mathcal O\,e^{-i\alpha Q}=e^{iq\alpha}\mathcal O$. This is GKSW's equal-time relation (2.4), and it confirms that $j_E=iK$ is the Euclidean continuation of the Hermitian current. The counterterm has a Hamiltonian meaning as well [Heuristic.]: the equal-time operator $e^{i\alpha Q}$ needs no subtraction, while in the path integral the product of two $\partial_\tau\theta$ at coincident times contains the contact term by which a Euclidean correlator of velocities differs from the time-ordered product of momenta, and the counterterm removes it.

## 3. Maxwell's two currents [Proved.]

### 3.1 The electric current and the Euclidean Gauss law

The Euclidean action is $S=\frac1{2e^2}\int F\wedge\star F=\frac1{4e^2}\int F_{\mu\nu}F_{\mu\nu}$ ([[courses/generalized-symmetries-course/conventions|conventions]] §§4–5), whose variation is $\delta S/\delta a_\nu=-\frac1{e^2}\partial_\mu F_{\mu\nu}$. The Wilson loop is $W_q(C)=\exp(iq\oint_Ca)=\exp\big(iq\int a_\nu J^\nu_C\big)$, with $J_C^\nu(x)=\oint_Cdy^\nu\,\delta^d(x-y)$. The Schwinger–Dyson equation $\langle\frac{\delta S}{\delta a_\nu}W_q\cdots\rangle=\langle\frac{\delta W_q}{\delta a_\nu}\cdots\rangle$ gives, for further insertions away from $x$,
$$
\frac1{e^2}\,\partial_\mu\big\langle F_{\nu\mu}(x)\,W_q(C)\cdots\big\rangle=iq\,J^\nu_C(x)\,\big\langle W_q(C)\cdots\big\rangle .\tag{3.1}
$$
Away from the loop this is the equation of motion $d\star F=0$, which closes the $(d-2)$-form $\star F/e^2$, and the contact term on $C$ carries an $i$. To read it physically, take a static charge along $+\tau$ in $d=4$, $J^\tau_C=\delta^3(\vec x)$. With $a=-\varphi\,dt+A\cdot dx$ ([[courses/generalized-symmetries-course/conventions|conventions]] §10) and $\tau=it$ the Euclidean component is $a_\tau=i\varphi$, so $F_{\tau i}=-i\partial_tA_i-i\partial_i\varphi=iE_i$ with $E$ the real-time electric field, and (3.1) becomes $\nabla\cdot E/e^2=q\,\delta^3(\vec x)$. The forward Wilson line is a positive charge, as [[courses/generalized-symmetries-course/conventions|conventions]] §10 states.

The same relation fixes the Euclidean electric operator. With $\epsilon_{\tau123}=+1$ and a closed surface Σ in a time slice, oriented by its outward normal, $(\star F)_{jk}=\epsilon_{\tau ijk}F_{\tau i}$ and therefore
$$
\oint_\Sigma\star F=\oint_\Sigma F_{\tau i}\,dS_i=i\oint_\Sigma E\cdot dS .\tag{3.2}
$$
The real-time operator $U_\alpha(\Sigma)=\exp(i\alpha\Phi_E)$, $\Phi_E=\oint_\Sigma E\cdot dS/e^2$, which measures the enclosed charge, reads in the Euclidean path integral
$$
U_\alpha(\Sigma)=\exp\Big(\frac{\alpha}{e^2}\oint_\Sigma\star F\Big)\times(\text{counterterm})=\exp\Big(i\alpha\oint_\Sigma\omega_E\Big)\times(\text{counterterm}),\qquad \omega_E=-\frac{i}{e^2}\star F .\tag{3.3}
$$
By (3.1) and Stokes' theorem, $\frac1{e^2}\oint_\Sigma\star F=iq\,{\rm Link}(C,\Sigma)$ inside correlators (§§5.2 and 6.1 prove it with the signs), so (3.3) produces the phase of (1.1). The form $\exp(i\alpha\oint\star F/e^2)$ written in [[courses/generalized-symmetries-course/conventions|conventions]] §6 is the real-time expression, in which $\star F$ restricted to a slice is the real flux density (F1).

The support of $U_\alpha$ is a closed $(d-2)$-dimensional surface, so the symmetry is 1-form ($d-q-1=d-2$ gives $q=1$) and its charged objects are lines, in agreement with the master table of [[courses/generalized-symmetries-course/conventions|conventions]] §6. The group is $U(1)$, with $\alpha\sim\alpha+2\pi$, because the charges of a compact gauge field are integers. Dynamical matter of charge $n$ adds its current to the right side of (3.1), and only the operators with $e^{in\alpha}=1$ stay topological: the electric symmetry is broken explicitly to $\mathbb{Z}_n^{(1)}$ (GKSW §4.1; the $\gcd$ rule of [[courses/generalized-symmetries-course/conventions|conventions]] §6).

### 3.2 The magnetic current

The 2-form $F/2\pi$ is closed by the Bianchi identity $dF=0$, which holds identically when $F=da$ locally, and Dirac quantization gives $\oint_{\Sigma_2}F\in2\pi\mathbb{Z}$ on every closed surface ([[week-08-dual-variables-abelian-gauge|Week 8]] §2.2). The operators
$$
U^{m}_\eta(M_2)=\exp\Big(i\eta\oint_{M_2}\frac{F}{2\pi}\Big),\qquad \eta\in\mathbb{R}/2\pi\mathbb{Z},\tag{3.4}
$$
live on closed 2-surfaces, so the magnetic symmetry has degree $d-3$: a 0-form symmetry with local monopole operators in $d=3$, a 1-form symmetry with 't Hooft lines in $d=4$. No factor of $i$ appears, since $F/2\pi$ is real on Euclidean configurations and its flux is an integer. The three-dimensional case was computed in [[week-09-compact-qed3-monopole-plasma|Week 9]] §5.1, where the Noether current of the dual photon, $\frac{e^2}{4\pi^2}\partial\sigma$, equals $-i\,j_{\rm mag}$, the factor of §2.1 on the dual side. On the Villain lattice the field strength $F=da-2\pi n$ obeys $dF=-2\pi\,dn=-2\pi m$, the flux out of a cube being $-2\pi m_c$ ([[courses/generalized-symmetries-course/conventions|conventions]] §4). The Bianchi identity, and with it the topological invariance of (3.4), holds exactly when there are no monopoles. Dynamical monopoles break the magnetic symmetry explicitly (Weeks 9–11), and the monopole-free theory with $dn=0$ imposed restores it (Semester II Week 12).

Table 1 collects the four presentations of the electric operator that the rest of the note derives and relates; F1 and F3 refer to it.

| presentation | operator on a closed, bounding Σ | action on $W_q$ | where |
|---|---|---|---|
| Euclidean continuum | $\exp\big(\frac{\alpha}{e^2}\oint_\Sigma\star F\big)\times$ counterterm | $e^{iq\alpha\,{\rm Link}(C,\Sigma)}$ | (3.3), §6.1 |
| Euclidean lattice | twisted sheet $T_\alpha(\tilde\Sigma)$: $F\to F-\alpha\,d\lambda_{\tilde V}$ | $e^{iq\alpha\,{\rm Link}(C,\tilde\Sigma)}$ | (5.6)–(5.7) |
| Kogut–Susskind slice | $e^{-i\alpha\Phi(\tilde\Sigma)}$, $\Phi=\sum_\ell\varepsilon_\ell E_\ell$ | $e^{-iq\alpha\,I_s(\Gamma,\tilde\Sigma)}$ | (5.8)–(5.9) |
| continuum slice | $e^{i\alpha\Phi_E(\Sigma)}$, $\Phi_E=\oint E\cdot dS/e^2$ | $e^{-iq\alpha\,I_s(\Gamma,\Sigma)}$ | (6.3) |

**Table 1. The electric symmetry operator of Maxwell theory in four presentations, with the signs fixed in this note.** The slice rows act by conjugation on spatial Wilson lines Γ; their minus sign is the slab orientation of §6.3.

## 4. Why higher-form symmetry groups are abelian [Model proof.]

GKSW (§3) read the fusion $U_g(M)U_h(M)=U_{gh}(M)$ as the product of two operators inserted at nearby times $t+\epsilon$ and $t$, ordered by time, and observe that for $q>0$ the support at $t+\epsilon$ can be deformed to $t-\epsilon$. We make the deformation explicit. Let $p\ge1$, let $M$ be a closed $(d-p-1)$-dimensional submanifold of the time slice, and let $M_s$ denote $M$ displaced to time $s$. At each point of $M$ the normal space in spacetime is $\mathbb{R}^{p+1}=\mathbb{R}\hat\tau\oplus N$, where $N$, of dimension $p\ge1$, is the normal space of $M$ inside the slice. Suppose that $M$ has a nowhere-vanishing unit normal vector field $v$ inside the slice and that no other insertion lies within a distance ε of $M$. The family
$$
M(s)=M_t+\epsilon\,\big(\cos\pi s\;\hat\tau+\sin\pi s\;v\big),\qquad 0\le s\le1,\tag{4.1}
$$
carries the copy with $g$ from $M_{t+\epsilon}$ to $M_{t-\epsilon}$. For every $s$ the displacement has length ε and is normal to $M$, so $M(s)$ never meets $M_t$ once ε is smaller than the radius of a tubular neighbourhood of $M$. By topological invariance
$$
U_g(M_{t+\epsilon})\,U_h(M_t)=U_h(M_t)\,U_g(M_{t-\epsilon}),
$$
and as $\epsilon\to0$ this is $U_gU_h=U_hU_g$ on $M$. With the fusion rule, $U_{gh}(M)=U_{hg}(M)$, and since distinct group elements give distinct operators, $gh=hg$.

The move (4.1) turns the displacement in the plane spanned by $\hat\tau$ and $v$, which exists because the codimension of $M$ in spacetime is at least two. For $p=0$ the support fills the slice, $N=0$, and the only normal directions are $\pm\hat\tau$; any path from $+\hat\tau$ to $-\hat\tau$ in the normal line passes through zero, that is, through $M_t$. In other words, the unit normal sphere of $M$ is $S^p$, which is connected exactly when $p\ge1$, as Figure 2 draws. The ordering of codimension-1 operators is therefore meaningful, and 0-form groups such as $SU(2)$ spin rotations can be nonabelian.

![[gs-s2w01-codimension-two-move.svg|The normal plane of M, where the copy carrying g turns on a half circle from time t plus epsilon to t minus epsilon without meeting M at time t, beside the normal line for p equal to zero, where the only path passes through it]]

**Figure 2. The codimension-2 move. For $p\ge1$ the copy carrying $g$ turns from $t+\epsilon$ to $t-\epsilon$ through a spatial normal direction and never meets $M_t$; for $p=0$ the normal space is the τ line and the copy must pass through $M_t$.**

Three remarks bound the statement. (i) The hypothesis on $v$ holds for every orientable $M$ when $p=1$, since an orientable codimension-1 submanifold of an orientable slice has a trivial normal line bundle, and for the spheres and flat subtori used in the course; for $p\ge2$ the normal bundle of $M$ in the slice has rank $p$ over a manifold of dimension $d-p-1$, its Euler class is the primary obstruction, complete when $d-p-1=p$, and there is no obstruction when $d-p-1<p$, so in $d\le4$ the hypothesis never fails. (ii) GKSW Appendix F shows that on a spatial manifold with torsion the electric and magnetic operators of Maxwell theory, built as networks of surfaces with junctions on torsion classes, need not commute (F7); a network with junctions admits no normal field of the kind (4.1) uses. (iii) Abelianness concerns parallel copies of one support. Operators whose supports cross inside the slice cannot be separated by (4.1), since their spatial intersection is a linking in spacetime, and a phase between them means that the operators are themselves charged: an 't Hooft anomaly for one symmetry (GKSW §3 and §4.4), a mixed one for two, as in the clock–shift algebra of $\mathbb{Z}_N$ gauge theory (Problem 6⋆; Semester II Week 2). On the Kogut–Susskind lattice the electric operators commute trivially, as functions of the commuting $E_\ell$; the argument shows that this is forced in every theory.

## 5. The linking action on the lattice

### 5.1 The intersection pairing and the linking number, with signs [Proved.]

For a $p$-chain $c$ on Λ and a $(d-p)$-chain $\tilde c$ on $\Lambda^*$, the intersection pairing of [[week-02-lattice-cell-complex-cochains|Week 2]] §8 is
$$
I(c,\tilde c)=\sum_{\sigma}\epsilon(S_\sigma,S^c_\sigma)\,c(\sigma)\,\tilde c(\sigma^*)=\big\langle J_c,\star^{-1}J_{\tilde c}\big\rangle ,\tag{5.1}
$$
where the sum runs over the $p$-cells $\sigma=(x;S_\sigma)$, $\sigma^*$ is the dual cell, $J_c$ is the cochain whose values are the coefficients of $c$, and $\star$ is the Hodge map of [[courses/generalized-symmetries-course/conventions|conventions]] §2. The sign is $+1$ when the orientation of σ followed by that of $\sigma^*$ is the orientation of Λ, the convention of the continuum. Two facts make the pairing a tool. First, the boundary of chains is the codifferential of their coefficients, $J_{\partial X}=\delta J_X$, since $\langle J_{\partial X},f\rangle=f(\partial X)=(df)(X)=\langle J_X,df\rangle$ for every cochain $f$. Second, the Hodge map intertwines the dual codifferential with the coboundary. From $\tilde\delta=(-1)^{d(q+1)+1}\star d\star$ on $C^q(\Lambda^*)$ ([[courses/generalized-symmetries-course/conventions|conventions]] §2) and $\star=(-1)^{q(d-q)}\star^{-1}$ there, and since $d(q+1)+1+q(d-q)\equiv d+q+1$ mod 2,
$$
\star^{-1}\tilde\delta=(-1)^{d+q+1}\,d\,\star^{-1}\qquad\text{on }C^q(\Lambda^*).\tag{5.2}
$$
For a $(p+1)$-chain $X$ on Λ and a $(d-p)$-chain $\tilde Y$ on $\Lambda^*$ these give $I(\partial X,\tilde Y)=\langle J_X,d\star^{-1}J_{\tilde Y}\rangle$ and $I(X,\partial\tilde Y)=\langle J_X,\star^{-1}\tilde\delta J_{\tilde Y}\rangle=(-1)^{p+1}\langle J_X,d\star^{-1}J_{\tilde Y}\rangle$, which is the lattice Stokes theorem for intersections,
$$
I(\partial X,\tilde Y)=(-1)^{p+1}\,I(X,\partial\tilde Y).\tag{5.3}
$$
We checked (5.2) and (5.3) on random integer chains for every $p$ in $d=2,3,4$, with the cell conventions of [[courses/generalized-symmetries-course/conventions|conventions]] §1.

Now let $C$ be a closed $p$-chain and $\tilde\Sigma=\partial\tilde V$ a closed dual $(d-p-1)$-chain that bounds. Following [[courses/generalized-symmetries-course/conventions|conventions]] §6,
$$
{\rm Link}(C,\partial\tilde V)\equiv\langle J_C,\lambda_{\tilde V}\rangle=I(C,\tilde V),\qquad \lambda_{\tilde V}\equiv\star^{-1}J_{\tilde V},\tag{5.4}
$$
the signed number of cells of $C$ dual to cells of $\tilde V$, with the sign of (5.1). It depends only on $\tilde\Sigma$: if $\tilde V'$ has the same boundary and $\tilde V'-\tilde V=\partial\tilde W$, then (5.3) gives $I(C,\partial\tilde W)=(-1)^pI(\partial C,\tilde W)=0$. If $C=\partial X$ bounds as well, (5.3) gives a second expression,
$$
{\rm Link}(C,\tilde\Sigma)=(-1)^{p+1}\,I(X,\tilde\Sigma),\tag{5.5}
$$
which agrees with (5.4) for $p=1$ and differs by a sign for $p=0$ (F5). On a torus a cycle need not bound, the linking number is not defined, and the homology pairing of §5.3 takes its place.

**Worked example in $d=3$** [Computed.]. Take $C=\partial P_{12}(0)=\ell_1(0)+\ell_2(\hat1)-\ell_1(\hat2)-\ell_2(0)$ and $\tilde V=\ell_1(0)^*$, the dual plaquette in the plane $x_1=\frac12$ spanned by the directions $(2,3)$ and centred on the midpoint of $\ell_1(0)$. Its boundary $\tilde\Sigma$, from the boundary formula of [[courses/generalized-symmetries-course/conventions|conventions]] §1 applied on $\Lambda^*$, is the dual loop $(\frac12,-\frac12,-\frac12)\to(\frac12,\frac12,-\frac12)\to(\frac12,\frac12,\frac12)\to(\frac12,-\frac12,\frac12)$, counter-clockwise in the $(x_2,x_3)$ plane, as Figure 3 shows. Only the link $\ell_1(0)$ of $C$ is dual to a cell of $\tilde V$, with coefficient $+1$ and $\epsilon(\{1\},\{2,3\})=+1$, so ${\rm Link}(C,\tilde\Sigma)=+1$. By (5.5) the same number is $I(P_{12}(0),\tilde\Sigma)$: the only dual link of $\tilde\Sigma$ dual to the plaquette is $P_{12}(0)^*$, from $(\frac12,\frac12,-\frac12)$ to $(\frac12,\frac12,\frac12)$, which enters $\tilde\Sigma$ with coefficient $+1$, and $\epsilon(\{1,2\},\{3\})=+1$. Gauss's integral $\frac1{4\pi}\oint\oint\frac{(r_1-r_2)\cdot(dr_1\times dr_2)}{|r_1-r_2|^3}$ for the two polygons, evaluated numerically, gives $1.0000$: the Hodge signs of the lattice reproduce the right-hand rule.

![[gs-s2w01-dual-loop-linking.svg|The plane x1 equal to one half of the cubic lattice, with the counter-clockwise dual loop around the dual plaquette of the link l1(0), the loop C crossing it once toward the reader inside the dual loop and once away from the reader outside it]]

**Figure 3. The plane $x_1=\frac12$ of the $d=3$ lattice. The dual loop $\tilde\Sigma$ bounds the dual plaquette $\ell_1(0)^*$, which $C=\partial P_{12}(0)$ crosses once along its normal, so ${\rm Link}(C,\tilde\Sigma)=+1$; the return link $\ell_1(\hat2)$ crosses the plane outside $\tilde\Sigma$.**

### 5.2 The twisted sheet in $d$ dimensions [Proved.]

In the Villain theory $S=\frac\beta2\|da-2\pi n\|^2$, $\beta=1/(e^2a_{\rm lat}^{4-d})$, the twisted sheet $T_\alpha(\tilde\Sigma)$ on a closed dual $(d-2)$-chain $\tilde\Sigma=\partial\tilde V$ replaces $da-2\pi n$ by $da-2\pi n-\alpha\,d\lambda_{\tilde V}$ in the weight and divides by $Z$ ([[courses/generalized-symmetries-course/conventions|conventions]] §6; [[week-11-monopole-condensation-4d|Week 11]] §5.1). By (5.2) with $q=d-1$ the sign is $(-1)^{2d}=+1$, and
$$
d\lambda_{\tilde V}=d\star^{-1}J_{\tilde V}=\star^{-1}\tilde\delta J_{\tilde V}=\star^{-1}J_{\tilde\Sigma}\equiv\Xi ,
$$
so the twist sits exactly on the plaquettes dual to the cells of $\tilde\Sigma$, with the signs the Hodge map gives them. This is the precise content of "oriented so that $d\lambda_{\tilde V}=+1$ on the plaquettes dual to $\tilde c$" in [[courses/generalized-symmetries-course/conventions|conventions]] §6, and it fixes the shuffle sign that Week 11 §5.1 left open. The substitution $a=a'+\alpha\lambda_{\tilde V}$ preserves the measure over one period, because the Villain weight is $2\pi$-periodic in each $a_\ell$, and it removes the twist, while $W_q(C)=e^{iq\langle J_C,a\rangle}$ acquires $e^{iq\alpha\langle J_C,\lambda_{\tilde V}\rangle}$. Therefore, in every phase,
$$
\big\langle T_\alpha(\tilde\Sigma)\,W_q(C)\,X\big\rangle=e^{iq\alpha\,{\rm Link}(C,\tilde\Sigma)}\,\big\langle W_q(C)\,X\big\rangle,\qquad \langle T_\alpha(\tilde\Sigma)\rangle=1,\tag{5.6}
$$
for $X$ any product of further Wilson loops, each with its own phase, and of functions of $F$ on plaquettes away from $\tilde\Sigma$. In $d=3$ the sheet is a dual loop and (5.6) is the exact electric $U(1)^{(1)}$ of compact QED₃, unbroken at every coupling by the area law of [[week-10-polyakov-mass-gap-area-law|Week 10]]; in $d=4$ it is Week 11 §5.1; at $\alpha=\pi$ in the $\mathbb{Z}_2$ theory it is the flipped sheet of [[week-05-wegner-z2-gauge-theory|Week 5]] §8.1.

Expanding the twisted weight, $\frac\beta2\|F-\alpha\Xi\|^2=\frac\beta2\|F\|^2-\alpha\beta\langle F,\Xi\rangle+\frac{\alpha^2\beta}2\|\Xi\|^2$, and $\langle F,\Xi\rangle=\langle\star F,J_{\tilde\Sigma}\rangle\equiv\oint_{\tilde\Sigma}\star F$, because the Hodge map transports values with a sign whose square is one. Thus
$$
T_\alpha(\tilde\Sigma)=\exp\Big\{\alpha\beta\oint_{\tilde\Sigma}\star F-\frac{\alpha^2\beta}2\,|\tilde\Sigma|\Big\},\tag{5.7}
$$
with $|\tilde\Sigma|=\|J_{\tilde\Sigma}\|^2$ the number of cells of the sheet: the exponentiated electric flux with the real Euclidean coefficient of (3.3), times the counterterm. This is (2.8) one degree up. The Ward identity behind it is the lattice Schwinger–Dyson equation $\int Da\,\partial_{a_\ell}\big(e^{-S}W_q\big)=0$, that is $\beta\langle(\delta F)_\ell W_q\rangle=iqJ_C(\ell)\langle W_q\rangle$, the lattice form of (3.1). With it, $\beta\oint_{\tilde\Sigma}\star F=\beta\langle\delta F,\lambda_{\tilde V}\rangle=iq\,{\rm Link}(C,\tilde\Sigma)$ inside correlators, which is (5.6) to first order in α.

**The static charge in $d=4$** [Computed.]. Put Euclidean time on axis 1 ([[courses/generalized-symmetries-course/conventions|conventions]] §10) and let $C=\partial X$, with $X$ the $T\times R$ rectangle of plaquettes $P_{12}$; its boundary runs along $+\hat1$ at $x_2=0$ and along $-\hat1$ at $x_2=R$, as in Figure 4. For $0<\tau_0<T$ let $\tilde V$ be the dual 3-cell dual to the temporal link $\ell_1$ at $(\tau_0,0,0,0)$, the unit dual cube of space at time $\tau_0+\frac12$ around the spatial origin, and $\tilde\Sigma=\partial\tilde V$ its boundary, oriented outward (the face in direction $+\hat\mu$ enters $\partial$ with $+1$, [[courses/generalized-symmetries-course/conventions|conventions]] §1). Then ${\rm Link}(C,\tilde\Sigma)=\epsilon(\{1\},\{2,3,4\})=+1$ around the forward end, and $-1$ around the backward end. By (5.6) the sheet measures the charge $+q$ on the forward worldline, in agreement with §3.1.

### 5.3 The Hamiltonian lattice and the transfer-matrix bridge [Proved.]

On the spatial lattice of the Kogut–Susskind Hamiltonian, of dimension $D=d-1$, with $[E_\ell,U_{\ell'}]=\delta_{\ell\ell'}U_\ell$ and Gauss's law $\delta E=-q$ ([[courses/generalized-symmetries-course/conventions|conventions]] §4), let $\tilde\Sigma$ be a closed dual $(D-1)$-chain of space and define the flux $\Phi(\tilde\Sigma)=\sum_\ell\varepsilon_\ell E_\ell$, with $\varepsilon=\star_s^{-1}J_{\tilde\Sigma}$ given by the spatial Hodge map; this is the flux of Week 11 §5.3. Since $e^{i\alpha E}Ue^{-i\alpha E}=e^{i\alpha}U$ on each link, for any spatial path Γ
$$
e^{i\alpha\Phi(\tilde\Sigma)}\,W_q(\Gamma)\,e^{-i\alpha\Phi(\tilde\Sigma)}=e^{iq\alpha\,I_s(\Gamma,\tilde\Sigma)}\,W_q(\Gamma),\tag{5.8}
$$
where $I_s$ is the pairing (5.1) in $D$ dimensions. For $\tilde\Sigma=\partial\tilde R^*$, the boundary of the dual $D$-cells around a set $R$ of sites, (5.2) with $q=D$ gives $\varepsilon=-d1_R$, so that $\varepsilon_\ell=+1$ on links leaving $R$, and $\Phi(\partial\tilde R^*)=-\langle1_R,\delta E\rangle=\sum_{x\in R}q_x$. On physical states the operator is $e^{i\alpha Q_R}$; moving $\tilde\Sigma$ across a site $x$ multiplies it by $e^{\pm i\alpha q_x}$, the lattice contact term, and without charges it depends only on the homology class of $\tilde\Sigma$. On the spatial torus a noncontractible $\tilde\Sigma$ carries an integer flux, and (5.8) with a Wilson loop on the transverse cycle is GKSW's (3.4), the pairing of $H_1$ with $H_{D-1}$: Week 2 §8 in operator form.

The bridge to §5.2 is the transfer matrix of [[week-07-kogut-susskind-hamiltonian|Week 7]] §2. Place the sheet of §5.2 at time $\tau+\frac12$, with $\tilde V=\sum_{x\in R}\ell_1(x,\tau)^*$, so that $\lambda_{\tilde V}$ is the indicator of the temporal links at time τ above $R$ and $d\lambda_{\tilde V}$ lives on the temporal plaquettes, $(d\lambda_{\tilde V})(P_{1\mu}(x,\tau))=1_R(x)-1_R(x+\hat\mu)=\varepsilon_{\ell_\mu(x)}$, the spatial sign of the flux through $\partial\tilde R^*$ (checked numerically). The temporal plaquette angle $\theta_\ell(\tau+1)-\theta_\ell(\tau)$ becomes $\theta_\ell(\tau+1)-\theta_\ell(\tau)-\alpha\varepsilon_\ell$, the kernel $\langle\theta'|T_E|\theta\rangle$ becomes $\langle\theta'|T_E|\theta+\alpha\varepsilon\rangle$, and since $e^{-iaE}|\theta\rangle=|\theta+a\rangle$,
$$
T_\alpha(\tilde\Sigma\ \text{at}\ \tau+\tfrac12)=e^{-i\alpha\Phi(\partial\tilde R^*)}\quad\text{inserted between the slices }\tau\text{ and }\tau+1.\tag{5.9}
$$
Around the forward end of Figure 4, (5.6) gives $e^{iq\alpha}$ and (5.9) gives $e^{-i\alpha Q_R}$, so the forward line carries Kogut–Susskind charge $-q$. Week 7 §4.2 agrees: a Wilson line from $x$ to $y$ creates $q_x=+1$ at its start, and the spatial segment of $C$ at $\tau=0$ runs from $x_2=R$ to $x_2=0$, ending on the forward line. The Kogut–Susskind $E_\ell=-i\partial/\partial\theta_\ell$ is the momentum conjugate to $\theta_\ell=\int_\ell a$, which in the continuum conventions of [[courses/generalized-symmetries-course/conventions|conventions]] §10 is $\Pi=-E/e^2$ (§6.2). That is why $\Phi=-\Phi_E$ and why the Kogut–Susskind row of Table 1 carries $-\alpha$ (F3).

## 6. The linking action in the continuum

### 6.1 Euclidean: the integrated Ward identity [Proved.]

In the continuum ${\rm Link}(C,\Sigma)=I(C,V)$ for $\Sigma=\partial V$, where $I(C,V)$ counts the points of $C\cap V$ with the sign $+1$ when the tangent of $C$ followed by the orientation of $V$ is the orientation $d\tau\wedge dx^1\wedge\cdots$ of spacetime, and $\partial V$ is oriented outward normal first. These are the orientations of (5.4) and [[courses/generalized-symmetries-course/conventions|conventions]] §6, and they give ${\rm Link}=+1$ in two reference cases: in $d=4$, a worldline along $+\tau$ and a sphere at fixed τ around it, oriented outward; in $d=3$, two loops related by the right-hand rule, $C$ crossing a disk bounded by Σ along the normal that the circulation of Σ defines, as in Figure 3. Let $\lambda_V$ be the 1-form Poincaré dual to $V$, normalized by $\langle J_C,\lambda_V\rangle=I(C,V)$, so that $d\lambda_V$ is dual to Σ as in §5.2. Then (3.1) gives, inside correlators,
$$
\frac1{e^2}\oint_\Sigma\star F=\frac1{e^2}\langle F,d\lambda_V\rangle=\frac1{e^2}\langle\delta F,\lambda_V\rangle=iq\,\langle J_C,\lambda_V\rangle=iq\,{\rm Link}(C,\Sigma),\tag{6.1}
$$
which for the static charge is (3.2) with $\oint E\cdot dS=e^2q$. The finite operator is the twist $a\to a+\alpha\lambda_V$, with the result (5.7) in the limit $a_{\rm lat}\to0$, where the counterterm $\frac{\alpha^2}{2e^2}\int|d\lambda_V|^2$ diverges as the area of Σ times the coincident-point singularity of the surface.

### 6.2 The equal-time commutator with $\oint\star F$ [Proved.]

In real time $L=\frac1{2e^2}(E^2-B^2)$ with $E=-\partial_tA-\nabla\varphi$, so the momentum conjugate to $A_i$ is $\Pi_i=\partial L/\partial\dot A_i=-E_i/e^2$, and $[A_i(\vec x),\Pi_j(\vec y)]=i\delta_{ij}\delta^3(\vec x-\vec y)$ reads
$$
[A_i(\vec x),E_j(\vec y)]=-ie^2\,\delta_{ij}\,\delta^3(\vec x-\vec y).\tag{6.2}
$$
For a closed surface Σ in space let $U_\alpha(\Sigma)=e^{i\alpha\Phi_E(\Sigma)}$, $\Phi_E=\oint_\Sigma E\cdot dS/e^2$, the restriction of (3.3) to the slice. By (6.2), $[\Phi_E,A_i(\vec y)]=i\oint_\Sigma dS_i\,\delta^3(\vec x-\vec y)$ is a c-number, so $U_\alpha A_i(\vec y)U_\alpha^{-1}=A_i(\vec y)-\alpha(\delta_\Sigma)_i(\vec y)$ with $(\delta_\Sigma)_i(\vec y)=\oint_\Sigma dS_i\,\delta^3(\vec x-\vec y)$, and for any spatial curve Γ, with $W_q(\Gamma)=\exp(iq\int_\Gamma A\cdot dl)$,
$$
U_\alpha(\Sigma)\,W_q(\Gamma)\,U_\alpha(\Sigma)^{-1}=e^{-iq\alpha\,I_s(\Gamma,\Sigma)}\,W_q(\Gamma),\tag{6.3}
$$
where $I_s(\Gamma,\Sigma)=\int_\Gamma\delta_\Sigma\cdot dl$ counts the crossings of Γ through Σ, positive along the normal $dS$. Two readings check the sign. For an open Γ from $\vec y$ to $\vec z$ and Σ a small sphere around $\vec z$, Γ enters the sphere, $I_s=-1$, and (6.3) says that $W_q(\Gamma)$ raises the charge inside by $q$: the line creates $+q$ at its head, which is Gauss's law in operator form, $[\nabla\cdot E/e^2,W_q(\Gamma)]=q\,[\delta^3(\vec x-\vec z)-\delta^3(\vec x-\vec y)]\,W_q(\Gamma)$. And with $\Phi=-\Phi_E$, (5.8) is (6.3): the two slice rows of Table 1 coincide.

### 6.3 Equal time from linking: the slab [Proved.]

The commutator (6.3) and the linking (6.1) are one statement. Let Σ lie in the slice $t$ and let $\Gamma_t$ be the part of $C$ in that slice. The time-ordered correlator with the operator at $t+\epsilon$ is the operator product $U_\alpha W_q(\Gamma_t)$, and at $t-\epsilon$ it is $W_q(\Gamma_t)U_\alpha$, so their ratio is the jump of $e^{iq\alpha{\rm Link}}$. Give $I_\epsilon\times\Sigma$, with $I_\epsilon=[t-\epsilon,t+\epsilon]$, the product orientation $(\hat\tau,\Sigma)$; since Σ is closed, $\partial(I_\epsilon\times\Sigma)=\Sigma_{t+\epsilon}-\Sigma_{t-\epsilon}$. Then $V_{t+\epsilon}-V_{t-\epsilon}-I_\epsilon\times\Sigma$ is closed and has zero intersection with $C$, and at a crossing of $\Gamma_t$ with Σ, with tangent $u$ and Σ oriented by $(e_1,e_2)$, the frame $(u,\hat\tau,e_1,e_2)$ has the orientation opposite to $(\hat\tau,u,e_1,e_2)$. Therefore
$$
{\rm Link}(C,\Sigma_{t+\epsilon})-{\rm Link}(C,\Sigma_{t-\epsilon})=-\,I_s(\Gamma_t,\Sigma),\tag{6.4}
$$
and $U_\alpha W_q(\Gamma_t)=e^{-iq\alpha I_s(\Gamma_t,\Sigma)}W_q(\Gamma_t)U_\alpha$, which is (6.3). In Figure 4 the sphere around the forward end links $C$ for $0<t<T$ and not for $t<0$; the jump at $t=0$ is $+1=-I_s(\Gamma_0,\Sigma)$, because the segment at $\tau=0$ enters the sphere. On the lattice of §5.2 we computed the same numbers: ${\rm Link}=0,1,1,0$ for the sheet at $\tau+\frac12=-\frac12,\frac12,\frac32,\frac52$ with $T=R=2$, and $I_s(\Gamma_0,\partial\tilde R^*)=-1$. GKSW's (3.3), $U_gV=g(V)^{(C,M)}VU_g$, is (6.3) with $(C,M)=-I_s(C,M)$ in our orientations; GKSW do not fix orientations; [[courses/generalized-symmetries-course/conventions|conventions]] §6 records (6.3) with this sign.

![[gs-s2w01-wilson-loop-sphere.svg|Rectangular Wilson loop with time vertical, a sphere drawn as a ring around its forward line at time t, the same sphere swept below t equal to zero, and the bottom segment Gamma0 running toward the forward line]]

**Figure 4. The $T\times R$ Wilson loop with time vertical. The sphere Σ, drawn as a circle, surrounds the forward end and links $C$ for $0<t<T$; swept below $t=0$ it unlinks, and the jump is the crossing of Σ by the segment $\Gamma_0$, which enters it.**

### 6.4 The magnetic symmetry

The same computation with the roles of $E$ and $B$ exchanged gives the action of (3.4) on 't Hooft lines in $d=4$. The equal-time 't Hooft loop is the exponentiated electric flux through an open surface with a properly quantized coefficient; it shifts $A$ by a multiple of $2\pi\delta_{\tilde S}$ and so inserts a magnetic flux tube $2\pi m$ along $\partial\tilde S$. Problem 4⋆ carries this out, and [[week-11-monopole-condensation-4d|Week 11]] §5.3 explains why the lattice version is the identity. In $d=3$ the magnetic action is the enclosure rule of Week 9 §5.1.

## 7. What Semester I already contained [Stated — refs.]

The Kadanoff–Ceva seam of [[week-04-bkt-kramers-wannier-disorder|Week 4]] §4.1 is the twist (2.5) for the $\mathbb{Z}_2^{(0)}$ of the 2d Ising model, a finite group without a current, and its endpoints are GKSW's open defects. The flipped sheet of Week 5 §8.1 and the identity (3.1) of Week 15 are (5.6) at $\alpha=\pi$; Week 9 §5 is §3.2 at $d=3$; Week 11 §§5.1 and 5.3 are (5.6) and (5.8) in $d=4$, now with the sign of $\lambda_{\tilde V}$ fixed and joined by (5.9). In the center symmetry of [[week-14-fradkin-shenker-order-parameters|Week 14]], the $\mathbb{Z}_N^{(1)}$ operators on surfaces at a fixed point of the thermal circle link the Polyakov loop and act on it as a 0-form symmetry of the spatial theory, the reduction GKSW §4.1 describes for Maxwell theory.

## 8. Seminar: GKSW §§2–3 and §4.1

**Format.** The presentation states the paper's technical claim, identifies what it needs from Semester I and reproduces one nontrivial step at the board; discussion follows, and the instructor closes by placing the result on the course map (syllabus §7). As the first seminar of the block, it is presented by the instructor as the model. Every student reads the sections beforehand and brings Problem 1, and in the discussion one student redoes the board step for the magnetic symmetry (Problem 4⋆).

**Sections.** GKSW §2 (pp. 5–9), §3 (pp. 9–12) and §4.1 (pp. 12–14); Appendix F (pp. 56–57) for the discussion.

**The technical claim.** A symmetry is a family of topological operators on closed submanifolds that fuse by a group law, eqs. (2.2) and (3.1) of the paper. The charge is read from linking in spacetime, (3.2), from the intersection number at equal time, (3.3), and globally from the pairing of cohomology with homology, (3.4). For $q>0$ the group is abelian. Pure Maxwell theory has an electric and a magnetic $U(1)^{(1)}$, generated by (4.1) and (4.2), whose open versions end on improperly quantized lines and which have a mixed 't Hooft anomaly.

**What it needs from Semester I.** Week 2 §§5 and 8 (the dual lattice and the intersection pairing), Week 7 §§3–4 (electric flux and Gauss's law), Week 8 §2.2 (Dirac quantization), Week 11 §5 and Week 15 §2.

**The step at the board.** Derive the equal-time relation (3.3) of GKSW from the linking relation (3.2) for the electric operator (4.1). First fix the coefficient of $\star F$ by requiring that the operator act by $e^{i\alpha}$ on the unit Wilson line: GKSW write $j_e=\frac2{g^2}\star F$ without displaying their action, and in the course's normalization the coefficient is $1/e^2$, as (3.1) shows. Then compute the canonical commutator (§6.2) and recover its sign from the slab (§6.3). Close with GKSW's remark on p. 13 that an open magnetic surface is bounded by an improperly quantized Wilson line, which is Stokes' theorem, $e^{\frac{i\eta}{2\pi}\int_\Sigma F}=e^{\frac{i\eta}{2\pi}\oint_\gamma A}$ for $\partial\Sigma=\gamma$, a genuine line exactly when $\eta\in2\pi\mathbb{Z}$.

**For the discussion.** Why the abelianness argument of §3 of the paper does not reach the networks of Appendix F (F7); which Semester I operators are the open surfaces of §3 of the paper (the 't Hooft loop of Week 11 §5.3 and the vison of Week 5 §8.2); and what charged matter does to (4.1), which GKSW describe as still meaningful but no longer always topological.

**The open question it leaves for this course.** GKSW work in the continuum. Whether both symmetries of Maxwell theory, with their mixed anomaly, can be exact in a lattice regularization is the question that the modified Villain formulation answers (Sulejmanpasic–Gattringer; Gorantla–Lam–Seiberg–Shao), in Semester II Week 12 and Problem 7⋆⋆.

**On the course map.** The definitions are those of Week 15, now derived; the linking action is the operator form of the intersection pairing of Week 2; the anomaly belongs to Block 2, and gauging to Week 4.

## 9. Subtleties and fine print

**F1. The Euclidean $i$ of the electric operator.** Since $\frac1{e^2}\oint\star F=iq\,{\rm Link}$ inside Euclidean correlators, $\exp(i\alpha\oint\star F/e^2)$ gives the real factor $e^{-\alpha q{\rm Link}}$; the Euclidean operator is (3.3), equal on a time slice to $e^{i\alpha\Phi_E}$. The shift symmetry of the compact scalar has the Euclidean form $i\beta\star d\theta$ (§2), and the magnetic form $F/2\pi$ needs no $i$. The forms $\beta\star d\theta$ and $\star F/e^2$ of [[courses/generalized-symmetries-course/conventions|conventions]] §6 are the real-time ones.

**F2. Counterterms and topological invariance.** The bare exponentiated charge depends on the size of its support, (2.9) and (5.7); the twist supplies the counterterm that cancels this, and since the counterterm is a local functional of the support it changes nothing physical. In the continuum it diverges, and the operator is defined by the twist or by the Hamiltonian $e^{i\alpha Q}$.

**F3. The Kogut–Susskind dictionary.** The Kogut–Susskind $E_\ell$ is the momentum conjugate to $\theta_\ell=\int_\ell a$, which in the continuum conventions of [[courses/generalized-symmetries-course/conventions|conventions]] §10 is $\Pi=-E/e^2$ times the area of the dual face (§5.3). Thus $\Phi=-\Phi_E$, and the charge $q_x$ of $\delta E=-q$ is minus the charge that §10 assigns to the endpoint of a Wilson line: the forward Wilson line, positive by §3.1, has $q_x=-1$, as Week 7 §4.2 implies. Each convention is consistent on its own; the dictionary is needed whenever a lattice charge is compared with a continuum one.

**F4. Linking needs boundaries.** Equations (5.4) and (6.1) presuppose that Σ and $C$ bound. On a torus a sheet on a noncontractible cycle is a twisted boundary condition, $\langle U\rangle=Z_{\rm tw}/Z$ ([[courses/generalized-symmetries-course/conventions|conventions]] §6; Week 5 F6), and the equal-time content is the integer flux through the cycle, (5.8) and Problem 3.

**F5. The orientation of Link and the degree.** With ${\rm Link}(C,\partial\tilde V)=I(C,\tilde V)$, charged object first, the operator measures the charge enclosed for every $p$; for $p=0$, ${\rm Link}(x,\partial V)=1_V(x)$. The alternative $I(X,\tilde\Sigma)$ with $\partial X=C$ differs by $(-1)^{p+1}$, by (5.5). Written with the indicator $\Xi=\star^{-1}J_{\tilde\Sigma}$ of the sheet itself the twist is $F\to F-(-1)^{p+1}\alpha\,\Xi$, since $\Xi=(-1)^{p+1}d\lambda_{\tilde V}$ by (5.2) (checked for $p=0,1,2$ in $d=3,4$); written with $\lambda_{\tilde V}$, as [[courses/generalized-symmetries-course/conventions|conventions]] §6 does, it is uniform in $p$.

**F6. Which contact terms are physical.** In (2.3) only the coefficient of $\delta^d(x-x_k)$ is fixed by the symmetry. Derivative-of-δ terms, seagulls such as the $\alpha^2|\phi|^2(\partial1_V)^2$ of a charged scalar, and improvements depend on definitions, and none of them changes (2.4) or (2.6), because each either integrates to zero over a closed support or is absorbed in the twist.

**F7. When abelianness fails.** The argument of §4 needs a normal field along the support. GKSW Appendix F, following Freed, Moore and Segal, shows that on a spatial manifold with torsion the electric and magnetic operators of Maxwell theory, which are networks of surfaces with junctions on torsion classes, obey $U^E(\alpha)U^M(\beta)=\langle\phi(\alpha),\beta\rangle U^M(\beta)U^E(\alpha)$, with φ the Bockstein homomorphism. On $\mathbb{R}^D$ and $T^D$ there is no torsion, and the flux operators commute.

**F8. Explicit breaking keeps the operator and removes its topology.** With charge-$n$ matter or dynamical monopoles, (3.3) and (3.4) remain well-defined operators, GKSW's Gukov–Witten operators, but outside the surviving subgroup they depend on the support beyond its homology class. On the lattice the twisted sheet still exists, and the substitution that proves (5.6) fails at the matter links.

## 10. Common misconceptions

- **"The symmetry operator is the exponential of the Noether charge."** It is tempting because in a Hamiltonian $e^{i\alpha Q}$ is exactly that. In the path integral the exponentiated charge on a closed surface needs the counterterm of (2.8) and (5.7), and for a finite group there is no current at all; the definition that always works is the twist (2.5), GKSW's discontinuity across $M$.
- **"An operator and a loop that never touch cannot see each other."** For a local operator outside a closed surface this is true, which makes it tempting. For extended objects the topological invariant is the linking number, and (5.6) gives a phase for a sheet and a loop that never meet, as in Figure 3.
- **"Since $p$-form groups are abelian for $p\ge1$, higher-form symmetry operators always commute."** Parallel copies commute (§4). Operators whose supports cross in space can carry a phase, which is an 't Hooft anomaly or a mixed one (Problem 6⋆), and on spaces with torsion even the electric and magnetic fluxes of Maxwell theory fail to commute (F7).

## 11. Historical note

Gaiotto, Kapustin, Seiberg and Willett posted "Generalized global symmetries" in December 2014 (*JHEP* 02 (2015) 172). Their §2 recast ordinary symmetries as topological defects $U_g(M^{(d-1)})$ defined by a discontinuity of the fields, and used networks of such defects for flat backgrounds, discrete torsion and two-dimensional SPT phases. §3 stated the definition this week derives: topological operators on closed manifolds of codimension $q+1$ with group-law fusion, charges measured by linking, an abelian group for $q>0$, anomalies detected by the absence of topological junctions, and a dual $(d-q-2)$-form symmetry after gauging. The examples of §4 begin with Maxwell theory, whose two operators they call Gukov–Witten operators, and §5 interprets the Coulomb phase as the spontaneous breaking of both 1-form symmetries, with the photon as their Goldstone boson. The paper is written in continuum language and draws on Kapustin–Seiberg (2014), whose distinction between genuine and non-genuine lines it uses, and on Aharony–Seiberg–Tachikawa (2013). Within this course the ancestors are older: Wegner's $\mathbb{Z}_2$ gauge theory of 1971, read through its closed sheets in Week 5, the electric flux of Kogut and Susskind, and 't Hooft's flux sectors of 1978 (Week 14).

## 12. What to take away

1. **Technical:** the topological operator of a 0-form symmetry is the twist (2.5); to first order it is the exponentiated Euclidean current $j_E=iK$, and beyond first order it carries counterterms on its support. **Physical:** a symmetry operator is a cut across which the fields are rotated.
2. **Technical:** Maxwell's two currents are $\star F/e^2$, closed by the equation of motion, and $F/2\pi$, closed by the Bianchi identity; the Euclidean Gauss law (3.1) carries an $i$, so the Euclidean electric operator is (3.3). **Physical:** one operator counts the flux lines of charges, the other the flux quanta of monopoles.
3. **Technical:** on the lattice ${\rm Link}(C,\partial\tilde V)=\langle J_C,\star^{-1}J_{\tilde V}\rangle$, well defined by (5.3), and the twisted sheet gives $e^{iq\alpha{\rm Link}}$ exactly, (5.6). **Physical:** the phase is an Aharonov–Bohm phase of the charge around a sheet it never touches [Heuristic].
4. **Technical:** the commutator (6.3) and the linking (6.1) are one statement, related by the slab identity (6.4), and on the lattice by the transfer matrix, (5.9). **Physical:** an equal-time phase records a sheet swept through a line.
5. **Technical:** for $p\ge1$ the unit normal sphere $S^p$ is connected, so parallel copies of a symmetry operator can be exchanged without meeting and the group is abelian. **Physical:** a phase between operators on crossing supports signals an anomaly.

## 13. Looking ahead

Semester II Week 2 takes $\mathbb{Z}_N$ gauge theory to zero coupling, where its electric and magnetic 1-form symmetries are both exact and topological, and writes it as BF theory. The operators of §5.3 wrapping the cycles of a spatial torus then realize the clock–shift algebra $ZX=\omega XZ$, whose coefficient comes from the BF bracket as the phase of (6.3) came from the canonical commutator here, and the ground-state degeneracy $N^{2g}$ follows from the intersection pairing of Week 2 §8. Week 3 reads that degeneracy as the spontaneous breaking of a 1-form symmetry, and Week 4 gauges.

## 14. Problem set

*Routing:* Problems 1–3 are the classroom core; 4⋆–6⋆ are self-study consolidation; 7⋆⋆ and 8⋆⋆ are research extensions.

### Core problems

**1. $p$-form gauge fields: degrees and the Euclidean current.** (Extends §§2, 3.1 and 5.2 from $p=0,1$ to general $p$.) Let $A\in C^p(\Lambda,\mathbb{R})$ be a compact $p$-form gauge field in $d$ dimensions with Villain action $S=\frac\kappa2\|dA-2\pi n\|^2$, $n\in C^{p+1}(\Lambda,\mathbb{Z})$, and Wilson surfaces $W_q(C)=e^{iq\langle J_C,A\rangle}$ on closed $p$-chains. (a) From the Schwinger–Dyson equation derive $\kappa\langle\delta F\,W_q\rangle=iqJ_C\langle W_q\rangle$ with $F=dA-2\pi n$. (b) Using (5.2), show that the indicator $\Xi=\star^{-1}J_{\tilde\Sigma}$ of a closed dual $(d-p-1)$-chain $\tilde\Sigma=\partial\tilde V$ equals $(-1)^{p+1}d\lambda_{\tilde V}$, and deduce that inside correlators $\oint_{\tilde\Sigma}\omega_E=q\,{\rm Link}(C,\tilde\Sigma)$ for $\omega_E=(-1)^p\,i\kappa\star F$. Check $p=0$ and $p=1$ against §2.2 and (3.3). (c) Give the degrees of the electric and magnetic symmetries and the dimensions of their charged objects. (d) Find all $(d,p)$ for which the two degrees are equal, and all for which the magnetic symmetry is a 0-form symmetry, naming the local charged operators in each case with $p\le2$.

**2. Four dual loops around a plaquette.** (Extends the worked example of §5.1.) In $d=3$ let $C=\partial P_{12}(0)$. (a) For each of the four links ℓ of $C$ compute ${\rm Link}(C,\partial(\ell^*))$, where $\ell^*$ is the dual plaquette dual to ℓ, from (5.4) with the Hodge signs, and explain each sign geometrically. (b) Recompute the value for $\ell_2(\hat1)$ from (5.5): identify the dual link of $\partial(\ell_2(\hat1)^*)$ that is dual to $P_{12}(0)$, its coefficient, and the shuffle sign. (c) Let $\tilde V'=\ell_1(0)^*+\partial(\hat1^*)$, where $\hat1^*$ is the dual cube around the site $\hat1$. Show that $\partial\tilde V'=\partial(\ell_1(0)^*)$, count the cells of $\tilde V'$, and compute $I(C,\tilde V')$ directly.

**3. Electric flux sectors on the three-torus.** (Extends §6.2 to a compact space.) Consider pure $U(1)$ gauge theory on the spatial torus $T^3$ of side $L$, with $\Sigma_{xy}$ the 2-torus at fixed $z$ with normal $+\hat z$ and $C_z$ a loop winding once along $+\hat z$. (a) Show that the large gauge transformation $\lambda=2\pi z/L$ is implemented by $\exp\big(i\int d^3x\,\partial_i\lambda\,\Pi_i\big)$, that Gauss's law makes $\Phi_E(\Sigma_{xy})$ independent of $z$, and conclude that $\Phi_E(\Sigma_{xy})\in\mathbb{Z}$ on physical states. (b) Compute $U_\alpha(\Sigma_{xy})W_q(C_z)U_\alpha(\Sigma_{xy})^{-1}$ and state to which flux sector $W_q(C_z)$ maps the sector $\Phi_E=n$. (c) Explain why α is defined modulo $2\pi$ here and why it would not be in a noncompact theory.

### Starred problems

**4⋆. The magnetic symmetry at equal time.** (Extends §§6.2 and 6.4.) In $3+1$ dimensions let $T_m(\tilde C)=\exp\big(2\pi im\int_{\tilde S}E\cdot dS/e^2\big)$, with $\partial\tilde S=\tilde C$. (a) Show that $T_mA\,T_m^{-1}=A-2\pi m\,\delta_{\tilde S}$ and that the state $T_m|\psi\rangle$ carries an extra magnetic flux $2\pi m$ along $\tilde C$. (b) Show that $T_m$ commutes with every Wilson loop of integer charge, so that it depends on $\tilde S$ only through $\tilde C$. (c) Show that $U^m_\eta(\Sigma)\,T_m(\tilde C)=e^{i\eta m\,I_s(\tilde C,\Sigma)}\,T_m(\tilde C)\,U^m_\eta(\Sigma)$. (d) Explain why the lattice operator $e^{2\pi i\Phi}$ is the identity (Week 11 §5.3) while $T_m$ is not. *Hint:* for a flat disk with normal $\hat z$, $\nabla\times\big(\hat z\,\delta(z)\,\Theta_{\rm disk}\big)=\delta(z)\,\delta(r-R)\,\hat\varphi$, and $T_mBT_m^{-1}=B-c$ means that $T_m|\psi\rangle$ carries $B+c$.

**5⋆. A $(d-1)$-form symmetry and decomposition.** (Extends §5.2 to $d=2$, where a closed sheet is a pair of points.) In the 2d $\mathbb{Z}_2$ gauge theory of Week 5 §6, let $U(p)$ reverse β on the single plaquette $p$. (a) Using the substitution of §5.2 along a dual path from $p$ to $p'$, show that $U(p)U(p')$ is a change of variables, so that $U(p)$ is a topological local operator, and that $\langle U(p)W(C)\cdots\rangle=-\langle U(p')W(C)\cdots\rangle$ when exactly one of $p,p'$ is enclosed by a contractible $C$. (b) On the $L\times L$ torus with $N_s$ sites and $N_P$ plaquettes, show that $Z_\pm=\langle\frac{1\pm U(p)}2\rangle Z$ are $2^{N_s}(2\cosh\beta)^{N_P}$ and $2^{N_s}(2\sinh\beta)^{N_P}$. (c) Show that the theory is a sum of two universes labelled by the eigenvalue of $U$, that no local operator connects them and that Wilson lines are interfaces between them, and identify them with the two flux sectors of the spatial circle in the Hamiltonian. (d) For a finite abelian $(d-1)$-form symmetry in any $d$, show that $P_\chi=\frac1{|G|}\sum_g\chi(g)^*U_g$ are orthogonal projectors commuting with every local operator. *Hint:* in (b) use the plaquette variables of Week 5 §6 and the constraint $\prod_P\sigma_P=1$ on a closed surface. (We checked (b) by enumeration on the $3\times3$ torus.)

**6⋆. An abelian group with a phase.** (Extends §4, remark (iii).) In the $2+1$-dimensional $\mathbb{Z}_2$ gauge theory of [[courses/generalized-symmetries-course/conventions|conventions]] §§4 and 9, restricted to the flux-free sector $B_P=1$ (the toric-code limit), let $U^e(\tilde\gamma)=\prod\sigma^x_\ell$ over the links crossed by a closed dual curve $\tilde\gamma$ and $W(\gamma)=\prod_{\ell\in\gamma}\sigma^z_\ell$. (a) Show that any two $U^e$ commute and any two $W$ commute, and that both are topological in this sector. (b) On the torus, show that $U^e(\tilde\gamma_x)W(\gamma_y)=-W(\gamma_y)U^e(\tilde\gamma_x)$ when the two cycles cross once. (c) Explain why (b) does not contradict §4, and identify $W$ as the generator of a second 1-form symmetry under which $U^e$ is charged. *Hint:* count the links shared by the two supports; the continuation is Semester II Week 2.

### ⋆⋆ problems

**7⋆⋆. Both symmetries of Maxwell theory exact on the lattice.** *Known:* in the Villain theory the electric symmetry is exact and the magnetic one is broken by monopoles; with $dn=0$ imposed (Sulejmanpasic–Gattringer, arXiv:1901.02637; Gorantla–Lam–Seiberg–Shao, arXiv:2103.01257, Villain sections) both are exact, and GKSW §4.1 states their mixed anomaly in the continuum. *Explored:* the magnetic operator on closed dual surfaces of the 4d monopole-free lattice, its topological invariance by the identities of §5.1, and the anomaly when both symmetries are coupled to backgrounds, with the cup product of [[courses/generalized-symmetries-course/conventions|conventions]] §8. *Sources:* the two lattice papers, GKSW §4.1, this note. *Completion:* a cochain derivation of both linking actions and of the anomalous phase on $T^4$, checked numerically on one explicit background.

**8⋆⋆. Non-commuting fluxes from a cell complex.** *Known:* GKSW Appendix F, following Freed, Moore and Segal, gives $U^E(\alpha)U^M(\beta)=\langle\phi(\alpha),\beta\rangle U^M(\beta)U^E(\alpha)$ on spatial manifolds with torsion. *Explored:* a Kogut–Susskind Hamiltonian on a cell complex of $\mathbb{RP}^3$, with the electric operator built as a network with a junction on the torsion cycle. *Sources:* GKSW Appendix F; Week 2 for cellular (co)homology. *Completion:* the phase of (F.1), a sign here, obtained from explicit operators on the complex, with the step of §4 that fails identified.

## Self-study answer checkpoints

**Problem 1.** *Decisive step:* $\langle F,\Xi\rangle=(-1)^{p+1}\langle\delta F,\lambda_{\tilde V}\rangle$, from (5.2) with $q=d-p$. *Result:* $\omega_E=(-1)^pi\kappa\star F$, which is $i\beta\star d\theta$ for $p=0$ and $-\frac i{e^2}\star F$ for $p=1$. The electric symmetry has degree $p$ with $p$-dimensional charged objects, the magnetic one degree $d-p-2$ with $(d-p-2)$-dimensional ones. The degrees are equal exactly for $d=2p+2$ (the compact boson in $d=2$, Maxwell theory in $d=4$, the 2-form gauge field in $d=6$), and the magnetic symmetry is 0-form exactly for $d=p+2$, with local vortex operators for $p=0$, $d=2$, local monopole operators $e^{i\sigma}$ for $p=1$, $d=3$, and the local operators of the dual compact scalar for $p=2$, $d=4$. *Failure mode:* dropping the $(-1)^{p+1}$ and concluding that the scalar's operator measures $-q$ inside.

**Problem 2.** *Decisive step:* the shuffle sign $\epsilon(\{2\},\{1,3\})=-1$, which makes the normal of $\ell_2^*$ point along $-\hat2$. *Result:* $+1$ for $\ell_1(0)$, $-1$ for $\ell_2(\hat1)$, $-1$ for $\ell_1(\hat2)$, $+1$ for $\ell_2(0)$: $C$ crosses the dual plaquettes of its bottom and left links along their normals and those of its right and top links against them. In (b) the dual link dual to $P_{12}(0)$, from $(\frac12,\frac12,-\frac12)$ to $(\frac12,\frac12,\frac12)$, enters $\partial(\ell_2(\hat1)^*)$ with coefficient $-1$, and $\epsilon(\{1,2\},\{3\})=+1$ gives $-1$, the value found in (a). In (c) $\tilde V'$ has five cells, the other five faces of the dual cube around $\hat1$, and $I(C,\tilde V')=+1$, through the face dual to $\ell_2(\hat1)$. *Failure mode:* using the coefficient of ℓ in $C$ without the shuffle sign, which gives $+1,+1,-1,-1$.

**Problem 3.** *Decisive step:* $\int d^3x\,\frac{2\pi}L\Pi_z=2\pi\,\Phi_\Pi(\Sigma_{xy})$ by $z$-independence, together with the invariance of physical states under large gauge transformations of a compact gauge group. *Result:* $\Phi_E=-\Phi_\Pi\in\mathbb{Z}$; $U_\alpha W_q(C_z)U_\alpha^{-1}=e^{-iq\alpha}W_q(C_z)$, since $I_s(C_z,\Sigma_{xy})=+1$, so $W_q(C_z)$ maps $\Phi_E=n$ to $n-q$: the loop carries electric flux $-q$ along its own orientation. The spectrum of $\Phi_E$ is $\mathbb{Z}$, so $U_{2\pi}=1$; in a noncompact theory the large transformations are absent, $\Phi_E$ is continuous and α ranges over $\mathbb{R}$. *Failure mode:* the sign $n\to n+q$, which comes from taking $E$ instead of $\Pi=-E/e^2$ as the momentum conjugate to $A$.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester II Block 1. Written to the note-quality-template standard on 2026-10-01. Last revised 2026-10-02.*
