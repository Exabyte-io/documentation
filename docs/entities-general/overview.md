# Types of Entities

The user interface of the platform contains three main classes of **Entities**, each recognizable by its unique symbol illustrated below:

| Entity    |  Icon      | Details        | 
| :-------- |:----------- |:------------- |
| Materials | <i class="zmdi zmdi-widgets"></i>    | Hold information about individual materials |
| Workflows | <i class="zmdi zmdi-dot-circle"></i> | Contain logical set of computational operations, applicable to multiple materials |
| Jobs      | <i class="zmdi zmdi-file"></i> | Represent computational tasks on a particular material-workflow combination to produce the corresponding properties and output files as results |


# Ownership and Permissions

Each entity has an [Owner](ownership.md). They are moreover subject to a set of [permissions](permissions.md) in relation to how they can be accessed, manipulated or modified by users. Permissions are relevant in the context of [Entity Sharing](/collaboration/sharing/ui.md) and [Organizational Accounts](/collaboration/organizations/overview.md). 

# Common User Interface Components

There are interface components, and some of their respective sub-components, which are [common to all entity types](ui/overview.md). 

# Data

Account-owned entity collections are stored in databases in the form of **structured data**.  Entities can also have **metadata**  attached to them, in the form of descriptive tags for example. These concepts are elucidated in the following [dedicated page](data.md).

# Sets

Jobs and Materials (but not Workflows) can be grouped together under folders, or "Sets", as explained [here](actions/sets.md).

# Bank

Please refer to [this page](bank.md) for an introduction to the "Bank" concept.

# Common Actions

Finally, [this page](/entities-general/actions/overview.md) introduces actions pertinent to all entity types.



