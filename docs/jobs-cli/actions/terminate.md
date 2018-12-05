# Job Termination

In order for the user to prematurely **terminate** a job which was [submitted for execution via CLI](../overview.md), and is therefore either "Queued" or "Running" under the [list of job statuses](check-status.md), the `qdel` command should be used. This command should be operated in conjunction with the **"Job ID"**, as returned by the `qstat` [command](check-status.md) under the **"JOBID"** column of its output. 

For example, the following command will kill the job with the `814.master-production-20160630-cluster-007.exabyte.io` ID.

```
[steve@bohr.exabyte.io:~]$ qdel 814.master-production-20160630-cluster-007.exabyte.io
```

The complete manual page for the `qdel` command, listing the available option flags, can be retrieved under page 337 of Ref. [^1].

## Links

[^1]: [Torque Resource Manager Administrator Guide, Document](http://docs.adaptivecomputing.com/torque/6-1-2/adminGuide/torqueAdminGuide-6.1.2.pdf)
