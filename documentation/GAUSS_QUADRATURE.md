## Overview

ENTIRELY BASED ON THE WORK OF
Jacob Williams https://github.com/jacobwilliams/quadrature-fortran
SEE There for a more object-oriented approach and further information.
LICENSE CAN BE FOUND HERE:
https://github.com/jacobwilliams/quadrature-fortran/blob/master/LICENSE
LIBRARY EXTENDED TO DEAL WITH:
1D, 2D sampled functions (dble arrays)
vectorial functions of vectorial variables F:R^n-->R^m
this required to slightly change *dgauss_generic routine and gX=6,8,10,12,14
to handle multiple functions simultaneously.

## Key Components

### Module: `GAUSS_QUADRATURE`
- **Purpose:** ENTIRELY BASED ON THE WORK OF
Jacob Williams https://github.com/jacobwilliams/quadrature-fortran
SEE There for a more object-oriented approach and further information.
LICENSE CAN BE FOUND HERE:
https://github.com/jacobwilliams/quadrature-fortran/blob/master/LICENSE
LIBRARY EXTENDED TO DEAL WITH:
1D, 2D sampled functions (dble arrays)
vectorial functions of vectorial variables F:R^n-->R^m
this required to slightly change *dgauss_generic routine and gX=6,8,10,12,14
to handle multiple functions simultaneously.
- **Contains:** `f_xvec`, `gauss_func_method`, `init_type`, `integrate_1d_func_main`, `integrate_1d_func_1`, `func`, `fx`, `integrate_nd_func_main`, `f_of_x1`, `f_of_x2`, `f_of_x3`, `f_of_x4`, `f_of_x5`, `f_of_x6`, `integrate_nd_func_1`, `func`, `fxvec`, `integrate_1d_sample`, `fx`, `integrate_2d_sample`, `fxvec`, `dgauss_generic`, `g6`, `g8`, `g10`, `g12`, `g14`, `init_finter_1d`, `init_finter_2d`, `delete_finter_1d`, `delete_finter_2d`, `locate`, `polint`, `polin2`, `iminloc`, `assert_eq`, `gauss_quad_linspace`

### Function: `f_xvec`
- **Signature:** `Function f_xvec(x,m)`
- **Purpose:** Gaussian quadrature method to be used in integration
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `gauss_func_method`
- **Signature:** `Function gauss_func_method(self, x, h, m)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `init_type`
- **Signature:** `Subroutine init_type(self,xl,xu,tol,method)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `integrate_1d_func_main`
- **Signature:** `Subroutine integrate_1d_func_main(m,fx,xl,xu,ans,tol,method,ierr,err)`
- **Purpose:** ##################################################################
  ##################################################################
  FUNCTIONS: nD R^n --> R^m
  m=1 is available as a simplified interface
  ##################################################################
  ##################################################################
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `integrate_1d_func_1`
- **Signature:** `Subroutine integrate_1d_func_1(func,xl,xu,ans,tol,method,ierr,err)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `func`
- **Signature:** `Function func(x)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `fx`
- **Signature:** `Function fx(x,m)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `integrate_nd_func_main`
- **Signature:** `Subroutine integrate_nd_func_main(m,fxvec,xl,xu,ans,methods,method,tols,tol,ierr,err)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `f_of_x1`
- **Signature:** `Function f_of_x1(x1,m)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `f_of_x2`
- **Signature:** `Function f_of_x2(x2,m)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `f_of_x3`
- **Signature:** `Function f_of_x3(x3,m)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `f_of_x4`
- **Signature:** `Function f_of_x4(x4,m)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `f_of_x5`
- **Signature:** `Function f_of_x5(x5,m)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `f_of_x6`
- **Signature:** `Function f_of_x6(x6,m)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `integrate_nd_func_1`
- **Signature:** `Subroutine integrate_nd_func_1(func,xl,xu,ans,methods,method,tols,tol,ierr,err)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `func`
- **Signature:** `Function func(x)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `fxvec`
- **Signature:** `Function fxvec(x,m)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `integrate_1d_sample`
- **Signature:** `Subroutine integrate_1d_sample(fsample,xl,xu,ans,tol,method,ierr,err)`
- **Purpose:** ##################################################################
  ##################################################################
  SAMPLED FUNCTIONS: 1D + 2D R^n --> R
  ##################################################################
  ##################################################################
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `fx`
- **Signature:** `Function fx(x,m)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `integrate_2d_sample`
- **Signature:** `Subroutine integrate_2d_sample(fsample,xl,xu,ans,methods,method,tols,tol,ierr,err)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `fxvec`
- **Signature:** `Function fxvec(xvec,m)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `dgauss_generic`
- **Signature:** `Subroutine dgauss_generic(self, ans, ierr, err, m)`
- **Purpose:** Integrate a real function of one variable over a finite
  interval using the specified adaptive algorithm.
  Intended primarily for high accuracy
  integration or integration of smooth functions.
  * SLATEC is public domain software: http://www.netlib.org/slatec/guide
  * Original sourcecode from: http://www.netlib.org/slatec/src/dgaus8.f
  * Jones, R. E., (SNLA) -- Original SLATEC code.
  * Jacob Williams : 1/20/2020 : refactored to modern Fortran and generalized.
  @note This function is recursive. [It can call itself indirectly during double integration]
  ! pick a value for abs(error_tol) so that
  ! dtol < abs(error_tol) <= 1.0e-3 where dtol is the larger
  ! of 1.0e-18 and the real(8) unit roundoff d1mach(4).
  ! ans will normally have no more error than abs(error_tol)
  ! times the integral of the absolute value of fun(x).  usually,
  ! smaller values of error_tol yield more accuracy and require
  ! more function evaluations.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `g6`
- **Signature:** `Function g6(self, x, h, m)`
- **Purpose:** > abscissae:
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `g8`
- **Signature:** `Function g8(self, x, h,m)`
- **Purpose:** > abscissae:
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `g10`
- **Signature:** `Function g10(self, x, h, m)`
- **Purpose:** > abscissae:
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `g12`
- **Signature:** `Function g12(self, x, h, m)`
- **Purpose:** > abscissae:
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `g14`
- **Signature:** `Function g14(self, x, h, m)`
- **Purpose:** > abscissae:
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `init_finter_1d`
- **Signature:** `Subroutine init_finter_1d(self,Xin,Fin,N)`
- **Purpose:** *******************************************************************
  *******************************************************************
  *******************************************************************
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `init_finter_2d`
- **Signature:** `Subroutine init_finter_2d(self,Xin,Yin,Fin,N)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `delete_finter_1d`
- **Signature:** `Subroutine delete_finter_1d(self)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `delete_finter_2d`
- **Signature:** `Subroutine delete_finter_2d(self)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `locate`
- **Signature:** `Function locate(xx,x)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `polint`
- **Signature:** `Subroutine polint(xa,ya,x,y,dy)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Subroutine: `polin2`
- **Signature:** `Subroutine polin2(x1a,x2a,ya,x1,x2,y,dy)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `iminloc`
- **Signature:** `Function iminloc(arr)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `assert_eq`
- **Signature:** `Function assert_eq(n1,n2,string)`
- **Purpose:** No specific description available.
- **Inputs:** [Details to be filled manually or by more advanced parsing]
- **Outputs:** [Details to be filled manually or by more advanced parsing]

### Function: `gauss_quad_linspace`
- **Signature:** `Function gauss_quad_linspace(start,stop,num,istart,iend,mesh)`
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
