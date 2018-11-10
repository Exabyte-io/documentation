# Properties 

The present section of the documentation explains our approach to organizing, storing and interacting with the **properties** of the different [entities](/entities-general/overview.md) present across our platform, and primarily those pertaining to [Materials](/materials/overview.md).

# Definitions
 
In a broad sense we consider **[Material](/materials/overview.md)** to be the physical (chemical, biological) system(s) under investigation, and **[Workflow](/workflows/overview.md)** to be the process of probing (measuring, modeling/simulating) such system. 

We further define **"Properties"** as any physical quantity which can be **extracted** from the output of a simulation [Job](/jobs/overview.md) operated on a Material. Following extraction, properties can subsequently be **refined** for a better categorization in databases, and for a better understanding of their physical meaning.

Exact set of properties that have to be supplied to, and can be extracted as a result of, a [Workflow](/workflows/overview.md) computation, can vary depending on the Workflow type and on the [models](/models/overview.md)/[methods](/methods/overview.md) included therein.

# List of Properties

We have listed the properties available for computation on our platform [in this page](list.md).

# Classification

We explain how properties can be classified into different categories [here](classification.md).

# Extractors

Properties are extracted from the output of the Workflow simulations and presented to the user following the procedures and conventions outlined in [this section](extractor.md).

# Refinement

The raw extracted properties are subsequently further refined and categorized based on their physical meaning and on their overall numerical precision. We explain how this refinement procedure is enacted [here](refinement.md). 

# Data

For examples of JSON representation of materials and structure-based descriptors, see the [Materials Data section](/materials/data.md).

# Schemas And Examples

We employ the **Exabyte Data Convention (EDC)** in order to organize and process data. A link to its dedicated documentation is provided under [this page](/data-structured/schemas.md).

# User Interface

Properties are presented in special panels within the user interface of the [Job Viewer](/jobs/ui/viewer.md). One of such panels contains the **final computed structure**, displayed under an instance of [Materials Viewer](/materials/ui/viewer.md). It is described separately [here](ui/viewer.md).

These properties can also be reviewed under a dedicated [Explorer-type interface](/entities-general/ui/explorer.md) for each Material stored in the account-owned [collection](/accounts/collections.md). We explain how to retrieve and inspect the contents of this Properties Explorer [in this page](ui/explorer.md). 
