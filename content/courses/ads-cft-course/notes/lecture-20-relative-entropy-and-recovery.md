---
title: "Lecture 20 — Distinguishability and recovery channels"
type: lecture-notes
edition: "2.2 — rewritten at the AQFT standard"
lecture: 20
semester: 2
week: 3
hours: 3
prerequisites: "Lectures 2, 3, 7 and 9; density matrices, Kraus operators and the Hilbert–Schmidt representation"
status: "rewritten 2026-09-30, pending instructor review; data processing and Petz's equality theorem proved in finite dimensions through relative modular operators, the universal recovery bound stated with sources"
modified: 2026-09-30
---

# Lecture 20 — Distinguishability and recovery channels

> *A channel may change a state without losing the information that distinguishes it from a reference. Relative entropy measures that information, and its monotonicity under channels, the data-processing inequality, is where every recovery argument starts. We prove it in finite dimensions with the relative modular operators of Lecture 9, following Petz, and then prove Petz's theorem on the case of equality: distinguishability is preserved exactly when one explicit channel, built from the reference state and the adjoint of the channel, undoes the channel on both states. The theorem is tested on dephasing, on a flagged erasure, and on the three-qutrit code of Lecture 2, where the Petz map rebuilds the logical state from any pair of shares. An approximate version, due to Junge, Renner, Sutter, Wilde and Winter, bounds the fidelity of recovery by the loss of relative entropy, and in that form Cotler, Hayden, Penington, Salton, Swingle and Walter used it to extend entanglement-wedge reconstruction to approximate recovery.*

## How to use this lecture

**Classroom core, one meeting of three hours.** The history (§1, 10 minutes), the classical model (§2, 20 minutes), the Petz map (§3, 20 minutes), and the proof of data processing (§4, 40 minutes) come before a 10-minute break. After it come the equality theorem (§5, 35 minutes) and the worked examples (§6, 30 minutes), with 15 minutes for Checkpoints 1 and 2; Problems 1–6 are the core assignment. These allocations are proposals and have not been tested in class.

**Self-study.** Approximate recovery and the fidelity convention (§7), the return to regional reconstruction (§8), and Problems 7–12, including the integral representation of the logarithm and Petz's condition on Connes cocycles.

**Research extension.** The Petz map of the deformed code of Lecture 7, rotated Petz maps for a non-unital channel, and the modular form of the recovery map, in Problems 13–15.

**Prerequisites.** Lecture 2 for the three-qutrit code, Lecture 3 for modular operators in finite dimensions, Lecture 7 for the deformed code, Lecture 9 for Araki's relative entropy and the Hilbert–Schmidt representation $\Delta_{\sigma|\rho}(X)=\sigma X\rho^{-1}$. Density matrices, Kraus operators, and completely positive maps.

**What this lecture establishes.** In finite dimensions, with faithful states, the data-processing inequality and Petz's equality theorem are proved completely; the direction from recovery to equality is elementary. The flagged erasure and the three-qutrit Petz map are exact calculations. The universal recovery theorem is stated with its source, and checked on the erasure channel, where it is saturated at the two ends. The extension of these results to von Neumann algebras is stated.

## 0. Reading

**Primary.**

- D. Petz, [Monotonicity of quantum relative entropy revisited](https://arxiv.org/abs/quant-ph/0209053) (2003).
- M. Junge, R. Renner, D. Sutter, M. M. Wilde, A. Winter, [Universal recovery maps and approximate sufficiency of quantum relative entropy](https://arxiv.org/abs/1509.07127) (2015).
- J. Cotler, P. Hayden, G. Penington, G. Salton, B. Swingle, M. Walter, [Entanglement Wedge Reconstruction via Universal Recovery Channels](https://arxiv.org/abs/1704.05839) (2017).

**Secondary.**

- D. Petz, Sufficient subalgebras and the relative entropy of states of a von Neumann algebra, *Commun. Math. Phys.* 105 (1986) 123, and Sufficiency of channels over von Neumann algebras, *Quart. J. Math.* 39 (1988) 97.
- P. Hayden, R. Jozsa, D. Petz, A. Winter, [Structure of states which satisfy strong subadditivity of quantum entropy with equality](https://arxiv.org/abs/quant-ph/0304007) (2003).
- H. Barnum, E. Knill, [Reversing quantum dynamics with near-optimal quantum and classical fidelity](https://arxiv.org/abs/quant-ph/0004088) (2000).
- M. M. Wilde, [From Classical to Quantum Shannon Theory](https://arxiv.org/abs/1106.1445), the chapters on relative entropy and recoverability.

**Optional research reading.**

- O. Fawzi, R. Renner, [Quantum conditional mutual information and approximate Markov chains](https://arxiv.org/abs/1410.0664) (2014).
- E. Witten, [Notes on Some Entanglement Properties of Quantum Field Theory](https://arxiv.org/abs/1803.04993) (2018), §§3.4–3.6, the proof of monotonicity for von Neumann algebras.
- A. Müller-Hermes, D. Reeb, [Monotonicity of the Quantum Relative Entropy Under Positive Maps](https://arxiv.org/abs/1512.06117) (2015).
- D. Harlow, [The Ryu-Takayanagi Formula from Quantum Error Correction](https://arxiv.org/abs/1607.03901) (2016).

## 1. What does it mean to lose no information?

The monotonicity of relative entropy has a history that runs through the strong subadditivity of entropy. Lieb and Ruskai proved strong subadditivity in 1973, and Lindblad derived from it in 1975 that relative entropy cannot increase under a completely positive, trace-preserving map. Uhlmann gave an independent proof in 1977 by interpolation. Petz then asked, in 1986 for subalgebras and in 1988 for channels, when the inequality is an equality, and borrowed the answer from statistics. A family of distributions is said to have a sufficient statistic if a function of the data retains everything needed to distinguish them. Petz showed that a quantum channel preserves the relative entropy of a pair of states exactly when the channel is sufficient for the pair, that is, when some channel reverses it on both states, and he wrote the reversing channel down explicitly. It is now called the Petz map.

The subject returned to prominence through quantum information. Barnum and Knill showed in 2000 that the same map, introduced as a reversal adapted to the input and to the noise, has an error at most twice that of the optimal reversal, measured with a reference system or on a classical ensemble. Hayden, Jozsa, Petz and Winter used the equality theorem in 2003 to classify the states that saturate strong subadditivity, the quantum Markov chains. Whether an approximate equality implies an approximate recovery remained open for a decade. Fawzi and Renner proved a version for conditional mutual information in 2014, and Junge, Renner, Sutter, Wilde and Winter proved in 2015 that a universal recovery channel, depending only on the reference state and the channel, achieves a fidelity controlled by the loss of relative entropy.

In holography these results turn the relative-entropy identity of Lecture 21 into reconstruction. Dong, Harlow and Wall turned the exact identity into reconstruction in 2016 with operator-algebra error correction, and Cotler and collaborators used the approximate identity and the recovery channels of §7 in 2017. The question for this lecture is the one Lecture 7 raised in a finite code: when can the effect of a channel on a family of states be undone, and by what map?

## 2. The classical model: restore a forgotten label

Let a channel forget $x$ and retain $y$ from a joint distribution $p(x,y)$, and fix a reference $q(x,y)$. Bayes' rule supplies a recovery channel,

$$
R_q(x,y\,|\,y')=\delta_{yy'}\,q(x|y),
$$

which reinserts $x$ with its reference conditional distribution. It recovers the reference exactly, and applied to $p_Y$ it gives $\widetilde p(x,y)=p_Y(y)\,q(x|y)$. The loss of relative entropy is measured by the chain rule,

$$
D(p_{XY}\Vert q_{XY})-D(p_Y\Vert q_Y)=\sum_yp_Y(y)\,D(p_{X|y}\Vert q_{X|y}),
$$

which follows by splitting $\log[p(x,y)/q(x,y)]$ into $\log[p_Y(y)/q_Y(y)]+\log[p(x|y)/q(x|y)]$ and summing. The loss vanishes exactly when $p(x|y)=q(x|y)$ for the relevant $y$, and then the forgotten label is restored by the reference conditional distribution. No physical copy of $x$ was preserved: the family of allowed distributions makes it redundant. The quantum version of $R_q$ is the Petz map.

## 3. The Petz map

For a channel $\mathcal N$, with Hilbert–Schmidt adjoint $\mathcal N^\dagger$, and a faithful reference $\sigma$, the Petz map is

$$
\mathcal R_{\sigma,\mathcal N}(X)=\sigma^{1/2}\,\mathcal N^\dagger\!\left[\mathcal N(\sigma)^{-1/2}X\,\mathcal N(\sigma)^{-1/2}\right]\sigma^{1/2}.
$$

It is completely positive, since conjugations and $\mathcal N^\dagger$ are completely positive and composition preserves the property. For $X$ supported on the support of $\mathcal N(\sigma)$ it preserves the trace,

$$
\operatorname{Tr}\mathcal R_{\sigma,\mathcal N}(X)=\operatorname{Tr}\left[\mathcal N(\sigma)\,\mathcal N(\sigma)^{-1/2}X\,\mathcal N(\sigma)^{-1/2}\right]=\operatorname{Tr}X,
$$

and it recovers the reference, $\mathcal R_{\sigma,\mathcal N}(\mathcal N(\sigma))=\sigma^{1/2}\mathcal N^\dagger(I)\sigma^{1/2}=\sigma$, because $\mathcal N^\dagger$ is unital. If the output space contains a sector outside the support of $\mathcal N(\sigma)$, the map is extended there by a fixed replacement state to obtain a channel on the whole output space. For a classical channel and commuting states it reduces to $R_q$. These properties make the Petz map a candidate decoder. But they do not by themselves imply that it recovers any state other than $\sigma$; that is the content of the theorem of §5.

## 4. Data processing, proved with relative modular operators

We work in finite dimensions with faithful states $\rho$ and $\sigma$ on the input and assume that $\widetilde\rho=\mathcal N(\rho)$ and $\widetilde\sigma=\mathcal N(\sigma)$ are faithful on the output, restricting to supports otherwise. In the Hilbert–Schmidt representation of Lecture 9, the relative entropy is

$$
D(\rho\Vert\sigma)=-\langle\xi_\rho,\log\Delta_{\sigma|\rho}\,\xi_\rho\rangle,
\qquad
\xi_\rho=\rho^{1/2},\qquad \Delta_{\sigma|\rho}(X)=\sigma X\rho^{-1}.
$$

Write $\Delta_1=\Delta_{\sigma|\rho}$ and $\xi_1=\xi_\rho$ on the input, and $\Delta_2=\Delta_{\widetilde\sigma|\widetilde\rho}$ and $\xi_2=\widetilde\rho^{1/2}$ on the output. The proof has four steps.

*A contraction between the two representations.* Define $V$ from output to input matrices by

$$
V\left(X\widetilde\rho^{1/2}\right)=\mathcal N^\dagger(X)\,\rho^{1/2}.
$$

Since $\mathcal N^\dagger$ is unital, $V\xi_2=\xi_1$. The Kadison–Schwarz inequality for the unital completely positive map $\mathcal N^\dagger$, $\mathcal N^\dagger(X)^\dagger\mathcal N^\dagger(X)\leq\mathcal N^\dagger(X^\dagger X)$, gives

$$
\left\|V\left(X\widetilde\rho^{1/2}\right)\right\|^2=\operatorname{Tr}\left[\rho\,\mathcal N^\dagger(X)^\dagger\mathcal N^\dagger(X)\right]\leq\operatorname{Tr}\left[\rho\,\mathcal N^\dagger(X^\dagger X)\right]=\operatorname{Tr}\left[\widetilde\rho X^\dagger X\right]=\left\|X\widetilde\rho^{1/2}\right\|^2,
$$

so $V$ is a contraction. Because $\|V\xi_2\|=\|\xi_2\|$ and $\|V\|\leq1$, also $V^\dagger V\xi_2=\xi_2$.

*An operator inequality.* The same inequality applied to $X^\dagger$ gives $V^\dagger\Delta_1V\leq\Delta_2$. Indeed,

$$
\left\langle V\bigl(X\widetilde\rho^{1/2}\bigr),\Delta_1V\bigl(X\widetilde\rho^{1/2}\bigr)\right\rangle=\operatorname{Tr}\left[\sigma\,\mathcal N^\dagger(X)\mathcal N^\dagger(X)^\dagger\right]\leq\operatorname{Tr}\left[\widetilde\sigma XX^\dagger\right]=\left\langle X\widetilde\rho^{1/2},\Delta_2\,X\widetilde\rho^{1/2}\right\rangle .
$$

*A variational bound.* For a positive invertible operator $B$ and a vector $\xi$,

$$
\langle\xi,B^{-1}\xi\rangle=\sup_\eta\left[2\operatorname{Re}\langle\eta,\xi\rangle-\langle\eta,B\eta\rangle\right],
$$

with the supremum attained only at $\eta=B^{-1}\xi$, since the bracket equals $\langle\xi,B^{-1}\xi\rangle-\langle\eta-B^{-1}\xi,B(\eta-B^{-1}\xi)\rangle$. For $s>0$ we have $\Delta_2+s\geq V^\dagger(\Delta_1+s)V$, because $V^\dagger\Delta_1V\leq\Delta_2$ and $V^\dagger V\leq I$, and $\langle\eta,\xi_2\rangle=\langle\eta,V^\dagger V\xi_2\rangle=\langle V\eta,\xi_1\rangle$. Therefore

$$
2\operatorname{Re}\langle\eta,\xi_2\rangle-\langle\eta,(\Delta_2+s)\eta\rangle\leq2\operatorname{Re}\langle V\eta,\xi_1\rangle-\langle V\eta,(\Delta_1+s)V\eta\rangle\leq\langle\xi_1,(\Delta_1+s)^{-1}\xi_1\rangle,
$$

and taking the supremum over $\eta$,

$$
\langle\xi_2,(\Delta_2+s)^{-1}\xi_2\rangle\leq\langle\xi_1,(\Delta_1+s)^{-1}\xi_1\rangle\qquad\text{for every }s>0 .
$$

*Integration.* The representation $-\log x=\int_0^\infty ds\left[(x+s)^{-1}-(1+s)^{-1}\right]$ and $\|\xi_1\|=\|\xi_2\|=1$ give

$$
D(\widetilde\rho\Vert\widetilde\sigma)=\int_0^\infty ds\left[\langle\xi_2,(\Delta_2+s)^{-1}\xi_2\rangle-\frac1{1+s}\right]\leq\int_0^\infty ds\left[\langle\xi_1,(\Delta_1+s)^{-1}\xi_1\rangle-\frac1{1+s}\right]=D(\rho\Vert\sigma).
$$

This is the data-processing inequality, $D(\mathcal N(\rho)\Vert\mathcal N(\sigma))\leq D(\rho\Vert\sigma)$. [Model proof, in finite dimensions; for von Neumann algebras it is the theorem of Uhlmann, stated in Lecture 9, §6.3.]

**Checkpoint 1.** Where did complete positivity enter, and where did trace preservation?

**Answer.** Complete positivity of $\mathcal N$ makes $\mathcal N^\dagger$ completely positive, which gives the Kadison–Schwarz inequality; positivity alone does not. Trace preservation of $\mathcal N$ makes $\mathcal N^\dagger$ unital, which gives $V\xi_2=\xi_1$ and the normalization of both vectors. Two-positivity of $\mathcal N^\dagger$ already suffices for this proof, and Müller-Hermes and Reeb showed by another argument that data processing holds even for positive trace-preserving maps.

## 5. The equality theorem

**Theorem (Petz, 1986–88). Model proof, in finite dimensions.** With $\rho$, $\sigma$, $\mathcal N(\rho)$ and $\mathcal N(\sigma)$ faithful,

$$
D(\mathcal N(\rho)\Vert\mathcal N(\sigma))=D(\rho\Vert\sigma)
\quad\Longleftrightarrow\quad
\mathcal R_{\sigma,\mathcal N}\bigl(\mathcal N(\rho)\bigr)=\rho .
$$

*Proof.* If the Petz map recovers $\rho$, apply data processing to $\mathcal N$ and then to $\mathcal R_{\sigma,\mathcal N}$, which maps $\mathcal N(\rho)$ and $\mathcal N(\sigma)$ back to $\rho$ and $\sigma$. The two inequalities force equality.

Conversely, suppose the relative entropies are equal. The integrands of §4 are continuous in $s$ and ordered, and their integrals agree, so they agree for every $s>0$. In the chain of inequalities of the variational bound, the left supremum is attained at $\eta_s=(\Delta_2+s)^{-1}\xi_2$, and equality requires $V\eta_s$ to attain the right supremum, whose unique maximizer is $(\Delta_1+s)^{-1}\xi_1$. Therefore

$$
V(\Delta_2+s)^{-1}\xi_2=(\Delta_1+s)^{-1}\xi_1\qquad\text{for every }s>0 .
$$

In finite dimensions the functions $x\mapsto(x+s)^{-1}$ for distinct values of $s$ span all functions on the finite spectra of $\Delta_1$ and $\Delta_2$, so the identity extends to $V\,h(\Delta_2)\xi_2=h(\Delta_1)\xi_1$ for every function $h$. Take $h(x)=x^{-1/2}$. Since $\Delta_2^{-1/2}\xi_2=\widetilde\sigma^{-1/2}\widetilde\rho^{1/2}\,\widetilde\rho^{1/2}$ and $\Delta_1^{-1/2}\xi_1=\sigma^{-1/2}\rho$, the identity reads

$$
\mathcal N^\dagger(A)\,\rho^{1/2}=\sigma^{-1/2}\rho,
\qquad
A=\widetilde\sigma^{-1/2}\widetilde\rho^{1/2},
$$

that is, $\rho^{1/2}=\sigma^{1/2}\mathcal N^\dagger(A)$. Then

$$
\rho=\rho^{1/2}\bigl(\rho^{1/2}\bigr)^\dagger=\sigma^{1/2}\mathcal N^\dagger(A)\,\mathcal N^\dagger(A)^\dagger\sigma^{1/2},
\qquad
\mathcal R_{\sigma,\mathcal N}(\widetilde\rho)=\sigma^{1/2}\mathcal N^\dagger(AA^\dagger)\,\sigma^{1/2},
$$

where the second expression uses $AA^\dagger=\widetilde\sigma^{-1/2}\widetilde\rho\,\widetilde\sigma^{-1/2}$. By Kadison–Schwarz the difference $\mathcal N^\dagger(AA^\dagger)-\mathcal N^\dagger(A)\mathcal N^\dagger(A)^\dagger$ is positive, and its expectation value in $\sigma$ vanishes:

$$
\operatorname{Tr}\left[\sigma\,\mathcal N^\dagger(AA^\dagger)\right]-\operatorname{Tr}\left[\sigma\,\mathcal N^\dagger(A)\mathcal N^\dagger(A)^\dagger\right]=\operatorname{Tr}\left[\widetilde\sigma AA^\dagger\right]-\operatorname{Tr}\rho=\operatorname{Tr}\widetilde\rho-1=0 .
$$

A positive operator with zero expectation value in a faithful state vanishes, so the difference is zero and $\mathcal R_{\sigma,\mathcal N}(\widetilde\rho)=\rho$. $\square$

Note that the intermediate identity carries its own meaning. With $h(x)=x^{it}$ it reads

$$
\mathcal N^\dagger\!\left(\widetilde\sigma^{\,it}\,\widetilde\rho^{\,-it}\right)=\sigma^{it}\rho^{-it}\qquad\text{for all real }t,
$$

which is Petz's original condition (Problem 10). The operators $\sigma^{it}\rho^{-it}$ are the Connes cocycles of the pair of states, the finite form of the relative modular flow. Equality of relative entropies thus says that the adjoint channel carries the relative modular flow of the output to that of the input. Lecture 21 meets the same statement in holography, where boundary modular flow is carried to bulk modular flow.

To recover a whole code, the condition must hold for the relevant family of states, and for their extensions by a reference system when quantum information is to be preserved as well as a classical ensemble. Equality for one pair establishes recovery of that pair alone.

## 6. Worked examples

*A flagged erasure.* Let

$$
\mathcal N_p(\rho)=(1-p)\,\rho\oplus p\,|e\rangle\langle e|,\qquad 0\leq p\leq1,
$$

where the flag $|e\rangle$ is orthogonal to the retained $d$-dimensional space, and fix $\sigma=I_d/d$. On a block-diagonal output $X=X_{\mathrm{keep}}\oplus x_e$ the Petz map is $\mathcal R(X)=X_{\mathrm{keep}}+x_e\,I_d/d$: it keeps the successful output and replaces an erasure by the reference state. Therefore $\mathcal R\mathcal N_p(\rho)=(1-p)\rho+pI_d/d$, while

$$
D\bigl(\mathcal N_p(\rho)\Vert\mathcal N_p(\sigma)\bigr)=(1-p)\,D(\rho\Vert\sigma),
$$

because the two outputs have identical flag probabilities. The lost relative entropy is $pD(\rho\Vert\sigma)$, and except for $p=0$ the Petz map cannot rebuild an unknown erased state. For a pure input the recovered overlap is $1-p+p/d$. For a maximally entangled input with a $d$-dimensional reference, applying the recovered channel to one side gives the overlap $1-p+p/d^2$. The second test is stricter and detects lost quantum correlations.

*The three-qutrit code.* Take the code of Lecture 2, $V|j\rangle=3^{-1/2}\sum_k|k\rangle|k+j\rangle|k+2j\rangle$ with arithmetic modulo three, and the channel that keeps shares 1 and 2, $\mathcal N_{12}(\rho)=\operatorname{Tr}_3(V\rho V^\dagger)$. For the reference $\sigma=I/3$ the pair is maximally mixed, $\mathcal N_{12}(\sigma)=I_9/9$, and the Petz map is

$$
\mathcal R(X)=\frac13\,\mathcal N_{12}^\dagger(9X)=3\,V^\dagger(X\otimes I_3)V .
$$

For $\rho=|0\rangle\langle0|$ the pair state is $\frac13\sum_k|kk\rangle\langle kk|$, with entropy $\log3$, and $D(\mathcal N_{12}(\rho)\Vert I_9/9)=\log9-\log3=\log3=D(\rho\Vert I/3)$: the pair preserves the relative entropy, and $\mathcal R$ returns $|0\rangle\langle0|$. The same holds for every code state and for every pair, and the course scripts check it for all three pairs on random states. A single share, by contrast, is maximally mixed for every code state, so $D(\mathcal N_1(\rho)\Vert\mathcal N_1(\sigma))=0$ and nothing can be recovered. [Exact calculation.] The Petz map is thus an explicit decoder for the authorized sets of the code, obtained from the channel and the reference alone.

**Checkpoint 2.** Why is the Petz map of the three-qutrit code proportional to the adjoint of the encoding?

**Answer.** With a maximally mixed reference and a maximally mixed output of the reference, the conjugations by $\sigma^{1/2}$ and $\mathcal N_{12}(\sigma)^{-1/2}$ are multiples of the identity, and only $\mathcal N_{12}^\dagger(X)=V^\dagger(X\otimes I)V$ remains, with the factor fixed by trace preservation.

## 7. Self-study: approximate equality, approximate recovery

Junge, Renner, Sutter, Wilde and Winter proved that for every $\rho$,

$$
D(\rho\Vert\sigma)-D(\mathcal N(\rho)\Vert\mathcal N(\sigma))\geq-2\log F\bigl(\rho,\overline{\mathcal R}_{\sigma,\mathcal N}\mathcal N(\rho)\bigr),
$$

where $F(\rho,\tau)=\|\sqrt\rho\sqrt\tau\|_1$ is the root fidelity and $\overline{\mathcal R}_{\sigma,\mathcal N}$ is a universal recovery channel: an average, with an explicit probability density, of the rotated Petz maps $X\mapsto\sigma^{it}\mathcal R_{\sigma,\mathcal N}\bigl(\mathcal N(\sigma)^{-it}X\,\mathcal N(\sigma)^{it}\bigr)\sigma^{-it}$. [Stated only — refs: Junge–Renner–Sutter–Wilde–Winter 2015.] If the loss is at most $\delta$, the recovered state has root fidelity at least $e^{-\delta/2}$. The unrotated Petz map should not be credited with this bound in general without checking the theorem. The rotations are trivial when $\sigma$ and $\mathcal N(\sigma)$ are both multiples of the identity on their supports, as for the three-qutrit code, and more generally when the phases $\mathcal N(\sigma)^{it}$ act only between blocks that $\mathcal N^\dagger$ does not see. A maximally mixed $\sigma$ alone is not enough: for amplitude damping with $\sigma=I/2$ the rotated maps differ (Problem 14).

The erasure channel with $\sigma=I_d/d$ is such a case, since $\mathcal N_p(\sigma)=\frac{1-p}dI_d\oplus p$ is a multiple of the identity on each block and $\mathcal N_p^\dagger$ reads only the diagonal blocks, so every rotated Petz map equals $\mathcal R$. For a pure input, $D(\rho\Vert\sigma)=\log d$ and the loss is $p\log d$, so the bound reads $F\geq d^{-p/2}$, while the Petz map achieves $F=\sqrt{1-p+p/d}$. The function $\frac12\log(1-p+p/d)+\frac p2\log d$ vanishes at $p=0$ and at $p=1$ and is concave, so the bound holds for every $p$ and is saturated at the two ends. The figure shows both curves.

![[ads-cft-recovery-fidelity.svg|The root fidelity of the Petz recovery of a pure qubit or qutrit state after a flagged erasure with probability p, together with the universal lower bound from the loss of relative entropy; the two agree at p equal to zero and one.]]

The fidelity convention matters. With the squared fidelity $F_{\mathrm{sq}}=F^2$ the right side of the bound is $-\log F_{\mathrm{sq}}$, and mixing the two conventions introduces a factor of two. A small error for a particular state is also not a bound on a channel in the diamond norm: uniformity over states, reference dimensions and the code family must be supplied when a statement about a whole algebra is needed.

## 8. Return to regional reconstruction

For an encoding isometry $V$ and a boundary region $A$, the channel of interest is $\mathcal N_A(\rho)=\operatorname{Tr}_{\bar A}(V\rho V^\dagger)$. If it preserves the relative entropy of the logical algebra for all code states, it factors through a channel on the states of that algebra, and the algebraic version of the theorem of §5, which Cotler and collaborators develop, supplies an explicit decoder: an algebraic route to reconstruction that needs no kernel. Lecture 21 derives the needed equality, boundary relative entropy equal to bulk relative entropy, first exactly in a sector code and then semiclassically in holography, and it notes that the identity of §5 on Connes cocycles becomes the statement that boundary modular flow implements bulk modular flow. Dong, Harlow and Wall used the exact equality with operator-algebra error correction to prove entanglement-wedge reconstruction. Cotler and collaborators replaced it by the approximate equality of bulk effective field theory and used the universal recovery channel, which also gives an expression of a bulk operator as the response of the boundary modular Hamiltonian to a perturbation of the bulk state, a noncommutative form of Bayes' rule. [Stated only — refs: Dong–Harlow–Wall 2016; Cotler et al. 2017.]

This is why a relative-entropy equality is more informative than the equality of one entropy. It compares responses to changing states, and so it constrains a channel.

## 9. What to take away

- **Model proof:** in finite dimensions, data processing follows from a contraction $V$ between the Hilbert–Schmidt representations, the inequality $V^\dagger\Delta_1V\leq\Delta_2$, a variational bound on resolvents, and the integral representation of the logarithm.
- **Model proof:** Petz's theorem, $D(\mathcal N\rho\Vert\mathcal N\sigma)=D(\rho\Vert\sigma)$ if and only if $\mathcal R_{\sigma,\mathcal N}\mathcal N(\rho)=\rho$; equality also forces $\mathcal N^\dagger(\widetilde\sigma^{it}\widetilde\rho^{-it})=\sigma^{it}\rho^{-it}$, the preservation of relative modular flow.
- **Exact calculation:** a flagged erasure loses $pD(\rho\Vert\sigma)$; the three-qutrit code preserves relative entropy on every pair, where the Petz map $3V^\dagger(X\otimes I)V$ is an exact decoder, and loses all of it on a single share.
- **Stated only, checked in an example:** the universal recovery channel achieves root fidelity at least $e^{-\delta/2}$ after a loss $\delta$; for the erasure the bound $d^{-p/2}$ is saturated at $p=0$ and $p=1$.

## 10. Looking ahead

Lecture 21 turns to the channel from a code to a boundary region. It derives, in a sector code, that boundary relative entropy equals the relative entropy of the recoverable algebra, with the area-like central term cancelling, and it presents the semiclassical argument of Jafferis, Lewkowycz, Maldacena and Suh. Together with this lecture it explains the reconstruction theorem of Dong, Harlow and Wall for the entanglement wedges of Lecture 19, whose proof uses operator-algebra error correction. Lecture 26 uses the same logic for the radiation of an evaporating black hole, where the island belongs to the entanglement wedge of the radiation.

## 11. Problem set

### Classroom core

1. **The classical equality case.** Let $p(x,y)=p_Y(y)q(x|y)$. Compute the loss of relative entropy and the action of $R_q$.

2. **Petz for dephasing.** Let $\mathcal N$ remove the off-diagonal entries in a basis and let $\sigma$ be diagonal and faithful. Compute the Petz map and say which states it recovers.

3. **Erasure with a reference.** Verify the overlap $1-p+p/d^2$ for a maximally entangled input.

4. **The contraction.** Prove $\|V\|\leq1$ from the Kadison–Schwarz inequality, and show that $V\xi_2=\xi_1$ and $V^\dagger V\xi_2=\xi_2$.

5. **The variational formula.** Prove $\langle\xi,B^{-1}\xi\rangle=\sup_\eta[2\operatorname{Re}\langle\eta,\xi\rangle-\langle\eta,B\eta\rangle]$ for positive invertible $B$, and identify the unique maximizer.

6. **The three-qutrit Petz map.** Show that $\mathcal R(X)=3V^\dagger(X\otimes I)V$ for $\sigma=I/3$, and verify that it returns $|0\rangle\langle0|$ from $\mathcal N_{12}(|0\rangle\langle0|)$.

### Self-study consolidation

7. **A fidelity convention.** If the squared fidelity is used, how does the universal bound read?

8. **A useless equality.** Why does equality for $\rho=\sigma$ alone establish nothing?

9. **The logarithm as an integral.** Verify $-\log x=\int_0^\infty ds\,[(x+s)^{-1}-(1+s)^{-1}]$ for $x>0$.

10. **Petz's condition.** Show that equality of relative entropies implies $\mathcal N^\dagger(\widetilde\sigma^{it}\widetilde\rho^{-it})=\sigma^{it}\rho^{-it}$ for all real $t$.

11. **The erasure bound.** Prove $\sqrt{1-p+p/d}\geq d^{-p/2}$ for $0\leq p\leq1$.

12. **A product state.** For $\mathcal N=\operatorname{Tr}_B$, $\rho=\rho_A\otimes\tau$ and $\sigma=\sigma_A\otimes\tau$, show that equality holds and that the Petz map returns $\rho$.

### Research extension

13. **The deformed code.** Compute the Petz map numerically for the deformed code of Lecture 7 and the pair of shares 1 and 2, since shares 2 and 3 still recover exactly (Lecture 7, §3), and compare it with the explicit decoder, on entangled inputs. *Known:* the deformation destroys exact recovery, so the relative entropy decreases, and the universal bound controls the loss of fidelity. *Completion:* the loss of relative entropy and the entanglement fidelity of both decoders as functions of the deformation, with supported inverses and numerical thresholds reported.

14. **Rotated Petz maps.** For a qubit amplitude-damping channel and a non-maximally mixed reference, compare the Petz map with the universal recovery channel. *Known:* the two differ when $\sigma$ and $\mathcal N(\sigma)$ are not multiples of the identity; the universal channel always satisfies the bound of §7. *Completion:* the fidelities of both maps and the bound, as functions of the damping, for one pure input.

15. **The modular form of recovery.** Write the Petz map in terms of the modular flows of $\sigma$ and $\mathcal N(\sigma)$, and interpret the formula of Cotler and collaborators for a bulk operator as the response of a boundary modular Hamiltonian. *Known:* the rotated Petz maps are conjugations of $\mathcal R_{\sigma,\mathcal N}$ by modular flows, and their average admits an integral representation over modular time. *Completion:* the modular form checked on the three-qutrit code, for a logical operator.

## 12. Answer checkpoints

1. Every conditional relative entropy vanishes, so the loss is zero, and $R_q(p_Y)=p_Yq(x|y)=p$.

2. The Petz map is the same dephasing on the diagonal image: with $\sigma$ and $\mathcal N(\sigma)$ diagonal, $\mathcal R(X)=\operatorname{diag}(X)$. It recovers every diagonal state and no coherence.

3. The recovered channel replaces the erased half by $I_d/d$, so the state becomes $(1-p)|\Phi_d\rangle\langle\Phi_d|+p\,I_d/d\otimes I_d/d$, and $\langle\Phi_d|I_{d^2}/d^2|\Phi_d\rangle=1/d^2$.

4. The norm computation of §4 uses $\mathcal N^\dagger(X)^\dagger\mathcal N^\dagger(X)\leq\mathcal N^\dagger(X^\dagger X)$ and $\operatorname{Tr}[\rho\,\mathcal N^\dagger(Y)]=\operatorname{Tr}[\mathcal N(\rho)Y]$. With $X=I$, $V\widetilde\rho^{1/2}=\rho^{1/2}$. For a contraction, $\|V\xi\|=\|\xi\|$ gives $\langle\xi,(I-V^\dagger V)\xi\rangle=0$ with $I-V^\dagger V\geq0$, so $V^\dagger V\xi=\xi$.

5. Completing the square, $2\operatorname{Re}\langle\eta,\xi\rangle-\langle\eta,B\eta\rangle=\langle\xi,B^{-1}\xi\rangle-\langle\eta-B^{-1}\xi,B(\eta-B^{-1}\xi)\rangle$, and the last term is positive unless $\eta=B^{-1}\xi$.

6. $\sigma^{1/2}=3^{-1/2}I$ and $\mathcal N_{12}(\sigma)^{-1/2}=3I$, so $\mathcal R(X)=\frac13\mathcal N_{12}^\dagger(9X)$, and $\mathcal N_{12}^\dagger(Y)=V^\dagger(Y\otimes I)V$. For $X=\frac13\sum_k|kk\rangle\langle kk|$, only the terms with $j=0$ survive the projection onto equal first and second shares, so $(X\otimes I)V|j\rangle=\frac13\,\delta_{j0}\,V|0\rangle$ and $3V^\dagger(X\otimes I)V=|0\rangle\langle0|$.

7. $-\log F_{\mathrm{sq}}$ on the right side, since $-2\log F=-\log F^2$.

8. Both relative entropies vanish identically for every channel, so the equality carries no information about other states.

9. $\int_0^M ds\,[(x+s)^{-1}-(1+s)^{-1}]=\log\frac{x+M}{1+M}-\log x\to-\log x$ as $M\to\infty$.

10. Take $h(x)=x^{it}$ in $V\,h(\Delta_2)\xi_2=h(\Delta_1)\xi_1$. Since $\Delta^{it}$ acts as $L_{\sigma^{it}}R_{\rho^{-it}}$, $\Delta_2^{it}\xi_2=(\widetilde\sigma^{it}\widetilde\rho^{-it})\widetilde\rho^{1/2}$, whose image under $V$ is $\mathcal N^\dagger(\widetilde\sigma^{it}\widetilde\rho^{-it})\rho^{1/2}$, while $\Delta_1^{it}\xi_1=\sigma^{it}\rho^{-it}\rho^{1/2}$. Multiplying by $\rho^{-1/2}$ on the right gives the condition.

11. $f(p)=\frac12\log(1-p+p/d)+\frac p2\log d$ vanishes at $p=0$ and $p=1$, and it is concave because $\log$ of an affine function is concave. A concave function that vanishes at the endpoints is nonnegative between them.

12. $D(\rho_A\otimes\tau\Vert\sigma_A\otimes\tau)=D(\rho_A\Vert\sigma_A)$, so the partial trace preserves the relative entropy. The adjoint is $\mathcal N^\dagger(Y)=Y\otimes I$, and $\mathcal R(X)=(\sigma_A^{1/2}\otimes\tau^{1/2})(\sigma_A^{-1/2}X\sigma_A^{-1/2}\otimes I)(\sigma_A^{1/2}\otimes\tau^{1/2})=X\otimes\tau$, which returns $\rho_A\otimes\tau$ from $\rho_A$.

**Wiki connections.** [[araki-uhlmann-relative-entropy|Araki–Uhlmann relative entropy]]
