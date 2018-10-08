This page provides a basic overview of the data conventions employed within our product.

# Overview

We provide each user with 2 types of non-structured data storage: *filesystem* and *object*. The former is used to store the data on the disk, and the latter is used for long-term storage and data access from within the web application. Data is copied from filesystem to object storage after each complete calculation. When data is deleted from filesystem, a copy remains in object storage during the grace period. After grace period is over the data is removed from object storage too.

## Home directory

Each user has a home directory on our filesystem: `/home/<username>/`. So user `steven` would have `/home/steven/` as a home directory.

## Share directory

We also have a role-based permission scheme for organizations and teams. Each organization has a directory shared between its members. Organization `exabyte` would have `/share/groups/exabyte/` as such.

!!! note "Command line users"
    The above information is relevant to users with access to command line and remote desktop, as they are able to navigate the `/home` and `/share` directories directly. Readers may also find more information about our unified storage system and how it affects the content of home/share directories [here](/compute/cli/storage-system/).



## Dropbox directory

In order to faciliate data upload and editing from the web we enable each user with a special directory accessible both from web and command-line. Just like with `/home` each user has such a directory located at `/dropbox/<username>` in filesystem.

!!! warning "Dropbox is limited to 1GB in size"
    In order to faciliate the accessibility of `Dropbox` directory on each of the components of our distributed compute system we limit it in size to 1GB. It is designed to be used for for input files, scripts (ex. pseudopotentials) and other non-bulky data used during multiple calculations.

# Modeling data

Data from each calculation/job initiated through the web application is stored inside user home directory within the `~/data` directory. So user `steven` would have the calculation data within `/home/steven/data/` directory.

## Project directories

Calculations/Jobs are organized into projects, each of which has a filesystem directory associated with. If user `steven` creates project `my-project`, then the data for the jobs corresponding to this project will be stored inside `/home/steven/data/my-project`.

!!! note "Default project"
    Each user has a *default* project that is named according to his/her username. So user `steven` has a default project `steven-default` (shown as "Default" on the web) within `/home/steven/data/steven-default` directory.

## Job directories

Within a project each job is stored in its own directory as well. Job names, as visible within the web application are *slugified*, or put into UNIX-safe format before creating a filesystem directory. In addition, each job name also contains a unique identifier. So if a job `New Job Sep 20th 2016, 13:43 PM` is created inside the default project for user `steven`, its files will be stored inside the folder named:

```bash
"/home/steven/data/steven/new-job-sep-20th-2016-13-43-pm-STb28Hgr82C5DRg5H"
```

# Sharing and collaboration

We provide a comprehensive set of options for setting up shared access to data. [Share directory](#share-directory) above is one example. More explanation [here](/collaboration/organizations.md).

## Default project

Access levels for a project could be set to private or public. Default project for each users has public access level. Therefore, all calculations submitted within this project by the user who owns it will be accessible to other users too.

## Private data

Depending on the [service level](/pricing/service-levels.md), it is possible to set up access level for a project to private. In this case no other users will be able to view jobs belonging to such project, unless they are given permission to do so.

!!! note "Data for organizations is private by default"
    Our organization concept is designed for enterprise users and so we set access level for the data generated under organizational accounts as private by default.

