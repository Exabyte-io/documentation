# Introduction

A "relaxation" is a systematic sampling of the free energy space to attempt to determine the position of atoms in their lowest energy state. The "relaxed" state criteria is usually determined by monitoring the force or stress on the atoms and/or system until it crosses below some critical threshold value.

This feature is accessible as a stand-alone (sub)workflow or as an add-on / modifier to an existing subworkflow during job creation.

# Relaxation types

Relaxations are usually classified by the number of degrees of freedom allowed to relax during the calculation which may include:

1. Atoms - position of the atoms
2. Cell shape - angles between lattice vectors
3. Cell size - length of lattice vectors and/or parameters

Default settings include the relaxation of the atoms, cell shape, and cell size of the structure. Experienced users can open up the input files to edit the exact behavior

# Constrained relaxation
    
For large structures where a full relaxation of cell size is not computationally feasible, priority should be given to relaxing atomic positions. 
    
In many cases simulation software allows one to specify constraints in certain directions or specific atoms. In some cases one can significantly reduce the computation time for relaxations by only relaxing a certain number of atoms within the structure when appropriate. For example, when simulating a 256 atom Si silicon supercell with 1 Si atom replaced by a P atom, fixing positions of all atoms other than the 2nd nearest neighbors of P will improve the speed of the calculation significantly.

!!! Note "Tutorial"
    Please visit the [relaxation tutorial](../tutorials/relaxation.md) for a more expansive and detailed look at adding a relaxation.
