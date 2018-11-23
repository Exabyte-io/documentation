# Storage Quota
    
We apply **storage quotas** to both the [home and shared folders](directories.md) on clusters. This limits the amount of storage space that can be consumed by the user or [Organization](../collaboration/organizations/overview.md), for the sake of keeping our infrastructure responsive and running smoothly at all times for all users of the platform. The concept of quota in the general context of account management is reviewed [here](../accounts/quota.md).

The quotas we offer are always **hard-set**, as opposed to soft quotas, in the sense that we don't allow for any temporary excesses of the pre-defined storage limits. Once the quota limit is attained on a certain computing node, the user will be prevented from saving and storing any additional data on it.

Current quotas applicable to the folders available to the user can be inspected at any time via the [Command Line Interface](../cli/overview.md), using the [`quota` command](../cli/actions/check-quotas.md), or alternatively using the [Web Interface](../accounts/accounting/check-balance-quota.md).
    
## Login Node Home

The quota under the [login home folder](directories.md#login-home) amounts to **10 Gb**. 

This small quota can be used for example to store and test some source code or scripts. We do also allow for Python packages to be run inside this folder.

## Cluster Home directory

The quota under the [home folders of the available clusters](directories.md#cluster-home) depends on the chosen [service level](../accounts/service-levels.md) for the account under consideration. 

For example, the "Promo", "Advanced" and "Pro" service levels have the storage quotas indicated [here](../pricing/service-levels.md) applied to them for storing data on the clusters.

## Shared Folder

The quota under the [shared folder](directories.md#organization-shared-folder) available for [Organizations](../collaboration/organizations/overview.md) again depends on the precise [service level](../accounts/service-levels.md) being implemented on the corresponding Organizational account. 

For the "Enterprise" and "Enterprise-Extra" service levels which afford for the creation of Organizations, the storage quota is set to the values indicated [here](../pricing/service-levels.md).

## Dropbox Folder

In order to facilitate the accessibility of the [Dropbox directory](../data-in-objectstorage/dropbox.md) on each of the components of our distributed compute system, we limit it in size to **1 Gb**. It is designed to be used for input files (for example pseudopotentials), scripts and other **non-bulky data** used during multiple calculations.
