import numpy as np
import matplotlib.pyplot as plt
import matplotlib


ampl = 230
freq =50 
duration = 1
fs = 200

t = np.linspace(0,duration,duration*fs)
sin = ampl *np.sin(2*np.pi*freq*t)

freq2 =10000
t2 = np.linspace(0,duration, duration*freq2)

t_size = len(t2)
reconstructed_signal = np.zeros(t_size)  
Ts = 1/fs

for i in range (t_size):
    t_rec = t2[i]
    reconstructed_signal[i] = np.sum(sin * np.sinc((t_rec - t) / Ts))
    
sinus_analog= ampl* np.sin(2*np.pi*freq*t2)

error = sinus_analog - reconstructed_signal

plt.figure(figsize=(10, 5))
plt.plot(t2, sinus_analog, 'b', label='Oryginalny sygnał (pseudo-analogowy)')
plt.plot(t2, reconstructed_signal, 'r', linestyle='dashed', label='Zrekonstruowany sygnał')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.legend()
plt.title('Porównanie sygnałów')
plt.grid()
plt.show()

# Wykres błędu rekonstrukcji
plt.figure(figsize=(10, 3))
plt.plot(t2, error, 'k', label='Błąd rekonstrukcji')
plt.xlabel('Czas [s]')
plt.ylabel('Błąd')
plt.legend()
plt.title('Błąd rekonstrukcji')
plt.grid()
plt.show()
