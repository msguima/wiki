---
title: "Appendix E — Holography and Large-N Primer"
type: appendix
course: syllabus
modified: 2026-06-11
---

# Holography and Large-N Primer

> **See also.** The [[courses/2026-algebraic-qft-course/syllabus|AdS/CFT course]] is the full curriculum that this primer is the lightweight version of. Students wanting more depth on any topic in this primer should consult that course's adscft-org-crosswalk for the corresponding adscft.org reading.

This appendix collects the holographic-side prerequisites for Semester II. It is intended for a student who knows QFT and operator algebras but has limited prior exposure to AdS/CFT or large-$N$ field theory. The primer is **schematic** — for a full treatment, consult the references in §E.10.

## E.1 What Is AdS/CFT?

**Maldacena's conjecture** (1997; Maldacena, *Adv. Theor. Math. Phys.* 2 (1998) 231): a non-perturbative duality between
- **Boundary side:** a conformal field theory (CFT) in $d$ spacetime dimensions;
- **Bulk side:** a theory of quantum gravity (typically string theory) on a $(d+1)$-dimensional asymptotically AdS spacetime.

The duality is exact: every state of the boundary CFT corresponds to a state of the bulk gravity theory, and every operator on one side has a counterpart on the other.

**Working examples:**
- $\mathcal{N} = 4$ super-Yang–Mills with gauge group $\mathrm{SU}(N)$ in 4D $\leftrightarrow$ Type IIB superstring theory on $\mathrm{AdS}_5 \times S^5$.
- 2D CFTs with large central charge $\leftrightarrow$ 3D gravity (or string theory) on $\mathrm{AdS}_3$.

For the course, we use AdS/CFT as a *framework* without doing string-theory calculations; we only need the algebraic features at large $N$.

## E.2 Large-$N$ Factorization

In a $\mathrm{U}(N)$ or $\mathrm{SU}(N)$ gauge theory, **single-trace operators** are of the form $\mathcal{O}(x) = \frac{1}{N}\mathrm{Tr}(\Phi(x)^k)$ for some matrix-valued field $\Phi$ and power $k$. The $1/N$ normalization is chosen so that $\langle \mathcal{O}\,\mathcal{O}\rangle$ stays $O(1)$ at large $N$.

**Large-$N$ factorization** (a structural consequence of planarity in the diagrammatic expansion):
$$
\langle \mathcal{O}^k \rangle = \langle \mathcal{O}^2\rangle^{k/2}\cdot(\text{Wick-contraction combinatorics}) + O(1/N^2),
$$
i.e., higher correlators factorize as if $\mathcal{O}$ were a **Gaussian random variable** at leading order. The algebra of single-trace operators becomes a **generalized free field** at $N = \infty$.

## E.3 Type III$_1$ at Large $N$

The algebra of single-trace operators on a boundary subregion of a holographic CFT is, at large $N$, the algebra of a generalized free field. Under mild conditions (Liu lectures §3), this algebra is **type III$_1$** — exactly the structural feature of QFT local algebras (Week 12).

At finite $N$, the algebra is type I (the CFT has finite-dimensional Hilbert spaces if the boundary region is compact). The type III$_1$ structure emerges in the $N \to \infty$ limit and is the algebraic content of "large $N$ = classical gravity."

*Physical reading (Sem II Wk 1 §4.4):* the type I → III$_1$ degradation at $N = \infty$ is the boundary algebra registering the formation of a sharp bulk horizon — no one-sided density matrix ↔ a genuinely inaccessible interior; ADM time turning outer ↔ exterior time translation cannot cross the horizon; the intrinsic modular clock ↔ Hawking thermality. Sharp horizons are an $N = \infty$ idealization.

This is **central to the Sem II program**: Witten 2022 / CPW / AAJ all work in the type III$_1$ regime obtained at large $N$. The crossed-product construction (Block D) is then the natural framework.

## E.4 Eternal AdS Black Hole

The **maximally extended AdS-Schwarzschild geometry** has:
- Two asymptotic AdS boundaries (left $L$, right $R$);
- A bifurcation surface at the center (the horizon);
- Two interior regions (future, past) behind the horizon.

The Penrose diagram is a diamond with two asymptotic edges. The right boundary supports a CFT$_R$; the left boundary supports a CFT$_L$. The two CFTs are causally disconnected (no observer in one boundary can send a signal to the other), but the bulk geometry connects them via the wormhole.

## E.5 Maldacena's TFD Identification

**Theorem (Maldacena 2003).** The two-sided eternal AdS-Schwarzschild black hole is dual to the boundary CFT in the thermofield-double state at the Hawking inverse temperature:
$$
|\mathrm{BH}\rangle_{\mathrm{gravity}} \;\leftrightarrow\; |\mathrm{TFD}_{\beta_H}\rangle_{\mathrm{CFT}_R \otimes \mathrm{CFT}_L},
$$
with $\beta_H = 1/T_H$, $T_H$ the Hawking temperature of the BH.

This is the holographic counterpart of the Bisognano–Wichmann TFD identification (free-field Rindler-Rindler ↔ Minkowski vacuum). The bulk geometry connects two CFTs whose joint state is entangled (TFD); the "wormhole" is the geometric image of this entanglement.

## E.6 The ADM Hamiltonian as Modular Flow

In the asymptotic AdS geometry, there is a notion of **ADM Hamiltonian** $H_{\mathrm{ADM}}$ — the energy as measured at the asymptotic boundary. For the eternal BH dual to a TFD, the ADM Hamiltonian on the right boundary is $H_R$ (and on the left, $H_L$).

In the TFD vacuum (which is the bulk eternal-BH state), the modular flow on the right boundary algebra is generated by $\beta_H(H_R - H_L)$, the two-sided "boost-like" generator that respects the bifurcation horizon. At leading order in $1/N$, this equals the bulk Killing-vector flow that fixes the bifurcation surface — the **modular flow ↔ bulk Killing flow** dictionary of Liu's lectures.

## E.7 Witten 2022 in One Sentence

Witten's central observation (arXiv:2112.12828):

> In the large-$N$ limit of a holographic CFT, the boundary single-trace algebra $\mathcal{A}_R$ is type III$_1$; the modular flow of the TFD state on $\mathcal{A}_R$ is the ADM time translation; dressing $\mathcal{A}_R$ by this flow gives a **type II$_\infty$** algebra with a faithful normal semifinite trace; and the dressed entropy equals the **generalized entropy** $A_{\mathrm{horizon}}/(4G_N) + S_{\mathrm{out}}$ modulo a state-independent additive constant.

This is the Sem II Block 1 result. The Block D crossed-product machinery + the holographic dictionary together produce it.

## E.8 CPW vs. CLPW

Two distinct papers, often confused:

**CPW** (Chandrasekaran–Penington–Witten 2022, arXiv:2209.10454): "Large $N$ algebras and generalized entropy." Two-sided eternal BH; TFD vacuum; type II$_\infty$ dressing by $H_R - H_L$; dressed entropy = generalized entropy with horizon area term.

**CLPW** (Chandrasekaran–Longo–Penington–Witten 2022, arXiv:2206.10780): "An algebra of observables for de Sitter space." de Sitter static patch with an *observer*; type II$_1$ algebra (compact horizon → finite-dim Hilbert space at the algebra level); maximum-entropy state theorem.

The author lists overlap, but the physics and the algebra type are different:
- CPW: type II$_\infty$, infinite-dim Hilbert space, eternal BH.
- CLPW: type II$_1$, finite total entropy, de Sitter static patch.

The course's Sem II Block 2 is CPW; CLPW appears as a contrasting aside in Block 5 Wk 14.

## E.9 Ahmad–Jefferson (Sem II Block 4)

AAJ (arXiv:2501.01487) develops **cocycle perturbation theory** on the crossed-product algebra. Setup:

1. Start with the unperturbed TFD vacuum + dressed algebra (the CPW construction).
2. Perturb by a **Gao–Jafferis–Wall** double-trace deformation $V = g\,\mathcal{O}_L\,\mathcal{O}_R$ — a "double-sided" deformation that *traversifies* the wormhole.
3. The perturbed state $\omega_V$ is related to $\omega_0$ by the **Connes cocycle** $u_t = (D\omega_V/D\omega_0)_t$ (Week 7).
4. Compute the perturbed dressed entropy to order $g^2$. AAJ find **20 distinct corrections** at this order, some universal and some holography-specific.

AAJ's machinery is **perturbation theory on the dressed algebra**, with the cocycle as the expansion parameter. It uses every piece of Block A through D.

## E.10 Further Reading

For a complete AdS/CFT introduction:
- Aharony, Gubser, Maldacena, Ooguri, Oz, "Large N field theories, string theory and gravity," *Phys. Rep.* 323 (2000) 183.
- McGreevy, "Holographic duality with a view toward many-body physics," *Adv. High Energy Phys.* 2010, 723105.
- Harlow, "TASI Lectures on the Emergence of Bulk Physics in AdS/CFT," arXiv:1802.01040.

For the algebraic-QFT side of holography:
- **Liu**, "Lectures on entanglement, von Neumann algebras, and emergence of spacetime," arXiv:2510.07017 — *this is Sem II Block 3 connective tissue. The recommended primary text.*
- Witten, "Gravity and the crossed product," arXiv:2112.12828 §2 — large-$N$ setup.
- CPW arXiv:2209.10454 §§2–3 — two-sided large-$N$ algebra.

For the holographic entropy formula:
- Ryu & Takayanagi, "Holographic derivation of entanglement entropy from AdS/CFT," *PRL* 96 (2006) 181602.
- Lewkowycz & Maldacena, "Generalized gravitational entropy," *JHEP* 08 (2013) 090.

The full Sem II program assumes familiarity with this conceptual framework but does *not* assume the student can do explicit AdS/CFT calculations. The Block D + Bisognano–Wichmann + Week 14 dressed-entropy toolkit, plus the Liu lectures as connective tissue, is sufficient to follow Witten/CPW/AAJ.

## E.11 What's Used Where in Semester II

| Block | Setting | Key holographic input |
|---|---|---|
| 1 — Witten 2022 | one-sided BH at large $N$ | type III$_1$ at large $N$; ADM Hamiltonian as modular flow generator |
| 2 — CPW | two-sided eternal BH | TFD vacuum + $H_R - H_L$ modular flow |
| 3 — Liu lectures | structural overview | modular flow ↔ bulk Killing flow; algebraic ER=EPR |
| 4 — AAJ | perturbative corrections | Connes cocycle of GJW-deformed state |
| 5 — MSY | bulk-side complement | ANEC, Shapiro time advance, geometric backreaction |

## E.12 Honest Scoping

The course does **not** teach holographic QFT from scratch. Students who want to understand the bulk-side physics of Witten/CPW/MSY in depth should consult AdS/CFT reviews. The course's algebraic-side toolkit is the necessary preparation for *reading* these papers critically, not for *deriving* their bulk-side claims independently.

For the course's stated goal — preparing students to read the recent crossed-product / dressed-entropy literature in algebraic QFT — Block D + this primer + Sem II Block 3 (Liu) is the minimum sufficient holographic background.

**For the holographic-side curriculum proper**, see the [[courses/2026-algebraic-qft-course/syllabus|AdS/CFT course]] and its adscft-org-crosswalk.
