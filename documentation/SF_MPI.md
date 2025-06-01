## Overview

The `SF_MPI` module provides a user-friendly interface to Message Passing Interface (MPI) functionalities within the SciFortran library. It aims to simplify common MPI operations for parallel programming. Key capabilities include:

-   **MPI Environment Management:** Initialization, finalization, and basic queries (rank, size).
-   **Synchronization:** Barrier operations.
-   **Collective Communication:**
    -   Broadcasting data (`Bcast_MPI`) from one process to all others.
    -   Gathering data from all processes to all processes (`AllGather_MPI`).
    -   Performing reductions across all processes (`AllReduce_MPI`, typically sum).
    These operations are supported for Boolean, Integer, Real(8), and Complex(8) data types, and for scalars up to multi-dimensional arrays (rank 0 to 7/8).
-   **Utility Functions:** Error handling, CPU timing, and processor name retrieval.
-   **BLACS Integration (Optional):** If compiled with ScaLAPACK support (via `-D_SCALAPACK` and `-D_MPI` flags), this module also initializes and manages BLACS contexts, providing information about the process grid.

The module often uses generic interfaces to provide type- and rank-specific MPI routines. Implementations for these are typically included from separate files (e.g., `mpi_bcast.f90`).

## Key Components

### Module: `SF_MPI`
- **Purpose:** Offers simplified wrappers for common MPI tasks and integrates BLACS setup for ScaLAPACK.
- **Dependencies:** Requires an MPI library (uses `include 'mpif.h'`). Optionally uses `SF_BLACS` for ScaLAPACK features.

---

### MPI Environment Management

#### `Subroutine Init_MPI(comm, msg)`
- **Purpose:** Initializes the MPI environment. Calls `MPI_Init`.
- **Inputs:**
    - `comm` (integer, optional, out): If present, returns the global communicator `MPI_COMM_WORLD`.
    - `msg` (logical, optional, in): If `.true.`, prints a startup message showing active MPI ranks (via `StartMsg_MPI`).

#### `Subroutine Finalize_MPI(comm)`
- **Purpose:** Finalizes the MPI environment. Calls `MPI_Finalize`.
- **Inputs:**
    - `comm` (integer, optional, inout): If present, will be set to `MPI_COMM_NULL`.

#### `Subroutine StartMsg_MPI(comm)`
- **Purpose:** Prints a startup message to standard output, showing the rank and total size of the communicator, for each process in turn.
- **Inputs:**
    - `comm` (integer, optional): The MPI communicator (defaults to `MPI_COMM_WORLD`).

#### `Subroutine Barrier_MPI(comm)`
- **Purpose:** Blocks until all processes in the communicator `comm` have reached this routine. Calls `MPI_Barrier`.
- **Inputs:**
    - `comm` (integer, optional): The MPI communicator (defaults to `MPI_COMM_WORLD`).

---

### MPI Utility Functions

#### `Function check_MPI() result(bool)`
- **Purpose:** Checks if MPI has been initialized.
- **Outputs:**
    - `bool` (logical): `.true.` if `MPI_Initialized` returns true, `.false.` otherwise.

#### `Function get_size_MPI(comm) result(size)`
- **Purpose:** Gets the total number of processes in the communicator. Calls `MPI_Comm_size`.
- **Inputs:**
    - `comm` (integer, optional): The MPI communicator (defaults to `MPI_COMM_WORLD`).
- **Outputs:**
    - `size` (integer): Number of processes. Returns undefined if MPI is not initialized or `comm` is null.

#### `Function Get_rank_MPI(comm) result(rank)`
- **Purpose:** Gets the rank of the calling process in the communicator. Calls `MPI_Comm_rank`.
- **Inputs:**
    - `comm` (integer, optional): The MPI communicator (defaults to `MPI_COMM_WORLD`).
- **Outputs:**
    - `rank` (integer): Rank of the current process (0 to size-1). Returns undefined if MPI is not initialized.

#### `Function Get_master_MPI(comm) result(master)`
- **Purpose:** Checks if the current process is the master process (rank 0).
- **Inputs:**
    - `comm` (integer, optional): The MPI communicator (defaults to `MPI_COMM_WORLD`).
- **Outputs:**
    - `master` (logical): `.true.` if current process has rank 0, `.false.` otherwise.

#### `Function Get_last_MPI(comm) result(last)`
- **Purpose:** Checks if the current process is the last process (rank size-1).
- **Inputs:**
    - `comm` (integer, optional): The MPI communicator (defaults to `MPI_COMM_WORLD`).
- **Outputs:**
    - `last` (logical): `.true.` if current process has rank `size-1`, `.false.` otherwise.

#### `Function cpu_time_MPI() result(time)`
- **Purpose:** Returns elapsed wall-clock time in seconds on the calling processor. Calls `MPI_WTIME()`.
- **Outputs:**
    - `time` (real(8)): Elapsed time.

#### `Function Get_Processor_MPI() result(workstation)`
- **Purpose:** Gets the name of the processor. Calls `MPI_GET_PROCESSOR_NAME`.
- **Outputs:**
    - `workstation` (character, len=MPI_MAX_PROCESSOR_NAME): Name of the processor.

#### `Subroutine Error_MPI(err, sub)`
- **Purpose:** Prints a descriptive error message based on an MPI error code.
- **Inputs:**
    - `err` (integer, optional, intent(in)): The MPI error code (defaults to internal `ierr` variable).
    - `sub` (character, optional, intent(in)): Name of the subroutine where the error occurred.

---

### Collective Communication Interfaces

These interfaces provide generic wrappers for MPI collective operations. They map to specific subroutines handling different data types (Boolean, Integer, Real(8), Complex(8)) and array ranks (0 for scalars, 1-7 or 1-8 for arrays).

#### Interface: `Bcast_MPI`
- **Purpose:** Broadcasts data from a root process to all other processes in a communicator. Wraps `MPI_BCAST`.
- **Typical Signature:** `CALL Bcast_MPI(comm, data, root)`
- **Inputs:**
    - `comm` (integer, intent(in)): The MPI communicator.
    - `data` (various types/ranks, intent(inout) on root, intent(out) on others): The data buffer.
    - `root` (integer, optional, intent(in)): Rank of the broadcasting process (default 0).

#### Interface: `AllGather_MPI`
- **Purpose:** Gathers data from all processes and delivers it to all processes. Wraps `MPI_ALLGATHER`.
- **Typical Signature:** `CALL AllGather_MPI(comm, send_data, recv_data, root)` (Note: `root` is not standard for `MPI_ALLGATHER` but present in some specific routines here, though typically unused). The `send_data` from each process is concatenated into `recv_data` on all processes.
- **Inputs:**
    - `comm` (integer, intent(in)): The MPI communicator.
    - `send_data` (various types/ranks, intent(in)): Data to send from the current process.
    - `recv_data` (various types/ranks, intent(inout)): Buffer to receive data from all processes. Must be large enough (typically `size(send_data) * num_processes`).
    - `root` (integer, optional, intent(in)): Generally unused for Allgather.

#### Interface: `AllReduce_MPI`
- **Purpose:** Combines data from all processes using an operation (typically `MPI_SUM`) and distributes the result back to all processes. Wraps `MPI_ALLREDUCE`.
- **Typical Signature:** `CALL AllReduce_MPI(comm, send_data, recv_data, root)` (Note: `root` is not standard for `MPI_ALLREDUCE`).
- **Inputs:**
    - `comm` (integer, intent(in)): The MPI communicator.
    - `send_data` (various types/ranks, intent(in)): Data from the current process.
    - `recv_data` (various types/ranks, intent(inout)): Buffer to store the result of the reduction.
    - `root` (integer, optional, intent(in)): Generally unused for Allreduce.
- **Operation:** The default operation used in these wrappers is `MPI_SUM`.

---

### BLACS Integration (from `SF_BLACS` module, available if compiled with ScaLAPACK)

These routines and variables are made public through `SF_MPI` when ScaLAPACK support is enabled.

-   **`Subroutine init_BLACS()`**: Initializes the BLACS process grid. Determines processor grid dimensions (`p_Nx`, `p_Ny`) and gets the BLACS context (`p_context`).
-   **`Subroutine finalize_BLACS(blacs_end_code)`**: Exits the BLACS grid and MPI.
-   **`Function get_master_BLACS() result(master)`**: True if current process is rank 0 in the BLACS grid.
-   **`Function get_rank_BLACS() result(id)`**: Returns BLACS process rank.
-   **`Function get_size_BLACS() result(numproc)`**: Returns total number of processes in BLACS grid.
-   **Module Variables:**
    -   `p_rank` (integer): Rank of the current process in the BLACS grid.
    -   `p_size` (integer): Total number of processes in the BLACS grid.
    -   `p_Nx`, `p_Ny` (integer): Dimensions of the 2D process grid.
    -   `p_context` (integer): BLACS context handle.
    -   `blacs_status` (logical): True if BLACS has been initialized.

## Important Variables/Constants
The module itself does not expose public constants beyond standard MPI parameters like `MPI_COMM_WORLD` (used as default) or `MPI_SUM` (used implicitly). The `SF_BLACS` part exposes its grid parameters as public module variables when active.

## Usage Examples

**1. Basic MPI Program Structure:**
```fortran
program test_mpi_basic
  use SF_MPI
  implicit none
  integer :: my_rank, num_procs, global_comm

  call Init_MPI(global_comm, msg=.true.) ! Initialize MPI and get communicator

  my_rank = Get_rank_MPI(global_comm)
  num_procs = Get_size_MPI(global_comm)

  if (Get_master_MPI(global_comm)) then
    print *, "Hello from the master process! Total processes:", num_procs
  end if

  print *, "Process ", my_rank, " is active."

  call Barrier_MPI(global_comm) ! Synchronize all processes

  call Finalize_MPI(global_comm) ! Finalize MPI
end program test_mpi_basic
```

**2. Broadcasting an array:**
```fortran
program test_mpi_bcast
  use SF_MPI
  implicit none
  integer :: my_rank, num_procs, root_proc
  real(8), dimension(3) :: data_array

  call Init_MPI()
  my_rank = Get_rank_MPI()
  root_proc = 0

  if (my_rank == root_proc) then
    data_array = [1.0d0, 2.0d0, 3.0d0]
    print *, "Process", my_rank, "is broadcasting:", data_array
  else
    data_array = 0.0d0 ! Initialize on other processes
  end if

  ! Broadcast data_array from root_proc to all other processes
  call Bcast_MPI(MPI_COMM_WORLD, data_array, root_proc)

  call Barrier_MPI() ! Ensure all processes have received before printing
  print *, "Process", my_rank, "received:", data_array

  call Finalize_MPI()
end program test_mpi_bcast
```

## Dependencies and Interactions

-   **MPI Library**: This module fundamentally relies on an installed MPI library and its Fortran bindings (`mpif.h`). Compilation usually requires MPI-specific compiler wrappers (e.g., `mpifort`). The MPI-dependent code is typically guarded by `#ifdef _MPI`.
-   **`SF_BLACS` Module (Conditional)**: If the code is compiled with ScaLAPACK support, `SF_MPI` integrates and re-exports functionalities from `SF_BLACS` for BLACS grid management.
-   **Internal Includes**: Specific implementations for collective operations across different data types and ranks (e.g., `mpi_bcast.f90`) are `include`d directly into the `SF_MPI` module.

This module is essential for developing parallel applications using the SciFortran library, providing a higher-level abstraction over standard MPI calls.

```
