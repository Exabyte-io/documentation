# Batch Scripts

This page explains the basics of [Command Line Interface](../cli/overview.md) (CLI) for the submission of [simulation Jobs](../jobs/overview.md). The corresponding actions are narrated [separately](actions/overview.md).

Simulation tasks submitted through CLI are expected to be run in **"batch" mode**. Batch jobs are controlled by the so-called **Batch Scripts** (also referred to as **Job Scripts**), which are written by the user and then submitted to the [resource management system](../infrastructure/resource/overview.md).

Batch scripts consist of two parts, a set of **directives** that describe the [resource requirements](../infrastructure/compute/parameters.md) (time, number of processors, etc.), and **UNIX commands** that perform the relevant computations. These UNIX command may perform anything that can be done under a UNIX shell prompt, such as creating directories, transferring files, etc.

The actual execution of the parallel job, however, is handled by a special command, called a **job launcher**. In a generic Linux environment, this utility is often labelled "mpirun".

## Interactive Parallel Jobs

Interactive parallel jobs are not supported by design. Users are encouraged to prototype calculations on the login node (using 2-8 CPU with < 1min walltime per user) instead, and submit larger debug tasks into the [debug queue](../infrastructure/resource/category.md).

## Non-Interactive Batch Jobs

Our batch system is based on the **PBS model** [^1], implemented with the **Moab scheduler** [^2] and **Torque resource manager** [^3].

Typically, the user submits a batch script to the batch system. This script specifies, at the very least, how many nodes and cores the job will use, how long the job will run, and the name of the [application](../software/overview.md) to run.

## Sample Batch Scripts

Sample batch scripts for the available [queue types](../infrastructure/resource/category.md) are given below. A common convention is to append the suffix ".pbs" or ".job" or ".sh" to batch scripts.

!!! tip "Template job scripts"
    Inside the [Login Home directory](../infrastructure/login/directories.md) there is a link to "job-script-template" directory that contains template job scripts for different applications. The user can copy template scripts into the job directory, and modify it accordingly.


### Debug queue (D)

This example explains the keywords, and requests 1 node with 2 processors (cores) for 10 minutes.

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

This example requests 1 node, and 18 cores per node, for 10 minutes.

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

This example requests 4 nodes, and 8 cores per node, for 10 minutes.

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

This example requests 1 node, and 18 cores per node, for 10 minutes.

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

This example requests 4 nodes, and 8 tasks per node, for 10 minutes.

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

In order to specify a [project](../jobs/projects.md) that the job should belong to and should be [charged upon](../accounts/payments-charges.md), a `#PBS -A PROJECT_NAME` directive should be used in the job script file. Each user has a default project that jobs are charged on by default.

### Register Jobs in Web Interface

By default, all jobs submitted from command line are registered in the [Web Interface](../ui/overview.md) for user convenience. When jobs are registered in this way, their files become accessible under the [Files Explorer Interface](../jobs/ui/explorer.md) within the corresponding [Job Viewer page](../jobs/ui/viewer.md). 

If the user does not want the job to be shown on the Web Interface, he/she should specify the `#PBS -R n` directive inside the job script file.

## Job Submission, Inspection and Termination

We review the commands necessary for handling job submission within the CLI, once the user has finished editing the Job script, under the [Actions documentation section](actions/overview.md).

## Links

[^1]: [Wikipedia Portable Batch System, Website](https://en.wikipedia.org/wiki/Portable_Batch_System)

[^2]: [Moab Cloud HPC Suite, Official Website](http://www.adaptivecomputing.com/moab-hpc-basic-edition/)

[^3]: [Torque Resource Manager Administrator Guide, Document](http://docs.adaptivecomputing.com/torque/6-1-2/adminGuide/torqueAdminGuide-6.1.2.pdf)
