# Environment Modules

Software libraries and applications are available for use under the command-line interface (CLI) through the [Environment Modules] implemented through its main executable - `module`.

!!! note "Module help"
    As with many other command-line tools `module help` explains the usage of the module command.

## List Available Modules

The command `module avail` provides a complete list of the **modules made available on our platform**. The common stem for the module installation paths is displayed on top of each section listed in the output, whereas the rest of the path name is specified under each listed entry.

We have reproduced the output of this command below listing all currently available modules, for reference purposes. The reader is referred to the [relevant section](../software/overview.md) of the documentation for an introduction to the codes, libraries and software packages listed here.

```text
---------------------------------- /export/compute/modulefiles/system -----------------------------------
emacs/24.5

------------------------------- /export/compute/modulefiles/applications --------------------------------
cp2k/41-i-174-impi-044               vasp/535-g-485-ompi-110
espresso/521-g-485-ompi-110          vasp/535-g-485-ompi-110-nc
espresso/521-i-174-impi-044(default) vasp/535-g-485-ompi-110-vtst
espresso/540-g-485-ompi-110          vasp/535-i-174-impi-044(default)
espresso/540-i-174-impi-044          vasp/535-i-174-impi-044-nc
espresso/600-g-485-ompi-110          vasp/535-i-174-impi-044-vtst
espresso/600-i-174-impi-044          vasp/544-i-174-impi-044
gromacs/20182-i-174-impi-044-gms     vasp/544-i-174-impi-044-gamma
gromacs/20183-i-174-impi-044-gms     vasp/544-i-174-impi-044-gpu
gromacs/514-g-485-ompi-110-md        vasp/544-i-174-impi-044-nc
gromacs/514-g-485-ompi-110-ms        vasp/544-i-174-impi-044-vtst
gromacs/514-i-174-impi-044-md        vasp/544-i-174-impi-044-vtst-gamma
gromacs/514-i-174-impi-044-ms        vasp/544-i-174-impi-044-vtst-nc
lammps/1116-g-485-ompi-110           vesta/3.3.8
lammps/1116-i-174-impi-044           vmd/1.9.3
nwchem/66-i-174-impi-044             vnl-atk/2016.2
p4vasp/0.3.30                        xcrysden/1.5.60
turbomole/v7.0

--------------------------------- /export/compute/modulefiles/compilers ---------------------------------
gcc/5.4.0            intel/i-174(default)

--------------------------------- /export/compute/modulefiles/libraries ---------------------------------
mkl/i-174(default)    mpi/impi-044(default) mpi/ompi-110          openblas/218-g-540
```

Through the `module avail` command, the user can also **search** for available modules, by partially inserting the module's name. This functionality is demonstrated in the example below.

```bash
[steve@bohr.exabyte.io:~]$ module avail espresso
------------------------------ /export/compute/modulefiles/applications ------------------------------
espresso/511-g-485-ompi-110          espresso/521-i-174-impi-044(default) espresso/540-i-174-impi-044

```

## Actions

Software modules can be listed, loaded and reset in the CLI environment as reviewed [in this page](actions/modules-actions.md).


## Links

[^1]: [Wikipedia Environment Modules, Website](https://en.wikipedia.org/wiki/Environment_Modules_(software))
