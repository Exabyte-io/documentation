# Structured Representation of Workflows

In order to organize and store the information about [workflows](../overview.md), we employ the **Exabyte Data Convention**, as explained [elsewhere](../../data-structured/overview.md) in this documentation.

In the expandable section below, the user can find an example JSON representation of a [workflow](../overview.md). It contains a series of [subworkflows](../components/subworkflows.md), each of which contains a number of [units](../components/units.md) in turn. 

<details markdown="1">
  <summary>
     Expand to view
  </summary> 

```json tab="Schema" 
{!schema/workflow.json!}
```

</details>

An example of the above representation can be found below.

<details markdown="1">
  <summary>
     Expand to view
  </summary> 

```json tab="Schema" 
{!example/workflow.json!}
```

</details>

There are a few notable points to emphasize from the example above.

## Nested data

We use top-level workflow as a "container", and separate the details of each individual section of calculation inside a subworkflow.

## Execution Units 

For the case of physics-based [modeling engines](../../software/applications.md), the execution unit is the main one. It contains the information about the input parameters and runtime environment for the specific simulation engine.

## Templating

We allow for using [templates](../templates/overview.md) inside the input to individual units. In this way, we can decouple material-specific information from the workflow-specific one. More explanation can be found inside the [units documentation page](../components/units.md).

## Properties

The "Properties" section serves as an aggregator of all the [properties](../../properties/overview.md) that are extracted at the workflow or subworkflow levels. The "results" key serves the same purpose, but for the case of units.  
