<!-- TODO by MH & AM -->

As described [here](cli-job.md), Exabyte offers the capability of running simulations in command-line terminal for power users.
If you have opted for running your simulations through the command-line interface, then you may also enjoy having their results in the web application. Whether your simulations have been already finished or you are about to submit a new job through terminal, we have a solution to manage the output files and results for you.

First, navigate to the terminal interface by clicking on the right sidebar which is obtained by clicking on your username in the upper-right corner of the home page and choosing "Terminal".

<img data-gifffer="/images/LoadTerminal.gif"/>

# Import new job results
If you would like to a submit a new job through command-line terminal and also see the output files along with simulation results in the web application, all you have to do is to follow the exact steps described [here](cli-job.md) and add `#PBS -web` directive to the job script. This optional directive instructs our platform to send back job results to the web application. All you need to do is to submit the job via `qsub` command as before.
Once the job starts executing, you should be able to see the job entry in the web application and monitor its execution.

<img data-gifffer="/images/CLIJobView.gif"/>

!!! Note "Defining project name"
    If the job belongs to a specific project domain, then you should also specify the project name with `#PBS -A project_name` directive.

# Import finished job results
If you have previously submitted a job through the command-line without adding `#PBS -web` directive, there is still a chance to import the results to the web application.

In the terminal, run `exajob_parse -j=/path/to/job/script` to import job results to the web application. You should see the success message after running the mentioned command. Otherwise, there is something wrong with your job or you may have entered wrong path to the job script.

<img data-gifffer="/images/ExaJobParseCommand.gif"/>

!!! Note "Enter full path"
    Please be advised that you should enter the full path to the job script. Otherwise, it cannot locate the job script path.

After running the command, please navigate to the jobs page in the web application. You should be able to see a new entry related to your job there.
