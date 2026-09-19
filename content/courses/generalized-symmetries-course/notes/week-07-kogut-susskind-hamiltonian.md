---
title: "Week 7 — Kogut–Susskind: the Hamiltonian Lattice"
type: lecture-notes
course: syllabus
semester: 1
week: 7
block: B
duration: 4 hours (2 lectures × 2 hours)
prerequisites: Weeks 1–6; canonical quantization; the quantum rotor; angular momentum
modified: 2026-07-01
---

# Week 7 — Kogut–Susskind: the Hamiltonian Lattice

> *So far the lattice has been a Euclidean path integral. Now we pass to the Hamiltonian, where the physics is transparent: link variables are quantum rotors, the electric field is their angular momentum, the Gauss law is an operator constraint, and physical states are closed electric strings. Confinement becomes the statement that a string costs energy proportional to its length. And the simplest case — ℤ₂ — is the toric code, sitting here one renaming away, planted for Semester II.*

## 0. Reading

**Primary:** Kogut & Susskind, *Phys. Rev. D* 11 (1975) 395 — the founding paper. Kogut, *Rev. Mod. Phys.* 51 (1979) 659, §IX (the Hamiltonian formulation).

**Secondary:**
- Fradkin, *Field Theories of Condensed Matter Physics*, 2nd ed., ch. 9 — the ℤ₂ Hamiltonian and its duality to the transverse-field Ising model.
- Kogut, *Rev. Mod. Phys.* 55 (1983) 775 — the "lattice methods" review; strong-coupling spectroscopy.

**Proof-status labels** as in [[week-01-compact-variables-xy-model|Week 1]]. The ℤ₂ Hamiltonian of §4 is revisited as the toric code in Semester II (Block 3).

## 1. From transfer matrix to Hamiltonian

Make the lattice **anisotropic**: keep the spatial spacing $a$ but let the temporal spacing $a_t \to 0$. The Euclidean transfer matrix $T$ along the time direction then approaches $T \approx e^{-a_t H}$, defining a **Hamiltonian** $H$ that acts on the Hilbert space of a fixed time slice. On each spatial link lives a variable $U_\ell \in G$; the Hilbert space is $\bigotimes_\ell L^2(G)$ (square-integrable functions on the group per link). Taking the limit carefully (Problem 1) yields the **Kogut–Susskind Hamiltonian**
$$
\boxed{\ H = \frac{g^2}{2}\sum_\ell E_\ell^2 \;-\; \frac{1}{g^2}\sum_P \big(U_P + U_P^\dagger\big).\ }
$$
The first (**electric**) term is diagonal in the flux basis; the second (**magnetic**) term is the plaquette holonomy, which *hops* flux. The coupling $g$ plays the role of $1/\sqrt\beta$: strong coupling $g\to\infty$ suppresses the magnetic term.

### 1.1 The electric field as angular momentum

$E_\ell$ is the generator of left (or right) group rotations of $U_\ell$ — the **conjugate momentum** to the link variable. For $U(1)$, write $U_\ell = e^{i\theta_\ell}$; then $E_\ell = -i\,\partial/\partial\theta_\ell$ with
$$
[\theta_\ell, E_{\ell'}] = i\,\delta_{\ell\ell'},\qquad E_\ell \in \mathbb{Z},
$$
so the electric field has **integer eigenvalues** — quantized electric flux along the link. The states $|E_\ell = n\rangle = e^{in\theta_\ell}$ are the flux eigenstates; $U_\ell$ raises the flux by one, $E_\ell \to E_\ell + 1$. For $SU(N)$, $E_\ell^2$ is the quadratic Casimir and the flux carries a representation label.

## 2. The Gauss law

### 2.1 The constraint [Computed.]

Gauge transformations act at sites; their generator is the **lattice divergence of the electric field**,
$$
G_x = \sum_{\ell\,\ni\, x} \pm E_\ell = (\delta E)_x ,
$$
(the signs orient flux out of $x$). One checks $[G_x, H] = 0$: the Hamiltonian is gauge-invariant. The physical Hilbert space is defined by imposing the **Gauss law** as a constraint,
$$
G_x\,|\psi\rangle = q_x\,|\psi\rangle,
$$
with $q_x$ the static charge at $x$. In the **pure gauge theory** (no matter) $q_x = 0$: the electric flux is **divergence-free at every site**. A divergence-free integer flux is a union of **closed electric strings**. Physical states are superpositions of closed flux loops.

> **Physical picture.** The Gauss law is not an equation of motion here — it is the definition of "physical." It says the only allowed field configurations are those with no loose ends of electric flux (absent charges). This is the operator content of "$\nabla\cdot E = \rho$": flux lines begin and end only on charges, and with no charges they close up. Everything about confinement is downstream of this: a quark and an antiquark are the two ends a flux string is *forced* to connect.

### 2.2 Electric strings and the strong-coupling vacuum

At strong coupling ($g$ large) the electric term dominates. Its ground state is the **no-flux** state $E_\ell = 0$ on every link — the unique gauge-invariant state with minimal electric energy. Excitations are closed loops of unit flux; by the electric term each unit of flux on a link costs $g^2/2$, so a loop of length $L$ costs
$$
\Delta E \simeq \frac{g^2}{2}\, L .
$$
This is the Hamiltonian face of confinement.

## 3. Confinement and the glueball [Computed.]

**Static quark–antiquark.** Insert charges $q_x = +1$, $q_y = -1$ at separation $R$. The Gauss law now *requires* a flux string running from $x$ to $y$. Its minimal length is $R$, so the ground-state energy is
$$
V(R) \simeq \frac{g^2}{2}\, R = \sigma_{\text{str}}\, R,\qquad \sigma_{\text{str}} \simeq \frac{g^2}{2},
$$
a **linear confining potential**, matching the Euclidean area law of [[week-06-wilson-action-strong-coupling|Week 6]] ($\sigma_{\text{str}} = -\ln\tilde c_f \sim -\ln(1/g^2)$ up to the change of variables $\beta \leftrightarrow 1/g^2$).

**Glueball.** The lightest gauge-invariant excitation of the vacuum is the **smallest closed flux loop** — a single plaquette's worth of flux, energy $\simeq 4\cdot\frac{g^2}{2} = 2g^2$ for a unit square, corrected by the magnetic term which lets the loop hop and lowers its energy (degenerate perturbation theory in $1/g^2$; Problem 2). The glueball mass gap is the strong-coupling statement that pure gauge theory is gapped.

## 4. The ℤ₂ case is the toric code

Specialize to $G = \mathbb{Z}_2$. Link variables are qubits; write $\sigma^z_\ell$ for the ℤ₂ "$U_\ell$" and $\sigma^x_\ell$ for the flux-raising operator. The Kogut–Susskind Hamiltonian becomes
$$
H = -\Gamma\sum_\ell \sigma^x_\ell \;-\; \frac{1}{\Gamma}\sum_P \prod_{\ell\in\partial P}\sigma^z_\ell ,
$$
with the Gauss-law constraint
$$
A_v \equiv \prod_{\ell\,\ni\, v}\sigma^x_\ell = +1 \quad\text{on physical states}.
$$
Now enforce the Gauss law **energetically** rather than as a hard constraint — add $-\sum_v A_v$ to the Hamiltonian (equivalently, work at the soluble point where the electric term reorganizes into the star operator). The result is
$$
\boxed{\ H_{\text{toric}} = -\sum_v A_v - \sum_P B_P,\qquad A_v = \prod_{\ell\ni v}\sigma^x_\ell,\quad B_P = \prod_{\ell\in\partial P}\sigma^z_\ell.\ }
$$
This is **Kitaev's toric code**. Its ground state is the deconfined phase of ℤ₂ gauge theory — the equal-weight superposition of all closed electric-flux loops (the Gauss law made into an energetic projector). Everything about it — the $2^{2g}$ ground-state degeneracy on genus $g$, the $e$ and $m$ anyons, topological entanglement entropy — is solved in Semester II (Block 3, Week 8). It is here already, as the ℤ₂ Kogut–Susskind Hamiltonian; we have simply not yet learned to read it.

> **Physical picture.** The toric code is not an exotic import from quantum information — it is the oldest object in this course, the ℤ₂ lattice gauge theory, written in the Hamiltonian at its soluble point. $A_v = 1$ is the Gauss law (closed strings); $B_P$ is the magnetic energy. The "electric charges" $e$ are the Gauss-law violations (string endpoints), the "magnetic fluxes" $m$ are the plaquette violations (frustrated $B_P$). Confinement/deconfinement of the gauge theory *is* the condensation of these anyons. Semester II will say all of this in the language of 1-form symmetry; the object it says it about is on this page.

## 5. The one-plaquette universe [Computed.]

The smallest nontrivial system — a single plaquette, gauge-fixed to one dynamical angle $\theta$ — is exactly solvable and shows the strong/weak crossover cleanly. For $U(1)$,
$$
H = \frac{g^2}{2}\,\Big(\!-\partial_\theta^2\Big) - \frac{2}{g^2}\cos\theta,
$$
a quantum rotor in a cosine potential — the **Mathieu equation**.
- **Strong coupling** ($g$ large): the potential is negligible; eigenstates are flux states $e^{in\theta}$ with $E_n = g^2 n^2/2$ — an electric-flux ladder.
- **Weak coupling** ($g$ small): expand the cosine around $\theta = 0$; a harmonic oscillator with $E_n \simeq (n+\tfrac12)\omega$, $\omega = 2/g$ — magnetic (photon-like) excitations.
The exact Mathieu spectrum interpolates, with a smooth crossover between the electric and magnetic descriptions (Problem 3). The ℤ₂ one-plaquette universe is a two-level system, solved in one line.

## 6. What to take away

1. **The Hamiltonian lattice is transparent.** $H = \frac{g^2}{2}\sum E^2 - \frac{1}{g^2}\sum(U_P + U_P^\dagger)$: electric energy (diagonal in flux) versus magnetic hopping.
2. **The Gauss law defines "physical."** $G_x = (\delta E)_x = q_x$; pure gauge theory has divergence-free flux — closed electric strings.
3. **Confinement is a string tension.** A charge pair is joined by a flux string costing $\frac{g^2}{2}R$; the glueball is the smallest closed loop.
4. **ℤ₂ Kogut–Susskind is the toric code.** With the Gauss law enforced energetically, $H = -\sum A_v - \sum B_P$ — the deconfined phase is a topologically ordered ground state we solve in Semester II.

## 7. Looking ahead: Week 8

Week 8 is the midterm, and then the last piece of Block B: **dual variables** for abelian gauge theories. We Poisson-resum the Villain $U(1)$ gauge action and find where the monopoles live — points (instantons) in $d=3$, worldlines in $d=4$. That single dimensional fact organizes Block C: the 3d monopole plasma gives Polyakov's confinement (Weeks 9–10), the 4d monopole loops give the dual superconductor (Week 11).

## 8. Problem set

**Core problems** (everyone).

**1. From transfer matrix to $H_{KS}$.**
Take the anisotropic (time-continuum) limit of the Wilson transfer matrix and derive $H = \frac{g^2}{2}\sum E_\ell^2 - \frac{1}{g^2}\sum_P(U_P + U_P^\dagger)$, tracking how $g$ relates to the space/time couplings. Where does the electric term come from?

**2. Strong-coupling spectroscopy.**
(a) Compute the static potential $V(R) = \frac{g^2}{2}R$ from the minimal flux string and identify $\sigma_{\text{str}}$.
(b) Compute the glueball mass to leading order in $1/g^2$, including the magnetic-term hopping that lets the unit loop delocalize (degenerate perturbation theory).

**3. The one-plaquette universe.**
(a) For $U(1)$, write the Mathieu Hamiltonian and give the strong- and weak-coupling spectra.
(b) For ℤ₂, diagonalize the two-level Hamiltonian exactly and plot the gap versus $\Gamma$; identify the self-dual point.

**Starred problems.**

**4⋆. ℤ₂ gauge theory ↔ transverse-field Ising (2+1d).**
Show that the (2+1)d ℤ₂ Kogut–Susskind Hamiltonian is dual to the (2+1)d transverse-field Ising model (Fradkin–Susskind). Map confinement/deconfinement of the gauge theory to disorder/order of the Ising spins, and the 't Hooft loop to the Ising order parameter. (This is the Hamiltonian face of Wegner's Euclidean duality, Week 5.)

**5⋆. The toric code from the Gauss law.**
Starting from the ℤ₂ Kogut–Susskind Hamiltonian with the hard Gauss-law constraint $A_v = 1$, show that enforcing the constraint energetically ($-\sum_v A_v$) yields $H = -\sum_v A_v - \sum_P B_P$, that $[A_v, B_P] = 0$, and that the ground state is the equal-weight sum over closed loops. Count the ground-state degeneracy on $T^2$. (Full anyon analysis: Semester II Week 8.)

**6⋆⋆ (optional).**
For $SU(2)$, compute the strong-coupling spectrum of the flux on a single link ($E^2 = $ Casimir $= j(j+1)$) and the leading glueball mass. Compare the pattern of low-lying states to the $U(1)$ and ℤ₂ cases and comment on how the non-abelian flux "thickness" differs.

---

*Notes prepared for the [[courses/generalized-symmetries-course/syllabus|generalized-symmetries course]], Semester I Block B. Last revised 2026-07-01.*
