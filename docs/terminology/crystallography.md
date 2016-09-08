# Unit cell
In the solid state, most materials have their atoms arranged in a some kind of regular, repeating pattern called crystal structure. The crystal structure of a material (the arrangement of atoms within a given type of crystal) can be described in terms of its unit cell. The unit cell is a small box containing one or more atoms arranged in 3-dimensions. The unit cells stacked in three-dimensional space describe the bulk arrangement of atoms of the crystal. The unit cell is represented in terms of its lattice parameters (as referred to "lattice" in Descriptive), which are the lengths of the cell edges (a,b and c) and the angles between them (alpha, beta and gamma), while the positions of the atoms inside the unit cell are described by the set of atomic positions (xi  , yi  , zi) measured from a lattice point (as referred to "basis" in Descriptive). Commonly, atomic positions are represented in terms of fractional coordinates, relative to the unit cell lengths.
A unit cell of a simple cubic crystal is shown below:

When this unit cell is repeated in 3 dimensions, a crystal lattice is formed (unit cell -> crystal lattice)

# Periodic boundary conditions

On the figure above the content of unit cell is repeated infinite amount of times in three dimensions. At every border between the cells, all conditions within the 2 cells have to match exactly, as it is illustrated below:

In this formalism, if one wants to study a system with less symmetry (eg. not a perfect crystal, but a defect, surface, slab or molecule), it would be necessary to add enough vacuum to unit cell
# Bloch's theorem

If the nuclei are arranged in a periodically repeating pattern (crystal), their potential acting on the electrons must also be periodic:

Where L is any lattice vector.
Bloch’s theorem: in a periodic potential, the density has the same periodicity. The possible wavefunctions are all ‘quasi-periodic’:

where u k (r + L) = u k (r), and e ikr is an arbitrary phase factor:

The above statement also shows that any vector k that is larger than 2π/L will produce the same phase factor (because e 2π  = 1). This fact effectively defines an analog for unit cell in reciprocal space called Brillouin zone. By studying vectors that belong to it, one would get the information about the entire crystal of infinite size.

# K-point sampling
In principle we need to integrate over all possible k when constructing the density. Fortunately the wavefunctions change slowly as we vary k, so we can approximate the integral with a summation:

here g k is a spectral weight of a point k in the reciprocal space formed by all such vectors.
