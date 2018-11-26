# Queues

## Name Convention

Queue name consists of 6 parts from which only one part (part 4 enclosed by braces, `{}`) is mandatory and other parts are optional (enclosed by brackets, `[]`).

```
[1][2][3]{4}[5][6]
```

1. Whether queue is GPU-enabled. If yes, queue name starts with `G` letter.

2. GPU type. `P` means [P100](overview/#gpu-types), [V100](overview/#gpu-types) is used if not specified.

3. Number of GPUs per each node, 1 GPU if not specified.

4. Queue [cost category](category.md#cost-categories), D (Debug), O (Ordinary) and S (Saving).

5. Queue [provision mode](category.md#provision-modes), R (Regular) and F (Fast).

6. Number of cores per node. Depends on the cluster if it is not specified.

### Examples

1. **G4OF**: GPU-enabled, V100, 4 GPUs, Ordinary, Fast, 32 cores on AWS - not available on Azure

2. **GPSF**, GPU-enabled, P100, 1 GPU, Saving, Fast, 6 cores on Azure - not available on AWS

3. **OR16**: Ordinary, Regular, 16 cores

4. **OF**: Ordinary, Fast, 36 cores on AWS - 16 cores on Azure

4. **SF+**: Saving, Fast, 36 cores on AWS - not available on Azure, faster CPU compare to SF queue

## Charge Policies

- **core-seconds**: jobs are charged according to the number of core-seconds consumed
- **core-hours**: jobs are charged according to the number of core-hours consumed
