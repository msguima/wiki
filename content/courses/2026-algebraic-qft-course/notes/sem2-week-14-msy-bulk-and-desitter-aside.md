---
title: "Sem II Week 14 — MSY: The Bulk Side; and a de Sitter Aside (CLPW, type II₁)"
type: lecture-notes
course: syllabus
semester: 2
week: 14
block: 5
duration: 4 hours (reading-and-discussion + the dS aside)
prerequisites: Sem II Wks 11–13 (AAJ); Sem I Wk 12 (type classification)
target_paper: "Maldacena, Stanford, Yang, arXiv:1704.05333; aside: CLPW, arXiv:2206.10780"
modified: 2026-08-23
---

# Sem II Week 14 — MSY: The Bulk Side; and a de Sitter Aside (CLPW, type II$_1$)

> *Block 4 (AAJ) computed the generalized-entropy corrections of a traversable wormhole from the **boundary algebra**. This week supplies the **bulk** side: Maldacena–Stanford–Yang's "Diving into traversable wormholes" (arXiv:1704.05333), the gravitational geometry of the same GJW deformation. The point is complementarity — the algebra sees the entropy corrections; the bulk sees the geometry (ANEC violation, the Shapiro time advance, the opening throat); the two are descriptions of one system, and matching them precisely is open. We close with an aside that completes the course's structural picture: Chandrasekaran–Longo–Penington–Witten on de Sitter space, where the **same** crossed-product machine gives **type II$_1$** rather than II$_\infty$ — proving the algebra type is a property of the geometry, not the construction.*

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
- Lin, Maldacena, Rozenberg, Shan, "Holography for people with no time," arXiv:2207.00407 (dS observers and clocks).

## 1. MSY: the bulk picture

### 1.1 The setup

Maldacena–Stanford–Yang work in the **bulk gravitational** description of the GJW-deformed eternal black hole. The deformation $V = g\,\mathcal{O}_L\mathcal{O}_R$ (Sem II Wk 11) couples the two boundaries; in the bulk it sources a quantum stress tensor that backreacts on the geometry.

### 1.2 ANEC violation

**Average null energy across the horizon (MSY). [Stated only — refs: MSY arXiv:1704.05333.]** *The GJW coupling produces a quantum stress tensor whose integral along a null geodesic crossing the horizon is **negative**:*
$$
\int T_{vv}\,dv < 0,
$$
*violating the averaged null energy condition (ANEC) along that geodesic. This is permitted because ANEC is only required to hold under conditions the deformed state does not meet (the coupling is non-local across the two boundaries).*

**Definitions.**
- **Average null energy:** $\int T_{vv}\,dv$ along a null geodesic with affine parameter $v$.
- **ANEC:** the condition $\int T_{vv}\,dv \ge 0$ for all complete null geodesics; holds in many QFT settings but is *violated* by the GJW-deformed state across the horizon.

> **Physical picture.** Classically, the Einstein–Rosen bridge of the eternal BH is non-traversable: any null ray that tries to cross is bent away by the positive energy it must pass, and the throat pinches off before a signal gets through. To open it you need *negative* averaged null energy — a region where matter gravitates "the wrong way," defocusing rather than focusing null rays. The GJW double-trace coupling supplies exactly this: it correlates quantum fluctuations across the two horizons so that the averaged null energy along the crossing geodesic goes negative. This is the bulk meaning of "turning on $g\mathcal{O}_L\mathcal{O}_R$" — it is the only known controlled way to source the negative energy that holds a wormhole open, and it works only briefly and only by a tiny amount.

### 1.3 The Shapiro time advance

**Shapiro time advance (MSY). [Stated only.]** *Gravitational backreaction from the negative-energy GJW stress tensor shifts a crossing null geodesic so it emerges on the far side **earlier** than naive (undeformed) causality would allow — a Shapiro time advance $\Delta v \propto -g$. A signal injected on the left can reach the right boundary.*

**Definitions.**
- **Shapiro time delay/advance:** the change in arrival time of a signal due to its passage through a gravitational field; positive (delay) for ordinary matter, **negative** (advance) for the negative-energy GJW shockwave.
- **Traversable wormhole (operationally):** a geometry through which a signal can pass from one asymptotic region to the other in finite proper time.

### 1.4 Only just traversable

A crucial honest point MSY emphasize: the wormhole is **only just** traversable. The throat opens for a moment, lets a parametrically small signal through, then closes. There is no causality violation in any cosmologically meaningful sense — the advance is bounded, and a signal through the wormhole never beats a signal sent through the ambient spacetime (chronology is protected). It is a controlled, marginal effect, which is exactly why it is theoretically clean.

## 2. Algebra vs. bulk: the complementarity

### 2.1 What each side sees

This is the pedagogical heart of the week. The **same** physical system — the GJW-deformed eternal BH — has two descriptions:

| | AAJ (boundary algebra) | MSY (bulk geometry) |
|---|---|---|
| Computes | $\delta S_{\rm gen}$ corrections (Mini-Calc 4) | the deformed wormhole geometry |
| Sees directly | dressed-entropy change, cocycle structure | ANEC violation, Shapiro advance, open throat |
| Does **not** see directly | the Shapiro shift (geometric) | the dressed entropy (algebraic) |
| Tool | Connes cocycle on type II$_\infty$ | gravitational backreaction, null geodesics |

> **Physical picture.** These are not competing descriptions but **complementary** ones, in the precise sense that each captures cleanly what the other accesses only indirectly. The algebra is the natural home of *entropy and information* — relative entropy, dressed entropy, the cocycle — and it computes $\delta S_{\rm gen}$ effortlessly while saying nothing direct about where the signal comes out. The bulk is the natural home of *geometry and causality* — null energy, Shapiro shifts, the throat — and it gives the traversal geometry while saying nothing direct about the von Neumann entropy. The full duality says these must encode the same physics; but the *dictionary* relating "this algebraic correction" to "that geometric feature" is established only in pieces. Seeing both calculations side by side is the clearest way to feel where the understood part ends.

### 2.2 The conjecture and the gap

**Conjecture (modular shift ↔ Killing-vector shift). [Heuristic — open at the rigorous level.]** *The shift in the modular flow computed by AAJ (the perturbed $\sigma^V_t$, Sem II Wk 11 §3.2) corresponds in the bulk to a shift of the modular Killing vector by the GJW backreaction — and the algebraic boundary term shift equals the geometric Shapiro shift. One should be able to verify this at lowest order.*

**Honest scoping (the course does not close this).**
- The course has **not** derived the Shapiro shift from the algebra side.
- The course has **not** shown the equivalence of AAJ's algebraic corrections and MSY's bulk corrections at the rigorous level.
- These are **open research questions** — excellent final-paper or follow-up-project material, and exactly the frontier the group's program sits near.

## 3. Worked computation: focusing, and why negative energy opens the throat

The previous section quoted ANEC violation and the Shapiro advance from MSY. The link between them — *why* negative averaged null energy opens a wormhole — is not a quotation. It is the Raychaudhuri equation, and it takes half a page. **[Proved, given Einstein's equation and the teleological horizon condition.]**

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

On the unperturbed bifurcate Killing horizon of the eternal black hole, $\theta = \sigma_{ab} = 0$ identically: the horizon is stationary. Turning on the GJW coupling makes $T_{vv} = O(g)$, hence $\theta = O(g)$ and $\sigma = O(g)$, so the quadratic terms are $O(g^2)$ and drop at leading order. The equation linearizes to
$$
\boxed{\;\frac{d\theta}{dv} = -8\pi G\,T_{vv} + O(g^{2}).\;}
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
**The horizon area decreases.** That is the geometric content of the traversal: the horizon recedes, exposing part of what was behind it, and a signal that would have been trapped can now get out. The Shapiro advance of §1.3 is the same statement told in terms of the crossing geodesic rather than the horizon generators.

### 3.3 Where the entropy went

This is the point at which the bulk story meets Week 12, and it is worth pausing on. Hawking's area theorem is not violated, because it assumes the null energy condition, which the GJW state does not satisfy. But something must still be monotone, and that something is the *generalized* entropy:
$$
\delta S_{\rm gen} = \underbrace{\delta\!\Big(\frac{A}{4G}\Big)}_{<\,0\ \text{by §3.2}} + \underbrace{\delta S_{\rm out}}_{>\,0} \;\ge\; 0 .
$$
The area term falls, so the bulk-matter entropy outside must rise to compensate — the generalized second law survives where the classical one fails. Note that these are exactly the two terms of the organizing identity in Week 12 §1.2: the modular-energy/boundary piece is the area response, the relative-entropy piece is the matter response, and their competition is what we computed in closed form in the model of Week 12 §2.3. The bulk and the algebra are keeping the same two books.

> **Physical picture.** The chain is short enough to hold in the head: a non-local coupling between the two boundaries correlates quantum fluctuations across the horizon; those correlations make the averaged null energy negative; negative null energy defocuses nothing and *focuses* the horizon generators under the teleological condition, so the horizon shrinks; a shrinking horizon exposes the throat; and the entropy that the area gave up reappears as matter entanglement outside. Every arrow in that chain is a line of the Raychaudhuri equation except the first, which is the quantum field theory of the deformation. Note also what the argument does *not* need: no detailed knowledge of the deformed metric, no shockwave profile, no transverse Green's function. Those are needed for the *magnitude* of the Shapiro advance — the Dray–'t Hooft computation MSY carry out — but the sign and the mechanism follow from focusing alone.

### 3.4 What remains stated

The magnitude is a genuine bulk computation we do not reproduce. **[Stated only — refs: MSY arXiv:1704.05333 §§2–3; Dray–'t Hooft 1985 for the shockwave metric.]** *The leading averaged null energy is $\int T_{vv}\,dv = -g\,C\,\langle\mathcal{O}_L\mathcal{O}_R\rangle_{\rm TFD} + O(g^2)$ with $C>0$ set by the bulk-to-boundary propagator, and solving the linearized Einstein equation for a thin shock at $v=0$ gives a crossing-geodesic shift $\Delta u = h(x_\perp)$ with $\nabla^2_\perp h = -16\pi G\int T_{vv}\,dv$, hence $\Delta u \propto -g$ at leading order.*

The violation is largest when $\mathcal{O}_L, \mathcal{O}_R$ sit symmetrically across the bifurcation surface and their bulk-to-boundary profiles overlap maximally on the crossing geodesic — the bulk counterpart of the free-field analog's "boost the test functions toward the bifurcation surface" (Sem II Wk 11 §5.2). The same placement that maximizes the symplectic overlap $\varsigma(f_L, f_R)$ maximizes the ANEC violation, which is the sharpest available hint that the two calculations are computing one number in two languages — and the content of the conjecture in §2.2.

## 4. The de Sitter aside: CLPW and type II$_1$

A self-contained ~1-lecture aside that completes the course's structural picture.

### 4.1 Why this aside

The course has followed the crossed-product machine through **one** geometry: the two-sided eternal BH (CPW, type II$_\infty$). CLPW apply the *same* machine to the **de Sitter static patch** and get a *different* type — **II$_1$**, with a finite trace and a maximum-entropy state. The contrast proves the structural punchline:

> **The type of the dressed algebra is not a property of the construction — it is a property of the geometry the construction is applied to.**

### 4.2 The de Sitter static patch

**Definitions.**
- **de Sitter static patch:** for the maximally symmetric solution of the vacuum Einstein equations with $\Lambda > 0$, the causal diamond accessible to a single inertial (comoving) observer, bounded by a **cosmological horizon**.
- **Observer Hamiltonian $H_{\rm obs}$:** the energy along the observer's worldline; unlike the ADM Hamiltonian, it is **bounded below**.

### 4.3 The CLPW construction, and the one-line reason the type changes

**The CLPW dressing (CLPW arXiv:2206.10780). [Stated only for the holographic input; the type computation below is a model proof.]** *At large $N$, the single-trace algebra on the dS static patch is type III$_1$ (as for the BH). Adjoin the **observer's clock** — a crossed product by the observer Hamiltonian $H_{\rm obs}$, which is bounded below. The resulting dressed algebra is type **II$_1$**, not II$_\infty$: it has a **finite** trace, and a normalizable maximum-entropy state.*

The type change is usually quoted. It is in fact a one-line integral, and doing it makes the whole aside land. Recall the crossed-product trace from Sem II Wk 7 §3.2, in which the clock variable $s$ labels the spectrum of the adjoined Hamiltonian:
$$
\hat\tau(a) = \int_{\mathrm{spec}} e^{-2\pi s}\,\big\langle \Psi\otimes\delta_s\,\big|\,a\,\big|\,\Psi\otimes\delta_s\big\rangle\,ds .
$$
Evaluate it on the identity, which is the quantity that decides semifinite-versus-finite. **Everything except the range of integration is the same in the two cases.**

For the eternal black hole, the dressing Hamiltonian is the ADM energy, whose spectrum is all of $\mathbb{R}$:
$$
\hat\tau_{\rm BH}(1) = \int_{-\infty}^{\infty} e^{-2\pi s}\,ds = \infty ,
$$
divergent at $s\to-\infty$. The trace is semifinite but not finite: **type II$_\infty$**.

For the de Sitter static patch, the observer Hamiltonian is bounded below, so the spectrum is a half-line, which we may take to be $[0,\infty)$:
$$
\hat\tau_{\rm dS}(1) = \int_{0}^{\infty} e^{-2\pi s}\,ds = \frac{1}{2\pi} \;<\; \infty .
$$
The trace is finite: **type II$_1$**. $\square$

That is the entire difference. One integral over a line, one over a half-line, and the exponential weight — which is there because the modular flow rescales the trace, and which is the same weight in both cases — converges in one and not the other. Note that the same computation explains why boundedness *below* is what matters rather than boundedness above: the weight $e^{-2\pi s}$ blows up in the direction of decreasing $s$, so it is the lower end of the spectrum that must be cut off.

### 4.4 The maximum-entropy theorem, proved

A finite trace immediately gives something the black-hole case cannot have. Normalize $\hat\tau$ so that $\hat\tau(1) = 1$ — possible precisely because the trace is finite, and note that this *fixes* the trace-rescaling freedom of Sem I Wk 14 §2.3, which in the II$_\infty$ case remains a genuine ambiguity. For a state with density $\hat\rho$, so that $\hat\tau(\hat\rho) = 1$, the dressed entropy is $S_{\mathrm{vN}} = -\hat\tau(\hat\rho\log\hat\rho)$, and
$$
-S_{\mathrm{vN}} = \hat\tau(\hat\rho\log\hat\rho) - \hat\tau(\hat\rho)\log\hat\tau(\hat\rho) \;=\; S(\hat\rho\,\|\,1) \;\ge\; 0,
$$
where the middle expression is zero by $\hat\tau(\hat\rho) = 1$, and the inequality is positivity of relative entropy against the tracial state (equivalently, Jensen's inequality for the convex function $x\log x$ under the tracial state). Hence
$$
\boxed{\;S_{\mathrm{vN}}(\hat\rho) \;\le\; 0\quad\text{for every state, with equality iff } \hat\rho = 1.\;}
$$
The tracial state is the unique maximum-entropy state, and CLPW identify it with the de Sitter vacuum. **[Proved, given the normalized finite trace.]**

The contrast with the black hole is now sharp rather than rhetorical. In II$_\infty$ the operator $\hat\rho = 1$ has $\hat\tau(1) = \infty$ and is therefore not a state at all, so no maximum-entropy state exists and the entropy is unbounded above — which is why black-hole entropy is meaningful only as a difference. In II$_1$ the same operator *is* a state, it is the maximum, and the entropy of every other state is an absolute number measured from it.

> **Physical picture: why II$_1$ here and II$_\infty$ for the BH.** The whole difference is whether the dressing Hamiltonian is bounded below and whether the horizon is compact. For the eternal BH, the ADM Hamiltonian is unbounded and the horizon is non-compact in modular time, so the crossed-product trace runs off to infinity — type II$_\infty$, with the famous divergent $A/4G_N$ entropy regulated only as a difference. For de Sitter, the observer Hamiltonian is bounded below and the cosmological horizon is compact, so the trace converges — type II$_1$, with a finite total entropy and a genuine maximum-entropy state. Same crossed product, same modular flow, different boundedness of the clock. The dS finite entropy is not put in by hand; it falls out of the trace being normalizable, which falls out of the observer's energy being bounded below. This is the cleanest illustration in the whole course that *the algebra type reads off the global causal structure of the geometry* — and the reason a cosmological horizon has an absolute entropy while a black-hole horizon has only entropy differences is, in the end, the range of one integral.

### 4.5 The entropy contrast

| | CPW (eternal BH) | CLPW (de Sitter static patch) |
|---|---|---|
| Dressing Hamiltonian | ADM $H_R$ (unbounded above) | observer $H_{\rm obs}$ (bounded below) |
| Horizon | non-compact (in modular time) | compact (cosmological) |
| Dressed algebra type | II$_\infty$ | **II$_1$** |
| Trace | semifinite (infinite on $1$) | **finite** (normalizable) |
| Dressed entropy | finite only as a difference; $A/4G_N$ divergent piece | **finite individually**; vacuum saturates a maximum |
| Special state | none (no max-entropy state) | dS vacuum = maximum-entropy state |

### 4.6 Where this sits in the type classification

It is worth naming the object. The dS dressed algebra is a holographic realization of the **hyperfinite type II$_1$ factor** of Sem I Wk 12 — the same algebra that appears there as the abstract example of a factor with a finite tracial state, now with the trace carrying physical meaning as the normalized static-patch entropy functional. The II$_\infty$ Rindler/BH dressed algebra of Sem II Wks 6–7 is its semifinite sibling, and the relation between them is the standard one: $\mathrm{II}_\infty \cong \mathrm{II}_1 \bar\otimes \mathcal{B}(\ell^2)$, the extra factor being exactly the non-normalizable direction that the unbounded ADM clock supplies and the dS observer clock does not.

So the course has now exhibited, holographically, three of the four types it classified abstractly in Semester I: III$_1$ (the undressed large-$N$ algebra, Wk 9), II$_\infty$ (the dressed eternal BH, Wks 6–7), and II$_1$ (the dressed dS static patch, here). Type I is what one gets at finite $N$ (Wk 9 §2.3). The abstract classification of Sem I Wk 3 was not a taxonomy for its own sake; every entry in it turned out to be a geometry.

## 5. What to take away

- **MSY bulk picture (magnitude stated only; mechanism proved):** the GJW deformation sources negative averaged null energy across the horizon; backreaction gives a Shapiro time **advance** $\Delta v \propto -g$; the wormhole becomes *just* traversable, with chronology protected.
- **Why negative energy opens the throat (proved, §3):** on a null congruence Einstein's equation gives $R_{\mu\nu}k^\mu k^\nu = 8\pi G\,T_{vv}$ with the $\Lambda$ and $R$ terms dropping, so linearized Raychaudhuri reads $d\theta/dv = -8\pi G\,T_{vv}$. With the teleological condition $\theta(\infty)=0$, negative averaged null energy gives $\theta<0$ and $\delta A<0$: the horizon shrinks. The area the horizon gives up reappears as $\delta S_{\rm out}$ — the same two terms Week 12 computed algebraically.
- **Algebra/bulk complementarity:** AAJ (algebra) sees $\delta S_{\rm gen}$ and the cocycle; MSY (bulk) sees the Shapiro shift and the throat. Same system, complementary descriptions; the precise dictionary between algebraic corrections and geometric features is **open** (honest scoping — the course does not close it).
- **Largest ANEC violation** ↔ largest symplectic overlap of the deformation operators across the bifurcation surface — the bulk counterpart of the free-field "boost toward the horizon."
- **CLPW de Sitter aside (type computed):** the same machine on the dS static patch gives **type II$_1$**, and the reason is one integral — $\hat\tau(1) = \int_{\mathbb{R}}e^{-2\pi s}ds = \infty$ for the BH's unbounded ADM clock, against $\int_0^\infty e^{-2\pi s}ds = 1/2\pi$ for dS's bounded-below observer clock. The maximum-entropy theorem then follows in two lines: normalizing $\hat\tau(1)=1$ gives $-S_{\mathrm{vN}} = S(\hat\rho\|1) \ge 0$, so $S \le 0$ with equality only at the tracial state.
- **Structural punchline:** the dressed-algebra type (II$_1$ vs II$_\infty$) is determined by the **geometry** (boundedness of the clock, compactness of the horizon), not by the construction. The algebra type reads off the global causal structure.

## 6. Looking ahead

Week 15 closes the course: final-write-up presentations, the instructor's outlook on open directions and thesis topics, and the connection back to the group's research program (Bell-CHSH, embezzlement, relative entropy in interacting theories). The course's permanent wiki resource — these notes — is complete after Week 15.

## 7. Problem set

**Core problems.**

**1. ANEC violation sign.** Explain why the GJW deformation can violate ANEC across the horizon without contradiction. (*Hint:* ANEC holds under hypotheses — completeness of the geodesic, a non-deformed state — that the GJW configuration does not satisfy.)

**2. Shapiro advance is linear.** Argue that the leading Shapiro advance is $\Delta v \propto -g$ (linear in the coupling), matching the AAJ first-order cocycle. Where does the negative sign come from?

**3. Ordinary matter, ordinary horizon.** Rerun §3.2 with $T_{vv} \ge 0$ and show that it reproduces Hawking's area theorem, $\delta A \ge 0$. Then identify precisely which hypothesis of that theorem the GJW state violates, and explain why the generalized second law survives anyway (§3.3).

**4. A clock bounded above.** Suppose a hypothetical dressing Hamiltonian had spectrum $(-\infty, 0]$ — bounded *above* rather than below. Evaluate $\hat\tau(1)$ for that case using §4.3 and determine the resulting type. Then explain why the physical clocks of this course (ADM energy, observer energy) are never of this kind, and what it would mean for the entropy if one were.

**Starred problems.**

**5\*. How far below the maximum.** Using the §4.4 result $-S_{\mathrm{vN}}(\hat\rho) = S(\hat\rho\|1)$, compute the entropy deficit of a state whose density is $\hat\rho = 1 + \epsilon\,x$ with $\hat\tau(x) = 0$ and $\|x\|$ small, to second order in $\epsilon$. Identify the quadratic form you obtain as the Kubo–Mori metric of Sem II Wk 12 §2.4 evaluated at the tracial state, and say why it is the *flat* case of that metric.

**6\*. Modular-shift / Killing-shift conjecture.** Set up (do not fully solve) the lowest-order check of the §2.2 conjecture: relate the AAJ perturbed modular flow shift to a shift of the bulk modular Killing vector. Identify precisely what would need to be computed on each side to match them.

**Project problems.**

**7. Algebra/bulk gap.** Write a 2-page critical assessment of what AAJ's algebraic corrections and MSY's bulk geometry each capture, where they are known to agree, and where the matching is open. This is a candidate final-paper section.

**8. CLPW exposition (optional final-topic).** A critical exposition of CLPW (the dS / II$_1$ side) is a valid final-write-up topic. Sketch its structure: the static patch, the observer clock, the II$_1$ dressing, the maximum-entropy theorem, and the contrast with CPW.

---

*Notes prepared for [[courses/2026-algebraic-qft-course/syllabus|the algebraic-QFT course]], Semester II Block 5. Last revised 2026-08-23.*
