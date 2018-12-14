# Subworkflow Units

[Subworkflows](subworkflows.md) are composed of one or multiple **units**, or elementary calculations that can be executed in succession based on algorithmic conditions.

## Unit types

The following types of units are available.

### Execution

Used for computationally-heavy tasks, e.g. for a singular run of a physics-based simulation engine. For physics-based [modeling engines](../../software/applications.md), the execution unit is the main one. It contains the information about the input parameters and runtime environment for the specific simulation engine.

### Processing

Used for data processing tasks that are not computationally intensive in nature, eg. data cleaning.

### I/O

Perform input/output operations, such as reading from a remote database.

### Assignment

Declare, set, increment, and perform math operations on variables. For example: iterate over a counter variable and a k-point density variable for a k-point convergence workflow.

### Conditional

Used to make a decision on what should be the next unit in the workflow to be executed. The conditional is a mathematical formula that operates on one or more assignment variables to choose the next unit.

### Map/Reduce

Step that is replicated for a list of independent input parameters. For example: run a total energy calculation subworkflow using a list of materials such as "Li, Na, K, Rb, Cs, Fr" as inputs.
