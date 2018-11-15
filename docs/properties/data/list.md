# Schemas for Material Properties

We present throughout this page a list of JSON schemas and example representations concerning material properties, of both scalar and non-scalar types. The reader is referred to their respective documentation pages, accessible by clicking the headers, for a review of their underlying physical significance.

## Non-Scalar Properties

### [Atomic Coordinates](../non-scalar/atomic.md)

Contains information about the coordinates of atoms within the unit cell by id.

```json tab="Schema"
{!schema/material/properties/primary/structural/basis/atomic_coordinates.json!}
```

```json tab="Example"
{!example/material/properties/primary/structural/basis/atomic_coordinates.json!}
```

### [Atomic Elements](../non-scalar/atomic.md)

Contains an array of the elements in the unit cell and the atom id’s association with each atom.

```json tab="Schema"
{!schema/material/properties/primary/structural/basis/atomic_elements.json!}
```

```json tab="Example"
{!example/material/properties/primary/structural/basis/atomic_elements.json!}
```

### [Basis](../non-scalar/atomic.md)

Basis defines elemental and geometrical constitution of the unit cell.


```json tab="Schema"
{!schema/material/properties/primary/structural/basis.json!}
```

```json tab="Example"
{!example/material/properties/primary/structural/basis.json!}
```

### [Atomic Forces](../non-scalar/atomic.md)

Forces may exist between atoms in a crystal structure if they are displaced away from their equilibrium configuration.

```json tab="Schema"
{!schema/material/properties/primary/structural/atomic_forces.json!}
```

```json tab="Example"
{!example/material/properties/primary/structural/atomic_forces.json!}
```

### [Bandstructure](../non-scalar/bandstructure.md)

Band structure shows the energy of electronic states (bands) as a function of k-point position throughout the cell.


```json tab="Schema"
{!schema/material/properties/primary/band_structure.json!}
```

```json tab="Example"
{!example/material/properties/primary/band_structure.json!}
```

### [Band Gaps](../non-scalar/bandstructure.md)

Band gap is the difference in energy from the highest occupied electronic state (Fermi energy at 0K) to the lowest unoccupied state.

```json tab="Schema"
{!schema/material/properties/primary/band_gaps.json!}
```

```json tab="Example"
{!example/material/properties/primary/band_gaps.json!}
```

### [Density of States](../non-scalar/dos.md)

Density of states contains information on the number of electronic states as a function of energy. It may include the atom resolved partial density of states and electron states in some cases. In addition it may also contain information about each atom’s spin state as well.

```json tab="Schema"
{!schema/material/properties/primary/density_of_states.json!}
```

```json tab="Example"
{!example/material/properties/primary/density_of_states.json!}
```

### [Lattice Vectors](../non-scalar/lattice.md)

Lattice vectors holds information about the three-dimensional periodic structure explicitly, by specifying three lattice vectors and their units.

```json tab="Schema"
{!schema/material/properties/primary/structural/lattice/lattice_vectors.json!}
```

```json tab="Example"
{!example/material/properties/primary/structural/lattice/lattice_vectors.json!}
```

### [Bravais Lattice](../non-scalar/lattice.md)

Lattice Bravais holds information about the 3d periodic structure specified implicitly through lengths and angles between lattice vectors, and their units.

```json tab="Schema"
{!schema/material/properties/primary/structural/lattice/lattice_bravais.json!}
```

```json tab="Example"
{!example/material/properties/primary/structural/lattice/lattice_bravais.json!}
```

### [Phonon Dispersions](../non-scalar/phonons.md)

Lattice vibrations can be plotted in the form of phonon dispersion plots across the reciprocal k-space of the crystal structure.

```json tab="Schema"
{!schema/material/properties/primary/phonon_dispersions.json!}
```

```json tab="Example"
{!example/material/properties/primary/phonon_dispersions.json!}
```

### [Stress Tensor](../non-scalar/stress-tensor.md)

Stress tensor contains a 3x3 matrix of the stress components of the unit cell.

```json tab="Schema" 
{!schema/material/properties/primary/stress_tensor.json!}
```

```json tab="Example"
{!example/material/properties/primary/stress_tensor.json!}
```

## Scalar Properties

### [Total Energy](../scalar/energies.md#total-energy)

Total energy contains the total energy of the unit cell.

```json tab="Schema" 
{!schema/material/properties/primary/total_energy.json!}
```

```json tab="Example" 
{!example/material/properties/primary/total_energy.json!}
```

### [Zero Point Energy](../scalar/energies.md#zero-point-energy)

Some residual thermal vibrational energy is left at zero temperature due to quantum effects, and is referred to as Zero Point Energy.

```json tab="Schema" 
{!schema/material/properties/primary/zero_point_energy.json!}
```

```json tab="Example" 
{!example/material/properties/primary/zero_point_energy.json!}
```

### [Fermi Energy](../scalar/energies.md#fermi-energy)

The Fermi energy marks the highest occupied energy level in a solid.

```json tab="Schema"  
{!schema/material/properties/primary/fermi_energy.json!}
```

```json tab="Example"
{!example/material/properties/primary/fermi_energy.json!}
```

### [Total Energy Contributions](../scalar/energy-contribution.md)

Total energy contributions contains information about the components in the total energy of the unit cell. The contributions available will depend on the type of method and software used.

```json tab="Schema"
{!schema/material/properties/primary/total_energy_contributions.json!}
```

```json tab="Example"
{!example/material/properties/primary/total_energy_contributions.json!}
```

### [Pressure](../scalar/pressure.md)

Pressure contains the average internal pressure of the unit cell.

```json tab="Schema"
{!schema/material/properties/primary/pressure.json!}
```

```json tab="Example"
{!example/material/properties/primary/pressure.json!}
```

### [Total Force](../scalar/total-force.md)

This is the total average force present within the crystal structure.

```json tab="Schema"
{!schema/material/properties/primary/total_force.json!}
```

```json tab="Example"
{!example/material/properties/primary/total_force.json!}
```
