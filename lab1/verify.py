"""Separate verification checks; not additional lab solution methods.

Run: python lab1/verify.py
"""

import unittest
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from fractions import Fraction

import numpy as np

import exercise1 as ex1
import exercise2 as ex2
import exercise3 as ex3


class Exercise1Checks(unittest.TestCase):
    def test_sequences_and_index_support(self):
        nx, x, ny, y = ex1.sequences()
        np.testing.assert_array_equal(nx, np.arange(-4, 5))
        np.testing.assert_array_equal(x, [14, 13, 12, 11, 10, 9, 8, 7, 6])
        np.testing.assert_array_equal(ny, np.arange(-2, 6))
        np.testing.assert_allclose(y, [1.25, 1, .8, .64, .512, .4096, .32768, .262144])
        self.assertEqual(nx[0] + ny[0], -6)
        self.assertEqual(nx[-1] + ny[-1], 9)

    def test_convolution_against_exact_arithmetic_and_numpy(self):
        nx, x, ny, y = ex1.sequences()
        # Exact rational evaluation using physical n,k indices, not float arrays.
        exact = [sum(Fraction(10 - k) * Fraction(4, 5) ** (n - k + 1)
                     for k in range(-4, 5) if -2 <= n - k <= 5)
                 for n in range(-6, 10)]
        z = ex1.convolution(x, y)
        self.assertEqual(len(z), 16)
        np.testing.assert_allclose(z, [float(v) for v in exact], rtol=1e-13, atol=1e-12)
        np.testing.assert_allclose(z, np.convolve(x, y), rtol=1e-13, atol=1e-12)
        self.assertAlmostEqual(z[0], 17.5)
        self.assertAlmostEqual(z[-1], 1.572864)
        self.assertAlmostEqual(z.sum(), x.sum() * y.sum())

    def test_convolution_identity_and_commutativity(self):
        np.testing.assert_allclose(ex1.convolution([1], [2, -3, 4]), [2, -3, 4])
        np.testing.assert_allclose(ex1.convolution([0, 1], [2, -3]), [0, 2, -3])
        _, x, _, y = ex1.sequences()
        np.testing.assert_allclose(ex1.convolution(x, y), ex1.convolution(y, x))

    def test_fft_product_and_inverse(self):
        _, x, _, y = ex1.sequences()
        z = ex1.convolution(x, y)
        product = np.fft.fft(x, 16) * np.fft.fft(y, 16)
        np.testing.assert_allclose(product, np.fft.fft(z), rtol=1e-12, atol=1e-10)
        np.testing.assert_allclose(np.fft.ifft(product), z, rtol=1e-12, atol=1e-12)

    def test_fft_against_physical_index_definition(self):
        nx, x, ny, y = ex1.sequences()
        z = ex1.convolution(x, y)
        nz = np.arange(-6, 10)
        for k in range(16):
            w = 2 * np.pi * k / 16
            X = sum(x * np.exp(-1j * w * nx))
            Y = sum(y * np.exp(-1j * w * ny))
            Z = sum(z * np.exp(-1j * w * nz))
            np.testing.assert_allclose(X * Y, Z, rtol=1e-11, atol=1e-10)

    def test_explicit_frequency_axis_and_normalization(self):
        _, x, _, y = ex1.sequences()
        z = ex1.convolution(x, y)
        # 1 Hz is the report convention; 20 Hz checks axis scaling independently.
        f1, m1 = ex1.spectra(x, y, z, 1)
        f20, m20 = ex1.spectra(x, y, z, 20)
        np.testing.assert_allclose(f20, 20 * f1)
        np.testing.assert_allclose(m20, m1)
        self.assertAlmostEqual(m1[0][8], x.sum() / 16)
        np.testing.assert_allclose(f1, np.arange(-8, 8) / 16, rtol=0, atol=1e-15)
        for n, values, magnitude in zip((np.arange(-4, 5), np.arange(-2, 6),
                                         np.arange(-6, 10)), (x, y, z), m1):
            direct = np.abs(np.exp(-2j * np.pi * f1[:, None] * n) @ values) / 16
            np.testing.assert_allclose(magnitude, direct, rtol=0, atol=1e-12)
        for fs in (0, -1, np.nan, np.inf):
            with self.assertRaises(ValueError):
                ex1.spectra(x, y, z, fs)


class Exercise2Checks(unittest.TestCase):
    def test_known_signal_values(self):
        np.testing.assert_allclose(ex2.signal(np.array([0, .1, .2, .3, .4])),
                                   [20, -60, 20, 20, 20], atol=1e-12)

    def test_open_intervals_and_sample_counts(self):
        for duration, counts in ((.5, (9, 4, 2)), (5, (99, 49, 24))):
            for fs, count in zip((20, 10, 5), counts):
                td = ex2.sample_times(duration, fs)
                self.assertEqual(len(td), count)
                self.assertTrue(np.all((td > 0) & (td < duration)))
                np.testing.assert_allclose(td * fs, np.arange(1, count + 1))

    def test_boundary_and_alias_sample_identities(self):
        for duration in (.5, 5):
            td = ex2.sample_times(duration, 5)
            np.testing.assert_allclose(ex2.signal(td), 20, atol=1e-11)
            td = ex2.sample_times(duration, 10)
            n = np.arange(1, len(td) + 1)
            expected = 20 * (-1.0) ** n - 40 * np.sin(np.pi * n / 2)
            np.testing.assert_allclose(ex2.signal(td), expected, atol=1e-11)

    def test_fft_magnitude_against_transform_sum(self):
        dt = .001
        t = ex2.sample_times(.5, 1 / dt)
        x = ex2.signal(t)
        F = np.fft.fftfreq(len(x), dt)
        X = np.fft.fft(x) * dt
        for k in (0, 1, 2, 10, len(x) - 1):
            direct = np.sum(x * np.exp(-2j * np.pi * F[k] * t)) * dt
            # Starting at t=dt changes phase, not the plotted magnitude.
            np.testing.assert_allclose(abs(X[k]), abs(direct), rtol=1e-12, atol=1e-12)


class Exercise3Checks(unittest.TestCase):
    def test_3a_magnitude_independent_of_phase_interpretation(self):
        _, radians, fs = ex3.signal_a("radians")
        _, degrees, _ = ex3.signal_a("degrees")
        self.assertFalse(np.allclose(radians, degrees))  # Samples do change.
        f_rad, mag_rad = ex3.spectrum(radians, fs)
        f_deg, mag_deg = ex3.spectrum(degrees, fs)
        np.testing.assert_array_equal(f_rad, f_deg)
        np.testing.assert_allclose(mag_rad, mag_deg, rtol=0, atol=1e-12)

    def test_phase_choice_required(self):
        for unit in (None, "", "unknown"):
            with self.assertRaises(ValueError):
                ex3.signal_a(unit)

    def test_both_phase_interpretations_and_exact_bins(self):
        for unit, phase in (("radians", 30), ("degrees", np.pi / 6)):
            t, x, fs = ex3.signal_a(unit)
            self.assertEqual(len(x), 128)
            self.assertGreater(fs, 120)
            np.testing.assert_allclose(np.diff(t), 1 / fs)
            self.assertAlmostEqual(x[0], 12 - 18 * np.sin(phase))
            f, mag = ex3.spectrum(x, fs)
            for freq, amplitude in ((-60, 9), (-20, 6), (20, 6), (60, 9)):
                self.assertAlmostEqual(mag[f == freq][0], amplitude, places=11)
            other = ~np.isin(f, [-60, -20, 20, 60])
            self.assertLess(np.max(mag[other]), 1e-11)

    def test_all_eight_spectra(self):
        frequencies = (500, 1000, 1500, 2000, 18000, 18500, 19000, 19500)
        aliases = (500, 1000, 1500, 2000, 2000, 1500, 1000, 500)
        for f0, alias in zip(frequencies, aliases):
            n, x, fs = ex3.signal_b(f0)
            self.assertEqual(len(n), 400)
            self.assertEqual(fs, 20000)
            f, mag = ex3.spectrum(x, fs)
            np.testing.assert_allclose(mag[np.abs(f) == alias], .5, atol=1e-12)
            self.assertLess(np.max(mag[np.abs(f) != alias]), 1e-12)

    def test_alias_sign_and_general_phase(self):
        for high, low in ((18000, 2000), (18500, 1500), (19000, 1000), (19500, 500)):
            for phase in (0, .3, -1.2):
                n, high_signal, fs = ex3.signal_b(high, phase)
                expected = np.sin(phase - 2 * np.pi * low * n / fs)
                np.testing.assert_allclose(high_signal, expected, atol=1e-12)

    def test_spectrum_normalization_parseval(self):
        _, x, fs = ex3.signal_b(1500)
        _, mag = ex3.spectrum(x, fs)
        self.assertAlmostEqual(np.sum(mag ** 2), np.mean(x ** 2), places=12)


class FigureRerunChecks(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        for name in ("exercise1.py", "exercise3.py"):
            shutil.copy2(Path(__file__).parent / name, self.root / name)

    def run_script(self, name, *args):
        result = subprocess.run(
            [sys.executable, str(self.root / name), *args], cwd=self.root,
            env=dict(os.environ, MPLBACKEND="Agg"), capture_output=True, text=True,
            timeout=60,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout

    def test_default_1b_restores_report_scale_and_preserves_other_files(self):
        self.run_script("exercise1.py", "--fs", "1")
        figure = self.root / "figures/ex1_spectra.png"
        self.assertTrue(figure.is_file())
        default_png = figure.read_bytes()
        unrelated = self.root / "figures/teammate-notes.txt"
        unrelated.write_text("Keep this file.")
        self.run_script("exercise1.py", "--fs", "20")
        self.assertNotEqual(figure.read_bytes(), default_png)
        output = self.run_script("exercise1.py")
        self.assertIn("Exercise 1B: fs = 1 Hz", output)
        self.assertEqual(figure.read_bytes(), default_png)
        self.assertEqual(unrelated.read_text(), "Keep this file.")
        self.assertTrue((self.root / "figures/ex1_convolution.png").is_file())

    def test_default_3a_replaces_previous_phase_output(self):
        output = self.run_script("exercise3.py")
        self.assertIn("phase = 30 radians", output)
        figure = self.root / "figures/ex3a_spectrum.png"
        default_png = figure.read_bytes()
        self.run_script("exercise3.py", "--phase-unit", "degrees")
        # Same magnitudes to numerical precision; the labelled convention differs.
        self.assertNotEqual(figure.read_bytes(), default_png)
        output = self.run_script("exercise3.py")
        self.assertNotIn("pending", output)
        self.assertEqual(figure.read_bytes(), default_png)


if __name__ == "__main__":
    unittest.main(verbosity=2)
