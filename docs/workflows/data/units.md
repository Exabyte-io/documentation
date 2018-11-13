# Sub/Workflow units

Workflows are made of units, or elementary calculations that can be executed in succession based on algorithmic conditions.

# Unit types

## Execution

Used for computationally-heavy tasks, eg. for a singular application of a physics-based simulation engine. For the input templating see [this page](templates.md).

## Processing

Used for data processing tasks that are not computationally intensive in nature, eg. data cleaning.

## I/O

Perform input/output operations, such as reading from a remote database, RESTful API.

## Assignment

Declare, set, increment, and perform math operations on variables.  For example: iterate over a counter variable and a k-point density variable for a k-point convergence workflow.

## Conditional

Used to make a decision on what the next unit in the workflow to be executed is.  The conditional is a mathematical formula that operates on one or more assignment variables to choose the next unit.

## Map/Reduce

Step that is replicated for a list of input parameters.  For example: run a total energy calculation subworkflow using a list "Li, Na, K, Rb, Cs, Fr" materials as inputs.
