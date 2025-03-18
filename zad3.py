import numpy as np
import matplotlib.pyplot as plt

N=100
freq=1000
time=N/freq
A1=50
A2=100
A3=150
freq1=50 #52.5
freq2=100 #107  , 102.5
freq3=150 #152.5
t=np.linspace(0,time,N,endpoint=False)

sin1=A1*np.sin(2*np.pi*freq1*t)
sin2=A2*np.sin(2*np.pi*freq2*t)
sin3=A3*np.sin(2*np.pi*freq3*t)

x = sin1+sin2+sin3
#plt.plot(t,signal)


A = np.zeros((N,N))
S= np.sqrt(2/N)
for n in range (0,N):
    for k in range (0,N):
        if(k==0):
            c=1/np.sqrt(2)
        else:
            c=1
        A[n][k] = S*c * np.cos(np.pi*k/N*(n+0.5))

S=A.transpose()

# for i in range(N):
#     plt.figure()
#     plt.plot(A[i, :], label=f"A row {i}")
#     plt.plot(S[:, i], label=f"S column {i}")
#     plt.xlabel("Index")
#     plt.ylabel("Value")
#     plt.title(f"Row {i} of A and Column {i} of S")
#     plt.legend()
#     plt.grid()
#     plt.show()

y= A@x

plt.figure()
plt.plot(y)
plt.show()



f=np.linspace(0,freq ,N,endpoint=False)
plt.figure()
plt.plot(f,y)
plt.show()

f=np.arange(N)*freq/N/2
plt.figure()
plt.plot(f,y)
plt.show()


S = A.transpose()

#print(np.round(S@A,8))



x.transpose()
np.conj(x)
x_= A @ x
x_reconstructed = S@x_

reconstruction_error = x - x_reconstructed

print("Original signal:\n", x)
print("\nReconstructed signal:\n", x_reconstructed)
print("\nReconstruction error:",  np.round(reconstruction_error,8))
