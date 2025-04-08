import numpy as np
import matplotlib.pyplot as plt

# Define the poles and zeros
poles = [-0.5 + 9.5j, -0.5 - 9.5j, 10j, -10j, -0.5 + 10.5j, -0.5 - 10.5j]
zeros = [5j, -5j, 15j, -15j]

# Convert poles and zeros into polynomials
numerator = np.poly(zeros)  # Polynomial for zeros
denominator = np.poly(poles)  # Polynomial for poles

# Define the transfer function
omega = np.linspace(0, 20, 500)  # Frequency range
H = np.polyval(numerator, 1j * omega) / np.polyval(denominator, 1j * omega)

# Amplitude characteristics
amplitude = np.abs(H)
amplitude_db = 20 * np.log10(amplitude)

# Phase characteristics
phase = np.angle(H)

# Plot zeros and poles on the complex plane
plt.figure()
plt.scatter(np.real(zeros), np.imag(zeros), label='Zeros', color='blue', marker='o')
plt.scatter(np.real(poles), np.imag(poles), label='Poles', color='red', marker='x')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid()
plt.title('Zeros and Poles')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.legend()
plt.show()

# Plot amplitude and decibel characteristics
plt.figure()
plt.plot(omega, amplitude, label='|H(jω)|')
plt.plot(omega, amplitude_db, label='20log10|H(jω)|')
plt.title('Amplitude-Frequency Characteristics')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()

# Plot phase characteristics
plt.figure()
plt.plot(omega, phase)
plt.title('Phase-Frequency Characteristics')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (radians)')
plt.grid()
plt.show()

