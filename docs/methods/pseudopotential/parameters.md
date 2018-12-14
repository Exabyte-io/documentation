# Parameters for the Planewave Pseudopotential Method 

We review in this page the most important computational parameters for defining [plane-wave pseudopotential calculations](overview.md), based upon the theoretical framework of the [DFT model](../../models/dft/parameters.md).

## Wavefunction Cutoff

In the global settings section titled "cutoffs" of the "Important Settings" tab under the [Subworkflow Editor](../../workflow-designer/subworkflow-editor/important-settings.md) interface, the user can enter the kinetic energy cutoff of the plane-waves used to represent the electronic wavefunctions. This cutoff value can be entered in the field under the label "wavefunction". It is expressed in the corresponding default energy units for the current [application](../../software/modeling/applications.md) of choice. For example, Rydbergs for [Quantum Espresso](../../software-directory/modeling/quantum-espresso.md), and electronVolts (eV) for the [VASP](../../software-directory/modeling/vasp.md) code.

This cutoff parameter is of crucial importance for establishing the overall accuracy of the DFT calculation, and a judicious choice will usually depend on the conduction of a preliminary [convergence test](../../workflows/addons/convergence-algorithms.md) to ensure that the desired precision in the total energy is reached. For instructions on how to add a preliminary convergence subworkflow add-on to the current workflow, see [this page](../../workflow-designer/subworkflow-editor/actions-menu.md). 

## Charge Density Cutoff

In the text field directly to the right of the plane-waves cutoff parameter for the wavefunction, under the label "density", the user can also set the kinetic energy cutoff (in the same application-dependent units as the previously-described plane-waves cutoff) for the electronic charge density and potential. 

For norm-conserving or PAW pseudopotentials [subtypes](#pseudopotential), a value of four times the aforementioned wavefunction cutoff parameter is recommended, whereas for Ultra-Soft pseudopotentials a higher value between eight and twelve times the wavefunction cutoff is typically more suitable (see the information available under the ["Links"](#links) section below).  

## Pseudopotential

The **type** of **pseudopotential** affects the way the inter-atomic interactions in the crystal structure under investigation are modelled. The following types of pseudopotentials are supported on our platform.

- Ultra-Soft (US)
- Norm-Conserving (NC) 
- Projector-Augmented Wave (PAW) 

Please consult [this page](../../models/dft/parameters.md) for a review of the available pseudopotential **subtypes**, implementing different approximations for the **exchange-correlation functional**.

The "Method" section inside the [Overview Tab](../../workflow-designer/subworkflow-editor/overview-tab.md) of the [Subworkflow Editor interface](../../workflow-designer/subworkflow-editor/overview.md) allows the user to choose which particular pseudopotential file to implement as part of the current subworkflow computations. A comprehensive set of pseudopotentials for most elements in the periodic table is already included on our platform and made available for user selection.

## k-point Sampling

The k-points in the [reciprocal space](../../models/auxiliary-concepts/reciprocal-space.md) of the crystal structure need to be [sampled](../../models/auxiliary-concepts/reciprocal-space/sampling.md), in order to reproduce the electronic structure of the symmetry-irreducible wedge of the Brillouin Zone.

## Electronic Occupations and Smearing

An artificial thermal broadening of the Fermi surface of metallic materials is typically necessary in order to obtain smoother electron occupation distributions than the original step function,  thus making the convergence of properties that need to be integrated across the Fermi surface more effective. 

The various implementations of this "electron smearing" technique, as well as other methods for treating electronic occupancies which might be more suitable for semiconductors and insulators, are reviewed starting from page 175 of Ref. [2] linked in [this page](../../software-directory/modeling/vasp.md).

## Links

For a more in-depth explanation of the theory cited above, the reader is referred to the general review literature on the plane-wave pseudopotential formulation of Density Functional Theory listed in the corresponding [references page](../../models/dft/references.md).
