# Submit Job

The [Batch Script](../batch-scripts/overview.md) of the simulation Job can finally be **submitted** for [Job execution via CLI](../overview.md) to the desired [computing cluster](../../infrastructure/clusters/overview.md), after all simulation input files have been [gathered together](create.md) under the same [Working Directory](../batch-scripts/directories.md). This Working Directory has to be located within the [Home folder](../../infrastructure/clusters/directories.md) of the cluster on which the user wants to execute the job.  

Job submission is performed with the `qsub` command, as demonstrated in the following example, where the Batch Script in this case is called `my_job.pbs`.

```
[steve@bohr.exabyte.io:~]$ qsub my_job.pbs
11665.cluster-001
```

The complete manual page for this `qsub` listing all the possible option flags command can be reviewed in Ref. [^1].

## Jobs ID

Just after it is entered, the `qsub` command displays the **"job id"**, which includes the alias of the cluster where the job has been submitted (11665.cluster-001 in the above example).
 
It is important to remember this "job id" for job tracking and any problem resolution, as well as in the eventuality of [job termination](terminate.md) by the user.

## Links

[^1]: [qsub Manual Page, Website](https://www.jlab.org/hpc/PBS/qsub.html)
