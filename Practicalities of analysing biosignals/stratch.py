# coding: utf-8
import numpy
import h5py
import numpy as np
np.read
np.loadtxt('data/ecg_101.txt')
a = np.loadtxt('data/ecg_101.txt')
a
a.shape
import matplotlib
import matplotlib.pyplot as plt
plt(a[0], a[1])
plt.plot(a[0], a[1])
plt.show()
a[0]
a[]
a[1]
get_ipython().magic('pinfo plt.plot')
plt.plot(a[1])
plt.show()
plt.plot(a[0])
plt.show()
a
a[0]
a[0][0]
a[;0]
a[,0]
a[,:]
a[:,]
a.shape
a[0][:]
a[0][:,]
a[0][,:]
a[0]
np.loadtxt('data/ecg_101.txt')?
np.loadtxt(?
get_ipython().magic('pinfo np.loadtxt')
a
a[1]
np.loadtxt('data/ecg_101.txt', usecols=(1,))
ecg = np.loadtxt('data/ecg_101.txt', usecols=(1,))
samples = np.loadtxt('data/ecg_101.txt', usecols=(0,))
plt.plot(samples, ecg)
plt.show()
ecg
ecg.shape
ecg /12
ecg.shape /12
ecg.shape / 12
ecg.shape[0] / 12
plt.plot(samples[:2048], ecg[:2048])
plt.show()
get_ipython().magic('clear ')
np.loadtxt('data/ecgsyn.dat')
samples = np.loadtxt('data/ecgsyn.dat', usecols=0)
samples = np.loadtxt('data/ecgsyn.dat', usecols=(0))
samples = np.loadtxt('data/ecgsyn.dat', usecols=(0,))
ecg = np.loadtxt('data/ecgsyn.dat', usecols=(1,))
plt.plot(samples[:2048], ecg[:2048])
plt.show
plt.show()
noisy = ecg[:2048] * np.random.randn
noisy = ecg[:2048] * np.random.randn()
noisy
plt.plot(samples[:2048], noisy)
plt.show
plt.show()
noisy = ecg[:2048] + np.random.randn()
plt.plot(samples[:2048], noisy)
plt.show()
np.random.randn()
np.random.randn()
np.random.randn()
np.random.randn()
ecg[:10
]
noisy = ecg[:2048] + np.random.randn()
noisry
noisy
ecg
plt.plot(samples[:2048], noisy)
noisy
plt.show()
noisy = ecg[:2048] + np.random.randn()*3
plt.plot(samples[:2048], noisy)
plt.show()
noise = np.random.normal(0,1,2048)
noisy = ecg[:2048] + noise
plt.plot(samples[:2048], noisy)
plt.show()
noise
noise = noise / 10
noise
noisy = ecg[:2048] + noise
plt.plot(samples[:2048], noisy)
plt.show()
import h5py
f = h5py.File("ecg.hdf5", "w")
ecg
ecg.shape
dataset = f.create_dataset("Normal ECG", (65772,), dtype='f')
dataset
dataset = ecg
dataset
dataset = f.create_dataset("Normal ECG", (65772,2), dtype='f')
get_ipython().magic('ls ')
get_ipython().magic('ls data/')
samples = f.create_dataset("Samples", (65772,), dtype='f')
samples = np.loadtxt('data/ecgsyn.dat', usecols=(0,))
samples
f
f.close()
