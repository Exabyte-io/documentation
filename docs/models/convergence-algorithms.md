<!-- by TB -->

The process of finding input parameters that deliver a certain level of precision for the properties extracted in the output is called **convergence study**.

!!! note "Relaxation is also critical to ensure fidelity of end results"
    [**structural relaxation**](structural-relaxation.md) also serves a similar purpose.

# Convergence algorithm

In most cases to ensure fidelity the total energy should not increase significantly when the k-point density is increased.  This search for the appropriate density of k-points is called k-point convergence. Below you can see the flowchart of the optimization algorithm used:

<img src="/images/kpointConvergenceDiagram.png" style="width: 560px">

Here we use a uniform k-point mesh (same in each of the three spatial directions) and first initiate the number of kpoints `N_K` at 1. We then run self-consistent density functional theory calculation (`pw_scf` - using Quantum ESPRESSO's terminology) and check whether the `Output` value difference at current step and at previus one (`x`) is less than convergence threshold.

# Details

Currently our k-point convergence algorithm systematically increments the starting k-point density by 1 in each lattice vector direction until the total energy of the system does not increase by more than 0.001 eV.  This feature is accessible as an stand-alone workflow or as an add-on initial step before the final total energy or property calculation desired (similar to relaxation).

<img data-gifffer="/images/AddKpointConvergence.gif" />

Please see the [k-point convergence tutorial](../tutorials/kpt-convergence.md) for more details.

If both k-point convergence and relaxation preparation steps are added to your simulation flow the k-point convergence flow will be executed prior to the relaxation flow.

!!! warning "Beware of k-point convergence on large systems"
    Due to system size the search for k-point convergence can be a computationally intensive. When working with systems with over hundreds of atoms it may be necessary to do first do k-point convergence on a smaller system of simular character and constituents and use that density as a proxy to calculate the converged k-point density. In most cases for large cells gamma point sampling is already sufficient.

Some properties, especially those depending on atomic forces, derivatives of the total energy, and displacements or perturbation, are highly dependent upon the quality of convergence and relaxation. For example accurate calculation of zero point energy requires a very well converged k-point grid to sample the total energy space when atoms are displaced from their equilibrium positions.

Other input parameters may also be important depending upon the desired property.  For example when calculating dielectiric property it is important to ensure there is a surplus of unoccupied bands in the structure to ensure accuracy.
