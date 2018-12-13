# Method

A theoretical [model](../models/overview.md) may have multiple **Methods**, or computational implementations. Since a method is a numerical property, it always has a certain precision. A method is implemented inside a **simulation engine** (or [application](../software/overview.md)), and each application can itself implement one or more methods.

!!! note "Example Model & Method"
    If we use Newtonian mechanics as Model, then the Method would be the algorithmic implementation of calculating the multiple between m and a in the `F = ma` equation.

## [Structured Representation](data.md)

We offer an example of JSON structured representation for a method [here](data.md).

## [Precision](precision.md)

[This page](precision.md) explains the relevance of the concept of numerical precision in the context of methods.

## [Plane-wave Pseudopotential Method](pseudopotential/overview.md)

We consider the **Plane-wave Pseudopotential** approach towards implementing the [Density Functional Theory](../models/dft/parameters.md) model as our primary method. This method is introduced in the [following section](pseudopotential/overview.md) of the documentation.
