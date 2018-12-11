# Subworkflow Units

[Subworkflows](subworkflows.md) are composed of one or multiple **units**, or elementary calculations that can be executed in succession based on algorithmic conditions.

## Example Structured Representation

The JSON [structured representation](../../data-structured/overview.md) of units is contained in the expandable section below. For a description of unit input templating, the reader is referred to [this section](../templates/overview.md) of the documentation.

<details markdown="1">
  <summary>
     Expand to view
  </summary> 

```json tab="Schema" 
{!schema/workflow/unit.json!}
```

</details>

An example of the above representation can be found below.

<details markdown="1">
  <summary>
     Expand to view
  </summary> 

```json tab="Schema" 
{!example/workflow/unit.json!}
```

</details>

## Unit types

The following types of units are available to be combined together.

### Execution

Used for computationally-heavy tasks, e.g. for a singular application of a physics-based simulation engine. 

### Processing

Used for data processing tasks that are not computationally intensive in nature, eg. data cleaning.

### I/O

Perform input/output operations, such as reading from a remote database.

### Assignment

Declare, set, increment, and perform math operations on variables. For example: iterate over a counter variable and a k-point density variable for a k-point convergence workflow.

### Conditional

Used to make a decision on what should be the next unit in the workflow to be executed. The conditional is a mathematical formula that operates on one or more assignment variables to choose the next unit.

### Map/Reduce

Step that is replicated for a list of input parameters. For example: run a total energy calculation subworkflow using a list of materials such as "Li, Na, K, Rb, Cs, Fr" as inputs.
