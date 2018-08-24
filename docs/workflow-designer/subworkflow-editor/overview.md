# The Overview tab

The general appearance of the typical content of the "Overview" tab is presented in the image below, where four main sections are emphasized and will be described in turn throughout the rest of this documentation page:

<img src="/images/overview-tab.png"/>

# The "Properties" section

> NOTE: this section is not present for newly-created subworkflows

The first line in the "Overview" tab, labeled "Properties", contains a summary of the physical quantities that will be computed during the course of the present materials calculation. These can be selected from a list of properties on the "Detailed View" tab, which is described in this alternative [part of the documentation](detailed-view.md). 

For a complete list of physical properties available for calculation, the reader is referred to [this page](../../materials/properties.md).

## Low-fidelity Runs

Optionally, the check-box "Draft" on the left can be selected. In this case the resulting properties will not be available in the "Analytics" part of the output of the calculation. This option is convenient to choose when new prototypical workflows need simply to be trialled and tested rapidly and in a preliminary fashion through low-fidelity runs.

# The "Application" section

The subsequent "Application" section in the "Overview" tab allows you to choose which computational engine (otherwise known as application) to employ for the current calculation and in which version, through the corresponding drop-down menus. The Exabyte platform currently offers the choice between two widely used and highly-reliable first-principle DFT software packages, Quantum Espresso (the default choice) and VASP, as well as our own Exabyte Machine Learning Engine. The options to write a Shell or a Python script manually are also offered in the same drop-down menu on the left. 

The reader who is interested in learning more about the detailed numerical implementations of such quantum mechanical calculations in both the Quantum Espresso and VASP application codes is referred to their documentation pages, to be found [here](../../applications/quantum-espresso.md) and [here](../../applications/vasp.md) respectively.

# The "Model" section

The "Model" section refers to the general theoretical approach which is to be considered as part of the current subworkflow. For the moment, the Exabyte platform offers the following combination of model type and subtypes, already selected by default in any newly-created subworkflow. The theoretical background underlying such model concepts is reviewed further in [this page](../../models/dft/overview.md). 
 
 
- We consider **Density Functional Theory** (DFT) as our conventional model.
 
- We assume the **Generalized Gradient Approximation** (GGA) for the Exchange-Correlation part of the total energy functional of the crystal being studied. 

- The particular flavor of GGA functional implemented in the Exabyte Platform is the one due to **Perdew, Burke and Ernzerhof** (PBE).

## Refiners 

The "Refiners" drop-down menu immediately below the model's type and subtypes selections offers the user the possibility to display additional calculated physical properties in separate dedicated columns, once the output of the workflow computation is visualized in the "Jobs" page of the Exabyte platform. 

Note that the inclusion of such refiners from within the Subworkflow Editor interface does not make them an integral part of the workflow computation per se (something that still needs to be done manually by editing the corresponding input script), but rather refers exclusively to the way the output data columns themselves are presented.

## Modifiers

Please refer to [this page](../../models/dft/modifiers.md) for a physical description of the available modifiers.

# The "Method" section

In the method section the user is allowed to choose the computational aspects of the current subworkflow calculation, and in particular the type of potential modeling the inter-atomic interactions in the crystal structure under investigation. Please consult [this page](../../methods/pseudopotential/actions.md) for a review of the available pseudopotentials within the theoretical context of the DFT model.


