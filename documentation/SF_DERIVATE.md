## Overview

The `SF_DERIVATE` module in SciFortran offers a suite of tools for numerical differentiation. It primarily focuses on:
1.  Calculating derivatives of discretised functions (provided as arrays) using finite difference methods of various orders of accuracy. This includes first, second, third, fourth, and a general N-th order derivative.
2.  Computing Jacobian matrices and gradients for vector-valued or scalar functions (real and complex) provided as external procedures, using forward-difference approximations.

## Key Components

### Module: `SF_DERIVATE`
- **Purpose:** Provides routines for numerical differentiation of discretised arrays and for calculating Jacobian/gradient of functions.
- **Public Interfaces & Functions:**
    - `deriv(f, dh)`: Basic first derivative for discretised functions.
    - `derivative(f, dh, order)`: First derivative with selectable accuracy order.
    - `derivative2(f, dh, order)`: Second derivative with selectable accuracy order.
    - `derivative3(f, dh, order)`: Third derivative with selectable accuracy order.
    - `derivative4(f, dh, order)`: Fourth derivative with selectable accuracy order.
    - `derivativeN(f, dh, n)`: N-th derivative.
    - `djacobian`: Interface for calculating Jacobian of real-valued functions (takes user function/subroutine as input).
    - `dgradient`: Interface for calculating gradient of real-valued scalar functions.
    - `f_djacobian`: Function wrapper for `djacobian`.
    - `f_dgradient`: Function wrapper for `dgradient`.
    - `cjacobian`: Interface for calculating Jacobian of complex-valued functions.
    - `cgradient`: Interface for calculating gradient of complex-valued scalar functions.
    - `f_cjacobian`: Function wrapper for `cjacobian`.
    - `f_cgradient`: Function wrapper for `f_cgradient`.

---

### Derivatives of Discretised Functions

These functions operate on arrays of `real(8)` values, assumed to be evaluations of a function at points with constant spacing `dh`.

#### Function: `deriv`
- **Signature:** `Function deriv(f, dh) result(df)`
- **Purpose:** Calculates the first derivative of a real discretised function `f`. Uses first-order forward/backward differences at endpoints and second-order central differences elsewhere.
- **Inputs:**
    - `f` (real(8) array, intent(in)): Discretised function values.
    - `dh` (real(8), intent(in)): Spacing between points.
- **Outputs:**
    - `df` (real(8) array, size of `f`): The calculated first derivative.

#### Function: `derivative`
- **Signature:** `Function derivative(f, dh, order) result(df)`
- **Purpose:** Calculates the first derivative of `f`. The `order` parameter controls the accuracy of finite difference schemes used, especially at boundaries.
- **Inputs:**
    - `f` (real(8) array, intent(in)): Discretised function values.
    - `dh` (real(8), intent(in)): Spacing.
    - `order` (integer, optional, intent(in)): Order of accuracy.
        - `1`: :math:`O(dh)` at boundaries, :math:`O(dh^2)` central.
        - `2`: :math:`O(dh^2)` at boundaries and central.
        - `4` (default): :math:`O(dh^4)` at boundaries and central.
        - `6`: :math:`O(dh^6)` at boundaries and central.
- **Outputs:**
    - `df` (real(8) array, size of `f`): The calculated first derivative.

#### Function: `derivative2`, `derivative3`, `derivative4`
- **Signatures:**
    - `Function derivative2(f, dh, order) result(df)`
    - `Function derivative3(f, dh, order) result(df)`
    - `Function derivative4(f, dh, order) result(df)`
- **Purpose:** Calculate the second, third, or fourth derivative, respectively. The `order` parameter (default 4, options typically 2, 4, 6) similarly controls accuracy.
- **Inputs:** Same as `derivative`.
- **Outputs:** `df` (real(8) array, size of `f`): The calculated derivative.

#### Function: `derivativeN`
- **Signature:** `Function derivativeN(f, dh, n) result(df)`
- **Purpose:** Calculates the `n`-th derivative of `f` by repeatedly applying a 6th order accuracy first derivative calculation.
- **Inputs:**
    - `f` (real(8) array, intent(in)): Discretised function values.
    - `dh` (real(8), intent(in)): Spacing.
    - `n` (integer, intent(in)): The order of the derivative to compute.
- **Outputs:**
    - `df` (real(8) array, size of `f`): The calculated `n`-th derivative.

---

### Jacobian and Gradient Calculations

These routines calculate derivatives of functions passed as procedure arguments. They use forward-difference approximations. Both function and subroutine forms of the user's procedure are supported.

#### Interface: `djacobian` / `f_djacobian`
- **Purpose:** Calculates the :math:`m \times n` Jacobian matrix :math:`[\partial F_i / \partial x_j]` for a vector function :math:`F: \mathbb{R}^n \rightarrow \mathbb{R}^m`. `f_djacobian` is a function wrapper.
- **Typical Signature (function variant of `f_djacobian`):** `Function f_jac_mn_func(funcv, x, m) result(df)`
- **Inputs:**
    - `funcv`: User-supplied function `funcv(x, m)` or subroutine `funcv(x, m, y)` that evaluates the vector function.
    - `x` (real(8) array): Point at which to evaluate the Jacobian. (Size `n`)
    - `m` (integer, for M x N): Dimension of the function's output vector.
    - `ml`, `mu` (integer, optional for `djacobian`): Number of lower/upper sub-diagonals if Jacobian is banded.
    - `epsfcn` (real(8), optional for `djacobian`): Step size hint.
- **Outputs:**
    - `fjac` (real(8) array, `m x n` for `djacobian`) or `df` (for `f_djacobian`): The approximated Jacobian matrix.

#### Interface: `dgradient` / `f_dgradient`
- **Purpose:** Calculates the gradient :math:`\nabla f` for a scalar function :math:`f: \mathbb{R}^n \rightarrow \mathbb{R}`. `f_dgradient` is a function wrapper.
- **Typical Signature (function variant of `f_dgradient`):** `Function f_jac_1n_func(funcv, x) result(df)`
- **Inputs:**
    - `funcv`: User-supplied function `funcv(x)` or subroutine `funcv(x, y)` that evaluates the scalar function.
    - `x` (real(8) array): Point at which to evaluate the gradient. (Size `n`)
    - `epsfcn` (real(8), optional for `dgradient`): Step size hint.
- **Outputs:**
    - `fjac` (real(8) array, size `n` for `dgradient`) or `df` (for `f_dgradient`): The approximated gradient vector.

#### Complex Versions: `cjacobian`, `f_cjacobian`, `cgradient`, `f_cgradient`
- These interfaces and functions are analogous to their real counterparts but operate on functions :math:`F: \mathbb{R}^n \rightarrow \mathbb{C}^m` (for Jacobian) or :math:`f: \mathbb{R}^n \rightarrow \mathbb{C}` (for gradient). The output Jacobian/gradient will be complex.

## Important Variables/Constants

The module defines numerous `parameter` arrays holding finite difference coefficients. These are used internally by the `derivative` functions. Examples:
- `d_ccoeff_n2`: Coefficients for 2nd order central difference, 1st derivative. `[-0.5, 0, 0.5]`
- `d2_fcoeff_n4`: Coefficients for 4th order forward difference, 2nd derivative.
- And similar sets for various orders (n2, n4, n6, n8) and derivative degrees (d, d2, d3, d4), for both central (ccoeff) and forward/backward (fcoeff) schemes.

These coefficients are not typically used directly by the end-user but determine the accuracy and stencil of the derivative calculations.

## Usage Examples

**1. Derivative of a discretised array:**
```fortran
program test_sf_derivate_array
  use SF_DERIVATE
  use SF_ARRAYS, only: linspace ! For generating sample data
  implicit none

  real(8), allocatable :: x(:), y(:), dy_dx(:), d2y_dx2(:)
  real(8) :: dx
  integer :: n_points

  n_points = 100
  x = linspace(0.0d0, 2.0d0 * SF_CONSTANTS%pi, n_points, mesh=dx)
  y = sin(x) ! Example function y = sin(x)

  ! Calculate first derivative (default 4th order accuracy)
  dy_dx = derivative(y, dx)

  ! Calculate second derivative (explicit 6th order accuracy)
  d2y_dx2 = derivative2(y, dx, order=6)

  ! print *, "x, y, dy/dx (cos(x)), d2y/dx2 (-sin(x))"
  ! do i=1, n_points
  !   print '(4F12.6)', x(i), y(i), dy_dx(i), d2y_dx2(i)
  ! end do
  print *, "First few points for dy/dx (expected cos(x)):", dy_dx(1:5)
  print *, "First few points for d2y/dx2 (expected -sin(x)):", d2y_dx2(1:5)

end program test_sf_derivate_array
```

**2. Gradient of a scalar function:**
```fortran
program test_sf_derivate_gradient
  use SF_DERIVATE
  implicit none
  real(8) :: x(2), grad(2)

  x = [1.0d0, 2.0d0] ! Point at which to calculate gradient

  ! Calculate gradient of f(x1, x2) = x1**2 * x2**3
  grad = f_dgradient(my_function, x)
  ! Expected: [2*x1*x2**3, 3*x1**2*x2**2] = [2*1*8, 3*1*4] = [16, 12]
  print *, "Gradient at x=", x, " is grad=", grad

contains
  function my_function(v) result(f_val)
    real(8), dimension(:), intent(in) :: v
    real(8) :: f_val
    f_val = v(1)**2 * v(2)**3
  end function my_function
end program test_sf_derivate_gradient
```

## Dependencies and Interactions

- **Internal Structure:** The Jacobian and gradient routines (e.g., `fdjac_nn_func`) are included from separate files (`derivate_fjacobian_d.f90`, `derivate_fjacobian_c.f90`) into the `SF_DERIVATE` module.
- **Intrinsic Modules:** `implicit none` is used.
- **External Libraries:** No direct dependencies on external libraries like BLAS/LAPACK.
- **Interactions:** This module is fundamental for numerical methods. It would be used by optimization routines, solvers for differential equations, and any analysis requiring derivatives of functions or discretised data. It may use `SF_ARRAYS` for examples or testing, and `SF_CONSTANTS` for mathematical constants like Pi if needed internally (though example shows it).

```
