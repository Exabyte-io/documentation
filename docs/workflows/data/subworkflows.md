# Subworkflow

In the computational domain, we define a **Subworkflow** as is a set of distinct units (elementary calculations) combined together in flowchart (algorithm) to extract one or more specific properties. A subworkflow must be specific (ie. have one and only one) to a particular simulation engine, model and method.

# Model

Model is an entity that contains **scientifically valuable information** about the approximations used for a **simulation**.

# Method

A model may have multiple numerical **Methods** or implementations. Since method is a numerical property, it has a certain [precision](#precision).  A method is implemented inside a [simulation engine](#simulation-engine) (or application/app), and a single simulation engine can also use one or more methods (eg. Quantum ESPRESSO, NWChem, VASP and such).

!!! note "Example Model/Method"
    If we use Newtonian mechanics as Model, then the Method would be the algorithmic implementation of calculating the multiple between m and a in the `F = ma` equation.

# Simulation Engine

A simulation engine is an implementation of a simulation algorithm in software.

# Precision

Precision characterizes the degree of numerical approximation. 

> For example, in the planewave pseudopotential method the input parameters that affect precision are:
>
>   1. k-point sampling
>   2. Number of points in irreducible Brillouin zone (N<sub>k</sub><sup>IBZ</sup>)
>   3. Electronic occupations (smearing, tetrahedra, fixed)
>   4. Smearing (gaussian, Methfessel-Paxton, Marzari-Vanderbilt, Fermi-Dirac)
>   5. Electronic wavefunction cutoff energy (or kinetic energy cutoff) - (ecutwfc)
>   6. Electronic density cutoff energy (ecutrho)

!!! note "Example Precision for a Model"
    If we use Newtonian mechanics as the model, then Precision would be limited by the numerical precision of the number format (eg. float/double) that we use while calculating `F = ma`.

# Accuracy

Accuracy measures the degree of proximity between the result of a simulation to the results of an experimental measurement (or "would-be" one).

> For Density Functional Theory Model the input parameters that affect accuracy include:
>
>   1. Electronic exchange and correlation functional used in the pseudopotentials (pseudo_xc_type)
>   2. Type of the model applied (eg. LDA, GGA, LDA + U, GGA + U, HSE, LDA + GW, GGA + GW)

!!! note "Example Accuracy for a Model"
    If we use Newtonian mechanics as the model, then the Accuracy would be limited by the relativistic effects - for example, for a spaceship it is important to introduce corrections beyond the Newtonian laws because the accuracy of it does not match experimentally found flight trajectories.

# Accuracy vs. Precision

Although Accuracy and Precision are often used interchangeably, they have different meanings. Accuracy is a direct property of the Model and can be thought about as a limit for when all computational parameters are at their optimum values. 

Precision is a characteristic of a particular computational implementation of the Model (property of Method) and is therefore directly dependent on the input parameters.


# Subworkflow modifiers

There are certain types of (sub)workflows that are commonly used in practice. We have support for their quick addition (or "modification").

## Convergence

Converges a certain property with respect to the input parameters (Example: [k-point convergence of total energy](../addons/convergence-algorithms.md))

## Optimization

Optimizes material's structure usually with respect to total energy (Example: [geometry optimization/structural relaxation](../addons/structural-relaxation.md))

# Example representation

See workflow example [here](data.md) for more details on the JSON representation.
