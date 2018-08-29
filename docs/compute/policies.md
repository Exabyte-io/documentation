# Computing Policies

## 1. Overview

  The following services are provided to the Customer starting from the payment date:

   - access to computing resources
   - ongoing support in systems administration
   
Prepaid amount is debited to an account. Per core hour rates are charged against the account balance. Additional core-hours can be purchased at the corresponding rate(s) during the validity period. Unused account balance will be applied toward any future purchases.

## 2. Operations

### 2.1 Overview

Customers have access to out computing resources via web browser and command-line terminal. Computing resources represent a set of servers aggregated into a cluster with a central login node that is used for non-computationally intensive tasks, and multiple compute nodes where more intensive calculations are done. The aggregate maximum capacity of the cluster is varied upon Customer demands, but can be estimated at not less than 10,000 computing cores. Multiple clusters may be deployed at the same time.

### 2.2 Data storage

Data storage is organized in three ways: local or on-the-node (temporary), global or cluster-wise-shared (persistent), and object-storage (long-term) available from the web application. Storage is encrypted at all times.

### 2.3 Workload manager

Cluster has a resource management system. Multiple compute types and compute queues are configured such that users can tune pricing and priority per job. Account balance can be used for all compute types and compute queues.

### 2.4 Compute Types

| Name | Description|
|:------|:------------|
| Ordinary | Standard low latency interconnect (meant for most production tasks) |
| Saving   | Jobs can be suspended and then restarted again based on the current load inside a datacenter (same hardware as “Ordinary”). During peak load times tasks can be redirected to “Ordinary” compute.
| Premium  | Ultra low-latency interconnect (communication-intensive large jobs) |

### 2.5 Compute Queues

| Name    | Usage model | Resource provision mode |
|:--------|:------------|:------------------------|
| Debug   | Test calculations in a nearly interactive manner|  1 extra standby compute node is maintained |
| Regular | Day-to-day submissions at normal priority | 1 compute node is added at a time when new tasks are submitted |
| Fast    | Urgent or high-throughput calculations at higher priority | Multiple compute nodes are added simultaneously when new jobs are submitted |


### 2.6 Charge Policies

| Compute   | Type         | Saving                   | Ordinary                 | Premium      |
| :-------- | :----------- | :-------                 | ----------               | ---------    |
| Queue     |              |                          |                          |              |
| Debug     |              | -                        | core-seconds<sup>1</sup> | core-seconds |
| Regular   |              | node-seconds<sup>2</sup> | node-seconds             | node-seconds |
| Fast      |              | node-hours<sup>3</sup>   | node-hours               | node-hours   |

**Notes**:
    
1. compute time is accumulated in seconds only for the cores occupied by the job, shared use model deployed for compute nodes in the queue.
2. compute time is accumulated in seconds for all cores per compute node, non-shared use model deployed.
3. compute time is accumulated in hours for all cores per compute node, non-shared use model deployed.
