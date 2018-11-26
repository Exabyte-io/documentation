# Introduction to Infrastructure

Our platform represents a comprehensive **distributed web application**. This section explains the most important components of its **computational infrastructure**.

We additionally support platform-level access via [advanced connection methods](../remote-connection/overview.md), as an alternative to the main Web Interface, which also offer the ability to submit [simulation jobs](../jobs-cli/overview.md) to the [computing clusters](clusters/overview.md). These advanced features are intended for expert users.

## Architecture diagram 

The different components forming the underlying architecture of our computational infrastructure are interconnected as demonstrated in the following diagram. The reader is referred to the number labels included here to find the component's corresponding introductory explanation in the remainder of this documentation page.

![Infrastructure](/images/Infrastructure.png "Infrastructure")

## 1. Web Interface

The Web Interface of our platform is introduced separately from the rest of the computational infrastructure, [in this page](../ui/overview.md).

## 2. Remote Desktop

A remote desktop environment is offered for connecting to the platform and accessing the relevant data stored in its different nodes. This is explained in detail [here](../remote-connection/remote-desktop.md).

## 3. Rest API

We explain the Rest API access method [in this section](../rest-api/overview.md) of the documentation.

## 4. Dropbox

Dropbox is a central sharing storage space accessible from all nodes of the platform. It is reviewed in its [dedicated page](../data-in-objectstorage/dropbox.md).

## 5. Login Node

The Login Node provides the main access gateway to the rest of the computational infrastructure, and is the object of a [separate discussion](login/overview.md).

## 6. Web Terminal

Alternatively to the aforementioned Remote Desktop connection method, the platform can also be accessed via the Command Line Interface described [here](../cli/overview.md). We provide a [Web Terminal](../remote-connection/web-terminal.md) utility for logging in via Command Line directly from the Web Interface.

## 7. SSH

The [Command Line Interface](../cli/overview.md) can also be accessed via an external SSH client instead of the Web Terminal. [This page](../remote-connection/ssh.md) outlines the instructions on how to do so.

## 8. Clusters

The computational power of our platform is distributed across different cloud-based computing clusters, which are described [in this section](clusters/overview.md) of the documentation. 

## 9. Storage System

The input and output data of simulations can be stored as [unstructured data](../data-on-disk/overview.md) on an appropriate storage system, as explained in its corresponding [documentation page](storage.md).

## 10. Resource Management

The computational resources offered on our platform are managed and allocated to the users by a task scheduler, operated under a system of queues, as documented [here](resource/overview.md).

## 11. Object Storage

The simulation files stored on the cluster hard drives can subsequently be stored as [objects](../data-in-objectstorage/overview.md) for their retrieval under the Web Interface. 

## 12. Master Node

The Master Node constitutes the main entry gateway to each available computing Cluster, and is documented in its respective [section of the documentation](clusters/directories.md).

## 13. Database

The Database contains the various account-owned [collections](../accounts/collections.md) of [entities](../entities-general/overview.md) and their respective [properties](../properties/overview.md), stored in the form of [structured data](../data-structured/overview.md).

## 14. Computational Resources

The various settings and parameters affecting the allocation of the computational resources offered on our infrastructure, at the moment of the launching of a [Job simulation](../jobs/overview.md), can be entered from the Web Interface according to the instructions contained [in this page](compute-settings/ui.md). 

The computational resources available as part of our services are themselves listed for each of the [Azure](clusters/azure.md) and [Amazon Web Service](clusters/aws.md) Cloud Providers.
