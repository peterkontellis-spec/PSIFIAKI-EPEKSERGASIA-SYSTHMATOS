# Lab 1 - Working report

**Status:** verified sections below; Exercise 1B and the final Exercise 3A result are pending clarification. This is not the final submission. Group naming and authors remain open.

## Exercise 1

### A. Sequences and convolution

The first sequence is `x[n] = 10 - n` for `-4 <= n <= 4`, with 9 samples. The second is `y[n] = 0.8^(n+1)` for `-2 <= n <= 5`, with 8 samples. Both are zero outside these ranges.

We calculate `z[n] = sum_k x[k] y[n-k]` with a loop, keeping only terms where both sequences are defined. Array positions start at zero, but the physical indices start at -4 and -2. The output therefore starts at -6 and ends at 9. Its length is `9 + 8 - 1 = 16`, as described on preparation p. 4.

The result agrees with `numpy.convolve`: the maximum absolute difference in the checked run was `8.882e-16`, within floating-point rounding. The first value is `14 * 1.25 = 17.5` and the last is `6 * 0.262144 = 1.572864`. Increasing either input length increases the full convolution length according to `Nx + Ny - 1`; the actual values depend on the products that overlap at each position.

![Input sequences and their convolution](figures/ex1_convolution.png)

### B. Magnitude spectra - pending physical frequency scale

The FFT calculation is implemented, but a final Hz plot is pending the sampling-frequency clarification. The inputs have discrete sample indices; neither PDF assigns a physical interval between them. Once supplied, `fftfreq(16, d=1/fs)` gives the Hz axis. The plot will show both inputs and the convolution together with a common FFT length and normalization `|FFT| / 16`. Changing `fs` changes the Hz axis, not these magnitudes. No value is presented here as the instructor's intended sampling rate.

### C. Convolution theorem

For finite sequences, put `m = n-k` in the Fourier sum:

```text
Z(w) = sum_n sum_k x[k] y[n-k] exp(-j w n)
     = sum_k x[k] exp(-j w k) sum_m y[m] exp(-j w m)
     = X(w) Y(w).
```

For the numerical check, both inputs are padded to 16 samples, the full linear-convolution length. The FFT product matches the FFT of the convolution; the maximum absolute difference was `5.684e-14`. The inverse FFT of the product also matches the convolution. Padding prevents circular overlap. The arrays start at their respective first nonzero samples, so the output is labelled from -6. Accounting for the physical origins in all three transforms gives the same identity because `-4 + (-2) = -6`.

![Convolution and inverse FFT comparison](figures/ex1_theorem.png)

## Exercise 2

### A-B. Signal, spectrum and Nyquist rate

The signal is `x(t) = 20 cos(10 pi t) - 40 sin(5 pi t)`. Comparing angular frequencies with `2 pi f` gives components at 5 Hz and 2.5 Hz. Thus the Nyquist sampling rate is `2 * 5 = 10 Hz`.

We use a 1 ms numerical grid strictly inside `0 < t < 0.5 s` to draw the continuous signal. Following preparation pp. 23/25, the plotted finite-record spectrum is `abs(FFT(x) * dt)` with a centred Hz axis. It is an approximation for the observed time record, not the ideal infinite-duration line spectrum. The short record and frequencies falling between FFT bins spread the spectral energy. The exact component frequencies and Nyquist rate follow from the given formula, rather than from selecting the largest plotted bin. A nonzero record start changes the transform phase, but not this magnitude plot.

![Original signal and finite-record spectrum](figures/ex2_signal_spectrum.png)

### C. Three sampling periods

Samples are at `t = n / fs`, with integer n and endpoints excluded as in the question. The plots follow preparation pp. 19-21: original curve and sampled points on the same axes. They are not plots of numerical interpolation.

![Sampling over half a second](figures/ex2_sampling_0p5s.png)

- **20 Hz (`Ts = 1/20 s`):** both components are below `fs/2 = 10 Hz`. With the ideal infinite sequence and the reconstruction theory in the brief, the signal can be recovered without aliasing. A finite set of plotted samples alone is not an exact infinite-record reconstruction.
- **10 Hz (`Ts = 1/10 s`):** the 5 Hz cosine is exactly at the Nyquist boundary. Its samples are `20 (-1)^n`; it does not vanish. The other component is `-40 sin(pi n/2)`, below that boundary. This is the limiting case illustrated for a cosine in preparation p. 20. It is not a general phase-independent guarantee: a sine at the same Nyquist boundary would have zero samples. The finite plot is not evidence of perfect reconstruction.
- **5 Hz (`Ts = 1/5 s`):** the cosine becomes `20 cos(2 pi n) = 20`, and the sine becomes `-40 sin(pi n) = 0`. Therefore every sample is 20. A DC signal of amplitude 20 has the same samples, so the original cannot be uniquely reconstructed. The 5 Hz component aliases to DC and the 2.5 Hz sine is lost at the boundary for this phase.

![Sampling over five seconds](figures/ex2_sampling_5s.png)

Increasing the interval to `0 < t < 5 s` gives more samples and shows more repetitions, but leaves `Ts` and the aliasing conditions unchanged. At 5 Hz the samples are still all 20. A longer record can improve FFT frequency spacing and reduce some finite-record effects, but cannot recover information lost through aliasing. No additional reconstruction algorithm is introduced.

## Exercise 3

### A. Sampling frequency and 128 samples - final plot pending phase unit

The signal contains 20 Hz and 60 Hz terms. The question allows choosing `fs`; we use 256 Hz, which is greater than `2 * 60 = 120 Hz`. Other rates strictly above 120 Hz also avoid aliasing for these components; choosing equality would require special care with the highest-frequency phase.

Exactly 128 samples are generated, at `n / 256` for `n = 0,...,127`. The FFT spacing is `256 / 128 = 2 Hz`. The centred, normalized magnitude spectrum has peaks of 6 at +/-20 Hz and 9 at +/-60 Hz (half the corresponding amplitudes in a two-sided spectrum).

The printed `+30` has no explicit unit. Both interpretations have been tested, but the final waveform and plot are pending clarification. These phase choices change sample values while preserving these magnitudes at the selected bin-aligned frequencies.

### B. Fixed sampling frequency of 20 kHz

Substituting `t = n/fs` into the given sine gives:

```text
x[n] = sin(2 pi (f0 / 20000) n + phi).
```

For the required plots, we choose `phi = 0` radians and 400 samples because neither is prescribed in this subpart. The FFT bin spacing is `20000 / 400 = 50 Hz`, so each requested frequency falls on a bin. We use `abs(FFT) / 400` as in preparation p. 22. Each unit-amplitude sine gives two peaks of magnitude 0.5. The figures show the useful range -2500 to 2500 Hz; the remaining bins are zero to numerical precision in these records.

![Spectra at 500, 1000, 1500 and 2000 Hz](figures/ex3b_low.png)

The four lower frequencies are below the Nyquist frequency of 10 kHz, so their peaks appear at their original positive and negative frequencies.

![Spectra at 18000, 18500, 19000 and 19500 Hz](figures/ex3b_high.png)

| Input frequency | Signed baseband frequency | Magnitude-spectrum peaks |
|---|---|---|
| 18000 Hz | -2000 Hz | +/-2000 Hz |
| 18500 Hz | -1500 Hz | +/-1500 Hz |
| 19000 Hz | -1000 Hz | +/-1000 Hz |
| 19500 Hz | -500 Hz | +/-500 Hz |

For `f0 = fs - fa`, integer n gives `sin(2 pi f0 n/fs + phi) = sin(phi - 2 pi fa n/fs)`. With phase zero, this is the negative of the sine at `fa`; it has the same magnitude spectrum but different sample signs. These four frequencies exceed 10 kHz, so their original frequencies cannot be identified uniquely from the samples.

## Remaining before submission

Resolve the physical Hz scale in 1B and phase unit in 3A, generate their figures, complete the report with those results and agreed group/author details, then prepare and verify the required ZIP. No final package or eClass upload is claimed.
