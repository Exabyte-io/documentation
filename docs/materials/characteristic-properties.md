Exabyte.io is focused on automation of your everyday tasks and analysis to free up your time to do real science rather than manage output files, scripts, and data sets.  Any property that can not be immediately derived through an output of the simulation software is termed a characteristic property.  This is opposed to derived properties like density, volume, pressure, etc. that are inherent properties of the material.

One potential way to break down characteristic properties is by their character such as electronic, mechnical, chemistry, & vibrational related properties.  Of course the choice of this classification is arbitrary and leads to some overlap but we think it serves as a good guide for the users and developers to associate similar properties and focus on a modular software development to enable reuse of tools and properties.

# Electronic Properties
## Current
### Band Structure
The band structure refers to a mapping of the energy individual electronic bands within a material in reciprocal space.  Please note that a well-known deficiency of Density Functional Theory in the Local Density Approximation is the energy of the excited or unoccupied states are lower than in reality.  This can be addressed through more advanced methods like the GW Approximation and modifications to DFT such as LDA+U and metaGGA
### Band Gap
Insulators and semiconductors have a gap in energy between their highest occupied electronic state and their lowest unoccupied electronic state.  At Exabyte we automatically search the band structure and determine both the smallest direct and indirect band gap.  An indirect band gap refers to the global minimum distance between the highest occupied band and the lowest unoccupied band.  A direct band gap refers to the energy gap at the same point in reciprocal space
### Density of States
Density of states is a summation over the all possible points in reciprocal space and measures the unit density of the number of electronic states per unit energy.
## Upcoming
### Crystal dependent band structure paths
Each of the unique crystal structures possible has a unique set of high symmetry points within its reciprocal space.  Exabyte will automate the determination of any material's crystal type and choose a band structure k-point path appropriate to sample all of that crystal structure's k-space through sampling of these high symmetry points.
### Complex band structure (slice)
A complex band structure slice is a projection in the complex or imaginary axis (i) at a particular k-point.  This information can be useful for calculation of items like an extinction length related to tunneling of electrons through a material.
### Dielectric Tensor
The dielectric tensor describes the response of a material to an electric field and it's ability to counteract it.  For example a metal is an example of a perfect dielectric material with a dielectric tensor with values of effectively infinity due to its free electrons which are able to immediately react to the presence of an electronic field.  Insulators and semiconductors have a non-infinity contributions to the dielectric tensor that measure how effectively it can screen an electronic field.  This property does not predict the actual voltage at which a material will no longer function as a capacitor. That is the breakdown voltage.
### Effective Mass
The effective mass is a concept defined at a particular point on the band structure and related to the curvature of the energy band with respect to k.  This curvature is the second derivative of the energy band with respect to k and has the same units as mass and is therefore called an effective mass.  It determines the mobility of electrons at a particular point in k-space and is most commonoly of interest at the k-points involved in the smallest direct and indirect band gaps in insulators and semiconductors.  In conductors the effective mass is most important in a region right around the fermi energy. 
### Linear scaling accurate GW Approximation Properties
Exabyte.io is working on a collaboration with an academic research team to bring a linear scaling GW approximation tool online with a high level of flexibility and automation to bring GW calculations into the mainstream.  GW Approximation calculations are excellent for predicting the energy of excited electronic states and until now the main impediment to their wide use is their poor parallel scaling and efficiency which limits their use due to the methods order of increase in computational cost versus traditional DFT techniques.
### Meta GGA and LDA+U support
Meta GGA and LDA+U are very different approaches both focused on modification of traditional DFT to correct predict excited state energies.  The U in LDA+U refers to the hubbard term in the pseudopotential.  Meta GGA is a modification of the GGA method by one or more parameters depending upon the implementation.  We will focus first of the common LDA+U and meta GGA methods implemented in VASP and quantum espresso.
## Future
If you don't see something on your wish list, feel free to email new@exabyte.io to request it.
### Complex band structure (full 3D)
The 3D complex band structure is simply the imaginary projection of the band structure at all k-points.
### Electrical Breakdown Voltage
The breakdown voltage is the applied voltage at which a material loses its ability to perform as an insulator and prevent the transport of electrons.  Intrinsically it is related to the band gap, but can be affected by a number of different aspects of the material including defects and structure.

# Mechanical Properties
## Current
None
## Upcoming
### All moduli and elastic properties
The elastic and compliance tensors measure the elastic response of a material to deformation in all unique directions in space.  From this property we can derive all elastic constants such as Young's Modulus, Bulk Modulus, Shear Modulus, and Poisson's Ratio.
## Future
If you don't see something on your wish list, feel free to email new@exabyte.io to request it.

# Chemistry
## Current
### Formation energy at 0K
Formation energy measures the stability of a material.  For example the formation energy of CO2 is the energy that results from forming CO2 from C and O2.  The formation energy of elements in their standard state is 0 eV.  At exabyte we have pre-calculated the total energy and zero point energy of all built-it pseudopotentials and provided a template workflow for calculatio of these properties for user-defined pseudopotentials.
## Upcoming
### Cohesive energy
The cohesive energy is a measure of the amount of energy required to break a material into it's constituent parts.  It is related to the formation eenrgy
### Nudged Elastic Band Method
Nudged Elastic Band Methods are used when one knows the initial and final molecular configuration related to a particular reaction and is used to determine the transition state for that reaction.  This determines the barrier of that particular reaction and the kinetic rate at which it will occur.
## Future
If you don't see something on your wish list, feel free to email new@exabyte.io to request it.
### Growing String Method
The growing string method has some advantages versus Nudged Elastic Band in its ability to search the free energy space.

# Vibrational
## Current
### Zero Point Energy
The zero pointe energy is a purely quantum mechanical property that is the amount of energy presence in a material due to quantum mechanical uncertainty of the supposition of electronic states at 0K.  It is generally most important for lighter elements and is critical to making accurate predictions of the energetic stability and changes in chemistry.
## Upcoming
### Phonon Band Structure and Density of States
A phonon band structure measures the character (direction of travel and propagation of energy) of phonons (coherent lattic vibrations) as a function of q space.  The phonon density of states is a summation of all possible phonons per unit of energy.
## Future
If you don't see something on your wish list, feel free to email new@exabyte.io to request it.
### FTIR and Raman Spectroscopy
A summartion of virbation modes within a material.