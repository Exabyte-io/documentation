# Important Concepts

In this page we introduce some important concepts explaining the operations of our platform. Links are attached to the keywords below, redirecting the user to the relevant documentation section containing more explanation.

## Relationship

Our platform enables the execution of computational **[Workflows](../workflows/overview.md)** applied upon **[Materials](../materials/overview.md)**, in order to extract a set of desired **[Properties](../properties/overview.md)**. We refer to **[Jobs](../jobs/overview.md)** as "containers" of Workflows and Materials information. 

The flowchart diagram below visualizes the general relationship between the above-mentioned entity types. Here, the Properties associated to each entity are labeled with <span class="btn badge badge-property border-50">P</span>. Those properties which are computed as output of a Job (also referred to as [Characteristic Properties](../properties/classification/general.md)), are shown in black - <span class="btn badge badge-property-inverse border-50">P</span>, and consequently have a certain numerical [precision](../methods/data.md) inherited from the Workflow and Job.

![Entities Relations](../images/getting-started/entities-relations.png "Entities Relations")

Jobs also refer to the simulation tasks on the Compute platform, as illustrated in the visual below.

![Simulation Components](../images/getting-started/simulation-components.png "Simulation Components")

## Main Entities

The three above-mentioned concepts of Workflows, Materials and Jobs can be grouped together under the same general umbrella term of **[Entities](../entities-general/overview.md)**, due to the many features and user interface components that they share in common. We review the similarities under [Entities and Common Aspects](../entities-general/overview.md) and then explain the details unique to each Entity type separately. 

For example, Jobs have **[Accounting](../accounts/overview.md)** set up for. Workflows and Materials are both **["Bankable" Entities](../entities-general/bank.md)**. Workflows further consist of **[Subworkflows](../workflows/components/subworkflows.md)**, and further of the combination of individual **[Units](../workflows/components/units.md)**, such as portrayed in the example diagram below.

![Workflow Components](../images/getting-started/workflow-components.png "Workflow Components")

## Other Items

Such simulations can be performed with any of the available **[modeling Applications](../software/applications.md)**, implementing the supported **[theoretical Models](../models/overview.md)** and corresponding **[computational Methods](../methods/overview.md)**.

## Data and Infrastructure

Our platform is designed to store and organize the **[simulation Data](../data/classification.md)** in centralized databases, under the conventions of **[Structured Representation](../data-structured/convention.md)**. A system of **[Queues](../infrastructure/resource/queues.md)** is in place for scheduling and tracking the allocation of **[computational Resources](../infrastructure/resource/overview.md)**, offered by the **[Clusters](../infrastructure/clusters/overview.md)** at the heart of our overall **[Infrastructure](../infrastructure/overview.md)**.
