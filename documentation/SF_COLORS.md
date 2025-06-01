## Overview

The `SF_COLORS` module in SciFortran provides definitions and tools for color manipulation. It introduces a custom type `rgb_color` to represent colors in RGB format (Red, Green, Blue) and offers a wide array of predefined color constants. Additionally, it supports arithmetic operations on colors through overloaded operators and provides functions for converting colors and selecting them by name.

## Key Components

### Type: `rgb_color`
- **Purpose:** Represents a color using Red, Green, and Blue integer components.
- **Fields:**
    - `r` (integer): Red component, typically in the range [0, 255].
    - `g` (integer): Green component, typically in the range [0, 255].
    - `b` (integer): Blue component, typically in the range [0, 255].

### Module: `SF_COLORS`
- **Purpose:** SciFortran module for color definitions and manipulation.
- **Contains:** `rgb_color` type, numerous predefined color constants (e.g., `black`, `red`, `blue`), `rgb` function, `equal_colors` subroutine, `add_colors` function, `subtract_colors` function, `scalar_left_color` function, `scalar_right_color` function, `dot_scalar_colors` function, `pick_color` function. Also defines operator overloads for `rgb_color` type.

### Function: `rgb`
- **Signature:** `Function rgb(c) result(num)`
- **Purpose:** Converts an `rgb_color` type variable `c` (containing r, g, b components) into a single integer representation using the formula `65536*r + 256*g + b`. This is often used for interfaces requiring a single integer for color.
- **Inputs:**
    - `c` (type(rgb_color), intent(in)): The input `rgb_color`.
- **Outputs:**
    - `num` (integer): The integer representation of the color.

### Subroutine: `equal_colors`
- **Signature:** `Elemental Subroutine equal_colors(C1, C2)`
- **Purpose:** Assigns the RGB components of color `C2` to color `C1`. This is also available via the overloaded assignment operator (`=`).
- **Inputs:**
    - `C2` (type(rgb_color), intent(in)): The source color.
- **Outputs:**
    - `C1` (type(rgb_color), intent(inout)): The destination color, modified to match `C2`.

### Function: `add_colors`
- **Signature:** `Elemental Function add_colors(c1, c2) result(c)`
- **Purpose:** Adds two `rgb_color` variables component-wise (`r1+r2`, `g1+g2`, `b1+b2`). This is also available via the overloaded `+` operator. The component values may exceed 255 or go below 0 if not managed.
- **Inputs:**
    - `c1` (type(rgb_color), intent(in)): The first color.
    - `c2` (type(rgb_color), intent(in)): The second color.
- **Outputs:**
    - `c` (type(rgb_color)): The resulting color from the addition.

### Function: `subtract_colors`
- **Signature:** `Elemental Function subtract_colors(c1, c2) result(c)`
- **Purpose:** Subtracts color `c2` from `c1` component-wise (`r1-r2`, `g1-g2`, `b1-b2`). This is also available via the overloaded `-` operator. The component values may exceed 255 or go below 0 if not managed.
- **Inputs:**
    - `c1` (type(rgb_color), intent(in)): The minuend color.
    - `c2` (type(rgb_color), intent(in)): The subtrahend color.
- **Outputs:**
    - `c` (type(rgb_color)): The resulting color from the subtraction.

### Function: `scalar_left_color`
- **Signature:** `Elemental Function scalar_left_color(k, cin) result(cout)`
- **Purpose:** Multiplies each component of an `rgb_color` `cin` by a scalar real value `k`. This is also available via the overloaded `*` operator (scalar on the left).
- **Inputs:**
    - `k` (real(8), intent(in)): The scalar multiplier.
    - `cin` (type(rgb_color), intent(in)): The input color.
- **Outputs:**
    - `cout` (type(rgb_color)): The resulting scaled color.

### Function: `scalar_right_color`
- **Signature:** `Elemental Function scalar_right_color(k, cin) result(cout)`
- **Purpose:** Multiplies each component of an `rgb_color` `cin` by a scalar real value `k`. (Note: The Fortran code's argument order is `k, cin` which is identical to `scalar_left_color`. This function seems redundant or a misnomer, but reflects the source. It's not typically directly invoked due to operator overloading.)
- **Inputs:**
    - `k` (real(8), intent(in)): The scalar multiplier.
    - `cin` (type(rgb_color), intent(in)): The input color.
- **Outputs:**
    - `cout` (type(rgb_color)): The resulting scaled color.

### Function: `dot_scalar_colors`
- **Signature:** `Function dot_scalar_colors(v, cin) result(cout)`
- **Purpose:** Computes a weighted sum of an array of `rgb_color` variables `cin`, where each color is weighted by a corresponding real value in array `v`. Effectively `cout = sum(v(i) * cin(i))` for each RGB component. This is also available via the overloaded `.dot.` operator.
- **Inputs:**
    - `v` (real(8) array, intent(in)): Array of real scalar weights.
    - `cin` (type(rgb_color) array, intent(in), size matching `v`): Array of input colors.
- **Outputs:**
    - `cout` (type(rgb_color)): The resulting color from the weighted sum.

### Function: `pick_color`
- **Signature:** `Function pick_color(string) result(crgb)`
- **Purpose:** Returns a predefined `rgb_color` based on a name string (e.g., "red", "blue"). If the name is not recognized, it defaults to black and prints a message.
- **Inputs:**
    - `string` (character, intent(in)): The name of the color to pick (case-insensitive).
- **Outputs:**
    - `crgb` (type(rgb_color)): The corresponding predefined color.

## Important Variables/Constants

The module defines a large number of `parameter` constants of type `rgb_color`. Key predefined colors include:
- `black`: `rgb_color(0,0,0)`
- `red`: `rgb_color(255,0,0)`
- `green`: `rgb_color(0,255,0)`
- `orange`: `rgb_color(255,193,0)`
- `blue`: `rgb_color(0,0,255)`
- `yellow`: `rgb_color(255,255,0)`
- `cyan`: `rgb_color(0,255,255)`
- `magenta`: `rgb_color(159,0,159)`
- `white`: `rgb_color(255,255,255)`

Many additional colors from the X11/rgb.txt specification (e.g., `snow`, `ghostwhite`, `skyblue1`, `maroon4`, various shades of `gray`/`grey`) are also available as parameters.

## Usage Examples

```fortran
program test_sf_colors
  use SF_COLORS
  implicit none

  type(rgb_color) :: my_color, color_sum, scaled_color
  integer :: color_int

  ! Using a predefined color
  my_color = blue
  print '("Blue: R=", I0, ", G=", I0, ", B=", I0)', my_color%r, my_color%g, my_color%b

  ! Picking a color by name
  my_color = pick_color("red")
  print '("Red: R=", I0, ", G=", I0, ", B=", I0)', my_color%r, my_color%g, my_color%b

  ! Converting to integer
  color_int = rgb(my_color)
  print '("Red as integer: ", I0)', color_int

  ! Color arithmetic
  color_sum = red + green ! (255, 255, 0) which is yellow
  print '("Sum (Red+Green): R=", I0, ", G=", I0, ", B=", I0)', color_sum%r, color_sum%g, color_sum%b
  if (color_sum%r == yellow%r .and. color_sum%g == yellow%g .and. color_sum%b == yellow%b) then
    print *, "Sum matches predefined yellow."
  end if

  scaled_color = 0.5d0 * blue ! (0, 0, 127)
  print '("Scaled Blue: R=", I0, ", G=", I0, ", B=", I0)', scaled_color%r, scaled_color%g, scaled_color%b

end program test_sf_colors
```

## Dependencies and Interactions

- **Operator Overloading:** The module heavily utilizes operator overloading for intuitive color manipulation:
    - Assignment: `=` (via `equal_colors`)
    - Addition: `+` (via `add_colors`)
    - Subtraction: `-` (via `subtract_colors`)
    - Scalar Multiplication: `*` (real * color, via `scalar_left_color`)
    - Dot Product-like sum: `.dot.` (array of reals .dot. array of colors, via `dot_scalar_colors`)
- **Internal Dependencies:** None beyond its own components.
- **External Libraries:** This module has no direct dependencies on external libraries.
- **Interactions:** This module is foundational for any graphical output or color specification within the SciFortran ecosystem. It is likely used by plotting routines or any component that needs to define or manage colors.

```
