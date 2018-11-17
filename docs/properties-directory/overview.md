# List of Properties

In this section of the documentation, we review in detail the physical relevance and description of each [property](../properties/overview.md) available for computation. 

In each case, we also explain how such results are presented to the user under the interface of the [Results Tab](../jobs/ui/results-tab.md) within [Jobs Viewer](../jobs/ui/viewer.md), when results are extracted from the output of simulations. 

Illustrative examples of the [JSON schemas](../properties/data/overview.md) and associated examples for each property discussed in the present section are contained [in this page](../properties/data/list.md).

## Materials Properties

Below we provide a list of Materials properties that can be [extracted](../properties/extractor.md) on our platform. The reader can click each entry to be redirected to the relevant documentation explanation.

| Property                                             | Overview                                         |
|:---------------------------------------------------  |:------------------------------------------------|
| [Total Energy](scalar/total-energy.md)  | The ground state energy (free energy) of the system |
| [Fermi Energy](scalar/fermi-energy.md)  | The highest energy level occupied by electrons in a system |
| [Fermi Surface](non-scalar/bandstructure.md)         | Surface of constant energy (Fermi) in reciprocal space |
| [Surface Energy](scalar/surface-energy.md)           | The energy of a crystal surface |
| [Atomic forces](structural/atomic-forces.md)           | Force exerted on each atom by its surrounding |
| [Stress tensor](non-scalar/stress-tensor.md)         | 3x3 matrix expressing stresses in x, y and z dimensions |
| [Pressure](scalar/pressure.md)                       | Scalar average pressure |
| Charge density                                       | Spatial function of charge distribution |
| [Band Structure](non-scalar/bandstructure.md)        | Electronic Band Structure |
| [Band Gap](non-scalar/band-gaps.md)       | Electronic Band Gap (direct / indirect) |
| [Electronic Density of States](non-scalar/electronic-dos.md)               | Electronic Density of States (including partial contributions) |
| [Phonon Dispersions](non-scalar/phonon-dispersions.md) | The dispersion plot of lattice vibrations (phonons) frequencies |
| [Phonon Density of States](non-scalar/phonon-dos.md) | The Density of States of Phonons |
| [Zero Point Energy](scalar/zero-point-energy.md) | Energy of the lowest vibrational level wrt to vacuum |
| [Final Structure](structural/final-structure.md)     |  Visualization of the final computed crystal structure  |
| [Total Energy Contributions](scalar/total-energy.md#total-energy-contributions) | Ewald, Exchange correlation and	Hartree contributions to the total energy |
| [Magnetic Moments](structural/magnetic-moment.md)    | The magnetic moment of ferromagnetic materials when the "Magnetism" modifier is activated |
| [Total Force](scalar/total-force.md)                 | Sum of the atomic forces |
| [Basis Atoms](structural/basis-atoms.md)             | The individual atoms comprised in the crystal structure  |
| [Final Structure](structural/final-structure.md)     | The final crystal structure obtained from basis atoms and lattice |
| [Bravais Lattice](structural/lattice.md)             | The underlying Bravais Lattice of the crystal structure |
| [Space Group](structural/space-group.md)             | Information about the symmetry elements contained in crystal structure |
| [Atomic Radius](elemental/atomic-radius.md) | The mean distance between atomic nucleus and edge of electron cloud |
| [Electronegativity](elemental/electronegativity.md) | The capacity of the atom to attract shared electrons |
| [Ionization Potential](elemental/ionization-potential.md) | The energy required to strip an atom of its outermost electron |

## Workflow Monitors

Below we list the data points that can be monitored during the course of the execution of a [Workflow](../workflows/overview.md) computation.

| Output information | Overview |
|:---------------   |:------------|
| Standard Output   | Standard output of an execution unit in UNIX sense |
| Ionic Convergence | Convergence information on ionic moves in relaxation or molecular dynamics calculations |
| Electronic Convergence  | Convergence information on self-consistent electronic calculation steps |
