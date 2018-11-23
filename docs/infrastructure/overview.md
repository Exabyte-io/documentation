# Introduction to Infrastructure

Our platform represents a comprehensive **distributed web application**. This section explains the most important components of its **computational infrastructure**, as opposed to the Web Interface which is explained separately in [other parts of this documentation](../ui/overview.md).

For users who are experts in computational science, we support platform-level access with ability to submit [simulation jobs](../jobs-cli/overview.md) to [computing clusters](clusters/overview.md) via [alternative advanced connection methods](../remote-connection/overview.md). 

## Architecture diagram 

The different components forming the underlying architecture of our computational infrastructure are interconnected as demonstrated in the following flowchart diagram. The reader is referred to the number labels included here to be redirected to the component's corresponding documentation explanation in the subsequent headers of this page.

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

## 6. Command Line Interface

Alternatively to the aforementioned Remote Desktop connection method, the platform can also be accessed via the Command Line Interface described [here](../cli/overview.md). We provide a [Web Terminal](../remote-connection/web-terminal.md) utility for logging in via Command Line directly from the Web Interface.

## 7. Clusters

The computational power of our platform is distributed across different cloud-based computing clusters, which are described [in this section](clusters/overview.md) of the documentation. 

## 8. Storage System

The input and output data of simulations can be stored as [unstructured data](../data-on-disk/overview.md) on an appropriate storage system, as explained in its corresponding [documentation page](storage.md).

## 9. Resource Management

The computational resources offered on our platform are managed and allocated to the users under a task scheduling system of queues, as documented [here](resource/overview.md).

## 10. Files

The simulation files stored on the cluster hard drives can subsequently be stored as [objects](../data-in-objectstorage/overview.md) for their retrieval under the Web Interface. 

## Compute Settings

The various settings and parameters affecting the allocation of the computational resources offered on our infrastructure at the moment of the launching of a [Job simulation](../jobs/overview.md) can be entered from the Web Interface according to the instructions contained [in this page](compute-settings/ui.md).
