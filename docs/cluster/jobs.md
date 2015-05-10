# Submitting Batch Jobs
---

High performance parallel computing codes generally run in "batch" mode. Batch jobs are controlled by scripts written by the user and submitted to a batch system that manages the compute resource and schedules the job to run based on a set of policies. In general, batch systems work on a first-in, first-out basis, but this is subject to a number of constraints.

---

## Batch Jobs

Batch scripts consist of two parts: 1) a set of directives that describe your resource requirements (time, number of processors, etc.) and 2) UNIX commands that perform your computations. These UNIX command may create directories, transfer files, etc.; anything you can type at a UNIX shell prompt.

The actual execution of your parallel job, however, is handled by a special command, called a job launcher. In a generic Linux environment this utility is often called "mpirun".

---

### Interactive parallel jobs

In Development

<!-- , debugging, and testing of parallel code demands interactivity. You can run parallel jobs interactively, subject to a 30-minute time limit and limit on the number of nodes. Instead of submitted a batch job script, you tell the batch system that you want interactive access and then run your command at the command prompt:

```
qsub -V -I -lmppwidth=<number of cores> 
cd $PBS_O_WORKDIR
mpirun -n <number of tasks> <name_of_executable_binary>
```
 -->

---

### Non-interactive batch jobs

A batch job is the most common way users run production applications on parallel machines. Our batch system is based on the PBS model, implemented with the Moab scheduler and Torque resource manager.

Typically, the user submits a batch script to the batch system. This script specifies, at the very least, how many nodes and cores the job will use, how long the job will run, and the name of the application to run. The job will advance in the queue until it has reached the top. At this point, Torque will allocate the requested number of nodes to the batch job. The batch script itself will execute on the "head node" (sometimes known as the "MOM" node).

---

## Sample Batch Scripts

Although there are default values for all batch parameters, it is a good idea always to specify the name of the queue, the number of nodes, and the walltime for all batch jobs. To minimize the time spent waiting in the queue, specify the smallest walltime that will safely allow the job to complete.

A common convention is to append the suffix ".pbs" to batch scripts.

---

### Batch Script for Regular Compute

This example requests 16 nodes, and 8 tasks per node, for 10 minutes, on regular (partition=O) compute resources.

```bash
#PBS -N my_job
#PBS -l partition=O
#PBS -l nodes=16
#PBS -l ppn=8
#PBS -l walltime=00:10:00:00
#PBS -m abe
#PBS -M user@email-service.com

cd $PBS_O_WORKDIR
module load mpi/intel/ips-2013
mpirun -np 128 ./my_executable
```

---

### Batch Script for Cost-saving Compute

This example requests 16 nodes, and 8 tasks per node, for 10 minutes, on Cost-saving (partition=S) compute resources.

```bash
#PBS -N my_job
#PBS -l partition=S
#PBS -l nodes=16
#PBS -l ppn=8
#PBS -l walltime=00:10:00:00
#PBS -m abe
#PBS -M user@email-service.com

cd $PBS_O_WORKDIR
module load mpi/intel/ips-2013
mpirun -np 128 ./my_executable
```

If you want PBS to automatically restart your jobs in case of spot node termination by price, please set `#PBS -r y` directive in job script file. 

In order to get notified of spot node termination via email, the `#PBS -m abe` and `#PBS -M email_address` directives should be set in job script file.

---

## Submit Example

Submit your batch script with the qsub command:

```
qsub my_job.pbs
123456.cluster
```

The qsub command displays the job_id (12346.cluster in the above example). It is important to keep track of your job_id for job tracking and problem resolution.

---

## View Example

View your currently submitted jobs with the qstat command:

```
qstat
[steve@cluster example_QE]$ qstat
Job ID                    Name             User            Time Use S Queue
------------------------- ---------------- --------------- -------- - -----
156.cluster                QE               steve           00:00:05 C batch          
157.cluster                QE               steve                  0 R batch
```

The qsub command displays the information about your job organized by its ID. You can also view detailed information about each job by passing -f flag: `qstat -f $JOB_ID`.

---

## Torque Keywords

The following keywords may be specified as qsub command line options, or as directives (preceded by #PBS) embedded in a batch script.

<hr>
<table border="0">
    <tbody>
        <tr>
            <th style="text-align: center; padding: 10px;" colspan="3">Required Torque Options/Directives</th>
        </tr>
        <tr>
            <th style="text-align: center;">Option</th>
            <th style="text-align: center;">Default</th>
            <th style="text-align: center;">Description</th>
        </tr>
        <tr>
            <td>-l nodes=Nodes</td>
            <td>1 node</td>
            <td>
                Number of nodes assigned to the job.
            </td>
        </tr>
        <tr>
            <td>-l ppn=ProcessPerNode</td>
            <td>1 process per node</td>
            <td>
                Number of processes per node **Note:** ppn must be less than or equal to the maximum available cores on the target compute node.
            </td>
        </tr>
        <tr>
            <td>-l partition=O</td>
            <td>O</td>
            <td>Compute resorces allocated to the job, could be "O" for regular On-demand resources and "S" for cost-saving Spot-based resources</td>
        </tr>
        <tr>
            <td>-l walltime=DD:HH:MM:SS</td>
            <td>00:00:05:00</td>
            <td>Maximum wallclock time for job</td>
        </tr>
        <tr>
            <td>-N job_name</td>
            <td>Name of job script</td>
            <td>Name of job; up to 15 printable, non-whitespace characters</td>
        </tr>
        <tr>
            <th style="text-align: center; padding:10px;" colspan="3">Useful Torque Options/Directives</th>
        </tr>
            <th style="text-align: center;">Option</th>
            <th style="text-align: center;">Default</th>
            <th style="text-align: center;">Description</th>
        </tr>
        <tr>
            <td>-q queue_name</td>
            <td>batch</td>
            <td>Name of submit queue</td>
        </tr>
        <tr>
        <!--<tr>
            <td>-A repo</td>
            <td>Default repo</td>
            <td>Charge job to repo</td>
        </tr>-->
        <tr>
            <td>-e filename</td>
            <td>&lt;job_name&gt;.e&lt;job_id&gt;</td>
            <td>Write stderr to filename</td>
        </tr>
        <tr>
            <td>-o filename</td>
            <td>&lt;job_name&gt;.o&lt;job_id&gt;</td>
            <td>Write stdout to filename</td>
        </tr>
        <tr>
            <td>-j [oe | eo]</td>
            <td>Do not merge</td>
            <td>Merge (join) stdout and stderr. If oe, merge as output file; ie eo, merge as error file</td>
        </tr>
        <tr>
            <td>-m [a | b | e | n]</td>
            <td>a</td>
            <td>Email notification: a=send mail if job aborted by system b=send mail when job begins e=send mail when job ends n=never send email Options a, b, e may be combined</td>
        </tr>
        <tr>
            <td>-M email_address</td>
            <td>None</td>
            <td>User email address</td>
        </tr>
        <!--<tr>
            <td>-S shell</td>
            <td>Login shell</td>
            <td>Specify shell to interpret batch script</td>
        </tr>
        <tr>
            <td>-l gres=resource[%resource]</td>
            <td>Run whether resource is available or not</td>
            <td>Resource can be gscratch, project, or projectb. Specify if a batch job uses /resource. When set, a job will not start during scheduled /resource file system maintenance.</td>
        </tr>
        <tr>
            <td>-V</td>
            <td>Do not export</td>
            <td>Export current environment variables into the batch job environment. NOTE: this option is not recommended by NERSC; it can make it difficult to reproduce results (including diagnosing job failures).</td>
        </tr>-->
    </tbody>
</table>
<hr>

## Torque Environment Variables

The batch system defines many environment variables, which are available for use in batch scripts. The following tables list some of the more useful variables. Users must not redefine the value of any of these variables!

<hr>
<table border="0">
    <tbody>
        <tr style="padding:10px;">
            <td><strong>Variable Name<strong></td>
            <td><strong>Meaning<strong></td>
        </tr>
        <tr>
            <td>PBS_O_LOGNAME</td>
            <td>Login name of user who executed qsub.</td>
        </tr>
        <tr>
            <td>PBS_O_HOME</td>
            <td>Home directory of submitting user.</td>
        </tr>
        <tr>
            <td>PBS_O_WORKDIR</td>
            <td>Directory in which qsub command was executed. Note that batch jobs begin execution in $PBS_O_HOME; many batch scripts execute "cd $PBS_O_WORKDIR" as first executable statement.</td>
        </tr>
        <tr>
            <td>PBS_O_HOST</td>
            <td>Hostname of system on which qsub was executed. This is typically a Carver login node.</td>
        </tr>
        <tr>
            <td>PBS_JOBID</td>
            <td>Unique identifier for this job; important for tracking job status.</td>
        </tr>
        <tr>
            <td>PBS_ENVIRONMENT</td>
            <td>Set to "PBS_BATCH" for scripts submitted as batch jobs; "PBS_INTERACTIVE" for interactive batch jobs ("qsub -I ...").</td>
        </tr>
        <tr>
            <td>PBS_O_QUEUE</td>
            <td>Name of submit queue.</td>
        </tr>
        <tr>
            <td>PBS_QUEUE</td>
            <td>Name of execution queue.</td>
        </tr>
        <tr>
            <td>PBS_O_JOBNAME</td>
            <td>Name of this job.</td>
        </tr>
        <tr>
            <td>PBS_NODEFILE</td>
            <td>Name of file conta
            ining list of nodes assigned to this job.</td>
        </tr>
        <tr>
            <td>PBS_NUM_NODES</td>
            <td>Number of nodes assigned to this job.</td>
        </tr>
        <tr>
            <td>PBS_NUM_PPN</td>
            <td>Value of "ppn" (processes per node) for this job.</td>
        </tr>
    </tbody>
</table>
<hr>

## Standard Output and Error

While your job is running, standard output (stdout) and standard error (stderr) are written to temporary "spool" files (for example: 123456-cluster.OU and 123456-cluster.ER) in the submit directory. If you merge stderr/stdout via the "#PBS -j eo" or "#PBS -j oe" option, then only one such spool file will appear.

These files will be updated in real-time while the job is running, allowing you to use them for job monitoring. It is important that you do not modify, remove or rename these spool files while the job is still running!

After your batch job completes, the above files will be renamed to the corresponding stdout/stderr files (for example: my_job.o123456 and my_job .e123456).

---

## Links

[1] [PBS](http://en.wikipedia.org/wiki/TORQUE)

[2] [A tutorial on running batch jobs using PBS](http://www.nersc.gov/users/computational-systems/carver/running-jobs/batch-jobs/)

---
