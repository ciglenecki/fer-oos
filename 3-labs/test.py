import scipy as sci
import scipy.signal

tf = scipy.signal.zpk2tf([-1/3, 1/3], [-3, 3], 1)
print(tf)
