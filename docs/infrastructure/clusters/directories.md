# Important Directories under Cluster Homes

The following directories are present under the home folder of each cluster (the so-called **Cluster Home**), accessible within the [Login Node](../login/directories.md) under the path `/home/<username>/<cluster-alias>`. 

```
.
├── data
├── dropbox              => /dropbox/gmogni
├── exabyte-io           => /cluster-001-share/groups/exabyte-io
└── job_script_templates => /export/compute/job_script_templates
```

The above **directory structure** is mounted on the cluster's dedicated **Master Node**. Each listed folder is introduced in what follows, complementing the [general discussion](../../data-on-disk/directories.md) on the directory structure within our platform.

## Personal Account Data 

Each user has a personal **data folder** associated with his own **personal account**. More detail about this folder can be found [here](../../data-on-disk/directories.md#data-folder).

## Organization Shared Data 
 
Members of an Organization can share data together via the corresponding **shared folder**, which bears the same name as the Organization itself ("exabyte.io" in the above example of directory structure). This type of folder is further described [in this page](../../data-on-disk/directories.md#shared-folders-for-organizations).

## Dropbox

Dropbox is a convenient way of sharing and transferring files across all nodes of the infrastructure. This functionality is narrated in detail in its own [dedicated page](../../data-in-objectstorage/dropbox.md).

## Jobscript Templates

The Login Home also contains a folder with [Job script](../../jobs-cli/batch-script.md) template examples, necessary for [submitting jobs via the Command Line Interface](../../jobs-cli/overview.md). 
 
## Temporary Data
 
Personal Accounts can also share data between them, without necessarily belonging to an Organization, via the **temporary folder** located under the path `/tmp`.

!!!warning "Warning: unreliability of temporary data storage"
    The data in this temporary folder is not guaranteed to be saved for a long time - use with caution or consider upgrading to an Organizational account.

## Modeling Data

The aforementioned personal data and Organization shared data folders contain the data from each [simulation job](../../jobs/overview.md) executed on the given cluster under consideration. This data is stored in these folders according to the conventions outlined below.

### Project directories

Calculations/Jobs are organized into [projects](../../jobs/projects.md) containers, each of which has a filesystem directory associated with it on each cluster where its associated Jobs have been executed. 

For example, if user `steven` creates a project called `my-project`, and executed some of its jobs under "cluster-001", then the data for the jobs corresponding to this project will be stored inside `/home/steven/cluster-001/data/my-project`.

!!! note "Default project"
    Each user has a *default* project that is named according to his/her username. So user `steven` has a default project `steven-default` (shown as "Default" on the Web Interface).

### Job directories

Within a project, each job is stored in its own directory as well. Job names are *[slugified](../../entities-general/data.md#Slug-Representation)*, or in other words put into UNIX-safe format, before creating a filesystem directory. In addition, each job name also contains a unique identifier. 

So if a job `New Job Sep 20th 2016, 13:43 PM` is created inside the default project for user `steven` and executed on "cluster-001", its files will be stored inside the folder named as the following example.

```bash
"/home/steven/cluster-001/data/steven-default/new-job-sep-20th-2016-13-43-pm-STb28Hgr82C5DRg5H"
```
