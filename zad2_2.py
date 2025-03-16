import numpy as np

N=20
A = np.zeros((N,N))
S= np.sqrt(2/N)
for n in range (0,N):
    for k in range (0,N):
        if(k==0):
            c=1/np.sqrt(2)
        else:
            c=1
        A[n][k] = S*c * np.cos(np.pi*k/N*(n+0.5))


S = A.transpose()

#print(np.round(S@A,8))


x= np.random.randn(N)
x.transpose()
np.conj(x)
x_= A @ x
x_reconstructed = S@x_

reconstruction_error =np.linalg.norm(x - x_reconstructed)

print("Original signal:\n", x)
print("\nReconstructed signal:\n", x_reconstructed)
print("\nReconstruction error:",  round(reconstruction_error,8))
