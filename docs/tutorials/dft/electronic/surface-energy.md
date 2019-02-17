# Calculate Surface Energy

This tutorial page explains how to calculate the [surface energy](../../../properties-directory/scalar/surface-energy.md) of [materials](../../../materials/overview.md) based on [Density Functional Theory](../../../models-directory/dft/overview.md). We consider crystalline silicon in its standard equilibrium cubic-diamond crystal structure, and use [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) as our main simulation engine during this tutorial.

## Verifications

In order to enable the surface energy calculations, the following checks have to be performed:

- Surface and bulk structures must have the same relative concentrations of equivalent elements. This means that if we have, for example, Si as the starting bulk structure, then the surface can only have Si and another element. Alternatively, if we have SrTiO3 as the bulk, then the surface has to have 1 to 1 to 3 ratio of Sr, Ti and O, beyond having passivation elements (like H).

- Surface and bulk structures have to have "commensurate" structure factors, i.e. the structure factor for the surface has to be equal to that for the bulk, with possibly some addition(s) due to passivation.

- The calculation of a slab has to have identical surfaces on top and bottom. Thus, a symmetry check has to be imposed. Secondly, there has to be a previous calculation in the database that contains the value for the bulk energy. If no such calculation is available, then it has to be executed. The bulk value has to be calculated with the same [method](../../../methods/overview.md) and [parameter setup](../../../methods/parameters.md) as the slab.

Additional checks are to be considered a posteriori:

- In order to have a true surface (and not a slab), where only one surface state is present effectively (as opposed to two states on two sides interacting with each other as in a slab of finite thickness), one has to assert the thickness of the surface to be large enough for the surface state wavefunction to "die off" within the bulk region.

## Workflow Structure

We shall now describe the computational implementation of Surface Energy calculations on our platform, illustrating the various steps constituting the overall [Workflow](../../../workflows/overview.md) based on [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md).


