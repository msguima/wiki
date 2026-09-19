---
title: "Week 3 — The Villain Form and the Exact Duality of the XY Model"
type: lecture-notes
course: syllabus
semester: 1
week: 3
block: A
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 1–2 (compact fields, cochain calculus, Hodge decomposition, Poisson resummation); Gaussian integrals with sources
modified: 2026-07-07
---

# Week 3 — The Villain Form and the Exact Duality of the XY Model

> *Last week promised that "the vortices are a Coulomb gas." This week we prove it — exactly, with the sums performed on the page. The route runs through four exact rewritings: the Villain model becomes a conserved-current model, the current model becomes a height model, the height model splits into spin waves plus integer charges, and the charges interact by the two-dimensional Coulomb law with a fugacity fixed by the lattice Green function constant of Week 1. No step is approximate. At the end the same object wears a fourth costume — sine-Gordon — and hands Week 4 the one number it needs: the scaling dimension $\pi\beta$ of the vortex operator.*

## 0. Reading

**Primary:** José, Kadanoff, Kirkpatrick, Nelson, *Phys. Rev. B* 16 (1977) 1217 (JKKN), §§I–III — this week reproduces and modernizes their derivation. Villain, *J. Physique* 36 (1975) 581, for the original substitution.

**Secondary:**
- Kogut, *Rev. Mod. Phys.* 51 (1979) 659, §VI — the duality in review form.
- Tong, *Statistical Field Theory*, §5.3 — Coulomb gas and sine-Gordon in continuum notation.

**Optional research reading:** Fröhlich & Spencer, *Comm. Math. Phys.* 81 (1981) 527 — the rigorous proof that the BKT transition exists, built exactly on this week's Coulomb-gas representation.

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]]. Cochain machinery: [[week-02-lattice-cell-complex-cochains|Week 2]] and the [[cochain-calculus-survival-kit|survival kit]]; conventions: [[courses/generalized-symmetries-course/conventions]].

## 1. The Villain substitution

### 1.1 The action

The cosine weight $e^{\beta\cos\phi}$ is $2\pi$-periodic but algebraically opaque: its character coefficients are Bessel functions (Week 1 §5). Villain's move: keep the periodicity, make each branch Gaussian,
$$
e^{\beta\cos\phi}\ \longrightarrow\ V_\beta(\phi) = \sum_{n\in\mathbb{Z}} e^{-\frac{\beta}{2}(\phi - 2\pi n)^2}.
$$
On the lattice, $\phi \to (d\theta)_\ell = \theta_y - \theta_x$ per link, each link carrying its own integer $n_\ell$. The **Villain XY partition function** is
$$
\boxed{\ Z = \left(\prod_x \int_{-\pi}^{\pi}\frac{d\theta_x}{2\pi}\right)\sum_{n\,\in\, C^1(\Lambda,\mathbb{Z})} \exp\!\Big(-\frac{\beta}{2}\big\|d\theta - 2\pi n\big\|^2\Big),\ }
$$
with $\|f\|^2 = \sum_\ell f_\ell^2$. The integer 1-cochain $n$ is precisely the "pair of ($\mathbb{R}$-cochain, $\mathbb{Z}$-cochain)" that Week 2's fine print F6 said a compact field really is: $n_\ell$ records which branch of the angle difference each link sits on.

We take the Villain model as the *definition* of the theory this week. Its relation to the cosine model — same universality class, different vortex core energy — is quantified in §9 (F2) and Week 1 Problem 5.

### 1.2 The branch redundancy and the vorticity [Computed.]

The pair $(\theta, n)$ overcounts configurations: shifting
$$
\theta_x \to \theta_x + 2\pi k_x,\qquad n \to n + dk,\qquad k \in C^0(\Lambda,\mathbb{Z})
$$
changes $d\theta - 2\pi n$ by $2\pi\,dk - 2\pi\,dk = 0$. (Equivalently: extending each $\theta_x$ integral from $(-\pi,\pi]$ to $\mathbb{R}$ while dropping one integer sum is the same partition function.) The branch-independent content of $n$ is its coboundary,
$$
v \;=\; dn \ \in\ C^2(\Lambda,\mathbb{Z}),
$$
one integer per plaquette, invariant under $n \to n + dk$ since $d^2 = 0$. This is the **vorticity**: applying $d$ to the Villain field strength,
$$
d\,(d\theta - 2\pi n) = -2\pi\, dn = -2\pi v,
$$
so a plaquette with $v_P \ne 0$ carries winding $\oint d\theta = 2\pi v_P$ — Week 1 §4.1's explicit vortex, now one line of cochain algebra. Section 6 confirms that these integers are the physical vortices by an independent route.

> **Physical picture.** The split "$n = $ branch junk $+$ vorticity" is the split "spin waves $+$ vortices." The part $dk$ is unwound by letting θ roam $\mathbb{R}$; the part with $dn \ne 0$ *cannot* be unwound — it is the topological obstruction, and it is all that survives of $n$ in any physical answer. Week 1's move "let $\theta\in\mathbb{R}$ to get the Gaussian model" is precisely: keep the junk, discard $v$. This week keeps both.

### 1.3 A vortex pair, walked through the variables [Computed.]

Concreteness before machinery. Take the vortex–antivortex pair of Week 1 §4.3: the phase field $\theta(x)$ winds $+2\pi$ around core plaquette $\tilde x_1$ and $-2\pi$ around $\tilde x_2$. Where do the integers sit? The multivalued angle has a **branch cut**: a curve joining the two cores across which θ jumps by $2\pi$. On the lattice, choose the cut as a path $\tilde\gamma$ on the *dual* lattice from $\tilde x_1$ to $\tilde x_2$. On every link crossed by $\tilde\gamma$, the branch-reduced difference $(d\theta)_\ell$ overshoots the fundamental domain, and minimizing the Villain action assigns exactly
$$
n_\ell = \begin{cases} \pm 1 & \ell \text{ crossed by } \tilde\gamma \\ 0 & \text{otherwise}\end{cases}
\qquad\text{i.e.}\qquad n = \star\,\mathbb{1}_{\tilde\gamma},
$$
the indicator cochain of a **string**. Its coboundary is supported where the string ends: $dn$ at a plaquette $P$ equals the net number of endpoints of $\tilde\gamma$ at the dual site $\tilde P$ (transport with §5.2 of Week 2: $d$ on Λ ↔ boundary on $\Lambda^*$), so
$$
v = dn = +\mathbb{1}_{\tilde x_2} - \mathbb{1}_{\tilde x_1}:
$$
the charges live at the string's ends and nowhere else.

```
     ·    ·    ·    ·    ·    ·
                                        ⊖ , ⊕ : core plaquettes (v = ∓1)
     ·   ⊖━━━━━━━━━━━⊕    ·             ━━━ : dual path  γ̃ (the branch cut)
              │  │  │                    | : links with n = 1
     ·    ·    ·    ·    ·    ·              (those crossed by the cut)
```
**Figure 0. The Villain integer as a Dirac string: $n$ is the indicator of an unobservable cut; $v = dn$ marks its observable endpoints.**

Moving the cut, $\tilde\gamma \to \tilde\gamma'$ with the same endpoints, changes $n$ by exactly a gauge shift $dk$ (the indicator of the enclosed region) — §1.2's redundancy, now with a picture. **The string is unobservable; the endpoints are not.** File this configuration away: it is, point for point, the Dirac string of a magnetic monopole pair ([[week-08-dual-variables-abelian-gauge|Week 8]], Week 12's Witten effect), and the seam of the Kadanoff–Ceva disorder operator ([[week-04-bkt-kramers-wannier-disorder|Week 4]]). One geometry, three theories.

## 2. First rewriting: the conserved-current model [Computed.]

We now execute the Week-2 recipe with every constant. Three moves.

**Move 1 — Hubbard–Stratonovich, link by link.** For each link, with $u_\ell = (d\theta - 2\pi n)_\ell$,
$$
e^{-\frac{\beta}{2}u_\ell^2} \;=\; \frac{1}{\sqrt{2\pi\beta}}\int_{-\infty}^{\infty} db_\ell\; e^{-\frac{1}{2\beta}b_\ell^2\; +\; i\, b_\ell u_\ell}
$$
(a Gaussian integral, verified by completing the square). The coupling has already inverted, $\beta \to 1/\beta$ — the fingerprint of duality. Doing all links:
$$
Z = (2\pi\beta)^{-N_\ell/2}\left(\prod_x\int\frac{d\theta_x}{2\pi}\right)\left(\prod_\ell\int db_\ell\right)\sum_{n}\;
e^{-\frac{1}{2\beta}\|b\|^2\; +\; i\,b\cdot(d\theta - 2\pi n)},
$$
with $N_\ell$ the number of links and $b\cdot f = \sum_\ell b_\ell f_\ell$.

**Move 2 — sum the integers: the comb.** The $n$-dependence is $\prod_\ell \sum_{n_\ell} e^{-2\pi i\, b_\ell n_\ell}$. By the Dirac-comb identity (Week 2 §7.1),
$$
\sum_{n_\ell\in\mathbb{Z}} e^{-2\pi i\, b_\ell n_\ell} = \sum_{m_\ell\in\mathbb{Z}}\delta(b_\ell - m_\ell):
$$
the auxiliary field is **pinned to integer values**, $b = m \in C^1(\Lambda,\mathbb{Z})$. The $b$ integrals collapse:
$$
Z = (2\pi\beta)^{-N_\ell/2}\left(\prod_x\int_{-\pi}^{\pi}\frac{d\theta_x}{2\pi}\right)\sum_{m\,\in\, C^1(\Lambda,\mathbb{Z})} e^{-\frac{1}{2\beta}\|m\|^2\; +\; i\, m\cdot d\theta}.
$$

**Move 3 — integrate the compact phase: a Kronecker delta.** Summation by parts (Week 2 §3.3, the definition of the adjoint):
$$
m\cdot d\theta = (\delta m)\cdot\theta = \sum_x (\delta m)_x\,\theta_x .
$$
Because $m$ is integer-valued, so is $(\delta m)_x$, and the *compact* integral gives a Kronecker — not Dirac — delta:
$$
\int_{-\pi}^{\pi}\frac{d\theta_x}{2\pi}\; e^{i(\delta m)_x\theta_x} = \delta_{(\delta m)_x,\,0}.
$$
This is worth pausing on: **compactness of θ is exactly what makes the dual current conserved with integer precision.** A noncompact θ would force $\delta m = 0$ as a real constraint on a real field; the compact θ forces it on an integer field — the difference between a gauge fixing and a conservation law. The result of the three moves:
$$
\boxed{\ Z = (2\pi\beta)^{-N_\ell/2}\sum_{\substack{m\,\in\, C^1(\Lambda,\mathbb{Z}) \\ \delta m\, =\, 0}} e^{-\frac{1}{2\beta}\|m\|^2}.\ }
$$
The XY model is exactly a statistical mechanics of **conserved integer currents** on links: divergence-free loops of integer flux, weighted by their squared length over $2\beta$. High-temperature physics (small β) suppresses currents entirely; low temperature lets them proliferate. (This is also precisely the form in which the model's global $U(1)$ charge sectors are manifest — each closed current loop is a worldline of charge.)

```
      ┌───→───┐   ┌→┐
      │       │   │ │            A typical current configuration:
      ↑       ↓   └←┘            closed integer flux loops (δm = 0),
      │       │                  weight exp(−Σ m²/2β).
      └───←───┘
```
**Figure 1. The conserved-current representation: the XY model as a gas of oriented integer loops.**

> **Physical picture.** The loops are worldlines of the $U(1)$ charge: the current representation is what a particle physicist would call the *world-line expansion* of the theory, with $m_\ell$ counting net charge flow through each link. High temperature (small β) suppresses all flow — an insulator of charge; low temperature lets long loops proliferate — the QLRO phase is a loop condensate. This representation is also, verbatim, what Monte Carlo "worm algorithms" simulate, and its gauge-theory sibling — electric flux lines as the dual variable — is the strong-coupling picture of [[week-06-wilson-action-strong-coupling|Week 6]] and the string-net condensate of Semester II. One exact rewriting, four decades of reuse.

## 3. Second rewriting: heights and windings [Computed.]

Solving $\delta m = 0$ is Week 2's Hodge theory, over the integers, on the torus.

**Claim.** Every divergence-free $m \in C^1(\Lambda,\mathbb{Z})$ on the $L\times L$ torus can be written **uniquely** as
$$
m \;=\; \star\, d\tilde h \;+\; w_1\, M^{(1)} + w_2\, M^{(2)},
\qquad \tilde h \in C^0(\Lambda^*,\mathbb{Z})\ \text{(mod global shift)},\quad w_{1,2}\in\mathbb{Z},
$$
where $\tilde h$ is an integer **height field on dual sites** and $M^{(1,2)}$ are two *fixed reference currents of unit winding* — e.g. $M^{(1)} = $ a single closed loop of current along one chosen row of $x$-links. (Note what the $M^{(i)}$ are **not**: they are not the harmonic cochains $h^{(i)}$ of Week 2 §6, which have value 1 on *every* parallel link and hence carry winding $L$, not 1. Over the integers there is no harmonic representative of unit winding — the real harmonic one would be $h^{(i)}/L$, which is not integer-valued. This distinction matters below.)

**Construction (this is the proof).** Transport $m$ to the dual lattice: $\star m$ is a *closed* integer 1-cochain on $\Lambda^*$ (§5.2 of Week 2: divergence becomes curl). Measure its two winding numbers $w_i = $ (sum of $\star m$ along the $i$-th dual cycle) and subtract $w_1 M^{(1)} + w_2 M^{(2)}$, whose windings are $(1,0)$ and $(0,1)$ by construction: the remainder $r$ is closed with zero winding. Now define $\tilde h(\tilde x) = \sum_{\gamma:\, \tilde x_0 \to \tilde x} \star r$ along any dual path γ: **path-independence** holds because two paths differ by a closed dual loop, on which a closed zero-winding cochain sums to zero. So $r = \star d\tilde h$ with $\tilde h$ integer-valued, unique up to the constant $\tilde h(\tilde x_0)$. $\square$

Equivalently and more usefully: $m = \star d\tilde h$ with a **multivalued** height, $\tilde h$ shifting by $w_i$ around the $i$-th cycle — "tilted" or twisted boundary conditions, the lattice version of a screw dislocation. The partition function splits **exactly as a sum over tilt sectors**,
$$
Z = (2\pi\beta)^{-N_\ell/2}\ \sum_{w_1, w_2\,\in\,\mathbb{Z}}\ Z^{(w)}_{\rm SOS},
\qquad
Z^{(w)}_{\rm SOS} = \sum_{\tilde h\ \text{twisted by } w} e^{-\frac{1}{2\beta}\|d\tilde h\|^2},
$$
with **no claim that the sectors factor off**: the reference current $M^{(i)}$ is not harmonic, so $\|m\|^2 = \|\star d\tilde h + wM\|^2$ contains genuine cross terms, and the $w$-dependence of $Z^{(w)}_{\rm SOS}$ is dynamical. What *can* be computed is its Gaussian (spin-wave) value: after the second Poisson resummation of §4, the twisted sector's real field relaxes to the uniform tilt $d\tilde\varphi = w_i/L$ per link, with action $\frac{1}{2\beta}\cdot L^2\cdot\big(\tfrac{w_i}{L}\big)^2 = \frac{w_i^2}{2\beta}$ per direction, so
$$
\frac{Z^{(w)}}{Z^{(0)}} = e^{-\frac{1}{2\beta}(w_1^2 + w_2^2)}\times\big(1 + \text{vortex corrections}\big)
$$
[Computed at the Gaussian level] — a Jacobi theta function of the *tilts*, temperature-dependent but $L$-independent at fixed β, encoding exactly the twisted-boundary-condition (helicity) physics of Week 1 Problem 6. From here on we work in the $w = 0$ sector: the tilt adds a linear background to the dual field and modifies only these sector weights; the vortex physics developed below is sector-independent (fine print F3).

$Z^{(0)}_{\rm SOS}$ is the **discrete Gaussian (solid-on-solid) model**: a crystal-surface height function with stiffness $1/2\beta$. The XY model at temperature $T$ *is* a fluctuating interface at inverse temperature $\propto T$; the XY transition, seen from this face, is the interface's **roughening transition** — a correspondence we meet again for the confining string in [[week-06-wilson-action-strong-coupling|Week 6]].

> **Physical picture.** Which surface phase is which: large β makes height steps *cheap* ($e^{-(\Delta\tilde h)^2/2\beta} \to 1$), so the **low-temperature QLRO phase of XY is the rough phase of the surface** — logarithmically wandering, massless heights, the critical Gaussian physics wearing crystal-growth clothes. Small β freezes the surface flat (a unit step carries weight $e^{-1/2\beta} \to 0$ as $\beta \to 0$): the **smooth phase is XY's disordered phase**. Roughening transitions of real crystal facets and BKT transitions of films are the same fixed point approached from the two dual sides — one experimental literature, two names.

```
   heights on dual sites:        2 2 3 3 2
                                 1 2 2 2 2      the SOS surface: integer
                                 1 1 2 2 1      "terraces"; steps cost
                                 0 1 1 1 1      (Δh)²/2β per dual link
```
**Figure 2. The height-model face of the XY model. Rough (wandering) surface ↔ low-$T$ QLRO phase of XY; smooth (frozen) surface ↔ high-$T$ disordered phase. Note the inversion: the surface temperature is $\propto 1/T_{\rm XY}$.**

## 4. Third rewriting: spin waves and the Coulomb gas [Computed.]

One more Poisson resummation — on the heights — separates the smooth fluctuations from the integer charges.

**Move 4 — Poisson on each height.** For each dual site, $\sum_{\tilde h\in\mathbb{Z}} f(\tilde h) = \sum_{v\in\mathbb{Z}}\int d\tilde\varphi\, f(\tilde\varphi)\, e^{2\pi i v\tilde\varphi}$:
$$
Z^{(0)}_{\rm SOS} = \sum_{v\,\in\, C^0(\Lambda^*,\mathbb{Z})}\ \int\mathcal{D}\tilde\varphi\;
\exp\!\Big(-\frac{1}{2\beta}\|d\tilde\varphi\|^2 + 2\pi i \sum_{\tilde x} v_{\tilde x}\,\tilde\varphi_{\tilde x}\Big).
$$
The real field $\tilde\varphi$ is the **spin-wave sector** (a free Gaussian field, dual-lattice avatar of the §1 fluctuations); the integers $v_{\tilde x}$ — one per dual site, i.e. **one per plaquette of Λ** — are about to become the vortices. That they sit exactly where Week 1 §4.1 localized vortex charge is the first sign; §6 completes the identification.

**Move 5 — the zero mode enforces neutrality.** Split $\tilde\varphi = \tilde\varphi_0 + \tilde\varphi'$ (constant + orthogonal). The action does not contain $\tilde\varphi_0$ ($d\tilde\varphi_0 = 0$), but the source term does:
$$
\int_{-\infty}^{\infty} d\tilde\varphi_0\; e^{2\pi i \tilde\varphi_0 \sum_{\tilde x} v_{\tilde x}} \;=\; \delta\Big(\sum_{\tilde x} v_{\tilde x}\Big)
\quad\Longrightarrow\quad
\boxed{\ \textstyle\sum_{\tilde x} v_{\tilde x} = 0\ \text{ exactly.}\ }
$$
Charge neutrality of the vortex gas is not an energetic tendency — it is enforced by the noncompact zero mode, configuration by configuration. (On the infinite plane the same statement appears as "a charged configuration costs infinite energy"; the torus derivation is cleaner. Fine print F4.)

**Move 6 — integrate the spin waves.** What remains is a Gaussian with an imaginary source $J = 2\pi v$. Complete the square explicitly: the action for the nonzero modes is $\frac{1}{2\beta}\langle\tilde\varphi', (-\Delta)\tilde\varphi'\rangle - i\langle J, \tilde\varphi'\rangle$; shifting $\tilde\varphi' = \tilde\varphi'' + i\beta\,(-\Delta)^{-1}J$ (legitimate contour rotation for a convergent Gaussian) gives
$$
\frac{1}{2\beta}\langle\tilde\varphi'', (-\Delta)\tilde\varphi''\rangle \;+\; \frac{\beta}{2}\,\langle J,\; (-\Delta)^{-1} J\rangle,
$$
so the $\tilde\varphi''$ integral factors off as the free determinant and the sources are left with $e^{-\frac{\beta}{2}\langle J,\, G' J\rangle}$, where $G' = (-\Delta)^{-1}$ on $\Lambda^*$ with the zero mode omitted (Week 2 §6: the inverse exists exactly on the complement of the harmonic constants). With $J = 2\pi v$, the exponent is $-\frac{\beta}{2}(2\pi)^2\langle v, G'v\rangle = -2\pi^2\beta\,\langle v, G'v\rangle$. Assembling,
$$
Z^{(0)}_{\rm SOS} = Z_{\rm sw}\ \cdot \sum_{\substack{v\,\in\, C^0(\Lambda^*,\mathbb{Z}) \\ \sum v = 0}}
\exp\!\Big(-2\pi^2\beta \sum_{\tilde x,\tilde y} v_{\tilde x}\, G'(\tilde x - \tilde y)\, v_{\tilde y}\Big),
$$
where $Z_{\rm sw} = \int\mathcal{D}\tilde\varphi'\, e^{-\|d\tilde\varphi'\|^2/2\beta}$ is the free spin-wave partition function (a determinant; its correlators reproduce Week 1 §3 — see §7). The factorization
$$
\boxed{\ Z^{(0)} \;=\; (2\pi\beta)^{-N_\ell/2}\; Z_{\rm sw}\; Z_{\rm Coulomb}\ }
$$
is **exact within the zero-tilt sector** — derived, term by term, from the Villain partition function with every prefactor displayed — and the full $Z = \sum_w Z^{(w)}$ multiplies this by the tilt theta function of §3 (whose Gaussian value was computed there; its vortex corrections do not affect bulk observables).

**Move 7 — expose the Coulomb law and the fugacity.** Insert $G'(r) = G'(0) - a(r)$ with $a(r)$ the exact subtracted Green function of Week 1 §3.3 ($a(0) = 0$). Using neutrality:
$$
\sum_{\tilde x,\tilde y} v_{\tilde x}v_{\tilde y}\,G'(\tilde x - \tilde y)
= G'(0)\underbrace{\Big(\sum v\Big)^2}_{=0}\; -\; \sum_{\tilde x \ne \tilde y} v_{\tilde x}v_{\tilde y}\, a(\tilde x - \tilde y)
$$
(diagonal terms of the second sum vanish since $a(0) = 0$). The **exact** vortex weight is therefore
$$
\boxed{\ Z_{\rm Coulomb} = \sum_{\substack{v:\ \sum v = 0}}
\exp\!\Big(2\pi^2\beta \sum_{\tilde x\ne\tilde y} v_{\tilde x}\,v_{\tilde y}\; a(\tilde x - \tilde y)\Big),\ }
$$
with the exact lattice $a(r)$ at *every* separation — this much is an identity.

**The long-distance normal form.** To read off the physics, insert the asymptotics $a(r) = \frac{1}{2\pi}\ln r + \kappa + O(r^{-2})$ — **exact only at large separation**. With $\sum_{\tilde x\ne\tilde y} v_{\tilde x}v_{\tilde y} = (\sum v)^2 - \sum v^2 = -\sum v^2$ (neutrality), the constant κ reorganizes into a per-charge cost:
$$
S_{\rm Coulomb}[v] \;\simeq\; -\pi\beta \sum_{\tilde x\ne\tilde y} v_{\tilde x}v_{\tilde y}\,\ln|\tilde x - \tilde y|
\;+\; \underbrace{2\pi^2\beta\,\kappa}_{\displaystyle E_{\rm core}}\ \sum_{\tilde x} v_{\tilde x}^2,
\qquad
y \equiv e^{-E_{\rm core}} = e^{-2\pi^2\beta\kappa},\quad \kappa = \frac{2\gamma_E + \ln 8}{4\pi}.
$$
Read the status of each symbol correctly: the **logarithmic interaction between well-separated charges is exact** (the $O(r^{-2})$ tail is an irrelevant short-range correction); the **fugacity $y$ is a long-distance matching convention**, the value that reproduces the exact gas when all charges are far apart. Configurations with nearby charges see the exact $a(r)$, whose deviation from the asymptote is a finite set of short-range couplings that further renormalize $y$ (and generate the multi-charge fugacities of F6) without touching the log. In RG terms: $y = e^{-2\pi^2\beta\kappa}$ is the correctly normalized *initial condition at the lattice scale, to leading order in the short-distance corrections* — not an exact microscopic identity. This distinction matters when quoting numbers (Week 4, F2).

**Check against Week 1.** One $+$ at $\tilde x_1$, one $-$ at $\tilde x_2$, well separated: the double sum over ordered pairs gives $2\cdot(+1)(-1)\ln r_{12}$, so $S = 2\pi\beta\ln r_{12} + 2E_{\rm core}$ — exactly the pair energy $2\pi\beta\ln(r/a_0) + 2E_{\rm core}$ estimated in Week 1 §4.3, with the core energy now *identified* in the long-distance normalization: $E_{\rm core} = 2\pi^2\beta\kappa$, the lattice Green-function constant doing physics. Like charges repel, opposite charges attract logarithmically, the gas is neutral: the two-dimensional Coulomb gas, derived.

> **Physical picture.** The XY model is two decoupled theories wearing one set of variables: a free field that is critical at every temperature and never does anything dramatic (spin waves), and a neutral logarithmic plasma that undergoes a dielectric-to-conductor transition (vortices). The duality is valuable because it *diagonalizes* the model into these sectors exactly — with the bonus that the plasma's fugacity is not a free parameter but a computed number, $y = e^{-2\pi^2\beta\kappa}$, fixed by the same lattice constant κ that normalized Week 1's correlator. When Week 4 tunes the vortex fugacity in the RG, this is the microscopic value it starts from.

## 5. Cross-check: the classic decomposition and the cancelling cross term [Model proof.]

JKKN originally argued the factorization by splitting configurations, and the argument identifies the integers $v$ physically. Decompose any configuration as
$$
\theta = \psi + \theta_v,
$$
where $\theta_v$ is a fixed representative carrying the vortex content (harmonic away from the cores: $\nabla^2\theta_v = 0$ except at the prescribed vortex positions, with $\oint\nabla\theta_v\cdot d\ell = 2\pi v$ around each), and ψ is a smooth, single-valued fluctuation. The energy splits as
$$
E[\theta] = \frac{\beta}{2}\int|\nabla\psi|^2 + \beta\int \nabla\psi\cdot\nabla\theta_v + \frac{\beta}{2}\int|\nabla\theta_v|^2 ,
$$
and the cross term vanishes:
$$
\int \nabla\psi\cdot\nabla\theta_v = -\int \psi\,\nabla^2\theta_v + \oint_{\partial} \psi\,\nabla\theta_v\cdot d\vec S = 0,
$$
because $\nabla^2\theta_v = 0$ away from cores, ψ is regular (finite) at the cores where $\nabla^2\theta_v$ has measure-zero support, and the boundary term vanishes on the torus. **The decoupling of spin waves and vortices is the harmonicity of the vortex configuration** — that is the mechanism; the lattice Villain derivation of §§2–4 is its exact, all-orders implementation (no choice of representative $\theta_v$, no continuum approximation). And since the charges of $\theta_v$ are by construction the plaquette windings, the integers $v$ of Move 4 are confirmed to be the physical vorticities $v = dn$ of §1.2. $\square$

## 6. Fourth face: sine-Gordon [Computed to $O(y^2)$, both directions.]

The Coulomb gas has a field-theory generating function. Introduce a real field χ on dual sites with covariance $\langle\chi_{\tilde x}\chi_{\tilde y}\rangle = (2\pi)^2\beta\, G'(\tilde x-\tilde y)$, i.e. Gaussian action $\frac{1}{2(2\pi)^2\beta}\|d\chi\|^2$. Then for any charge configuration,
$$
\Big\langle e^{\,i\sum_{\tilde x} v_{\tilde x}\chi_{\tilde x}}\Big\rangle_\chi
= \exp\Big(-\tfrac12 (2\pi)^2\beta \sum v\,G'\,v\Big)
= \exp\Big(-2\pi^2\beta\sum v\,G'\,v\Big),
$$
exactly the Coulomb weight. Summing over charges with $|v_{\tilde x}| \le 1$ (justified below) and fugacity $y$ per unit charge:
$$
\sum_{v_{\tilde x}\in\{0,\pm1\}} y^{v^2} e^{iv\chi_{\tilde x}} = 1 + 2y\cos\chi_{\tilde x} \;\simeq\; e^{2y\cos\chi_{\tilde x}}\quad(\text{dilute: } y \ll 1),
$$
so
$$
\boxed{\ Z_{\rm Coulomb} \;\simeq\; \int\mathcal{D}\chi\ \exp\!\Big(-\!\int d^2x\,\Big[\frac{1}{8\pi^2\beta}\,(\partial\chi)^2\; -\; 2y\cos\chi\Big]\Big)\ }
$$
— **sine-Gordon**, with stiffness $1/(2\pi)^2\beta$ (continuum normalization $\frac{1}{8\pi^2\beta}$) and the vortex operator $e^{\pm i\chi}$ inserting a $\pm$ charge.

> **Physical picture.** χ is the *disorder field*: its vertex operator creates a vortex, exactly as $e^{i\theta}$ creates a charge — the two fields are each other's dark side, and neither is more fundamental. The $\cos\chi$ potential is the amplitude for the vacuum to nucleate vortex–antivortex pairs; when it is irrelevant the vacuum stays a dielectric of bound pairs, and when it is relevant the field χ gets pinned at a minimum — a "vortex condensate" — which *is* the disordered phase. Pinning χ gaps it, and with it every correlation of the dual theory: this "the disorder field acquires a gap-generating potential from proliferating defects" mechanism is precisely Polyakov's confinement mechanism one dimension up ([[week-08-dual-variables-abelian-gauge|Week 8]]–Week 10), where χ becomes the dual photon and the defects become monopoles. Learn the mechanism here, where nothing else is going on.

**The $O(y^2)$ match, both directions.** Expand $e^{2y\sum\cos\chi}$ and Wick-contract. The $O(y^2)$, charge-neutral term is
$$
y^2 \sum_{\tilde x\ne\tilde y}\big\langle e^{i\chi_{\tilde x}}\, e^{-i\chi_{\tilde y}}\big\rangle
= y^2\sum_{\tilde x\ne\tilde y} e^{\,\langle\chi_{\tilde x}\chi_{\tilde y}\rangle - \langle\chi^2\rangle}
= y^2\sum_{\tilde x\ne\tilde y} e^{-(2\pi)^2\beta\, a(\tilde x-\tilde y)}
= \sum_{\tilde x\ne\tilde y}\, y^2\, e^{-4\pi^2\beta\kappa}\; |\tilde x - \tilde y|^{-2\pi\beta} \cdot e^{...}
$$
— carefully: $(2\pi)^2\beta\, a(r) = 2\pi\beta\ln r + 4\pi^2\beta\kappa$, so the summand is $y^2 e^{-4\pi^2\beta\kappa}\, r^{-2\pi\beta}$. On the Coulomb side, the one-pair term of §4 is $y^2\, e^{-2\pi\beta\ln r} = y^2 r^{-2\pi\beta}$ **per pair with the core already inside $y$** — matching term by term once one fixes a single self-energy bookkeeping: either the vertex operators are normal-ordered (tadpole $e^{-\langle\chi^2\rangle/2}$ removed, cores carried by $y$), or bare (cores generated by the tadpole). The two schemes differ by a finite redefinition $y \to y\,e^{-2\pi^2\beta\kappa'}$ and agree on everything physical (fine print F5). Same-sign $O(y^2)$ terms and the $O(y^1)$ term match trivially (the latter vanishes by neutrality on both sides). The reverse direction — expanding the Coulomb gas and resumming into the χ path integral — is the same computation read upward. $\square$

**The number Week 4 needs.** From the same contraction,
$$
\big\langle e^{i\chi(\tilde x)}\, e^{-i\chi(0)}\big\rangle \sim |\tilde x|^{-2\pi\beta}
\qquad\Longrightarrow\qquad
\Delta_{\rm vortex} = \pi\beta .
$$
The vortex insertion is a scaling operator of dimension $\pi\beta$: **relevant** when $\pi\beta < 2$ ($y$ grows: plasma), **irrelevant** when $\pi\beta > 2$ (bound dipoles), **marginal** at $\beta = 2/\pi$ — precisely Week 1's energy–entropy threshold, now derived as an operator dimension. Week 4 turns this into the Kosterlitz flow.

### 6.1 The operator content of the fixed line [Computed.]

Collect the dimensions of *all* the exponential operators on the Gaussian fixed line of stiffness $\beta_R$ — both the order (electric) operators $e^{iq\theta}$ of Week 1 and the disorder (magnetic) operators $e^{ip\chi}$ of this week:
$$
\Delta^{\rm el}_q = \frac{q^2}{4\pi\beta_R}
\quad(\text{from } \langle e^{iq\theta}e^{-iq\theta}\rangle \sim r^{-q^2/2\pi\beta_R}),
\qquad
\Delta^{\rm mag}_p = \pi\beta_R\, p^2
\quad(\text{from above}).
$$

| operator | dimension | relevant when | role |
|---|---|---|---|
| $e^{i\theta}$ (spin) | $1/4\pi\beta_R$ | always ($\Delta < 2$ in QLRO) | order probe; $\eta = 2\Delta^{\rm el}_1$ |
| $e^{iq\theta}$ | $q^2/4\pi\beta_R$ | small $q$ | higher-charge probes |
| $e^{i\chi}$ (vortex) | $\pi\beta_R$ | $\pi\beta_R < 2$ | drives BKT |
| $e^{ip\chi}$ | $\pi\beta_R\,p^2$ | far in the plasma phase only | multi-vortex (Week 3 F6: negligible) |

Two structural facts sit in this table. First, the **β-independent product**
$$
\Delta^{\rm el}_q\,\cdot\,\Delta^{\rm mag}_p = \frac{q^2p^2}{4}\,,
$$
the fingerprint of the underlying free-boson ("$c = 1$") critical line: electric and magnetic dimensions see the coupling reciprocally, and their product is pure integer data. Second, integer charges $q$ and vortices $p$ are **mutually local** (monodromy phase $e^{2\pi i qp} = 1$), but *fractional* values would braid nontrivially — the germ of anyonic statistics, realized for real in the toric code (Semester II Week 8), where exactly such mutual monodromies between "electric" and "magnetic" excitations become the physical observable. The XY fixed line is the simplest place where the electric/magnetic operator pairing — the engine of Semester II — can be seen whole.

## 7. Charge correlators through the duality [Computed in the spin-wave sector; dressing Sketched.]

What of the original observable $\langle e^{i\theta_x}e^{-i\theta_y}\rangle$? Repeat Moves 1–3 with the insertions. The extra factor $e^{i(\theta_x - \theta_y)}$ shifts the Kronecker constraint at the two marked sites:
$$
\int\frac{d\theta_z}{2\pi}\, e^{i[(\delta m)_z + \epsilon_z]\theta_z} = \delta_{(\delta m)_z,\, -\epsilon_z},
\qquad \epsilon = \mathbb{1}_x - \mathbb{1}_y :
$$
the dual current is no longer conserved — it has a **unit source at $y$ and sink at $x$**. Every configuration contains an open current line from $y$ to $x$ (plus closed loops): the charge correlator is a *sum over integer flux lines* connecting the insertions, the lattice ancestor of "a charged operator trails a Wilson line."

To evaluate, split off one fixed unit current $m_\gamma$ along a chosen path $\gamma_{y\to x}$ (so $\delta m_\gamma = \epsilon$) and write $m = m_\gamma + m'$ with $\delta m' = 0$ integer. The weight splits as
$$
\|m\|^2 = \|m_\gamma\|^2 + 2\, m_\gamma\!\cdot m' + \|m'\|^2 .
$$
Run Moves 4–6 on $m'$: heights, then Poisson, then the Gaussian field $\tilde\varphi$ with vortex charges $v$. In the Gaussian ($v = 0$) sector, the cross term contributes a *real linear source* for $\tilde\varphi$, and the whole computation reduces to one orthogonality argument [Computed]:

**Step 1 — decompose the fixed current.** Real-Hodge-decompose $m_\gamma$ (Week 2 §6; $\gamma$ in the trivial homology class):
$$
m_\gamma = dg + \star d\lambda,
\qquad \delta m_\gamma = \delta d g = \Delta g = \epsilon
\;\Longrightarrow\; g = G * \epsilon
$$
(the co-closed piece $\star d\lambda$ carries no divergence; $g$ is the lattice Coulomb potential of the endpoint charges).

**Step 2 — the sum over $m'$ absorbs the co-closed piece.** The fluctuation integral over the dual field is a shifted Gaussian; shifting $\tilde\varphi$ by the fixed function $\lambda$ (allowed: $\tilde\varphi$ ranges over all reals) cancels the cross term $m_\gamma\cdot m'$ against the co-closed part of $m_\gamma$ *exactly* — the Gaussian sector cannot tell a co-closed background from its own fluctuations. What survives of $\|m_\gamma\|^2 + 2m_\gamma\cdot m'$ after the shift is only the exact piece:
$$
\text{surviving exponent} = -\frac{1}{2\beta}\,\|dg\|^2 .
$$

**Step 3 — evaluate the exact piece.** By adjointness and Step 1,
$$
\|dg\|^2 = \langle g,\, \delta d g\rangle = \langle g,\, \epsilon\rangle
= \langle G*\epsilon,\, \epsilon\rangle
= 2\big[G(0) - G(x-y)\big] = 2\,a(x-y),
$$
using $\epsilon = \mathbb{1}_x - \mathbb{1}_y$ in the last line. Therefore
$$
\big\langle e^{i\theta_x} e^{-i\theta_y}\big\rangle_{\rm sw}
= \exp\!\Big[-\frac{1}{\beta}\, a(x-y)\Big],
$$
**exactly** — path-independence is now manifest (the answer depends on $m_\gamma$ only through $\delta m_\gamma = \epsilon$: any two choices of path differ by a conserved current, which Step 2 absorbs). Expanding $a$ at large distance, this is $e^{-\kappa/\beta}|x-y|^{-1/2\pi\beta}$: Week 1's spin-wave answer — exponent *and* amplitude, and in fact the full exact lattice function $e^{-a(x-y)/\beta}$, not merely its asymptote — recovered from the dual side. No factor was dropped anywhere in Moves 1–6; this is the strongest available consistency check on the whole chain. The vortex charges couple to the open line through the angle it subtends; at low temperature (bound dipoles) they renormalize $C$ and $\beta \to \beta_R$ but preserve the power law; in the plasma phase they screen the line into exponential decay [Sketched — the full dressing is JKKN §III; Problem 3 develops the leading correction]. This is the mechanism by which the *same* transition shows up in the original spin variables.

## 8. The duality dictionary

| XY / spin language | current model | height (SOS) model | Coulomb gas / sine-Gordon |
|---|---|---|---|
| phase $\theta_x$ (compact, sites of Λ) | — | — | dual field $\chi$ (dual sites) |
| stiffness β | loop weight $e^{-m^2/2\beta}$ | surface stiffness $1/2\beta$ | plasma coupling $\pi\beta$; SG stiffness $\frac{1}{(2\pi)^2\beta}$ |
| charge operator $e^{i\theta}$ | open current line | step dislocation | (dual to) $e^{i\chi}$: the vortex operator |
| vortex $v = dn$ (plaquettes) | — | screw-type defect of $\tilde h$ | Coulomb charge; $\cos\chi$ vertex |
| ordered tendency (large β) | dense loops | smooth surface | bound dipoles; $\cos\chi$ irrelevant |
| disordered (small β) | dilute loops | rough surface | free plasma; $\cos\chi$ relevant |
| lattice constant κ (Week 1) | — | — | fugacity $y = e^{-2\pi^2\beta\kappa}$ |

Four faces, one partition function, all equalities exact except the two flagged dilute-gas steps of §6. This is the first full column-set of the semester's duality table; [[week-08-dual-variables-abelian-gauge|Week 8]] adds the gauge rows, and Semester II Week 12 upgrades the whole table to exact operator statements.

## 9. Subtleties and fine print

**F1 — What "exact factorization" rests on.** $Z^{(0)} = (\cdots)\,Z_{\rm sw}Z_{\rm Coulomb}$ came from two structural facts: the exact solvability of the constraint $\delta m = 0$ by heights within a tilt sector (§3) and the *linearity* of the source coupling $2\pi i\,v\cdot\tilde\varphi$ (so the Gaussian integral factorizes, §4). The tilt sectors themselves do **not** factor off exactly (§3): only their Gaussian weights are cleanly computable, which suffices for bulk physics. Perturb the model non-Gaussianly (e.g. cosine instead of Villain) and factorization becomes approximate: the vortex core acquires a size and spin-wave–vortex interactions appear at short distance. They renormalize $y$ and β but generate no new *relevant* couplings — which is why the universal content survives (F2).

**F2 — Villain vs cosine = a fugacity shift.** Matching the two models' character expansions (Week 1, Problem 5) fixes $\tilde\beta(\beta)$ by the first harmonic; the residual mismatch in the higher harmonics is then **algebraically small in $1/\beta$** (the $m = 2$ coefficient first disagrees at subleading order in the $1/\beta$ expansions of $e^{-m^2/2\tilde\beta}$ vs $I_m/I_0$ — power-law, *not* exponentially, suppressed). In Coulomb-gas language: a shifted core energy and small multi-charge fugacities. Consequence: $T_{BKT}$'s *numerical value* differs between the models — and neither equals the naive $2/\pi$: the measured bare critical couplings are $\beta_c^{\cos} \approx 1.12$ and $\beta_c^{\rm Vil} \approx 0.75$ [Stated — refs: standard Monte Carlo values], both well above $2/\pi \approx 0.64$ because screening lowers the renormalized stiffness (Week 4). The transition's existence, the flow, the jump, and all exponents coincide (universal). When comparing with data, match *renormalized stiffnesses*, never bare couplings.

**F3 — The tilt (winding) sectors.** The sector weights $Z^{(w)}/Z^{(0)} \simeq e^{-(w_1^2+w_2^2)/2\beta}$ (Gaussian level, §3) carry the global-current / twisted-boundary-condition physics: inserting a twist α shifts $w_i \to w_i + \alpha/2\pi$ in the theta function, and differentiating twice reproduces the helicity modulus of Week 1 Problem 6. Note the weights are $L$-independent at fixed β — global tilts are *not* volume-suppressed, unlike what a naive "harmonic mode of norm $L^2$" argument would suggest (the error the first version of this section made: the unit-winding configuration relaxes to tilt density $1/L$, and $L^2 \times (1/L)^2 = O(1)$). They are, however, invisible in bulk correlators at any fixed observable separation; they are decisive exactly for stiffness measurements. Dropping the tilt sum is legitimate only after deciding which observable one wants.

**F4 — Neutrality: finite vs infinite volume.** On the torus, neutrality came from a noncompact zero-mode integral — an identity, not energetics. On the infinite plane one instead says "a net charge costs $\sim\ln L \to \infty$." The two statements match: the zero mode *is* the $k \to 0$ limit that makes $G(x)$ itself ill-defined in 2d (Week 1, F5). Systems with a neutralizing background (e.g. an applied "magnetic field" term in JKKN) evade the constraint by modifying exactly this mode.

**F5 — One self-energy, three appearances.** The constant κ enters as (i) the amplitude of Week 1's spin-wave correlator, (ii) the vortex core energy $E_{\rm core} = 2\pi^2\beta\kappa$, (iii) the sine-Gordon tadpole $e^{-\langle\chi^2\rangle/2}$ absorbed by normal-ordering. These are the *same* number seen through three calculations; any consistent scheme keeps it in exactly one place. Double-counting κ (a classic error) shifts the fugacity by a spurious square.

**F6 — The two dilute-gas steps, and why they are safe.** §6 (a) truncated to $|v|\le1$ and (b) exponentiated $1 + 2y\cos\chi$. Both are controlled by operator dimensions: the charge-2 vertex has dimension $4\pi\beta = 4\times$(charge-1) — strongly irrelevant near the transition ($\pi\beta \approx 2$ ⟹ dimension ≈ 8 vs marginality at 2); and the difference $e^{2y\cos\chi} - (1+2y\cos\chi)$ starts at $O(y^2)$ with the *same* operators already present. Neither step touches universal content; both shift non-universal constants only.

## 10. Common misconceptions

- **"The Villain model is an uncontrolled approximation to the real XY model."** The Villain model is a well-defined lattice model in the same universality class, with its *own exact* duality — that is why we compute in it. The relation to the cosine model is a quantified, irrelevant deformation (F2), not an unexamined replacement.
- **"Spin waves drive the transition."** The spin-wave sector is critical at *every* temperature and completely transition-blind; all non-analyticity lives in the Coulomb factor. What spin waves do is fix the vortex interaction (the log) and the critical correlators — the stage, not the play.
- **"Duality maps the XY model to a different theory."** Every arrow in §§2–4 is an identity of partition functions: currents, heights, and the Coulomb gas are the *same theory* in different variables. "Dual" means a change of basis that makes different physics manifest, not a new model. (Semester II sharpens this: dualities are *operators inside* the theory.)
- **"Vortices are inserted by hand into the Gaussian theory."** They were never absent: the integers $n_\ell$ are part of the compact model's definition, and $v = dn$ emerged from resummation, uninvited. It is the *Gaussian* model of Week 1 §3 that was obtained by hand-deletion.

## 11. Historical note

Villain (1975) introduced the periodic Gaussian precisely to make the low-temperature expansion of the XY model tractable; José, Kadanoff, Kirkpatrick and Nelson (1977) turned it into the systematic spin-wave/vortex decomposition reproduced here, extended it to $\mathbb{Z}_N$ clock models and symmetry-breaking fields, and connected the fugacity expansion to Kosterlitz's RG. The height-model face goes back to the same era's crystal-surface literature (Chui–Weeks: roughening = inverted BKT). Fröhlich and Spencer (1981) made the whole picture rigorous — their proof that the Coulomb gas has a dipole phase at large β is, mathematically, the existence proof of the BKT transition, built on the identical representation derived in §4.

## 12. What to take away

1. **The duality is four exact rewritings**: Villain → conserved currents (compactness ⟹ integer Kronecker constraints) → heights + windings (integer Hodge) → spin waves + neutral Coulomb gas (Poisson + zero mode). Every constant tracked; factorization exact.
2. **The vortex gas comes out quantitative**: interaction $-\pi\beta\sum_{\ne} vv\ln r$, exact neutrality from the zero mode, and fugacity $y = e^{-2\pi^2\beta\kappa}$ with κ the Week-1 lattice constant — microscopics feeding the RG.
3. **Sine-Gordon is the same theory once more**, with the vortex operator $e^{i\chi}$ of dimension $\pi\beta$: relevant/irrelevant across $\beta = 2/\pi$. That single dimension is Week 4's input.
4. **The mechanism of decoupling is harmonicity** (§5): vortex configurations solve Laplace away from cores, so they cannot exchange energy with spin waves at quadratic order — the physical reason a free field and a plasma coexist in one model without mixing.

## 13. Looking ahead: Week 4

We hold an exact Coulomb gas with a computed fugacity and a vortex operator of dimension $\pi\beta$. Week 4 asks when the dipoles ionize: the energy–entropy argument, then Kosterlitz's renormalization group — $dy/d\ell = (2-\pi\beta_R)\,y$ and the screening-driven flow of $\beta_R$ — the universal stiffness jump $\rho_s/T_{BKT} = 2/\pi$, and the essential singularity of the correlation length. Then the week pivots to the Ising model's Kramers–Wannier duality and the Kadanoff–Ceva disorder operator: the ℤ₂ sibling of everything done here, and the first duality implemented by a *defect* — the seed of Semester II's non-invertible symmetries.

## 14. Problem set

**Core problems** (everyone).

**1. The correlator through the duality, extended.**
(a) Repeat §7's three steps for charge-$q$ insertions ($\epsilon \to q\,\epsilon$) and show $\langle e^{iq\theta_x}e^{-iq\theta_y}\rangle_{\rm sw} = e^{-q^2 a(x-y)/\beta}$, recovering the $q^2\eta$ of Week 1 Problem 3 with the exact amplitude.
(b) On the $2\times2$ torus, carry out Step 2's shift explicitly: pick two paths between a fixed pair of sites, compute $\|m_\gamma\|^2$ and $\|dg\|^2$ for both, and watch the path-dependence cancel numerically.
(c) Identify which part of the calculation fails if the two insertions carry *unequal* charges $q_1 \ne -q_2$, and reconcile with the neutrality of §4.

**2. Anisotropic duality.**
Redo Moves 1–6 with couplings $\beta_x \ne \beta_y$ (use the weighted Hodge decomposition of Week 2 Problem 7). Show the dual heights see swapped stiffnesses ($\beta_x \leftrightarrow \beta_y$ across the duality) and that the Coulomb gas acquires an anisotropic logarithm. What combination of $\beta_x, \beta_y$ controls the transition?

**3. Vortex dressing of the spin correlator.**
At $O(y^2)$, compute the correction to $\langle e^{i\theta_x}e^{-i\theta_y}\rangle$ from one vortex–antivortex pair interacting with the open current line of §7. Show it renormalizes the effective stiffness downward (the seed of the RG flow of $\beta_R$ in Week 4) and estimate its size at $\pi\beta = 2.2$.

**Starred problems.**

**4⋆. Winding sectors and the helicity modulus.**
From the tilt-sector weights of §3, compute the free-energy response to a twist $\alpha$ across the $x$-cycle (the twist shifts $w_1 \to w_1 + \alpha/2\pi$ inside the Gaussian theta function — show this) and derive the helicity modulus $\Upsilon(\beta)$ of the model in terms of theta functions. Verify $\Upsilon \to \beta$ (spin-wave value) as $L\to\infty$ at large β, and explain how vortices would enter this observable (Week 4 closes this loop with the universal jump).

**5⋆. Multi-charge fugacities.**
Keep $|v| \le 2$ in §6: derive the two-cosine sine-Gordon $2y\cos\chi + 2y_2\cos2\chi$ with $y_2 = e^{-8\pi^2\beta\kappa}$, compute the dimension of $\cos2\chi$, and show it is irrelevant everywhere the charge-1 operator is not strongly relevant. Conclude (in one paragraph) why the BKT fixed-point analysis may safely ignore all $|v|\ge2$.

**6⋆⋆ (optional). The $\mathbb{Z}_N$ clock model.**
Restrict θ to $2\pi k/N$: repeat the duality (the character sum is now finite) and show the dual is a $\mathbb{Z}_N$ clock model with inverted coupling — self-duality. Then couple both the vortex operator ($\cos\chi$) and the clock anisotropy ($\cos N\chi'$-type) and use dimension counting as in §6 to show an intermediate critical phase opens for $N \ge 5$ (two BKT-like transitions), while $N \le 4$ has a single transition. (This is JKKN §IV, and the $\mathbb{Z}_N$ warm-up for Semester II.)

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block A. Rewritten to the note-quality-template standard 2026-07-07 (first draft 2026-07-01).*
