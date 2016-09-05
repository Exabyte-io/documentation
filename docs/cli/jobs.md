<!-- by MM -->

This page explains the basics of command-line interface for batch job submission.

# Batch jobs

Simulation tasks submitted through command-line interface are expected to be run in "batch" mode. Batch jobs are controlled by scripts written by the user and submitted to the resource management system.

## Batch Jobs

Batch scripts consist of two parts, a set of directives that describe your resource requirements (time, number of processors, etc.) and UNIX commands that perform your computations. These UNIX command may create directories, transfer files, etc.; anything you can type at a UNIX shell prompt.

The actual execution of your parallel job, however, is handled by a special command, called a job launcher. In a generic Linux environment this utility is often called "mpirun".

## Interactive parallel jobs

Interactive parallel jobs are not supported by design. Users are encouraged to prototype calculations on the login node (using 2-8 CPU with < 1min walltime per user) instead, and submit larger debug tasks into the debug queue.

## Non-interactive batch jobs

Our batch system is based on the PBS model, implemented with the Moab scheduler and Torque resource manager.

Typically, the user submits a batch script to the batch system. This script specifies, at the very least, how many nodes and cores the job will use, how long the job will run, and the name of the application to run.

## Sample Batch Scripts

Sample batch scripts for the available [queue types]() are given below. A common convention is to append the suffix ".pbs" or ".job" or ".sh" to batch scripts.

### Debug queue (D)

This example explains the keywords and requests 1 node with 2 processors (cores) for 10 minutes:

```bash
#!/bin/bash

# ---------------------------------------------------------- #
#                                                            #
#  Example job submission script for Exabyte.io platform     #
#                                                            #
#  Shows resource manager directives for:                    #
#                                                            #
#    1. the name of the job                (-N)              #
#    2. the number of nodes to be used     (-l nodes=)       #
#    3. the number of processors per node  (-l ppn=)         #
#    4. queue                              (-q D) or OR, OF  #
#    5. merging standard output and error  (-j oe)           #
#    6. email about job abort, begin, end  (-m abe)          #
#    7. email address to use               (-M)              #
#    8. the walltime in dd:hh:mm:ss format (-l walltime=)    #
#                                                            #
# ---------------------------------------------------------- #

#PBS -N job_name
#PBS -l nodes=1
#PBS -l ppn=2
#PBS -q D
#PBS -j oe
#PBS -l walltime=00:10:00
#PBS -m abe
#PBS -M name@domain.com

cd $PBS_O_WORKDIR
module load < MODULE_NAME >
mpirun -np $PBS_NP ./my_executable
```

### On-demand regular (OR)

This example requests 1 node, and 18 cores per node, for 10 minutes

```bash
#!/bin/bash

#PBS -N job_name
#PBS -l nodes=1
#PBS -l ppn=18
#PBS -q OR
#PBS -j oe
#PBS -l walltime=00:10:00
#PBS -m abe
#PBS -M name@domain.com

cd $PBS_O_WORKDIR
module load < MODULE_NAME >
mpirun -np $PBS_NP ./my_executable
```

### On-demand fast (OF)

This example requests 4 nodes, and 8 cores per node, for 10 minutes

```bash
#!/bin/bash

#PBS -N job_name
#PBS -l nodes=4
#PBS -l ppn=8
#PBS -q OF
#PBS -j oe
#PBS -l walltime=00:10:00
#PBS -m abe
#PBS -M name@domain.com

cd $PBS_O_WORKDIR
module load < MODULE_NAME >
mpirun -np $PBS_NP ./my_executable
```


### Saving regular (SR)

This example requests 1 node, and 18 cores per node, for 10 minutes

```bash
#!/bin/bash

#PBS -N job_name
#PBS -l nodes=1
#PBS -l ppn=18
#PBS -q SR
#PBS -j oe
#PBS -l walltime=00:10:00
#PBS -m abe
#PBS -M name@domain.com

cd $PBS_O_WORKDIR
module load < MODULE_NAME >
mpirun -np $PBS_NP ./my_executable
```

### Saving fast (SF)

This example requests 4 nodes, and 8 tasks per node, for 10 minutes

```bash
#!/bin/bash

#PBS -N job_name
#PBS -l nodes=4
#PBS -l ppn=8
#PBS -q SF
#PBS -j oe
#PBS -l walltime=00:10:00
#PBS -m abe
#PBS -M name@domain.com

cd $PBS_O_WORKDIR
module load < MODULE_NAME >
mpirun -np $PBS_NP ./my_executable
```


### Specify Job Project
In order to specify a project that job belongs to and should be charged upon, a `#PBS -A PROJECT_NAME` directive should be used in job script file. Each user has a default project that jobs are charged on by default.


## Submit Example

Submit your batch script with `qsub` command:

```
[steve@bohr.exabyte.io:~]$ qsub -c cluster-001 my_job.pbs
11665.cluster-001
```

The qsub command displays the job_id (11665.cluster-001 in the above example). It is important to keep track of your job_id for job tracking and problem resolution.


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

## Job termination

In order to get notified about capacity-based termination of a task in saving queue via email, `#PBS -m abe` and `#PBS -M < email_address >` directives must be set inside the job script file. In addition, our scheduling system automatically restarts terminated jobs and re-submits them into the regular queue. If you do not want your job to be restarted this way, set `#PBS -r n` directive in the job script. A temporary directory for job's intermediate results are created in user's home directory.
