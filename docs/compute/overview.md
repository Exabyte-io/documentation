<!-- by MM -->

# Compute platform

## Compute levels

We have multiple levels of compute:

- Debug
- Regular
- Fast
- Saving

`Debug` level provides a relatively small amount of compute resources immediately with no wait time at an increased cost.

`Regular` level is meant for most production tasks. It provides extensive compute resources at the base rate defined by [subscription level](/billing/accounts-and-billing#pricing).

'Fast' level is meant for large-scale tasks. It provides extensive compute resources with almost no wait time and slightly higher price.

`Saving` compute level is charged at a significantly lower price than Regular, because it is using compute resources that are currently idle. Users need to be aware, however, that cost-saving compute resources may be terminated depending on the load in the data center. More information on this subject is [here](../cli/jobs.md#job-termination)

## Resources

As of Sep, 2016 our major compute and storage systems have:

|Provider  |Total CPU |Total Memory (GB)|Total Disk (GB)|
|:---------|:--------:|:---------------:|:-------------:|
|AWS       |36000     |60000            |Unlimited      |
|Azure     |10000     |20000            |Unlimited      |
|Rackspace |6400      |12000            |Unlimited      |
|Softlayer |3200      |6400             |Unlimited      |


* We provide you with unlimited disk storage space. Elastic File System lets us reach to 8EB (exabytes) of disk storage.

* All nodes are connected together via fast low latency interconnection networks with bandwidth ranging from 1-10 Gbps.

Our resources are all hosted by top best cloud vendors, [Amazon Web Services](http://www.aws.amazon.com), [Microsoft Azure](http://www.azure.microsoft.com), [IBM SoftLayer](http://www.softlayer.com) and [Rackspace](http://www.rackspace.com). The following shows the hardware specification for each cloud vendor.

|Provider  |CPU Count |CPU Type                       |Memory (GB)|Disk (GB)|Bandwidth (Gbps)|
|:---------|:--------:|:-----------------------------:|:---------:|:-------:|:--------------:|
|AWS       |36        |Intel Xeon E5-2666-v3, 2.90GHz |60         |10       |10              |
|Rackspace |32        |Intel Xeon E5-2680-v2, 2.80GHz |60         |50       |5               |
|Azure     |16        |Intel Xeon E5-2673-v3, 2.40GHz |32         |256      |10              |
|Softlayer |16        |Intel Xeon E5-2650-v0, 2.00GHz |32         |25       |1               |

!!! tip "On-Premises Deployment"
    For customers who want to use their on-premises resources instead of cloud resources because of high security concerns, easier access and management or specific hardware and software support, we are ready to deploy our application stack on top of your private resources. Please contact us at support@exabyte.io for more information.
