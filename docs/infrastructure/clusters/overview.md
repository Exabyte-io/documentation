# Clusters

We offer a set of **high-performance computing clusters** to facilitate materials modeling with high throughput and high fidelity. Our infrastructure contains multiple clusters at any point in time, deployed at multiple cloud providers as referenced at the end of the present page. The modular character of our system allows for the on-premises and hybrid cloud deployments, as well as a managed cloud scenario.

## Architecture Diagram

The architecture of a cluster is explained in the diagram below, comprising a **Master Node**, a set of **Compute Nodes** a **Storage System**. The allocation of these computational resources is handled by the **Resource Manager**, which is the object of a [separate discussion](../resource/overview.md).

![Cluster](/images/Cluster.png "Cluster")

## Storage

Clusters also offer a certain amount of **storage space** for [storing](../storage.md) simulation files as [unstructured data](../../data-on-disk/overview.md), subject to certain **quotas** as explained [here](../../data-on-disk/quotas.md).

### Directory Structure 

We discuss the directory structure which can be found inside the home folder of each cluster [in this section](directories.md) of the documentation.

## Performance Benchmarks

The clusters offered as part of the [infrastructure of our platform](../overview.md) have been subject to an extensive set of **tests and benchmarks**, in order to measure their reliability and performance for different [hardware types](hardware.md) and for the [simulation engines](../../software/applications.md) used. They are reviewed and assessed in a [separate section](../../benchmarks/overview.md) of the present documentation.

### Cloud Providers 

We rely on multiple cloud providers for delivering the computational resources that we offer. The current choice consists in either [Azure](azure.md) and [Amazon Web Services](aws.md) .
