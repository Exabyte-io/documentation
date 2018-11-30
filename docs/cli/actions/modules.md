# The Module Command 

We describe in the present page how pre-compiled [modules](../environment.md#modules) can be handled under the [Command Line Interface](../overview.md) of our platform, via the `module` command and its corresponding keyword parameters.

## List Currently Loaded Modules

The first command of interest is `module list`, which returns the list of **currently loaded modules**. No modules are pre-loaded by default at the moment of login, such that this command will return an empty list unless new modules are loaded as explained in a forthcoming section of this page. 

Below is an example of the output of this command, showing the list of modules loaded by user "Steve".

```bash
[steve@bohr.exabyte.io:~]$ module list
Currently Loaded Modulefiles:
  1) intel/i-174(default)    2) mpi/impi-044(default)    3) mkl/i-174(default)    4) espresso/521-i-174-impi-044(default)
```

## List Available Modules

The command `module avail` provides a complete list of the modules made available on our platform. The common stem for the complete module installation path is displayed on top of each section listed in the output, whereas the rest of the path name is specified under each listed entry.

We have reproduced the output of this command below, for reference purposes. The reader is referred to the [relevant section](../../software/overview.md) of the documentation for an introduction to the codes, libraries and software packages listed here.

```bash
---------------------------------------------------------------------------- /export/compute/modulefiles/system ----------------------------------------------------------------------------
emacs/24.5

------------------------------------------------------------------------- /export/compute/modulefiles/applications -------------------------------------------------------------------------
cp2k/41-i-174-impi-044               gromacs/20182-i-174-impi-044-gms     lammps/1116-i-174-impi-044           vasp/535-i-174-impi-044(default)     vasp/544-i-174-impi-044-vtst
espresso/521-g-485-ompi-110          gromacs/20183-i-174-impi-044-gms     nwchem/66-i-174-impi-044             vasp/535-i-174-impi-044-nc           vasp/544-i-174-impi-044-vtst-gamma
espresso/521-i-174-impi-044(default) gromacs/514-g-485-ompi-110-md        p4vasp/0.3.30                        vasp/535-i-174-impi-044-vtst         vasp/544-i-174-impi-044-vtst-nc
espresso/540-g-485-ompi-110          gromacs/514-g-485-ompi-110-ms        turbomole/v7.0                       vasp/544-i-174-impi-044              vesta/3.3.8
espresso/540-i-174-impi-044          gromacs/514-i-174-impi-044-md        vasp/535-g-485-ompi-110              vasp/544-i-174-impi-044-gamma        vmd/1.9.3
espresso/600-g-485-ompi-110          gromacs/514-i-174-impi-044-ms        vasp/535-g-485-ompi-110-nc           vasp/544-i-174-impi-044-gpu          vnl-atk/2016.2
espresso/600-i-174-impi-044          lammps/1116-g-485-ompi-110           vasp/535-g-485-ompi-110-vtst         vasp/544-i-174-impi-044-nc           xcrysden/1.5.60

-------------------------------------------------------------------------- /export/compute/modulefiles/compilers ---------------------------------------------------------------------------
gcc/5.4.0            intel/i-174(default)

-------------------------------------------------------------------------- /export/compute/modulefiles/libraries ---------------------------------------------------------------------------
mkl/i-174(default)    mpi/impi-044(default) mpi/ompi-110          openblas/218-g-540
```

The user can also search for available modules with this command, through a partial insertion of the module's name, as demonstrated in the example below.

```bash
[steve@bohr.exabyte.io:~]$ module avail espresso
------------------------------ /export/compute/modulefiles/applications ------------------------------
espresso/511-g-485-ompi-110          espresso/521-i-174-impi-044(default) espresso/540-i-174-impi-044

```

## Load Desired Module

The user can load a certain desired module from the aforementioned list of available ones via the `module load <module name>` command.

For example, to use the [Quantum ESPRESSO](../../software/modeling/quantum-espresso.md) modelling application, the corresponding module can be loaded as follows. All other library dependencies of the desired module will also be loaded automatically in this way.

```bash
[steve@bohr.exabyte.io:~]$ module load espresso/521-i-174-impi-044
The module intel/i-174 is loaded
The module mpi/impi-044 is loaded
The module intel/i-174 is loaded
The module mkl/i-174 is loaded
The module espresso/521-i-174-impi-044 is loaded
```

If there is a "default" keyword next to a module name, it can be loaded without specifying the full module name, as demonstrated below.

```bash
[steve@bohr.exabyte.io:~]$ module load espresso
The module intel/i-174 is loaded
The module mpi/impi-044 is loaded
The module intel/i-174 is loaded
The module mkl/i-174 is loaded
The module espresso/521-i-174-impi-044 is loaded
```

## Purge All Loaded Modules

Finally, the `module purge` command can be entered to completely clean the environment and deactivate all currently loaded modules. This functionality is illustrated by way of the following example.

```bash
[steve@bohr.exabyte.io:~]$ module list
Currently Loaded Modulefiles:
  1) intel/i-174(default)    2) mpi/impi-044(default)    3) mkl/i-174(default)    4) espresso/521-i-174-impi-044(default)
[steve@bohr.exabyte.io:~]$ module purge
[steve@bohr.exabyte.io:~]$ module list
No Modulefiles Currently Loaded.
```
