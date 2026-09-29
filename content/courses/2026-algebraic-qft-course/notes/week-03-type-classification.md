---
title: "Week 3 — Type Classification (I, II, III) and Projections"
type: lecture-notes
course: syllabus
semester: 1
week: 3
block: A
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Week 2 (von Neumann algebras, bicommutant)
modified: 2026-09-29
---

# Week 3 — Type Classification (I, II, III) and Projections

> *Last week we identified von Neumann algebras as those \*-subalgebras of $\mathcal{B}(\mathcal{H})$ closed in WOT/SOT, with factors as the indecomposable building blocks. We now ask for their first structural division. The Murray–von Neumann classification sorts factors into three **types**—I, II, and III—but does not classify all factors up to isomorphism inside a type. Type I is the "ordinary" world of bounded operators on a Hilbert space. Type II admits a trace and is the world of noncommutative integration. Type III admits no nonzero normal semifinite trace and is the type found for broad classes of local QFT algebras under the hypotheses made explicit in Block C. This loss of trace motivates the rest of the course: Tomita–Takesaki theory, relative entropy, and the [[crossed-product-construction|crossed product]].*

### How to use this chapter

- **In class:** let projection comparison do the conceptual work. Build the type-I/II/III table only after finite, infinite, minimal, and equivalent projections have been tested in examples.
- **For self-study:** keep a running ledger with four columns—minimal projections, finite projections, available trace, and canonical example. Use it to reconstruct the classification rather than memorize names.
- **Instructor checkpoint:** require a trace-based proof that type III is not semifinite, and keep Murray–von Neumann's projection theory distinct from Connes' later III$_\lambda$ refinement and property-Gamma history.

## 0. Reading

**Primary:**
- Bratteli & Robinson Vol. I, §2.6 (type classification).
- Murphy, *C\*-algebras and Operator Theory*, ch. 5.

**Secondary, for the curious:**
- Murray & von Neumann, "On Rings of Operators" I (1936), the original classification.
- Takesaki Vol. I, ch. V.
- Connes, *Noncommutative Geometry*, ch. V.

### Proof-status legend

The classification theory is technically heavy; in a one-week treatment we cannot prove most of the structural results. Each labeled result in this note carries one of the following tags so students know what level of justification is on offer:

- **[Proved.]** Full proof given in the notes.
- **[Sketched.]** Key idea given; details suppressed.
- **[Stated only — refs.]** Black-box statement with references for the proof.
- **[Example-only.]** Verified in a specific (usually finite-dimensional) case; the general statement is by analogy.
- **[Hypothesis-explicit.]** Stated with the technical assumptions required, even if the proof is in references.

This labeling carries through Weeks 4–15 and is codified in the note-quality template and [[courses/2026-algebraic-qft-course/conventions|conventions.md]]. Weeks 1–2 use the same labels retroactively.

## 1. The order structure on projections

A *projection* in a vN algebra $\mathcal{M}$ is a self-adjoint idempotent: $p = p^* = p^2$. Projections are the "characteristic functions" of vN algebra theory: they correspond to closed subspaces (their range) and to yes/no questions about quantum states.

The set $\mathrm{Proj}(\mathcal{M})$ of projections in $\mathcal{M}$ is a *complete lattice*: any family $\{p_\alpha\}$ has a supremum $\bigvee_\alpha p_\alpha$ (the projection onto the closed span of their ranges) and an infimum $\bigwedge_\alpha p_\alpha$ (the projection onto the intersection of their ranges). Both are again in $\mathcal{M}$. For the supremum, direct the finite subsets $F$ of indices by inclusion and form the finite joins $p_F=\bigvee_{\alpha\in F}p_\alpha$, which belong to $\mathcal M$. The increasing net $p_F$ converges strongly to $\bigvee_\alpha p_\alpha$. Infima follow from complements. No finite-rank projection is being assumed—type II and III factors may have none.

### 1.1 Murray–von Neumann equivalence

**Definition 1.1 (Partial isometry).** An element $v \in \mathcal{M}$ is a *partial isometry* if $v^* v$ is a projection. Equivalently, $v v^*$ is a projection; equivalently, $v v^* v = v$.

The two projections $v^* v$ (the *initial projection*) and $v v^*$ (the *final projection*) are the projections onto the kernel-complement and the range of $v$, respectively. The partial isometry $v$ implements an isometry from $\mathrm{ran}(v^* v) \subset \mathcal{H}$ to $\mathrm{ran}(v v^*) \subset \mathcal{H}$.

**Definition 1.2 (Murray–vN equivalence).** Two projections $p, q \in \mathcal{M}$ are *Murray–vN equivalent in $\mathcal{M}$*, written $p \sim_{\mathcal{M}} q$, if there exists a partial isometry $v \in \mathcal{M}$ with $v^* v = p$ and $v v^* = q$.

This equivalence relation captures what it means for two projections to "have the same dimension" *as seen by* $\mathcal{M}$. A partial isometry $v \in \mathcal{M}$ implements an isomorphism between the ranges of $p$ and $q$, but only one that lives inside the algebra. If two projections are equivalent in $\mathcal{B}(\mathcal{H})$ but not in $\mathcal{M}$, then $\mathcal{M}$ "doesn't see" their equivalence, and we treat them as inequivalent.

> **Physical picture.** Murray–vN equivalence is a *resource-theoretic* notion of "same size": two yes/no questions $p$ and $q$ count as equally big precisely when an operation *available to the observer* (an element of $\mathcal{M}$) converts one into the other. The restriction "$v \in \mathcal{M}$" is the physics. An observer confined to a subsystem, or to a spacetime region, cannot use global unitaries to compare subspaces; she can only use her own operations. The same pair of projections can therefore be "equally large" for a global observer ($\mathcal{B}(\mathcal{H})$) and incomparable for a local one (Example 1.4). The entire type classification below is, in this sense, a classification of *what notions of size are available to a constrained observer* — and the punchline of the course is that the observer confined to a bounded spacetime region (type III) has the most degenerate size notion possible: everything nonzero is infinite.

**Example 1.3.** In $\mathcal{M} = M_n(\mathbb{C})$, two projections $p, q$ are Murray–vN equivalent iff they have the same rank (this is a standard linear-algebra fact). The partial isometry can be constructed as a "rotation" between the two ranges.

**Example 1.4.** In a *non-factor* like $\mathcal{B}(\mathcal{H}_1) \oplus \mathcal{B}(\mathcal{H}_2)$, two rank-1 projections — one in each summand — are *not* Murray–vN equivalent because no partial isometry connects them: every operator in the algebra is block-diagonal. This shows that the equivalence depends on the algebra, not just on the Hilbert-space ranks.

### 1.2 Order on projections

**Definition 1.5.** $p \preceq_{\mathcal{M}} q$ if $p \sim_{\mathcal{M}} p'$ for some projection $p' \le q$ (i.e., $p'$ is dominated by $q$ in the usual sense $p' = qp'$).

This is the order on equivalence classes: $[p] \le [q]$ iff $p$ is equivalent to a subprojection of $q$.

**Theorem 1.6 (Comparison theorem for factors). [Sketched.]** *In a factor $\mathcal{M}$, any two projections $p, q$ are comparable: $p \preceq q$ or $q \preceq p$.*

This is one of the foundational results of Murray–vN: in a factor, the order on equivalence classes of projections is a *total* order. In a non-factor (e.g., $\mathcal{B}(\mathcal{H}_1) \oplus \mathcal{B}(\mathcal{H}_2)$), projections supported on different summands are incomparable.

**Proof sketch.** Use Zorn's lemma to find a maximal family $\{p_\alpha\}_{\alpha \in A}$ of pairwise orthogonal subprojections of $p$, each Murray–vN equivalent to a subprojection of $q$. Set $p' := \sum_\alpha p_\alpha \le p$. By maximality, the "remaining" projection $p - p'$ has no equivalent subprojection in $q$. Use that $\mathcal{M}$ is a factor to show that this forces either $p - p' = 0$ (so $p \preceq q$) or $q$ is "exhausted" by the construction (so $q \preceq p$). The argument requires care because of the choice of partial isometries; we omit the details. $\square$

The comparison theorem is what makes "dimension" of projections (relative to the algebra) a *totally ordered* invariant in a factor.

## 2. Finite versus infinite projections

**Definition 2.1.** A non-zero projection $p \in \mathcal{M}$ is *finite* if for all $q \in \mathcal{M}$ with $q \le p$ and $q \sim_{\mathcal{M}} p$, we have $q = p$. Equivalently: $p$ is not Murray–vN equivalent to a strict subprojection of itself.

This is the algebraic generalization of "finite-dimensional subspace." A projection is *infinite* if it is equivalent to a strict subprojection of itself — Hilbert's hotel.

**Definition 2.2.** A projection $p$ is *minimal* if $0 < q \le p$ implies $q = 0$ or $q = p$. Minimal projections are the "atoms" of $\mathrm{Proj}(\mathcal{M})$.

**Example 2.3.** In $\mathcal{B}(\mathcal{H})$:
- *Finite* projections = projections of finite rank.
- *Infinite* projections = projections of infinite rank (e.g., the identity if $\dim\mathcal{H} = \infty$).
- *Minimal* projections = rank-1 projections, of the form $|\xi\rangle\langle\xi|$ for unit $\xi \in \mathcal{H}$.

In $\mathcal{B}(\mathcal{H})$, the projections form a "discrete" structure: ranks are integers, finite ranks are finite, infinite ranks are infinite. This will be the case in *type I* algebras generally.

**Example 2.4 (Hilbert's hotel).** In $\mathcal{B}(\ell^2)$, the projection $1$ (onto all of $\ell^2$) is equivalent to the projection $p$ onto $\{e_2, e_3, \ldots\}$. The shift $S e_n = e_{n+1}$ is a partial isometry with $S^* S = 1$ and $S S^* = p$. So $1 \sim p < 1$, demonstrating that $1$ is infinite in $\mathcal{B}(\ell^2)$.

**Example 2.5 (Type II oddity).** In a type II$_1$ factor $\mathcal{M}$, *every* projection, including the identity, is finite, but the projection lattice is not discrete — between any two projections $p_1 < p_2$ there is a continuum of projections (parameterized by trace value). This is the "continuous-dimension" structure that gives type II its name.

## 3. The Murray-von Neumann classification

**Theorem 3.1 (Murray-von Neumann 1936). [Stated only — refs: Murray–vN, Ann. of Math. 37 (1936) 116–229; Takesaki Vol. I §V.1.]** *A factor $\mathcal{M}$ falls into exactly one of three types:*

- *Type I: $\mathcal{M}$ contains a non-zero minimal projection.*
- *Type II: $\mathcal{M}$ contains no minimal projection but contains a non-zero finite projection.*
    - *Type II$_1$ if $1_{\mathcal{M}}$ is finite.*
    - *Type II$_\infty$ if $1_{\mathcal{M}}$ is infinite.*
- *Type III: every non-zero projection in $\mathcal{M}$ is infinite.*

The classification is exhaustive and exclusive: every factor is in exactly one type.

> **Physical picture.** Read the trichotomy as three answers to the question *"what is the smallest thing the observer can resolve?"* Type I: there is an atom—a minimal projection, a finest-grained yes/no question. Type II: there is no atom—questions can be subdivided forever—but a trace still calibrates their continuous size. Type III: there are no atoms and no faithful normal semifinite calibration; every nonzero projection is equivalent to a proper part of itself. This does **not** mean that equal decompositions are impossible—proper infiniteness supplies many such decompositions. It means that the finite dimension-counting intuition has collapsed. In local QFT, combined with a cyclic-separating vacuum, this algebraic structure is the setting in which sharp tensor factors and intrinsic reduced density matrices fail.

### 3.1 Type I factors

**Theorem 3.2. [Sketched.]** *Every type I factor is isomorphic to $\mathcal{B}(\mathcal{K})$ for some Hilbert space $\mathcal{K}$. The isomorphism class is determined by $\dim\mathcal{K}$:*
- *Type I$_n$ for $n < \infty$: $\mathcal{M} \cong M_n(\mathbb{C})$.*
- *Type I$_\infty$: $\mathcal{M}\cong\mathcal B(\mathcal K)$ with $\dim\mathcal K$ infinite; in the separable case, $\mathcal K\cong\ell^2(\mathbb N)$.*

**Sketch of proof.** Let $\mathcal{M}$ be a type I factor on $\mathcal{H}$, and pick a minimal projection $p_0 \in \mathcal{M}$ (exists by Theorem 3.1). Since $\mathcal{M}$ is a factor, the comparison theorem gives a family of pairwise orthogonal projections $\{p_\alpha\}$, all equivalent to $p_0$, with $\sum_\alpha p_\alpha = 1$. Let $|A|$ be the cardinality of this family.

Pick partial isometries $v_\alpha$ with $v_\alpha^* v_\alpha = p_0$ and $v_\alpha v_\alpha^* = p_\alpha$. Then the $v_\alpha v_\beta^*$ form a system of "matrix units" satisfying $v_{\alpha\beta} v_{\gamma\delta} = \delta_{\beta\gamma} v_{\alpha\delta}$. The vN algebra they generate is isomorphic to $\mathcal{B}(\ell^2(A))$. Plus, the original $\mathcal{M}$ contains $\{v_{\alpha\beta}\}_{\alpha,\beta}$ as generators (using minimality of $p_0$), so $\mathcal{M} = \{v_{\alpha\beta}\}'' \cong \mathcal{B}(\ell^2(A))$. $\square$

This is the "rigidity" of type I: there is essentially only one type I factor of each cardinality, and they are all the standard $\mathcal{B}(\mathcal{H})$.

### 3.2 Type II$_1$ factors

**Theorem 3.3 (Trace existence on type II$_1$). [Stated only — refs: Murray–vN 1937; Takesaki Vol. I §V.2.]** *Every type II$_1$ factor $\mathcal{M}$ admits a unique normalized faithful normal trace $\tau : \mathcal{M} \to \mathbb{C}$, characterized by $\tau(1) = 1$ and $\tau(ab) = \tau(ba)$ for all $a, b \in \mathcal{M}$.*

The uniqueness is striking: the trace is *intrinsic* to the algebra, not requiring any external data. This contrasts with $\mathcal{B}(\mathcal{H})$ for infinite-dimensional $\mathcal H$, where the standard trace is only an extended-valued semifinite weight and is infinite on the identity.

The trace gives a notion of "dimension" for projections that takes *continuous* values in $[0, 1]$: for a projection $p \in \mathcal{M}$, the number $\tau(p) \in [0,1]$ is the "fraction of the algebra" that $p$ occupies.

**Lemma 3.4 (Continuous-dimension). [Sketched.]** *In a type II$_1$ factor, the values $\{\tau(p) : p \in \mathrm{Proj}(\mathcal{M})\}$ fill the entire interval $[0, 1]$.*

**Sketch.** Using the comparison theorem and divisibility properties: for any $p$ with $\tau(p) > 0$, one can find $q \le p$ with $\tau(q) = \tau(p)/2$ (split $p$ into two equivalent halves). Iterating gives a dense set of dyadic rationals; SOT-limits of projections give the continuous interval. $\square$

This is the source of the name "noncommutative integration": type II$_1$ algebras are like "spaces of bounded measurable functions" with a continuous probability measure, where projections play the role of indicator functions of measurable sets.

> **Physical picture.** A type II$_1$ factor is a quantum system in which "dimension of a subspace" has become a continuous quantity, the way "number of microstates" becomes continuous in classical statistical mechanics when one passes from counting to phase-space volume. There is no smallest subspace — no qubit you can point to — but there is a perfectly good answer to "what fraction of the system is this?" In Block D this is exactly what makes the crossed-product algebras of gravity tractable: a type II algebra supports density operators and entropies *relative to the trace* ($\rho$ with $\omega = \tau(\rho\,\cdot)$, $S = -\tau(\rho\log\rho)$), even though a diffuse type-II factor has no **normal** pure states. Singular pure states may still exist when the factor is viewed as a C\*-algebra. Entropy differences can then be finite and meaningful under the hypotheses developed later, while absolute state counting still is not — which matches the physical situation of generalized entropy in gravity, where regulated differences, rather than a bare local entropy, are the controlled quantities.

### 3.3 Type II$_\infty$ factors

**Intrinsic definition.** A factor $\mathcal{M}$ is *type II$_\infty$* if it is type II (no minimal projection but has a non-zero finite projection, per Theorem 3.1) and the identity $1_{\mathcal{M}}$ is *infinite*. Equivalently, $\mathcal{M}$ has no minimal projections and admits a faithful normal *semifinite* trace $\tau$ — defined on a dense \*-ideal and satisfying $\tau(ab) = \tau(ba)$ where defined — but no *normalized* trace. The condition on minimal projections is needed: $\mathcal B(\mathcal H)$ with $\dim\mathcal H=\infty$ also carries a faithful normal semifinite trace, $\operatorname{Tr}$, and no normalized one, but it is type I$_\infty$.

The trace takes projection-values in the full extended interval $[0, \infty]$.

**Theorem 3.5 (Structure theorem). [Stated only — separability assumed; refs: Murray–vN; Takesaki Vol. I §V.1.]** *Every type II$_\infty$ factor on a separable Hilbert space is isomorphic to $\mathcal{N} \otimes \mathcal{B}(\ell^2)$ for some type II$_1$ factor $\mathcal{N}$.*

The II$_1$ factor $\mathcal N$ depends on the II$_\infty$ factor and need not be the hyperfinite factor $\mathcal R$ of §5.2. The hyperfinite case $\mathcal R\otimes\mathcal B(\ell^2)$ is the one that reappears in Block D as the continuous core of the hyperfinite type III$_1$ factor.

The structure theorem is what justifies the slogan "type II$_\infty$ = II$_1$ tensor type I$_\infty$." But the *type* is intrinsic to the algebra (a property of its projection lattice and trace), and we should be careful to distinguish the intrinsic definition from the structural decomposition. The decomposition is a theorem; the intrinsic property is the definition.

### 3.4 Type III factors

**Theorem 3.6. [Stated only — refs as Theorem 4.1 below.]** *A factor $\mathcal M$ is type III iff it admits no faithful normal semifinite trace, iff every non-zero projection in $\mathcal M$ is infinite, iff for every projection $p\neq0$ there is a partial isometry $v\in\mathcal M$ with $v^*v=p$ and $vv^*$ a strict subprojection of $p$.*

The three characterizations are equivalent and reinforce one another. The operational consequences:
- No **intrinsic** density matrices: there is no canonical semifinite trace $\tau$ on the algebra relative to which a normal state could be written as $\omega(a)=\tau(\rho a)$. In a particular concrete representation, a normal functional may still be represented by an ambient trace-class operator; that representation is neither intrinsic nor a reduced density matrix for a tensor factor.
- No **intrinsic local** von Neumann entropy of the form $S=-\tau(\rho\log\rho)$, because neither the local trace $\tau$ nor its density $\rho$ exists inside the factor.
- Different entropy notions: [[week-07-connes-cocycle-and-relative-entropy|Araki–Uhlmann relative entropy]] (Week 7) is the substitute that survives in type III.

Type III factors are *bizarre* by standard QM intuition. Yet they are the typical case in QFT. More precisely, phase-space and split/approximation hypotheses supply the hyperfinite side; an independent scaling or modular-spectrum theorem supplies type III$_1$; factoriality removes the centre; and separable predual lets the Connes--Haagerup classification identify the unique hyperfinite type III$_1$ factor. These hypotheses are non-trivial, and the result is *not* "true of every QFT" in the loose sense; Week 12 gives the full citation chain. The whole motivation for the [[week-13-crossed-product-construction|crossed product]] (Block D) and for [[sem2-week-01-witten-setup|Witten's gravitational dressing]] is to pass from the sharp type-III algebra to an enlarged semifinite algebra under additional hypotheses.

We refine the classification of type III in §6 below.

## 4. Trace existence

**Theorem 4.1 (Existence of trace). [Type-III $\Rightarrow$ no trace direction sketched below; other directions stated only — refs: Murray–vN; Takesaki Vol. I §V.2.]** *A factor $\mathcal{M}$ admits a faithful normal semifinite trace iff $\mathcal{M}$ is of type I or II.*

In particular, type III factors are characterized by the *non-existence* of trace.

Why does the trace exist for I, II and not III?

- *Type I:* the trace is the "operator trace" $\mathrm{Tr}$ on $\mathcal{B}(\mathcal{H})$. Normalized in finite dimensions, semifinite in infinite.
- *Type II$_1$:* the Murray–von Neumann dimension theory uses comparison and continuity of the projection lattice to construct a normalized dimension function on projections, then extends it to a faithful normal trace. The resulting trace is the unique normal state invariant under all inner automorphisms. There is no minimal projection relative to which one could count ranks.
- *Type II$_\infty$:* tensor product of II$_1$ trace and $\ell^2$ trace.
- *Type III:* here is the short contradiction that uses **both** semifiniteness and infiniteness. Suppose $\tau$ were a faithful normal semifinite trace and choose a non-zero projection $p$. Semifiniteness supplies a non-zero $q\le p$ with $0<\tau(q)<\infty$. Since every non-zero projection is infinite, there is a strict subprojection $q_1<q$ with $q_1\sim q$. Traciality gives $\tau(q_1)=\tau(q)<\infty$, while finite additivity on the orthogonal decomposition $q=q_1+(q-q_1)$ gives
  $$
  \tau(q)=\tau(q_1)+\tau(q-q_1).
  $$
  Hence $\tau(q-q_1)=0$. Faithfulness forces $q-q_1=0$, contradicting $q_1<q$. Thus no faithful normal semifinite trace exists. $\square$

The crucial role of trace in physics: it underlies the standard von Neumann entropy. The *absence* of trace in type III is what forces the development of relative-entropy methods, the [[week-07-connes-cocycle-and-relative-entropy|Araki–Uhlmann]] entropy, and ultimately the crossed-product construction that recovers a semifinite trace by adjoining the modular-translation degree of freedom. Interpreting that degree of freedom as an observer's clock is additional physics, introduced only in the gravitational applications.

> **Physical picture.** The trace is the algebraic form of a state-independent counting measure. For a finite-dimensional projection, $\mathrm{Tr}(p)$ counts dimensions; in a II$_1$ factor, $\tau(p)$ generalizes the fraction of available degrees of freedom selected by $p$. Type III has no faithful normal semifinite version of that measure. Therefore a sharply local QFT algebra has no intrinsic “uniform local ensemble” and no entropy of the form $-\tau(\rho\log\rho)$. This statement does not say that every local state has a literal temperature. It says something more precise: absolute state counting is unavailable, whereas comparisons of states through modular theory and relative entropy remain meaningful. Block D will enlarge the algebra to a semifinite core, where a trace becomes available only after the extra modular degree of freedom has been included.

## 5. Concrete examples

### 5.1 Type I factors

- $\mathcal{B}(\mathcal{H})$ for any Hilbert space $\mathcal{H}$. Type I$_n$ if $\dim\mathcal{H} = n$, type I$_\infty$ otherwise.
- $L^\infty(\mathbb{R})$ acting on $L^2(\mathbb{R})$ is *not* a factor (it is its own commutant); decomposed into factors via direct integral over $\mathbb{R}$, each fiber is type I$_1 = \mathbb{C}$.
- Tensor products $M_n(\mathbb{C}) \otimes M_m(\mathbb{C}) = M_{nm}(\mathbb{C})$ — still type I.

### 5.2 Type II$_1$: hyperfinite construction

The most concrete and useful type II$_1$ factor is the *hyperfinite II$_1$ factor* $\mathcal{R}$, constructed as an inductive limit of matrix algebras.

**Construction.** Set $\mathcal{A}_n := M_2(\mathbb{C})^{\otimes n} = M_{2^n}(\mathbb{C})$, with the normalized trace $\tau_n(a_1 \otimes \cdots \otimes a_n) := 2^{-n} \prod_i \mathrm{Tr}(a_i)$. The inclusion $\mathcal{A}_n \hookrightarrow \mathcal{A}_{n+1}$ via $a \mapsto a \otimes 1$ is *trace-preserving*: $\tau_{n+1}(a \otimes 1) = 2^{-(n+1)} \mathrm{Tr}(a \otimes 1) = 2^{-(n+1)} \cdot 2 \cdot \mathrm{Tr}(a) = 2^{-n} \mathrm{Tr}(a) = \tau_n(a)$.

Form the inductive limit (a \*-algebra) $\mathcal{A}_\infty := \bigcup_n \mathcal{A}_n$ with the consistent trace $\tau$. Run GNS in this trace state: in our convention, linear in the second slot, $\mathcal{H}_\tau$ is the completion of $\mathcal{A}_\infty$ with respect to $\langle a, b\rangle_\tau := \tau(a^*b)$. Take the WOT-closure of the image of $\mathcal{A}_\infty$ in $\mathcal{B}(\mathcal{H}_\tau)$.

**The result $\mathcal{R}$ is the hyperfinite II$_1$ factor.** Concretely:
- Every element of $\mathcal{R}$ is a WOT-limit of elements in some $M_{2^n}(\mathbb{C})$.
- The trace $\tau$ extends from $\mathcal{A}_\infty$ to $\mathcal{R}$ as a faithful normal state: $\tau(a) = \langle 1, a 1\rangle_\tau$ where $1 \in \mathcal{H}_\tau$ is the cyclic vector (image of $1 \in \mathcal{A}_\infty$).
- $\mathcal{R}$ is a factor: its center is trivial. (This requires a non-trivial argument — see Murray–vN.)
- $\mathcal{R}$ contains projections of every value $\tau(p) \in [0, 1]$: dyadic rationals from finite-dimensional approximation, full interval by SOT-limits.

**Theorem 5.1 (Murray–vN uniqueness). [Stated only — refs: Murray & von Neumann, *On rings of operators IV*, Ann. of Math. 44 (1943) 716–808.]** *Among factors with separable predual, the hyperfinite II$_1$ factor is unique up to isomorphism.*

This is the analog of Theorem 3.2 (every type I factor is $\mathcal{B}(\mathcal{K})$): the hyperfinite II$_1$ factor is *the* type II$_1$ factor that arises from inductive limits of finite-dimensional algebras. Non-hyperfinite type II$_1$ factors exist (e.g., the group factors $\mathcal{L}(F_2)$ — see below) and are *not* isomorphic to $\mathcal{R}$.

### 5.3 Type II$_1$: group factors

For a discrete icc group $G$, the group vN algebra $\mathcal{L}(G) = \{\lambda(g)\}'' \subset \mathcal{B}(\ell^2(G))$ is a type II$_1$ factor.

**Verification (clean route via factor classification).** Three structural facts together force type II$_1$:

1. *$\mathcal{L}(G)$ is a factor when $G$ is icc.* Any $a \in \mathcal{L}(G) \cap \mathcal{L}(G)'$ commutes with every $\lambda(g)$, so its expansion $a = \sum_g a_g \lambda(g)$ has coefficients constant on conjugacy classes. The icc condition (every non-identity conjugacy class is infinite) combined with $\ell^2$-summability of the coefficients forces $a_g = 0$ for $g \neq e$, so $a \in \mathbb{C}\cdot 1$. Hence $\mathcal{L}(G)$ has trivial center.

2. *Faithful normalized trace exists.* The trace $\tau(a) := \langle\delta_e, a\delta_e\rangle$ is faithful, normal, normalized, and tracial (Week 2 Example 5.5). Existence of a normalized trace rules out types II$_\infty$ (no normalized trace) and III (no trace at all).

3. *No minimal projections (and infinite-dimensional).* Every type I$_n$ factor with $n < \infty$ is finite-dimensional, while $\mathcal{L}(G)$ for $G$ infinite is infinite-dimensional (the $\lambda(g)$ for distinct $g$ are linearly independent). Type I$_\infty$ factors do not admit a *normalized* trace (only a semifinite one), contradicting (2). So $\mathcal{L}(G)$ is not type I.

By Theorem 3.1 the only remaining option is II$_1$. **[Sketched.]**

The argument deliberately avoids relying on a "$\mathcal{L}(G)$ has projections of every trace value $\in [0,1]$" claim. That conclusion follows from the general continuous-dimension theorem for II$_1$ factors once the type has been established, but it cannot be used here as an input without making the reasoning circular.

**The icc condition is essential.** For $G = \mathbb{Z}$: not icc (the conjugacy class of $g \neq e$ is just $\{g\}$). And indeed $\mathcal{L}(\mathbb{Z}) \cong L^\infty(\mathbb{T})$ — abelian, not a factor.

**Examples of icc groups.** $S_\infty$ (finitary permutations of $\mathbb{N}$); free groups $F_n$ for $n \ge 2$; $\mathrm{PSL}_2(\mathbb{Z})$.

**Theorem 5.2 (Murray–von Neumann 1943). [Stated only — ref: *On rings of operators IV*, Ann. of Math. 44 (1943) 716–808.]** *$\mathcal L(F_2)$ is not isomorphic to the hyperfinite II$_1$ factor $\mathcal R$.*

Murray and von Neumann introduced **property $\Gamma$** for this purpose: $\mathcal R$ has property $\Gamma$, whereas $\mathcal L(F_2)$ does not. Connes' 1976 classification of injective factors later placed this distinction in a much broader framework, but it is not the original proof of non-isomorphism. We will use neither proof; the point is simply that the trace and the Murray–von Neumann type do not classify II$_1$ factors up to isomorphism.

### 5.4 Type II$_\infty$: tensor extension

$\mathcal{R} \otimes \mathcal{B}(\ell^2(\mathbb{N}))$ is a type II$_\infty$ factor. The semifinite trace is $\tau \otimes \mathrm{Tr}$. Projections have continuous trace values in $[0, \infty]$.

This will be the type of the *crossed product* algebra in Block D: the dressed algebra $\mathcal{M} \rtimes_\sigma \mathbb{R}$ for $\mathcal{M}$ type III$_1$ is type II$_\infty$.

### 5.5 Type III: Powers factors (preview of Week 4)

We construct a type III factor in detail in Week 4 via the *Powers* construction — an infinite tensor product of $M_2(\mathbb{C})$'s with each factor in a *non-tracial* state. For each $\lambda \in (0,1)$ (strictly!), the resulting algebra is the hyperfinite type III$_\lambda$ factor. The endpoint $\lambda = 1$ corresponds to the *tracial* product state, and the resulting algebra is the hyperfinite II$_1$ factor — **not** the type III$_1$ factor.

**Important caveat on notation.** The Connes classification (§6 below) names a separate full-spectrum class III$_1$, distinct from "the $\lambda = 1$ endpoint" of the Powers III$_\lambda$ family. Concretely:
- Powers III$_\lambda$ family: $\lambda \in (0, 1)$ strictly. Discrete S-invariant $\{0\}\cup\{\lambda^n : n\in\mathbb Z\}$.
- Tracial endpoint of the Powers family ($\lambda = 1$): hyperfinite II$_1$.
- Type III$_1$: a *separate* Connes class with S-invariant $[0, \infty)$ (full positive half-line). The QFT case, not the Powers $\lambda \to 1$ limit.

The contrast with §5.2 is striking: changing the state on each $M_2(\mathbb{C})$ factor from tracial to non-tracial qualitatively *changes the type* of the inductive limit, from II$_1$ to III$_\lambda$. A small change in state, a qualitative algebraic shift.

## 6. The type III classification (Connes' invariants)

Type III factors come in a one-parameter family of subtypes, distinguished by Connes' invariants. We state the classification; we do not derive it.

**A subtle point first.** The "period" or "spectrum" of a modular flow depends on a *choice of state* (a cyclic-separating vector). The thing that is invariant of the algebra alone is constructed by *intersecting* over all faithful normal states, giving the **Connes S-invariant**:
$$
S(\mathcal{M}) \;:=\; \bigcap_{\varphi\;\text{faithful normal semifinite weight}} \,\sigma(\Delta_\varphi),
$$
where $\sigma(\Delta_\varphi)$ is the spectrum of the modular operator associated with the weight $\varphi$. This intersection is a closed multiplicative subset of $[0, \infty)$ that depends only on $\mathcal{M}$. The terms *weight*, *faithful*, *normal*, and *semifinite* are defined together in [[functional-analysis-survival-kit|Appendix A §A.5.1]]. A faithful normal state is a special finite example of such a weight.

**Theorem 6.1 (Connes 1973). [Stated only — refs: Connes, Ann. Sci. ENS 6 (1973) 133–252.]** *A type III factor $\mathcal{M}$ falls into one of three subfamilies, distinguished by $S(\mathcal{M})$:*

- *Type III$_\lambda$ for $\lambda \in (0,1)$: $S(\mathcal{M}) = \{0\} \cup \{\lambda^n : n \in \mathbb{Z}\}$ — a discrete multiplicative subset. The Powers factor $\mathcal{R}_\lambda$ (Week 4) realizes this case explicitly; on the Powers state $\omega_\lambda^{\otimes\infty}$ the modular flow is periodic with period $T_\lambda = 2\pi/|\log\lambda|$, but periodicity of the flow is a state-level statement and the algebra-level invariant is $S(\mathcal{M})$.*
- *Type III$_0$: $S(\mathcal{M}) = \{0, 1\}$ (no nontrivial multiplicative structure).*
- *Type III$_1$: $S(\mathcal{M}) = [0, \infty)$ — the full positive half-line. Equivalently, every faithful normal semifinite weight has full positive modular spectrum. This is the "most non-tracial" subtype in the precise sense of the $S$-invariant.*

**Type III$_1$ is the type relevant to standard QFT examples under additional hypotheses.** Week 12 makes the theorem chain precise. Bisognano–Wichmann computes one preferred wedge modular operator; a separate type or scaling theorem is needed because the spectrum of one state does not evaluate the intersection defining $S(\mathcal M)$.

> **Physical picture.** In a finite type-I standard form, modular eigenvalues are ratios $p_i/p_j$ of density-matrix eigenvalues. This makes a discrete Powers ladder and a continuous III$_1$ spectrum easy to visualize. Beyond type I, however, those numbers are modular spectral values, not literal ratios of eigenvalues of a local density matrix. The $S$-invariant extracts the part of the modular spectrum that survives every faithful weight. The analogy is a mnemonic; Week 12 supplies the classification theorem.

We will see Connes' invariants in operational form in Week 6 (modular flow on a specific state) and in Week 11 (Bell-CHSH on type III$_1$ algebras in QFT).

**Hyperfinite type III$_1$ — the citation chain.** In the separable-predual setting there is a *unique* hyperfinite type III$_1$ factor up to isomorphism—but pinning down the precise statement and its proof is a multi-paper effort:

- *Connes* (1976, *Ann. of Math.*) — classified the hyperfinite type III$_\lambda$ factors for $\lambda \in (0, 1)$ and reduced the III$_1$ case to a remaining technical question.
- *Haagerup* (1987, *Acta Math.*) — completed the classification by proving uniqueness of the hyperfinite type III$_1$ factor.
- *Buchholz–D'Antoni–Fredenhagen* (1987, *Comm. Math. Phys.*) — obtained the hyperfinite universal structure from phase-space/split assumptions, retaining the centre in the general statement. A separate modular or scaling input supplies the III$_1$ subtype.

We do not prove these in this course; they are stated and used. **[Stated only — refs as above.]**

## 7. Why this matters for QFT

Block C will state and use the following result, **with hypotheses made explicit there:**

**Claim (hypothesis-explicit synthesis, to be used in Block C). [Stated only.]** *If suitable phase-space hypotheses give hyperfiniteness, a separate scaling/modular theorem gives type III$_1$, and the bounded-region local algebra is a factor with separable predual, then $\mathcal A(\mathcal O)$ is isomorphic to the unique hyperfinite type III$_1$ factor.*

The hypotheses are non-trivial and must be verified model by model. Free-field and many conformal nets provide standard examples. No complete four-dimensional interacting construction licenses an automatic extrapolation to QCD or to the Standard Model.

**Citation chain.** This is *not* the Haag–Hugenholtz–Winnink theorem (1967), which is about the equivalence of KMS and equilibrium states — a foundational but distinct result. The local-algebra type III$_1$ universality theorem is the cumulative product of:

- *Driessler* (Comm. Math. Phys. 1975/1977) — modular-spectrum criteria forcing local algebras to be type III.
- *Fredenhagen* (Comm. Math. Phys. 97 (1985)) — type III$_1$ under asymptotic-scale-invariance / modular-spectrum hypotheses.
- *Buchholz–Wichmann* (Comm. Math. Phys. 106 (1986)) — *nuclearity* as the right phase-space condition.
- *Buchholz–D'Antoni–Fredenhagen* (Comm. Math. Phys. 111 (1987)) — hyperfinite universal structure from phase-space/split input, with the centre present in the general result.
- *Buchholz–Verch* (Rev. Math. Phys. 7 (1995)) — scaling-algebra route from a nontrivial scaling limit to the III$_1$ conclusion under its hypotheses.

We will not reproduce this chain. Block C states the theorem with hypotheses, cites the references, and uses the result. A student who wants the proofs should consult the references directly (or Halvorson's "Algebraic Quantum Field Theory" 2006 review, which surveys the chain).

Implications:

1. **No intrinsic local density matrix.** A normal local state may have an ambient trace-class representative on the vacuum Hilbert space, but there is no canonical trace-density inside the type-III algebra and no sharp tensor-factor partial trace.

2. **No intrinsic absolute von Neumann entropy.** Regulated entanglement entropies may diverge as the cutoff is removed, but that divergence is not a proof of type. Relative entropy remains intrinsic and may be finite or $+\infty$; regulated differences require a controlled matching theorem.

3. **Operational resources, with scope.** Type-III$_1$ factors are universal embezzlers in the precise approximate sense reviewed in Week 12. Bell maximality, by contrast, is a theorem about a specified pair of commuting local algebras and cannot be inferred from the type label alone.

4. **The continuous core supplies a semifinite enlargement.** Block D forms $\mathcal M\rtimes_{\sigma^\omega}\mathbb R$ on a space involving $L^2(\mathbb R)$. For a III$_1$ factor the core is II$_\infty$ with a faithful normal semifinite trace. Trace-densities and entropies still require normality and integrability, and the “modular clock” interpretation is extra physical structure.

## 8. What to take away

1. **Murray–vN classification.** Three families: I (ordinary operator factors), II (semifinite with continuous projection dimension), and III (no faithful normal semifinite trace). Type III subdivides into III$_0$, III$_\lambda$ for $0<\lambda<1$, and III$_1$; the symbols $0$ and $1$ label distinct Connes classes and are not endpoints of a single Powers construction.

2. **The trace is the engine.** Types I and II have traces; type III does not. Most quantum-mechanical reasoning relies on trace and breaks down in type III. **Two structurally distinct fixes** operate in tandem in the rest of the course: (a) modular theory (Block B) gives the canonical *state-dependent dynamics* — the modular flow — for any faithful normal state on a type III algebra, *without* producing a trace; (b) the crossed product (Block D) uses that dynamics to build a *larger* semifinite algebra carrying a faithful normal semifinite trace. The trace lives on the dressed algebra, not on the original type III algebra.

3. **The hyperfinite II$_1$ factor.** Concrete example, constructed by inductive limit of matrix algebras with the tracial states. Unique up to isomorphism in the separable-predual setting (Murray–vN). An analogous hyperfinite type III$_1$ factor exists and is the local-QFT type under the additional hypotheses stated in Week 12.

4. **Connes' invariants.** Type III subdivides into III$_0$, III$_\lambda$ ($0<\lambda<1$), and III$_1$. Type III$_1$ is the generic local-QFT case under the additional hypotheses stated in Week 12 and is characterized by the full Connes $S$-invariant $[0,\infty)$.

5. **The challenge type III poses.** Without trace, we need new tools: relative entropy (Week 7), modular theory (Block B), crossed products (Block D). These are exactly what Tomita–Takesaki provides.

6. **The vN closure of a C\*-algebra is state-dependent — and so its type can be.** Type is an *isomorphism invariant of the von Neumann algebra*: once you have a vN factor, its type is intrinsic and does not depend on any external state. What *does* depend on the state is which vN algebra you get out of the GNS construction in the first place. The Powers construction (Week 4) is the cleanest illustration: the same UHF C\*-algebra $\bigotimes_{n=1}^\infty M_2(\mathbb{C})$, completed in the tracial product state $\tau^{\otimes\infty}$, yields the hyperfinite II$_1$ factor; completed in a non-tracial product state $\omega_\lambda^{\otimes\infty}$, yields a type III$_\lambda$ factor. Two different von Neumann algebras come out of the same C\*-algebraic skeleton, depending on which GNS representation you take. The two vN algebras are not isomorphic, and each has its type intrinsically.

## 9. Looking ahead: Week 4

Next week we introduce the *KMS condition* — the algebraic notion of thermal equilibrium that survives in type III, where Gibbs states do not exist. We construct the Powers factor (a concrete type III) by infinite tensor product, and we preview the central theorem of Block B: the Tomita-Takesaki theorem, which says that every cyclic-separating vector for a vN algebra produces a canonical one-parameter "modular flow" for which it is KMS at $\beta = 1$ (in our upper-strip $\beta > 0$ convention; see Week 4 §6.1 for the sign-convention discussion). This gives type III the dynamical structure it lacked.

## 10. Problem set

**Core problems.**

**1. Type I in detail.**
(a) Show that $\mathcal{B}(\mathcal{H})$ has minimal projections: any rank-one projection $|\xi\rangle\langle\xi|$ for unit $\xi$ is minimal.
(b) Identify the trace on $\mathcal{B}(\mathcal{H})$ when $\dim\mathcal{H} < \infty$ (the standard $\mathrm{Tr}$). When $\dim\mathcal H=\infty$, regard the standard trace as an extended-valued weight on positive operators. Show that it cannot be normalized, that it is finite on positive finite-rank operators, and that these operators witness semifiniteness below every nonzero positive element.
(c) Show that any two minimal projections in a type I factor are Murray–vN equivalent.
(d) Compute the trace of the projection $1 - p$ for an arbitrary minimal $p \in M_n(\mathbb{C})$.

**2. Comparison theorem in finite dimensions.**
For $\mathcal{M} = M_n(\mathbb{C})$, prove the comparison theorem (Theorem 1.6) directly: any two projections $p, q$ satisfy $\mathrm{rank}(p) \le \mathrm{rank}(q)$ or vice versa, and projections of equal rank are Murray–vN equivalent. Construct explicit partial isometries.

**3. Hilbert's hotel.**
For $\mathcal{B}(\ell^2)$:
(a) Construct an explicit partial isometry $v$ with $v^* v = 1$ and $v v^* < 1$. Identify the missing dimension.
(b) Show that the identity projection $1$ is Murray–vN equivalent to any non-zero projection of infinite rank. (*Hint:* construct a partial isometry via a suitable bijection of the basis.)
(c) Conclude that *every* infinite-rank projection is infinite, and *every* finite-rank projection is finite.

**4. The hyperfinite II$_1$ factor.**
Recall the inductive construction in §5.2.
(a) Verify that the inclusion $M_{2^n}(\mathbb{C}) \hookrightarrow M_{2^{n+1}}(\mathbb{C})$ (via $a \mapsto a \otimes 1$) is trace-preserving for the normalized traces.
(b) Verify that the consistent trace $\tau$ extends to the inductive limit $\mathcal{A}_\infty$.
(c) Show that $\mathcal{R}$ contains projections of every value $\tau(p) \in [0, 1] \cap \mathbb{Q}_{(2)}$ (rationals with denominators a power of 2).
(d) (Harder.) Show that $\mathcal{R}$ contains projections of *every* value $\tau(p) \in [0, 1]$ — the trace takes all real values in $[0,1]$ on projections.
(e) Work at the finite stage $\mathcal A_3=M_8(\mathbb C)$. Exhibit a diagonal projection of rank $3$, compute its normalized trace, and follow it under the embedding $\mathcal A_3\hookrightarrow\mathcal R$. This is the finite-stage dyadic case; the non-dyadic value $1/3$ is reserved for Problem 7.

**5. No semifinite trace in type III.**
Suppose $\mathcal M$ is a factor in which every non-zero projection is infinite. Assume for contradiction that $\tau$ is a faithful normal semifinite trace.
(a) Use semifiniteness to show that every non-zero projection $p$ contains a non-zero subprojection $q\le p$ with $0<\tau(q)<\infty$.
(b) Since $q$ is infinite, choose $q_1<q$ with $q_1\sim q$. Use traciality and the **finite** value of $\tau(q)$ to show $\tau(q-q_1)=0$.
(c) Apply faithfulness and obtain the contradiction. Explain explicitly why starting with a projection of trace $\infty$ would make the subtraction $\infty-\infty$ invalid.

**6. Group factors.**
For $G$ a discrete icc group:
(a) Verify that the trace $\tau(a) = \langle\delta_e, a\delta_e\rangle$ is normal and tracial on $\mathcal{L}(G)$.
(b) Show that the trace takes the value $\tau(\lambda(g)) = [g = e]$ on group elements — purely supported at the identity.
(c) For $G = F_2=\langle a,b\rangle$, use the functional calculus of the Haar-spectrum unitary $\lambda(a)$ to find a projection in $\mathcal{L}(F_2)$ with trace $1/2$. (*Hint:* take the spectral projection of $\lambda(a)$ for a semicircle in $\mathbb T$.)

**Starred problems.**

**7\*. Type II$_1$ as continuous-dimension matrix algebras.**
Construct an explicit projection $p \in \mathcal{R}$ with $\tau(p) = 1/3$. (*Hint:* approximate from above and below using $M_{2^n}(\mathbb{C})$ projections; the dyadic rationals are dense.) Generalize: for any $r \in [0, 1]$, exhibit a projection of trace $r$ in $\mathcal{R}$.

**8\*. Group factors and property $\Gamma$.**
Show that $\mathcal L(F_2)$ is a factor by proving that $F_2$ is icc. State Murray and von Neumann's property-$\Gamma$ distinction between $\mathcal R$ and $\mathcal L(F_2)$, and then explain how Connes' later injectivity classification subsumes the hyperfinite side of the comparison. Keep the two historical results separate.

**9\*. Comparison theorem revisited.**
Prove the comparison theorem (Theorem 1.6) in full for a *factor* $\mathcal{M}$, using Zorn's lemma and the comparability of projections in the type I subcase. Sketch how the argument extends to types II and III.

**10\*\* (Optional, very hard).** Study the property-$\Gamma$ separation directly. Construct an asymptotically central sequence of trace-zero unitaries in the hyperfinite factor $\mathcal R$, and read the Murray–von Neumann argument that no such sequence exists in $\mathcal L(F_2)$. Explain why this proves non-isomorphism. Then compare this invariant with Connes' 1976 characterization of injective factors. (Do not formulate the issue in terms of an inner automorphism that is not approximately inner: every inner automorphism is already approximately inner.)

## Self-study answer checkpoints

The checks below cover the core route through projection comparison and traces. Starred problems remain theorem- and source-led, especially the non-dyadic construction and property-$\Gamma$ arguments.

1. **Type I.** Rank-one projections are minimal. In infinite dimension the standard trace is an extended-valued faithful normal semifinite trace, finite on finite-rank positives and infinite on $1$; a nonzero $a\ge0$ dominates $\varepsilon p$ for some rank-one $p$ inside a nonzero spectral subspace of $a$. Minimal projections in a factor are equivalent. In $M_n$, $\operatorname{Tr}(1-p)=n-1$.

2. **Finite-dimensional comparison.** The comparison is exactly rank comparison. If $\operatorname{rank}p\le\operatorname{rank}q$, an isometry from $p\mathbb C^n$ into $q\mathbb C^n$, extended by zero, gives the required partial isometry; equality of ranks gives equivalence.

3. **Hilbert's hotel.** The unilateral shift has $S^*S=1$ and $SS^*=1-|e_1\rangle\langle e_1|$. Any infinite-rank projection on separable $\ell^2$ has range isomorphic to $\ell^2$, hence is equivalent to $1$ and to a proper subprojection of itself. Finite-rank projections cannot be equivalent to a proper subprojection because rank is preserved.

4. **The hyperfinite II$_1$ factor.** The embeddings $a\mapsto a\otimes1$ preserve normalized trace. The compatible trace extends first to the UHF norm closure and then normally to the GNS weak closure. At finite stages, projection traces are dyadic. Increasing strong limits of nested dyadic projections, together with normality, realize every $r\in[0,1]$. For part (e),
   $$
   p=\operatorname{diag}(1,1,1,0,0,0,0,0)\in M_8
   $$
   has normalized trace $3/8$, retained under every later embedding.

5. **No semifinite trace in type III.** Semifiniteness supplies $0\ne q\le p$ with $0<\tau(q)<\infty$. If $q_1<q$ and $q_1\sim q$, then $\tau(q_1)=\tau(q)$ and finite additivity gives $\tau(q-q_1)=0$, contradicting faithfulness. The finiteness of $\tau(q)$ is essential: $\infty-\infty$ is not an argument.

6. **Group factors.** The vector functional at $\delta_e$ is normal, tracial, faithful, and satisfies $\tau(\lambda(g))=\delta_{g,e}$. For $F_2$, the unitary $\lambda(a)$ has Haar spectral measure on $\mathbb T$; the spectral projection of any semicircle therefore has trace $1/2$.

**Wiki connections.** [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]] · [[entanglement-embezzlement|entanglement embezzlement]] · [[2025-liu-lectures-entanglement-vna|Liu's lectures on entanglement and von Neumann algebras]] · [[bell-inequalities-qft|Bell inequalities in QFT]] (research area) · [[relative-entropy-qft|relative entropy in QFT]] (research area)

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester I Block A. Last revised 2026-09-29.*
