<!-- by AM -->

This page explains how to import the results of a [command-line jobs](cli-job.md) to web application. Whether the jobs have already finished or you are about to be submitted, we have a solution to organize and manage the output files and results.

# Open terminal

First, navigate to command-line terminal by clicking on the right sidebar and choosing "Terminal".

<img data-gifffer="/images/LoadTerminal.gif"/>

# Import new job results

In order to a submit a new job through command-line terminal and view the output files along with simulation results in the web application `#PBS -web` directive should be added to [job submission script](cli-job.md). This directive instructs our software to automatically parse the output of the calculation and send back the results to the web application. After that submit the job via `qsub` command as before.

Once the job starts executing, you should be able to see the job entry in the web application and monitor its execution.

<img data-gifffer="/images/CLIJobView.gif"/>

!!! Note "Defining project name"
    If the job belongs to a specific project, then you should also specify the project name with `#PBS -A project_name` directive.

# Import finished job results

If you have previously submitted a job without adding `#PBS -web` directive, its results can still be imported. In the terminal, run 

```bash 
exajob_parse -j=/path/to/job/script
``` 

You should see a success message after command finishes. Otherwise, there is something wrong with your job or you may have entered a wrong path.

<img data-gifffer="/images/ExaJobParseCommand.gif"/>

!!! Note "Enter full path"
    Please be advised that you should enter the **full** path to the job script..

After running the command, please navigate to the jobs page in the web application. You should be able to see a new entry related to your job there, as it was shown above.
