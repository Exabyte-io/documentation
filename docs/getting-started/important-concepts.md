# Important Concepts

In this page we introduce some important concepts which pertain to how material modeling simulations are executed within our platform. Links are attached to each important keyword mentioned here, redirecting the user to the relevant documentation section containing the full explanation.

## Overview

Our platform enables the execution of computational **[Workflows](../workflows/overview.md)** applied upon **[Materials](../materials/overview.md)**, in order to extract a set of desired **[Properties](../properties/overview.md)**. We refer to **[Jobs](../jobs/overview.md)** as "containers" of Workflows and Materials information to perform simulation tasks.

## Relationship

The flowchart diagram below visualizes the general relationship between the above-mentioned entity types. Here, the Properties associated to each entity are labeled with "P". Those properties which are computed as output of a Job (the so-called [Characteristic Properties](../properties/classification/general.md)), shown in black, have a certain numerical [precision](../methods/data.md) attributed to them.

![Simulation Diagram](/images/simulation-job-wokflow-unit-explained.png "Simulation Diagram")

## Main Entities

The three above-mentioned concepts of Workflows, Materials and Jobs can be grouped together under the same general umbrella term of **[Entities](../entities-general/overview.md)**, due to the many features and user interface components that they share in common. We review the similarities under [Entities and Common Aspects](../entities-general/overview.md) and then explain the details unique to each Entity type separately. 

For example, Jobs have **[Accounting](../accounts/overview.md)** set up for. Workflows consist of **[Subworkflows](../workflows/data/subworkflows.md)**, and further of the combination of individual **[Units](../workflows/data/units.md)**. Workflows and Materials are both **["Bankable" Entities](../entities-general/bank.md)**. 

## Other Items

Such simulations can be performed with any of the available **[modeling Applications](../software/applications.md)**, implementing the supported **[theoretical Models](../models/overview.md)** and corresponding **[computational Methods](../methods/overview.md)**.

## Computational Infrastructure

Our platform, moreover, is designed to store and organize the **[simulation Data](../data/classification.md)** in centralized databases, under the conventions of **[Structured Representation](../data-structured/schemas.md)**. A system of **[Queues](../infrastructure/resource/queues.md)** is in place for scheduling and tracking the allocation of **[computational Resources](../infrastructure/resource/overview.md)**, offered by the **[Clusters](../infrastructure/clusters/overview.md)** at the heart of our overall **[Infrastructure](../infrastructure/overview.md)**.
