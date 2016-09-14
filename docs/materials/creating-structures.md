<!-- by MH -->

This tutorial shows how to create a structure prior to running a simulation.

# First step

The first step in any Exabyte.io calculation is creating an atomic structure that is a 3 dimensional representation of (1) the position of each atom and (2)the types of elements of each atom.  This structure serves as a primary input for the various methods and software that Exabyte.io provides.

Upon logging into your Exabyte.io account, the home page contains details of your recent computing usage, jobs, and charge on your account plus your current balance.

1. Basics of creating structures:
    - Ideal crystal - bravais lattices supported, basis options
    - Supercells - how to create
2. Upcoming Capabilities: surfaces, interfaces, slabs, interstitials
3. Future Capabilities (longer-term): polymers

### Ideal crystal

To create your first structure you need to [open sidebar](/getting-started/ui-overview/#project-navigation-left-sidebar).

<img data-gifffer="/images/CreateMaterial.gif" />

This brings up a new page with a default silicon atomic structure.  The 3 dimension model on the lower right is interactive and can be manipulated by clicking and dragging with your mouse to rotate the structure.  You can also zoom in and out if you have a trackball on your mouse.

If you would like to work with something other than Silicon, please follow the directions on the [upload-and-import](/upload-and-import.md) webpage and return to this webpage.

#### Lattice selection

If you move your mouse to the box containing `angstrom, FCC` the `>` inside that box will turn to `<`.  If you click anywhere inside that box an overlay will pop up on your screen.  The overlay will allow you to set the parameters of the crystal structure. (Crystal structure reference [[1](#links)])

It is possible to manually set all lattice constants and angles between the lattice vectors.  Alternately, to choose a default crystal cell other than Face-Centered Cubic, click on the `Face-centered Cubic` line below the `Lattice type` heading and a selection box with the 14 possible crystal cells will appear.  You can select an alternate crystal lattice by clicking on a different cell type and the displayed angles and lattice constants will automatically change.  When you select a new crystal lattice click the "Update Lattice" button.  The overlay will disappear and the 3D visual representation of the structure will change to reflect the new lattice type.
<img data-gifffer="/images/ChangeMaterialLattice.gif" />


#### Atomic basis/coordinates selection

The default representation of the atomic cooridates is in direct corrdinates (also commonly called fractional coordinates [[2](#links)]) and specified under the basis section.  If you would like to work with the actual cartesian coordinates simply click on the "Cartesian" to convert the coordinates.

<img data-gifffer="/images/ChangeMaterialBasis.gif" />

Alternating you can generate a custom lattice structure

### Supercells

A supercell most commonly refers to an atomic structure that is a multiplicative representation of a smaller building block structure.  A primitive unit cell is the smallest possible building block structure to represent the material.  Most elements in the periodic table contain 2 atoms or less in their primitive unit cell.  If however you want an impurity at less than 50% in a 2-atom primitive unit cell element, you would need to make a copy of the unit cell in one or more directions on each axis in the structure.  That structure created after the copies of the unit cell are made is a supercell.

For example, silicon which a 2 atom unit cell, being replication by 2x2x2 leads to a supercell with 8 copies of that primitive unit cell and 16 atoms total.  The `2x2x2` notation refers to the number of copies of that primitive unit cell in the `x`, `y`, and `z` directions respectively.

The ability to create a supercell can be accessed through the `Advanced Geometry Tools` box below the `Crystal Basis` section.  Once again moving your mouse into the box the  `>` inside that box will turn to `<`.  If you click anywhere inside that box an overlay will pop up on your screen.  The overlay will allow you to set the number of multiplicative copies of the unit cell displayed in all 3 directions of the crystal cell.  After clicking the `Create Supercell` button, both the `Crystal Basis` and 3D visual representation of the structure will change according to the replication entered.

<img data-gifffer="/images/CreateMaterialSupercell.gif" />

Please note that you are multiplying the structure of what is currently reprentated in the `Crystal Basis` and 3D visualization window.  If Si is replicated by 2x2x2 that results in a 16 atom supercell.  If you then do another 2x2x2 replication, that will result in a 128-atom Si supercell.

## Upcoming Capabilities
- Surface generation
- Passivation
- Interface generation
- Interstitials
- Polymers

More detailed description [here](/other/upcoming-capabilities.md).

### Links

1. [Wikipedia Bravais Lattice, Website](https://en.wikipedia.org/wiki/Bravais_lattice)
2. [Wikipedia Fractional Coordinates, Website](https://en.wikipedia.org/wiki/Fractional_coordinates)

