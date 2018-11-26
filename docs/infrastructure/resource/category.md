# Resource Categories

We have multiple compute categories that let our users optimize the cost-to-performance ratio.

| Level      | Description                                                                   |
| :--------- | :-----------                                                                  |
| Debug      | Limited compute resources with no-to-little wait time at a cost premium       |
| Ordinary   | Meant for most production tasks, extensive compute resources at the base rate |
| Saving     | Significantly lower rate through utilizing idle compute resources             |
| GPU        | GPU-enabled resources                                                         |

!!! tip "Queue Selection"
    It is advised to use Debug level while prototyping your calculations, Ordinary for mission-critical tasks, and Saving - for restartable runs that can tolerate interruptions (eg. check-pointed relaxation runs).

!!! note "Saving Resources Termination"
    When the data center has increased load, some or all saving resources may be terminated. We attempt restarting the calculations by resubmitting the corresponding job to resource manager queue. At current, no charge for the first whole hour is incurred upon saving resource termination.


## Provision Mode

The provision mode specifies the way multiple compute nodes are provisioned.

| Name    | Usage model | Resource provision mode |
|:--------|:------------|:------------------------|
| Debug   | Test calculations in a nearly interactive manner|  1 extra standby compute node is maintained |
| Regular | Day-to-day submissions at normal priority | 1 compute node is added at a time when new tasks are submitted |
| Fast    | Urgent or high-throughput calculations at higher priority | Multiple compute nodes are added simultaneously when new jobs are submitted |
