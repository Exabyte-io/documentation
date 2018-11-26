# Queues

## Name Convention

Queue name consists of 6 parts from which 2 parts always exist (4 and 5) and other parts are optional.

```
[1][2][3]{4}{5}[6]
```

1. Whether queue is GPU-enabled. If yes, queue name starts with `G` letter.

2. GPU type. `P` means [P100](overview/#gpu-types), [V100](overview/#gpu-types) is used if not specified.

3. Number of GPUs per each node, 1 GPU if not specified.

4. Queue [resource category](category.md*resource-categories), D (Debug), O (Ordinary) and S (Saving).

5. Queue [provision mode](category.md*provision-modes), R (Regular) and F (Fast).

6. Number of cores per node. Depends on the cluster if it is not specified.

### Examples

1. **G4OF**: GPU-enabled, V100, 4 GPUs, Ordinary, Fast, 32 cores on AWS - not available pn Azure

2. **GPSF**, GPU-enabled, P100, 1 GPU, Saving, Fast, 6 cores on Azure - not available pn AWS

3. **OR16**: Ordinary, Regular, 16 cores

4. **OF**: Ordinary, Fast, 36 cores on AWS - 16 cores on Azure

## Charge Policies

- **core-seconds**: jobs are charged according to the number of core-seconds consumed
- **core-hours**: jobs are charged according to the number of core-hours consumed
