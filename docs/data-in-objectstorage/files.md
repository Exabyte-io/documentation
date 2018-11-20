# Files

We organize our [simulation data](../data/overview.md) under **files** in order to interact with the [simulation engine](../software/applications.md), both for **inputting** parameters defining the nature of the simulation, and for [retrieving](../properties/lifecycle/retrieval.md) the **output** of the calculation upon its completion.

## Directory Structure

Files are distributed under a **Directory Structure**, otherwise known as **file system**, present within the [Storage Disk](../data-on-disk/directories.md) component of the computing [infrastructure](../infrastructure/storage.md). This affords for a better organization of the files under a well-defined **hierarchic structure**, for their easier navigation, retrieval and inspection via [remote connection methods](../remote-connection/overview.md).
            
## Object Storage of Files

If the Files need to be accessed from within the Web Interface instead of remote connection, then their **storage as Objects** becomes necessary. Object storage [^1] is a particular type of **storage architecture** that manages unstructured data as **Objects**, as opposed to other architectures such as the aforementioned hierarchical file systems. It the established way of accessing files from Web applications.
