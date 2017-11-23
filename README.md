# OF-4-vasp
Crystal geometry Optimization and Quadratic-function fitting program using VASP as calculator.
This program can:

    1.Check POSCAR "symmetry" (This only determines wether lattice parameters' length are the same).
    2.Change lattice parameters and create corresponding POSCAR.
    3.Submit Geometry optimization job (can support different submitting methods like "Portabl Batch System" (PBS) and Slurm).
    4.After calculations, check for convergence and out-put "data.dat" file which contains energy data and lattice parameters.
    5.Fit lattice parameters using quadratic function and print the optimized one.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine or remote cluster for development and testing purposes.

### Prerequisites
This program was written with Python2.7
The following newest library are needed:
```
numpy
readline (or pyreadline for windows machine, However, Linux are preferred)
matplotlib
```

### Installing
Simply download the latest version and put it in a directory that is in your system's `PATH`.
Then:
```
Chmod 755 Axis_OPT_universal_vx.x.py
```

## Usage
Explain how to run this program.

### Axis Optimization
```
./Axis_OPT_universal_vx.x.py

Do you want to submit all jobs (yes/no):yes

Enter the job submition command(e.g.qsub -N test run.sh):qsub -N test run.sh
RU sure? (yes/no):yes

Enter the name of your job_submittion script[e.g. run.sh](use Tab):run.sh
RU sure? (yes/no):yes
Input the name of POSCAR source(use Tab):test_POS

All axis length are different

Input the value of a_min: 4.70
Input the value of a_max: 4.90
How many steps for a_step: 20
Input the value of b_min: 4.40
Input the value of b_max: 4.60
How many steps for b_step: 20
Input the value of c_min: 20.00
Input the value of c_max: 20.00
How many steps for c_step: 1

...
...

Goodbye.
```
Program will produce multiple folders named after different lattice parameters and run(or not run, depending on your choice) VASP.
Program will also generate two files named "data_extration.py" and "Quadratic_fit.py", use:
```
python data_extration.py
```
to extract final energy for every lattice parameters. Results are gathtered in "data.dat" file.
and:
```
python Quadratic_fit.py
```
to fitting the energy surface with quadratic function

Addition notes:

*1.Original POSCAR file can not be named "POSCAR" since program will automatically delete any file named after it.

*2.Quadratic function are only applicable if lattice parameters do not differ much from the optimum one. **Use this at your own discretion.**


### Example result:
```
Fitted result: 1.533x^2 + 0.597*y^2 + 0.981*x*y - 17.793*x - 9.855*y + 44.214.
Minimum located: x= 4.293  y= 4.722.
```
