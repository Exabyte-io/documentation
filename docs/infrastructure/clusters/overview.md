# Clusters

We offer a set of **high-performance computing clusters** for performing material modeling simulations in a **massively parallel** fashion. These clusters are part of the computing cloud infrastructures offered by various providers, which are referenced towards the end of the present page.

Clusters also offer a certain amount of **storage space** for [storing](../storage.md) simulation files as [unstructured data](../../data-on-disk/overview.md), subject to certain **quotas** as explained [here](../../data-on-disk/quotas.md).

The clusters offered as part of the [infrastructure of our platform](../overview.md) have been subject to an extensive set of **tests and benchmarks**, in order to measure their reliability and performance for different [hardware types](hardware.md) and for the [simulation engines](../../software/applications.md) used. They are reviewed and assessed in a [separate section](../../benchmarks/overview.md) of the documentation.

## Architecture Diagram

The architecture of a cluster is explained in the diagram below, comprising both a set of **distributed compute nodes** and a **distributed storage system**. Each cluster offered in our infrastructure can be accessed via its corresponding **Master Node**, with the network communication between nodes occurring via the **SSH protocol** implemented over a **Network File System (NFS)**. The allocation of these computational resources is handled by the **Resource Manager**, which is the object of a [separate discussion](../resource/overview.md).

![Cluster](/images/Cluster.png "Cluster")

!!!warning "Mandatory transit via Login Node"
    It is strongly recommended that the user first connects to the [login node](../login/overview.md) in order to access the cluster resources, via any of the available [connection methods](../../remote-connection/overview.md). Clusters are **not** supposed to be accessed directly. We can exceptionally concede the ability to connect directly to the cluster master node(s) for advanced users, but a special permission needs to be [requested](../../ui/support.md) first.

## Directory Structure 

We discuss the directory structure which can be found inside the home folder of each cluster [in this section](directories.md) of the documentation.

## Cloud Providers 

We rely on different **Cloud Providers** for delivering the computational resources that we offer. The current choice consists in either [Azure](azure.md) and [Amazon Web Service](aws.md) Cloud computing services.

!!!info "Private clusters for enterprise"
    Accounts equipped with the "Enterprise" [service level](../../pricing/service-levels.md) may [request](../../ui/support.md) a private cluster from us.
