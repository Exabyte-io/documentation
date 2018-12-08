# Resource Management

The [computational resources](../clusters/overview.md) offered under our [infrastructure](../overview.md) are managed according to a **Resource Management system** [^1]. Under this system, a set of [**Queues**](queues.md) is employed to allow for the efficient distribution of resources, which are themselves administered by a **task scheduler software** [^2].

When a calculation task is submitted to any of the queues, our infrastructure management software provisions the computational nodes and allocates resources on them for the task. Waiting times might be incurred by the user depending of the availability of computing resources and the priority of the task.

## Categories

We explain the different resource categories and their methods of allocation [in this page](category.md).

## Queues

Different queues are available corresponding to the compute categories, as explained [here](queues.md).

## Links

[^1]: [Torque Resource Manager Administrator Guide, Document](http://docs.adaptivecomputing.com/torque/6-1-2/adminGuide/torqueAdminGuide-6.1.2.pdf)

[^2]: [Wikipedia Maui Cluster Scheduler, Website](https://en.wikipedia.org/wiki/Maui_Cluster_Scheduler)
