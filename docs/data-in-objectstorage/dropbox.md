# Dropbox

Dropbox is a general-utility cloud-based data **storage system** that is **mounted on all nodes** of our computational [infrastructure](../infrastructure/overview.md), and is accessible everywhere under the same filesystem path. It can therefore be used to conveniently **share** [files](files.md) everywhere across the platform, as it is often necessary when dealing with the auxiliary files required for the simulations (for example, [pseudopotentials](../methods/pseudopotential/overview.md)).

Dropbox is implemented through the [Object Storage](files.md#object-storage-of-files), and effectively connects the unstructured [Data on Disk](../data-on-disk/overview.md) with the rest of the infrastructure, including the Web Interface.

!!!warning "Warning: limited capacity"
    Dropbox is meant for non-bulky data and has a storage capacity administratively limited to **1 Gb** per [user](../accounts/users.md).
        
## List of Nodes with Dropbox Mounted 

In the table below, we provide a list of the nodes where the central Dropbox is mounted and therefore accessible. Under the Web Interface, its file contents can be inspected from within its [dedicated page](ui/dropbox-page.md).

<center>

| Nodes with Dropbox mounted |
|------------|
| [Web Interface](../ui/overview.md) |
| [Remote Desktop](../remote-connection/remote-desktop.md) |
| [Command Line Interface](../cli/overview.md) |
| [Data on Disks](../data-on-disk) |

<center>
