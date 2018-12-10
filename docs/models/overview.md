# Model

**Models** refer to the general theoretical approach which is considered as part of the current workflow. A model is an entity that contains scientifically valuable information about the approximations used for the given simulation.

In computational science, theoretical models are typically coupled with their corresponding numerical algorithmic implementations, or [methods](../methods/overview.md).
 
!!! note "Example Model & Method"
    If we use Newtonian mechanics as Model, then the Method would be the algorithmic implementation of calculating the multiple between m and a in the `F = ma` equation.

## [Data Representation Schema]()

Our platform offers the following example model categorization.
 
### [Type](../models/dft/overview.md)
  
Density Functional Theory (DFT) is as a widely used **type** of model. Its theoretical background is reviewed further in [this page](../models/dft/overview.md), 

### [Subtype]()
 
Generalized Gradient Approximation (GGA) is the corresponding model **subtype**, 

### [Functional]()

The particular flavor of exchange-correlation **functional** is the one due to **Perdew, Burke and Ernzerhof** (PBE).

### [Refiners]() 

Refiners can be further added to identify a more extensive simulation approach.

#### [Setting Refiners in User Interface]()

The "Refiners" drop-down menu present under the "Overview" tab of the [Subworkflow Editor](../workflow-designer/subworkflow-editor/overview.md) interface offers the user the possibility to display additional calculated physical properties in separate dedicated columns, once the output of the workflow computation is visualized in the "Jobs" page of the Exabyte platform. 

Note that the inclusion of such refiners from within the Subworkflow Editor interface does not automatically adjust the input file content for the simulation engines involved (something that still needs to be done manually by editing the corresponding input script), but rather refers exclusively to the way the resulting properties are classified.

### [Modifiers]()

Modifiers can be further added to identify a certain important modifications to the simulation approach (eg. the inclusion of magnetic interactions).

### [Setting Refiners in User Interface]()

Several modifiers can be included as part of the subworkflow under consideration, through the corresponding drop-down menu in the "Model" section of the ["Overview" tab](../workflow-designer/subworkflow-editor/overview.md) contained in the Subworflow Editor interface. These in particular allow for the inclusion of the following two atomic physical phenomena.

## [Auxiliary Concepts]()

For obvious reasons we make extensive use of the concept of **reciprocal space**. The notion of reciprocal lattice is introduced [in this section](auxiliary-concepts/reciprocal-space.md), whereas the **grids** of reciprocal lattice points, necessary for performing such calculations along the desired **paths** in reciprocal space, are described [here](auxiliary-concepts/reciprocal-space/sampling.md) and [here](auxiliary-concepts/reciprocal-space/paths.md) respectively.

## [Example JSON Representation]()

The example of a JSON data structure is shown in the expandable section below. The associated method components are also included in this example, and are explained further [in this page](../methods/overview.md). 

### [JSON source]()

<details markdown="1">
  <summary>
     "Expand to view": ...
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
                    { ...pseudopotentialData }
                ]
            }
        }
    }
}
```

</details>
