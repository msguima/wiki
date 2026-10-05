---
title: "Conventions — Geometric QCD"
type: course-note
course: geometric-qcd-course-guide
modified: 2026-10-05
---

# Conventions

## Geometry and operators

Modules I–IV use Euclidean $\mathbb R^4$, $\delta_{\mu\nu}$ and $\epsilon_{1234}=1$. For two-forms, $(*B)_{\mu\nu}=\epsilon_{\mu\nu\rho\sigma}B_{\rho\sigma}/2$ and $*^2=1$. The spinor rotating-surface example in V.5 uses Minkowski signature $(+---)$ and states that choice explicitly. Euclidean self-duality is not carried unchanged into Lorentzian signature.

The anti-Hermitian connection is $\mathcal A=igA$ when $A$ is Hermitian. Write $D=\partial+\mathcal A$, $\mathcal F=[D,D]=igF$, and Euclidean $\{\gamma_\mu,\gamma_\nu\}=2\delta_{\mu\nu}$. Define $\sigma_{\mu\nu}=[\gamma_\mu,\gamma_\nu]/2$. Then $\not D^2=D^2+\sigma_{\mu\nu}\mathcal F_{\mu\nu}/2$.

Parallel sections obey $DU=0$ and have $U=\mathcal P e^{-\int\mathcal A}$ along the stated orientation. The source's ordered covariant-derivative product and the common Wilson convention $\mathcal P e^{+ig\oint A}$ use their explicitly stated transport orientation. I.3–I.5 keep the orientation and area insertion together. Reversing one sign without the other is invalid.

## Loop quantities and color normalization

$w_C[A]=N_c^{-1}\operatorname{tr}U_C[A]$ is the unaveraged observable; $W[C]=\langle w_C[A]\rangle$. The full two-loop correlator is $\langle w_{C_1}w_{C_2}\rangle$; its connected part subtracts $W[C_1]W[C_2]$.

The worked color algebra uses $\operatorname{tr}T^aT^b=\delta^{ab}/2$ and $\lambda=g^2N_c$. In I.5 the normalized color insertion has coefficient $\lambda/2$. Source equations written with coefficient $\lambda$ have their own loop-operator normalization, denoted $\lambda_{\mathrm{loop}}$ when comparing. The induced coupling must be matched, not inferred by identifying those symbols.

I.4 defines $A_{\mu\nu}$ as an oriented, point-split antisymmetric insertion and $\Delta_\mu$ as the difference of neighboring dot derivatives. The vector operator is $\mathcal L_\nu=\Delta_\mu A_{\mu\nu}$; $L=\oint\dot C_\nu\mathcal L_\nu$. The surrounding holonomy remains inside every traced insertion.

## Fourier transforms and harmonic extension

Finite examples use $\widehat f(p)=\int e^{ipx}f(x)\,dx$, inverse measure $dp/(2\pi)$, and $\widehat{f'}=-ip\widehat f$. The coordinate Dirac kernel in V.3 uses $e^{iq\cdot\tau}$ and $d^4q/(2\pi)^4$.

For the disk, $z=u+iv$, $d^2z=du\,dv$, and $\partial_z=(\partial_u-i\partial_v)/2$. The Hilbert transform has Fourier multiplier $-i\,\operatorname{sgn}n$. Thus $H\cos n\theta=\sin n\theta$, and $f=(C+iHC)/2$ solves the fixed boundary harmonic problem. The null condition is $f'\cdot f'=0$, a bilinear square, not $|f'|^2=0$.

## Dimensions and distinct symbols

Natural units are used. A length has mass dimension $-1$; ordinary and proposed areas have dimension $-2$; $\kappa$ and string tension $\sigma$ have dimension $2$. $\sqrt\sigma$ is a mass. The quoted fit scale is $\sqrt\sigma\simeq0.417$ GeV.

The auxiliary surface-fermion mass in Module IV is not the endpoint quark mass in Module V. The RG scale $\Lambda_{\mathrm{QCD}}$ is not the spinor norm $\Lambda=\lambda^\dagger\lambda$. The metric factor $e^{2\rho}$, geometric density denoted $e$ in the source, and boundary einbein must be distinguished.

In V.6–V.7, $\mathcal E=E/\sqrt\sigma$, $x=m/\sqrt\sigma$, $K$, $\beta$, and $J$ are dimensionless. The source's stationary phase is written in these dimensionless variables throughout the worked derivation.
