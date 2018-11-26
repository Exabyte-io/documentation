## Clusters

The following table provides information about available clusters on Microsoft Azure[^1] cloud computing platform. The latest cluster status can be found on <a href="https://platform.exabyte.io/clusters" target="_blank">Clusters</a> page in web application.


| Name        | Hostname                                          | Location |
| :---:       | :---:                                             | :---:    |
| cluster-007 | master-production-20160630-cluster-007.exabyte.io | East US  |

## Queues

The list of currently enabled queues are given below.

| Name  | Type[^2] | Subtype[^3] | Charge Policy[^4] | Price (Cents/Core*Hour) | Nodes/Job | Max Nodes |
| :---: | :---:    | :---:       | :---:             | :---:                   | :---:     | :---:     |
| D     | debug    | debug       | core-seconds      | 40.02                   | 1         | 10        |
| OR    | ordinary | regular     | core-seconds      | 20.00                   | 1         | 10        |
| OR8   | ordinary | regular     | core-seconds      | 20.01                   | 1         | 10        |
| OF    | ordinary | fast        | core-hours        | 22.00                   | &le;50    | 100       |
| SR    | saving   | regular     | core-seconds      | 4.00                    | 1         | 10        |
| SR8   | saving   | regular     | core-seconds      | 4.01                    | 1         | 10        |
| SF    | saving   | fast        | core-hours        | 4.41                    | &le;50    | 100       |
| GPOF  | ordinary | fast        | core-hours        | 12.22                   | &le;50    | 10        |
| GP2OF | ordinary | fast        | core-hours        | 12.22                   | &le;50    | 10        |
| GP4OF | ordinary | fast        | core-hours        | 12.22                   | &le;50    | 10        |

## Hardware Specifications

The following table contains hardware specifications of the above queues.

| Name  | CPU Type[^5] | Cores/Node | GPU Type[^6] | GPU/Node | Memory (GB) | Bandwidth (Gbps) |
| :---: | :---:        | :---:      | :---:        | :---:    | :---:       | :---:            |
| D     | type-1       | 8          | -            | -        | 56          | &le;10           |
| OR    | type-1       | 16         | -            | -        | 112         | 10               |
| OR8   | type-1       | 8          | -            | -        | 56          | &le;10           |
| OF    | type-1       | 16         | -            | -        | 112         | 54.54[^7]        |
| SR    | type-1       | 16         | -            | -        | 112         | 10               |
| SR8   | type-1       | 8          | -            | -        | 56          | &le;10           |
| SF    | type-1       | 16         | -            | -        | 112         | 54.54            |
| GPOF  | type-2       | 6          | type-2       | 1        | 112         | 10               |
| GP2OF | type-2       | 12         | type-2       | 2        | 224         | 10               |
| GP4OF | type-2       | 24         | type-2       | 4        | 448         | 10               |
| GPSF  | type-2       | 6          | type-2       | 1        | 112         | 10               |
| GP2SF | type-2       | 12         | type-2       | 2        | 224         | 10               |
| GP4SF | type-2       | 24         | type-2       | 4        | 448         | 10               |

## Links

[^1]: [Microsoft Azure](https://azure.microsoft.com/en-us/)

[^2]: [Queue types](/infrastructure/resource/queues/#types)

[^3]: [Queue subtypes](/infrastructure/resource/queues/#subtypes)

[^4]: [Charge polices](/infrastructure/resource/queues/#charge-policies)

[^5]: [CPU types](overview/#cpu-types)

[^6]: [GPU types](overview/#gpu-types)

[^7]: [Azure high performance compute virtual machines](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes-hpc)

///FOOTNOTES GO HERE///
