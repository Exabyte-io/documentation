# Compute Parameters

In the present page, we review the different **compute parameters** which can be set under the [user interface](overview.md).

## Time limit 
 
The first option under the "Time limit" section allows the user to specify the maximum time limit for the calculation to be run for. The format is `HH:MM:SS` in which H, M and S stand for day, hour, minute and second respectively. Please note that a calculation will be terminated when the runtime exceeds the maximum time specified in this field.

## Cluster choice

Further down, under the "Cluster" section, a list of [computing clusters](../clusters/overview.md) available for performing the desired calculation is presented in the corresponding drop-down menu, with the option to visualize the status of each cluster ("See clusters status"). 

## Queue

The options for submitting the computing job to the [task scheduler](../resource/overview.md) of the cluster can be found under the section "Queue". 

The user is offered the possibility to launch the desired job with a flexible set of hardware and resource allocation modes per queue. For example, the Debug ("D") queue is especially suited for preliminary tests, "fast" queues (eg. "OF")" are best for high-throughput or multi-node distributed memory runs, and "regular queues" (eg. OR) provide regular access to the scheduler.

## Nodes / PPN

The desired number of computing nodes and the number of cores on each node (PPN = processors per node) can be selected, depending on the expected computational costs and requirements of the calculation under consideration. The necessary payments will have to be made as explained [in this page](../../accounts/balance.md), before the execution of any task can be made possible.

## Advanced Options

Further advanced options are offered in the expandable section at the bottom of the panel, in order to further optimize the calculation. This section is dependent on the application (see the corresponding application [pages](../../software/overview.md) for more information). 

Example improvements may include parallelization over the k-points of the crystal structure, over its band-structure or over the execution of Fast Fourier Transforms (FFT). The novice user will find that these options are normally better left unchanged from their default values. 

## Notifications

Finally, in the "Notifications" section on the right-hand side of the interface, the possibility to be notified as a user about the start of the calculation on the supercomputing cluster, about its termination, or about a possible accidental abortion, can be accessed. The user can click on the button corresponding to [each type of Job status](../../jobs/status.md) to trigger the associated notifications.

Alternatively, all three notification types can be activated simultaneously by clicking the user icon.  
