<!-- TODO by MH -->

You may want more control over the execution flow or run a type of calculation different from anything we have yet implemented. For that purpose we provide access through command-line terminal.

# Command-line terminal

We provide an interface to command line terminal directly through the web. You can view details on setting up your terminal connection and ssh keys [here](/cli/login.md)

To use the terminal interface, open right sidebar and click "Terminal":

<img data-gifffer="/images/LoadTerminal.gif"/>

The data directory where your simulations that have been submitted through the web are under the data/<your_username> sub-directory under your home directory.

Our queuing system is built on top of PBS/Torque and is thus controlled through a batch script. You can find batch script templates under `~/job-script-templates/`.

# Create job

To create a job, we recommend working inside the same sub-directory where all your jobs are submitted from the website. Create a new directory under this sub-directory called `test_job`.

Copy template file from within `~/job-script-templates` directory and rename it as `job.script`. Copy any necessary input files or executables into this directory as well.

To run you will need to edit at least the line within the file that starts with "mpirun" if you want to use a tool other than Quantum ESPRESSO. Directions on how to set the various resource manager variables can be found in [CLI job examples](/cli/jobs.md). The screen shot below shows how to add your username and adjust the number of cores per node to 4.

![Edit Job Script](/images/CreateJobScript.png "Edit Job Script")

![Final Job Script](/images/FinalJobScript.png "Final Job Script")

For a more detailed explaination of the features available using the job.script file, please check out the [jobs](/cli/jobs.md) page. A more complete list of the job.script and environment setting options is available [here](/cli/extra.md).

In addition if you would like to set up your environment in the terminal window to access some of our resources you can see detailed information [here](/cli/modules-environment.md)

You can see the options for choosing your queue to submit the job [here](/compute/queues.md)

# Submit job

Once you have edited the job.script file that you copied in and set up all your simulation input files, then you can submit the command via the "qsub" script. To submit the job simply run the command "qsub job.script". The queueing system will give a message letting you know if the job was accepted.

# Monitor job

If you'd like to check on the status of the job, type "qstat" for a one-time view of the current status of your jobs, or type "watch qstat" for a continuously updated screen showing the status of your jobs. Once your job starts running all the output from the job will be placed in the directory where the qsub command was run from unless you changed the "directory" line within the job.script file.

![Submit Job Script](/images/SubmitJobScript.png "Submit Job Script")

# Links

1. [Command Line Usage Documentation](/cli/overview.md)



