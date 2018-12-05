# Batch Scripts

This page explains the basic framework for the submission of [simulation Jobs](../../jobs/overview.md) via the [Command Line Interface](../../cli/overview.md) (CLI). The corresponding actions for handling the job submission are narrated [separately](../actions/overview.md).

## Batch Mode

Simulation tasks submitted through CLI are expected to be run in **"batch" mode**. Batch jobs are controlled by the so-called **Batch Scripts** (also referred to as **Job Scripts**), which are written by the user and then submitted to the [resource management system](../../infrastructure/resource/overview.md). These scripts specify, at the very least, how many nodes and cores the job will use, how long the job will run, the name of the [application](../../software/overview.md) to be run, and other important [compute parameters](../../infrastructure/compute/parameters.md).

Interactive parallel jobs are not supported on our platform by design. Users are encouraged to prototype calculations on the [login node](../../infrastructure/login/overview.md) (using 2-8 CPU cores with < 1min walltime per user) instead, and submit larger debug tasks into the [Debug queue](../../infrastructure/resource/category.md) designed specifically for testing purposes.

## Implementation

Our batch system is based on the **PBS model** [^1], implemented with the **Moab scheduler** [^2] and **Torque resource manager** [^3]. The actual execution of the parallel job, however, is handled by a special command, called a **job launcher**, which is implemented by a **parallel (MPI) library**. In a generic Linux environment, this utility is often labelled **"mpirun"**.

## General Structure

The general layout structure of Batch Scripts is the object of [this discussion](general-structure.md).

## Resource Manager Directives

[This page](directives.md) contains the list of the most important directives for specifying the allocation of [computing resources](../../infrastructure/resource/overview.md), necessary for the execution of the job under consideration.

## UNIX Commands

Typically, a batch script needs to include a series of UNIX commands for performing such actions as navigating to the working directory of the job being created, loading the required [modules](../../cli/actions/modules.md), and defining the parallel execution of the job under multiple computing cores. The most frequently encountered commands in the context of our batch scripts are narrated [here](commands.md).

## Working Directory

The main "working" directory, which is important in the context of defining Batch Scripts, storing simulation files and submitting jobs via CLI, is described [in this page](directories.md).

## Examples

We provide some examples on how to enter the relevant information about jobs in batch scripts [here](sample-scripts.md).

## Links

[^1]: [Wikipedia Portable Batch System, Website](https://en.wikipedia.org/wiki/Portable_Batch_System)

[^2]: [Moab Cloud HPC Suite, Official Website](http://www.adaptivecomputing.com/moab-hpc-basic-edition/)

[^3]: [Torque Resource Manager Administrator Guide, Document](http://docs.adaptivecomputing.com/torque/6-1-2/adminGuide/torqueAdminGuide-6.1.2.pdf)
