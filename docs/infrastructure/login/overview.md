# Login Node

When the user first logs in into our platform using either the remote desktop or terminals (introduced below), he/she will be directed first to his/her **home folder** under the **Login Node**, instead of accessing the clusters directly. The Login node therefore constitutes the intermediary access point to the [clusters](../clusters/overview.md), and is organized according to the directory structure introduced below.

!!!warning "Mandatory transit via Login Node"
    It is strongly recommended that the user first connects to the login node in order to access the cluster resources. Clusters are **not** supposed to be accessed directly. We can exceptionally concede the ability to connect directly to the cluster master node(s) for advanced users, but a special permission needs to be [requested](../../ui/support.md).
    
## Connection Options

We introduce the different options for connecting to the Login Node in [this part of the documentation](connections.md).

## Directory Structure

The directory structure which is encountered under the home folder of the Login Node (referred to as the **Login Home**) is explained in detail [here](directories.md).
