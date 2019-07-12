# Microsoft Azure

This page contains information about clusters hosted on Microsoft Azure[^1] and their hardware specifications.

## Clusters

The following table provides information about available clusters on Microsoft Azure cloud computing platform. The latest cluster status can be found on <a href="https://platform.exabyte.io/clusters" target="_blank">Clusters</a> page in web application.

| Name        | Hostname                                          | Location |
| :---:       | :---:                                             | :---:    |
| cluster-007 | master-production-20160630-cluster-007.exabyte.io | East US  |

## Queues

The list of currently enabled queues is given below. Price per core hour is shown in relation to the [relative unit price](../../pricing/service-levels.md#comparison-table) and is subject to change at any time. Total number of nodes can be increased upon [request](../../ui/support.md). 

| Name  | Category[^2] | Mode[^3] | Charge Policy[^4] | Price | Max Nodes per Job | Max Nodes Total |
| :---: | :---:        | :---:    | :---:             | :---:                   | :---:     | :---:     |
| D     | debug        | debug    | core-seconds      | 4.002                   | 1         | 10        |
| OR    | ordinary     | regular  | core-seconds      | 2.000                   | 1         | 10        |
| OR8   | ordinary     | regular  | core-seconds      | 2.001                   | 1         | 10        |
| OF    | ordinary     | fast     | core-hours        | 2.200                   | &le;50    | 100       |
| SR    | saving       | regular  | core-seconds      | 0.400                   | 1         | 10        |
| SR8   | saving       | regular  | core-seconds      | 0.401                   | 1         | 10        |
| SF    | saving       | fast     | core-hours        | 0.441                   | &le;50*    | 100       |
| GPOF  | ordinary     | fast     | core-hours        | 6.110                   | &le;10    | 10        |
| GP2OF | ordinary     | fast     | core-hours        | 6.110                   | &le;10    | 10        |
| GP4OF | ordinary     | fast     | core-hours        | 6.110                   | &le;10    | 10        |
| GPSF  | saving       | fast     | core-hours        | 1.222                   | &le;10    | 10        |
| GP2SF | saving       | fast     | core-hours        | 1.222                   | &le;10    | 10        |
| GP4SF | saving       | fast     | core-hours        | 1.222                   | &le;10    | 10        |

* - presently the infrastructure limitations are not allowing for the multi-node communication in SF queue, so only single-node jobs should be attempted (as of July 2019)

## Hardware Specifications

The following table contains hardware specifications for the above queues. 

| Name  | CPU[^5] | Cores per Node | GPU[^6] | GPU per Node | Memory (GB) | Bandwidth (Gbps) |
| :---: | :---:        | :---:      | :---:        | :---:    | :---:       | :---:            |
| D     | c-1          | 8          | -            | -        | 56          | &le;10           |
| OR    | c-1          | 16         | -            | -        | 112         | 10               |
| OR8   | c-1          | 8          | -            | -        | 56          | &le;10           |
| OF    | c-1          | 16         | -            | -        | 112         | 54.54[^7]        |
| SR    | c-1          | 16         | -            | -        | 112         | 10               |
| SR8   | c-1          | 8          | -            | -        | 56          | &le;10           |
| SF    | c-1          | 16         | -            | -        | 112         | 54.54            |
| GPOF  | c-2          | 6          | g-2          | 1        | 112         | 10               |
| GP2OF | c-2          | 12         | g-2          | 2        | 224         | 10               |
| GP4OF | c-2          | 24         | g-2          | 4        | 448         | 10               |
| GPSF  | c-2          | 6          | g-2          | 1        | 112         | 10               |
| GP2SF | c-2          | 12         | g-2          | 2        | 224         | 10               |
| GP4SF | c-2          | 24         | g-2          | 4        | 448         | 10               |

## Links

[^1]: [Microsoft Azure, Website](https://azure.microsoft.com/en-us/)

[^2]: [Queue Cost Categories, Website](../resource/category.md#cost-categories)

[^3]: [Queue Provision Modes, Website](../resource/category.md#provision-modes)

[^4]: [Charge polices, Website](../resource/queues.md#charge-policies)

[^5]: [CPU types, Website](hardware.md#cpu-types)

[^6]: [GPU types, Website](hardware.md#gpu-types)

[^7]: [Azure high performance compute virtual machines, Website](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes-hpc)

///FOOTNOTES GO HERE///
