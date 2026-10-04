---
title: "Sem II Week 15 — Write-Up Presentations and Panoramic Closing"
type: lecture-notes
course: syllabus
semester: 2
week: 15
block: 5
duration: 4 hours (2 hr write-up presentations and discussion + 2 hr closing lecture)
prerequisites: All of Semester I, in particular Week 15; Sem II Weeks 1–14; the student's revised write-up
modified: 2026-10-04
---

# Sem II Week 15 — Write-Up Presentations and Panoramic Closing

> *The course ends where its first duality began. Kramers and Wannier exchanged two expansions of the Ising model in 1941; in Semester II the same exchange became a topological line with $D\times\bar D=1+\eta$, gauging on a surface produced condensation defects, and Week 14 met them as the higher-gauging walls of four-dimensional $\mathbb{Z}_N$ gauge theory, whose completion lines the group's manuscript gives a finite cost. In the first part of the week the students present their write-ups. In the second we retell both semesters as one story, told with operators on closed submanifolds, draw the four threads of the [[courses/generalized-symmetries-course/syllabus|syllabus]] across both semesters, and list what to read next. Nothing is derived here that an earlier week did not derive.*

### How to use this chapter

- **In class:** the first two hours are the presentations, run as §2 prescribes, with Problem 3 prepared by each speaker. The closing lecture tells §3 station by station with Figure 1, writing at each station the relation quoted there and naming the week that derived it, and ends with Figure 2 (§4) and the reading list (§5). Problems 1–3 are the classroom core; Problem 1 belongs to §3.5 and Problem 2 to §3.8.
- **For self-study:** §§6–9 and Problems 4⋆–5⋆. There is no new calculation; the one exercise to do alone is Problem 5⋆.
- **Instructor checkpoint:** $D\times\bar D=1+\eta$ (a fusion rule, no normalization), $D^\dagger D=1+\eta$ (an operator identity) and $D^2=(1+\eta)T$ (with the lattice translation) are three statements (F1). And summing the condensed lines over all of spacetime gives a different theory with residual ${\rm Ann}(H)$, while summing them on a closed surface inserts the sheet $S_H$ into the original theory (F2).

## 0. Reading

**Primary.** Shao, "What's done cannot be undone: TASI lectures on non-invertible symmetries" [arXiv:2308.00747], §3.3 (pp. 27–34), §5 (pp. 42–50) and §6 (pp. 50–58): the last stations of §3 in one author's words.

**Secondary.** Córdova, Dumitrescu, Intriligator, Shao, Snowmass white paper [arXiv:2205.09545], read whole as the map of the field; McGreevy [arXiv:2204.03045], the review to keep.

**Optional research.** Roumpedakis, Seifnashri, Shao (RSS) [arXiv:2204.02407], §1.2 (pp. 4–6); Bah, Leung, Waddleton [arXiv:2506.04346]; the group's manuscript in preparation, M. S. Guimaraes, *Finite-Cost Currents at Higher-Gauging Walls in Four-Dimensional $\mathbb{Z}_N$ Gauge Theory* (version of 2026-09-20), §9 (relation to prior work) and §10 (conclusions and open problems).

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Sem I Week 1]]. This week derives nothing: every result is **[Stated — refs.]** to the week and section that derived it, with that section's label in parentheses. Signs and normalizations are those of [[courses/generalized-symmetries-course/conventions|conventions]], and every degree is checked against its §6.

## 1. Motivation and setting

Semester I closed on a thesis ([[week-15-semester-i-consolidation|Sem I Week 15]] §1): a phase is characterized by how its topological operators are realized and by which extended operators they detect. The question of the closing lecture is whether these twenty-nine weeks tell one story. We claim that they do when the story uses three kinds of objects only: operators on closed submanifolds, open operators through their boundaries, and sums over networks of closed operators.

## 2. The write-up presentations

### 2.1 Format and timing

The revised write-up (at least 15 pages) was due at the end of Week 14, after feedback on the Week 10 draft; its oral presentation belongs to the same item, 60% of the grade, the other 40% being the seminar presentations and participation (syllabus §5). The talk has no separate weight. Each student speaks for 20 minutes on the technical claim of the write-up, one calculation reproduced in full at the board, as in every seminar hour (syllabus §7), and the place of the write-up on Figure 2. Questions take about five minutes per talk, so four talks leave twenty minutes for a group discussion of the open problems of Week 14; with five speakers the questions shorten to four minutes and that discussion moves to the end of the closing lecture.

### 2.2 What the committee asks

The committee is the instructor, who grades, together with the class, who ask first. Its four questions are those every seminar presenter answered for a paper ([[courses/generalized-symmetries-course/appendices/bibliography-and-paper-map|bibliography-and-paper-map]], "How to read the references"), turned on the student's own work:

1. *The claim:* state the main result as a statement about operators on closed submanifolds (operator, support, algebra or realization), or say why it cannot be so stated.
2. *What it needs:* which weeks and threads; the write-up's row of Figure 2 (Problem 3).
3. *The calculation:* which hypothesis, if dropped, makes it fail, and where the course met that failure (charged matter, dynamical monopoles, finite volume); and which statements are proved, computed, stated or heuristic, in the labels of §0.
4. *The open problem:* what the write-up leaves open, at M.Sc. or Ph.D. scale.

### 2.3 From the write-up to the frontier

Topic 1 (Polyakov confinement retold) ends in [[sem2-week-12-modified-villain|Sem II Week 12]], where the modified Villain construction restores the magnetic symmetry that monopoles break, and continues to item 9 of the open problems of Sem II Week 14 §10, fractons via the exotic symmetries of Gorantla, Lam, Seiberg and Shao (GLSS). Topic 2 (the Fradkin–Shenker diagram from the toric-code side, [[sem2-week-08-toric-code-solved-to-the-bone|Sem II Week 8]] §7) meets item 11, the measurement-based realization of gauging, which Week 14 sets at M.Sc. scale as Phase C2 of the master-project. Topic 3 (condensation defects in $\mathbb{Z}_N$ lattice gauge theory) is the seed of the master project, whose Phases B and C draw on Week 14 §§2.3, 3 and 4, on Week 13 §5 and on Week 4 §5.1; the project's text predates the current manuscript (Week 14 §12). Topic 4 continues with its paper: Levin–Wen or RSS toward non-abelian condensates (item 10), Gaiotto–Kapustin–Komargodski–Seiberg toward the $3+1$d duality-defect connection (item 12; [[sem2-week-13-non-invertible-symmetries|Sem II Week 13]] §6). The other eight items come from the manuscript, each marked there as M.Sc.- or Ph.D.-scale.

## 3. One story, told with operators on closed submanifolds [Stated — refs: the weeks named at each station.]

The story has nine stations, drawn in Figure 1.

```
 1941            seam on a closed dual curve: η ;  μ at the ends of an open seam ;  D†D = 1+η
 Sem I Wk 4           │
                      │ [2] one dimension up, the seam becomes a sheet
                      ▼
 1971–79         Wegner's sheet: (−1)^Link on W(C) ;  open sheets end on visons, 't Hooft loops ;
 Sem I Wks 5,11,14    │ twists = flux sectors ;  charge-q matter keeps only Ann(H) ≅ ℤ_r         ◆
                      │ [1] Poisson resummation exchanges the operators of two descriptions
                      ▼
 1975–77         W(C) = vortex line of σ ;  e^{iσ} charged under U(1)^(0), broken by monopoles
 Sem I Wks 8–10       │
                      │ [2] GKSW: each closed operator above is a symmetry operator
                      ▼
 2014            U_α(Σ) W_q(C) = e^{iqα Link} ;  BF: GSD = N^{2g} ;  broken ⇔ perimeter law
 Sem II Wks 1–3       │
                      │ [4] sum over networks of symmetry operators = gauging ;  obstruction = anomaly
                      ▼
                 Σ_[B] Z_T[B] ;  KW = gauging ;  SPT, DW ;  0 → Ann(H) → ℤ_N → Ĥ → 0        ◆
 Sem II Wks 4–7       ├──▶ [3] the deconfined phase: code, state, anyons, string net  (Wks 8–11)
                      ├──▶ [1] exact lattice: Villain = MV + summed 't Hooft lines     (Wk 12)
                      │ [3]+[4] gauge on part of spacetime
                      ▼
 2016–22         half space: D × D̄ = 1+η ;  slab: C_q(M) ;  surface: S_H, Ann(H) fluxes pass ◆
 Sem II Wk 13         │
                      │ [3]+[4] gauge H on a closed hypersurface Y ;  give its lines a cost
                      ▼
 Sem II Wk 14    wall D_H: Ann(H) charges cross, D_H × D̄_H = D_H ;  costly lines ↔ ℤ_N′ clock ◆
```
**Figure 1. The single story as a chain of operators on closed submanifolds. Each arrow carries the thread of syllabus §8 that makes the step ([1] duality, [2] topological operators, [3] condensation, [4] cohomology); ◆ marks the stations at which the exact sequence of ${\rm Ann}(H)$ appears.**

### 3.1 1941: a duality is a seam

Kramers and Wannier matched the high-temperature expansion of the Ising model, a sum over closed loops on Λ, with the low-temperature one, a sum over closed walls on $\Lambda^*$, and found $\sinh2K\,\sinh2K^*=1$ ([[week-04-bkt-kramers-wannier-disorder|Sem I Week 4]] §3.3, Computed; [[kramers-wannier-duality]]). Reversing the coupling along a dual path is a seam: a closed seam that bounds is undone by flipping the spins it encloses, one around a cycle is a twisted boundary condition, and an open one is visible only at its ends, the disorder operators μ (Sem I Week 4 §4.1, Computed). On the chain the duality became an operator,
$$
D\,H(g)=g\,H(1/g)\,D,\qquad D^\dagger D=1+\eta,\qquad \eta=\prod_i\sigma^x_i ,
$$
where $H(g)=-\sum_i(\sigma^z_i\sigma^z_{i+1}+g\,\sigma^x_i)$ (Sem I Week 4 §4.4, Computed, with the normalization and one sign fixed numerically). The 1941 problem thus holds all three kinds of object: a closed topological operator, an object at the end of an open one, and a map with no inverse.

### 3.2 1971–1979: sheets, and the flux they count

In Wegner's gauge theory the seam becomes a sheet on a closed dual $(d-2)$-chain. When the sheet bounds, $\tilde\Sigma=\partial\tilde V$, a change of variables removes it, so that at every β
$$
\langle U(\tilde\Sigma)\rangle=1,\qquad \langle W(C)\,U(\tilde\Sigma)\rangle=(-1)^{{\rm Link}(C,\tilde\Sigma)}\,\langle W(C)\rangle
$$
(Sem I Week 15 (3.1), Proved; [[week-05-wegner-z2-gauge-theory|Sem I Week 5]] §8.1). A sheet around a noncontractible cycle is a twist instead: its expectation value is the ratio of the twisted to the untwisted partition function, which need not be 1, and the eigenvalues of the corresponding operator label the torus sectors (Sem I Week 5 F6; Sem I Week 15 §3.4). Open sheets end on visons in $d=3$ and on 't Hooft loops in $d=4$ (Sem I Week 5 §§7.3, 8.2), and in the deconfined phase the sheets and the Wilson loops that cross them on a spatial torus give $|H^1(T^2,\mathbb{Z}_2)|=4$ ground states (Sem I Week 15 (3.2)–(3.3)). For $U(1)$ the twisted sheet generates $U(1)^{(1)}$, and the integer 't Hooft loop of the Villain theory equals 1, screened by the monopoles ([[week-11-monopole-condensation-4d|Sem I Week 11]] §§5.1–5.2, Proved). With charge-$q$ matter only ${\rm Ann}(H)\cong\mathbb{Z}_r$, $H=\langle q\rangle$, $r=\gcd(N,q)$, stays topological, the kernel of $0\to{\rm Ann}(H)\to\mathbb{Z}_N\to\widehat H\to0$ ([[week-14-fradkin-shenker-order-parameters|Sem I Week 14]] (3.5), Proved).

### 3.3 1975–1977: Poisson resummation exchanges the operators

Every Semester I duality was Poisson resummation followed by a constraint solved on the dual lattice, with $\beta\to1/4\pi^2\beta$ in each $U(1)$ row, and the defects of the second resummation break the dual symmetry explicitly (Sem I Week 15 §4, Table 1). In compact QED₃ a charge-$q$ Wilson loop becomes a vortex line around which σ winds by $2\pi q$ ([[week-10-polyakov-mass-gap-area-law|Sem I Week 10]] §4.3, Proved), and $e^{i\sigma}$ is the local operator charged under the magnetic $U(1)^{(0)}$ generated by $\exp(i\alpha\oint_\Sigma F/2\pi)$ ([[week-09-compact-qed3-monopole-plasma|Sem I Week 9]] §5.1). Monopoles put it into the action as $-2\zeta\cos\sigma$, which gaps the photon, $m_\gamma^2=8\pi^2\zeta/e^2$, and the wall dragged by the vortex line gives the area law (Sem I Week 9 §§3, 5.3; Sem I Week 10 §§3, 5; [[courses/generalized-symmetries-course/conventions|conventions]] §5). Polyakov confinement reads: the electric $U(1)^{(1)}$ is unbroken because the magnetic $U(1)^{(0)}$ is explicitly broken ([[sem2-week-03-spontaneous-breaking-of-higher-form-symmetries|Sem II Week 3]] §6).

### 3.4 2014: the operators are symmetries

The definition of Gaiotto, Kapustin, Seiberg and Willett (GKSW) covers every closed operator above ([[higher-form-symmetries]]). [[sem2-week-01-symmetries-are-topological-operators|Sem II Week 1]] derived it from Noether's theorem: the operator is a twist of the fields across $\Sigma=\partial V$, and
$$
\langle U_\alpha(\Sigma)\,W_q(C)\cdots\rangle=e^{iq\alpha\,{\rm Link}(C,\Sigma)}\,\langle W_q(C)\cdots\rangle ,
$$
exactly for the lattice twisted sheet and in the continuum, with the equal-time commutator as the same statement and an abelian group for $p\ge1$ (Sem II Week 1 (2.5), (5.6), (6.3)–(6.4), §4; Proved, the last a Model proof). $\mathbb{Z}_N$ BF theory gives $W(\gamma)V(\gamma')=\omega^{-\gamma\cdot\gamma'}V(\gamma')W(\gamma)$, ${\rm GSD}(\Sigma_g)=N^{2g}$ and braiding as linking, $\langle W_eV_m\rangle=\omega^{-em\,{\rm Lk}}$ ([[sem2-week-02-zn-gauge-theory-as-bf-theory|Sem II Week 2]] (3.6), (4.2), (5.4)). Phases became realizations: a perimeter law up to a local counterterm means broken, the photon is a Goldstone boson, continuous $p$-form symmetries break only for $p\le d-3$, and charge-$q$ pairs leave $\mathbb{Z}_q^{(1)}$, which the condensate breaks (Sem II Week 3 (2.1), §§3–5).

### 3.5 Summing the operators, and when the sum fails

A background is a cocycle $B\in Z^{p+1}(X,\mathbb{Z}_N)$, a network of closed symmetry operators, and gauging is
$$
Z_{T/\mathbb{Z}_N^{(p)}}=\frac{|H^{p-1}|\,|H^{p-3}|\cdots}{|H^{p}|\,|H^{p-2}|\cdots}\sum_{[B]\in H^{p+1}(X,\mathbb{Z}_N)}Z_T[B]
$$
([[sem2-week-04-gauging-backgrounds-and-dual-symmetry|Sem II Week 4]] (2.5), Proved). It produces a dual $\mathbb{Z}_N^{(d-p-2)}$, is undone on tori by gauging that, and exchanges genuine operators with boundaries (Sem II Week 4 (4.2), (4.4), §4.3, Proved). On the Ising chain it is Kramers–Wannier, $D=2^{L/2}RPE$, non-invertible because $\prod_iG_i=\eta$ (Sem II Week 4 (3.12), (3.7a), Computed); subgroups follow the sequence of §3.2 (Sem II Week 4 (5.1)). The sum fails when a phase $Z[A^\lambda]=e^{i\mathcal A(A,\lambda)}Z[A]$ survives every counterterm: an 't Hooft anomaly ([[t-hooft-anomaly]]; [[sem2-week-05-thooft-anomalies-obstruction-as-physics|Sem II Week 5]] (2.1)–(2.2), with its projective, Lieb–Schultz–Mattis and inflow forms), and in Yang–Mills theory the center background gives $Z_{\theta+2\pi}[B]=\exp\big(\frac{2\pi i(N-1)}{2N}\int\mathcal P(B)\big)Z_\theta[B]$, which at θ = π excludes a trivially gapped, $T$-symmetric, confining vacuum for even $N$ ([[sem2-week-06-mixed-anomalies-yang-mills-at-theta-pi|Sem II Week 6]] (4.2), Proved; §5.1, Proved given the counterterms of §4.2, which are Stated). An SPT phase is a topological action for its background, $(-1)^{\sum a\cup a\cup a}$ from $H^3(\mathbb{Z}_2,U(1))=\mathbb{Z}_2$, and gauging it gives Dijkgraaf–Witten theory with semion fluxes, $\theta_s^2=F(s,s,s)$ ([[spt-phases]]; [[sem2-week-07-spt-phases-group-cohomology-dijkgraaf-witten|Sem II Week 7]] (2.5), (5.7), (6.9)).

### 3.6 The deconfined phase, read four ways

The toric code has $2^{2g}$ ground states; its logical operators are Wilson loops and electric cuts, $W(C)U(\tilde C)=(-1)^{I(C,\tilde C)}U(\tilde C)W(C)$, the order parameters and generators of two broken 1-form symmetries, and its anyons are endpoints of open strings with $S=M/\mathcal D$ ([[toric-code]]; Sem II Week 8 (3.6), (3.8), (5.5)). As a code it is $[\![2L_1L_2,2,\min(L_1,L_2)]\!]$, and its disk entropy $|\partial A|\ln2-\ln2$ carries $\gamma=\ln\mathcal D$ ([[sem2-week-09-long-range-entanglement-and-error-correction|Sem II Week 9]] (3.6), (4.2), (5.3), Proved); abelian Chern–Simons theory gives ${\rm GSD}=|\det K|^g$ ([[sem2-week-10-beyond-z2-quantum-doubles-modular-data-chern-simons|Sem II Week 10]] (3.4)). In Wen's reading the ground state is a condensate of closed string nets, $\Phi(\mathcal X)=d_1^{N(\mathcal X)}$, with the gauge field and its charges emerging together ([[topological-order]]; [[string-net-condensation]]; [[sem2-week-11-string-net-condensation|Sem II Week 11]] (3.4), §6). Perturbing the toric code, $e$ condensation is Higgsing and $m$ condensation confinement, and the Fradkin–Shenker diagram is the diagram of the two (Sem II Week 8 §§7.3–7.4, Proved through exact maps; §7.6, Stated).

### 3.7 Exactness on the lattice

The modified Villain (MV) construction makes the Villain integer a flat $\mathbb{Z}$ gauge field and removes the defects, so dualities and symmetries are both exact: $Z_{\rm MV}[\Lambda;\beta]=(2\pi\beta)^{-N_1/2}Z_{\rm MV}[\Lambda^*;1/4\pi^2\beta]$, the magnetic operator $U^{\rm m}_\alpha(\Sigma)=e^{-i\alpha\sum_\Sigma n}$ is topological, a $\mathbb{Z}_N$ background enters through $d(Nn+B)=0$, and θ is exactly $2\pi$-periodic (Sem II Week 12 (2.7), (4.1), (5.1), Proved; (3.2), Proved for the static configuration, the general linking sign Sketched). The plain Villain theory is the MV theory with its defect operators summed with unit weight: vortex operators in $d=2$, 't Hooft lines over all closed configurations in $d=4$ (Sem II Week 12 (6.1)–(6.2), Proved). This is the condensation thread as an operator statement: a defect condensate sums charged operators on closed supports, while gauging sums symmetry operators. The two meet in $\mathbb{Z}_N$ gauge theory, where the Wilson lines are both the charged objects of the electric symmetry and the generators of the magnetic one.

### 3.8 Back to 1941: duality lines and condensation sheets

On the self-dual line the dressed Kramers–Wannier operator commutes with the transfer matrix; along time it is the interface left by gauging on half of space; and $D\times\bar D=1+\eta$, $D\times\eta=D$ (Sem II Week 13 (2.8), (3.9)–(3.10), Proved). If $T\cong T/\mathbb{Z}_N^{(q)}$, gauging in a region gives a defect on its boundary $M$ whose fusion is the gauging in the slab,
$$
D\times\bar D=C_q(M)\equiv\frac{|H^{q-2}(M)|\,|H^{q-4}(M)|\cdots}{|H^{q-1}(M)|\,|H^{q-3}(M)|\cdots}\sum_{\Sigma\in H_{d-1-q}(M;\mathbb{Z}_N)}\eta(\Sigma),
$$
which is $1+\eta$ for $d=2$, $q=0$, $N=2$, and the $3+1$d fusion of Choi, Córdova, Hsin, Lam and Shao (CCHLS) for $d=4$, $q=1$ (Sem II Week 13 (4.2)–(4.3); §6 Stated). The right side needs no self-duality ([[condensation-defects]]). In $2+1$d $\mathbb{Z}_N$ gauge theory, summing the Wilson lines of $H=\langle k\rangle$ on a closed surface is higher gauging of $H$ inside the magnetic $\mathbb{Z}_N^{(1)}$,
$$
S_H(\Sigma)=\frac1{|H^0(\Sigma;H)|}\sum_{\gamma\in H_1(\Sigma;H)}W(\gamma),\qquad S_H\times\bar S_H=Z_H(\Sigma)\,S_H,\qquad Z_H(\Sigma_g)=|H|^{2g-1},
$$
on which the charges of $H$ end and through which only fluxes in ${\rm Ann}(H)$ pass unless a dual line is attached (Sem II Week 13 (5.8), §5.4, Proved).

### 3.9 Week 14: the wall, and the cost of its lines [Stated — refs: Sem II Week 14 §§2–7 and 9, with the labels given there.]

The last station is Sem II Week 14, "Defect Condensation and the Julia–Toulouse Mechanism in Modern Dress". There $H=\langle k\rangle$ is a group of fluxes of the electric $\mathbb{Z}_N^{(1)}$, while at the sheet of §3.8 it is a group of condensed charges, and the pairing $\omega^{qh}$ translates between the two (Sem II Week 14 §2.2). The wall sums the closed $H$-labelled sheet networks on a closed hypersurface $Y$, $D_H(Y)=\mathcal N_Y^{-1}\sum_{S\in Z_2(Y;H)}U[S]$, and weights a charge-$q$ Wilson line that crosses it by
$$
P_H(q)=\frac1{N'}\sum_{u=0}^{N'-1}e^{2\pi iqu/N'}=\begin{cases}1,&q\in{\rm Ann}(H),\\0,&q\notin{\rm Ann}(H),\end{cases}
$$
so that the other lines meet $Y$ at junctions carrying ${\rm res}_H(q)$, through $0\to{\rm Ann}(H)\to\mathbb{Z}_N\to\widehat H\to0$ (Sem II Week 14 (2.2), Stated; (2.3)–(2.4), Proved). For any $Y$ the wall fuses as $D_H\times\bar D_H=D_H$, and on a time slice it is a projector; Table 1 there sets bulk and hypersurface condensation side by side (Sem II Week 14 (2.8), (2.6), §3; Proved, the course's own). In $2+1$d a charge-$k$ condensate restricted to a surface is, in its London limit, the sheet of §3.8, $|H|\,\Pi_H$ (Sem II Week 14 (4.4), Proved, the course's own). The [[julia-toulouse-mechanism|Julia–Toulouse]] ensemble, read as entropy against activation (Sem II Week 14 §5.1, Stated, the interpretation Heuristic; Sem I Week 11 §3.3), motivates the manuscript's step: the completion lines on $Y$ receive a periodic-Gaussian cost κ per unit length, and an exact character transform maps their $\mathbb{Z}_{N'}$ currents to a clock model of Villain stiffness $1/\kappa$ (Sem II Week 14 (6.3), (6.5)–(6.6), Proved). A junction pair is the clock correlator $\langle\omega_{N'}^{-\alpha(\theta_x-\theta_{x'})}\rangle$, so the endpoint tension vanishes throughout the ordered phase $\kappa<\kappa_c$, and at large cost $\tau_\alpha/\kappa\to\bar\alpha/2$ with $\bar\alpha=\min_m|\alpha+N'm|$ (Sem II Week 14 (7.2), Proved; (7.8), minimization Proved, bounds Sketched). The novelty boundary is the manuscript's (Sem II Week 14 §9, Stated): the subgroup surface sum, its filter and its fusion are prior work (RSS, CCHLS and, as the closest construction, Bah, Leung and Waddleton), and "the contribution is this endpoint prescription with a fixed crossing filter, the resulting observable dictionary, and the uniform bound on the stable charge cost."

## 4. The four threads across both semesters

Figure 2 places the threads of syllabus §8 against the weeks. The Semester I column lists only the weeks in which a thread is the subject, which Figure 2 of Sem I Week 15 resolves week by week; the Semester II rows are complete. The marks are a reading of the notes.

```
                           Sem I            Sem II
                           (● weeks)         Block 1    │ Block 2 │ Block 3    │ Bl. 4 │ Bl. 5
                                             1  2  3  4 │ 5  6  7 │ 8  9 10 11 │12 13 │14 15
 1  duality                1–5, 8            ·  ○  ○  ● │ ·  ·  · │ ○  ·  ·  ○ │ ●  ● │ ●  ○
 2  topological operators  4, 5, 9–11, 14    ●  ●  ●  ● │ ○  ○  ○ │ ●  ○  ○  ○ │ ●  ● │ ●  ○
 3  condensation           4, 5, 9–13        ·  ·  ○  ○ │ ·  ○  · │ ●  ·  ○  ● │ ○  ● │ ●  ○
 4  cohomology             2, 3, 8, 12, 14   ○  ●  ·  ● │ ●  ●  ● │ ●  ○  ○  ○ │ ○  ● │ ●  ○

 ● the thread is the subject of the week      ○ the thread is used      · absent
 Threads: 1 duality is Poisson resummation; 2 symmetries live on topological operators;
          3 condensation changes the theory; 4 cohomology is the bookkeeping.
```
**Figure 2. The threads × weeks map of the course. The Semester I column lists the weeks marked ● in Figure 2 of Sem I Week 15.**

Read by rows, the duality thread becomes gauging in Sem II Week 4, exact in Week 12, a line at the self-dual coupling in Week 13, and the current–clock duality of the wall in Week 14; topological operators, the subject of Block 1, end without inverse (Weeks 13–14); condensation returns in Block 3 as anyon and string-net condensation and ends as gauging on a hypersurface, whose lines Week 14 gives a cost; cohomology ends as $H_1(\Sigma;H)$, $Z_2(Y;H)$, the relative cohomology of a slab and the sequence of ${\rm Ann}(H)$. Read by columns, Weeks 13 and 14 are the weeks in which all four threads are the subject. On the wiki the threads continue on [[villain-action]] (1), [[higher-form-symmetries]] (2), [[condensation-defects]] and [[julia-toulouse-mechanism]] (3), and [[spt-phases]] and [[topological-order]] (4).

## 5. After the course: what to read, and why

Every entry is in the [[courses/generalized-symmetries-course/appendices/bibliography-and-paper-map|bibliography-and-paper-map]], with its verified metadata.

| Reference | Why | Where to start |
|---|---|---|
| RSS, *Commun. Math. Phys.* 401 (2023) 3043 [arXiv:2204.02407] | The higher-gauging framework that the manuscript takes as prior work; its sheet normalization differs from ours (F3) | §§1–3, then §5 |
| Bah, Leung, Waddleton, *JHEP* 09 (2026) 272 [arXiv:2506.04346] | The four-dimensional subgroup condensation defect with its fusion data, the manuscript's closest construction | the dual lines of the wall, their eq. (2.24) |
| Shao, TASI lectures [arXiv:2308.00747] | Non-invertible symmetries systematically; Blocks 4–5 follow its order | §§5–6 (pp. 42–58) |
| CCHLS, *Phys. Rev. D* 105 (2022) 125016 [arXiv:2111.01139]; Kaidi, Ohmori, Zheng, *Phys. Rev. Lett.* 128 (2022) 111601 [arXiv:2111.01141]; Koide, Nagoya, Yamaguchi, *PTEP* 2022 (2022) 013B03 [arXiv:2109.05992] | The $3+1$d duality defects that Sem II Week 13 §6 only states; open problem 12 of Week 14 | CCHLS §§2.1–2.3, 4.2, 5.2 |
| Julia & Toulouse, *J. Physique Lett.* 40 (1979) L-395; Quevedo & Trugenberger, *Nucl. Phys. B* 501 (1997) 143 [hep-th/9604196]; the group's JTA series, paper by paper, e.g. Grigorio, Guimaraes, Rougemont, Wotzasek, *JHEP* 08 (2011) 118 [1102.3933] | The weighted defect ensemble that motivates the cost of the wall's lines, and the brane-symmetry formulation the manuscript uses (Week 14 §5.1) | JT in full; QT §§1–3 |
| GLSS, *J. Math. Phys.* 62 (2021) 102301 [arXiv:2103.01257]; Seiberg & Shao, *SciPost Phys.* 10 (2021) 003 [arXiv:2004.06115]; Nandkishore & Hermele, "Fractons", *Ann. Rev. Condens. Matter Phys.* 10 (2019) 295 [arXiv:1803.11196] | The fracton applications that Week 12 skipped, the exotic $\mathbb{Z}_N$ symmetries of fractons in $3+1$d, and a review of fractons (open problem 9 of Week 14) | the review; GLSS after its Villain sections |
| Kitaev, *Ann. Phys.* 321 (2006) 2 [cond-mat/0506438]; Bais & Slingerland, *Phys. Rev. B* 79 (2009) 045316 [arXiv:0808.0627]; Burnell, "Anyon condensation and its applications", *Ann. Rev. Condens. Matter Phys.* 9 (2018) 307 [arXiv:1706.04940] | Anyon data, condensation rules and a review of anyon condensation: the entry to non-abelian condensates (open problem 10) | Burnell; Kitaev App. E |
| Dennis, Kitaev, Landahl, Preskill, *J. Math. Phys.* 43 (2002) 4452 [quant-ph/0110143]; Tantivasadakarn, Thorngren, Vishwanath, Verresen, *Phys. Rev. X* 14 (2024) 021040 [arXiv:2112.01519] | The memory of Sem II Week 9 in full, and long-range entanglement obtained by measuring SPT phases, the route to gauging by measurement: open problem 11 of Week 14 (Phase C2 of the master project) | DKLP §§I, III.A–B, IV |
| McGreevy [arXiv:2204.03045]; Schäfer-Nameki [arXiv:2305.18296]; Bhardwaj et al. [arXiv:2307.07547]; Brennan & Hong [arXiv:2306.00912] | Reviews to keep, and routes into the categorical language the course left out (syllabus §11) | whichever reads best |
| M. S. Guimaraes, *Finite-Cost Currents at Higher-Gauging Walls in Four-Dimensional $\mathbb{Z}_N$ Gauge Theory* (in preparation, version of 2026-09-20) | The destination of the course | §9 (prior work), §10 (open problems) |

## 6. Subtleties and fine print

**F1 — Three statements about $D$.** $D\times\bar D=1+\eta$ is a fusion rule and carries no normalization; $D^\dagger D=1+\eta=2P_{\rm even}$ is an operator identity in the normalization of [[courses/generalized-symmetries-course/conventions|conventions]] §4; $D^2=(1+\eta)T$ carries a translation because the dual chain sits half a spacing away (Sem I Week 4 §4.4; Sem II Week 13 F1–F2).

**F2 — Bulk versus hypersurface.** Gauging $H$, or condensing charge-$k$ matter, in all of spacetime produces a different theory with a residual $\mathbb{Z}_r$ (Sem I Week 14 §3; Sem II Week 4 §5); summing the same objects on a closed hypersurface inserts a defect into the original theory (Sem II Week 13 §5). One exact sequence organizes both, read on opposite sides of the pairing according as $H$ is a group of charges or of fluxes (Sem II Week 14 §2.2 and Table 1).

**F3 — Normalizations.** Gauging returns the original theory up to $N^{\pm\chi(X)}$, which is 1 on tori ([[courses/generalized-symmetries-course/conventions|conventions]] §6). The sheet's $1/|H^0(\Sigma;H)|$ and RSS's $1/\sqrt{|H_1(\Sigma;H)|}$ differ by $|H|^{g-1}$, an Euler counterterm (Sem II Week 13 F7); the group's manuscript takes precedence where it fixes its own ([[courses/generalized-symmetries-course/conventions|conventions]] §7).

**F4 — Status and degree.** A statement of the story holds where its symmetry is exact: Wegner's magnetic $\mathbb{Z}_2^{(1)}$ is emergent ([[courses/generalized-symmetries-course/conventions|conventions]] §6), the Villain magnetic symmetry explicitly broken and the MV one exact, and $S_H$ topological at the BF point (Sem II Week 13 F5). Gauging gives degree $d-p-2$, while the magnetic symmetry of $p$-form BF theory has degree $d-p-1$ ([[courses/generalized-symmetries-course/conventions|conventions]] §6).

## 7. Common misconceptions

- **"Non-invertible symmetries are unrelated to ordinary gauging."** Tempting because $D$ fits no group law. Every non-invertible operator of the course is gauging on part of spacetime: half-space gauging composed with a duality map, or gauging on a manifold of codimension one (Sem II Week 13 §4).
- **"A duality is a symmetry."** Tempting because self-duality located $T_c$. A duality maps $H(g)$ to $g\,H(1/g)$ and is a topological line of one theory only at the self-dual point; elsewhere duality interfaces separate two theories (Sem II Week 13 §2.2, F3).

## 8. Historical note

Two lineages meet here. Order and disorder: Kramers–Wannier (1941), Kadanoff–Ceva and Wegner (1971), 't Hooft's flux classification (1978–79), the single definition of GKSW (2014), the lattice defect of Aasen, Mong and Fendley (2016), the $3+1$d duality defects of CCHLS and of Kaidi, Ohmori and Zheng (2021), and higher gauging (RSS, 2022). Condensation: vortex unbinding, Polyakov's plasma (1975–77), Julia and Toulouse (1979), the rank-changing field theory of Quevedo and Trugenberger (1996–97), the group's 2009–2013 series, and the string nets of Levin and Wen (2005). Bah, Leung and Waddleton (2025) added the four-dimensional subgroup defect to the first lineage, and the group's manuscript of 2026 joins the two through a finite-cost line sector on the wall, with the Julia–Toulouse ensemble motivating its weight.

## 9. What to take away

1. **Technical:** every result of the course concerns operators on closed submanifolds, open operators through their boundaries, or sums over networks of closed operators. **Physical:** dualities, gauging and condensation are operations on the topological operators whose realization is the phase.
2. **Technical:** Poisson resummation exchanges the charged objects of two symmetries; the MV construction makes both exact, and the Villain theory is MV with its defects summed. **Physical:** a duality says which operators are cheap on each side.
3. **Technical:** gauging sums symmetry operators with (2.5) of Sem II Week 4, and an anomaly is the failure of that sum. **Physical:** what survives of an anomaly are edges and degeneracies.
4. **Technical:** gauging on part of spacetime gives $D\times\bar D=1+\eta$, $C_q(M)$ and $S_H\times\bar S_H=Z_HS_H$, organized with matter and walls by $0\to{\rm Ann}(H)\to\mathbb{Z}_N\to\widehat H\to0$. **Physical:** gauging a subgroup changes the theory in the bulk and inserts a defect on a hypersurface, and the group's manuscript gives a cost to the lines that complete, on the wall, the Wilson lines it stops.

## 10. Looking ahead: after the course

There is no Week 16. At M.Sc. scale the write-up continues along the routes of §2.3; at Ph.D. scale it leads to the group's manuscript and to the revival of the [[confinement-duality]] program.

## 11. Problem set

Problems 1–3 are the classroom core (Problem 3 prepared before the talk), 4⋆–5⋆ self-study consolidation, 6⋆⋆ research extension. All use only results quoted in §3; none asks for a new calculation.

### Core problems

**Problem 1 (the degree rule along the story).** Apply Sem II Week 4 (4.2) to (a) the transverse-field Ising chain ($d=2$, $p=0$) and the $2+1$d $\mathbb{Z}_2$ gauge theory ($d=3$, $p=1$), naming the row of Table 1 of Sem I Week 15 each reproduces and the operators that become genuine (Sem II Week 4 §4.3(c)); (b) the four-dimensional $\mathbb{Z}_2$ gauge theory. (c) Why is the BF degree $d-p-1$ a different statement? *Extends:* §3.5.

**Problem 2 (three fusions, one mechanism).** (a) For $D\times\bar D$ with $d=2$, $q=0$, $N=2$, for $D\times\bar D$ with $d=4$, $q=1$, and for $S_H\times\bar S_H$, name the manifold on which a symmetry is gauged, the group, and the operators summed. (b) Why does the left side of Sem II Week 13 (4.2) need $T\cong T/\mathbb{Z}_N^{(q)}$ and the right side not? *Extends:* §3.8.

**Problem 3 (your write-up on the map).** (a) State your main claim as a statement about operators on closed submanifolds; (b) mark its row of Figure 2; (c) name the hypothesis whose failure the course met, and where. *Extends:* §§2.2, 4.

### Starred problems

**Problem 4⋆ (the cohomology thread).** For (a) $H^1(\Sigma_g,\mathbb{Z}_N)$, (b) $H^2(\mathbb{Z}_2\times\mathbb{Z}_2,U(1))$, (c) $H^3(\mathbb{Z}_2,U(1))$, (d) $\int_{T^4}\mathcal P(B)$ mod $2N$, (e) $H_1(\Sigma;H)$, (f) $H^k(M\times I,M\times\partial I;\mathbb{Z}_N)$: what does a class label, which operators carry it, and which week computed it? *Hint:* a class is an insertion that no local move removes.

**Problem 5⋆ (exact, emergent, explicit).** Classify, with the deciding week: (a) the magnetic $U(1)^{(1)}$ of four-dimensional Villain compact QED; (b) the same in the MV theory; (c) Wegner's magnetic $\mathbb{Z}_2^{(1)}$ in $d=3$; (d) the Kramers–Wannier operator at $g\ne1$; (e) the residual $\mathbb{Z}_r^{(1)}$ with charge-$q$ matter. *Hint:* F4 and Table 3 of Sem I Week 15.

### ⋆⋆ problems

**Problem 6⋆⋆ (from the write-up to a project).** Choose one of the twelve open problems of Sem II Week 14 §10; a reader without that chapter can choose among the four that do not depend on the group's manuscript: fractons via the exotic symmetries of GLSS, non-abelian condensates, measurement-based realizations of gauging, and the $3+1$d duality-defect connection. *Known:* at least three results of §3 that bear on it. *Explored:* the first computation that would test it in the smallest lattice model of the course, with its inputs. *Sources:* the entries of §5 for it and, for the eight items drawn from it, the group's manuscript. *Completion:* a plan of at most two pages whose first computation is finite and checked in its simplest case against the course or a §5 source, with its scale argued and accepted by the instructor.

## Self-study answer checkpoints

**Problem 1.** *Decisive step:* $d-p-2$ with $d$ the spacetime dimension. *Result:* (a) degree 0 twice: the Kramers–Wannier row, with the disorder operators μ becoming genuine (Sem II Week 4 §4.3(c)); the row of the three-dimensional gauge theory and its Ising dual, with the visons becoming the dual spins (Sem II Week 4 §7.3, Sub-tasks 3–5; Sem I Week 5 §7.3). (b) Degree 1: the 't Hooft loop becomes a genuine line (Sem II Week 4 §4.3(c); Sem I Week 15 Table 4). (c) $d-p-1$ is the degree of the symmetry generated by Wilson operators in BF theory, $d-p-2$ that created by gauging; for $d=3$, $p=1$ they are 1 and 0. *Common failure:* the spatial dimension, which gives $-1$ for the chain (erratum E1).

**Problem 2.** *Decisive step:* reading Sem II Week 13 (4.2) and (5.1) as gaugings. *Result:* (a) $\mathbb{Z}_2^{(0)}$ on the closed curve $M$, summed over $H_1(M;\mathbb{Z}_2)$: $1+\eta$; $\mathbb{Z}_N^{(1)}$ on the 3-manifold $M$, surface operators over $H_2(M;\mathbb{Z}_N)$ with $1/N$; $H$ inside the magnetic $\mathbb{Z}_N^{(1)}$ on Σ, Wilson lines over $H_1(\Sigma;H)$ with $1/|H^0(\Sigma;H)|$, so that $Z_H(\Sigma_g)=|H|^{2g-1}$. (b) The left side composes half-space gauging with the duality map, which exists only if the gauged theory is the original one; the slab needs only a non-anomalous symmetry. *Common failure:* reading $1+\eta$ as a projector (F1).

**Problem 3.** *Decisive step:* naming operator, support and realization. *Result,* for topic 1: (a) the electric $U(1)^{(1)}$ of compact QED₃ is unbroken because the magnetic $U(1)^{(0)}$, generated by $\exp(i\alpha\oint_\Sigma F/2\pi)$, is explicitly broken by monopoles entering as $2\zeta\cos\sigma$ (§3.3); (b) 1 ●, 2 ●, 3 ●, 4 ○; (c) without monopoles the magnetic symmetry is exact and spontaneously broken, with the photon as its Goldstone boson (Sem II Week 3 §3.4; Sem II Week 12 §3.1). *Common failure:* calling the 't Hooft loop the generator of the magnetic symmetry (Sem I Week 15 §9).

**Problem 4⋆.** *Decisive step:* separating cochains on the group from cochains on the lattice. *Result:* (a) holonomy sectors of flat fields, the $N^{2g}$ BF ground states (Sem II Week 2 (4.2)); (b) projective classes of the symmetry operators, $c(a,b)=\pm1$, carried by the cluster-chain edge (Sem II Week 5 (3.9)); (c) the associator $(-1)^{xyz}$ of flux lines, which makes them semions (Sem II Week 7 (2.5), (6.9)); (d) the twist of the center background, $\int\mathcal P\equiv2\kappa$ with $\kappa={\rm Pf}(n)$, which fixes the anomalous phase (Sem II Week 6 (2.6), (3.11), (4.2)); (e) networks of condensed lines, $|H|^{2g}$ of them (Sem II Week 13 (5.2)); (f) slab backgrounds, $H^{k-1}(M)$, which give $C_q(M)$ (Sem II Week 13 (4.1)). *Common failure:* reading (b) and (c) as spacetime sectors.

**Problem 5⋆.** *Decisive step:* does a topological generator exist at every coupling? *Result:* (a) explicitly broken, the integer 't Hooft loop equals 1 (Sem I Week 11 §5.2); (b) exact, $U^{\rm m}_\alpha=e^{-i\alpha\sum_\Sigma n}$ (Sem II Week 12 (3.2)); (c) emergent, since visons are dynamical at finite β ([[courses/generalized-symmetries-course/conventions|conventions]] §6); (d) no symmetry, an interface between $H(g)$ and $g\,H(1/g)$, a line only at $g=1$ (Sem II Week 13 §2.2); (e) exact, ${\rm Ann}(\langle q\rangle)\cong\mathbb{Z}_{\gcd(N,q)}$ (Sem I Week 14 (3.5)). *Common failure:* protecting an exact degeneracy with an emergent symmetry; Wegner's torus sectors are exact through the electric operators and split at order $(\Gamma/K)^L$ (Sem I Week 15 §3.4).

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester II Block 5. Written to the note-quality-template standard on 2026-10-03. Last revised 2026-10-04.*
