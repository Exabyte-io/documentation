# Data Lifecycle

We now explain the general evolution of data. This evolution spans the duration of events from the moment the data is sent to the computing resources for the execution of simulation tasks, to the moment it is stored as [objects](../data-in-objectstorage/overview.md) or [structured data](../data-structured/overview.md) in the [database](../data-structured/overview.md#database) to be read by the Web Interface. We refer to this evolution flow as the **Data Lifecycle**.

## Flowchart

In the image below, we present a flowchart summarizing the steps involved in the data lifecycle. 

![Data Lifecycle](/images/data-lifecycle.png "Data Lifecycle")

The Data Lifecycle is composed primarily of the following three steps. The reader is referred to the same number labelling cited in the above image.

## 1. Entity Structured Data Creation

The [actions](../entities-general/actions/overview.md) performed by the user in the Web Interface lead to the creation of entity-related [structured data](../data-structured/overview.md) in the corresponding [account-owned collections](../accounts/collections.md), stored within the database. [Jobs](../jobs/overview.md) corresponding to the simulation tasks provide one such example.
                
## 2. Execution of Simulation

The structured data describing such Entities is then sent from the database to the [computing clusters](../infrastructure/clusters/overview.md), the core component of the overall [computational infrastructure](../infrastructure/overview.md). Here, the relevant simulations are executed, which creates non-structured data in the form of output files.
                
## 3. Data Retrieval                
                
Following simulation completion, the output data produced by the simulation engine is stored on disk as [unstructured files](../data-on-disk/overview.md). 

### 3a. Extraction of Properties as Structured Data

The [properties](../properties/overview.md) (and/or other information) contained in the output data are subsequently [extracted](../properties/lifecycle/extractor.md) through the processing of simulation output. 

This information is further stored as [structured data](../data-structured/overview.md) in the database, and can be [retrieved](../properties/lifecycle/retrieval.md), for example, from the Web Interface as part of the [account-owned collections](../accounts/collections.md) of entities.

### 3b. Storage of Output Files as Objects

All simulation output files are additionally stored in the [Object storage](../data-in-objectstorage/overview.md), in order to make them accessible to the Web Interface. This can be accomplished under the [Files Tab](../jobs/ui/files-tab.md) of [Job Viewer](../jobs/ui/viewer.md), for example.
