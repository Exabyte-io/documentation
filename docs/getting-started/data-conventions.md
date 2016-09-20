<!-- by TB -->

This page contains basic conventions employed within our product.

# Data storage

We provide each user with 2 types of data storage: *filesystem* and *object*. The former is used to store the data on the disk, and the latter is used for long-term storage and data access from within the web application. Data is copied from filesystem to object storage after each complete calculation. When data is deleted from filesystem, a copy remains in object storage during the grace period. After grace period is over the data is removed from object storage.

## Home directory(s)

Each user has a home directory on our filesystem: `/home/<username>/`. So user `steven` would have `/home/steven/` as a home directory.

We also have a role-based permission scheme for organizations and teams. Each organization has a directory shared between its members. Organization `exabyte` would have `/share/groups/exabyte/` as such.

!!! note "Command line users"
    The above information is relevant to users with access to command line and remote desktop, as only they are able to navigate the filesystem directly.

## Calculation data

Data from each calculation/job initiated through the web application is stored inside user home directory within the `~/data` directory. So user `steven` would have the calculation data within `/home/steven/data/` directory.

## Project directories

Calculations/Jobs are organized into projects, each of which has a filesystem directory associated with. If user `steven` creates project `my-project`, then the data for the jobs corresponding to this project will be stored inside `/home/steven/data/my-project`.

!!! note "Default project"
    Each user has a *default* project that is named the same as his/her username. So user `steven` has a default project `steven` within `/home/steven/data/steven` directory.

## Job directories

Within a project each job is stored in its own directory as well. Job names, as visible within the web application are *slugified*, or put into UNIX-safe format before creating a filesystem directory. In addition, each job name also contains a unique identifier. So if a job `New Job Sep 20th 2016, 13:43 PM` is created inside the default project for user `steven`, its files will be stored inside the folder named:

```bash
/home/steven/data/steven/new-job-sep-20th-2016-13-43-pm-STb28Hgr82C5DRg5H
```

# Data sharing

We provide a comprehensive set of options for setting up shared access to data.

## Default project

Access levels for a project could be set to private or public. Default project for each users has public access level. Therefore, all calculations submitted within this project by the user who owns it will be accessible to other users too.

## Private data

Depending on the [service level](/billing/pricing-and-service-levels.md), it is possible to set up access level for a project to private. In this case no other users will be able to view jobs belonging to such project, unless they are given permission to do so.

