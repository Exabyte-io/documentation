

## Modeling Applications

The platform currently offers the choice between the following modeling software engines, otherwise known as **[applications](../software/modeling/applications.md)**. Some of these applications (Quantum ESPRESSO and VASP, for instance) have extensive integrated support in the user interface, and others are currently available through [command line terminal connection](../cli/overview.md) only. Click on the name of the application below to navigate to the corresponding part of the documentation.

| Name    |  Version(s)      | Notes      |
| :-------- |:----------- |:------------- |
| [Quantum ESPRESSO](modeling/quantum-espresso.md) | 5.1-6.0 | Fully integrated |
| [VASP](modeling/vasp.md)      | 5.3.5-5.4.4 | Fully integrated (*) |
| [LAMMPS](modeling/lammps.md)    | 11-2016 | Available through command line |
| [NWChem](mdeling/nwchem.md)    | 6.6     | Available through command line |
| [CP2K](modeling/cp2k.md)      | 4.1     | Available through command line |
| [GROMACS](modeling/gromacs.md) |        | Available through command line |
| [Turbomole](modeling/turbomole.md) | 7.0     | Available through remote desktop |

> * VASP is available for current licensees and on-demand for users with academic affiliations

## Structural Analysis and Visualization Tools

### Graphical

We support the following structural analysis and visualization tools through a [remote desktop connection](../remote-connection/remote-desktop.md). The reader may click each entry listed below to be redirected to the software's corresponding documentation introduction.

| Name      |  Version(s) | Notes         |
| :-------- |:----------- |:------------- |
| [VMD](vmd.md) | 1.9.3 | Available through remote desktop |
| [XCRYSDEN](xcrysden.md) |  1.5.60 | Available through remote desktop |
| [VESTA](vesta.md)  | 3.3.8 | Available through remote desktop |
| [P4VASP](p4vasp.md) |  0.3.30 |  |

### Python-based

For command-line users we provide system system-default python installation and suggest for users to employ virtual environment for controlling the versions for python packages, as explained [in this page](../cli/actions/create-python-env.md).

## Scripting

Our platform includes support for two widely-used scripting languages, [shell scripting](scripting/shell.md) and [python](scripting/python.md), which are introduced in their respective documentation pages.

## Development

Users of our [Command Line Interface](../cli/overview.md) have at their disposal a comprehensive set of development [compilers](development/compilers.md) and [libraries](development/libraries.md).
