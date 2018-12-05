# Working Directory 

Each job defined via the [Command Line Interface](../../cli/overview.md) (CLI) is associated with a user-defined **Working Directory**, referred to under the `PBS_O_WORKDIR` [environment variable](directives.md#environment-variables). This directory typically contains the [Batch Script](overview.md) for defining the Job, as well as all of the job's corresponding input and output simulation files generated during the course of its execution.

!!!warning "Required location of Working Directory"
    A Job can be [submitted](../actions/submit.md) to a [cluster](../../infrastructure/clusters/overview.md) for its execution only if its corresponding working directory is located somewhere within the [cluster's home directory](../../infrastructure/clusters/directories.md), or under any of its sub-directories. 
