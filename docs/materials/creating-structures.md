# Ideal crystal

In order to create a new material one would need to navigate to "Materials" page using the left-hand sidebar, and then click on "Create New" button - <i class="zmdi zmdi-plus-circle-o"></i>. 

Materials Designer page opens with the default structure for FCC Si. It has an interactive 3D viewer on the lower right.

If you would like to start with something other than Silicon, please follow the directions on the [upload-and-import](upload-and-import.md) and set the newly upload material as "Default.

## Crystal Lattice

Lattice parameters can be edited by clicking on the corresponding button (containing "angstrom, FCC").  The overlay will allow you to set the parameters of the Bravais lattice [[1](#links)].

One can set lattice constants and angles between the lattice vectors. In order to choose lattice type click on the corresponding selector. You can select an alternate lattice type and the corresponding angles and lattice constants will automatically adjust. 

When you done selecting a new lattice click "Update Lattice" button.  The overlay will disappear and the 3D visual representation of the structure will change to reflect the new lattice type.

Click on the animation below to see the above in action:

<img data-gifffer="/images/ChangeMaterialLattice.gif" />


## Crystal Basis

The default representation of the atomic coordinates is in crystal (also commonly called fractional) coordinates [[2](#links)]. It is specified under the "Crystal Basis" section. You may edit the elements and corrdinates directly inside the corresponding textarea. Click on the "Cartesian" to convert coordinates to Angstroms.

Click on the animation below to see the above in action:

<img data-gifffer="/images/ChangeMaterialBasis.gif" />

# Supercells

You may create supercells or multiplicative representations of a smaller building block in space. For example, silicon with a 2 atom unit cell, being replicated by 2x2x2 leads to a supercell with 8 copies of primitive unit cell and 16 atoms total.

Start by clickin "Advanced Geometry Tools" button. The overlay will allow you to set parameters of the supercell matrix.  When finished, both the "Crystal Basis" and 3D representation of the structure will change accordingly.

Click on the animation below to see the above in action:

<img data-gifffer="/images/CreateMaterialSupercell.gif" />

Please note that you are multiplying the structure of what is currently represented in the "Crystal Basis" and 3D visualization window.  If Si is replicated by 2x2x2 that results in a 16 atom supercell.  If you then do another 2x2x2 replication, that will result in a 128-atom Si supercell.

# Links

1. [Wikipedia Bravais Lattice, Website](https://en.wikipedia.org/wiki/Bravais_lattice)
2. [Wikipedia Fractional Coordinates, Website](https://en.wikipedia.org/wiki/Fractional_coordinates)

