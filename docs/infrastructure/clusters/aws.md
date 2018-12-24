# Amazon Web Services

This page contains information about clusters hosted on Amazon Web Services[^1] (AWS) and their hardware specifications.

## Clusters

The following table provides information about available clusters on Amazon Web Services (AWS) cloud computing platform. The latest cluster status can be found on <a href="https://platform.exabyte.io/clusters" target="_blank">Clusters</a> page in web application.

| Name        | Master Hostname                                   | Location |
| :---:       | :---:                                             | :---:    |
| cluster-001 | master-production-20160630-cluster-001.exabyte.io | West US  |

## Queues

The list of currently enabled queues is given below. Price per core hour is shown in relation to the [relative unit price](../../pricing/service-levels.md#comparison-table) and is subject to change at any time. Total number of nodes can be increased upon [request](../../ui/support.md).

| Name  | Category[^2] | Mode[^3] | Charge Policy[^4] | Price | Max Nodes per Job | Max Nodes Total |
| :---: | :---:        | :---:    | :---:             | :---:                   | :---:     | :---:     |
| D     | debug        | debug    | core-seconds      | 2.251                   | 1         | 10        |
| OR    | ordinary     | regular  | core-seconds      | 1.000                   | 1         | 10        |
| OR4   | ordinary     | regular  | core-seconds      | 1.126                   | 1         | 20        |
| OR8   | ordinary     | regular  | core-seconds      | 1.126                   | 1         | 20        |
| OR16  | ordinary     | regular  | core-seconds      | 1.126                   | 1         | 20        |
| OF    | ordinary     | fast     | core-hours        | 1.000                   | &le;50    | 100       |
| OF+   | ordinary     | fast     | core-hours        | 0.962                   | &le;10    | 10        |
| SR    | saving       | regular  | core-seconds      | 0.200                   | 1         | 10        |
| SR4   | saving       | regular  | core-seconds      | 0.225                   | 1         | 20        |
| SR8   | saving       | regular  | core-seconds      | 0.225                   | 1         | 20        |
| SR16  | saving       | regular  | core-seconds      | 0.225                   | 1         | 20        |
| SF    | saving       | fast     | core-hours        | 0.200                   | &le;50    | 100       |
| SF+   | saving       | fast     | core-hours        | 0.241                   | &le;10    | 10        |
| GOF   | ordinary     | fast     | core-hours        | 8.655                   | &le;10    | 10        |
| G4OF  | ordinary     | fast     | core-hours        | 8.655                   | &le;10    | 10        |
| G8OF  | ordinary     | fast     | core-hours        | 8.655                   | &le;10    | 10        |
| GSF   | saving       | fast     | core-hours        | 3.370                   | &le;10    | 10        |
| G4SF  | saving       | fast     | core-hours        | 4.158                   | &le;10    | 10        |
| G8SF  | saving       | fast     | core-hours        | 4.335                   | &le;10    | 10        |

## Hardware Specifications

The following table contains hardware specifications for the above queues. 

| Name  | CPU[^5]  | Cores per Node | GPU[^6] | GPU per Node | Memory (GB) | Bandwidth (Gbps) |
| :---: | :---:        | :---:      | :---:        | :---:    | :---:       | :---:            |
| D     | c-3          | 8          | -            | -        | 15          | &le;10           |
| OR    | c-3          | 36         | -            | -        | 60          | &le;10           |
| OR4   | c-3          | 4          | -            | -        | 7.5         | &le;10           |
| OR8   | c-3          | 8          | -            | -        | 15          | &le;10           |
| OR16  | c-3          | 16         | -            | -        | 30          | &le;10           |
| OF    | c-3          | 36         | -            | -        | 60          | 10               |
| OF+   | c-5          | 72         | -            | -        | 144         | 25               |
| SR    | c-3          | 36         | -            | -        | 60          | 10               |
| SR4   | c-3          | 4          | -            | -        | 7.5         | &le;10           |
| SR8   | c-3          | 8          | -            | -        | 15          | &le;10           |
| SR16  | c-3          | 16         | -            | -        | 30          | &le;10           |
| SF    | c-3          | 36         | -            | -        | 60          | 10               |
| SF+   | c-5          | 72         | -            | -        | 144         | 25               |
| GOF   | c-4          | 8          | g-1          | 1        | 61          | 10               |
| G4OF  | c-4          | 32         | g-1          | 4        | 244         | 10               |
| G8OF  | c-4          | 64         | g-1          | 8        | 488         | 25               |
| GSF   | c-4          | 8          | g-1          | 1        | 61          | 10               |
| G4SF  | c-4          | 32         | g-1          | 4        | 244         | 10               |
| G8SF  | c-4          | 64         | g-1          | 8        | 488         | 25               |


!!! note "Hyper-threading"
    Hyper-threading[^7] is enabled on all AWS compute nodes by default. It is recommended to use half of available cores on each compute node (e.g 18 cores on OF queue) if the application does not benefit from the extra virtual cores.

## Links

[^1]: [Amazon Web Services, Official Website](https://aws.amazon.com/)

[^2]: [Queue Cost Categories, Link](../resource/category.md#cost-categories)

[^3]: [Queue Provision Modes, Link](../resource/category.md#provision-modes)

[^4]: [Charge polices, Link](../resource/queues.md#charge-policies)

[^5]: [CPU types, Link](hardware.md#cpu-types)

[^6]: [GPU types, Link](hardware.md#gpu-types)

[^7]: [Wikipedia Hyper-threading, Website](https://en.wikipedia.org/wiki/Hyper-threading)

///FOOTNOTES GO HERE///
