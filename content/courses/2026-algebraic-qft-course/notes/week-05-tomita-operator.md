---
title: "Week 5 — Cyclic-Separating Vectors and the Tomita Operator"
type: lecture-notes
course: syllabus
semester: 1
week: 5
block: B
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 1–4, especially vN algebras and KMS states
modified: 2026-08-24
---

# Week 5 — Cyclic-Separating Vectors and the Tomita Operator

> *Week 4 ended with the promise that every faithful normal state on a von Neumann algebra carries its own time evolution. This week we build the machine that produces it. The input is austere: a von Neumann algebra $\mathcal{M}\subset\mathcal{B}(\mathcal{H})$ and a vector $\Omega$ that is cyclic and separating. The output is the Tomita operator $S$, its polar decomposition $S=J\Delta^{1/2}$, and the two objects that will run the rest of the course: the modular conjugation $J$ and the modular operator $\Delta$.*

### How to use this chapter

- **In class:** establish cyclicity and separatingness in finite-dimensional standard form, define $S_0(A\Omega)=A^*\Omega$, and spend time on why $S_0$ is well defined and closable before taking its polar decomposition.
- **For self-study:** compute $S$, $J$, and $\Delta$ for a faithful matrix state on Hilbert–Schmidt space. Use that calculation as the dictionary for every abstract formula in the chapter.
- **Instructor checkpoint:** ask for the anti-linearity checks and for the exact identity $JL_aJ=R_{a^*}$. Cyclic/separating is information completeness, not a synonym for maximal entanglement.

## 0. Reading

**Primary:**
- Bratteli & Robinson, Vol. I, §2.5, for the standard Tomita-Takesaki setup.
- Takesaki, *Theory of Operator Algebras II*, ch. VI, for the operator-theoretic version.

**Secondary:**
- Kadison & Ringrose, Vol. II, ch. 9.
- Witten, "Notes on some entanglement properties of QFT," arXiv:1803.04993, §3 — same sign convention as this course.

**Optional research reading:**
- Takesaki, "Tomita's theory of modular Hilbert algebras and its applications," Lecture Notes in Mathematics 128.
- Connes & Rovelli, "Von Neumann algebra automorphisms and time-thermodynamics relation in generally covariant quantum theories," *CQG* 11 (1994), for the later thermal-time interpretation.

**Survival-kit background.** Before entering the domain arguments, review [[functional-analysis-survival-kit|Appendix A]] for closable operators, anti-linear adjoints and polar decomposition, and the use of graph norms and cores. These are the analytic prerequisites behind the proof; the finite-dimensional model below can be read without them.

## 1. Why cyclic and separating?

Let $\mathcal{M}\subset\mathcal{B}(\mathcal{H})$ be a von Neumann algebra. A vector $\Omega\in\mathcal{H}$ gives a normal vector state
$$
\omega_\Omega(a)=\langle \Omega,a\Omega\rangle,\qquad a\in\mathcal{M}.
$$
Tomita-Takesaki theory starts when this vector sees both the algebra and its commutant without losing information.

**Definition 1.1.** A vector $\Omega$ is **cyclic** for $\mathcal{M}$ if
$$
\overline{\mathcal{M}\Omega}=\mathcal{H}.
$$
It is **separating** for $\mathcal{M}$ if
$$
a\Omega=0,\quad a\in\mathcal{M}
\quad\Longrightarrow\quad
a=0.
$$

Cyclicity says $\Omega$ generates the Hilbert space by acting with observables. Separating says no nonzero observable annihilates the state. The two conditions are dual to one another through the commutant.

> **Physical picture—with an important warning.** In a bipartite type-I model, cyclic and separating means that every Schmidt coefficient is nonzero: the reduced state has full support. It does **not** mean “maximally entangled”; unequal nonzero Schmidt coefficients work equally well. In QFT, Reeh–Schlieder says that vectors $a\Omega$ with $a$ localized in a small region are dense. This is a statement about approximation by algebra elements, whose norms may grow without bound, not a deterministic protocol for preparing a distant state or sending a signal. Separatingness says that no nonzero local operator annihilates the vacuum. Thus cyclicity and separatingness encode full support and exceptionally strong vacuum correlations, while operational entanglement claims require additional arguments.

**Lemma 1.2. [Proved.]** $\Omega$ is cyclic for $\mathcal{M}$ iff $\Omega$ is separating for $\mathcal{M}'$. Likewise, $\Omega$ is separating for $\mathcal{M}$ iff $\Omega$ is cyclic for $\mathcal{M}'$.

**Proof.** Suppose $\Omega$ is cyclic for $\mathcal{M}$ and $b'\Omega=0$ for some $b'\in\mathcal{M}'$. For every $a\in\mathcal{M}$,
$$
b'a\Omega=ab'\Omega=0.
$$
Since $\mathcal{M}\Omega$ is dense, $b'=0$. Hence $\Omega$ is separating for $\mathcal{M}'$.

Conversely, suppose $\Omega$ is separating for $\mathcal{M}'$. Let
$$
K:=\overline{\mathcal{M}\Omega}.
$$
The subspace $K$ reduces $\mathcal{M}$: it is invariant under every $a\in\mathcal{M}$ and under every $a^*$, since $\mathcal{M}$ is a $*$-algebra. Therefore the orthogonal projection $P_K$ commutes with $\mathcal{M}$, so $P_K\in\mathcal{M}'$. Also $P_K\Omega=\Omega$. Thus $(1-P_K)\Omega=0$. Separatingness for $\mathcal{M}'$ gives $1-P_K=0$, so $K=\mathcal{H}$. The remaining implication follows by replacing $\mathcal{M}$ by $\mathcal{M}'$ and using $\mathcal{M}''=\mathcal{M}$. $\square$

**Lemma 1.3. [Proved.]** The vector state $\omega_\Omega$ is faithful on $\mathcal{M}$ iff $\Omega$ is separating for $\mathcal{M}$.

**Proof.** Faithfulness means $\omega_\Omega(a^*a)=0$ implies $a=0$. But
$$
\omega_\Omega(a^*a)=\langle a\Omega,a\Omega\rangle=\|a\Omega\|^2.
$$
So faithfulness is exactly the statement that $a\Omega=0$ implies $a=0$. $\square$

This is the first point where the course's state-first language matters. A cyclic-separating vector is the Hilbert-space representative of a faithful normal state in a representation large enough for modular theory.

## 2. The Tomita operator

Assume from now on that $\Omega$ is cyclic and separating for $\mathcal{M}$.

**Definition 2.1.** On the dense domain $\mathcal{D}(S_0)=\mathcal{M}\Omega$, define the conjugate-linear operator
$$
S_0(a\Omega)=a^*\Omega,\qquad a\in\mathcal{M}.
$$
This is the **Tomita operator before closure**.

Why is $S_0$ well-defined? If $a\Omega=b\Omega$, then $(a-b)\Omega=0$. Separatingness gives $a=b$, hence $a^*\Omega=b^*\Omega$.

It is worth pausing on how strange this operator is. It is not a Hamiltonian. It is not chosen. It is defined by the algebra and the vector alone: "turn $a$ into $a^*$ on the cyclic orbit of $\Omega$."

> **Physical picture.** Why should "$a \mapsto a^*$ on the orbit of $\Omega$" contain dynamics? Because $S$ is *anti-linear and state-dependent*. In the tracial standard vector, this flip is isometric and $\Delta=1$. For a nontracial faithful vector, the vectors $a\Omega$ and $a^*\Omega$ need not have the same length: in the type-I model of §5, $\|E_{ij}\Omega\|^2=p_j$ while $\|E_{ji}\Omega\|^2=p_i$. The operator $S$ records all such modular weight ratios. Its polar decomposition separates an anti-unitary part $J$, which performs the kinematical mirror operation, from a positive part $\Delta^{1/2}$, which carries the weighting. Imaginary powers of $\Delta$ then form a unitary group. When an independently specified physical dynamics makes the state KMS, these modular weights acquire the usual thermal interpretation; modular theory itself does not require that extra identification.

### 2.1 Closability

Unbounded operators are only useful after closure. The first analytic fact is that $S_0$ closes.

**Proposition 2.2. [Proved.]** The operator $S_0$ is closable.

**Proof.** We must show: if $x_n=a_n\Omega\to 0$ and $S_0x_n=a_n^*\Omega\to\eta$, then $\eta=0$.

Take $b'\in\mathcal{M}'$. Then, using $a_nb'=b'a_n$,
$$
\langle b'\Omega,\eta\rangle
=\lim_n \langle b'\Omega,a_n^*\Omega\rangle
=\lim_n \langle a_nb'\Omega,\Omega\rangle
=\lim_n \langle b'a_n\Omega,\Omega\rangle
=0.
$$
Here $a_n\Omega\to 0$ and $b'$ is bounded. Since $\Omega$ is separating for $\mathcal{M}$, Lemma 1.2 says $\Omega$ is cyclic for $\mathcal{M}'$. Thus $\mathcal{M}'\Omega$ is dense in $\mathcal{H}$, and the last display forces $\eta=0$. $\square$

We write $S$ for the closure of $S_0$.

### 2.2 The adjoint Tomita operator

The commutant has its own Tomita operator. Define, on $\mathcal{M}'\Omega$,
$$
F_0(b'\Omega)=b'^*\Omega,\qquad b'\in\mathcal{M}'.
$$
The same argument shows $F_0$ is closable; call its closure $F$.

**Lemma 2.3. [Sketched — one inclusion proved, converse outlined.]** $F=S^*$ and $S=F^*$.

*Conventions for anti-linear adjoints.* For a densely defined conjugate-linear operator $T$, the adjoint $T^*$ is defined by $\langle T^*\eta, \xi\rangle = \langle T\xi, \eta\rangle$ for all $\xi \in \mathcal{D}(T)$ (note the *un*-conjugated pairing — this is the convention that makes $T^*$ again conjugate-linear).

*Proof of $F \subset S^*$.* For $a \in \mathcal{M}$ and $b' \in \mathcal{M}'$, compute, using $b'^*\Omega \in \mathcal{D}(F_0)$ and commutativity of $a$ with $b'^*$:
$$
\langle S_0(a\Omega),b'\Omega\rangle
=\langle a^*\Omega,b'\Omega\rangle
=\langle b'^*\Omega,a\Omega\rangle
=\langle F_0(b'\Omega),a\Omega\rangle.
$$
This says exactly that every $b'\Omega \in \mathcal{D}(F_0)$ lies in $\mathcal{D}(S_0^*)$ with $S_0^* (b'\Omega) = F_0(b'\Omega)$. Hence $F_0 \subset S_0^* = S^*$, and since $S^*$ is closed, $F \subset S^*$.

*The converse $S^* \subset F$. [Stated only for this direction -- refs: Takesaki Vol. II, ch. VI; Bratteli--Robinson Vol. I, §2.5.]* This is the genuinely technical step. It says that every $\eta\in\mathcal D(S^*)$ can be approximated by vectors $b'_i\Omega$, $b'_i\in\mathcal M'$, simultaneously in Hilbert norm and in the graph norm relevant to $F$. The standard proof uses the $2\times2$ matrix trick together with polar decomposition and bounded spectral cutoffs of an affiliated operator. Establishing that the cutoffs lie in $\mathcal M'$ and converge in graph norm is precisely the part we do not reproduce. With this cited input, $F=S^*$, and $S=F^*$ follows by taking adjoints of closed operators. $\square$

## 3. Polar decomposition: $S=J\Delta^{1/2}$

Since $S$ is a closed densely defined conjugate-linear operator, it has a polar decomposition.

**Definition 3.1.** The **modular operator** is
$$
\Delta:=S^*S.
$$
It is positive, self-adjoint, and generally unbounded. The **modular conjugation** $J$ is the anti-unitary partial isometry in the polar decomposition
$$
S=J\Delta^{1/2}.
$$

In the cyclic-separating case, the partial isometry is anti-unitary on all of $\mathcal{H}$, so $J$ is a conjugation:
$$
J^*=J,\qquad J^2=1.
$$

**Proposition 3.2. [Proved — modulo routine domain checks.]** The modular objects satisfy
$$
J^* = J,\qquad J^2 = 1,\qquad
J\Delta J=\Delta^{-1},
\qquad
S=J\Delta^{1/2},
\qquad
S^*=J\Delta^{-1/2}.
$$

**Proof.** The engine is the identity $S = S^{-1}$: on the core $\mathcal{M}\Omega$ we have $S_0^2(a\Omega) = S_0(a^*\Omega) = a\Omega$, so $S_0$ is a bijection of its domain equal to its own inverse, and this property passes to the closure: $S$ is injective with dense range and $S^{-1} = S$ as closed operators.

*Step 1: $J\Delta^{1/2}J^* = \Delta^{-1/2}$.* Invert the polar decomposition: $S^{-1} = (J\Delta^{1/2})^{-1} = \Delta^{-1/2}J^{-1} = \Delta^{-1/2}J^*$ (for an anti-unitary, $J^{-1} = J^*$). Rewrite by pulling $J^*$ through:
$$
S = S^{-1} = \Delta^{-1/2}J^* = J^*\,\big(J\Delta^{-1/2}J^*\big).
$$
The operator $J\Delta^{-1/2}J^*$ is *positive self-adjoint*: for an anti-unitary $J$, $\langle x, J\Delta^{-1/2}J^*x\rangle = \langle \Delta^{-1/2}J^*x, J^*x\rangle \ge 0$ (anti-unitarity reverses inner products, $\langle Jx,Jy\rangle = \langle y,x\rangle$, which is what makes the chain work). So $S = J^*(J\Delta^{-1/2}J^*)$ exhibits a *second* polar decomposition of $S$: anti-unitary times positive.

*Step 2: uniqueness of polar decomposition.* The polar decomposition of a closed densely defined (conjugate-linear) operator is unique. Comparing $S = J\Delta^{1/2} = J^*(J\Delta^{-1/2}J^*)$:
$$
J = J^*, \qquad \Delta^{1/2} = J\Delta^{-1/2}J^* = J\Delta^{-1/2}J.
$$
From $J = J^*$ and anti-unitarity $J^*J = 1$ we get $J^2 = 1$: the modular conjugation is an involution. Squaring the second relation (or applying the functional calculus, which commutes with conjugation by the involution $J$ up to complex conjugation of the function) gives
$$
J\Delta J = \Delta^{-1}, \qquad\text{and more generally}\qquad J f(\Delta) J = \bar f(\Delta^{-1}).
$$

*Step 3: the adjoint.* $S^* = (J\Delta^{1/2})^* = \Delta^{1/2}J^* = \Delta^{1/2}J = J(J\Delta^{1/2}J) = J\Delta^{-1/2}$, using Step 2. This also re-derives Lemma 2.3's identification $F = S^* = J\Delta^{-1/2}$: the commutant's Tomita operator has the *inverse* modular weighting, as the system$\leftrightarrow$mirror symmetry demands. $\square$

The relation $J\Delta J=\Delta^{-1}$ is the operator-theoretic shadow of the formal identity $S_0^2=1$ on $\mathcal{M}\Omega$. It should not be read as saying that $\Delta$ is bounded; $\Delta^{-1}$ is usually unbounded too, and the identities are identities of closed operators on their proper domains.

> **Physical picture.** The polar decomposition splits the state-flip $S$ into a mirror operation and a modular weighting. $J$ is the *mirror*: an anti-unitary involution exchanging $\mathcal{M}$ with its commutant—in the type-I model it swaps the two tensor factors; for a neutral bosonic Rindler-wedge algebra it becomes the CPT-plus-rotation wedge reflection (Bisognano–Wichmann, Week 10). In the type-I model, the spectrum of $\Delta$ consists of probability ratios; in general it is modular spectral data, not a list of density-matrix weights. The identity $J\Delta J=\Delta^{-1}$ says that the commutant carries the inverse modular weighting. The two-sided-black-hole interpretation used in Semester II is a further geometric realization of this exact operator identity.

## 4. Tomita's theorem

Everything so far can be checked with standard unbounded-operator arguments. The hard theorem is the next one.

**Theorem 4.1 (Tomita-Takesaki). [Stated only — refs: B-R Vol. I §2.5; Takesaki Vol. II Ch. VI; Kadison–Ringrose Vol. II Ch. 9.]** Let $\mathcal{M}$ be a von Neumann algebra on $\mathcal{H}$ and let $\Omega$ be cyclic and separating for $\mathcal{M}$. With $S=J\Delta^{1/2}$ as above,
$$
J\mathcal{M}J=\mathcal{M}',
$$
and for every $t\in\mathbb{R}$,
$$
\Delta^{-it}\,\mathcal{M}\,\Delta^{it}=\mathcal{M}.
$$
Hence
$$
\sigma_t^\Omega(a)\;:=\;\Delta^{-it}\,a\,\Delta^{it},\qquad a\in\mathcal{M},
$$
defines a one-parameter automorphism group of $\mathcal{M}$.

This $\sigma^\Omega$ is the **modular automorphism group** of $(\mathcal{M},\Omega)$.

> **Physical picture.** The two assertions of the theorem say that the modular data of $(\mathcal M,\Omega)$ are algebraically self-consistent. The relation $\Delta^{-it}\mathcal{M}\Delta^{it}=\mathcal{M}$ says modular evolution preserves the algebra. The relation $J\mathcal{M}J=\mathcal{M}'$ gives a conjugate-linear identification with the commutant—not, for a generic spatial region, an automatic identification with a geometric complement. Both facts are invisible from the definition of $S$ and require the hard analytic theorem. Thermal and geometric interpretations become exact only when the additional KMS or Bisognano–Wichmann input is present.

**Sign convention.** We use $\sigma^\Omega_t = \mathrm{Ad}(\Delta^{-it})$ so that $\omega$ is KMS at $\beta = +1$ in the upper-strip convention of Week 4 Definition 2.1. The opposite convention $\sigma_t = \mathrm{Ad}(\Delta^{+it})$ also appears in the literature (Bratteli–Robinson Vol. II) and gives KMS at $\beta = -1$. The two are related by $t \to -t$ and describe the same automorphism group running in opposite directions. Our convention matches Witten 1803.04993, where the modular Hamiltonian $K = -\log\rho$ generates the flow via $\sigma_t = \mathrm{Ad}(e^{itK}) = \mathrm{Ad}(\Delta^{-it})$.

We will not prove Tomita's theorem in full. The proof is one of the great analytic arguments in operator algebra theory. What we will do, now, is compute it in the finite-dimensional type-I model where every domain issue disappears and the theorem becomes a density-matrix calculation.

## 5. The type-I model: modular theory as density-matrix algebra

Let $\mathcal{H}_A$ and $\mathcal{H}_B$ be $n$-dimensional Hilbert spaces. Let
$$
\mathcal{M}=\mathcal{B}(\mathcal{H}_A)\otimes 1
\subset
\mathcal{B}(\mathcal{H}_A\otimes\mathcal{H}_B).
$$
Choose a vector in Schmidt form
$$
\Omega=\sum_{i=1}^n \sqrt{p_i}\, e_i\otimes f_i,
\qquad
p_i>0,\qquad \sum_i p_i=1.
$$
The strict positivity $p_i>0$ is exactly the cyclic-separating condition in this finite-dimensional model.

Define
$$
\rho_A=\sum_i p_i |e_i\rangle\langle e_i|,
\qquad
\rho_B=\sum_i p_i |f_i\rangle\langle f_i|.
$$

### 5.1 Cyclic and separating in the model

The vectors
$$
(|e_i\rangle\langle e_j|\otimes 1)\Omega
=\sqrt{p_j}\, e_i\otimes f_j
$$
span $\mathcal{H}_A\otimes\mathcal{H}_B$, since all $p_j>0$. Thus $\Omega$ is cyclic for $\mathcal{M}$.

If $(a\otimes 1)\Omega=0$, then
$$
\sum_j \sqrt{p_j}\, ae_j\otimes f_j=0,
$$
so $ae_j=0$ for every $j$, hence $a=0$. Thus $\Omega$ is separating.

### 5.2 Computing $S$, $\Delta$, and $J$

Set
$$
E_{ij}=|e_i\rangle\langle e_j|,\qquad
x_{ij}:=(E_{ij}\otimes 1)\Omega=\sqrt{p_j}\, e_i\otimes f_j.
$$
Then
$$
Sx_{ij}
=S(E_{ij}\otimes 1)\Omega
=(E_{ji}\otimes 1)\Omega
=\sqrt{p_i}\, e_j\otimes f_i.
$$

Define the anti-unitary $J$ by
$$
J(e_i\otimes f_j)=e_j\otimes f_i
$$
with complex conjugation in the displayed bases. Define
$$
\Delta=\rho_A\otimes\rho_B^{-1}.
$$
Then
$$
\Delta(e_i\otimes f_j)=\frac{p_i}{p_j}\, e_i\otimes f_j,
$$
and hence
$$
J\Delta^{1/2}x_{ij}
=J\left(\sqrt{p_j}\sqrt{\frac{p_i}{p_j}}\,e_i\otimes f_j\right)
=\sqrt{p_i}\, e_j\otimes f_i
=Sx_{ij}.
$$

So in this model,
$$
\boxed{\Delta=\rho_A\otimes\rho_B^{-1}},
\qquad
\boxed{J(e_i\otimes f_j)=e_j\otimes f_i\text{, anti-linearly}.}
$$

> **Physical picture.** Read the eigenvalue formula $\Delta\,(e_i \otimes f_j) = (p_i/p_j)\, e_i\otimes f_j$: the modular operator weighs each “transition” $j\to i$ by a ratio of state probabilities. In a factor, the spectral data that survive after intersecting over faithful normal states enter Connes' $S$-invariant; the spectrum of this one finite-dimensional $\Delta$ is only the model, not yet the invariant. Note also what $\Delta$ is *not*: it is not $\rho_A$ alone. The factor $\rho_B^{-1}$ on the mirror side makes $\Delta\Omega=\Omega$. Consequently the full modular Hamiltonian is a difference,
> $$
> -\log\Delta=(-\log\rho_A)\otimes1-1\otimes(-\log\rho_B),
> $$
> anticipating the opposite boost orientations of the two Rindler wedges.

### 5.3 The modular flow

For $a\in\mathcal{B}(\mathcal{H}_A)$, the modular automorphism (Tomita-Takesaki convention of §4) is
$$
\begin{aligned}
\sigma_t^\Omega(a\otimes 1)
&=\Delta^{-it}(a\otimes 1)\Delta^{it}\\
&=(\rho_A^{-it}a\rho_A^{it})\otimes 1.
\end{aligned}
$$
The modular flow is inner in this finite-dimensional type-I model and is generated by the **modular Hamiltonian**
$$
K_A:=-\log\rho_A.
$$
Indeed, $\rho_A^{-it}=e^{itK_A}$, so $\sigma_t^\Omega(a\otimes 1) = (e^{itK_A} a\, e^{-itK_A}) \otimes 1$ — Heisenberg evolution generated by $K_A$.

This is the density-matrix formula that physicists know. Tomita-Takesaki is the theorem that the same construction survives when $\rho_A$ no longer exists as a trace-class density matrix.

### 5.4 The commutant formula

For $a\otimes 1\in\mathcal{M}$,
$$
J(a\otimes 1)J=1\otimes \overline{a},
$$
where $\overline{a}$ is the matrix of $a$ in the Schmidt bases, transported from $\mathcal{H}_A$ to $\mathcal{H}_B$. Hence
$$
J\mathcal{M}J=1\otimes\mathcal{B}(\mathcal{H}_B)=\mathcal{M}'.
$$

This proves Tomita's commutant theorem in the type-I model.

## 6. Worked computation: a thermal qubit

Let
$$
H=\begin{pmatrix}0&0\\0&E\end{pmatrix},
\qquad
\rho_\beta=\frac{e^{-\beta H}}{Z}
=\frac{1}{1+e^{-\beta E}}
\begin{pmatrix}
1&0\\0&e^{-\beta E}
\end{pmatrix}.
$$
Purify $\rho_\beta$ on $\mathbb{C}^2\otimes\mathbb{C}^2$:
$$
\Omega_\beta
=\sqrt{p_0}\, e_0\otimes f_0+\sqrt{p_1}\, e_1\otimes f_1,
\qquad
p_0=\frac{1}{Z},\quad p_1=\frac{e^{-\beta E}}{Z}.
$$
For $\mathcal{M}=M_2(\mathbb{C})\otimes 1$,
$$
\Delta=\rho_\beta\otimes\rho_\beta^{-1},
$$
and the modular flow on $\mathcal{M}$ is
$$
\sigma_t^\beta(a)=\rho_\beta^{-it}\,a\,\rho_\beta^{it}.
$$

Since $\rho_\beta^{-it}=Z^{it}e^{i\beta tH}$, the scalar $Z^{it}$ cancels:
$$
\boxed{\sigma_t^\beta(a)=e^{i\beta tH}\,a\, e^{-i\beta tH}.}
$$
With our upper-strip KMS convention of Week 4, this modular flow is KMS at $\beta=1$. Relative to the physical Heisenberg flow $a_s=e^{isH}ae^{-isH}$, **modular time is the inverse-temperature rescaling of physical time**: $\sigma_t^\beta = \alpha_{\beta t}$ where $\alpha_s = \mathrm{Ad}(e^{isH})$.

For the matrix unit $E_{01}=|e_0\rangle\langle e_1|$,
$$
\sigma_t^\beta(E_{01})
=e^{-i\beta Et}E_{01},
\qquad
\sigma_t^\beta(E_{10})
=e^{+i\beta Et}E_{10}.
$$
The modular operator detects the energy gap through phases.

## 7. The tracial case

If $\rho_A=\frac{1}{n}1$, then
$$
\Delta=1,\qquad \sigma_t=\mathrm{id}.
$$
The modular conjugation still exchanges the two tensor factors, but the modular flow is trivial. This is the finite-dimensional version of the II$_1$ trace example: traces have no preferred modular time.

The contrast is the lesson:
- non-tracial faithful states produce non-trivial modular flow;
- tracial states produce trivial modular flow;
- type III algebras have no trace, so non-trivial modular dynamics is not an optional feature but part of the basic geometry of states.

## 8. What to take away

- **Proved:** cyclic for $\mathcal{M}$ is the same as separating for $\mathcal{M}'$, and faithful vector states are exactly separating vector states.
- **Proved:** the Tomita operator $S_0(a\Omega)=a^*\Omega$ is well-defined and closable when $\Omega$ is cyclic and separating.
- **Model proof:** in the type-I bipartite model, $\Delta=\rho_A\otimes\rho_B^{-1}$, $J$ exchanges the two sides, and $\sigma_t^\Omega = \mathrm{Ad}(\Delta^{-it})$ acts as Heisenberg evolution with modular Hamiltonian $K = -\log\rho_A$.
- **Stated only:** the full Tomita-Takesaki theorem says $J\mathcal{M}J=\mathcal{M}'$ and $\Delta^{-it}\mathcal{M}\Delta^{it}=\mathcal{M}$.
- **Physical interpretation:** the modular Hamiltonian $K=-\log\rho$ in finite dimensions is the shadow of $\Delta$; in type III there is no density matrix relative to a canonical trace, but $\Delta$ remains.

## 9. Looking ahead

Week 6 turns $\Delta$ into dynamics. We will prove in the finite-dimensional model, and state in full generality, that the vector state $\omega_\Omega$ is KMS at $\beta=1$ for the modular flow $\sigma_t^\Omega(a)=\Delta^{-it}a\Delta^{it}$. This is where the KMS condition of Week 4 and the Tomita operator of Week 5 lock together.

## 10. Problem set

**Core problems.**

**1. Cyclic versus separating.** Fill in the details of Lemma 1.2. In particular, prove carefully that $K=\overline{\mathcal{M}\Omega}$ reduces $\mathcal{M}$ and that the projection onto $K$ lies in $\mathcal{M}'$.

**2. Faithfulness.** Let $\omega_\Omega(a)=\langle\Omega,a\Omega\rangle$. Prove that $\omega_\Omega$ is faithful iff $\Omega$ is separating.

**3. Closability of $S_0$.** Reproduce the proof of Proposition 2.2. Where is cyclicity used? Where is separatingness used?

**4. Type-I modular operator.** For
$$
\Omega=\sum_{i=1}^n\sqrt{p_i}\,e_i\otimes f_i,\qquad p_i>0,
$$
show directly that
$$
\Delta(e_i\otimes f_j)=\frac{p_i}{p_j}e_i\otimes f_j.
$$

**5. Thermal qubit.** With $H=\mathrm{diag}(0,E)$ and $\rho_\beta=e^{-\beta H}/Z$, compute $\sigma_t^\beta(\sigma_x)$ and $\sigma_t^\beta(\sigma_y)$ in our convention.

**Starred problems.**

**6\*. The commutant in the type-I model.** Prove that $J(a\otimes 1)J=1\otimes\overline{a}$ and hence $J\mathcal{M}J=\mathcal{M}'$.

**7\*. Domains.** Let $S$ be the closure of $S_0$. Show that $\mathcal{M}\Omega$ is a core for $S$. Then explain why domain control matters when $\Delta$ is unbounded.

**8\*. The tracial GNS case.** Let $\mathcal{M}$ be a finite factor with faithful normal trace $\tau$, acting on $L^2(\mathcal{M},\tau)$ by left multiplication. Let $\Omega=[1]$. Show that
$$
S[a]=[a^*],\qquad \Delta=1,
$$
and identify $J\mathcal{M}J$ with the right multiplication algebra.

**9\*. Modular data cheat sheet.** Build a one-page table comparing $(S,J,\Delta,\sigma_t)$ in four examples: $M_n(\mathbb{C})$ with a non-tracial state, $M_n(\mathbb{C})$ with the trace, a II$_1$ factor with trace, and the Powers factor preview from Week 4.

**10\*. Reading bridge.** Read Witten's finite-dimensional modular discussion in arXiv:1803.04993 §3 and reproduce it in the notation of this note. Flag every place where the finite-dimensional argument uses a density matrix.

## Self-study answer checkpoints

The five core problems should be reproducible without outside sources. The starred domain, commutant, and reading problems remain guided extensions; compare them with the cited operator-theory references.

1. **Cyclic versus separating.** For $K=\overline{\mathcal M\Omega}$, invariance under both $a$ and $a^*$ makes $K$ reducing for every $a\in\mathcal M$. Hence its orthogonal projection $P_K$ commutes with $\mathcal M$, so $P_K\in\mathcal M'$. If $\Omega$ is separating for $\mathcal M'$, $(1-P_K)\Omega=0$ forces $P_K=1$.

2. **Faithfulness.** The decisive identity is
   $$
   \omega_\Omega(a^*a)=\|a\Omega\|^2.
   $$
   Thus $\omega_\Omega$ is faithful exactly when $a\Omega=0$ implies $a=0$, which is separatingness.

3. **Closability.** If $a_n\Omega\to0$ and $a_n^*\Omega\to\eta$, commute $a_n$ through vectors $b'\Omega$ with $b'\in\mathcal M'$ to show $\langle b'\Omega,\eta\rangle=0$. Separatingness for $\mathcal M$ makes $\Omega$ cyclic for $\mathcal M'$, so $\eta=0$. Cyclicity for $\mathcal M$ makes the original Tomita domain dense; separatingness makes $S_0(a\Omega)=a^*\Omega$ well defined and supplies the dense commutant orbit used in the closability test.

4. **Type-I modular spectrum.** On the matrix-unit vectors,
   $$
   \Delta(e_i\otimes f_j)=\frac{p_i}{p_j}\,e_i\otimes f_j.
   $$
   A useful check is $\Delta\Omega=\Omega$: only the $i=j$ terms occur in $\Omega$.

5. **Thermal qubit.** Put $\theta=\beta Et$. In the course convention,
   $$
   \sigma_t^\beta(\sigma_x)
   =\cos\theta\,\sigma_x+\sin\theta\,\sigma_y,
   \qquad
   \sigma_t^\beta(\sigma_y)
   =\cos\theta\,\sigma_y-\sin\theta\,\sigma_x.
   $$
   These are the physical Heisenberg rotations evaluated at time $\beta t$.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block B. Last revised 2026-08-24.*
