# Subworkflow

In the computational domain, we define a **Subworkflow** as a set of distinct **units** (elementary calculations) combined together in flowchart (algorithm), in order to extract one or more specific [property](../../properties/overview.md). A subworkflow must be specific to a particular [simulation engine](../../software/applications.md), [model](../../models/overview.md) and [method](../../methods/overview.md).

## Model

A **Model** is an entity that contains **scientifically valuable information** about the approximations used for a **simulation**. Models are the object of a [separate discussion](../../models/overview.md).

## Method

A model may have multiple numerical **Methods**, or computational implementations, which are described in detail [here](../../methods/overview.md). Since method is a numerical property, it has a certain [precision](#precision) associated with it. A method is implemented inside a [simulation engine](#simulation-engine) (or application), and a single simulation engine can also use one or more methods.

!!! note "Example Model/Method"
    If we use Newtonian mechanics as Model, then the Method would be the algorithmic implementation of calculating the multiple between m and a in the `F = ma` equation.

## Simulation Engine

A **Simulation Engine** is an implementation of a simulation algorithm in software. The engines available on our platform are reviewed [in this section](../../software/applications.md) of the documentation.

## Precision

The **Precision** characterizes the degree of numerical approximation. 

> For example, in the planewave pseudopotential method, the input parameters that affect precision are:
>
>   1. k-point sampling
>   2. Number of points in irreducible Brillouin zone (N<sub>k</sub><sup>IBZ</sup>)
>   3. Electronic occupations (smearing, tetrahedra, fixed)
>   4. Smearing (gaussian, Methfessel-Paxton, Marzari-Vanderbilt, Fermi-Dirac)
>   5. Electronic wavefunction cutoff energy (or kinetic energy cutoff) - (ecutwfc)
>   6. Electronic density cutoff energy (ecutrho)

!!! note "Example Precision for a Model"
    If we use Newtonian mechanics as the model, then Precision would be limited by the numerical precision of the number format (eg. float/double) that we use while calculating `F = ma`.

## Accuracy

**Accuracy** measures the degree of proximity between the result of a simulation to the results of an experimental measurement (or "would-be" one).

> For Density Functional Theory Model, the input parameters that affect accuracy include:
>
>   1. Electronic exchange and correlation functional used in the pseudopotentials (pseudo_xc_type)
>   2. Type of the model applied (eg. LDA, GGA, LDA + U, GGA + U, HSE, LDA + GW, GGA + GW)

!!! note "Example Accuracy for a Model"
    If we use Newtonian mechanics as the model, then the Accuracy would be limited by the relativistic effects - for example, for a spaceship it is important to introduce corrections beyond the Newtonian laws because the accuracy of it does not match experimentally found flight trajectories.

## Accuracy vs. Precision

Although Accuracy and Precision are often used interchangeably, they have different meanings. Accuracy is a direct property of the theoretical Model, and can be thought about as a limit for when all computational parameters are at their optimum values. 

Precision is a numerical characteristic of a particular computational implementation of the Model, that is of the Method itself, and is therefore directly dependent on the input parameters.

## Subworkflow Modifiers

There are certain types of (sub)workflows that are commonly used in practice. We have support for their quick addition (or "modification"), as explained for the following two cases.

### Convergence

This option converges a certain property with respect to the input parameters (Example: [k-point convergence of total energy](../addons/convergence-algorithms.md)). 

### Optimization

This second option optimizes the material's structure, typically with respect to the total energy, in order to find the most stable equilibrium configuration of the crystal structure (Example: [geometry optimization/structural relaxation](../addons/structural-relaxation.md)).

## Example Structured Representation

The reader is referred to the example contained [here](data.md) for more details on the JSON structured representation of workflows.
