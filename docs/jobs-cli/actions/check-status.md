## View Example

View your currently submitted jobs with `qstat` command:

```
[steve@bohr.exabyte.io:~]$ qstat
JOBID              USERNAME    QUEUE    JOBNAME    STATE    MEMORY    USEDTIME    WALLTIME      NODES    CPU
-----------------  ----------  -------  ---------  -------  --------  ----------  ----------  -------  -----
11665.cluster-001  steve       D        my_job     C        0kb       00:00:10    00:10:00          1      1
11666.cluster-001  steve       OR       my_job     R        1235kb    00:00:10    00:10:00          1      1
```

The qsub command displays the information about your job organized by its ID.
