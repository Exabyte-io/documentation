# List of Properties

## Materials Properties

Below we provide a list of Materials properties that can be [extracted](../properties/extractor.md) on our platform. The reader can click each entry to be redirected to the relevant documentation explanation.

| Property                                             | Overview                                         |
|:---------------------------------------------------  |:------------------------------------------------|
| [Total Energy](../properties-directory/scalar/total-energy.md#total-energy)      | The ground state energy (free energy) of the system |
| [Fermi Energy](../properties-directory/scalar/total-energy.md#fermi-energy)      | The highest energy level occupied by electrons in a system |
| [Fermi Surface](non-scalar/bandstructure.md)         | Surface of constant energy (Fermi) in reciprocal space |
| [Atomic forces](structural/basis-atoms.md)                | Force exerted on each atom by its surrounding |
| [Stress tensor](non-scalar/stress-tensor.md)         | 3x3 matrix expressing stresses in x, y and z dimensions |
| [Pressure](scalar/pressure.md)                       | Scalar average pressure |
| Charge density                                       | Spatial function of charge distribution |
| [Band Structure](non-scalar/bandstructure.md)        | Electronic Band Structure |
| [Band Gap](../properties-directory/scalar/total-energy.md#band-gap-energy)       | Electronic Band Gap (direct / indirect) |
| [Density of States](../properties-directory/non-scalar/dos.md)               | Electronic Density of States (including partial contributions) |
| [Zero Point Energy](../properties-directory/scalar/total-energy.md#zero-point-energy) | Energy of the lowest vibrational level wrt to vacuum |
| [Final Structure](structural/final-structure.md)     |  Visualization of the final computed crystal structure  |
| [Total Energy Contributions](scalar/energy-contribution.md) | Ewald, Exchange correlation and	Hartree contributions to the total energy |
| Magnetic Moments                                     | The magnetic moment of ferromagnetic materials when the "Magnetism" modifier is activated |
| [Total Force](scalar/total-force.md)                 | Sum of the atomic forces |

## Workflow Monitors

Below we list the data points that can be monitored during the course of the execution of a [Workflow](../workflows/overview.md) computation.

| Output information | Overview |
|:---------------   |:------------|
| Standard Output   | Standard output of an execution unit in UNIX sense |
| Ionic Convergence | Convergence information on ionic moves in relaxation or molecular dynamics calculations |
| Electronic Convergence  | Convergence information on self-consistent electronic calculation steps |
