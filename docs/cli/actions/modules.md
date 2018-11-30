### List Currently Loaded Modules

The first command of interest is "module list", which will show you your currently loaded modules. When you first log in, you have NO modules loaded for you. Here is an example:

```bash
[steve@bohr.exabyte.io:~]$ module list
Currently Loaded Modulefiles:
  1) intel/i-174(default)    2) mpi/impi-044(default)    3) mkl/i-174(default)    4) espresso/521-i-174-impi-044(default)
```

### List Available Modules

Let's say you want to use a simulation engine. `module avail` command will list all the available modules.

```bash
[steve@bohr.exabyte.io:~]$ module avail
----------------------------- /export/compute/modulefiles/system -----------------------------
emacs/24.5

------------------------------------------ /export/compute/modulefiles/applications ------------------------------------------
espresso/511-g-485-ompi-110          espresso/540-i-174-impi-044          vasp/535-i-174-impi-044(default)     vesta/3.3.8
espresso/521-i-174-impi-044(default) vasp/535-g-485-ompi-110              vasp/535-i-174-impi-044-nc           xcrysden/1.5.60

--------------------------- /export/compute/modulefiles/compilers ----------------------------
gcc/5.4.0            intel/i-174(default)

--------------------------- /export/compute/modulefiles/libraries ----------------------------
mkl/i-174(default)    mpi/impi-044(default) mpi/ompi-110          openblas/218-g-540
```

You can use the module's name stem to do a useful search:

```bash
[steve@bohr.exabyte.io:~]$ module avail espresso
------------------------------ /export/compute/modulefiles/applications ------------------------------
espresso/511-g-485-ompi-110          espresso/521-i-174-impi-044(default) espresso/540-i-174-impi-044

```

### Load Desired Module

If you want to use [Quantum ESPRESSO](http://quantum-espresso.org) application, you can "load" or "add" the corresponding module.

```bash
[steve@bohr.exabyte.io:~]$ module load espresso/521-i-174-impi-044
The module intel/i-174 is loaded
The module mpi/impi-044 is loaded
The module intel/i-174 is loaded
The module mkl/i-174 is loaded
The module espresso/521-i-174-impi-044 is loaded
```

Now you can invoke Quantum ESPRESSO by typing `pw.x < <input_file>` command, where `<input_file>` is the path to the input file.

If there is a "default" keyword in front of a module name, you can load it without specifying the full module name.

```bash
[steve@bohr.exabyte.io:~]$ module add espresso
The module intel/i-174 is loaded
The module mpi/impi-044 is loaded
The module intel/i-174 is loaded
The module mkl/i-174 is loaded
The module espresso/521-i-174-impi-044 is loaded
```

### Purge all Loaded Modules

You can use "module purge" command to clean your environment and deactivate all current loaded modules.

```bash
[steve@bohr.exabyte.io:~]$ module list
Currently Loaded Modulefiles:
  1) intel/i-174(default)    2) mpi/impi-044(default)    3) mkl/i-174(default)    4) espresso/521-i-174-impi-044(default)
[steve@bohr.exabyte.io:~]$ module purge
[steve@bohr.exabyte.io:~]$ module list
No Modulefiles Currently Loaded.
```
