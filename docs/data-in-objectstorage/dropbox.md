# Dropbox

Dropbox is a general-utility cloud-based data **storage system** that is **mounted on all nodes** of our computational [infrastructure](../infrastructure/overview.md), and is accessible everywhere under the same filesystem path. It can therefore be used to conveniently **share** [files](files.md) everywhere across the platform, as it is often necessary when dealing with the auxiliary files required for the simulations (for example, [pseudopotentials](../methods-directory/pseudopotential/overview.md)).

!!!warning "Warning: limited capacity"
    Dropbox is meant for non-bulky data and has a storage capacity administratively limited to **1 Gb** per [user](../accounts/users.md).

## Implementation

Dropbox is implemented through the [Object Storage](overview.md), and effectively connects the unstructured [Data on Disk](../data-on-disk/overview.md) with the rest of the infrastructure, including the Web Interface.

## User Interface

Interface, its file contents can be inspected from within its [dedicated page](ui/dropbox-page.md).

## Accessible From 

In the table below, we list the parts of our [infrastructure](../infrastructure/overview.md) where Dropbox is accessible from. Under the Web 

| Dropbox is Accessible From |
|------------|
| [Web Interface](../ui/overview.md) |
| [Remote Desktop](../remote-connection/remote-desktop.md) |
| [Command Line Interface](../cli/overview.md) |
| [Data on Disks](../data-on-disk/overview.md) |

## Notes

??? quote "Dropbox Term"
    The usage of the "Dropbox" term is purely for the purpose of assisting our readers with the concept of universally available storage and has no implication of the usage of products or services of the Dropbox file sharing service.
