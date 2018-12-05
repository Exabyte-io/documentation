# Create New Job

Here, we explain how to assemble the necessary input scripts for [job submission via the CLI](../overview.md) using some pre-defined examples. The reader is referred to the [dedicated Tutorial](../../tutorials/) on this topic for a more comprehensive description and examples on how such input scripts can be customized by the user.

## General Procedure

A new [simulation Job](../../jobs/overview.md) can be created by assembling all necessary **simulation input files**, as well as the **[Batch Script](../batch-scripts/overview.md)** associated with the job, and bringing all such files together under the same [Working folder](../batch-scripts/directories.md).
 
This Working folder has to be located under the [cluster home directory](../../infrastructure/clusters/directories.md) of the [computing cluster](../../infrastructure/clusters/overview.md) being considered for job execution.

!!! note "Choose walltime carefully"
    The [Walltime](../../infrastructure/compute/parameters.md#time-limit) of the simulation is defined in the [Batch Script](../batch-scripts/overview.md) through its corresponding [directive](../batch-scripts/directives.md), and should be chosen carefully for a number of reasons.
    
    1. Jobs that require long walltime will [reserve the corresponding balance](../../accounts/balance.md#reserved-balance), and thus prevent other jobs from starting.
    2. When not enough walltime is allocated, the job may not finish on time, resulting in an erroneous output. 
    3. The user is advised to [submit a support ticket](../../ui/support.md) if a walltime adjustment is needed during the course of a long job execution. Our support staff will do their best to accommodate the necessary desired changes, depending on the current computing load and business hours.

## Job Templates

Users can find our examples of job batch scripts and input files within the **"job-script-template"** folder present inside the [Login Home directory](../../infrastructure/login/directories.md). 

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
