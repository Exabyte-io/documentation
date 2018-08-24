# Plane-waves cutoff

In the global settings section titled "cutoffs" of the "Important Settings" tab under the Subworkflow Editor interface, the user can enter the kinetic energy cutoff of the plane-waves used for expanding the ground-state electronic wavefunction solution to the corresponding Schroedinger Equation of the crystal (within the limits and approximations of Density Functional Theory). This cutoff value can be entered in the field under the label "wavefunction". This cutoff is expressed in units of Rydbergs when Quantum Espresso is used as the main simulation engine, or alternatively in units of electronVolts (eV) for the case of VASP.

This cutoff parameter is of crucial importance for establishing the overall accuracy of the DFT calculation, and a judicious choice will usually depend on the conduction of a preliminary convergence test to ensure that the desired precision in the total energy is reached. For instructions on how to add a preliminary convergence subworkflow add-on to the current workflow, please see [this page](../../workflow-designer/subworkflow-editor/actions-menu.md). 

# Charge density cutoff

In the text field directly to the right of the plane-waves cutoff parameter for the wavefunction, under the label "density", the user can also set the kinetic energy cutoff (in the same application-dependent units as the previously-described plane-waves cutoff) for the electronic charge density and potential. 

For norm-conserving or PAW pseudopotentials subtypes, a value of four times the afore-mentioned wavefunction cutoff parameter is recommended, whereas for Ultra-Soft pseudopotentials a higher value between eight and twelve times the wavefunction cutoff is typically more suitable.  

# Links

For a more in-depth explanation of the theory underlying plane-waves and charge density expansion basis sets and cutoffs, the reader is referred to the general review literature on DFT concepts listed in the [main references page](/models/dft/references.md).
