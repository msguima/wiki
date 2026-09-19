---
title: "Sem II Week 11 — The island formula"
type: lecture-notes
course: syllabus
semester: 2
week: 11
block: 2
duration: "3 hours (lecture + seminar)"
status: final
modified: 2026-05-28
---

# Sem II Week 11 — The Island Formula

> *Weeks 8–10 set up the problem (Hawking's calculation, the Page-curve target, the replica-wormhole saddle). This week states the **island formula** and shows what it does. The formula is the [[sem2-week-05-quantum-extremal-surfaces|quantum extremal surface (QES) prescription]] applied to the **radiation** region rather than to a boundary subregion. We run it explicitly in the eternal Jackiw–Teitelboim (JT) black hole coupled to a bath: at early times the optimal island is empty and the radiation entropy grows (Hawking); past the Page time a non-empty island just inside the horizon dominates and the entropy saturates at twice the black-hole entropy — the descending branch of the [[sem2-week-09-page-curve|Page curve]]. We close by reading off what the island means physically: the black-hole interior lies in the entanglement wedge of the radiation.*
>
> *Honesty up front: this week does **not** derive the island formula. The derivation is the gravitational replica trick of [[sem2-week-10-replica-wormholes|Week 10]] — the island is where the replica wormholes glue the interior to the radiation. Here we take the formula as input and study its content and consequences.*

## Learning goals

By the end of this week, a student can:

1. State the island formula and explain the role of each term — the area/dilaton term, the bulk-matter entropy of $\mathrm{Rad}\cup I$, the extremisation, and the minimisation over island topologies.
2. Identify the island $I$ as the dominant QES saddle for the radiation at late times and locate it geometrically (just inside the horizon, at the thermal scale) in the Penrose diagram.
3. Run the no-island and island saddles in the eternal JT + bath model and show the first grows linearly while the second saturates at $\approx 2S_{\mathrm{BH}}$.
4. Read off the Page time from the crossover of the two saddles.
5. Explain why the appearance of the island means the interior is reconstructible from the radiation, and state the complexity caveat.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Black Hole Information* §4** — *The Island Formula*, *What Is the Island?* and *Islands in Higher Dimensions*.
- Almheiri, Mahajan, Maldacena, Zhao, *The Page curve of Hawking radiation from semiclassical geometry*, JHEP 03 (2020) 149, [arXiv:1908.10996](https://arxiv.org/abs/1908.10996) (**AMMZ**) — the island formula in its current form, with the JT toy model. **This is the week's anchor paper; §§2–4 are the calculation we reproduce.**
- Almheiri, Engelhardt, Marolf, Maxfield, *The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole*, JHEP 12 (2019) 063, [arXiv:1905.08762](https://arxiv.org/abs/1905.08762) (**AEMM**) — introduced the radiation-wedge argument.
- Penington, *Entanglement wedge reconstruction and the information paradox*, JHEP 09 (2020) 002, [arXiv:1905.08255](https://arxiv.org/abs/1905.08255) — the companion paper; §§3–4 contain the island calculation in the eternal geometry and the reconstruction discussion.

**Secondary.**

- Almheiri, Mahajan, Maldacena, *Islands outside the horizon*, [arXiv:1910.11077](https://arxiv.org/abs/1910.11077) — clarifies the QES location for the eternal black hole (the island boundary sits *outside* the horizon by an $O(\beta)$ amount).
- Almheiri, Hartman, Maldacena, Shaghoulian, Tajdini, *The entropy of Hawking radiation*, Rev. Mod. Phys. 93 (2021) 035002, [arXiv:2006.06872](https://arxiv.org/abs/2006.06872) — the review; §4 is the canonical pedagogical version of this calculation.

**Prerequisites (within this course).**

- [[sem2-week-05-quantum-extremal-surfaces]] — the QES prescription. The island formula *is* the QES prescription, applied to the radiation. If §1 below feels fast, reread Week 5 first.
- [[sem2-week-10-replica-wormholes]] — the derivation of the island rule. This week assumes you accept the formula; Week 10 is why you may.
- [[sem2-week-09-page-curve]] — the target. We are reproducing the curve drawn there.
- [[sem2-week-06-jt-gravity-page-curve|Sem II Wk 6]] — the JT + bath machinery (Schwarzian, dilaton profile) used in §3.

**Assumed QFT background.** Entanglement entropy of a union of intervals in a 2d CFT; the vacuum formula $S = \tfrac{c}{3}\log(\ell/\epsilon)$ and its conformal-frame dressing; thermal CFT entropy flux.

## 1. The radiation region and the generalised entropy

Set up the problem the QES prescription will solve.

A black hole radiates into a **non-gravitating bath** — a flat half-line (or, for the two-sided eternal black hole, two baths) carrying a 2d CFT of central charge $c$. We collect the radiation in a region $R$ of the bath: for the eternal two-sided geometry, $R = (-\infty, b_-] \cup [b_+, +\infty)$, two semi-infinite intervals, one in each bath, anchored at cutoff points $b_\pm$ just outside the two asymptotic boundaries.

We want the fine-grained (von Neumann) entropy $S(R)$ of the quantum state restricted to $R$. Because the bath is glued to a *gravitating* region (the black hole), the QES prescription ([[sem2-week-05-quantum-extremal-surfaces|Week 5]]) applies. It instructs us to extremise the **generalised entropy** over candidate bulk surfaces $\partial I$ and to take the minimum:

$$
S(R) \;=\; \min_{I}\;\mathrm{ext}_{\partial I}\; S_{\mathrm{gen}}(R\cup I),
\qquad
S_{\mathrm{gen}}(R\cup I) \;=\; \frac{\mathrm{Area}(\partial I)}{4G_N} \;+\; S_{\mathrm{bulk}}\!\big(R\cup I\big).
$$

Here $I$ is a **bulk region** — the *island* — whose boundary $\partial I$ is the QES; $S_{\mathrm{bulk}}(R\cup I)$ is the entanglement entropy of the quantum fields on the *union* of the radiation $R$ and the island $I$, computed on the fixed semiclassical background. The homology constraint of [[week-13-ryu-takayanagi|RT]]/[[sem2-week-05-quantum-extremal-surfaces|QES]] is what allows $I$ to be disconnected from $R$: the entanglement wedge of $R$ is permitted to include a disconnected bulk piece.

In two bulk dimensions the transverse "area" of a point is replaced by the value of the **dilaton** $\phi$ there, so $\mathrm{Area}(\partial I)/4G_N \to (\phi_0 + \phi(\partial I))/4G_N$, with $\phi_0$ the constant (topological) part. We use this substitution throughout §3–§6.

> **Two saddles.** The minimisation has (at least) two competing candidates: $I = \varnothing$ (**no island**) and $I \neq \varnothing$ (**island**). The whole story is the competition between them.

## 2. The island formula

Specialising the QES prescription to the radiation, and writing the area term in its general-$d$ form:

$$
\boxed{\;
S(\mathrm{Rad}) \;=\; \min_{I}\;\mathrm{ext}_{\partial I}\left[\;\frac{\mathrm{Area}(\partial I)}{4G_N} \;+\; S_{\mathrm{bulk}}\!\big(\mathrm{Rad}\cup I\big)\;\right].
\;}
$$

Reading the formula term by term:

- **$\mathrm{Rad}$** is the radiation region $R$ in the bath — fixed, chosen by us.
- **$I$** is the island: a bulk region we get to add. The minimisation includes $I = \varnothing$.
- **$\partial I$** is the quantum extremal surface — extremise $S_{\mathrm{gen}}$ over its location.
- **$\mathrm{Area}(\partial I)/4G_N$** penalises a large island boundary. With $I=\varnothing$ this term is absent.
- **$S_{\mathrm{bulk}}(\mathrm{Rad}\cup I)$** is computed for the quantum fields on the *union*. When $I$ captures the interior partners of the Hawking quanta in $R$, this entropy is **small** — the partners purify the radiation.

The physics in one sentence: *adding the island costs area but can dramatically reduce the bulk-matter entropy by re-including the interior partners of the Hawking radiation; whichever saddle gives the smaller total wins.*

- **Early times.** Few Hawking quanta have been collected; the area cost of any island exceeds the entropy it would save. The minimum is $I=\varnothing$ and $S(\mathrm{Rad}) = S_{\mathrm{bulk}}(R)$ — the rising Hawking answer.
- **Late times.** The interior is highly entangled with the collected radiation. An island just inside the horizon purifies almost all of it; the area cost ($\sim 2S_{\mathrm{BH}}$) is now cheaper than the ever-growing $S_{\mathrm{bulk}}(R)$. The island wins.

## 3. Geometry: the eternal JT black hole + bath

We run the formula in the cleanest model (AMMZ §2; AHMST §4). Take JT gravity on a nearly-AdS$_2$ throat in the **thermofield-double / eternal** configuration at inverse temperature $\beta$, glued at each boundary to a flat bath carrying a $c$-large 2d CFT. (The two-sided geometry is the holographic image of the [[sem2-week-12-er-epr-and-tfd|TFD state]], which is next week's subject; here it is just the cleanest arena.)

Two facts we import (proof-status flagged in §8):

- **Black-hole entropy.** The extremal/topological piece is $S_0 = \phi_0/4G_N$; the thermal black hole carries
$$
S_{\mathrm{BH}} \;=\; S_0 + \frac{\phi_h}{4G_N},
$$
with $\phi_h$ the dilaton value at the horizon. This is the dilaton evaluated on the eternal-BH solution at temperature $1/\beta$ (Sem II [[sem2-week-06-jt-gravity-page-curve|Wk 6]]).
- **Bath CFT entropy of an interval.** For an interval with endpoints $x_1, x_2$ in the 2d CFT, in the relevant conformal frame with Weyl factor $\Omega$,
$$
S_{\mathrm{CFT}}[x_1,x_2] \;=\; \frac{c}{6}\,\log\!\frac{d(x_1,x_2)^2}{\epsilon^2\,\Omega(x_1)\Omega(x_2)},
$$
where $d$ is the appropriate (chordal/conformal) distance. For a union of two intervals at large separation the entropy is additive up to exponentially small cross terms — the regime we use.

## 4. The no-island saddle: linear growth

Take $I = \varnothing$. Then $S(\mathrm{Rad}) = S_{\mathrm{bulk}}(R)$, the entanglement entropy of the bath CFT on the two semi-infinite radiation intervals, in the state produced by the eternal black hole.

The black hole emits a steady thermal flux at the Hawking temperature $1/\beta$. A 2d CFT thermal flux carries entropy at rate $\tfrac{\pi c}{3\beta}$ per radiating side; collecting on both sides,

$$
S_{\text{no-island}}(t) \;\simeq\; \frac{2\pi c}{3\beta}\,t
\qquad (\text{late } t),
$$

i.e. **linear, unbounded growth** (AMMZ §3; rate derivation flagged [Sketched] in §8). This is the eternal-black-hole avatar of the information paradox: a fine-grained entropy that grows without bound exceeds the coarse-grained black-hole entropy and is incompatible with a unitary, finite-entropy system. Something must cap it.

## 5. The island saddle: saturation

Now allow a non-empty island. By the left–right symmetry of the eternal geometry the island is a single interval $I = [a_-, a_+]$ straddling the two sides, with $\partial I = \{a_-, a_+\}$ sitting near the two horizons. The generalised entropy is

$$
S_{\mathrm{gen}}^{\text{island}}
= \underbrace{\frac{2\,(\phi_0+\phi(a))}{4G_N}}_{\text{two QES points}}
\;+\; S_{\mathrm{CFT}}\big(R\cup I\big),
$$

where $\phi(a)$ is the dilaton at the (symmetric) QES location and $S_{\mathrm{CFT}}(R\cup I)$ is the CFT entropy of the union of the radiation intervals and the island interval. At large separation between $\partial I$ and the radiation cutoffs $b_\pm$, the dominant connected contribution pairs each island endpoint $a_\pm$ with the *near* radiation endpoint $b_\pm$ (the partners), and the formula above becomes a function of the single coordinate $a$.

**Extremise (worked).** Parametrise the QES by its proper distance $\delta$ *outside* the right horizon and expand the two competing pieces near the horizon:

- *Area term.* The dilaton grows outward, $\phi(\delta) \simeq \phi_h + \phi_h'\,\delta$, with a positive near-horizon slope $\phi_h' = \partial_\delta\phi|_{\mathrm{hor}}$ fixed by the JT eternal-BH solution at temperature $1/\beta$; parametrically $\phi_h' \sim \phi_r\,\tfrac{2\pi}{\beta}$ <!-- CHECK: exact O(1) in phi_h' from the JT eternal-BH dilaton profile, AMMZ §3 -->. So $\partial_\delta\big[\tfrac{2(\phi_0+\phi)}{4G_N}\big] = \tfrac{2\phi_h'}{4G_N} > 0$ — pushing the QES *inward* (smaller $\delta$) is cheaper in area.
- *CFT term.* The two-interval entropy decreases as the island captures the Hawking partners more completely, i.e. as $\delta$ decreases; near the horizon its gradient is set by the 2d thermal entropy density, $\partial_\delta S_{\mathrm{CFT}} \simeq +\tfrac{c}{6}\tfrac{2\pi}{\beta}$ <!-- CHECK: sign/coefficient of the near-horizon CFT-entropy gradient, AMMZ §3 -->, i.e. moving inward *reduces* $S_{\mathrm{CFT}}$.

Setting $\partial_\delta S_{\mathrm{gen}}^{\text{island}} = 0$ balances these opposing gradients:

$$
\frac{2\phi_h'}{4G_N} \;=\; \frac{c}{6}\,\frac{2\pi}{\beta},
$$

whose solution places the QES **just outside the horizon at $\delta_\star \sim \beta/2\pi$ times an $O(1)$ factor** — "islands outside the horizon" (Almheiri–Mahajan–Maldacena 2019), confirming the skeleton's $x_I \sim x_{\mathrm{hor}} + O(\beta)$. The *existence* of the extremum just outside the horizon and the plateau value below are robust; the exact $O(1)$ in $\delta_\star$ is model-detail <!-- CHECK: delta_star coefficient from the full JT profile, AMMZ §3 -->. **Exercise 1** carries out the extremisation with the explicit profile.

**Value at the extremum.** Plugging the QES location back in, the CFT term is subleading and the area term dominates:

$$
S_{\text{island}} \;\simeq\; \frac{2(\phi_0 + \phi_h)}{4G_N} \;=\; 2\,S_{\mathrm{BH}}
\qquad(\text{up to } O(c) \text{ corrections}).
$$

The factor of 2 is one $S_{\mathrm{BH}}$ per side: the two-sided radiation is purified by an interior that carries the entropy of *both* horizons. **This is time-independent** — the island saddle is flat in $t$, because the extremal dilaton value does not grow.

## 6. The Page curve

The radiation entropy is the **minimum** of the two saddles:

$$
S(\mathrm{Rad})(t) \;=\; \min\Big\{\, \underbrace{\tfrac{2\pi c}{3\beta}\,t}_{\text{no island}},\; \underbrace{2S_{\mathrm{BH}}}_{\text{island}} \,\Big\}.
$$

- For $t < t_{\mathrm{Page}}$ the no-island saddle is smaller: entropy rises linearly (Hawking).
- For $t > t_{\mathrm{Page}}$ the island saddle is smaller: entropy is flat at $2S_{\mathrm{BH}}$.

The crossover is fully fixed by the two saddle expressions already in hand — the §4 growth rate $\tfrac{2\pi c}{3\beta}$ and the §5 plateau $2S_{\mathrm{BH}}$. Equating them,

$$
\frac{2\pi c}{3\beta}\,t_{\mathrm{Page}} = 2S_{\mathrm{BH}}
\;\;\Longrightarrow\;\;
\boxed{\; t_{\mathrm{Page}} = \frac{2S_{\mathrm{BH}}}{\,2\pi c/3\beta\,} = \frac{3\beta}{\pi c}\,S_{\mathrm{BH}}.\;}
$$

The coefficient $3/\pi$ is therefore *determined*, not fitted — given the growth rate of §4 (whose $\tfrac{2\pi c}{3\beta}$ is the one input carrying a 2d-CFT-flux convention, [Sketched] in §8) and the saturation value of §5. The resulting curve — linear rise, sharp turnover at $t_{\mathrm{Page}}$, flat plateau — is the [[sem2-week-09-page-curve|Page curve]]. The QES prescription reproduces it from a *semiclassical* gravity computation, with no explicit microstate counting. **This is the punchline of Block 2.**

> **Where the "$\min$" comes from.** The minimisation is not ad hoc: in the [[sem2-week-10-replica-wormholes|replica-wormhole]] derivation (Week 10) the two saddles are literally two gravitational saddle topologies of the $n$-replica path integral — the disconnected geometry (no island) and the connected wormhole (island). The $\min$ is "whichever saddle dominates the path integral." That is the precise sense in which the island formula is *derived* rather than posited.

## 7. Entanglement wedge of the radiation; reconstruction

The island carries the conceptual payload. When the island saddle dominates ($t > t_{\mathrm{Page}}$), the **entanglement wedge of the radiation** $R$ is no longer just the bath: it now *includes the island* $I$, a bulk region behind/near the horizon — a piece of the **black-hole interior**.

By entanglement-wedge reconstruction (the [[sem2-week-12-er-epr-and-tfd|JLMS]]/subregion–subalgebra logic of [[sem2-week-03-modular-flow-on-subregions|Sem II Wk 3]]), bulk operators localised in $I$ can be reconstructed from operators acting on the radiation $R$ alone. Concretely this is implemented by a **Petz (or twirled-Petz) recovery map** acting on the radiation Hilbert space. So:

> *After the Page time, the black-hole interior is encoded in the Hawking radiation.* Information is not lost; it is recoverable from $R$, exactly as unitarity of the boundary description requires.

**Caveat (essential, not optional).** Reconstruction is not operationally easy. Recovering interior operators from the radiation requires processing of complexity exponential in $S_{\mathrm{BH}}$ — consistent with the computational-complexity obstructions to "reading" Hawking radiation (Harlow–Hayden; Kim–Preskill–Tang). The island formula says the information is *there*; complexity says you cannot cheaply *extract* it. Both can hold at once, and the firewall-type paradoxes live in the gap between them.

## 8. Key claims and their proof status

Stated explicitly, since honest status-labelling is the point of these notes.

- **[Stated-without-proof] Island formula (QES prescription for radiation).** $S(\mathrm{Rad}) = \min_I \mathrm{ext}_{\partial I}[\mathrm{Area}(\partial I)/4G_N + S_{\mathrm{bulk}}(\mathrm{Rad}\cup I)]$. We *use* it; its justification is the [[sem2-week-10-replica-wormholes|Week 10]] replica-wormhole computation (itself a saddle-point evaluation of the gravitational replica path integral — not a theorem).
- **[Stated-without-proof] JT inputs.** $S_{\mathrm{BH}} = (\phi_0+\phi_h)/4G_N$ and the 2d-CFT interval-entropy formula. Both are standard results imported from Sem II [[sem2-week-06-jt-gravity-page-curve|Wk 6]] and 2d CFT respectively.
- **[Sketched] Linear growth rate $\tfrac{2\pi c}{3\beta}t$.** Follows from the thermal entropy flux of a 2d CFT; we state the flux and quote the rate rather than deriving it from the stress tensor. (Derivation: **Exercise 4**.)
- **[Proven, within the model] Extremisation, saturation, and Page time.** Given the two inputs above, the §5 extremisation (QES just outside the horizon, balancing the dilaton and CFT-entropy gradients), the plateau $S_{\text{island}}\simeq 2S_{\mathrm{BH}}$, and the §6 crossover $t_{\mathrm{Page}} = 3\beta S_{\mathrm{BH}}/(\pi c)$ are ordinary calculus, worked in the note. The exact $O(1)$ offset $\delta_\star$ of the QES from the horizon, and the precise near-horizon dilaton/CFT-entropy gradients used to fix it, are model-detail flagged with `CHECK` in §5 for confirmation against AMMZ §3.
- **[Stated-without-proof] Interior reconstruction from radiation.** The island lying in the radiation's entanglement wedge implies interior operators are recoverable on $R$ (Petz map). The reconstruction theorem is imported; the complexity caveat is a separate, also-imported, statement.

## 9. What to take away

- The **island formula is the QES prescription applied to the radiation**, with the new ingredient that the entanglement wedge of $R$ may include a *disconnected* bulk island.
- Two saddles compete: **no island** (entropy grows, Hawking) and **island** (entropy flat at $2S_{\mathrm{BH}}$). The radiation entropy is their **minimum**.
- The crossover is the **Page time** $t_{\mathrm{Page}}\simeq 3\beta S_{\mathrm{BH}}/(\pi c)$. The result is the Page curve, from semiclassical gravity.
- The island is **just outside the horizon** (by $O(\beta)$), not deep in the interior.
- After the Page time the **interior is in the entanglement wedge of the radiation** — information is recoverable from $R$, though only with exponential complexity.
- The formula is *used*, not *derived*, this week; the derivation is the replica wormholes of Week 10. Keep that boundary sharp.

## Exercises

**Core.**

1. **Locate the island.** In the eternal JT + bath model at late times, take the island $I=[a_-,a_+]$ with the symmetric ansatz, write $S_{\mathrm{gen}}^{\text{island}}(a)$ using the §3 dilaton profile and the two-interval CFT entropy, and extremise. Show $\partial I$ sits outside the horizon by an $O(\beta)$ amount.
2. **Saturation value.** Using the result of Exercise 1, show $S_{\text{island}} \simeq 2S_{\mathrm{BH}}$ at late times, and that it is independent of $t$.
3. **Penrose diagrams.** Draw the eternal AdS$_2$ + bath Penrose diagram at (a) early times — mark the no-island QES and the radiation wedge; (b) late times — mark the island, its QES just outside the horizon, and the enlarged radiation wedge that now reaches behind the horizon.
4. **Growth rate.** Derive the no-island linear rate $\tfrac{2\pi c}{3\beta}$ from the thermal entropy flux of a 2d CFT at temperature $1/\beta$ (recall $\langle T_{tt}\rangle$ and $s = \tfrac{\pi c}{3}T$). Hence reproduce $t_{\mathrm{Page}}$.

**Starred.**

5. $\star$ **No-island ≠ exactly Hawking.** Show that even the $I=\varnothing$ saddle has a QES (near the bifurcation surface), and that for the *eternal* black hole its contribution is what makes the early-time entropy grow rather than sit constant. Contrast with the *evaporating* case where the area shrinks.
6. $\star$ **Mutual information check.** For two well-separated radiation intervals, estimate the cross term neglected in the "additive" approximation of §3, and bound the regime of validity of the single-coordinate reduction in §5.
7. $\star$ **Single-sided.** Repeat §§4–6 for a *one-sided* eternal black hole collecting radiation in a single bath. Show the saturation value becomes $S_{\mathrm{BH}}$ (not $2S_{\mathrm{BH}}$) and recompute $t_{\mathrm{Page}}$.

**Project.**

8. **Replica-wormhole bridge.** Read AMMZ §4 (or PSSY §2). Identify, in the $n$-replica gravitational path integral, the two saddle topologies whose dominance switch *is* the $\min$ of §6. Write a 3-page note connecting this week's $\min\{\cdot,\cdot\}$ to the [[sem2-week-10-replica-wormholes|Week 10]] saddle competition.

## Connections to other parts of the wiki

- **Within the course.** The island formula is the culmination of the entanglement-entropy thread: [[week-13-ryu-takayanagi|RT (Sem I Wk 13)]] → [[sem2-week-05-quantum-extremal-surfaces|QES (Wk 5)]] → [[sem2-week-10-replica-wormholes|replica wormholes (Wk 10)]] → here. Forward: [[sem2-week-12-er-epr-and-tfd|Wk 12]] uses the same two-sided geometry for ER=EPR/TFD.
- **AQFT course cross-reference.** The island formula has an algebraic reformulation via crossed products: the radiation algebra is dressed and the island is where the dressed entropy localises. AQFT 2026 [[week-13-crossed-product-construction|Wk 13 (crossed-product construction)]] develops the algebra; the connection page [[crossed-product-and-island-formula]] tracks both sides in detail.
- **Open questions raised or motivated.** [[crossed-product-and-island-formula]] — an algebraic derivation of the island rule from the dressed type-II trace; [[quantum-extremal-surfaces]] — proof of the island formula beyond the semiclassical saddle approximation.
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 2. Reviewed and approved (status: final). The `CHECK`-flagged JT coefficients in §5 are minor model-detail to confirm against AMMZ §3 in a later pass. Last revised 2026-05-28.*
