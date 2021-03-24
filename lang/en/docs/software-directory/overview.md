# List of Available Software

We list in the present page the [software](../software/overview.md) available on our platform, accessible via the appropriate [connection method](../remote-connection/overview.md). The reader is referred to the introductory pages dedicated to each of the packages listed here, by clicking the links contained below. Dedicated pages contain references to the relevant documentation explaining the operations of the corresponding software in detail.

## Access Scenarios

Tools can be accessed through one or more of the following methods:
 
 1. The main user interface (in the [subworkflow editor](../workflow-designer/subworkflow-editor/overview.md)), 
 2. Remote Desktop (we provide and example for [VESTA](analysis/vesta.md)) in [this page](../remote-connection/actions-rd/open-app.md),
 3. [Environment Modules](../cli/modules.md) in [command line interface](../cli/overview.md).


## Modeling Applications

The platform currently offers the choice between the following software engines for modeling, otherwise known as **[applications](../software/components.md)**.

| Name    |  Version(s)      | Access Scenarios (see previous section)      |
| :-------- | ----------- | -------------|
| [Quantum ESPRESSO](modeling/quantum-espresso/overview.md) | 5.1-6.3 | 1, 3|
| [VASP](modeling/vasp/overview.md)      | 5.3.5-5.4.4 | 1, 3 |
| [LAMMPS](modeling/lammps.md)    | 11-2016 | 3 |
| [NWChem](modeling/nwchem.md)    | 6.6     | 3 |
| [CP2K](modeling/cp2k.md)      | 4.1     | 3 |
| [GROMACS](modeling/gromacs.md) |   5.1.4  | 3 |
| [Turbomole](modeling/turbomole.md) | 7.0     | 2, 3 |
| [WIEN2k](modeling/wien2k.md) | 17.1     | 3 |

## Machine Learning

We have a proof-of-concept support for [machine learning](../models-directory/machine-learning/overview.md) through [Exabyte-ML](machine-learning/exabyte/overview.md). This application is accessible via the [subworkflow editor interface](../workflow-designer/subworkflow-editor/overview.md) only.

## Analysis Tools

We support the following structural analysis and visualization tools through a [remote desktop connection](../remote-connection/remote-desktop.md). The reader may click each entry listed below to be redirected to the software's corresponding documentation introduction.

| Name      |  Version(s) | Access Scenarios (see previous section) |
| :-------- | ----------- | ------------- |
| [VMD](analysis/vmd.md) | 1.9.3 | 2, 3 |
| [XCRYSDEN](analysis/xcrysden.md) |  1.5.60 | 2, 3 |
| [VESTA](analysis/vesta.md)  | 3.3.8 | 2, 3 |
| [P4VASP](analysis/p4vasp.md) |  0.3.30 | 2, 3 |

!!!info "Opening graphical software in remote desktop"
    An example on how to open a graphical structural visualization tool in our remote desktop environment is provided [under this page](../remote-connection/actions-rd/open-app.md).

## Scripting Applications

Our platform includes support for two widely-used scripting languages, [shell scripting](scripting/shell/overview.md) and [python](scripting/python/overview.md), which are introduced in their respective documentation pages. 

For command line users we provide a system-default python installation, and recommend users to employ virtual environments for controlling the versions of python packages in [Command Line Interface](../cli/overview.md), as explained [in this page](../cli/actions/create-python-env.md).

## Development Tools

Users of our [Command Line Interface](../cli/overview.md) have at their disposal a comprehensive set of development [compilers](development/compilers.md) and [libraries](development/libraries.md), as well as of [text editors](development/text-editors.md) for inspecting or editing the relevant scripts and simulation files.
