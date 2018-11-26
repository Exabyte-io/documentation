# Resource Management

The [cluster computational resources](../clusters/overview.md) offered under our [infrastructure](../overview.md) are managed according to a **Resource Management system** [^1] [^2]. Under this system, a set of **Queues** is deployed to allow for the efficient distribution of resources, which are themselves administered by a **task scheduler software** [^3].

When a job is submitted to any of the queues, the cloud scheduler is responsible for provisioning computational nodes and allocating resources on them for the jobs. **Waiting times** might be incurred by the user depending of the availability of computing resources and the priority of the job in the queue.

## Category

We explain the different speed categories [in this page](category.md).

## Queues

Different queues are available under each category, as explained [here](queues.md).

## Links

[^1]: [Wikipedia TORQUE Resource Manager, Website](https://en.wikipedia.org/wiki/TORQUE)

[^2]: [Torque Resource Manager Administrator Guide 9.0.0, Document](http://docs.adaptivecomputing.com/torque/6-0-0/torqueAdminGuide-6.0.0.pdf)

[^3]: [Wikipedia Maui Cluster Scheduler, Website](https://en.wikipedia.org/wiki/Maui_Cluster_Scheduler)
