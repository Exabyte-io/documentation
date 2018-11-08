# Properties 

The present section of the documentation explains our approach to organizing, storing and interacting with the **properties** of the different [entities](/entities-general/overview.md) present across our platform, and primarily those pertaining to [Materials](/materials/overview.md). We define "Materials properties" as any physical quantity which can be **extracted** from the output of a simulation [Job](/jobs/overview.md) executed on the relevant [Material](/materials/overview.md), and that can be subsequently **refined** for a better categorization in databases and for a better understanding of its physical meaning.

Exact set of Materials properties that have to be supplied to, and can be extracted as a result of, a [Workflow](/workflows/overview.md) computation, can vary depending on the Workflow type and on the [models](/models/overview.md)/[methods](/methods/overview.md) included therein.

# List of Properties

We have listed the materials properties available for computation on our platform [in this page](list.md).

# Properties Classification

We explain how materials properties can be classified into different categories [here](classification.md).

# Extractors

Properties are extracted from the output of the Workflow simulations and presented to the user following the procedures and conventions outlined in [this section](extractor.md).

# Refinement

The raw extracted properties are subsequently further refined and categorized based on their physical meaning and on their overall numerical precision. We explain how this refinement procedure is enacted [here](refinement.md). 

# Schemas And Examples

An entry gateway to the documentation dedicated to the Exabyte Materials Data Convention is provided under [this page](/data-structured/schemas.md).

# User Interface

Materials properties are presented in special panels within the user interface of the [Job Viewer](/jobs/ui/viewer.md). One of such panels contains the **final computed structure**, displayed under an instance of [Materials Viewer](/materials/ui/viewer.md). It is described separately [here](ui/viewer.md).

Materials properties can also be reviewed under a dedicated [Explorer-type interface](/entities-general/ui/explorer.md) for each Material stored in the account-owned [collection](/accounts/collections.md). We explain how to retrieve and inspect the contents of this Properties Explorer [in this page](ui/explorer.md). 
