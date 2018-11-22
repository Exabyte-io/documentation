# Directory Structure

We organize the unstructured data corresponding to simulation files under a certain hierarchic **directory structure**, as explained during the course of the present page.
     
## Permissions

We organize our directories under a Linux filesystem [^1], where standard permissions apply [^2].
    
## Login Home

When the user first accesses our platform via any of the available [remote connection methods](../remote-connection/overview.md), he/she will initially enter the [login node](../infrastructure/login/overview.md). The **home directory** under this login node (referred to as the **Login Home**) is at the head of a hierarchic directory structure which is described [in this section](../infrastructure/login/directories.md) of the documentation. 

Each user has its own login home directory on our filesystem under: `/home/<username>/`, such that `steven` has `/home/steven/` as a home directory. The quota limit for data storage under this login home directory is described [here](quotas.md).

The location of the login home folder under the main [remote desktop environment](../remote-connection/remote-desktop.md) is encircled in red in the following illustration. 

![Login Home](/images/login-home.png "Login Home")

## Cluster Home

The home directories of each available [cluster](../infrastructure/clusters/overview.md) are mapped under the aforementioned login home, and can be accessed under the **cluster alias name**. Their absolute paths are of the form `/<cluster-alias>-home/<username>/`.

Starting from these cluster homes, the user can run any [simulation Jobs](../jobs/overview.md). We explain the procedure for doing so via the [Command Line Interface](../cli/overview.md) in [this section](../jobs-cli/overview.md) of the documentation.

These directories contain the hierarchic structure outlined [in the following page](../infrastructure/clusters/directories.md), and are affected by the storage quotas described [here](quotas.md).

In the following image, we highlight two examples of cluster home directories present under the login home, as viewed in a [remote desktop environment](../remote-connection/remote-desktop.md). The two clusters available in this case are referenced under the aliases "cluster-001" and "cluster-007". The contents of cluster-001 are displayed in the subsequent image. In this latter image, the exabyte.io folder refers to the shared folder of an [Organization](../collaboration/organizations/overview.md), as documented later in this page.

![Cluster Homes](/images/cluster-homes.png "Cluster Homes")

![Cluster Homes](/images/cluster-home-content.png "Cluster Homes")

## Dropbox

As we explain [in this page](../data-in-objectstorage/dropbox.md), Dropbox is a folder mounted on all nodes, allowing data and files to be shared across the platform. It is subject to the storage quota described [in this page](quotas.md).

The absolute path to the Dropbox folder is `/dropbox/<username>/`. A link to it is present under the Login Home, and under the home directories for each cluster.

## Job Script Templates

A shortcut to a folder called "Job Script Templates" is also present under both the login and cluster home directories. It contains examples of [Jobscripts](../jobs-cli/batch-script.md) for running [Jobs via the Command Line Interface](../jobs-cli/overview.md).
 
This folder is stored centrally on our platform, under the path `/export/compute/job_script_templates`.
    
## Organization Shared Folder

If the user is member of an [Organization](../collaboration/organizations/overview.md) collaborative account, a corresponding folder with the same name as the Organization account will be present under each cluster home directory, containing simulation files that can be **shared** between all Organization members.
 
Each organization of which the user is member has its own corresponding shared directory. For example, organization `exabyte` would have its folder under the path `/share/groups/exabyte/`. The files contained in each organizational folder are then subdivided based on the [Project](../jobs/projects.md) and constituent [Job](../jobs/overview.md) that they are associated with.

The storage quotas which pertain to these shared folders are explained in the corresponding [documentation page](quotas.md).

## Data Folder For Personal Account

The "data" folder present under each cluster home directory contains all the **private files** on the cluster accessible to the user only, and generated with his own personal account. The simulation files present under this data folder are categorized according to the [Project](../jobs/projects.md) and [Job](../jobs/overview.md) subfolders to which they belong.

For example, the data folder for a cluster under the alias "cluster-001" would be located at the path location `/cluster-001-home/<username>/data`.

## Links

[^1]: [Wikipedia Linux Filesystem Hierarchy Standard, Website](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)

[^2]: [Wikipedia Linux File system permissions](https://en.wikipedia.org/wiki/File_system_permissions)
