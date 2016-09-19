<!-- TODO by MH - finish tutorial -->

Our product provides you with a quick and easy way to set up custom simulation methods. Our focus is to automate as much of this functionality as possible, but it is always possible that you may want more control over the execution flow or run a type of calculation different from anything we have yet implemented.  Our focus is to enable as much of this as possible through the web interface, but this may not be possible yet in all cases and some experienced users may be more comfortable submitting their simulations directly.

# Command-line terminal

We provide a interface to a terminal command line window directly through the web to enable this.  This is also the preferred method of execution for a software tool that we have not yet implemented in our automated framework.

To use the terminal interface, click on the right sidebar which is obtained by clicking on your username in the upper-right corner of the home page.

![Right Sidebar](../images/RightSidebar.png "Right Sidebar")

One of the options in this side bar is "Terminal".

![Right Sidebar->Terminal](../images/StartTerminal.png "Right Sidebar->Terminal")

After clicking on "Terminal" an overlay will appear filling up your browser window with a text based terminal emulator called Guacamole.

![Terminal Overlay](../images/LogInToTerminal.png "Terminal Overlay")

The data directory where your simulations that have been submitted through the web are under the data/<your_username> sub-directory under your home directory.

Our queuing system is a variant of PBS and is controlled through a script called job.script.  You can find a template of this script linked to your home directory under ~/job_script.template

# Create first terminal job

To submit a job, we recommend working inside the same sub-directory where all your jobs are submitted from the website.  Create a new directory under this sub-directory called first_terminal_test.

Copying in the job.script template file for submission and any necessary input files or executables into this directory as well.  To run you will need to edit at least the line within the file that starts with "mpirun".  The directions on how to set the various PBS related variables are here.  The template version of the script will submit a job to our on-demand regular queue using 2 cores on 1 machine and have a maximum run-time of 5 minutes.  It also will name any output files with a pre-fix of "".

# Submit first terminal job

Once you have edited the job.script file that you copied in and set up all your simulation input files, then you can submit the command via the "qsub" script.  To submit the job simply run the command "qsub job.script".  The queueing system will give a message letting you know if the job was accepted.

# Monitoring first terminal job

If you'd like to check on the status of the job, type "qstat" for a one-time view of the current status of your jobs, or type "watch qstat" for a continuously updated screen showing the status of your jobs.  Once your job starts running all the output from the job will be placed in the directory where the qsub command was run from unless you changed the "directory" line within the job.script file.




