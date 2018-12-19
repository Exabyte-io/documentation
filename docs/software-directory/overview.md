# List of Available Software

We list in the present page the [software](../software/overview.md) available on our platform, accessible via the appropriate [connection method](../remote-connection/overview.md). The reader is referred to the introductory pages dedicated to each of the packages listed here, by clicking the links contained below. Dedicated pages contain references to the relevant documentation explaining the operations of the corresponding software in detail.

## Modeling Applications

The platform currently offers the choice between the following modeling software engines, otherwise known as **[applications](../software/components.md)**. Some applications have extensive integrated support in the user interface, and others are currently available through [command line terminal](../cli/overview.md) only.

| Name    |  Version(s)      | Notes      |
| :-------- |:----------- |:------------- |
| [Quantum ESPRESSO](modeling/quantum-espresso/overview.md) | 5.1-6.0 | Fully integrated |
| [VASP](modeling/vasp/overview.md)      | 5.3.5-5.4.4 | Fully integrated |
| [LAMMPS](modeling/lammps.md)    | 11-2016 | Available through command line |
| [NWChem](modeling/nwchem.md)    | 6.6     | Available through command line |
| [CP2K](modeling/cp2k.md)      | 4.1     | Available through command line |
| [GROMACS](modeling/gromacs.md) |   5.1.4  | Available through command line |
| [Turbomole](modeling/turbomole.md) | 7.0     | Available through remote desktop |

!!!info "Loading Modeling Applications via Command Line Interface"
    We package modeling software available via Command Line Interface as pre-compiled [modules](../cli/modules.md). Instructions on how such modules can be loaded and made available for use can be found [here](../cli/actions/modules-actions.md).

## Analysis Tools

We support the following structural analysis and visualization tools through a [remote desktop connection](../remote-connection/remote-desktop.md). The reader may click each entry listed below to be redirected to the software's corresponding documentation introduction.

| Name      |  Version(s) | Notes         |
| :-------- |:----------- |:------------- |
| [VMD](analysis/vmd.md) | 1.9.3 | Available through remote desktop |
| [XCRYSDEN](analysis/xcrysden.md) |  1.5.60 | Available through remote desktop |
| [VESTA](analysis/vesta.md)  | 3.3.8 | Available through remote desktop |
| [P4VASP](analysis/p4vasp.md) |  0.3.30 | Available through remote desktop |

!!!info "Opening graphical software in remote desktop"
    An example on how to open a graphical structural visualization tool in our remote desktop environment is provided [under this page](../remote-connection/actions-rd/open-app.md).


## Scripting Applications

Our platform includes support for two widely-used scripting languages, [shell scripting](scripting/shell.md) and [python](scripting/python.md), which are introduced in their respective documentation pages. 

For command-line users we provide a system-default python installation, and recommend users to employ virtual environments for controlling the versions of python packages in [Command Line Interface](../cli/overview.md), as explained [in this page](../cli/actions/create-python-env.md).

## Development

Users of our [Command Line Interface](../cli/overview.md) have at their disposal a comprehensive set of development [compilers](development/compilers.md) and [libraries](development/libraries.md), as well as of [text editors](development/text-editors.md) for inspecting or editing the relevant scripts and simulation files.