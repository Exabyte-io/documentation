# Sample Batch Scripts

Sample batch scripts for the available [queue types](../infrastructure/resource/category.md) are given below. A common convention is to append the suffix ".pbs" or ".job" or ".sh" to batch scripts.

!!! tip "Template job scripts"
    Inside the [Login Home directory](../infrastructure/login/directories.md) there is a link to "job-script-template" directory that contains template job scripts for different applications. The user can copy template scripts into the job directory, and modify it accordingly.


## Debug queue (D)

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

## On-demand regular (OR)

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

## On-demand fast (OF)

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


## Saving regular (SR)

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

## Saving fast (SF)

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
