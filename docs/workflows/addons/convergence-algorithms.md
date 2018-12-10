<!-- TODO: TB to review more in details -->

# Convergence algorithms

This feature is accessible as a stand-alone workflow or as an add-on / modifier to an existing subworkflow during in [Wokflow Designer](../../workflow-designer/overview.md).

## Example algorithm

We will explain convergence based on the study of the number of sampling points (k-points) in reciprocal cell.

In most cases in order to achieve precision the total energy should not increase significantly when the k-point density is increased. Below you can see the flowchart of the optimization algorithm used to find the optimal density.

<img src="/images/workflows/KpointConvergenceDiagram.png" style="width: 560px">

Here we use a uniform k-point mesh (same in each of the three spatial directions) and first initiate the number of kpoints `N_K` at 1. We then run self-consistent density functional theory calculation (`pw_scf` - using Quantum ESPRESSO's terminology) and check whether the `Output` value difference at current step and at previus one (`x`) is less than convergence threshold.

## Details

Currently the default k-point convergence algorithm systematically increments the starting k-point density by 1 in along each reciprocal lattice vector until the total energy of the system does not increase by more than 0.001% (10^-5).
  
<!-- TODO: revise or remove gif -->
<!-- <img data-gifffer="/images/workflows/AddKpointConvergence.gif" /> -->

Please see the [k-point convergence tutorial](../../tutorials/dft/kpt-convergence.md) for more details.

> Some properties, especially those depending on atomic forces, derivatives of the total energy, and displacements or perturbation, are highly dependent upon the quality of convergence and relaxation. For example accurate calculation of zero point energy requires a well converged k-point grid to sample the total energy space when atoms are displaced from their equilibrium positions.
