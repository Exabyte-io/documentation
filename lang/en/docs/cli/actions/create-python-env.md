# Create Python Environment

Here, we explain how to use the **"virtualenv"** command [^1] within the [Command Line Interface](../overview.md) (CLI) to assemble some commonly used python packages for materials science computations into a **virtual environment**. These packages include the **"pymatgen"**, **"pandas"** and **"atomic simulation environment (ase)"** libraries.

!!! note "Default version of Python is 2.7.5"
    By default, the system-wide Python 2.7.5 is available.  Other versions of Python are available for use; see [the Command Line Environment documentation's section on Python](../environment.md#default-python-environment) for more details.  

## Using Virtual Environment

The `virtualenv` command can be used by following the instructions presented in its official website [^1]. The installation of a new Python package consists of the following sequence of commands, where we also make use of the `pip` package manager [^2] (already installed by default).

First, we'll create a new virtual environment, as a directory named `.virtualenv` in the current directory, and then activate it:

```bash
virtualenv .virtualenv
source .virtualenv/bin/activate
```

At this point the CLI prompt will change to reflect that the virtual environment is active and will look similar to:

```bash
(.virtualenv) [steven@bohr.exabyte.io:~/cluster-001/tmp]$
```

Next, let's install the desired package(s). Here we use "pymatgen", further explained below:

```bash
pip install pymatgen
```

Check that installation is successful (exit code of zero means everything OK):

```bash
python -c "import pymatgen" && echo $?
0
```

Now one can execute the scripts requiring the installed package as follows, for example:

```bash
python script.py
```

In order to disable the virtual environment and return to the original default command line, enter the following.

```bash
deactivate
```

To reactivate an existing virtual environment, source the virtual environment's `activate` script again:

```bash
source .virtualenv/bin/activate
```

## Other Versions of Python

As noted above, the default version of Python can be overridden with any of the ways described in  [the Command Line Environment documentation's section on Python](../environment.md#default-python-environment).

Once the chosen version of Python is active, virtual environments can be created as expected and packages installed and code executed against that version.  For example, using the Environment Module approach:

```bash
module load python/3.8.6
python --version
# Python 3.8.6

virtualenv .virtualenv_py3
source .virtualenv_py3/bin/activate

python --version
# Python 3.8.6
```

Note that once a Python virtual environment is created, its Python version is permanent and it's not possible to switch to a different version.  In that case, a new virtual environment with a different path will need to be created.

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
