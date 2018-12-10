# Basis and Atoms

<span class="btn badge b-success border-50">Non-Scalar</span> <span class="btn badge b-info border-50">Structural</span>

## Crystal Basis

The individual atoms in a [crystal structure](../../materials/classification/crystalline.md) are arranged periodically in three-dimensions according to a **repeating unit**, or **basis** - a set of atoms corresponding to certain chemical **elements** and positions.  

## Example Atomic Structure

A typical example of an atomic arrangement within a material is given by the cubic-diamond crystal structure displayed below. This represents the underlying structural framework of crystalline materials such as Carbon (in the diamond phase), Silicon and Germanium. Atoms are shown here as dark balls, connected by white tubes representing the covalent bonds between them.

![Crystal Atoms](/images/properties-directory/Properties/crystal_atoms.png "Crystal Atoms")

## Atomic Positions

The atomic positions, defining the atom's geometric arrangement within the structure, can be defined and entered in the [basis editor](../../materials-designer/source-editor/basis.md) of [Materials Designer](../../materials-designer/overview.md), as separate three-dimensional vectors. Each vector labels the position of the corresponding atom within the unit cell of the crystal, expressed under either a fractional or Cartesian coordinate system. 

Depending on these atomic coordinates, finite [inter-atomic forces](atomic-forces.md) might arise.

## Elemental Ratio 

The ratio of an element in a compound or alloy describes the fraction of all atoms present in the crystal structure which are constituted by that particular element.

## Schema 

The JSON schema and an example representation for the properties described in this page can be found for each of the [basis](../../properties/data/list.md#basis), [atomic elements](../../properties/data/list.md#atomic-elements), [atomic positions](../../properties/data/list.md#atomic-coordinates) and [elemental ratio](../../properties/data/list.md#elemental-ratio).

## Links

[^1]: [Wikipedia Bonding in solids, Website](https://en.wikipedia.org/wiki/Bonding_in_solids)
