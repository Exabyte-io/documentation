<!-- by MM -->

This page describes how to set up compute parameters for a job. It is assumed that you've already created a project and have started creating a job inside it. Job wizard has 3 main tabs, MATERIAL, WORKFLOW and COMPUTE. MATERIAL tab lets you create and save materials for future use. The default structure corresponds to Silicon in face-centered cubic configuration. We will leave it so. Simulations usually have multiple steps that need to be executed in a certain order. This step sequence is called a "Workflow". By default the first workflow - "Bandstructure" - is selected. One can modify the input files for each part of the calculation, available under input tabs. One can also customize the workflow by adding and deleting individual "Units" by adding and deleting the tabs containing input files. We will leave parameters at their default values here again. These steps are explained in more details in [here](https://docs.exabyte.io/tutorials/quickstart).

COMPUTE tab lets you set up the compute parameters.

![Compute Tab](../images/ComputeTab.png "Compute Tab")


### Time Limit

This value specifies the maximum time limit for your calculation to be run for. The format is DD:HH:MM:SS in which D, H, M and S stand for day, hour, minute and second respectively. Please note that your calculation will be stopped if the calculation runtime is more than the maximum time specified in this field. The default time limit is 5 minutes (00:05:00).

### Queue

Depending on the size and degree of urgency, simulation tasks can be directed to different submission queues to optimize cost/efficiency ratio. We have multiple queues, as explained in [here](../compute/queues). The number of nodes and number of CPUs (cores) specifies the degree of parallelism. Increasing the number of nodes and cores allocated to a job accelerates calculation for materials with large unit cells, for example.

### Notifications

This options lets you get notified on certain events, including job start, abort and end notifications. You can select who will be notified when calculation is started, aborted or ended. By default an email is sent to the email address associated with your account.

### Advanced Options

There are multiple data centers with different specifications that you can submit your job to. When selecting the data center you should consider the current load on each data center. This information is available on Load page located in left hand sidebar.

![Data Centers Load](../images/DataCentersLoad.png "Data Centers Load")
