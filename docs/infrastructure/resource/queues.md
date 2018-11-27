# Queues

Different task scheduling **Queues** are available under each [category](category.md), for accessing the [computational clusters](../clusters/overview.md) and executing [simulation Jobs](../../jobs/overview.md) upon them. These queues afford for the allocation of different amounts of **computational resources** (number of cores).

Cluster-specific list of queues are available for each of the [Amazon Web Service](../clusters/aws.md) and [Azure](../clusters/azure.md) Cloud providers.

Queues can be selected under the Web Interface at the moment of [Job Creation](../../jobs-designer/overview.md) according to the instructions found [here](../compute-settings/ui.md#queue). Similarly, the desired queue can be specified under the [Batch Script](../../jobs-cli/batch-script.md) for the case of [Job submission via the Command Line Interface](../../jobs-cli/overview.md).

## Naming Convention

Queue name consists of 4 main parts as demonstrated below. Only one part, denoted as 2 and enclosed by braces `{}`, is mandatory. Other parts, enclosed by brackets `[]`, are optional.

```regexp
[1a][1b][1c]{2}[3][4]
```

### Explanation

1. GPU-specific concerns:

    a. Whether queue is GPU-enabled. If yes, letter "G" is used.
    b. Type of GPU. `P` means [P100](../clusters/hardware.md#gpu-types). [V100](../clusters/hardware.md#gpu-types) is used by default for GPU-enabled queues otherwise.
    c. Number of GPUs per each node, 1 GPU if not specified.

2. Queue [cost category](category.md#cost-categories): either "D" (Debug), "O" (Ordinary) or "S" (Saving).

3. Queue [provision mode](category.md#provision-modes), R (Regular) and F (Fast).

4. Maximum number of cores per single node. Depends on the cluster and [cloud provider](../clusters/overview.md) if it is not specified.

### Examples

- **G4OF**: GPU-enabled, [V100](../clusters/hardware.md#gpu-types), 4 GPUs, Ordinary, Fast; 32 cores per node on [AWS](../clusters/aws.md) only
- **GPSF**, GPU-enabled, [P100](../clusters/hardware.md#gpu-types), 1 GPU, Saving, Fast, 6 cores per node on [Azure](../clusters/azure.md) only
- **OR16**: Ordinary, Regular, 16 cores per each compute node
- **OF**: Ordinary, Fast; 36 cores per node on [AWS](../clusters/aws.md), 16 cores on [Azure](../clusters/azure.md)
- **SF+**: Saving, Fast; 72 later generation (compared to "SF") cores on [AWS](../clusters/aws.md) only

## Charge Policies

We deploy two charge policies, as explained below:

- **core seconds**: jobs are charged according to the number of core-seconds consumed
- **core hours**: jobs are charged according to the nearest (greater) integer number of core-hours consumed; also referred to as "whole hours" 

The latter is used for queues with [Fast](category.md#provision-modes) provision category. The former is used otherwise.

!!! warning "Be considerate when using queues with core-hours charge policies"
    When tasks are submitted to the queue with "core hours" based charge policy, our accounting system would charge the [account](../../accounts/overview.md) for at least 1 hour of usage of the resource. We advise users to prototype the calculations in other queues and deploy production-ready large-scale runs using queues with "core hours" charge policies. 
