<!-- TODO by MH -->
One of the most important things to learn about atomic simulations is that is critical how you prepare your structures and inputs before actually running your final property calculation.

In most cases to have a reasonable level of confidence that a result can be trusted one must do a study to ensure that an increase in the k-point does not lead to a significant change in the total energy of the system.  This search for the appropriate density of k-points is called k-point convergence.

!!! warning "Beware of k-point convergence on 100's of atom systems"
    Due to system size the search for k-point convergence can be a computationally intensive calculation in and of itself.  When working with systems with hundreds of atoms it may be necessary to do k-point convergence on one system of simular character and constituents and use that density as a proxy for the converged k-point density of all systems.


In addition to k-point convergence it is also important to ensure that your system is in the lowest total energy state configuration possible before computing your property.  This usually involves some sort of relaxation before running your property calculation.  In some cases like interfaces it may be necessary to constrain the relaxation to not allow growth of the cell in a direction perpendicular to the interface but it is generally advisable to allow your atomic positions to at least relax in most cases.

In particular some properties are highly dependent upon the quality of convergence and relaxation done prior to property calculation.  This is especially true of properties that depend on the force on the atoms, derivatives of the total energy, and any displacements or perturbation related properties.  For example accurate calculation of zero point energy requires a very well converged k-mesh.  Other input properties may also be important depending upon the desired property.  For example when calculating dielectiric property it is important to ensure there is a surplus of unoccupied bands in the structure to ensure accuracy.