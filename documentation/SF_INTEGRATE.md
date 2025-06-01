## Overview

The `SF_INTEGRATE` module provides a comprehensive suite of routines for numerical integration in SciFortran. It caters to various integration needs, including:

-   **Basic Quadrature Rules:** Trapezoidal and Simpson's rules for integrating functions provided as discretised data arrays (1D and 2D).
-   **Adaptive Gaussian Quadrature:** High-precision integration of user-defined Fortran functions using adaptive Gauss-Kronrod schemes (leveraging the `GAUSS_QUADRATURE` module, which is based on the work by Jacob Williams). This is exposed via the `gauss_quad` and `integrate` interfaces.
-   **QUADPACK Routines:** A versatile set of routines (via the `quad` interface) for integrating user-defined functions, including those with singularities, infinite intervals, or specific weight functions (e.g., for Fourier transforms). The module includes wrappers for common QUADPACK functions like `QAGS`, `QAGI`, `QAWO`, etc.
-   **Kramers-Kronig Transform:** A specific function `kronig` for performing this transform.
-   **Auxiliary Routines:** Helper routines, such as `get_quadrature_weights` for Simpson's rule coefficients.

The module often provides interfaces that map to specific procedures for real (`d_...`) and complex (`c_...`) data types, as well as for functions defined as procedures versus those provided as sampled data.

## Key Components

### Module: `SF_INTEGRATE`
- **Purpose:** Offers a wide array of numerical integration methods for functions and discretised data.
- **Key Public Interfaces (details below):**
    - `trapz`: Trapezoidal rule for 1D data/functions.
    - `simps`: Simpson's rule for 1D data/functions.
    - `trapz2d`: Trapezoidal rule for 2D data/functions.
    - `simps2d`: Simpson's rule for 2D data/functions.
    - `quad`: Interface to various QUADPACK routines for adaptive integration of functions.
    - `gauss_quad` / `integrate`: Interface to adaptive Gaussian quadrature routines (from `GAUSS_QUADRATURE` module).
- **Key Public Functions/Subroutines:**
    - `kronig`: Performs Kramers-Kronig integration.
    - `get_quadrature_weights`: Provides weights for Simpson's rule.

---

### Basic Quadrature for Discretised Data and Functions

#### Interface: `trapz`
- **Purpose:** Performs 1D integration using the trapezoidal rule.
- **Variants:**
    - For sampled data: `d_trapz_ab_sample(f,a,b)`, `c_trapz_ab_sample(f,a,b)` (fixed interval `a,b`), `d_trapz_dh_sample(f,dh)`, `c_trapz_dh_sample(f,dh)` (fixed spacing `dh`), `d_trapz_nonlin_sample(f,x)`, `c_trapz_nonlin_sample(f,x)` (non-uniform spacing given by `x`).
    - For functions: `d_trapz_ab_func(my_func,a,b,N)`, `c_trapz_ab_func(my_func,a,b,N)` (fixed interval `a,b`, `N` points), `d_trapz_nonlin_func(my_func,x)`, `c_trapz_nonlin_func(my_func,x)` (points given by `x`).
- **Inputs (general):**
    - `f` (real(8)/complex(8) array or function): Data array or user-defined function.
    - `a`, `b` (real(8)): Integration limits.
    - `dh` (real(8)): Constant spacing for sampled data.
    - `x` (real(8) array): Array of x-coordinates for non-uniformly sampled data or function evaluation points.
    - `N` (integer, optional): Number of points for function integration over an interval.
- **Outputs (general):**
    - `int` (real(8)/complex(8)): The calculated integral.

#### Interface: `simps`
- **Purpose:** Performs 1D integration using Simpson's rule.
- **Variants:** Similar to `trapz`, includes `_ab_sample`, `_dh_sample`, `_nonlin_sample` for sampled data, and `_ab_func`, `_nonlin_func` for functions (real `d_` and complex `c_` versions).
- **Inputs/Outputs:** Similar to `trapz`.

#### Interface: `trapz2d` / `simps2d`
- **Purpose:** Performs 2D integration using Trapezoidal (`trapz2d`) or Simpson's (`simps2d`) rules.
- **Variants:**
    - For sampled data: `d_trapz2d_sample(func_matrix, dhx, dhy, xrange, yrange)`, `c_trapz2d_sample(...)`, `d_simps2d_sample(...)`, `c_simps2d_sample(...)`.
    - For functions: `d_trapz2d_func(my_func2d, xrange, yrange, Nx, Ny)`, `c_trapz2d_func(...)`, `d_simps2d_func(...)`, `c_simps2d_func(...)`. Recursive versions also exist (e.g., `d_trapz2d_func_recursive`).
- **Inputs (general):**
    - `func_matrix` (2D array) or `my_func2d` (function `my_func2d(xy_vec)`): 2D data or function.
    - `dhx`, `dhy` (real(8), optional): Spacing for sampled data.
    - `xrange`, `yrange` (real(8) array of size 2): Integration limits `[x_min, x_max]`, `[y_min, y_max]`.
    - `Nx`, `Ny` (integer): Number of points for function integration.
- **Outputs (general):**
    - `int` (real(8)/complex(8)): The calculated 2D integral.

---

### Adaptive Quadrature for Functions

#### Interface: `quad`
- **Purpose:** Provides access to various QUADPACK routines for numerical integration of a user-defined function `func(x)`. Allows fine-grained control over error tolerances, handling of singularities, infinite intervals, and weighted integration.
- **Key Subroutine:** `quad_func(func, a, b, ...)` (many optional arguments to select specific QUADPACK routine and its parameters). A `quad_sample` variant also exists which first interpolates sampled data.
- **Inputs (selected):**
    - `func` (external function `func(x)` returning real(8)): The function to integrate.
    - `a`, `b` (real(8)): Integration limits. `b` is optional if `inf` is used.
    - `epsabs`, `epsrel` (real(8), optional): Absolute and relative error tolerances.
    - `key` (integer, optional): Selects Gauss-Kronrod rule for `QAG` (e.g., 1-6).
    - `inf` (integer, optional): For `QAGI`, specifies interval: -1 for (-inf, b), 1 for (a, inf), 2 for (-inf, inf).
    - `singular_points` (real(8) array, optional): Locations of singularities for `QAGP`.
    - `cpole` (real(8), optional): Location of Cauchy principal value pole for `QAWC`.
    - `omega`, `weight_func` (optional): For `QAWO` (finite interval oscillatory) or `QAWF` (Fourier transform). `weight_func` selects cos or sin.
    - `alfa`, `beta` (optional): For `QAWS` (algebraic/logarithmic endpoint singularities).
- **Outputs:**
    - `result` (real(8)): The value of the integral.
    - `abserr` (real(8), output from wrapped QUADPACK): Estimate of the absolute error.
    - `neval`, `ier` (integer, output from wrapped QUADPACK): Number of function evaluations and error flag.

#### Interface: `gauss_quad` / `integrate`
- **Purpose:** Performs adaptive Gaussian quadrature for 1D or N-D functions (up to 6D). This interface uses routines from the `GAUSS_QUADRATURE` module. `integrate` is an alias for `gauss_quad`.
- **Variants:**
    - 1D for `f(x)` returning scalar: `integrate_1d_func_1(my_func, xl, xu, ans, ...)`
    - 1D for `f(x,m)` returning vector: `integrate_1d_func_main(m, my_f_vec, xl, xu, ans_vec, ...)`
    - N-D for `f(x_vec)` returning scalar: `integrate_nd_func_1(my_func_nd, xl_vec, xu_vec, ans, ...)`
    - N-D for `f(x_vec,m)` returning vector: `integrate_nd_func_main(m, my_f_vec_nd, xl_vec, xu_vec, ans_vec, ...)`
    - For sampled data (1D, 2D): `integrate_1d_sample`, `integrate_2d_sample`.
- **Inputs (general for function variants):**
    - `my_func...`: User-defined Fortran function.
    - `xl`, `xu` (real(8) scalar or array): Lower and upper integration limits.
    - `tol` / `tols` (real(8) scalar or array, optional): Error tolerance(s).
    - `method` / `methods` (integer scalar or array, optional): Quadrature points (6, 8, 10, 12, 14). Default 10.
- **Outputs:**
    - `ans` / `ans_vec`: The calculated integral(s).
    - `ierr`, `err` (optional): Error flag and estimated error.

---

### Other Routines

#### Function: `kronig`
- **Signature:** `Function kronig(fi, wr, M) result(fr)`
- **Purpose:** Performs a fast Kramers-Kronig transform.
- **Inputs:**
    - `fi` (real(8) array, size `M`): Input array (e.g., imaginary part).
    - `wr` (real(8) array, size `M`): Array of regularly spaced points (e.g., frequencies).
    - `M` (integer): Size of the arrays.
- **Outputs:**
    - `fr` (real(8) array, size `M`): Output array (e.g., real part).

#### Subroutine: `get_quadrature_weights`
- **Signature:** `Subroutine get_quadrature_weights(wt, nrk)`
- **Purpose:** Fills the `wt` array with quadrature weights for Simpson's rule or trapezoidal rule, based on `nrk`. Used internally by `simps` routines.
- **Inputs:**
    - `nrk` (integer, optional): Order of rule. 2 for trapezoidal, 4 (default) for Simpson's variants.
- **Outputs:**
    - `wt` (real(8) array, intent(out)): Quadrature weights.

## Important Variables/Constants

The module `SF_INTEGRATE` itself makes its internal constants `pi`, `zero`, `xi`, `one` private. The `GAUSS_QUADRATURE` module defines some internal parameters for its methods, but these are not directly exposed as public constants by `SF_INTEGRATE`.

## Usage Examples

**1. Simpson's rule for a sampled function:**
```fortran
program test_sf_integrate_sample
  use SF_INTEGRATE
  use SF_ARRAYS, only: linspace
  use SF_CONSTANTS, only: pi
  implicit none

  real(8), allocatable :: x(:), y(:)
  real(8) :: integral_val, a, b
  integer :: n_points

  n_points = 101 ! Must be odd for simple Simpson's rule implementation
  a = 0.0d0
  b = pi

  x = linspace(a, b, n_points)
  y = sin(x) ! Function y = sin(x)

  ! Integrate sin(x) from 0 to pi (expected result is 2.0)
  integral_val = d_simpson_ab_sample(y, a, b)
  print *, "Integral of sin(x) from 0 to pi (sampled):", integral_val

end program test_sf_integrate_sample
```

**2. Adaptive Gaussian quadrature for a Fortran function:**
```fortran
program test_sf_integrate_gauss
  use SF_INTEGRATE
  use SF_CONSTANTS, only: pi
  implicit none

  real(8) :: result, lower_lim, upper_lim, abs_err
  integer :: err_flag

  lower_lim = 0.0d0
  upper_lim = pi / 2.0d0

  ! Integrate cos(x) from 0 to pi/2 (expected result is 1.0)
  call integrate_1d_func_1(cos_func, lower_lim, upper_lim, result, &
                         & tol=1.0d-8, method=10, ierr=err_flag, err=abs_err)

  print *, "Integral of cos(x) from 0 to pi/2 (Gauss):", result
  print *, "Estimated error:", abs_err, "Error flag:", err_flag

contains
  function cos_func(x_val) result(y_val)
    real(8), intent(in) :: x_val
    real(8) :: y_val
    y_val = cos(x_val)
  end function cos_func
end program test_sf_integrate_gauss
```

## Dependencies and Interactions

-   **`GAUSS_QUADRATURE`**: This module is used internally and its main routines are exposed via `gauss_quad` and `integrate` interfaces. `GAUSS_QUADRATURE` itself implements adaptive Gaussian quadrature.
-   **QUADPACK**: The `quad` interface provides wrappers to various QUADPACK routines (which are classic Fortran 77 routines for numerical integration, not part of this SciFortran codebase but assumed to be available if these specific features are used, though `SF_INTEGRATE` includes Fortran translations of some QUADPACK routines like `QAGS`, `QAGI` etc. in `integrate_quad_func.f90` and `integrate_quad_sample.f90`).
-   **Internal `include` files**:
    -   `integrate_func_1d.f90`, `integrate_sample_1d.f90`: Basic 1D rules (Trapezoidal, Simpson's).
    -   `integrate_func_2d.f90`, `integrate_sample_2d.f90`: Basic 2D rules.
    -   `integrate_quad_func.f90`, `integrate_quad_sample.f90`: Wrappers for QUADPACK-like routines.
-   **Uses `SF_ARRAYS`**: Specifically `sf_integrate_linspace` (which is a copy of `linspace`) is used internally in some routines.
-   **Uses `SF_CONSTANTS`**: For `pi`, `xi`, etc., though these are defined privately within `SF_INTEGRATE`.

This module is crucial for any numerical computation requiring the integration of functions or discretised data.

```
