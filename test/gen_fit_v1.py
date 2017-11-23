def gen_fit():
    file_extration = open('Quadratic_fit.py','a')
    file_extration.write('''import numpy as np'''+"\n")
    file_extration.write('''import itertools'''+"\n")
    file_extration.write('''import matplotlib.pyplot as plt'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''def main():'''+"\n")
    file_extration.write('''    # Generate Data...'''+"\n")
    file_extration.write('''#    numdata = 100'''+"\n")
    file_extration.write('''#    x = np.random.random(numdata)'''+"\n")
    file_extration.write('''    # X array'''+"\n")
    file_extration.write('''#    y = np.random.random(numdata)'''+"\n")
    file_extration.write('''#    z = x**2 + y**2'''+"\n")
    file_extration.write('''    data_raw = np.zeros((100,100))'''+"\n")
    file_extration.write('''    file = open("data.dat", "r")'''+"\n")
    file_extration.write('''    content = [x.rstrip('''+r'''"\n"'''+''') for x in file]'''+"\n")
    file_extration.write('''    data_raw = np.array([x.split()[:5] for x in content[:]])'''+"\n")
    file_extration.write('''    data = np.zeros(data_raw.shape)'''+"\n")
    file_extration.write('''    #print data'''+"\n")
    file_extration.write('''    for i in range(data_raw.shape[0]):'''+"\n")
    file_extration.write('''        for j in range(data_raw.shape[1]):'''+"\n")
    file_extration.write('''            data[i,j] = float(data_raw[i,j])'''+"\n")
    file_extration.write('''    #print float(data[0,0])+float(data[0,1])'''+"\n")
    file_extration.write('''    x = data[:,0]'''+"\n")
    file_extration.write('''    y = data[:,1]'''+"\n")
    file_extration.write('''    z = data[:,2]'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''    dimension_x = 0'''+"\n")
    file_extration.write('''    dimension_y = 0'''+"\n")
    file_extration.write('''    dimension_z = 0'''+"\n")
    file_extration.write('''    if data[0,0] == data[-1,0]:'''+"\n")
    file_extration.write('''        print "x axis same"'''+"\n")
    file_extration.write('''        dimension_x = 1'''+"\n")
    file_extration.write('''    elif data[0,1] == data[-1,1]:'''+"\n")
    file_extration.write('''        print "y axis same"'''+"\n")
    file_extration.write('''        dimension_y = 1'''+"\n")
    file_extration.write('''    elif data[0,2] == data[-1,2]:'''+"\n")
    file_extration.write('''        print "z axis same"'''+"\n")
    file_extration.write('''        dimension_z = 1'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''    dimension = dimension_x+dimension_y+dimension_z'''+"\n")
    file_extration.write('''    if dimension == 1:'''+"\n")
    file_extration.write('''        print "2D_material'''+r'''\n"'''+"\n")
    file_extration.write('''    elif dimension == 2:'''+"\n")
    file_extration.write('''        print "1D_material'''+r'''\n"'''+"\n")
    file_extration.write('''    elif dimension == 0:'''+"\n")
    file_extration.write('''        print "3D material'''+r'''\n"'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''    eneg = data[:,3]'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''\n''')
    file_extration.write('''    # Fit a 3rd order, 2d polynomial'''+"\n")
    file_extration.write('''    m = polyfit2d(x,y,z,eneg, dimension_x, dimension_y, dimension_z)'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''\n''')
    file_extration.write('''    # Evaluate it on a grid...'''+"\n")
    file_extration.write('''    #nx, ny = 100, 100'''+"\n")
    file_extration.write('''    #print x.min(), x.max(),  y.min(), y.max()'''+"\n")
    file_extration.write('''    #xx, yy = np.meshgrid(np.linspace(x.min(), x.max(), nx),'''+"\n")
    file_extration.write('''    #                     np.linspace(y.min(), y.max(), ny))'''+"\n")
    file_extration.write('''    #zz = polyval2d(xx, yy, m)'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''    # Plot'''+"\n")
    file_extration.write('''    #plt.imshow(zz, extent=(x.min()-0.2, y.max()+0.2, x.max()+0.2, y.min()-0.2))'''+"\n")
    file_extration.write('''    # Some times withou 0.5 would fail'''+"\n")
    file_extration.write('''    #plt.scatter(x, y, c=z)'''+"\n")
    file_extration.write('''    #plt.show()'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''def polyfit2d(x, y, z, eneg, dimension_x, dimension_y, dimension_z, order=2):'''+"\n")
    file_extration.write('''    ncols = (order + 1)**3'''+"\n")
    file_extration.write('''    G = np.zeros((x.size, ncols))'''+"\n")
    file_extration.write('''    ijq = itertools.product(range(order+1), range(order+1), range(order+1))'''+"\n")
    file_extration.write('''    # Generate polynomial function matrix'''+"\n")
    file_extration.write('''    for k, (i,j,q) in enumerate(ijq):'''+"\n")
    file_extration.write('''    # Using enumerate to add coefficients fo mattix'''+"\n")
    file_extration.write('''        if k < 5 or k == 6 or k==9 or k==10 or k==12 or k==18:'''+"\n")
    file_extration.write('''        # Using quadratic function: a*x^2+b*x^2+c*x*y+d*x+e*y+f as fitting function'''+"\n")
    file_extration.write('''            G[:,k] = x**i * y**j * z**q'''+"\n")
    file_extration.write('''    m, _, _, _ = np.linalg.lstsq(G, eneg)'''+"\n")
    file_extration.write('''    # I don't fully understand this, supposely a matirx trick.'''+"\n")
    file_extration.write('''    if dimension_x == 0 and dimension_y == 0 and dimension_z == 0:'''+"\n")
    file_extration.write('''        print "Fitted result:", m[18],"*x^2+",m[6],"*y^2+",m[2],"*z^2+",m[12],"*x*y+",m[10],"*x*z+",m[4],"*y*z+",m[9],"*x+",m[3],"*y+",m[1],"*z+",m[0],'''+r'''"\n"'''+"\n")
    file_extration.write('''        a = m[18]'''+"\n")
    file_extration.write('''        b = m[6]'''+"\n")
    file_extration.write('''        c = m[2]'''+"\n")
    file_extration.write('''        d = m[12]'''+"\n")
    file_extration.write('''        e = m[10]'''+"\n")
    file_extration.write('''        f = m[4]'''+"\n")
    file_extration.write('''        g = m[9]'''+"\n")
    file_extration.write('''        h = m[3]'''+"\n")
    file_extration.write('''        i = m[1]'''+"\n")
    file_extration.write('''        j = m[0]'''+"\n")
    file_extration.write('''        print "Minimum located: x=",-(4*b*c*g-f**2*g-2*c*d*h+e*f*h-2*b*e*i+d*f*i)/(2*(4*a*b*c-c*d**2-b*e**2+d*e*f-a*f**2))," y=",-(2*c*d*g-e*f*g-4*a*c*h+e**2*h-d*e*i+2*a*f*i)/(2*(-4*a*b*c+c*d**2+b*e**2-d*e*f+a*f**2))," z=",-(2*b*e*g-d*f*g-d*e*h+2*a*f*h-4*a*b*i+d**2*i)/(2*(-4*a*b*c+c*d**2+b*e**2-d*e*f+a*f**2))'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''    elif dimension_x == 1 and dimension_y == 0 and dimension_z == 0:'''+"\n")
    file_extration.write('''        print "Fitted result:", m[6],"*y^2+",m[2],"*z^2+",m[4],"*y*z+",m[12]*x[0]+m[3],"*y+",m[10]*x[0]+m[1],"*z+", m[18]*x[0]**2+m[9]*x[0]+m[0],'''+r'''"\n"'''+"\n")
    file_extration.write('''        a = m[6]'''+"\n")
    file_extration.write('''        b = m[2]'''+"\n")
    file_extration.write('''        c = m[4]'''+"\n")
    file_extration.write('''        d = m[12]*x[0]+m[3]'''+"\n")
    file_extration.write('''        e = m[10]*x[0]+m[1]'''+"\n")
    file_extration.write('''        f = m[18]*x[0]**2+m[9]*x[0]+m[0]'''+"\n")
    file_extration.write('''        print "Minimum located: y=",-(2*b*d-c*e)/(4*a*b-c**2)," z=",-(c*d-2*a*e)/(-4*a*b+c**2)'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''    elif dimension_x == 0 and dimension_y == 1 and dimension_z == 0:'''+"\n")
    file_extration.write('''        print "Fitted result:", m[18],"*x^2+",m[2],"*z^2+",m[10],"*x*z+",m[12]*y[0]+m[9],"*x+",m[4]*y[0]+m[1],"*z+",m[6]*y[0]**2+m[3]*y[0]+m[0],'''+r'''"\n"'''+"\n")
    file_extration.write('''        a = m[18]'''+"\n")
    file_extration.write('''        b = m[6]'''+"\n")
    file_extration.write('''        c = m[10]'''+"\n")
    file_extration.write('''        d = m[12]*y[0]+m[9]'''+"\n")
    file_extration.write('''        e = m[4]*y[0]+m[1]'''+"\n")
    file_extration.write('''        f = m[6]*y[0]**2+m[3]*y[0]+m[0]'''+"\n")
    file_extration.write('''        print "Minimum located: x=",-(2*b*d-c*e)/(4*a*b-c**2)," z=",-(c*d-2*a*e)/(-4*a*b+c**2)'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''    elif dimension_x == 0 and dimension_y == 0 and dimension_z == 1:'''+"\n")
    file_extration.write('''        print "Fitted result:", m[18],"*x^2+",m[6],"*y^2+",m[12],"*x*y+",m[10]*z[0]+m[9],"*x+",m[4]*z[0]+m[3],"*y+",m[2]*z[0]**2+m[1]*z[0]+m[0],'''+r'''"\n"'''+"\n")
    file_extration.write('''        a = m[18]'''+"\n")
    file_extration.write('''        b = m[6]'''+"\n")
    file_extration.write('''        c = m[12]'''+"\n")
    file_extration.write('''        d = m[10]*z[0]+m[9]'''+"\n")
    file_extration.write('''        e = m[4]*z[0]+m[3]'''+"\n")
    file_extration.write('''        f = m[2]*z[0]**2+m[1]*z[0]+m[0]'''+"\n")
    file_extration.write('''        print "Minimum located: x=",-(2*b*d-c*e)/(4*a*b-c**2)," y=",-(c*d-2*a*e)/(-4*a*b+c**2)'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''    elif dimension_x == 1 and dimension_y == 1 and dimension_z == 0:'''+"\n")
    file_extration.write('''        print "Fitted result:",m[2],"*z^2+",m[10]*x[0]+m[4]*y[0]+m[1],"*z+", m[18]*x[0]**2+m[6]*y[0]**2+m[12]*x[0]*y[0]+m[9]*x[0]+m[3]*y[0]+m[0],'''+r'''"\n"'''+"\n")
    file_extration.write('''        a = m[2]'''+"\n")
    file_extration.write('''        b = m[10]*x[0]+m[4]*y[0]+m[1]'''+"\n")
    file_extration.write('''        print "Minimum located: z=",-b/(2*a)'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''    elif dimension_x == 1 and dimension_y == 0 and dimension_z == 1:'''+"\n")
    file_extration.write('''        print "Fitted result:",m[6],"*y^2+",m[12]*x[0]+m[4]*z[0]+m[3],"*y+", m[18]*x[0]**2+m[2]*z[0]**2+m[10]*x[0]*z[0]+m[9]*x[0]+m[1]*z[0]+m[0],'''+r'''"\n"'''+"\n")
    file_extration.write('''        a = m[6]'''+"\n")
    file_extration.write('''        b = m[12]*x[0]+m[4]*z[0]+m[3]'''+"\n")
    file_extration.write('''        print "Minimum located: y=",-b/(2*a)'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''    elif dimension_x == 0 and dimension_y == 1 and dimension_z == 1:'''+"\n")
    file_extration.write('''        print "Fitted result:",m[18],"*x^2+",m[12]*y[0]+m[10]*z[0]+m[9],"*x+",m[6]*y[0]**2+m[2]*z[0]**2+m[4]*y[0]*z[0]+m[3]*y[0]+m[1]*z[0]+m[0],'''+r'''"\n"'''+"\n")
    file_extration.write('''        a = m[18]'''+"\n")
    file_extration.write('''        b = m[12]*y[0]+m[10]*z[0]+m[9]'''+"\n")
    file_extration.write('''        print "Minimum located: x=",-b/(2*a)'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''    #print "Fitted result:", m[6],"*x^2+",m[2],"*y^2+",m[4],"*x*y+",m[3],"*x+",m[1],"*y+",m[0],'''+r'''"\n"'''+"\n")
    file_extration.write('''    #print "Fitted result:", m[18],"*x^2+",m[6],"*y^2+",m[2],"*z^2+",m[12],"*x*y+",m[10],"*x*z+",m[4],"*y*z+",m[9],"*x+",m[3],"*y+",m[1],"*z+",m[0],'''+r'''"\n"'''+"\n")
    file_extration.write('''    #a=m[6],b=m[2],c=m[4],d=m[3],e=m[1],f=m[0]'''+"\n")
    file_extration.write('''    #print "Minimum located: x=",-(2*m[2]*m[3]-m[4]*m[1])/(4*m[6]*m[2]-m[4]*m[4])," y=",-(m[4]*m[3]-2*m[6]*m[1])/(-4*m[6]*m[2]+m[4]*m[4])'''+"\n")
    file_extration.write('''    # Print the result'''+"\n")
    file_extration.write('''    #print m'''+"\n")
    file_extration.write('''    return m'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''def polyval2d(x, y, z, m):'''+"\n")
    file_extration.write('''    order = int(np.sqrt(len(m))) - 1'''+"\n")
    file_extration.write('''    ij = itertools.product(range(order+1), range(order+1))'''+"\n")
    file_extration.write('''    z = np.zeros_like(x)'''+"\n")
    file_extration.write('''    for a, (i,j) in zip(m, ij):'''+"\n")
    file_extration.write('''        z += a * x**i * y**j * z**q'''+"\n")
    file_extration.write('''        # Using =+ to add up all term'''+"\n")
    file_extration.write('''    return z'''+"\n")
    file_extration.write('''\n''')
    file_extration.write('''main()'''+"\n")
gen_fit()