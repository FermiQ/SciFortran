## Overview

The `SF_LINALG` module provides a comprehensive suite of Fortran routines for performing linear algebra operations. It serves as a high-level interface to standard libraries like LAPACK and BLAS, and optionally SCALAPACK for parallel computations. The functionalities offered include:

-   **Eigenvalue Problems:** Solving for eigenvalues and eigenvectors for general, symmetric, and Hermitian matrices.
-   **Singular Value Decomposition (SVD):** Computing SVD and singular values.
-   **Matrix Inversion:** Inverting general, symmetric, Hermitian, and triangular matrices. Includes Gauss-Jordan elimination.
-   **Solving Linear Systems:** Routines for solving systems of linear equations `Ax=b`, including least-squares solutions.
-   **Tridiagonal Matrix Utilities:** Specific tools for building, checking, inverting, and getting diagonals of tridiagonal and block-tridiagonal matrices.
-   **Auxiliary Matrix Operations:** Calculating determinants, traces, creating identity/zeros/ones matrices, and constructing diagonal matrices.
-   **External Products:** Kronecker product, outer product, cross product, and scalar triple product.
-   **BLAS Wrappers:** Matrix multiplication using BLAS routines.

The module extensively uses interfaces to provide generic procedures that can handle different data types (real and complex) and variations of problems.

## Key Components

### Module: `SF_LINALG`
- **Purpose:** Provides a high-level API for a wide range of linear algebra tasks, often wrapping LAPACK, BLAS, and (optionally) SCALAPACK routines.
- **Uses Modules:** `SF_BLACS` (conditionally for SCALAPACK support).
- **Key Public Interfaces (details grouped by functionality below):**
    - Eigenvalue Problems: `eig`, `eigh`, `p_eigh` (parallel), `eigh_jacobi`, `eigvals`, `eigvalsh`.
    - SVD: `svdvals`, `svd`.
    - Matrix Inversion: `inv`, `p_inv` (parallel), `inv_sym`, `inv_her`, `inv_triang`, `inv_gj`.
    - Linear Systems: `solve`, `lstsq`.
    - Tridiagonal Utilities: `inv_tridiag`, `eye_tridiag` (for `deye_tridiag`, `zeye_tridiag`), `check_tridiag`, `get_tridiag`, `build_tridiag`.
    - Auxiliary: `det`, `eye` (and `deye`, `zeye`), `zeros`, `ones`, `diag`, `diagonal`, `trace`.
    - Products: `kron` (operator `.kx.`), `kronecker_product`, `outerprod`, `cross_product`, `s3_product`.
    - BLAS: `mat_product` (operator `.x.`), `p_mat_product` (parallel operator `.Px.`).
- **Other Public Procedures:** `upper_triangle`, `outerdiff`, `arth`, `shift_dw` (Note: `free_unit` seems out of place here and is part of `IOFILE`).

---

### Eigenvalue Problems
(Implementations in `linalg_eig.f90`, `linalg_eigh.f90`, `linalg_eigh_jacobi.f90`, `linalg_eigvals.f90`, `linalg_eigvalsh.f90`)

#### Interface: `eig`
- **Purpose:** Solves eigenvalue/eigenvector problems for general non-symmetric real (`deig`) or complex (`zeig`) matrices.
- **Inputs:** `A` (matrix), optional `jobvl` (left eigenvectors), `jobvr` (right eigenvectors).
- **Outputs:** `Eval` (eigenvalues), `Evec` (eigenvectors, typically right if `jobvr='V'`).

#### Interface: `eigh`
- **Purpose:** Solves eigenvalue/eigenvector problems for real symmetric (`deigh_simple`, `deigh_generalized`, `deigh_tridiag`) or complex Hermitian (`zeigh_simple`, `zeigh_generalized`) matrices.
- **Inputs:** `A` (matrix), optionally `B` for generalized problem `Ax = lambda Bx`.
- **Outputs:** `Eval` (eigenvalues), `Evec` (eigenvectors).

#### Interface: `p_eigh` (Requires SCALAPACK)
- **Purpose:** Parallel version of `eigh` for distributed matrices.

#### Interface: `eigh_jacobi`
- **Purpose:** Uses Jacobi method for real symmetric (`d_jacobi`) or complex Hermitian (`c_jacobi`) matrices. Eigenvectors are unsorted.
- **Inputs/Outputs:** Similar to `eigh`.

#### Interface: `eigvals` / `eigvalsh`
- **Purpose:** Compute only eigenvalues for general (`eigvals`) or symmetric/Hermitian (`eigvalsh`) matrices.
- **Inputs:** `A` (matrix).
- **Outputs:** `Eval` (eigenvalues).

---

### Singular Value Decomposition (SVD)
(Implementations in `linalg_svd.f90`, `linalg_svdvals.f90`)

#### Interface: `svd`
- **Purpose:** Computes the SVD: `A = U * Sigma * V^H`.
- **Specific Functions:** `dsvd` (real), `zsvd` (complex).
- **Inputs:** `A` (matrix).
- **Outputs:** `s` (singular values), `U` (left singular vectors), `Vtransp` (V^H or V^T).

#### Interface: `svdvals`
- **Purpose:** Computes only the singular values of a matrix.
- **Specific Functions:** `dsvdvals` (real), `zsvdvals` (complex).
- **Inputs:** `A` (matrix).
- **Outputs:** `s` (singular values).

---

### Matrix Inversion
(Implementations in `linalg_inv.f90`, `linalg_inv_sym.f90`, `linalg_inv_her.f90`, `linalg_inv_triang.f90`, `linalg_inv_gj.f90`)

#### Interface: `inv`
- **Purpose:** Inverts general square matrices (real `dinv`, complex `zinv`). Modifies input matrix.
- **Inputs/Outputs:** `Am` (matrix, inout).

#### Interface: `p_inv` (Requires SCALAPACK)
- **Purpose:** Parallel matrix inversion.

#### Others: `inv_sym`, `inv_her`, `inv_triang`, `inv_gj`
- **Purpose:** Inversion for specific matrix types: symmetric, Hermitian, triangular, or using Gauss-Jordan.

---

### Solving Linear Systems
(Implementations in `linalg_solve.f90`, `linalg_lstsq.f90`)

#### Interface: `solve`
- **Purpose:** Solves `Ax=b` for `x`. Supports single (`_1rhs`) or multiple (`_Mrhs`) right-hand sides.
- **Specific Subroutines:** `dsolve_1rhs`, `zsolve_1rhs`, `dsolve_Mrhs`, `zsolve_Mrhs`.
- **Inputs:** `A` (matrix), `b` (vector or matrix for RHS), optional `trans` (transpose option).
- **Outputs:** `b` is overwritten with solution `x`. `A` is overwritten with LU factors.

#### Interface: `lstsq`
- **Purpose:** Computes least-squares solution for `Ax=b` (real `dlstsq`, complex `zlstsq`).
- **Inputs:** `A` (matrix), `b` (vector).
- **Outputs:** `x` (least-squares solution vector).

---

### Tridiagonal Matrix Utilities
(Implementations in `linalg_inv_tridiag.f90`, etc.)

-   **`inv_tridiag`**: Interface to invert (block) tridiagonal matrices.
-   **`deye_tridiag(Nblock,N)` / `zeye_tridiag(Nblock,N)`**: Functions. Return block identity for tridiagonal systems.
-   **`check_tridiag`**: Interface. Checks if a matrix is (block) tridiagonal.
-   **`get_tridiag`**: Interface. Extracts diagonals from a (block) tridiagonal matrix.
-   **`build_tridiag`**: Interface. Constructs a (block) tridiagonal matrix from diagonals.

---

### Auxiliary Matrix Operations
(Implementations in `linalg_auxiliary.f90`)

-   **`det(A)`**: Interface. Computes determinant (real `ddet`, complex `zdet`).
-   **`eye(N)` / `deye(N)` / `zeye(N)`**: Interfaces. Returns NxN identity matrix.
-   **`zeros(...)` / `ones(...)`**: Interfaces. Return matrices/arrays of zeros/ones of specified dimensions (up to 7D).
-   **`diag(x)`**: Interface. Creates a diagonal matrix from vector `x`.
-   **`diagonal(A)`**: Interface. Extracts the diagonal of matrix `A`.
-   **`trace(A)`**: Interface. Computes the trace of matrix `A`.
-   **`upper_triangle(j,k,extra)`**: Function. Creates a logical mask for an upper triangle.
-   **`outerdiff(a,b)`**: Function. Computes outer difference `a(i) - b(j)`.
-   **`arth(first,increment,n)`**: Function. Generates an arithmetic sequence.
-   **`shift_dw(x_in)`**: Function. Bit manipulation (purpose unclear from name alone, likely specific utility).

---

### External Products & BLAS
(Implementations in `linalg_external_products.f90`, `linalg_blas.f90`)

-   **`kron(A,B)` (also `kronecker_product`, `.kx.`)**: Interface. Kronecker product of matrices.
-   **`outerprod(a,b)`**: Interface. Outer product of two vectors.
-   **`cross_product(a,b)`**: Interface. 3D vector cross product.
-   **`s3_product(a,b,c)`**: Interface. Scalar triple product `a . (b x c)`.
-   **`mat_product(A,B,C,alfa,beta)` (also `.x.`)**: Interface. Matrix product `C = alfa*A*B + beta*C` using BLAS `DGEMM`/`ZGEMM`.
-   **`p_mat_product` (also `.Px.`)**: Interface (Requires SCALAPACK). Parallel matrix product.

## Important Variables/Constants
The module defines private constants `zero = (0.0, 0.0)`, `xi = (0.0, 1.0)`, `one = (1.0, 0.0)` for internal use. No public constants are exposed.

## Usage Examples

**1. Matrix Inversion:**
```fortran
program test_linalg_inv
  use SF_LINALG
  implicit none
  real(8), dimension(2,2) :: A, A_inv
  A(1,:) = [2.0d0, 1.0d0]
  A(2,:) = [1.0d0, 2.0d0]
  A_inv = A
  call inv(A_inv) ! A_inv now holds the inverse
  print *, "Original A:", A(1,:), A(2,:)
  print *, "Inverse A_inv:", A_inv(1,:), A_inv(2,:)
  ! Expected: [[0.666, -0.333], [-0.333, 0.666]]
end program test_linalg_inv
```

**2. Solving Ax = b:**
```fortran
program test_linalg_solve
  use SF_LINALG
  implicit none
  real(8), dimension(2,2) :: A
  real(8), dimension(2)   :: b, x
  A(1,:) = [3.0d0, 1.0d0]
  A(2,:) = [1.0d0, 2.0d0]
  b      = [9.0d0, 8.0d0]
  x = b ! Copy b to x, as solve overwrites RHS with solution
  call solve(A, x) ! A is LU decomposed, x contains solution
  print *, "Solution x:", x
  ! Expected: [2.0, 3.0]
end program test_linalg_solve
```

**3. Eigenvalue Problem (Symmetric):**
```fortran
program test_linalg_eigh
  use SF_LINALG
  implicit none
  real(8), dimension(2,2) :: A
  real(8), dimension(2)   :: eigenvalues
  real(8), dimension(2,2) :: eigenvectors

  A(1,:) = [2.0d0, 1.0d0]
  A(2,:) = [1.0d0, 2.0d0]

  call eigh(A, eigenvalues, eigenvectors) ! For symmetric A
  print *, "Eigenvalues:", eigenvalues
  print *, "Eigenvectors (columns):"
  print *, eigenvectors(1,:)
  print *, eigenvectors(2,:)
  ! Expected eigenvalues: [1.0, 3.0] (or vice-versa)
end program test_linalg_eigh
```

## Dependencies and Interactions

-   **LAPACK and BLAS**: The core functionality of `SF_LINALG` (eigenvalue problems, SVD, matrix inversions, solving linear systems, matrix multiplication) relies heavily on underlying calls to LAPACK and BLAS libraries. These must be linked during compilation.
-   **SCALAPACK (Optional)**: If compiled with SCALAPACK support (e.g., using `-D_SCALAPACK` flag), parallel versions of some routines become available (`p_eigh`, `p_inv`, `p_mat_product`). These require the `SF_BLACS` module for BLACS context management.
-   **Internal Structure**: The module `SF_LINALG` uses `include` statements to incorporate implementation files like `linalg_eig.f90`, `linalg_blas.f90`, etc. These included files contain the wrapper code around LAPACK/BLAS calls.
-   **Interactions**: This module provides fundamental linear algebra operations essential for a wide range of scientific and engineering applications built with SciFortran.

```
