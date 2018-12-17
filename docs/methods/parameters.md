# Parameters

We refer to **parameters** as any computational setting that can influence the execution of a simulation, via the implementation of any given [method](overview.md). An appropriate choice of parameters is important since they can typically have an impact upon the [precision](precision.md) of the computation, and for this reason the conduction of [convergence tests](../workflows/addons/convergence-algorithms.md) is often recommended.

## Examples

For example, for the case of [parameters involved in DFT computations](../methods-directory/pseudopotential/parameters.md), the precision is mainly affected by the choice of parameters such as the plane-wave cutoff energy and size of the grid of reciprocal k-points.   

For the case of the classical Molecular Dynamics method on the other hand, important computational parameters to bear in mind for reproducing the desired effects with the appropriate precision consist for example in the size of the simulation box, corresponding to a sufficient total number of atoms. The correct choice for the parametric form of the inter-atomic potential is also very important.
