# Definition of Models

**Models**, in the context of the Exabyte platform, refer to the various aspects of the general theoretical approach which is to be considered as part of the current workflow. As such, a model is an entity that contains **scientifically valuable information** about the approximations used for the given simulation.

In computational science, theoretical models are typically coupled with their corresponding numerical algorithmic implementations, or [methods](/methods/overview.md).
 
!!! note "Example Model & Method"
    If we use Newtonian mechanics as Model, then the Method would be the algorithmic implementation of calculating the multiple between m and a in the `F = ma` equation.

# Available Models

For the moment, the Exabyte platform offers the following combination of model type and subtypes, already selected by default in any newly-created subworkflow. The theoretical background underlying such model concepts is reviewed further in [this page](/models/dft/density-functional-theory.md). 
 
- We consider **Density Functional Theory** (DFT) as our conventional theoretical model **type**.
 
- We assume the **Generalized Gradient Approximation** (GGA) model **subtype** for the Exchange-Correlation part of the total energy functional of the crystal being studied. 

- The particular flavor of GGA **functional** implemented as part of this DFT model is the one due to **Perdew, Burke and Ernzerhof** (PBE).

- We make extensive use of the concept of **reciprocal space** and **reciprocal lattices** for performing phonon or band structure dispersion calculations. The notion of reciprocal lattice is introduced [in this section](dft/reciprocal-space.md), whereas the **grids** of reciprocal lattice points, necessary for performing such calculations along the desired **paths** in reciprocal space, are described [here](dft/sampling.md) and [here](dft/paths.md) respectively.

# Example of JSON data structure

The example of a JSON data structure excerpt shown in the expandable section below demonstrates how the various hierarchical classes of model components are stored internally within the Workflow Designer interface. The associated method components are also included in this example, and are explained further [in this page](/methods/overview.md). 

## JSON source

<details>
  <summary>
     "Expand to view content": ...
  </summary> 

```json
{
    "model": {
        "type": "dft",
        "subtype": "gga",
        "method": {
            "type": "pseudopotential",
            "subtype": "paw",
            "data": {
                "pseudo": [
                    {
                        "apps": [
                            "vasp"
                        ],
                        "element": "Ho",
                        "version": "5.2",
                        "type": "paw",
                        "exchangeCorrelation": {
                            "approximation": "gga",
                            "functional": "pbe"
                        }
                    }
                ]
            }
        }
    }
}
```
</details>
 
# Refiners 

The "Refiners" drop-down menu present under the "Overview" tab of the Subworkflow Editor interface offers the user the possibility to display additional calculated physical properties in separate dedicated columns, once the output of the workflow computation is visualized in the "Jobs" page of the Exabyte platform. 

Note that the inclusion of such refiners from within the Subworkflow Editor interface does not make them an integral part of the workflow computation per se (something that still needs to be done manually by editing the corresponding input script), but rather refers exclusively to the way the output data columns themselves are presented.

# Modifiers

Several modifiers can be included as part of the subworkflow computation under consideration, through the corresponding drop-down menu in the "Model" section of the ["Overview" tab](/workflow-designer/subworkflow-editor/overview.md) contained in the Subworflow Editor interface. These in particular allow for the inclusion of the following two atomic physical phenomena:

- Spin-Orbit Coupling (soc), a relativistic quantum physical interaction of a particle's spin with its motion inside a potential [[1](#Links)]. 

- Magnetism (magn), resulting from the spontaneous polarization (parallel lining up) of the spins of conduction electrons in ferromagnetic metals, such as iron, nickel and cobalt, giving rise to a magnetic moment in these materials even in the absence of an externally applied magnetic field [[2](#Links)].


# Links

1. [Wikipedia Spin–orbit interaction, website](https://en.wikipedia.org/wiki/Spin%E2%80%93orbit_interaction)
2. [Wikipedia Ferromagnetism, website](https://en.wikipedia.org/wiki/Ferromagnetism)
