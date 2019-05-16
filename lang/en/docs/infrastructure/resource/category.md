# Resource Categories

This page explains different classifications that are combined together to form the queues.

## Hardware Classes

The hardware class specifies the type of hardware being used underneath which is either GPU-enabled or CPU-only at the moment.  

| Class       | Description           |
| :---------  | :-----------          |
| CPU-only    | CPU-only resources    |
| GPU-enabled | GPU-enabled resources |

!!! note "Enhance hardware"
    Queues ended with `+` letter (OF+) use an enhanced version (new generation) of the hardware compare to the original queue (OF).

## Cost Categories

There are multiple cost categories that let users optimize the cost-to-performance ratio.

| Category   | Description                                                                   |
| :--------- | :-----------                                                                  |
| Debug      | Limited compute resources with no-to-little wait time at a cost premium       |
| Ordinary   | Meant for most production tasks, extensive compute resources at the base rate |
| Saving     | Significantly lower rate through utilizing idle compute resources             |

!!! tip "Queue Selection"
    It is advised to use Debug category while prototyping your calculations, Ordinary for mission-critical tasks, and Saving - for restartable runs that can tolerate interruptions (eg. check-pointed relaxation runs).

!!! note "Saving Resources Termination"
    When the data center has increased load, some or all saving resources may be terminated. We attempt restarting the calculations by resubmitting the corresponding job to resource manager queue. At current, no charge for the first/last whole hour is incurred upon saving resource termination, and the original time limit is re-applied to the restarted job (thus the overall time limit can be longer than originally set).

## Provision Modes

The provision mode specifies the way compute nodes are provisioned.

| Mode     | Description                                                                 |
| :---:    | :---:                                                                       |
| Debug    | 1 extra standby compute node is maintained                                  |
| Regular  | 1 compute node is added at a time when new jobs are submitted               |
| Fast     | Multiple compute nodes are added simultaneously when new jobs are submitted |
