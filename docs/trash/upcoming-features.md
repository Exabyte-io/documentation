<!-- by MH, DEPRECATED -->

We are focused on quickly expanding the number and range of properties we can predict.  We encourage your feedback on potential development efforts, if you don't see something on your wish list, feel free to email info@exabyte.io to request it, or comment on our [trello board](https://trello.com/b/89eLrRW0/exabyte-io-feature-roadmap).

<hr>
# Principal Properties

## Bond length

## Electrons per atom/bond

<hr>

## Electronic Properties

### Fermi surface
Surface of constant energy (Fermi Energy) in reciprocal space that separates the unfilled electronic levels from the filled ones.  NOTE: usually expressed in one of the formats for 3d surface plotting

### Crystal dependent band structure paths
Each of the unique crystal structures possible has a unique set of high symmetry points within its reciprocal space.  Exabyte will automate the determination of any material's crystal type and choose a band structure k-point path appropriate to sample all of that crystal structure's k-space through sampling of these high symmetry points.

### Work function/affinity
Energy required to take an electron from the bulk of a surface slab to the vacuum energy (essentially how much energy it takes to remove and electron from a surface)

### Band offset
Measures the difference in fermi energy, valence band edge, and conduction band edge between 2 materials.

### Effective Mass
The effective mass is a concept defined at a particular point on the band structure and related to the curvature of the energy band with respect to k.  This curvature is the second derivative of the energy band with respect to k and has the same units as mass and is therefore called an effective mass.  It determines the mobility of electrons at a particular point in k-space and is most commonoly of interest at the k-points involved in the smallest direct and indirect band gaps in insulators and semiconductors.  In conductors the effective mass is most important in a region right around the fermi energy. [[1](#links)]

### Linear scaling accurate GW Approximation Properties
Exabyte.io is working on a collaboration with an academic research team to bring a linear scaling GW approximation tool online with a high level of flexibility and automation to bring GW calculations into the mainstream.  GW Approximation calculations are excellent for predicting the energy of excited electronic states and until now the main impediment to their wide use is their poor parallel scaling and efficiency which limits their use due to the methods order of increase in computational cost versus traditional DFT techniques.

### Meta GGA and LDA+U support
Meta GGA and LDA+U are very different approaches both focused on modification of traditional DFT to correct predict excited state energies.  The U in LDA+U refers to the hubbard term in the pseudopotential.  Meta GGA is a modification of the GGA method by one or more parameters depending upon the implementation.  We will focus first of the common LDA+U and meta GGA methods implemented in VASP and quantum espresso.

### Complex band structure (slice)
A complex band structure slice is a projection in the complex or imaginary axis (i) at a particular k-point.  This information can be useful for calculation of items like an extinction length related to tunneling of electrons through a material.

### Dielectric Tensor and properties (permitivity and dielectric constant)
The dielectric tensor describes the response of a material to an electric field and it's ability to counteract it.  For example a metal is an example of a perfect dielectric material with a dielectric tensor with values of effectively infinity due to its free electrons which are able to immediately react to the presence of an electronic field.  Insulators and semiconductors have a non-infinity contributions to the dielectric tensor that measure how effectively it can screen an electronic field.  This property does not predict the actual voltage at which a material will no longer function as a capacitor. That is the breakdown voltage.  Relative permittivity is the factor by which the electric field between two point charges is decreased inside a material relative to vacuum.

### Effective band structure
Unfolding of zones of a large supercell projected onto its primitive cell equivalent

### Complex band structure (full 3D)
The 3D complex band structure is simply the imaginary projection of the band structure at all k-points.

### Schottky Barrier Height
Height of the potential barrier that results from bringing 2 different materials together to form an interface and those materials fermi energies trying to align when a semiconductor and a metal are brought into contact. [[2](#links)] [[3](#links)]

### Electrical Breakdown Voltage
The breakdown voltage is the applied voltage at which a material loses its ability to perform as an insulator and prevent the transport of electrons.  Intrinsically it is related to the band gap, but can be affected by a number of different aspects of the material including defects and structure.

### Resistivity
Property that quantifies how strongly a given material opposes the flow of electric current.  [[4](#links)]

### Contact Resistance
Measures the quantum mechanical interface resistance due to bringing 2 materials together and a mismatch of the electronic wave functions across that interface.

### Transmission spectrum & coefficients (k-point/energy resolved)
Spectral current

### Spin-torque transfer (STT) for collinear/non-collinear spin

### Current density and transmission pathways

<hr>

## Mechanical Properties

### All moduli and elastic properties
The elastic and compliance tensors measure the elastic response of a material to deformation in all unique directions in space.  From this property we can derive all elastic constants such as Young's Modulus, Bulk Modulus, Shear Modulus, and Poisson's Ratio.

### Elasticity (Bulk) Modulus
The bulk modulus (K or B) of a substance measures the substance's resistance to uniform compression. It is defined as the ratio of the infinitesimal pressure increase to the resulting relative decrease of the volume. More information including a conversion table from K to other elasticity parameters can be found on Wikipedia.

### Young's Modulus
Measures the elastic (reversible deformation response) to a tensile force or extension.

### Poisson's ratio
Negative ratio of transverse to axial strain.

### Shear Modulus
The ratio of shear stress to the shear strain

### Adhesion
Strength of the interface bonds formed between 2 materials. It can be related to experimental properties such as those derived by 4-pt bend measurements.  [[5](#links)]

### Stacking fault energy
Measure of the energy added to the surface by the presence of a discrete defect within the structure. The exact atomic configuration of the defect can be defined in many ways, but the stacking fault energy is related to the amount of energy added to the structure due to the defects presence

### Hardness
Measure of how resistant solid matter is to various kinds of permanent shape change when a compressive force is applied. Some materials, such as metal, are harder than others. Macroscopic hardness is generally characterized by strong intermolecular bonds, but the behavior of solid materials under force is complex; therefore, there are different measurements of hardness: scratch hardness, indentation hardness, and rebound hardness.

### Fracture toughness
Fracture toughness is related to the hardness but is also structure dependent upon the surface to be created to form a crack.  [[6](#links)]

<hr>

## Chemical Properties

### Cohesive energy
The cohesive energy is a measure of the amount of energy required to break a material into it's constituent parts.  It is related to the formation eenrgy

### Nudged Elastic Band Method
Nudged Elastic Band Methods are used when one knows the initial and final molecular configuration related to a particular reaction and is used to determine the transition state for that reaction.  This determines the barrier of that particular reaction and the kinetic rate at which it will occur.

### Reaction Energy
Difference in energy of reactants and products  eV  Multiple DFT calculations of reactants and products and total energy [[7](#links)]

### Surface energy
Energy added to the structure due to the presence of the surface as opposed to a perfect fully periodic structure [[8](#links)]

### Wetting
Closely related to adhesion, but usually referred to as part of the initial deposition process of one material on top of another to form the interface. The wetting ability of the second material refers to whether a material is more likely to bind to the second material (spread out on the surface) vs. binding to the depositing material (form islands)

### Heat of Formation

### Bond disassociation energy
[[9](#links)]

### Reaction Barrier
Energy of the lowest energy intermediate structure between reactants and products.  NEB/GSM calculation of many DFT images and total energy [[10](#links)]

### Growing String Method
The growing string method has some advantages versus Nudged Elastic Band in its ability to search the free energy space.

### Reaction Rate
Measure of the speed at which a reaction will proceed [[11](#links)]

### Diffusion Coefficients
Energy above hull   The energy of decomposition of this material into the set of most stable materials at this chemical composition, in eV/atom. Stability is tested against all potential chemical combinations that result in the material's composition. For example, a Co2O3 structure would be tested for decomposition against other Co2O3 structures, against Co and O2 mixtures, and against CoO and O2 mixtures. [[12](#links)]

<hr>

## Vibrational Properties

### Phonon Spectrum
Similar to the electronic band structure. Phonon dispersions (spectra) describes the frequencies and shapes of possible atomic oscillations inside a material.  NOTE: this is a complex property containing energy values for a number of phonon modes on a path in a three-dimensional reciprocal space. [[13](#links)]

### Phonon Band Structure
A phonon band structure measures the character (direction of travel and propagation of energy) of phonons (coherent lattic vibrations) as a function of q space.

### Phonon Density of States
The phonon density of states is a summation of all possible phonons per unit of energy.  Similar to the electronic DOS - calculated from phonon spectra.  [[13](#links)]

### Electron-phonon coupling
Unit-less parameter that characterizes the strength of interaction between the electronic and atomic subsystems in a crystal.  [[14](#links)]

### Eliashberg spectral function
Classifies the distribution of electron-phonon coupling coefficients by energy [[15](#links)]

<hr>

## Magnetic Properties

### Magnetic susceptibility
A dimensionless proportionality constant that indicates the degree of magnetization of a material in response to an applied magnetic field.

### Magnetic moment
Magnetic moment of an atom (ie. determined at this atomic site). The magnetic moment of a magnet is a quantity that determines the torque it will experience in an external magnetic field. [[16](#links)]

<hr>

## Superconducting Properties

### Transition temperature
Temperature at which a material becomes a superconductor.

### Critical Magnetic Field
The value of magnetic field at which superconductivity disappears (could be type I and type II)

<hr>

## Thermal Properties

### Coefficient of Thermal Expansion

### Heat capacity
Ratio of the heat added to (or removed from) an object to the resulting temperature change. [[17](#links)]

### Thermal Conductivity
The property of a material to conduct heat. Heat transfer occurs at a lower rate across materials of low thermal conductivity than across materials of high thermal conductivity. Correspondingly, materials of high thermal conductivity are widely used in heat sink applications and materials of low thermal conductivity are used as thermal insulation. [[18](#links)]

### Thermopower (or Seebeck coefficient)
Magnitude of an induced thermoelectric voltage in response to a temperature difference across that material, as induced by the Seebeck effect.  [[19](#links)]

### Hall coefficient

### Electronic specific heat

<hr>

## Optical Properties

### Absorption spectra
Measured through the imaginary part of Dielectric Permittivity Symmetry analysis of vibrational modes at the center of the Brillouin zone with classification in IR active, Raman active and silent modes

<hr>


# Capabilities

Exabyte.io is focused on building a capable structure generator and manipulator to enable you to create a wide variety of structures interactivey and online.  Toward that vision we currently are working on the following capabilties review in brief below.  If you are particularly interested in one of the below capabilities or think a different capability is more important than those listed below, please don't hesitate to send us your suggestions at info@exabyte.io

## Surface generation

The real world is a complex interaction of materials with other gases, liquids, and solids.  When you take a crystal structure and terminate it in a particular direction at a defined thickness, you have created a surface.  At Exabyte.io we are focused on developing an surface generator capability that gives flexibility to choose any surface orientation, the atom terminating the surface for multi-element structures, and a passivation option as well.

## Passivation

Except in rare cases such the real world is not made up of perfect materials extended out to macroscopic dimensions.  This means that the perfect structures must terminate at some point or contain defects in their atomic structure.  If we leave these defects to simply be the absence of atoms, that is unphysical because it implies that eletrons in the structure are free to bond with anything and that is unstable.  At Exabyte.io we are focused on developing a capabilty to passivate with a wide variety of atoms in both a directed and automated manner to satisfy certain chemistry rules.

## Interface generation

The real world is a complex interaction of many different materials across atomic boundaries between these materials.  These interfaces are a difficult challenge for atomic simulations as a balance between the size of the atomic system and generality of the system must be maintained to enable reasonable computational times.  At Exabyte.io we are focused on developing an interface capability that uses the surface generation modulue outputs as input and allows one to search the linear algebra space of combining 2 different crystal cells together into 1 structure, enabling a study of the interfacial spacing and line-up of interfce atoms across that interface, and possible alterations of the interface structure to try to reduce the charge near the interface.

## Interstitials

Many crystal structure have natural voids in their structures called interstitices.  These intersticies are common locations of the diffusion and holding impurities in the structure.  Based on the symmetry, local bonding environment, and a free space finder it is possible to identify what locations are most likely to hold another atom of particular size or number of electrons

## Polymers

Creation of polymer structures is a rich and diverse area that requires a multitude of functionality.


# Upcoming convergence workflows

1. Pseudopotential Energy Cutoff
2. Pseudopotential Radius Cutoff
3. Number of bands


# Upcoming simulation engines.

1. BerkelyGW
1. NWChem
1. LAMMPS
1. OMEN/NEMO


# Links

1. [Wikipedia Effective Mass, Website](https://en.wikipedia.org/wiki/Effective_mass_(solid-state_physics))
2. [First-Principles Calculations of Schottky Barrier Heights
of Monolayer Metal/6H-SiC{0001} Interfaces, PDF](https://www.jim.or.jp/journal/e/pdf3/47/11/2690.pdf)
3. [Theoretical study of Schottky-barrier formation at epitaxial rare-earth-metal/semiconductor interfaces, PDF](http://journals.aps.org/prb/abstract/10.1103/PhysRevB.81.165312)
4. [First-principles studies on electrical resistivity of iron under pressure , PDF](http://arxiv.org/pdf/1007.3423.pdf)
5. [Wikipedia Adhesion, Website](https://en.wikipedia.org/wiki/Adhesion)
6. [Wikipedia Fracture Toughness, Website](https://en.wikipedia.org/wiki/Fracture_toughness)
7. [BerkeleyGW: A Massively Parallel Computer Package
for the Calculation of the Quasiparticle and Optical
Properties of Materials and Nanostructures, PDF](http://arxiv.org/pdf/1111.4429v3.pdf)
8. [Wikipedia Surface Energy, Website](https://en.wikipedia.org/wiki/Surface_energy)
9. [A DFT study of bond dissociation energies of several alkyl nitrate and nitrite compounds, PDF](http://www.sciencedirect.com/science/article/pii/S0166128007008159)
10. [A growing string method for determining transition states.
Comparison to the nudged elastic band and string methods, PDF](http://www.cchem.berkeley.edu/akcgrp/arups%20papers/96.pdf)
11. [Theoretical Calculations in
Reaction Mechanism Studies, PDF](http://www.sumitomo-chem.co.jp/english/rd/report/theses/docs/2013E_5.pdf)
12. [Prediction and Calculation of Crystal Structures: Methods and Applications, Book](https://books.google.com/books?id=9nu5BQAAQBAJ)
13. [Spin-resolved electron-phonon coupling in FeSe and KFe2Se2, PDF](http://journals.aps.org/prb/abstract/10.1103/PhysRevB.86.134517)
14. [Electron-Phonon Coupling and its implication for the superconducting topological insulators, PDF](http://www.nature.com/articles/srep08964)
15. [Superconductivity and electron-phonon coupling in lithium at high pressures, PDF](http://journals.aps.org/prb/abstract/10.1103/PhysRevB.82.184509)
16. [Effects of charge doping and constrained magnetization on the electronic structure of
an FeSe monolayer, PDF](http://arxiv.org/pdf/1208.2260v2.pdf)
17. [First-Principles Calculations of the Specific Heats of Cubic Carbides and Nitrides, PDF](https://www.jim.or.jp/journal/e/pdf3/51/03/574.pdf)
18. [Role of Disorder and Anharmonicity in the Thermal Conductivity of Silicon-Germanium Alloys: A First-Principles Study, PDF](http://dspace.mit.edu/handle/1721.1/63802)
19. [First Principles explanation of the positive Seebeck coefficient of lithium, PDF](http://arxiv.org/pdf/1311.6805v1.pdf http://arxiv.org/pdf/1305.1587.pdf)
