## Overview

The `SF_ARRAYS` module is a SciFortran component dedicated to the creation and manipulation of various types of numerical arrays and sequences. It provides functions to generate evenly spaced numbers on linear or logarithmic scales, integer ranges, and more complex custom spacing schemes like "upmspace" for creating meshes that are denser in certain regions.

## Key Components

### Module: `SF_ARRAYS`
- **Purpose:** SciFortran module for array creation and manipulation.
- **Contains:** `linspace`, `logspace`, `arange`, `upmspace`, `upminterval`, `powspace`

### Function: `linspace`
- **Signature:** `Function linspace(start, stop, num, istart, iend, mesh) result(array)`
- **Purpose:** Returns an array of `num` evenly spaced numbers over a specified interval from `start` to `stop`. The inclusion of `start` and `stop` points can be controlled by `istart` and `iend` respectively.
- **Inputs:**
    - `start` (real(8)): Starting value of the sequence.
    - `stop` (real(8)): End value of the sequence.
    - `num` (integer): Number of samples to generate.
    - `istart` (logical, optional): If `.true.` (default), `start` is included.
    - `iend` (logical, optional): If `.true.` (default), `stop` is included.
    - `mesh` (real(8), optional, out): If present, the step size is saved in this variable.
- **Outputs:**
    - `array` (real(8) array of size `num`): The generated array of evenly spaced numbers.

### Function: `logspace`
- **Signature:** `Function logspace(start, stop, num, base) result(array)`
- **Purpose:** Returns `num` numbers spaced evenly on a log scale, from `start` to `stop`. The base of the logarithm can be specified.
- **Inputs:**
    - `start` (real(8)): The starting value of the sequence (must be positive; 0 is shifted to 1e-12).
    - `stop` (real(8)): The end value of the sequence (must be positive; 0 is shifted to 1e-12).
    - `num` (integer): Number of samples to generate.
    - `base` (real(8), optional): The base of the logarithm (default is 10.0).
- **Outputs:**
    - `array` (real(8) array of size `num`): The generated array of logarithmically spaced numbers.

### Function: `arange`
- **Signature:** `Function arange(start, num) result(array)`
- **Purpose:** Returns an array of `num` integers, starting with `start` and incrementing by 1.
- **Inputs:**
    - `start` (integer): First element of the array.
    - `num` (integer): Length of the array.
- **Outputs:**
    - `array` (integer array of size `num`): Contains integers from `start` to `start + num - 1`.

### Function: `upmspace`
- **Signature:** `Function upmspace(start, stop, p, u, ndim, base, istart, iend, mesh) result(aout)`
- **Purpose:** Returns an array of numbers spaced linearly between exponentially spaced checkpoints. The interval [`start`, `stop`] is divided into `p` coarse regions with exponentially increasing widths (base `base`), and each coarse interval is then linearly divided into `u` subintervals.
- **Inputs:**
    - `start` (real(8)): First element of the array.
    - `stop` (real(8)): Last element of the array.
    - `p` (integer): Number of coarse exponential subdivisions.
    - `u` (integer): Number of fine linear subdivisions within each coarse interval.
    - `ndim` (integer): Length of the output array, must be `p*u` or `p*u + 1`.
    - `base` (real(8), optional): Base of the exponential spacing (default 2.0).
    - `istart` (logical, optional): If `.true.` (default), `start` is included.
    - `iend` (logical, optional): If `.true.` (default), `stop` is included.
    - `mesh` (real(8) array, optional, out): If present, contains the distances between consecutive points.
- **Outputs:**
    - `aout` (real(8) array of size `ndim`): The generated array with "upm" spacing.

### Function: `upminterval`
- **Signature:** `Function upminterval(start, stop, midpoint, p, q, type, base, mesh) result(array)`
- **Purpose:** Returns an array of numbers with spacing similar to `upmspace`, but configured specularly around a `midpoint`. The mesh can be thicker around the `midpoint` or the boundaries (`start`, `stop`) based on the `type` parameter.
- **Inputs:**
    - `start` (real(8)): First element of the array.
    - `stop` (real(8)): Last element of the array.
    - `midpoint` (real(8)): The point around which the mesh spacing is specular.
    - `p` (integer): Number of coarse subdivisions on each side of `midpoint`.
    - `q` (integer): Number of fine subdivisions within each coarse interval.
    - `type` (integer, optional): If 0 (default), mesh is thicker at `start` and `stop`. If 1, mesh is thicker around `midpoint`.
    - `base` (real(8), optional): Base of the exponential spacing (default 2.0).
    - `mesh` (real(8) array, optional, out): If present, contains distances between consecutive points.
- **Outputs:**
    - `array` (real(8) array of size `2*p*q + 1`): The generated array.

### Function: `powspace`
- **Signature:** `Function powspace(start, stop, num, base) result(array)`
- **Purpose:** Returns `num` numbers spaced on an exponential scale. The i-th number is `start + (stop - start) * base**(-num + i)`.
- **Inputs:**
    - `start` (real(8)): First element of the array.
    - `stop` (real(8)): Last element of the array (used to determine the range).
    - `num` (integer): Number of elements in the array.
    - `base` (real(8), optional): Base of the exponential (default 2.0).
- **Outputs:**
    - `array` (real(8) array of size `num`): The generated array of exponentially spaced numbers.

## Important Variables/Constants

This module does not expose public module-level variables or constants. Configuration is done via function arguments.

## Usage Examples

```fortran
program test_sf_arrays
  use SF_ARRAYS
  implicit none

  real(8), allocatable :: arr1(:), arr2(:), arr3(:)
  integer, allocatable :: arr_int(:)
  real(8) :: mesh_step

  ! Example for linspace
  arr1 = linspace(0.0d0, 1.0d0, 5)
  ! arr1 will be [0.0, 0.25, 0.5, 0.75, 1.0]
  print *, "linspace(0,1,5): ", arr1

  arr1 = linspace(0.0d0, 1.0d0, num=4, istart=.false., iend=.false(), mesh=mesh_step)
  ! arr1 will be [0.2, 0.4, 0.6, 0.8], mesh_step will be 0.2
  print *, "linspace open interval (0,1,4): ", arr1, "step:", mesh_step

  ! Example for logspace
  arr2 = logspace(0.1d0, 100.0d0, 4, base=10.0d0)
  ! arr2 will be [0.1, 1.0, 10.0, 100.0]
  print *, "logspace(0.1,100,4,base=10): ", arr2

  ! Example for arange
  arr_int = arange(1, 5)
  ! arr_int will be [1, 2, 3, 4, 5]
  print *, "arange(1,5): ", arr_int

  ! Example for powspace
  arr3 = powspace(0.0d0, 1.0d0, 5, base=2.0d0)
  ! arr3 will be [0.0, 0.0625, 0.125, 0.25, 0.5] (approx, due to formula)
  ! (stop - start) * base**(-num+i) part:
  ! i=1: 2^-4 = 0.0625 (array(1)=start=0)
  ! i=2: 2^-3 = 0.125. array(2) = 0 + 1*0.0625 -- this is slightly off.
  ! The actual formula is: forall(i=2:num)array(i)=start + (stop-start)*base_**(-num+i)
  ! array(1) = start
  ! array(2) = start + (stop-start)*base**(-num+2)
  ! array(num) = start + (stop-start)*base**0 = start + (stop-start) = stop
  ! For powspace(0,1,5,2):
  ! arr(1)=0
  ! arr(2)=0+(1)*2^(-5+2) = 2^-3 = 0.125
  ! arr(3)=0+(1)*2^(-5+3) = 2^-2 = 0.25
  ! arr(4)=0+(1)*2^(-5+4) = 2^-1 = 0.5
  ! arr(5)=0+(1)*2^(-5+5) = 2^0  = 1.0
  print *, "powspace(0,1,5,base=2): ", powspace(0.0d0,1.0d0,5,2.0d0)


end program test_sf_arrays
```

## Dependencies and Interactions

- **Internal Dependencies:**
    - The `logspace` function internally calls `linspace` to generate the logarithmic scale after transforming the start/end points.
    - The `upminterval` function internally calls `upmspace`.
- **External Libraries:** This module does not have direct dependencies on external libraries like BLAS or LAPACK for its core functionality.
- **Interactions:** The `SF_ARRAYS` module provides fundamental array generation capabilities. Its functions are likely used by various other modules within the SciFortran library that require structured numerical grids or sequences (e.g., for numerical integration, function interpolation, finite difference methods, etc.).

```
