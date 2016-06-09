# Submission queues

## Overview

Depending on the size and degree of urgency, simulation tasks can be directed to different submission queues to optimize cost/efficiency ratio. We have multiple queues, as explained below:

- **debug (D)**: for small-sized and short debug calculations
    * node cout == 1
    * CPU cout <= 4; memory usage per CPU is capped at 1GB
    * jobs are charged according to consumed walltime in seconds
    * number of compute nodes in the queue regulated between 1-10

- **on-demand regular (OR)**: for most regular tasks, with the following rules per job:
    * node cout == 1
    * CPU cout <= 36
    * jobs are charged according to consumed walltime in seconds
    * number of compute nodes in the queue is regulated between 10-100

- **on-demand fast (OF)**: for large-scale tasks, with the following rules per job:
    * node cout < 50
    * CPU count <= 1800 (total)
    * jobs in OF queue are charged according to the number of Node-hours consumed, each partial hour is charged as whole
    * number of compute nodes in the queue is regulated between 100-1000

- **saving regular (SR)**: same settings as (OR) above
- **saving fast (SF)**: same settings as (OF) above

NOTE: 1 Node-hour = CPU count per node  x  1 CPU-hour


## Wait time

Approximate wait times for a single job:

- debug queue: no wait
- on-demand: 5 min
- saving: 15 min (unless datacenter capacity is exceeded)
