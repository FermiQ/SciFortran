## Overview

The `SF_INTERPOLATE` module provides a comprehensive toolkit for data interpolation in SciFortran. It supports various interpolation methods for 1D and 2D datasets, including:

-   **Linear Interpolation:** Simple and fast, connecting data points with straight lines.
-   **Polynomial Interpolation:** Uses a single polynomial to fit a set of data points. Provided via wrappers to routines from Numerical Recipes.
-   **Cubic Spline Interpolation:** Produces smooth curves by fitting piecewise cubic polynomials, ensuring continuity of the function and its first two derivatives. It includes interfaces to DeBoer's cubic spline routines (from PPPACK).
-   **Bilinear Interpolation:** For interpolating values on a 2D regular grid.
-   **Object-Oriented Style Interpolation:** Defines `finter_type` and `finter2d_type` for managing 1D and 2D interpolation problems, allowing for initialization and repeated evaluation.

The module often groups specific implementations (e.g., for real or complex data, scalar or vector output points) under generic interfaces.

## Key Components

### Module: `SF_INTERPOLATE`
- **Purpose:** Provides a collection of routines and interfaces for 1D and 2D data interpolation.
- **Key Public Interfaces (details below):** `linear_spline`, `poly_spline`, `cubic_spline`.
- **Key Public Types (details below):** `finter_type`, `finter2d_type`.
- **Other Key Public Procedures (details below):** `locate`, `polint`, `polin2` (from Numerical Recipes), `init_finter`, `delete_finter`, `finter`, `cinter`, `init_finter2d`, `delete_finter2d`, `finter2d`, `bilinear_interpolate`.

---

### Public Types

#### Type: `finter_type`
- **Purpose:** Holds data for 1D function interpolation, allowing for initialization and repeated evaluation using polynomial interpolation.
- **Fields (simplified):**
    - `X` (real(8) array): Original x-coordinates.
    - `F` (real(8) array): Original y-coordinates (real part for complex).
    - `G` (real(8) array, optional): Original y-coordinates (imaginary part for complex).
    - `N` (integer): Order for polynomial interpolation.
- **Associated Procedures:** `init_finter_d`, `init_finter_c`, `delete_finter`, `finter`, `cinter`.

#### Type: `finter2d_type`
- **Purpose:** Holds data for 2D function interpolation using local polynomial interpolation.
- **Fields (simplified):**
    - `X`, `Y` (real(8) arrays): Original x and y grid coordinates.
    - `F` (real(8) 2D array): Original z-values (function values on grid).
    - `N` (integer): Order for local polynomial interpolation.
- **Associated Procedures:** `init_finter2d`, `delete_finter2d`, `finter2d`.

---

### Main Interpolation Interfaces

#### Interface: `linear_spline`
- **Purpose:** Performs 1D or 2D linear interpolation.
- **1D Variants:**
    - `d_linear_spline_s(Xin, Fin, Xout, Fout)`: Real scalar output.
    - `d_linear_spline_v(Xin, Fin, Xout, Fout)`: Real vector output.
    - `c_linear_spline_s(Xin, Fin, Xout, Fout)`: Complex scalar output.
    - `c_linear_spline_v(Xin, Fin, Xout, Fout)`: Complex vector output.
- **2D Variants (Bilinear):**
    - `d_linear_spline_2d_s(xin, yin, fin, xout, yout, fout)`: Real scalar output.
    - `d_linear_spline_2d_v(xin, yin, fin, xout_vec, yout_vec, fout_matrix)`: Real matrix output.
    - `c_linear_spline_2d_s(...)`, `c_linear_spline_2d_v(...)`: Complex versions.
- **Inputs (1D general):**
    - `Xin` (real(8) array): Input x-coordinates (sorted).
    - `Fin` (real(8)/complex(8) array): Input y-coordinates.
    - `Xout` (real(8) scalar or array): X-coordinate(s) for interpolation.
- **Outputs (1D general):**
    - `Fout` (real(8)/complex(8) scalar or array): Interpolated y-coordinate(s).
- **Inputs (2D general):**
    - `xin`, `yin` (real(8) arrays): Input grid x and y coordinates.
    - `fin` (2D real(8)/complex(8) array): Input function values on the grid.
    - `xout`, `yout` (real(8) scalar or array): Output coordinates.
- **Outputs (2D general):**
    - `fout` (scalar or 2D array): Interpolated function value(s).

#### Interface: `poly_spline`
- **Purpose:** Performs 1D or 2D polynomial interpolation using a local N-point scheme. For 1D, it uses `polint`. For 2D, it uses `polin2`.
- **1D Variants:** `d_poly_spline_s(Xin,Fin,Xout,Fout,N)`, `d_poly_spline_v(...)`, `c_poly_spline_s(...)`, `c_poly_spline_v(...)`.
- **2D Variants:** `d_poly_spline_2d_s(xin,yin,fin,xout,yout,fout,N)`, `d_poly_spline_2d_v(...)`, `c_poly_spline_2d_s(...)`, `c_poly_spline_2d_v(...)`.
- **Inputs (general):** Similar to `linear_spline`, plus:
    - `N` (integer, optional): Order of polynomial for local interpolation (default 5 for 1D, also for `finter_type`). For 2D, it refers to the local plaquette size.
- **Outputs (general):** Similar to `linear_spline`.

#### Interface: `cubic_spline`
- **Purpose:** Performs 1D cubic spline interpolation. Uses routines from PPPACK (`cubspl`, `ppvalu`).
- **Variants:** `d_cub_interp_s(Xin,Fin,Xout,Fout)`, `d_cub_interp_v(...)`, `c_cub_interp_s(...)`, `c_cub_interp_v(...)`.
- **Inputs (general):**
    - `Xin` (real(8) array): Input x-coordinates (must be sorted).
    - `Fin` (real(8)/complex(8) array): Input y-coordinates.
    - `Xout` (real(8) scalar or array): X-coordinate(s) for interpolation.
- **Outputs (general):**
    - `Fout` (real(8)/complex(8) scalar or array): Interpolated y-coordinate(s).
- **Note:** Boundary conditions for the cubic spline are typically "not-a-knot".

---

### Other Public Procedures

#### From Numerical Recipes (via `INTERPOLATE_NR` module):
-   **`locate(xx, x)`**: Function. Given a sorted array `xx`, finds index `j` such that `xx(j) <= x < xx(j+1)`.
-   **`polint(xa, ya, x, y, dy)`**: Subroutine. Performs polynomial interpolation of order `size(xa)-1`. Returns value `y` and error estimate `dy`.
-   **`polin2(x1a, x2a, ya, x1, x2, y, dy)`**: Subroutine. Performs polynomial interpolation in 2D.

#### For `finter_type` and `finter2d_type`:
-   **`init_finter_d(func_obj, Xin, Fin, N)` / `init_finter_c(func_obj, Xin, Fin, N)`**: Subroutines. Initialize an `finter_type` object `func_obj` with real/complex data.
-   **`delete_finter(func_obj)`**: Subroutine. Deallocates arrays within an `finter_type` object.
-   **`finter(func_obj, x)` / `cinter(func_obj, x)`**: Functions. Interpolate value at `x` using data in `func_obj` (real/complex).
-   **`init_finter2d(func2d_obj, Xin, Yin, Fin, N)`**: Subroutine. Initializes an `finter2d_type` object.
-   **`delete_finter2d(func2d_obj)`**: Subroutine. Deallocates arrays.
-   **`finter2d(func2d_obj, x, y)`**: Function. Interpolates value at `(x,y)` using data in `func2d_obj`.

#### Miscellaneous:
-   **`bilinear_interpolate(xgrid, ygrid, fgrid, x, y, delta)`**: Function. Performs bilinear interpolation on a regular grid. `delta` is an unused optional argument.
-   **`test_grid_equality_d(xin, xout, Fin, Fout)` / `test_grid_equality_c(...)`**: Subroutines. If input grid `xin` matches `xout`, copies `Fin` to `Fout` and returns, otherwise does nothing. Used for optimization.

## Important Variables/Constants

This module primarily provides procedures and derived types. It does not expose public module-level constants.

## Usage Examples

**1. Linear 1D Interpolation:**
```fortran
program test_linear_interp
  use SF_INTERPOLATE
  implicit none
  real(8), dimension(5) :: x_in = [0.0, 1.0, 2.0, 3.0, 4.0]
  real(8), dimension(5) :: f_in = [0.0, 0.5, 0.866, 1.0, 0.866] ! Approx sin(x*pi/6)
  real(8) :: x_out_s, f_out_s
  real(8), dimension(3) :: x_out_v = [0.5, 1.5, 2.5]
  real(8), dimension(3) :: f_out_v

  ! Scalar output
  x_out_s = 1.2
  call linear_spline(x_in, f_in, x_out_s, f_out_s)
  print *, "Linear interp at x=", x_out_s, " f(x)=", f_out_s

  ! Vector output
  call linear_spline(x_in, f_in, x_out_v, f_out_v)
  print *, "Linear interp at x_vec=", x_out_v
  print *, "f_vec(x)=", f_out_v
end program test_linear_interp
```

**2. Cubic Spline 1D Interpolation:**
```fortran
program test_cubic_spline
  use SF_INTERPOLATE
  implicit none
  real(8), dimension(5) :: x_in = [0.0, 1.0, 2.0, 3.0, 4.0]
  real(8), dimension(5) :: f_in = [0.0, 0.8415, 0.9093, 0.1411, -0.7568] ! sin(x)
  real(8) :: x_out_s, f_out_s

  x_out_s = 1.5
  call cubic_spline(x_in, f_in, x_out_s, f_out_s)
  print *, "Cubic spline interp at x=", x_out_s, " f(x)=", f_out_s
  ! Expected sin(1.5) approx 0.9975
end program test_cubic_spline
```

## Dependencies and Interactions

-   **`INTERPOLATE_NR`**: This module (from `interpolate_nr.f90`) is used, providing `locate`, `polint`, and `polin2` which are made public by `SF_INTERPOLATE`.
-   **Included Files**:
    -   `interpolate_cubspl_routines.f90`: Contains DeBoer's `cubspl` and `ppvalu` (from PPPACK) used by the `cubic_spline` interface.
    -   `interpolate_finter_1d.f90` / `interpolate_finter_2d.f90`: Define the `finter_type` / `finter2d_type` and associated methods (`init_finter`, `finter`, etc.).
    -   `interpolate_pack.f90`: Contains various interpolation helper routines (e.g., `interp_linear`, `lagrange_value`), some of which are used by the main spline interfaces.
    -   `interpolate_pppack.f90`: Contains a larger suite of routines from PPPACK (like `bsplvb`, `bsplpp`, `splint`). Some of these are used internally by `SF_INTERPOLATE`'s higher-level functions.
-   **Interactions**: Interpolation routines are essential for many numerical tasks, including data analysis, plotting, and as components in solvers for differential equations or integration routines.

```
