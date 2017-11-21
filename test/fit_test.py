import numpy as np
import itertools
import matplotlib.pyplot as plt

def main():
    # Generate Data...
#    numdata = 100
#    x = np.random.random(numdata)
    # X array
#    y = np.random.random(numdata)
#    z = x**2 + y**2
    data_raw = np.zeros((100,100))
    file = open("data.dat", "r")
    content = [x.rstrip("\n") for x in file]
    data_raw = np.array([x.split()[:5] for x in content[:]])
    data = np.zeros(data_raw.shape)
    #print data
    for i in range(data_raw.shape[0]):
        for j in range(data_raw.shape[1]):
            data[i,j] = float(data_raw[i,j])
    #print float(data[0,0])+float(data[0,1])
    x = data[:,0]
    y = data[:,1]
    z = data[:,3]
    z_axis = data[:,2]


    # Fit a 3rd order, 2d polynomial
    m = polyfit2d(x,y,z)


    # Evaluate it on a grid...
    nx, ny = 100, 100
    #print x.min(), x.max(),  y.min(), y.max()
    xx, yy = np.meshgrid(np.linspace(x.min(), x.max(), nx),
                         np.linspace(y.min(), y.max(), ny))
    zz = polyval2d(xx, yy, m)

    # Plot
    plt.imshow(zz, extent=(x.min()-0.2, y.max()+0.2, x.max()+0.2, y.min()-0.2))
    # Some times withou 0.5 would fail
    plt.scatter(x, y, c=z)
    plt.show()

def polyfit2d(x, y, z, order=2):
    ncols = (order + 1)**2
    G = np.zeros((x.size, ncols))
    ij = itertools.product(range(order+1), range(order+1))
    # Generate polynomial function matrix
    for k, (i,j) in enumerate(ij):
    # Using enumerate to add coefficients fo mattix
        if k < 7 and k != 5:
        # Using quadratic function: a*x^2+b*x^2+c*x*y+d*x+e*y+f as fitting function
            G[:,k] = x**i * y**j
    m, _, _, _ = np.linalg.lstsq(G, z)
    # I don't fully understand this, supposely a matirx trick.
    print "Fitted result:", m[6],"*x^2+",m[2],"*y^2+",m[4],"*x*y+",m[3],"*x+",m[1],"*y+",m[0],"\n"
    #a=m[6],b=m[2],c=m[4],d=m[3],e=m[1],f=m[0]
    print "Minimum located: x=",-(2*m[2]*m[3]-m[4]*m[1])/(4*m[6]*m[2]-m[4]*m[4])," y=",-(m[4]*m[3]-2*m[6]*m[1])/(-4*m[6]*m[2]+m[4]*m[4])
    # Print the result
    return m

def polyval2d(x, y, m):
    order = int(np.sqrt(len(m))) - 1
    ij = itertools.product(range(order+1), range(order+1))
    z = np.zeros_like(x)
    for a, (i,j) in zip(m, ij):
        z += a * x**i * y**j
        # Using =+ to add up all term
    return z

main()
