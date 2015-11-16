Submitting jobs on `angstrom.exabyte.io`
---

### Architecture

`angstrom.exabyte.io` currently has a login node that is connected to 3 compute clusters. Each cluster is running a separate instance of queueing and resource management systems, but has access to the same data. `exalist_masters` shows the cluster master nodes that can be accessed via ssh.

The explanation below is the same for each compute cluster.

### Queues overview

We have multiple job routing queues implemented.

- debug (D): for small-sized and short debug calculations
    - node cout == 1
    - CPU cout <= 36
    - number of compute nodes in the queue is 1

- regular: for most regular tasks, new compute resources are added one-by-one

    - on-demand regular (OR), with the following rules per job:
        - node cout == 1
        - CPU cout <= 36
        jobs in OR queue are charged according to consumed walltime in seconds, number of compute nodes in the queue is 10

    - saving regular (SR): same parameters as above

- fast: for large-scale tasks, new compute resources are added in parallel

    - on-demand fast (OF), with the following rules per job:
        - node cout < 50
        - CPU count <= 1800
        jobs in OF queue are charged according to the number of CPU-hours consumed, each partial hour is charged as whole, number of compute nodes in the queue is 50

    - saving fast (SF): same parameters as above

Debug queue is charged at 2x the base rate, on-demand queues are charged at 1x the base price and saving queues are charged at 0.2x the base price.

Approximate waiting times for a single job execution for the queues (dependent on the load):

- debug: no wait (unless queue is fulfilled)
- on-demand: within 5 min
- saving: usually within 15 min (unless datacenter capacity is exceeded)

### Interactive parallel jobs

Interactive parallel jobs are not supported by design. Users are encouraged to prototype calculations on the master node (using 2-8 CPU and <1min walltime per user) instead, and submit larger debug tasks into the debug queue.

---

### Non-interactive batch jobs

Our batch system is based on the PBS model, implemented with the Moab scheduler and Torque resource manager.

Typically, the user submits a batch script to the batch system. This script specifies, at the very least, how many nodes and cores the job will use, how long the job will run, and the name of the application to run.

---

## Sample Batch Scripts

A common convention is to append the suffix ".pbs" or ".job" or ".sh" to batch scripts.

---

### Example Batch Scripts

#### Debug queue (D)

This example explains the keywords and requests 1 node with 8 processors per node for 10 minutes:

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
#                                                            #
# ---------------------------------------------------------- #

#PBS -N job_name
#PBS -l nodes=16
#PBS -l ppn=8
#PBS -q OF
#PBS -j oe
#PBS -l walltime=00:10:00
#PBS -m abe
#PBS -M name@domain.com

cd $PBS_O_WORKDIR
module load <MODULE_NAME>
mpirun -np 128 ./my_executable
```

#### On-demand regular (OR)

This example requests 1 node, and 36 tasks per node, for 10 minutes

```bash
#!/bin/bash

#PBS -N job_name
#PBS -l nodes=1
#PBS -l ppn=36
#PBS -q OR
#PBS -j oe
#PBS -l walltime=00:10:00
#PBS -m abe
#PBS -M name@domain.com

cd $PBS_O_WORKDIR
module load <MODULE_NAME>
mpirun -np 128 ./my_executable
```

#### On-demand fast (OF)

This example requests 16 nodes, and 8 tasks per node, for 10 minutes

```bash
#!/bin/bash

#PBS -N job_name
#PBS -l nodes=16
#PBS -l ppn=8
#PBS -q OF
#PBS -j oe
#PBS -l walltime=00:10:00
#PBS -m abe
#PBS -M name@domain.com

cd $PBS_O_WORKDIR
module load <MODULE_NAME>
mpirun -np 128 ./my_executable
```

### Cost-saving compute

Job submission process to cost-saving queues is identical to on-demand ones, except for the queue names.

#### Saving regular (SR)

This example requests 1 node, and 36 tasks per node, for 10 minutes

```bash
#!/bin/bash

#PBS -N job_name
#PBS -l nodes=1
#PBS -l ppn=36
#PBS -q SR
#PBS -j oe
#PBS -l walltime=00:10:00
#PBS -m abe
#PBS -M name@domain.com

cd $PBS_O_WORKDIR
module load <MODULE_NAME>
mpirun -np 128 ./my_executable
```

#### Saving fast (SF)

This example requests 16 nodes, and 8 tasks per node, for 10 minutes

```bash
#!/bin/bash

#PBS -N job_name
#PBS -l nodes=16
#PBS -l ppn=8
#PBS -q SF
#PBS -j oe
#PBS -l walltime=00:10:00
#PBS -m abe
#PBS -M name@domain.com

cd $PBS_O_WORKDIR
module load <MODULE_NAME>
mpirun -np 128 ./my_executable
```

---

### Cost-saving Compute Termination

Due to the spot price fluctuation, cost-saving compute may be terminated. In order to get notified of cost-saving compute termination via email, the `#PBS -m abe` and `#PBS -M email_address` directives must be set in the job script file. In addition, PBS automatically restarts jobs in case of cost-saving compute termination. If you don not want PBS to restart your jobs, please set `#PBS -r n` directive in the job script file. A temporary directory for job's intermediate results are created in user's home directory when a job is killed or restarted due to cost-saving compute termination.

### Specify Job Project
In order to specify a project that job belongs to and should be charged upon, a `#PBS -A PROJECT_NAME` directive should be used in job script file. Each user has a default project that jobs are charged on by default.

---

## Submit Example

Submit your batch script with the qsub command:

```
qsub my_job.pbs
123456.cluster
```

The qsub command displays the job_id (123456.cluster in the above example). It is important to keep track of your job_id for job tracking and problem resolution.

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
