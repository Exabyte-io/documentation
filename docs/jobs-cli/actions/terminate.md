# Job Termination

In order to prematurely **terminate** a job which was [submitted for execution via CLI](../overview.md), and is therefore either "Queued" or "Running" under the [list of job statuses](check-status.md), the `qdel` command should be used. This command should be operated in conjunction with the **job id**, as returned by the `qstat` [command](check-status.md) under the **"JOBID"** column of its output. 

For example, the following command will kill the job with id "11665.cluster-001".

```
[steve@bohr.exabyte.io:~]$ qdel 11665.cluster-001
```

The complete manual page for the `qdel` command, listing the available option flags, can be retrieved under Ref. [^1].

## Email Notifications

In order to get notified via email about an accidental job termination, resulting for example from computational errors or in case the job is being executed in the [Saving Queue](../../infrastructure/resource/category.md), the `#PBS -m abe` and `#PBS -M < email_address >` [directives](../batch-scripts/directives.md) must be set inside the [job script file](../batch-scripts/overview.md). 

In addition, for the latter case of Jobs being run in the Saving Queue, our scheduling system automatically restarts any unintentionally terminated jobs, and re-submits them into the [regular queue](../../infrastructure/resource/category.md). If the user does not want the job to be restarted in this way, he/she must set the `#PBS -r n` [directive](../batch-scripts/directives.md) inside the [job script](../batch-scripts/overview.md). In this case, a temporary folder containing the job's intermediate results is created in the user's home directory.

## Links

[^1]: [qdel Manual Page, Website](https://www.jlab.org/hpc/PBS/qdel.html)
