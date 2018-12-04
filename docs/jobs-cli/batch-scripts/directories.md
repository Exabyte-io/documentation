# Working Directory 

To each job defined via the [Command Line Interface](../../cli/overview.md) (CLI) corresponds a user-defined **Working Directory**, referred to under the `PBS_O_WORKDIR` [environment variable](directives.md#environment-variables). This directory typically contains the [Batch Script](overview.md) for defining the Job, as well as all of the job's corresponding input and output files generated during the course of its execution.

## Required Location

A Job can be [submitted](../actions/submit.md) to a [cluster](../../infrastructure/clusters/overview.md) for its execution only if its corresponding working directory is located somewhere within the [cluster's home directory](../../infrastructure/clusters/directories.md), or under any of its sub-directories. 
