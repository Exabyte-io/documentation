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

| Name                | Level       | Meaning                   | Nodes per job    | Charge policy               | Max nodes<sup>*</sup>  | GPUs per node  |
| :-----------------: | :---------: | :---------------:         | ---------------: | --------------------------: | :--------------------: | :------------: |
| D                   | Debug       | debug                     | 1                | exact seconds<sup>**</sup>  | 10                     | -              |
| OR                  | Ordinary    | Ordinary regular          | 1                | exact seconds               | 10                     | -              |
| OF                  | Ordinary    | Ordinary fast             | &le;50           | whole hours<sup>***</sup>   | 100                    | -              |
| SR                  | Saving      | saving regular            | 1                | exact seconds               | 10                     | -              |
| SF                  | Saving      | saving fast               | &le;50           | whole hours                 | 100                    | -              |
| GOF                 | Ordinary    | GPU-enabled Ordinary fast | &le;50           | whole hours                 | 100                    | 1              |
| 4GOF                | Ordinary    | GPU-enabled Ordinary fast | &le;50           | whole hours                 | 100                    | 4              |
| 8GOF                | Ordinary    | GPU-enabled Ordinary fast | &le;50           | whole hours                 | 100                    | 8              |

Notes:

<sup>*</sup> maximum number of nodes per single cluster, may be administratively adjusted depending on load

<sup>**</sup> exact seconds = jobs are charged according to consumed walltime in seconds;

<sup>***</sup> whole hours = jobs are charged according to the number of Node-hours consumed, each partial hour is charged as whole

## Wait time

Approximate wait times for a single job to start (unless datacenter capacity is exceeded):

- debug: no wait
- on-demand: 5 min
- saving: 10-15 min

## Premium

Premium compute level multiplier is applied based on the underlying compute hardware. We isolate resources by clusters, hence the multiplier will be applied when a premium-level compute cluster is used together with queue-based multipliers.
