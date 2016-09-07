<!-- by MM -->

# Submission queues

## Overview

Depending on the size and degree of urgency, simulation tasks can be directed to different submission queues to optimize cost/efficiency ratio. We have multiple queues, as explained below:

- **debug (D)**: for small-sized and short debug calculations
    * node cout == 1
    * CPU cout per node <= 4; memory usage per CPU is capped at 2GB
    * jobs are charged according to consumed walltime in seconds
    * number of compute nodes in the queue regulated between 1-10

- **on-demand regular (OR)**: for most regular tasks, with the following rules per job:
    * node cout == 1
    * CPU cout per node <= 36 on cluster-001, 32 on cluster-002, 16 on cluster-003 and cluster-004
    * jobs are charged according to consumed walltime in seconds
    * number of compute nodes in the queue is regulated between 10-100

- **on-demand fast (OF)**: for large-scale tasks, with the following rules per job:
    * node cout < 50
    * CPU cout per node <= 36 on cluster-001, 32 on cluster-002, 16 on cluster-003 and cluster-004
    * jobs in OF queue are charged according to the number of Node-hours consumed, each partial hour is charged as whole
    * number of compute nodes in the queue is regulated between 100-1000

- **saving regular (SR)**: same settings as (OR) above
- **saving fast (SF)**: same settings as (OF) above

NOTE: 1 Node-hour = (36 on cluster-001, 32 on cluster-002, 16 on cluster-003 and cluster-004)  x  1 CPU-hour


## Wait time

Approximate wait times for a single job (unless datacenter capacity is exceeded):

- debug: no wait
- on-demand: 5 min
- saving: 10 min
