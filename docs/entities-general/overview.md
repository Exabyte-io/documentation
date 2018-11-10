# Types of Entities

Our platform contains three main classes of **Entities**, each recognizable by its unique icon, as illustrated below:

| Entity    |  Icon      | Details        | 
| :-------- |:----------- |:------------- |
| [Materials](/materials/overview.md) | <i class="zmdi zmdi-widgets"></i>    | Hold information about individual materials |
| [Workflows](/workflows/overview.md) | <i class="zmdi zmdi-dot-circle"></i> | Contain logical set of computational operations, applicable to multiple materials |
| [Jobs](/jobs/overview.md)           | <i class="zmdi zmdi-file"></i>       | Represent computational tasks on a particular material-workflow combination to produce the corresponding properties and output files as results |

# Ownership and Permissions

Each entity has an [Owner](ownership.md) and a set of [permissions](permissions.md) in relation to how they can be accessed, manipulated or modified by users. Permissions are relevant in the context of [Entity Sharing](/collaboration/sharing/ui.md) and [Organizational Accounts](/collaboration/organizations/overview.md). 

# Common User Interface Components

There are interface components, and some of their respective sub-components, which are [common to all entity types](ui/overview.md). 

# Data

Entities are stored in a database in the form of **structured data**. Entities can also have **metadata** attached to them, in the form of descriptive tags for example. These concepts are elucidated in the following [dedicated page](data.md).

# Sets

Some Entities can be grouped together under folders, or "Sets", as explained [here](sets.md).

# Bank

Unique Entities are collected inside the Entity Banks by type. Please refer to [this page](bank.md) for an introduction to the "Bank" concept.

# Common Actions

Finally, [this page](/entities-general/actions/overview.md) introduces actions pertinent to all entity types.
