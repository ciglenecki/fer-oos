# Uvezi potrebne funkcije u globalni imenik
# numpy mora biti učitan prvi tako da njegove funkcije ne prikriju funkcije iz scipy.signal i scipy.fft
import numpy as np
import scipy.signal as signal
import scipy.fft as fft
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)


def plot_dft_spectrum(spectrum: np.ndarray):
    amplitue = np.abs(spectrum)
    angle = np.angle(spectrum)
    angle_unwraped = np.unwrap(angle)

    plt.figure(figsize=(12, 6))

    plt.subplot(
        221, title="Amplitude $|X[k]|$", ylabel="Amplitude $|X[k]|$", xlabel="k"
    )
    plt.stem(amplitue, basefmt="")

    plt.subplot(
        222, title="Phase $\\angle X[k]$", ylabel="Phase $\\angle X[k]$", xlabel="k"
    )
    plt.stem(angle_unwraped)

    plt.subplot(223, title="Real $Re[X[k]]$", ylabel="Real $Re[X[k]]$", xlabel="k")
    plt.stem(np.real(spectrum))

    plt.subplot(224, title="Im $Im[X[k]]$", ylabel="Im $Im[X[k]]$", xlabel="k")
    plt.stem(np.imag(spectrum))

    plt.tight_layout()
    plt.show()


def plot_dtft_spectrum(spectrum: np.ndarray):
    amplitue = np.abs(spectrum)
    angle = np.angle(spectrum)
    angle_unwraped = np.unwrap(angle)

    plt.figure(figsize=(12, 6))

    plt.subplot(
        221,
        title="Amplitude $|X[k]|$",
        ylabel="Amplitude $|X[k]|$",
        xlabel="$\\omega [rad/s]$",
    )
    plt.plot(amplitue)

    plt.subplot(
        222,
        title="Phase $\\angle X[k]$",
        ylabel="Phase $\\angle X[k]$",
        xlabel="$\\omega [rad/s]$",
    )
    plt.plot(angle_unwraped)

    plt.subplot(
        223,
        title="Real $Re[X[k]]$",
        ylabel="Real $Re[X[k]]$",
        xlabel="$\\omega [rad/s]$",
    )
    plt.plot(np.real(spectrum))

    plt.subplot(
        224, title="Im $Im[X[k]]$", ylabel="Im $Im[X[k]]$", xlabel="$\\omega [rad/s]$"
    )
    plt.plot(np.imag(spectrum))

    plt.tight_layout()
    plt.show()


def sinus_discrete(
    omega: float = 1.0, phi: float = 0.0, amplitude: float = 1.0, samples=100
):
    n = np.arange(0.0, samples, 1.0)
    x = amplitude * np.sin(omega * n + phi)
    return x


def draw(x, title=""):
    plt.figure()
    plt.title(title)
    plt.plot(x)
    plt.stem(x)
    plt.show()


def draw2(xd, td, xc, tc):
    plt.figure()
    plt.plot(tc, xc)
    plt.stem(td, xd)
    plt.show()


pi = np.pi


def dtft(x: np.ndarray, sampling_freq: float, n: int = 100):
    """
    Args:
            x (x[n]): signal
            sampling_freq (K): sampling frequency, number of sampled points
            n (N): effective signal length, either cut or pad
        k: current frequency
    """

    if len(x) >= n:
        x = x[:n]
    else:
        """
        pad 0, don't pad at the beggining
        pad n - len(x) pad at the end so that x has n elements
        """
        x = np.pad(x, (0, n - len(x)))

    N = len(x)
    K = sampling_freq
    k = np.arange(sampling_freq).reshape(-1, 1)  # effectively bounded to [0, 1]
    e = np.exp(-2j * k * pi * np.arange(N) / sampling_freq)

    return np.dot(e, x)


def dft(x: np.ndarray, n: int = 100):
    return dtft(x, sampling_freq=n, n=n)


# Number of samplepoints
N = 30
# sample spaci2ng
T = 1 / 4
capture = 100


x = np.linspace(-N * T, N * T, N)
# x = x - np.mean(x)

print(x[:3], x[-3:])
print(x)
y = np.sinc(x) ** 2 * np.square(capture)

freq = np.fft.fftfreq(len(y), 25)

plt.figure()
plt.plot(freq, np.abs(y))
plt.figure()
plt.plot(freq, np.angle(y))
plt.show()
exit(1)


plt.plot(y)
print("Y:", y)
yf = np.abs(fft.fft(y))
plt.plot(yf)
print(yf)

xf = np.linspace(0, 1.0 / (2.0 * T), N // 2)


fig, ax = plt.subplots()
ax.plot(xf, np.abs(yf[: N // 2]))
plt.show()
