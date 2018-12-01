# Create Python Environment

Here, we explain how to use the **"virtualenv"** module [^1] within the [Command Line Interface](../overview.md) (CLI) to assemble some commonly used python packages for materials science computations into a **virtual environment**. These packages include the **"pymatgen"**, **"pandas"** and **"atomic simulation environment (ase)"** libraries.

## How to Use Virtualenv

Virtualenv can be used by following the instructions presented in its official website [^1]. The installation of a new python package under virtualenv, in its simplest version, consists in the following sequence of commands, where we also make use of the `pip` package manager [^2] (already installed on the CLI by default).

```bash
virtualenv .virtualenv
source .virtualenv/bin/activate
pip install <some-package-name>
```

To finally disable the virtual environment and return to the original default command line, enter the following.

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
