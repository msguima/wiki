---
title: "Source map of the IAS lectures — Geometric QCD"
type: appendix
course: geometric-qcd-course-guide
modified: 2026-10-05
---

# Source Map

> **Edition 2.0 reading rule.** This table indexes the content and claims of the supplied slides; it is not an endorsement of those claims. The current [[courses/geometric-qcd-course/claim-status-map|claim map]] and corrected notes take precedence as teaching guidance. In particular, pp. 78–79 fail the literal tensor test in III.5; p. 108's radial kernel has total mass $3\pi^2$ with ordinary Lebesgue measure; p. 139's general claim about the planar pion is not adopted. Reported fit families are not automatically held out.


This file is the main coordination tool for the course pack. It maps every page of the source PDF to a module, mini-lecture, and the core objects appearing on that page, and flags strong claims that require a status label.

- **Source PDF:** `IASQCDLectures.pdf` — *The Complete 2026 IAS Lectures*, Alexander Migdal, IAS, March 27, 2026. 142 pages.
- **Extracted text:** `extracted/pages/p001.txt` … `p142.txt` (one file per page; layout extraction mangles superscripts/subscripts, so math is reconstructed in the notes from context).
- **Page numbering:** PDF page = footer page "X / 142". The page files are zero-padded `pXXX.txt`.

## Page Ranges by Module

| Module | PDF pages | Mini-lectures |
|---|---|---|
| Front matter | 1-3 | — |
| I — Loop Calculus & MM Equation | 4-42 | I.1-I.7 |
| II — Momentum Loop Space | 43-65 | II.1-II.7 |
| III — Hodge-Dual Minimal Surface | 66-91 | III.1-III.7 |
| IV — Majorana Fermions (Elfin) | 92-110 | IV.1-IV.7 |
| V — Twistor Spectrum | 111-142 | V.1-V.7 |

## Per-Module Arc

**Front matter (pp. 1-3).** Title, abstract, and series overview. Frames the whole program: large-$N_c$ planar QCD $\to$ string dual via Makeenko-Migdal; Hodge-dual rigid minimal surface vacuum; Majorana "Elves" inducing QCD; twistor exact-WKB $\to$ 36-state PDG meson fit. The abstract asserts all headline results; treat as advertisement, not proof.

**Module I (pp. 4-42).** Defines $W[C]$ (holonomy) and the goal $S_{\mathrm{eff}}[C]$ (string action); shows $\bar q q$ correlators are path integrals over Brownian quark loops, not fixed-contour $W$. Builds loop calculus from the hopping/disentangling identity (Lie-Trotter). Introduces loop derivatives and the diffusion operator $L$. States the Makeenko-Migdal equation and shows it bootstraps planar Feynman graphs. Climax: the coordinate-space catastrophe — cusp renormalization is not closed at self-intersections, so no renormalized single-contour $W[C]$ exists; must move to momentum space.

**Module II (pp. 43-65).** Transforms $W[C]\to W[P]$ by Fourier transform; contact $\delta^{(4)}(x-y)$ is absorbed natively by the loop measure. Derives the Momentum Loop Equation (MLE): finite, algebraic-differential, no cusps. Identifies the kinematic tensor and Magnus forms; uses the shuffle ideal. Solves $W^{(4)}$ and $W^{(6)}$ exactly. **Strong claim:** at $W^{(8)}$ the system is algebraically overdetermined. Q&A addendum defends the Cuntz-algebra Master Field and argues 4D geometry is necessary.

**Module III (pp. 66-91).** The nontrivial zero mode $L_\nu(W)=0$ corresponds to a classical Yang-Mills Master Field. The (anti)self-dual area derivative identically satisfies the loop diffusion equation. Goldschmidt-vs-Plateau analysis: the QCD vacuum must stay on the additive two-disk Goldschmidt branch. **Strong claim:** exact construction of the Hodge-dual minimal surface via 't Hooft matrices and a holomorphic map to $\mathbb C^4$; Virasoro constraint collapses Nambu-Goto to a quadratic Dirichlet functional; Hilbert transform solves the boundary. Active-vs-frozen twistors, parity restoration, OPE cancellation at $D=4$, gluon-condensate relation for $\kappa$.

**Module IV (pp. 92-110).** Majorana bispinor "Elves" on the surface with chiral bag boundary conditions. Conformal invariance: a Pauli-Villars regulator cancels the Liouville anomaly, so $\rho$ is a gauge variable. **Strong claim:** the Dirac determinant is a sum over closed loops weighted by $(-1)^\nu$; non-planar intersections cancel via the Pauli principle, leaving only planar 't Hooft diagrams. Computes first and second area derivatives ($A$-term, $B$-term). **Strong claim:** in the large-mass limit the Bianchi identity kills the $A$-term; White's bridge plus 't Hooft symbol algebra reduce the $B$-term to a universal kernel; the geodesic inequality localizes to $\delta^{(4)}(x-y)$; the MM equation is recovered; asymptotically free QCD is induced.

**Module V (pp. 111-142).** Twistor-parametrizes the loop measure; computes the Faddeev-Popov Jacobian. Liouville field $\rho=2\log u$; scale factors cancel. **Strong claim:** Minkowski formulation restores real saddles; a flat "monodromy valley" with steep transverse Hessian gives exact-WKB at large winding. Twisted boundary conditions (Meusnier helicoid); twistor monodromy projects to fixed $J$. Parametric Regge trajectories with a chiral bound and a topological vector index. **Strong claim:** 5-parameter global fit to 36 PDG meson states across 13 families with a single universal $\sqrt{\sigma}\approx417$ MeV; ~8.1% RMS mass error (excluding the pion). References to two Nuclear Physics B papers and a Wolfram Cloud notebook.

## Complete Page-by-Page Table

| PDF page | Slide title | Module | Core formulas/objects | Claim-status warning |
|---|---|---|---|---|
| 1 | Title page | Front matter | title, author, date | — |
| 2 | Abstract | Front matter | $W[C]$, $S_{\mathrm{eff}}$, MM equation, Hodge-dual surface, Majorana Elves, twistor exact-WKB, 36-state PDG fit | STRONG CLAIM (abstract asserts all headline results) |
| 3 | Series Overview | Front matter | 6-point lecture map (Modules I-V + Exact WKB) | — |
| 4 | The 50-Year Challenge | I.1 | Wilson loop $W[C]$ eq (1); string action $S_{\mathrm{eff}}[C]$ eq (2); cusp/perimeter/self-intersection UV obstacles | — |
| 5 | Wilson loop and physical amplitudes | I.2 | $\bar q q$ current correlator as path integral over velocity $v=C'$ eq (3); perturbative $W$; quark loop in momentum space eq (4) | — |
| 6 | Conclusions for $W[C]$ | I.2 | Brownian paths, infinite cusps; $W[C]$ not the right renormalization object for amplitudes | — |
| 7 | Parallel Transport and Loop Calculus | I.3 | Holonomy identity eq (5); product-integral definition eq (6) | — |
| 8 | Parallel Transport and Loop Calculus | I.3 | Infinitesimal disentangling (Lie-Trotter) eq (7); translation identity eq (8) | — |
| 9 | Parallel Transport and Loop Calculus | I.3 | Hopping identity eq (9); iteration/re-ordering eqs (10)-(11) | — |
| 10 | Parallel Transport and Loop Calculus | I.3 | Non-Abelian path-ordered $A(C_k)$; shifted argument $x_k=C_k$ eq (12); two ordered parts eq (13) | — |
| 11 | Parallel Transport and Loop Calculus | I.3 | Local $N\to\infty$ limit eq (14); closed-loop condition $\oint dC=0$ eq (15); holonomy $=W[C]\cdot I$ | — |
| 12 | Conclusions for $W[C]$ | I.3 | Base-point identity; bilocal $U(1,2)$ eqs (16)-(17); gauge invariance at closed loop eq (18) | — |
| 13 | The Loop Space Derivative | I.4 | Dot derivative $\delta W/\delta\dot C_\mu$ eq (19); area derivative $[D_\mu,D_\nu]$ eq (20); loop diffusion operator $L$ eq (21) | — |
| 14 | Leibniz property | I.4 | $L(AB)=L(A)B+AL(B)$; ansatz $W=W_{\mathrm{pert}}e^{-\kappa\,\mathrm{Area}}$ | — |
| 15 | The Makeenko-Migdal Equation | I.5 | MM equation eq (22); LHS loop diffusion, RHS loop splitting; factorization $W_2\to W\cdot W+O(1/N_c^2)$ | — |
| 16 | Graphic form of MM equation | I.5 | figure: MM equation with diffusion operator + integral term | diagram |
| 17 | Generating Planar Graphs (Bootstrap) | I.6 | frame diagrams; $\partial^{-2}\to$ gluon propagator $1/(x-y)^2$; commutator tensor structures | — |
| 18 | Discussion map: choose a fork | I.6 | Fork A planarity/combinatorics; Fork B UV/contact regularization; Fork C momentum loop space | — |
| 19 | Fork A: how the loop equation generates planar graphs | I.6 | large-$N$ factorization; $\delta(x-y)$ forces cyclic split $C=C_{xy}\cdot C_{yx}$; double-line planarity | — |
| 20 | Fork B: why coordinate space is singular | I.7 | contact term at self-intersections; cusps/Brownian; analytic regularization $1/k^2\to 1/(k^2)^{1+\varepsilon}$; point-splitting "wires" | — |
| 21 | Fork C: momentum loop space | I.7 | delta-contact catastrophe disappears; finite local functional-diff eq in $P(\theta)$; off-shell recursion | — |
| 22 | Phys. Rep. '83 excerpt: what to look for | I.7 | three ingredients: $\varepsilon$-softening, gauge-invariant point splitting, "wires" closure | — |
| 23 | From Phys Rep '83 (1) | I.7 | figure-only page | diagram |
| 24 | From Phys Rep '83 (2) | I.7 | figure-only page | diagram |
| 25 | From Phys Rep '83 (3) | I.7 | figure: analytic regularization of loop equation | diagram |
| 26 | From Phys Rep '83 (4) | I.7 | figure: analytic regularization of loop equation | diagram |
| 27 | From Phys Rep '83 (5) | I.7 | figure: analytic regularization of loop equation | diagram |
| 28 | From Phys Rep '83 (6) | I.7 | figure: analytic regularization of loop equation | diagram |
| 29 | From Phys Rep '83 (7) | I.7 | figure: analytic regularization of loop equation | diagram |
| 30 | From Phys Rep '83 (8) | I.7 | figure-only page | diagram |
| 31 | Bootstrap equation in detail | I.6 | area derivative eq (23); source $J_\nu$ eq (25); inversion operator expansion eq (26) | — |
| 32 | Brownian path representation | I.6 | area-derivative identity eq (27); Brownian path $\Gamma$ representation eq (28) | — |
| 33 | Graphic Form of Bootstrap equation | I.6 | figure: path integral (28) with Brownian paths | diagram |
| 34 | Gluon graphs by iterations of Bootstrap equation | I.6 | $\lambda$-iteration from $W[0]=1$; reproduces planar graphs incl. ghost loops; recovers planar beta-function | slide claim (recovery of all planar graphs) |
| 35 | Summary of the Bootstrap Approach 1 | I.6 | frame diagrams as planar trees with $W$-glazed windows; Brownian sums $\to$ gluon propagators | — |
| 36 | Summary of the Bootstrap Approach 2 | I.6 | manifest gauge invariance; unique Faddeev-Popov recovery; ghost loops | — |
| 37 | The Coordinate Space Catastrophe | I.7 | $\delta^{(4)}(x-y)$ contact; cusp divergence $\log W\sim -\Gamma_{\mathrm{cusp}}(\gamma)\log(\Lambda_{\mathrm{UV}}L)$ eq (29) | — |
| 38 | Self-intersection and four wedges | I.7 | figure: four wedges $\theta_1,\dots,\theta_4$ at self-intersection | diagram |
| 39 | Why multiplicative cusp renormalization is not closed at intersections (1) | I.7 | angle-dependent $Z(\theta_i)$; LHS has 4 cusps, RHS only 2; missing $Z(\theta_2)Z(\theta_4)$ | — |
| 40 | How the loop diffusion operator cancels divergent diagrams | I.7 | $L$ cancels $\theta_2,\theta_4$ wedge diagrams; no local limit for $L$; coordinate-space $W$ not stable under RG | — |
| 41 | RG: local operators vs. Wilson loops on Brownian paths | I.7 | local OPE RG eq; $W[C]$ is nonlocal; Brownian $\Rightarrow$ infinite cusp density; strategy: go to momentum loop space | — |
| 42 | Summary of Lecture I | I.7 | MM defining planar loop dynamics; Brownian amplitudes; coordinate UV not the observable RG; way forward = momentum space | — |
| 43 | Lecture II title | II.1 | title slide | — |
| 44 | Discussion map: choose a fork | II.1 | Fork A momentum space; Fork B algebraic MLE (Magnus, shuffle); Fork C catastrophe at $W^{(8)}$ | — |
| 45 | Regularization, Renormalizability, and Lattice QCD | II.1 | lattice breaks $O(4)$/Hodge duality; continuum needed for instantons & Hodge surfaces; use fermion mass $m$ as UV cutoff | — |
| 46 | Shifting the Paradigm: From Coordinates to Momentum | II.1 | $W[P]$ Fourier transform eq (30); loop measure $D_C$ eq (31); cusps integrated out | — |
| 47 | Quark Loop Amplitudes in Phase Space | II.2 | Dirac path amplitude $K[P]$ eq (32); full scattering $A[q_1,\dots,q_n]$ eq (33); $Q(t)=\sum q_k\Theta(t-t_k)$ | — |
| 48 | Feynman Wheel | II.2 | figure: momentum loop $W[P]$ (inner) + Dirac rim $K[P]$; external momenta $q_k$ | diagram |
| 49 | Factorization of the Measure in Momentum Space | II.3 | self-intersection measure factorizes $D_C=D_{C_{12}}D_{C_{21}}$ eq (34); $\delta^{(4)}$ absorbed by sub-loop measure | — |
| 50 | The Momentum Loop Equation (MLE) | II.3 | coordinate MM eq (35) $\to$ momentum MLE eq (36); no delta, no cusps, finite algebraic-differential | formal (transform from coordinate MM to MLE) |
| 51 | The Kinematic Tensor and the Shuffle Ideal | II.4 | $\hat L_\nu=T^{\alpha\beta\gamma}_\nu\Omega^{(3)}$ eqs (37)-(38); Magnus form $\Omega^{(3)}$; Dynkin projector $T$ eq (39); Ree's theorem annihilates shuffle ideal | — |
| 52 | Algebraic Recurrence for the MLE | II.4 | $W[P]$ expansion in $\Omega^{(n)}$ eq (40); functional derivative brings commutator eqs (41)-(42) | — |
| 53 | The Magnus forms MLE | II.4 | figure: recurrent equation for $W_n$ coefficients; blobs with wavy legs, rhombus 4-tensor $T$ | diagram |
| 54 | Topological Closure and Exact Solutions | II.5 | $\Omega^{(1)}=\oint P'd\theta=0$; boundary gap $P_{\mathrm{closed}}'$ eq (43); $W^{(4)}$ and $W^{(6)}$ solved exactly | — |
| 55 | Exact Algebraic Solutions up to $O(P'^5)$ | II.5 | $W^{(4)}$ eq (44); $W^{(6)}$ eq (45) in $(n-1)!!$ Wick-contraction Kronecker basis | — |
| 56 | The Breakdown: Mathematical Contradiction at $W^{(8)}$ | II.6 | RHS source $W^{(4)}\times W^{(4)}$; commutator $D(W^{(8)})$ annihilates symmetric structures; rank crushed | STRONG CLAIM — failure of Taylor-Magnus at $W^{(8)}$ |
| 57 | The Root Cause: Vector vs. Scalar Mismatch | II.6 | vector $\hat L_\nu W=\partial_P(W\times W)$ eq (46) vs scalar $W[P]$; scalar grows $4\times$ slower; overdetermined | STRONG CLAIM — vector/scalar mismatch |
| 58 | The Consequence for Naive String Theories | II.6 | loop eq descends from vector YM; Nambu-Goto Laplacian is scalar; cannot satisfy vector MLE | STRONG CLAIM — naive bosonic strings inadequate |
| 59 | Physical Meaning: The Non-Analytic Vacuum | II.7 | $W[P]$ not analytic in $P(\theta)$; no indefinite Taylor-Magnus; Elfin theory provides the "conspiracy"; ultra-local factorized solution | STRONG CLAIM — exact solution non-perturbative/non-analytic |
| 60 | Summary of Lecture II | II.7 | momentum space cures UV; Magnus solvable to 6th order; vector/scalar mismatch at 8th; naive strings fail | STRONG CLAIM (summary) |
| 61 | Addendum: Questions & Answers (title) | II.7 | section divider | — |
| 62 | Q&A 1: Does the Trace Ansatz Restrict Generality? | II.7 | $W=\mathrm{tr}\,\hat T\exp(i\hat X_\mu dP_\mu)$; $N_c\to\infty$ infinite Hilbert space; Cuntz algebra $a_\mu a^\dagger_\nu=\delta_{\mu\nu}$; zero trace identities | — |
| 63 | Q&A 2: The Single Universal Operator | II.7 | $\hat X_\mu=a_\mu+\sum Q_{\mu,\mu_1..\mu_k}a^\dagger_{\mu_1}\cdots$ eq (47); infinite tower of planar moments $Q$ | — |
| 64 | Q&A 3: Can the MLE be Absorbed into a Closed Algebra? | II.7 | RHS = Cuntz automorphism (works for scalar); fails for vector MLE: $\hat L_\nu W=T\Omega^{(3)}\cdot W$ eq (48); degree-1 derivation $\neq$ degree-3 shuffle | — |
| 65 | Q&A 4: The Necessity of 4D Geometry | II.7 | 1D Cuntz space lacks geometric DOF for 2D Yang-Mills stress; reason for $W^{(8)}$ failure; need Hodge-dual surface | STRONG CLAIM — 4D geometry mandated |
| 66 | Lecture III title | III.1 | title slide | — |
| 67 | Discussion map: choose a fork | III.1 | Fork A loop zero modes; Fork B topological stability (Plateau/Goldschmidt); Fork C Hodge-dual geometry | — |
| 68 | The Big Picture: The Continuum Solution | III.1 | quantize Fermi-string (1981) on rigid Hodge-dual surface; bulk rigid, holographically fixed; no Liouville instability | — |
| 69 | The Singular Solution of the MLE and the QCD Vacuum | III.1 | trivial zero mode $L_\nu(W)=O(P^3)$ eq (49); nontrivial zero mode $L_\nu(W)=0$ eq (50); classical YM $[D_\mu,F_{\mu\nu}]=0$ eq (51) | — |
| 70 | The Area Derivative and Loop Equation | III.2 | regular area derivative eq (52); loop diffusion eq (53); zero mode $W=\exp(-\kappa S[C])$ requires $L_\nu(S)=0$ | STRONG CLAIM — exact zero mode exists |
| 71 | Self-Duality in Loop Space | III.2 | (anti)self-dual area derivative $\star\delta S/\delta\sigma=\pm\delta S/\delta\sigma$ eq (54); Bianchi/Jacobi eqs (55)-(56) | STRONG CLAIM — self-dual surface solves MM exactly |
| 72 | Compatibility with the MM Equation | III.2 | $W=\exp(-\kappa S_\chi)W_{\mathrm{fluct}}$ eq (57); superposition of (A)SD gauge fields eq (58); MM with contact eq (59) | — |
| 73 | Topological Stability: Area Functional at Intersections | III.3 | additivity $S[C]=S[C_{xy}]+S[C_{yx}]$ required; Goldschmidt (two disks) vs Plateau (catenoid); phase-transition question | — |
| 74 | Visualizing the Topological Phase Transition | III.3 | figure: subloops rotate; catenoid vs Goldschmidt; $S_{\mathrm{add}}$ vs $S_{\mathrm{conn}}$ | diagram |
| 75 | Classical Physics vs. Planar QCD: The Catenoid | III.3 | soap film $\to$ catenoid; QCD string forbids connected cylinder (destroys planar factorization); vacuum trapped on Goldschmidt branch | STRONG CLAIM — catenoid forbidden as QCD vacuum |
| 76 | Mathematical Stability of the Goldschmidt Branch | III.3 | Douglas & Rado; Gulliver's barrier; White's bridge principle; varifold convergence | — |
| 77 | The Physical Vacuum: Multi-Instanton Resummation | III.4 | zero mode $\equiv$ multi-instanton vacuum resummation; $S_\chi$ translation-invariant holographic representation | STRONG CLAIM — geometric zero mode = instanton vacuum |
| 78 | Constructing the Hodge-Dual Minimal Surface | III.5 | $S_\chi[C]=\min\int\sqrt{\Sigma^2/2}$; Hodge constraint $\star\Sigma=\chi\Sigma$; 't Hooft matrices $\eta^{\chi,i}_{\mu\nu}$ eq (60); holomorphic ansatz eq (61) | — |
| 79 | Boundary Conditions and Area Duality | III.5 | Dirichlet in $\mathbb C^4$: $2\mathrm{Re}\,f_\mu=C_\mu$ eq (62); $\Sigma=2(F+\chi\star F)$ eq (63); auto Hodge-dual eq (64) | STRONG CLAIM — area element auto Hodge-dual for any holomorphic $f$ |
| 80 | The Virasoro Constraint & Uniformization | III.5 | reparam invariance; uniformization $\to$ isothermal coords; Virasoro null $(f'_\mu)^2=0$ eq (65); Nambu-Goto $\to$ quadratic $L=g_{\bar z z}\propto|f'|^2$ eq (66) | — |
| 81 | Exact Zero Modes and the Hilbert Transform | III.5 | Hilbert transform solution $f=\tfrac12(1+iH)C$ eq (67); $S_+=S_-\propto\int|f'|^2$; $L_\nu(S_\pm)=0$ eq (68) | STRONG CLAIM — each chirality solves MM independently |
| 82 | Spinor Factorization and Gauss Maps | III.6 | twistor factorization $f'_{a'\dot b}=\lambda_{a'}\mu_{\dot b}$; $e=2(\bar\lambda\lambda)(\bar\mu\mu)$; area derivative $=-n_i\eta^{\alpha\beta}$; left/right Gauss maps $n^+_i,n^-_i$ | — |
| 83 | The True Difference: Active vs. Frozen Twistors | III.6 | SD: left $SU(2)$ active ($\lambda$ poles, $\mu$ const); ASD: right $SU(2)$ active; one chiral twistor sector permanently frozen | STRONG CLAIM — Hodge-dual distinct from generic minimal surface |
| 84 | Parity Restoration & Why Not Nambu-Goto? | III.6 | $S=\tfrac12(S_++S_-)$ eq (69); NG lacks chiral decomposition; NG contact singularities $(\delta y)^2|\delta x|$ bypassed by chiral solution | — |
| 85 | String Scale and the Operator Product Expansion | III.7 | OPE 2nd area derivative eq (70); conformal short-distance tensor $I_{\mu\lambda}$ eq (71); antisymmetric projector $\Pi$ | — |
| 86 | The OPE Cancellation at $D=4$ and the Gluon Condensate | III.7 | $S(d)=(d-1)(d-4)$ eq (72) $\Rightarrow$ zero at $D=4$; surviving gluon condensate eq (73); $\kappa^2=\pi^2D\alpha_s\langle G^2\rangle/(8N_c\pi)$ eq (74) | STRONG CLAIM — dimensional miracle at $D=4$; $\kappa$ from SVZ condensate |
| 87 | The Physical Vacuum and the MLE Singularity | III.7 | $W[P]=\int DQ\,G[P-Q]W_{\mathrm{fluct}}[Q]$ eqs (75)-(76); non-local, non-analytic; resolves $W^{(8)}$ contradiction | STRONG CLAIM — explicit singular resolution of $W^{(8)}$ |
| 88 | Helicoid of the rigid string | III.7 | figure: Meusnier helicoid (1785); $X(\tau,r)$ eq (77); metric $g_{ab}$ eq (78) | diagram |
| 89 | The holographic string and Regge trajectories | III.7 | $V=\sigma R$, $\sigma=\sqrt2\cdot 2\kappa$; effective action $S$ eq (79); $L(v,\omega)$ eq (80); linear Regge $E^2\to 2\pi\sigma J$ eq (81); rigid stick, no vibrations | — |
| 90 | Philosophical Discussion: Quantum Physics vs. Classical Models | III.7 | no literal string/surface energy in QCD; minimize vacuum energy, not surface area; no bulk fluctuations | interpretive |
| 91 | Summary of Lecture III | III.7 | zero mode = multi-instanton vacuum; Goldschmidt additivity; Hodge-dual holomorphic embedding; active/frozen twistors; gluon-condensate $\kappa$ | STRONG CLAIM (summary) |
| 92 | Lecture IV title | IV.1 | title slide | — |
| 93 | Discussion map: choose a fork | IV.1 | Fork A Elfin theory; Fork B topological stability (Vdovichenko/Ising); Fork C recovering MM eq (geodesic inequality, asymptotic freedom) | — |
| 94 | The Elfin Theory on a Flat Surface | IV.1 | Majorana bispinor $\psi^\alpha_\lambda$; action $A_0$ eq (82); chiral bag BC $\sigma_3\psi=\lambda\psi$ eq (83); Pauli wall repulsion | — |
| 95 | Conformal Metric as a Local Gauge Parameter | IV.1 | curved metric $g=e^{2\rho}\delta$; $A_\rho$ with Liouville + spinor connection; functional integral $Z$ eq (84); PV regulator cancels Liouville variation | — |
| 96 | The fermions on a curved surface | IV.2 | full action $A_\rho$ eq (85); spinor connection $\nabla_k$ eq (86); vierbein/curvature eq (87); $\rho=\ln\sqrt e$ reduces to constant-mass Dirac on $S$ | — |
| 97 | General Covariance and the 2D Spinor | IV.2 | 2D metric $\to$ conformally flat; torsion-free locks $\omega_k=\tfrac12\varepsilon_{kl}\partial_l\rho$ eq (88); single scalar $\rho$ suffices | — |
| 98 | Conformal Anomaly and the Gauge Variable $\rho$ | IV.2 | Dirac operator anomaly $D\to e^{-3\delta\rho/2}De^{-\delta\rho/2}$; Jacobian canceled by Liouville; $\rho$ dummy gauge; use $\rho=0$ for proofs, $\rho=\ln\sqrt e$ for twistor string | — |
| 99 | Fermion Determinants & Planar Topology | IV.3 | $\Delta=\Delta_+\Delta_-$ as sum over closed vacuum loops; weight $A[\Gamma]=(-1)^\nu\exp(-ml_\Gamma)$ eq (89); Gauss-Bonnet $\sum\Delta\theta=2\pi(1-\nu)$ eq (90) | — |
| 100 | Cancellation of Intersections: The Pauli Principle | IV.4 | figure: planar & non-planar line collisions; Vdovichenko/Ising analogy; non-planar vertex cancels planar-touching; $(\bar\psi_R\psi_R)^2=0$ | STRONG CLAIM — Pauli principle annihilates non-planar graphs |
| 101 | Emergence of the Planar String | IV.4 | figure: hierarchy of trapped non-intersecting loops; time slice = Elf-pair string; matches 't Hooft planar expansion; gluon forces $\equiv$ Elf fluctuations | STRONG CLAIM — planar QCD induced from Elf determinants |
| 102 | Loop Equations on the Minimal Surface (1st deriv) | IV.4 | $\delta e/\delta\sigma_{\mu\nu}=2T_{\mu\nu}\delta^{(2)}(x-y)$ eq (91); first area derivative of $Z[S]$ eq (92); figure: path $\Gamma$ cuts surface into $S_{\mathrm{in}}/S_{\mathrm{out}}$ | diagram |
| 103 | Loop Equations on the Minimal Surface (2nd deriv) | IV.4 | second area derivative: $A$-term (disconnected, two loops $\Gamma_l,\Gamma_r$) + $B$-term (one loop touching $C$ at two points); two figures | diagram |
| 104 | Large Fermion Mass Limit | IV.5 | $m\gg\Lambda_{\mathrm{QCD}}$ eq (93); UV cutoff; $\delta^2 Z/\delta\sigma_{\mu\nu}\delta\sigma_{\alpha\beta}=A+B$ eq (94); locally flat geometry | — |
| 105 | The A-term: Vanishing by the Bianchi Identity | IV.5 | $A_{\mu\nu\alpha\beta}\to T_{\mu\nu}T_{\alpha\beta}Za^2$; $\propto\delta^2 S/\delta\sigma\delta\sigma\,\exp(-\kappa S)$ eq (95); $\int dx^\beta\cdots=-\partial_\mu\delta S/\delta\sigma$ eq (96); zero by Bianchi | STRONG CLAIM — $A$-term identically vanishes (Hodge self-duality used) |
| 106 | White's Bridge and the Contact Term | IV.6 | figure: crescent $S_{\mathrm{mid}}$ collapsing; White's bridge aligns $T(l),T(r)$; product $\to -\tfrac14\delta_{\alpha\nu}$ | diagram |
| 107 | The B-term: Generating the MM Contact Term | IV.6 | $T_{\alpha\mu}(r)T_{\mu\nu}(l)\to-\tfrac14\delta_{\alpha\nu}$ via 't Hooft symbols; universal kernel for MM | — |
| 108 | Recovering the Makeenko-Migdal Equation | IV.6 | geodesic inequality $L_{\mathrm{geo}}\ge|x-y|$ eq (97); smeared $\delta_m^{(4)}$ eq (98); exact MM eq (99) with $\lambda\propto Z[1]^2$; Hodge self-duality + tangent identity | STRONG CLAIM — Elfin determinant recovers MM equation exactly |
| 109 | Inducing Asymptotically Free QCD | IV.7 | figure: bootstrap path integral (delta = straight double line, Brownian = crescent); $Z[1]^2\to0\Rightarrow\lambda\to0$; $\Lambda_{\mathrm{QCD}}$ formula eq (100) | STRONG CLAIM — asymptotically free QCD induced from Elves |
| 110 | Summary of Lecture IV | IV.7 | Elfin theory mimics gauge-invariant loop dynamics; Pauli $\to$ planar; White's bridge $\to\delta^{(4)}$; induced QCD; Casimir from Elf zero-point (not string vibrations) | STRONG CLAIM — Majorana fermions induce planar QCD |
| 111 | Lecture V title | V.1 | title slide | — |
| 112 | Discussion map: A straight path to the QCD Mass Spectrum | V.1 | Fork A quark phase space; Fork B WKB & monodromy; Fork C exact spectrum (PDG fit) | — |
| 113 | Twistor Parametrization of the Loop Space Measure | V.2 | phase-space measure eq (101); Virasoro $(f'_\mu)^2=0$; null twistor factorization $f'_{a'}\sigma^\alpha=\lambda\otimes\mu$ eq (102); $v_\alpha=2\mathrm{Re}(iz\lambda\sigma_\alpha\mu)$ eq (103); Faddeev-Popov $\bar\lambda\lambda=\bar\mu\mu$ | — |
| 114 | The measure change from loop velocity to twistors | V.2 | norm $\|\delta v\|^2$ eq (104); quadratic form $\delta\Lambda^\dagger\hat Q\delta\Lambda$ eq (105); $4\times4$ block kernel $\hat Q$ eq (106) | — |
| 115 | The local Jacobian | V.2 | eigenvalues $\omega_1=0$ (gauge), $\omega_2=2\Lambda$ (dilatation), $\omega_{3,4}=\Lambda$; Faddeev-Popov $d^4v=\sqrt{\det'Q}\,d\Omega_{\mathrm{FP}}$ eq (107); $\sqrt{\det'Q}=\sqrt{2\Lambda^3}$ eq (108) | — |
| 116 | Elimination of the zero mode | V.2 | gauge orbit $\delta\lambda=\delta r\,\lambda$, $\delta\mu=-\delta r\,\mu$ eq (109); $\|\delta g_{\mathrm{auge}}\|^2=2\Lambda(\delta r)^2$ eqs (110)-(111); $J_{\mathrm{total}}=2\Lambda^2$ eq (113) | — |
| 117 | Summary and Interpretation of Twistor parametrization | V.2 | $\mathrm{Diff}(S^1)$ gauge-fixed; Faddeev-Popov Jacobian; residual $U(1)$; normalized spinors on $S^3\times S^3/U(1)$ | — |
| 118 | Local limit of $W[P]$ using effective action of Elfin theory | V.3 | Fourier integral $W[\hat P]$ eq (114); effective Lagrangian $L(z,\bar z)$ eq (115); zero-mode $k_\mu\to\delta(\oint v\,d\theta)$ | — |
| 119 | Polar Coordinate Parametrization of the Null Twistor Measure | V.3 | $\lambda=u\xi$, $\mu=v\eta$ eq (117); constraint $u=v$ eqs (116),(118); measure $\propto u^5\,du\,d\Omega_\xi d\Omega_\eta$ eq (119); coset $(S^3\times S^3)/U(1)$ eq (120) | — |
| 120 | Reduction to $u,\xi,\eta$ Variables | V.3 | path integral eq (121); Liouville field $\rho=2\log u$ eq (122); $u^5du=e^{3\rho}d\rho$ eq (123); measure $\int d\rho\,e^{3\rho}$ eq (124) | — |
| 121 | Phase space path integral for quark loop amplitudes | V.3 | einbein $e(\theta)>0$; eq (125); $\int du\,\exp(-u\,i\gamma\cdot P)=1/(i\gamma\cdot P)$ eq (126) | — |
| 122 | Phase space path integral (cont.) | V.3 | Fourier integral $I(\tau)=\int d^4q\,\exp(iq\cdot\tau)/(i\gamma\cdot q)$ eq (127); $I(\tau)\propto i\gamma\cdot\tau/(\tau^2)^2$ eq (128); $\tau^2=e^{2\rho}$ eq (129); $I(\tau)\propto e^{-3\rho}[i\gamma\cdot\mathrm{Im}(\cdots)]$ eq (130) | — |
| 123 | Holographic Liouville Theory and Exact Scale Invariance | V.4 | $e^{-3\rho}$ (momentum inversion) cancels $e^{+3\rho}$ (twistor Jacobian); scale-invariant $dP\wedge dC\sim\hbar$; 1D boundary sigma model + induced Liouville anomaly | — |
| 124 | Twistor Holography vs. Topological Twistor String | V.4 | $S_{\mathrm{Liouville}}$ eq (131); 4D bulk projected to 1D boundary; no fluctuating worldsheet metric; distinct from Witten's topological WZW twistor string; akin Penrose Non-Linear Graviton | interpretive |
| 125 | Path integral in Minkowski space and the Exact-WKB Valley | V.5 | Euclidean obstruction; Minkowski restoration (real saddles, no tachyons, $J\ge0$); flat monodromy valley + steep transverse Hessian; large-winding freezing | STRONG CLAIM — exact-WKB via monodromy valley |
| 126 | Twisted Boundaries: The Helicoid | V.5 | Fourier projection $\hat P^A_J=\int d\alpha\,\exp(-ik\alpha J)A_k(\alpha)$ eq (132); figure: Meusnier helicoid; $d\hat X\to M(\alpha)d\hat X M^\dagger(\alpha)$ eq (133) | diagram |
| 127 | Twistor in Minkowski space and twisted boundary conditions | V.5 | $dX=\varphi\varphi^\dagger d\xi+\psi\psi^\dagger d\eta$ eq (134); complex eigenvectors $\varphi(\xi),\psi(\eta)$ eq (135); $SU(2)$ target-space monodromy | — |
| 128 | Twistor monodromies | V.6 | branch point $z^a,\bar z^a$ eq (136); $M(2\pi a)$ monodromy eq (137); $dX(\tau+2\pi)=M\,dX\,M^\dagger$ eq (138); $\alpha=4\pi a$ projection | — |
| 129 | The metric and its light cone boundaries | V.6 | $\Omega^2=|\varphi_1\psi_2-\varphi_2\psi_1|^2$ eq (139); $=R^2\cos^2(2a\theta)$ eq (140); $ds^2=R^2\cos^2(2a\theta)(d\tau^2-d\theta^2)$ eq (141); endpoints at speed of light; massive truncation | — |
| 130 | Minkowski Action monodromy | V.6 | $\beta=2a\theta_b$; target-time $\Delta X^0=2\pi ER$ eq (142); minimal area $\Delta S_{\mathrm{Area}}$ eq (143); Liouville $\Delta S_{\mathrm{Liouv}}$ eq (144); proper mass $\Delta S_{\mathrm{mass}}$ eq (145) | — |
| 131 | The Minkowski Minimal Surface Action | V.6 | $\Delta S=a\,\Phi(E,K,\beta)$; $\Phi=\Phi_1+\cdots+\Phi_5$; $n=0$ only Bohr-Sommerfeld; $\beta=0$ non-relativistic, $\beta\to\pi/2$ massless | STRONG CLAIM — exact-WKB quantization ($n=0$ only) |
| 132 | Stationary metric, linear $a$ dependence and exact spin projection | V.6 | classical $A_J$ eq (146); winding sum; simple pole $1/\Phi_\star$; $A_J^{\mathrm{cl}}\propto 4\pi i\log k_{\max}/\Phi_\star$ eq (147) | — |
| 133 | Steep walls of the flat valley and Hessian determinant | V.6 | Hessian $H\propto k$; $\zeta(0)=-1/2$; fluctuation weight $k^{1/4}$; sum $\propto k_{\max}^{1/4}/\Phi_\star$ eqs (148)-(149); pole preserved | STRONG CLAIM — exact-WKB status (mechanism clear, rigorous proof pending) |
| 134 | The Parametric Regge Trajectories | V.7 | constituent mass $\bar x=x+\sqrt{x^2-1/(3\pi)}$; $E(\beta),J(\beta),K(\beta)$ eqs (150)-(152); chiral bound $x\ge1/\sqrt{3\pi}$; topological vector index $q$ ($q=0$ pseudoscalar, $q=-1$ vector) | — |
| 135 | Asymptotics: Relativistic Drag and Non-Relativistic Hook | V.7 | ultra-relativistic $J(E)$ eq (153) with $O(\sqrt E)$ slope-softening; non-relativistic hook $J(E)$ eq (154), $dJ/dE\to0$ at threshold | — |
| 136 | Global Fit: Comparison with Experimental Meson Spectrum | V.7 | figure: exact twistor-string Regge trajectories vs 36 PDG states, 13 families; $\sqrt{\sigma}\approx417$ MeV; $m_{u,d}\approx136$ MeV, $m_s\approx219$ MeV, $m_c\approx1.60$ GeV, $m_b\approx5.07$ GeV; $D_s,B_s,B_c$ included in the reported family comparison | STRONG CLAIM — 36-state PDG meson fit, single universal tension |
| 137 | A Unified Spectrum: Linear for Light, Curved for Heavy | V.7 | $\pi,\rho$ linear asymptote with $O(\sqrt E)$ drag; $D,B$ non-relativistic hook; universal kinematics $140$ MeV$\to6.27$ GeV $B_c$; ~8.1% RMS error $\approx O(1/N_c^2)$ | STRONG CLAIM — global planar universality |
| 138 | Fit Accuracy: Physical and Geometric Metrics | V.7 | $\delta m_{\mathrm{RMS}}\approx8.1\%$ (excl. pion); $\Delta J_{\mathrm{RMS}}\approx0.18$ ($<1/5$ orbital step); $\Phi_{\mathrm{RMS}}/2\pi\approx0.36$ (~$1/3$ quantum level) | STRONG CLAIM — quantitative fit accuracy |
| 139 | Conclusion: The QCD String is Derived, Not Postulated | V.7 | loop eq $\to$ finite MLE $\to$ $W^{(8)}$ failure $\to$ 4D Hodge-dual geometry $\to$ twistor string; Elves induce planar QCD; meson masses from twistor monodromy; chiral mass gap is geometric reality; pion needs non-planar chiral condensate | STRONG CLAIM — QCD string derived, not postulated; massless pion outside $N_c=\infty$ |
| 140 | Outlook: The Loop Calculus as a Skeleton Key to Nonlinear Flows | V.7 | planar glueballs/baryons (Y-junction); 3D Navier-Stokes HD turbulence (Sreenivasan DNS); MHD turbulence phase transition at $Pr=1$; turbulent mixing / Euler totient; "skeleton key" vs Polyakov's "master key" | interpretive |
| 141 | References and Supplementary Material I | V.7 | Geometric QCD I & II (Nucl. Phys. B 2026); Turbulence arXiv:2511.02165v3; interactive Mathematica 5D mass fit (link/QR) | diagram (QR/code link) |
| 142 | References and Supplementary Material II | V.7 | Twistor String With Quark Masses (Wolfram Cloud notebook); blog "Turbulence: Harmony of Primes"; main website | — |

## Diagram-Heavy Pages (visual inspection of the original PDF recommended)

The text extraction loses all visual information. These pages should be cross-checked against the original PDF:

- **p16** — graphic form of the MM equation.
- **p23-p30** — eight consecutive figure-only pages (Phys. Rep. 1983 scans of analytic regularization); essentially no extractable text. **High priority.**
- **p33** — graphic form of the bootstrap equation (Brownian paths).
- **p38** — four wedges at a self-intersection.
- **p48** — Feynman wheel (momentum loop + Dirac rim).
- **p53** — Magnus-form recurrence diagram.
- **p74** — catenoid-vs-Goldschmidt topological phase transition.
- **p88** — Meusnier helicoid bounded by a double helix.
- **p100** — planar vs non-planar line collisions (Pauli principle).
- **p101** — hierarchy of trapped non-intersecting loops.
- **p102, p103** — first and second area derivatives of $Z[S]$ (two figures on p103).
- **p106** — White's bridge (collapsing crescent).
- **p109** — bootstrap path integral (delta = straight double line, Brownian = crescent).
- **p126** — twisted-boundary helicoid.
- **p136** — **the central spectrum-fit plot**: parametric Regge trajectories overlaid on the 36-state PDG meson spectrum. **Highest priority for verifying the 8.1% fit claim.**
- **p141** — likely a QR code / link to the interactive Mathematica 5D mass-fit notebook.

Geometry-heavy pages that would also benefit from visual cross-check: p74, p78, p82-p83, p88, p126-p129, p130-p131.

## Equation Index

The PDF numbers displayed equations sequentially (1)-(152) across the whole document. The table above references these equation numbers. When a mini-lecture cites "eq (22)", it refers to this PDF numbering, not to a renumbered local equation.
