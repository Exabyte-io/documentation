<!-- by MH -->

A workflow is a set of distinct units combined together in a hierarchical way to calculate a specific characteristic property. A workflow is specific to a particular simulation engine

# Workflow types

## Convergence

Converges a certain property with respect to the input parameters (Example: [k-point convergence of total energy](convergence-algorithms.md))

## Optimization

Optimizes a materials structure usually with respect to total energy (Example: [geometry optimization/structural relaxation](strucural-relaxation.md))

## Primary

Used to calculate a specific characteristic property (Examples: [characteristic properties](../materials/characteristic-properties.md))

# Typical workflow

Often multiple convergences are performed to choose a set of input parameters. Then the structure is optimized to minimize the non-equilibrium force or pressure. Finally, a primary workflow is attempted to extract a characteristic property.

<hr>

# Workflow unit building blocks

## Assignment

Declare, set, increment, and perform math operations on variables.  For example, iterating over a counter variable and a k-point density variable for k-point convergence.

## Execution

Calculation a complex material property or analysis that is not possible through a simple mathematical formula.  For example: use Quantum ESPRESSO to calculate the total energy of a system.

## Conditional

The diagram below shows an example implementation of a conditional that adjusts the input data for a unit based on the materials property:

## Mapping

Step replicated for a set of input parameters.  For example: change the element name using a list "Li, Na, K, Rb, Cs, Fr"

### Workflow example:

Currently [k-point convergence of total energy](convergence-algorithms.md) is our most complex workflow with a combination of multiple assignment units, 1 execution unit for total energy, and one conditional unit used to determine whether the total energy is converged or whether the k-point density needs to be incremented further.