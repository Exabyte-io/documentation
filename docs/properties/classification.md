# Materials Properties Classification

We draw some important distinctions when referring to materials properties as introduced in the [following page](/data-structured/overview.md), which also illustrates graphically the Material-Job-Property relation.

For the case of [Characteristic](/data-structured/overview.md) properties, we classify them based on whether they are returned and presented to the user as **scalars**, **arrays** (both of vector and matrix nature) or **dispersion curves**. We also group together all the **structural crystalline properties** of [Descriptive](/data-structured/overview.md) nature under a common category. 

Each aforementioned material property is reviewed and described separately in a dedicated section of the documentation, based on its position in the overall classification. The reader is referred to the links presented throughout the remainder of the present documentation page. 

# Example Representation

For examples of JSON representation of materials and structure-based descriptors, see the [Materials Data](/materials/data.md) section.

# Scalar Properties

The most significant scalar properties that can be computed on materials include their [Energy](scalar/energies.md) and [Pressure](scalar/pressure.md), including an estimate of the [total average internal force](scalar/pressure.md). They are reviewed in their respective documentation pages.

# Array Properties

Important array-like properties that can emerge from a Material computation are the [internal stress tensor](tensorial/stress-tensor.md) and the [inter-atomic forces](tensorial/atomic-forces.md). The former is computed in the form of a matrix, whereas the latter is presented as separate vectors. One vector exists for each atom present in the structure, describing the net force acting upon it due to the bonding interactions originating from all other atoms.

# Dispersion Curves

Examples of dispersion curves which are routinely encountered in materials science computations include those describing the [electronic bandstructure](dispersion/bandstructure.md) and [phonon lattice vibrations](dispersion/phonons.md) of the material. The [Density of States](dispersion/dos.md) pertaining to both of these dispersion properties can also be calculated and displayed graphically. 

# Structural Properties

Descriptive Structural Properties pertaining to the individual [atoms](structural/atomic.md), to the [Bravais Lattice](structural/lattice.md), and to the overall [Crystal Structure](structural/final-structure.md) of the material under consideration are reviewed and described in their respective documentation pages. 
