# Jobs Explorer Interface

Jobs Explorer allows users to interact with the jobs. The features of Jobs Explorer that make it distinct from the [general case](/entities-general/ui/explorer.md) include the kind of information that can be displayed under the items list.

The image below shows how Jobs Explorer appears under typical circumstances. The general [entity actions](/entities-general/actions/overview.md) as well as those [specific to Jobs](../actions/overview.md) originate from this interface.

![Jobs Explorer Interface](/images/jobs-explorer.png "Jobs Explorer Interface")

# Status Indicators

An important property present in the items list is the [Status indicator](../status.md) of each listed Job, under the "Status" column highlighted in the above image. 

# Other Specific Properties

Additional columns to be listed in Jobs Explorer specifically include those ticked in the image below and can be selected in the [Columns Selector](/entities-general/ui/explorer.md#columns-selector).

![Jobs Specific Properties](/images/jobs-properties.png "Jobs Specific Properties")

## Application

This option displays the [applications](/applications/overview.md) employed within the [workflow](/workflows/overview.md) used inside the Job, including their version numbers.

## Cluster - Queue & Cores

Here, the [name and queue](/jobs-designer/compute-tab.md) of the [cluster](/pricing/service-levels.md#clusters-and-premium-hardware) where for Job is executed are shown. The number of computational nodes and CPU cores are also indicated.

## Run & Wait Time

This corresponds to the amount of time that the Job took to finish, and for how long it had to wait in the [queue](/compute/levels-queues.md) of the cluster before being executed.

## Project

The name of the [Project](../projects.md) containing the Job is displayed under this column.
