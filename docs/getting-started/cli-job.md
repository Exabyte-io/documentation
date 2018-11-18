# Command-line Jobs

You may want more control over the workflow execution or run a type of calculation we have yet to implement. For that purpose we provide access through command-line terminal.

## Command-line terminal

We provide an interface to command line terminal directly through the web. You can view details on setting up your terminal connection and ssh keys [here](/remote-connection/overview.md).

To use the terminal interface, open right sidebar and click "Terminal":

The data directory where your simulations that have been submitted through the web are under the data/<your_username> sub-directory under your home directory.

Our queuing system is built on top of PBS/Torque and is thus controlled through a batch script. You can find batch script templates under `~/job-script-templates/`.

## Create job

### Prepare subdirectory

To create a job, we recommend working inside the same sub-directory where all your jobs are submitted from the website. Create a new directory under this sub-directory (called `test_job`, for example).

Copy template file from within `~/job-script-templates` and rename it as `job.script`. Copy any necessary input files or executables into current directory as well.

### Edit submission script

You may need to edit the submission script if you want to use a tool other the default. Directions on how to set resource manager variables can be found in [CLI job examples](/jobs-cli/overview.md). A comprehensive list of the resource manager options is available [here](/infrastructure/resource/overview.md).

In addition, if you would like to alter runtime environment for the calculation, can may consult [modules environment](/cli/environment.md) section of our documentation.

Lastly, you can see the options for choosing your queue to submit the job [here](/infrastructure/resource/queues.md).

In this tutorial we will proceed with the default submission script template without modification.

## Submit job

As a next step you can submit the scipt for execution using "qsub" resource manager directive: 
 
```bash
 qsub job.script
```
 
 Our resource management system will respond with a message letting you know that job was accepted.

## Monitor job

If you'd like to check on the status of the job, type "qstat" for a one-time view of the current status of your jobs. 

Once your job starts running all the output will be placed in the directory where the qsub command was run from (unless you changed the "directory" line within the job.script file).

## Animation

The animation below demonstrated the above steps in action:

<!-- TODO: use local gif instead -->
<img data-gifffer="https://exabyte.io/img/screencast-1.gif"/>

## Links

1. [Command Line Usage Documentation](/cli/overview.md)



