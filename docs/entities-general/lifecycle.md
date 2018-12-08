# Entities Lifecycle

We explain in this page the **Lifecycle** that [entities](overview.md) go through on our platform from the moment of their design by the users, to the moment they are sent to the [computing clusters](../infrastructure/clusters/overview.md) of our [infrastructure](../infrastructure/overview.md) for **Job Execution**. This lifecycle concludes when the relevant entity [Properties](../properties/overview.md) are extracted from the output of the Job simulation, and finally stored as [structured data](../data-structured/overview.md) in the database.

The entity lifecycle is portrayed in the diagram below, where the four main logical steps involved are labelled. Each of these steps is reviewed separately in the ensuing explanations. Further information about the general data lifecycle within our platform can be retrieved [here](../data/lifecycle.md).

![Entities Lifecycle](/images/entities-lifecycle.png "Entities Lifecycle")

## 1. Job Design

New [simulation Jobs](../jobs/overview.md) can be designed by the user with the help of the [Job Designer Interface](../jobs-designer/overview.md). Jobs can be designed in this way by assembling together a [material](../materials/overview.md) structure with a corresponding [Workflow computation](../workflows/overview.md).

## 2. Submit and Execute Jobs

The Jobs designed in the preceding step can then be submitted to our [computing clusters](../infrastructure/clusters/overview.md) for their execution.

## 3. Extraction of Properties

At the end of Job execution, the computed [Properties](../properties/overview.md) can finally be [extracted](../properties/lifecycle/extractor.md) and [refined](../properties/lifecycle/refinement.md) from the corresponding simulation output, for their final storage in the database as [structured data](../data-structured/overview.md).

## 4. Analysis of Results

The user is then free to inspect, manipulate and analyse the entity properties output by simulations by [retrieving](../properties/lifecycle/retrieval.md) them from the relevant [Account-owned entity collections](../accounts/collections.md), as displayed to the user under the corresponding [Explorer Interface](ui/explorer.md) for the given entity type.
