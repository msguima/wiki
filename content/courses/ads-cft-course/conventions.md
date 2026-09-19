---
title: "Course Conventions"
type: course-note
course: syllabus
modified: 2026-05-26
---

# Course Conventions

Canonical convention reference for the AdS/CFT course. **All skeletons, notes, and appendices follow these conventions consistently.** Where these conventions differ from adscft.org's, the difference is recorded in `appendices/adscft-org-crosswalk.md` §D.

## Units and signature

- Natural units: $\hbar = c = 1$.
- Metric signature: **mostly plus**, $(-,+,+,\ldots,+)$. This matches the AQFT course in Minkowski signature; it differs from some AdS/CFT texts (which use mostly minus). adscft.org's signature deltas are listed in the crosswalk.
- AdS radius normalised to $L = 1$ unless stated otherwise. When dimensional restoration matters, $L$ is restored explicitly.

## AdS coordinates

- **Global:** $ds^2 = L^2(-\cosh^2\rho \, d\tau^2 + d\rho^2 + \sinh^2\rho \, d\Omega_{d-1}^2)$.
- **Poincaré (Lorentzian):** $ds^2 = \frac{L^2}{z^2}(-dt^2 + d\vec{x}^2 + dz^2)$, with $z>0$ the radial direction; $z\to 0$ is the boundary.
- **Euclidean Poincaré:** $ds^2 = \frac{L^2}{z^2}(d\tau^2 + d\vec{x}^2 + dz^2)$.

The boundary is conformal $\mathbb{R}^{1,d-1}$ (Lorentzian) or $\mathbb{R}^d$ (Euclidean) at $z=0$.

## Gauge theory

- Gauge group: $\mathrm{SU}(N)$ with $N$ large unless stated.
- 't Hooft coupling: $\lambda = g_{\text{YM}}^2 N$, kept fixed in the large-$N$ limit.
- Single-trace operators: $\mathcal{O}(x) = \frac{1}{N}\mathrm{Tr}(\Phi(x)^k)$ for some adjoint scalar $\Phi$; normalisation chosen so $\langle\mathcal{O O}\rangle = O(1)$ at large $N$.

## GKP-Witten formula

The convention used throughout the course is

$$ Z_{\text{CFT}}[J] \;=\; Z_{\text{gravity}}\big[\,\phi_{\partial}(x) = J(x)\,\big] $$

with no sign in the exponent (the bulk action is the Euclidean classical action evaluated on the solution with boundary data $J$). When the operator $\mathcal{O}$ has dimension $\Delta$, the bulk field $\phi$ satisfies $m^2 L^2 = \Delta(\Delta - d)$ and the leading boundary behaviour is

$$ \phi(z, x) \sim z^{d-\Delta} J(x) + z^{\Delta} \langle \mathcal{O}(x)\rangle + \cdots \qquad (z \to 0). $$

## Entanglement entropy

- Ryu-Takayanagi: $S(A) = \frac{\text{Area}(\gamma_A)}{4 G_N}$ for $\gamma_A$ the minimal-area surface in the bulk anchored to $\partial A$ on the boundary and homologous to $A$.
- Generalised entropy: $S_{\text{gen}} = \frac{\text{Area}(\gamma)}{4 G_N} + S_{\text{bulk}}$.
- $G_N$ always denotes the bulk Newton constant.

## Modular theory (when needed)

The course uses modular theory only as a black box; for full development see the [[courses/ads-cft-course/syllabus|2026 AQFT course]]. Notation:

- $\Delta_\omega$: modular operator of state $\omega$ on a von Neumann algebra $\mathcal{M}$.
- $J_\omega$: modular conjugation.
- Modular flow: $\sigma_t(a) = \Delta_\omega^{it} a \Delta_\omega^{-it}$.

## Abbreviations

AdS, CFT, GKP-W (Gubser-Klebanov-Polyakov-Witten), RT (Ryu-Takayanagi), HRT (Hubeny-Rangamani-Takayanagi), QES (quantum extremal surface), TFD (thermofield double), JT (Jackiw-Teitelboim), SYK (Sachdev-Ye-Kitaev), ANEC (averaged null energy condition), GJW (Gao-Jafferis-Wall), AEMM (Almheiri-Engelhardt-Marolf-Maxfield).

## Weyl anomaly (2d) and the central charge

The overall sign and $2\pi$ placement of the two-dimensional trace anomaly differ across the literature. **This course fixes**
$$
\langle T^\mu{}_\mu\rangle = \frac{c}{12}\,R,
$$
with $R$ the Ricci scalar in the convention where the round sphere has $R>0$, and with $c$ normalised so that a single free boson has $c=1$.

This choice is not free: it is the one produced by the holographic derivation in [[week-09-holographic-renormalisation|Sem I Week 9]], which obtains $\langle T^\mu{}_\mu\rangle = \tfrac{c}{12}R[\gamma]$ together with the Brown–Henneaux value $c = 3L/2G_N$. [[week-04-stress-tensor-and-central-charge|Week 4]] states the same coefficient. Any note quoting a different sign is in error, not in a different convention.
