## Job termination

In order to get notified about capacity-based termination of a task in saving queue via email, `#PBS -m abe` and `#PBS -M < email_address >` directives must be set inside the job script file. In addition, our scheduling system automatically restarts terminated jobs and re-submits them into the regular queue. If you do not want your job to be restarted this way, set `#PBS -r n` directive in the job script. A temporary directory for job's intermediate results are created in user's home directory.
