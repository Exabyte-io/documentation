<!-- by MH -->

In addition to [k-point convergence](convergence-algorithms.md) it is also important to ensure that your system is in the equilibrium configuration before computing characteristic properties. This usually involves structural relaxation.

# Overview

A "relaxation" is a systematic sampling of the free energy space to attempt to determine the position of atoms in their lowest energy state. The "relaxed" state criteria is usually determined by monitoring the force or stress on the atoms and/or system until it crosses below some critical threshold value.

The following shows the steps to add relaxation to a property calculation such as band structure.

<img data-gifffer="/images/RelaxBandstructure.gif" />

!!! Note "Relaxation Tutorial"
    Please visit the [relaxation tutorial](tutorial/relaxation.md) for a more expansive and detailed look at adding a relaxation.

# Relaxation types

Relaxations are usually classified by the number of degrees of freedom allowed to relax during the calculation which may include:

1. Atoms - position of the atoms
2. Cell shape - angles between lattice vectors
3. Cell size - length of lattice vectors and/or parameters

!!! note "Default relaxation settings"
    When clicking the "Workflow Options" section on "Relaxation" the default settings relax the atoms, cell shape, and cell size of the structure. Experienced users can open up the input files to change the exact behavior of this relaxation

!!! warning "About relaxation degrees of freedom priority"
    Please note that in general the priority listed above is preferable.  For large structures where a full relaxation of cell size is not computationally feasible, then priority should be given to relaxing the atomic positions.  In some cases you can significantly reduce the computation time for relaxations by only relaxing a certain number of atoms within the structure when appropriate.  For example, if trying to simulate a 256 atom silicon supercell with 1 Si atom replaced by a P atom, fixing the positions of all atoms other than the 2nd nearest neighbor of the P atom will improve the speed of the calculation significantly.

# Constrained relaxation

In many cases simulation software allows one to specify constraints in certain directions in the material or on specific atoms of the material.  These are more advanced features of the simulation engine and must be used with caution but are critical in some cases.  For example, for interface calculations, constraining the lattice parameter perpendicular to the interface plane may be critical otherwise the stress involved in building the interface would result in the supercell structure expanding to the point at which the distance between interface atoms suggest there is no bonding across the interface.

Please see the [relaxation tutorial](../tutorials/relaxation.md) for more details.

In some cases, for example when dealing with interfaces, it may be necessary to constrain the relaxation to not allow growth of the cell in a direction perpendicular to the interface but it is generally advisable to allow your atomic positions to at least relax in most cases.
