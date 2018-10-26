# Jobs Explorer Interface

The features of Jobs Explorer which make it distinct from the [general case](/entities-general/ui/explorer.md) include the kind of properties that can be displayed under the items list.

The image below shows how Jobs Explorer appears under typical circumstances. The general [entity actions](/entities-general/actions/overview.md) as well as those [specific to Jobs](../actions/overview.md) originate from this interface.

![Jobs Explorer Interface](/images/jobs-explorer.png "Jobs Explorer Interface")

# Status Indicators

Arguably the most evident property present in the items list is the Status indicator of each listed Job, under the "Status" column highlighted in the above image. The status of a Job can be one of the following possibilities, appearing under its corresponding letter/color label.

| Letter    |  Color      | Meaning        |  Details |
| :-------- |:----------- |:------------- |:------------- |
| P | light blue | Pre-submission | Job has not been submitted to the queue of the cluster yet |
| S | dark blue | Submitted | Job has been submitted to the queue of the cluster, but is not actively running yet |
| A | orange | Active | Job is currently in the process of being executed by the relevant cluster |
| F | green | Finished | Job execution terminated correctly (without errors) following its completion |
| E | black | Error | Job execution terminated as a result of encountering a computational error |
| T |       | Terminated | Job execution terminated as a result of user intervention |
|   |       | Timeout   | Job exceeded allocated time limit |

# Other Job-specific Properties

Additional properties available to be listed in Explorer, which are specific to Jobs, include those ticked in the image below. These options can be selected under the [Columns Selector](/entities-general/ui/explorer.md#Columns-Selector).

![Jobs Specific Properties](/images/jobs-properties.png "Jobs Specific Properties")

## Application

This option displays the computational [applications](/applications/overview.md) employed within the Job, including their version numbers.

## Cluster - Queue & Cores

The [name and queue](/jobs-designer/compute-tab.md) of the cluster considered for Job execution. The number of nodes and cores in this cluster used for running the Job is also indicated.

## Run & Wait Time

The amount of time that the Job took to finish, and for how long it had to wait in the queue before being executed.

## Project

The name of the [Project](../projects.md) containing the Job.
