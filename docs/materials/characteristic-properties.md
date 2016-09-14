<!-- by MH -->

!!! note "Classification"
    We subdivide all properties into [**Core**](../terminology/property-classification#core-properties), [**Principal**](../terminology/property-classification#principal-properties), and [**Derived**](../terminology/property-classification#derived-properties) (see the [terminology section](../terminology/property-classification.md) for more explanation)

# Core Properties

## Electronic wave functions

Spatial functions represent the probability distribution for electronic states.  These are expressed in reciprocal space due to the periodic nature of crystals

## Electronic energies

Energy of the given electronic state (eigenvalues of the electronic Hamiltonian represented in a chosen basis)

!!! note "Density Function Theory"
    For density functional theory, electronic energies are energies of Kohn-Sham states

# Principal Properties
There are some parameters that are directly extracted from Density Functional Theory simulations (as implemented in Quantum ESPRESSO and similar software packages).


| Principal Property | Explanation |
|:---------------|:------------|
| Total Energy   | The ground state energy of the system (NOTE: not equal to the sum of electronic energies)|
|Entropy|Measures the disorder of the structure|
|Energy contributions|Hartree, Exchange-correlation (XC), one-electron, Ewald, smearing (Density Functional Theory energy contributions overview [[1](#links)])|
|Fermi energy|The highest energy level occupied by electrons in a system.|
|Atomic forces|Force exerted on each atom by its surroundings|
|Stress tensor|3x3 matrix expressing stresses in x, y and z dimensions|
|Average pressure|Scalar average pressure|
|Charge density|Spatial function that contains information about charge distribution|

# Derived Properties
We further subdivide all derived properties into:

- [**Electronic Properties**](#electronic-properties)
- [**Chemistry Properties**](#chemistry-properties)
- [**Vibrational Properties**](#vibrational-properties)

<hr>

## Electronic Properties

### Band Structure
Property that describes the ranges of energy that an electron within the solid may have (called energy bands,allowed bands, or simply bands) and ranges of energy that it may not have (called band gaps or forbidden bands).  The band structure refers to a mapping of the energy individual electronic bands within a material in reciprocal space.  Please note that a well-known deficiency of Density Functional Theory in the Local Density Approximation is the energy of the excited or unoccupied states are lower than in reality.  This can be addressed through more advanced methods like the GW Approximation and modifications to DFT such as LDA+U and metaGGA.

### Band Gap
The minimum energy difference between the highest occupied (valence) band and the lowest unoccupied (conduction) band. Extracted from the bandstructure. Can be direct - when the difference is between the energy points at the same point in reciprocal space, and indirect - when the difference between two inequivalent points.  Insulators and semiconductors have a gap in energy between their highest occupied electronic state and their lowest unoccupied electronic state.  At Exabyte we automatically search the band structure and determine both the smallest direct and indirect band gap.  An indirect band gap refers to the global minimum distance between the highest occupied band and the lowest unoccupied band.  A direct band gap refers to the energy gap at the same point in reciprocal space.

### Density of States and Partial DOS
Density of states is a summation over the all possible points in reciprocal space and measures the unit density of the number of electronic states per unit energy.  Describes the number of electronic states per interval of energy at each energy level that are available to be occupied (more on Wikipedia).
!!! note
    There are also projections of total electronic density onto each of the atomic states that are often useful

### Fermi surface
Surface of constant energy (Fermi Energy) in reciprocal space that separates the unfilled electronic levels from the filled ones.
!!!note
    Usually expressed in one of the formats for 3d surface plotting

<hr>

## Chemistry Properties

### Formation energy at 0K
Formation energy measures the stability of a material.  For example the formation energy of CO2 is the energy that results from forming CO2 from C and O2.  The formation energy of elements in their standard state is 0 eV.  At exabyte we have pre-calculated the total energy and zero point energy of all built-it pseudopotentials and provided a template workflow for calculatio of these properties for user-defined pseudopotentials.  Computed formation energy at 0K, 0atm using a reference state of zero for the pure elements. This quantity is often a good approximation for formation enthalpy at ambient conditions.

<hr>

## Vibrational Properties

### Zero Point Energy
The zero pointe energy is a purely quantum mechanical property that is the amount of energy presence in a material due to quantum mechanical uncertainty of the supposition of electronic states at 0K.  It is generally most important for lighter elements and is critical to making accurate predictions of the energetic stability and changes in chemistry.

<hr>

### Links

1. [Density Functional Theory energy contributions overview, PDF](http://elk.sourceforge.net/CECAM/Burke-DFT.pdf)
