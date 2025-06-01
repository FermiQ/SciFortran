## Overview

The `SF_CONSTANTS` module is a cornerstone of the SciFortran library, providing a comprehensive collection of mathematical and physical constants. It also includes several utility subroutines and functions for common tasks such as timestamping, custom error handling, checking for infinity or NaN values, and pausing execution. All constants are defined with `real(8)` (double precision) or `complex(8)` where appropriate.

## Key Components

### Module: `SF_CONSTANTS`
- **Purpose:** Provides a wide range of predefined mathematical and physical constants, along with utility functions and subroutines.
- **Contains:**
    - Mathematical constants (e.g., `pi`, `euler`, `zero`, `xi`).
    - Precision kind parameters (e.g., `sp`, `dp`, `ddp`).
    - A vast array of physical constants (e.g., `speed_of_light_in_vacuum`, `Planck_constant`, `Avogadro_constant`).
    - Utility functions: `isinfty` (generic interface for `i_isinfty`, `d_isinfty`, `z_isinfty`), `isnan` (generic interface for `i_isnan`, `d_isnan`, `z_isnan`).
    - Utility subroutines: `timestamp`, `print_date` (internal), `stop_error`, `wait` (generic interface for `i_wait`, `r_wait`, `d_wait`).

### Generic Interface: `isinfty`
- **Purpose:** Tests if a given integer, real(8), or complex(8) number is infinite.
- **Functions:**
    - `i_isinfty(a)`: `a` is integer.
    - `d_isinfty(a)`: `a` is real(8).
    - `z_isinfty(a)`: `a` is complex(8).
- **Inputs:**
    - `a` (integer/real(8)/complex(8), intent(in)): The number to evaluate.
- **Outputs:**
    - `bool` (logical): `.true.` if `a` is infinite, `.false.` otherwise. (Note: Implemented by checking `a-1 == a`).

### Generic Interface: `isnan`
- **Purpose:** Tests if a given integer, real(8), or complex(8) number is NaN (Not a Number).
- **Functions:**
    - `i_isnan(a)`: `a` is integer.
    - `d_isnan(a)`: `a` is real(8).
    - `z_isnan(a)`: `a` is complex(8).
- **Inputs:**
    - `a` (integer/real(8)/complex(8), intent(in)): The number to evaluate.
- **Outputs:**
    - `bool` (logical): `.true.` if `a` is NaN, `.false.` otherwise. (Note: Implemented by checking `a /= a .OR. a-1 == a`).

### Subroutine: `timestamp`
- **Signature:** `Subroutine timestamp(unit)`
- **Purpose:** Prints the current date and time to the specified output `unit` (default is standard output). The format is `Timestamp: [day] [MonthName] [year] [hh]:[mm]:[ss].[mss]`.
- **Inputs:**
    - `unit` (integer, optional): The output unit number (e.g., 6 for console).

### Subroutine: `stop_error`
- **Signature:** `Subroutine stop_error(msg)`
- **Purpose:** Prints a given error message `msg` to the standard error unit (0) and then terminates program execution with a non-zero exit code (specifically, `stop 1`). This is preferred over a simple `STOP "msg"` if a non-zero exit status is desired.
- **Inputs:**
    - `msg` (character, intent(in)): The error message to display.

### Generic Interface: `wait`
- **Purpose:** Pauses program execution for a specified duration. The duration is given in milliseconds. This is implemented using a busy-wait loop checking `date_and_time`.
- **Subroutines:**
    - `i_wait(time)`: `time` is integer.
    - `r_wait(time)`: `time` is real.
    - `d_wait(time)`: `time` is real(8).
- **Inputs:**
    - `time` (integer/real/real(8), intent(in)): The duration to wait, in milliseconds.

## Important Variables/Constants

This module defines a large number of `parameter` constants. They are all `public`.

**Precision Kinds:**
- `sp` (integer): Single precision kind value.
- `dp` or `dbl` (integer): Double precision kind value (typically 8).
- `ddp` (integer): Quadruple precision kind value (typically 16).

**Selected Mathematical Constants (all `real(8)` or `complex(8)`):**
- `pi`: The mathematical constant :math:`\pi`.
- `pi2`: :math:`2\pi`.
- `euler`: Euler's number :math:`e`.
- `gamma_euler`: Euler-Mascheroni constant :math:`\gamma`.
- `sqrt2`, `sqrt3`, `sqrt6`: Square roots of 2, 3, and 6.
- `zero`: Complex :math:`(0.0, 0.0)`.
- `one`: Complex :math:`(1.0, 0.0)`.
- `xi`: Complex :math:`(0.0, 1.0)` (imaginary unit).
- `max_int` (integer): Largest representable integer.
- `max_real` (real(8)): Largest representable double precision real.
- `epsilonr` (real(8)): Smallest positive number such that `1.0 + epsilonr /= 1.0`.

**Selected Physical Constants (all `real(8)`, in SI units unless specified):**
- `speed_of_light_in_vacuum`: :math:`c` [m/s]
- `Planck_constant`: :math:`h` [J·s]
- `Planck_constant_over_2_pi` (reduced Planck constant): :math:`\hbar` [J·s]
- `Avogadro_constant`: :math:`N_A` [mol<sup>-1</sup>]
- `Boltzmann_constant`: :math:`k_B` [J·K<sup>-1</sup>]
- `elementary_charge`: :math:`e` [C]
- `electron_mass`: :math:`m_e` [kg]
- `Bohr_radius`: :math:`a_0` [m]
- `Rydberg_constant`: :math:`R_\infty` [m<sup>-1</sup>]
- `fine_structure_constant`: :math:`\alpha` (dimensionless)
- `electric_constant` (vacuum permittivity): :math:`\epsilon_0` [F·m<sup>-1</sup>]
- `Newtonian_constant_of_gravitation`: :math:`G` [m<sup>3</sup>·kg<sup>-1</sup>·s<sup>-2</sup>]
- ... and many others, including versions of constants in different units (eV, MeV, etc.).

## Usage Examples

```fortran
program test_sf_constants
  use SF_CONSTANTS
  implicit none
  real(8) :: circumference, energy
  real(8) :: radius
  logical :: check

  radius = 1.0_dp ! Use double precision kind from the module

  circumference = pi2 * radius ! Using pi2 (2*pi)
  print *, "Circumference of unit circle:", circumference

  energy = Rydberg_constant_times_hc_in_eV
  print *, "Rydberg energy (eV):", energy

  call timestamp() ! Print current timestamp to console

  check = d_isnan(0.0_dp / 0.0_dp) ! Check for NaN
  if (check) then
    print *, "0.0/0.0 is NaN"
  end if

  check = d_isinfty(max_real * 2.0_dp) ! Check for infinity
  if (check) then
    print *, "max_real * 2 is Inf"
  end if

  print *, "Waiting for 0.5 seconds..."
  call wait(500.0_dp) ! Wait for 500 milliseconds
  print *, "Done waiting."

  ! Example of stopping execution with an error message
  ! call stop_error("This is a test error message.")
  ! print *, "This line will not be reached if stop_error is called."

end program test_sf_constants
```

## Dependencies and Interactions

- **Intrinsic Modules:** The module uses `implicit none`. The `timestamp` and `wait` routines rely on the standard intrinsic `date_and_time`. The `isnan` and `isinfty` functions use custom logic rather than relying on `ieee_arithmetic` directly in their implementation, though `ieee_arithmetic` might be used by the compiler for the operations involved.
- **External Libraries:** None.
- **Interactions:**
    - The constants and precision kinds defined are intended for widespread use across scientific applications and other SciFortran modules.
    - Utility functions like `timestamp`, `stop_error`, `isinfty`, `isnan`, and `wait` provide general-purpose functionalities.

```
