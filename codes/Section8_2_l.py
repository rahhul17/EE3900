import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal
from scipy import vectorize as vec
import numpy as np

#read .wav file 
input_signal,fs = sf.read('./files/Sound_Noise.wav') 

#sampling frequency of Input signal
sampl_freq = fs

#order of the filter
order1 = 7 

#cutoff frquency 4kHz
cutoff_freq = 4000.0  

#digital frequency
Wn = 2*cutoff_freq/sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order1, Wn, 'low') 

# get partial fraction expansion
r, p, k = signal.residuez(b, a)

#number of terms of the impulse response
sz1 = 50
sz_lin = np.arange(sz1)

def rp(x):
    return r@(p**x).T

rp_vec = vec(rp, otypes=['double'])

h1 = rp_vec(sz_lin)
k_add = np.pad(k, (0, sz1 - len(k)), 'constant', constant_values=(0,0))
h = h1 + k_add

#subplots
plt.subplot(3, 1, 1)
plt.stem(sz_lin, h)
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid()
plt.plot()

#order of the filter
order2 = 4  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order2, Wn, 'low') 

#DTFT
def H(z):
	num = np.polyval(b,z**(-1))
	den = np.polyval(a,z**(-1))
	H = num/den
	return H
		
#Input and Output
omega = np.linspace(0,np.pi,100)

plt.subplot(3, 1, 2)
plt.plot(omega, abs(H(np.exp(1j*omega))))
plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{\jmath\omega})| $')
plt.grid()

#order of the filter
order3 = 7 

#number of terms of the impulse response
sz2 = 64
sz_lin = np.arange(sz2)

dftmtx = np.fft.fft(np.eye(sz2))
invmtx = np.linalg.inv(dftmtx)
def rp(x):
    return r@(p**x).T

rp_vec = vec(rp, otypes=['double'])

h1 = rp_vec(sz_lin)
k_add = np.pad(k, (0, sz2 - len(k)), 'constant', constant_values=(0,0))
h = h1 + k_add
H = h@dftmtx
X = input_signal[:sz2]@dftmtx
Y = H*X
y = (Y@invmtx).real

plt.subplot(3, 1, 3)
plt.stem(np.arange(sz2), y[:sz2])
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid()
plt.plot()
plt.gcf().set_size_inches(10, 12)
plt.savefig('./figs/section8.png')