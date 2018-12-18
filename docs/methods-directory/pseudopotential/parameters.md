# Parameters for the Plane-wave Pseudopotential Method 

We review in this page the most important computational parameters for defining [plane-wave pseudopotential calculations](overview.md), based upon the theoretical framework of the [DFT model](../../models-directory/dft/overview.md).

These parameters can be set under the [Subworkflow Editor](../../workflow-designer/subworkflow-editor/overview.md) interface of our platform.

## Wavefunction Cutoff

The user can enter the **kinetic energy cutoff** of the **plane-waves** used to represent the electronic wavefunctions. 

## Charge Density Cutoff

The user can also set the **kinetic energy cutoff** for the **electronic charge density and potential**. 

## Pseudopotential

The **type** of **pseudopotential** affects the way the inter-atomic interactions in the crystal structure under investigation are modelled. The following types of pseudopotentials are supported on our platform.

- Ultra-Soft (US)
- Norm-Conserving (NC) 
- Projector-Augmented Wave (PAW) 

Please consult [this page](../../models-directory/dft/overview.md) for a review of the available pseudopotential **subtypes**, implementing different approximations for the **exchange-correlation functional**.

## k-point Sampling

The k-points in the [reciprocal space](../../models/auxiliary-concepts/reciprocal-space.md) of the crystal structure need to be [sampled](../../models/auxiliary-concepts/reciprocal-space/sampling.md), in order to reproduce the electronic structure of the symmetry-irreducible wedge of the Brillouin Zone.

## Electronic Occupations and Smearing

An artificial thermal broadening of the Fermi surface of metallic materials is typically necessary in order to obtain smoother electron occupation distributions than the original step function,  thus making the convergence of properties that need to be integrated across the Fermi surface more effective. 

The different implementations of this "electron smearing" technique, as well as other methods for treating electronic occupancies which might be more suitable for semiconductors and insulators, are reviewed starting from page 175 of Ref. [2] linked in [this page](../../software/modeling/vasp.md).

## Links

For a more in-depth explanation of the theory cited above, the reader is referred to the general review literature on the plane-wave pseudopotential formulation of Density Functional Theory listed in the corresponding [references page](../../models-directory/dft/references.md).
