"""Exercise 1: convolution by definition, comparison and FFT."""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def sequences():
    nx = np.arange(-4, 5)
    ny = np.arange(-2, 6)
    x = 10 - nx
    y = 0.8 ** (ny + 1)
    return nx, x, ny, y


def convolution(x, y):
    # z[i] = sum_k x[k] y[i-k]; values outside each array are zero.
    z = np.zeros(len(x) + len(y) - 1)
    for i in range(len(z)):
        for k in range(len(x)):
            j = i - k
            if 0 <= j < len(y):
                z[i] += x[k] * y[j]
    return z


def spectra(x, y, z, fs):
    if not np.isfinite(fs) or fs <= 0:
        raise ValueError("Sampling frequency must be finite and positive.")
    # One common length and scale for the three magnitude spectra.
    nfft = len(z)
    f = np.fft.fftshift(np.fft.fftfreq(nfft, d=1 / fs))
    magnitudes = [np.abs(np.fft.fftshift(np.fft.fft(a, nfft))) / nfft
                  for a in (x, y, z)]
    return f, magnitudes


def main(fs=None):
    nx, x, ny, y = sequences()
    nz = np.arange(nx[0] + ny[0], nx[-1] + ny[-1] + 1)
    z = convolution(x, y)
    reference = np.convolve(x, y)
    np.testing.assert_allclose(z, reference, rtol=1e-12, atol=1e-12)

    out = Path(__file__).parent / "figures"
    out.mkdir(exist_ok=True)
    if fs is None:
        # This script owns this generated file. Do not retain an earlier Hz choice.
        (out / "ex1_spectra.png").unlink(missing_ok=True)
    fig, axes = plt.subplots(3, 1, figsize=(9, 8), layout="constrained")
    for ax, n, values, title in zip(axes, (nx, ny, nz), (x, y, z),
                                   ("x[n]", "y[n]", "z[n] = x[n] * y[n]")):
        ax.stem(n, values)
        ax.set(title=title, xlabel="Sample index n", ylabel="Amplitude")
        ax.grid(alpha=0.3)
    fig.savefig(out / "ex1_convolution.png", dpi=150)
    plt.close(fig)

    # Padding to 9 + 8 - 1 = 16 avoids circular overlap.
    # Array origins are -4 and -2, so the result starts at -6.
    X = np.fft.fft(x, len(z))
    Y = np.fft.fft(y, len(z))
    Z = np.fft.fft(z)
    np.testing.assert_allclose(Z, X * Y, rtol=1e-12, atol=1e-10)
    z_fft = np.fft.ifft(X * Y)
    np.testing.assert_allclose(z_fft, z, rtol=1e-12, atol=1e-12)
    fig, ax = plt.subplots(figsize=(9, 4), layout="constrained")
    ax.plot(nz, z, "o", label="Convolution sum")
    ax.plot(nz, z_fft.real, "+", markersize=10, label="IFFT(FFT(x) FFT(y))")
    ax.set(title="Exercise 1C: convolution theorem", xlabel="Sample index n",
           ylabel="Amplitude")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.savefig(out / "ex1_theorem.png", dpi=150)
    plt.close(fig)
    print("Convolution: 16 samples, indices -6 through 9.")
    print(f"Maximum NumPy difference: {np.max(np.abs(z - reference)):.3e}")
    print(f"Maximum FFT-product difference: {np.max(np.abs(Z - X * Y)):.3e}")

    if fs is None:
        print("Exercise 1B pending: supply --fs only after choosing/clarifying the Hz scale. "
              "Any earlier ex1_spectra.png has been removed.")
        return
    f, magnitudes = spectra(x, y, z, fs)
    fig, ax = plt.subplots(figsize=(9, 4), layout="constrained")
    for values, name in zip(magnitudes, ("x", "y", "z = x * y")):
        ax.plot(f, values, ".-", label=name)
    ax.set(title=f"Exercise 1B: selected fs = {fs:g} Hz, NFFT = 16",
           xlabel="Frequency (Hz)", ylabel="Magnitude |FFT| / 16")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.savefig(out / "ex1_spectra.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fs", type=float, help="Explicit Exercise 1 sampling frequency in Hz")
    args = parser.parse_args()
    if args.fs is not None and (not np.isfinite(args.fs) or args.fs <= 0):
        parser.error("--fs must be finite and positive")
    main(args.fs)
