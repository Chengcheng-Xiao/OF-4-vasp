def gen_fit():
    file_extration = open('Quadratic_fit.py','a')
    file_extration.write("import numpy as np"+'\n')
    file_extration.write("import itertools"+'\n')
    file_extration.write("import matplotlib.pyplot as plt"+'\n')
    file_extration.write("\n")
    file_extration.write("def main():"+'\n')
    file_extration.write("    # Generate Data..."+'\n')
    file_extration.write("#    numdata = 100"+'\n')
    file_extration.write("#    x = np.random.random(numdata)"+'\n')
    file_extration.write("    # X array"+'\n')
    file_extration.write("#    y = np.random.random(numdata)"+'\n')
    file_extration.write("#    z = x**2 + y**2"+'\n')
    file_extration.write("    data_raw = np.zeros((100,100))"+'\n')
    file_extration.write('''    file = open("data.dat", "r")'''+'\n')
    file_extration.write('''    content = [x.rstrip('''+r"'\n'"+''') for x in file]'''+'\n')
    file_extration.write("    data_raw = np.array([x.split()[:5] for x in content[:]])"+'\n')
    file_extration.write("    data = np.zeros(data_raw.shape)"+'\n')
    file_extration.write("    #print data"+'\n')
    file_extration.write("    for i in range(data_raw.shape[0]):"+'\n')
    file_extration.write("        for j in range(data_raw.shape[1]):"+'\n')
    file_extration.write("            data[i,j] = float(data_raw[i,j])"+'\n')
    file_extration.write("    #print float(data[0,0])+float(data[0,1])"+'\n')
    file_extration.write("    x = data[:,0]"+'\n')
    file_extration.write("    y = data[:,1]"+'\n')
    file_extration.write("    z = data[:,3]"+'\n')
    file_extration.write("    z_axis = data[:,2]"+'\n')
    file_extration.write("\n")
    file_extration.write("\n")
    file_extration.write("    # Fit a 3rd order, 2d polynomial"+'\n')
    file_extration.write("    m = polyfit2d(x,y,z)"+'\n')
    file_extration.write("\n")
    file_extration.write("\n")
    file_extration.write("    # Evaluate it on a grid..."+'\n')
    file_extration.write("    nx, ny = 100, 100"+'\n')
    file_extration.write("    #print x.min(), x.max(),  y.min(), y.max()"+'\n')
    file_extration.write("    xx, yy = np.meshgrid(np.linspace(x.min(), x.max(), nx),"+'\n')
    file_extration.write("                         np.linspace(y.min(), y.max(), ny))"+'\n')
    file_extration.write("    zz = polyval2d(xx, yy, m)"+'\n')
    file_extration.write("\n")
    file_extration.write("    # Plot"+'\n')
    file_extration.write("    plt.imshow(zz, extent=(x.min()-0.2, y.max()+0.2, x.max()+0.2, y.min()-0.2))"+'\n')
    file_extration.write("    # Some times withou 0.5 would fail"+'\n')
    file_extration.write("    plt.scatter(x, y, c=z)"+'\n')
    file_extration.write("    plt.show()"+'\n')
    file_extration.write("\n")
    file_extration.write("def polyfit2d(x, y, z, order=2):"+'\n')
    file_extration.write("    ncols = (order + 1)**2"+'\n')
    file_extration.write("    G = np.zeros((x.size, ncols))"+'\n')
    file_extration.write("    ij = itertools.product(range(order+1), range(order+1))"+'\n')
    file_extration.write("    # Generate polynomial function matrix"+'\n')
    file_extration.write("    for k, (i,j) in enumerate(ij):"+'\n')
    file_extration.write("    # Using enumerate to add coefficients fo mattix"+'\n')
    file_extration.write("        if k < 7 and k != 5:"+'\n')
    file_extration.write("        # Using quadratic function: a*x^2+b*x^2+c*x*y+d*x+e*y+f as fitting function"+'\n')
    file_extration.write("            G[:,k] = x**i * y**j"+'\n')
    file_extration.write("    m, _, _, _ = np.linalg.lstsq(G, z)"+'\n')
    file_extration.write("    # I don't fully understand this, supposely a matirx trick."+'\n')
    file_extration.write('''    print "Fitted result:", m[6],"*x^2+",m[2],"*y^2+",m[4],"*x*y+",m[3],"*x+",m[1],"*y+",m[0],'''+'\n')
    file_extration.write("    #a=m[6],b=m[2],c=m[4],d=m[3],e=m[1],f=m[0]"+'\n')
    file_extration.write('''    print "Minimum located: x=",-(2*m[2]*m[3]-m[4]*m[1])/(4*m[6]*m[2]-m[4]*m[4])," y=",-(m[4]*m[3]-2*m[6]*m[1])/(-4*m[6]*m[2]+m[4]*m[4])'''+'\n')
    file_extration.write("    # Print the result"+'\n')
    file_extration.write("    return m"+'\n')
    file_extration.write("\n")
    file_extration.write("def polyval2d(x, y, m):"+'\n')
    file_extration.write("    order = int(np.sqrt(len(m))) - 1"+'\n')
    file_extration.write("    ij = itertools.product(range(order+1), range(order+1))"+'\n')
    file_extration.write("    z = np.zeros_like(x)"+'\n')
    file_extration.write("    for a, (i,j) in zip(m, ij):"+'\n')
    file_extration.write("        z += a * x**i * y**j"+'\n')
    file_extration.write("        # Using =+ to add up all term"+'\n')
    file_extration.write("    return z"+'\n')
    file_extration.write("\n")
    file_extration.write("main()"+'\n')