#import numpy as np
#from scipy.optimize import curve_fit

#def func(x, a, b, c):
#    return a * np.exp(-b * x) + c
#xdata = np.linspace(0, 4, 50)
#y = func(xdata, 2.5, 1.3, 0.5)
#ydata = y + 0.2 * np.random.normal(size=len(xdata))
#popt, pcov = curve_fit(func, xdata, ydata)
#popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 2., 1.]))
#print popt, pcov

#import numpy as np
#from scipy.optimize import curve_fit

#xdata = np.array([-2,-1.64,-1.33,-0.7,0,0.45,1.2,1.64,2.32,2.9])
#ydata = np.array([0.699369,0.700462,0.695354,1.03905,1.97389,2.41143,1.91091,0.919576,-0.730975,-1.42001])

#def func(x, p1,p2):
#  return p1*np.cos(p2*x) + p2*np.sin(p1*x)

#popt, pcov = curve_fit(func, xdata, ydata)#,p0=(1.0,0.2))

#print popt

import numpy as np
from itertools import combinations
import scipy.linalg
x = [1.2, 1.3, 1.6, 2.5, 2.3, 2.8]
y = [167.0, 180.3, 177.8, 160.4, 179.6, 154.3]
z = [-0.3, -0.8, -0.75, -1.21, -1.65, -0.68]
f = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6]).transpose()

G = np.c_[x, y, z]

#A = np.concatenate((G, np.ones((G.shape[0],1))), axis=1)
#
C, _, _, _ = scipy.linalg.lstsq(A, f)
# C will have now the coefficients for:
# f(x, y, z) = ax + by + cz + d

# quadratic eq.
dim = G.shape[1]
A = np.concatenate((G**2, np.array([np.prod(G[:, k], axis=1) for k in combinations(range(dim), dim-1)]).transpose(), G, np.ones((G.shape[0], 1))), axis=1)
C, _, _, _ = scipy.linalg.lstsq(A, f)
# C will have now the coefficients for:
# f(x, y, z) = ax**2 + by**2 + cz**2 + dxy+ exz + fyz + gx + hy + iz + j

# This can be used then:
def quadratic(a):
    dim = a.shape[0]
    A = np.concatenate((a**2, np.array([np.prod(a[k,]) for k in combinations(range(dim), dim-1)]), a, [1]))
    return np.sum(np.dot(A, C))

for i in range(G.shape[0]):
    print(quadratic(G[i,:]), f[i])
