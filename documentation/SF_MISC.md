## Overview

The `SF_MISC` module in SciFortran provides a collection of miscellaneous utility routines for various common tasks. These include:

-   **Array Shape Assertions:** Verifying that arrays conform to expected dimensions.
-   **Sorting Algorithms:** Several methods for sorting 1D arrays of integers or real numbers, often returning an index map of the sort.
-   **Array Element Uniqueness:** Identifying and extracting unique elements from arrays.
-   **Array Reshuffling:** Reordering array elements based on a provided index map.
-   **Numerical Utilities:** Finding elements in an array (e.g., nearest value less than a target) and performing merge-sort inverse ranking.

The module often groups specific implementations (e.g., for integer or real data) under generic interfaces.

## Key Components

### Module: `SF_MISC`
- **Purpose:** Provides a collection of utility functions for array manipulation, sorting, and other sundry tasks.
- **Key Public Interfaces (details below):**
    - `assert_shape`: Verifies array dimensions.
    - `sort`, `sort_array`, `sort_quicksort`, `sort_insertion`, `sort_qsort`: Various sorting algorithms.
    - `uniq_array`, `uniq`: Routines for finding unique elements.
    - `reorder_array`, `reorder`: For reordering array elements.
    - `uniinv`: Merge-sort inverse ranking with duplicate removal.
    - `unista`: Stable unique element extraction.
    - `nearless`: Finds nearest value in an array less than a target (Note: implementation seems to be missing in the provided source for `SF_MISC.f90` itself, though the interface is defined).

---

### Array Shape Assertions

#### Interface: `assert_shape`
- **Purpose:** Asserts that an input array `A` matches a specified shape `Ndim`. If not, it prints an error message including the calling `routine` and `matname` (if provided) and stops execution.
- **Specific Subroutines:**
    - `i_assert_shape_N<R>(A, Ndim, routine, matname)` for integer arrays of rank `<R>` (1 to 7/8).
    - `d_assert_shape_N<R>(A, Ndim, routine, matname)` for real(8) arrays of rank `<R>`.
    - `z_assert_shape_N<R>(A, Ndim, routine, matname)` for complex(8) arrays of rank `<R>`.
- **Inputs:**
    - `A` (integer/real(8)/complex(8) array, intent(in)): The array whose shape is to be checked.
    - `Ndim` (integer array, intent(in)): The expected shape vector (e.g., `[3, 4]` for a 3x4 matrix).
    - `routine` (character, optional): Name of the calling routine for error messages.
    - `matname` (character, optional): Name of the matrix/array for error messages.

---

### Sorting Algorithms

#### Interface: `sort_insertion`
- **Purpose:** Sorts a 1D array using the insertion sort algorithm (scales as N<sup>2</sup>, suitable for small arrays). Also returns the original indices.
- **Specific Subroutines:**
    - `sort_insertion_i(a, indx_a)`: For integer arrays.
    - `sort_insertion_d(a, indx_a)`: For real(8) arrays.
- **Inputs:**
    - `a` (integer/real(8) array, intent(inout)): Array to be sorted (modified in place).
- **Outputs:**
    - `a` (integer/real(8) array, intent(inout)): The sorted array.
    - `indx_a` (integer array, intent(inout)): Permutation indices such that `a_sorted(i) = a_original(indx_a(i))`.

#### Interface: `sort_quicksort` (also aliased as `sort`, `sort_array`, `sort_qsort`)
- **Purpose:** Sorts a 1D array using a quicksort algorithm. Optionally returns original indices.
- **Specific Subroutines:**
    - `sort_quicksort_i(a, indx)`: For integer arrays. Contains recursive `quicksort_i`.
    - `sort_quicksort_d(a, indx)`: For real(8) arrays. Contains recursive `quicksort_d`.
    - `sort_array_i(a, indx_a)` / `sort_array_d(a, indx_a)`: Another variant that applies indices after sorting.
- **Inputs:**
    - `a` (integer/real(8) array, intent(inout)): Array to be sorted.
- **Outputs (Optional for some variants, mandatory for others):**
    - `a` (integer/real(8) array, intent(inout)): The sorted array.
    - `indx` / `indx_a` (integer array, intent(inout) or intent(out)): Permutation indices.

---

### Array Element Uniqueness and Reshuffling

#### Interface: `uniq_array` (Subroutine) / `uniq` (Function)
- **Purpose:** Finds unique elements in a 1D array.
- **`uniq_array` Specific Subroutines:**
    - `i_uniq(AIN, AOUT, MASK)`: Integer arrays.
    - `d_uniq(AIN, AOUT, MASK)`: Real(8) arrays.
- **`uniq` Specific Functions:**
    - `f_i_uniq(AIN, MASK) result(AOUT)`: Integer arrays.
    - `f_d_uniq(AIN, MASK) result(AOUT)`: Real(8) arrays.
- **Inputs:**
    - `AIN` (integer/real(8) array, intent(inout) for subroutines, intent(in) for functions): Input array. For subroutines, it's modified to contain unique elements at the beginning.
- **Outputs:**
    - `AOUT` (allocatable array): Array containing only the unique elements from `AIN`.
    - `MASK` (logical array, optional, allocatable, intent(out)): Mask indicating positions of unique elements in the original sorted `AIN`.
    - For subroutines, `AIN` is modified, and `NDIM` (number of unique elements) is effectively the size of `AOUT`.

#### Interface: `reorder_array` (Subroutine) / `reorder` (Function)
- **Purpose:** Reshuffles elements of an array `Ain` according to an `Index` array. `Ain(i)` becomes `Aout(Index(i))`.
- **Specific Procedures:** `I_reshuffle`, `D_reshuffle`, `Z_reshuffle`, `L_reshuffle` (for Integer, Real(8), Complex(8), Logical types). Function versions are `f_I_reshuffle`, etc.
- **Inputs:**
    - `Ain` (array of any supported type): Input array.
    - `Index` (integer array, same size as `Ain`): Array of new positions for elements.
- **Outputs:**
    - For subroutines, `Ain` (intent(inout)) is modified in place.
    - For functions, `Aout` (array of same type and size as `Ain`): The reshuffled array.

#### Interface: `uniinv`
- **Purpose:** Performs merge-sort inverse ranking of an array, removing duplicate entries. The output `igoest(i)` is the rank of `xdont(i)` in the unique sorted version of `xdont`.
- **Specific Subroutines:** `d_uniinv`, `r_uniinv`, `i_uniinv` (for real(8), real, integer).
- **Inputs:**
    - `xdont` (array, intent(in)): Input array.
- **Outputs:**
    - `igoest` (integer array, intent(out)): Inverse ranking.

#### Interface: `unista`
- **Purpose:** (Stable Unique) Removes duplicates from an array, keeping unique entries in the order of their first appearance. The input array `xdont` is modified to contain the unique elements at the beginning, and `nuni` returns their count.
- **Specific Subroutines:** `d_unista`, `r_unista`, `i_unista`.
- **Inputs:**
    - `xdont` (array, intent(inout)): Input array, modified in place.
- **Outputs:**
    - `xdont`: Contains unique elements in original order at `xdont(1:nuni)`.
    - `nuni` (integer, intent(out)): Number of unique elements.
    - `mask` (logical array, optional, intent(out)): True for elements that are first occurrences.

## Important Variables/Constants
This module defines a private constant `pi`. No public constants are exposed for direct use.

## Usage Examples

**1. Sorting a real array and getting indices:**
```fortran
program test_sf_misc_sort
  use SF_MISC
  implicit none
  real(8), dimension(5) :: my_array = [50.0, 10.0, 30.0, 20.0, 40.0]
  integer, dimension(5) :: original_indices

  call sort(my_array, original_indices) ! Uses sort_quicksort_d by default for reals

  print *, "Sorted array:", my_array
  print *, "Original indices:", original_indices
  ! Expected: Sorted array:   10.0  20.0  30.0  40.0  50.0
  ! Expected: Original indices: 2     4     3     5     1 (or similar, if sort is stable)
end program test_sf_misc_sort
```

**2. Finding unique elements:**
```fortran
program test_sf_misc_uniq
  use SF_MISC
  implicit none
  integer, dimension(7) :: data_in = [10, 20, 10, 30, 20, 20, 40]
  integer, allocatable :: data_out(:)
  logical, allocatable :: mask_uniq(:)

  data_out = uniq(data_in, mask=mask_uniq) ! Using the function interface

  print *, "Original data:", data_in
  print *, "Unique sorted data:", data_out
  print *, "Mask of first occurrences (after sort):", mask_uniq

  ! Example with unista (stable unique)
  call unista(data_in, size(data_out), mask_uniq) ! data_in is modified
  print *, "Unique elements (stable order):", data_in(1:size(data_out))
  print *, "Mask (stable): ", mask_uniq
end program test_sf_misc_uniq
```

## Dependencies and Interactions

-   **Intrinsic Modules**: Uses `random_number` for pivot selection in some quicksort implementations.
-   **External Libraries**: None.
-   **Interactions**: This module provides general-purpose utility functions. The sorting routines are fundamental. Array shape assertions can be useful for debugging and ensuring correctness in more complex numerical codes. Unique element finders and reshuffling routines are common pre/post-processing steps in data analysis.

```
