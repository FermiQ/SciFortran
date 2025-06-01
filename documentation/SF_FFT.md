## Overview

The `SF_FFT_FFTPACK` module (from `SF_FFT.f90`) serves as the primary SciFortran interface for Fourier Transform operations. It provides:
- Simple direct Fourier Transform implementations for discretised functions.
- A comprehensive set of interfaces to the FFTPACK 5.1 library for performing Fast Fourier Transforms (FFTs) on real and complex data, in 1D, 2D, and N-D. This includes standard FFTs, as well as Cosine and Sine transforms.
- Helper functions for managing FFT data, such as shifting zero-frequency components and generating time/frequency arrays.

The actual FFTPACK routines are wrapped in a lower-level module `FFT_FFTPACK` (from `FFT_FFTPACK.f90`), which `SF_FFT_FFTPACK` uses. Users should typically interact with the interfaces provided by `SF_FFT_FFTPACK`.

## Key Components

### Module: `SF_FFT_FFTPACK`
- **Purpose:** Provides high-level interfaces for various Fourier Transform operations, primarily leveraging FFTPACK 5.1.
- **Key Public Interfaces (details below):** `FT_direct`, `FT_inverse`, `FFT_signal`, `iFFT_signal`, `tfft`, `itfft`, `fft`, `ifft`, `fft2`, `ifft2`, `fftn`, `ifftn`, `cosft`, `icosft`, `cosftn`, `icosftn`, `sinft`, `isinft`, `sinftn`, `isinftn`, `fftshift`, `ifftshift`, `fftex`.
- **Key Public Functions:** `fft_tmax`, `fft_fmax`, `fft_tarray`, `fft_farray`.

---

### Direct Fourier Transforms

These functions perform a direct, non-FFT calculation of the Fourier transform using numerical integration (Simpson's rule).

#### Interface: `FT_direct`
- **Purpose:** Evaluates the direct Fourier transform of a discretised function from time to frequency domain.
  Calculates :math:`fw(w_j) = \int ft(t) e^{-i 2\pi w_j t} dt`.
- **Specific Functions:** `d_FT_direct` (real input/output), `c_FT_direct` (complex input/output).
- **Inputs:**
    - `ft` (real(8) or complex(8) array, intent(in)): Discretised function in time domain.
    - `t` (real(8) array, intent(in), size of `ft`): Time points.
    - `w` (real(8) array, intent(in)): Frequency points at which to evaluate the transform.
- **Outputs:**
    - `fw` (real(8) or complex(8) array, size of `w`): Transformed function in frequency domain.

#### Interface: `FT_inverse`
- **Purpose:** Evaluates the inverse direct Fourier transform from frequency to time domain.
  Calculates :math:`ft(t_j) = \int fw(w) e^{i 2\pi t_j w} dw`.
- **Specific Functions:** `d_FT_inverse` (real input/output), `c_FT_inverse` (complex input/output).
- **Inputs:**
    - `fw` (real(8) or complex(8) array, intent(in)): Discretised function in frequency domain.
    - `w` (real(8) array, intent(in), size of `fw`): Frequency points.
    - `t` (real(8) array, intent(in)): Time points at which to evaluate the transform.
- **Outputs:**
    - `ft` (real(8) or complex(8) array, size of `t`): Transformed function in time domain.

---

### FFT for Signals (Time/Frequency Domain)

These routines provide a higher-level abstraction for typical signal processing FFTs, incorporating scaling and shifting.

#### Interface: `FFT_signal`
- **Purpose:** Evaluates the FFT of a time-domain signal `ft` with time step `dt`. Returns `fw = dt * tfft(ft)`.
- **Specific Functions:** `d_FFT_signal` (real), `c_FFT_signal` (complex).
- **Inputs:**
    - `ft` (real(8) or complex(8) array, intent(in)): Time-domain signal.
    - `dt` (real(8), intent(in)): Time step.
- **Outputs:**
    - `fw` (real(8) or complex(8) array, size of `ft`): Frequency-domain signal.

#### Interface: `iFFT_signal`
- **Purpose:** Evaluates the inverse FFT of a frequency-domain signal `fw`. Returns `ft = itfft(fw) / dt`.
- **Specific Functions:** `d_iFFT_signal` (real), `c_iFFT_signal` (complex).
- **Inputs:**
    - `fw` (real(8) or complex(8) array, intent(in)): Frequency-domain signal.
    - `dt` (real(8), intent(in)): Original time step (used for scaling).
- **Outputs:**
    - `ft` (real(8) or complex(8) array, size of `fw`): Time-domain signal.

#### Interface: `tfft`
- **Purpose:** A wrapper that applies `ifftshift`, then `fft`, then `fftshift` and scales by array size. Modifies input array in place or returns to `func_out`.
- **Specific Subroutines:** `d_tfft` (real), `c_tfft` (complex).
- **Inputs:**
    - `func_in` (real(8) or complex(8) array, intent(inout) or intent(in)): Input signal.
- **Outputs (Optional):**
    - `func_out` (real(8) or complex(8) array, optional, intent(out)): Output transformed signal. If not present, `func_in` is overwritten.

#### Interface: `itfft`
- **Purpose:** A wrapper that applies `ifft`, then `fftex` (alternates sign), then `ifftshift` and scales by 1/array_size. Modifies input array in place or returns to `func_out`.
- **Specific Subroutines:** `d_itfft` (real), `c_itfft` (complex).
- **Inputs:**
    - `func_in` (real(8) or complex(8) array, intent(inout) or intent(in)): Input signal.
- **Outputs (Optional):**
    - `func_out` (real(8) or complex(8) array, optional, intent(out)): Output transformed signal. If not present, `func_in` is overwritten.

---

### Core FFTPACK Wrappers

These interfaces provide more direct access to FFTPACK routines for 1D, 2D, and N-D transforms of real or complex data, as well as Cosine and Sine transforms. The input array `func` is typically modified in-place.

- **`fft` / `ifft`**: 1D forward/backward FFT. (Maps to `rfft_1d_forward/backward`, `cfft_1d_forward/backward`)
- **`fft2` / `ifft2`**: 2D forward/backward FFT. (Maps to `rfft_2d_forward/backward`, `cfft_2d_forward/backward`)
- **`fftn` / `ifftn`**: N-D forward/backward FFT. (Maps to `rfft_nd_forward/backward`, `cfft_nd_forward/backward`)
    - **Inputs for N-D:** `func` (1D array representing N-D data), `n` (integer, size of dimension being transformed), `lot` (integer, number of such dimensions or batches).
- **`cosft` / `icosft`**: 1D forward/backward Cosine FFT. (Maps to `cost_1d_forward/backward`)
- **`cosftn` / `icosftn`**: N-D forward/backward Cosine FFT. (Maps to `cost_nd_forward/backward`)
- **`sinft` / `isinft`**: 1D forward/backward Sine FFT. (Maps to `sint_1d_forward/backward`)
- **`sinftn` / `isinftn`**: N-D forward/backward Sine FFT. (Maps to `sint_nd_forward/backward`)

**Inputs (General for FFTPACK wrappers):**
- `func` (real(8) or complex(8) array, intent(inout)): The data to be transformed. Modified in place.
- For N-D transforms:
    - `n` (integer, intent(in)): The length of the dimension currently being transformed.
    - `lot` (integer, intent(in)): The number of transforms of length `n` to perform.
**Outputs:**
- `func` (array, intent(inout)): Contains the transformed data in the specific packed format used by FFTPACK.

---

### Helper Functions

#### Interface: `fftshift` / `ifftshift`
- **Purpose:**
    - `fftshift`: Shifts the zero-frequency component of an FFT output from the start of the array to the center.
    - `ifftshift`: Reverses the `fftshift` operation.
- **Specific Functions:** `rfft_1d_shift/ishift` (real), `cfft_1d_shift/ishift` (complex).
- **Inputs:**
    - `fin` (real(8) or complex(8) array, intent(in)): Input array.
- **Outputs:**
    - `fout` (real(8) or complex(8) array, size of `fin`): Shifted array.

#### Interface: `fftex`
- **Purpose:** Alternates the sign of the elements in an array. Used in some inverse FFT formulations.
- **Specific Subroutines:** `rfft_1d_ex` (real), `cfft_1d_ex` (complex).
- **Inputs/Outputs:**
    - `func` (real(8) or complex(8) array, intent(inout)): Array to be modified.

#### Time/Frequency Array Generation:
- **`fft_tmax(L, dt)`**: Calculates maximum time for a signal of length `L` and time step `dt`. Returns `L*dt/2`.
- **`fft_fmax(L, dt)`**: Calculates maximum frequency (Nyquist) for a signal. Returns `pi/dt`.
- **`fft_tarray(L, dt)`**: Generates a time array for an FFT signal, from `-tmax` to `tmax`. Uses `SF_ARRAYS%linspace`.
- **`fft_farray(L, dt, df)`**: Generates a frequency array, from `-fmax` to `fmax`. Uses `SF_ARRAYS%linspace`. `df` is an optional output for frequency step.
- **Inputs:**
    - `L` (integer): Length of the signal/array.
    - `dt` (real(8)): Time step.
- **Outputs:** Corresponding max value or array.

## Important Variables/Constants

This module itself does not define public constants, but it relies on `pi` and `xi` from `SF_CONSTANTS`.

## Usage Examples

```fortran
program test_sf_fft
  use SF_FFT_FFTPACK
  use SF_ARRAYS, only: linspace
  use SF_CONSTANTS, only: pi
  implicit none

  integer, parameter :: N = 64 ! Number of points
  real(8) :: signal(N), time_step, freq_step
  complex(8) :: spectrum(N)
  real(8) :: t_arr(N), f_arr(N)

  ! 1. Generate a sample signal (e.g., sum of two sines)
  time_step = 0.01d0
  t_arr = fft_tarray(N, time_step) ! Using helper from SF_FFT_FFTPACK
  signal = sin(2.0d0 * pi * 5.0d0 * t_arr) + 0.5d0 * sin(2.0d0 * pi * 10.0d0 * t_arr)

  ! 2. Perform FFT
  ! For real input, typically use rfft_1d_forward or the 'fft' interface
  ! which handles real data appropriately.
  ! The 'fft' interface for real data might return a packed complex format.
  ! For simplicity, let's use the higher-level FFT_signal for real->complex

  spectrum = c_FFT_signal(cmplx(signal, 0.0d0), time_step) ! Use complex version for full spectrum view

  ! 3. Shift zero-frequency component to the center for visualization
  spectrum = cfft_1d_shift(spectrum)

  ! 4. Generate frequency array for plotting
  f_arr = fft_farray(N, time_step, df=freq_step)

  print *, "Sample of shifted spectrum magnitudes:"
  ! do i = 1, N
  !   print '(F8.4, ES12.4)', f_arr(i), abs(spectrum(i))
  ! end do
  print '(A, 5ES12.4)', "Freqs: ", f_arr(N/2 - 2 : N/2 + 2)
  print '(A, 5ES12.4)', "Amps:  ", abs(spectrum(N/2 - 2 : N/2 + 2))


  ! 5. Inverse FFT (demonstrating ifft_signal)
  ! First, inverse shift the spectrum
  spectrum = cfft_1d_ishift(spectrum)
  signal = real(c_iFFT_signal(spectrum, time_step)) ! Back to real signal

  ! print *, "First 5 points of original and reconstructed signal:"
  ! print *, t_arr(1:5)
  ! print *, sin(2.0d0 * pi * 5.0d0 * t_arr(1:5)) + 0.5d0 * sin(2.0d0 * pi * 10.0d0 * t_arr(1:5))
  ! print *, signal(1:5)

end program test_sf_fft
```

## Dependencies and Interactions

- **`SF_INTEGRATE`**: Used by `FT_direct` and `FT_inverse` for Simpson's rule integration.
- **`SF_ARRAYS`**: Used by `fft_tarray` and `fft_farray` for generating time/frequency coordinate arrays via `linspace`.
- **`SF_CONSTANTS`**: Uses `pi`, `pi2`, `xi` for mathematical formulations.
- **FFTPACK 5.1**: The core FFT subroutines (`rfft1i`, `rfft1f`, `cfft1i`, `cfft1f`, etc.) are external routines from the FFTPACK library. These are called by the procedures within the `FFT_FFTPACK` module, which is then used by `SF_FFT_FFTPACK`.
- **Interactions:** This module is critical for any signal processing, frequency analysis, or numerical methods that rely on Fourier transforms.

```
