<!-- TODO by MH -->

One of the most important things to learn about atomic simulations is that it is critical how you prepare your structures and inputs to ensure you can trust your results. A study of input file settings with individual simulations on the same structure versus some result is called a convergence study.  The focus of most convergence studies are to determine the lowest possible energy state of your material system with the minimum computational settings.

!!! Note "Relaxation is also critical for quality of results"
    Please note that although not technically convergence, [**relaxation**](structural-relaxation.md) of structures also serves a similar purpose to ensure your calculation is computing the lowest total energy state of the material that you can trust.

# Current convergence workflow (K-points):

In most cases to have a reasonable level of confidence that a result can be trusted the total energy should not increase significantly when the k-point density is increassed.  This search for the appropriate density of k-points is called k-point convergence.

Currently our k-point convergence algorithm systematically increments the starting k-point density by 1 in each lattice vector direction until the total energy of the system does not increase by more than 0.001 eV.  This feature is accessible as an stand-alone workflow or as an add-on initial step before the final total energy or property calculation desired (similar to relaxation).

<img data-gifffer="/images/AddKpointConvergence.gif" />
Please see the [k-point convergence tutorial](../tutorials/kpt-convergence.md) for more details.

!!! note "Convergence + Relaxation"
    If both k-point convergence and relaxation preparation steps are added to your simulation flow the k-point convergence flow will be executed prior to the relaxation flow.

!!! warning "Beware of k-point convergence on 100's of atom systems"
    Due to system size the search for k-point convergence can be a computationally intensive calculation by itself.  When working with systems with hundreds of atoms it may be necessary to do k-point convergence on one system of simular character and constituents and use that density as a proxy for the converged k-point density of all the other related systems.

In particular some properties are highly dependent upon the quality of convergence and relaxation done prior to property calculation.  This is especially true of properties that depend on the force on the atoms, derivatives of the total energy, and any displacements or perturbation related properties.  For example accurate calculation of zero point energy requires a very well converged k-mesh to properly sample the total energy space when atoms are displaced from their equilibrium lattice positions.

Other input parameters may also be important depending upon the desired property.  For example when calculating dielectiric property it is important to ensure there is a surplus of unoccupied bands in the structure to ensure accuracy.

# Upcoming convergence workflows
1. Pseudopotential Energy Cutoff
2. Pseudopotential Radius Cutoff
3. Number of bands
