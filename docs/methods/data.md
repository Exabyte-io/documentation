# Structured Representation of Methods

In order to organize and store the information about [Methods](overview.md), we employ the **Exabyte Data Convention**, as explained [elsewhere](../data-structured/overview.md) in the documentation.

Below, the user can find an example JSON structured representation of a [Method](overview.md). 

```json tab="Schema" 
{!schema/workflow/subworkflow/model/method.json!}
```

```json tab="Example" 
{!example/workflow/subworkflow/model/method.json!}
```

## Precision

Since method is a numerical property, it has a certain **Numerical Precision** associated with it with regards to the [properties](../properties/overview.md) that it calculates, characterizing the degree of numerical approximation.

For example, in the [planewave pseudopotential method](pseudopotential/overview.md), the input parameters that affect precision include the following.

   1. k-point sampling
   2. Number of points in irreducible Brillouin zone (N<sub>k</sub><sup>IBZ</sup>)
   3. Electronic occupations (smearing, tetrahedra, fixed)
   4. Smearing (gaussian, Methfessel-Paxton, Marzari-Vanderbilt, Fermi-Dirac)
   5. Electronic wavefunction cutoff energy (or kinetic energy cutoff) - (ecutwfc)
   6. Electronic density cutoff energy (ecutrho)

!!! note "Example Precision for a Model"
    If we use Newtonian mechanics as the model, then Precision would be limited by the numerical precision of the number format (eg. float/double) that we use while calculating `F = ma`.

## Accuracy

The **Accuracy** measures the degree of proximity between the result of a simulation to the results of a realistic experimental measurement.

For the case of the [Density Functional Theory Model](../models/dft/overview.md), the input parameters that affect accuracy include the ones listed below.

   1. Electronic exchange and correlation functional used in the pseudopotentials (pseudo_xc_type)
   2. Type of the model applied (eg. LDA, GGA, LDA + U, GGA + U, HSE, LDA + GW, GGA + GW)

!!! note "Example Accuracy for a Model"
    If we use Newtonian mechanics as the model, then the Accuracy would be limited by the relativistic effects - for example, for a spaceship traveling close to the speed of light it is important to introduce corrections beyond the Newtonian laws, because the accuracy of it does not match experimentally-found relativistic flight trajectories.

## Accuracy vs. Precision

Although Accuracy and Precision are often used interchangeably, they have different meanings. Accuracy is a direct property of the theoretical [Model](../models/overview.md), and can be thought about as a limit for when all computational parameters are at their optimum values. 

Precision is a numerical characteristic of the [Method](overview.md) itself, intended as a particular computational implementation of the Model, and is therefore directly dependent on the choice of input compute parameters.
