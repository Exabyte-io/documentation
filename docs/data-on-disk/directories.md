# Directory Structure

We organize the [unstructured](../data/classification.md#by-internal-organization) data corresponding to simulation files under a certain hierarchic directory structure, as explained in the present page.
     
## Permissions

We organize our directories under a Linux/Unix filesystem [^1], where standard permissions apply [^2]. We refer the Reader to the original sources of explanation about the Unix permissions. 

We associate [Users](../accounts/users.md) with operating system users and [Accounts](../accounts/overview.md) with operating system groups. This way the data generated within an account is not accessible to anyone else, but the members of this account, unless explicitly shared. Shared access for the members of the same organizational account is explained further [below](#shared-folders-for-organizations).
    
## Login Home

When first accessing the platform via any of the [remote connection methods](../remote-connection/overview.md), users initially enter the [login node](../infrastructure/login/overview.md). The home directory where a user lands upon login is referred to as the **Login Home**. This directory is at the head of a hierarchical directory structure further described [in this section](../infrastructure/login/directories.md) of the documentation. 

Each user has its own login home directory on our filesystem under: `/home/<username>/`, such that `steven` has `/home/steven/` as a home directory. The quota limit for data storage under this directory is described [here](quotas.md). Login node is meant for storing auxiliary data, such as source code, scripts, notes. Simulations should be executed and bulky data should be stored under Cluster Home(s) as explained below.

### Example

The location of the login home folder under the main [remote desktop environment](../remote-connection/remote-desktop.md) is encircled in red in the following illustration. 

![Login Home](/images/login-home.png "Login Home")

## Cluster Home

### Naming

Our [infrastructure](../infrastructure/overview.md) contains multiple [clusters](../infrastructure/clusters/overview.md). The home directories on each cluster are mapped under the aforementioned login home, and can be accessed under the **[cluster alias name](../infrastructure/clusters/overview.md#cluster-aliases)**. Their absolute paths are of the form `/<cluster-alias>-home/<username>/`, ie. `/cluster-001-home/steven/`, for example. Cluster home directories thus serve as "gateways" to the data in each sluster. These directories contain the hierarchical structure outlined [in the following page](../infrastructure/clusters/directories.md), and are affected by the storage quotas described [here](quotas.md).


!!! note "Simulations to be inside clusters only"
    Any [simulation jobs](../jobs/overview.md) must be executed within the clusters (ie. inside cluster home directories) and all bulk data must be stored therein as well. We explain the procedure for doing so via the [Command Line Interface](../cli/overview.md) in [this section](../jobs-cli/overview.md) of the documentation.

### Example

In the image below, we highlight two examples of cluster home directories present under the login home, as viewed in a [remote desktop environment](../remote-connection/remote-desktop.md). The two clusters available in this case are referenced under the aliases "cluster-001" and "cluster-007". 

![Cluster Homes](/images/cluster-homes.png "Cluster Homes")

Example contents of the home directory for cluster-001 are displayed in the subsequent image below. We explain the naming convention and the contents of each of the directories in more details below. 

![Cluster Home Contents](/images/cluster-home-content.png "Cluster Home Contents")

### Dropbox

As explained [in this page](../data-in-objectstorage/dropbox.md), Dropbox is a universally available storage, allowing data and files to be shared across the platform. It is subject to the storage quota described [in this page](quotas.md).

The absolute path to the Dropbox folder is `/dropbox/<username>/`. A link to it is present under the Login Home, and under the home directories for each cluster, as demonstrated in the visual above.

### Job Script Templates

A shortcut to a folder containing some quick examples (templates) for command-line jobs is also present under both the login and cluster home directories. It contains examples of [Jobscripts](../jobs-cli/batch-script.md) for running [Jobs via the Command Line Interface](../jobs-cli/overview.md).
 
This folder is stored under the absolute path `/export/compute/job_script_templates`.
    
### Shared Folders for Organizations

[Organization accounts](../collaboration/organizations/overview.md) have a **shared folder** at their disposal in order to share simulation data between all Organization members. This shared folder bears the same name as the Organization itself, for example "exabyte-io" in the visual above. More information concerning this folder can be found [in this page](../infrastructure/clusters/directories.md#shared-folders-for-organizations).

### Personal Account "Data" Folder

Each user has a personal **data folder** associated with his own **personal account**. It is described further [here](../infrastructure/clusters/directories.md#personal-account-"data"-folder).

## Links

[^1]: [Wikipedia Linux Filesystem Hierarchy Standard, Website](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)

[^2]: [Wikipedia Linux File system permissions](https://en.wikipedia.org/wiki/File_system_permissions)
