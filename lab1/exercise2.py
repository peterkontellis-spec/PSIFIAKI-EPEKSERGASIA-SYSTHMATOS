"""Exercise 2: plot the given signal, its spectrum and its samples."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def signal(t):
    return 20 * np.cos(10 * np.pi * t) - 40 * np.sin(5 * np.pi * t)


def sample_times(duration, fs):
    # duration is in seconds and fs in Hz; exclude both interval endpoints.
    n = np.arange(1, int(np.ceil(duration * fs)))
    return n / fs


def main():
    out = Path(__file__).parent / "figures"
    out.mkdir(exist_ok=True)
    dt = 0.001  # 1 ms grid for plotting the continuous-time signal.
    t = sample_times(0.5, 1 / dt)
    x = signal(t)
    # Multiplication by dt approximates the continuous Fourier integral.
    f = np.fft.fftshift(np.fft.fftfreq(len(t), d=dt))
    X = np.fft.fftshift(np.fft.fft(x)) * dt
    fig, axes = plt.subplots(2, 1, figsize=(9, 7), layout="constrained")
    axes[0].plot(t, x)
    axes[0].set(title="Exercise 2A: x(t), 0 < t < 0.5 s",
                xlabel="Time (s)", ylabel="Amplitude")
    axes[1].plot(f, np.abs(X), ".-")
    axes[1].set(title="Exercise 2B: finite-record magnitude spectrum (dt = 1 ms)",
                xlabel="Frequency (Hz)", ylabel="|FFT(x) dt|", xlim=(-20, 20))
    for ax in axes:
        ax.grid(alpha=0.3)
    fig.savefig(out / "ex2_signal_spectrum.png", dpi=150)
    plt.close(fig)

    # Compare the continuous curve with its samples over 0.5 s and 5 s.
    for duration, suffix in ((0.5, "0p5s"), (5.0, "5s")):
        t = sample_times(duration, 1 / dt)
        fig, axes = plt.subplots(3, 1, figsize=(10, 9), layout="constrained")
        for ax, fs in zip(axes, (20, 10, 5)):
            td = sample_times(duration, fs)  # Sampling instants t = n/fs.
            ax.plot(t, signal(t), label="Original signal (fine plotting grid)")
            ax.plot(td, signal(td), "ro", markersize=4, label=f"Samples: fs = {fs} Hz")
            ax.set(title=f"Exercise 2C: Ts = 1/{fs} s, 0 < t < {duration:g} s",
                   xlabel="Time (s)", ylabel="Amplitude", xlim=(0, duration),
                   ylim=(-70, 60))
            ax.legend(loc="upper right", fontsize=8)
            ax.grid(alpha=0.3)
        fig.savefig(out / f"ex2_sampling_{suffix}.png", dpi=150)
        plt.close(fig)
    print("Components: 5 Hz and 2.5 Hz. Nyquist sampling rate: 10 Hz.")
    print("At fs = 5 Hz all exact samples are 20; the original cannot be recovered.")


if __name__ == "__main__":
    main()
