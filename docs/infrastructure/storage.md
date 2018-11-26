# Storage System

We allow for the storage of simulation data on **hard drives** connected to the [computational clusters](clusters/overview.md) of our infrastructure. The storage of simulation files on disks, in the form of **unstructured data**, is explained [in this section](../data-on-disk/overview.md) of the documentation.

## Storage Diagram

A representative example of an overall storage system, such as implemented on our infrastructure, is explained visually in the flowchart below. This example includes multiple clusters connected to the same central [Login Node](login/overview.md), each one with its own corresponding [access master node](clusters/directories.md) and associated storage space. Here, we also show how the Cluster Home shortcuts present under the Login Home are linked to their absolute paths, based on the common color labelling.

![Storage System](/images/Storage-System.png "Storage System")

## Storage Quotas

These storage spaces are subject to certain **quotas**, limiting the size of the data that may be saved in them. These quotas are documented [here](../data-on-disk/quotas.md).
