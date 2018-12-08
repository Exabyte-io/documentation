# Sample Batch Scripts

Examples of batch scripts for a few of the [queue types](../../infrastructure/resource/queues.md) available on our platform are given throughout the present page. The reader is referred to the documentation pages explaining the [Resource Manager Directives](directives.md) and [environment modules](../../cli/modules.md) for the explanation of the batch script contents presented herein.

!!!tip "Template job scripts"
    [Job templates](../../data-on-disk/directories.md#job-script-templates) directory that contains template job scripts for different [applications](../../software/applications.md).

## Debug queue (D)

This example requests 1 node with 2 processors (cores) for 10 minutes, in the Debug Queue for a sample [Quantum ESPRESSO](../../software/modeling/quantum-espresso.md) run.

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
module load espresso
mpirun -np $PBS_NP pw.x -in pw.input
```

## On-demand regular (OR)

This example requests 1 node and 16 cores for 10 minutes, on the OR [queue](../../infrastructure/resource/queues.md) for a sample [VASP](../../software/modeling/quantum-espresso.md) calculation.

```bash
#!/bin/bash

#PBS -N job_name
#PBS -l nodes=1
#PBS -l ppn=16
#PBS -q OR
#PBS -j oe
#PBS -l walltime=00:10:00
#PBS -m abe
#PBS -M name@domain.com

cd $PBS_O_WORKDIR
module load vasp
mpirun -np $PBS_NP vasp
```
