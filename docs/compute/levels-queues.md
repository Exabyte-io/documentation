# Levels

We have multiple levels of compute that let our users optimize the cost-to-performance ratio.

|Level     |Description | Charge factor|
|:---------|:-----------|:-------------|
| Debug    | limited compute resources with no-to-little wait time at a cost premium       |2.0
| Ordinary | meant for most production tasks, extensive compute resources at the base rate  |1.0
| Saving   | significantly lower rate through utilizing idle compute resources; compute resources may be terminated at any time depending on the load in the data center   |0.2
| Premium  | premium-quality resources (eg. low-latency interconnect)   | 2.7
| GPU      | GPU resources   | 8.8

It is advised to use Debug level while prototyping your calculations, Ordinary for mission-critical tasks, and Saving - for restartable runs that can tolerate interruptions (eg. check-pointed relaxation runs).

> &quot;Saving&quot; compute level and compute resources termination
> 
> The concept of saving resources is very similar to the spot-based instances introduced by [AWS](https://aws.amazon.com/ec2/spot/). When the datacenter has increased load, some or all saving compute servers may be terminated. We attempt restarting the calculations by resubmitting the corresponding job to resource manager queue. At current, no charge for the first whole hour is incurred upon compute resource termination. More information available [here](../cli/jobs.md#job-termination)

# Queues

Depending on the size and degree of urgency, simulation tasks can be directed by user to different submission queues to optimize cost/efficiency ratio.

| Name                | Level       | Meaning                   | Nodes/job        | Charge policy               | Max nodes<sup>1</sup>  | Cores/Node      | GPU/Node       |
| :-----------------: | :---------: | :---------------:         | ---------------: | --------------------------: | :--------------------: | :------------:  | :------------: |
| D                   | Debug       | debug                     | 1                | core-seconds<sup>2</sup>    | 10                     | 8               | -              |
| OR                  | Ordinary    | Ordinary regular          | 1                | node-seconds<sup>3</sup>    | 10                     | MAX<sup>4</sup> | -              |
| OR4                 | Ordinary    | Ordinary regular          | 1                | node-seconds                | 10                     | 4               | -              |
| OR8                 | Ordinary    | Ordinary regular          | 1                | node-seconds                | 10                     | 8               | -              |
| OR16                | Ordinary    | Ordinary regular          | 1                | node-seconds                | 10                     | 16              | -              |
| OF                  | Ordinary    | Ordinary fast             | &le;50           | node-hours<sup>5</sup>      | 100                    | MAX             | -              |
| SR                  | Saving      | saving regular            | 1                | node-seconds                | 10                     | MAX             | -              |
| SR4                 | Saving      | saving regular            | 1                | node-seconds                | 10                     | 4               | -              |
| SR8                 | Saving      | saving regular            | 1                | node-seconds                | 10                     | 8               | -              |
| SR16                | Saving      | saving regular            | 1                | node-seconds                | 10                     | 16              | -              |
| SF                  | Saving      | saving fast               | &le;50           | node-hours                  | 100                    | MAX             | -              |
| GOF                 | Ordinary    | GPU-enabled ordinary fast | &le;50           | node-hours                  | 100                    | MAX             | 1              |
| G4OF                | Ordinary    | GPU-enabled ordinary fast | &le;50           | node-hours                  | 100                    | MAX             | 4              |
| G8OF                | Ordinary    | GPU-enabled ordinary fast | &le;50           | node-hours                  | 100                    | MAX             | 8              |

**Notes**:

1. maximum number per single cluster, may be administratively adjusted depending on load
2. jobs are charged according to the number of core-seconds consumed
3. maximum number of cores per node depends on the cluster and is shown in platform [here](https://platform.exabyte.io/clusters)
4. jobs are charged according to the number of node-seconds consumed
5. charged according to the number of whole (integer) node hours consumed



## Wait time

Approximate wait times for a single job to start (unless datacenter capacity is exceeded):

- debug: no wait
- on-demand: 5 min
- saving: 10-15 min

## Premium

Premium compute level multiplier is applied based on the underlying compute hardware. We isolate resources by clusters, hence the multiplier will be applied when a premium-level compute cluster is used together with queue-based multipliers.
