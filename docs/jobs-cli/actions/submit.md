# Submit Job

The [Batch Script](../batch-scripts/overview.md) of the simulation Job can finally be **submitted** for [Job execution via CLI](../overview.md) to the desired [computing cluster](../../infrastructure/clusters/overview.md), after all simulation input files have been [gathered together](create.md) under the same [Working Directory](../batch-scripts/directories.md). This Working Directory has to be located within the [Home folder](../../infrastructure/clusters/directories.md) of the cluster on which the user wants to execute the job.  

Job submission is performed with the `qsub` command, as demonstrated in the following example, where the Batch Script in this case is called `my_job.pbs`.

```
[steve@bohr.exabyte.io:~]$ qsub my_job.pbs
814.master-production-20160630-cluster-007.exabyte.io
```

The complete manual page for this `qsub` command, listing its possible option flags, can be reviewed in page 373 of Ref. [^1].

## Jobs ID

Just after it is entered, the `qsub` command returns the **"Job ID"**, which includes the alias of the cluster where the job has been submitted (for example, `cluster-007` within the `814.master-production-20160630-cluster-007.exabyte.io` job ID in the above example).
 
It is important to remember this "job id" for job tracking and for any problem resolution, as well as in the eventuality of [job termination](terminate.md) by the user.

## Links

[^1]: [Torque Resource Manager Administrator Guide, Document](http://docs.adaptivecomputing.com/torque/6-1-2/adminGuide/torqueAdminGuide-6.1.2.pdf)
