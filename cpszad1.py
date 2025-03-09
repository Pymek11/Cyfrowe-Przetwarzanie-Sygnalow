import numpy as np

import matplotlib.pyplot as plt
import matplotlib
from scipy.signal import periodogram
frequency =50
AMPL= 230
duration = 0.1
freq1=10000
freq2=500
freq3=200

t1=np.linspace(0, duration, int(duration*freq1))
t2=np.linspace(0, duration, int(duration*freq2))
t3=np.linspace(0, duration, int(duration*freq3))

sin1 = AMPL*np.sin(2*np.pi*frequency*t1)
sin2 = AMPL*np.sin(2*np.pi*frequency*t2)
sin3 = AMPL*np.sin(2*np.pi*frequency*t3)

plt.plot(t1, sin1, 'b-')  
plt.plot(t2, sin2, 'r-o')
plt.plot(t3, sin3, 'k-x')  


duration =1

freq1=10000
freq2=51
freq3=50
freq4=49

t4=np.linspace(0, duration, int(duration*freq1))
t5=np.linspace(0, duration, int(duration*freq2))
t6=np.linspace(0, duration, int(duration*freq3))
t7=np.linspace(0 ,duration, int(duration*freq4))

#sin4 = AMPL*np.sin(2*np.pi*frequency*t4)
sin5 = AMPL*np.sin(2*np.pi*frequency*t5)
sin6 = AMPL*np.sin(2*np.pi*frequency*t6)
sin7 = AMPL*np.sin(2*np.pi*frequency*t7)

plt.figure()

#plt.plot(t4, sin4, 'b-')  
plt.plot(t5, sin5, 'g-o')
plt.plot(t6, sin6, 'r-o')
plt.plot(t7, sin7, 'k-o')
  
freq1=10000
freq2=26
freq3=25
freq4=24

#t4=np.linspace(0, duration, int(duration*freq1))
t5=np.linspace(0, duration, int(duration*freq2))
t6=np.linspace(0, duration, int(duration*freq3))
t7=np.linspace(0 ,duration, int(duration*freq4))

#sin4 = AMPL*np.sin(2*np.pi*frequency*t4)
sin5 = AMPL*np.sin(2*np.pi*frequency*t5)
sin6 = AMPL*np.sin(2*np.pi*frequency*t6)
sin7 = AMPL*np.sin(2*np.pi*frequency*t7)

plt.figure()

#plt.plot(t4, sin4, 'b-')  
plt.plot(t5, sin5, 'g-o')
plt.plot(t6, sin6, 'r-o')
plt.plot(t7, sin7, 'k-o')  


freq = 100


t= np.linspace(0,1,freq*1)
sinuses=[]
for i in range(0,301,5):
    sin = np.sin(2*np.pi*i*t)
    sinuses.append(sin)
    plt.figure()
    plt.plot(t,sin,label = f'freq = {i} Hz ,i = {i/5}')
    plt.legend()

plt.figure()
plt.plot(t, sinuses[1], label="5Hz, i = 1")
plt.plot(t, sinuses[21], label="105Hz, i = 21")
plt.plot(t, sinuses[41], label="205Hz, i = 41")
plt.legend()

plt.figure()
plt.plot(t, sinuses[19], label="95Hz, i = 19")
plt.plot(t, sinuses[39], label="195Hz, i = 39")
plt.plot(t, sinuses[59], label="295Hz, i = 59")
plt.legend()

plt.figure()
plt.plot(t, sinuses[19], label="95Hz, i = 19")
plt.plot(t, sinuses[21], label="105Hz, i = 21")
plt.legend()
cosinuses=[]
for i in range(0,301,5):
    cos = np.cos(2*np.pi*i*t)
    cosinuses.append(cos)
    plt.figure()
    plt.plot(t,cos,label = f'freq = {i} Hz ,i = {i/5}')
    plt.legend()
    
plt.figure()
plt.plot(t, cosinuses[1], label="5Hz, i = 1")
plt.plot(t, cosinuses[21], label="105Hz, i = 21")
plt.plot(t, cosinuses[41], label="205Hz, i = 41")
plt.legend()

plt.figure()
plt.plot(t, cosinuses[19], label="95Hz, i = 19")
plt.plot(t, cosinuses[39], label="195Hz, i = 39")
plt.plot(t, cosinuses[59], label="295Hz, i = 59")
plt.legend()

plt.figure()
plt.plot(t, cosinuses[19], label="95Hz, i = 19")
plt.plot(t, cosinuses[21], label="105Hz, i = 21")
plt.legend()


freq_s = 10000
freq_n = 50
freq_m = 1
depth_m = 5

t = np.linspace(0,1,freq_s)
sygnal_mod = depth_m*np.sin(2*np.pi*freq_m*t)
syg_zmod = np.sin(2*np.pi*freq_n*t + sygnal_mod)
sygnal = np.sin(2*np.pi*freq_n*t)


plt.figure()
plt.plot(t,syg_zmod,label="sygnal zmodulowany")
#plt.plot(t,sygnal_mod,label="sygnal modulujacy")
plt.plot(t,sygnal,label="sygnal przed")
plt.legend()


freq_s = 10000
freq_n = 50
freq_m = 1
depth_m = 5

t = np.linspace(0,1,freq_s)
sygnal_mod = depth_m*np.sin(2*np.pi*freq_m*t)
syg_zmod = np.cos(2*np.pi*freq_n*t + sygnal_mod)
sygnal = np.cos(2*np.pi*freq_n*t)


plt.figure()
plt.plot(t,syg_zmod,label="sygnal zmodulowany")
#plt.plot(t,sygnal_mod,label="sygnal modulujacy")
plt.plot(t,sygnal,label="sygnal przed")
plt.legend()

## 

freq_p = 25

t2 = np.linspace(0,1,freq_p)

sygnal_mod2 = depth_m*np.sin(2*np.pi*freq_m*t2)
syg_zmod2 = np.cos(2*np.pi*freq_n*t2 + sygnal_mod2)
sygnal2 = np.cos(2*np.pi*freq_n*t2)
error = syg_zmod - np.interp(t, t2, syg_zmod2)
plt.figure()
plt.plot(t2,syg_zmod2,label="sygnal zmodulowany 25Hz")
plt.plot(t,syg_zmod,label="sygnal zmodulowany")
plt.plot(t,error,label="bledy")
plt.legend()

freq1, power1 = periodogram(syg_zmod,10000)
freq2, power2 = periodogram(syg_zmod2,25)

plt.figure()
plt.xlim(0,100)
plt.plot(freq1,power1,label="MOC zmodulowany 10kHz")
plt.legend()
plt.figure()
plt.xlim(0,12)
plt.plot(freq2,power2,label="MOC zmodulowany 25Hz")
plt.legend()
