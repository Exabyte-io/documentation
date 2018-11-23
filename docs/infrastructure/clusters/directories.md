# Modeling data

Data from each calculation/job initiated through the web application is stored inside user home directory within the `~/data` directory. So user `steven` would have the calculation data within `/home/steven/data/` directory.

### Project directories

Calculations/Jobs are organized into projects, each of which has a filesystem directory associated with. If user `steven` creates project `my-project`, then the data for the jobs corresponding to this project will be stored inside `/home/steven/data/my-project`.

!!! note "Default project"
    Each user has a *default* project that is named according to his/her username. So user `steven` has a default project `steven-default` (shown as "Default" on the web) within `/home/steven/data/steven-default` directory.

### Job directories

Within a project each job is stored in its own directory as well. Job names, as visible within the web application are *slugified*, or put into UNIX-safe format before creating a filesystem directory. In addition, each job name also contains a unique identifier. So if a job `New Job Sep 20th 2016, 13:43 PM` is created inside the default project for user `steven`, its files will be stored inside the folder named:

```bash
"/home/steven/data/steven/new-job-sep-20th-2016-13-43-pm-STb28Hgr82C5DRg5H"
```
