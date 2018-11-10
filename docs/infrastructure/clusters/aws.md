# Clusters

The following table provides information about available clusters on [Amazon Web Service](#Links) (AWS) cloud computing platform. The latest cluster status can be found on [clusters](https://platform.exabyte.io/clusters) page in web application.

| Name        | Master Hostname                                   | Location |
| :---:       | :---:                                             | :---:    |
| cluster-001 | master-production-20160630-cluster-001.exabyte.io | West US  |

# Queues

The list of currently enabled queues are given below.

| Name  | Type<sup>1</sup> | Subtype<sup>2</sup> | Nodes/Job | Charge Policy<sup>3</sup> | Max Nodes | Price (Cents/Core*Hour) |
| :---: | :---:            | :---:               | :---:     | :---:                     | :---:     | :---:                   |
| D     | debug            | debug               | 1         | core-seconds              | 10        | 22.51                   |
| OR    | ordinary         | regular             | 1         | core-seconds              | 10        | 10.00                   |
| OR4   | ordinary         | regular             | 1         | core-seconds              | 20        | 11.26                   |
| OR8   | ordinary         | regular             | 1         | core-seconds              | 20        | 11.26                   |
| OR16  | ordinary         | regular             | 1         | core-seconds              | 20        | 11.26                   |
| OF    | ordinary         | fast                | &le;50    | core-hours                | 100       | 10.00                   |
| OF+   | ordinary         | fast                | &le;50    | core-hours                | 10        | 09.62                   |
| SR    | saving           | regular             | 1         | core-seconds              | 10        | 02.00                   |
| SR4   | saving           | regular             | 1         | core-seconds              | 20        | 02.25                   |
| SR8   | saving           | regular             | 1         | core-seconds              | 20        | 02.25                   |
| SR16  | saving           | regular             | 1         | core-seconds              | 20        | 02.25                   |
| SF    | saving           | fast                | &le;50    | core-hours                | 100       | 02.00                   |
| SF+   | saving           | fast                | &le;50    | core-hours                | 10        | 02.41                   |
| GOF   | ordinary         | fast                | &le;50    | core-hours                | 10        | 86.55                   |
| G4OF  | ordinary         | fast                | &le;50    | core-hours                | 10        | 86.55                   |
| G8OF  | ordinary         | fast                | &le;50    | core-hours                | 10        | 86.55                   |
| GSF   | saving           | fast                | &le;50    | core-hours                | 10        | 33.70                   |
| G4SF  | saving           | fast                | &le;50    | core-hours                | 10        | 41.58                   |
| G8SF  | saving           | fast                | &le;50    | core-hours                | 10        | 43.35                   |


**Notes**:

1. [Queue types](/infrastructure/resource/queues/#types)

2. [Queue subtypes](/infrastructure/resource/queues/#subtypes)

3. [Charge polices](/infrastructure/resource/queues/#charge-policies)


# Hardware Specifications

The following table contains hardware specifications of the above queues. 

| Name  | CPU Type<sup>1</sup> | Cores/Node | GPU Type<sup>2</sup> | GPU/Node | Memory (GB) | Bandwidth (Gbps) |
| :---: | :---:                | :---:      | :---:                | :---:    | :---:       | :---:            |
| D     | type-3               | 8          | -                    | -        | 15          | &le;10           |
| OR    | type-3               | 36         | -                    | -        | 60          | &le;10           |
| OR4   | type-3               | 4          | -                    | -        | 7.5         | &le;10           |
| OR8   | type-3               | 8          | -                    | -        | 15          | &le;10           |
| OR16  | type-3               | 16         | -                    | -        | 30          | &le;10           |
| OF    | type-3               | 36         | -                    | -        | 60          | 10               |
| OF+   | type-3               | 72         | -                    | -        | 144         | 25               |
| SR    | type-3               | 36         | -                    | -        | 60          | 10               |
| SR4   | type-3               | 4          | -                    | -        | 7.5         | &le;10           |
| SR8   | type-3               | 8          | -                    | -        | 15          | &le;10           |
| SR16  | type-3               | 16         | -                    | -        | 30          | &le;10           |
| SF    | type-3               | 36         | -                    | -        | 60          | 10               |
| SF+   | type-3               | 72         | -                    | -        | 144         | 25               |
| GOF   | type-4               | 8          | type-1               | 1        | 61          | 10               |
| G4OF  | type-4               | 32         | type-1               | 4        | 244         | 10               |
| G8OF  | type-4               | 64         | type-1               | 8        | 488         | 25               |
| GSF   | type-4               | 8          | type-1               | 1        | 61          | 10               |
| G4SF  | type-4               | 32         | type-1               | 4        | 244         | 10               |
| G8SF  | type-4               | 64         | type-1               | 8        | 488         | 25               |

**Notes**:

1. [CPU types](overview/#cpu-types)

2. [GPU types](overview/#gpu-types)


!!! note "Hyper-threading"
    [Hyper-threading](#Links) is enabled on all AWS compute nodes by default. It is recommended to use half of available cores on each compute node (e.g 18 cores on OF queue) if the application does not benefit from the extra virtual cores.

# Links

- [Amazon Web Service](https://aws.amazon.com/)
- [Hyper-threading](https://en.wikipedia.org/wiki/Hyper-threading)
