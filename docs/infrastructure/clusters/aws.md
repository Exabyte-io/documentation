# Amazon Web Services Clusters

This page contains information about clusters hosted on Amazon Web Service[^1] (AWS) and their hardware specifications.

## Clusters

The following table provides information about available clusters on Amazon Web Service (AWS) cloud computing platform. The latest cluster status can be found on <a href="https://platform.exabyte.io/clusters" target="_blank">Clusters</a> page in web application.

| Name        | Master Hostname                                   | Location |
| :---:       | :---:                                             | :---:    |
| cluster-001 | master-production-20160630-cluster-001.exabyte.io | West US  |

## Queues

The list of currently enabled queues are given below.

| Name  | Category[^2] | Mode[^3] | Charge Policy[^4] | Price (Cents/Core*Hour) | Nodes/Job | Max Nodes |
| :---: | :---:        | :---:    | :---:             | :---:                   | :---:     | :---:     |
| D     | debug        | debug    | core-seconds      | 22.51                   | 1         | 10        |
| OR    | ordinary     | regular  | core-seconds      | 10.00                   | 1         | 10        |
| OR4   | ordinary     | regular  | core-seconds      | 11.26                   | 1         | 20        |
| OR8   | ordinary     | regular  | core-seconds      | 11.26                   | 1         | 20        |
| OR16  | ordinary     | regular  | core-seconds      | 11.26                   | 1         | 20        |
| OF    | ordinary     | fast     | core-hours        | 10.00                   | &le;50    | 100       |
| OF+   | ordinary     | fast     | core-hours        | 9.62                    | &le;50    | 10        |
| SR    | saving       | regular  | core-seconds      | 2.00                    | 1         | 10        |
| SR4   | saving       | regular  | core-seconds      | 2.25                    | 1         | 20        |
| SR8   | saving       | regular  | core-seconds      | 2.25                    | 1         | 20        |
| SR16  | saving       | regular  | core-seconds      | 2.25                    | 1         | 20        |
| SF    | saving       | fast     | core-hours        | 2.00                    | &le;50    | 100       |
| SF+   | saving       | fast     | core-hours        | 2.41                    | &le;50    | 10        |
| GOF   | ordinary     | fast     | core-hours        | 86.55                   | &le;50    | 10        |
| G4OF  | ordinary     | fast     | core-hours        | 86.55                   | &le;50    | 10        |
| G8OF  | ordinary     | fast     | core-hours        | 86.55                   | &le;50    | 10        |
| GSF   | saving       | fast     | core-hours        | 33.70                   | &le;50    | 10        |
| G4SF  | saving       | fast     | core-hours        | 41.58                   | &le;50    | 10        |
| G8SF  | saving       | fast     | core-hours        | 43.35                   | &le;50    | 10        |

## Hardware Specifications

The following table contains hardware specifications of the above queues. 

| Name  | CPU Type[^5] | Cores/Node | GPU Type[^6] | GPU/Node | Memory (GB) | Bandwidth (Gbps) |
| :---: | :---:        | :---:      | :---:        | :---:    | :---:       | :---:            |
| D     | c-3          | 8          | -            | -        | 15          | &le;10           |
| OR    | c-3          | 36         | -            | -        | 60          | &le;10           |
| OR4   | c-3          | 4          | -            | -        | 7.5         | &le;10           |
| OR8   | c-3          | 8          | -            | -        | 15          | &le;10           |
| OR16  | c-3          | 16         | -            | -        | 30          | &le;10           |
| OF    | c-3          | 36         | -            | -        | 60          | 10               |
| OF+   | c-3          | 72         | -            | -        | 144         | 25               |
| SR    | c-3          | 36         | -            | -        | 60          | 10               |
| SR4   | c-3          | 4          | -            | -        | 7.5         | &le;10           |
| SR8   | c-3          | 8          | -            | -        | 15          | &le;10           |
| SR16  | c-3          | 16         | -            | -        | 30          | &le;10           |
| SF    | c-3          | 36         | -            | -        | 60          | 10               |
| SF+   | c-3          | 72         | -            | -        | 144         | 25               |
| GOF   | c-4          | 8          | g-1          | 1        | 61          | 10               |
| G4OF  | c-4          | 32         | g-1          | 4        | 244         | 10               |
| G8OF  | c-4          | 64         | g-1          | 8        | 488         | 25               |
| GSF   | c-4          | 8          | g-1          | 1        | 61          | 10               |
| G4SF  | c-4          | 32         | g-1          | 4        | 244         | 10               |
| G8SF  | c-4          | 64         | g-1          | 8        | 488         | 25               |


!!! note "Hyper-threading"
    Hyper-threading[^7] is enabled on all AWS compute nodes by default. It is recommended to use half of available cores on each compute node (e.g 18 cores on OF queue) if the application does not benefit from the extra virtual cores.

## Links

[^1]: [Amazon Web Service](https://aws.amazon.com/)

[^2]: [Queue Cost Categories](/infrastructure/resource/category/#cost-categories)

[^3]: [Queue Provision Modes](/infrastructure/resource/category/#provision-modes)

[^4]: [Charge polices](/infrastructure/resource/queues/#charge-policies)

[^5]: [CPU types](overview/#cpu-types)

[^6]: [GPU types](overview/#gpu-types)

[^7]: [Hyper-threading, Wikipedia](https://en.wikipedia.org/wiki/Hyper-threading)

///FOOTNOTES GO HERE///
