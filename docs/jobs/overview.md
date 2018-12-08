# Jobs

In this section we review the concept of computational "Jobs", which consist in the application of a [Workflow](../workflows/overview.md) (or simulation) on a [Material](../materials/overview.md) to produce one or more [Properties](../properties/overview.md).

Job is a "container" entity that is used to organize the data and track resource allocation. The terminology and naming is commonly used for distributed resource allocation management. A job, in the computational sense, represents the simplest entity that has accounting set up for, and can have one or more [Material](../materials/overview.md) and a single [Workflow](../workflows/overview.md) associated with it.

We implement Jobs as another [entity type](../entities-general/overview.md). As such, they have the same user interface components (with some distinct features) as other entities, as explained [here](../entities-general/ui/overview.md).

## Data

The data convention applied for Jobs including, for example, their database representation is explained [in this page](data.md).

## Status

Jobs have different statuses attributed to them depending on the level of progress of the simulation. We explain the list of possible statuses [here](status.md).

## Projects

Jobs can collectively be grouped together into [Sets](../entities-general/sets.md), which in this context are referred to as **[Projects](projects.md)**.

## User Interface

### [Explorer](ui/explorer.md)

Jobs Explorer is another specific implementation of the [Explorer](../entities-general/ui/explorer.md) component and is explained [in this page](ui/explorer.md). 

### [Designer](../jobs-designer/overview.md) 

Jobs Designer is another specific implementation of the [Designer](../entities-general/ui/designer.md) component described in more detail [here](../jobs-designer/overview.md).

### [Viewer](ui/viewer.md)
 
[This page](ui/viewer.md) explains how the [Viewer](../entities-general/ui/viewer.md) differs from Designer component in the context of Jobs.

## Actions

Some actions pertain specifically to Jobs, and are introduced [in this page](actions/overview.md).
