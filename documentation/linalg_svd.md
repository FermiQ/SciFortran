## Overview

Overview not automatically extracted.

## Key Components

### Module: `linalg_svd`
- **Purpose:** Overview not automatically extracted.
- **Contains:** `dsvd`, `zsvd`

### Subroutine: `dsvd`
- **Signature:** `Subroutine dsvd(A, s, U, Vtransp)`
- **Purpose:** real m x n matrix A
  U is m x m
  Vtransp is n x n
  s has size min(m, n) --> sigma matrix is (n x m) with sigma_ii = s_i
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `zsvd`
- **Signature:** `Subroutine zsvd(A, s, U, Vtransp)`
- **Purpose:** complex m x m matrix A
  U is m x min(m, n)
  Vtransp is n x n
  sigma is m x n with with sigma_ii = s_i
  note that this routine returns V^H, not V!
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
