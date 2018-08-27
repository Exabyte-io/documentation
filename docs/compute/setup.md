# Compute setup

The Compute panel allows user to set up the computational parameters for the simulation to be executed.

<!-- TODO: update a visual -->

![Compute Tab](../images/ComputeTab.png "Compute Tab")

# Time limit 
 
The first option under the "Time limit" section of the tab allows the user to set the time limit for the calculation, in the format "hh:mm:ss". 

# Cluster choice

Further down this "Compute" tab, under the "Cluster" section, a list of supercomputing clusters available for performing the desired calculation is presented in the corresponding drop-down menu, with the option to visualize the status of each cluster ("See clusters status"). 

# Queue

The options for submitting the computing job to the task scheduler of the cluster can be found under the section "Queue". In particular, the user is offered the possibility to launch the desired job with three different levels of priority: a "Debug (D)" mode which is especially suited for preliminary tests, an "fast (eg. OF)" mode for high priority on the scheduler and rapid execution of the job, and finally an "regular (eg. OR)" mode to obtain regular access to the scheduler. This is further explained [here](levels-queues.md)

### Time Limit

This value specifies the maximum time limit for the calculation to be run for. The format is `HH:MM:SS` in which H, M and S stand for day, hour, minute and second respectively. Please note that a calculation will be terminated when the runtime exceeds the maximum time specified in this field.

# Nodes / PPN

The desired number of computing nodes and the number of cores on each node (PPN = processors per node) can be selected, depending on the expected computational costs and requirements of the calculation under consideration. The necessary payments will have to be made as explained [in this page](/billing/billing-and-payments.md), before the execution of any task can be made possible.

# Advanced Options

Further advanced options are offered in the expandable section at the bottom of the tab, in order to further optimize the calculation. This section is dependent on the application (see the corresponding application [pages](/applications/overview.md) for more info). Example improvements may include parallelization over the k-points of the crystal structure, over its band-structure or over the execution of Fast Fourier Transforms (FFT). The novice user will find that these options are normally better left unchanged from their default values. 

# Notifications

Finally, in the "Notifications" section on the right-hand side of the tab interface, the possibility to be notified as a user about the start of the calculation on the supercomputing cluster, about its termination, or about a possible accidental abortion, can be accessed. The user can click on the button corresponding to each type of event to trigger the associated notifications.
