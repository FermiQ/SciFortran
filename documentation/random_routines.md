## Overview

Overview not automatically extracted.

## Key Components

### Module: `random_routines`
- **Purpose:** Overview not automatically extracted.
- **Contains:** `random_normal`, `random_gamma`, `random_gamma1`, `random_gamma2`, `random_chisq`, `random_exponential`, `random_Weibull`, `random_beta`, `random_mvnorm`, `random_inv_gauss`, `random_Poisson`, `random_binomial1`, `bin_prob`, `lngamma`, `random_binomial2`, `random_neg_binomial`, `random_von_Mises`, `integral`, `random_Cauchy`

### Function: `random_normal`
- **Signature:** `Function random_normal()`
- **Purpose:** +-----------------------------------------------------------------+
  PROGRAM  :
  TYPE     : Subroutine
  PURPOSE  :
  +-----------------------------------------------------------------+
  Adapted from the following Fortran 77 code
  ALGORITHM 712, COLLECTED ALGORITHMS FROM ACM.
  THIS WORK PUBLISHED IN TRANSACTIONS ON MATHEMATICAL SOFTWARE,
  VOL. 18, NO. 4, DECEMBER, 1992, PP. 434-435.
  The function random_normal() returns a normally distributed pseudo-random
  number with zero mean and unit variance.
  The algorithm uses the ratio of uniforms method of A.J. Kinderman
  and J.F. Monahan augmented with quadratic bounding curves.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `random_gamma`
- **Signature:** `Function random_gamma(s, first)`
- **Purpose:** *******************************************************************
  *******************************************************************
  *******************************************************************
  +-----------------------------------------------------------------+
  PROGRAM  :
  TYPE     : Subroutine
  PURPOSE  :
  +-----------------------------------------------------------------+
  Adapted from Fortran 77 code from the book:
  Dagpunar, J. 'Principles of random variate generation'
  Clarendon Press, Oxford, 1988.   ISBN 0-19-852202-9
  FUNCTION GENERATES A RANDOM GAMMA VARIATE.
  CALLS EITHER random_gamma1 (S > 1.0)
  OR random_exponential (S = 1.0)
  OR random_gamma2 (S < 1.0).
  S = SHAPE PARAMETER OF DISTRIBUTION (0 < REAL).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `random_gamma1`
- **Signature:** `Function random_gamma1(s, first)`
- **Purpose:** Local variables
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `random_gamma2`
- **Signature:** `Function random_gamma2(s, first)`
- **Purpose:** Local variables
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `random_chisq`
- **Signature:** `Function random_chisq(ndf, first)`
- **Purpose:** Generates a random variate from the chi-squared distribution with
  ndf degrees of freedom
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `random_exponential`
- **Signature:** `Function random_exponential()`
- **Purpose:** Local variable
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `random_Weibull`
- **Signature:** `Function random_Weibull(a)`
- **Purpose:** For speed, there is no checking that a is not zero or very small.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `random_beta`
- **Signature:** `Function random_beta(aa, bb, first)`
- **Purpose:** Local variables
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `random_mvnorm`
- **Signature:** `Subroutine random_mvnorm(n, h, d, f, first, x, ier)`
- **Purpose:** Local variables
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `random_inv_gauss`
- **Signature:** `Function random_inv_gauss(h, b, first)`
- **Purpose:** Local variables
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `random_Poisson`
- **Signature:** `Function random_Poisson(mu, first)`
- **Purpose:** ..
  .. Local Scalars ..
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `random_binomial1`
- **Signature:** `Function random_binomial1(n, p, first)`
- **Purpose:** Local variables
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `bin_prob`
- **Signature:** `Function bin_prob(n, p, r)`
- **Purpose:** Calculate a binomial probability
  Local variable
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `lngamma`
- **Signature:** `Function lngamma(x)`
- **Purpose:** Logarithm to base e of the gamma function.

  Accurate to about 1.e-14.
  Programmer: Alan Miller
  Latest revision of Fortran 77 version - 28 February 1988
  Local variables
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `random_binomial2`
- **Signature:** `Function random_binomial2(n, pp, first)`
- **Purpose:** ..
  .. Scalar Arguments ..
  ..
  .. Local Scalars ..
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `random_neg_binomial`
- **Signature:** `Function random_neg_binomial(sk, p)`
- **Purpose:** Local variables
  THE PARAMETER ULN = -LOG(MACHINE'S SMALLEST REAL NUMBER).
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `random_von_Mises`
- **Signature:** `Function random_von_Mises(k, first)`
- **Purpose:** Local variables
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `integral`
- **Signature:** `Subroutine integral(a, b, result, dk)`
- **Purpose:** Gaussian integration of exp(k.cosx) from a to b.
  Local variables
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `random_Cauchy`
- **Signature:** `Function random_Cauchy()`
- **Purpose:** Generate a random deviate from the standard Cauchy distribution
  Local variables
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
