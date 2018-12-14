# Accuracy

The **Accuracy** measures the degree of proximity between the result of a simulation to the results of a realistic experimental measurement.

!!! note "Example Accuracy for a Model"
    If we use Newtonian mechanics as the model, then the Accuracy would be limited by the relativistic effects - for example, for a spaceship traveling close to the speed of light it is important to introduce corrections beyond the Newtonian laws, because the accuracy of it does not match experimentally-found relativistic flight trajectories.

## Accuracy vs. Precision

Although Accuracy and Precision are often used interchangeably, they have different meanings. 

[Precision](../methods/precision.md) is a numerical characteristic of the [Method](../methods/overview.md), intended as a particular computational implementation of the Model, and is therefore directly dependent on the choice of input [compute parameters](../methods/pseudopotential/parameters.md).  

Accuracy is a direct property of the theoretical [Model](parameters.md) itself, and can be thought about as a limit for when all computational parameters are set to their optimum values, thus yielding full-precision calculations. 
