# Important Directories under Cluster Homes

The following directories are present under the home folder of each cluster (referred to as "Cluster Home").

```bash
.
├── data
├── dropbox              => /dropbox/gmogni
├── exabyte-io           => /cluster-001-share/groups/exabyte-io
└── job_script_templates => /export/compute/job_script_templates
```

Each important folder is introduced in what follows, complementing the [general discussion](../../data-on-disk/directories.md) on the directory structure within our platform.

## Naming

The home directories on each cluster are mapped under the main [Login Home](../login/directories.md) and serve as "gateways" to the data in each cluster. They can be accessed by [cluster alias](overview.md#cluster-aliases) with their absolute paths of the form `/<cluster-alias>-home/<username>/`, for example `/cluster-001-home/steven/`.  These directories contain the hierarchical structure outlined in the remainder of the present page, and are affected by the storage quotas described [here](../../data-on-disk/quotas.md).

!!! warning "Simulations must be executed after navigating to one of the clusters folders only"
    Any [simulation jobs](../../jobs/overview.md) must be executed within the clusters (ie. inside cluster home directories) so that the tasks are sent to the corresponding cluster by our [resource management system](../resource/overview.md) and the associated data is stored therein as well. We explain the procedure for doing so via the [Command Line Interface](../../cli/overview.md) in [this section](../../jobs-cli/overview.md) of the documentation.

## Example

In the image below, we highlight two examples of cluster home directories present under the login home, as viewed in a [remote desktop environment](../../remote-connection/remote-desktop.md). The two clusters available in this case are referenced under the aliases "cluster-001" and "cluster-007". 

![Cluster Homes](/images/infrastructure/cluster-homes.png "Cluster Homes")

Example contents of the home directory for cluster-001 are displayed in the subsequent image below. We explain the naming convention and the contents of each of the directories in more detail in what follows. 

![Cluster Home Contents](/images/infrastructure/cluster-home-content.png "Cluster Home Contents")

The "dropbox" and "job_script_templates" folders are present under both Cluster Home and [Login Home](../login/directories.md) and are explained in more detail [in this page](../../data-on-disk/directories.md).
    
## Shared Folders for Organizations

Simulations data for [Organizations](../../collaboration/organizations/overview.md) (collaborative [accounts](../../accounts/overview.md)) is stored in a dedicated **shared folder** accessible by its **members only**. This shared folder bears the same name as the Organization itself: for example, "exabyte-io" in the visual above.  Simulation files present under this data are organized according to the Project/Job based directory naming explained below.

Each organization of which the user is member has its own corresponding shared directory. For example, organization `exabyte-io` has its folder under the path `/share/groups/exabyte-io/`.

## Temporary Data
 
Personal Accounts can also share data between them, without necessarily belonging to an Organization, via the **temporary folder** located under the path `/tmp`.

!!!warning "Warning: temporary data storage is not permanent"
    The data in this temporary folder is not guaranteed to be saved for a long time - use with caution or consider upgrading to an Organizational account.

## Personal Account "Data" Folder

The "data" folder present under each cluster home directory contains the **private files** on the cluster accessible to the user only, and generated with his/her [personal account](../../accounts/overview.md). Simulation files present under this data are organized according to the Project/Job based directory naming explained below.

The absolute path of the data folder for a cluster under the alias "cluster-001" is located at the path location `/cluster-001-home/<username>/data`.

## Project/Job based directory naming

Simulation files created through the [Web Interface](../../ui/overview.md) are automatically organized based on the [Project](../../jobs/projects.md) and constituent [Jobs](../../jobs/overview.md) that they are associated with. The subfolders are named according to the [project slug](../../jobs/projects.md#slug) and the job [slug](../../entities-general/data.md#slug), as well as its [ID](../../entities-general/data.md#top-level-keywords). 

This is demonstrated below for an example user with username "steven", project named "Default", and a job named "New Job Nov 11, 2018-20-59 pm", with id "575z5FgGQvtRMBnXg".

```bash
steven-default/new-job-nov-11-2018-20-59-pm-575z5FgGQvtRMBnXg
```
