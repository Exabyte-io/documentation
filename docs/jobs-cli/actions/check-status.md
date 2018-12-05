# Check Job Status

The user can **inspect the status** of current [Jobs submitted via CLI](../overview.md) at any moment through the `qstat` command, which returns an output of the following kind.

```
[steve@bohr.exabyte.io:~]$ qstat
JOBID              USERNAME    QUEUE    JOBNAME    STATE    MEMORY    USEDTIME    WALLTIME      NODES    CPU
-----------------  ----------  -------  ---------  -------  --------  ----------  ----------  -------  -----
11665.cluster-001  steve       D        my_job     C        0kb       00:00:10    00:10:00          1      1
11666.cluster-001  steve       OR       my_job     R        1235kb    00:00:10    00:10:00          1      1
```

The complete manual page for this command listing all its possible option flags can be found under Ref. [^1].

## Job ID

The `qstat` command displays the information about jobs organized by their IDs, as listed under the **"JOBID"** column of the output. This "job id" includes the alias of the cluster where the job has been submitted (for example, the entry "11665.cluster-001" listed above).

It is important to make a note of this ID for job tracking and problem resolution, as well as for the case when [job termination](terminate.md) by the user becomes necessary.
 
## Possible Job Statuses

The possible job statuses indicated under the "STATE" column of the command output include the following possibilities.

- "Q": Job is currently **Queued** and still pending execution. 
- "R": Job is currently **Running**.
- "C": Job execution is **Complete**. This can include the possibility of jobs terminated because of errors.

## Links

[^1]: [qstat Manual Page, Website](https://www.jlab.org/hpc/PBS/qstat.html)
