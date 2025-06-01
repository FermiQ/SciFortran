## Overview

The `SF_OPTIMIZE` module in SciFortran provides a comprehensive suite of routines for numerical optimization and root-finding. It offers a variety of algorithms to address different problem types:

-   **Function Minimization (Optimization):**
    -   **1D (Scalar) Minimization:**
        -   `brent`: Brent's method for minimization without derivatives.
        -   `dbrent`: Brent's method using user-supplied derivatives.
        -   `bracket`: Utility to bracket a minimum.
    -   **N-D (Multivariate) Unconstrained Minimization:**
        -   `fmin`: Nelder-Mead downhill simplex algorithm.
        -   `fmin_cg`: Conjugate Gradient methods (Fletcher-Reeves, Polak-Ribiere).
        -   `fmin_cgplus`: Another Conjugate Gradient implementation.
        -   `fmin_cgminimize`: Older Conjugate Gradient routine.
        -   `fmin_bfgs`: BFGS and L-BFGS-B algorithm for unconstrained and bound-constrained problems.
    -   **Least Squares:**
        -   `leastsq`: Minimizes the sum of squares of M equations in N variables (interface to MINPACK's `lmdif`/`lmder`).
        -   `curvefit`: Non-linear least squares fitting of a function to data (interface to MINPACK).
-   **Root Finding:**
    -   **1D (Scalar) Root Finding:** `brentq` (Brent's method), `bisect` (Bisection), `newton` (Newton-Raphson), `fzero` (general safeguarded root finder).
    -   **N-D (Systems of Equations):**
        -   `fsolve`: Solves systems of nonlinear equations (interface to MINPACK's `hybrd`/`hybrj`).
        -   `broyden1`: Broyden's first method for root finding.
-   **Fixed-Point Iteration Accelerators (Mixing Schemes):**
    -   `linear_mix`: Simple linear mixing.
    -   `adaptive_mix`: Linear mixing with an adaptive mixing parameter.
    -   `broyden_mix`: Broyden's mixing scheme.

The module leverages well-established numerical libraries like MINPACK and L-BFGS-B (often included as source) and provides interfaces to simplify their usage. Many routines offer variants for functions where derivatives are provided analytically versus those where derivatives must be approximated numerically.

## Key Components

### Module: `SF_OPTIMIZE`
- **Purpose:** Provides a collection of algorithms for numerical optimization, root finding, and least-squares fitting.
- **Uses Modules:** `CGFIT_ROUTINES`, `BROYDEN_ROUTINES` (defined in included files), `SF_CONSTANTS`, `SF_LINALG`.
- **Key Public Interfaces & Procedures (details grouped by functionality below).**

---

### Function Minimization (Optimization)

#### 1D Scalar Minimization
-   **`brent(func, xmin, brack, tol, niter)`**: Subroutine. Finds the minimum of a scalar function `func(x)` using Brent's method without derivatives.
    -   `xmin` (real(8), inout): Initial guess, output is abscissa of minimum.
    -   `brack` (real(8) array, optional, size 2 or 3): Bracketing interval `[ax, bx]` or triplet `[ax, bx, cx]`.
    -   Returns minimum function value implicitly through internal storage if not directly assigned.
-   **`dbrent`**: Interface for Brent's method using derivatives.
    -   `dbrent_wgrad(func, dfunc, xmin, brack, tol, niter)`: User provides derivative `dfunc(x)`.
    -   `dbrent_nograd(func, xmin, brack, tol, niter)`: Derivative is approximated numerically.
-   **`bracket(ax, bx, cx, fa, fb, fc, func)`**: Subroutine. Brackets a minimum of `func(x)`.

#### N-D Multivariate Unconstrained/Bound-Constrained Minimization
-   **`fmin(fn, start, lambda, tol, ...)`**: Subroutine. Minimizes `fn(x_vec)` using Nelder-Mead downhill simplex.
    -   `start` (real(8) array, inout): Initial guess, output is the point of minimum.
    -   `lambda` (real(8) array, optional): Initial step sizes for simplex.
-   **`fmin_cg`**: Interface. Conjugate Gradient methods.
    -   `fmin_cg_df(p, func, fjac, iter, fret, ...)`: User provides function `func(p)` and gradient `fjac(p)`.
    -   `fmin_cg_f(p, func, iter, fret, ...)`: Gradient approximated numerically.
    -   `p` (real(8) array, inout): Initial guess / output minimum point.
    -   `fret` (real(8), out): Minimum function value.
-   **`fmin_cgplus`**: Interface. Another Conjugate Gradient implementation (Gilbert & Nocedal). Variants for analytic vs. numerical gradient.
-   **`fmin_cgminimize`**: Interface. Older F77-style Conjugate Gradient routines (`minimize_krauth` or `minimize_sascha`). Variants for analytic vs. numerical gradient.
-   **`fmin_bfgs`**: Interface. BFGS (unconstrained) and L-BFGS-B (bound-constrained) algorithms.
    -   `bfgs_with_grad(func, grad, x, l, u, nbd, ...)`: User provides function `func(x)` and gradient `grad(x)`.
    -   `bfgs_no_grad(func, x, l, u, nbd, ...)`: Gradient approximated numerically.
    -   `x` (real(8) array, inout): Initial guess / output minimum point.
    -   `l`, `u` (real(8) arrays, optional): Lower and upper bounds.
    -   `nbd` (integer array, optional): Specifies bound types for each variable.

#### Least Squares
-   **`leastsq`**: Interface. Minimizes sum of squares of `m` equations in `n` variables. Wraps MINPACK's `lmdif` (Jacobian approximated) or `lmder` (Jacobian provided).
    -   `leastsq_lmdif_func(model_func, a, m, ...)`: `model_func(a,m)` returns vector of `m` function values for parameters `a`.
    -   `leastsq_lmder_func(model_func, model_dfunc, a, m, ...)`: Also takes `model_dfunc(a,m)` returning Jacobian matrix.
    -   Subroutine variants also exist.
    -   `a` (real(8) array, inout): Parameters to be fitted.
-   **`curvefit`**: Interface. Similar to `leastsq` but specifically for fitting a model function to `ydata` given `xdata`.
    -   `curvefit_lmdif_func(model_func, a, xdata, ydata, ...)`: `model_func(xdata_point, a_params)` returns model value.
    -   Variants for subroutines and analytic Jacobians exist.

---

### Root Finding

#### 1D Scalar Root Finding
-   **`brentq(func, a, b, tol) result(fzero)`**: Function. Brent's method for root finding in interval `[a,b]`.
-   **`bisect(f, x1, x2, eps, niter, flag)`**: Subroutine. Bisection method. `x1` (inout) returns the root.
-   **`newton(f, xinit, eps, niter)`**: Subroutine. Newton-Raphson method. `xinit` (inout) returns the root.
-   **`fzero(f, b, c, iflag, rguess, ...)`**: Subroutine. General safeguarded root finder (combination of bisection and secant). `b` (inout) returns the root.

#### N-D Systems of Equations
-   **`fsolve`**: Interface. Solves a system of `n` nonlinear equations `F(x)=0`. Wraps MINPACK's `hybrd` (Jacobian approximated) or `hybrj` (Jacobian provided).
    -   `fsolve_hybrd_func(func, x, ...)`: `func(x)` returns vector of function values.
    -   `fsolve_hybrj_func(func, dfunc, x, ...)`: Also takes `dfunc(x)` returning Jacobian.
    -   Subroutine variants exist.
    -   `x` (real(8) array, inout): Initial guess / output root.
-   **`broyden1(ff, x, ...)`**: Subroutine. Broyden's first method for finding root of `ff(x)=0`.
    -   `ff` is a procedure `ff(x)` that returns the vector of function values.
    -   `x` (real(8) array, inout): Initial guess / output root.

---

### Fixed-Point Iteration Accelerators (Mixing Schemes)

These routines aim to accelerate the convergence of fixed-point iterations `x_new = G(x_old)`, often expressed as finding `x` such that `x = G(x)` or `F(x) = G(x) - x = 0`. The `Fx` input to these routines is typically `G(x_old) - x_old`.

#### Interface: `linear_mix`
- **Purpose:** Simple linear mixing: `x_new = x_old + alpha * Fx`.
- **Specific Subroutines:** `d_linear_mix_<R>` and `c_linear_mix_<R>` for real/complex arrays of rank `<R>` (1 to 7).
- **Inputs:** `x` (inout), `Fx` (in), `alpha` (in).

#### Interface: `adaptive_mix`
- **Purpose:** Linear mixing where the mixing parameter `beta` for each component is adapted based on the sign of `Fx` in successive iterations.
- **Specific Subroutines:** `d_adaptive_mix`, `c_adaptive_mix`.
- **Inputs:** `x` (inout), `Fx` (in), `alpha` (base mixing, in), `iter` (current iteration number, in).

#### Interface: `broyden_mix`
- **Purpose:** More sophisticated mixing scheme based on Broyden's method to accelerate convergence.
- **Specific Subroutines:** `d_broyden_mix`, `c_broyden_mix`.
- **Inputs:** `X` (inout), `Fx` (in), `alpha` (in), `M` (number of previous steps to store for Broyden update, in), `iter` (current iteration, in), `w0` (optional weight, in).

## Important Variables/Constants

-   **`df_eps` (real(8), private):** A small value, typically `epsilon(1.0d0)`, used as a default step for numerical differentiation if an analytic Jacobian/gradient is not provided to routines like `fmin_bfgs` (no-gradient version) or `fmin_cg_f`.

## Usage Examples

**1. 1D Minimization using Brent's method:**
```fortran
program test_brent_min
  use SF_OPTIMIZE
  implicit none
  real(8) :: x_min_val, func_at_min
  real(8), dimension(3) :: bracket_interval = [-2.0d0, 0.0d0, 2.0d0] ! Ax, Bx, Cx

  ! Minimize f(x) = (x-1)^2
  call brent(my_func1d, x_min_val, brack=bracket_interval, tol=1.0d-7)
  func_at_min = my_func1d(x_min_val)
  print *, "Brent: Minimum of (x-1)^2 found at x =", x_min_val, "f(x) =", func_at_min

contains
  function my_func1d(x)
    real(8), intent(in) :: x
    real(8) :: my_func1d
    my_func1d = (x - 1.0d0)**2
  end function my_func1d
end program test_brent_min
```

**2. N-D Unconstrained Minimization using L-BFGS-B (via `fmin_bfgs`):**
```fortran
program test_fmin_bfgs_example
  use SF_OPTIMIZE
  implicit none
  real(8), dimension(2) :: x_initial = [ -1.2d0, 1.0d0 ]
  real(8) :: f_at_min
  integer :: iter_count, fault_code

  ! Minimize Rosenbrock function: f(x,y) = (1-x)^2 + 100*(y-x^2)^2
  ! No explicit gradient provided, will be approximated.
  ! No bounds provided (nbd will default to 0 for all variables).
  call fmin_bfgs(rosenbrock_func, x_initial, &
               & pgtol=1.0d-5, iprint=-1)  ! Suppress print from L-BFGS-B

  f_at_min = rosenbrock_func(x_initial)
  print *, "L-BFGS: Rosenbrock minimum at x =", x_initial
  print *, "Function value at minimum =", f_at_min
  ! Expected minimum: [1.0, 1.0] with f=0.0

contains
  function rosenbrock_func(p)
    real(8), dimension(:), intent(in) :: p
    real(8) :: rosenbrock_func
    rosenbrock_func = (1.0d0 - p(1))**2 + 100.0d0 * (p(2) - p(1)**2)**2
  end function rosenbrock_func
end program test_fmin_bfgs_example
```

## Dependencies and Interactions

-   **Internal Modules/Includes:**
    -   `CGFIT_ROUTINES` (from `optimize_cgfit_routines.f90`): Used by `fmin_cg`.
    -   `BROYDEN_ROUTINES` (from `optimize_broyden_routines.f90`): Used by `broyden1`.
    -   Numerous `.f90` and `.f` files containing specific algorithms (e.g., `brent.f90`, `fmin_Nelder_Mead.f90`, `lbfgsb.f`, MINPACK sources like `lmdif.f`, `hybrd.f`) are `include`d directly into `SF_OPTIMIZE.f90`.
-   **`SF_CONSTANTS`**: Used for mathematical constants like `pi` and machine precision values.
-   **`SF_LINALG`**: Used for linear algebra operations like matrix inversion (`inv_sym`) within some algorithms.
-   **External Libraries (Bundled Source):**
    -   **MINPACK**: Routines like `lmdif`, `lmder`, `hybrd`, `hybrj` are included for `leastsq` and `fsolve` functionalities.
    -   **L-BFGS-B**: The `lbfgsb.f` code is included for `fmin_bfgs`.
    -   **LINPACK/BLAS-like**: Some older Fortran 77 files (e.g., `cgblas.f`, `linpack.f`) contain basic linear algebra operations.
-   **Interactions**: This module is a core component for numerical problem-solving, providing essential tools for scientific applications that require finding optima or roots of functions.

```
