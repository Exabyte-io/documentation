# Files

Simulations [data](../data/overview.md) is naturally organized in Files in order to interact and exchange information with the [simulation engines](../software/components.md). These could be **input** parameters defining the nature of the simulation, and the **output** of the calculation upon its completion. 

## Files in the Web Interface

When the Files need to be accessed from within the [Web Interface](../ui/overview.md), however, it becomes necessary to store them in the Object Storage as mentioned [here](overview.md). The latter then becomes an intermediary to allow accessing the information produced during the simulation time from the web. We further discuss the policies implemented in order to facilitate the security of this approach [here](security.md). 

We introduce the actions related to the Files in the Web Interface in [this page](actions/overview.md). 
            
## Directory Structure

Files are distributed under a **Directory Structure** present within the [Storage Disk](../data-on-disk/directories.md) of the computing [infrastructure](../infrastructure/storage.md). 

This affords for the organization of files under a well-defined **hierarchic structure**, for their easier navigation, retrieval and inspection via [remote connection methods](../remote-connection/overview.md) for example.
