# Storage Quota
    
We apply **storage quotas** to both the [directories](directories.md) on clusters. This limits the amount of storage space that can be consumed by [accounts](../accounts/overview.md), in order to avoid any problems. The concept of quota in the general context of account management is reviewed [here](../accounts/quota.md). This is an administrative limitation and can be easily extended as explained [here](../accounts/accounting/increase-quota.md)

## Conventions

The quotas are set per [cluster](../infrastructure/clusters) and are always **hard-set** (as opposed to soft quotas) [^1]. Once the quota limit is attained on a certain [cluster](../infrastructure/clusters), the user will be prevented from saving and storing any additional data on it.

!!! note "Service levels contain *compound* quotas"
    The explanation of the service levels [in this page](../pricing/service-levels.md) contains compound values for the disk quota for all accessible clusters. Depending on user demands we can allocate more or less quota per cluster.

Current quotas applicable to the folders available to the user can be inspected at any time via the [Command Line Interface](../cli/overview.md), using the [`quota` command](../jobs-cli/accounting/check-quotas.md), or alternatively using the [Web Interface](../accounts/accounting/check-balance-quota.md).
    
## Login Node Home

The quota under the [login home folder](directories.md#login-home) amounts to **10 Gb**. This limited quota can be used to store and test source code or scripts. 

## Cluster Home directory

The quota under the [home folders of the available clusters](directories.md#cluster-home) depends on the [service level](../accounts/service-levels.md) associated with the account under consideration. For example, the "Promo", "Advanced" and "Pro" service levels have the storage quotas indicated [here](../pricing/service-levels.md).

## Shared Folders for Organizations

The quota under the [shared folder](directories.md#shared-folders-for-organizations) available for [Organizations](../collaboration/organizations/overview.md) again depends on the [service level](../accounts/service-levels.md) associated with the corresponding Organizational account. For the "Enterprise" and "Enterprise-Extra" service levels the storage quota is set to the values indicated [here](../pricing/service-levels.md).

## Dropbox Folder

In order to facilitate the accessibility of the [Dropbox directory](../data-in-objectstorage/dropbox.md) on each of the components of our distributed compute system, we limit it in size to **1 Gb**. It is designed to be used for input files (for example pseudopotentials), scripts and other **non-bulky data** used during multiple calculations.

## Links

[^1] [Disk Quota, Wikipedia](https://en.wikipedia.org/wiki/Disk_quota)
