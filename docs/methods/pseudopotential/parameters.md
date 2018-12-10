# Wavefunction Cutoff

In the global settings section titled "cutoffs" of the "Important Settings" tab under the [Subworkflow Editor](../../workflow-designer/subworkflow-editor/important-settings.md) interface, the user can enter the kinetic energy cutoff of the plane-waves used to represent the electronic wavefunctions. This cutoff value can be entered in the field under the label "wavefunction". This cutoff is expressed in the corresponding default energy units for the current application of choice. For example, Rydbergs for Quantum Espresso, electronVolts (eV) for VASP

This cutoff parameter is of crucial importance for establishing the overall accuracy of the DFT calculation, and a judicious choice will usually depend on the conduction of a preliminary convergence test to ensure that the desired precision in the total energy is reached. For instructions on how to add a preliminary convergence subworkflow add-on to the current workflow, see [this page](../../workflow-designer/subworkflow-editor/actions-menu.md). 

## Charge Density Cutoff

In the text field directly to the right of the plane-waves cutoff parameter for the wavefunction, under the label "density", the user can also set the kinetic energy cutoff (in the same application-dependent units as the previously-described plane-waves cutoff) for the electronic charge density and potential. 

For norm-conserving or PAW pseudopotentials subtypes, a value of four times the afore-mentioned wavefunction cutoff parameter is recommended, whereas for Ultra-Soft pseudopotentials a higher value between eight and twelve times the wavefunction cutoff is typically more suitable (see the information available under the "Links" section below).  

## Links

For a more in-depth explanation of the theory the above the reader is referred to the general review literature on the pseudopotential Density Functional Theory concepts listed in the corresponding [references page](../../models/dft/references.md).
