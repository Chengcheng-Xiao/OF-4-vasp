import numpy as np
import itertools
import matplotlib.pyplot as plt

def main():
    # Generate Data...
    numdata = 100
    x = np.random.random(numdata)
    y = np.random.random(numdata)
    z = x**2 + y**2 + np.random.random(numdata)

    # Fit a 3rd order, 2d polynomial
    m = polyfit2d(x,y,z)
    #print m


    # Evaluate it on a grid...
    nx, ny = 20, 20
    xx, yy = np.meshgrid(np.linspace(x.min(), x.max(), nx),
                         np.linspace(y.min(), y.max(), ny))
    zz = polyval2d(xx, yy, m)

    # Plot
    plt.imshow(zz, extent=(x.min(), y.max(), x.max(), y.min()))
    plt.scatter(x, y, c=z)
    plt.show()

def polyfit2d(x, y, z, order=2):
    ncols = (order + 1)**2
    G = np.zeros((x.size, ncols))
    ij = itertools.product(range(order+1), range(order+1))
    for k, (i,j) in enumerate(ij):
        if k < 7 and k != 5:
            G[:,k] = x**i * y**j
    m, _, _, _ = np.linalg.lstsq(G, z)
    print "Fitted result:", m[6],"*x^2+",m[2],"*y^2+",m[4],"*x*y+",m[3],"*x+",m[1],"*y+",m[0]
    return m

def polyval2d(x, y, m):
    order = int(np.sqrt(len(m))) - 1
    ij = itertools.product(range(order+1), range(order+1))
    z = np.zeros_like(x)
    for a, (i,j) in zip(m, ij):
        z += a * x**i * y**j
    return z

main()

