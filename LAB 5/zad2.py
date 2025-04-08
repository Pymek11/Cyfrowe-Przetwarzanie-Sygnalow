import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqs, lti, impulse, step

# Parameters
omega_3dB = 2 * np.pi * 100  # Cut-off frequency (rad/s)
orders = [2, 4, 6, 8]  # Filter orders
frequencies = np.linspace(1, 500, 1000)  # Frequency range

# Plot amplitude characteristics
plt.figure(figsize=(12, 6))
for N in orders:
    # Design Butterworth filter
    b, a = butter(N, omega_3dB, btype='low', analog=True)
    w, h = freqs(b, a, worN=2 * np.pi * frequencies)

    # Amplitude response
    plt.subplot(2, 1, 1)
    plt.plot(frequencies, 20 * np.log10(abs(h)), label=f'N={N}')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude (dB)')
    plt.title('Amplitude Response (Linear Scale)')
    plt.legend()
    plt.grid()

    # Amplitude response on logarithmic frequency scale
    plt.subplot(2, 1, 2)
    plt.semilogx(frequencies, 20 * np.log10(abs(h)), label=f'N={N}')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude (dB)')
    plt.title('Amplitude Response (Logarithmic Scale)')
    plt.legend()
    plt.grid()

plt.tight_layout()
plt.show()

# Phase characteristics
plt.figure(figsize=(12, 6))
for N in orders:
    b, a = butter(N, omega_3dB, btype='low', analog=True)
    w, h = freqs(b, a, worN=2 * np.pi * frequencies)

    # Phase response
    plt.plot(frequencies, np.angle(h), label=f'N={N}')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase (rad)')
    plt.title('Phase Response (Linear Scale)')
    plt.legend()
    plt.grid()

plt.tight_layout()
plt.show()

# Impulse and step responses for N=4
b, a = butter(4, omega_3dB, btype='low', analog=True)
system = lti(b, a)
t_impulse, x_impulse = impulse(system)
t_step, x_step = step(system)

plt.figure(figsize=(10, 5))
plt.plot(t_impulse, x_impulse, label='Impulse Response (N=4)')
plt.plot(t_step, x_step, label='Step Response (N=4)')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Impulse and Step Responses')
plt.legend()
plt.grid()

plt.show()
