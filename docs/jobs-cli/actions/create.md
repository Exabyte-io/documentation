# Create New Job

Here, we explain how to assemble the necessary input scripts for [job submission via the CLI](../overview.md) using some pre-defined examples. The reader is referred to the [dedicated Tutorial](../../tutorials/) on this topic for a more comprehensive description and examples on how such input scripts can be customized by the user.

## General Procedure

A new [simulation Job](../../jobs/overview.md) can be created by assembling all necessary **simulation input files** and the associated **[Batch Script](../batch-scripts/overview.md)** together in the same [Working folder](../batch-scripts/directories.md), which has to be located under the [cluster home directory](../../infrastructure/clusters/directories.md) for the [computing cluster](../../infrastructure/clusters/overview.md) being considered for job execution.

### Importance of Walltime

The user is recommended to be deliberate when setting the **Walltime**, defining the maximum authorized duration of the simulation, through its corresponding [resource management directive](../batch-scripts/directives.md) defined under the [Batch Script](../batch-scripts/overview.md). The reasons why doing this is important include the following.

- Jobs that require long walltime will [reserve the corresponding balance](../../accounts/balance.md#reserved-balance), and thus prevent other jobs from starting.
- When not enough walltime is allocated, the job may not finish on time, resulting in an erroneous output. 
- The user is advised to [submit a support ticket](../../ui/support.md) if a walltime adjustment is needed during the course of a long job execution. Our support staff will do their best to accommodate the necessary desired changes, depending on the current computing load and business hours.

## Pre-configured Submit Scripts

The user can find our pre-configured job script template examples and input files within the **"job-script-template"** folder present inside the [Login Home directory](../../infrastructure/login/directories.md). 

Below are example commands needed to copy and run one of these template examples with the [Quantum ESPRESSO](../../software/modeling/quantum-espresso.md) modeling application, contained in the `espresso` sub-directory inside `job_script_templates`.

```bash
# make temporary directory
cd && mkdir -p job-examples/
# copy example files
cd job-examples/ && cp -r ~/job_script_templates/espresso .
# submit for execution
cd espresso && qsub job.pbs
```

The above case [submits](submit.md) the sample Quantum ESPRESSO job into the [queue](../../infrastructure/resource/queues.md) of the [resource manager](../../infrastructure/resource/overview.md) for scheduling its execution. You can view its status with the `qstat` command described [here](check-status.md).
