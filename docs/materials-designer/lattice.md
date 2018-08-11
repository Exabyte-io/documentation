# Crystal Lattice

The parameters of a Material's Bravais lattice [[1](#links)] can be edited and set by expanding the top "Crystal Lattice" section in the central panel of the Materials Designer. Expanding is achieved by clicking the downward-pointing arrow next to the section header. The reader who is unfamiliar with the fundamental notions of crystallography is referred to any of the introductory textbooks on solid-state physics [[2](#links)].
 
The appearance of the "Crystal Lattice" editor inside the Materials Designer interface is shown in the figure below:

<img src="/images/crystal-lattice.png"/>

# Setting the Lattice Parameters

One can set the lattice constants (a,b and c) and the angles between the lattice vectors by editing the corresponding numerical text fields. In order to choose lattice type click on the corresponding selector. You can select an alternate lattice type and the corresponding angles and lattice constants will automatically adjust. 

# Apply changes to the Lattice Parameters

When you are done selecting a new lattice and its corresponding parameters, click on the `Apply Edits` button.  The 3D visual representation of the structure on the right-hand side of the Materials Designer interface will change to reflect the new lattice type.

# Preserve Basis

The option to preserve the basis atoms in their absolute Angstrom coordinates, regardless of any change brought to the crystal structure in terms of the size of its unit cell, is also offered. This feature can be activated by turning on the "Preserve Basis" slider at the bottom of the "Crystal Lattice" panel.  

# Animation

Click on the animation below to see the above lattice editing features in action. Here we try to change lattice type from FCC to Tetragonal, and then we try modifying the size of one of the lattice axes (the a axis). The corresponding change in the unit cell size can be observed to occur in the crystal viewer on the right-hand side of the interface.

<img data-gifffer="/images/ChangeMaterialLattice.gif" />

# Links

1. [Wikipedia Bravais Lattice, Website](https://en.wikipedia.org/wiki/Bravais_lattice)

2. N.W. Ashcroft and N.D. Mermin: "Solid State Physics"; Cengage Learning (1976)
