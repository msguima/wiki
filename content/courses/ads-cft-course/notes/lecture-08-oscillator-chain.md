---
title: "Lecture 8 — A field approached through coupled oscillators"
type: lecture-notes
edition: "2.2 — rewritten at the AQFT standard"
lecture: 8
semester: 1
week: 6
hours: 4
prerequisites: "Lectures 1, 3 and 4; normal modes, the harmonic oscillator and Gaussian integrals"
status: "rewritten 2026-09-30, pending instructor review; exact Gaussian calculations and a reproducible lattice experiment, with the corner-transfer-matrix spectrum and the infrared term stated with sources"
modified: 2026-09-30
---

# Lecture 8 — A field approached through coupled oscillators

> *A chain of coupled harmonic oscillators is the simplest system in which the ground state of a local Hamiltonian is entangled across a spatial cut, and in which the number of degrees of freedom near the cut grows as the resolution improves. We develop the Gaussian formalism completely. For two oscillators the reduced state is obtained twice, from the wavefunction and from the covariance matrix, and it turns out to be exactly thermal for an oscillator that appears nowhere in the Hamiltonian. For many oscillators Williamson's normal form reduces every regional state to independent thermal modes, and the modular Hamiltonian becomes an explicit quadratic form. A lattice experiment then separates what depends on the regulator from what does not: at fixed physical size the entropy of an interval grows as $\frac13\log(1/a)$, while the mutual information of two separated intervals converges. The first fact is why Lecture 9 gives up regional density matrices; the second anticipates the split property. The modular spectrum of a half-chain, a ladder whose spacing closes as $a\to0$, anticipates the boost of Lecture 10.*

## How to use this lecture

**Classroom core, two meetings of two hours.** The first meeting covers the motivation (§1, 10 minutes), two oscillators by the wavefunction (§2, 40 minutes) and by the covariance matrix (§3, 25 minutes), and the ground state of many oscillators with Williamson's normal form (§§4.1–4.2, 35 minutes), leaving 10 minutes for Checkpoint 1. The second meeting covers the entropy and the modular Hamiltonian of a Gaussian state (§4.3, 15 minutes), the lattice field and its continuum limit (§§5.1–5.2, 25 minutes), the lattice experiment (§6, 40 minutes), and the scope of the result (§8, 10 minutes), with 30 minutes for Problems 3 and 4; Problems 1, 2, 5 and 6 complete the core assignment. These allocations are proposals and have not been tested in class.

**Self-study.** The zero mode and the infrared (§5.3), the half-chain and its modular ladder (§7), and Problems 7–12, including the entropy per endpoint from the corner-transfer-matrix spectrum.

**Research extension.** The lattice modular Hamiltonian near a cut, the mutual information as the gap closes, and the area law of a sphere, in Problems 13–15; Lecture 10 compares the lattice modular Hamiltonian with the continuum boost.

**Prerequisites.** Lecture 1 for restricted access, Lecture 3 for modular Hamiltonians and flows, Lecture 4 for entropy. Normal modes, the harmonic oscillator and Gaussian integrals.

**What this lecture establishes.** The reduced state of two oscillators and the entropy of a Gaussian regional state are exact calculations; Williamson's normal form is proved for covariances without position–momentum correlations, which is the case of every ground state below. The lattice entropies of §6 are numerical results in an explicitly defined model, reproducible from the page. The two-dimensional conformal result $\frac c3\log(\ell/a)$ and the corner-transfer-matrix spectrum of the half-chain are stated with sources; the entropy per endpoint is then derived from that spectrum.

## 0. Reading

**Primary.**

- M. Srednicki, [Entropy and Area](https://arxiv.org/abs/hep-th/9303048) (1993). The two-oscillator example of §2 is his.
- H. Casini, M. Huerta, [Entanglement entropy in free quantum field theory](https://arxiv.org/abs/0905.2562) (2009), the lattice formulas for Gaussian states and the two-dimensional results.
- I. Peschel, V. Eisler, [Reduced density matrices and entanglement entropy in free lattice models](https://arxiv.org/abs/0906.1663) (2009).

**Secondary.**

- L. Bombelli, R. K. Koul, J. Lee, R. D. Sorkin, Quantum source of entropy for black holes, *Phys. Rev. D* 34 (1986) 373.
- C. Holzhey, F. Larsen, F. Wilczek, [Geometric and Renormalized Entropy in Conformal Field Theory](https://arxiv.org/abs/hep-th/9403108) (1994), and P. Calabrese, J. Cardy, [Entanglement entropy and quantum field theory](https://arxiv.org/abs/hep-th/0405152) (2004).
- C. Weedbrook, S. Pirandola, R. García-Patrón, N. J. Cerf, T. C. Ralph, J. H. Shapiro, S. Lloyd, [Gaussian Quantum Information](https://arxiv.org/abs/1110.3234) (2011), for Williamson's theorem and symplectic eigenvalues.
- K. Audenaert, J. Eisert, M. B. Plenio, R. F. Werner, [Entanglement Properties of the Harmonic Chain](https://arxiv.org/abs/quant-ph/0205025) (2002).

**Optional research reading.**

- I. Peschel, M.-C. Chung, [Density Matrices for a Chain of Oscillators](https://arxiv.org/abs/cond-mat/9906224) (1999), and I. Peschel, M. Kaulke, Ö. Legeza, [Density-matrix spectra for integrable models](https://arxiv.org/abs/cond-mat/9810174) (1998).
- H. Casini, M. Huerta, [Entanglement and alpha entropies for a massive scalar field in two dimensions](https://arxiv.org/abs/cond-mat/0511014) (2005).
- J. Eisert, M. Cramer, M. B. Plenio, [Area laws for the entanglement entropy — a review](https://arxiv.org/abs/0808.3773) (2008).
- V. Eisler, G. Di Giulio, E. Tonni, I. Peschel, [Entanglement Hamiltonians for non-critical quantum chains](https://arxiv.org/abs/2007.01804) (2020), and G. Di Giulio, E. Tonni, [On entanglement hamiltonians of an interval in massless harmonic chains](https://arxiv.org/abs/1911.07188) (2019).

## 1. Entropy behind a surface

In 1986 Bombelli, Koul, Lee and Sorkin asked whether the entropy of a black hole could be the entropy of quantum fields hidden behind its horizon. They took the vacuum of a free scalar field, traced out the field inside a sphere, and found an entropy proportional to the area of the sphere, with a coefficient set by the short-distance cutoff. Srednicki returned to the question in 1993, discretizing the field on radial shells, which turns it into a set of coupled harmonic oscillators, and evaluating the entropy numerically; his paper opens with the example of two oscillators that we work out in §2. The following year Holzhey, Larsen and Wilczek obtained the entropy of an interval in a two-dimensional conformal field theory, $\frac c3\log(\ell/a)$, and in 2004 Calabrese and Cardy rederived it with the replica trick and showed that in a massive theory it saturates at $\frac c3\log(\xi/a)$, with $\xi$ the correlation length.

A second line of work came from condensed matter, where the density-matrix renormalization group keeps the largest eigenvalues of reduced density matrices and the spectrum of those matrices became a practical question. Peschel and his collaborators showed that for free lattice models the reduced density matrix of half a chain is the exponential of a quadratic operator, and that its spectrum follows from Baxter's corner transfer matrices of an associated two-dimensional model, a result we use in §7.

For this course the chain answers a question left by the finite codes of Lectures 1–7. Dividing three qutrits into shares is unambiguous, so why does dividing a quantum field into spatial regions require more care? The chain lets us perform the experiment with quantum mechanics alone: we fix a region of physical size, refine the lattice, and watch which quantities change. Three results of this lecture are used later. The entropy of a region diverges as the lattice spacing goes to zero, which motivates the algebraic description of Lecture 9. The mutual information of separated regions converges, which is the lattice shadow of the split property of the same lecture. And the modular Hamiltonian of a half-chain has a spectrum that becomes continuous in the limit, in the way the boost generator of Lecture 10 requires.

## 2. Two oscillators: the reduced wavefunction

Set $\hbar=1$ and take unit masses. Consider

$$
H=\frac12(p_1^2+p_2^2)+\frac{\omega_0^2}{2}(q_1^2+q_2^2)+\frac\kappa2(q_1-q_2)^2,
\qquad [q_i,p_j]=i\delta_{ij},
$$

with $\omega_0>0$ and $\kappa\geq0$. The normal coordinates $q_\pm=(q_1\pm q_2)/\sqrt2$, and similarly $p_\pm$, preserve the commutators and decouple the Hamiltonian into two oscillators of frequencies

$$
\omega_+=\omega_0,\qquad \omega_-=\sqrt{\omega_0^2+2\kappa}.
$$

The ground state is the product of the two normal-mode ground states,

$$
\psi_0(q_1,q_2)=\left(\frac{\omega_+\omega_-}{\pi^2}\right)^{1/4}
\exp\left[-\frac12\left(\omega_+q_+^2+\omega_-q_-^2\right)\right],
$$

and in the site variables the exponent reads $-\frac14(\omega_++\omega_-)(q_1^2+q_2^2)-\frac12(\omega_+-\omega_-)q_1q_2$. The state factorizes between the normal modes and is entangled between the sites whenever $\kappa>0$. This is the distinction we met in Lecture 2 between the physical shares and the logical variables of a code.

An observer with access to site 1 alone sees the reduced density matrix. Its kernel is a Gaussian integral over the second site,

$$
\rho_1(q,q')=\int dq_2\,\psi_0(q,q_2)\,\psi_0(q',q_2)
=\sqrt{\frac{A-B}{\pi}}\,
\exp\left[-\frac A2\left(q^2+q'^2\right)+Bqq'\right],
$$

where

$$
A=\frac{\omega_+^2+6\omega_+\omega_-+\omega_-^2}{4(\omega_++\omega_-)},
\qquad
B=\frac{(\omega_+-\omega_-)^2}{4(\omega_++\omega_-)}.
$$

To obtain them, complete the square in $q_2$: the integral of $\exp[-\alpha q_2^2-\beta q_2]$ with $\alpha=\frac12(\omega_++\omega_-)$ and $\beta=\frac12(\omega_+-\omega_-)(q+q')$ gives $\sqrt{\pi/\alpha}\,e^{\beta^2/4\alpha}$, and the term $\beta^2/4\alpha$ produces both the cross term and the reduction of the diagonal coefficient. Note that $A-B=2\omega_+\omega_-/(\omega_++\omega_-)$, which fixes the normalization $\int dq\,\rho_1(q,q)=1$.

The kernel has the form of a thermal density matrix. For an oscillator $H_\Omega=\frac12p^2+\frac12\Omega^2q^2$, Mehler's formula gives

$$
\langle q|e^{-\beta H_\Omega}|q'\rangle=\sqrt{\frac{\Omega}{2\pi\sinh\beta\Omega}}\,
\exp\left\{-\frac{\Omega}{2\sinh\beta\Omega}\left[(q^2+q'^2)\cosh\beta\Omega-2qq'\right]\right\}.
$$

Matching the two exponents requires $A=\Omega\coth\varepsilon$ and $B=\Omega/\sinh\varepsilon$, with $\varepsilon=\beta\Omega$. Therefore $\Omega^2=A^2-B^2=(A-B)(A+B)$, and a short computation gives

$$
\Omega=\sqrt{\omega_+\omega_-},
\qquad
\xi:=e^{-\varepsilon}=\frac{B}{A+\Omega}
=\left(\frac{\sqrt{\omega_+}-\sqrt{\omega_-}}{\sqrt{\omega_+}+\sqrt{\omega_-}}\right)^2.
$$

For the last step write $s=\sqrt{\omega_+}$ and $t=\sqrt{\omega_-}$; then $4(s^2+t^2)(A+\Omega)=s^4+6s^2t^2+t^4+4st(s^2+t^2)=(s+t)^4$, while $4(s^2+t^2)B=(s^2-t^2)^2$.

Thus the reduced state is exactly thermal,

$$
\rho_1=(1-\xi)\sum_{n=0}^\infty\xi^n\,|n_\Omega\rangle\langle n_\Omega|,
\qquad
K_1=-\log\rho_1=\frac{\varepsilon}{\Omega}H_\Omega-\frac\varepsilon2-\log(1-\xi),
$$

where $|n_\Omega\rangle$ are the number states of the oscillator of frequency $\Omega$. Its entropy is

$$
S_1=-\log(1-\xi)-\frac{\xi}{1-\xi}\log\xi .
$$

For $\omega_-/\omega_+=4$ we obtain $\xi=1/9$ and $S_1=\log\frac98+\frac18\log9\approx0.3924$.

> **Physical picture: thermal for a Hamiltonian nobody wrote down.** The oscillator that diagonalizes $\rho_1$ has frequency $\sqrt{\omega_+\omega_-}$, the geometric mean of the normal modes. The Hamiltonian of site 1 by itself, $\frac12p_1^2+\frac12(\omega_0^2+\kappa)q_1^2$, has frequency $\sqrt{\omega_0^2+\kappa}$, and the two agree only to first order in $\kappa$. The effective temperature $\Omega/\varepsilon$ also depends on the coupling. What is exact is the statement about the modular Hamiltonian $K_1$: the restricted pure state is a Gibbs state of $K_1$ at unit temperature. Whether $K_1$ is proportional to a physical Hamiltonian is a separate question, and in Lecture 10 the answer for a relativistic wedge will be yes, with a boost in the role of $K_1$.

## 3. Two oscillators: the covariance matrix

The same result follows from second moments alone, and this second route is the one that generalizes. Since $\langle q_\pm^2\rangle=1/(2\omega_\pm)$ and $\langle p_\pm^2\rangle=\omega_\pm/2$, the covariance of site 1 is

$$
X=\langle q_1^2\rangle=\frac14\left(\frac1{\omega_+}+\frac1{\omega_-}\right),
\qquad
P=\langle p_1^2\rangle=\frac14(\omega_++\omega_-),
\qquad
\frac12\langle q_1p_1+p_1q_1\rangle=0 .
$$

A Gaussian state is fixed by its first and second moments, so these three numbers determine $\rho_1$. The canonical rescaling $Q=(P/X)^{1/4}q_1$, $\Pi=(X/P)^{1/4}p_1$ preserves $[Q,\Pi]=i$ and makes both variances equal to

$$
\nu=\sqrt{XP}=\frac{\omega_++\omega_-}{4\sqrt{\omega_+\omega_-}} .
$$

Note that $(P/X)^{1/2}=\sqrt{\omega_+\omega_-}=\Omega$: the rescaling turns $q_1$ into the coordinate of the oscillator found in §2. A thermal oscillator with mean occupation $\bar n$ has $\langle Q^2\rangle=\langle\Pi^2\rangle=\bar n+\frac12$. Therefore $\bar n=\nu-\frac12$, and $\xi=\bar n/(\bar n+1)=(\nu-\frac12)/(\nu+\frac12)$. With $r=\omega_-/\omega_+$ we have $\nu=\frac14(\sqrt r+1/\sqrt r)$, so that $\nu\mp\frac12=(\sqrt r\mp1)^2/(4\sqrt r)$ and the ratio reproduces $\xi$ of §2. The entropy becomes

$$
S_1=s(\nu):=\left(\nu+\frac12\right)\log\left(\nu+\frac12\right)-\left(\nu-\frac12\right)\log\left(\nu-\frac12\right).
$$

For $r=4$ we have $\nu=5/8$ and $\xi=1/9$, as before.

The number $\nu$ is invariant under local canonical rescalings, and it satisfies $\nu\geq\frac12$ by the Robertson–Schrödinger uncertainty relation $XP-C^2\geq\frac14$, with $C$ the symmetrized covariance of $q_1$ and $p_1$. For a single oscillator in a pure Gaussian state the bound is saturated. At $\kappa=0$ we obtain $\nu=\frac12$, and for $\kappa>0$ the arithmetic–geometric mean inequality gives $\nu>\frac12$.

**Checkpoint 1.** The total state is pure. Why is $\nu>\frac12$ allowed for site 1?

**Answer.** Purity constrains the full covariance of both sites, whose two symplectic eigenvalues equal $\frac12$. The covariance of site 1 omits the cross-correlations $\langle q_1q_2\rangle$ and $\langle p_1p_2\rangle$, and the restricted state is mixed.

## 4. Gaussian states of many oscillators

### 4.1 The ground-state covariance

For $N$ oscillators consider

$$
H=\frac12p^Tp+\frac12q^TVq,
$$

where $V$ is a real symmetric positive matrix. Write $V=O^T\operatorname{diag}(\omega_k^2)\,O$ and rotate $q$ and $p$ by the same orthogonal matrix $O$, which preserves the commutators. Each normal mode contributes $1/(2\omega_k)$ to the position covariance and $\omega_k/2$ to the momentum covariance, and rotating back gives

$$
X_{ij}=\langle q_iq_j\rangle=\frac12\left(V^{-1/2}\right)_{ij},
\qquad
P_{ij}=\langle p_ip_j\rangle=\frac12\left(V^{1/2}\right)_{ij},
\qquad
\langle q_ip_j+p_jq_i\rangle=0 .
$$

The last relation holds because the ground-state wavefunction is real. Note that $XP=\frac14$, the matrix form of the statement that the global state is pure.

For a set of sites $A$ the reduced state is Gaussian, with covariance given by the principal submatrices $X_A$ and $P_A$. Note that one must restrict after computing the square roots: restricting $V$ first would remove the couplings before finding the ground state, and it describes a different, isolated system (Problem 3).

### 4.2 Williamson's normal form

The regional covariance can be brought to the diagonal form of §3 by a single canonical transformation.

**Claim (Williamson's normal form, block-diagonal case). Model proof.** Let $X_A$ and $P_A$ be real symmetric positive matrices of size $n$, and write $X_A^{1/2}P_AX_A^{1/2}=O\,D^2\,O^T$ with $O$ orthogonal and $D=\operatorname{diag}(\nu_1,\dots,\nu_n)$ positive. The variables

$$
Q=D^{1/2}O^TX_A^{-1/2}q_A,\qquad \Pi=D^{-1/2}O^TX_A^{1/2}p_A
$$

are canonical, $[Q_i,\Pi_j]=i\delta_{ij}$, and in them

$$
\langle QQ^T\rangle=\langle\Pi\Pi^T\rangle=D,
\qquad
\langle Q_i\Pi_j+\Pi_jQ_i\rangle=0 .
$$

*Proof.* The commutator matrix of $Q$ and $\Pi$ is $i\,D^{1/2}O^TX_A^{-1/2}X_A^{1/2}O\,D^{-1/2}=i\,\mathbb 1$, and $Q$, $\Pi$ are separately linear in $q_A$ and $p_A$, so they commute among themselves. The covariances are $D^{1/2}O^TX_A^{-1/2}X_AX_A^{-1/2}O\,D^{1/2}=D$ and $D^{-1/2}O^T(X_A^{1/2}P_AX_A^{1/2})O\,D^{-1/2}=D^{-1/2}D^2D^{-1/2}=D$. The mixed moments vanish because they vanish for $q_A$ and $p_A$. $\square$

Since $X_A^{1/2}P_AX_A^{1/2}$ is similar to $X_AP_A$, the symplectic eigenvalues $\nu_j$ are the positive square roots of the eigenvalues of $X_AP_A$, a matrix that need not be symmetric. Each $\nu_j\geq\frac12$ by the uncertainty relation applied to the pair $(Q_j,\Pi_j)$. A computed value below $\frac12$ signals an error in the covariance or insufficient precision, and it should be diagnosed before any logarithm is taken; clipping it would hide the error.

The general theorem, due to Williamson (1936), states that every positive covariance matrix, including one with position–momentum correlations, is brought to diagonal form by a symplectic transformation, and that its symplectic eigenvalues are the moduli of the eigenvalues of $i\,\sigma\gamma$, with $\gamma$ the covariance and $\sigma$ the symplectic form. We use only the block-diagonal case, which covers every ground state and every thermal state of a Hamiltonian of the form above. [Stated only — refs: Williamson 1936; Weedbrook et al. 2011.]

### 4.3 Entropy, modular Hamiltonian and Weyl operators

In the variables of the claim the Gaussian state is a product of thermal states, one for each pair $(Q_j,\Pi_j)$, since a Gaussian state is fixed by its moments and the product has the same moments. Therefore

$$
\rho_A=\bigotimes_{j=1}^n(1-\xi_j)\,\xi_j^{\,b_j^\dagger b_j},
\qquad
S(A)=\sum_{j=1}^ns(\nu_j),
\qquad
\xi_j=\frac{\nu_j-\frac12}{\nu_j+\frac12},
$$

where $b_j=(Q_j+i\Pi_j)/\sqrt2$. This is a calculation with $n\times n$ matrices, although every oscillator has an infinite-dimensional Hilbert space.

The modular Hamiltonian is $K_A=\sum_j\varepsilon_jb_j^\dagger b_j$ up to a constant, with $\varepsilon_j=\log[(\nu_j+\frac12)/(\nu_j-\frac12)]$. Since $b_j^\dagger b_j=\frac12(Q_j^2+\Pi_j^2)-\frac12$, substituting the claim gives a quadratic form in the original variables,

$$
K_A=\frac12q_A^TM\,q_A+\frac12p_A^TN\,p_A+\text{constant},
$$

where

$$
M=X_A^{-1/2}\,O\operatorname{diag}(\nu_j\varepsilon_j)\,O^T\,X_A^{-1/2},
\qquad
N=X_A^{1/2}\,O\operatorname{diag}(\varepsilon_j/\nu_j)\,O^T\,X_A^{1/2}.
$$

Two consequences are used later. The modular flow $e^{isK_A}(\cdot)e^{-isK_A}$ of a Gaussian state acts linearly on $q_A$ and $p_A$, by a symplectic transformation; in the continuum this becomes the statement that the modular flow of a free field acts on Weyl operators by a symplectic map of test functions, which Lecture 10 identifies with a boost. The second consequence is a numerical warning: modes deep inside the region have $\nu_j-\frac12\simeq e^{-\varepsilon_j}$ exponentially small, so the entropy is insensitive to them, while $M$ and $N$ require arithmetic with a precision beyond $e^{-\varepsilon_{\max}}$. The lattice computations of modular Hamiltonians in the literature, and the one in Lecture 10, use high-precision arithmetic for this reason.

The state can also be described without density matrices, and this is the form that survives in the continuum. For real vectors $u,v$ define the Weyl operators

$$
W(u,v)=\exp\left[i\left(u^Tq+v^Tp\right)\right],
\qquad
W(u,v)\,W(u',v')=e^{-i\sigma/2}\,W(u+u',v+v'),
$$

where $\sigma=u^Tv'-v^Tu'$ is the symplectic form, fixed by $[u^Tq+v^Tp,\,u'^Tq+v'^Tp]=i\sigma$. In a centered Gaussian state without position–momentum correlations,

$$
\langle W(u,v)\rangle=\exp\left[-\frac12\left(u^TXu+v^TPv\right)\right],
$$

as follows for one thermal mode from $\langle e^{i(uQ+v\Pi)}\rangle=e^{-\nu(u^2+v^2)/2}$ and for many modes from the linear transformation of the claim. The regional state is this characteristic function restricted to vectors $u,v$ supported in $A$. Lecture 9 defines the vacuum of the continuum field in exactly this way, with test functions in place of $u$ and $v$ and with no reference to a regional trace.

Finally, displacing the state leaves the entropy unchanged and shifts the expectation value of a quadratic $K_A$. For the state $W\rho W^\dagger$ with $\langle q_A\rangle=\delta q$ and $\langle p_A\rangle=\delta p$, the relative entropy with respect to the undisplaced regional state is therefore

$$
S(\rho_{\delta,A}\Vert\rho_A)=\langle K_A\rangle_\delta-\langle K_A\rangle
=\frac12\,\delta q^TM\,\delta q+\frac12\,\delta p^TN\,\delta p .
$$

For a single thermal mode this is $\varepsilon|\alpha|^2$, with $\alpha$ the displacement of $b$ (Problem 9), and Lecture 10 computes the continuum limit of the formula for a half-line.

## 5. A chain and the limit that makes a field

### 5.1 The lattice field

Discretize a scalar field of mass $m$ on a periodic line of length $L=Na$, with

$$
q_j=\sqrt a\,\phi(ja),\qquad p_j=\sqrt a\,\pi(ja),
$$

so that $[q_i,p_j]=i\delta_{ij}$ follows from $[\phi(x),\pi(y)]=i\delta(x-y)$. The regulated Hamiltonian is

$$
H_a=\frac12\sum_{j=1}^N\left[p_j^2+m^2q_j^2+\frac{(q_{j+1}-q_j)^2}{a^2}\right],
$$

and its normal-mode frequencies are

$$
\omega_k^2=m^2+\frac4{a^2}\sin^2\frac{\pi k}{N},\qquad k=0,\dots,N-1 .
$$

For fixed physical momentum $2\pi k/L$ and $a\to0$, this approaches $m^2+(2\pi k/L)^2$. Modes near the lattice cutoff, with momenta of order $1/a$, have no counterpart at fixed energy, but they are the ones that correlate neighboring sites across a cut.

A rescaling makes the lattice spacing disappear from every entropy. With $\tilde q_j=q_j/\sqrt a$ and $\tilde p_j=\sqrt a\,p_j$, which is canonical,

$$
H_a=\frac1a\,\tilde H,\qquad
\tilde H=\frac12\sum_j\left[\tilde p_j^2+(ma)^2\tilde q_j^2+(\tilde q_{j+1}-\tilde q_j)^2\right].
$$

The ground state is that of $\tilde H$, and local canonical rescalings do not change symplectic eigenvalues. Therefore the entropy of $n$ consecutive sites depends only on $ma$ and $n$, together with the global boundary conditions. On the infinite line the covariances of $\tilde H$ are

$$
\tilde X_{ij}=\int_{-\pi}^{\pi}\frac{dk}{2\pi}\,\frac{e^{ik(i-j)}}{2\tilde\omega(k)},
\qquad
\tilde P_{ij}=\int_{-\pi}^{\pi}\frac{dk}{2\pi}\,\frac{\tilde\omega(k)}2\,e^{ik(i-j)},
\qquad
\tilde\omega(k)^2=(ma)^2+4\sin^2\frac k2 .
$$

At fixed physical separation $|i-j|a=r$ and $a\to0$, $\tilde X_{ij}=\langle\phi(ia)\phi(ja)\rangle$ approaches the continuum two-point function $K_0(mr)/2\pi$. For $mr=1$ the lattice values are $0.066921$, $0.067003$ and $0.067008$ at $1/a=8$, $32$ and $128$, against $K_0(1)/2\pi=0.067008$.

### 5.2 What the limit holds fixed

A continuum limit fixes the physical mass, the lengths of the regions and their separations, and sends $a\to0$. The number of sites in a region of length $\ell$ grows as $\ell/a$, and the dimensionless mass $ma$ goes to zero. But two other limits are easily confused with this one. Sending $N\to\infty$ at fixed $a$ is a thermodynamic limit of the lattice, which removes finite-size effects and keeps the cutoff. Keeping the number of sites of a region fixed while $a\to0$ shrinks the region to a point. Only the first procedure asks what a region of a field theory contains.

### 5.3 The zero mode and the infrared

At $m=0$ the mode $k=0$ of the periodic chain has zero frequency, a free particle with no normalizable ground state, so the Gaussian formulas above do not apply. Dropping the mode silently changes the model; one may instead impose other boundary conditions, or treat a compact scalar with its zero mode handled separately.

On the infinite line the massless limit is also delicate, since the equal-point covariance grows logarithmically,

$$
\tilde X_{jj}=\frac1{2\pi}\log\frac8{ma}+O\!\left((ma)^2\log\frac1{ma}\right),
$$

which is the infrared divergence of $\langle\phi^2\rangle$ for a massless scalar in two dimensions (Problem 12). Entropies of finite intervals stay finite for $m>0$, but at small $m\ell$ they acquire, besides the conformal term, a slowly varying contribution $\frac12\log(-\log m\ell)$ found by Casini and Huerta. [Stated only — refs: Casini–Huerta 2005.] For this reason the lattice experiment below keeps $m>0$ and reads the universal coefficient from the dependence on $a$ at fixed $m\ell$.

## 6. Worked example: the entropy diverges, the mutual information converges

Take $m=1$, an interval $A$ of length $\ell=1$, and a second interval $B$ of the same length separated from $A$ by a gap $d=\frac12$. For each lattice spacing we compute the covariances of §5.1, the symplectic eigenvalues of the principal submatrices for $A$, $B$ and $A\cup B$, and the entropies of §4.3. Every step is a finite matrix computation. In exact arithmetic every $\nu_j\geq\frac12$; in double precision the deepest modes sit at $\frac12$ to within rounding, about $10^{-15}$, and contribute nothing to the entropy. The results are

| $1/a$ | $S(A)$ | increment | $I(A{:}B)$ |
|---:|---:|---:|---:|
| 8 | 0.68210 | — | 0.054376 |
| 16 | 0.91043 | 0.22833 | 0.054435 |
| 32 | 1.14067 | 0.23024 | 0.054430 |
| 64 | 1.37149 | 0.23082 | 0.054425 |
| 128 | 1.60247 | 0.23098 | 0.054424 |
| 256 | 1.83350 | 0.23103 | 0.054423 |
| 512 | 2.06455 | 0.23104 | 0.054423 |

where the increment is $S(A)$ minus its value at twice the spacing, and $I(A{:}B)=S(A)+S(B)-S(A\cup B)$ is the mutual information. The increments approach $\frac13\log2=0.231049$. That is,

$$
S(A)=\frac13\log\frac\ell a+\text{finite},
$$

with the coefficient of the two-dimensional conformal result for $c=1$. The finite part depends on $m\ell$ and on the lattice, and it has no universal meaning. The mutual information converges to $0.054423$ within six digits.

A second experiment tests the massive saturation. For an interval much longer than the correlation length, $\ell=40/m$, the entropy at $ma=0.2,\,0.1,\,0.05,\,0.025,\,0.0125$ increases by $0.3245$, $0.3306$, $0.3325$ and $0.3331$ per halving of $ma$, in units of $\log2$. The slope approaches $\frac13$: the entropy of a long interval is $\frac13\log(1/ma)$ plus a constant, the result of Calabrese and Cardy with $c=1$ and two endpoints, and the figure shows both behaviors.

![[ads-cft-chain-entanglement.svg|Left: entropy of an interval in the harmonic chain against its length in lattice units, for four masses; each curve grows logarithmically and saturates when the length exceeds the correlation length. Right: at fixed physical sizes, the entropy of an interval grows by one third of log 2 each time the lattice spacing halves, while the mutual information of two separated intervals stays constant.]]

**Checkpoint 2.** Why does $I(A{:}B)$ converge while $S(A)$ diverges?

**Answer.** The divergent part of an entropy comes from correlations at distances of order $a$ across its endpoints. Separated intervals have $\partial(A\cup B)=\partial A\cup\partial B$, so the endpoint contributions cancel in $S(A)+S(B)-S(A\cup B)$. What remains measures correlations across the gap, at distances at least $d$, and these have a continuum limit.

> **Physical picture: entanglement at the shortest scale.** The vacuum correlates neighboring points at every scale, and a sharp cut severs correlations at all wavelengths down to the cutoff. Each halving of $a$ adds a new layer of short-wavelength modes near each endpoint, and each layer contributes the same amount, $\frac16\log2$ per endpoint. A gap of fixed size removes those layers from the correlation between two regions. This is a statement about the lattice model and its numerics. In Lecture 9 the same contrast appears in algebraic form: for touching regions no type-I factor lies between $\mathcal A(O)$ and $\mathcal A(O')'$, while a buffer supplies one under the hypotheses of the split property.

## 7. Self-study: the half-chain and its modular ladder

For the half-chain the regional spectrum is known in closed form: Peschel and Chung showed, using the corner transfer matrices of an associated two-dimensional Gaussian model, that the reduced density matrix of the sites $j\geq1$ of the infinite chain $\tilde H$ is

$$
\rho_{\mathrm{half}}=\bigotimes_{j=0}^\infty\left(1-e^{-\varepsilon_j}\right)e^{-\varepsilon_jn_j},
\qquad
\varepsilon_j=(2j+1)\varepsilon,
\qquad
\varepsilon=\pi\,\frac{K(k')}{K(k)},
$$

where $n_j$ are number operators of independent modes, $K$ is the complete elliptic integral of the first kind, and the modulus is fixed by $k+1/k=2+(ma)^2$, with $k'=\sqrt{1-k^2}$. [Stated only — refs: Peschel–Chung 1999; Peschel–Eisler 2009.] The numerics of §6 confirm it. An interval of $1500$ sites at $ma=0.02$ is thirty correlation lengths long, so its two endpoints act as independent half-chains, and its lowest modular energies come in degenerate pairs $1.64727$, $4.94181$, $8.23635$; the formula gives $\varepsilon=1.64727$ and the ratios $1:3:5$.

The entropy of the half-chain follows from this spectrum. Write $q=e^{-\varepsilon}$ and

$$
F(\varepsilon)=-\sum_{j=0}^\infty\log\left(1-q^{2j+1}\right),
\qquad
S_{\mathrm{half}}=\sum_{j=0}^\infty s_j=\left(1-\varepsilon\frac{d}{d\varepsilon}\right)F(\varepsilon),
$$

where $s_j=\varepsilon_j/(e^{\varepsilon_j}-1)-\log(1-e^{-\varepsilon_j})$ is the entropy of one thermal mode. The product is a ratio of Dedekind functions. With $\eta(\tau)=e^{i\pi\tau/12}\prod_{n\geq1}(1-e^{2\pi in\tau})$ and $\tau=i\varepsilon/2\pi$,

$$
\prod_{j\geq0}\left(1-q^{2j+1}\right)=q^{1/24}\,\frac{\eta(\tau)}{\eta(2\tau)} .
$$

The modular transformation $\eta(-1/\tau)=\sqrt{-i\tau}\,\eta(\tau)$ converts the small-$\varepsilon$ behavior into a rapidly convergent product, and one obtains (Problem 11)

$$
F(\varepsilon)=\frac{\pi^2}{12\varepsilon}-\frac12\log2+\frac\varepsilon{24}+O\!\left(e^{-2\pi^2/\varepsilon}\right),
\qquad
S_{\mathrm{half}}=\frac{\pi^2}{6\varepsilon}-\frac12\log2+O\!\left(\varepsilon^{-1}e^{-2\pi^2/\varepsilon}\right).
$$

For small $ma$ the modulus satisfies $k'^2=2ma+O((ma)^2)$, so that $K(k')\to\pi/2$ and $K(k)\simeq\log(4/k')$. Thus

$$
\varepsilon\simeq\frac{\pi^2}{\log(8/ma)},
\qquad
S_{\mathrm{half}}\simeq\frac16\log\frac8{ma}-\frac12\log2=\frac16\log\frac1{ma},
$$

since $\frac16\log8=\frac12\log2$. The values of $S_{\mathrm{half}}$ at $ma=0.1$, $0.02$ and $0.005$ are $0.38508$, $0.65208$ and $0.88306$, against $\frac16\log(1/ma)=0.38376$, $0.65200$ and $0.88305$. The corrections are of order $(ma)^2\log(1/ma)$: the terms exponentially small in $1/\varepsilon$ are of this size, since $e^{-2\pi^2/\varepsilon}\simeq(ma/8)^2$, and $\pi^2/6\varepsilon$ itself differs from $\frac16\log(8/ma)$ by $(ma)^2/96$. Each endpoint therefore contributes $\frac c6\log(\xi/a)$ with $c=1$ and $\xi=1/m$, and an interval longer than $\xi$ has two of them, which is the saturation of §6.

But the spectrum carries more information than its entropy. The modular energies form a ladder of spacing $2\varepsilon=2\pi^2/\log(8/ma)$, which closes as $a\to0$, and the number of levels below a fixed modular energy grows as $\log(1/ma)$. The divergence of the entropy is the growth of this density of levels, and in the continuum the ladder becomes a continuous spectrum.

> **Physical picture: a lattice boost.** Baxter's corner transfer matrix transports a two-dimensional lattice model around a corner, and Thacker observed in 1986 that its generator is a lattice version of the Lorentz boost. The reduced density matrix of the half-chain is a product of corner transfer matrices that together turn the Euclidean plane by a full angle around the cut. Lecture 10 meets the same full turn as the origin of the factor $2\pi$ in the Bisognano–Wichmann relation $\Delta=e^{-2\pi K}$, where $K$ is the boost generator. This is a heuristic link. The lattice statements are those of Peschel and collaborators, and the continuum statement is the theorem of Lecture 10.

## 8. What the chain does and does not decide

At every finite lattice spacing, a set of sites carries a type-I algebra, a trace and a density matrix. Refining the lattice at fixed physical size makes its entropy grow without bound. The growth alone does not determine what algebra describes the region in the limit: the type of a limiting algebra depends on the observables retained, the state, and the representation in which the limit is taken, and Lecture 9 gives infinite-product examples with divergent entropy and different types.

What the calculation does establish is why the continuum question cannot be answered by keeping a fixed number of oscillators. At fixed physical length the number of modes near each endpoint grows as the spacing shrinks, and each new layer is entangled across the cut. The convergence of the mutual information and the closing of the modular ladder are lattice evidence for two continuum statements, the split property of Lecture 9 and the geometric modular flow of Lecture 10. They are evidence only; the continuum statements are theorems with their own hypotheses.

## 9. What to take away

- **Exact calculation:** the reduced state of one of two coupled oscillators is thermal for an oscillator of frequency $\sqrt{\omega_+\omega_-}$, with $e^{-\varepsilon}=\left(\frac{\sqrt{\omega_+}-\sqrt{\omega_-}}{\sqrt{\omega_+}+\sqrt{\omega_-}}\right)^2$; the wavefunction and the covariance give the same state.
- **Model proof:** a Gaussian state without position–momentum correlations is a product of thermal modes, with symplectic eigenvalues $\nu_j$ the square roots of the eigenvalues of $X_AP_A$; the entropy is $\sum_js(\nu_j)$, and the modular Hamiltonian is a quadratic form whose flow is symplectic.
- **Numerical, in a defined model:** at fixed physical sizes the increments of the interval entropy per halving of $a$ approach $\frac13\log2$, while the mutual information of separated intervals converges to six digits.
- **Stated only, with an exact consequence:** the half-chain has modular energies $(2j+1)\varepsilon$ with $\varepsilon\simeq\pi^2/\log(8/ma)$, and its entropy is $\frac16\log(1/ma)+O\bigl((ma)^2\log(1/ma)\bigr)$.
- **Heuristic:** divergent entropy does not classify the limiting algebra; convergent mutual information and a closing modular ladder anticipate the split property and the boost.

## 10. Looking ahead

Lecture 9 replaces the matrices $X_A$ and $P_A$ by the algebra generated by Weyl operators of test functions supported in a region, and the characteristic function of §4.3 by the vacuum state on that algebra; the divergence of §6 becomes the absence of a regional trace, and the convergence becomes the split property. Lecture 10 states the continuum result for the half-line, that the modular Hamiltonian of a Rindler wedge is $2\pi$ times the boost generator, and tests numerically that the lattice relative entropy of §4.3 approaches the boost energy of a classical wave. Lecture 23 reuses the effective thermal spectrum of §2, with a physical Hamiltonian in the role of $K_1$.

## 11. Problem set

### Classroom core

1. **The uncoupled limit.** Show that $\nu=\frac12$ if and only if $\omega_+=\omega_-$, that is, $\kappa=0$.

2. **Purity without a wavefunction integral.** Compute $\operatorname{Tr}\rho_1^2$ from the spectrum of $\rho_1$ and express it in terms of $\nu$.

3. **A principal submatrix does not commute with a function.** For two oscillators compare $X_{11}$ with $1/\bigl(2\sqrt{V_{11}}\bigr)$ and explain which system each describes.

4. **The Mehler match.** Show that $A=\Omega\coth\varepsilon$ and $B=\Omega/\sinh\varepsilon$ imply $\Omega=\sqrt{A^2-B^2}$ and $e^{-\varepsilon}=B/(A+\Omega)$, and verify $\Omega=\sqrt{\omega_+\omega_-}$ from the expressions for $A$ and $B$.

5. **A numerical example.** For $\omega_-/\omega_+=4$, compute $\nu$, $\xi$, $S_1$ and the effective temperature $\Omega/\varepsilon$ in units of $\omega_+$.

6. **Only $ma$ matters.** Show that the symplectic eigenvalues of $n$ consecutive sites of $H_a$ depend on $a$ and $m$ only through $ma$. What does this imply for the entropy of an interval of fixed physical length as $a\to0$?

### Self-study consolidation

7. **Weak coupling.** Let $u=\kappa/\omega_0^2\ll1$. Find the leading behavior of $\nu-\frac12$ and of $S_1$, and explain why the entropy has no regular power series in $u$.

8. **Williamson in two lines.** For $X_A=\operatorname{diag}(x_1,x_2)$ and a nondiagonal $P_A$, construct the transformation of §4.2 explicitly and verify that it diagonalizes both covariances.

9. **Relative entropy of a displacement.** Show that $S(\rho_{\delta,A}\Vert\rho_A)=\frac12\delta q^TM\delta q+\frac12\delta p^TN\delta p$, and that for one thermal mode displaced by $\alpha$ it equals $\varepsilon|\alpha|^2$.

10. **Mutual information at large separation.** Explain why $I(A{:}B)\geq0$, and estimate how it decays when the gap $d$ is much larger than $1/m$. *Hint:* the mutual information of Gaussian states is quadratic in weak cross-correlations.

11. **The modular transformation.** Derive $F(\varepsilon)=\frac{\pi^2}{12\varepsilon}-\frac12\log2+\frac{\varepsilon}{24}+O(e^{-2\pi^2/\varepsilon})$ from the product formula of §7, and from it $S_{\mathrm{half}}=\frac{\pi^2}{6\varepsilon}-\frac12\log2$ up to exponentially small terms.

12. **The infrared.** Show that $\tilde X_{jj}=\frac1{2\pi}\log\frac8{ma}$ up to corrections of order $(ma)^2\log(1/ma)$, and explain why the periodic massless chain has no normalizable Gaussian ground state.

### Research extension

13. **The modular Hamiltonian near a cut.** Compute the kernels $M$ and $N$ of §4.3 for a long interval of the massive chain, with high-precision arithmetic, and compare them near one endpoint with the discretized boost generator $2\pi\sum_jx_j\,h_j$, where $h_j$ is the energy density at site $j$ and $x_j$ its distance from the cut. *Known:* Eisler, Di Giulio, Tonni and Peschel find dominant on-site and nearest-neighbor terms with triangular profiles, and small longer-range couplings that matter near criticality; Di Giulio and Tonni obtain the conformal result in the massless continuum limit. *Completion:* the profiles of the diagonal terms of $N$ and of the nearest-neighbor terms of $M$ for two masses, with the size of the longer-range terms.

14. **When the gap closes.** Compute $I(A{:}B)$ for two intervals of length $\ell$ as the gap $d$ decreases at fixed $a$, and as $a\to0$ at fixed $d$. *Known:* for adjacent intervals the mutual information diverges as $a\to0$, and Lecture 9 relates this to the absence of a type-I factor between touching regions; Hollands and Sanders bound entanglement measures in terms of the size of the buffer. *Completion:* the behavior of $I$ as a function of $d/\ell$ at small $d$, and the demonstration that the limits $a\to0$ and $d\to0$ do not commute.

15. **The area law.** Discretize a free massless scalar in $3+1$ dimensions on radial shells, as Srednicki did, and compute the entropy of a ball of radius $R$. *Known:* Srednicki finds an entropy proportional to $R^2/a^2$, with a coefficient of about $0.3$. *Completion:* the coefficient to a few percent, and the demonstration that the dependence on $R$ is quadratic over a decade.

## 12. Answer checkpoints

1. With $r=\omega_-/\omega_+$, $\nu=\frac14(\sqrt r+1/\sqrt r)\geq\frac12$ with equality only at $r=1$, which requires $\kappa=0$.

2. The geometric series gives $(1-\xi)^2/(1-\xi^2)=(1-\xi)/(1+\xi)=1/(2\nu)$, which is less than one for $\kappa>0$.

3. $X_{11}=\frac14(\omega_+^{-1}+\omega_-^{-1})$, while $1/(2\sqrt{V_{11}})=1/(2\sqrt{\omega_0^2+\kappa})$. They agree at $\kappa=0$ and differ at second order in $\kappa$. The second is the ground-state variance of site 1 with site 2 clamped, an isolated oscillator, and it has no entropy.

4. $A^2-B^2=\Omega^2(\coth^2\varepsilon-\sinh^{-2}\varepsilon)=\Omega^2$, and $B/(A+\Omega)=1/(\cosh\varepsilon+\sinh\varepsilon)=e^{-\varepsilon}$. With $A-B=2\omega_+\omega_-/(\omega_++\omega_-)$ and $A+B=\frac12(\omega_++\omega_-)$, the product is $\omega_+\omega_-$.

5. $\nu=5/8$, $\xi=1/9$, $S_1=\log\frac98+\frac18\log9\approx0.3924$, $\Omega=2\omega_+$, $\varepsilon=\log9$, and $\Omega/\varepsilon=2\omega_+/\log9\approx0.910\,\omega_+$.

6. The canonical rescaling $\tilde q_j=q_j/\sqrt a$, $\tilde p_j=\sqrt a\,p_j$ gives $H_a=\tilde H/a$, where $\tilde H$ contains only $ma$. The ground state does not depend on the overall factor $1/a$, and symplectic eigenvalues are invariant under local rescalings. An interval of length $\ell$ contains $\ell/a$ sites with $ma\to0$, so its entropy is a function $S(\ell/a,ma)$, and the limit probes both arguments at once.

7. $r=\sqrt{1+2u}$ gives $\nu-\frac12=\frac{u^2}{16}+O(u^3)$. With $n=\nu-\frac12$, $s(\nu)=n(1-\log n)+O(n^2)$, so $S_1\simeq\frac{u^2}{16}\left(1-\log\frac{u^2}{16}\right)$. The logarithm reflects the nonanalyticity of $-x\log x$ at a pure state.

8. $X_A^{\pm1/2}=\operatorname{diag}(x_1^{\pm1/2},x_2^{\pm1/2})$. Diagonalize the symmetric matrix $X_A^{1/2}P_AX_A^{1/2}=OD^2O^T$ and form $Q$ and $\Pi$; the two covariance computations of the proof in §4.2 apply entry by entry.

9. $S(W\rho W^\dagger)=S(\rho)$ because $W$ is unitary, so the relative entropy equals the change of $\langle K_A\rangle$. A quadratic $K_A$ shifts by $\frac12\delta^T(M\oplus N)\delta$, because the linear terms vanish in the centered state. For one mode $K=\varepsilon b^\dagger b$, and the displaced expectation value is $\varepsilon(\bar n+|\alpha|^2)$.

10. $I(A{:}B)$ is the relative entropy between $\rho_{AB}$ and $\rho_A\otimes\rho_B$, and therefore nonnegative. The cross-correlations decay as $K_0(md)\sim e^{-md}$, and a second-order expansion in them gives $I\sim e^{-2md}$ times a power of $d$. For two intervals of length $1/m$, with $m=1$ as in §6 and $1/a=64$, the lattice gives $I=0.0133$, $0.00116$ and $0.000119$ at $md=1$, $2$ and $3$.

11. $\tau\mapsto-1/\tau$ sends $\tau=i\varepsilon/2\pi$ to $2\pi i/\varepsilon$, so that $\eta(\tau)=\sqrt{2\pi/\varepsilon}\,e^{-\pi^2/6\varepsilon}\left[1+O(e^{-4\pi^2/\varepsilon})\right]$ and $\eta(2\tau)=\sqrt{\pi/\varepsilon}\,e^{-\pi^2/12\varepsilon}\left[1+O(e^{-2\pi^2/\varepsilon})\right]$. The ratio is $\sqrt2\,e^{-\pi^2/12\varepsilon}$, and $F=-\log\left(q^{1/24}\eta(\tau)/\eta(2\tau)\right)$ gives the stated series. Applying $1-\varepsilon\,d/d\varepsilon$ cancels the term linear in $\varepsilon$ and doubles $\pi^2/12\varepsilon$.

12. $\tilde X_{jj}=\frac1{2\pi}\int_0^\pi dk/\sqrt{(ma)^2+4\sin^2(k/2)}$ is a complete elliptic integral with modulus close to one; its logarithmic behavior gives $\frac1{2\pi}\log(8/ma)$. At $ma=10^{-3}$ the integral is $1.430357$ and the formula gives $1.430357$. On the periodic massless chain the mode $k=0$ has $V$-eigenvalue zero, so $X=\frac12V^{-1/2}$ does not exist; that mode is a free particle, with continuous spectrum and no normalizable ground state.
