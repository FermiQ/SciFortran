## Overview

The `SF_PARSE_INPUT` module in SciFortran provides a robust mechanism for parsing input parameters for applications. It allows programs to read configuration variables from a specified input file and supports overriding these values with command-line arguments. The module handles various data types, including scalars (integer, real, logical, character) and 1D arrays/vectors of these types.

A key feature is its ability to maintain a list of all input parameters processed, along with their values and optional comments. This list can then be saved to a file (e.g., `used_parameters.dat`), providing a record of the exact inputs used for a particular program run.

## Key Components

### Module: `SF_PARSE_INPUT`
- **Purpose:** Facilitates reading and managing input parameters from files and command-line arguments.
- **Uses Modules:** `LIST_INPUT` (for managing a linked list of parsed parameters).
- **Key Public Interfaces:**
    - `parse_input_variable`: Primary interface for reading a variable. It first attempts to find the variable in the specified input file. If not found, it uses a provided default value. Finally, it checks command-line arguments for any overrides.
    - `parse_cmd_variable`: Interface for specifically reading a variable from command-line arguments only.
    - `save_input`: Interface to `save_input_file`.
    - `print_input`: Interface to `print_input_list` (from `LIST_INPUT`) for printing the current list of parsed parameters, typically to the console.
- **Key Public Procedures:**
    - `save_input_file(filename)`: Saves all parsed input variables (name, value, comment) to the specified `filename`.
    - `delete_input`: Alias for `delete_input_list` from `LIST_INPUT`, clears the stored list of parsed parameters.

---

### Main Parsing Interfaces

#### Interface: `parse_input_variable`
- **Purpose:** Reads a variable's value. The process is:
    1. Initialize `variable` with `default` if provided.
    2. Attempt to read the variable `name` from the specified `file`.
    3. Attempt to override the value with a command-line argument matching `name`.
    4. Stores the final variable name, value, and optional `comment` into an internal list for later saving.
- **Specific Subroutines (selected, others follow similar patterns):**
    - `i_parse_input(variable, name, file, default, comment)`: For an integer scalar.
    - `d_parse_input(variable, name, file, default, comment)`: For a real(8) scalar.
    - `l_parse_input(variable, name, file, default, comment)`: For a logical scalar.
    - `ch_parse_input(variable, name, file, default, comment)`: For a character string.
    - `iv_parse_input(variable_vec, name, file, default_vec, comment)`: For a 1D integer array.
    - `dv_parse_input(variable_vec, name, file, default_vec, comment)`: For a 1D real(8) array.
    - `lv_parse_input(variable_vec, name, file, default_vec, comment)`: For a 1D logical array.
- **Inputs:**
    - `variable` (various types, scalar or 1D array, intent(out)): The Fortran variable to be set. For arrays, it must be pre-allocated to the expected size.
    - `name` (character): The name of the variable as it appears in the input file or command line (case-insensitive).
    - `file` (character): Path to the input file.
    - `default` (same type as `variable`, optional): Default value if not found in file or command line. For arrays, this is a default array.
    - `comment` (character, optional): A description for this variable, saved if `save_input_file` is called.
- **File Format Expected:**
    - Lines like `VARIABLE_NAME = VALUE # Optional comment`
    - For vectors/arrays: `VECTOR_NAME = val1,val2,val3`
- **Command-Line Format Expected:**
    - Arguments like `VARIABLE_NAME=VALUE` or `VECTOR_NAME=val1,val2,val3`.

#### Interface: `parse_cmd_variable`
- **Purpose:** Reads a variable's value *only* from command-line arguments. If not found, the `variable` retains its value (which should be pre-set to a default if desired).
- **Specific Subroutines:** Similar to `parse_input_variable` (e.g., `i_parse_cmd_variable`, `dv_parse_cmd_variable`), but without the `file` and `comment` arguments.
- **Inputs:**
    - `variable` (various types, scalar or 1D array, intent(inout)): Pre-set with a default, then updated if found on command line.
    - `name` (character): Name to look for on command line.
    - `default` (various types, optional, intent(in)): This is misleadingly named in the source; it's used to pre-set `variable` *before* command-line parsing if provided to the `_parse_cmd_variable` routine itself, not as a fallback if the cmd var is missing. It's better to initialize `variable` before calling.

---

### Other Public Procedures and Utilities

-   **`save_input_file(filename)` / `save_input` (interface to `save_input_file`)**:
    -   **Purpose:** Writes the currently stored list of all parsed variables, their final values, and their comments to the specified `filename`.
    -   **Inputs:** `filename` (character).
-   **`print_input` (interface to `LIST_INPUT%print_input_list`)**:
    -   **Purpose:** Prints the list of stored input variables to standard output or an optional file unit.
-   **`delete_input` (alias for `LIST_INPUT%delete_input_list`)**:
    -   **Purpose:** Clears the internal list of stored parameters. Call `init_input_list()` (from `LIST_INPUT`, usually handled internally) before parsing new inputs if needed after deletion.
-   **String Utilities (from `SF_PARSE_INPUT` directly, also in `IOFILE`):**
    -   `upper_case(string)`, `lower_case(string)`: Convert string case.
    -   `ch_cap(char)`, `ch_low(char)`: Convert single character case.
    -   `s_blank_delete(string)`: Removes all blanks and TABs from a string, left-justifying.
-   **File/System Utilities (from `SF_PARSE_INPUT` directly, also in `IOFILE`):**
    -   `free_unit()`: Function, returns an unused Fortran I/O unit number.
-   **Internal Helper Functions (listed by generation script, but likely not for direct user calls):** `scan_comment`, `scan_cmd_variable`, `scan_input_variable`, `check_cmd_vector_size`.

## Important Variables/Constants

-   The module uses an internal, private instance of `type(input_list)` (from `LIST_INPUT` module) named `default_list` to store all parsed parameters. Users interact with this list via the provided subroutines.

## Usage Examples

**Sample Input File (`my_params.dat`):**
```
# Simulation Parameters
MAX_ITER      = 1000       ! Maximum iterations
TOLERANCE     = 1.0e-6     ! Convergence tolerance
GRID_POINTS   = 10,20,30   ! Number of points in X,Y,Z
ENABLE_FEATURE = .TRUE.    ! Enable a feature
SIM_LABEL     = "Run_01"   ! Label for this simulation
```

**Fortran Code:**
```fortran
program test_sf_parse_input
  use SF_PARSE_INPUT
  implicit none

  integer :: max_iterations
  real(8) :: tolerance
  integer, dimension(3) :: grid_dims
  logical :: feature_enabled
  character(len=50) :: simulation_label

  ! Initialize LIST_INPUT (usually done automatically on first parse call if needed,
  ! but explicit init can be good practice if reusing module in complex ways)
  ! call init_input_list() ! Not strictly needed if SF_PARSE_INPUT handles it.

  ! Parse variables from file, with defaults, and check command line
  call parse_input_variable(max_iterations, name="MAX_ITER", file="my_params.dat", default=500, &
                         & comment="Maximum number of iterations")
  call parse_input_variable(tolerance, name="TOLERANCE", file="my_params.dat", default=1.0d-5)
  call parse_input_variable(grid_dims, name="GRID_POINTS", file="my_params.dat", &
                         & default=[16,16,16], comment="Grid dimensions (X,Y,Z)")
  call parse_input_variable(feature_enabled, name="ENABLE_FEATURE", file="my_params.dat", &
                         & default=.false.)
  call parse_input_variable(simulation_label, name="SIM_LABEL", file="my_params.dat", &
                         & default="DefaultRun", comment="Simulation identifier")

  ! An example of parsing a variable only from command line
  ! real(8) :: cmd_only_param
  ! cmd_only_param = 0.0 ! Set a Fortran default
  ! call parse_cmd_variable(cmd_only_param, name="CMD_PARAM", default=0.001d0) ! default here is for the list entry

  print *, "--- Parsed Values ---"
  print *, "Max Iterations: ", max_iterations
  print *, "Tolerance:      ", tolerance
  print *, "Grid Dims:      ", grid_dims
  print *, "Feature On:     ", feature_enabled
  print *, "Sim Label:      ", trim(simulation_label)
  ! print *, "Cmd Only Param: ", cmd_only_param
  print *, "---------------------"

  ! Save the used parameters to a file
  call save_input_file("used_params.dat")
  print *, "Used parameters saved to used_params.dat"

  ! Clean up the list if done
  call delete_input()

end program test_sf_parse_input
```
**Command-line execution example (to override file/default):**
`./my_program MAX_ITER=2000 ENABLE_FEATURE=F`

## Dependencies and Interactions

-   **`LIST_INPUT` Module**: This is a critical dependency. `SF_PARSE_INPUT` uses `LIST_INPUT` to create, manage, and store a linked list of the input variables that are parsed. Routines like `append_to_input_list`, `print_input_list`, and `delete_input_list` are from this module.
-   **Fortran Intrinsics**: Uses `command_argument_count()` and `get_command_argument()` for parsing command-line arguments.
-   **Interactions**: Designed as a primary configuration tool for applications, typically used at the beginning of program execution. The `save_input_file` routine is useful for logging and reproducibility.

```
