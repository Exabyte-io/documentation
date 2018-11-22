# Data on Disk

The **unstructured data** generated on our platform consists primarily in the input and output files of simulations. This data is **stored** on **[hard drive disks](../infrastructure/storage.md)**, which are connected to the [computing clusters](../infrastructure/clusters/overview.md) at the heart of the general [infrastructure](../infrastructure/overview.md). 

We introduce below the key concepts associated with the disk storage of such unstructured data.

## Directory Structure

We review our approach towards distributing the storage of simulation data in a well-organized hierarchic fashion, referred to as the **directory structure**, in [this section](directories.md) of the documentation.

## Storage Quota

Different **storage quotas** are attributed to every storage space present across our infrastructure, limiting the amount (size) of the data that may be contained in them at any moment. They are explained in detail [here](quotas.md), for each case. 

## Security

Security policies affecting the storage of simulation files on the hard drives of our infrastructure are the object of a [dedicated discussion](security.md).
