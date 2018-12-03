# Jobs via Command Line Interface

The present section of the documentation explains how [simulation Jobs](../jobs/overview.md) can be created and executed via the [Command Line Interface (CLI)](../cli/overview.md) of our platform.

## Important Directories 

Jobs can be submitted to a [cluster](../infrastructure/clusters/overview.md) for their execution only if their corresponding files are present somewhere within the [cluster's home directory](../infrastructure/clusters/directories.md), or in any of its sub-directories. The user should therefore navigate first to this cluster home after entering the [Login Home](../infrastructure/login/directories.md), upon connecting to the CLI.

We explain the directory naming for storing the output files of simulations associated with a certain [Project](../jobs/projects.md) / [Job](../jobs/overview.md) combination in [this page](../infrastructure/clusters#project/job-based-directory-naming).

## Batch script

We explain how to compose **Batch Scripts** (also known as **Job Scripts**), necessary for job submission via CLI, [in this section](batch-scripts/overview.md).

## Accounting

We describe the accounting aspects of Job submission via CLI, such as specifying [Projects](../jobs/projects.md) and inspecting the [Account charges and balance](../accounts/overview.md), here.

## Actions

The actions pertaining to Jobs submission and execution under the CLI are reviewed [in this section](actions/overview.md) of the documentation. Other general actions concerning the CLI, such as the loading of modules, the compilation of new applications or the creation of new python environments, are described [separately](../cli/overview.md).
