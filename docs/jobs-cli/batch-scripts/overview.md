# Batch Scripts

This page explains the basic framework for the submission of [simulation Jobs](../jobs/overview.md) via the [Command Line Interface](../cli/overview.md) (CLI). The corresponding actions for handling the job submission are narrated [separately](../actions/overview.md).

## Batch Mode

Simulation tasks submitted through CLI are expected to be run in **"batch" mode**. Batch jobs are controlled by the so-called **Batch Scripts** (also referred to as **Job Scripts**), which are written by the user and then submitted to the [resource management system](../infrastructure/resource/overview.md). These scripts specify, at the very least, how many nodes and cores the job will use, how long the job will run, and the name of the [application](../software/overview.md) to run, as described in the examples contained [in this page](sample-scripts.md).

Interactive parallel jobs are not supported by design. Users are encouraged to prototype calculations on the login node (using 2-8 CPU with < 1min walltime per user) instead, and submit larger debug tasks into the [debug queue](../infrastructure/resource/category.md) designed for testing purposes.

## Implementation

Our batch system is based on the **PBS model** [^1], implemented with the **Moab scheduler** [^2] and **Torque resource manager** [^3]. The actual execution of the parallel job, however, is handled by a special command, called a **job launcher**. In a generic Linux environment, this utility is often labelled **"mpirun"**.

## Examples

We provide some examples on how to enter the relevant information about jobs in batch scripts [here](sample-scripts.md).

## Specify Projects

A special note on how to specify the [project name](../../jobs/projects.md) in batch scripts is provided [here](../accounting.md).

## Links

[^1]: [Wikipedia Portable Batch System, Website](https://en.wikipedia.org/wiki/Portable_Batch_System)

[^2]: [Moab Cloud HPC Suite, Official Website](http://www.adaptivecomputing.com/moab-hpc-basic-edition/)

[^3]: [Torque Resource Manager Administrator Guide, Document](http://docs.adaptivecomputing.com/torque/6-1-2/adminGuide/torqueAdminGuide-6.1.2.pdf)
