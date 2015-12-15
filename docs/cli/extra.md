Advanced batch job configuration
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
        <tr>
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
            <td>-A repo</td>
            <td>Default repo</td>
            <td>Charge job to repo</td>
        </tr>
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
            <td><strong>Variable Name</strong></td>
            <td><strong>Meaning</strong></td>
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

## Links

1. [PBS/Torque](http://en.wikipedia.org/wiki/TORQUE)
2. [A tutorial on running batch jobs using PBS](http://www.nersc.gov/users/computational-systems/carver/running-jobs/batch-jobs/)
