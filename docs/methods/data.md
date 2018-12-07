# Structured Representation of Methods

In order to organize and store the information about [Methods](overview.md), we employ the **Exabyte Data Convention**, as explained [elsewhere](../data-structured/overview.md) in the documentation.

Below, the user can find an example JSON structured representation of a [Method](overview.md). 

```json tab="Schema" 
{!schema/workflow/subworkflow/model/method.json!}
```

An example of the above representation can be found below.

```json tab="Schema" 
{!example/workflow/subworkflow/model/method.json!}
```

## Precision

Since method is a numerical property, it has a certain **numerical precision** associated with it regarding the [properties](../properties/overview.md) that it calculates, characterizing the degree of numerical approximation.

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
