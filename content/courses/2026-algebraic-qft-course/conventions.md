---
title: "Course Conventions"
type: course-note
course: syllabus
modified: 2026-08-24
---

# Course Conventions

This is the canonical convention reference for the algebraic-QFT course. Every
formula involving modular flow, boosts, crossed products, or dressed entropy
must be read against this page. When a source uses the opposite sign, we
translate the source into the course convention before continuing.

For a comprehensive symbol table, see [[notation-and-conventions|Appendix F]].

## Spacetime and Free-Field Signs

We use the mostly-plus Minkowski metric
$$
\eta=\operatorname{diag}(-1,+1,\ldots,+1),
\qquad x^2=-(x^0)^2+|\mathbf x|^2.
$$
The Pauli--Jordan distribution is real and is defined by
$[\phi(x),\phi(y)]=i\Delta(x-y)$. Wightman functions are boundary values with
the time prescription $x^0\mapsto x^0-i\epsilon$. These three choices are a
single sign package; a source written with the opposite metric must be
translated before its formulas are imported.

**Dimension notation.** In the free-field chapters, $\mathbb R^{1,d}$ means
one time and $d$ spatial dimensions, so physical Minkowski spacetime has
$d=3$. In the holography chapters, the standard notation CFT$_d$/AdS$_{d+1}$
instead counts the boundary **spacetime** dimension. We state which convention
is active whenever the two parts of the course meet; a bare phrase such as
“for $d=4$” is not sufficient there.

## Modular Flow

The course uses the **Witten 1803.04993 §3 convention**:
$$
\boxed{\sigma_t^\omega(a) := \Delta_\omega^{-it}\, a\, \Delta_\omega^{it}.}
$$

For $\mathcal{M} = M_n(\mathbb{C})$ and $\omega_\rho(a) = \mathrm{Tr}(\rho\, a)$:
$$
\sigma_t^\rho(a) = \rho^{-it}\, a\, \rho^{it}.
$$

For a Gibbs state $\rho = e^{-\beta H}/Z$ with physical Heisenberg flow $\alpha_s(a) = e^{isH}\,a\,e^{-isH}$:
$$
\sigma_t^\rho = \alpha_{+\beta t}.
$$

**Modular time runs in the same direction as physical time**, at $\beta$-rescaled rate. This is the structural reason our convention is "natural" for thermal physics.

**Opposite convention.** Some references, including Bratteli–Robinson Vol. II,
use $\sigma_t^\omega = \mathrm{Ad}(\Delta^{+it})$, giving
$\sigma_t^\rho = \alpha_{-\beta t}$. The two conventions describe the same
automorphism group running in opposite directions; they are related by
$t\mapsto-t$. **Our convention is fixed; do not mix formulas before making
this translation.**

## KMS Convention

We use the **upper-strip $\beta > 0$** KMS condition:

A state $\omega$ is KMS at $\beta > 0$ for a one-parameter automorphism group $\sigma_t$ if for every $a, b$ there is a function $F_{a,b}$ on the closed strip $\{0 \le \mathrm{Im}\,z \le \beta\}$, holomorphic in the interior, bounded and continuous, with
$$
F_{a, b}(t) = \omega(a\,\sigma_t(b)), \qquad F_{a, b}(t + i\beta) = \omega(\sigma_t(b)\,a).
$$

**Two facts under this convention:**
1. The Gibbs state $\rho = e^{-\beta H}/Z$ with **physical Heisenberg flow** is KMS at $\beta > 0$ upper-strip (Week 4 §1.1, derived).
2. A faithful normal state $\omega$ with **its modular flow** (in our $\Delta^{-it}$ convention) is KMS at $\beta = +1$ upper-strip (Week 6 §3, model proof).

Both physical and modular flows live in the **same upper strip** in our convention — that is the pedagogical advantage.

## Rindler / Bisognano–Wichmann

For the right Rindler wedge $W_R$ in any Wightman QFT (Week 10):
$$
\Delta_{W_R} = e^{-2\pi K}, \qquad \sigma_t^{W_R}(a) = U(\Lambda^{\mathrm{boost}}(2\pi t))\, a\, U(\Lambda^{\mathrm{boost}}(2\pi t))^*.
$$
**Modular time $t$ corresponds to boost rapidity $+2\pi t$.** Unruh temperature $T_U = a/(2\pi)$.

We define the boost generator by
$$
U(\Lambda^{\mathrm{boost}}(u))=e^{iuK}.
$$
With this definition, $\Delta_{W_R}^{-it}=e^{i2\pi tK}$ and the two formulas
above agree without an additional sign. A reference using
$U(\Lambda(u))=e^{-iuK_{\rm ref}}$ is using $K_{\rm ref}=-K$.

## Crossed-Product Variables

Several real variables occur in a modular crossed product. They are related,
but they are not interchangeable.

| Symbol | Role |
|---|---|
| $t$ | modular-group parameter in $\sigma_t$ |
| $u$ | physical rapidity or physical time; for the wedge, $u=2\pi t$ |
| $q$ | coordinate on the auxiliary $L^2(\mathbb{R},dq)$ factor |
| $Q$ | multiplication by $q$: $(Q\xi)(q)=q\xi(q)$ |
| $P$ | momentum conjugate to $Q$: $P=-i\partial_q$ |
| $r$ | parameter of the dual action $\theta_r$ |

In the covariant representation,
$$
(\pi_\sigma(a)\xi)(q)=\sigma_{-q}(a)\xi(q),\qquad
(\lambda(t)\xi)(q)=\xi(q-t),\qquad
\lambda(t)=e^{-itP}.
$$
The covariance relation is
$$
\lambda(t)\pi_\sigma(a)\lambda(t)^*=\pi_\sigma(\sigma_t(a)).
$$
The dual action is implemented by $e^{irQ}$:
$$
\theta_r(\pi_\sigma(a))=\pi_\sigma(a),\qquad
\theta_r(\lambda(t))=e^{irt}\lambda(t).
$$
Thus the dual action is a phase in the $q$-representation and a translation
in the Fourier-dual $p$-representation. A function of $P$ is not a
multiplication function of $q$. Whenever we Fourier transform, we name the
new variable $p$ and state the transformation explicitly.

The canonical trace on the continuous core is normalized so that
$$
\hat\tau\circ\theta_r=e^{-r}\hat\tau.
$$
In a Fourier realization this scaling may be represented by a weight
$e^{-p}\,dp$. If one instead uses a rapidity-normalized variable
$p=2\pi q_{\rm rap}$, the same weight is proportional to
$e^{-2\pi q_{\rm rap}}dq_{\rm rap}$. The factor $2\pi$ is therefore a change
of variable, not a second trace convention.

## Modular Boundary Term

In a type-I representation, for two states $\omega, \phi$ with density matrices and with modular Hamiltonian $K_\phi = -\log\rho_\phi$ of the **reference** state $\phi$, the **modular boundary term** is
$$
\mathcal{B}(\omega, \phi) := \omega(K_\phi) - \phi(K_\phi) = \mathrm{Tr}((\rho_\omega - \rho_\phi)\,K_\phi).
$$

**Note:** uses $K_\phi$ (the second argument's modular Hamiltonian), not $K_\omega$. This is the relative modular energy of $\omega$ measured by the reference flow $\sigma^\phi$.

Vanishes when $\omega = \phi$.

## Entropy and Trace Normalization

Let $\hat\omega(x)=\hat\tau(hx)$ be a normalized state on a semifinite
algebra. If the trace is rescaled to $\hat\tau'=c\hat\tau$, the density becomes
$h'=h/c$, and hence
$$
S_{\hat\tau'}(\hat\omega)=S_{\hat\tau}(\hat\omega)+\log c.
$$
Only differences computed with the same trace normalization are invariant.

For the type-I model
$$
\hat\tau(a\otimes f)=\operatorname{Tr}(a)\int_{\mathbb R}f(p)e^{-p}dp
$$
and a product state with system density $\rho$ and clock probability density
$\mu(p)$, the density relative to $\hat\tau$ is
$h(p)=\rho\,\mu(p)e^p$. Its entropy is
$$
S_{\hat\tau}(\rho\otimes\mu)
=S(\rho)-\int\mu(p)\log\mu(p)\,dp-\int p\,\mu(p)\,dp.
$$
The final term is the clock-energy term induced by the non-flat trace. It must
not be dropped or renamed as a Shannon entropy.

## Entropy-Difference Identity

Let $D_\omega$ and $D_\phi$ be normalized trace-densities in the **same**
semifinite algebra with respect to the **same** faithful normal semifinite
trace $\hat\tau$, and set $K_\phi=-\log D_\phi$. Whenever the displayed terms
are well defined (or after a stated common regularization), the exact
same-algebra identity is
$$
\boxed{
S_{\hat\tau}(D_\omega)-S_{\hat\tau}(D_\phi)
=-D_{\hat\tau}(D_\omega\|D_\phi)
+\hat\tau\!\left[(D_\omega-D_\phi)K_\phi\right],
}
$$
where
$D_{\hat\tau}(D_\omega\|D_\phi)
=\hat\tau[D_\omega(\log D_\omega-\log D_\phi)]$.

In finite dimensions this becomes
$$
S(\rho_\omega)-S(\rho_\phi)
=-S(\rho_\omega\|\rho_\phi)+\mathcal B(\omega,\phi),
$$
with $\mathcal B$ as above. Week 14 proves the algebraic identity directly
and checks it in the type-I Fourier model.

Relating $D_{\hat\tau}(D_\omega\|D_\phi)$ on a continuous core to Araki
relative entropy of states on the original type-III algebra requires more
data: a fixed core, a fixed trace normalization, and a specified lift of both
states. Witten and CPW construct such data in their respective large-$N$
settings. We do not promote that **lift** to a theorem for arbitrary pairs of
type-III states without these hypotheses.

## Proof-Status Labels

Every theorem-level claim should carry one of these labels in the prose:

- **Proved.** Full proof is included.
- **Model proof.** Proved in finite dimensions, type I, or another controlled case.
- **Sketched.** Main ideas only; missing analytic details are named.
- **Stated only — refs.** Used as a theorem from the literature; reference given.
- **Hypothesis-explicit.** Stated with the technical assumptions required, even if the proof is in references.
- **Heuristic.** Physical or conceptual motivation, not a proof.
- **Exact calculation.** An exact computation inside the explicitly defined model.
- **Controlled perturbative.** Derived through the stated order in a named expansion parameter.
- **Formal analogy.** A structural comparison, not an equality or derivation.
- **Example-only.** Demonstrated in one model; not claimed generally.

## Scope Discipline

The course must not blur:

- **Type-I density-matrix calculations** with **type-III local-algebra facts**.
- **Wedge-specific Bisognano–Wichmann geometry** with **generic bounded-region modular flow** (which is *not* geometric).
- **Structural Bell-correlation theorems** (Summers–Werner, hypothesis-explicit) with **explicit Weyl-test-function computations** (which approach but don't attain $2\sqrt 2$).
- **Proved operator-algebra statements** (Connes–Takesaki) with **holographic or gravitational interpretation** (Witten 2022 identification).
- The **clock coordinate**, its **conjugate momentum**, the **modular
  parameter**, and the **Fourier-dual variable**.
- The **clock wavefunction width** with a **matter UV cutoff**. The crossed
  product gives a semifinite trace and can support finite entropy differences
  under explicit integrability hypotheses; it does not derive a QFT area-law
  coefficient from clock localization.

## Common Errors to Avoid

1. **Type III$_1$ ≠ Powers III$_\lambda$ at $\lambda = 1$.** The tracial endpoint of the Powers family is type II$_1$, not type III$_1$. III$_1$ is a separate Connes class with full positive S-invariant $[0, \infty)$. Week 12 gives the hypothesis-sensitive AQFT route to the hyperfinite III$_1$ result; no single condition such as split or nuclearity is treated as sufficient by itself.

2. **Type III$_1$ universality is NOT due to Haag–Hugenholtz–Winnink.** HHW 1967 is about KMS/equilibrium states, not local-algebra classification. The correct citation chain is Driessler 1975/77 / Fredenhagen 1985 / Buchholz–Wichmann 1986 / Buchholz–D'Antoni–Fredenhagen 1987, plus Connes 1976 + Haagerup 1987 for operator-algebra uniqueness.

3. **Tomita–Takesaki does NOT produce a state.** Given a faithful normal state $\omega$ on $\mathcal{M}$ (equivalently, a cyclic-separating vector in a standard representation), Tomita–Takesaki produces the state's canonical modular flow $\sigma^\omega_t$, and $\omega$ is KMS for that flow at $\beta = 1$. The state is *input*, not output.

4. **Murray–vN equivalence of projections is INTERNAL to the algebra.** A non-tracial vector state cannot certify or rule out Murray–vN equivalence. Use a partial isometry $u \in \mathcal{M}$, not a state expectation.

5. **The crossed product is NOT by itself the gravitational dressing.** The
   crossed product is an operator-algebraic construction (Block D, Week 13).
   Witten and CPW identify a crossed-product algebra with a gravitationally
   dressed observable algebra in their stated large-$N$ regimes, after adding
   the appropriate energy variable and gravitational constraints. That
   identification is a source-specific physical result with perturbative and
   holographic hypotheses, not a consequence of the abstract continuous-core
   theorem.

6. **Tensor-product factorization does NOT hold for AQFT bounded local algebras.** Type III$_1$ algebras do not split $\mathcal{H} = \mathcal{H}(\mathcal{O}) \otimes \mathcal{H}(\mathcal{O}')$. Tensor reasoning is valid only under the split property (Doplicher–Longo) or in type-I regulators.

7. **A shared clock unitary is not central.** In a crossed product,
   $\lambda(t)$ implements a nontrivial automorphism and therefore does not
   commute with the represented original algebra. Two commuting dressed
   algebras cannot both be generated by the same noncentral $\lambda(t)$ in
   the naive way; the commutant construction must be used.

8. **Type II$_1$ is not finite-dimensional.** A II$_1$ factor has a finite
   normalized trace but is generally infinite-dimensional. In the de Sitter
   construction, the finite trace follows from the observer-clock spectral
   restriction, not from replacing QFT by a finite-dimensional Hilbert space.
