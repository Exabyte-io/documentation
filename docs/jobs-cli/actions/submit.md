## Submit Example

The batch script can finally be submitted with the `qsub` command:

```
[steve@bohr.exabyte.io:~]$ qsub -c cluster-001 my_job.pbs
11665.cluster-001
```

The qsub command displays the job_id (11665.cluster-001 in the above example). It is important to keep track of your job_id for job tracking and problem resolution.
