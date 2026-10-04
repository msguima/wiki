---
title: "Sem II Week 5 — 't Hooft Anomalies: Obstruction as Physics"
type: lecture-notes
course: syllabus
semester: 2
week: 5
block: 2
duration: 4 hours (3 hr lectures + 1 hr seminar, the first seminar of Block 2, presented by the instructor)
prerequisites: Sem II Weeks 1–4; Semester I Weeks 4 and 7
modified: 2026-10-02
---

# Sem II Week 5 — 't Hooft Anomalies: Obstruction as Physics

> *[[sem2-week-04-gauging-backgrounds-and-dual-symmetry|Sem II Week 4]] summed a theory over its backgrounds, which required a gauge-invariant partition function (F3 there). This week we study symmetries whose invariance fails by a phase that no local counterterm removes. The phase depends only on how the symmetry acts and on locality, so no symmetric deformation or renormalization-group flow changes it, and it forbids a trivially gapped ground state. We meet it in three finite calculations: a projective representation of $\mathbb{Z}_2\times\mathbb{Z}_2$, the Lieb–Schultz–Mattis constraint on a spin-1/2 ring threaded by a flux, and the end of the cluster chain, where the bulk one dimension up cancels it. Sem II Week 6 finds the same structure in Yang–Mills theory at θ = π; Sem II Week 7 classifies the bulks.*

### How to use this chapter

- **In class:** in the first lecture derive (2.1)–(2.2), then §3 in order: the cocycle condition (3.2), the Pauli cocycle (3.6), the two-dimensional irreducible representation (§3.3), the classification (3.9) and the partition-function form (3.11); Problem 1. In the second, the ring operators (4.2)–(4.4), the flux argument (4.5) with Figure 2 on the board, the anomaly (4.7) and the odd ring (4.8); Problems 2 and 3. In the third, the restricted symmetry of the cluster chain (5.6)–(5.7) with Figure 3, the twisted rings of §5.3, the inflow identity (5.9)–(5.12) and §§6.1–6.2; Problem 4. The seminar hour (§7) is Oshikawa's letter, presented by the instructor as the model for Block 2.
- **For self-study:** §6.3, the fine print of §8 and Problems 5⋆–7⋆. The one calculation to do alone is the four-site ring of §4.3 by hand: the six states with $S^z_{\rm tot}=0$, the blocks with $P=0$ and $P=\pi$, and their lowest levels followed from φ = 0 to 2π.
- **Instructor checkpoint:** two errors recur. The first is to call any sign in a product of symmetry operators an anomaly: $U(a)^2=-1$ for one $\mathbb{Z}_2$ is removed by $U(a)\to iU(a)$, and the invariant is the commutator phase $c(a,b)$ of (3.4) (F1). The second is to forget why momentum is conserved during the flux insertion: the uniform gauge (4.1) keeps every $H(\varphi)$ translation invariant, and the shift $2\pi\nu$ comes entirely from (4.4), whose boundary factor $e^{2\pi in_1}$ is 1 because occupations are integers.

## 0. Reading

**Primary:** Oshikawa, *Phys. Rev. Lett.* 84 (2000) 1535, the whole letter (the seminar of §7). Gaiotto, Kapustin, Komargodski, Seiberg (GKKS), arXiv:1703.00501, App. D.1: 't Hooft anomalies in quantum mechanics as projective representations (Problem 6⋆).

**Secondary:** Cheng & Seiberg, *SciPost Phys.* 15 (2023) 051 [arXiv:2211.12543], for the viewpoint of §§4–6, in which the symmetries of twisted Hilbert spaces and their representations capture the anomaly. Lieb, Schultz, Mattis (LSM), *Ann. Phys.* 16 (1961) 407, and Hastings, *Phys. Rev. B* 69 (2004) 104431 [cond-mat/0305505], for the theorems (statements). Else & Nayak, *Phys. Rev. B* 90 (2014) 235137 [arXiv:1409.5436], for the edge restriction of §5.2; Chen, Gu, Liu, Wen (CGLW), arXiv:1106.4772, for the classification statements of §§5.4 and 6.3. From the course: Sem II Week 4 §§2, 5 and F3; [[week-04-bkt-kramers-wannier-disorder|Sem I Week 4]] §3.4; [[sem2-week-02-zn-gauge-theory-as-bf-theory|Sem II Week 2]] §§3.3–3.4; McGreevy, arXiv:2204.03045, as the companion review.

**Optional research reading:** 't Hooft, *NATO Sci. Ser. B* 59 (1980) 135 (Cargèse 1979), for anomaly matching; Callan & Harvey, *Nucl. Phys. B* 250 (1985) 427, for inflow; Ogata, Tachikawa, Tasaki (OTT), *Commun. Math. Phys.* 385 (2021) 79 [arXiv:2004.06458], for §4.5; Briegel & Raussendorf, *Phys. Rev. Lett.* 86 (2001) 910 [quant-ph/0004051], for the cluster state; Majumdar & Ghosh, *J. Math. Phys.* 10 (1969) 1388, for Problem 7⋆; Tachikawa, arXiv:1712.09542, for §6.3.

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Sem I Week 1]]. Every sign and normalization is from [[courses/generalized-symmetries-course/conventions|conventions]]: the projective-representation conventions (3.1)–(3.4) and the SPT weight and edge rule (5.8), (5.11) are recorded in its §6, the twisted ring (4.1)–(4.2) and the cluster chain (5.1)–(5.2) in its §4. Every matrix identity below was checked with explicit Pauli matrices on the sizes named where it is used.

## 1. Motivation and setting

A symmetry usually says little about the low-energy physics of a local Hamiltonian: a symmetric chain can be gapless, break the symmetry, or be a paramagnet with a unique gapped ground state, depending on the couplings. Translation-invariant chains of spins 1/2 with spin-rotation symmetry are different. The Heisenberg chain is gapless and the Majumdar–Ghosh chain has two dimerized ground states (Problem 7⋆), but a unique gapped ground state never occurs: Lieb, Schultz and Mattis proved in 1961 that for isotropic interactions a state orthogonal to the ground state has an excitation energy that vanishes as the chain grows, and OTT exclude a unique gapped ground state for every such chain (§4.5). Likewise each end of an open cluster chain carries a qubit that no symmetric perturbation near that end polarizes, and in the gauged $\mathbb{Z}_4$ chain of Sem II Week 4 §5.2 the residual symmetry squares to $-1$ on a twisted sector.

The three are one phenomenon, an 't Hooft anomaly ([[t-hooft-anomaly]]): the symmetry cannot be coupled to backgrounds with a gauge-invariant partition function, and no local redefinition repairs this. We define it (§2), compute it in the smallest case (§3), find it in spin chains (§4), cancel it from one dimension up (§5) and turn it into a constraint (§6), always in finite dimensions; the anomalies of chiral fermions, where the subject began (§10), have the same structure.

## 2. What an 't Hooft anomaly is [Definitions; the remarks Proved.]

Let a theory on a closed spacetime $X$ have a symmetry $G$, with partition function $Z[A]$ in a background $A$: a cocycle $B\in Z^{p+1}(X,\mathbb{Z}_N)$ for $\mathbb{Z}_N^{(p)}$ (Sem II Week 4 (2.2)), a flat connection for $U(1)$, and in Hamiltonian language twisted boundary conditions and symmetry insertions (Sem I Week 4 §3.4). A background gauge transformation $A\to A^\lambda$ moves the defects without changing their classes. The models of Sem II Week 4 were invariant, (2.3) there; in general

$$
Z[A^\lambda]=e^{i\mathcal A(A,\lambda)}Z[A],\tag{2.1}
$$

where $\mathcal A$ is a local functional of $A$ and λ. The partition function is defined only up to local counterterms, $Z[A]\to e^{iS_{\rm ct}[A]}Z[A]$, with $S_{\rm ct}$ a local functional of the background alone, such as a phase per junction of defects or $k\oint A$ with integer $k$; they express the freedom in defining the symmetry operators near their junctions, the counterterm of a finite symmetry operator in [[sem2-week-01-symmetries-are-topological-operators|Sem II Week 1]] §2.2, and they change

$$
\mathcal A(A,\lambda)\to\mathcal A(A,\lambda)+S_{\rm ct}[A^\lambda]-S_{\rm ct}[A].\tag{2.2}
$$

**Definition.** $G$ has an 't Hooft anomaly if no local counterterm makes $\mathcal A$ vanish; the anomaly is the class of $\mathcal A$ modulo (2.2).

Three remarks. (i) The symmetry is exact, and the theory without backgrounds is untouched. (ii) An anomalous symmetry cannot be gauged: with $\mathcal A\neq0$ the sum (2.4) of Sem II Week 4 depends on the representatives (F3 there). (iii) The anomaly is computed from the symmetry operators and their locality, so all Hamiltonians with the same symmetry operators share it, the root of matching (§6); §5.4 shows, in the simplest case, that (2.1) is the boundary variation of a gauge-invariant theory one dimension up.

## 3. Projective $\mathbb{Z}_2\times\mathbb{Z}_2$ quantum mechanics

### 3.1 Projective representations and their cocycles [Proved.]

A projective representation of $G$ on $V$ is a set of unitaries with

$$
U(g)U(h)=\omega(g,h)\,U(gh),\qquad\omega(g,h)\in U(1),\tag{3.1}
$$

normalized by $U(e)=1$, so $\omega(e,g)=\omega(g,e)=1$. Associativity gives $(U(g)U(h))U(k)=\omega(g,h)\omega(gh,k)U(ghk)$ and $U(g)(U(h)U(k))=\omega(h,k)\omega(g,hk)U(ghk)$, so

$$
\omega(g,h)\,\omega(gh,k)=\omega(h,k)\,\omega(g,hk),\tag{3.2}
$$

the 2-cocycle condition. Rephasing $U'(g)=\beta(g)U(g)$, $\beta(g)\in U(1)$, changes

$$
\omega'(g,h)=\omega(g,h)\frac{\beta(g)\beta(h)}{\beta(gh)}\equiv\omega(g,h)(\delta\beta)(g,h).\tag{3.3}
$$

Cocycles modulo coboundaries form $H^2(G,U(1))$, whose product is the tensor product of representations. For abelian $G$, δβ is symmetric, so the commutator phase

$$
c(g,h)=\frac{\omega(g,h)}{\omega(h,g)},\qquad U(g)U(h)=c(g,h)\,U(h)U(g),\tag{3.4}
$$

depends only on the class. It is bimultiplicative: $U(g)U(h)U(k)=c(g,h)c(g,k)U(h)U(k)U(g)$ and $U(h)U(k)=\omega(h,k)U(hk)$ give $c(g,hk)=c(g,h)c(g,k)$, and $c(g,g)=1$, $c(h,g)=c(g,h)^{-1}$.

### 3.2 The Pauli cocycle [Computed.]

Write $g=a^{g_1}b^{g_2}\in\mathbb{Z}_2\times\mathbb{Z}_2=\{e,a,b,ab\}$, $g_i\in\{0,1\}$, and set on $\mathbb{C}^2$

$$
U(a^{g_1}b^{g_2})=X^{g_1}Z^{g_2}:\qquad U(e)=1,\ \ U(a)=X,\ \ U(b)=Z,\ \ U(ab)=XZ,\tag{3.5}
$$

with $X,Z$ the Pauli matrices. Since $ZX=-XZ$ and $X^2=Z^2=1$,

$$
U(g)U(h)=X^{g_1}Z^{g_2}X^{h_1}Z^{h_2}=(-1)^{g_2h_1}X^{g_1+h_1}Z^{g_2+h_2}\ \Longrightarrow\ \omega(g,h)=(-1)^{g_2h_1}.\tag{3.6}
$$

With rows $g$ and columns $h$ ordered $e,a,b,ab$, the rows of $e$ and $a$ are $(1,1,1,1)$ and those of $b$ and $ab$ are $(1,-1,1,-1)$. Being bilinear, (3.6) satisfies (3.2) identically, and $c(g,h)=(-1)^{g_1h_2+g_2h_1}$, with $c(a,b)=-1$. Compare $(-1)^{g_1h_1}$, the cocycle of $U(a)=iX$, with $U(a)^2=-1$: it is symmetric and equals δβ for $\beta(a^{g_1}b^{g_2})=i^{g_1}$, so a sign in $U(a)^2$ is removed by rephasing, and the invariant content is $c(a,b)$. We checked the sixteen entries of (3.6) and the 64 instances of (3.2) with Pauli matrices; of the 16 normalized ±1-valued cocycles, in 8 classes modulo ±1-valued coboundaries, the 8 symmetric ones are $U(1)$ coboundaries with β in $\{\pm1,\pm i\}$ and the 8 with $c(a,b)=-1$ are not.

### 3.3 The irreducible representation is two-dimensional [Proved.]

Let $U$ have $c(a,b)=-1$, rephased so that $U(a)^2=U(b)^2=1$ (possible since $U(g)^2=\omega(g,g)$ is a number for $g^2=e$). (i) There is no one-dimensional representation, since numbers commute. (ii) $\operatorname{tr}U(b)=\operatorname{tr}(U(a)U(b)U(a)^{-1})=-\operatorname{tr}U(b)$, so the eigenvalues $\pm1$ of $U(b)$ have equal multiplicity $m$ and $\dim V=2m$. (iii) $U(a)$ maps the eigenspace $V_+$ of $U(b)$ onto $V_-$, since $U(b)U(a)v=-U(a)U(b)v$. With an orthonormal basis $e_k$ of $V_+$ and $f_k=U(a)e_k$, so that $U(a)f_k=e_k$, the basis $e_k\otimes|{\uparrow}\rangle\equiv e_k$, $e_k\otimes|{\downarrow}\rangle\equiv f_k$ gives

$$
U(a)=1_m\otimes X,\qquad U(b)=1_m\otimes Z.\tag{3.7}
$$

Every representation in the class is $m$ copies of (3.5), the unique irreducible one, which is two-dimensional. If $[H,U(g)]=0$ for all $g$, $H$ commutes with $1_m\otimes X$ and $1_m\otimes Z$, which generate all $2\times2$ matrices on the second factor, so

$$
H=h\otimes1_2,\tag{3.8}
$$

with $h$ on $\mathbb{C}^m$: every level is at least doubly degenerate, a symmetric perturbation $h'\otimes1_2$ cannot split the doublets, and $\operatorname{Tr}(U(g)e^{-\beta H})=\operatorname{tr}(e^{-\beta h})\operatorname{tr}\sigma_g=0$ for $g\neq e$, with $\sigma_g\in\{X,Z,XZ\}$. The torus degeneracy of $\mathbb{Z}_N$ gauge theory (Sem II Week 2 §§3.3–3.4) has the same origin: the holonomies obey $ZX=\omega XZ$, a projective representation of $\mathbb{Z}_N\times\mathbb{Z}_N$ whose irreducible representation is $N$-dimensional (Problem 1).

### 3.4 $H^2(\mathbb{Z}_2\times\mathbb{Z}_2,U(1))=\mathbb{Z}_2$ [Proved.]

The map $[\omega]\mapsto c(a,b)$ is well defined (§3.1), a homomorphism, and onto (the trivial representation gives $+1$, (3.5) gives $-1$). It is one-to-one. If $c\equiv1$, ω is symmetric, and the algebra with basis $u_g$ and product $u_gu_h=\omega(g,h)u_{gh}$ is associative by (3.2) and commutative. Left multiplications by the $u_g$ then have a common eigenvector, $u_gv=\beta(g)v$, with $\beta(g)\neq0$ because $u_g$ is invertible, and

$$
\beta(g)\beta(h)\,v=u_gu_hv=\omega(g,h)\,u_{gh}v=\omega(g,h)\beta(gh)\,v ,
$$

so $\omega=\delta\beta$; since $|\omega|=1$, $|\beta|$ is a homomorphism of a finite group into the positive reals, so $|\beta|=1$ and $[\omega]=0$. Therefore

$$
H^2(\mathbb{Z}_2\times\mathbb{Z}_2,U(1))=\mathbb{Z}_2,\qquad[\omega]\longleftrightarrow c(a,b)=\pm1.\tag{3.9}
$$

The enumeration of §3.2 shows the same collapse: the 8 classes of $H^2(\mathbb{Z}_2\times\mathbb{Z}_2,\mathbb{Z}_2)=\mathbb{Z}_2^3$ fall into two according to $c$. The argument holds for every finite abelian group (Problem 1).

### 3.5 The anomaly in background language [Proved.]

On a Euclidean time circle of length β cut into $n$ steps of length ε, a background is a $G$-valued 1-cochain $g_t$ on the time links (flat in one dimension), and

$$
Z[g]=\operatorname{Tr}\big(e^{-\varepsilon H}U(g_{n-1})\cdots e^{-\varepsilon H}U(g_0)\big),\tag{3.10}
$$

with gauge transformations $g_t\to h_{t+1}g_th_t^{-1}$, $h_t\in G$. Since $[H,U]=0$, $Z[g]=\operatorname{Tr}\big(U(g_{n-1})\cdots U(g_0)\,e^{-\beta H}\big)$; for a linear representation this depends only on the holonomy, so gauge-equivalent backgrounds agree. Here a nontrivial holonomy gives $Z=0$, by $\operatorname{tr}\sigma_g=0$ in (3.8), so the test uses backgrounds with trivial holonomy. Take two backgrounds whose only nontrivial links are four insertions, consecutive ones separated by at least $r+1$ identity links (so $n\ge4(r+2)$), in the time orders $a,b,a,b$ and $a,a,b,b$. Both have trivial holonomy and are therefore gauge equivalent, and since $ZXZX=-1$ while $ZZXX=1$,

$$
Z[a\cdots b\cdots a\cdots b]=-\operatorname{Tr}e^{-\beta H},\qquad Z[a\cdots a\cdots b\cdots b]=+\operatorname{Tr}e^{-\beta H}.\tag{3.11}
$$

The relative sign is a non-local function of the links, fixed by the order of insertions arbitrarily far apart: it is the class $[\omega]\neq0$ at work. A local counterterm of range $r$ is a product of factors $f(g_t,\dots,g_{t+r})$ over windows of $r+1$ consecutive links; with the insertions this far apart each window contains at most one of them, both backgrounds contain the same windows, and the counterterm multiplies both by the same number. For adjacent insertions, $(a,b,a,b)$ and $(a,a,b,b)$ on four links, the pair counterterm $f(a,b)=-1$, all other $f=1$, does absorb the sign; the statement is that no local counterterm makes all gauge-equivalent backgrounds agree. The $0+1$d 't Hooft anomaly of $G$ is therefore the class $[\omega]\in H^2(G,U(1))$, since a coboundary is removed by the counterterm $\beta(g_t)$ per link, and for $\mathbb{Z}_2\times\mathbb{Z}_2$ the nontrivial class is (3.5). Gauging fails with it: in quantum mechanics gauging projects onto states with $U(g)|\psi\rangle=|\psi\rangle$ for all $g$, the Gauss law of Sem II Week 4 §3.1, and $U(a)U(b)=-U(b)U(a)$ admits none.

## 4. Lieb–Schultz–Mattis as a mixed anomaly

### 4.1 The ring and its operators [Proved.]

Take $L$ spins 1/2 on a ring, $j=1,\dots,L$, $j+L\equiv j$, with $S^a_j=\tfrac12\sigma^a_j$, occupations $n_j=S^z_j+\tfrac12\in\{0,1\}$, charge $Q=\sum_jn_j=S^z_{\rm tot}+L/2$ and filling $\nu=Q/L$. The $U(1)$ acts by $S^\pm_j\to e^{\pm i\alpha}S^\pm_j$, translation by $TS^a_jT^{-1}=S^a_{j+1}$ ([[courses/generalized-symmetries-course/conventions|conventions]] §4), and momentum is defined by $T|\psi\rangle=e^{iP}|\psi\rangle$. In a background flux φ, in the uniform gauge of Figure 1,

$$
H(\varphi)=\sum_{j=1}^{L}\Big[\frac J2\big(e^{i\varphi/L}S^+_{j+1}S^-_j+e^{-i\varphi/L}S^-_{j+1}S^+_j\big)+J\Delta\,S^z_jS^z_{j+1}\Big],\tag{4.1}
$$

where $J>0$, Δ is the anisotropy (Δ = 1 for the Heisenberg chain), and a hop from $j$ to $j+1$ picks up $e^{i\varphi/L}$, so the holonomy is $e^{i\varphi}$: the link phases of [[week-07-kogut-susskind-hamiltonian|Sem I Week 7]] frozen into a flat background, and the flux of Laughlin's argument. Every link carries the same phase, so $TH(\varphi)T^{-1}=H(\varphi)$ for all φ, and $Q$ is conserved.

```
                 e^{i phi/L}
          1 o --------------> o 2
           ^                   \
          /                     v
       6 o     phi (flux)        o 3
          ^                     /
           \                   v
          5 o <-------------- o 4
```
**Figure 1. The six-site ring in a flux φ, uniform gauge (4.1): each hop $j\to j+1$ of an up spin carries $e^{i\varphi/L}$, the holonomy is $e^{i\varphi}$, $H(\varphi)$ is translation invariant, and the twist $U$ of (4.2) maps $H(\varphi)$ to $H(\varphi+2\pi)$.**

The large gauge transformation is

$$
U=\exp\Big(\frac{2\pi i}{L}\sum_{j=1}^Lj\,n_j\Big),\tag{4.2}
$$

with $US^+_jU^{-1}=e^{2\pi ij/L}S^+_j$. On a link $(j,j+1)$ with $j<L$ the hop acquires $e^{2\pi i(j+1)/L}e^{-2\pi ij/L}=e^{2\pi i/L}$, and on $(L,1)$ it acquires $e^{2\pi i/L}e^{-2\pi i}=e^{2\pi i/L}$ as well, so

$$
UH(\varphi)U^{-1}=H(\varphi+2\pi),\tag{4.3}
$$

and the background is the holonomy $e^{i\varphi}$: a flux $2\pi$ is gauge trivial. Relabeling $k=j+1$, with the site $L+1\equiv1$ carrying weight $L$,

$$
TUT^{-1}=\exp\Big(\frac{2\pi i}L\sum_jj\,n_{j+1}\Big)=\exp\Big(\frac{2\pi i}L\Big[\sum_kk\,n_k-Q+Ln_1\Big]\Big)=U\,e^{-2\pi iQ/L},\tag{4.4}
$$

because $e^{2\pi in_1}=1$. The half-integer spin enters here: with $S^z_j$ in place of $n_j$ the boundary factor is $e^{2\pi iS^z_1}=-1$, and with $n_j$ the offset $L/2$ in $Q$ gives the same sign (Problem 3 treats spin $S$).

### 4.2 Flux threading [the operator steps Proved; the conclusion Heuristic; the theorems Stated — refs: LSM; Hastings]

Let $|\psi_0\rangle$ be a ground state of $H(0)$ with $Q=N$ and momentum $P_0$, and let φ grow slowly from 0 to $2\pi$. The evolution operator commutes with $T$ and $Q$, because every $H(\varphi)$ does, so the final state $|\psi_f\rangle$ has momentum $P_0$ and, if the evolution is adiabatic, is an eigenstate of $H(2\pi)$. By (4.3), $|\psi'\rangle=U^{-1}|\psi_f\rangle$ is an eigenstate of $H(0)=U^{-1}H(2\pi)U$ with the same energy, and by (4.4), $TU^{-1}=e^{2\pi iQ/L}U^{-1}T$, so

$$
T|\psi'\rangle=e^{2\pi iN/L}U^{-1}T|\psi_f\rangle=e^{i(P_0+2\pi\nu)}|\psi'\rangle,\qquad\nu=\frac NL.\tag{4.5}
$$

For $\nu\notin\mathbb{Z}$, $|\psi'\rangle$ has a different momentum and is orthogonal to $|\psi_0\rangle$. If $H(0)$ had a unique ground state with a gap that stays open along the path, $|\psi_f\rangle$ would be the ground state of $H(2\pi)$, $|\psi'\rangle$ that of $H(0)$, and $P_0+2\pi\nu=P_0$, a contradiction. So at fractional filling, for instance spins 1/2 at $S^z_{\rm tot}=0$, where ν = 1/2 and the shift is π, no unique ground state has a gap that survives the insertion. On a finite ring the gap closes along the path through a crossing of levels with different momenta (Figure 2). The physical input [Heuristic] is that a flux through a large ring is invisible to local operators, so in a gapped phase it moves the low-lying spectrum by an amount that vanishes as $L\to\infty$; then $|\psi'\rangle$ becomes a second ground state, and the system is gapless or degenerate. For $\nu=p/q$ in lowest terms, $q$ insertions give the momenta $P_0+2\pi\nu k$, $k=0,\dots,q-1$: a gapped phase has at least $q$ ground states. LSM proved the spin-1/2 statement without the adiabatic assumption (Problem 5⋆), and Hastings the higher-dimensional one [Stated — refs].

### 4.3 The six-site ring [Computed.]

For $L=6$, $J=\Delta=1$, $N=3$ (20 states with $S^z_{\rm tot}=0$) the ground state is unique, with $E_0=-\tfrac12(2+\sqrt{13})=-2.802776$ and $P_0=\pi$; the lowest $P=0$ level is $-\tfrac12(2+\sqrt5)=-2.118034$. As φ grows (Figure 2) the ground-state level rises to $-2.118034$ at $\varphi=2\pi$, the lowest $P=0$ level falls to $-2.802776$, and they cross at φ = π at $E=-2.56150$. Inside the $P=\pi$ sector the followed level stays at least $\tfrac12(\sqrt5-1)=0.618034$ below the next one, the minimum being reached at $2\pi$, so the evolution in the sector is adiabatic, and $U^{-1}|\psi_f\rangle$ has $P=0$ and energy $-2.118034$, the lowest $P=0$ eigenvalue of $H(0)$. We checked (4.3), (4.4) and $TH(\varphi)T^{-1}=H(\varphi)$ to machine precision for $L=4,6,8$, and the flow for the other sizes: for $L=4$ from $E_0=-2$ ($P_0=0$) to the $P=\pi$ level at $-1$, crossing at $-\tfrac12(1+\sqrt5)$; for $L=8$ from $-3.651093$ to $-3.128419$.

```
   phi/pi :     0        1/2        1        3/2        2
   P = pi :  -2.80278  -2.74037  -2.56150  -2.30104  -2.11803
   P = 0  :  -2.11803  -2.30104  -2.56150  -2.74037  -2.80278

     E
   -2.12 | o                                       x
   -2.30 |          o                     x
   -2.56 |                    ox
   -2.74 |          x                     o
   -2.80 | x                                       o
         +-------------------------------------------> phi
           0                  pi                  2 pi
     x : lowest P = pi level (the ground state at phi = 0)     o : lowest P = 0 level
```
**Figure 2. Spectral flow on the six-site Heisenberg ring at $S^z_{\rm tot}=0$: the flux $2\pi$ carries the ground state ($P=\pi$) to the lowest $P=\pi$ level of $H(2\pi)$, which $U^{-1}$ maps to the lowest $P=0$ level of $H(0)$; the crossing at φ = π is allowed because the momenta differ. Schematic plot; the numbers are exact to the digits shown.**

### 4.4 The anomaly as a phase of the partition function [Proved.]

Put the ring on a Euclidean torus with holonomy $e^{i\varphi}$ around space and a translation twist around time,

$$
Z_N(\varphi)=\operatorname{Tr}_{Q=N}\big(T\,e^{-\beta H(\varphi)}\big).\tag{4.6}
$$

From (4.4), $U^{-1}TU=e^{-2\pi iQ/L}T$, and with (4.3) and cyclicity

$$
Z_N(\varphi+2\pi)=\operatorname{Tr}_N\big(TUe^{-\beta H(\varphi)}U^{-1}\big)=\operatorname{Tr}_N\big(U^{-1}TU\,e^{-\beta H(\varphi)}\big)=e^{-2\pi i\nu}Z_N(\varphi).\tag{4.7}
$$

Gauge-equivalent backgrounds give partition functions that differ by $e^{-2\pi i\nu}$. A compensating counterterm would couple the spatial holonomy to the temporal translation twist, a factor $e^{ik\varphi}$ per unit of twist; it is a function of $e^{i\varphi}$ only for $k\in\mathbb{Z}$, and then contributes $e^{2\pi ik}=1$ to the ratio. Redefining $T$ or $U$ by functions of $Q$, or moving the origin of $j$ in (4.2), which multiplies $U$ by $e^{-2\pi ij_0Q/L}$, leaves (4.4) and (4.7) unchanged. The phase is a mixed anomaly of $U(1)$ and translation, labeled by ν mod 1. We checked (4.7) at β = 1 for $L=4,6,8$, where the ratio is $-1$.

### 4.5 Without $U(1)$: the odd ring [Proved; the theorem Stated — refs: OTT]

The π rotations $\mathbb{Z}_2\times\mathbb{Z}_2\subset SO(3)$, generated by $R_x=\prod_jX_j$ and $R_z=\prod_jZ_j$ (up to an irrelevant $i^L$), act on each site by (3.5), the nontrivial class of (3.9). Each site contributes one sign to the commutator, so

$$
R_xR_z=(-1)^LR_zR_x.\tag{4.8}
$$

For odd $L$ the Hilbert space carries the nontrivial class, and by §3.3 every $\mathbb{Z}_2\times\mathbb{Z}_2$-symmetric Hamiltonian, translation invariant or not, has an exactly doubly degenerate spectrum: on five sites with independent random symmetric two- and three-spin couplings on every bond all 32 levels pair exactly, while on six sites the same construction is generically nondegenerate. For even $L$ nothing is forced, and a chain with alternating bonds, whose two-spin unit cell carries the trivial class, can have a unique gapped ground state. With translation by one site, a projective class per unit cell forbids a unique gapped ground state of the infinite chain: the translation-invariant theorem of OTT, proved by operator-algebraic methods built on projective representations [Stated — refs]. Equation (4.8) is its finite-size face: one extra site inserts a unit of translation around space, and each unit carries one copy of the on-site class, as each flux $2\pi$ carries the momentum $2\pi\nu$ in (4.5) [Heuristic; reading the odd ring as a translation-twisted sector is the course's interpretation].

## 5. Inflow in the simplest case: the cluster chain

### 5.1 The chain and its symmetry [Proved.]

On a ring of even length $L$ put a qubit per site, with Pauli operators $X_j,Z_j$ (the $\sigma^x_j,\sigma^z_j$ of [[courses/generalized-symmetries-course/conventions|conventions]] §4), and take

$$
H_c=-\sum_jK_j,\qquad K_j=Z_{j-1}X_jZ_{j+1}.\tag{5.1}
$$

$K_j$ and $K_{j+1}$ overlap in two anticommuting pairs and commute, other pairs commute trivially, and $K_j^2=1$. The symmetry $\mathbb{Z}_2^a\times\mathbb{Z}_2^b$ is generated by

$$
U_a=\prod_{j\ {\rm odd}}X_j,\qquad U_b=\prod_{j\ {\rm even}}X_j .\tag{5.2}
$$

For odd $j$ the two $Z_{j\pm1}$ of $K_j$ sit on even sites, so $K_j$ commutes with $U_a$ and picks two signs under $U_b$; even $j$ is the same with $a\leftrightarrow b$. Each even site appears in the two $K_j$ with odd $j$ next to it, and the $Z$'s square away:

$$
\prod_{j\ {\rm odd}}K_j=U_a,\qquad\prod_{j\ {\rm even}}K_j=U_b.\tag{5.3}
$$

The ground state is the unique state with all $K_j=1$, the cluster state of Briegel and Raussendorf, with gap 2 and $U_a=U_b=1$. The symmetry acts on-site and linearly, so the closed chain has no anomaly; it is a symmetry-protected topological phase ([[spt-phases]]), whose content appears at a boundary.

### 5.2 The symmetry restricted to an open chain [Computed; the higher orders of perturbation theory Sketched]

Cut the ring between $L$ and 1:

$$
H_{\rm open}=-\sum_{j=2}^{L-1}K_j .\tag{5.4}
$$

The $L-2$ independent stabilizers on $L$ qubits leave a ground space of dimension 4, with gap 2. Four operators commute with every $K_j$ of (5.4),

$$
\Sigma^z_{\rm L}=Z_1,\quad\Sigma^x_{\rm L}=X_1Z_2,\qquad\Sigma^z_{\rm R}=Z_L,\quad\Sigma^x_{\rm R}=Z_{L-1}X_L,\tag{5.5}
$$

($X_1Z_2$ meets $K_2=Z_1X_2Z_3$ in two anticommuting pairs); each pair anticommutes and the left pair commutes with the right one, so they are the Pauli operators of two edge qubits. To restrict the symmetry, the method of Else and Nayak in its simplest case, use the exact identity $X_j=Z_{j-1}Z_{j+1}K_j$, $2\le j\le L-1$, for every odd $j\ge3$ in $U_a$, where the factors $Z_{j-1}Z_{j+1}$ telescope to $Z_2Z_L$ (Figure 3), and for every even $j\le L-2$ in $U_b$:

$$
U_a=(X_1Z_2)(Z_L)\prod_{j\ {\rm odd}\ \ge3}K_j,\qquad U_b=(Z_1)(Z_{L-1}X_L)\prod_{j\ {\rm even}\ \le L-2}K_j.\tag{5.6}
$$

```
   j     :   1      2      3      4      5      6      7      8
   U_a   :   X             X             X             X
   X_3   =          Z     K_3     Z
   X_5   =                        Z     K_5     Z
   X_7   =                                      Z     K_7     Z
   U_a   =  X_1 Z_2   x   K_3 K_5 K_7   x   Z_8         (Z_4^2 = Z_6^2 = 1)
           Sigma^x_L     (= 1 on the        Sigma^z_R
                          ground space)
```
**Figure 3. The telescoping (5.6) on eight sites: each bulk $X_j$ is traded for its stabilizer and two $Z$'s, which cancel in pairs, and one operator survives at each edge.**

On the ground space all $K_j=1$, and the symmetry is a product of edge operators,

$$
U_a=V_{\rm L}(a)V_{\rm R}(a),\ \ U_b=V_{\rm L}(b)V_{\rm R}(b),\qquad V_{\rm L}(a)=\Sigma^x_{\rm L},\ V_{\rm L}(b)=\Sigma^z_{\rm L},\ V_{\rm R}(a)=\Sigma^z_{\rm R},\ V_{\rm R}(b)=\Sigma^x_{\rm R}.\tag{5.7}
$$

At each edge $V(a)V(b)=-V(b)V(a)$: the left edge carries (3.5) exactly, the right edge the same class with $X$ and $Z$ exchanged, and the two signs cancel in $U_aU_b=U_bU_a$; the four ground states carry the charges $(\pm1,\pm1)$ once each. We checked (5.3), (5.5) and (5.6) as operator identities on eight sites, and (5.7) on the ground space.

Each edge is an anomalous quantum mechanics (§3.5), which protects it. A symmetric perturbation near the left edge generates, at orders well below $L/2$, an effective operator on the left qubit that commutes with $V_{\rm L}(a)$ and $V_{\rm L}(b)$, which generate all $2\times2$ matrices, so it is a multiple of the identity; only processes reaching across the chain split the doublets [Sketched; the general argument, with matrix-product states, is Sem II Week 7]. Adding the symmetric $-0.3\sum_jX_j-0.2\sum_jZ_jZ_{j+2}$ splits the four lowest levels by 0.217, 0.102, 0.048 and 0.023 for $L=6,8,10,12$, while $-0.1\,Z_1$, which breaks $\mathbb{Z}_2^a$, splits them by 0.200 at every $L$ [Computed by exact diagonalization].

### 5.3 The bulk response [Computed.]

The bulk partner of the edge class appears on the twisted ring. A $b$-twist between $L$ and 1 identifies $Z_{j+L}\equiv U_bZ_jU_b^{-1}$, which is $-Z_j$ on even sites; only $K_1=Z_0X_1Z_2$ contains such a $Z$ across the cut, with $Z_0\equiv-Z_L$, so $H^{(b)}_c=-\sum_{j\neq1}K_j+K_1$. Its unique ground state has $K_1=-1$, all other $K_j=1$, and by the operator identity (5.3) $U_a=-1$. The $a$-twist flips $K_L$ and gives $U_b=-1$: a $b$-defect carries $a$-charge and an $a$-defect carries $b$-charge. On the torus with holonomies $A$ of $\mathbb{Z}_2^a$ and $B$ of $\mathbb{Z}_2^b$ the low-temperature partition function is $\operatorname{Tr}_{H^{(b)}}(U_ae^{-\beta H})\to-e^{-\beta E_0}$ for $A$ around time and $B$ around space, the same with $a\leftrightarrow b$, and $+e^{-\beta E_0}$ when both run along the same cycle. This is the response

$$
Z_{\rm SPT}[A,B]=(-1)^{\sum_PA\cup B},\tag{5.8}
$$

with the cup product of [[courses/generalized-symmetries-course/conventions|conventions]] §8: for $A=1$ on the time links of one slice and $B=1$ on the space links of one column, $\sum_PA\cup B=-1$; for the reverse assignment, $+1$; with both holonomies in space, 0. We checked the three twisted rings on eight sites and the cup sums on a $4\times5$ torus. On a closed surface (5.8) is gauge invariant, since $A\cup(B+d\beta)=A\cup B-d(A\cup\beta)$ for closed $A$ (Leibniz, [[courses/generalized-symmetries-course/conventions|conventions]] §8).

### 5.4 Inflow as a cochain identity [Proved.]

The open chain lives on the cylinder $[0,L_x]\times S^1$, whose boundary is the two edge worldlines (Figure 4). For closed $A$ and $B\to B+d\beta$, the sum of $d(A\cup\beta)$ over the plaquettes reduces to the time links of the boundary circles, with $(A\cup\beta)(\ell)=A(\ell)\beta({\rm head}\,\ell)$, so

$$
\sum_P(A\cup d\beta)(P)=-\sum_Pd(A\cup\beta)(P)=-\sum_t\big[A_t(L_x,t)\beta(L_x,t+1)-A_t(0,t)\beta(0,t+1)\big],\tag{5.9}
$$

and, signs being irrelevant mod 2,

$$
Z_{\rm SPT}[A,B+d\beta]=(-1)^{\sum_tA_t(0,t)\beta(0,t+1)}(-1)^{\sum_tA_t(L_x,t)\beta(L_x,t+1)}Z_{\rm SPT}[A,B].\tag{5.10}
$$

The edge partition function is (3.10) with transition operators $M_t=e^{-\varepsilon H}V(a)^{A_t}V(b)^{B_t}$, later times to the left. Conjugating each by the gauge transformations at its ends, $M_t\to V(b)^{\beta_{t+1}}M_tV(b)^{\beta_t}$, leaves the trace unchanged, since neighbouring factors combine into $V(b)^{2\beta_{t+1}}=1$; moving $V(b)^{\beta_{t+1}}$ through $V(a)^{A_t}$ costs $c(b,a)^{A_t\beta_{t+1}}$, and what remains is $M_t$ at $B+d\beta$. Therefore

$$
Z_{\rm edge}[A,B+d\beta]=(-1)^{\sum_tA_t\beta_{t+1}}Z_{\rm edge}[A,B]\tag{5.11}
$$

for both edges, since $c(b,a)=-1$ in (5.7), and each boundary factor of (5.10) is cancelled by its edge:

$$
Z_{\rm SPT}[A,B]\,Z_{\rm edge,L}[A,B]\,Z_{\rm edge,R}[A,B]\ \text{is gauge invariant.}\tag{5.12}
$$

For $A\to A+d\alpha$ the same steps give $\sum_Pd\alpha\cup B=\sum_Pd(\alpha\cup B)$, with α at the tails of the boundary links. This is inflow in its simplest case: each edge is an anomalous $0+1$d theory, and its anomaly is the boundary variation of the $1+1$d SPT. We checked (5.9) and its $d\alpha$ partner for 200 random closed integer cochains on a $4\times5$ cylinder, and (5.11) for both edge orientations of (5.7) on about a hundred random backgrounds with trivial holonomies, since $Z_{\rm edge}$ vanishes otherwise (§3.3).

```
   x = 0                                              x = L_x
  edge L  .-------.-------.-------.-------.-------.  edge R
    ^     |       |       |       |       |       |    ^       time periodic
    |     .-------.-------.-------.-------.-------.    |
          |       |       |       |       |       |
          .-------.-------.-------.-------.-------.
           bulk weight (-1)^{sum_P A u B}; under B -> B + d beta it gains
           (-1)^{sum_t A_t(0,t)beta(0,t+1)} at edge L and (-1)^{sum_t A_t(L_x,t)beta(L_x,t+1)} at edge R
```
**Figure 4. Inflow on the cylinder: under $B\to B+d\beta$ the bulk weight (5.8) changes by one phase on each boundary circle, (5.10), each edge produces the same phase, (5.11), and the product (5.12) is invariant.**

For bosonic theories with finite $G$, the anomalies of $d$-dimensional theories and the SPT phases in $d+1$ dimensions are both described, in the group-cohomology construction, by $H^{d+1}(G,U(1))$ ((3.9) for $d=1$), and each SPT's boundary realizes the corresponding anomaly [Stated — refs: CGLW; Else–Nayak; Callan–Harvey for continuous symmetries and fermions]. Sem II Week 7 classifies the $1+1$d bulks by $H^2(G,U(1))$, with (5.6)–(5.7) as its explicit example.

## 6. Anomaly matching

### 6.1 The statement and the spectator argument [Model proof in $0+1$ dimensions; the general case Sketched]

**Anomaly matching.** If a local theory with symmetry $G$ and anomaly α is deformed by $G$-symmetric local terms, or flows under the renormalization group, with $G$ realized at every stage, the resulting theory has the same anomaly α.

In quantum mechanics this is immediate: if $H(\lambda)$ commutes with a fixed projective $U$ for all λ, every eigenspace carries the class (3.9) and every level is degenerate for every λ (§3.3), since the deformation never touches the $U(g)$ [Proved]. In field theory 't Hooft's argument adds a decoupled spectator sector $S$ with anomaly $\alpha^{-1}$. The total is anomaly free, so $G$ can be coupled to a dynamical gauge field with arbitrarily small coupling, and the gauged theory is consistent at every scale; in the infrared, gauge invariance requires the anomaly of the infrared sector to cancel that of $S$, which a free or topological spectator keeps fixed, so it is α [Sketched]. In the inflow form the spectator is the SPT of §5.4, and the flow acts locally on the boundary without changing the gapped bulk response [Sketched].

The spectator has an exact $0+1$d model [Proved]. The left edge qubit of §5.2 cannot be gauged (§3.5). A spectator qubit with the inverse class, here the same class, makes $X\otimes X$ and $Z\otimes Z$ commute, and the Gauss law $X\otimes X=Z\otimes Z=1$ has the unique solution $(|{\uparrow\uparrow}\rangle+|{\downarrow\downarrow}\rangle)/\sqrt2$. On the open cluster chain the right edge is the spectator of the left one: $U_a$ and $U_b$ commute because the two edge classes cancel through the bulk, (5.7).

### 6.2 What a nonzero anomaly allows [Proved, granting that a unique gapped ground state flows to an invertible theory]

If α ≠ 0 the infrared cannot be trivially gapped, with a unique ground state and a gap on every closed spatial manifold and $G$ unbroken: such a theory flows to an invertible theory, whose partition function $Z[A]=e^{iS_{\rm inv}[A]}$ is a local functional of the background, like (5.8), so its variation (2.1) is removed by the counterterm $S_{\rm ct}=-S_{\rm inv}$. Three options remain: (a) gapless, as the Heisenberg chain; (b) spontaneous breaking of part of the symmetry, as the Majumdar–Ghosh chain, whose ground states at momenta 0 and π break translation (Problem 7⋆), and the gauged $\mathbb{Z}_4$ chain of §6.3; (c) in $d\ge3$, topological order with fractionalized symmetry, the subject of Block 3. Matching constrains the infrared without fixing it; which option occurs depends on the couplings.

### 6.3 The $\mathbb{Z}_4$ chain of Sem II Week 4, recognized [the anomaly Stated — refs: Tachikawa; the signature Computed in Sem II Week 4]

In the gauged $\mathbb{Z}_4$ chain of [[sem2-week-04-gauging-backgrounds-and-dual-symmetry|Sem II Week 4]] §5.2 the residual $\mathbb{Z}_2$, generated by $U=\prod_iX_i$, and the dual $\mathbb{Z}_2$, generated by $W=\prod_iZ_{i+1/2}$, have a mixed anomaly because $0\to\mathbb{Z}_2\to\mathbb{Z}_4\to\mathbb{Z}_2\to0$ does not split [Stated — refs: Tachikawa], with the signature $U^2=\prod_iG_i=-1$ on the dual-twisted sector, (5.2) there. Note what is invariant. Inside that sector the sign could be absorbed by $U\to iU$, since $H^2(\mathbb{Z}_2,U(1))=0$, and $U$ commutes with $W$ there; what survives is the comparison between sectors, since $U$ is one operator, the same local formula on all of them, and $U^2$ is the gauge transformation $\prod_iG_i$, fixed on each sector by the Gauss law. A $1+1$d anomaly concerns the action of the symmetry across twisted sectors, which is why its classes are 3-cocycles, $H^3(G,U(1))$ for bosonic theories with finite $G$ [Stated — refs: CGLW; Else–Nayak], and Problem 4 checks at the soluble points that the gauged chain has no symmetric trivially gapped phase. In every case of this week one symmetry acts with a modified group law on the sector twisted by another (the commutator (3.4) on the edge qubit, the momentum shift (4.5) after a flux $2\pi$, the commutator (4.8) on the odd ring, $U^2=-1$ here), which is the viewpoint of Cheng and Seiberg.

## 7. Seminar: Oshikawa (2000), presented by the instructor

**Format.** The first seminar of Block 2, presented by the instructor as the model in the format of syllabus §7. Students read the letter and bring Problem 3.

**Sections.** The whole letter, *Phys. Rev. Lett.* 84 (2000) 1535, four pages.

**The technical claim.** For particles with a conserved number on a periodic lattice, in any dimension and for any interaction and statistics, a finite gap above a unique ground state is possible only when the number of particles per unit cell is an integer, and at $\nu=p/q$ a gapped phase has at least $q$ degenerate ground states; the argument combines the LSM construction with Laughlin's flux insertion.

**What it needs from Semester I.** Twisted sectors (Sem I Week 4 §3.4) and link phases as a gauge field (Sem I Week 7), with §§4.1–4.2 of this note.

**The step at the board.** The higher-dimensional (4.4)–(4.5): on an $L_x\times L_y$ torus, $U_x=\exp\big(\frac{2\pi i}{L_x}\sum_{\mathbf r}x\,n_{\mathbf r}\big)$ gives $T_xU_xT_x^{-1}=U_xe^{-2\pi iQ/L_x}=U_xe^{-2\pi i\nu L_y}$, a shift $2\pi\nu L_y$, so at $\nu=p/q$ the transverse size needs $\gcd(L_y,q)=1$ to produce $q$ distinct momenta.

**For the discussion.** Where the gap assumption enters (§4.2, F3) and how LSM (Problem 5⋆) and Hastings avoid it; in $d\ge3$ the $q$ states need not break any symmetry, which leads to Block 3.

**The open question it leaves for this course.** Constraints with no $U(1)$ to thread: the $\mathbb{Z}_2\times\mathbb{Z}_2$ case of §4.5 (OTT) and its inflow from $2+1$ dimensions (Problem 8⋆⋆).

**On the course map.** The anomaly is the failure of $Z$ to depend only on the classes of its backgrounds, (4.7); Sem II Week 6 finds the same failure for the $\mathbb{Z}_N^{(1)}$ background of Yang–Mills theory at θ = π.

## 8. Subtleties and fine print

**F1 — Not every sign is an anomaly.** $H^2(\mathbb{Z}_N,U(1))=0$: a projective representation of a cyclic group becomes linear after rephasing its generator. The π rotation of a spin 1/2 squares to $-1$, $(iX)^2=-1$, which alone means nothing; the anomaly of §4.5 is the commutator of two π rotations, the $\mathbb{Z}_2\times\mathbb{Z}_2$ face of the spin-1/2 class of $SO(3)$.

**F2 — Odd rings are exact, even rings need translation.** The degeneracy (4.8) needs no translation invariance, while on even rings the on-site class constrains only chains invariant under translation by one site (§4.5).

**F3 — The adiabatic assumption.** The conclusion of §4.2 needs the gap to stay open during the insertion in the thermodynamic limit, an assumption that LSM's variational state (Problem 5⋆) and Hastings's quasi-adiabatic continuation avoid [Stated — refs].

**F4 — Edge protection is symmetric.** Each $\mathbb{Z}_2$ alone is anomaly free, so a field breaking either one splits the edge doublets of §5.2 at first order; only the pair has $c(a,b)=-1$.

**F5 — Translation is not an internal symmetry.** The anomaly of §4 involves a spatial symmetry, which (4.6) treats as a twist in the trace and §4.5 through the length of the ring. Matching applies to its action on the low-energy theory, where lattice translation can act as an internal symmetry; Cheng and Seiberg analyze when and how [Stated — refs].

## 9. Common misconceptions

**"An anomalous symmetry is broken by quantum effects."** Tempting because the axial symmetry of QED is broken by its anomaly, which involves the dynamical gauge field. An 't Hooft anomaly concerns an exact global symmetry whose operators commute with the Hamiltonian; the obstruction appears only in coupling it to backgrounds or gauging it (§2).

**"A projective representation is a matter of phase conventions and can always be made linear."** Tempting because of (3.3). Rephasing removes only coboundaries; $c(a,b)$ is invariant (§3.1), and the class (3.5) forces the doublets of §3.3.

**"Lieb–Schultz–Mattis says that a chain of half-integer spins is gapless."** Tempting because the 1961 paper concluded that there is no gap, and the Heisenberg chain is gapless. The theorem excludes a unique gapped ground state; the gapped, doubly degenerate Majumdar–Ghosh chain is allowed (§6.2, Problem 7⋆).

## 10. Historical note

Lieb, Schultz and Mattis (1961) solved two models of an antiferromagnetic chain exactly by rewriting the spins as fermions, and showed, with the twist operator (4.2), that for spin-1/2 chains with rather general isotropic Heisenberg interactions the ground state is nondegenerate with no gap above it; that the low-lying twisted state may instead become a second ground state was understood later, and the chain Majumdar and Ghosh had solved in 1969 realizes it. 't Hooft formulated anomaly matching in his Cargèse lectures of 1979 (published 1980) to constrain massless composite fermions, which must reproduce the triangle anomalies of the global symmetries of their constituents; he argued by weakly gauging those symmetries, with spectator fermions cancelling the anomaly. Callan and Harvey (1985) showed that the anomalies of chiral zero modes on strings and domain walls are cancelled by a flow of charge from the bulk, the inflow of §5.4; Cheng and Seiberg review how the lattice constraints fit the same definition.

## 11. What to take away

1. **An anomaly is an obstruction modulo counterterms,** (2.1)–(2.2). The symmetry is exact; what fails is its coupling to backgrounds, and with it gauging.
2. **In quantum mechanics it is a projective class.** $H^2(\mathbb{Z}_2\times\mathbb{Z}_2,U(1))=\mathbb{Z}_2$, detected by the commutator phase (3.9); the nontrivial class forces two-dimensional irreducible representations (3.7) and doublets that no symmetric perturbation lifts (3.8).
3. **Lieb–Schultz–Mattis is a mixed anomaly.** Translation fails to commute with the large gauge transformation, (4.4): a flux $2\pi$ shifts the momentum by $2\pi\nu$, (4.5), and the torus partition function by $e^{-2\pi i\nu}$, (4.7); without $U(1)$ the on-site class does the same, (4.8). Physically, a half-filled ring remembers a flux quantum that no local probe sees.
4. **Inflow.** Restricted to an open cluster chain, the symmetry is a product of projective edge operators, (5.6)–(5.7), and the bulk response (5.8) varies on the boundary by exactly the edge phases, (5.10)–(5.12).
5. **Matching.** The anomaly survives symmetric deformations and renormalization (§6.1) and excludes a trivially gapped phase: the infrared is gapless, breaks a symmetry, or, for $d\ge3$, is topologically ordered (§6.2).

## 12. Looking ahead: Sem II Weeks 6 and 7

Sem II Week 6 turns on the $\mathbb{Z}_N^{(1)}$ background of four-dimensional Yang–Mills theory and finds at θ = π a phase of the type (4.7): with a 2-form background, θ → θ + 2π shifts the partition function by a fractional instanton number that no counterterm compatible with time reversal removes, and matching excludes a trivially gapped, time-reversal-invariant confining vacuum; Problem 6⋆ is its quantum-mechanical shadow. Sem II Week 7 turns §5 around: it classifies the $1+1$d bulks by $H^2(G,U(1))$ with matrix-product states, computes the AKLT edge doublet, and builds the $2+1$d Dijkgraaf–Witten theories, whose boundaries carry the $1+1$d anomalies $H^3$ of §6.3.

## 13. Problem set

*Routing: Problems 1–4 are the classroom core, 5⋆–7⋆ are self-study consolidation, and 8⋆⋆–9⋆⋆ are research extensions.*

### Core problems

**1. Projective representations of $\mathbb{Z}_N\times\mathbb{Z}_N$.** (Extends §§3.1–3.4.) Show that $H^2(\mathbb{Z}_N\times\mathbb{Z}_N,U(1))\cong\mathbb{Z}_N$, detected by $c(a,b)=e^{2\pi ik/N}$, with class $k$ realized by $U(a)=X$, $U(b)=Z^{-k}$ (clock and shift of [[courses/generalized-symmetries-course/conventions|conventions]] §4). Find the dimension of the irreducible representations of class $k$ and how many are inequivalent, and list them for $N=4$.

**2. π rotations of a spin $S$.** (Extends §4.5.) With $R_x=e^{i\pi S^x}$, $R_z=e^{i\pi S^z}$, compute $R_xR_zR_x^{-1}R_z^{-1}$ and $R_x^2$, and decide for which $S$ and ring lengths $L$ every $\mathbb{Z}_2\times\mathbb{Z}_2$-symmetric Hamiltonian has an exactly degenerate spectrum. What follows for a two-leg ladder of spins 1/2 with $L$ rungs?

**3. Flux threading at spin $S$ and magnetization $m$.** (Extends §§4.1–4.2.) For spins $S$, with $H(\varphi)$ of the form (4.1), $n_j=S^z_j+S$ and $m=S^z_{\rm tot}/L$, compute $TUT^{-1}$ and the momentum shift of the flux-threaded state. For which $(S,m)$ is a unique gapped ground state allowed? Apply this to $S=\tfrac12$ at $m=0$ and $m=\tfrac16$, to $S=1$ at $m=0$, and to $m=S$.

**4. The gauged $\mathbb{Z}_4$ chain obeys matching.** (Extends §6.3 with Sem II Week 4 §5.2.) For the gauged chain of Sem II Week 4 §5.2 on $L$ sites, find the physical ground states at $g=0$ and, to leading order, as $g\to\infty$, with their eigenvalues of $U$ and $W$. Show that neither limit is trivially gapped and say which $\mathbb{Z}_2$ is broken in each.

### Starred problems

**5⋆. The LSM variational state.** (Extends §4.2 without the adiabatic assumption.) For (4.1) at φ = 0 and $N=L/2$, show that $U^{\pm1}|\psi_0\rangle$ are orthogonal to $|\psi_0\rangle$ and that $\min_\pm\langle\psi_0|U^{\mp1}H(0)U^{\pm1}|\psi_0\rangle-E_0\le(1-\cos\frac{2\pi}L)|\langle H_{xy}\rangle_0|\le\pi^2J/L$, with $H_{xy}$ the hopping part of (4.1). *Hint:* $U^{-1}H(0)U=H(-2\pi)$ by (4.3); averaging the two signs cancels the terms in $\sin(2\pi/L)$, and $\|S^+_{j+1}S^-_j+{\rm h.c.}\|=1$. On six sites the left side is 0.934 and the bound 1.645.

**6⋆. The particle on a circle at θ = π.** (Extends §3 to a continuous symmetry; GKKS App. D.1.) For $H=\tfrac12(\Pi_q-\tfrac\theta{2\pi})^2$, $q\simeq q+2\pi$, with $E_n=\tfrac12(n-\tfrac\theta{2\pi})^2$, take at θ = π the shift $O_\alpha|n\rangle=e^{i\alpha n}|n\rangle$ and $C|n\rangle=|1-n\rangle$. Show that $O_\pi$ and $C$ generate the projective $\mathbb{Z}_2\times\mathbb{Z}_2$ of (3.5), so every level is doubly degenerate; that at θ = 0, with $C|n\rangle=|-n\rangle$, they commute and the ground state is unique; and that no rephasing makes the group generated by $O_\alpha$ and $C$ a linear representation of $O(2)$. *Hint:* $O_\pi C|n\rangle=(-1)^{1-n}|1-n\rangle$; for the last part restrict to the subgroup of the first.

**7⋆. The degenerate option: Majumdar–Ghosh.** (Extends §§4.2 and 6.2.) For $H_{\rm MG}=J\sum_j(\mathbf S_j\cdot\mathbf S_{j+1}+\tfrac12\mathbf S_j\cdot\mathbf S_{j+2})$ on an even ring, show that the dimer state $|D_1\rangle$ (singlets on $(1,2),(3,4),\dots$) and $|D_2\rangle=T|D_1\rangle$ are ground states with $E_0=-3JL/8$, that $T^2|D_1\rangle=|D_1\rangle$, and that $|D_1\rangle\pm|D_2\rangle$ have momenta 0 and π, the pair (4.5) predicts. *Hint:* $H_{\rm MG}=\frac J4\sum_j[(\mathbf S_j+\mathbf S_{j+1}+\mathbf S_{j+2})^2-\tfrac94]$; bound each triple by its spin-1/2 value. On six and eight sites the ground space is exactly two-dimensional, with gaps $0.500J$ and $0.405J$.

### ⋆⋆ problems

**8⋆⋆. The inflow of the LSM anomaly.** *Known:* a translation-invariant chain whose on-site symmetry acts projectively has no unique gapped ground state (OTT); lattice anomalies involving translation are captured by twisted Hilbert spaces (Cheng–Seiberg). *Explored:* a stack of cluster chains along $y$, each ending on the line $x=0$, puts one edge qubit with the class (5.7) per chain on that line, the on-site content of §4.5, with translation along the boundary acting as translation of the stack. Build the boundary symmetry operators from (5.6), recover (4.8) for an odd number of chains around a periodic $y$, and find the $2+1$d response that cancels the boundary anomaly. *Sources:* §§4.5 and 5; OTT; Cheng–Seiberg; Else–Nayak. *Completion:* an explicit two-dimensional model with its boundary operators, the twisted-sector computation on small lattices, and a cochain formula for the bulk response with a translation background, checked numerically.

**9⋆⋆. Flux threading in two dimensions.** *Known:* on an $L_x\times L_y$ torus the shift is $2\pi\nu L_y$ (§7), so at $\nu=p/q$ a gapped phase needs at least $q$ ground states when $\gcd(L_y,q)=1$ [Heuristic, Oshikawa; theorem, Hastings], and they need not break any symmetry. *Explored:* how the $q$ momenta relate to the torus degeneracy of a topological phase, for instance the $K$-matrix states of Sem II Week 10 with $|\det K|=q$. *Sources:* Oshikawa; Hastings; Sem II Weeks 8 and 10. *Completion:* for one gapped model at fractional filling, a check that the insertion permutes its torus ground states with momenta $P_0+2\pi\nu L_yk$, and what happens when $\gcd(L_y,q)\neq1$.

## Self-study answer checkpoints

**Problem 1.** *Decisive step:* $c$ is bimultiplicative (§3.1), so it is fixed by $c(a,b)$, with $c(a,b)^N=c(a^N,b)=1$; injectivity is the commutative-algebra argument of §3.4 unchanged. *Result:* $H^2\cong\mathbb{Z}_N$, $k\leftrightarrow e^{2\pi ik/N}$, realized by $X$, $Z^{-k}$, since $ZX=\omega XZ$ gives $XZ^{-k}=\omega^kZ^{-k}X$. Class $k$ has irreducible representations of dimension $n=N/\gcd(N,k)$, $\gcd(N,k)^2$ of them inequivalent: the $g$ with $c(g,h)=1$ for all $h$ form a subgroup of that order, and $n^2\gcd(N,k)^2=N^2$. For $N=4$: $k=0$, sixteen one-dimensional; $k=1,3$, one four-dimensional (the pair $X$, $Z^{-k}$ itself); $k=2$, four two-dimensional, $U(a)=i^sX$, $U(b)=i^tZ$ with Pauli matrices, $s,t\in\{0,1\}$, distinguished by $U(a)^2=(-1)^s$, $U(b)^2=(-1)^t$. On $\mathbb{C}^N$, $X$ and $Z^{-k}$ split into $\gcd(N,k)$ inequivalent irreducible pieces, the eigenspaces of the central $X^n$ (checked for $N=4,6$). *Common failure:* expecting dimension $N$ for every $k\neq0$, or taking $U(b)=Z^k$, which realizes the class $-k$.

**Problem 2.** *Decisive step:* $R_xS^zR_x^{-1}=-S^z$, so $R_xR_zR_x^{-1}=e^{-i\pi S^z}=e^{-2\pi iS^z}R_z=(-1)^{2S}R_z$. *Result:* $R_xR_zR_x^{-1}R_z^{-1}=(-1)^{2S}$ and $R_x^2=(-1)^{2S}$ (checked for $S=\tfrac12,1,\tfrac32,2$). On a ring the commutator is $(-1)^{2SL}$: exact degeneracy for every symmetric Hamiltonian if and only if $S$ is half-integer and $L$ odd; integer-spin rings and all even rings are unconstrained. A two-leg ladder has $2L$ spins and commutator $+1$, and each rung carries the trivial class, so §4.5 does not constrain translation along the ladder. *Common failure:* reading $R_x^2=-1$ for spin 1/2 as an anomaly (F1).

**Problem 3.** *Decisive step:* $n_1=S^z_1+S$ is an integer, so (4.4) holds unchanged with $Q=L(S+m)$. *Result:* the shift is $2\pi(S+m)\equiv-2\pi(S-m)$ mod $2\pi$, since $2S\in\mathbb{Z}$; a unique gapped ground state requires $S-m\in\mathbb{Z}$, and for $S-m=p/q$ in lowest terms a gapped phase has at least $q$ ground states. $S=\tfrac12$, $m=0$: π (§4.2); $S=\tfrac12$, $m=\tfrac16$: $4\pi/3$, at least three states (checked on six sites, $N=4$); $S=1$, $m=0$: no constraint, room for the gapped spin-1 chain of Sem II Week 7; $m=S$: no constraint, and the saturated state is unique. *Common failure:* writing (4.2) with $S^z_j$ and dropping the boundary factor $e^{2\pi iS^z_1}=e^{2\pi iS}$, which is where the half-integer spin enters.

**Problem 4.** *Decisive step:* at $g=0$ the energy $-2L$ requires $k_{i+1}-k_i\in\{0,2\}$ mod 4 on every bond with $Z_{i+1/2}=(-1)^{(k_{i+1}-k_i)/2}$; for each value of $k\bmod2$ the Gauss operators act freely and transitively on these $2^L$ configurations, leaving one physical state. *Result:* at $g=0$, two ground states at $E=-2L$, exchanged by $U$ ($k\to k+1$), with $W=+1$ on both because the bond differences add up to a multiple of 4: residual $\mathbb{Z}_2$ broken, dual unbroken. As $g\to\infty$, $E_0=-2gL$ at leading order, with all $X_i=1$ and, by the Gauss law with $X_i^2=1$, all link values $X_{i+1/2}$ equal: two states exchanged by $W$, with $U=+1$, so the dual $\mathbb{Z}_2$ is broken. On three sites the $g=0$ pair is exactly degenerate and the large-$g$ pair is split by $6.0\cdot10^{-4}$ at $g=50$, of order $g^{1-L}$. Neither limit is trivially gapped. *Common failure:* ignoring the Gauss law, which gives the four ground states of the ungauged $\mathbb{Z}_4$ ferromagnet at $g=0$ and the unique paramagnet as $g\to\infty$.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester II Block 2. Written to the note-quality-template standard on 2026-10-02. Last revised 2026-10-02.*
