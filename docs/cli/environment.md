# Command-line Environment

The present page explains the environment setup for a [command-line session](overview.md) within our platform. The **Environment** is an important concept in the Unix operating system [^1]. It is defined in terms of **environment variables** [^2], some of which are set by the system, others by the user, yet others by the shell or by any program that loads another program.

After logging into our platform via the Command Line Interface (CLI), the user will by default enter the [Login Home](../infrastructure/login/directories.md) directory, from which other nodes of the [infrastructure](../infrastructure/overview.md) can be accessed.

## Customization

The CLI environment can be **customized** by the user in two respects: by choosing the **Shell type**, and through the **loading of predefined Modules**, which include numerous commonly-used simulation codes and associated libraries.  

This customization can be controlled via certain **startup scripts**, which are executed when the user first logs into the CLI. The user can customize some of these scripts, which are called "dot files," by setting environment variables and aliases in them as explained in what follows.

## Shell Type

The **Shell type** [^3] can modify the way that the user can interact with the CLI by, for example, introducing new commands or key shortcuts. For example, Ref. [^4] explains how bash differs from zsh. The different shell types that are available as part of our product, and can be chosen from by the user, are listed below.

- **sh** [^5]
- **bash** [^6]
- **csh** [^7]
- **ksh** [^8]
- **zsh** [^9]

!!!info "ZSH"
    We use **oh-my-zsh**, a community-driven framework for managing the zsh configuration. For more information, please visit its official website [^10].

The default shell is set to bash. The user can change shell from this default setting by following the instructions contained [in this page](actions/customize.md).

## Python Environment

By default, we implement **python 2.7.5** as our main system version. Different python versions can be installed via the the instructions and code contained in Ref. [^11].

Additionally, we explain how to create customized **python environments** [here](actions/create-python-env.md).

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
## Links

[^1]: [Wikipedia UNIX, Website](https://en.wikipedia.org/wiki/Unix)

[^2]: [Wikipedia Environment variable, Website](https://en.wikipedia.org/wiki/Environment_variable)

[^3]: [Wikipedia Unix shell, Website](https://en.wikipedia.org/wiki/Unix_shell)

[^4]: [Zsh vs Bash, Website](https://stackabuse.com/zsh-vs-bash/)

[^5]: [Wikipedia Bourne shell, Website](https://en.wikipedia.org/wiki/Bourne_shell)

[^6]: [Wikipedia Bash (Unix shell), Website](https://en.wikipedia.org/wiki/Bash_(Unix_shell))

[^7]: [Wikipedia C shell, Website](https://en.wikipedia.org/wiki/C_shell)

[^8]: [Wikipedia Korn Shell, Website](https://en.wikipedia.org/wiki/KornShell)

[^9]: [Wikipedia Z Shell, Website](https://en.wikipedia.org/wiki/Z_shell)

[^10]: [Oh My ZSH!, Official Website](https://ohmyz.sh/)

[^11]: [Simple Python Version Management: pyenv, Official GitHub Repository](https://github.com/pyenv/pyenv)
