---
title: "Lecture 3 — Modular structure of an entangled pair"
type: lecture-notes
course: syllabus
edition: "2.0"
semester: 1
week: 2
lecture: 3
duration: "2 hours; additional self-study material"
status: written — checked in the scope of the validation record
modified: 2026-09-28
---

# Lecture 3 — Modular structure of an entangled pair

A reduced density matrix tells us how a state weights the observables on one side of a bipartite system. Its eigenvalues also determine a family of transformations of those observables. For a thermal state this family is ordinary time evolution with a temperature-dependent rescaling. For a general state there need be no such physical identification.

We will calculate that structure using two finite systems and then two oscillators. The purpose is to learn what the modular operator does before meeting it as an abstract theorem. The distinction between a one-sided density matrix and the full modular operator will be especially important when the course reaches horizons.

## How to use this lecture

**Classroom core, 120 minutes.** Review Schmidt weights and matrix units (20 minutes), derive the Tomita and modular operators (30), compute the unequal qubit example (25), identify Gibbs modular flow with rescaled time (20), and introduce the oscillator thermofield double (25). The full KMS proof and the domain discussion are self-study material; the instructor guide gives a shorter oscillator route if discussion takes longer.

**Self-study.** Verify the action on every basis vector before manipulating operator symbols. Check all three identities $\Delta\Omega=\Omega$, $S_T^2=I$, and $J\Delta J=\Delta^{-1}$. Work through the KMS boundary condition using matrix units.

**Research extension.** Compare the finite construction with the general Tomita–Takesaki theorem and with Bisognano–Wichmann. The latter requires spacetime and QFT assumptions absent from the finite model.

**Prerequisites.** [[lecture-01-observables-and-restricted-access|Lecture 1]], spectral decomposition of a positive matrix, and the oscillator energy spectrum for Section 7. This lecture can be read independently of the detailed qutrit decoder.

**Reading.** Witten, [arXiv:1803.04993](https://arxiv.org/abs/1803.04993), Section 4, develops finite-dimensional modular operators. The canonical AQFT course gives a fuller account in [[week-05-tomita-operator|its Tomita lecture]]. For the later holographic use of a thermofield double, see Maldacena, [arXiv:hep-th/0106112](https://arxiv.org/abs/hep-th/0106112).

**What this lecture imports.** We recall the finite Schmidt decomposition and prove the modular identities in that representation. The general Tomita–Takesaki and Bisognano–Wichmann theorems are stated only as later destinations. No geometry follows from the finite calculation alone.

## 1. The state and the accessible algebra

Take two $d$-dimensional systems and a normalized vector
$$
|\Omega\rangle
=\sum_{j=1}^{d}\sqrt{p_j}\,
|j\rangle_A|j\rangle_B,
\qquad
p_j>0,\qquad \sum_jp_j=1.
$$
The displayed basis is a Schmidt basis. A general bipartite pure state can be brought to this form by applying the singular-value decomposition to its coefficient matrix. The nonzero singular values are $\sqrt{p_j}$; the two reduced density matrices have eigenvalues $p_j$.

For now, both systems have dimension $d$ and all coefficients are nonzero. The accessible algebra is
$$
\mathcal M_A=\mathcal B(\mathcal H_A)\otimes I_B,
$$
and
$$
\rho_A=\sum_jp_j|j\rangle\langle j|_A,\qquad
\rho_B=\sum_jp_j|j\rangle\langle j|_B.
$$
The condition $p_j>0$ says that both matrices have full support. They need not be maximally mixed.

### 1.1 Why full support matters

Introduce matrix units $E_{ij}=|i\rangle\langle j|$ on $A$. They act on the state as
$$
(E_{ij}\otimes I_B)|\Omega\rangle
=\sqrt{p_j}|i,j\rangle.
$$
Since every $\sqrt{p_j}$ is nonzero, these vectors span the full bipartite Hilbert space. We call $\Omega$ **cyclic** for $\mathcal M_A$.

If $(a\otimes I_B)\Omega=0$, then
$$
\sum_j\sqrt{p_j}\,a|j\rangle_A|j\rangle_B=0.
$$
Orthogonality of the $B$ basis forces $a|j\rangle=0$ for every $j$, so $a=0$. We call $\Omega$ **separating** for $\mathcal M_A$.

These are algebraic support statements. Cyclicity does not say that a unitary in Alice's laboratory can prepare every bipartite vector deterministically. The operators generating the span include nonunitary matrices, and some required norms become large when a Schmidt weight is small.

**Checkpoint 1.** Is $\sqrt{3/4}|00\rangle+\sqrt{1/4}|11\rangle$ cyclic and separating for the first qubit's full algebra?

**Answer.** Yes. Both Schmidt coefficients are nonzero. Maximal entanglement is not required.

## 2. The Tomita map compares an operation with its adjoint

Knowing $\Omega$ and the algebra gives a distinguished rule:
$$
S_T\bigl((a\otimes I_B)\Omega\bigr)
=(a^\dagger\otimes I_B)\Omega.
$$
The subscript $T$ distinguishes this map from entropy. Because the state is separating, the vector $(a\otimes I)\Omega$ determines $a$ uniquely, so the rule is well defined. Because the state is cyclic in this finite model, its domain is the whole Hilbert space.

The map is **antilinear**:
$$
S_T(c\,a\Omega)=c^*a^\dagger\Omega.
$$
Adjointing the operation conjugates its complex coefficient. Treating $S_T$ as an ordinary complex-linear matrix would give incorrect formulas.

On the matrix-unit vectors,
$$
S_T\bigl(\sqrt{p_j}|i,j\rangle\bigr)
=\sqrt{p_i}|j,i\rangle.
$$
Thus, for the ordinary orthonormal basis,
$$
\boxed{
S_T|i,j\rangle=\sqrt{\frac{p_i}{p_j}}\,|j,i\rangle,
}
$$
with antilinear extension to superpositions.

This formula explains why $S_T$ is generally not antiunitary. The norms of $E_{ij}\Omega$ and $E_{ji}\Omega$ are $\sqrt{p_j}$ and $\sqrt{p_i}$. Interchanging the operation and its adjoint can change the weight of a transition.

Applying the antilinear map twice returns the original basis vector:
$$
S_T^2|i,j\rangle
=\sqrt{\frac{p_i}{p_j}}
\sqrt{\frac{p_j}{p_i}}|i,j\rangle
=|i,j\rangle.
$$
An involution can still fail to preserve norm; those are different properties.

> **Physical picture.** The state assigns different weights to different transitions. Acting with $E_{ij}$ selects the Schmidt component labeled by $j$; acting with its adjoint selects the component labeled by $i$. The Tomita map records their relative weighting. We will separate that weighting from the conjugate exchange of the two sides.

## 3. Separating the exchange from the weights

Define an antilinear exchange
$$
J\left(\sum_{ij}c_{ij}|i,j\rangle\right)
=\sum_{ij}c_{ij}^*|j,i\rangle.
$$
This preserves norms, conjugates inner products, and satisfies $J^2=I$. It is an antiunitary map.

Define also the positive operator
$$
\Delta=\rho_A\otimes\rho_B^{-1}.
$$
Its action is
$$
\Delta|i,j\rangle=\frac{p_i}{p_j}|i,j\rangle.
$$
Since all $p_j$ are positive, the inverse is well defined in this finite-dimensional example.

The positive square root followed by $J$ gives
$$
J\Delta^{1/2}|i,j\rangle
=\sqrt{\frac{p_i}{p_j}}|j,i\rangle
=S_T|i,j\rangle.
$$
Therefore
$$
\boxed{S_T=J\Delta^{1/2}.}
$$
This is the finite-model polar decomposition. We have constructed both factors explicitly. Equivalently $\Delta=S_T^\dagger S_T$ with the adjoint understood for antilinear maps.

### 3.1 Checks that prevent common mistakes

Only terms with $i=j$ occur in $\Omega$, so
$$
\Delta\Omega=\Omega,\qquad J\Omega=\Omega.
$$
Interchanging $i,j$ in the eigenvalue ratio also gives
$$
J\Delta J=\Delta^{-1}.
$$
The spectrum consists of ratios $p_i/p_j$, not the probabilities $p_i$ alone. In particular, $\Delta$ is not the one-sided density matrix $\rho_A$.

### 3.2 The conjugation identifies the commutant

For any matrix $a$ on $A$, applying the two exchanges to a basis vector yields
$$
J(a\otimes I_B)J=I_A\otimes\overline a_B,
$$
where the bar means entrywise complex conjugation in the paired Schmidt bases. Since complex conjugation maps the set of all matrices onto itself,
$$
J\mathcal M_AJ=I_A\otimes\mathcal B(\mathcal H_B)=\mathcal M_A'.
$$
This is a model proof of the modular commutant relation.

The formula depends on the chosen Schmidt identification of the two bases. It is not a universal physical operation that copies Alice's state to Bob. Its meaning is an algebraic relation between operators.

## 4. Modular flow and its two generators

The positive eigenvalues of $\Delta$ allow us to define its imaginary powers. We follow the [[courses/ads-cft-course/conventions|course convention]], which agrees with the AQFT course:
$$
\sigma_t^\Omega(x)=\Delta^{-it}x\Delta^{it}.
$$
Imaginary powers of a positive invertible matrix are unitary, so this preserves multiplication and adjoints. For Alice's algebra, Bob's factors cancel:
$$
\sigma_t^\Omega(a\otimes I_B)
=\bigl(\rho_A^{-it}a\rho_A^{it}\bigr)\otimes I_B.
$$
The result stays inside $\mathcal M_A$.

Define the one-sided **modular Hamiltonian**
$$
K_A=-\log\rho_A.
$$
Then
$$
\sigma_t^\Omega(a)=e^{itK_A}a\,e^{-itK_A}.
$$
This looks like Heisenberg evolution. The resemblance becomes a physical time identification only when we know how $K_A$ relates to the system's independently specified Hamiltonian.

The generator on the complete bipartite Hilbert space is instead
$$
\boxed{
\widehat K=-\log\Delta
=K_A\otimes I_B-I_A\otimes K_B.
}
$$
The subtraction follows by taking the logarithm of the tensor-product eigenvalues. It makes $\widehat K\Omega=0$. By contrast, $K_A$ alone generally does not annihilate $\Omega$.

There are therefore three related objects:

| Object | Acts on | Role |
|---|---|---|
| $\rho_A$ | One system | Represents its restricted state |
| $K_A=-\log\rho_A$ | One system | Generates modular conjugation of its observables |
| $\Delta$ and $\widehat K=-\log\Delta$ | The bipartite representation | Include both sides and leave the reference vector invariant |

**Checkpoint 2.** If the pair is maximally entangled, is modular evolution a nontrivial rotation?

**Answer.** No. Then $\rho_A=\rho_B=I/d$, so $\Delta=I$, $\widehat K=0$, and $\sigma_t$ is the identity. The one-sided $K_A=(\log d)I$ also generates trivial conjugation. A large entropy does not imply nontrivial modular flow.

## 5. A qubit example with every coefficient visible

Choose
$$
\Omega=\frac{\sqrt3}{2}|00\rangle+\frac12|11\rangle,
\qquad
\rho_A=\rho_B=
\begin{pmatrix}
3/4&0\\
0&1/4
\end{pmatrix}.
$$
In the ordered basis $|00\rangle,|01\rangle,|10\rangle,|11\rangle$,
$$
\Delta=\operatorname{diag}(1,3,1/3,1).
$$
The Tomita map acts by
$$
S_T|01\rangle=\sqrt3|10\rangle,\qquad
S_T|10\rangle=\frac1{\sqrt3}|01\rangle,
$$
and fixes $|00\rangle,|11\rangle$, with complex conjugation of coefficients.

The two generators are
$$
K_A=\operatorname{diag}\bigl(\log(4/3),\log4\bigr),
$$
and
$$
\widehat K=\operatorname{diag}(0,-\log3,\log3,0).
$$
The negative entry in $\widehat K$ is consistent with positivity of $\Delta$: a positive number larger than one has a negative negative-logarithm. The full generator is a difference of one-sided generators.

For $E_{01}=|0\rangle\langle1|$,
$$
\sigma_t(E_{01})
=\left(\frac{p_1}{p_0}\right)^{it}E_{01}
=e^{-it\log3}E_{01}.
$$
Similarly $\sigma_t(E_{10})=e^{it\log3}E_{10}$. With $X=E_{01}+E_{10}$ and $Y=-iE_{01}+iE_{10}$,
$$
\begin{aligned}
\sigma_t(X)&=\cos(t\log3)X+\sin(t\log3)Y,\\
\sigma_t(Y)&=\cos(t\log3)Y-\sin(t\log3)X.
\end{aligned}
$$
These are explicit rotations of observables. The state remains invariant under them because $\rho_A$ commutes with all its own powers.

If the physical Hamiltonian is $H=\epsilon|1\rangle\langle1|$, the state is Gibbs exactly when $\beta\epsilon=\log3$. If a different Hamiltonian has been specified, this thermal interpretation must be checked again. Writing $K_A=-\log\rho_A$ does not by itself identify the laboratory energy or temperature.

## 6. Thermal states and the KMS relation

For a Gibbs state on a finite system,
$$
\rho_\beta=\frac{e^{-\beta H}}{Z},
\qquad Z=\operatorname{Tr}e^{-\beta H},
$$
the modular Hamiltonian is
$$
K_\beta=\beta H+(\log Z)I.
$$
The scalar drops out of conjugation:
$$
\sigma_t^\beta(a)
=e^{i\beta tH}a\,e^{-i\beta tH}.
$$
If physical Heisenberg evolution is $\alpha_s(a)=e^{isH}ae^{-isH}$, then
$$
\boxed{\sigma_t^\beta=\alpha_{\beta t}.}
$$
The modular parameter $t$ is dimensionless; physical time is $s=\beta t$ in units $\hbar=1$. The temperature rescales the clock.

### 6.1 What the KMS condition compares

The Kubo–Martin–Schwinger condition relates two orderings of a correlation function through imaginary time. For our modular-flow sign it reads
$$
F_{a,b}(t)=\omega(a\sigma_t(b)),\qquad
F_{a,b}(t+i)=\omega(\sigma_t(b)a).
$$
The function is analytic between these boundary lines. The strip height is one for the modular parameter; for physical Gibbs time the height is $\beta$.

The two operator orderings need not agree at the same real time. Imaginary continuation relates them. This is why replacing KMS by a statement of ordinary periodicity would miss the noncommutativity.

### 6.2 Finite-matrix proof

Let $\rho>0$, $\omega(x)=\operatorname{Tr}(\rho x)$, and
$$
F_{a,b}(z)
=\operatorname{Tr}\bigl(\rho a\rho^{-iz}b\rho^{iz}\bigr).
$$
In finite dimensions this is a finite sum of exponentials and is analytic. Its factors are uniformly bounded for $0\le\operatorname{Im}z\le1$ because imaginary powers along the real direction are unitary.

At the upper boundary,
$$
\rho^{-i(t+i)}=\rho^{1-it},\qquad
\rho^{i(t+i)}=\rho^{-1+it}.
$$
Substitution gives
$$
\begin{aligned}
F_{a,b}(t+i)
&=\operatorname{Tr}\bigl(\rho a\rho\,\sigma_t(b)\rho^{-1}\bigr)\\
&=\operatorname{Tr}\bigl(a\rho\,\sigma_t(b)\bigr)\\
&=\operatorname{Tr}\bigl(\rho\,\sigma_t(b)a\bigr).
\end{aligned}
$$
The last two steps use cyclicity of the trace. This proves the stated condition.

**Model proof.** Every faithful finite-dimensional state is KMS at modular inverse temperature one for its own modular flow. It need not be thermal for an unrelated physical evolution.

### 6.3 Check the sign on the unequal qubit

Choose $a=E_{10}$ and $b=E_{01}$ in Section 5. Then
$$
F(t)=\frac14e^{-it\log3}.
$$
At $t+i$, the exponential acquires a factor of three:
$$
F(t+i)=\frac34e^{-it\log3}.
$$
The reversed ordering gives exactly the same answer because $E_{01}E_{10}=E_{00}$. This one calculation is a useful sign check whenever modular conventions are translated.

## 7. Two oscillators and the thermofield double

Consider two identical oscillators with Hamiltonians $H_A=\epsilon N_A$ and $H_B=\epsilon N_B$, omitting a common zero-point energy that cancels from the formulas below. Here $N|n\rangle=n|n\rangle$ and $\epsilon>0$.

Set $q=e^{-\beta\epsilon}$ with $0<q<1$, and prepare
$$
|\Omega_\beta\rangle
=\sqrt{1-q}\sum_{n=0}^\infty q^{n/2}|n\rangle_A|n\rangle_B.
$$
Its normalization follows from the geometric series:
$$
\langle\Omega_\beta|\Omega_\beta\rangle
=(1-q)\sum_{n=0}^\infty q^n=1.
$$
This is a **thermofield double**: a pure state of two systems whose Schmidt coefficients are square roots of Gibbs probabilities.

### 7.1 The reduced state and its entropy

Tracing out $B$ removes terms with unequal occupation numbers:
$$
\rho_A=(1-q)\sum_{n=0}^\infty q^n|n\rangle\langle n|
=\frac{e^{-\beta H_A}}{Z},
\qquad Z=\frac1{1-q}.
$$
The average occupation is
$$
\bar n=(1-q)\sum_n nq^n=\frac q{1-q}.
$$
The entropy follows directly from the eigenvalues:
$$
\begin{aligned}
S(\rho_A)
&=-\sum_n(1-q)q^n
\bigl[\log(1-q)+n\log q\bigr]\\
&=-\log(1-q)-\frac q{1-q}\log q\\
&=(\bar n+1)\log(\bar n+1)-\bar n\log\bar n.
\end{aligned}
$$
The last line uses $q=\bar n/(\bar n+1)$. It is finite for every $0<q<1$.

### 7.2 The two-sided generator

The same Schmidt calculation gives
$$
\Delta|n,m\rangle=q^{n-m}|n,m\rangle,
$$
understood as a positive self-adjoint diagonal operator on its spectral domain. The finite linear span of the occupation basis is a core; it is not the whole domain. Unlike the finite matrix example, $\Delta$ and its inverse are unbounded here.

The full modular generator is
$$
\widehat K=-\log\Delta
=\beta(H_A-H_B).
$$
The normalization constants in $K_A=\beta H_A+\log Z$ and $K_B=\beta H_B+\log Z$ cancel. The paired occupations make $(H_A-H_B)\Omega_\beta=0$.

On Alice's lowering operator $a_A$, the formal action on the finite-particle domain is
$$
\sigma_t(a_A)=e^{-i\beta\epsilon t}a_A.
$$
For a bounded alternative, the matrix unit $|n\rangle\langle m|$ transforms as $e^{i\beta\epsilon(n-m)t}|n\rangle\langle m|$. The latter is sufficient to test the correlation identities without treating an unbounded annihilation operator as an element of $\mathcal B(\mathcal H_A)$.

> **Physical picture.** The purification supplies correlated energy labels on two sides. Its modular operator compares the thermal weights of a transition on one side with those on the other. The difference $H_A-H_B$ preserves the paired state and determines opposite orientations in the two-sided modular description.

### 7.3 The limits teach two different lessons

As $q\to0$, the vector approaches $|0,0\rangle$ and the reduced state loses full support in the limit. The cyclic-separating construction on the full oscillator algebra no longer applies to that limiting product state in the same way.

As $q\to1$, $Z$ and the entropy diverge. At $q=1$ the displayed sum is not a normalized vector, and there is no infinite-temperature Gibbs density matrix for this oscillator. One must not substitute $q=1$ into a formula requiring a trace-class state.

Even at fixed $0<q<1$, $\Delta$ is unbounded and its spectrum has an accumulation point at zero. Yet Alice's algebra is still the type-I algebra $\mathcal B(\ell^2(\mathbb N))$. **An unbounded modular operator for one state does not establish type III.** This concrete counterexample will be useful when the course later studies continuum and large-$N$ limits.

## 8. What changes in the general theorem?

In the finite model, every operation was defined on the full Hilbert space and every inverse was a matrix inverse. In QFT, the initial Tomita map is defined on the dense set $\mathcal M\Omega$. Proving that it is closable, identifying the domain of its closure, and showing that its polar factors preserve the algebra require analytic work.

**Stated only.** The Tomita–Takesaki theorem supplies these results for a von Neumann algebra with a cyclic and separating vector. It gives
$$
J\mathcal MJ=\mathcal M',
\qquad
\Delta^{-it}\mathcal M\Delta^{it}=\mathcal M.
$$
The finite calculations motivate and verify a model of this structure; they do not prove the infinite-dimensional theorem. Witten's [notes](https://arxiv.org/abs/1803.04993) and the canonical AQFT course provide the continuation.

When a local QFT algebra is type III, the intrinsic local trace and reduced density matrix used here are unavailable. The modular operator is still defined from the pair $(\mathcal M,\Omega)$. Its existence is not contingent on writing $\Delta$ as a ratio of local density matrices.

An additional theorem can identify modular evolution with geometry in special settings. For the vacuum and a Rindler wedge, Bisognano–Wichmann gives a boost interpretation under its QFT hypotheses. For a generic state and region, modular flow need not move local operators along a geometric trajectory.

The thermofield-double description of an eternal AdS black hole requires a suitable holographic theory and regime. An entangled oscillator pair does not meet those requirements merely because its reduced states are thermal.

## 9. What to take away

- Full nonzero Schmidt support, rather than maximal entanglement, gives the cyclic-separating property in the finite model.
- The Tomita map is antilinear and measures the relative weighting of an operation and its adjoint.
- $\Delta=\rho_A\otimes\rho_B^{-1}$ contains ratios of Schmidt weights and fixes the reference vector.
- The one-sided generator $K_A$ and full generator $\widehat K$ are different objects.
- A Gibbs state identifies modular flow with physical time rescaled by $\beta$; the general modular construction does not choose a physical Hamiltonian.
- Unbounded modular data or thermal marginals alone do not establish an algebraic type or a spacetime interpretation.

The next lecture returns to encoding. We will combine the distinction between a logical and a physical algebra with entropy and modular Hamiltonians, deriving an exact finite-model counterpart of formulas that later acquire gravitational interpretations.

## 10. Problem set

### Classroom core

**1. Support.** For $\Omega_p=\sqrt p|00\rangle+\sqrt{1-p}|11\rangle$, determine when the vector is cyclic and separating for $M_2(\mathbb C)\otimes I$. Exhibit an operator witnessing the failure of separatingness at $p=1$.

**2. Modular spectrum.** Compute the four eigenvalues of $\Delta$ for general $0<p<1$, and verify $\Delta\Omega_p=\Omega_p$.

**3. Antilinearity.** Evaluate $S_T(i|01\rangle)$ for the unequal qubit example. Explain why applying a linear swap matrix with positive weights gives the wrong sign.

**4. Thermal clock.** Let $H=\epsilon|1\rangle\langle1|$ and $\beta\epsilon=\log5$. Find the probabilities, the modular phase of $E_{01}$, and the relation between physical and modular time.

### Self-study consolidation

**5. The KMS boundary.** For $\rho=\operatorname{diag}(p,1-p)$, take $a=E_{10}$ and $b=E_{01}$. Calculate $F(t)$ and $F(t+i)$ and verify the reversed-order condition.

**6. Oscillator entropy.** Starting from the geometric series, derive $\bar n=q/(1-q)$ and the entropy in Section 7. Evaluate both at $q=1/2$.

**7. The conjugation.** Verify $J(a\otimes I)J=I\otimes\overline a$ first for $a=E_{01}$ and then for $a=iE_{01}$. Identify where antilinearity is used.

### Research extension

**8. Two meanings of temperature.** Choose a faithful qubit density matrix that does not commute with the independently specified Hamiltonian $H=\epsilon Z/2$. Compute its modular generator and show that its modular evolution differs from evolution under $H$ for every choice of positive inverse temperature. Completion means an explicit pair of matrices and a comparison of the resulting actions. No claim about a physical detector temperature follows from the modular construction alone.

## 11. Answer checkpoints

**1.** Both properties hold for $0<p<1$. At $p=1$, $(|1\rangle\langle1|\otimes I)|00\rangle=0$ although the operator is nonzero, so separatingness fails. The cyclic span is only $\mathcal H_A\otimes|0\rangle_B$.

**2.** In the ordered basis the eigenvalues are
$$
1,\quad \frac p{1-p},\quad \frac{1-p}{p},\quad1.
$$
The reference vector uses only the first and fourth basis vectors.

**3.** $S_T(i|01\rangle)=-i\sqrt3|10\rangle$. A complex-linear map would retain $i$ and therefore fail the defining adjoint rule.

**4.** The probabilities are $5/6$ and $1/6$. The modular phase is $e^{-it\log5}$; physical time is $s=\beta t$. The dimensionless product $\beta\epsilon$ controls the phase.

**5.** With $r=(1-p)/p$,
$$
F(t)=(1-p)r^{it},\qquad
F(t+i)=(1-p)r^{it-1}=p\,r^{it}.
$$
The upper boundary equals $\operatorname{Tr}(\rho\,\sigma_t(E_{01})E_{10})$.

**6.** Differentiate $\sum_nq^n=(1-q)^{-1}$ and multiply by $q(1-q)$ to obtain the occupation. At $q=1/2$, $\bar n=1$ and $S=2\log2$.

**7.** The first case gives $I\otimes E_{01}$; the second gives $-iI\otimes E_{01}$. The coefficient is conjugated by the outer $J$.

**8.** One choice is $\rho=(I+rX)/2$ with $0<r<1$. Its modular Hamiltonian is $cI+dX$, where
$$
d=\frac12\log\frac{1-r}{1+r}\ne0.
$$
It generates rotations about the $X$ axis. Evolution under the specified $Z$ Hamiltonian rotates about the $Z$ axis. In particular, modular flow fixes $X$ whereas physical evolution does not. The two groups cannot coincide by a positive time rescaling.

---

Previous: [[lecture-02-three-qutrit-code|Lecture 2]]. Next: [[lecture-04-entropy-and-algebraic-codes|Lecture 4 — Entropy and algebraic codes]]. Return to the [[courses/ads-cft-course/syllabus|course route]].

**Wiki connections.** [[tomita-takesaki-modular-theory|Tomita–Takesaki modular theory]] · [[thermofield-double-state|thermofield double]]
