## Overview

Overview not automatically extracted.

## Key Components

### Module: `interpolate_pppack`
- **Purpose:** Overview not automatically extracted.
- **Contains:** `banfac`, `banslv`, `bchfac`, `bchslv`, `bsplpp`, `bsplvb`, `bsplvd`, `bspp2d`, `bvalue`, `chol1d`, `colloc`, `colpnt`, `cubspl`, `cwidth`, `difequ`, `dtblok`, `eqblok`, `evnnot`, `factrb`, `fcblok`, `interv`, `knots`, `l2appr`, `l2err`, `l2knts`, `newnot`, `ppvalu`, `putit`, `round`, `sbblok`, `setupq`, `shiftb`, `slvblk`, `smooth`, `spli2d`, `splint`, `splopt`, `subbak`, `subfor`, `tautsp`, `titand`

### Subroutine: `banfac`
- **Signature:** `Subroutine banfac(w, nroww, nrow, nbandl, nbandu, iflag)`
- **Purpose:** *****************************************************************************80

  ! BANFAC factors a banded matrix without pivoting.

  Discussion:

  BANFAC returns in W the LU-factorization, without pivoting, of
  the banded matrix A of order NROW with (NBANDL+1+NBANDU) bands
  or diagonals in the work array W.

  Gauss elimination without pivoting is used.  The routine is
  intended for use with matrices A which do not require row
  interchanges during factorization, especially for the totally
  positive matrices which occur in spline calculations.

  The matrix storage mode used is the same one used by LINPACK
  and LAPACK, and results in efficient innermost loops.

  Explicitly, A has

  NBANDL bands below the diagonal
  1     main diagonal
  NBANDU bands above the diagonal

  and thus, with MIDDLE=NBANDU+1,
  A(I+J,J) is in W(I+MIDDLE,J) for I=-NBANDU,...,NBANDL, J=1,...,NROW.

  For example, the interesting entries of a banded matrix
  matrix of order 9, with NBANDL=1, NBANDU=2:

  11 12 13  0  0  0  0  0  0
  21 22 23 24  0  0  0  0  0
  0 32 33 34 35  0  0  0  0
  0  0 43 44 45 46  0  0  0
  0  0  0 54 55 56 57  0  0
  0  0  0  0 65 66 67 68  0
  0  0  0  0  0 76 77 78 79
  0  0  0  0  0  0 87 88 89
  0  0  0  0  0  0  0 98 99

  would appear in the first 1+1+2=4 rows of W as follows:

  0  0 13 24 35 46 57 68 79
  0 12 23 34 45 56 67 78 89
  11 22 33 44 55 66 77 88 99
  21 32 43 54 65 76 87 98  0

  All other entries of W not identified in this way with an
  entry of A are never referenced.

  This routine makes it possible to solve any particular linear system
  A*X=B for X by the call

  call banslv ( w, nroww, nrow, nbandl, nbandu, b )

  with the solution X contained in B on return.

  If IFLAG=2, then one of NROW-1, NBANDL, NBANDU failed to be nonnegative,
  or else one of the potential pivots was found to be zero
  indicating that A does not have an LU-factorization.  This
  implies that A is singular in case it is totally positive.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input/output, real ( kind = 8 ) W(NROWW,NROW).
  On input, W contains the "interesting" part of a banded
  matrix A, with the diagonals or bands of A stored in the
  rows of W, while columns of A correspond to columns of W.
  On output, W contains the LU-factorization of A into a unit
  lower triangular matrix L and an upper triangular matrix U
  (both banded) and stored in customary fashion over the
  corresponding entries of A.

  Input, integer ( kind = 4 ) NROWW, the row dimension of the work array W.
  NROWW must be at least NBANDL+1 + NBANDU.

  Input, integer ( kind = 4 ) NROW, the number of rows in A.

  Input, integer ( kind = 4 ) NBANDL, the number of bands of A below
  the main diagonal.

  Input, integer ( kind = 4 ) NBANDU, the number of bands of A above
  the main diagonal.

  Output, integer ( kind = 4 ) IFLAG, error flag.
  1, success.
  2, failure, the matrix was not factored.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `banslv`
- **Signature:** `Subroutine banslv(w, nroww, nrow, nbandl, nbandu, b)`
- **Purpose:** *****************************************************************************80

  ! BANSLV solves a banded linear system A * X = B factored by BANFAC.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) W(NROWW,NROW).  W contains the banded matrix,
  after it has been factored by BANFAC.

  Input, integer ( kind = 4 ) NROWW, the row dimension of the work array W.
  NROWW must be at least NBANDL+1 + NBANDU.

  Input, integer ( kind = 4 ) NROW, the number of rows in A.

  Input, integer ( kind = 4 ) NBANDL, the number of bands of A below the
  main diagonal.

  Input, integer ( kind = 4 ) NBANDU, the number of bands of A above the
  main diagonal.

  Input/output, real ( kind = 8 ) B(NROW).
  On input, B contains the right hand side of the system to be solved.
  On output, B contains the solution, X.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `bchfac`
- **Signature:** `Subroutine bchfac(w, nbands, nrow, diag)`
- **Purpose:** *****************************************************************************80

  ! BCHFAC constructs a Cholesky factorization of a matrix.

  Discussion:

  The factorization has the form

  C = L * D * L'

  with L unit lower triangular and D diagonal, for a given matrix C of
  order NROW, where C is symmetric positive semidefinite and banded,
  having NBANDS diagonals at and below the main diagonal.

  Gauss elimination is used, adapted to the symmetry and bandedness of C.

  Near-zero pivots are handled in a special way.  The diagonal
  element C(N,N) = W(1,N) is saved initially in DIAG(N), all N.

  At the N-th elimination step, the current pivot element, W(1,N),
  is compared with its original value, DIAG(N).  If, as the result
  of prior elimination steps, this element has been reduced by about
  a word length, that is, if W(1,N) + DIAG(N) <= DIAG(N), then the pivot
  is declared to be zero, and the entire N-th row is declared to
  be linearly dependent on the preceding rows.  This has the effect
  of producing X(N) = 0 when solving C * X = B for X, regardless of B.

  Justification for this is as follows.  In contemplated applications
  of this program, the given equations are the normal equations for
  some least-squares approximation problem, DIAG(N) = C(N,N) gives
  the norm-square of the N-th basis function, and, at this point,
  W(1,N) contains the norm-square of the error in the least-squares
  approximation to the N-th basis function by linear combinations
  of the first N-1.

  Having W(1,N)+DIAG(N) <= DIAG(N) signifies that the N-th function
  is linearly dependent to machine accuracy on the first N-1
  functions, therefore can safely be left out from the basis of
  approximating functions.

  The solution of a linear system C * X = B is effected by the
  succession of the following two calls:

  call bchfac ( w, nbands, nrow, diag )

  call bchslv ( w, nbands, nrow, b, x )

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input/output, real ( kind = 8 ) W(NBANDS,NROW).
  On input, W contains the NBANDS diagonals in its rows,
  with the main diagonal in row 1.  Precisely, W(I,J)
  contains C(I+J-1,J), I=1,...,NBANDS, J=1,...,NROW.
  For example, the interesting entries of a seven diagonal
  symmetric matrix C of order 9 would be stored in W as

  11 22 33 44 55 66 77 88 99
  21 32 43 54 65 76 87 98  *
  31 42 53 64 75 86 97  *  *
  41 52 63 74 85 96  *  *  *

  Entries of the array not associated with an
  entry of C are never referenced.
  On output, W contains the Cholesky factorization
  C = L*D*L', with W(1,I) containing 1/D(I,I) and W(I,J)
  containing L(I-1+J,J), I=2,...,NBANDS.

  Input, integer ( kind = 4 ) NBANDS, indicates the bandwidth of the
  matrix C, that is, C(I,J) = 0 for NBANDS < abs(I-J).

  Input, integer ( kind = 4 ) NROW, is the order of the matrix C.

  Work array, real ( kind = 8 ) DIAG(NROW).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `bchslv`
- **Signature:** `Subroutine bchslv(w, nbands, nrow, b)`
- **Purpose:** *****************************************************************************80

  ! BCHSLV solves a banded symmetric positive definite system.

  Discussion:

  The system is of the form:

  C * X = B

  and the Cholesky factorization of C has been constructed
  by BCHFAC.

  With the factorization

  C = L * D * L'

  available, where L is unit lower triangular and D is diagonal,
  the triangular system

  L * Y = B

  is solved for Y (forward substitution), Y is stored in B, the
  vector D**(-1)*Y is computed and stored in B, then the
  triangular system L'*X = D**(-1)*Y is solved for X
  (back substitution).

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) W(NBANDS,NROW), the Cholesky factorization for C,
  as computed by BCHFAC.

  Input, integer ( kind = 4 ) NBANDS, the bandwidth of C.

  Input, integer ( kind = 4 ) NROW, the order of the matrix C.

  Input/output, real ( kind = 8 ) B(NROW).
  On input, the right hand side.
  On output, the solution.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `bsplpp`
- **Signature:** `Subroutine bsplpp(t, bcoef, n, k, scrtch, break, coef, l)`
- **Purpose:** *****************************************************************************80

  ! BSPLPP converts from B-spline to piecewise polynomial form.

  Discussion:

  The B-spline representation of a spline is ( T, BCOEF, N, K ),
  while the piecewise polynomial representation is
  ( BREAK, COEF, L, K ).

  For each breakpoint interval, the K relevant B-spline coefficients
  of the spline are found and then differenced repeatedly to get the
  B-spline coefficients of all the derivatives of the spline on that
  interval.

  The spline and its first K-1 derivatives are then evaluated at the
  left end point of that interval, using BSPLVB repeatedly to obtain
  the values of all B-splines of the appropriate order at that point.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) T(N+K), the knot sequence.

  Input, real ( kind = 8 ) BCOEF(N), the B spline coefficient sequence.

  Input, integer ( kind = 4 ) N, the number of B spline coefficients.

  Input, integer ( kind = 4 ) K, the order of the spline.

  Work array, real ( kind = 8 ) SCRTCH(K,K).

  Output, real ( kind = 8 ) BREAK(L+1), the piecewise polynomial breakpoint
  sequence.  BREAK contains the distinct points in the sequence T(K:N+1)

  Output, real ( kind = 8 ) COEF(K,N), with COEF(I,J) = (I-1)st derivative
  of the spline at BREAK(J) from the right.

  Output, integer ( kind = 4 ) L, the number of polynomial pieces which
  make up the spline in the interval ( T(K), T(N+1) ).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `bsplvb`
- **Signature:** `Subroutine bsplvb(t, jhigh, index, x, left, biatx)`
- **Purpose:** *****************************************************************************80

  ! BSPLVB evaluates B-splines at a point X with a given knot sequence.

  Discusion:

  BSPLVB evaluates all possibly nonzero B-splines at X of order

  JOUT = MAX ( JHIGH, (J+1)*(INDEX-1) )

  with knot sequence T.

  The recurrence relation

  X - T(I)               T(I+J+1) - X
  B(I,J+1)(X) = ----------- * B(I,J)(X) + --------------- * B(I+1,J)(X)
  T(I+J)-T(I)               T(I+J+1)-T(I+1)

  is used to generate B(LEFT-J:LEFT,J+1)(X) from B(LEFT-J+1:LEFT,J)(X)
  storing the new values in BIATX over the old.

  The facts that

  B(I,1)(X) = 1  if  T(I) <= X < T(I+1)

  and that

  B(I,J)(X) = 0  unless  T(I) <= X < T(I+J)

  are used.

  The particular organization of the calculations follows
  algorithm 8 in chapter X of the text.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) T(LEFT+JOUT), the knot sequence.  T is assumed to
  be nondecreasing, and also, T(LEFT) must be strictly less than
  T(LEFT+1).

  Input, integer ( kind = 4 ) JHIGH, INDEX, determine the order
  JOUT = max ( JHIGH, (J+1)*(INDEX-1) )
  of the B-splines whose values at X are to be returned.
  INDEX is used to avoid recalculations when several
  columns of the triangular array of B-spline values are
  needed, for example, in BVALUE or in BSPLVD.
  If INDEX = 1, the calculation starts from scratch and the entire
  triangular array of B-spline values of orders
  1, 2, ...,JHIGH is generated order by order, that is,
  column by column.
  If INDEX = 2, only the B-spline values of order J+1, J+2, ..., JOUT
  are generated, the assumption being that BIATX, J,
  DELTAL, DELTAR are, on entry, as they were on exit
  at the previous call.  In particular, if JHIGH = 0,
  then JOUT = J+1, that is, just the next column of B-spline
  values is generated.
  Warning: the restriction  JOUT <= JMAX (= 20) is
  imposed arbitrarily by the dimension statement for DELTAL
  and DELTAR, but is nowhere checked for.

  Input, real ( kind = 8 ) X, the point at which the B-splines
  are to be evaluated.

  Input, integer ( kind = 4 ) LEFT, an integer chosen so that
  T(LEFT) <= X <= T(LEFT+1).

  Output, real ( kind = 8 ) BIATX(JOUT), with BIATX(I) containing the
  value at X of the polynomial of order JOUT which agrees
  with the B-spline B(LEFT-JOUT+I,JOUT,T) on the interval
  (T(LEFT),T(LEFT+1)).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `bsplvd`
- **Signature:** `Subroutine bsplvd(t, k, x, left, a, dbiatx, nderiv)`
- **Purpose:** *****************************************************************************80

  ! BSPLVD calculates the nonvanishing B-splines and derivatives at X.

  Discussion:

  Values at X of all the relevant B-splines of order K:K+1-NDERIV
  are generated via BSPLVB and stored temporarily in DBIATX.

  Then the B-spline coefficients of the required derivatives
  of the B-splines of interest are generated by differencing,
  each from the preceding one of lower order, and combined with
  the values of B-splines of corresponding order in DBIATX
  to produce the desired values.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) T(LEFT+K), the knot sequence.  It is assumed that
  T(LEFT) < T(LEFT+1).  Also, the output is correct only if
  T(LEFT) <= X <= T(LEFT+1).

  Input, integer ( kind = 4 ) K, the order of the B-splines to be evaluated.

  Input, real ( kind = 8 ) X, the point at which these values are sought.

  Input, integer ( kind = 4 ) LEFT, indicates the left endpoint of the
  interval of interest.  The K B-splines whose support contains the interval
  ( T(LEFT), T(LEFT+1) ) are to be considered.

  Workspace, real ( kind = 8 ) A(K,K).

  Output, real ( kind = 8 ) DBIATX(K,NDERIV).  DBIATX(I,M) contains
  the value of the (M-1)st derivative of the (LEFT-K+I)-th B-spline
  of order K for knot sequence T, I=M,...,K, M=1,...,NDERIV.

  Input, integer ( kind = 4 ) NDERIV, indicates that values of B-splines and
  their derivatives up to but not including the NDERIV-th are asked for.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `bspp2d`
- **Signature:** `Subroutine bspp2d(t, bcoef, n, k, m, scrtch, break, coef, l)`
- **Purpose:** *****************************************************************************80

  ! BSPP2D converts from B-spline to piecewise polynomial representation.

  Discussion:

  The B-spline representation

  T, BCOEF(.,J), N, K

  is converted to its piecewise polynomial representation

  BREAK, COEF(J,.,.), L, K, J=1, ..., M.

  This is an extended version of BSPLPP for use with tensor products.

  For each breakpoint interval, the K relevant B-spline
  coefficients of the spline are found and then differenced
  repeatedly to get the B-spline coefficients of all the
  derivatives of the spline on that interval.

  The spline and its first K-1 derivatives are then evaluated
  at the left endpoint of that interval, using BSPLVB
  repeatedly to obtain the values of all B-splines of the
  appropriate order at that point.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) T(N+K), the knot sequence.

  Input, real ( kind = 8 ) BCOEF(N,M).  For each J, B(*,J) is the
  B-spline coefficient sequence, of length N.

  Input, integer ( kind = 4 ) N, the length of BCOEF.

  Input, integer ( kind = 4 ) K, the order of the spline.

  Input, integer ( kind = 4 ) M, the number of data sets.

  Work array, real ( kind = 8 ) SCRTCH(K,K,M).

  Output, real ( kind = 8 ) BREAK(L+1), the breakpoint sequence
  containing the distinct points in the sequence T(K),...,T(N+1)

  Output, real ( kind = 8 ) COEF(M,K,N), with COEF(MM,I,J) = the (I-1)st
  derivative of the MM-th spline at BREAK(J) from the right, MM=1, ..., M.

  Output, integer ( kind = 4 ) L, the number of polynomial pieces which
  make up the spline in the interval (T(K), T(N+1)).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `bvalue`
- **Signature:** `Function bvalue(t, bcoef, n, k, x, jderiv)`
- **Purpose:** *****************************************************************************80

  ! BVALUE evaluates a derivative of a spline from its B-spline representation.

  Discussion:

  The spline is taken to be continuous from the right.

  The nontrivial knot interval (T(I),T(I+1)) containing X is
  located with the aid of INTERV.  The K B-spline coefficients
  of F relevant for this interval are then obtained from BCOEF,
  or are taken to be zero if not explicitly available, and are
  then differenced JDERIV times to obtain the B-spline
  coefficients of (D**JDERIV)F relevant for that interval.

  Precisely, with J = JDERIV, we have from X.(12) of the text that:

  (D**J)F = sum ( BCOEF(.,J)*B(.,K-J,T) )

  where
  / BCOEF(.),                    if J == 0
  /
  BCOEF(.,J) = / BCOEF(.,J-1) - BCOEF(.-1,J-1)
  / -----------------------------,  if 0 < J
  /    (T(.+K-J) - T(.))/(K-J)

  Then, we use repeatedly the fact that

  sum ( A(.) * B(.,M,T)(X) ) = sum ( A(.,X) * B(.,M-1,T)(X) )

  with
  (X - T(.))*A(.) + (T(.+M-1) - X)*A(.-1)
  A(.,X) =   ---------------------------------------
  (X - T(.))      + (T(.+M-1) - X)

  to write (D**J)F(X) eventually as a linear combination of
  B-splines of order 1, and the coefficient for B(I,1,T)(X)
  must then be the desired number (D**J)F(X).
  See Chapter X, (17)-(19) of text.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) T(N+K), the knot sequence.  T is assumed
  to be nondecreasing.

  Input, real ( kind = 8 ) BCOEF(N), B-spline coefficient sequence.

  Input, integer ( kind = 4 ) N, the length of BCOEF.

  Input, integer ( kind = 4 ) K, the order of the spline.

  Input, real ( kind = 8 ) X, the point at which to evaluate.

  Input, integer ( kind = 4 ) JDERIV, the order of the derivative to
  be evaluated.  JDERIV is assumed to be zero or positive.

  Output, real ( kind = 8 ) BVALUE, the value of the (JDERIV)-th
  derivative of the spline at X.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `chol1d`
- **Signature:** `Subroutine chol1d(p, v, qty, npoint, ncol, u, qu)`
- **Purpose:** *****************************************************************************80

  ! CHOL1D sets up and solves linear systems needed by SMOOTH.

  Discussion:

  This routine constructs the upper three diagonals of

  V(I,J), I = 2 to NPOINT-1, J=1,3,

  of the matrix

  6 * (1-P) * Q' * (D**2) * Q + P * R.

  It then computes its L*L' decomposition and stores it also
  in V, then applies forward and back substitution to the right hand side

  Q'*Y

  in QTY to obtain the solution in U.

  Modified:

  16 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) P, the smoothing parameter that defines
  the linear system.

  Input/output, real ( kind = 8 ) V(NPOINT,7), contains data used
  to define the linear system, some of which is determined by
  routine SETUPQ.

  Input, real ( kind = 8 ) QTY(NPOINT), the value of Q' * Y.

  Input, integer ( kind = 4 ) NPOINT, the number of equations.

  Input, integer ( kind = 4 ) NCOL, an unused parameter, which may be
  set to 1.

  Output, real ( kind = 8 ) U(NPOINT), the solution.

  Output, real ( kind = 8 ) QU(NPOINT), the value of Q * U.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `colloc`
- **Signature:** `Subroutine colloc(aleft, aright, lbegin, iorder, ntimes, addbrk, relerr)`
- **Purpose:** *****************************************************************************80

  ! COLLOC solves an ordinary differential equation by collocation.

  Method:

  The M-th order ordinary differential equation with M side
  conditions, to be specified in subroutine DIFEQU, is solved
  approximately by collocation.

  The approximation F to the solution G is piecewise polynomial of order
  K+M with L pieces and M-1 continuous derivatives.   F is determined by
  the requirement that it satisfy the differential equation at K points
  per interval (to be specified in COLPNT ) and the M side conditions.

  This usually nonlinear system of equations for F is solved by
  Newton's method. the resulting linear system for the B-coefficients of an
  iterate is constructed appropriately in EQBLOK and then solved
  in SLVBLK, a program designed to solve almost block
  diagonal linear systems efficiently.

  There is an opportunity to attempt improvement of the breakpoint
  sequence, both in number and location, through the use of NEWNOT.

  Printed output consists of the piecewise polynomial representation
  of the approximate solution, and of the error at selected points.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) ALEFT, ARIGHT, the endpoints of the interval.

  Input, integer ( kind = 4 ) LBEGIN, the initial number of polynomial
  pieces in the approximation.  A uniform breakpoint sequence will be chosen.

  Input, integer ( kind = 4 ) IORDER, the order of the polynomial pieces
  to be used in the approximation

  Input, integer ( kind = 4 ) NTIMES, the number of passes to be made
  through NEWNOT.

  Input, real ( kind = 8 ) ADDBRK, the number, possibly fractional, of
  breaks to be added per pass through NEWNOT.  For instance, if
  ADDBRK = 0.33334, then a breakpoint will be added at every third pass
  through NEWNOT.

  Input, real ( kind = 8 ) RELERR, a tolerance.  Newton iteration is
  stopped if the difference between the B-coefficients of two successive
  iterates is no more than RELERR*(absolute largest B-coefficient).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `colpnt`
- **Signature:** `Subroutine colpnt(k, rho)`
- **Purpose:** *****************************************************************************80

  ! COLPNT supplies collocation points.

  Discussion:

  The collocation points are for the standard interval (-1,1) as the
  zeros of the Legendre polynomial of degree K, provided K <= 8.

  Otherwise, uniformly spaced points are given.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, integer ( kind = 4 ) K, the number of collocation points desired.

  Output, real ( kind = 8 ) RHO(K), the collocation points.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cubspl`
- **Signature:** `Subroutine cubspl(tau, c, n, ibcbeg, ibcend)`
- **Purpose:** *****************************************************************************80

  ! CUBSPL defines an interpolatory cubic spline.

  Discussion:

  A tridiagonal linear system for the unknown slopes S(I) of
  F at TAU(I), I=1,..., N, is generated and then solved by Gauss
  elimination, with S(I) ending up in C(2,I), for all I.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) TAU(N), the abscissas or X values of
  the data points.  The entries of TAU are assumed to be
  strictly increasing.

  Input, integer ( kind = 4 ) N, the number of data points.  N is
  assumed to be at least 2.

  Input/output, real ( kind = 8 ) C(4,N).
  On input, if IBCBEG or IBCBEG is 1 or 2, then C(2,1)
  or C(2,N) should have been set to the desired derivative
  values, as described further under IBCBEG and IBCEND.
  On output, C contains the polynomial coefficients of
  the cubic interpolating spline with interior knots
  TAU(2) through TAU(N-1).
  In the interval interval (TAU(I), TAU(I+1)), the spline
  F is given by
  F(X) =
  C(1,I) +
  C(2,I) * H +
  C(3,I) * H**2 / 2 +
  C(4,I) * H**3 / 6.
  where H=X-TAU(I).  The routine PPVALU may be used to
  evaluate F or its derivatives from TAU, C, L=N-1,
  and K=4.

  Input, integer ( kind = 4 ) IBCBEG, IBCEND, boundary condition indicators.
  IBCBEG = 0 means no boundary condition at TAU(1) is given.
  In this case, the "not-a-knot condition" is used.  That
  is, the jump in the third derivative across TAU(2) is
  forced to zero.  Thus the first and the second cubic
  polynomial pieces are made to coincide.
  IBCBEG = 1 means the slope at TAU(1) is to equal the
  input value C(2,1).
  IBCBEG = 2 means the second derivative at TAU(1) is
  to equal C(2,1).
  IBCEND = 0, 1, or 2 has analogous meaning concerning the
  boundary condition at TAU(N), with the additional
  information taken from C(2,N).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cwidth`
- **Signature:** `Subroutine cwidth(w, b, nequ, ncols, integs, nbloks, d, x, iflag)`
- **Purpose:** *****************************************************************************80

  ! CWIDTH solves an almost block diagonal linear system.

  Discussion:

  This routine is a variation of the theme in the algorithm
  by Martin and Wilkinson.  It solves the linear system

  A * X = B

  of NEQU equations in case A is almost block diagonal with all
  blocks having NCOLS columns using no more storage than it takes to
  store the interesting part of A.  Such systems occur in the determination
  of the B-spline coefficients of a spline approximation.

  Block structure of A:

  The interesting part of A is taken to consist of NBLOKS
  consecutive blocks, with the I-th block made up of NROWI = INTEGS(1,I)
  consecutive rows and NCOLS consecutive columns of A, and with
  the first LASTI = INTEGS(2,I) columns to the left of the next block.
  These blocks are stored consecutively in the work array W.

  For example, here is an 11th order matrix and its arrangement in
  the work array W.  (The interesting entries of A are indicated by
  their row and column index modulo 10.)

  ---   A   ---                          ---   W   ---

  NROW1=3
  11 12 13 14                                     11 12 13 14
  21 22 23 24                                     21 22 23 24
  31 32 33 34      NROW2=2                        31 32 33 34
  LAST1=2      43 44 45 46                               43 44 45 46
  53 54 55 56         NROW3=3               53 54 55 56
  LAST2=3         66 67 68 69                      66 67 68 69
  76 77 78 79                      76 77 78 79
  86 87 88 89   NROW4=1            86 87 88 89
  LAST3=1   97 98 99 90   NROW5=2         97 98 99 90
  LAST4=1   08 09 00 01                08 09 00 01
  18 19 10 11                18 19 10 11
  LAST5=4

  For this interpretation of A as an almost block diagonal matrix,
  we have NBLOKS = 5, and the INTEGS array is

  I = 1   2   3   4   5
  K =
  INTEGS(K,I) =      1      3   2   3   1   2
  2      2   3   1   1   4

  Method:

  Gauss elimination with scaled partial pivoting is used, but
  multipliers are not saved in order to save storage.  Rather, the
  right hand side is operated on during elimination.  The two parameters
  IPVTEQ and LASTEQ are used to keep track of the action.  IPVTEQ
  is the index of the variable to be eliminated next, from equations
  IPVTEQ+1,...,LASTEQ, using equation IPVTEQ, possibly after an
  interchange, as the pivot equation.

  The entries in the pivot column are always in column
  1 of W.  This is accomplished by putting the entries in rows
  IPVTEQ+1,...,LASTEQ revised by the elimination of the IPVTEQ-th
  variable one to the left in W.  In this way, the columns of the
  equations in a given block, as stored in W, will be aligned with
  those of the next block at the moment when these next equations
  become involved in the elimination process.

  Thus, for the above example, the first elimination steps proceed
  as follows.

  *11 12 13 14    11 12 13 14    11 12 13 14    11 12 13 14
  *21 22 23 24   *22 23 24       22 23 24       22 23 24
  *31 32 33 34   *32 33 34      *33 34          33 34
  43 44 45 46    43 44 45 46   *43 44 45 46   *44 45 46
  53 54 55 56    53 54 55 56   *53 54 55 56   *54 55 56
  66 67 68 69    66 67 68 69    66 67 68 69    66 67 68 69

  In all other respects, the procedure is standard, including the
  scaled partial pivoting.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Roger Martin, James Wilkinson,
  Solution of Symmetric and Unsymmetric Band Equations and
  the Calculation of Eigenvectors of Band Matrices,
  Numerische Mathematik,
  Volume 9, Number 4, December 1976, pages 279-301.

  Parameters:

  Input/output, real ( kind = 8 ) W(NEQU,NCOLS), on input, contains
  the interesting part of the almost block diagonal coefficient matrix
  A.  The array INTEGS describes the storage scheme.  On output, W
  contains the upper triangular factor U of the LU factorization of a
  possibly permuted version of A.  In particular, the determinant of
  A could now be found as
  IFLAG * W(1,1) * W(2,1) * ... * W(NEQU,1).

  Input/output, real ( kind = 8 ) B(NEQU); on input, the right hand
  side of the linear system.  On output, B has been overwritten by
  other information.

  Input, integer ( kind = 4 ) NEQU, the number of equations.

  Input, integer ( kind = 4 ) NCOLS, the block width, that is, the number of
  columns in each block.

  Input, integer ( kind = 4 ) INTEGS(2,NEQU), describes the block structure
  of A.
  INTEGS(1,I) = number of rows in block I = NROW.
  INTEGS(2,I) = number of elimination steps in block I = overhang over
  next block = LAST.

  Input, integer ( kind = 4 ) NBOKS, the number of blocks.

  Workspace, real D(NEQU), used to contain row sizes.  If storage is
  scarce, the array X could be used in the calling sequence for D.

  Output, real ( kind = 8 ) X(NEQU), the computed solution, if
  IFLAG is nonzero.

  Output, integer ( kind = 4 ) IFLAG, error flag.
  = (-1)**(number of interchanges during elimination) if A is invertible;
  = 0 if A is singular.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `difequ`
- **Signature:** `Subroutine difequ(mode, xx, v)`
- **Purpose:** *****************************************************************************80

  ! DIFEQU returns information about a differential equation.

  Discussion:

  This sample version of DIFEQU is for the example in chapter XV.  It is a
  nonlinear second order two point boundary value problem.

  Modified:

  16 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, integer ( kind = 4 ) MODE, an integer indicating the task to
  be performed.
  1, initialization
  2, evaluate the differential equation at point XX.
  3, specify the next side condition
  4, analyze the approximation

  Input, real ( kind = 8 ) XX, a point at which information is wanted

  Output, real ( kind = 8 ) V, depends on the MODE.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `dtblok`
- **Signature:** `Subroutine dtblok(bloks, integs, nbloks, ipivot, iflag, detsgn, detlog)`
- **Purpose:** *****************************************************************************80

  ! DTBLOK gets the determinant of an almost block diagonal matrix.

  Discussion:

  The matrix's PLU factorization must have been obtained
  previously by FCBLOK.

  The logarithm of the determinant is computed instead of the
  determinant itself to avoid the danger of overflow or underflow
  inherent in this calculation.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) BLOKS(*), the factorization of A computed
  by FCBLOK.

  Input, integer ( kind = 4 ) INTEGS(3,NBLOKS), describes the block
  structure of A.

  Input, integer ( kind = 4 ) NBLOKS, the number of blocks in A.

  Input, integer ( kind = 4 ) IPIVOT(*), pivoting information.
  The dimension of IPIVOT is the sum ( INTEGS(1,1:NBLOKS) ).

  Input, integer ( kind = 4 ) IFLAG, = (-1)**(number of interchanges during
  factorization) if successful, otherwise IFLAG = 0.

  Output, real ( kind = 8 ) DETSGN, the sign of the determinant.

  Output, real ( kind = 8 ) DETLOG, the natural logarithm of the
  determinant, if the determinant is not zero.  If the determinant
  is 0, then DETLOG is returned as 0.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `eqblok`
- **Signature:** `Subroutine eqblok(t, n, kpm, work1, work2, bloks, lenblk, integs, nbloks, b)`
- **Purpose:** *****************************************************************************80

  ! EQBLOK is to be called in COLLOC.

  Method:

  Each breakpoint interval gives rise to a block in the linear system.
  This block is determined by the K collocation equations in the interval
  with the side conditions, if any, in the interval interspersed
  appropriately, and involves the KPM B-splines having the interval in
  their support.  Correspondingly, such a block has NROW = K + ISIDEL
  rows, with ISIDEL = number of side conditions in this and the
  previous intervals, and NCOL = KPM columns.

  Further, because the interior knots have multiplicity K, we can
  carry out in SLVBLK K elimination steps in a block before pivoting
  might involve an equation from the next block.  In the last block,
  of course, all KPM elimination steps will be carried out in SLVBLK.

  See the detailed comments in SLVBLK for further
  information about the almost block diagonal form used here.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) T(N+KPM), the knot sequence.

  Input, integer ( kind = 4 ) N, the dimension of the approximating spline
  space, that is, the order of the linear system to be constructed.

  Input, integer ( kind = 4 ) KPM, = K + M, the order of the approximating
  spline.

  Input, integer ( kind = 4 ) LENBLK, the maximum length of the array BLOKS,
  as allowed by the dimension statement in COLLOC.

  Workspace, real ( kind = 8 ) WORK1(KPM,KPM), used in PUTIT.

  Workspace, real ( kind = 8 ) WORK2(KPM,M+1), used in PUTIT.

  Output, real ( kind = 8 ) BLOKS(*), the coefficient matrix of the
  linear system, stored in almost block diagonal form, of size
  KPM * sum ( INTEGS(1,1:NBLOKS) ).

  Output, integer ( kind = 4 ) INTEGS(3,NBLOKS), describing the block
  structure.
  INTEGS(1,I) = number of rows in block I;
  INTEGS(2,I) = number of columns in block I;
  INTEGS(3,I) = number of elimination steps which can be carried out in
  block I before pivoting might bring in an equation from the next block.

  Output, integer ( kind = 4 ) NBLOKS, the number of blocks, equals number
  of polynomial pieces.

  Output, real ( kind = 8 ) B(*), the right hand side of the linear
  system, stored corresponding to the almost block diagonal form,
  of size sum ( INTEGS(1,1:NBLOKS) ).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `evnnot`
- **Signature:** `Subroutine evnnot(break, coef, l, k, brknew, lnew, coefg)`
- **Purpose:** *****************************************************************************80

  ! EVNNOT is a version of NEWNOT returning uniform knots.

  Discussion:

  EVNNOT returns LNEW+1 knots in BRKNEW which are evenly spaced between
  BREAK(1) and BREAK(L+1).

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) BREAK(L+1), real ( kind = 8 ) COEF(K,L),
  integer ( kind = 4 ) L, integer K, the piecewise polynomial representation
  of a certain function F of order K.  Specifically,
  d**(K-1) F(X) = COEF(K,I) for BREAK(I) <= X < BREAK(I+1).

  Input, integer ( kind = 4 ) LNEW, the number of subintervals into which
  the interval (A,B) is to be sectioned by the new breakpoint
  sequence BRKNEW.

  Output, real ( kind = 8 ) BRKNEW(LNEW+1), the new breakpoints.

  Output, real (kind = 8 ) COEFG(2,L), the coefficient part of the
  piecewise polynomial representation BREAK, COEFG, L, 2 for the monotone
  piecewise linear function G with respect to which BRKNEW will
  be equidistributed.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `factrb`
- **Signature:** `Subroutine factrb(w, ipivot, d, nrow, ncol, last, iflag)`
- **Purpose:** *****************************************************************************80

  ! FACTRB constructs a partial PLU factorization.

  Discussion:

  This factorization corresponds to steps 1 through LAST in Gauss
  elimination for the matrix W of order ( NROW, NCOL ), using
  pivoting of scaled rows.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input/output, real ( kind = 8 ) W(NROW,NCOL); on input, contains the
  matrix to be partially factored; on output, the partial factorization.

  Output, integer ( kind = 4 ) IPIVOT(NROW), contains a record of the
  pivoting strategy used; row IPIVOT(I) is used during the I-th elimination
  step, for I = 1, ..., LAST.

  Workspace, real ( kind = 8 ) D(NROW), used to store the maximum entry
  in each row.

  Input, integer ( kind = 4 ) NROW, the number of rows of W.

  Input, integer ( kind = 4 ) NCOL, the number of columns of W.

  Input, integer ( kind = 4 ) LAST, the number of elimination steps to
  be carried out.

  Input/output, integer ( kind = 4 ) IFLAG.  On output, equals the input
  value times (-1)**(number of row interchanges during the factorization
  process), in case no zero pivot was encountered.
  Otherwise, IFLAG = 0 on output.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `fcblok`
- **Signature:** `Subroutine fcblok(bloks, integs, nbloks, ipivot, scrtch, iflag)`
- **Purpose:** *****************************************************************************80

  ! FCBLOK supervises the PLU factorization of an almost block diagonal matrix.

  Discussion:

  The routine supervises the PLU factorization with pivoting of
  the scaled rows of an almost block diagonal matrix.

  The almost block diagonal matrix is stored in the arrays
  BLOKS and INTEGS.

  The FACTRB routine carries out steps 1,..., LAST of Gauss
  elimination, with pivoting, for an individual block.

  The SHIFTB routine shifts the remaining rows to the top of
  the next block.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input/output, real ( kind = 8 ) BLOKS(*).  On input, the almost
  block diagonal matrix A to be factored.  On output, the
  factorization of A.

  Input, integer ( kind = 4 ) INTEGS(3,NBLOKS), describes the block
  structure of A.

  Input, integer ( kind = 4 ) NBLOKS, the number of blocks in A.

  Output, integer ( kind = 4 ) IPIVOT(*), which will contain pivoting
  information.  The dimension of IPIVOT is the sum ( INTEGS(1,1:NBLOKS) ).

  Workspace, real SCRTCH(*), of length maxval ( integs(1,1:NBLOKS) ).

  Output, integer ( kind = 4 ) IFLAG, error flag.
  = 0,  in case matrix was found to be singular;
  = (-1)**(number of row interchanges during factorization), otherwise.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `interv`
- **Signature:** `Subroutine interv(xt, lxt, x, left, mflag)`
- **Purpose:** *****************************************************************************80

  ! INTERV brackets a real value in an ascending vector of values.

  Discussion:

  The XT array is a set of increasing values.  The goal of the routine
  is to determine the largest index I so that XT(I) <= X.

  The routine is designed to be efficient in the common situation
  that it is called repeatedly, with X taken from an increasing
  or decreasing sequence.

  This will happen when a piecewise polynomial is to be graphed.
  The first guess for LEFT is therefore taken to be the value
  returned at the previous call and stored in the local variable ILO.

  A first check ascertains that ILO < LXT.  This is necessary
  since the present call may have nothing to do with the previous
  call.  Then, if

  XT(ILO) <= X < XT(ILO+1),

  we set LEFT = ILO and are done after just three comparisons.

  Otherwise, we repeatedly double the difference ISTEP = IHI - ILO
  while also moving ILO and IHI in the direction of X, until

  XT(ILO) <= X < XT(IHI)

  after which we use bisection to get, in addition, ILO + 1 = IHI.
  The value LEFT = ILO is then returned.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) XT(LXT), a nondecreasing sequence of values.

  Input, integer ( kind = 4 ) LXT, the dimension of XT.

  Input, real ( kind = 8 ) X, the point whose location with
  respect to the sequence XT is to be determined.

  Output, integer ( kind = 4 ) LEFT, the index of the bracketing value:
  1     if             X  <  XT(1)
  I     if   XT(I)  <= X  < XT(I+1)
  LXT   if  XT(LXT) <= X

  Output, integer ( kind = 4 ) MFLAG, indicates whether X lies within the
  range of the data.
  -1:            X  <  XT(1)
  0: XT(I)   <= X  < XT(I+1)
  +1: XT(LXT) <= X
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `knots`
- **Signature:** `Subroutine knots(break, l, kpm, m, t, n)`
- **Purpose:** *****************************************************************************80

  ! KNOTS is to be called in COLLOC.

  Discussion:

  Note that the FORTRAN77 calling sequence has been modified, by
  adding the variable M.

  From the given breakpoint sequence BREAK, this routine constructs the
  knot sequence T so that

  SPLINE(K+M,T) = PP(K+M,BREAK)

  with M-1 continuous derivatives.

  This means that T(1:N+KPM) is equal to BREAK(1) KPM times, then
  BREAK(2) through BREAK(L) each K times, then, finally, BREAK(L+1)
  KPM times.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) BREAK(L+1), the breakpoint sequence.

  Input, integer ( kind = 4 ) L, the number of intervals or pieces.

  Input, integer ( kind = 4 ) KPM, = K+M, the order of the piecewise
  polynomial function or spline.

  Input, integer ( kind = 4 ) M, the order of the differential equation.

  Output, real ( kind = 8 ) T(N+KPM), the knot sequence.

  Output, integer ( kind = 4 ) N, = L*K+M = the dimension of SPLINE(K+M,T).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `l2appr`
- **Signature:** `Subroutine l2appr(t, n, k, q, diag, bcoef)`
- **Purpose:** *****************************************************************************80

  ! L2APPR constructs a weighted L2 spline approximation to given data.

  Discussion:

  The routine constructs the weighted discrete L2-approximation by
  splines of order K with knot sequence T(1:N+K) to
  given data points ( TAU(1:NTAU), GTAU(1:NTAU) ).

  The B-spline coefficients BCOEF of the approximating spline are
  determined from the normal equations using Cholesky's method.

  Method:

  The B-spline coefficients of the L2-approximation are determined as the
  solution of the normal equations, for 1 <= I <= N:

  sum ( 1 <= J <= N ) ( B(I), B(J) ) * BCOEF(J) = ( B(I), G ).

  Here, B(I) denotes the I-th B-spline, G denotes the function to
  be approximated, and the inner product of two functions F and G
  is given by

  ( F, G ) = sum ( 1 <= I <= NTAU ) WEIGHT(I) * F(TAU(I)) * G(TAU(I)).

  The arrays TAU and WEIGHT are given in common block DATA, as is the
  array GTAU(1:NTAU) = G(TAU(1:NTAU)).

  The values of the B-splines B(1:N) are supplied by BSPLVB.

  The coefficient matrix C, with

  C(I,J) = ( B(I), B(J) )

  of the normal equations is symmetric and (2*K-1)-banded, therefore
  can be specified by giving its K bands at or below the diagonal.

  For I = 1:N and J = I:min(I+K-1,N), we store

  ( B(I), B(J) ) = C(I,J)

  in

  Q(I-J+1,J),

  and the right hand side

  ( B(I), G )

  in

  BCOEF(I).

  Since B-spline values are most efficiently generated by finding
  simultaneously the value of every nonzero B-spline at one point,
  the entries of C (that is, of Q), are generated by computing, for
  each LL, all the terms involving TAU(LL) simultaneously and adding
  them to all relevant entries.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) T(N+K), the knot sequence.

  Input, integer ( kind = 4 ) N, the dimension of the space of splines
  of order K with knots T.

  Input, integer ( kind = 4 ) K, the order of the splines.

  Workspace, real ( kind = 8 ) Q(K,N), used to store the K lower
  diagonals of the Gramian matrix C.

  Workspace, real ( kind = 8 ) DIAG(N), used in BCHFAC.

  Output, real ( kind = 8 ) BCOEF(N), the B-spline coefficients of
  the L2 approximation to the data.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `l2err`
- **Signature:** `Subroutine l2err(iprfun, ftau, error)`
- **Purpose:** *****************************************************************************80

  ! L2ERR computes the errors of an L2 approximation.

  Discussion:

  This routine computes various errors of the current L2 approximation,
  whose piecewise polynomial representation is contained in common
  block APPROX, to the given data contained in common block DATA.

  It prints out the average error ERRL1, the L2 error ERRL2, and the
  maximum error ERRMAX.

  Modified:

  16 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, integer ( kind = 4 ) IPRFUN.  If IPRFUN = 1, the routine prints out
  the value of the approximation as well as its error at
  every data point.

  Output, real ( kind = 8 ) FTAU(NTAU), contains the value of the computed
  approximation at each value TAU(1:NTAU).

  Output, real ( kind = 8 ) ERROR(NTAU), with
  ERROR(I) = SCALE * ( G - F )(TAU(I)).  Here, SCALE equals 1
  in case IPRFUN /= 1, or the absolute error is greater than 100
  somewhere.  Otherwise, SCALE is such that the maximum of the
  absolute value of ERROR(1:NTAU) lies between 10 and 100.  This
  makes the printed output more illustrative.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `l2knts`
- **Signature:** `Subroutine l2knts(break, l, k, t, n)`
- **Purpose:** *****************************************************************************80

  ! L2KNTS converts breakpoints to knots.

  Discussion:

  The breakpoint sequence BREAK is converted into a corresponding
  knot sequence T to allow the representation of a piecewise
  polynomial function of order K with K-2 continuous derivatives
  as a spline of order K with knot sequence T.

  This means that T(1:N+K) = BREAK(1) K times, then BREAK(2:L),
  then BREAK(L+1) K times.

  Therefore, N = K - 1 + L.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, integer ( kind = 4 ) K, the order.

  Input, integer ( kind = 4 ) L, the number of polynomial pieces.

  Input, real ( kind = 8 ) BREAK(L+1), the breakpoint sequence.

  Output, real ( kind = 8 ) T(N+K), the knot sequence.

  Output, integer ( kind = 4 ) N, the dimension of the corresponding spline
  space of order K.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `newnot`
- **Signature:** `Subroutine newnot(break, coef, l, k, brknew, lnew, coefg)`
- **Purpose:** *****************************************************************************80

  ! NEWNOT returns LNEW+1 knots which are equidistributed on (A,B).

  Discussion:

  The knots are equidistributed on (A,B) = ( BREAK(1), BREAK(L+1) )
  with respect to a certain monotone function G related to the K-th root of
  the K-th derivative of the piecewise polynomial function F whose
  piecewise polynomial representation is contained in BREAK, COEF, L, K.

  Method:

  The K-th derivative of the given piecewise polynomial function F does
  not exist, except perhaps as a linear combination of delta functions.

  Nevertheless, we construct a piecewise constant function H with
  breakpoint sequence BREAK which is approximately proportional
  to abs ( d**K(F) ).

  Specifically, on (BREAK(I), BREAK(I+1)),

  abs(jump at BREAK(I) of PC)     abs(jump at BREAK(I+1) of PC)
  H = ---------------------------  +  ----------------------------
  BREAK(I+1) - BREAK(I-1)         BREAK(I+2) - BREAK(I)

  with PC the piecewise constant (K-1)st derivative of F.

  Then, the piecewise linear function G is constructed as

  G(X) = integral ( A <= Y <= X )  H(Y)**(1/K) dY,

  and its piecewise polynomial coefficients are stored in COEFG.

  Then BRKNEW is determined by

  BRKNEW(I) = A + G**(-1)((I-1)*STEP), for I = 1:LNEW+1,

  where STEP = G(B) / LNEW and (A,B) = ( BREAK(1), BREAK(L+1) ).

  In the event that PC = d**(K-1)(F) is constant in ( A, B ) and
  therefore H = 0 identically, BRKNEW is chosen uniformly spaced.

  If IPRINT is set positive, then the piecewise polynomial coefficients
  of G will be printed out.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) BREAK(L+1), real ( kind = 8 ) COEF(K,L),
  integer ( kind = 4 ) L, integer K, the piecewise polynomial representation
  of a certain function F of order K.  Specifically,
  d**(k-1) F(X) = COEF(K,I) for BREAK(I) <= X < BREAK(I+1).

  Input, integer ( kind = 4 ) LNEW, the number of intervals into which the
  interval (A,B) is to be divided by the new breakpoint sequence BRKNEW.

  Output, real ( kind = 8 ) BRKNEW(LNEW+1), the new breakpoint sequence.

  Output, real ( kind = 8 ) COEFG(2,L), the coefficient part of the piecewise
  polynomial representation BREAK, COEFG, L, 2 for the monotone piecewise
  linear function G with respect to which BRKNEW will be equidistributed.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `ppvalu`
- **Signature:** `Function ppvalu(break, coef, l, k, x, jderiv)`
- **Purpose:** *****************************************************************************80

  ! PPVALU evaluates a piecewise polynomial function or its derivative.

  Discussion:

  PPVALU calculates the value at X of the JDERIV-th derivative of
  the piecewise polynomial function F from its piecewise
  polynomial representation.

  The interval index I, appropriate for X, is found through a
  call to INTERV.  The formula for the JDERIV-th derivative
  of F is then evaluated by nested multiplication.

  The J-th derivative of F is given by:

  (d**J) F(X) =
  COEF(J+1,I) + H * (
  COEF(J+2,I) + H * (
  ...
  COEF(K-1,I) + H * (
  COEF(K,  I) / (K-J-1) ) / (K-J-2) ... ) / 2 ) / 1

  with

  H = X - BREAK(I)

  and

  I = max ( 1, max ( J, BREAK(J) <= X, 1 <= J <= L ) ).

  Modified:

  16 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) BREAK(L+1), real COEF(*), integer L, the
  piecewise polynomial representation of the function F to be evaluated.

  Input, integer ( kind = 4 ) K, the order of the polynomial pieces that
  make up the function F.  The usual value for K is 4, signifying a
  piecewise cubic polynomial.

  Input, real ( kind = 8 ) X, the point at which to evaluate F or
  of its derivatives.

  Input, integer ( kind = 4 ) JDERIV, the order of the derivative to be
  evaluated.  If JDERIV is 0, then F itself is evaluated,
  which is actually the most common case.  It is assumed
  that JDERIV is zero or positive.

  Output, real ( kind = 8 ) PPVALU, the value of the JDERIV-th
  derivative of F at X.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `putit`
- **Signature:** `Subroutine putit(t, kpm, left, scrtch, dbiatx, q, nrow, b)`
- **Purpose:** *****************************************************************************80

  ! PUTIT puts together one block of the collocation equation system.

  Method:

  The K collocation equations for the interval ( T(LEFT), T(LEFT+1) )
  are constructed with the aid of the subroutine DIFEQU( 2, ., . )
  and interspersed (in order) with the side conditions, if any, in
  this interval, using DIFEQU ( 3, ., . )  for the information.

  The block Q has KPM columns, corresponding to the KPM B-splines of order
  KPM which have the interval ( T(LEFT), T(LEFT+1) ) in their support.

  The block's diagonal is part of the diagonal of the total system.

  The first equation in this block not overlapped by the preceding block
  is therefore equation LOWROW, with LOWROW = number of side conditions
  in preceding intervals (or blocks).

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) T(LEFT+KPM), the knot sequence.

  Input, integer ( kind = 4 ) KPM, the order of the spline.

  Input, integer ( kind = 4 ) LEFT, indicates the interval of interest,
  that is, the interval ( T(LEFT), T(LEFT+1) ).

  Workspace, real ( kind = 8 ) SCRTCH(KPM,KPM).

  Workspace, real ( kind = 8 ) DBIATX(KPM,M+1), derivatives of B-splines,
  with DBIATX(J,I+1) containing the I-th derivative of the J-th B-spline
  of interest.

  Output, real ( kind = 8 ) Q(NROW,KPM), the block.

  Input, integer ( kind = 4 ) NROW, number of rows in block to be
  !   put together.

  Output, real ( kind = 8 ) B(NROW), the corresponding piece of
  the right hand side.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `round`
- **Signature:** `Function round(x, size)`
- **Purpose:** *****************************************************************************80

  ! ROUND is called to add some noise to data.

  Discussion:

  This function simply adds plus or minus a perturbation value
  to the input data.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input. real ( kind = 8 ) X, the value to be perturbed.

  Input, real ( kind = 8 ) SIZE, the size of the perturbation.

  Output, real ( kind = 8 ) ROUND, the perturbed value.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `sbblok`
- **Signature:** `Subroutine sbblok(bloks, integs, nbloks, ipivot, b, x)`
- **Purpose:** *****************************************************************************80

  ! SBBLOK solves a linear system that was factored by FCBLOK.

  Discussion:

  The routine supervises the solution, by forward and backward
  substitution, of the linear system

  A * x = b

  for X, with the PLU factorization of A already generated in FCBLOK.
  Individual blocks of equations are solved via SUBFOR and SUBBAK.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) BLOKS(*), integer INTEGS(3,NBLOKS), integer
  NBLOKS, integer IPIVOT(*), are as on return from FCBLOK.

  Input, real ( kind = 8 ) B(*), the right hand side, stored corresponding
  to the storage of the equations.  See comments in SLVBLK for details.

  Output, real ( kind = 8 ) X(*), the solution vector.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `setupq`
- **Signature:** `Subroutine setupq(x, dx, y, npoint, v, qty)`
- **Purpose:** *****************************************************************************80

  ! SETUPQ is to be called in SMOOTH.

  Discussion:

  Put DELX = X(*+1) - X(*) into V(*,4).

  Put the three bands of Q' * D into V(*,1:3).

  Put the three bands of ( D * Q )' * ( D * Q ) at and above the diagonal
  into V(*,5:7).

  Here, Q is the tridiagonal matrix of order ( NPOINT-2, NPOINT )
  with general row

  1/DELX(I), -1/DELX(I)-1/DELX(I+1), 1/DELX(I+1)

  and D is the diagonal matrix with general row DX(I).

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) X(NPOINT), the abscissas, assumed to be
  strictly increasing.

  Input, real ( kind = 8 ) DX(NPOINT), the data uncertainty estimates,
  which are assumed to be positive.

  Input, real ( kind = 8 ) Y(NPOINT), the corresponding ordinates.

  Input, integer ( kind = 4 ) NPOINT, the number of data points.

  Output, real ( kind = 8 ) V(NPOINT,7), contains data needed for
  the smoothing computation.

  Output, real ( kind = 8 ) QTY(NPOINT), the value of Q' * Y.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `shiftb`
- **Signature:** `Subroutine shiftb(ai, ipivot, nrowi, ncoli, last, ai1, nrowi1, ncoli1)`
- **Purpose:** *****************************************************************************80

  ! SHIFTB shifts the rows in the current block.

  Discussion:

  This routine shifts rows in the current block, AI, which are not used
  as pivot rows, if any, that is, rows IPIVOT(LAST+1) through IPIVOT(NROWI),
  onto the first MMAX = NROW - LAST rows of the next block, AI1,
  with column LAST + J of AI going to column J,
  for J = 1,..., JMAX = NCOLI - LAST.

  The remaining columns of these rows of AI1 are zeroed out.

  Diagram:

  Original situation after         Results in a new block I+1
  LAST = 2 columns have been       created and ready to be
  done in FACTRB, assuming no      factored by next FACTRB call.
  interchanges of rows.

  1
  X  X 1X  X  X           X  X  X  X  X
  1
  0  X 1X  X  X           0  X  X  X  X
  BLOCK I          1                       ---------------
  NROWI=4     0  0 1X  X  X           0  0 1X  X  X  0  01
  NCOLI=5          1                       1             1
  LAST=2      0  0 1X  X  X           0  0 1X  X  X  0  01
  -------------------          1             1   NEW
  1X  X  X  X  X          1X  X  X  X  X1  BLOCK
  1                       1             1   I+1
  BLOCK I+1        1X  X  X  X  X          1X  X  X  X  X1
  NROWI1= 5        1                       1             1
  NCOLI1= 5        1X  X  X  X  X          1X  X  X  X  X1
  -------------------          1-------------1
  1

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) AI(NROWI,NCOLI), the current block.

  Input, integer ( kind = 4 ) IPIVOT(NROWI), the pivot vector.

  Input, integer ( kind = 4 ) NROWI, NCOLI, the number of rows and columns
  in block AI.

  Input, integer ( kind = 4 ) LAST, indicates the last row on which pivoting
  has been carried out.

  Input/output, real ( kind = 8 ) AI1(NROWI1,NCOLI1), the next block.

  Input, integer ( kind = 4 ) NROWI1, NCOLI1, the number of rows and columns
  in block AI1.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `slvblk`
- **Signature:** `Subroutine slvblk(bloks, integs, nbloks, b, ipivot, x, iflag)`
- **Purpose:** *****************************************************************************80

  ! SLVBLK solves the almost block diagonal linear system A * x = b.

  Discussion:

  Such almost block diagonal matrices arise naturally in piecewise
  polynomial interpolation or approximation and in finite element
  methods for two-point boundary value problems.  The PLU factorization
  method is implemented here to take advantage of the special structure
  of such systems for savings in computing time and storage requirements.

  SLVBLK relies on several auxiliary programs:

  FCBLOK (BLOKS,INTEGS,NBLOKS,IPIVOT,SCRTCH,IFLAG)
  factors the matrix A.

  SBBLOK (BLOKS,INTEGS,NBLOKS,IPIVOT,B,X)
  solves the system A*X=B once A is factored.

  DTBLOK (BLOKS,INTEGS,NBLOKS,IPIVOT,IFLAG,DETSGN,DETLOG)
  computes the determinant of A once it has been factored.

  Block structure of A:

  The NBLOKS blocks are stored consecutively in the array BLOKS.

  The first block has its (1,1)-entry at BLOKS(1), and, if the I-th
  block has its (1,1)-entry at BLOKS(INDEX(I)), then

  INDEX(I+1) = INDEX(I) + NROW(I) * NCOL(I).

  The blocks are pieced together to give the interesting part of A
  as follows.  For I=1,2,..., NBLOKS-1, the (1,1)-entry of the next
  block (the (I+1)st block) corresponds to the (LAST+1,LAST+1)-entry
  of the current I-th block.  Recall LAST = INTEGS(3,I) and note that
  this means that

  A: every block starts on the diagonal of A.

  B: the blocks overlap (usually). the rows of the (I+1)st block
  which are overlapped by the I-th block may be arbitrarily
  defined initially.  They are overwritten during elimination.

  The right hand side for the equations in the I-th block are stored
  correspondingly as the last entries of a piece of B of length NROW
  (= INTEGS(1,I)) and following immediately in B the corresponding
  piece for the right hand side of the preceding block, with the right
  hand side for the first block starting at B(1).  In this, the right
  hand side for an equation need only be specified once on input,
  in the first block in which the equation appears.

  Example:

  The test driver for this package contains an example, a linear
  system of order 11, whose nonzero entries are indicated in the
  following diagram by their row and column index modulo 10.  Next to it
  are the contents of the INTEGS arrray when the matrix is taken to
  be almost block diagonal with NBLOKS = 5, and below it are the five
  blocks.

  NROW1 = 3, NCOL1 = 4
  11 12 13 14
  21 22 23 24   NROW2 = 3, NCOL2 = 3
  31 32 33 34
  LAST1 = 2      43 44 45
  53 54 55            NROW3 = 3, NCOL3 = 4
  LAST2 = 3         66 67 68 69   NROW4 = 3, NCOL4 = 4
  76 77 78 79      NROW5 = 4, NCOL5 = 4
  86 87 88 89
  LAST3 = 1   97 98 99 90
  LAST4 = 1   08 09 00 01
  18 19 10 11
  LAST5 = 4

  Actual input to BLOKS shown by rows of blocks of A.
  The ** items are arbitrary.

  11 12 13 14  / ** ** **  / 66 67 68 69  / ** ** ** **  / ** ** ** **
  21 22 23 24 /  43 44 45 /  76 77 78 79 /  ** ** ** ** /  ** ** ** **
  31 32 33 34/   53 54 55/   86 87 88 89/   97 98 99 90/   08 09 00 01
  18 19 10 11

  INDEX = 1      INDEX = 13  INDEX = 22     INDEX = 34     INDEX = 46

  Actual right hand side values with ** for arbitrary values:

  B1 B2 B3 ** B4 B5 B6 B7 B8 ** ** B9 ** ** B10 B11

  It would have been more efficient to combine block 3 with block 4.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input/output, real ( kind = 8 ) BLOKS(*), a one-dimenional array,
  of length sum ( INTEGS(1,1:NBLOKS) * INTEGS(2,1:NBLOKS) ).
  On input, contains the blocks of the almost block diagonal matrix A.
  The array INTEGS describes the block structure.
  On output, contains correspondingly the PLU factorization
  of A, if IFLAG /= 0.  Certain entries in BLOKS are arbitrary,
  where the blocks overlap.

  Input, integer ( kind = 4 ) INTEGS(3,NBLOKS), description of the block
  structure of A.
  integs(1,I) = number of rows of block I = nrow;
  integs(2,I) = number of colums of block I = ncol;
  integs(3,I) = number of elimination steps in block I = last.
  The linear system is of order n = sum ( integs(3,i), i=1,...,nbloks ),
  but the total number of rows in the blocks is
  nbrows=sum( integs(1,i) ; i = 1,...,nbloks)

  Input, integer ( kind = 4 ) NBLOKS, the number of blocks.

  Input, real ( kind = 8 ) B(NBROWS), the right hand side.  Certain entries
  are arbitrary, corresponding to rows of the blocks which overlap.  See
  the block structure in the example.

  Output, integer ( kind = 4 ) IPIVOT(NBROWS), the pivoting sequence used.

  Output, real ( kind = 8 ) X(N), the computed solution, if iflag /= 0.

  Output, integer ( kind = 4 ) IFLAG.
  = (-1)**(number of interchanges during factorization) if A is invertible;
  = 0 if A is singular.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `smooth`
- **Signature:** `Function smooth(x, y, dy, npoint, s, v, a)`
- **Purpose:** *****************************************************************************80

  ! SMOOTH constructs the cubic smoothing spline to given data.

  Discussion:

  The data is of the form

  ( X(1:NPOINT), Y(1:NPOINT) )

  The cubic smoothing spline has as small a second derivative as
  possible, while

  S(F) <= S,

  where

  S(F) = sum ( 1 <= I <= NPOINT ) ( ( ( Y(I) - F(X(I)) ) / DY(I) )**2.

  Method:

  The matrices Q' * D and Q' * D**2 * Q are constructed in SETUPQ from
  X and DY, as is the vector QTY = Q' * Y.

  Then, for given P, the vector U is determined in CHOL1D as
  the solution of the linear system

  ( 6 * (1-P) * Q' * D**2 * Q + P * R ) * U = QTY.

  From U and this choice of smoothing parameter P, the smoothing spline F
  is obtained in the sense that:

  F(X(.)) = Y - 6 (1-P) D**2 * Q * U,
  (d**2) F(X(.)) = 6 * P * U.

  The smoothing parameter P is found, if possible, so that

  SF(P) = S,

  with SF(P) = S(F), where F is the smoothing spline as it depends
  on P.  If S = 0, then P = 1.  If SF(0) <= S, then P = 0.
  Otherwise, the secant method is used to locate an appropriate P in
  the open interval (0,1).

  Specifically,

  P(0) = 0,  P(1) = ( S - SF(0) ) / DSF

  with

  DSF = -24 * U' * R * U

  a good approximation to

  D(SF(0)) = DSF + 60 * (D*Q*U)' * (D*Q*U),

  and U as obtained for P = 0.

  After that, for N = 1, 2,...  until SF(P(N)) <= 1.01 * S, do:
  determine P(N+1) as the point at which the secant to SF at the
  points P(N) and P(N-1) takes on the value S.

  If 1 <= P(N+1), choose instead P(N+1) as the point at which
  the parabola SF(P(N))*((1-.)/(1-P(N)))**2 takes on the value S.

  Note that, in exact arithmetic, it is always the case that
  P(N+1) < P(N),
  hence
  SF(P(N+1)) < SF(P(N)).

  Therefore, also stop the iteration, with final P = 1, in case
  SF(P(N)) <= SF(P(N+1)).

  Modified:

  16 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) X(NPOINT), the abscissas, assumed to be
  strictly increasing.

  Input, real ( kind = 8 ) Y(NPOINT), the corresponding ordinates.

  Input, real ( kind = 8 ) DY(NPOINT), the data uncertainty estimates,
  which are assumed to be positive.

  Input, integer ( kind = 4 ) NPOINT, the number of data points.

  Input, real ( kind = 8 ) S, an upper bound on the discrete weighted mean
  square distance of the approximation F from the data.

  Workspace, real ( kind = 8 ) V(NPOINT,7).

  Workspace, real ( kind = 8 ) A(NPOINT,4).

  Output, real ( kind = 8 ) A(NPOINT,4).
  A(*,1).....contains the sequence of smoothed ordinates.
  A(I,J) = d**(J-1) F(X(I)), for J = 2:4, I = 1:NPOINT-1.
  That is, the first three derivatives of the smoothing spline F at the
  left end of each of the data intervals.  Note that A would have to
  be transposed before it could be used in PPVALU.

  Output, real ( kind = 8 ) SMOOTH, the value of the smoothing parameter.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `spli2d`
- **Signature:** `Subroutine spli2d(tau, gtau, t, n, k, m, work, q, bcoef, iflag)`
- **Purpose:** *****************************************************************************80

  ! SPLI2D produces a interpolatory tensor product spline.

  Discussion:

  SPLI2D is an extended version of SPLINT.

  SPLI2D produces the B-spline coefficients BCOEF(J,.) of the
  spline of order K with knots T(1:N+K), which takes on
  the value GTAU(I,J) at TAU(I), I=1,..., N, J=1,...,M.

  The I-th equation of the linear system

  A * BCOEF = B

  for the B-spline coefficients of the interpolant enforces
  interpolation at TAU(I), I=1,...,N.  Hence,  B(I) = GTAU(I),
  for all I, and A is a band matrix with 2*K-1 bands, if it is
  invertible.

  The matrix A is generated row by row and stored, diagonal by
  diagonal, in the rows of the array Q, with the main diagonal
  going into row K.

  The banded system is then solved by a call to BANFAC, which
  constructs the triangular factorization for A and stores it
  again in Q, followed by a call to BANSLV, which then obtains
  the solution BCOEF by substitution.

  The linear system to be solved is theoretically invertible if
  and only if

  T(I) < TAU(I) < TAU(I+K), for all I.

  Violation of this condition is certain to lead to IFLAG = 2.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) TAU(N), contains the data point abscissas.
  TAU must be strictly increasing

  Input, real ( kind = 8 ) GTAU(N,M), contains the data point ordinates.

  Input, real ( kind = 8 ) T(N+K), the knot sequence.

  Input, integer ( kind = 4 ) N, the number of data points and the
  dimension of the spline space SPLINE(K,T)

  Input, integer ( kind = 4 ) K, the order of the spline.

  Input, integer ( kind = 4 ) M, the number of data sets.

  Work space, real ( kind = 8 ) WORK(N).

  Output, real ( kind = 8 ) Q(2*K-1)*N, the triangular
  factorization of the coefficient matrix of the linear
  system for the B-spline coefficients of the spline interpolant.
  The B-spline coefficients for the interpolant of an additional
  data set ( TAU(I), HTAU(I) ), I=1,...,N  with the same data
  abscissae can be obtained without going through all the
  calculations in this routine, simply by loading HTAU into
  BCOEF and then using the statement
  CALL BANSLV ( Q, 2*K-1, N, K-1, K-1, BCOEF )

  Output, real ( kind = 8 ) BCOEF(N), the B-spline coefficients of
  the interpolant.

  Output, integer ( kind = 4 ) IFLAG, error indicator.
  1, no error.
  2, an error occurred, which may have been caused by
  singularity of the linear system.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `splint`
- **Signature:** `Subroutine splint(tau, gtau, t, n, k, q, bcoef, iflag)`
- **Purpose:** *****************************************************************************80

  ! SPLINT produces the B-spline coefficients BCOEF of an interpolating spline.

  Discussion:

  The spline is of order K with knots T(1:N+K), and takes on the
  value GTAU(I) at TAU(I), for I = 1 to N.

  The I-th equation of the linear system

  A * BCOEF = B

  for the B-spline coefficients of the interpolant enforces interpolation
  at TAU(1:N).

  Hence, B(I) = GTAU(I), for all I, and A is a band matrix with 2*K-1
  bands, if it is invertible.

  The matrix A is generated row by row and stored, diagonal by diagonal,
  in the rows of the array Q, with the main diagonal going
  into row K.  See comments in the program.

  The banded system is then solved by a call to BANFAC, which
  constructs the triangular factorization for A and stores it again in
  Q, followed by a call to BANSLV, which then obtains the solution
  BCOEF by substitution.

  BANFAC does no pivoting, since the total positivity of the matrix
  A makes this unnecessary.

  The linear system to be solved is (theoretically) invertible if
  and only if
  T(I) < TAU(I) < TAU(I+K), for all I.
  Violation of this condition is certain to lead to IFLAG = 2.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) TAU(N), the data point abscissas.  The entries in
  TAU should be strictly increasing.

  Input, real ( kind = 8 ) GTAU(N), the data ordinates.

  Input, real ( kind = 8 ) T(N+K), the knot sequence.

  Input, integer ( kind = 4 ) N, the number of data points.

  Input, integer ( kind = 4 ) K, the order of the spline.

  Output, real ( kind = 8 ) Q((2*K-1)*N), the triangular factorization
  of the coefficient matrix of the linear system for the B-coefficients
  of the spline interpolant.  The B-coefficients for the interpolant
  of an additional data set can be obtained without going through all
  the calculations in this routine, simply by loading HTAU into BCOEF
  and then executing the call:
  call banslv ( q, 2*k-1, n, k-1, k-1, bcoef )

  Output, real ( kind = 8 ) BCOEF(N), the B-spline coefficients of
  the interpolant.

  Output, integer ( kind = 4 ) IFLAG, error flag.
  1, = success.
  2, = failure.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `splopt`
- **Signature:** `Subroutine splopt(tau, n, k, scrtch, t, iflag)`
- **Purpose:** *****************************************************************************80

  ! SPLOPT computes the knots for an optimal recovery scheme.

  Discussion:

  The optimal recovery scheme is of order K for data at TAU(1:N).

  The interior knots T(K+1:N) are determined by Newton's method in
  such a way that the signum function which changes sign at
  T(K+1:N)  and nowhere else in ( TAU(1), TAU(N) ) is
  orthogonal to the spline space SPLINE ( K, TAU ) on that interval.

  Let XI(J) be the current guess for T(K+J), J=1,...,N-K.  Then
  the next Newton iterate is of the form

  XI(J) + (-)**(N-K-J)*X(J),  J=1,...,N-K,

  with X the solution of the linear system

  C * X = D.

  Here, for all J,

  C(I,J) = B(I)(XI(J)),

  with B(I) the I-th B-spline of order K for the knot sequence TAU,
  for all I, and D is the vector given, for each I, by

  D(I) = sum ( -A(J), J=I,...,N ) * ( TAU(I+K) - TAU(I) ) / K,

  with, for I = 1 to N-1:

  A(I) = sum ( (-)**(N-K-J)*B(I,K+1,TAU)(XI(J)), J=1,...,N-K )

  and

  A(N) = -0.5.

  See Chapter XIII of text and references there for a derivation.

  The first guess for T(K+J) is sum ( TAU(J+1:J+K-1) ) / ( K - 1 ).

  The iteration terminates if max ( abs ( X(J) ) ) < TOL, with

  TOL = TOLRTE * ( TAU(N) - TAU(1) ) / ( N - K ),

  or else after NEWTMX iterations.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) TAU(N), the interpolation points.
  assumed to be nondecreasing, with TAU(I) < TAU(I+K), for all I.

  Input, integer ( kind = 4 ) N, the number of data points.

  Input, integer ( kind = 4 ) K, the order of the optimal recovery scheme
  to be used.

  Workspace, real ( kind = 8 ) SCRTCH((N-K)*(2*K+3)+5*K+3).  The various
  contents are specified in the text below.

  Output, real ( kind = 8 ) T(N+K), the optimal knots ready for
  use in optimal recovery.  Specifically, T(1:K) = TAU(1),
  T(N+1:N+K) = TAU(N), while the N - K interior knots T(K+1:N)
  are calculated.

  Output, integer ( kind = 4 ) IFLAG, error indicator.
  = 1, success.  T contains the optimal knots.
  = 2, failure.  K < 3 or N < K or the linear system was singular.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `subbak`
- **Signature:** `Subroutine subbak(w, ipivot, nrow, ncol, last, x)`
- **Purpose:** *****************************************************************************80

  ! SUBBAK carries out back substitution for the current block.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) W(NROW,NCOL), integer IPIVOT(NROW), integer
  NROW, integer NCOL, integer LAST, are as on return from FACTRB.

  Input/output, real ( kind = 8 ) X(NCOL).
  On input, the right hand side for the equations in this block after
  back substitution has been carried out up to, but not including,
  equation IPIVOT(LAST).  This means that X(1:LAST) contains the right hand
  sides of equation IPIVOT(1:LAST) as modified during elimination,
  while X(LAST+1:NCOL) is already a component of the solution vector.
  On output, the components of the solution corresponding to the present
  block.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `subfor`
- **Signature:** `Subroutine subfor(w, ipivot, nrow, last, b, x)`
- **Purpose:** *****************************************************************************80

  ! SUBFOR carries out the forward pass of substitution for the current block.

  Discussion:

  The forward pass is the action on the right hand side corresponding to the
  elimination carried out in FACTRB for this block.

  At the end, X(1:NROW) contains the right hand side of the transformed
  IPIVOT(1:NROW)-th equation in this block.

  Then, since for I=1,...,NROW-LAST, B(NROW+I) is going to be used as
  the right hand side of equation I in the next block (shifted over there
  from this block during factorization), it is set equal to X(LAST+I) here.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) W(NROW,LAST), integer IPIVOT(NROW),
  integer ( kind = 4 ) NROW, integer LAST, are as on return from FACTRB.

  Output, real ( kind = 8 ) B(2*NROW-LAST).  On input, B(1:NROW)
  contains the right hand sides for this block.  On output,
  B(NROW+1:2*NROW-LAST) contains the appropriately modified right
  hand sides for the next block.

  Output, real X(NROW), contains, on output, the appropriately modified
  right hand sides of equations IPIVOT(1:NROW).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `tautsp`
- **Signature:** `Subroutine tautsp(tau, gtau, ntau, gamma, s, break, coef, l, k, iflag)`
- **Purpose:** *****************************************************************************80

  ! TAUTSP constructs a cubic spline interpolant to given data.

  Discussion:

  If 0 < GAMMA, additional knots are introduced where needed to
  make the interpolant more flexible locally.  This avoids extraneous
  inflection points typical of cubic spline interpolation at knots to
  rapidly changing data.

  Method:

  On the I-th interval, (TAU(I), TAU(I+1)), the interpolant is of the
  form:

  (*)  F(U(X)) = A + B * U + C * H(U,Z) + D * H(1-U,1-Z),

  with

  U = U(X) = ( X - TAU(I) ) / DTAU(I).

  Here,

  Z(I) = ADDG(I+1) / ( ADDG(I) + ADDG(I+1) )

  but if the denominator vanishes, we set Z(I) = 0.5

  Also, we have

  ADDG(J) = abs ( DDG(J) ),
  DDG(J) = DG(J+1) - DG(J),
  DG(J) = DIVDIF(J) = ( GTAU(J+1) - GTAU(J) ) / DTAU(J)

  and

  H(U,Z) = ALPHA * U**3
  + ( 1 - ALPHA ) * ( max ( ( ( U - ZETA ) / ( 1 - ZETA ) ), 0 )**3

  with

  ALPHA(Z) = ( 1 - GAMMA / 3 ) / ZETA
  ZETA(Z) = 1 - GAMMA * min ( ( 1 - Z ), 1/3 )

  Thus, for 1/3 <= Z <= 2/3, F is just a cubic polynomial on
  the interval I.  Otherwise, it has one additional knot, at

  TAU(I) + ZETA * DTAU(I).

  As Z approaches 1, H(.,Z) has an increasingly sharp bend near 1,
  thus allowing F to turn rapidly near the additional knot.

  In terms of F(J) = GTAU(J) and FSECND(J) = second derivative of F
  at TAU(J), the coefficients for (*) are given as:

  A = F(I) - D
  B = ( F(I+1) - F(I) ) - ( C - D )
  C = FSECND(I+1) * DTAU(I)**2 / HSECND(1,Z)
  D = FSECND(I) * DTAU(I)**2 / HSECND(1,1-Z)

  Hence these can be computed once FSECND(1:NTAU) is fixed.

  F is automatically continuous and has a continuous second derivative
  except when Z=0 or 1 for some I.  We determine FSECND from
  the requirement that the first derivative of F be continuous.

  In addition, we require that the third derivative be continuous
  across TAU(2) and across TAU(NTAU-1).  This leads to a strictly
  diagonally dominant tridiagonal linear system for the FSECND(I)
  which we solve by Gauss elimination without pivoting.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Input, real ( kind = 8 ) TAU(NTAU), the sequence of data points.
  TAU must be strictly increasing.

  Input, real ( kind = 8 ) GTAU(NTAU), the corresponding sequence of
  function values.

  Input, integer ( kind = 4 ) NTAU, the number of data points.
  NTAU must be at least 4.

  Input, real ( kind = 8 ) GAMMA, indicates whether additional flexibility
  is desired.
  GAMMA = 0.0, no additional knots;
  GAMMA in (0.0,3.0), under certain conditions on the given data at
  points I-1, I, I+1, and I+2, a knot is added in the I-th interval,
  for I = 2,...,NTAU-2.  See description of method.  The interpolant
  gets rounded with increasing gamma.  A value of 2.5 for GAMMA is typical.
  GAMMA in (3.0,6.0), same, except that knots might also be added in
  intervals in which an inflection point would be permitted.  A value
  of 5.5 for GAMMA is typical.

  Output, real ( kind = 8 ) BREAK(L), real ( kind = 8 ) COEF(K,L),
  integer ( kind = 4 ) L, integer K, give the piecewise polynomial
  representation of the interpolant.  Specifically,
  for BREAK(i) <= X <= BREAK(I+1), the interpolant has the form:
  F(X) = COEF(1,I) +  DX    * (
  COEF(2,I) + (DX/2) * (
  COEF(3,I) + (DX/3) *
  COEF(4,I) ) )
  with  DX = X - BREAK(I) for I = 1,..., L.

  Output, integer ( kind = 4 ) IFLAG, error flag.
  1, no error.
  2, input was incorrect.

  Output, real ( kind = 8 ) S(NTAU,6).  The individual columns of this
  array contain the following quantities mentioned in the write up
  and below.
  S(.,1) = DTAU = TAU(.+1)-TAU;
  S(.,2) = DIAG = diagonal in linear system;
  S(.,3) = U = upper diagonal in linear system;
  S(.,4) = R = right hand side for linear system (initially)
  = FSECND = solution of linear system, namely the second
  derivatives of interpolant at TAU;
  S(.,5) = Z = indicator of additional knots;
  S(.,6) = 1/HSECND(1,X) with X = Z or 1-Z.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `titand`
- **Signature:** `Subroutine titand(t, g, n)`
- **Purpose:** *****************************************************************************80

  ! TITAND represents a temperature dependent property of titanium.

  Discussion:

  The data has been used extensively as an example in spline
  approximation with variable knots.

  Modified:

  14 February 2007

  Author:

  Carl DeBoor

  Reference:

  Carl DeBoor,
  A Practical Guide to Splines,
  Springer, 2001,
  ISBN: 0387953663,
  LC: QA1.A647.v27.

  Parameters:

  Output, real ( kind = 8 ) T(N), the location of the data points.

  Output, real ( kind = 8 ) G(N), the value associated with the data points.

  Output, integer ( kind = 4 ) N, the number of data points, which is 49.
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
