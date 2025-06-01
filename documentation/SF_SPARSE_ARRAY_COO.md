## Overview

#ifdef _MPI
module procedure :: mpi_sf_init_dmatrix_coo
module procedure :: mpi_sf_init_cmatrix_coo
#endif

## Key Components

### Module: `SF_SPARSE_ARRAY_COO`
- **Purpose:** #ifdef _MPI
module procedure :: mpi_sf_init_dmatrix_coo
module procedure :: mpi_sf_init_cmatrix_coo
#endif
- **Contains:** `sf_init_dmatrix_coo`, `sf_init_cmatrix_coo`, `sf_delete_dmatrix_coo`, `sf_delete_cmatrix_coo`, `sf_insert_delement_coo`, `sf_insert_celement_coo`, `sf_dump_dmatrix_coo`, `sf_dump_cmatrix_coo`

### Subroutine: `sf_init_dmatrix_coo`
- **Signature:** `Subroutine sf_init_dmatrix_coo(sparse,N,N1)`
- **Purpose:** +------------------------------------------------------------------+
  PURPOSE:  initialize the sparse matrix list
  +------------------------------------------------------------------+
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `sf_init_cmatrix_coo`
- **Signature:** `Subroutine sf_init_cmatrix_coo(sparse,N,N1)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `sf_delete_dmatrix_coo`
- **Signature:** `Subroutine sf_delete_dmatrix_coo(sparse)`
- **Purpose:** #ifdef _MPI
  subroutine mpi_sf_init_dmatrix_coo(MpiComm,sparse,N,N1)
  integer                               :: MpiComm
  type(sf_sparse_dmatrix_coo),intent(inout) :: sparse
  integer                               :: N
  integer,optional                      :: N1
  integer                               :: i,Ncol,Nloc
  !
  #ifdef _DEBUG
  write(*,"(A)")"DEBUG MPI_sf_init_dmatrix_coo: allocate sparse"
  #endif
  if(MpiComm==Mpi_Comm_Null)return
  !
  call sf_test_matrix_mpi(MpiComm,sparse,"mpi_sf_init_dmatrix_coo")
  !
  Ncol = N
  if(present(N1))Ncol=N1
  !
  Nloc = sparse%iend-sparse%istart+1
  !
  call sf_init_matrix_coo(sparse,Nloc,Ncol)
  !
  allocate(sparse%loc(Nloc))
  do i=1,Nloc
  sparse%loc(i)%size=0
  allocate(sparse%loc(i)%vals(0)) !empty array
  allocate(sparse%loc(i)%cols(0)) !empty array
  end do
  !
  end subroutine mpi_sf_init_dmatrix_coo
  subroutine mpi_sf_init_cmatrix_coo(MpiComm,sparse,N,N1)
  integer                               :: MpiComm
  type(sf_sparse_cmatrix_coo),intent(inout) :: sparse
  integer                               :: N
  integer,optional                      :: N1
  integer                               :: i,Ncol,Nloc
  !
  #ifdef _DEBUG
  write(*,"(A)")"DEBUG MPI_sf_init_cmatrix_coo: allocate sparse"
  #endif
  if(MpiComm==Mpi_Comm_Null)return
  !
  call sf_test_matrix_mpi(MpiComm,sparse,"mpi_sf_init_cmatrix_coo")
  !
  Ncol = N
  if(present(N1))Ncol=N1
  !
  Nloc = sparse%iend-sparse%istart+1
  !
  call sf_init_matrix_coo(sparse,Nloc,Ncol)
  !
  allocate(sparse%loc(Nloc))
  do i=1,Nloc
  sparse%loc(i)%size=0
  allocate(sparse%loc(i)%vals(0)) !empty array
  allocate(sparse%loc(i)%cols(0)) !empty array
  end do
  !
  end subroutine mpi_sf_init_cmatrix_coo
  #endif
  +------------------------------------------------------------------+
  PURPOSE: delete an entire sparse matrix
  +------------------------------------------------------------------+
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `sf_delete_cmatrix_coo`
- **Signature:** `Subroutine sf_delete_cmatrix_coo(sparse)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `sf_insert_delement_coo`
- **Signature:** `Subroutine sf_insert_delement_coo(sparse,value,i,j)`
- **Purpose:** #ifdef _MPI
  subroutine mpi_sf_delete_dmatrix_coo(MpiComm,sparse)
  integer                              :: MpiComm
  type(sf_sparse_dmatrix_coo),intent(inout) :: sparse
  integer                              :: i
  type(sf_sparse_drow_coo),pointer          :: row
  !
  #ifdef _DEBUG
  write(*,"(A)")"DEBUG MPI_sf_delete_dmatrix_coo: delete sparse"
  #endif
  if(.not.sparse%status)return !stop "Error SPARSE/mpi_sp_delete_matrix: sparse is not allocated."
  !
  do i=1,sparse%Nrow
  deallocate(sparse%row(i)%vals)
  deallocate(sparse%row(i)%cols)
  sparse%row(i)%Size  = 0
  !
  deallocate(sparse%loc(i)%vals)
  deallocate(sparse%loc(i)%cols)
  sparse%loc(i)%Size  = 0
  enddo
  deallocate(sparse%row)
  deallocate(sparse%loc)
  !
  sparse%Nrow=0
  sparse%Ncol=0
  sparse%status=.false.
  !
  sparse%istart=0
  sparse%iend=0
  sparse%ishift=0
  sparse%mpi=.false.
  !
  end subroutine mpi_sf_delete_dmatrix_coo
  subroutine mpi_sf_delete_cmatrix_coo(MpiComm,sparse)
  integer                              :: MpiComm
  type(sf_sparse_cmatrix_coo),intent(inout) :: sparse
  integer                              :: i
  type(sf_sparse_crow_coo),pointer          :: row
  !
  #ifdef _DEBUG
  write(*,"(A)")"DEBUG MPI_sf_delete_cmatrix_coo: delete sparse"
  #endif
  if(.not.sparse%status)return !stop "Error SPARSE/mpi_sp_delete_matrix: sparse is not allocated."
  !
  do i=1,sparse%Nrow
  deallocate(sparse%row(i)%vals)
  deallocate(sparse%row(i)%cols)
  sparse%row(i)%Size  = 0
  !
  deallocate(sparse%loc(i)%vals)
  deallocate(sparse%loc(i)%cols)
  sparse%loc(i)%Size  = 0
  enddo
  deallocate(sparse%row)
  deallocate(sparse%loc)
  !
  sparse%Nrow=0
  sparse%Ncol=0
  sparse%status=.false.
  !
  sparse%istart=0
  sparse%iend=0
  sparse%ishift=0
  sparse%mpi=.false.
  !
  end subroutine mpi_sf_delete_cmatrix_coo
  #endif
  +------------------------------------------------------------------+
  PURPOSE: insert an element value at position (i,j) in the sparse matrix
  +------------------------------------------------------------------+
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `sf_insert_celement_coo`
- **Signature:** `Subroutine sf_insert_celement_coo(sparse,value,i,j)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `sf_dump_dmatrix_coo`
- **Signature:** `Subroutine sf_dump_dmatrix_coo(sparse,matrix)`
- **Purpose:** #ifdef _MPI
  subroutine mpi_sf_insert_delement_coo(MpiComm,sparse,value,i,j)
  integer                               :: MpiComm
  type(sf_sparse_dmatrix_coo),intent(inout) :: sparse
  real(8),intent(in)                    :: value
  integer,intent(in)                    :: i,j
  type(sf_sparse_drow_coo),pointer          :: row
  integer                               :: column,pos
  logical                               :: iadd
  !
  #ifdef _DEBUG
  write(*,"(A,2I8)")"DEBUG MPI_sf_insert_delement_coo: insert element in sparse @",i,j
  #endif
  !
  if(MpiComm==Mpi_Comm_Null)return
  !
  call sp_test_matrix_mpi(MpiComm,sparse," mpi_sf_insert_delement_coo")
  !
  column = j
  !
  row => sparse%row(i-sparse%Ishift)
  !
  iadd = .false.                          !check if column already exist
  if(any(row%cols == column))then         !
  pos = binary_search(row%cols,column) !find the position  column in %cols
  iadd=.true.                          !set Iadd to true
  endif
  !
  if(iadd)then                            !this column exists so just sum it up
  row%vals(pos)=row%vals(pos) + value  !add up value to the current one in %vals
  else                                    !this column is new. increase counter and store it
  call add_to(row%vals,value)
  call add_to(row%cols,column)
  row%Size = row%Size + 1
  endif
  !
  if(row%Size > sparse%Ncol)stop "mpi_sp_insert_element_coo ERROR: row%Size > sparse%Ncol"
  !
  end subroutine mpi_sf_insert_delement_coo
  subroutine mpi_sf_insert_celement_coo(MpiComm,sparse,value,i,j)
  integer                               :: MpiComm
  type(sf_sparse_cmatrix_coo),intent(inout) :: sparse
  complex(8),intent(in)                 :: value
  integer,intent(in)                    :: i,j
  type(sf_sparse_crow_coo),pointer          :: row
  integer                               :: column,pos
  logical                               :: iadd
  !
  #ifdef _DEBUG
  write(*,"(A,2I8)")"DEBUG MPI_sf_insert_celement_coo: insert element in sparse @",i,j
  #endif
  !
  call sp_test_matrix_mpi(MpiComm,sparse," mpi_sf_insert_celement_coo")
  !
  column = j
  !
  if(column>=sparse%Istart.AND.column<=sparse%Iend)then
  row => sparse%loc(i-sparse%Ishift)
  else
  row => sparse%row(i-sparse%Ishift)
  endif
  !
  iadd = .false.                          !check if column already exist
  if(any(row%cols == column))then         !
  pos = binary_search(row%cols,column) !find the position  column in %cols
  iadd=.true.                          !set Iadd to true
  endif
  !
  if(iadd)then                            !this column exists so just sum it up
  row%vals(pos)=row%vals(pos) + value  !add up value to the current one in %vals
  else                                    !this column is new. increase counter and store it
  call add_to(row%vals,value)
  call add_to(row%cols,column)
  row%Size = row%Size + 1
  endif
  !
  if(row%Size > sparse%Ncol)stop "mpi_sp_insert_element_coo ERROR: row%Size > sparse%Ncol"
  !
  end subroutine mpi_sf_insert_celement_coo
  #endif
  +------------------------------------------------------------------+
  PURPOSE: dump a sparse matrix into a regular 2dim array
  +------------------------------------------------------------------+
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `sf_dump_cmatrix_coo`
- **Signature:** `Subroutine sf_dump_cmatrix_coo(sparse,matrix)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

## Important Variables/Constants

[List and describe any important variables or constants defined or used extensively in this file.]

- **Variable/Constant 1:** ([Type]) [Description, purpose, and typical values/range]
- **Variable/Constant 2:** ([Type]) [Description, purpose, and typical values/range]

## Usage Examples

[Provide one or more code snippets demonstrating how to use the components of this file.]

```fortran
! Example 1: Calling a key subroutine/function
! ... code ...
```

## Dependencies and Interactions

[Describe any dependencies this file has on other modules or external libraries. Also, explain how this file interacts with other parts of the project.]

- **Internal Dependencies:** [List other project files/modules this file depends on]
- **External Libraries:** [List any external libraries required, e.g., BLAS, LAPACK]
- **Interactions:** [Describe how this file is used by or uses other components of the software]
