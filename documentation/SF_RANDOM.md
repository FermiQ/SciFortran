## Overview

The `SF_RANDOM` module in SciFortran provides a comprehensive suite of tools for random number generation (RNG). It offers access to:

-   **Mersenne Twister (MT) Algorithm:** A high-quality pseudorandom number generator with a long period. The module includes routines to initialize the MT generator, draw random numbers from it, and generate deviates from various statistical distributions using MT as the underlying uniform RNG.
-   **Fortran Intrinsic RNG:** Wrappers and extensions for Fortran's intrinsic `RANDOM_NUMBER` subroutine, including initialization routines and functions to generate deviates from several common statistical distributions.
-   **Utility Functions:** Including a routine to generate random permutations of integers.

The module often uses generic interfaces to provide type-specific (e.g., real, complex, integer) and rank-specific (scalars up to 7D/8D arrays) versions of its random number generation routines.

## Key Components

### Module: `SF_RANDOM`
- **Purpose:** Offers a variety of random number generators and distribution functions, based on both Mersenne Twister and Fortran's intrinsic RNG.
- **Key Public Interfaces & Procedures (details grouped by functionality below):**
    - **Mersenne Twister (MT):** `mersenne_init` (or `mt_init`), `mersenne`, `mt_random`, `mt_uniform`, `mt_normal`, `mt_exponential`, `mt_gamma`, `mt_chi_square`, `mt_inverse_gamma`, `mt_weibull`, `mt_cauchy`, `mt_student_t`, `mt_laplace`, `mt_log_normal`, `mt_beta`, `mt_save`, `mt_get`.
    - **Intrinsic RNG Based:** `random_number_init`, `random_number_seed`, `random_normal`, `random_gamma`, `random_chisq`, `random_exponential`, `random_Weibull`, `random_beta`, `random_inv_gauss`, `random_Poisson`, `random_binomial1`, `random_binomial2`, `random_neg_binomial`, `random_von_Mises`, `random_Cauchy`.
    - **Utilities:** `random_order`, `nrand`.

---

### Mersenne Twister (MT) Random Number Generation
(Implementations primarily in `random_mt.f90`, interfaced via `SF_RANDOM`)

#### Initialization
-   **`mersenne_init` (interface to `init_genrand(seed)`) / `mt_init` (alias)**
    -   **Purpose:** Initializes the Mersenne Twister generator with an integer `seed`.
    -   **Inputs:** `seed` (integer, intent(in)).
-   **`sgrnd(seed)` (older init, called by `grnd` if not initialized)**
    -   **Purpose:** Alternative initialization for MT. `init_genrand` is generally preferred.

#### Core MT Generator
-   **`mersenne` (interface to `grnd()`) result(random_val)**
    -   **Purpose:** Returns a single `real(8)` pseudorandom number uniformly distributed in [0, 1).
    -   **Outputs:** `random_val` (real(8)).

#### Array Filling and Distributions using MT
-   **`mt_random`**: Interface. Fills arrays of various ranks (1D to 7D/8D) and types (real `d_grnd_...`, complex `c_grnd_...`) with uniform random numbers from MT.
    -   **Typical Signature:** `CALL mt_random(Array_out)`
-   **`mt_uniform`**: Interface.
    -   `igrnd(l, h) result(val)`: Integer uniform in `[l, h]`.
    -   `dgrnd_uniform(a, b) result(val)`: Real(8) uniform in `[a, b)`.
-   **`mt_normal`**: Interface. Generates normally distributed numbers (mean 0, stddev 1 via `gaussrnd()`) or with specified `mean`, `stdev` via `normalrnd(mean, stdev)`.
-   **Other Distributions (`mt_exponential`, `mt_gamma`, etc.)**: Interfaces providing random deviates from various statistical distributions, all based on the Mersenne Twister generator.
    -   **Typical Inputs:** Parameters of the distribution (e.g., `shape`, `scale`).
    -   **Outputs:** A single random deviate of `real(8)` type.

#### MT State Management
-   **`mt_save`**: Interface. Saves the current state of the Mersenne Twister generator.
    -   `mtsavef(filename, format_char)`: Saves to a named file.
    -   `mtsaveu(unit_number, format_char)`: Saves to an open Fortran unit.
    -   `format_char` ('u' for unformatted, else formatted).
-   **`mt_get`**: Interface. Loads a previously saved state into the Mersenne Twister generator.
    -   `mtgetf(filename, format_char)`: Loads from a named file.
    -   `mtgetu(unit_number, format_char)`: Loads from an open Fortran unit.

---

### Intrinsic Random Number Generation
(Implementations primarily in `random_routines.f90` and `SF_RANDOM.f90`)

#### Initialization
-   **`Subroutine random_number_init(shift)`**:
    -   **Purpose:** Initializes Fortran's intrinsic RNG using `SYSTEM_CLOCK` and `RANDOM_SEED`. An optional integer `shift` can be provided to vary the seed.
-   **`Function random_number_seed(info, file) result(seed_val)`**:
    -   **Purpose:** Generates a seed value, attempting to use `/dev/urandom` (or `/dev/random` if `file=1`) or falling back to `DATE_AND_TIME` if device access fails.
    -   **Inputs:** `info` (integer, optional; if /=0, prints info), `file` (integer, optional; 0 for /dev/urandom, 1 for /dev/random).
    -   **Outputs:** `seed_val` (integer). This can then be used with `RANDOM_SEED(PUT=...)`.

#### Distribution Functions (Intrinsic RNG based)
-   **`Function random_normal() result(fn_val)`**: Returns a `real` normally distributed random number (mean 0, stddev 1) using the ratio of uniforms method.
-   **`Function random_gamma(s, first) result(fn_val)`**: Gamma distribution with shape `s`. `first` (logical) indicates if parameters changed.
-   **`Function random_chisq(ndf, first) result(fn_val)`**: Chi-squared distribution with `ndf` degrees of freedom.
-   **`Function random_exponential() result(fn_val)`**: Exponential distribution (mean 1).
-   **`Function random_Weibull(a) result(fn_val)`**: Weibull distribution with shape `a`.
-   **`Function random_beta(aa, bb, first) result(fn_val)`**: Beta distribution with parameters `aa`, `bb`.
-   **`Function random_inv_gauss(h, b, first) result(fn_val)`**: Generalized Inverse Gaussian distribution.
-   **`Function random_Poisson(mu, first) result(ival)`**: Poisson distribution with mean `mu`. Returns integer.
-   **`Function random_binomial1(n, p, first) result(ival)` / `Function random_binomial2(n, p, first) result(ival)`**: Binomial distribution (n trials, probability p). `random_binomial1` is for fixed n,p.
-   **`Function random_neg_binomial(sk, p) result(ival)`**: Negative binomial distribution.
-   **`Function random_von_Mises(k, first) result(fn_val)`**: Von Mises distribution.
-   **`Function random_Cauchy() result(fn_val)`**: Standard Cauchy distribution.

---

### Utilities

#### `Subroutine random_order(order, n)`
- **Purpose:** Generates a random permutation of integers from 1 to `n`.
- **Inputs:**
    - `n` (integer, intent(in)): The number of integers to permute.
- **Outputs:**
    - `order` (integer array of size `n`, intent(out)): Contains the random permutation.

#### `Function nrand(dseed_) result(val)`
- **Purpose:** A specific pseudorandom number generator (Numerical Recipes `ran1` legacy).
- **Inputs:** `dseed_` (integer, optional): Seed. If <=0, initializes.
- **Outputs:** `val` (real(8)): Random number in [0,1).

## Important Variables/Constants
-   **`defaultsd` (private in `SF_RANDOM`):** Integer parameter, `4357`. Default seed for Mersenne Twister if `sgrnd` is called without a seed (e.g., implicitly by `grnd` if never initialized).
-   Internal MT parameters (`N`, `M`, `mt`, `mti`, etc.) are private.

## Usage Examples

**1. Using Mersenne Twister for uniform random numbers:**
```fortran
program test_mt_random
  use SF_RANDOM
  implicit none
  real(8) :: r_val
  real(8), dimension(5) :: r_array
  integer :: i

  call mt_init(12345) ! Initialize MT with a seed

  r_val = mersenne()  ! Get a single random number
  print *, "Single MT random:", r_val

  call mt_random(r_array) ! Fill an array
  print *, "MT random array:", r_array
end program test_mt_random
```

**2. Using intrinsic RNG for normally distributed numbers:**
```fortran
program test_intrinsic_normal
  use SF_RANDOM
  implicit none
  real :: normal_val
  integer :: i

  call random_number_init() ! Initialize intrinsic RNG

  print *, "Intrinsic Normal Random Numbers:"
  do i = 1, 5
    normal_val = random_normal()
    print *, normal_val
  end do
end program test_intrinsic_normal
```

**3. Generating a random permutation:**
```fortran
program test_random_permutation
  use SF_RANDOM
  implicit none
  integer, parameter :: n_items = 5
  integer, dimension(n_items) :: p_order

  call random_number_init() ! Seed intrinsic generator used by random_order
  call random_order(p_order, n_items)
  print *, "Random permutation of 1 to", n_items, ":", p_order
end program test_random_permutation
```

## Dependencies and Interactions

-   **Intrinsic Fortran RNG**: Routines like `random_normal`, `random_gamma`, etc., rely on Fortran's `RANDOM_NUMBER` intrinsic subroutine. `random_number_init` and `random_number_seed` use `RANDOM_SEED`, `SYSTEM_CLOCK`, and potentially `/dev/urandom`.
-   **Included Files**:
    -   `random_mt.f90`: Contains the Mersenne Twister implementation (`init_genrand`, `grnd`, array fillers, and MT-based distributions).
    -   `random_routines.f90`: Contains implementations for various statistical distributions based on the intrinsic RNG.
-   **`SF_ARRAYS`, `SF_INTEGRATE`, `SF_IOTOOLS`, `SF_LINALG`**: While the `SF_RANDOM` module itself does not directly depend on these, the associated `SF_STAT` module (often found in the same directory and used for statistical analysis of random data) does.
-   **Interactions**: This module is crucial for simulations, statistical analysis, Monte Carlo methods, and any application requiring pseudorandom numbers or sampling from various distributions.

```
