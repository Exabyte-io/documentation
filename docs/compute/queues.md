<!-- by MM -->

## Overview

Depending on the size and degree of urgency, simulation tasks can be directed by user to different submission queues to optimize cost/efficiency ratio. Submission queues have the corresponding [compute levels](overview.md). We have multiple queues, as explained below:

| Name | Meaning | Nodes per job | CPU per node | Charge policy | Max nodes<sup>*</sup> |
|:-----|:--------|--------------:|-------------:|--------------:|----------:|
| D    | debug   | 1             | 4            | exact seconds** | 10
| OR   | on-demand regular   | 1             | 36****            | exact seconds | 10
| OF   | on-demand fast      | &le; 50             | 36****             | whole hours*** | 75
| SR   | saving regular   | 1             | 36****            | exact seconds | 10
| SF   | saving fast      | &le; 50             | 36****             | whole hours*** | 75

<sup>*</sup> maximum number of nodes per single cluster, may be administratively adjusted depending on load

<sup>**</sup> exact seconds = jobs are charged according to consumed walltime in seconds;

<sup>***</sup> whole hours = jobs are charged according to the number of Node-hours consumed, each partial hour is charged as whole

<sup>****</sup> CPU count per node is 36 on cluster-001, 32 on cluster-002 and 16 on cluster-003, cluster-004, and cluster-005


!!! note "What is 1 Node-hour"
    1 Node-hour = (36 on cluster-001, 32 on cluster-002, 16 on cluster-003, cluster-004 and cluster-005)  x  1 CPU-hour


## Wait time

Approximate wait times for a single job to start (unless datacenter capacity is exceeded):

- debug: no wait
- on-demand: 5 min
- saving: 10-15 min
