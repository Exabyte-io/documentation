# Crystal Atoms

The individual atoms in a Crystal Structure are arranged periodically in three-dimensions according to a **repeating unit**, or [basis](final-structure.md), set of atoms. They give the solid structure a finite strength against deformation through the **chemical bonds** linking them together, whose nature can be ionic, covalent, metallic etc. 

A typical example of an atomic arrangement within a material is given by the cubic-diamond crystal structure displayed below. This represents the underlying structural framework of crystalline materials such as Carbon (in the diamond phase), Silicon and Germanium.

![Crystal Atoms](/images/crystal_atoms.png "Crystal Atoms")

## Vector Properties

Crystalline atoms are characterized primarily by two important vector quantities: **atomic positions** and **atomic forces**. The former is related to their geometric arrangement within the structure, whereas the latter defines the strength of their bonding interactions away from the most stable (lowest potential energy) equilibrium configuration. 

### Atomic Positions

The atomic positions can be defined and entered in the [basis editor](../../materials-designer/source-editor/basis.md) of [Materials Designer](../../materials-designer/overview.md), as separate three-dimensional vectors. Each vector labels the position of the corresponding atom within the unit cell of the crystal, expressed under either a fractional or Cartesian coordinate system. 

### Atomic Forces

Atomic forces can be computed as part of any [Workflow](../../workflows/overview.md) executing a total energy self-consistent field calculation. They are also expressed as a set of vectors, one for each atom in the material, describing the combination of all inter-atomic forces acting upon it originating from all other atoms. Under the [Results Tab](../../jobs/ui/results-tab.md) within [Jobs Viewer](../../jobs/ui/viewer.md), the atomic forces are returned to the user as displayed in the example image below (exhibiting an ideal equilibrium situation with zero force components), expressed in units of eV/Angstroms.

![Atomic forces](/images/atomic_forces.png "Atomic forces")
