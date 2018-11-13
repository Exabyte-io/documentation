# Structure-based approach

Our current work is focused on **structure-based** atomistic approach, where the information about the atomistic arrangement is known *a priori* (see [data conventions](/data/overview.md)).

!!! note "Non-structure-based scenario"
    Our data convention has support for materials data where no structural information is available, however this topic is beyond the content of the current documentation.

## Example Representation

For examples of JSON representation of materials and structure-based descriptors see [materials data](data.md) section.

## Features, Fingerprints, Targets

On many occasions terms "Features", "Fingerprints", "Targets" are used for materials informatics purposes. For example, when constructing a machine learning model a dataset containing information about multiple materials is used in order to find regular patterns and inter-dependencies. Such dataset is usually split into properties that represent the known data, or *features*, and the properties to be predicted, or *targets*.
 First we clarify this terminology as follows:

- **Feature**: any property of a material, eg. density or electronic band gap.
- **Fingerprint**: property of a material used as an input for a (statistical modeling) Workflow, equivalent of **Descriptive** property by definition

    > By default, we only store the minimal amount of information required to identify a material enough to reveal a set of its **Fingerprints**. Such minimal set of properties is called **Identity Fingerprints**, and the rest - **Derived Fingerprints**.

 - **Target**: property of a material used as an input for a (statistical modeling) Workflow, equivalent of a **Characteristic** property by definition.

 Thus a *property-descriptive-characteristic* triad is equivalent to *feature-fingerprint-target*.


# Example properties

Exact set of Materials properties that have to be supplied to and can be extracted as a result of a Workflow vary based on the type of Workflow and models/methods included therein.

## Results

Below we provide example properties extracted by the using [Density Functional Theory](/models/dft) (DFT) as simulation results:

| Property          | Overview    |
|:----------------- |:------------|
| Total Energy      | The ground state energy (free energy) of the system |
| Fermi Energy      | The highest energy level occupied by electrons in a system |
| Fermi Surface     | Surface of constant energy (Fermi) in reciprocal space |
| Atomic forces     | Force exerted on each atom by its surrounding |
| Stress tensor     | 3x3 matrix expressing stresses in x, y and z dimensions |
| Pressure          | Scalar average pressure |
| Charge density    | Spatial function of charge distribution |
| Band Structure    | Electronic Band Structure |
| Band Gap          | Electronic Band Gap (direct / indirect) |
| Density of States | Electronic Density of States (including partial contributions) |
| Zero Point Energy | Energy of the lowest vibrational level wrt to vacuum |
| Final Structure   |  Visualization of the final computed crystal structure  |
| Total Energy Contributions | Ewald, Exchange correlation and	Hartree contributions to the total energy |
| Magnetic Moments  | The magnetic moment of ferromagnetic materials when the "Magnetism" modifier is activated |
| Total Force       | Sum of the atomic forces |

## Monitors

These are the data points that can be monitored during the course of a DFT calculation:

| Output information | Overview |
|:---------------   |:------------|
| Standard Output   | Standard output of an execution unit in UNIX sense |
| Ionic Convergence | Convergence information on ionic moves in relaxation or molecular dynamics calculations |
| Electronic Convergence  | Convergence information on self-consistent electronic calculation steps |


