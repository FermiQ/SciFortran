## Overview

The `SF_IOTOOLS` module is SciFortran's primary toolkit for input/output operations and related utilities. It serves as a unified interface to a range of functionalities, including:

-   **Plotting Assistance:** Generating script files for `gnuplot` to create 1D (`splot`) and 2D/3D (`splot3d`) visualizations of array data.
-   **Data Persistence:** Saving and reading Fortran arrays of various ranks (up to 7D) and types (real and complex) to/from files, with options for data compression.
-   **File System Operations:** Creating directories, getting file information (size, length, path components), and managing file compression/decompression (gzip, bzip2, xz, tar archives) via system calls.
-   **String Manipulation:** Converting numerical and logical types to strings, case conversion, and filename regularization.
-   **Fortran Unit Management:** Finding and freeing available Fortran I/O units.
-   **Matrix Printing:** Simple routines to print matrices to the console or a file.

Functionality is often organized into sub-modules (`IOFILE`, `IOPLOT`, `IOREAD`) and then exposed through `SF_IOTOOLS`.

## Key Components

### Module: `SF_IOTOOLS`
- **Purpose:** Provides a comprehensive set of routines for data input/output, plotting assistance, file management, and string utilities.
- **Uses Modules:** `IOFILE`, `IOPLOT`, `IOREAD`.
- **Key Public Interfaces & Procedures (details grouped by source module below):**
    - From `IOPLOT`: `splot`, `splot3d` (interfaces for plotting), `save_array` (interface for saving arrays).
    - From `IOREAD`: `sread`, `read_array` (interfaces for reading arrays).
    - From `IOFILE`: `set_store_size`, `str` (interface for type to string conversion), `txtfy` (obsolete alias for `str`), `reg` (filename regularization), `to_lower`, `to_upper` (case conversion), `file_size`, `file_length`, `file_info`, `file_gzip`, `file_gunzip`, `file_bzip`, `file_bunzip`, `file_xz`, `file_unxz`, `file_targz`, `file_untargz`, `newunit` (interface, actually `free_unit`), `free_unit`, `free_units`, `create_dir` (interface), `get_filename`, `get_filepath`, `print_matrix` (interface).

---

### Plotting Assistance (from `IOPLOT` module)

These routines generate data files and corresponding `.gp` gnuplot script files.

#### Interface: `splot`
- **Purpose:** Generates a data file and a gnuplot script for 1D plots. Supports real (RR) and complex (RC) data arrays of rank 1 to 7. For complex data, real and imaginary parts are typically plotted against the x-axis.
- **Typical Signature:** `splotA<N>_<TYPE>(pname, X, Y1, append)` where `<N>` is rank (1-7), `<TYPE>` is `RR` or `RC`.
- **Inputs:**
    - `pname` (character): Base name for the output data and `.gp` files.
    - `X` (real(8) array): X-axis data (typically the last dimension of `Y1`).
    - `Y1` (real(8) or complex(8) array, rank 1 to 7): Y-axis data.
    - `append` (logical, optional): If true, appends to existing data file (for multiple plots).
- **Outputs:** Creates `pname` (data file) and `pname.gp` (gnuplot script).

#### Interface: `splot3d`
- **Purpose:** Generates a data file and gnuplot scripts for 2D surface plots (`_surface.gp`) and 2D map plots (`_map.gp`). Supports real (`d_splot3d`) and complex (`c_splot3d`) 2D input arrays. Animated versions also exist.
- **Typical Signature:** `d_splot3d(pname, X1, X2, Y, ...)`
- **Inputs:**
    - `pname` (character): Base name for output files.
    - `X1`, `X2` (real(8) arrays): Grid coordinates for X and Y axes.
    - `Y` (2D real(8)/complex(8) array or 3D for animation): Z-axis data (function values).
    - Optional arguments for ranges (`xmin`, `xmax`, etc.), line plotting.
- **Outputs:** Creates data file(s) and `.gp` script(s).

---

### Data Persistence (from `IOPLOT` and `IOREAD` modules)

#### Interface: `save_array`
- **Purpose:** Saves arrays of rank 0 (scalar) to 7 to a file. Data is typically compressed using bzip2 after saving.
- **Typical Signature:** `data_saveA<N>_<TYPE>(pname, Y1, order, wspace)`
- **Inputs:**
    - `pname` (character): Output filename.
    - `Y1` (real(8) or complex(8) array, rank 0-7): Array to save.
    - `order` (character, optional): "R" for Row-major (Fortran default like), "C" for Column-major style output iteration (affects element order in file).
    - `wspace` (logical, optional): If true (default), adds newlines between higher-dimension slices for some array ranks.
- **Outputs:** Creates a file `pname` (then typically `pname.bz2`).

#### Interface: `read_array`
- **Purpose:** Reads arrays of rank 0 to 7 from a file, typically after decompressing it.
- **Typical Signature:** `data_readA<N>_<TYPE>(pname, Y1, order, wspace)`
- **Inputs:**
    - `pname` (character): Input filename.
    - `Y1` (real(8) or complex(8) array, rank 0-7, intent(out)): Array to fill with data. Must be allocated to correct size before calling.
    - `order`, `wspace` (optional): Should generally match options used during saving.
- **Process:** Automatically attempts to decompress `.bz2` (or `.gz`, `.xz`) if the base `pname` is not found.

#### Interface: `sread`
- **Purpose:** Reads columnar data, typically where the first column is an X-coordinate and subsequent columns are Y data. Primarily for data created by `splot`.
- **Typical Signature:** `sreadA<N>_<TYPE>(pname, X, Y1)`
- **Inputs:**
    - `pname` (character): Input filename.
    - `X` (real(8) array, intent(out)): X-axis data read from the first column.
    - `Y1` (real(8)/complex(8) array, intent(out)): Y-axis data. For complex, expects two columns (imaginary then real).
- **Process:** Handles file decompression.

---

### File and String Utilities (from `IOFILE` module)

-   **`set_store_size(size)`**: Subroutine. Sets a threshold `size` (in Kb). Files larger than this will be automatically compressed by routines like `file_gzip`. Default is 2048 Kb.
-   **`str(variable)`**: Interface. Converts integer, real, complex, logical, or character variables to a string.
    - `str_r_to_ch(r8, d, lead)`: Real to string with `d` decimal places and `lead` leading characters for sign/integer part.
-   **`reg(filename)`**: Function. Returns a regularized filename (trimmed, adjusted left).
-   **`to_lower(StrIn)` / `to_upper(StrIn)`**: Functions. Convert string case.
-   **`file_size(file, printf)`**: Function. Returns file size in Kb. Optionally prints it.
-   **`file_length(file, verbose, incl_comments)`**: Function. Counts lines in a text file, optionally skipping comments (`#`) and blank lines.
-   **`file_info(file)`**: Function (returns integer status). Prints detailed file status information using `fstat`.
-   **File Compression/Decompression:**
    -   `file_gzip(file, size_threshold)`, `file_gunzip(filename_no_gz_ext)`
    -   `file_bzip(file, size_threshold)`, `file_bunzip(filename_no_bz2_ext)`
    -   `file_xz(file, size_threshold)`, `file_unxz(filename_no_xz_ext)`
    -   `file_targz(tarball_name, pattern_to_tar)`, `file_untargz(tarball_name_no_ext)`
    -   `file_tarbz2(...)`, `file_untarbz2(...)`
    - These use system calls (`gzip`, `bzip2`, `xz`, `tar`).
-   **Fortran Unit Management:**
    -   `newunit()` or `free_unit()`: Function. Returns an unused Fortran unit number (typically >100).
    -   `free_units(n)`: Function. Returns an array of `n` unused unit numbers.
-   **`create_dir(dir_name)`**: Interface to `create_data_dir`. Creates a directory using `mkdir -v`.
-   **`get_filename(filepath)` / `get_filepath(filepath)`**: Functions. Extract filename or path from a full filepath string.
-   **`print_matrix`**: Interface. Prints 2D real (`print_array_d`) or complex (`print_array_c`) matrices to console or file.

## Important Variables/Constants

-   **`store_size` (private in `IOFILE`, settable via `set_store_size`):** Integer. Threshold in Kb. Files larger than this are compressed by routines like `file_gzip`. Default: 2048 Kb.

## Usage Examples

**1. Saving and Reading a 1D Array:**
```fortran
program test_save_read_array
  use SF_IOTOOLS
  implicit none
  real(8), dimension(10) :: data_out, data_in
  integer :: i

  data_out = [(real(i)**2, i=1,10)]
  call save_array("my_data.dat", data_out) ! Will be saved as my_data.dat.bz2

  ! ... later ...
  call read_array("my_data.dat", data_in) ! Will read my_data.dat.bz2
  print *, "Read data:", data_in
end program test_save_read_array
```

**2. Generating a Gnuplot script for a simple plot:**
```fortran
program test_splot_example
  use SF_IOTOOLS
  use SF_ARRAYS, only: linspace
  use SF_CONSTANTS, only: pi
  implicit none
  real(8), dimension(100) :: x, y

  x = linspace(0.0d0, 2.0d0*pi, 100)
  y = sin(x)

  call splot("sin_x_plot", x, y)
  ! This creates sin_x_plot (data) and sin_x_plot.gp (gnuplot script)
  ! You can then run: gnuplot sin_x_plot.gp
  print *, "Generated sin_x_plot and sin_x_plot.gp"
end program test_splot_example
```

**3. String conversion and file info:**
```fortran
program test_io_utils
  use SF_IOTOOLS
  implicit none
  integer :: val_i = 123
  real(8) :: val_r = 456.789
  character(len=50) :: str_i, str_r
  integer :: fsize

  str_i = str(val_i)
  str_r = str(val_r, d=2, lead=4) ! str_r = str(val_r, digits=2, leading_chars_for_integer_part=4)
  print *, "Integer as string: '", trim(str_i), "'"
  print *, "Real as string:    '", trim(str_r), "'"

  ! Create a dummy file to check its size
  open(unit=10, file="dummy.txt", status="replace")
  write(10,*) "Hello world"
  close(10)
  fsize = file_size("dummy.txt", printf=.true.)
  ! call file_gzip("dummy.txt") ! This would compress it
end program test_io_utils
```

## Dependencies and Interactions

-   **`IOFILE`, `IOPLOT`, `IOREAD`**: The `SF_IOTOOLS` module is a facade that uses these modules for its core functionality. These modules contain the implementations for file operations, plotting helpers, and data reading/saving respectively.
-   **System Commands**: Several file operations (compression, tar, mkdir) rely on external system commands being available in the environment PATH (e.g., `gzip`, `bzip2`, `xz`, `tar`, `mkdir`).
-   **Gnuplot**: The `splot` and `splot3d` routines generate script files intended for use with the external `gnuplot` program.
-   **`SF_ARRAYS`, `SF_CONSTANTS`**: Used in examples, and potentially by some internal logic (e.g., `linspace` might be used if array generation is needed for plotting axes, though `ioplot_*.f90` files might use their own).

This module is essential for managing data, generating simple plots via gnuplot, and interacting with the file system within SciFortran applications.

```
