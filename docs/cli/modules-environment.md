<!-- by MM -->

This page explains the environment setup for a command-line session with exabyte.io.

## Overview

When you log in to exabyte.io via command-line, you are in your global $HOME directory. You initially land in the same place all the time. This means that if you have files or binary executables that are located in your home directory, they will be available on all cluster nodes through a network-shared filesystem.

## Customizing Environment

The way you interact with compute resources can be controlled via certain startup scripts that run when you log in and at other times.  You can customize some of these scripts, which are called "dot files," by setting environment variables and aliases in them.

## Choosing Shell Type

When as a CLI user, there are different shell types you can use, sh, bash, csh, ksh an zsh. The default shell is set to bash. You can change your default shell by running change_shell command, for example to change your shell to zsh run `change_shell /bin/zsh`.

!!! tip "ZSH"
    We use oh-my-zsh, a delightful community-driven framework for managing zsh configuration. For more information please visit [oh-my-zsh](http://ohmyz.sh).

There are several "standard" dot-files that are symbolic links to read-only files that Exabyte.io controls. Thus, you should NEVER modify or try to modify such files as .bash_profile, .bashrc, .cshrc, .kshrc, .login, .profile, or .zshrc. Instead, you should put your customizations into files that have a ".ext" suffix, such as .bashrc.ext, .cshrc.ext, .kshrc.ext, .login.ext, .profile.ext, and .zshrc.ext. Which of those you modify depends on your choice of shell, although note that we recommend bash.

The table below contains examples of basic customizations directives one can put inside dot files. Note that when making changes such as these it's always a good idea to have two terminal sessions active so that you can back out changes if needed!

| Bash                  | Csh                   |
|:-------------------   |:-------------------   |
| `export ENVAR=var`    | `setenv ENVAR var`    |
| `alias ll='ls -lrt’`  | `alias ll “ls –lrt”`  |


## Using Modules

Easy access to software is controlled by the *modules* utility. With modules, you can easily manipulate your computing environment to use applications and programming libraries. If you want to change the environment you "load," "unload," and "swap" modules. A small set of module commands can do most of what you'll want to do.

### module list

The first command of interest is "module list", which will show you your currently loaded modules. When you first log in, you have NO modules loaded for you. Here is an example:

```bash
[steve@bohr.exabyte.io:~]$ module list
Currently Loaded Modulefiles:
  1) intel/i-174(default)    2) mpi/impi-044(default)    3) mkl/i-174(default)    4) espresso/521-i-174-impi-044(default)
```

### module avail

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

### module load

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

### module purge

You can use "module purge" command to clean your environment and deactivate all current loaded modules.

```bash
[steve@bohr.exabyte.io:~]$ module list
Currently Loaded Modulefiles:
  1) intel/i-174(default)    2) mpi/impi-044(default)    3) mkl/i-174(default)    4) espresso/521-i-174-impi-044(default)
[steve@bohr.exabyte.io:~]$ module purge
[steve@bohr.exabyte.io:~]$ module list
No Modulefiles Currently Loaded.
```
