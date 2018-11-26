# Microsoft Azure Clusters

This page contains information about clusters hosted on Microsoft Azure[^1] and their hardware specifications.

## Clusters

The following table provides information about available clusters on Microsoft Azure cloud computing platform. The latest cluster status can be found on <a href="https://platform.exabyte.io/clusters" target="_blank">Clusters</a> page in web application.

| Name        | Hostname                                          | Location |
| :---:       | :---:                                             | :---:    |
| cluster-007 | master-production-20160630-cluster-007.exabyte.io | East US  |

## Queues

The list of currently enabled queues are given below.

| Name  | Category[^2] | Mode[^3] | Charge Policy[^4] | Price (Cents/Core*Hour) | Nodes/Job | Max Nodes |
| :---: | :---:        | :---:    | :---:             | :---:                   | :---:     | :---:     |
| D     | debug        | debug    | core-seconds      | 40.02                   | 1         | 10        |
| OR    | ordinary     | regular  | core-seconds      | 20.00                   | 1         | 10        |
| OR8   | ordinary     | regular  | core-seconds      | 20.01                   | 1         | 10        |
| OF    | ordinary     | fast     | core-hours        | 22.00                   | &le;50    | 100       |
| SR    | saving       | regular  | core-seconds      | 4.00                    | 1         | 10        |
| SR8   | saving       | regular  | core-seconds      | 4.01                    | 1         | 10        |
| SF    | saving       | fast     | core-hours        | 4.41                    | &le;50    | 100       |
| GPOF  | ordinary     | fast     | core-hours        | 12.22                   | &le;50    | 10        |
| GP2OF | ordinary     | fast     | core-hours        | 12.22                   | &le;50    | 10        |
| GP4OF | ordinary     | fast     | core-hours        | 12.22                   | &le;50    | 10        |

## Hardware Specifications

The following table contains hardware specifications of the above queues.

| Name  | CPU Type[^5] | Cores/Node | GPU Type[^6] | GPU/Node | Memory (GB) | Bandwidth (Gbps) |
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

[^1]: [Microsoft Azure](https://azure.microsoft.com/en-us/)

[^2]: [Queue Resource categories](/infrastructure/resource/category/#resource-categories)

[^3]: [Queue Provision Modes](/infrastructure/resource/category/#provision-modes)

[^4]: [Charge polices](/infrastructure/resource/queues/#charge-policies)

[^5]: [CPU types](overview/#cpu-types)

[^6]: [GPU types](overview/#gpu-types)

[^7]: [Azure high performance compute virtual machines](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes-hpc)

///FOOTNOTES GO HERE///
