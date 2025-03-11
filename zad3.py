import numpy as np
import scipy.io as scipy
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

adsl = scipy.loadmat("adsl_x(1).mat")
x = adsl["x"].flatten()

M = 32
N = 512
K= 4
y = np.arange(0, 2080, 1)

def compute_correlation():
    for i in range(K):
        prefix = x[(i+1)*N - M-1:(i+1)*N-1]
        correlation = np.correlate(x, prefix, mode="full")
        threshold = max(correlation) * 0.99
        plt.plot(y,correlation)
        plt.show()
        peaks = find_peaks(correlation, threshold)
        peak_x = peaks[0]-M+1
        print(peak_x)

compute_correlation()
