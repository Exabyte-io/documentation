# Important Directories under Cluster Homes

The following directories are present under the home folder of each cluster (the so-called **Cluster Home**), accessible within the [Login Node](../login/directories.md) under the symlink `/home/<username>/<cluster-alias>` (pointing to the absolute path `/<cluster-alias>-home/<username>`). 

```
.
├── data
├── dropbox              => /dropbox/gmogni
├── exabyte-io           => /cluster-001-share/groups/exabyte-io
└── job_script_templates => /export/compute/job_script_templates
```

Each listed folder is introduced in what follows, complementing the [general discussion](../../data-on-disk/directories.md) on the directory structure within our platform.

## Shared Folders for Organizations

For members of an [Organization](../../collaboration/organizations/overview.md) (collaborative [account](../../accounts/overview.md)), a corresponding folder with the same name as the name of the organizational account ("exabyte.io" in the above example) is present under each cluster home directory, allowing for data to be **shared** between the organization members. Simulation files present under this data are organized according to the Project/Job based directory naming explained below.
 
Each organization of which the user is member has its own corresponding shared directory. For example, organization `exabyte-io` has its folder under the path `/share/groups/exabyte-io/`.

The storage quotas which pertain to these shared folders are explained in the corresponding [documentation page](../../data-on-disk/quotas.md).

## Personal Account "Data" Folder

The "data" folder present under each cluster home directory contains the **private files** on the cluster accessible to the user only, and generated with their [personal account](../../accounts/overview.md). Simulation files present under this data are organized according to the Project/Job based directory naming explained below.

The absolute path of the data folder for a cluster under the alias "cluster-001" is located at the path location `/cluster-001-home/<username>/data`.

## Project/Job based directory naming

Simulation files created through the [Web Interface](../../ui/overview.md) are automatically organized based on the [Project](../../jobs/projects.md) and constituent [Jobs](../../jobs/overview.md) that they are associated with. The subfolders are named according to the [project slug](../../jobs/projects.md#slug) and the job [slug](../../entities-general/data.md#slug) as well as its [ID](../../entities-general/data.md#top-level-keywords) as demonstrated below for user with username "steven", project named "Default", job named "New Job Nov 11, 2018-20-59 pm" with id "575z5FgGQvtRMBnXg".

```bash
steven-default/new-job-nov-11-2018-20-59-pm-575z5FgGQvtRMBnXg
```

## Dropbox

Dropbox is a convenient way of sharing and transferring files across all nodes of the infrastructure. This functionality is narrated in detail in its own [dedicated page](../../data-in-objectstorage/dropbox.md).

## Jobscript Templates

The Login Home also contains a folder with [Job script](../../jobs-cli/batch-script.md) template examples, necessary for [submitting jobs via the Command Line Interface](../../jobs-cli/overview.md). 
 
## Temporary Data
 
Personal Accounts can also share data between them, without necessarily belonging to an Organization, via the **temporary folder** located under the path `/tmp`.

!!!warning "Warning: temporary data storage is not permanent"
    The data in this temporary folder is not guaranteed to be saved for a long time - use with caution or consider upgrading to an Organizational account.
