import numpy as np
N=20
X = np.zeros((N,N))
S= np.sqrt(2/N)
for n in range (0,N):
    for k in range (0,N):
        if(k==0):
            c=1/np.sqrt(2)
        else:
            c=1
        X[n][k] = S*c * np.cos(np.pi*k/N*(n+0.5))
for i in range(0,N-1):
    L= np.dot(X[i],X[i+1])
    print(round(L,8))
