# Hardware Specifications

Our computing resources are currently hosted by trusted vendors: [Amazon Web Services](aws.md) and [Microsoft Azure](azure.md). 
We support IBM SoftLayer[^1] and Rackspace[^2] and can deploy capacity there on a short notice.

The following shows the CPU and GPU hardware specification on aforementioned vendors.

## CPU Types

The following table shows different types of CPUs the compute nodes are provisioned with.

| Name  | Type                      | Processor Base Frequency (GHz) |
| :---: | :---:                     | :---:                          |
| c-1   | Intel Xeon E5-2667-v3[^3] | 3.20                           |
| c-2   | Intel Xeon E5-2690-v4[^4] | 2.60                           |
| c-3   | Intel Xeon E5-2666-v3[^5] | 2.90                           |
| c-4   | Intel Xeon E5-2686-v4[^6] | 2.30                           |

## GPU Types

The following table shows different types of GPUs the GPU-enabled compute nodes are provisioned with.

| Name  | Type            |
| :---: | :---:           |
| g-1   | NVIDIA V100[^7] |
| g-2   | NVIDIA P100[^8] |


## Available Resources

As of Apr, 2018 our major compute and storage systems are as below. We provide virtually unlimited disk storage space. 
Elastically grown file system lets us reach to 8EB (exabytes) of disk storage per single compute cluster.

| Provider   | Total cores | Total Memory (GB) | Total Disk (GB) |
| :--------- | :--------:  | :---------------: | :-------------: |
| AWS        | 36,000      | 60,000            | Unlimited       |
| Azure      | 10,000      | 20,000            | Unlimited       |

## Links

[^1]: [IBM SoftLayer, official website](http://www.softlayer.com)

[^2]: [Rackspace, official website](http://www.rackspace.com)

[^3]: [Intel Xeon Processor E5-2667 v3](https://ark.intel.com/products/83361/Intel-Xeon-Processor-E5-2667-v3-20M-Cache-3-20-GHz-)

[^4]: [Intel Xeon Processor E5-2690 v4](https://ark.intel.com/products/91770/Intel-Xeon-Processor-E5-2690-v4-35M-Cache-2-60-GHz-)

[^5]: [Amazon C4 instances](https://aws.amazon.com/ec2/instance-types/)

[^6]: [Amazon P3 instances](https://aws.amazon.com/ec2/instance-types/)

[^7]: [NVIDIA TESLA V100 ](https://www.nvidia.com/en-us/data-center/tesla-v100/)

[^8]: [NVIDIA TESLA P100 ](https://www.nvidia.com/en-us/data-center/tesla-p100/)

///FOOTNOTES GO HERE///
