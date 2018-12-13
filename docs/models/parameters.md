# Model Parameters

Our platform offers the following model parameters categorization.
 
## Type
  
Density Functional Theory (DFT) is as a widely used **type** of model. Its theoretical background is reviewed further in the references contained in [this page](dft/references.md), whereas its specific parameters are narrated [here](dft/parameters.md). 

## Subtype

We refer to **subtypes** as any generic sub-classification of the main model type.
 
## Refiners

Refiners can be further added to identify a more extensive simulation approach.

### Setting Refiners in User Interface

The "Refiners" drop-down menu present under the "Overview" tab of the [Subworkflow Editor](../workflow-designer/subworkflow-editor/overview.md) interface offers the user the possibility to display additional calculated physical properties in separate dedicated columns, once the output of the workflow computation is visualized in the "Jobs" page of the Exabyte platform. 

Note that the inclusion of such refiners from within the Subworkflow Editor interface does not automatically adjust the input file content for the simulation engines involved (something that still needs to be done manually by editing the corresponding input script), but rather refers exclusively to the way the resulting properties are classified.

## Modifiers

Modifiers can be further added to identify a certain important modifications to the simulation approach (eg. the inclusion of magnetic interactions).

### Setting Modifiers in User Interface

Several modifiers can be included as part of the subworkflow under consideration, through the corresponding drop-down menu in the "Model" section of the ["Overview" tab](../workflow-designer/subworkflow-editor/overview.md) contained in the Subworflow Editor interface. 
