
# Documentation

Welcome to our documentation repository! We aim to provide all the necessary information for you to use our product here. In case you find that something is missing of you are still puzzled after reading this documentation, please <a href="mailto:support@exabyte.io" target="_blank">contact us</a> .

# QuickStart

If you are new to Exabyte and feeling impatient, you can get started by following this tutorial summarizing the
[first steps with Exabyte](tutorials/first-steps.md). You will learn how to create and save your first material and run a simulation that predicts this material's electronic bandstructure.

# Basic concepts

## Projects

We organize user workspace using projects. Project contains a study of a particular material or a set of materials that are related to each other. Projects have a single owner, and can have multiple users that collaborate together.

Here is how the list of projects looks like from within the application.

<br>
<img src="images/list_of_projects.png" width="800">
<br>

You can create a new project by clicking (+) button at the top right corner of the page.

To see the jobs that belong to a project, click on the project's name.


## Jobs

Job is a computational abstraction. It contains set of [units](#units).
Units formulate a workflow. You can imagine workflow as an entity that defines how a materials simulation should be run: which models, methods application should be employed and the order.

### Job Properties

- Title
- Type: a brief description of a workflow that this job is using
- Created At: date and time of project creation
- Status: one of the statuses explained below
- Owner: creator of a project (by default)
- Actions: available actions applicable to this job - example: clone, delete


### Job Statuses

| Label    |      Meaning  |
|----------|:--------------|
<span class="label label-info">pre-submission</span> | created and saved
<span class="label label-primary">submitted</span> | scheduled for execution
<span class="label label-warning">active</span> | currently running
<span class="label label-success">finished</span> | finished successfully <br>
<span class="label label-danger">error</span> | something is wrong <br>
<span class="label label-default">timeout</span> | exceeded walltime <br>
<span class="label label-default">terminated</span> | terminated by user <br>

When you click on one of the Projects you see the list of jobs.

<br>
<img src="images/list_of_jobs.png" width="800">
<br>

You can create a new Job by clicking "New Job" button at the top right corner of the page.

To view the job, click on its name.


## Materials

"Materials" section contains all previously created materials. It is empty initially, however you can start saving your materials during the simulations (jobs), and you can use previously saved materials in your new jobs.

Add more materials by clicking "New Material" button at the top right corner of the page.


## SSH Keys

SSH Keys section contains the your public keys that give you command-line access to our compute platform through secure shell protocol. You can generate ssh keys on your local machine and upload the public one to our compute platform.

More documentation about our compute platform is available [here](cluster/index.md).

A good tutorial on how to create SSH keys can be found [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2).


## Billing

Billing page contains accounting information about your jobs:

- Project: project the job belongs to
- Job: the name of the job
- Processors: number of the processors the job used at runtime
- Invoice Date: Billing record for the job
- Sum($): cost per job in $
- Wall duration: total amount of compute time used by the job (in CPU-hours)

## Settings

Settings section lets one update personal information, system-specific parameters and security settings.

