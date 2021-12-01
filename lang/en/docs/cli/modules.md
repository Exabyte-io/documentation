# Environment Modules

With Environment Modules, a variety of software libraries and applications are available for use in the command line interface (CLI).  These modules are selectively activated and deactivated with the Environment Module command line utility `module`.

!!! note "Module help"
    As with many other command line tools `module help` explains the usage of the module command.

## List Available Modules

The command `module avail` provides a complete list of the **modules made available on our platform**. The common stem for the module installation paths is displayed on top of each section listed in the output, whereas the rest of the path name is specified under each listed entry.

We have reproduced the output of this command below listing all currently available modules, for reference purposes. The reader is referred to the [software directory overview](../software-directory/overview.md) for an introduction to the codes, libraries and software packages listed here.

```text
------------------------------------ /export/compute/modulefiles/system -------------------------------------
emacs/24.5

--------------------------------- /export/compute/modulefiles/applications ----------------------------------
cp2k/4.1-i-14.0.3.174-impi-5.0.2.044              lammps/12Dec2018-i-14.0.3.174-impi-5.0.2.044
cp2k/41-i-174-impi-044                            lammps/5Nov16-g-4.8.5-ompi-1.10.0
espresso/521-g-485-ompi-110                       lammps/5Nov16-i-14.0.3.174-impi-5.0.2.044
espresso/5.2.1-g-4.8.5-ompi-1.10.0                nwchem/6.6-i-14.0.3.174-impi-5.0.2.044
espresso/5.2.1-i-14.0.3.174-impi-5.0.2.044        nwchem/66-i-174-impi-044
espresso/521-i-174-impi-044                       nwchem/702-g-485-ompi-110
espresso/540-g-485-ompi-110                       nwchem/7.0.2-g-4.8.5-ompi-1.10.0
espresso/5.4.0-g-4.8.5-ompi-1.10.0                nwchem/7.0.2-i-14.0.3.174-impi-5.0.2.044
espresso/5.4.0-i-14.0.3.174-impi-5.0.2.044        nwchem/702-i-174-impi-044
espresso/540-i-174-impi-044(default)              p4vasp/0.3.30
espresso/600-g-485-ompi-110                       turbomole/v7.0
espresso/6.0.0-g-4.8.5-ompi-1.10.0                vasp/535-g-485-ompi-110
espresso/6.0.0-i-14.0.3.174-impi-5.0.2.044        vasp/5.3.5-g-4.8.5-ompi-1.10.0
espresso/600-i-174-impi-044                       vasp/5.3.5-g-4.8.5-ompi-1.10.0-nc
espresso/63-g-485-ompi-110                        vasp/5.3.5-g-4.8.5-ompi-1.10.0-vtst
espresso/6.3-g-4.8.5-ompi-1.10.0                  vasp/535-g-485-ompi-110-nc
espresso/6.3-i-14.0.3.174-impi-5.0.2.044          vasp/535-g-485-ompi-110-vtst
espresso/63-i-174-impi-044                        vasp/5.3.5-i-14.0.3.174-impi-5.0.2.044
espresso/6.4.1-g-11.2.0-ompi-4.1.1                vasp/5.3.5-i-14.0.3.174-impi-5.0.2.044-nc
espresso/641-g-1120-ompi-411                      vasp/5.3.5-i-14.0.3.174-impi-5.0.2.044-vtst
espresso/6.5.0-g-11.2.0-ompi-4.1.1                vasp/535-i-174-impi-044(default)
espresso/650-g-1120-ompi-411                      vasp/535-i-174-impi-044-nc
espresso/6.6.0-g-11.2.0-ompi-4.1.1                vasp/535-i-174-impi-044-vtst
espresso/660-g-1120-ompi-411                      vasp/5.4.4-i-14.0.3.174-impi-5.0.2.044
espresso/6.7.0-g-11.2.0-ompi-4.1.1                vasp/5.4.4-i-14.0.3.174-impi-5.0.2.044-gamma
espresso/670-g-1120-ompi-411                      vasp/5.4.4-i-14.0.3.174-impi-5.0.2.044-gpu
espresso/6.8.0-g-11.2.0-ompi-4.1.1                vasp/5.4.4-i-14.0.3.174-impi-5.0.2.044-nc
espresso/680-g-1120-ompi-411                      vasp/5.4.4-i-14.0.3.174-impi-5.0.2.044-vtst
gromacs/2018.2-i-14.0.3.174-impi-5.0.2.044-gms    vasp/5.4.4-i-14.0.3.174-impi-5.0.2.044-vtst-gamma
gromacs/20182-i-174-impi-044-gms                  vasp/5.4.4-i-14.0.3.174-impi-5.0.2.044-vtst-nc
gromacs/2018.3-i-14.0.3.174-impi-5.0.2.044-gms    vasp/544-i-174-impi-044
gromacs/20183-i-174-impi-044-gms                  vasp/544-i-174-impi-044-gamma
gromacs/5.1.4-g-4.8.5-ompi-1.10.0-md              vasp/544-i-174-impi-044-gpu
gromacs/5.1.4-g-4.8.5-ompi-1.10.0-ms              vasp/544-i-174-impi-044-nc
gromacs/514-g-485-ompi-110-md                     vasp/544-i-174-impi-044-vtst
gromacs/514-g-485-ompi-110-ms                     vasp/544-i-174-impi-044-vtst-gamma
gromacs/5.1.4-i-14.0.3.174-impi-5.0.2.044-md      vasp/544-i-174-impi-044-vtst-nc
gromacs/5.1.4-i-14.0.3.174-impi-5.0.2.044-ms      vesta/3.3.8
gromacs/514-i-174-impi-044-md                     vmd/1.9.3
gromacs/514-i-174-impi-044-ms                     vnl-atk/2016.2
lammps/1116-g-485-ompi-110                        wien2k/17.1-i-14.0.3.174-impi-5.0.2.044
lammps/1116-i-174-impi-044                        wien2k/171-i-174-impi-044(default)
lammps/1218-i-174-impi-044                        xcrysden/1.5.60

----------------------------------- /export/compute/modulefiles/compilers -----------------------------------
gcc/11.2.0           gcc/5.4.0            intel/14.0.3.174     intel/i-174(default)

----------------------------------- /export/compute/modulefiles/libraries -----------------------------------
cuda/11.5                mkl/i-174(default)       mpi/ompi-110             openblas/0.2.18-g-5.4.0
cuda/9.2                 mpi/impi-044(default)    mpi/ompi-1.10            openblas/0.3.18-g-11.2.0
mkl/i-11.1.3.174         mpi/impi-5.0.2.044       mpi/ompi-4.1.1           openblas/218-g-540

----------------------------------- /export/compute/modulefiles/languages -----------------------------------
python/2.7.5           python/3.7.9           python/3.9.1
python/3.6.12          python/3.8.6(default)  python/anaconda3-5.2.0
```

Through the `module avail` command, the user can also **search** for available modules, by partially inserting the module's name. This functionality is demonstrated in the example below.

```bash
[steve@bohr.exabyte.io:~]$ module avail espresso
------------------------------ /export/compute/modulefiles/applications ------------------------------
espresso/511-g-485-ompi-110          espresso/521-i-174-impi-044(default) espresso/540-i-174-impi-044

```

## Actions

See the [module actions documentation](actions/modules-actions.md) for more information on listing, loading, and resetting software modules.


## Links

[^1]: [Wikipedia Environment Modules, Website](https://en.wikipedia.org/wiki/Environment_Modules_(software))
