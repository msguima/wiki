---
title: "The Chern-Simons Function and the Quantum Hall Effect"
type: paper
authors: [Edward Witten]
year: 2026
arxiv: "2609.21182"
journal: "Bull. Amer. Math. Soc. (to appear; issue in memory of James Simons)"
areas: [condensed-matter-connections, confinement-duality]
status: preprint
---

## Summary

An expository article by [[edward-witten|Edward Witten]] (IAS; hep-th, v1 18 Sep 2026, v2 22 Sep 2026). It is the written version of a lecture given in 2013 at the CUNY Graduate Center conference for Jim Simons' 75th birthday, and will appear in the *Bulletin of the AMS* issue in memory of Simons (1938–2024). It is written for mathematicians and has four short sections and 29 references. The article defines the [[chern-simons-theory|Chern–Simons function]] as the secondary characteristic class attached to the second Chern class. Using nothing but the effective action of the electromagnetic field, it then explains why the response of a two-dimensional insulator is labeled by an integer, the [[quantum-hall-effect|quantum Hall]] level $k$ with $\sigma_{xy} = k\,e^2/h$. Finally it shows how an emergent Chern–Simons gauge field turns that integer into the rational numbers of the fractional effect.

The chain of reasoning is the part worth keeping:

1. An **insulator** is a material with no relevant low-energy degrees of freedom. Its electromagnetic response is therefore a local effective action $I_{\rm eff}[A]$, organized as an expansion in fields and derivatives and constrained by the microscopic symmetries.
2. In $2+1$ dimensions exactly **one** term in that action cannot be written in terms of $\vec E$ and $\vec B$. That term is the Chern–Simons function, which is defined only mod $\mathbb{Z}$.
3. Classically an additive ambiguity in the action is harmless. Quantum mechanically $e^{iI}$ must be well defined (Dirac's lesson), so the coefficient must be $2\pi k$ with $k\in\mathbb{Z}$.
4. The Chern–Simons term is the only one whose variation gives a current **proportional to the field** rather than to its derivatives. That current is the Hall effect, with an integer coefficient.
5. For $U(1)$, defining the function mod $\mathbb{Z}$ requires a **spin structure**, because the intersection form of a spin 4-manifold is even. Without one only even $k$ would be allowed, so the experimental observation of odd $k$ is, in Witten's reading, physical evidence that spacetime carries a spin structure.

For this wiki the paper matters well beyond its expository aim. It states cleanly several global facts that other threads here use but state loosely:

- the **integrality of Chern–Simons levels**, which underlies the group's Maxwell–Chern–Simons/self-dual program and Project 18 ([[non-invertible-symmetries-mcs]]);
- the **spin-structure dependence of θ-periodicity** ([[axionic-electrodynamics]]; course Semester I Week 12);
- **anomaly inflow** at a boundary ([[t-hooft-anomaly]]);
- the **TQFT reading of the fractional effect** ([[topological-order]]; course Semester II Week 10).

Witten also flags that the emergence of the Chern–Simons gauge field "is more a theoretical interpretation of experimental facts than a theorem about the solutions of the Schrödinger equation". That is precisely the gap the group's [[julia-toulouse-mechanism|Julia–Toulouse]] program addresses: effective gauge fields derived from defect condensation.

## Key Results

**§1. The Chern–Simons function.** Take a $G$-bundle with connection $A$ on a closed oriented 3-manifold $W=\partial X$, for example $G = SU(N)$. Define $\mathrm{CS}_X(A)=\int_X \mathrm{Tr}\,F\wedge F/8\pi^2$. Two extensions $X, X'$ glue into a closed $Y = X\cup\overline{X'}$, and $\mathrm{CS}_X-\mathrm{CS}_{X'} = \mathcal{I}_Y \in\mathbb{Z}$ is the instanton number of $Y$. Hence $\mathrm{CS}(A)\in\mathbb{R}/\mathbb{Z}$ depends only on $A|_W$. Physicists usually carry a factor $2\pi$, so their $\mathrm{CS}$ takes values in $\mathbb{R}/2\pi\mathbb{Z}$ (footnote 1).

**§2. Insulators as effective actions.** $I_{\rm eff} = I_{\rm Maxwell} + \int_S f(\vec E,\vec B,\partial\vec E,\dots)$, with $I_{\rm Maxwell} = \frac{1}{4e^2}\int F\wedge\star F$. The Taylor coefficients are restricted by $O(3)$ and by time reversal $T$:

- $\vec c\cdot\vec E$: a ferroelectric.
- $\vec c'\cdot\vec B$ ($T$-odd): a ferromagnet.
- $\epsilon\vec E^2+\mu\vec B^2+\gamma\,\vec E\cdot\vec B$: a dielectric, with $\gamma = 0$ if $T$ holds (footnote 4; see the θ = π caveat in [[axionic-electrodynamics]]).
- Derivative terms: dispersion. Anisotropic quadratic forms: birefringence. Cubic and higher terms: nonlinear optics.

The current is $\mathcal{J}=e^2\,\delta\widetilde I/\delta A$. Any term built from $\vec E,\vec B$ yields a current proportional to *derivatives* of the field, so the longitudinal conductivity vanishes. That is the precise sense of "insulator".

**§3. Two-dimensional materials: the integer effect.**

- *Spin structure is essential.* Spacetime is $M=\mathbb{R}\times Y$ with $Y$ a spin 3-manifold, and the film's worldvolume is $W = \mathbb{R}\times D$. On a spin 4-manifold $\int_X c_1^2$ is even, so the basic integer is $\int_X F\wedge F/8\pi^2$. For a $U(1)$ connection on a spin 3-manifold $W$ one therefore gets a well-defined $\mathrm{CS}(A)=\int_X F\wedge F/8\pi^2 \bmod \mathbb{Z}$, and it **depends on the spin structure**. Example: on $T^3=T^2\times S^1$, with $A$ pulled back from a degree-one connection on $T^2$, $\mathrm{CS}(A)=0$ or $\tfrac12$ according to the spin structure.
- *Local formulas.* $\mathrm{CS}(A)=\frac{1}{8\pi^2}\int_W A\wedge dA$ for a trivialized bundle, and $\delta\mathrm{CS}=\frac{1}{4\pi^2}\int\delta A\wedge F$. Critical points are flat connections.
- *Quantization.* $I_{\rm eff}\supset 2\pi k\,\mathrm{CS}(A)=\frac{k}{4\pi}\int A\,dA$ with $k\in\mathbb{Z}$. Two-dimensional insulators are thus classified by an integer.
- *The Hall current.* $J_y = \frac{e^2 k}{2\pi}E_x\,\delta(z)$, i.e. $\sigma_{xy} = \frac{k e^2}{2\pi\hbar} = k\,\frac{e^2}{h}$ (von Klitzing 1980; measured to about $10^{-9}$). Odd $k$ is observed, which is the physical imprint of the spin structure.
- *Edges.* When $\partial W=\Sigma\neq\emptyset$, $\exp(2\pi i k\,\mathrm{CS}(A))$ is not a number. It is a unit vector in a line $\mathcal{R}$ fixed by $A|_\Sigma$ (Ramadas–Singer–Weitsman). A boundary QFT whose partition function lives in $\mathcal{R}^{-1}$ restores well-definedness. This is **anomaly inflow** (Callan–Harvey). The edge theory is not fixed by $k$; the simplest choice has $Z = \det(\text{Dirac})^k$, i.e. $k$ chiral fermions.

**§4. The fractional effect.**

- *Topological degrees of freedom.* Relax "no relevant degrees of freedom" to "no relevant *local* degrees of freedom", which leaves a TQFT. The material carries an **emergent** $U(1)$ field $a$ with action $2\pi r\,\mathrm{CS}(a)$. Here $r\in\mathbb{Z}$, a spin structure is needed if $r$ is odd, and a Maxwell term is irrelevant at long distances when $r\neq0$.
- *The coupling to electromagnetism.* The mixed invariant $\mathrm{CS}(A,a)$, defined via $\int_X F\wedge f/4\pi^2$, needs **no** spin structure, since $c_1(\mathcal{L})c_1(\mathcal{M})$ can be odd. It enters with coefficient $2\pi s$, $s\in\mathbb{Z}$:
$$
I_{\rm int}=\int_W\Big(\frac{k}{4\pi}A\,dA+\frac{s}{2\pi}A\,da+\frac{r}{4\pi}a\,da\Big),\qquad sF+rf=0,\qquad \sigma_{xy}=\Big(k-\frac{s^2}{r}\Big)\frac{e^2}{h}.
$$
- *Laughlin's state.* $(k,s,r)=(0,1,-3)$ gives $\nu=1/3$ (Tsui–Störmer–Gossard 1982).
- *Closing remarks.*
  - Almost all known unitary 3d TQFTs are Chern–Simons theories (Moore–Seiberg).
  - Quasiparticle charge and spin, and the ground-state degeneracy on genus $g$, follow from the TQFT.
  - The $\nu=5/2$ state is believed to be non-abelian (Moore–Read), but "decisive experimental proof remains elusive".
  - Recent zero-field fractional quantum anomalous Hall states have been observed (Park et al. 2023).
  - Non-abelian Chern–Simons theory gives a QFT framework for the Jones polynomial.

**Evidence status** (labels as in the physics-research methodology):

| Claim | Status | Basis |
|---|---|---|
| Integer quantization of $\sigma_{xy}$ | **PROVED** under gap assumptions | TKNN (1982) and Avron–Seiler–Simon (1983) for free fermions; Hastings–Michalakis, CMP 334 (2015) 433 for interacting gapped systems on a torus. Witten's argument is the EFT version and assumes a local gapped effective action. |
| Rational $\sigma_{xy}$ with denominator bounded by the torus degeneracy | **PROVED** under assumptions | Bachmann–Bols–De Roeck–Fraas, J. Math. Phys. 62 (2021) 011901 [arXiv:2001.06458] |
| FQH described by an emergent abelian Chern–Simons theory | **STRONGLY SUPPORTED**, not derived | Experiment and numerics; the emergence is interpretation, by Witten's own caveat |
| $\nu = 5/2$ is non-abelian | **CONJECTURED** | Moore–Read; experimentally unsettled |
| Almost all unitary 3d TQFTs are Chern–Simons theories | **EXPECTED** (folklore) | Moore–Seiberg (1989) |

## Methods

- **Effective field theory as the organizing principle.** The effective action is expanded in fields and derivatives and pruned by symmetry. Material properties are read off from its Euler–Lagrange equations and currents.
- **Secondary characteristic classes via bordism.** A 3-manifold invariant is defined by extending to a bounding 4-manifold and showing independence mod $\mathbb{Z}$ with a gluing argument.
- **Well-definedness of $e^{iI}$** (Dirac; Feynman) as the source of quantization.
- **Spin geometry.** Evenness of the intersection form on spin 4-manifolds (Wu's formula) is the reason odd levels need a spin structure.
- **Boundaries.** Determinant lines (Ramadas–Singer–Weitsman) and [[t-hooft-anomaly|anomaly inflow]] (Callan–Harvey).

## Relevance

- **[[condensed-matter-connections]]: a common origin for the line's three topics.**
  - The line studies θ-electrodynamics, Weyl superconductors and monopole operators, and this article is the cleanest statement of the logic behind all three: response = effective action, and quantization = well-definedness of $e^{iI}$.
  - Read backwards, Witten's eq. (25), $\mathrm{CS}_X(A)=\int_X F\wedge F/8\pi^2$, says a film's Chern–Simons level is the $\theta/2\pi$ of a 4d region bounded by it. A θ-wall with $\Delta\theta$ carries level $\Delta\theta/2\pi$, so the $\theta=\pi$ surface of a topological insulator has half-integer level. That is *forbidden* for a standalone 2d insulator, which is why the surface must be anomalous. See [[axionic-electrodynamics]].
- **[[confinement-duality]]: the global input the Maxwell–Chern–Simons papers never needed until now.**
  - The MCS/self-dual duality (Marcelo's MSc thesis; PLB 605, 2005) and the Julia–Toulouse papers with a Chern–Simons term (PLB 674, 2009; PRD 88, 2013) were local, perturbative statements.
  - Project 18 ([[non-invertible-symmetries-mcs]]) is a question about *global* symmetry structure. It needs exactly Witten's §3–4 data: $k\in\mathbb{Z}$, spin structure for odd $k$, $|k|^g$ ground states, and the mixed term $\mathrm{CS}(A,a)$ with integer coefficient.
  - Witten's caveat on emergence is the opening for [[julia-toulouse-higher-form-symmetries|Project 17]]: a Julia–Toulouse derivation of the $(k,s,r)$ action with integrality built in.
- **[[bell-inequalities-qft]] and [[relative-entropy-qft]]: the edge as a type III₁ laboratory.**
  - By anomaly inflow, the edge of the $(k,s,r)$ fluid carries a chiral $U(1)$ current whose Schwinger term is the Hall conductance: $[\rho(x),\rho(y)] = \frac{i\nu}{2\pi}\delta'(x-y)$ with $\nu = k - s^2/r$. The **Pauli–Jordan distribution of the edge current is $\sigma_{xy}$**.
  - The edge is a chiral boson whose local algebra contains the electron vertex operator, which is fermionic for odd $r$, while quasiparticle operators with charge $e/|r|$ generate superselection sectors (for a Laughlin state, $k=0$, $s=1$, so $\nu = 1/|r|$ with $r<0$ in Witten's orientation).
  - This is precisely the object of the group's vertex-operator Tsirelson paper (Caribé–Guimarães–Roditi–Sorella, arXiv:2604.18513) and of the coherent-state Araki–Uhlmann computations. See Questions Raised §1.
- **Courses and the immersion program.**
  - The article is the natural reading for the "one honest lecture" on the fractional effect in the generalized-symmetries course (Semester II Week 10, `wiki/courses/generalized-symmetries-course/`). Its §3 gives the spin-structure condition for θ-periodicity, which Semester I Week 12 states in §3.3 and F5.
  - It is Track A reading for the [[immersion-plan]], and a compact specimen for the Witten writing apprenticeship: the question stated in words before any formula ("is it possible for a multiple of $\mathrm{CS}(A)$ to appear…?"), the classical answer set against the quantum one, rigor spent only where it changes the conclusion (the spin structure).

## Questions Raised

*Discussed with the researcher on ingest; not yet filed as question pages.*

1. **Edge Bell/relative-entropy laboratory.** On the edge of the $(k,s,r)$ fluid, $\nu$ normalizes the current's Pauli–Jordan distribution.
   - (a) What is the Araki–Uhlmann relative entropy between the vacuum and a quasiparticle-sector state localized in an interval? Longo's $U(1)$-current formula suggests it scales as $q^2/\nu$ at fixed profile: $\propto 1/|r|$ for the charge-$e/|r|$ Laughlin quasiparticle and $\propto |r|$ for the electron.
   - (b) Does the vertex-operator Tsirelson saturation of arXiv:2604.18513 survive when only the physically local vertex operators are admitted (electron-type, and fermionic for odd $r$, so graded locality applies)?
   - (c) The charge-counting operator $e^{2\pi i Q_I}$ acts trivially on integer charge and detects fractional charge; in the bulk it closes into a $\mathbb{Z}_{|r|}$ 1-form-symmetry loop. Is it a usable Bell observable?

   Links: [[bell-inequalities-qft]], [[relative-entropy-qft]], [[weyl-operators]].
2. **The global form of the MCS/self-dual duality.** On $T^2$ the MCS holonomy zero modes form a Landau problem with cyclotron frequency equal to the topological mass $m = ke^2/2\pi$ and a $k$-fold degenerate lowest level, the $U(1)_k$ TQFT. The self-dual model has no such sector. Is the precise statement MCS $\simeq$ SD $\otimes$ $U(1)_k$ (a spin TQFT for odd $k$)? What does this imply for the non-invertible symmetries of Project 18, and for the noncommutative version (PLB 605, 2005) next to Susskind's noncommutative-CS description of the Laughlin fluid? → [[non-invertible-symmetries-mcs]]
3. **A Julia–Toulouse derivation of Witten's $(k,s,r)$ action with exact integrality.** Condensing composite-boson vortices (the Zhang–Hansson–Kivelson/Read picture Witten cites) should produce $s=1$ and the level $r$. Can the modified-Villain lattice make $r\in\mathbb{Z}$ and the odd-$r$ spin requirement exact? Jacobson–Sulejmanpasic build lattice $U(1)_k$ from a lattice θ-term, which is the lattice version of eq. (25). Is the hierarchy iterated condensation? → [[julia-toulouse-higher-form-symmetries]]
4. **θ-walls, periodicity and pseudo-axion strings.**
   - A θ-wall with $\Delta\theta = \pi$ has half-integer level and must be anomalous.
   - $\theta \cong \theta+2\pi$ holds only with a spin structure; bosonic systems have $4\pi$ periodicity and the statistical Witten effect.
   - For the group's Weyl-superconductor pseudo-axion (a charge-$2e$ condensate), what are the correct periodicity and the Callan–Harvey modes on pseudo-axion strings?

   → [[axionic-electrodynamics]], [[condensed-matter-connections]]
5. **Magic along the MCS flow.** MCS runs from a local QFT, whose states must carry magic ([[2026-benedetti-magic-in-qft]]), to the abelian TQFT $U(1)_k$, whose link states are stabilizer states (Salton–Swingle–Walter). Where does the magic go? Long-range-magic work is crowded (2025–26), so the group's angle would be the modular/type III one. → [[magic-and-confinement-phases]]
6. *Pedagogical.* Footnote 5 notes that the argument can be run in Minkowski space using magnetic monopoles. A monopole crossing a level-$k$ film deposits charge $k$ (Laughlin's flux argument). Dirac-string invisibility gives $k\in\mathbb{Z}$, and for odd $k$ the resulting dyon's statistics is the spin-structure refinement. This would make a good course problem for Semester I Week 12 or Semester II Week 10.

## Reading Notes

**Five-line referee note** (the [[immersion-plan]] format):

- **Claim:** two-dimensional insulators are classified electromagnetically by an integer Chern–Simons level, and the fractional effect is an emergent abelian Chern–Simons TQFT coupled through $(k,s,r)$.
- **Method:** effective action, well-definedness of $e^{iI}$, and spin bordism.
- **Weakest step:** the existence of a local gapped effective action for $A$ is assumed, and the emergence of $a$ is explicitly not derived.
- **What would break it:** gapless bulks (e.g. the composite Fermi liquid at $\nu=1/2$), or non-abelian orders beyond abelian Chern–Simons.
- **Question for the author:** footnote 5 says the argument can be run in Minkowski space using monopoles. Does that version also see the spin-structure refinement, through the statistics of the dyon a monopole becomes after crossing an odd-$k$ film?

**Notation ledger.**

- Witten's $\mathrm{CS}\in\mathbb{R}/\mathbb{Z}$; the physics action is $2\pi k\,\mathrm{CS} = \frac{k}{4\pi}\int A\,dA$.
- Signature $-+++$ (mostly plus), whereas the playbook's group convention is $(+,-,-,-)$.
- $A$ is normalized so that charges are integers, with $e$ in front of the Maxwell term.
- $K$-matrix dictionary. In the common convention $\mathcal{L} = -\frac{1}{4\pi}K a\,da + \frac{t}{2\pi}A\,da$, Witten's $r = -K$ and $s = t$, and $\sigma_{xy} = k + t^{\mathsf T}K^{-1}t$. The generalized-symmetries course (Semester II Week 10) writes $+\frac{1}{4\pi}K a\,da$, the mirror image; there $r=K$, $s=t$ and $\sigma_{xy}=k-t^{\mathsf T}K^{-1}t$, and Witten's $\nu=1/3$ example $(k,s,r)=(0,1,-3)$ is $K=-3$, $t=1$.

**Minor slips in v1** (18 Sep). The v2 of 22 Sep announces "minor corrections"; whether they cover this list was not checked.

- Eq. (23) integrates over $M$ where $X$ is meant.
- Eq. (17) writes $I(\Phi,A)$ for $\widetilde I(\Phi,A)$.
- Eq. (11) drops the $1/e^2$ of eq. (9).
- Ref. [6] (Laughlin's 1981 gauge argument, the flux-insertion cousin of footnote 5) is listed but not cited in the text.
- The Chern–Simons 1974 paper itself is not in the bibliography, presumably taken as read in a Simons memorial issue.

**INSPIRE walk (parents).**

- Belavin–Polyakov–Schwarz–Tyupkin (1975) and 't Hooft (1976), on instantons (the latter ★ in Zotero).
- Dirac (1931).
- von Klitzing et al. (1980); Tsui–Störmer–Gossard (1982); Laughlin (1983).
- Witten, CMP 121 (1989).
- Callan–Harvey (1985).
- Zhang–Hansson–Kivelson and Read (1989).

The paper is too new for children.

## Related Papers

- E. Witten, *Quantum Field Theory and the Jones Polynomial*, CMP 121 (1989) 351. Non-abelian Chern–Simons theory, its Hilbert spaces on Riemann surfaces, and knot invariants (ref. [19]; with Wen, ref. [27], for the genus-$g$ degeneracy).
- E. Witten, *Fermion Path Integrals and Topological Phases*, RMP 88 (2016) 035001 [arXiv:1508.04715], and *Three Lectures on Topological Phases of Matter*, Riv. Nuovo Cim. 39 (2016) 313 [arXiv:1510.07698]. Both are ★ in Zotero. They carry the story into 3+1d: θ = π, $T$, η-invariants.
- E. Witten, K. Yonekura, *Anomaly Inflow and the η-Invariant*, arXiv:1909.08775. The modern inflow reference (immersion Track A).
- E. Witten, *From Superconductivity and Four-Manifolds to Weak Interactions*, Bull. AMS 44 (2007) 361. The companion Bull. AMS article (ref. [20]).
- C. G. Callan, J. A. Harvey, NPB 250 (1985) 427. Anomaly inflow on axion strings and domain walls, the same family as the group's pseudo-axion work.
- S. C. Zhang, T. H. Hansson, S. Kivelson, PRL 62 (1989) 82; N. Read, PRL 62 (1989) 86. Chern–Simons–Landau–Ginzburg theory and composite bosons, the condensation picture closest to [[julia-toulouse-mechanism|Julia–Toulouse]].
- T. Jacobson, T. Sulejmanpasic, *Modified Villain formulation of abelian Chern–Simons theory*, PRD 107 (2023) 125017 [arXiv:2303.06160]. Lattice $U(1)_k$ with level quantization, 1-form anomaly and monopole charge manifest, built from a lattice θ-term. See [[villain-action]].
- G. Salton, B. Swingle, M. Walter, *Entanglement from Topology in Chern–Simons Theory*, PRD 95 (2017) 105007 [arXiv:1611.01516]. $U(1)_k$ link states are stabilizer states.
- R. Longo, *Entropy of Coherent Excitations*, LMP 109 (2019) 2587. Vacuum relative entropy of coherent states on wedge algebras, including the $U(1)$-current formula: the formula to specialize to the edge.
- S. Hollands, *Relative entropy for coherent states in chiral CFT*, LMP (2020) [arXiv:1903.07508]. For stress-tensor coherent states the relative entropy is $c$ times a Schwarzian action; this is the $c=1$ edge's energy sector.
- J. G. A. Caribé, M. S. Guimarães, I. Roditi, S. P. Sorella, *Bosonization, vertex operators and maximal violation of the Bell-CHSH inequality in wedge regions*, arXiv:2604.18513 (2026). The group's chiral-boson Tsirelson construction, which the edge program would extend.
- [[2026-benedetti-magic-in-qft]]. Magic separates local QFT from TQFT, relevant to the Maxwell–Chern–Simons → $U(1)_k$ flow.
