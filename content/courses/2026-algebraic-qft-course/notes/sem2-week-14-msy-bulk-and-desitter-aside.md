---
title: "Sem II Week 14 — MSY: The Bulk Side; and a de Sitter Aside (CLPW, type II₁)"
type: lecture-notes
course: syllabus
semester: 2
week: 14
block: 5
duration: "master dossier: 4 hours of material; classroom core: 2-hour seminar + 1-hour office/self-study"
prerequisites: Sem II Wks 11–13 (AAJ); Sem I Wk 12 (type classification)
target_paper: "Maldacena, Stanford, Yang, arXiv:1704.05333; aside: CLPW, arXiv:2206.10780"
modified: 2026-09-29
---

# Sem II Week 14 — MSY: The Bulk Side; and a de Sitter Aside (CLPW, type II$_1$)

> *Block 4 studied AAJ's perturbative formulas for the crossed-product entropy of a deformed traversable-wormhole setup. This week supplies the bulk comparison: Maldacena–Stanford–Yang's gravitational account of the GJW deformation, including negative averaged null energy and a time advance. Matching individual AAJ terms to individual geometric observables remains a separate calculation. We close with CLPW's de Sitter construction. Its type-II$_1$ result follows from adding a bounded-below observer energy and then compressing the continuous core by the positive-energy projection. The resulting finite trace is exact in the model; it does not follow merely from saying that the cosmological horizon is compact.*

> **Route through this master dossier.** **Classroom core (two-hour seminar):** §§1–3 and the defining CLPW corner computation. **Full derivation or self-study:** the linearized Raychaudhuri calculation, the maximum-entropy argument, and the nonstarred problems. **Research extension or office hour:** the unresolved AAJ–MSY matching, the full CLPW source route, and the starred/project problems. The wormhole and de Sitter constructions share operator-algebraic language but are not presented as one theorem.

## 0. Reading

**Primary:**
- Maldacena, Stanford, Yang, "Diving into traversable wormholes," **arXiv:1704.05333**, full paper.
- Refresher: Gao, Jafferis, Wall, arXiv:1608.05687 (bulk side of GJW, read in Wk 11).

**Aside (light):**
- Chandrasekaran, Longo, Penington, Witten (CLPW), "An algebra of observables for de Sitter space," **arXiv:2206.10780** — introduction and the type-II$_1$ structure section. (Skim the technical proofs.)

**Secondary / gentler:**
- Sem II Wks 11–13 (AAJ — the boundary-algebra side of this same wormhole).
- Sem I Wk 12 (type classification; the II$_1$ vs II$_\infty$ distinction the aside turns on).

**Optional research reading:**
- Maldacena, Qi, "Eternal traversable wormholes," arXiv:1804.00491.
- Witten, "A background independent algebra in quantum gravity," arXiv:2308.03663 (the algebra along an observer's worldline, with the Hartle–Hawking state as the maximum-entropy state; de Sitter vacua as the worked case).

## 1. MSY: the bulk picture

### 1.1 The setup

Maldacena–Stanford–Yang work in the **bulk gravitational** description of the GJW-deformed eternal black hole. We fix the GJW Hamiltonian convention used in Week 11,

$$
\delta H(t)=-\int d^{d-1}x\,h(t,x)\,
\mathcal O_R(t,x)\mathcal O_L(-t,x).
$$

For the positive $h$ profile in the controlled scalar example, the computed horizon-averaged null energy is negative. If one abbreviates the same interaction as $+g\mathcal O_L\mathcal O_R$, then $g=-h<0$ after matching the time arguments and smearing. All sign statements below refer to this fixed convention.

### 1.2 Negative averaged null energy on the relevant horizon generator

**Horizon-averaged null energy (MSY). [Stated only — ref: MSY arXiv:1704.05333.]** *For the appropriate coupling sign and switching profile, the GJW deformation produces a negative integral of the null stress tensor on the horizon generator relevant to the signal:*
$$
\int T_{vv}\,dv < 0,
$$
*and the corresponding gravitational backreaction gives the time advance used by the protocol.*

**Definitions.**
- **Average null energy:** $\int T_{vv}\,dv$ along a null geodesic with affine parameter $v$.
- **ANEC:** the condition $\int_{-\infty}^{\infty} T_{vv}\,dv\ge 0$ on a complete null geodesic, under the hypotheses of the relevant theorem. The two-boundary interaction is nonlocal from the viewpoint of either decoupled boundary theory, so one should not cite a standard single-QFT ANEC theorem and then announce a paradox. What MSY need is the sign of the horizon integral in their coupled system; the precise relation between that integral and a theorem formulated on a complete achronal geodesic is setup-dependent.

> **Physical picture.** The eternal bridge is non-traversable because the horizon geometry prevents a causal curve from one boundary from reaching the other. With the suitable sign and time profile, the GJW coupling produces negative averaged null energy on the relevant horizon generator. The resulting gravitational backreaction shifts the causal relation enough to let a controlled signal through. This is a specific quantum protocol, not a claim that any bilocal coupling or any negative local energy density produces a traversable wormhole.

### 1.3 The Shapiro time advance

**Shapiro time advance (MSY). [Stated only.]** *For the positive-$h$ GJW convention fixed in §1.1, gravitational backreaction from the negative-energy stress tensor shifts the relevant crossing null geodesic in the advance direction, so a signal injected on one side can reach the other during a controlled window.* The shift is linear in the coupling at leading order, but its signed symbol depends on the orientation chosen for the Kruskal coordinate; we therefore do not write a convention-free formula such as $\Delta v\propto-g$.

**Definitions.**
- **Shapiro time delay/advance:** the change in arrival time of a signal due to its passage through a gravitational field; positive (delay) for ordinary matter, **negative** (advance) for the negative-energy GJW shockwave.
- **Traversable wormhole (operationally):** a geometry through which a signal can pass from one asymptotic region to the other in finite proper time.

### 1.4 Only just traversable

In the perturbative regime emphasized here, the traversable window and the amount of information that can be sent are limited. GJW and MSY analyze compatibility with the causal structure of the directly coupled boundary system; our Raychaudhuri calculation below does not prove a separate chronology-protection theorem. The detailed bounds depend on the geometry, coupling profile, and backreaction of the signal. “Only just traversable” is therefore a regime statement, not a universal definition of traversable wormholes.

## 2. Algebra vs. bulk: the complementarity

### 2.1 What each side sees

This is the pedagogical heart of the week. The **same** physical system — the GJW-deformed eternal BH — has two descriptions:

| | AAJ (boundary algebra) | MSY (bulk geometry) |
|---|---|---|
| Computes | perturbative type-II entropy structures | bulk response and signal propagation |
| Sees directly | changed trace weight, Jacobian, BCH commutators | negative null energy, time advance, traversable window |
| Does **not** see directly | the Shapiro shift (geometric) | the dressed entropy (algebraic) |
| Tool | unitary modular covariance and crossed-product trace | gravitational backreaction and null geodesics |

> **Physical picture.** These are complementary descriptions in the ordinary holographic sense: the algebraic calculation organizes entropy and modular data, while the bulk calculation organizes geometry and causal propagation. Neither result is effortless, and neither individual term comes with an automatic translation into the other language. A valid matching must use the same state, coupling profile, normalization, order in $h$, and order in $1/N$.

### 2.2 The conjecture and the gap

**Course-generated matching question. [Heuristic.]** *Can a specified change in the AAJ modular charge or entropy weight be related, in one common perturbative scheme, to the bulk stress tensor, shifted QES, or null-geodesic time advance?* Entropy and a time shift have different dimensions and operational meanings, so no direct equality is assumed.

**Honest scoping (the course does not close this).**
- The course has **not** derived the Shapiro shift from the algebra side.
- The course has **not** shown the equivalence of AAJ's algebraic corrections and MSY's bulk corrections at the rigorous level.
- These are **open research questions** — excellent final-paper or follow-up-project material, and exactly the frontier the group's program sits near.

## 3. Worked computation: the linearized horizon-area response

The previous section quoted the negative horizon integral and the Shapiro advance from the sources. Raychaudhuri gives a precise intermediate result: the linearized response of the chosen horizon congruence and its area. **[Proved below, given Einstein's equation, perturbative control, and the teleological horizon condition.]** It does not by itself prove that a causal curve connects the two asymptotic boundaries; that global statement also needs the metric solution, boundary conditions, and geodesic shift computed by GJW/MSY.

### 3.1 Null focusing

Consider the congruence of null generators of the horizon, with affine parameter $v$, tangent $k^\mu = (\partial_v)^\mu$, expansion $\theta$, shear $\sigma_{ab}$ and twist $\omega_{ab}$. The Raychaudhuri equation for a null congruence in $D$ spacetime dimensions reads
$$
\frac{d\theta}{dv} = -\frac{\theta^{2}}{D-2} - \sigma_{ab}\sigma^{ab} + \omega_{ab}\omega^{ab} - R_{\mu\nu}k^{\mu}k^{\nu}.
$$
Horizon generators are hypersurface-orthogonal, so $\omega_{ab} = 0$. And the Ricci term simplifies dramatically on a null vector: contracting Einstein's equation $R_{\mu\nu} - \tfrac12 R\,g_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\,T_{\mu\nu}$ with $k^\mu k^\nu$, both the $g_{\mu\nu}$ terms drop because $g_{\mu\nu}k^\mu k^\nu = 0$, leaving
$$
R_{\mu\nu}k^{\mu}k^{\nu} = 8\pi G\,T_{vv}.
$$
Note that neither the cosmological constant nor the Ricci scalar appears — null focusing is sensitive only to the null energy, which is why ANEC is the relevant condition and not, say, the weak energy condition.

On the unperturbed bifurcate Killing horizon of the eternal black hole, $\theta = \sigma_{ab} = 0$ identically: the horizon is stationary. In the positive-$h$ convention fixed in §1.1, turning on the GJW coupling makes $T_{vv}=O(h)$, hence $\theta=O(h)$ and $\sigma=O(h)$, so the quadratic terms are $O(h^2)$ and drop at leading order. The equation linearizes to
$$
\boxed{\;\frac{d\theta}{dv} = -8\pi G\,T_{vv} + O(h^{2}).\;}
$$

### 3.2 The boundary condition fixes the sign

Integrating requires a boundary condition, and the right one is *teleological*: an event horizon is defined by the far future, and a horizon that settles down must have $\theta \to 0$ as $v\to\infty$. Integrating the boxed equation backward from there,
$$
\theta(v) = \theta(\infty) + 8\pi G\!\int_v^{\infty}\! T_{vv}\,dv' = 8\pi G\!\int_v^{\infty}\! T_{vv}\,dv'.
$$
So the sign of the expansion is the sign of the *remaining* averaged null energy. With ordinary matter, $\int T_{vv}\,dv' \ge 0$ gives $\theta \ge 0$ — generators diverge toward the future, the area grows, and this is Hawking's area theorem. With the GJW deformation, $\int T_{vv}\,dv' < 0$ gives
$$
\theta(v) < 0 ,
$$
the generators *converge*, and since the transverse area along the generators obeys $\theta = \tfrac{d}{dv}\log A$,
$$
\frac{\delta A}{A} = \int \theta\,dv \;<\; 0 .
$$
**The chosen horizon area decreases at linear order.** This is the focusing/defocusing response that makes traversability plausible, but it is not yet the global two-boundary result. To show that a signal actually escapes, one must solve for the perturbed metric and follow the relevant null geodesic with the correct asymptotic boundary conditions. The Shapiro advance of §1.3 is that additional source-level result, not an algebraic restatement of the area integral.

### 3.3 What Raychaudhuri does not prove about entropy

The calculation above determines the leading change of the chosen horizon generators under the stated boundary condition. It does not by itself determine $\delta S_{\rm out}$, prove that $\delta S_{\rm out}>0$, or establish a generalized second law for arbitrary cuts. A GSL statement requires a precisely defined future causal horizon, a choice of outside algebra/state, renormalization of $S_{\rm out}$, and the hypotheses of the relevant theorem.

When those hypotheses apply, the generalized entropy is

$$
S_{\rm gen}=\frac{A}{4G}+S_{\rm out},
$$

and its monotonicity constrains the sum rather than either term separately. In the present notes, the area decrease is the Raychaudhuri result; the matter-entropy response must be calculated. Week 12's finite-matrix identity illustrates how entropy and modular energy can compensate, but it is not a proof of the gravitational GSL for the GJW spacetime.

> **Physical picture.** The safe causal chain is: the chosen boundary coupling changes the bulk stress tensor; negative averaged null energy changes the horizon expansion; the shifted geometry can admit a crossing signal. The entropy chain is parallel but requires additional input. Keeping those chains separate prevents the Raychaudhuri equation from being asked to prove a quantum-information statement it does not contain.

### 3.4 What remains stated

The magnitude is a genuine bulk computation we do not reproduce. **[Stated only — refs: MSY arXiv:1704.05333 and GJW arXiv:1608.05687.]** The stress tensor is obtained from bulk propagators with the specified boundary coupling, and the metric/geodesic shift follows from the linearized gravitational equation in that geometry. Coefficients, signs, and transverse operators depend on conventions and dimension; students should extract the actual formula from the assigned section rather than use a universal schematic Poisson equation.

There is no free-field cross-wedge symplectic counterpart to maximize: locality gives $\sigma(f_L,f_R)=0$, and a Lorentz boost does not move the Rindler radius toward the horizon. Comparing a Gaussian Weyl commutator with the MSY time advance would require a new observable-level dictionary.

## 4. The de Sitter aside: CLPW and type II$_1$

### 4.1 The actual starting point

CLPW work in the limit $G_N\to0$ with quantum fields in a de Sitter static patch. The field algebra $\mathcal A$ is type III$_1$. Because de Sitter has no asymptotic boundary to which one can dress a local operator, CLPW add an observer and dress observables to the observer's worldline.

Their minimal observer has

$$
H_{\rm obs}=q,
\qquad
q\geq0,
\qquad
\mathcal H_{\rm obs}=L^2(\mathbb R_+).
$$

The nonnegative-energy assumption is the decisive algebraic input. It is not a finite-dimensional observer and does not assert that the de Sitter Hilbert space is finite dimensional.

### 4.2 Continuous core first, positive-energy compression second

CLPW first ignore $q\geq0$. Imposing the combined time-translation constraint then produces the usual modular crossed product $\mathcal A_{\rm cr}$, a type-II$_\infty$ continuous core. In a convenient representation set

$$
x=-q.
$$

The canonical trace is

$$
\operatorname{Tr}_{\rm cr}\widehat a
=\int_{-\infty}^{\infty}
\beta_{\rm dS}\,dx\,e^{\beta_{\rm dS}x}
\langle\Psi_{\rm dS}|a(x)|\Psi_{\rm dS}\rangle.
$$

Now restore positive observer energy. Before the conjugation that put the core in the displayed $H+x$ form, the projection is $\Theta(q)$. In the standard core representation it is the operator

$$
\boxed{\Pi=\Theta(-H-x),}
$$

because the observer constraint becomes $H+x\leq0$. The physical algebra is the corner

$$
\widehat{\mathcal A}
=\Pi\mathcal A_{\rm cr}\Pi.
$$

The projection is not generally the scalar half-line indicator $\Theta(-x)$, because $H$ acts on the field Hilbert space. The trace of the identity can nevertheless be evaluated in the de Sitter reference vector, for which $H|\Psi_{\rm dS}\rangle=0$. Only in this matrix element does $\Pi$ reduce to $\Theta(-x)$, and CLPW obtain

$$
\boxed{
\operatorname{Tr}_{\widehat{\mathcal A}}1
=\operatorname{Tr}_{\mathcal A_{\rm cr}}\Pi
=\int_{-\infty}^{0}
\beta_{\rm dS}\,dx\,e^{\beta_{\rm dS}x}
=1.
}
$$

Thus $\Pi$ is a finite projection in the type-II$_\infty$ core, and the corner is type II$_1$. This is the source's calculation. Saying only “the horizon is compact” misses the operator that makes the trace finite.

### 4.3 Why the black-hole core stays II$_\infty$

CLPW's black-hole comparison uses subtracted ADM energies

$$
h_{L,R}=H_{L,R}-M_0.
$$

The physical $H_{L,R}$ need not be unbounded below. Rather, after subtracting the background mass $M_0\sim1/G_N$ and taking the semiclassical limit, $h_{L,R}$ can range over all real values. There is no analog of the finite positive-energy projection $\Pi$ that cuts the core to a finite corner. The right-exterior algebra therefore remains type II$_\infty$.

The correct contrast is:

| Black-hole exterior | de Sitter static patch |
|---|---|
| continuous core with subtracted ADM fluctuation taking real values | same continuous-core stage |
| no finite compression imposed | positive observer energy gives $\Pi=\Theta(-H-x)$ |
| $\operatorname{Tr}1=\infty$ | $\operatorname{Tr}\Pi=1$ |
| type II$_\infty$ | type II$_1$ corner |

This is an algebraic mechanism tied to the observer/constraint model. Compactness of the cosmological horizon is part of the physical setting, but it is not the proof of the type.

### 4.4 Maximum entropy

Normalize the finite trace as CLPW do, so $\operatorname{Tr}1=1$. For a density $\rho\geq0$ with $\operatorname{Tr}\rho=1$,

$$
D(\rho\Vert1)
=\operatorname{Tr}(\rho\log\rho)
=-S(\rho)\geq0.
$$

Therefore

$$
\boxed{S(\rho)\leq0,}
$$

with equality only for $\rho=1$ when the relative-entropy equality condition applies. The tracial state is the unique maximum-entropy state.

CLPW identify its purification as

$$
\Psi_{\max}
=\Psi_{\rm dS}\sqrt{\beta_{\rm dS}}
e^{\beta_{\rm dS}x/2},
\qquad x\leq0,
$$

so the observer energy has the normalized distribution

$$
p(q)=\beta_{\rm dS}e^{-\beta_{\rm dS}q},
\qquad q\geq0.
$$

For semiclassical states, CLPW relate the type-II entropy to $A/(4G_N)+S_{\rm out}$ up to a state-independent additive constant. The normalized algebraic maximum is $0$; the large positive Gibbons–Hawking entropy is recovered after restoring that conventional constant. Thus “finite trace” does not mean “no renormalization ambiguity.”

### 4.5 Scope ledger

- **Exact in the CLPW model:** positive-energy projection, finite trace, type-II$_1$ corner, maximum tracial state.
- **Semiclassical relation:** entropy agrees with generalized entropy up to a state-independent constant.
- **Not claimed:** a finite-dimensional static-patch Hilbert space, a proof from compact-horizon geometry alone, or a universal rule that causal structure uniquely determines von Neumann-algebra type.

The last point matters. The algebra is sensitive to the observer, constraints, limiting procedure, and allowed spectrum. It can reflect global geometry without being a one-to-one classifier of geometries.

## 5. What to take away

- **MSY bulk picture (source result):** in the fixed GJW convention $\delta H=-\int h\mathcal O_R\mathcal O_L$ with the controlled positive-$h$ profile, the deformation sources negative horizon-averaged null energy; the computed backreaction gives a Shapiro time advance and a limited traversable window. No convention-independent sign formula for an undefined $g$ is used.
- **What §3 proves:** on a null congruence Einstein's equation gives $R_{\mu\nu}k^\mu k^\nu=8\pi G T_{vv}$, so linearized Raychaudhuri reads $d\theta/dv=-8\pi G T_{vv}$. With the stated teleological condition, negative averaged null energy yields a decreasing horizon area. The global crossing geodesic, matter-entropy response, and any GSL or chronology claim require additional input.
- **Algebra/bulk comparison:** AAJ organize the perturbed type-II entropy; MSY organize bulk stress energy and causal propagation. A term-by-term dictionary is not supplied by either calculation alone.
- **No cross-wedge symplectic match:** $\sigma(f_L,f_R)=0$ by locality, and a common boost does not localize test functions at the horizon.
- **CLPW type computation:** start with the type-II$_\infty$ continuous core and impose positive observer energy with $\Pi=\Theta(-H-x)$. On the de Sitter reference vector $H\Psi_{\rm dS}=0$, the trace check reduces to
  $$
  \operatorname{Tr}\Pi
  =\int_{-\infty}^{0}\beta_{\rm dS}e^{\beta_{\rm dS}x}dx=1.
  $$
  The finite corner is type II$_1$.
- **Maximum entropy:** with $\operatorname{Tr}1=1$, $-S(\rho)=D(\rho\Vert1)\geq0$; the tracial state is the unique maximum. Generalized entropy agrees up to a state-independent constant in the semiclassical regime.

## 6. Looking ahead

Week 15 closes the course: final-write-up presentations, the instructor's outlook on open directions and thesis topics, and the connection back to the group's research program (Bell-CHSH, embezzlement, relative entropy in interacting theories). The course's permanent wiki resource — these notes — is complete after Week 15.

## 7. Problem set

**Core problems.**

**1. Averaged null energy and hypotheses.** Identify the precise horizon integral used in GJW/MSY and compare it with a standard ANEC theorem's hypotheses. Do not say merely “the state is deformed”; state which completeness, boundary-condition, locality, or achronality assumptions differ.

**2. Linear response on both sides.** Explain why the leading bulk response and several AAJ entropy structures are linear in the deformation. Why does equal perturbative order not make an entropy coefficient equal to a time advance?

**3. Ordinary matter, ordinary horizon.** Rerun §3.2 with $T_{vv}\geq0$ and obtain the sign of the area response under the stated boundary condition. Then list the extra definitions and theorem hypotheses needed before asserting a generalized second law.

**4. Reverse the reference-sector half-line.** Start from the general CLPW projection $\Pi=\Theta(-H-x)$ and show why its trace in the de Sitter reference vector reduces to an integral over $x\leq0$. As a deliberately unphysical comparison, reverse only that reference-sector half-line to $x\geq0$, evaluate $\int\beta e^{\beta x}dx$, and explain why it diverges. State why this toy reversal is neither the general operator constraint nor a claim about the physical ADM Hamiltonian.

**Starred problems.**

**5\*. How far below the maximum.** Using $-S(\rho)=D(\rho\Vert1)$, expand $\rho=1+\epsilon x$ with $\operatorname{Tr}x=0$ and $\|x\|$ small. Show that the leading entropy deficit is $\epsilon^2\operatorname{Tr}(x^2)/2$.

**6\*. Algebra/bulk matching protocol.** Choose one term in AAJ Eq. (77) and one bulk observable in MSY. List the state, coupling profile, normalization, and correlators required to compare them. Explain why matching perturbative order alone is insufficient.

**Project problems.**

**7. Algebra/bulk gap.** Write a 2-page critical assessment of what AAJ's algebraic corrections and MSY's bulk geometry each capture, where they are known to agree, and where the matching is open. This is a candidate final-paper section.

**8. CLPW exposition (optional final-topic).** A critical exposition of CLPW (the dS / II$_1$ side) is a valid final-write-up topic. Sketch its structure: the static patch, the observer clock, the II$_1$ dressing, the maximum-entropy theorem, and the contrast with CPW.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 5. Last revised 2026-09-29.*
