<!-- by MH -->

This page contains the basics about simulation workflows, their types and constituent units.

# Workflow

A workflow is a set of distinct units (elementary calculations) combined together in flowchart (algorithm) to calculate a specific characteristic property. A workflow is specific to a particular simulation engine, model and method.

<hr>

# Workflow types

## Convergence

Converges a certain property with respect to the input parameters (Example: [k-point convergence of total energy](convergence-algorithms.md))

## Optimization

Optimizes material's structure usually with respect to total energy (Example: [geometry optimization/structural relaxation](structural-relaxation.md))

## Primary

Used to calculate a specific characteristic property (Examples: [characteristic properties](../materials/characteristic-properties.md))

# Typical workflow

Often multiple convergences are performed to choose a set of input parameters. Then the structure is optimized to minimize the non-equilibrium force or pressure. Finally, a primary workflow is attempted to extract a characteristic property.

<hr>

# Workflow unit

Workflows are made of units, or elementary calculations that can be executed in succession based on algorithmic conditions.

# Workflow unit types

## Assignment

Declare, set, increment, and perform math operations on variables.  For example: iterate over a counter variable and a k-point density variable for a k-point convergence workflow.

## Execution

Calculation of a complex material property or analysis that is not possible through a simple mathematical formula.  For example: use Quantum ESPRESSO to calculate the total energy.

## Conditional

Used to make a decision on what the next unit in the workflow to be executed is.  The conditional is a mathematical formula that operates on one or more assignment variables to choose the next unit.

## Mapping

Step that is replicated for a set of input parameters.  For example: change the element name using a list "Li, Na, K, Rb, Cs, Fr"

<hr>

### Workflow example:

Currently [k-point convergence of total energy](convergence-algorithms.md) is a complex workflow with a combination of multiple assignment units, 1 execution unit for total energy, and one conditional unit used to compare the total energy with the previous total energy to see if it is converged and whether the k-point density needs to be incremented further.
