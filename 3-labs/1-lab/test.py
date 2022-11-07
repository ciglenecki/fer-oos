import numpy as np
pi = np.pi

def sinus_discrete2(omega: float = 1.0, samples: int = 100, time_step: float = 1.0, phi: float = 0.0, amplitue: float = 1.0, minimum_samples_per_sampling_period: int = 10):
  time_continuous_num = 0.1 * time_step
  
  limit = pi / omega / minimum_samples_per_sampling_period
  if limit< time_continuous_num:
    time_continuous_num = limit
    
  t_max = time_step * samples
  
  td = np.arange(0.0, t_max, time_step)
  xd = amplitue * np.sin(omega * td + phi)
  
  tc = np.arange(0.0, t_max, time_continuous_num)
  xc = amplitue * np.sin(omega * tc + phi)
  return xd, td, xc, tc
xd, td, xc, tc = sinus_discrete2(omega=2*pi, samples=15, time_step=0.05)

def DFT(x):
    """
    Function to calculate the 
    discrete Fourier Transform 
    of a 1D real-valued signal x
    """

    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    print(e)
    print("n", n)
    print("k", k)
    X = np.dot(e, x)
    
    return X

# sampling rate
sr = 100
# sampling interval
ts = 1.0/sr
t = np.arange(0,1,ts)

freq = 1.
x = 3*np.sin(2*np.pi*freq*t)

freq = 4
x += np.sin(2*np.pi*freq*t)

freq = 7   
x += 0.5* np.sin(2*np.pi*freq*t)
print(DFT(xd))