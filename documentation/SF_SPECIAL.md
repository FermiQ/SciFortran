## Overview

SciFortran module for specific functions and distributions

## Key Components

### Module: `SF_SPECIAL`
- **Purpose:** SciFortran module for specific functions and distributions
- **Contains:** `heaviside`, `step_x`, `step_ij`, `fermi`, `dfermi`, `i_sgn`, `d_sgn`, `wfun`, `dens_hyperc`, `dens_2dsquare`, `dens_3dcubic`, `func`, `EllipticK`, `ellf`, `rf`

### Function: `heaviside`
- **Signature:** `Function heaviside(x)`
- **Purpose:** +------------------------------------------------------------------+
  PURPOSE  : calculate the Heaviside  function
  +------------------------------------------------------------------+
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `step_x`
- **Signature:** `Function step_x(x,origin)`
- **Purpose:** +------------------------------------------------------------------+
  PURPOSE  : calculate step function
  +------------------------------------------------------------------+
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `step_ij`
- **Signature:** `Function step_ij(i,j,origin)`
- **Purpose:** +------------------------------------------------------------------+
  PURPOSE  : calculate step function
  +------------------------------------------------------------------+
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `fermi`
- **Signature:** `Function fermi(x,beta,limit)`
- **Purpose:** *******************************************************************
  *******************************************************************
  *******************************************************************
  +-------------------------------------------------------------------+
  PURPOSE  : calculate the Fermi-Dirac distribution
  +-------------------------------------------------------------------+
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `dfermi`
- **Signature:** `Function dfermi(x,beta,limit)`
- **Purpose:** *******************************************************************
  *******************************************************************
  *******************************************************************
  +-------------------------------------------------------------------+
  PURPOSE  : calculate the derivative of Fermi-Dirac distribution
  +-------------------------------------------------------------------+
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `i_sgn`
- **Signature:** `Function i_sgn(x)`
- **Purpose:** *******************************************************************
  *******************************************************************
  *******************************************************************
  +-------------------------------------------------------------------+
  PURPOSE:  evaluate the sign of a given number (I,R)
  +-------------------------------------------------------------------+
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `d_sgn`
- **Signature:** `Function d_sgn(x)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `wfun`
- **Signature:** `Function wfun(z)`
- **Purpose:** *******************************************************************
  *******************************************************************
  *******************************************************************
  +------------------------------------------------------------------+
  PURPOSE  : Evaluate the Complex Error Functions (Faddeeva function)
  w(x)=exp(-x^2)erfc(-ix)
  ANYWAY USE ZERF
  +------------------------------------------------------------------+
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `dens_hyperc`
- **Signature:** `Function dens_hyperc(x,t1)`
- **Purpose:** +-------------------------------------------------------------------+
  PURPOSE  : calculate the non-interacting dos for HYPERCUBIC lattice
  +-------------------------------------------------------------------+
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `dens_2dsquare`
- **Signature:** `Function dens_2dsquare(x,ts)`
- **Purpose:** +-------------------------------------------------------------------+
  PURPOSE  : calculate the non-interacting dos for 2D lattice

  +-------------------------------------------------------------------+
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `dens_3dcubic`
- **Signature:** `Function dens_3dcubic(x,ts)`
- **Purpose:** +-------------------------------------------------------------------+
  PURPOSE  : calculate the non-interacting dos for SIMPLE CUBIC lattice
  follows closely the works:
  + Economou Greens functions in quantum physics
  + Horiguchi, Journal of the Physical Society of Japan, Vol.30,N.5 (1971)
  +-------------------------------------------------------------------+
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `func`
- **Signature:** `Function func(p)`
- **Purpose:** > F(p) = K(k1')
  > k1'  = sqrt(1-k1**2)
  > k1   = (s-cos(p))/2 = 1/k
  > k    = 2/(s-cos(p))
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `EllipticK`
- **Signature:** `Function EllipticK(z)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `ellf`
- **Signature:** `Function ellf(phi,ak)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `rf`
- **Signature:** `Function rf(x,y,z)`
- **Purpose:** No specific description available.
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
