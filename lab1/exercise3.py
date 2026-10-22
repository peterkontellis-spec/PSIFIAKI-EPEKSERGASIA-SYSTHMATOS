"""Exercise 3: sampling and two-sided FFT magnitude spectra."""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def signal_a(phase_unit):
    # The brief allows a sampling frequency of our choice. 256 > 2 * 60 Hz.
    fs = 256
    t = np.arange(128) / fs
    if phase_unit == "radians":
        phase = 30.0
    elif phase_unit == "degrees":
        phase = np.deg2rad(30.0)
    else:
        raise ValueError("Choose 'radians' or 'degrees' explicitly for the printed +30.")
    x = 12 * np.cos(2 * np.pi * 20 * t) - 18 * np.sin(2 * np.pi * 60 * t + phase)
    return t, x, fs


def signal_b(f0, phase=0.0):
    fs = 20000
    # 400 samples give 50 Hz bin spacing; all assigned frequencies fit FFT bins.
    # The brief does not fix N or phi in 3B. Use phi=0 radians for the plots.
    n = np.arange(400)
    x = np.sin(2 * np.pi * f0 * n / fs + phase)
    return n, x, fs


def spectrum(x, fs):
    # Preparation p. 22: divide by N. Two-sided amplitudes are A/2 per peak.
    f = np.fft.fftshift(np.fft.fftfreq(len(x), d=1 / fs))
    magnitude = np.abs(np.fft.fftshift(np.fft.fft(x))) / len(x)
    return f, magnitude


def main(phase_unit=None):
    out = Path(__file__).parent / "figures"
    out.mkdir(exist_ok=True)
    if phase_unit is None:
        print("Exercise 3A pending: clarify +30 and supply --phase-unit radians or degrees.")
    else:
        t, x, fs = signal_a(phase_unit)
        f, magnitude = spectrum(x, fs)
        fig, ax = plt.subplots(figsize=(9, 4), layout="constrained")
        ax.plot(f, magnitude)
        ax.set(title=f"Exercise 3A: 128 samples, fs = 256 Hz, phase = 30 {phase_unit}",
               xlabel="Frequency (Hz)", ylabel="Magnitude |FFT| / N", xlim=(-128, 128))
        ax.grid(alpha=0.3)
        fig.savefig(out / "ex3a_spectrum.png", dpi=150)
        plt.close(fig)

    for frequencies, suffix in (((500, 1000, 1500, 2000), "low"),
                                ((18000, 18500, 19000, 19500), "high")):
        fig, axes = plt.subplots(2, 2, figsize=(11, 7), layout="constrained")
        fig.suptitle("Exercise 3B: fs = 20 kHz, N = 400, phase = 0 radians")
        for ax, f0 in zip(axes.flat, frequencies):
            n, x, fs = signal_b(f0)
            f, magnitude = spectrum(x, fs)
            ax.plot(f, magnitude)
            ax.set(title=f"Input frequency = {f0} Hz", xlabel="Frequency (Hz)",
                   ylabel="Magnitude |FFT| / N", xlim=(-2500, 2500), ylim=(0, 0.55))
            ax.grid(alpha=0.3)
        fig.savefig(out / f"ex3b_{suffix}.png", dpi=150)
        plt.close(fig)
    print("High-frequency aliases: 18000->2000, 18500->1500, 19000->1000, 19500->500 Hz.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase-unit", choices=("radians", "degrees"),
                        help="Explicit unit for Exercise 3A's printed +30")
    main(parser.parse_args().phase_unit)
