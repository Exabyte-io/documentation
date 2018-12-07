# Create Python Environment

Here, we explain how to use the **"virtualenv"** command [^1] within the [Command Line Interface](../overview.md) (CLI) to assemble some commonly used python packages for materials science computations into a **virtual environment**. These packages include the **"pymatgen"**, **"pandas"** and **"atomic simulation environment (ase)"** libraries.

!!! note "Default version of python is 2.7.5"
    By default the system-wide version of python is used.

## Using Virtual Environment

`virtualenv` command can be used by following the instructions presented in its official website [^1]. The installation of a new python package consists of the following sequence of commands, where we also make use of the `pip` package manager [^2] (already installed by default).

```bash
virtualenv .virtualenv
source .virtualenv/bin/activate
```

At this point the CLI prompt will change to reflect that the virtual environment is installed and will look similar to.

```bash
(.virtualenv) [steven@bohr.exabyte.io:~/cluster-001/tmp]$
```

Next, let's install the desired package(s). Here we use "pymatgen", further explained below.

```bash
pip install pymatgen
```

Check that installation is successful (exit code of zero means everything OK).

```bash
python -c "import pymatgen" && echo $?
0
```

Now one can execute the scripts requiring the installed package as follows, for example.

```bash
python script.py
```

In order to disable the virtual environment and return to the original default command line, enter the following.

```bash
deactivate
```

## Example Python Packages

We support the following python packages in our platform.

### Pymatgen

**Python Materials Genomics (pymatgen)** [^3] is a materials analysis code that defines core object representations for crystal structures and molecules, with support for many electronic structure codes. It is currently the core analysis engine powering the **Materials Project** [^4] online database of material structures. 

### Pandas 
 
**Pandas** is a python software library for data manipulation and analysis [^5]. In particular, it offers data structures and operations for manipulating numerical tables and time series.

### Atomic Simulation Environment

The **Atomic Simulation Environment (ASE)** is a set of tools and python modules for setting up, manipulating, running, visualizing and analyzing atomistic simulations [^6]. 

## Links

[^1]: [Virtualenv, Official Website](https://virtualenv.pypa.io)

[^2]: [Wikipedia Pip package manager, Website](https://en.wikipedia.org/wiki/Pip_(package_manager))

[^3]: [pymatgen, Official Website](http://www.pymatgen.org)

[^4]: [Materials Project, Official Website](https://materialsproject.org/)

[^5]: [Pandas, Official Website](https://pandas.pydata.org/)

[^6]: [Atomic Simulation Environment, Official Website](https://wiki.fysik.dtu.dk/ase/)
