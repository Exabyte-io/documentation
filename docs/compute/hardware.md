# Hardware Specifications

Our computing resources are currently hosted by trusted vendors: [Amazon Web Services](http://www.aws.amazon.com) and [Microsoft Azure](http://www.azure.microsoft.com). We support [IBM SoftLayer](http://www.softlayer.com) and [Rackspace](http://www.rackspace.com) and can deploy capacity there on a short notice.

The following shows the hardware specification for each vendor.

| Provider               | Core Count | CPU Type                        | Memory (GB) | Disk (GB) | Bandwidth (Gbps) | GPUs per node  |
| :---------             | :--------: | :-----------------------------: | :---------: | :-------: | :--------------: | :------------: |
| AWS                    | 36         | Intel Xeon E5-2666-v3, 2.90GHz  | 60          | 10        | 10               | -              |
| AWS GPU<sup>1</sup>    | 8          | Intel Xeon E5-2686-v4, 2.30GHz  | 61          | 10        | 10               | 1              |
| AWS 4GPUs              | 32         | Intel Xeon E5-2686-v4, 2.30GHz  | 244         | 10        | 10               | 4              |
| AWS 8GPUs              | 64         | Intel Xeon E5-2686-v4, 2.30GHz  | 488         | 10        | 25               | 8              |
| Azure                  | 16         | Intel Xeon E5-2673-v3, 2.40GHz  | 32          | 256       | 10               | -              |
| Azure GPU<sup>2</sup> | 6          | Intel Xeon E5-2690-v4, 2.60GHz  | 112         | 336       | 10               | 1              |
| Azure 2GPUs            | 12         | Intel Xeon E5-2690-v4, 2.60GHz  | 224         | 672       | 10               | 2              |
| Azure 4GPUs            | 24         | Intel Xeon E5-2690-v4, 2.60GHz  | 448         | 1344      | 10               | 4              |
| Azure IB<sup>3</sup> | 16         | Intel Xeon E5-2667-v3, 3.20GHz  | 112         | 1,000     | 40               | -              |

<!-- 
| Rackspace                   | 32         | Intel Xeon E5-2680-v2, 2.80GHz  | 60          | 50        | 5                | -              |
| Softlayer                   | 16         | Intel Xeon E5-2650-v0, 2.00GHz  | 32          | 25        | 1                | -              |
 -->
Notes:

1. [GPU-enabled](https://aws.amazon.com/ec2/instance-types/p3/) computing resources.
2. [GPU-enabled](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes-gpu) computing resources.
3. [Infiniband-enabled](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes-hpc) networking hardware.


# Available Resources

As of Apr, 2018 our major compute and storage systems are as below:

| Provider   | Total cores | Total Memory (GB) | Total Disk (GB) |
| :--------- | :--------:  | :---------------: | :-------------: |
| AWS        | 36,000      | 60,000            | Unlimited**     |
| Azure      | 10,000      | 20,000            | Unlimited**     |


<!--
| Rackspace  | 6,400       | 12,000            | Unlimited**     | 
| Softlayer  | 3,200       | 6,400             | Unlimited**     |
-->

** We provide virtually unlimited disk storage space. Elastically grown file system lets us reach to 8EB (exabytes) of disk storage per single compute cluster.

*** All nodes are connected together via fast low latency interconnection networks with bandwidth ranging from 1-10 Gbps.
