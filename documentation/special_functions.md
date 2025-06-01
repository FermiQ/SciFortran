## Overview

Overview not automatically extracted.

## Key Components

### Module: `special_functions`
- **Purpose:** Overview not automatically extracted.
- **Contains:** `airya`, `airyb`, `airyzo`, `ajyik`, `aswfa`, `aswfb`, `bernoa`, `bernob`, `betaf`, `bjndd`, `cbk`, `cchg`, `cerf`, `cerror`, `cerzo`, `cfc`, `cfs`, `cgama`, `ch12n`, `chgm`, `chgu`, `chgubi`, `chguit`, `chgul`, `chgus`, `cik01`, `ciklv`, `cikna`, `ciknb`, `cikva`, `cikvb`, `cisia`, `cisib`, `cjk`, `cjy01`, `cjylv`, `cjyna`, `cjynb`, `cjyva`, `cjyvb`, `clpmn`, `clpn`, `clqmn`, `clqn`, `comelp`, `cpbdn`, `cpdla`, `cpdsa`, `cpsi`, `csphik`, `csphjy`, `cv0`, `cva1`, `cva2`, `cvf`, `cvql`, `cvqm`, `cy01`, `cyzo`, `dvla`, `dvsa`, `e1xa`, `e1xb`, `e1z`, `eix`, `elit`, `elit3`, `envj`, `enxa`, `enxb`, `werror`, `eulera`, `eulerb`, `fcoef`, `fcs`, `fcszo`, `ffk`, `gaih`, `gam0`, `gammaf`, `gmn`, `herzo`, `hygfx`, `hygfz`, `ik01a`, `ik01b`, `ikna`, `iknb`, `ikv`, `incob`, `incog`, `itairy`, `itika`, `itikb`, `itjya`, `itjyb`, `itsh0`, `itsl0`, `itth0`, `ittika`, `ittikb`, `ittjya`, `ittjyb`, `jdzo`, `jelp`, `jy01a`, `jy01b`, `jyna`, `jynb`, `jyndd`, `jyv`, `jyzo`, `klvna`, `klvnb`, `klvnzo`, `kmn`, `lagzo`, `lamn`, `lamv`, `legzo`, `lgama`, `lpmn`, `lpmns`, `lpmv`, `lpn`, `lpni`, `lqmn`, `lqmns`, `lqna`, `lqnb`, `msta1`, `msta2`, `mtu0`, `mtu12`, `othpl`, `pbdv`, `pbvv`, `pbwa`, `psi`, `qstar`, `rctj`, `rcty`, `refine`, `rmn1`, `rmn2l`, `rmn2so`, `rmn2sp`, `rswfo`, `rswfp`, `scka`, `sckb`, `sdmn`, `segv`, `sphi`, `sphj`, `sphk`, `sphy`, `stvh0`, `stvh1`, `stvhv`, `stvl0`, `stvl1`, `stvlv`, `vvla`, `vvsa`

### Subroutine: `airya`
- **Signature:** `Subroutine airya(x, ai, bi, ad, bd)`
- **Purpose:** *****************************************************************************80

  ! AIRYA computes Airy functions and their derivatives.

  Licensing:

  The original FORTRAN77 version of this routine is copyrighted by
  Shanjie Zhang and Jianming Jin.  However, they give permission to
  incorporate this routine into a user program that the copyright
  is acknowledged.

  Modified:

  30 June 2012

  Author:

  Original FORTRAN77 version by Shanjie Zhang, Jianming Jin.
  FORTRAN90 version by John Burkardt.

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument of the Airy function.

  Output, real ( kind = 8 ) AI, BI, AD, BD, the values of Ai(x), Bi(x),
  Ai'(x), Bi'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `airyb`
- **Signature:** `Subroutine airyb(x, ai, bi, ad, bd)`
- **Purpose:** *****************************************************************************80

  ! AIRYB computes Airy functions and their derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  02 June 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, argument of Airy function.

  Output, real ( kind = 8 ) AI, Ai(x).

  Output, real ( kind = 8 ) BI, Bi(x).

  Output, real ( kind = 8 ) AD, Ai'(x).

  Output, real ( kind = 8 ) BD, Bi'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `airyzo`
- **Signature:** `Subroutine airyzo(nt, kf, xa, xb, xc, xd)`
- **Purpose:** *****************************************************************************80

  ! AIRYZO computes the first NT zeros of Ai(x) and Ai'(x).

  Discussion:

  Compute the first NT zeros of Airy functions Ai(x) and Ai'(x),
  a and a', and the associated values of Ai(a') and Ai'(a); and
  the first NT zeros of Airy functions Bi(x) and Bi'(x), b and
  b', and the associated values of Bi(b') and Bi'(b).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  14 March 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) NT, the number of zeros.

  Input, integer ( kind = 4 ) KF, the function code.
  1 for Ai(x) and Ai'(x);
  2 for Bi(x) and Bi'(x).

  Output, real ( kind = 8 ) XA(m), a, the m-th zero of Ai(x) or
  b, the m-th zero of Bi(x).

  Output, real ( kind = 8 ) XB(m), a', the m-th zero of Ai'(x) or
  b', the m-th zero of Bi'(x).

  Output, real ( kind = 8 ) XC(m), Ai(a') or Bi(b').

  Output, real ( kind = 8 ) XD(m), Ai'(a) or Bi'(b)
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ajyik`
- **Signature:** `Subroutine ajyik(x, vj1, vj2, vy1, vy2, vi1, vi2, vk1, vk2)`
- **Purpose:** *****************************************************************************80

  ! AJYIK computes Bessel functions Jv(x), Yv(x), Iv(x), Kv(x).

  Discussion:

  Compute Bessel functions Jv(x) and Yv(x), and modified Bessel functions
  Iv(x) and Kv(x), and their derivatives with v = 1/3, 2/3.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  31 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.  X should not be zero.

  Output, real ( kind = 8 ) VJ1, VJ2, VY1, VY2, VI1, VI2, VK1, VK2,
  the values of J1/3(x), J2/3(x), Y1/3(x), Y2/3(x), I1/3(x), I2/3(x),
  K1/3(x), K2/3(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `aswfa`
- **Signature:** `Subroutine aswfa(m, n, c, x, kd, cv, s1f, s1d)`
- **Purpose:** *****************************************************************************80

  ! ASWFA: prolate and oblate spheroidal angular functions of the first kind.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  13 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter.

  Input, integer ( kind = 4 ) N, the mode parameter, with N = M, M+1, ...

  Input, real ( kind = 8 ) C, the spheroidal parameter.

  Input, real ( kind = 8 ) X, the argument of the angular function.
  |X| < 1.0.

  Input, integer ( kind = 4 ) KD, the function code.
  1, the prolate function.
  -1, the oblate function.

  Input, real ( kind = 8 ) CV, the characteristic value.

  Output, real ( kind = 8 ) S1F, S1D, the angular function of the first
  kind and its derivative.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `aswfb`
- **Signature:** `Subroutine aswfb(m, n, c, x, kd, cv, s1f, s1d)`
- **Purpose:** *****************************************************************************80

  ! ASWFB: prolate and oblate spheroidal angular functions of the first kind.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  20 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter, m = 0, 1, 2, ...

  Input, integer ( kind = 4 ) N, mode parameter, N = M, M+1, M+2, ...

  Input, real ( kind = 8 ) C, the spheroidal parameter.

  Input, real ( kind = 8 ) X, the argument, with |X| < 1.0.

  Input, integer ( kind = 4 ) KD, the function code.
  1, the prolate function.
  -1, the oblate function.

  Input, real ( kind = 8 ) CV, the characteristic value.

  Output, real ( kind = 8 ) S1F, S1D, the angular function of the first
  kind and its derivative.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `bernoa`
- **Signature:** `Subroutine bernoa(n, bn)`
- **Purpose:** *****************************************************************************80

  ! BERNOA computes the Bernoulli number Bn.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  11 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the index.

  Output, real ( kind = 8 ) BN, the value of the N-th Bernoulli number.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `bernob`
- **Signature:** `Subroutine bernob(n, bn)`
- **Purpose:** *****************************************************************************80

  ! BERNOB computes the Bernoulli number Bn.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  11 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the index.

  Output, real ( kind = 8 ) BN, the value of the N-th Bernoulli number.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `betaf`
- **Signature:** `Subroutine betaf(p, q, bt)`
- **Purpose:** *****************************************************************************80

  ! BETA computes the Beta function B(p,q).

  Licensing:

  The original FORTRAN77 version of this routine is copyrighted by
  Shanjie Zhang and Jianming Jin.  However, they give permission to
  incorporate this routine into a user program that the copyright
  is acknowledged.

  Modified:

  12 March 2012

  Author:

  Original FORTRAN77 version by Shanjie Zhang, Jianming Jin.
  FORTRAN90 version by John Burkardt.

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45

  Parameters:

  Input, real ( kind = 8 ) P, Q, the parameters.
  0 < P, 0 < Q.

  Output, real ( kind = 8 ) BT, the value of B(P,Q).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `bjndd`
- **Signature:** `Subroutine bjndd(n, x, bj, dj, fj)`
- **Purpose:** *****************************************************************************80

  ! BJNDD computes Bessel functions Jn(x) and first and second derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  11 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) BJ(N+1), DJ(N+1), FJ(N+1), the values of
  Jn(x), Jn'(x) and Jn''(x) in the last entries.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cbk`
- **Signature:** `Subroutine cbk(m, n, c, cv, qt, ck, bk)`
- **Purpose:** *****************************************************************************80

  ! CBK computes coefficients for oblate radial functions with small argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  20 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter;  M = 0, 1, 2, ...

  Input, integer ( kind = 4 ) N, mode parameter, N = M, M + 1, M + 2, ...

  Input, real ( kind = 8 ) C, spheroidal parameter.

  Input, real ( kind = 8 ) CV, the characteristic value.

  Input, real ( kind = 8 ) QT, ?

  Input, real ( kind = 8 ) CK(*), ?

  Output, real ( kind = 8 ) BK(*), the coefficients.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cchg`
- **Signature:** `Subroutine cchg(a, b, z, chg)`
- **Purpose:** *****************************************************************************80

  ! CCHG computes the confluent hypergeometric function.

  Discussion:

  This function computes the confluent hypergeometric function
  M(a,b,z) with real parameters a, b and complex argument z.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  26 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) A, B, parameter values.

  Input, complex ( kind = 8 ) Z, the argument.

  Output, complex ( kind = 8 ) CHG, the value of M(a,b,z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cerf`
- **Signature:** `Subroutine cerf(z, cer, cder)`
- **Purpose:** *****************************************************************************80

  ! CERF computes the error function and derivative for a complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  25 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, complex ( kind = 8 ), the argument.

  Output, complex ( kind = 8 ) CER, CDER, the values of erf(z) and erf'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cerror`
- **Signature:** `Subroutine cerror(z, cer)`
- **Purpose:** *****************************************************************************80

  ! CERROR computes the error function for a complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  15 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, complex ( kind = 8 ) Z, the argument.

  Output, complex ( kind = 8 ) CER, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cerzo`
- **Signature:** `Subroutine cerzo(nt, zo)`
- **Purpose:** *****************************************************************************80

  ! CERZO evaluates the complex zeros of the error function.

  Discussion:

  The modified Newton method is used.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  15 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) NT, the number of zeros.

  Output, complex ( kind = 8 ) ZO(NT), the zeros.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cfc`
- **Signature:** `Subroutine cfc(z, zf, zd)`
- **Purpose:** *****************************************************************************80

  ! CFC computes the complex Fresnel integral C(z) and C'(z).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  26 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, complex ( kind = 8 ) Z, the argument.

  Output, complex ( kind = 8 ) ZF, ZD, the values of C(z) and C'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cfs`
- **Signature:** `Subroutine cfs(z, zf, zd)`
- **Purpose:** *****************************************************************************80

  ! CFS computes the complex Fresnel integral S(z) and S'(z).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  24 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, complex ( kind = 8 ) Z, the argument.

  Output, complex ( kind = 8 ) ZF, ZD, the values of S(z) and S'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cgama`
- **Signature:** `Subroutine cgama(x, y, kf, gr, gi)`
- **Purpose:** *****************************************************************************80

  ! CGAMA computes the Gamma function for complex argument.

  Discussion:

  This procedcure computes the gamma function Γ(z) or ln[Γ(z)]
  for a complex argument

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  26 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, Y, the real and imaginary parts of
  the argument Z.

  Input, integer ( kind = 4 ) KF, the function code.
  0 for ln[Γ(z)]
  1 for Γ(z)

  Output, real ( kind = 8 ) GR, GI, the real and imaginary parts of
  the selected function.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ch12n`
- **Signature:** `Subroutine ch12n(n, z, nm, chf1, chd1, chf2, chd2)`
- **Purpose:** *****************************************************************************80

  ! CH12N computes Hankel functions of first and second kinds, complex argument.

  Discussion:

  Both the Hankel functions and their derivatives are computed.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  26 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of the functions.

  Input, complex ( kind = 8 ) Z, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, complex ( kind = 8 ) CHF1(0:n), CHD1(0:n), CHF2(0:n), CHD2(0:n),
  the values of Hn(1)(z), Hn(1)'(z), Hn(2)(z), Hn(2)'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `chgm`
- **Signature:** `Subroutine chgm(a, b, x, hg)`
- **Purpose:** *****************************************************************************80

  ! CHGM computes the confluent hypergeometric function M(a,b,x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  27 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) A, B, parameters.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) HG, the value of M(a,b,x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `chgu`
- **Signature:** `Subroutine chgu(a, b, x, hu, md)`
- **Purpose:** *****************************************************************************80

  ! CHGU computes the confluent hypergeometric function U(a,b,x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  27 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) A, B, parameters.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) HU, U(a,b,x).

  Output, integer ( kind = 4 ) MD, the method code.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `chgubi`
- **Signature:** `Subroutine chgubi(a, b, x, hu, id)`
- **Purpose:** *****************************************************************************80

  ! CHGUBI: confluent hypergeometric function with integer argument B.

  Discussion:

  This procedure computes the confluent hypergeometric function
  U(a,b,x) with integer ( kind = 4 ) b ( b = ±1,±2,... )

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  31 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) A, B, parameters.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) HU, the value of U(a,b,x).

  Output, integer ( kind = 4 ) ID, the estimated number of significant
  digits.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `chguit`
- **Signature:** `Subroutine chguit(a, b, x, hu, id)`
- **Purpose:** *****************************************************************************80

  ! CHGUIT computes the hypergeometric function using Gauss-Legendre integration.

  Discussion:

  This procedure computes the hypergeometric function U(a,b,x) by
  using Gaussian-Legendre integration (n = 60)

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  22 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, double precision A, B, parameters.

  Input, double precision X, the argument.

  Output, double precision HU, U(a,b,z).

  Output, integer ID, the estimated number of significant digits.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `chgul`
- **Signature:** `Subroutine chgul(a, b, x, hu, id)`
- **Purpose:** *****************************************************************************80

  ! CHGUL: confluent hypergeometric function U(a,b,x) for large argument X.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  22 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) A, B, parameters.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) HU, the value of U(a,b,x).

  Output, integer ( kind = 4 ) ID, the estimated number of
  significant digits.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `chgus`
- **Signature:** `Subroutine chgus(a, b, x, hu, id)`
- **Purpose:** *****************************************************************************80

  ! CHGUS: confluent hypergeometric function U(a,b,x) for small argument X.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  27 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) A, B, parameters.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) HU, U(a,b,x).

  Output, integer ( kind = 4 ) ID, the estimated number of
  significant digits.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cik01`
- **Signature:** `Subroutine cik01(z, cbi0, cdi0, cbi1, cdi1, cbk0, cdk0, cbk1, cdk1)`
- **Purpose:** *****************************************************************************80

  ! CIK01: modified Bessel I0(z), I1(z), K0(z) and K1(z) for complex argument.

  Discussion:

  This procedure computes the modified Bessel functions I0(z), I1(z),
  K0(z), K1(z), and their derivatives for a complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  31 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, complex ( kind = 8 ) Z, the argument.

  Output, complex ( kind = 8 ) CBI0, CDI0, CBI1, CDI1, CBK0, CDK0, CBK1,
  CDK1, the values of I0(z), I0'(z), I1(z), I1'(z), K0(z), K0'(z), K1(z),
  and K1'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ciklv`
- **Signature:** `Subroutine ciklv(v, z, cbiv, cdiv, cbkv, cdkv)`
- **Purpose:** *****************************************************************************80

  ! CIKLV: modified Bessel functions Iv(z), Kv(z), complex argument, large order.

  Discussion:

  This procedure computes modified Bessel functions Iv(z) and
  Kv(z) and their derivatives with a complex argument and a large order.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  31 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) V, the order of Iv(z) and Kv(z).

  Input, complex ( kind = 8 ) Z, the argument.

  Output, real ( kind = 8 ) CBIV, CDIV, CBKV, CDKV, the values of
  Iv(z), Iv'(z), Kv(z), Kv'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cikna`
- **Signature:** `Subroutine cikna(n, z, nm, cbi, cdi, cbk, cdk)`
- **Purpose:** *****************************************************************************80

  ! CIKNA: modified Bessel functions In(z), Kn(z), derivatives, complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  30 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of In(z) and Kn(z).

  Input, complex ( kind = 8 ) Z, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, complex ( kind = 8 ) CBI((0:N), CDI(0:N), CBK(0:N), CDK(0:N),
  the values of In(z), In'(z), Kn(z), Kn'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ciknb`
- **Signature:** `Subroutine ciknb(n, z, nm, cbi, cdi, cbk, cdk)`
- **Purpose:** *****************************************************************************80

  ! CIKNB computes complex modified Bessel functions In(z) and Kn(z).

  Discussion:

  This procedure also evaluates the derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  30 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of In(z) and Kn(z).

  Input, complex ( kind = 8 ) Z, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, complex ( kind = 8 ) CB((0:N), CDI(0:N), CBK(0:N), CDK(0:N),
  the values of In(z), In'(z), Kn(z), Kn'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cikva`
- **Signature:** `Subroutine cikva(v, z, vm, cbi, cdi, cbk, cdk)`
- **Purpose:** *****************************************************************************80

  ! CIKVA: modified Bessel functions Iv(z), Kv(z), arbitrary order, complex.

  Discussion:

  Compute the modified Bessel functions Iv(z), Kv(z)
  and their derivatives for an arbitrary order and
  complex argument

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  31 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) V, the order of the functions.

  Input, complex ( kind = 8 ) Z, the argument.

  Output, real ( kind = 8 ) VM, the highest order computed.

  Output, real ( kind = 8 ) CBI(0:N), CDI(0:N), CBK(0:N), CDK(0:N),
  the values of In+v0(z), In+v0'(z), Kn+v0(z), Kn+v0'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cikvb`
- **Signature:** `Subroutine cikvb(v, z, vm, cbi, cdi, cbk, cdk)`
- **Purpose:** *****************************************************************************80

  ! CIKVB: modified Bessel functions,Iv(z), Kv(z), arbitrary order, complex.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  02 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) V, the order of the functions.

  Input, complex ( kind = 8 ) Z, the argument.

  Output, real ( kind = 8 ) VM, the highest order computed.

  Output, real ( kind = 8 ) CBI(0:N), CDI(0:N), CBK(0:N), CDK(0:N),
  the values of In+v0(z), In+v0'(z), Kn+v0(z), Kn+v0'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cisia`
- **Signature:** `Subroutine cisia(x, ci, si)`
- **Purpose:** *****************************************************************************80

  ! CISIA computes cosine Ci(x) and sine integrals Si(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  03 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument of Ci(x) and Si(x).

  Output, real ( kind = 8 ) CI, SI, the values of Ci(x) and Si(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cisib`
- **Signature:** `Subroutine cisib(x, ci, si)`
- **Purpose:** *****************************************************************************80

  ! CISIB computes cosine and sine integrals.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  20 March 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument of Ci(x) and Si(x).

  Output, real ( kind = 8 ) CI, SI, the values of Ci(x) and Si(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cjk`
- **Signature:** `Subroutine cjk(km, a)`
- **Purpose:** *****************************************************************************80

  ! CJK: asymptotic expansion coefficients for Bessel functions of large order.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  01 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) KM, the maximum value of K.

  Output, real ( kind = 8 ) A(L), the value of Cj(k) where j and k are
  related to L by L = j+1+[k*(k+1)]/2; j,k = 0,1,...,Km.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cjy01`
- **Signature:** `Subroutine cjy01(z, cbj0, cdj0, cbj1, cdj1, cby0, cdy0, cby1, cdy1)`
- **Purpose:** *****************************************************************************80

  ! CJY01: complexBessel functions, derivatives, J0(z), J1(z), Y0(z), Y1(z).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  02 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, complex ( kind = 8 ) Z, the argument.

  Output, complex ( kind = 8 ) CBJ0, CDJ0, CBJ1, CDJ1, CBY0, CDY0, CBY1,
  CDY1, the values of J0(z), J0'(z), J1(z), J1'(z), Y0(z), Y0'(z),
  Y1(z), Y1'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cjylv`
- **Signature:** `Subroutine cjylv(v, z, cbjv, cdjv, cbyv, cdyv)`
- **Purpose:** *****************************************************************************80

  ! CJYLV: Bessel functions Jv(z), Yv(z) of complex argument and large order v.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  25 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) V, the order of Jv(z) and Yv(z).

  Input, complex ( kind = 8 ) Z, the argument.

  Output, complex ( kind = 8 ) CBJV, CDJV, CBYV, CDYV, the values of Jv(z),
  Jv'(z), Yv(z), Yv'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cjyna`
- **Signature:** `Subroutine cjyna(n, z, nm, cbj, cdj, cby, cdy)`
- **Purpose:** *****************************************************************************80

  ! CJYNA: Bessel functions and derivatives, Jn(z) and Yn(z) of complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  02 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of Jn(z) and Yn(z).

  Input, complex ( kind = 8 ) Z, the argument of Jn(z) and Yn(z).

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, complex ( kind = 8 ), CBJ(0:N), CDJ(0:N), CBY(0:N), CDY(0:N),
  the values of Jn(z), Jn'(z), Yn(z), Yn'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cjynb`
- **Signature:** `Subroutine cjynb(n, z, nm, cbj, cdj, cby, cdy)`
- **Purpose:** *****************************************************************************80

  ! CJYNB: Bessel functions, derivatives, Jn(z) and Yn(z) of complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  03 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of Jn(z) and Yn(z).

  Input, complex ( kind = 8 ) Z, the argument of Jn(z) and Yn(z).

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, complex ( kind = 8 ) CBJ(0:N), CDJ(0:N), CBY(0:N), CDY(0:N),
  the values of Jn(z), Jn'(z), Yn(z), Yn'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cjyva`
- **Signature:** `Subroutine cjyva(v, z, vm, cbj, cdj, cby, cdy)`
- **Purpose:** *****************************************************************************80

  ! CJYVA: Bessel functions and derivatives, Jv(z) and Yv(z) of complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  03 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) V, the order of Jv(z) and Yv(z).

  Input, complex ( kind = 8 ), the argument.

  Output, real ( kind = 8 ) VM, the highest order computed.

  Output, real ( kind = 8 ) CBJ(0:*), CDJ(0:*), CBY(0:*), CDY(0:*),
  the values of Jn+v0(z), Jn+v0'(z), Yn+v0(z), Yn+v0'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cjyvb`
- **Signature:** `Subroutine cjyvb(v, z, vm, cbj, cdj, cby, cdy)`
- **Purpose:** *****************************************************************************80

  ! CJYVB: Bessel functions and derivatives, Jv(z) and Yv(z) of complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  03 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) V, the order of Jv(z) and Yv(z).

  Input, complex ( kind = 8 ) Z, the argument.

  Output, real ( kind = 8 ) VM, the highest order computed.

  Output, real ( kind = 8 ) CBJ(0:*), CDJ(0:*), CBY(0:*), CDY(0:*),
  the values of Jn+v0(z), Jn+v0'(z), Yn+v0(z), Yn+v0'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `clpmn`
- **Signature:** `Subroutine clpmn(mm, m, n, x, y, cpm, cpd)`
- **Purpose:** *****************************************************************************80

  ! CLPMN: associated Legendre functions and derivatives for complex argument.

  Discussion:

  Compute the associated Legendre functions Pmn(z)
  and their derivatives Pmn'(z) for a complex argument

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  01 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) MM, the physical dimension of CPM and CPD.

  Input, integer ( kind = 4 ) M, N, the order and degree of Pmn(z).

  Input, real ( kind = 8 ) X, Y, the real and imaginary parts of
  the argument Z.

  Output, complex ( kind = 8 ) CPM(0:MM,0:N), CPD(0:MM,0:N), the values of
  Pmn(z) and Pmn'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `clpn`
- **Signature:** `Subroutine clpn(n, x, y, cpn, cpd)`
- **Purpose:** *****************************************************************************80

  ! CLPN computes Legendre functions and derivatives for complex argument.

  Discussion:

  Compute Legendre polynomials Pn(z) and their derivatives Pn'(z) for
  a complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  15 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the degree.

  Input, real ( kind = 8 ) X, Y, the real and imaginary parts
  of the argument.

  Output, complex ( kind = 8 ) CPN(0:N), CPD(0:N), the values of Pn(z)
  and Pn'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `clqmn`
- **Signature:** `Subroutine clqmn(mm, m, n, x, y, cqm, cqd)`
- **Purpose:** *****************************************************************************80

  ! CLQMN: associated Legendre functions and derivatives for complex argument.

  Discussion:

  This procedure computes the associated Legendre functions of the second
  kind, Qmn(z) and Qmn'(z), for a complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  02 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) MM, the physical dimension of CQM and CQD.

  Input, integer ( kind = 4 ) M, N, the order and degree of Qmn(z).

  Input, real ( kind = 8 ) X, Y, the real and imaginary parts of the
  argument Z.

  Output, complex ( kind = 8 ) CQM(0:MM,0:N), CQD(0:MM,0:N), the values of
  Qmn(z) and Qmn'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `clqn`
- **Signature:** `Subroutine clqn(n, x, y, cqn, cqd)`
- **Purpose:** *****************************************************************************80

  ! CLQN: Legendre function Qn(z) and derivative Wn'(z) for complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  01 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the degree of Qn(z).

  Input, real ( kind = 8 ) X, Y, the real and imaginary parts of the
  argument Z.

  Output, complex ( kind = 8 ) CQN(0:N), CQD(0:N), the values of Qn(z)
  and Qn'(z.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `comelp`
- **Signature:** `Subroutine comelp(hk, ck, ce)`
- **Purpose:** *****************************************************************************80

  ! COMELP computes complete elliptic integrals K(k) and E(k).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  07 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) HK, the modulus.  0 <= HK <= 1.

  Output, real ( kind = 8 ) CK, CE, the values of K(HK) and E(HK).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cpbdn`
- **Signature:** `Subroutine cpbdn(n, z, cpb, cpd)`
- **Purpose:** *****************************************************************************80

  ! CPBDN: parabolic cylinder function Dn(z) and Dn'(z) for complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  29 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order.

  Input, complex ( kind = 8 ) Z, the argument.

  Output, complex ( kind = 8 ) CPB(0:N), CPD(0:N), the values of Dn(z)
  and Dn'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cpdla`
- **Signature:** `Subroutine cpdla(n, z, cdn)`
- **Purpose:** ****************************************************************************80

  ! CPDLA computes complex parabolic cylinder function Dn(z) for large argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  07 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer N, the order.

  Input, complex ( kind = 8 ) Z, the argument.

  Output, complex ( kind = 8 ) CDN, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cpdsa`
- **Signature:** `Subroutine cpdsa(n, z, cdn)`
- **Purpose:** *****************************************************************************80

  ! CPDSA computes complex parabolic cylinder function Dn(z) for small argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  29 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order.

  Input, complex ( kind = 8 ) Z, the argument.

  Output, complex ( kind = 8 ) CDN, the value of DN(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cpsi`
- **Signature:** `Subroutine cpsi(x, y, psr, psi)`
- **Purpose:** *****************************************************************************80

  ! CPSI computes the psi function for a complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  16 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, Y, the real and imaginary parts
  of the argument.

  Output, real ( kind = 8 ) PSR, PSI, the real and imaginary parts
  of the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `csphik`
- **Signature:** `Subroutine csphik(n, z, nm, csi, cdi, csk, cdk)`
- **Purpose:** *****************************************************************************80

  ! CSPHIK: complex modified spherical Bessel functions and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  29 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of in(z) and kn(z).

  Input, complex ( kind = 8 ) Z, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, complex ( kind = 8 ) CSI(0:N), CDI(0:N), CSK(0:N), CDK(0:N),
  the values of in(z), in'(z), kn(z), kn'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `csphjy`
- **Signature:** `Subroutine csphjy(n, z, nm, csj, cdj, csy, cdy)`
- **Purpose:** *****************************************************************************80

  ! CSPHJY: spherical Bessel functions jn(z) and yn(z) for complex argument.

  Discussion:

  This procedure computes spherical Bessel functions jn(z) and yn(z)
  and their derivatives for a complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  01 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of jn(z) and yn(z).

  Input, complex ( kind = 8 ) Z, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, complex ( kind = 8 ) CSJ(0:N0, CDJ(0:N), CSY(0:N), CDY(0:N),
  the values of jn(z), jn'(z), yn(z), yn'(z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cv0`
- **Signature:** `Subroutine cv0(kd, m, q, a0)`
- **Purpose:** *****************************************************************************80

  ! CV0 computes the initial characteristic value of Mathieu functions.

  Discussion:

  This procedure computes the initial characteristic value of Mathieu
  functions for m <= 12 or q <= 300 or q <= m*m.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  03 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) KD, the case code:
  1, for cem(x,q)  ( m = 0,2,4,...)
  2, for cem(x,q)  ( m = 1,3,5,...)
  3, for sem(x,q)  ( m = 1,3,5,...)
  4, for sem(x,q)  ( m = 2,4,6,...)

  Input, integer ( kind = 4 ) M, the order of the functions.

  Input, real ( kind = 8 ) Q, the parameter of the functions.

  Output, real ( kind = 8 ) A0, the characteristic value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cva1`
- **Signature:** `Subroutine cva1(kd, m, q, cv)`
- **Purpose:** *****************************************************************************80

  ! CVA1 computes a sequence of characteristic values of Mathieu functions.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  25 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) KD, the case code.
  1, for cem(x,q)  ( m = 0,2,4,... )
  2, for cem(x,q)  ( m = 1,3,5,... )
  3, for sem(x,q)  ( m = 1,3,5,... )
  4, for sem(x,q)  ( m = 2,4,6,... )

  Input, integer ( kind = 4 ) M, the maximum order of the Mathieu functions.

  Input, real ( kind = 8 ) Q, the parameter of the Mathieu functions.

  Output, real ( kind = 8 ) CV(*), characteristic values.
  For KD = 1, CV(1), CV(2), CV(3),..., correspond to
  the characteristic values of cem for m = 0,2,4,...
  For KD = 2, CV(1), CV(2), CV(3),..., correspond to
  the characteristic values of cem for m = 1,3,5,...
  For KD = 3, CV(1), CV(2), CV(3),..., correspond to
  the characteristic values of sem for m = 1,3,5,...
  For KD = 4, CV(1), CV(2), CV(3),..., correspond to
  the characteristic values of sem for m = 0,2,4,...
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cva2`
- **Signature:** `Subroutine cva2(kd, m, q, a)`
- **Purpose:** *****************************************************************************80

  ! CVA2 computes a specific characteristic value of Mathieu functions.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  22 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) KD, the case code:
  1, for cem(x,q)  ( m = 0,2,4,...)
  2, for cem(x,q)  ( m = 1,3,5,...)
  3, for sem(x,q)  ( m = 1,3,5,...)
  4, for sem(x,q)  ( m = 2,4,6,...)

  Input, integer ( kind = 4 ) M, the order of the Mathieu functions.

  Input, real ( kind = 8 ) Q, the parameter of the Mathieu functions.

  Output, real ( kind = 8 ) A, the characteristic value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cvf`
- **Signature:** `Subroutine cvf(kd, m, q, a, mj, f)`
- **Purpose:** *****************************************************************************80

  ! CVF computes F for the characteristic equation of Mathieu functions.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  16 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) KD, the case code:
  1, for cem(x,q)  ( m = 0,2,4,...)
  2, for cem(x,q)  ( m = 1,3,5,...)
  3, for sem(x,q)  ( m = 1,3,5,...)
  4, for sem(x,q)  ( m = 2,4,6,...)

  Input, integer ( kind = 4 ) M, the order of the Mathieu functions.

  Input, real ( kind = 8 ) Q, the parameter of the Mathieu functions.

  Input, real ( kind = 8 ) A, the characteristic value.

  Input, integer ( kind = 4 ) MJ, ?

  Output, real ( kind = 8 ) F, the value of the function for the
  characteristic equation.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cvql`
- **Signature:** `Subroutine cvql(kd, m, q, a0)`
- **Purpose:** *****************************************************************************80

  ! CVQL computes the characteristic value of Mathieu functions for q <= 3*m.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  10 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) KD, the case code:
  1, for cem(x,q)  ( m = 0,2,4,...)
  2, for cem(x,q)  ( m = 1,3,5,...)
  3, for sem(x,q)  ( m = 1,3,5,...)
  4, for sem(x,q)  ( m = 2,4,6,...)

  Input, integer ( kind = 4 ) M, the order of the Mathieu functions.

  Input, real ( kind = 8 ) Q, the parameter value.

  Output, real ( kind = 8 ) A0, the initial characteristic value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cvqm`
- **Signature:** `Subroutine cvqm(m, q, a0)`
- **Purpose:** *****************************************************************************80

  ! CVQM computes the characteristic value of Mathieu functions for q <= m*m.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  07 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the order of the Mathieu functions.

  Input, real ( kind = 8 ) Q, the parameter value.

  Output, real ( kind = 8 ) A0, the initial characteristic value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cy01`
- **Signature:** `Subroutine cy01(kf, z, zf, zd)`
- **Purpose:** *****************************************************************************80

  ! CY01 computes complex Bessel functions Y0(z) and Y1(z) and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  01 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer KF, the function choice.
  0 for ZF = Y0(z) and ZD = Y0'(z);
  1 for ZF = Y1(z) and ZD = Y1'(z);
  2 for ZF = Y1'(z) and ZD = Y1''(z).

  Input, complex ( kind = 8 ) Z, the argument.

  Output, complex ( kind = 8 ) ZF, ZD, the values of the requested function
  and derivative.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cyzo`
- **Signature:** `Subroutine cyzo(nt, kf, kc, zo, zv)`
- **Purpose:** *****************************************************************************80

  ! CYZO computes zeros of complex Bessel functions Y0(z) and Y1(z) and Y1'(z).

  Parameters:

  Ths procedure computes the complex zeros of Y0(z), Y1(z) and Y1'(z),
  and their associated values at the zeros using the modified Newton's
  iteration method.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  22 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) NT, the number of zeros.

  Input, integer ( kind = 4 ) KF, the function choice.
  0 for Y0(z) and Y1(z0);
  1 for Y1(z) and Y0(z1);
  2 for Y1'(z) and Y1(z1').

  Input, integer ( kind = 4 ) KC, complex/real choice.
  0, for complex roots;
  1, for real roots.

  Output, real ( kind = 8 ) ZO(NT), ZV(NT), the zeros of Y0(z) or Y1(z)
  or Y1'(z), and the value of Y0'(z) or Y1'(z) or Y1(z) at the L-th zero.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `dvla`
- **Signature:** `Subroutine dvla(va, x, pd)`
- **Purpose:** *****************************************************************************80

  ! DVLA computes parabolic cylinder functions Dv(x) for large argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  06 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Input, real ( kind = 8 ) VA, the order.

  Output, real ( kind = 8 ) PD, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `dvsa`
- **Signature:** `Subroutine dvsa(va, x, pd)`
- **Purpose:** *****************************************************************************80

  ! DVSA computes parabolic cylinder functions Dv(x) for small argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  07 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) VA, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) PD, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `e1xa`
- **Signature:** `Subroutine e1xa(x, e1)`
- **Purpose:** *****************************************************************************80

  ! E1XA computes the exponential integral E1(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  06 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) E1, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `e1xb`
- **Signature:** `Subroutine e1xb(x, e1)`
- **Purpose:** *****************************************************************************80

  ! E1XB computes the exponential integral E1(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  06 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) E1, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `e1z`
- **Signature:** `Subroutine e1z(z, ce1)`
- **Purpose:** *****************************************************************************80

  ! E1Z computes the complex exponential integral E1(z).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  16 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, complex ( kind = 8 ) Z, the argument.

  Output, complex ( kind = 8 ) CE1, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `eix`
- **Signature:** `Subroutine eix(x, ei)`
- **Purpose:** *****************************************************************************80

  ! EIX computes the exponential integral Ei(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  10 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) EI, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `elit`
- **Signature:** `Subroutine elit(hk, phi, fe, ee)`
- **Purpose:** *****************************************************************************80

  ! ELIT: complete and incomplete elliptic integrals F(k,phi) and E(k,phi).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  12 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) HK, the modulus, between 0 and 1.

  Input, real ( kind = 8 ) PHI, the argument in degrees.

  Output, real ( kind = 8 ) FE, EE, the values of F(k,phi) and E(k,phi).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `elit3`
- **Signature:** `Subroutine elit3(phi, hk, c, el3)`
- **Purpose:** *****************************************************************************80

  ! ELIT3 computes the elliptic integral of the third kind.

  Discussion:

  Gauss-Legendre quadrature is used.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  14 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) PHI, the argument in degrees.

  Input, real ( kind = 8 ) HK, the modulus, between 0 and 1.

  Input, real ( kind = 8 ) C, the parameter, between 0 and 1.

  Output, real ( kind = 8 ) EL3, the value of the elliptic integral
  of the third kind.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `envj`
- **Signature:** `Function envj(n, x)`
- **Purpose:** *****************************************************************************80

  ! ENVJ is a utility function used by MSTA1 and MSTA2.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  14 March 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, ?

  Input, real ( kind = 8 ) X, ?

  Output, real ( kind = 8 ) ENVJ, ?
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `enxa`
- **Signature:** `Subroutine enxa(n, x, en)`
- **Purpose:** *****************************************************************************80

  ! ENXA computes the exponential integral En(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  07 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) EN(0:N), the function values.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `enxb`
- **Signature:** `Subroutine enxb(n, x, en)`
- **Purpose:** *****************************************************************************80

  ! ENXB computes the exponential integral En(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  10 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) EN(0:N), the function values.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `werror`
- **Signature:** `Subroutine werror(x, err)`
- **Purpose:** *****************************************************************************80

  ! WERROR evaluates the error function.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  07 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) ERR, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `eulera`
- **Signature:** `Subroutine eulera(n, en)`
- **Purpose:** *****************************************************************************80

  ! EULERA computes the Euler number En.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  10 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the index of the highest value to compute.

  Output, real ( kind = 8 ) EN(0:N), the Euler numbers up to the N-th value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `eulerb`
- **Signature:** `Subroutine eulerb(n, en)`
- **Purpose:** *****************************************************************************80

  ! EULERB computes the Euler number En.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  09 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the index of the highest value to compute.

  Output, real ( kind = 8 ) EN(0:N), the Euler numbers up to the N-th value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `fcoef`
- **Signature:** `Subroutine fcoef(kd, m, q, a, fc)`
- **Purpose:** *****************************************************************************80

  ! FCOEF: expansion coefficients for Mathieu and modified Mathieu functions.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  01 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) KD, the case code.
  1, for cem(x,q)  ( m = 0,2,4,...)
  2, for cem(x,q)  ( m = 1,3,5,...)
  3, for sem(x,q)  ( m = 1,3,5,...)
  4, for sem(x,q)  ( m = 2,4,6,...)

  Input, integer ( kind = 4 ) M, the order of the Mathieu function.

  Input, real ( kind = 8 ) Q, the parameter of the Mathieu functions.

  Input, real ( kind = 8 ) A, the characteristic value of the Mathieu
  functions for given m and q.

  Output, real ( kind = 8 ) FC(*), the expansion coefficients of Mathieu
  functions ( k =  1,2,...,KM ).  FC(1),FC(2),FC(3),... correspond to
  A0,A2,A4,... for KD = 1 case,
  A1,A3,A5,... for KD = 2 case,
  B1,B3,B5,... for KD = 3 case,
  B2,B4,B6,... for KD = 4 case.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `fcs`
- **Signature:** `Subroutine fcs(x, c, s)`
- **Purpose:** *****************************************************************************80

  ! FCS computes Fresnel integrals C(x) and S(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  17 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) C, S, the function values.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `fcszo`
- **Signature:** `Subroutine fcszo(kf, nt, zo)`
- **Purpose:** *****************************************************************************80

  ! FCSZO computes complex zeros of Fresnel integrals C(x) or S(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  17 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) KF, the function code.
  1 for C(z);
  2 for S(z)

  Input, integer ( kind = 4 ) NT, the total number of zeros desired.

  Output, complex ( kind = 8 ) Z0(NT), the zeros.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ffk`
- **Signature:** `Subroutine ffk(ks, x, fr, fi, fm, fa, gr, gi, gm, ga)`
- **Purpose:** *****************************************************************************80

  ! FFK computes modified Fresnel integrals F+/-(x) and K+/-(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  23 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) KS, the sign code.
  0, to calculate F+(x) and K+(x);
  1, to calculate F_(x) and K_(x).

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) FR, FI, FM, FA, the values of
  Re[F+/-(x)], Im[F+/-(x)], |F+/-(x)|, Arg[F+/-(x)]  (Degs.).

  Output, real ( kind = 8 ) GR, GI, GM, GA, the values of
  Re[K+/-(x)], Im[K+/-(x)], |K+/-(x)|, Arg[K+/-(x)]  (Degs.).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `gaih`
- **Signature:** `Subroutine gaih(x, ga)`
- **Purpose:** *****************************************************************************80

  ! GAIH computes the GammaH function.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  09 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) GA, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `gam0`
- **Signature:** `Subroutine gam0(x, ga)`
- **Purpose:** *****************************************************************************80

  ! GAM0 computes the Gamma function for the LAMV function.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  09 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) GA, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `gammaf`
- **Signature:** `Subroutine gammaf(x, ga)`
- **Purpose:** *****************************************************************************80

  ! GAMMA evaluates the Gamma function.

  Licensing:

  The original FORTRAN77 version of this routine is copyrighted by
  Shanjie Zhang and Jianming Jin.  However, they give permission to
  incorporate this routine into a user program that the copyright
  is acknowledged.

  Modified:

  08 September 2007

  Author:

  Original FORTRAN77 version by Shanjie Zhang, Jianming Jin.
  FORTRAN90 version by John Burkardt.

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45

  Parameters:

  Input, real ( kind = 8 ) X, the argument.
  X must not be 0, or any negative integer.

  Output, real ( kind = 8 ) GA, the value of the Gamma function.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `gmn`
- **Signature:** `Subroutine gmn(m, n, c, x, bk, gf, gd)`
- **Purpose:** *****************************************************************************80

  ! GMN computes quantities for oblate radial functions with small argument.

  Discussion:

  This procedure computes Gmn(-ic,ix) and its derivative for oblate
  radial functions with a small argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  15 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter;  M = 0, 1, 2, ...

  Input, integer ( kind = 4 ) N, mode parameter, N = M, M + 1, M + 2, ...

  Input, real ( kind = 8 ) C, spheroidal parameter.

  Input, real ( kind = 8 ) X, the argument.

  Input, real ( kind = 8 ) BK(*), coefficients.

  Output, real ( kind = 8 ) GF, GD, the value of Gmn(-C,X) and Gmn'(-C,X).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `herzo`
- **Signature:** `Subroutine herzo(n, x, w)`
- **Purpose:** *****************************************************************************80

  ! HERZO computes the zeros the Hermite polynomial Hn(x).

  Discussion:

  This procedure computes the zeros of Hermite polynomial Ln(x)
  in the interval [-1,+1], and the corresponding
  weighting coefficients for Gauss-Hermite integration.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  15 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of the polynomial.

  Output, real ( kind = 8 ) X(N), the zeros.

  Output, real ( kind = 8 ) W(N), the corresponding weights.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `hygfx`
- **Signature:** `Subroutine hygfx(a, b, c, x, hf)`
- **Purpose:** *****************************************************************************80

  ! HYGFX evaluates the hypergeometric function F(A,B,C,X).

  Licensing:

  The original FORTRAN77 version of this routine is copyrighted by
  Shanjie Zhang and Jianming Jin.  However, they give permission to
  incorporate this routine into a user program that the copyright
  is acknowledged.

  Modified:

  08 September 2007

  Author:

  Original FORTRAN77 version by Shanjie Zhang, Jianming Jin.
  FORTRAN90 version by John Burkardt.

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45

  Parameters:

  Input, real ( kind = 8 ) A, B, C, X, the arguments of the function.
  C must not be equal to a nonpositive integer.
  X < 1.

  Output, real HF, the value of the function.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `hygfz`
- **Signature:** `Subroutine hygfz(a, b, c, z, zhf)`
- **Purpose:** *****************************************************************************80

  ! HYGFZ computes the hypergeometric function F(a,b,c,x) for complex argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  03 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) A, B, C, parameters.

  Input, complex ( kind = 8 ) Z, the argument.

  Output, complex ( kind = 8 ) ZHF, the value of F(a,b,c,z).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ik01a`
- **Signature:** `Subroutine ik01a(x, bi0, di0, bi1, di1, bk0, dk0, bk1, dk1)`
- **Purpose:** *****************************************************************************80

  ! IK01A compute Bessel function I0(x), I1(x), K0(x), and K1(x).

  Discussion:

  This procedure computes modified Bessel functions I0(x), I1(x),
  K0(x) and K1(x), and their derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  16 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) BI0, DI0, BI1, DI1, BK0, DK0, BK1, DK1, the
  values of I0(x), I0'(x), I1(x), I1'(x), K0(x), K0'(x), K1(x), K1'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ik01b`
- **Signature:** `Subroutine ik01b(x, bi0, di0, bi1, di1, bk0, dk0, bk1, dk1)`
- **Purpose:** *****************************************************************************80

  ! IK01B: Bessel functions I0(x), I1(x), K0(x), and K1(x) and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  17 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) BI0, DI0, BI1, DI1, BK0, DK0, BK1, DK1, the
  values of I0(x), I0'(x), I1(x), I1'(x), K0(x), K0'(x), K1(x), K1'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ikna`
- **Signature:** `Subroutine ikna(n, x, nm, bi, di, bk, dk)`
- **Purpose:** *****************************************************************************80

  ! IKNA compute Bessel function In(x) and Kn(x), and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  16 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of In(x) and Kn(x).

  Input, real ( kind = 8 ) X, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, real ( kind = 8 ) BI(0:N), DI(0:N), BK(0:N), DK(0:N),
  the values of In(x), In'(x), Kn(x), Kn'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `iknb`
- **Signature:** `Subroutine iknb(n, x, nm, bi, di, bk, dk)`
- **Purpose:** *****************************************************************************80

  ! IKNB compute Bessel function In(x) and Kn(x).

  Discussion:

  Compute modified Bessel functions In(x) and Kn(x),
  and their derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  17 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of In(x) and Kn(x).

  Input, real ( kind = 8 ) X, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, real ( kind = 8 ) BI(0:N), DI(0:N), BK(0:N), DK(0:N),
  the values of In(x), In'(x), Kn(x), Kn'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ikv`
- **Signature:** `Subroutine ikv(v, x, vm, bi, di, bk, dk)`
- **Purpose:** *****************************************************************************80

  ! IKV compute modified Bessel function Iv(x) and Kv(x) and their derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  17 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) V, the order of Iv(x) and Kv(x).
  V = N + V0.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) VM, the highest order computed.

  Output, real ( kind = 8 ) BI(0:N), DI(0:N), BK(0:N), DK(0:N), the
  values of In+v0(x), In+v0'(x), Kn+v0(x), Kn+v0'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `incob`
- **Signature:** `Subroutine incob(a, b, x, bix)`
- **Purpose:** *****************************************************************************80

  ! INCOB computes the incomplete beta function Ix(a,b).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  22 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) A, B, parameters.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) BIX, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `incog`
- **Signature:** `Subroutine incog(a, x, gin, gim, gip)`
- **Purpose:** *****************************************************************************80

  ! INCOG computes the incomplete gamma function r(a,x), Γ(a,x), P(a,x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  22 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) A, the parameter.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) GIN, GIM, GIP, the values of
  r(a,x), Γ(a,x), P(a,x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `itairy`
- **Signature:** `Subroutine itairy(x, apt, bpt, ant, bnt)`
- **Purpose:** ****************************************************************************80

  ! ITAIRY computes the integrals of Airy functions.

  Discussion:

  Compute the integrals of Airy functions with respect to t,
  from 0 and x.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  19 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the upper limit of the integral.

  Output, real ( kind = 8 ) APT, BPT, ANT, BNT, the integrals, from 0 to x,
  of Ai(t), Bi(t), Ai(-t), and Bi(-t).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `itika`
- **Signature:** `Subroutine itika(x, ti, tk)`
- **Purpose:** *****************************************************************************80

  ! ITIKA computes the integral of the modified Bessel functions I0(t) and K0(t).

  Discussion:

  This procedure integrates modified Bessel functions I0(t) and
  K0(t) with respect to t from 0 to x.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  18 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the upper limit of the integral.

  Output, real ( kind = 8 ) TI, TK, the integrals of I0(t) and K0(t)
  from 0 to X.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `itikb`
- **Signature:** `Subroutine itikb(x, ti, tk)`
- **Purpose:** *****************************************************************************80

  ! ITIKB computes the integral of the Bessel functions I0(t) and K0(t).

  Discussion:

  This procedure integrates Bessel functions I0(t) and K0(t)
  with respect to t from 0 to x.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  24 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the upper limit of the integral.

  Output, real ( kind = 8 ) TI, TK, the integral of I0(t) and K0(t)
  from 0 to X.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `itjya`
- **Signature:** `Subroutine itjya(x, tj, ty)`
- **Purpose:** *****************************************************************************80

  ! ITJYA computes integrals of Bessel functions J0(t) and Y0(t).

  Discussion:

  This procedure integrates Bessel functions J0(t) and Y0(t) with
  respect to t from 0 to x.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  25 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the upper limit of the integral.

  Output, real ( kind = 8 ) TJ, TY, the integrals of J0(t) and Y0(t)
  from 0 to x.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `itjyb`
- **Signature:** `Subroutine itjyb(x, tj, ty)`
- **Purpose:** *****************************************************************************80

  ! ITJYB computes integrals of Bessel functions J0(t) and Y0(t).

  Discussion:

  This procedure integrates Bessel functions J0(t) and Y0(t)
  with respect to t from 0 to x.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  25 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the upper limit of the integral.

  Output, real ( kind = 8 ) TJ, TY, the integrals of J0(t) and Y0(t)
  from 0 to x.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `itsh0`
- **Signature:** `Subroutine itsh0(x, th0)`
- **Purpose:** *****************************************************************************80

  ! ITSH0 integrates the Struve function H0(t) from 0 to x.

  Discussion:

  This procedure evaluates the integral of Struve function
  H0(t) with respect to t from 0 and x.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  25 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the upper limit of the integral.

  Output, real ( kind = 8 ) TH0, the integral of H0(t) from 0 to x.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `itsl0`
- **Signature:** `Subroutine itsl0(x, tl0)`
- **Purpose:** *****************************************************************************80

  ! ITSL0 integrates the Struve function L0(t) from 0 to x.

  Discussion:

  This procedure evaluates the integral of modified Struve function
  L0(t) with respect to t from 0 to x.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  31 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the upper limit of the integral.

  Output, real ( kind = 8 ) TL0, the integral of L0(t) from 0 to x.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `itth0`
- **Signature:** `Subroutine itth0(x, tth)`
- **Purpose:** *****************************************************************************80

  ! ITTH0 integrates H0(t)/t from x to oo.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  23 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the lower limit of the integral.

  Output, real ( kind = 8 ) TTH, the integral of H0(t)/t from x to oo.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ittika`
- **Signature:** `Subroutine ittika(x, tti, ttk)`
- **Purpose:** *****************************************************************************80

  ! ITTIKA integrates (I0(t)-1)/t from 0 to x, K0(t)/t from x to infinity.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  23 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the integral limit.

  Output, real ( kind = 8 ) TTI, TTK, the integrals of [I0(t)-1]/t
  from 0 to x, and of K0(t)/t from x to oo.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ittikb`
- **Signature:** `Subroutine ittikb(x, tti, ttk)`
- **Purpose:** *****************************************************************************80

  ! ITTIKB integrates (I0(t)-1)/t from 0 to x, K0(t)/t from x to infinity.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  28 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the integral limit.

  Output, real ( kind = 8 ) TTI, TTK, the integrals of
  [I0(t)-1]/t from 0 to x, and K0(t)/t from x to oo.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ittjya`
- **Signature:** `Subroutine ittjya(x, ttj, tty)`
- **Purpose:** *****************************************************************************80

  ! ITTJYA integrates (1-J0(t))/t from 0 to x, and Y0(t)/t from x to infinity.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  28 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the integral limit.

  Output, real ( kind = 8 ) TTJ, TTY, the integrals of [1-J0(t)]/t
  from 0 to x and of Y0(t)/t from x to oo.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ittjyb`
- **Signature:** `Subroutine ittjyb(x, ttj, tty)`
- **Purpose:** *****************************************************************************80

  ! ITTJYB integrates (1-J0(t))/t from 0 to x, and Y0(t)/t from x to infinity.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  01 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the integral limit.

  Output, real ( kind = 8 ) TTJ, TTY, the integrals of [1-J0(t)]/t
  from 0 to x and of Y0(t)/t from x to oo.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `jdzo`
- **Signature:** `Subroutine jdzo(nt, n, m, p, zo)`
- **Purpose:** *****************************************************************************80

  ! JDZO computes the zeros of Bessel functions Jn(x) and Jn'(x).

  Discussion:

  This procedure computes the zeros of Bessel functions Jn(x) and
  Jn'(x), and arrange them in the order of their magnitudes.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  01 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) NT, the number of zeros.

  Output, integer ( kind = 4 ) N(*), the  order of Jn(x) or Jn'(x) associated
  with the L-th zero.

  Output, integer ( kind = 4 ) M(*), the serial number of the zeros of Jn(x)
  or Jn'(x) associated with the L-th zero ( L is the serial number of all the
  zeros of Jn(x) and Jn'(x) ).

  Output, character ( len = 4 ) P(L), 'TM' or 'TE', a code for designating
  the zeros of Jn(x)  or Jn'(x).  In the waveguide applications, the zeros
  of Jn(x) correspond to TM modes and those of Jn'(x) correspond to TE modes.

  Output, real ( kind = 8 ) ZO(*), the zeros of Jn(x) and Jn'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `jelp`
- **Signature:** `Subroutine jelp(u, hk, esn, ecn, edn, eph)`
- **Purpose:** *****************************************************************************80

  ! JELP computes Jacobian elliptic functions SN(u), CN(u), DN(u).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  08 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) U, the argument.

  Input, real ( kind = 8 ) HK, the modulus, between 0 and 1.

  Output, real ( kind = 8 ) ESN, ECN, EDN, EPH, the values of
  sn(u), cn(u), dn(u), and phi (in degrees).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `jy01a`
- **Signature:** `Subroutine jy01a(x, bj0, dj0, bj1, dj1, by0, dy0, by1, dy1)`
- **Purpose:** *****************************************************************************80

  ! JY01A computes Bessel functions J0(x), J1(x), Y0(x), Y1(x) and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  01 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) BJ0, DJ0, BJ1, DJ1, BY0, DY0, BY1, DY1,
  the values of J0(x), J0'(x), J1(x), J1'(x), Y0(x), Y0'(x), Y1(x), Y1'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `jy01b`
- **Signature:** `Subroutine jy01b(x, bj0, dj0, bj1, dj1, by0, dy0, by1, dy1)`
- **Purpose:** *****************************************************************************80

  ! JY01B computes Bessel functions J0(x), J1(x), Y0(x), Y1(x) and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  02 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) BJ0, DJ0, BJ1, DJ1, BY0, DY0, BY1, DY1,
  the values of J0(x), J0'(x), J1(x), J1'(x), Y0(x), Y0'(x), Y1(x), Y1'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `jyna`
- **Signature:** `Subroutine jyna(n, x, nm, bj, dj, by, dy)`
- **Purpose:** *****************************************************************************80

  ! JYNA computes Bessel functions Jn(x) and Yn(x) and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  29 April 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, real ( kind = 8 ) BJ(0:N), DJ(0:N), BY(0:N), DY(0:N), the values
  of Jn(x), Jn'(x), Yn(x), Yn'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `jynb`
- **Signature:** `Subroutine jynb(n, x, nm, bj, dj, by, dy)`
- **Purpose:** *****************************************************************************80

  ! JYNB computes Bessel functions Jn(x) and Yn(x) and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  02 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, real ( kind = 8 ) BJ(0:N), DJ(0:N), BY(0:N), DY(0:N), the values
  of Jn(x), Jn'(x), Yn(x), Yn'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `jyndd`
- **Signature:** `Subroutine jyndd(n, x, bjn, djn, fjn, byn, dyn, fyn)`
- **Purpose:** *****************************************************************************80

  ! JYNDD: Bessel functions Jn(x) and Yn(x), first and second derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  02 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) BJN, DJN, FJN, BYN, DYN, FYN, the values of
  Jn(x), Jn'(x), Jn"(x), Yn(x), Yn'(x), Yn"(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `jyv`
- **Signature:** `Subroutine jyv(v, x, vm, bj, dj, by, dy)`
- **Purpose:** *****************************************************************************80

  ! JYV computes Bessel functions Jv(x) and Yv(x) and their derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  02 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) V, the order of Jv(x) and Yv(x).

  Input, real ( kind = 8 ) X, the argument of Jv(x) and Yv(x).

  Output, real ( kind = 8 ) VM, the highest order computed.

  Output, real ( kind = 8 ) BJ(0:N), DJ(0:N), BY(0:N), DY(0:N),
  the values of Jn+v0(x), Jn+v0'(x), Yn+v0(x), Yn+v0'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `jyzo`
- **Signature:** `Subroutine jyzo(n, nt, rj0, rj1, ry0, ry1)`
- **Purpose:** *****************************************************************************80

  ! JYZO computes the zeros of Bessel functions Jn(x), Yn(x) and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  28 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of the Bessel functions.

  Input, integer ( kind = 4 ) NT, the number of zeros.

  Output, real ( kind = 8 ) RJ0(NT), RJ1(NT), RY0(NT), RY1(NT), the zeros
  of Jn(x), Jn'(x), Yn(x), Yn'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `klvna`
- **Signature:** `Subroutine klvna(x, ber, bei, ger, gei, der, dei, her, hei)`
- **Purpose:** *****************************************************************************80

  ! KLVNA: Kelvin functions ber(x), bei(x), ker(x), and kei(x), and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  03 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) BER, BEI, GER, GEI, DER, DEI, HER, HEI,
  the values of ber x, bei x, ker x, kei x, ber'x, bei'x, ker'x, kei'x.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `klvnb`
- **Signature:** `Subroutine klvnb(x, ber, bei, ger, gei, der, dei, her, hei)`
- **Purpose:** *****************************************************************************80

  ! KLVNB: Kelvin functions ber(x), bei(x), ker(x), and kei(x), and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  03 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) BER, BEI, GER, GEI, DER, DEI, HER, HEI,
  the values of ber x, bei x, ker x, kei x, ber'x, bei'x, ker'x, kei'x.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `klvnzo`
- **Signature:** `Subroutine klvnzo(nt, kd, zo)`
- **Purpose:** *****************************************************************************80

  ! KLVNZO computes zeros of the Kelvin functions.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  15 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) NT, the number of zeros.

  Input, integer ( kind = 4 ) KD, the function code.
  1 for ber x,
  2 for bei x,
  3 for ker x,
  4 for kei x,
  5 for ber' x,
  6 for bei' x,
  7 for ker' x,
  8 for kei' x.

  Output, real ( kind = 8 ) ZO(NT), the zeros of the given Kelvin function.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `kmn`
- **Signature:** `Subroutine kmn(m, n, c, cv, kd, df, dn, ck1, ck2)`
- **Purpose:** *****************************************************************************80

  ! KMN: expansion coefficients of prolate or oblate spheroidal functions.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  02 August 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter;  M = 0, 1, 2, ...

  Input, integer ( kind = 4 ) N, mode parameter, N = M, M + 1, M + 2, ...

  Input, real ( kind = 8 ) C, spheroidal parameter.

  Input, real ( kind = 8 ) CV, the characteristic value.

  Input, integer ( kind = 4 ) KD, the function code.
  1, the prolate function.
  -1, the oblate function.

  Input, real ( kind = 8 ) DF(*), the expansion coefficients.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `lagzo`
- **Signature:** `Subroutine lagzo(n, x, w)`
- **Purpose:** *****************************************************************************80

  ! LAGZO computes zeros of the Laguerre polynomial, and integration weights.

  Discussion:

  This procedure computes the zeros of Laguerre polynomial Ln(x) in the
  interval [0,∞], and the corresponding weighting coefficients for
  Gauss-Laguerre integration.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  07 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of the Laguerre polynomial.

  Output, real ( kind = 8 ) X(N), the zeros of the Laguerre polynomial.

  Output, real ( kind = 8 ) W(N), the weighting coefficients.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `lamn`
- **Signature:** `Subroutine lamn(n, x, nm, bl, dl)`
- **Purpose:** *****************************************************************************80

  ! LAMN computes lambda functions and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  14 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, real ( kind = 8 ) BL(0:N), DL(0:N), the
  value of the lambda function and its derivative of orders 0 through N.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `lamv`
- **Signature:** `Subroutine lamv(v, x, vm, vl, dl)`
- **Purpose:** *****************************************************************************80

  ! LAMV computes lambda functions and derivatives of arbitrary order.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  31 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) V, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) VM, the highest order computed.

  Output, real ( kind = 8 ) VL(0:*), DL(0:*), the Lambda function and
  derivative, of orders N+V0.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `legzo`
- **Signature:** `Subroutine legzo(n, x, w)`
- **Purpose:** *****************************************************************************80

  ! LEGZO computes the zeros of Legendre polynomials, and integration weights.

  Discussion:

  This procedure computes the zeros of Legendre polynomial Pn(x) in the
  interval [-1,1], and the corresponding weighting coefficients for
  Gauss-Legendre integration.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  13 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of the polynomial.

  Output, real ( kind = 8 ) X(N), W(N), the zeros of the polynomial,
  and the corresponding weights.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `lgama`
- **Signature:** `Subroutine lgama(kf, x, gl)`
- **Purpose:** *****************************************************************************80

  ! LGAMA computes the gamma function or its logarithm.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  15 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) KF, the argument code.
  1, for gamma(x);
  2, for ln(gamma(x)).

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) GL, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `lpmn`
- **Signature:** `Subroutine lpmn(mm, m, n, x, pm, pd)`
- **Purpose:** *****************************************************************************80

  ! LPMN computes associated Legendre functions Pmn(X) and derivatives P'mn(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  19 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) MM, the leading dimension of PM and PD.

  Input, integer ( kind = 4 ) M, the order of Pmn(x).

  Input, integer ( kind = 4 ) N, the degree of Pmn(x).

  Input, real ( kind = 8 ) X, the argument of Pmn(x).

  Output, real ( kind = 8 ) PM(0:MM,0:N), PD(0:MM,0:N), the
  values of Pmn(x) and Pmn'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `lpmns`
- **Signature:** `Subroutine lpmns(m, n, x, pm, pd)`
- **Purpose:** *****************************************************************************80

  ! LPMNS computes associated Legendre functions Pmn(X) and derivatives P'mn(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  18 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the order of Pmn(x).

  Input, integer ( kind = 4 ) N, the degree of Pmn(x).

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) PM(0:N), PD(0:N), the values and derivatives
  of the function from degree 0 to N.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `lpmv`
- **Signature:** `Subroutine lpmv(v, m, x, pmv)`
- **Purpose:** *****************************************************************************80

  ! LPMV computes associated Legendre functions Pmv(X) with arbitrary degree.

  Discussion:

  Compute the associated Legendre function Pmv(x) with an integer order
  and an arbitrary nonnegative degree v.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  19 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) V, the degree of Pmv(x).

  Input, integer ( kind = 4 ) M, the order of Pmv(x).

  Input, real ( kind = 8 ) X, the argument of Pm(x).

  Output, real ( kind = 8 ) PMV, the value of Pm(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `lpn`
- **Signature:** `Subroutine lpn(n, x, pn, pd)`
- **Purpose:** *****************************************************************************80

  ! LPN computes Legendre polynomials Pn(x) and derivatives Pn'(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  07 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the maximum degree.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) PN(0:N), PD(0:N), the values and derivatives
  of the polyomials of degrees 0 to N at X.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `lpni`
- **Signature:** `Subroutine lpni(n, x, pn, pd, pl)`
- **Purpose:** *****************************************************************************80

  ! LPNI computes Legendre polynomials Pn(x), derivatives, and integrals.

  Discussion:

  This routine computes Legendre polynomials Pn(x), Pn'(x)
  and the integral of Pn(t) from 0 to x.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  13 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the maximum degree.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) PN(0:N), PD(0:N), PL(0:N), the values,
  derivatives and integrals of the polyomials of degrees 0 to N at X.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `lqmn`
- **Signature:** `Subroutine lqmn(mm, m, n, x, qm, qd)`
- **Purpose:** *****************************************************************************80

  ! LQMN computes associated Legendre functions Qmn(x) and derivatives.

  Discussion:

  This routine computes the associated Legendre functions of the
  second kind, Qmn(x) and Qmn'(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  13 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) MM, determines the leading dimension
  of QM and QD.

  Input, integer ( kind = 4 ) M, the order of Qmn(x).

  Input, integer ( kind = 4 ) N, the degree of Qmn(x).

  Output, real ( kind = 8 ) QM(0:MM,0:N), QD(0:MM,0:N), contains the values
  of Qmn(x) and Qmn'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `lqmns`
- **Signature:** `Subroutine lqmns(m, n, x, qm, qd)`
- **Purpose:** *****************************************************************************80

  ! LQMNS computes associated Legendre functions Qmn(x) and derivatives Qmn'(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  28 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the order.

  Input, integer ( kind = 4 ) N, the degree.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) QM(0:N), QD(0:N), the values of Qmn(x)
  and Qmn'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `lqna`
- **Signature:** `Subroutine lqna(n, x, qn, qd)`
- **Purpose:** *****************************************************************************80

  ! LQNA computes Legendre function Qn(x) and derivatives Qn'(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  19 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the degree of Qn(x).

  Input, real ( kind = 8 ) X, the argument of Qn(x).

  Output, real ( kind = 8 ) QN(0:N), QD(0:N), the values of
  Qn(x) and Qn'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `lqnb`
- **Signature:** `Subroutine lqnb(n, x, qn, qd)`
- **Purpose:** *****************************************************************************80

  ! LQNB computes Legendre function Qn(x) and derivatives Qn'(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  19 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the degree of Qn(x).

  Input, real ( kind = 8 ) X, the argument of Qn(x).

  Output, real ( kind = 8 ) QN(0:N), QD(0:N), the values of
  Qn(x) and Qn'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `msta1`
- **Signature:** `Function msta1(x, mp)`
- **Purpose:** *****************************************************************************80

  ! MSTA1 determines a backward recurrence starting point for Jn(x).

  Discussion:

  This procedure determines the starting point for backward
  recurrence such that the magnitude of
  Jn(x) at that point is about 10^(-MP).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  08 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Input, integer ( kind = 4 ) MP, the negative logarithm of the
  desired magnitude.

  Output, integer ( kind = 4 ) MSTA1, the starting point.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `msta2`
- **Signature:** `Function msta2(x, n, mp)`
- **Purpose:** *****************************************************************************80

  ! MSTA2 determines a backward recurrence starting point for Jn(x).

  Discussion:

  This procedure determines the starting point for a backward
  recurrence such that all Jn(x) has MP significant digits.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  08 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument of Jn(x).

  Input, integer ( kind = 4 ) N, the order of Jn(x).

  Input, integer ( kind = 4 ) MP, the number of significant digits.

  Output, integer ( kind = 4 ) MSTA2, the starting point.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `mtu0`
- **Signature:** `Subroutine mtu0(kf, m, q, x, csf, csd)`
- **Purpose:** *****************************************************************************80

  ! MTU0 computes Mathieu functions CEM(x,q) and SEM(x,q) and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  20 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) KF, the function code.
  1 for computing cem(x,q) and cem'(x,q)
  2 for computing sem(x,q) and sem'(x,q).

  Input, integer ( kind = 4 ) M, the order of the Mathieu functions.

  Input, real ( kind = 8 ) Q, the parameter of the Mathieu functions.

  Input, real ( kind = 8 ) X, the argument of the Mathieu functions,
  in degrees.

  Output, real ( kind = 8 ) CSF, CSD, the values of cem(x,q) and cem'(x,q),
  or of sem(x,q) and sem'(x,q).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `mtu12`
- **Signature:** `Subroutine mtu12(kf, kc, m, q, x, f1r, d1r, f2r, d2r)`
- **Purpose:** *****************************************************************************80

  ! MTU12 computes modified Mathieu functions of the first and second kind.

  Discussion:

  This procedure computes modified Mathieu functions of the first and
  second kinds, Mcm(1)(2)(x,q) and Msm(1)(2)(x,q),
  and their derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  31 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) KF, the function code.
  1 for computing Mcm(x,q);
  2 for computing Msm(x,q).

  Input, integer ( kind = 4 ) KC, the function code.
  1, for computing the first kind
  2, for computing the second kind or Msm(2)(x,q) and Msm(2)'(x,q)
  3, for computing both the first and second kinds.

  Input, integer ( kind = 4 ) M, the order of the Mathieu functions.

  Input, real ( kind = 8 ) Q, the parameter of the Mathieu functions.

  Input, real ( kind = 8 ) X, the argument of the Mathieu functions.

  Output, real ( kind = 8 ) F1R, D1R, F2R, D2R, the values of
  Mcm(1)(x,q) or Msm(1)(x,q), Derivative of Mcm(1)(x,q) or Msm(1)(x,q),
  Mcm(2)(x,q) or Msm(2)(x,q), Derivative of Mcm(2)(x,q) or Msm(2)(x,q).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `othpl`
- **Signature:** `Subroutine othpl(kf, n, x, pl, dpl)`
- **Purpose:** *****************************************************************************80

  ! OTHPL computes orthogonal polynomials Tn(x), Un(x), Ln(x) or Hn(x).

  Discussion:

  This procedure computes orthogonal polynomials: Tn(x) or Un(x),
  or Ln(x) or Hn(x), and their derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  08 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) KT, the function code:
  1 for Chebyshev polynomial Tn(x)
  2 for Chebyshev polynomial Un(x)
  3 for Laguerre polynomial Ln(x)
  4 for Hermite polynomial Hn(x)

  Input, integer ( kind = 4 ) N, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) PL(0:N), DPL(0:N), the value and derivative of
  the polynomials of order 0 through N at X.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `pbdv`
- **Signature:** `Subroutine pbdv(v, x, dv, dp, pdf, pdd)`
- **Purpose:** *****************************************************************************80

  ! PBDV computes parabolic cylinder functions Dv(x) and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  29 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) V, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) DV(0:*), DP(0:*), the values of
  Dn+v0(x), Dn+v0'(x).

  Output, real ( kind = 8 ) PDF, PDD, the values of Dv(x) and Dv'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `pbvv`
- **Signature:** `Subroutine pbvv(v, x, vv, vp, pvf, pvd)`
- **Purpose:** *****************************************************************************80

  ! PBVV computes parabolic cylinder functions Vv(x) and their derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  29 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) V, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) VV(0:*), VP(0:*), the values of Vv(x), Vv'(x).

  Output, real ( kind = 8 ) PVF, PVD, the values of Vv(x) and Vv'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `pbwa`
- **Signature:** `Subroutine pbwa(a, x, w1f, w1d, w2f, w2d)`
- **Purpose:** *****************************************************************************80

  ! PBWA computes parabolic cylinder functions W(a,x) and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  29 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) A, the parameter.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) W1F, W1D, W2F, W2D, the values of
  W(a,x), W'(a,x), W(a,-x), W'(a,-x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `psi`
- **Signature:** `Subroutine psi(x, ps)`
- **Purpose:** *****************************************************************************80

  ! PSI computes the PSI function.

  Licensing:

  The original FORTRAN77 version of this routine is copyrighted by
  Shanjie Zhang and Jianming Jin.  However, they give permission to
  incorporate this routine into a user program that the copyright
  is acknowledged.

  Modified:

  08 September 2007

  Author:

  Original FORTRAN77 by Shanjie Zhang, Jianming Jin.
  FORTRAN90 version by John Burkardt.

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) PS, the value of the PSI function.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `qstar`
- **Signature:** `Subroutine qstar(m, n, c, ck, ck1, qs, qt)`
- **Purpose:** *****************************************************************************80

  ! QSTAR computes Q*mn(-ic) for oblate radial functions with a small argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  18 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter;  M = 0, 1, 2, ...

  Input, integer ( kind = 4 ) N, mode parameter, N = M, M + 1, M + 2, ...

  Input, real ( kind = 8 ) C, spheroidal parameter.

  Input, real ( kind = 8 ) CK(*), ?

  Input, real ( kind = 8 ) CK1, ?

  Output, real ( kind = 8 ) QS, ?

  Output, real ( kind = 8 ) QT, ?
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `rctj`
- **Signature:** `Subroutine rctj(n, x, nm, rj, dj)`
- **Purpose:** *****************************************************************************80

  ! RCTJ computes Riccati-Bessel function of the first kind, and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  18 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of jn(x).

  Input, real ( kind = 8 ) X, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, real ( kind = 8 ) RJ(0:N), the values of x jn(x).

  Output, real ( kind = 8 ) DJ(0:N), the values of [x jn(x)]'.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `rcty`
- **Signature:** `Subroutine rcty(n, x, nm, ry, dy)`
- **Purpose:** *****************************************************************************80

  ! RCTY computes Riccati-Bessel function of the second kind, and derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  18 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of yn(x).

  Input, real ( kind = 8 ) X, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, real ( kind = 8 ) RY(0:N), the values of x yn(x).

  Output, real ( kind = 8 ) DY(0:N), the values of [x yn(x)]'.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `refine`
- **Signature:** `Subroutine refine(kd, m, q, a, iflag)`
- **Purpose:** *****************************************************************************80

  ! REFINE refines an estimate of the characteristic value of Mathieu functions.

  Discussion:

  This procedure calculates the accurate characteristic value
  by the secant method.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  20 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) KD, the case code:
  1, for cem(x,q)  ( m = 0,2,4,...)
  2, for cem(x,q)  ( m = 1,3,5,...)
  3, for sem(x,q)  ( m = 1,3,5,...)
  4, for sem(x,q)  ( m = 2,4,6,...)

  Input, integer ( kind = 4 ) M, the order of the Mathieu functions.

  Input, real ( kind = 8 ) Q, the parameter of the Mathieu functions.

  Input/output, real ( kind = 8 ) A, the characteristic value, which
  should have been refined on output.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `rmn1`
- **Signature:** `Subroutine rmn1(m, n, c, x, df, kd, r1f, r1d)`
- **Purpose:** *****************************************************************************80

  ! RMN1 computes prolate and oblate spheroidal functions of the first kind.

  Discussion:

  This procedure computes prolate and oblate spheroidal radial
  functions of the first kind for given m, n, c and x.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  29 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter;  M = 0, 1, 2, ...

  Input, integer ( kind = 4 ) N, mode parameter, N = M, M + 1, M + 2, ...

  Input, real ( kind = 8 ) C, spheroidal parameter.

  Input, real ( kind = 8 ) X, the argument.

  Input, real ( kind = 8 ) DF(*), the expansion coefficients.

  Input, integer ( kind = 4 ) KD, the function code.
  1, the prolate function.
  -1, the oblate function.

  Output, real ( kind = 8 ) R1F, R1D, the function and derivative.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `rmn2l`
- **Signature:** `Subroutine rmn2l(m, n, c, x, df, kd, r2f, r2d, id)`
- **Purpose:** *****************************************************************************80

  ! RMN2L: prolate and oblate spheroidal functions, second kind, large CX.

  Discussion:

  This procedure computes prolate and oblate spheroidal radial functions
  of the second kind for given m, n, c and a large cx.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  30 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter;  M = 0, 1, 2, ...

  Input, integer ( kind = 4 ) N, mode parameter, N = M, M + 1, M + 2, ...

  Input, real ( kind = 8 ) C, spheroidal parameter.

  Input, real ( kind = 8 ) X, the argument.

  Input, real ( kind = 8 ) DF(*), the expansion coefficients.

  Input, integer ( kind = 4 ) KD, the function code.
  1, the prolate function.
  -1, the oblate function.

  Output, real ( kind = 8 ) R2F, R2D, the function and derivative values.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `rmn2so`
- **Signature:** `Subroutine rmn2so(m, n, c, x, cv, df, kd, r2f, r2d)`
- **Purpose:** *****************************************************************************80

  ! RMN2SO: oblate radial functions of the second kind with small argument.

  Discussion:

  This procedure computes oblate radial functions of the second kind
  with a small argument, Rmn(-ic,ix) and Rmn'(-ic,ix).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  27 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter;  M = 0, 1, 2, ...

  Input, integer ( kind = 4 ) N, mode parameter, N = M, M + 1, M + 2, ...

  Input, real ( kind = 8 ) C, spheroidal parameter.

  Input, real ( kind = 8 ) X, the argument.

  Input, real ( kind = 8 ) CV, the characteristic value.

  Input, real ( kind = 8 ) DF(*), the expansion coefficients.

  Input, integer ( kind = 4 ) KD, the function code.
  1, the prolate function.
  -1, the oblate function.

  Output, real ( kind = 8 ) R2F, R2D, the values of Rmn(-ic,ix)
  and Rmn'(-ic,ix).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `rmn2sp`
- **Signature:** `Subroutine rmn2sp(m, n, c, x, cv, df, kd, r2f, r2d)`
- **Purpose:** *****************************************************************************80

  ! RMN2SP: prolate, oblate spheroidal radial functions, kind 2, small argument.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  28 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter;  M = 0, 1, 2, ...

  Input, integer ( kind = 4 ) N, mode parameter, N = M, M + 1, M + 2, ...

  Input, real ( kind = 8 ) C, spheroidal parameter.

  Input, real ( kind = 8 ) X, the argument.

  Input, real ( kind = 8 ) CV, the characteristic value.

  Input, real ( kind = 8 ) DF(*), the expansion coefficients.

  Input, integer ( kind = 4 ) KD, the function code.
  1, the prolate function.
  -1, the oblate function.

  Output, real ( kind = 8 ) R2F, R2D, the values of the function and
  its derivative.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `rswfo`
- **Signature:** `Subroutine rswfo(m, n, c, x, cv, kf, r1f, r1d, r2f, r2d)`
- **Purpose:** *****************************************************************************80

  ! RSWFO computes prolate spheroidal radial function of first and second kinds.

  Discussion:

  This procedure computes oblate radial functions of the first
  and second kinds, and their derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  07 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter;  M = 0, 1, 2, ...

  Input, integer ( kind = 4 ) N, mode parameter, N = M, M + 1, M + 2, ...

  Input, real ( kind = 8 ) C, spheroidal parameter.

  Input, real ( kind = 8 ) X, the argument.

  Input, real ( kind = 8 ) CV, the characteristic value.

  Input, integer ( kind = 4 ) KF, the function code.
  1, for the first kind
  2, for the second kind
  3, for both the first and second kinds.

  Output, real ( kind = 8 ) R1F, the radial function of the first kind;

  Output, real ( kind = 8 ) R1D, the derivative of the radial function of
  the first kind;

  Output, real ( kind = 8 ) R2F, the radial function of the second kind;

  Output, real ( kind = 8 ) R2D, the derivative of the radial function of
  the second kind;
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `rswfp`
- **Signature:** `Subroutine rswfp(m, n, c, x, cv, kf, r1f, r1d, r2f, r2d)`
- **Purpose:** *****************************************************************************80

  ! RSWFP computes prolate spheroidal radial function of first and second kinds.

  Discussion:

  This procedure computes prolate spheriodal radial functions of the
  first and second kinds, and their derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  07 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter;  M = 0, 1, 2, ...

  Input, integer ( kind = 4 ) N, mode parameter, N = M, M + 1, M + 2, ...

  Input, real ( kind = 8 ) C, spheroidal parameter.

  Input, real ( kind = 8 ) X, the argument of the radial function, 1 < X.

  Input, real ( kind = 8 ) CV, the characteristic value.

  Input, integer ( kind = 4 ) KF, the function code.
  1, for the first kind
  2, for the second kind
  3, for both the first and second kinds.

  Output, real ( kind = 8 ) R1F, the radial function of the first kind;

  Output, real ( kind = 8 ) R1D, the derivative of the radial function of
  the first kind;

  Output, real ( kind = 8 ) R2F, the radial function of the second kind;

  Output, real ( kind = 8 ) R2D, the derivative of the radial function of
  the second kind;
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `scka`
- **Signature:** `Subroutine scka(m, n, c, cv, kd, ck)`
- **Purpose:** *****************************************************************************80

  ! SCKA: expansion coefficients for prolate and oblate spheroidal functions.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  22 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter.

  Input, integer ( kind = 4 ) N, the mode parameter.

  Input, real ( kind = 8 ) C, the spheroidal parameter.

  Input, real ( kind = 8 ) CV, the characteristic value.

  Input, integer ( kind = 4 ) KD, the function code.
  1, the prolate function.
  -1, the oblate function.

  Output, real ( kind = 8 ) CK(*), the expansion coefficients.
  CK(1), CK(2),... correspond to c0, c2,..., and so on.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `sckb`
- **Signature:** `Subroutine sckb(m, n, c, df, ck)`
- **Purpose:** *****************************************************************************80

  ! SCKB: expansion coefficients for prolate and oblate spheroidal functions.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  15 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter.

  Input, integer ( kind = 4 ) N, the mode parameter.

  Input, real ( kind = 8 ) C, the spheroidal parameter.

  Input, real ( kind = 8 ) DF(*), the expansion coefficients DK.

  Output, real ( kind = 8 ) CK(*), the expansion coefficients CK.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `sdmn`
- **Signature:** `Subroutine sdmn(m, n, c, cv, kd, df)`
- **Purpose:** *****************************************************************************80

  ! SDMN: expansion coefficients for prolate and oblate spheroidal functions.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  29 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter.

  Input, integer ( kind = 4 ) N, the mode parameter.

  Input, real ( kind = 8 ) C, the spheroidal parameter.

  Input, real ( kind = 8 ) CV, the characteristic value.

  Input, integer ( kind = 4 ) KD, the function code.
  1, the prolate function.
  -1, the oblate function.

  Output, real ( kind = 8 ) DF(*), expansion coefficients;
  DF(1), DF(2), ... correspond to d0, d2, ... for even n-m and d1,
  d3, ... for odd n-m
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `segv`
- **Signature:** `Subroutine segv(m, n, c, kd, cv, eg)`
- **Purpose:** *****************************************************************************80

  ! SEGV computes the characteristic values of spheroidal wave functions.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  28 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) M, the mode parameter.

  Input, integer ( kind = 4 ) N, the mode parameter.

  Input, real ( kind = 8 ) C, the spheroidal parameter.

  Input, integer ( kind = 4 ) KD, the function code.
  1, the prolate function.
  -1, the oblate function.

  Output, real ( kind = 8 ) CV, the characteristic value.

  Output, real ( kind = 8 ) EG(*), the characteristic value for
  mode parameters m and n.  ( L = n - m + 1 )
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `sphi`
- **Signature:** `Subroutine sphi(n, x, nm, si, di)`
- **Purpose:** *****************************************************************************80

  ! SPHI computes spherical Bessel functions in(x) and their derivatives in'(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  18 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of In(X).

  Input, real ( kind = 8 ) X, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, real ( kind = 8 ) SI(0:N), DI(0:N), the values and derivatives
  of the function of orders 0 through N.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `sphj`
- **Signature:** `Subroutine sphj(n, x, nm, sj, dj)`
- **Purpose:** *****************************************************************************80

  ! SPHJ computes spherical Bessel functions jn(x) and their derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  15 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, real ( kind = 8 ) SJ(0:N), the values of jn(x).

  Output, real ( kind = 8 ) DJ(0:N), the values of jn'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `sphk`
- **Signature:** `Subroutine sphk(n, x, nm, sk, dk)`
- **Purpose:** *****************************************************************************80

  ! SPHK computes modified spherical Bessel functions kn(x) and derivatives.

  Discussion:

  This procedure computes modified spherical Bessel functions
  of the second kind, kn(x) and kn'(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  15 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, real ( kind = 8 ) SK(0:N), DK(0:N), the values of kn(x) and kn'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `sphy`
- **Signature:** `Subroutine sphy(n, x, nm, sy, dy)`
- **Purpose:** *****************************************************************************80

  ! SPHY computes spherical Bessel functions yn(x) and their derivatives.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  15 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, integer ( kind = 4 ) N, the order.

  Input, real ( kind = 8 ) X, the argument.

  Output, integer ( kind = 4 ) NM, the highest order computed.

  Output, real ( kind = 8 ) SY(0:N), DY(0:N), the values of yn(x) and yn'(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `stvh0`
- **Signature:** `Subroutine stvh0(x, sh0)`
- **Purpose:** *****************************************************************************80

  ! STVH0 computes the Struve function H0(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  22 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) SH0, the value of H0(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `stvh1`
- **Signature:** `Subroutine stvh1(x, sh1)`
- **Purpose:** *****************************************************************************80

  ! STVH1 computes the Struve function H1(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  22 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) SH1, the value of H1(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `stvhv`
- **Signature:** `Subroutine stvhv(v, x, hv)`
- **Purpose:** *****************************************************************************80

  ! STVHV computes the Struve function Hv(x) with arbitrary order v.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  24 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) V, the order of the function.

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) HV, the value of Hv(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `stvl0`
- **Signature:** `Subroutine stvl0(x, sl0)`
- **Purpose:** *****************************************************************************80

  ! STVL0 computes the modified Struve function L0(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  22 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) SL0, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `stvl1`
- **Signature:** `Subroutine stvl1(x, sl1)`
- **Purpose:** *****************************************************************************80

  ! STVL1 computes the modified Struve function L1(x).

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  05 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Output, real ( kind = 8 ) SL1, the function value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `stvlv`
- **Signature:** `Subroutine stvlv(v, x, slv)`
- **Purpose:** *****************************************************************************80

  ! STVLV computes the modified Struve function Lv(x) with arbitary order.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  04 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) V, the order of Lv(x).

  Input, real ( kind = 8 ) X, the argument of Lv(x).

  Output, real ( kind = 8 ) SLV, the value of Lv(x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `vvla`
- **Signature:** `Subroutine vvla(va, x, pv)`
- **Purpose:** *****************************************************************************80

  ! VVLA computes parabolic cylinder function Vv(x) for large arguments.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  04 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Input, real ( kind = 8 ) VA, the order nu.

  Output, real ( kind = 8 ) PV, the value of V(nu,x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `vvsa`
- **Signature:** `Subroutine vvsa(va, x, pv)`
- **Purpose:** *****************************************************************************80

  ! VVSA computes parabolic cylinder function V(nu,x) for small arguments.

  Licensing:

  This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
  they give permission to incorporate this routine into a user program
  provided that the copyright is acknowledged.

  Modified:

  04 July 2012

  Author:

  Shanjie Zhang, Jianming Jin

  Reference:

  Shanjie Zhang, Jianming Jin,
  Computation of Special Functions,
  Wiley, 1996,
  ISBN: 0-471-11963-6,
  LC: QA351.C45.

  Parameters:

  Input, real ( kind = 8 ) X, the argument.

  Input, real ( kind = 8 ) VA, the order nu.

  Output, real ( kind = 8 ) PV, the value of V(nu,x).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

## Important Variables/Constants

[List and describe any important variables or constants defined or used extensively in this file.]

- **Variable/Constant 1:** ([Type]) [Description, purpose, and typical values/range]
- **Variable/Constant 2:** ([Type]) [Description, purpose, and typical values/range]

## Usage Examples

[Provide one or more code snippets demonstrating how to use the components of this file.]

```fortran
! Example 1: Calling a key subroutine/function
! ... code ...
```

## Dependencies and Interactions

[Describe any dependencies this file has on other modules or external libraries. Also, explain how this file interacts with other parts of the project.]

- **Internal Dependencies:** [List other project files/modules this file depends on]
- **External Libraries:** [List any external libraries required, e.g., BLAS, LAPACK]
- **Interactions:** [Describe how this file is used by or uses other components of the software]
