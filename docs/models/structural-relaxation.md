<!-- TODO by MH - Explain what relaxation is, how it is implemented by us and how to add relaxation as a workflow.

Link to coreresponding step-by-step tutorial inside 'tutorials' folder.
-->

It is often desired to obtain relaxed structures before running property calculations.

In addition to [k-point convergence](convergence-algorithms.md) it is also important to ensure that your system is in the lowest total energy state configuration possible before computing your property.  This usually involves some sort of relaxation before running your property calculation.  A relaxation is a systematic sampling of the free energy space to attempt to determine the position of atoms in their lowest energy state.

In some cases like interfaces it may be necessary to constrain the relaxation to not allow growth of the cell in a direction perpendicular to the interface but it is generally advisable to allow your atomic positions to at least relax in most cases.

