# Import Command Line Jobs to Web Interface

The present tutorial page explains how to import the results of a [job](../../jobs-cli/overview.md) run via [command-line interface](../../cli/overview.md) to the main [Web Interface](../../ui/overview.md) of our platform. Whether the jobs have already finished or are about to be submitted, we have a solution to organize and manage their output files and results.

When this feature is employed, the user can directly see the job output files, as well as the following properties automatically extracted and available for analysis in the web interface.

* Number of iterations
* Total energy
* Fermi energy
* Pressure
* Atomic forces
* Total forces
* Stress tensor
* Total energy contributions

We use the content of the [job submission script file](../../jobs-cli/batch-scripts/overview.md) in order to collect job information and create an entry for it inside the web interface. Currently, only simple job scripts containing a single [execution command](../../jobs-cli/batch-scripts/general-structure.md#4.-commands) are supported. Hence, make sure that the script's content is properly formatted and straightforward. 

Below, the reader can find a [sample job script file](../../jobs-cli/batch-scripts/general-structure.md) for running a [VASP](../../software-directory/modeling/vasp/overview.md) simulation that can be used as template.

```bash
#!/bin/bash

#PBS -R y
#PBS -N job_name
#PBS -l nodes=1
#PBS -l ppn=1
#PBS -q D
#PBS -j oe
#PBS -l walltime=00:10:00
#PBS -m abe
#PBS -M name@domain.com

cd $PBS_O_WORKDIR
module load vasp/535-g-485-ompi-110
mpirun -np 4 vasp > vasp.log
```

!!!note "Simple job scripts"
    Please avoid using complex formatting and extra indentations or spacing in the job script.

## Open Web Terminal

First, [navigate](../../remote-connection/actions/open-terminal.md) to the [Web Terminal](../../remote-connection/web-terminal.md) for accessing the [command-line interface](../../cli/overview.md) of our platform.

## Import New Job Results

In order to a submit a new job through [command-line interface](../../cli/overview.md), and then view the output files along with simulation results under the [Web Interface](../../ui/overview.md), the `#PBS -R y` [directive](../../jobs-cli/batch-scripts/directives.md) should be added to the [job submission script](../../jobs-cli/batch-scripts/overview.md) (it is enabled by default). This directive instructs our software to automatically parse the output of the calculation, and send back the results to the web interface. After adding this directive, the job can then be [submitted](../../jobs-cli/actions/submit.md) as usual.

Once the job starts executing, you should be able to see the job entry in the web interface under [Jobs Explorer](../../jobs/ui/explorer.md), and thus monitor the [status](../../jobs/status.md) of its execution.

This feature can conversely be disabled by inserting the `#PBS -R n` directive in the [job submission script](../../jobs-cli/batch-scripts/overview.md).

!!!note "Defining project name"
    If the job belongs to a specific [project](../../jobs/projects.md), then the project name should also be specified with the `#PBS -A project_name` [directive](../../jobs-cli/batch-scripts/directives.md) within the [job submission script](../../jobs-cli/batch-scripts/overview.md).

## Import Finished Job Results

If a job was previously submitted and was not set to be registered under the web interface, its results can still be imported into web interface. Under the [command-line interface](../../cli/overview.md), the following command should be run.

```bash
exajob_parse -j=/path/to/job/script
```

The user should then see a success message appearing after the command finishes its execution. Otherwise, there could be an error in the job execution, or the wrong path may have been entered.

!!!note "Enter full path"
    Please be advised that the **full** path to the job script should be entered in the above command.

After running the command, the user should then navigate to the [Jobs Explorer Interface](../../jobs/ui/explorer.md). He/she should consequently be able to notice a new entry added there related to the job.

## Animation 

In the below video, we first navigate to a directory under the [command-line interface](../../cli/overview.md) where we have copied the contents of the [VASP template Job](../../jobs-cli/batch-scripts/directories.md#job-templates). Here, we edit the [job submission script](../../jobs-cli/batch-scripts/overview.md) to insert the aforementioned `#PBS -R y` [directive](../../jobs-cli/batch-scripts/directives.md) for completeness, even though as explained earlier this directive is already enabled by default.
 
This allows us to monitor the job [status](../../jobs/status.md) under [Jobs Explorer](../../jobs/ui/explorer.md) in [Web Interface](../../ui/overview.md), which we inspect towards the end of the animation.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/p7ex0V0husY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
