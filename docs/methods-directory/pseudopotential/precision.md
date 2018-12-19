# Precision of Plane-Wave Pseudopotential Method

At present, we limit the estimation of the [numerical precision](../../methods/precision.md) of plane-wave pseudopotential computations to the following list of parameters, as contained within the [data structure](../../methods/data.md) for methods.

## Plane-wave

### Wavefunction Cutoff

The user can enter the **kinetic energy cutoff** of the **plane-waves** used to represent the electronic wavefunctions. 

### Charge Density Cutoff

The user can also set the **kinetic energy cutoff** for the **electronic charge density and potential**. 

## Reciprocal Space

### k-point Sampling

The k-points in the [reciprocal space](../../models/auxiliary-concepts/reciprocal-space.md) of the crystal structure need to be [sampled](../../models/auxiliary-concepts/reciprocal-space/sampling.md), in order to reproduce the electronic structure of the symmetry-irreducible wedge of the Brillouin Zone.

### Electronic Occupations and Smearing

An artificial thermal broadening of the Fermi surface of metallic materials is typically necessary in order to obtain smoother electron occupation distributions than the original step function,  thus making the convergence of properties that need to be integrated across the Fermi surface more effective. 

The different implementations of this "electron smearing" technique, as well as other methods for treating electronic occupancies which might be more suitable for semiconductors and insulators, are reviewed starting from page 175 of Ref. [2] linked in [this page](../../software-directory/modeling/vasp/overview.md).


## Links

For a more in-depth explanation of the theory cited above, the reader is referred to the general review literature on the plane-wave pseudopotential formulation of Density Functional Theory listed in the corresponding [references page](../../models-directory/dft/references.md).
