# Resource Manager Directives

As introduced [here](general-structure.md#3.-directives), the keywords described in the present page may be specified as **PBS Resource Manager Directives** (preceded by the `#PBS` prefix), to be embedded in a [batch script](overview.md). These directives are particularly important for allocating the necessary [computational resources and parameters](../../infrastructure/compute/parameters.md) to the given [simulation Job](../../jobs/overview.md), for its [submission to the CLI](../overview.md).

!!!note "Accounting information"
    We recommend the user to first consult the accounting aspects of such directives documented [here](../accounting.md), before proceeding with job submission.

!!!info "Further information and documentation"
    Further documentation on the software we employ, known as **TORQUE**, for implementing the PBS job scheduling and resource management protocol, can be found under Ref. [^1].

## Important Directives

|   Directive   |  Default | Description |
| ------------------|------------------|------------------|
| -l nodes = <number nodes>  |  1 node   | Number of [compute nodes](../../infrastructure/compute/parameters.md#nodes-/-ppn) assigned to the job  |
| -l ppn = <processors per node> | 1 processor per node | Number of [processors per node](../../infrastructure/compute/parameters.md#nodes-/-ppn) (ppn). **Note:** ppn must be less than or equal to the maximum available number of cores on the target compute node |
| -l walltime = <DD:HH:MM:SS> |  00:00:05:00  |  The maximum authorized [wallclock time](../../infrastructure/compute/parameters.md#time-limit) for the job, after which the job will be automatically terminated |
| -N <Name of job script> | No default  |  The name of the job; up to 15 printable, non-whitespace characters |
| -q <queue code>  |  batch  |  Name of submit [queue](../../infrastructure/resource/queues.md), for example "D" for Debug or "OR16" for Ordinary, Regular, 16 cores per each compute node  |
| -R  <y or n>     |      y           | Register Job in the Web Interface ("y" for yes or "n" for no). This option is further explained [here](../accounting.md#register-jobs-in-web-interface) |
| -A <Project Name> | Default Project |  [Charge job](../../accounts/payments-charges.md) to the selected [project](../../jobs/projects.md) |

## Other Useful Directives

|   Directive   |  Default | Description |
| ------------------|------------------|------------------|
| -r  <y or n>     |      y           | Make the job re-runnable, in the sense that it can be restarted automatically. Select either "y" for yes or "n" for no. This is particularly useful when running Jobs under the [Saving queue category](../../infrastructure/resource/category.md), where the job can be interrupted anytime due to limited resources |     
| -e <filename>     |   &lt;job_name&gt;.e&lt;job_id&gt; | Write the standard error message(s) (stderr) encountered during job execution to the selected file name |
| -o <filename>     |  &lt;job_name&gt;.o&lt;job_id&gt; | Write the standard output of the simulation (stdout) to the selected file name |
| -j <oe or eo>      | Do not merge  | Merge (join) stdout and stderr. Select "oe" for merging to output file, or "eo" for merging to error file instead | 
| -m <a or b or e or n> |  a  | Email notification: a = send mail if job aborted by system; b = send mail when job begins; e = send mail when job ends; n = never send email. All the options may be combined together |
| -M <email_address> |  None  | User email address to which the above-mentioned notifications should be sent |

## Environment Variables

The batch system defines many **environment variables**, which are available for use in batch scripts. The following tables list some of the more useful variables.
 
!!!warning "Variables modification not recommended" 
    The user is advised not to redefine the value of any of these variables.
    
!!!info "Further information and documentation"
    Further explanation of these Environment Variables can be found under Ref. [^1].

| Variable Name   | Meaning |
| --------------- | -------------|
| PBS_O_LOGNAME   | Login name of user who [submitted](../actions/submit.md) the job |
| PBS_O_HOME      | Home directory of submitting user    |
| PBS_O_WORKDIR   | Working directory in which the job files were defined and then [submitted](../actions/submit.md) |
| PBS_JOBID       | Unique identifier for this job; important for tracking [job status](../actions/check-status.md) |
| PBS_O_QUEUE     | Name of submit [queue](../../infrastructure/resource/queues.md) |
| PBS_QUEUE       | Name of execution [queue](../../infrastructure/resource/queues.md)  |
| PBS_O_JOBNAME   | Name of the present job |
| PBS_NODEFILE    | Name of file containing list of [nodes](../../infrastructure/compute/parameters.md#nodes-/-ppn) assigned to this job |
| PBS_NUM_NODES   | Number of [nodes](../../infrastructure/compute/parameters.md#nodes-/-ppn) assigned to this job  |
| PBS_NUM_PPN     | Value of ["ppn" (processes per node)](../../infrastructure/compute/parameters.md#nodes-/-ppn) for this job |
| PBS_NP          | Total number of processors, that is the multiplication of the above-mentioned PBS_NUM_NODES with PBS_NUM_PPN |

## Standard Output and Error

While your job is running, the **standard output (stdout)** and **standard error (stderr)** of the simulation are written to temporary **"spool" files** (for example: 123456-cluster.OU and 123456-cluster.ER) in the submit directory. If the user decides to merge stderr/stdout via the aforementioned `#PBS -j eo` or `#PBS -j oe` directives, then only one such spool file will appear.

These files will be updated in real-time while the job is running, allowing the user to make use of them for job monitoring. It is important that these spool files are not modified, removed or renamed while the job is still running.

After the batch job completes, the above files will be renamed to the corresponding stdout/stderr files (for example: my_job.o123456 and my_job .e123456).

## Links

[^1]: [Torque Resource Manager Administrator Guide, Document](http://docs.adaptivecomputing.com/torque/6-1-2/adminGuide/torqueAdminGuide-6.1.2.pdf)
