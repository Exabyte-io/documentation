# Time limit 
 
The first option under the "Time limit" section of the tab allows the user to set the time limit for the calculation, in the format "hh:mm:ss". 

# Cluster choice

Further down this "Compute" tab, under the "Cluster" section, a list of supercomputing clusters available for performing the desired calculation is presented in the corresponding drop-down menu, with the option to visualize the status of each cluster ("See clusters status"). 

The options for submitting the computing job to the task scheduler of the cluster can be found under the section "Queue". In particular, the user is offered the possibility to launch the desired job with three different levels of priority: a "Debug (D)" mode which is especially suited for preliminary tests, an "on-demand fast (OF)" mode for high priority on the scheduler and rapid execution of the job, and finally an "on-demand regular (OR)" mode to obtain regular access to the scheduler. 

Furthermore, the desired number of supercomputing nodes (batches of processors) and the number of cores on each node can be selected, depending on the expected computational costs and requirements of the calculation under consideration. The necessary payments will have to be made as explained [in this page](../../billing/billing-and-payments.md), before the execution of any task can be made possible.

# Advanced Options

Further advanced options are offered in the expandable section at the bottom of the tab, in order to further optimize the parallelization of the calculation over the k-points of the crystal structure, over its band-structure or over the execution of Fast Fourier Transforms (FFT). The novice user will find that these options are normally better left unchanged from their default values. 

# Notifications

Finally, in the "Notifications" section on the right-hand side of the tab interface, the possibility to be notified as a user about the start of the calculation on the supercomputing cluster, about its termination, or about a possible accidental abortion, can be accessed. The user can click on the button corresponding to each type of event to trigger the associated notifications.
