## Overview

Overview not automatically extracted.

## Key Components

### Module: `interpolate_pack`
- **Purpose:** Overview not automatically extracted.
- **Contains:** `cc_abscissas`, `cc_abscissas_ab`, `f1_abscissas`, `f1_abscissas_ab`, `f2_abscissas`, `f2_abscissas_ab`, `lagrange_value`, `ncc_abscissas`, `ncc_abscissas_ab`, `nco_abscissas`, `nco_abscissas_ab`, `parameterize_arc_length`, `parameterize_index`, `r8mat_expand_linear2`, `r8vec_ascends_strictly`, `r8vec_bracket`, `r8vec_expand_linear`, `r8vec_expand_linear2`

### Subroutine: `cc_abscissas`
- **Signature:** `Subroutine cc_abscissas(n, x)`
- **Purpose:** *****************************************************************************80

  ! CC_ABSCISSAS computes the Clenshaw Curtis abscissas.

  Discussion:

  The interval is [ -1, 1 ].

  The abscissas are the cosines of equally spaced angles between
  180 and 0 degrees, including the endpoints.

  X(I) = cos ( ( ORDER - I ) * PI / ( ORDER - 1 ) )

  except for the basic case ORDER = 1, when

  X(1) = 0.

  If the value of ORDER is increased in a sensible way, then
  the new set of abscissas will include the old ones.  One such
  sequence would be ORDER(K) = 2*K+1 for K = 0, 1, 2, ...

  When doing interpolation with Lagrange polynomials, the Clenshaw Curtis
  abscissas can be a better choice than regularly spaced abscissas.

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  04 December 2007

  Author:

  John Burkardt

  Reference:

  Charles Clenshaw, Alan Curtis,
  A Method for Numerical Integration on an Automatic Computer,
  Numerische Mathematik,
  Volume 2, Number 1, December 1960, pages 197-205.

  Philip Davis, Philip Rabinowitz,
  Methods of Numerical Integration,
  Second Edition,
  Dover, 2007,
  ISBN: 0486453391,
  LC: QA299.3.D28.

  Joerg Waldvogel,
  Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
  BIT Numerical Mathematics,
  Volume 43, Number 1, 2003, pages 1-18.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of the rule.

  Output, real ( kind = 8 ) X(N), the abscissas.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `cc_abscissas_ab`
- **Signature:** `Subroutine cc_abscissas_ab(a, b, n, x)`
- **Purpose:** *****************************************************************************80

  ! CC_ABSCISSAS_AB computes the Clenshaw Curtis abscissas for the interval [A,B].

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  29 December 2007

  Author:

  John Burkardt

  Parameters:

  Input, real ( kind = 8 ) A, B, the endpoints of the interval.

  Input, integer ( kind = 4 ) N, the order of the rule.

  Output, real ( kind = 8 ) X(N), the abscissas.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `f1_abscissas`
- **Signature:** `Subroutine f1_abscissas(n, x)`
- **Purpose:** *****************************************************************************80

  ! F1_ABSCISSAS computes Fejer type 1 abscissas.

  Discussion:

  The interval is [ -1, +1 ].

  The abscissas are the cosines of equally spaced angles, which
  are the midpoints of N equal intervals between 0 and PI.

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  29 December 2007

  Author:

  John Burkardt

  Reference:

  Philip Davis, Philip Rabinowitz,
  Methods of Numerical Integration,
  Second Edition,
  Dover, 2007,
  ISBN: 0486453391,
  LC: QA299.3.D28.

  Walter Gautschi,
  Numerical Quadrature in the Presence of a Singularity,
  SIAM Journal on Numerical Analysis,
  Volume 4, Number 3, 1967, pages 357-362.

  Joerg Waldvogel,
  Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
  BIT Numerical Mathematics,
  Volume 43, Number 1, 2003, pages 1-18.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of the rule.

  Output, real ( kind = 8 ) X(N), the abscissas.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `f1_abscissas_ab`
- **Signature:** `Subroutine f1_abscissas_ab(a, b, n, x)`
- **Purpose:** *****************************************************************************80

  ! F1_ABSCISSAS_AB computes Fejer type 1 abscissas for the interval [A,B].

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  29 December 2007

  Author:

  John Burkardt

  Reference:

  Philip Davis, Philip Rabinowitz,
  Methods of Numerical Integration,
  Second Edition,
  Dover, 2007,
  ISBN: 0486453391,
  LC: QA299.3.D28.

  Walter Gautschi,
  Numerical Quadrature in the Presence of a Singularity,
  SIAM Journal on Numerical Analysis,
  Volume 4, Number 3, 1967, pages 357-362.

  Joerg Waldvogel,
  Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
  BIT Numerical Mathematics,
  Volume 43, Number 1, 2003, pages 1-18.

  Parameters:

  Input, real ( kind = 8 ) A, B, the endpoints of the interval.

  Input, integer ( kind = 4 ) N, the order of the rule.

  Output, real ( kind = 8 ) X(N), the abscissas.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `f2_abscissas`
- **Signature:** `Subroutine f2_abscissas(n, x)`
- **Purpose:** *****************************************************************************80

  ! F2_ABSCISSAS computes Fejer Type 2 abscissas.

  Discussion:

  The interval is [-1,+1].

  The abscissas are the cosines of equally spaced angles.
  The angles are computed as N+2 equally spaced values between 0 and PI,
  but with the first and last angle omitted.

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  29 December 2007

  Author:

  John Burkardt

  Reference:

  Philip Davis, Philip Rabinowitz,
  Methods of Numerical Integration,
  Second Edition,
  Dover, 2007,
  ISBN: 0486453391,
  LC: QA299.3.D28.

  Walter Gautschi,
  Numerical Quadrature in the Presence of a Singularity,
  SIAM Journal on Numerical Analysis,
  Volume 4, Number 3, 1967, pages 357-362.

  Joerg Waldvogel,
  Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
  BIT Numerical Mathematics,
  Volume 43, Number 1, 2003, pages 1-18.

  Parameters:

  Input, integer ( kind = 4 ) N, the order of the rule.

  Output, real ( kind = 8 ) X(N), the abscissas.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `f2_abscissas_ab`
- **Signature:** `Subroutine f2_abscissas_ab(a, b, n, x)`
- **Purpose:** *****************************************************************************80

  ! F2_ABSCISSAS_AB computes Fejer Type 2 abscissas for the interval [A,B].

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  29 December 2007

  Author:

  John Burkardt

  Parameters:

  Input, real ( kind = 8 ) A, B, the endpoints of the interval.

  Input, integer ( kind = 4 ) N, the order of the rule.

  Output, real ( kind = 8 ) X(N), the abscissas.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `lagrange_value`
- **Signature:** `Subroutine lagrange_value(data_num, t_data, interp_num, t_interp, l_interp)`
- **Purpose:** *****************************************************************************80

  ! LAGRANGE_VALUE evaluates the Lagrange polynomials.

  Discussion:

  Given DATA_NUM distinct abscissas, T_DATA(1:DATA_NUM),
  the I-th Lagrange polynomial L(I)(T) is defined as the polynomial of
  degree DATA_NUM - 1 which is 1 at T_DATA(I) and 0 at the DATA_NUM - 1
  other abscissas.

  A formal representation is:

  L(I)(T) = Product ( 1 <= J <= DATA_NUM, I /= J )
  ( T - T(J) ) / ( T(I) - T(J) )

  This routine accepts a set of INTERP_NUM values at which the Lagrange
  polynomials should be evaluated.

  Given data values P_DATA at each of the abscissas, the value of the
  Lagrange interpolating polynomial at each of the interpolation points
  is then simple to compute by matrix multiplication:

  P_INTERP(1:INTERP_NUM) =
  P_DATA(1:DATA_NUM) * L_INTERP(1:DATA_NUM,1:INTERP_NUM)

  or, in the case where P is multidimensional:

  P_INTERP(1:DIM_NUM,1:INTERP_NUM) =
  P_DATA(1:DIM_NUM,1:DATA_NUM) * L_INTERP(1:DATA_NUM,1:INTERP_NUM)

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  03 December 2007

  Author:

  John Burkardt

  Parameters:

  Input, integer ( kind = 4 ) DATA_NUM, the number of data points.
  DATA_NUM must be at least 1.

  Input, real ( kind = 8 ) T_DATA(DATA_NUM), the data points.

  Input, integer ( kind = 4 ) INTERP_NUM, the number of
  interpolation points.

  Input, real ( kind = 8 ) T_INTERP(INTERP_NUM), the
  interpolation points.

  Output, real ( kind = 8 ) L_INTERP(DATA_NUM,INTERP_NUM), the values
  of the Lagrange polynomials at the interpolation points.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ncc_abscissas`
- **Signature:** `Subroutine ncc_abscissas(n, x)`
- **Purpose:** *****************************************************************************80

  ! NCC_ABSCISSAS computes the Newton Cotes Closed abscissas.

  Discussion:

  The interval is [ -1, 1 ].

  The abscissas are the equally spaced points between -1 and 1,
  including the endpoints.

  If N is 1, however, the single abscissas is X = 0.

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  29 December 2007

  Author:

  John Burkardt

  Parameters:

  Input, integer ( kind = 4 ) N, the order of the rule.

  Output, real ( kind = 8 ) X(N), the abscissas.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `ncc_abscissas_ab`
- **Signature:** `Subroutine ncc_abscissas_ab(a, b, n, x)`
- **Purpose:** *****************************************************************************80

  ! NCC_ABSCISSAS_AB computes the Newton Cotes Closed abscissas for [A,B].

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  29 December 2007

  Author:

  John Burkardt

  Parameters:

  Input, real ( kind = 8 ) A, B, the endpoints of the interval.

  Input, integer ( kind = 4 ) N, the order of the rule.

  Output, real ( kind = 8 ) X(N), the abscissas.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `nco_abscissas`
- **Signature:** `Subroutine nco_abscissas(n, x)`
- **Purpose:** *****************************************************************************80

  ! NCO_ABSCISSAS computes the Newton Cotes Open abscissas.

  Discussion:

  The interval is [ -1, 1 ].

  The abscissas are the equally spaced points between -1 and 1,
  not including the endpoints.

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  29 December 2007

  Author:

  John Burkardt

  Parameters:

  Input, integer ( kind = 4 ) N, the order of the rule.

  Output, real ( kind = 8 ) X(N), the abscissas.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `nco_abscissas_ab`
- **Signature:** `Subroutine nco_abscissas_ab(a, b, n, x)`
- **Purpose:** *****************************************************************************80

  ! NCO_ABSCISSAS_AB computes the Newton Cotes Open abscissas for [A,B].

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  29 December 2007

  Author:

  John Burkardt

  Parameters:

  Input, real ( kind = 8 ) A, B, the endpoints of the interval.

  Input, integer ( kind = 4 ) N, the order of the rule.

  Output, real ( kind = 8 ) X(N), the abscissas.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `parameterize_arc_length`
- **Signature:** `Subroutine parameterize_arc_length(dim_num, data_num, p_data, t_data)`
- **Purpose:** *****************************************************************************80

  ! PARAMETERIZE_ARC_LENGTH parameterizes data by pseudo-arclength.

  Discussion:

  A parameterization is required for the interpolation.

  This routine provides a parameterization by computing the
  pseudo-arclength of the data, that is, the Euclidean distance
  between successive points.

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  19 May 2007

  Author:

  John Burkardt

  Parameters:

  Input, integer ( kind = 4 ) DIM_NUM, the spatial dimension.

  Input, integer ( kind = 4 ) DATA_NUM, the number of data points.

  Input, real ( kind = 8 ) P_DATA(DIM_NUM,DATA_NUM), the data values.

  Output, real ( kind = 8 ) T_DATA(DATA_NUM), parameter values
  assigned to the data.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `parameterize_index`
- **Signature:** `Subroutine parameterize_index(dim_num, data_num, p_data, t_data)`
- **Purpose:** *****************************************************************************80

  ! PARAMETERIZE_INDEX parameterizes data by its index.

  Discussion:

  A parameterization is required for the interpolation.

  This routine provides a naive parameterization by vector index.

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  19 May 2007

  Author:

  John Burkardt

  Parameters:

  Input, integer ( kind = 4 ) DIM_NUM, the spatial dimension.

  Input, integer ( kind = 4 ) DATA_NUM, the number of data points.

  Input, real ( kind = 8 ) P_DATA(DIM_NUM,DATA_NUM), the data values.

  Output, real ( kind = 8 ) T_DATA(DATA_NUM), parameter values
  assigned to the data.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `r8mat_expand_linear2`
- **Signature:** `Subroutine r8mat_expand_linear2(m, n, a, m2, n2, a2)`
- **Purpose:** *****************************************************************************80

  ! R8MAT_EXPAND_LINEAR2 expands an R8MAT by linear interpolation.

  Discussion:

  An R8MAT is an array of R8 values.

  In this version of the routine, the expansion is indicated
  by specifying the dimensions of the expanded array.

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  07 December 2004

  Author:

  John Burkardt

  Parameters:

  Input, integer ( kind = 4 ) M, N, the number of rows and columns in A.

  Input, real ( kind = 8 ) A(M,N), a "small" M by N array.

  Input, integer ( kind = 4 ) M2, N2, the number of rows and columns in A2.

  Output, real ( kind = 8 ) A2(M2,N2), the expanded array, which
  contains an interpolated version of the data in A.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `r8vec_ascends_strictly`
- **Signature:** `Function r8vec_ascends_strictly(n, x)`
- **Purpose:** *****************************************************************************80

  ! R8VEC_ASCENDS_STRICTLY determines if an R8VEC is strictly ascending.

  Discussion:

  An R8VEC is a vector of R8 values.

  Notice the effect of entry number 6 in the following results:

  X = ( -8.1, 1.3, 2.2, 3.4, 7.5, 7.4, 9.8 )
  Y = ( -8.1, 1.3, 2.2, 3.4, 7.5, 7.5, 9.8 )
  Z = ( -8.1, 1.3, 2.2, 3.4, 7.5, 7.6, 9.8 )

  R8VEC_ASCENDS_STRICTLY ( X ) = FALSE
  R8VEC_ASCENDS_STRICTLY ( Y ) = FALSE
  R8VEC_ASCENDS_STRICTLY ( Z ) = TRUE

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  03 December 2007

  Author:

  John Burkardt

  Parameters:

  Input, integer ( kind = 4 ) N, the size of the array.

  Input, real ( kind = 8 ) X(N), the array to be examined.

  Output, logical R8VEC_ASCENDS_STRICTLY, is TRUE if the
  entries of X strictly ascend.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `r8vec_bracket`
- **Signature:** `Subroutine r8vec_bracket(n, x, xval, left, right)`
- **Purpose:** *****************************************************************************80

  ! R8VEC_BRACKET searches a sorted R8VEC for successive brackets of a value.

  Discussion:

  An R8VEC is an array of double precision real values.

  If the values in the vector are thought of as defining intervals
  on the real line, then this routine searches for the interval
  nearest to or containing the given value.

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  06 April 1999

  Author:

  John Burkardt

  Parameters:

  Input, integer ( kind = 4 ) N, length of input array.

  Input, real ( kind = 8 ) X(N), an array sorted into ascending order.

  Input, real ( kind = 8 ) XVAL, a value to be bracketed.

  Output, integer ( kind = 4 ) LEFT, RIGHT, the results of the search.
  Either:
  XVAL < X(1), when LEFT = 1, RIGHT = 2;
  X(N) < XVAL, when LEFT = N-1, RIGHT = N;
  or
  X(LEFT) <= XVAL <= X(RIGHT).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `r8vec_expand_linear`
- **Signature:** `Subroutine r8vec_expand_linear(n, x, fat, xfat)`
- **Purpose:** *****************************************************************************80

  ! R8VEC_EXPAND_LINEAR linearly interpolates new data into an R8VEC.

  Discussion:

  This routine copies the old data, and inserts NFAT new values
  between each pair of old data values.  This would be one way to
  determine places to evenly sample a curve, given the (unevenly
  spaced) points at which it was interpolated.

  An R8VEC is an array of double precision real values.

  Example:

  N = 3
  NFAT = 2

  X(1:N)        = (/ 0.0,           6.0,             7.0 /)
  XFAT(1:2*3+1) = (/ 0.0, 2.0, 4.0, 6.0, 6.33, 6.66, 7.0 /)

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  10 October 2001

  Author:

  John Burkardt

  Parameters:

  Input, integer ( kind = 4 ) N, the number of input data values.

  Input, real ( kind = 8 ) X(N), the original data.

  Input, integer ( kind = 4 ) FAT, the number of data values to interpolate
  between each pair of original data values.

  Output, real ( kind = 8 ) XFAT((N-1)*(FAT+1)+1), the "fattened" data.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `r8vec_expand_linear2`
- **Signature:** `Subroutine r8vec_expand_linear2(n, x, before, fat, after, xfat)`
- **Purpose:** *****************************************************************************80

  ! R8VEC_EXPAND_LINEAR2 linearly interpolates new data into an R8VEC.

  Discussion:

  This routine starts with a vector of data.

  The intent is to "fatten" the data, that is, to insert more points
  between successive values of the original data.

  There will also be extra points placed BEFORE the first original
  value and AFTER that last original value.

  The "fattened" data is equally spaced between the original points.

  The BEFORE data uses the spacing of the first original interval,
  and the AFTER data uses the spacing of the last original interval.

  Example:

  N = 3
  BEFORE = 3
  FAT = 2
  AFTER = 1

  X(1:N)        = (/                   0.0,           6.0,             7.0       /)
  XFAT(1:2*3+1) = (/ -6.0, -4.0, -2.0, 0.0, 2.0, 4.0, 6.0, 6.33, 6.66, 7.0, 7.66 /)
  3 "BEFORE's"      Old  2 "FATS"  Old    2 "FATS"  Old  1 "AFTER"

  Licensing:

  This code is distributed under the GNU LGPL license.

  Modified:

  03 December 2007

  Author:

  John Burkardt

  Parameters:

  Input, integer ( kind = 4 ) N, the number of input data values.
  N must be at least 2.

  Input, real ( kind = 8 ) X(N), the original data.

  Input, integer ( kind = 4 ) BEFORE, the number of "before" values.

  Input, integer ( kind = 4 ) FAT, the number of data values to interpolate
  between each pair of original data values.

  Input, integer ( kind = 4 ) AFTER, the number of "after" values.

  Output, real ( kind = 8 ) XFAT(BEFORE+(N-1)*(FAT+1)+1+AFTER), the "fattened" data.
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
