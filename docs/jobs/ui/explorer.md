# Jobs Explorer Interface

The features of Jobs Explorer which make it distinct from the [general case](/entities-general/ui/explorer.md) include the kind of properties that can be displayed under the items list.

The image below shows how Jobs Explorer appears under typical circumstances. The general [entity actions](/entities-general/actions/overview.md) as well as those [specific to Jobs](../actions/overview.md) originate from this interface.

![Jobs Explorer Interface](/images/jobs-explorer.png "Jobs Explorer Interface")

# Status Indicators

An important property present in the items list is the [Status indicator](../status.md) of each listed Job, under the "Status" column highlighted in the above image. 

# Other Job-specific Properties

Additional properties available to be listed in Explorer, which are specific to Jobs, include those ticked in the image below. These options can be selected under the [Columns Selector](/entities-general/ui/explorer.md#columns-selector).

![Jobs Specific Properties](/images/jobs-properties.png "Jobs Specific Properties")

## Application

This option displays the computational [applications](/applications/overview.md) employed within the Job, including their version numbers.

## Cluster - Queue & Cores

Here, the [name and queue](/jobs-designer/compute-tab.md) of the [cluster](/pricing/service-levels.md#clusters-and-premium-hardware) considered for Job execution are shown. The number of nodes and cores in this cluster used for running the Job is also indicated.

## Run & Wait Time

This corresponds to the amount of time that the Job took to finish, and for how long it had to wait in the [queue](/compute/levels-queues.md) of the cluster before being executed.

## Project

The name of the [Project](../projects.md) containing the Job is displayed under this column.
