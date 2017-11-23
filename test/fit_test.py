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
    z = data[:,2]

    dimension_x = 0
    dimension_y = 0
    dimension_z = 0
    if data[0,0] == data[-1,0]:
        print "x axis same"
        dimension_x = 1
    elif data[0,1] == data[-1,1]:
        print "y axis same"
        dimension_y = 1
    elif data[0,2] == data[-1,2]:
        print "z axis same"
        dimension_z = 1

    dimension = dimension_x+dimension_y+dimension_z
    if dimension == 1:
        print "2D_material\n"
    elif dimension == 2:
        print "1D_material\n"
    elif dimension == 0:
        print "3D material\n"

    eneg = data[:,3]


    # Fit a 3rd order, 2d polynomial
    m = polyfit2d(x,y,z,eneg, dimension_x, dimension_y, dimension_z)


    # Evaluate it on a grid...
    #nx, ny = 100, 100
    #print x.min(), x.max(),  y.min(), y.max()
    #xx, yy = np.meshgrid(np.linspace(x.min(), x.max(), nx),
    #                     np.linspace(y.min(), y.max(), ny))
    #zz = polyval2d(xx, yy, m)

    # Plot
    #plt.imshow(zz, extent=(x.min()-0.2, y.max()+0.2, x.max()+0.2, y.min()-0.2))
    # Some times withou 0.5 would fail
    #plt.scatter(x, y, c=z)
    #plt.show()

def polyfit2d(x, y, z, eneg, dimension_x, dimension_y, dimension_z, order=2):
    ncols = (order + 1)**3
    G = np.zeros((x.size, ncols))
    ijq = itertools.product(range(order+1), range(order+1), range(order+1))
    # Generate polynomial function matrix
    for k, (i,j,q) in enumerate(ijq):
    # Using enumerate to add coefficients fo mattix
        if k < 5 or k == 6 or k==9 or k==10 or k==12 or k==18:
        # Using quadratic function: a*x^2+b*x^2+c*x*y+d*x+e*y+f as fitting function
            G[:,k] = x**i * y**j * z**q
    m, _, _, _ = np.linalg.lstsq(G, eneg)
    # I don't fully understand this, supposely a matirx trick.
    if dimension_x == 0 and dimension_y == 0 and dimension_z == 0:
        print "Fitted result:", m[18],"*x^2+",m[6],"*y^2+",m[2],"*z^2+",m[12],"*x*y+",m[10],"*x*z+",m[4],"*y*z+",m[9],"*x+",m[3],"*y+",m[1],"*z+",m[0],"\n"
        a = m[18]
        b = m[6]
        c = m[2]
        d = m[12]
        e = m[10]
        f = m[4]
        g = m[9]
        h = m[3]
        i = m[1]
        j = m[0]
        print "Minimum located: x=",-(4*b*c*g-f**2*g-2*c*d*h+e*f*h-2*b*e*i+d*f*i)/(2*(4*a*b*c-c*d**2-b*e**2+d*e*f-a*f**2))," y=",-(2*c*d*g-e*f*g-4*a*c*h+e**2*h-d*e*i+2*a*f*i)/(2*(-4*a*b*c+c*d**2+b*e**2-d*e*f+a*f**2))," z=",-(2*b*e*g-d*f*g-d*e*h+2*a*f*h-4*a*b*i+d**2*i)/(2*(-4*a*b*c+c*d**2+b*e**2-d*e*f+a*f**2))

    elif dimension_x == 1 and dimension_y == 0 and dimension_z == 0:
        print "Fitted result:", m[6],"*y^2+",m[2],"*z^2+",m[4],"*y*z+",m[12]*x[0]+m[3],"*y+",m[10]*x[0]+m[1],"*z+", m[18]*x[0]**2+m[9]*x[0]+m[0],"\n"
        a = m[6]
        b = m[2]
        c = m[4]
        d = m[12]*x[0]+m[3]
        e = m[10]*x[0]+m[1]
        f = m[18]*x[0]**2+m[9]*x[0]+m[0]
        print "Minimum located: y=",-(2*b*d-c*e)/(4*a*b-c**2)," z=",-(c*d-2*a*e)/(-4*a*b+c**2)

    elif dimension_x == 0 and dimension_y == 1 and dimension_z == 0:
        print "Fitted result:", m[18],"*x^2+",m[2],"*z^2+",m[10],"*x*z+",m[12]*y[0]+m[9],"*x+",m[4]*y[0]+m[1],"*z+",m[6]*y[0]**2+m[3]*y[0]+m[0],"\n"
        a = m[18]
        b = m[6]
        c = m[10]
        d = m[12]*y[0]+m[9]
        e = m[4]*y[0]+m[1]
        f = m[6]*y[0]**2+m[3]*y[0]+m[0]
        print "Minimum located: x=",-(2*b*d-c*e)/(4*a*b-c**2)," z=",-(c*d-2*a*e)/(-4*a*b+c**2)

    elif dimension_x == 0 and dimension_y == 0 and dimension_z == 1:
        print "Fitted result:", m[18],"*x^2+",m[6],"*y^2+",m[12],"*x*y+",m[10]*z[0]+m[9],"*x+",m[4]*z[0]+m[3],"*y+",m[2]*z[0]**2+m[1]*z[0]+m[0],"\n"
        a = m[18]
        b = m[6]
        c = m[12]
        d = m[10]*z[0]+m[9]
        e = m[4]*z[0]+m[3]
        f = m[2]*z[0]**2+m[1]*z[0]+m[0]
        print "Minimum located: x=",-(2*b*d-c*e)/(4*a*b-c**2)," y=",-(c*d-2*a*e)/(-4*a*b+c**2)

    elif dimension_x == 1 and dimension_y == 1 and dimension_z == 0:
        print "Fitted result:",m[2],"*z^2+",m[10]*x[0]+m[4]*y[0]+m[1],"*z+", m[18]*x[0]**2+m[6]*y[0]**2+m[12]*x[0]*y[0]+m[9]*x[0]+m[3]*y[0]+m[0],"\n"
        a = m[2]
        b = m[10]*x[0]+m[4]*y[0]+m[1]
        print "Minimum located: z=",-b/(2*a)

    elif dimension_x == 1 and dimension_y == 0 and dimension_z == 1:
        print "Fitted result:",m[6],"*y^2+",m[12]*x[0]+m[4]*z[0]+m[3],"*y+", m[18]*x[0]**2+m[2]*z[0]**2+m[10]*x[0]*z[0]+m[9]*x[0]+m[1]*z[0]+m[0],"\n"
        a = m[6]
        b = m[12]*x[0]+m[4]*z[0]+m[3]
        print "Minimum located: y=",-b/(2*a)

    elif dimension_x == 0 and dimension_y == 1 and dimension_z == 1:
        print "Fitted result:",m[18],"*x^2+",m[12]*y[0]+m[10]*z[0]+m[9],"*x+",m[6]*y[0]**2+m[2]*z[0]**2+m[4]*y[0]*z[0]+m[3]*y[0]+m[1]*z[0]+m[0],"\n"
        a = m[18]
        b = m[12]*y[0]+m[10]*z[0]+m[9]
        print "Minimum located: x=",-b/(2*a)

    #print "Fitted result:", m[6],"*x^2+",m[2],"*y^2+",m[4],"*x*y+",m[3],"*x+",m[1],"*y+",m[0],"\n"
    #print "Fitted result:", m[18],"*x^2+",m[6],"*y^2+",m[2],"*z^2+",m[12],"*x*y+",m[10],"*x*z+",m[4],"*y*z+",m[9],"*x+",m[3],"*y+",m[1],"*z+",m[0],"\n"
    #a=m[6],b=m[2],c=m[4],d=m[3],e=m[1],f=m[0]
    #print "Minimum located: x=",-(2*m[2]*m[3]-m[4]*m[1])/(4*m[6]*m[2]-m[4]*m[4])," y=",-(m[4]*m[3]-2*m[6]*m[1])/(-4*m[6]*m[2]+m[4]*m[4])
    # Print the result
    #print m
    return m

def polyval2d(x, y, z, m):
    order = int(np.sqrt(len(m))) - 1
    ij = itertools.product(range(order+1), range(order+1))
    z = np.zeros_like(x)
    for a, (i,j) in zip(m, ij):
        z += a * x**i * y**j * z**q
        # Using =+ to add up all term
    return z

main()

