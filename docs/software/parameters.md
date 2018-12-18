# Applications

The concept of **"Software Application"** is related to the main **modeling engine** and associated software tools employed by the user for the design, execution and postprocessing of a [simulation Job](../jobs/overview.md), through the implementation of any of the available [computational methods](../methods/overview.md). 

Each application may be comprised of one or multiple **Executables**, implementing in turn different possible computation **Flavors**. These settings can be entered within the [unit editor interface](../workflow-designer/unit-editor.md#application) of [Workflow Designer](../workflow-designer/overview.md).

## Executables

Applications are typically run via the launching of their respective executable binary files [^1] (more simply referred to as Executables), of which there may be just one or multiple.

### Example

The [Quantum ESPRESSO](../software-directory/modeling/quantum-espresso.md) modeling application for example is comprised of several main input executables, included as part of its distribution package, such as `pw.x`, `ph.x`, `bands.x` etc.

Other applications such as [VASP](../software-directory/modeling/vasp.md) on the other hand contain just a single main executable, through which all of its supported computation features can be performed.

## Flavors

The executables for running modeling applications may in turn be composed of numerous distinct Flavors, implementing different forms and types of materials computations such as total ground-state energy calculations, structural relaxations or electronic bandstructure calculations.

## Links

[^1]: [Wikipedia Executable, Website](https://en.wikipedia.org/wiki/Executable)
