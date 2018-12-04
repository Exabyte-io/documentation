# Sample Batch Scripts

Examples of batch scripts for the [queue types](../infrastructure/resource/category.md) available on our platform are given throughout the present page. The reader is referred to the documentation pages explaining the [Resource Manager Directives](directives.md) and [UNIX Commands](commands.md) respectively for an explanation of the batch script contents presented herein.

!!!tip "Template job scripts"
    Inside the [Login Home directory](../infrastructure/login/directories.md) there is a link to the **"job-script-template"** directory that contains template job scripts examples for different [applications](../../software/applications.md) offered on our platform. The user can copy any template script contained there into the corresponding job directory, and modify it accordingly based on the job's requirements.

## Debug queue (D)

This example requests 1 node with 2 processors (cores) for 10 minutes.

```bash
#!/bin/bash

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
