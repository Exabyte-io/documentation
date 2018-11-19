# Properties 

The present section of the documentation explains our approach to organizing, storing and interacting with the **properties** of the different [entities](../entities-general/overview.md) present across our platform.

## Definition
 
**"Property"** is any measurable quantity which provides information about the entity under consideration. Properties can hold information about [Materials](../materials/overview.md) and [Workflows](../workflows/overview.md) as demonstrated [here](../getting-started/important-concepts.md)

Exact set of properties that have to be supplied to, and can be extracted as a result of, a [Job](../jobs/overview.md) computation, can vary depending on the Workflow type and on the [models](../models/overview.md)/[methods](../methods/overview.md) included therein.

## List of Properties

We have listed and described the properties available for computation on our platform [in this section](../properties-directory/overview.md).

## Classification

We explain how properties can be classified into different categories [here](classification/overview.md).

## Data

For an example of a JSON structure-based representation of properties, and of the associated validating/descriptive schema, please consult the [Data section](data/overview.md).

## Lifecycle

We describe the lifecycle that properties go through in order to be extracted from simulation output, and then subsequently refined and retrieved, [in this section](lifecycle/overview.md).

## User Interface

Properties are presented in special panels within the user interface of the [Job Viewer](../jobs/ui/viewer.md). One of such panels contains the **final computed structure**, displayed under an instance of [Materials Viewer](../materials/ui/viewer.md). It is described separately [here](ui/viewer.md).

These properties can also be reviewed under a dedicated [Explorer-type interface](../entities-general/ui/explorer.md) for each Material stored in the account-owned [collection](../accounts/collections.md). We explain how to retrieve and inspect the contents of this Properties Explorer [in this page](ui/explorer.md). 
