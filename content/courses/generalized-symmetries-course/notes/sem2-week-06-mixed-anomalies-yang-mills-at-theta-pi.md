---
title: "Sem II Week 6 — Mixed Higher-Form Anomalies: Yang–Mills at θ = π"
type: lecture-notes
course: syllabus
semester: 2
week: 6
block: 2
duration: 4 hours (3 hr lectures + 1 hr seminar)
prerequisites: Sem II Weeks 1–5; Semester I Weeks 2, 6, 12 and 14
modified: 2026-10-02
---

# Sem II Week 6 — Mixed Higher-Form Anomalies: Yang–Mills at θ = π

> *Semester I left θ = π as a point of time-reversal symmetry where the Euclidean weight stops being positive ([[week-12-theta-terms-witten-effect|Sem I Week 12]]), and 't Hooft's twisted boundary conditions as the definition of flux sectors ([[week-14-fradkin-shenker-order-parameters|Sem I Week 14]]). This week they meet: a twist on the four-torus is a background for the center 1-form symmetry, in it the instanton number is fractional, and at θ = π the resulting phase is a mixed 't Hooft anomaly between the center symmetry and time reversal. We construct the twisted bundle by hand, define the Pontryagin square on the lattice, derive the anomaly and follow it to the vacuum at θ = π; Sem II Week 7 reads the counterterms as SPT phases.*

### How to use this chapter

- **In class:** in the first lecture derive the cocycle condition (2.5), build the SU(2) bundle (2.7) with Figure 1 and its half-instanton, (2.8)–(2.11), and prove (2.15) through (2.12)–(2.14); then the lattice Pontryagin square: the failure (3.1) with Figure 2, the product $\cup_1$ (3.2) with the model proof of (3.5), and (3.6)–(3.11). Problems 1 and 2. In the second lecture derive the anomaly, (4.2)–(4.7) with Figure 3, the matching argument (5.1)–(5.2) and its twisted-box form (5.3)–(5.5), and close with §6 and Figure 4; Problems 3 and 4. The seminar hour (§8) is Gaiotto–Kapustin–Komargodski–Seiberg.
- **For self-study:** §§3.5, 5.3, 9–10 and Problems 5⋆–7⋆. Mini-calculation 2 (§7) is handed in at the end of the week; the calculation to do alone is its Sub-task 2.
- **Instructor checkpoint:** two errors recur. The first is to take $\sum\tilde B\cup\tilde B$ as the anomaly for even N: it depends on the integer lift, by 2 mod 4 in the example of §3.1, and only the corrected square (3.6) is a function of [B]. The second is a confusion of maps: under T the counterterm moves as $p\to-p-(N-1)$, (4.6), and the label of an infrared vacuum as $p_{\rm IR}\to-p_{\rm IR}+N-1$, §5.1; mixing them assigns wrong labels to the vacua of §6.2. Behind both sits the slip of reading the anomaly as a proof that T breaks at θ = π; it removes one scenario of five (§6.1).

## 0. Reading

**Primary:** Gaiotto, Kapustin, Komargodski, Seiberg (GKKS), "Theta, time reversal and temperature", *JHEP* 05 (2017) 091 [arXiv:1703.00501], §1 (pp. 2–6), §§2.1–2.4 (pp. 6–13) and §2.6 (pp. 14–15): the seminar paper of §8.

**Secondary:** 't Hooft, "A property of electric and magnetic flux in non-Abelian gauge theories", *Nucl. Phys. B* 153 (1979) 141, §§2–5 and 8; 't Hooft, "Some twisted self-dual solutions for the Yang–Mills equations on a hypertorus", *Commun. Math. Phys.* 81 (1981) 267; Chen and Tata, *J. Math. Phys.* 64 (2023) 091902 [arXiv:2106.05274], §§IV–V, eqs. (20)–(29) and Figure 4; AST §§1–2 and 6.4. Earlier notes: Sem I Weeks 6, 12 and 14; [[sem2-week-02-zn-gauge-theory-as-bf-theory|Sem II Week 2]], [[sem2-week-04-gauging-backgrounds-and-dual-symmetry|Sem II Week 4]] §§2, 6, and [[sem2-week-05-thooft-anomalies-obstruction-as-physics|Sem II Week 5]], "'t Hooft Anomalies: Obstruction as Physics", §6.

**Optional research reading:** Witten, "Large N chiral dynamics", *Ann. Phys.* 128 (1980) 363, and "Theta dependence in the large N limit of four-dimensional gauge theories", *Phys. Rev. Lett.* 81 (1998) 2862 [hep-th/9807109]; GKKS §§3–7 and Appendix D; Kapustin and Seiberg, arXiv:1401.0740, to whom GKKS attribute the quantization of the counterterm and the Pontryagin square; Lüscher, "Topology of lattice gauge fields", *Commun. Math. Phys.* 85 (1982) 39.

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]]; signs and normalizations from [[courses/generalized-symmetries-course/conventions|conventions]] §§4, 6, 8 and 10. The note fixes three conventions, recorded in [[courses/generalized-symmetries-course/conventions|conventions]] §8 with it: the product $\cup_1$ (3.2) with its coboundary formula (3.5), the lattice Pontryagin square (3.6), and the B-coupled Wilson action (2.1).

## 1. Motivation and setting

At θ = 0 the vacuum of four-dimensional SU(N) Yang–Mills theory is believed to be the simplest possible: unique, gapped and confining. The strong-coupling expansion of [[week-06-wilson-action-strong-coupling|Sem I Week 6]] §4 gives the area law on the lattice, and simulations, whose weight is positive at θ = 0, support the picture in the continuum. The point θ = π is the other value at which the theory is invariant under time reversal, since T maps θ to −θ and θ is an angle (Sem I Week 12 §3), and there the weight $e^{i\pi Q}=(-1)^Q$ is indefinite. The vacuum at θ = π was therefore a question for models and for large N, where Witten's analysis predicts two degenerate vacua exchanged by T.

Gaiotto, Kapustin, Komargodski and Seiberg turned the question into a constraint. Pure Yang–Mills theory has a 1-form center symmetry ([[higher-form-symmetries]]; [[sem2-week-01-symmetries-are-topological-operators|Sem II Week 1]]) whose background is a $\mathbb{Z}_N$ 2-form gauge field B (Sem II Week 4 §2), and on the four-torus its nontrivial backgrounds are the twisted boundary conditions 't Hooft introduced in 1979. In such a background the instanton number is fractional and θ ∼ θ + 2π holds only up to a phase that depends on B; at θ = π the phase becomes an obstruction to coupling B while keeping T, a mixed 't Hooft anomaly ([[t-hooft-anomaly]]) in the sense of Sem II Week 5, and anomaly matching forbids a trivial vacuum.

Throughout, d = 4 is the Euclidean dimension, time is axis 1, and the center symmetry is the electric $\mathbb{Z}_N^{(1)}$ of [[courses/generalized-symmetries-course/conventions|conventions]] §6, exact in pure Yang–Mills theory and broken explicitly by fundamental matter.

## 2. The center background on $T^4$ and the fractional instanton number

### 2.1 Backgrounds and twisted boundary conditions [Proved.]

On the lattice the center symmetry couples to a background through $da-B$, as every $\mathbb{Z}_N$ symmetry does in Sem II Week 4 (2.2). For the Wilson action of [[courses/generalized-symmetries-course/conventions|conventions]] §4 this reads
$$
S_W[U,B]=\frac{\beta}{N}\sum_P{\rm Re}\,{\rm tr}\big(1-\omega^{-B_P}U_P\big),\qquad B\in Z^2(\Lambda,\mathbb{Z}_N),\tag{2.1}
$$
where $\omega=e^{2\pi i/N}$ and $U_P=U_\mu(x)U_\nu(x+\hat\mu)U_\mu(x+\hat\nu)^\dagger U_\nu(x)^\dagger$ is the plaquette of Sem I Week 6 §1.2. Under $U_\ell\to\omega^{\lambda_\ell}U_\ell$ the four links contribute the phases of $\partial P$ with the signs of [[courses/generalized-symmetries-course/conventions|conventions]] §1, $U_P\to\omega^{(d\lambda)_P}U_P$, so that
$$
U_\ell\to\omega^{\lambda_\ell}U_\ell,\qquad B\to B+d\lambda\tag{2.2}
$$
leaves (2.1) invariant and Z depends only on $[B]\in H^2(\Lambda,\mathbb{Z}_N)$: the center symmetry is an exact, local 1-form symmetry of the Wilsonian lattice (GKKS p. 7). The periods
$$
n_{\mu\nu}=\sum_{P\in T^2_{\mu\nu}}B_P\pmod N,\qquad n_{\nu\mu}=-n_{\mu\nu},\tag{2.3}
$$
label $H^2(T^4,\mathbb{Z}_N)\cong\mathbb{Z}_N^6$ (Sem I Week 2 §4), and our representative is the stack $B^{(n)}_{\mu\nu}(x)=n_{\mu\nu}\delta_{x_\mu,0}\delta_{x_\nu,0}$, one twisted plaquette in each (μν)-plane for every value of the transverse coordinates.

In the continuum the background is a boundary condition. On the box $0\le x_\mu\le L_\mu$ write $A^\Lambda\equiv\Lambda^\dagger A\Lambda-i\Lambda^\dagger d\Lambda$ for the gauge transformation of [[courses/generalized-symmetries-course/conventions|conventions]] §4, which composes as $(A^{\Lambda_1})^{\Lambda_2}=A^{\Lambda_1\Lambda_2}$, and demand
$$
A(x+L_\mu\hat\mu)=A^{\Omega_\mu(x)}(x)\tag{2.4}
$$
for four transition functions $\Omega_\mu\in SU(N)$, 't Hooft's twist matrices. Going round the corner of the (μν)-face in the two orders gives $A^{\Omega_\mu(x)\Omega_\nu(x+L_\mu\hat\mu)}$ and $A^{\Omega_\nu(x)\Omega_\mu(x+L_\nu\hat\nu)}$, and for generic A the two group elements can differ only by a central element. Thus
$$
\Omega_\mu(x)\,\Omega_\nu(x+L_\mu\hat\mu)=\omega^{n_{\mu\nu}}\,\Omega_\nu(x)\,\Omega_\mu(x+L_\nu\hat\nu),\tag{2.5}
$$
the cocycle condition, with antisymmetric twist $n_{\mu\nu}\in\mathbb{Z}_N$. A gauge transformation replaces $\Omega_\mu(x)$ by $\Lambda(x)^\dagger\Omega_\mu(x)\Lambda(x+L_\mu\hat\mu)$; in (2.5) the inner factors $\Lambda(x+L_\mu\hat\mu)\Lambda(x+L_\mu\hat\mu)^\dagger$ cancel, and n is gauge invariant. For n ≠ 0 the $\Omega_\mu$ define an SU(N)/$\mathbb{Z}_N$ bundle that is not an SU(N) bundle, and n is its 't Hooft flux, the class $w_2$ of Sem II Week 4 §6.2. The instanton number will see n through the Pfaffian
$$
\kappa\equiv{\rm Pf}(n)=n_{12}n_{34}-n_{13}n_{24}+n_{14}n_{23}=\tfrac14\,n_{\mu\nu}\tilde n_{\mu\nu},\qquad\tilde n_{\mu\nu}=\tfrac12\epsilon_{\mu\nu\rho\sigma}n_{\rho\sigma}.\tag{2.6}
$$
That (2.3) and (2.5) define the same n is checked in §3.5; in general a closed B is 't Hooft's twisted boundary condition [Stated — refs: GKKS p. 7, footnote 6].

### 2.2 The SU(2) bundle with κ = 1 [Computed.]

For SU(2), ω = −1. Take
$$
\Omega_1(x)=\exp\Big(\frac{i\pi x_2}{L_2}\,\sigma_3\Big),\qquad\Omega_3(x)=\exp\Big(\frac{i\pi x_4}{L_4}\,\sigma_3\Big),\qquad\Omega_2=\Omega_4=\mathbb 1 .\tag{2.7}
$$
Since $e^{i\pi\sigma_3}=-\mathbb 1$, $\Omega_1(x+L_2\hat e_2)=-\Omega_1(x)$, and (2.5) for (12) reads $\Omega_1(x)=-\omega^{n_{12}}\Omega_1(x)$, so $n_{12}=1$; (34) is the same computation, $n_{34}=1$. For (13) both matrices are diagonal and each is independent of the other's direction, so $n_{13}=0$; for (14) and (23) one matrix is $\mathbb 1$ and the other does not depend on the shifted coordinate, and (24) is trivial. The twist is $n_{12}=n_{34}=1$, κ = 1. As $x_2$ crosses the (12) face, $\Omega_1$ turns by half a period about $\sigma_3$ (Figure 1), and this half-turn is the twist.

```
          x2
     L2   +------------------------------------+
          |                                    |  Omega_1(x2) glues x1 = L1 to x1 = 0,
 Omega_2  |             the (12) face          |  turning from 1 (x2 = 0) to -1 (x2 = L2)
   = 1    |     A(x + L1 e1) = A^{Omega_1}(x)  |
      0   +------------------------------------+--> x1
          0                                    L1
     corner (2.5):  Omega_1(x) Omega_2(x+L1 e1) = (-1) Omega_2(x) Omega_1(x+L2 e2)
```
**Figure 1. The (12) face of the box for the bundle (2.7): the two ways round the corner differ by the center element −1, the twist n₁₂ = 1.**

The winding of (2.7) is forced [Proved.]. The anticommuting constant matrices $\Omega_1=i\sigma_1$, $\Omega_2=i\sigma_2$ realize $n_{12}=1$ with A = 0 (the SU(2) form of Sem I Week 14 §6.2), but four constant matrices cannot have κ odd. If two of them anticommute they are conjugate to $i\sigma_1,i\sigma_2$, and a matrix that commutes or anticommutes with both is, up to sign, one of $\mathbb 1,i\sigma_1,i\sigma_2,i\sigma_3$ (commuting with $\sigma_1$ means lying in the span of $\mathbb 1,\sigma_1$, anticommuting in that of $\sigma_2,\sigma_3$). Each $\Omega_\mu$ then has a class $v_\mu\in\mathbb{Z}_2^2$ with $n_{\mu\nu}=v^1_\mu v^2_\nu+v^2_\mu v^1_\nu$ mod 2; the matrix n has rank at most 2 over $\mathbb{Z}_2$, so ${\rm Pf}(n)^2=\det n\equiv0$ and κ is even (a script confirms all $4^4$ assignments).

### 2.3 The connection and Q = ½ [Computed.]

With the abelian connection
$$
A=\pi\sigma_3\Big(\frac{x_1\,dx_2}{L_1L_2}+\frac{x_3\,dx_4}{L_3L_4}\Big),\tag{2.8}
$$
$A(x+L_1\hat e_1)=A+(\pi/L_2)\sigma_3dx_2$ equals $\Omega_1^\dagger A\Omega_1-i\Omega_1^\dagger d\Omega_1=A-i(i\pi\sigma_3/L_2)dx_2$, since A commutes with $\Omega_1$; direction 3 works the same way, and A is independent of $x_2,x_4$, as $\Omega_2=\Omega_4=\mathbb 1$ requires. Since $A\wedge A=0$,
$$
F=dA+iA\wedge A=\pi\sigma_3\Big(\frac{dx^1\wedge dx^2}{L_1L_2}+\frac{dx^3\wedge dx^4}{L_3L_4}\Big),\tag{2.9}
$$
and in $F\wedge F$ only the cross terms survive, $F\wedge F=2\pi^2\,\mathbb 1\,d^4x/V$ with $V=L_1L_2L_3L_4$. With ${\rm tr}\,\mathbb 1=2$ and the conventions of [[courses/generalized-symmetries-course/conventions|conventions]] §10,
$$
Q=\frac1{8\pi^2}\int_{T^4}{\rm tr}\,F\wedge F=\frac1{8\pi^2}\cdot\frac{4\pi^2}{V}\cdot V=\frac12 .\tag{2.10}
$$
The action $S=\frac1{2g^2}\int d^4x\,{\rm tr}\,F_{\mu\nu}F_{\mu\nu}$, with ${\rm tr}\,F_{12}^2=2\pi^2/(L_1L_2)^2$ and ${\rm tr}\,F_{34}^2=2\pi^2/(L_3L_4)^2$ each counted twice, is
$$
S=\frac{2\pi^2}{g^2}\Big(r+\frac1r\Big),\qquad r=\frac{L_1L_2}{L_3L_4},\qquad S\ \ge\ \frac{4\pi^2}{g^2}=\frac{8\pi^2}{g^2}\,|Q| .\tag{2.11}
$$
At r = 1, $F_{12}=F_{34}$ and $F=\star F$: the configuration is self-dual, saturates the bound that follows from $\int{\rm tr}(F-\star F)^2\ge0$, and minimizes the action in its bundle. The twisted box thus contains a half-instanton with half the instanton action, a twisted self-dual solution of the constant-curvature kind 't Hooft wrote down in 1981. A sympy script checks (2.7)–(2.11): the six cocycle conditions, the four transition laws of A, Q and S.

> **Physical picture.** In a simulation of SU(2) with a closed background of odd κ, every configuration that can be smoothed has $Q\in\frac12+\mathbb{Z}$: the histogram of the topological charge is rigidly shifted by one half, an exact statement (§2.4). The cheapest such configuration costs $4\pi^2/g^2$, so semiclassically the twisted box is dominated by half-instantons, a heuristic that the anomaly does not use. Each configuration carries $e^{i\theta Q}=e^{i\theta/2}\times$(an integer power of $e^{i\theta}$), and the extra half is where periodicity in θ will fail.

### 2.4 The fractional part belongs to the twist [Model proof on $T^4$.]

First, Q does not depend on the connection within a bundle. Let $a=A'-A$, so that $a(x+L_\mu\hat\mu)=\Omega_\mu^\dagger a\,\Omega_\mu$, and $A_t=A+ta$. With $D_ta=da+i(A_t\wedge a+a\wedge A_t)$ we have $\partial_tF_t=D_ta$, the Bianchi identity $dF_t+i(A_t\wedge F_t-F_t\wedge A_t)=0$, and, moving $A_t$ cyclically through the trace with the signs of forms, $d\,{\rm tr}(a\wedge F_t)={\rm tr}(D_ta\wedge F_t)$. Therefore
$$
\partial_t\,{\rm tr}\,F_t\wedge F_t=2\,{\rm tr}\,(D_ta\wedge F_t)=2\,d\,{\rm tr}\,(a\wedge F_t),\tag{2.12}
$$
where ${\rm tr}(a\wedge F_t)$ is periodic, both factors transforming by conjugation; it integrates to zero, and $\partial_tQ_t=0$.

Second, bundles with the same twist have the same Q mod 1. Multiply the transition functions by central phases,
$$
\Omega'_\mu=e^{i\lambda_\mu}\,\Omega_\mu,\qquad\lambda_\mu(x)=\frac{2\pi}N\sum_{\nu>\mu}\frac{n_{\mu\nu}\,x_\nu}{L_\nu}.\tag{2.13}
$$
For μ < ν, $\lambda_\nu$ is independent of $x_\mu$ while $\lambda_\mu(x+L_\nu\hat\nu)=\lambda_\mu(x)+2\pi n_{\mu\nu}/N$, so the phases contribute $\omega^{-n_{\mu\nu}}$ to (2.5): the $\Omega'_\mu$, for any twisted $\Omega_\mu$, define a U(N) bundle E. The connection $A'=A+b\,\mathbb 1$ with $b=\frac{2\pi}N\sum_{\mu<\nu}n_{\mu\nu}x_\mu dx_\nu/(L_\mu L_\nu)$ obeys $b(x+L_\mu\hat\mu)=b+d\lambda_\mu$, as (2.4) with $\Omega'_\mu$ requires; then $F'=F+db\,\mathbb 1$ and $c_1(E)={\rm tr}\,F'/2\pi=N\,db/2\pi$ has the integer periods $n_{\mu\nu}$. The U(N) identity $\frac1{8\pi^2}\int{\rm tr}\,F'\wedge F'=\frac12\int c_1\wedge c_1-\int c_2$ with $c_2\in\mathbb{Z}$ [Stated — refs: GKKS (2.21)], ${\rm tr}\,F=0$ and $\frac N{8\pi^2}db\wedge db=c_1\wedge c_1/2N$ give
$$
Q=\frac1{8\pi^2}\int{\rm tr}\,F'\wedge F'-\frac N{8\pi^2}\int db\wedge db=\frac{N-1}{2N}\int_{T^4}c_1\wedge c_1-\int_{T^4}c_2 ,\tag{2.14}
$$
and with $\int c_1\wedge c_1=2\kappa$ (Sem I Week 12 §3.3 with fluxes $n_{\mu\nu}$),
$$
\boxed{\;Q\ \equiv\ \frac{(N-1)\,\kappa}{N}\ \equiv\ -\frac{\kappa}{N}\pmod 1\;}\tag{2.15}
$$
for every connection on every bundle with twist n. For N = 2, Q ≡ κ/2, realized by (2.10) with $c_2=0$. The general-N analogue of (2.8), with $\sigma_3/2$ replaced by $T={\rm diag}\big(\frac{N-1}N,-\frac1N,\dots,-\frac1N\big)$, has $c_2=0$ and $Q=(N-1)\kappa/N$ exactly (script for N = 2, 3, 4; Problem 1). In the language of §3, (2.15) is the $T^4$ value of
$$
Q\ \equiv\ \frac{N-1}{2N}\int_X\mathcal P(B)\pmod 1,\tag{2.16}
$$
since $\int_{T^4}\mathcal P(B)=2\kappa$ by (3.11); in this form it holds on every closed oriented four-manifold, with $c_1(E)$ in the role of GKKS's $dC/2\pi$ [Stated — refs: GKKS (2.18)–(2.22)]. For SU(2) the coefficient is the ¼ of the week: on $T^4$ the fraction is a half, and on $\mathbb{CP}^2$, with B the reduction of the hyperplane class, $\int\mathcal P(B)=1$ and Q ≡ ¼ [Stated — refs: Sem I Week 12 §3.3].

## 3. The Pontryagin square on the lattice

### 3.1 Why $B\cup B$ is not enough [Computed.]

The obvious lattice candidate for $\int\mathcal P(B)$ is $\sum\tilde B\cup\tilde B$, with $\tilde B$ an integer lift of B, defined up to $\tilde B\to\tilde B+Nu$, $u\in C^2(\Lambda,\mathbb{Z})$. Under this change
$$
\sum\tilde B'\cup\tilde B'-\sum\tilde B\cup\tilde B=N\sum\big(u\cup\tilde B+\tilde B\cup u\big)+N^2\sum u\cup u .\tag{3.1}
$$
For N odd, with the even counterterm coefficients of §4.2, this is harmless and $\sum\tilde B\cup\tilde B$ mod N suffices. For N even the middle term is N times an integer that can be odd, because the cubical cup product is not graded commutative on cochains ([[courses/generalized-symmetries-course/conventions|conventions]] §8). Take N = 2, the stack with $n_{12}=n_{34}=1$, and u the indicator of $P_{12}(0)$. In $u\cup\tilde B$ only the shuffle {1,2} pairs a 12-face with a 34-face, with u at the base corner and $\tilde B$ at the far corner, and $\sum u\cup\tilde B=u_{12}(0)\tilde B_{34}(\hat e_1+\hat e_2)=1$, since the 34-stack sits at $x_3=x_4=0$. In $\tilde B\cup u$ the shuffle {3,4} reads $\tilde B_{34}$ at $-\hat e_3-\hat e_4$, off the stack, and gives 0; $\sum u\cup u=0$ (Figure 2). The change is 2 ≢ 0 mod 4: $\sum\tilde B\cup\tilde B$ mod 4 is not a function of B. This is GKKS (2.8), repaired, after Kapustin and Seiberg, by the Pontryagin square.

```
   u ∪ B~ :  u_12 at the base corner 0,     B~_34 read at e1+e2    (on the stack)    ->  1
   B~ ∪ u :  u_12 at the far corner x+e3+e4, B~_34 read at -e3-e4  (off the stack)   ->  0

        x2 ^                                   x4 ^
         1 |  o e1+e2                           0 o--.---.---.--> x3     (34-stack at x3=x4=0)
         0 [u]--.---.--> x1                   -1   * -e3-e4
```
**Figure 2. The two orders of the cup product for the lift change of §3.1: the partner of u is read on the stack in one order and off it in the other, and the difference is the odd integer that spoils Σ B̃∪B̃ mod 4.**

### 3.2 The higher cup product $\cup_1$

Chen and Tata give the hypercubic $\cup_1$ in their eqs. (27)–(28), with factors ordered as in their ∪, which is ours with the factors exchanged ([[courses/generalized-symmetries-course/conventions|conventions]] §8). We translate with the same rule, $\alpha\cup_1\beta\equiv(-1)^{pq}\beta\cup_1^{\rm CT}\alpha$ for $\alpha\in C^p$, $\beta\in C^q$. On a (p+q−1)-cell (x;S) choose a direction $i\in S$ shared by the two faces and split $S\setminus\{i\}=A\sqcup C$, $|A|=p-1$, $|C|=q-1$: α lives on the face $\{i\}\cup A$, β on $\{i\}\cup C$. Directions before i are treated as in the cup product, those after i the opposite way; with $A_<=\{j\in A:j<i\}$ and $C_>=\{j\in C:j>i\}$,
$$
(\alpha\cup_1\beta)(x;S)=\sum_{i\in S}\ \sum_{A\sqcup C=S\setminus\{i\}}(-1)^{|C_>|}\,\epsilon\big(\{i\}\cup A,\,C\big)\ \alpha\big(x+\hat e_{C_>};\{i\}\cup A\big)\ \beta\big(x+\hat e_{A_<};\{i\}\cup C\big),\tag{3.2}
$$
where $\epsilon(\{i\}\cup A,C)$ is the sign of the sequence listing $\{i\}\cup A$ in increasing order and then C. The overall sign is the one for which Chen and Tata's recursion, their (29), holds (our reading of their rule (28) differs from it by −1, which the script detects). In low degrees, for μ < ν,
$$
(\alpha\cup_1\beta)(\ell_\mu(x))=\alpha_\mu(x)\beta_\mu(x),\quad(\alpha'\cup_1\beta)(P_{\mu\nu}(x))=\alpha'_{\mu\nu}(x)\big[\beta_\mu(x)+\beta_\nu(x+\hat\mu)\big],\quad(\alpha\cup_1\beta')(P_{\mu\nu}(x))=-\beta'_{\mu\nu}(x)\big[\alpha_\mu(x+\hat\nu)+\alpha_\nu(x)\big],\tag{3.3}
$$
for 1-cochains α, β and 2-cochains α′, β′, and for two 2-cochains on a cube, μ < ν < ρ,
$$
\begin{aligned}
(\alpha\cup_1\beta)(x;\mu\nu\rho)=\ &-\alpha_{\mu\nu}(x+\hat\rho)\beta_{\mu\rho}(x)+\alpha_{\mu\rho}(x+\hat\nu)\beta_{\mu\nu}(x)-\alpha_{\mu\nu}(x+\hat\rho)\beta_{\nu\rho}(x+\hat\mu)\\
&+\alpha_{\nu\rho}(x)\beta_{\mu\nu}(x)-\alpha_{\mu\rho}(x)\beta_{\nu\rho}(x+\hat\mu)+\alpha_{\nu\rho}(x)\beta_{\mu\rho}(x+\hat\nu),
\end{aligned}\tag{3.4}
$$
the six terms of Chen and Tata's Figure 4 (right) with the factors exchanged. The use of $\cup_1$ is the coboundary formula
$$
d(\alpha\cup_1\beta)=d\alpha\cup_1\beta+(-1)^p\,\alpha\cup_1d\beta+(-1)^{p+q-1}\,\alpha\cup\beta+(-1)^{pq+p+q}\,\beta\cup\alpha ,\tag{3.5}
$$
Chen and Tata's (29) in our ordering, with the same form. [Model proof for p = q = 1; general case Stated — refs: Chen–Tata Prop. 4, App. D; checked by script for every degree pair on random integer cochains in d = 3, 4, 5.] On $P_{\mu\nu}(x)$ write $a_1,\dots,a_4$ for α on $\ell_\mu(x),\ell_\nu(x+\hat\mu),\ell_\mu(x+\hat\nu),\ell_\nu(x)$ and $b_1,\dots,b_4$ for β. The left side is $a_1b_1+a_2b_2-a_3b_3-a_4b_4$. On the right, (3.3) gives $d\alpha\cup_1\beta=(a_1+a_2-a_3-a_4)(b_1+b_2)$ and $-\alpha\cup_1d\beta=(b_1+b_2-b_3-b_4)(a_3+a_4)$, and [[courses/generalized-symmetries-course/conventions|conventions]] §8 gives $-\alpha\cup\beta-\beta\cup\alpha=-(a_1b_2-a_4b_3)-(b_1a_2-b_4a_3)$; every product $a_ib_j$ with i ≠ j cancels, leaving the left side. For cocycles (3.5) gives $\alpha\cup\beta-(-1)^{pq}\beta\cup\alpha=(-1)^{p+q-1}d(\alpha\cup_1\beta)$, the sign now recorded in [[courses/generalized-symmetries-course/conventions|conventions]] §8.

### 3.3 The Pontryagin square [Proved, given (3.5).]

Let $\tilde B\in C^2(\Lambda,\mathbb{Z})$ lift a closed B, so $d\tilde B=Ny$ with $y\in C^3(\Lambda,\mathbb{Z})$, dy = 0. For N even define
$$
\mathcal P(\tilde B)=\tilde B\cup\tilde B+\tilde B\cup_1d\tilde B\ \in C^4(\Lambda,\mathbb{Z}_{2N}),\tag{3.6}
$$
and for N odd $\mathcal P(\tilde B)=\tilde B\cup\tilde B\in C^4(\Lambda,\mathbb{Z}_N)$: the Pontryagin square of the survival kit (§6). Three properties follow from (3.5).

(i) *Closed mod 2N.* Leibniz gives $d(\tilde B\cup\tilde B)=N(y\cup\tilde B+\tilde B\cup y)$, and (3.5) with (p,q) = (2,3) gives $d(\tilde B\cup_1d\tilde B)=N(Ny\cup_1y+\tilde B\cup y-y\cup\tilde B)$, so
$$
d\,\mathcal P(\tilde B)=2N\,\tilde B\cup y+N^2\,y\cup_1y\equiv0\pmod{2N}\qquad(N\ \text{even}).\tag{3.7}
$$
(ii) *Independent of the lift up to exact terms.* Under $\tilde B\to\tilde B+Nu$ the change is $N(u\cup\tilde B+\tilde B\cup u)+N\tilde B\cup_1du+Nu\cup_1d\tilde B$ plus multiples of $N^2$. With (3.5) for (p,q) = (2,2), $\tilde B\cup_1du=d(\tilde B\cup_1u)-d\tilde B\cup_1u+\tilde B\cup u-u\cup\tilde B$, and with $d\tilde B=Ny$,
$$
\Delta\mathcal P=N\,d(\tilde B\cup_1u)+2N\,\tilde B\cup u+N^2\big(u\cup u+u\cup_1du+u\cup_1y-y\cup_1u\big)\equiv N\,d(\tilde B\cup_1u)\pmod{2N}.\tag{3.8}
$$
In the example of §3.1, (3.5) summed over the torus gives $\sum\tilde B\cup_1du=\sum(\tilde B\cup u-u\cup\tilde B)=-1$: the $\cup_1$ term changes by −2 and absorbs the 2 of (3.1).

(iii) *Gauge invariant up to exact terms.* Under $\tilde B\to\tilde B+d\lambda$, Leibniz turns $d\lambda\cup\tilde B+\tilde B\cup d\lambda+d\lambda\cup d\lambda$ into $d(\lambda\cup\tilde B+\tilde B\cup\lambda+\lambda\cup d\lambda)+\lambda\cup d\tilde B-d\tilde B\cup\lambda$, and (3.5) for (p,q) = (1,3) gives $d\lambda\cup_1d\tilde B=d(\lambda\cup_1d\tilde B)+\lambda\cup d\tilde B+d\tilde B\cup\lambda$. Adding,
$$
\Delta\mathcal P=d\big(\lambda\cup\tilde B+\tilde B\cup\lambda+\lambda\cup d\lambda+\lambda\cup_1d\tilde B\big)+2N\,\lambda\cup y .\tag{3.9}
$$
On a closed lattice, therefore, $\sum\mathcal P(\tilde B)$ mod 2N is a function of [B], and for N odd the same steps show it for $\sum\tilde B\cup\tilde B$ mod N. The sign of the $\cup_1$ term is immaterial, the two choices differing by $2N\tilde B\cup_1y$. A script checks (3.7) on random lifts on a $2^5$ lattice, where $d\mathcal P$ is a genuine 5-cochain, and the invariance of $\sum\mathcal P$ mod 2N under random lifts and gauge transformations on $3^4$ for N = 2, 4, 6, while $\sum\tilde B\cup\tilde B$ mod 2N takes two values.

### 3.4 Evaluation on the four-torus [Computed.]

Each component of the stack is independent of the two transverse coordinates, so every term of $dB^{(n)}$ is a difference along a direction on which that component does not depend: $dB^{(n)}=0$ over $\mathbb{Z}$, and the $\cup_1$ term vanishes. On (x;1234) the cup product has six shuffles,
$$
\begin{aligned}
(B\cup B)(x;1234)=\ &B_{12}(x)B_{34}(x+\hat e_1+\hat e_2)-B_{13}(x)B_{24}(x+\hat e_1+\hat e_3)+B_{14}(x)B_{23}(x+\hat e_1+\hat e_4)\\
&+B_{23}(x)B_{14}(x+\hat e_2+\hat e_3)-B_{24}(x)B_{13}(x+\hat e_2+\hat e_4)+B_{34}(x)B_{12}(x+\hat e_3+\hat e_4),
\end{aligned}\tag{3.10}
$$
and for the stack each product is nonzero at exactly one site ($B_{12}(x)B_{34}(x+\hat e_1+\hat e_2)$ needs $x=0$, and so on). With §3.3 and the fact that closed cochains with equal periods differ by exact ones (Sem I Week 2 §4),
$$
\int_{T^4}\mathcal P(B)\equiv2\big(n_{12}n_{34}-n_{13}n_{24}+n_{14}n_{23}\big)=2\kappa\pmod{2N}\tag{3.11}
$$
for every closed B with periods n. The lattice Pontryagin square on $T^4$ is even, the cochain-level trace of $T^4$ being spin, and with (2.16) it returns (2.15). For N odd, $\sum\tilde B\cup\tilde B\equiv2\kappa$ mod N. The script reproduces (3.11) for random twists, lifts and gauge transformations (N = 2, 4, 6; odd N = 3, 5).

### 3.5 The half-instanton on the lattice [Computed.]

For SU(2), $\omega^{-1}\mathbb 1=e^{i\pi\sigma_3}$, and abelian links $U_\ell=e^{i\sigma_3\varphi_\ell}$ give in (2.1)
$$
\omega^{-B_P}U_P=\exp\big(i\sigma_3F_P\big),\qquad F=d\varphi+\pi\tilde B .\tag{3.12}
$$
On the $L^4$ lattice with the stack $n_{12}=n_{34}=1$, the constant cochain $F_{12}=F_{34}=\pi/L^2$ (others zero) is of this form, since $F-\pi\tilde B$ is closed with zero periods, so exact (Sem I Week 2); a least-squares solve produces φ with residual below $10^{-14}$. Its fluxes $\sum F=\pi$ through the 12- and 34-tori are those of (2.9), so the lattice stack and the continuum twist with the same n describe the same bundle. The lattice charge of Sem I Week 12 §6, applied to the Cartan field with ${\rm tr}\,\sigma_3^2=2$, is
$$
Q_{\rm lat}=\frac1{8\pi^2}\sum_x{\rm tr}\,(\sigma_3F\cup\sigma_3F)(x;1234)=\frac{2}{8\pi^2}\cdot L^4\cdot2\,\frac{\pi^2}{L^4}=\frac12\tag{3.13}
$$
for every L (script: L = 2, 3, 4), and $S_W=2\beta L^4(1-\cos(\pi/L^2))\to\beta\pi^2=4\pi^2/g^2$ for β = 4/g², the value (2.11) at r = 1. A general SU(N) lattice field has no topological charge without an admissibility condition (Lüscher 1982), and the course does not formulate the SU(N) θ-term on the lattice; the anomaly needs from the lattice only the dependence on B, which (3.6) supplies exactly.

## 4. The anomaly under θ → θ + 2π

### 4.1 The phase [Proved.]

With B turned on, the partition function sums over the bundles of §2 with the twist of B,
$$
Z_\theta[B]=\sum_{\text{bundles with twist }B}\int\mathcal DA\ e^{-S[A]}\,e^{i\theta Q[A]},\tag{4.1}
$$
with the weight and orientation of [[courses/generalized-symmetries-course/conventions|conventions]] §10. For B = 0 every Q is an integer and $Z_{\theta+2\pi}=Z_\theta$. For B ≠ 0 every configuration has $Q\in\frac{N-1}{2N}\int\mathcal P(B)+\mathbb{Z}$ by (2.16), so $e^{2\pi iQ}$ is one phase for all of them, and
$$
\boxed{\;Z_{\theta+2\pi}[B]=\exp\Big(\frac{2\pi i\,(N-1)}{2N}\int_X\mathcal P(B)\Big)\,Z_\theta[B].\;}\tag{4.2}
$$
On $T^4$ the phase is $\omega^{-\kappa}$: −1 for SU(2) with κ odd, $e^{-2\pi i\kappa/3}$ for SU(3).

### 4.2 Counterterms [Stated — refs: GKKS (2.9), (2.11), (2.20), after Kapustin–Seiberg.]

A phase that depends only on B could be absorbed by a local counterterm. The local functionals of B invariant under $B\to B+d\lambda$ are, apart from B-independent terms in the metric,
$$
Z_{\theta,p}[B]=Z_\theta[B]\,\exp\Big(\frac{2\pi i\,p}{2N}\int_X\mathcal P(B)\Big),\qquad p\in\mathbb{Z}_{2N}\ (N\ \text{even}),\quad p\in2\mathbb{Z}_{2N}\ (N\ \text{odd}),\tag{4.3}
$$
gauge invariant by §3.3; on spin manifolds only p mod N matters. By (4.2),
$$
Z_{\theta+2\pi,\,p}[B]=Z_{\theta,\,p+N-1}[B],\tag{4.4}
$$
GKKS (2.23): a shift of θ by 2π is a shift of the integer p by N − 1, and no choice of p makes the B-coupled family 2π-periodic.

### 4.3 Time reversal at θ = π: the mixed anomaly [Proved.]

Time reversal is the reflection $R:x_1\to-x_1$, an orientation-reversing isometry of $T^4$ (GKKS use CP, equivalent by CPT). Under $A\to R^*A$ the action is invariant, Q changes sign, and bundles with twist B go to bundles with twist $R^*B$, so
$$
Z_\theta[R^*B]=Z_{-\theta}[B],\qquad\int\mathcal P(R^*B)=-\int\mathcal P(B),\qquad Z_{\theta,p}[R^*B]=Z_{-\theta,-p}[B].\tag{4.5}
$$
At θ = 0 the choice p = 0 is T-invariant. At θ = π, (4.5) followed by (4.4) at θ = −π gives
$$
Z_{\pi,p}[R^*B]=Z_{-\pi,-p}[B]=Z_{\pi,\,-p-(N-1)}[B],\tag{4.6}
$$
and T-invariance requires $p\equiv-p-(N-1)$, that is,
$$
2p\equiv1-N\pmod{2N}.\tag{4.7}
$$
For N even the right side is odd and there is no solution, on spin manifolds (2p ≡ 1 mod N) either. No counterterm makes the B-coupled theory at θ = π invariant under T: this is the mixed 't Hooft anomaly between $\mathbb{Z}_N^{(1)}$ and time reversal (Figure 3). Each symmetry alone is fine, since B couples consistently and T is a symmetry at B = 0; the obstruction is to keeping both. For N odd, (4.7) is solved by p ≡ (N+1)/2 mod N on spin manifolds, and §5.3 extracts what survives. GKKS put $i\theta Q$ and the counterterm in the exponent with the same signs as (4.1) and (4.3), and their (2.22)–(2.23) are (4.4); their maps $p\to-p-1$, (2.10), and $p\to-p+N-1$, (2.24), follow from composing the 2π shift as $(\theta,p)\cong(\theta+2\pi,p+N-1)$, the inverse of their (2.23). For even N the conclusion is unchanged: for N = 2, (2.10) agrees with (4.6) mod 4, and (2.24) differs from it by 2, which only non-spin manifolds detect. For odd N their fixed point (2.13), p ≡ (N−1)/2 mod N (p = 4 for N = 3), is the infrared label $p_{\rm IR}$ of (5.2), and the T-invariant counterterm is p ≡ (N+1)/2.

```
      T at theta = 0 :  p -> -p      (mod 4)        T at theta = pi :  p -> -p - 1   (mod 4)
            0 -> 0   and   2 -> 2   fixed                 0 <-> 3,   1 <-> 2
            1 <-> 3                                       no fixed point
      theta -> theta + 2pi :  p -> p + (N - 1) = p + 1
```
**Figure 3. The counterterm label p ∈ ℤ₄ of SU(2) under time reversal: at θ = 0 the map fixes p = 0, 2; at θ = π the map (4.6) pairs the labels and fixes none, the anomaly (4.7).**

Summing over B at fixed p gives the PSU(N) theory with the discrete θ-angle p of AST (Sem II Week 4 §6.2), and (4.3) is the lattice form of that angle. By (4.4) its θ is no longer 2π-periodic (period 2πN on spin manifolds, GKKS p. 9; Problem 6⋆), and by (4.6) it is not T-invariant at θ = π for N even: gauging one member of an anomalous pair breaks the other (Sem II Week 5 §2).

## 5. Anomaly matching at θ = π

### 5.1 No trivially gapped, T-symmetric, confining vacuum [Proved, given §4.2.]

Suppose that at θ = π the theory (a) has a mass gap, (b) has a unique ground state on every spatial manifold, (c) confines, with the center symmetry unbroken and area laws for loops of nonzero N-ality ([[sem2-week-03-spontaneous-breaking-of-higher-form-symmetries|Sem II Week 3]] §2), and (d) does not break T: the properties of the vacuum at θ = 0. At long distances such a theory flows to an invertible field theory (Sem II Week 5 §6.2), a B-independent factor built from the metric times a local, 1-form gauge-invariant functional of B, which by §4.2 is
$$
\frac{Z_\pi[X,B]}{Z_\pi[X,0]}\ \longrightarrow\ \exp\Big(\frac{2\pi i\,p_{\rm IR}}{2N}\int_X\mathcal P(B)\Big),\qquad p_{\rm IR}\in\mathbb{Z}.\tag{5.1}
$$
Anomaly matching (Sem II Week 5 §6.1) requires the infrared to reproduce $Z_\pi[R^*B]=Z_{-\pi}[B]=e^{-2\pi i(N-1)\int\mathcal P(B)/2N}Z_\pi[B]$, from (4.5) and (4.2); with (5.1) this is $e^{-2\pi ip_{\rm IR}\int\mathcal P/2N}=e^{2\pi i(p_{\rm IR}-N+1)\int\mathcal P/2N}$ for every B, that is,
$$
2p_{\rm IR}\equiv N-1\pmod{2N},\tag{5.2}
$$
with no solution for N even. Therefore:
$$
\boxed{\;\text{for }N\text{ even, the vacuum of SU}(N)\text{ Yang–Mills theory at }\theta=\pi\text{ cannot be trivially gapped, T-symmetric and confining.}\;}
$$
Condition (5.2) is (4.7) with $p_{\rm IR}=-p$: adding the counterterm $-p_{\rm IR}$ would make the theory flow to the trivial, T-invariant theory, which is the spectator argument of Sem II Week 5 §6.1. Under T an infrared label moves as $p_{\rm IR}\to-p_{\rm IR}+N-1$, and a counterterm as in (4.6); the first map has the form of GKKS (2.24), for the reason given in §4.3.

### 5.2 The same argument in a twisted box [the degeneracy Proved; its infinite-volume reading Stated — refs: 't Hooft 1979 §§7–8.]

Take space to be the three-torus of axes 2, 3, 4 and read both twists from B: $k_a=n_{1,a+1}$ and $n_{a+1,b+1}=\epsilon_{abc}m_c$, so that $n_{34}=m_1$, $n_{42}=m_2$, $n_{23}=m_3$ and $\kappa=\vec k\cdot\vec m$. Inserting the center-symmetry operator with labels $\vec k$ in the trace over the Hilbert space $\mathcal H_{\vec m}$ with magnetic twist $\vec m$ is the temporal twist, and
$$
Z_\theta(\vec e,\vec m)=\frac1{N^3}\sum_{\vec k\in\mathbb{Z}_N^3}\omega^{-\vec k\cdot\vec e}\,Z_\theta[\vec k,\vec m]\tag{5.3}
$$
is 't Hooft's partition function at electric flux $\vec e$, Sem I Week 14 (6.2). Its $\vec m$ is minus the label of Sem I Week 14 §6.2, which couples the twist as $B_P\to\omega^{n_P}B_P$ where (2.1) has $\omega^{-B_P}U_P$, while the temporal label agrees; in Week 14's labels (5.4) below reads $Z_{\theta+2\pi}(\vec e,\vec m)=Z_\theta(\vec e-\vec m,\vec m)$ and (5.5) reads $Z_\pi(\vec e,\vec m)=Z_\pi(-\vec e+\vec m,\vec m)$. On $T^3\times S^1$, (4.2) reads $Z_{\theta+2\pi}[\vec k,\vec m]=\omega^{-\vec k\cdot\vec m}Z_\theta[\vec k,\vec m]$ and (4.5) reads $Z_\theta[-\vec k,\vec m]=Z_{-\theta}[\vec k,\vec m]$, R reversing the (1, a+1)-planes only, and (5.3) turns them into
$$
Z_{\theta+2\pi}(\vec e,\vec m)=Z_\theta(\vec e+\vec m,\vec m),\qquad Z_{-\theta}(\vec e,\vec m)=Z_\theta(-\vec e,\vec m),\tag{5.4}
$$
the first being the Witten effect for fluxes, with the direction of the dyon relabelling of [[courses/generalized-symmetries-course/conventions|conventions]] §10. At θ = π the two combine into
$$
Z_\pi(\vec e,\vec m)=Z_\pi(-\vec e-\vec m,\vec m),\tag{5.5}
$$
exact at every volume and temperature. For N even and $\vec m$ with an odd component, $\vec e\equiv-\vec e-\vec m$ has no solution: every level of $\mathcal H_{\vec m}$ is degenerate with a level of different electric flux. Properties (a)–(d) forbid this: (5.1) gives $Z[\vec k,\vec m]\propto\omega^{p_{\rm IR}\vec k\cdot\vec m}$, supported by (5.3) on the single sector $\vec e=p_{\rm IR}\vec m$ (other sectors cost σ|e|L in 't Hooft's analysis of confinement), and (5.5) then needs $p_{\rm IR}\vec m\equiv-(p_{\rm IR}+1)\vec m$, which is (5.2) mod N.

> **Physical picture.** Put SU(2) at θ = π in a box with $\vec m=(0,0,1)$. Equation (5.5) pairs the eight flux sectors as $\vec e\leftrightarrow\vec e+\vec m$, with identical spectra at any size: an exact twofold degeneracy enforced by the anomaly. If T is spontaneously broken, the sectors $\vec e=0$ and $\vec e=\vec m$ are lowest and the rest rise like σL, while the untwisted box shows the two vacua only as a splitting that closes exponentially in the volume; if the center symmetry breaks, all eight sectors approach degeneracy. The finite-volume statement is exact, the large-L patterns are expectations, and the sign problem of $e^{i\pi Q}$ makes the test hard to run.

### 5.3 Odd N: the global inconsistency [Proved.]

For N odd, (5.2) is solved by $p_{\rm IR}\equiv\frac{N-1}2$ mod N on spin manifolds, while T at θ = 0 requires $p_{\rm IR}=0$. An integer label cannot change without a phase transition, so if the vacua at θ = 0 and θ = π are both trivially gapped and T-invariant, a transition separates them in (0, π): the global inconsistency of GKKS §2.3, "almost as good as saying that there is an anomaly". In the twisted box the ground state of $\mathcal H_{\vec m}$ would move from $\vec e=0$ to $\vec e=\frac{N-1}2\vec m$ ($\vec e=\vec m$ for N = 3).

## 6. The infrared at θ = π

### 6.1 The allowed scenarios [the matching Proved; the dynamics Stated — refs: GKKS §§1.1, 2.2, 2.6, 7.]

For N even the phases that can carry the anomaly are those GKKS list in §2.2.

(i) *T spontaneously broken:* two trivially gapped, confining vacua exchanged by T, with labels related by the infrared map, $p_2=-p_1+N-1$; the pair matches the anomaly. The transition at θ = π is first order, and the domain wall, across which $p_{\rm IR}$ jumps by N − 1, carries a three-dimensional theory with an anomalous $\mathbb{Z}_N$ 1-form symmetry, conjectured by GKKS (§2.6) to be SU(N)₋₁ Chern–Simons theory. In the twisted box the vacua are the sectors $\vec e=0$ and $\vec e=-\vec m$.

(ii) *Center symmetry broken (deconfinement) with T unbroken:* the infrared is a $\mathbb{Z}_N$ gauge theory, the BF theory of Sem II Week 2, whose B-dependence is not of the form (5.1) (GKKS §7).

(iii) *Gapless:* a conformal or Coulomb phase (GKKS mention one for SU(2)); the two-dimensional $\mathbb{CP}^{n-1}$ model at θ = π (their §1.1) realizes (i) for n > 2 and (iii) for n = 2.

(iv) *Topological order* with T and $\mathbb{Z}_N^{(1)}$ unbroken, a TQFT on which the symmetries act (GKKS footnote 7).

For N odd the same list applies, with the transition of §5.3 as a further option. GKKS reach (i) by assuming that the theory is gapped for all θ, and warn that the assumption may fail for small N, especially N = 2 (footnote 1).

### 6.2 The large-N check [the branches Stated — refs: Witten 1980, 1998; their consequences Computed.]

At large N, θ enters the vacuum energy through θ/N, $E(\theta)=N^2h(\theta/N)$, and 2π-periodicity is restored by branches,
$$
E(\theta)=\min_kE_k(\theta),\qquad E_k(\theta)=N^2h\Big(\frac{\theta+2\pi k}{N}\Big)=\frac\chi2\,(\theta+2\pi k)^2+O(1/N^2),\tag{6.1}
$$
with $\chi=\langle Q^2\rangle/V$ at θ = 0 of order $N^0$ [Stated — refs: Witten, *Ann. Phys.* 128 (1980) 363; *Phys. Rev. Lett.* 81 (1998) 2862]. Four consequences check §§4–6.1 (Figure 4).

(a) At θ = π, $E_0=E_{-1}=\pi^2\chi/2$ and every other branch lies at least $4\pi^2\chi$ higher; T maps $\theta+2\pi k$ to $\theta+2\pi(-k-1)$ at θ = π and exchanges the two: scenario (i).

(b) With $Z=e^{-VE}$, $\langle Q\rangle/V=iE'(\theta)=i\chi(\theta+2\pi k)$ jumps from $i\pi\chi$ to $-i\pi\chi$ across π: a T-odd order parameter.

(c) Branch k at θ is branch 0 at θ + 2πk, so by (4.2) its label is $p_k=-k(N-1)\equiv k$ mod N. The vacua at θ = π have $p_0=0$, $p_{-1}=N-1$, exchanged by $p\to-p+N-1$: the large-N vacua match the anomaly.

(d) By (5.4) the ground state of $\mathcal H_{\vec m}$ in branch k has $\vec e=k\vec m$, and the screened line is (k, 1), the 't Hooft line (0, 1) relabelled |k| times by [[courses/generalized-symmetries-course/conventions|conventions]] §10: across θ = π the screened line switches from (0, 1) to (−1, 1), the non-abelian counterpart of the switch of condensates of Sem I Week 12 §7.3.

```
 E(θ)
   |                  *                       *
   |                 * *                     * *
   |                *   *                   *   *
   |               *     *                 *     *
   |              *       *               *       *
   |*           **         **           **         **           *
   | **       **             **       **             **       **
   |   *******                 *******                 *******
   +------+-----------+-----------+-----------+-----------+------> θ
         -2π         -π           0           π          2π
 branch       k = 1   |       k = 0           |   k = -1
 IR label     p = 1   |       p = 0           |   p = N-1
 flux in H_m  e = m   |       e = 0           |   e = -m
 screened     (1,1)   |       (0,1)           |   (-1,1)
```
**Figure 4. The large-N vacuum energy (6.1), the lower envelope of the branches. At its cusps the vacuum switches branch, and with it the infrared label, the flux of the twisted-box ground state and the screened line.**

## 7. Mini-calculation 2 (hand-in)

### 7.1 Scope

Exact on $T^4$ and on finite hypercubic tori, using §§2–5 and [[courses/generalized-symmetries-course/conventions|conventions]] §§1, 4, 8, 10. Nothing is claimed about dynamics: Sub-task 3 only translates each scenario of §6.1 into a twisted-box signature. The $\mathbb{CP}^2$ value is imported from §2.4.

### 7.2 Variable dictionary

| symbol | meaning | defined in |
|---|---|---|
| $n_{\mu\nu}$, κ | twist (periods of B), its Pfaffian | (2.3), (2.5), (2.6) |
| $\Omega_\mu$ | twist matrices | (2.4) |
| $\tilde B$, u, λ | integer lift, change of lift, gauge parameter | §3.3 |
| $\cup_1$, $\mathcal P$ | higher cup product, Pontryagin square | (3.2), (3.6) |
| p, $p_{\rm IR}$ | counterterm label, infrared label | (4.3), (5.1) |
| $\vec k,\vec m,\vec e$ | temporal twist, magnetic twist, electric flux | (5.3) |

### 7.3 Sub-tasks

**Sub-task 1: the other SU(2) twists.** (a) For $n_{13}=n_{24}=1$ take $\Omega_1=e^{i\pi x_3\sigma_3/L_3}$, $\Omega_2=e^{i\pi x_4\sigma_3/L_4}$, $\Omega_3=\Omega_4=\mathbb 1$; verify the six conditions (2.5), build the abelian connection, compute F, Q and S. (b) For $n_{12}=1$ take $\Omega_1=i\sigma_1$, $\Omega_2=i\sigma_2$, $\Omega_3=\Omega_4=\mathbb 1$ and A = 0. *Deliverable:* the six $\omega^{n_{\mu\nu}}$ in each case, A, F, Q, S and the (anti-)self-duality condition. *Checkpoint:* (a) κ = −1, Q = −½, $S=\frac{2\pi^2}{g^2}(r'+1/r')$ with $r'=L_1L_3/(L_2L_4)$, anti-self-dual with $S=4\pi^2/g^2$ at r′ = 1; (b) Q = S = 0, a flat connection with twist, allowed because κ = 0 (§2.2).

**Sub-task 2: the lattice.** Implement d, ∪ and $\cup_1$ (3.2) on the $3^4$ torus. (a) Verify Leibniz and (3.5) on random integer cochains for all p + q ≤ 4. (b) For N = 2 compute $\sum\mathcal P(\tilde B)$ mod 4 for the 64 classes $n\in\mathbb{Z}_2^6$, each with three random lifts $B^{(n)}+d\lambda+2u$, and $\sum\tilde B\cup\tilde B$ mod 4 for the same lifts. (c) Build (3.12) and compute $Q_{\rm lat}$ and $S_W/\beta$. *Deliverable:* the residuals, the histogram of $\sum\mathcal P$ mod 4, the numbers of (c). *Checkpoint:* all residuals exactly 0; $\sum\mathcal P\equiv2\kappa$ mod 4 for every lift, 28 classes at 2 (κ odd) and 36 at 0; $\sum\tilde B\cup\tilde B$ mod 4 takes both values for some classes; $Q_{\rm lat}=0.5$ and $S_W/\beta=162(1-\cos(\pi/9))=9.7698$, against $\pi^2=9.8696$.

**Sub-task 3: the anomaly and the vacuum of SU(2) at θ = π.** (a) From (4.2) and (3.11), tabulate $Z_{\theta+2\pi}[B]/Z_\theta[B]$ for the 64 classes, and give it for $\int\mathcal P(B)=1$. (b) Write the maps $p\to-p$ (θ = 0) and $p\to-p-1$ (θ = π) on $\mathbb{Z}_4$ as permutations, and on $\mathbb{Z}_2$ (spin manifolds). (c) For $\vec m=(0,0,1)$ list the pairs of flux sectors identified by (5.5) and the large-L pattern of nearly degenerate sectors in $\mathcal H_{\vec m}$ and $\mathcal H_0$ for scenarios (i)–(iv). *Deliverable:* the table, the permutations, the pairing and one paragraph. *Checkpoint:* (a) −1 for the 28 classes with κ odd, +1 otherwise, i for $\int\mathcal P=1$; (b) (0)(2)(1 3) and (0 3)(1 2) on $\mathbb{Z}_4$, the identity and (0 1) on $\mathbb{Z}_2$; (c) {(0,0,0),(0,0,1)}, {(1,0,0),(1,0,1)}, {(0,1,0),(0,1,1)}, {(1,1,0),(1,1,1)}; T broken: $\vec e=0$ and $\vec e=\vec m$ lowest and exactly degenerate, two states in $\mathcal H_0$ split exponentially in the volume; center broken: all eight sectors nearly degenerate.

### 7.4 What is proved, modeled and imported

Proved on $T^4$ and finite tori: (2.5), (2.12)–(2.15), (3.5) for p = q = 1 and §3.3 given (3.5), (4.2), (4.4)–(4.7), (5.2), (5.4)–(5.5). Computed: (2.10)–(2.11), (3.11), (3.13) and the sub-task tables. Imported: $c_2\in\mathbb{Z}$, the general case of (3.5), the classification of §4.2, the flow of a unique gapped vacuum to an invertible theory, the large-N branches and the energetics of flux sectors.

## 8. Seminar: Gaiotto–Kapustin–Komargodski–Seiberg §§1–2

**Format.** As in [[sem2-week-04-gauging-backgrounds-and-dual-symmetry|Sem II Week 4]] §8 ([[courses/generalized-symmetries-course/syllabus|syllabus]] §7): the presenter states the technical claim, identifies what it needs from Semester I and reproduces one nontrivial step at the board; discussion follows, and the instructor places the result on the course map. Every student reads the sections and brings Problem 3.

**Sections.** GKKS §1 with §1.1 (pp. 2–5), §§2.1–2.4 (pp. 6–13), §2.6 (pp. 14–15), and Appendix D.1 (from p. 40), the quantum-mechanical model of the phenomenon.

**The technical claim.** At θ = π, SU(N) Yang–Mills theory with N even has a mixed anomaly between the center symmetry and CP, (2.7)–(2.10); for N odd there is a global inconsistency (§2.3); the vacuum at θ = π is not a trivial non-degenerate gapped state, for N odd under the further assumption that no transition occurs in (0, π), the vacuum at θ = 0 being trivial.

**What it needs from Semester I.** Sem I Weeks 6, 12 and 14 §6, and Sem II Weeks 2, 4 and 5.

**The step at the board.** GKKS §2.4, (2.16)–(2.23): the U(N) embedding with NB = dC and the shift p → p + N − 1, set against (2.13)–(2.14), where $c_1(E)$ plays the role of $dC/2\pi$.

**For the discussion.** (a) GKKS §2.2, where θ → θ + 2π maps the line (0, 1) to (1, 1) and the counterterm (2.7) lets the attached surface shrink, against (5.4). (b) GKKS (2.8) against §3.1. (c) The $\mathbb{CP}^{n-1}$ analogy of §1.1. (d) Footnote 6: 't Hooft's twist carries CP charge, the content of (5.5).

**The open question it leaves for this course.** The Wilsonian lattice carries the center symmetry exactly (p. 7), but neither the θ-term nor time reversal at θ = π is realized on it here; whether a lattice regularization exhibits the anomaly exactly, with $\mathcal P(B)$ as the counterterm, is Problem 8⋆⋆.

**On the course map.** The background is Block 1's, the obstruction Sem II Week 5's in its first higher-form instance, and the counterterm a four-dimensional SPT phase (Sem II Week 7).

## 9. Subtleties and fine print

**9.1 Spin structure.** On $T^4$, and on any spin four-manifold, $\int\mathcal P(B)$ is even, p is defined mod N and (4.2) is a power of ω. The even-N anomaly survives the restriction (2p ≡ 1 mod N has no solution), so the torus sees the full obstruction; on non-spin manifolds p lives in $\mathbb{Z}_{2N}$ and for SU(2) the phase can be i.

**9.2 Both twists are needed.** A spatial twist alone has no Pfaffian, and $H[\vec m]$ is T-symmetric at θ = π. The anomaly lives in $\kappa=\vec k\cdot\vec m$, when the center operator is inserted in the trace: T maps its eigenvalue $\vec e$ to $-\vec e-\vec m$, (5.5).

**9.3 Finite volume.** The exact degeneracy (5.5) holds in twisted sectors only. In $\mathcal H_0$ the sector $\vec e=0$ is T-invariant, and even with T broken in infinite volume the two lowest states of the untwisted box are split by tunnelling; a numerical search should look at $\mathcal H_{\vec m}$ with $\vec m$ odd.

**9.4 Cochains versus integrals.** By (3.8)–(3.9) only $\sum\mathcal P$ over a closed lattice is a function of [B]; across a domain wall the exact terms contribute, which is how a wall carries an anomalous 1-form symmetry (§6.1(i)).

**9.5 The center symmetry must be exact.** Fundamental matter breaks $\mathbb{Z}_N^{(1)}$ ([[courses/generalized-symmetries-course/conventions|conventions]] §6), B cannot be coupled, and §5 disappears. Adjoint matter keeps it: GKKS §2.5 follow the anomaly into softly broken $\mathcal N=1$ super-Yang–Mills theory.

**9.6 T, CP and the sign of B.** Whether T acts as $B\to R^*B$ or as $B\to-R^*B$ is immaterial, since $\mathcal P(-B)=\mathcal P(B)$, which also makes (2.15) and (3.11) insensitive to the sign with which a lattice twist is matched to (2.5).

## 10. Common misconceptions

**"The anomaly proves that T is spontaneously broken at θ = π."** Tempting, because large N, softly broken supersymmetry and the two-dimensional analogue all break T. The anomaly excludes the trivially gapped, T-symmetric, confining phase and leaves deconfinement, gaplessness and topological order (§6.1); T-breaking is the dynamical expectation, open for SU(2).

**"The fractional instanton number means that SU(N) Yang–Mills theory is not 2π-periodic in θ."** Tempting, because Q ∉ ℤ in twisted bundles. The SU(N) theory sums over SU(N) bundles, where Q is an integer, and its spectrum is 2π-periodic; the fractions appear in the background B and make periodicity projective, (4.4). The PSU(N) theory, which sums over B, has period 2πN on spin manifolds.

**"On the lattice the anomaly is carried by B ∪ B."** Tempting, because $\sum B\cup B=2\kappa$ for the stack. For N even, $\sum\tilde B\cup\tilde B$ mod 2N depends on the lift (§3.1); the $\cup_1$ correction (3.6) makes it a function of [B].

## 11. Historical note

't Hooft's 1979 paper put SU(N) gauge fields in a Euclidean box with twisted boundary conditions, labelled the resulting bundles by $n_{\mu\nu}$, defined electric and magnetic fluxes through the center operators and the twists, and computed their free energies in the Higgs, confining and massless phases (§§2–9 of the paper); the flux sectors of Sem I Week 14 and the energetics of §5.2 are his. In 1981 he gave self-dual solutions on the twisted hypertorus with fractional Pontryagin number, abelian and of constant curvature, of which (2.8) at r = 1 is an instance. Witten's large-N analysis (1980, holographically 1998) predicted the branches of §6.2. Gaiotto, Kapustin, Komargodski and Seiberg (2017) read the twist as a background of the 1-form symmetry and found the mixed anomaly, the four-dimensional relative, in their words, of the parity anomaly of a free Dirac fermion in three dimensions.

## 12. What to take away

1. **Technical:** a $\mathbb{Z}_N$ background on $T^4$ is 't Hooft's twist, and every connection in a twisted bundle has $Q\equiv(N-1)\kappa/N$ mod 1, (2.15); for SU(2) the bundle (2.7)–(2.8) has Q = ½ and a self-dual half-instanton. **Physical:** a twist allows windings of 1/N.
2. **Technical:** on the lattice the fraction is carried by $\tilde B\cup\tilde B+\tilde B\cup_1d\tilde B$, closed mod 2N and independent of lift and gauge, with $\int_{T^4}\mathcal P=2\kappa$. **Physical:** the non-commutativity of the cubical cup product is real, and $\cup_1$ accounts for it.
3. **Technical:** θ → θ + 2π multiplies $Z_\theta[B]$ by $\exp\big(2\pi i\frac{N-1}{2N}\int\mathcal P(B)\big)$, and at θ = π no counterterm restores T for N even, (4.7). **Physical:** T and the center symmetry can each be kept, and both cannot.
4. **Technical:** matching excludes a trivially gapped, T-symmetric, confining vacuum at θ = π, (5.2); in a twisted box the anomaly is the exact degeneracy (5.5). **Physical:** at large N the vacua break T and are two different condensates (§6.2).

## 13. Looking ahead

The counterterm (4.3) is the partition function of an invertible four-dimensional theory of B, and the vacua at θ = π differ by such a phase. [[sem2-week-07-spt-phases-group-cohomology-dijkgraaf-witten|Sem II Week 7]] makes this the general structure: SPT phases as invertible responses to backgrounds (its §5.1), their classification by group cohomology, and Dijkgraaf–Witten theories as gauged SPTs (its §6), the finite counterpart of summing over B with a discrete θ-angle.

## 14. Problem set

*Routing:* Problems 1–4 are the classroom core, with checkpoints below; 5⋆–7⋆ are self-study; 8⋆⋆–9⋆⋆ are research extensions.

### Core problems

1. **Twisted SU(N) bundles with a diagonal generator.** (Extends §§2.3–2.4.) With $T={\rm diag}\big(\frac{N-1}N,-\frac1N,\dots,-\frac1N\big)$ and $\Omega_\mu=\exp\big(2\pi iT\sum_{\nu>\mu}n_{\mu\nu}x_\nu/L_\nu\big)$, show that $e^{2\pi iT}$ is central and that (2.5) holds with twist n; build $A=2\pi T\sum_{\mu<\nu}n_{\mu\nu}x_\mu dx_\nu/(L_\mu L_\nu)$, check (2.4), and compute Q. Evaluate it for SU(3) with $n_{13}=n_{24}=1$ and SU(4) with $n_{12}=2$, $n_{34}=1$.

2. **A change of lift, by hand.** (Extends §§3.1, 3.3.) For N = 2, the stack with $n_{12}=n_{34}=1$ and u the indicator of $P_{34}(0)$, compute the change of $\sum\tilde B\cup\tilde B$ under $\tilde B\to\tilde B+2u$ from (3.10). Use (3.5) summed over the torus to find the change of the $\cup_1$ term mod 4, and show that for any u the change of $\sum\mathcal P$ is $\equiv4\sum\tilde B\cup u\equiv0$ mod 4 when $d\tilde B=0$.

3. **Phases and counterterms for N = 3 and 4.** (Extends §4.) On $T^4$ write (4.2) as a function of κ for N = 3, 4; find the T-invariant counterterms at θ = 0 and θ = π on spin manifolds and on all manifolds; for N = 4 give the infrared labels of the two large-N vacua at θ = π.

4. **The branches of SU(3) at θ = π.** (Extends §6.2.) For k = 0, −1, 1, −2 tabulate $E_k(\pi)/\chi$, $p_k$ mod 3, the flux of the ground state of $\mathcal H_{\vec m}$ and the screened line; identify the branch whose flux sector is T-invariant under (5.5) and where it lies.

### Starred problems

5⋆. **Periodicity at a price, and inflow.** Show that $Z_\theta[B]\exp\big(-\frac{i\theta(N-1)}{2N}\int\mathcal P(B)\big)$ is 2π-periodic, with a factor that is not a function of [B] unless θ(N−1)/2π ∈ ℤ; then show that on $X\times S^1$, with θ winding once, $\exp\big(\frac{2\pi i(N-1)}{2N}\int\frac{d\theta}{2\pi}\cup\mathcal P(B)\big)$ is the phase (4.2). *Hint:* changes of lift shift $\int\mathcal P$ by multiples of 2N; compare Sem II Week 5 §5.

6⋆. **The period of θ in PSU(N).** From (4.4) find the smallest k for which θ → θ + 2πk is an identification at fixed p, on spin and on all manifolds, and specialize to SO(3), where θ → θ + 2π exchanges $SO(3)_\pm$. *Hint:* gcd(N − 1, N) = 1, and gcd(N − 1, 2N) = 1 for N even.

7⋆. **Odd N in a twisted box.** For N = 3 show that a T-invariant trivially gapped vacuum at θ = π has its $\mathcal H_{\vec m}$ ground state at $\vec e=\vec m$, and argue that the ground state must change flux sector between θ = 0 and π, a phase transition in infinite volume. *Hint:* §5.3; $\vec e$ is conserved for every θ.

### ⋆⋆ problems

8⋆⋆. **A lattice θ-term for SU(2) with B.** *Known:* Lüscher's admissibility construction gives SU(N) lattice fields an integer charge; the center symmetry is exact on the lattice; §3.5 has $Q_{\rm lat}=\frac12$ exactly. *Explored:* whether the construction extends to $\omega^{-B_P}U_P$ with $Q_{\rm lat}\in\frac14\sum\mathcal P(B)+\mathbb{Z}$ for every admissible field. *Sources:* Lüscher (1982), Chen–Tata §V, GKKS §2. *Completion:* a definition with a proof on the $L^4$ torus, or an admissible counterexample.

9⋆⋆. **SU(2) on $Y\times S^1$.** *Known:* GKKS §3.1 reduce the anomaly to three dimensions at high temperature, with the dihedral symmetry of their §§3.2–3.4 and Appendices B–C. *Explored:* the reduction in the lattice language of §§3–4. *Sources:* GKKS §3, App. B–C; Sem I Week 14 §§4–5. *Completion:* the three-dimensional anomaly and the T-action on the reduced backgrounds in the conventions of this note.

## Self-study answer checkpoints

**Problem 1.** *Decisive step:* $e^{2\pi iT}=\omega^{-1}\mathbb 1$, so $\Omega_\mu(x+L_\nu\hat\nu)=\omega^{-n_{\mu\nu}}\Omega_\mu(x)$ for ν > μ, and ${\rm tr}\,T^2=(N-1)/N$. *Result:* $Q=(N-1)\kappa/N$ exactly; SU(3) with $n_{13}=n_{24}=1$: κ = −1, Q = −2/3, fractional part 1/3; SU(4) with $n_{12}=2$, $n_{34}=1$: κ = 2, Q = 3/2, fractional part ½. *Failure mode:* dropping the shuffle sign of $n_{13}n_{24}$, or using diag(1, 0, …, 0), a U(N) connection with Q = κ.

**Problem 2.** *Decisive step:* $\sum u\cup\tilde B=u_{34}(0)\tilde B_{12}(\hat e_3+\hat e_4)=1$, $\sum\tilde B\cup u=\tilde B_{12}(-\hat e_1-\hat e_2)u_{34}(0)=0$, $\sum u\cup u=0$. *Result:* $\Delta\sum\tilde B\cup\tilde B=2$; $\sum\tilde B\cup_1du=\sum(\tilde B\cup u-u\cup\tilde B)=-1$, so the $\cup_1$ term changes by −2 mod 4 (exactly −2 on the lattice) and $\Delta\sum\mathcal P\equiv0$; in general (3.8) with y = 0 gives $\Delta\sum\mathcal P=4\sum\tilde B\cup u+4\sum(u\cup u+u\cup_1du)\equiv0$ mod 4, an equality mod 4 only. *Failure mode:* treating $\sum u\cup\tilde B$ and $\sum\tilde B\cup u$ as equal.

**Problem 3.** *Decisive step:* the phase $\omega^{-\kappa}$ and the fixed points of $p\to-p$ and $p\to-p-(N-1)$. *Result:* N = 3: $e^{-2\pi i\kappa/3}$; θ = 0: p ≡ 0 mod 3 (p = 0 in $2\mathbb{Z}_6$); θ = π: p ≡ 2 mod 3 (p = 2 in $2\mathbb{Z}_6$). N = 4: $(-i)^\kappa$; θ = 0: p ∈ {0, 2} mod 4, p ∈ {0, 4} mod 8; θ = π: none; vacua $p_0=0$, $p_{-1}=3$. *Failure mode:* using the infrared map for the counterterm, which gives p = 1 at θ = π for N = 3; this is GKKS's fixed point (2.13) mod 3, which is the infrared label of (5.2) (§4.3).

**Problem 4.** *Decisive step:* $p_k\equiv k$, $\vec e=k\vec m$, line (k, 1), T: $\vec e\to-\vec e-\vec m$. *Result:* $E_0(\pi)=E_{-1}(\pi)=\pi^2\chi/2$, $E_1(\pi)=E_{-2}(\pi)=9\pi^2\chi/2$; labels 0, 2, 1, 1; fluxes $0,2\vec m,\vec m,\vec m$; lines (0, 1), (−1, 1), (1, 1), (1, 1) mod 3. The T-invariant sector $\vec e=\vec m$ belongs to the pair k = 1, −2, which T exchanges, $4\pi^2\chi$ above the vacua: at large N the T-invariant option of §5.3 is a metastable branch. *Failure mode:* taking $p_k=k(N-1)$, which interchanges the fluxes $\vec m$ and $2\vec m$.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester II Block 2. Written to the note-quality-template standard on 2026-10-02. Last revised 2026-10-02.*
