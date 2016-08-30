<!-- TODO by TB -->
# Simulations

Characteristic properties of materials can be obtained either in experiment or via the application of computational techniques, or *simulations*.

> Simulation is an application of a computational method or technique aimed at extracting a specific property of materials.

Within our product multiple entities related to simulations are used:

- Model
- Method
- Unit
- Workflow
- Job

These are explained below in more details. The diagram illustrates the relationships between the terms in a visual manner:

<br>
<img src="../images/simulation-job-wokflow-unit-explained.png">
<br>

# Jobs

Job is a computational abstraction. It contains a set of [units](#units).
Units formulate a workflow. You can imagine workflow as an entity that defines how a materials simulation should be run: which models, methods application should be employed and the order.


## Job Properties

- Title
- Type: a brief description of a workflow that this job is using
- Created At: date and time of project creation
- Status: one of the statuses explained below
- Owner: creator of a project (by default)
- Actions: available actions applicable to this job - example: clone, delete


## Job Statuses

| Label    |      Meaning  |
|----------|:--------------|
<span class="label label-info">pre-submission</span> | created and saved
<span class="label label-primary">submitted</span> | scheduled for execution
<span class="label label-warning">active</span> | currently running
<span class="label label-success">finished</span> | finished successfully <br>
<span class="label label-danger">error</span> | something is wrong <br>
<span class="label label-default">timeout</span> | exceeded walltime <br>
<span class="label label-default">terminated</span> | terminated by user <br>
