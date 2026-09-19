---
title: "Sem II Week 14 — Traversable wormholes: Gao–Jafferis–Wall"
type: lecture-notes
course: syllabus
semester: 2
week: 14
block: 2
duration: "3 hours (lecture + seminar)"
status: drafting
modified: 2026-05-28
---

# Sem II Week 14 — Traversable Wormholes: Gao–Jafferis–Wall

> *Week 12 left us with a non-traversable wormhole: the two boundaries of the eternal black hole commute, and the Einstein–Rosen bridge is spacelike. This week we open it. Gao–Jafferis–Wall couple the two boundaries by a double-trace deformation $g\,\mathcal{O}_L\mathcal{O}_R$; for the right sign this injects **negative averaged null energy** onto the horizon, violating the ANEC of [[sem2-week-13-quantum-focusing-anec|Week 13]] and giving an infalling signal a time **advance** that lets it cross. We then meet the Maldacena–Qi eternal traversable wormhole (two coupled SYK models) and — the punchline for this group — the fact that the GJW deformation is, algebraically, exactly the **cocycle perturbation** studied in the AAJ programme of the AQFT course.*
>
> *Honesty up front: the GJW negative-energy calculation is sign-convention-heavy (Kruskal orientation, the time-folding of $\mathcal{O}_L\mathcal{O}_R$, the sign of $g$). This note derives the **structure** and the parametric result faithfully and **flags every sign-/coefficient-sensitive step** for the reader to confirm against GJW §§2–4 rather than asserting a definite numerical factor. The robust, convention-free statement — "negative averaged null energy ⟹ traversable" — is given cleanly.*

## Learning goals

By the end of this week, a student can:

1. State the GJW mechanism: a double-trace deformation $g\,\mathcal{O}_L\mathcal{O}_R$ injects negative averaged null energy and opens the wormhole.
2. State the convention-free traversability criterion $\int dU\,\langle T_{UU}\rangle < 0$ and explain *why* a negative ANEC integral gives a time advance (integrated Raychaudhuri/Einstein equation).
3. Set up the leading-order-in-$g$ perturbation of $\langle T_{UU}\rangle$ and identify which sign of $g$ and which operator dimension open the wormhole.
4. Explain the teleportation interpretation and sketch the Maldacena–Qi SYK construction.
5. State the algebraic reading: GJW = cocycle perturbation of the crossed-product algebra (AAJ), the closest contact between this course and the group's programme.

## 0. Reading and prerequisites

**Primary reading.**


- **adscft.org — *Black Hole Information* §5** — the *ER=EPR and Traversable Wormholes* page.
- Gao, Jafferis, Wall, *Traversable wormholes via a double trace deformation*, JHEP 12 (2017) 151, [arXiv:1608.05687](https://arxiv.org/abs/1608.05687) (**GJW**) — **the anchor**; §§2–4 contain the explicit negative-energy calculation. *Read these for the exact sign conventions this note flags.*
- Maldacena, Qi, *Eternal traversable wormhole*, [arXiv:1804.00491](https://arxiv.org/abs/1804.00491) — the coupled-SYK eternal wormhole.
- Maldacena, Stanford, Yang, *Diving into traversable wormholes*, [arXiv:1704.05333](https://arxiv.org/abs/1704.05333) (secondary) — the teleportation interpretation.

**Prerequisites (within the course).**

- [[sem2-week-12-er-epr-and-tfd]] — the TFD and the eternal black hole; the GJW deformation modifies that Hamiltonian.
- [[sem2-week-13-quantum-focusing-anec]] — ANEC and why its violation is necessary for traversability.

**For students coming from the AQFT course.** AQFT 2026 Sem II Block 4 (AAJ) develops the cocycle perturbation theory of the crossed-product algebra — the operator-algebraic form of exactly this deformation. §6 below is the bridge.

**Assumed.** Kruskal coordinates on the eternal BH; first-order time-dependent perturbation theory; the thermal (TFD) two-point function from [[sem2-week-12-er-epr-and-tfd|Wk 12]].

## 1. The obstruction, recalled

From [[sem2-week-12-er-epr-and-tfd|Wk 12]]: the eternal black hole's two exteriors are causally disconnected, $[\mathcal{A}_L,\mathcal{A}_R]=0$, and the wormhole is spacelike. From [[sem2-week-13-quantum-focusing-anec|Wk 13]]: in any reasonable unperturbed QFT the **averaged null energy** is non-negative,

$$
\int_{-\infty}^{\infty} dU\;\langle T_{UU}(U)\rangle \;\ge\; 0 \qquad(\text{ANEC}),
$$

along a complete null geodesic. The next box explains why this is exactly the obstruction to crossing.

> **[Stated-without-proof]** ANEC for the unperturbed theory (Wk 13; proved for free/interacting QFT by Faulkner et al. and Hartman et al.).

## 2. Traversability ⟺ negative averaged null energy (the robust statement)

Work in Kruskal coordinates $(U,V)$ on the eternal AdS-Schwarzschild geometry, future horizon at $U=0$. Consider a signal sent inward from the right boundary along an outgoing null ray of fixed $U$, trying to reach the left boundary. Backreaction of stress-energy on the horizon shifts the ray's $V$-coordinate by an amount obtained by integrating the $UU$-Einstein equation across the horizon (the Shapiro/Dray–’t Hooft computation):

$$
\boxed{\;\Delta V \;=\; -\,\frac{(\text{positive geometric factor})\,\times\,G_N}{\;}\int_{-\infty}^{\infty} dU\;\langle T_{UU}(U)\rangle.\;}
$$

The sign is the whole story:

- **ANEC obeyed** ($\int dU\,\langle T_{UU}\rangle \ge 0$): $\Delta V \le 0$ in the convention where a *positive* $\Delta V$ is needed to emerge in the other exterior — i.e. the signal is delayed (Shapiro **time delay**) and cannot cross. *(Sign of "delay vs advance" depends on the $U,V$ orientation — `<!-- CHECK: fix the convention so ANEC ⇒ delay; GJW eq (2.x) -->`.)*
- **ANEC violated** ($\int dU\,\langle T_{UU}\rangle < 0$): $\Delta V$ has the opposite sign — a **time advance** — and the signal emerges in the opposite exterior: the wormhole is traversable.

The convention-free content, which is robust: **a negative averaged null energy on the horizon makes the wormhole traversable.** Everything in §3 is about engineering that negative integral.

> **[Stated-without-proof]** the $\Delta V \propto -\int\langle T_{UU}\rangle$ relation (integrated Einstein equation; GJW §2, Dray–’t Hooft). The overall sign/orientation is flagged for the reader to fix against GJW.

## 3. The GJW double-trace deformation (worked structure, flagged coefficients)

**The deformation.** Couple the two boundaries, turning on at $t=0$:

$$
\delta H(t) = g\,\theta(t)\!\int\! d^{d-1}x\;\mathcal{O}_R(t,x)\,\mathcal{O}_L(t,x),
$$

with $\mathcal{O}$ a **relevant** scalar primary of dimension $\Delta$. (Some treatments fold the left time, $\mathcal{O}_L(-t)$; the choice tracks the TFD's L–R identification — `<!-- CHECK: GJW use the time-reflected pairing; confirm before fixing exercise signs -->`.) Because $\mathcal{O}_L\in\mathcal{A}_L$ and $\mathcal{O}_R\in\mathcal{A}_R$ previously commuted, this is precisely the coupling that breaks $[\mathcal{A}_L,\mathcal{A}_R]=0$ and lets $R$ talk to $L$.

**Leading effect on the null energy.** In first-order time-dependent perturbation theory, the expectation of $T_{UU}$ on the horizon in the deformed state is

$$
\langle T_{UU}(U)\rangle = \underbrace{\langle\mathrm{TFD}|T_{UU}|\mathrm{TFD}\rangle}_{=\,0\ \text{on the horizon}} \;+\; i\,g\!\int\! dt\,\big\langle\,[\,\mathcal{O}_R(t)\mathcal{O}_L(t),\,T_{UU}(U)\,]\,\big\rangle \;+\; O(g^2).
$$

The unperturbed term vanishes (the TFD is the Hartle–Hawking/vacuum state, regular on the horizon). So the leading effect is **$O(g)$**, and the integrated null energy is

$$
\int dU\;\langle T_{UU}\rangle \;=\; g\,\times\, \mathcal{I}(\Delta,\beta) \;+\; O(g^2),
$$

where $\mathcal{I}(\Delta,\beta)$ is a horizon integral of the TFD two-point function $\langle\mathcal{O}_L\mathcal{O}_R\rangle$ (the analytically-continued thermal correlator of [[sem2-week-12-er-epr-and-tfd|Wk 12]]) against the bulk-to-boundary propagator. The structure is robust; the explicit value and sign of $\mathcal{I}$ are convention-dependent:

> `<!-- CHECK: sign and magnitude of I(Delta,beta), hence the sign of g that gives the negative integral. GJW find the integral is negative for one sign of the coupling and a relevant operator; reproduce GJW eq (3.x)-(4.x) before asserting the sign. -->`

**The result (GJW).** For a **relevant** operator and the **appropriate sign of $g$**, $\int dU\,\langle T_{UU}\rangle < 0$ — ANEC is violated and the wormhole opens. The induced advance is parametrically

$$
\Delta V \;\sim\; -\,g\,G_N\;|\mathcal{I}(\Delta,\beta)| \;<\;0 \quad(\text{traversable, for the right sign of }g),
$$

so $\Delta V = O(G_N)$ — the opening is a quantum ($1/N$) effect, as it must be (classically ANEC forbids it). The window during which the wormhole is open is set by the thermal scale, $\Delta t_{\mathrm{open}} \sim \beta_H$.

**Why only relevant operators.** For irrelevant $\mathcal{O}$ ($\Delta$ too large) the horizon integral $\mathcal{I}$ either fails to converge favourably or carries the wrong sign; the deformation is also irrelevant in the RG sense and does not survive to the IR. Relevant $\mathcal{O}$ ($\Delta < d$, with the precise window set by convergence of $\mathcal{I}$) is what GJW require — **Exercise 2** works out the dimension condition.

> **[Sketched]** the $O(g)$ structure and the parametric $\Delta V$. **[Stated-without-proof, sign flagged]** that the integral is negative for the GJW sign/operator. This is the note's one genuinely convention-sensitive result — the `CHECK` flags mark exactly what to confirm against GJW.

## 4. Traversability and teleportation

Once $\Delta V<0$, a signal from the right exterior reaches the left exterior within the open window. The interpretation (Maldacena–Stanford–Yang) is **quantum teleportation through the wormhole**:

- the TFD is the **EPR resource** shared between $L$ and $R$;
- the double-trace coupling $g\,\mathcal{O}_L\mathcal{O}_R$ plays the role of the **classical communication** (it transmits, in effect, the measurement outcome that lets $L$ decode);
- the Einstein–Rosen bridge is the **quantum channel** along which the state travels.

A qubit thrown into the right black hole emerges from the left after the coupling is applied — a geometrically vivid realisation of teleportation. (No superluminal signalling: the coupling is an explicit interaction between the two systems.)

> **[Stated-without-proof]** the teleportation equivalence (MSY 2017).

## 5. Maldacena–Qi: the eternal traversable wormhole

Replace "turn on a coupling at $t=0$" with a **permanent** coupling. Maldacena–Qi take two SYK models and couple them:

$$
H = H_L^{\mathrm{SYK}} + H_R^{\mathrm{SYK}} + i\mu\sum_j \psi_L^j\,\psi_R^j.
$$

At low temperature the ground state is close to the TFD and is dual to a wormhole that stays **open at all times** — an eternal traversable wormhole, a genuine ground-state phase of the coupled system. There is a transition (as a function of $T/\mu$) between a high-temperature two-black-hole phase (wormhole closed) and a low-temperature wormhole phase (open) at $T\sim\mu$.

> **[Stated-without-proof]** Maldacena–Qi construction and the $T\sim\mu$ transition.

## 6. The algebraic bridge: GJW = cocycle perturbation (closest contact with the group's programme)

This is the week where the course touches the group's own research most directly. Algebraically, the GJW deformation is a **perturbation of the state** on the eternal black hole's algebra. In the [[crossed-product-construction|crossed-product]] description (CPW, [[sem2-week-12-er-epr-and-tfd|Wk 12 §6]]), the perturbed state $\omega_g$ is related to the unperturbed TFD state $\omega_0$ by the **Connes cocycle** $u_t = (D\omega_g : D\omega_0)_t$ — exactly the object the **AAJ programme** (AQFT Sem II Block 4) expands perturbatively to compute corrections to the dressed (generalised) entropy.

| This course (holographic) | AQFT course (algebraic) |
|---|---|
| GJW double-trace $g\,\mathcal{O}_L\mathcal{O}_R$ | state perturbation $\omega_0 \to \omega_g$ |
| negative null energy / opening | shift in the dressed type II$_\infty$ trace |
| $\Delta V = O(G_N)$ | $O(1/N^2)$ cocycle correction |
| traversability window $\sim\beta$ | modular-time support of $u_t$ |

So the bulk statement "the wormhole opens by $O(G_N)$" and the algebraic statement "the dressed entropy receives an $O(1/N^2)$ cocycle correction" are two faces of one computation. This is the natural place to connect to the group's [[holographic-dual-embezzlement-protocol|embezzlement / cost-theorem]] question: both ask what the leading $G_N$ (equivalently $1/N^2$) correction does to an exact-at-$N=\infty$ statement. See [[crossed-product-and-island-formula]].

## 7. Key claims and proof status

- **[Stated-without-proof]** ANEC in the unperturbed theory (Wk 13).
- **[Stated-without-proof]** $\Delta V \propto -\int dU\,\langle T_{UU}\rangle$ (integrated Einstein eq.; GJW §2) — **overall sign/orientation flagged**.
- **[Sketched]** the $O(g)$ structure of $\langle T_{UU}\rangle$ and the parametric $\Delta V \sim -g\,G_N|\mathcal{I}|$.
- **[Stated-without-proof, sign flagged]** that the GJW integral is negative for a relevant operator and the right sign of $g$ — **the `CHECK` items in §§2–3 must be confirmed against GJW before this note is stamped `final`.**
- **[Stated-without-proof]** teleportation equivalence (MSY); Maldacena–Qi eternal wormhole and the $T\sim\mu$ transition.
- **[Stated-without-proof]** GJW = Connes-cocycle perturbation (AAJ) — the algebraic dictionary of §6.

### `CHECK` items for the researcher (Wk 14)

1. **§2** — orientation/sign of $\Delta V \propto -\int\langle T_{UU}\rangle$ so that ANEC ⇒ delay (not advance). Confirm against GJW eq. (2.x).
2. **§3** — time-folding of the double-trace operator ($\mathcal{O}_L(t)$ vs $\mathcal{O}_L(-t)$).
3. **§3** — sign and magnitude of the horizon integral $\mathcal{I}(\Delta,\beta)$, hence which sign of $g$ opens the wormhole and the precise relevant-operator window.

These are the only places this batch asserts physics I did not fully pin down; they are deliberately flagged rather than guessed.

## 8. What to take away

- **Traversability ⟺ negative averaged null energy** $\int dU\,\langle T_{UU}\rangle < 0$ on the horizon — the one convention-free statement.
- **GJW:** a relevant double-trace $g\,\mathcal{O}_L\mathcal{O}_R$ injects that negative energy at $O(g)$; the opening is an $O(G_N)$ quantum effect, window $\sim\beta$.
- **Teleportation:** TFD = EPR resource, coupling = classical channel, bridge = quantum channel.
- **Maldacena–Qi:** coupled SYK gives an *eternal* traversable wormhole; transition at $T\sim\mu$.
- **Algebra:** GJW = Connes-cocycle perturbation of the crossed-product algebra (AAJ) — the tightest link between this course and the group's programme.
- The exact GJW sign/coefficient is **flagged, not asserted** (§7).

## Exercises

**Core.**

1. **Null-energy structure.** Set up the $O(g)$ perturbation of $\langle T_{UU}\rangle$ from the boundary insertion $g\,\mathcal{O}_L\mathcal{O}_R$ using the bulk-to-boundary propagator; write $\int dU\,\langle T_{UU}\rangle = g\,\mathcal{I}(\Delta,\beta)$ and identify $\mathcal{I}$ as a horizon integral of the TFD two-point function.
2. **Dimension window.** Determine the operator-dimension condition under which $\mathcal{I}$ converges with the sign needed for traversability; show why irrelevant operators fail. (Compare to GJW §4 — note any `CHECK` sign you must fix.)
3. **SYK wormhole.** Write the Maldacena–Qi Hamiltonian, identify the ground-state energy's $\mu$-dependence qualitatively, and describe the open/closed phases and the $T\sim\mu$ transition.

**Starred.**

4. $\star$ **Shapiro advance.** Derive $\Delta V \propto -\int dU\,\langle T_{UU}\rangle$ by integrating the $UU$-Einstein equation across the horizon (Dray–’t Hooft shockwave); fix the orientation so ANEC gives a delay.
5. $\star$ **Teleportation count.** In the MSY picture, match the information transmitted through the wormhole to the classical bits carried by the coupling; estimate the number of qubits that can be sent in one open window $\sim\beta$.

**Project.**

6. **GJW = cocycle.** Read AQFT Sem II Block 4 (AAJ). Express the GJW deformation as a Connes-cocycle perturbation $u_t=(D\omega_g:D\omega_0)_t$ of the TFD state on the crossed-product algebra, and write a 3–4 page note connecting the bulk $O(G_N)$ opening to the algebraic $O(1/N^2)$ correction — explicitly tying into [[holographic-dual-embezzlement-protocol]] and [[crossed-product-and-island-formula]].

## Connections to other parts of the wiki

- **Within the course.** Back: [[sem2-week-12-er-epr-and-tfd]] (TFD/eternal BH), [[sem2-week-13-quantum-focusing-anec]] (ANEC). This is the last technically new topic; forward to [[sem2-week-15-panoramic-closing]] (outlook).
- **AQFT course cross-reference.** AQFT 2026 Sem II Block 4 (AAJ cocycle perturbation) is the operator-algebraic framework for the GJW deformation; the correspondence is recorded on [[crossed-product-and-island-formula]].
- **Open questions raised or motivated.** [[crossed-product-and-island-formula]] — the algebraic view of GJW; [[holographic-dual-embezzlement-protocol]] — whether the same $O(1/N^2)$ cocycle machinery controls embezzlement cost; whether the Maldacena–Qi wormhole has a clean type II interpretation.
- **Area page.** [[gauge-gravity-duality]].

---

*Notes prepared for [[courses/ads-cft-course/syllabus|the Gauge/Gravity Duality course]], Semester II Block 2. Draft (status: drafting) — pending expert review; see the `CHECK` items in §7 for the sign-convention-sensitive GJW factors that need confirmation before `final`. Last revised 2026-05-28.*
