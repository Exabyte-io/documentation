## Types

We have multiple types of queues that let our users optimize the cost-to-performance ratio.

| Level      | Description                                                                   |
| :--------- | :-----------                                                                  |
| Debug      | Limited compute resources with no-to-little wait time at a cost premium       |
| Ordinary   | Meant for most production tasks, extensive compute resources at the base rate |
| Saving     | Significantly lower rate through utilizing idle compute resources             |


!!! tip "Queue Selection"
    It is advised to use Debug level while prototyping your calculations, Ordinary for mission-critical tasks, and Saving - for restartable runs that can tolerate interruptions (eg. check-pointed relaxation runs).

!!! note "Saving Resources Termination"
    When the data center has increased load, some or all saving resources may be terminated. We attempt restarting the calculations by resubmitting the corresponding job to resource manager queue. At current, no charge for the first whole hour is incurred upon saving resource termination.


## Subtypes

| Name    | Usage model | Resource provision mode |
|:--------|:------------|:------------------------|
| Debug   | Test calculations in a nearly interactive manner|  1 extra standby compute node is maintained |
| Regular | Day-to-day submissions at normal priority | 1 compute node is added at a time when new tasks are submitted |
| Fast    | Urgent or high-throughput calculations at higher priority | Multiple compute nodes are added simultaneously when new jobs are submitted |

## Name Convention

Queue name consists of 6 parts from which 2 parts always exist (4 and 5) and other parts are optional.

```
[1][2][3]{4}{5}[6]
```

1. Whether queue is GPU-enabled. If yes, queue name starts with `G` letter.

2. GPU type. `P` means [P100](overview/#gpu-types), [V100](overview/#gpu-types) if not specified.

3. Number of GPUs per each node, 1 GPU if not specified.

4. Queue type, D (Debug), O (Ordinary) and S (Saving).

5. Queue subtype, R (Regular) and F (Fast).

6. Number of cores per node. Depends on the cluster if it is not specified.

### Examples

1. **G4OF**: GPU-enabled, V100, 4 GPUs, Ordinary, Fast, 32 cores on AWS - not available pn Azure

2. **GPSF**, GPU-enabled, P100, 1 GPU, Saving, Fast, 6 cores on Azure - not available pn AWS

3. **OR16**: Ordinary, Regular, 16 cores

4. **OF**: Ordinary, Regular, 36 cores on AWS - 16 cores on Azure

## Charge Policies

- **core-seconds**: jobs are charged according to the number of core-seconds consumed
- **core-hours**: jobs are charged according to the number of core-hours consumed
