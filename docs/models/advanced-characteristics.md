<!-- TODO by MH -->

The calculation of some characteristic properties requires multiple calculations, inputs, and analysis.  At Exabyte.io our focus is to automate these multi-step methodologies to free up the user's time to do real science.  Currently we have 2 such flows for formation energy and band gap described below.  In addition we provide automation to add both k-point convergence and relaxation as initial steps in any subsequent property calculation you chose to do.

<hr>


# Formation Energy

We have calculated a series of simulations on all pseudopotentials that we currently supported for an automated formation energy calculation.  We have pre-calculated the converged k-point density, total energy, and zero point energy of all elemental pseduopotentials and saved these values.  When choosing the formation energy workflows for either application, the correct elemental total and zero point energies are used to calculate the formation energy of the material in question.  Please note that the reference state for the elements is at 0 K and 0 pressure.  The formation energy of a material as well as the reference state total and zero point energy for each element in the material are displayed in the "Results" tab within their own text box.

!!! warning "Formation energy automation"
    Currently we only support automated calculation of formation energy for the pseudopotentials that we currently provide (PAW for VASP and gbrv for quantum espresso).  If you chose to import your own pseudopotential for your calculation, you will need to manually calculate your reference total and zero point energies at converged k-point densities.  In the future we will automate this entire flow for user-imported pseudopotentials as well.  The full automation of formation energy also only currently works for 2-element compounds.  This will be upgraded to enable automation on a arbitrary number of elements in a compound in the future.

<hr>

# Band Gap

The band gap is defined as the energy difference between the highest occupied energy state of a material and the lowest unoccupied energy state of the material.  However, a band gap can either be a direct or indirect band gap.  Direct band gap means the minimum change in energy between occupied and unoccupied states at the same k-point.  The indirect band gap means the minimum change in energy between occupied and unoccupied states at different k-points.  The indirect band gap could potentially be smaller than the direct band gap.  We have automated the search for both types of band gaps, but require a band structure calculation first to determine these values.

<hr>

# Convergence and Relaxation

One of the most important things to learn about atomic simulations is that is critical how you prepare your structures and inputs before actually running your final property calculation.

In particular some properties are highly dependent upon the quality of convergence and relaxation done prior to property calculation.  This is especially true of properties that depend on the force on the atoms, derivatives of the total energy, and any displacements or perturbation related properties.  For example accurate calculation of zero point energy requires a very well converged k-mesh.  Other input properties may also be important depending upon the desired property.  For example when calculating dielectiric property it is important to ensure there is a surplus of unoccupied bands in the structure to ensure accuracy.

## K-point convergence

In most cases to have a reasonable level of confidence that a result can be trusted the total energy should not increase significantly when the k-point density is increassed.  This search for the appropriate density of k-points is called k-point convergence.

See [here](convergence-algorithms.md) for more details.

## Relaxation

In addition to k-point convergence it is also important to ensure that your system is in the lowest total energy state configuration possible before computing your property.  This usually requires at least some relaxation before running your property calculation.  In some cases like interfaces it may be necessary to constrain the relaxation to not allow growth of the cell in a direction perpendicular to the interface but it is generally advisable to allow your atomic positions to at least relax in most cases.

See [here](structural-relaxation.md) for more details.
