# Plane-Waves Pseudopotential Method

The **"Plane-waves Pseudopotential Method"** is based upon the implementation of **plane-waves as a basis set** for expanding the electronic ground-state wavefunction of the material [^1], as well as the adoption of **pseudopotentials** for encapsulating the core electrons of atoms and formulating inter-atomic interactions exclusively on the effects of the outermost valence electrons.
 
This method is widely used as an effective algorithmic recipe for the computational formulation and implementation of the [DFT theoretical model](../../models/dft/parameters.md).  

## [Parameters](parameters.md)

[This page](parameters.md) contains a list of the fundamental computational parameters involved in the Plane-waves Pseudopotential Method.

## [Actions](actions.md)

We introduce [here](actions.md) the action for uploading a custom Pseudopotential file to our platform via the [Subworkflow Editor Interface](../../workflow-designer/subworkflow-editor/overview.md). 

## [Precision](precision.md)

We discuss the parameters that limit the [numerical precision](../precision.md) of the plane-waves pseudopotential method [here](precision.md).

## Links

[^1]: [Plane Waves as a Basis, Durham University Website](http://cmt.dur.ac.uk/sjc/thesis_dbj/node16.html)

[^2]: [Wikipedia Pseudopotential, Website](https://en.wikipedia.org/wiki/Pseudopotential)
