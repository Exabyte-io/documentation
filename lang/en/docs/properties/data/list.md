# Schemas for Material Properties

We present throughout this page a list of JSON schemas and example representations concerning [properties](../../properties-directory/overview.md). The reader is referred to their respective documentation pages, accessible by clicking the headers below, for a review of their underlying physical significance.

## Scalar Properties

### [Total Energy](../../properties-directory/scalar/total-energy.md)

Total energy contains the total energy of the unit cell.

```json tab="Schema" 
{!schema/properties_directory/scalar/total_energy.json!}
```

```json tab="Example" 
{!example/properties_directory/scalar/total_energy.json!}
```

### [Zero Point Energy](../../properties-directory/scalar/zero-point-energy.md)

Some residual thermal vibrational energy is left at zero temperature due to quantum effects, and is referred to as Zero Point Energy.

```json tab="Schema" 
{!schema/properties_directory/scalar/zero_point_energy.json!}
```

```json tab="Example" 
{!example/properties_directory/scalar/zero_point_energy.json!}
```

### [Fermi Energy](../../properties-directory/scalar/fermi-energy.md)

The Fermi energy marks the highest occupied energy level in a solid.

```json tab="Schema"  
{!schema/properties_directory/scalar/fermi_energy.json!}
```

```json tab="Example"
{!example/properties_directory/scalar/fermi_energy.json!}
```

### [Total Energy Contributions](../../properties-directory/scalar/total-energy.md#total-energy-contributions)

Total energy contributions contains information about the components in the total energy of the unit cell. The contributions available will depend on the type of method and software used.

```json tab="Schema"
{!schema/properties_directory/non-scalar/total_energy_contributions.json!}
```

```json tab="Example"
{!example/properties_directory/non-scalar/total_energy_contributions.json!}
```

### [Formation Energy](../../properties-directory/scalar/formation-energy.md)

The Formation energy represents the energy required to create a defect in an otherwise perfect solid structure.

```json tab="Schema"  
{!schema/properties_directory/scalar/formation_energy.json!}
```

```json tab="Example"
{!example/properties_directory/scalar/formation_energy.json!}
```

### [Surface Energy](../../properties-directory/scalar/surface-energy.md)

The energy of a surface can also be computed.

```json tab="Schema"  
{!schema/properties_directory/scalar/surface_energy.json!}
```

```json tab="Example"
{!example/properties_directory/scalar/surface_energy.json!}
```

### [Pressure](../../properties-directory/scalar/pressure.md)

Pressure contains the average internal pressure of the unit cell.

```json tab="Schema"
{!schema/properties_directory/scalar/pressure.json!}
```

```json tab="Example"
{!example/properties_directory/scalar/pressure.json!}
```

### [Total Force](../../properties-directory/scalar/total-force.md)

This is the total average force present within the crystal structure.

```json tab="Schema"
{!schema/properties_directory/scalar/total_force.json!}
```

```json tab="Example"
{!example/properties_directory/scalar/total_force.json!}
```

## Non-Scalar Properties

### [Bandstructure](../../properties-directory/non-scalar/bandstructure.md)

Band structure shows the energy of electronic states (bands) as a function of k-point position throughout the cell.


```json tab="Schema"
{!schema/properties_directory/non-scalar/band_structure.json!}
```

```json tab="Example"
{!example/properties_directory/non-scalar/band_structure.json!}
```

### [Band Gaps](../../properties-directory/non-scalar/band-gaps.md)

Band gap is the difference in energy from the highest occupied electronic state (Fermi energy at 0K) to the lowest unoccupied state.

```json tab="Schema"
{!schema/properties_directory/non-scalar/band_gaps.json!}
```

```json tab="Example"
{!example/properties_directory/non-scalar/band_gaps.json!}
```

### [Electronic Density of States](../../properties-directory/non-scalar/electronic-dos.md)

Density of states contains information on the number of electronic states as a function of energy. It may include the atom resolved partial density of states and electron states in some cases. In addition it may also contain information about each atom’s spin state as well.

```json tab="Schema"
{!schema/properties_directory/non-scalar/density_of_states.json!}
```

```json tab="Example"
{!example/properties_directory/non-scalar/density_of_states.json!}
```

### [File Content](../../properties-directory/non-scalar/file-content.md)    

Tags a file for display on the results tab of the web-app.

```json tab="Schema"
{!schema/properties_directory/non-scalar/file_content.json!}
```

```json tab="Example"
{!example/properties_directory/non-scalar/file_content.json!}
```

### [Reaction Energy Profile](../../properties-directory/non-scalar/reaction-energy-profile.md)

The energy profile of a chemical reaction is a representation of its energetic pathway, followed by the reactants as they are transformed into products.

```json tab="Schema"
{!schema/properties_directory/non-scalar/reaction_energy_profile.json!}
```

```json tab="Example"
{!example/properties_directory/non-scalar/reaction_energy_profile.json!}
```

### [Reaction Energy Barrier](../../properties-directory/scalar/reaction-energy-barrier.md)

The Reaction Energy Barrier marks the highest energy state encountered during the course of the progress of a chemical reaction.

```json tab="Schema"
{!schema/properties_directory/scalar/reaction_energy_barrier.json!}
```

```json tab="Example"
{!example/properties_directory/scalar/reaction_energy_barrier.json!}
```

### [Phonon Dispersions](../../properties-directory/non-scalar/phonon-dispersions.md)

Lattice vibrations can be plotted in the form of phonon frequency dispersion plots across the reciprocal k-space of the crystal structure.

```json tab="Schema"
{!schema/properties_directory/non-scalar/phonon_dispersions.json!}
```

```json tab="Example"
{!example/properties_directory/non-scalar/phonon_dispersions.json!}
```

### [Phonon Density of States](../../properties-directory/non-scalar/phonon-dos.md)

The Density of States for phonons can also be computed.

```json tab="Schema"
{!schema/properties_directory/non-scalar/phonon_dos.json!}
```

```json tab="Example"
{!example/properties_directory/non-scalar/phonon_dos.json!}
```

### [Stress Tensor](../../properties-directory/non-scalar/stress-tensor.md)

Stress tensor contains a 3x3 matrix of the stress components of the unit cell.

```json tab="Schema" 
{!schema/properties_directory/non-scalar/stress_tensor.json!}
```

```json tab="Example"
{!example/properties_directory/non-scalar/stress_tensor.json!}
```

## Elemental Properties

### [Atomic Radius](../../properties-directory/elemental/atomic-radius.md)

The atomic radius represents the average distance between the nucleus of an atom and the edges of its surrounding electron cloud.

```json tab="Schema"
{!schema/properties_directory/elemental/atomic_radius.json!}
```

```json tab="Example"
{!example/properties_directory/elemental/atomic_radius.json!}
```

### [Electronegativity](../../properties-directory/elemental/electronegativity.md)

The electronegativity describes the capacity of an atom to attract the electrons involved in chemical bonding.

```json tab="Schema"
{!schema/properties_directory/elemental/electronegativity.json!}
```

```json tab="Example"
{!example/properties_directory/elemental/electronegativity.json!}
```

### [Ionization Potential](../../properties-directory/elemental/ionization-potential.md)

The ionization energy (or potential) measures the energy required to strip an atom from its most loosely bound valence electron.

```json tab="Schema"
{!schema/properties_directory/elemental/ionization_potential.json!}
```

```json tab="Example"
{!example/properties_directory/elemental/ionization_potential.json!}
```

## Structural Properties

### [Atomic Forces](../../properties-directory/structural/atomic-forces.md)

Forces may exist between atoms in a crystal structure if they are displaced away from their equilibrium configuration.

```json tab="Schema"
{!schema/properties_directory/structural/atomic_forces.json!}
```

```json tab="Example"
{!example/properties_directory/structural/atomic_forces.json!}
```

### [Atomic Coordinates](../../properties-directory/structural/basis.md)

Contains information about the coordinates of atoms within the unit cell by id.

```json tab="Schema"
{!schema/properties_directory/structural/basis/atomic_coordinates.json!}
```

```json tab="Example"
{!example/properties_directory/structural/basis/atomic_coordinates.json!}
```

### [Atomic Elements](../../properties-directory/structural/basis.md)

Contains an array of the elements in the unit cell and the atom id’s association with each atom.

```json tab="Schema"
{!schema/properties_directory/structural/basis/atomic_elements.json!}
```

```json tab="Example"
{!example/properties_directory/structural/basis/atomic_elements.json!}
```

### [Atomic Constraints](../../properties-directory/structural/basis.md)

Contains information about the spatial constraints on the movement of atoms.

```json tab="Schema"
{!schema/properties_directory/structural/basis/atomic_constraints.json!}
```

```json tab="Example"
{!example/properties_directory/structural/basis/atomic_constraints.json!}
```

### [Basis](../../properties-directory/structural/basis.md)

Basis defines elemental and geometrical constitution of the unit cell.


```json tab="Schema"
{!schema/properties_directory/structural/basis.json!}
```

```json tab="Example"
{!example/properties_directory/structural/basis.json!}
```

### [Bravais Lattice](../../properties-directory/structural/lattice.md)

Lattice Bravais holds information about the three-dimensional periodic structure specified implicitly through lengths and angles between lattice vectors, and their units.

```json tab="Schema"
{!schema/properties_directory/structural/lattice/lattice_bravais.json!}
```

```json tab="Example"
{!example/properties_directory/structural/lattice/lattice_bravais.json!}
```

### [Lattice Vectors](../../properties-directory/structural/lattice.md)

Lattice vectors holds information about the three-dimensional periodic structure explicitly, by specifying the three lattice vectors and their units.

```json tab="Schema"
{!schema/properties_directory/structural/lattice/lattice_vectors.json!}
```

```json tab="Example"
{!example/properties_directory/structural/lattice/lattice_vectors.json!}
```

### [Density](../../properties-directory/structural/lattice.md#volume-and-density)

The Density of the material is defined by the sum of the atomic masses within the unit cell, divided by its volume.

```json tab="Schema"
{!schema/properties_directory/structural/density.json!}
```

```json tab="Example"
{!example/properties_directory/structural/density.json!}
```

### [Elemental Ratio](../../properties-directory/structural/basis.md#elemental-ratio)

The elemental ratio is given by the fraction of all atoms in a crystal which are composed of a certain element.

```json tab="Schema"
{!schema/properties_directory/structural/elemental_ratio.json!}
```

```json tab="Example"
{!example/properties_directory/structural/elemental_ratio.json!}
```

### [Magnetic Moments](../../properties-directory/structural/magnetic-moment.md)

The magnetic moment of ferromagnetic materials can also be computed.

```json tab="Schema"
{!schema/properties_directory/structural/magnetic_moments.json!}
```

```json tab="Example"
{!example/properties_directory/structural/magnetic_moments.json!}
```

### [P Norm](../../properties-directory/structural/lattice.md)

The P norm measures how homogeneous a material is in terms of its chemical composition. 

```json tab="Schema"
{!schema/properties_directory/structural/p-norm.json!}
```

```json tab="Example"
{!example/properties_directory/structural/p-norm.json!}
```

### [Symmetry](../../properties-directory/structural/space-group.md)

The Space Group of the crystal structure, indicating the symmetry elements that it contains, is also available. 

```json tab="Schema"
{!schema/properties_directory/structural/symmetry.json!}
```

```json tab="Example"
{!example/properties_directory/structural/symmetry.json!}
```

### [Volume](../../properties-directory/structural/lattice.md)

The volume of the unit cell is given by the scalar triple product of the lattice vectors. 

```json tab="Schema"
{!schema/properties_directory/structural/volume.json!}
```

```json tab="Example"
{!example/properties_directory/structural/volume.json!}
```
