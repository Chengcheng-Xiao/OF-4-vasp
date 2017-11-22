# OF-4-vasp
Geometry Optimisation and Quadratic fitting program for VASP

This program was written with Python

This program can do:

    1.Check POSCAR "symmetry" (This only determins wether lattice paremeters' length are the same).
    2.Change lattice parameters and creat corresponding POSCAR.
    3.Submit Geometry optmization job (can support different submitting methods).
    4.After calculations, check for convergence and out-put "data.dat" file which contians energy data and lattice parameters.
    5.Fit lattice parameters using quadratic function and print the optmized one.

Example result:
    Fitted result: 1.53253625 *x^2+ 0.597441333335 *y^2+ 0.981367600002 *x*y+ -17.79265322 *x+ -9.85541972002 *y+ 44.2136277874
    Minimum located: x= 4.29306080482  y= 4.72209456102

