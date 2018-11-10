# Clusters

The following table provides information about available clusters on [Microsoft Azure](#Links) cloud computing platform. The latest cluster status can be found on [clusters](https://platform.exabyte.io/clusters) page in web application.


| Name        | Hostname                                          | Location |
| :---:       | :---:                                             | :---:    |
| cluster-007 | master-production-20160630-cluster-007.exabyte.io | East US  |

# Queues

The list of currently enabled queues are given below.

| Name  | Type<sup>1</sup> | Subtype<sup>2</sup> | Nodes/Job | Charge Policy<sup>3</sup> | Max Nodes | Price (Cents/Core*Hour) |
| :---: | :---:            | :---:               | :---:     | :---:                     | :---:     | :---:                   |
| D     | debug            | debug               | 1         | core-seconds              | 10        | 40.02                   |
| OR    | ordinary         | regular             | 1         | core-seconds              | 10        | 20.00                   |
| OR8   | ordinary         | regular             | 1         | core-seconds              | 10        | 20.01                   |
| OF    | ordinary         | fast                | &le;50    | core-hours                | 100       | 22.00                   |
| SR    | saving           | regular             | 1         | core-seconds              | 10        | 04.00                   |
| SR8   | saving           | regular             | 1         | core-seconds              | 10        | 04.01                   |
| SF    | saving           | fast                | &le;50    | core-hours                | 100       | 04.41                   |
| GPOF  | ordinary         | fast                | &le;50    | core-hours                | 10        | 12.22                   |
| GP2OF | ordinary         | fast                | &le;50    | core-hours                | 10        | 12.22                   |
| GP4OF | ordinary         | fast                | &le;50    | core-hours                | 10        | 12.22                   |


**Notes**:

1. [Queue types](/infrastructure/resource/queues/#types)

2. [Queue subtypes](/infrastructure/resource/queues/#subtypes)

3. [Charge polices](/infrastructure/resource/queues/#charge-policies)


# Hardware Specifications

The following table contains hardware specifications of the above queues.

| Name  | CPU Type<sup>1</sup> | Cores/Node | GPU Type<sup>2</sup> | GPU/Node | Memory (GB) | Bandwidth (Gbps)  |
| :---: | :---:                | :---:      | :---:                | :---:    | :---:       | :---:             |
| D     | type-1               | 8          | -                    | -        | 56          | &le;10            |
| OR    | type-1               | 16         | -                    | -        | 112         | 10                |
| OR8   | type-1               | 8          | -                    | -        | 56          | &le;10            |
| OF    | type-1               | 16         | -                    | -        | 112         | 54.54<sup>3</sup> |
| SR    | type-1               | 16         | -                    | -        | 112         | 10                |
| SR8   | type-1               | 8          | -                    | -        | 56          | &le;10            |
| SF    | type-1               | 16         | -                    | -        | 112         | 54.54             |
| GPOF  | type-2               | 6          | type-2               | 1        | 112         | 10                |
| GP2OF | type-2               | 12         | type-2               | 2        | 224         | 10                |
| GP4OF | type-2               | 24         | type-2               | 4        | 448         | 10                |
| GPSF  | type-2               | 6          | type-2               | 1        | 112         | 10                |
| GP2SF | type-2               | 12         | type-2               | 2        | 224         | 10                |
| GP4SF | type-2               | 24         | type-2               | 4        | 448         | 10                |

**Notes**:

1. [CPU types](overview/#cpu-types)

2. [GPU types](overview/#gpu-types)

3. [Infiniband](#Links) interconnect network

# Links

- [Microsoft Azure](https://azure.microsoft.com/en-us/)
- [Infiniband-enabled](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes-hpc)
