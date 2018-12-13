# Model

**Models** refer to the general theoretical approach which is considered as part of the current workflow. A model is an entity that contains scientifically valuable information about the approximations used for the given simulation.

In computational science, theoretical models are typically coupled with their corresponding numerical algorithmic implementations, or [methods](../methods/overview.md).

!!! note "Example Model"
    If we use Newtonian mechanics as Model, then we can deduce that the relation between the force applied to an object and its resulting acceleration is `F = ma` (Note: no assumptions concerning the numerical calculation of such a formula in a practical example have yet been made, which is instead the role of the method).

## [Parameters](parameters.md)

We review the parameters which affect the formulation of models [in this page](parameters.md).

## [Structured Representation](data.md)

We offer an example of JSON structured representation for a model [here](data.md).

## [Accuracy](accuracy.md)

[This page](accuracy.md) explains the relevance of the concept of accuracy in the context of models, and stresses its difference from the notion of numerical precision which is instead relevant for methods only.

## [Density Functional Theory](dft/overview.md)

We implement **Density Functional Theory** as our primary model. The specific parameters which apply to this model are reviewed [in this page](dft/overview.md), whereas a review of its theoretical background is offered in the references listed [here](dft/references.md).

## [Auxiliary Concepts](auxiliary-concepts/reciprocal-space.md)

For obvious reasons we make extensive use of the concept of **reciprocal space**. The notion of reciprocal lattice is introduced [in this section](auxiliary-concepts/reciprocal-space.md), whereas the **grids** of reciprocal lattice points, necessary for performing such calculations along the desired **paths** in reciprocal space, are described [here](auxiliary-concepts/reciprocal-space/sampling.md) and [here](auxiliary-concepts/reciprocal-space/paths.md) respectively.
