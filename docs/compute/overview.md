<!-- by MM -->

## Compute levels

We have multiple levels of compute that let users diversify and optimize the cost-to-performance ratio.

|Level     |Description | Charge factor|
|:---------|:-----------|:-------------|
|`Debug`     |provides limited compute resources with no-to-little wait time at a cost premium       |2.0
|`On-demand` | is meant for most production tasks, provides extensive compute resources at the base rate  |1.0
|`Saving`    | provides significantly lower rate by utilizing currently idle compute resources; compute resources may be terminated at any time depending on the load in the data center   |0.2

It is advised to use Debug level while prototyping your calculations, On-demand for mission-critical tasks, and Saving - for restartable runs that can tolerate interruptions (eg. check-pointed relaxation runs).

!!! note "&quot;Saving&quot; compute level and compute resources termination"
    The concept of saving resources is very similar to the spot-based instances introduced by [AWS](https://aws.amazon.com/ec2/spot/). When the datacenter has increased load, some or all saving compute servers may be terminated. We attempt restarting the calculations by resubmitting the corresponding job to resource manager queue. At current, no charge for the first whole hour is incurred upon compute resource termination. More information available [here](../cli/jobs.md#job-termination)

## Platform Architecture

Our product is build out of multiple microservices that together form a distributed web application deployable both on public- and private cloud infrastructure. We aggregate together multiple computing clusters that in turn can be deployed in shared- and single-occupancy modes depending on customer preferences and data restrictions. The architecture diagram below demonstrates the basics:

![Service Levels](/images/Architecture.png "Architecture diagram")

## Hardware Specifications

Our public cloud resources are all hosted by trusted vendors: [Amazon Web Services](http://www.aws.amazon.com), [Microsoft Azure](http://www.azure.microsoft.com), [IBM SoftLayer](http://www.softlayer.com) and [Rackspace](http://www.rackspace.com). The following shows the hardware specification for each vendor.

|Provider  |CPU Count |CPU Type                       |Memory (GB)|Disk (GB)|Bandwidth (Gbps)|
|:---------|:--------:|:-----------------------------:|:---------:|:-------:|:--------------:|
|AWS       |36        |Intel Xeon E5-2666-v3, 2.90GHz |60         |10       |10              |
|Rackspace |32        |Intel Xeon E5-2680-v2, 2.80GHz |60         |50       |5               |
|Azure     |16        |Intel Xeon E5-2673-v3, 2.40GHz |32         |256      |10              |
|Softlayer |16        |Intel Xeon E5-2650-v0, 2.00GHz |32         |25       |1               |

!!! tip "On-Premises Deployment"
    For customers who want to use their on-premises resources instead of cloud resources because of high security concerns, easier access and management or specific hardware and software support, we are ready to deploy our application stack on top of your private resources. Please contact us at support@exabyte.io for more information.


## Available Resources

As of Sep, 2016 our major compute and storage systems have:

|Provider  |Total CPU |Total Memory (GB)|Total Disk (GB)|
|:---------|:--------:|:---------------:|:-------------:|
|AWS       |36,000     |60,000            |Unlimited**      |
|Azure     |10,000     |20,000            |Unlimited**      |
|Rackspace |6,400      |12,000            |Unlimited**      |
|Softlayer |3,200      |6,400             |Unlimited**      |


** We provide virtually unlimited disk storage space. Elastically grown file system lets us reach to 8EB (exabytes) of disk storage per single compute cluster.

*** All nodes are connected together via fast low latency interconnection networks with bandwidth ranging from 1-10 Gbps.
